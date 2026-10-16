"""Loading and measures for the hippocampus and amygdala recordings of dandiset 000061.

Girardeau, Inema & Buzsaki (2017), Nature Neuroscience, doi:10.1038/nn.4637.

Each NWB file is one day of one rat: sorted units with a brain-region label, sleep states
(Awake, Non-REM, REM), an epochs table (pre-run, pre-sleep, run, post-sleep, post-run), and
annotation series for hippocampal ripples (`rip`: start, peak and stop of each ripple), air
puffs (`puf`) and rewards at the left and right ends of the track (`lrw`, `rrw`). Some files
also hold raw voltage, LFP and video, which are not read here. Files are streamed from the
archive at the pinned version; nothing is written to disk.

Where the parameters come from: the paper's full text is not open access, so its Methods were
not available, and neither the paper's abstract nor the dandiset links analysis code. Every
parameter below is a common choice made here, fixed in the claims file before the analysis:

- `EPOCH_TIME_SCALE`: the epochs table is stored in milliseconds although its column says
  seconds; the data check shows this (its last stop time is 1000 times the last spike time).
- Region labels: `HPC_LABELS` and `BLA_LABELS` (case is ignored). `BLA_COMPLEX_LABELS` adds the
  undescribed labels that look like basolateral subdivisions (blv, bmp, ladl), for a variant.
- `BIN_S` (50 ms), `MIN_RATE_HZ` (0.1 Hz in the run epoch), `MIN_UNITS` (5 per region),
  `N_SURROGATES` (200 circular shifts) and `SIGNIFICANCE_PERCENTILE` (95) for the joint
  patterns, which are the singular vectors of the hippocampus by BLA cross-correlation matrix of
  the run.
- Ripple modulation: `RIPPLE_SHIFTS` (500 shifts of 0.5 to 5 s), `RIPPLE_ALPHA` (0.01, one
  sided), `CHANCE_SHIFT_S` (7 s), at `RIPPLE_RES_S` (5 ms) resolution.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
from dandi.dandiapi import DandiAPIClient

DANDISET_ID = "000061"
DANDISET_VERSION = "0.250624.0426"

EPOCH_TIME_SCALE = 1e-3
HPC_LABELS = {"hpc", "hip"}
BLA_LABELS = {"bla"}
BLA_COMPLEX_LABELS = {"bla", "blv", "bmp", "ladl"}
KEEP_LABELS = HPC_LABELS | BLA_COMPLEX_LABELS

BIN_S = 0.05
MIN_RATE_HZ = 0.1
MIN_UNITS = 5
N_SURROGATES = 200
SIGNIFICANCE_PERCENTILE = 95.0

RIPPLE_SHIFTS = 500
RIPPLE_SHIFT_RANGE_S = (0.5, 5.0)
RIPPLE_ALPHA = 0.01
CHANCE_SHIFT_S = 7.0
RIPPLE_RES_S = 0.005

MIXED_UNITS_NOTE = (
    "In some files the spike times of unit 1 fall back once, after 65536 times k spikes, and "
    "unit 0 stops part way through the session where unit 1 starts: the first part of unit 1 "
    "is the end of unit 0. Units 0 and 1 of those files are left out.")


def asset_urls() -> list[tuple[str, str]]:
    """(path, streaming URL) of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in dandiset.get_assets() if a.path.endswith(".nwb"))


def _text(value) -> str:
    value = value[()]
    if isinstance(value, np.ndarray):
        value = value[0]
    return value.decode() if isinstance(value, bytes) else str(value)


def _strings(dataset) -> np.ndarray:
    return np.array([v.decode() if isinstance(v, bytes) else str(v) for v in dataset[()]])


