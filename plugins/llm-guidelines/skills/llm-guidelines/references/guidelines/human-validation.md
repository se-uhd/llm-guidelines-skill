# Use Human Validation for LLM Outputs

> ***Summary***: If assessing the quality of generated artifacts is important and no reference datasets or suitable comparison metrics exist, researchers **should** use human validation for LLM outputs. If they do, they **must** define the measured construct (e.g., usability, maintainability) and describe the measurement instrument in the *paper*. Researchers **should** consider human validation early in the study design, and not as an afterthought. They **should** build on established reference models for human-LLM comparison. When developing or adapting measurement instruments, researchers **must** share them. When LLMs replace, rather than augment, humans in research tasks such as annotating software artifacts, coding interview transcripts, or simulating study participants, researchers **must** explain whether and how the replacement is justified and **should** ground it with inter-model and model-to-human agreement. For qualitative coding of interpretive data, they **should** justify why an LLM is methodologically appropriate. When aggregating LLM judgments, methods and rationale **should** be reported and inter-rater agreement **should** be assessed. Confounding factors **should** be controlled for; where applicable, researchers may perform a power analysis to estimate the required sample size. For value-laden or culturally contingent constructs, researchers **should** describe rater demographics beyond expertise and discuss potential demographic biases. When evaluating agentic tools, user feedback on the agent’s proposed actions **should** be assessed and acceptance statistics reported.

## Rationale

Even with well-justified benchmarks and metrics ([*Benchmarks and Metrics*](../guidelines/benchmarks-metrics.md)), automated measurement captures only the constructs the benchmark was designed to measure. Subjective constructs and constructs that no current benchmark covers require human assessment.

## Recommendations

When LLMs automate research or software development tasks previously performed by humans, the LLM’s performance needs to be assessed. Where no benchmark adequately operationalizes the target construct, researchers **should** validate LLM outputs against human judgment.

### Study Design Considerations

Studies that include human participants need additional considerations, including a recruitment strategy, annotation guidelines, training sessions, or ethical approvals. Therefore, researchers **should** consider human validation early in the study design, not as an afterthought. Authors **must** clearly define in the *paper* the constructs that the human and LLM annotators evaluate (Ralph and Tempero 2018). When designing custom instruments to assess LLM output (e.g., questionnaires, scales), researchers **must** share these instruments.

### Replacing Human Judgment

LLMs may be used to replace, rather than augment, humans in research tasks such as annotating software artifacts, coding interview transcripts, or simulating participants in user studies. In such cases, researchers **must** explain whether and how the replacement is justified and **should** follow systematic approaches to support this judgment, e.g., showing that a jury of three LLMs exhibits inter-model agreement at the same threshold researchers would require for human-to-human agreement, such as Krippendorff’s *α* &gt; 0.8. Such agreement is necessary but not sufficient. High inter-model agreement can reflect shared model biases rather than valid annotation, so researchers **should** additionally validate a sample against human experts before treating LLM outputs as a substitute for human work (Ahmed et al. 2025; Krippendorff 2018). For qualitative coding of interpretive data such as open-ended developer interview responses, agreement metrics do not show that an LLM can perform the interpretive work that the task requires. Researchers **should** justify why the LLM is methodologically appropriate (see [*LLMs for Research*](../study-types/llms-for-research.md)).

### Subjective Judgment and Agreement

When the judgment is subjective (i.e., depends on the judge’s values or theories), the same artifacts **should** be judged independently by both the LLM and a panel of human experts, and the LLM judgments **should** then be compared against an aggregated human reference. Researchers **should** clearly describe their aggregation method and reasoning. Researchers **should** use established reference models to compare humans with LLMs. For example, Schneider, Fotrousi, and Wohlrab (2025) outline design considerations for studies comparing LLMs with humans.

One systematic approach to building the human reference is to randomly order the objects requiring judgment and put them in groups small enough to judge in one to three hours. Two or three human experts review the first group together, simultaneously judging, discussing, and creating a set of decision rules documenting their reasoning. Then, the experts iterate among rounds of:

1. independently rating one group of objects,
2. calculating inter-rater agreement (IRA) or reliability (IRR),
3. meeting to discuss disagreements and reach consensus,
4. updating the decision rules so the disagreement will not recur.

The goal is to reach a target IRA or IRR (e.g., Krippendorff’s *α* &gt; 0.8), indicating sufficient decision rules. Once this target is reached and sustained for two to three groups, it is permissible to continue with a single rater. Researchers **should** report measures of IRA or IRR, preferably broken down by round, and **should** apply thresholds consistent with established standards. Krippendorff (2018) recommends discarding data with *α* &lt; 0.667, considers 0.667 ≤ *α* &lt; 0.8 sufficient only for tentative conclusions, and requires *α* ≥ 0.8 for reliable data (Krippendorff 2018).

