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
tools/build_targets.py; targets/crcns.json and targets/ebrains.json are written by hand; targets/dryad.json is built from chosen DOIs by
tools/build_dryad_targets.py.
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
                   "(https://crcnsarchive.s3-us-west-2.amazonaws.com/{id}/), as docs/archives.md says under "
                   "\"CRCNS\": stream them, opening a zip in place with fsspec and zipfile; do not download them "
                   "to disk."),
        "list": "crcns.json",
    },
    "ebrains": {
        # A dataset is named by its DOI's suffix (10.25493/Q0FG-1X8 is q0fg-1x8, shown Q0FG-1X8); the data proxy
        # needs its Knowledge Graph id, which the target list gives as kg_id.
        "label": "EBRAINS", "name": "EBRAINS", "url": "https://doi.org/10.25493/{id}", "case": "upper",
        "access": ("Read the files anonymously through the EBRAINS data proxy "
                   "(https://data-proxy.ebrains.eu/api/v1/public/datasets/{kg_id}/<file>), as docs/archives.md says "
                   "under \"EBRAINS\": stream each file into memory with fsspec; do not download them to disk."),
        "list": "ebrains.json",
    },
    "dryad": {
        # A dataset is named by its DOI's suffix without "dryad." (10.5061/dryad.bvq83bkk9 is bvq83bkk9); Dryad DOIs
        # ignore case. published_version is the id of the dataset's version in Dryad's API, which pins it.
        "label": "DRYAD", "name": "Dryad", "url": "https://doi.org/10.5061/dryad.{id}", "case": "lower",
        "access": ("Read the files through Dryad's API v2 (https://datadryad.org/api/v2/versions/{published_version}/"
                   "files), as docs/archives.md says under \"Dryad\": downloads need the bearer token in the "
                   "environment variable DRYAD_TOKEN; read each file into memory (pandas, openpyxl, zipfile on a "
                   "BytesIO) and check its SHA-256 against the listing; do not write the files to disk."),
        "list": "dryad.json",
    },
    # The two kinds of dataset `encore check` runs on (encore_science/, docs/encore.md), which never enter the
    # registry's record: a directory on the machine running it, and files at a URL. Their list is written for
    # the run alone, into the run's own copy of the registry.
    "local": {
        "label": "local", "name": "a directory on this machine", "url": "",
        "access": ("The dataset is the directory {path} on this machine. Read its files in place: do not copy, "
                   "move or change them, and do not look for the dataset in any archive (docs/protocol.md, "
                   "\"Local and remote datasets\")."),
        "list": "local.json",
    },
    "remote": {
        "label": "remote", "name": "files at a URL", "url": "",
        "access": ("The dataset is the files at {url}. Stream them with fsspec, or the store's own client; do not "
                   "download them to disk, and do not look for the dataset in any archive (docs/protocol.md, "
                   "\"Local and remote datasets\")."),
        "list": "local.json",
    },
}


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
