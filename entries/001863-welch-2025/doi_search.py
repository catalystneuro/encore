"""Loading and measures for the DOI olfactory search sessions of dandiset 001863.

Welch, Gonzales-Hess, Tarvin, Connor & Smear (2025), "The impact of a psychedelic drug on
olfactory search behavior by mice", bioRxiv doi:10.1101/2025.07.09.663970.

Each NWB file holds one session of one mouse: the trial table (start and stop time, odor_control
0 for an odor trial and 3 for an omission trial, side, outcome, the set ITI and, for the 17 mice of
the later cohort, `false_alarm` and `repoke` counts), DeepLabCut tracking of eight keypoints, the
sniff cycles detected from the nasal thermistor (31 sessions) and a series
`task_event_timestamps` (32 sessions). Files are streamed from the archive at the pinned version;
nothing is written to disk.

Where the parameters come from. "Code" is the authors' repository
github.com/Smear-Lab/Olfactory-search-on-psychedelics at commit
aa80af0a153c6bf099e5668d27c9d88e2bfc033f, which the claims file cites.

- `DOI_SESSION` and `SALINE_SESSION`: the claims file's opening comment (the code's list).
- `FEMALES`: the claims file's opening comment and fig1_cleaned.Rmd; the files' own sex field is
  checked against it in the notebook.
- `FIRST_COHORT`: Methods, Figure 1 and Figure 2 ("the first cohort of 5"), and the code's
  `flip_ids`; their x coordinate is flipped as 1200 - x for the maps (fig5_cleaned.Rmd).
- `MIN_TRIALS = 40`: fig1_cleaned.Rmd and fig3_cleaned.Rmd, as the claims file gives it.
- Tracking cleaning: Methods, Figure 3 ("points with likelihood < 0.95 or delta > 8 pixels were
  interpolated", "Any speed that was > 160 cm/s was excluded"), with the code's `CleanTracking`
  (delta from the raw positions, linear interpolation, ends held at the nearest value as
  imputeTS::na_interpolation does).
- `CODE_FPS = 80` and `CM_PER_PX = 0.0237`: fig3_cleaned.Rmd (`speed_aw`, `speed_aw_cm`; frame i,
  counted from 1, at time i / 80 s), as the claims file gives them. The files' own frame rate is
  an estimate made at conversion (frames divided by the last trial's end time) and is not used;
  the notebook checks the 80 frames/s clock against the trial table.
- `OCC_BIN_PX = 48`: the claims file (fig5ab, "48 pixels in fig5_cleaned.Rmd", 1 cm bins).
- `HTR_BIN_PX = 100` and the dropped edge bins (x bin 1200, y bin 700): fig5_cleaned.Rmd.
- `task_event_timestamps` are the head-twitch (HTR) times: the conversion script
  (nwb_conversion/convert_session_to_nwb.py) loads them from the folders "Time Stamps Task" and
  "Time Stamps Task Logan", which fig5_cleaned.Rmd reads as HTR timestamps. The files do not name
  them. For the "Time Stamps Task" files (later cohort) the conversion script read the last field
  of an HH:MM:SS:XX string as hundredths of a second, fig5_cleaned.Rmd reads it as thousandths,
  and the values (0 to 79) look like a frame count at 80 frames/s. `htr_times` returns each
  reading; "code" (thousandths) is the one the paper's numbers were computed with.
- Statistical tests follow R's defaults as the code calls them (`r_signrank`, `r_ranksum`):
  exact when there are fewer than 50 values and no ties, otherwise the normal approximation with
  continuity correction, zero differences dropped.
"""

from __future__ import annotations

import ast
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import stats

DANDISET_ID = "001863"
DANDISET_VERSION = "0.260806.2109"

DOI_SESSION = {2174: 57, 2181: 42, 2182: 32, 2183: 34, 2185: 41, 2191: 25, 2195: 17, 2196: 18,
               2197: 17, 2198: 17, 2200: 14, 2201: 16, 2202: 19, 2203: 13, 2204: 17, 2205: 12,
               2208: 18, 2209: 14, 2210: 17, 2211: 13, 2212: 16, 2213: 14}
