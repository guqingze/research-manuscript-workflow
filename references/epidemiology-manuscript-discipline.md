# Epidemiology Manuscript Discipline

Read this reference during `style-polish` and `qa` when the manuscript is an
epidemiology, clinical-epidemiology, or population-health study. It encodes the
section discipline, causal-language restraint, internal-language scrubbing, and
methods-citation rules that separate journal-ready epidemiologic prose from
workflow-system prose. It supplements — it does not replace — the mode
procedures in `SKILL.md`.

Core principle: write like a careful epidemiologist, not like a workflow system.
Prose must be precise, restrained, transparent about design limits, and free of
internal project language. Preserve numeric estimates exactly unless source
outputs justify a change.

## Paper Architecture Review (run before sentence-level polishing)

Build a short reviewer-facing map first; sentence polish cannot fix a misplaced
limitation or an unsupported causal claim.

1. What is the epidemiologic question?
2. What population and design answer it?
3. What are the primary outcomes and estimands?
4. Which results answer the primary question?
5. Which Discussion claims are directly supported by those results?
6. Which claims must be softened, moved, cited, or removed?

## Section Discipline

### Abstract
- State background, objective, design, population, main measures, main results,
  and conclusion.
- Keep limitations and model caveats out of the conclusion unless the journal
  format requires a limitations sentence.
- Do not overexplain methods; cite methods in the main Methods section.
- Use "attenuated after adjustment" for statistical attenuation; avoid
  "explained by" unless carefully framed.

### Introduction
- Move from broad burden → specific gap → study objective.
- Avoid novelty inflation ("unique platform," "first ever," "deconstructs
  assumptions").
- Do not overclaim regional or ethnic generalizability.
- End with the objective and, where appropriate, prespecified hypotheses.

### Methods
- Describe the study in article-ready terms, not internal data-layer terms
  (see Internal-Language Scrub).
- Use cohort/study language (e.g. "participants underwent standardized research
  assessments"), not pipeline labels.
- Cite non-obvious statistical choices: robust/modified Poisson prevalence
  ratios, marginal standardization, g-computation, special missing-data methods.
- Separate estimands clearly: prevalence ratios (modified Poisson); adjusted
  prevalence and risk differences (standardization); prediction curves (the
  specified prediction model).

### Results
- Report estimates, uncertainty intervals, p-values where used, and observed
  patterns — nothing else.
- No interpretation, apology, causal caution, or limitations in Results.
- Move "should not be interpreted as…" sentences to Discussion.
- Do not say "this confirms," "this proves," or "driven by."
- If estimates reverse after adjustment, report the reversal numerically without
  editorial commentary.

### Discussion
- First paragraph: principal findings without repeating every number.
- Interpret adjusted contrasts, standardization, and residual heterogeneity
  here, not in Results.
- Cross-sectional findings require restrained language ("associated with,"
  "attenuated after adjustment," "consistent with," "may reflect"). Avoid
  "caused by," "mediated by," "explained by," "protective," "driven by" unless
  the design supports it.
- Put model-dependent caveats, residual confounding, and missing etiologic
  covariates in limitations. Keep future-work language specific and short.

## Causal-Language Restraint

Match wording to design. In cross-sectional / associational designs, scan for
and challenge: `explained by`, `driven by`, `protective`, `causal`, `caused by`,
`mediated by`, `confirms`, `proves`. Each must be justified by the design or
rewritten.

## Internal-Language Scrub

Remove data-layer / pipeline / AI-workflow vocabulary from article text. These
tokens are illustrative — adapt to the project's own build vocabulary (record
the project set in the repo's epi revision-lessons file):

- pipeline/data labels: "core table," "core phenotype," "linked_ready,"
  "output layer," "manuscript-facing," "generated artifact," "latest models"
- instructional verbs in prose: "write," "output," "generated" (allowed only
  when describing reproducibility materials outside the article text)
- placeholders such as `[Insert Figure 1 here]` may remain in Markdown drafts
  when the document build removes them from Word output.

Also avoid AI-like prose: repeated mechanical transitions ("Furthermore,"
"Moreover," "Importantly"); inflated adjectives ("highly," "substantially")
without numeric support; generic closers ("future studies are needed") that do
not specify what remains unknown. "Humanizing" means removing template-like
prose while preserving epidemiologic restraint — not adding conversational
language.

## Phrase Replacements

- "explained by" → "attenuated after adjustment for" / "accounted for by
  measured …"
- "driven by" → "corresponded with" / "was associated with"
- "unique platform" → "relevant setting" / "single cohort and analytic
  framework"
- "latest models" → "fully adjusted models" / the exact model name
- "health-screening data" → the study-specific assessment description
- "should not be interpreted as…" in Results → delete; move the caution to
  Discussion
- reserve code variable names (e.g. `race`) for code/data dictionaries; use
  "ethnicity" in manuscript prose

## Statistical-Methods Citation Checks

- Modified Poisson with robust SEs: cite foundational robust Poisson and, for
  cross-sectional prevalence-ratio studies, a prevalence-ratio methods paper.
- Logistic marginal standardization: cite a paper on predicted probabilities,
  marginal standardization, target populations, or g-computation.
- The citation must support the chosen estimand and target population — do not
  cite a methods paper only because it is famous.
- Number references by first appearance for Vancouver-style drafts; renumber
  after any citation insertion.

## Results Examples

Acceptable in Results:
- "The prevalence ratio was 1.50 (95% CI, 1.42 to 1.59)."
- "After adjustment for BMI, prevalence ratios were close to the null."
- "The risk difference changed from +14.9 to −3.8 percentage points."

Move to Discussion:
- "This should not be interpreted as biological protection."
- "These findings suggest residual confounding."
- "This confirms robustness."
- "This is likely driven by unmeasured factors."

## Pre-Handoff Checks (epidemiology)

1. Section discipline: interpretation and limitations absent from Results.
2. Internal language: workflow/data-layer phrases removed from prose.
3. Causal language: wording matches the study design.
4. Citation support: methods and literature claims cited through canonical
   project sources.
5. Numbering: numeric references ordered by first appearance.
6. Consistency: counts, estimates, and model names match current outputs.

## Per-Repo Revision Lessons

Treat repeated user corrections during revision as durable, project-specific
writing rules. Keep them in a repo file (e.g.
`docs/manuscript/epi_revision_lessons.md`) — the project's build vocabulary,
prohibited phrases, and preferred replacements — and consult it during
`style-polish` and `qa`. This file is the running memory this generic reference
deliberately does not hard-code.
