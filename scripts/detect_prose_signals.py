#!/usr/bin/env python3
"""Lightweight heuristic signals for AI-ish / hollow prose (stdlib only).

Not a guilt detector. Hits are prompts for human judgment — see
skills/ai-prose-detect/SKILL.md. This script cannot decide whether a text has
necessary content or a meaningful order; review notes/meaning-and-order.md.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Signal:
    id: str
    label: str
    pattern: re.Pattern[str]


SIGNALS: tuple[Signal, ...] = (
    Signal(
        "cn_stock_phrase",
        "陈言/空话套语",
        re.compile(
            r"(赋能|闭环|对齐|抓手|落地|全方位|多维度|显著提升|"
            r"充分验证|标准作业流程|风险可控|协同效率)"
        ),
    ),
    Signal(
        "en_stock_phrase",
        "English stock / AI filler",
        re.compile(
            r"\b(delve into|landscape|robust|leverag(?:e|ing)|"
            r"it is (?:important|worth) (?:to )?not(?:e|ing)|"
            r"in today's (?:fast-paced|ever-evolving)|"
            r"unlock(?:ing)? (?:the )?potential|"
            r"comprehensive (?:overview|solution))\b",
            re.I,
        ),
    ),
    Signal(
        "empty_therefore",
        "空「因此/据此」类连接（需人工查 Warrant）",
        re.compile(r"(因此|据此|由此可见|综上所述)[，,]"),
    ),
    Signal(
        "translationese",
        "翻译腔/名义化痕迹",
        re.compile(
            r"(基于.{0,24}(背景|前提)|予以(推进|落实|实施)|"
            r"进行.{0,8}(优化|提升|落地)|双重实现|"
            r"的作出是为了)"
        ),
    ),
    Signal(
        "overclaim",
        "过强断言信号",
        re.compile(
            r"(已充分验证|证明可|立即全面|全面推广|事实证明|"
            r"多方确认|不可否认)"
        ),
    ),
)


@dataclass
class Hit:
    signal_id: str
    label: str
    match: str
    start: int
    end: int
    line: int


def _line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def scan(text: str, signals: tuple[Signal, ...] = SIGNALS) -> list[Hit]:
    hits: list[Hit] = []
    for sig in signals:
        for m in sig.pattern.finditer(text):
            hits.append(
                Hit(
                    signal_id=sig.id,
                    label=sig.label,
                    match=m.group(0),
                    start=m.start(),
                    end=m.end(),
                    line=_line_number(text, m.start()),
                )
            )
    hits.sort(key=lambda h: (h.start, h.signal_id))
    return hits


def format_report(path: str | None, hits: list[Hit]) -> str:
    header = path or "(stdin)"
    if not hits:
        return f"{header}: no heuristic signals\n"
    lines = [f"{header}: {len(hits)} signal(s)"]
    for h in hits:
        snippet = h.match.replace("\n", " ")
        lines.append(f"  L{h.line}\t[{h.signal_id}] {h.label}: {snippet}")
    lines.append(
        "Note: signals ≠ verdict. This script cannot determine whether content is necessary "
        "or well ordered; see skills/ai-prose-detect/SKILL.md and "
        "notes/meaning-and-order.md."
    )
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Scan text for lightweight AI-prose heuristic signals."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Files to scan (default: stdin)",
    )
    args = parser.parse_args(argv)

    if not args.paths:
        text = sys.stdin.read()
        sys.stdout.write(format_report(None, scan(text)))
        return 0

    for raw in args.paths:
        p = Path(raw)
        text = p.read_text(encoding="utf-8")
        sys.stdout.write(format_report(str(p), scan(text)))
    # Exit 0 always: hits are advisory, not CI failures.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
