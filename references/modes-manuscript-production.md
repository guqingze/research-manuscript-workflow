# Manuscript Production

## Draft Mode

Use `draft` once a SAP/Outline Controller exists, or for a partial section the
user asks for from the available controlling materials.

Core rule: follow the controller; do not rediscover the argument. If it
conflicts with the gap synthesis or results report, flag the conflict before
drafting the affected claim.

Procedure:

1. Draft by section from the controller's purposes, claims, citations, results,
   displays, word targets and transitions. Introduction from the gap synthesis;
   Methods from the SAP and definitions; Results from the results report only,
   without interpretation; Discussion from both, separating evidence, inference,
   limitations and implications.
2. Never invent citations, numbers, table references or methods details; log
   placeholders and unresolved items instead. Use the live-citation workflow
   when available.
3. Before handoff, check that every major claim has a citation or output
   source, displays exist, and word counts are recorded against the controller.
   Save rendered drafts in the repo's manuscript output directory. Hand off to
   `style-polish` or `qa`.

## Style Polish Mode

Use `style-polish` after `draft` or `revise` for readability and author voice.

Core rule: improve prose without changing the science. Polish for clarity, not
to evade AI detection or hide AI assistance; keep any required disclosure.

Procedure:

1. Lock numbers, estimates, intervals, definitions, citation keys, display
   references and section claims unless the user asks for scientific revision.
2. Calibrate to author samples when available; discipline and journal
   conventions override personal style.
3. Cut filler, throat-clearing, inflated novelty and template-like rhythm; keep
   academic register and precise Methods prose. For epidemiology,
   clinical-epidemiology or population-health papers, apply
   `references/epidemiology-manuscript-discipline.md` and the project's revision
   lessons file if one exists.
4. If a smoother sentence loses its tie to a source, or polishing would change
   meaning, drop a caveat or weaken a limitation, leave the passage and list it.
   If polishing exposes content uncertainty, return to `draft`; otherwise hand
   off to `qa`.

## QA Gate Mode

Use `qa` on the latest draft, polished draft or revised draft. It checks
factual readiness, not merit.

Core rule: every claim, number and citation traces to its source.

Procedure:

1. Claim QA: classify major claims as literature-backed, analysis-backed, mixed
   or unsupported; analysis claims must match the results report and current
   outputs; flag causal overreach, inflated novelty, and Discussion claims
   stronger than the evidence. For epidemiology manuscripts, apply the
   epidemiology discipline (no interpretation in Results, design-matched causal
   wording, no internal language, references numbered by first appearance).
2. Citation QA: in-text citations map to the reference collection; no orphans;
   metadata complete; apply the citation-verification discipline (SKILL.md) to
   important claims.
3. Data QA: numbers, denominators, model labels, intervals and p-values match
   outputs; displays exist and captions match; main/supplement placement
   matches the controller.
4. Package QA: word counts, placeholders and citation workflow are recorded;
   re-render after final edits when render tooling exists.
5. Verdict: `PASS`, `PASS_WITH_WARNINGS` (needs the user's explicit
   acceptance), or `BLOCKED`.

## Pre-Submission Review Mode

Use `pre-submission-review` after QA, when the user wants reviewer-style
critique before first submission. It judges merit, not data integrity, and does
not rewrite unless asked.

Assess journal fit and contribution, argument quality, methods and reporting
clarity at a manuscript level, and the likeliest reviewer objections. Rank fixes
must-fix, should-fix or optional, link integrity issues back to the QA report,
and recommend the next mode (`draft`, `qa` or `package`).

## Artifact Contracts

- **Manuscript Draft Package**: draft and render paths, inputs used, section word
  counts and deviations, citation workflow, display references, placeholder and
  unresolved-item log, known limitations.
- **Style-Polished Draft Package**: source and polished paths, author-sample
  status, change summary, preserved-content check, word-count changes,
  unresolved passages, disclosure notes.
- **QA Gate Report**: verdict; claim, citation, claim-source, data and package
  QA; blockers; warnings; handoff readiness.
- **Pre-Submission Review Report**: journal fit and contribution, strengths,
  must-fix, should-fix and optional items, likely objections, next mode.
