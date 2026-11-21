"""Loading and measures for the late-delay photoinhibition sessions of dandiset 000363.

Yang (2026), "Form, Timing, and Behavioral Matching of the Population Response to ALM
Photoinhibition", Research Square preprint doi:10.21203/rs.3.rs-11447300/v1, which reanalyses
the Mesoscale Activity Map dataset of Chen et al. (2024), DANDI 000363.

Each NWB file holds one session: the trial table, behavioural events (Go cue, licks,
photostimulation onsets with a control code), the photostimulation sites, video keypoints, and
the units (spike times, a classifier label, the electrode of each unit). Files are streamed from
the archive at the pinned version; only the arrays needed are read, and nothing is written to disk.
The raw electrical series, which make up almost all of each file, are never read.

Where the parameters come from. "Claims" is claims/yang-2026.yaml, whose shared methods M1 to M10
cite the paper; "Methods" is the paper's Materials and Methods.

- Sessions, laser and control trials (claims M1; Methods, Dataset, paragraph 2): bilateral
  trials are those whose photostimulation control code has a site list with ALM on both sides;
  a session enters when the median bilateral onset is within 0.08 s of -0.5 s from Go; control
  trials have no photostimulation and no early lick. Whether laser trials with an early lick are
  kept is open; `LASER_EARLY` names the readings ("keep", "drop").
- Units and regions (claims M2; Methods, Units and regions): units with classification "good";
  a region is the probe target the files give for the unit's electrode (`brain_regions` of the
  electrode location, "left ALM", "right Striatum" and so on), hemispheres pooled; reading (a) of
  M2. A region enters with at least 20 good units, a side with at least 10 laser and 10 control
  trials.
- Lick direction (claims M3, open): "licks", the side of the first lick after Go; "outcome",
  instructed side for hits, the other side for misses. Reaction time is the first lick after Go
  minus Go (a standard choice, M3). The pre-lick window is the 200 ms before that lick, in four
  50 ms bins (Methods, Matched distance).
- Rates (claims M4; Methods, Rates and coding axes): mean rate in a window, z-scored by the mean
  and SD of control trials in that window; units with control SD below 1e-6 dropped. The early
  window is 20 to 120 ms after laser onset. Its placement on control trials is open (M4):
  "go", every trial at the session's median onset; "own", laser trials at their own onset and
  controls at the median onset. Units used by a measure are those kept in every window it uses
  (a standard choice, M4).
- Go-aligned grid (claims M10; Methods, Time courses): 50 ms bins from -600 to +600 ms; 100 ms
  bins as the mean of two adjacent 50 ms rates, stepped by 50 ms (the non-overlapping reading is
  the subset starting at -600 ms).
- Video regression (claims M5; Methods, Rates and coding axes): mean x and y of jaw, nose and
  tongue over the choice window with an intercept. A frame counts as a detection when the
  keypoint's likelihood is at least `LIKELIHOOD_MIN` (0.9), an assumption: the files give a
  likelihood per frame and no detection flag, and 0.9 is the usual DeepLabCut cut (0.5 and 0.99
  are computed as well, `LIKELIHOOD_VARIANTS`, to show how much it matters). Trials
  without a detection take the control mean ("fill", reading a) or are dropped from the fit
  ("drop", reading b). Under reading b a region entry whose kept control trials are no more
  than the design's columns is left out: the regression is then exact, and the residual choice
  axis is round-off that differs between machines (a standard choice; the claims file and the
  paper set no minimum).
"""

from __future__ import annotations

import json
import os
import zlib
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
from dandi.dandiapi import DandiAPIClient

DANDISET_ID = "000363"
DANDISET_VERSION = "0.231012.2129"
PAPER_KEY = "yang-2026"

REGIONS = ["ALM", "striatum", "thalamus", "midbrain", "medulla"]
_PROBE_REGION = {"ALM": "ALM", "Striatum": "striatum", "Thalamus": "thalamus",
                 "Midbrain": "midbrain", "Medulla": "medulla"}

