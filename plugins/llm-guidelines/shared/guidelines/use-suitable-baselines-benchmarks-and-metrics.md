# Use Suitable Baselines, Benchmarks, and Metrics

> ***Summary***: Researchers **must** justify all benchmark and metric choices in the *paper* and **should** summarize benchmark structure, task types, and limitations. They **should** operationally define the phenomenon being measured, justify the sampling strategy used to select problems for inclusion in the benchmark, isolate the target capability from confounders where possible, and report an error analysis of the observed failures. Where possible, traditional (non-LLM) baselines **should** be used for comparison. Researchers **must** explain in the *paper* why the selected metrics are suitable for the specific study; prior adoption in related work alone does not constitute sufficient justification. They **should** report established metrics to make study results comparable, but can report additional metrics that they consider appropriate. Due to the inherent non-determinism of LLMs, experiments **should** be repeated; the result distribution **should** then be reported using descriptive statistics. If comparing models or tools, researchers **must** use appropriate inferential statistics rather than relying solely on summary statistics. Researchers **should** justify the number of experiment repetitions, for example through a power analysis or by monitoring convergence of descriptive statistics.

## Rationale

Meaningful evaluation requires well-understood, valid measurement instruments. Without justified benchmarks and metrics, claims about LLM performance lack the rigor needed for scientific comparison and cumulative progress. A *benchmark* is a “standard tool for the competitive evaluation and comparison of competing systems or components according to specific characteristics, such as performance, dependability, or security” (Kistowski et al. 2015). “A *metric* is a method, algorithm, or procedure for assigning one or more numbers to a phenomenon” (Ralph et al. 2024). A baseline is a reference point, enabling comparison of LLMs against traditional algorithms with lower computational costs.

## Recommendations

Benchmark and metric selection requires understanding the benchmark tasks, what exactly is being measured, and how it relates to the (often latent) variables researchers actually care about. If one or more metrics or benchmarks are used, researchers:

- **must** briefly justify (in the *paper*) why selected benchmarks and metrics are suitable for the given task or study;
- **must** discuss the reliability and validity (especially construct validity) of selected metrics and benchmarks;
- **should** provide an operational definition of the phenomenon the benchmark is intended to measure (e.g., functional correctness, code maintainability, vulnerability detection), including its scope and any sub-components (Bean et al. 2025);
- **should** summarize the structure and tasks of the selected benchmark(s), including the programming language(s) and descriptive statistics such as the number of contained tasks and test cases;
- **should** describe and justify the sampling strategy used to select problems for inclusion in the benchmark (e.g., function-completion problems in *HumanEval*, GitHub issues in *SWE-bench*, vulnerable functions in *DiverseVul*); if non-probability sampling (e.g., convenience) is used, discuss its implications for the generalizability of conclusions (Baltes and Ralph 2022; Bean et al. 2025);
- **should** discuss the limitations of the selected benchmark(s) (e.g. widely used benchmarks such as *HumanEval* (M. Chen et al. 2021) and *MBPP* (Austin et al. 2021) Python functions assess a very specific part of software development, which is not representative of the full breadth of SE work (Chandra 2025));
- **should** include an example of a task and the corresponding test case(s) to illustrate the structure of the benchmark.

If multiple benchmarks exist for the same task, researchers **should** compare both performance and design choices (task selection, scoring, scope) across benchmarks (Bean et al. 2025). When selecting only a subset of all available benchmarks, researchers **should** use the most specific benchmarks given the context. When adapting an existing benchmark, researchers **should** document what was changed and why, and **should** report performance on both the original and the adapted version where feasible (Bean et al. 2025).

Benchmark scores often confound the target capability with unrelated abilities the task happens to require. For code-generation benchmarks, prompt formatting alone can shift code-translation performance by up to 40% (He et al. 2024; Cao et al. 2026), conflating prompt-format sensitivity with translation skill. More broadly, output-format compliance (e.g., specific JSON schemas or unit-test conventions) and general instruction-following ability are routinely bundled into the score (Bean et al. 2025). Researchers **should** identify which capabilities a benchmark conflates, isolate the target capability where possible (e.g., by reporting per-subtask breakdowns or by adopting benchmarks designed to test the target capability in isolation), and acknowledge remaining confounders as threats to construct validity.

After running a benchmark, researchers **should** perform an error analysis by categorizing the failures observed and reporting the relative frequency of each category. If failures concentrate on inputs that demand abilities other than the target phenomenon (e.g., reading across many files rather than fixing the bug the benchmark targets), this is a construct-validity threat and **should** be reported alongside the primary scores (Bean et al. 2025).

