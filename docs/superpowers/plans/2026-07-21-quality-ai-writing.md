# 《高质量 AI 写作》v0.1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 落地公开仓库 `quality-ai-writing`：活标准 + 八维原则 + 两篇传统打底 + 三个脱敏种子判例 + 案例校验脚本 + 入库技能，并写清公开/私有边界。

**Architecture:** 单仓库 Markdown 活标准。`STANDARD.md` 为成文法；`principles/` 展开八维；`cases/` 仅存虚构/脱敏判例；`inbox/` gitignore；`skills/case-intake` 把本地改稿整理成案例草稿；`scripts/check_cases.py` 校验判例格式与维度标签。私人 Notion 写作体系不进仓。

**Tech Stack:** Markdown；Python 3.11+（stdlib only：`pathlib`、`re`、`sys`）；pytest；Agent Skill（`SKILL.md`）。

## Global Constraints

- 仓库名：`quality-ai-writing`；中文名：高质量 AI 写作
- 管辖：知识工作文档；中英通用；仓库正文中文为主 + `README.en.md`
- 公开/私有：框架公开；Notion SOP/真料私有；`inbox/` 永不提交；案例仅虚构脱敏
- 许可：代码 MIT；文本 CC BY 4.0
- 不做：文档站、独立评审技能仓、评分产品、创意写作覆盖
- 规范来源：`docs/superpowers/specs/2026-07-21-quality-ai-writing-design.md`

## File Map

| Path | Responsibility |
|---|---|
| `README.md` / `README.en.md` | 定位、边界、现状、目录 |
| `STANDARD.md` | 否决 + 八维 + 终审（v0.1） |
| `principles/*.md` | 每维定义/问句/病征/改法/出处 |
| `traditions/*.md` | 韩愈、Orwell 短摘映射 |
| `cases/*.md` | 脱敏判例 |
| `inbox/README.md` | 收件箱说明（内容 gitignore） |
| `skills/case-intake/SKILL.md` | 入库技能 |
| `scripts/check_cases.py` | 判例校验 |
| `tests/test_check_cases.py` | 校验器测试 |
| `MAINTENANCE.md` | 修法节奏 + 脱敏红线 |
| `CHANGELOG.md` | 修订记录 |
| `LICENSE` / `LICENSE-CONTENT` | MIT / CC BY 4.0 |
| `.gitignore` | 含 `inbox/*` 例外 README |

---

### Task 1: 仓库脚手架与边界文件

**Files:**
- Create: `.gitignore`, `LICENSE`, `LICENSE-CONTENT`, `MAINTENANCE.md`, `CHANGELOG.md`, `inbox/README.md`, `README.md`, `README.en.md`
- Test: 无（文档任务；Task 5 起测脚本）

**Interfaces:**
- Consumes: 设计文档 §4 公开/私有分层、§7 仓库结构
- Produces: 可克隆的空壳仓；README 含边界句与「现状」占位

- [ ] **Step 1: 写 `.gitignore`**

```gitignore
__pycache__/
*.py[cod]
.pytest_cache/
.venv/
.env
.DS_Store
Thumbs.db

# Local intake — never publish raw drafts
inbox/*
!inbox/README.md
```

- [ ] **Step 2: 写 `LICENSE`（MIT，Copyright 2026 Anonymousyz）与 `LICENSE-CONTENT`（CC BY 4.0，说明适用于 STANDARD/principles/cases/traditions/README 等文本）**

`LICENSE-CONTENT` 正文可用 Creative Commons CC BY 4.0 标准摘要 + 指向 https://creativecommons.org/licenses/by/4.0/ ，并写明：代码与脚本以根目录 `LICENSE`（MIT）为准。

- [ ] **Step 3: 写 `inbox/README.md`**

内容要点：
- 本目录只放本地改前/改后草稿
- 整目录被 gitignore（本 README 除外）
- 入库前必须虚构化；用 `skills/case-intake`；通过脱敏后再移入 `cases/`
- 决策规则：删掉专名与内部数字后仍有独特取舍才可公开

- [ ] **Step 4: 写 `MAINTENANCE.md`**

内容要点：
- 修法节奏：约 10 条案例或每季度
- 修法检查：最密维度、未接住病征、从未被引用的原则（考虑删除）
- 脱敏红线与公开/私有表（从设计 §4 抄入）
- CHANGELOG 只写结论与公开案例 ID，不写私人文档名
- 私人操作系统：Notion 写作体系，不在此开源

