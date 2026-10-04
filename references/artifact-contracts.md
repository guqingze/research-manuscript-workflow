## Artifact Contracts

Keep contracts lightweight. Use the repo's existing formats when available, but
ensure each artifact carries the fields needed for later sessions to consume it
without re-discovering everything.

- **Literature search record**: research question or scoped topic, databases or
  sources searched, search date and local timezone, round ID and trigger, query
  strings and filters, inclusion/exclusion criteria, raw/de-duplicated/screened
  counts, retained candidate sources with stable IDs and PMID/DOI/URL metadata,
  exclusion notes, citation-chasing or named-project searches, non-auditable
  reserve suggestions, unresolved metadata, and acquisition handoff status.
- **Literature acquisition queue**: `source_id`, tier or priority, title, PMID,
  DOI, URL, manuscript role, target collection, reference-manager status, PDF
  attachment status, local cache status, and next human action.
- **Literature index**: `citation_key`, title, year, paper role, themes, key
  claims, caveats, reference-manager item key, and markdown-cache status
  (`md` path, conversion method, source PDF checksum).
- **Markdown cache manifest**: per paper — reference-manager item key and
  attachment key, collection, source PDF path, `md` path, source SHA-256,
  conversion method (`markdown` | `plaintext_fallback` | `needs_ocr`), status,
  and char count. PDFs remain in the reference manager and are not committed to
  the repo.
- **Evidence-extraction cache**: per paper — `citation_key`, source `md` path and
  SHA-256 (mirrored from the markdown-cache manifest), `schema_version`, study
  characterization (design, setting, population, N, modality, cutoffs), an
  evidence grade, a list of anchored quantitative findings (each: claim, value,
  CI/p, adjustment set, and a `quote`/`section`/`table` anchor), relevance tags
  (manuscript role, which claim it bears on, convergence/divergence note, caveat),
  and `verification_status`. Full field-level schema, anchor rules, and the worker
  prompt template live in `evidence-extraction-contract.md`; a mirrored
  SHA-keyed extraction-cache manifest makes rebuilds idempotent. Anchors are
  verified by `../scripts/verify_extract_anchors.py`.
- **Gap synthesis**: evidence matrix, key themes, convergence/divergence map,
  contradiction table, gap taxonomy, positioning claim, CER chains, synthesis
  limitations, SAP/outline implications, and claims requiring PDF verification
  before drafting.
- **Planned-analyses roadmap**: candidate analyses with driver/source;
  per-candidate in-cohort/in-data availability audit (completeness, subcohort,
  confounder/mediator/collider status); role and effort-tier classification;
  run-now/defer/convert-to-limitation recommendation; and a separated
  non-auditable/speculative reserve.
- **Analysis Refresh Report**: commands run or inspected, run label/date,
  relevant input and output paths, cohort/sample definitions, exclusion flow,
  denominators, result artifact inventory, primary/secondary/sensitivity labels,
  statistical interpretation, fallacy and overclaim scan, table/figure
  provenance, Results-ready claims, Discussion-only interpretations,
  supplement-only findings, unresolved blockers, and recommended next actions.
- **Reflection memo**: per-result convergence/divergence/silence against the
  indexed literature; interpreted contradictions with likely reason; internal-
  meeting feedback digest and resulting actions; drivers for planned-analyses and
  SAP updates; and open questions and Discussion seeds.
- **SAP/Outline Controller**: target journal or audience if known, manuscript
  structure pattern, central thesis or positioning claim, section outline,
  section purposes, word count allocation, argument map, CER-to-section mapping,
  evidence/result/table/figure map, primary and secondary analyses, sensitivity
  and exploratory labels, supplement placement, transition logic, drafting
  instructions, and unresolved decisions.
- **Narrative deck**: spine/storyline and locked framing decisions (with options
  considered and set aside); act/section structure with per-slide takeaways and
  presenter notes; on-slide claims anchored to the Analysis Refresh Report or
  verified literature records with per-slide citations; open framing questions for
  the group; and feedback routed back to reflection/analysis-plan.
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
- **Pre-Submission Review Report**: journal fit, contribution assessment,
  manuscript strengths, must-fix issues, should-fix issues, optional
  improvements, likely reviewer objections, and recommended next mode.
- **Journal Submission Package**: target journal, article type, final
  manuscript paths, figure/table/supplement paths, cover letter, required
  statements, citation/reference status, journal checklist, blockers, commands
  run, and render status.
- **Revision Roadmap**: decision context, parsed comment inventory, raw comment
  text, reviewer/editor source, severity, priority, target section, suggested
  action, cross-reviewer patterns, new analysis/literature needs, suggested
  revision order, and response-letter skeleton.
- **Revised Manuscript Draft Package**: revised draft/render paths, revision
  log mapped to comment IDs, resolved/unresolved/blocked items,
  response-to-reviewers draft, updated placeholders, source inputs, commands
  used, and recommended next mode.
- **Response Package**: revised manuscript paths, clean/tracked/change-log paths
  when available, response-to-reviewers letter, editor cover letter or
  resubmission note, comment-resolution checklist, updated QA Gate Report path,
  and journal resubmission checklist.
- **Handoff note**: final artifact paths, commands run, outputs changed, known
  limitations, and next human actions.