Confounding factors **should** be discussed and, where feasible, controlled for (e.g., by categorizing participants according to their level of experience or expertise). For value-laden or culturally contingent constructs (e.g., judging code-style appropriateness or comment helpfulness), researchers **should** describe rater demographics beyond expertise (e.g., geographic, linguistic, or professional background) and discuss potential demographic biases in rater recruitment and instructions (Bean et al. 2025). Where applicable, researchers may perform a power analysis (Cohen 1992; Dybå, Kampenes, and Sjøberg 2006) to estimate the required sample size, ensuring sufficient statistical power in their experimental design. Although established sample-size guidance for LLM-human comparisons is limited, related fields commonly use 100 comparisons without further justification (Tam et al. 2024).

### Agentic Tools

Agentic human-in-the-loop interaction is a built-in human validation, with larger degrees of freedom than traditional experiments that use LLMs directly. Besides generating and modifying content, agentic systems such as *Claude Code* (see [*System and Prompt Design*](../guidelines/design.md)) can autonomously call command-line tools or pull in additional information from MCP servers. When evaluating agentic tools, researchers **should** assess the feedback that users provided on the agent’s proposed actions (e.g., file edits, command executions), report statistics on how frequently they accepted the proposals, and how they modified them.

## Examples

Ahmed et al. (2025) proposed a systematic method for deciding whether LLMs can replace human annotators on a given task, using inter-model agreement as an initial screening criterion (with a threshold of *α* &gt; 0.5) and model confidence for sample-level decisions (Ahmed et al. 2025). However, their threshold is well below the levels generally considered acceptable for inter-rater agreement. Notably, while three LLMs exhibited higher inter-model agreement than human annotators on some tasks, human-model agreement remained low on others. This illustrates that high inter-model reliability does not guarantee alignment with human judgment, reinforcing the need for human validation before assuming that LLM annotations are valid. Moreover, a high inter-model agreement could merely indicate that the models share systematic biases and hence reliably agree on the wrong answer.

Hymel and Johnson (2025) evaluated ChatGPT’s capability to generate requirements documents by comparing an LLM-generated and a human-generated document based on the same business use case. Domain experts reviewed both documents and attempted to distinguish their origin. For agentic tools, Takerngsaksiri et al. (2025) reported acceptance and modification rates from real users for *HULA*, an agentic plan-and-code system deployed in Atlassian JIRA.

## Benefits

Validation against human judgments builds confidence in the LLM’s accuracy and validity (Khraisha et al. 2024). Reporting IRA or IRR supports this validation but does not stand in for it, since even high agreement may reflect shared biases rather than valid judgment. When human reviewers disagree with the LLM, the disagreement points to concrete improvements in the prompts, the context provided to the LLM, or the operational definition of the construct.

## Challenges

Assessing LLM performance with respect to a construct such as code maintainability, answer correctness, or annotation reliability is challenging because ensuring that a construct is defined well and operationalized using an appropriate measurement model requires a deep understanding of (1) the construct, (2) construct validity in general, and (3) instrumentation (Sjøberg and Bergersen 2023; Ralph et al. 2024). Comparing an LLM to human judges is typically slower and more expensive than machine-generated measures. More fundamentally, neither human judgment nor machine-generated measures provides an objective ground truth against which LLM accuracy can be firmly determined. Human preference ratings under-represent properties such as factuality and faithfulness, and assertively phrased outputs receive systematically fewer flagged errors from crowdworkers (Hosking, Blunsom, and Bartolo 2024). Human validation is worth its added cost only when automated measures alone fail to capture the constructs the study evaluates.

Human judgments exhibit variability due to differences in experience, expertise, interpretations, and personal biases (McDonald, Schoenebeck, and Forte 2019). In pairwise judgment of LLM outputs, both human and LLM judges shift their preferences toward answers carrying fake references or richly formatted content, regardless of correctness (Chen et al. 2024). When diverse humans rate items reliably given clear decision rules, we assume that reliability implies validity, but it does not. Measuring reliability is *much* easier than measuring validity, and often the best researchers can do is argue conceptually for why their judges, decision rules, and constructs *should* produce valid ratings.

## Study Types

