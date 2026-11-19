"""Loading and measures for CRCNS pvc-12 (Martinez-Conde et al. 2019, PLoS ONE 14:e0210941).

The data set is one zip, V1_Vasarely_data.zip, in the public S3 bucket crcnsarchive under
pvc-12/live/. It is streamed and opened in place (fsspec range requests and zipfile); nothing
is written to disk.

What the files hold (checked in the notebook's data check, not taken from the descriptor):

- One folder per condition: Edge-compare (the paper's Square and Edge), Star and Corners. Per
  recording, <code>_SpikeRateMap.mat and <code>_Stimulus.mat. The code is a prefix (AEC, ABC,
  ABD or ABS) followed by the cell code listed in V1_Vasarely_data_SMC.xlsx, sometimes with a
  trailing block letter; the letter before the last digit of the cell code is the monkey (J or A).
- SpikeRateMap `dat.image`: spike count divided by eye time in ms at each screen DU, in gaze
  coordinates (480 x 640). It is spikes per ms, so x 1000 gives spikes/s (shown in the notebook
  with the one recording that also holds `eyetime`).
- `dat.Standard`: the region of interest (ROI) in stimulus coordinates, rotated so that the
  aligned fold is vertical, with `image` and `smoothed_image` (same units) and the vertices of
  the 100 nested luminance polygons in that frame (`SquareVert`/`RectVert`, `DiagVert` or
  `CornersVert`). Not every recording has it.
- Stimulus `dat.<X>Image`: the grey level (0 to 100) of every screen DU, and the same polygons
  in screen coordinates. The two vertex sets are related by an exact rotation and shift, which
  is used here to sample the stimulus luminance into the Standard frame.

Parameters and where they come from:

- Spike rate map: `Standard.smoothed_image` x 1000, the rate map smoothed after dividing by eye
  time (Fig 3B legend, cited by the claim fig4b-spike-rate-difference). The unsmoothed
  `Standard.image` is offered as the variant the claim names.
- Midpoint fold response: mean in an 8 x 8 DU square centred on the fold's 50% luminance point
  (Results, Strength of neuronal responses, paragraph 1). The 50% point is taken between the
  vertices of polygons 49 and 50 (polygon i has grey level about i/99 x 100 along the Square and
  Edge and Star folds and about (99 - i)/99 x 100 along the Corners fold, so the 50% point is
  between the same two polygons; checked against the sampled stimulus in the notebook). Which 8 pixels make an 8 DU span is a standard choice
  (pixel centres within 4 DU of the centre, rounded); it cannot change a result beyond a pixel.
- Square (S90) and Star (S52): the two symmetric midpoints on the aligned diagonal are averaged
  (Methods, Corners, paragraph 2).
- P180: the line 48 DU from the Edge inside the rectangle (Methods, Square and edge).
- Corners S40: the bright fold only (Methods, Corners, paragraph 2). The bright fold is the
  tooth of the zigzag that points into the 0% side, identified from the sampled luminance
  (luminance on the fold above that 10 DU to either side) and matching Fig 2C.
- Absolute baseline: mean rate in 16 x 16 DU squares in 0% luminance areas (Methods, Visual
  stimuli). Square and Edge: four squares inside the corners of the 138 x 138 DU square
  circumscribing the Square (Methods, Square and edge); Star: four squares inside the corners
  of the square circumscribing the 0% star polygon (Methods, Star); Corners: two squares in
  0% areas, placed inside the two ROI corners on the 0% side, as Fig 2C (lower panel) draws
  them (the text gives no position; the figure was read from the journal's page).
- Blocks along a fold: ten non-overlapping blocks from 0% to 100%, each 8 DU wide and one tenth
  of the fold's length (Results, Responses averaged along the entire fold, paragraph 1). The
  block order matters only for the profiles drawn; the Table 1 and Fig 6 summaries do not use it.
- Edge squares for Fig 7: 16 x 16 DU squares centred on the Edge at a luminance level (Results,
  Neuron responses to corner-folds vs. different contrasts along edge, paragraph 1).
"""
from __future__ import annotations

import io
import re
import zipfile

