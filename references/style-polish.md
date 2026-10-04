## Style Polish Mode

Use `style-polish` after `draft` or `revise` when the manuscript needs a
readability, tone, or author-voice pass before QA. This mode improves prose
quality without changing the scientific argument, results, citations, or
disclosure obligations.

Core rule: polish for clarity and author voice, not for AI-detector evasion or
to hide AI assistance. If the project or target journal requires AI-use
disclosure, preserve or flag that requirement.

Minimum procedure:

1. Establish inputs: Manuscript Draft Package or Revised Manuscript Draft
   Package, SAP/Outline Controller, gap synthesis, Analysis Refresh Report,
   literature index, author writing samples if available, target journal style
   if known, and render workflow.
2. Lock scientific content before editing. Preserve numbers, denominators,
   effect estimates, confidence intervals, p-values, endpoint definitions,
   table/figure references, citation keys, and section-level claims unless the
   user explicitly requests scientific revision through `draft` or `revise`.
3. Calibrate style from author samples when available. Treat the style profile
   as a soft guide; discipline conventions, journal instructions, and factual
   clarity override personal style preferences.
4. Run a writing-quality sweep inspired by ARS writing-quality checks:
   - replace generic high-frequency academic filler only when a more precise
     phrase is available;
   - remove throat-clearing openers and meta-commentary such as "this section
     discusses" when the section can simply make the point;
   - reduce inflated novelty or importance language not supported by the gap
     synthesis or Analysis Refresh Report;
   - avoid monotonous rule-of-three lists, repeated paragraph templates,
     synonym cycling, and overused binary contrasts;
   - control punctuation tics such as excessive em dashes, semicolons, and
     colon-list sequences;
   - vary sentence and paragraph rhythm where doing so improves readability,
     while accepting more uniform prose in procedural Methods text.
5. Preserve academic register. Do not make epidemiology, clinical, statistical,
   or methods prose conversational when precision is more important than
   rhythm. For epidemiology, clinical-epidemiology, or population-health
   manuscripts, also read `epidemiology-manuscript-discipline.md` and
   apply its section discipline, causal-language restraint, internal-language
   scrub, and phrase replacements; consult the project's epi revision-lessons
   file if one exists.
6. Maintain traceability. If a sentence becomes smoother but less obviously
   tied to a citation or output, revise again or flag it for QA rather than
   leaving a polished but unsupported claim.
7. Record risky edits separately. If polishing would require changing meaning,
   adding interpretation, deleting a caveat, or weakening a required limitation,
   leave the passage unchanged and list it as an unresolved awkward passage.
8. Produce the handoff artifact, named conceptually **Style-Polished
   Manuscript Draft Package**. This package feeds `qa`.

Default handoff artifact: **Style-Polished Manuscript Draft Package** with
these sections or metadata:

- Source draft or revised draft path
- Polished draft path and render path if available
- Author style sample status
- Style changes summary
- Preserved facts, citations, numbers, and table/figure references check
- Section word count changes
- Unresolved awkward passages
- Warnings where polishing risks changing meaning
- Disclosure or journal-style notes
