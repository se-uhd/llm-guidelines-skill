# Report Limitations and Mitigations

> ***Summary***: Researchers **must** transparently report study limitations, including the impact of non-determinism and generalizability constraints. The *paper* **must** specify whether generalization across LLMs or across time was assessed, and discuss model and version differences. Authors **must** discuss potential data leakage effects and their impact on results, including the risk of evaluation data entering model improvement pipelines, and **must** describe how the quality of subjective results was ensured. For studies involving sensitive data, they **must** discuss data governance mechanisms. They **should** justify LLM usage in light of its resource demands. Mitigation strategies such as replication packages, human validation, longitudinal re-runs, triangulation, and sensitivity analysis **should** be employed and reported where applicable. Where full data sharing is not possible, a subset of the validation data **should** be included to enable partial replication.

## Rationale

When using LLMs for empirical studies in SE, researchers face unique challenges and potential limitations that can influence the validity, reliability, and reproducibility of their findings (Sallou, Durieux, and Panichella 2024). Researchers must openly discuss these limitations and explain how their impact was mitigated. These limitations are relative to current LLM capabilities and tool architectures; speculating about future improvements is beyond the scope of a paper’s limitation section. Nevertheless, risk management and threat mitigation **should** be planned during study design, not as an afterthought.

## Recommendations

Researchers **must** clearly present the limitations of their work without defensiveness or obfuscation. These limitations may concern external, internal, and construct validity; reliability and reproducibility; and ethical, regulatory, and environmental concerns.

We follow the standard SE convention of organizing limitations by external, internal, and construct validity, plus reliability (Runeson and Höst 2009; Ralph et al. 2021), extended below with ethical, regulatory, and environmental concerns specific to LLM research. For studies that adopt qualitative analytic methods (the use of LLMs in reflexive qualitative analysis is itself contested, see [*LLMs as Annotators*](../study-types/annotators.md)), researchers **should** use the trustworthiness criteria of credibility, transferability, dependability, and confirmability instead (Guba 1981). When deterministic reproducibility is structurally unattainable (e.g., SaaS-based models with opaque versioning), researchers **should** adopt the same trustworthiness criteria to substantiate dependability and confirmability of findings.

### External Validity.

The primary threats to external validity are:

- *Cross-model transfer limitations*: Results obtained with one LLM or family of LLMs may not generalize to others due to differences in training data, architecture, and post-training procedures (e.g., fine-tuning and reinforcement learning from human feedback); see [*Open LLMs*](../guidelines/open-llm.md) for using an open LLM as a comparison baseline.
- *Configuration sensitivity*: Results may not generalize beyond the specific configuration(s) tested (e.g., decoding parameters, system prompt, or context settings); see [*System and Prompt Design*](../guidelines/design.md) for an overview.
- *Tool-architecture specificity*: Tools built around vendor-specific APIs or features (e.g., function calling, structured output, or context-window size) may not transfer to other models without substantial re-engineering (see [*System and Prompt Design*](../guidelines/design.md)).
- *Limited domain coverage*: Studies often focus on a narrow set of programming languages, task types, or application domains, limiting generalizability to other SE contexts.
- *Limited participant and rater diversity*: Study participants (e.g., developers) and human raters validating LLM outputs may not represent the broader population in terms of expertise, geographic location, or cultural background (see [*Human Validation*](../guidelines/human-validation.md) for guidance on rater diversity in value-laden constructs).
- *Research-to-practice gap*: Developers using the same tools outside researcher-supervised conditions may obtain results that differ from those reported in the study.
- *Cross-time instability*: Performance of proprietary models can change over time, leading to non-generalizable study outcomes (Chen, Zaharia, and Zou 2024; Li et al. 2024) (see [*Version and Configuration*](../guidelines/model-version.md) for version and fingerprint reporting that enables tracking such drift).

Generalizability is particularly critical for proprietary and non-deterministic systems whose behavior is subject to drift (i.e., silent changes in model output over time). Researchers **must** discuss the limitations and mitigations of external validity. Mitigations include *triangulation* across multiple models (e.g., proprietary and open), independent datasets, and complementary metrics; *sensitivity analysis* that varies LLM configurations, prompts, architecture decisions, datasets, and where applicable participant backgrounds; and performing *longitudinal re-runs* (see *Reliability & Reproducibility* below), which also helps detect cross-time instability.

