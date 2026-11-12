"""Loading and measures for CRCNS pvc-12 (Martinez-Conde et al. 2019, PLoS ONE 14(3) e0210941).

The data set is one zip, ``pvc-12/live/V1_Vasarely_data.zip``, read in place from the public S3
bucket ``crcnsarchive`` over range requests (docs/archives.md, "CRCNS"). It holds one folder per
experiment (``Corners``, ``Star``, ``Edge-compare``), and per neuron and experiment a
``<code>_SpikeRateMap.mat`` and a ``<code>_Stimulus.mat``, plus ``V1_Vasarely_data_SMC.xlsx``.

What the files hold, as found here (the data descriptor says otherwise in places):

- ``image``: the unsmoothed spike rate map on the 480 x 640 display-unit (DU) screen, in spikes
  per eye-time sample. In the one file that also holds ``eyetime`` (in samples, 1 kHz),
  ``image * eyetime`` is an integer spike count at every pixel, so the unit is spikes per ms;
  rates here are multiplied by 1000 to give spikes/s. The descriptor calls ``image`` the raw
  spike counts.
- ``smoothed_image``: ``image`` smoothed (Fig 3B legend: Gaussian, 16 DU, STD 7 DU).
- Both maps are in gaze coordinates: spikes are placed at the gaze position, not at the place of
  the stimulus the receptive field (RF) covered, so they are offset from the stimulus by the RF
  eccentricity, which no file states.
- ``Standard`` (in all Corners and Edge-compare files and 12 of the 27 star files): the authors'
  ROI-aligned maps (``image``, ``smoothed_image``), the stimulus polygons in the same frame
  (``CornersVert``, ``DiagVert``, ``EdgecompVert``), and in some files ``BaseActivity`` (the
  baseline, spikes per ms) and ``smoothed_image_norm``. This frame is the one of Fig 5: the fold
  aligned with the preferred orientation is vertical. The stimulus polygons of the screen and of
  ``Standard`` are related by a rotation and a translation (residual below 1e-9 DU), and the
  screen ``smoothed_image`` rotated by it and shifted correlates with the ``Standard`` one at r
  above 0.98 (shown in the notebook), so ``Standard`` is the screen map moved by the RF offset
  and rotated.
- ``*Vert`` polygons: 100 nested polygons per stimulus, polygon j at luminance 100 - j*100/99 %
  (Square, Star: 0 is the outermost, 0%; Corners: 0 is the 100% edge; the luminance of every
  location is checked against the stimulus image in the notebook).

Geometry (all in the ``Standard`` frame; vertex coordinates are MATLAB 1-based):

- Midpoint fold response: mean of the map in an 8 x 8 DU square centred on the fold's 50%
  luminance point (claims file, opening comment; Results, "Strength of neuronal responses",
  paragraph 1; Fig 2 legend).
- Square S90: the two half-diagonals from the centre (100%) to the corners (0%) on the vertical
  diagonal; Star S52: the two half-diagonals from the centre to the outer vertices on the vertical
  diagonal; both midpoints are averaged (Methods, "Corners", paragraph 2).
- Corners S40: the pattern has two 40 degree folds of opposite polarity. The bright one is where
  the corner of the luminance contours points towards lower luminance; the paper analysed "only
  ... symmetric bright corner-folds" (Methods, "Corners", paragraph 2). The claims file leaves
  open whether the two S40 folds are averaged, so both readings are computed (``corners_mode``).
- Edge: the short side of the rectangle, collinear with the Square's diagonal, 0% to 100%.
  P180: the line parallel to the Edge, 48 DU into the rectangle, through its 50% luminance line
  (Methods, "Square and edge").
- Blocks: ten non-overlapping blocks along each fold from 0% to 100%, each 10% of luminance long
  (15, 7, 15, 10 and 15 DU for P180, S90, S52, S40 and Edge, from the fold length in the data) and
  8 DU wide (Results, "Responses averaged along the entire fold", paragraph 1).
- Absolute baseline: the mean of the map in four 16 x 16 DU squares at the corners of the
  square circumscribing the Square (side 141.4 DU, its diagonal; the text says 8.84 DVA, which
  is 141.4 DU, and also 138 DU) or the Star's 0% polygon (side 300 DU), and for Corners in two
  16 x 16 DU squares in the 0% area (Methods, "Visual stimuli"). Where the squares are centred is
  not stated; the choice is checked against the files' ``BaseActivity`` in the notebook. For
  Corners the two squares' positions are not given in the text; see ``corners_baseline_centres``.
- Spike rate difference: response minus absolute baseline (Methods, "Spike rate and spike rate
  difference map").

Sampling uses bilinear interpolation on a 1 DU grid inside each square or block, a standard
choice that cannot change a result at these sizes.
"""

