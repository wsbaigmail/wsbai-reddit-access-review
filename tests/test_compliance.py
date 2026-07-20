from __future__ import annotations

import os
import unittest
from unittest.mock import patch

from wsbai_reddit_access_review.compliance import (
    RedditApprovalRequired,
    require_reddit_approval,
)


class ComplianceGateTests(unittest.TestCase):
    def test_access_fails_closed_without_approval(self) -> None:
        with patch.dict(os.environ, {"REDDIT_ACCESS_APPROVED": "false"}, clear=False):
            with self.assertRaises(RedditApprovalRequired):
                require_reddit_approval()


if __name__ == "__main__":
    unittest.main()