### Internal Validity.

The primary threats to internal validity are:

- *Data leakage and contamination*: Inter-dataset duplication can produce training-evaluation overlap, yielding overly optimistic results (see [*Benchmarks and Metrics*](../guidelines/benchmarks.md)).
- *Evaluation data entering model-improvement pipelines*: Evaluation samples can unintentionally feed retraining or fine-tuning, especially in longitudinal studies involving LLMs.
- *Incomplete architecture, prompt, or pipeline reporting*: Undisclosed components introduce hidden confounders (see [*System and Prompt Design*](../guidelines/design.md)).

As transparency on training data is limited for LLMs, researchers **must** discuss potential data leakage effects and their impact on results. Concrete mitigations for contamination (e.g., post-cutoff benchmark construction, held-out subsets, canary strings) are discussed in [*Benchmarks and Metrics*](../guidelines/benchmarks.md).

### Construct Validity.

The primary threats to construct validity are:

- *Metric-construct mismatch*: Traditional metrics such as BLEU or ROUGE may miss SE-specific aspects such as functional correctness or behavioral equivalence (see [*Benchmarks and Metrics*](../guidelines/benchmarks.md)).
- *Construct under-specification*: If a construct lacks an operational definition, neither automated metrics nor human raters can apply it consistently.
- *Reliability without validity*: High inter-rater or inter-model agreement does not imply that the measurement captures the intended construct; a reliable LLM can be reliably inaccurate (see [*Human Validation*](../guidelines/human-validation.md)).
- *Benchmark scope limitations*: Benchmarks commonly ignore runtime behaviors, security implications, readability, testability, and maintainability, yielding results that may not transfer to realistic development settings.
- *Capability confounding*: Benchmark performance can blend the target capability with unrelated capabilities such as output format compliance, instruction following, or prompt format sensitivity, inflating apparent scores (see [*Benchmarks and Metrics*](../guidelines/benchmarks.md)).
- *Over-reliance on benchmark-specific metrics*: Optimizing for a single benchmark may produce dataset-specific shortcuts that pass the benchmark without exhibiting the capability it was designed to test, overstating real-world utility.
- *Prompt sensitivity*: Small changes in instructions, formatting, or in-context examples can substantially shift what the LLM appears to measure, making the operationalized construct unstable across prompt variants (see [*System and Prompt Design*](../guidelines/design.md)).
- *Judge biases*: LLM and human judges exhibit systematic biases such as position bias, verbosity bias, and preferences for richly formatted or citation-rich outputs regardless of correctness (see [*Human Validation*](../guidelines/human-validation.md)).

If constructs are based on subjective interpretations, purely automated metrics are insufficient. Researchers **must** discuss how they ensured quality of subjective results, similarly to qualitative research. The primary mitigation is *human validation* of subjective constructs following quality criteria known from qualitative research (see [*Human Validation*](../guidelines/human-validation.md)).

### Reliability & Reproducibility.

The primary threats to reliability and reproducibility are:

- *Non-deterministic outputs*: Identical prompts and configurations can yield different outputs across runs due to factors such as floating-point arithmetic, batching, and stochastic decoding strategies.
- *Infrastructure dependence*: Results may vary depending on the hardware, software stack, and hosting environment used; vendor-imposed quotas, throttling, or pricing changes can further prevent re-running experiments at the original scale, making exact replication challenging across different infrastructure setups.
- *Resource inequality*: LLM research is resource-intensive and remains predominantly in the domain of private companies or well-funded research institutions (Schwartz et al. 2020; Ahmed, Wahed, and Thompson 2023), excluding researchers from under-resourced institutions.

