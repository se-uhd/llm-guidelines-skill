# Report Session Traces

> ***Summary***: To address model non-determinism and ensure reproducibility, especially when targeting SaaS-based commercial tools, researchers **should** include full interaction logs (prompts and responses) as *supplementary material* if privacy and confidentiality can be ensured. For agentic systems, interaction logs **should** be extended to cover exchanges between humans and the agent and between external tools and the agent, including human-in-the-loop feedback and approval decisions. Researchers **should** report the complete runtime trace as *supplementary material*, covering both external tool invocations (tool name, arguments, result, ordering) and which configured artifacts (skills, context files, sub-agents reported under [*System and Prompt Design*](../guidelines/report-system-and-prompt-design.md)) were activated, so that readers can attribute task outcomes to the model, the tools, or their interaction pattern. Developed plans **should** be reported as *supplementary material* if available. When full trace disclosure is not feasible, representative or anonymized examples **should** be provided, and unobservable aspects of commercial-tool runs **must** be acknowledged as reproducibility limitations.

## Rationale

A *session* is any bounded stretch of activity during which an LLM is invoked. Sessions cover one-shot prompts, batch runs, multi-turn conversations, and agentic runs that span many tool calls. A *session trace* records everything that crosses the LLM boundary or is produced around the model during that stretch: prompts received, responses returned, tool calls the model made together with their arguments and results, plans the model developed, and which of the statically configured artifacts (e.g., skills, context files, sub-agents, tools) were actually picked up at runtime.

Two kinds of session trace are important to capture. An *interaction log* captures what humans or other software tools sent to the LLM and what the LLM returned. A *runtime trace* captures what the LLM did at runtime: calls to external tools (e.g., APIs, file systems, databases, MCP servers, sub-agents) and activations of configured artifacts (e.g., context files, skills). Reporting both kinds is needed for an agentic run, because neither tells the full story on its own.

Even with the exact same prompts, decoding strategies, and parameters, LLMs can behave non-deterministically. Non-determinism can arise from probabilistic sampling and, even with greedy decoding (temperature = 0), from batching and floating-point arithmetic on GPUs (Yuan et al. 2025), and from Mixture-of-Experts routing (Chann 2023). For other researchers to verify the conclusions drawn from LLM interactions, the traces of what happened at runtime are often as important as the design of the system itself. This matters particularly for studies targeting commercial software-as-a-service (SaaS) solutions such as ChatGPT, and for agentic runs where behavior depends on how the model chose among many possible tool calls.

The rationale is similar to reporting interview transcripts in qualitative research. Just as a human participant might give different answers to the same question asked two months apart, the responses from tools such as ChatGPT can also vary over time, and the trace of an agent’s decisions on any given run is often not reproducible at a later date. This guideline addresses runtime reporting and complements [*System and Prompt Design*](../guidelines/report-system-and-prompt-design.md), which covers the static artifacts that determine what the model sees.

## Recommendations

### Interaction Logs:

Researchers **should** report the full interaction logs (prompts sent to the LLM and responses returned) as part of their *supplementary material*. For agentic systems, interaction logs generalize to cover exchanges between humans and the agent as well as between external tools and the agent, including human-in-the-loop feedback, approval or rejection decisions, and iterative refinements. These **should** also be reported as *supplementary material* so that readers can reconstruct the sequence of exchanges and assess human oversight decisions. For traces containing sensitive information, researchers **must** anonymize personal identifiers, replace proprietary code with placeholders, and clearly highlight modified sections.

### Runtime Traces:

When an LLM calls out to external tools (e.g., APIs, file systems, databases, MCP servers, sub-agents) or activates configured artifacts (e.g., context files, skills, sub-agents reported under [*System and Prompt Design*](../guidelines/report-system-and-prompt-design.md)), this runtime activity forms a *runtime trace* distinct from the interaction log. Researchers **should** report the complete runtime trace as *supplementary material*, including for each entry the tool or artifact name, arguments (if any), result, and ordering relative to surrounding interaction-log entries. This lets readers attribute task success to the model, the external tools, or their interaction pattern, and distinguish artifacts that were configured from those that actually influenced a given run. Researchers **should** record runtime traces in an open format compatible with the OpenTelemetry Protocol (OTLP), such as the OpenTelemetry GenAI semantic conventions (OpenTelemetry Authors 2026) or OpenInference (Arize AI 2026), and report the version used, rather than a study-specific schema.

### Agentic Plans:

For agentic systems that autonomously plan and execute tasks, the developed plans **should** be reported as *supplementary material* if available. In Claude Code, for example, a plan is a short Markdown document the user can open and edit during a session, listing the proposed steps and the files or commands the agent intends to touch. Other frameworks such as LangGraph keep plans inside the agent’s internal execution state.

All reported traces **must** be made publicly available as *supplementary material*, subject to privacy and confidentiality constraints. When full trace logging is not feasible, researchers **should** provide representative examples or anonymized traces.

## Examples

