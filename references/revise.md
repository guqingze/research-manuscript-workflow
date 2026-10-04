## Revise Mode

Use `revise` after a Revision Roadmap exists and the user has approved the
revision strategy. This mode applies the roadmap to the manuscript and records
what changed. It should preserve traceability from each revision to the
reviewer/editor comment it addresses.

Core rule: revise against the approved roadmap, not opportunistically.

Minimum procedure:

1. Establish revision inputs: Revision Roadmap, submitted or current Manuscript
   Draft Package or Style-Polished Manuscript Draft Package, Journal Submission
   Package if available, QA Gate Report, and any newly generated analysis or
   literature artifacts.
2. Address must-fix items first, then should-fix items, then optional items if
   appropriate. Do not silently drop any roadmap item.
3. For each revision item, record action taken, manuscript location, source
   material used, status, and whether the response letter needs explanation.
4. Keep Results revisions tied to the Analysis Refresh Report or regenerated
   outputs; keep literature revisions tied to the literature index or verified
   PDFs.
5. Produce or update response-to-reviewers draft text alongside manuscript
   changes.
6. List unresolved items and rationale. If a comment cannot be addressed without
   new analysis, new literature, or author decision, mark it as blocked.
7. Produce the handoff artifact, named conceptually **Revised Manuscript Draft
   Package**. This package feeds `style-polish` before `qa` when prose changed
   substantially or when the user requests a readability pass; otherwise it
   feeds `qa`.

Default handoff artifact: **Revised Manuscript Draft Package** with these
sections or metadata:

- Revised draft path and render path if available
- Revision log mapped to comment IDs
- Resolved, partially resolved, unresolved, and blocked items
- Response-to-reviewers draft
- Updated placeholders and limitations
- Source inputs and commands used
- Recommended next mode: `qa`
