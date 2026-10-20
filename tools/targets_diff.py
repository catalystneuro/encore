"""Say what changed between two versions of the target list, for the pull request that updates it.

    python tools/targets_diff.py OLD.json NEW.json

Prints a Markdown summary: new targets (dandisets that now name a paper), papers added to or removed
from existing targets, new published versions of attempted dandisets, and targets that are gone.
Exits 1 when the targets did not change (the list's `generated` time and counts aside), else 0.
Used by .github/workflows/targets.yml.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DANDI = "https://dandiarchive.org/dandiset"


def attempted() -> set[str]:
    return {p.name.split("-", 1)[0] for p in (ROOT / "attempts").glob("*.yaml")}


def summary(old: dict, new: dict, tried: set[str]) -> str | None:
    before = {t["dandiset"]: t for t in old["targets"]}
    after = {t["dandiset"]: t for t in new["targets"]}
    if before == after:
        return None
    link = lambda d: f"[{d}]({DANDI}/{d})"  # noqa: E731
    doi = lambda p: f"[{p['doi']}](https://doi.org/{p['doi']})"  # noqa: E731
    out = []
    added = [after[d] for d in after if d not in before]
    if added:
        out.append(f"### New targets ({len(added)})\n")
        out += [f"- {link(t['dandiset'])} {t['name']}: " + ", ".join(doi(p) for p in t["papers"])
                + (" (converted by CatalystNeuro)" if t.get("catalystneuro") else "") for t in added]
    papers, versions = [], []
    for d in sorted(set(before) & set(after)):
        was = {p["doi"].lower() for p in before[d]["papers"]}
        now = {p["doi"].lower() for p in after[d]["papers"]}
        note = " **attempted: its new papers need claims**" if d in tried and now - was else ""
        if now != was:
            papers.append(f"- {link(d)}: " + ", ".join(
                [f"added {doi(p)}" for p in after[d]["papers"] if p["doi"].lower() in now - was]
                + [f"removed {doi(p)}" for p in before[d]["papers"] if p["doi"].lower() in was - now]) + note)
        if d in tried and before[d].get("published_version") != after[d].get("published_version"):
            versions.append(f"- {link(d)}: {before[d].get('published_version') or 'none'} → "
                            f"{after[d].get('published_version')}, a candidate for a repeat attempt")
    if papers:
        out.append(f"\n### Papers changed on existing targets ({len(papers)})\n")
        out += papers
    if versions:
        out.append(f"\n### New versions of attempted dandisets ({len(versions)})\n")
        out += versions
    gone = [d for d in before if d not in after]
    if gone:
        out.append(f"\n### No longer targets ({len(gone)})\n")
        out += [f"- {link(d)} {before[d]['name']}" + (" (attempted)" if d in tried else "") for d in gone]
    other = sum(1 for d in set(before) & set(after) if before[d] != after[d]) - len(papers) - len(versions)
    if other > 0:
        out.append(f"\n{other} other targets changed in their metadata (size, files, species and so on).")
    return "\n".join(out) + "\n"


def main() -> int:
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    old, new = (json.loads(Path(p).read_text()) for p in sys.argv[1:])
    text = summary(old, new, attempted())
    if text is None:
        return 1
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