import fsspec
import numpy as np
import scipy.io as sio
import scipy.sparse as sp
from scipy.ndimage import map_coordinates

URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/pvc-12/live/V1_Vasarely_data.zip"
ROOT = "V1_Vasarely_data/"
CONDITIONS = {"Edge-compare": "square_edge", "Star": "star", "Corners": "corners"}
STIM_KEY = {"square_edge": "EdgecompImage", "star": "DiagImage", "corners": "CornersImage"}
VERT_KEYS = {"square_edge": ["SquareVert", "RectVert"], "star": ["DiagVert"], "corners": ["CornersVert"]}
FOLDS = {"square_edge": ["Edge", "P180", "S90"], "star": ["S52"], "corners": ["S40"]}
P180_OFFSET = 48.0       # DU from the Edge (Methods, Square and edge)
SQUARE_BASE_SIDE = 138.0  # DU, circumscribing square (Methods, Square and edge)
MID_BOX = 8               # DU (Results, Strength of neuronal responses, paragraph 1)
BASE_BOX = 16             # DU (Methods, Visual stimuli)
BLOCK_WIDTH = 8           # DU (Results, Responses averaged along the entire fold)
EDGE_BOX = 16             # DU (Results, Neuron responses ... along edge, paragraph 1)


def open_zip():
    """Open the data set's zip in place over HTTP range requests."""
    f = fsspec.open(URL, block_size=2**20).open()
    return zipfile.ZipFile(f)


def list_recordings(z):
    """One row per SpikeRateMap file: folder, condition, file code, cell code, monkey."""
    rows = []
    for n in sorted(z.namelist()):
        m = re.match(ROOT + r"([^/]+)/(.+)_SpikeRateMap\.mat$", n)
        if not m:
            continue
        folder, code = m.groups()
        c = re.match(r"A(?:EC|BC|BD|BS)(\d{5,6}[JA]\d)", code)
        rows.append(dict(folder=folder, condition=CONDITIONS[folder], code=code, cell=c.group(1),
                         monkey=c.group(1)[-2], map_path=n,
                         stim_path=n.replace("_SpikeRateMap.mat", "_Stimulus.mat")))
    return rows


def _dense(a):
    return a.toarray() if sp.issparse(a) else np.asarray(a, dtype=float)


def read_mat(z, path):
    """Return ('v5', struct) for MATLAB 5 files, or ('v73', bytes) for MATLAB 7.3 (HDF5) files."""
    b = z.read(path)
    if b"MATLAB 7.3" in b[:128]:
        return "v73", b
    return "v5", sio.loadmat(io.BytesIO(b))["dat"][0, 0]


def _verts(struct, keys):
    out = {}
    for k in keys:
        out[k] = np.stack([np.c_[struct[k][i, 0]["x"].ravel(), struct[k][i, 0]["y"].ravel()]
                           for i in range(struct[k].shape[0])])
    return out


def sample_stimulus(img, M, shape, stim_offset=1.0):
    """Grey level of the stimulus image at each pixel of the Standard frame (nearest pixel; NaN
    off the display), through the affine map M from Standard to screen coordinates."""
    H, W = shape
    yy, xx = np.mgrid[0:H, 0:W]
    sc = np.c_[xx.ravel(), yy.ravel(), np.ones(xx.size)] @ M - stim_offset
    return map_coordinates(img, [sc[:, 1], sc[:, 0]], order=0, cval=np.nan).reshape(H, W)


