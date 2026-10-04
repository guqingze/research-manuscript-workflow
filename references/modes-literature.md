# Literature

## Literature Search Mode

Use `literature-search` when the user wants to find candidate papers before
curating them in Zotero or generating the literature index. Borrow the
discipline of ARS `deep-research` Phase 2, but keep the output repo-oriented and
ready for reference-manager import and full-text acquisition.

This mode should produce a reproducible search record and a machine-auditable
candidate corpus. It should not assume that PDFs are already available. In
projects where the user retrieves full text through university or institutional
access, make the next human action obvious for each retained source.

Minimum procedure:

1. Define search parameters: research question or scoped topic, databases or
   sources, keywords and synonyms, Boolean strategy, date range, languages, and
   document types.
2. Apply inclusion and exclusion criteria before screening results. Do not
   retrofit criteria to justify already-preferred papers.
3. Screen in two passes when enough metadata is available: title/abstract first,
   then full text or detailed metadata for retained sources.
4. Record reproducibility details: search date, database/source, query string,
   raw hit count, screened count, excluded count, and inclusion reasons for
   retained sources.
5. Verify candidate existence with DOI, publisher, PubMed, Crossref, Semantic
   Scholar, OpenAlex, or another authoritative record when feasible. Mark
   unresolved metadata explicitly instead of inventing it.
6. Make the retained corpus auditable by later `literature-acquisition` and
   `literature-ingest` runs. For each retained source, include stable fields
   such as `source_id`, tier or priority, title, first author, year, journal or
   source, PMID, DOI, URL, manuscript role, verification status, and unresolved
   metadata.
7. Add acquisition handoff fields when the next step is Zotero/PDF collection:
   `target_collection`, `zotero_status`, `pdf_status`, `local_cache_status`,
   and `next_human_action`. Default these to pending or unknown rather than
   implying that the paper has been collected.
8. Separate auditable core sources from reserve or conditional suggestions.
   Mark generic reserve suggestions, such as "add PRS-CS/LDpred2 methods papers
   if needed", as non-auditable so they are not counted as missing
   reference-manager items during later reconciliation.
9. Stop at candidate corpus and search documentation. Do not write the gap
   synthesis, manuscript prose, or literature index unless the user also asked
   for the next mode.

Default output: a search strategy report plus a candidate source table suitable
for Zotero import or manual curation. The table should be stable enough that a
later run can compare it against a Zotero collection by DOI, PMID, URL, and
normalized title without re-parsing prose.

Recommended candidate table columns:

`source_id`, `audit_scope`, `tier`, `priority`, `title`, `first_author`,
`year`, `journal_or_source`, `PMID`, `DOI`, `URL`, `manuscript_role`,
`inclusion_reason`, `verification_status`, `target_collection`,
`zotero_status`, `pdf_status`, `local_cache_status`, `next_human_action`,
`notes`.

### Literature refresh/search-round rule

Re-enter `literature-search` whenever the manuscript gains a new comparison
population, outcome, modality, section, reviewer request, or other material
scope change, or when the planned search horizon has meaningfully aged. A
meeting decision that promotes a new global comparison is a search trigger,
not merely a request to add citations. Do not treat a Zotero or literature-index
refresh as evidence that a new search was performed.

For every refresh, create a new dated search record in the project repository
before importing papers. The record must identify the round and trigger, search
date and local timezone, sources/interfaces, exact queries and filters, date
limits, languages/document types, predeclared inclusion/exclusion criteria,
raw/de-duplicated/screened/full-text/included counts, citation-chasing or
named-project searches, retained candidates with stable identifiers, exclusions,
reserve suggestions, unresolved metadata, and the next Zotero/acquisition
action. A record can be opened as `planned`, but it must not contain invented
counts. Do not overwrite a completed round; link the new round to the issue,
meeting note, or roadmap that triggered it.

When the search supports a prevalence comparison or meta-analysis, add a
comparability gate before pooling: sampling frame, geography/ethnicity,
population size and structure, modality, CAP/LSM thresholds, probe, quality
rules, BMI/obesity strata, and crude versus adjusted estimands. If these are
not sufficiently harmonizable, retain the studies as a structured comparison
or separate evidence tiers rather than presenting a pooled estimate as if it
were directly comparable.

