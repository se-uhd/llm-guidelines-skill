#!/usr/bin/env python3
"""Smoke tests for the llm-guidelines lint_markdown wrapper.

Exercises the vendored PyMarkdown tree, the pre-pass checks for issues
PyMarkdown silently accepts, the `llm-guidelines-report.md` schema check,
and `--fix` mode end-to-end. Exits 0 if all tests pass; non-zero on the
first failure with a summary.
"""
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent
LINTER = SCRIPTS / 'lint_markdown.py'
PYTHON = sys.executable


def run(*args):
    result = subprocess.run(
        [PYTHON, str(LINTER), *args], capture_output=True, text=True,
    )
    return result.returncode, result.stdout, result.stderr


def write(d, name, content_bytes):
    p = Path(d) / name
    p.write_bytes(content_bytes)
    return p


def test_clean_file_passes():
    with tempfile.TemporaryDirectory() as d:
        p = write(d, 'doc.md', b"# Title\n\nbody\n")
        rc, out, err = run(str(p))
        assert rc == 0, f"clean: rc={rc} out={out!r} err={err!r}"
        assert out == '', f"clean: stdout should be empty, got {out!r}"


def test_vendored_tree_loads():
    # Wrapper exits 2 when _vendor/ is missing; conversely, a clean
    # invocation against a real file proves it loaded successfully.
    with tempfile.TemporaryDirectory() as d:
        p = write(d, 'doc.md', b"# Title\n\nbody\n")
        rc, _out, err = run(str(p))
        assert rc == 0, f"vendored tree load failed: err={err!r}"


def test_pre_pass_crlf():
    with tempfile.TemporaryDirectory() as d:
        p = write(d, 'doc.md', b"# Title\r\n\r\nbody\r\n")
        rc, out, _err = run(str(p))
        assert rc == 1, f"crlf: rc={rc}"
        assert 'crlf-line-endings' in out, f"crlf: {out!r}"


def test_pre_pass_unclosed_fence():
    with tempfile.TemporaryDirectory() as d:
        p = write(d, 'doc.md', b"# Title\n\n```python\nfoo\n")
        rc, out, _err = run(str(p))
        assert rc == 1, f"fence: rc={rc}"
        assert 'unclosed-fence' in out, f"fence: {out!r}"


def test_pre_pass_unclosed_frontmatter():
    with tempfile.TemporaryDirectory() as d:
        p = write(d, 'doc.md', b"---\nname: test\n\n# Title\n\nbody\n")
        rc, out, _err = run(str(p))
        assert rc == 1, f"frontmatter: rc={rc}"
        assert 'unclosed-frontmatter' in out, f"frontmatter: {out!r}"


def test_pymarkdown_rule_fires():
    with tempfile.TemporaryDirectory() as d:
        # MD022 — heading not surrounded by blank lines.
        p = write(d, 'doc.md', b"# Title\nimmediately after H1\n")
        rc, out, _err = run(str(p))
        assert rc == 1, f"md022: rc={rc}"
        assert 'md022' in out, f"md022: {out!r}"


def test_schema_guideline_missing_label():
    content = (
        b"# LLM Guidelines Assessment\n\n"
        b"## Per-guideline findings\n\n"
        b"### Test Guideline\n\n"
        b"- Status: covered\n- Evidence: x.\n"
    )
    with tempfile.TemporaryDirectory() as d:
        p = write(d, 'llm-guidelines-report.md', content)
        rc, out, _err = run(str(p))
        assert rc == 1, f"schema: rc={rc}"
        assert 'guideline-block-missing-label' in out, f"schema: {out!r}"
        assert 'Gaps' in out and 'Pointers' in out, \
            f"schema: missing label names not surfaced: {out!r}"


def test_schema_guideline_clean_passes():
    content = (
        b"# LLM Guidelines Assessment\n\n"
        b"## Per-guideline findings\n\n"
        b"### Test Guideline\n\n"
        b"- Status: covered\n"
        b"- Evidence: x.\n"
        b"- Gaps: none.\n"
        b"- Pointers: ./guidelines/x.md\n"
    )
    with tempfile.TemporaryDirectory() as d:
        p = write(d, 'llm-guidelines-report.md', content)
        rc, out, _err = run(str(p))
        assert rc == 0, f"clean schema: rc={rc} out={out!r}"


def test_schema_ignores_headings_in_fence():
    # `### Test Guideline` inside a fenced code block must NOT be treated
    # as a real guideline block by the schema check.
    content = (
        b"# LLM Guidelines Assessment\n\n"
        b"## Example\n\n"
        b"````markdown\n"
        b"### Test Guideline\n"
        b"- Status: covered\n"
        b"````\n\n"
        b"## Per-guideline findings\n\n"
        b"### Real Guideline\n\n"
        b"- Status: covered\n"
        b"- Evidence: x.\n"
        b"- Gaps: none.\n"
        b"- Pointers: ./x.md\n"
    )
    with tempfile.TemporaryDirectory() as d:
        p = write(d, 'llm-guidelines-report.md', content)
        rc, out, _err = run(str(p))
        assert rc == 0, f"fenced heading: rc={rc} out={out!r}"


def test_fix_mode_normalizes():
    # Multiple blank lines and missing trailing newline are auto-fixed.
    content = b"# Title\n\n\n\n\nbody\nmore"
    with tempfile.TemporaryDirectory() as d:
        p = write(d, 'doc.md', content)
        rc, out, err = run('--fix', str(p))
        assert rc == 0, f"fix: rc={rc} out={out!r} err={err!r}"
        fixed = p.read_bytes()
        assert fixed.endswith(b'\n'), f"fix: missing trailing newline: {fixed!r}"
        import re as _re
        assert not _re.search(rb'\n{4,}', fixed), \
            f"fix: still has >2 consecutive blank lines: {fixed!r}"


TESTS = [
    test_clean_file_passes,
    test_vendored_tree_loads,
    test_pre_pass_crlf,
    test_pre_pass_unclosed_fence,
    test_pre_pass_unclosed_frontmatter,
    test_pymarkdown_rule_fires,
    test_schema_guideline_missing_label,
    test_schema_guideline_clean_passes,
    test_schema_ignores_headings_in_fence,
    test_fix_mode_normalizes,
]


def main():
    failed = 0
    for t in TESTS:
        try:
            t()
            print(f"PASS  {t.__name__}")
        except AssertionError as e:
            print(f"FAIL  {t.__name__}: {e}", file=sys.stderr)
            failed += 1
        except Exception as e:
            print(f"ERROR {t.__name__}: {type(e).__name__}: {e}", file=sys.stderr)
            failed += 1
    if failed:
        print(f"\n{failed}/{len(TESTS)} failure(s)", file=sys.stderr)
        return 1
    print(f"\nAll {len(TESTS)} tests passed.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
