# Use an Open LLM as a Baseline

> ***Summary***: Researchers **should** include an open LLM as a baseline when using commercial models and report inter-model agreement. By open LLM, we mean a model that everyone with the required hardware can deploy and operate. Such models are usually “open weight.” A full replication package with step-by-step instructions **should** be provided as part of the *supplementary material*.

## Rationale

Reproducibility depends on access to the model under study. When research relies exclusively on proprietary models, other researchers cannot independently verify or build upon the findings. Including an open LLM as a baseline ensures that at least part of the study can be fully replicated.

## Recommendations

Empirical studies using LLMs in SE, especially those that target commercial tools or models, **should** incorporate an open LLM as a baseline and report established metrics for inter-model agreement (see [*Benchmarks and Metrics*](../guidelines/benchmarks.md)). We acknowledge that including an open LLM baseline might not always be possible, for example, if the study involves human participants, and letting them work on the tasks using two different models might not be feasible. Using an open model as a baseline is also not necessary if the use of the LLM is tangential to the study goal.

Open models allow other researchers to verify research results and build upon them, even without access to commercial models. A comparison of commercial and open models also allows researchers to contextualize model performance. Researchers **should** ensure the open-LLM baseline is independently reproducible from their *supplementary material*.

Open LLMs are available from hubs such as [*Hugging Face*](https://huggingface.co/). They can be self-hosted with frameworks such as [*Ollama*](https://ollama.com/) or [*LM Studio*](https://lmstudio.ai/), accessed through cloud services such as [*Together AI*](https://together.ai/), AWS, Azure, and Google Cloud, or routed through aggregators such as [*OpenRouter*](https://openrouter.ai/) that expose many providers behind a single API. For agentic setups, open-source tools such as [*Continue*](https://www.continue.dev/), [*Cline*](https://cline.bot/), and [*opencode*](https://opencode.ai/) (OpenCode Contributors 2025) publish their full agent code, system prompts, and tool catalog—vendor-hosted services such as *GitHub Copilot* and *Claude Code* expose only parts of their tooling (e.g., editor extensions, hook examples) and keep their deployed agent loops, system prompts, and tool catalogs proprietary.

The term “open” can have different meanings in the context of LLMs. Widder, Whittaker, and West (2024) discuss three types of openness (i.e., transparency, reusability, and extensibility) and what openness can and cannot provide (Widder, Whittaker, and West 2024). The *Open Source Initiative* (OSI) (Open Source Initiative (OSI) 2025) defines open-source AI as having access to everything needed to understand, modify, share, retrain, and recreate the model.

## Examples

An increasing number of studies have adopted open LLMs as baseline models. For example, Wang et al. (2024) evaluated seven advanced LLMs, six of which were open-source, testing 145 API mappings drawn from eight popular Python libraries across 28,125 completion prompts aimed at detecting deprecated API usage in code completion. Moumoula et al. (2024) compared four LLMs on a cross-language code clone detection task. Three evaluated models were open-source. Gonçalves et al. (2025) fine-tuned the open LLM *LLaMA* 3.2 on a refined version of the *DiverseVul* dataset to benchmark vulnerability detection performance (Gonçalves et al. 2025). Golnari et al. (2026) evaluated nine code completion models on the *DevBench* benchmark and included three open-weight models (*DeepSeek-V3*, *DeepSeek-V3.1*, and *Ministral-3B*) alongside commercial frontier models, releasing benchmark, evaluation scripts, and per-model raw completions under an MIT license (Golnari et al. 2026). *CodeBERT*, a bimodal transformer pre-trained by Microsoft Research, is published with model weights, source code, and data-processing scripts on GitHub (Microsoft 2023). It has been used as an open baseline across diverse SE tasks, including exploit code generation (Yang et al. 2023), vulnerability detection (Xia, Shao, and Deng 2024), code clone detection (Sonnekalb et al. 2022), and programming assistance for exception handling (Cai et al. 2024).

## Benefits

A true open LLM baseline improves reproducibility by exposing model architectures, parameter settings, and ideally training data, enabling independent verification of results. Such baselines also let researchers compare novel methods against a stable reference point, since proprietary models can silently change between tests. They also allow inspection of training data (when released) and model behavior, helping identify biases and limitations. Unlike closed-source alternatives, which can be withdrawn or silently updated, open LLMs remain available for future studies. They typically avoid the per-use API fees that can constrain research groups with limited budgets.

## Challenges

Open-source LLMs face several challenges:

- *Definitional inconsistency.* Many models release only trained weights without training data or methodological details (“open weight” openness) (Gibney 2024), which is why we reference the OSI definition in our recommendations (Open Source Initiative (OSI) 2025).
- *Performance gap.* Open models often lag behind the most advanced proprietary “frontier” models in common benchmarks, making it difficult to demonstrate clear improvements when evaluating new methods using open LLMs alone.
- *Hardware demands.* Deploying and experimenting with these models typically requires substantial hardware resources, in particular high-performance GPUs that may be beyond reach for many academic groups.
- *Operational complexity.* Unlike APIs provided by proprietary vendors (e.g., the OpenAI API), installing, configuring, and fine-tuning open-source models can be technically demanding.

## Study Types

This guideline applies primarily to study types in which the researcher controls which LLM is used. For [*Benchmarking LLMs*](../study-types/benchmarks.md), an open LLM **should** be one of the models under evaluation, so that the reported scores can be independently re-run. Where this is not feasible, researchers **should** justify the omission and, per [*System and Prompt Design*](../guidelines/design.md), ensure the evaluation harness can be used with open models. For controlled experiments, an open LLM **should** be one of the models under test; if the experimental design requires capabilities that only a specific commercial model exhibits, researchers **should** acknowledge this as a limitation. When evaluating [*LLMs for Tools*](../study-types/tools.md), researchers **should** use an open LLM as a baseline whenever it is technically feasible; if integration proves too complex, they **should** report the initial benchmarking results of open models. For [*LLMs as Annotators*](../study-types/annotators.md) and [*LLMs as Judges*](../study-types/judges.md), researchers **should** compare annotation or judgment quality from open vs. commercial models to assess the extent to which results depend on a specific proprietary model. For [*LLMs for Synthesis*](../study-types/synthesis.md), researchers **should** compare synthesis results from open and commercial models to evaluate robustness of the findings. For [*Studying LLM Usage*](../study-types/usage.md), using an open LLM as a baseline is often not feasible when the study observes participants using specific commercial tools; in such cases, investigators **should** explicitly acknowledge its absence and discuss how this limitation might affect their conclusions. For [*LLMs as Subjects*](../study-types/subjects.md), using an open LLM as a baseline may similarly be impractical if the study design requires the capabilities of a specific model; researchers **should** acknowledge this limitation when applicable.

## Advice for Reviewers

Reviewers should distinguish between LLM use that is central to the research (e.g., building LLM-driven SE tools, using LLMs for synthesis) and use that is tangential (e.g., generating recruiting materials). An open LLM baseline is expected only when LLM use is central; otherwise, its absence need not be justified. When an open baseline is expected, reviewers should look for either the use of an open LLM or a convincing argument for why it is impractical. If authors claim openness, some justification for that characterization is appropriate. Where practical, reviewers should examine whether the replication package contains sufficiently detailed instructions. Performance differences between open and proprietary models are beyond the study authors’ control. Reviewers should focus on whether the open baseline serves the study’s methodological purpose rather than on its absolute performance.

## See Also

- [Report Model Version, Configuration, and Customizations](../guidelines/model-version.md): Authors must report version, configuration, and parameters for open models, not just commercial ones.
- [Report System and Prompt Design](../guidelines/design.md): Self-hosting an open model adds hardware, hosting, and infrastructure to document.
- [Use Suitable Baselines, Benchmarks, and Metrics](../guidelines/benchmarks.md): Inter-model agreement metrics make open-vs-commercial comparisons interpretable.
- [Report Limitations and Mitigations](../guidelines/limitations.md): When using an open LLM as a baseline is impractical, authors must report this as a limitation.

## References

Cai, Yuchen, Aashish Yadavally, Abhishek Mishra, Genesis Montejo, and Tien N. Nguyen. 2024. “Programming Assistant for Exception Handling with CodeBERT.” In *Proceedings of the 46th IEEE/ACM International Conference on Software Engineering, ICSE 2024, Lisbon, Portugal, April 14-20, 2024*, 94:1–13. ACM. <https://doi.org/10.1145/3597503.3639188>.

Gibney, Elizabeth. 2024. “Not all ‘open source’ AI models are actually open.” *Nature News*. <https://doi.org/10.1038/d41586-024-02012-5>.

Golnari, Pareesa Ameneh, Adarsh Kumarappan, Wen Wen, Xiaoyu Liu, Gabriel Ryan, Yuting Sun, Shengyu Fu, and Elsie Nallipogu. 2026. “DevBench: A Realistic, Developer-Informed Benchmark for Code Generation Models.” *CoRR* abs/2601.11895. <https://doi.org/10.48550/ARXIV.2601.11895>.

Gonçalves, José, Miguel Silva, Bernardo Cabral, Tiago Dias, Eva Maia, Isabel Praça, Ricardo Severino, and Luı́s Lino Ferreira. 2025. “Evaluating LLaMA 3.2 for Software Vulnerability Detection.” In *Cybersecurity - 9th European Interdisciplinary Cybersecurity Conference, EICC 2025, Rennes, France, June 18-19, 2025, Proceedings*, edited by Isabel Praça, Simona Bernardi, and Pedro R. M. Inácio, 38–51. Communications in Computer and Information Science. Springer. [https://doi.org/10.1007/978-3-031-94855-8\\3](https://doi.org/10.1007/978-3-031-94855-8\_3).

Microsoft. 2023. “CodeBERT on GitHub.” <https://github.com/microsoft/CodeBERT>.

Moumoula, Micheline Bénédicte, Abdoul Kader Kaboré, Jacques Klein, and Tegawendé F. Bissyandé. 2024. “Large Language Models for Cross-Language Code Clone Detection.” *CoRR* abs/2408.04430. <https://doi.org/10.48550/ARXIV.2408.04430>.

Open Source Initiative (OSI). 2025. “Open Source AI Definition 1.0.” <https://opensource.org/ai/open-source-ai-definition>.

OpenCode Contributors. 2025. “OpenCode: The Open Source AI Coding Agent.” <https://opencode.ai/>.

Sonnekalb, Tim, Bernd Gruner, Clemens-Alexander Brust, and Patrick Mäder. 2022. “Generalizability of Code Clone Detection on CodeBERT.” In *37th IEEE/ACM International Conference on Automated Software Engineering, ASE 2022*, 143:1–3. ACM. <https://doi.org/10.1145/3551349.3561165>.

Wang, Chong, Kaifeng Huang, Jian Zhang, Yebo Feng, Lyuye Zhang, Yang Liu, and Xin Peng. 2024. “How and Why LLMs Use Deprecated APIs in Code Completion? An Empirical Study.” *CoRR* abs/2406.09834. <https://doi.org/10.48550/ARXIV.2406.09834>.

Widder, David Gray, Meredith Whittaker, and Sarah Myers West. 2024. “Why ‘Open’AI Systems Are Actually Closed, and Why This Matters.” *Nature* 635 (8040): 827–33.

Xia, Yuying, Haijian Shao, and Xing Deng. 2024. “VulCoBERT: A CodeBERT-Based System for Source Code Vulnerability Detection.” In *2024 International Conference on Generative Artificial Intelligence and Information Security, GAIIS 2024, Kuala Lumpur, Malaysia, May 10-12, 2024*. ACM. <https://doi.org/10.1145/3665348.3665391>.

Yang, Guang, Yu Zhou, Xiang Chen, Xiangyu Zhang, Tingting Han, and Taolue Chen. 2023. “ExploitGen: Template-Augmented Exploit Code Generation Based on CodeBERT.” *J. Syst. Softw.* 197: 111577. <https://doi.org/10.1016/J.JSS.2022.111577>.