## Literature Acquisition Mode

Use `literature-acquisition` after candidate papers have been identified but
before literature indexing. This mode supports a human-in-the-loop full-text
collection workflow where the user may need institutional credentials to access
publisher PDFs.

Minimum procedure:

1. Read the literature search record and identify the auditable core corpus.
   Keep reserve or non-auditable suggestions separate.
2. Resolve or confirm the target reference-manager collection name/key.
3. Generate or update an acquisition queue with stable source IDs, title, PMID,
   DOI, URL, tier or priority, manuscript role, reference-manager status, and
   PDF attachment status.
4. When the reference manager is reachable, compare the queue against the target
   collection by DOI, PMID, URL, and normalized title. Report missing collection
   items separately from items that exist but lack PDF attachments.
5. Help the user work the manual download queue by grouping missing items by
   priority and providing PubMed, DOI, or publisher URLs. If asked, open or list
   target links, but do not handle institutional credentials or bypass paywalls.
6. After the user confirms that records/PDFs have been added to the collection,
   hand off to `literature-ingest` to build the markdown cache from the
   collection's PDFs, write the manifest, and regenerate the literature index.
   PDFs stay in the reference manager; they are not copied into the repo.

Default output: an acquisition checklist or CSV plus a concise list of missing
reference-manager records and missing PDF attachments.

## Gap Synthesis Mode

Use `gap-synthesis` after `literature-ingest` has produced a stable literature
index. This mode performs interpretation across indexed papers. It should make
the manuscript's intellectual position explicit before SAP/outline or drafting.

Core rule: integrate across sources, do not summarize papers sequentially.

Minimum procedure:

1. Build or update a compact evidence matrix before writing prose. Include
   themes, supporting papers, contradicting papers, population or context,
   method type, evidence strength, and manuscript use.
2. Identify convergence, divergence, and silence:
   - convergence: where multiple sources support the same claim;
   - divergence: where sources conflict or imply different boundary conditions;
   - silence: where the indexed literature lacks evidence needed for the
     manuscript's question.
3. Resolve or explain contradictions where possible. Consider population,
   geography, endpoint/exposure definitions, methods, confounding control,
   follow-up period, study quality, and publication date.
4. Classify the gap instead of using vague gap language. Useful types include
   empirical, methodological, definition, temporal, geographic, translation,
   mechanistic, ancestry/population, prospective-cohort, endpoint-harmonization,
   and PRS/generalizability gaps.
5. Produce claim-evidence-reasoning (CER) chains for manuscript-facing claims:
   each claim needs cited evidence, reasoning, caveat or hedge, and suggested
   manuscript section.
6. Run a short stress test before finalizing:
   - Has the synthesis cherry-picked supportive papers?
   - Are contradictions interpreted rather than explained away?
   - Would the gap still stand if the strongest supporting paper were removed?
   - What would a skeptical reviewer say is overstated?
   - Does the proposed gap justify the project's actual analyses?
7. Hand off explicitly to `sap-outline`: state which introduction claims,
   methods justifications, primary analyses, discussion comparisons, and
   supplement-only claims should follow from the synthesis.
8. Stop at synthesis and handoff guidance. Do not write manuscript prose or
   decide final table/figure order unless the user also asked for the next mode.

Default output: an integrated gap synthesis with an evidence matrix,
convergence/divergence map, gap taxonomy, positioning claim, CER chains, stress
test notes, and SAP/outline implications.

### Key-paper evidence extraction (subagent map-reduce)

> **Token cost — warn the user before running.** Fanning out full-text extraction
> is one of the most token-expensive operations in this workflow: every selected
> paper is read in full by a worker, and larger sets multiply that cost. State the
> intended scope and that this step is token-heavy before starting, and default to
> a focused key-paper set rather than the whole corpus.

Reading a large full-text corpus directly into one context to synthesize it
either overflows the context or silently regresses to abstract-level summary.
Build the gap synthesis with an explicit map-reduce that first materializes a
persistent, verifiable **evidence-extraction cache** for the papers that matter,
then reduces from that cache.

