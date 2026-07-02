---
name: research-manuscript-workflow
description: Use for research manuscript projects that need a reproducible workflow from literature search and Zotero literature collection through literature indexing, gap synthesis, analysis reports, manuscript outline/SAP, Word or document drafting, style polishing, citation QA, and final manuscript artifact generation. Trigger when the user asks to organize, document, reuse, audit, or execute a literature-to-manuscript workflow across research project repositories.
---

# Research Manuscript Workflow

## Core Principle

Separate the manuscript system into artifacts with distinct jobs. Do not let literature synthesis, analysis results, manuscript specification, and final prose collapse into one document.

Use this default artifact model unless the repo already has stronger conventions:

- **Reference manager**: canonical library for paper membership, metadata, attachments, and live citations.
- **Literature search record**: reproducible search strategy, screening decisions, and candidate source corpus before or alongside reference-manager import.
- **Literature acquisition queue**: human-in-the-loop full-text collection checklist that bridges searched candidates to a project reference-manager collection.
- **Literature index**: generated LLM-facing lookup table with citation keys, themes, roles, key claims, caveats, and local attachment status.
- **Gap synthesis**: curated interpretation of the literature and the research gap.
- **Analysis Refresh Report**: current project results only, generated or updated from scripts and outputs, with provenance, interpretation, and manuscript handoff.
- **SAP/Outline Controller**: controlling manuscript structure, analysis hierarchy, section claims, word counts, tables, figures, and main-vs-supplement decisions.
- **Manuscript Draft Package**: draft document generated from the SAP/Outline Controller, gap synthesis, Analysis Refresh Report, and citation index.
- **Style-Polished Manuscript Draft Package**: readability and author-voice pass over a draft or revised draft, with preserved facts, citations, numbers, and scientific meaning.
- **QA Gate Report**: factual integrity and readiness audit for claims, citations, data outputs, tables, figures, and render status.
- **Pre-Submission Review Report**: reviewer-style critique of manuscript merit, journal fit, argument quality, and likely reviewer objections.
- **Journal Submission Package**: target-journal formatted first-submission bundle and submission checklist.
- **Revision Roadmap**: structured post-review plan built from editor, reviewer, or coauthor comments.
- **Revised Manuscript Draft Package**: revised draft plus revision log and response-to-reviewers draft.
- **Response Package**: resubmission bundle with revised manuscript, response letter, updated QA, and journal resubmission checklist.

## Workflow Router

Choose the smallest mode that satisfies the user's request. Do not run the full
workflow when the user asks for one layer only.

