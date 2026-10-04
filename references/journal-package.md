## Journal Package Mode

Use `journal-package` after QA and optional pre-submission review are complete.
This mode prepares first-submission files for a target journal or a generic
submission bundle. It is formatting and packaging oriented; content changes
should be raised as blockers rather than silently made.

Core rule: preserve content while enforcing target-journal packaging
requirements.

Minimum procedure:

1. Establish package inputs: QA Gate Report, Manuscript Draft Package or
   Style-Polished Manuscript Draft Package, target journal or article type,
   citation style, author/title page needs, figure and supplement files, and
   render workflow.
2. Check target-journal requirements when supplied: word limits, abstract
   structure, reference style, figure/table placement, reporting checklist,
   funding, COI, ethics, data availability, code availability, acknowledgments,
   AI disclosure, and supplementary-material rules.
3. Render or assemble requested formats when tooling exists, such as DOCX,
   PDF, Markdown, LaTeX, bibliography, figures, and supplements.
4. Prepare submission text assets: title page, abstract/keywords when not
   already final, cover letter draft, author contributions, funding/COI/data
   availability/ethics statements, and AI disclosure when needed.
5. Produce a submission checklist. If content-level issues appear, return to
   `draft` or `qa`; do not hide them in formatting.
6. Produce the handoff artifact, named conceptually **Journal Submission
   Package**.

Default handoff artifact: **Journal Submission Package** with these sections or
metadata:

- Target journal and article type
- Final manuscript file paths
- Figure/table/supplement file paths
- Cover letter path or text
- Required statements
- Citation/reference style status
- Journal checklist and blockers
- Commands run and render status
