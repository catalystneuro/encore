"""Tests for tools/transcript.py: what a published transcript keeps and leaves out."""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))

import transcript as tool  # noqa: E402


def write_run(path: Path, events: list[dict]) -> Path:
    path.write_text("\n".join(json.dumps(e) for e in events) + "\n")
    return path


def call(id_, name, **input_):
    return {"type": "assistant", "message": {"content": [{"type": "tool_use", "id": id_, "name": name, "input": input_}]}}


def result(id_, text):
    return {"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": id_, "content": text}]}}


RUN = [
    {"type": "system", "subtype": "init", "model": "claude-opus-5-5", "permissionMode": "dontAsk", "tools": ["Bash"]},
    {"type": "user", "message": {"content": "Attempt dandiset 000001.<system-reminder>private context</system-reminder>"}},
    {"type": "assistant", "message": {"content": [{"type": "thinking", "thinking": "secret reasoning"},
                                                  {"type": "text", "text": "Reading the paper first."}]}},
    call("a", "WebFetch", url="https://doi.org/10.1000/demo", prompt="read"),
    result("a", "Full text of the paper, paragraph after paragraph."),
    call("b", "Bash", command="curl -sL https://example.org/paper.html -o paper/p.html"),
    result("b", "downloaded"),
    call("c", "Bash", command="sed -n 1,40p paper/p.txt"),
    result("c", "Methods. We recorded from twenty patients."),
    call("d", "Bash", command="python analysis.py"),
    result("d", "\n".join(f"line {i}" for i in range(100))),
    {"type": "assistant", "parent_tool_use_id": "x", "message": {"content": [{"type": "text", "text": "Subagent says hi."}]}},
    {"type": "result", "subtype": "success", "num_turns": 7, "duration_ms": 120000},
]


def test_keeps_the_run_and_leaves_out_context_thinking_and_paper_text(tmp_path):
    text = tool.render(write_run(tmp_path / "run.jsonl", RUN), "Demo")
    assert "Attempt dandiset 000001." in text and "Reading the paper first." in text
    assert "python analysis.py" in text and "Subagent says hi." in text
    assert "https://doi.org/10.1000/demo" in text
    for gone in ("private context", "secret reasoning", "paragraph after paragraph", "twenty patients"):
        assert gone not in text


def test_long_tool_output_is_cut(tmp_path):
    text = tool.render(write_run(tmp_path / "run.jsonl", RUN), "Demo")
    assert "line 19" in text and "line 20" not in text
    assert "more lines not kept" in text


def test_private_content_is_removed_and_reported_without_its_text(tmp_path, monkeypatch, capsys):
    run = RUN + [call("e", "Bash", command="cat /Users/someone/.ssh/id_rsa"),
                 result("e", "-----BEGIN OPENSSH PRIVATE KEY-----\nme@example.com")]
    source, output = write_run(tmp_path / "run.jsonl", run), tmp_path / "out.md"
    monkeypatch.setattr(sys, "argv", ["transcript.py", str(source), str(output)])
    assert tool.main() == 0
    text, err = output.read_text(), capsys.readouterr().err
    for kind in ("a home directory path", "a private key", "an e-mail address"):
        assert f"[removed: {kind}]" in text and kind in err
    for secret in ("someone", "me@example.com", "BEGIN OPENSSH"):
        assert secret not in text and secret not in err
    assert "python analysis.py" in text


def test_code_is_not_taken_for_an_e_mail_address():
    for code in ("Xd@np.ones((3, 3))", "w = A@B.T", "y = X@np.linalg.inv(C)"):
        assert tool.redact(code)[1] == []


def test_a_home_directory_can_be_rewritten(tmp_path):
    run = RUN + [call("e", "Bash", command="ls /Users/someone/dev/registry"),
                 result("e", "drwxr-xr-x  5 someone  staff  160 registry")]
    text = tool.render(write_run(tmp_path / "run.jsonl", run), "Demo", home="/Users/someone")
    assert "ls ~/dev/registry" in text and "someone" not in text
    assert tool.redact(text)[1] == []
