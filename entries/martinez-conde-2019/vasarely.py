"""Loading and measures for CRCNS pvc-12, V1 responses to Vasarely-based illusions.

Martinez-Conde, McCamy, Troncoso, Otero-Millan & Macknik (2019), PLoS ONE 14(3): e0210941,
doi:10.1371/journal.pone.0210941. Data set doi:10.6080/K05D8Q1T.

The data set is one zip, V1_Vasarely_data.zip, streamed from the public S3 bucket and opened in
place; nothing is written to disk. It holds, per neuron and experiment (Corners, Star,
Edge-compare), a `<code>_SpikeRateMap.mat` and a `<code>_Stimulus.mat`, and a spreadsheet that
lists the cells. The data descriptor names the fields image, smoothed_image and
smoothed_image_norm. The files hold more than it says:

- `image` (480 x 640) is the unsmoothed spike rate map, spikes per 1 ms sample of eye time at
  each display unit (DU); one file also stores `eyetime`, and image * eyetime is an integer
  count there. `smoothed_image` is its smoothed version. Both are in gaze coordinates.
- `Standard`, in 60 of the 77 spike rate map files, holds the map registered to the stimulus,
  rotated so that the aligned fold is vertical and cropped to the region of interest (ROI), with
  the stimulus's equal-luminance polygons in the same frame (`EdgecompVert`, `DiagVert`,
  `CornersVert`) and, in 40 of them, `BaseActivity`. The registration from the gaze frame to
  `Standard` uses the neuron's receptive field position, which the files do not store, so a
  file without `Standard` cannot be registered here.

Where the parameters come from:

- Spike rate map: the smoothed map of `Standard` (`smoothed_image`), times 1000 to give spikes/s.
  The Fig 3B legend says the rate map is smoothed after division by eye time. The unsmoothed
  `Standard.image` is a variant (claim fig4b-spike-rate-difference).
- Geometry, all in the Standard frame and read from each file's own polygons: polygon k of
  the Square, the Star and the Edge rectangle is the k% equal-luminance boundary (k = 0..99,
  the last one collapsing to the 100% point); in Corners it is the (99 - k)% boundary, as the
  stimulus image shows (`check_luminance`). Fold ends (0% and 100%) come from polygons 0 and 99.
- Midpoint: the 8 x 8 DU square centred on the 50% point of the fold (Results, "Strength of
  neuronal responses", paragraph 1; Fig 2 legend). The Square and the Star have two symmetric
  midpoints on the aligned diagonal, averaged (Methods, Corners, paragraph 2).
- P180: the line in the rectangle 48 DU from the Edge, parallel to it (Methods, Square and edge:
  "3 DVA (48 DU) away from Edge in the rectangle at the 50% luminance line").
- Corners: of the two 40 degree folds, the bright one (Methods, Corners, paragraph 2, "We did
  not analyze dark corner-folds"). Which one is bright is decided from the stimulus: on a
  bright fold the luminance on the fold is higher than beside it on the same row, as on the
  Square's diagonal (Fig 1A legend, nested squares of decreasing luminance have bright
  diagonals). `fold_is_ridge` computes it.
- Blocks along a fold: ten non-overlapping blocks from 0% to 100% luminance, each 10% of the
  fold long and 8 DU wide (Results, "Responses averaged along the entire fold", paragraph 1).
- Absolute baseline, reading "squares": the mean rate in 16 x 16 DU squares in 0% luminance
  areas (Methods, Visual stimuli). Square and Edge: four squares inside the corners of the
  138 x 138 DU square centred on the Square (Methods, Square and edge; centred on the corners
  they would leave the ROI). Star: four squares inside the corners of the 300 x 300 DU square
  that circumscribes the 0% star's circumscribed circle (radius 150 DU; Methods, Star). Corners:
  the paper says only "two 1 x 1 DVA square regions in 0% luminance areas within the ROI"
  (Fig 2C shows them); the squares taken here are the two bottom corners of the ROI, the only
  0% band inside it. This placement is an assumption. The squares inside the corners are
  adopted because the Methods say the baseline was measured within the ROI, and squares centred
  on the corners of the Square and Edge cross its border; reading "centred" (squares centred on
  the corners, the part outside the ROI dropped) is a variant. Reading "dataset": the file's own
  `Standard.BaseActivity`, undocumented, present for 40 of the 60 registered files; the files'
  `smoothed_image_norm` is normalised by it (`norm_relation`).
- RMS contrast: 16 x 16 DU square centred on the Edge, moved from 0% to 100% in 1.5% steps
  (Results, "Neuron responses to corner-folds vs. different contrasts along edge"). The
  definition of RMS contrast is open; `rms_contrast` gives the readings of the claims file.
"""

