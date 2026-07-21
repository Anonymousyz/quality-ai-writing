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
| [`notes/`](notes/) | Process notes: modes, structure, Warrant, MECE, reader, scenes, … |
| [`cases/`](cases/) | Before/after revision cases (de-identified) |
| [`traditions/`](traditions/) | Classic excerpts mapped to AI drafting (10 notes) |
| [`skills/ai-prose-detect/`](skills/ai-prose-detect/) | Fast scan for AI-ish / stale prose signals |
| [`skills/case-intake/`](skills/case-intake/) | Draft cases from before/after edits |

Local drafts go in [`inbox/`](inbox/) (gitignored). See [`CHANGELOG.md`](CHANGELOG.md) and [`MAINTENANCE.md`](MAINTENANCE.md).

### Install skills

Copy each folder under `skills/` into your Agent skills path (on Windows, replace `~` with `%USERPROFILE%`):

```text
Cursor:      ~/.cursor/skills/ai-prose-detect
             ~/.cursor/skills/case-intake
Claude Code: ~/.claude/skills/...
Codex:       ~/.codex/skills/...
```

---

## Status

| Item | Value |
|---|---|
| Version | `0.4.0` |
| Cases | `3` |
| Tradition notes | `10` |
| Process notes | `9` |
| Skills | `2` (detect + intake) |
| Last revision | `2026-07-21` (Williams, Warrant, MECE, ai-prose-detect) |

---

## License

- **Code and scripts:** [MIT License](LICENSE)
- **Standard, principles, cases, traditions, and other text:** [CC BY 4.0](LICENSE-CONTENT)

Chinese README: [`README.md`](README.md).