| User intent | Mode | Required inputs | Output |
|---|---|---|---|
| Discover or document a project manuscript workflow | `setup` | `AGENTS.md`, `README.md`, project docs | Workflow map, missing pieces, and recommended `docs/manuscript_workflow.md` updates |
| Search for candidate literature before Zotero/indexing | `literature-search` | Research question or scoped topic, databases/sources, inclusion/exclusion criteria | Search strategy, screened candidate corpus, and import/next-search recommendations |
| Assist manual full-text collection into Zotero | `literature-acquisition` | Literature search record, target reference collection name/key | Acquisition queue, missing-item checklist, and missing-PDF attachment notes |
| Refresh reference-manager membership, citation keys, the repo markdown cache, or literature summaries | `literature-refresh` | Reference manager details, PDF→markdown converter, index generator or index path | Updated markdown cache + manifest and literature index, plus mismatch or missing-PDF notes |
| Synthesize or revise the research gap and paper positioning | `gap-synthesis` | Literature index and markdown cache; reference-manager PDFs only to verify | Integrated evidence synthesis, manuscript positioning, CER chains, and SAP implications |
| Refresh project results for manuscript use | `analysis-refresh` | Repo pipeline commands, current outputs, Analysis Refresh Report path | Analysis Refresh Report with run provenance, result validation, interpretation, and manuscript handoff |
| Build or revise the controlling manuscript plan | `sap-outline` | Gap synthesis, Analysis Refresh Report, current tables/figures | SAP/Outline Controller with section structure, argument map, evidence/result map, and main-vs-supplement decisions |
| Draft or revise manuscript prose | `draft` | SAP/Outline Controller, gap synthesis, Analysis Refresh Report, literature index | Manuscript Draft Package in the repo's manuscript output directory |
| Polish manuscript readability and author voice | `style-polish` | Manuscript Draft Package or Revised Manuscript Draft Package, author writing samples if available | Style-Polished Manuscript Draft Package with style changes summary and preserved-content check |
| Audit manuscript readiness | `qa` | Manuscript Draft Package, Style-Polished Manuscript Draft Package, or Revised Manuscript Draft Package, reference collection/index, generated outputs | QA Gate Report with claim, citation, data/output, draft-package, and render readiness checks |
| Critique manuscript before first submission | `pre-submission-review` | QA-passed Manuscript Draft Package or Style-Polished Manuscript Draft Package, SAP/Outline Controller, target journal if known | Pre-Submission Review Report with merit critique and recommended fixes |
| Prepare first-submission journal files | `journal-package` | QA-passed Manuscript Draft Package or Style-Polished Manuscript Draft Package, target journal requirements, render workflow | Journal Submission Package with formatted files, statements, cover letter, and checklist |
| Parse editor/reviewer/coauthor comments | `revision-plan` | Reviewer/editor comments, submitted manuscript package, decision letter if available | Revision Roadmap with prioritized comments and response-letter skeleton |
| Apply an approved revision plan | `revise` | Revision Roadmap, submitted or current Manuscript Draft Package or Style-Polished Manuscript Draft Package, source materials | Revised Manuscript Draft Package with revision log and response draft |
| Prepare resubmission files | `response-package` | Revised draft, Revision Roadmap, QA Gate Report, target journal requirements | Response Package with revised files, response letter, and resubmission checklist |
| Produce final handoff/archive note | `handoff` | Journal Submission Package or Response Package, QA Gate Report, render workflow | Concise handoff/archive note with final paths, commands, limitations, and next actions |

If the request spans multiple modes, start at the earliest affected mode and
state the planned sequence. If the user's current stage is ambiguous, inspect the
repo workflow docs and existing manuscript artifacts before asking for
clarification.

## Literature Search Mode

Use `literature-search` when the user wants to find candidate papers before
curating them in Zotero or generating the literature index. Borrow the
discipline of ARS `deep-research` Phase 2, but keep the output repo-oriented and
ready for reference-manager import and full-text acquisition.

This mode should produce a reproducible search record and a machine-auditable
candidate corpus. It should not assume that PDFs are already available. In
projects where the user retrieves full text through university or institutional
access, make the next human action obvious for each retained source.

Minimum procedure:

1. Define search parameters: research question or scoped topic, databases or
   sources, keywords and synonyms, Boolean strategy, date range, languages, and
   document types.
2. Apply inclusion and exclusion criteria before screening results. Do not
   retrofit criteria to justify already-preferred papers.
3. Screen in two passes when enough metadata is available: title/abstract first,
   then full text or detailed metadata for retained sources.
4. Record reproducibility details: search date, database/source, query string,
   raw hit count, screened count, excluded count, and inclusion reasons for
   retained sources.
5. Verify candidate existence with DOI, publisher, PubMed, Crossref, Semantic
   Scholar, OpenAlex, or another authoritative record when feasible. Mark
   unresolved metadata explicitly instead of inventing it.
6. Make the retained corpus auditable by later `literature-acquisition` and
   `literature-refresh` runs. For each retained source, include stable fields
   such as `source_id`, tier or priority, title, first author, year, journal or
   source, PMID, DOI, URL, manuscript role, verification status, and unresolved
   metadata.
7. Add acquisition handoff fields when the next step is Zotero/PDF collection:
   `target_collection`, `zotero_status`, `pdf_status`, `local_cache_status`,
   and `next_human_action`. Default these to pending or unknown rather than
   implying that the paper has been collected.
8. Separate auditable core sources from reserve or conditional suggestions.
   Mark generic reserve suggestions, such as "add PRS-CS/LDpred2 methods papers
   if needed", as non-auditable so they are not counted as missing
   reference-manager items during later reconciliation.
9. Stop at candidate corpus and search documentation. Do not write the gap
   synthesis, manuscript prose, or literature index unless the user also asked
   for the next mode.

