from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from detect_prose_signals import format_report, scan  # noqa: E402


class DetectProseSignalsTest(unittest.TestCase):
    def test_stock_and_overclaim(self) -> None:
        text = "本试点已充分验证方案可行，并赋能协同效率。"
        hits = scan(text)
        ids = {h.signal_id for h in hits}
        self.assertIn("overclaim", ids)
        self.assertIn("cn_stock_phrase", ids)

    def test_empty_therefore(self) -> None:
        text = "检索更快。因此，我们应当立即迁移。"
        hits = scan(text)
        self.assertTrue(any(h.signal_id == "empty_therefore" for h in hits))

    def test_translationese(self) -> None:
        text = "基于当前流程尚未落地的背景，相关协同将予以推进。"
        hits = scan(text)
        self.assertTrue(any(h.signal_id == "translationese" for h in hits))

    def test_clean_text_no_hits(self) -> None:
        text = "权限还没批下来，这周先不改导出模板。"
        self.assertEqual(scan(text), [])

    def test_report_mentions_advisory(self) -> None:
        report = format_report("x.md", scan("因此，立刻全面推广。"))
        self.assertIn("signal", report)
        self.assertIn("≠ verdict", report)


if __name__ == "__main__":
    unittest.main()
