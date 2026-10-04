---
name: research-manuscript-workflow
description: Use for research manuscript projects that need a reproducible workflow from literature search and Zotero literature collection through literature indexing, gap synthesis, planned-analyses roadmaps, analysis reports, a results-reflection research-iteration loop, manuscript outline/SAP, narrative/framing-rehearsal decks, Word or document drafting, style polishing, citation QA, and final manuscript artifact generation. Includes epidemiology, clinical-epidemiology, and population-health manuscript discipline (section discipline, causal-language restraint, internal/AI-workflow language scrub, STROBE-like clarity, methods-citation checks) applied during style polishing and QA. Trigger when the user asks to organize, document, reuse, audit, or execute a literature-to-manuscript workflow across research project repositories, or to revise, polish, humanize, or review an epidemiology manuscript for journal-ready prose.
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

| User intent | Mode | Required inputs | Output |
|---|---|---|---|
| Discover, document or reorganise a project manuscript workflow | `setup` | `AGENTS.md`, `README.md`, project docs and caller/artifact inventory | Canonical artifact map, script navigation and project workflow updates; authorised migration with verification |
| **Phase 1 — Literature foundation** | | | |
| Search for candidate literature before Zotero/indexing | `literature-search` | Research question or scoped topic, databases/sources, inclusion/exclusion criteria | Search strategy, screened candidate corpus, and import/next-search recommendations |
| Build the human download checklist for searched candidates and reconcile the collection | `literature-acquisition` | Literature search record, target reference collection name/key | Acquisition queue (DOI/PMID/URL, priority, role) for the human to download into the reference manager, plus missing-item and missing-PDF lists |
| Sync the reference manager into the repo's committed literature layer: membership + citation keys, markdown full-text cache + manifest, and the literature index | `literature-ingest` | Reference manager details, PDF→markdown converter, index generator or index path | Updated markdown cache + manifest, regenerated literature index, reconciled citation keys, plus mismatch or missing-PDF notes |
| Extract structured evidence from identified key papers into a verifiable cache | `evidence-extraction` | Literature index, markdown cache, identified key-paper set | Evidence-extraction cache of anchored per-paper records (token-costly subagent fan-out; human-in-the-loop key-paper selection; feeds gap-synthesis) |
| Synthesize or revise the research gap and paper positioning | `gap-synthesis` | Literature index and markdown cache (or an evidence-extraction cache from `evidence-extraction` for key-paper grounding); reference-manager PDFs only to verify | Integrated evidence synthesis, manuscript positioning, CER chains, and SAP implications |
| **Phase 2 — Research iteration loop** | | | |
| Refresh project results for manuscript use | `analysis-refresh` | Repo pipeline commands, current outputs, Analysis Refresh Report path | Analysis Refresh Report with run provenance, result validation, interpretation, and manuscript handoff |
| Plan literature/reviewer-motivated analyses not yet run | `analysis-plan` | Gap synthesis, reflection memo, literature index, repo data/availability | Planned-analyses roadmap with in-cohort availability audit and effort tiers |
| Reflect on current results against literature, gaps, and meeting feedback | `reflect` | Analysis Refresh Report, gap synthesis, literature index, internal-meeting notes | Reflection memo: results-vs-literature reconciliation, contradictions, and drivers for planned-analyses/SAP updates |
| Build or revise the controlling manuscript plan | `sap-outline` | Gap synthesis, Analysis Refresh Report, reflection memo, current tables/figures | SAP/Outline Controller with section structure, argument map, evidence/result map, and main-vs-supplement decisions |
| Rehearse and lock the narrative/framing before drafting (often for an internal meeting) | `narrative-deck` | SAP/Outline Controller, Analysis Refresh Report, gap synthesis, reflection memo | Narrative deck: spine, framing decisions, act structure, presenter notes, open questions |
| **Phase 3 — Manuscript production** | | | |
| Draft or revise manuscript prose | `draft` | SAP/Outline Controller, gap synthesis, Analysis Refresh Report, literature index | Manuscript Draft Package in the repo's manuscript output directory |
| Polish manuscript readability and author voice | `style-polish` | Manuscript Draft Package or Revised Manuscript Draft Package, author writing samples if available | Style-Polished Manuscript Draft Package with style changes summary and preserved-content check |
| Audit manuscript readiness | `qa` | Manuscript Draft Package, Style-Polished Manuscript Draft Package, or Revised Manuscript Draft Package, reference collection/index, generated outputs | QA Gate Report with claim, citation, data/output, draft-package, and render readiness checks |
| Critique manuscript before first submission | `pre-submission-review` | QA-passed Manuscript Draft Package or Style-Polished Manuscript Draft Package, SAP/Outline Controller, target journal if known | Pre-Submission Review Report with merit critique and recommended fixes |
| Prepare first-submission journal files | `journal-package` | QA-passed Manuscript Draft Package or Style-Polished Manuscript Draft Package, target journal requirements, render workflow | Journal Submission Package with formatted files, statements, cover letter, and checklist |
| **Phase 3 — Post-review revision cycle** | | | |
| Parse editor/reviewer/coauthor comments | `revision-plan` | Reviewer/editor comments, submitted manuscript package, decision letter if available | Revision Roadmap with prioritized comments and response-letter skeleton |
| Apply an approved revision plan | `revise` | Revision Roadmap, submitted or current Manuscript Draft Package or Style-Polished Manuscript Draft Package, source materials | Revised Manuscript Draft Package with revision log and response draft |
| Prepare resubmission files | `response-package` | Revised draft, Revision Roadmap, QA Gate Report, target journal requirements | Response Package with revised files, response letter, and resubmission checklist |
| Produce final handoff/archive note | `handoff` | Journal Submission Package or Response Package, QA Gate Report, render workflow | Concise handoff/archive note with final paths, commands, limitations, and next actions |

