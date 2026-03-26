"""Persistence layer - reads/writes the catalog JSON file."""

import json
from pathlib import Path

from .config import CATALOG_FILE
from .models import Catalog


def load_catalog() -> Catalog:
    """Load catalog from disk, or return empty catalog if none exists."""
    if CATALOG_FILE.exists():
        data = json.loads(CATALOG_FILE.read_text(encoding="utf-8"))
        # Migrate old field names
        if "online_sources" in data and "online_files" not in data:
            data["online_files"] = data.pop("online_sources")
        elif "online_sources" in data:
            data.pop("online_sources")
        if "favorites" in data and "pinned_files" not in data:
            data["pinned_files"] = data.pop("favorites")
        elif "favorites" in data:
            data.pop("favorites")
        data.pop("last_opened", None)
        return Catalog.model_validate(data)
    return Catalog()


def save_catalog(catalog: Catalog) -> None:
    """Save catalog to disk."""
    CATALOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    CATALOG_FILE.write_text(
        catalog.model_dump_json(indent=2),
        encoding="utf-8",
    )
