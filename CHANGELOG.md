# Changelog

## [0.8.0] - 2026-07-29

### Added
- 中文文风来源索引：叶圣陶、余光中、商金林、宗守云、杜泽逊、王国维、王慧敏与 Ant Design 的可核对出处和规则映射
- Traditions：叶圣陶的公共写作与修改、修改与文气、界面任务文案
- 署名前审稿：任务型文字的状态、动作、后果与下一步附加问句

### Changed
- STANDARD：中文修改先回到任务、判断和读者；表达检查不替代事实、来源与专业核验
- Principles：补充限定条件、责任主体、自然中文与任务信息前置的检查边界
- README：版本 0.8.0；传统/参考篇 19 篇


## [0.7.0] - 2026-07-21

### Added
- Notes: veto-scan, evidence-ladder, cars-intro, english-knowledge-prose
- Traditions: Swales CARS; Lanham *Revising Prose*
- Cases (11 total): false-balance, unsourced-claim, appendix-dump, uniform-rhythm, en-overclaim
- Skill: `pre-sign-review` — veto then eight dimensions (no auto-score)
- Scripts: `case_coverage.py`; cases/README index
- Tests: unittest for check_cases; coverage requires all 8 dimensions tagged

### Changed
- STANDARD → 0.7.0; all principles link live cases; check_cases skips README.md

## [0.6.0] - 2026-07-21

### Added
- Seed cases: empty「因此」(logic/proportion), fake MECE (selection/stale-words), translationese (decorum/qi)
- Script: `scripts/detect_prose_signals.py` — stdlib regex heuristics; advisory exit 0
- Tests: `tests/test_detect_prose_signals.py`

### Changed
- STANDARD → 0.6.0; README case count 6; skill points to the script

## [0.5.0] - 2026-07-21

### Added
- Traditions: Lu Ji *Wenfu* (意—文损耗 / 警策); Su Shi 辞达; Tongcheng 义理·考据·词章
- Skill: `mock-reader` — target-reader paraphrase and questions (not a substitute for humans)

### Changed
- STANDARD → 0.5.0; README skill install lists three skills

## [0.4.0] - 2026-07-21

### Added
- Tradition: Williams *Style* (characters as subjects, actions as verbs, old→new)
- Notes: Toulmin Warrant; MECE as classification heuristic
- Skill: `ai-prose-detect` — signal scan for AI-ish / stale / empty-logic / translation-ese prose

### Changed
- STANDARD → 0.4.0; logic/selection/qi cross-links; README install covers two skills

## [0.3.0] - 2026-07-21

### Added
- Process notes: one idea per paragraph, reader-first, understanding ceiling, scene choices
- Tradition notes: Zhu Guangqian (cliché / 套板反应), Ye Shengtao (paragraph + reader), Pinker (*Sense of Style*)
- MAINTENANCE: four conditions for a rule to enter the living standard

### Changed
- STANDARD → 0.3.0; task-modes / revision-order cross-links strengthened
- README status counts updated

## [0.2.0] - 2026-07-21

### Added
- Process notes: task modes, structure-serves-use, revision order (`notes/`)
- Tradition notes: *Wenxin Diaolong · Rongcai*, Yu Guangzhong on Chinese normal/deviant style, Strunk & White, Zinsser
- STANDARD: write-before modes and three questions; pointers to notes/traditions

### Changed
- Principle pages cross-link to the new tradition notes
- README status → 0.2.0

## [0.1.0] - 2026-07-21

### Added
- Initial living standard, eight principles, two tradition notes, three seed cases, case-intake skill.