LATE_ONSET, ONSET_TOL = -0.50, 0.08      # Methods, Dataset
MIN_UNITS, MIN_TRIALS_SIDE = 20, 10      # Methods, Units and regions
SD_MIN = 1e-6                            # Methods, Rates and coding axes
EARLY = (0.02, 0.12)                     # s after laser onset
CHOICE_BINS = slice(0, 12)               # -600 to 0 ms (Methods, Rates and coding axes)
ACTION_BINS = slice(12, 18)              # 0 to 300 ms
GO_EDGES = np.round(np.arange(-0.6, 0.6001, 0.05), 3)   # 24 bins of 50 ms
N_GO = len(GO_EDGES) - 1
PRELICK = 0.2                            # s before the first lick, 4 bins of 50 ms
LIKELIHOOD_MIN = 0.9                     # assumption, see the docstring
LIKELIHOOD_VARIANTS = (0.5, 0.9, 0.99)   # thresholds also computed, to show the dependence
KEYPOINTS = ["Jaw", "Nose", "Tongue"]

# Column layout of the per-trial rate array: 24 Go bins, early ("go" placement), early ("own"
# placement), 4 pre-lick bins, the early window in two 50 ms bins ("own" placement).
COL_EARLY_GO, COL_EARLY_OWN = N_GO, N_GO + 1
COL_PRE = slice(N_GO + 2, N_GO + 6)
COL_EARLY50 = slice(N_GO + 6, N_GO + 8)
N_COLS = N_GO + 8


PAPER_SEED = 17   # the paper's one seed (Methods, Statistics; claims M8, M9)


def seed(claim: str, k: int | str = 0) -> int:
    """The claim's seed (protocol, Author step 3), plus k. With k = "paper", the paper's seed 17,
    run as a variant; NumPy's generator and the order of draws differ from the paper's private
    code, so it does not give the paper's splits, folds or match order."""
    if k == "paper":
        return PAPER_SEED
    return zlib.crc32(f"{PAPER_KEY}/{claim}".encode()) + k


# --------------------------------------------------------------------------------------------
# Archive access