SALINE_SESSION = {2174: 56, 2181: 41, 2182: 31, 2183: 33, 2185: 40, 2191: 21, 2195: 20, 2196: 16,
                  2197: 19, 2198: 19, 2200: 19, 2201: 21, 2202: 14, 2203: 18, 2204: 22, 2205: 16,
                  2208: 14, 2209: 18, 2210: 13, 2211: 17, 2212: 13, 2213: 18}
FEMALES = {2174, 2181, 2191, 2200, 2201, 2202, 2203, 2204, 2210, 2211, 2212, 2213}
FIRST_COHORT = {2174, 2181, 2182, 2183, 2185}
FAULTY_SNIFF = {(2198, 17), (2195, 17), (2198, 19), (2213, 18)}   # fig4_cleaned.Rmd

MIN_TRIALS = 40
CODE_FPS = 80.0
CM_PER_PX = 0.0237
LIKELIHOOD_MIN = 0.95
MAX_DELTA_PX = 8.0
MAX_SPEED_CM_S = 160.0
SESSION_S = 2400.0
OCC_BIN_PX = 48
HTR_BIN_PX = 100
HTR_EDGE_X, HTR_EDGE_Y = 1200, 700
FLIP_X = 1200.0


def asset_urls() -> list[tuple[str, str]]:
    """(path, streaming URL) of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in dandiset.get_assets() if a.path.endswith(".nwb"))


def _text(value) -> str:
    value = value[()]
    return value.decode() if isinstance(value, bytes) else str(value)


def load_session(path: str, url: str) -> dict:
    """One session: metadata, trial table, nose track, sniff cycles and event times."""
    with h5py.File(remfile.File(url), "r") as f:
        mouse, session = (int(v) for v in _text(f["general/session_id"]).split("_"))
        tr = f["intervals/trials"]
        cols = [c.decode() if isinstance(c, bytes) else str(c) for c in tr.attrs["colnames"]]
        trials = pd.DataFrame({c: tr[c][:] for c in cols})
        nose = f["processing/behavior/PoseEstimation/nose"]
        s = {
            "path": path, "mouse": mouse, "session": session,
            "drug": _text(f["scratch/drug_condition"]),
            "sex_file": _text(f["general/subject/sex"]),
            "description": _text(f["session_description"]),
            "start": _text(f["session_start_time"]),
            "trials": trials,
            "nose_xy": nose["data"][:],
            "nose_conf": nose["confidence"][:],
            "file_rate": float(nose["starting_time"].attrs["rate"]),
            "pose_unit": nose["data"].attrs.get("unit"),
            "notes": ast.literal_eval(_text(f["general/notes"])),
        }
        if "sniff_cycles" in f["intervals"]:
            sc = f["intervals/sniff_cycles"]
            s["sniff_start"] = sc["start_time"][:]
            s["sniff_stop"] = sc["stop_time"][:]
            s["sniff_description"] = sc.attrs["description"]
        else:
            s["sniff_start"] = None
        if "task_event_timestamps" in f["processing/behavior"]:
            te = f["processing/behavior/task_event_timestamps"]
            s["events"] = te["timestamps"][:]
            s["events_source"] = "logan" if "Logan" in te.attrs["description"] else "task"
            s["events_data"] = np.unique(te["data"][:])
        else:
            s["events"] = None
    s["condition"] = ("DOI" if DOI_SESSION[mouse] == session else
                      "saline" if SALINE_SESSION[mouse] == session else "other")
    s["sex"] = "F" if mouse in FEMALES else "M"
    s["cohort"] = "first" if mouse in FIRST_COHORT else "later"
    return s


def load_all(workers: int = 8) -> list[dict]:
    """Every session of the dandiset, loaded in parallel."""
    urls = asset_urls()
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(lambda pu: load_session(*pu), urls))


# ---------------------------------------------------------------- trials


def odor_mask(trials: pd.DataFrame) -> np.ndarray:
    return trials.odor_control.to_numpy() == 0


def iti_lengths(trials: pd.DataFrame) -> np.ndarray:
    """Next trial's start minus this trial's end (the last trial has none), as the code does."""
    st, en = trials.start_time.to_numpy(), trials.stop_time.to_numpy()
    return np.append(st[1:] - en[:-1], np.nan)


def rolling_accuracy(trials: pd.DataFrame) -> np.ndarray:
    """Percent correct of a trial type's trials up to and including each trial (fig1_cleaned.Rmd)."""
    out = np.full(len(trials), np.nan)
    for kind in (0, 3):
        m = trials.odor_control.to_numpy() == kind
        succ = trials.outcome.to_numpy()[m]
        out[m] = 100 * np.cumsum(succ) / np.arange(1, m.sum() + 1)
    return out


