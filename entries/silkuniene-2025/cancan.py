"""Loading and profile measures for the CANCAN monolayer images of dandisets 001047, 001276,
001277 and 001284.

Silkuniene, Silkunas, Pakhomova, Semenov & Pakhomov (2025), Bioelectrochemistry 166, 109016,
doi:10.1016/j.bioelechem.2025.109016.

Each NWB file holds one stitched image of one well (4x objective, 1.625 um pixels in the OME
metadata the files carry), with one or two channels: Hoechst (DAPI) before exposure, YO-PRO-1
(FITC) 30 min after, and in killing experiments propidium (Cy3) with Hoechst (DAPI) 2 h after.
The exposure parameters are in each file's session description. Files are streamed from the
archive at the pinned versions and reduced as they load to blocks of `BLOCK` x `BLOCK` pixels
(26 um); nothing is written to disk.

Where the parameters come from:

- ROI size 325 x 406 um, ROIs along the diagonals of the square at distances from its
  geometrical centre, the two diagonals of a well pooled as one experiment, background as the
  mean of 3 ROIs inside an electrode footprint subtracted from every ROI: Methods 2.5 (claims
  file F1 to F3). The 406-um side along the diagonal is the claims file's standard choice (O1).
- Which footprint holds the background ROIs is not given ("within a footprint of an electrode",
  Methods 2.5). The claims file, amended on 2026-11-20 in answer to this attempt's question,
  makes it an open reading (O1 i to iv, the footprint at the same position in every well). Each
  footprint gets 3 ROIs (its centre and 0.5 mm to either side across the diagonal); `profiles`
  returns every footprint's value, and `with_background` gives the profile with the background
  from one footprint. `profiles` itself subtracts the darkest footprint of the well, the choice
  this attempt made before the answer, kept in the notebook as a reference.
- ROIs parallel to the sides (Fig. 3C, claim fig3bc-rate-suppresses-off-target): along the lines
  through the centre to the middle of each side, 6.4 mm out (half the 12.8-mm side), at whole
  mm to 6 mm (`DIST_PAR_A`) or contiguous to 6.09 mm (`DIST_PAR_B`), the last ROIs inside the
  square; `parallel_profiles`.
- ROI positions (O1): reading (a) ROIs centred at whole mm, 0 to 7 mm (`DIST_A`); reading (b)
  contiguous ROIs, one ROI length (0.406 mm) per step, from the centre outward (`DIST_B`).
- Electrode geometry: four 2.8-mm needles in a square with 15.3-mm side-to-side diagonals
  (Methods 2.2), so 6 and 7 mm from the centre are 1.65 and 0.65 mm from an electrode
  (Results 3.1). The footprints are found in each image as dark disks of that diameter at the
  corners of a square (`find_array`); the geometry found is printed in the notebook.
- Lorentzian YP(x) = a (b/2)^2 / (x^2 + (b/2)^2) and Gaussian Pr(x) = a exp(-x^2 / (2 s^2)),
  FWHM = 2.4 s, fitted by least squares: Methods 2.5 (F4).
"""

from __future__ import annotations

import re
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

import h5py
import numpy as np
import remfile
import requests
from scipy import ndimage as ndi
from scipy.optimize import curve_fit

VERSIONS = {
    "001047": "0.250701.1609",
    "001276": "0.250701.1609",
    "001277": "0.250701.1610",
    "001284": "0.250701.1610",
}
API = "https://api.dandiarchive.org/api"

