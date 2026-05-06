# Report Limitations and Mitigations

> ***Summary***: Researchers **must** transparently report study limitations, including the impact of non-determinism and generalizability constraints. The *paper* **must** specify whether generalization across LLMs or across time was assessed, and discuss model and version differences. Authors **must** describe measurement constructs and methods, disclose any data leakage risks, and avoid leaking evaluation data into LLM improvement pipelines. For studies involving sensitive data, they **must** discuss data governance mechanisms. They **should** justify LLM usage in light of its resource demands. Mitigation strategies such as replication packages, human validation, longitudinal re-runs, triangulation, and sensitivity analysis **should** be employed and reported where applicable. Where full data sharing is not possible, a subset of the validation data **should** be included to enable partial replication.

## Rationale

When using LLMs for empirical studies in SE, researchers face unique challenges and potential limitations that can influence the validity, reliability, and reproducibility of their findings (Sallou, Durieux, and Panichella 2024). Researchers must openly discuss these limitations and explain how their impact was mitigated. These limitations are relative to current LLM capabilities and tool architectures; speculating about future improvements is beyond the scope of a paper’s limitation section. Nevertheless, risk management and threat mitigation **should** be planned during study design, not as an afterthought.

## Recommendations

Researchers **must** clearly present the limitations of their work without defensiveness or obfuscation. These limitations may concern diverse topics including generalizability, internal validity (e.g. data leakage), reliability (i.e. non-determinism), and reproducibility (e.g. resource requirements). When deterministic reproducibility is structurally unattainable (e.g., SaaS-based models with opaque versioning), researchers **should** adopt trustworthiness criteria from qualitative research to substantiate dependability and confirmability of findings. LLM-based studies may involve many kinds of generalization including the following:

1. From tested LLMs to others; that is, do the performance characteristics of the LLM(s) studied generalize to LLM(s) not included in the study.
2. From tested configurations to others; that is, how sensitive are the results to the specific configuration(s) of the LLM under test.
3. From research to practice; for instance, just because researchers can get a certain level of code generation performance under ideal conditions does not mean software developers, given the same tools, will get similar results without having the researchers present to show them exactly what to do.
4. From a sample of people (e.g. human validators; human participants) to a larger population of people.
5. From one time period to another; i.e., does the same LLM, or other versions of the same LLM, produce similar results at a different point in time?

The following concerns present an overview that has to be tailored to the individual study context. This section does not repeat requirements from other recommendations.

### Internal Validity:

The primary threats to internal validity are:

- Data leakage and contamination, including inter-dataset duplication, potentially resulting in a training–evaluation overlaps, leading to overly optimistic evaluation results.
- Unintended inclusion of evaluation data in model-improvement pipelines, contributing to data leakage. This is especially relevant for longitudinal studies including LLMs.
- Incomplete architecture, prompt, or pipeline reporting, posing hidden confounding factors.

Inter-dataset duplication is prevalent in SE, particularly for code-related benchmarks. As transparency on training data is limited for LLMs, researchers **must** discuss potential data leakage effects and their impact on results.

### Construct Validity:

The primary threats to construct validity are:

- Metric–construct mismatch (e.g., BLEU/ROUGE vs. functional correctness). More traditional metrics might not capture all relevant SE-specific aspects.
- Over-reliance on benchmark-specific metrics. Optimizing for a single benchmark might result in dataset-specific heuristics rather than the intended construct, overstating real-world utility.
- Benchmark scope limitations. Benchmarks commonly ignore runtime behaviors, security implications, readability, testability, and maintainability, yielding results that may not transfer to realistic development settings.

If constructs are based on subjective interpretations, purely automated metrics are insufficient. Researchers **must** discuss how they ensured quality of subjective results, similarly to qualitative research.

### External Validity:

The primary threats to external validity are:

- Cross-model transfer limitations. Results obtained with one LLM (or family of LLMs) may not generalize to others due to differences in training data, architecture, and capabilities.
- Tool-architecture specificity. Tools built around a specific LLM’s API or capabilities may not transfer to other models without substantial re-engineering.
- Limited domain coverage. Studies often focus on a narrow set of programming languages, task types, or application domains, limiting generalizability to other SE contexts.
- Limited participant diversity. Study participants (e.g., human validators, developers) may not represent the broader population in terms of expertise, geographic location, or cultural background.
- Cross-time instability (model evolution). Performance of proprietary models can change over time, leading to non-generalizable study outcomes (Chen, Zaharia, and Zou 2024; Li et al. 2024).

Generalizability is particularly critical for proprietary and non-deterministic systems whose behavior is subject to drift (i.e., silent changes in model output over time) (Chen, Zaharia, and Zou 2024). Researchers **must** discuss the limitations and mitigations of external validity.

### Reliability & Reproducibility:

The primary threats to reliability and reproducibility are:

- Non-deterministic outputs. Identical prompts and configurations can yield different outputs across runs due to factors such as floating-point arithmetic, batching, and stochastic decoding strategies.
- Infrastructure dependence. Results may vary depending on the hardware, software stack, and hosting environment used, making exact replication challenging across different infrastructure setups.
- Resource inequality preventing replication. LLM research is resource-intensive and hence remains predominantly in the domain of private companies or well-funded research institutions (Schwartz et al. 2020; Ahmed, Wahed, and Thompson 2023), excluding researchers from under-resourced institutions.

Researchers **must** discuss the measures taken to increase reliability and reproducibility. However, non-deterministic reproducibility is not inherently disqualifying. Qualitative traditions such as ethnography, grounded theory, and action research ensure trustworthiness through *credibility*, *transferability*, *dependability*, and *confirmability* (Guba 1981). The same applies to SaaS-based LLM research, where providers frequently deprecate model versions without guaranteeing stable behavior.

### Ethical & Regulatory Boundaries:

The primary concerns for ethical and regulatory matters are:

- Use of sensitive or proprietary data. Studies involving proprietary code, confidential business data, or personally identifiable information may face restrictions on data sharing that limit reproducibility.
- Jurisdictional obligations. Data protection regulations (e.g., GDPR, CCPA) and institutional policies may impose constraints on data collection, processing, and sharing in LLM-based studies.
- Implicit model bias. Especially for qualitative research LLM might “*reinforce dominant paradigms and biases*” and “*identify, replicate and reinforce dominant language and patterns*” (Jowsey et al. 2025).

Studies involving sensitive data **must** discuss data governance mechanisms tailored towards LLM environments, compliant with applicable juristical obligations. If applicable, researchers **should** discuss how model biases potentially impact the study outcomes and how those biases were evaluated.

### Environmental & Sustainability Constraints:

- Energy consumption. With growing model size, the environmental impact of experiments with LLMs increases. Considering the environmental impact in the study design is important given the substantial energy costs of LLM experiments (Strubell, Ganesh, and McCallum 2019).
- Trade-off between repetition and sustainability. Repeating experiments increases reliability but also energy consumption, requiring trade-offs during study design.

Researchers **should** justify the LLM’s resource consumption against the benefits over traditional approaches.

### Mitigation Strategies:

The following mitigation strategies can help address the threats described above, depending on the study scope and feasibility.

- *Replication Packages* covering prompt and architecture specifications, model outputs, and representative examples for partial replicability, accompanied by an implementation using an open model for long-term stability.
- *Human Validation* of subjective constructs, following quality criteria known from qualitative research.
- *Longitudinal Re-Runs* to repeat experiments with LLMs over time, complemented by statistical analyses.
- *Methodological Trustworthiness Measures.* Researchers **should** consider triangulation, reflexivity, audit trails, and peer debriefing as complementary measures when deterministic reproduction is structurally impossible.
- *Triangulation* via multiple models (e.g., proprietary and open models), multiple independent datasets, and multiple complementary metrics.
- *Cost Accounting* through reporting of input/output tokens, token and service costs, or hardware specifications.
- *Energy Preservation* by selecting smaller or newer less resource-intensive models and employing techniques such as input/output token reduction, model pruning, quantization, or knowledge distillation (Mitu and Mitu 2024) where feasible. Carbon footprint estimation is desirable, but still difficult.
- *Ethical and Regulatory Considerations* through data governance mechanisms, ethical reviews, and bias assessment procedures.
- *Sensitivity Analysis* through variation of LLM configurations, prompts, architecture decisions, datasets, and if applicable human participant backgrounds.

## Study Types

Researchers **must** follow this guideline for all study types. Transparently reporting limitations and mitigations is a universal requirement, but specific concerns vary by study type. For [*LLMs as Annotators*](../study-types/llms-as-annotators.md), researchers **must** discuss potential biases in label assignment, label reliability limitations, and sensitivity of annotations to prompt wording and model choice. For [*LLMs as Judges*](../study-types/llms-as-judges.md), researchers **must** address measurement validity concerns, known biases such as position bias or verbosity bias, and the extent to which LLM judgments align with human expert assessments. For [*LLMs for Synthesis*](../study-types/llms-for-synthesis.md), researchers **must** discuss the risk of contextual misinterpretation, potential loss of nuance in summarized or aggregated outputs, and reflexivity limitations inherent in using an LLM for qualitative interpretation. For [*LLMs as Subjects*](../study-types/llms-as-subjects.md), researchers **must** discuss the fundamental inability of LLMs to truly simulate human behavior, the risk of stereotype amplification, and the limited ecological validity of simulated responses. For [*Studying LLM Usage*](../study-types/studying-llm-usage-in-software-engineering.md), researchers **must** discuss generalizability constraints across different tools and user populations, and acknowledge how observed usage patterns may not transfer to other contexts. For [*LLMs for Tools*](../study-types/llms-for-new-software-engineering-tools.md), researchers **must** discuss replicability constraints arising from dependencies on commercial models, the impact of model updates on tool behavior, and limitations of the evaluation setup. For [*Benchmarking LLMs*](../study-types/benchmarking-llms-for-software-engineering-tasks.md), researchers **must** discuss potential data contamination, benchmark scope limitations, and the extent to which benchmark performance generalizes to real-world tasks.

