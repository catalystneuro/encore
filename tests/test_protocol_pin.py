"""The protocol version is written out in protocol.lock and in every workflow that calls encore-protocol's
workflows, since a reusable workflow's version cannot come from a file. They must agree."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CALL = re.compile(r"uses: encorescience/encore-protocol/\.github/workflows/[a-z-]+\.yml@(\S+)")


def test_every_call_of_the_protocol_names_the_version_in_protocol_lock():
    lock = (ROOT / "protocol.lock").read_text().strip()
    calls = {path.name: CALL.findall(path.read_text()) for path in (ROOT / ".github" / "workflows").glob("*.yml")}
    assert {name for name, refs in calls.items() if refs} == {"attempt.yml", "papers.yml", "attempt-sequence.yml"}
    assert {name: set(refs) for name, refs in calls.items() if refs and set(refs) != {lock}} == {}


def test_the_protocol_version_is_a_tag_or_a_whole_commit():
    lock = (ROOT / "protocol.lock").read_text().strip()
    assert re.fullmatch(r"v\d+\.\d+\.\d+|[0-9a-f]{40}", lock)


def test_every_input_passed_to_the_protocol_is_declared_there():
    # papers.yml passed papers_only, which encore-protocol v0.1.0 did not declare for a call: every run of it failed
    # at startup (2026-11-23). The called workflows are read from the cache tools/protocol.sh keeps, at the version
    # protocol.lock names.
    import os
    import subprocess

    import pytest
    import yaml
    lock = (ROOT / "protocol.lock").read_text().strip()
    cache = Path(os.environ.get("ENCORE_CACHE") or Path.home() / ".cache" / "encore") / "protocol.git"
    if not cache.is_dir():
        pytest.skip("no cached clone of encore-protocol: run tools/protocol.sh")
    for path in (ROOT / ".github" / "workflows").glob("*.yml"):
        for job in (yaml.safe_load(path.read_text()).get("jobs") or {}).values():
            m = CALL.match("uses: " + str(job.get("uses", "")))
            if not m:
                continue
            name = job["uses"].split("/")[-1].split("@")[0]
            called = yaml.safe_load(subprocess.run(["git", "-C", str(cache), "show", f"{lock}:.github/workflows/{name}"],
                                                   capture_output=True, text=True, check=True).stdout)
            declared = set(called[True]["workflow_call"]["inputs"])
            assert set(job.get("with") or {}) <= declared, (path.name, name, set(job["with"]) - declared)
