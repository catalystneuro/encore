"""Loading and measures for dandiset 001277 (Silkuniene et al. 2025, Bioelectrochemistry 166:109016).

The dandiset holds stitched whole-well images of CT26 monolayers: Hoechst before exposure (DAPI),
YO-PRO-1 30 min after exposure (FITC), and for plates P1 and P2 propidium with Hoechst 2 h after
exposure (Cy3-DAPI). Images are streamed from the archive and reduced, as they load, to means of
25 x 25 pixel blocks (40.6 um at 1.625 um per pixel, from the OME metadata in each file). The
block size is a standard choice: the paper's 325 x 406 um ROI (Methods 2.5) is exactly 8 x 10
blocks, so ROI means are exact pixel means; only ROI positions are rounded to 40.6 um.

Where each parameter comes from:
- ROI size 325 x 406 um, ROIs on the diagonals joining the electrode footprints, the two diagonals
  pooled as one experiment, background as the mean of 3 ROIs inside an electrode footprint, the
  Lorentzian YP(x) = a (b/2)^2 / (x^2 + (b/2)^2) and the Gaussian Pr(x) = a exp(-x^2 / 2 s^2) with
  FWHM = 2.4 s: Methods 2.5, as the claims file's header gives them.
- Electrode geometry (2.8 mm outer diameter, 15.3 mm diagonal between the footprints' facing
  edges): Methods 2.2. Positions 6 and 7 mm from the centre are "1.65 and 0.65 mm from electrodes"
  (Results 3.1), so a footprint's inner edge is 7.65 mm from the centre and its centre 9.05 mm.
- ROI spacing (1-mm steps, or contiguous ROIs one ROI length apart), the fit half-range (4, 5 or
  6 mm) and the pooling of the diagonals (averaged at each signed distance, or all points
  fitted): readings named by the claims file's criteria, all run.
- Which side of the ROI lies along the diagonal: the 406-um side, a standard choice the claims file
  names as unlikely to change an outcome. ROIs are axis-aligned rectangles centred on the
  diagonal, as a MetaMorph rectangle region is.
- Which footprint holds the background ROIs: the claims file leaves it open as a standard choice.
  The 3 background ROIs are placed in the footprint of each electrode, inside the hollow (within
  0.6 mm of the footprint centre, the bore of a 2.8-mm needle being about 1.8 mm wide, an
  assumption), and the footprint with the lowest mean is used (no field inside a hollow
  electrode, Methods 2.5; an assumption, the variant with the mean of all four is shown).
- Locating the footprints: the paper places ROIs by eye in MetaMorph. Here the four footprints
  are found as the corners of the square of Methods 2.2 that best matches dark discs with a rim
  in the image, after dividing out the tile shading of the stitched mosaic (find_electrodes; a
  standard image-analysis choice, checked against the paper's geometry in the notebook).
"""

from __future__ import annotations

import json
import urllib.request
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import remfile
from scipy import ndimage, optimize, stats

DANDISET = "001277"
VERSION = "0.250701.1610"
API = "https://api.dandiarchive.org/api"

PIXEL_UM = 1.625          # OME PhysicalSizeX/Y in every file
BLOCK = 25                # pixels per block side (standard choice, see module docstring)
BLOCK_MM = BLOCK * PIXEL_UM / 1000
ROI_ALONG_BLOCKS = 10     # 406 um along the diagonal
ROI_ACROSS_BLOCKS = 8     # 325 um across
ELECTRODE_DIAMETER_MM = 2.8
FOOTPRINT_CENTRE_MM = 7.65 + 1.4   # from the array centre along a diagonal (Methods 2.2, Results 3.1)
DIAGONAL_GAP_MM = 15.3


