"""Loading and measures for dandiset 001256 (Cody, Kumar & Tzounopoulos 2024, J Neurosci,
doi:10.1523/JNEUROSCI.0939-23.2024).

Each NWB file holds one mouse and one experiment. A trial is one two-photon .tif file: the
stimulus table (`stimulus/presentation/stim param table`) gives per trial the .tif file, its start
time, the sound (`pulseNames`, `pulseSets`), the delay to sound onset (`stimDelay`, s) and the
treatment (none, preZX1, postZX1, preACSF, postACSF). Each trial has a pupil radius series
(`processing/behavior/PupilTracking/pupil_radius_NNN`, 10 Hz, matched to its trial by the .tif file
named in its `comments`) and an ROI fluorescence series
(`processing/ophys/Fluorescence/RoiResponseSeries_NNN`, 5 Hz, frames x ROIs, matched by the
TwoPhotonSeries it names). Files are streamed from the archive at the pinned version; nothing is
written to disk. Only the pupil and fluorescence of sound trials are read; the videos and raw
two-photon frames are not.

Where the parameters come from:

- Trial kinds. `pulseSets` starting with `PC_PTinContrast` is the CGC assay (DRC with a 70 dB
  pure tone at 2 s, Methods "CGC assay"); `PC_contrastChange` is the DRC without a tone used for
  the sound-evoked pupil analyses (Methods, "DRC sound stimuli": "For sound-evoked pupil response
  analyses, DRC stimuli did not include a pure tone"). In the files these DRCs are 10 s of one
  contrast followed by 10 s of the other (`50-60dB_to_40-70dB` or the reverse); the paper does not
  describe the switch. A trial's contrast is that of its first 10 s (assumption: the analyses use
  0 to 2 s, or at most 0 to 8 s, from sound onset, all inside the first block).
  Contrast: 50-60 dB SPL low, 40-70 dB SPL high (Methods, "DRC sound stimuli").
- Sound onset is `stimDelay` seconds after the trial's first frame (the table's description,
  "delay to start of pulses in seconds"); the pupil video starts 4 s before sound onset (Methods,
  "Pupillometry: acquisition"), consistent with stimDelay = 4 s.
- Pupil preprocessing (Methods, "Pupillometry: analysis"): remove frames whose first derivative is
  a > 6 SD outlier, interpolate missing points linearly, low-pass filter (third order Butterworth,
  3 Hz). The filter is run zero-phase (`filtfilt`), a standard choice the claims file names. The
  files hold the pupil radius; the radius is proportional to the diameter, so % baseline and %
  animal max are the same for both.
- Evoked pupil (Methods): trace / mean over -4 to 0 s x 100. Baseline PD in % animal max: trace as
  % of the animal's maximum over all its sound trials (the paper: "the animal's maximum PD during
  the experiment"), averaged over -4 to 0 s.
- Baseline PD bins (claims file, shared methods): < 21, 21-32, 32-43, 43-54, 54-65, 65-76, > 76.
- dF/F (Methods, "2PCI processing and analysis"): (F - F0_DRC) / F0_DRC x 100 with F0_DRC the mean
  over -1.2 to 0 s; pure-tone response F(t) - F0_PT with F0_PT the mean over 1 to 2 s. Frame k
  of a trial is at time k / 5 - stimDelay s from sound onset; windows are half open [a, b).
- Peak windows: [2.0, 2.8) s (800 ms after tone onset) and [2.0, 3.2) s (claims file readings).
"""

from __future__ import annotations

import re
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy.signal import butter, filtfilt

DANDISET_ID = "001256"
DANDISET_VERSION = "0.241120.2150"
API = "https://api.dandiarchive.org/api"

PUPIL_HZ = 10.0
TWOP_HZ = 5.0
BIN_EDGES = [21, 32, 43, 54, 65, 76]  # claims file, shared methods
BIN_LABELS = ["<21", "21-32", "32-43", "43-54", "54-65", "65-76", ">76"]


def list_assets():
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=200"
    out = requests.get(url, timeout=60).json()["results"]
    return pd.DataFrame([{"asset_id": a["asset_id"], "path": a["path"], "size": a["size"]} for a in out])


def _s(v):
    v = v[()] if hasattr(v, "shape") else v
    return v.decode() if isinstance(v, bytes) else v


def _open(asset_id):
    url = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60).url
    return h5py.File(remfile.File(url), "r")


