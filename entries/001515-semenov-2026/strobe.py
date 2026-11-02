"""Loading and simple measures for the strobe imaging files of dandiset 001515.

Semenov, Silkuniene, Silkunas, Pakhomova, Bixler, Ibey, Kochunov & Pakhomov (2026),
Bioelectrochemistry 171, 109283, doi:10.1016/j.bioelechem.2026.109283.

Each NWB file holds one ImageSeries, `acquisition/StrobeImaging`: 70 frames of 512 x 512 pixels
(uint16, unit "n.a.") at a stated 6 Hz, of CHO cells loaded with FluoVolt. The session
description gives the pulse (a single 1-us pulse and its amplitude in volts), the electrode
spacing, whether the anode was above or below the cell, and whether the recording ran "forward"
or "backward". Files are streamed from the archive at the pinned version; nothing is written to
disk.

Where the parameters come from:

- `polarization_trace` is a check of the data against their description, used for no claim. Its
  parameters are standard choices made here, not the paper's: the background of each frame is its
  5th percentile of pixel values; the membrane mask is the brightest 10% of pixels of the
  frame-averaged image; cells are connected parts of the mask of at least `MIN_CELL_PX` pixels;
  each frame is divided by its mean over the mask (to remove the frame-to-frame changes of laser
  intensity, Methods 2.3 and Introduction, paragraph 2 of the paper); the index is, per cell, the
  mean relative change of the pixels above the cell's centroid minus that of the pixels below it,
  in percent, and the median over cells, smoothed by a 3-frame running median.
- `f_factor` is Eq. (2) of the paper (Methods 2.3) and `CONSTANTS` its constants as Methods 2.3
  gives them: cytoplasm 0.4 S/m, medium 1.64 S/m, intact membrane 3e-7 S/m, radius 8 um,
  membrane thickness 5 nm.
"""

from __future__ import annotations

import hashlib
import re

import h5py
import numpy as np
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import ndimage

DANDISET_ID = "001515"
DANDISET_VERSION = "0.261006.1841"

MIN_CELL_PX = 300          # standard choice: smallest connected part of the mask taken as a cell
MASK_PERCENTILE = 90       # standard choice: brightest 10% of pixels of the mean image
BACKGROUND_PERCENTILE = 5  # standard choice: per-frame background level

# Methods 2.3 of the paper.
CONSTANTS = {"lambda_i": 0.4, "lambda_o": 1.64, "lambda_m_intact": 3e-7, "R": 8e-6, "d": 5e-9}


