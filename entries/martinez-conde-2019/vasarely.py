"""Loading and measures for CRCNS pvc-12, V1 responses to Vasarely-based illusions.

Martinez-Conde, McCamy, Troncoso, Otero-Millan & Macknik (2019), PLoS ONE 14(3): e0210941,
doi:10.1371/journal.pone.0210941.

The data set is one zip file, V1_Vasarely_data.zip, read in place from the public S3 bucket
crcnsarchive over range requests; nothing is written to disk. CRCNS data sets are not
versioned, so the zip's MD5 sum from the data set's checksums.md5 is recorded (`ZIP_MD5`).

Each neuron and condition has a `<prefix><cell>_SpikeRateMap.mat` and a `_Stimulus.mat` file,
in the folders Edge-compare (Square and Edge), Star and Corners. The map file's `dat` holds
`image` (480 x 640, screen frame), `smoothed_image`, `smoothed_image_norm` and `Standard`, the
same maps cut out and rotated into the region of interest (ROI) with the aligned fold vertical,
the stimulus's luminance polygons in that frame (100 levels) and `BaseActivity`. What the data
show about these fields (checked in the notebook):

- `image` is spikes per 1 ms eye sample: its nonzero values are 1/n (one spike over n samples),
  so it is the spike count divided by the eye time, in spikes per ms, and not raw spike counts
  as the data description says. Multiplying by 1000 (`RATE_SCALE`) gives spikes/s; the 1 kHz eye
  sampling is in the Methods ("We recorded eye movements ... at 1 kHz").
- `smoothed_image` is `image` smoothed; `smoothed_image_norm` is (smoothed_image - BaseActivity)
  divided by (its maximum - BaseActivity). The spike rate map of the paper is `smoothed_image`
  ("dividing the spike count by the Eye Time. The resulting 2D image was subsequently smoothed",
  Fig 3B legend), so all measures use `Standard.smoothed_image` x 1000.
- The polygon vertices are in MATLAB 1-based pixel coordinates (x = column, y = row): a pixel
  with 0-based index (i, j) has coordinates (j + 1, i + 1); rasterising the screen-frame
  polygons reproduces the stimulus images best with this offset. Luminance is the number of
  polygons containing a pixel for Square, Edge rectangle and Star, and 100 minus it for Corners.

Where the parameters come from:

- Midpoint fold response: mean of the spike rate map in an 8 x 8 DU square centred on the fold's
  50% luminance point (claims file, opening comment; Results, "Strength of neuronal responses",
  paragraph 1). Square and Star average their two symmetric midpoints (Methods, Corners,
  paragraph 2). P180 is the 50% luminance line of the rectangle 48 DU from the Edge (Methods,
  Square and edge). The Edge midpoint is the 50% point of the Edge (claim table1-edge).
- Blocks: ten non-overlapping blocks of 10% luminance along the gradient, 8 DU wide, 15, 15, 7,
  15 and 10 DU long for Edge, P180, S90, S52 and S40 (Results, "Responses averaged along the
  entire fold", paragraph 1). The block lengths are computed from the polygons (the luminance
  lines), which give 15.15, 15.15, 7.07, 15.0 and 10.0 DU.
- Edge RMS contrast: a 16 x 16 DU square centred on the Edge moved in 1.5% luminance steps; RMS
  contrast fit with f(l) = a exp(-b l) + c (Results, "Neuron responses to corner-folds vs.
  different contrasts along edge", paragraph 1; Methods, Edge RMS contrast model). Ten RMS levels
  0.610 to 0.943 in steps of 0.037, mapped to luminance by the inverse fit; the Edge response at
  each is the mean in a 16 x 16 DU square centred there (same paragraph).
- Absolute baseline: four (Square and Edge, Star) or two (Corners) 16 x 16 DU squares in 0%
  luminance (Methods, Visual stimuli). The squares of Square and Edge and of Star are at the
  corners of the circumscribing square (138 DU for the Square, the 300 DU square around the
  Star's circumscribed circle). Whether they sit inside the corners or are centred on them is not
  stated; `baseline_squares` gives both, and the notebook compares them with the stored
  `BaseActivity`. The Corners squares are only drawn in Fig 2C, so for Corners the stored
  `BaseActivity` is the baseline (an assumption, stated in the notebook).
- Pixel selection in a box: pixels whose coordinates lie in [c - w/2, c + w/2) on each axis. This
  is a standard choice; a half-pixel shift cannot change a result.
"""

