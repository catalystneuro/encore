"""Loading and measuring the monolayer images of dandiset 001047 (Silkuniene et al. 2025).

Each NWB file holds one stitched fluorescence image (`acquisition/SingleTimePointImaging`),
of one well ("W") or of two wells side by side, the first subject of the session description
on the left ("L") and the second on the right ("R"). Images are streamed and reduced on load to
26-um pixels by block means, so that a region-of-interest mean on the reduced image equals the
mean of the full-resolution pixels it covers.

Where each parameter comes from:

- ROI size, 325 x 406 um, placed along the diagonals; background as the mean of 3 ROIs inside an
  electrode footprint, subtracted (paper, Methods 2.5; claims file F1, F2). The 406-um side lies
  along the line (claims file O1, a standard choice). Which footprint holds the 3 background ROIs
  is not said; the mean over the four footprints is used, each with 3 ROIs at its centre and 0.5 mm
  either side along the diagonal (a choice; the notebook shows the footprint with the lowest mean as
  a variant).
- ROI positions: whole-mm distances (claims file O1 reading a) or contiguous ROIs from the centre
  (O1 reading b). Diagonals pooled as the mean of the two diagonals at each signed position (O2
  reading a) or the four half-diagonals at each distance (O2 reading b).
- Array geometry: 15.3 mm between the inner sides of electrodes along a diagonal, 2.8-mm needles
  (Methods 2.2), and 6 and 7 mm from the centre being 1.65 and 0.65 mm from the electrodes
  (Results 3.1), which puts each electrode centre (7.65 + 1.4) mm from the array centre along a
  diagonal, 6.40 mm along each image axis. The square's sides are taken parallel to the image
  axes, as all images show (checked in the notebook).
- Pixel size. The CHO files state 1.625 um (OME metadata, 4x objective on an ORCA-Flash4.0); the
  CT26 files state none. Whole-well CT26 images (21870 x 21289 pixels) span the 35-mm well at
  1.625 um; the two-well CT26 images fit the same electrode spacing at 3.25 um. This is an
  inference from the data, checked in the notebook.
- Array centre. Found by matching the four footprints of the paper's geometry to the YP image (dark
  discs, 1.1-mm radius, against a ring 1.6 to 2.4 mm from each footprint centre). Where the match is
  weak (score below MATCH_MIN, a choice, shown with its effect in the notebook), the centre is the
  weighted centroid of the half-maximum region of the smoothed image, an assumption: the staining
  pattern is four-fold symmetric about the array centre in every condition.
- Burst labels. The files give the burst number only as a subject label (x1, x2, x3, x5), and
  their protocol text says that "upon completion of the protocol, it was either repeated 2, 3, or 5
  times". BURSTS gives the two readings: label = repeats after the first burst ("after_first",
  adopted: x1 is the paper's 2 bursts (x4) and x5 its largest number, 6 bursts (x4), Figure 7), or
  label = total number of bursts ("total").
- Lorentzian YP(x) = a (b/2)^2 / (x^2 + (b/2)^2) and Gaussian Pr(x) = a exp(-x^2 / (2 s^2)),
  FWHM = 2.4 s (Methods 2.5), fitted by least squares (claims file F4).
"""

from __future__ import annotations

import json
import re
import urllib.request
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import remfile
from scipy import stats
from scipy.ndimage import gaussian_filter, map_coordinates
from scipy.optimize import curve_fit
from scipy.signal import fftconvolve

DANDISET_ID = "001047"
DANDISET_VERSION = "0.250701.1609"
API = "https://api.dandiarchive.org/api"

PX_MM = 0.026  # pixel size of the reduced images
DIAG_GAP_MM = 15.3  # Methods 2.2
NEEDLE_MM = 2.8  # Methods 2.2
ELECTRODE_FROM_CENTRE_MM = DIAG_GAP_MM / 2 + NEEDLE_MM / 2  # along a diagonal
HALF_SIDE_MM = ELECTRODE_FROM_CENTRE_MM / np.sqrt(2)  # along each image axis
ROI_ALONG_MM, ROI_ACROSS_MM = 0.406, 0.325  # Methods 2.5
MATCH_MIN = 0.035  # a choice; see the module docstring

RATE = {"011": "0.2 MHz", "013": "1 Hz"}
BURSTS = {"after_first": {"x1": 2, "x2": 3, "x3": 4, "x5": 6}, "total": {"x1": 1, "x2": 2, "x3": 3, "x5": 5}}


