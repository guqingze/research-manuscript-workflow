# Research Iteration

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

## Analysis Plan Mode

Use `analysis-plan` inside the research iteration loop when the literature, a
reflection memo, internal-meeting feedback, or a reviewer suggests analyses the
project has not yet run. This mode decides what is worth running next and whether
it is even possible with the project's data; it does not run the analyses or
draft prose.

Core rule: audit availability before proposing. A proposed analysis that the
cohort or linked data cannot support is a limitation to document, not a task to
queue.

Minimum procedure:

1. Collect candidate analyses from the gap synthesis, reflection memo, meeting
   feedback, reviewer comments, and the covariate/measurement literature.
2. For each candidate, run an in-cohort/in-data availability audit: is the
   variable or assay present, at what completeness, in which subcohort, and is it
   a confounder, mediator, or collider relative to the current model? Distinguish
   "computable now from existing columns", "needs new derivation/linkage", and
   "not available in-cohort".
3. Classify each candidate by role (strengthens confounding control, orthogonal
   cross-check, mechanism, robustness/QC, descriptive) and by effort tier
   (straightforward now / intermediate needs generation or linkage / future
   research program).
4. Recommend which candidates to run this cycle, which to defer, and which to
   convert into stated limitations; keep non-auditable or speculative suggestions
   separate from the actionable queue.
5. Hand off: actionable Tier-1 items feed the repo pipeline and `analysis-refresh`;
   deferred and future items seed a Next-Steps/roadmap section for the SAP and
   eventual Discussion.
6. Stop at planning and triage. Do not run analyses or edit the SAP unless the
   user also asked for the next mode.

Default handoff document: **Planned-analyses roadmap** with these sections:

- Candidate analyses with driver/source
- In-cohort/in-data availability audit (completeness, subcohort, confounder/mediator/collider status)
- Role and effort-tier classification
- Run-now / defer / convert-to-limitation recommendation
- Non-auditable or speculative reserve (kept separate)

## Reflection Mode

Use `reflect` inside the research iteration loop after `analysis-refresh`, when
current results need to be argued against the external literature, the gap
synthesis, and internal-meeting feedback. This is the living mid-project
Discussion. It interprets and reconciles; it does not restate the numbers or
draft final prose.

Core rule: reconcile, do not cherry-pick. Interpret contradictions between your
results and the literature rather than explaining them away, and treat each as a
possible driver of a new analysis, a framing change, or a stated limitation.

Minimum procedure:

1. Confirm inputs: Analysis Refresh Report, gap synthesis, literature index (and
   evidence-extraction cache when present), and any internal-meeting notes or
   coauthor feedback.
2. For each headline result, state where it converges with, diverges from, or is
   silent against the indexed literature. For divergence, interpret the likely
   reason (population, definitions, methods, adjustment set, measure-dependence)
   before deciding it is a real contribution.
3. Digest internal-meeting feedback: record decisions, objections, and requested
   analyses relevant to the analysis set or framing; convert each into a tracked
   action (analysis-plan candidate, SAP change, or open question).
