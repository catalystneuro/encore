"""Loading and spiking measures for dandiset 000946 (Gao, Ramachandran, Yu & He 2025).

The dandiset holds one NWB file per recorded area and session: a units table with
spike times and a `celltype_label` column, and a trials table whose `start_time`
is taken as sonication onset (checked in the notebook). The session's parameters
are in `identifier` (`<rat>_<PRF>_<PD>_<UD>_<n>[_suffix]`), `general/notes`
(`Recording:<area>; stim at:<target>`) and `general/data_collection`
(`tFUS parameters {PRF:..Hz PD:..us UD:67ms}`).

Where each parameter comes from:

- `MIN_SPIKES = 2000`: Methods, Neuronal type classification ("Only neurons that
  fire >2,000 spikes for each session were considered"); the claims file header,
  Units.
- `WINDOWS` (67 ms bins from sonication onset, 0 to 268 ms) and the baseline
  [-67, 0) ms: claims file header, Windows, and Statistical analysis ("normalized
  to the pre-stim period (67 ms pre-stim)").
- `normalized_rates`, readings N1 and N2, and the comparison windows B1 and B2:
  claims file header, Normalized spiking rate and Test against baseline.
- `vs_baseline`: one-tailed two-sample Wilcoxon (rank-sum) test against the
  baseline sample with Bonferroni correction over the comparisons in the panel
  (reading C1), significance 0.01: Statistical analysis and the claims file
  header. `kruskal_levels`: Kruskal-Wallis across parameter levels, units as
  observations (claims file header).
- Removing duplicate deposits (`dedupe`): protocol, author step 1.2; a file is a
  duplicate of another when subject, identifier, recorded area and the spike
  count of every unit are the same. The notebook checks that the spike times of
  such pairs are identical.
- `N_PROC` (processes used to stream files) and the shift used for the clock
  check are standard choices that cannot change a result.
"""
import json
import re
import h5py
import numpy as np
import remfile
import requests
from scipy import stats

DANDISET_ID = "000946"
VERSION = "0.250829.1249"
API = "https://api.dandiarchive.org/api"
MIN_SPIKES = 2000
BASELINE = (-0.067, 0.0)
PRE_BASELINE = (-0.134, -0.067)
WINDOWS = {
    "0-67": (0.0, 0.067),
    "67-134": (0.067, 0.134),
    "134-201": (0.134, 0.201),
    "201-268": (0.201, 0.268),
}
N_PROC = 24


