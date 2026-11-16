# Defensive-Writing Discipline

Read this reference in `draft`, `reflect`, `style-polish`, `qa` and `revise`.
It applies to every discipline; epidemiology specifics live in
`references/epidemiology-manuscript-discipline.md`.

Defensive writing is prose that argues with an imagined reviewer: caveats bolted
onto results, denials of claims nobody made, the same limitation repeated in
every section, hedges stacked on hedges. Newer LLMs add it heavily, especially
when prompted to anticipate reviewers or run repeated self-review. The added
qualifications are mostly redundant, read as uncertainty, and bury the finding.

Core rule: **a caveat is deleted by default and kept only when it passes the
keep test.** Reporting facts are not caveats and always stay.

## Keep Test

Keep a caveat only if all three hold:

1. **Specific.** It names a concrete constraint from this study's design, data
   or analysis ("BMI was self-reported"; "92% of participants were Chinese"),
   not a generic one ("residual confounding cannot be ruled out", "interpret
   with caution", "further studies are needed").
2. **New.** The constraint is not already stated elsewhere in the paper. The
   only allowed repeat is in text read on its own: the Abstract conclusion,
   and there as a single design phrase ("In this cross-sectional study, X was
   associated with Y").
3. **Needed here.** A competent reader would misread this particular sentence
   without it. A constraint that matters but not at this spot goes once to the
   Discussion or Limitations.

A caveat that fails is deleted. Do not list it for review, and do not keep a
denial ("this does not imply…") because a misreading is conceivable.

## Not Caveats: Always Keep

- Estimates, intervals, p-values, denominators, missing data, sparse events,
  failed or non-converged models.
- Analysis labels (primary, sensitivity, exploratory, post hoc), stated once in
  Methods or the display, not repeated in every Results sentence.
- Design-matched wording: "was associated with", "attenuated after
  adjustment", "consistent with". A single "may" is fine where an
  interpretation is genuinely uncertain; stacked hedges are not.
- Null, discordant and unfavourable results themselves. Anti-defensive writing
  states results plainly; it never hides them.

## Placement

- **Results** report. No interpretation, caution, apology or explanation of why
  a result is null.
- **Discussion** interprets. Each paragraph opens with its interpretation,
  stated without a hedge. An alternative explanation belongs here when it
  changes how a finding should be read; write it as interpretation, once.
- **Limitations** explain constraints on interpretation. At most five items by
  default (the project or journal can change this), ranked by how much each
  changes the reading of the results. For multi-modality studies (for example,
  combining imaging, body composition, omics, health records and genetics),
  group constraints into one cohesive paragraph organised by modality, each
  constraint with its direction of bias when known, rather than scattering caveats into
  earlier Discussion paragraphs or cutting a distinct modality's material
  constraint to meet a flat count. Merge related items; drop
  or move minor ones to the supplement. State the direction of bias when it is
  known; when it is not, name the limitation and stop. If more than five
  materially change interpretation, QA warns and the author chooses.
- **Methods** state scope and final design choices as positive fact ("Analyses
  were cross-sectional"; "Panels were refitted on the full cohort with
  200-sample participant-level bootstrap optimism correction"), never as an
  audit confession.
- **Abstract, Introduction, contribution sentences** carry no self-weakening
  ("we attempt to", "preliminary", "only").
- **Pending multi-stage components** (when drafting before an external cohort
  or genetic arm finishes) stay strictly quarantined in isolated `[PENDING: …]`
  blocks (their own Results subsection, Discussion paragraph and Methods
  subsection). Completed sections carry no `[PENDING: …]` markers and zero
  disclaimers about what has not yet been run.

## Upstream Guard: Audit Provenance ≠ Article Prose

Planning ledgers (`sap.md`, `outline.md`, `results.md`, `reflection.md`) record
internal governance: negative boundary rules ("not histological fibrosis", "do
not claim causality", "conditional bootstrap excludes retraining variance") and
dated iteration history ("after inspecting the initial split, we refitted…").

- **Negative guardrails constrain what claims may be made; they are never
  copied into prose as negative denials.** Translate a negative boundary into
  exact positive terminology once ("elevated liver stiffness (LSM ≥8.0 kPa)",
  "referral-threshold discordance") instead of repeating what a measure is *not*
  across Results and Discussion (a single measurement-validity scope statement,
  with its direction of bias, stays once in Methods or Limitations under the
  keep test).
- **Project chronology stays in Methods or repository records, not Results or
  Discussion.** Report one canonical estimator per question in the main text;
  do not narrate superseded splits, bug fixes or internal review rounds as
  story beats.

## Patterns to Cut

| Pattern | Example | Action |
| --- | --- | --- |
| Escape-clause tail | "…; however, this does not necessarily imply causation." | Delete |
| Denial of an unmade claim | "We do not claim that…", "This should not be interpreted as…" | Delete or state the positive scope |
| Null-result self-rescue in Results | "…possibly owing to limited power." | Delete; power belongs in Methods or one Limitations item |
| Stacked hedges | "may potentially suggest a possible…" | One hedge or none |
| Repeated or generic caveat | "residual confounding cannot be excluded" in three sections; "further studies are needed" | Once in Limitations, specific, or delete |
| Reader instructions | "It should be noted that", "To be clear", "Importantly, caution is warranted" | Delete the wrapper |
| Self-grading adjectives | "only a modest", "limited", "unfortunately" | Give the number and its comparison |
| Concession-only paragraph | A Discussion paragraph that concedes without interpreting | Delete; move any specific constraint to Limitations |

## Overclaim Guard

De-hedging must not change what the evidence supports. After cutting:

- no association becomes causal ("driven by", "protective", "explained by");
- "no clear association" never becomes "no association";
- no estimate, interval, denominator or analysis label is lost;
- no null or discordant result disappears.

## Rule Zero

When drafting, polishing or revising, add no caveat that would fail the keep
test. Answer an ambiguity with a precise definition, not a disclaimer. A small
requested change gets a small change, not a protective paragraph. Reviewer-style
critique (`pre-submission-review`, `gap-synthesis` stress tests) informs the
analysis and the plan; it does not become manuscript caveats unless a revision
roadmap the user approved says so.

## Review Aid

These patterns help find candidates; a match is not a verdict.

```bash
grep -nEi "however|nevertheless|that said|with caution|caveat|should be noted|worth noting|\
to be clear|not necessarily|does not (imply|mean|establish)|we do not claim|should not be (interpreted|construed)|\
cannot be (ruled out|excluded)|further (research|studies)|may (potentially|possibly)|might potentially|\
possibly (due|owing)|(attempt|try) to|preliminary|unfortunately" manuscript.md
```

## Examples

| Before | After |
| --- | --- |
| "Higher BMI was associated with steatosis (PR 1.50, 95% CI 1.42–1.59); however, this does not necessarily imply a causal relationship and should be interpreted with caution." | "Higher BMI was associated with steatosis (PR 1.50, 95% CI 1.42–1.59)." |
| "No association was observed for statin use (PR 0.97, 0.85–1.10), possibly owing to limited power." | "Statin use was not clearly associated with steatosis (PR 0.97, 0.85–1.10)." |
| "These findings may potentially suggest a possible role of insulin resistance." | "These findings are consistent with a role for insulin resistance." |
| Limitations: "First, residual confounding cannot be excluded. Second, causality cannot be inferred. Third, generalizability may be limited. Fourth, further studies are needed." | "Alcohol intake was self-reported and likely under-reported, which would bias associations with steatosis toward the null. The cohort was 92% Chinese, so absolute prevalences may not transfer to other ancestries." |
| "In a sensitivity analysis excluding diabetes, the association attenuated (PR 1.21, 1.05–1.39)." | Keep as written: a discordant sensitivity result is a reporting fact. |
