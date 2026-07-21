# Quality AI Writing

> Before you sign your name — what makes a knowledge-work document actually good?

A living review standard with de-identified revision cases and bilingual writing-tradition notes. Not a prompt cookbook, not a humanizer plugin, and not a creative-writing course.

**Scope:** plans, reviews, reports, decision memos, READMEs, and technical docs — in Chinese or English.

---

## What this repo includes / excludes

**Includes:** the review standard, principle pages, short tradition notes, and fictional or de-identified revision cases.  
**Excludes:** raw identifiable drafts, client/employer/project material, and unpublished process ledgers.

Cases must be fictionalized before intake; local drafts live in `inbox/` (not versioned).

---

## vs. humanizer tools

De-AI-ing covers only part of the prose layer. This work covers the full pre-signature judgment: intent, logic, sources, proportion, wording, rhythm, and appropriateness.

---

## Repository map

| Path | Contents |
|---|---|
| [`STANDARD.md`](STANDARD.md) | Task modes + veto + eight dimensions + final judgment |
| [`principles/`](principles/) | One file per dimension |
| [`notes/`](notes/) | Process notes: veto, evidence ladder, CARS, Warrant, MECE, … |
| [`cases/`](cases/) | Before/after revision cases (de-identified) |
| [`traditions/`](traditions/) | Classic excerpts mapped to AI drafting |
| [`skills/pre-sign-review/`](skills/pre-sign-review/) | Full pre-sign review (veto → eight dims) |
| [`skills/ai-prose-detect/`](skills/ai-prose-detect/) | Fast scan for AI-ish / stale prose signals |
| [`skills/mock-reader/`](skills/mock-reader/) | Mock-reader paraphrase and questions |
| [`skills/case-intake/`](skills/case-intake/) | Draft cases from before/after edits |
| [`scripts/`](scripts/) | Case checks, prose heuristics, dimension coverage |

Local drafts go in [`inbox/`](inbox/) (gitignored). See [`CHANGELOG.md`](CHANGELOG.md) and [`MAINTENANCE.md`](MAINTENANCE.md).

### Install skills

Copy each folder under `skills/` into your Agent skills path (on Windows, replace `~` with `%USERPROFILE%`):

```text
Cursor:      ~/.cursor/skills/pre-sign-review
             ~/.cursor/skills/ai-prose-detect
             ~/.cursor/skills/mock-reader
             ~/.cursor/skills/case-intake
Claude Code: ~/.claude/skills/...
Codex:       ~/.codex/skills/...
```

### Local checks

```bash
python -m unittest discover -s tests -v
python scripts/check_cases.py
python scripts/case_coverage.py
```

---

## Status

| Item | Value |
|---|---|
| Version | `0.7.0` |
| Cases | `11` |
| Tradition notes | `15` |
| Process notes | `13` |
| Skills | `4` |
| Last revision | `2026-07-21` (full dim case coverage + pre-sign-review) |

---

## License

- **Code and scripts:** [MIT License](LICENSE)
- **Standard, principles, cases, traditions, and other text:** [CC BY 4.0](LICENSE-CONTENT)

Chinese README: [`README.md`](README.md).
