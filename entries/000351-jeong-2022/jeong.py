"""Loading and measures for the photometry data of dandiset 000351.

Jeong, Taylor, Floeder et al. (2022), Mesolimbic dopamine release conveys causal associations,
Science 378, eabq6740, doi:10.1126/science.abq6740.

Each NWB file holds one session of one mouse: the event log (`acquisition/eventlog`: event code,
event time and a no-solenoid flag), the raw photometry (`acquisition/photometry`, not read
here) and dF/F (`processing/photometry/dff`). Files are streamed from the archive at the pinned
version; nothing is written to disk. Only the event log and dF/F are read.

Where the parameters come from. "Code" is github.com/namboodirilab/ANCCR at commit
cff44144e60a4313a30ffbb4bb8a1f3dd398b525, the commit the claims file was written from;
"claims" is claims/000351/10.1126-science.abq6740.yaml, whose criteria cite the Methods and
that code.

- Event codes (claims, header; functions/eventfrompavlovian.m): 0 session end, 5 lick, 7 random
  or background reward, 10 cue-associated reward (no-solenoid flag set when no reward was
  given), 14 trial end, 15 and 16 the two cues, 31 laser (Experiment 7). In Experiment 7 code 15
  marks both cues, CS1 the odd occurrences and CS2 the even ones (code,
  backpropagation_sequential.py).
- Event times are in seconds in the files (the file states milliseconds; see the data check).
  The Matlab scripts work in milliseconds; windows here are written in seconds.
- `auc_matlab` reproduces functions/aucsignal2event.m: the dF/F sample nearest each event, and
  the sum of the samples from round(w0/dt) to round(w1/dt) bins from it, without multiplying by
  the sample interval (claims, header). `auc_python` reproduces calculate_auc of
  functions/plot.py: samples with time in [t + w0, t + w1], summed and multiplied by the mean
  sample interval. `align` and `auc_aligned` reproduce alignsignal2event.m (with its Gaussian
  smoothing, sigma `resolution` samples over 5 x resolution samples, the Matlab
  fspecial('Gaussian') kernel, 'same' convolution along time) and aucsignal.m (the sum of the
  aligned samples in the window times the mean bin size, here in milliseconds, as the Matlab
  scripts have it, so that values are on the scale of the paper's code).
- `first_time_after` reproduces functions/firsttimeafterevent.m; `classify_licks` reproduces
  functions/classifylicks.m (bout interval 1 s, claims figs8b).
"""

from __future__ import annotations

import re
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import remfile
from dandi.dandiapi import DandiAPIClient

DANDISET_ID = "000351"
DANDISET_VERSION = "0.260828.1905"

# Subjects of the code's lists (claims, header), named as in the dandiset.
EXP1_MICE = ["HJ-FP-M2", "HJ-FP-M3", "HJ-FP-M4", "HJ-FP-F1", "HJ-FP-F2", "HJ-FP-M6", "HJ-FP-M7",
             "HJ-FP-M8"]
PAV_MICE = EXP1_MICE[:7]
DAT_MICE = [f"HJ-FP-datHT-stGtACR-M{i}" for i in range(2, 8)]   # M8 excluded (Fig S12D)
DAT_EXCLUDED = "HJ-FP-datHT-stGtACR-M8"
CONTROL_MICE = ["HJ-FP-datWT-stGtACR-F1"] + [f"HJ-FP-WT-stGtACR-{i}" for i in
                                             ["F1", "F2", "F3", "M1", "M2", "M3"]]
LONGITI_MICE = [f"DB-longITI-C1-{i}" for i in ["F1", "F2", "M1", "M2", "M3", "M4"]]

LICK, BGD_REWARD, REWARD, TRIAL_END, CUE1, CUE2, SESSION_END, LASER = 5, 7, 10, 14, 15, 16, 0, 31


def session_day(path: str) -> int:
    """The number after "Day" in the file name, as load_dandi_url of the code reads it."""
    return int(re.split(r"\.nwb|-", path.split("Day")[1])[0])


def list_assets() -> list[dict]:
    """Every asset of the pinned version: path, size, subject, day and S3 URL."""
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        out = []
        for a in ds.get_assets():
            subject = a.path.split("/")[0].removeprefix("sub-")
            out.append({"path": a.path, "size": a.size, "subject": subject,
                        "session": a.path.split("_ses-")[1].removesuffix(".nwb"),
                        "day": session_day(a.path),
                        # the S3 address of the blob, as get_content_url resolves it
                        "url": f"https://dandiarchive.s3.amazonaws.com/blobs/{a.blob[:3]}/"
                               f"{a.blob[3:6]}/{a.blob}"})
    return sorted(out, key=lambda r: (r["subject"], r["day"]))


def _text(f, key):
    if key not in f:
        return None
    v = f[key][()]
    return v.decode() if isinstance(v, bytes) else str(v)