def load_recording(z, rec, stim_offset=1.0):
    """Load one recording's Standard-frame maps (spikes/s) and the stimulus luminance there.

    stim_offset: the stimulus image is indexed from 0 here while the vertices are MATLAB
    coordinates; 1.0 (the default) treats the vertices as 1-based pixel coordinates, which the
    notebook checks against the position of the Edge in the sampled image.
    """
    kind, d = read_mat(z, rec["map_path"])
    out = dict(rec, format=kind, has_standard=False)
    if kind != "v5":
        return out
    out["fields"] = d.dtype.names
    full = _dense(d["image"])
    out["full_image_sum"] = float(full.sum())
    # recording-wide summaries of the gaze-frame map (spikes/s), to compare recordings with and
    # without the aligned map: the mean over pixels with a nonzero rate, and the fraction of such pixels
    out["full_rate_nonzero_mean"] = 1000.0 * float(full[full > 0].mean()) if (full > 0).any() else np.nan
    out["full_coverage"] = float((full > 0).mean())
    if "eyetime" in d.dtype.names:
        out["eyetime"] = _dense(d["eyetime"])
        out["full_image"] = _dense(d["image"])
    if "Standard" not in d.dtype.names:
        return out
    st = d["Standard"][0, 0]
    cond = rec["condition"]
    vs = st["EdgecompVert"][0, 0] if "EdgecompVert" in st.dtype.names else st
    out["has_standard"] = True
    out["standard_fields"] = st.dtype.names
    out["rate"] = 1000.0 * np.asarray(st["smoothed_image"], float)
    out["rate_raw"] = 1000.0 * _dense(st["image"])
    out["std_sum_ratio"] = float(out["rate"].sum() / out["rate_raw"].sum())
    out["base_stored"] = 1000.0 * float(st["BaseActivity"][0, 0]) if "BaseActivity" in st.dtype.names else np.nan
    out["verts"] = _verts(vs, VERT_KEYS[cond])
    _, s = read_mat(z, rec["stim_path"])
    sverts = _verts(s, VERT_KEYS[cond])
    # The vertex order of a polygon can differ between the two files (a cyclic shift or a
    # reversal), and the 12-point star fits exactly under several orders (its symmetries).
    # Among the exact rigid fits, the one whose off-display region best matches the pixels of
    # the Standard map with no coverage (rate exactly 0) is used; proper rotations are preferred.
    H, W = out["rate"].shape
    yy, xx = np.mgrid[0:H, 0:W]
    img = np.asarray(s[STIM_KEY[cond]], float)
    zero = out["rate_raw"] == 0
    fits = []
    nv = {k: sverts[k].shape[1] for k in VERT_KEYS[cond]}
    for shift in range(max(nv.values())):
        for direction in (1, -1):
            P = np.vstack([out["verts"][k].reshape(-1, 2) for k in VERT_KEYS[cond]])
            Q = np.vstack([sverts[k][:, (direction * np.arange(nv[k]) + shift) % nv[k], :].reshape(-1, 2)
                           for k in VERT_KEYS[cond]])
            A = np.c_[P, np.ones(len(P))]
            M = np.linalg.lstsq(A, Q, rcond=None)[0]
            err = float(np.abs(A @ M - Q).max())
            fits.append((err, M, shift, direction))
            if shift == 0 and direction == 1:
                out["identity_fit_error"] = err
    emin = min(f[0] for f in fits)
    exact = [f for f in fits if f[0] < max(1e-6, 2 * emin)]
    scored = []
    for err, M, shift, direction in exact:
        lum = sample_stimulus(img, M, (H, W), stim_offset)
        off = np.isnan(lum)
        match = float(zero[off].mean()) if off.any() else 1.0
        proper = np.linalg.det(M[:2]) > 0
        scored.append((proper, match, -shift, err, M, shift, direction, lum))
    proper, match, _, err, M, shift, direction, lum = max(scored, key=lambda t: (t[0], t[1], t[2]))
    out["frame_fit_error"] = err
    out["frame_M"] = M
    out["frame_candidates"] = len(exact)
    out["offscreen_zero_match"] = match
    out["vertex_shift"] = (shift, direction)
    out["frame_rotation"] = float(np.degrees(np.arctan2(M[0, 1], M[0, 0])))
    out["lum"] = lum
    # Pixels of the ROI that fall off the display hold no stimulus; they are left out of every
    # measure (a choice: the paper says only that the rectangle was sometimes partly off the
    # display, Methods, Square and edge).
    out["offscreen"] = np.isnan(out["lum"])
    out["rate_unmasked"] = out["rate"].copy()
    for k in ("rate", "rate_raw"):
        out[k] = np.where(out["offscreen"], np.nan, out[k])
    return out


# ---------------------------------------------------------------- geometry (Standard frame)

