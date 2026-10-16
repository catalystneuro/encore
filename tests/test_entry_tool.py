"""Tests for tools/entry.py: the checks a deposit has to pass."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

import nbformat
import pytest
import yaml

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))

import entry as tool  # noqa: E402

VERSION = "0.240101.0000"
ENTRY = {
    "schema_version": 1, "name": "demo", "type": "reproduction", "title": "Demo",
    "description": "A demo entry.", "license": "Apache-2.0",
    "notebooks": [{"path": "analysis.ipynb"}],
    "related": [{"id": "dandi:000001/0.240101.0000", "relation": "uses_data"},
                {"id": "doi:10.1000/demo", "relation": "reproduces"}],
}
CLAIMS = {"schema_version": 1, "dandiset": "000001", "paper": "doi:10.1000/demo",
          "claims": [{"id": "fig1", "statement": "Something rises.", "source": "Figure 1"}]}
ATTEMPT = {
    "schema_version": 1, "id": "demo-01", "dandiset": "000001", "dandiset_version": "0.240101.0000",
    "paper": "doi:10.1000/demo", "date": "2026-10-13", "entry": "demo",
    "provenance": {"kind": "agent", "accountable": {"name": "Someone"},
                   "agent": {"harness": "h", "model": "m", "protocol": "p"}},
    "outcomes": [{"claim": "fig1", "outcome": "reproduced", "notebook": "analysis.ipynb",
                  "output": "claim:fig1"}],
}


def notebook(code: str, tags=("claim:fig1", "sanity"), outputs=False):
    nb = nbformat.v4.new_notebook()
    cell = nbformat.v4.new_code_cell(code)
    cell.metadata["tags"] = list(tags)
    if outputs:
        cell.outputs = [nbformat.v4.new_output("stream", name="stdout", text="1\n")]
        cell.execution_count = 1
    nb.cells.append(cell)
    return nb


@pytest.fixture
def repo(tmp_path, monkeypatch):
    """A minimal registry with one valid entry, its claims and one attempt."""
    shutil.copytree(REPO / "schemas", tmp_path / "schemas")
    entry_dir = tmp_path / "entries" / "demo"
    entry_dir.mkdir(parents=True)
    (entry_dir / "entry.yaml").write_text(yaml.safe_dump(ENTRY))
    (entry_dir / "requirements.in").write_text("numpy\n")
    (entry_dir / "requirements.lock.txt").write_text("numpy==2.0.0\n")
    nbformat.write(notebook(f'DANDISET, VERSION = "000001", "{VERSION}"\nprint(1)'), entry_dir / "analysis.ipynb")
    (tmp_path / "claims" / "000001").mkdir(parents=True)
    (tmp_path / "claims" / "000001" / "demo.yaml").write_text(yaml.safe_dump(CLAIMS))
    (tmp_path / "attempts").mkdir()
    (tmp_path / "attempts" / "demo-01.yaml").write_text(yaml.safe_dump(ATTEMPT))
    monkeypatch.setattr(tool, "ROOT", tmp_path)
    return tmp_path


def errors(repo: Path) -> list[str]:
    return tool.check(repo / "entries" / "demo").errors


def test_a_valid_entry_passes(repo):
    assert errors(repo) == []


def test_an_unlisted_notebook_is_an_error(repo):
    nbformat.write(notebook('"000001"'), repo / "entries" / "demo" / "extra.ipynb")
    assert any("extra.ipynb: notebook is not listed" in e for e in errors(repo))


def test_a_notebook_needs_a_data_check_cell(repo):
    nbformat.write(notebook('"000001"', tags=("claim:fig1",)), repo / "entries" / "demo" / "analysis.ipynb")
    assert any("tagged `sanity`" in e for e in errors(repo))


def test_committed_outputs_are_an_error(repo):
    nbformat.write(notebook('"000001"', outputs=True), repo / "entries" / "demo" / "analysis.ipynb")
    assert any("without outputs" in e for e in errors(repo))


def test_a_notebook_must_name_its_dandiset(repo):
    nbformat.write(notebook("print(1)"), repo / "entries" / "demo" / "analysis.ipynb")
    assert any("names dandiset 000001" in e for e in errors(repo))


def test_a_helper_may_name_the_dandiset(repo):
    entry_dir = repo / "entries" / "demo"
    nbformat.write(notebook("import helper"), entry_dir / "analysis.ipynb")
    (entry_dir / "helper.py").write_text(f'DANDISET, VERSION = "000001", "{VERSION}"\n')
    (entry_dir / "entry.yaml").write_text(yaml.safe_dump({**ENTRY, "helpers": ["helper.py"]}))
    assert errors(repo) == []


@pytest.mark.parametrize("code, message", [
    ('"000001"\nx = [' + ", ".join(["0.5"] * 300) + "]", "literal of more than"),
    ('"000001"\nimg = plt.imread("figure2.png")', "reads an image file"),
    ('"000001"\nsrc = "data:image/png;base64,AAAA"', "encoded image"),
    ('"000001"\nf = h5py.File("/Users/me/sub-01.nwb")', "local path"),
    ('"000001"\nf = h5py.File("~/data/sub-01.nwb")', "local path"),
])
def test_results_must_be_computed_from_the_data(repo, code, message):
    nbformat.write(notebook(code), repo / "entries" / "demo" / "analysis.ipynb")
    assert any(message in e for e in errors(repo))


def test_an_unlocked_requirement_is_an_error(repo):
    (repo / "entries" / "demo" / "requirements.in").write_text("numpy\nscipy\n")
    assert any("scipy is required but not locked" in e for e in errors(repo))


def test_an_attempt_must_point_at_a_known_claim_and_a_tagged_cell(repo):
    attempt = {**ATTEMPT, "outcomes": [
        {"claim": "fig9", "outcome": "reproduced", "notebook": "analysis.ipynb", "output": "claim:fig9"}]}
    (repo / "attempts" / "demo-01.yaml").write_text(yaml.safe_dump(attempt))
    found = errors(repo)
    assert any("claim 'fig9' is not in the claims file" in e for e in found)
    assert any("no cell tagged 'claim:fig9'" in e for e in found)


def test_a_blocked_outcome_needs_a_reason(repo):
    attempt = {**ATTEMPT, "outcomes": [{"claim": "fig1", "outcome": "blocked"}]}
    (repo / "attempts" / "demo-01.yaml").write_text(yaml.safe_dump(attempt))
    assert any("blocked_by" in e for e in errors(repo))


def test_the_entry_name_must_match_its_directory(repo):
    (repo / "entries" / "demo" / "entry.yaml").write_text(yaml.safe_dump({**ENTRY, "name": "other"}))
    assert any("must match the directory name" in e for e in errors(repo))


def test_every_claim_needs_one_outcome(repo):
    claims = {**CLAIMS, "claims": CLAIMS["claims"] + [{"id": "fig2", "statement": "S.", "source": "Figure 2"}]}
    (repo / "claims" / "000001" / "demo.yaml").write_text(yaml.safe_dump(claims))
    attempt = {**ATTEMPT, "outcomes": ATTEMPT["outcomes"] * 2}
    (repo / "attempts" / "demo-01.yaml").write_text(yaml.safe_dump(attempt))
    found = errors(repo)
    assert any("claim 'fig2' has no outcome" in e for e in found)
    assert any("claim 'fig1' has more than one outcome" in e for e in found)


def test_the_dandiset_version_must_be_pinned(repo):
    entry = {**ENTRY, "related": [{"id": "dandi:000001", "relation": "uses_data"}, ENTRY["related"][1]]}
    (repo / "entries" / "demo" / "entry.yaml").write_text(yaml.safe_dump(entry))
    assert any("pin the version of dandiset 000001" in e for e in errors(repo))


def test_the_dandiset_version_must_agree_across_files(repo):
    (repo / "attempts" / "demo-01.yaml").write_text(yaml.safe_dump({**ATTEMPT, "dandiset_version": "draft"}))
    nbformat.write(notebook('"000001"'), repo / "entries" / "demo" / "analysis.ipynb")
    found = errors(repo)
    assert any("dandiset_version 'draft' differs" in e for e in found)
    assert any(f"names version {VERSION}" in e for e in found)


def test_handover_removes_the_conclusions(repo):
    entry_dir = repo / "entries" / "demo"
    executed = repo / "executed" / "demo"
    executed.mkdir(parents=True)
    nb = notebook(f'"000001", "{VERSION}"')
    nb.cells += [nbformat.v4.new_markdown_cell("**Result: reproduced.** It rises."),
                 nbformat.v4.new_markdown_cell("Data check note."),
                 nbformat.v4.new_markdown_cell("## Summary"),
                 nbformat.v4.new_code_cell("summary_table()")]
    nbformat.write(nb, executed / "analysis.ipynb")
    assert tool.handover(entry_dir, executed) == 0
    out = executed / "handover"
    sources = [c.source for c in nbformat.read(out / "analysis.ipynb", as_version=4).cells]
    assert sources == [nb.cells[0].source, "Data check note."]
    assert (out / "demo.yaml").is_file()


def test_invalid_yaml_in_an_attempt_is_reported(repo):
    (repo / "attempts" / "broken.yaml").write_text("notes: Confirmed: no\n  x: [\n")
    assert any("broken.yaml: not valid YAML" in e for e in errors(repo))


def test_notebooks_run_on_a_kernel_of_the_entrys_own_environment(repo, monkeypatch, tmp_path):
    commands = []

    def fake_run(cmd, **kwargs):
        commands.append((cmd, kwargs))
        return type("Done", (), {"returncode": 0, "stderr": ""})()

    monkeypatch.setattr(tool.subprocess, "run", fake_run)
    out = tmp_path / "executed"
    assert tool.run(repo / "entries" / "demo", out, timeout=60, max_minutes=30) == 0
    venv = str((out / ".venv").resolve())
    install = next(c for c, _ in commands if c[1:3] == ["-m", "ipykernel"])
    assert install[install.index("--prefix") + 1] == venv
    name = install[install.index("--name") + 1]
    assert name != "python3"
    execute, options = next((c, k) for c, k in commands if c[1:4] == ["-m", "jupyter", "nbconvert"])
    assert f"--ExecutePreprocessor.kernel_name={name}" in execute
    assert options["env"]["JUPYTER_PATH"].startswith(venv)


def test_a_claim_may_have_several_expected_values_and_depend_on_another(repo):
    claims = {**CLAIMS, "claims": [
        {"id": "fig1", "statement": "S.", "source": "Figure 1",
         "expected": [{"quantity": "a", "value": 0.5, "tolerance": 0.05}, {"quantity": "b", "value": 2.0}]},
        {"id": "fig2", "statement": "T.", "source": "Figure 2", "depends_on": ["fig1"]}]}
    (repo / "claims" / "000001" / "demo.yaml").write_text(yaml.safe_dump(claims))
    attempt = {**ATTEMPT, "outcomes": ATTEMPT["outcomes"] + [{"claim": "fig2", "outcome": "blocked",
                                                              "blocked_by": "other", "notes": "n"}],
               "inputs": [{"what": "model RDMs", "source": "https://github.com/x/y at abc123"}],
               "findings": [{"kind": "format_error", "statement": "Spike times are not sorted."}]}
    (repo / "attempts" / "demo-01.yaml").write_text(yaml.safe_dump(attempt))
    assert errors(repo) == []


def test_a_claim_cannot_depend_on_one_that_is_not_there(repo):
    claims = {**CLAIMS, "claims": CLAIMS["claims"] + [
        {"id": "fig2", "statement": "T.", "source": "Figure 2", "depends_on": ["fig9"]}]}
    (repo / "claims" / "000001" / "demo.yaml").write_text(yaml.safe_dump(claims))
    assert any("depends on 'fig9'" in e for e in errors(repo))


def test_an_outcome_may_change_after_round_1(repo):
    round1 = {"date": "2026-10-13", "kind": "agent", "by": "v",
              "results": [{"claim": "fig1", "agrees": True, "outcome": "blocked"}]}
    (repo / "attempts" / "demo-01.yaml").write_text(yaml.safe_dump({**ATTEMPT, "verifications": [round1]}))
    assert errors(repo) == []


def test_an_outcome_cannot_change_after_the_last_verification(repo):
    verified = {"date": "2026-10-13", "kind": "agent", "by": "v",
                "results": [{"claim": "fig1", "agrees": True, "outcome": "not_reproduced"}]}
    attempt = {**ATTEMPT, "verifications": [verified, verified]}
    (repo / "attempts" / "demo-01.yaml").write_text(yaml.safe_dump(attempt))
    assert any("last verification agreed with 'not_reproduced'" in e for e in errors(repo))
    attempt["outcomes"] = [{**ATTEMPT["outcomes"][0], "outcome": "not_reproduced"}]
    (repo / "attempts" / "demo-01.yaml").write_text(yaml.safe_dump(attempt))
    assert errors(repo) == []


def test_measured_may_hold_one_value_per_expected_value(repo):
    attempt = {**ATTEMPT, "outcomes": [{**ATTEMPT["outcomes"][0], "measured": [0.65, 0.23]},
                                       ]}
    (repo / "attempts" / "demo-01.yaml").write_text(yaml.safe_dump(attempt))
    assert errors(repo) == []


def test_a_claim_may_say_it_uses_outside_data(repo):
    claims = {**CLAIMS, "claims": [{**CLAIMS["claims"][0], "data": "with_inputs"}]}
    (repo / "claims" / "000001" / "demo.yaml").write_text(yaml.safe_dump(claims))
    assert errors(repo) == []
    claims["claims"][0]["data"] = "somewhere"
    (repo / "claims" / "000001" / "demo.yaml").write_text(yaml.safe_dump(claims))
    assert any("data" in e for e in errors(repo))


def test_a_claim_on_data_in_another_archive_names_it_and_is_tested_there(repo):
    claims = {**CLAIMS, "claims": [{**CLAIMS["claims"][0], "data": "elsewhere"}]}
    (repo / "claims" / "000001" / "demo.yaml").write_text(yaml.safe_dump(claims))
    assert any("where" in e for e in errors(repo))
    claims["claims"][0]["where"] = "PRIDE PXD000001"
    (repo / "claims" / "000001" / "demo.yaml").write_text(yaml.safe_dump(claims))
    assert any("list them under `inputs`" in e for e in errors(repo))
    attempt = {**ATTEMPT, "inputs": [{"what": "proteomics", "source": "PRIDE PXD000001"}]}
    (repo / "attempts" / "demo-01.yaml").write_text(yaml.safe_dump(attempt))
    assert errors(repo) == []
    attempt = {**ATTEMPT, "outcomes": [{**ATTEMPT["outcomes"][0], "outcome": "blocked",
                                        "blocked_by": "data_missing"}]}
    (repo / "attempts" / "demo-01.yaml").write_text(yaml.safe_dump(attempt))
    assert any("not `data_missing`" in e for e in errors(repo))



def test_an_earlier_attempt_is_not_held_to_a_later_elsewhere(repo):
    claims = {**CLAIMS, "claims": [{**CLAIMS["claims"][0], "data": "elsewhere", "where": "PRIDE PXD000001"}]}
    (repo / "claims" / "000001" / "demo.yaml").write_text(yaml.safe_dump(claims))
    earlier = {**ATTEMPT, "outcomes": [{**ATTEMPT["outcomes"][0], "outcome": "blocked",
                                        "blocked_by": "data_missing", "notes": "Not in the dandiset."}]}
    (repo / "attempts" / "demo-01.yaml").write_text(yaml.safe_dump(earlier))
    later = {**ATTEMPT, "id": "demo-02", "outcomes": [{**ATTEMPT["outcomes"][0], "outcome": "blocked",
                                                       "blocked_by": "too_large", "notes": "Too large."}]}
    (repo / "attempts" / "demo-02.yaml").write_text(yaml.safe_dump(later))
    assert errors(repo) == []


def test_a_later_round_decides_the_claims_it_reviews(repo):
    round2 = {"date": "2026-10-13", "kind": "agent", "by": "v",
              "results": [{"claim": "fig1", "agrees": True, "outcome": "not_reproduced"}]}
    round3 = {"date": "2026-10-14", "kind": "agent", "by": "v",
              "results": [{"claim": "fig1", "agrees": True, "outcome": "reproduced"}]}
    attempt = {**ATTEMPT, "verifications": [round2, round2]}
    (repo / "attempts" / "demo-01.yaml").write_text(yaml.safe_dump(attempt))
    assert any("last verification agreed with 'not_reproduced'" in e for e in errors(repo))
    attempt["outcomes"] = [{**ATTEMPT["outcomes"][0], "outcome": "not_reproduced",
                            "proposed": {"outcome": "reproduced", "reason": "A later analysis."}}]
    (repo / "attempts" / "demo-01.yaml").write_text(yaml.safe_dump(attempt))
    assert errors(repo) == []
    attempt = {**ATTEMPT, "verifications": [round2, round2, round3]}
    (repo / "attempts" / "demo-01.yaml").write_text(yaml.safe_dump(attempt))
    assert errors(repo) == []


def test_names_from_outside_need_a_source_and_a_finding(repo):
    claims = {**CLAIMS, "claims": [{**CLAIMS["claims"][0], "data": "with_labels"}]}
    (repo / "claims" / "000001" / "demo.yaml").write_text(yaml.safe_dump(claims))
    assert any("with_labels" in e for e in errors(repo))
    attempt = {**ATTEMPT, "inputs": [{"what": "stimulus names", "source": "https://example.org at abc"}],
               "findings": [{"kind": "metadata_insufficient", "statement": "Codes have no names."}]}
    (repo / "attempts" / "demo-01.yaml").write_text(yaml.safe_dump(attempt))
    assert errors(repo) == []


def test_only_the_latest_attempt_must_match_the_entrys_version(repo):
    earlier = {**ATTEMPT, "dandiset_version": "0.230101.0000"}
    (repo / "attempts" / "demo-01.yaml").write_text(yaml.safe_dump(earlier))
    (repo / "attempts" / "demo-02.yaml").write_text(yaml.safe_dump({**ATTEMPT, "id": "demo-02"}))
    assert errors(repo) == []
    (repo / "attempts" / "demo-02.yaml").write_text(yaml.safe_dump({**ATTEMPT, "id": "demo-02",
                                                                   "dandiset_version": "0.230101.0000"}))
    assert any("differs from" in e for e in errors(repo))
