from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from case_coverage import coverage  # noqa: E402


class CaseCoverageTest(unittest.TestCase):
    def test_all_dimensions_have_cases(self) -> None:
        cov = coverage(ROOT / "cases")
        missing = [d for d, ids in cov.items() if not ids]
        self.assertEqual(missing, [], f"uncovered dimensions: {missing}")


if __name__ == "__main__":
    unittest.main()
