# Quality AI Writing

A review framework for plans, reviews, reports, decision memos, READMEs, and technical documentation in Chinese or English.

Before a knowledge-work document carries an author's name, it should make its question, judgment, evidence, and boundary clear. This repository maintains standards, revision cases, source notes, and small tools for that review.

For project status, scope, feedback, and public-material boundaries, see [`STATUS.md`](STATUS.md).

## Sources and their use

The repository gives priority to traceable primary texts, established writing works, authors' own essays, published institutional guidance, and signed articles in formal publications or established media. The [Chinese source index](traditions/chinese-style-sources.md) records each Chinese source, its publication or access route, and how this repository uses it.

Sources help identify a writing problem. They do not replace fact checking or professional judgment. Quotations, repository paraphrases, and repository rules are labeled separately; no rule here claims to speak for any one author or source.

## Scope

Use the framework to draft, revise, or review knowledge-work documents. It does not replace fact verification, domain review, legal or compliance review, or the author's responsibility for what they sign.

## Contents

- A maintainable review standard, principle notes, and process notes
- Fictional or de-identified before-and-after revision cases
- Source descriptions, necessary short quotations, and paraphrases
- Installable review skills and validation scripts

The repository excludes identifiable client, employer, or project material, unpublished drafts, and unredacted working records. Keep local drafts in [`inbox/`](inbox/); that directory is not versioned.

## The place of “de-AI-ing”

Stock phrasing, translationese, and vague connectors are prose problems. This framework also checks judgment, reasoning, sources, claim strength, selection, and fit for the reader. Do not remove necessary terms, conditions, numbers, or responsible parties merely to make prose sound less machine-generated.

## Repository map

| Path | Contents |
|---|---|
| [`STANDARD.md`](STANDARD.md) | The complete pre-sign review standard |
| [`principles/`](principles/) | Eight review dimensions: definition, questions, common problems, and repairs |
| [`notes/`](notes/) | Short notes on drafting, structure, reasoning, revision, and readers |
| [`cases/`](cases/) | Fictional or de-identified revision cases |
| [`traditions/`](traditions/) | Source descriptions and writing references |
| [`skills/`](skills/) | Pre-sign review, prose signals, mock reader, and case-intake skills |
| [`scripts/`](scripts/) | Case validation and heuristic scans |

## Using the repository

1. Read [`STANDARD.md`](STANDARD.md) to set the document's purpose, reader, and risk.
2. For consequential documents, do a veto scan first and then review the eight dimensions.
3. Use a skill for a focused check. To add a case, de-identify it locally first and follow [`MAINTENANCE.md`](MAINTENANCE.md).
4. Run local checks:

```bash
python -m unittest discover -s tests -v
python scripts/check_cases.py
python scripts/case_coverage.py
```

## Status

| Item | Current value |
|---|---|
| Version | `0.8.1` |
| Cases | 11 |
| Source and writing references | 19 |
| Skills | 4 |
| Last revision | 2026-07-29: Chinese source index and public Chinese-copy review |

See [`CHANGELOG.md`](CHANGELOG.md) for revisions and [`MAINTENANCE.md`](MAINTENANCE.md) for intake and maintenance rules.

## License

- **Code and scripts:** [MIT License](LICENSE)
- **Standards, principles, cases, notes, and source descriptions:** [CC BY 4.0](LICENSE-CONTENT)

Chinese README: [`README.md`](README.md).
