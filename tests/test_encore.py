"""Tests for encore_science (`encore check`) and the registry's support for local and remote datasets."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(REPO / "tools"))

import agent_run  # noqa: E402
import datasets  # noqa: E402
import entry  # noqa: E402
from encore_science import report, run  # noqa: E402


def test_a_directory_or_url_gets_a_plain_id():
    assert run.slug("Smith_2024 NWB files/") == "smith-2024-nwb-files"
    assert run.slug("***") == "dataset"


def test_a_directory_is_a_local_dataset_with_a_fingerprint(tmp_path):
    (tmp_path / "sub-1").mkdir()
    (tmp_path / "sub-1" / "a.nwb").write_bytes(b"x" * 10)
    d = run.dataset_of(str(tmp_path))
    assert (d.archive, d.location) == ("local", str(tmp_path.resolve()))
    assert d.folder == f"local-{d.id}" and d.fingerprint.startswith("files-")
    before = d.fingerprint
    (tmp_path / "sub-1" / "a.nwb").write_bytes(b"y" * 10)
    assert run.dataset_of(str(tmp_path)).fingerprint != before


def test_a_url_and_an_archive_dataset_are_told_apart():
    d = run.dataset_of("s3://bucket/smith-2024/")
    assert (d.archive, d.id) == ("remote", "smith-2024")
    assert run.dataset_of("DANDI:000147").folder == "000147"
    assert run.dataset_of("000147", "draft").version == "draft"
    assert run.dataset_of("CRCNS:ret-1").folder == "crcns-ret-1"
    with pytest.raises(run.Stop):
        run.dataset_of("not a dataset at all")


def test_the_doi_is_found_on_the_first_pages():
    assert run.find_doi(["Nature Neurosci 3, 211 (2000). doi:10.1038/72910."]) == "10.1038/72910"
    assert run.find_doi(["https://doi.org/10.1101/2024.01.02.123456v2 posted"]) == "10.1101/2024.01.02.123456v2"
    assert run.find_doi(["no identifier here"]) is None


@pytest.fixture
def local_target(monkeypatch, tmp_path):
    """A registry whose targets/local.json lists one local dataset, as `encore check` writes it."""
    root = tmp_path / "registry"
    (root / "targets").mkdir(parents=True)
    target = {"archive": "local", "id": "smith-2024", "name": "A paper", "path": "/data/smith-2024",
              "fingerprint": "files-0123456789ab", "papers": [{"doi": "10.1038/72910", "title": "A paper", "preprint": False}]}
    (root / "targets" / "local.json").write_text(json.dumps({"targets": [target, dict(target, archive="remote", id="r",
                                                                                         url="s3://b/r", path=None)]}))
    monkeypatch.setattr(datasets, "ROOT", root)
    return root


def test_local_and_remote_datasets_come_from_their_shared_list(local_target):
    found = {t["key"]: t for t in datasets.targets()}
    assert set(found) == {"local:smith-2024", "remote:r"}
    assert found["local:smith-2024"]["folder"] == "local-smith-2024"
    assert "/data/smith-2024" in datasets.access("local:smith-2024")
    assert "s3://b/r" in datasets.access("remote:r")
    assert datasets.folder(datasets.parse("local:smith-2024")) == "local-smith-2024"


def test_a_local_dataset_gets_its_fingerprint_as_its_version(local_target, monkeypatch):
    monkeypatch.setattr(agent_run, "ROOT", REPO)
    monkeypatch.setattr(agent_run, "attempt_of", lambda folder: None)
    prompt = agent_run.fill("author", "local-smith-2024", "claude-opus-5-5")
    assert "/data/smith-2024" in prompt and "files-0123456789ab" in prompt
    assert "pinned published version" not in prompt
    assert "doi:10.1038/72910" in agent_run.fill("claims", "local-smith-2024", "claude-opus-5-5")


def test_only_the_local_dataset_path_may_be_named_in_an_entry(monkeypatch):
    monkeypatch.delenv("ENCORE_LOCAL_DATA", raising=False)
    code = 'io = NWBHDF5IO("/Users/me/smith-2024/sub-1.nwb")'

    def errors(text):
        rep = entry.Report()
        entry._derivation_checks(rep, "nb", text)
        return [e for e in rep.errors if "local path" in str(e)]

    assert errors(code)
    monkeypatch.setenv("ENCORE_LOCAL_DATA", "/Users/me/smith-2024")
    assert not errors(code)
    assert errors('open("/Users/me/other/file.csv")')
    assert errors('open("/Users/me/smith-2024-copy/x.nwb")')


def test_the_report_counts_outcomes_and_lists_findings(tmp_path):
    reg = tmp_path / "registry"
    (reg / "attempts").mkdir(parents=True)
    (reg / "claims" / "local-x").mkdir(parents=True)
    (reg / "claims" / "local-x" / "c.yaml").write_text("claims:\n- id: rate\n  statement: Rates rose.\n")
    (reg / "attempts" / "local-x-smith-2024-01.yaml").write_text(
        "id: local-x-smith-2024-01\nentry: local-x-smith-2024\noutcomes:\n"
        "- claim: rate\n  outcome: blocked\n  blocked_by: data_missing\n  notes: No trials table.\n"
        "findings:\n- kind: data_missing\n  statement: The trials table is missing.\n")
    state = {"folder": "local-x", "title": "Smith 2024", "doi": "10.1/x", "mode": "quick", "model": "m",
             "protocol": "p", "finished": "2026-10-22T12:00", "dataset": {"location": "/d", "fingerprint": "files-1"},
             "roles": {"claims": {"status": "success"}}}
    text = report.write_report(tmp_path, reg, state).read_text()
    assert "## Claims: 1 blocked" in text and "blocked (data missing)" in text
    assert "The trials table is missing." in text and "quick run" in text


def test_a_run_keeps_only_the_example_attempt(tmp_path):
    reg = tmp_path / "out" / "registry"
    for path in ("claims/001453/a.yaml", "claims/001754/b.yaml", "entries/001453-fouke-2025/x.ipynb",
                 "entries/001754-knierim-2000/y.ipynb", "attempts/001453-fouke-2025-01.yaml",
                 "attempts/001754-knierim-2000-01.yaml", "transcripts/001754/author.md", "questions/001754.yaml"):
        (reg / path).parent.mkdir(parents=True, exist_ok=True)
        (reg / path).write_text("x")
    run.git("init", "-q", str(reg))
    run.git("-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "--allow-empty", "-m", "init", cwd=reg)
    run.git("config", "user.name", "t", cwd=reg)
    run.git("config", "user.email", "t@t", cwd=reg)
    r = run.Run(tmp_path / "out", run.Dataset("local", "x", "/d", "files-1"), None, None, None, False, "m", "main")
    r.prune()
    left = sorted(p.relative_to(reg).as_posix() for p in reg.rglob("*") if p.is_file() and ".git" not in p.parts)
    assert left == ["attempts/001453-fouke-2025-01.yaml", "claims/001453/a.yaml", "entries/001453-fouke-2025/x.ipynb"]
