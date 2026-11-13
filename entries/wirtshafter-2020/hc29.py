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
- `GAP_S` (60 s), the shortest spike-free stretch reported as a possible boundary of the maze
  session, and `PIECE`, the samples of Times.mat read at a time, are choices for a data check;
  they decide no claim.
- `CODE_REPO` and `CODE_COMMIT` are the paper's archived code at the commit the claims file
  read, listed only to show what files it holds.
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


CODE_REPO = "elifesciences-publications/data_analysis"
CODE_COMMIT = "5c6320a9133b8ac551300efdd7abbbc44767c575"   # the archived commit the claims file read
GAP_S = 60.0      # a spike-free stretch this long is reported as a candidate epoch boundary
PIECE = 2**23     # samples of Times.mat read at a time


def repo_files(repo: str = CODE_REPO, commit: str = CODE_COMMIT) -> pd.DataFrame:
    """Every file of a GitHub repository at a commit, with its size in bytes, from the git tree."""
    import requests

    r = requests.get(f"https://api.github.com/repos/{repo}/git/trees/{commit}",
                     params={"recursive": "1"}, timeout=60)
    r.raise_for_status()
    j = r.json()
    if j.get("truncated"):
        raise RuntimeError("the git tree listing was truncated")
    df = pd.DataFrame([t for t in j["tree"] if t["type"] == "blob"])[["path", "size"]]
    df["ext"] = df.path.str.extract(r"(\.[^./]+)$")[0].str.lower().fillna("(none)")
    return df


def times_intervals(keys) -> pd.DataFrame:
    """Every sample interval of each recording in Times.mat, read in pieces of PIECE samples:
    the median, how many intervals are not positive, more than 1.5 or less than 0.5 times the
    median, the longest, the shortest of those over 1.5 times the median, and the distinct medians of the pieces (a change of sampling rate
    inside a recording would show as more than one); where the long intervals start (not listed
    below 1 ms sampling) and the first and last timestamps followed by one not later."""
    rows = []
    with fsspec.open(DATA + TIMES, block_size=2**24, cache_type="readahead") as f:
        g = h5py.File(f, "r")["TIMEall"]
        for k in keys:
            d = g[k]
            n = d.shape[0]
            med = None
            counts = {"not_positive": 0, "long": 0, "short": 0}
            longest, longest_at, piece_medians, last = 0.0, np.nan, set(), None
            shortest_long = np.inf
            long_at, repeat_at = [], []
            for s in range(0, n, PIECE):
                x = d[s:s + PIECE, 0]
                y = x if last is None else np.concatenate([[last], x])
                dt = np.diff(y)
                last = x[-1]
                if dt.size == 0:
                    continue
                pm = float(np.median(dt))
                piece_medians.add(round(pm * 1e3, 4))
                if med is None:
                    med = pm
                counts["not_positive"] += int(np.sum(dt <= 0))
                repeat_at += [float(y[j]) for j in np.flatnonzero(dt <= 0)]
                if med >= 1e-3:   # below 1 ms sampling the long intervals are jitter, too many to list
                    long_at +=[round(float(y[j]), 1) for j in np.flatnonzero(dt > 1.5 * med)]
                counts["long"] += int(np.sum(dt > 1.5 * med))
                if np.any(dt > 1.5 * med):
                    shortest_long = min(shortest_long, float(dt[dt > 1.5 * med].min()))
                counts["short"] += int(np.sum((dt > 0) & (dt < 0.5 * med)))
                i = int(np.argmax(dt))
                if dt[i] > longest:
                    longest, longest_at = float(dt[i]), float(y[i])
            rows.append({"times_key": k, "samples": n, "dt_median_ms": 1e3 * med,
                         "piece_medians_ms": sorted(piece_medians), **counts,
                         "longest_ms": 1e3 * longest, "longest_at_s": longest_at,
                         "shortest_long_ms": 1e3 * shortest_long if np.isfinite(shortest_long) else np.nan,
                         "long_at_s": long_at,
                         "not_positive_from_s": min(repeat_at) if repeat_at else np.nan,
                         "not_positive_to_s": max(repeat_at) if repeat_at else np.nan})
    return pd.DataFrame(rows)


def spike_gaps(units: pd.DataFrame, spikes: dict[str, np.ndarray], exclude=(),
               gap_s: float = GAP_S, ranges: pd.DataFrame | None = None) -> pd.DataFrame:
    """For each recording, the spikes of all its clusters pooled (leaving out the keys in
    exclude): the longest stretch with no spike between its first and last spike, and every
    stretch of at least gap_s, with where it starts. With ranges (t_first_s and t_last_s of each
    recording, indexed by times_key), also the silence from the recording's first timestamp to
    the first spike (lead_s) and from the last spike to its last timestamp (trail_s)."""
    rows = []
    for key, grp in units[~units.key.isin(set(exclude))].groupby("times_key"):
        t = np.sort(np.concatenate([spikes[k] for k in grp.key]))
        dt = np.diff(t)
        long = np.flatnonzero(dt >= gap_s)
        row = {"times_key": key, "clusters": len(grp), "spikes": t.size,
               "first_s": t[0], "last_s": t[-1], "longest_gap_s": float(dt.max()) if dt.size else np.nan,
               "longest_gap_at_s": round(float(t[np.argmax(dt)]), 1) if dt.size else np.nan,
               "gaps": len(long), "gap_starts_s": [round(float(t[i]), 1) for i in long],
               "gap_lengths_s": [round(float(dt[i]), 1) for i in long]}
        if ranges is not None:
            row["lead_s"] = t[0] - ranges.loc[key, "t_first_s"]
            row["trail_s"] = ranges.loc[key, "t_last_s"] - t[-1]
        rows.append(row)
    return pd.DataFrame(rows)


def repo_mat_variables(paths, repo: str = CODE_REPO, commit: str = CODE_COMMIT) -> pd.DataFrame:
    """The variables, shapes and classes of MATLAB files of a GitHub repository at a commit, read
    from raw.githubusercontent.com (MATLAB 5 files with scipy, 7.3 files with h5py)."""
    import requests

    rows = []
    for p in paths:
        r = requests.get(f"https://raw.githubusercontent.com/{repo}/{commit}/{p}", timeout=60)
        r.raise_for_status()
        try:
            for name, shape, cls in sio.whosmat(io.BytesIO(r.content)):
                rows.append({"path": p, "variable": name, "shape": str(shape), "class": cls})
        except Exception:
            h = h5py.File(io.BytesIO(r.content), "r")
            h.visititems(lambda n, d: rows.append({"path": p, "variable": n, "shape": str(d.shape),
                                                   "class": str(d.dtype)})
                         if isinstance(d, h5py.Dataset) else None)
    return pd.DataFrame(rows)