## Advice for Reviewers

Reviewers should verify that the limitation section is comprehensive and appropriate for the specific study type, checking that: (1) limitations address the specific threats relevant to the study type (e.g., label reliability for annotation studies, simulation fidelity for studies using LLMs as subjects); (2) mitigations are concrete and correspond to identified limitations rather than being generic statements; (3) the impact of LLM non-determinism on findings is discussed; (4) generalizability constraints, across models, configurations, time periods, and populations, are acknowledged. When important limitations are missing, reviewers should request they be added. The absence of a limitation section, or one that is formulaic or insufficiently specific, is a more serious concern than any individual missing limitation and may warrant a major revision.

## See Also

- [Report Model Version, Configuration, and Customizations](../guidelines/report-model-version-configuration-and-customizations.md): Authors can re-run with different models or configurations to check whether the results depend on those specific choices.
- [Report System and Prompt Design](../guidelines/report-system-and-prompt-design.md): Triangulation across architectures and prompts is one mitigation strategy.
- [Report Session Traces](../guidelines/report-session-traces.md): Stored session traces serve as a baseline against which authors can monitor LLM behavior drift over time.
- [Use Suitable Baselines, Benchmarks, and Metrics](../guidelines/use-suitable-baselines-benchmarks-and-metrics.md): Benchmark and metric choices are one source of construct-validity threats authors must discuss.
- [Use Human Validation for LLM Outputs](../guidelines/use-human-validation-for-llm-outputs.md): When automated metrics cannot validly measure a construct, human validation is an alternative.

## References

Ahmed, Nur, Muntasir Wahed, and Neil C. Thompson. 2023. “The Growing Influence of Industry in AI Research.” *Science* 379 (6635): 884–86. <https://doi.org/10.1126/science.ade2420>.

Chen, Lingjiao, Matei Zaharia, and James Zou. 2024. “How Is ChatGPT’s Behavior Changing over Time?” *Harvard Data Science Review* 6 (2). <https://doi.org/10.1162/99608f92.5317da47>.

Guba, Egon G. 1981. “Criteria for Assessing the Trustworthiness of Naturalistic Inquiries.” *ECTJ* 29 (2): 75–91. <https://doi.org/10.1007/BF02766777>.

Jowsey, Tanisha, Virginia Braun, Victoria Clarke, Victoria Clarke, Deborah Lupton, and Michelle Fine. 2025. “We Reject the Use of Generative Artificial Intelligence for Reflexive Qualitative Research.” *SSRN*. <https://doi.org/10.2139/ssrn.5676462>.

Li, David, Kartik Gupta, Mousumi Bhaduri, Paul Sathiadoss, Sahir Bhatnagar, and Jaron Chong. 2024. “Comparing GPT-3.5 and GPT-4 Accuracy and Drift in Radiology Diagnosis Please Cases.” *Radiology* 310 (1): e232411. <https://doi.org/10.1148/radiol.232411>.

Mitu, Narcis Eduard, and George Teodor Mitu. 2024. “The Hidden Cost of AI: Carbon Footprint and Mitigation Strategies.” *Revista de Stiinte Politice. Revue Des Sciences Politiques* 84: 9–16. <https://doi.org/10.2139/ssrn.5036344>.

Sallou, June, Thomas Durieux, and Annibale Panichella. 2024. “Breaking the Silence: The Threats of Using LLMs in Software Engineering.” In *Proceedings of the 2024 ACM/IEEE 44th International Conference on Software Engineering: New Ideas and Emerging Results, NIER@ICSE 2024, Lisbon, Portugal, April 14-20, 2024*, 102–6. ACM. <https://doi.org/10.1145/3639476.3639764>.

Schwartz, Roy, Jesse Dodge, Noah A. Smith, and Oren Etzioni. 2020. “Green AI.” *Communications of the ACM* 63 (12): 54–63. <https://doi.org/10.1145/3381831>.

Strubell, Emma, Ananya Ganesh, and Andrew McCallum. 2019. “Energy and Policy Considerations for Deep Learning in NLP.” In *Proceedings of the 57th Conference of the Association for Computational Linguistics, ACL 2019, Florence, Italy, July 28- August 2, 2019, Volume 1: Long Papers*, edited by Anna Korhonen, David R. Traum, and Lluı́s Màrquez, 3645–50. Association for Computational Linguistics. <https://doi.org/10.18653/V1/P19-1355>.

