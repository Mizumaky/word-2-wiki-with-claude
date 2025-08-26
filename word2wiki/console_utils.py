"""Console output utilities for handling Unicode in Windows environments."""

import sys
from rich.console import Console


def create_safe_console() -> Console:
    """Create a console that handles Unicode safely on Windows."""
    return Console(
        force_terminal=True,
        legacy_windows=False,
        safe_box=True
    )


def safe_print(console: Console, text: str, **kwargs):
    """Print text safely, handling Unicode encoding errors."""
    try:
        console.print(text, **kwargs)
    except UnicodeEncodeError:
        # Replace problematic characters for console display only
        safe_text = text.encode('ascii', 'replace').decode('ascii')
        console.print(f"{safe_text} [dim](Unicode display issue - file names contain Czech characters)[/dim]", **kwargs)


def safe_filename_display(filename: str) -> str:
    """Return a safe version of filename for console display."""
    try:
        # Test if the filename can be encoded for console
        filename.encode(sys.stdout.encoding or 'utf-8')
        return filename
    except UnicodeEncodeError:
        # Return ASCII-safe version
        return filename.encode('ascii', 'replace').decode('ascii')