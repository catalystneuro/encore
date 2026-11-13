"""Loading and checks for CRCNS hc-29 (Wirtshafter and Wilson 2020, eLife 9:e55252).

The data set (doi:10.6080/K0NG4NV8) is three MATLAB files under hc-29/live/data/ in the public
S3 bucket crcnsarchive:

- HPC_clusters.mat and LS_clusters.mat (MATLAB 5 files): one struct per region (`CLUSTERShpc`,
  `CLUSTERSls`), one field per sorted cluster, named
  `cluster_<rat>_<yyyy_mm_dd>[_<session suffix>]_<tetrode>[_maze]_cl_<cluster>`, each holding
  a column of spike times in seconds.
- Times.mat (MATLAB 7.3, HDF5): struct `TIMEall`, one field per recording,
  `date_<rat>_<yyyy_mm_dd>[_<session suffix>]_time`, each a column of sample timestamps in
  seconds.

The data set's description says the files hold sorted spikes and "time files for all
sessions"; nothing else is in the data set (spiketrain.m, an example script, and the
description). Files are streamed from the bucket with fsspec; nothing is written to disk.

Where the parameters come from:

- The names are parsed as the data description gives them ("labeled with each session date,
  tetrode number, and cluster number"); the session suffixes (`run_1`, `maze_and_sleep` and so
  on) are matched to the Times.mat fields of the same rat and date, a choice made here so that
  each cluster can be put on its recording's clock.
- `COINCIDENCE_S` (0.5 ms) and `DUPLICATE_FRACTION` (0.5), used to look for units deposited
  twice, are standard choices for a data check; they decide no claim.
- `MIN_RATE_HZ` (0.05 Hz) is the paper's rate threshold (Methods, Bits/spike: "Cells with a mean
  firing rate below 0.05 Hz above the speed threshold were excluded"). Without positions it is
  applied here over the whole recording, as a variant that decides no claim.
"""

from __future__ import annotations

import hashlib
import io
import re

import fsspec
import h5py
import numpy as np
import pandas as pd
import scipy.io as sio

BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-29/live/"
DATA = BUCKET + "data/"
DATASET = "crcns:hc-29"
VERSION = "unversioned"   # CRCNS data sets are not versioned; MD5 sums pin the files read
DOI = "10.6080/K0NG4NV8"
FILES = {"HPC": "HPC_clusters.mat", "LS": "LS_clusters.mat"}
TIMES = "Times.mat"

COINCIDENCE_S = 0.0005
DUPLICATE_FRACTION = 0.5
MIN_RATE_HZ = 0.05
EDGE_SAMPLES = 8000

NAME = re.compile(r"^cluster_(rat\d+)_(\d{4}_\d\d_\d\d)_(.*?)_?cl_?(\w+)$")
REST = re.compile(r"^(?:(?P<suffix>.*)_)?(?P<tetrode>\d+)(?P<maze>_maze)?$")


def list_bucket() -> pd.DataFrame:
    """Every object under hc-29/ in the bucket, with its size in bytes."""
    import requests

    r = requests.get("https://crcnsarchive.s3-us-west-2.amazonaws.com/",
                     params={"list-type": "2", "prefix": "hc-29/"}, timeout=60)
    r.raise_for_status()
    found = re.findall(r"<Key>(.*?)</Key>.*?<Size>(\d+)</Size>", r.text)
    return pd.DataFrame(found, columns=["key", "bytes"]).astype({"bytes": int})


def checksums() -> dict[str, str]:
    """The data set's own checksums.md5, as {path: md5}."""
    with fsspec.open(BUCKET + "checksums.md5", "rt") as f:
        lines = [ln.split() for ln in f.read().splitlines() if ln.strip()]
    return {path: md5 for md5, path in lines}


def read_bytes(name: str) -> bytes:
    with fsspec.open(DATA + name, block_size=2**22) as f:
        return f.read()


def stream_md5(name: str, block: int = 2**24) -> tuple[str, int]:
    """MD5 of a file read as a stream in 16 MB blocks, never held whole."""
    h, n = hashlib.md5(), 0
    with fsspec.open(DATA + name, block_size=block) as f:
        while True:
            b = f.read(block)
            if not b:
                break
            h.update(b)
            n += len(b)
    return h.hexdigest(), n


def parse_name(name: str) -> dict:
    """Rat, date, session suffix, tetrode and cluster from a cluster's field name."""
    m = NAME.match(name)
    if not m:
        raise ValueError(f"unparsed cluster name {name}")
    rat, date, rest, cluster = m.groups()
    r = REST.match(rest)
    if not r:
        raise ValueError(f"unparsed tetrode part {rest!r} in {name}")
    suffix = r.group("suffix") or ""
    return {"rat": rat, "date": date, "suffix": suffix, "tetrode": int(r.group("tetrode")),
            "cluster": cluster, "maze_tag": bool(r.group("maze")),
            "standard_form": bool(re.search(r"_cl_\w+$", name)),
            "times_key": f"date_{rat}_{date}{'_' + suffix if suffix else ''}_time"}


