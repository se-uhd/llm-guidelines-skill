# LLMs for New Software Engineering Tools

## Description

LLMs are being integrated into new tools that support software engineers in their daily tasks (e.g., to assist in code comprehension (Yan et al. 2024) and test case generation (Schäfer et al. 2024)). One way of integrating LLM-based tools into software engineers’ workflows is using GenAI agents. Unlike traditional LLM-based tools, these agents are capable of acting autonomously and proactively, are often tailored to meet specific user needs, and can interact with external environments (Wiesinger, Marlow, and Vuskovic 2025; Yang et al. 2025). From an architectural perspective, GenAI agents can be implemented in various ways (Wiesinger, Marlow, and Vuskovic 2025). However, they generally share three key components: (1) a reasoning mechanism that guides the LLM (often enabled by advanced prompt engineering), (2) a set of tools to interact with external systems (e.g., APIs or databases), and (3) a user communication interface that extends beyond traditional chat-based interactions (Sumers et al. 2024; Zhou et al. 2023). Researchers can also test and compare different tool architectures to increase artifact quality and developer satisfaction.

## Examples

Yan et al. (2024) proposed *IVIE*, a tool integrated into the VS Code graphical interface that generates and explains code using LLMs. The authors focused more on the presentation, providing a user-friendly interface to interact with the LLM. Schäfer et al. (2024) presented a large-scale empirical evaluation on the effectiveness of LLMs for automated unit test generation. They presented *TestPilot*, a tool that implements an approach in which the LLM is provided with prompts that include the signature and implementation of a function under test, along with usage examples extracted from the documentation. Richards and Wessel (2024) introduced a preliminary GenAI agent designed to assist developers in understanding source code by incorporating a reasoning component grounded in the theory of mind. Takerngsaksiri et al. (2025) present *HULA*, a multi-agent system deployed in Atlassian JIRA that lets engineers refine LLM-generated coding plans and source code, and report acceptance and modification rates from real users.

## References

Richards, Jonan, and Mairieli Wessel. 2024. “What You Need Is What You Get: Theory of Mind for an LLM-Based Code Understanding Assistant.” In *IEEE International Conference on Software Maintenance and Evolution, ICSME 2024*, 666–71. IEEE. <https://doi.org/10.1109/ICSME58944.2024.00070>.

Schäfer, Max, Sarah Nadi, Aryaz Eghbali, and Frank Tip. 2024. “An Empirical Evaluation of Using Large Language Models for Automated Unit Test Generation.” *IEEE Trans. Software Eng.* 50 (1): 85–105. <https://doi.org/10.1109/TSE.2023.3334955>.

Sumers, Theodore R., Shunyu Yao, Karthik Narasimhan, and Thomas L. Griffiths. 2024. “Cognitive Architectures for Language Agents.” *Trans. Mach. Learn. Res.* 2024. <https://openreview.net/forum?id=1i6ZCvflQJ>.

Takerngsaksiri, Wannita, Jirat Pasuksmit, Patanamon Thongtanunam, Chakkrit Tantithamthavorn, Ruixiong Zhang, Fan Jiang, Jing Li, Evan Cook, Kun Chen, and Ming Wu. 2025. “Human-in-the-Loop Software Development Agents.” In *47th IEEE/ACM International Conference on Software Engineering: Software Engineering in Practice, SEIP@ICSE 2025, Ottawa, ON, Canada, April 27 - May 3, 2025*, 342–52. IEEE. <https://doi.org/10.1109/ICSE-SEIP66354.2025.00036>.

Wiesinger, Julia, Patrick Marlow, and Vladimir Vuskovic. 2025. “Agents.” *Google DeepMind*. <https://gemini.google.com>.

Yan, Litao, Alyssa Hwang, Zhiyuan Wu, and Andrew Head. 2024. “Ivie: Lightweight Anchored Explanations of Just-Generated Code.” In *Proceedings of the CHI Conference on Human Factors in Computing Systems, CHI 2024*, edited by Florian ’Floyd’Mueller, Penny Kyburz, Julie R. Williamson, Corina Sas, Max L. Wilson, Phoebe O. Toups Dugas, and Irina Shklovski, 140:1–15. ACM. <https://doi.org/10.1145/3613904.3642239>.

Yang, Yifan, Jiho Shin, Byeonggyu Choi, Minjun Park, Dayun Ju, Changmin Lee, Sanghyuk Chun, Dongjin Kang, Jiin Kim, and Sungroh Yoon. 2025. “From Code Foundation Models to Agents and Applications: A Comprehensive Survey and Practical Guide to Code Intelligence.” *arXiv Preprint arXiv:2502.11827*.

Zhou, Wangchunshu, Yuchen Eleanor Jiang, Long Li, Jialong Wu, Tiannan Wang, Shi Qiu, Jintian Zhang, et al. 2023. “Agents: An Open-Source Framework for Autonomous Language Agents.” *CoRR* abs/2309.07870. <https://doi.org/10.48550/ARXIV.2309.07870>.