Researchers **must** discuss the measures taken to increase reliability and reproducibility. However, non-deterministic reproducibility is not inherently disqualifying. The trustworthiness criteria introduced above apply particularly to SaaS-based LLM research, where providers frequently deprecate model versions without guaranteeing stable behavior. Mitigations include providing *replication packages* that cover prompt and architecture specifications, model outputs, and representative examples for partial replicability (ideally accompanied by an implementation using an open model for long-term stability), and performing *longitudinal re-runs* with statistical analyses. When deterministic reproduction is structurally impossible, researchers **should** consider *methodological trustworthiness measures* such as triangulation, reflexivity, audit trails, and peer debriefing as complementary measures.

### Ethical & Regulatory Boundaries.

The primary concerns for ethical and regulatory matters are:

- *Use of sensitive or proprietary data*: Studies involving proprietary code, confidential business data, or personally identifiable information may face restrictions on data sharing that limit reproducibility.
- *Jurisdictional obligations*: Data protection regulations such as GDPR or CCPA and institutional policies may impose constraints on data collection, processing, and sharing in LLM-based studies.
- *Implicit model bias*: Especially for qualitative research, LLMs might “*reinforce dominant paradigms and biases*” and “*identify, replicate and reinforce dominant language and patterns*” (Jowsey et al. 2025) (see [*Human Validation*](../guidelines/human-validation.md)).

Studies involving sensitive data **must** discuss data governance mechanisms tailored toward LLM environments, compliant with applicable jurisdictional obligations. If applicable, researchers **should** discuss how model biases potentially impact the study outcomes and how those biases were evaluated.

### Environmental & Sustainability Constraints.

The primary environmental and sustainability concerns are:

- *Energy consumption*: With growing model size, the environmental impact of experiments with LLMs increases, and the substantial energy costs of LLM experiments warrant consideration in study design (Strubell, Ganesh, and McCallum 2019).
- *Trade-off between repetition and sustainability*: Repeating experiments increases reliability but also energy consumption, requiring trade-offs during study design.

Researchers **should** justify the LLM’s resource consumption against the benefits over traditional approaches. Mitigations include *energy preservation* and *cost accounting*. *Energy preservation* involves selecting smaller or newer, less resource-intensive models and applying techniques such as input/output token reduction, model pruning, quantization, or knowledge distillation (Mitu and Mitu 2024) where feasible. Carbon footprint estimation is desirable, but still difficult. *Cost accounting* tracks resource consumption by reporting tokens, service costs, or hardware specifications.

## Examples

Sallou, Durieux, and Panichella (2024) catalog three categories of LLM-specific threats to validity (i.e., closed-source models, implicit data leakage, and reproducibility) and pair each with concrete mitigation strategies (e.g., versioned model archives, metamorphic test data, multiple replication runs with variability metrics, and detailed execution metadata) (Sallou, Durieux, and Panichella 2024). Du et al. (2024) pair each threat in their *ClassEval* evaluation with a concrete mitigation: manually constructing the benchmark with multiple annotators to limit data leakage, piloting prompts on held-out tasks to control for prompt sensitivity, and reporting greedy-decoding results to control for non-determinism.

## Benefits

Transparent reporting of limitations and mitigations helps readers calibrate confidence in the findings, makes explicit which threats were addressed and which remain open, and documents design decisions that other authors can borrow or refine. It also keeps a paper’s claims proportionate to its evidence.

## Challenges

Identifying limitations one is not already aware of is the hardest part of writing a threats section, particularly for methodological threats outside the team’s primary expertise. Publication and reviewing norms can pressure authors to downplay weaknesses, while page limits make exhaustive treatment impractical. Threat lists that recite generic LLM-research issues (e.g., model bias, non-determinism, or contamination) without showing how each one applies to specific design choices in this study leave reviewers unable to tell which risks actually applied.

The threats to validity framework itself is contested within SE. Verdecchia et al. (2023) argue that threats sections too often read as “*laundry-lists*”, Lago et al. (2024) corroborated this empirically across a decade of ICSE Distinguished Paper Award winners, and Robillard et al. (2024) argue for refocusing the discussion on study design trade-offs rather than the standard validity categories.

## Study Types