from __future__ import annotations

import io
import re
import zipfile

import fsspec
import numpy as np
import pandas as pd
import scipy.io as sio
import scipy.sparse as sp
from matplotlib.path import Path

ZIP_URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/pvc-12/live/V1_Vasarely_data.zip"
ZIP_MD5 = "e1301fe463e72332e2303b2053ee0559"   # pvc-12/live/checksums.md5
DOI = "10.6080/K05D8Q1T"
DATASET = "crcns:pvc-12"
VERSION = "unversioned"     # CRCNS data sets are not versioned (docs/archives.md)
ROOT = "V1_Vasarely_data"
RATE_SCALE = 1000.0          # spikes per 1 ms eye sample -> spikes/s
CONDITIONS = ["Edge-compare", "Star", "Corners"]
VERT_FIELD = {"Edge-compare": "EdgecompVert", "Star": "DiagVert", "Corners": "CornersVert"}
MID_BOX = 8                  # DU, midpoint square
BLOCK_WIDTH = 8              # DU
BASE_BOX = 16                # DU
RMS_BOX = 16                 # DU
P180_OFFSET = 48             # DU from the Edge, inside the rectangle
SQUARE_CIRCUMSCRIBING = 138  # DU (Methods, Square and edge)

_CELL = re.compile(r"^([A-Z]{3})(\d+)([JA])(\d)([A-Z]?)$")


def open_zip() -> zipfile.ZipFile:
    """The data set's zip, opened in place over HTTP range requests."""
    return zipfile.ZipFile(fsspec.open(ZIP_URL, block_size=2**20).open())


def file_table(z: zipfile.ZipFile) -> pd.DataFrame:
    """One row per neuron and condition folder: file code, neuron identifier, monkey."""
    rows = []
    for name in z.namelist():
        parts = name.split("/")
        if len(parts) != 3 or not parts[2].endswith("_SpikeRateMap.mat"):
            continue
        code = parts[2][: -len("_SpikeRateMap.mat")]
        m = _CELL.match(code)
        rows.append(dict(folder=parts[1], code=code, prefix=m.group(1),
                         neuron=m.group(2) + m.group(3) + m.group(4), monkey=m.group(3),
                         suffix=m.group(5),
                         has_stimulus=f"{ROOT}/{parts[1]}/{code}_Stimulus.mat" in z.namelist()))
    return pd.DataFrame(rows).sort_values(["folder", "neuron"]).reset_index(drop=True)


def read_sheet(z: zipfile.ZipFile) -> pd.DataFrame:
    """The data set's list of cells and conditions (V1_Vasarely_data_SMC.xlsx), as booleans."""
    raw = pd.read_excel(io.BytesIO(z.read(f"{ROOT}/V1_Vasarely_data_SMC.xlsx")), header=None)
    head = raw.index[raw.eq("Cell").any(axis=1)][0]
    col = raw.columns[raw.loc[head].eq("Cell")][0]
    table = raw.loc[head + 1:, col:col + 3]
    table.columns = ["neuron", "Corners", "Star", "Edge-compare"]
    table = table.dropna(subset=["neuron"])
    for c in ["Corners", "Star", "Edge-compare"]:
        table[c] = table[c].astype(str).str.strip().eq("X")
    table["neuron"] = table["neuron"].astype(str).str.strip()
    return table.reset_index(drop=True)


def _dense(a):
    return a.toarray() if sp.issparse(a) else np.asarray(a)


def _polys(arr) -> list[np.ndarray]:
    return [np.c_[arr[k, 0]["x"].ravel(), arr[k, 0]["y"].ravel()] for k in range(arr.shape[0])]


