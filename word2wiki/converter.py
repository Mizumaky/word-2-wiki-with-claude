"""Core conversion functionality for Word to HTML conversion."""

from pathlib import Path
from typing import List, Optional, Dict, Any
import re
import pypandoc
from bs4 import BeautifulSoup
from rich.console import Console
from rich.progress import track

console = Console()


class WordToWikiConverter:
    """Converts Word documents to HTML wiki format using Pandoc."""
    
    def __init__(
        self,
        output_dir: Path = Path("output"),
        media_dir: str = "media",
        split_by_headers: bool = True,
        header_level: int = 1
    ):
        """Initialize the converter.
        
        Args:
            output_dir: Directory for output files
            media_dir: Directory name for extracted media
            split_by_headers: Whether to split by top-level headers
            header_level: Header level to split on (1 for h1, 2 for h2, etc.)
        """
        self.output_dir = Path(output_dir)
        self.media_dir = media_dir
        self.split_by_headers = split_by_headers
        self.header_level = header_level
        
        # Ensure output directory exists
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def convert_document(self, input_path: Path, output_name: Optional[str] = None) -> List[Path]:
        """Convert a Word document to HTML.
        
        Args:
            input_path: Path to the input Word document
            output_name: Base name for output files (defaults to input filename)
            
        Returns:
            List of generated HTML file paths
        """
        input_path = Path(input_path)
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")
            
        if output_name is None:
            output_name = input_path.stem
            
        console.print(f"Converting {input_path.name}...", style="blue")
        
        # Convert to single HTML file first
        html_path = self._convert_to_html(input_path, output_name)
        
        if self.split_by_headers:
            console.print("Splitting by headers...", style="blue")
            split_files = self._split_by_headers(html_path, output_name)
            
            # Create index page
            index_path = self._create_index_page(split_files, output_name)
            return [index_path] + split_files
        else:
            return [html_path]
    
    def _convert_to_html(self, input_path: Path, output_name: str) -> Path:
        """Convert Word document to HTML using Pandoc."""
        output_path = self.output_dir / f"{output_name}.html"
        media_path = str(self.output_dir / self.media_dir)
        
        try:
            # Use pypandoc to convert with media extraction
            pypandoc.convert_file(
                str(input_path),
                'html5',
                outputfile=str(output_path),
                extra_args=[
                    '--standalone',
                    f'--extract-media={media_path}',
                    '--embed-resources',
                    '--toc',
                    '--toc-depth=3'
                ]
            )
            console.print(f"✓ Created {output_path.name}", style="green")
            return output_path
            
        except Exception as e:
            console.print(f"✗ Conversion failed: {e}", style="red")
            raise
    
    def _split_by_headers(self, html_path: Path, base_name: str) -> List[Path]:
        """Split HTML file by top-level headers."""
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find all headers at the specified level
        header_tag = f'h{self.header_level}'
        headers = soup.find_all(header_tag)
        
        if not headers:
            console.print(f"No {header_tag} headers found, keeping as single file", style="yellow")
            return [html_path]
        
        console.print(f"Found {len(headers)} {header_tag} headers", style="blue")
        
        split_files = []
        
        for i, header in enumerate(track(headers, description="Creating sections...")):
            section_name = self._sanitize_filename(header.get_text().strip())
            section_filename = f"{base_name}_{i+1:02d}_{section_name}.html"
            section_path = self.output_dir / section_filename
            
            # Extract content for this section
            section_content = self._extract_section_content(soup, header, headers, i)
            
            # Create complete HTML document
            section_html = self._create_section_html(section_content, header.get_text().strip(), content)
            
            with open(section_path, 'w', encoding='utf-8') as f:
                f.write(section_html)
                
            split_files.append(section_path)
            console.print(f"✓ Created {section_filename}", style="green")
        
        return split_files
    
    def _extract_section_content(self, soup: BeautifulSoup, current_header, all_headers: List, header_index: int) -> str:
        """Extract content between current header and next header of same level."""
        # Find the next header at the same level
        next_header = all_headers[header_index + 1] if header_index + 1 < len(all_headers) else None
        
        # Collect all elements between current and next header
        content_elements = []
        current_element = current_header
        
        while current_element:
            content_elements.append(str(current_element))
            current_element = current_element.next_sibling
            
            # Stop if we reach the next header of the same level
            if (next_header and current_element and 
                hasattr(current_element, 'name') and 
                current_element == next_header):
                break
        
        return '\n'.join(content_elements)
    
    def _create_section_html(self, section_content: str, title: str, original_html: str) -> str:
        """Create a complete HTML document for a section."""
        # Extract head section from original HTML
        soup = BeautifulSoup(original_html, 'html.parser')
        head = soup.find('head')
        head_html = str(head) if head else '<head><meta charset="UTF-8"><title>Document Section</title></head>'
        
        # Update title
        head_html = head_html.replace('<title>.*?</title>', f'<title>{title}</title>')
        
        return f"""<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
{head_html}
<body>
{section_content}
</body>
</html>"""
    
    def _create_index_page(self, split_files: List[Path], base_name: str) -> Path:
        """Create an index page with links to all sections."""
        index_path = self.output_dir / f"{base_name}_index.html"
        
        index_html = f"""<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{base_name} - Index</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        h1 {{ color: #333; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin: 10px 0; }}
        a {{ text-decoration: none; color: #0066cc; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <h1>{base_name} - Table of Contents</h1>
    <ul>
"""
        
        for file_path in split_files:
            # Extract section title from filename
            filename = file_path.name
            # Remove base_name prefix and .html suffix, then clean up
            title = filename.replace(f"{base_name}_", "").replace(".html", "")
            title = re.sub(r'^\d+_', '', title).replace('_', ' ').title()
            
            index_html += f'        <li><a href="{filename}">{title}</a></li>\n'
        
        index_html += """    </ul>
</body>
</html>"""
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_html)
            
        console.print(f"✓ Created index page: {index_path.name}", style="green")
        return index_path
    
    def _sanitize_filename(self, text: str) -> str:
        """Sanitize text for use as filename."""
        # Remove HTML tags if any
        text = re.sub(r'<[^>]+>', '', text)
        # Replace special characters with underscores
        text = re.sub(r'[^\w\s-]', '', text)
        # Replace spaces and multiple underscores with single underscore
        text = re.sub(r'[\s_]+', '_', text)
        # Remove leading/trailing underscores and limit length
        return text.strip('_').lower()[:50]