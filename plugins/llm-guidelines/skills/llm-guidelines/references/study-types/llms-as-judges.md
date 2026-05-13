# LLMs as Judges

## Description

LLMs can rate properties of software artifacts (e.g. assess code readability, adherence to coding standards, or comment quality) or sort multiple solutions by some attribute. These kinds of judgments are distinct from annotating unstructured text (see [*LLMs as Annotators*](../study-types/llms-as-annotators.md)).

## Examples

Lubos et al. (2024) used [Llama-2](https://www.llama.com/llama2/) to evaluate the quality of software requirements statements. They prompted the LLM with the text below, where the words in braces reflect the study parameters:

    Your task is to evaluate the quality of a software requirement. Evaluate
    whether the following requirement is quality_characteristic.
    quality_characteristic means: quality_characteristic_explanation The
    evaluation result must be: ’yes’ or ’no’. Request: Based on the
    following description of the project: project_description Evaluate the
    quality of the following requirement: requirement. Explain your decision
    and suggest an improved version.

They evaluated LLM output against expert human judges and found moderate agreement for simple requirements and poor agreement for more complex requirements. In contrast, Wang et al. (2025) used an LLM to generate acceptance criteria for user stories, and provided a rubric to an LLM to judge the generated acceptance criteria on interpretable scales (0 to 4).

## References

Lubos, Sebastian, Alexander Felfernig, Thi Ngoc Trang Tran, Damian Garber, Merfat El Mansi, Seda Polat Erdeniz, and Viet-Man Le. 2024. “Leveraging LLMs for the Quality Assurance of Software Requirements.” In *32nd IEEE International Requirements Engineering Conference, RE 2024, Reykjavik, Iceland, June 24-28, 2024*, edited by Grischa Liebel, Irit Hadar, and Paola Spoletini, 389–97. IEEE. <https://doi.org/10.1109/RE59067.2024.00046>.

Wang, Fanyu, Chetan Arora, Yonghui Liu, Kaicheng Huang, Chakkrit Tantithamthavorn, Aldeida Aleti, Dishan Sambathkumar, and David Lo. 2025. “Multi-Modal Requirements Data-Based Acceptance Criteria Generation Using LLMs.” In *40th IEEE/ACM International Conference on Automated Software Engineering, ASE 2025, Seoul, Korea, Republic of, November 16-20, 2025*, 3334–45. IEEE. <https://doi.org/10.1109/ASE63991.2025.00275>.
