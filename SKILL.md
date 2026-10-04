---
name: research-manuscript-workflow
description: Use for research manuscript projects that need a reproducible workflow from literature search and Zotero literature collection through literature indexing, gap synthesis, planned-analyses roadmaps, analysis reports, a results-reflection research-iteration loop, manuscript outline/SAP, narrative/framing-rehearsal decks, Word or document drafting, style polishing, citation QA, and final manuscript artifact generation. Includes epidemiology, clinical-epidemiology, and population-health manuscript discipline (section discipline, causal-language restraint, internal/AI-workflow language scrub, STROBE-like clarity, methods-citation checks) applied during style polishing and QA. Trigger when the user asks to organize, document, reuse, audit, or execute a literature-to-manuscript workflow across research project repositories, or to revise, polish, humanize, or self-review the user's own epidemiology manuscript for journal-ready prose. Do not use this skill to write or polish peer-review comments on someone else's manuscript.
---

# Research Manuscript Workflow

## Core Principle

Separate the manuscript system into artifacts with distinct jobs. Do not let literature synthesis, analysis results, manuscript specification, and final prose collapse into one document.

Use this default artifact model unless the repo already has stronger conventions:

- **Reference manager**: canonical library for paper membership, metadata, attachments, and live citations.
- **Literature search record**: reproducible search strategy, screening decisions, and candidate source corpus before or alongside reference-manager import.
- **Literature acquisition queue**: human-in-the-loop full-text collection checklist that bridges searched candidates to a project reference-manager collection.
- **Literature index**: generated LLM-facing lookup table with citation keys, themes, roles, key claims, caveats, and local attachment status.
- **Evidence-extraction cache**: generated, committed, per-paper structured extraction (one record per cached full text) produced by fan-out worker subagents from the markdown cache; carries study characterization, anchored quantitative findings, and relevance tags so that gap synthesis, drafting, and QA read verified numbers without re-reading full text. Optional layer used when the corpus is large; sits between the literature index and gap synthesis.
- **Gap synthesis**: curated interpretation of the literature and the research gap.
- **Planned-analyses roadmap**: literature- and reviewer-motivated analyses not yet run, with an in-cohort/data availability audit and effort tiers; a cross-cutting artifact that feeds both gap synthesis and the Analysis Refresh Report during the research iteration loop.
- **Analysis Refresh Report**: current project results only, generated or updated from scripts and outputs, with provenance, interpretation, and manuscript handoff.
- **Reflection memo**: living mid-project discussion — current results argued against the gap synthesis, the external literature, and internal-meeting feedback — that identifies contradictions, drives planned-analyses and SAP updates, and eventually seeds the manuscript Discussion. Distinct from gap synthesis (which interprets external literature only) and from the Analysis Refresh Report (which carries results without framing).
- **SAP/Outline Controller**: controlling manuscript structure, analysis hierarchy, section claims, word counts, tables, figures, and main-vs-supplement decisions.
- **Narrative deck**: a framing-rehearsal slide outline built before drafting prose — storyline/spine, locked framing decisions, act/section structure, presenter notes, and open questions — used to pressure-test the narrative (often at an internal meeting) and gather feedback that re-enters the research iteration loop. An any-time branch off reflection, not a fixed linear stage.
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
workflow when the user asks for one layer only. Modes are grouped by the three
macro-phases (see Workflow); `setup` is a cross-phase preamble.

After selecting a mode, read its corresponding reference before executing any step; do not execute from the router summary alone.