# ---------------------------------------------------------------- tracking


def _interp_nan(v: np.ndarray) -> np.ndarray:
    ok = ~np.isnan(v)
    if ok.sum() == 0:
        return v
    idx = np.arange(len(v))
    return np.interp(idx, idx[ok], v[ok])   # ends held at the nearest value


def clean_nose(s: dict) -> tuple[np.ndarray, np.ndarray, dict]:
    """Nose x, y after the code's CleanTracking (likelihood < 0.95 or delta > 8 px interpolated)."""
    x, y = s["nose_xy"][:, 0].astype(float), s["nose_xy"][:, 1].astype(float)
    delta = np.r_[np.nan, np.hypot(np.diff(x), np.diff(y))]
    low = s["nose_conf"] < LIKELIHOOD_MIN
    jump = delta > MAX_DELTA_PX
    bad = low | jump | np.isnan(x) | np.isnan(y)
    x[bad] = np.nan
    y[bad] = np.nan
    info = {"frames": len(x), "low_likelihood": int(low.sum()), "jump": int(jump.sum()),
            "interpolated": int(bad.sum())}
    return _interp_nan(x), _interp_nan(y), info


def frame_times(n: int, fps: float = CODE_FPS) -> np.ndarray:
    """Frame i (from 1) at i / fps s, as add_trial_label in the code."""
    return np.arange(1, n + 1) / fps


def label_periods(times: np.ndarray, trials: pd.DataFrame) -> np.ndarray:
    """0 for the ITI, 1 within an odor trial, 3 within an omission trial (start <= t <= end).

    A later trial overwrites an earlier one where they overlap, as the code's loop does."""
    lab = np.zeros(len(times), dtype=int)
    for st, en, oc in zip(trials.start_time, trials.stop_time, trials.odor_control):
        i0, i1 = np.searchsorted(times, st, "left"), np.searchsorted(times, en, "right")
        lab[i0:i1] = 3 if oc == 3 else 1
    return lab


def speed_cm_s(x: np.ndarray, y: np.ndarray, fps: float = CODE_FPS) -> np.ndarray:
    """Frame-to-frame nose speed in cm/s; the first frame has none."""
    return np.r_[np.nan, np.hypot(np.diff(x), np.diff(y)) * fps * CM_PER_PX]


# ---------------------------------------------------------------- HTR


def htr_times(s: dict, reading: str = "code") -> np.ndarray | None:
    """HTR times in s under a reading of the timestamp files (see the module docstring).

    "file": as stored (last field of HH:MM:SS:XX as hundredths); "code": as fig5_cleaned.Rmd
    (thousandths); "frames": as frames at 80 per second. The manually scored ("Logan") files were
    stored in seconds and are the same under every reading."""
    t = s["events"]
    if t is None or s["events_source"] == "logan" or reading == "file":
        return t
    whole = np.floor(t + 1e-9)
    xx = np.round((t - whole) * 100)
    return whole + xx / (1000.0 if reading == "code" else CODE_FPS)


# ---------------------------------------------------------------- statistics


def r_signrank(a, b) -> tuple[float, float]:
    """Two-sided paired Wilcoxon signed-rank test as R's wilcox.test(a, b, paired = TRUE).

    Returns (V, p); V is the sum of positive ranks of a - b."""
    d = np.asarray(a, float) - np.asarray(b, float)
    d = d[~np.isnan(d)]
    d = d[d != 0]
    n = len(d)
    if n == 0:
        return np.nan, np.nan
    r = stats.rankdata(np.abs(d))
    v = float(r[d > 0].sum())
    ties = len(np.unique(np.abs(d))) < n
    if n < 50 and not ties:
        p = stats.wilcoxon(d, method="exact").pvalue
    else:
        mu = n * (n + 1) / 4
        _, cnt = np.unique(r, return_counts=True)
        sigma = np.sqrt(n * (n + 1) * (2 * n + 1) / 24 - (cnt ** 3 - cnt).sum() / 48)
        z = v - mu
        z = (z - np.sign(z) * 0.5) / sigma
        p = 2 * min(stats.norm.cdf(z), stats.norm.sf(z))
    return v, float(min(p, 1.0))