- [ ] **Step 5: 写 `CHANGELOG.md`**

```markdown
# Changelog

## [0.1.0] - 2026-07-21

### Added
- Initial living standard, eight principles, two tradition notes, three seed cases, case-intake skill.
```

- [ ] **Step 6: 写 `README.md`（中文）与 `README.en.md`（英文摘要）**

`README.md` 必须含：
1. 标题与一句话定位（署名前的质量）
2. **边界**：本仓库是公开评审标准与示范；完整个人写作操作系统不在此开源；案例均为虚构/脱敏
3. 与 humanizer 的差别（一句）
4. 目录导航：STANDARD / principles / cases / traditions / skills
5. **现状**：版本 `0.1.0`；案例数 `3`；上次修法 `2026-07-21`（初版）
6. 许可说明（MIT + CC BY 4.0）

`README.en.md`：半页英文镜像上述要点即可，不必全文翻译八维。

- [ ] **Step 7: Commit**

```bash
git add .gitignore LICENSE LICENSE-CONTENT MAINTENANCE.md CHANGELOG.md inbox/README.md README.md README.en.md
git commit -m "docs: scaffold repo with public/private boundary"
```

---

### Task 2: STANDARD.md v0.1

**Files:**
- Create: `STANDARD.md`
- Modify: none
- Test: 无

**Interfaces:**
- Consumes: 设计 §3
- Produces: 版本化一页标准；维度 slug 固定如下，供 principles/cases/脚本共用

**维度 slug（锁定）：** `intent` | `logic` | `selection` | `sources` | `proportion` | `stale-words` | `qi` | `decorum`

- [ ] **Step 1: 写 `STANDARD.md`**

结构与必含内容：

```markdown
# 高质量 AI 写作 · 标准

**版本：** 0.1.0  
**范围：** 知识工作文档（方案、评审、报告、决策备忘、README/技术文档）；中英文通用。

## 一票否决
（五条，用设计 §3.1 原文）

## 义理
1. 立意 (`intent`) …
2. 逻辑 (`logic`) …
3. 取舍 (`selection`) …

## 考据
4. 来源 (`sources`) …
5. 分寸 (`proportion`) …

## 辞章
6. 陈言务去 (`stale-words`) …
7. 文气 (`qi`) …
8. 得体 (`decorum`) …

每维一行：中文名 + slug + 一句评审问句。详情见 `principles/`。

## 终审

八维查毕，清单结束。最后成不成——没有任何清单能替判断者做。

> 文章千古事，得失寸心知。

## 使用方式
1. 先扫否决；触发即不合格。
2. 按任务风险选深度：轻量通读 / 八维全检。
3. 修改沉淀：脱敏后经 case-intake 入 `cases/`；积累后修法。
```

- [ ] **Step 2: Commit**

```bash
git add STANDARD.md
git commit -m "docs: add STANDARD v0.1.0"
```

---

### Task 3: 八维 principles/

**Files:**
- Create: `principles/intent.md`, `logic.md`, `selection.md`, `sources.md`, `proportion.md`, `stale-words.md`, `qi.md`, `decorum.md`
- Test: 无

**Interfaces:**
- Consumes: STANDARD 维度 slug；Notion 七原理仅作思想对齐，**不复制私人 SOP 原文**
- Produces: 每文件同一模板

每文件模板：

```markdown
# {中文名} (`{slug}`)

## 定义
（2–4 句）

## 评审问句
- …

## AI 初稿典型病征
- …

## 改法
- …

## 中文出处
（短摘 + 出处；无可写「见 traditions/…」）

## 英文出处
（短摘 + 出处）

## 关联判例
- （首版可写「见 cases/…」或「待积累」）
```

内容要点（实现时写满，勿留空段）：

| slug | 中文 | 病征焦点 |
|---|---|---|
| intent | 立意 | 无判断、话题说明冒充结论 |
| logic | 逻辑 | 因此无推导、事实/解释/建议混谈 |
| selection | 取舍 | 面面俱到、附录塞进正文 |
| sources | 来源 | 编造引文、不可溯 |
| proportion | 分寸 | demo 说成结论、过度周全无立场 |
| stale-words | 陈言务去 | AI 腔、空话、删除无信息损失 |
| qi | 文气 | 匀速排比、段落无呼吸 |
| decorum | 得体 | 翻译腔、语体错位 |

