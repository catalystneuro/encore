"""Membrane charging by 2-us pulses from the strobe images of DANDI:001273 (Figure 4 of Semenov et al. 2025).

The claim fig4-pooled-time-constants of claims/001272/10.1016-j.xcrp.2025.102660.yaml defers its fits
and readings to the claims file for DANDI:001273 (claims/001273/10.1016-j.xcrp.2025.102660.yaml),
whose header items are cited here as 001273-F1 to F4 and 001273-O1 to O3.

Each file is one replicate: 160 full-sensor frames (512 x 512) at 50-ns steps, recorded forward or
backward in time (the session description says which). Replicates of one cell, electrode orientation
and amplitude form an experiment.

Where each parameter comes from:

- DANDISET, VERSION: the most recent published version (the paper cites none).
- STEP_US = 0.05, PRE_US = 1.0, PULSE_US = 2.0: the 50-ns steps, 1 us before the pulse and the 2-us
  pulse (Methods, Pulsed laser fluorescence microscopy; the files' descriptions). The frame at the
  pulse onset is checked against the data in the notebook.
- Backward recordings are reversed so that every replicate runs forward in time (file descriptions).
- The first acquired frame of every file is dark (about 0.55 of the median); it is left out. Standard
  choice, shown in the notebook.
- ratio_image: 001273 claims header and the Methods: the mean of the frames in the last 0.5 us of the
  pulse over the CONTROL image (frames before the pulse and from 4 us after its end), both low-pass
  filtered over 12 x 12 pixels.
- cell_mask: the pixels of the 12 x 12 filtered CONTROL image above its Otsu threshold, largest
  connected component. A standard choice; the paper draws ROIs by eye.
- roi_masks: 001273-O1 readings (a) a 12 x 12 square centred on the extreme pixel of each sign within
  the cell, (b) the pixels within the cell beyond half the extreme of each sign.
- dF = 100 (F - F0) / F0 per frame, F0 the mean of the frames before the pulse (001273-F1). The fitted
  trace is the mean over replicates (001273-F3). Unscaled: the debris ROI of 001273-F2 is not deposited.
- fit_tau: 001273-F4, charging dF = A (1 - exp(-t/tau)) over the pulse, discharging dF = B exp(-t/tau)
  after it; 001273-O2 weighting (a) none, (b) 1/SEM^2 of the replicate mean; 001273-O3 discharge
  amplitude (a) free, (b) fixed at the charging fit's A.
"""

from __future__ import annotations

import json
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
from scipy import ndimage, optimize

DANDISET = "001273"
VERSION = "0.250805.1356"
API = "https://api.dandiarchive.org/api"
STEP_US = 0.05
PRE_US = 1.0
PULSE_US = 2.0


def list_assets() -> list[dict]:
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    out = []
    while url:
        page = json.load(urllib.request.urlopen(url))
        for a in page["results"]:
            b = a["blob"]
            out.append(dict(path=a["path"], size=a["size"],
                            url=f"https://dandiarchive.s3.amazonaws.com/blobs/{b[:3]}/{b[3:6]}/{b}"))
        url = page["next"]
    return sorted(out, key=lambda a: a["path"])


def read_meta(asset: dict) -> dict:
    with h5py.File(remfile.File(asset["url"]), "r") as f:
        desc = f["session_description"][()].decode()
        shape = f["acquisition/StrobeImaging/data"].shape
        subject = f["general/subject/subject_id"][()].decode()
        start = f["session_start_time"][()].decode()
    pos = "up_bottom" if "above (Up)" in desc else ("right_left" if "Right and Left" in desc else "not_specified")
    return dict(asset, subject=subject, start=start, shape=shape,
                volts=float(re.search(r"pulse at ([\d,.]+)V", desc).group(1).replace(",", ".")),
                pulse_us=float(re.search(r"with ([\d,.]+) µs", desc).group(1).replace(",", ".")),
                backward="backward manner" in desc, electrodes=pos)


def read_stack(meta: dict) -> np.ndarray:
    """One replicate as float32 frames in forward time, the dark first-acquired frame set to NaN."""
    with h5py.File(remfile.File(meta["url"]), "r") as f:
        d = f["acquisition/StrobeImaging/data"][:].astype(np.float32)
    means = d.reshape(d.shape[0], -1).mean(axis=1)
    d[means < 0.8 * np.median(means)] = np.nan
    return d[::-1] if meta["backward"] else d


def times_us(n: int) -> np.ndarray:
    """Time of each frame from the pulse onset, in us."""
    return np.arange(n) * STEP_US - PRE_US


def ratio_image(mean_stack: np.ndarray, t: np.ndarray):
    control = np.nanmean(mean_stack[(t < 0) | (t >= PULSE_US + 4.0)], axis=0)
    late = np.nanmean(mean_stack[(t >= PULSE_US - 0.5) & (t < PULSE_US)], axis=0)
    cf = ndimage.uniform_filter(control, 12)
    return ndimage.uniform_filter(late, 12) / cf, cf


