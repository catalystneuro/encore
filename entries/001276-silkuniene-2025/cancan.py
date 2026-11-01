"""Loading and profile measures for the CANCAN monolayer images of dandiset 001276.

Silkuniene, Silkunas, Pakhomova, Semenov & Pakhomov (2025), Bioelectrochemistry 166:109016,
doi:10.1016/j.bioelechem.2025.109016.

Each NWB file holds one stitched whole-well image (19190 x 19190 pixels, uint16) of one well:
YO-PRO-1 (YP, FITC cube) after exposure or Hoechst (DAPI cube) before it. The protocol, cell line,
channel and phase are only in the free-text description of the image series; `parse_description`
reads them. Files are streamed from the archive at the pinned version: the chunk index is read
with h5py over remfile, the chunks are fetched by HTTP range requests and decompressed in memory,
and each image is reduced as it loads to means over 10 x 10 pixel bins. Nothing is written to disk.

Where the parameters come from:

- `UM_PER_PX = 1.625`. The files give no pixel size. The paper images with a 4x objective on an
  ORCA-Flash4 sCMOS camera (Methods 2.4), whose sensor pixels are 6.5 um (manufacturer's
  specification), so 6.5 / 4 = 1.625 um per pixel. This is an assumption; the notebook checks it
  against the electrode geometry (`square_fit` with the side left free).
- Geometry (Methods 2.2, Results 3.1). Four needles of 2.8 mm outer diameter form a square with
  15.3 mm side-to-side diagonals, so the electrode centers are 15.3 + 2.8 = 18.1 mm apart along a
  diagonal (12.8 mm along a side); 6 and 7 mm from the center are 1.65 and 0.65 mm from an
  electrode (Results 3.1), which this geometry gives.
- The center of the array is the center of the four electrode footprints (claims file, header,
  "the geometrical center of the electrode array", Methods 2.5). Footprints are found as dark
  disks: "Footprints of 4 electrodes are identified by the lack of YP signal underneath" (Fig. 3A
  legend). `square_fit` places a square of the known size where the four corners are darkest
  relative to their surroundings, so a footprint that is faint in one image is placed by the
  other three. The disk and annulus radii of the detector (`LUMEN_R_MM`, `RING_MM`) are a
  standard choice for a lumen of about 2 mm; the notebook shows each fit for checking.
- ROIs of 325 x 406 um along the diagonals, background as the mean of 3 ROIs inside an electrode
  footprint, measurements of two diagonals pooled (Methods 2.5). The long side lies across the
  diagonal (claims file, standard choice). The paper does not say which footprint holds the
  background ROIs; here 3 ROIs (the footprint center and 0.45 mm to either side across the
  diagonal) are placed in each of the four footprints, and the background is the median of the
  four footprint means, a standard choice that keeps one footprint with bright debris, or lying
  outside the image, from setting it; the notebook shows the spread between footprints.
- ROI spacing along the diagonal, 1 mm or 0.5 mm (claims file, header, the two readings).
- Lorentzian YP(x) = a (b/2)^2 / (x^2 + (b/2)^2), b the FWHM in mm (Methods 2.5).
- Lines through the center parallel to the sides (Methods 2.5, Fig. 3C) use the same ROIs.
"""

from __future__ import annotations

import re
import zlib
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from dandi.dandiapi import DandiAPIClient
from scipy import ndimage, optimize, signal, stats

DANDISET_ID = "001276"
DANDISET_VERSION = "0.250701.1609"

IMAGE_PATH = "acquisition/SingleTimePointImaging/data"
BIN = 10                      # pixels per bin side, as the image loads
UM_PER_PX = 1.625             # 6.5 um camera pixel / 4x objective (assumption, see docstring)
UM_PER_BIN = UM_PER_PX * BIN

DIAG_CENTER_TO_ELECTRODE_MM = (15.3 + 2.8) / 2   # 9.05 mm, Methods 2.2
SIDE_MM = DIAG_CENTER_TO_ELECTRODE_MM * np.sqrt(2)  # 12.8 mm between electrode centers
ROI_ALONG_UM, ROI_ACROSS_UM = 325.0, 406.0       # Methods 2.5; long side across the line
LUMEN_R_MM = 0.8              # dark disk of the detector (inside the lumen)
RING_MM = (1.25, 1.9)         # annulus of the detector (outside the needle wall)
BG_OFFSETS_MM = (-0.45, 0.0, 0.45)