from __future__ import annotations

import io
import re
import zipfile

import fsspec
import h5py
import numpy as np
import pandas as pd
import scipy.io as sio
from scipy.ndimage import map_coordinates
from scipy.signal import fftconvolve

DATASET_ID = "pvc-12"
DATASET_VERSION = "unversioned"   # CRCNS data sets have no versions; the zip's MD5 is pinned below
BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/pvc-12/live/"
ZIP_URL = BUCKET + "V1_Vasarely_data.zip"
ZIP_MD5 = "e1301fe463e72332e2303b2053ee0559"   # checksums.md5 of the data set
DOI = "10.6080/K05D8Q1T"

CONDITIONS = {"Edge-compare": "Square and Edge", "Star": "Star", "Corners": "Corners"}
DU_PER_DVA = 16
MID_SIZE = 8            # DU, midpoint square (Results; Fig 2 legend)
BLOCK_WIDTH = 8         # DU (Results, Responses averaged along the entire fold)
BASE_SIZE = 16          # DU, baseline squares (Methods, Visual stimuli)
CIRC_HALF = 69          # DU, half of the 138 DU square around the Square (Methods)
P180_OFFSET = 48        # DU from the Edge into the rectangle (Methods)
RMS_BOX = 16            # DU (Results, contrast section)
RMS_STEP = 1.5          # % luminance (Results, contrast section)
RATE_SCALE = 1000.0     # maps are spikes per 1 ms sample; times 1000 gives spikes/s

CODE_RE = re.compile(r"^(A[A-Z]{2})(\d+[JA]\d)([A-Z]?)$")


def open_zip() -> zipfile.ZipFile:
    """The data set's zip, opened in place over range requests."""
    return zipfile.ZipFile(fsspec.open(ZIP_URL, block_size=2**20).open())


def checksums() -> str:
    with fsspec.open(BUCKET + "checksums.md5", "rt") as f:
        return f.read()


def read_mat(z: zipfile.ZipFile, name: str):
    """The `dat` variable of a MATLAB file; files saved as v7.3 come back as an h5py File."""
    raw = z.read(name)
    try:
        return sio.loadmat(io.BytesIO(raw), squeeze_me=True, struct_as_record=False)["dat"]
    except NotImplementedError:
        return h5py.File(io.BytesIO(raw), "r")


def parse_code(stem: str) -> dict:
    """File code such as ABC07240J1D: experiment prefix, cell (as in the spreadsheet), suffix."""
    m = CODE_RE.match(stem)
    prefix, cell, suffix = m.groups()
    return {"prefix": prefix, "cell": cell, "suffix": suffix, "monkey": cell[-2]}


def spreadsheet(z: zipfile.ZipFile) -> pd.DataFrame:
    """V1_Vasarely_data_SMC.xlsx: one row per cell, an X under each experiment."""
    raw = pd.read_excel(io.BytesIO(z.read("V1_Vasarely_data/V1_Vasarely_data_SMC.xlsx")), header=None)
    head = raw.index[raw.eq("Cell").any(axis=1)][0]
    cols = raw.iloc[head].tolist()
    df = raw.iloc[head + 1:].copy()
    df.columns = cols
    df = df[[c for c in cols if isinstance(c, str)]].dropna(subset=["Cell"])
    df["Cell"] = df["Cell"].astype(str)
    for c in ["Corners", "Star", "Edge-Compare"]:
        df[c] = df[c].astype(str).str.strip().eq("X")
    return df.reset_index(drop=True)


def _dense(a):
    a = a.toarray() if hasattr(a, "toarray") else a
    return np.asarray(a, dtype=float)


def _poly(p) -> np.ndarray:
    return np.c_[np.asarray(p.x, float).ravel(), np.asarray(p.y, float).ravel()]


def _rigid(P: np.ndarray, Q: np.ndarray):
    """Rotation R and translation t with Q = P R^T + t (least squares)."""
    Pm, Qm = P.mean(0), Q.mean(0)
    U, _, Vt = np.linalg.svd((P - Pm).T @ (Q - Qm))
    R = (U @ Vt).T
    return R, Qm - R @ Pm


