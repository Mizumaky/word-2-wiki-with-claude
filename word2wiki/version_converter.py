"""Version-aware Word to HTML converter with diff capabilities."""

import json
import shutil
from pathlib import Path
from typing import List, Optional, Dict, Any
import re
import pypandoc
from bs4 import BeautifulSoup
from rich.console import Console
from rich.progress import track

from .fs_parser import FSDocument
from .console_utils import safe_print, safe_filename_display
from .version_utils import version_sort_key

console = Console()


class VersionAwareConverter:
    """Converts Word documents to HTML with version management and diff capabilities."""
    
    def __init__(
        self,
        base_output_dir: Path = Path("output"),
        split_by_headers: bool = True,
        header_level: int = 1
    ):
        """Initialize the version-aware converter.
        
        Args:
            base_output_dir: Base output directory
            split_by_headers: Whether to split by top-level headers
            header_level: Header level to split on (1 for h1, 2 for h2, etc.)
        """
        self.base_output_dir = Path(base_output_dir)
        self.split_by_headers = split_by_headers
        self.header_level = header_level
        
        # Ensure base output directory exists
        self.base_output_dir.mkdir(parents=True, exist_ok=True)
    
    def convert_document(self, document: FSDocument) -> List[Path]:
        """Convert an FS document to HTML with version management.
        
        Args:
            document: FSDocument to convert
            
        Returns:
            List of generated HTML file paths
        """
        console.print(f"Converting {document.path.name}...", style="blue")
        
        # Create document-specific directory structure
        doc_dir = self._get_document_directory(document)
        version_dir = self._get_version_directory(document)
        
        # Ensure directories exist
        doc_dir.mkdir(parents=True, exist_ok=True)
        version_dir.mkdir(parents=True, exist_ok=True)
        
        # Convert to single HTML file first
        temp_html = self._convert_to_html(document, version_dir)
        
        # Split by headers if requested
        if self.split_by_headers:
            console.print("Splitting by headers...", style="blue")
            split_files = self._split_by_headers(temp_html, document, version_dir)
            
            # Create version-specific index page
            version_index = self._create_version_index(split_files, document, version_dir)
            split_files.insert(0, version_index)
            
            # Clean up temporary file
            if temp_html.exists():
                temp_html.unlink()
        else:
            split_files = [temp_html]
        
        # Create/update document-wide version index
        doc_version_index = self._create_document_version_index(document, doc_dir)
        
        # Add diff capabilities to all HTML files
        self._enhance_html_with_diff_capabilities(split_files, document)
        
        # Save metadata
        self._save_version_metadata(document, version_dir, split_files)
        
        result_files = split_files + [doc_version_index]
        safe_print(console, f"Conversion completed", style="green")
        return result_files
    
    def _get_document_directory(self, document: FSDocument) -> Path:
        """Get the document-specific directory.
        
        Args:
            document: FSDocument
            
        Returns:
            Path to document directory
        """
        # Use display name for directory (clean, readable)
        doc_name = document.display_name.replace(' ', '_')
        return self.base_output_dir / doc_name
    
    def _get_version_directory(self, document: FSDocument) -> Path:
        """Get the version-specific directory.
        
        Args:
            document: FSDocument
            
        Returns:
            Path to version directory
        """
        doc_dir = self._get_document_directory(document)
        version_name = f"v{document.full_version}"
        return doc_dir / version_name
    
    def _convert_to_html(self, document: FSDocument, output_dir: Path) -> Path:
        """Convert Word document to HTML using Pandoc.
        
        Args:
            document: FSDocument to convert
            output_dir: Output directory for the HTML file
            
        Returns:
            Path to generated HTML file
        """
        output_path = output_dir / f"{document.base_name}.html"
        media_path = str(output_dir / "media")
        
        try:
            # Use pypandoc to convert with media extraction
            pypandoc.convert_file(
                str(document.path),
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
            safe_print(console, f"Created {safe_filename_display(output_path.name)}", style="green")
            return output_path
            
        except Exception as e:
            safe_print(console, f"Conversion failed: {e}", style="red")
            raise
    
    def _split_by_headers(self, html_path: Path, document: FSDocument, output_dir: Path) -> List[Path]:
        """Split HTML file by top-level headers.
        
        Args:
            html_path: Path to HTML file to split
            document: Original FSDocument
            output_dir: Directory for split files
            
        Returns:
            List of split file paths
        """
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
            section_filename = f"{document.base_name}_{i+1:02d}_{section_name}.html"
            section_path = output_dir / section_filename
            
            # Extract content for this section
            section_content = self._extract_section_content(soup, header, headers, i)
            
            # Create complete HTML document with enhanced template
            section_html = self._create_enhanced_section_html(
                section_content, 
                header.get_text().strip(), 
                content,
                document,
                i + 1
            )
            
            with open(section_path, 'w', encoding='utf-8') as f:
                f.write(section_html)
                
            split_files.append(section_path)
            safe_print(console, f"Created {safe_filename_display(section_filename)}", style="green")
        
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
    
    def _create_enhanced_section_html(self, section_content: str, title: str, original_html: str, 
                                    document: FSDocument, section_number: int) -> str:
        """Create an enhanced HTML document for a section with diff capabilities.
        
        Args:
            section_content: Content for this section
            title: Section title
            original_html: Original HTML content
            document: Source FSDocument
            section_number: Section number
            
        Returns:
            Complete HTML document string
        """
        # Extract head section from original HTML
        soup = BeautifulSoup(original_html, 'html.parser')
        head = soup.find('head')
        head_html = str(head) if head else '<head><meta charset="UTF-8"></head>'
        
        # Get available versions for comparison
        doc_dir = self._get_document_directory(document)
        available_versions = self._get_available_versions(doc_dir, document.full_version)
        
        # Generate version dropdown options
        version_options = ""
        for version in available_versions:
            selected = "selected" if version == f"v{document.full_version}" else ""
            version_options += f'<option value="{version}" {selected}>{version}</option>\n'
        
        return f"""<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - {document.display_name}</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css">
    <style>
        :root {{
            --pico-font-size: 16px;
            --pico-line-height: 1.5;
        }}

        /* Layout Structure */
        body {{
            margin: 0;
            padding: 0;
            padding-top: 60px; /* Space for floating header */
        }}

        /* Floating Top Bar */
        .top-bar {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: 60px;
            background: var(--pico-background-color);
            border-bottom: 1px solid var(--pico-muted-border-color);
            backdrop-filter: blur(10px);
            z-index: 1000;
            display: flex;
            align-items: center;
            padding: 0 1rem;
            gap: 1rem;
            transition: transform 0.3s ease;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}

        .top-bar.hidden {{
            transform: translateY(-100%);
        }}

        .top-bar .nav-buttons {{
            display: flex;
            gap: 0.5rem;
        }}

        .top-bar .nav-buttons button {{
            margin: 0;
            padding: 0.5rem 1rem;
        }}

        .top-bar .title {{
            flex: 1;
            font-weight: 600;
            margin: 0;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}

        .top-bar .controls {{
            display: flex;
            align-items: center;
            gap: 1rem;
        }}

        .top-bar .controls label {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin: 0;
            white-space: nowrap;
        }}

        .top-bar .controls select,
        .top-bar .controls input[type="checkbox"] {{
            margin: 0;
        }}

        /* Main Layout */
        .layout {{
            display: flex;
            min-height: calc(100vh - 60px);
        }}

        /* Left Sidebar - Modern 2025 Design */
        .sidebar {{
            width: 280px;
            background: var(--pico-background-color);
            border-right: 1px solid var(--pico-muted-border-color);
            height: calc(100vh - 60px);
            position: sticky;
            top: 60px;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }}

        /* Search Section */
        .sidebar-search {{
            padding: 1rem;
            border-bottom: 1px solid var(--pico-muted-border-color);
            background: var(--pico-card-background-color);
        }}

        .sidebar-search input {{
            width: 100%;
            padding: 0.5rem 0.75rem;
            border: 1px solid var(--pico-muted-border-color);
            border-radius: var(--pico-border-radius);
            background: var(--pico-background-color);
            color: var(--pico-color);
            font-size: 0.875rem;
            transition: border-color 0.2s;
        }}

        .sidebar-search input:focus {{
            outline: none;
            border-color: var(--pico-primary);
            box-shadow: 0 0 0 2px var(--pico-primary-background);
        }}

        .sidebar-search input::placeholder {{
            color: var(--pico-muted-color);
        }}

        /* Navigation Header */
        .sidebar-header {{
            padding: 1rem 1rem 0.5rem;
            background: var(--pico-card-background-color);
        }}

        .sidebar-header h4 {{
            margin: 0;
            color: var(--pico-color);
            font-size: 0.875rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}

        /* Scrollable Navigation Area */
        .sidebar-nav {{
            flex: 1;
            overflow-y: auto;
            padding: 0.5rem 1rem 1rem;
            background: var(--pico-card-background-color);
        }}

        .sidebar nav ul {{
            list-style: none;
            padding: 0;
            margin: 0;
        }}

        .sidebar nav li {{
            margin: 0;
        }}

        /* Modern Tree Navigation Item */
        .nav-item {{
            margin: 2px 0;
            border-radius: var(--pico-border-radius);
            overflow: hidden;
        }}

        .nav-item-header {{
            display: flex;
            align-items: center;
            width: 100%;
            padding: 0;
            margin: 0;
            background: none;
            border: none;
            cursor: pointer;
            border-radius: var(--pico-border-radius);
            transition: all 0.2s ease;
        }}

        .nav-item-header:hover {{
            background: var(--pico-secondary-background);
        }}

        .nav-toggle {{
            display: flex;
            align-items: center;
            justify-content: center;
            width: 24px;
            height: 24px;
            margin-right: 0.5rem;
            color: var(--pico-muted-color);
            font-size: 12px;
            border-radius: 3px;
            transition: all 0.2s ease;
            flex-shrink: 0;
        }}

        .nav-toggle:hover {{
            background: var(--pico-muted-border-color);
            color: var(--pico-color);
        }}

        .nav-toggle.expanded {{
            transform: rotate(90deg);
        }}

        .nav-link {{
            flex: 1;
            display: flex;
            align-items: center;
            padding: 0.5rem 0.75rem 0.5rem 0;
            text-decoration: none;
            color: var(--pico-color);
            font-size: 0.875rem;
            line-height: 1.4;
            border-radius: var(--pico-border-radius);
            transition: all 0.2s ease;
            min-height: 32px;
        }}

        .nav-link:hover {{
            color: var(--pico-primary);
            text-decoration: none;
        }}

        .nav-link.active {{
            color: var(--pico-primary);
            font-weight: 500;
            background: var(--pico-primary-background);
        }}

        /* Hierarchy Levels */
        .nav-link.h1 {{
            font-weight: 500;
            font-size: 0.9rem;
        }}

        .nav-link.h2 {{
            font-size: 0.85rem;
            margin-left: 1.5rem;
            color: var(--pico-muted-color);
        }}

        .nav-link.h3 {{
            font-size: 0.8rem;
            margin-left: 2.5rem;
            color: var(--pico-muted-color);
        }}

        /* Children Container */
        .nav-children {{
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease;
            margin-left: 24px;
        }}

        .nav-children.expanded {{
            max-height: 1000px;
        }}

        /* No Results State */
        .nav-no-results {{
            padding: 1rem;
            text-align: center;
            color: var(--pico-muted-color);
            font-size: 0.875rem;
            font-style: italic;
        }}

        /* Main Content */
        .main-content {{
            flex: 1;
            padding: 2rem;
            max-width: none;
            transition: max-width 0.3s ease;
        }}

        .main-content.narrow {{ max-width: 800px; margin: 0 auto; }}
        .main-content.wide {{ max-width: 1400px; margin: 0 auto; }}
        .main-content.standard {{ max-width: 1200px; margin: 0 auto; }}

        /* Right Sidebar - Modern Minimap */
        .minimap {{
            width: 80px;
            background: var(--pico-card-background-color);
            border-left: 1px solid var(--pico-muted-border-color);
            height: calc(100vh - 60px);
            position: sticky;
            top: 60px;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }}

        .minimap-header {{
            padding: 0.75rem 0.5rem;
            border-bottom: 1px solid var(--pico-muted-border-color);
            background: var(--pico-background-color);
        }}

        .minimap h4 {{
            font-size: 0.7rem;
            margin: 0;
            text-align: center;
            color: var(--pico-muted-color);
            font-weight: 500;
            writing-mode: vertical-rl;
            text-orientation: mixed;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .minimap-content {{
            flex: 1;
            position: relative;
            overflow: hidden;
            background: var(--pico-background-color);
        }}

        .minimap-viewport {{
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            background: rgba(0, 123, 255, 0.1);
            border: 1px solid rgba(0, 123, 255, 0.3);
            border-radius: 2px;
            min-height: 20px;
            transition: all 0.1s ease;
        }}

        [data-theme="dark"] .minimap-viewport {{
            background: rgba(100, 200, 255, 0.15);
            border-color: rgba(100, 200, 255, 0.4);
        }}

        /* Change Indicator Bar - Integrated with Minimap */
        .change-indicator {{
            position: absolute;
            top: 0;
            left: 4px;
            right: 4px;
            bottom: 0;
            pointer-events: none;
            z-index: 10;
        }}

        .change-mark {{
            position: absolute;
            left: 0;
            right: 0;
            height: 3px;
            border-radius: 1.5px;
            cursor: pointer;
            transition: all 0.2s ease;
            pointer-events: all;
        }}

        .change-mark.added {{
            background: #22c55e;
            box-shadow: 0 0 4px rgba(34, 197, 94, 0.4);
        }}

        .change-mark.modified {{
            background: #f59e0b;
            box-shadow: 0 0 4px rgba(245, 158, 11, 0.4);
        }}

        .change-mark.removed {{
            background: #ef4444;
            box-shadow: 0 0 4px rgba(239, 68, 68, 0.4);
        }}

        .change-mark:hover {{
            height: 5px;
            box-shadow: 0 0 8px currentColor;
        }}

        /* Modern Line-by-Line Diff Highlighting */
        .diff-line-added {{
            background: rgba(34, 197, 94, 0.15) !important;
            border-left: 3px solid #22c55e;
            padding-left: 1rem !important;
            margin: 2px 0;
        }}

        .diff-line-removed {{
            background: rgba(239, 68, 68, 0.15) !important;
            border-left: 3px solid #ef4444;
            padding-left: 1rem !important;
            margin: 2px 0;
            text-decoration: line-through;
            opacity: 0.8;
        }}

        .diff-line-modified {{
            background: rgba(245, 158, 11, 0.15) !important;
            border-left: 3px solid #f59e0b;
            padding-left: 1rem !important;
            margin: 2px 0;
        }}

        /* Dark theme adjustments */
        [data-theme="dark"] .diff-line-added {{
            background: rgba(34, 197, 94, 0.2) !important;
        }}

        [data-theme="dark"] .diff-line-removed {{
            background: rgba(239, 68, 68, 0.2) !important;
        }}

        [data-theme="dark"] .diff-line-modified {{
            background: rgba(245, 158, 11, 0.2) !important;
        }}

        /* Enhanced Table Styling */
        table {{ 
            border-collapse: collapse; 
            width: 100%; 
            margin: 2rem 0;
            background: var(--pico-card-background-color);
            border-radius: var(--pico-border-radius);
            overflow: hidden;
            box-shadow: var(--pico-card-box-shadow);
        }}

        table th, table td {{ 
            border: 1px solid var(--pico-muted-border-color);
            padding: 0.75rem;
            text-align: left;
            vertical-align: top;
        }}

        table td {{
            background-color: var(--pico-card-background-color);
        }}

        table th {{ 
            background: var(--pico-contrast);
            color: var(--pico-contrast-inverse);
            font-weight: 600;
            border-bottom: 2px solid var(--pico-muted-border-color);
            position: relative;
        }}

        /* High contrast table headers for both themes */
        [data-theme="dark"] table th {{
            background: #2a2a2a;
            color: #ffffff;
            border-color: #404040;
        }}

        [data-theme="light"] table th {{
            background: #f8f9fa;
            color: #212529;
            border-color: #dee2e6;
        }}

        table caption {{ 
            caption-side: top; 
            padding: 1rem; 
            font-weight: 600; 
            text-align: left;
            color: var(--pico-muted-color);
        }}

        /* Diff Styling - Light and Dark Mode Aware */
        .diff-added {{ 
            background: var(--pico-ins-color) !important; 
            color: var(--pico-contrast-color); 
            border: 2px solid #28a745 !important;
        }}

        .diff-removed {{ 
            background: var(--pico-del-color) !important; 
            color: var(--pico-contrast-color); 
            text-decoration: line-through; 
            border: 2px solid #dc3545 !important;
        }}

        .diff-modified {{
            background: var(--pico-mark-background-color) !important;
            color: var(--pico-mark-color) !important;
            border: 2px solid #ffc107 !important;
        }}

        /* Custom theme-aware variables */
        :root {{
            --diff-added-bg: #d4f6d4;
            --diff-added-color: #0d5016;
            --diff-removed-bg: #f8d7da;
            --diff-removed-color: #721c24;
            --diff-modified-bg: #fff3cd;
            --diff-modified-color: #856404;
        }}

        [data-theme="dark"] {{
            --diff-added-bg: #1a3d1a;
            --diff-added-color: #90ee90;
            --diff-removed-bg: #3d1a1a;
            --diff-removed-color: #ffb3b3;
            --diff-modified-bg: #3d3d1a;
            --diff-modified-color: #ffeb99;
        }}

        .diff-added {{ 
            background: var(--diff-added-bg) !important; 
            color: var(--diff-added-color) !important; 
            border: 2px solid #28a745 !important;
        }}

        .diff-removed {{ 
            background: var(--diff-removed-bg) !important; 
            color: var(--diff-removed-color) !important; 
            text-decoration: line-through; 
            border: 2px solid #dc3545 !important;
        }}

        .diff-modified {{
            background: var(--diff-modified-bg) !important;
            color: var(--diff-modified-color) !important;
            border: 2px solid #ffc107 !important;
        }}

        /* Improved dark mode colors */
        [data-theme="dark"] {{
            --pico-muted-color: #b3b3b3;
            --pico-color: #e0e0e0;
        }}

        /* Responsive Design */
        @media (max-width: 768px) {{
            .sidebar {{
                display: none;
            }}
            
            .top-bar .title {{
                font-size: 0.9rem;
            }}
            
            .top-bar .controls {{
                gap: 0.5rem;
            }}
            
            .top-bar .controls label {{
                font-size: 0.8rem;
            }}
            
            .change-indicator {{
                right: 10px;
                width: 8px;
            }}
        }}

        /* Dark mode enhancements */
        @media (prefers-color-scheme: dark) {{
            .change-indicator {{
                background: rgba(255,255,255,0.1);
            }}
        }}
    </style>
    <script src="https://cdn.jsdelivr.net/npm/diff@5.1.0/dist/diff.min.js"></script>
</head>
<body>
    <!-- Floating Top Bar -->
    <header class="top-bar" id="topBar">
        <div class="nav-buttons">
            <button onclick="goBack()">← Back</button>
            <button onclick="goToIndex()">📋 Index</button>
        </div>
        
        <h1 class="title">{document.display_name} - {title}</h1>
        
        <div class="controls">
            <label>
                <input type="checkbox" id="showChanges" onchange="toggleDiff()" role="switch">
                Show changes
            </label>
            
            <label>
                Version:
                <select id="versionSelect" onchange="loadVersionForComparison()">
                    {version_options}
                </select>
            </label>
            
            <label>
                Width:
                <select id="widthSelect" onchange="changeWidth()">
                    <option value="standard">Standard</option>
                    <option value="narrow">Narrow</option>
                    <option value="wide">Wide</option>
                    <option value="full">Full</option>
                </select>
            </label>
            
            <button id="themeToggle" onclick="toggleTheme()" title="Toggle theme" style="background: none; border: none; font-size: 1.2rem; cursor: pointer; padding: 0.5rem;">
                🌙
            </button>
        </div>
    </header>

    <!-- Main Layout -->
    <div class="layout">
        <!-- Left Sidebar -->
        <aside class="sidebar">
            <!-- Search Section -->
            <div class="sidebar-search">
                <input type="text" id="navSearch" placeholder="Search headings..." autocomplete="off">
            </div>
            
            <!-- Navigation Header -->
            <div class="sidebar-header">
                <h4>Contents</h4>
            </div>
            
            <!-- Scrollable Navigation Area -->
            <div class="sidebar-nav">
                <nav>
                    <ul id="sectionNav">
                        <!-- Will be populated by JavaScript -->
                    </ul>
                    <div id="navNoResults" class="nav-no-results" style="display: none;">
                        No matching headings found
                    </div>
                </nav>
            </div>
        </aside>

        <!-- Main Content -->
        <main class="main-content standard" id="mainContent">
            {section_content}
        </main>

        <!-- Right Sidebar - Modern Minimap -->
        <aside class="minimap" id="minimap">
            <div class="minimap-header">
                <h4>Overview</h4>
            </div>
            <div class="minimap-content">
                <div class="minimap-viewport" id="minimapViewport"></div>
                <div class="change-indicator" id="changeIndicator" style="display: none;">
                    <!-- Change marks will be populated by JavaScript -->
                </div>
            </div>
        </aside>
    </div>
    
    <script>
        // Document metadata
        const documentMetadata = {{
            baseName: "{document.base_name}",
            displayName: "{document.display_name}",
            version: "v{document.full_version}",
            sectionNumber: {section_number},
            sectionTitle: "{title}"
        }};
        
        let originalContent = document.getElementById('mainContent').outerHTML;
        let comparisonContent = null;
        
        // Test diff library on load
        function initializeDiff() {{
            if (typeof Diff === 'undefined') {{
                console.error('Diff library failed to load from CDN');
                const warningDiv = document.createElement('div');
                warningDiv.style.cssText = 'background: #fff3cd; color: #856404; padding: 10px; margin: 10px 0; border: 1px solid #ffeaa7; border-radius: 4px;';
                warningDiv.innerHTML = '⚠️ Diff comparison library failed to load. The "Show changes" feature may not work properly.';
                document.querySelector('.version-bar').appendChild(warningDiv);
                return false;
            }}
            console.log('Diff library loaded successfully');
            return true;
        }}
        
        // Initialize on page load
        window.addEventListener('load', function() {{
            initializeTheme();
            initializeDiff();
            initializeVersionControls();
            initializeNavigation();
            initializeScrollBehavior();
        }});
        
        function initializeVersionControls() {{
            console.log('Initializing version controls');
            const versionSelect = document.getElementById('versionSelect');
            const showChangesCheckbox = document.getElementById('showChanges');
            
            // Detect if running standalone (file:// protocol)
            const isStandalone = window.location.protocol === 'file:';
            const availableVersions = versionSelect.options.length;
            
            console.log('Protocol:', window.location.protocol);
            console.log('Is standalone:', isStandalone);
            console.log('Available versions:', availableVersions);
            
            if (isStandalone) {{
                // Running standalone - disable comparison features
                console.log('Standalone mode detected, disabling comparison features');
                versionSelect.disabled = true;
                showChangesCheckbox.disabled = true;
                showChangesCheckbox.checked = false;
                
                // Add standalone notice
                const notice = document.createElement('div');
                notice.style.cssText = 'background: #e3f2fd; color: #1565c0; padding: 8px 12px; margin: 0 1rem; border-radius: 4px; font-size: 0.8rem;';
                notice.innerHTML = '📄 Standalone mode - Version comparison disabled';
                document.querySelector('.top-bar .controls').appendChild(notice);
                
                // Hide version controls
                versionSelect.parentElement.style.display = 'none';
                showChangesCheckbox.parentElement.style.display = 'none';
            }} else if (availableVersions === 0) {{
                // Server mode but no versions to compare with - disable controls
                console.log('No comparison versions available, disabling controls');
                versionSelect.disabled = true;
                showChangesCheckbox.disabled = true;
                showChangesCheckbox.checked = false;
            }} else {{
                // At least one version available for comparison - enable controls
                console.log('Comparison versions available, enabling controls');
                versionSelect.disabled = false;
                showChangesCheckbox.disabled = false;
                showChangesCheckbox.checked = false; // Start unchecked
                
                // Pre-load the selected version for comparison
                loadVersionForComparison();
            }}
        }}
        
        function toggleDiff() {{
            console.log('toggleDiff() called');
            const showChanges = document.getElementById('showChanges').checked;
            console.log('showChanges checkbox value:', showChanges);
            const contentDiv = document.getElementById('mainContent');
            console.log('comparisonContent exists:', !!comparisonContent);
            
            if (showChanges && comparisonContent) {{
                console.log('Showing diff view');
                showDiffView(originalContent, comparisonContent);
                // Create change indicators after showing diff
                setTimeout(createChangeIndicators, 100);
            }} else {{
                console.log('Showing original content');
                contentDiv.innerHTML = originalContent;
                // Hide change indicators
                document.getElementById('changeIndicator').style.display = 'none';
            }}
        }}
        
        function loadVersionForComparison() {{
            console.log('loadVersionForComparison() called');
            const selectedVersion = document.getElementById('versionSelect').value;
            console.log('Selected version:', selectedVersion);
            console.log('Current version:', documentMetadata.version);
            if (selectedVersion === documentMetadata.version) {{
                console.log('Same version selected, clearing comparison');
                comparisonContent = null;
                toggleDiff();
                return;
            }}
            
            // Generate the correct filename using the same sanitization logic as the backend
            function sanitizeFilename(text) {{
                return text
                    .replace(/<[^>]+>/g, '') // Remove HTML tags
                    .replace(/[^\\p{{L}}\\p{{N}}\\s\\-_]/gu, '') // Remove non-letters/numbers but preserve Unicode letters
                    .replace(/[\\s_]+/g, '_') // Replace spaces/underscores with single underscore
                    .toLowerCase()
                    .substring(0, 50) // Limit length
                    .replace(/^_+|_+$/g, ''); // Remove leading/trailing underscores
            }}
            
            const sanitizedTitle = sanitizeFilename(documentMetadata.sectionTitle);
            const comparisonPath = `../${{selectedVersion}}/${{documentMetadata.baseName}}_${{String(documentMetadata.sectionNumber).padStart(2, '0')}}_${{sanitizedTitle}}.html`;
            
            console.log('Attempting to load:', comparisonPath);
            
            fetch(comparisonPath)
                .then(response => {{
                    if (!response.ok) {{
                        throw new Error(`HTTP ${{response.status}}: ${{response.statusText}}`);
                    }}
                    return response.text();
                }})
                .then(html => {{
                    const parser = new DOMParser();
                    const doc = parser.parseFromString(html, 'text/html');
                    const content = doc.getElementById('mainContent');
                    if (content) {{
                        comparisonContent = content.outerHTML;
                        console.log('Comparison content loaded successfully');
                        toggleDiff();
                    }} else {{
                        console.error('No mainContent found in comparison file');
                        comparisonContent = null;
                    }}
                }})
                .catch(error => {{
                    console.error('Error loading comparison version:', error);
                    console.error('Attempted path was:', comparisonPath);
                    comparisonContent = null;
                    
                    // Show user-friendly error
                    const errorMsg = `Could not load comparison version: ${{error.message}}\\n\\nPath: ${{comparisonPath}}\\n\\nNote: Make sure you're opening the HTML file directly in your browser, not through a web server.`;
                    alert(errorMsg);
                }});
        }}
        
        function showDiffView(original, comparison) {{
            if (!comparison) return;
            
            const contentDiv = document.getElementById('mainContent');
            
            if (typeof Diff !== 'undefined') {{
                console.log('Creating comprehensive diff view');
                try {{
                    // First, show the original content
                    contentDiv.innerHTML = original;
                    
                    // Create temporary elements to parse the HTML
                    const tempOriginal = document.createElement('div');
                    const tempComparison = document.createElement('div');
                    tempOriginal.innerHTML = original;
                    tempComparison.innerHTML = comparison;
                    
                    // Apply table-specific highlighting
                    const originalRows = Array.from(tempOriginal.querySelectorAll('tbody tr'));
                    const comparisonRows = Array.from(tempComparison.querySelectorAll('tbody tr'));
                    
                    if (originalRows.length > 0 || comparisonRows.length > 0) {{
                        console.log(`Comparing ${{originalRows.length}} vs ${{comparisonRows.length}} table rows`);
                        
                        if (originalRows.length !== comparisonRows.length) {{
                            highlightTableDifferences(original, comparison, contentDiv);
                        }} else {{
                            highlightCellDifferences(originalRows, comparisonRows, contentDiv, original);
                        }}
                    }}
                    
                    // Apply line-by-line text highlighting
                    highlightTextDifferences(tempOriginal, tempComparison, contentDiv);
                    
                }} catch (error) {{
                    console.error('Error creating diff:', error);
                    contentDiv.innerHTML = original;
                }}
            }} else {{
                console.warn('Diff library not loaded, using original content');
                contentDiv.innerHTML = original;
            }}
        }}
        
        function highlightTextDifferences(originalElement, comparisonElement, contentDiv) {{
            console.log('Applying line-by-line text highlighting');
            
            // Only compare actual document content, not template elements  
            // Now that we preserve outerHTML, we can use the specific selector
            const contentSelector = '#mainContent p, #mainContent li, #mainContent h1, #mainContent h2, #mainContent h3, #mainContent h4, #mainContent h5, #mainContent h6, #mainContent blockquote';
            
            // Get text-containing elements from document content only
            const originalTextElements = originalElement.querySelectorAll(contentSelector);
            const comparisonTextElements = comparisonElement.querySelectorAll(contentSelector);
            
            console.log(`Comparing ${{originalTextElements.length}} original elements vs ${{comparisonTextElements.length}} comparison elements`);
            
            // Create maps for comparison
            const originalTexts = Array.from(originalTextElements).map(el => el.textContent.trim()).filter(text => text.length > 0);
            const comparisonTexts = Array.from(comparisonTextElements).map(el => el.textContent.trim()).filter(text => text.length > 0);
            
            console.log(`Filtered to ${{originalTexts.length}} original texts vs ${{comparisonTexts.length}} comparison texts`);
            
            // Find corresponding elements in the rendered content
            const renderedElements = contentDiv.querySelectorAll(contentSelector);
            
            let changeCount = {{ added: 0, modified: 0, removed: 0 }};
            
            // Create a more sophisticated comparison
            const originalSet = new Set(originalTexts);
            const comparisonSet = new Set(comparisonTexts);
            
            // Find differences
            const addedTexts = originalTexts.filter(text => !comparisonSet.has(text));
            const removedTexts = comparisonTexts.filter(text => !originalSet.has(text));
            const commonTexts = originalTexts.filter(text => comparisonSet.has(text));
            
            // Apply highlighting to rendered elements
            Array.from(renderedElements).forEach(element => {{
                const elementText = element.textContent.trim();
                
                if (addedTexts.includes(elementText)) {{
                    // This content was added in the new version
                    element.classList.add('diff-line-added');
                    element.title = 'Added in this version';
                    changeCount.added++;
                }} else if (removedTexts.includes(elementText)) {{
                    // This shouldn't happen in original content, but for completeness
                    element.classList.add('diff-line-removed'); 
                    element.title = 'Removed in this version';
                    changeCount.removed++;
                }} else if (commonTexts.includes(elementText)) {{
                    // Check if position changed (simple heuristic for modification)
                    const originalIndex = originalTexts.indexOf(elementText);
                    const comparisonIndex = comparisonTexts.indexOf(elementText);
                    
                    if (Math.abs(originalIndex - comparisonIndex) > 2) {{
                        // Content moved significantly - mark as modified
                        element.classList.add('diff-line-modified');
                        element.title = 'Position changed in this version';
                        changeCount.modified++;
                    }}
                }}
            }});
            
            // Count removed items (for completeness in logging)
            changeCount.removed = removedTexts.length;
            
            console.log(`Text differences: ${{changeCount.added}} added, ${{changeCount.modified}} modified, ${{changeCount.removed}} removed`);
        }}
        
        function highlightTableDifferences(original, comparison, contentDiv) {{
            console.log('Highlighting table row differences');
            contentDiv.innerHTML = original;
            
            // Parse both versions to find the differences
            const tempOriginal = document.createElement('div');
            const tempComparison = document.createElement('div');
            tempOriginal.innerHTML = original;
            tempComparison.innerHTML = comparison;
            
            const originalRows = Array.from(tempOriginal.querySelectorAll('tbody tr'));
            const comparisonRows = Array.from(tempComparison.querySelectorAll('tbody tr'));
            
            console.log(`v${{documentMetadata.version}} has ${{originalRows.length}} rows vs comparison with ${{comparisonRows.length}} rows - ${{originalRows.length - comparisonRows.length}} new rows`);
            
            // Highlight the new rows (if there are more in original than comparison)
            if (originalRows.length > comparisonRows.length) {{
                const tableRows = contentDiv.querySelectorAll('tbody tr');
                const newRowsCount = originalRows.length - comparisonRows.length;
                console.log(`Highlighting ${{newRowsCount}} new rows (${{comparisonRows.length}} to ${{originalRows.length - 1}})`);
                
                for (let i = comparisonRows.length; i < originalRows.length; i++) {{
                    if (tableRows[i]) {{
                        tableRows[i].style.setProperty('background-color', '#d4edda', 'important');
                        tableRows[i].style.border = '3px solid #28a745';
                        tableRows[i].title = 'New row added in this version';
                        
                        // Apply background to all cells in the row
                        const cells = tableRows[i].querySelectorAll('td');
                        cells.forEach(cell => {{
                            cell.style.setProperty('background-color', '#d4edda', 'important');
                        }});
                    }}
                }}
            }}
        }}
        
        function highlightCellDifferences(originalRows, comparisonRows, contentDiv, originalHtml) {{
            console.log('Highlighting cell-level differences');
            contentDiv.innerHTML = originalHtml;
            
            // Find and highlight specific cell differences
            let differencesFound = false;
            const tableRows = contentDiv.querySelectorAll('tbody tr');
            
            originalRows.forEach((originalRow, rowIndex) => {{
                if (rowIndex < comparisonRows.length) {{
                    const comparisonRow = comparisonRows[rowIndex];
                    const originalCells = Array.from(originalRow.querySelectorAll('td'));
                    const comparisonCells = Array.from(comparisonRow.querySelectorAll('td'));
                    
                    originalCells.forEach((originalCell, cellIndex) => {{
                        if (cellIndex < comparisonCells.length) {{
                            const originalText = originalCell.textContent.trim();
                            const comparisonText = comparisonCells[cellIndex].textContent.trim();
                            
                            if (originalText !== comparisonText) {{
                                console.log(`Row ${{rowIndex}}, Cell ${{cellIndex}} differs`);
                                const actualCell = tableRows[rowIndex]?.querySelectorAll('td')[cellIndex];
                                if (actualCell) {{
                                    actualCell.style.backgroundColor = '#fff3cd';
                                    actualCell.style.border = '2px solid #ffc107';
                                    actualCell.title = `Changed from: "${{comparisonText}}"`;
                                    differencesFound = true;
                                }}
                            }}
                        }}
                    }});
                }}
            }});
            
            if (!differencesFound) {{
                const indicator = document.createElement('div');
                indicator.style.cssText = 'background: #d1ecf1; color: #0c5460; padding: 10px; margin: 10px 0; border: 1px solid #bee5eb; border-radius: 4px;';
                indicator.innerHTML = 'ℹ️ No significant content differences found between versions';
                contentDiv.insertBefore(indicator, contentDiv.firstChild);
            }}
        }}
        
        function changeWidth() {{
            const widthSelect = document.getElementById('widthSelect');
            const contentDiv = document.getElementById('mainContent');
            const selectedWidth = widthSelect.value;
            
            // Remove all width classes
            contentDiv.classList.remove('narrow', 'wide', 'full-width', 'standard');
            
            // Add the selected width class
            contentDiv.classList.add(selectedWidth);
            
            console.log('Width changed to:', selectedWidth);
        }}
        
        // Theme Toggle Functions
        function toggleTheme() {{
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            
            const themeButton = document.getElementById('themeToggle');
            themeButton.innerHTML = newTheme === 'dark' ? '☀️' : '🌙';
            
            console.log('Theme changed to:', newTheme);
        }}
        
        function initializeTheme() {{
            // Check for saved theme preference or default to system preference
            const savedTheme = localStorage.getItem('theme');
            const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
            
            let theme;
            if (savedTheme) {{
                theme = savedTheme;
            }} else {{
                theme = systemPrefersDark ? 'dark' : 'light';
            }}
            
            document.documentElement.setAttribute('data-theme', theme);
            const themeButton = document.getElementById('themeToggle');
            themeButton.innerHTML = theme === 'dark' ? '☀️' : '🌙';
            
            console.log('Theme initialized:', theme);
        }}
        
        // Navigation Functions
        function goBack() {{
            window.history.back();
        }}
        
        function goToIndex() {{
            window.location.href = 'index.html';
        }}
        
        // Modern Navigation System with Search
        function initializeNavigation() {{
            const nav = document.getElementById('sectionNav');
            const searchInput = document.getElementById('navSearch');
            const noResults = document.getElementById('navNoResults');
            const headers = document.querySelectorAll('#mainContent h1, #mainContent h2, #mainContent h3');
            
            let navigationData = [];
            let currentH1 = null;
            let currentH2 = null;
            
            // Build navigation data structure
            headers.forEach((header, index) => {{
                // Create anchor ID if it doesn't exist
                if (!header.id) {{
                    header.id = `section-${{index}}`;
                }}
                
                const level = parseInt(header.tagName.charAt(1));
                const navItem = {{
                    id: header.id,
                    text: header.textContent.trim(),
                    level: level,
                    element: header,
                    searchText: header.textContent.toLowerCase().trim()
                }};
                
                navigationData.push(navItem);
            }});
            
            // Render navigation tree
            function renderNavigation(items = navigationData) {{
                nav.innerHTML = '';
                noResults.style.display = items.length === 0 ? 'block' : 'none';
                
                let currentH1Container = null;
                let currentH2Container = null;
                
                items.forEach((item, index) => {{
                    const li = document.createElement('li');
                    li.className = 'nav-item';
                    
                    // Create item header container
                    const headerDiv = document.createElement('div');
                    headerDiv.className = 'nav-item-header';
                    
                    if (item.level === 1) {{
                        const hasChildren = items.some((child, childIndex) => 
                            childIndex > index && child.level === 2);
                        
                        if (hasChildren) {{
                            const toggle = document.createElement('div');
                            toggle.className = 'nav-toggle';
                            toggle.innerHTML = '▶';
                            toggle.onclick = (e) => {{
                                e.stopPropagation();
                                toggleNavSection(toggle, li);
                            }};
                            headerDiv.appendChild(toggle);
                        }} else {{
                            const spacer = document.createElement('div');
                            spacer.style.width = '24px';
                            headerDiv.appendChild(spacer);
                        }}
                        
                        const a = document.createElement('a');
                        a.href = `#${{item.id}}`;
                        a.textContent = item.text;
                        a.className = `nav-link h1`;
                        a.onclick = (e) => navigateToSection(e, item.element, a);
                        headerDiv.appendChild(a);
                        
                        li.appendChild(headerDiv);
                        
                        if (hasChildren) {{
                            const childrenContainer = document.createElement('div');
                            childrenContainer.className = 'nav-children';
                            li.appendChild(childrenContainer);
                            currentH2Container = childrenContainer;
                        }}
                        
                        nav.appendChild(li);
                        currentH1Container = li;
                        
                    }} else if (item.level === 2 && currentH2Container) {{
                        const h2Li = document.createElement('li');
                        h2Li.className = 'nav-item';
                        
                        const h2Header = document.createElement('div');
                        h2Header.className = 'nav-item-header';
                        
                        const spacer = document.createElement('div');
                        spacer.style.width = '24px';
                        h2Header.appendChild(spacer);
                        
                        const a = document.createElement('a');
                        a.href = `#${{item.id}}`;
                        a.textContent = item.text;
                        a.className = `nav-link h2`;
                        a.onclick = (e) => navigateToSection(e, item.element, a);
                        h2Header.appendChild(a);
                        
                        h2Li.appendChild(h2Header);
                        currentH2Container.appendChild(h2Li);
                        
                    }} else if (item.level === 3 && currentH2Container) {{
                        const h3Li = document.createElement('li');
                        h3Li.className = 'nav-item';
                        
                        const h3Header = document.createElement('div');
                        h3Header.className = 'nav-item-header';
                        
                        const spacer = document.createElement('div');
                        spacer.style.width = '24px';
                        h3Header.appendChild(spacer);
                        
                        const a = document.createElement('a');
                        a.href = `#${{item.id}}`;
                        a.textContent = item.text;
                        a.className = `nav-link h3`;
                        a.onclick = (e) => navigateToSection(e, item.element, a);
                        h3Header.appendChild(a);
                        
                        h3Li.appendChild(h3Header);
                        currentH2Container.appendChild(h3Li);
                    }}
                }});
                
                // Auto-expand first level
                const firstExpandable = nav.querySelector('.nav-toggle');
                if (firstExpandable) {{
                    const firstContainer = firstExpandable.parentElement.parentElement;
                    toggleNavSection(firstExpandable, firstContainer);
                }}
            }}
            
            // Search functionality
            searchInput.addEventListener('input', (e) => {{
                const query = e.target.value.toLowerCase().trim();
                
                if (query === '') {{
                    renderNavigation(navigationData);
                }} else {{
                    const filtered = navigationData.filter(item => 
                        item.searchText.includes(query));
                    renderNavigation(filtered);
                }}
            }});
            
            // Initial render
            renderNavigation();
            
            // Update active nav item on scroll
            window.addEventListener('scroll', updateActiveNavOnScroll);
            
            // Initialize minimap
            initializeMinimap();
        }}
        
        function checkForChildren(headers, currentIndex, targetLevel = null) {{
            const currentLevel = parseInt(headers[currentIndex].tagName.charAt(1));
            const checkLevel = targetLevel || (currentLevel + 1);
            
            for (let i = currentIndex + 1; i < headers.length; i++) {{
                const nextLevel = parseInt(headers[i].tagName.charAt(1));
                if (nextLevel <= currentLevel) break;
                if (nextLevel === checkLevel) return true;
            }}
            return false;
        }}
        
        function toggleNavSection(toggle, container) {{
            const childrenContainer = container.querySelector('.nav-children');
            if (!childrenContainer) return;
            
            const isExpanded = childrenContainer.classList.contains('expanded');
            
            if (isExpanded) {{
                childrenContainer.classList.remove('expanded');
                toggle.classList.remove('expanded');
                toggle.innerHTML = '▶';
            }} else {{
                childrenContainer.classList.add('expanded');
                toggle.classList.add('expanded');
                toggle.innerHTML = '▼';
            }}
        }}
        
        // Modern Minimap Implementation
        function initializeMinimap() {{
            const minimap = document.getElementById('minimap');
            const minimapViewport = document.getElementById('minimapViewport');
            const mainContent = document.getElementById('mainContent');
            
            if (!minimap || !minimapViewport || !mainContent) return;
            
            function updateMinimapViewport() {{
                const docHeight = document.documentElement.scrollHeight;
                const viewHeight = window.innerHeight;
                const scrollTop = window.pageYOffset;
                const minimapHeight = minimap.clientHeight - 100; // Account for header
                
                // Calculate viewport position and size
                const viewportTop = (scrollTop / docHeight) * minimapHeight;
                const viewportHeight = Math.max(20, (viewHeight / docHeight) * minimapHeight);
                
                minimapViewport.style.top = `${{viewportTop}}px`;
                minimapViewport.style.height = `${{viewportHeight}}px`;
            }}
            
            // Update on scroll and resize
            window.addEventListener('scroll', updateMinimapViewport);
            window.addEventListener('resize', updateMinimapViewport);
            
            // Click to navigate
            const minimapContent = minimap.querySelector('.minimap-content');
            minimapContent.addEventListener('click', (e) => {{
                const rect = minimapContent.getBoundingClientRect();
                const clickY = e.clientY - rect.top;
                const minimapHeight = minimapContent.clientHeight;
                const scrollPercent = clickY / minimapHeight;
                const targetScroll = scrollPercent * (document.documentElement.scrollHeight - window.innerHeight);
                
                window.scrollTo({{ top: Math.max(0, targetScroll), behavior: 'smooth' }});
            }});
            
            // Initial update
            updateMinimapViewport();
        }}
        
        function navigateToSection(e, header, link) {{
            e.preventDefault();
            header.scrollIntoView({{ behavior: 'smooth' }});
            updateActiveNavItem(link);
        }}
        
        function updateActiveNavItem(activeLink) {{
            document.querySelectorAll('#sectionNav a').forEach(link => {{
                link.classList.remove('active');
            }});
            activeLink.classList.add('active');
        }}
        
        function updateActiveNavOnScroll() {{
            const headers = document.querySelectorAll('#mainContent h1, #mainContent h2, #mainContent h3');
            const navLinks = document.querySelectorAll('#sectionNav a');
            
            let current = '';
            headers.forEach(header => {{
                const rect = header.getBoundingClientRect();
                if (rect.top <= 100) {{
                    current = header.id;
                }}
            }});
            
            navLinks.forEach(link => {{
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${{current}}`) {{
                    link.classList.add('active');
                }}
            }});
        }}
        
        // Floating Top Bar Scroll Behavior
        let lastScrollTop = 0;
        let scrollTimeout;
        
        function initializeScrollBehavior() {{
            const topBar = document.getElementById('topBar');
            
            window.addEventListener('scroll', function() {{
                const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
                
                // Clear any existing timeout
                clearTimeout(scrollTimeout);
                
                // Hide/show logic
                if (scrollTop > lastScrollTop && scrollTop > 60) {{
                    // Scrolling down & past header height
                    topBar.classList.add('hidden');
                }} else {{
                    // Scrolling up or at top
                    topBar.classList.remove('hidden');
                }}
                
                lastScrollTop = scrollTop;
                
                // Update change indicators if visible
                updateChangeIndicators();
            }}, {{ passive: true }});
        }}
        
        // Change Indicator Functions
        function updateChangeIndicators() {{
            const indicator = document.getElementById('changeIndicator');
            if (!indicator.style.display || indicator.style.display === 'none') return;
            
            // Get document dimensions
            const docHeight = document.documentElement.scrollHeight;
            const viewHeight = window.innerHeight;
            const scrollTop = window.pageYOffset;
            
            // Update existing change marks
            const marks = indicator.querySelectorAll('.change-mark');
            marks.forEach(mark => {{
                const targetId = mark.dataset.target;
                const targetElement = document.getElementById(targetId);
                if (targetElement) {{
                    const elementTop = targetElement.offsetTop;
                    const percentage = (elementTop / docHeight) * 100;
                    mark.style.top = `${{percentage}}%`;
                }}
            }});
        }}
        
        function createChangeIndicators() {{
            const indicator = document.getElementById('changeIndicator');
            const minimapContent = document.querySelector('.minimap-content');
            
            if (!indicator || !minimapContent) return;
            
            indicator.innerHTML = ''; // Clear existing marks
            
            // Find all changed elements
            const addedElements = document.querySelectorAll('.diff-line-added, tr[style*="background-color: #d4edda"]');
            const modifiedElements = document.querySelectorAll('.diff-line-modified, td[style*="background-color: #fff3cd"]');
            const removedElements = document.querySelectorAll('.diff-line-removed');
            
            const docHeight = document.documentElement.scrollHeight;
            const minimapHeight = minimapContent.clientHeight;
            
            // Helper function to create change marks
            function createChangeMark(element, type, index) {{
                const mark = document.createElement('div');
                mark.className = `change-mark ${{type}}`;
                mark.dataset.target = element.id || `${{type}}-${{index}}`;
                
                if (!element.id) {{
                    element.id = `${{type}}-${{index}}`;
                }}
                
                const elementTop = element.offsetTop;
                const percentage = (elementTop / docHeight) * minimapHeight;
                mark.style.top = `${{Math.max(0, Math.min(minimapHeight - 3, percentage))}}px`;
                
                // Set titles
                const titles = {{
                    added: 'Added content',
                    modified: 'Modified content', 
                    removed: 'Removed content'
                }};
                mark.title = titles[type] || element.title || `${{type}} content`;
                
                // Click to scroll to element
                mark.addEventListener('click', (e) => {{
                    e.stopPropagation();
                    element.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                }});
                
                return mark;
            }}
            
            // Create marks for added elements
            addedElements.forEach((element, index) => {{
                const mark = createChangeMark(element, 'added', index);
                indicator.appendChild(mark);
            }});
            
            // Create marks for modified elements
            modifiedElements.forEach((element, index) => {{
                const mark = createChangeMark(element, 'modified', index);
                indicator.appendChild(mark);
            }});
            
            // Create marks for removed elements
            removedElements.forEach((element, index) => {{
                const mark = createChangeMark(element, 'removed', index);
                indicator.appendChild(mark);
            }});
            
            const totalChanges = addedElements.length + modifiedElements.length + removedElements.length;
            
            // Show indicator if there are changes
            if (totalChanges > 0) {{
                indicator.style.display = 'block';
                console.log(`Created ${{totalChanges}} change indicators (${{addedElements.length}} added, ${{modifiedElements.length}} modified, ${{removedElements.length}} removed)`);
            }} else {{
                indicator.style.display = 'none';
            }}
        }}
    </script>
</body>
</html>"""
    
    def _create_version_index(self, split_files: List[Path], document: FSDocument, version_dir: Path) -> Path:
        """Create an index page for this specific version.
        
        Args:
            split_files: List of split HTML files
            document: Source FSDocument
            version_dir: Version directory
            
        Returns:
            Path to created index file
        """
        index_path = version_dir / "index.html"
        
        # Create navigation links
        nav_links = ""
        for i, file_path in enumerate(split_files):
            filename = file_path.name
            # Extract section title from filename
            title = filename.replace(f"{document.base_name}_", "").replace(".html", "")
            title = re.sub(r'^\d+_', '', title).replace('_', ' ').title()
            nav_links += f'        <li><a href="{filename}">{title}</a></li>\n'
        
        index_html = f"""<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{document.display_name} - v{document.full_version}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        h1 {{ color: #333; }}
        .version-info {{ background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 20px 0; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin: 10px 0; }}
        a {{ text-decoration: none; color: #0066cc; }}
        a:hover {{ text-decoration: underline; }}
        .navigation {{ margin-top: 30px; padding-top: 20px; border-top: 1px solid #eee; }}
    </style>
</head>
<body>
    <h1>{document.display_name}</h1>
    
    <div class="version-info">
        <strong>Version:</strong> {document.version_display}<br>
        <strong>Sections:</strong> {len(split_files)}<br>
        <strong>Generated:</strong> <span id="timestamp"></span>
    </div>
    
    <h2>Table of Contents</h2>
    <ul>
{nav_links}    </ul>
    
    <div class="navigation">
        <a href="../version_index.html">All Versions</a>
    </div>
    
    <script>
        document.getElementById('timestamp').textContent = new Date().toLocaleString();
    </script>
</body>
</html>"""
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_html)
            
        safe_print(console, f"Created version index: {safe_filename_display(index_path.name)}", style="green")
        return index_path
    
    def _create_document_version_index(self, document: FSDocument, doc_dir: Path) -> Path:
        """Create or update the main version index for the document.
        
        Args:
            document: Current FSDocument
            doc_dir: Document directory
            
        Returns:
            Path to version index file
        """
        index_path = doc_dir / "version_index.html"
        
        # Get all available versions
        available_versions = self._get_all_available_versions(doc_dir)
        current_version = f"v{document.full_version}"
        
        # Create version links
        version_links = ""
        for version in available_versions:
            is_current = version == current_version
            style = "font-weight: bold;" if is_current else ""
            status = " (Current)" if is_current else ""
            version_links += f'        <li><a href="{version}/index.html" style="{style}">{version}{status}</a></li>\n'
        
        index_html = f"""<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{document.display_name} - All Versions</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        h1 {{ color: #333; }}
        .current-version {{ background: #d4edda; padding: 15px; border-radius: 5px; margin: 20px 0; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin: 15px 0; padding: 10px; background: #f8f9fa; border-radius: 5px; }}
        a {{ text-decoration: none; color: #0066cc; font-size: 18px; }}
        a:hover {{ text-decoration: underline; }}
        .version-count {{ color: #666; margin-top: 20px; }}
    </style>
</head>
<body>
    <h1>{document.display_name}</h1>
    <h2>Version History</h2>
    
    <div class="current-version">
        <strong>Latest Version:</strong> {document.version_display}
    </div>
    
    <ul>
{version_links}    </ul>
    
    <div class="version-count">
        Total versions: {len(available_versions)}
    </div>
    
    <script>
        // Auto-refresh every 30 seconds to pick up new versions
        setTimeout(() => location.reload(), 30000);
    </script>
</body>
</html>"""
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_html)
            
        safe_print(console, f"Updated document version index", style="green")
        return index_path
    
    def _get_available_versions(self, doc_dir: Path, exclude_version: Optional[str] = None) -> List[str]:
        """Get list of available versions for comparison.
        
        Args:
            doc_dir: Document directory
            exclude_version: Version to exclude from list
            
        Returns:
            List of version strings
        """
        if not doc_dir.exists():
            return []
        
        versions = []
        for version_dir in doc_dir.iterdir():
            if version_dir.is_dir() and version_dir.name.startswith('v'):
                if exclude_version is None or version_dir.name != f"v{exclude_version}":
                    versions.append(version_dir.name)
        
        return sorted(versions, key=version_sort_key, reverse=True)
    
    def _get_all_available_versions(self, doc_dir: Path) -> List[str]:
        """Get all available versions including current.
        
        Args:
            doc_dir: Document directory
            
        Returns:
            List of all version strings
        """
        if not doc_dir.exists():
            return []
        
        versions = []
        for version_dir in doc_dir.iterdir():
            if version_dir.is_dir() and version_dir.name.startswith('v'):
                versions.append(version_dir.name)
        
        return sorted(versions, key=version_sort_key, reverse=True)
    
    def _enhance_html_with_diff_capabilities(self, html_files: List[Path], document: FSDocument):
        """Add diff capabilities to HTML files (if needed for additional enhancements).
        
        Args:
            html_files: List of HTML files to enhance
            document: Source FSDocument
        """
        # This method can be used for additional HTML enhancements if needed
        # Currently, diff capabilities are built into the template
        pass
    
    def _save_version_metadata(self, document: FSDocument, version_dir: Path, output_files: List[Path]):
        """Save metadata about this version.
        
        Args:
            document: Source FSDocument
            version_dir: Version directory
            output_files: List of generated files
        """
        metadata = {
            "document_name": document.display_name,
            "base_name": document.base_name,
            "version": document.full_version,
            "version_display": document.version_display,
            "source_file": str(document.path),
            "generated_files": [str(f) for f in output_files],
            "generation_time": str(document.path.stat().st_ctime),
            "split_by_headers": self.split_by_headers,
            "header_level": self.header_level
        }
        
        metadata_path = version_dir / "metadata.json"
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)
    
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