def load_session(path: str, url: str) -> dict:
    """One file: metadata, tables and events, and the spike trains of hippocampal and BLA units.

    Units of other regions keep only their spike count and first spike time (for the check of
    duplicated recordings). Epoch times are converted to seconds with `EPOCH_TIME_SCALE`.
    """
    for attempt in range(3):
        try:
            f = h5py.File(remfile.File(url), "r")
            break
        except OSError:
            if attempt == 2:
                raise
    with f:
        s = {"path": path, "session": path.split("ses-")[1].split("_")[0],
             "rat": _text(f["general/subject/subject_id"]),
             "species": _text(f["general/subject/species"]),
             "age": _text(f["general/subject/age"]), "sex": _text(f["general/subject/sex"]),
             "session_start": _text(f["session_start_time"])}
        ep = f["intervals/epochs"]
        s["epoch_columns"] = list(ep.attrs["colnames"])
        s["epoch_unit_stated"] = ep["start_time"].attrs.get("description")
        s["epochs_raw"] = list(zip(_strings(ep["tags"]), ep["start_time"][()], ep["stop_time"][()]))
        s["epochs"] = [(t, a * EPOCH_TIME_SCALE, b * EPOCH_TIME_SCALE) for t, a, b in s["epochs_raw"]]
        if "processing/behavior/states" in f:
            st = f["processing/behavior/states"]
            s["states"] = list(zip(_strings(st["label"]), st["start_time"][()].astype(float),
                                   st["stop_time"][()].astype(float)))
        else:
            s["states"] = None
        s["trials"] = None
        if "intervals/trials" in f:
            tr = f["intervals/trials"]
            s["trials"] = (tr["start_time"][()], tr["stop_time"][()], tr.attrs.get("description"))
        events = {}
        for name in (f["stimulus/presentation"] if "stimulus/presentation" in f else []):
            g = f[f"stimulus/presentation/{name}"]
            events[name] = (_strings(g["data"]), g["timestamps"][()], g.attrs.get("description"))
        s["events"] = events
        s["ripples"] = parse_ripples(*events["rip"][:2]) if "rip" in events else None
        lfp = "processing/ecephys/LFP/LFP"
        s["lfp"] = None
        if lfp in f:
            s["lfp"] = (f[f"{lfp}/data"].shape, float(f[f"{lfp}/starting_time"].attrs["rate"]),
                        f[f"{lfp}/data"].attrs.get("unit"))
        s["raw"] = f["acquisition/ElectricalSeries/data"].shape if "acquisition/ElectricalSeries" in f else None
        s["videos"] = {k: (f[f"acquisition/{k}/data"].shape[0], *f[f"acquisition/{k}/timestamps"][[0, -1]],
                           f[f"acquisition/{k}/timestamps"].attrs.get("unit"))
                       for k in f["acquisition"] if k.startswith("Video")}
        s["electrode_locations"] = sorted(set(_strings(f["general/extracellular_ephys/electrodes/location"])))
        s["units"] = None
        if "units" in f:
            u = f["units"]
            loc = _strings(u["location"]) if "location" in u else np.array(["(none)"] * len(u["id"]))
            index = u["spike_times_index"][()]
            spikes = u["spike_times"][()]
            trains = np.split(spikes, index[:-1])
            unsorted = [i for i, t in enumerate(trains) if np.any(np.diff(t) < 0)]
            # A unit whose times fall back once holds the end of the unit before it (see
            # `MIXED_UNITS_NOTE`); both are left out.
            mixed = sorted({j for i in unsorted for j in (i - 1, i) if j >= 0})
            s["units"] = {
                "label": loc, "region": np.char.lower(loc), "shank": u["shank_id"][()],
                "group": np.array([f[r].name.split("/")[-1] for r in u["electrode_group"][()]]),
                "n_spikes": np.diff(np.concatenate([[0], index])),
                "first_spike": np.array([t[0] if len(t) else np.nan for t in trains]),
                "sorted": not unsorted, "unsorted": unsorted, "mixed": mixed,
                "unsorted_at": {i: np.flatnonzero(np.diff(trains[i]) < 0).tolist() for i in unsorted},
                "unit0_last": float(trains[0][-1]) if len(trains) and len(trains[0]) else np.nan,
                "unit1_first": float(trains[1][0]) if len(trains) > 1 and len(trains[1]) else np.nan,
                "trains": {i: t for i, t in enumerate(trains)
                           if loc[i].lower() in KEEP_LABELS and i not in mixed},
                "last_spike": float(spikes.max()) if len(spikes) else np.nan,
                "has_location_column": "location" in u,
            }
    return s