import io
import re
import zipfile

import fsspec
import h5py
import numpy as np
import scipy.io as sio
import scipy.sparse as sp
from scipy import ndimage

URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/pvc-12/live/V1_Vasarely_data.zip"
CHECKSUMS_URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/pvc-12/live/checksums.md5"
ZIP_MD5 = "e1301fe463e72332e2303b2053ee0559"  # from the data set's checksums.md5
ROOT = "V1_Vasarely_data/"
XLSX = ROOT + "V1_Vasarely_data_SMC.xlsx"

PER_MS_TO_PER_S = 1000.0  # maps are in spikes per 1 ms eye-time sample (see module docstring)

CODE_RE = re.compile(r"^(ABC|ABD|ABS|AEC)(\d{5,6})([JA])(\d)([A-Z]?)$")
PREFIX_CONDITION = {"ABC": "Corners", "ABD": "Star", "ABS": "Corners", "AEC": "Square and Edge"}
VERT = {"Corners": "CornersVert", "Star": "DiagVert", "Edge-compare": "SquareVert"}
IMG = {"Corners": "CornersImage", "Star": "DiagImage", "Edge-compare": "EdgecompImage"}

_ZIP = None


def zip_file():
    """The data set's zip, opened in place over HTTP range requests."""
    global _ZIP
    if _ZIP is None:
        _ZIP = zipfile.ZipFile(fsspec.open(URL, block_size=2**20).open())
    return _ZIP


def parse_code(code):
    """Split a file code such as ``ABD07240J1B`` into prefix, cell (``07240J1``), monkey, suffix."""
    m = CODE_RE.match(code)
    if not m:
        raise ValueError(code)
    prefix, date, monkey, num, suffix = m.groups()
    return {"prefix": prefix, "cell": f"{date}{monkey}{num}", "monkey": monkey, "suffix": suffix}


def list_files():
    """One row per spike rate map: folder, code, and the parsed code."""
    rows = []
    for n in zip_file().namelist():
        parts = n.split("/")
        if len(parts) == 3 and parts[2].endswith("_SpikeRateMap.mat"):
            code = parts[2].split("_")[0]
            rows.append({"folder": parts[1], "code": code, "path": n, **parse_code(code)})
    return sorted(rows, key=lambda r: (r["folder"], r["code"]))


def _arr(a):
    return a.toarray() if sp.issparse(a) else np.asarray(a, float)


def load_mat(path):
    """Return ('v5', struct) or ('h5', group) for the ``dat`` variable of a MATLAB file."""
    b = zip_file().read(path)
    if b"MATLAB 7.3" in b[:128]:
        return "h5", h5py.File(io.BytesIO(b), "r")["dat"]
    return "v5", sio.loadmat(io.BytesIO(b))["dat"][0, 0]


def polygons(s):
    """A MATLAB struct array of polygons (fields x, y) as an array (n_poly, n_vert, 2)."""
    return np.array([np.c_[np.asarray(s[j, 0]["x"], float).ravel(),
                           np.asarray(s[j, 0]["y"], float).ravel()] for j in range(s.shape[0])])


def fit_rigid(a, b):
    """Least-squares similarity b ~ s R a + t; returns s, R, t and the largest residual."""
    a0, b0 = a.mean(0), b.mean(0)
    u, sv, vt = np.linalg.svd((b - b0).T @ (a - a0))
    r = u @ vt
    s = sv.sum() / ((a - a0) ** 2).sum()
    t = b0 - s * r @ a0
    return s, r, t, np.abs(b - (s * (r @ a.T).T + t)).max()