def assets() -> list[dict]:
    """Path, size and streaming URL of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        out = []
        for a in ds.get_assets():
            if a.path.endswith(".nwb"):
                out.append({"path": a.path, "size": a.size,
                            "url": a.get_content_url(follow_redirects=1, strip_query=True)})
    return sorted(out, key=lambda a: a["path"])


def _open(url: str) -> h5py.File:
    return h5py.File(remfile.File(url), "r")


def _names(path: str) -> tuple[str, str]:
    base = path.split("/")[-1]
    return base.split("_")[0], base.split("_")[1]


def _trial_table(f: h5py.File) -> dict:
    """Trial events per trial: Go time, photostimulation code and onset, first lick."""
    T = f["intervals/trials"]
    st, sp = T["start_time"][:], T["stop_time"][:]
    n = len(st)
    B = f["acquisition/BehavioralEvents"]
    go = B["go_start_times/timestamps"][:]
    gt = np.full(n, np.nan)
    j = np.searchsorted(go, st)
    for i in range(n):
        if j[i] < len(go) and go[j[i]] < sp[i]:
            gt[i] = go[j[i]]
    code = np.zeros(n, int)
    on = np.full(n, np.nan)
    if "photostim_start_times" in B:
        pt = B["photostim_start_times/timestamps"][:]
        pc = B["photostim_start_times/control"][:]
        ti = np.searchsorted(st, pt, side="right") - 1
        for t, c, i in zip(pt, pc, ti):
            if i >= 0 and t < sp[i]:
                code[i], on[i] = int(c), t
    left = B["left_lick_times/timestamps"][:]
    right = B["right_lick_times/timestamps"][:]
    first = np.full(n, np.nan)
    lick_dir = np.zeros(n, int)
    for i in range(n):
        if np.isnan(gt[i]):
            continue
        a = left[(left > gt[i]) & (left < sp[i])]
        b = right[(right > gt[i]) & (right < sp[i])]
        la = a.min() if len(a) else np.inf
        lb = b.min() if len(b) else np.inf
        if np.isfinite(min(la, lb)):
            first[i] = min(la, lb)
            lick_dir[i] = 1 if lb < la else -1
    dec = lambda k: np.array([x.decode() if isinstance(x, bytes) else str(x) for x in T[k][:]])
    instr = dec("trial_instruction")
    outcome = dec("outcome")
    sites = {}
    if "optogenetics" in f["general"]:
        for d in f["general/optogenetics"]:
            loc = json.loads(f["general/optogenetics"][d]["location"][()])
            sites[int(d.split("_")[-1])] = loc
    bilateral = [c for c, loc in sites.items()
                 if len({x["ml_location"] for x in loc if x.get("brain_area") == "ALM"}) == 2]
    outcome_dir = np.where(outcome == "hit", np.where(instr == "right", 1, -1),
                           np.where(outcome == "miss", np.where(instr == "right", -1, 1), 0))
    return {
        "n": n, "start": st, "stop": sp, "go": gt, "code": code, "onset": on - gt,
        "first_lick": first - gt, "lick_dir": lick_dir, "outcome_dir": outcome_dir,
        "instr": np.where(instr == "right", 1, np.where(instr == "left", -1, 0)),
        "early": dec("early_lick") == "early", "outcome": outcome,
        "stim": dec("photostim_duration") != "N/A", "auto_water": T["auto_water"][:],
        "free_water": T["free_water"][:], "bilateral_codes": bilateral, "sites": sites,
        "photostim_events": int(len(B["photostim_start_times/timestamps"])) if "photostim_start_times" in B else 0,
    }


def survey(asset: dict) -> dict:
    """Session metadata and trial table, without spikes or video."""
    f = _open(asset["url"])
    mouse, ses = _names(asset["path"])
    tt = _trial_table(f)
    U = f["units"]
    cls = U["classification"][:]
    out = {"path": asset["path"], "url": asset["url"], "mouse": mouse, "session": ses,
           "size": asset["size"], "trials": tt, "n_units": len(cls),
           "n_good": int((cls == b"good").sum()), "n_spikes": int(U["spike_times"].shape[0])}
    bil = np.isin(tt["code"], tt["bilateral_codes"])
    out["n_bilateral"] = int(bil.sum())
    out["median_onset"] = float(np.nanmedian(tt["onset"][bil])) if bil.any() else np.nan
    out["has_photostim"] = bool(tt["stim"].any())
    f.close()
    return out


def survey_all(asset_list: list[dict], workers: int = 8) -> list[dict]:
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(survey, asset_list))


def is_late_delay(s: dict) -> bool:
    return np.isfinite(s["median_onset"]) and abs(s["median_onset"] - LATE_ONSET) <= ONSET_TOL


def _video(f: h5py.File, go: np.ndarray, licks: np.ndarray) -> tuple[np.ndarray, dict]:
    """Per trial mean x, y of jaw, nose, tongue over the choice window (-0.6 to 0 s from Go).

    For the clock check, also the fraction of frames with the tongue detected in the 50 ms
    after each lick, and with the lick times shifted by -0.5 s."""
    B = f["acquisition/BehavioralTimeSeries"]
    out = {thr: np.full((len(go), 6), np.nan) for thr in LIKELIHOOD_VARIANTS}
    info = {}
    for k, kp in enumerate(KEYPOINTS):
        name = f"Camera0_side_{kp}Tracking"
        if name not in B:
            info[kp] = "missing"
            continue
        d = B[name]["data"][:]
        ts = B[name]["timestamps"][:]
        a = np.searchsorted(ts, go - 0.6)
        b = np.searchsorted(ts, go)
        valid = np.isfinite(go)
        a, b = np.where(valid, a, 0), np.where(valid, b, 0)
        for thr in LIKELIHOOD_VARIANTS:
            ok_t = d[:, 2] >= thr
            csum = np.vstack([np.zeros((1, 3)), np.cumsum(np.c_[d[:, 0] * ok_t, d[:, 1] * ok_t, ok_t], axis=0)])
            s = csum[b] - csum[a]
            with np.errstate(invalid="ignore", divide="ignore"):
                out[thr][:, 2 * k] = np.where(s[:, 2] > 0, s[:, 0] / s[:, 2], np.nan)
                out[thr][:, 2 * k + 1] = np.where(s[:, 2] > 0, s[:, 1] / s[:, 2], np.nan)
        ok = d[:, 2] >= LIKELIHOOD_MIN
        info[kp] = {"frames": len(ts), "detected": float(ok.mean()),
                    "frame_interval_ms": float(np.median(np.diff(ts[:2000])) * 1000),
                    "t_range": (float(ts[0]), float(ts[-1]))}
        if kp == "Tongue" and len(licks):
            cs = np.r_[0, np.cumsum(ok)]
            for name_, shift in (("tongue_after_lick", 0.0), ("tongue_after_shifted", -0.5)):
                a_ = np.searchsorted(ts, licks + shift)
                b_ = np.searchsorted(ts, licks + shift + 0.05)
                n_ = b_ - a_
                info[name_] = float((cs[b_] - cs[a_]).sum() / max(n_.sum(), 1))
    return out, info


def load_session(s: dict) -> dict:
    """Rates of the good units of the five regions, per trial, in the windows the analyses use.

    `rates` has shape (trials, units, N_COLS) in spikes/s (see the column layout above); pre-lick
    columns are NaN on trials without a lick after Go. Trials without a Go cue keep NaN rates.
    """
    f = _open(s["url"])
    tt = s["trials"]
    U = f["units"]
    cls = U["classification"][:]
    uel = U["electrodes"][:]
    eloc = f["general/extracellular_ephys/electrodes/location"][:]
    probe = []
    for e in uel:
        try:
            probe.append(json.loads(eloc[e])["brain_regions"])
        except (ValueError, KeyError):
            probe.append("")
    probe = np.array(probe)
    region = np.array([_PROBE_REGION.get(p.split(" ")[-1], "") for p in probe])
    keep = np.where((cls == b"good") & (region != ""))[0]
    idx = U["spike_times_index"][:]
    spikes = U["spike_times"][:]
    go = tt["go"]
    med = s["median_onset"]
    n = tt["n"]
    bil = np.isin(tt["code"], tt["bilateral_codes"])
    starts = np.full((n, N_COLS), np.nan)
    ends = np.full((n, N_COLS), np.nan)
    starts[:, :N_GO] = go[:, None] + GO_EDGES[None, :-1]
    ends[:, :N_GO] = go[:, None] + GO_EDGES[None, 1:]
    starts[:, COL_EARLY_GO] = go + med + EARLY[0]
    ends[:, COL_EARLY_GO] = go + med + EARLY[1]
    own = np.where(bil, tt["onset"], med)
    starts[:, COL_EARLY_OWN] = go + own + EARLY[0]
    ends[:, COL_EARLY_OWN] = go + own + EARLY[1]
    fl = go + tt["first_lick"]
    pre_edges = np.arange(-PRELICK, 0.0001, 0.05)
    starts[:, COL_PRE] = fl[:, None] + pre_edges[None, :-1]
    ends[:, COL_PRE] = fl[:, None] + pre_edges[None, 1:]
    starts[:, COL_EARLY50] = (go + own)[:, None] + np.array([0.02, 0.07])[None, :]
    ends[:, COL_EARLY50] = (go + own)[:, None] + np.array([0.07, 0.12])[None, :]
    dur = ends - starts
    fin = np.isfinite(starts)
    sflat, eflat = starts[fin], ends[fin]
    rates = np.full((n, len(keep), N_COLS), np.nan, dtype=np.float32)
    unsorted = 0
    for j, u in enumerate(keep):
        lo = idx[u - 1] if u > 0 else 0
        st = spikes[lo:idx[u]]
        if np.any(np.diff(st) < 0):
            unsorted += 1
            st = np.sort(st)
        c = np.searchsorted(st, eflat) - np.searchsorted(st, sflat)
        r = np.full((n, N_COLS), np.nan)
        r[fin] = c / dur[fin]
        rates[:, j, :] = r
    B = f["acquisition/BehavioralEvents"]
    licks = np.sort(np.r_[B["left_lick_times/timestamps"][:], B["right_lick_times/timestamps"][:]])
    video, vinfo = _video(f, go, licks)
    out = {k: s[k] for k in ("path", "mouse", "session", "median_onset")}
    out.update({"trials": tt, "rates": rates, "region": region[keep], "probe": probe[keep],
                "video": video[LIKELIHOOD_MIN], "video_by_threshold": video, "video_info": vinfo, "unsorted_units": unsorted,
                "spike_range": (float(spikes.min()), float(spikes.max())) if len(spikes) else (np.nan, np.nan),
                "trial_range": (float(tt["start"][0]), float(tt["stop"][-1])),
                "first_spikes": spikes[:20].copy()})
    f.close()
    return out


def load_all(surveys: list[dict], workers: int = 3) -> list[dict]:
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(load_session, surveys))


# --------------------------------------------------------------------------------------------
# Trial sets


def trial_sets(S: dict, laser_early: str = "drop", lick: str = "licks") -> dict:
    """Laser and control masks, valid sides, lick direction and reaction time (M1, M3)."""
    tt = S["trials"]
    has_go = np.isfinite(tt["go"])
    laser = np.isin(tt["code"], tt["bilateral_codes"]) & has_go
    if laser_early == "drop":
        laser &= ~tt["early"]
    control = (~tt["stim"]) & (~tt["early"]) & has_go
    lick_dir = tt["lick_dir"] if lick == "licks" else tt["outcome_dir"]
    rt = tt["first_lick"].copy()
    rt[tt["lick_dir"] == 0] = np.nan
    sides = [sd for sd in (-1, 1)
             if (laser & (tt["instr"] == sd)).sum() >= MIN_TRIALS_SIDE
             and (control & (tt["instr"] == sd)).sum() >= MIN_TRIALS_SIDE]
    return {"laser": laser, "control": control, "sides": sides, "lick_dir": lick_dir,
            "rt": rt, "instr": tt["instr"]}


def zscore_window(X: np.ndarray, control: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Z-score (trials, units) by control trials; return z and the mask of units kept."""
    mu = np.nanmean(X[control], axis=0)
    sd = np.nanstd(X[control], axis=0)
    keep = sd >= SD_MIN
    with np.errstate(invalid="ignore", divide="ignore"):
        Z = (X - mu) / np.where(keep, sd, 1.0)
    return Z, keep


