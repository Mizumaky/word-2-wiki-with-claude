"""Conversion pipeline service - stub for future implementation.

Architecture:
    Word .docx  -->  Internal Representation (IR)  -->  Target format

The IR preserves:
    - Logical structure: sections, use cases, tables, attributes
    - Formatting: text color, bold/italic, etc.
    - Word comments

Target formats:
    - Confluence pages (primary goal)
    - HTML (quick viewing)
    - Markdown (existing, via word2wiki)
"""


def convert_to_html_preview(file_path: str) -> str:
    """Convert a Word document to a simple HTML preview.

    TODO: Implement HTML preview generation.
    Returns HTML string for quick viewing in the browser.
    """
    raise NotImplementedError("HTML preview not yet implemented")


def convert_to_confluence(file_path: str, target_space: str) -> dict:
    """Convert a Word document to Confluence pages via IR.

    TODO: Implement the full conversion pipeline.
    """
    raise NotImplementedError("Confluence conversion not yet implemented")
