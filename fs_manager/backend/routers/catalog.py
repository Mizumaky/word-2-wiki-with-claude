"""API routes for catalog: pinned files, recent history, online files."""

import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..models import OnlineFile, PinnedFile, RecentFile, SourceType
from ..persistence import load_catalog, save_catalog

router = APIRouter(prefix="/api/catalog", tags=["catalog"])

MAX_RECENT = 20


# --- Pinned Files ---

class PinFileRequest(BaseModel):
    label: str
    path: str
    source_type: SourceType = SourceType.LOCAL
    url: str | None = None


@router.get("/pinned")
def get_pinned_files() -> list[PinnedFile]:
    catalog = load_catalog()
    return catalog.pinned_files


@router.post("/pinned")
def pin_file(req: PinFileRequest) -> PinnedFile:
    catalog = load_catalog()
    if any(p.path == req.path for p in catalog.pinned_files):
        raise HTTPException(status_code=409, detail="Already pinned")
    pinned = PinnedFile(
        id=str(uuid.uuid4())[:8],
        label=req.label,
        path=req.path,
        source_type=req.source_type,
        url=req.url,
        added=datetime.now(timezone.utc),
    )
    catalog.pinned_files.append(pinned)
    save_catalog(catalog)
    return pinned


@router.delete("/pinned/{pin_id}")
def unpin_file(pin_id: str) -> dict:
    catalog = load_catalog()
    catalog.pinned_files = [p for p in catalog.pinned_files if p.id != pin_id]
    save_catalog(catalog)
    return {"status": "ok"}


# --- Recent Files ---

class TrackRecentRequest(BaseModel):
    label: str
    path: str
    source_type: SourceType = SourceType.LOCAL
    url: str | None = None


@router.get("/recent")
def get_recent_files() -> list[RecentFile]:
    catalog = load_catalog()
    return catalog.recent_files


@router.post("/recent")
def track_recent(req: TrackRecentRequest) -> RecentFile:
    """Record a file as recently opened. Deduplicates by path, keeps most recent first."""
    catalog = load_catalog()
    # Remove existing entry for same path
    catalog.recent_files = [r for r in catalog.recent_files if r.path != req.path]
    entry = RecentFile(
        label=req.label,
        path=req.path,
        source_type=req.source_type,
        url=req.url,
        opened_at=datetime.now(timezone.utc),
    )
    # Insert at front, trim to max
    catalog.recent_files.insert(0, entry)
    catalog.recent_files = catalog.recent_files[:MAX_RECENT]
    save_catalog(catalog)
    return entry


# --- Online Files ---

class AddOnlineFileRequest(BaseModel):
    label: str
    url: str
    folder: str = "Uncategorized"


@router.get("/online")
def get_online_files() -> list[OnlineFile]:
    catalog = load_catalog()
    return catalog.online_files


@router.post("/online")
def add_online_file(req: AddOnlineFileRequest) -> OnlineFile:
    online_file = OnlineFile(
        id=str(uuid.uuid4())[:8],
        label=req.label,
        url=req.url,
        folder=req.folder,
        added=datetime.now(timezone.utc),
    )
    catalog = load_catalog()
    catalog.online_files.append(online_file)
    save_catalog(catalog)
    return online_file


@router.delete("/online/{file_id}")
def remove_online_file(file_id: str) -> dict:
    catalog = load_catalog()
    catalog.online_files = [f for f in catalog.online_files if f.id != file_id]
    save_catalog(catalog)
    return {"status": "ok"}