def load_session(asset: dict, dff: bool = True) -> dict:
    """Event log and, if asked and present, dF/F of one file, streamed."""
    with h5py.File(remfile.File(asset["url"]), "r") as f:
        s = {k: asset[k] for k in ("path", "subject", "session", "day", "size")}
        s["description"] = _text(f, "session_description")
        s["session_id"] = _text(f, "general/session_id")
        s["subject_id"] = _text(f, "general/subject/subject_id")
        s["genotype"] = _text(f, "general/subject/genotype")
        s["sex"] = _text(f, "general/subject/sex")
        s["start"] = _text(f, "session_start_time")
        ev = f["acquisition/eventlog"]
        s["event_unit"] = ev["eventtime"].attrs.get("unit")
        s["code"] = ev["eventindex"][:].astype(int)
        s["time"] = ev["eventtime"][:].astype(float)
        s["nosol"] = ev["nonsolenoidflag"][:].astype(int)
        tab = f["acquisition/eventidx_table"]
        s["code_names"] = dict(zip(tab["event_index"][:].tolist(),
                                   [x.decode() if isinstance(x, bytes) else x
                                    for x in tab["event_description"][:]]))
        s["has_dff"] = "processing/photometry/dff" in f
        if "acquisition/photometry" in f:
            raw = f["acquisition/photometry/timestamps"]
            s["raw_n"] = raw.shape[0]
            s["raw_t_last"] = float(raw[-1])
        if s["has_dff"] and dff:
            d = f["processing/photometry/dff"]
            s["dff_unit"] = d["data"].attrs.get("unit")
            s["dff"] = d["data"][:].astype(np.float64)
            s["t"] = d["timestamps"][:].astype(np.float64)
    return s


def _load_with_dff(asset):
    return load_session(asset, True)


def _load_events_only(asset):
    return load_session(asset, False)


def load_many(assets: list[dict], dff: bool = True, workers: int = 16) -> list[dict]:
    """Load sessions in parallel processes (h5py serialises threads)."""
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(_load_with_dff if dff else _load_events_only, assets))


def events(s, code, flag=None):
    m = s["code"] == code
    if flag is not None:
        m &= s["nosol"] == flag
    return s["time"][m]


def session_end(s):
    e = events(s, SESSION_END)
    return e[0] if len(e) else s["time"][-1] + 5.0   # eventfrompavlovian.m: last event + 5 s


# ----------------------------------------------------------------- functions of the paper's code

def first_time_after(target, ref, until=None, within=None):
    """firsttimeafterevent.m: first target time after each reference time.

    `until` is an array of window ends (target > ref and target < until), `within` a single
    window length (target > ref and target < ref + within), neither an unlimited search
    (target >= ref)."""
    target = np.sort(np.asarray(target))
    out = np.full(len(ref), np.nan)
    for i, r in enumerate(ref):
        if until is None and within is None:
            j = np.searchsorted(target, r, side="left")
            if j < len(target):
                out[i] = target[j]
            continue
        j = np.searchsorted(target, r, side="right")
        end = until[i] if until is not None else r + within
        if j < len(target) and target[j] < end:
            out[i] = target[j]
    return out


def nearest_index(t, times):
    """Index of the sample of `t` nearest each time (min |t - x| as in the Matlab code)."""
    good = np.isfinite(t)
    tt = t[good]
    idx_good = np.flatnonzero(good)
    j = np.clip(np.searchsorted(tt, times), 1, len(tt) - 1)
    left, right = tt[j - 1], tt[j]
    j = np.where(np.abs(times - left) <= np.abs(right - times), j - 1, j)
    return idx_good[j]


def mean_dt(t):
    return float(np.nanmean(np.diff(t)))


def auc_matlab(t, x, ev, window, out=None):
    """aucsignal2event.m: sum of samples from round(w0/dt) to round(w1/dt) around the nearest
    sample of each event; NaN where the event is NaN, excluded or the window leaves the
    recording. Samples are summed as the code does (sum, NaN propagates)."""
    ev = np.asarray(ev, float)
    dt = mean_dt(t)
    b0, b1 = int(round(window[0] / dt)), int(round(window[1] / dt))
    res = np.full(len(ev), np.nan)
    ok = np.isfinite(ev) if out is None else np.isfinite(ev) & ~np.asarray(out, bool)
    if not ok.any():
        return res
    idx = nearest_index(t, ev[ok])
    vals = np.full(len(idx), np.nan)
    for k, i in enumerate(idx):
        if i + b0 >= 0 and i + b1 < len(x):
            vals[k] = np.sum(x[i + b0:i + b1 + 1])
    res[ok] = vals
    return res


def auc_python(t, x, ev, window):
    """calculate_auc of functions/plot.py: sum of samples with t in [e + w0, e + w1] times the
    mean sample interval; NaN when no sample falls in the window."""
    dt = np.nanmean(np.diff(t))
    res = np.full(len(ev), np.nan)
    good = np.isfinite(t)
    tt, xx = t[good], x[good]
    for k, e in enumerate(ev):
        if not np.isfinite(e):
            continue
        a = np.searchsorted(tt, e + window[0], side="left")
        b = np.searchsorted(tt, e + window[1], side="right")
        if b > a:
            res[k] = np.sum(xx[a:b]) * dt
    return res


def gaussian_kernel(resolution):
    """fspecial('Gaussian', [1 5*resolution], resolution)."""
    n = 5 * resolution
    x = np.arange(n) - (n - 1) / 2
    k = np.exp(-x ** 2 / (2 * resolution ** 2))
    return k / k.sum()


def align(t, x, ev, window, resolution=0):
    """alignsignal2event.m: rows of dF/F around the nearest sample of each event, from
    round(w0/dt) to round(w1/dt) bins, dt the mean interval rounded to 0.1 ms; Gaussian
    smoothing along time when resolution > 0 (conv2 'same', so NaN spreads as in Matlab).
    Returns the time axis (s) and the aligned matrix."""
    dt_ms = round(mean_dt(t) * 1000 * 10) / 10
    b0, b1 = int(round(window[0] * 1000 / dt_ms)), int(round(window[1] * 1000 / dt_ms))
    rel = np.arange(b0, b1 + 1)
    out = np.full((len(ev), len(rel)), np.nan)
    ev = np.asarray(ev, float)
    ok = np.isfinite(ev)
    if ok.any():
        idx = nearest_index(t, ev[ok])
        cols = idx[:, None] + rel[None, :]
        valid = (cols >= 0) & (cols < len(x))
        rows = np.where(valid, x[np.clip(cols, 0, len(x) - 1)], np.nan)
        out[ok] = rows
    if resolution > 0:
        k = gaussian_kernel(resolution)
        out = np.apply_along_axis(lambda r: np.convolve(r, k, mode="same"), 1, out)
    return rel * dt_ms / 1000, out, dt_ms