Default output: a search strategy report plus a candidate source table suitable
for Zotero import or manual curation. The table should be stable enough that a
later run can compare it against a Zotero collection by DOI, PMID, URL, and
normalized title without re-parsing prose.

Recommended candidate table columns:

`source_id`, `audit_scope`, `tier`, `priority`, `title`, `first_author`,
`year`, `journal_or_source`, `PMID`, `DOI`, `URL`, `manuscript_role`,
`inclusion_reason`, `verification_status`, `target_collection`,
`zotero_status`, `pdf_status`, `local_cache_status`, `next_human_action`,
`notes`.

## Literature Acquisition Mode

Use `literature-acquisition` after candidate papers have been identified but
before literature indexing. This mode supports a human-in-the-loop full-text
collection workflow where the user may need institutional credentials to access
publisher PDFs.

Minimum procedure:

1. Read the literature search record and identify the auditable core corpus.
   Keep reserve or non-auditable suggestions separate.
2. Resolve or confirm the target reference-manager collection name/key.
3. Generate or update an acquisition queue with stable source IDs, title, PMID,
   DOI, URL, tier or priority, manuscript role, reference-manager status, and
   PDF attachment status.
4. When the reference manager is reachable, compare the queue against the target
   collection by DOI, PMID, URL, and normalized title. Report missing collection
   items separately from items that exist but lack PDF attachments.
5. Help the user work the manual download queue by grouping missing items by
   priority and providing PubMed, DOI, or publisher URLs. If asked, open or list
   target links, but do not handle institutional credentials or bypass paywalls.
6. After the user confirms that records/PDFs have been added to the collection,
   hand off to `literature-refresh` to build the markdown cache from the
   collection's PDFs, write the manifest, and regenerate the literature index.
   PDFs stay in the reference manager; they are not copied into the repo.

Default output: an acquisition checklist or CSV plus a concise list of missing
reference-manager records and missing PDF attachments.

## Gap Synthesis Mode

Use `gap-synthesis` after `literature-refresh` has produced a stable literature
index. This mode performs interpretation across indexed papers. It should make
the manuscript's intellectual position explicit before SAP/outline or drafting.

Core rule: integrate across sources, do not summarize papers sequentially.

Minimum procedure:

1. Build or update a compact evidence matrix before writing prose. Include
   themes, supporting papers, contradicting papers, population or context,
   method type, evidence strength, and manuscript use.
2. Identify convergence, divergence, and silence:
   - convergence: where multiple sources support the same claim;
   - divergence: where sources conflict or imply different boundary conditions;
   - silence: where the indexed literature lacks evidence needed for the
     manuscript's question.
3. Resolve or explain contradictions where possible. Consider population,
   geography, endpoint/exposure definitions, methods, confounding control,
   follow-up period, study quality, and publication date.
4. Classify the gap instead of using vague gap language. Useful types include
   empirical, methodological, definition, temporal, geographic, translation,
   mechanistic, ancestry/population, prospective-cohort, endpoint-harmonization,
   and PRS/generalizability gaps.
5. Produce claim-evidence-reasoning (CER) chains for manuscript-facing claims:
   each claim needs cited evidence, reasoning, caveat or hedge, and suggested
   manuscript section.
6. Run a short stress test before finalizing:
   - Has the synthesis cherry-picked supportive papers?
   - Are contradictions interpreted rather than explained away?
   - Would the gap still stand if the strongest supporting paper were removed?
   - What would a skeptical reviewer say is overstated?
   - Does the proposed gap justify the project's actual analyses?
7. Hand off explicitly to `sap-outline`: state which introduction claims,
   methods justifications, primary analyses, discussion comparisons, and
   supplement-only claims should follow from the synthesis.
8. Stop at synthesis and handoff guidance. Do not write manuscript prose or
   decide final table/figure order unless the user also asked for the next mode.

Default output: an integrated gap synthesis with an evidence matrix,
convergence/divergence map, gap taxonomy, positioning claim, CER chains, stress
test notes, and SAP/outline implications.

## Analysis Refresh Mode

Use `analysis-refresh` when project results need to be regenerated, reconciled,
interpreted, or prepared for manuscript planning. This mode consumes repo
pipelines and generated outputs; it does not invent analyses outside the
project's scripts or controlling SAP.