公开写作可吸收的公开层信号（改写进 `stale-words` / `logic` / `intent`，勿整段搬 Notion）：
- 抽象名词与万能排比密集
- 主体可替换句仍成立
- 「因此」无真实推导
- 核心判断须可被读者复述

- [ ] **Step 1: 按模板创建八个文件并写满**

- [ ] **Step 2: Commit**

```bash
git add principles/
git commit -m "docs: add eight principle pages"
```

---

### Task 4: 两篇 traditions/

**Files:**
- Create: `traditions/han-yu-da-li-yi-shu.md`, `traditions/orwell-politics-and-english.md`
- Test: 无

**Interfaces:**
- Consumes: 设计 §6
- Produces: 各 500–1500 字；短摘须可核对出处

- [ ] **Step 1: 写韩愈篇**

必含：
- 「惟陈言之务去」短摘与《答李翊书》出处说明
- 「气盛则言之短长与声之高下者皆宜」与文气维的映射
- 对 AI：陈言 = 未经过判断的套话与陈旧思路，不只是禁用词表

- [ ] **Step 2: 写 Orwell 篇**

必含：
- 垂死隐喻 / 假白南充句式与 AI 套话的对应
- 六条规则中与「陈言务去」「分寸」直接相关的 2–3 条短摘
- 注明：规则是启发式，不是科学定律（对齐私人体系「来源使用原则」的公开表述）

- [ ] **Step 3: Commit**

```bash
git add traditions/
git commit -m "docs: add Han Yu and Orwell tradition notes"
```

---

### Task 5: 案例校验器（TDD）+ 三个种子判例

**Files:**
- Create: `scripts/check_cases.py`, `tests/test_check_cases.py`, `cases/2026-07-21-overclaim-demo.md`, `cases/2026-07-21-stale-words-enable.md`, `cases/2026-07-21-no-judgment.md`
- Test: `tests/test_check_cases.py`

**Interfaces:**
- Consumes: 维度 slug 集合（与 Task 2 锁定一致）
- Produces:
  - `check_cases(cases_dir: Path) -> list[str]` 返回错误信息列表；空列表 = 通过
  - CLI：`python scripts/check_cases.py` 退出码 0/1

**判例 front-matter 必填字段：**

```yaml
---
id: 2026-07-21-overclaim-demo
scene: 内部试点总结（虚构）
dimensions: [proportion, sources]
verdict: demo 被写成已验证结论
---
```

正文必含四级标题（恰好这些）：`## 场景` `## AI 初稿` `## 修改稿` `## 改动说明`

- [ ] **Step 1: 写失败测试**

```python
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
```

- [ ] **Step 2: 跑测试确认失败**

```bash
python -m pytest tests/test_check_cases.py -v
```

Expected: FAIL（`check_cases` 未定义或导入失败）

- [ ] **Step 3: 实现 `scripts/check_cases.py`**

```python
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
```

- [ ] **Step 4: 跑单元测试确认通过**

```bash
python -m pytest tests/test_check_cases.py -v
```

Expected: PASS

- [ ] **Step 5: 写三个虚构种子判例**

1. `cases/2026-07-21-overclaim-demo.md` — 试点 demo 写成「已验证可推广」（`proportion`, `sources`）
2. `cases/2026-07-21-stale-words-enable.md` — 「赋能/值得注意的是」空转（`stale-words`, `qi`）
3. `cases/2026-07-21-no-judgment.md` — AI 初稿直接交付、无立意（`intent`, 触发否决意象但案例正文示范如何补判断）

全部场景必须标明虚构；禁止真实机构名。