def warp(img, s, r, t, shape, shift=(0.0, 0.0), order=1):
    """Resample a screen image into a frame of ``shape`` under u = s R x + t + shift (1-based)."""
    h, w = shape
    yy, xx = np.mgrid[0:h, 0:w].astype(float)
    u = np.c_[xx.ravel() + 1 - shift[0], yy.ravel() + 1 - shift[1]]
    x = (r.T @ (u - t).T).T / s
    return ndimage.map_coordinates(img, [x[:, 1] - 1, x[:, 0] - 1], order=order, cval=0).reshape(h, w)


def register_shift(screen, s, r, t, target, pad=600):
    """Integer shift (in the target frame) that best aligns the rotated screen map with target."""
    big = warp(screen, s, r, t + np.array([pad, pad]), (target.shape[0] + 2 * pad, target.shape[1] + 2 * pad))
    hh, ww = big.shape[0] + target.shape[0], big.shape[1] + target.shape[1]
    fa = np.fft.fft2(big - big.mean(), (hh, ww))
    fb = np.fft.fft2(target - target.mean(), (hh, ww))
    c = np.real(np.fft.ifft2(fa * np.conj(fb)))
    i, j = np.unravel_index(np.argmax(c), c.shape)
    i = i - hh if i > hh // 2 else i
    j = j - ww if j > ww // 2 else j
    shift = (-(j - pad), -(i - pad))
    moved = warp(screen, s, r, t, target.shape, shift=shift)
    return shift, float(np.corrcoef(moved.ravel(), target.ravel())[0, 1])


def load_record(row, with_screen=False):
    """Read one neuron and experiment: maps (spikes/s), the Standard frame, vertices, luminance."""
    folder = row["folder"]
    kind, d = load_mat(row["path"])
    skind, st = load_mat(row["path"].replace("_SpikeRateMap", "_Stimulus"))
    rec = {**row, "mat": kind, "stim_mat": skind}
    if skind == "h5":
        rec["stim_type"] = "".join(chr(c) for c in np.array(st["type"]).ravel())
        rec["stimulus"] = np.array(st["image"]).T
        rec["fields"] = sorted(k for k in d.keys()) if kind == "h5" else list(d.dtype.names)
        rec["has_standard"] = False
        if with_screen:
            rec["screen_smoothed"] = (np.array(d["smoothed_image"]).T if kind == "h5"
                                      else _arr(d["smoothed_image"])) * PER_MS_TO_PER_S
        return rec
    rec["stim_type"] = {"Corners": "CORNERS", "Star": "STAR", "Edge-compare": "EDGE-COMPARE"}[folder]
    rec["fields"] = list(d.dtype.names)
    rec["stimulus"] = np.asarray(st[IMG[folder]], float)
    rec["screen_poly"] = polygons(st[VERT[folder]])
    if folder == "Edge-compare":
        rec["screen_rect"] = polygons(st["RectVert"])
    if with_screen or "Standard" not in d.dtype.names:
        rec["screen_smoothed"] = _arr(d["smoothed_image"]) * PER_MS_TO_PER_S
        rec["screen_image"] = _arr(d["image"]) * PER_MS_TO_PER_S
    if "eyetime" in d.dtype.names:
        rec["eyetime"] = _arr(d["eyetime"])
        rec["screen_image"] = _arr(d["image"]) * PER_MS_TO_PER_S
    rec["has_standard"] = "Standard" in d.dtype.names
    if not rec["has_standard"]:
        return rec
    S = d["Standard"][0, 0]
    rec["smoothed"] = _arr(S["smoothed_image"]) * PER_MS_TO_PER_S
    rec["raw"] = _arr(S["image"]) * PER_MS_TO_PER_S
    vname = [q for q in S.dtype.names if q.endswith("Vert")][0]
    vv = S[vname]
    if "x" in vv.dtype.names:
        rec["poly"] = polygons(vv)
    else:
        rec["poly"] = polygons(vv[0, 0]["SquareVert"])
        rec["rect"] = polygons(vv[0, 0]["RectVert"])
    rec["base_activity"] = (float(np.asarray(S["BaseActivity"]).ravel()[0]) * PER_MS_TO_PER_S
                            if "BaseActivity" in S.dtype.names else np.nan)
    # Screen-to-Standard transform from the polygons. The Star's 24 vertices are symmetric under
    # rotations of 30 degrees, so its vertex order is matched by trying every cyclic shift.
    a = rec["screen_poly"]
    best = None
    if rec["folder"] == "Edge-compare":
        # the rectangle breaks the Square's symmetry, so both are fitted together, in file order
        s, r, t, err = fit_rigid(np.r_[a.reshape(-1, 2), rec["screen_rect"].reshape(-1, 2)],
                                 np.r_[rec["poly"].reshape(-1, 2), rec["rect"].reshape(-1, 2)])
        best = (s, r, t, err, 0)
    for k in range(a.shape[1] if best is None else 0):
        s, r, t, err = fit_rigid(np.roll(a, k, axis=1).reshape(-1, 2), rec["poly"].reshape(-1, 2))
        if np.linalg.det(r) > 0 and (best is None or err < best[3]):
            best = (s, r, t, err, k)
    rec["transform"] = best
    rec["lum"] = warp(rec["stimulus"], best[0], best[1], best[2], rec["smoothed"].shape, order=1)
    return rec


