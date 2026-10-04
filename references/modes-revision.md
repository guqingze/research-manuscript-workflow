# Revision

## Revision Plan Mode

Use `revision-plan` after external editor/reviewer comments or major coauthor
comments arrive. This mode parses unstructured feedback into an actionable
roadmap. It should not revise the manuscript directly.

Core rule: no comment left behind.

Minimum procedure:

1. Collect reviewer/editor/coauthor comments, decision letter if available, the
   submitted manuscript or Journal Submission Package, and any journal deadline.
2. Parse comments into atomic items. Split comments that contain multiple
   actionable requests.
3. Preserve reviewer intent: keep raw comment text, reviewer/editor source,
   paraphrased summary, and ambiguity flags.
4. Classify each item as major, minor, editorial, positive, or unclear. Assign
   priority: must-fix, should-fix, or consider. Promote items raised by the
   editor or multiple reviewers.
5. Map each item to manuscript sections, tables, figures, analyses, references,
   response-letter needs, and whether new analysis or literature work is
   required.
6. Produce a suggested revision order and response-letter skeleton. Flag
   contradictory reviewer requests for user decision.
7. Produce the handoff document, named conceptually **Revision Roadmap**. This
   report feeds `revise`.

Default handoff document: **Revision Roadmap** with these sections:

- Decision and revision context
- Parsed comment inventory
- Must-fix / should-fix / consider tables
- Cross-reviewer patterns
- Section/action map
- New analysis or literature needs
- Suggested revision order
- Response-letter skeleton

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

## Response Package Mode

Use `response-package` after a revised manuscript has passed QA. This mode
prepares the resubmission bundle. It is distinct from first-submission
`journal-package` because it must include point-by-point responses and revision
traceability.

Core rule: every reviewer/editor item in the Revision Roadmap must be accounted
for in the response package.

Minimum procedure:

1. Establish response inputs: Revised Manuscript Draft Package, Revision
   Roadmap, QA Gate Report, target journal/resubmission requirements, and any
   requested clean/tracked manuscript files.
2. Finalize point-by-point response letter: quote or summarize each comment,
   state response, state changes made, and list manuscript locations.
3. Assemble clean revised manuscript and tracked/change-log version when
   available or requested.
4. Update cover letter/editor note, required statements, supplement list, and
   figure/table files as needed.
5. Check that all must-fix items are resolved or explicitly justified.
6. Produce the handoff artifact, named conceptually **Response Package**.

Default handoff artifact: **Response Package** with these sections or metadata:

- Revised manuscript file paths
- Clean/tracked/change-log file paths when available
- Response-to-reviewers letter
- Editor cover letter or resubmission note
- Comment-resolution checklist
- Updated QA Gate Report path
- Journal resubmission checklist and blockers

## Artifact Contracts

- **Revision Roadmap**: decision context, parsed comment inventory, raw comment
  text, reviewer/editor source, severity, priority, target section, suggested
  action, cross-reviewer patterns, new analysis/literature needs, suggested
  revision order, and response-letter skeleton.
- **Response Package**: revised manuscript paths, clean/tracked/change-log paths
  when available, response-to-reviewers letter, editor cover letter or
  resubmission note, comment-resolution checklist, updated QA Gate Report path,
  and journal resubmission checklist.
- **Handoff note**: final artifact paths, commands run, outputs changed, known
  limitations, and next human actions.

## Post-review revision cycle and handoff

13. **Plan revisions after external comments**
   - Use `revision-plan` only after editor, reviewer, or major coauthor comments are received.
   - Parse every comment, preserve reviewer intent, prioritize actions, map comments to manuscript sections, and create a response-letter skeleton.

14. **Revise, polish, and re-QA**
   - Use `revise` to apply the approved Revision Roadmap and produce a Revised Manuscript Draft Package.
   - Use `style-polish` after revision when prose changed substantially or the user requests readability calibration.
   - Return to `qa` after revision or style polishing before any resubmission package.

15. **Prepare response package**
   - Use `response-package` after the revised manuscript passes QA.
   - Assemble revised files, response-to-reviewers letter, editor note, comment-resolution checklist, and resubmission checklist.

16. **Final handoff/archive**
   - Use `handoff` for a concise status/archive note after Journal Submission Package or Response Package creation.
   - Record final artifact paths, commands run, outputs changed, unresolved limitations, and next human actions.
