# Reporting Checklist

The following checklist, inspired by CONSORT (Schulz, Altman, and Moher 2010), summarizes actionable items from the guidelines based on the **summary** sections. The checklist is organized along typical paper sections. Items marked ● are requirements (**must**); items marked <span class="marker-should">●</span> are recommendations (**should**). Each item references its source guideline by short name. Items annotated with *paper* or *supplementary material* indicate where information should be reported; unmarked items may be reported in either.

## Introduction

- ● Disclose any use of LLMs in the empirical study, specifying which LLM, how, and where it was used ([Declare Usage](./guidelines/declare-llm-usage-and-role.md)).
- <span class="marker-should">●</span> Report the purpose of using LLMs, automated tasks, and expected benefits in the *paper* ([Declare Usage](./guidelines/declare-llm-usage-and-role.md)).

## Research Design and Methods


### Model Selection and Configuration

- ● Report the exact LLM model or tool version, configuration, and experiment date in the *paper* ([Model Version](./guidelines/report-model-version-configuration-and-customizations.md)).
- ● For fine-tuned models, describe the fine-tuning goal, dataset, and procedure in the *paper* ([Model Version](./guidelines/report-model-version-configuration-and-customizations.md)).
- <span class="marker-should">●</span> Report default parameters and explain model and version choices ([Model Version](./guidelines/report-model-version-configuration-and-customizations.md)).
- <span class="marker-should">●</span> For quantized models, report the quantization level (e.g., 4-bit, 8-bit) and method (e.g., GPTQ or AWQ) ([Model Version](./guidelines/report-model-version-configuration-and-customizations.md)).
- <span class="marker-should">●</span> Compare base and fine-tuned models using suitable metrics and benchmarks; share fine-tuning data and weights as *supplementary material* (or justify in the *paper* why they cannot be shared) ([Model Version](./guidelines/report-model-version-configuration-and-customizations.md)).

### System and Prompt Design

- ● Describe the full architecture of LLM-based tools in the *paper*, including the role of the LLM, interactions with other components, and overall system behavior ([Design](./guidelines/report-system-and-prompt-design.md)).
- ● Specify whether zero-shot, one-shot, or few-shot prompting was used in the *paper* ([Design](./guidelines/report-system-and-prompt-design.md)).
- ● Specify prompt reuse across models and configurations ([Design](./guidelines/report-system-and-prompt-design.md)).
- ● For dynamically generated prompts, document the generation process thoroughly ([Design](./guidelines/report-system-and-prompt-design.md)).
- ● Publish all prompts or, when using templates, prompt templates with representative instances, including their structure, content, formatting, and dynamic components, as *supplementary material* ([Design](./guidelines/report-system-and-prompt-design.md)).
- ● Describe any context-file mechanisms used (e.g., `AGENTS.md`, `CLAUDE.md`) in the *paper* ([Design](./guidelines/report-system-and-prompt-design.md)).
- ● Summarize which tools and skills were exposed to the model in the *paper* ([Design](./guidelines/report-system-and-prompt-design.md)).
- ● If autonomous agents are used, specify agent roles, reasoning frameworks, and communication flows ([Design](./guidelines/report-system-and-prompt-design.md)).
- ● For retrieval-augmented generation (RAG) or related methods, describe how external data was retrieved, stored, and integrated ([Design](./guidelines/report-system-and-prompt-design.md)).
- ● Report hosting, hardware setup, and latency implications ([Design](./guidelines/report-system-and-prompt-design.md)).
- <span class="marker-should">●</span> Justify design decisions ([Design](./guidelines/report-system-and-prompt-design.md)).
- <span class="marker-should">●</span> Describe prompt development rationale and selection process ([Design](./guidelines/report-system-and-prompt-design.md)).
- <span class="marker-should">●</span> Report prompt evolution and any LLM-suggested refinements ([Design](./guidelines/report-system-and-prompt-design.md)).
- <span class="marker-should">●</span> For user-authored prompts, describe how they were collected and analyzed ([Design](./guidelines/report-system-and-prompt-design.md)).
- <span class="marker-should">●</span> Document input handling and token optimization strategies when prompts are long or complex ([Design](./guidelines/report-system-and-prompt-design.md)).
- <span class="marker-should">●</span> If full prompt disclosure is not feasible, provide summaries or examples ([Design](./guidelines/report-system-and-prompt-design.md)).
- <span class="marker-should">●</span> For ensemble architectures, explain the coordination logic between models in the *paper* ([Design](./guidelines/report-system-and-prompt-design.md)).
- <span class="marker-should">●</span> Where legally possible, release the source code of the implementation under an open-source license ([Design](./guidelines/report-system-and-prompt-design.md)).
- <span class="marker-should">●</span> Report data preprocessing, versioning, and update frequency for stored data used for context augmentation ([Design](./guidelines/report-system-and-prompt-design.md)).
- <span class="marker-should">●</span> Include context-file contents as *supplementary material* ([Design](./guidelines/report-system-and-prompt-design.md)).
- <span class="marker-should">●</span> Include the complete list of tools and skills (names with one-line purposes), tool schemas, skill definitions, sub-agent definitions, and connected MCP servers as *supplementary material* ([Design](./guidelines/report-system-and-prompt-design.md)).

### Session Traces

- <span class="marker-should">●</span> Include full interaction logs (prompts and responses) as *supplementary material* if privacy and confidentiality can be ensured ([Traces](./guidelines/report-session-traces.md)).
- <span class="marker-should">●</span> For agentic systems, include interaction logs covering exchanges between humans and the agent and between external tools and the agent (human-in-the-loop feedback, approvals, refinements) as *supplementary material* ([Traces](./guidelines/report-session-traces.md)).
- <span class="marker-should">●</span> For agentic systems, report the complete runtime trace as *supplementary material*, including for each entry the tool or artifact name, arguments, result, and ordering, and which configured artifacts (skills, context files, sub-agents) were activated ([Traces](./guidelines/report-session-traces.md)).
- <span class="marker-should">●</span> For agentic systems, report developed plans as *supplementary material* if available ([Traces](./guidelines/report-session-traces.md)).