def window_rates(S: dict, units: np.ndarray, name) -> np.ndarray:
    """Rates (trials, units) in a named window: 'choice', 'action', 'early_go', 'early_own',
    'pre' (mean of the four pre-lick bins), ('go50', k), ('go100', k) with k the 50 ms start
    index, ('pre50', k), ('early50', k) the early window in two 50 ms bins."""
    R = S["rates"][:, units, :]
    if name == "choice":
        return R[:, :, CHOICE_BINS].mean(axis=2)
    if name == "action":
        return R[:, :, ACTION_BINS].mean(axis=2)
    if name == "early_go":
        return R[:, :, COL_EARLY_GO]
    if name == "early_own":
        return R[:, :, COL_EARLY_OWN]
    if name == "pre":
        return R[:, :, COL_PRE].mean(axis=2)
    kind, k = name
    if kind == "go50":
        return R[:, :, k]
    if kind == "go100":
        return R[:, :, k:k + 2].mean(axis=2)
    if kind == "pre50":
        return R[:, :, COL_PRE.start + k]
    if kind == "early50":
        return R[:, :, COL_EARLY50.start + k]
    raise ValueError(name)


def go100_starts() -> np.ndarray:
    """Start (s from Go) of each 100 ms bin stepped by 50 ms; 23 bins from -0.6 to 0.5."""
    return GO_EDGES[:N_GO - 1]