def frame_transform(stim, std, condition: str, every: bool = False):
    """Rotation R and translation t from the stimulus file's frame to the Standard frame,
    fitted on the equal-luminance polygons, which both files store (Q = P R^T + t). The star is
    symmetric under turns of 30 degrees, so its polygons fit several; `every` returns them all."""
    if condition == "Edge-compare":
        full, frame = stim.SquareVert, std.EdgecompVert.SquareVert
    elif condition == "Corners":
        full, frame = stim.CornersVert, std.CornersVert
    else:
        full, frame = stim.DiagVert, std.DiagVert
    fits = []
    # the star's vertices may be listed from another point, so try every cyclic shift
    for shift in (range(24) if condition == "Star" else [0]):
        P = np.vstack([np.roll(_poly(full[k]), shift, axis=0) for k in range(0, 90, 10)])
        Q = np.vstack([_poly(frame[k]) for k in range(0, 90, 10)])
        R, t = _rigid(P, Q)
        fits.append((np.abs(P @ R.T + t - Q).max(), R, t))
    fits.sort(key=lambda f: f[0])
    if every:
        return [(R, t) for err, R, t in fits if err < 1e-6]
    return fits[0][1], fits[0][2]


def _to_full(shape, R, t, margin: int = 0):
    H, W = shape
    cc, rr = np.meshgrid(np.arange(-margin, W + margin) + 1.0, np.arange(-margin, H + margin) + 1.0)
    return (np.c_[cc.ravel(), rr.ravel()] - t) @ R, (H + 2 * margin, W + 2 * margin)


def standard_stimulus(stim, std, condition: str) -> np.ndarray:
    """The file's stimulus image resampled into the Standard frame (nearest pixel); image pixel
    (row, col) has coordinates (x, y) = (col + 1, row + 1), as the image and its polygons show."""
    image = {"Edge-compare": "EdgecompImage", "Corners": "CornersImage", "Star": "DiagImage"}[condition]
    R, t = frame_transform(stim, std, condition)
    F, shape = _to_full(std.smoothed_image.shape, R, t)
    return map_coordinates(np.asarray(getattr(stim, image), float), [F[:, 1] - 1, F[:, 0] - 1], order=0,
                           cval=np.nan).reshape(shape)


def gaze_shift(full_map: np.ndarray, std_map: np.ndarray, R, t, margin: int = 420):
    """The shift (DU, display frame) that carries the stimulus-frame position of each Standard
    pixel to where the gaze-frame map holds its value, found by least squares over integer shifts
    in the Standard frame; with the correlation of the shifted map with `std_map`. It stands for
    the receptive field position, which the files do not store."""
    F, shape = _to_full(std_map.shape, R, t, margin)
    G = map_coordinates(full_map, [F[:, 1] - 1, F[:, 0] - 1], order=1, cval=0).reshape(shape)
    xc = fftconvolve(G, std_map[::-1, ::-1], mode="valid")
    g2 = fftconvolve(G ** 2, np.ones_like(std_map), mode="valid")
    i, j = np.unravel_index(np.argmin(g2 - 2 * xc), xc.shape)
    H, W = std_map.shape
    r = np.corrcoef(G[i:i + H, j:j + W].ravel(), std_map.ravel())[0, 1]
    return np.array([j - margin, i - margin], float) @ R, float(r)