def list_assets():
    """All assets of the pinned version, with their paths, sizes and ids."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=200"
    out = []
    while url:
        page = json.load(urllib.request.urlopen(url))
        out += page["results"]
        url = page["next"]
    return out


def version_metadata():
    return json.load(urllib.request.urlopen(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/"))


def _open(asset_id):
    return h5py.File(remfile.File(f"{API}/assets/{asset_id}/download/", verbose=False), "r")


def read_metadata(asset):
    """Session description, subject, image shape and stated pixel size of one file."""
    with _open(asset["asset_id"]) as f:
        desc = f["session_description"][()].decode()
        subj = {k: f["general/subject"][k][()].decode() for k in ("subject_id", "species", "strain", "description")}
        img = f["acquisition/SingleTimePointImaging"]
        shape = img["data"].shape
        res = float(img["data"].attrs.get("resolution", np.nan))
        acq_desc = img.attrs.get("description", "")
        start = f["session_start_time"][()].decode()
    return {"path": asset["path"], "asset_id": asset["asset_id"], "size": asset["size"], "desc": desc,
            "subject": subj, "shape": shape, "resolution_attr": res, "acq_desc": acq_desc, "start": start}


def parse(meta):
    """Exposure areas of one file: rate code, protocol, burst label, side, channel."""
    d = meta["desc"]
    name = meta["path"].split("/")[1].replace("_image.nwb", "")
    if name.startswith("sub-P"):  # CHO files, one well each
        m = re.search(r"Subject ID: (\S+), Fluorescent Channel: (\w+), Phase: (\w+).*?\. (\d+): 9 packets of pulses "
                      r"delivered at (\S+) frequency, (.+?), repeated (\d+) time", d)
        um = re.search(r'PhysicalSizeX="([\d.]+)"', d)
        return {"file": name, "cells": "CHO", "channel": m.group(2), "phase": m.group(3), "pixel_um": float(um.group(1)),
                "areas": [{"side": "W", "rate": m.group(4), "protocol": "CANCAN" if "CanCan" in m.group(6) else "control",
                           "label": "r" + m.group(7), "subject": m.group(1)}]}
    ch = re.search(r"Channel used: (\w+)", d).group(1)
    subs = list(dict.fromkeys(re.findall(r"(\d{3})(CC|Control|C)_x(\d)", d[:400])))
    sides = ["L", "R"] if len(subs) == 2 else ["W"]
    rows, cols = meta["shape"][1:]
    pixel_um = 1.625 if sides == ["W"] else 3.25  # inferred, see the module docstring
    # Hoechst (DAPI) images were acquired before the YP and Pr images of the same wells (checked
    # in the notebook from the acquisition times), as the paper's pre-exposure Hoechst images
    phase = "pre" if ch == "DAPI" else "post"
    # subject "011C_x5" (protocol code "C", "Unknown protocol type") is taken as a control: every
    # control subject carries the same "Unknown protocol type" text
    return {"file": name, "cells": "CT26", "channel": ch, "phase": phase, "pixel_um": pixel_um,
            "areas": [{"side": s, "rate": r, "protocol": "CANCAN" if p == "CC" else "control", "label": "x" + x,
                       "subject": f"{r}{p}_x{x}"} for (r, p, x), s in zip(subs, sides)]}


def _reduce(a, k):
    h, w = a.shape[0] // k * k, a.shape[1] // k * k
    return a[:h, :w].reshape(h // k, k, w // k, k).astype(np.float32).mean(axis=(1, 3))


def load_reduced(asset_id, pixel_um):
    """Stream one image and reduce it to PX_MM pixels by block means."""
    k = int(round(PX_MM * 1000 / pixel_um))
    with _open(asset_id) as f:
        a = f["acquisition/SingleTimePointImaging/data"][0]
    return _reduce(a, k), (int(a.min()), int(a.max()))


def _load(args):
    return load_reduced(*args)


def load_many(items, workers=10):
    """items: list of (asset_id, pixel_um). Returns reduced images in the same order."""
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(_load, items))


def split_areas(img, n_areas):
    if n_areas == 1:
        return [(img, 0)]
    h = img.shape[1] // 2
    return [(img[:, :h], 0), (img[:, h:], h)]


def _norm(A):
    lo, hi = np.percentile(A, [5, 99.5])
    return gaussian_filter(np.clip((A - lo) / (hi - lo), 0, 1), 2)


def match_footprints(A, half_side_mm=HALF_SIDE_MM):
    """Best match of the four footprints; returns (score, (row, col) of the centre)."""
    S = _norm(A)
    R = int(2.6 / PX_MM) + 1
    r = np.hypot(*np.mgrid[-R:R + 1, -R:R + 1])
    disc = (r <= 1.1 / PX_MM).astype(float)
    disc /= disc.sum()
    ring = ((r >= 1.6 / PX_MM) & (r <= 2.4 / PX_MM)).astype(float)
    ring /= ring.sum()
    d = fftconvolve(S, ring, "same") - fftconvolve(S, disc, "same")
    o = int(round(half_side_mm / PX_MM))
    H, W = d.shape
    if H <= 2 * o + 2 or W <= 2 * o + 2:
        return -np.inf, (H / 2, W / 2)
    sc = np.stack([d[o + dy:H - o + dy, o + dx:W - o + dx] for dy in (-o, o) for dx in (-o, o)]).min(0)
    i = np.unravel_index(np.argmax(sc), sc.shape)
    return float(sc[i]), (float(i[0] + o), float(i[1] + o))


def pattern_centroid(A):
    S = gaussian_filter(_norm(A), 10)
    m = S >= 0.5 * S.max()
    yy, xx = np.nonzero(m)
    w = S[m]
    return float((yy * w).sum() / w.sum()), float((xx * w).sum() / w.sum())


def locate(A):
    score, c = match_footprints(A)
    if score >= MATCH_MIN:
        return c, "footprints", score
    return pattern_centroid(A), "centroid", score


def roi_mean(A, centre, direction, x_mm):
    """Mean of A in a 406 x 325 um ROI centred x_mm from centre along unit vector direction
    (row, col); the long side lies along the line."""
    u = np.asarray(direction, float)
    v = np.array([-u[1], u[0]])
    s = np.arange(-ROI_ALONG_MM / 2 + 0.0065, ROI_ALONG_MM / 2, 0.013)
    t = np.arange(-ROI_ACROSS_MM / 2 + 0.0065, ROI_ACROSS_MM / 2, 0.013)
    S, T = np.meshgrid(s, t)
    pos = np.asarray(centre)[:, None, None] + ((x_mm + S) * u[:, None, None] + T * v[:, None, None]) / PX_MM
    vals = map_coordinates(A, pos.reshape(2, -1), order=1, mode="constant", cval=np.nan)
    return float(np.nanmean(vals)) if np.isfinite(vals).any() else np.nan


DIAGONALS = [np.array([1, 1]) / np.sqrt(2), np.array([1, -1]) / np.sqrt(2)]
PARALLEL = [np.array([1.0, 0.0]), np.array([0.0, 1.0])]
POS_WHOLE_MM = np.arange(-7, 8, 1.0)  # O1 reading a
POS_CONTIG_MM = np.arange(-18, 19) * ROI_ALONG_MM  # O1 reading b, to 7.3 mm


def background(A, centre):
    """Mean of 3 ROIs in each footprint (centre and 0.5 mm either side along its diagonal);
    returns the mean over the four footprints and the lowest footprint."""
    vals = []
    for u in DIAGONALS:
        for sgn in (-1, 1):
            vals.append(np.mean([roi_mean(A, centre, u, sgn * (ELECTRODE_FROM_CENTRE_MM + e)) for e in (-0.5, 0, 0.5)]))
    return float(np.mean(vals)), float(np.min(vals))


def profiles(A, centre, positions, directions):
    """Raw ROI means, one row per direction, one column per signed position."""
    return np.array([[roi_mean(A, centre, u, x) for x in positions] for u in directions])


def pool(prof, positions, reading):
    """O2 reading a: mean of the lines at each signed position; reading b: mean of the four
    half-lines at each distance, mirrored to negative distances."""
    if reading == "a":
        return positions, np.nanmean(prof, axis=0)
    dist = np.abs(positions)
    out = np.array([np.nanmean(prof[:, dist == d]) for d in dist])
    return positions, out


def lorentz(x, a, b):
    return a * (b / 2) ** 2 / (x ** 2 + (b / 2) ** 2)


def gauss(x, a, s):
    return a * np.exp(-x ** 2 / (2 * s ** 2))


def fit(fun, x, y, lim):
    """Least-squares fit over |x| <= lim. Returns params, R (Pearson of fit and data), its p, R2."""
    m = (np.abs(x) <= lim + 1e-9) & np.isfinite(y)
    xx, yy = x[m], y[m]
    if len(yy) < 4:
        return None
    p0 = [max(yy.max(), 1e-6), 2.0]
    try:
        p, _ = curve_fit(fun, xx, yy, p0=p0, bounds=([0, 1e-3], [np.inf, 100]), maxfev=20000)
    except RuntimeError:
        return None
    f = fun(xx, *p)
    r, pv = stats.pearsonr(f, yy)
    r2 = 1 - ((yy - f) ** 2).sum() / ((yy - yy.mean()) ** 2).sum()
    return {"a": p[0], "w": p[1], "R": r, "p": pv, "R2": r2, "n": int(m.sum())}


def fwhm(res, kind):
    if res is None:
        return np.nan
    return res["w"] if kind == "lorentz" else 2.4 * res["w"]


ARMS = ("long", "mean", "short")


def gap_significant(m1, se1, m2, se2, arm="long"):
    """The paper's reading of its plots (Methods 2.5): "A gap exceeding the length of the error
    bars indicates a significant difference at p<0.05". Where the two s.e. arms differ, the length
    the gap must exceed is not given; readings: the longer arm ("long", adopted: the gap exceeds
    each error bar, the literal reading), the mean of the two ("mean") or the shorter ("short")."""
    lo_hi = (m1 - se1, m2 + se2) if m1 > m2 else (m2 - se2, m1 + se1)
    gap = lo_hi[0] - lo_hi[1]
    need = {"long": max(se1, se2), "mean": (se1 + se2) / 2, "short": min(se1, se2)}[arm]
    return bool(gap > need), float(gap)
