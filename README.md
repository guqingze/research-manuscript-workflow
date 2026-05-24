# Research Manuscript Workflow

A Codex skill for managing research manuscript projects as a reproducible
artifact workflow, from literature search and reference curation through
manuscript drafting, QA, journal packaging, revision, and resubmission.

The skill is designed for project repositories where manuscript work depends on
stable inputs such as literature indexes, analysis outputs, tables, figures,
draft files, and QA reports.

## When To Use

Use this skill when a manuscript project needs a structured workflow across one
or more of these stages:

- literature search and candidate-source tracking
- full-text acquisition and reference-manager reconciliation
- literature index refresh
- gap synthesis and manuscript positioning
- analysis result refresh and manuscript handoff
- SAP/outline planning
- manuscript drafting
- style polishing for clarity and author voice
- factual, citation, data, and render QA
- pre-submission review
- journal submission packaging
- reviewer-comment revision planning
- revised manuscript and response-package preparation

For broad research ideation, Socratic research-question refinement, systematic
review design, or general academic-paper assistance outside a specific project
repo, use a broader academic research workflow first. Once the project has a
clear manuscript frame and repo artifacts, this skill becomes the operating
workflow.

## Workflow Modes

The skill routes requests to the smallest useful mode:

| Mode | Purpose |
|---|---|
| `setup` | Discover or document a project manuscript workflow |
| `literature-search` | Search for candidate papers before Zotero/indexing |
| `literature-acquisition` | Track manual full-text collection into a reference manager |
| `literature-refresh` | Refresh reference membership, citation keys, PDF/cache status, or summaries |
| `gap-synthesis` | Synthesize the research gap and manuscript positioning |
| `analysis-refresh` | Regenerate, reconcile, and interpret current project results |
| `sap-outline` | Build the controlling manuscript plan |
| `draft` | Draft manuscript prose from controlled inputs |
| `style-polish` | Improve readability and author voice without changing scientific meaning |
| `qa` | Audit claims, citations, data outputs, figures, tables, and render readiness |
| `pre-submission-review` | Critique manuscript merit and likely reviewer objections |
| `journal-package` | Prepare first-submission journal files |
| `revision-plan` | Parse editor, reviewer, or major coauthor comments into an action roadmap |
| `revise` | Apply an approved revision plan with traceability |
| `response-package` | Assemble resubmission files and point-by-point responses |
| `handoff` | Produce a concise final status or archive note |

## Core Artifacts

The workflow keeps major responsibilities separated into explicit artifacts:

- Literature search record
- Literature acquisition queue
- Literature index
- Gap synthesis
- Analysis Refresh Report
- SAP/Outline Controller
- Manuscript Draft Package
- Style-Polished Manuscript Draft Package
- QA Gate Report
- Pre-Submission Review Report
- Journal Submission Package
- Revision Roadmap
- Revised Manuscript Draft Package
- Response Package
- Handoff note

This separation helps future sessions continue from the right state without
rediscovering literature, rerunning analyses unnecessarily, or mixing
interpretation, planning, and final prose in one document.

## Installation

Clone or copy this repository into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills/research-manuscript-workflow
cp SKILL.md ~/.codex/skills/research-manuscript-workflow/SKILL.md
```

Or clone the repository directly:

```bash
git clone https://github.com/guqingze/research-manuscript-workflow.git ~/.codex/skills/research-manuscript-workflow
```

Restart Codex or reload skills after installation.

## Updating

If installed by cloning:

```bash
cd ~/.codex/skills/research-manuscript-workflow
git pull
```

If maintaining a local development copy, edit `SKILL.md`, commit the change,
push to GitHub, then pull or copy the updated file into the Codex skills
directory.

## Publishing Note

This repository is safe to keep private while the workflow is still evolving.
Before making it public, review `SKILL.md` for local paths, private project
names, unpublished manuscript details, reference-manager collection keys, or
institution-specific workflow notes.

## License

No license has been specified yet. Add one before publishing publicly if you
want others to reuse or adapt the skill.
