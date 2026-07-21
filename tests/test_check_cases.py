from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_cases import ALLOWED_DIMENSIONS, check_cases  # noqa: E402


class CheckCasesTest(unittest.TestCase):
    def test_allowed_dimensions_locked(self) -> None:
        self.assertEqual(
            ALLOWED_DIMENSIONS,
            {
                "intent",
                "logic",
                "selection",
                "sources",
                "proportion",
                "stale-words",
                "qi",
                "decorum",
            },
        )

    def test_valid_case_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "2026-07-21-ok.md"
            p.write_text(
                "---\n"
                "id: 2026-07-21-ok\n"
                "scene: fictional\n"
                "dimensions: [intent, stale-words]\n"
                "verdict: short verdict\n"
                "---\n\n"
                "## 场景\ns\n\n## AI 初稿\na\n\n## 修改稿\nb\n\n## 改动说明\nc\n",
                encoding="utf-8",
            )
            self.assertEqual(check_cases(Path(tmp)), [])

    def test_unknown_dimension_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "2026-07-21-bad.md"
            p.write_text(
                "---\n"
                "id: 2026-07-21-bad\n"
                "scene: fictional\n"
                "dimensions: [tone]\n"
                "verdict: x\n"
                "---\n\n"
                "## 场景\ns\n\n## AI 初稿\na\n\n## 修改稿\nb\n\n## 改动说明\nc\n",
                encoding="utf-8",
            )
            errs = check_cases(Path(tmp))
            self.assertTrue(any("tone" in e for e in errs))

    def test_missing_section_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "2026-07-21-miss.md"
            p.write_text(
                "---\n"
                "id: 2026-07-21-miss\n"
                "scene: fictional\n"
                "dimensions: [logic]\n"
                "verdict: x\n"
                "---\n\n"
                "## 场景\ns\n\n## AI 初稿\na\n",
                encoding="utf-8",
            )
            self.assertTrue(check_cases(Path(tmp)))


if __name__ == "__main__":
    unittest.main()
