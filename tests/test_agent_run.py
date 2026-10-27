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


def test_an_author_on_a_dandiset_with_an_attempt_gets_the_blind_repeat_prompt():
    latest = tool.attempt_of("001754")[0]["id"]
    n = int(latest.rsplit("-", 1)[1])
    text = tool.fill("author", "001754", "m", version="draft")
    assert f"attempts/001754-knierim-2000-{n + 1:02d}.yaml" in text and "entries/001754-knierim-2000" in text
    assert "Use version draft" in text and "{" not in text
    # Blind: no earlier attempt is named, and the author is told not to look for one.
    for p in tool.records_of("001754"):
        assert p.stem not in text
    assert "blind" in text and "encorescience.org" in text


def test_the_reconcile_prompt_names_both_attempts():
    *_, earlier, latest = tool.records_of("001754")
    text = tool.fill("reconcile", "001754", "m")
    assert latest.stem in text and earlier.stem in text and "tools/blind.sh audit 001754" in text
    assert "{" not in text and "Time:" in text
    assert tool.repeat("001754") and not tool.repeat("001453")
    with pytest.raises(SystemExit, match="no earlier attempt"):
        tool.fill("reconcile", "001453", "m")


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
    assert "The dataset has changed" in text


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


def test_a_blind_author_sees_no_earlier_attempt_and_it_all_comes_back(tmp_path):
    import subprocess
    blind = REPO / "tools" / "blind.sh"
    for path, text in {"attempts/000001-demo-01.yaml": "id: 000001-demo-01\nentry: 000001-demo\n",
                       "attempts/000002-other-01.yaml": "id: 000002-other-01\n",
                       "entries/000001-demo/nb.ipynb": "{}", "questions/000001.yaml": "questions: []\n",
                       "claims/000001/paper.yaml": "claims: []\n",
                       "transcripts/000001/author.md": "# author\n", "transcripts/000001/claims.md": "# claims\n",
                       "transcripts/000001/attempt-00/author.md": "# author\n",
                       "docs/pilot-notes/000001-demo-01.md": "notes\n", "docs/pilot-notes.md": "all notes\n",
                       ".git/HEAD": "ref\n"}.items():
        (tmp_path / path).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / path).write_text(text)
    stash = tmp_path.parent / f"{tmp_path.name}-hidden"
    run = lambda *a: subprocess.run(["bash", str(blind), *a], cwd=tmp_path, check=True, capture_output=True, text=True)
    run("hide", "000001", "author", str(stash))
    for gone in ("attempts/000001-demo-01.yaml", "entries/000001-demo", "questions/000001.yaml", ".git",
                 "transcripts/000001/author.md", "transcripts/000001/attempt-00", "docs/pilot-notes/000001-demo-01.md"):
        assert not (tmp_path / gone).exists(), gone
    for kept in ("attempts/000002-other-01.yaml", "claims/000001/paper.yaml", "transcripts/000001/claims.md"):
        assert (tmp_path / kept).exists(), kept
    assert "Left out" in (tmp_path / "docs/pilot-notes.md").read_text()
    # The author writes a new entry and record; the earlier ones come back, the old entry and questions do not.
    (tmp_path / "entries/000001-demo").mkdir()
    (tmp_path / "entries/000001-demo/new.ipynb").write_text("{}")
    (tmp_path / "attempts/000001-demo-02.yaml").write_text("id: 000001-demo-02\n")
    run("restore", "000001", "author", str(stash))
    for back in ("attempts/000001-demo-01.yaml", ".git/HEAD", "transcripts/000001/author.md",
                 "transcripts/000001/attempt-00/author.md", "docs/pilot-notes/000001-demo-01.md"):
        assert (tmp_path / back).exists(), back
    assert (tmp_path / "docs/pilot-notes.md").read_text() == "all notes\n"
    assert sorted(p.name for p in (tmp_path / "entries/000001-demo").iterdir()) == ["new.ipynb"]
    assert not (tmp_path / "questions/000001.yaml").exists()
    # A later run of the same attempt hides the earlier record but not its own, and keeps the entry.
    run("hide", "000001", "author-revise-1", str(stash))
    assert not (tmp_path / "attempts/000001-demo-01.yaml").exists()
    assert (tmp_path / "attempts/000001-demo-02.yaml").exists() and (tmp_path / "entries/000001-demo").exists()
    run("restore", "000001", "author-revise-1", str(stash))
    assert (tmp_path / "attempts/000001-demo-01.yaml").exists()


def test_a_first_attempt_has_nothing_to_hide(tmp_path):
    import subprocess
    (tmp_path / "attempts").mkdir()
    out = subprocess.run(["bash", str(REPO / "tools" / "blind.sh"), "hide", "000001", "author", str(tmp_path / "s")],
                         cwd=tmp_path, check=True, capture_output=True, text=True).stdout
    assert "nothing to hide" in out and not (tmp_path / "s").exists()