def fold_geometry(std, condition: str) -> dict:
    """Folds as vertical segments in the Standard frame: x, y at 0% and y at 100% luminance.

    Read from the file's polygons (see the module docstring). Square and Star give two
    half-diagonals each; Corners gives both 40 degree folds, labelled by apex direction.
    """
    folds = {}
    if condition == "Edge-compare":
        sq0, sq99 = _poly(std.EdgecompVert.SquareVert[0]), _poly(std.EdgecompVert.SquareVert[99])
        cx, cy = sq99.mean(0)
        on_axis = sq0[np.abs(sq0[:, 0] - cx) < 1]
        for y0 in sorted(on_axis[:, 1]):
            folds["S90_" + ("near" if y0 < cy else "far")] = (cx, y0, cy)
        r0, r99 = _poly(std.EdgecompVert.RectVert[0]), _poly(std.EdgecompVert.RectVert[99])
        ex = r0[:, 0].min()
        inward = 1.0 if r0[:, 0].max() > ex else -1.0
        y_zero = r0[:, 1].max() if r99[:, 1].mean() < r0[:, 1].mean() else r0[:, 1].min()
        y_full = r99[:, 1].mean()
        folds["Edge"] = (ex, y_zero, y_full)
        folds["P180"] = (ex + inward * P180_OFFSET, y_zero, y_full)
        folds["_square_centre"] = (cx, cy)
    elif condition == "Star":
        p0, p99 = _poly(std.DiagVert[0]), _poly(std.DiagVert[99])
        cx, cy = p99.mean(0)
        r = np.hypot(p0[:, 0] - cx, p0[:, 1] - cy)
        outer = p0[(r > r.max() - 1) & (np.abs(p0[:, 0] - cx) < 1)]
        for x0, y0 in sorted(map(tuple, outer), key=lambda v: v[1]):
            folds["S52_" + ("upper" if y0 < cy else "lower")] = (cx, y0, cy)
        folds["_centre"] = (cx, cy)
        folds["_outer_radius"] = r.max()
    else:
        p0, p99 = _poly(std.CornersVert[0]), _poly(std.CornersVert[99])
        # apexes: vertices that move along y only; in polygon 0 the up-pointing apex is the
        # vertex with the smallest y, the down-pointing one is the local maximum inside the zigzag
        up = p0[np.argmin(p0[:, 1])]
        inner = p0[(p0[:, 0] > p0[:, 0].min() + 1) & (p0[:, 0] < p0[:, 0].max() - 1)]
        base_y = np.median(inner[:, 1])
        down = inner[np.argmax(np.where(inner[:, 1] < base_y + 200, inner[:, 1], -np.inf))]
        for name, apex in [("S40_up", up), ("S40_down", down)]:
            same_x = p99[np.abs(p99[:, 0] - apex[0]) < 0.5]
            k99 = same_x[np.argmin(np.abs(same_x[:, 1] - apex[1] - 100))]
            # Corners polygons run from 100% (k = 0) to 0% (k = 99); see check_luminance
            folds[name] = (apex[0], k99[1], apex[1])
    return folds


def box_mask(shape, x: float, y: float, w: float, h: float) -> np.ndarray:
    """Pixels whose centres (1-based coordinates) lie in [x - w/2, x + w/2) x [y - h/2, y + h/2)."""
    H, W = shape
    cols = np.arange(W) + 1.0
    rows = np.arange(H) + 1.0
    mc = (cols >= x - w / 2) & (cols < x + w / 2)
    mr = (rows >= y - h / 2) & (rows < y + h / 2)
    return mr[:, None] & mc[None, :]


def box_mean(M: np.ndarray, x: float, y: float, w: float, h: float | None = None) -> float:
    m = box_mask(M.shape, x, y, w, w if h is None else h)
    return float(M[m].mean()) if m.any() else np.nan


def point_at(fold, frac: float):
    """(x, y) at luminance fraction frac (0 = 0%, 1 = 100%) along a fold."""
    x, y0, y1 = fold
    return x, y0 + frac * (y1 - y0)


def midpoint(M, fold) -> float:
    x, y = point_at(fold, 0.5)
    return box_mean(M, x, y, MID_SIZE)


def blocks(M, fold, n: int = 10) -> np.ndarray:
    """Mean of M in n blocks from 0% to 100%, each 1/n of the fold long and 8 DU wide."""
    x, y0, y1 = fold
    L = abs(y1 - y0)
    return np.array([box_mean(M, x, y0 + (i + 0.5) / n * (y1 - y0), BLOCK_WIDTH, L / n)
                     for i in range(n)])


def fold_is_ridge(lum: np.ndarray, fold, side: float = 10.0) -> float:
    """Luminance on the fold minus beside it (same row, +-side DU), mean over 20% to 80%.

    Positive on a bright fold (luminance peaks on the fold), negative on a dark one.
    """
    x, y0, y1 = fold
    out = []
    for f in np.linspace(0.2, 0.8, 13):
        _, y = point_at(fold, f)
        on = box_mean(lum, x, y, 2)
        off = np.nanmean([box_mean(lum, x - side, y, 2), box_mean(lum, x + side, y, 2)])
        out.append(on - off)
    return float(np.nanmean(out))