This guideline applies to all study types, although the need for human validation varies. *Replacing Human Judgment* introduces a conditional **must** that applies particularly to [*LLMs as Annotators*](../study-types/annotators.md), [*LLMs as Judges*](../study-types/judges.md), [*LLMs for Synthesis*](../study-types/synthesis.md), and [*LLMs as Subjects*](../study-types/subjects.md), where the LLM substitutes for human input. For [*LLMs as Annotators*](../study-types/annotators.md), researchers **should** validate LLM-generated annotations against human annotators to assess labeling quality and identify systematic biases. When using [*LLMs as Judges*](../study-types/judges.md), researchers **should** co-create initial rating criteria with humans and validate a sample of LLM judgments against human expert assessments. For [*LLMs for Synthesis*](../study-types/synthesis.md), researchers **should** employ human oversight to verify that qualitative interpretations and synthesized outputs faithfully represent the underlying data. For [*LLMs as Subjects*](../study-types/subjects.md), researchers **should** validate simulated responses against real human data to assess the fidelity of the simulation. For [*Studying LLM Usage*](../study-types/usage.md), researchers **should** carefully reflect on the validity of their evaluation criteria and validate subjective assessments with human experts. For [*LLMs for Tools*](../study-types/tools.md) whose output is supposed to match human expectations, researchers **should** validate the LLM output against human judgment. For [*Benchmarking LLMs*](../study-types/benchmarking.md), there is less need for human validation when using extensively validated and widely-used benchmarks, but researchers **should** employ human validation when creating or adapting new benchmarks.

## Advice for Reviewers

Human validation may be the most challenging of our guidelines to assess because it often requires evaluating conceptual arguments. If LLM output is validated only by comparison with other LLMs, reviewers should look for *quantitative empirical evidence* that such comparison is reliable *and* valid. High inter-model agreement alone is insufficient, as reliability does not imply validity. Similarly, reviewers should expect evidence that any employed benchmarks are reliable and valid. Absent such evidence, human validation is warranted. A single human judge is appropriate only when judgments depend on widely accepted theories and involve limited value conflict (e.g., tagging method names containing abbreviations). For multiple judges, reviewers should expect IRA/IRR improvement techniques as described in the recommendations above (experienced raters, organized rounds, consensus meetings, updated decision rules). Low IRA or IRR (e.g., Krippendorff’s *α* &lt; 0.8) without these techniques is a concern. Conversely, if authors have followed best practices and still obtained mediocre results (e.g., 0.66 &lt; *α* &lt; 0.8), this should be noted as a limitation. Beyond reliability, reviewers should expect authors to explain conceptually why their human judgments should be valid, considering construct definitions, decision rules, and judge expertise. As with other guidelines, missing information is typically a revision request. Absent judge instructions, instruments, decision rules, or construct definitions may prevent assessment of rigor and validity, while missing recruitment details are less critical. Clarification requests about construct definitions are routine and should not alone warrant rejection.

## See Also

- [Use Suitable Baselines, Benchmarks, and Metrics](../guidelines/benchmarks-metrics.md): Human evaluation complements automated metrics where benchmarks cannot sufficiently capture the target construct.
- [Report Model Version, Configuration, and Customizations](../guidelines/model-version.md): Human-validation findings characterize only the specific model and configuration that produced the outputs.
- [Report System and Prompt Design](../guidelines/design.md): Prompt and architecture choices produce the outputs that humans then validate.
- [Report Session Traces](../guidelines/traces.md): Stored interaction logs and runtime traces are the artifacts human reviewers examine.
- [Report Limitations and Mitigations](../guidelines/limitations.md): Rater demographics, threshold choices, and the validity of human judgments are limitations to discuss.

## References

Ahmed, Toufique, Premkumar T. Devanbu, Christoph Treude, and Michael Pradel. 2025. “Can LLMs Replace Manual Annotation of Software Engineering Artifacts?” In *22nd IEEE/ACM International Conference on Mining Software Repositories, MSR@ICSE 2025, Ottawa, ON, Canada, April 28-29, 2025*, 526–38. IEEE. <https://doi.org/10.1109/MSR66628.2025.00086>.

Bean, Andrew M., Ryan Othniel Kearns, Angelika Romanou, Franziska Sofia Hafner, Harry Mayne, Jan Batzner, Negar Foroutan, et al. 2025. “Measuring What Matters: Construct Validity in Large Language Model Benchmarks.” In *Advances in Neural Information Processing Systems 38: Annual Conference on Neural Information Processing Systems 2025, NeurIPS 2025, Datasets and Benchmarks Track*. <https://arxiv.org/abs/2511.04703>.

Chen, Guiming, Shunian Chen, Ziche Liu, Feng Jiang, and Benyou Wang. 2024. “Humans or LLMs as the Judge? A Study on Judgement Bias.” In *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, EMNLP 2024, Miami, FL, USA, November 12-16, 2024*, edited by Yaser Al-Onaizan, Mohit Bansal, and Yun-Nung Chen, 8301–27. Association for Computational Linguistics. <https://doi.org/10.18653/V1/2024.EMNLP-MAIN.474>.