# ---------------------------------------------------------------- geometry in the Standard frame

def folds(rec, corners_mode="bright"):
    """Fold segments as lists of (P0, P100) in the Standard frame (1-based x, y), per fold name.

    corners_mode: "bright" (the bright S40 fold only), "both" (the two S40 folds, averaged) or
    "dark" (the dark S40 fold, shown for reference).
    """
    p = rec["poly"]
    out = {}
    if rec["folder"] == "Edge-compare":
        centre = p[-1].mean(0)
        outer = p[0]
        on_axis = outer[np.argsort(np.abs(outer[:, 0] - centre[0]))[:2]]
        out["S90"] = [(c, centre) for c in on_axis]
        r0, r99 = rec["rect"][0], rec["rect"][-1]
        # the Edge: the short side of the rectangle whose line passes through the Square's centre
        sides = [(r0[i], r0[(i + 1) % 4]) for i in range(4)]
        lengths = [np.linalg.norm(b - a) for a, b in sides]
        short = [sd for sd, ln in zip(sides, lengths) if ln < max(lengths) - 1]
        edge = min(short, key=lambda sd: abs((sd[0] - centre)[0] * (sd[1] - sd[0])[1]
                                             - (sd[0] - centre)[1] * (sd[1] - sd[0])[0]))
        hi = [q for q in edge if np.min(np.linalg.norm(r99 - q, axis=1)) < 1e-6]
        lo = [q for q in edge if np.min(np.linalg.norm(r99 - q, axis=1)) >= 1e-6]
        p100, p0 = hi[0], lo[0]
        out["Edge"] = [(p0, p100)]
        # P180: parallel to the Edge, 48 DU into the rectangle
        into = r0.mean(0) - (p0 + p100) / 2
        d = p100 - p0
        n = np.array([-d[1], d[0]]) / np.linalg.norm(d)
        n = n if np.dot(n, into) > 0 else -n
        out["P180"] = [(p0 + 48 * n, p100 + 48 * n)]
    elif rec["folder"] == "Star":
        centre = p[-1].mean(0)
        outer = p[0]
        r = np.linalg.norm(outer - centre, axis=1)
        tips = outer[r > r.max() - 1]
        on_axis = tips[np.argsort(np.abs(tips[:, 0] - centre[0]))[:2]]
        out["S52"] = [(c, centre) for c in on_axis]
    elif rec["folder"] == "Corners":
        segs = []
        for i in range(p.shape[1]):
            a, b = p[0, i], p[-1, i]
            # an apex: a vertex whose neighbours are not collinear with it, on the travel axis
            prev, nxt = p[0, i - 1], p[0, (i + 1) % p.shape[1]]
            if np.linalg.norm(b - a) < 1:
                continue
            v1, v2 = prev - a, nxt - a
            if np.linalg.norm(v1) < 1e-6 or np.linalg.norm(v2) < 1e-6:
                continue
            ang = np.degrees(np.arccos(np.clip(np.dot(v1, v2) / np.linalg.norm(v1) / np.linalg.norm(v2), -1, 1)))
            if 30 < ang < 50:
                segs.append((b, a, ang))  # polygon 0 is 100%, polygon 99 is 0%
        bright, dark = [], []
        for p0, p100, ang in segs:
            # bright fold: at its midpoint the luminance beside the fold is below 50%
            mid = (p0 + p100) / 2
            d = (p100 - p0) / np.linalg.norm(p100 - p0)
            n = np.array([-d[1], d[0]])
            side = np.mean([sample_point(rec["lum"], mid + k * n) for k in (-15, 15)])
            (bright if side < 50 else dark).append((p0, p100))
        rec["corners_polarity"] = (len(bright), len(dark))
        out["S40"] = {"bright": bright, "both": bright + dark, "dark": dark}[corners_mode]
    return out


