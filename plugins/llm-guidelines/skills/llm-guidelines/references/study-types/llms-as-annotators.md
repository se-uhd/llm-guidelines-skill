# LLMs as Annotators

## Description

In qualitative data analysis, manually annotating (“coding”) natural language text (e.g., requirements, interview transcripts, open-ended survey responses) is a time-consuming manual process (Bano et al. 2024). LLMs can augment human coding, suggest new codes, and label artifacts based on a pre-defined coding guide much faster than humans can (He et al. 2024). The extent to which, or under what conditions, LLMs can perform these tasks *effectively* remains an open research question (Ahmed et al. 2025). Indeed, measuring their effectiveness is practically and philosophically challenging. From an interpretivist philosophical perspective, one cannot measure the quality of analysis by comparing one (human or machine) analyst’s work to another. From a realist perspective, triangulating across multiple human judges, LLM judges, and other data sources (e.g., whether a pull request is marked as having resolved an issue) improves confidence in the findings but does not prove that any one judge is valid.

## Examples

Huang et al. (2024) used multiple LLMs for joint annotation of mobile application reviews. They used three models of comparable size with an absolute majority voting rule (i.e., a label is only accepted if it receives more than half of the total votes from the models). This approach slightly outperformed the best individual model tested. Meanwhile, Ahmed et al. (2025) examined LLMs as annotators in SE research across five datasets, six LLMs, and ten annotation tasks. They found that model-model agreement strongly correlates with human-model agreement; models performed poorly in tasks where humans also frequently disagreed. They proposed to use model confidence scores to identify specific samples that could be safely delegated to LLMs, potentially reducing human annotation effort without compromising inter-rater agreement.

## References

Ahmed, Toufique, Premkumar T. Devanbu, Christoph Treude, and Michael Pradel. 2025. “Can LLMs Replace Manual Annotation of Software Engineering Artifacts?” In *22nd IEEE/ACM International Conference on Mining Software Repositories, MSR@ICSE 2025, Ottawa, ON, Canada, April 28-29, 2025*, 526–38. IEEE. <https://doi.org/10.1109/MSR66628.2025.00086>.

Bano, Muneera, Rashina Hoda, Didar Zowghi, and Christoph Treude. 2024. “Large Language Models for Qualitative Research in Software Engineering: Exploring Opportunities and Challenges.” *Autom. Softw. Eng.* 31 (1): 8. <https://doi.org/10.1007/S10515-023-00407-8>.

He, Zeyu, Chieh-Yang Huang, Chien-Kuang Cornelia Ding, Shaurya Rohatgi, and Ting-Hao Kenneth Huang. 2024. “If in a Crowdsourced Data Annotation Pipeline, a GPT-4.” In *Proceedings of the CHI Conference on Human Factors in Computing Systems, CHI 2024*, edited by Florian ’Floyd’Mueller, Penny Kyburz, Julie R. Williamson, Corina Sas, Max L. Wilson, Phoebe O. Toups Dugas, and Irina Shklovski, 1040:1–25. ACM. <https://doi.org/10.1145/3613904.3642834>.

Huang, Jiangping, Bochen Yi, Weisong Sun, Bangrui Wan, Yang Xu, Yebo Feng, Wenguang Ye, and Qinjun Qin. 2024. “Enhancing Review Classification via LLM-Based Data Annotation and Multi-Perspective Feature Representation Learning.” *SSRN Electronic Journal*, 1–15. <https://doi.org/10.2139/ssrn.5002351>.

