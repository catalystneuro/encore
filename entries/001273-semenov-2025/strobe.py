"""Loading and measures for the pulsed laser strobe imaging of dandiset 001273.

Semenov, Kim, Silkuniene & Pakhomov (2025), Cell Reports Physical Science 6, 102660,
doi:10.1016/j.xcrp.2025.102660, Figure 4.

Each NWB file holds one replicate: 160 full-sensor images (512 x 512, uint16) of one FluoVolt-loaded
neuron, taken at 50-ns steps around a 2-us pulse. The session description gives the nominal pulse
amplitude, whether the delays were stepped forward or backward, and, for the January 19 and March
11 cells, the axis of the electrodes ("Up" and "Bottom", or "Right" and "Left"). An experiment is
a run of consecutive files of one cell at one amplitude and electrode axis (eight replicates).
Files are streamed from the archive at the pinned version; nothing is written to disk.

Where the parameters come from:

- Frame timing. Methods, Pulsed laser fluorescence microscopy: "Strobe images were collected at
  50-ns intervals, starting 1 us before the pulse and continuing for 5 us after it (8 us total,
  160 images)". `FRAME_US` and the nominal pulse window `NOMINAL_ONSET` to `NOMINAL_ONSET +
  PULSE_FRAMES` follow it. Files recorded "in a backward manner" are stored in acquisition order,
  so in reverse time; `load_experiment` reverses them (the notebook shows the data support this).
  The fits use the nominal onset (frame 20); the notebook estimates the onset of each experiment
  from the data and repeats the fits with it as a variant.
- Dim first frames. The first image acquired in most files is about half as bright as the rest,
  and a few other frames are as dim. Frames whose mean is below `DIM_FRACTION` of the file's
  median frame mean are dropped. A standard choice: the paper does not mention them, and they are
  failed flashes, not data.
- RATIO image and ROIs. Methods: CONTROL is the mean of the images "before the pulse and late
  after the pulse (when the membrane was fully discharged)"; POLARIZED the mean of the images
  "during the last 0.5 us of the pulse"; both "low-pass filtered, with a filter setting of 12 x 12
  pixels" (`FILTER_PX`); RATIO = POLARIZED / CONTROL. "Late after the pulse" is taken as the last
  1 us (`LATE_FRAMES`), a standard choice. The RATIO image is computed from the mean over the
  replicates, and divided by its median over the cell, so that the unpolarized membrane is 1 (the
  paper's images are viewed against the background; this removes the flash-intensity difference
  between the two averages). The cell is the soma: the connected region of the filtered CONTROL
  image brighter than halfway between the image median and the brightest pixel of the central
  128 x 128 pixels (the neuron was centred in the field of vision, Methods, Sine wave and square
  pulse stimulation), a standard choice; the claims file's ROIs are "within the cell". The ROIs themselves are not in the dataset; they are rebuilt under the two
  readings of the claims file (O1): (a) a 12 x 12 pixel square centred on the extreme pixel of
  each sign within the cell, (b) the pixels within the cell beyond half the extreme of each sign.
  A variant of (a), "a_clip", keeps only the pixels of the square that lie within the cell.
- dF. Methods: "The average of measurements before the pulse was taken as F0, and the optical TMP
  changes in each frame were expressed as dF = 100% x (F - F0) / F0", per replicate, then the mean
  and SEM over replicates ("experiments were repeated to determine the mean dF for every
  datapoint and its standard error"). F0 is the mean over the nominal pre-pulse frames.
- Debris scaling. The debris ROI is not in the dataset, so the traces are unscaled (claims file,
  F2). `trace(..., scale="frame")` divides by the whole-frame mean instead, a variant only.
- Fits. Methods: dF = dFmax (1 - exp(-t/tau)) for charging, t the time into the pulse, and
  dF = dFmax exp(-t/tau) for discharging, t the time after the pulse. Readings of the claims file:
  weighting (O2) none or 1/SEM^2; discharge amplitude (O3) free or fixed at the charging dFmax.
"""

from __future__ import annotations

import hashlib
import json
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
from scipy import ndimage
from scipy.optimize import curve_fit

DANDISET_ID = "001273"
DANDISET_VERSION = "0.250805.1356"
API = "https://api.dandiarchive.org/api"