Cohen, Jacob. 1992. “A Power Primer.” *Psychological Bulletin* 112 (1): 155–59. <https://doi.org/10.1037/0033-2909.112.1.155>.

Dybå, Tore, Vigdis By Kampenes, and Dag I. K. Sjøberg. 2006. “A Systematic Review of Statistical Power in Software Engineering Experiments.” *Inf. Softw. Technol.* 48 (8): 745–55. <https://doi.org/10.1016/J.INFSOF.2005.08.009>.

Hosking, Tom, Phil Blunsom, and Max Bartolo. 2024. “Human Feedback Is Not Gold Standard.” In *The Twelfth International Conference on Learning Representations, ICLR 2024, Vienna, Austria, May 7-11, 2024*. OpenReview.net. <https://openreview.net/forum?id=7W3GLNImfS>.

Hymel, Cory, and Hiroe Johnson. 2025. “Analysis of LLMs Vs Human Experts in Requirements Engineering.” *CoRR* abs/2501.19297. <https://doi.org/10.48550/ARXIV.2501.19297>.

Khraisha, Qusai, Sophie Put, Johanna Kappenberg, Azza Warraitch, and Kristin Hadfield. 2024. “Can Large Language Models Replace Humans in Systematic Reviews? Evaluating GPT-4’s Efficacy in Screening and Extracting Data from Peer-Reviewed and Grey Literature in Multiple Languages.” *Research Synthesis Methods* 15 (4): 616–26. <https://doi.org/10.1002/jrsm.1715>.

Krippendorff, Klaus. 2018. *Content Analysis: An Introduction to Its Methodology*. 4th ed. SAGE Publications.

McDonald, Nora, Sarita Schoenebeck, and Andrea Forte. 2019. “Reliability and Inter-Rater Reliability in Qualitative Research: Norms and Guidelines for CSCW and HCI Practice.” *Proc. ACM Hum. Comput. Interact.* 3 (CSCW): 72:1–23. <https://doi.org/10.1145/3359174>.

Ralph, Paul, Miikka Kuutila, Hera Arif, and Bimpe Ayoola. 2024. “Teaching Software Metrology: The Science of Measurement for Software Engineering.” In *Handbook on Teaching Empirical Software Engineering*, edited by Daniel Méndez, Paris Avgeriou, Marcos Kalinowski, and Nauman Bin Ali, 101–54. Springer Nature Switzerland. <https://doi.org/10.1007/978-3-031-71769-7_5>.

Ralph, Paul, and Ewan D. Tempero. 2018. “Construct Validity in Software Engineering Research and Software Metrics.” In *Proceedings of the 22nd International Conference on Evaluation and Assessment in Software Engineering, EASE2018*, edited by Austen Rainer, Stephen G. MacDonell, and Jacky W. Keung, 13–23. ACM. <https://doi.org/10.1145/3210459.3210461>.

Schneider, Kurt, Farnaz Fotrousi, and Rebekka Wohlrab. 2025. “A Reference Model for Empirically Comparing LLMs with Humans.” In *47th IEEE/ACM International Conference on Software Engineering: Software Engineering in Society, ICSE-SEIS 2025, Ottawa, ON, Canada, April 27 - May 3, 2025*, 130–34. IEEE. <https://doi.org/10.1109/ICSE-SEIS66351.2025.00018>.

Sjøberg, Dag I. K., and Gunnar Rye Bergersen. 2023. “Construct Validity in Software Engineering.” *IEEE Trans. Software Eng.* 49 (3): 1374–96. <https://doi.org/10.1109/TSE.2022.3176725>.

Takerngsaksiri, Wannita, Jirat Pasuksmit, Patanamon Thongtanunam, Chakkrit Tantithamthavorn, Ruixiong Zhang, Fan Jiang, Jing Li, Evan Cook, Kun Chen, and Ming Wu. 2025. “Human-in-the-Loop Software Development Agents.” In *47th IEEE/ACM International Conference on Software Engineering: Software Engineering in Practice, SEIP@ICSE 2025, Ottawa, ON, Canada, April 27 - May 3, 2025*, 342–52. IEEE. <https://doi.org/10.1109/ICSE-SEIP66354.2025.00036>.

Tam, Thomas Yu Chow, Sonish Sivarajkumar, Sumit Kapoor, Alisa V. Stolyar, Katelyn Polanska, Karleigh R. McCarthy, Hunter Osterhoudt, et al. 2024. “A Framework for Human Evaluation of Large Language Models in Healthcare Derived from Literature Review.” *Npj Digit. Medicine* 7 (1). <https://doi.org/10.1038/S41746-024-01258-7>.