def sample_point(img, xy):
    return float(ndimage.map_coordinates(img, [[xy[1] - 1], [xy[0] - 1]], order=1)[0])


def box_mean(img, centre, direction, length, width):
    """Mean of img over a length x width box centred at ``centre``, long axis along ``direction``."""
    d = np.asarray(direction, float)
    d = d / np.linalg.norm(d)
    n = np.array([-d[1], d[0]])
    a = np.arange(length) - (length - 1) / 2
    b = np.arange(width) - (width - 1) / 2
    aa, bb = np.meshgrid(a, b)
    pts = centre + aa.ravel()[:, None] * d + bb.ravel()[:, None] * n
    return float(ndimage.map_coordinates(img, [pts[:, 1] - 1, pts[:, 0] - 1], order=1).mean())


def midpoint_response(img, segs):
    """8 x 8 DU square at the 50% point of each segment, averaged over segments."""
    return float(np.mean([box_mean(img, (p0 + p100) / 2, p100 - p0, 8, 8) for p0, p100 in segs]))


def block_profile(img, segs):
    """Ten 8 DU wide blocks from 0% to 100% per segment; array (n_segments, 10)."""
    prof = []
    for p0, p100 in segs:
        d = p100 - p0
        ln = np.linalg.norm(d) / 10
        prof.append([box_mean(img, p0 + (i + 0.5) / 10 * d, d, ln, 8) for i in range(10)])
    return np.array(prof)


def lum_at_fraction(rec, segs, f):
    return float(np.mean([sample_point(rec["lum"], p0 + f * (p100 - p0)) for p0, p100 in segs]))


def baseline_centres(rec):
    """Centres of the baseline squares in the Standard frame (Star, Square and Edge)."""
    p = rec["poly"]
    centre = p[-1].mean(0)
    outer = p[0]
    half = np.abs(outer - centre).max()  # half the side of the circumscribing square
    return [centre + np.array([sx, sy]) * half for sx in (-1, 1) for sy in (-1, 1)]


def baseline(img, centres, size=16):
    return float(np.mean([box_mean(img, c, (1, 0), size, size) for c in centres]))


def baseline_centres_inside(rec):
    """Variant: the 16 x 16 DU squares drawn inside the corners of the circumscribing square."""
    centre = rec["poly"][-1].mean(0)
    half = np.abs(rec["poly"][0] - centre).max() - 8
    return [centre + np.array([sx, sy]) * half for sx in (-1, 1) for sy in (-1, 1)]


def corners_baseline_centres(rec):
    """Corners: two 16 x 16 DU squares in the 0% area of the ROI (Methods, "Corners").

    The text says only that the two squares are in 0% luminance areas within the ROI, "shown in
    Fig 2C", whose drawing is not in the text read. Assumption: the two bottom corners of the ROI,
    8 DU in from each side, which are 0% in every file (checked in the notebook) and lie on either
    side of the folds, as Fig 2C's two squares are described.
    """
    h, w = rec["smoothed"].shape
    return [np.array([8.5 + 1, h - 8.5]), np.array([w - 8.5, h - 8.5])]


def baseline_value(rec, img, reading="centred"):
    """Absolute baseline (spikes/s) under a reading: "centred", "inside" or "files".

    "files" is the file's own ``BaseActivity`` (NaN where the file has none).
    """
    if reading == "files":
        return rec["base_activity"]
    if rec["folder"] == "Corners":
        return baseline(img, corners_baseline_centres(rec))
    return baseline(img, baseline_centres(rec) if reading == "centred" else baseline_centres_inside(rec))


FOLD_ANGLE = {"P180": 180, "S90": 90, "S52": 52, "S40": 40}
FOLD_ORDER = ["Edge", "P180", "S90", "S52", "S40"]
CONDITION_OF_FOLD = {"Edge": "Square and Edge", "P180": "Square and Edge", "S90": "Square and Edge",
                     "S52": "Star", "S40": "Corners"}