def trial_kind(pulse_set):
    if pulse_set.startswith("PC_PTinContrast"):
        return "pt"
    if pulse_set.startswith("PC_contrastChange"):
        return "drc"
    if pulse_set.startswith("PC_TestTones"):
        return "map"
    return "led"


def trial_contrast(pulse_name):
    """Contrast of the first DRC block: 50-60 dB low, 40-70 dB high."""
    m = re.search(r"kHz_(\d\d-\d\d)dB", pulse_name)
    if not m:
        return None
    return {"50-60": "LOW", "40-70": "HIGH"}.get(m.group(1))


def load_file(asset_id):
    """Read the metadata, stimulus table, pupil of sound trials and fluorescence of CGC trials."""
    f = _open(asset_id)
    g = f["general"]
    meta = {
        "subject": _s(g["subject/subject_id"]),
        "genotype": _s(g["subject/genotype"]),
        "sex": _s(g["subject/sex"]),
        "age": _s(g["subject/age"]),
        "session_description": _s(f["session_description"]),
        "session_start": _s(f["session_start_time"]),
    }
    t = f["stimulus/presentation/stim param table"]
    tab = pd.DataFrame({c: [_s(x) for x in t[c][:]] for c in t.attrs["colnames"]})
    tab["kind"] = tab.pulseSets.map(trial_kind)
    tab["contrast"] = tab.pulseNames.map(trial_contrast)
    pt = f["processing/behavior/PupilTracking"]
    pupil_by_tif = {}
    for k in pt:
        m = re.search(r"associated \.tif file: (\S+\.tif)", pt[k].attrs.get("comments", ""))
        pupil_by_tif[m.group(1)] = k
    fl = f["processing/ophys/Fluorescence"]
    fl_by_series = {}
    for k in fl:
        m = re.search(r"(TwoPhotonSeries_\d+)", fl[k].attrs.get("description", ""))
        fl_by_series[m.group(1)] = k
    pupils, fluos, planes, n_pupil_frames = [], [], [], []
    for _, row in tab.iterrows():
        pk = pupil_by_tif.get(row.file)
        if row.kind in ("pt", "drc") and pk is not None:
            p = pt[pk]["data"][:]
            pupils.append(p)
            assert abs(float(pt[pk]["starting_time"][()]) - float(row.starting_time)) < 1e-3
        else:
            pupils.append(None)
        n_pupil_frames.append(pt[pk]["data"].shape[0] if pk is not None else 0)
        if row.kind == "pt":
            fk = fl_by_series[row.TwoPhotonSeries]
            fluos.append(fl[fk]["data"][:])
            planes.append(f[fl[fk]["rois"].attrs["table"]].name.split("/")[-1])
        else:
            fluos.append(None)
            planes.append(None)
    tab["pupil"] = pupils
    tab["F"] = fluos
    tab["plane"] = planes
    tab["n_pupil"] = n_pupil_frames
    tab["trial_id"] = meta["subject"] + "/" + tab.file
    for k, v in meta.items():
        tab[k] = v
    return meta, tab


def load_all(assets, workers=8):
    with ProcessPoolExecutor(workers) as ex:
        res = list(ex.map(load_file, assets.asset_id))
    meta = pd.DataFrame([r[0] for r in res])
    meta["path"] = list(assets.path)
    trials = pd.concat([r[1] for r in res], ignore_index=True)
    return meta, trials


# ---------------------------------------------------------------- pupil


_B, _A = butter(3, 3.0 / (PUPIL_HZ / 2), btype="low")


def hampel(p, half=5, k=6.0):
    """Mark as NaN samples further than k robust SDs (1.4826 x MAD of the deviations over the
    trace) from the running median of 2 x half + 1 samples. Not in the paper (see clean_pupil)."""
    s = pd.Series(p)
    med = s.rolling(2 * half + 1, center=True, min_periods=3).median()
    dev = (s - med).abs()
    mad = 1.4826 * np.nanmedian(dev)
    out = p.copy()
    if np.isfinite(mad) and mad > 0:
        out[(dev > k * mad).values] = np.nan
    return out


