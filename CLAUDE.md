# Word-2-Wiki-with-Claude

## Project Overview
FS (Functional Specification) document manager and converter. Two main components:

1. **FS Manager** (`fs_manager/`) - Active development - FastAPI + browser GUI for browsing, managing, and opening FS documents from multiple sources (local, OneDrive, Confluence)
2. **Word2Wiki** (`word2wiki/`) - Legacy conversion library - Word to Obsidian Markdown. May be reused as part of FS Manager's conversion pipeline.

## FS Manager (active development)

### Architecture
- **Backend**: FastAPI (Python) serving REST API + static frontend
- **Frontend**: Vanilla HTML/CSS/JS with Pico CSS + DM Sans font (Google Fonts)
- **Persistence**: JSON file in `fs_manager/data/` (gitignored)
- **Run**: `cd fs_manager && python run.py` (opens browser at localhost:8080)
- **Dev/Preview**: `.claude/launch.json` configures `python run.py --no-browser` for Claude Preview tool

### Structure
```
fs_manager/
  backend/
    app.py              - FastAPI entry point (CORS, static serving, router includes)
    config.py           - DATA_DIR, CATALOG_FILE paths
    models.py           - Pydantic models: FSEntry, LocalSource, OnlineFile, PinnedFile, RecentFile, Catalog
    persistence.py      - JSON catalog read/write (handles field migrations)
    routers/
      sources.py        - Local folder browsing, source management CRUD, downloads-path
      catalog.py        - Starred files (called "pinned" in API), recent files, online files CRUD
      actions.py        - open-in-word, open-url (ms-word: protocol), show-in-explorer,
                          view-html (stub), convert-confluence (stub)
    services/
      local_browser.py  - Filesystem browsing, .docx filtering, tree recursion, Windows drive root fix
      onedrive.py       - OneDrive integration (STUB: NotImplementedError)
      confluence.py     - Confluence proxy integration (STUB: NotImplementedError)
      converter.py      - Conversion pipeline (STUB: NotImplementedError)
  frontend/
    index.html          - Main SPA: 4 tabs, dialogs (pin folder, add online, settings)
    css/style.css       - Styles: sidebar layout, file rows, context menus, star buttons, dark/light theme
    js/app.js           - Core logic: API helper, theme, tabs, settings (localStorage), context menu, helpers
    js/file-browser.js  - File browser: sidebar locations, address bar + breadcrumbs, flat + tree navigation
    js/catalog.js       - Home (starred + recent), online files UI
  data/                 - Persisted state (gitignored)
  run.py                - Server launcher (uvicorn port 8080, --no-browser flag supported)
  requirements.txt      - fastapi==0.115.0, uvicorn==0.30.6, pydantic==2.9.0
```

### Feature Status

#### Working / Complete
- **Local folder browsing** - flat browse mode + pinned folder tree view; address bar with breadcrumbs + history
- **Sidebar** - "Browse" entry (navigates to last path / Downloads) + pinned folders; click to toggle tree/browse; click active pinned folder again to return to browse mode
- **File starring** - star files from file browser or right-click context menu; stored in catalog as "pinned" in the API, "starred/favorites" in the UI
- **Favorites section** (Home tab) - starred files with "Open in Word/HTML/Interactive" actions (hover-only); right-click menu with Show in Explorer
- **Recent files** - last 20 opened files with relative timestamps ("4h ago") and all 3 open actions
- **Online files** - store OneDrive share links, group by folder, open via ms-word: protocol; right-click to copy link, star, or remove (with confirmation)
- **Context menus** - local files: Show in Explorer, open actions, star/unstar; online: Copy link, star/unstar, Remove
- **Settings dialog** - default double-click action (Word/HTML/Interactive), persisted to localStorage; gear icon in header
- **Theme toggle** - dark/light with sun/moon icon, persisted to localStorage
- **Pin folder dialog** - pre-fills label and path from current browsed location
- **File info tooltip** - hover over any file row to see full filename, size, and date
- **Show in Explorer** - opens Windows Explorer with file selected (cross-platform)

#### Stubbed / Planned
- **HTML quick-view** - `view-html` endpoint returns placeholder; no conversion yet
- **Interactive viewer** - button present everywhere, alerts "not yet implemented"
- **OneDrive file download** - onedrive.py has stub functions; links are stored, but content cannot be fetched
- **Confluence tab** - UI shell exists ("coming soon"); confluence.py is stub; no backend endpoints
- **Confluence conversion** - convert-confluence endpoint is stub
- **Conversion pipeline** - IR design pending; waiting for colleague's specsync code for inspiration

### Terminology Note
The **API and backend** use "pinned" (PinnedFile, /api/catalog/pinned) for what the **frontend calls "starred"** (star icons, Favorites section). This is a legacy naming inconsistency. The API should be renamed to "favorites" in a future cleanup, but it requires migrating the JSON catalog field name (persistence.py already handles one such migration).

