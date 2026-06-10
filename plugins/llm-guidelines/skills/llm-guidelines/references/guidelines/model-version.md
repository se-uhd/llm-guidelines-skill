# Report Model Version, Configuration, and Customizations

> ***Summary***: Researchers **must** report the exact LLM model or tool version, configuration, and date of study execution in the *paper*. When using quantized models, researchers **should** report the quantization level and method. For fine-tuned models, they **must** describe the fine-tuning goal, dataset, and procedure in the *paper*. Researchers **should** include default parameters, explain model choices, compare base- and fine-tuned model using suitable metrics and benchmarks, and share fine-tuning data and weights as *supplementary material* (or alternatively justify in the *paper* why they cannot share them).

## Rationale

LLMs and LLM-based tools are frequently updated, and configuration parameters such as temperature or seed values affect content generation. This guideline focuses on documenting the *model-specific* aspects of empirical studies involving LLMs, concentrating on the models themselves, their version, configuration parameters, and customizations (e.g., fine-tuning). While the [*System and Prompt Design*](../guidelines/design.md) section addresses system-level integration and the authored artifacts (including prompts) that the model uses on each call, the information outlined here is essential for reproducibility whenever an LLM is involved.

## Recommendations

Researchers **must** document in the *paper* which model or tool version they used in their study, along with the date of study execution and the parameters they configured that affect output generation. Since default values might change over time, researchers **should** report all configuration values, even if they used the defaults. Checksums and fingerprints **should** be reported since they identify specific versions and configurations. Depending on the study context, other properties such as the context window size (number of tokens) **should** be reported. When using quantized models, researchers **should** report the quantization level (e.g., 4-bit, 8-bit) and method (e.g., GPTQ or AWQ), as different quantization approaches produce different outputs, affecting both output quality and reproducibility. Researchers **should** motivate in the *paper* why they selected certain models, versions, and configurations. Reasons may be monetary, technical, or methodological (e.g., planned comparison to previous work). Depending on the specific study context, additional information regarding the experiment or tool architecture **should** be reported.

A common customization approach for existing LLMs is fine-tuning. If a model was fine-tuned, researchers **must** describe the fine-tuning goal (e.g., improving the performance for a specific task), the fine-tuning procedure (e.g., full fine-tuning versus Low-Rank Adaptation (LoRA), selected hyperparameters, loss function, learning rate, and batch size), and the fine-tuning dataset (e.g., data sources, the preprocessing pipeline, dataset size) in the *paper*. Researchers **should** either share the fine-tuning dataset as part of the *supplementary material* or explain in the *paper* why the data cannot be shared (e.g., because it contains confidential or personal data that could not be anonymized). The same applies to the fine-tuned model weights. Suitable benchmarks and metrics **should** be used to compare the base model with the fine-tuned model.

In summary, researchers **must** report in the *paper* at minimum (1) the exact model or tool name and version, (2) all parameters they configured that affect output generation, (3) the date of study execution, and, for fine-tuned models, (4) the fine-tuning goal, dataset characterization, approach (e.g., full fine-tuning vs. LoRA), and hyperparameters. Beyond these requirements, researchers **should** additionally report default parameter values, checksums or fingerprints, model properties relevant to the study (e.g., context-window size), and quantization level and method where applicable. For fine-tuned models, they **should** also share the dataset and model weights as *supplementary material* (unless legal or privacy constraints prevent disclosure) and report validation metrics and benchmarks.

Commercial models (e.g., GPT-5) or LLM-based tools (e.g., ChatGPT) might not give researchers access to all required information. For these tools, researchers **should** report what is available and openly acknowledge limitations that hinder reproducibility.

## Examples

Based on the documentation that OpenAI and Azure provide (OpenAI 2025; Microsoft 2025), researchers might, for example, report:

> *“We integrated a `gpt-4` model in version `0125-Preview` via the Azure OpenAI Service, and configured it with a temperature of 0.7, top\_p set to 0.8, a maximum token length of 512, and the seed value `23487`. We ran our experiment on 10th January 2025. The system fingerprint was `fp_6b68a8204b`.*

Kang, Yoon, and Yoo (2023) provide a similar statement in their paper on exploring LLM-based bug reproduction:

> *“We access OpenAI Codex via its closed beta API, using the code-davinci-002 model. For Codex, we set the temperature to 0.7, and the maximum number of tokens to 256.”*

Our guidelines additionally recommend reporting a checksum/fingerprint and exact dates; otherwise, this example is close to our recommendations.

Dhar, Vaidhyanathan, and Varma (2024) assessed whether LLMs can generate architectural design decisions, detailing the system architecture and the LLM’s role within it. They provide information on the fine-tuning approach and datasets, including the source of architectural decision records, preprocessing methods, and data selection criteria.

For self-hosted models, the *supplementary material* can become a true replication package. For example, for models provisioned using [ollama](https://ollama.com/library/), one can report the specific tag and checksum, e.g., *“llama3.3, tag 70b-instruct-q8\_0, checksum d5b5e1b84868.”* Given suitable hardware, running the model is then as easy as executing the following command: `ollama run llama3.3:70b-instruct-q8_0`

## Benefits

Reporting the model version, configuration, and date of study execution is a prerequisite for the verification and replication of LLM-based studies. While LLMs are inherently non-deterministic, this cannot excuse dismissing reproducibility. Although exact reproducibility is hard to achieve, the recommendations above help researchers come as close as possible to that standard.

## Challenges

Different model providers and modes of operating the models allow for varying degrees of information. For example, OpenAI provides a model version and a system fingerprint describing the backend configuration, which can also influence the output. However, the fingerprint is intended only to detect changes in the model or its configuration; one cannot go back to a certain fingerprint. As a beta feature, OpenAI lets users set a seed parameter to receive “*(mostly) consistent output*” (OpenAI 2023). However, the seed value does not allow for full reproducibility and the fingerprint changes frequently. Although, as motivated above, open models substantially simplify re-running experiments, they also come with challenges in terms of reproducibility, as generated outputs can be inconsistent despite setting the temperature to 0 and using a seed value (see [GitHub issue for Llama3](https://github.com/ollama/ollama/issues/5321)). Setting the temperature to 0 configures greedy decoding (always selecting the most probable next token), which minimizes output variability but can degrade quality by producing repetitive text and missing higher-quality responses (Holtzman et al. 2020).

Even with a temperature of 0, full determinism is rarely guaranteed. Floating-point arithmetic on GPUs causes slight numerical differences that cascade into divergent token selections (Yuan et al. 2025), and Sparse Mixture-of-Experts routing amplifies this effect (Chann 2023). Silent backend changes in commercial APIs produce different outputs over time (Chen, Zaharia, and Zou 2024), and even self-hosted open models with identical settings do not always yield consistent outputs (Atil et al. 2024). Researchers **should not** treat a temperature of 0 as a guarantee of reproducibility, but as one measure among several, including fixed seed values (OpenAI 2023), system fingerprints, and archiving of raw outputs. When a temperature of 0 is chosen primarily for reproducibility, this motivation **should** be stated explicitly, along with an acknowledgment of its potential impact on output quality.

## Study Types

This guideline **must** be followed for all study types for which the researcher has access to (parts of) the model’s configuration. They **must** always report the configuration that is visible to them, acknowledging the reproducibility challenges of commercial tools and models that are offered as-a-service. Depending on the specific study type, researchers **should** provide additional information on the system and prompt design (see [*System and Prompt Design*](../guidelines/design.md)), session traces (see [*Session Traces*](../guidelines/traces.md)), and specific limitations and mitigations (see [*Limitations and Mitigations*](../guidelines/limitations.md)).

For example, when [*Studying LLM Usage*](../study-types/usage.md) by focusing on commercial tools such as ChatGPT or GitHub Copilot, researchers **must** be as specific as possible in describing their study setup. The configured model name, version, and the date of study execution **must** always be reported. See [*System and Prompt Design*](../guidelines/design.md) for prompt reporting and [*Session Traces*](../guidelines/traces.md) for interaction logs.

For [*LLMs as Annotators*](../study-types/annotators.md), [*LLMs as Judges*](../study-types/judges.md), and [*LLMs for Synthesis*](../study-types/synthesis.md), researchers **must** report the model configuration used for the respective annotation, judging, or synthesis tasks, including temperature and other sampling parameters that affect output variability. For [*LLMs as Subjects*](../study-types/subjects.md), researchers **must** report any persona-related configuration settings and parameters that configure the simulated behavior. For [*LLMs for Tools*](../study-types/tools.md), researchers **must** report the configuration for each model integrated in the tool’s architecture, including any model-specific parameter choices. For [*Benchmarking LLMs*](../study-types/benchmarking.md), researchers **must** report the configuration for all benchmarked models to enable fair cross-model comparisons.

## Advice for Reviewers

Missing version, configuration, or parameter information is typically a minor revision request. Before concluding that information is absent, reviewers should check appendices and supplementary materials, as details are sometimes reported there rather than in the main text. Rejection over missing details is rarely warranted unless the omissions obscure deeper methodological problems.

## See Also

- [Report System and Prompt Design](../guidelines/design.md): Beyond the model itself, authors must also document the architecture and prompts that use it.
- [Report Session Traces](../guidelines/traces.md): Session traces show what the reported model and configuration produced at runtime.
- [Use Suitable Baselines, Benchmarks, and Metrics](../guidelines/benchmarks-metrics.md): Benchmark comparisons require identifying the exact model version under test.
- [Use an Open LLM as a Baseline](../guidelines/open-llm.md): An open model gives full version visibility, which some commercial products do not.
- [Report Limitations and Mitigations](../guidelines/limitations.md): Hidden or shifting commercial versions become reproducibility threats in their own right.

## References

Atil, Berk, Sarp Aykent, Alexa Chittams, Lisheng Fu, Rebecca J. Passonneau, Evan Radcliffe, Guru Rajan Rajagopal, et al. 2024. “Non-Determinism of ‘Deterministic’ LLM Settings.” *CoRR* abs/2408.04667. <https://arxiv.org/abs/2408.04667>.

Chann, Sherman. 2023. “Non-determinism in GPT-4 is caused by Sparse MoE.” <https://152334h.github.io/blog/non-determinism-in-gpt-4/>.

Chen, Lingjiao, Matei Zaharia, and James Zou. 2024. “How Is ChatGPT’s Behavior Changing over Time?” *Harvard Data Science Review* 6 (2). <https://doi.org/10.1162/99608f92.5317da47>.

Dhar, Rudra, Karthik Vaidhyanathan, and Vasudeva Varma. 2024. “Can LLMs Generate Architectural Design Decisions? - an Exploratory Empirical Study.” In *21st IEEE International Conference on Software Architecture, ICSA 2024, Hyderabad, India, June 4-8, 2024*, 79–89. IEEE. <https://doi.org/10.1109/ICSA59870.2024.00016>.

Holtzman, Ari, Jan Buys, Li Du, Maxwell Forbes, and Yejin Choi. 2020. “The Curious Case of Neural Text Degeneration.” In *8th International Conference on Learning Representations, ICLR 2020, Addis Ababa, Ethiopia, April 26-30, 2020*. OpenReview.net. <https://openreview.net/forum?id=rygGQyrFvH>.

Kang, Sungmin, Juyeon Yoon, and Shin Yoo. 2023. “Large Language Models Are Few-Shot Testers: Exploring LLM-Based General Bug Reproduction.” In *45th IEEE/ACM International Conference on Software Engineering, ICSE 2023*, 2312–23. IEEE. <https://doi.org/10.1109/ICSE48619.2023.00194>.

Microsoft. 2025. “Azure OpenAI Service models.” <https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models>.

OpenAI. 2023. “How to make your completions outputs consistent with the new seed parameter.” <https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter>.

———. 2025. “OpenAI API Reference.” <https://platform.openai.com/docs/api-reference>.

Yuan, Jiayi, Hao Li, Xinheng Ding, Wenya Xie, Yu-Jhe Li, Wentian Zhao, Kun Wan, Jing Shi, Xia Hu, and Zirui Liu. 2025. “Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference.” In *Advances in Neural Information Processing Systems 38: Annual Conference on Neural Information Processing Systems 2025, NeurIPS 2025*. <https://openreview.net/forum?id=Q3qAsZAEZw>.
