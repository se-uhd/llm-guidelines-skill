# Motivation and Scope

## Motivation

Since the release of ChatGPT in November 2022, large language models (LLMs) have rapidly become a major focus of software engineering (SE) research (Hou et al. 2024), yet the reproducibility and replicability of empirical studies involving LLMs remains uncertain. Recent findings indicate a low reproducibility of SE studies involving LLMs (Angermeir et al. 2025). Three characteristics of LLMs make this particularly challenging: their inherent non-determinism causes variability across runs, with slight changes leading to substantially different results (Schroeder and Wood-Doughty 2024; Song et al. 2025; Agarwal et al. 2021; Bjarnason, Silva, and Monperrus 2026); commercial models evolve beyond version identifiers, so reported performance can change over time (Chen, Zaharia, and Zou 2024); and even for “open” models, training data and fine-tuning details often remain undisclosed (Gibney 2024). Moreover, prompt formatting choices alone can shift accuracy by tens of percentage points (Sclar et al. 2024), and configured parameters such as temperature affect output variability (Renze 2024). Hence, not reporting these settings directly affects reproducibility.

Although the SE research community has developed guidelines for conducting and reporting specific types of empirical studies such as controlled experiments (e.g., (Wohlin et al. 2024; Shull, Singer, and Sjøberg 2008)), their replications (e.g., (Santos et al. 2021)), or empirical studies in general (e.g., the *ACM SIGSOFT Empirical Standards* (Ralph et al. 2021)), none of these address the LLM-specific aspects described above. Previously, a position paper highlighted these issues (Wagner et al. 2025), but there was no comprehensive community-developed guidance for designing and reporting empirical studies involving LLMs in SE.

