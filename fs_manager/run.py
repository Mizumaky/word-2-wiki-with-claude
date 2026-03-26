#!/usr/bin/env python3
"""Run the FS Manager server."""

import sys
import webbrowser
from threading import Timer

import uvicorn


def open_browser():
    webbrowser.open("http://localhost:8080")


if __name__ == "__main__":
    print("Starting FS Manager on http://localhost:8080")
    if "--no-browser" not in sys.argv:
        Timer(1.5, open_browser).start()
    uvicorn.run(
        "backend.app:app",
        host="127.0.0.1",
        port=8080,
        reload="--reload" in sys.argv,
    )
