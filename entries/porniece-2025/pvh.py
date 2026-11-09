"""Loading and measures for the PVH MC4R photometry data of dandiset 001474.

Porniece, Baker, Ausfahl, Zhang & Andermann (2025), Sci Rep 15, 35837,
doi:10.1038/s41598-025-19800-2.

Each NWB file holds one recording session. Under `acquisition` it holds per-trial matrices of
3001 samples (10 s before to 50 s after the tone, 50 Hz) by trial: `ensure_signal` (the pump
signal, about 3.26 while Ensure is delivered), `lick_signal` (0/1 per sample), `running_signal`
(cm/s) and `fiber_signal_zscore` (a Z-scored photometry signal computed by the depositors), and
the continuous `fiber_465_trace` (raw 465 nm fluorescence at 50 Hz, with the 5-min baseline).
Session facts are in `general/notes` as "key: value" lines: diet, condition (fasted or
nonfasted), ensure (consumed volume), bw (body weight on the day), ad lib bw, and for the
diet-switch recordings startdiet, 2nd_diet and before ad lib bw. There is no trial table and no
tone time stamps.

Files are read whole into memory over HTTPS from the archive at the pinned version (one GET per
file, about 1 s; `remfile` took about 30 s per file because the matrices are most of each
file). Nothing is written to disk.

Where the parameters come from:

- Sample 500 of each trial matrix is the tone (t = 0) and sample 550 the start of Ensure
  delivery (t = 1 s): the data show the pump signal rising at sample 550 in every delivered
  trial, and the Methods say trials are cut "60-s long traces beginning 10 s prior to the cue".
- A trial is triggered when the pump signal exceeds 1.0 after the tone (Methods, "we only
  selected the triggered trials"; the threshold is a standard choice between the pump's 0 and
  3.26 levels and cannot change which trials are found).
- Windows (claims file, opening comment): response windows 0-10, 1-10, 1-9 s, and 0-20, 1-20,
  1-19 s; F0 the mean of the 10 s before the tone (Methods); cue lick rate the licks in 0-1 s
  (Methods, "number of licks per second during the tone presentation"); reward-window lick
  rate 1-10 s (Methods).
- Z readings (claims file, opening comment). Z1: per trial (F - F0) / sigma, with sigma the SD
  of the mouse's recordings concatenated, each recording's fluorescence mean-subtracted from
  sample 50 on (tcpZ.m in the paper's code). Z2: per trial dF/F0 divided by the SD of the
  mouse's dF/F0 over all its trial samples concatenated. The Methods' "a single Z-score per
  animal" is read as one sigma per mouse over all its recordings in the dataset (both diet
  phases); Z1p and Z2p use one sigma per mouse and diet phase, a second reading of the same
  passage. Z0, the depositors' `fiber_signal_zscore`, is a variant, not a reading of the
  claims file.
- The raw trace is not filtered again: it holds no power above 10 Hz (shown in the notebook),
  so it has already had the Methods' 10 Hz low-pass.
- Trial onsets in the raw trace are not stored. They are found by correlating the raw trace
  with the deposited Z-score columns (each trial starts 3000 samples after the previous one).
  Where a file has no Z-score, or its Z-score does not match its raw trace (see
  ALIGN_MIN_R), the modal offset of the matched files with the same number of trials is used
  (an assumption: the session timing is the same; reported in the notebook). Every recording's
  trial starts are checked against the tone-evoked rise of the raw signal (`alignment_check`;
  the window 0.5-2 s against 2 s before the tone, and the 30-s and 5-trial search ranges, are
  standard choices for a check that decides no outcome).
"""

from __future__ import annotations

import io
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import requests

DANDISET_ID = "001474"
DANDISET_VERSION = "0.251031.1725"
API = "https://api.dandiarchive.org/api"

FS = 50
TONE = 500          # sample index of the tone in each trial matrix
DELIVERY = 550      # sample index of the start of Ensure delivery
TRIAL_STEP = 3000   # samples between trial starts (60 s inter-trial interval, Methods)
ENSURE_ON = 1.0     # pump signal threshold (standard choice)

# response windows in seconds after the tone
WINDOWS = {"0-10": (0, 10), "1-10": (1, 10), "1-9": (1, 9), "0-20": (0, 20), "1-20": (1, 20),
           "1-19": (1, 19)}