def load_units() -> tuple[pd.DataFrame, dict[str, np.ndarray], dict[str, bytes]]:
    """All clusters of both regions: a table of their names and spike counts, the spike times
    by unique key (region and field name), and the raw bytes of each file (for the MD5)."""
    rows, spikes, raw = [], {}, {}
    for region, fname in FILES.items():
        b = read_bytes(fname)
        raw[region] = b
        m = sio.loadmat(io.BytesIO(b))
        var = [k for k in m if not k.startswith("__")]
        assert len(var) == 1, var
        s = m[var[0]]
        for field in s.dtype.names:
            t = np.asarray(s[field][0, 0], dtype=float).ravel()
            key = f"{region}:{field}"
            spikes[key] = t
            rows.append({"key": key, "region": region, "variable": var[0], "field": field,
                         **parse_name(field), "n_spikes": t.size,
                         "first_s": t.min() if t.size else np.nan,
                         "last_s": t.max() if t.size else np.nan,
                         "sorted": bool(np.all(np.diff(t) >= 0)),
                         "shape": str(s[field][0, 0].shape)})
    return pd.DataFrame(rows), spikes, raw


def times_layout() -> pd.DataFrame:
    """Every field of Times.mat with its length, dtype and HDF5 attributes, from the metadata."""
    with fsspec.open(DATA + TIMES, block_size=2**16, cache_type="readahead") as f:
        h = h5py.File(f, "r")
        out = []
        for top in h.keys():
            if top.startswith("#"):
                continue
            g = h[top]
            for k in g.keys():
                d = g[k]
                out.append({"variable": top, "times_key": k, "samples": d.shape[0],
                            "shape": str(d.shape), "dtype": str(d.dtype),
                            "matlab_class": d.attrs.get("MATLAB_class", b"").decode()})
        return pd.DataFrame(out)


def times_edges(keys) -> pd.DataFrame:
    """First and last EDGE_SAMPLES timestamps of each recording: start, end, sample interval,
    and whether the span equals (samples - 1) x the median interval (no gaps)."""
    rows = []
    with fsspec.open(DATA + TIMES, block_size=2**16, cache_type="readahead") as f:
        g = h5py.File(f, "r")["TIMEall"]
        for k in keys:
            d = g[k]
            n = d.shape[0]
            a = d[:EDGE_SAMPLES, 0]
            z = d[n - EDGE_SAMPLES:, 0]
            dt = np.median(np.diff(a))
            rows.append({"times_key": k, "samples": n, "t_first_s": a[0], "t_last_s": z[-1],
                         "dt_median_ms": 1e3 * dt, "dt_min_ms": 1e3 * np.diff(a).min(),
                         "dt_max_ms": 1e3 * np.diff(a).max(),
                         "monotonic_edges": bool(np.all(np.diff(a) > 0) and np.all(np.diff(z) > 0)),
                         "span_over_n_dt": (z[-1] - a[0]) / ((n - 1) * dt)})
    return pd.DataFrame(rows)


def coincident_fraction(a: np.ndarray, b: np.ndarray, tol: float = COINCIDENCE_S) -> float:
    """Fraction of the spikes of the smaller train that have a spike of the other within tol."""
    if a.size > b.size:
        a, b = b, a
    if a.size == 0 or b.size == 0:
        return 0.0
    i = np.searchsorted(b, a)
    lo = np.abs(a - b[np.clip(i - 1, 0, b.size - 1)])
    hi = np.abs(b[np.clip(i, 0, b.size - 1)] - a)
    return float(np.mean(np.minimum(lo, hi) <= tol))


def identical_groups(spikes: dict[str, np.ndarray]) -> list[list[str]]:
    """Groups of two or more clusters whose spike time arrays are byte for byte identical."""
    digests: dict[str, list[str]] = {}
    for k, t in spikes.items():
        digests.setdefault(hashlib.md5(t.tobytes()).hexdigest(), []).append(k)
    return [ks for ks in digests.values() if len(ks) > 1]


def duplicate_pairs(units: pd.DataFrame, spikes: dict[str, np.ndarray]) -> pd.DataFrame:
    """Pairs of clusters on the same recording (either region) sharing at least
    DUPLICATE_FRACTION of the smaller train's spikes within COINCIDENCE_S, and all pairs with
    identical spike times anywhere in the data set."""
    rows = []
    for key, grp in units.groupby("times_key"):
        ks = list(grp.key)
        for i in range(len(ks)):
            for j in range(i + 1, len(ks)):
                fr = coincident_fraction(spikes[ks[i]], spikes[ks[j]])
                if fr >= DUPLICATE_FRACTION:
                    rows.append({"a": ks[i], "b": ks[j], "same_recording": True,
                                 "coincident_fraction": fr,
                                 "identical": np.array_equal(spikes[ks[i]], spikes[ks[j]])})
    recording = units.set_index("key").times_key
    for ks in identical_groups(spikes):
        for i in range(len(ks)):
            for j in range(i + 1, len(ks)):
                if recording[ks[i]] != recording[ks[j]]:
                    rows.append({"a": ks[i], "b": ks[j], "same_recording": False,
                                 "coincident_fraction": 1.0, "identical": True})
    return pd.DataFrame(rows, columns=["a", "b", "same_recording", "coincident_fraction", "identical"])
