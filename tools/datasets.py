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

Targets come from each archive's list in targets/: targets/dandisets.json is DANDI's, built by
tools/build_targets.py; targets/crcns.json is CRCNS's, written by hand.
"""

from __future__ import annotations

import functools
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# label: how the site names it; url: a dataset's page there; access: what an agent is told about reading
# its datasets (the details are in docs/archives.md, under the archive's heading).
ARCHIVES = {
    "dandi": {
        "label": "DANDI", "name": "the DANDI Archive", "url": "https://dandiarchive.org/dandiset/{id}",
        "access": ("Use the DANDI API (docs/archives.md, \"DANDI\") and stream the NWB files; do not download "
                   "them to disk."),
        "list": "dandisets.json",
    },
    "crcns": {
        "label": "CRCNS", "name": "CRCNS.org", "url": "https://crcns.org/data-sets",
        "access": ("Read the files anonymously from the public S3 bucket crcnsarchive "
                   "(https://crcnsarchive.s3-us-west-2.amazonaws.com/<id>/), as docs/archives.md says under "
                   "\"CRCNS\": stream them, opening a zip in place with fsspec and zipfile; do not download them "
                   "to disk."),
        "list": "crcns.json",
    },
}


def key_of(archive: str, id_: str) -> str:
    return f"{archive}:{id_}"


def split_key(key: str) -> tuple[str, str]:
    archive, _, id_ = key.partition(":")
    return archive, id_


def label(key: str) -> str:
    """How a dataset is named to people: DANDI:000003."""
    archive, id_ = split_key(key)
    return f'{ARCHIVES.get(archive, {}).get("label", archive.upper())}:{id_}'


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
    """What an agent is told about reading this dataset's archive."""
    archive = split_key(key)[0]
    return ARCHIVES.get(archive, {}).get("access", f'Read the data as docs/archives.md says under "{archive}".')


def targets() -> list[dict]:
    """Every target of every archive's list, each with its key, archive, id and folder."""
    out = []
    for archive, spec in ARCHIVES.items():
        path = ROOT / "targets" / spec["list"]
        if not path.is_file():
            continue
        for t in json.loads(path.read_text())["targets"]:
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
