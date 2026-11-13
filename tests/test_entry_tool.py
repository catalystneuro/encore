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
CLAIMS = {"schema_version": 2, "paper": "doi:10.1000/demo",
          "claims": [{"id": "fig1", "statement": "Something rises.", "source": "Figure 1"}]}
ATTEMPT = {
    "schema_version": 3, "id": "demo-01",
    "datasets": [{"archive": "dandi", "id": "000001", "version": "0.240101.0000", "relation": "primary"}],
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
    (tmp_path / "claims").mkdir(parents=True)
    (tmp_path / "claims" / "demo.yaml").write_text(yaml.safe_dump(CLAIMS))
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
    assert any("names dataset 000001" in e for e in errors(repo))


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



def test_an_outcome_on_an_assumption_states_it_and_is_not_blocked(repo):
    """An outcome that rests on an assumption about an open method says what was assumed in a deviation
    (docs/protocol.md, Author, step 1.6); a claim with no defensible choice is blocked instead."""
    def with_outcome(**o):
        attempt = {**ATTEMPT, "outcomes": [{**ATTEMPT["outcomes"][0], **o}]}
        (repo / "attempts" / "demo-01.yaml").write_text(yaml.safe_dump(attempt))
        return errors(repo)
    assumed = "Assumed a 1 s window, the one Figure 3 uses, since the Methods give none."
    assert with_outcome(assumed=True, deviations=[assumed]) == []
    assert with_outcome(assumed=True) != []
    assert with_outcome(assumed=True, deviations=[]) != []
    assert with_outcome(assumed=True, deviations=[assumed], outcome="blocked", blocked_by="methods_underspecified",
                        notes="N.") != []
    assert with_outcome(assumed="yes", deviations=[assumed]) != []

def test_the_entry_name_must_match_its_directory(repo):
    (repo / "entries" / "demo" / "entry.yaml").write_text(yaml.safe_dump({**ENTRY, "name": "other"}))
    assert any("must match the directory name" in e for e in errors(repo))


def test_every_claim_needs_one_outcome(repo):
    claims = {**CLAIMS, "claims": CLAIMS["claims"] + [{"id": "fig2", "statement": "S.", "source": "Figure 2"}]}
    (repo / "claims" / "demo.yaml").write_text(yaml.safe_dump(claims))
    attempt = {**ATTEMPT, "outcomes": ATTEMPT["outcomes"] * 2}
    (repo / "attempts" / "demo-01.yaml").write_text(yaml.safe_dump(attempt))
    found = errors(repo)
    assert any("claim 'fig2' has no outcome" in e for e in found)
    assert any("claim 'fig1' has more than one outcome" in e for e in found)


def test_claims_read_again_after_an_attempt_are_the_next_attempts_to_test(repo):
    """A dataset added to a paper has its claims read again, and they reach main ahead of the repeat attempt."""
    check = {"date": "2099-01-01", "kind": "agent", "ready": True}
    claims = {**CLAIMS, "claims": CLAIMS["claims"] + [{"id": "fig2", "statement": "S.", "source": "Figure 2"}],
              "checks": (CLAIMS.get("checks") or []) + [check]}
    (repo / "claims" / "demo.yaml").write_text(yaml.safe_dump(claims))
    assert not any("claim 'fig2' has no outcome" in e for e in errors(repo))


def test_the_dandiset_version_must_be_pinned(repo):
    entry = {**ENTRY, "related": [{"id": "dandi:000001", "relation": "uses_data"}, ENTRY["related"][1]]}
    (repo / "entries" / "demo" / "entry.yaml").write_text(yaml.safe_dump(entry))
    assert any("pin the version of dataset 000001" in e for e in errors(repo))


def test_the_dandiset_version_must_agree_across_files(repo):
    (repo / "attempts" / "demo-01.yaml").write_text(yaml.safe_dump({**ATTEMPT, "datasets": [{**ATTEMPT["datasets"][0], "version": "draft"}]}))
    nbformat.write(notebook('"000001"'), repo / "entries" / "demo" / "analysis.ipynb")
    found = errors(repo)
    assert any("dataset 000001 version 'draft' differs" in e for e in found)
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
    (repo / "claims" / "demo.yaml").write_text(yaml.safe_dump(claims))
    attempt = {**ATTEMPT, "outcomes": ATTEMPT["outcomes"] + [{"claim": "fig2", "outcome": "blocked",
                                                              "blocked_by": "other", "notes": "n"}],
               "inputs": [{"what": "model RDMs", "source": "https://github.com/x/y at abc123"}],
               "findings": [{"kind": "format_error", "statement": "Spike times are not sorted."}]}
    (repo / "attempts" / "demo-01.yaml").write_text(yaml.safe_dump(attempt))
    assert errors(repo) == []


def test_a_claim_cannot_depend_on_one_that_is_not_there(repo):
    claims = {**CLAIMS, "claims": CLAIMS["claims"] + [
        {"id": "fig2", "statement": "T.", "source": "Figure 2", "depends_on": ["fig9"]}]}
    (repo / "claims" / "demo.yaml").write_text(yaml.safe_dump(claims))
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
    (repo / "claims" / "demo.yaml").write_text(yaml.safe_dump(claims))
    assert errors(repo) == []
    claims["claims"][0]["data"] = "somewhere"
    (repo / "claims" / "demo.yaml").write_text(yaml.safe_dump(claims))
    assert any("data" in e for e in errors(repo))


def test_a_claim_on_data_in_another_archive_names_it_and_is_tested_there(repo):
    claims = {**CLAIMS, "claims": [{**CLAIMS["claims"][0], "data": "elsewhere"}]}
    (repo / "claims" / "demo.yaml").write_text(yaml.safe_dump(claims))
    assert any("where" in e for e in errors(repo))
    claims["claims"][0]["where"] = "PRIDE PXD000001"
    (repo / "claims" / "demo.yaml").write_text(yaml.safe_dump(claims))
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
    (repo / "claims" / "demo.yaml").write_text(yaml.safe_dump(claims))
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
    (repo / "claims" / "demo.yaml").write_text(yaml.safe_dump(claims))
    assert any("with_labels" in e for e in errors(repo))
    attempt = {**ATTEMPT, "inputs": [{"what": "stimulus names", "source": "https://example.org at abc"}],
               "findings": [{"kind": "metadata_insufficient", "statement": "Codes have no names."}]}
    (repo / "attempts" / "demo-01.yaml").write_text(yaml.safe_dump(attempt))
    assert errors(repo) == []


def test_only_the_latest_attempt_must_match_the_entrys_version(repo):
    earlier = {**ATTEMPT, "datasets": [{**ATTEMPT["datasets"][0], "version": "0.230101.0000"}]}
    (repo / "attempts" / "demo-01.yaml").write_text(yaml.safe_dump(earlier))
    (repo / "attempts" / "demo-02.yaml").write_text(yaml.safe_dump({**ATTEMPT, "id": "demo-02"}))
    assert errors(repo) == []
    (repo / "attempts" / "demo-02.yaml").write_text(yaml.safe_dump({**earlier, "id": "demo-02"}))
    assert any("differs from" in e for e in errors(repo))


def test_an_entry_runs_on_its_own_python_version(repo):
    entry_dir = repo / "entries" / "demo"
    # Before the field, the version the lock was compiled for; with none, the registry's default.
    assert tool.python_of(entry_dir) == tool.PYTHON_VERSION
    (entry_dir / "requirements.lock.txt").write_text(
        "#    uv pip compile --python-version 3.12 requirements.in -o requirements.lock.txt\nnumpy==2.0.0\n")
    assert tool.python_of(entry_dir) == "3.12"
    tool.set_python(entry_dir, "3.14")
    assert tool.python_of(entry_dir) == "3.14" and 'python: "3.14"' in (entry_dir / "entry.yaml").read_text()
    # A lock compiled for another version than entry.yaml names is an error.
    assert any("locked for Python 3.12" in e for e in errors(repo))


def test_claim_outputs_are_compared_cell_by_cell(tmp_path):
    nb = notebook("print(1)", outputs=True)
    nbformat.write(nb, tmp_path / "a.ipynb")
    assert tool.tagged_outputs(tmp_path / "a.ipynb") == {"claim:fig1": "1\n"}


def test_the_colab_copy_sets_itself_up_only_on_colab():
    import colab
    code = colab.SETUP.format(branch="colab", repo="catalystneuro/encore", name="demo")
    compile(code, "setup", "exec")
    assert 'if "google.colab" in sys.modules:' in code and "entries/demo" in code
    exec(code, {})   # outside Colab: nothing happens


def _executed(repo, monkeypatch):
    """The demo entry with executed copies and the stamp a passing run leaves, without executing anything: the
    environment and the notebook run are replaced by a copy of the notebook."""
    entry_dir, out = repo / "entries" / "demo", repo / "executed" / "demo"
    calls = []

    def fake(cmd, **kwargs):
        calls.append(cmd)
        if cmd[1:4] == ["-m", "jupyter", "nbconvert"]:
            shutil.copy(entry_dir / cmd[-1], out / cmd[-1])
        return type("R", (), {"returncode": 0, "stderr": ""})()
    monkeypatch.setattr(tool.subprocess, "run", fake)
    assert tool.run(entry_dir, out, 60, 60) == 0
    return entry_dir, out, calls


def test_a_run_with_nothing_changed_reuses_the_executed_copies(repo, monkeypatch, capsys):
    entry_dir, out, calls = _executed(repo, monkeypatch)
    assert (out / tool.STAMP).is_file() and any(c[1:4] == ["-m", "jupyter", "nbconvert"] for c in calls)
    del calls[:]
    capsys.readouterr()
    assert tool.run(entry_dir, out, 60, 60) == 0
    assert calls == []                                      # nothing was built or executed
    said = capsys.readouterr().out
    assert "analysis.ipynb" in said and "reused" in said and "--fresh" in said
    assert tool.run(entry_dir, out, 60, 60, fresh=True) == 0 and any(c[1:4] == ["-m", "jupyter", "nbconvert"] for c in calls)


def test_any_change_to_what_a_run_reads_makes_it_run_again(repo, monkeypatch):
    entry_dir, out, calls = _executed(repo, monkeypatch)
    before = tool.entry_hash(entry_dir)
    assert tool.reusable(entry_dir, out, 60)
    # A change to a notebook, a helper, the lock or entry.yaml (the Python, the dataset's version) changes the hash.
    for name, text in (("helper.py", "X = 1\n"), ("requirements.lock.txt", "numpy==2.1.0\n")):
        old = (entry_dir / name).read_text() if (entry_dir / name).exists() else None
        (entry_dir / name).write_text(text)
        assert tool.entry_hash(entry_dir) != before and tool.reusable(entry_dir, out, 60) is None
        (entry_dir / name).unlink() if old is None else (entry_dir / name).write_text(old)
    assert tool.entry_hash(entry_dir) == before and tool.reusable(entry_dir, out, 60)
    # Files a run does not read leave it as it was.
    (entry_dir / "__pycache__").mkdir(); (entry_dir / "__pycache__" / "helper.cpython-313.pyc").write_bytes(b"x")
    assert tool.entry_hash(entry_dir) == before


def test_executed_copies_that_are_not_what_the_run_left_are_not_reused(repo, monkeypatch):
    import json
    entry_dir, out, _ = _executed(repo, monkeypatch)
    stamp = json.loads((out / tool.STAMP).read_text())
    # An executed copy edited after the run.
    (out / "analysis.ipynb").write_text((out / "analysis.ipynb").read_text() + "\n")
    assert tool.reusable(entry_dir, out, 60) is None
    shutil.copy(entry_dir / "analysis.ipynb", out / "analysis.ipynb")
    assert tool.reusable(entry_dir, out, 60)
    # A run that took longer than the limit asked for now; one too old; one that failed leaves no stamp.
    (out / tool.STAMP).write_text(json.dumps({**stamp, "results": [{**stamp["results"][0], "seconds": 4000}]}))
    assert tool.reusable(entry_dir, out, 60) is None and tool.reusable(entry_dir, out, 80)
    (out / tool.STAMP).write_text(json.dumps({**stamp, "finished": stamp["finished"] - 40 * 86400}))
    assert tool.reusable(entry_dir, out, 60) is None
    (out / tool.STAMP).write_text("not json")
    assert tool.reusable(entry_dir, out, 60) is None



def test_a_finding_that_can_be_about_either_says_which_from_pilot_15(repo):
    def check(protocol, findings, datasets=None):
        attempt = {**ATTEMPT, "findings": findings,
                   "provenance": {**ATTEMPT["provenance"], "agent": {**ATTEMPT["provenance"]["agent"], "protocol": protocol}}}
        if datasets:
            attempt["datasets"] = datasets
        (repo / "attempts" / "demo-01.yaml").write_text(yaml.safe_dump(attempt))
        return [e for e in errors(repo) if "finding 1" in e]
    other = [{"kind": "other", "statement": "Something about it."}]
    # The rule is the protocol's from pilot-15: an attempt made under an earlier version is not held to it.
    assert check("pilot-14", other) == [] and check("pilot-7", other) == []
    assert any("say what it is about" in e for e in check("pilot-15", other))
    assert any("say what it is about" in e for e in check("pilot-16", other))
    assert check("pilot-15", [{**other[0], "about": "paper"}]) == []
    # A kind that says what it is about needs nothing more.
    assert check("pilot-15", [{"kind": "metadata_error", "statement": "Wrong age."}]) == []