FRAME_US = 0.05          # Methods: 50-ns steps
N_FRAMES = 160           # Methods: 8 us, 160 images
NOMINAL_ONSET = 20       # Methods: starting 1 us before the pulse
PULSE_FRAMES = 40        # 2-us pulse
POLARIZED_FRAMES = 10    # Methods: last 0.5 us of the pulse
LATE_FRAMES = 20         # standard choice: "late after the pulse" taken as the last 1 us
FILTER_PX = 12           # Methods: low-pass filter of 12 x 12 pixels
DIM_FRACTION = 0.7       # standard choice: frames below 70% of the file's median mean are dropped
THREADS = 8
TAU_BOUNDS = (0.005, 50.0)  # us; standard choice, a fit ending at a bound counts as failed
AMPLITUDE_BOUND = 200.0     # % dF; standard choice, likewise


def list_assets():
    """Every asset of the pinned version, with its path, size and download URL."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=1000"
    with urllib.request.urlopen(url) as r:
        results = json.load(r)["results"]
    return [{"path": a["path"], "size": a["size"], "blob": a["blob"],
             "url": f"{API}/assets/{a['asset_id']}/download/"} for a in results]


def _open(url):
    return h5py.File(remfile.File(url), "r")


def read_metadata(asset):
    """Session metadata and array shape of one file, without reading its images."""
    with _open(asset["url"]) as h:
        s = h["acquisition/StrobeImaging"]
        desc = h["session_description"][()].decode()
        amp = re.search(r"at ([\d,]+)V amplitude", desc)
        axis = None
        if "above (Up) and below (Bottom)" in desc:
            axis = "vertical"
        elif "Right and Left" in desc:
            axis = "horizontal"
        return {
            "path": asset["path"], "blob": asset["blob"], "url": asset["url"],
            "subject_id": h["general/subject/subject_id"][()].decode(),
            "session_start": h["session_start_time"][()].decode(),
            "amplitude_v": float(amp.group(1).replace(",", ".")) if amp else np.nan,
            "direction": re.search(r"in a (\w+) manner", desc).group(1),
            "electrode_axis": axis,
            "description": desc,
            "electrode_text": (re.search(r"Electrode[s]? [^.]*\.", desc) or [None])[0],
            "shape": tuple(s["data"].shape), "dtype": str(s["data"].dtype),
            "rate_hz": float(s["starting_time"].attrs["rate"]),
            "starting_time": float(s["starting_time"][()]),
            "series_description": s.attrs["description"],
            "age": h["general/subject/age"][()].decode(),
            "species": h["general/subject/species"][()].decode(),
        }


def read_all_metadata(assets):
    with ThreadPoolExecutor(THREADS * 4) as ex:
        return list(ex.map(read_metadata, assets))


def group_experiments(meta):
    """Runs of consecutive files of one cell with the same amplitude and electrode text."""
    rows = sorted(meta, key=lambda m: (m["subject_id"], m["session_start"]))
    groups, current = [], []
    for m in rows:
        if current and (m["subject_id"] != current[-1]["subject_id"]
                        or m["amplitude_v"] != current[-1]["amplitude_v"]
                        or m["electrode_text"] != current[-1]["electrode_text"]):
            groups.append(current)
            current = []
        current.append(m)
    groups.append(current)
    return groups


def _read_images(m):
    with _open(m["url"]) as h:
        raw = h["acquisition/StrobeImaging/data"][:]
    digest = hashlib.md5(raw.tobytes()).hexdigest()
    x = raw.astype(np.float32)
    if m["direction"] == "backward":
        x = x[::-1].copy()
    return x, digest


def load_experiment(files):
    """Images of every replicate in time order, shape (replicates, 160, 512, 512), with dim
    frames set to NaN, the dim-frame flags, the frame means and an MD5 digest of each file's images."""
    with ThreadPoolExecutor(THREADS) as ex:
        read = list(ex.map(_read_images, files))
    x = np.stack([r[0] for r in read])
    means = x.mean(axis=(2, 3))
    dim = means < DIM_FRACTION * np.median(means, axis=1, keepdims=True)
    x[dim] = np.nan
    return x, dim, means, [r[1] for r in read]


