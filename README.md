# Research Manuscript Workflow

An agent skill for managing research manuscript projects as a reproducible
artifact workflow, from literature search and reference curation through
manuscript drafting, QA, journal packaging, revision, and resubmission.

The skill is a plain `SKILL.md` (YAML frontmatter + Markdown body) plus a
`references/` directory and an `agents/openai.yaml` descriptor. This is the format
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

The skill routes requests to the smallest useful mode, grouped by phase
(`setup` is a cross-phase preamble):

| Mode | Purpose |
|---|---|
| `setup` | Discover, document or reorganise artifact ownership, folders and script entry points |
| **Phase 1: literature** | |
| `literature-search` | Dated, auditable search; candidate table and acquisition queue for the human |
| `literature-ingest` | Sync the reference manager into the markdown cache, manifest and index |
| `evidence-extraction` | Anchored extraction of key papers into a verifiable cache (token-heavy) |
| `gap-synthesis` | Synthesize the research gap and manuscript positioning |
| **Phase 2: research iteration** | |
| `analysis-plan` | Triage analyses not yet run, with an availability and power audit |
| `analysis-refresh` | Regenerate, reconcile and report current results |
| `reflect` | Argue results against literature and meeting feedback; put scope options to the authors |
| `sap-outline` | Build the controlling manuscript plan from agreed scope |
| `narrative-deck` | Rehearse the storyline before drafting |
| **Phase 3: production and revision** | |
| `draft` | Draft manuscript prose from controlled inputs |
| `style-polish` | Improve readability and author voice without changing scientific meaning |
| `qa` | Audit claims, citations, data outputs, displays and render readiness |
| `pre-submission-review` | Critique merit and likely reviewer objections |
| `revision-plan` | Parse editor, reviewer or coauthor comments into a roadmap |
| `revise` | Apply an approved roadmap with traceability |
| `package` | First-submission files, resubmission bundle, or final handoff note |

## Core Artifacts

Literature search record and acquisition queue; literature index and markdown
cache; evidence-extraction cache; gap synthesis; planned-analyses roadmap;
Analysis Refresh Report; reflection memo; SAP/Outline Controller; narrative
deck; draft packages; QA Gate Report; Pre-Submission Review Report; Revision
Roadmap; submission or response package.

Keeping these separate lets a future session continue from the right state
without rediscovering literature, rerunning analyses, or mixing interpretation,
planning and prose. When scope changes materially, start a new dated search
record; refreshing the index is not a search.

## Repository Layout

For project structure and refactoring, see
[repository organisation](references/repository-organisation.md): one editable
home per artifact, meeting text and assets together, purpose-grouped scripts,
and source-preserving migration checks. The suggested lifecycle roles do not
require duplicate docs/output folders. Markdown-only meeting packages are fully
supported.

```
research-manuscript-workflow/
├── SKILL.md                                       # the skill: artifacts, mode router, shared rules, and workflow overview
├── agents/openai.yaml                             # Codex descriptor (display name, default prompt)
├── references/
│   ├── modes-literature.md                        # search, ingest, gap synthesis, and evidence extraction
│   ├── modes-research-iteration.md                # analysis planning, results refresh, reflection, SAP, and narrative deck
│   ├── modes-manuscript-production.md             # drafting, style polish, QA, and pre-submission review
│   ├── modes-revision.md                          # revision planning, revision, and packaging (submission, resubmission, handoff)
│   ├── repository-organisation.md                 # artifact ownership, meeting packages, script navigation, safe migration, and recommended repo docs
│   ├── epidemiology-manuscript-discipline.md      # applied during style-polish and qa for epi, clinical-epi, and population-health manuscripts
│   └── evidence-extraction-contract.md            # schema, anchor rules, and worker prompt for evidence extraction
└── scripts/
    ├── verify_extract_anchors.py                  # mechanical anchor checker for the evidence-extraction cache
    └── requirements.txt                           # Python deps for the scripts
```

`SKILL.md`, `references/`, and `scripts/` are tool-neutral. `agents/openai.yaml`
is only read by Codex; Claude Code and other agents ignore it.

## Installation

Both Claude Code and Codex discover skills under their own home directory
(`~/.claude/skills/<name>` and `~/.agents/skills/<name>`). Rather than copying the
files into each one, keep this repository as the single source of truth and
symlink it into both, so edits here are live everywhere with no re-sync step.

```bash
# Point this at wherever you cloned the repo:
REPO="$HOME/GitHub/research-manuscript-workflow"

# Claude Code
mkdir -p ~/.claude/skills
ln -s "$REPO" ~/.claude/skills/research-manuscript-workflow

# Codex
mkdir -p ~/.agents/skills
ln -s "$REPO" ~/.agents/skills/research-manuscript-workflow
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
- Codex's [official skills documentation](https://learn.chatgpt.com/docs/build-skills)
  lists the user-level location as `USER | $HOME/.agents/skills` and states:
  “Codex supports symlinked skill folders and follows the symlink target when
  scanning these locations.”
- Prefer a copy over a symlink? Substitute `cp -R "$REPO" <target>` for either
  `ln -s` line; you then re-copy after each change instead of editing in place.

### Migrating an existing Codex link

The official documentation does not state whether the old directory
`~/.codex/skills` is still read. If you previously linked to the old directory,
we recommend linking to the new directory instead.

The script removes the old path only if it is a symbolic link whose recorded
target exactly matches `REPO`. Otherwise it prints an explanation and stops.
It also stops if the new path already exists, including a dangling link.

```bash
(
  REPO="$HOME/GitHub/research-manuscript-workflow"
  OLD_LINK="$HOME/.codex/skills/research-manuscript-workflow"
  NEW_LINK="$HOME/.agents/skills/research-manuscript-workflow"

  if [ -e "$NEW_LINK" ] || [ -L "$NEW_LINK" ]; then
    printf '%s\n' "New path already exists; inspect it yourself: $NEW_LINK"
    exit 0
  fi
  if [ ! -L "$OLD_LINK" ]; then
    printf '%s\n' "Old path is not a symbolic link or is absent; nothing changed: $OLD_LINK"
    exit 0
  fi
  if [ "$(readlink "$OLD_LINK")" != "$REPO" ]; then
    printf '%s\n' "Old link does not point exactly to REPO; nothing changed: $OLD_LINK"
    exit 0
  fi

  mkdir -p "$HOME/.agents/skills" || exit 1
  unlink "$OLD_LINK" || exit 1
  ln -s "$REPO" "$NEW_LINK"
)
```

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
