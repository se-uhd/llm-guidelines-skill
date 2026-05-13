#!/usr/bin/env python3
"""lint_markdown.py [--fix] <path>

Lint a Markdown file against the GFM dialect using the vendored PyMarkdown
tree under `_vendor/`, and apply the project-specific schema check for
`llm-guidelines-report.md`.

The vendored tree is refreshed by `refresh_vendor.py` (maintainer-only).
End users never need to install anything; the bundle is self-contained.

Dialect
-------
GitHub-Flavored Markdown via PyMarkdown's CommonMark base plus the
`markdown-tables`, `markdown-task-list-items`, `markdown-strikethrough`,
`markdown-extended-autolinks`, and `front-matter` extensions. Disabled
plugins (`md013`, `md033`, `md041`) are noisy or report-template-
incompatible.

Pre-pass checks
---------------
PyMarkdown silently accepts these, so the wrapper runs a small pre-pass
on the raw bytes before pymarkdown is invoked:

  crlf-line-endings     CR or CRLF line ending anywhere in the file.
  unclosed-fence        a fenced code block has no matching closer.
  unclosed-frontmatter  a leading `---` has no matching `---`.

Schema check
------------
  guideline-block-missing-label   `llm-guidelines-report.md`: a `### <name>`
                                  block inside `## Per-guideline findings`
                                  is missing one of the four labels
                                  (`- Status:`, `- Evidence:`, `- Gaps:`,
                                  `- Pointers:`).

CLI
---
  python3 lint_markdown.py <path>
  python3 lint_markdown.py --fix <path>

Stdout: one finding per line, tab-separated `<path>:<line>\\t<rule>\\t<message>`.
Stderr: one-line summary `checked <path>; <N> finding(s)`.

Exit codes
----------
  0  clean.
  1  one or more findings (after --fix, if used).
  2  could not read or run the linter.
"""
import argparse
import contextlib
import io
import re
import runpy
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
VENDOR_DIR = SCRIPTS_DIR / "_vendor"
CONFIG_FILE = SCRIPTS_DIR / "lint_markdown.yaml"

if not VENDOR_DIR.is_dir():
    sys.stderr.write(
        f"lint_markdown.py: vendored tree not found at {VENDOR_DIR}; "
        f"run refresh_vendor.py\n"
    )
    sys.exit(2)

sys.path.insert(0, str(VENDOR_DIR))

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
PYMARKDOWN_LINE_RE = re.compile(
    r'^(?P<path>.+?):(?P<line>\d+):\d+:\s+(?P<rule>[A-Za-z0-9_]+):\s+'
    r'(?P<message>.+?)(?:\s+\((?P<aliases>[^)]+)\))?\s*$'
)


def pre_findings(raw_text):
    """Findings PyMarkdown silently accepts but the bundle should still flag.

    Runs on the raw text (with CR/CRLF preserved) before pymarkdown is
    invoked. Reports CRLF / lone CR once per file, an unclosed fenced code
    block, and an unclosed YAML frontmatter block.
    """
    findings = []

    if '\r' in raw_text:
        line_no = 1
        for ch in raw_text:
            if ch == '\r':
                findings.append((
                    line_no, 'crlf-line-endings',
                    'CR or CRLF line ending; pymarkdown silently accepts this',
                ))
                break
            if ch == '\n':
                line_no += 1

    norm = raw_text.replace('\r\n', '\n').replace('\r', '\n')
    lines = norm.split('\n')
    if lines and lines[-1] == '':
        lines = lines[:-1]

    fence_width = None
    fence_open_line = None
    for ln, line in enumerate(lines, 1):
        if fence_width is not None:
            m = FENCE_CLOSER_RE.match(line)
            if m and len(m.group(1)) >= fence_width:
                fence_width = None
                fence_open_line = None
            continue
        m = FENCE_OPENER_RE.match(line)
        if m:
            fence_width = len(m.group(1))
            fence_open_line = ln
    if fence_width is not None:
        findings.append((
            fence_open_line, 'unclosed-fence',
            f'{fence_width}-backtick fence opened with no matching closer',
        ))

    if lines and lines[0].strip() == '---':
        closed = any(line.strip() == '---' for line in lines[1:])
        if not closed:
            findings.append((
                1, 'unclosed-frontmatter',
                'leading `---` has no matching close',
            ))

    return findings


