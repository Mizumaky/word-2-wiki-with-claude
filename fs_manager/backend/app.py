"""FS Manager - FastAPI application entry point."""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .config import FRONTEND_DIR
from .routers import actions, catalog, sources

app = FastAPI(
    title="FS Manager",
    description="Functional Specification document manager",
    version="0.1.0",
)

# API routes
app.include_router(sources.router)
app.include_router(catalog.router)
app.include_router(actions.router)

# Serve frontend static files
app.mount("/", StaticFiles(directory=str(FRONTEND_DIR), html=True), name="frontend")