# ---------------------------------------------------------------- archive and metadata

def list_assets() -> list[dict]:
    """Every asset of the pinned version, with its path, size and S3 URL."""
    client = DandiAPIClient()
    ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
    out = []
    for a in ds.get_assets():
        out.append({"path": a.path, "size": a.size,
                    "url": a.get_content_url(follow_redirects=1, strip_query=True)})
    return out


def parse_description(text: str) -> dict:
    """Channel, phase, protocol, packet rate and number of bursts from an image description."""
    sub = text.split("General Protocol Description")[0]
    rate = re.search(r"delivered at ([\d.]+\s*\w+) frequency", sub).group(1).replace(" ", "")
    return {
        "subject_text": re.search(r"Subject ID: ([\w-]+)", sub).group(1),
        "channel": re.search(r"Fluorescent Channel: (\w+)", sub).group(1),
        "phase": re.search(r"Phase: (\w+)", sub).group(1),
        "protocol": "control" if "Control protocol" in sub else "cancan",
        "protocol_code": re.search(r"\),\s*(\d+):", sub).group(1),
        "packet_rate": rate,
        "bursts": int(re.search(r"repeated (\d+) time", sub).group(1)),
    }


def read_metadata(asset: dict) -> dict:
    """Metadata of one file, read without its image data."""
    with h5py.File(remfile.File(asset["url"]), "r") as f:
        ser = f["acquisition/SingleTimePointImaging"]
        desc = ser.attrs["description"]
        desc = desc.decode() if isinstance(desc, bytes) else desc
        row = {
            "path": asset["path"], "url": asset["url"], "size_mb": asset["size"] / 1e6,
            "subject": f["general/subject/subject_id"][()].decode(),
            "cell_line": f["general/subject/strain"][()].decode().replace("cellline: ", ""),
            "species": f["general/subject/species"][()].decode(),
            "shape": tuple(ser["data"].shape), "dtype": str(ser["data"].dtype),
            "chunks": tuple(ser["data"].chunks),
            "session_start": f["session_start_time"][()].decode(),
            "description": desc,
        }
    row.update(parse_description(desc))
    return row


def load_metadata(assets: list[dict], workers: int = 16) -> pd.DataFrame:
    with ThreadPoolExecutor(workers) as ex:
        rows = list(ex.map(read_metadata, assets))
    return pd.DataFrame(rows).sort_values(["subject", "channel", "path"]).reset_index(drop=True)


# ---------------------------------------------------------------- streaming the images

_session = requests.Session()
_session.mount("https://", requests.adapters.HTTPAdapter(pool_maxsize=64))


