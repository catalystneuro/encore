"""Loading and Fluo-4 measures for dandiset 001521.

Semenov, Silkuniene, Silkunas, Pakhomova, Bixler, Ibey, Kochunov & Pakhomov (2026),
Bioelectrochemistry 171, 109283, doi:10.1016/j.bioelechem.2026.109283.

The dandiset holds 73 NWB files, one time-lapse of 512 x 512 widefield Fluo-4 images each
(`acquisition/TimeLapseImaging`), with no ROIs, traces or tables. Two sessions:

- 2025-02-03 (31 files): a single 1-us pulse (or a sham, 0 V) 60 s into a 300-frame recording
  at 1 frame/s. This is the paper's first set of Ca2+ experiments (Methods 2.4; Fig. 6A).
- 2025-05-02 (42 files): sixty 1-us pulses at 6 Hz (or a sham) 30 s into a 90-frame recording
  at 0.5 frame/s. This is the paper's second set (Methods 2.4; Fig. 6B).

The pulse is given in each file's `session_description` as a voltage; the paper gives field
strengths only. Files are streamed from the archive at the pinned version; nothing is written
to disk.

Where the parameters come from:

- dF (%) = 100 (F - F0)/F0, with F the mean over a circular region over the cell less the
  background of a cell-free region, and F0 the mean before the pulse: Methods 2.4, as the
  claims' criterion gives it.
- The pulse times (60 s for single pulses, 30 s for trains) are from Methods 2.4 and agree with
  the files' descriptions; `PULSE_FRAME` converts them to frames at the files' rates.
- Cell detection is not described in the paper (the regions were drawn in MetaMorph). It is a
  standard choice here, which the claims file says should not change the outcome: Otsu
  threshold of the smoothed pre-pulse mean image, a watershed on the distance transform to
  split touching cells, objects of at least `MIN_AREA` pixels not touching the image border.
  The circular region is centred on each object with a radius of `ROI_FRACTION` of its
  equivalent radius, so that it stays over the cell when the cell drifts by a few pixels; the
  traces for the radii in `ROI_VARIANTS` are kept too, to show that the choice does not change
  a result.
- The cell-free region is every pixel more than `BG_MARGIN` pixels from any detected object;
  its median per frame is the background (a standard choice). As dim cells that the threshold
  misses can sit in that region, the `BG_LOW_PERCENTILE` percentile of the same pixels is kept
  as a variant background, for the main region size only.
- The end-of-recording value is the mean of the last `END_FRAMES` frames (the claims' criterion,
  "a standard choice"); the peak is the largest value after the pulse.
"""

from __future__ import annotations

import re
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import ndimage as ndi
from skimage.feature import peak_local_max
from skimage.filters import gaussian, threshold_otsu
from skimage.measure import regionprops
from skimage.segmentation import watershed

DANDISET_ID = "001521"
DANDISET_VERSION = "0.261006.1845"

PULSE_S = {"single": 60.0, "train": 30.0}   # Methods 2.4
MIN_AREA = 400        # pixels; standard choice (a cell of radius 8 um is about 30 px here)
ROI_FRACTION = 0.7    # standard choice
ROI_VARIANTS = (0.5, 1.0)  # other region sizes, to show that the choice does not change a result
BG_MARGIN = 15        # pixels; standard choice
BG_LOW_PERCENTILE = 10  # variant background, less affected by dim unsegmented cells
SMOOTH_SIGMA = 2.0    # pixels, for detection only; standard choice
END_FRAMES = 10       # claims' criterion

_DESC = re.compile(r"Stimulation was applied with (.*?)\. Distance between electrodes ([\d.]+) mm")


def list_files() -> pd.DataFrame:
    """Assets of the pinned version, with their S3 URLs."""
    client = DandiAPIClient()
    ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
    rows = []
    for a in ds.get_assets():
        rows.append({"path": a.path, "asset_id": a.identifier, "size": a.size,
                     "url": a.get_content_url(follow_redirects=1, strip_query=True)})
    return pd.DataFrame(rows).sort_values("path").reset_index(drop=True)


def parse_description(desc: str) -> dict:
    """Protocol, voltage and electrode gap from a file's session_description."""
    m = _DESC.search(desc)
    stim, gap = m.group(1), float(m.group(2))
    volts = float(re.search(r"(\d+) V", stim).group(1))
    if "sham" in stim:
        n_pulses = 0
    elif stim.startswith("a single"):
        n_pulses = 1
    else:
        n_pulses = int(re.match(r"(\d+) 1 us", stim).group(1))
    return {"stim_text": stim, "volts": volts, "n_pulses": n_pulses, "gap_mm": gap}


