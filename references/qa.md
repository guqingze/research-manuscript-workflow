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
     apply `epidemiology-manuscript-discipline.md`: verify Results
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