def assets() -> list[dict]:
    """Path, size and streaming URL of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        out = [{"path": a.path, "size": a.size,
                "url": a.get_content_url(follow_redirects=1, strip_query=True)}
               for a in dandiset.get_assets() if a.path.endswith(".nwb")]
    return sorted(out, key=lambda a: a["path"])


def version_metadata() -> dict:
    with DandiAPIClient() as client:
        return client.get_dandiset(DANDISET_ID, DANDISET_VERSION).get_raw_metadata()


def _text(value) -> str:
    return value.decode() if isinstance(value, bytes) else str(value)


def parse_description(text: str) -> dict:
    """The pulse, electrodes, anode side, recording order and dye named in a session description."""
    def find(pattern, cast=str):
        m = re.search(pattern, text)
        return cast(m.group(1)) if m else None
    return {
        "pulse_us": find(r"single ([\d.]+) µs", float),
        "volts": find(r"at ([\d.]+)\s*V amplitude", float),
        "spacing_mm": find(r"between electrodes ([\d.]+) mm", float),
        "electrode_diameter_mm": find(r"electrode diameter ([\d.]+) mm", float),
        "anode": find(r"Anode positioned (above|below)"),
        "order": find(r"performed in a (forward|backward) manner"),
        "dye": find(r"dye (\S+) and"),
        "sine": "sine" in text.lower(),
    }


def read_metadata(asset: dict) -> dict:
    """Everything a file holds apart from the pixel values: groups, attributes, shapes."""
    with h5py.File(remfile.File(asset["url"]), "r") as f:
        series = f["acquisition/StrobeImaging"]
        data = series["data"]
        groups = []
        f.visit(lambda name: groups.append(name) if not name.startswith("specifications") else None)
        sd = _text(f["session_description"][()])
        out = {
            "path": asset["path"],
            "subject": asset["path"].split("/")[0].removeprefix("sub-"),
            "subject_id": _text(f["general/subject/subject_id"][()]),
            "species": _text(f["general/subject/species"][()]),
            "age": _text(f["general/subject/age"][()]),
            "strain": _text(f["general/subject/strain"][()]),
            "session_id": _text(f["general/session_id"][()]),
            "session_start": _text(f["session_start_time"][()]),
            "acquisition": list(f["acquisition"].keys()),
            "stimulus": list(f["stimulus/presentation"].keys()),
            "processing": list(f["processing"].keys()),
            "analysis": list(f["analysis"].keys()),
            "intervals": "intervals" in f,
            "groups": groups,
            "shape": data.shape,
            "dtype": str(data.dtype),
            "unit": _text(data.attrs.get("unit")),
            "conversion": float(data.attrs.get("conversion")),
            "rate": float(series["starting_time"].attrs["rate"]),
            "starting_time": float(series["starting_time"][()]),
            "has_timestamps": "timestamps" in series,
            "dimension": series["dimension"][:].tolist() if "dimension" in series else None,
            "series_description": _text(series.attrs.get("description")),
            "session_description": sd,
        }
    out.update(parse_description(sd))
    return out


def polarization_trace(stack: np.ndarray) -> dict:
    """Top-minus-bottom membrane index per frame (percent), as the module docstring describes."""
    a = stack.astype(np.float64)
    a -= np.percentile(a.reshape(len(a), -1), BACKGROUND_PERCENTILE, axis=1)[:, None, None]
    mean_image = a.mean(0)
    mask = mean_image > np.percentile(mean_image, MASK_PERCENTILE)
    labels, n = ndimage.label(mask)
    sizes = ndimage.sum(mask, labels, range(1, n + 1))
    rows = np.indices(mask.shape)[0]
    values = a[:, mask]
    norm = values / values.mean(1, keepdims=True)
    rel = norm / norm.mean(0, keepdims=True) - 1.0
    lab = labels[mask]
    per_cell = []
    for k in np.flatnonzero(sizes >= MIN_CELL_PX) + 1:
        sel = lab == k
        y = rows[mask][sel]
        top, bottom = y < y.mean(), y > y.mean()
        per_cell.append(100 * (rel[:, sel][:, top].mean(1) - rel[:, sel][:, bottom].mean(1)))
    per_cell = np.array(per_cell)
    index = ndimage.median_filter(np.median(per_cell, axis=0), size=3, mode="nearest")
    return {"index": index, "n_cells": len(per_cell), "frame_mean": stack.reshape(len(stack), -1).mean(1),
            "mean_image_small": mean_image.reshape(64, 8, 64, 8).mean((1, 3))}


def response_window(index: np.ndarray, first: int = 1) -> dict:
    """Baseline, peak and the frames where the index exceeds half its peak change.

    Frame 0 is left out by default: in many files it is about half as bright as the others
    (shown in the notebook's data check), which the per-frame normalization does not remove.
    """
    index = np.asarray(index, dtype=float).copy()
    index[:first] = np.nan
    base = float(np.nanmedian(index))
    dev = np.nan_to_num(index - base)
    peak = int(np.argmax(np.abs(dev)))
    above = np.flatnonzero(np.abs(dev) > 0.5 * abs(dev[peak]))
    return {"baseline": base, "peak_frame": peak, "peak": float(dev[peak]),
            "first_half": int(above.min()), "last_half": int(above.max()), "n_half": len(above)}


def summarize_file(asset: dict) -> dict:
    """Read one file's pixels once: per-frame checksums and the polarization index."""
    with h5py.File(remfile.File(asset["url"]), "r") as f:
        stack = f["acquisition/StrobeImaging/data"][:]
    out = {"path": asset["path"],
           "frame_md5": [hashlib.md5(fr.tobytes()).hexdigest() for fr in stack],
           "min": int(stack.min()), "max": int(stack.max())}
    out.update(polarization_trace(stack))
    out.update(response_window(out["index"]))
    return out


def f_factor(lambda_m: float, lambda_i: float = CONSTANTS["lambda_i"], lambda_o: float = CONSTANTS["lambda_o"],
             R: float = CONSTANTS["R"], d: float = CONSTANTS["d"]) -> float:
    """Eq. (2): the factor that replaces 1.5 in Eq. (1) for a membrane of conductivity lambda_m (S/m)."""
    num = 3 * lambda_o * (3 * R**2 * d * lambda_i + (3 * d**2 * R - d**3) * (lambda_m - lambda_i))
    den = (2 * R**3 * (lambda_m + 2 * lambda_o) * (lambda_m + 0.5 * lambda_i)
           - 2 * (R - d)**3 * (lambda_o - lambda_m) * (lambda_i - lambda_m))
    return num / den
