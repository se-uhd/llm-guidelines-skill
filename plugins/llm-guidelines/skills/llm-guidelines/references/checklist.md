# Reporting Checklist

The following checklist, inspired by CONSORT (Schulz, Altman, and Moher 2010), summarizes actionable items from the guidelines based on the **summary** sections. The checklist is organized along typical paper sections. Items prefixed with **must** are requirements; items prefixed with **should** are recommendations. Each item references its source guideline by short name. Items annotated with *paper* or *supplementary material* indicate where we expect the information to be reported. Unmarked items may be reported either in the paper or as supplementary material. Items prefixed with a backticked tag (e.g., `[fine-tuning]`, `[agents]`) apply only to studies with that characteristic. Beyond these characteristic-tagged items, each guideline’s *Study Types* subsection lists study-type-specific recommendations where applicable.

## Introduction

- **must** Disclose any use of LLMs in the empirical study, specifying which LLM, how, and where it was used ([Declare Usage](./guidelines/declare-llm-usage-and-role.md)).
- **should** Report in the *paper* the purpose of using LLMs, the tasks they automate, and the expected benefits ([Declare Usage](./guidelines/declare-llm-usage-and-role.md)).

## Research Design and Methods

### Model Selection and Configuration

- **must** Report in the *paper* the exact LLM model or tool version, the configuration, and the date of study execution ([Model Version](./guidelines/report-model-version-configuration-and-customizations.md)).
- **must** `[fine-tuning]` For fine-tuned models, describe in the *paper* the fine-tuning goal, the dataset, and the procedure ([Model Version](./guidelines/report-model-version-configuration-and-customizations.md)).
- **should** Report default parameters and explain model and version choices ([Model Version](./guidelines/report-model-version-configuration-and-customizations.md)).
- **should** Report checksums and additional model properties where available; for commercial tools, openly acknowledge their reproducibility limits ([Model Version](./guidelines/report-model-version-configuration-and-customizations.md)).
- **should** `[quantization]` For quantized models, report the quantization level (e.g., 4-bit, 8-bit) and method (e.g., GPTQ or AWQ) ([Model Version](./guidelines/report-model-version-configuration-and-customizations.md)).
- **should** `[fine-tuning]` Compare base and fine-tuned models using suitable metrics and benchmarks; share fine-tuning data and weights as *supplementary material* (or justify in the *paper* why they cannot be shared) ([Model Version](./guidelines/report-model-version-configuration-and-customizations.md)).
- **should** `[commercial-models]` Include an open LLM as a baseline when using commercial models and report inter-model agreement ([Open LLM](./guidelines/use-an-open-llm-as-a-baseline.md)).

### System and Prompt Design

