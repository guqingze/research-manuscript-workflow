# Manuscript Production

## Draft Mode

Use `draft` after a SAP/Outline Controller exists, or when the user explicitly
asks for a partial section draft from available controlling materials. This mode
executes prose from the controller; it does not rediscover the argument.

Core rule: follow the SAP/Outline Controller. If the controller conflicts with
the gap synthesis or Analysis Refresh Report, flag the conflict before drafting
the affected claim.

Minimum procedure:

1. Confirm inputs: SAP/Outline Controller, gap synthesis, Analysis Refresh
   Report, literature index/reference collection, current tables/figures, and
   any journal or word-count instructions. Read paper content from the markdown
   cache; open the reference-manager PDF only to verify exact wording or numbers.
2. Draft section by section. For each section, use the controller's purpose,
   assigned claims, citations, results, tables/figures, word count, and
   transition logic.
3. Use source-specific inputs by section:
   - Introduction: gap synthesis, positioning claim, and verified literature
     index entries.
   - Methods: SAP, cohort/data definitions, endpoint/exposure definitions, and
     analysis provenance.
   - Results: Analysis Refresh Report only; avoid interpretation that belongs
     in Discussion.
   - Discussion: gap synthesis plus Analysis Refresh Report; separate evidence,
     inference, limitations, implications, and future work.
4. Track placeholders and unresolved items inline or in a draft log. Do not
   invent citations, numbers, table references, or methods details.
5. Preserve citation discipline. Use citation keys or live-reference workflow
   when available, and keep claims traceable to the literature index or analysis
   outputs.
6. Track word counts by section and report deviations from the controller.
7. Run a pre-QA self-check before handoff:
   - every major claim has a citation or analysis-output source;
   - table/figure references exist;
   - Results wording does not overinterpret;
   - Discussion hedging matches evidence strength;
   - unresolved placeholders are listed.
8. Produce the handoff artifact, named conceptually **Manuscript Draft Package**.
   This package feeds `style-polish` when prose quality or author voice needs
   attention, otherwise `qa`.

Default handoff artifact: **Manuscript Draft Package** with these sections or
metadata:

- Draft path and render path if available
- Source inputs used
- Section word counts and deviations
- Citation workflow used
- Table/figure references used
- Placeholder and unresolved-item log
- Known limitations before QA

## Style Polish Mode

Use `style-polish` after `draft` or `revise` when the manuscript needs a
readability, tone, or author-voice pass before QA. This mode improves prose
quality without changing the scientific argument, results, citations, or
disclosure obligations.

Core rule: polish for clarity and author voice, not for AI-detector evasion or
to hide AI assistance. If the project or target journal requires AI-use
disclosure, preserve or flag that requirement.

Minimum procedure:

1. Establish inputs: Manuscript Draft Package or Revised Manuscript Draft
   Package, SAP/Outline Controller, gap synthesis, Analysis Refresh Report,
   literature index, author writing samples if available, target journal style
   if known, and render workflow.
2. Lock scientific content before editing. Preserve numbers, denominators,
   effect estimates, confidence intervals, p-values, endpoint definitions,
   table/figure references, citation keys, and section-level claims unless the
   user explicitly requests scientific revision through `draft` or `revise`.
3. Calibrate style from author samples when available. Treat the style profile
   as a soft guide; discipline conventions, journal instructions, and factual
   clarity override personal style preferences.
4. Run a writing-quality sweep inspired by ARS writing-quality checks:
   - replace generic high-frequency academic filler only when a more precise
     phrase is available;
   - remove throat-clearing openers and meta-commentary such as "this section
     discusses" when the section can simply make the point;
   - reduce inflated novelty or importance language not supported by the gap
     synthesis or Analysis Refresh Report;
   - avoid monotonous rule-of-three lists, repeated paragraph templates,
     synonym cycling, and overused binary contrasts;
   - control punctuation tics such as excessive em dashes, semicolons, and
     colon-list sequences;
   - vary sentence and paragraph rhythm where doing so improves readability,
     while accepting more uniform prose in procedural Methods text.
5. Preserve academic register. Do not make epidemiology, clinical, statistical,
   or methods prose conversational when precision is more important than
   rhythm. For epidemiology, clinical-epidemiology, or population-health
   manuscripts, also read `references/epidemiology-manuscript-discipline.md` and
   apply its section discipline, causal-language restraint, internal-language
   scrub, and phrase replacements; consult the project's epi revision-lessons
   file if one exists.
