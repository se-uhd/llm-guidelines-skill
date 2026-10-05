# Review Mode

This file is loaded by `../SKILL.md` when the user wants a concrete draft assessed against the guidelines (slash command `/llm-guidelines:review`, or when the user names a paper / hands a path to `.tex` or `.pdf` / asks to check / audit / review a draft). For the audience, tone, mode-selection rules, shared constraints, and full file indices, see [`../SKILL.md`](../SKILL.md).

## When to use

Stay in review mode when the user:

1. Asks to check a paper (or paper plus supplementary material) against the LLM reporting guidelines.
2. Is drafting the methodology, results, or limitations of an empirical study involving an LLM and wants reporting suggestions on a concrete draft.
3. Is reviewing such a paper and asks for clarifying questions to consider.

If the user is still planning a study or asking conceptual questions, switch to explore mode and follow [`./explore.md`](./explore.md).

## Inputs the user will provide

The user typically provides one or more of:

- A path to the paper. Both forms are supported:
  - A LaTeX source file (`.tex`): read it directly and follow `\input{}`/`\include{}` for files inside the project tree. A flattened `.tex` works the same way.
  - A PDF (`.pdf`): extract text using whatever tool is available in the environment (e.g., `pdftotext`, `mutool draw -F txt`, or a Python library). If no extractor is available, tell the user which one to install rather than failing silently.
  When both are available, prefer the LaTeX source: it lets you spot LaTeX-specific artifacts (e.g., commented-out disclosures, `\todo{}` notes) that get lost in the PDF.
- One or more pointers to supplementary material with prompts, traces, datasets, code, or replication packages. Each can be a local directory, a local repository, or a public URL (e.g., a GitHub repo or a Zenodo record). For URLs, **clone or download the artifact locally and read its files directly**; do not characterise the artifact from a `WebFetch` summary of its landing page (see workflow step 1).
- Optionally, a description of sharing restrictions that apply to the study (e.g., an NDA, an industry-partner agreement, an embargo, or ethics-board conditions), either stated in the request or as a path to a document listing what cannot be shared. See workflow step 2.

If no paper path is supplied, ask the user for one before proceeding. Supplementary paths are optional: if the user omits them, search the paper itself for links to replication packages, datasets, prompts, traces, or code (see workflow step 1).

## Workflow