PIXEL_UM = 1.625            # OME PhysicalSizeX of every file
BLOCK = 16                  # block mean of 16 x 16 pixels, 26 um, a standard choice
MM_PER_PX = PIXEL_UM * BLOCK / 1000.0
ROI_ALONG_MM, ROI_ACROSS_MM = 0.406, 0.325      # Methods 2.5
NEEDLE_D_MM = 2.8                               # Methods 2.2
DIAG_GAP_MM = 15.3                              # Methods 2.2, edge to edge along a diagonal
SIDE_MM = (DIAG_GAP_MM + NEEDLE_D_MM) / np.sqrt(2)   # 12.8 mm between electrode centres
DIST_A = np.arange(0.0, 7.01, 1.0)                     # O1 reading (a)
DIST_B = np.arange(0, 19) * ROI_ALONG_MM               # O1 reading (b), out to 7.3 mm
DIST_PAR_A = np.arange(0.0, 6.01, 1.0)                 # parallel to the sides, to 6.4 mm
DIST_PAR_B = np.arange(0, 16) * ROI_ALONG_MM           # contiguous, out to 6.09 mm


# ---------------------------------------------------------------- listing and metadata

def list_assets(dandiset: str) -> list[dict]:
    """Every asset of a dandiset at its pinned version (path, asset_id, size)."""
    url = f"{API}/dandisets/{dandiset}/versions/{VERSIONS[dandiset]}/assets/?page_size=400"
    out = []
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        j = r.json()
        out += [dict(dandiset=dandiset, path=a["path"], asset_id=a["asset_id"], size=a["size"])
                for a in j["results"]]
        url = j["next"]
    return out


def s3_url(asset_id: str) -> str:
    r = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=False, timeout=60)
    return r.headers["location"]


def _open(asset_id: str):
    f = h5py.File(remfile.File(s3_url(asset_id), verbose=False), "r")
    key = list(f["acquisition"])[0]
    return f, f["acquisition"][key]


def read_metadata(asset: dict) -> dict:
    """Exposure parameters of one file, parsed from its session description."""
    f, acq = _open(asset["asset_id"])
    sd = f["session_description"][()].decode()
    strain = f["general/subject/strain"][()].decode() if "general/subject/strain" in f else ""
    desc = acq.attrs.get("description", "")
    shape = acq["data"].shape
    spec = sd.split("General Protocol")[0]
    gen = sd.split("General Protocol")[-1]
    first = lambda pat, s=spec: (re.findall(pat, s) or [None])[0]
    channel = (first(r"Fluorescent Channel(?:\(s\))?(?: used)?: ([\w-]+)")
               or first(r"Channel used: (\w+)", sd))
    proto = sorted(set(re.findall(r"(CanCan|Control)", spec)))
    m = dict(asset, subject=asset["path"].split("/")[0][4:], cell=strain.replace("cellline: ", ""),
             channel=channel, phase=first(r"Phase: (\w+)"),
             protocol="/".join(proto), packet_rate=first(r"at ([\d.]+ ?[kKM]?Hz) frequency"),
             repeats=first(r"repeated (\d+|Unknown) ?time"), pulse_ns=first(r"Pulse duration - (\d+) ns"),
             packets=first(r"consisted of (\d+) packets"),
             elevation_mm=first(r"(\d) mm electrode elevation"),
             sham="SHAM" in spec,
             spacing_mm=first(r"(?:distance|spacing)[^.]*?([\d.]+) mm", gen),
             first_pulse_kv=first(r"([\d.]+) ?kV", gen),
             two_hours=("2 hours after" in spec) or ("Cy3" in (channel or "")),
             shape=tuple(int(x) for x in shape),
             pixel_um=float(first(r'PhysicalSizeX="([\d.]+)"', desc) or "nan"),
             ome_channels=re.findall(r'<OME:Channel ID="Channel:\d+" Name="(\w+)"', desc))
    f.close()
    return m


# ---------------------------------------------------------------- images