def clean_pupil(p, max_pass=10, spike_filter=True, max_missing=0.5):
    """Methods: drop > 6 SD outliers of the first derivative, interpolate linearly, 3 Hz low-pass.

    The derivative is taken between consecutive tracked frames (frames the circle fit dropped are
    NaN in the files), both frames of an outlier jump are dropped, and the step is repeated until
    no outlier remains (at most `max_pass` times). The paper describes one pass. The files keep
    tracking failures (single frames and runs of frames at 3 to 1e6 times the pupil size, often
    next to dropped frames) that one pass does not remove, so two steps are added, as an
    assumption stated in the notebook: a Hampel filter first (`spike_filter`), and trials with
    more than `max_missing` (half) of their frames missing or removed are dropped (None).
    `max_pass=1, spike_filter=False, max_missing=1` gives the paper's single pass.
    """
    p = np.asarray(p, float).copy()
    if spike_filter:
        p = hampel(p)
    for _ in range(max_pass):
        idx = np.where(np.isfinite(p))[0]
        if len(idx) < 4:
            return None
        d = np.diff(p[idx])
        sd = d.std()
        if sd == 0:
            break
        bad = np.where(np.abs(d - d.mean()) > 6 * sd)[0]
        if len(bad) == 0:
            break
        p[idx[bad]] = np.nan
        p[idx[bad + 1]] = np.nan
    x = np.arange(len(p))
    good = np.isfinite(p)
    if good.sum() < 4 or (1 - good.mean()) > max_missing:
        return None
    p = np.interp(x, x[good], p[good])
    return filtfilt(_B, _A, p)


def pupil_measures(trials, **clean):
    """Add cleaned pupil, baseline PD (% animal max), and evoked windows to sound trials."""
    tr = trials[trials.pupil.notna()].copy()
    # a pupil series must have two video frames per two-photon frame (10 and 5 Hz)
    tr = tr[tr.pupil.map(len) == 2 * tr.nFrames.astype(int)]
    tr["pclean"] = [clean_pupil(p, **clean) for p in tr.pupil]
    tr = tr[tr.pclean.notna()].copy()
    animal_max = tr.groupby("subject").pclean.apply(lambda s: max(np.max(x) for x in s))
    out = []
    for _, r in tr.iterrows():
        p = r.pclean
        t = np.arange(len(p)) / PUPIL_HZ - float(r.stimDelay)
        base = p[(t >= -4) & (t < 0)].mean()
        ev = p / base * 100
        out.append({
            "base_pct_max": base / animal_max[r.subject] * 100,
            "ev_0_8": ev[(t >= 0) & (t < 8)].mean(),
            "ev_1_2": ev[(t >= 1) & (t < 2)].mean(),
            "ev_0_2": ev[(t >= 0) & (t < 2)].mean(),
            "ev_trace_0_2": ev[(t >= 0) & (t <= 2.0 + 1e-9)],
            "ev_trace": ev,
            "t": t,
            "file_time": pd.Timestamp(r.fileTimeInstantiate) + pd.Timedelta(seconds=float(r.stimDelay)),
        })
    tr = pd.concat([tr.reset_index(drop=True), pd.DataFrame(out)], axis=1)
    # Recording time from the .tif creation times (`fileTimeInstantiate`), in minutes from the
    # experiment's first sound trial. The table's `starting_time` is not used: in files whose
    # reference .tif is a mapping file recorded mid-experiment, trials recorded before it have
    # starting times near 86400 s (a negative offset wrapped by one day).
    first = tr.groupby("subject").file_time.transform("min")
    tr["rec_min"] = (tr.file_time - first).dt.total_seconds() / 60.0
    tr["treat"] = tr.treatment.map({"none": "CTRL", "preZX1": "CTRL", "preACSF": "CTRL",
                                    "postZX1": "ZX1", "postACSF": "ACSF"})
    return tr


def pd_bin(base, lower_edge=None):
    """Bin index 0..6 of a baseline PD (% animal max); NaN below `lower_edge` when given."""
    b = np.digitize(base, BIN_EDGES)
    if lower_edge is not None:
        b = np.where(np.asarray(base) < lower_edge, -1, b)
    return b


# ---------------------------------------------------------------- calcium


def frame_times(n, delay):
    return np.arange(n) / TWOP_HZ - float(delay)


def dff(F, delay):
    """% dF/F with F0_DRC the mean over -1.2 to 0 s (frames x cells)."""
    t = frame_times(F.shape[0], delay)
    f0 = F[(t >= -1.2) & (t < 0)].mean(0)
    return (F - f0) / f0 * 100, t


def pt_response(F, delay):
    """Pure-tone response trace F(t) - F0_PT, F0_PT the mean of dF/F over 1 to 2 s."""
    d, t = dff(F, delay)
    return d - d[(t >= 1) & (t < 2)].mean(0), t