4. Every literature or external claim asserted as established must anchor to a
   literature-index/evidence-cache record; verify it supports the specific
   outcome, subgroup, and direction being claimed (see citation-verification
   discipline in [QA Gate Mode](modes-manuscript-production.md#qa-gate-mode)). Flag unresolved claims for PDF verification.
5. Produce drivers for the loop: what to send to `analysis-plan`, what SAP or
   framing changes to make, what to relegate to limitations, and what remains an
   open question for the next meeting or the eventual Discussion.
6. Stop at reflection. Do not run analyses, revise the SAP, or draft prose unless
   the user also asked for the next mode.

Default handoff document: **Reflection memo** with these sections:

- Result-by-result convergence/divergence/silence against the literature
- Interpreted contradictions (with likely reason)
- Internal-meeting feedback digest and resulting actions
- Drivers for analysis-plan and SAP updates
- Open questions and Discussion seeds

## Narrative Deck Mode

Use `narrative-deck` as an any-time branch off reflection, before committing to
manuscript prose, to pressure-test the storyline — commonly to build a slide
outline for an internal meeting and gather feedback. This mode locks framing
decisions and structure; it does not write the manuscript or invent results.

Core rule: the deck is a framing rehearsal, not the paper. Every number and
citation on a slide must trace to the Analysis Refresh Report or a verified
literature record, at the same standard as a draft.

Minimum procedure:

1. Confirm inputs: SAP/Outline Controller, Analysis Refresh Report, gap
   synthesis, reflection memo, and current figures/tables.
   Choose one canonical package for editable deck text and display assets. If
   the project versions selected meeting folders under `outputs/`, use that
   location directly; do not also create an editable deck under docs. Honour the
   requested format, including Markdown with linked assets without a PPTX.
2. Choose and record the spine/storyline and the explicit framing decisions
   (what leads, what is secondary, what is shown vs relegated), including options
   considered and set aside so the group can see the forks.
3. Structure the deck into acts/sections with a one-line takeaway each; add
   presenter notes and mark reviewer-aware caveats to keep visible rather than
   compress.
4. Anchor every on-slide claim: results to the Analysis Refresh Report; external
   claims to verified literature records with the correct outcome/subgroup/
   direction; prefer per-slide footnote-style citations over a single reference
   dump. Apply the citation-verification discipline ([QA Gate Mode](modes-manuscript-production.md#qa-gate-mode)).
5. Collect open framing questions on a dedicated slide for the meeting; route the
   resulting feedback back into `reflect` and `analysis-plan`.
6. Stop at the framing outline. Do not draft the manuscript unless the user also
   asked for `draft`.

Default handoff artifact: **Narrative deck** with these sections:

- Spine/storyline and locked framing decisions (with options set aside)
- Act/section structure with per-slide takeaways and presenter notes
- On-slide claims anchored to results/literature, with per-slide citations
- Open framing questions for the group
- Feedback routed back to reflection/analysis-plan

## Artifact Contracts

- **Planned-analyses roadmap**: candidate analyses with driver/source;
  per-candidate in-cohort/in-data availability audit (completeness, subcohort,
  confounder/mediator/collider status); role and effort-tier classification;
  run-now/defer/convert-to-limitation recommendation; and a separated
  non-auditable/speculative reserve.
- **Reflection memo**: per-result convergence/divergence/silence against the
  indexed literature; interpreted contradictions with likely reason; internal-
  meeting feedback digest and resulting actions; drivers for planned-analyses and
  SAP updates; and open questions and Discussion seeds.
- **Narrative deck**: spine/storyline and locked framing decisions (with options
  considered and set aside); act/section structure with per-slide takeaways and
  presenter notes; on-slide claims anchored to the Analysis Refresh Report or
  verified literature records with per-slide citations; open framing questions for
  the group; and feedback routed back to reflection/analysis-plan.

### Phase 2 — Research iteration loop (cycles until results are publication-ready)

Enter with a Phase-1 gap synthesis and an initial SAP/Outline Controller, then
cycle the following until the exit gate is met. The narrative deck (6d) may
branch off at any reflection point.

6. **Run the research iteration loop**
   - **6a. Plan analyses** (`analysis-plan`): from the gap synthesis, the latest reflection memo, and meeting feedback, choose which not-yet-run analyses to run this cycle; audit in-cohort/in-data availability and confounder/mediator/collider status before queuing; keep the planned-analyses roadmap current.
   - **6b. Implement and refresh results** (`analysis-refresh`): update scripts and outputs through the repo pipeline; summarize current results in the Analysis Refresh Report (project data, provenance, model results, tables/figures, statistical interpretation, handoff); check counts, denominators, and table/figure references match generated outputs. Do not use the report as the literature review.
   - **6c. Reflect** (`reflect`): argue the current results against the gap synthesis, the external literature, and internal-meeting feedback; interpret contradictions rather than explaining them away; produce drivers for the next `analysis-plan` and for SAP/framing changes; keep the reflection memo current. This is the living Discussion.
   - **6d. Rehearse the narrative when useful** (`narrative-deck`, optional branch): build or update the framing-rehearsal deck, often for an internal meeting, and route the feedback back into 6c/6a. Every on-slide number and citation must trace to the Analysis Refresh Report or a verified literature record.
   - **6e. Update the controlling plan** (`sap-outline`): fold accepted results, reflections, and framing decisions into the SAP/Outline Controller; build it from both the gap synthesis and the Analysis Refresh Report; flag and resolve any SAP-vs-results conflict deliberately; keep exploratory narratives out of the main manuscript unless promoted here.
   - **Loop** back to 6a with the updated SAP and roadmap.

Results-lock exit gate: see SKILL.md, Workflow overview.