### Benchmarks and Metrics

- ● Justify all benchmark and metric choices in the *paper* ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- ● Explain in the *paper* why the selected metrics are suitable for the specific study ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- <span class="marker-should">●</span> Provide an operational definition of the phenomenon the benchmark is intended to measure, including its scope and any sub-components ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- <span class="marker-should">●</span> Summarize benchmark structure, task types, and limitations ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- <span class="marker-should">●</span> Describe and justify the sampling strategy used to select problems for inclusion in the benchmark; for non-probability sampling, discuss generalizability implications ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- <span class="marker-should">●</span> Identify the capabilities a benchmark conflates with the target phenomenon, isolate the target where possible, and acknowledge remaining confounders as construct-validity threats ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- <span class="marker-should">●</span> Perform an error analysis: categorize the failures observed and report their relative frequency; report failures that cluster on confounding capabilities as construct-validity threats ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- <span class="marker-should">●</span> For new or released benchmarks, adopt contamination-prevention mechanisms: held-out subset, canary strings, and pre-exposure investigation against common training corpora ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- <span class="marker-should">●</span> For ratings that vary across raters or runs (human raters, LLM-as-judge), report the distribution of ratings per item rather than only aggregated point estimates ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- <span class="marker-should">●</span> Justify the number of experiment repetitions, for example through a power analysis or by monitoring convergence of descriptive statistics ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- <span class="marker-should">●</span> Include an open LLM as a baseline when using commercial models and report inter-model agreement ([Open LLM](./guidelines/use-an-open-llm-as-a-baseline.md)).

### Human Validation

- ● If using human validation, define the measured construct (e.g., usability, maintainability) and describe the measurement instrument in the *paper* ([Human Validation](./guidelines/use-human-validation-for-llm-outputs.md)).
- ● When developing or adapting measurement instruments, share them ([Human Validation](./guidelines/use-human-validation-for-llm-outputs.md)).
- <span class="marker-should">●</span> Consider human validation early in the study design and build on established reference models for human-LLM comparison ([Human Validation](./guidelines/use-human-validation-for-llm-outputs.md)).
- <span class="marker-should">●</span> Validate LLM judgments against human judgment, report aggregation methods, and assess human-LLM agreement ([Human Validation](./guidelines/use-human-validation-for-llm-outputs.md)).
- <span class="marker-should">●</span> Discuss and, where feasible, control for confounding factors ([Human Validation](./guidelines/use-human-validation-for-llm-outputs.md)).
- <span class="marker-should">●</span> For value-laden or culturally contingent constructs, describe rater demographics beyond expertise and discuss potential demographic biases ([Human Validation](./guidelines/use-human-validation-for-llm-outputs.md)).

### Reproducibility, Ethics, and Resources

- ● For studies involving sensitive data, discuss data governance mechanisms compliant with applicable jurisdictional obligations ([Limitations](./guidelines/report-limitations-and-mitigations.md)).
- <span class="marker-should">●</span> Justify LLM usage in light of its resource demands ([Limitations](./guidelines/report-limitations-and-mitigations.md)).
- <span class="marker-should">●</span> Where full sharing of prompts, traces, or datasets is not feasible, share representative examples for partial replicability ([Limitations](./guidelines/report-limitations-and-mitigations.md)).
- <span class="marker-should">●</span> Provide a full replication package with step-by-step instructions as *supplementary material* ([Open LLM](./guidelines/use-an-open-llm-as-a-baseline.md)).

## Results

- ● If comparing models or tools, use appropriate inferential statistics (e.g., hypothesis tests, effect sizes) rather than relying solely on summary statistics ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- <span class="marker-should">●</span> Repeat experiments due to the inherent non-determinism of LLMs and report the result distribution using descriptive statistics ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- <span class="marker-should">●</span> Use traditional (non-LLM) baselines for comparison where possible ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).
- <span class="marker-should">●</span> Report established metrics to make study results comparable; additional metrics may be reported where appropriate ([Benchmarks](./guidelines/use-suitable-baselines-benchmarks-and-metrics.md)).

## Limitations and Threats to Validity

- ● Describe measurement constructs and methods; disclose any data leakage risks and avoid leaking evaluation data into LLM improvement pipelines ([Limitations](./guidelines/report-limitations-and-mitigations.md)).
- ● Acknowledge non-disclosed confidential or proprietary components as reproducibility limitations ([Design](./guidelines/report-system-and-prompt-design.md)).
- ● Transparently report study limitations, including the impact of non-determinism and generalizability constraints ([Limitations](./guidelines/report-limitations-and-mitigations.md)).
- ● Specify whether generalization across LLMs or across time was assessed, and discuss model and version differences ([Limitations](./guidelines/report-limitations-and-mitigations.md)).
- <span class="marker-should">●</span> Employ and report strategies to mitigate identified validity and reproducibility threats, such as replication packages, human validation, longitudinal re-runs, triangulation, and sensitivity analysis ([Limitations](./guidelines/report-limitations-and-mitigations.md)).

## References

Schulz, Kenneth F., Douglas G. Altman, and David Moher. 2010. “CONSORT 2010 Statement: Updated Guidelines for Reporting Parallel Group Randomised Trials.” *BMJ* 340: c332. <https://doi.org/10.1136/bmj.c332>.