def load_map(z: zipfile.ZipFile, folder: str, code: str) -> dict:
    """One neuron and condition: its aligned (Standard) maps in spikes/s and polygons.

    Keys present depend on the file: `smoothed` and `image` (Standard frame), `base_stored`
    (Standard.BaseActivity, spikes/s), the polygons, and for Star the screen-frame
    `screen_smoothed` with the screen-frame polygons of the stimulus file. `fields` and
    `standard_fields` list what the file holds. Files in MATLAB 7.3 format (only one, a
    misfiled stimulus, see the notebook) are not read: `fields` is None.
    """
    out = dict(folder=folder, code=code, fields=None, standard_fields=None)
    try:
        dat = sio.loadmat(io.BytesIO(z.read(f"{ROOT}/{folder}/{code}_SpikeRateMap.mat")))
    except NotImplementedError:
        return out
    dat = dat["dat"][0, 0]
    out["fields"] = list(dat.dtype.names)
    nz = _dense(dat["image"])
    nz = nz[nz > 0]
    # share of nonzero screen-frame values that are 1/n (one spike over n eye samples)
    out["screen_one_over_n"] = float(np.mean(np.abs(1 / nz - np.round(1 / nz)) < 1e-6))
    if folder == "Star":
        out["screen_smoothed"] = _dense(dat["smoothed_image"]) * RATE_SCALE
        try:
            st = sio.loadmat(io.BytesIO(z.read(f"{ROOT}/{folder}/{code}_Stimulus.mat")))
            out["screen_polys"] = _polys(st["dat"][0, 0]["DiagVert"])
        except (NotImplementedError, ValueError):
            pass
    if "eyetime" in dat.dtype.names:
        out["screen_eyetime"] = _dense(dat["eyetime"])
        out["screen_image"] = _dense(dat["image"])
    if "Standard" not in dat.dtype.names:
        return out
    std = dat["Standard"][0, 0]
    out["standard_fields"] = list(std.dtype.names)
    out["image"] = _dense(std["image"]) * RATE_SCALE
    out["smoothed"] = _dense(std["smoothed_image"]) * RATE_SCALE
    if "BaseActivity" in std.dtype.names:
        out["base_stored"] = float(std["BaseActivity"][0, 0]) * RATE_SCALE
    if "smoothed_image_norm" in std.dtype.names:
        out["norm"] = _dense(std["smoothed_image_norm"])
    v = std[VERT_FIELD[folder]]
    if folder == "Edge-compare":
        out["square"] = _polys(v[0, 0]["SquareVert"])
        out["rect"] = _polys(v[0, 0]["RectVert"])
    else:
        out["polys"] = _polys(v)
    return out


def stimulus_type(z: zipfile.ZipFile, folder: str, code: str) -> str:
    """The stimulus's image field name, or the `type` string of a MATLAB 7.3 stimulus file."""
    raw = z.read(f"{ROOT}/{folder}/{code}_Stimulus.mat")
    try:
        dat = sio.loadmat(io.BytesIO(raw))["dat"][0, 0]
        return [n for n in dat.dtype.names if n.endswith("Image")][0]
    except NotImplementedError:
        import h5py
        with h5py.File(io.BytesIO(raw), "r") as h:
            return "v7.3 type " + "".join(map(chr, h["dat/type"][()].ravel()))


# ---------------------------------------------------------------- geometry (Standard frame)

def box_mean(m: np.ndarray, cx: float, cy: float, wx: float, wy: float) -> float:
    """Mean of map `m` over pixels whose 1-based coordinates lie in the box centred at (cx, cy)."""
    xs = np.arange(m.shape[1]) + 1.0
    ys = np.arange(m.shape[0]) + 1.0
    cols = (xs >= cx - wx / 2) & (xs < cx + wx / 2)
    rows = (ys >= cy - wy / 2) & (ys < cy + wy / 2)
    if not cols.any() or not rows.any():
        return np.nan
    return float(m[np.ix_(rows, cols)].mean())