def ratio_image(x, onset=NOMINAL_ONSET):
    """CONTROL, POLARIZED and RATIO images (Methods) from the replicate mean."""
    mean = np.nanmean(x, axis=0)
    pre = list(range(0, onset))
    late = list(range(N_FRAMES - LATE_FRAMES, N_FRAMES))
    end = onset + PULSE_FRAMES
    control = ndimage.uniform_filter(np.nanmean(mean[pre + late], axis=0), FILTER_PX)
    polarized = ndimage.uniform_filter(np.nanmean(mean[end - POLARIZED_FRAMES:end], axis=0), FILTER_PX)
    return control, polarized, polarized / control


def cell_mask(control):
    """The soma: the connected region of the filtered CONTROL image brighter than halfway between
    the image median and the brightest pixel of the central 128 x 128 pixels, holding that pixel."""
    n = control.shape[0]
    q = slice(3 * n // 8, 5 * n // 8)
    centre = np.full_like(control, -np.inf)
    centre[q, q] = control[q, q]
    seed = np.unravel_index(np.argmax(centre), control.shape)
    background = np.median(control)
    labels, _ = ndimage.label(control > background + 0.5 * (control[seed] - background))
    return labels == labels[seed]


def rois(ratio, mask):
    """ROIs of the two readings (O1), the extreme pixels, and the normalised RATIO image."""
    r = ratio / np.median(ratio[mask]) - 1
    inside = np.where(mask, r, np.nan)
    dep_px = np.unravel_index(np.nanargmax(inside), r.shape)
    hyp_px = np.unravel_index(np.nanargmin(inside), r.shape)
    out = {"ratio": r, "dep_px": dep_px, "hyp_px": hyp_px,
           "dep_extreme": float(r[dep_px]), "hyp_extreme": float(r[hyp_px])}
    half = FILTER_PX // 2
    for name, px in (("dep", dep_px), ("hyp", hyp_px)):
        sq = np.zeros_like(mask)
        sq[max(px[0] - half, 0):px[0] + half, max(px[1] - half, 0):px[1] + half] = True
        out[f"a_{name}"] = sq
    out["a_clip_dep"] = out["a_dep"] & mask
    out["a_clip_hyp"] = out["a_hyp"] & mask
    out["b_dep"] = mask & (r > r[dep_px] / 2)
    out["b_hyp"] = mask & (r < r[hyp_px] / 2)
    return out


def traces(x, roi, scale=None):
    """Mean intensity in an ROI per replicate and frame; scale="frame" divides by the frame mean."""
    f = x[:, :, roi].mean(axis=2)
    if scale == "frame":
        f = f / np.nanmean(x, axis=(2, 3))
    return f


def delta_f(f, onset=NOMINAL_ONSET):
    """dF = 100 (F - F0) / F0 per replicate, F0 the mean before the pulse; mean and SEM."""
    f0 = np.nanmean(f[:, :onset], axis=1, keepdims=True)
    d = 100 * (f - f0) / f0
    n = np.sum(~np.isnan(d), axis=0)
    return np.nanmean(d, axis=0), np.nanstd(d, axis=0, ddof=1) / np.sqrt(n)


def charging(t, a, tau):
    return a * (1 - np.exp(-t / tau))


def _at_bound(tau):
    return tau <= TAU_BOUNDS[0] * 1.01 or tau >= TAU_BOUNDS[1] * 0.99


def fit_experiment(mean, sem, onset, weighted=False, fixed_amplitude=False):
    """Charging and discharging fits (Methods). `onset` is the frame (may be fractional) at which
    the pulse starts. Returns dFmax, charging tau, discharge amplitude and tau (us), or NaN for
    a fit that fails or ends at a bound (`TAU_BOUNDS`, `AMPLITUDE_BOUND`)."""
    i = np.arange(N_FRAMES)
    t = (i - onset) * FRAME_US
    end = onset + PULSE_FRAMES
    on = (i >= np.ceil(onset)) & (i < end) & ~np.isnan(mean)
    off = (i >= np.ceil(end)) & ~np.isnan(mean)
    sig_on = sem[on] if weighted else None
    sig_off = sem[off] if weighted else None
    out = {"dfmax": np.nan, "tau_charge": np.nan, "dis_amp": np.nan, "tau_discharge": np.nan}
    sign = np.sign(np.nanmean(mean[on][-POLARIZED_FRAMES:])) or 1.0
    try:
        p, _ = curve_fit(charging, t[on], mean[on], p0=(sign * np.nanmax(np.abs(mean[on])), 0.7),
                         sigma=sig_on, bounds=([-AMPLITUDE_BOUND, TAU_BOUNDS[0]], [AMPLITUDE_BOUND, TAU_BOUNDS[1]]), maxfev=20000)
        if not _at_bound(p[1]) and abs(p[0]) < AMPLITUDE_BOUND * 0.99:
            out["dfmax"], out["tau_charge"] = p
    except (RuntimeError, ValueError):
        pass
    if np.isnan(out["tau_charge"]):
        return out
    td = t[off] - PULSE_FRAMES * FRAME_US
    try:
        if fixed_amplitude:
            a = out["dfmax"]
            p, _ = curve_fit(lambda s, tau: a * np.exp(-s / tau), td, mean[off], p0=(0.9,),
                             sigma=sig_off, bounds=([TAU_BOUNDS[0]], [TAU_BOUNDS[1]]), maxfev=20000)
            if not _at_bound(p[0]):
                out["dis_amp"], out["tau_discharge"] = a, p[0]
        else:
            p, _ = curve_fit(lambda s, a, tau: a * np.exp(-s / tau), td, mean[off],
                             p0=(out["dfmax"], 0.9), sigma=sig_off,
                             bounds=([-AMPLITUDE_BOUND, TAU_BOUNDS[0]], [AMPLITUDE_BOUND, TAU_BOUNDS[1]]), maxfev=20000)
            if not _at_bound(p[1]) and abs(p[0]) < AMPLITUDE_BOUND * 0.99:
                out["dis_amp"], out["tau_discharge"] = p
    except (RuntimeError, ValueError):
        pass
    return out


def pulse_model(i, base, amp, onset, tau1, tau2):
    """Charging from `onset` for one pulse width, then discharging, on a constant baseline."""
    t = (i - onset) * FRAME_US
    w = PULSE_FRAMES * FRAME_US
    y = np.where(t < 0, 0.0, amp * (1 - np.exp(-np.clip(t, 0, w) / tau1)))
    top = amp * (1 - np.exp(-w / tau1))
    return base + np.where(t >= w, top * np.exp(-(t - w) / tau2), y)


def estimate_onset(trace):
    """Pulse onset (frame) from a polarization trace, by fitting `pulse_model`."""
    i = np.arange(N_FRAMES)
    ok = ~np.isnan(trace)
    amp0 = np.nanmax(trace) - np.nanmedian(trace[:NOMINAL_ONSET])
    p, _ = curve_fit(pulse_model, i[ok], trace[ok],
                     p0=(np.nanmedian(trace[:NOMINAL_ONSET]), amp0, NOMINAL_ONSET, 0.7, 0.9),
                     bounds=([-100, 0, 10, 0.01, 0.01], [100, 400, 30, 20, 20]), maxfev=20000)
    return p[2]


def process_experiment(files, onset_for_ratio=NOMINAL_ONSET):
    """Everything later steps need from one experiment, so its images can be released: the
    RATIO image and the cell mask (also downsampled for display), the ROI centres and sizes, the
    replicate traces for each ROI reading (unscaled and frame-scaled), and the frames dropped."""
    x, dim, frame_means, digests = load_experiment(files)
    control, _, ratio = ratio_image(x, onset_for_ratio)
    mask = cell_mask(control)
    r = rois(ratio, mask)
    out = {"n_replicates": x.shape[0], "dim_frames": dim, "frame_means": frame_means,
           "mask_px": int(mask.sum()), "dep_px": r["dep_px"], "hyp_px": r["hyp_px"],
           "dep_extreme": r["dep_extreme"], "hyp_extreme": r["hyp_extreme"],
           "ratio_small": r["ratio"][::4, ::4].copy(), "control_small": control[::4, ::4].copy(),
           "mask_small": mask[::4, ::4].copy(), "ratio": r["ratio"].astype(np.float32), "mask": mask,
           "traces": {}, "roi_px": {}}
    yy, xx = np.nonzero(mask)
    out["centroid"] = (float(yy.mean()), float(xx.mean()))
    for reading in ("a", "b", "a_clip"):
        for pole in ("dep", "hyp"):
            roi = r[f"{reading}_{pole}"]
            out["roi_px"][(reading, pole)] = int(roi.sum())
            for scale in (None, "frame"):
                out["traces"][(reading, pole, scale)] = traces(x, roi, scale)
    out["digests"] = digests
    del x
    return out
