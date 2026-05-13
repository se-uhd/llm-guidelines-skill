# Benchmarking LLMs for Software Engineering Tasks

## Description

Benchmarking is the process of evaluating an LLM’s performance on standardized tasks, using standardized metrics, on a standardized dataset. The LLM output is compared to a supposed ground truth from the benchmark dataset. Typical tasks include code generation, code summarization, code completion, and code repair (Yang et al. 2025), but also natural language processing tasks, such as anaphora resolution (i.e., the task of identifying the referring expression of a word or phrase occurring earlier in the text). Metrics may include general metrics for text generation, such as *ROUGE*, *BLEU*, or *METEOR* (Hou et al. 2024), or task-specific metrics, such as *CodeBLEU* for code generation. Benchmarking requires high-quality reference datasets.

## Examples

In SE, benchmarking may include evaluating an LLM’s ability to produce accurate and reliable outputs for a given input (usually a task description, possibly accompanied by data obtained from curated real-world projects or from synthetic SE-specific datasets). *RepairBench* (Silva and Monperrus 2025), for example, contains 574 buggy Java methods and their corresponding fixed versions, which can be used to evaluate the performance of LLMs in code repair tasks. It uses the *Plausible@1* metric (i.e., the probability that the first generated patch passes all test cases) and the *AST Match@1* metric (i.e., the probability that the abstract syntax tree of the first generated patch matches the ground truth patch). *SWE-Bench* (Jimenez et al. 2024) is a more generic benchmark that contains 2,294 SE Python tasks extracted from GitHub pull requests. To score the LLM’s task performance, the benchmark validates whether the generated patch successfully compiles and calculates the percentage of passed test cases. Meanwhile, *HumanEval* (Chen et al. 2021) is often used to assess code generation.

## References

Chen, Mark, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Pondé de Oliveira Pinto, Jared Kaplan, Harri Edwards, et al. 2021. “Evaluating Large Language Models Trained on Code.” *CoRR* abs/2107.03374. <https://arxiv.org/abs/2107.03374>.

Hou, Xinyi, Yanjie Zhao, Yue Liu, Zhou Yang, Kailong Wang, Li Li, Xiapu Luo, David Lo, John Grundy, and Haoyu Wang. 2024. “Large Language Models for Software Engineering: A Systematic Literature Review.” *ACM Trans. Softw. Eng. Methodol.* 33 (8): 220:1–79. <https://doi.org/10.1145/3695988>.

Jimenez, Carlos E., John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik R. Narasimhan. 2024. “SWE-bench: Can Language Models Resolve Real-World Github Issues?” In *The Twelfth International Conference on Learning Representations, ICLR 2024, Vienna, Austria, May 7-11, 2024*. OpenReview.net. <https://openreview.net/forum?id=VTF8yNQM66>.

Silva, André, and Martin Monperrus. 2025. “RepairBench: Leaderboard of Frontier Models for Program Repair.” In *IEEE/ACM International Workshop on Large Language Models for Code, LLM4Code@ICSE 2025, Ottawa, ON, Canada, May 3, 2025*, 9–16. IEEE. <https://doi.org/10.1109/LLM4CODE66737.2025.00006>.

Yang, Yifan, Jiho Shin, Byeonggyu Choi, Minjun Park, Dayun Ju, Changmin Lee, Sanghyuk Chun, Dongjin Kang, Jiin Kim, and Sungroh Yoon. 2025. “From Code Foundation Models to Agents and Applications: A Comprehensive Survey and Practical Guide to Code Intelligence.” *arXiv Preprint arXiv:2502.11827*.

