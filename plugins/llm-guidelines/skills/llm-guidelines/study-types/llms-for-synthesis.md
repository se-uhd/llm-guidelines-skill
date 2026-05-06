# LLMs for Synthesis

## Description

Unlike annotation (see [*LLMs as Annotators*](../study-types/llms-as-annotators.md)), which focuses on categorizing or labeling individual data points, synthesis refers to the process of integrating and interpreting information from multiple sources to generate higher-level insights, identify patterns across datasets, and develop conceptual frameworks or theories. LLMs may be able to support synthesis tasks in SE research by processing and distilling information from qualitative data sources. Although synthesis in the preceding notion refers to abstraction and interpretation across multiple data sources, the term is sometimes also used to refer to generating synthetic content (e.g., source code, bug-fix pairs, requirements, etc.) that are then used in downstream tasks to train, fine-tune, or evaluate existing models or tools. In this case, the synthesis is done primarily using the LLM and its training data; the input is limited to basic instructions and examples.

## Examples

Published examples of applying LLMs for synthesis in SE remain scarce; however, some recent work in other domains is instructive (Bano et al. 2024). Barros et al. (2025) (Barros et al. 2025) conducted a systematic mapping study on using LLMs for qualitative research and found that most studies focused on the healthcare and social sciences. In these studies, LLMs supported qualitative methods, such as grounded theory and thematic analysis, by aiding in pattern identification. In SE, de Morais Leca et al. (Morais Leça et al. 2025) explored how LLMs have been applied for qualitative data analysis (QDA) and proposed general strategies and guidelines for their application. Ornelas et al. (Ornelas et al. 2025) complemented this perspective by studying the opportunities and limitations of introducing LLM-based support into QDA, and by formulating recommendations for embedding human–AI collaboration across the thematic analysis phases. Building on these, subsequent work has proposed hybrid frameworks combining LLM support with human-led QDA. Rashid et al. (Rasheed et al. 2024) designed an LLM-driven multi-agent system that integrates AI with human decision-making to automate qualitative data analysis methods. Their system generated initial codes, developed themes, and summarized text. Similarly, Montes et al. (Montes et al. 2025) compared the performance of humans and LLMs in coding, theme development, definition, and refinement, creating guidelines for a hybrid-LLM framework. Finally, El-Hajjami and Salinesi (2025)’s work is an example of using LLMs to create synthetic datasets. They present an approach to generate synthetic requirements, showing that they “*can match or surpass human-authored requirements for specific classification tasks*” (El-Hajjami and Salinesi 2025).

## References

Bano, Muneera, Rashina Hoda, Didar Zowghi, and Christoph Treude. 2024. “Large Language Models for Qualitative Research in Software Engineering: Exploring Opportunities and Challenges.” *Autom. Softw. Eng.* 31 (1): 8. <https://doi.org/10.1007/S10515-023-00407-8>.

Barros, Cauã Ferreira, Bruna Borges Azevedo, Valdemar Vicente Graciano Neto, Mohamad Kassab, Marcos Kalinowski, Hugo Alexandre Dantas do Nascimento, and Michelle C. G. S. P. Bandeira. 2025. “Large Language Model for Qualitative Research: A Systematic Mapping Study.” In *IEEE/ACM International Workshop on Methodological Issues with Empirical Studies in Software Engineering, WSESE@ICSE 2025, Ottawa, ON, Canada, May 3, 2025*, 48–55. IEEE. <https://doi.org/10.1109/WSESE66602.2025.00015>.

El-Hajjami, Abdelkarim, and Camille Salinesi. 2025. “How Good Are Synthetic Requirements? Evaluating LLM-Generated Datasets for AI4RE.” *CoRR* abs/2506.21138. <https://doi.org/10.48550/ARXIV.2506.21138>.

Montes, Cristina Martinez, Robert Feldt, Cristina Miguel Martos, Sofia Ouhbi, Shweta Premanandan, and Daniel Graziotin. 2025. “Large Language Models in Thematic Analysis: Prompt Engineering, Evaluation, and Guidelines for Qualitative Software Engineering Research.” *CoRR* abs/2510.18456. <https://doi.org/10.48550/ARXIV.2510.18456>.

Morais Leça, Matheus de, Lucas Valença, Reydne Santos, and Ronnie de Souza Santos. 2025. “Applications and Implications of Large Language Models in Qualitative Analysis: A New Frontier for Empirical Software Engineering.” In *IEEE/ACM International Workshop on Methodological Issues with Empirical Studies in Software Engineering, WSESE@ICSE 2025, Ottawa, ON, Canada, May 3, 2025*, 36–43. IEEE. <https://doi.org/10.1109/WSESE66602.2025.00013>.

Ornelas, Tatiane, Allysson Allex Araújo, Júlia Araújo, Marina Araújo, Bianca Trinkenreich, and Marcos Kalinowski. 2025. “LLM-Assisted Thematic Analysis: Opportunities, Limitations, and Recommendations.” *CoRR* abs/2511.14528. <https://doi.org/10.48550/ARXIV.2511.14528>.

Rasheed, Zeeshan, Muhammad Waseem, Aakash Ahmad, Kai-Kristian Kemell, Xiaofeng Wang, Anh Nguyen-Duc, and Pekka Abrahamsson. 2024. “Can Large Language Models Serve as Data Analysts? A Multi-Agent Assisted Approach for Qualitative Data Analysis.” *CoRR* abs/2402.01386. <https://doi.org/10.48550/ARXIV.2402.01386>.

