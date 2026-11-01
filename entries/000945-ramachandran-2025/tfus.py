"""Loading and response measures for dandiset 000945 (tFUS in awake and anesthetized rat S1).

Ramachandran, Gao, Yttri, Yu & He (2025), J Neural Eng 22 026022, doi:10.1088/1741-2552/adbb1f.

Each NWB file holds one recording: sorted units (`units/spike_times`, and in 60 of the 75 files a
`celltype_label`, "1 = RSU, 2 = FSU") and a trial table whose `start_time` is taken as the
ultrasound trigger (time 0; checked in the notebook). The condition is only in the file's
`identifier`, as `<rat>_<PRF Hz>_<TBD us>[_2][_anes|_anes2]`. Files are streamed from the archive
at the pinned version; nothing is written to disk.

Where the parameters come from:

- PSTH from -0.5 to 1.5 s around the trigger, divided by the number of trials; baseline the 0.5 s
  before onset; response the mean rate in a window as a percent of baseline (Methods 2.4, "PSTHs
  were computed from 0.5 s prior to ultrasound stimulation, until 1.5 s afterwards ... Baseline was
  computed from the 0.5 s before tFUS onset, and the response to tFUS was characterized as the
  normalized spike rate as a percent of baseline within the specified time span").
- Bin 35.7 ms (Figure 4 legend, "bin size: 35.7 ms"), taken as 1/28 s so that the 0.5 s baseline
  is 14 whole bins with an edge at 0 (claims file header).
- Windows: time-locked 0 to 67 ms (Methods 2.4, "the response during the 67 ms ultrasound
  stimulation"); delayed 0.5 to 1 s awake and 0.2 to 0.7 s anesthetized (Figure 5 legend). The
  claims file names two ways to measure a window that is not on bin edges: W1, spikes in the exact
  window; W2, the PSTH bins that overlap it. Both are computed.
- Delayed-response latency (Methods 2.4, "at least three consecutive time bins in their PSTH with
  value greater or equal to one SEM above baseline. Latency was then characterized as the time bin
  of the first of the three"). The SEM (S1, S2), the first bin allowed (D1, D2) and the time of a
  bin (L1, L2) are the claims file's readings; every combination is computed.
- A unit with no spike in the baseline cannot be normalized and is left out (claims file header, a
  standard choice; the count is reported).
- The 5 ms PSTH (`psth5`) is a display and clock-check choice that cannot change an outcome.
"""

from __future__ import annotations

import itertools
import re
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import stats

DANDISET_ID = "000945"
DANDISET_VERSION = "0.250213.2212"   # the version the paper cites (reference 50)

BIN = 1 / 28                          # 35.714 ms
PRE, POST = 0.5, 1.5
EDGES = np.round(np.arange(-14, 43) * BIN, 10)  # 56 bins from -0.5 to 1.5 s
N_BASE_BINS = 14
US_DURATION = 0.067
FINE = 0.005
FINE_EDGES = np.round(np.arange(-PRE, POST + FINE / 2, FINE), 10)

# Windows in seconds from the trigger. *_w2 are the bins that overlap the window.
WINDOWS = {
    "base": (-0.5, 0.0),
    "tl_w1": (0.0, 0.067),
    "tl_w2": (0.0, 2 * BIN),
    "del_awake": (0.5, 1.0),           # on bin edges, the same under W1 and W2
    "del_anes_w1": (0.2, 0.7),
    "del_anes_w2": (5 * BIN, 20 * BIN),
    # clock check: the same 67 ms window and 0.5 s baseline, 1.25 s later (mid-interval)
    "shift_base": (0.75, 1.25),
    "shift_tl": (1.25, 1.25 + 0.067),
}

PRF_ISPTA = {30: 0.6, 300: 6.03, 1500: 30.13, 3000: 60.26, 4500: 90.39}  # mW/cm2, Methods 2.3
TBD_DC = {40: 6, 200: 30, 400: 60}                                       # us -> %, Methods 2.3

_IDENT = re.compile(r"^(BH\d+)_(\d+)_(\d+)(_2)?(_anes2?)?$")


def parse_identifier(ident: str) -> dict:
    """Rat, PRF, TBD, state and repeat flag from an identifier such as BH498_1500_200_2."""
    m = _IDENT.match(ident)
    if not m:
        raise ValueError(f"unexpected identifier {ident}")
    rat, prf, tbd, rep, anes = m.groups()
    return {"rat": rat, "prf": int(prf), "tbd": int(tbd), "dc": TBD_DC.get(int(tbd)),
            "state": "anesthetized" if anes else "awake",
            "repeat": bool(rep) or anes == "_anes2"}


def asset_list() -> list[dict]:
    """Path, asset id, size and streaming URL of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return sorted(({"path": a.path, "asset_id": a.identifier, "size": a.size,
                        "url": a.get_content_url(follow_redirects=1, strip_query=True)}
                       for a in ds.get_assets() if a.path.endswith(".nwb")), key=lambda r: r["path"])


def dandiset_description() -> str:
    """The dandiset's description at the pinned version (it describes the `_2` repeats)."""
    with DandiAPIClient() as client:
        return client.get_dandiset(DANDISET_ID, DANDISET_VERSION).get_raw_metadata()["description"]


