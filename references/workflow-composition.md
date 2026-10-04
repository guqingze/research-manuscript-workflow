## Workflow

Contents: Phase 1 — Literature foundation (mostly linear, re-enterable); Phase 2 — Research iteration loop (cycles until results are publication-ready); Phase 3 — Manuscript production (mostly linear).

Use this sequence for new projects, broad audit requests, or a full
literature-to-manuscript run. It has **three macro-phases**: a mostly linear
**Phase 1 — Literature foundation**; an iterative **Phase 2 — Research iteration
loop** that cycles until results are publication-ready; and a mostly linear
**Phase 3 — Manuscript production**. Modes remain individually addressable; the
phases only describe how they compose. The narrative deck is an any-time branch
off Phase 2, not a fixed step.

**Preamble (before any phase)**

1. **Discover repo conventions**
   - Read `AGENTS.md`, `README.md`, and project-specific workflow docs first.
   - Identify the reference manager, collection/library identifier, literature index path, gap document, Analysis Refresh Report, SAP/Outline Controller, analysis output directories, and manuscript output directory.
   - Treat repo-specific instructions as authoritative over this generic workflow.

### Phase 1 — Literature foundation (mostly linear, re-enterable)

2. **Search for candidate literature when needed**
   - Use `literature-search` before reference-manager import when the project lacks a curated corpus or the user asks for new sources.
   - Re-enter it for any material manuscript-scope change, including a new comparison population or global-comparison section; open a new dated search record rather than silently extending an earlier search.
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

7. **Exit gate — "results lock"** (leave Phase 2 only when all hold)
   - primary analyses are run and stable on the current cohort/extract;
   - sensitivity analyses are complete and do not contradict the primary result;
   - the reflection memo reconciles each headline result with the literature, with no unresolved contradiction;
   - no Tier-1 (run-now) items remain outstanding in the planned-analyses roadmap;
   - internal-meeting feedback is addressed or explicitly logged;
   - the Analysis Refresh Report lists no unresolved blockers;
   - human sign-off that the results meet publication standard.

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