- [ ] **Step 6: 跑 CLI 校验真实 cases/**

```bash
python scripts/check_cases.py
```

Expected: `OK` 退出码 0

- [ ] **Step 7: Commit**

```bash
git add scripts/check_cases.py tests/test_check_cases.py cases/
git commit -m "feat: add case checker and three seed cases"
```

---

### Task 6: case-intake 技能

**Files:**
- Create: `skills/case-intake/SKILL.md`
- Test: 无自动化；手工按技能说明跑一次虚构样例（步骤内自检清单）

**Interfaces:**
- Consumes: 维度 slug；脱敏规则（MAINTENANCE）
- Produces: 可安装技能；输出写入 `inbox/` 的案例草稿 Markdown

- [ ] **Step 1: 写 `skills/case-intake/SKILL.md`**

```markdown
---
name: case-intake
description: >-
  把 AI 初稿与人工修改整理成《高质量 AI 写作》判例草稿：做 diff 归维、
  生成 cases 格式 Markdown、跑脱敏提醒。Use when the user pastes before/after
  writing samples, asks to intake a writing case, 入库案例, or 整理改稿判例.
---

# 案例入库（case-intake）

你帮助维护公开仓库 quality-ai-writing 的判例库。你输出的是**草稿**，人审校后才可移入 `cases/`。

## 硬规则
1. 默认写入本地 `inbox/`，不要直接写入 `cases/`。
2. 发现疑似真实客户、雇主、项目、内部系统名、精确内部数据时，必须列出「脱敏待处理」清单；不得假装已安全。
3. 维度标签只能使用：intent, logic, selection, sources, proportion, stale-words, qi, decorum。
4. 不复制用户的私人 SOP 或 Notion 操作系统原文进公开文件。

## 流程
1. 读取改前、改后文本（若用户只给一段，询问缺的一侧）。
2. 列出实质改动（忽略纯空格）；每处映射 1–2 个维度。
3. 生成完整判例 Markdown（front-matter + 四节）。
4. 脱敏扫描：专名、邮箱、URL、精确百分比/金额、内部代号 → 标红建议替换为虚构名。
5. 附「修法暗示」：若现有八维接不住，说明可能要改 STANDARD 的哪一句。
6. 提醒用户：审校通过后再手动移入 `cases/YYYY-MM-DD-slug.md` 并运行 `python scripts/check_cases.py`。

## 输出模板
（与 cases 文件格式相同，另加章节 `## 脱敏待处理` 与 `## 修法暗示`）
```

- [ ] **Step 2: 在 README「目录」中链到该技能，并写 3 行安装说明**（clone 到 `~/.cursor/skills/case-intake` 等，Windows 用 `%USERPROFILE%`）

- [ ] **Step 3: Commit**

```bash
git add skills/case-intake/SKILL.md README.md README.en.md
git commit -m "feat: add case-intake skill"
```

---

### Task 7: 收口核对

**Files:**
- Modify: `README.md`（确认现状数字与链接齐全）, `CHANGELOG.md`（如有遗漏）
- Test: `python scripts/check_cases.py` + `python -m pytest tests/ -v`

**Interfaces:**
- Consumes: 全部既有文件
- Produces: v0.1 可发布状态（尚未要求 push）

- [ ] **Step 1: 跑全量校验**

```bash
python -m pytest tests/ -v
python scripts/check_cases.py
```

Expected: 全部 PASS / OK

- [ ] **Step 2: 对照设计文档自检清单**

- [ ] STANDARD 含否决、八维 slug、终审杜甫联  
- [ ] 八个 principles 无空段  
- [ ] 两篇 traditions  
- [ ] 三个 cases 通过校验  
- [ ] README 含公开/私有边界句与现状节  
- [ ] inbox gitignore 生效（`git check-ignore -v inbox/draft.md` 在创建临时文件后应命中）  
- [ ] 无 Notion SOP 原文、无真实机构名  

- [ ] **Step 3: 若有修正，提交**

```bash
git add -A
git status
git commit -m "docs: finalize v0.1 consistency pass"
```

（无变更则跳过 commit）

---

## Spec Coverage Check

| 设计要求 | Task |
|---|---|
| 脚手架 + 许可 + MAINTENANCE | 1 |
| 公开/私有边界写入 README/MAINTENANCE | 1 |
| STANDARD v0.1 | 2 |
| principles ×8 | 3 |
| traditions ×2 | 4 |
| seed cases ×3 + check_cases.py | 5 |
| case-intake 技能 | 6 |
| CHANGELOG + 现状节 | 1, 7 |
| 不公开 Notion SOP | 全局约束 + Task 3/6 硬规则 |

## Placeholder Scan

无 TBD/TODO 步骤；校验器与测试代码已写全；判例主题已指定，正文由实现时按虚构场景写满。