### Known Future Plans (Priority Order)
1. **HTML quick-view** - convert .docx to HTML for in-browser preview
2. **Online files management improvements**
   - Edit folder assignment from right-click menu (currently only set at add time)
   - Cache the actual filename from the OneDrive file (currently label is manually entered)
   - Detect if the remote file's name has changed and offer to update the stored label
3. **Backend caching layer**
   - Cache generated HTML preview per file (keyed by path + mtime, invalidate on change)
   - Cache generated interactive view per file
   - Cache OneDrive file metadata (name, size, last modified) to avoid re-fetching
4. **Colleague's specsync evaluation**
   - Colleague has similar FS parsing code ("specsync")
   - Get and review specsync before designing the IR schema
   - Evaluate merging/reusing specsync's parsing logic for the conversion pipeline
5. OneDrive shared file access (download content, not just store links)
6. Confluence proxy authentication + FS link reading
7. Conversion pipeline: Word -> IR -> Confluence pages

### Conversion Pipeline Architecture (future)
```
Word .docx  -->  Internal Representation (IR)  -->  Target format
```
IR preserves: logical structure (sections, use cases, tables), formatting (colors, bold), Word comments.
Targets: Confluence pages (primary), HTML (viewing), interactive viewer.
**IR design is blocked on receiving colleague's specsync code.**

---

## Word2Wiki (legacy, reference code)

### Active Code
- `main.py` - Entry point (delegates to CLI)
- `interactive_launcher.py` - Questionary menu launcher (BROKEN: looks for HTML in output/)
- `word2wiki/cli.py` - Click CLI (browse command broken: looks for version_index.html)
- `word2wiki/markdown_converter.py` - Word to Obsidian Markdown
- `word2wiki/fs_parser.py` - FS document naming parser (reusable for IR)
- `word2wiki/version_utils.py` - Version sorting (reusable)
- `word2wiki/git_manager.py` - Git integration
- `word2wiki/interactive_cli.py` - Interactive document selection
- `word2wiki/config.py` - Configuration dataclass (lightly used)
- `word2wiki/console_utils.py` - Windows Unicode handling
- `table-pipe-converter.lua` - Pandoc Lua filter for pipe tables

### Legacy Code (reference/inspiration)
- `word2wiki/version_converter.py` (~87KB) - HTML version comparison web app with diff, tree nav, minimap, themes. **Kept intentionally** as reference for the planned interactive viewer in FS Manager.
- `word2wiki/converter.py` - Original HTML converter, deprecated.

### Debug Logs (kept intentionally)
- `debug3.log` - Documents a real crash in `split-merged-cells.lua` line 44: "Cannot set unknown property" in `expand_merged_cells()`. Evidence of a known Lua filter bug.
- `debug_phase1.log` - Shows intermediate state of merged cell processing (which cells had merges, their content). Useful reference if debugging merged cell handling in future conversion work.

### Supporting Files
- `Word2Wiki_Launcher.bat` - Windows launcher (uses broken interactive_launcher.py)
- `SHARING.md` - Sharing guide (outdated - describes legacy Word2Wiki, not FS Manager)
- `requirements.txt` - Legacy Word2Wiki dependencies

## Dependencies
### FS Manager
- fastapi==0.115.0, uvicorn==0.30.6, pydantic==2.9.0

### Word2Wiki (legacy)
- pypandoc==1.13, click==8.1.7, GitPython==3.1.40
- beautifulsoup4==4.12.2, rich==13.7.0, questionary==2.1.0

## Data
- Source documents: `FS_source/` (3 real FS docs + 2 test docs)
- Markdown output: `output_md/` (Obsidian vault, 2 documents, 5 versions)
- HTML output: `output/` (legacy)
- Media: `media/` at project root

## Commands
### FS Manager
```bash
cd fs_manager && python run.py               # Start server, auto-open browser
cd fs_manager && python run.py --no-browser  # Start server without opening browser
```

### Word2Wiki (legacy)
```bash
python main.py convert document.docx           # Convert single document
python main.py convert document.docx --no-split # Single file output
python main.py convert-all                     # Convert all documents
python main.py convert-all --skip-existing     # Only convert new
python main.py clear                           # Remove converted files
python main.py clear --force                   # Clear without confirmation
python main.py reset                           # Clear + convert all
python main.py browse                          # Open in browser (BROKEN)
python main.py status                          # Check status
python main.py init-git                        # Initialize git
python main.py commit files -m "message"       # Commit
python interactive_launcher.py                 # Interactive menu (BROKEN)
```

## Conventions
- Do not use emojis within code
- Czech characters must be preserved in filenames and content
- Discuss approach before implementing major features
- Document the "why" behind decisions, not just the "what"
- Be honest about what works vs what's broken in status reports
- Prefer hover-only action buttons in file rows (consistent pattern everywhere)
- Star (★/☆) for favorites; section called "Favorites" (not "Pinned")
- API uses "pinned" terminology internally - do not rename without migrating the JSON catalog