def _str(v) -> str:
    v = v[()] if hasattr(v, "shape") else v
    if isinstance(v, np.ndarray):        # the unlabelled anesthetized files store session_start_time as an array
        v = v.ravel()[0]
    return v.decode() if isinstance(v, bytes) else str(v)


def _counts(st: np.ndarray, tr: np.ndarray, lo: float, hi: float) -> np.ndarray:
    """Spikes of one unit in [t + lo, t + hi) for each trial t."""
    return (np.searchsorted(st, tr + hi, "left") - np.searchsorted(st, tr + lo, "left")).astype(np.int32)


def load_session(asset: dict) -> dict:
    """Read one file and reduce it to per-unit, per-trial window counts and trial-averaged PSTHs."""
    with h5py.File(remfile.File(asset["url"]), "r") as f:
        ident = _str(f["identifier"])
        meta = {
            "path": asset["path"], "identifier": ident,
            "subject_id": _str(f["general/subject/subject_id"]),
            "age": _str(f["general/subject/age"]),
            "session_description": _str(f["session_description"]),
            "session_start": _str(f["session_start_time"]),
            "units_colnames": list(map(_str, f["units"].attrs["colnames"])),
            "trials_colnames": list(map(_str, f["intervals/trials"].attrs["colnames"])),
            "acquisition": list(f["acquisition"].keys()), "processing": list(f["processing"].keys()),
        }
        tr = f["intervals/trials/start_time"][:]
        stop = f["intervals/trials/stop_time"][:]
        st_all = f["units/spike_times"][:]
        idx = f["units/spike_times_index"][:]
        lab = f["units/celltype_label"][:] if "celltype_label" in f["units"] else np.full(len(idx), np.nan)
        ids = f["units/id"][:]
    meta.update(parse_identifier(ident))
    starts = np.r_[0, idx[:-1]].astype(int)
    n_u, n_t = len(idx), len(tr)
    counts = np.zeros((n_u, n_t, len(WINDOWS)), np.int32)
    psth = np.zeros((n_u, len(EDGES) - 1))
    psth5 = np.zeros((n_u, len(FINE_EDGES) - 1), np.float32)
    base_bins = np.zeros((n_u, n_t), np.int32)
    n_spikes, sorted_ok = np.zeros(n_u, int), True
    for u, (s, e) in enumerate(zip(starts, idx.astype(int))):
        st = st_all[s:e]
        if np.any(np.diff(st) < 0):
            sorted_ok = False
            st = np.sort(st)
        n_spikes[u] = len(st)
        for k, (lo, hi) in enumerate(WINDOWS.values()):
            counts[u, :, k] = _counts(st, tr, lo, hi)
        i0 = np.searchsorted(st, tr - PRE)
        i1 = np.searchsorted(st, tr + POST)
        rel = np.concatenate([st[a:b] - t for a, b, t in zip(i0, i1, tr)]) if n_t else np.array([])
        psth[u] = np.histogram(rel, EDGES)[0] / n_t
        psth5[u] = np.histogram(rel, FINE_EDGES)[0] / n_t / FINE
        base_bins[u] = counts[u, :, 0]
    meta.update({
        "n_units": n_u, "n_trials": n_t, "trial_times": tr, "trial_len": stop - tr,
        "spike_range": (float(st_all.min()), float(st_all.max())) if len(st_all) else (np.nan, np.nan),
        "spikes_sorted": sorted_ok, "unit_ids": ids, "label": lab, "n_spikes": n_spikes,
        "counts": counts, "psth": psth, "psth5": psth5,
        "first_spikes": st_all[:5000].copy(),
    })
    return meta


def load_all(assets: list[dict], threads: int = 12) -> list[dict]:
    with ThreadPoolExecutor(threads) as ex:
        return list(ex.map(load_session, assets))


def window_index(name: str) -> int:
    return list(WINDOWS).index(name)


def unit_table(sessions: list[dict]) -> pd.DataFrame:
    """One row per unit: condition, cell type, baseline rate and normalized responses (% of baseline).

    The response is the window's mean rate over trials divided by the baseline's mean rate, times
    100 (the ratio in percent; claims file header).
    """
    rows = []
    for s in sessions:
        c = s["counts"].sum(axis=1)          # units x windows, summed over trials
        n_t = s["n_trials"]
        dur = {k: hi - lo for k, (lo, hi) in WINDOWS.items()}
        rate = {k: c[:, i] / (n_t * dur[k]) for i, k in enumerate(WINDOWS)}
        for u in range(s["n_units"]):
            lab = s["label"][u]
            r = {"session": s["identifier"], "path": s["path"], "rat": s["rat"],
                 "subject_id": s["subject_id"], "state": s["state"], "prf": s["prf"], "tbd": s["tbd"],
                 "dc": s["dc"], "repeat": s["repeat"], "unit": u,
                 "celltype": {1.0: "RSU", 2.0: "FSU"}.get(lab, None) if not np.isnan(lab) else None,
                 "n_trials": n_t, "n_spikes": int(s["n_spikes"][u]), "base_hz": rate["base"][u]}
            for k in WINDOWS:
                if k in ("base", "shift_base"):
                    continue
                b = rate["shift_base"][u] if k.startswith("shift") else rate["base"][u]
                r[k] = 100 * rate[k][u] / b if b > 0 else np.nan
            rows.append(r)
    return pd.DataFrame(rows)