def _fold_track(V, j):
    """Points of vertex j over the 100 polygons: index 0 is polygon 0, index 99 polygon 99."""
    return V[:, j, :]


def _mid(track):
    return (track[49] + track[50]) / 2.0


def _dark_first(V, j, lum):
    """(start, end) of the track of vertex j, ordered so that the start is the 0% end. In the Corners
    files polygon 0 is at the bright end of the fold, so the track is reversed there (shown by the
    block luminance profiles in the notebook's data check)."""
    t = _fold_track(V, j)
    lo, hi = [lum[int(round(t[i][1])), int(round(t[i][0]))] for i in (10, 89)]
    return (t[99], t[0]) if lo > hi else (t[0], t[99])


def geometry(rec):
    """Folds (each a list of halves, each a (start, end) pair with start at the 0% end),
    midpoints, baseline squares (x0, y0 top-left, side) and the Edge for one recording."""
    cond = rec["condition"]
    g = dict(folds={}, baseline=[])
    H, W = rec["rate"].shape
    lum = rec["lum"]
    if cond == "square_edge":
        S = rec["verts"]["SquareVert"]
        R = rec["verts"]["RectVert"]
        c = S[99].mean(0)
        # vertices of the Square on the vertical (aligned) diagonal
        js = [j for j in range(S.shape[1]) if abs(S[0, j, 0] - c[0]) < 1]
        halves = [(_fold_track(S, j)[0], c) for j in js]
        mids = [_mid(_fold_track(S, j)) for j in js]
        g["folds"]["S90"] = dict(halves=halves, mids=mids)
        # Edge: rectangle vertex whose track moves along the Edge
        moving = [j for j in range(R.shape[1]) if np.linalg.norm(R[0, j] - R[98, j]) > 50]
        far = [j for j in moving if abs(R[0, j, 0] - c[0]) < 1][0]
        fixed_end = [j for j in range(R.shape[1]) if j not in moving and abs(R[0, j, 0] - c[0]) < 1][0]
        e0, e1 = R[0, far], R[0, fixed_end]
        g["folds"]["Edge"] = dict(halves=[(e0, e1)], mids=[(R[49, far] + R[50, far]) / 2])
        across = [j for j in range(R.shape[1]) if j not in (far, fixed_end) and j in moving][0]
        u = R[0, across] - R[0, far]
        u = u / np.linalg.norm(u)
        g["folds"]["P180"] = dict(halves=[(e0 + P180_OFFSET * u, e1 + P180_OFFSET * u)],
                                  mids=[g["folds"]["Edge"]["mids"][0] + P180_OFFSET * u])
        g["edge"] = (e0, e1)
        h = SQUARE_BASE_SIDE / 2
        for sx in (-1, 1):
            for sy in (-1, 1):
                g["baseline"].append((c[0] + sx * h - (BASE_BOX if sx > 0 else 0),
                                      c[1] + sy * h - (BASE_BOX if sy > 0 else 0)))
        g["base_corners"] = [(c[0] + sx * h, c[1] + sy * h) for sx in (-1, 1) for sy in (-1, 1)]
    elif cond == "star":
        D = rec["verts"]["DiagVert"]
        c = D[99].mean(0)
        r0 = np.linalg.norm(D[0] - c, axis=1)
        js = [j for j in range(D.shape[1]) if abs(D[0, j, 0] - c[0]) < 1 and r0[j] > r0.mean()]
        g["folds"]["S52"] = dict(halves=[(D[0, j], c) for j in js], mids=[_mid(_fold_track(D, j)) for j in js])
        h = r0.max()
        for sx in (-1, 1):
            for sy in (-1, 1):
                g["baseline"].append((c[0] + sx * h - (BASE_BOX if sx > 0 else 0),
                                      c[1] + sy * h - (BASE_BOX if sy > 0 else 0)))
        g["base_corners"] = [(c[0] + sx * h, c[1] + sy * h) for sx in (-1, 1) for sy in (-1, 1)]
    elif cond == "corners":
        C = rec["verts"]["CornersVert"]
        # apex vertices: those whose x lies strictly between the base vertices of a tooth
        cand = [j for j in range(C.shape[1]) if 0 <= C[0, j, 0] <= W and
                abs(C[0, j, 1] - np.median(C[0, :, 1])) > 30]
        cand = sorted(set(cand), key=lambda j: C[0, j, 0])
        info = []
        for j in cand:
            m = _mid(_fold_track(C, j))
            x, y = int(round(m[0])), int(round(m[1]))
            side = np.nanmean([lum[y, x - 10], lum[y, x + 10]])
            info.append((lum[y, x] - side, j, m))
        bright = max(info, key=lambda t: t[0])
        dark = min(info, key=lambda t: t[0])
        j = bright[1]
        g["folds"]["S40"] = dict(halves=[_dark_first(C, j, lum)], mids=[bright[2]])
        g["dark_S40"] = dict(halves=[_dark_first(C, dark[1], lum)], mids=[dark[2]])
        g["bright_contrast"] = (bright[0], dark[0])
        top, bottom = np.nanmean(lum[:16]), np.nanmean(lum[-16:])
        y0 = 0 if top < bottom else H - BASE_BOX
        g["baseline"] = [(0, y0), (W - BASE_BOX, y0)]
        g["base_corners"] = g["baseline"]
    return g