Researchers **must** follow this guideline for all study types. Transparently reporting limitations and mitigations is a universal requirement, but specific concerns vary by study type. For [*LLMs as Annotators*](../study-types/annotators.md), researchers **must** discuss potential biases in label assignment, label reliability limitations, and sensitivity of annotations to prompt wording and model choice. For [*LLMs as Judges*](../study-types/judges.md), researchers **must** address measurement validity concerns, known biases such as position bias or verbosity bias, and the extent to which LLM judgments align with human expert assessments. For [*LLMs for Synthesis*](../study-types/synthesis.md), researchers **must** discuss the risk of contextual misinterpretation, potential loss of nuance in summarized or aggregated outputs, and reflexivity limitations inherent in using an LLM for qualitative interpretation. For [*LLMs as Subjects*](../study-types/subjects.md), researchers **must** discuss the fundamental inability of LLMs to truly simulate human behavior, the risk of stereotype amplification, and the limited ecological validity of simulated responses. For [*Studying LLM Usage*](../study-types/usage.md), researchers **must** discuss generalizability constraints across different tools and user populations, and acknowledge how observed usage patterns may not transfer to other contexts. For [*LLMs for Tools*](../study-types/tools.md), researchers **must** discuss replicability constraints arising from dependencies on commercial models, the impact of model updates on tool behavior, and limitations of the evaluation setup. For [*Benchmarking LLMs*](../study-types/benchmarks.md), researchers **must** discuss potential data contamination, benchmark scope limitations, capability confounding, and the extent to which benchmark performance generalizes to real-world tasks.

## Advice for Reviewers

Reviewers should verify that the limitation section is comprehensive and appropriate for the specific study type, checking that: (1) limitations address the specific threats relevant to the study type (e.g., label reliability for annotation studies, simulation fidelity for studies using LLMs as subjects); (2) mitigations are concrete and correspond to identified limitations rather than being generic statements; (3) the impact of LLM non-determinism on findings is discussed; (4) generalizability constraints, across models, configurations, time periods, and populations, are acknowledged. When important limitations are missing, reviewers should request they be added. The absence of a limitation section, or one that is formulaic or insufficiently specific, is a more serious concern than any individual missing limitation and may warrant a major revision.

## See Also

- [Report Model Version, Configuration, and Customizations](../guidelines/model-version.md): Authors can re-run with different models or configurations to check whether the results depend on those specific choices.
- [Report System and Prompt Design](../guidelines/design.md): Triangulation across architectures and prompts is one mitigation strategy.
- [Report Session Traces](../guidelines/traces.md): Stored session traces serve as a baseline against which authors can monitor LLM behavior drift over time.
- [Use Suitable Baselines, Benchmarks, and Metrics](../guidelines/benchmarks.md): Benchmark and metric choices are one source of construct-validity threats authors must discuss.
- [Use an Open LLM as a Baseline](../guidelines/open-llm.md): An open LLM baseline mitigates cross-model transfer concerns by providing an independently reproducible comparison.
- [Use Human Validation for LLM Outputs](../guidelines/human-validation.md): When automated metrics cannot validly measure a construct, human validation is an alternative.

## References

Ahmed, Nur, Muntasir Wahed, and Neil C. Thompson. 2023. “The Growing Influence of Industry in AI Research.” *Science* 379 (6635): 884–86. <https://doi.org/10.1126/science.ade2420>.

Chen, Lingjiao, Matei Zaharia, and James Zou. 2024. “How Is ChatGPT’s Behavior Changing over Time?” *Harvard Data Science Review* 6 (2). <https://doi.org/10.1162/99608f92.5317da47>.

Du, Xueying, Mingwei Liu, Kaixin Wang, Hanlin Wang, Junwei Liu, Yixuan Chen, Jiayi Feng, Chaofeng Sha, Xin Peng, and Yiling Lou. 2024. “Evaluating Large Language Models in Class-Level Code Generation.” In *Proceedings of the 46th IEEE/ACM International Conference on Software Engineering, ICSE 2024, Lisbon, Portugal, April 14-20, 2024*, 81:1–13. ACM. <https://doi.org/10.1145/3597503.3639219>.

Guba, Egon G. 1981. “Criteria for Assessing the Trustworthiness of Naturalistic Inquiries.” *ECTJ* 29 (2): 75–91. <https://doi.org/10.1007/BF02766777>.

