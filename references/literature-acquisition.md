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