def auc_aligned(time, rows, window, dt_ms):
    """aucsignal.m: nansum of the aligned samples with time in the window, times the mean bin
    (ms, as the Matlab code's time axis is in ms). As in the code ("auc(~out) =
    nansum(signal(~out,time>=window(1) & time<=window(2)),2)*binsize"), a trial whose window
    is all NaN gets 0 and one with some NaN samples the sum of the others; `incomplete` flags
    them."""
    m = (time >= window[0] - 1e-9) & (time <= window[1] + 1e-9)
    binsize = np.nanmean(np.diff(time * 1000))
    return np.nansum(rows[:, m], axis=1) * binsize


def incomplete(time, rows, window):
    """True for each trial with any NaN aligned (and, where smoothed, smoothed) sample in the
    window: outside or at the edge of the dF/F coverage, or near a NaN sample."""
    m = (time >= window[0] - 1e-9) & (time <= window[1] + 1e-9)
    return np.isnan(rows[:, m]).any(axis=1)


def classify_licks(lick, reward, end, bout=1.0):
    """classifylicks.m. Returns bout index (1 onset, 2 mid, 3 offset), consummatory flag per lick,
    consummatory bout length per reward (s) and the reward index of each lick."""
    lick = np.asarray(lick, float)
    reward = np.asarray(reward, float)
    n_r = len(reward)
    first = first_time_after(lick, reward, until=np.r_[reward[1:], end])
    edges = np.r_[0.0, reward, end]
    # lickrwidx of the code: the 1-based number of the latest reward before each lick (0 before
    # the first reward, -1 after the session end).
    lickrw = np.full(len(lick), -1)
    for k in range(n_r + 1):
        lickrw[(lick >= edges[k]) & (lick < edges[k + 1])] = k
    d = np.diff(np.r_[0.0, lick])
    idx = np.full(len(lick), 2)
    idx[d >= bout] = 1
    nxt = np.r_[d[1:], 0.0]
    idx[nxt >= bout] = 3
    consum = np.zeros(len(lick), bool)
    blen = np.full(n_r, np.nan)
    for r in range(n_r):
        if not np.isfinite(first[r]):
            continue
        fi = np.flatnonzero(lick == first[r])[0]
        after = lick > first[r]
        e = np.flatnonzero(after & (idx == 3))
        if len(e):
            consum[fi:e[0] + 1] = True
        if np.sum(idx[after] == 2) == np.sum(after):
            consum[fi:] = True
        cand = lick[(idx == 3) & (lickrw >= r + 1)]
        ends = [end] + ([cand[0]] if len(cand) else [])
        if r < n_r - 1:
            ends.append(reward[r + 1])
        bend = min(ends)
        blen[r] = bend - first[r]
        consum[(lick >= first[r]) & (lick <= bend)] = True
    return idx, consum, blen, lickrw


# ------------------------------------------------------------------ day lists of the paper's code
# Copied from the scripts named (claims, session-day-link); keys are dandiset subject names.

def _bymouse(values):
    return dict(zip(PAV_MICE, values))


# analysis/fig4/cumsum_pavlovian.m: columns initial learning, cue duration change, extinction,
# background rewards; ndaybeforestart [0, 3, 1, 1]; ratio [1.5, 1.9, 2.5, 2].
CUMSUM_START = _bymouse([[16, 29, 70, 38], [12, 24, 61, 28], [13, 32, 66, 38], [7, 19, 42, 23],
                         [13, 24, 46, 28], [7, 19, 47, 23], [6, 20, 43, 24]])
CUMSUM_END = _bymouse([[28, 32, 72, 43], [23, 27, 63, 38], [31, 37, 67, 47], [18, 22, 43, 27],
                       [23, 27, 47, 33], [18, 22, 50, 30], [19, 23, 44, 29]])
CUMSUM_BEFORE = [0, 3, 1, 1]
CUMSUM_RATIO = [1.5, 1.9, 2.5, 2.0]
LEARNED_DAY = _bymouse([22, 17, 25, 12, 17, 12, 14])
# analysis/fig4/cumsum_bgdrw_vs_extinction.m: background rewards, extinction; 2 sessions before.
BGD_START = _bymouse([[33, 70], [28, 61], [38, 66], [23, 42], [28, 46], [23, 47], [24, 43]])
BGD_END = _bymouse([[43, 72], [38, 63], [47, 67], [27, 43], [33, 47], [30, 50], [29, 44]])
# analysis/fig5/intermediate_rsp_trialless.m
TRIALLESS_LEARNED = _bymouse([77, 67, 70, 46, 51, 53, 48])
TRIALLESS_END = _bymouse([78, 68, 72, 49, 54, 55, 50])
# analysis/figS10/omission.m: first session of Experiment 3 and of extinction.
OMISSION_DAYS = _bymouse(list(zip([29, 24, 32, 19, 24, 19, 20], [70, 61, 66, 42, 46, 47, 43])))
# analysis/figS10/cue_acquisition.m and analysis/fig6/backpropagation_pavlovian.m use the
# initial learning start and end days and LEARNED_DAY, the same as CUMSUM_* column 0.


