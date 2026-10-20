"""Draft the issue that starts fixing a conversion from what the registry found.

    python tools/conversion_issue.py DANDISET > issue.md

Prints a title on the first line and the body after a blank line, for the conversion repository
(docs/fixing-conversions.md). Each finding of the dandiset's latest attempt becomes a checklist
item for the person who converted it to triage. Nothing is posted.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from agent_run import attempt_of  # noqa: E402

SITE = "https://catalystneuro.github.io/reproduction-registry"
REPO = "https://github.com/catalystneuro/reproduction-registry"


def issue(dandiset: str) -> str:
    found = attempt_of(dandiset)
    if found is None:
        raise SystemExit(f"error: no attempt on dandiset {dandiset}")
    record, entry_dir = found
    version = record["dataset"]["version"]
    dandi = (f"https://dandiarchive.org/dandiset/{dandiset}/{version}" if version != "draft"
             else f"https://dandiarchive.org/dandiset/{dandiset}/draft")
    findings = record.get("findings") or []
    items = "\n".join(f"- [ ] {i}. ({f['kind']}) {' '.join(f['statement'].split())}"
                      for i, f in enumerate(findings, 1))
    return f"""Problems found in DANDI:{dandiset} by a reproduction attempt

An agent attempt to reproduce the paper from the published dandiset ([DANDI:{dandiset}]({dandi}), version {version}) recorded {len(findings)} findings about the data. The details are in the reproduction registry ([findings]({SITE}/datasets/dandi/{dandiset}/#findings), [attempt record]({REPO}/blob/main/attempts/{record['id']}.yaml), [notebook]({REPO}/tree/main/entries/{entry_dir.name})). The attempt was made and checked by AI agents, so each finding needs confirming against the source data before anything is changed.

For each finding, the person who converted the data notes whether it holds, and if it does, where it comes from: the conversion code, information the source has that the conversion dropped, or something the source data does not contain.

{items}

Steps ([fixing conversions]({REPO}/blob/main/docs/fixing-conversions.md) in the registry):
- [ ] Triage every finding above
- [ ] Fix what the conversion can fix, in a pull request linked here
- [ ] Test the fix on a few sessions, and run NWB Inspector
- [ ] Re-convert and upload to the dandiset's draft, without publishing
- [ ] Re-check: a registry repeat attempt on the draft
- [ ] Publish a new version
- [ ] Link this repository from the dandiset's metadata, if it is not linked yet
"""


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    print(issue(sys.argv[1]))
