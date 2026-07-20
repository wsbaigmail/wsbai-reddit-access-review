from __future__ import annotations

import os


class RedditApprovalRequired(RuntimeError):
    """Raised when Reddit access has not been explicitly approved."""


def require_reddit_approval() -> None:
    """Fail closed unless the operator explicitly records Reddit approval."""
    approved = os.getenv("REDDIT_ACCESS_APPROVED", "false").strip().lower()
    if approved != "true":
        raise RedditApprovalRequired(
            "Reddit Data API access is disabled until explicit approval is obtained."
        )