def read_reduced(asset_id: str, block: int = BLOCK) -> np.ndarray:
    """A whole-well image as block means, float32, shape (channels, rows, columns). Pixels
    outside the stitched tiles are zero in the files."""
    f, acq = _open(asset_id)
    d = acq["data"]
    n = d.shape[-2] // block * block
    m = d.shape[-1] // block * block
    nc = d.shape[1] if d.ndim == 4 else 1
    rows = []
    step = block * 16
    for i in range(0, n, step):
        rs = slice(i, min(i + step, n))
        blk = (d[0, :, rs, :m] if d.ndim == 4 else d[0, rs, :m][None]).astype(np.float32)
        rows.append(blk.reshape(nc, -1, block, m // block, block).mean(axis=(2, 4)))
    f.close()
    return np.concatenate(rows, axis=1)


def read_many(asset_ids: list[str], workers: int = 4) -> list[np.ndarray]:
    """read_reduced over many files in parallel processes."""
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(read_reduced, asset_ids))


# ---------------------------------------------------------------- electrode array

def _kernel(r_lo_mm, r_hi_mm, scale):
    R = int(np.ceil(r_hi_mm / MM_PER_PX * scale)) + 1
    yy, xx = np.mgrid[-R:R + 1, -R:R + 1]
    rr = np.hypot(yy, xx) * MM_PER_PX / scale
    k = ((rr >= r_lo_mm) & (rr <= r_hi_mm)).astype(np.float32)
    return k / k.sum()


def footprint_score(im: np.ndarray) -> np.ndarray:
    """Score for a needle footprint centred at each pixel, in units of the local mean. A
    footprint shows either as a dark disk (no YP uptake under the hollow needle) or as a
    bright ring at the needle wall; the score is the larger of the dark-disk contrast (ring
    1.7 to 2.3 mm minus disk within 1.1 mm) and the bright-ring contrast (annulus 1.15 to 1.65
    mm minus the mean of the disk within 0.9 mm and the annulus 1.9 to 2.4 mm)."""
    scale = 0.5
    valid_px = im[im > 0]
    lo, hi = np.percentile(valid_px, [1, 98]) if valid_px.size else (0, 1)
    small = ndi.zoom(np.where(im > 0, np.clip(im, lo, hi), 0), scale, order=1)
    conv = lambda lo, hi: ndi.convolve(small, _kernel(lo, hi, scale), mode="constant")
    inner = conv(0.0, 1.1)
    outer = conv(1.7, 2.3)
    wall = conv(1.15, 1.65)
    core = conv(0.0, 0.9)
    out2 = conv(1.9, 2.4)
    valid = ndi.convolve((small > 0).astype(np.float32), _kernel(0, 2.4, scale),
                         mode="constant") > 0.98
    norm = np.maximum(outer, 1.0)
    disk = (outer - inner) / norm
    ring = (wall - (core + out2) / 2) / norm
    c = np.where(valid, np.maximum(disk, 2 * ring), 0.0)
    return ndi.zoom(c, im.shape[0] / c.shape[0], order=1)[: im.shape[0], : im.shape[1]]


def find_array(im: np.ndarray) -> dict:
    """Centre, rotation and half-side of the square of footprints that maximises the summed
    dark-disk score at its four corners. Returns footprint centres in pixels (x, y). On a
    synthetic image it recovers the centre and rotation exactly and gives a side about 0.4 mm
    short (verifier, round 1); the side is used only to accept a square (MAX_SIDE_ERR_MM)."""
    c = footprint_score(im)
    H, W = im.shape
    sm = ndi.uniform_filter(np.where(im > 0, im, 0), int(3 / MM_PER_PX))
    best = None
    half0 = SIDE_MM / 2 / MM_PER_PX
    cy0, cx0 = H / 2, W / 2
    # coarse grid, then a fine one around the best
    for stage in range(2):
        if stage == 0:
            cys = np.arange(cy0 - 6 / MM_PER_PX, cy0 + 6 / MM_PER_PX, 6)
            cxs = np.arange(cx0 - 6 / MM_PER_PX, cx0 + 6 / MM_PER_PX, 6)
            ths = np.deg2rad(np.arange(-8, 8.1, 1.0))
            hs = half0 * np.arange(0.94, 1.061, 0.02)
        else:
            _, by, bx, bt, bh = best
            cys = np.arange(by - 6, by + 6.1, 1)
            cxs = np.arange(bx - 6, bx + 6.1, 1)
            ths = bt + np.deg2rad(np.arange(-2, 2.1, 0.5))
            hs = bh * np.arange(0.97, 1.031, 0.005)
        CY, CX = np.meshgrid(cys, cxs, indexing="ij")
        for th in ths:
            for h in hs:
                score = 0.0
                for sx, sy in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
                    dx = h * (sx * np.cos(th) - sy * np.sin(th))
                    dy = h * (sx * np.sin(th) + sy * np.cos(th))
                    score = score + ndi.map_coordinates(c, [CY + dy, CX + dx], order=1, cval=0.0)
                k = np.unravel_index(np.argmax(score), score.shape)
                if best is None or score[k] > best[0]:
                    best = (float(score[k]), float(CY[k]), float(CX[k]), float(th), float(h))
    s, cy, cx, th, h = best
    corners = []
    for sx, sy in ((-1, -1), (1, -1), (1, 1), (-1, 1)):
        corners.append((cx + h * (sx * np.cos(th) - sy * np.sin(th)),
                        cy + h * (sx * np.sin(th) + sy * np.cos(th))))
    corners = np.array(corners)
    per_corner = [float(ndi.map_coordinates(c, [[y], [x]], order=1)[0]) for x, y in corners]
    return dict(centre=(cx, cy), theta_deg=np.rad2deg(th), side_mm=2 * h * MM_PER_PX,
                corners=corners, score=s / 4, corner_scores=per_corner)


MIN_CORNER_SCORE = 0.15     # a standard choice, from inspecting the detections (notebook)
MAX_SIDE_ERR_MM = 0.6       # side of the found square within 0.6 mm of 12.8 mm


def reliable(geom: dict) -> bool:
    """A footprint square is taken as found when every corner scores at least
    MIN_CORNER_SCORE and its side is within MAX_SIDE_ERR_MM of the nominal 12.8 mm."""
    return (min(geom["corner_scores"]) >= MIN_CORNER_SCORE
            and abs(geom["side_mm"] - SIDE_MM) <= MAX_SIDE_ERR_MM)


def spot_centre(im: np.ndarray, search_mm: float = 5.0) -> tuple[float, float]:
    """Centre of the central bright spot: the maximum of the image smoothed with a 0.5-mm
    Gaussian within search_mm of the image centre, refined as the intensity-weighted centroid
    of the smoothed image above its half-maximum (over the local median) within 1.5 mm."""
    v = im[im > 0]
    hi = np.percentile(v, 99.5) if v.size else 1.0
    sm = ndi.gaussian_filter(np.clip(im, 0, hi), 0.5 / MM_PER_PX)
    H, W = im.shape
    yy, xx = np.mgrid[0:H, 0:W]
    near = np.hypot(yy - H / 2, xx - W / 2) <= search_mm / MM_PER_PX
    base = np.median(sm[near & (im > 0)])
    k = np.argmax(np.where(near, sm, -np.inf))
    py, px = np.unravel_index(k, sm.shape)
    w = sm - base
    disk = np.hypot(yy - py, xx - px) <= 1.5 / MM_PER_PX
    w = np.where(disk & (w > 0.5 * w[py, px]), w, 0.0)
    return float((w * xx).sum() / w.sum()), float((w * yy).sum() / w.sum())


def geometry_from_centre(centre_xy, theta_deg: float) -> dict:
    """Nominal square (12.8-mm side) at a given centre and rotation."""
    th = np.deg2rad(theta_deg)
    h = SIDE_MM / 2 / MM_PER_PX
    cx, cy = centre_xy
    corners = np.array([(cx + h * (sx * np.cos(th) - sy * np.sin(th)),
                         cy + h * (sx * np.sin(th) + sy * np.cos(th)))
                        for sx, sy in ((-1, -1), (1, -1), (1, 1), (-1, 1))])
    return dict(centre=(cx, cy), theta_deg=theta_deg, side_mm=SIDE_MM, corners=corners,
                score=np.nan, corner_scores=[np.nan] * 4)


# ---------------------------------------------------------------- ROI measures

def roi_mean(im: np.ndarray, centre_xy, along_unit, along_mm=ROI_ALONG_MM,
             across_mm=ROI_ACROSS_MM) -> float:
    """Mean of a rectangular ROI centred at centre_xy (pixels), its long side along along_unit."""
    ux, uy = along_unit
    vx, vy = -uy, ux
    a = np.linspace(-along_mm / 2, along_mm / 2, max(3, int(round(along_mm / MM_PER_PX)) + 1))
    b = np.linspace(-across_mm / 2, across_mm / 2, max(3, int(round(across_mm / MM_PER_PX)) + 1))
    A, B = np.meshgrid(a / MM_PER_PX, b / MM_PER_PX)
    xs = centre_xy[0] + A * ux + B * vx
    ys = centre_xy[1] + A * uy + B * vy
    v = ndi.map_coordinates(im, [ys.ravel(), xs.ravel()], order=1, cval=np.nan)
    return float(np.nanmean(v))


def profiles(im: np.ndarray, geom: dict, dists=DIST_A) -> dict:
    """Background-subtracted ROI means along the four half-diagonals.

    Returns `half` (4 x len(dists)), one row per half-diagonal from the centre toward each
    footprint (corner order of `find_array`), `background` (the value used), and
    `backgrounds` (one per footprint)."""
    cx, cy = geom["centre"]
    bgs = []
    half = []
    for x, y in geom["corners"]:
        u = np.array([x - cx, y - cy])
        u = u / np.hypot(*u)
        across = np.array([-u[1], u[0]])
        off = 0.5 / MM_PER_PX
        bgs.append(np.mean([roi_mean(im, (x + k * off * across[0], y + k * off * across[1]), u)
                            for k in (-1, 0, 1)]))
        half.append([roi_mean(im, (cx + d / MM_PER_PX * u[0], cy + d / MM_PER_PX * u[1]), u)
                     for d in dists])
    bg = float(np.min(bgs))
    return dict(half=np.array(half) - bg, raw=np.array(half), background=bg,
                backgrounds=np.array(bgs), dists=np.asarray(dists))


def parallel_profiles(im: np.ndarray, geom: dict, dists=DIST_PAR_A) -> dict:
    """As `profiles`, along the four half-lines from the centre parallel to the sides of the
    square, each ending at the middle of a side, 6.4 mm out (Fig. 3C, claims file
    fig3bc-rate-suppresses-off-target). Row k runs toward the middle of the side from corner k
    to corner k+1 (corner order of `find_array`); the background is that of `profiles`."""
    cx, cy = geom["centre"]
    c = np.asarray(geom["corners"])
    half = []
    for k in range(4):
        mx, my = (c[k] + c[(k + 1) % 4]) / 2
        u = np.array([mx - cx, my - cy])
        u = u / np.hypot(*u)
        half.append([roi_mean(im, (cx + d / MM_PER_PX * u[0], cy + d / MM_PER_PX * u[1]), u)
                     for d in dists])
    p = profiles(im, geom, dists[:1])
    bg = p["background"]
    return dict(half=np.array(half) - bg, raw=np.array(half), background=bg,
                backgrounds=p["backgrounds"], dists=np.asarray(dists))


def with_background(p: dict, footprint) -> dict:
    """A profile from `profiles` or `parallel_profiles` with the background taken from one
    footprint (claims file O1 readings i to iv): `footprint` 0 to 3 is the footprint at that
    corner of `find_array` (upper left, upper right, lower right, lower left in the image),
    the same position in every well; "min" is the darkest footprint of the well."""
    bg = float(np.min(p["backgrounds"])) if footprint == "min" else float(p["backgrounds"][footprint])
    return dict(p, half=p["raw"] - bg, background=bg)


def pooled(p: dict, reading: str = "a") -> tuple[np.ndarray, np.ndarray]:
    """One experiment's profile from its half-diagonals (claims file O2).

    Reading "a": the two diagonals averaged at each signed distance; corners 0 and 2 form one
    diagonal, 1 and 3 the other; negative x runs toward corners 0 and 3 (left of the image).
    Reading "b": the four half-diagonals averaged at each distance and mirrored to -x.
    Returns (x, values) with x from -max to +max, the centre once."""
    d = p["dists"]
    h = p["half"]
    if reading == "a":
        neg = (h[0] + h[3]) / 2      # toward the two left electrodes
        pos = (h[2] + h[1]) / 2      # toward the two right electrodes
    else:
        neg = pos = h.mean(axis=0)
    x = np.concatenate([-d[:0:-1], d])
    y = np.concatenate([neg[:0:-1], pos])
    return x, y


# ---------------------------------------------------------------- fits

def lorentz(x, a, b):
    return a * (b / 2) ** 2 / (x ** 2 + (b / 2) ** 2)


def gauss(x, a, s):
    return a * np.exp(-x ** 2 / (2 * s ** 2))


def fit(x, y, func="lorentz", half_range=4.0):
    """Least-squares fit over |x| <= half_range. Returns dict(a, b or s, fwhm, r2, r_pearson,
    p_pearson, n, ok)."""
    from scipy import stats
    m = (np.abs(x) <= half_range + 1e-9) & np.isfinite(y)
    xx, yy = x[m], y[m]
    f = lorentz if func == "lorentz" else gauss
    if m.sum() < 3:
        return dict(ok=False, a=np.nan, w=np.nan, fwhm=np.nan, r2=np.nan, r=np.nan, p_r=np.nan,
                    p_f=np.nan, n=int(m.sum()))
    p0 = [max(yy.max(), 1e-3), 2.0 if func == "lorentz" else 1.0]
    try:
        p, _ = curve_fit(f, xx, yy, p0=p0, bounds=([0, 1e-3], [np.inf, 100]), maxfev=20000)
        ok = True
    except RuntimeError:
        return dict(ok=False, a=np.nan, w=np.nan, fwhm=np.nan, r2=np.nan, r=np.nan, p_r=np.nan,
                    p_f=np.nan, n=int(m.sum()))
    pred = f(xx, *p)
    ss_res = float(np.sum((yy - pred) ** 2))
    ss_tot = float(np.sum((yy - yy.mean()) ** 2))
    r2 = 1 - ss_res / ss_tot
    r, p_r = stats.pearsonr(pred, yy)
    n, k = len(yy), 2
    # F test of the fit against the mean-only model
    F = ((ss_tot - ss_res) / (k - 1)) / (ss_res / (n - k)) if ss_res > 0 else np.inf
    p_f = float(stats.f.sf(F, k - 1, n - k))
    fwhm = p[1] if func == "lorentz" else 2.4 * p[1]
    return dict(ok=ok, a=float(p[0]), w=float(p[1]), fwhm=float(fwhm), r2=r2, r=float(r),
                p_r=float(p_r), p_f=p_f, n=n)


def slope_test(x, y):
    """Least-squares line, slope and its two-sided t test (scipy.stats.linregress)."""
    from scipy import stats
    res = stats.linregress(np.asarray(x, float), np.asarray(y, float))
    return dict(slope=res.slope, intercept=res.intercept, r=res.rvalue, p=res.pvalue,
                se=res.stderr, n=len(x))


def gap_exceeds(m1, se1, m2, se2) -> bool:
    """The paper's graph reading (Methods 2.5, F8): a gap between the error bars (mean +/- s.e.)
    larger than the length of the error bars. The length is taken as the larger of the two
    s.e., a standard choice when the two differ."""
    lo, hi = (m1, se1), (m2, se2)
    if m1 > m2:
        lo, hi = hi, lo
    gap = (hi[0] - hi[1]) - (lo[0] + lo[1])
    return bool(gap > max(se1, se2))


# ---------------------------------------------------------------- whole-dataset tables

def metadata_table(dandisets=tuple(VERSIONS)) -> list[dict]:
    """read_metadata for every asset of the given dandisets (threads; metadata only)."""
    assets = [a for d in dandisets for a in list_assets(d)]
    with ThreadPoolExecutor(16) as ex:
        return list(ex.map(read_metadata, assets))


THETA_DEFAULT_DEG = -3.0    # median rotation of the squares found (notebook); an assumption


def well_profiles(files: list[dict], images: dict, workers: int = 4) -> list[dict]:
    """Profiles of every channel of every well.

    files: metadata rows of the files of the wells; images: asset_id -> reduced image.
    The array geometry of a well is the best-scoring reliable footprint square found in any
    of its images (the images of one well share one stage frame, checked in the notebook);
    where none is reliable, the nominal square centred on the central YP spot of the well's
    FITC image, rotated by THETA_DEFAULT_DEG (an assumption, stated in the notebook)."""
    wells = {}
    for m in files:
        wells.setdefault((m["dandiset"], m["subject"]), []).append(m)
    jobs = [(items, {m["asset_id"]: images[m["asset_id"]] for m in items})
            for items in wells.values()]
    with ProcessPoolExecutor(workers) as ex:
        return [r for rows in ex.map(_one_well, jobs) for r in rows]


def _one_well(job):
    items, images = job
    dets = []
    for m in items:
        for c, im in enumerate(images[m["asset_id"]]):
            g = find_array(im)
            g["source"] = f"{m['channel']} channel {c}"
            dets.append(g)
    found = [g for g in dets if reliable(g)]
    if found:
        geom, how = max(found, key=lambda g: g["score"]), "footprints"
    else:
        fitc = [m for m in items if m["channel"] == "FITC"][0]
        geom = geometry_from_centre(spot_centre(images[fitc["asset_id"]][0]), THETA_DEFAULT_DEG)
        how = "spot centre"
    out = []
    for m in items:
        names = ["FITC"] if m["channel"] == "FITC" else ["Cy3", "DAPI_2h"]
        for c, name in enumerate(names):
            im = images[m["asset_id"]][c]
            out.append(dict(m, chan=name, how=how, geom=geom, n_found=len(found), detections=dets,
                            pa=profiles(im, geom, DIST_A), pb=profiles(im, geom, DIST_B),
                            qa=parallel_profiles(im, geom, DIST_PAR_A),
                            qb=parallel_profiles(im, geom, DIST_PAR_B),
                            zone=zone_values(im, geom)))
    return out


def zone_values(im: np.ndarray, geom: dict) -> dict:
    """Mean intensity (not background-subtracted) in the zones of claim fig5c-nuclear-yp-centre,
    along the four half-diagonals: zone 1 within 1 mm of the centre, zone 2 at 2 to 4 mm
    (reading a) or 3 to 5 mm (reading b), zone 3 the 0.5-mm band outside an electrode wall
    (7.15 to 7.65 mm), and the footprints (3 ROIs each, as for the background)."""
    p = profiles(im, geom, np.arange(0.0, 7.66, 0.1))
    d, raw = p["dists"], p["raw"].mean(axis=0)
    sel = lambda lo, hi: float(np.nanmean(raw[(d >= lo - 1e-9) & (d <= hi + 1e-9)]))
    v = im[im > 0]
    return dict(zone1=sel(0, 1), zone2a=sel(2, 4), zone2b=sel(3, 5), zone3=sel(7.15, 7.65),
                footprint=float(np.mean(p["backgrounds"])), background=p["background"],
                offset=float(np.percentile(v, 0.1)) if v.size else np.nan,
                median=float(np.median(v)) if v.size else np.nan)
