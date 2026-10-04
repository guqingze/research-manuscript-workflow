## Analysis Plan Mode

Use `analysis-plan` inside the research iteration loop when the literature, a
reflection memo, internal-meeting feedback, or a reviewer suggests analyses the
project has not yet run. This mode decides what is worth running next and whether
it is even possible with the project's data; it does not run the analyses or
draft prose.

Core rule: audit availability before proposing. A proposed analysis that the
cohort or linked data cannot support is a limitation to document, not a task to
queue.

Minimum procedure:

1. Collect candidate analyses from the gap synthesis, reflection memo, meeting
   feedback, reviewer comments, and the covariate/measurement literature.
2. For each candidate, run an in-cohort/in-data availability audit: is the
   variable or assay present, at what completeness, in which subcohort, and is it
   a confounder, mediator, or collider relative to the current model? Distinguish
   "computable now from existing columns", "needs new derivation/linkage", and
   "not available in-cohort".
3. Classify each candidate by role (strengthens confounding control, orthogonal
   cross-check, mechanism, robustness/QC, descriptive) and by effort tier
   (straightforward now / intermediate needs generation or linkage / future
   research program).
4. Recommend which candidates to run this cycle, which to defer, and which to
   convert into stated limitations; keep non-auditable or speculative suggestions
   separate from the actionable queue.
5. Hand off: actionable Tier-1 items feed the repo pipeline and `analysis-refresh`;
   deferred and future items seed a Next-Steps/roadmap section for the SAP and
   eventual Discussion.
6. Stop at planning and triage. Do not run analyses or edit the SAP unless the
   user also asked for the next mode.

Default handoff document: **Planned-analyses roadmap** with these sections:

- Candidate analyses with driver/source
- In-cohort/in-data availability audit (completeness, subcohort, confounder/mediator/collider status)
- Role and effort-tier classification
- Run-now / defer / convert-to-limitation recommendation
- Non-auditable or speculative reserve (kept separate)
