## Recommended Repo Documentation

Keep the reusable workflow in this skill; store project-specific details and
artifacts in the repo. **Group repo docs by their role in the workflow** so
lifecycle stages stay visible and artifacts do not scatter into one folder. The
default layout (adapt names to repo convention):

- `AGENTS.md`: short operational rules for future LLM threads, including a
  documentation map pointing to each artifact below.
- `README.md`: concise user-facing pointer to the workflow, layout, and literature index.

Separate three top-level concerns so the analysis engine, source references, and
the manuscript lifecycle do not blur:

- `docs/analysis/` — the analysis engine (not manuscript-stage-specific):
  - `pipeline.md`: data flow and the script-by-script walkthrough of the actual
    pipeline (the code-linked "follow it without reading the code" map). This is
    the single home for the pipeline description; do not duplicate it into the SAP.
  - `methodology.md`: QC rules, cutoffs, harmonization, missing-data handling, and
    statistical-method rationale.
  - `data_dictionary.md`: variables in the project's derived datasets; cross-link
    the raw-source reference so the derived-vs-source boundary is explicit.
- `docs/reference/` — raw source references (source-table/covariate inventories,
  data-provider user guides); a header on each states its boundary against the
  derived data dictionary.
- `docs/literature/` — the literature corpus: dated search records, index,
  markdown cache + manifest, and optionally the evidence-extraction cache; PDFs
  stay in the reference manager.
- `docs/manuscript/` — the research→manuscript lifecycle, one folder per role so
  the phases are legible:
  - `workflow.md`: exact project workflow, paths, collection keys, update
    commands, and QA checklist.
  - `gaps/` — gap synthesis.
  - `plan/` — `outline.md` (manuscript argument, sections, table/figure plan),
    `sap.md` (prespecified statistical analysis plan — kept stable; links to
    `docs/analysis/pipeline.md` rather than restating it), and the
    planned-analyses roadmap.
  - `results/` — the Analysis Refresh Report (the results ledger; no framing).
  - `reflection/` — the reflection memo and any internal-meeting-feedback digest.
  - `narrative/` — the canonical narrative deck package, or a navigation pointer
    when meeting packages live elsewhere; never a second editable copy.
  - `draft/` — manuscript draft(s), supplement, and reporting checklists (e.g.,
    STROBE); rendered outputs go to the repo's manuscript output directory.
  - `qa/` — QA Gate Report and Pre-Submission Review Report when produced.
  - `archive/` — superseded drafts and artifacts.

This is an artifact-role map, not a requirement to create duplicate physical
folders. A project may version selected, curated meeting packages under
`outputs/presentations/<meeting>/`, keeping editable Markdown and display assets
together with narrow Git exceptions. Manuscript Markdown and rendered Word are
different roles; declare which is editable. Keep reusable builders in purpose
groups under `scripts/`, with a task-oriented index distinguishing current entry
points, helpers, historical recipes and compatibility tools. See
[repository organisation](repository-organisation.md) for migration,
preservation and validation guidance.

Splitting the controller into `outline.md` + `sap.md` is recommended when the
combined document grows unwieldy or the argument and the statistical plan update
on different cadences; keep them tightly cross-linked so structure and analysis
stay consistent. Small projects may keep a single combined SAP/Outline Controller,
and single-file roles need not be foldered until they grow.

Project-specific docs should record: the canonical reference collection name and
key; that the reference manager holds canonical PDFs while the repo holds only a
derived markdown cache (or the repo-specific override); the markdown cache,
manifest, and conversion command; literature search-record, acquisition-queue,
and index paths plus the index regeneration command; the path to each lifecycle
artifact above (gap synthesis, planned-analyses roadmap, Analysis Refresh Report,
reflection memo, outline/SAP, narrative deck, draft package, style-polished
package, QA Gate Report, Pre-Submission Review Report, Journal Submission Package,
and post-review Revision Roadmap / Revised Draft / Response Package); the
citation/live-reference workflow; and the QA checks required before manuscript
handoff.