CODE_URL = ("https://raw.githubusercontent.com/namboodirilab/ANCCR/"
            "cff44144e60a4313a30ffbb4bb8a1f3dd398b525/")
CODE_SCRIPTS = ["analysis/fig4/cumsum_pavlovian.m", "analysis/fig4/cumsum_bgdrw_vs_extinction.m",
                "analysis/fig5/intermediate_rsp_trialless.m", "analysis/figS10/omission.m",
                "analysis/figS10/cue_acquisition.m", "analysis/fig6/backpropagation_pavlovian.m"]
CODE_NAMES = ["mouseList", "startday", "endday", "learnedday", "ndaybeforestart", "ratio"]


def fetch_code_lists():
    """The mouse and day lists of the scripts named in CODE_SCRIPTS, read from the repository at
    the pinned commit: per script, the source lines that define them (Matlab continuation lines
    joined) and their values (mouseList as dandiset names, the others as integer or float
    arrays, one row per row of the Matlab matrix)."""
    from urllib.request import urlopen
    out = {}
    for path in CODE_SCRIPTS:
        text = urlopen(CODE_URL + path, timeout=60).read().decode()
        text = re.sub(r"\.\.\.\s*\n\s*", " ", text)
        found = {}
        for line in text.splitlines():
            m = re.match(r"\s*(\w+)\s*=\s*([\[{].*?[\]}])\s*;", line)
            if not m or m.group(1) not in CODE_NAMES:
                continue
            name, body = m.groups()
            if name == "mouseList":
                value = [x.replace("_", "-") for x in re.findall(r"'([^']+)'", body)]
            else:
                value = np.array([[float(v) for v in row.split(",")]
                                  for row in body.strip("[]").split(";")])
            found[name] = (line.strip(), value)
        out[path] = found
    return out


def matlab_round(x):
    return int(np.floor(x + 0.5)) if x >= 0 else -int(np.floor(-x + 0.5))


# ----------------------------------------------------------------------------- Experiment 1

def exp1_rewards(s):
    """Per reward of a random reward session (corr_randomrewards.m): IRI (s, NaN for the first),
    first lick before the next reward or session end, the exclusions, and the response, the sum
    of dF/F samples from -0.5 to 1 s around the first lick minus that from -2 to -0.5 s."""
    lick = events(s, LICK)
    rw = events(s, BGD_REWARD)
    end = session_end(s)
    iri = np.r_[np.nan, np.diff(rw)]
    first = first_time_after(lick, rw, until=np.r_[rw[1:], end])
    short = (iri < 3) & (np.arange(len(rw)) > 0)
    nolick = np.isnan(first)
    out = short | nolick
    out[0] = False
    x = s["dff"] / 100.0
    sig = auc_matlab(s["t"], x, first, (-0.5, 1.0), out)
    base = auc_matlab(s["t"], x, first, (-2.0, -0.5), out)
    return {"reward": rw, "iri": iri, "first_lick": first, "short": short, "nolick": nolick,
            "out": out, "response": sig - base, "lick": lick, "end": end}


def exp1_licks(s):
    """Lick rates and per-reward measures of lick_rsp_randomrewards.m (bout interval 1 s)."""
    r = exp1_rewards(s)
    lick, rw, end = r["lick"], r["reward"], r["end"]
    idx, consum, blen, lickrw = classify_licks(lick, rw, end, 1.0)
    tot_b = np.nansum(blen)
    rates = {"total": len(lick) / end, "consummatory": consum.sum() / tot_b,
             "nonconsummatory": (~consum).sum() / (end - tot_b)}
    nxt = np.r_[rw[1:], end]
    n_consum = np.array([np.sum((lick >= a) & (lick < b) & consum) for a, b in zip(rw, nxt)])
    with np.errstate(divide="ignore", invalid="ignore"):
        lick_rate_rw = n_consum / blen
    separate = np.array([np.isin([1, 2], idx[lickrw == k + 1]).all() for k in range(len(rw))])
    x = s["dff"] / 100.0
    resp_all = (auc_matlab(s["t"], x, r["first_lick"], (-0.5, 1.0))
                - auc_matlab(s["t"], x, r["first_lick"], (-2.0, -0.5)))
    keep = ~r["short"] & separate
    return {"rates": rates, "lick_rate_rw": lick_rate_rw[keep], "response_rw": resp_all[keep],
            "bout_idx": idx, "consum": consum, "first_lick": r["first_lick"], "lick": lick}


def bout_onset_z(s, lk, windows):
    """Fig S8E (lick_rsp_randomrewards.m): dF/F around consummatory (first lick after reward)
    and non-consummatory bout onsets, -3 to 6 s, z-scored by the mean and SD over onsets of each
    onset's mean from -1.5 to -0.5 s; returns the mean z in each window."""
    out = {}
    onsets = {"consummatory": lk["first_lick"],
              "nonconsummatory": lk["lick"][(lk["bout_idx"] == 1) & ~lk["consum"]]}
    for kind, ev in onsets.items():
        time, rows, _ = align(s["t"], s["dff"], ev, (-3.0, 6.0), 0)
        bmask = (time >= -1.5 - 1e-9) & (time < -0.5 - 1e-9)
        base = np.nanmean(rows[:, bmask], axis=1)
        z = (np.nanmean(rows, axis=0) - np.nanmean(base)) / np.nanstd(base, ddof=1)
        for name, (a, b) in windows.items():
            m = (time >= a - 1e-9) & (time <= b + 1e-9)
            out[(kind, name)] = float(np.nanmean(z[m]))
        out[(kind, "n")] = int(np.isfinite(ev).sum())
    return out