def r_ranksum(a, b, exact: bool | None = None) -> tuple[float, float]:
    """Two-sided Wilcoxon rank-sum test as R's wilcox.test(a, b); returns (W, p)."""
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    a, b = a[~np.isnan(a)], b[~np.isnan(b)]
    allv = np.r_[a, b]
    ties = len(np.unique(allv)) < len(allv)
    use_exact = (len(a) < 50 and len(b) < 50 and not ties) if exact is None else exact
    res = stats.mannwhitneyu(a, b, alternative="two-sided",
                             method="exact" if use_exact else "asymptotic", use_continuity=True)
    return float(res.statistic), float(res.pvalue)


def pairwise_ranksum_bonferroni(groups: dict[str, np.ndarray]) -> pd.DataFrame:
    """R pairwise.wilcox.test(..., p.adjust.method = "bonferroni") over every pair of groups."""
    names = list(groups)
    rows = []
    m = len(names) * (len(names) - 1) // 2
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            w, p = r_ranksum(groups[names[i]], groups[names[j]])
            rows.append({"a": names[i], "b": names[j], "W": w, "p": p, "p_bonf": min(1.0, p * m)})
    return pd.DataFrame(rows)


def fisher_pitman(x: np.ndarray, y: np.ndarray, n_resample: int = 10000, seed: int = 0,
                  chunk: int = 50) -> tuple[float, float]:
    """Two-sample Fisher-Pitman permutation test as coin::oneway_test.

    Returns (Z, p): Z is the standardised sum of the first group, p two-sided from `n_resample`
    random permutations (coin's approximate(nresample = 10000))."""
    v = np.r_[x, y].astype(float)
    n1, n = len(x), len(v)
    t_obs = v[:n1].sum()
    mean_t = n1 * v.mean()
    var_t = n1 * (n - n1) / (n * (n - 1)) * ((v - v.mean()) ** 2).sum()
    z = (t_obs - mean_t) / np.sqrt(var_t)
    rng = np.random.default_rng(seed)
    hits = 0
    done = 0
    while done < n_resample:
        k = min(chunk, n_resample - done)
        for _ in range(k):
            t = v[rng.permutation(n)[:n1]].sum()
            hits += abs(t - mean_t) >= abs(t_obs - mean_t) - 1e-9
        done += k
    return float(z), (hits / n_resample if n_resample else float("nan"))


def perm_corr_test(rate: np.ndarray, coord: np.ndarray, n_perm: int = 10000,
                   seed: int = 123) -> tuple[float, float]:
    """Correlation of rate with a bin coordinate, null from permuted coordinates (fig5_cleaned.Rmd).

    Two-sided p as the fraction of permuted |r| at or above the observed |r|. The seed is the
    code's number, though numpy's generator gives other permutations than R's: a choice that
    cannot change the outcome beyond Monte Carlo error."""
    rate = np.asarray(rate, float)
    coord = np.asarray(coord, float)
    r_obs = np.corrcoef(rate, coord)[0, 1]
    rng = np.random.default_rng(seed)
    rc = rate - rate.mean()
    cc = coord - coord.mean()
    denom = np.sqrt((rc ** 2).sum() * (cc ** 2).sum())
    perm = np.array([rc @ rng.permutation(cc) for _ in range(n_perm)]) / denom
    return float(r_obs), float(np.mean(np.abs(perm) >= abs(r_obs) - 1e-12))


# ---------------------------------------------------------------- clocks