def geometry(rec: dict) -> dict:
    """Fold lines in the Standard frame, from the luminance polygons.

    Each fold is (x, y at 0% luminance, y at 100% luminance) on a vertical line; the 50% point is
    halfway, since luminance is linear along each fold (Methods, Visual stimuli).
    """
    g = {}
    if rec["folder"] == "Edge-compare":
        rect0, rect99 = rec["rect"][0], rec["rect"][-1]
        x_edge = rect0[:, 0].min()
        y_top, y_bottom = rect0[:, 1].min(), rect0[:, 1].max()
        # Luminance = polygon count: the top of the rectangle is in every polygon (100%).
        y100, y0 = y_top, y_bottom
        g["Edge"] = [(x_edge, y0, y100)]
        g["P180"] = [(x_edge + P180_OFFSET, y0, y100)]
        sq0 = rec["square"][0]
        cx = sq0[:, 0].mean()
        top, bottom = sq0[:, 1].min(), sq0[:, 1].max()
        cy = (top + bottom) / 2
        g["S90"] = [(cx, top, cy), (cx, bottom, cy)]
        g["square_centre"] = (cx, cy)
    elif rec["folder"] == "Star":
        p0 = rec["polys"][0]
        cx = np.median(p0[:, 0])
        top, bottom = p0[:, 1].min(), p0[:, 1].max()
        cy = (top + bottom) / 2
        g["S52"] = [(cx, top, cy), (cx, bottom, cy)]
        g["star_centre"] = (cx, cy)
        g["star_radius"] = (bottom - top) / 2
    else:
        p0, p99 = rec["polys"][0], rec["polys"][-1]
        # The two S40 vertices of the zigzag; the bright fold is the one pointing towards
        # decreasing luminance (Corners luminance = 100 - polygon count, so luminance falls
        # with y): the downward vertex, the maximum of y on the zigzag.
        zig = p0[(p0[:, 1] < p0[:, 1].max() - 1)]
        down = zig[np.argmax(zig[:, 1])]
        down99 = p99[(p99[:, 1] < p99[:, 1].max() - 1)]
        down99 = down99[np.argmax(down99[:, 1])]
        step = (down99[1] - down[1]) / 99.0
        g["S40"] = [(down[0], down[1] + 100 * step, down[1])]   # 0% below, 100% at the level-0 vertex
        up = zig[np.argmin(zig[:, 1])]
        g["S40_dark"] = [(up[0], up[1], up[1] + 100 * step)]
    return g


def baseline_squares(rec: dict, g: dict, placement: str = "inside") -> list[tuple[float, float]]:
    """Centres of the 16 x 16 DU baseline squares (Square and Edge, Star).

    placement "inside": squares inside the corners of the circumscribing square;
    "centred": squares centred on its corners.
    """
    if rec["folder"] == "Edge-compare":
        (cx, cy), half = g["square_centre"], SQUARE_CIRCUMSCRIBING / 2
    elif rec["folder"] == "Star":
        (cx, cy), half = g["star_centre"], g["star_radius"]
    else:
        return []
    d = half - BASE_BOX / 2 if placement == "inside" else half
    return [(cx + sx * d, cy + sy * d) for sx in (-1, 1) for sy in (-1, 1)]


def baseline_from_map(m: np.ndarray, centres) -> float:
    vals = [box_mean(m, x, y, BASE_BOX, BASE_BOX) for x, y in centres]
    return float(np.nanmean(vals))


def midpoint(m: np.ndarray, folds) -> float:
    """Mean over the fold's midpoints of the 8 x 8 DU square at 50% luminance."""
    return float(np.mean([box_mean(m, x, (y0 + y1) / 2, MID_BOX, MID_BOX) for x, y0, y1 in folds]))


def blocks(m: np.ndarray, fold) -> np.ndarray:
    """Means of the ten 10% luminance blocks, from 0% to 100%, along one fold line."""
    x, y0, y1 = fold
    edges = np.linspace(y0, y1, 11)
    out = []
    for a, b in zip(edges[:-1], edges[1:]):
        out.append(box_mean(m, x, (a + b) / 2, BLOCK_WIDTH, abs(b - a)))
    return np.array(out)


def luminance_point(fold, lum_percent: float) -> tuple[float, float]:
    x, y0, y1 = fold
    return x, y0 + (y1 - y0) * lum_percent / 100.0


# ---------------------------------------------------------------- Edge luminance image

def edge_luminance(rec: dict) -> np.ndarray:
    """Luminance (0-100) of the Square and Edge stimulus in the Standard frame, from its polygons."""
    shape = rec["smoothed"].shape
    yy, xx = np.mgrid[0:shape[0], 0:shape[1]]
    pts = np.c_[xx.ravel() + 1.0, yy.ravel() + 1.0]
    lum = np.zeros(len(pts))
    for poly in rec["rect"] + rec["square"]:
        lum += Path(poly).contains_points(pts)
    return lum.reshape(shape)


def corners_baseline_squares(rec: dict) -> list[tuple[float, float]]:
    """Centres of the two Corners baseline squares: the bottom corners of the Standard frame.

    The paper only draws them (Fig 2C, "two 1 x 1 DVA (16 x 16 DU) square regions in 0%
    luminance areas within the ROI"). The bottom corners of the frame are in 0% luminance in every
    file (below the last luminance line); this placement is an assumption.
    """
    h, w = rec["smoothed"].shape
    half = BASE_BOX / 2
    return [(half + 0.5, h - half + 0.5), (w - half + 0.5, h - half + 0.5)]