An example of reporting full interaction logs is the study by Ronanki, Berger, and Horkoff (2023), for which the authors reported the full answers of ChatGPT and uploaded them to [Zenodo](https://zenodo.org/records/8124936). For agentic systems, Bouzenia and Pradel (2025) unified the runtime trajectories of three SE agents (*RepairAgent*, *AutoCodeRover*, *OpenHands*) into a common format and released the resulting 120 trajectories with 2,822 LLM interactions as a public dataset.

## Benefits

Unlike human participant conversations, which often cannot be reported because of confidentiality, LLM interaction logs can be shared. This enables reproduction studies, tracking of response changes over time or across model versions, and secondary research on LLM consistency for specific SE tasks.

For agentic systems, reporting runtime traces alongside interaction logs lets readers attribute task outcomes to the right component: the model, the tool, or the orchestration pattern. Usage traces complement the static configuration reported under [*System and Prompt Design*](../guidelines/report-system-and-prompt-design.md) by showing which of the configured artifacts actually influenced a given run.

## Challenges

Not all systems allow reporting of complete interaction logs with ease, and this hinders transparency and verifiability. For commercial tools, researchers **must** report all available information and acknowledge unknown aspects as limitations. Tool-call traces for commercial SaaS agents are often opaque: the user sees the final response but not the sequence of internal tool calls. When this is the case, authors should document what was and was not observable. For agents running locally or via open-source tools, these traces are usually more accessible and **should** be reported whenever available. Agent frameworks differ in whether and how they log agent-to-agent communication, so reporting practices vary across studies.

## Study Types

Runtime trace reporting requirements depend heavily on the study type and on the accessibility of the underlying system. The general expectation is that interaction logs are reported as *supplementary material* whenever feasible; runtime traces are additionally expected when agentic execution or evaluation harnesses go beyond direct API calls.

For [*Studying LLM Usage*](../study-types/studying-llm-usage-in-software-engineering.md), especially observational studies targeting commercial tools, researchers **must** report the full interaction logs except when transcripts might identify anonymous participants or reveal personal or confidential information. If complete interaction logs cannot be shared (e.g., because they contain confidential information), the prompts and responses **must** at least be summarized and described in the *paper*. For [*LLMs for Tools*](../study-types/llms-for-new-software-engineering-tools.md) that use agentic execution, researchers **should** report runtime traces for the runs used to evaluate the tool. For [*Benchmarking LLMs*](../study-types/benchmarking-llms-for-software-engineering-tasks.md) that use agent-based harnesses, researchers **should** report runtime traces for representative runs, letting readers understand how task success depends on the agent’s decision sequence rather than the model’s raw output alone. For [*LLMs as Annotators*](../study-types/llms-as-annotators.md), [*LLMs as Judges*](../study-types/llms-as-judges.md), [*LLMs for Synthesis*](../study-types/llms-for-synthesis.md), and [*LLMs as Subjects*](../study-types/llms-as-subjects.md), when the research setup involves multi-turn interaction or agentic orchestration, researchers **should** report the corresponding interaction logs and, where applicable, runtime traces.

## Advice for Reviewers

As with other guidelines, missing trace information is typically a minor revision request unless so much is missing that methodological rigor cannot be assessed. Reviewers should recognize that complete trace reporting is easier for local and open-source setups than for commercial SaaS agents. When reviewing commercial-tool studies, reviewers should focus on whether authors have reported everything the system exposed and have been explicit about what remains unobservable.

## See Also

- [Report System and Prompt Design](../guidelines/report-system-and-prompt-design.md): Session traces show runtime behavior; system and prompt design covers the static artifacts that produce it.
- [Report Model Version, Configuration, and Customizations](../guidelines/report-model-version-configuration-and-customizations.md): A trace cannot be reproduced or compared across studies without the model identity that produced it.
- [Use Human Validation for LLM Outputs](../guidelines/use-human-validation-for-llm-outputs.md): Agentic traces produce outputs that often warrant human evaluation.
- [Use an Open LLM as a Baseline](../guidelines/use-an-open-llm-as-a-baseline.md): Open models let other researchers reproduce a reported trace on the exact same model weights.
- [Report Limitations and Mitigations](../guidelines/report-limitations-and-mitigations.md): When a tool hides parts of the trace, authors must report the gap as a limitation.

## References

Arize AI. 2026. “OpenInference: AI Observability and Evaluation Specification.” <https://github.com/Arize-ai/openinference>.

Bouzenia, Islem, and Michael Pradel. 2025. “Understanding Software Engineering Agents: A Study of Thought-Action-Result Trajectories.” In *40th IEEE/ACM International Conference on Automated Software Engineering, ASE 2025, Seoul, Korea, Republic of, November 16-20, 2025*, 2846–57. IEEE. <https://doi.org/10.1109/ASE63991.2025.00234>.

Chann, Sherman. 2023. “Non-determinism in GPT-4 is caused by Sparse MoE.” <https://152334h.github.io/blog/non-determinism-in-gpt-4/>.

OpenTelemetry Authors. 2026. “OpenTelemetry Semantic Conventions for Generative AI.” <https://opentelemetry.io/docs/specs/semconv/gen-ai/>.

Ronanki, Krishna, Christian Berger, and Jennifer Horkoff. 2023. “Investigating ChatGPT’s Potential to Assist in Requirements Elicitation Processes.” In *2023 49th Euromicro Conference on Software Engineering and Advanced Applications (SEAA)*, 354–61. IEEE.

Yuan, Jiayi, Hao Li, Xinheng Ding, Wenya Xie, Yu-Jhe Li, Wentian Zhao, Kun Wan, Jing Shi, Xia Hu, and Zirui Liu. 2025. “Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference.” In *Advances in Neural Information Processing Systems 38: Annual Conference on Neural Information Processing Systems 2025, NeurIPS 2025*. <https://openreview.net/forum?id=Q3qAsZAEZw>.
