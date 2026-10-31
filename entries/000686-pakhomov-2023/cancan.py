"""Loading and profile measures for the monolayer images of dandiset 000686.

Pakhomov, Gudvangen, Mangalanathan, Kondratiev, Redondo & Semenov (2023), Bioelectrochemistry
152, 108437, doi:10.1016/j.bioelechem.2023.108437.

Each NWB file holds one dish: a single stitched YO-PRO-1 fluorescence image (uint16, 22323 x
22323 pixels, 12 x 12 tiles of a 10x objective) of the quadrupole array region after treatment,
in `acquisition/ScanningImaging`. Files are streamed from the archive at the pinned version: the
HDF5 chunk index is read through `remfile`, the compressed chunks are fetched with parallel HTTP
range requests and decompressed in memory, and the image is reduced to block means of `BLOCK`
x `BLOCK` pixels as it loads. Nothing is written to disk.
"""
from __future__ import annotations

import re
import zlib
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
import requests
from dandi.dandiapi import DandiAPIClient

DANDISET_ID = "000686"
DANDISET_VERSION = "0.240515.1909"
DATA_PATH = "acquisition/ScanningImaging/data"
BLOCK = 8   # standard choice: block means of 8 x 8 pixels; ROIs are many blocks wide


def assets() -> list[dict]:
    """Every NWB file at the pinned version, with its group parsed from the file name."""
    out = []
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        for a in ds.get_assets():
            if not a.path.endswith(".nwb"):
                continue
            sub = a.path.split("/")[0]
            rotated = sub.startswith("sub-1p-x4-10cycles")
            treatment = "packet" if re.search(r"-CC-", sub) else "train"
            dish = re.search(r"\((dish[^)]*)\)", sub).group(1)
            out.append(dict(path=a.path, url=a.get_content_url(follow_redirects=1, strip_query=True),
                            rotated=rotated, treatment=treatment, dish=dish,
                            group=("1P x 40" if treatment == "packet" else "1T x 40") if rotated
                            else ("40 Packets" if treatment == "packet" else "40 Trains")))
    return sorted(out, key=lambda r: (r["rotated"], r["treatment"], r["dish"]))


def _ranges(infos, max_bytes=8 << 20):
    infos = sorted(infos, key=lambda s: s.byte_offset)
    groups, cur = [], []
    for s in infos:
        if cur and (s.byte_offset + s.size - cur[0].byte_offset > max_bytes
                    or s.byte_offset != cur[-1].byte_offset + cur[-1].size):
            groups.append(cur)
            cur = []
        cur.append(s)
    groups.append(cur)
    return groups


def load_image(url: str, block: int = BLOCK, threads: int = 16) -> tuple[np.ndarray, dict]:
    """Stream one stitched image and return its block means (float32) and file metadata.

    Pixels equal to 0 lie outside the stitched tiles (no data); a block's mean is taken over its
    non-zero pixels, and blocks with none are NaN.
    """
    with h5py.File(remfile.File(url), "r") as f:
        d = f[DATA_PATH]
        meta = dict(shape=d.shape, dtype=str(d.dtype), chunks=d.chunks,
                    filters=[d.id.get_create_plist().get_filter(i)[3].decode()
                             for i in range(d.id.get_create_plist().get_nfilters())],
                    unit=d.attrs.get("unit"), resolution=float(d.attrs.get("resolution")),
                    conversion=float(d.attrs.get("conversion")),
                    subject_id=f["general/subject/subject_id"][()].decode(),
                    species=f["general/subject/species"][()].decode(),
                    session_start=f["session_start_time"][()].decode(),
                    session_description=f["session_description"][()].decode(),
                    image_description=str(f["acquisition/ScanningImaging"].attrs.get("description")))
        assert meta["filters"] == ["deflate"], meta["filters"]
        n = d.id.get_num_chunks()
        infos = [d.id.get_chunk_info(i) for i in range(n)]
        H, W = d.shape[1:]
        ch = d.chunks[1:]
    full = np.zeros((H, W), np.uint16)
    session = requests.Session()

    def fetch(group):
        a, b = group[0].byte_offset, group[-1].byte_offset + group[-1].size
        buf = session.get(url, headers={"Range": f"bytes={a}-{b - 1}"}, timeout=120).content
        assert len(buf) == b - a
        for s in group:
            arr = np.frombuffer(zlib.decompress(buf[s.byte_offset - a:s.byte_offset - a + s.size]),
                                dtype="<u2").reshape(ch)
            r0, c0 = s.chunk_offset[1:]
            h, w = min(ch[0], H - r0), min(ch[1], W - c0)
            full[r0:r0 + h, c0:c0 + w] = arr[:h, :w]

    with ThreadPoolExecutor(threads) as ex:
        list(ex.map(fetch, _ranges(infos)))
    meta["n_chunks"] = n
    meta["frac_zero"] = float((full == 0).mean())
    meta["frac_ge_65000"] = float((full >= 65000).mean())   # the maximum seen is ~65450
    meta["max"] = int(full.max())
    hb, wb = H // block, W // block
    x = full[:hb * block, :wb * block].reshape(hb, block, wb, block)
    nz = (x > 0).sum((1, 3))
    s = x.sum((1, 3), dtype=np.float64)
    del full, x
    img = np.where(nz > 0, s / np.maximum(nz, 1), np.nan).astype(np.float32)
    return img, meta


