#!/usr/bin/env python3
"""Validate case files under cases/."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ALLOWED_DIMENSIONS = {
    "intent",
    "logic",
    "selection",
    "sources",
    "proportion",
    "stale-words",
    "qi",
    "decorum",
}

REQUIRED_SECTIONS = ("## 场景", "## AI 初稿", "## 修改稿", "## 改动说明")
FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def _parse_front_matter(text: str) -> dict[str, str] | None:
    m = FM_RE.match(text)
    if not m:
        return None
    data: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        data[k.strip()] = v.strip()
    return data


def _parse_dimensions(raw: str) -> list[str]:
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        if not inner:
            return []
        return [p.strip().strip("'\"") for p in inner.split(",") if p.strip()]
    return [raw.strip("'\"")]


def check_cases(cases_dir: Path) -> list[str]:
    errors: list[str] = []
    if not cases_dir.is_dir():
        return [f"missing cases dir: {cases_dir}"]
    files = sorted(cases_dir.glob("*.md"))
    if not files:
        return ["no case files found"]
    for path in files:
        text = path.read_text(encoding="utf-8")
        fm = _parse_front_matter(text)
        if fm is None:
            errors.append(f"{path.name}: missing or invalid front matter")
            continue
        for key in ("id", "scene", "dimensions", "verdict"):
            if key not in fm or not fm[key]:
                errors.append(f"{path.name}: missing front matter field `{key}`")
        stem = path.stem
        if fm.get("id") and fm["id"] != stem:
            errors.append(f"{path.name}: id `{fm.get('id')}` != filename stem `{stem}`")
        if "dimensions" in fm:
            dims = _parse_dimensions(fm["dimensions"])
            if not dims:
                errors.append(f"{path.name}: empty dimensions")
            for d in dims:
                if d not in ALLOWED_DIMENSIONS:
                    errors.append(f"{path.name}: unknown dimension `{d}`")
        for sec in REQUIRED_SECTIONS:
            if sec not in text:
                errors.append(f"{path.name}: missing section `{sec}`")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errs = check_cases(root / "cases")
    if errs:
        print("FAIL")
        for e in errs:
            print(f"  - {e}")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