# --------------------------------------------------------------------------------------------
# Axes and fractions (M5, M6)


def _side_diff(Z, a_mask, b_mask, instr, sides, weights_mask):
    """Mean(Z[a]) - mean(Z[b]) within each side, combined by the counts of weights_mask."""
    num, den = 0.0, 0
    for sd in sides:
        a = a_mask & (instr == sd)
        b = b_mask & (instr == sd)
        w = int((weights_mask & (instr == sd)).sum())
        if a.sum() == 0 or b.sum() == 0 or w == 0:
            continue
        num = num + w * (np.nanmean(Z[a], axis=0) - np.nanmean(Z[b], axis=0))
        den += w
    return num / den if den else None


def video_design(S: dict, control_lick: np.ndarray, reading: str = "fill", threshold: float | None = None):
    """Design matrix (with intercept) for the video regression on the given trials; threshold
    selects the keypoint likelihood cut (default LIKELIHOOD_MIN)."""
    V = (S["video"] if threshold is None else S["video_by_threshold"][threshold])[control_lick]
    if reading == "fill":
        mu = np.nanmean(V, axis=0)
        mu = np.where(np.isfinite(mu), mu, 0.0)
        V = np.where(np.isfinite(V), V, mu)
        keep = np.ones(len(V), bool)
    else:
        keep = np.all(np.isfinite(V), axis=1)
        V = V[keep]
    V = V[:, np.nanstd(V, axis=0) > 0] if len(V) else V
    return np.c_[np.ones(len(V)), V], keep