def load_all(workers: int = 12) -> list[dict]:
    """Every file of the dandiset, loaded in parallel."""
    urls = asset_urls()
    with ThreadPoolExecutor(workers) as pool:
        return list(pool.map(lambda pu: load_session(*pu), urls))


def parse_ripples(labels: np.ndarray, times: np.ndarray) -> dict:
    """The `rip` annotations as arrays of start, peak and stop, with the channel in each label.

    The labels come in triplets "Ripple start N", "Ripple peak N", "Ripple stop N"; `ordered`
    says whether every triplet is in that order with increasing times.
    """
    kind = np.array([lab.split()[1] for lab in labels])
    channel = np.array([lab.split()[2] if len(lab.split()) > 2 else "" for lab in labels])
    n = len(labels) // 3
    k = kind[:3 * n].reshape(n, 3)
    t = times[:3 * n].reshape(n, 3)
    ordered = bool(len(labels) % 3 == 0 and np.all(k == ["start", "peak", "stop"])
                   and np.all(np.diff(t, axis=1) >= 0))
    return {"start": t[:, 0], "peak": t[:, 1], "stop": t[:, 2], "ordered": ordered,
            "channels": sorted(set(channel))}


# --- intervals -------------------------------------------------------------------------------

def intervals_of(session: dict, label: str) -> np.ndarray:
    """(n, 2) state intervals with the given label, in seconds."""
    if session["states"] is None:
        return np.zeros((0, 2))
    return np.array([(a, b) for lab, a, b in session["states"] if lab == label]).reshape(-1, 2)


def sleep_epochs(session: dict) -> tuple[np.ndarray, np.ndarray, tuple[float, float] | None]:
    """Pre-sleep intervals, post-sleep intervals and the (first) run epoch, in seconds.

    Tags presleep and postsleep are used where present. Files that tag sleep only as "sleep"
    take the sleep epochs before and after the first run.
    """
    eps = session["epochs"]
    runs = [(a, b) for t, a, b in eps if t == "run"]
    run = runs[0] if runs else None
    pre = [(a, b) for t, a, b in eps if t == "presleep"]
    post = [(a, b) for t, a, b in eps if t == "postsleep"]
    if not pre and not post and run is not None:
        pre = [(a, b) for t, a, b in eps if t == "sleep" and b <= run[0]]
        post = [(a, b) for t, a, b in eps if t == "sleep" and a >= run[1]]
    return np.array(pre).reshape(-1, 2), np.array(post).reshape(-1, 2), run