| User intent | Mode | Required inputs | Output | Must read before execution |
| --- | --- | --- | --- | --- |
| Discover, document or reorganise a project manuscript workflow | `setup` | `AGENTS.md`, `README.md`, project docs and caller/artifact inventory | Canonical artifact map, script navigation and project workflow updates; authorised migration with verification | [references/repository-organisation.md](references/repository-organisation.md) |
| **Phase 1 — Literature foundation** |  |  |  | Group heading; not executable |
| Search for candidate literature before Zotero/indexing | `literature-search` | Research question or scoped topic, databases/sources, inclusion/exclusion criteria | Search strategy, screened candidate corpus, and import/next-search recommendations | [references/modes-literature.md](references/modes-literature.md) |
| Build the human download checklist for searched candidates and reconcile the collection | `literature-acquisition` | Literature search record, target reference collection name/key | Acquisition queue (DOI/PMID/URL, priority, role) for the human to download into the reference manager, plus missing-item and missing-PDF lists | [references/modes-literature.md](references/modes-literature.md) |
| Sync the reference manager into the repo's committed literature layer: membership + citation keys, markdown full-text cache + manifest, and the literature index | `literature-ingest` | Reference manager details, PDF→markdown converter, index generator or index path | Updated markdown cache + manifest, regenerated literature index, reconciled citation keys, plus mismatch or missing-PDF notes | [references/modes-literature.md](references/modes-literature.md) |
| Extract structured evidence from identified key papers into a verifiable cache | `evidence-extraction` | Literature index, markdown cache, identified key-paper set | Evidence-extraction cache of anchored per-paper records (token-costly subagent fan-out; human-in-the-loop key-paper selection; feeds gap-synthesis) | [references/modes-literature.md](references/modes-literature.md) |
| Synthesize or revise the research gap and paper positioning | `gap-synthesis` | Literature index and markdown cache (or an evidence-extraction cache from `evidence-extraction` for key-paper grounding); reference-manager PDFs only to verify | Integrated evidence synthesis, manuscript positioning, CER chains, and SAP implications | [references/modes-literature.md](references/modes-literature.md) |
| **Phase 2 — Research iteration loop** |  |  |  | Group heading; not executable |
| Refresh project results for manuscript use | `analysis-refresh` | Repo pipeline commands, current outputs, Analysis Refresh Report path | Analysis Refresh Report with run provenance, result validation, interpretation, and manuscript handoff | [references/modes-research-iteration.md](references/modes-research-iteration.md) |
| Plan literature/reviewer-motivated analyses not yet run | `analysis-plan` | Gap synthesis, reflection memo, literature index, repo data/availability | Planned-analyses roadmap with in-cohort availability audit and effort tiers | [references/modes-research-iteration.md](references/modes-research-iteration.md) |
| Reflect on current results against literature, gaps, and meeting feedback | `reflect` | Analysis Refresh Report, gap synthesis, literature index, internal-meeting notes | Reflection memo: results-vs-literature reconciliation, contradictions, and drivers for planned-analyses/SAP updates | [references/modes-research-iteration.md](references/modes-research-iteration.md); [references/modes-manuscript-production.md](references/modes-manuscript-production.md#qa-gate-mode) — read only QA Gate Mode, Minimum procedure step 4 (citation-verification discipline) |
| Build or revise the controlling manuscript plan | `sap-outline` | Gap synthesis, Analysis Refresh Report, reflection memo, current tables/figures | SAP/Outline Controller with section structure, argument map, evidence/result map, and main-vs-supplement decisions | [references/modes-research-iteration.md](references/modes-research-iteration.md) |
| Rehearse and lock the narrative/framing before drafting (often for an internal meeting) | `narrative-deck` | SAP/Outline Controller, Analysis Refresh Report, gap synthesis, reflection memo | Narrative deck: spine, framing decisions, act structure, presenter notes, open questions | [references/modes-research-iteration.md](references/modes-research-iteration.md); [references/modes-manuscript-production.md](references/modes-manuscript-production.md#qa-gate-mode) — read only QA Gate Mode, Minimum procedure step 4 (citation-verification discipline) |
| **Phase 3 — Manuscript production** |  |  |  | Group heading; not executable |
| Draft or revise manuscript prose | `draft` | SAP/Outline Controller, gap synthesis, Analysis Refresh Report, literature index | Manuscript Draft Package in the repo's manuscript output directory | [references/modes-manuscript-production.md](references/modes-manuscript-production.md) |
| Polish manuscript readability and author voice | `style-polish` | Manuscript Draft Package or Revised Manuscript Draft Package, author writing samples if available | Style-Polished Manuscript Draft Package with style changes summary and preserved-content check | [references/modes-manuscript-production.md](references/modes-manuscript-production.md) |
| Audit manuscript readiness | `qa` | Manuscript Draft Package, Style-Polished Manuscript Draft Package, or Revised Manuscript Draft Package, reference collection/index, generated outputs | QA Gate Report with claim, citation, data/output, draft-package, and render readiness checks | [references/modes-manuscript-production.md](references/modes-manuscript-production.md) |
| Critique manuscript before first submission | `pre-submission-review` | QA-passed Manuscript Draft Package or Style-Polished Manuscript Draft Package, SAP/Outline Controller, target journal if known | Pre-Submission Review Report with merit critique and recommended fixes | [references/modes-manuscript-production.md](references/modes-manuscript-production.md) |
| Prepare first-submission journal files | `journal-package` | QA-passed Manuscript Draft Package or Style-Polished Manuscript Draft Package, target journal requirements, render workflow | Journal Submission Package with formatted files, statements, cover letter, and checklist | [references/modes-manuscript-production.md](references/modes-manuscript-production.md) |
| **Phase 3 — Post-review revision cycle** |  |  |  | Group heading; not executable |
| Parse editor/reviewer/coauthor comments | `revision-plan` | Reviewer/editor comments, submitted manuscript package, decision letter if available | Revision Roadmap with prioritized comments and response-letter skeleton | [references/modes-revision.md](references/modes-revision.md) |
| Apply an approved revision plan | `revise` | Revision Roadmap, submitted or current Manuscript Draft Package or Style-Polished Manuscript Draft Package, source materials | Revised Manuscript Draft Package with revision log and response draft | [references/modes-revision.md](references/modes-revision.md) |
| Prepare resubmission files | `response-package` | Revised draft, Revision Roadmap, QA Gate Report, target journal requirements | Response Package with revised files, response letter, and resubmission checklist | [references/modes-revision.md](references/modes-revision.md) |
| Produce final handoff/archive note | `handoff` | Journal Submission Package or Response Package, QA Gate Report, render workflow | Concise handoff/archive note with final paths, commands, limitations, and next actions | [references/modes-revision.md](references/modes-revision.md) — read the handoff section after first-submission packaging as well as after revision |

If the request spans multiple modes, start at the earliest affected mode and
state the planned sequence. If the user's current stage is ambiguous, inspect the
repo workflow docs and existing manuscript artifacts before asking for
clarification.

## Scope boundary

Route by whether the user is an author of the manuscript, not by whether the
request contains the word "review".

- `research-manuscript-workflow` serves the author side: producing, revising,
  and polishing the user's own manuscript (`draft`, `style-polish`); checking it
  from the author's perspective before submission (`pre-submission-review`);
  and planning changes, revising the manuscript, and preparing responses to
  received reviews (`revision-plan`, `revise`, `response-package`).
- `write-peer-review` serves the reviewer side: reviewing someone else's
  manuscript and writing or polishing author-facing peer-review comments,
  confidential editor feedback, and structured journal review-form responses.
  Use that skill for those tasks, rather than this manuscript workflow.
- If the user's role is unclear, as in "help me review this manuscript", first
  ask whether the user is an author of the manuscript. Do not guess from the
  word "review" or start either workflow until the role is clarified. Once the
  author/reviewer role is established, select the mode that fits the task and
  available inputs; apply the existing mode prerequisites.

## Setup and Repository Organisation Mode

For discovery or structural refactoring, read
[repository organisation](references/repository-organisation.md). Establish each
artifact's canonical editable home, distinguish generated exports and historical
evidence, and inventory script callers before moving files. If the user has
approved a deck or research plan, save it before structural work.

Adapt to the repository rather than creating every folder in the example layout.
One artifact can carry several lightweight metadata fields without needing a
new framework. A request to organise files does not authorise changing scientific
definitions, rewriting manuscript claims, rerunning model selection or publishing.

## Reference paths

Inline code paths beginning with `references/` or `scripts/` are relative to the skill root, including inside references; Markdown links are relative to the containing file. Read any additional references required by the selected mode.

## Artifact Contracts

Keep contracts lightweight. Use the repo's existing formats when available, but
ensure each artifact carries the fields needed for later sessions to consume it
without re-discovering everything.

- **Literature index**: `citation_key`, title, year, paper role, themes, key
  claims, caveats, reference-manager item key, and markdown-cache status
  (`md` path, conversion method, source PDF checksum).
- **Evidence-extraction cache**: per paper — `citation_key`, source `md` path and
  SHA-256 (mirrored from the markdown-cache manifest), `schema_version`, study
  characterization (design, setting, population, N, modality, cutoffs), an
  evidence grade, a list of anchored quantitative findings (each: claim, value,
  CI/p, adjustment set, and a `quote`/`section`/`table` anchor), relevance tags
  (manuscript role, which claim it bears on, convergence/divergence note, caveat),
  and `verification_status`. Full field-level schema, anchor rules, and the worker
  prompt template live in `references/evidence-extraction-contract.md`; a mirrored
  SHA-keyed extraction-cache manifest makes rebuilds idempotent. Anchors are
  verified by `scripts/verify_extract_anchors.py`.
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
- **Journal Submission Package**: target journal, article type, final
  manuscript paths, figure/table/supplement paths, cover letter, required
  statements, citation/reference status, journal checklist, blockers, commands
  run, and render status.
- **Revised Manuscript Draft Package**: revised draft/render paths, revision
  log mapped to comment IDs, resolved/unresolved/blocked items,
  response-to-reviewers draft, updated placeholders, source inputs, commands
  used, and recommended next mode.
## Workflow overview

Full steps are in the corresponding references; any inconsistency between this overview and a reference is governed by the reference and must be treated as an error to repair.

Use this sequence for new projects, broad audits, or a full literature-to-manuscript run; individual modes remain independently usable.

**Preamble (before any phase)**

1. **Discover repo conventions**
   - Read `AGENTS.md`, `README.md`, and project-specific workflow docs first.
   - Identify the reference manager, collection/library identifier, literature index path, gap document, Analysis Refresh Report, SAP/Outline Controller, analysis output directories, and manuscript output directory.
   - Treat repo-specific instructions as authoritative over this generic workflow.

### Phase 1 — Literature foundation

When the project lacks a curated corpus or new sources are requested, begin with literature-search before reference-manager import; re-enter it after a material manuscript-scope change, using a new dated search record.

When searched papers require human full-text acquisition, use literature-acquisition and reconcile the added records and PDFs against the auditable search record before indexing.

Proceed through literature-ingest to maintain the markdown cache, manifest, and index, then gap-synthesis to interpret the literature and establish positioning and SAP implications.

   - Read the repo markdown cache for paper content during synthesis, indexing, and drafting. Open the canonical PDF in the reference manager only to verify exact thresholds, study design, cohort details, definitions, or wording — especially for entries marked `plaintext_fallback` or `needs_ocr` in the manifest.

### Phase 2 — Research iteration loop

Enter with a Phase-1 gap synthesis and an initial SAP/Outline Controller.

Cycle through analysis-plan, analysis-refresh, reflect, and sap-outline, returning to analysis-plan with the updated SAP and roadmap until the results-lock gate is met.

Narrative-deck is an optional branch at any reflection point, with feedback returning to reflection and analysis planning.

**Exit gate — "results lock"** (leave Phase 2 only when all hold)
   - primary analyses are run and stable on the current cohort/extract;
   - sensitivity analyses are complete and do not contradict the primary result;
   - the reflection memo reconciles each headline result with the literature, with no unresolved contradiction;
   - no Tier-1 (run-now) items remain outstanding in the planned-analyses roadmap;
   - internal-meeting feedback is addressed or explicitly logged;
   - the Analysis Refresh Report lists no unresolved blockers;
   - human sign-off that the results meet publication standard.

### Phase 3 — Manuscript production

Draft from the SAP/Outline Controller, gap synthesis, literature index, Analysis Refresh Report, and current outputs; apply style-polish when needed, returning to draft before QA if polishing exposes content uncertainty.

During style-polish, preserve scientific meaning, numbers, citations, table/figure references, and disclosure obligations.

Run QA on the latest draft package and re-render after final edits when render tooling exists; proceed to pre-submission-review or journal-package only with PASS, or PASS_WITH_WARNINGS explicitly accepted by the user.

When pre-submission-review is requested, return to draft and then qa for major issues; proceed to journal-package when only minor issues or accepted warnings remain.

Keep content changes out of journal packaging, route content blockers back to draft or qa, and perform external submission outside this workflow.

### Post-review revision cycle and handoff

Enter revision-plan only after editor, reviewer, or major coauthor comments are received, preserving reviewer intent and mapping every comment to an action and response skeleton.

Use revise to apply the approved Revision Roadmap; apply style-polish when prose changed substantially or readability calibration is requested, then return to qa before any resubmission package.

Use response-package after the revised manuscript passes QA to assemble revised files, responses, the editor note, and resolution and resubmission checklists.

Use handoff after either a Journal Submission Package or a Response Package is created, recording final paths, commands, changed outputs, unresolved limitations, and next human actions.

## Repository documentation

For the recommended project documentation layout, read [Recommended Repo Documentation](references/repository-organisation.md#recommended-repo-documentation).
