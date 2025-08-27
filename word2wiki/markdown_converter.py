"""Markdown converter for Word documents with Obsidian compatibility."""

import re
import shutil
from pathlib import Path
from typing import List, Dict, Tuple, Optional
import pypandoc
from rich.console import Console

from .fs_parser import FSParser, FSDocument
from .version_utils import version_sort_key
from .console_utils import create_safe_console, safe_print


console = create_safe_console()


class MarkdownConverter:
    """Converts Word documents to Obsidian-compatible Markdown with navigation."""
    
    def __init__(self, output_dir: Path = Path("output_md")):
        """Initialize converter.
        
        Args:
            output_dir: Directory for Markdown output
        """
        self.output_dir = output_dir
        self.fs_parser = FSParser()
    
    def convert_document(self, document: FSDocument) -> List[Path]:
        """Convert a single Word document to Markdown files.
        
        Args:
            document: FSDocument to convert
            
        Returns:
            List of generated Markdown files
        """
        safe_print(console, f"Converting {document.display_name} to Markdown...", style="blue")
        
        # Create output directories - clean regeneration by default
        doc_dir = self.output_dir / document.base_name
        version_dir = doc_dir / f"v{document.full_version}"
        media_dir = version_dir / "media"
        
        # Clean existing version directory (preserve .obsidian)
        if version_dir.exists():
            for item in version_dir.iterdir():
                if item.name != ".obsidian":
                    if item.is_dir():
                        shutil.rmtree(item)
                    else:
                        item.unlink()
        
        doc_dir.mkdir(parents=True, exist_ok=True)
        version_dir.mkdir(parents=True, exist_ok=True)
        media_dir.mkdir(parents=True, exist_ok=True)
        
        # Convert to single Markdown file
        full_md = self._convert_to_markdown(document.path, version_dir, media_dir)
        
        # Tables are now processed at AST level via Lua filter during Pandoc conversion
        
        # Split into sections
        section_files = self._split_markdown_by_headers(full_md, version_dir)
        
        # Create version index
        index_file = self._create_version_index(section_files, document, version_dir)
        
        # Update document index
        self._update_document_index(document, doc_dir)
        
        # Update master index
        self._update_master_index()
        
        all_files = section_files + [index_file]
        safe_print(console, f"[green]Generated {len(all_files)} Markdown files[/green]")
        
        return all_files
    
    def _convert_to_markdown(self, docx_path: Path, output_dir: Path, media_dir: Path) -> Path:
        """Convert Word document to Markdown using Pandoc.
        
        Args:
            docx_path: Path to Word document
            output_dir: Directory for output
            media_dir: Directory for extracted media
            
        Returns:
            Path to generated Markdown file
        """
        output_path = output_dir / "full_document.md"
        
        try:
            # Get absolute path to Lua filter
            lua_filter = Path(__file__).parent.parent / "split-merged-cells.lua"
            
            # Pandoc options optimized to force pipe table output
            extra_args = [
                "--wrap=none",                           # No line wrapping
                "--markdown-headings=atx",               # Use ### style headers
                f"--extract-media={media_dir}",          # Extract images
                "--standalone",                          # Complete document
                f"--lua-filter={lua_filter}",            # Process merged cells at AST level
                "--to=markdown+pipe_tables-simple_tables-multiline_tables-grid_tables",  # Force pipe tables, keep raw_html as fallback
                "--columns=999",                         # Very wide columns to prefer pipe tables
            ]
            
            pypandoc.convert_file(
                str(docx_path),
                'markdown',
                outputfile=str(output_path),
                extra_args=extra_args,
                encoding='utf-8'
            )
            
            safe_print(console, f"[green]Converted to {output_path.name}[/green]")
            return output_path
            
        except Exception as e:
            safe_print(console, f"[red]Conversion failed: {e}[/red]")
            raise
    
    
    def _split_markdown_by_headers(self, md_file: Path, output_dir: Path) -> List[Path]:
        """Split Markdown file by H1 headers into separate files.
        
        Args:
            md_file: Full Markdown file
            output_dir: Directory for section files
            
        Returns:
            List of section file paths
        """
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split by H1 headers (# Header)
        sections = re.split(r'^# (.+)$', content, flags=re.MULTILINE)
        
        section_files = []
        if len(sections) > 1:
            # First section (before first header) - usually metadata
            if sections[0].strip():
                metadata_file = output_dir / "00_metadata.md"
                with open(metadata_file, 'w', encoding='utf-8') as f:
                    f.write(sections[0].strip())
                section_files.append(metadata_file)
            
            # Process header sections
            for i in range(1, len(sections), 2):
                if i + 1 < len(sections):
                    header = sections[i].strip()
                    section_content = sections[i + 1].strip()
                    
                    if header and section_content:
                        # Create filename from header
                        filename = self._create_filename(header, (i // 2) + 1)
                        section_file = output_dir / f"{filename}.md"
                        
                        # Write section with header
                        with open(section_file, 'w', encoding='utf-8') as f:
                            f.write(f"# {header}\n\n{section_content}")
                        
                        section_files.append(section_file)
        
        # Clean up full document file
        md_file.unlink(missing_ok=True)
        
        safe_print(console, f"[blue]Split into {len(section_files)} sections[/blue]")
        return section_files
    
    def _create_filename(self, header: str, index: int) -> str:
        """Create clean filename from header text.
        
        Args:
            header: Header text
            index: Section index
            
        Returns:
            Clean filename without extension
        """
        # Remove HTML tags and special chars, preserve Czech characters
        clean = re.sub(r'<[^>]+>', '', header)
        clean = re.sub(r'[^\w\s\-_áčďěíňóřšťúůýžÁČĎĚÍŇÓŘŠŤÚŮÝŽ]', '', clean)
        clean = re.sub(r'\s+', '_', clean.strip())
        clean = clean.lower()
        
        # Limit length and add index
        clean = clean[:40]
        return f"{index:02d}_{clean}".rstrip('_')
    
    def _create_version_index(self, section_files: List[Path], document: FSDocument, 
                            version_dir: Path) -> Path:
        """Create index file for this version.
        
        Args:
            section_files: List of section files
            document: Source document
            version_dir: Version directory
            
        Returns:
            Path to created index file
        """
        index_path = version_dir / "INDEX.md"
        
        # Extract headers from section files for navigation
        toc_entries = []
        for section_file in sorted(section_files):
            headers_with_levels = self._extract_headers_with_levels(section_file)
            if headers_with_levels:
                filename = section_file.stem
                
                # Main section as first-level list item
                main_header, main_level = headers_with_levels[0]
                emoji = self._get_section_emoji(main_header)
                
                # Clean up header text (remove Word styling artifacts)
                clean_main_header = self._clean_header_text(main_header)
                toc_entries.append(f"- [[{filename}|{emoji} {clean_main_header}]]")
                
                # Sub-headers with proper nesting relative to main (H1 = 0 indent, H2 = 2 spaces, etc.)
                for header_text, level in headers_with_levels[1:]:
                    # Clean header text
                    clean_header = self._clean_header_text(header_text)
                    
                    # Calculate indent: main_level+1 = 2 spaces, main_level+2 = 4 spaces, etc.
                    if level > main_level:
                        indent = "  " * (level - main_level)
                    else:
                        indent = "  "  # Default to one level if same or higher
                    
                    anchor = self._create_header_anchor(clean_header)
                    toc_entries.append(f"{indent}- [[{filename}#{anchor}|{clean_header}]]")
                
                toc_entries.append("")  # Empty line between sections
        
        # Get file modification time as readable date
        import datetime
        mod_time = datetime.datetime.fromtimestamp(document.path.stat().st_mtime)
        date_str = mod_time.strftime("%Y-%m-%d %H:%M:%S")
        
        # Create index content with YAML frontmatter
        index_content = f"""---
title: "{document.display_name} {document.version_display}"
version: "{document.version_display}"
base_name: "{document.base_name}"
generated: "{date_str}"
type: "version_index"
---

# {document.display_name} {document.version_display}

## Table of Contents

{chr(10).join(toc_entries)}

---
*Navigate back to [[../INDEX|📚 Document Versions]] or [[../../INDEX|🏠 Document Library]]*
"""
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)
        
        return index_path
    
    def _extract_headers(self, md_file: Path) -> List[str]:
        """Extract all headers from Markdown file.
        
        Args:
            md_file: Markdown file to analyze
            
        Returns:
            List of header texts
        """
        headers_with_levels = self._extract_headers_with_levels(md_file)
        return [header_text for header_text, level in headers_with_levels]
    
    def _extract_headers_with_levels(self, md_file: Path) -> List[Tuple[str, int]]:
        """Extract all headers from Markdown file with their levels.
        
        Args:
            md_file: Markdown file to analyze
            
        Returns:
            List of tuples (header_text, level) where level is 1-6
        """
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        headers = []
        lines = content.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            match = re.match(r'^(#{1,6})\s+(.+)$', line)
            if match:
                level = len(match.group(1))  # Count # characters
                header_text = match.group(2).strip()
                headers.append((header_text, level))
            elif line.startswith('####') and i + 1 < len(lines):
                # Handle case where #### is on separate line from header text
                next_line = lines[i + 1].strip()
                if next_line and not next_line.startswith('#'):
                    headers.append((next_line, 4))
        
        return headers
    
    def _clean_header_text(self, header: str) -> str:
        """Clean header text by removing Word styling artifacts.
        
        Args:
            header: Original header text
            
        Returns:
            Cleaned header text
        """
        # Remove Word styling like {#id .class}
        header = re.sub(r'\s*\{[^}]*\}', '', header)
        
        # Remove extra whitespace
        header = re.sub(r'\s+', ' ', header.strip())
        
        return header
    
    # Table processing now handled at AST level via Lua filter during Pandoc conversion
    
    def _create_header_anchor(self, header: str) -> str:
        """Create Obsidian-compatible header anchor.
        
        Args:
            header: Header text (should be cleaned first)
            
        Returns:
            Anchor string for linking
        """
        # Obsidian uses the header text directly as anchor
        return header
    
    def _get_section_emoji(self, header: str) -> str:
        """Get emoji for section based on header content.
        
        Args:
            header: Header text
            
        Returns:
            Appropriate emoji
        """
        header_lower = header.lower()
        
        if any(word in header_lower for word in ['obsah', 'content', 'table']):
            return '📋'
        elif any(word in header_lower for word in ['historie', 'history', 'změny']):
            return '📜'
        elif any(word in header_lower for word in ['úvod', 'intro', 'overview']):
            return '🔖'
        elif any(word in header_lower for word in ['model', 'domain', 'entit']):
            return '🏗️'
        elif any(word in header_lower for word in ['případy', 'use case', 'scénář']):
            return '⚡'
        elif any(word in header_lower for word in ['funkce', 'function', 'api']):
            return '🔧'
        elif any(word in header_lower for word in ['příloha', 'appendix', 'attachment']):
            return '📎'
        else:
            return '📄'
    
    def _update_document_index(self, document: FSDocument, doc_dir: Path):
        """Update or create document-level index.
        
        Args:
            document: Current document
            doc_dir: Document directory
        """
        # Find all versions for this document
        versions = []
        for version_dir in doc_dir.iterdir():
            if version_dir.is_dir() and version_dir.name.startswith('v'):
                index_path = version_dir / "INDEX.md"
                if index_path.exists():
                    versions.append(version_dir.name)
        
        # Sort versions
        versions.sort(key=lambda v: version_sort_key(v), reverse=True)
        
        # Create document index
        index_path = doc_dir / "INDEX.md"
        version_links = []
        
        for i, version in enumerate(versions):
            # Add special markers
            markers = []
            if i == 0:
                markers.append("⭐ Latest")
            if version.startswith('v') and version == f"v{document.full_version}":
                markers.append("🆕 Current")
            
            marker_text = f" {' '.join(markers)}" if markers else ""
            version_links.append(f"- [[{version}/INDEX|📄 {version}]]{marker_text}")
        
        content = f"""# {document.display_name}

## Available Versions ({len(versions)})

{chr(10).join(version_links)}

---
*Navigate back to [[../INDEX|🏠 Document Library]]*
"""
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def _update_master_index(self):
        """Update master index with all documents."""
        index_path = self.output_dir / "INDEX.md"
        
        # Find all document directories
        doc_entries = []
        for doc_dir in self.output_dir.iterdir():
            if doc_dir.is_dir() and doc_dir.name != "media":
                doc_index = doc_dir / "INDEX.md"
                if doc_index.exists():
                    # Count versions
                    version_count = len([d for d in doc_dir.iterdir() 
                                       if d.is_dir() and d.name.startswith('v')])
                    
                    doc_name = doc_dir.name.replace('_', ' ')
                    doc_entries.append(f"- [[{doc_dir.name}/INDEX|📚 {doc_name}]] ({version_count} versions)")
        
        content = f"""# Document Library

*Word to Markdown Conversion System*

## Available Documents ({len(doc_entries)})

{chr(10).join(sorted(doc_entries))}

---
*Generated by Word2Wiki Markdown Converter*
"""
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)