def _peaks(x, height=None, prominence=None):
    from scipy.signal import find_peaks
    y = np.where(np.isfinite(x), x, np.nanmin(x))
    kw = {"distance": 50}
    if height is not None:
        kw["height"] = height
    if prominence is not None:
        kw["prominence"] = prominence
    locs, props = find_peaks(y, **kw)
    return locs, y[locs]


def peak_threshold(s):
    """baseline_activity_randomrewards.m: 20% of the mean of the top 5% of peaks (minimum
    distance 50 samples) of the animal's first session. dF/F is used in percent, as the code's
    dff*100 has it if its dff was a fraction; the scale does not enter the correlation."""
    _, pks = _peaks(s["dff"])
    srt = np.sort(pks)[::-1]
    return float(np.nanmean(srt[:int(np.floor(len(srt) * 0.05))]) * 0.2)


def baseline_peaks(s, threshold):
    """Mean size of spontaneous peaks in a session under the Methods' rule (more than 0.5 s from
    any lick and more than 2 s from any reward) and the code's (not within 0 to 2 s after a
    first lick after reward, and not within 0.5 s of a lick)."""
    locs, pks = _peaks(s["dff"], height=threshold, prominence=threshold * 0.5)
    pt = s["t"][locs]
    good = np.isfinite(pt)
    pt, pks = pt[good], pks[good]
    lick = np.sort(events(s, LICK))
    rw = events(s, BGD_REWARD)
    first = first_time_after(lick, rw, until=np.r_[rw[1:], session_end(s)])
    j = np.searchsorted(lick, pt)
    prev = np.where(j > 0, pt - lick[np.clip(j - 1, 0, len(lick) - 1)], np.inf)
    nxt = np.where(j < len(lick), lick[np.clip(j, 0, len(lick) - 1)] - pt, np.inf)
    near_lick = (prev < 0.5) | (nxt < 0.5)
    near_rw = (np.abs(pt[:, None] - rw[None, :]) <= 2.0).any(axis=1)
    ff = first[np.isfinite(first)]
    in_first = ((pt[:, None] >= ff[None, :]) & (pt[:, None] < ff[None, :] + 2.0)).any(axis=1)
    near_lick_m = (np.abs(pt[:, None] - lick[None, :]) <= 0.5).any(axis=1)
    return {"methods": float(np.mean(pks[~near_lick_m & ~near_rw])),
            "code": float(np.mean(pks[~in_first & ~near_lick])),
            "n_methods": int((~near_lick_m & ~near_rw).sum()), "n_code": int((~in_first & ~near_lick).sum()),
            "n_peaks": len(pks)}


def longiti_rates(s):
    """lick_across_iri_randomrewards.m: consummatory and non-consummatory lick rates."""
    lick, rw, end = events(s, LICK), events(s, BGD_REWARD), session_end(s)
    _, consum, blen, _ = classify_licks(lick, rw, end, 1.0)
    tot = np.nansum(blen)
    return {"consummatory": consum.sum() / tot, "nonconsummatory": (~consum).sum() / (end - tot)}


# ------------------------------------------------------------------------- Experiments 2 to 6

def pavlovian_events(s, trialless=False):
    """eventfrompavlovian.m. Cues (1 for code 15, 2 for code 16) after the last cue-associated
    reward event are dropped; each remaining cue is paired with the reward event of the same
    order. Returns cue identity, cue time, reward time, rewarded flag, CS duration (s), licks,
    and the first lick after each reward (until trial end when it comes 2 s or more after the
    reward, else until 1 s before the next cue; without limit in the trial-less task)."""
    code, t = s["code"], s["time"]
    lick = events(s, LICK)
    m = np.isin(code, [CUE1, CUE2])
    cs = np.where(code[m] == CUE1, 1, 2)
    cst = t[m]
    rwt = events(s, REWARD)
    rewarded = 1 - s["nosol"][code == REWARD]
    keep = cst <= rwt[-1]
    cs, cst = cs[keep], cst[keep]
    n = min(len(cst), len(rwt))
    pair_ok = len(cst) == len(rwt)
    cs, cst, rwt, rewarded = cs[:n], cst[:n], rwt[:n], rewarded[:n]
    csdur = np.nanmean(rwt - cst) - 1.0
    trial_end = events(s, TRIAL_END)
    end = session_end(s)
    if trialless:
        first = first_time_after(lick, rwt)
    elif len(trial_end) == len(rwt) and np.nanmean(trial_end - rwt) >= 2.0:
        first = first_time_after(lick, rwt, until=trial_end)
    else:
        first = first_time_after(lick, rwt, until=np.r_[cst[1:] - 1.0, end])
    return {"cs": cs, "cs_time": cst, "rw_time": rwt, "rewarded": rewarded, "cs_dur": csdur,
            "lick": lick, "first_lick": first, "paired": pair_ok, "n_trial_end": len(trial_end)}


def cs_plus_identity(s):
    ev = pavlovian_events(s)
    ids = np.unique(ev["cs"][ev["rewarded"] == 1])
    assert len(ids) == 1, ids
    return int(ids[0])