Jowsey, Tanisha, Virginia Braun, Victoria Clarke, Deborah Lupton, and Michelle Fine. 2025. “We Reject the Use of Generative Artificial Intelligence for Reflexive Qualitative Research.” *Qualitative Inquiry*. <https://doi.org/10.1177/10778004251401851>.

Lago, Patricia, Per Runeson, Qunying Song, and Roberto Verdecchia. 2024. “Threats to Validity in Software Engineering - Hypocritical Paper Section or Essential Analysis?” In *Proceedings of the 18th ACM/IEEE International Symposium on Empirical Software Engineering and Measurement, ESEM 2024, Barcelona, Spain, October 24-25, 2024*, edited by Xavier Franch, Maya Daneva, Silverio Martı́nez-Fernández, and Luigi Quaranta, 314–24. ACM. <https://doi.org/10.1145/3674805.3686691>.

Li, David, Kartik Gupta, Mousumi Bhaduri, Paul Sathiadoss, Sahir Bhatnagar, and Jaron Chong. 2024. “Comparing GPT-3.5 and GPT-4 Accuracy and Drift in Radiology Diagnosis Please Cases.” *Radiology* 310 (1): e232411. <https://doi.org/10.1148/radiol.232411>.

Mitu, Narcis Eduard, and George Teodor Mitu. 2024. “The Hidden Cost of AI: Carbon Footprint and Mitigation Strategies.” *Revista de Stiinte Politice. Revue Des Sciences Politiques* 84: 9–16. <https://doi.org/10.2139/ssrn.5036344>.

Ralph, Paul, Nauman bin Ali, Sebastian Baltes, Domenico Bianculli, Jessica Diaz, Yvonne Dittrich, Neil Ernst, et al. 2021. “Empirical Standards for Software Engineering Research.” <https://arxiv.org/abs/2010.03525>.

Robillard, Martin P., Deeksha M. Arya, Neil A. Ernst, Jin L. C. Guo, Maxime Lamothe, Mathieu Nassif, Nicole Novielli, Alexander Serebrenik, Igor Steinmacher, and Klaas-Jan Stol. 2024. “Communicating Study Design Trade-Offs in Software Engineering.” *ACM Trans. Softw. Eng. Methodol.* 33 (5): 112:1–10. <https://doi.org/10.1145/3649598>.

Runeson, Per, and Martin Höst. 2009. “Guidelines for Conducting and Reporting Case Study Research in Software Engineering.” *Empir. Softw. Eng.* 14 (2): 131–64. <https://doi.org/10.1007/S10664-008-9102-8>.

Sallou, June, Thomas Durieux, and Annibale Panichella. 2024. “Breaking the Silence: The Threats of Using LLMs in Software Engineering.” In *Proceedings of the 2024 ACM/IEEE 44th International Conference on Software Engineering: New Ideas and Emerging Results, NIER@ICSE 2024, Lisbon, Portugal, April 14-20, 2024*, 102–6. ACM. <https://doi.org/10.1145/3639476.3639764>.

Schwartz, Roy, Jesse Dodge, Noah A. Smith, and Oren Etzioni. 2020. “Green AI.” *Communications of the ACM* 63 (12): 54–63. <https://doi.org/10.1145/3381831>.

Strubell, Emma, Ananya Ganesh, and Andrew McCallum. 2019. “Energy and Policy Considerations for Deep Learning in NLP.” In *Proceedings of the 57th Conference of the Association for Computational Linguistics, ACL 2019, Florence, Italy, July 28- August 2, 2019, Volume 1: Long Papers*, edited by Anna Korhonen, David R. Traum, and Lluı́s Màrquez, 3645–50. Association for Computational Linguistics. <https://doi.org/10.18653/V1/P19-1355>.

Verdecchia, Roberto, Emelie Engström, Patricia Lago, Per Runeson, and Qunying Song. 2023. “Threats to Validity in Software Engineering Research: A Critical Reflection.” *Inf. Softw. Technol.* 164: 107329. <https://doi.org/10.1016/J.INFSOF.2023.107329>.
