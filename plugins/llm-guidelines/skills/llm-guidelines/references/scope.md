# Scope

## Motivation

Since the release of ChatGPT in November 2022, large language models (LLMs) have been adopted widely across software engineering (SE) research (Hou et al. 2024), yet the reproducibility and replicability of empirical studies involving LLMs remains uncertain. Recent findings indicate a low reproducibility of SE studies involving LLMs (Angermeir et al. 2025). Evertz et al. (2026) survey 72 peer-reviewed papers from leading security and SE venues published in 2023–2024 and find that every paper contains at least one of nine LLM-specific pitfalls they identify, spanning data collection, pre-training, fine-tuning, prompting, and evaluation; only 15.7% of the pitfalls present in those papers were explicitly discussed. Three characteristics of LLMs make this particularly challenging: their inherent non-determinism causes variability across runs (Song et al. 2025; Bjarnason, Silva, and Monperrus 2026), with slight changes leading to substantially different results (Agarwal et al. 2021; Schroeder and Wood-Doughty 2024); commercial models evolve beyond version identifiers, so reported performance can change over time (Chen, Zaharia, and Zou 2024); and even for “open” models, training data and fine-tuning details often remain undisclosed (Gibney 2024). Moreover, prompt formatting choices alone can shift accuracy by tens of percentage points (Sclar et al. 2024), and configured parameters such as temperature affect output variability (Renze 2024). Hence, not reporting these settings directly affects reproducibility. Traditional open science practice in SE has focused on releasing source code and datasets as a replication package. The empirical artifact analysis literature in SE focuses more on code repositories and data than on upstream artifacts such as requirements specifications and design documents (Liu et al. 2024). With LLMs, code is often generated from prompts, context files, and other runtime inputs to the model, so reporting must shift left to cover these upstream artifacts in addition to the code and data they produce.

Although the SE research community has developed guidelines for conducting and reporting specific types of empirical studies such as controlled experiments (e.g., (Wohlin et al. 2024; Shull, Singer, and Sjøberg 2008)), their replications (e.g., (Santos et al. 2021)), or empirical studies in general (e.g., the *ACM SIGSOFT Empirical Standards* (Ralph et al. 2021)), none of these address the LLM-specific aspects described above. Previously, a position paper highlighted these issues (Wagner et al. 2025), but there was no comprehensive community-developed guidance for designing and reporting empirical studies involving LLMs in SE.

