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