def delayed_window(state: str, w: str) -> str:
    """Column of the delayed response for a state and window reading (W1 or W2)."""
    if state == "awake":
        return "del_awake"
    return "del_anes_w1" if w == "W1" else "del_anes_w2"


def group_test(groups: dict, alpha: float = 0.05) -> tuple[dict, pd.DataFrame]:
    """Kruskal-Wallis over the groups, then two-sided rank-sum tests between every pair,
    Bonferroni-corrected over all pairs (Methods 2.6; claims file header)."""
    names = [g for g in groups if len(groups[g]) > 0]
    vals = [np.asarray(groups[g], float) for g in names]
    kw = stats.kruskal(*vals) if len(vals) > 1 else None
    pairs = list(itertools.combinations(names, 2))
    rows = []
    for a, b in pairs:
        x, y = np.asarray(groups[a], float), np.asarray(groups[b], float)
        p = stats.ranksums(x, y).pvalue
        rows.append({"a": a, "b": b, "n_a": len(x), "n_b": len(y), "mean_a": x.mean(), "mean_b": y.mean(),
                     "median_a": np.median(x), "median_b": np.median(y), "p": p,
                     "p_bonf": min(1.0, p * len(pairs))})
    post = pd.DataFrame(rows)
    if len(post):
        post["sig"] = post.p_bonf < alpha
    out = {"H": kw.statistic if kw else np.nan, "p": kw.pvalue if kw else np.nan,
           "n": {g: len(v) for g, v in zip(names, vals)},
           "mean": {g: float(np.mean(v)) for g, v in zip(names, vals)},
           "median": {g: float(np.median(v)) for g, v in zip(names, vals)}}
    return out, post


def pair(post: pd.DataFrame, a, b) -> pd.Series:
    """The post hoc row for groups a and b, oriented so that mean_a is a's mean."""
    r = post[((post.a == a) & (post.b == b)) | ((post.a == b) & (post.b == a))].iloc[0].copy()
    if r.a != a:
        r["a"], r["b"] = a, b
        r["mean_a"], r["mean_b"] = r["mean_b"], r["mean_a"]
        r["median_a"], r["median_b"] = r["median_b"], r["median_a"]
        r["n_a"], r["n_b"] = r["n_b"], r["n_a"]
    return r


def latency(psth: np.ndarray, base_counts: np.ndarray, sem: str, first: str, timing: str) -> float:
    """Delayed-response onset of one unit (s), or nan when it has no significant delayed response.

    psth: trial-averaged spikes per 1/28 s bin over -0.5 to 1.5 s (56 bins).
    base_counts: spikes in the 0.5 s baseline of each trial.
    sem: S1, SEM over the 14 baseline bins of the trial-averaged PSTH; S2, SEM over trials of the
    per-trial baseline in spikes per bin. first: D1, bins starting at or after 67 ms; D2, bins
    ending after 67 ms. timing: L1, a bin's start; L2, its centre.
    """
    base = psth[:N_BASE_BINS]
    mu = base.mean()
    if sem == "S1":
        se = base.std(ddof=1) / np.sqrt(len(base))
    else:
        per_bin = base_counts / N_BASE_BINS
        se = per_bin.std(ddof=1) / np.sqrt(len(per_bin))
    post = psth[N_BASE_BINS:]
    starts = EDGES[N_BASE_BINS:-1]
    ends = EDGES[N_BASE_BINS + 1:]
    allowed = starts >= US_DURATION - 1e-12 if first == "D1" else ends > US_DURATION
    above = (post >= mu + se) & allowed
    run = 0
    for k, a in enumerate(above):
        run = run + 1 if a else 0
        if run == 3:
            j = k - 2
            return float(starts[j] if timing == "L1" else starts[j] + BIN / 2)
    return np.nan


def find_duplicates(sessions: list[dict]) -> pd.DataFrame:
    """Recordings deposited more than once: files with identical trial times.

    For each group, the copy kept is the one with cell-type labels, then a non-repeat identifier,
    then the first path. Returns one row per file with `kept` and `duplicate_of`.
    """
    key = {}
    for s in sessions:
        key.setdefault(s["trial_times"].tobytes(), []).append(s)
    rows = []
    for grp in key.values():
        order = sorted(grp, key=lambda s: (np.all(np.isnan(s["label"])), s["repeat"], s["path"]))
        keep = order[0]
        for s in grp:
            rows.append({"path": s["path"], "identifier": s["identifier"], "subject_id": s["subject_id"],
                         "kept": s is keep, "duplicate_of": None if s is keep else keep["path"],
                         "group_size": len(grp)})
    return pd.DataFrame(rows)