**Extract the identified key papers, not the whole corpus.** Before fanning out,
select the subset that actually bears on the manuscript's claims — anchor,
counter-example, and benchmark papers (by role and theme in the literature index)
plus any the user names. This is a **human-in-the-loop** step, especially when
token-limited: propose the key-paper set with the reason each is "key", and let
the user confirm, add, or trim it before extraction runs. Reserve full-corpus
extraction for when the user explicitly wants exhaustive full-text grounding.

When to build a cache at all (vs reading the markdown cache directly in-context):

- the selected key-paper set is larger than roughly 25-30 papers, or
- the user explicitly asks for a full-text-grounded synthesis, or
- the same extracted numbers will be reused across reflection, drafting, and QA.

For a smaller key-paper set, read those markdown files directly in-context; the
map-reduce overhead is not worth it.

**Map (parallel worker subagents, engine-agnostic, workers write).** Fan out the
selected key papers in small batches (~5-6 papers per worker). Each worker reads
only the assigned full-text markdown files and writes one committed record per paper into
the evidence-extraction cache, following `references/evidence-extraction-contract.md`
(schema, three-layer anchor rules, and the worker prompt template). The worker
engine is pluggable and both session hosts are supported:

| Session host | Claude workers | Codex workers |
|---|---|---|
| Claude Code | Agent tool, `general-purpose`, `Write` enabled, background | Bash fan-out of `codex exec` |
| Codex | `claude` CLI workers if present | native `codex exec` fan-out |

Codex worker invocation (read the papers, write records, scoped to the cache dir):
`codex exec -m <model> -c model_reasoning_effort=medium --sandbox workspace-write --cd <repo> -a never`.
Extraction is mechanical structured transcription against a fixed schema, so run
workers one model tier below the reduce (a cheaper/faster model), keep the
session's strongest model for the reduce, and confine worker writes to the
extraction-cache directory (audit with `git diff` plus the anchor checker).

Make extraction idempotent: mirror the markdown-cache manifest into an
extraction-cache manifest keyed to each source's SHA-256, and re-extract a paper
only when its source SHA or the schema version changed (`--force` rebuilds all).

**Verify (100% mechanical + targeted human).** Before reducing, run the shared
checker `scripts/verify_extract_anchors.py` over the whole cache: it decodes every
`quote` anchor and substring-matches it against the source markdown, enforces the
no-unanchored-number rule (any quantitative finding lacking a `quote`/`section`/
`table` anchor must be flagged `verification_status: needs_pdf`), and checks each
record's source SHA against the manifest. Fix or quarantine every hard failure.
Then re-read (human/orchestrator) only the numbers bound for the manuscript (the
anchor comparators and any figure that will reach prose) to catch
misinterpretation of otherwise-valid quotes.

**Reduce (orchestrator, in-context, with project context).** The session
orchestrator — not a fresh cold subagent — reads the whole verified cache in one
context and writes the gap synthesis. Doing the reduce in the session that holds
the project's results, SAP, and positioning discussion is deliberate: a cold
synthesis subagent re-derives the story from scratch and drifts toward stale or
generic framing. If a corpus is too large for the cache to fit one context, fall
back to a hierarchical reduce (batch-level partial syntheses from subagents, then
an orchestrator merge) rather than handing the whole reduce to a subagent.

The reduce output is the same integrated gap synthesis specified above; the cache
only changes how its evidence is sourced and verified, not the synthesis contract.

## Artifact Contracts

- **Literature search record**: research question or scoped topic, databases or
  sources searched, search date and local timezone, round ID and trigger, query
  strings and filters, inclusion/exclusion criteria, raw/de-duplicated/screened
  counts, retained candidate sources with stable IDs and PMID/DOI/URL metadata,
  exclusion notes, citation-chasing or named-project searches, non-auditable
  reserve suggestions, unresolved metadata, and acquisition handoff status.
- **Literature acquisition queue**: `source_id`, tier or priority, title, PMID,
  DOI, URL, manuscript role, target collection, reference-manager status, PDF
  attachment status, local cache status, and next human action.
- **Markdown cache manifest**: per paper — reference-manager item key and
  attachment key, collection, source PDF path, `md` path, source SHA-256,
  conversion method (`markdown` | `plaintext_fallback` | `needs_ocr`), status,
  and char count. PDFs remain in the reference manager and are not committed to
  the repo.

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
   - Cross-mode source-reading rule: see SKILL.md, Workflow overview.

