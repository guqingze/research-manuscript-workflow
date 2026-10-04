## Gap Synthesis Mode

Contents: Key-paper evidence extraction (subagent map-reduce).

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
the evidence-extraction cache, following `evidence-extraction-contract.md`
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
checker `../scripts/verify_extract_anchors.py` over the whole cache: it decodes every
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
