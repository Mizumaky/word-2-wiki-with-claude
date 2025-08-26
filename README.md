# Word to Wiki Converter

A Python application that converts Word documents (.docx) to HTML wiki format using Pandoc, with automatic header-based splitting and git versioning support.

## Features

- **Word to HTML Conversion**: Converts .docx files to clean HTML5 using Pandoc
- **Header-based Splitting**: Automatically splits documents by top-level headers into separate files
- **Media Extraction**: Extracts and properly references images, tables, and other media
- **Modern UI**: Beautiful HTML interface with tree navigation, theme switching, and diff comparison
- **Version Comparison**: Side-by-side diff highlighting between document versions
- **Git Integration**: Automatic versioning and commit functionality
- **Interactive Launcher**: Arrow-key navigation menu for easy operation
- **Standalone Mode**: Share individual HTML files that work without server

## Installation

1. **Prerequisites**:
   - Python 3.8+ (tested with Python 3.13)
   - Pandoc (install from https://pandoc.org/installing.html)

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Quick Start

### 🚀 Easy Launcher (Recommended)
Double-click **`Word2Wiki Launcher.bat`** (Windows) or run:
```bash
python interactive_launcher.py
```
This provides an interactive arrow-key menu for all operations including:
- Browse converted documents with HTTP server
- Convert documents with progress tracking  
- Clear and reset operations
- Advanced git integration
- Status monitoring

### 📋 Command Line Usage

Convert a Word document to HTML:
```bash
python main.py convert document.docx
```

This will:
- Convert `document.docx` to HTML
- Split by h1 headers into separate files
- Extract media to `output/media/` folder
- Create an index page with navigation

### Advanced Options

```bash
# Custom output directory and name
python main.py convert document.docx -o my_output -n my_document

# Don't split by headers (single file)
python main.py convert document.docx --no-split

# Split by h2 headers instead of h1
python main.py convert document.docx --header-level 2

# Auto-commit to git
python main.py convert document.docx --git-commit
```

### Git Integration

```bash
# Initialize git repository
python main.py init-git

# Check status
python main.py status

# Manual commit
python main.py commit output/*.html -m "Add converted documentation"
```

## Example Output

For a document with structure:
```
# Introduction
# Configuration  
# Implementation
```

The converter generates:
- `document_index.html` - Navigation index
- `document_01_introduction.html` - First section
- `document_02_configuration.html` - Second section  
- `document_03_implementation.html` - Third section
- `media/` folder with extracted images

## Requirements

- `pypandoc==1.13` - Python wrapper for Pandoc
- `click==8.1.7` - CLI framework
- `GitPython==3.1.40` - Git integration
- `beautifulsoup4==4.12.2` - HTML parsing
- `rich==13.7.0` - CLI output