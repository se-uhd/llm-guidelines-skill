---
description: Review a paper draft (and any supplementary material) against the community LLM guidelines for empirical SE studies.
---

Use the `llm-guidelines` skill in **review mode**.

The skill's router lives at `skills/llm-guidelines/SKILL.md`; the review-mode workflow, inputs, and report template are at `skills/llm-guidelines/references/review.md`. Inputs (passed as arguments after the command, or asked for if missing): a path to the paper as `.tex` or `.pdf`, plus optional paths to supplementary material (local directories, local repositories, or public URLs such as a GitHub repo or Zenodo record). When both LaTeX source and PDF are available, prefer the LaTeX source. If no path is supplied, ask the user before proceeding. Do not modify the user's paper or supplementary material.