def load_binned(url: str, plane: int = 0, workers: int = 24) -> dict:
    """Stream one image and reduce it to means over BIN x BIN pixels.

    Pixels equal to 0 lie outside the stitched area; they are left out of the means, and a bin
    with none inside is NaN. Returns the binned image and the fraction of pixels inside.
    `plane` selects the image in the files that hold two (shape (1, 2, H, W)).
    """
    with h5py.File(remfile.File(url), "r") as f:
        d = f[IMAGE_PATH]
        shape, chunks = d.shape, d.chunks
        assert d.compression == "gzip" and not d.shuffle and d.dtype == np.uint16
        index = []
        d.id.chunk_iter(lambda ci: index.append((ci.chunk_offset, ci.byte_offset, ci.size)))
    H, W = shape[-2:]
    ch, cw = chunks[-2:]
    if len(shape) == 4:
        index = [c for c in index if c[0][1] == plane]
    assert ch % BIN == 0 and cw % BIN == 0
    hb, wb = -(-H // BIN), -(-W // BIN)
    total = np.zeros((hb, wb))
    count = np.zeros((hb, wb))
    index.sort(key=lambda c: c[1])
    groups, cur = [], []
    for c in index:
        if cur and (c[1] != cur[-1][1] + cur[-1][2] or sum(x[2] for x in cur) > 8e6):
            groups.append(cur)
            cur = []
        cur.append(c)
    groups.append(cur)

    def fetch(group):
        start, end = group[0][1], group[-1][1] + group[-1][2]
        r = _session.get(url, headers={"Range": f"bytes={start}-{end - 1}"}, timeout=120)
        r.raise_for_status()
        buf = r.content
        if len(buf) != end - start:
            raise IOError(f"short read from {url}")
        for off, bo, sz in group:
            arr = np.frombuffer(zlib.decompress(buf[bo - start:bo - start + sz]), np.uint16)
            arr = arr.reshape(ch, cw).astype(np.float64)
            y, x = off[-2], off[-1]
            hh, ww = min(ch, H - y), min(cw, W - x)
            arr = arr[:hh, :ww]
            # pad to whole bins; padded pixels count as outside
            ph, pw = -(-hh // BIN) * BIN, -(-ww // BIN) * BIN
            a = np.zeros((ph, pw))
            a[:hh, :ww] = arr
            inside = a > 0
            s = a.reshape(ph // BIN, BIN, pw // BIN, BIN).sum((1, 3))
            n = inside.reshape(ph // BIN, BIN, pw // BIN, BIN).sum((1, 3))
            yb, xb = y // BIN, x // BIN
            total[yb:yb + s.shape[0], xb:xb + s.shape[1]] = s
            count[yb:yb + s.shape[0], xb:xb + s.shape[1]] = n
        return len(buf)

    with ThreadPoolExecutor(workers) as ex:
        nbytes = sum(ex.map(fetch, groups))
    with np.errstate(invalid="ignore", divide="ignore"):
        img = np.where(count > 0, total / count, np.nan)
    return {"image": img.astype(np.float32), "inside": (count / BIN**2).astype(np.float32),
            "bytes": nbytes, "n_chunks": len(index), "full_shape": (H, W)}


# ---------------------------------------------------------------- electrode square

def _disk_kernel(r_in_bins: float, r_out_bins: float, step: int) -> np.ndarray:
    r = int(np.ceil(r_out_bins / step)) + 1
    yy, xx = np.mgrid[-r:r + 1, -r:r + 1] * step
    rr = np.hypot(yy, xx)
    k = ((rr >= r_in_bins) & (rr < r_out_bins)).astype(float)
    return k / k.sum()


def darkness_map(img: np.ndarray, step: int = 4) -> tuple[np.ndarray, int]:
    """Annulus mean minus disk mean, relative to the image median, on a grid of `step` bins.

    High where a dark disk of the lumen's size is surrounded by brighter monolayer.
    """
    small = img[::step, ::step].astype(float)
    valid = np.isfinite(small)
    # log intensity, so that contrast counts the same in bright and dim images; area outside the
    # stitched image is left out of the means (normalized convolution)
    lg = np.where(valid, np.log(np.clip(small, 1.0, None)), 0.0)
    to_bins = 1000.0 / UM_PER_BIN
    disk = _disk_kernel(0, LUMEN_R_MM * to_bins, step)
    ring = _disk_kernel(RING_MM[0] * to_bins, RING_MM[1] * to_bins, step)
    with np.errstate(invalid="ignore", divide="ignore"):
        w_disk = signal.fftconvolve(valid.astype(float), disk, mode="same")
        w_ring = signal.fftconvolve(valid.astype(float), ring, mode="same")
        m_disk = signal.fftconvolve(lg, disk, mode="same") / w_disk
        m_ring = signal.fftconvolve(lg, ring, mode="same") / w_ring
        out = m_ring - m_disk
    out[~((w_disk >= 0.5) & (w_ring >= 0.3))] = 0.0
    return np.nan_to_num(out), step


def square_corners(cx: float, cy: float, theta: float, side_bins: float) -> np.ndarray:
    """Corners (x, y) in bins of a square centered at (cx, cy), rotated by theta (radians)."""
    h = side_bins / 2
    base = np.array([[-h, -h], [h, -h], [h, h], [-h, h]])
    rot = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    return base @ rot.T + [cx, cy]


def square_fit(img: np.ndarray, free_side: bool = False) -> dict:
    """Place the electrode square where the four corners are darkest against their surround.

    The side is fixed at SIDE_MM unless free_side, when it is fitted too (a check of UM_PER_PX).
    Returns the center (bins), angle, side, the corner positions and the corner scores.
    """
    dmap, step = darkness_map(img)
    side0 = SIDE_MM * 1000.0 / UM_PER_BIN

    def score(cx, cy, th, side):
        c = square_corners(cx, cy, th, side) / step
        return ndimage.map_coordinates(dmap, [c[:, 1], c[:, 0]], order=1, mode="constant", cval=-1.0)

    # coarse search: for each angle and side, the summed score of the four corners at every
    # center of the grid, by shifting the map; centers within the middle 40% of the image
    gh, gw = dmap.shape
    pad = int(np.ceil(side0 * 1.2 / step))
    padded = np.pad(dmap, pad, constant_values=-1.0)
    best = (-np.inf, None)
    sides = [side0] if not free_side else side0 * np.linspace(0.85, 1.15, 31)
    for side in sides:
        for th in np.deg2rad(np.arange(-45, 45, 1.0)):
            offs = np.rint(square_corners(0, 0, th, side) / step).astype(int)
            total = np.zeros_like(dmap)
            for ox, oy in offs:
                total += padded[pad + oy:pad + oy + gh, pad + ox:pad + ox + gw]
            y0, y1, x0_, x1 = int(gh * 0.3), int(gh * 0.7), int(gw * 0.3), int(gw * 0.7)
            sub = total[y0:y1, x0_:x1]
            iy, ix = np.unravel_index(np.argmax(sub), sub.shape)
            if sub[iy, ix] > best[0]:
                best = (sub[iy, ix], ((ix + x0_) * step, (iy + y0) * step, th, side))
    x0 = np.array(best[1])

    def neg(p):
        side = p[3] if free_side else side0
        return -score(p[0], p[1], p[2], side).sum()

    res = optimize.minimize(neg, x0 if free_side else x0[:3], method="Nelder-Mead",
                            options={"xatol": 0.2, "fatol": 1e-5})
    cx, cy, th = res.x[:3]
    side = res.x[3] if free_side else side0
    corners = square_corners(cx, cy, th, side)
    return {"cx": cx, "cy": cy, "theta_deg": float(np.rad2deg(th)), "side_bins": side,
            "side_mm": side * UM_PER_BIN / 1000, "corners": corners,
            "corner_scores": score(cx, cy, th, side)}


# ---------------------------------------------------------------- ROIs and profiles

def roi_mean(img: np.ndarray, x: float, y: float, u: np.ndarray) -> float:
    """Mean of the binned image in a 325 x 406 um ROI centered at (x, y) bins.

    u is the unit vector along the line; the 325 um side lies along it, the 406 um side across.
    Bins whose centers fall inside the rotated rectangle are averaged.
    """
    half_a = ROI_ALONG_UM / 2 / UM_PER_BIN
    half_c = ROI_ACROSS_UM / 2 / UM_PER_BIN
    r = int(np.ceil(np.hypot(half_a, half_c))) + 1
    x0, y0 = int(round(x)), int(round(y))
    ys, xs = np.mgrid[y0 - r:y0 + r + 1, x0 - r:x0 + r + 1]
    dx, dy = xs - x, ys - y
    along = dx * u[0] + dy * u[1]
    across = -dx * u[1] + dy * u[0]
    m = (np.abs(along) <= half_a) & (np.abs(across) <= half_c)
    ok = (ys >= 0) & (ys < img.shape[0]) & (xs >= 0) & (xs < img.shape[1])
    m &= ok
    vals = img[ys[m], xs[m]]
    return float(np.nanmean(vals)) if np.isfinite(vals).any() else np.nan


def background(img: np.ndarray, sq: dict) -> dict:
    """3 ROIs inside each electrode footprint (center and +/-0.45 mm across the diagonal).

    The background is the median over the footprints of their 3-ROI means.
    """
    c = np.array([sq["cx"], sq["cy"]])
    per = []
    for corner in sq["corners"]:
        u = (corner - c) / np.linalg.norm(corner - c)
        v = np.array([-u[1], u[0]])
        vals = [roi_mean(img, *(corner + v * o * 1000 / UM_PER_BIN), u) for o in BG_OFFSETS_MM]
        per.append(np.nanmean(vals) if np.isfinite(vals).any() else np.nan)
    return {"background": float(np.nanmedian(per)), "per_footprint": per}


def profile(img: np.ndarray, sq: dict, distances_mm: np.ndarray, kind: str = "diagonal") -> pd.DataFrame:
    """Raw ROI means along the two diagonals (or the two lines parallel to the sides).

    Returns one row per line and signed distance; distance is positive toward corner 0 or 1
    (diagonals: corners 0-2 and 1-3; sides: the midpoints of sides 0-1 / 3-2 and 1-2 / 0-3).
    """
    c = np.array([sq["cx"], sq["cy"]])
    k = sq["corners"]
    if kind == "diagonal":
        targets = [k[0], k[1]]
    elif kind == "sides":
        targets = [(k[0] + k[1]) / 2, (k[1] + k[2]) / 2]
    else:
        raise ValueError(kind)
    rows = []
    for line, t in enumerate(targets):
        u = (t - c) / np.linalg.norm(t - c)
        for dmm in distances_mm:
            p = c + u * dmm * 1000 / UM_PER_BIN
            rows.append({"line": line, "x_mm": float(dmm), "raw": roi_mean(img, p[0], p[1], u)})
    return pd.DataFrame(rows)


def pooled_profile(prof: pd.DataFrame, bg: float) -> pd.Series:
    """Background-subtracted intensity per signed distance, the two lines averaged."""
    p = prof.assign(yp=prof.raw - bg)
    return p.groupby("x_mm").yp.mean()


def distances(spacing_mm: float, max_mm: float = 7.0) -> np.ndarray:
    n = int(round(max_mm / spacing_mm))
    return np.arange(-n, n + 1) * spacing_mm


# ---------------------------------------------------------------- fits and tests

def lorentz(x, a, b):
    return a * (b / 2) ** 2 / (x ** 2 + (b / 2) ** 2)


def gauss(x, a, sigma):
    return a * np.exp(-x ** 2 / (2 * sigma ** 2))


def fit_lorentz(x: np.ndarray, y: np.ndarray, fit_range: float) -> dict:
    """Least-squares Lorentzian on the points with |x| <= fit_range.

    Returns a, b (FWHM, mm), R (correlation of fitted and observed values), its p, and R2.
    """
    m = (np.abs(x) <= fit_range + 1e-9) & np.isfinite(y)
    xs, ys = x[m], y[m]
    try:
        (a, b), _ = optimize.curve_fit(lorentz, xs, ys, p0=[max(ys.max(), 1e-3), 2.0],
                                       bounds=([0, 0.05], [np.inf, 100.0]), maxfev=20000)
    except RuntimeError:
        return {"a": np.nan, "b": np.nan, "R": np.nan, "p": np.nan, "R2": np.nan, "n": int(m.sum())}
    fit = lorentz(xs, a, b)
    r, p = stats.pearsonr(fit, ys)
    r2 = 1 - np.sum((ys - fit) ** 2) / np.sum((ys - ys.mean()) ** 2)
    return {"a": a, "b": b, "R": r, "p": p, "R2": r2, "n": int(m.sum())}


def slope_test(x, y) -> dict:
    """Linear regression of y on x; the slope tested against zero (2-sided t test)."""
    x, y = np.asarray(x, float), np.asarray(y, float)
    r = stats.linregress(x, y)
    return {"slope": r.slope, "intercept": r.intercept, "se": r.stderr, "p": r.pvalue,
            "r": r.rvalue, "n": len(x)}


def fit_band(x, y, x_new, level: float = 0.95) -> pd.DataFrame:
    """Linear fit of y on x with the confidence band of the fitted line at x_new."""
    x, y = np.asarray(x, float), np.asarray(y, float)
    n = len(x)
    r = stats.linregress(x, y)
    resid = y - (r.intercept + r.slope * x)
    s = np.sqrt(np.sum(resid ** 2) / (n - 2))
    t = stats.t.ppf(0.5 + level / 2, n - 2)
    x_new = np.asarray(x_new, float)
    se = s * np.sqrt(1 / n + (x_new - x.mean()) ** 2 / np.sum((x - x.mean()) ** 2))
    pred = r.intercept + r.slope * x_new
    return pd.DataFrame({"x": x_new, "fit": pred, "lo": pred - t * se, "hi": pred + t * se})
