---
name: research-manuscript-workflow
description: Use for research manuscript projects that need a reproducible workflow from literature search and Zotero literature collection through literature indexing, gap synthesis, planned-analyses roadmaps, analysis reports, a results-reflection research-iteration loop, manuscript outline/SAP, narrative/framing-rehearsal decks, Word or document drafting, style polishing, citation QA, and final manuscript artifact generation. Includes epidemiology, clinical-epidemiology, and population-health manuscript discipline (section discipline, causal-language restraint, internal/AI-workflow language scrub, STROBE-like clarity, methods-citation checks) applied during style polishing and QA. Trigger when the user asks to organize, document, reuse, audit, or execute a literature-to-manuscript workflow across research project repositories, or to revise, polish, humanize, or self-review the user's own epidemiology manuscript for journal-ready prose. Do not use this skill to write or polish peer-review comments on someone else's manuscript.
---

# Research Manuscript Workflow

## Core Principle

Keep the manuscript system in separate artifacts with distinct jobs, so a later
session can resume from the right state without rediscovering the literature,
rerunning analyses, or mixing interpretation, planning and prose:

- **Reference manager** (e.g. Zotero): canonical papers, metadata, PDFs and live citations.
- **Literature search record** and **acquisition queue**: dated, auditable searches and the human download list.
- **Literature index** and **markdown cache**: generated lookup table and derived full text in the repo.
- **Evidence-extraction cache** (optional, large corpora): anchored per-paper numbers.
- **Gap synthesis**: interpretation of the literature and the paper's position.
- **Planned-analyses roadmap**: analyses not yet run, with an availability audit.
- **Analysis Refresh Report**: current results only, with provenance; no framing.
- **Reflection memo**: results argued against the literature and meeting feedback; the living Discussion.
- **SAP/Outline Controller**: the authority for structure, analysis hierarchy and displays.
- **Narrative deck**: framing rehearsal before prose.
- **Draft, QA, review, revision and submission packages**: see the production and revision references.

## Workflow Router

Choose the smallest mode that meets the request. Read the mode's reference
before executing it. If a request spans modes, start at the earliest and state
the sequence; if the stage is unclear, inspect the repo's artifacts first.

| Mode | Use when | Reference |
| --- | --- | --- |
| `setup` | Discover, document or reorganise a project's manuscript workflow | [repository-organisation](references/repository-organisation.md) |
| **Phase 1: literature** | | |
| `literature-search` | Find candidate papers; new dated round after a scope change; acquisition queue for the human | [modes-literature](references/modes-literature.md) |
| `literature-ingest` | Sync the reference-manager collection into the markdown cache, manifest and index | [modes-literature](references/modes-literature.md) |
| `evidence-extraction` | Anchored extraction of key papers (token-heavy; warn first) | [modes-literature](references/modes-literature.md), [contract](references/evidence-extraction-contract.md) |
| `gap-synthesis` | Synthesize the gap and the paper's position | [modes-literature](references/modes-literature.md) |
| **Phase 2: research iteration** | | |
| `analysis-plan` | Triage analyses not yet run, with an availability and power audit | [modes-research-iteration](references/modes-research-iteration.md) |
| `analysis-refresh` | Regenerate and reconcile results into the results report | [modes-research-iteration](references/modes-research-iteration.md) |
| `reflect` | Argue results against literature and meeting feedback; put scope options to the authors | [modes-research-iteration](references/modes-research-iteration.md) |
| `sap-outline` | Build or revise the controlling plan from agreed scope | [modes-research-iteration](references/modes-research-iteration.md) |
| `narrative-deck` | Rehearse the storyline, often for a meeting | [modes-research-iteration](references/modes-research-iteration.md) |
| **Phase 3: production and revision** | | |
| `draft` | Draft prose from the controller | [modes-manuscript-production](references/modes-manuscript-production.md) |
| `style-polish` | Readability and author voice without changing the science | [modes-manuscript-production](references/modes-manuscript-production.md), [epi discipline](references/epidemiology-manuscript-discipline.md) |
| `qa` | Claim, citation, data and render readiness gate | [modes-manuscript-production](references/modes-manuscript-production.md) |
| `pre-submission-review` | Reviewer-style critique before first submission | [modes-manuscript-production](references/modes-manuscript-production.md) |
| `revision-plan` | Turn editor/reviewer/coauthor comments into a roadmap | [modes-revision](references/modes-revision.md) |
| `revise` | Apply an approved roadmap | [modes-revision](references/modes-revision.md) |
| `package` | First submission, resubmission bundle, or final handoff note | [modes-revision](references/modes-revision.md) |

## Shared Rules

- **Repo conventions win.** Read `AGENTS.md`, `README.md` and project workflow
  docs first. Keep an existing repo layout; record the mapping from this skill's
  artifacts to repo paths in the README or `AGENTS.md`.
- **Scope is the authors' call.** Put scope changes (question, population,
  endpoints, primary analyses, discovery components, target journal) to the user
  as options with a recommendation, and change scope-setting documents only
  after they decide.
- **Never invent** citations, numbers, counts, metadata or methods details. Mark
  what is unresolved.
- **Read the markdown cache** for paper content; open the canonical PDF only to
  verify exact numbers, thresholds, definitions or wording.
- **Citation-verification discipline** (in `reflect`, `narrative-deck`, `draft`
  and `qa`): a reference existing is not the same as it supporting the sentence.
  Check that the source supports the specific outcome, subgroup, direction and
  magnitude claimed, not just the topic; catch misattribution across papers and
  drifted numbers; anchor a "well-established" claim to a record in the library
  or flag that one is needed; cite per claim. A claim whose source has
  `claim_basis: abstract` fails until the full text is read.
- **Stop at the mode's output.** Do not run the next mode unless asked.
- Paths beginning `references/` or `scripts/` are relative to the skill root.

## Scope Boundary

This skill serves the author side: producing, polishing, self-reviewing and
revising the user's own manuscript. Reviewing someone else's manuscript belongs
to `write-peer-review`. If the user's role is unclear ("help me review this
manuscript"), ask whether they are an author before starting either.

## Workflow Overview

**Phase 1, literature foundation.** `literature-search` (new dated record after
any material scope change) → the user adds papers to the reference manager →
`literature-ingest` → optionally `evidence-extraction` → `gap-synthesis`.

**Phase 2, research iteration loop.** Cycle `analysis-plan` → `analysis-refresh`
→ `reflect` → `sap-outline`, with `narrative-deck` as an optional branch whose
feedback returns to reflection. Leave the loop only at the **results lock**:

- primary analyses run and stable on the current cohort or extract;
- sensitivity analyses complete and not contradicting the primary result;
- every headline result reconciled with the literature in the reflection memo;
- no run-now items outstanding in the roadmap;
- meeting feedback addressed or logged;
- no unresolved blockers in the results report;
- the user signs off that the results meet publication standard.

**Phase 3, production.** `draft` → `style-polish` when needed → `qa` →
`pre-submission-review` when requested (major issues return to `draft` and
`qa`) → `package`. Proceed past QA only with `PASS`, or `PASS_WITH_WARNINGS`
the user accepts. After external comments: `revision-plan` → `revise` →
`style-polish` if prose changed substantially → `qa` → `package`.

For the recommended repo documentation layout, see
[Recommended Repo Documentation](references/repository-organisation.md#recommended-repo-documentation).
