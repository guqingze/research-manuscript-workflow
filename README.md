# Research Manuscript Workflow

An agent skill for managing research manuscript projects as a reproducible
artifact workflow, from literature search and reference curation through
manuscript drafting, QA, journal packaging, revision, and resubmission.

The skill is a plain `SKILL.md` (YAML frontmatter + Markdown body) plus a
`references/` file and an `agents/openai.yaml` descriptor. This is the format
Claude Code, Codex, and other `SKILL.md`-based agents read, so the same checkout
works for all of them — see [Installation](#installation).

The skill is designed for project repositories where manuscript work depends on
stable inputs such as literature indexes, analysis outputs, tables, figures,
draft files, and QA reports.

## When To Use

Use this skill when a manuscript project needs a structured workflow across one
or more of these stages:

- literature search and candidate-source tracking
- dated literature-search refreshes when manuscript scope or comparison populations change
- full-text acquisition and reference-manager reconciliation
- literature index refresh
- key-paper evidence extraction into a verifiable cache
- gap synthesis and manuscript positioning
- planned-analyses roadmapping with an availability audit
- analysis result refresh and manuscript handoff
- results-vs-literature reflection and internal-meeting feedback
- SAP/outline planning
- narrative/framing-deck rehearsal before drafting
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

The skill routes requests to the smallest useful mode, grouped by the three
macro-phases (`setup` is a cross-phase preamble):

| Mode | Purpose |
|---|---|
| `setup` | Discover, document or reorganise artifact ownership, folders and script entry points |
| **Phase 1 — Literature foundation** | |
| `literature-search` | Search for candidate papers before Zotero/indexing |
| `literature-acquisition` | Build the human download checklist for searched candidates and reconcile the collection |
| `literature-ingest` | Sync the reference manager into the repo's literature layer: membership + citation keys, markdown cache + manifest, and index |
| `evidence-extraction` | Extract structured evidence from identified key papers into a verifiable cache (token-heavy; subagent fan-out) |
| `gap-synthesis` | Synthesize the research gap and manuscript positioning |
| **Phase 2 — Research iteration loop** | |
| `analysis-refresh` | Regenerate, reconcile, and interpret current project results |
| `analysis-plan` | Triage literature/reviewer-motivated analyses not yet run, with an availability audit |
| `reflect` | Argue current results against the literature, gaps, and internal-meeting feedback |
| `sap-outline` | Build the controlling manuscript plan |
| `narrative-deck` | Rehearse and lock the narrative/framing before drafting (often for an internal meeting) |
| **Phase 3 — Manuscript production** | |
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
- Evidence-extraction cache
- Gap synthesis
- Planned-analyses roadmap
- Analysis Refresh Report
- Reflection memo
- SAP/Outline Controller
- Narrative deck
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

When a manuscript scope changes materially, start a new dated literature-search
record with the exact source, query, date, screening, and count audit trail;
refreshing the literature index alone is not a substitute for searching.

## Repository Layout

For project structure and refactoring, see
[repository organisation](references/repository-organisation.md): one editable
home per artifact, meeting text and assets together, purpose-grouped scripts,
and source-preserving migration checks. The suggested lifecycle roles do not
require duplicate docs/output folders. Markdown-only meeting packages are fully
supported.

```
research-manuscript-workflow/
├── SKILL.md                                       # the skill: frontmatter + workflow body
├── agents/openai.yaml                             # Codex descriptor (display name, default prompt)
├── references/
│   ├── epidemiology-manuscript-discipline.md      # loaded during style-polish and qa for epi manuscripts
│   └── evidence-extraction-contract.md            # schema, anchor rules, and worker prompt for evidence extraction
└── scripts/
    ├── verify_extract_anchors.py                  # mechanical anchor checker for the evidence-extraction cache
    └── requirements.txt                           # Python deps for the scripts
```

`SKILL.md`, `references/`, and `scripts/` are tool-neutral. `agents/openai.yaml`
is only read by Codex; Claude Code and other agents ignore it.

## Installation

Both Claude Code and Codex discover skills under their own home directory
(`~/.claude/skills/<name>` and `~/.codex/skills/<name>`). Rather than copying the
files into each one, keep this repository as the single source of truth and
symlink it into both, so edits here are live everywhere with no re-sync step.

```bash
# Point this at wherever you cloned the repo:
REPO="$HOME/GitHub/research-manuscript-workflow"

# Claude Code
mkdir -p ~/.claude/skills
ln -s "$REPO" ~/.claude/skills/research-manuscript-workflow

# Codex
mkdir -p ~/.codex/skills
ln -s "$REPO" ~/.codex/skills/research-manuscript-workflow
```

Don't have the repo yet? Clone it first, then run the commands above:

```bash
git clone https://github.com/guqingze/research-manuscript-workflow.git \
  "$HOME/GitHub/research-manuscript-workflow"
```

Restart or reload the agent after linking so it re-scans its skills directory.

Notes:

- Claude Code follows symlinks in `~/.claude/skills/` and picks the skill up on
  its next start.
- Codex enumerates `~/.codex/skills/` with a directory check that follows
  symlinks, so a symlinked skill registers as installed. If your Codex build
  does not surface it, replace that one symlink with a real copy
  (`cp -R "$REPO" ~/.codex/skills/research-manuscript-workflow`) and refresh it
  after edits.
- Prefer a copy over a symlink? Substitute `cp -R "$REPO" <target>` for either
  `ln -s` line; you then re-copy after each change instead of editing in place.

## Updating

With the symlink install, there is nothing to re-copy — edit `SKILL.md` (or the
reference file) in this repository and the change is live in both agents on their
next start. To pull upstream changes:

```bash
cd "$HOME/GitHub/research-manuscript-workflow"
git pull
```

If you installed by copying instead of symlinking, re-run the `cp -R` command for
each target after pulling or editing.

## License

© 2026 Qingze Gu

Licensed under [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/)
(CC BY-NC 4.0) — see [`LICENSE`](LICENSE). You may share and adapt the skill with
attribution for non-commercial purposes.