Therefore, we present community-developed guidelines for conducting and reporting studies involving LLMs in SE research, co-developed by 22 researchers. After outlining our [*Scope*](./scope.md), we introduce a taxonomy of [*Study Types*](./study-types/), then present eight [*Guidelines*](./guidelines/). We complement these with an applicability matrix mapping guidelines to study types and a reporting checklist for authors and reviewers. For each study type and guideline, we identify relevant examples, both within and outside of SE research. We maintain the guidelines online as a living resource for the community to use and shape ([llm-guidelines.org](https://llm-guidelines.org/)).

## Scope and Conventions

### Software Engineering as our Target Discipline

We target SE research because reporting guidelines from other disciplines do not address its specific needs (see *Related Reporting Guidelines* below). In particular, SE research employs a wide variety of empirical methods (Ralph et al. 2021; Wohlin et al. 2024). We organize the LLM-involving subset of these methods into a taxonomy of [*Study Types*](./study-types/), and each of our [*Guidelines*](./guidelines/) specifies its applicability per study type.

### Focus on Text-Based Use Cases

While multi-modal foundation models that use or generate images, audio, or video may also support SE research and practice, we focus on textual use cases of LLMs (e.g., in natural language or programming languages). Many of our guidelines, particularly those concerning model reporting, prompt documentation, and reproducibility, are likely applicable to multi-modal settings as well, but we leave their explicit validation to future work.

### Focus on Direct Development or Research Support

While researchers may use LLMs for many peripheral tasks (e.g., proofreading, spell-checking, translation), our guidelines focus on their direct role in empirical research and engineering practice. For engineers, we focus on the use of LLMs to automate SE tasks, that is, artificial intelligence (AI) for software engineering (AI4SE) (see [*LLMs for SE*](./study-types/llms-for-se.md)). This includes agentic systems that autonomously plan and execute multi-step tasks using LLMs (see [*System and Prompt Design*](./guidelines/design.md)). For researchers, we focus on the use of LLMs to automate empirical research tasks such as data collection, processing, or analysis (see [*LLMs for Research*](./study-types/llms-for-research.md)). The 2026 ACM Policy on Authorship makes the same distinction, requiring disclosure of AI used in the conduct of research while exempting AI used only to assist with writing (Association for Computing Machinery 2026).

### Researchers as our Target Audience

Our guidelines are intended to help SE researchers design, plan, conduct, and report empirical studies involving LLMs, and to support scholarly peer review of such studies. Each guideline includes an *Advice for Reviewers* subsection with targeted assessment suggestions. Our guidelines focus on what to report and how; they complement but do not replace methodological guidance for designing specific types of empirical studies.

### Reporting Locations

We use *paper* to refer to the manuscript PDF, including any appendices bound with it. We use *supplementary material* to refer to any artifact, replication package, dataset, or other resource external to the manuscript PDF (e.g., hosted on Zenodo or Figshare). What belongs in the main body versus an appendix is a presentation choice for authors and venues; what belongs inside the manuscript versus outside it is the reporting-location decision the guidelines make. When a recommendation does not specify a location, either *paper* or *supplementary material* is acceptable.

### Related Reporting Guidelines

Reporting guidelines have a long tradition in healthcare research, where CONSORT (Schulz, Altman, and Moher 2010) is the canonical standard for randomized clinical trials. Our reporting checklist ([checklist](./checklist.md)) follows its structural template. LLM-specific reporting guidelines have appeared more recently: Gallifant et al. (2025)’s TRIPOD-LLM for healthcare, Navarro, Syriani, and Arawjo (2026)’s HCI guidelines, Kapoor et al. (2024)’s REFORMS for ML-based science, and within SE, Sallou, Durieux, and Panichella (2024)’s vision paper on validity threats, our earlier workshop position paper (Wagner et al. 2025), and Korn et al. (2026)’s prompt-reporting guideline for automated SE, derived from a literature review of ICSE, FSE, and ASE papers and a survey of 105 program committee members. Beyond LLM-specific work, the NeurIPS reproducibility checklist (Pineau et al. 2021) prescribes per-submission disclosure for ML papers, covering items such as algorithm description, experimental setup, and statistical reporting.

Korn et al. (2026) frame their recommendations as complementing ours, with the essential items their 105 SE PC respondents endorsed aligning with what [*Version and Configuration*](./guidelines/model-version.md), [*System and Prompt Design*](./guidelines/design.md), and [*Limitations and Mitigations*](./guidelines/limitations.md) already require. Navarro, Syriani, and Arawjo (2026)’s HCI guidelines, by contrast, balance “*the practical realities of authors’ time, cost, and page limitations*” with scientific concerns and HCI norms, while our [*Guidelines*](./guidelines/) aim for comprehensive coverage and use **must** and **should** to express that balance. On prompt reporting, Navarro, Syriani, and Arawjo (2026) argue for selective disclosure based on each prompt’s centrality to author claims, whereas [*System and Prompt Design*](./guidelines/design.md) recommends fuller disclosure with named exceptions for privacy, anonymity, or confidentiality concerns. On technical evaluation, Navarro, Syriani, and Arawjo (2026) recommend a “*modest technical evaluation of the LLM component on a dataset of representative inputs*” tailored to HCI research, whereas [*Benchmarks and Metrics*](./guidelines/benchmarks.md) asks for established benchmarks, traditional baselines, and inferential statistics where applicable. Peripheral LLM uses such as proofreading, spell-checking, and translation are entirely out of scope (see *Focus on Direct Development or Research Support* above).

Our guidelines name *paper* or *supplementary material* as the reporting location for each recommendation (see *Reporting Locations* above). The *supplementary material* is published according to the *ACM SIGSOFT Open Science Policies* (Graziotin 2024) for replication and downstream reuse. In summary, our guidelines apply to SE empirical research broadly, organize recommendations around the taxonomy of seven study types introduced in [*Study Types*](./study-types/) with explicit per-study-type applicability, and pair each recommendation with a target reporting location in *paper* or *supplementary material*.

### Navigating These Guidelines

Our guidelines are structured to support different reading strategies depending on the reader’s goal. *Researchers planning a new study* may start with the taxonomy of study types (see [*Study Types*](./study-types/)) to identify which types apply to their planned work, then consult the [applicability matrix](./guidelines/#guidelines-by-study-type) to determine which guidelines are requirements (**must**) and which are recommendations (**should**) for those study types. Each guideline section opens with a brief summary, allowing readers to quickly assess relevance before reading the full text. *Researchers writing up results* may start with the [checklist](./checklist.md), which organizes actionable items by typical paper sections (Introduction, Research Design and Methods, Results, etc.). *Reviewers* can use the *Advice for Reviewers* subsection at the end of each guideline for targeted guidance on assessing manuscripts.

## References

Agarwal, Rishabh, Max Schwarzer, Pablo Samuel Castro, Aaron C. Courville, and Marc G. Bellemare. 2021. “Deep Reinforcement Learning at the Edge of the Statistical Precipice.” In *Advances in Neural Information Processing Systems 34: Annual Conference on Neural Information Processing Systems 2021, NeurIPS 2021, December 6-14, 2021, Virtual*, edited by Marc’Aurelio Ranzato, Alina Beygelzimer, Yann N. Dauphin, Percy Liang, and Jennifer Wortman Vaughan, 29304–20. <https://proceedings.neurips.cc/paper/2021/hash/f514cec81cb148559cf475e7426eed5e-Abstract.html>.

Angermeir, Florian, Maximilian Amougou, Mark Kreitz, Andreas Bauer, Matthias Linhuber, Davide Fucci, Fabiola Moyón Constante, Daniel Méndez, and Tony Gorschek. 2025. “Reflections on the Reproducibility of Commercial LLM Performance in Empirical Software Engineering Studies.” *CoRR* abs/2510.25506. <https://doi.org/10.48550/ARXIV.2510.25506>.

Association for Computing Machinery. 2026. “ACM Policy on Authorship.” <https://www.acm.org/publications/policies/new-acm-policy-on-authorship>.

Bjarnason, Bjarni Haukur, André Silva, and Martin Monperrus. 2026. “On Randomness in Agentic Evals.” *CoRR* abs/2602.07150. <https://doi.org/10.48550/ARXIV.2602.07150>.

Chen, Lingjiao, Matei Zaharia, and James Zou. 2024. “How Is ChatGPT’s Behavior Changing over Time?” *Harvard Data Science Review* 6 (2). <https://doi.org/10.1162/99608f92.5317da47>.

Evertz, Jonathan, Niklas Risse, Nicolai Neuer, Andreas Müller, Philipp Normann, Gaetano Sapia, Srishti Gupta, et al. 2026. “Chasing Shadows: Pitfalls in LLM Security Research.” In *33rd Annual Network and Distributed System Security Symposium, NDSS 2026, San Diego, California, USA, February 23-27, 2026*. The Internet Society. <https://www.ndss-symposium.org/ndss-paper/chasing-shadows-pitfalls-in-llm-security-research/>.

Gallifant, Jack, Majid Afshar, Saleem Ameen, Yindalon Aphinyanaphongs, Shan Chen, Giovanni Cacciamani, Dina Demner-Fushman, et al. 2025. “The TRIPOD-LLM Reporting Guideline for Studies Using Large Language Models.” *Nature Medicine* 31 (1): 60–69. <https://doi.org/10.1038/s41591-024-03425-5>.

Gibney, Elizabeth. 2024. “Not all ‘open source’ AI models are actually open.” *Nature News*. <https://doi.org/10.1038/d41586-024-02012-5>.

Graziotin, Daniel. 2024. “Acmsigsoft/Open-Science-Policies: V1.0.0.” Zenodo. <https://doi.org/10.5281/zenodo.10796477>.

Hou, Xinyi, Yanjie Zhao, Yue Liu, Zhou Yang, Kailong Wang, Li Li, Xiapu Luo, David Lo, John Grundy, and Haoyu Wang. 2024. “Large Language Models for Software Engineering: A Systematic Literature Review.” *ACM Trans. Softw. Eng. Methodol.* 33 (8): 220:1–79. <https://doi.org/10.1145/3695988>.

Kapoor, Sayash, Emily M. Cantrell, Kenny Peng, Thanh Hien Pham, Christopher A. Bail, Odd Erik Gundersen, Jake M. Hofman, et al. 2024. “REFORMS: Consensus-Based Recommendations for Machine-Learning-Based Science.” *Science Advances* 10 (18): eadk3452. <https://doi.org/10.1126/sciadv.adk3452>.

Korn, Alexander, Lea Zaruchas, Chetan Arora, Andreas Metzger, Sven Smolka, Fanyu Wang, and Andreas Vogelsang. 2026. “Reporting LLM Prompting in Automated Software Engineering: A Guideline Based on Current Practices and Expectations.” *CoRR* abs/2601.01954. <https://doi.org/10.48550/ARXIV.2601.01954>.

Liu, Mugeng, Xiaolong Huang, Wei He, Yibing Xie, Jie M. Zhang, Xiang Jing, Zhenpeng Chen, and Yun Ma. 2024. “Research Artifacts in Software Engineering Publications: Status and Trends.” *J. Syst. Softw.* 213: 112032. <https://doi.org/10.1016/J.JSS.2024.112032>.

Navarro, Karla Felix, Eugene Syriani, and Ian Arawjo. 2026. “Reporting and Reviewing LLM-Integrated Systems in HCI: Challenges and Considerations.” In *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems, CHI 2026, Barcelona, Spain, April 13-17, 2026*, edited by Nuria Oliver, David A. Shamma, Heloisa Candello, Pablo César, Pedro Lopes, Alessandro Bozzon, Thomas Kosch, et al., 1546:1–18. ACM. <https://doi.org/10.1145/3772318.3790439>.

Pineau, Joelle, Philippe Vincent-Lamarre, Koustuv Sinha, Vincent Larivière, Alina Beygelzimer, Florence d’Alché-Buc, Emily B. Fox, and Hugo Larochelle. 2021. “Improving Reproducibility in Machine Learning Research (a Report from the NeurIPS 2019 Reproducibility Program).” *J. Mach. Learn. Res.* 22: 164:1–20. <https://jmlr.org/papers/v22/20-303.html>.

Ralph, Paul, Nauman bin Ali, Sebastian Baltes, Domenico Bianculli, Jessica Diaz, Yvonne Dittrich, Neil Ernst, et al. 2021. “Empirical Standards for Software Engineering Research.” <https://arxiv.org/abs/2010.03525>.

Renze, Matthew. 2024. “The Effect of Sampling Temperature on Problem Solving in Large Language Models.” In *Findings of the Association for Computational Linguistics: EMNLP 2024*, 7346–56. <https://doi.org/10.18653/v1/2024.findings-emnlp.432>.

Sallou, June, Thomas Durieux, and Annibale Panichella. 2024. “Breaking the Silence: The Threats of Using LLMs in Software Engineering.” In *Proceedings of the 2024 ACM/IEEE 44th International Conference on Software Engineering: New Ideas and Emerging Results, NIER@ICSE 2024, Lisbon, Portugal, April 14-20, 2024*, 102–6. ACM. <https://doi.org/10.1145/3639476.3639764>.

Santos, Adrian, Sira Vegas, Markku Oivo, and Natalia Juristo. 2021. “A Procedure and Guidelines for Analyzing Groups of Software Engineering Replications.” *IEEE Trans. Software Eng.* 47 (9): 1742–63. <https://doi.org/10.1109/TSE.2019.2935720>.

Schroeder, Kayla, and Zach Wood-Doughty. 2024. “Can You Trust LLM Judgments? Reliability of LLM-as-a-Judge.” *CoRR* abs/2412.12509. <https://doi.org/10.48550/ARXIV.2412.12509>.

Schulz, Kenneth F., Douglas G. Altman, and David Moher. 2010. “CONSORT 2010 Statement: Updated Guidelines for Reporting Parallel Group Randomised Trials.” *BMJ* 340: c332. <https://doi.org/10.1136/bmj.c332>.

Sclar, Melanie, Yejin Choi, Yulia Tsvetkov, and Alane Suhr. 2024. “Quantifying Language Models’ Sensitivity to Spurious Features in Prompt Design or: How I Learned to Start Worrying about Prompt Formatting.” In *The Twelfth International Conference on Learning Representations, ICLR 2024, Vienna, Austria, May 7-11, 2024*. OpenReview.net. <https://openreview.net/forum?id=RIu5lyNXjT>.

Shull, Forrest, Janice Singer, and Dag I. K. Sjøberg, eds. 2008. *Guide to Advanced Empirical Software Engineering*. Springer. <https://doi.org/10.1007/978-1-84800-044-5>.

Song, Yifan, Guoyin Wang, Sujian Li, and Bill Yuchen Lin. 2025. “The Good, the Bad, and the Greedy: Evaluation of LLMs Should Not Ignore Non-Determinism.” In *Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies, NAACL 2025 - Volume 1: Long Papers*, edited by Luis Chiruzzo, Alan Ritter, and Lu Wang, 4195–4206. Association for Computational Linguistics. <https://doi.org/10.18653/V1/2025.NAACL-LONG.211>.

Wagner, Stefan, Marvin Muñoz Barón, Davide Falessi, and Sebastian Baltes. 2025. “Towards Evaluation Guidelines for Empirical Studies Involving LLMs.” In *IEEE/ACM International Workshop on Methodological Issues with Empirical Studies in Software Engineering, WSESE@ICSE 2025, May 3, 2025*, 24–27. IEEE. <https://doi.org/10.1109/WSESE66602.2025.00011>.

Wohlin, Claes, Per Runeson, Martin Höst, Magnus C. Ohlsson, Björn Regnell, and Anders Wesslén. 2024. *Experimentation in Software Engineering, Second Edition*. Springer. <https://doi.org/10.1007/978-3-662-69306-3>.