Therefore, we present community-developed guidelines for conducting and reporting studies involving LLMs in SE research, co-developed by 22 researchers. After outlining our [*Scope*](./scope.md), we introduce a taxonomy of [*Study Types*](./study-types/), then present eight [*Guidelines*](./guidelines/). We complement these with an applicability matrix mapping guidelines to study types and a reporting checklist for authors and reviewers. For each study type and guideline, we identify relevant examples, both within and outside of SE research. We maintain the guidelines online as a living resource for the community to use and shape ([llm-guidelines.org](https://llm-guidelines.org/)).

## Scope

### Software Engineering as our Target Discipline

We target SE research because existing cross-disciplinary guidelines do not address its needs. For instance, Gallifant et al.’s (Gallifant et al. 2025) guidelines for LLM use in healthcare research include discipline-specific items irrelevant to most SE studies (e.g., clinical-care usability) while lacking guidance on tool architectures, benchmarking, and code-specific evaluation that SE research requires. Moreover, SE research employs a wide variety of empirical methods (Ralph et al. 2021; Wohlin et al. 2024). Our work builds on Sallou, Durieux, and Panichella (2024)’s vision paper on mitigating validity threats in LLM-based SE research (Sallou, Durieux, and Panichella 2024) and our own position paper (Wagner et al. 2025), providing more detailed advice for a wider variety of research methods organized into a taxonomy of [*Study Types*](./study-types/).

### Focus on Text-Based Use Cases

While multi-modal foundation models that use or generate images, audio, or video may also support SE research and practice, we focus on textual use cases of LLMs (e.g., in natural language or programming languages). Many of our guidelines, particularly those concerning model reporting, prompt documentation, and reproducibility, are likely applicable to multi-modal settings as well, but we leave their explicit validation to future work.

### Focus on Direct Development or Research Support

While researchers may use LLMs for many peripheral tasks (e.g., proof-reading, spell-checking, translation), our guidelines focus on their direct role in empirical research and engineering practice. For engineers, we focus on the use of LLMs to automate SE tasks, that is, artificial intelligence (AI) for software engineering (AI4SE) (see [*LLMs for SE*](./study-types/llms-as-tools-for-software-engineers.md)). This includes agentic systems that autonomously plan and execute multi-step tasks using LLMs (see [*System and Prompt Design*](./guidelines/report-system-and-prompt-design.md)). For researchers, we focus on the use of LLMs to automate empirical research tasks such as data collection, processing, or analysis (see [*LLMs for Research*](./study-types/llms-as-tools-for-software-engineering-researchers.md)).

### Researchers as our Target Audience

Our guidelines are intended to help SE researchers design, plan, conduct, and report empirical studies involving LLMs, and to support scholarly peer review of such studies. Each guideline includes an *Advice for Reviewers* subsection with targeted assessment suggestions. Our guidelines focus on what to report and how; they complement but do not replace methodological guidance for designing specific types of empirical studies.

### Reporting Locations

We use *paper* to refer to the manuscript PDF, including any appendices bound with it. We use *supplementary material* to refer to any artifact, replication package, dataset, or other resource external to the manuscript PDF (e.g., hosted on Zenodo or Figshare). What belongs in the main body versus an appendix is a presentation choice for authors and venues; what belongs inside the manuscript versus outside it is the reporting-location decision the guidelines make. When a recommendation does not specify a location, either *paper* or *supplementary material* is acceptable.

### How to Navigate this Paper

This paper is structured to support different reading strategies depending on the reader’s goal. *Researchers planning a new study* may start with the taxonomy of study types (see [*Study Types*](./study-types/)) to identify which types apply to their planned work, then consult the [applicability matrix](./guidelines/#guidelines-by-study-type) to determine which guidelines are requirements (**must**) and which are recommendations (**should**) for those study types. Each guideline section opens with a brief summary in a shaded box, allowing readers to quickly assess relevance before reading the full text. *Researchers writing up results* may prefer to start with the [checklist](./checklist.md), which organizes actionable items by typical paper sections (Introduction, Research Design and Methods, Results, etc.).

*Reviewers* can use the *Advice for Reviewers* subsection at the end of each guideline for targeted guidance on assessing manuscripts.

## References

Agarwal, Rishabh, Max Schwarzer, Pablo Samuel Castro, Aaron C. Courville, and Marc G. Bellemare. 2021. “Deep Reinforcement Learning at the Edge of the Statistical Precipice.” In *Advances in Neural Information Processing Systems 34: Annual Conference on Neural Information Processing Systems 2021, NeurIPS 2021, December 6-14, 2021, Virtual*, edited by Marc’Aurelio Ranzato, Alina Beygelzimer, Yann N. Dauphin, Percy Liang, and Jennifer Wortman Vaughan, 29304–20. <https://proceedings.neurips.cc/paper/2021/hash/f514cec81cb148559cf475e7426eed5e-Abstract.html>.

Angermeir, Florian, Maximilian Amougou, Mark Kreitz, Andreas Bauer, Matthias Linhuber, Davide Fucci, Fabiola Moyón Constante, Daniel Méndez, and Tony Gorschek. 2025. “Reflections on the Reproducibility of Commercial LLM Performance in Empirical Software Engineering Studies.” *CoRR* abs/2510.25506. <https://doi.org/10.48550/ARXIV.2510.25506>.

Bjarnason, Bjarni Haukur, André Silva, and Martin Monperrus. 2026. “On Randomness in Agentic Evals.” *CoRR* abs/2602.07150. <https://doi.org/10.48550/ARXIV.2602.07150>.

Chen, Lingjiao, Matei Zaharia, and James Zou. 2024. “How Is ChatGPT’s Behavior Changing over Time?” *Harvard Data Science Review* 6 (2). <https://doi.org/10.1162/99608f92.5317da47>.

Gallifant, Jack, Majid Afshar, Saleem Ameen, Yindalon Aphinyanaphongs, Shan Chen, Giovanni Cacciamani, Dina Demner-Fushman, et al. 2025. “The TRIPOD-LLM Reporting Guideline for Studies Using Large Language Models.” *Nature Medicine* 31 (1): 60–69. <https://doi.org/10.1038/s41591-024-03425-5>.

Gibney, Elizabeth. 2024. “<span class="nocase">Not all ‘open source’ AI models are actually open</span>.” *Nature News*. <https://doi.org/10.1038/d41586-024-02012-5>.

Hou, Xinyi, Yanjie Zhao, Yue Liu, Zhou Yang, Kailong Wang, Li Li, Xiapu Luo, David Lo, John Grundy, and Haoyu Wang. 2024. “Large Language Models for Software Engineering: A Systematic Literature Review.” *ACM Trans. Softw. Eng. Methodol.* 33 (8): 220:1–79. <https://doi.org/10.1145/3695988>.

Ralph, Paul, Nauman bin Ali, Sebastian Baltes, Domenico Bianculli, Jessica Diaz, Yvonne Dittrich, Neil Ernst, et al. 2021. “Empirical Standards for Software Engineering Research.” <https://arxiv.org/abs/2010.03525>.

Renze, Matthew. 2024. “The Effect of Sampling Temperature on Problem Solving in Large Language Models.” In *Findings of the Association for Computational Linguistics: EMNLP 2024*, 7346–56. <https://doi.org/10.18653/v1/2024.findings-emnlp.432>.

Sallou, June, Thomas Durieux, and Annibale Panichella. 2024. “Breaking the Silence: The Threats of Using LLMs in Software Engineering.” In *Proceedings of the 2024 ACM/IEEE 44th International Conference on Software Engineering: New Ideas and Emerging Results, NIER@ICSE 2024, Lisbon, Portugal, April 14-20, 2024*, 102–6. ACM. <https://doi.org/10.1145/3639476.3639764>.

Santos, Adrian, Sira Vegas, Markku Oivo, and Natalia Juristo. 2021. “A Procedure and Guidelines for Analyzing Groups of Software Engineering Replications.” *IEEE Trans. Software Eng.* 47 (9): 1742–63. <https://doi.org/10.1109/TSE.2019.2935720>.

Schroeder, Kayla, and Zach Wood-Doughty. 2024. “Can You Trust LLM Judgments? Reliability of LLM-as-a-Judge.” *CoRR* abs/2412.12509. <https://doi.org/10.48550/ARXIV.2412.12509>.

Sclar, Melanie, Yejin Choi, Yulia Tsvetkov, and Alane Suhr. 2024. “Quantifying Language Models’ Sensitivity to Spurious Features in Prompt Design or: How I Learned to Start Worrying about Prompt Formatting.” In *The Twelfth International Conference on Learning Representations, ICLR 2024, Vienna, Austria, May 7-11, 2024*. OpenReview.net. <https://openreview.net/forum?id=RIu5lyNXjT>.

Shull, Forrest, Janice Singer, and Dag I. K. Sjøberg, eds. 2008. *Guide to Advanced Empirical Software Engineering*. Springer. <https://doi.org/10.1007/978-1-84800-044-5>.

Song, Yifan, Guoyin Wang, Sujian Li, and Bill Yuchen Lin. 2025. “The Good, the Bad, and the Greedy: Evaluation of LLMs Should Not Ignore Non-Determinism.” In *Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies, NAACL 2025 - Volume 1: Long Papers*, edited by Luis Chiruzzo, Alan Ritter, and Lu Wang, 4195–4206. Association for Computational Linguistics. <https://doi.org/10.18653/V1/2025.NAACL-LONG.211>.

Wagner, Stefan, Marvin Muñoz Barón, Davide Falessi, and Sebastian Baltes. 2025. “Towards Evaluation Guidelines for Empirical Studies Involving LLMs.” In *IEEE/ACM International Workshop on Methodological Issues with Empirical Studies in Software Engineering, WSESE@ICSE 2025, May 3, 2025*, 24–27. IEEE. <https://doi.org/10.1109/WSESE66602.2025.00011>.

Wohlin, Claes, Per Runeson, Martin Höst, Magnus C. Ohlsson, Björn Regnell, and Anders Wesslén. 2024. *Experimentation in Software Engineering, Second Edition*. Springer. <https://doi.org/10.1007/978-3-662-69306-3>.