Core rule: produce a manuscript-ready analysis handoff, not just a prose results
summary.

Minimum procedure:

1. Establish run provenance: commands run or inspected, run label/date, working
   directory, key script paths, input paths, output paths, and relevant
   environment or git context when useful.
2. Check cohort and data contracts: sample counts, exclusion flow, denominators,
   missingness, endpoint/exposure definitions, follow-up windows, and whether
   counts agree across generated tables and QC outputs.
3. Inventory result artifacts: tables, figures, model outputs, logs, and
   manuscript-facing summaries. Label each as primary, secondary, sensitivity,
   exploratory, supplement-only, or not-for-manuscript when the SAP or repo docs
   provide that distinction.
4. Interpret statistical outputs conservatively. Record effect estimates,
   confidence intervals, p-values when present, practical magnitude, direction,
   precision, model adjustment set, and whether assumptions or diagnostics are
   documented.
5. Run a focused fallacy and overclaim scan:
   - causal language unsupported by the design;
   - multiple comparisons without correction or clear exploratory framing;
   - subgroup, endpoint, or ancestry generalization beyond the data;
   - selection, survivorship, collider, or overadjustment concerns;
   - non-significant or imprecise estimates framed as definitive;
   - statistical significance reported without effect size or uncertainty.
6. Verify manuscript consistency: numbers in the report must match current
   generated outputs; table/figure references must exist; captions and
   denominators must match; primary/secondary labels must match the SAP or be
   flagged as unresolved.
7. Produce the handoff document, named conceptually **Analysis Refresh Report**.
   This report feeds `sap-outline` and `draft` and should separate
   Results-ready claims, Discussion-only interpretations, supplement-only
   findings, and unresolved blockers.
8. Stop at analysis reporting and handoff guidance. Do not revise the SAP,
   reorder tables/figures, or draft manuscript prose unless the user also asked
   for the next mode.

Default handoff document: **Analysis Refresh Report** with these sections:

- Run provenance
- Cohort and data checks
- Result artifact inventory
- Statistical interpretation
- Fallacy and overclaim scan
- Manuscript handoff
- Unresolved blockers and recommended next actions

## SAP/Outline Mode

Use `sap-outline` after `gap-synthesis` and `analysis-refresh` have produced
their handoff documents. This mode creates the controlling manuscript plan. It
should decide what goes where, at what priority, and with what evidence; it
should not draft polished prose.

Core rule: structure serves the manuscript argument and the available results.

Minimum procedure:

1. Select or confirm the manuscript structure pattern. For empirical cohort or
   clinical epidemiology work, default to IMRaD unless repo or journal
   instructions require another structure.
2. Define the central manuscript thesis or positioning claim from
   `gap-synthesis`, then decompose it into 3-5 section-level sub-arguments.
3. Map evidence and results to sections:
   - literature claims and CER chains from `gap-synthesis`;
   - Results-ready claims, Discussion-only interpretations, and
     supplement-only findings from the Analysis Refresh Report;
   - tables, figures, model outputs, and sensitivity analyses.
4. Allocate manuscript roles explicitly: primary, secondary, sensitivity,
   exploratory, supplement-only, or not-for-manuscript.
5. Build the section plan. For each section or subsection, record purpose,
   target word count, core claim, required evidence/results, table/figure
   references, citations or citation-key groups, and transition logic.
6. Check argument strength before handing off to drafting:
   - each core claim has evidence and reasoning;
   - counter-arguments or limitations are assigned to Discussion;
   - no Results claim exceeds the Analysis Refresh Report;
   - no Introduction or Discussion claim exceeds the gap synthesis;
   - unresolved decisions are listed instead of silently filled.
7. Produce the handoff document, named conceptually **SAP/Outline Controller**.
   This document is the authority for `draft`.
8. Stop at planning. Do not draft manuscript prose unless the user also asked
   for `draft`.

Default handoff document: **SAP/Outline Controller** with these sections:

- Manuscript target and structure pattern
- Central thesis or positioning claim
- Section-by-section outline with purpose and word counts
- Argument map and CER-to-section mapping
- Evidence/result/table/figure map
- Main-vs-supplement and primary-vs-secondary decisions
- Transition logic
- Drafting instructions and unresolved decisions

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
   rhythm.
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
     Discussion claims stronger than the evidence.
