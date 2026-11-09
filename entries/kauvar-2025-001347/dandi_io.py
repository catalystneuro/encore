"""Streaming access to dandiset 001347 (Kauvar, Richman, Liu et al. 2025) and 001326.

Every notebook of this entry reads the NWB files through this module. Files are
streamed from the DANDI Archive with remfile and h5py; nothing is written to disk.

Version: 001347 has one published version, 0.250528.0702 (28 May 2025), the
day before the paper's publication (29 May 2025). The paper cites the dandiset
without a version, so the latest published version is pinned (protocol, author
step 1.3). The mouse Neuropixels data of the paper are in dandiset 001326,
pinned likewise at its only published version, 0.250528.1957.
"""
import functools

import h5py
import remfile
import requests

DANDISET = "001347"
VERSION = "0.250528.0702"
NPX_DANDISET = "001326"
NPX_VERSION = "0.250528.1957"
API = "https://api.dandiarchive.org/api"


@functools.lru_cache(maxsize=None)
def list_assets(dandiset=DANDISET, version=VERSION):
    """Return {path: asset_id} for every asset of a pinned dandiset version."""
    out = {}
    url = f"{API}/dandisets/{dandiset}/versions/{version}/assets/?page_size=1000"
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        d = r.json()
        for a in d["results"]:
            out[a["path"]] = a["asset_id"]
        url = d["next"]
    return out


def asset_url(path, dandiset=DANDISET, version=VERSION):
    """Download URL of an asset, resolved through the pinned version's asset list."""
    return f"{API}/assets/{list_assets(dandiset, version)[path]}/download/"


def open_h5(path, dandiset=DANDISET, version=VERSION):
    """Open an NWB file of the pinned version as a streamed h5py.File."""
    return h5py.File(remfile.File(asset_url(path, dandiset, version)), "r")