In addition to disclosing data sources and collection dates (see Challenges below), researchers creating or releasing a new benchmark **should** adopt concrete contamination-prevention mechanisms: maintaining a held-out subset of items for ongoing, uncontaminated evaluation; embedding canary strings, that is, unique markers that downstream tools can later search for in model outputs to detect inclusion in training data; and investigating whether the benchmark’s source materials may already appear in common LLM training corpora (Bean et al. 2025; Cao et al. 2026). Researchers using existing benchmarks **should** additionally discuss contamination as a study limitation ([*Limitations and Mitigations*](../guidelines/report-limitations-and-mitigations.md)).

Furthermore, researchers **should** check whether a less resource-intensive approach (e.g., for static analysis tasks or program repair) can serve as a baseline. If so, the LLM or LLM-based tool **should** be compared with such baselines using suitable metrics. Even if LLM-based tools outperform baselines, researchers **should** discuss whether the resources consumed justify the (often marginal) improvements (Menzies 2025).

To compare traditional and LLM-based approaches or different LLM-based tools, researchers **should** report established metrics whenever possible, as this allows secondary research. They can report additional metrics that they consider appropriate. We briefly discuss common metrics in the Examples subsection below. As mentioned, researchers **must** motivate why they chose a certain metric or variant thereof for their particular study. Prior adoption alone does not constitute sufficient justification; researchers **must not** justify metric choices solely by citing their use in prior work.

Due to LLM non-determinism, researchers **should** repeat experiments and report descriptive statistics of model or tool performance (e.g., arithmetic mean, median, confidence intervals, standard deviations) (Agarwal et al. 2021; Bjarnason, Silva, and Monperrus 2026). If comparing models or tools, researchers **must** use appropriate inferential statistics (e.g., hypothesis tests such as the Mann-Whitney U test, McNemar’s test for binary outcomes (Kübler et al. 2026), or bootstrap-based comparisons, along with effect sizes) rather than relying solely on differences in means or other summary statistics. When scoring uses ratings that vary across raters or runs (e.g., human raters, LLM-as-judge), researchers **should** report the distribution of ratings per item rather than only aggregated point estimates or exact-match agreement, since aggregation can mask systematic disagreement (Bean et al. 2025).

The number of required repetitions depends on factors such as the study type, the variability of the task, and the desired precision of estimates. As with sample sizes for human validation ([*Human Validation*](../guidelines/use-human-validation-for-llm-outputs.md)), researchers **should** justify their chosen number of repetitions, for example, through a power analysis (Cohen 1992; Bjarnason, Silva, and Monperrus 2026) or by monitoring the convergence of descriptive statistics across incremental runs (Blackwell, Barry, and Cohn 2024). A pilot study can help estimate the expected variability and inform this decision.

From a measurement perspective, researchers **should** reflect on the theories, values, and measurement models on which the benchmarks and metrics they have selected for their study are based. For example, the phenomena labeled “bugs” in a large open dataset of software bugs are according to a certain theory of what constitutes a bug, and from the values and perspectives of the people who labeled the dataset. Reflecting on the context in which these labels were assigned and discussing whether and how the labels generalize to a new study context is crucial.

Researchers building or releasing new SE benchmarks **should** consult operational checklists. Cao et al. (2026) (Cao et al. 2026) provide *HOW2BENCH*, a 55-item checklist covering benchmark design, construction, evaluation, analysis, and release. Bean et al. (2025) (Bean et al. 2025) provide a complementary domain-agnostic checklist organized around the construct-validity recommendations summarized above.

## Examples

### Common Metrics:

Two common metrics used for generation tasks are *BLEU-N* and *pass@k*. *BLEU-N* (Papineni et al. 2002) was originally developed for evaluating machine translation quality by measuring n-gram precision between a candidate and reference text, ranging from$0$ (dissimilar) to$1$ (similar). It has been widely adopted in SE for code generation tasks, though its validity in this context is debatable: n-gram overlap does not capture functional correctness, and syntactically different code can be semantically equivalent (see Challenges below). Code-specific variations such as *CodeBLEU* (Ren et al. 2020) and *CrystalBLEU* (Eghbali and Pradel 2022) attempt to address these limitations by introducing additional heuristics such as AST matching.

