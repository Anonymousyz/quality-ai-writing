from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def first_release_version() -> str:
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    match = re.search(r"^## \[([^\]]+)\]", changelog, flags=re.MULTILINE)
    if not match:
        raise AssertionError("CHANGELOG.md must start with a version heading")
    return match.group(1)


class ReleaseMetadataTest(unittest.TestCase):
    def test_readmes_match_latest_changelog_version(self) -> None:
        version = first_release_version()
        chinese = (ROOT / "README.md").read_text(encoding="utf-8")
        english = (ROOT / "README.en.md").read_text(encoding="utf-8")

        self.assertIn(f"| 版本 | {version} |", chinese)
        self.assertIn(f"| Version | `{version}` |", english)

    def test_status_links_to_release_evidence(self) -> None:
        status = (ROOT / "STATUS.md").read_text(encoding="utf-8")
        self.assertIn("CHANGELOG.md", status)
        self.assertIn("Git tag", status)
        self.assertIn("Release", status)


if __name__ == "__main__":
    unittest.main()