def list_assets(version=VERSION):
    """All assets of the pinned version: path, asset id and size."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=1000"
    out = []
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        js = r.json()
        out += [dict(path=a["path"], asset_id=a["asset_id"], size=a["size"]) for a in js["results"]]
        url = js["next"]
    return out


def version_info(version=VERSION):
    r = requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{version}/info/", timeout=60)
    r.raise_for_status()
    return r.json()


def asset_url(asset_id):
    return f"{API}/assets/{asset_id}/download/"


def _open(asset_id):
    return h5py.File(remfile.File(asset_url(asset_id)), "r")


def _s(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def parse_identifier(identifier):
    """PRF (Hz) and PD (us) from the identifier `<rat>_<PRF>_<PD>_<UD>_...`."""
    parts = identifier.split("_")
    try:
        return float(parts[1]), float(parts[2].replace("point", "."))
    except (IndexError, ValueError):
        return np.nan, np.nan


def parse_header(identifier, notes, data_collection):
    """Area, target, PRF (Hz) and PD (us) from the file's text fields (PRF and PD from data_collection;
    the notebook compares them with the identifier and falls back on it where data_collection is empty)."""
    m = re.search(r"(?i)recording:\s*([A-Za-z0-9_]*)", notes or "")
    area = m.group(1).upper() if m else ""
    m = re.search(r"(?i)(?:stim at|stimulation):\s*([A-Za-z0-9_]*)", notes or "")
    stim = m.group(1).upper() if m else ""
    m = re.search(r"PRF:(\w+)Hz", data_collection or "")
    prf = float(m.group(1)) if m else np.nan
    m = re.search(r"PD:(\w+)us", data_collection or "")
    pd_us = float(m.group(1).replace("point", ".")) if m else np.nan
    return area, stim, prf, pd_us


def read_header(asset):
    """Metadata, trial count and per-unit spike counts of one file (no spike times)."""
    try:
        f = _open(asset["asset_id"])
        r = dict(asset)
        r["identifier"] = _s(f["identifier"][()])
        r["notes"] = _s(f["general/notes"][()]) if "general/notes" in f else ""
        r["data_collection"] = _s(f["general/data_collection"][()]) if "general/data_collection" in f else ""
        r["subject_id"] = _s(f["general/subject/subject_id"][()])
        ts = f["session_start_time"]
        r["session_start"] = _s(ts[0] if ts.shape else ts[()])
        r["n_trials"] = len(f["intervals/trials/start_time"])
        u = f["units"]
        r["unit_columns"] = ",".join(_s(c) for c in u.attrs["colnames"])
        r["groups"] = ",".join(k for k in ("acquisition", "analysis", "processing") if len(f[k]))
        if "spike_times_index" in u:
            idx = u["spike_times_index"][:]
            r["n_spikes"] = json.dumps(np.diff(np.r_[0, idx]).astype(int).tolist())
            r["n_units"] = len(idx)
            if "celltype_label" in u:
                lab = u["celltype_label"][:]
                r["labels"] = json.dumps(sorted(set(np.asarray(lab).ravel().tolist())))
            else:
                r["labels"] = "absent"
        else:
            r["n_spikes"], r["n_units"], r["labels"] = "[]", 0, "absent"
        r["area"], r["stim"], r["prf_dc"], r["pd_dc"] = parse_header(r["identifier"], r["notes"], r["data_collection"])
        r["prf_id"], r["pd_id"] = parse_identifier(r["identifier"])
        r["prf"] = r["prf_dc"] if np.isfinite(r["prf_dc"]) else r["prf_id"]
        r["pd_us"] = r["pd_dc"] if np.isfinite(r["pd_dc"]) else r["pd_id"]
        r["error"] = ""
        return r
    except Exception as e:  # recorded and reported in the notebook
        r = dict(asset)
        r["error"] = repr(e)
        return r


def inventory(assets, processes=N_PROC):
    """read_header over many files, in parallel processes (h5py serialises threads)."""
    import pandas as pd
    rows = map_sessions(read_header, assets, processes)
    return pd.DataFrame(rows)


def dedupe(inv):
    """Keep one file of each group with the same subject, identifier, area and per-unit spike counts.

    Returns the kept table and a table of the duplicate pairs (kept path, dropped path).
    """
    inv = inv.sort_values("path").copy()
    key = ["subject_id", "identifier", "area", "n_spikes"]
    inv["dup_of"] = None
    first = {}
    for i, r in inv.iterrows():
        k = tuple(r[c] for c in key)
        if k in first:
            inv.at[i, "dup_of"] = first[k]
        else:
            first[k] = r["path"]
    kept = inv[inv.dup_of.isna()].copy()
    dropped = inv[inv.dup_of.notna()][["dup_of", "path"]].rename(columns={"dup_of": "kept", "path": "dropped"})
    return kept, dropped


def load_session(asset_id):
    """Trial start times and the spike times of every unit of one file."""
    f = _open(asset_id)
    st = f["intervals/trials/start_time"][:]
    sp = f["intervals/trials/stop_time"][:]
    idx = f["units/spike_times_index"][:]
    times = f["units/spike_times"][:]
    units = np.split(times, idx[:-1].astype(int))
    return dict(start=st, stop=sp, units=units)


def spike_hash(asset_id):
    """A digest of all spike times and trial starts, to compare duplicate deposits."""
    import hashlib
    s = load_session(asset_id)
    h = hashlib.sha256()
    for u in s["units"]:
        h.update(np.asarray(u, dtype=np.float64).tobytes())
    h.update(np.asarray(s["start"], dtype=np.float64).tobytes())
    return h.hexdigest()


def window_counts(spikes, onsets, win):
    """Spike count of one unit in [onset + win[0], onset + win[1]) for every onset."""
    spikes = np.sort(spikes)
    a = np.searchsorted(spikes, onsets + win[0], side="left")
    b = np.searchsorted(spikes, onsets + win[1], side="left")
    return b - a


def unit_counts(session, onsets=None, windows=None, min_spikes=MIN_SPIKES):
    """Per unit with more than `min_spikes` spikes: counts per trial in baseline, pre-baseline and each window."""
    onsets = session["start"] if onsets is None else onsets
    windows = WINDOWS if windows is None else windows
    out = []
    for k, u in enumerate(session["units"]):
        if len(u) <= min_spikes:
            continue
        c = dict(unit=k, n_spikes=len(u),
                 base=window_counts(u, onsets, BASELINE),
                 pre=window_counts(u, onsets, PRE_BASELINE))
        for w, rng in windows.items():
            c[w] = window_counts(u, onsets, rng)
        out.append(c)
    return out


def normalized_rates(c, window, reading):
    """Normalized rate (percent) of one unit in `window` ("pre" for [-134, -67) ms).

    N1: mean count in the window over trials / mean count in [-67, 0) ms (nan if zero).
    N2: mean over trials with a nonzero baseline of the per-trial ratio.
    """
    x = c[window].astype(float)
    b = c["base"].astype(float)
    if reading == "N1":
        return 100 * x.mean() / b.mean() if b.mean() > 0 else np.nan
    if reading == "N2":
        ok = b > 0
        return 100 * np.mean(x[ok] / b[ok]) if ok.any() else np.nan
    raise ValueError(reading)


def baseline_sample(cs, nreading, breading):
    """The sample a window is compared with: B1, normalized [-67, 0) ms; B2, normalized [-134, -67) ms."""
    w = "base" if breading == "B1" else "pre"
    return np.array([normalized_rates(c, w, nreading) for c in cs])


def vs_baseline(x, base, n_comparisons, alternative="greater"):
    """One-tailed rank-sum of a window's values against the baseline sample, Bonferroni-corrected."""
    x = np.asarray(x, float)
    base = np.asarray(base, float)
    x, base = x[np.isfinite(x)], base[np.isfinite(base)]
    p = stats.mannwhitneyu(x, base, alternative=alternative).pvalue
    return min(1.0, p * n_comparisons), p