The metric *pass@k* reports the likelihood that a model correctly completes a code snippet at least once within$k$ attempts. Originally introduced as *success rate at B* by Kulal et al. (2019) (Kulal et al. 2019) and popularized by M. Chen et al. (2021) (M. Chen et al. 2021), it ranges from$0$ (no correct solution in$k$ tries) to$1$ (at least one correct solution), with correctness typically defined by passing test cases.

The *pass@k* metric is defined as:

$\text{pass@}k = 1 - \frac{\binom{n-c}{k}}{\binom{n}{k}}\,, \text{where:}$

-$n$ is the total number of generated samples per prompt,
-$c$ is the number of correct samples among$n$, and
-$k$ is the number of samples drawn.

The choice of$k$ depends on the downstream task: *pass@1* is critical for single-suggestion scenarios such as code completion, while higher$k$ values (e.g.,$2$,$5$,$10$) assess multi-attempt capability and are commonly reported in technical reports of recent code LLMs (e.g., Code Llama (Rozière et al. 2023), DeepSeek-Coder (Guo et al. 2024), Qwen2.5-Coder (Hui et al. 2024), StarCoder (Li et al. 2023)). However, *pass@k* is not a universal metric suitable for all generation tasks. It requires a binary notion of correctness, making the metric appropriate for code synthesis evaluated via unit tests, but unsuitable for open-ended generation tasks such as comment generation, where multiple valid outputs exist.

A complementary perspective from industry practice is *pass<sup>k</sup>* (also written *pass^k*), which measures the probability that *all*$k$ trials succeed rather than *at least one* (Anthropic 2025). While *pass@k* increases with$k$, *pass<sup>k</sup>* decreases, making it useful for assessing reliability in deployment scenarios where consistent success matters (e.g., customer-facing agents).

If a study evaluates an LLM-based tool for supporting humans, a relevant metric is the acceptance rate, meaning the ratio of all accepted artifacts (e.g., test cases, code snippets) in relation to all artifacts that were generated and presented to the user. Another way of evaluating LLM-based tools is calculating inter-model agreement, which reveals how much a tool’s performance depends on specific models and versions. Metrics used to measure inter-model agreements include general agreement (percentage), *Cohen’s kappa*, and *Krippendorff’s$\alpha$* (see [*Human Validation*](../guidelines/use-human-validation-for-llm-outputs.md) for recommended thresholds and best practices for measuring agreement).

Common problem types for LLM-based studies are classification, recommendation, and generation, each requiring different metrics (Hou et al. 2024). Hu et al. (2025) (Hu et al. 2025) categorized 191 LLM benchmarks by SE task, providing a valuable reference. For an overview of code foundation models, agents, and their evaluation, see Yang et al. (2025) (Yang et al. 2025). From a practitioner perspective, Anthropic (2025) (Anthropic 2025) categorize evaluation approaches for LLM-based agents into code-based graders (e.g., test suite execution, static analysis), model-based graders (e.g., rubric-scored LLM judgments), and human graders. This taxonomy may help researchers systematically design evaluation strategies for agent-based tools. Common metrics include *BLEU*, *pass@k*, *Accuracy@k*, and *Exact Match* for generation; *Mean Reciprocal Rank* for recommendation; and *Precision*, *Recall*, *F1-score*, and *Accuracy* for classification.

### Benchmark Examples:

Benchmarks used for code generation include *HumanEval* (available on [GitHub](https://github.com/openai/human-eval)) (M. Chen et al. 2021), *MBPP* (available on [Hugging Face](https://huggingface.co/datasets/google-research-datasets/mbpp)) (Austin et al. 2021), *ClassEval* (available on [GitHub](https://github.com/FudanSELab/ClassEval)) (Du et al. 2023), *LiveCodeBench* (available on [GitHub](https://github.com/LiveCodeBench/LiveCodeBench)) (Jain et al. 2024), and *SWE-bench* (available on [GitHub](https://github.com/swe-bench/SWE-bench)) (Jimenez et al. 2024). An example of a code translation benchmark is *TransCoder* (Rozière et al. 2020) (available on [GitHub](https://github.com/facebookresearch/CodeGen)).

Most benchmarks focus on generation tasks, but benchmarks for classification and recommendation also exist. For classification, *DiverseVul* (available on [GitHub](https://github.com/wagner-group/diversevul)) (Y. Chen et al. 2023) provides vulnerable and non-vulnerable functions evaluated using standard classification metrics. For recommendation, *CodeSearchNet* (available on [GitHub](https://github.com/github/CodeSearchNet)) (Husain et al. 2019) contains code-documentation pairs evaluated using *Mean Reciprocal Rank*.

## Benefits

Benchmarks and metrics improve reproducibility and comparability across studies, leading to faster improvements in the cumulative body of knowledge. It is simply easier to assess a new system against one or a few benchmarks than hundreds of competing systems, and when most systems are assessed against the same benchmarks and metrics, we can see which approaches work best (at least, on those benchmarks). This comparison enables progress tracking; for example, when researchers iteratively improve a new LLM-based tool and test it against benchmarks after substantial changes. For practitioners, leaderboards (published benchmark results of models) support selecting models for downstream tasks. Meanwhile, baselines help us understand just how much LLMs improve performance over non-LLM-enabled alternatives.

## Challenges

Computer scientists have long used oversimplified, unvalidated metrics (Ralph and Tempero 2018) (e.g., lines of code, CPU time) as proxies for complex, multidimensional latent variables (e.g., system size, environmental sustainability). Unlike fields such as psychology where measurement theory has a longer tradition (Borsboom 2005), many AI metrics and benchmarks lack both theoretical underpinnings and empirical validation of their construct, measurement, and ecological validity.

These validity issues are widespread, not isolated. In a survey of 572 code benchmarks released between 2014 and 2025, Cao et al. (2026) (Cao et al. 2026) found that 84.2% did not consider test-suite coverage when constructing test cases, 64.0% reported single-pass evaluations without controlling for randomness, and 82.5% did not address data contamination. Bean et al. (2025) (Bean et al. 2025) reported comparable patterns in a parallel review of 445 LLM benchmarks from ML and NLP venues. As a result, model performance on these benchmarks can reflect benchmark artifacts rather than the capability the benchmark claims to test.

For example, *pass@k* is intended to measure a model’s *functional correctness*, that is, its ability to generate code that produces the expected output for a given specification. However, functional correctness is only one dimension of code quality. *pass@k* does not capture maintainability, readability, security, or efficiency of the generated code, all of which are critical for downstream use. Furthermore, “correctness” is defined entirely by test suites, whose coverage is itself unvalidated: a solution that passes all provided tests may still be incorrect for untested inputs. Whether a test suite adequately operationalizes correctness for a given task is a subjective judgment that is rarely examined.

Similarly, *HumanEval* is intended to measure a model’s ability to *synthesize short Python functions from docstring specifications*. This operationalizes a narrow slice of “code generation ability”: it covers neither multi-file tasks, nor debugging, nor the use of existing codebases. These tasks dominate real-world software engineering (Chandra 2025; Yang et al. 2025). Notably, neither *pass@k* nor *HumanEval* has undergone rigorous empirical validation of its construct validity; their widespread adoption rests on face validity and convenience rather than on evidence that they reliably measure what researchers intend them to measure (Cao et al. 2026). *HumanEval* also contains implementation, documentation, and test-case bugs in its original release, which directly affect score interpretation (Liu et al. 2023); comparable issues have been documented in other widely-used code benchmarks (Cao et al. 2026).

Benchmarks and metrics also have generalizability problems. Prominent LLM benchmarks such as *HumanEval* and *MBPP* use Python, so researchers can optimize for Python’s idiosyncrasies, creating illusory improvements that do not generalize to other languages. Similarly, the metric *BLEU-N* is a syntactic metric, so code can score highly without being executable. The metric *Exact Match*, meanwhile, does not account for functional equivalence of syntactically different code. Both *BLEU-N* and *Exact Match* are influenced by code formatting, which confounds their intended use.

Execution-based metrics such as *pass@k* directly evaluate correctness by running test cases, but they require a setup with an execution environment. When researchers observe unexpected values for certain metrics, the specific results should be investigated in more detail to uncover potential problems.

Finally, benchmark data contamination, where the benchmark itself is part of the training data, may lead to artificially high performance if the model remembers the solution from the training data rather than actually solving the task based on the input data (Xu et al. 2024). Therefore, for proprietary LLMs that do not release their training data, researchers **should** consider using human validation, curating new data, or refactoring existing data (Xu et al. 2024).

To mitigate contamination, researchers can create new benchmark datasets by collecting data after a specified cutoff date; researchers **must** disclose data sources and collection dates for each release. However, this temporal approach requires continuous updates as new models may include the benchmark in future training data. Alternatively, keeping the benchmark private prevents inclusion in training sets, but requires trust in the benchmark creator and a system to execute it without leaking data. Researchers can also evaluate how contaminated their benchmark is (Choi et al. 2025).

## Study Types

This guideline **must** be followed for all study types that automatically evaluate the performance of LLMs or LLM-based tools. The design of a benchmark and the selection of appropriate metrics are highly dependent on the specific study type and research goal. Recommending specific metrics for specific study types is beyond the scope of these guidelines, but Hu et al. (2025) provide a good overview of existing metrics for evaluating LLMs (Hu et al. 2025).

For [*Benchmarking LLMs*](../study-types/benchmarking-llms-for-software-engineering-tasks.md), this guideline is of primary importance: researchers **must** use established benchmarks or rigorously justify the creation of new ones, **must** report standard metrics to enable cross-study comparison, and **should** report an error analysis alongside the primary scores so that readers can assess whether reported gains reflect the target capability or other abilities the task happens to require. For [*LLMs as Annotators*](../study-types/llms-as-annotators.md), the research goal might be to assess which model comes close to a ground truth dataset created by human annotators. Especially for open annotation tasks, selecting suitable metrics to compare LLM-generated and human-generated labels is important. In general, annotation tasks can vary widely. Are multiple labels allowed for the same sequence? Are the available labels predefined, or should the LLM generate a set of labels independently? Due to this task dependence, researchers **must** justify their metric choice, explaining what aspects of the task it captures together with known limitations. For [*LLMs for Tools*](../study-types/llms-for-new-software-engineering-tools.md), researchers **should** benchmark the tool against suitable baselines using appropriate metrics that capture the tool’s intended contribution. For [*LLMs as Judges*](../study-types/llms-as-judges.md), researchers **should** report inter-rater agreement metrics and validity measures to demonstrate the reliability and quality of LLM judgments. For [*LLMs for Synthesis*](../study-types/llms-for-synthesis.md), researchers **should** specify metrics for comparing synthesized outputs (e.g., coverage, faithfulness) and justify their appropriateness for the synthesis task. For [*Studying LLM Usage*](../study-types/studying-llm-usage-in-software-engineering.md), researchers **should** justify the measurement instruments and metrics used for studying LLM usage patterns, including any survey scales or behavioral measures. For [*LLMs as Subjects*](../study-types/llms-as-subjects.md), researchers **should** compare simulated and real human responses using appropriate metrics to assess simulation fidelity. If researchers assess a well-established task such as code generation, they **should** report standard metrics such as *pass@k* and compare the performance between models. If non-standard metrics are used, researchers **must** state their reasoning.

## Advice for Reviewers

Reviewers should expect manuscripts to:

1. clearly identify the constructs or variables the study aims to measure (e.g., LLM performance, quality of generated code), including independent, dependent, and control variables;
2. present their measurement model, i.e., which metrics, benchmarks, or baselines are used and how they relate to the target constructs;
3. justify the selection of any metrics, benchmarks, and baselines used;
4. discuss *in detail* the assumptions, reliability, and validity (*especially construct validity*) of each benchmark and metric;
5. articulate any limitations regarding construct and measurement validity.

As with other guidelines, missing information about baselines or metrics is typically a revision request. However, vague descriptions that conflate broad concerns (e.g., effectiveness, quality) with specific counting methods should be questioned. Ubiquity of a benchmark or metric does not imply validity or appropriateness for a given context. Manuscripts should convey a solid understanding of construct and measurement validity by explaining and justifying their measurement models.

## See Also

- [Use an Open LLM as a Baseline](../guidelines/use-an-open-llm-as-a-baseline.md): Using an open LLM as a baseline supports reproducible benchmark comparisons across studies.
- [Use Human Validation for LLM Outputs](../guidelines/use-human-validation-for-llm-outputs.md): Human evaluation captures aspects of LLM outputs that automated metrics cannot measure.
- [Report Limitations and Mitigations](../guidelines/report-limitations-and-mitigations.md): Every benchmark and metric choice carries construct-validity threats that authors must discuss.

## References

Agarwal, Rishabh, Max Schwarzer, Pablo Samuel Castro, Aaron C. Courville, and Marc G. Bellemare. 2021. “Deep Reinforcement Learning at the Edge of the Statistical Precipice.” In *Advances in Neural Information Processing Systems 34: Annual Conference on Neural Information Processing Systems 2021, NeurIPS 2021, December 6-14, 2021, Virtual*, edited by Marc’Aurelio Ranzato, Alina Beygelzimer, Yann N. Dauphin, Percy Liang, and Jennifer Wortman Vaughan, 29304–20. <https://proceedings.neurips.cc/paper/2021/hash/f514cec81cb148559cf475e7426eed5e-Abstract.html>.

Anthropic. 2025. “Demystifying Evals for AI Agents.” <https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents>.

Austin, Jacob, Augustus Odena, Maxwell I. Nye, Maarten Bosma, Henryk Michalewski, David Dohan, Ellen Jiang, et al. 2021. “Program Synthesis with Large Language Models.” *CoRR* abs/2108.07732. <https://arxiv.org/abs/2108.07732>.

Baltes, Sebastian, and Paul Ralph. 2022. “Sampling in Software Engineering Research: A Critical Review and Guidelines.” *Empir. Softw. Eng.* 27 (4): 94. <https://doi.org/10.1007/s10664-021-10072-8>.

Bean, Andrew M., Ryan Othniel Kearns, Angelika Romanou, Franziska Sofia Hafner, Harry Mayne, Jan Batzner, Negar Foroutan, et al. 2025. “Measuring What Matters: Construct Validity in Large Language Model Benchmarks.” In *Advances in Neural Information Processing Systems 38: Annual Conference on Neural Information Processing Systems 2025, NeurIPS 2025, Datasets and Benchmarks Track*. <https://arxiv.org/abs/2511.04703>.

Bjarnason, Bjarni Haukur, André Silva, and Martin Monperrus. 2026. “On Randomness in Agentic Evals.” *CoRR* abs/2602.07150. <https://doi.org/10.48550/ARXIV.2602.07150>.

Blackwell, Robert E., Jon Barry, and Anthony G. Cohn. 2024. “Towards Reproducible LLM Evaluation: Quantifying Uncertainty in LLM Benchmark Scores.” *CoRR* abs/2410.03492. <https://doi.org/10.48550/ARXIV.2410.03492>.

Borsboom, Denny. 2005. *Measuring the Mind: Conceptual Issues in Contemporary Psychometrics*. Cambridge University Press. <https://doi.org/10.1017/CBO9780511490026>.

Cao, Jialun, Yuk-Kit Chan, Zixuan Ling, Wenxuan Wang, Shuqing Li, Mingwei Liu, Ruixi Qiao, et al. 2026. “Rigor, Reliability, and Reproducibility Matter: A Decade-Scale Survey of 572 Code Benchmarks.” *CoRR* abs/2501.10711. <https://arxiv.org/abs/2501.10711>.

Chandra, Satish. 2025. “Benchmarks for AI in Software Engineering (BLOG@CACM).” <https://cacm.acm.org/blogcacm/benchmarks-for-ai-in-software-engineering/>.

Chen, Mark, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pondé de Oliveira Pinto, Jared Kaplan, Harri Edwards, et al. 2021. “Evaluating Large Language Models Trained on Code.” *CoRR* abs/2107.03374. <https://arxiv.org/abs/2107.03374>.

Chen, Yizheng, Zhoujie Ding, Lamya Alowain, Xinyun Chen, and David A. Wagner. 2023. “DiverseVul: A New Vulnerable Source Code Dataset for Deep Learning Based Vulnerability Detection.” In *Proceedings of the 26th International Symposium on Research in Attacks, Intrusions and Defenses, RAID 2023, Hong Kong, China, October 16-18, 2023*, 654–68. ACM. <https://doi.org/10.1145/3607199.3607242>.

Choi, Hyeong Kyu, Maxim Khanov, Hongxin Wei, and Yixuan Li. 2025. “How Contaminated Is Your Benchmark? Quantifying Dataset Leakage in Large Language Models with Kernel Divergence.” *CoRR* abs/2502.00678. <https://doi.org/10.48550/ARXIV.2502.00678>.

Cohen, Jacob. 1992. “A Power Primer.” *Psychological Bulletin* 112 (1): 155–59. <https://doi.org/10.1037/0033-2909.112.1.155>.

Du, Xueying, Mingwei Liu, Kaixin Wang, Hanlin Wang, Junwei Liu, Yixuan Chen, Jiayi Feng, Chaofeng Sha, Xin Peng, and Yiling Lou. 2023. “ClassEval: A Manually-Crafted Benchmark for Evaluating LLMs on Class-Level Code Generation.” *CoRR* abs/2308.01861. <https://doi.org/10.48550/ARXIV.2308.01861>.

Eghbali, Aryaz, and Michael Pradel. 2022. “CrystalBLEU: Precisely and Efficiently Measuring the Similarity of Code.” In *37th IEEE/ACM International Conference on Automated Software Engineering, ASE 2022*, 28:1–12. ACM. <https://doi.org/10.1145/3551349.3556903>.

Guo, Daya, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, et al. 2024. “DeepSeek-Coder: When the Large Language Model Meets Programming - the Rise of Code Intelligence.” *CoRR* abs/2401.14196. <https://doi.org/10.48550/ARXIV.2401.14196>.

He, Jia, Mukund Rungta, David Koleczek, Arshdeep Sekhon, Franklin X. Wang, and Sadid Hasan. 2024. “Does Prompt Formatting Have Any Impact on LLM Performance?” *CoRR* abs/2411.10541. <https://doi.org/10.48550/ARXIV.2411.10541>.

Hou, Xinyi, Yanjie Zhao, Yue Liu, Zhou Yang, Kailong Wang, Li Li, Xiapu Luo, David Lo, John Grundy, and Haoyu Wang. 2024. “Large Language Models for Software Engineering: A Systematic Literature Review.” *ACM Trans. Softw. Eng. Methodol.* 33 (8): 220:1–79. <https://doi.org/10.1145/3695988>.

Hu, Xing, Feifei Niu, Junkai Chen, Xin Zhou, Junwei Zhang, Junda He, Xin Xia, and David Lo. 2025. “Assessing and Advancing Benchmarks for Evaluating Large Language Models in Software Engineering Tasks.” *CoRR* abs/2505.08903. <https://doi.org/10.48550/ARXIV.2505.08903>.

Hui, Binyuan, Jian Yang, Zeyu Cui, Jiaxi Yang, Dayiheng Liu, Lei Zhang, Tianyu Liu, et al. 2024. “Qwen2.5-Coder Technical Report.” *CoRR* abs/2409.12186. <https://doi.org/10.48550/ARXIV.2409.12186>.

Husain, Hamel, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, and Marc Brockschmidt. 2019. “CodeSearchNet Challenge: Evaluating the State of Semantic Code Search.” *CoRR* abs/1909.09436. <http://arxiv.org/abs/1909.09436>.

Jain, Naman, King Han, Alex Gu, Wen-Ding Li, Fanjia Yan, Tianjun Zhang, Sida Wang, Armando Solar-Lezama, Koushik Sen, and Ion Stoica. 2024. “LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code.” *CoRR* abs/2403.07974. <https://doi.org/10.48550/ARXIV.2403.07974>.

Jimenez, Carlos E., John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik R. Narasimhan. 2024. “SWE-bench: Can Language Models Resolve Real-World Github Issues?” In *The Twelfth International Conference on Learning Representations, ICLR 2024, Vienna, Austria, May 7-11, 2024*. OpenReview.net. <https://openreview.net/forum?id=VTF8yNQM66>.

Kistowski, Jóakim von, Jeremy A. Arnold, Karl Huppler, Klaus-Dieter Lange, John L. Henning, and Paul Cao. 2015. “How to Build a Benchmark.” In *Proceedings of the 6th ACM/SPEC International Conference on Performance Engineering, Austin, TX, USA, January 31 - February 4, 2015*, edited by Lizy K. John, Connie U. Smith, Kai Sachs, and Catalina M. Lladó, 333–36. ACM. <https://doi.org/10.1145/2668930.2688819>.

Kübler, Jonas M., Kailash Budhathoki, Matthäus Kleindessner, Xiong Zhou, Junming Yin, Ashish Khetan, and George Karypis. 2026. “When LLMs Get Significantly Worse: A Statistical Approach to Detect Model Degradations.” In *Proc. Of the International Conference on Learning Representations (ICLR)*.

Kulal, Sumith, Panupong Pasupat, Kartik Chandra, Mina Lee, Oded Padon, Alex Aiken, and Percy Liang. 2019. “SPoC: Search-Based Pseudocode to Code.” In *Advances in Neural Information Processing Systems 32: Annual Conference on Neural Information Processing Systems 2019, NeurIPS 2019, December 8-14, 2019, Vancouver, BC, Canada*, edited by Hanna M. Wallach, Hugo Larochelle, Alina Beygelzimer, Florence d’Alché-Buc, Emily B. Fox, and Roman Garnett, 11883–94. <https://proceedings.neurips.cc/paper/2019/hash/7298332f04ac004a0ca44cc69ecf6f6b-Abstract.html>.

Li, Raymond, Loubna Ben Allal, Yangtian Zi, Niklas Muennighoff, Denis Kocetkov, Chenghao Mou, Marc Marone, et al. 2023. “StarCoder: May the Source Be with You!” *Trans. Mach. Learn. Res.* 2023. <https://openreview.net/forum?id=KoFOg41haE>.

Liu, Jiawei, Chunqiu Steven Xia, Yuyao Wang, and Lingming Zhang. 2023. “Is Your Code Generated by ChatGPT Really Correct? Rigorous Evaluation of Large Language Models for Code Generation.” In *Advances in Neural Information Processing Systems 36: Annual Conference on Neural Information Processing Systems 2023, NeurIPS 2023*, edited by Alice Oh, Tristan Naumann, Amir Globerson, Kate Saenko, Moritz Hardt, and Sergey Levine. [http://papers.nips.cc/paper\\files/paper/2023/hash/43e9d647ccd3e4b7b5baab53f0368686-Abstract-Conference.html](http://papers.nips.cc/paper\_files/paper/2023/hash/43e9d647ccd3e4b7b5baab53f0368686-Abstract-Conference.html).

Menzies, Tim. 2025. “The Case for Compact AI.” *Commun. ACM* 68 (9): 6–7. <https://doi.org/10.1145/3746057>.

Papineni, Kishore, Salim Roukos, Todd Ward, and Wei-Jing Zhu. 2002. “BLEU: A Method for Automatic Evaluation of Machine Translation.” In *Proceedings of the 40th Annual Meeting of the Association for Computational Linguistics*, 311–18. ACL. <https://doi.org/10.3115/1073083.1073135>.

Ralph, Paul, Miikka Kuutila, Hera Arif, and Bimpe Ayoola. 2024. “Teaching Software Metrology: The Science of Measurement for Software Engineering.” In *Handbook on Teaching Empirical Software Engineering*, edited by Daniel Méndez, Paris Avgeriou, Marcos Kalinowski, and Nauman Bin Ali, 101–54. Springer Nature Switzerland. [https://doi.org/10.1007/978-3-031-71769-7\\5](https://doi.org/10.1007/978-3-031-71769-7\_5).

Ralph, Paul, and Ewan D. Tempero. 2018. “Construct Validity in Software Engineering Research and Software Metrics.” In *Proceedings of the 22nd International Conference on Evaluation and Assessment in Software Engineering, EASE2018*, edited by Austen Rainer, Stephen G. MacDonell, and Jacky W. Keung, 13–23. ACM. <https://doi.org/10.1145/3210459.3210461>.

Ren, Shuo, Daya Guo, Shuai Lu, Long Zhou, Shujie Liu, Duyu Tang, Neel Sundaresan, Ming Zhou, Ambrosio Blanco, and Shuai Ma. 2020. “CodeBLEU: A Method for Automatic Evaluation of Code Synthesis.” *CoRR* abs/2009.10297. <https://arxiv.org/abs/2009.10297>.

Rozière, Baptiste, Jonas Gehring, Fabian Gloeckle, Sten Sootla, Itai Gat, Xiaoqing Ellen Tan, Yossi Adi, et al. 2023. “Code Llama: Open Foundation Models for Code.” *CoRR* abs/2308.12950. <https://doi.org/10.48550/ARXIV.2308.12950>.

Rozière, Baptiste, Marie-Anne Lachaux, Lowik Chanussot, and Guillaume Lample. 2020. “Unsupervised Translation of Programming Languages.” In *Advances in Neural Information Processing Systems 33: Annual Conference on Neural Information Processing Systems 2020, NeurIPS 2020, December 6-12, 2020, Virtual*, edited by Hugo Larochelle, Marc’Aurelio Ranzato, Raia Hadsell, Maria-Florina Balcan, and Hsuan-Tien Lin. <https://proceedings.neurips.cc/paper/2020/hash/ed23fbf18c2cd35f8c7f8de44f85c08d-Abstract.html>.

Xu, Cheng, Shuhao Guan, Derek Greene, and M. Tahar Kechadi. 2024. “Benchmark Data Contamination of Large Language Models: A Survey.” *CoRR* abs/2406.04244. <https://doi.org/10.48550/ARXIV.2406.04244>.

Yang, Yifan, Jiho Shin, Byeonggyu Choi, Minjun Park, Dayun Ju, Changmin Lee, Sanghyuk Chun, Dongjin Kang, Jiin Kim, and Sungroh Yoon. 2025. “From Code Foundation Models to Agents and Applications: A Comprehensive Survey and Practical Guide to Code Intelligence.” *arXiv Preprint arXiv:2502.11827*.