- **must** Describe in the *paper* the full architecture of LLM-based tools, including the role of the LLM, interactions with other components, and overall system behavior ([Design](./guidelines/report-system-and-prompt-design.md)).
- **must** Specify in the *paper* whether zero-shot, one-shot, or few-shot prompting was used ([Design](./guidelines/report-system-and-prompt-design.md)).
- **must** Specify prompt reuse across models and configurations ([Design](./guidelines/report-system-and-prompt-design.md)).
- **must** Publish all prompts or, when using templates, prompt templates with representative instances, including their structure, content, formatting, and variable components, as *supplementary material* ([Design](./guidelines/report-system-and-prompt-design.md)).
- **must** Report hosting and hardware setup ([Design](./guidelines/report-system-and-prompt-design.md)).
- **must** `[dynamic-prompts]` For dynamically generated prompts, document the code or rules that assemble each prompt from runtime inputs ([Design](./guidelines/report-system-and-prompt-design.md)).
- **must** `[context-files]` Describe in the *paper* any configuration mechanisms used (e.g., context files such as `CLAUDE.md` or `AGENTS.md`, skills, subagents, hooks, settings, rules) ([Design](./guidelines/report-system-and-prompt-design.md)).
- **must** `[tool-use]` Summarize in the *paper* which tools were exposed to the model ([Design](./guidelines/report-system-and-prompt-design.md)).
- **must** `[agents]` If autonomous agents are used, specify agent roles, reasoning frameworks, and communication flows ([Design](./guidelines/report-system-and-prompt-design.md)).
- **must** `[context-augmentation]` For retrieval-augmented generation (RAG) or related methods, describe how external data was retrieved, stored, and selected for inclusion in the model’s context ([Design](./guidelines/report-system-and-prompt-design.md)).
- **must** `[benchmarking]` Describe the evaluation harness and infrastructure when it goes beyond bare model API calls (e.g., custom sandboxing, orchestration layers, or post-processing pipelines) ([Design](./guidelines/report-system-and-prompt-design.md)).
- **should** Justify substantive architectural choices where alternatives existed (e.g., agentic framework, tool catalog) ([Design](./guidelines/report-system-and-prompt-design.md)).
- **should** Describe prompt development rationale and selection process ([Design](./guidelines/report-system-and-prompt-design.md)).
- **should** Report prompt evolution and any LLM-suggested refinements ([Design](./guidelines/report-system-and-prompt-design.md)).
- **should** Where legally possible, release the source code of the implementation under an open-source license ([Design](./guidelines/report-system-and-prompt-design.md)).
- **should** `[participant-prompts]` For user-authored prompts, describe how they were collected and analyzed ([Design](./guidelines/report-system-and-prompt-design.md)).
- **should** `[long-prompts]` Document input handling and token optimization strategies when prompts are long or complex ([Design](./guidelines/report-system-and-prompt-design.md)).
- **should** `[restricted-sharing]` If full prompt disclosure is not feasible, provide summaries or examples ([Design](./guidelines/report-system-and-prompt-design.md)).
- **should** `[ensemble]` For ensemble architectures, explain in the *paper* the coordination logic between models ([Design](./guidelines/report-system-and-prompt-design.md)).
- **should** `[context-augmentation]` Report data preprocessing, versioning, and update frequency for stored data used for context augmentation ([Design](./guidelines/report-system-and-prompt-design.md)).
- **should** `[context-files]` Include all configuration artifacts (context files, skill folders, subagent files, hooks, settings, rules) as *supplementary material* ([Design](./guidelines/report-system-and-prompt-design.md)).
- **should** `[tool-use]` Include the tool catalog (names with purposes), tool schemas, and connected MCP servers as *supplementary material* ([Design](./guidelines/report-system-and-prompt-design.md)).
- **should** `[benchmarking]` Design the evaluation harness so it is usable with open models ([Design](./guidelines/report-system-and-prompt-design.md)).

### Session Traces

- **should** Include full interaction logs (prompts and responses) as *supplementary material* if privacy and confidentiality can be ensured ([Traces](./guidelines/report-session-traces.md)).
- **should** `[agents]` For agentic systems, include interaction logs covering human-in-the-loop exchanges with the agent (feedback, approvals, refinements) as *supplementary material* ([Traces](./guidelines/report-session-traces.md)).
- **should** `[agents]` For agentic systems, report the complete runtime trace as *supplementary material*, including for each entry the tool or artifact name, arguments, result, and ordering, and which configured artifacts (skills, context files, subagents) were activated ([Traces](./guidelines/report-session-traces.md)).
- **should** `[agents]` For agentic systems, report any plans the system exposes as *supplementary material* ([Traces](./guidelines/report-session-traces.md)).

### Benchmarks and Metrics

- **must** Justify in the *paper* all benchmark and metric choices ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- **must** Explain in the *paper* why the selected metrics are suitable for the specific study ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- **must** `[latency-sensitive]` Report latency when it can affect study outcomes (e.g., interactive user studies, latency comparisons) ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- **should** Provide an operational definition of the phenomenon the benchmark is intended to measure, including its scope and any sub-components ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- **should** Summarize benchmark structure, task types, and limitations ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- **should** Identify the capabilities a benchmark conflates with the target phenomenon, isolate the target where possible, and acknowledge remaining confounders as construct-validity threats ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- **should** Perform an error analysis: categorize the failures observed and report their relative frequency; report failures that cluster on confounding capabilities as construct-validity threats ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- **should** Describe and justify the sampling strategy used to select problems for inclusion in the benchmark ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- **should** Justify the number of experiment repetitions, for example through a power analysis or by monitoring convergence of descriptive statistics ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- **should** `[non-probability-sampling]` For non-probability sampling (e.g., convenience), discuss the implications for the generalizability of conclusions ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- **should** `[new-benchmark]` For new or released benchmarks, adopt contamination-prevention mechanisms: held-out subset, canary strings, and pre-exposure investigation against common training corpora ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- **should** `[multi-rater-scoring]` For ratings that vary across raters or runs (human raters, LLM-as-judge), report the distribution of ratings per item rather than only aggregated point estimates ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).

