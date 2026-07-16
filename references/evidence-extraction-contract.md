# Evidence-Extraction Contract

This document is the field-level contract for the **evidence-extraction cache**
used by `gap-synthesis` mode's large-corpus subagent map-reduce. It defines the
per-paper record schema, the anchor rules, the idempotency manifest, and the
worker prompt template. The cache is a generated, committed artifact: one record
per cached full text, produced by fan-out worker subagents and verified by
`scripts/verify_extract_anchors.py`.

Design intent: after extraction, gap synthesis, drafting, and QA should be able to
read verified numbers from the cache without re-reading full text, and any cached
number should be mechanically traceable back to a verbatim string in its source.

## Record location and format

- One file per paper: `<repo-literature-dir>/extracts/<citation_key>.md`
  (mirrors the `fulltext/<citation_key>.md` naming so the two caches align).
- Format: YAML front-matter (machine-parsed by the checker and the reduce) plus a
  markdown body (human-readable relevance narrative and caveats).
- Extraction-cache manifest: `<repo-literature-dir>/extracts/manifest.csv` with
  columns `citation_key,md_file,source_sha256,schema_version,extracted_at`. The
  `source_sha256` is copied from the markdown-cache manifest so a paper is
  re-extracted only when its source SHA (or `schema_version`) changes.

## Front-matter schema (schema_version: 1)

```yaml
---
citation_key: chan2014            # bibtex/index key; matches fulltext/<key>.md
md_file: fulltext/chan2014.md     # source read for this record (repo-relative)
source_sha256: <hex>              # copied from the markdown-cache manifest
schema_version: 1
title: "Non-alcoholic fatty liver disease in a young multiracial Asian population"
year: 2014
first_author: Chan
journal: Hepatology International
design: cross-sectional           # cross-sectional | cohort | rct | meta-analysis | review | guideline | other
country_setting: Malaysia
population: "young multiracial medical students, mean age 23"
n_total: 469
modality: ultrasound              # vcte-cap-lsm | ultrasound | mrs | fli | biopsy | mixed | na
cutoffs_used: ""                  # e.g. "CAP S1 248 dB/m; LSM F2 8 kPa"; "" if n/a
evidence_grade: C                 # A | B | C | D | F (per evidence-assessment rubric)
manuscript_role: regional-comparator   # intro-burden | methods-cutoff | regional-comparator | glycemia | adiposity | prognosis | stats | background
bears_on_claim: "ethnic differences attenuate after metabolic adjustment"
verification_status: fulltext_verified  # fulltext_verified | needs_pdf | metadata_gap
findings:
  - claim: "overall NAFLD prevalence"
    value: "7.9%"
    ci_p: ""
    adjust: crude
    anchor_kind: quote            # quote | section | table | none
    anchor: "The overall prevalence of NAFLD was 7.9"
  - claim: "adjusted ethnicity OR, Malay vs Chinese"
    value: "3.01"
    ci_p: "95% CI 0.99-9.15, p=0.052"
    adjust: "male sex, obesity, hypertriglyceridemia"
    anchor_kind: table
    anchor: "Table 3 multivariate Race Malay"
---
```

Body (markdown, after the front-matter): a short prose block covering the paper's
relevance to the project's argument, its convergence/divergence with the expected
finding, and why it should not be overused. Keep it integrative, not a re-summary
of the abstract.

## Anchor rules (the trust mechanism)

Every row in `findings` must carry an anchor so the number is auditable:

- `anchor_kind: quote` — `anchor` is a **verbatim** string of at most 25 words
  copied from the source markdown. The checker normalizes whitespace and case and
  requires it to be a substring of `fulltext/<key>.md`. Use for any number that
  will reach the manuscript.
- `anchor_kind: section` — `anchor` names a section/subsection heading present in
  the source (soft-checked: warned, not failed, if not literally found).
- `anchor_kind: table` — `anchor` names a table/figure label present in the source
  (soft-checked).
- `anchor_kind: none` — allowed **only** when `verification_status: needs_pdf`
  (the number could not be anchored to the text layer and must be re-checked
  against the PDF before it may be cited). A `none` anchor on a
  `fulltext_verified` record is a hard failure.

No-unanchored-number rule: a `findings` row with no anchor, or `anchor_kind: none`
on a verified record, is a contract violation. Do not let an un-anchored number
become a manuscript claim.

Extraction discipline (borrowed, standalone): workers **emit** anchors from the
full text they were given; they do not self-audit. Verification is a separate,
mechanical step (`verify_extract_anchors.py`) plus a targeted human/orchestrator
re-read of manuscript-bound numbers. Cap findings at the manuscript-relevant
numbers (roughly the 8 most decision-relevant per paper); do not transcribe every
table cell.

## Worker prompt template (engine-agnostic)

Give each worker only its batch of full-text files and this instruction. Do not
give it the desired conclusion — extract neutrally.

```
You are an evidence-extraction worker for a research manuscript. For each paper
markdown file listed below, read ONLY that file and write one record to
extracts/<citation_key>.md following references/evidence-extraction-contract.md
(schema_version 1): YAML front-matter with the required fields plus a `findings`
list, then a short markdown body on relevance/convergence/caveats.

Rules:
- Copy source_sha256 for each paper from <markdown-cache manifest path>.
- Every findings row MUST have an anchor. For any number that could appear in a
  manuscript, use anchor_kind: quote with a verbatim string of <=25 words copied
  exactly from the paper. Use section/table anchors for structural references.
- If you cannot anchor a number to the paper's text, set anchor_kind: none AND
  verification_status: needs_pdf.
- Extract at most ~8 manuscript-relevant numbers per paper. Do not invent values,
  CIs, or p-values. If a field is unknown, leave it empty; do not guess.
- Neutral extraction: record what the paper reports, not what fits a hypothesis.

Project context (for relevance tagging only, NOT a conclusion to confirm):
<one paragraph: the project's primary question, exposure, outcomes, comparators>

Papers in this batch:
<list of fulltext/<key>.md paths>
```

Codex worker invocation (workers write, scoped to the extraction-cache dir):

```
codex exec -m <model> -c model_reasoning_effort=medium \
  --sandbox workspace-write --cd <repo> -a never "<the prompt above>"
```

Claude worker invocation: dispatch a `general-purpose` agent with `Write` enabled
and the same prompt; run batches in the background and gate the reduce on
completion.

## Verification and reduce

1. Build/refresh extracts for changed papers (idempotent via the SHA manifest).
2. Run `scripts/verify_extract_anchors.py --extracts <extracts-dir> --fulltext
   <fulltext-dir> --manifest <markdown-cache-manifest>`; fix or quarantine every
   hard failure (missing quote, unanchored number on a verified record, SHA
   mismatch).
3. Re-read the manuscript-bound numbers (anchor comparators + any figure reaching
   prose) to catch misinterpretation of otherwise-valid quotes.
4. Reduce in-context (the session orchestrator, not a cold subagent) into the gap
   synthesis. Hierarchical fallback only if the cache cannot fit one context.