def axes(S: dict, region: str, ts: dict, early: str = "early_own", video: str = "fill",
         regress: bool = True, extra_windows=(), threshold: float | None = None) -> dict | None:
    """Choice and action axes, the early difference, and the units they use, for one region."""
    units = np.where(S["region"] == region)[0]
    if len(units) < MIN_UNITS or not ts["sides"]:
        return None
    ctrl = ts["control"]
    wins = ["choice", "action", early] + list(extra_windows)
    Zs, keep = {}, np.ones(len(units), bool)
    for w in wins:
        Z, k = zscore_window(window_rates(S, units, w), ctrl)
        Zs[w] = Z
        keep &= k
    if keep.sum() < 2:
        return None
    for w in wins:
        Zs[w] = Zs[w][:, keep]
    ld = ts["lick_dir"]
    cl = ctrl & (ld != 0)
    Xc = Zs["choice"][cl]
    dirs = ld[cl]
    if regress:
        D, rows = video_design(S, cl, video, threshold)
        if D.shape[0] <= D.shape[1]:
            return None
        Xc, dirs = Xc[rows], dirs[rows]
        beta, *_ = np.linalg.lstsq(D, Xc, rcond=None)
        Xc = Xc - D @ beta
    if (dirs == 1).sum() < 1 or (dirs == -1).sum() < 1:
        return None
    c = Xc[dirs == 1].mean(0) - Xc[dirs == -1].mean(0)
    Xa = Zs["action"][cl]
    a = Xa[ld[cl] == 1].mean(0) - Xa[ld[cl] == -1].mean(0)
    if np.linalg.norm(c) == 0 or np.linalg.norm(a) == 0:
        return None
    c, a = c / np.linalg.norm(c), a / np.linalg.norm(a)
    d = _side_diff(Zs[early], ts["laser"], ctrl, ts["instr"], ts["sides"], ts["laser"])
    if d is None:
        return None
    Q, _ = np.linalg.qr(np.c_[c, a])
    return {"choice": c, "action": a, "Q": Q, "d": d, "Z": Zs, "units": units[keep],
            "n_units": int(keep.sum()), "n_region_units": len(units)}


def fractions(d: np.ndarray, ax: dict) -> dict:
    e = float(d @ d)
    return {"joint": float(np.sum((ax["Q"].T @ d) ** 2) / e),
            "choice": float((ax["choice"] @ d) ** 2 / e),
            "action": float((ax["action"] @ d) ** 2 / e),
            "energy": e}


# --------------------------------------------------------------------------------------------
# Control splits (Methods, Rates and coding axes, paragraph 3)


def control_splits(Z: np.ndarray, ts: dict, rng: np.random.Generator, n_splits: int = 20,
                   small: str = "disjoint") -> list[np.ndarray]:
    """Difference vectors between two groups of control trials, each the size of the side's
    laser set, sides combined by laser counts. For a side with fewer than twice as many
    controls as laser trials: 'disjoint', two groups without overlap as large as the controls
    allow; 'independent', two groups of laser-set size drawn independently."""
    out = []
    instr = ts["instr"]
    for _ in range(n_splits):
        num, den = 0.0, 0
        for sd in ts["sides"]:
            c = np.where(ts["control"] & (instr == sd))[0]
            nl = int((ts["laser"] & (instr == sd)).sum())
            if len(c) >= 2 * nl:
                p = rng.permutation(c)
                g1, g2 = p[:nl], p[nl:2 * nl]
            elif small == "disjoint":
                p = rng.permutation(c)
                k = len(c) // 2
                g1, g2 = p[:k], p[k:2 * k]
            else:
                g1 = rng.choice(c, nl, replace=False)
                g2 = rng.choice(c, nl, replace=False)
            num = num + nl * (Z[g1].mean(0) - Z[g2].mean(0))
            den += nl
        out.append(num / den)
    return out