6. Maintain traceability. If a sentence becomes smoother but less obviously
   tied to a citation or output, revise again or flag it for QA rather than
   leaving a polished but unsupported claim.
7. Record risky edits separately. If polishing would require changing meaning,
   adding interpretation, deleting a caveat, or weakening a required limitation,
   leave the passage unchanged and list it as an unresolved awkward passage.
8. Produce the handoff artifact, named conceptually **Style-Polished
   Manuscript Draft Package**. This package feeds `qa`.

Default handoff artifact: **Style-Polished Manuscript Draft Package** with
these sections or metadata:

- Source draft or revised draft path
- Polished draft path and render path if available
- Author style sample status
- Style changes summary
- Preserved facts, citations, numbers, and table/figure references check
- Section word count changes
- Unresolved awkward passages
- Warnings where polishing risks changing meaning
- Disclosure or journal-style notes

## QA Gate Mode

Use `qa` after a Manuscript Draft Package, Style-Polished Manuscript Draft
Package, or Revised Manuscript Draft Package exists. This mode is the
manuscript integrity and readiness gate. It verifies that the draft is
traceable to the reference collection, literature index, Analysis Refresh
Report, generated outputs, and SAP/Outline Controller.

Core rule: audit factual readiness, not manuscript merit. Do not perform peer
review, editorial scoring, or broad rewriting unless the user also asks for a
revision mode.

Minimum procedure:

1. Establish QA inputs: Manuscript Draft Package, Style-Polished Manuscript
   Draft Package, or Revised Manuscript Draft Package, draft/render paths,
   SAP/Outline Controller, gap synthesis, Analysis Refresh Report, literature
   index/reference collection, generated tables/figures, and render workflow.
2. Run claim QA:
   - classify major claims as literature-backed, analysis-backed, mixed, or
     unsupported;
   - verify that analysis-backed claims match the Analysis Refresh Report and
     generated outputs;
   - verify that literature-backed claims map to citation keys or reference
     records;
   - flag overreach, especially causal language, exaggerated novelty, or
     Discussion claims stronger than the evidence;
   - for epidemiology, clinical-epidemiology, or population-health manuscripts,
     apply `references/epidemiology-manuscript-discipline.md`: verify Results
     carry no interpretation or limitations, causal wording matches the design,
     internal/data-layer language is absent from prose, and references are
     numbered by first appearance.
3. Run citation QA:
   - check in-text citations against the reference collection or literature
     index;
   - identify orphan in-text citations and orphan references when a reference
     list is present;
   - check DOI/PMID/URL or metadata completeness when available;
   - flag cited sources with missing PDFs/cache entries if the repo requires
     local source verification.