3. Run citation QA:
   - check in-text citations against the reference collection or literature
     index;
   - identify orphan in-text citations and orphan references when a reference
     list is present;
   - check DOI/PMID/URL or metadata completeness when available;
   - flag cited sources with missing PDFs/cache entries if the repo requires
     local source verification.
4. Run claim-source alignment on important cited claims. Distinguish
   "reference exists" from "the source supports this sentence." Use the markdown
   cache for context and the canonical reference-manager PDF or authoritative
   metadata to verify exact wording; mark unverified items explicitly.
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

## Revision Plan Mode

Use `revision-plan` after external editor/reviewer comments or major coauthor
comments arrive. This mode parses unstructured feedback into an actionable
roadmap. It should not revise the manuscript directly.

Core rule: no comment left behind.

Minimum procedure:

1. Collect reviewer/editor/coauthor comments, decision letter if available, the
   submitted manuscript or Journal Submission Package, and any journal deadline.
2. Parse comments into atomic items. Split comments that contain multiple
   actionable requests.
3. Preserve reviewer intent: keep raw comment text, reviewer/editor source,
   paraphrased summary, and ambiguity flags.
4. Classify each item as major, minor, editorial, positive, or unclear. Assign
   priority: must-fix, should-fix, or consider. Promote items raised by the
   editor or multiple reviewers.
5. Map each item to manuscript sections, tables, figures, analyses, references,
   response-letter needs, and whether new analysis or literature work is
   required.
6. Produce a suggested revision order and response-letter skeleton. Flag
   contradictory reviewer requests for user decision.
7. Produce the handoff document, named conceptually **Revision Roadmap**. This
   report feeds `revise`.

Default handoff document: **Revision Roadmap** with these sections:

- Decision and revision context
- Parsed comment inventory
- Must-fix / should-fix / consider tables
- Cross-reviewer patterns
- Section/action map
- New analysis or literature needs
- Suggested revision order
- Response-letter skeleton

## Revise Mode

Use `revise` after a Revision Roadmap exists and the user has approved the
revision strategy. This mode applies the roadmap to the manuscript and records
what changed. It should preserve traceability from each revision to the
reviewer/editor comment it addresses.

Core rule: revise against the approved roadmap, not opportunistically.

Minimum procedure:

1. Establish revision inputs: Revision Roadmap, submitted or current Manuscript
   Draft Package or Style-Polished Manuscript Draft Package, Journal Submission
   Package if available, QA Gate Report, and any newly generated analysis or
   literature artifacts.
2. Address must-fix items first, then should-fix items, then optional items if
   appropriate. Do not silently drop any roadmap item.
3. For each revision item, record action taken, manuscript location, source
   material used, status, and whether the response letter needs explanation.
4. Keep Results revisions tied to the Analysis Refresh Report or regenerated
   outputs; keep literature revisions tied to the literature index or verified
   PDFs.
5. Produce or update response-to-reviewers draft text alongside manuscript
   changes.
6. List unresolved items and rationale. If a comment cannot be addressed without
   new analysis, new literature, or author decision, mark it as blocked.
7. Produce the handoff artifact, named conceptually **Revised Manuscript Draft
   Package**. This package feeds `style-polish` before `qa` when prose changed
   substantially or when the user requests a readability pass; otherwise it
   feeds `qa`.

Default handoff artifact: **Revised Manuscript Draft Package** with these
sections or metadata:

- Revised draft path and render path if available
- Revision log mapped to comment IDs
- Resolved, partially resolved, unresolved, and blocked items
- Response-to-reviewers draft
- Updated placeholders and limitations
- Source inputs and commands used
- Recommended next mode: `qa`

## Response Package Mode

Use `response-package` after a revised manuscript has passed QA. This mode
prepares the resubmission bundle. It is distinct from first-submission
`journal-package` because it must include point-by-point responses and revision
traceability.

Core rule: every reviewer/editor item in the Revision Roadmap must be accounted
for in the response package.

Minimum procedure:

1. Establish response inputs: Revised Manuscript Draft Package, Revision
   Roadmap, QA Gate Report, target journal/resubmission requirements, and any
   requested clean/tracked manuscript files.
