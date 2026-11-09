"""Datasets and the archives that hold them: how the registry names, finds and files a dataset.

    python tools/datasets.py folder DATASET    # the dataset's folder name: 000003, ebrains-<id>
    python tools/datasets.py label DATASET     # how it is shown: DANDI:000003
    python tools/datasets.py key DATASET       # how it is keyed: dandi:000003

DATASET may be given as a key (dandi:000003), a label (DANDI:000003), a folder name (000003,
ebrains-<id>) or, for DANDI, the bare identifier. A dataset is keyed as "<archive>:<id>". Its
files in the repository (claims/, questions/, transcripts/, attempt branches, the paper store) are
under its folder name: the identifier alone for DANDI, which the registry began with, and
"<archive>-<id>" for any other archive. How an agent reads each archive's datasets is in
docs/archives.md.

Each archive is an adapter, a module in tools/archives/ (docs/archives.md, "Adding an archive"). Targets come
from each archive's list in targets/, built by the adapter's builder or written by hand.
"""

from __future__ import annotations

import functools
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from archives import ALL as ADAPTERS  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]

# Each archive's adapter is a module in tools/archives/. ARCHIVES gives its fields as a dict, as it always has:
# label: how the site names it; url: a dataset's page there; access: what an agent is told about reading
# its datasets (the details are in docs/archives.md, under the archive's heading).
ARCHIVES = {key: archive.as_dict() for key, archive in ADAPTERS.items()}


def key_of(archive: str, id_: str) -> str:
    # An archive whose identifiers ignore case is keyed in lower case, as its folders are.
    return f"{archive}:{id_.lower() if ARCHIVES.get(archive, {}).get('case') else id_}"


def split_key(key: str) -> tuple[str, str]:
    archive, _, id_ = key.partition(":")
    return archive, id_


def label(key: str) -> str:
    """How a dataset is named to people: DANDI:000003, EBRAINS:Q0FG-1X8."""
    archive, id_ = split_key(key)
    spec = ARCHIVES.get(archive, {})
    return f'{spec.get("label", archive.upper())}:{id_.upper() if spec.get("case") == "upper" else id_}'


def folder(key: str) -> str:
    """The folder name a dataset's files have in the repository."""
    archive, id_ = split_key(key)
    return id_ if archive == "dandi" else f"{archive}-{id_}"


def key_of_folder(name: str) -> str:
    return key_of("dandi", name) if re.fullmatch(r"[0-9]{6}", name) else key_of(*name.split("-", 1))


def parse(text: str) -> str:
    """A dataset's key from any of the ways it is written."""
    text = text.strip()
    if re.fullmatch(r"[0-9]{6}", text):
        return key_of("dandi", text)
    if ":" in text:
        archive, id_ = text.split(":", 1)
        archive = next((a for a, v in ARCHIVES.items() if v["label"].lower() == archive.lower()), archive.lower())
        if not re.fullmatch(r"[a-z][a-z0-9]*", archive) or not re.fullmatch(r"[A-Za-z0-9._-]+", id_):
            raise ValueError(f"not a dataset: {text!r}")
        return key_of(archive, id_)
    if re.fullmatch(r"[a-z][a-z0-9]*-[A-Za-z0-9._-]+", text):
        return key_of_folder(text)
    raise ValueError(f"not a dataset: {text!r}")


def url(key: str) -> str:
    """A dataset's page at its archive: the target list's own address for it, else the archive's pattern."""
    listed = _urls().get(key)
    if listed:
        return listed
    archive, id_ = split_key(key)
    return ARCHIVES[archive]["url"].format(id=id_) if archive in ARCHIVES else ""


@functools.lru_cache(maxsize=1)
def _urls() -> dict[str, str]:
    return {t["key"]: t["url"] for t in targets() if t.get("url")}


def archive_name(key: str) -> str:
    return ARCHIVES.get(split_key(key)[0], {}).get("name", split_key(key)[0])


def access(key: str) -> str:
    """What an agent is told about reading this dataset's archive, with the target's own fields filled in."""
    archive = split_key(key)[0]
    text = ARCHIVES.get(archive, {}).get("access", f'Read the data as docs/archives.md says under "{archive}".')
    target = next((t for t in targets() if t["key"] == key), {})
    return text.format(**{k: v for k, v in target.items() if isinstance(v, str)})


def targets() -> list[dict]:
    """Every target of every archive's list, each with its key, archive, id and folder."""
    out = []
    for archive, spec in ARCHIVES.items():
        path = ROOT / "targets" / spec["list"]
        if not path.is_file():
            continue
        for t in json.loads(path.read_text())["targets"]:
            if t.get("archive", archive) != archive:   # local.json holds both local and remote datasets
                continue
            id_ = t.get("id") or t["dandiset"]
            key = key_of(archive, id_)
            out.append({**t, "key": key, "archive": archive, "id": id_, "folder": folder(key)})
    return out


def main() -> int:
    if len(sys.argv) != 3 or sys.argv[1] not in ("folder", "label", "key"):
        sys.exit(__doc__)
    try:
        key = parse(sys.argv[2])
    except ValueError as err:
        sys.exit(f"error: {err}")
    print({"folder": folder, "label": label, "key": lambda k: k}[sys.argv[1]](key))
    return 0


if __name__ == "__main__":
    sys.exit(main())
