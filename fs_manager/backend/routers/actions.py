"""API routes for actions on FS files (open, view, convert)."""

import subprocess
import sys
from pathlib import Path

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..services.local_browser import open_in_word, open_url_in_desktop_app

router = APIRouter(prefix="/api/actions", tags=["actions"])


class OpenFileRequest(BaseModel):
    path: str


class OpenUrlRequest(BaseModel):
    url: str


class ViewHtmlRequest(BaseModel):
    path: str


@router.post("/open-in-word")
def open_file_in_word(req: OpenFileRequest) -> dict:
    """Open a .docx file in the default Word application."""
    try:
        open_in_word(req.path)
        return {"status": "ok", "message": f"Opened: {Path(req.path).name}"}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/open-url")
def open_url(req: OpenUrlRequest) -> dict:
    """Open a URL in the desktop app (e.g. OneDrive link opens in Word)."""
    try:
        open_url_in_desktop_app(req.url)
        return {"status": "ok", "message": "Opened in desktop app"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/view-html")
def view_as_html(req: ViewHtmlRequest) -> dict:
    """Convert and return HTML preview of an FS document.

    TODO: Implement actual conversion. Currently returns a placeholder.
    """
    path = Path(req.path)
    if not path.exists():
        raise HTTPException(status_code=404, detail=f"File not found: {req.path}")

    return {
        "status": "stub",
        "message": "HTML preview not yet implemented",
        "filename": path.name,
    }


@router.post("/show-in-explorer")
def show_in_explorer(req: OpenFileRequest) -> dict:
    """Open file explorer with the given file selected."""
    path = Path(req.path)
    if not path.exists():
        raise HTTPException(status_code=404, detail=f"File not found: {req.path}")
    if sys.platform == "win32":
        subprocess.Popen(["explorer", "/select,", str(path)])
    elif sys.platform == "darwin":
        subprocess.Popen(["open", "-R", str(path)])
    else:
        subprocess.Popen(["xdg-open", str(path.parent)])
    return {"status": "ok"}


@router.post("/convert-confluence")
def convert_to_confluence(req: OpenFileRequest) -> dict:
    """Convert an FS document to Confluence pages.

    TODO: Implement actual conversion pipeline.
    """
    return {
        "status": "stub",
        "message": "Confluence conversion not yet implemented",
    }