def kruskal_levels(groups):
    g = [np.asarray(v, float)[np.isfinite(v)] for v in groups]
    return stats.kruskal(*g).pvalue


PSTH_EDGES = np.round(np.arange(-0.5, 1.0 + 1e-9, 0.01), 3)
CLOCK_SHIFT = 1.0


def session_counts(asset_id):
    """Window counts of every unit (the MIN_SPIKES rule is applied by the caller, so that it can be varied),
    at the trial starts and at the trial starts shifted by CLOCK_SHIFT s (for the clock check), with each
    unit's PSTH (10 ms bins, -0.5 to 1 s, spikes per trial), the trial starts and the number of units."""
    s = load_session(asset_id)
    onsets = s["start"]
    true = unit_counts(s, onsets, min_spikes=0)
    shifted = unit_counts(s, onsets + CLOCK_SHIFT, min_spikes=0)
    psth = []
    for u in s["units"]:
        u = np.sort(u)
        h = np.zeros(len(PSTH_EDGES) - 1)
        for t0 in onsets:
            a, b = np.searchsorted(u, [t0 + PSTH_EDGES[0], t0 + PSTH_EDGES[-1]])
            h += np.histogram(u[a:b] - t0, PSTH_EDGES)[0]
        psth.append(h / len(onsets))
    return dict(true=true, shifted=shifted, psth=psth, start=onsets, n_units=len(s["units"]),
                spikes_per_unit=[len(u) for u in s["units"]])


def map_sessions(func, ids, processes=N_PROC):
    """Map over files in forked processes (h5py serialises threads, so threads do not overlap the reads)."""
    from multiprocessing import get_context
    with get_context("fork").Pool(processes) as p:
        return p.map(func, ids, chunksize=1)