FOLDS = {"Edge-compare": ["Edge", "P180", "S90"], "Star": ["S52"], "Corners": ["S40", "S40_dark"]}


def measures(rec: dict, smoothed: bool = True) -> dict:
    """Per-neuron measures in the Standard frame (spikes/s, not baseline-subtracted).

    midpoint_<fold>: the 8 x 8 DU midpoint mean (two midpoints averaged for S90 and S52);
    blocks_<fold>: array (n halves, 10 blocks) from 0% to 100% luminance;
    base_inside / base_centred (Square and Edge, Star), base_corners (Corners), base_stored.
    `smoothed=False` uses the unsmoothed rate map (Standard.image).
    """
    m = rec["smoothed"] if smoothed else rec["image"]
    g = geometry(rec)
    out = {}
    if rec["folder"] == "Corners":
        out["base_main"] = baseline_from_map(m, corners_baseline_squares(rec))
    else:
        out["base_main"] = baseline_from_map(m, baseline_squares(rec, g, "inside"))
        out["base_centred"] = baseline_from_map(m, baseline_squares(rec, g, "centred"))
    out["base_stored"] = rec.get("base_stored", np.nan)
    for f in FOLDS[rec["folder"]]:
        out[f"midpoint_{f}"] = midpoint(m, g[f])
        out[f"blocks_{f}"] = np.array([blocks(m, fold) for fold in g[f]])
        # the same midpoint square moved 32 DU (2 DVA) sideways, off the fold, for the data check
        out[f"offfold_{f}"] = float(np.mean([midpoint(m, [(x + s, y0, y1) for x, y0, y1 in g[f]])
                                             for s in (-32, 32)]))
    return out


def edge_window(rec: dict, lum_percent: float, smoothed: bool = True, size: float = RMS_BOX) -> float:
    """Mean of the map in a size x size DU square centred on the Edge at a luminance level."""
    m = rec["smoothed"] if smoothed else rec["image"]
    x, y = luminance_point(geometry(rec)["Edge"][0], lum_percent)
    return box_mean(m, x, y, size, size)


def rms_profile(rec: dict, levels: np.ndarray) -> pd.DataFrame:
    """Local RMS contrast of the Edge stimulus in a 16 x 16 DU square centred on the Edge.

    Readings of the claims file: (a) standard deviation of luminance over its mean; (b) standard
    deviation of luminance normalised to 0-1.
    """
    lum = edge_luminance(rec)
    fold = geometry(rec)["Edge"][0]
    xs = np.arange(lum.shape[1]) + 1.0
    ys = np.arange(lum.shape[0]) + 1.0
    rows = []
    for l in levels:
        x, y = luminance_point(fold, l)
        c = (xs >= x - RMS_BOX / 2) & (xs < x + RMS_BOX / 2)
        r = (ys >= y - RMS_BOX / 2) & (ys < y + RMS_BOX / 2)
        w = lum[np.ix_(r, c)]
        rows.append(dict(luminance=l, rms_a=w.std() / w.mean() if w.mean() > 0 else np.nan,
                         rms_b=(w / 100.0).std()))
    return pd.DataFrame(rows)


# ---------------------------------------------------------------- Star in the screen frame
# Used only for the data check: the screen-frame maps are in gaze coordinates, so measures taken
# at the stimulus's screen-frame polygons do not match those of the Standard frame.

def _rotated_box_mean(m, origin, e_w, wc, ww, wu=BLOCK_WIDTH):
    """Mean over screen pixels within a box on the line from `origin` along unit vector e_w.

    The box spans [wc - ww/2, wc + ww/2) along e_w and [-wu/2, wu/2) across it.
    """
    e_u = np.array([-e_w[1], e_w[0]])
    centre = origin + e_w * wc
    r = int(np.ceil(max(ww, wu))) + 2
    x0, y0 = int(centre[0]) - r, int(centre[1]) - r
    xs = np.arange(max(x0, 1), min(x0 + 2 * r, m.shape[1]) + 1, dtype=float)
    ys = np.arange(max(y0, 1), min(y0 + 2 * r, m.shape[0]) + 1, dtype=float)
    if xs.size == 0 or ys.size == 0:
        return np.nan
    X, Y = np.meshgrid(xs, ys)
    d = np.stack([X - centre[0], Y - centre[1]], -1)
    w = d @ e_w
    u = d @ e_u
    sel = (w >= -ww / 2) & (w < ww / 2) & (u >= -wu / 2) & (u < wu / 2)
    if not sel.any():
        return np.nan
    return float(m[(Y[sel] - 1).astype(int), (X[sel] - 1).astype(int)].mean())


