# Chinese Style Sources Integration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 Notion 写作体系中的中文文风来源和经过抽离的规则，安全地融入公开的 `quality-ai-writing` 标准。

**Architecture:** `traditions/` 保存来源卡和解释性短注；`STANDARD.md`、原则页和技能只保留可执行规则。来源、转述和仓库规则分层呈现，以现有八维和维护准入规则约束新增内容。

**Tech Stack:** Markdown、Python 标准库校验脚本、Git。

## Global Constraints

- 受版权保护材料只保留书目信息、原始链接、短摘录和转述，不复制全文。
- 不公开 Notion 私人笔记、真实项目材料或未脱敏草稿。
- 规则必须说明适用条件和例外；信号检查不能替代事实核验。
- 维持现有八维 slug，不新增打分或自动发布结论。

---

### Task 1: 建立中文文风来源卡

**Files:**
- Create: `traditions/chinese-style-sources.md`
- Create: `traditions/ye-shengtao-public-writing.md`
- Create: `traditions/ui-copy-task-writing.md`
- Modify: `traditions/README.md`

- [ ] 记录来源线索、作者、原始链接和仓库映射。
- [ ] 将叶圣陶、余光中、商金林、宗守云、杜泽逊、王国维、王慧敏和 Ant Design 分为“内容与修改”“自然中文”“任务文案”三组。
- [ ] 对每个来源写明：它提供的是问题线索或实践原则，不是跨文体的硬规则。
- [ ] 在 `traditions/README.md` 增加三篇中文参考索引。

### Task 2: 将规则写入现有标准

**Files:**
- Modify: `STANDARD.md`
- Modify: `principles/stale-words.md`
- Modify: `principles/decorum.md`
- Modify: `skills/pre-sign-review/SKILL.md`

- [ ] 在写前三问与终审流程之间补充“任务—判断—读者”的检查顺序。
- [ ] 在 `stale-words` 增加删除测试、范围与条件保留、主体和动作还原。
- [ ] 在 `decorum` 增加自然中文与任务文本的场景边界，不把名词化、被动或长句一概判错。
- [ ] 在 `pre-sign-review` 增加任务型文案的状态、动作、后果与下一步检查，保留不打分和不替代事实核验的边界。

### Task 3: 更新导航与版本记录

**Files:**
- Modify: `README.md`
- Modify: `CHANGELOG.md`

- [ ] 更新传统篇数量、版本号与上次修法说明。
- [ ] 在 README 说明来源索引与规则映射的公开边界。
- [ ] 在 CHANGELOG 记录新增来源和标准调整，不录入私人笔记内容。

### Task 4: 校验、审阅与发布

**Files:**
- Test: `tests/test_check_cases.py`
- Test: `tests/test_case_coverage.py`
- Test: `tests/test_detect_prose_signals.py`

- [ ] 运行 `python -m unittest discover -s tests -v`、`python scripts/check_cases.py`、`python scripts/case_coverage.py`。
- [ ] 用 `rg` 检查所有新增来源链接、版本号、传统篇数量与 README 导航。
- [ ] 重读新增和变更内容：检查出处、转述/引文边界、重复、空泛表述和自然中文。
- [ ] 提交全部有意改动，推送 `main`，再以 `git ls-remote origin refs/heads/main` 核验远端提交。
