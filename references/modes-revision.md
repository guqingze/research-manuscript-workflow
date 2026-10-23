# Revision and Packaging

## Revision Plan Mode

Use `revision-plan` when editor, reviewer or major coauthor comments arrive. It
plans; it does not edit the manuscript.

Core rule: no comment left behind.

Split comments into atomic items, keeping the raw text, source and any
ambiguity. Classify severity and priority (must-fix, should-fix, consider),
promoting items raised by the editor or several reviewers. Map each item to
sections, displays, analyses, references and response needs, including new
analysis or literature work. Flag contradictory requests for the user. Propose a
revision order and a response-letter skeleton, and get the user's approval
before `revise`.

## Revise Mode

Use `revise` once the user has approved the Revision Roadmap.

Core rule: revise against the approved roadmap, not opportunistically.

Work must-fix items first and silently drop none. For each item, log the action,
location, source and status. Tie Results changes to regenerated outputs and
literature changes to verified records. Draft the responses alongside the
changes. Mark items that need new analysis, literature or an author decision as
blocked. Recommend the next modes: `style-polish` if prose changed
substantially, then `qa` before any resubmission package.

## Package Mode

Use `package` to assemble a submission once QA has passed (or its warnings are
accepted): a first submission, a resubmission after revision, or a final
handoff note.

Core rule: packaging does not change content. Route content problems back to
`draft`, `revise` or `qa` rather than fixing them during formatting.

- **First submission**: apply the target journal's requirements (word limits,
  abstract structure, reference style, displays, reporting checklist, required
  statements including AI disclosure, supplement rules); render the requested
  formats; draft the cover letter and statements; produce a checklist of
  blockers.
- **Resubmission**: also finalize the point-by-point response (each comment,
  response, change and location), clean and tracked versions when available,
  and confirm every roadmap item is resolved or explicitly justified.
- **Handoff note**: final paths, commands run, outputs changed, open
  limitations and next human actions. Submission itself happens outside this
  workflow.

## Artifact Contracts

- **Revision Roadmap**: decision context; atomic comments with raw text, source,
  severity, priority, target and action; cross-reviewer patterns; new
  analysis/literature needs; revision order; response skeleton.
- **Revised Draft Package**: revised paths; revision log by comment ID;
  resolved/partial/unresolved/blocked items; response draft; inputs and
  commands.
- **Submission or Response Package**: target journal and article type; final
  manuscript, display and supplement paths; cover letter; required statements;
  reference-style status; checklist and blockers; for resubmission, the
  response letter, clean/tracked paths and comment-resolution checklist;
  render status.
