# Quality AI Writing

> Before you sign your name — what makes a knowledge-work document actually good?

A living review standard with de-identified revision cases and bilingual writing-tradition notes. Not a prompt cookbook, not a humanizer plugin, and not a creative-writing course.

**Scope:** plans, reviews, reports, decision memos, READMEs, and technical docs — in Chinese or English.

---

## Boundary

**This repo publishes the review standard and examples only. The full personal writing operating system is not open-sourced; all cases are fictional or de-identified.**

- Public: standard dimensions, review questions, veto rules, tradition excerpts, de-identified cases
- Private: personal writing operating system (SOPs, workflows, real tasks), `inbox/` drafts, raw before/after edits

---

## vs. humanizer tools

De-AI-ing covers only part of the prose layer. This work covers the full pre-signature judgment: intent, logic, sources, proportion, wording, rhythm, and appropriateness.

---

## Repository map

| Path | Contents |
|---|---|
| [`STANDARD.md`](STANDARD.md) | Veto rules + eight dimensions + final judgment |
| [`principles/`](principles/) | One file per dimension |
| [`cases/`](cases/) | Before/after revision cases (de-identified) |
| [`traditions/`](traditions/) | Classic writing notes mapped to AI drafting |
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
| Version | `0.1.0` |
| Cases | `3` |
| Last revision | `2026-07-21` (initial release) |

---

## License

- **Code and scripts:** [MIT License](LICENSE)
- **Standard, principles, cases, traditions, and other text:** [CC BY 4.0](LICENSE-CONTENT)

Chinese README: [`README.md`](README.md).