LICK_WINDOWS = {"cue": (0, 1), "rew": (1, 10), "rew19": (1, 9), "pre": (-10, 0), "post": (0, 50)}
RUN_WINDOWS = {"pre": (-10, 0), "whole": (-10, 50), "rew": (1, 10)}
ROLL_S = (1, 10, 60)
# Alignment of the deposited Z-score with the raw trace is accepted when the median
# correlation over trials exceeds ALIGN_MIN_R and the offset is within ALIGN_TOL samples of
# 5 min 5 s less 10 s (the 5-min baseline of the Methods); standard choices, the distribution
# of both is shown in the notebook.
LOST_FRACTION = 0.2
EXPECTED_OFFSET = 14771
ALIGN_MIN_R = 0.5
ALIGN_TOL = 25   # rolling SD windows, readings of the claims file (supp2j)


def sl(t0, t1):
    return slice(TONE + int(round(t0 * FS)), TONE + int(round(t1 * FS)))


def list_assets():
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=1000"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r["next"]
    return out


def parse_notes(text):
    d = {}
    for line in text.split("\n"):
        if ": " in line:
            k, v = line.split(": ", 1)
            d[k.strip()] = v.strip()
    return d


def _fetch(asset_id):
    for attempt in range(4):
        try:
            r = requests.get(f"{API}/assets/{asset_id}/download/", timeout=120)
            r.raise_for_status()
            return r.content
        except Exception:
            if attempt == 3:
                raise


def find_offset(raw, z):
    """Start sample of trial 0 in the raw trace, by correlation of the first Z-score column,
    then the lag of every column within +-3 samples of the 3000-sample grid."""
    c = z[:, 0]
    n = len(c)
    lim = min(len(raw) - n * 1, 60000)
    # sliding correlation via cumulative sums
    seg_len = n
    x = raw[: lim + seg_len]
    cs, cs2 = np.cumsum(np.r_[0, x]), np.cumsum(np.r_[0, x ** 2])
    m = (cs[seg_len:] - cs[:-seg_len]) / seg_len
    v = (cs2[seg_len:] - cs2[:-seg_len]) / seg_len - m ** 2
    cc = np.correlate(x, (c - c.mean()) / c.std(), mode="valid") / seg_len
    r = cc / np.sqrt(np.maximum(v, 1e-30))
    s0 = int(np.argmax(r[:lim]))
    lags, rs = [], []
    for j in range(z.shape[1]):
        best = (-2, 0)
        for d in range(-3, 4):
            t = s0 + TRIAL_STEP * j + d
            if t < 0 or t + n > len(raw):
                continue
            rr = np.corrcoef(raw[t:t + n], z[:, j])[0, 1]
            if rr > best[0]:
                best = (rr, d)
        rs.append(best[0])
        lags.append(best[1])
    return s0, np.array(lags), np.array(rs)