# --------------------------------------------------------------------------------------------
# Decoding (M8; Methods, Decoding)


def decode(X: np.ndarray, y: np.ndarray, instr: np.ndarray, is_ctrl: np.ndarray, seed_: int,
           Cs=(0.1, 1.0, 10.0), fixed_C: float | None = None, precentered: bool = False) -> float:
    """Balanced accuracy of L2 logistic regression under 5-fold CV stratified by instructed
    side and lick direction. Features are X minus the mean of control trials of the same side,
    that mean estimated in the training fold. With precentered, X is already a deviation from
    the control mean (laser trials decoded alone, M8 reading a, where no control trial is in a
    fold) and is used as given. With fixed_C None, C is chosen from Cs by an inner
    stratified 5-fold search on balanced accuracy (a standard choice, claims M8)."""
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import balanced_accuracy_score
    from sklearn.model_selection import StratifiedKFold
    import warnings
    warnings.filterwarnings("ignore")

    strat = (y > 0).astype(int) * 2 + (instr > 0).astype(int)

    def center(Xtr, itr, ctr, Xte, ite):
        Xtr, Xte = Xtr.copy(), Xte.copy()
        if precentered:
            return Xtr, Xte
        for sd in (-1, 1):
            m = ctr & (itr == sd)
            mu = Xtr[m].mean(0) if m.any() else Xtr[itr == sd].mean(0)
            Xtr[itr == sd] -= mu
            Xte[ite == sd] -= mu
        return Xtr, Xte

    def fit_score(Xtr, ytr, Xte, yte, C):
        m = LogisticRegression(C=C, solver="lbfgs", max_iter=2000)
        m.fit(Xtr, ytr)
        return balanced_accuracy_score(yte, m.predict(Xte))

    outer = StratifiedKFold(5, shuffle=True, random_state=seed_ % (2 ** 32))
    pred = np.zeros(len(y))
    for tr, te in outer.split(X, strat):
        Xtr, Xte = center(X[tr], instr[tr], is_ctrl[tr], X[te], instr[te])
        if fixed_C is None:
            inner = StratifiedKFold(5, shuffle=True, random_state=(seed_ + 1) % (2 ** 32))
            scores = []
            for C in Cs:
                sc = []
                for itr, ite in inner.split(X[tr], strat[tr]):
                    a, b = center(X[tr][itr], instr[tr][itr], is_ctrl[tr][itr], X[tr][ite], instr[tr][ite])
                    sc.append(fit_score(a, y[tr][itr], b, y[tr][ite], C))
                scores.append(np.mean(sc))
            C = Cs[int(np.argmax(scores))]
        else:
            C = fixed_C
        m = LogisticRegression(C=C, solver="lbfgs", max_iter=2000).fit(Xtr, y[tr])
        pred[te] = m.predict(Xte)
    return float(balanced_accuracy_score(y, pred))


# --------------------------------------------------------------------------------------------
# Matching (M9; Methods, Matched distance)


