---
description: Review a paper draft (and any supplementary material) against the community LLM guidelines for empirical SE studies.
---

Review a paper against the community LLM reporting guidelines.

Use the `llm-guidelines` skill in **review mode**: classify the study type, check the draft against each of the eight guidelines, and write `llm-guidelines-report.md` in the working directory.

Inputs (passed as arguments after the command, or asked for if missing): a path to the paper as `.tex` or `.pdf`, plus optional paths to supplementary material (local directories, local repositories, or public URLs such as a GitHub repo or Zenodo record). When both LaTeX source and PDF are available, prefer the LaTeX source. If no path is supplied, ask the user before proceeding.

The skill workflow, inputs, and report template live in the bundled `SKILL.md`. Do not modify the user's paper or supplementary material.
