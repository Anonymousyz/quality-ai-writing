#!/usr/bin/env python3
"""Report which STANDARD dimensions are tagged in cases/."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ALLOWED = [
    "intent",
    "logic",
    "selection",
    "sources",
    "proportion",
    "stale-words",
    "qi",
    "decorum",
]

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def _dims(raw: str) -> list[str]:
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        if not inner:
            return []
        return [p.strip().strip("'\"") for p in inner.split(",") if p.strip()]
    return [raw.strip("'\"")]


def coverage(cases_dir: Path) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {d: [] for d in ALLOWED}
    for path in sorted(cases_dir.glob("*.md")):
        if path.name.upper() == "README.MD":
            continue
        text = path.read_text(encoding="utf-8")
        m = FM_RE.match(text)
        if not m:
            continue
        dims_raw = None
        for line in m.group(1).splitlines():
            if line.startswith("dimensions:"):
                dims_raw = line.split(":", 1)[1].strip()
                break
        if not dims_raw:
            continue
        for d in _dims(dims_raw):
            if d in out:
                out[d].append(path.stem)
    return out


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    cov = coverage(root / "cases")
    missing = [d for d, ids in cov.items() if not ids]
    print("dimension coverage (case ids):")
    for d in ALLOWED:
        ids = cov[d]
        print(f"  {d}: {', '.join(ids) if ids else '(none)'}")
    if missing:
        print("UNCOVERED:", ", ".join(missing))
        return 1
    print("OK: all eight dimensions have ≥1 case tag")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
