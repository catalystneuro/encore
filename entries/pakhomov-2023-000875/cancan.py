"""Loading and profile measures for dandiset 000875 (Pakhomov et al. 2023, NG-CANCAN).

The dandiset holds one stitched YO-PRO-1 (YP) image per dish (a 20480 x 20480 uint16
ImageSeries with one frame), taken after Packet 2 was applied 1, 5 or 10 times from each of
the four electrodes of a quadrupole array (1Px4, 5Px4, 10Px4), first pulse 3.2 kV, three dishes
per treatment. This is the experiment of Fig. 6 of the paper.

Where each parameter comes from:

- ``PIXEL_UM`` (0.65 um per pixel): an assumption. The files give no pixel size. It is the
  sensor pixel of the ORCA-Flash4 camera (6.5 um) through the 10x objective named in the
  session's device description and in Methods 2.4. The notebook checks it against the needle
  diameter (1.5 mm, Methods 2.3) measured on the electrode footprints.
- ``HALF_SPAN_MM`` (1.65 mm for the small array) and ``N_ROI`` (92 for the small array):
  Methods 2.4, "The measurements were performed in 92 or 224 regions of interest (ROI), placed
  along one or both diagonals, and covering a distance of +/- 1.65 mm or +/- 3.65 mm from the
  geometrical center for the small and large arrays, respectively". Which array the images show
  is taken from the images (claims file header), and the notebook shows it is the small one.
- ROI layout readings r1 (all 92 ROIs on one diagonal) and r2 (46 on each diagonal, averaged at
  equal distance from the center): the claims file header. ROI width equal to the ROI spacing,
  square ROIs centred on the diagonal: a standard choice named in the claims file header.
- The geometrical center: the mean of the four electrode footprint centers (Methods 2.4,
  "distance from the geometrical center of the electrode array").
- Background readings b1 (raw) and b2 (minus "a cell-free or dark offset, where the data hold
  one"): the claims file header. The files hold no dark frame. b2-dark subtracts the 1st
  percentile of the image's nonzero block means, which lie far outside the array (the notebook
  maps them and checks that the zero padding does not set the level); b2-min subtracts the
  darkest pixel of the full-resolution region around the array. Both are standard choices for a
  dark offset. The median inside the electrode footprints (b2-fp) was the b2 of the first round;
  the footprints hold a faint monolayer, so it is not cell-free and is kept only as a variant
  outside the outcome.
- Center readings c1 (the ROI nearest the center; with an even number of ROIs two are equally
  near, and their mean is taken, a standard choice) and c2 (the highest ROI between the minima on
  either side): the claims file header.
- Periphery readings e1 (mean of the two ends) and e2 (each end): the claims file header, from
  Methods 2.4, "in percent to the most peripheral (closest to the electrode) ROI".
- Normalization readings n1 and n2: the claims file header.
- LOESS spans 0.25 and 0.5: standard choices named in the claims file header (Methods 2.4 names
  LOESS without a span).
"""

from __future__ import annotations

import re
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import remfile
import requests
from scipy.signal import fftconvolve

DANDISET_ID = "000875"
DANDISET_VERSION = "0.240515.1925"
API = "https://api.dandiarchive.org/api"
DATA_PATH = "acquisition/ScanningImaging/data"

PIXEL_UM = 0.65          # assumption, see module docstring
HALF_SPAN_MM = 1.65      # Methods 2.4, small array
N_ROI = 92               # Methods 2.4, small array
BLOCK = 8                # overview block size (pixels); a standard choice for locating electrodes
STRIP = 1280             # rows per streamed strip (a multiple of the 160-row HDF5 chunk)


def list_assets():
    """Assets of the pinned version, with the treatment parsed from the path."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=100"
    out = []
    for a in requests.get(url, timeout=60).json()["results"]:
        m = re.match(r"sub-(\d+)p-x4-600ns-200ms-(\d)-(\d)kV-YP-\(dish(\d+)\)", a["path"])
        per_electrode = int(m.group(1))
        out.append({
            "asset_id": a["asset_id"], "path": a["path"], "size": a["size"],
            "per_electrode": per_electrode, "total_packets": 4 * per_electrode,
            "treatment": f"{per_electrode}Px4", "kv_from_name": float(f"{m.group(2)}.{m.group(3)}"),
            "dish": int(m.group(4)),
        })
    return sorted(out, key=lambda a: (a["per_electrode"], a["dish"]))


def version_metadata():
    """The archive's metadata record of the pinned version."""
    return requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/", timeout=60).json()