def run_pymarkdown(subcommand, path, config=None):
    argv = [
        "pymarkdown",
        "--no-json5",
        "--config", str(config or CONFIG_FILE),
        "--return-code-scheme", "minimal",
        subcommand, str(path),
    ]
    saved_argv = sys.argv
    sys.argv = argv
    out_buf = io.StringIO()
    err_buf = io.StringIO()
    rc = 0
    try:
        with contextlib.redirect_stdout(out_buf), \
             contextlib.redirect_stderr(err_buf):
            try:
                runpy.run_module("pymarkdown", run_name="__main__",
                                 alter_sys=True)
            except SystemExit as exc:
                rc = int(exc.code) if exc.code is not None else 0
    finally:
        sys.argv = saved_argv
    return rc, out_buf.getvalue(), err_buf.getvalue()


def schema_findings(text):
    """Apply the llm-guidelines-report.md schema check."""
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


def parse_pymarkdown_stdout(stdout):
    findings = []
    for raw in stdout.splitlines():
        m = PYMARKDOWN_LINE_RE.match(raw.rstrip())
        if not m:
            continue
        findings.append((
            int(m.group('line')),
            m.group('rule').lower(),
            m.group('message').strip(),
        ))
    return findings


def main():
    parser = argparse.ArgumentParser(
        description=("Lint a Markdown file via the vendored PyMarkdown "
                     "tree plus the llm-guidelines schema check."),
    )
    parser.add_argument('path', help='Markdown file to check')
    parser.add_argument('--fix', action='store_true',
                        help='apply auto-fixable rules in place, then re-check')
    parser.add_argument('--config', metavar='PATH',
                        help=('override the bundled lint_markdown.yaml '
                              '(useful when linting website-side files '
                              'that need different rule tolerances)'))
    args = parser.parse_args()
    config_override = Path(args.config) if args.config else None

    p = Path(args.path)
    try:
        # read_bytes + decode preserves CR/CRLF so the pre-pass can flag them;
        # read_text would silently normalize via universal newlines mode.
        raw = p.read_bytes().decode('utf-8')
    except (OSError, UnicodeDecodeError) as e:
        sys.stderr.write(f"lint_markdown.py: cannot read {args.path}: {e}\n")
        sys.exit(2)

    if args.fix:
        rc_fix, _, _ = run_pymarkdown('fix', p, config=config_override)
        if rc_fix not in (0, 3):
            sys.stderr.write(
                f"lint_markdown.py: pymarkdown fix exited {rc_fix}\n"
            )
        try:
            raw = p.read_bytes().decode('utf-8')
        except (OSError, UnicodeDecodeError) as e:
            sys.stderr.write(
                f"lint_markdown.py: cannot reread {args.path}: {e}\n"
            )
            sys.exit(2)

    rc_scan, stdout, stderr = run_pymarkdown('scan', p, config=config_override)
    if rc_scan not in (0, 1):
        sys.stderr.write(
            f"lint_markdown.py: pymarkdown scan exited {rc_scan}\n{stderr}\n"
        )
        sys.exit(2)

    findings = pre_findings(raw)
    findings.extend(parse_pymarkdown_stdout(stdout))
    findings.extend(schema_findings(raw))
    findings.sort()

    for line_no, rule, message in findings:
        print(f"{args.path}:{line_no}\t{rule}\t{message}")

    sys.stderr.write(f"checked {args.path}; {len(findings)} finding(s)\n")
    sys.exit(0 if not findings else 1)


if __name__ == '__main__':
    main()