def count_rate(lick, ref, window):
    """numevent.m with normalisation: licks with t in [ref + w0, ref + w1] per second."""
    lick = np.sort(lick)
    a = np.searchsorted(lick, ref + window[0], side="left")
    b = np.searchsorted(lick, ref + window[1], side="right")
    return (b - a) / (window[1] - window[0])


def cs_plus_trials(s, csrw):
    """Per CS+ trial of a Pavlovian session (cumsum_pavlovian.m): the dopamine response, AUC of
    smoothed dF/F (fraction) from 0 to 2 s halved minus that from -1 to 0 s; the anticipatory
    lick rate of the Methods (0 to 2 s minus -1 to 0 s) and of the code (0 to CS duration + 1 s
    minus -1 to 0 s, kept as separate parts); the median lick time in cue and trace (s from cue
    onset, NaN without licks); the omission-window responses of omission.m."""
    ev = pavlovian_events(s)
    cst = ev["cs_time"][ev["cs"] == csrw]
    x = s["dff"] / 100.0
    time, rows, dt = align(s["t"], x, cst, (-2.0, 12.0), 10)
    base = auc_aligned(time, rows, (-1.0, 0.0), dt)
    cue = auc_aligned(time, rows, (0.0, 2.0), dt) / 2
    lick = ev["lick"]
    trace_end = ev["cs_dur"] + 1.0
    med = np.array([np.median(lick[(lick >= c) & (lick <= c + trace_end)]) - c
                    if np.any((lick >= c) & (lick <= c + trace_end)) else np.nan for c in cst])
    w3 = auc_aligned(time, rows, (3.0, 4.0), dt)
    w9 = auc_aligned(time, rows, (9.0, 10.0), dt)
    # unsmoothed AUCs for cue_acquisition.m and backpropagation_pavlovian.m
    time0, rows0, dt0 = align(s["t"], x, cst, (-2.0, 3.0), 0)
    return {"cs_time": cst, "da": cue - base, "da_base": base,
            "da_incomplete": incomplete(time, rows, (-1.0, 2.0)),
            "omit3_incomplete": incomplete(time, rows, (-1.0, 4.0)),
            "omit9_incomplete": incomplete(time, rows, (-1.0, 10.0)),
            "unsmoothed_incomplete": incomplete(time0, rows0, (-1.0, 3.0)),
            "lick_methods": count_rate(lick, cst, (0.0, 2.0)) - count_rate(lick, cst, (-1.0, 0.0)),
            "lick_code_cs": count_rate(lick, cst, (0.0, trace_end)),
            "lick_code_base": count_rate(lick, cst, (-1.0, 0.0)),
            "lick_median_ms": med * 1000, "cs_dur": ev["cs_dur"],
            "omit3_base": w3 - base, "omit9_base": w9 - base,
            "omit3_code": w3 / 1000 - base, "omit9_code": w9 / 1000 - base,
            "early": auc_aligned(time0, rows0, (0.0, 1.0), dt0),
            "late": auc_aligned(time0, rows0, (2.0, 3.0), dt0),
            "pre": auc_aligned(time0, rows0, (-1.0, 0.0), dt0)}


def abruptness(cum, ntotal):
    """cumsum_pavlovian.m: smooth the cumulative sum (Gaussian, sigma 2 trials, 10 wide, valid
    convolution), divide by its last value, and take the largest distance of the points 5 to
    ntotal - 5 from the line from (5, first value) to (ntotal - 5, 1). Returns the distance and
    its position (1-based index, as the code's change trial)."""
    sm = np.convolve(cum[:ntotal], gaussian_kernel(2), mode="valid")
    sm = sm / sm[-1]
    xs = np.arange(5, ntotal - 4)
    v1 = np.array([5.0, sm[0]])
    v2 = np.array([ntotal - 5.0, 1.0])
    a = v1 - v2
    b = np.c_[xs, sm] - v2
    d = np.abs(a[0] * b[:, 1] - a[1] * b[:, 0]) / np.hypot(*a)
    k = int(np.argmax(d))
    return float(d[k]), k + 1


def weibull(x, A, L, S, b):
    return A * (1 - 2.0 ** (-(x / L) ** S)) + b


def fit_weibull(y, lower, upper, rng, starts=20, bounded=True):
    """Least squares fit of the changing model within the code's bounds, from several random
    start points (Matlab's fit starts custom models at random points); returns the RSS. With
    `bounded=False` the start points are drawn the same way but only L > 0 and S > 0 are kept
    (the model is undefined otherwise)."""
    from scipy.optimize import least_squares
    x = np.arange(1, len(y) + 1, dtype=float)
    lo, hi = np.array(lower, float), np.array(upper, float)
    fit_lo = lo if bounded else np.array([-np.inf, 1e-6, 1e-6, -np.inf])
    fit_hi = hi + 1e-12 if bounded else np.full(4, np.inf)
    best = np.inf
    for _ in range(starts):
        p0 = lo + rng.random(4) * (hi - lo)
        p0[1] = max(p0[1], 1e-6)
        if not bounded:
            p0[2] = max(p0[2], 1e-6)
        try:
            r = least_squares(lambda p: weibull(x, *p) - y, p0, bounds=(fit_lo, fit_hi))
        except ValueError:
            continue
        best = min(best, float(np.sum(r.fun ** 2)))
    return best


def aic(rss, k, n):
    """2k + N ln(RSS) (cumsum_pavlovian.m)."""
    return 2 * k + n * np.log(rss)


