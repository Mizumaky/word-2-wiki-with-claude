"""Application configuration."""

from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
CATALOG_FILE = DATA_DIR / "catalog.json"
FRONTEND_DIR = BASE_DIR / "frontend"

# Ensure data directory exists
DATA_DIR.mkdir(exist_ok=True)
