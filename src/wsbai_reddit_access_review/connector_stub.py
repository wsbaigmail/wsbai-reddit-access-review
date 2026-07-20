from __future__ import annotations

from .compliance import require_reddit_approval


def start_connector() -> None:
    """Nonfunctional review stub. No Reddit endpoint is called."""
    require_reddit_approval()
    raise NotImplementedError(
        "Connector implementation is intentionally withheld pending Reddit approval."
    )