def baseline_squares(shape, condition: str, folds: dict, placement: str = "inside") -> list[tuple[float, float]]:
    """Centres of the 16 x 16 DU baseline squares (reading "squares"; module docstring).

    placement "inside": each square inside a corner of the circumscribing square (the main
    reading); "centred": each square centred on the corner, the part outside the ROI dropped
    (a variant; the Methods say only "at the corners"). Corners has one placement."""
    H, W = shape
    s = BASE_SIZE / 2 if placement == "inside" else 0.0
    if condition == "Edge-compare":
        cx, cy = folds["_square_centre"]
        return [(cx + sx * (CIRC_HALF - s), cy + sy * (CIRC_HALF - s)) for sx in (-1, 1) for sy in (-1, 1)]
    if condition == "Star":
        cx, cy = folds["_centre"]
        R = folds["_outer_radius"]
        return [(cx + sx * (R - s), cy + sy * (R - s)) for sx in (-1, 1) for sy in (-1, 1)]
    s = BASE_SIZE / 2
    # Corners: the two bottom corners of the ROI, in the 0% band (an assumption)
    return [(s + 0.5, H - s + 0.5), (W - s + 0.5, H - s + 0.5)]


def baseline(M, centres) -> float:
    """Mean over the squares of each square's mean; a square wholly outside the map is dropped."""
    return float(np.nanmean([box_mean(M, x, y, BASE_SIZE) for x, y in centres]))


def norm_relation(sm: np.ndarray, sm_norm: np.ndarray, base: float) -> str:
    """How `smoothed_image_norm` relates to `smoothed_image` (both per 1 ms sample) and the
    file's BaseActivity: "difference" (sm - base), "index" ((sm - base) / (sm + base)), "all nan",
    or "other". Checked on the pixels where both are finite."""
    ok = np.isfinite(sm_norm) & np.isfinite(sm)
    if not ok.any():
        return "all nan"
    if not np.isfinite(base):
        return "other (no BaseActivity)"
    a, n = sm[ok], sm_norm[ok]
    if np.allclose(n, a - base, atol=1e-9):
        return "difference"
    den = a + base
    pos = den > 0
    if pos.any() and np.allclose(n[pos], (a[pos] - base) / den[pos], atol=1e-6):
        return "index"
    return "other"


def load_all(z: zipfile.ZipFile | None = None, shifts: bool = True) -> list[dict]:
    """Every spike rate map file with its stimulus, reduced to what the analysis uses."""
    z = z or open_zip()
    recs = []
    for name in sorted(z.namelist()):
        if not name.endswith("_SpikeRateMap.mat"):
            continue
        condition = name.split("/")[1]
        stem = name.split("/")[-1].split("_")[0]
        rec = {"file": stem, "condition": condition, **parse_code(stem)}
        d = read_mat(z, name)
        if isinstance(d, h5py.File):
            rec.update(format="v7.3", fields=sorted(d["dat"].keys()), registered=False)
            recs.append(rec)
            continue
        rec["format"] = "v5"
        rec["fields"] = list(d._fieldnames)
        img = _dense(d.image)
        rec["full_image_max"] = float(img.max())
        rec["full_smoothed_max_hz"] = float(np.asarray(d.smoothed_image).max() * RATE_SCALE)
        if hasattr(d, "eyetime"):
            et = _dense(d.eyetime)
            rec["eyetime_s"] = float(et.sum() / 1000)
            rec["eyetime_max"] = float(et.max())
            rec["spikes_from_eyetime"] = float(np.round(img * et).sum())
            rec["count_is_integer"] = bool(np.allclose(img * et, np.round(img * et)))
        sm = np.asarray(d.smoothed_image, float)
        rec["full_smoothed_median_hz"] = float(np.median(sm[sm > 0]) * RATE_SCALE)
        if hasattr(d, "norm"):
            rec["norm_values"] = np.atleast_1d(_dense(d.norm)).ravel()[:5].tolist()
        std = getattr(d, "Standard", None)
        if hasattr(d, "smoothed_image_norm"):
            base = float(std.BaseActivity) if std is not None and hasattr(std, "BaseActivity") else np.nan
            sn = _dense(d.smoothed_image_norm)
            rec["smoothed_norm_range"] = (float(np.nanmin(sn)), float(np.nanmax(sn))) if np.isfinite(sn).any() else (np.nan, np.nan)
            rec["smoothed_norm_relation"] = norm_relation(sm, sn, base)
        rec["registered"] = std is not None
        if std is not None:
            rec["std_fields"] = list(std._fieldnames)
            rec["rate"] = np.asarray(std.smoothed_image, float) * RATE_SCALE
            rec["rate_unsmoothed"] = _dense(std.image) * RATE_SCALE
            rec["base_dataset"] = (float(std.BaseActivity) * RATE_SCALE
                                   if hasattr(std, "BaseActivity") else np.nan)
            rec["folds"] = fold_geometry(std, condition)
            stim = read_mat(z, name.replace("_SpikeRateMap", "_Stimulus"))
            rec["lum"] = standard_stimulus(stim, std, condition)
            if shifts:
                found = [gaze_shift(np.asarray(d.smoothed_image, float), np.asarray(std.smoothed_image, float), R, t)
                         for R, t in frame_transform(stim, std, condition, every=True)]
                rec["gaze_shift"], rec["gaze_shift_r"] = max(found, key=lambda f: f[1])
            if condition == "Edge-compare":
                rec["std_rect"] = _poly(std.EdgecompVert.RectVert[0])
        recs.append(rec)
    return recs


