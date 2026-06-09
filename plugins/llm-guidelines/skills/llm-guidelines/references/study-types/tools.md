# LLMs for New Software Engineering Tools

In this role, LLMs serve as components of new tools that assist software engineers (e.g., with code comprehension or test generation) or as autonomous agents that perform multi-step tasks on their behalf.

## Description

New LLM-based tools support software engineers in their daily tasks, such as code comprehension (Yan et al. 2024) and test case generation (Schäfer et al. 2024). One way of integrating LLM-based tools into software engineers’ workflows is using GenAI agents. Unlike traditional LLM-based tools, these agents are capable of acting autonomously and proactively, are often tailored to meet specific user needs (e.g., via context files or domain-specific tools), and can interact with external environments (e.g., file systems, shells, or web APIs) (Wiesinger, Marlow, and Vuskovic 2025; Yang et al. 2025). From an architectural perspective, GenAI agents can be implemented in various ways (Wiesinger, Marlow, and Vuskovic 2025), but at their core they run a control loop around the LLM (observe → inspect → choose → act) (Raschka 2026). Each chosen action (e.g., a tool call) produces a result that the agent feeds back into the next iteration, until the task is complete. *CoALA* (Sumers et al. 2024) offers a conceptual framework for organizing such agents. For coding agents specifically, Raschka (2026) identifies building blocks such as the repository context gathered before each call, the constructed prompt and its tool definitions, structured session memory, and delegation to bounded subagents. Because these architectures vary, researchers can test and compare them to study how design choices affect downstream performance.

## Examples

Yan et al. (2024) proposed *IVIE*, a tool integrated into the VS Code graphical interface that generates and explains code using LLMs. The authors focused more on the presentation, providing a user-friendly interface to interact with the LLM. Schäfer et al. (2024) presented a large-scale empirical evaluation on the effectiveness of LLMs for automated unit test generation. They presented *TestPilot*, a tool that implements an approach in which the LLM is provided with prompts that include the signature and implementation of a function under test, along with usage examples extracted from the documentation. Richards and Wessel (2024) introduced a preliminary GenAI agent designed to assist developers in understanding source code by incorporating a reasoning component grounded in the theory of mind. Takerngsaksiri et al. (2025) presented *HULA*, a multi-agent system deployed in Atlassian JIRA that lets engineers refine LLM-generated coding plans and source code, and reported acceptance and modification rates from real users.

## References

Raschka, Sebastian. 2026. “Components of a Coding Agent.” <https://magazine.sebastianraschka.com/p/components-of-a-coding-agent>.

Richards, Jonan, and Mairieli Wessel. 2024. “What You Need Is What You Get: Theory of Mind for an LLM-Based Code Understanding Assistant.” In *IEEE International Conference on Software Maintenance and Evolution, ICSME 2024*, 666–71. IEEE. <https://doi.org/10.1109/ICSME58944.2024.00070>.

Schäfer, Max, Sarah Nadi, Aryaz Eghbali, and Frank Tip. 2024. “An Empirical Evaluation of Using Large Language Models for Automated Unit Test Generation.” *IEEE Trans. Software Eng.* 50 (1): 85–105. <https://doi.org/10.1109/TSE.2023.3334955>.

Sumers, Theodore R., Shunyu Yao, Karthik Narasimhan, and Thomas L. Griffiths. 2024. “Cognitive Architectures for Language Agents.” *Trans. Mach. Learn. Res.* 2024. <https://openreview.net/forum?id=1i6ZCvflQJ>.

Takerngsaksiri, Wannita, Jirat Pasuksmit, Patanamon Thongtanunam, Chakkrit Tantithamthavorn, Ruixiong Zhang, Fan Jiang, Jing Li, Evan Cook, Kun Chen, and Ming Wu. 2025. “Human-in-the-Loop Software Development Agents.” In *47th IEEE/ACM International Conference on Software Engineering: Software Engineering in Practice, SEIP@ICSE 2025, Ottawa, ON, Canada, April 27 - May 3, 2025*, 342–52. IEEE. <https://doi.org/10.1109/ICSE-SEIP66354.2025.00036>.

Wiesinger, Julia, Patrick Marlow, and Vladimir Vuskovic. 2025. “Agents.” Google Whitepaper, <https://www.kaggle.com/whitepaper-agents>.

Yan, Litao, Alyssa Hwang, Zhiyuan Wu, and Andrew Head. 2024. “Ivie: Lightweight Anchored Explanations of Just-Generated Code.” In *Proceedings of the CHI Conference on Human Factors in Computing Systems, CHI 2024*, edited by Florian ’Floyd’Mueller, Penny Kyburz, Julie R. Williamson, Corina Sas, Max L. Wilson, Phoebe O. Toups Dugas, and Irina Shklovski, 140:1–15. ACM. <https://doi.org/10.1145/3613904.3642239>.

Yang, Yifan, Jiho Shin, Byeonggyu Choi, Minjun Park, Dayun Ju, Changmin Lee, Sanghyuk Chun, Dongjin Kang, Jiin Kim, and Sungroh Yoon. 2025. “From Code Foundation Models to Agents and Applications: A Comprehensive Survey and Practical Guide to Code Intelligence.” *arXiv Preprint arXiv:2502.11827*.