def asset_url(asset_id):
    return f"{API}/assets/{asset_id}/download/"


def open_file(asset_id):
    return h5py.File(remfile.File(asset_url(asset_id)), "r")


def read_metadata(asset_id):
    with open_file(asset_id) as f:
        d = f[DATA_PATH]
        s = f["general/subject"]
        g = f["acquisition/ScanningImaging"]
        return {
            "shape": d.shape, "dtype": str(d.dtype), "chunks": d.chunks,
            "unit": d.attrs.get("unit"), "conversion": float(d.attrs.get("conversion")),
            "offset": float(d.attrs.get("offset", 0.0)), "rate": float(f["acquisition/ScanningImaging/starting_time"].attrs["rate"]),
            "series_fields": sorted(g.keys()),
            "device_description": g.attrs.get("description"),
            "session_description": f["session_description"][()].decode(),
            "session_id": f["general/session_id"][()].decode(),
            "session_start_time": f["session_start_time"][()].decode(),
            "subject_id": s["subject_id"][()].decode(), "species": s["species"][()].decode(),
            "strain": s["strain"][()].decode(), "age": s["age"][()].decode(), "sex": s["sex"][()].decode(),
            "experimenter": [x.decode() for x in f["general/experimenter"][()]],
            "groups": sorted(f.keys()),
        }


