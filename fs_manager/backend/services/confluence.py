"""Confluence proxy integration service - stub for future implementation."""


def authenticate(proxy_url: str, credentials: dict) -> str:
    """Authenticate via the Confluence proxy.

    TODO: Implement using colleague's proxy project.
    """
    raise NotImplementedError("Confluence proxy integration not yet implemented")


def list_fs_links(page_url: str, auth_token: str) -> list[dict]:
    """Read a Confluence page and extract links to FS documents.

    TODO: Implement Confluence page parsing.
    """
    raise NotImplementedError("Confluence proxy integration not yet implemented")
