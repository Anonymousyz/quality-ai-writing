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
| [`notes/`](notes/) | Process notes: modes, structure, revision, paragraph, reader, scenes |
| [`cases/`](cases/) | Before/after revision cases (de-identified) |
| [`traditions/`](traditions/) | Classic excerpts mapped to AI drafting (9 notes) |
| [`skills/case-intake/`](skills/case-intake/) | Agent skill to draft cases from edits |

Local drafts go in [`inbox/`](inbox/) (gitignored). See [`CHANGELOG.md`](CHANGELOG.md) and [`MAINTENANCE.md`](MAINTENANCE.md).

### Install the case-intake skill

Copy this repo’s `skills/case-intake` folder into your Agent skills path (on Windows, replace `~` with `%USERPROFILE%`):

```text
Cursor:      ~/.cursor/skills/case-intake
Claude Code: ~/.claude/skills/case-intake
Codex:       ~/.codex/skills/case-intake
```

---

## Status

| Item | Value |
|---|---|
| Version | `0.3.0` |
| Cases | `3` |
| Tradition notes | `9` |
| Process notes | `7` |
| Last revision | `2026-07-21` (consensus notes + rule admission + Zhu/Ye/Pinker) |

---

## License

- **Code and scripts:** [MIT License](LICENSE)
- **Standard, principles, cases, traditions, and other text:** [CC BY 4.0](LICENSE-CONTENT)

Chinese README: [`README.md`](README.md).