def trial_displacement(x: np.ndarray, trials: pd.DataFrame, fps: float, offset: float) -> float:
    """Median of nose x at trial end minus nose x at trial start, frames placed by a clock.

    Frame i (from 1) is taken at trial time i / fps - offset. A trial starts at the initiation
    port and ends when the mouse enters the odor side's quadrant at the far end (Methods, Odor
    navigation task), so with the right clock x moves far toward the odor end over a trial; with
    a wrong one the difference is near 0. x must point toward the odor end (first cohort flipped)."""
    n = len(x)
    i0 = np.clip(np.round((trials.start_time.to_numpy() + offset) * fps).astype(int) - 1, 0, n - 1)
    i1 = np.clip(np.round((trials.stop_time.to_numpy() + offset) * fps).astype(int) - 1, 0, n - 1)
    return float(np.median(x[i1] - x[i0]))


def fit_clock(x: np.ndarray, trials: pd.DataFrame) -> dict:
    """The frame rate and offset that best align the track with the trial table.

    A grid search (70 to 90 frames/s in 0.25 steps, offsets -20 to 20 s in 0.5 s steps, then a
    finer grid around the best) for the largest `trial_displacement`, and the offset refitted on
    each half of the session at that rate, to see whether one linear clock holds throughout. This
    is a check made here, not the paper's method; the grids are a standard choice."""
    def best(fgrid, ogrid, tr):
        return max((trial_displacement(x, tr, f, o), f, o) for f in fgrid for o in ogrid)
    sc, f, o = best(np.arange(70, 90.01, 0.25), np.arange(-20, 20.01, 0.5), trials)
    sc, f, o = best(np.arange(f - 0.5, f + 0.501, 0.02), np.arange(o - 2, o + 2.01, 0.1), trials)
    h = len(trials) // 2
    first = best([f], np.arange(o - 5, o + 5.01, 0.1), trials.iloc[:h])
    second = best([f], np.arange(o - 5, o + 5.01, 0.1), trials.iloc[h:])
    return {"fps": float(f), "offset": float(o), "displacement": sc,
            "offset_first_half": float(first[2]), "offset_second_half": float(second[2])}


def nearest_frame(times: np.ndarray, events: np.ndarray) -> np.ndarray:
    """Index of the frame nearest each event time (which.min in the code)."""
    n = len(times)
    i = np.clip(np.searchsorted(times, events), 1, n - 1)
    return np.where(np.abs(times[i - 1] - events) <= np.abs(times[i] - events), i - 1, i)


# ---------------------------------------------------------------- sniffing


def sniff_table(s: dict, trials_times: np.ndarray | None = None) -> pd.DataFrame | None:
    """One row per sniff: duration (ms, between successive inhalations) and frequency (Hz).

    As fig4_cleaned.Rmd: rows with no exhalation are already dropped in the file; inhalations
    sorted, differences taken, those not above 0 dropped, frequency 1000 / difference. Each sniff
    is placed by its inhalation time in an odor trial (1), an omission trial (3) or the ITI (0).
    `trials_times` may give the inhalation times on another clock (for checks)."""
    if s["sniff_start"] is None:
        return None
    t = np.sort(s["sniff_start"])
    dms = np.diff(t * 1000)
    keep = dms > 0
    tt = t[1:][keep] if trials_times is None else trials_times
    return pd.DataFrame({"mouse": s["mouse"], "condition": s["condition"], "t": tt,
                         "duration_ms": dms[keep], "frequency": 1000 / dms[keep],
                         "period": label_periods(tt, s["trials"])})


