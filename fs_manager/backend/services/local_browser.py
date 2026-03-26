"""Local filesystem browsing service."""

import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from ..models import FSEntry


def _normalize_path(dir_path: str) -> Path:
    """Normalize a path string, handling drive roots like 'C:' on Windows."""
    path = Path(dir_path)
    # On Windows, Path("C:") resolves to CWD, not root. Fix it.
    if sys.platform == "win32" and len(dir_path) <= 3 and dir_path[1:2] == ":":
        path = Path(dir_path.rstrip("/\\") + "\\")
    return path


def list_directory(dir_path: str) -> list[FSEntry]:
    """List contents of a directory, returning files and subdirectories.

    Only shows .docx files and directories (hides temp files, hidden files).
    Skips individual items that raise PermissionError.
    """
    path = _normalize_path(dir_path)
    if not path.is_dir():
        raise ValueError(f"Not a directory: {dir_path}")

    entries = []
    try:
        items = sorted(path.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
    except PermissionError:
        raise ValueError(f"Permission denied: {dir_path}")

    for item in items:
        # Skip hidden files, temp files
        if item.name.startswith(".") or item.name.startswith("~$"):
            continue

        try:
            if item.is_dir():
                entries.append(FSEntry(
                    name=item.name,
                    path=str(item),
                    is_dir=True,
                ))
            elif item.suffix.lower() == ".docx":
                stat = item.stat()
                entries.append(FSEntry(
                    name=item.name,
                    path=str(item),
                    is_dir=False,
                    size=stat.st_size,
                    modified=datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc),
                    extension=item.suffix.lower(),
                ))
        except PermissionError:
            continue

    return entries


def list_directory_recursive(dir_path: str, max_depth: int = 5) -> list[FSEntry]:
    """List contents of a directory recursively as a tree.

    Returns nested FSEntry objects with children populated for directories.
    """
    path = Path(dir_path)
    if not path.is_dir():
        raise ValueError(f"Not a directory: {dir_path}")

    def _scan(p: Path, depth: int) -> list[FSEntry]:
        entries = []
        try:
            items = sorted(p.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
        except PermissionError:
            return entries

        for item in items:
            if item.name.startswith(".") or item.name.startswith("~$"):
                continue

            if item.is_dir():
                children = _scan(item, depth + 1) if depth < max_depth else None
                # Only include directories that contain .docx files (directly or nested)
                if children is not None and len(children) == 0:
                    continue
                entries.append(FSEntry(
                    name=item.name,
                    path=str(item),
                    is_dir=True,
                    children=children,
                ))
            elif item.suffix.lower() == ".docx":
                stat = item.stat()
                entries.append(FSEntry(
                    name=item.name,
                    path=str(item),
                    is_dir=False,
                    size=stat.st_size,
                    modified=datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc),
                    extension=item.suffix.lower(),
                ))

        return entries

    return _scan(path, 0)


def get_downloads_folder() -> str:
    """Get the user's Downloads folder path."""
    if sys.platform == "win32":
        downloads = Path.home() / "Downloads"
    elif sys.platform == "darwin":
        downloads = Path.home() / "Downloads"
    else:
        downloads = Path.home() / "Downloads"
    return str(downloads) if downloads.is_dir() else str(Path.home())


def open_in_word(file_path: str) -> None:
    """Open a .docx file in the default application (Word)."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if sys.platform == "win32":
        os.startfile(str(path))
    elif sys.platform == "darwin":
        subprocess.Popen(["open", str(path)])
    else:
        subprocess.Popen(["xdg-open", str(path)])


def open_url_in_desktop_app(url: str) -> None:
    """Open a OneDrive/SharePoint URL in Word desktop app.

    Uses the ms-word: protocol handler which tells Windows to open
    the URL directly in Word rather than in the browser.
    Format: ms-word:ofe|u|<url>
    """
    word_url = f"ms-word:ofe|u|{url}"
    if sys.platform == "win32":
        os.startfile(word_url)
    elif sys.platform == "darwin":
        subprocess.Popen(["open", word_url])
    else:
        subprocess.Popen(["xdg-open", word_url])