def _text(group, key: str) -> str:
    """A string dataset of an HDF5 group, or "" if absent."""
    if key not in group:
        return ""
    v = group[key][()]
    return v.decode() if isinstance(v, bytes) else str(v)


def read_metadata(url: str) -> dict:
    """Everything a file holds except the image data."""
    with h5py.File(remfile.File(url), "r") as f:
        ts = f["acquisition/TimeLapseImaging"]
        st = ts["starting_time"]
        out = {
            "session_id": f["general/session_id"][()].decode(),
            "subject_id": f["general/subject/subject_id"][()].decode(),
            "subject_age": _text(f["general/subject"], "age"),
            "subject_species": _text(f["general/subject"], "species"),
            "session_start": f["session_start_time"][()].decode(),
            "description": f["session_description"][()].decode(),
            "series_description": ts.attrs["description"],
            "rate_hz": float(st.attrs["rate"]),
            "starting_time": float(st[()]),
            "shape": tuple(ts["data"].shape),
            "dtype": str(ts["data"].dtype),
            "unit": ts["data"].attrs["unit"],
            "groups": sorted(k for k in f.keys()),
            "acquisition": sorted(f["acquisition"].keys()),
            "processing": sorted(f["processing"].keys()),
            "stimulus": sorted(f["stimulus/presentation"].keys()) + sorted(f["stimulus/templates"].keys()),
            "analysis": sorted(f["analysis"].keys()),
        }
    out.update(parse_description(out["description"]))
    out["set"] = "train" if out["session_id"].endswith("05-02") else "single"
    return out


def segment(image: np.ndarray):
    """Label cells in a pre-pulse mean image; returns labels and a table of objects."""
    sm = gaussian(image, SMOOTH_SIGMA, preserve_range=True)
    mask = sm > threshold_otsu(sm)
    mask = ndi.binary_fill_holes(ndi.binary_opening(mask, iterations=2))
    dist = ndi.distance_transform_edt(mask)
    peaks = peak_local_max(dist, min_distance=12, labels=ndi.label(mask)[0], exclude_border=False)
    markers = np.zeros(mask.shape, int)
    markers[tuple(peaks.T)] = np.arange(1, len(peaks) + 1)
    labels = watershed(-dist, markers, mask=mask)
    h, w = image.shape
    rows = []
    for p in regionprops(labels):
        r0, c0, r1, c1 = p.bbox
        border = r0 == 0 or c0 == 0 or r1 == h or c1 == w
        rows.append({"label": p.label, "area": int(p.area), "y": p.centroid[0], "x": p.centroid[1],
                     "radius_px": float(np.sqrt(p.area / np.pi)), "border": border,
                     "kept": (p.area >= MIN_AREA) and not border})
    return labels, pd.DataFrame(rows)


def cell_traces(stack: np.ndarray, pulse_frame: int, fraction: float = ROI_FRACTION, variants=()):
    """Background-corrected F per kept cell (and per variant region size) and the background trace."""
    pre = stack[:pulse_frame].mean(0)
    labels, cells = segment(pre)
    far = ~ndi.binary_dilation(labels > 0, iterations=BG_MARGIN)
    flat = stack.reshape(stack.shape[0], -1)
    bg = np.median(flat[:, far.ravel()], axis=1)
    bg_low = np.percentile(flat[:, far.ravel()], BG_LOW_PERCENTILE, axis=1)
    yy, xx = np.mgrid[:pre.shape[0], :pre.shape[1]]
    kept = cells[cells.kept].reset_index(drop=True)
    out = {}
    for fr in (fraction, *variants):
        F = []
        for _, c in kept.iterrows():
            roi = (yy - c.y) ** 2 + (xx - c.x) ** 2 <= (fr * c.radius_px) ** 2
            F.append(flat[:, roi.ravel()].mean(1))
        out[fr] = np.array(F).reshape(len(kept), stack.shape[0]) - bg[None]
    raw_main = out[fraction] + bg[None]
    return out, bg, cells, far.mean(), raw_main - bg_low[None], bg_low