def check_luminance(rec: dict) -> dict:
    """Stimulus luminance (0-100) at the 0%, 50% and 100% points of each fold, and on the
    baseline squares, read from the file's own stimulus image in the Standard frame."""
    lum = rec["lum"]
    out = {}
    for k, f in rec["folds"].items():
        if k.startswith("_"):
            continue
        for frac in (0.05, 0.5, 0.95):
            x, y = point_at(f, frac)
            out[f"{k}@{int(frac * 100)}%"] = box_mean(lum, x, y, 2)
        out[f"{k} ridge"] = fold_is_ridge(lum, f)
    centres = baseline_squares(lum.shape, rec["condition"], rec["folds"])
    out["baseline squares max lum"] = max(np.nanmax(lum[box_mask(lum.shape, x, y, BASE_SIZE, BASE_SIZE)])
                                          for x, y in centres)
    return out


def bright_corner_fold(rec: dict) -> str:
    """Name of the bright S40 fold of a Corners file (the one with the luminance ridge)."""
    r = {k: fold_is_ridge(rec["lum"], rec["folds"][k]) for k in ("S40_up", "S40_down")}
    return max(r, key=r.get)


def fold_measures(rec: dict, base: float, smoothed: bool = True) -> dict:
    """Per fold: midpoint response, midpoint spike rate difference and the ten block
    differences (halves of the Square and Star kept apart, as `<fold>_<half>`)."""
    M = rec["rate"] if smoothed else rec["rate_unsmoothed"]
    out = {}
    folds = rec["folds"]
    if rec["condition"] == "Edge-compare":
        names = {"Edge": ["Edge"], "P180": ["P180"], "S90": ["S90_near", "S90_far"]}
    elif rec["condition"] == "Star":
        names = {"S52": ["S52_upper", "S52_lower"]}
    else:
        bright = bright_corner_fold(rec)
        dark = "S40_down" if bright == "S40_up" else "S40_up"
        names = {"S40": [bright], "S40dark": [dark]}
    for fold, parts in names.items():
        mids = [midpoint(M, folds[p]) for p in parts]
        out[fold] = {
            "response": float(np.mean(mids)),
            "diff": float(np.mean(mids)) - base,
            "blocks": [blocks(M, folds[p]) - base for p in parts],
        }
    return out


def rms_contrast(lum: np.ndarray, edge_fold, levels: np.ndarray) -> pd.DataFrame:
    """Local RMS contrast of the stimulus in a 16 x 16 DU square centred on the Edge at each
    luminance level (%). Readings: (a) SD / mean of the luminance values; (b) SD of the
    luminance normalised to 0-1."""
    rows = []
    for L in levels:
        x, y = point_at(edge_fold, L / 100)
        v = lum[box_mask(lum.shape, x, y, RMS_BOX, RMS_BOX)]
        v = v[~np.isnan(v)]
        rows.append({"level": L, "a_sd_over_mean": v.std() / v.mean() if v.mean() > 0 else np.nan,
                     "b_sd_norm": (v / 100).std(), "mean_lum": v.mean()})
    return pd.DataFrame(rows)


def edge_response(M, edge_fold, level: float) -> float:
    """Mean of M in a 16 x 16 DU square centred on the Edge at a luminance level (%)."""
    x, y = point_at(edge_fold, level / 100)
    return box_mean(M, x, y, RMS_BOX)
