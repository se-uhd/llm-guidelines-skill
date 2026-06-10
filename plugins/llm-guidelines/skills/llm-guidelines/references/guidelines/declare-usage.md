# Declare LLM Usage and Role

> ***Summary***: Researchers **must** disclose any use of LLMs to support empirical studies, specifying which LLM was used, how it was used, and where in the research process it was employed. This disclosure **should** appear in a suitable section of the *paper*. They **should** report the exact purpose, the tasks that were automated, and the expected benefits in the *paper*. When the LLM is central to the study, the declaration **should** be prominent and detailed in the methodology section; for tangential uses, a brief statement in the methodology section suffices.

## Rationale

Transparency about LLM involvement is a prerequisite for informed assessment of a study’s scope, limitations, and potential biases. Without explicit disclosure, readers cannot evaluate how the LLM’s characteristics may have influenced the research process or its outcomes.

## Recommendations

When conducting any kind of empirical study involving LLMs, researchers **must** clearly declare that an LLM was used (see [*Scope*](../scope.md) for what we consider relevant research support). This **should** be done in a suitable section of the *paper*, for example, in the introduction or research methods section; Cheng, Calhoun, and Reedy (2025) argue specifically for the methods section, since acknowledgments are easily missed at the end of a paper. The ACM Policy on Authorship requires authors to describe in the methods section any use of AI in the research itself (Association for Computing Machinery 2026).

Beyond generic declarations, researchers **should** report the exact purpose of using an LLM in a study, the tasks it was used to automate, and the expected benefits in the *paper*. A sufficient declaration specifies not only *that* an LLM was used, but also *which* LLM (name and version), *how* it was used (e.g., as an annotator, code generator, or judge), and *where* in the research process it was employed (e.g., data collection, analysis, or synthesis).

When the LLM is central to the study (e.g., as the main tool being evaluated or as a core component of the research method), the declaration **should** be prominent and detailed, appearing in the methodology section with cross-references to the specific guidelines that apply (e.g., Sections [*Version and Configuration*](../guidelines/model-version.md), [*System and Prompt Design*](../guidelines/design.md), and [*Session Traces*](../guidelines/traces.md)). When the LLM’s role is more tangential (e.g., used for a single preprocessing step), a brief but explicit statement in the methodology section is sufficient. When a study assigns multiple distinct roles to LLMs (e.g., one model generates evaluation data while another scores outputs), each role **should** be declared separately. In each case, the disclosure **must** be specific enough for readers to assess how the LLM’s involvement may affect the study’s validity and reproducibility.

## Examples

The *ACM Policy on Authorship* requires reporting AI-generated artifacts such as code, datasets, and figures where they underlie a study’s conclusions (Association for Computing Machinery 2026). Reporting in the methods section keeps this disclosure visible under double-blind review, where end-of-paper acknowledgments are often removed. An example of an LLM disclosure beyond writing support can be found in a recent paper by Lubos et al. (2024), in which they write in the methodology section:

> *“We conducted an LLM-based evaluation of requirements utilizing the Llama 2 language model with 70 billion parameters, fine-tuned to complete chat responses...”*

A more contemporary declaration could similarly state:

> *“We used Claude Opus 4.7 via the Anthropic API to synthesize themes from interview transcripts, with all prompts and conversation logs published as supplementary material.”*

Golnari et al. (2026)’s DevBench paper illustrates separate disclosure of multiple LLM roles: *GPT-4o* generated the synthetic benchmark instances, nine models (including *Claude 4 Sonnet*, *GPT-4.1*, *DeepSeek-V3*, and *Ministral-3B*) were the evaluation subjects, and *o3-mini* was the LLM judge that scored completions for relevance and helpfulness (Golnari et al. 2026).

## Benefits

Transparency in the use of LLMs helps other researchers understand the context and scope of the study, supporting interpretation and comparison of the results. Realizing these benefits requires reporting the LLM’s exact role and version (see [*Version and Configuration*](../guidelines/model-version.md)).

## Challenges