def otsu(x: np.ndarray, bins: int = 256) -> float:
    hist, edges = np.histogram(x, bins=bins)
    mids = (edges[:-1] + edges[1:]) / 2
    w0 = np.cumsum(hist); w1 = w0[-1] - w0
    m0 = np.cumsum(hist * mids) / np.maximum(w0, 1)
    m1 = (np.sum(hist * mids) - np.cumsum(hist * mids)) / np.maximum(w1, 1)
    return float(mids[np.argmax((w0 * w1 * (m0 - m1) ** 2)[:-1])])


def cell_mask(control_filtered: np.ndarray) -> np.ndarray:
    lab, n = ndimage.label(control_filtered > otsu(control_filtered))
    if n == 0:
        return np.zeros_like(control_filtered, dtype=bool)
    sizes = ndimage.sum(np.ones_like(lab), lab, index=range(1, n + 1))
    return lab == (1 + int(np.argmax(sizes)))


def roi_masks(ratio: np.ndarray, cell: np.ndarray) -> dict:
    """001273-O1: per sign, (a) 12 x 12 square at the extreme pixel in the cell, (b) beyond half the extreme."""
    r = np.where(cell, ratio - 1.0, np.nan)
    out = {}
    for pole, fn in (("cathodic", np.nanargmax), ("anodic", np.nanargmin)):
        iy, ix = np.unravel_index(fn(r), r.shape)
        sq = np.zeros_like(cell)
        sq[max(0, iy - 6):iy + 6, max(0, ix - 6):ix + 6] = True
        ext = r[iy, ix]
        half = (r > ext / 2) if pole == "cathodic" else (r < ext / 2)
        out[(pole, "a")] = sq & cell
        out[(pole, "b")] = np.nan_to_num(half, nan=0).astype(bool)
        out[(pole, "extreme")] = float(ext)
        out[(pole, "pixel")] = (int(iy), int(ix))
    return out


def load_experiment(metas: list[dict], workers: int = 8) -> dict:
    """Stream the replicates of one experiment; keep the ROI traces of each replicate, not the frames."""
    with ThreadPoolExecutor(workers) as ex:
        stacks = list(ex.map(read_stack, metas))
    n = min(s.shape[0] for s in stacks)
    stacks = [s[:n] for s in stacks]
    t = times_us(n)
    mean_stack = np.nanmean(np.stack(stacks), axis=0)
    ratio, cf = ratio_image(mean_stack, t)
    cell = cell_mask(cf)
    rois = roi_masks(ratio, cell)
    traces = {}
    for key in [k for k in rois if k[1] in ("a", "b")]:
        m = rois[key]
        tr = np.array([s[:, m].mean(axis=1) for s in stacks])
        f0 = np.nanmean(tr[:, t < 0], axis=1, keepdims=True)
        traces[key] = 100.0 * (tr - f0) / f0
    whole = np.array([np.nanmean(s.reshape(n, -1), axis=1) for s in stacks])
    return dict(t=t, traces=traces, rois={k: v for k, v in rois.items() if k[1] in ("extreme", "pixel")},
                roi_px={k: int(v.sum()) for k, v in rois.items() if k[1] in ("a", "b")},
                cell_px=int(cell.sum()), ratio=ratio[::8, ::8], frame_means=whole,
                n_replicates=len(stacks))


def fit_tau(t: np.ndarray, reps: np.ndarray, weighting: str, discharge_amp: str) -> dict:
    """001273-F4 with the O2 and O3 readings, on the mean over replicates."""
    y = np.nanmean(reps, axis=0)
    sem = np.nanstd(reps, axis=0, ddof=1) / np.sqrt(np.sum(np.isfinite(reps), axis=0))
    out = dict(tau_c=np.nan, tau_d=np.nan, amp_c=np.nan, ok=False)
    on = (t >= 0) & (t < PULSE_US) & np.isfinite(y)
    off = (t >= PULSE_US) & np.isfinite(y)
    sig_on = sem[on] if weighting == "b" else None
    sig_off = sem[off] if weighting == "b" else None
    try:
        a0 = float(np.nanmean(y[on][-10:]))
        p, _ = optimize.curve_fit(lambda x, a, tau: a * (1 - np.exp(-x / tau)), t[on], y[on],
                                  p0=(a0, 0.5), sigma=sig_on, bounds=([-np.inf, 0.01], [np.inf, 20]), maxfev=10000)
        out.update(amp_c=p[0], tau_c=p[1])
        x = t[off] - PULSE_US
        if discharge_amp == "a":
            q, _ = optimize.curve_fit(lambda x, b, tau: b * np.exp(-x / tau), x, y[off], p0=(p[0], 0.5),
                                      sigma=sig_off, bounds=([-np.inf, 0.01], [np.inf, 20]), maxfev=10000)
            out["tau_d"] = q[1]
        else:
            q, _ = optimize.curve_fit(lambda x, tau: p[0] * np.exp(-x / tau), x, y[off], p0=(0.5,),
                                      sigma=sig_off, bounds=([0.01], [20]), maxfev=10000)
            out["tau_d"] = q[0]
        out["ok"] = True
    except (RuntimeError, ValueError):
        pass
    return out
