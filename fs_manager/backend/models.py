"""Data models for FS Manager."""

from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Optional

from pydantic import BaseModel


class SourceType(str, Enum):
    LOCAL = "local"
    ONEDRIVE = "onedrive"
    CONFLUENCE = "confluence"


class FSFile(BaseModel):
    """Represents a single FS document file."""
    name: str
    path: str
    size: Optional[int] = None
    modified: Optional[datetime] = None
    source_type: SourceType = SourceType.LOCAL
    # For online files
    url: Optional[str] = None


class FSEntry(BaseModel):
    """A file or directory entry for the file browser."""
    name: str
    path: str
    is_dir: bool
    size: Optional[int] = None
    modified: Optional[datetime] = None
    extension: Optional[str] = None
    children: Optional[list["FSEntry"]] = None


class LocalSource(BaseModel):
    """A configured local folder source."""
    id: str
    label: str
    path: str
    added: datetime


class OnlineFile(BaseModel):
    """A configured online file (OneDrive link)."""
    id: str
    label: str
    url: str
    folder: str = "Uncategorized"
    added: datetime


class PinnedFile(BaseModel):
    """A user-pinned FS file for quick access on Home tab."""
    id: str
    label: str
    path: str
    source_type: SourceType = SourceType.LOCAL
    url: Optional[str] = None
    added: datetime


class RecentFile(BaseModel):
    """A recently opened file, tracked for history."""
    label: str
    path: str
    source_type: SourceType = SourceType.LOCAL
    url: Optional[str] = None
    opened_at: datetime


class Catalog(BaseModel):
    """Persisted catalog - the user's configured sources and favorites."""
    local_sources: list[LocalSource] = []
    online_files: list[OnlineFile] = []
    pinned_files: list[PinnedFile] = []
    recent_files: list[RecentFile] = []
