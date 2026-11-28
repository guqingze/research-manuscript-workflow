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
   using declarative subheadings where the journal allows them and brief question-framing lead-ins without
   interpretation; Discussion from both, separating evidence, inference,
   limitations and implications. Apply `references/defensive-writing-discipline.md`:
   each Discussion paragraph opens with its interpretation, no caveat is added
   that fails its keep test, controller audit guardrails become positive scope
   definitions rather than negative denials ("Audit Provenance ≠ Article Prose"),
   one canonical estimator leads each main-text question, and any unfinished
   multi-stage component stays strictly quarantined in isolated `[PENDING: …]`
   blocks without bleeding disclaimers into completed sections.
2. Never invent citations, numbers, table references or methods details; log
   placeholders and unresolved items instead. Use the live-citation workflow
   when available.
3. Before handoff, check that every major claim has a citation or output
   source, displays exist, and word counts are recorded against the controller.
   When the repo has a render command, render and save the draft in its
   manuscript output directory. Hand off to `style-polish` or `qa`.

## Style Polish Mode

Use `style-polish` after `draft` or `revise` for readability and author voice.

Core rule: improve prose without changing the science. Polish for clarity, not
to evade AI detection or hide AI assistance; keep any required disclosure.

Procedure:

1. Lock numbers, estimates, intervals, definitions, citation keys, display
   references and section claims unless the user asks for scientific revision.
2. Calibrate to author samples when available; discipline and journal
   conventions override personal style. Make the calibration measurable: read
   the sample and write down its observable traits as rules before rewriting
   (for example: each Results paragraph opens with the finding in words, then
   the numbers in brackets; at most two estimates with intervals per sentence;
   sensitivity checks collapsed to one closing sentence; Discussion paragraphs
   carry one or two numbers at most; Limitations open with the study's
   strengths). Rewrite one representative Results and one Discussion paragraph
   as a before/after sample and get the author's agreement on the voice before
   rewriting the whole paper. Apply the jargon test: a term the author has to
   ask about will not be understood by readers either; explain it in plain
   words or move it to the Supplement.
3. Cut filler, throat-clearing, inflated novelty and template-like rhythm; keep
   academic register and precise Methods prose. For epidemiology,
   clinical-epidemiology or population-health papers, apply
   `references/epidemiology-manuscript-discipline.md` and the project's revision
   lessons file if one exists.
4. Cut defensive writing per `references/defensive-writing-discipline.md`:
   delete every caveat that fails its keep test and merge or drop minor
   Limitations toward its default cap, applying its overclaim guard. Do not
   weaken a limitation that passes the keep test; if more than the cap still
   change interpretation, keep them and list the excess for the author.
5. If a smoother sentence loses its tie to a source, or polishing would change
   meaning, leave the passage and list it.
   If polishing exposes content uncertainty, return to `draft`; otherwise hand
   off to `qa`.

## QA Gate Mode

Use `qa` on the latest draft, polished draft or revised draft. It checks
factual readiness, not merit.

Core rule: every claim, number and citation traces to its source.

Scope: every file that will be submitted (main text, supplements, cover
letter), including files drafted in earlier phases and never re-polished, and
every part of each file: title, headings, display captions and legends, table
notes, data- and code-availability statements, acknowledgements and the
reference list with any line above it. Each check below applies to all of
them.

Procedure:

1. Claim QA: classify major claims as literature-backed, analysis-backed, mixed
   or unsupported; analysis claims must match the results report and current
   outputs; flag causal overreach, inflated novelty, and Discussion claims
   stronger than the evidence. For epidemiology manuscripts, apply the
   epidemiology discipline (no interpretation in Results, design-matched causal
   wording, no internal language, references numbered by first appearance).
   Check calibration in the other direction too, per
   `references/defensive-writing-discipline.md`: a leaked audit-ledger denial,
   or a pending-component disclaimer or `[PENDING: …]` block in a completed
   section (other than an author-approved bare result slot), is a blocker
   regardless of the keep test; a caveat or hedge that fails its keep test in
   Results or in the Abstract's headline result is a blocker (design-matched
   wording such as "no clear association" passes); competing developmental
   baselines in main-text Results, defensive writing elsewhere, or more
   Limitations items than the cap (even when each is material) is a warning; a cut
   that breaks the overclaim guard is a blocker.
2. Citation QA: in-text citations map to the reference collection; no orphans;
   metadata complete; apply the citation-verification discipline (SKILL.md) to
   important claims. Check each rendered reference entry, not only its key:
   every DOI, URL or PMID must be a real, resolving identifier, never a
   placeholder value (`unresolved`, `TODO`, `N/A`, an empty DOI path) or
   dangling punctuation left by an empty field. When a work has no verified
   DOI, fall back to a verified PMID or the journal's own article locator, or
   omit the identifier.
3. Data QA: numbers, denominators, model labels, intervals and p-values match
   outputs; displays exist and captions match; main/supplement placement
   matches the controller. Trace every main-text number to its source and
   sample; for model-derived estimates, also name the model and validation
   design that produced them, and flag any sentence that
   credits a result to a different estimator (for example, a full-proteome
   held-out result written as the performance of a compact panel, or
   development cross-validation written as validation of final coefficients).
   Supersession sweep: when an analysis has been superseded or the scope
   narrowed, search every supplementary table, figure (including in-image
   titles, subtitles, axis and legend labels), legend, Supplementary Methods
   section and table- or figure-generating script for its remnants; a display
   that no remaining sentence relies on is removed with its Methods text, not
   relabelled. Display vocabulary: column headers, generated row labels and
   in-image text use readable scientific labels, never code-level variable
   names (for example `log_ast`), internal tiers or workflow labels. The same
   holds for Supplementary Methods prose: no software class or function names
   where the method has a standard name, no code-style notation, and no raw
   source-data field names left in another language than the document's.
4. Package QA: word counts, placeholders and citation workflow are recorded;
   re-render after final edits when render tooling exists. No repository
   paths, file names, build notes or generation remarks appear in submitted
   text; a data- or code-availability statement names the public repository or
   access route, not its internal layout. When the deliverable is a rendered
   file (`.docx`, `.pdf`), rerun the placeholder, internal-language and
   leftover-markup scans on text extracted from that file, not only on its
   source, and look at the title page, any panel or box, wide tables,
   embedded figures and the reference pages as rendered. After any
   renumbering of references or supplementary items, confirm the same mapping
   reached the supplement, table cells, the scripts that generate tables and
   figures, and links between documents. An unresolved
   `[PENDING: …]` block is a blocker for a submission package; in an internal
   review draft it is recorded, not blocked.
5. Verdict: `PASS`, `PASS_WITH_WARNINGS` (needs the user's explicit
   acceptance), or `BLOCKED`. Pattern scans are a floor, not the gate: they
   miss variant word forms, undefined abbreviations and engineering register.
   Before issuing `PASS`, read every submitted file end to end, in the order
   an editor opens them (title, abstract, main text, end matter, references,
   supplement), and record that read in the report.

## Pre-Submission Review Mode

Use `pre-submission-review` after QA, when the user wants reviewer-style
critique before first submission. It judges merit, not data integrity, and does
not rewrite unless asked. Likely objections stay in the report; they reach the
manuscript only through a fix the user approves, never as pre-emptive caveats.

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
- **QA Gate Report**: verdict; files and rendered outputs checked; claim
  (including calibration), citation, claim-source, data and package QA;
  full-read record; blockers; warnings; handoff readiness.
- **Pre-Submission Review Report**: journal fit and contribution, strengths,
  must-fix, should-fix and optional items, likely objections, next mode.