def load_one(asset):
    b = _fetch(asset["asset_id"])
    f = h5py.File(io.BytesIO(b), "r")
    acq = f["acquisition"]
    notes = parse_notes(f["general/notes"][()].decode())
    rec = {
        "path": asset["path"], "asset_id": asset["asset_id"], "blob": asset.get("blob"),
        "identifier": f["identifier"][()].decode(),
        "subject": f["general/subject/subject_id"][()].decode(),
        "sex": f["general/subject/sex"][()].decode(),
        "start": f["session_start_time"][()].decode(),
        "description": f["session_description"][()].decode(),
        "notes": notes, "series": sorted(acq.keys()),
        "rates": {k: float(acq[k]["starting_time"].attrs.get("rate", np.nan)) for k in acq},
        "units": {k: acq[k]["data"].attrs.get("unit") for k in acq},
    }
    ens = acq["ensure_signal"]["data"][()]
    lick = acq["lick_signal"]["data"][()]
    ntr = ens.shape[1]
    rec["n_trials"] = ntr
    rec["n_samples"] = ens.shape[0]
    rec["triggered"] = (ens[TONE:] > ENSURE_ON).any(axis=0)
    on = np.array([int(np.argmax(c > ENSURE_ON)) if (c > ENSURE_ON).any() else -1 for c in ens.T])
    rec["ensure_onset"] = on
    rec["ensure_range"] = (float(ens.min()), float(ens.max()))
    rec["lick_values"] = np.unique(lick).tolist()
    rec["lick"] = {k: lick[sl(*w)].sum(axis=0) / (w[1] - w[0]) for k, w in LICK_WINDOWS.items()}
    # lick rate curve in 1-s bins from -10 to 50 s, for the AUC readings
    rec["lick_1s"] = lick[:3000].reshape(60, FS, ntr).sum(axis=1)
    if "running_signal" in acq:
        run = acq["running_signal"]["data"][()]
        # the running signal is signed (direction on the treadmill); speed is its absolute
        # value, the signed mean is kept as a variant
        rec["run"] = {k: np.abs(run[sl(*w)]).mean(axis=0) for k, w in RUN_WINDOWS.items()}
        rec["run_signed"] = {k: run[sl(*w)].mean(axis=0) for k, w in RUN_WINDOWS.items()}
        rec["run_neg_fraction"] = float((run < 0).mean())
        rec["run_range"] = (float(run.min()), float(run.max()))
    z = acq["fiber_signal_zscore"]["data"][()] if "fiber_signal_zscore" in acq else None
    if z is not None:
        rec["z0"] = {k: z[sl(*w)].mean(axis=0) for k, w in WINDOWS.items()}
        rec["z0_pre"] = z[:TONE].mean(axis=0)
        rec["z0_range"] = (float(z.min()), float(z.max()))
        rec["z0_allmean"], rec["z0_allsd"] = float(z.mean()), float(z.std())
    if "fiber_465_trace" in acq:
        raw = acq["fiber_465_trace"]["data"][:, 0]
        rec["raw_len"] = len(raw)
        rec["raw_nan"] = int(np.isnan(raw).sum())
        rec["raw_range"] = (float(np.nanmin(raw)), float(np.nanmax(raw)))
        # NaN samples (a few files start with some) are filled for alignment and the spectrum
        # only; the measures ignore them
        filled = pd.Series(raw).interpolate(limit_direction="both").to_numpy()
        f_, p_ = _psd(filled)
        rec["raw_power_above10"] = float(p_[f_ > 10.5].sum() / p_.sum())
        if z is not None:
            s0, lags, rs = find_offset(filled, z)
            rec["offset"], rec["lags"], rec["align_r"] = s0, lags, rs
        rec["_raw"] = raw
    return rec


def _psd(x):
    from scipy.signal import welch
    return welch(x, fs=FS, nperseg=1024)


TONE_LAGS = np.arange(-1500, 1501, 5)   # alignment check, -30 to 30 s in 0.1-s steps


