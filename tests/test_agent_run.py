"""Tests for tools/agent_run.py: the prompts and materials of an agent run."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))

import agent_run as tool  # noqa: E402


@pytest.mark.parametrize("role", tool.ROLES)
def test_every_role_has_a_prompt(role):
    assert (REPO / "docs" / "agents" / f"{tool.TEMPLATES[role]}.md").is_file()


def test_the_author_prompt_names_the_target():
    text = tool.fill("author", "000147", "claude-opus-5-5")
    assert "dataset DANDI:000147" in text and "doi:10.7554/elife.74478" in text and "claude-opus-5-5" in text
    assert "{" not in text


def test_a_verifier_prompt_names_the_pinned_version():
    text = tool.fill("verifier-1", "000207", "m")
    assert "version 0.220216.0323" in text and "{" not in text


def test_a_revision_needs_the_verifiers_report():
    with pytest.raises(SystemExit, match="run verifier-1 first"):
        tool.fill("author-revise-1", "000207", "m")


def test_proposals_are_found_from_the_record():
    assert tool.proposals("001097") == ["fig2e-glm-behaviour-explains-little"]
    assert tool.proposals("001453") == []


def test_an_author_on_a_dandiset_with_an_attempt_gets_the_repeat_prompt():
    latest = tool.attempt_of("001754")[0]["id"]
    n = int(latest.rsplit("-", 1)[1])
    text = tool.fill("author", "001754", "m", version="draft")
    assert latest in text and f"attempts/001754-knierim-2000-{n + 1:02d}.yaml" in text
    assert "Use version draft" in text and "{" not in text


def test_a_first_author_without_a_version_picks_a_published_one(monkeypatch):
    monkeypatch.setattr(tool, "attempt_of", lambda dandiset: None)
    text = tool.fill("author", "001933", "m")
    assert "pinned published version" in text and "Use version" not in text


def test_a_repeat_attempt_on_the_same_version_says_the_protocol_changed(monkeypatch):
    record, entry_dir = tool.attempt_of("001933")
    monkeypatch.setattr(tool, "protocol_version", lambda: "pilot-99")
    text = tool.fill("author", "001933", "m", version=record["dataset"]["version"])
    assert "applies pilot-99" in text and "has changed, and this attempt tests" not in text
    text = tool.fill("author", "001933", "m", version="draft")
    assert "the dataset has changed" in text


def test_a_repeat_attempt_keeps_the_earlier_transcripts(tmp_path):
    import subprocess
    (tmp_path / "attempts").mkdir()
    (tmp_path / "attempts" / "000001-demo-01.yaml").write_text("id: 000001-demo-01\n")
    (tmp_path / "transcripts" / "000001").mkdir(parents=True)
    (tmp_path / "transcripts" / "000001" / "author.md").write_text("# author\n")
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run([REPO / "tools" / "archive_transcripts.sh", "000001"], cwd=tmp_path, check=True)
    assert (tmp_path / "transcripts" / "000001" / "attempt-01" / "author.md").is_file()
    assert not (tmp_path / "transcripts" / "000001" / "author.md").exists()


def test_a_repeated_claims_run_before_any_attempt_archives_nothing(tmp_path):
    import subprocess
    (tmp_path / "attempts").mkdir()
    (tmp_path / "transcripts" / "000001").mkdir(parents=True)
    (tmp_path / "transcripts" / "000001" / "claims.md").write_text("# claims\n")
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run([REPO / "tools" / "archive_transcripts.sh", "000001"], cwd=tmp_path, check=True)
    assert (tmp_path / "transcripts" / "000001" / "claims.md").is_file()


def test_the_recorder_prompt_names_the_attempt():
    latest = tool.attempt_of("001933")[0]["id"]
    text = tool.fill("recorder", "001933", "m")
    assert latest in text and "readme_row.py 001933" in text and "--write" not in text and "{" not in text


def test_the_conversion_issue_lists_every_finding():
    import conversion_issue
    record = tool.attempt_of("000559")[0]
    text = conversion_issue.issue("000559")
    assert text.splitlines()[0] == "Problems found in DANDI:000559 by a reproduction attempt"
    assert text.count("\n- [ ] ") == len(record["findings"]) + 7
    assert record["id"] in text


def test_the_target_paper_follows_the_hand_corrections():
    # papers/triage.yaml names the paper behind 001871's data and says the one its metadata names is not.
    assert tool.target("001871")["paper"] == "10.1073/pnas.2608896123"
    # A review that triage says is not the paper is never chosen.
    assert tool.target("000336")["paper"] != "10.1016/j.tins.2012.11.006"
    # DOIs are cleaned, as the paper store names them.
    assert tool.target("000026")["paper"] == "10.1117/1.jbo.24.10.106504"


def test_an_authors_prompt_ends_with_its_time(monkeypatch):
    monkeypatch.setenv("AGENT_TIME_BUDGET_MIN", "60")
    monkeypatch.setenv("AGENT_TIME_LIMIT_MIN", "90")
    text = tool.fill("author", "001754", "claude-opus-5-5", "draft")
    assert "Time: this run started at" in text and "1 h 30 min after it started" in text
    assert "Time: this run started" not in tool.fill("verifier-1", "001754", "claude-opus-5-5")
