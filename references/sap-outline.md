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