def intersect(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Intersection of two sets of (start, stop) intervals."""
    out = []
    for s1, e1 in a:
        for s2, e2 in b:
            s, e = max(s1, s2), min(e1, e2)
            if e > s:
                out.append((s, e))
    return np.array(sorted(out)).reshape(-1, 2)


def in_intervals(t: np.ndarray, iv: np.ndarray) -> np.ndarray:
    """Whether each time lies in one of the sorted, non-overlapping intervals."""
    if len(iv) == 0:
        return np.zeros(len(t), bool)
    i = np.searchsorted(iv[:, 0], t, side="right") - 1
    ok = i >= 0
    out = np.zeros(len(t), bool)
    out[ok] = t[ok] < iv[i[ok], 1]
    return out


def laps(session: dict) -> list[tuple[float, float, str]]:
    """Laps from a reward at one end of the track to the next reward at the other end.

    Direction "LR" runs from the left reward to the right one. Consecutive rewards at the same
    end do not make a lap.
    """
    ev = sorted([(t, "L") for t in session["events"]["lrw"][1]] +
                [(t, "R") for t in session["events"]["rrw"][1]])
    return [(a, b, sa + sb) for (a, sa), (b, sb) in zip(ev[:-1], ev[1:]) if sa != sb]


def run_laps(session: dict) -> list[tuple[float, float, str]]:
    """Laps clipped to the run epoch.

    A lap that starts before the run (the last reward of the pre-run) and ends inside it keeps
    its direction for the part inside the run, so the time before the first reward of the run
    counts as a lap toward that reward.
    """
    _, _, run = sleep_epochs(session)
    if run is None:
        return []
    out = []
    for a, b, d in laps(session):
        a, b = max(a, run[0]), min(b, run[1])
        if b > a:
            out.append((a, b, d))
    return out


def puff_direction(session: dict) -> tuple[str | None, dict]:
    """The lap direction in the run epoch that holds most air puffs, and the counts."""
    _, _, run = sleep_epochs(session)
    counts = {"LR": 0, "RL": 0, "none": 0}
    if "puf" not in session["events"] or run is None:
        return None, counts
    run_laps_ = run_laps(session)
    for t in session["events"]["puf"][1]:
        d = [lap[2] for lap in run_laps_ if lap[0] <= t < lap[1]]
        counts[d[0] if d else "none"] += 1
    if counts["LR"] == counts["RL"]:
        return None, counts
    return ("LR" if counts["LR"] > counts["RL"] else "RL"), counts


# --- binning and patterns --------------------------------------------------------------------

def unit_sets(session: dict, bla_labels=BLA_LABELS) -> tuple[list[int], list[int]]:
    """Hippocampal and BLA units that fire at `MIN_RATE_HZ` or more in the run epoch."""
    _, _, run = sleep_epochs(session)
    u = session["units"]
    if u is None or run is None:
        return [], []
    dur = run[1] - run[0]

    def ok(i):
        t = u["trains"][i]
        return np.count_nonzero((t >= run[0]) & (t < run[1])) / dur >= MIN_RATE_HZ
    hpc = [i for i in u["trains"] if u["region"][i] in HPC_LABELS and ok(i)]
    bla = [i for i in u["trains"] if u["region"][i] in bla_labels and ok(i)]
    return hpc, bla


def grid_size(session: dict, bin_s: float) -> int:
    """Number of bins of width bin_s from 0 to the end of the last epoch."""
    return int(np.ceil(max(b for _, _, b in session["epochs"]) / bin_s)) + 1


def binned(session: dict, units: list[int], bin_s: float, rows: np.ndarray) -> np.ndarray:
    """(len(rows), n_units) spike counts in the bins `rows` of the grid of width bin_s."""
    n = grid_size(session, bin_s)
    out = np.zeros((len(rows), len(units)), np.float32)
    for j, i in enumerate(units):
        idx = (session["units"]["trains"][i] / bin_s).astype(np.int64)
        out[:, j] = np.bincount(idx[(idx >= 0) & (idx < n)], minlength=n)[rows]
    return out


def zscore(x: np.ndarray) -> np.ndarray:
    """Z-score each column; a column without variance becomes zero."""
    sd = x.std(0)
    return np.where(sd > 0, (x - x.mean(0)) / np.where(sd > 0, sd, 1), 0).astype(np.float32)


def joint_patterns(zh: np.ndarray, zb: np.ndarray, rng: np.random.Generator,
                   n_surrogates: int = N_SURROGATES) -> dict:
    """Singular vectors of the hippocampus by BLA cross-correlation matrix, and their threshold.

    zh and zb are z-scored counts of the template bins. The threshold is the
    `SIGNIFICANCE_PERCENTILE` percentile of the largest singular value over surrogates in which
    each BLA column is circularly shifted by its own random offset.
    """
    T = len(zh)
    c = zh.T @ zb / T
    u, sv, vt = np.linalg.svd(c, full_matrices=False)
    null = np.empty(n_surrogates)
    for k in range(n_surrogates):
        zs = np.empty_like(zb)
        for j, shift in enumerate(rng.integers(1, T, zb.shape[1])):
            zs[:, j] = np.roll(zb[:, j], shift)
        null[k] = np.linalg.svd(zh.T @ zs / T, compute_uv=False)[0]
    threshold = float(np.percentile(null, SIGNIFICANCE_PERCENTILE))
    return {"u": u, "s": sv, "v": vt.T, "threshold": threshold, "significant": sv > threshold,
            "n_bins": T}


def strength(zh: np.ndarray, zb: np.ndarray, u: np.ndarray, v: np.ndarray) -> np.ndarray:
    """Reactivation strength (zh . u)(zb . v) per bin, one column per pattern."""
    return (zh @ u) * (zb @ v)


def ripple_modulation(train: np.ndarray, windows: list[tuple[np.ndarray, np.ndarray]], end_s: float,
                      rng: np.random.Generator) -> list[dict]:
    """A unit's spikes in sets of ripple windows, each against the same windows shifted at random.

    For each (start, stop) set: the observed count, the mean surrogate count, and one-sided p
    values for an increase and a decrease (the fraction of `RIPPLE_SHIFTS` surrogates at or
    above, or at or below, the observed count, counting the observed one). All windows of a set
    are shifted together by one offset of `RIPPLE_SHIFT_RANGE_S`, either sign. Times are handled
    on a `RIPPLE_RES_S` grid.
    """
    n = int(np.ceil(end_s / RIPPLE_RES_S)) + 2
    idx = (train / RIPPLE_RES_S).astype(np.int64)
    cs = np.concatenate([[0], np.cumsum(np.bincount(idx[(idx >= 0) & (idx < n)], minlength=n))])
    lo, hi = (int(x / RIPPLE_RES_S) for x in RIPPLE_SHIFT_RANGE_S)
    out = []
    for start, stop in windows:
        a = (start / RIPPLE_RES_S).astype(np.int64)
        b = (stop / RIPPLE_RES_S).astype(np.int64) + 1
        observed = int((cs[np.clip(b, 0, n)] - cs[np.clip(a, 0, n)]).sum())
        offsets = rng.integers(lo, hi + 1, RIPPLE_SHIFTS) * rng.choice([-1, 1], RIPPLE_SHIFTS)
        null = (cs[np.clip(b[None, :] + offsets[:, None], 0, n)]
                - cs[np.clip(a[None, :] + offsets[:, None], 0, n)]).sum(1)
        out.append({"observed": observed, "null_mean": float(null.mean()),
                    "p_up": (1 + np.count_nonzero(null >= observed)) / (1 + RIPPLE_SHIFTS),
                    "p_down": (1 + np.count_nonzero(null <= observed)) / (1 + RIPPLE_SHIFTS)})
    return out


def usable(session: dict, bla_labels=BLA_LABELS) -> bool:
    """Whether a session meets the claims file's rule for the reactivation analysis."""
    pre, post, run = sleep_epochs(session)
    if session["states"] is None or session["ripples"] is None or run is None:
        return False
    if len(pre) == 0 or len(post) == 0:
        return False
    hpc, bla = unit_sets(session, bla_labels)
    return len(hpc) >= MIN_UNITS and len(bla) >= MIN_UNITS


def ripple_bins(session: dict, bin_s: float) -> np.ndarray:
    """Boolean grid of the bins that overlap a ripple (start to stop)."""
    n = grid_size(session, bin_s)
    r = session["ripples"]
    a = np.clip((r["start"] / bin_s).astype(np.int64), 0, n - 1)
    b = np.clip((r["stop"] / bin_s).astype(np.int64), 0, n - 1)
    d = np.zeros(n + 1, np.int64)
    np.add.at(d, a, 1)
    np.add.at(d, b + 1, -1)
    return np.cumsum(d[:-1]) > 0


def reactivation(session: dict, rng: np.random.Generator, bin_s: float = BIN_S,
                 bla_labels=BLA_LABELS, templates=("run",), equal_bins: bool = False,
                 lags: int = 20, keep_traces: bool = True) -> dict:
    """Joint patterns of the run and their reactivation in pre- and post-sleep Non-REM.

    `templates` names the run bins a template is built from: "run" (the whole run epoch),
    "puff" or "safe" (bins inside laps of the air-puff or the safe direction). With
    `equal_bins` the two directional templates use the same number of bins (the first bins of
    the longer one are kept). Returns one row per pattern, and for significant patterns the
    ripple-peak-triggered mean strength in post-sleep (lags of `lags` bins either side) and the
    mean strength in ripple and non-ripple bins of pre- and post-sleep. The same triggered mean
    in pre-sleep is kept as a reference.
    """
    hpc, bla = unit_sets(session, bla_labels)
    units = hpc + bla
    nh = len(hpc)
    n = grid_size(session, bin_s)
    centers = (np.arange(n) + 0.5) * bin_s
    pre_iv, post_iv, run = sleep_epochs(session)
    nrem = intervals_of(session, "Non-REM")
    pre_rows = np.flatnonzero(in_intervals(centers, intersect(nrem, pre_iv)))
    post_rows = np.flatnonzero(in_intervals(centers, intersect(nrem, post_iv)))
    rip = ripple_bins(session, bin_s)

    in_run = (centers >= run[0]) & (centers < run[1])
    direction, _ = puff_direction(session)
    template_rows = {"run": np.flatnonzero(in_run)}
    if direction is not None:
        lap_iv = {d: np.array([(a, b) for a, b, dd in run_laps(session) if dd == d]).reshape(-1, 2)
                  for d in ("LR", "RL")}
        safe = "RL" if direction == "LR" else "LR"
        template_rows["puff"] = np.flatnonzero(in_run & in_intervals(centers, lap_iv[direction]))
        template_rows["safe"] = np.flatnonzero(in_run & in_intervals(centers, lap_iv[safe]))
        if equal_bins:
            m = min(len(template_rows["puff"]), len(template_rows["safe"]))
            template_rows["puff"], template_rows["safe"] = template_rows["puff"][:m], template_rows["safe"][:m]

    def z(rows):
        c = binned(session, units, bin_s, rows)
        return zscore(c[:, :nh]), zscore(c[:, nh:])
    zpre, zpost = z(pre_rows), z(post_rows)

    peaks = session["ripples"]["peak"]
    post_peak_bins = (peaks[in_intervals(peaks, intersect(nrem, post_iv))] / bin_s).astype(np.int64)
    pre_peak_bins = (peaks[in_intervals(peaks, intersect(nrem, pre_iv))] / bin_s).astype(np.int64)

    rows, traces = [], []
    for name in templates:
        if name not in template_rows or len(template_rows[name]) < 100:
            continue
        zh, zb = z(template_rows[name])
        p = joint_patterns(zh, zb, rng)
        r_pre = strength(*zpre, p["u"], p["v"])
        r_post = strength(*zpost, p["u"], p["v"])
        for k in range(len(p["s"])):
            rows.append({"session": session["session"], "rat": session["rat"], "template": name,
                         "pattern": k, "singular": float(p["s"][k]), "threshold": p["threshold"],
                         "significant": bool(p["significant"][k]), "n_template_bins": p["n_bins"],
                         "n_hpc": nh, "n_bla": len(bla),
                         "pre": float(r_pre[:, k].mean()), "post": float(r_post[:, k].mean()),
                         "bla_units": bla, "bla_weights": p["v"][:, k].copy()})
            if keep_traces and p["significant"][k]:
                curves = {}
                for label, rows_, r_, peak_bins in (("post", post_rows, r_post, post_peak_bins),
                                                    ("pre", pre_rows, r_pre, pre_peak_bins)):
                    full = np.full(n, np.nan, np.float32)
                    full[rows_] = r_[:, k]
                    lag_idx = peak_bins[:, None] + np.arange(-lags, lags + 1)[None, :]
                    ok = np.all((lag_idx >= 0) & (lag_idx < n), axis=1)
                    curves[label] = (np.nanmean(full[lag_idx[ok]], axis=0), int(ok.sum()))
                traces.append({"session": session["session"], "rat": session["rat"], "template": name,
                               "pattern": k, "curve": curves["post"][0], "n_ripples": curves["post"][1],
                               "curve_pre": curves["pre"][0], "n_ripples_pre": curves["pre"][1],
                               "pre_rip": float(r_pre[rip[pre_rows], k].mean()),
                               "pre_out": float(r_pre[~rip[pre_rows], k].mean()),
                               "post_rip": float(r_post[rip[post_rows], k].mean()),
                               "post_out": float(r_post[~rip[post_rows], k].mean())})
    return {"rows": rows, "traces": traces, "direction": direction,
            "n_pre_bins": len(pre_rows), "n_post_bins": len(post_rows),
            "template_bins": {k: len(v) for k, v in template_rows.items()}}