def match(ts: dict, rng: np.random.Generator, pick: str = "closest", caliper: float = 0.1,
          min_pairs: int = 10) -> list[tuple[int, int, int]]:
    """Pairs (laser, control, second control or -1) within session and instructed side.

    Each laser trial with a lick, in random order, takes an unused control trial with the same
    lick direction and reaction time within the caliper: 'closest' takes the smallest difference,
    'random' any within the caliper; ties are broken at random. Each retained control then takes
    a second control by the same rule from controls not already used. Sessions with fewer than
    min_pairs pairs give no pairs."""
    rt, ld, instr = ts["rt"], ts["lick_dir"], ts["instr"]
    pairs = []
    used = set()
    for sd in ts["sides"]:
        L = np.where(ts["laser"] & (instr == sd) & np.isfinite(rt) & (ld != 0))[0]
        C = np.where(ts["control"] & (instr == sd) & np.isfinite(rt) & (ld != 0))[0]
        side_pairs = []
        for l in rng.permutation(L):
            cand = [c for c in C if c not in used and ld[c] == ld[l] and abs(rt[c] - rt[l]) <= caliper]
            if not cand:
                continue
            cand = np.array(cand)
            if pick == "closest":
                diff = np.abs(rt[cand] - rt[l])
                cand = cand[diff == diff.min()]
            c = int(rng.choice(cand))
            used.add(c)
            side_pairs.append([int(l), c, -1])
        for p in rng.permutation(len(side_pairs)) if side_pairs else []:
            l, c, _ = side_pairs[p]
            cand = [k for k in C if k not in used and ld[k] == ld[c] and abs(rt[k] - rt[c]) <= caliper]
            if not cand:
                continue
            cand = np.array(cand)
            if pick == "closest":
                diff = np.abs(rt[cand] - rt[c])
                cand = cand[diff == diff.min()]
            k = int(rng.choice(cand))
            used.add(k)
            side_pairs[p][2] = k
        pairs += [tuple(p) for p in side_pairs]
    return pairs if len(pairs) >= min_pairs else []


def residual(Zbins: list[np.ndarray], pairs, missing: str = "drop", combine: str = "mean"):
    """Mean laser-control minus mean control-control Euclidean distance on the pairs.

    Zbins is a list of (trials, units) arrays (one per bin). combine 'mean' averages the
    per-bin distances, 'concat' takes the distance of the concatenated bins. missing 'drop'
    drops a pair without a second control from both distances; 'keep' keeps it for the
    laser-control distance."""
    P = np.array(pairs)
    X = Zbins[0][:, :, None] if len(Zbins) == 1 else np.stack(Zbins, axis=2)

    def dist(a, b):
        if combine == "mean":
            return np.sqrt(((X[a] - X[b]) ** 2).sum(axis=1)).mean(axis=1)
        return np.sqrt(((X[a] - X[b]) ** 2).sum(axis=(1, 2)))

    has2 = P[:, 2] >= 0
    lc_rows = P if missing == "keep" else P[has2]
    lc = dist(lc_rows[:, 0], lc_rows[:, 1])
    cc = dist(P[has2, 1], P[has2, 2])
    return float(np.nanmean(lc) - np.nanmean(cc)), float(np.nanmean(lc)), float(np.nanmean(cc))


def curve_units(S: dict, units: np.ndarray, control: np.ndarray):
    """Units and z-scored 50 ms Go bins for the distance curve (claims M10): units passing the
    SD threshold in every bin; if fewer than 20 do, units passing in at least 80% of bins, with
    their failing bins set to zero. Z-score reference, every non-early-lick control trial."""
    Zs, ks = [], []
    for k in range(N_GO):
        Z, keep = zscore_window(window_rates(S, units, ("go50", k)), control)
        Zs.append(Z)
        ks.append(keep)
    K = np.array(ks)
    every = K.all(axis=0)
    if every.sum() >= MIN_UNITS:
        sel = every
    else:
        sel = K.mean(axis=0) >= 0.8
    out = []
    for k in range(N_GO):
        Z = Zs[k][:, sel].copy()
        Z[:, ~K[k, sel]] = 0.0
        out.append(Z)
    return out, sel


# --------------------------------------------------------------------------------------------
# Summary (M7)


def mouse_summary(values: dict[tuple[str, str], float]) -> tuple[float, float, int, int, dict]:
    """Mean of session values within mouse, then mean and SEM (n-1) across mice."""
    by = {}
    for (m, s), v in values.items():
        if v is not None and np.isfinite(v):
            by.setdefault(m, []).append(v)
    mm = {m: float(np.mean(v)) for m, v in by.items()}
    x = np.array(list(mm.values()))
    if len(x) == 0:
        return np.nan, np.nan, 0, 0, mm
    sem = float(x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else np.nan
    return float(x.mean()), sem, len(x), sum(len(v) for v in by.values()), mm


def limit_threads():
    for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
        os.environ.setdefault(k, "1")