# ---------------------------------------------------------------------------------------------
# Electrode footprints
# ---------------------------------------------------------------------------------------------

def _disk(r: int) -> np.ndarray:
    y, x = np.mgrid[-r:r + 1, -r:r + 1]
    return (x * x + y * y <= r * r).astype(float)


def find_electrodes(img: np.ndarray, coarse: int = 4, r: int = 20, n_candidates: int = 8,
                    square_tol: float = 0.2) -> dict:
    """Locate the four electrode footprints, the dark circles the file description names.

    On a further 4x reduced, log-scaled image, a dark-disk score (mean of an annulus of twice the
    radius minus mean of the disk; radius 20 coarse pixels, the footprint size seen in the images)
    is computed, candidates near no-data pixels are dropped, and of the best `n_candidates` local
    maxima the four that form a square (sides and diagonals within `square_tol` of each other)
    with the highest summed score are kept. These are image-processing choices made here: the
    paper locates the electrodes by eye. Returns centres (row, col) in `img` pixels, in
    clockwise order in the image starting from the top-left one, and the footprint radius.
    """
    from itertools import combinations
    from scipy import ndimage as ndi
    from scipy.signal import fftconvolve
    nod = ~np.isfinite(img) | (np.nan_to_num(img) == 0)
    h, w = (img.shape[0] // coarse) * coarse, (img.shape[1] // coarse) * coarse
    s = np.nan_to_num(img)[:h, :w].reshape(h // coarse, coarse, w // coarse, coarse).mean((1, 3))
    n = nod[:h, :w].reshape(h // coarse, coarse, w // coarse, coarse).mean((1, 3))
    s = np.log1p(s)
    R = 2 * r
    d = _disk(r)
    a = _disk(R) - np.pad(d, R - r)
    score = fftconvolve(s, a / a.sum(), "same") - fftconvolve(s, d / d.sum(), "same")
    bad = fftconvolve(n, _disk(R), "same") > 0.5
    score[bad] = -np.inf
    peaks = (ndi.maximum_filter(score, size=4 * r + 1) == score) & ~bad
    idx = np.argwhere(peaks)
    vals = score[peaks]
    order = np.argsort(vals)[::-1][:n_candidates]
    idx, vals = idx[order].astype(float), vals[order]
    best = None
    for combo in combinations(range(len(idx)), 4):
        p = idx[list(combo)]
        c = p.mean(0)
        ang = np.arctan2(p[:, 0] - c[0], p[:, 1] - c[1])
        p = p[np.argsort(ang)]
        sides = np.linalg.norm(p - np.roll(p, -1, 0), axis=1)
        diags = np.array([np.linalg.norm(p[0] - p[2]), np.linalg.norm(p[1] - p[3])])
        err = max(np.ptp(sides) / sides.mean(), np.ptp(diags) / diags.mean(),
                  abs(diags.mean() / sides.mean() - np.sqrt(2)) / np.sqrt(2))
        if err < square_tol and (best is None or vals[list(combo)].sum() > best[0]):
            best = (vals[list(combo)].sum(), combo, err)
    assert best is not None, "no square of footprints found"
    p = idx[list(best[1])] * coarse + (coarse - 1) / 2
    c = p.mean(0)
    # clockwise in image coordinates (row down, col right), starting from the top-left one
    ang = np.arctan2(p[:, 0] - c[0], p[:, 1] - c[1])
    p = p[np.argsort(ang)]
    start = int(np.argmin(p[:, 0] + p[:, 1]))
    p = np.roll(p, -start, 0)
    p = np.array([refine_centre(img, q) for q in p])
    radius = footprint_radius(img, p)
    return dict(centres=p, centre=p.mean(0), score=float(best[0]), square_error=float(best[2]),
                diagonal=float(np.mean([np.linalg.norm(p[0] - p[2]), np.linalg.norm(p[1] - p[3])])),
                radius=radius)


def refine_centre(img: np.ndarray, guess, r: int = 85, search: int = 60) -> np.ndarray:
    """Refine a footprint centre on the full block image: the position within `search` pixels of
    the coarse guess where a disk of radius `r` (just inside the ~98-pixel footprint) has the lowest
    mean intensity. The coarse annulus score is biased toward the dim side when the uptake around an
    electrode is uneven; the disk mean alone is not. An image-processing choice made here."""
    from scipy.signal import fftconvolve
    r0, c0 = int(round(guess[0])), int(round(guess[1]))
    h = search + r
    patch = img[r0 - h:r0 + h + 1, c0 - h:c0 + h + 1]
    patch = np.where(np.isfinite(patch), patch, np.nanmax(patch))
    d = _disk(r)
    m = fftconvolve(patch, d / d.sum(), "valid")
    i, j = np.unravel_index(np.argmin(m), m.shape)
    return np.array([r0 - search + i, c0 - search + j], float)


def footprint_radius(img: np.ndarray, centres: np.ndarray, rmax: int = 200) -> float:
    """Median over electrodes of the radius where the radial mean crosses half-way between the
    footprint interior (inner 30% of the coarse radius) and the ring outside it."""
    out = []
    for (r0, c0) in centres:
        r0, c0 = int(round(r0)), int(round(c0))
        patch = img[max(r0 - rmax, 0):r0 + rmax + 1, max(c0 - rmax, 0):c0 + rmax + 1]
        yy, xx = np.mgrid[:patch.shape[0], :patch.shape[1]]
        rr = np.hypot(yy - (r0 - max(r0 - rmax, 0)), xx - (c0 - max(c0 - rmax, 0))).astype(int)
        ok = np.isfinite(patch)
        prof = np.bincount(rr[ok], patch[ok], minlength=rmax + 1)[:rmax + 1] / np.maximum(
            np.bincount(rr[ok], minlength=rmax + 1)[:rmax + 1], 1)
        inner = np.median(prof[:25])
        outer = np.median(prof[110:rmax])
        half = (inner + outer) / 2
        above = np.nonzero(prof[25:] > half)[0]
        out.append(25 + above[0] if len(above) else np.nan)
    return float(np.nanmedian(out))


def footprint_background(img: np.ndarray, el: dict, frac: float = 0.7) -> float:
    """Background for reading O4(b): median intensity inside the electrode footprints (within
    `frac` of the footprint radius), averaged over the four electrodes. Under the hollow needle the
    monolayer is covered and not exposed to the field; this is the "unexposed background" the
    claims file allows (an assumption of this attempt; the paper names no background)."""
    vals = []
    for (r0, c0) in el["centres"]:
        R = int(el["radius"] * frac)
        r0, c0 = int(round(r0)), int(round(c0))
        patch = img[r0 - R:r0 + R + 1, c0 - R:c0 + R + 1]
        m = _disk(R).astype(bool) & np.isfinite(patch)
        vals.append(np.median(patch[m]))
    return float(np.mean(vals))


# ---------------------------------------------------------------------------------------------
# ROI profiles along the diagonals
# ---------------------------------------------------------------------------------------------

UM_PER_PIXEL = 0.65          # assumption: 6.5 um camera pixels (ORCA-Flash4) under the 10x
                             # objective; the files give no pixel size (resolution -1). Used only
                             # to state distances in mm; every measure is in units of the array.
PAPER_RANGE_MM = 3.65        # Methods 2.4: ROIs cover +/- 3.65 mm from the centre (large array)
PAPER_HALF_DIAGONAL_MM = 4.2  # Results 3.5: the large array has an 8.4-mm diagonal
N_HALF = 56                  # Methods 2.4: 224 ROIs along both diagonals, 112 per diagonal,
                             # 56 per half; here one more ROI is centred on the array centre


def roi_positions(el: dict, electrode: int) -> tuple[np.ndarray, float]:
    """Centres (row, col) of the ROIs from the array centre (k = 0) toward one electrode (k = 56).

    The ROIs end at the fraction 3.65/4.2 of the distance from the centre to the inner edge of the
    footprint, which is the paper's +/- 3.65 mm when the 8.4-mm diagonal of Results 3.5 is the
    distance between inner edges (the files give 9.4 mm between centres and 8.4 mm between
    inner edges at 0.65 um per pixel). This keeps out more than the 5% of the diagonal next to
    each electrode that Methods 2.4 excludes. Returns the centres and the ROI step in pixels.
    """
    c = el["centre"]
    e = el["centres"][electrode]
    v = e - c
    dist = np.linalg.norm(v)
    end = PAPER_RANGE_MM / PAPER_HALF_DIAGONAL_MM * (dist - el["radius"])
    step = end / N_HALF
    k = np.arange(N_HALF + 1)
    return c + np.outer(k * step, v / dist), step


def roi_means(img: np.ndarray, pts: np.ndarray, side: float) -> np.ndarray:
    """Mean intensity in axis-aligned square ROIs of the given side (pixels) at each point.
    The ROI shape and size are not given by the paper; contiguous squares one step wide are a
    standard choice (wider bands are shown as a variant in the notebook)."""
    h = max(int(round(side / 2)), 1)
    out = []
    for r, c in pts:
        r, c = int(round(r)), int(round(c))
        out.append(np.nanmean(img[r - h:r + h + 1, c - h:c + h + 1]))
    return np.array(out)


def diagonal_profiles(img: np.ndarray, el: dict, width: float = 1.0) -> dict:
    """Intensity profiles along both diagonals: for each electrode (0 to 3, clockwise from the
    image's top left) the 57 ROI means from the centre (index 0) outward, ROI side `width` steps.
    Also the distance of each ROI from the centre in fractions of the measured range (0 to 1)
    and in mm at `UM_PER_PIXEL`."""
    halves, mm = [], []
    for i in range(4):
        pts, step = roi_positions(el, i)
        halves.append(roi_means(img, pts, step * width))
        mm.append(np.arange(N_HALF + 1) * step * BLOCK * UM_PER_PIXEL / 1000)
    return dict(halves=np.array(halves), frac=np.arange(N_HALF + 1) / N_HALF, mm=np.array(mm))


# ---------------------------------------------------------------------------------------------
# Readings of the claims file (O1 to O6) and the paper's test
# ---------------------------------------------------------------------------------------------

LOESS_SPANS = (0.1, 0.2, 0.3)   # claims file, O5: the span is varied over 0.1, 0.2 and 0.3


def signed_profile(halves: np.ndarray, pos: int, neg: int) -> np.ndarray:
    """Profile along one diagonal from electrode `neg` (index 0) through the centre (index 56) to
    electrode `pos` (index 112); positive distances point to `pos`."""
    return np.concatenate([halves[neg][::-1], halves[pos][1:]])


def loess(y: np.ndarray, span: float) -> np.ndarray:
    """LOESS fit of a profile against its ROI index (statsmodels lowess, no robustness
    iterations), at every ROI. Methods 2.4 fits profiles with LOESS but gives no span (O5)."""
    from statsmodels.nonparametric.smoothers_lowess import lowess
    x = np.arange(len(y), dtype=float)
    return lowess(y, x, frac=span, it=0, return_sorted=False)


def centre_value(profile: np.ndarray, reading: str) -> float:
    """O1: (a) 'roi', the ROI at distance 0; (b) 'loess<span>', the LOESS fit at distance 0."""
    mid = len(profile) // 2
    if reading == "roi":
        return float(profile[mid])
    return float(loess(profile, float(reading[5:]))[mid])


def smooth(profile: np.ndarray, reading: str) -> np.ndarray:
    """The profile as read under O1: the ROI values themselves or their LOESS fit."""
    return profile if reading == "roi" else loess(profile, float(reading[5:]))


def ttest(a, b, paired: bool = False) -> tuple[float, float]:
    """Two-sided Student's t-test (Methods 2.4), equal-variance form when unpaired."""
    from scipy import stats
    r = stats.ttest_rel(a, b) if paired else stats.ttest_ind(a, b, equal_var=True)
    return float(r.statistic), float(r.pvalue)


def errorbar_gap(a, b) -> tuple[float, bool]:
    """The paper's graphical rule (Methods 2.4, citing Cumming et al. 2007): a gap between the
    s.e. bars of two means longer than the bars marks p < 0.05. Returns the gap in units of the
    longer s.e. bar, and whether it exceeds 1."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    sa, sb = a.std(ddof=1) / np.sqrt(len(a)), b.std(ddof=1) / np.sqrt(len(b))
    gap = abs(a.mean() - b.mean()) - sa - sb
    g = gap / max(sa, sb)
    return float(g), bool(g > 1)