def delta_f(F: np.ndarray, pf: int):
    """dF (%) = 100 (F - F0)/F0 with F0 the mean before the pulse (Methods 2.4)."""
    F0 = F[:, :pf].mean(1, keepdims=True)
    return 100.0 * (F - F0) / F0, F0.ravel()


def pulse_frame(meta: dict) -> int:
    return int(round(PULSE_S[meta["set"]] * meta["rate_hz"]))


def process(url: str) -> dict:
    """Stream one file and reduce it to per-cell dF traces."""
    meta = read_metadata(url)
    with h5py.File(remfile.File(url), "r") as f:
        stack = f["acquisition/TimeLapseImaging/data"][:].astype(np.float32)
    pf = pulse_frame(meta)
    Fs, bg, cells, bg_frac, F_bg_low, bg_low = cell_traces(stack, pf, ROI_FRACTION, ROI_VARIANTS)
    dF, F0 = delta_f(Fs[ROI_FRACTION], pf)
    dF_bg_low = delta_f(F_bg_low, pf)[0]
    dF_roi = {fr: delta_f(Fs[fr], pf)[0] for fr in ROI_VARIANTS}
    whole = stack.reshape(stack.shape[0], -1).mean(1)
    pre_small = stack[:pf].mean(0).reshape(128, 4, 128, 4).mean((1, 3))
    meta.update({"pre_small": pre_small, "url": url, "pulse_frame": pf, "F0": F0, "dF": dF,
                 "dF_roi": dF_roi, "bg": bg,
                 "dF_bg_low": dF_bg_low, "bg_low": bg_low,
                 "cells": cells, "bg_fraction": bg_frac, "frame_mean": whole,
                 "raw_min": int(stack.min()), "raw_max": int(stack.max())})
    return meta


def process_all(urls, workers: int = 4) -> list[dict]:
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(process, urls))


def end_value(dF: np.ndarray, frames: int = END_FRAMES) -> np.ndarray:
    """Mean dF over the last `frames` frames, per cell."""
    return dF[:, -frames:].mean(1)


def peak_value(dF: np.ndarray, pf: int) -> np.ndarray:
    """Largest dF after the pulse, per cell."""
    return dF[:, pf:].max(1)


# --- field strengths -----------------------------------------------------------------------
#
# The files give the pulse as a generator voltage; the paper gives field strengths only (the
# Sim4Life field 5 um above the glass, Methods 2.2) and states no conversion. Two readings of the
# conversion, each a factor in V/cm per V, are run (author, step 1.6):
#
# - "M1", 3.9 V/cm per V, the reading adopted (an assumption). The single-pulse voltages 150, 200,
#   250, 300 and 350 V then fall on the field series used throughout the paper, 570, 780, 1000,
#   1200 and 1400 V/cm (Figs. 1, 2, 4), and 780/200 = 3.9. The train voltages 70, 150, 170, 200,
#   230 and 250 V then fall nearest the six fields labelled in Fig. 6B (230, 570, 650, 780, 900 and
#   1000 V/cm), and their group sizes in the dataset are close to the n the figure gives for each
#   field (the notebook compares them). The same electrodes and generator served both sessions
#   (Methods 2.2), so one factor is assumed for both.
# - "M2", 3.3 V/cm per V, a variant: the train voltages 70, 200 and 230 V then fall on the three
#   fields the paper names in the text for the trains, 230, 650 and 780 V/cm (Section 3.6,
#   paragraph 3; 3.29, 3.25 and 3.39 V/cm per V), but the voltages nearest 900 and 1000 V/cm are
#   250 and 300 V, and the group sizes do not follow the figure's.
#
# Neither factor follows from the electrode gap: V/d is 10 V/cm per V for the 1.00 mm the files
# state and 6.25 V/cm per V for the 1.6 mm of Methods 2.2, and the Sim4Life field at the cells is
# not given as a fraction of V/d.

FIELD_PER_VOLT = {"M1": 3.9, "M2": 3.3}


def field(volts, mapping: str):
    return np.asarray(volts, float) * FIELD_PER_VOLT[mapping]


def voltage_for(field_v_cm: float, mapping: str, available) -> float:
    """The available voltage whose field under a mapping is nearest a field the paper names."""
    available = np.asarray(sorted(set(available)), float)
    return float(available[np.argmin(np.abs(available * FIELD_PER_VOLT[mapping] - field_v_cm))])
