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