4. Run claim-source alignment on important cited claims (the **citation-verification
   discipline**, applied here and during `draft`, `reflect`, and `narrative-deck`).
   Distinguish "reference exists" from "the source supports this sentence." Use the
   markdown cache for context and the canonical reference-manager PDF or
   authoritative metadata to verify exact wording; mark unverified items explicitly.
   Specifically:
   - verify the source supports the *specific* outcome, subgroup, direction, and
     magnitude claimed — not merely the general topic (a real failure mode is a
     citation that is right about the topic but wrong about which outcome or group,
     e.g. attributing a steatosis finding to a paper's fibrosis result);
   - catch misattribution across papers and fabricated or drifted numbers;
   - for a "well-established"/"known" claim asserted without a cite, either anchor
     it to a record already in the library or flag that a source must be added —
     do not invent a citation not in the reference collection;
   - prefer per-claim citation so each assertion is independently checkable.
5. Run data and output QA:
   - numbers, denominators, cohort counts, model labels, and p-values/CIs must
     match generated outputs;
   - table and figure references must point to existing files;
   - captions must match the current output and denominator;
   - main-vs-supplement placement must match the SAP/Outline Controller.
6. Run draft package QA:
   - section word counts and deviations are recorded;
   - placeholders and unresolved items are listed;
   - table/figure references and citation workflow are documented;
   - render status is checked when a render path or command exists.
7. Assign a gate verdict:
   - `PASS`: ready for the next packaging/review mode;
   - `PASS_WITH_WARNINGS`: usable, with listed warnings for human review;
   - `BLOCKED`: must fix blockers before packaging or handoff.
8. Produce the handoff document, named conceptually **QA Gate Report**. This
   report feeds `pre-submission-review`, `journal-package`, or
   `response-package` depending on the lifecycle branch.

Default handoff document: **QA Gate Report** with these sections:

- Verdict
- Claim QA
- Citation QA
- Claim-source alignment checks
- Data and output QA
- Draft package and render QA
- Blockers
- Warnings
- Handoff readiness

## Pre-Submission Review Mode

Use `pre-submission-review` after `qa` and before `journal-package` when the
user wants reviewer-style critique before first submission. This mode evaluates
manuscript merit and likely reviewer concerns; it does not replace QA and does
not rewrite the manuscript unless the user asks for a follow-on revision.

Core rule: critique the manuscript as a manuscript, not as a data audit.

Minimum procedure:

1. Establish review inputs: QA-passed Manuscript Draft Package or
   Style-Polished Manuscript Draft Package, QA Gate Report, SAP/Outline
   Controller, gap synthesis, Analysis Refresh Report, target journal or
   article type if known, and any author priorities.
2. Assess journal fit and contribution: audience, novelty, scope, article type,
   and whether the stated contribution follows from the literature gap and
   results.
3. Assess manuscript argument: Introduction problem framing, Results logic,
   Discussion interpretation, limitation handling, and whether the strongest
   claims are defensible.
4. Assess methods and reporting clarity at a manuscript level. Do not rerun
   analyses; instead flag unclear design, missing reporting, or weak explanation
   that a reviewer would notice.
5. Identify strongest likely reviewer objections, including methodology,
   novelty, generalizability, causal overreach, endpoint definitions, analysis
   hierarchy, and missing literature comparisons.
6. Prioritize recommended fixes as must-fix, should-fix, or optional. Keep
   factual integrity issues linked back to the QA Gate Report.
7. Produce the handoff document, named conceptually **Pre-Submission Review
   Report**. This report can feed `draft` for targeted improvements or
   `journal-package` if only minor warnings remain.

Default handoff document: **Pre-Submission Review Report** with these sections:

- Journal fit and contribution
- Major strengths
- Must-fix issues before submission
- Should-fix issues
- Optional improvements
- Likely reviewer objections
- Recommended next mode: `draft`, `qa`, or `journal-package`

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

## Artifact Contracts

- **Pre-Submission Review Report**: journal fit, contribution assessment,
  manuscript strengths, must-fix issues, should-fix issues, optional
  improvements, likely reviewer objections, and recommended next mode.

### Phase 3 — Manuscript production (mostly linear)

8. **Draft the manuscript**
   - Structure from the SAP/Outline Controller.
   - Frame the introduction and discussion from the gap synthesis and literature index.
   - Write results from the Analysis Refresh Report and current generated outputs.
   - Track section word counts, placeholders, citation workflow, and table/figure references in the Manuscript Draft Package.
   - Insert or preserve live citations through the reference manager when available.
   - Save rendered manuscript drafts in the repo’s manuscript output directory.

9. **Polish style when needed**
   - Use `style-polish` after `draft` when the manuscript needs clearer rhythm, author-voice calibration, or removal of generic AI-flavoured prose patterns.
   - Scientific-content preservation during style-polish: see SKILL.md, Workflow overview.
   - Treat this as a prose-quality pass, not as AI-detector evasion.
   - If polishing exposes content uncertainty, route back to `draft` before QA.

10. **QA before first submission**
   - Produce a QA Gate Report from the latest Manuscript Draft Package, Style-Polished Manuscript Draft Package, or Revised Manuscript Draft Package.
   - Confirm each major claim is backed by either the Analysis Refresh Report/output or a cited literature record.
   - Confirm citations map to the canonical reference collection and important cited claims are source-aligned where feasible.
   - Confirm cited tables and figures exist and match current outputs, captions, denominators, and SAP placement.
   - Confirm local PDF cache mismatches are either fixed or explicitly listed by the index.
   - Re-render the manuscript after final edits when render tooling exists.
   - Proceed to `pre-submission-review` or `journal-package` only when the QA verdict is `PASS` or the user explicitly accepts `PASS_WITH_WARNINGS`.

11. **Review before first submission when requested**
   - Use `pre-submission-review` to critique journal fit, contribution, argument quality, methods/reporting clarity, likely reviewer objections, and recommended fixes.
   - If major issues are found, route back to `draft` and then `qa`.
   - If only minor or accepted warnings remain, proceed to `journal-package`.

12. **Prepare first-submission package**
   - Use `journal-package` to apply target journal requirements, render final files, assemble figures/tables/supplements, draft cover letter, and prepare required statements.
   - Keep content changes out of packaging; route content blockers back to `draft` or `qa`.
   - Submit externally outside this workflow.

