"""API routes for browsing file sources."""

import uuid
from datetime import datetime, timezone
from pathlib import Path

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..models import FSEntry, LocalSource
from ..persistence import load_catalog, save_catalog
from ..services.local_browser import get_downloads_folder, list_directory, list_directory_recursive

router = APIRouter(prefix="/api/sources", tags=["sources"])


class AddLocalSourceRequest(BaseModel):
    label: str
    path: str


class BrowseRequest(BaseModel):
    path: str


@router.get("/local")
def get_local_sources() -> list[LocalSource]:
    """Get all configured local folder sources."""
    catalog = load_catalog()
    return catalog.local_sources


@router.post("/local")
def add_local_source(req: AddLocalSourceRequest) -> LocalSource:
    """Add a new local folder source."""
    path = Path(req.path)
    if not path.is_dir():
        raise HTTPException(status_code=400, detail=f"Not a valid directory: {req.path}")

    source = LocalSource(
        id=str(uuid.uuid4())[:8],
        label=req.label,
        path=str(path.resolve()),
        added=datetime.now(timezone.utc),
    )
    catalog = load_catalog()
    catalog.local_sources.append(source)
    save_catalog(catalog)
    return source


@router.delete("/local/{source_id}")
def remove_local_source(source_id: str) -> dict:
    """Remove a local folder source."""
    catalog = load_catalog()
    catalog.local_sources = [s for s in catalog.local_sources if s.id != source_id]
    save_catalog(catalog)
    return {"status": "ok"}


@router.get("/downloads-path")
def get_downloads_path() -> dict:
    """Get the user's Downloads folder path."""
    return {"path": get_downloads_folder()}


@router.get("/browse")
def browse_directory(path: str) -> list[FSEntry]:
    """Browse contents of a directory. Returns files (.docx) and subdirectories."""
    try:
        return list_directory(path)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/browse-tree")
def browse_directory_tree(path: str) -> list[FSEntry]:
    """Browse a directory recursively, returning a nested tree of all .docx files."""
    try:
        return list_directory_recursive(path)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