Declaring LLM usage requires only a brief statement and no additional experiments, making compliance straightforward. One challenge might be authors’ reluctance to disclose LLM usage for valid use cases, because they fear that AI-generated content makes reviewers think that the authors’ work is less original. In fact, there is evidence suggesting that AI disclosure can negatively affect trust in authors (Schilke and Reimann 2025). However, the *ACM Policy on Authorship* requires disclosure of AI used in the research itself, not AI used only to assist with writing (Association for Computing Machinery 2026). Our guidelines focus on such use (see [*Scope*](../scope.md)), not on proofreading or writing support.

## Study Types

Researchers **must** follow this guideline for all study types. The specific focus of the declaration varies by study type. For [*LLMs as Annotators*](../study-types/annotators.md), [*LLMs as Judges*](../study-types/judges.md), [*LLMs for Synthesis*](../study-types/synthesis.md), and [*LLMs as Subjects*](../study-types/subjects.md), researchers **must** declare the specific role assigned to the LLM (e.g., annotator, judge, synthesizer, or simulated participant). For [*Studying LLM Usage*](../study-types/usage.md), researchers **must** clarify which LLM(s) the observed participants used and under which conditions. For [*LLMs for Tools*](../study-types/tools.md), researchers **must** declare the LLM’s role within the tool architecture and its contribution to the tool’s functionality. For [*Benchmarking LLMs*](../study-types/benchmarks.md), researchers **must** declare which LLMs were benchmarked and for which tasks.

## Advice for Reviewers

The most common problem with disclosure is incompleteness or vagueness about how the LLM was used. If the paper says “we used LLM X to help with task Y” without specifying how, reviewers should request clarification. Such requests are typically minor revisions unless the missing details may reveal methodological problems.

If undisclosed LLM use is suspected, the reviewer should consult their editor or program chair. When the evidence is conclusive, the key question is the degree to which undisclosed use affects the study’s contribution, ranging from negligible (e.g., word choice in a single sentence) to severe (e.g., generating the reported data or results).

## See Also

- [Report Model Version, Configuration, and Customizations](../guidelines/model-version.md): The disclosure is incomplete without naming the specific model and version.
- [Report System and Prompt Design](../guidelines/design.md): When the LLM lives inside a tool or agent, authors must also describe that tool’s architecture and prompts.
- [Report Session Traces](../guidelines/traces.md): Session traces show what the LLM did during the study.

## References

Association for Computing Machinery. 2026. “ACM Policy on Authorship.” <https://www.acm.org/publications/policies/new-acm-policy-on-authorship>.

Cheng, Adam, Aaron Calhoun, and Gabriel Reedy. 2025. “Artificial Intelligence-Assisted Academic Writing: Recommendations for Ethical Use.” *Advances in Simulation* 10 (1): 26. <https://doi.org/10.1186/s41077-025-00350-6>.

Golnari, Pareesa Ameneh, Adarsh Kumarappan, Wen Wen, Xiaoyu Liu, Gabriel Ryan, Yuting Sun, Shengyu Fu, and Elsie Nallipogu. 2026. “DevBench: A Realistic, Developer-Informed Benchmark for Code Generation Models.” *CoRR* abs/2601.11895. <https://doi.org/10.48550/ARXIV.2601.11895>.

Lubos, Sebastian, Alexander Felfernig, Thi Ngoc Trang Tran, Damian Garber, Merfat El Mansi, Seda Polat Erdeniz, and Viet-Man Le. 2024. “Leveraging LLMs for the Quality Assurance of Software Requirements.” In *32nd IEEE International Requirements Engineering Conference, RE 2024, Reykjavik, Iceland, June 24-28, 2024*, edited by Grischa Liebel, Irit Hadar, and Paola Spoletini, 389–97. IEEE. <https://doi.org/10.1109/RE59067.2024.00046>.

Schilke, Oliver, and Martin Reimann. 2025. “The Transparency Dilemma: How AI Disclosure Erodes Trust.” *Organizational Behavior and Human Decision Processes* 188: 104405. <https://doi.org/10.1016/j.obhdp.2025.104405>.