### Human Validation

- **must** `[human-validation]` If using human validation, define in the *paper* the measured construct (e.g., usability, maintainability) and describe the measurement instrument ([Human Validation](./guidelines/use-human-validation-for-llm-outputs.md)).
- **must** `[human-validation]` When developing or adapting measurement instruments, share them ([Human Validation](./guidelines/use-human-validation-for-llm-outputs.md)).
- **must** `[human-validation]` When LLMs replace humans in research tasks, explain in the *paper* whether and how the replacement is justified ([Human Validation](./guidelines/use-human-validation-for-llm-outputs.md)).
- **should** Consider human validation early in the study design and build on established reference models for human-LLM comparison ([Human Validation](./guidelines/use-human-validation-for-llm-outputs.md)).
- **should** `[human-validation]` When LLMs replace humans in research tasks, report in the *paper* the systematic approach used to justify the replacement, including model-to-model and model-to-human agreement ([Human Validation](./guidelines/use-human-validation-for-llm-outputs.md)).
- **should** `[human-validation]` Validate LLM judgments against human judgment, report aggregation methods, and assess human-LLM agreement ([Human Validation](./guidelines/use-human-validation-for-llm-outputs.md)).
- **should** `[human-validation]` Discuss and, where feasible, control for confounding factors ([Human Validation](./guidelines/use-human-validation-for-llm-outputs.md)).
- **should** `[human-validation]``[subjective-constructs]` For value-laden or culturally contingent constructs, describe rater demographics beyond expertise and discuss potential demographic biases ([Human Validation](./guidelines/use-human-validation-for-llm-outputs.md)).

### Reproducibility, Ethics, and Resources

- **must** `[restricted-sharing]` For studies involving sensitive data, discuss data governance mechanisms compliant with applicable jurisdictional obligations ([Limitations](./guidelines/report-limitations-and-mitigations.md)).
- **should** Justify LLM usage in light of its resource demands ([Limitations](./guidelines/report-limitations-and-mitigations.md)).
- **should** Provide a full replication package as *supplementary material*, including step-by-step instructions for verifying and reproducing the results ([Limitations](./guidelines/report-limitations-and-mitigations.md)).
- **should** `[restricted-sharing]` Where full sharing of prompts, traces, or datasets is not feasible, share representative examples for partial replicability ([Limitations](./guidelines/report-limitations-and-mitigations.md)).

## Results

- **should** Repeat experiments due to the inherent non-determinism of LLMs and report the result distribution using descriptive statistics ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- **should** Use traditional (non-LLM) baselines for comparison where possible ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- **should** Report established metrics to make study results comparable; additional metrics may be reported where appropriate ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- **should** `[comparing-models]` If comparing models or tools, use appropriate inferential statistics (e.g., hypothesis tests, effect sizes) rather than relying solely on summary statistics ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).

## Limitations and Threats to Validity

- **must** Describe measurement constructs and methods; disclose any data leakage risks and avoid leaking evaluation data into LLM improvement pipelines ([Limitations](./guidelines/report-limitations-and-mitigations.md)).
- **must** Transparently report study limitations, including the impact of non-determinism and generalizability constraints ([Limitations](./guidelines/report-limitations-and-mitigations.md)).
- **must** Specify whether generalization across LLMs or across time was assessed, and discuss model and version differences ([Limitations](./guidelines/report-limitations-and-mitigations.md)).
- **must** `[restricted-sharing]` Acknowledge non-disclosed confidential or proprietary components as reproducibility limitations ([Design](./guidelines/report-system-and-prompt-design.md)).
- **should** Employ and report strategies to mitigate identified validity and reproducibility threats, such as replication packages, human validation, longitudinal re-runs, triangulation, and sensitivity analysis ([Limitations](./guidelines/report-limitations-and-mitigations.md)).

## References

Schulz, Kenneth F., Douglas G. Altman, and David Moher. 2010. “CONSORT 2010 Statement: Updated Guidelines for Reporting Parallel Group Randomised Trials.” *BMJ* 340: c332. <https://doi.org/10.1136/bmj.c332>.