def list_assets() -> list[dict]:
    """Every asset of the pinned version, with its path, size and id."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    out = []
    while url:
        with urllib.request.urlopen(url) as r:
            page = json.load(r)
        out += page["results"]
        url = page["next"]
    return out


def asset_url(asset_id: str) -> str:
    return f"{API}/assets/{asset_id}/download/"


def open_nwb(asset_id: str) -> h5py.File:
    return h5py.File(remfile.File(asset_url(asset_id)), "r")


def describe(asset_id: str) -> dict:
    """Metadata of one file: subject, series name, shape, condition fields and pixel size."""
    h = open_nwb(asset_id)
    (name,) = list(h["acquisition"].keys())
    series = h["acquisition"][name]
    desc = h["general/subject/description"][()].decode()
    own = desc.split("***General")[0]
    ome = series.attrs["description"]

    def ome_field(key, end='"'):
        return ome.split(key)[1].split(end)[0] if key in ome else None

    px = ome_field('PhysicalSizeX="')
    return {
        "subject": h["general/subject/subject_id"][()].decode(),
        "series": name,
        "shape": tuple(series["data"].shape),
        "dtype": str(series["data"].dtype),
        "chunks": series["data"].chunks,
        "own_description": own,
        "general_description": desc.split("***General")[1] if "***General" in desc else "",
        "strain": h["general/subject/strain"][()].decode(),
        "pixel_um": float(px) if px else None,
        "significant_bits": ome_field('SignificantBits="'),
        "acquisition_date": ome_field("<OME:AcquisitionDate>", "<"),
        "session_start_time": h["session_start_time"][()].decode(),
        "identifier": h["identifier"][()].decode(),
    }


def parse_condition(own_description: str) -> dict:
    """Pulse duration (ns, or None for sham), packets, packet rate and repeats from the text."""
    d = own_description
    sham = "SHAM" in d
    dur = None if sham else int(d.split("Pulse duration - ")[1].split(" ns")[0])
    packets = int(d.split("consisted of ")[1].split(" packets")[0])
    rate = d.split("delivered at ")[1].split(" frequency")[0]
    repeats = int(d.split("repeated ")[1].split(" time")[0])
    return {"pulse_ns": dur, "sham": sham, "packets": packets, "rate": rate, "repeats": repeats}


def block_means(asset_id: str, channel: int | None = None, band_rows: int = 1500) -> np.ndarray:
    """Stream one image and return the means of 25 x 25 pixel blocks (float32), the fraction
    of pixels at the uint16 maximum (65535, saturated) and the largest pixel value.

    The 19190-pixel sides are cropped to 19175 (767 blocks); the 15 dropped pixel rows and
    columns lie at the well's edge, outside the electrode array.
    """
    h = open_nwb(asset_id)
    (name,) = list(h["acquisition"].keys())
    d = h["acquisition"][name]["data"]
    n = (d.shape[-1] // BLOCK) * BLOCK
    out = np.empty((n // BLOCK, n // BLOCK), dtype=np.float32)
    sat = 0
    top = 0
    for r0 in range(0, n, band_rows):
        r1 = min(r0 + band_rows, n)
        if channel is None:
            x = d[0, r0:r1, :n]
        else:
            x = d[0, channel, r0:r1, :n]
        sat += int((x == 65535).sum())
        top = max(top, int(x.max()))
        x = x.astype(np.float32).reshape((r1 - r0) // BLOCK, BLOCK, n // BLOCK, BLOCK)
        out[r0 // BLOCK:r1 // BLOCK] = x.mean(axis=(1, 3))
    return out, sat / float(n * n), top


def _load(args):
    asset_id, channel = args
    return block_means(asset_id, channel)


def load_many(jobs: list[tuple[str, int | None]], workers: int = 4) -> list:
    """block_means for many (asset_id, channel) pairs, in parallel processes."""
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(_load, jobs))


# ---------------------------------------------------------------- geometry

def tile_period(img: np.ndarray) -> tuple[float, float]:
    """Period (blocks) of the stitched mosaic's tile shading along rows and columns.

    The row and column medians of the log image, with their slow trend removed, are folded at
    trial periods of 70 to 85 blocks; the period whose folded mean varies most is kept. Tiles are
    2048-pixel camera frames (83 blocks) with some overlap.
    """
    ok = img > 0
    L = np.where(ok, np.log(np.maximum(img, 1)), np.nan)
    out = []
    trials = np.arange(70, 85, 0.05)
    for ax in (0, 1):
        p = np.nanmedian(L, axis=1 - ax)
        idx = np.arange(len(p))
        good = ~np.isnan(p)
        p = p - ndimage.median_filter(np.where(good, p, np.nanmedian(p)), 151)
        idx, p = idx[good], p[good]
        score = []
        for P in trials:
            b = ((idx % P) / P * 40).astype(int)
            s = np.bincount(b, p, 40) / np.maximum(np.bincount(b, None, 40), 1)
            score.append(s.var())
        out.append(float(trials[int(np.argmax(score))]))
    return out[0], out[1]


def flatten(img: np.ndarray) -> np.ndarray:
    """Divide out the shading common to all tiles of the mosaic, for locating the footprints
    only (the measurements use the unflattened image, as the paper's MetaMorph analysis does).

    The shading is the median, over all tiles, of the log image minus its mean over one tile
    width, at each position within a tile (positions taken modulo the tile_period).
    """
    ok = img > 0
    P = tile_period(img)
    L = np.log(np.where(ok, np.maximum(img, 1), np.median(img[ok])))
    r = L - ndimage.uniform_filter(L, size=int(round(P[0])))
    n = img.shape[0]
    ii, jj = np.mgrid[0:n, 0:n]
    nb = int(np.ceil(max(P)))
    lab = np.floor(ii % P[0]).astype(int) * nb + np.floor(jj % P[1]).astype(int)
    med = np.nan_to_num(np.asarray(ndimage.median(r[ok], lab[ok], index=np.arange(nb * nb))))
    return np.where(ok, np.exp(L - med[lab]), 0)


def ring_contrast(img: np.ndarray) -> np.ndarray:
    """Mean of the annulus 1.2 to 2.0 mm from a point minus the mean of the disc within 0.8 mm.

    A footprint has no YP signal inside (Fig. 3A legend) and a rim at the needle wall; this
    contrast peaks at a footprint's centre. Unimaged corners of the stitched image (zeros) are
    filled with the image median first.
    """
    img = np.where(img > 0, img, np.median(img[img > 0]))
    img = np.minimum(img, np.percentile(img, 99))  # limit bright debris
    r_in, r0, r1 = 0.8 / BLOCK_MM, 1.2 / BLOCK_MM, 2.0 / BLOCK_MM
    k = int(np.ceil(r1))
    yy, xx = np.mgrid[-k:k + 1, -k:k + 1]
    rr = np.hypot(yy, xx)
    disc = (rr <= r_in).astype(float)
    ann = ((rr >= r0) & (rr <= r1)).astype(float)
    return (ndimage.convolve(img, ann / ann.sum(), mode="nearest")
            - ndimage.convolve(img, disc / disc.sum(), mode="nearest"))


def find_electrodes(img: np.ndarray) -> dict:
    """Centres (row, col in blocks) of the four electrode footprints in a block image.

    The four footprints lie at the corners of a square whose centre-to-centre diagonal is
    2 x 9.05 mm (Methods 2.2). The square (centre, rotation, and a scale of 0.9 to 1.1 to allow
    for the stitching) that maximizes the summed ring_contrast at its corners is found on a grid,
    and each corner is then moved to the contrast maximum within 0.6 mm. The order of the
    electrodes goes round the square, so (0, 2) and (1, 3) are the diagonals.
    """
    C = ring_contrast(flatten(img))
    n = img.shape[0]
    c0 = (n - 1) / 2
    best = (-np.inf, None)
    half = FOOTPRINT_CENTRE_MM / BLOCK_MM
    for step, span, cen, angs, scales in [
        (4, int(5 / BLOCK_MM), (c0, c0), np.radians(np.arange(0, 90, 2.0)), np.arange(0.9, 1.101, 0.02)),
    ]:
        offs = np.arange(-span, span + 1, step)
        cy = cen[0] + offs[:, None]
        cx = cen[1] + offs[None, :]
        for a in angs:
            for s in scales:
                tot = 0
                for q in range(4):
                    t = a + q * np.pi / 2
                    yy = np.clip(np.round(cy + s * half * np.sin(t)).astype(int), 0, n - 1)
                    xx = np.clip(np.round(cx + s * half * np.cos(t)).astype(int), 0, n - 1)
                    tot = tot + C[yy, xx]
                i, j = np.unravel_index(np.argmax(tot), tot.shape)
                if tot[i, j] > best[0]:
                    best = (tot[i, j], (cy[i, 0], cx[0, j], a, s))
    cy, cx, a, s = best[1]
    pts = []
    r = int(round(0.6 / BLOCK_MM))
    for q in range(4):
        t = a + q * np.pi / 2
        y, x = int(round(cy + s * half * np.sin(t))), int(round(cx + s * half * np.cos(t)))
        patch = C[y - r:y + r + 1, x - r:x + r + 1]
        di, dj = np.unravel_index(np.argmax(patch), patch.shape)
        pts.append((y - r + di, x - r + dj))
    ref = np.array(pts, dtype=float)
    centre = ref.mean(axis=0)
    d1 = (ref[2] - ref[0]) * BLOCK_MM
    d2 = (ref[3] - ref[1]) * BLOCK_MM
    return {
        "electrodes": ref,
        "centre": centre,
        "diag_lengths_mm": (float(np.hypot(*d1)), float(np.hypot(*d2))),
        "diag_angle_deg": float(np.degrees(np.arccos(abs(np.dot(d1, d2)) / np.hypot(*d1) / np.hypot(*d2)))),
        "contrast": [float(C[int(i), int(j)]) for i, j in ref],
    }


def roi_mean(img: np.ndarray, centre_rc: np.ndarray, along_rc: np.ndarray) -> float:
    """Mean of an axis-aligned 325 x 406 um ROI centred at centre_rc (blocks).

    The 406-um side is placed along whichever image axis is closer to the diagonal direction
    along_rc (a standard choice; the diagonals run near 45 degrees, so either is as close).
    """
    if abs(along_rc[0]) >= abs(along_rc[1]):
        h, w = ROI_ALONG_BLOCKS, ROI_ACROSS_BLOCKS
    else:
        h, w = ROI_ACROSS_BLOCKS, ROI_ALONG_BLOCKS
    i0 = int(round(centre_rc[0] - h / 2))
    j0 = int(round(centre_rc[1] - w / 2))
    return float(img[i0:i0 + h, j0:j0 + w].mean())


def positions(spacing: str, max_mm: float = 7.0) -> np.ndarray:
    """Signed ROI centre distances from the array centre (mm) along a diagonal.

    "1mm": 0, +-1, ..., +-7 mm (the text names 0, 6 and 7 mm). "contiguous": ROIs touching, one
    ROI length (0.406 mm) apart, out to 7 mm.
    """
    if spacing == "1mm":
        k = np.arange(-int(max_mm), int(max_mm) + 1)
        return k.astype(float)
    step = ROI_ALONG_BLOCKS * BLOCK_MM
    k = np.arange(-int(np.floor(max_mm / step)), int(np.floor(max_mm / step)) + 1)
    return k * step


def background(img: np.ndarray, geom: dict, which: str = "darkest") -> float:
    """Mean of 3 ROIs in an electrode footprint (Methods 2.5).

    The 3 ROIs are placed at the footprint centre and 0.4 mm either side of it across the
    diagonal, inside the hollow bore. which="darkest" uses the footprint with the lowest mean;
    which="all" averages the four footprints (variant).
    """
    vals = []
    c = geom["centre"]
    for e in geom["electrodes"]:
        u = (e - c) / np.hypot(*(e - c))
        perp = np.array([-u[1], u[0]])
        off = 0.4 / BLOCK_MM
        vals.append(np.mean([roi_mean(img, e + s * off * perp, u) for s in (-1, 0, 1)]))
    vals = np.array(vals)
    return float(vals.min() if which == "darkest" else vals.mean())


def diagonal_profiles(img: np.ndarray, geom: dict, spacing: str, bg: float,
                      scaled: bool = True) -> tuple[np.ndarray, np.ndarray]:
    """Background-subtracted ROI means along both diagonals.

    Returns x (mm, signed; positive toward the first electrode of each pair) and an array of
    shape (2, len(x)), one row per diagonal. Distances are scaled to the paper's geometry: a
    footprint centre is 9.05 mm from the array centre (Methods 2.2), so x is measured as a
    fraction of the measured centre-to-footprint distance times 9.05 mm. This takes out a small
    difference in the stitched image's scale. scaled=False uses the pixel size of the OME
    metadata instead (variant, shown in the notebook).
    """
    x = positions(spacing)
    c = geom["centre"]
    out = []
    for a, b in ((0, 2), (1, 3)):
        ea, eb = geom["electrodes"][a], geom["electrodes"][b]
        half = (ea - eb) / 2
        mid = (ea + eb) / 2  # the diagonal's own midpoint, which differs little from c
        u = half / np.hypot(*half)
        scale = np.hypot(*half) / FOOTPRINT_CENTRE_MM if scaled else 1 / BLOCK_MM  # blocks per mm
        prof = [roi_mean(img, mid + xi * scale * u, u) - bg for xi in x]
        out.append(prof)
    return x, np.array(out)


# ---------------------------------------------------------------- fits

def lorentz(x, a, b):
    return a * (b / 2) ** 2 / (x ** 2 + (b / 2) ** 2)


def gauss(x, a, s):
    return a * np.exp(-x ** 2 / (2 * s ** 2))


def fit_curve(x, y, kind: str, half_range: float) -> dict:
    """Least-squares fit of the Lorentzian (FWHM b) or Gaussian (FWHM 2.4 sigma, Methods 2.5)
    over |x| <= half_range, centred at 0, no offset. Returns parameters, FWHM, R, R2 and the
    p-value of the correlation of fit with data."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    m = np.abs(x) <= half_range + 1e-9
    xs, ys = x[m], y[m]
    a0 = max(ys.max(), 1e-6)
    try:
        if kind == "lorentz":
            p, _ = optimize.curve_fit(lorentz, xs, ys, p0=(a0, 2.0), maxfev=20000)
            p[1] = abs(p[1])
            fwhm = p[1]
            pred = lorentz(xs, *p)
        else:
            p, _ = optimize.curve_fit(gauss, xs, ys, p0=(a0, 1.0), maxfev=20000)
            p[1] = abs(p[1])
            fwhm = 2.4 * p[1]
            pred = gauss(xs, *p)
    except RuntimeError:
        return {"ok": False, "a": np.nan, "fwhm": np.nan, "r": np.nan, "r2": np.nan, "p": np.nan, "n": int(m.sum())}
    ss_res = ((ys - pred) ** 2).sum()
    ss_tot = ((ys - ys.mean()) ** 2).sum()
    r, pr = stats.pearsonr(pred, ys)
    return {"ok": True, "a": float(p[0]), "fwhm": float(fwhm), "r": float(r), "r2": float(1 - ss_res / ss_tot),
            "p": float(pr), "n": int(m.sum())}


def fit_experiment(x, prof2, half_range: float, pooling: str, kind: str = "lorentz") -> dict:
    """Fit one experiment's two diagonals: pooling="avg" averages them at each signed distance,
    pooling="all" fits all points of both together."""
    if pooling == "avg":
        return fit_curve(x, prof2.mean(axis=0), kind, half_range)
    return fit_curve(np.concatenate([x, x]), prof2.ravel(), kind, half_range)


def slope_test(x, y) -> dict:
    """Linear regression of y on x with the two-sided t-test of the slope."""
    res = stats.linregress(x, y)
    return {"slope": float(res.slope), "p": float(res.pvalue), "r": float(res.rvalue), "n": len(x)}


def gap_rule(m1, s1, m2, s2) -> bool:
    """Methods 2.5 (after Cumming et al. 2007): a gap between the s.e. bars longer than the bars
    means p < 0.05. True when the gap exceeds the mean length of the two bars (Cumming's
    "average arm", a standard choice when the bars differ)."""
    lo, hi = (m1, s1), (m2, s2)
    if m1 > m2:
        lo, hi = hi, lo
    gap = (hi[0] - hi[1]) - (lo[0] + lo[1])
    return bool(gap > (s1 + s2) / 2)


# ---------------------------------------------------------------- the dataset's files and wells

def file_table(workers: int = 8):
    """One row per file of the pinned version: path, asset id, size, well, plate, plate row and
    column, channel, condition (from the subject description) and the metadata of describe()."""
    import pandas as pd
    from concurrent.futures import ThreadPoolExecutor
    assets = list_assets()
    with ThreadPoolExecutor(workers) as ex:
        descs = list(ex.map(lambda a: describe(a["asset_id"]), assets))
    rows = []
    for a, d in zip(assets, descs):
        plate, date, pos = d["subject"].split("_")
        row = {"path": a["path"], "asset_id": a["asset_id"], "size_gb": a["size"] / 1e9,
               "well": d["subject"], "plate": plate, "date": date, "plate_row": pos[0],
               "plate_col": int(pos[1]), "series": d["series"]}
        row.update(parse_condition(d["own_description"]))
        row.update({k: d[k] for k in ("shape", "dtype", "chunks", "strain", "pixel_um", "significant_bits",
                                      "acquisition_date", "session_start_time", "identifier",
                                      "own_description", "general_description")})
        rows.append(row)
    return pd.DataFrame(rows).sort_values(["well", "series", "path"]).reset_index(drop=True)


def triplet_rows(wells) -> set:
    """Plate rows that hold one well each of 300, 600 and 900 ns. Each such row is taken as one
    experiment of Fig. 6 (n=5 per duration, Fig. 6B legend); an assumption, see the notebook."""
    out = set()
    for (plate, prow), g in wells.groupby(["plate", "plate_row"]):
        if sorted(g["pulse_ns"].dropna().astype(int)) == [300, 600, 900]:
            out.add((plate, prow))
    return out


# ---------------------------------------------------------------- per-well measures

SPACINGS = ("1mm", "contiguous")
HALF_RANGES = (4.0, 5.0, 6.0)
POOLINGS = ("avg", "all")


def measure_well(img: np.ndarray) -> dict:
    """Footprints, both background choices, and the diagonal profiles under both ROI spacings."""
    g = find_electrodes(img)
    out = {"geom": g}
    for which in ("darkest", "all"):
        bg = background(img, g, which)
        out[("bg", which)] = bg
        for sp in SPACINGS:
            out[(which, sp)] = diagonal_profiles(img, g, sp, bg)
    return out


def centre_value(meas: dict, spacing: str = "1mm", bg: str = "darkest") -> float:
    """Background-subtracted YP at 0 mm, mean of the two diagonals (the same ROI region)."""
    x, prof = meas[(bg, spacing)]
    return float(prof.mean(axis=0)[np.argmin(np.abs(x))])


def fwhm(meas: dict, spacing: str, half_range: float, pooling: str, bg: str = "darkest",
         kind: str = "lorentz") -> dict:
    x, prof = meas[(bg, spacing)]
    return fit_experiment(x, prof, half_range, pooling, kind)


def mean_se(v) -> tuple[float, float]:
    v = np.asarray(v, float)
    return float(v.mean()), float(v.std(ddof=1) / np.sqrt(len(v)))


def ttest_bonf(a, b, m: int) -> dict:
    """Two-sided Student's t-test (equal variances, as 'Student's'), Bonferroni over m tests."""
    t = stats.ttest_ind(a, b)
    return {"t": float(t.statistic), "p": float(t.pvalue), "p_bonf": float(min(1.0, t.pvalue * m)),
            "diff": float(np.mean(a) - np.mean(b)),
            "cohen_d": float((np.mean(a) - np.mean(b)) / np.sqrt((np.var(a, ddof=1) + np.var(b, ddof=1)) / 2))}