2. Finalize point-by-point response letter: quote or summarize each comment,
   state response, state changes made, and list manuscript locations.
3. Assemble clean revised manuscript and tracked/change-log version when
   available or requested.
4. Update cover letter/editor note, required statements, supplement list, and
   figure/table files as needed.
5. Check that all must-fix items are resolved or explicitly justified.
6. Produce the handoff artifact, named conceptually **Response Package**.

Default handoff artifact: **Response Package** with these sections or metadata:

- Revised manuscript file paths
- Clean/tracked/change-log file paths when available
- Response-to-reviewers letter
- Editor cover letter or resubmission note
- Comment-resolution checklist
- Updated QA Gate Report path
- Journal resubmission checklist and blockers

## Artifact Contracts

Keep contracts lightweight. Use the repo's existing formats when available, but
ensure each artifact carries the fields needed for later sessions to consume it
without re-discovering everything.

- **Literature search record**: research question or scoped topic, databases or
  sources searched, search date, query strings, inclusion/exclusion criteria,
  raw and screened counts, retained candidate sources with stable IDs and
  PMID/DOI/URL metadata, exclusion notes, non-auditable reserve suggestions, and
  unresolved metadata.
- **Literature acquisition queue**: `source_id`, tier or priority, title, PMID,
  DOI, URL, manuscript role, target collection, reference-manager status, PDF
  attachment status, local cache status, and next human action.
- **Literature index**: `citation_key`, title, year, paper role, themes, key
  claims, caveats, reference-manager item key, and markdown-cache status
  (`md` path, conversion method, source PDF checksum).
- **Markdown cache manifest**: per paper — reference-manager item key and
  attachment key, collection, source PDF path, `md` path, source SHA-256,
  conversion method (`markdown` | `plaintext_fallback` | `needs_ocr`), status,
  and char count. PDFs remain in the reference manager and are not committed to
  the repo.
- **Gap synthesis**: evidence matrix, key themes, convergence/divergence map,
  contradiction table, gap taxonomy, positioning claim, CER chains, synthesis
  limitations, SAP/outline implications, and claims requiring PDF verification
  before drafting.
- **Analysis Refresh Report**: commands run or inspected, run label/date,
  relevant input and output paths, cohort/sample definitions, exclusion flow,
  denominators, result artifact inventory, primary/secondary/sensitivity labels,
  statistical interpretation, fallacy and overclaim scan, table/figure
  provenance, Results-ready claims, Discussion-only interpretations,
  supplement-only findings, unresolved blockers, and recommended next actions.
- **SAP/Outline Controller**: target journal or audience if known, manuscript
  structure pattern, central thesis or positioning claim, section outline,
  section purposes, word count allocation, argument map, CER-to-section mapping,
  evidence/result/table/figure map, primary and secondary analyses, sensitivity
  and exploratory labels, supplement placement, transition logic, drafting
  instructions, and unresolved decisions.
- **Manuscript Draft Package**: source inputs used, draft/render path, citation
  workflow used, section word counts, table/figure references, placeholder and
  unresolved-item log, and known limitations before QA.
- **Style-Polished Manuscript Draft Package**: source draft path, polished
  draft/render path, author style sample status, style changes summary,
  preserved facts/citations/numbers/table-figure references check, section word
  count changes, unresolved awkward passages, warnings where polishing risks
  changing meaning, and disclosure or journal-style notes.
- **QA Gate Report**: gate verdict, claim QA, citation QA, claim-source
  alignment checks, data and output QA, draft package and render QA, blockers,
  warnings, and handoff readiness.
- **Pre-Submission Review Report**: journal fit, contribution assessment,
  manuscript strengths, must-fix issues, should-fix issues, optional
  improvements, likely reviewer objections, and recommended next mode.
- **Journal Submission Package**: target journal, article type, final
  manuscript paths, figure/table/supplement paths, cover letter, required
  statements, citation/reference status, journal checklist, blockers, commands
  run, and render status.
- **Revision Roadmap**: decision context, parsed comment inventory, raw comment
  text, reviewer/editor source, severity, priority, target section, suggested
  action, cross-reviewer patterns, new analysis/literature needs, suggested
  revision order, and response-letter skeleton.