def trialless_pairs(s, peak_readings=None, drop_incomplete=False):
    """intermediate_rsp_trialless.m for one session. Intermediate cues follow the previous cue by
    less than the mean cue-reward delay; cues in runs of three, pairs 0.5 s apart or less and
    intermediate cues 2.5 to 3 s after the previous cue are dropped (code). Cue response, AUC
    (unsmoothed) from 0 to 0.5 s minus the AUC 0.5 s before the previous cue (for both cues of a
    pair); reward response, AUC (smoothed) 0 to 0.5 s after the first lick after the reward minus
    the same baseline, only where that lick precedes the next reward. Returns per-session means
    for previous (0) and intermediate (1) cues, and the Fig S11D-E peak readings. With
    `drop_incomplete`, cue and reward values with a NaN sample in their windows (`incomplete`)
    are left out of the means; the counts of such values among the pairs are returned either
    way."""
    ev = pavlovian_events(s, trialless=True)
    cst, rwt, first = ev["cs_time"], ev["rw_time"], ev["first_lick"]
    delay = np.mean(rwt - cst)
    x = s["dff"] / 100.0
    tc, rc, dtc = align(s["t"], x, cst, (-2.0, 10.0), 0)
    tr, rr, dtr = align(s["t"], x, first, (-2.0, 5.0), 10)
    base = auc_aligned(tc, rc, (-0.5, 0.0), dtc)
    cue = auc_aligned(tc, rc, (0.0, 0.5), dtc)
    rew = auc_aligned(tr, rr, (0.0, 0.5), dtr)
    rew[np.isnan(first)] = np.nan
    inter = np.r_[False, np.diff(cst) < delay]
    idx = np.c_[np.r_[inter[1:], False], inter].astype(int)
    both = np.flatnonzero(idx.sum(1) == 2)
    for j in (both - 1, both + 1):
        j = j[(j >= 0) & (j < len(idx))]
        idx[j] = 0
    idx[idx.sum(1) == 2] = 0
    d = np.r_[np.inf, np.diff(cst)]
    short = np.flatnonzero((d <= 0.5) | ((d > 2.5) & (d < 3.0)))
    for j in (short, short - 1):
        j = j[(j >= 0)]
        idx[j] = 0
    idx = idx.astype(bool)
    inlick = np.r_[first[:-1] < rwt[1:], False]
    base[idx[:, 1]] = base[idx[:, 0]]
    cue_b, rew_b = cue - base, rew - base
    inc_c = incomplete(tc, rc, (-0.5, 0.5))
    inc_c[idx[:, 1]] |= inc_c[idx[:, 0]]
    inc_r = (incomplete(tr, rr, (0.0, 0.5)) & np.isfinite(first)) | inc_c
    out = {"n_pairs": int(idx[:, 1].sum()), "n_cues": len(cst), "delay": float(delay),
           "n_incomplete_cue": int((inc_c & idx.any(1)).sum()),
           "n_incomplete_rew": int((inc_r & idx.any(1) & inlick).sum())}
    if drop_incomplete:
        cue_b[inc_c] = np.nan
        rew_b[inc_r] = np.nan
    for k, name in enumerate(["prev", "inter"]):
        out[f"cue_{name}"] = float(np.nanmean(cue_b[idx[:, k]])) if idx[:, k].any() else np.nan
        sel = idx[:, k] & inlick
        out[f"rew_{name}"] = float(np.nanmean(rew_b[sel])) if sel.any() else np.nan
    # Fig S11D-E: peak dF/F after each cue minus dF/F immediately before it.
    if peak_readings:
        for (pw, bw), _ in peak_readings.items():
            post = (tc > 0) & (tc <= pw + 1e-9)
            peak = np.nanmax(rc[:, post], axis=1)
            if bw == "last":
                b = rc[:, np.flatnonzero(tc < 0)[-1]]
            else:
                b = np.nanmean(rc[:, (tc >= -0.5 - 1e-9) & (tc < 0)], axis=1)
            v = peak - b
            if drop_incomplete:
                v[inc_c] = np.nan
            for k, name in enumerate(["prev", "inter"]):
                out[f"peak_{pw}_{bw}_{name}"] = float(np.nanmean(v[idx[:, k]])) if idx[:, k].any() else np.nan
    return out


# ------------------------------------------------------------------------------ Experiment 7

def first_within(s, ref_code, within):
    """first_event_time_after_reference of functions/plot.py: first lick with
    0 < t - ref <= within after each reference event."""
    lick = np.sort(events(s, LICK))
    ref = events(s, ref_code)
    out = np.full(len(ref), np.nan)
    j = np.searchsorted(lick, ref, side="right")
    ok = (j < len(lick))
    out[ok] = lick[j[ok]]
    out[~(out - ref <= within)] = np.nan
    return out


def sequential_cues(s):
    """CS1 and CS2 times: odd and even occurrences of code 15 (backpropagation_sequential.py)."""
    c = events(s, CUE1)
    return c[0::2], c[1::2]


