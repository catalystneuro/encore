"""The registry's archive adapters: one module per archive, each defining ARCHIVE.

An adapter says everything the registry needs to know about an archive: how its datasets are named and
shown, where a dataset's page is, which target list holds its datasets, what an agent is told about reading
them, which hosts an agent's commands may reach, and, for an archive whose files need credentials, how the
files are put in place before an agent starts (stage), and the secrets that takes. The details an agent
reads are in docs/archives.md, under the archive's heading.

To add an archive, add a module here (docs/archives.md, "Adding an archive"); nothing else lists them.
"""

from __future__ import annotations

import importlib
import pkgutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

# Where stage() puts an archive's files: /tmp/<archive>/<id>/<version>/, readable by an agent's sandbox.
STAGED = Path("/tmp")


@dataclass(frozen=True)
class Archive:
    key: str            # dandi: the first part of a dataset's key, and of its folder name (but for DANDI)
    label: str          # DANDI: how the site and the record name it
    name: str           # the DANDI Archive: in sentences
    url: str            # a dataset's page, with {id}; a target's own url, when it has one, wins
    access: str         # what an agent is told about reading a dataset, with the target's fields as {name}
    list: str           # the target list in targets/
    case: str = ""      # "upper" or "lower" when identifiers ignore case: keyed in lower case, shown in this one
    hosts: tuple[str, ...] = ()      # the hosts an agent's commands may reach to read it (encore check's sandbox)
    builder: str = ""   # the script that builds the target list, when it is not written by hand
    secrets: tuple[str, ...] = ()    # the environment variables stage() needs; the workflows pass them
    stage: Callable[[dict, Path], Path] | None = field(default=None, compare=False)
    # stage(target, root) puts the files of the target's pinned version under root/<archive>/<id>/<version>/,
    # checks them, and returns that directory. Only for an archive that agents cannot read directly.

    def as_dict(self) -> dict:
        """The fields tools/datasets.py has always given as ARCHIVES[<archive>]."""
        out = {"label": self.label, "name": self.name, "url": self.url, "access": self.access, "list": self.list}
        return {**out, "case": self.case} if self.case else out


def _load() -> dict[str, Archive]:
    found = {}
    for info in pkgutil.iter_modules(__path__):
        archive = getattr(importlib.import_module(f"{__name__}.{info.name}"), "ARCHIVE", None)
        if isinstance(archive, Archive):
            found[archive.key] = archive
    # DANDI first, as the registry began with it; local and remote, which only encore check uses, last.
    order = ["dandi"] + sorted(set(found) - {"dandi", "local", "remote"}) + ["local", "remote"]
    return {k: found[k] for k in order if k in found}


ALL: dict[str, Archive] = _load()
