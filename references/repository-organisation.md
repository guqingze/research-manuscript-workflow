# Repository organisation

Use for `setup`, a broad workflow audit, or an authorised structural refactor.
The goal is that a researcher can find the current manuscript, a meeting package
and the command for a task without reading every script.

## Ownership before folders

For each artifact, identify its role, canonical editable path, inputs, generated
exports, status and owner/builder where useful. Keep this in the existing README
or workflow map; add a catalog only when the number of files warrants one.

- Scientific controllers, results, reflection and manuscript prose have distinct
  jobs. Retain useful existing boundaries instead of renaming everything.
- Each editable artifact has one home. Repeated Markdown copies are not a source
  and an output merely because their folders have those names.
- A generated Word/PDF version can coexist with canonical Markdown. Label which
  is editable and which command regenerates the other format.
- A submitted review snapshot or presented original is historical evidence.
  Preserve it; do not replace it with current content while repairing navigation.
- Results and input availability remain separate from local build success.

## Meeting packages

Choose one canonical location for a meeting's deck, presenter notes and selected display
assets. Either a docs-based package or a curated versioned output package can
work; follow the user's choice and repository conventions. Example:

```text
outputs/presentations/<date>_<meeting>/
  README.md                 Status, provenance and regeneration commands
  deck_plan.md              Approved storyline, when needed before production
  deck.md                   Editable slide text and presenter notes
  research_plan_note.md     Optional requested companion
  assets/tables/            Generated display tables
  assets/figures/           Generated display figures
```

Meeting records have a different role from presenter notes. Preserve dated
meeting notes, transcripts and presented originals in the project's existing
meeting-record location, and link them from the package/index rather than
copying them. Reflection digests decisions, objections and requested analyses
against results and literature, linking the source meeting and the current
research action register. Accepted decisions feed the plan and next analysis or
deck; the next meeting supplies further feedback. Keep historical records intact
and current action status in its declared owner.

Do not create each file or subfolder until it has a use. Use relative links for
assets that travel with the package. Distinguish portable display links from
repository-only provenance links. Reuse existing results; do not copy full model
workbenches or participant tables into a deck folder. A short provenance list or
asset manifest should link displayed results to their authoritative sources.

If the user wants a Markdown package, produce that format; do not silently add a
PPTX build. If a lifecycle folder points to a package elsewhere, keep an index or
link there, not another editable deck. Explicit exports may create copies, but
label them as exports and avoid treating both copies as current sources.

Selected generated assets can be versioned when the user/repository wants
reviewable meeting history. Use narrow Git exceptions or a curated allowlist,
and inspect what becomes eligible for tracking. Keep source data and bulky
working outputs ignored. Existing tracked files under ignored folders still
need preservation.

## Script navigation

Group by the researcher's task, not just language or filename prefix. Depending
on scale, useful groups include analysis runners, manuscript builders, literature
maintenance, presentation assets, review exports and secure-environment handoffs.
Avoid adding empty groups or moving domain analysis modules out of an already
clear analysis tree merely to centralise everything under scripts.

The script index should answer: what do I run, what does it read/write, does it
fit models or only render, and is it current? Classify less visible files as
helpers, optional tools, dated analyses, historical recipes or compatibility
entry points. Historical code can still be an imported dependency; inspect the
call graph before retiring or deleting it.

For a large inventory, a small CSV with `path`, `purpose`, `status` and
`previous_path` is enough. Keep frequent commands in a concise README. Do not
replace a cluttered root with dozens of unexplained folders or automatic aliases
at every old path. Retain compatibility entry points where real callers need
them; otherwise update live callers and provide a migration map for dated notes.

## Authorised migration sequence

1. Save any approved work plan first. Record dirty files in all affected repos;
   preserve unrelated work, including pre-existing edits to the workflow skill.
2. Inventory tracked and relevant ignored artifacts, duplicate candidates,
   entry points, imports, subprocess calls, templates, tests, manifests and
   current documentation. Compare duplicate content before choosing a source.
3. State the proposed ownership map and scope. A user-authorised organisation
   task can proceed without a second approval for routine reversible moves.
4. Save a baseline for scientific text, data/result hashes and key generated
   artifacts. Move with an explicit old-to-new mapping. Update runtime root
   detection, imports, command builders and maintained navigation together.
5. Preserve dated evidence. Repair live navigation; let historical command
   receipts resolve through the migration map instead of rewriting their claims.
6. Rebuild affected products in fresh directories. Never delete an authored or
   versioned package to test regeneration. Verify numerical/display equivalence,
   links, script discovery and relevant failure/overwrite guards.
7. Report new entry points, changes, validation evidence and any unavailable
   checks. Do not claim that a layout refactor validates scientific findings.

Change the reusable skill only for lessons that apply across projects. Keep
specific study names, dates, paths, counts and current scientific decisions in
the project repository.