def seq_session(s):
    """Per-trial and per-session measures of one Experiment 7 session (dF/F in percent, AUC of
    calculate_auc in percent x s)."""
    t, x = s["t"], s["dff"]
    cs1, cs2 = sequential_cues(s)
    lick = np.sort(events(s, LICK))
    out = {"cs1": cs1, "cs2": cs2}
    # Fig 6D (backpropagation_sequential.py): AUC 0 to 1 s after CS1 and CS2; baselines of the
    # Methods' reading, 1 s and 1.5 s before CS1 (scaled to the 1 s window).
    out["early"] = auc_python(t, x, cs1, (0, 1))
    out["late"] = auc_python(t, x, cs2, (0, 1))
    out["pre1"] = auc_python(t, x, cs1, (-1, 0))
    out["pre15"] = auc_python(t, x, cs1, (-1.5, 0)) / 1.5
    # Fig 6I (learnign_curve_sequential.py): 1.5 s windows.
    b15 = auc_python(t, x, cs1, (-1.5, 0))
    out["cs1_15"] = auc_python(t, x, cs1, (0, 1.5)) - b15
    fl5 = first_within(s, REWARD, 5)
    n = min(len(fl5), len(b15))
    out["rw_15"] = auc_python(t, x, fl5[:n], (0, 1.5)) - b15[:n]
    cnt = lambda a, b: np.array([np.sum((lick >= c + a) & (lick < c + b)) for c in cs1])
    out["lick_cs1_rw"] = cnt(0, 3) - cnt(-3, 0)
    out["lick_cs1_cs2"] = cnt(0, 1.5) - cnt(-1.5, 0)
    out["lick_cs1_cs2_code"] = cnt(0, 1.5) - cnt(-1500, -1498.5)
    # Fig 6G (measure_inhibition_sequential.py): baseline level over the 0.5 s before CS1 (or
    # all code-15 events, the code's reference), CS2 bins of 0.5 s, reward from the first lick
    # within 3 s.
    fl3 = first_within(s, REWARD, 3)
    out["base05_cs1"] = np.nanmean(auc_python(t, x, cs1 - 0.5, (0, 0.5)))
    out["base05_all15"] = np.nanmean(auc_python(t, x, events(s, CUE1) - 0.5, (0, 0.5)))
    out["inh_bins"] = {b: np.nanmean(auc_python(t, x, cs2 + b, (0, 0.5))) for b in (-0.5, 0, 0.5, 1.0, 1.5)}
    out["rw05"] = np.nanmean(auc_python(t, x, fl3, (0, 0.5)))
    out["rw1"] = np.nanmean(auc_python(t, x, fl3, (0, 1.0)))
    out["n_first_lick3"] = int(np.isfinite(fl3).sum())
    return out


def random_session_reward(s):
    """Random reward session of Experiment 7: reward responses from the first lick within 3 s
    (Fig 6G) and within 5 s (Fig 6I), with the baselines of each script."""
    t, x = s["t"], s["dff"]
    rw = events(s, BGD_REWARD)
    fl3, fl5 = first_within(s, BGD_REWARD, 3), first_within(s, BGD_REWARD, 5)
    base05 = np.nanmean(auc_python(t, x, rw - 0.5, (0, 0.5)))
    return {"base05": base05, "rw05": np.nanmean(auc_python(t, x, fl3, (0, 0.5))),
            "rw1": np.nanmean(auc_python(t, x, fl3, (0, 1.0))),
            "rw_15": np.nanmean(np.array(auc_python(t, x, fl5, (0, 1.5)))
                                - np.array(auc_python(t, x, fl5, (-1.5, 0))))}


# ---------------------------------------------------------------------- conditions and checks

def session_condition(s):
    """What a session's event log shows of its condition: the task (session description), the
    cue-to-reward delays (s, rounded to 0.5 s), whether background rewards (code 7) occur, and
    the fraction of cue-associated reward events delivered."""
    out = {"task": s["description"], "n_bgd": int(np.sum(s["code"] == BGD_REWARD))}
    if s["description"] in ("Pavlovian", "Poisson") and np.any(s["code"] == REWARD) \
            and "stGtACR" not in s["subject"]:
        ev = pavlovian_events(s, trialless=s["description"] == "Poisson")
        d = np.round((ev["rw_time"] - ev["cs_time"]) * 2) / 2
        out["delays"] = sorted(set(d.tolist()))
        out["delivered"] = float(np.mean(ev["rewarded"]))
    return out


def clock_reference(s, csplus=None):
    """Events for the clock check and the contrast used. Random reward sessions: the first lick
    within 3 s after each reward (unpredicted). Experiments 2 to 5: CS+ against CS- onsets (the
    contrast between conditions). Experiment 6: cue onsets. Experiment 7 conditioning: CS1
    onsets."""
    code, t = s["code"], s["time"]
    if s["description"] == "RandomRewards":
        rw = t[code == BGD_REWARD]
        f = first_time_after(np.sort(events(s, LICK)), rw, within=3.0)
        return "first lick after reward", f[np.isfinite(f)], None
    if "stGtACR" in s["subject"]:
        return "CS1 onset", sequential_cues(s)[0], None
    if s["description"] == "Poisson":
        return "cue onset", t[np.isin(code, [CUE1, CUE2])], None
    cue = CUE1 if csplus == 1 else CUE2
    other = CUE2 if csplus == 1 else CUE1
    return "CS+ minus CS- onset", t[code == cue], t[code == other]


def response_profile(s, lags, csplus=None):
    """Mean dF/F from 0 to 1 s minus -1 to 0 s around the reference events of
    `clock_reference`, minus the same around the contrast events where there are any, with the
    event times shifted by each lag (s). If dF/F and the event log share a clock, the response
    peaks near lag 0 (within the response latency)."""
    ref, ev, ctrl = clock_reference(s, csplus)

    def resp(e):
        post = np.asarray(auc_python(s["t"], s["dff"], e, (0, 1)))
        pre = np.asarray(auc_python(s["t"], s["dff"], e, (-1, 0)))
        return np.nanmean(post - pre)

    out = []
    for lag in lags:
        v = resp(ev + lag)
        if ctrl is not None:
            v -= resp(ctrl + lag)
        out.append(v)
    return np.array(out), len(ev), ref