def neuron_table(recs, corners_mode="bright", baseline_reading="centred", map_name="smoothed"):
    """One row per neuron and fold: midpoint response, baseline, spike rate difference and blocks.

    ``blocks`` holds the ten block means of the spike rate difference per segment
    (n_segments x 10, from 0% to 100% luminance).
    """
    import pandas as pd
    rows = []
    for r in recs:
        if not r.get("has_standard"):
            continue
        img = r[map_name]
        base = baseline_value(r, img, baseline_reading)
        for fold, segs in folds(r, corners_mode).items():
            rows.append({"code": r["code"], "cell": r["cell"], "monkey": r["monkey"], "fold": fold,
                         "condition": CONDITION_OF_FOLD[fold], "mid": midpoint_response(img, segs),
                         "base": base, "blocks": block_profile(img, segs) - base})
    df = pd.DataFrame(rows)
    df["diff"] = df["mid"] - df["base"]
    return df


def block_summaries(df, halves="averaged"):
    """Per-neuron min, max, mean and median over the ten blocks.

    halves: "averaged" (two segments averaged block by block, reading i) or "separate" (each
    segment summarised on its own, then the summaries averaged, reading ii).
    """
    out = []
    for _, row in df.iterrows():
        b = row["blocks"]
        if halves == "averaged":
            b = b.mean(0, keepdims=True)
        s = np.array([[x.min(), x.max(), x.mean(), np.median(x)] for x in b]).mean(0)
        out.append(s)
    return np.array(out)


def rms_contrast_profile(rec, steps=np.arange(0, 100.0001, 1.5), size=16, reading="a"):
    """Local RMS contrast of the stimulus in a 16 x 16 DU square centred on the Edge.

    reading "a": standard deviation of pixel luminance over its mean; "b": standard deviation of
    luminance scaled to 0 to 1 (claims file, fig7a-rms-contrast-fit). Luminance is the stimulus
    image in percent, as the file holds it.
    """
    p0, p100 = folds(rec)["Edge"][0]
    d = (p100 - p0) / np.linalg.norm(p100 - p0)
    n = np.array([-d[1], d[0]])
    a = np.arange(size) - (size - 1) / 2
    aa, bb = np.meshgrid(a, a)
    out = []
    for lv in steps:
        c = p0 + lv / 100 * (p100 - p0)
        pts = c + aa.ravel()[:, None] * d + bb.ravel()[:, None] * n
        w = ndimage.map_coordinates(rec["lum"], [pts[:, 1] - 1, pts[:, 0] - 1], order=1)
        out.append(w.std() / w.mean() if reading == "a" and w.mean() > 0 else
                   (w / 100).std() if reading == "b" else np.nan)
    return np.asarray(steps, float), np.array(out)


def fit_exponential_lar(x, y):
    """f(l) = a exp(-b l) + c by Levenberg-Marquardt, then least absolute residuals (MATLAB's
    'LAR' robust option, Methods, "Edge RMS contrast model"), started from the paper's values."""
    from scipy.optimize import least_squares, minimize
    ok = np.isfinite(y)
    x, y = x[ok], y[ok]
    f = lambda p, xx: p[0] * np.exp(-p[1] * xx) + p[2]
    p_lm = least_squares(lambda p: f(p, x) - y, [-0.34, 0.05, 0.95], method="lm").x
    p = minimize(lambda p: np.abs(f(p, x) - y).sum(), p_lm, method="Nelder-Mead",
                 options={"xatol": 1e-8, "fatol": 1e-10, "maxiter": 20000}).x
    r2 = 1 - ((y - f(p, x)) ** 2).sum() / ((y - y.mean()) ** 2).sum()
    return p, r2


def edge_response(rec, img, base, lum_points, size=16):
    """Mean spike rate difference in a 16 x 16 DU square centred on the Edge at each luminance
    (percent along the Edge from 0% to 100%; Results, "Neuron responses to corner-folds vs.
    different contrasts along edge", paragraph 1)."""
    p0, p100 = folds(rec)["Edge"][0]
    return np.array([box_mean(img, p0 + lv / 100 * (p100 - p0), p100 - p0, size, size) for lv in lum_points]) - base