# ---------------------------------------------------------------- measures

def window(M, r0, c0, h, w):
    """The part of the h x w window with top-left pixel (r0, c0) that lies inside M. The ends are
    clipped at 0 too, so that a window wholly above or left of M is empty (a negative slice end
    would otherwise wrap around)."""
    return M[max(r0, 0):max(r0 + h, 0), max(c0, 0):max(c0 + w, 0)]


def _window_mean(M, r0, c0, h, w):
    sub = window(M, r0, c0, h, w)
    return float(np.nanmean(sub)) if sub.size and np.isfinite(sub).any() else np.nan


def box_mean(M, cx, cy, w, h=None):
    """Mean of M over the w x h pixels centred on (cx, cy) (x = column, y = row)."""
    h = w if h is None else h
    c0 = int(np.floor(cx - w / 2 + 0.5))
    r0 = int(np.floor(cy - h / 2 + 0.5))
    return _window_mean(M, r0, c0, h, w)


def square_mean(M, x0, y0, w):
    """Mean of M over the w x w pixels with top-left corner at (x0, y0)."""
    c0, r0 = int(round(x0)), int(round(y0))
    return _window_mean(M, r0, c0, w, w)


def baseline(M, g):
    """Mean over the baseline squares that are on the display (NaN when none is)."""
    vals = np.array([square_mean(M, x0, y0, BASE_BOX) for x0, y0 in g["baseline"]])
    return float(np.nanmean(vals)) if np.isfinite(vals).any() else np.nan


def midpoint(M, fold):
    return float(np.mean([box_mean(M, m[0], m[1], MID_BOX) for m in fold["mids"]]))


def blocks(M, start, end, n=10, width=BLOCK_WIDTH):
    """Means of n blocks from start (0%) to end (100%) along a vertical fold."""
    start, end = np.asarray(start, float), np.asarray(end, float)
    out = []
    for k in range(n):
        a = start + (end - start) * k / n
        b = start + (end - start) * (k + 1) / n
        cx = (a[0] + b[0]) / 2
        ylo, yhi = min(a[1], b[1]), max(a[1], b[1])
        rows = np.arange(int(np.ceil(ylo - 0.5)), int(np.ceil(yhi - 0.5)))
        rows = rows[(rows >= 0) & (rows < M.shape[0])]
        c0 = int(np.floor(cx - width / 2 + 0.5))
        cols = np.arange(c0, c0 + width)
        cols = cols[(cols >= 0) & (cols < M.shape[1])]
        out.append(float(np.nanmean(M[np.ix_(rows, cols)])) if rows.size and cols.size else np.nan)
    return np.array(out)


def edge_point(g, level):
    """Point on the Edge at a luminance level in percent (0 at polygon 0)."""
    e0, e1 = g["edge"]
    return e0 + (e1 - e0) * level / 100.0


def rms_contrast(patch, reading):
    p = patch[~np.isnan(patch)]
    if reading == "a":
        return float(p.std() / p.mean())
    return float((p / 100.0).std())