def tone_contrast(raw, t):
    """Per tone time t (sample of the tone; any shape), the mean signal 0.5-2 s after it over
    the mean of the 2 s before it, minus 1; NaN where the window leaves the trace. The tone
    itself evokes a fast rise of the signal in triggered and untriggered trials alike (shown in
    the notebook), so this marks where the tones are in the raw trace."""
    x = pd.Series(raw).interpolate(limit_direction="both").to_numpy()
    c = np.r_[0, np.cumsum(x)]
    ok = (t - 2 * FS >= 0) & (t + 2 * FS <= len(x))
    tt = np.where(ok, t, 2 * FS)
    pre = (c[tt] - c[tt - 2 * FS]) / (2 * FS)
    post = (c[tt + 2 * FS] - c[tt + FS // 2]) / (1.5 * FS)
    return np.where(ok, post / pre - 1, np.nan)


def alignment_check(raw, starts, good, k=5):
    """Checks of the trial starts used for the raw measures. (a) The tone response averaged over
    the recording's trials, with every tone time shifted by each lag of TONE_LAGS: with the
    right starts it peaks within a fraction of a second of lag 0. (b) The tone response at the
    k tone slots of the 60-s grid before the first trial and after the last one, against the
    first and last k trials: with the right trial count it is absent outside the trials (the
    5-min baseline holds no tones)."""
    tones = starts + TONE
    v = tone_contrast(raw, tones[good][:, None] + TONE_LAGS[None, :])
    scan = np.nanmean(v, axis=0)
    before = tone_contrast(raw, tones[0] - TRIAL_STEP * np.arange(k, 0, -1))
    after = tone_contrast(raw, tones[-1] + TRIAL_STEP * np.arange(1, k + 1))
    inside = tone_contrast(raw, tones)
    return {"scan": scan, "before": before, "first": inside[:k], "last": inside[-k:], "after": after}


def raw_measures(rec, s0):
    """Per-trial F - F0 and dF/F0 window means from the raw trace, and the per-recording sums
    for the per-mouse SDs of Z1 and Z2."""
    raw = rec.pop("_raw")
    ntr, n = rec["n_trials"], rec["n_samples"]
    starts = s0 + TRIAL_STEP * np.arange(ntr)
    ok = starts + n <= len(raw)
    seg = np.full((n, ntr), np.nan)
    for j in np.where(ok)[0]:
        seg[:, j] = raw[starts[j]:starts[j] + n]
    # trials where the signal drops to near zero (lost signal) are left out of the raw measures:
    # any sample below LOST_FRACTION of the recording's median F0 (a standard choice; counted
    # in the notebook)
    F0 = np.nanmean(seg[:TONE], axis=0)
    lost = np.nanmin(seg, axis=0) < LOST_FRACTION * np.nanmedian(F0)
    seg[:, lost] = np.nan
    rec["lost"] = lost & ok
    F0 = np.nanmean(seg[:TONE], axis=0)
    dF = seg - F0
    dff = dF / F0
    rec["raw_ok"] = ok
    rec["F0"] = F0
    rec["raw_tail_s"] = (len(raw) - (s0 + TRIAL_STEP * ntr)) / FS
    good = ok & ~lost
    trg = rec["triggered"][:ntr] & good
    utr = ~rec["triggered"][:ntr] & good
    # mean dF/F0 trace of triggered and untriggered trials, -10 to 50 s, at 10 Hz (alignment check)
    rec["avg_trig"] = np.nanmean(dff[:3000, trg], axis=1).reshape(-1, 5).mean(axis=1) if trg.any() else None
    rec["avg_untrig"] = np.nanmean(dff[:3000, utr], axis=1).reshape(-1, 5).mean(axis=1) if utr.any() else None
    rec["align_check"] = alignment_check(raw, starts, good)
    rec["dF"] = {k: np.nanmean(dF[sl(*w)], axis=0) for k, w in WINDOWS.items()}
    rec["dff"] = {k: np.nanmean(dff[sl(*w)], axis=0) for k, w in WINDOWS.items()}
    # Z1 sigma (tcpZ.m): trace from sample 50 on, mean-subtracted per recording
    x = raw[50:][~np.isnan(raw[50:])]
    x = x[x >= LOST_FRACTION * np.nanmedian(F0)]   # lost-signal samples left out, as above
    x = x - x.mean()
    rec["z1_n"], rec["z1_ss"] = len(x), float((x ** 2).sum())
    # Z2 sigma: dF/F0 over all trial samples
    v = dff[:, ok & ~lost]
    v = v[~np.isnan(v)]
    rec["z2_n"], rec["z2_s"], rec["z2_ss"] = v.size, float(v.sum()), float((v ** 2).sum())
    # pre-Ensure spontaneous variability (supp2j): from the start of the recording to the first
    # Ensure delivery
    trig = np.where(rec["triggered"])[0]
    if len(trig):
        end = int(starts[trig[0]] + DELIVERY)
        pre = raw[:end]
        d = (pre - np.nanmean(pre)) / np.nanmean(pre)
        s = pd.Series(d)
        rec["pre_ensure_s"] = end / FS
        rec["roll_sd"] = {w: float(s.rolling(w * FS).std().mean()) for w in ROLL_S}
    return rec


def load_all(workers=8):
    assets = list_assets()
    with ThreadPoolExecutor(workers) as ex:
        recs = list(ex.map(load_one, assets))
    # trial offset for files without the deposited Z-score: modal offset per trial count
    for r in recs:
        if "offset" in r:
            r["z_raw_match"] = bool(np.median(r["align_r"]) > ALIGN_MIN_R
                                    and abs(r["offset"] - EXPECTED_OFFSET) <= ALIGN_TOL)
            if not r["z_raw_match"]:
                r["offset_corr"] = r.pop("offset")
    have = pd.DataFrame([(r["n_trials"], r["offset"]) for r in recs if "offset" in r],
                        columns=["n", "off"])
    modal = have.groupby("n").off.agg(lambda s: s.mode().iloc[0]).to_dict()
    overall = int(have.off.mode().iloc[0])
    for r in recs:
        if "_raw" in r:
            if "offset" in r:
                s0, r["offset_source"] = r["offset"], "correlation"
            else:
                s0 = int(modal.get(r["n_trials"], overall))
                r["offset"], r["offset_source"] = s0, "modal"
            raw_measures(r, s0)
    return recs


def sessions_table(recs):
    rows = []
    for r in recs:
        n = r["notes"]
        rows.append({
            "path": r["path"], "blob": r["blob"], "subject": r["subject"], "sex": r["sex"],
            "date": r["start"][:10], "identifier": r["identifier"], "n_trials": r["n_trials"],
            "n_triggered": int(r["triggered"].sum()), "diet": n.get("diet"),
            "startdiet": n.get("startdiet"), "seconddiet": n.get("2nd_diet"), "rig": n.get("rig"),
            "condition": n.get("condition"), "ensure": float(n["ensure"]) if "ensure" in n else np.nan,
            "bw": float(n["bw"]) if "bw" in n else np.nan,
            "adlib_bw": float(n["ad lib bw"]) if "ad lib bw" in n else np.nan,
            "before_adlib_bw": float(n["before ad lib bw"]) if "before ad lib bw" in n else np.nan,
            "has_z0": "z0" in r, "has_raw": "F0" in r, "has_run": "run" in r,
            "offset": r.get("offset"), "offset_source": r.get("offset_source"),
            "z_raw_match": r.get("z_raw_match"),
        })
    return pd.DataFrame(rows)


def phase_of(r):
    return "second" if "startdiet" in r["notes"] else "first"


def add_z(recs, mouse_of=lambda r: r["subject"], suffix=""):
    """Z1 and Z2 per trial, with one sigma per mouse over all its recordings in `recs`.
    With mouse_of = subject and phase, and suffix "p", the per-phase readings Z1p, Z2p."""
    acc = {}
    for r in recs:
        if "F0" not in r:
            continue
        a = acc.setdefault(mouse_of(r), [0, 0.0, 0, 0.0, 0.0])
        a[0] += r["z1_n"]; a[1] += r["z1_ss"]
        a[2] += r["z2_n"]; a[3] += r["z2_s"]; a[4] += r["z2_ss"]
    sig = {}
    for m, (n1, ss1, n2, s2, ss2) in acc.items():
        sig[m] = (np.sqrt(ss1 / n1), np.sqrt(ss2 / n2 - (s2 / n2) ** 2))
    for r in recs:
        if "F0" not in r:
            continue
        s1, s2 = sig[mouse_of(r)]
        r["z1" + suffix] = {k: v / s1 for k, v in r["dF"].items()}
        r["z2" + suffix] = {k: v / s2 for k, v in r["dff"].items()}
        r["sigma1" + suffix], r["sigma2" + suffix] = s1, s2
    return sig


def trig_values(r, z, w):
    """Per-triggered-trial response values of a recording under reading z (z0, z1, z2, dff)
    and window w, in trial order."""
    if z not in r:
        return None
    v = np.asarray(r[z][w])[r["triggered"]]
    return v


def phase_means(v, k=15):
    """Early (first k) and late (last k) triggered-trial means."""
    return np.nanmean(v[:k]), np.nanmean(v[-k:])


# z1, z2: the claims file's Z readings with one sigma per mouse over all its recordings;
# z1p, z2p: the same with one sigma per mouse and diet phase (the Methods' "a single Z-score
# per animal" does not say whether the second-diet recordings are included); z0 deposited
READINGS = ("z1", "z2", "z1p", "z2p", "z0", "dff")


def session_groups(recs):
    """Sessions table with duplicates marked and experiment groups.

    Cohort 1: subjects MPK118 to MPK148 (60-trial sessions), cohort 2: MPK172 to MPK191
    (90-trial sessions; files with 89 columns lack the last trial). The diet-switch second
    phase is the files whose notes have startdiet and 2nd_diet; their first phase is the same
    mice's cohort recordings (Fig. 3 legend counts match these mice, shown in the notebook).
    """
    T = sessions_table(recs)
    T["duplicate"] = T.path.str.contains("ses-None") & T.blob.duplicated(keep=False)
    T["num"] = T.subject.str[3:].astype(int)
    T["phase"] = np.where(T.startdiet.notna(), "second", "first")
    T["cohort"] = np.where(T.num <= 148, 1, 2)
    cond = {}
    for _, r in T[T.phase == "second"].iterrows():
        cond[r.subject] = f"{r.startdiet}->{r.seconddiet}"
    T["switch"] = T.subject.map(cond)
    T.loc[T.switch == "NCD->HFD", "switch"] = "NCD->HFD6w"
    return T


def _tv(v, trig):
    """Values on triggered trials. Some files hold one more trial column in one series than in
    the Ensure matrix (counted in the notebook); trials beyond the shorter are dropped."""
    v = np.asarray(v, float)
    m = min(len(v), len(trig))
    return v[:m][trig[:m]]


def column_counts(r):
    out = {"ensure": len(r["triggered"]), "lick": len(r["lick"]["cue"])}
    if "run" in r:
        out["running"] = len(r["run"]["pre"])
    if "z0" in r:
        out["zscore"] = len(r["z0"]["1-10"])
    return out


def recording_measures(recs, T):
    """One row per recording: early, late, mid-meal, D5, D15 and first-trial values for each
    response reading and window, and the lick and running measures over triggered trials."""
    by_path = {r["path"]: r for r in recs}
    rows = []
    for _, t in T.iterrows():
        r = by_path[t.path]
        trig = r["triggered"]
        row = t.to_dict()
        for z in READINGS:
            if z not in r:
                continue
            for w in WINDOWS:
                v = _tv(r[z][w], trig)
                if len(v) == 0:
                    continue
                row[f"{z}|{w}|early"] = np.nanmean(v[:15])
                row[f"{z}|{w}|late"] = np.nanmean(v[-15:])
                row[f"{z}|{w}|mid"] = np.nanmean(v[14:29]) if len(v) >= 15 else np.nan
                row[f"{z}|{w}|D5"] = np.nanmean(v[-5:]) - np.nanmean(v[:5])
                row[f"{z}|{w}|D15"] = row[f"{z}|{w}|late"] - row[f"{z}|{w}|early"]
                row[f"{z}|{w}|all"] = np.nanmean(v)
        for k, v in r["lick"].items():
            v = _tv(v, trig)
            row[f"lick_{k}|all"] = v.mean() if len(v) else np.nan
            row[f"lick_{k}|early"] = v[:15].mean() if len(v) else np.nan
            row[f"lick_{k}|late"] = v[-15:].mean() if len(v) else np.nan
            row[f"lick_{k}|mid"] = v[14:29].mean() if len(v) >= 15 else np.nan
            row[f"lick_{k}|first"] = v[0] if len(v) else np.nan
        if "run" in r:
            for k, v in r["run"].items():
                v = _tv(v, trig)
                row[f"run_{k}|all"] = v.mean() if len(v) else np.nan
                row[f"run_{k}|early"] = v[:15].mean() if len(v) else np.nan
                row[f"run_{k}|late"] = v[-15:].mean() if len(v) else np.nan
            for k, v in r["run_signed"].items():
                v = _tv(v, trig)
                row[f"runsigned_{k}|all"] = v.mean() if len(v) else np.nan
                row[f"runsigned_{k}|early"] = v[:15].mean() if len(v) else np.nan
                row[f"runsigned_{k}|late"] = v[-15:].mean() if len(v) else np.nan
        if "roll_sd" in r:
            for w, v in r["roll_sd"].items():
                row[f"rollsd_{w}s"] = v
        rows.append(row)
    return pd.DataFrame(rows)


def per_trial_index(recs, paths, key, n=90):
    """Matrix recordings x trial index (1..n) of a per-trial measure on triggered trials, NaN
    for untriggered trials (the figures' per-trial curves use triggered trials only)."""
    by_path = {r["path"]: r for r in recs}
    out = np.full((len(paths), n), np.nan)
    for i, p in enumerate(paths):
        r = by_path[p]
        group, k = key
        v = np.asarray(r[group][k], float)
        m = min(n, len(v), len(r["triggered"]))
        vv = np.where(r["triggered"][:m], v[:m], np.nan)
        out[i, :m] = vv
    return out
