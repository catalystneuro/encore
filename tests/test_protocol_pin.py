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