def cell_trial_table(pt_trials, windows=((2.0, 2.8), (2.0, 3.2))):
    """Per cell and trial: the pure-tone response trace, trial peak in each window and the
    0-2 s DRC response.

    A cell is (subject, plane, roi index); ROIs of PlaneSegmentation_preZX1 and _postZX1 are
    different segmentations and are treated as different cells.
    """
    rows = []
    for _, r in pt_trials.iterrows():
        F = np.asarray(r.F, float)
        resp, t = pt_response(F, r.stimDelay)
        d, _ = dff(F, r.stimDelay)
        drc02 = d[(t >= 0) & (t < 2)].mean(0)
        for c in range(F.shape[1]):
            row = {"subject": r.subject, "plane": r.plane, "roi": c, "trial": r.trial_id,
                   "contrast": r.contrast, "treat": r.treat, "drc_0_2": drc02[c],
                   "base_mean_dff": d[(t >= 1) & (t < 2), c].mean(),
                   "trace": resp[:, c], "t": t}
            for a, b in windows:
                row[f"peak_{a}_{b}"] = resp[(t >= a) & (t < b), c].max()
            rows.append(row)
    ct = pd.DataFrame(rows)
    ct["cell"] = ct.subject + "/" + ct.plane + "/" + ct.roi.astype(str)
    return ct


def responsive(ct, window=(2.0, 2.8), sd="time", by_contrast=True):
    """Cells significantly responsive to the pure tone (Methods): the maximum of the trial-
    averaged response in `window` >= 2 SD above the baseline average (1 to 2 s, which is 0 after
    the F0_PT subtraction). SD readings: 'time', the SD over time of the trial-averaged trace in
    1-2 s; 'trials', the SD across trials of the trial baseline means of dF/F (before F0_PT
    subtraction the baseline mean varies by trial). d' >= 0 (mean response >= mean baseline) is
    applied too. With `by_contrast`, a cell must pass in LOW and in HIGH; else trials of both
    contrasts are pooled. Returns the set of cell ids.
    """
    keep = set()
    groups = ["cell", "contrast"] if by_contrast else ["cell"]
    res = {}
    for key, g in ct.groupby(groups):
        tr = np.vstack(g.trace.values)
        t = g.t.iloc[0]
        avg = tr.mean(0)
        wmask = (t >= window[0]) & (t < window[1])
        bmask = (t >= 1) & (t < 2)
        peak = avg[wmask].max()
        if sd == "time":
            s = avg[bmask].std(ddof=1)
        else:
            s = g.base_mean_dff.std(ddof=1) if len(g) > 1 else np.nan
        dprime_ok = tr[:, wmask].max(1).mean() >= tr[:, bmask].mean()
        res[key] = (peak >= avg[bmask].mean() + 2 * s) and dprime_ok
    if by_contrast:
        cells = {}
        for (cell, con), ok in res.items():
            cells.setdefault(cell, []).append(ok)
        keep = {c for c, v in cells.items() if len(v) == 2 and all(v)}
    else:
        keep = {c[0] if isinstance(c, tuple) else c for c, ok in res.items() if ok}
    return keep


# ---------------------------------------------------------------- growth curve analysis


def orth_poly(t, degree=2):
    """Orthogonal polynomials over the time samples with unit-norm columns, as R poly()."""
    t = np.asarray(t, float)
    X = np.vander(t - t.mean(), degree + 1, increasing=True)
    q, r = np.linalg.qr(X)
    q = q * np.sign(np.diag(r))
    return q[:, 1:]


def gca_long(tr, extra=()):
    """Long table: one row per trial and time sample 0..2 s (pupil % baseline)."""
    rows = []
    tt = np.round(np.arange(0, 2.0001, 1 / PUPIL_HZ), 3)
    P = orth_poly(tt)
    for _, r in tr.iterrows():
        y = r.ev_trace_0_2
        if len(y) != len(tt):
            continue
        d = pd.DataFrame({"pupil": y, "tPoly1": P[:, 0], "tPoly2": P[:, 1], "time": tt})
        d["subject"] = r.subject
        d["trial"] = r.trial_id
        for c in ("contrast", "treat", "genotype") + tuple(extra):
            d[c] = r[c]
        rows.append(d)
    return pd.concat(rows, ignore_index=True)
