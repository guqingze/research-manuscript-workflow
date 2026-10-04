## Pre-Submission Review Mode

Use `pre-submission-review` after `qa` and before `journal-package` when the
user wants reviewer-style critique before first submission. This mode evaluates
manuscript merit and likely reviewer concerns; it does not replace QA and does
not rewrite the manuscript unless the user asks for a follow-on revision.

Core rule: critique the manuscript as a manuscript, not as a data audit.

Minimum procedure:

1. Establish review inputs: QA-passed Manuscript Draft Package or
   Style-Polished Manuscript Draft Package, QA Gate Report, SAP/Outline
   Controller, gap synthesis, Analysis Refresh Report, target journal or
   article type if known, and any author priorities.
2. Assess journal fit and contribution: audience, novelty, scope, article type,
   and whether the stated contribution follows from the literature gap and
   results.
3. Assess manuscript argument: Introduction problem framing, Results logic,
   Discussion interpretation, limitation handling, and whether the strongest
   claims are defensible.
4. Assess methods and reporting clarity at a manuscript level. Do not rerun
   analyses; instead flag unclear design, missing reporting, or weak explanation
   that a reviewer would notice.
5. Identify strongest likely reviewer objections, including methodology,
   novelty, generalizability, causal overreach, endpoint definitions, analysis
   hierarchy, and missing literature comparisons.
6. Prioritize recommended fixes as must-fix, should-fix, or optional. Keep
   factual integrity issues linked back to the QA Gate Report.
7. Produce the handoff document, named conceptually **Pre-Submission Review
   Report**. This report can feed `draft` for targeted improvements or
   `journal-package` if only minor warnings remain.

Default handoff document: **Pre-Submission Review Report** with these sections:

- Journal fit and contribution
- Major strengths
- Must-fix issues before submission
- Should-fix issues
- Optional improvements
- Likely reviewer objections
- Recommended next mode: `draft`, `qa`, or `journal-package`