def _strip(args):
    asset_id, r0, r1, c0, c1, block = args
    with open_file(asset_id) as f:
        x = f[DATA_PATH][0, r0:r1, c0:c1].astype(np.float32)
    if block == 1:
        return x
    h, w = x.shape
    return x.reshape(h // block, block, w // block, block).mean(axis=(1, 3))


def _read(asset_id, r0, r1, c0, c1, block, workers):
    edges = list(range(r0, r1, STRIP)) + [r1]
    jobs = [(asset_id, a, b, c0, c1, block) for a, b in zip(edges[:-1], edges[1:])]
    with ProcessPoolExecutor(workers) as ex:
        return np.vstack(list(ex.map(_strip, jobs)))


def load_overview(asset_id, block=BLOCK, workers=8):
    """The whole image as block means (block x block pixels), streamed in strips."""
    return _read(asset_id, 0, 20480, 0, 20480, block, workers)


def saturated_fraction(asset_id, r0, r1, c0, c1):
    with open_file(asset_id) as f:
        x = f[DATA_PATH][0, r0:r1, c0:c1]
    return float((x >= 65535).mean()), int(x.max())


def load_region(asset_id, center, half, workers=8):
    """Full-resolution square of half-width ``half`` pixels around ``center`` (row, col)."""
    r0 = int(center[0]) - half
    c0 = int(center[1]) - half
    r0 -= r0 % 160  # align to chunks
    r1 = int(center[0]) + half
    r1 += (-r1) % 160
    c1 = int(center[1]) + half
    return _read(asset_id, r0, r1, c0, c1, 1, workers), (r0, c0)


# ---------------------------------------------------------------- electrodes

def _disc(r):
    y, x = np.mgrid[-r:r + 1, -r:r + 1]
    return (x * x + y * y <= r * r).astype(float)


def find_electrodes(overview, block=BLOCK):
    """Centers and radii of the four dark electrode footprints, in full-resolution pixels.

    A disc-minus-annulus filter on the log image finds four coarse centers (a standard image
    processing choice); each is then refined by fitting a circle to the largest radial step of
    intensity along 36 rays. Zero-valued padding outside the stitched tiles is replaced by the
    median so it is not taken for a footprint.
    """
    im = overview.astype(float)
    k = 4
    h, w = (im.shape[0] // k) * k, (im.shape[1] // k) * k
    sm = im[:h, :w].reshape(h // k, k, w // k, k).mean(axis=(1, 3))
    med = np.median(sm[sm > 0])
    sm = np.log(np.where(sm < 20, med, sm))
    n = sm.shape[0]
    lo, hi = int(n * 0.23), int(n * 0.78)
    best = None
    for r in range(20, 46, 2):
        d = _disc(r)
        R = int(r * 1.5)
        a = _disc(R)
        a[R - r:R + r + 1, R - r:R + r + 1] -= d
        c = fftconvolve(sm, d / d.sum(), "same") - fftconvolve(sm, a / a.sum(), "same")
        cc = c.copy()
        pts = []
        for _ in range(4):
            sub = cc[lo:hi, lo:hi]
            i = np.unravel_index(np.argmin(sub), sub.shape)
            i = (i[0] + lo, i[1] + lo)
            pts.append((i, cc[i]))
            cc[max(0, i[0] - 2 * r):i[0] + 2 * r, max(0, i[1] - 2 * r):i[1] + 2 * r] = np.inf
        score = sum(p[1] for p in pts)
        if best is None or score < best[0]:
            best = (score, r, pts)
    _, r, pts = best
    logim = np.log(np.clip(im, 1, None))
    out = []
    for (cy, cx), _ in pts:
        cy, cx = cy * k + k // 2, cx * k + k // 2
        rmax = int(r * k * 1.6)
        edge = []
        for ang in np.deg2rad(np.arange(0, 360, 10)):
            rr = np.arange(int(r * k * 0.5), rmax)
            yy = np.clip((cy + rr * np.sin(ang)).astype(int), 0, im.shape[0] - 1)
            xx = np.clip((cx + rr * np.cos(ang)).astype(int), 0, im.shape[1] - 1)
            prof = np.convolve(logim[yy, xx], np.ones(5) / 5, "same")
            g = np.diff(prof)[3:-3]
            j = np.argmax(g) + 3
            edge.append((cy + rr[j] * np.sin(ang), cx + rr[j] * np.cos(ang)))
        edge = np.array(edge)
        # algebraic circle fit, then one pass dropping rays more than 15% off the fit
        for _ in range(2):
            A = np.c_[2 * edge[:, 0], 2 * edge[:, 1], np.ones(len(edge))]
            bb = (edge ** 2).sum(1)
            (y0, x0, cst), *_ = np.linalg.lstsq(A, bb, rcond=None)
            rad = np.sqrt(cst + y0 ** 2 + x0 ** 2)
            dist = np.hypot(edge[:, 0] - y0, edge[:, 1] - x0)
            edge = edge[np.abs(dist - rad) < 0.15 * rad]
        out.append({"row": y0 * block, "col": x0 * block, "radius": rad * block})
    # order by angle around the center, so 0-2 and 1-3 are the diagonals
    cy = np.mean([e["row"] for e in out])
    cx = np.mean([e["col"] for e in out])
    out.sort(key=lambda e: np.arctan2(e["row"] - cy, e["col"] - cx))
    return out


def geometry(electrodes, pixel_um=PIXEL_UM):
    c = np.array([[e["row"], e["col"]] for e in electrodes])
    center = c.mean(0)
    diag = [np.linalg.norm(c[2] - c[0]), np.linalg.norm(c[3] - c[1])]
    sides = [np.linalg.norm(c[(i + 1) % 4] - c[i]) for i in range(4)]
    radii = [e["radius"] for e in electrodes]
    inner = [diag[0] - radii[0] - radii[2], diag[1] - radii[1] - radii[3]]
    mm = pixel_um / 1000
    return {
        "center": center, "diag_cc_mm": [d * mm for d in diag], "side_cc_mm": [s * mm for s in sides],
        "footprint_diameter_mm": [2 * r * mm for r in radii], "diag_inner_mm": [d * mm for d in inner],
    }


def geometric_half_span(electrodes):
    """Half-span in pixels that ends 5% of the diagonal short of the footprint edges.

    A variant free of the assumed pixel size: Methods 2.4 excludes "Areas immediately adjacent
    to the electrodes (<5% of the diagonal length)". The diagonal is taken here as the distance
    between footprint edges, averaged over the two diagonals.
    """
    c = np.array([[e["row"], e["col"]] for e in electrodes])
    r = [e["radius"] for e in electrodes]
    inner = np.mean([np.linalg.norm(c[2] - c[0]) - r[0] - r[2], np.linalg.norm(c[3] - c[1]) - r[1] - r[3]])
    return 0.45 * inner


def footprint_level(overview, electrodes, block=BLOCK, frac=0.7):
    """Median block intensity inside the electrode footprints (within ``frac`` of the radius).

    The footprints hold a faint monolayer (the notebook shows a full-resolution crop), so this is
    the level of cells that took up little dye, not a cell-free or dark offset. It is kept as the
    variant b2-fp, outside the readings of the claims file.
    """
    vals = []
    yy, xx = np.mgrid[0:overview.shape[0], 0:overview.shape[1]]
    for e in electrodes:
        m = np.hypot(yy - e["row"] / block, xx - e["col"] / block) < frac * e["radius"] / block
        vals.append(overview[m])
    return float(np.median(np.concatenate(vals)))


def dark_level(overview, q=1.0):
    """The ``q``-th percentile of the nonzero block means of the whole image (reading b2-dark).

    The darkest blocks lie far outside the array, more than twice the center-to-footprint distance
    from its center (the notebook maps them). The files hold no dark frame, so this is the
    closest thing to a dark offset the data hold; 1% is a standard choice, and the notebook prints
    0.1% and 5% too.
    """
    return float(np.percentile(overview[overview > 0], q))


def zone_values(overview, electrodes, block=BLOCK):
    """Block means in three zones, for the histograms of the notebook.

    footprint: within 0.7 of each footprint radius; monolayer outside: 1.2 to 1.6 times the mean
    center-to-footprint distance from the array center, more than 1.3 radii from any footprint;
    between: within 0.5 of that distance from the center (the exposed area of the array).
    """
    yy, xx = np.mgrid[0:overview.shape[0], 0:overview.shape[1]]
    c = np.array([[e["row"], e["col"]] for e in electrodes]) / block
    r = np.array([e["radius"] for e in electrodes]) / block
    cen = c.mean(0)
    R = np.mean(np.linalg.norm(c - cen, axis=1))
    dfp = np.stack([np.hypot(yy - a, xx - b) / rr for (a, b), rr in zip(c, r)]).min(0)
    dc = np.hypot(yy - cen[0], xx - cen[1])
    nz = overview > 0
    return {
        "footprint": overview[(dfp < 0.7) & nz],
        "outside": overview[(dc > 1.2 * R) & (dc < 1.6 * R) & (dfp > 1.3) & nz],
        "between": overview[(dc < 0.5 * R) & nz],
    }


# ---------------------------------------------------------------- ROI profiles

def roi_values(region, origin, center, toward, n, spacing_px, width_px=None):
    """Mean intensity in ``n`` square ROIs centred on the line from ``center`` toward ``toward``.

    ROIs are spaced ``spacing_px`` apart, symmetric about the center, with their side along and
    across the line equal to ``width_px`` (default: the spacing). Positions are returned in mm,
    negative on the side away from ``toward``.
    """
    width_px = spacing_px if width_px is None else width_px
    u = np.asarray(toward, float) - np.asarray(center, float)
    u /= np.linalg.norm(u)
    v = np.array([-u[1], u[0]])
    pos = (np.arange(n) - (n - 1) / 2) * spacing_px
    half = width_px / 2
    vals = np.empty(n)
    sat = np.empty(n)
    for i, p in enumerate(pos):
        cy, cx = np.asarray(center) + p * u
        r = int(np.ceil(half * np.sqrt(2))) + 1
        y0, x0 = int(cy) - r - origin[0], int(cx) - r - origin[1]
        patch = region[y0:y0 + 2 * r + 1, x0:x0 + 2 * r + 1]
        yy, xx = np.mgrid[y0:y0 + patch.shape[0], x0:x0 + patch.shape[1]]
        dy, dx = yy + origin[0] - cy, xx + origin[1] - cx
        m = (np.abs(dy * u[0] + dx * u[1]) <= half) & (np.abs(dy * v[0] + dx * v[1]) <= half)
        vals[i] = patch[m].mean()
        sat[i] = (patch[m] >= 65000).mean()  # near the 16-bit ceiling of these images
    return pos * PIXEL_UM / 1000, vals, sat


def dish_profiles(region, origin, electrodes, half_span_px=None):
    """The layouts of the claims file header for one dish.

    r1-dA, r1-dB: all 92 ROIs along diagonal A (electrodes 0 to 2) or B (1 to 3);
    r2: 46 ROIs along each diagonal, the two averaged at equal signed distance.
    ``half_span_px`` defaults to HALF_SPAN_MM at PIXEL_UM; ``geometric_half_span`` gives the
    variant that does not use the assumed pixel size.
    """
    c = np.array([[e["row"], e["col"]] for e in electrodes])
    center = c.mean(0)
    span_px = 2 * (HALF_SPAN_MM * 1000 / PIXEL_UM if half_span_px is None else half_span_px)
    out = {}
    s1 = span_px / N_ROI
    for name, (a, b) in {"r1-dA": (0, 2), "r1-dB": (1, 3)}.items():
        pos, vals, sat = roi_values(region, origin, center, c[b], N_ROI, s1)
        out[name] = {"pos_mm": pos, "values": vals, "saturated": sat}
    s2 = span_px / (N_ROI // 2)
    pa, va, sa = roi_values(region, origin, center, c[2], N_ROI // 2, s2)
    pb, vb, sb = roi_values(region, origin, center, c[3], N_ROI // 2, s2)
    out["r2"] = {"pos_mm": pa, "values": (va + vb) / 2, "saturated": (sa + sb) / 2}
    return out


# ---------------------------------------------------------------- profile measures

def center_index(profile, reading):
    """Indices of the center ROI(s): c1 the ROI(s) nearest 0; c2 the peak between the side minima."""
    n = len(profile)
    mid = [n // 2 - 1, n // 2] if n % 2 == 0 else [n // 2]
    if reading == "c1":
        return mid
    lo, hi = side_minima(profile)
    return [lo + int(np.argmax(profile[lo:hi + 1]))]


def side_minima(profile):
    """Index of the minimum of the profile on each side of the center (excluding the end ROIs)."""
    n = len(profile)
    left = int(np.argmin(profile[1:n // 2])) + 1
    right = int(np.argmin(profile[n // 2:n - 1])) + n // 2
    return left, right


def loess(pos, y, span):
    from statsmodels.nonparametric.smoothers_lowess import lowess
    return lowess(y, pos, frac=span, it=0, return_sorted=False)


def half_max_width(pos, profile, center_idx, peak, base):
    """Full width of the central peak at half its height ``peak`` above ``base``.

    Walks out from ``center_idx`` on each side to the first ROI at or below the half level and
    interpolates linearly; NaN when the profile does not fall to half on a side.
    """
    half = base + (peak - base) / 2
    i = center_idx
    while i > 0 and profile[i] > half:
        i -= 1
    j = center_idx
    while j < len(profile) - 1 and profile[j] > half:
        j += 1
    if profile[i] > half or profile[j] > half or i == center_idx or j == center_idx:
        return np.nan

    def cross(a, b):
        return pos[a] + (half - profile[a]) * (pos[b] - pos[a]) / (profile[b] - profile[a])
    return cross(j - 1, j) - cross(i + 1, i)


# ---------------------------------------------------------------- readings of the claims file

LAYOUTS = ("r2", "r1-dA", "r1-dB")
BACKGROUNDS = ("b1", "b2-dark", "b2-min")
VARIANT_BACKGROUNDS = ("b2-fp",)   # not a reading of the claims file: the footprints hold cells
CENTERS = ("c1", "c2")
PERIPHERIES = ("e1", "e2-neg", "e2-pos")
NORMALIZATIONS = ("n1", "n2")
TROUGHS = ("t1", "t2-neg", "t2-pos")
SMOOTHING = ("none", "loess-0.25", "loess-0.5")


def dish_matrix(dishes, layout, background):
    """Per-dish ROI values (dishes x ROIs) and positions for one layout and background reading.

    ``dishes`` is a list of dicts with ``profiles`` (from ``dish_profiles``), ``dark``,
    ``region_min`` and ``footprint``. b1: raw counts; b2-dark: minus ``dark_level``; b2-min: minus
    the darkest pixel of the full-resolution region around the array; b2-fp (variant): minus the
    footprint median.
    """
    pos = dishes[0]["profiles"][layout]["pos_mm"]
    P = np.array([d["profiles"][layout]["values"] for d in dishes], float)
    key = {"b1": None, "b2-dark": "dark", "b2-min": "region_min", "b2-fp": "footprint"}[background]
    if key is not None:
        P = P - np.array([d[key] for d in dishes], float)[:, None]
    return pos, P


def periphery(P, reading):
    """Most peripheral ROI value(s), per row: e1 mean of both ends, e2 one end."""
    P = np.atleast_2d(P)
    if reading == "e1":
        return (P[:, 0] + P[:, -1]) / 2
    return P[:, 0] if reading == "e2-neg" else P[:, -1]


def center_value(P, idx):
    return np.atleast_2d(P)[:, idx].mean(axis=1)


def trough_value(P, minima, reading):
    P = np.atleast_2d(P)
    if reading == "t1":
        return (P[:, minima[0]] + P[:, minima[1]]) / 2
    return P[:, minima[0]] if reading == "t2-neg" else P[:, minima[1]]


def mean_profile(P, per, norm):
    """The treatment profile a normalized measure is read from.

    n1: each dish normalized to its own periphery, then averaged; n2: the mean a.u. profile,
    normalized to its periphery. Both in percent of the most peripheral ROI.
    """
    if norm == "n1":
        return (P / periphery(P, per)[:, None] * 100).mean(axis=0)
    m = P.mean(axis=0)
    return m / periphery(m, per)[0] * 100