def star_screen_measures(rec: dict, diagonal_angle: float | None = None) -> dict:
    """Star midpoint, blocks and baseline from the screen-frame map and stimulus polygons.

    For a file without a Standard frame the aligned diagonal is not known; with
    `diagonal_angle=None` the measures are averaged over the six diagonals of the star.
    `diagonal_angle` (degrees, screen frame, direction from the centre to one outer vertex)
    selects one diagonal. The baseline uses four squares inside the corners of the 300 DU square
    around the circumscribed circle, with the screen axes (the star's outer vertices are at 15 + 30k
    degrees, so this differs from the aligned square by a rotation of 15 degrees; all four stay in
    0% luminance).
    """
    m = rec["screen_smoothed"]
    p0 = rec["screen_polys"][0]
    c = p0.mean(axis=0)
    d = p0 - c
    rad = np.hypot(d[:, 0], d[:, 1])
    outer = p0[rad > rad.mean()]
    angles = np.degrees(np.arctan2(outer[:, 1] - c[1], outer[:, 0] - c[0]))
    if diagonal_angle is not None:
        diff = np.abs((angles - diagonal_angle + 180) % 180 - 180) % 180
        ends = outer[np.isclose(diff % 180, 0, atol=1) | np.isclose(diff % 180, 180, atol=1)]
        diagonals = [ends]
    else:
        diagonals = []
        used = set()
        for i, a in enumerate(angles):
            if i in used:
                continue
            j = int(np.argmin(np.abs(((angles - a) % 360) - 180)))
            used |= {i, j}
            diagonals.append(outer[[i, j]])
    mids, blks = [], []
    for ends in diagonals:
        per_end_mid, per_end_blk = [], []
        for o in ends:
            vec = c - o
            length = np.hypot(*vec)
            e_w = vec / length
            per_end_mid.append(_rotated_box_mean(m, o, e_w, length / 2, MID_BOX, MID_BOX))
            step = length / 10
            per_end_blk.append([_rotated_box_mean(m, o, e_w, step * (k + 0.5), step)
                                for k in range(10)])
        mids.append(np.mean(per_end_mid))
        blks.append(per_end_blk)
    half = rad.max() - BASE_BOX / 2
    base = []
    for sx in (-1, 1):
        for sy in (-1, 1):
            base.append(_rotated_box_mean(m, c + np.array([sx * half, sy * half - BASE_BOX / 2]),
                                          np.array([0.0, 1.0]), BASE_BOX / 2, BASE_BOX, BASE_BOX))
    return dict(midpoint_S52=float(np.mean(mids)), blocks_S52=np.mean(np.array(blks), axis=0),
                base_main=float(np.nanmean(base)), n_diagonals=len(diagonals))


def star_aligned_angle(rec: dict) -> float:
    """Screen-frame direction (degrees) of the aligned diagonal of a Star file with a Standard frame.

    Fits the rotation and shift that maps the Standard-frame polygon onto the screen polygon,
    allowing a cyclic shift of the vertex order, and returns the direction from the centre to the
    vertex that the Standard frame places at the top of its vertical fold.
    """
    a = rec["screen_polys"][0]
    b = rec["polys"][0]
    za, zb = a[:, 0] + 1j * a[:, 1], b[:, 0] + 1j * b[:, 1]
    best = None
    for s in range(len(zb)):
        bb = np.roll(zb, s)
        mat = np.c_[bb, np.ones_like(bb)]
        coef = np.linalg.lstsq(mat, za, rcond=None)[0]
        err = np.abs(mat @ coef - za).max()
        if best is None or err < best[0]:
            best = (err, coef)
    err, coef = best
    top = b[np.argmin(b[:, 1])]
    centre_b = b.mean(axis=0)
    q = coef[0] * (top[0] + 1j * top[1]) + coef[1]
    qc = coef[0] * (centre_b[0] + 1j * centre_b[1]) + coef[1]
    return float(np.degrees(np.angle(q - qc)))
