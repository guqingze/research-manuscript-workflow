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
