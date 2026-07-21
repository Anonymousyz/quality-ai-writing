# tests/test_check_cases.py
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_cases import check_cases, ALLOWED_DIMENSIONS

def test_allowed_dimensions_locked():
    assert ALLOWED_DIMENSIONS == {
        "intent", "logic", "selection", "sources",
        "proportion", "stale-words", "qi", "decorum",
    }

def test_valid_case_passes(tmp_path: Path):
    p = tmp_path / "2026-07-21-ok.md"
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
    assert check_cases(tmp_path) == []

def test_unknown_dimension_fails(tmp_path: Path):
    p = tmp_path / "2026-07-21-bad.md"
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
    errs = check_cases(tmp_path)
    assert any("tone" in e for e in errs)

def test_missing_section_fails(tmp_path: Path):
    p = tmp_path / "2026-07-21-miss.md"
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
    errs = check_cases(tmp_path)
    assert errs
