# Literature

## Literature Search Mode

Use `literature-search` to find candidate papers before they are curated in the
reference manager. The output is a reproducible search record plus a candidate
table and acquisition queue that later runs can reconcile by DOI, PMID, URL and
normalized title without re-parsing prose.

Core rule: the record must be auditable. Never invent counts, metadata or
papers.

Procedure:

1. Fix the question, sources, queries, date limits and inclusion/exclusion
   criteria before screening. Do not retrofit criteria to justify preferred
   papers.
2. Write each query's returned count into the record when the query runs. A
   count not captured then is recorded as `not logged`, never reconstructed.
3. Verify each retained paper against an authoritative record (DOI, PubMed,
   Crossref, OpenAlex, publisher). Mark unresolved metadata instead of guessing.
4. Record each retained source's `claim_basis`: `abstract`, `full_text`, or
   `pdf_verified`. Abstract-only claims may shape plans but must be verified
   against the full text before drafting.
5. Separate the auditable core from reserve suggestions (for example "add a
   methods paper for X if needed"), so reserves are never counted as missing
   reference-manager items.
6. When the search supports a pooled comparison or meta-analysis, check
   comparability before pooling: sampling frame, population, measurement
   modality and thresholds, quality rules, strata, and crude versus adjusted
   estimands. If they do not harmonize, present a structured comparison rather
   than a pooled estimate.
7. Produce the acquisition queue for the human: the papers to add to the
   reference manager, grouped by priority, with DOI/PubMed/publisher links. Do
   not handle institutional credentials or bypass paywalls.
8. Stop at the record and queue. Do not write the gap synthesis or the index.

A quick scouting search (for example, while weighing storyline options) may use
a dated record with status `scouting`; complete its criteria, counts and
candidate table before it supports a gap synthesis, SAP or draft.

### Search rounds

Re-enter `literature-search` with a new dated record whenever the manuscript
gains a new comparison population, outcome, modality, section or reviewer
request, or otherwise changes scope materially, or when the search horizon has
aged. A meeting decision that adds a new comparison is a search trigger, not
just a request for citations. An index refresh is not a search. Do not
overwrite a completed round; link the new round to what triggered it.

## Literature Ingest Mode

Use `literature-ingest` after the user has added records and PDFs to the
reference-manager collection. It syncs the collection into the repo's committed
literature layer: membership and citation keys, the markdown full-text cache and
its manifest, and the literature index.

Core rule: the reference manager holds the canonical PDFs and metadata; the repo
holds only derived markdown and a manifest (unless the repo explicitly says
otherwise).

Procedure:

1. Reconcile the collection against the search record's acquisition queue by
   DOI, PMID, URL and normalized title. Report missing records separately from
   records that lack a PDF attachment.
2. Locate PDFs read-only. For Zotero: read the data directory from the profile
   `prefs.js` (`extensions.zotero.dataDir`); copy `zotero.sqlite` before
   querying to avoid locks; map collection → items → `itemAttachments` (`path`
   like `storage:<file>.pdf`) → `<dataDir>/storage/<attachmentKey>/<file>.pdf`.
3. Convert each new or changed PDF to markdown (keyed by SHA-256; `--force`
   rebuilds all). Default converter, CPU-only, good for born-digital papers;
   substitute marker, Docling or OCR for scans or math-heavy pages:

   ```python
   import pymupdf4llm, pymupdf, pathlib
   md = pymupdf4llm.to_markdown(str(pdf_path), show_progress=False)
   if not md.strip():
       doc = pymupdf.open(str(pdf_path))
       text = "".join(p.get_text() for p in doc)
       md = text if text.strip() else None   # None: scan with no text layer, flag needs_ocr, write nothing
   if md:
       pathlib.Path(md_path).write_text(md, encoding="utf-8")
   ```

4. Write the manifest and regenerate the index with the repo's generator. If
   none exists, propose a small committed index format before large drafting.
5. Read the markdown cache for content from here on; open the canonical PDF
   only to verify exact numbers, thresholds, definitions or wording, especially
   for `plaintext_fallback` or `needs_ocr` entries.

## Gap Synthesis Mode

Use `gap-synthesis` once the index is stable, to make the manuscript's position
explicit before the SAP/outline.

Core rule: integrate across sources; do not summarize papers one by one. Keep
the paper inventory in the index, not here.

Procedure:

1. Build a compact evidence matrix first: themes, supporting and contradicting
   papers, population, method, evidence strength, manuscript use.
2. Map convergence, divergence and silence. Interpret contradictions
   (population, definitions, methods, confounding control, follow-up, date)
   rather than explaining them away.
3. Name the gap type (empirical, methodological, definitional, population,
   temporal, mechanistic, generalizability, and so on) instead of vague gap
   language.
4. Write claim-evidence-reasoning (CER) chains for manuscript-facing claims,
   each with its caveat and target section.
5. Stress-test: would the gap survive removing the strongest supporting paper,
   and what would a sceptical reviewer call overstated?
6. If a target journal is known, scan what it has published on the topic in
   about the last five years and state how this manuscript differs from the
   closest papers. A gap already filled there is not a gap.
7. Hand off to `sap-outline`: which Introduction claims, methods
   justifications, primary analyses, Discussion comparisons and supplement-only
   claims follow. Stop there.

### Key-paper evidence extraction (`evidence-extraction`)

Warn the user before running: every selected paper is read in full by a worker,
which is token-heavy.

Use it when the key-paper set is larger than about 25–30 papers, when the user
wants a full-text-grounded synthesis, or when the same numbers will be reused in
reflection, drafting and QA. For smaller sets, read the markdown cache directly.

1. Propose the key-paper set (anchor, counter-example and benchmark papers, plus
   any the user names) with a reason for each, and let the user confirm or trim
   it. Extract the whole corpus only on request.
2. Map: fan out to parallel workers that can write files, about 5–6 papers per
   worker, using a cheaper model than the one doing the reduce. Each worker reads
   only its assigned markdown files and writes one record per paper following
   `references/evidence-extraction-contract.md`. Confine writes to the
   extraction-cache directory. Re-extract only when a source SHA or the schema
   version changes.
3. Verify: run `scripts/verify_extract_anchors.py` over the whole cache and fix
   or quarantine every hard failure; then re-read only the numbers bound for
   the manuscript.
4. Reduce in the session that holds the project context, not in a cold
   subagent, into the gap synthesis above. Use a hierarchical reduce only if the
   cache will not fit one context.

## Artifact Contracts

- **Literature search record**: round ID, trigger and status; dates and
  timezone; sources, exact queries, filters and limits; inclusion/exclusion
  criteria; counts as logged; retained candidates (`source_id`, tier,
  `title`, `first_author`, `year`, journal, PMID, DOI, URL, role, inclusion
  reason, verification status, `claim_basis`); exclusions; reserve
  suggestions; unresolved metadata.
- **Acquisition queue**: `source_id`, priority, title, PMID, DOI, URL, role,
  target collection, reference-manager status, PDF status, next human action.
- **Literature index** (generated, not hand-edited): `citation_key`, title,
  year, role, themes, key claims, caveats, `claim_basis`, reference-manager item
  key, and cache status (`md` path, conversion method, source SHA-256).
- **Markdown cache manifest**: per paper, the item and attachment keys,
  collection, source PDF path, `md` path, source SHA-256, conversion method
  (`markdown` | `plaintext_fallback` | `needs_ocr`), status and character count.
- **Gap synthesis**: evidence matrix, convergence/divergence/silence map,
  contradiction notes, gap types, positioning claim, target-journal scan, CER
  chains, stress-test notes, SAP implications, and claims needing PDF
  verification.
