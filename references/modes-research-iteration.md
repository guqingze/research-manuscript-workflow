# Research Iteration

The loop: `analysis-plan` → `analysis-refresh` → `reflect` → `sap-outline` →
back to `analysis-plan`, with `narrative-deck` as an optional branch off
reflection. Leave the loop only at the results-lock gate in SKILL.md.

## Analysis Plan Mode

Use `analysis-plan` when the literature, a reflection memo, a meeting or a
reviewer suggests analyses not yet run. It decides what is worth running and
whether the data can support it; it does not run anything.

Core rule: audit availability before proposing. An analysis the data cannot
support is a limitation to state, not a task to queue.

Procedure:

1. Collect candidates with their source (gap synthesis, reflection, meeting,
   reviewer).
2. Audit each in the data: is the variable or assay present, at what
   completeness, in which subcohort; is it a confounder, mediator or collider
   for the current model; is it computable now, does it need new derivation or
   linkage, or is it unavailable? For outcome analyses, add the event count and
   a rough power or minimum-detectable-effect check for the key contrast.
3. Classify by role (confounding control, cross-check, mechanism, robustness,
   descriptive) and effort (now, needs derivation/linkage, future programme).
4. Recommend run now, defer, or convert to limitation. Keep speculative ideas in
   a separate reserve. Stop at the roadmap.

## Analysis Refresh Mode

Use `analysis-refresh` when results need to be regenerated, reconciled or
prepared for planning. It uses the repo's pipeline and outputs; it does not
invent analyses outside the scripts or the SAP.

Core rule: produce a results handoff that later modes can trust, not a prose
summary. No framing; that belongs in reflection.

Procedure:

1. Record provenance: commands, run label/date, scripts, inputs, outputs, git
   state.
2. Check counts, exclusion flow, denominators, missingness, definitions and
   follow-up, and that numbers agree across tables and QC outputs.
3. Inventory results and label each primary, secondary, sensitivity,
   exploratory, supplement-only or not-for-manuscript, as the SAP says.
4. Interpret conservatively (estimate, uncertainty, magnitude, adjustment set,
   diagnostics), then scan for overclaims: causal wording beyond the design,
   uncorrected multiplicity, subgroup or ancestry generalization, selection or
   collider bias, imprecise estimates framed as definitive.
5. Separate Results-ready claims, Discussion-only interpretations,
   supplement-only findings and blockers. Stop at the report.

## Reflection Mode

Use `reflect` after a results refresh, to argue the results against the
literature, the gap synthesis and meeting feedback. It is the living
mid-project Discussion.

Core rule: reconcile, do not cherry-pick. Each contradiction becomes a new
analysis, a framing change or a stated limitation.

Procedure:

1. For each headline result, state where it converges with, diverges from or is
   silent against the indexed literature, and interpret divergence (population,
   definitions, methods, adjustment) before calling it a contribution.
2. Anchor every external claim to an index or extraction-cache record and apply
   the citation-verification discipline (SKILL.md).
3. Digest meeting feedback into tracked actions (analysis-plan candidate, SAP
   change, open question). If what a remark refers to is unclear, quote it and
   mark it unresolved; ask rather than infer.
4. Scope is the authors' call. When reflection suggests a change to the
   question, population, endpoints, primary analyses or discovery components,
   put two to four options in the memo, each with a feasibility check (event
   counts, rough power), and a recommendation; then stop. Record the user's
   decision and date in the memo.
5. List drivers for `analysis-plan` and the SAP, limitations, and open
   questions. Stop at the memo.

## SAP/Outline Mode

Use `sap-outline` to build or revise the controlling manuscript plan from the
gap synthesis, the results report and the reflection memo. It decides what goes
where and with what evidence; it does not draft prose.

Core rule: structure serves the argument and the available results. Scope comes
from the authors.

Procedure:

1. Build or change scope only from scope the user has agreed (recorded in a
   reflection memo or their own message), including for the first controller.
   Do not edit the SAP, outline or one-pager ahead of that agreement.
2. Confirm the structure (IMRaD by default for empirical work, unless the repo
   or journal says otherwise) and the central thesis, decomposed into three to
   five section-level arguments.
3. Map CER chains, results and displays to sections, and label each analysis
   primary, secondary, sensitivity, exploratory or supplement-only.
4. For each section, record purpose, word target, core claim, evidence,
   tables/figures, citation groups and the transition.
5. Check: no Results claim exceeds the results report; no Introduction or
   Discussion claim exceeds the gap synthesis; open decisions are listed, not
   silently filled. Stop at the plan.

## Narrative Deck Mode

Use `narrative-deck` at any reflection point to pressure-test the storyline,
often for an internal meeting, before committing to prose.

Core rule: a framing rehearsal, not the paper. Every number and citation on a
slide meets the same standard as a draft.

Procedure:

1. Use one canonical package for the editable deck text and display assets (see
   repository organisation); honour the requested format, including Markdown
   without a PPTX.
2. Record the spine and the framing decisions, including the options set aside
   so the group can see the forks.
3. Give each act or section a one-line takeaway and presenter notes; keep
   reviewer-relevant caveats visible.
4. Anchor results to the results report and external claims to verified
   records, with per-slide citations.
5. End with a slide of open framing questions; route the feedback into
   `reflect` and `analysis-plan`. Stop at the deck.

## Artifact Contracts

- **Planned-analyses roadmap**: candidates with source; availability audit
  (completeness, subcohort, confounder/mediator/collider status, event counts
  and power where relevant); role and effort; run/defer/limitation
  recommendation; separate speculative reserve.
- **Analysis Refresh Report**: provenance; cohort and data checks; result
  inventory with labels; statistical interpretation; overclaim scan;
  Results-ready, Discussion-only and supplement-only claims; blockers and next
  actions.
- **Reflection memo**: per-result convergence/divergence/silence; interpreted
  contradictions; meeting feedback digest with actions and unresolved remarks;
  scope options and recorded decisions; drivers for analysis-plan and the SAP;
  open questions and Discussion seeds.
- **SAP/Outline Controller**: target journal and structure; thesis; section
  plan with purposes, word targets, claims, evidence and displays; argument and
  CER-to-section map; primary/secondary/sensitivity and main/supplement
  decisions; transitions; drafting instructions; open decisions.
- **Narrative deck**: spine and framing decisions with options set aside; acts
  with takeaways and presenter notes; anchored on-slide claims with citations;
  open questions; feedback routing.