def sniff_readings(d: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """The exclusions of the claims file's readings for Figure 4.

    "a_session": durations below the 5th or above the 95th percentile of the session dropped, and
    durations outside 10 to 1000 ms; "b_condition": the percentiles over all sessions of a
    condition; "code": no further exclusion, as fig4_cleaned.Rmd computes from the same files."""
    in_range = (d.duration_ms >= 10) & (d.duration_ms <= 1000)

    def within(g):
        lo, hi = g.quantile(0.05), g.quantile(0.95)
        return (g >= lo) & (g <= hi)
    per_session = d.groupby(["mouse", "condition"]).duration_ms.transform(within).astype(bool)
    per_condition = d.groupby("condition").duration_ms.transform(within).astype(bool)
    return {"a_session": d[per_session & in_range], "b_condition": d[per_condition & in_range],
            "code": d}


# ---------------------------------------------------------------- maps


def map_frames(s: dict, fps: float = CODE_FPS, offset: float = 0.0,
               htr_reading: str = "code") -> pd.DataFrame:
    """Per frame of a session: nose x, y (first cohort flipped, negatives set to 0), speed,
    period label and whether an HTR is assigned to it, as fig5_cleaned.Rmd builds them.

    Frames are timed at i / 80 s for the HTR assignment (the video clock of the timestamps) and
    at i / fps - offset for the period labels; the code uses 80 and 0 for both."""
    x, y, _ = clean_nose(s)
    sp = speed_cm_s(x, y)
    if s["cohort"] == "first":
        x = FLIP_X - x
    x, y = np.maximum(x, 0), np.maximum(y, 0)
    n = len(x)
    video_t = frame_times(n)
    lab = label_periods(frame_times(n, fps) - offset, s["trials"])
    htr = np.zeros(n, bool)
    h = htr_times(s, htr_reading)
    if h is not None and len(h):
        htr[nearest_frame(video_t, h)] = True
    return pd.DataFrame({"x": x, "y": y, "speed": sp, "period": lab, "htr": htr})


def htr_rate_table(frames: pd.DataFrame, mouse: int, period: str) -> pd.DataFrame:
    """Per bin of 100 px, HTR count over occupancy in HTR/min for one mouse (fig5_cleaned.Rmd).

    Frames at or above 160 cm/s (and the first frame, which has no speed) are dropped. "all":
    bins the mouse occupied; "within": every bin the mouse occupied in the session, filled with 0
    where it had no within-trial time; "iti": bins it occupied in the ITI. The edge bins (x 1200,
    y 700) are dropped."""
    f = frames[frames.speed < MAX_SPEED_CM_S]
    f = f.assign(bx=(np.floor(f.x / HTR_BIN_PX) * HTR_BIN_PX).astype(int),
                 by=(np.floor(f.y / HTR_BIN_PX) * HTR_BIN_PX).astype(int))
    master = f.groupby(["bx", "by"]).size().rename("all_frames")
    sub = f if period == "all" else f[f.period > 0] if period == "within" else f[f.period == 0]
    occ = (sub.groupby(["bx", "by"]).size() / CODE_FPS).rename("occupancy_s")
    count = sub[sub.htr].groupby(["bx", "by"]).size().rename("htr_count")
    if period == "within":
        g = pd.DataFrame(index=master.index).join(occ).join(count).fillna(0)
        g["rate"] = np.where(g.occupancy_s > 0, g.htr_count / g.occupancy_s * 60, 0.0)
    else:
        g = pd.DataFrame(occ).join(count, how="outer").fillna({"htr_count": 0})
        g["rate"] = (g.htr_count / g.occupancy_s * 60).fillna(0)
    g = g.reset_index()
    g["mouse"] = mouse
    return g[(g.bx != HTR_EDGE_X) & (g.by != HTR_EDGE_Y)]


def occupancy_measures(frames: pd.DataFrame, bounds: tuple[float, float, float, float]) -> dict:
    """Shannon entropy (bits) of the 48 px occupancy map, and the fraction of frames in the four
    corner squares of 5 cm and 10 cm side, for frames at or below 160 cm/s.

    `bounds` (x0, x1, y0, y1) is the arena's extent, taken in the notebook from the pooled
    positions (an assumption, as the paper gives no arena coordinates)."""
    f = frames[frames.speed <= MAX_SPEED_CM_S]
    bx = np.floor(f.x.to_numpy() / OCC_BIN_PX).astype(int)
    by = np.floor(f.y.to_numpy() / OCC_BIN_PX).astype(int)
    _, cnt = np.unique(bx * 10000 + by, return_counts=True)
    p = cnt / cnt.sum()
    out = {"entropy": float(-(p * np.log2(p)).sum())}
    x0, x1, y0, y1 = bounds
    for side_cm in (5, 10):
        side = side_cm / CM_PER_PX
        xs = (f.x < x0 + side) | (f.x > x1 - side)
        ys = (f.y < y0 + side) | (f.y > y1 - side)
        out[f"corners_{side_cm}cm"] = float((xs & ys).mean())
    return out