- **Revised Manuscript Draft Package**: revised draft/render paths, revision
  log mapped to comment IDs, resolved/unresolved/blocked items,
  response-to-reviewers draft, updated placeholders, source inputs, commands
  used, and recommended next mode.
- **Response Package**: revised manuscript paths, clean/tracked/change-log paths
  when available, response-to-reviewers letter, editor cover letter or
  resubmission note, comment-resolution checklist, updated QA Gate Report path,
  and journal resubmission checklist.
- **Handoff note**: final artifact paths, commands run, outputs changed, known
  limitations, and next human actions.

## Workflow

Use this full sequence for new projects, broad audit requests, or when the user
asks to run the complete literature-to-manuscript workflow.

1. **Discover repo conventions**
   - Read `AGENTS.md`, `README.md`, and project-specific workflow docs first.
   - Identify the reference manager, collection/library identifier, literature index path, gap document, Analysis Refresh Report, SAP/Outline Controller, analysis output directories, and manuscript output directory.
   - Treat repo-specific instructions as authoritative over this generic workflow.

2. **Search for candidate literature when needed**
   - Use `literature-search` before reference-manager import when the project lacks a curated corpus or the user asks for new sources.
   - Keep search strategy, screening decisions, acquisition status, and unresolved metadata separate from the literature index and gap synthesis.
   - Treat retained candidates as provisional until imported or reconciled with the canonical reference manager.

3. **Acquire full text into the reference manager**
   - Use `literature-acquisition` when searched papers need human download through university, institutional, or publisher access.
   - Produce a missing-item and missing-PDF checklist rather than trying to bypass access controls.
   - After the user adds records and PDFs to the target collection, reconcile the collection against the auditable search record before indexing.

4. **Update the literature source and markdown cache**
   - Treat the reference manager (e.g., Zotero) as the canonical store of PDFs and metadata.
   - Do not copy PDFs into the project repo. Instead, build a committed **markdown cache** in the repo by converting the reference manager's PDFs read-only. The PDFs stay in the reference manager; the repo holds only the derived markdown plus a manifest. A repo may override this and keep PDFs only if it explicitly says so.
   - Reading the markdown cache instead of re-parsing PDFs is much cheaper in tokens, which is the point of maintaining it.
   - Locate the reference manager's PDFs read-only. For Zotero: read the data directory from the profile `prefs.js` (`extensions.zotero.dataDir`); copy `zotero.sqlite` before querying to avoid file locks; then map the target collection → items → `itemAttachments` (whose `path` looks like `storage:<file>.pdf`) → `<dataDir>/storage/<attachmentKey>/<file>.pdf`.
   - Convert each PDF to markdown. Default conversion workflow (Python, CPU-only, good for born-digital papers; projects may substitute marker, Docling, or OCR for scans/math-heavy pages):

     ```bash
     pip install pymupdf4llm
     ```
     ```python
     import pymupdf4llm, pymupdf, pathlib
     md = pymupdf4llm.to_markdown(str(pdf_path), show_progress=False)
     if not md.strip():
         # markdown heuristics returned empty: fall back to plain text if a text layer exists
         doc = pymupdf.open(str(pdf_path))
         text = "".join(p.get_text() for p in doc)
         md = text if text.strip() else None   # None => true scan, no text layer: flag needs_ocr, do NOT write an empty file
     if md:
         pathlib.Path(md_path).write_text(md, encoding="utf-8")
     ```
   - Make the cache idempotent: record each source PDF's SHA-256 in the manifest and re-convert only new or changed PDFs; offer a `--force` rebuild.
   - Write a committed manifest linking each `.md` back to its source: reference-manager item key and attachment key, collection, source PDF path, `md` path, source SHA-256, conversion method (`markdown` | `plaintext_fallback` | `needs_ocr`), status, and char count.
   - If an index generator exists, run it after changes to the reference collection, the markdown cache, or curated summary fields.
   - If no generator exists, propose or create a small committed index format before doing large manuscript drafting.

