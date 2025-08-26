# Word-2-Wiki-with-Claude Project Memory

## Project Overview
This is a Python application that converts Word documents (.docx) to HTML wiki format using Pandoc. The project provides:

- Word to HTML conversion with clean HTML5 output
- **Modern HTML UI** with Pico CSS framework, tree navigation, theme switching
- **Version comparison** with intelligent diff highlighting 
- Header-based document splitting (configurable h1/h2 levels)  
- Media extraction and proper referencing
- **Interactive launcher** with arrow-key menu navigation
- **Standalone HTML** files that work without server
- Git integration for versioning
- Rich CLI interface

## Current State (Updated 2025-08-22)
- ✅ **Modern UI Completed**: Hierarchical tree navigation, theme toggle, diff comparison
- ✅ **Interactive Launcher**: questionary-based menu with arrow key navigation
- ✅ **Standalone Detection**: HTML files detect file:// protocol and disable comparison features
- ✅ **File Cleanup**: Removed unused launchers, empty directories, debug files
- Core conversion functionality implemented in `word2wiki/` package
- CLI interface via `main.py` and `word2wiki/cli.py`
- Test output shows successful conversion of Czech billing documentation
- **29 HTML files** generated with full modern UI functionality

## Key Files
- `main.py` - Entry point
- **`interactive_launcher.py`** - **NEW** Modern arrow-key menu launcher  
- **`Word2Wiki Launcher.bat`** - **NEW** Double-click Windows launcher
- `word2wiki/converter.py` - Core conversion logic
- `word2wiki/cli.py` - Command line interface
- **`word2wiki/version_converter.py`** - **ENHANCED** Modern HTML template with full UI
- `word2wiki/version_utils.py` - Shared version comparison utilities
- `word2wiki/fs_parser.py` - FS document naming pattern parser
- `word2wiki/git_manager.py` - Git integration
- **`SHARING.md`** - **NEW** Complete sharing guide for coworkers
- `requirements.txt` - Python dependencies

## Dependencies
- pypandoc==1.13 (Pandoc wrapper)
- click==8.1.7 (CLI framework)  
- GitPython==3.1.40 (Git integration)
- beautifulsoup4==4.12.2 (HTML parsing)
- rich==13.7.0 (CLI output)
- **questionary==2.1.0** - **NEW** Interactive CLI menus

## Test Data
- Source document: `FS_source/HR_FS_Billing_Accounts_Receivables_CZ_00_03_at_2025_08_21.docx`
- Generated 14 HTML files in `output/` directory
- Media files extracted to nested `media/` folders

## Commands Available
```bash
python main.py convert document.docx           # Basic conversion
python main.py convert document.docx --no-split # Single file output
python main.py convert document.docx --header-level 2  # Split on h2
python main.py convert-all                     # **NEW** Convert all documents
python main.py convert-all --skip-existing     # **NEW** Only convert new documents
python main.py clear                           # **NEW** Remove all converted files
python main.py clear --force                   # **NEW** Clear without confirmation
python main.py reset                           # **NEW** Clear + convert all (clean rebuild)
python main.py browse                          # Open converted docs in browser
python main.py status                          # Check conversion status
python main.py init-git                        # Initialize git
python main.py commit files -m "message"      # Commit files
```

## Recent Work Completed (2025-08-22)

### COMPLETED: Modern UI with Full Functionality ✅
- **Modern HTML Interface**: Complete redesign using Pico CSS framework
- **Hierarchical Tree Navigation**: Left sidebar with expand/collapse headers
- **Theme Switching**: Dark/Light mode toggle with persistent storage
- **Diff Comparison**: Intelligent table row comparison with highlighting
- **Right Minimap**: VS Code-style change indicators (fixed position)
- **Responsive Design**: Mobile-friendly layout with proper breakpoints
- **Files Modified**: `word2wiki/version_converter.py` - Complete template overhaul

### ADDED: Interactive Launcher System ✅
- **`interactive_launcher.py`**: Modern questionary-based menu with arrow key navigation
- **`Word2Wiki Launcher.bat`**: Double-click Windows launcher with dependency checking
- **Smart Error Handling**: Proper detection of file locks, server conflicts
- **Server Management**: Automatic HTTP server startup/shutdown for browsing
- **Clean UI**: Appropriate use of colors (green=success, red=error) without emoji spam
- **Files Added**: Complete launcher ecosystem for easy coworker sharing

### IMPLEMENTED: Standalone HTML Support ✅
- **Protocol Detection**: Automatically detects `file://` vs `http://` protocol  
- **Graceful Degradation**: Disables comparison features when running standalone
- **User Feedback**: Shows "Standalone mode - Version comparison disabled" notice
- **Full Compatibility**: All other features (navigation, themes, width) work standalone
- **Files Modified**: `word2wiki/version_converter.py` - Added standalone detection logic

### FIXED: Unicode Character Handling ✅
- **Problem**: Czech characters (ú, é, ř) were being stripped from filenames
- **Solution**: Updated regex to preserve Unicode letters: `/[^\p{L}\p{N}\s\-_]/gu`
- **Result**: Filenames now correctly preserve Czech characters in navigation

### CLEANED: Project Structure ✅
- **Removed**: `launcher.py`, `start.py`, `debug_diff.html`, `test_output.html`
- **Removed**: Empty `templates/` and `tests/` directories  
- **Updated**: All documentation to reflect new launcher system
- **Added**: `SHARING.md` - Complete guide for sharing with coworkers

## Current Status
- ✅ **Full Modern UI**: All features working (tree nav, themes, diff, minimap)
- ✅ **Two Sharing Modes**: Full project + Standalone HTML files
- ✅ **Interactive Launcher**: Arrow-key menu with proper error handling  
- ✅ **Clean Codebase**: Removed unused files, polished remaining code
- ✅ **Complete Documentation**: README, SHARING.md, and CLAUDE.md updated

## Architecture Summary
- **Server Mode** (Full Project): HTTP server enables cross-file loading for version comparison
- **Standalone Mode** (Individual Files): file:// protocol limitations disable comparison features
- **Smart Detection**: JavaScript automatically detects protocol and adjusts UI accordingly
- **Easy Sharing**: Double-click launcher makes deployment to coworkers trivial