If the request spans multiple modes, start at the earliest affected mode and
state the planned sequence. If the user's current stage is ambiguous, inspect the
repo workflow docs and existing manuscript artifacts before asking for
clarification.

## Load the selected procedure

Read only the reference for the selected mode before executing it. Resolve all
resource paths relative to this skill's directory, not the research project's
working directory. Each mode reference keeps the original procedure and output
requirements. Read another mode only when the requested work crosses that boundary.

| Selected mode | Procedure |
|---|---|
| `setup` | [Setup and Repository Organisation Mode](references/setup.md) |
| `literature-search` | [Literature Search Mode](references/literature-search.md) |
| `literature-acquisition` | [Literature Acquisition Mode](references/literature-acquisition.md) |
| `gap-synthesis` | [Gap Synthesis Mode](references/gap-synthesis.md) |
| `analysis-refresh` | [Analysis Refresh Mode](references/analysis-refresh.md) |
| `sap-outline` | [SAP/Outline Mode](references/sap-outline.md) |
| `analysis-plan` | [Analysis Plan Mode](references/analysis-plan.md) |
| `reflect` | [Reflection Mode](references/reflect.md) |
| `narrative-deck` | [Narrative Deck Mode](references/narrative-deck.md) |
| `draft` | [Draft Mode](references/draft.md) |
| `style-polish` | [Style Polish Mode](references/style-polish.md) |
| `qa` | [QA Gate Mode](references/qa.md) |
| `pre-submission-review` | [Pre-Submission Review Mode](references/pre-submission-review.md) |
| `journal-package` | [Journal Package Mode](references/journal-package.md) |
| `revision-plan` | [Revision Plan Mode](references/revision-plan.md) |
| `revise` | [Revise Mode](references/revise.md) |
| `response-package` | [Response Package Mode](references/response-package.md) |
| `evidence-extraction` | [Gap synthesis and key-paper extraction](references/gap-synthesis.md), then [extraction contract](references/evidence-extraction-contract.md) |
| `literature-ingest` | [Workflow composition](references/workflow-composition.md), literature-ingest step |
| `handoff` | [Workflow composition](references/workflow-composition.md), final handoff step |

For a new project, a broad audit, or a multi-phase request, read
[workflow composition](references/workflow-composition.md). For planning or
checking artifact fields, read [artifact contracts](references/artifact-contracts.md).
For project-specific workflow documentation, read
[project documentation](references/project-documentation.md).

For setup or structural migration, also read
[repository organisation](references/repository-organisation.md).
During epidemiology style polishing or QA, also read
[epidemiology manuscript discipline](references/epidemiology-manuscript-discipline.md).
The [evidence-extraction contract](references/evidence-extraction-contract.md)
defines extraction fields and anchor rules; `scripts/verify_extract_anchors.py`
checks those anchors mechanically.

## Keep the skill boundary clear

Use this skill for the author's research-to-manuscript workflow, including
pre-submission critique and responding to received reviews. Use the separate
`write-peer-review` skill for reviewer-authored comments on other authors'
manuscripts and journal review forms. Keep scientific meaning and evidence
intact in either workflow. Do not require the other skill to run this one.