5. **Maintain the literature intelligence layer**
   - Use the literature index for paper lookup and citation key selection.
   - Use the gap synthesis document for integrated evidence interpretation, argument structure, research gap, positioning, and paper roles.
   - Keep gap synthesis focused on themes, contradictions, gap taxonomy, CER chains, and SAP implications; do not turn it into manuscript prose.
   - Keep raw paper inventory in the generated index, not in the gap synthesis.
   - Read the repo markdown cache for paper content during synthesis, indexing, and drafting. Open the canonical PDF in the reference manager only to verify exact thresholds, study design, cohort details, definitions, or wording — especially for entries marked `plaintext_fallback` or `needs_ocr` in the manifest.

6. **Maintain the analysis result layer**
   - Update analysis scripts and outputs through the repo pipeline.
   - Summarize current results in the Analysis Refresh Report.
   - Keep the report focused on project data, run provenance, model results, tables, figures, statistical interpretation, and manuscript handoff.
   - Check that result claims, counts, denominators, and table/figure references match current generated outputs.
   - Do not use the report as the main literature review.

7. **Use the SAP/Outline Controller**
   - Let the SAP/Outline Controller decide manuscript sections, section claims, primary and secondary analyses, table/figure order, and supplement placement.
   - Build the controller from both `gap-synthesis` and the Analysis Refresh Report so it combines what the manuscript should argue with what the data can safely claim.
   - If the Analysis Refresh Report and SAP disagree, flag the conflict and update the controlling document deliberately.
   - Keep exploratory narratives out of the main manuscript unless promoted in the SAP.

8. **Draft the manuscript**
   - Structure from the SAP/Outline Controller.
   - Frame the introduction and discussion from the gap synthesis and literature index.
   - Write results from the Analysis Refresh Report and current generated outputs.
   - Track section word counts, placeholders, citation workflow, and table/figure references in the Manuscript Draft Package.
   - Insert or preserve live citations through the reference manager when available.
   - Save rendered manuscript drafts in the repo’s manuscript output directory.

9. **Polish style when needed**
   - Use `style-polish` after `draft` when the manuscript needs clearer rhythm, author-voice calibration, or removal of generic AI-flavoured prose patterns.
   - Preserve scientific meaning, numbers, citations, table/figure references, and disclosure obligations.
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

13. **Plan revisions after external comments**
   - Use `revision-plan` only after editor, reviewer, or major coauthor comments are received.
   - Parse every comment, preserve reviewer intent, prioritize actions, map comments to manuscript sections, and create a response-letter skeleton.

14. **Revise, polish, and re-QA**
   - Use `revise` to apply the approved Revision Roadmap and produce a Revised Manuscript Draft Package.
   - Use `style-polish` after revision when prose changed substantially or the user requests readability calibration.
   - Return to `qa` after revision or style polishing before any resubmission package.

15. **Prepare response package**
   - Use `response-package` after the revised manuscript passes QA.
   - Assemble revised files, response-to-reviewers letter, editor note, comment-resolution checklist, and resubmission checklist.

16. **Final handoff/archive**
   - Use `handoff` for a concise status/archive note after Journal Submission Package or Response Package creation.
   - Record final artifact paths, commands run, outputs changed, unresolved limitations, and next human actions.

## Recommended Repo Documentation

For each project, keep the reusable workflow here and store project-specific details in the repo:

- `AGENTS.md`: short operational rules for future LLM threads.
- `docs/manuscript_workflow.md`: exact project workflow, paths, collection keys, update commands, and QA checklist.
- `README.md`: concise user-facing pointer to the workflow and literature index.

Project-specific docs should record:

- canonical reference collection name and key,
- that the reference manager holds canonical PDFs while the repo holds only a derived markdown cache (or the repo-specific override if PDFs are kept),
- markdown cache path, manifest path, and PDF→markdown conversion command,
- literature search record and acquisition queue paths,
- literature index paths and regeneration command,
- gap synthesis path,
- Analysis Refresh Report path,
- SAP/Outline Controller path,
- manuscript output path,
- Style-Polished Manuscript Draft Package path when used,
- author style sample paths or note that no samples were used,
- citation/live-reference workflow,
- QA Gate Report path,
- Pre-Submission Review Report path when used,
- Journal Submission Package path,
- Revision Roadmap path when post-review,
- Revised Manuscript Draft Package path when post-review,
- Response Package path when post-review,
- QA checks required before manuscript handoff.
