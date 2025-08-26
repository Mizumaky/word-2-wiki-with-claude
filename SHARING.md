# Sharing Word2Wiki Projects

This document explains how to share Word2Wiki projects with coworkers and the different modes available.

## 🚀 Quick Start for Coworkers

### Option 1: Full Project Sharing (Recommended)
1. **Share the entire project folder** with coworkers
2. **Double-click `Word2Wiki Launcher.bat`** (Windows) or run `python launcher.py`
3. **Select option 1** "Browse converted documents" from the menu
4. **Full functionality** including version comparison and diff features

### Option 2: Standalone HTML Files
1. **Share individual HTML files** from the `output/` directory
2. **Double-click any HTML file** to open in browser
3. **Limited functionality** - no version comparison, but all other features work

## 📋 Requirements

### For Full Project Sharing:
- **Python 3.8+** installed on target machine
- **Internet connection** (for automatic dependency installation)
- **All files** in the project directory

### For Standalone HTML Files:
- **Just a web browser** - no Python required!
- **Single HTML file** can be shared via email, USB, etc.

## 🔧 Setup Instructions

### First-Time Setup (Full Project):
1. Install Python 3.8+ from [python.org](https://python.org)
2. ✅ **Check "Add Python to PATH"** during installation
3. Double-click `Word2Wiki Launcher.bat` - dependencies install automatically

### No Setup Required (Standalone):
- Just open any HTML file in your browser
- Modern browsers (Chrome, Firefox, Safari, Edge) all supported

## 🎯 Feature Comparison

| Feature | Full Project | Standalone HTML |
|---------|-------------|-----------------|
| 📖 Document viewing | ✅ Full | ✅ Full |
| 🎨 Theme toggle (Dark/Light) | ✅ Yes | ✅ Yes |
| 🗂️ Tree navigation | ✅ Yes | ✅ Yes |
| 📏 Width adjustment | ✅ Yes | ✅ Yes |
| 🔍 Version comparison | ✅ Yes | ❌ Disabled |
| 🎯 Diff highlighting | ✅ Yes | ❌ Disabled |
| 🗺️ Change minimap | ✅ Yes | ❌ Hidden |
| 🔄 Live updates | ✅ Yes | ❌ No |

## 📁 Project Structure

```
word-2-wiki-with-claude/
├── 🚀 Word2Wiki Launcher.bat    # Double-click to start (Windows)
├── 🐍 launcher.py               # Python launcher script
├── 📄 main.py                   # Main conversion tool
├── 📋 requirements.txt          # Python dependencies
├── 📂 output/                   # Converted HTML files
│   └── Hr_Fs_Billing_Accounts_Receivables_Cz/
│       ├── v00_02/              # Version 0.02 files
│       └── v00_03_2025_08_21/   # Version 0.03 files
├── 📂 FS_source/                # Source Word documents
└── 📂 word2wiki/                # Core conversion modules
```

## 💡 Usage Tips

### For Project Administrators:
- Use **Full Project** mode for complete control
- Run conversions locally and share entire project
- Use git integration for version control

### For Document Reviewers:
- **Standalone HTML** files work great for reviews
- No installation required - just open in browser
- All navigation and theming features available

### Best Practices:
1. **Test first**: Always test shared files on target machine
2. **Include instructions**: Share this SHARING.md file with coworkers
3. **Update regularly**: Re-run conversions when Word documents change

## 🆘 Troubleshooting

### "Python is not installed" Error:
- Install Python from [python.org](https://python.org)
- ✅ Check "Add Python to PATH"
- Restart command prompt/terminal

### "Failed to install dependencies" Error:
- Check internet connection
- Run as administrator (Windows)
- Try: `pip install -r requirements.txt` manually

### Standalone HTML Not Working:
- ✅ Use modern browser (Chrome, Firefox, Safari, Edge)
- ❌ Internet Explorer not supported
- Check browser console (F12) for errors

### Version Comparison Not Working:
- ✅ Must use HTTP server mode (option 1 in launcher)
- ❌ File:// protocol blocks cross-file loading
- Use Full Project sharing for comparison features

## 🔗 Support

- Check `main.py --help` for command-line options
- See `CLAUDE.md` for detailed project documentation
- Use launcher menu option 6 for advanced features