1. **Resolve inputs.** For a LaTeX paper, read the entry-point file and follow `\input{}`/`\include{}` for files inside the project tree. For a PDF paper, extract text with a tool available in the environment (`pdftotext`, `mutool`, `pdfminer.six`, etc.). For supplementary directories, start with the top-level `README*` or `INDEX*` and the directory layout to orient yourself, then read whatever the layout points at as relevant: prompts, traces, datasets, code, replication scripts. Drill deeper only where the structure suggests evidence for a guideline; do not try to read every file in a large package.

    **Search the paper for supplementary-material links** even when the user has supplied supplementary paths, and especially when they have not. Look across the abstract, introduction, methodology, data-availability / artifact-availability statements, footnotes, acknowledgments, appendices, and the references list for URLs that point to replication packages, datasets, code, prompts, or traces. Common hosts include `github.com`, `gitlab.com`, `zenodo.org`, `figshare.com`, `huggingface.co`, `anonymous.4open.science`, and institutional archives; also check for DOIs (`doi.org/10.5281/...`) and any sentence containing phrases such as "available at", "we release", "we open-source", "replication package", "artifact", or "supplementary material". Record every link you find and the surrounding sentence. If the paper claims to release something but does not anchor the claim to a concrete URL, note the unanchored claim too. The findings populate the *Supplementary material availability* section of the report (see template).

    **Fetch every supplementary URL locally and inspect the actual files.** Confirming that a link resolves is necessary but **not sufficient**. For each URL found in the paper or supplied by the user, materialise it on disk before saying anything about its contents:

    - **Git repositories** (`github.com`, `gitlab.com`, `bitbucket.org`, `anonymous.4open.science`, institutional GitLabs): `git clone --depth 1 <url> <local-path>`. If the default branch fails because the URL points at a specific branch or tag, retry with `--branch`. For GitHub specifically, `gh repo clone` works too when the `gh` CLI is available.
    - **Zenodo / Figshare / Hugging Face datasets / institutional archives**: download the archive (`curl -L -O`, `wget`, or the host's API) and extract it (`unzip`, `tar -xzf`). Hugging Face repos can also be cloned via `git clone https://huggingface.co/<owner>/<repo>` (LFS may be required).
    - **arXiv source tarballs** (when the paper is on arXiv): `curl -sL -o source.tar.gz https://arxiv.org/src/<id>` then `tar -xzf source.tar.gz`. This often contains the LaTeX source plus prompt/figure files not visible in the PDF.
    - **Direct file URLs** (PDFs, JSON datasets, CSVs): `curl -L -O` and inspect with the appropriate tool.

    Once the artifact is on disk, read it with `Read`, `Bash` (e.g., `ls`, `find`, `wc -l`, `grep`), or the language-appropriate tool. **Cite specific paths in the report**, the same way you cite paper sections — e.g., "`prompts/judge_prompt.txt:1-40`" for a text file with meaningful line ranges, or just "`benchmark/python_api_usage/instance_0042.json`" (or the path plus a key, e.g., `... → .golden_completion`) for a binary/structured data file where line ranges do not apply. A finding such as "the repo includes prompts" must be backed by a file that was actually read, not by a model rendering of the repo's GitHub landing page.

    **Do not use `WebFetch` to characterise a code repository, dataset archive, or replication package.** `WebFetch` summarises a rendered HTML page (typically the host's directory-listing UI), not the files inside. Relying on it produces hedged language like *"the repo appears to include …"*, which is exactly the failure this step is designed to prevent. `WebFetch` remains appropriate for: (a) confirming that a URL resolves at all; (b) reading a hosted blog post, paper landing page, or other genuinely web-only content that has no underlying file to fetch.

    **When fetching genuinely fails**, say so explicitly in the report — name the URL, the failure mode (404, archive corrupt, repo private, auth/approval wall, rate limit, LFS pull failed, network blocked), and what is therefore unverified. Do not paper over the gap with a `WebFetch` summary.

2. **Establish sharing restrictions.** Several guidelines ask authors to publish prompts, traces, datasets, or code. When parts of a study are under an NDA, an industry-partner agreement, an embargo, or ethics-board conditions, those recommendations do not apply as written, and a report that ignores this is mostly noise. Settle which restrictions apply before the per-guideline assessment:

    1. **Look for signs of restrictions** in the inputs you already read. In the paper, check data-availability and artifact-availability statements, threats to validity, acknowledgments, and footnotes for terms such as "NDA", "non-disclosure", "confidential", "proprietary", "industry partner", "industrial collaboration", "embargo", "cannot be shared", "not publicly available", "available upon request", "anonymized", or "ethics approval". In the supplementary material, check `README*`, `LICENSE*`, `NOTICE*`, data-availability or data-management files, and project notes (e.g., `CLAUDE.md`, `AGENTS.md`, `memory/`). Also take into account anything the user said in the request.
    2. **If you find no sign and the user said nothing about restrictions**, ask the user one short question before continuing: whether any part of the study (paper, data, prompts, traces, code, or model access) is under an NDA, embargo, or other sharing restriction. If the user says no, proceed with the guidelines as written. If you cannot ask (e.g., a non-interactive run), proceed as if there are no restrictions and state that assumption in the report's *Sharing restrictions* section.
    3. **If restrictions apply**, look for a document that lists what is protected: a section in the paper or supplementary `README`, a data-management plan, an NDA summary, an artifact-availability note, or project notes. Record the source of each restriction. A statement that names only some protected elements (e.g., "the defect reports cannot be shared") is a partial list: record what it names, and ask in sub-step 4 only about what it leaves open.
    4. **If restrictions apply but no such list exists, or the list leaves elements open**, ask the user to provide one, either in the chat or as a path to a document. Name the elements whose status is unclear, including ones derived from protected material (e.g., filled prompts or model outputs that contain protected text). Ask what is protected (e.g., source code, datasets, prompts, model outputs or traces, model identity or configuration, participant data) and to what degree (cannot be shared at all; shareable only as summaries, excerpts, or anonymized samples; shareable after an embargo date; shareable on request). Wait for the answer before the per-guideline assessment (step 5). If you cannot ask, proceed with the restrictions you could record, and state in the *Sharing restrictions* section that the list may be incomplete.
    5. **Record the restrictions** in the report's *Sharing restrictions* section, each with its source (a quote with location, a file path, or "stated by the user in this session") and the elements it covers. Restrictions are the user's statement of fact; do not second-guess them, but do not invent restrictions the user did not state either. Where a restriction's wording leaves it unclear whether a reduced form (an excerpt, a summary, an anonymized sample) may be shared, ask; if you cannot ask, read the restriction strictly and say so.

    The restrictions recorded here change how step 5 phrases each gap; they do not change what you look for in the paper.

3. **Identify the study type(s).** Use the files under `./study-types/` to classify the study. A single paper can fall under multiple types (e.g., a new tool that also benchmarks LLMs). Note the classification at the top of the report.

4. **Consult [`./scope.md`](./scope.md)** to confirm the work is in scope. The guidelines cover LLM use that materially affects the research method or its outcomes; peripheral uses (proofreading, spell-checking, translation, writing assistance) are explicitly out of scope, even though venue policies such as the ACM Policy on Authorship may still require an author-writing disclosure separately.

5. **Per-guideline assessment.** For each of the eight guidelines listed in [`../SKILL.md`](../SKILL.md), load the corresponding file in `./guidelines/` on demand, then for that guideline produce:
   - `Status`: one of `covered`, `partial`, `not found`, or `not applicable` (with a one-line reason if N/A).
   - `Evidence`: 1 to 3 items, each a **verbatim quote** from the paper or supplementary material (or, for binary/structured data files, a direct file-or-key pointer), with its source location (e.g., `_s4_evaluation.tex:34` or `benchmark/python/api_usage/instance_0042.json`). Do not paraphrase. See the *Constraints* section for the full grounding rule.
   - `Gaps`: bullet list of specific missing items (`must`/`should`-level), each phrased as an author-facing suggestion (e.g., "Consider naming the exact model version and access date in the methodology."). Each gap's premise must be supported either by an Evidence item above or by a verified absence (state what you searched for and how, e.g., "`grep -i 'experiment date' _s*.tex` returned no hit").
   - `Pointers`: links to the relevant section(s) of the consulted guideline file.

   Apply the RFC 2119 levels from the guideline text: **must** items become "required for full reporting"; **should** items become "recommended". Do not invent severity levels not present in the guideline.

   **Apply the sharing restrictions from step 2.** Before finalizing each guideline's gaps, compare every gap against the recorded restrictions:
   - If a gap asks to publish or share an element that a restriction covers (e.g., "publish all prompts" when prompts are under NDA), replace it with the alternative the guideline itself names for restricted settings, such as publishing summaries or representative examples, anonymizing identifiers and replacing proprietary code with placeholders, acknowledging the non-disclosed components as a reproducibility limitation, or describing data governance. Use the severity the guideline gives to that alternative (the checklist marks these items with a `[restricted-sharing]` tag), not the severity of the original recommendation. Prefix the adjusted gap with *Adjusted for restriction:* and name the restriction.
   - If the restriction makes a gap impossible to address and the guideline offers no alternative, drop the gap from the guideline's block and list it under *Recommendations not applicable under these restrictions* in the *Sharing restrictions* section, with the restriction that blocks it. Do not drop gaps silently.
   - If every gap of a guideline is dropped (none kept or adjusted), set its status to `not applicable` with the restriction as the one-line reason. An adjusted gap stays in the guideline it came from, even if the alternative is about limitations.
   - Restrictions on *sharing* do not remove requirements on *reporting* in the paper. For example, an NDA on the dataset does not remove the need to name the model version or describe the prompting strategy, unless the restriction explicitly covers that information too.

6. **Cross-cutting concerns.** After the per-guideline pass, scan [`./checklist.md`](./checklist.md) for any item that did not surface during step 5 and add it to a `Checklist gaps` section if missing. Apply the step-2 restrictions to these items the same way. If restrictions apply, also check the checklist's `[restricted-sharing]` items, which become applicable.

7. **Write the report.** Save the assessment as `llm-guidelines-report.md` in the user's current working directory **and** print the same content to the console. Use the [report template](#report-template) below.

    Then try to resolve the bundled Markdown linter. Check these locations in order and use the first `lint_markdown.py` that exists:

    1. `${CLAUDE_SKILL_DIR}/scripts/lint_markdown.py`, when `${CLAUDE_SKILL_DIR}` is set.
    2. A checked-out plugin path under the current directory or one of its parents: `plugins/llm-guidelines/skills/llm-guidelines/scripts/lint_markdown.py`.
    3. The Codex plugin cache under `${CODEX_HOME:-$HOME/.codex}/plugins/cache`, preferring paths that contain `/se-uhd/llm-guidelines/` and then any `llm-guidelines` cache entry.

    If no linter is found, continue without the lint loop. Do not mention the missing linter in the user-facing summary.

    If a linter is found, run `python3 <resolved-lint_markdown.py> --fix llm-guidelines-report.md`. If the linter exits non-zero, read its stdout findings (one per line, tab-separated `<file>:<line>\t<rule>\t<message>`), revise the report in place to address each, and re-run the linter. Repeat at most three iterations; after the third pass proceed regardless of the linter's state. The lint loop is internal quality control; do not mention lint output, rule names, exit codes, or iteration counts in the user-facing summary.

8. **Stop after the report.** Do not modify the user's paper or supplementary material. If the user asks for follow-up edits, treat that as a new request.

## Report template

```markdown
# LLM Guidelines Assessment

**Paper:** <path or title>
**Supplementary material:** <paths>
**Identified study type(s):** <one or more from study-types/>
**Skill version:** <VERSION>

> This report applies the community LLM reporting guidelines from
> <https://llm-guidelines.org> as a self-check for authors. It is not a
> rejection rubric; missing items are reporting gaps to consider, not
> grounds for rejection.

## Summary

<Two-to-four-sentence overall summary: what is reported well, what is missing.>

## Supplementary material availability

<Report what the user provided and what you found in the paper itself:
- User-supplied paths: <list, or "none provided">.
- Links found in the paper: <bulleted list of each URL, with a verbatim quote of the surrounding sentence and its source location (file:line for LaTeX, section/page for PDF). For each URL, state whether it was fetched locally (cloned/downloaded) or only checked for HTTP reachability; if neither was possible, say why.>
- Unanchored release claims: <quote verbatim any "we release" / "available at" / "we open-source" / "publicly available" sentence that does not anchor to a concrete URL, with its source location; this is a reporting gap for the relevant guideline.>
- Coverage: <one sentence on what the fetched supplementary material actually contains, each component anchored to a specific path you read (e.g., "prompts: `prompts/python/api_usage.txt:1-220`; raw completions: `completions/claude-4-sonnet/python_0042.json`; benchmark instances: `benchmark/python/api_usage/`; evaluation code: `execute_benchmark.py`"). If you could not fetch the material, say "not verified — could not fetch" and list the failure mode; do not characterise contents from a `WebFetch` summary.>

If nothing was supplied and nothing was found, say so explicitly and flag it under
the relevant guideline (typically *Report System and Prompt Design* and *Report
Session Traces*).>

## Sharing restrictions

<Report the outcome of workflow step 2:
- Restrictions: <one bullet per restriction, naming the protected elements and the degree of protection, with its source (verbatim quote and location, file path, or "stated by the user in this session"); or "none: <how this was established, e.g., no signs found and the user confirmed none / not asked (non-interactive run), assumed none>".>
- Recommendations not applicable under these restrictions: <one bullet per dropped gap, naming the guideline, the recommendation, and the restriction that blocks it; omit this bullet if nothing was dropped.>

Gaps that were rephrased rather than dropped stay in their guideline block,
prefixed with *Adjusted for restriction:*.>

## Per-guideline findings

### Declare LLM Usage and Role

- Status: <covered | partial | not found | not applicable>
- Evidence: <1-3 items, each a verbatim quote from the paper or a verbatim excerpt from a file in the supplementary material (or, for binary/structured data files, a direct file-or-key pointer), with source location (e.g., `_s3_realistic.tex:140`, `prompts/judge_prompt.txt:1-12`, or `benchmark/python/api_usage/instance_0042.json`). Do not paraphrase here; gaps and interpretation belong in the Gaps bullet.>
- Gaps: <author-facing bullets; each bullet's premise must be supported by an Evidence item or by an absence you actually checked for (state what you searched and how, e.g., "grep for '\\bdate\\b' across all .tex files returned no experiment date").>
- Pointers: <links to ./guidelines/declare-usage.md>

<... repeat for each of the remaining guidelines ...>

## Checklist gaps

<Items from ./checklist.md that were not surfaced above.>

## Notes for reviewers

<If invoked by a reviewer, surface 3 to 5 clarifying questions worth asking the
authors. Otherwise omit this section.>
```

## Mode-specific constraints

These add to the shared constraints in [`../SKILL.md`](../SKILL.md):

- **Ground every claim in a verbatim quote or a file pointer.** Every factual statement in the report about what the paper or the supplementary material does, says, contains, or omits **must** be backed by one of: (a) a verbatim quote from the paper with a source location (e.g., `_s4_evaluation.tex:34` or "§4.2, p. 7"), or (b) a pointer to a specific file (or file plus line range / key) in the supplementary material that was actually read (e.g., `prompts/judge_prompt.txt:1-40`, `benchmark/python/instance_0042.json`). Statements that paraphrase or summarise the paper **must** cite the underlying source the same way. **Do not write hedged language** such as *"the repo appears to include …"*, *"the README seems to describe …"*, *"presumably …"*, *"likely contains …"*, *"suggests that …"*, *"indicates that …"*, *"based on the structure …"*, *"it can be inferred …"* — if you cannot back the claim with a verbatim quote or a file pointer, do not make the claim. Instead, state the gap explicitly: name what you tried to verify, what you read, and what is therefore unknown. Absence of evidence is reported as absence, not as a guess.
- **Only quote what you have read.** Quotation marks in the report must contain text that appears verbatim in a source you opened (the paper's `.tex` / extracted PDF text, or a file in the materialised supplementary directory). Do not "quote" a `WebFetch` summary or a rendering of an HTML directory listing — that is paraphrase, not source text. If a quote spans an ellipsis, use `[...]` and keep the rest verbatim.
- **Review mode writes only `llm-guidelines-report.md`** in the working directory. No other user files are touched.
