"""schema_checks.py — llm-guidelines schema rule for the assessment report.

One check:

  guideline-block-missing-label   `llm-guidelines-report.md`: a `### <name>`
                                  block inside `## Per-guideline findings`
                                  is missing one of the four labels
                                  (`- Status:`, `- Evidence:`, `- Gaps:`,
                                  `- Pointers:`).

The linter (`lint_markdown.py`, synced from pymarkdown-skill) loads this
file via importlib and calls `schema_findings(text, path)` at lint time.
"""
import re

SKILL_NAME = "llm-guidelines"

REPORT_H1_BODY = "LLM Guidelines Assessment"
PER_GUIDELINE_H2_BODY = "Per-guideline findings"
FINDING_LABELS = (
    "- Status:",
    "- Evidence:",
    "- Gaps:",
    "- Pointers:",
)

HEADING_RE = re.compile(r'^(#{1,6})\s+(.*)$')
FENCE_OPENER_RE = re.compile(r'^(`{3,})')
FENCE_CLOSER_RE = re.compile(r'^(`{3,})\s*$')


def schema_findings(text, path):
    findings = []
    lines = text.split('\n')
    if lines and lines[-1] == '':
        lines = lines[:-1]

    in_fence = None
    in_frontmatter = lines and lines[0].strip() == '---'
    is_report = False
    in_per_guideline_section = False
    guideline_blocks = []
    current_guideline = None

    for i, line in enumerate(lines, 1):
        if in_frontmatter:
            if i > 1 and line.strip() == '---':
                in_frontmatter = False
            continue
        if in_fence is not None:
            m = FENCE_CLOSER_RE.match(line)
            if m and len(m.group(1)) >= in_fence:
                in_fence = None
            continue
        m = FENCE_OPENER_RE.match(line)
        if m:
            in_fence = len(m.group(1))
            continue

        hm = HEADING_RE.match(line)
        if hm:
            level = len(hm.group(1))
            body = hm.group(2).rstrip().rstrip('#').rstrip()
            if level == 1 and not is_report:
                if body == REPORT_H1_BODY:
                    is_report = True
            if level == 2:
                if body == PER_GUIDELINE_H2_BODY:
                    in_per_guideline_section = True
                else:
                    in_per_guideline_section = False
            elif level == 1:
                in_per_guideline_section = False
            if in_per_guideline_section and level == 3:
                if current_guideline is not None:
                    guideline_blocks.append(current_guideline)
                current_guideline = (i, body, [])
            else:
                if current_guideline is not None:
                    guideline_blocks.append(current_guideline)
                    current_guideline = None
            continue

        if current_guideline is not None:
            current_guideline[2].append(line)

    if current_guideline is not None:
        guideline_blocks.append(current_guideline)

    if is_report:
        for header_line, _body, content in guideline_blocks:
            joined = '\n'.join(content)
            for label in FINDING_LABELS:
                if label not in joined:
                    findings.append((
                        header_line, 'guideline-block-missing-label',
                        f'guideline block is missing `{label}`',
                    ))

    return findings
