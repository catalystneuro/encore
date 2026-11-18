"""Loading and measures for the CANCAN monolayer images of Pakhomov et al. (2023).

Pakhomov, Gudvangen, Mangalanathan, Kondratiev, Redondo & Semenov (2023), "Next generation
CANCAN focusing for remote stimulation by nanosecond electric pulses", Bioelectrochemistry 152,
108437, doi:10.1016/j.bioelechem.2023.108437.

Each NWB file of dandisets 000686, 000875, 001025, 001027 and 001028 holds one dish: one
stitched 10x image of YO-PRO-1 fluorescence (uint16, 22323 or 20480 pixels square), and in some
files a second channel. The files hold no ROI, no pixel size and no electrode positions, so the
measurement of Methods 2.4 is rebuilt here from the images.

Files are streamed from the archive at the pinned versions: each is read with HTTP range
requests into memory (never to disk), decoded with h5py and reduced at once to block means of
`K` x `K` pixels. Only the reduced images are kept.

Where the parameters come from:

- Pixel size, `UM_PER_PX_FULL` = 0.65 um. An assumption: the files give none (the
  ImageSeries `resolution` is -1). Methods 2.4 names a 10x objective and an ORCA-Flash4 camera,
  whose 6.5 um pixels give 0.65 um at 10x. The notebook checks it against the paper's geometry:
  the needles are 1.5 mm across (Methods 2.3) and the large array has an 8.4-mm diagonal
  (Results 3.5).
- Electrode positions are found in the images as the four dark footprints ("dark circles
  indicate electrode footprints", the files' own image description) by a disc-against-ring
  contrast filter and a fit of a square. For electrodes lifted above the monolayer (001028,
  Results 3.5) the footprints are absent from the YO-PRO-1 channel; there the two marks the
  needles left in the second channel are fitted with circles and the square is completed from
  them. Both are this attempt's methods (the paper measured in MetaMorph and says nothing of how
  the centre was found); the notebook checks them against each other.
- ROI layout, from Methods 2.4: "92 or 224 regions of interest (ROI), placed along one or both
  diagonals, and covering a distance of +/- 1.65 mm or +/- 3.65 mm from the geometrical center for
  the small and large arrays". The claims file's readings O1 (a) the count is per diagonal,
  (b) it is split over the two; ROI width (w1) one spacing, (w2) three spacings, a standard
  choice and a check of sensitivity.
- Background, reading O6 (b) of the claims file: the 1st percentile of the reduced image inside
  the electrode square, outside the footprints, a standard choice for a cell-free level.
- The other readings (O2 to O9) are the claims file's and are applied with `group_values`.
  `SUPPORTED` names the readings the paper or the claims file gives a basis for.
"""

from __future__ import annotations

import concurrent.futures as cf
import hashlib
import io
import itertools
import re

import h5py
import numpy as np
import requests
from scipy import ndimage as ndi
from scipy.optimize import least_squares
from scipy.signal import fftconvolve

API = "https://api.dandiarchive.org/api"
VERSIONS = {
    "000686": "0.240515.1909",
    "000875": "0.240515.1925",
    "001025": "0.240605.1826",
    "001027": "0.240605.1859",
    "001028": "0.240605.1954",
}

UM_PER_PX_FULL = 0.65     # assumption, see the module docstring
K = 8                     # block size of the reduced images
UM_PER_PX = UM_PER_PX_FULL * K
HALF_RANGE_MM = {"small": 1.65, "large": 3.65}   # Methods 2.4
ROI_COUNT = {"small": 92, "large": 224}          # Methods 2.4
NEEDLE_MM = 1.5                                  # Methods 2.3


# ---------------------------------------------------------------- reading the archive

def list_assets(dandiset):
    """Assets of the pinned version, with their S3 URL and size."""
    v = VERSIONS[dandiset]
    url = f"{API}/dandisets/{dandiset}/versions/{v}/assets/?page_size=200"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r.get("next")
    return sorted(out, key=lambda a: a["path"])


def _asset_meta(dandiset, asset_id):
    v = VERSIONS[dandiset]
    return requests.get(f"{API}/dandisets/{dandiset}/versions/{v}/assets/{asset_id}/",
                        timeout=60).json()


def _fetch(url, size, block=32_000_000, threads=8):
    def get(a):
        b = min(a + block, size) - 1
        for _ in range(6):
            r = requests.get(url, headers={"Range": f"bytes={a}-{b}"}, timeout=180)
            if r.status_code == 206 and len(r.content) == b - a + 1:
                return r.content
        raise RuntimeError(f"range {a}-{b} of {url} could not be read")
    with cf.ThreadPoolExecutor(threads) as ex:
        return b"".join(ex.map(get, range(0, size, block)))


def _text(f, path):
    if path not in f:
        return None
    v = f[path][()]
    if isinstance(v, bytes):
        return v.decode()
    if isinstance(v, np.ndarray):
        return [x.decode() if isinstance(x, bytes) else x for x in v.tolist()]
    return v


def load_image(dandiset, asset):
    """Stream one NWB file and return its metadata and reduced image frames."""
    meta = _asset_meta(dandiset, asset["asset_id"])
    url = [u for u in meta["contentUrl"] if "s3" in u][0]
    buf = _fetch(url, meta["contentSize"])
    with h5py.File(io.BytesIO(buf), "r") as f:
        series = list(f["acquisition"].keys())
        d = f[f"acquisition/{series[0]}/data"]
        rec = dict(
            dandiset=dandiset, asset_id=asset["asset_id"], path=asset["path"],
            subject_id=_text(f, "general/subject/subject_id"),
            session_id=_text(f, "general/session_id"),
            description=_text(f, "session_description"),
            start=_text(f, "session_start_time"),
            species=_text(f, "general/subject/species"),
            strain=_text(f, "general/subject/strain"),
            image_description=f[f"acquisition/{series[0]}"].attrs.get("description"),
            series=series, shape=d.shape, dtype=str(d.dtype),
            resolution=float(d.attrs.get("resolution", np.nan)),
            unit=d.attrs.get("unit"),
            rate=float(f[f"acquisition/{series[0]}/starting_time"].attrs.get("rate", np.nan)),
        )
        frames, hashes, stats = [], [], []
        for i in range(d.shape[0]):
            im = d[i]
            hashes.append(hashlib.sha1(im.tobytes()).hexdigest())
            stats.append(dict(min=int(im.min()), max=int(im.max()),
                              saturated=float((im >= np.iinfo(im.dtype).max).mean()),
                              zero=float((im == 0).mean())))
            h, w = im.shape[0] // K * K, im.shape[1] // K * K
            frames.append(im[:h, :w].reshape(h // K, K, w // K, K).mean((1, 3), dtype=np.float32))
            del im
    del buf
    rec.update(frames=frames, pixel_sha1=hashes, stats=stats)
    return rec


def load_dandiset(dandiset, threads=2):
    """All files of a dandiset, two at a time (each needs about 3 GB while it is decoded)."""
    assets = list_assets(dandiset)
    with cf.ThreadPoolExecutor(threads) as ex:
        return list(ex.map(lambda a: load_image(dandiset, a), assets))


# ---------------------------------------------------------------- conditions

def condition(rec):
    """Treatment of a dish, parsed from its subject id or session description."""
    ds, sid, desc = rec["dandiset"], rec["subject_id"] or "", rec["description"] or ""
    c = dict(voltage_kv=None, protocol=None, packet=2, gap_mm=0.0, array=None)
    m = re.search(r"(\d+)[,.](\d)\s*kV", sid + " " + desc)
    if m:
        c["voltage_kv"] = float(f"{m.group(1)}.{m.group(2)}")
    if ds == "000686":
        c["array"] = "large"
        rot = "10cycles" in sid
        ctrl = "Ctrl" in sid
        c["protocol"] = ("1Tx40" if ctrl else "1Px40") if rot else ("40T" if ctrl else "40P")
    elif ds == "000875":
        c["array"] = "small"
        c["protocol"] = re.match(r"(\d+)p_x4", sid).group(1) + "Px4"
    else:
        n = int(re.search(r"repeated (\d+) times", desc).group(1))
        c["protocol"] = f"{n}Px4"
        c["array"] = "small" if n == 1 else "large"
        m = re.search(r"Protocol(\d)", desc)
        if m:
            c["packet"] = int(m.group(1))
        m = re.search(r"lifted by (\d+)\s*mm", desc)
        if m:
            c["gap_mm"] = float(m.group(1))
    return c


# ---------------------------------------------------------------- electrode positions

def _disk(r):
    y, x = np.mgrid[-r:r + 1, -r:r + 1]
    return (x * x + y * y <= r * r).astype(float)


def _ring(r1, r2):
    y, x = np.mgrid[-r2:r2 + 1, -r2:r2 + 1]
    d = x * x + y * y
    return ((d > r1 * r1) & (d <= r2 * r2)).astype(float)


def _reduce(a, k):
    h, w = a.shape[0] // k * k, a.shape[1] // k * k
    return a[:h, :w].reshape(h // k, k, w // k, k).mean((1, 3))


def _score_map(s, valid, r):
    """Contrast of a ring (1.15 to 1.6 r) over a disc (r), on log intensity."""
    D, R = _disk(r), _ring(r * 1.15, r * 1.6)
    nd = fftconvolve(valid, D, "same")
    nr = fftconvolve(valid, R, "same")
    md = fftconvolve(s, D, "same") / np.maximum(nd, 1)
    mr = fftconvolve(s, R, "same") / np.maximum(nr, 1)
    ok = (nd > 0.98 * D.sum()) & (nr > 0.9 * R.sum())
    return np.where(ok, mr - md, -9.0)


def _peaks(sc, n, sep):
    sc = sc.copy()
    y, x = np.ogrid[:sc.shape[0], :sc.shape[1]]
    out = []
    for _ in range(n):
        i = np.unravel_index(np.argmax(sc), sc.shape)
        out.append((float(i[1]), float(i[0]), float(sc[i])))
        sc[(x - i[1]) ** 2 + (y - i[0]) ** 2 < sep ** 2] = -9.0
    return out


def _square_error(P):
    c = P.mean(0)
    P = P[np.argsort(np.arctan2(P[:, 1] - c[1], P[:, 0] - c[0]))]
    sides = np.linalg.norm(P - np.roll(P, -1, 0), axis=1)
    diags = np.array([np.linalg.norm(P[0] - P[2]), np.linalg.norm(P[1] - P[3])])
    ms = sides.mean()
    err = sides.std() / ms + abs(diags.mean() / ms - np.sqrt(2)) + abs(diags[0] - diags[1]) / ms
    return P, ms, err


# side of the electrode square, centre to centre, in reduced pixels (wide bounds)
SIDE_RANGE = {"small": (500, 950), "large": (1100, 1600)}


def find_footprints(frame, array, k=4):
    """Four footprint centres (reduced pixels), by the best square of dark discs.

    Works at 1/k of the reduced image. Four of nine candidate discs are fitted to a square
    whose side lies in SIDE_RANGE; when no four fit well (error over 0.08), three discs at the
    corners of a right isosceles triangle are completed to a square.
    """
    s = _reduce(frame, k)
    valid = (s > 0).astype(float)
    s = np.log1p(s)
    lo, hi = SIDE_RANGE[array][0] / k, SIDE_RANGE[array][1] / k
    best = None
    for r in range(22, 38, 2):
        sc = _score_map(s, valid, r)
        pk = _peaks(sc, 9, 2.5 * r)
        for q in itertools.combinations(range(len(pk)), 4):
            P = np.array([pk[i][:2] for i in q])
            P, ms, err = _square_error(P)
            if not lo < ms < hi:
                continue
            val = np.mean([pk[i][2] for i in q]) - 5 * err
            if best is None or val > best["val"]:
                best = dict(val=val, P=P, err=err, score=np.mean([pk[i][2] for i in q]), r=r,
                            method="four footprints", peaks=pk)
    if best is not None and best["err"] > 0.08:
        pk = best["peaks"]
        b3 = None
        for q in itertools.permutations(range(len(pk)), 3):
            a, b, c = (np.array(pk[i][:2]) for i in q)
            u, v = a - b, c - b
            la, lc = np.linalg.norm(u), np.linalg.norm(v)
            if not (lo < la < hi and lo < lc < hi):
                continue
            err = abs(la - lc) / la + abs(np.dot(u, v)) / (la * lc)
            val = np.mean([pk[i][2] for i in q]) - 5 * err
            if b3 is None or val > b3["val"]:
                P = np.array([a, b, c, a + c - b])
                P, ms, e4 = _square_error(P)
                b3 = dict(val=val, P=P, err=err, score=np.mean([pk[i][2] for i in q]),
                          r=best["r"], method="three footprints, fourth completed")
        if b3 is not None and b3["err"] < best["err"]:
            best = b3
    best["P"] = best["P"] * k + k / 2
    best["r"] = best["r"] * k
    best.pop("peaks", None)
    return best


def find_marks(frame1, side, radius=128.0, k=4):
    """Electrode square from the needle marks of the second channel (lifted electrodes).

    The marks are dark arcs at the two upper needles. Each is fitted with a circle of the
    footprint radius; the square is completed downwards with the side found between the two
    marks (or `side` when the two are not one side apart).
    """
    s = _reduce(frame1, k)
    ms = s > 0
    bg = ndi.median_filter(s, size=41)
    ratio = np.where(ms & (bg > 0), s / np.maximum(bg, 1), 1)
    dark = (ratio < 0.45) & ndi.binary_erosion(ms, iterations=8)
    dark = ndi.binary_opening(dark, iterations=1)
    lab, n = ndi.label(dark)
    arcs = []
    for i in range(1, n + 1):
        yy, xx = np.nonzero(lab == i)
        if len(yy) < 40 or max(np.ptp(xx), np.ptp(yy)) < radius / k * 0.6:
            continue
        w, v = np.linalg.eigh(np.cov(xx, yy))
        fits = []
        for sgn in (-1, 1):
            c0 = np.array([xx.mean(), yy.mean()]) + sgn * v[:, 0] * radius / k * 0.7
            sol = least_squares(lambda c: np.hypot(xx - c[0], yy - c[1]) - radius / k, c0)
            fits.append((np.sqrt(np.mean(sol.fun ** 2)), sol.x))
        rms, c = min(fits, key=lambda t: t[0])
        arcs.append((c * k + k / 2, len(yy)))
    if len(arcs) < 2:
        return None
    arcs = sorted(arcs, key=lambda a: -a[1])[:2]
    p1, p2 = sorted([a[0] for a in arcs], key=lambda p: p[0])
    v = p2 - p1
    L = np.linalg.norm(v)
    perp = np.array([-v[1], v[0]]) / L
    if perp[1] < 0:
        perp = -perp
    sd = L if 0.85 * side < L < 1.15 * side else side
    P = np.array([p1, p2, p2 + perp * sd, p1 + perp * sd])
    P, msd, err = _square_error(P)
    return dict(P=P, err=err, score=np.nan, r=radius, method="two needle marks, second channel",
                mark_distance=L)


def corner_names(P):
    """Name each electrode by its image corner: TL, TR, BR, BL (image y points down)."""
    c = P.mean(0)
    ang = np.degrees(np.arctan2(P[:, 1] - c[1], P[:, 0] - c[0]))
    target = {"TL": -135, "TR": -45, "BR": 45, "BL": 135}
    out = {}
    for name, t in target.items():
        dif = np.abs((ang - t + 180) % 360 - 180)
        out[name] = P[int(np.argmin(dif))]
    return out


OPPOSITE = {"TL": "BR", "BR": "TL", "TR": "BL", "BL": "TR"}


# ---------------------------------------------------------------- ROI measures

def roi_samples(frame, c, u, d, w, step):
    """Pixel values of a square ROI of side w (reduced pixels) centred at c + d u, along u."""
    n = max(int(np.ceil(w / step)), 1)
    g = (np.arange(n) + 0.5) / n * w - w / 2
    a, b = np.meshgrid(g, g, indexing="ij")
    vperp = np.array([-u[1], u[0]])
    xy = c[None, None, :] + (d + a)[..., None] * u + b[..., None] * vperp
    return ndi.map_coordinates(frame, [xy[..., 1].ravel(), xy[..., 0].ravel()], order=1,
                               mode="constant", cval=0.0)


def _roi_means(frame, c, u, dists, w, step):
    """Mean of square ROIs; an ROI with more than 20% of its area outside the image is dropped."""
    out = np.empty(len(dists))
    for i, d in enumerate(dists):
        vals = roi_samples(frame, c, u, d, w, step)
        out[i] = np.nan if (vals <= 0).mean() > 0.2 else vals[vals > 0].mean()
    return out


def background(frame, geom):
    """O6 (b): 1st percentile inside the electrode square, outside the footprints."""
    P = geom["P"]
    yy, xx = np.mgrid[:frame.shape[0], :frame.shape[1]]
    from matplotlib.path import Path
    inside = Path(P).contains_points(np.c_[xx.ravel(), yy.ravel()]).reshape(frame.shape)
    for p in P:
        inside &= (xx - p[0]) ** 2 + (yy - p[1]) ** 2 > (1.2 * geom["r"]) ** 2
    v = frame[inside & (frame > 0)]
    return float(np.percentile(v, 1))


def dish_profiles(frame, geom, array):
    """ROI values along the four half-diagonals, for each layout (O1, width) and O6.

    Returns {(o1, w, o6): dict(d=distances in mm, halves={corner: values}, centre_a)}.
    The ROIs of a diagonal are centred at -R + (i + 1/2) s, i = 0 .. n - 1 (s = 2R / n), so each
    half holds n / 2 ROIs at (j + 1/2) s from the centre; `centre_a` is one more ROI centred on
    the centre (O3 a). O3 (b), the mean of the ROIs on either side of the centre, is taken from
    the first ROI of the half-diagonals in use (`centre_value`).
    """
    R_mm = HALF_RANGE_MM[array]
    corners = corner_names(geom["P"])
    c = geom["P"].mean(0)
    bg = background(frame, geom)
    out = {}
    for o1, n_diag in (("a", ROI_COUNT[array]), ("b", ROI_COUNT[array] // 2)):
        s_mm = 2 * R_mm / n_diag
        d_mm = (np.arange(n_diag // 2) + 0.5) * s_mm
        for wname, wmul in (("w1", 1), ("w2", 3)):
            w_px = wmul * s_mm * 1000 / UM_PER_PX
            step = min(w_px / 4, 1.0)
            halves = {}
            for name, p in corners.items():
                u = (p - c) / np.linalg.norm(p - c)
                halves[name] = _roi_means(frame, c, u, d_mm * 1000 / UM_PER_PX, w_px, step)
            u0 = (corners["TR"] - c) / np.linalg.norm(corners["TR"] - c)
            ca = _roi_means(frame, c, u0, [0.0], w_px, step)[0]
            for o6, sub in (("a", 0.0), ("b", bg)):
                out[(o1, wname, o6)] = dict(
                    d=d_mm, s=s_mm, halves={k: v - sub for k, v in halves.items()},
                    centre_a=ca - sub, background=bg)
    return out


def geometry_mm(geom):
    """Sizes of the electrode square in mm, from the footprint centres."""
    P = geom["P"]
    side = np.linalg.norm(P - np.roll(P, -1, 0), axis=1).mean() * UM_PER_PX / 1000
    diag = np.mean([np.linalg.norm(P[0] - P[2]), np.linalg.norm(P[1] - P[3])]) * UM_PER_PX / 1000
    return dict(side_mm=side, diag_centres_mm=diag, diag_inner_edges_mm=diag - NEEDLE_MM,
                footprint_diameter_mm=2 * geom["r"] * UM_PER_PX / 1000)


# ---------------------------------------------------------------- readings

def lowess_profile(d, y, frac):
    """O7 (b): LOWESS of a profile against distance (statsmodels), returned at d.

    `d` starts at the centre (0). The fit is made on the profile mirrored about the centre, from
    -R to R, as the paper's figures fit a whole diagonal (Figs. 5 to 9, "LOESS fits"); a fit of
    the half-profile alone would put the edge of the fit, where LOESS is biased, at the centre.
    """
    from statsmodels.nonparametric.smoothers_lowess import lowess
    x, yy = np.r_[-d[:0:-1], d], np.r_[y[:0:-1], y]
    ok = np.isfinite(yy)
    return np.interp(d, *lowess(yy[ok], x[ok], frac=frac, return_sorted=True).T)


def half_set(o2):
    """O2: (a) both diagonals; (d1) the TL-BR diagonal; (d2) the TR-BL diagonal."""
    return {"a": ["TL", "TR", "BR", "BL"], "d1": ["TL", "BR"], "d2": ["TR", "BL"]}[o2]


def centre_value(prof, halves, o3):
    """O3: (a) the ROI on the centre; (b) the mean of the first ROIs of the half-diagonals used."""
    if o3 == "a":
        return prof["centre_a"]
    return float(np.nanmean([prof["halves"][h][0] for h in halves]))


def dish_values(prof, halves, o3, o4):
    """Per-dish centre, end, half-way value and the profile averaged over the chosen halves.

    The profile includes the centre at distance 0 (O3 a or b) followed by the ROIs.
    """
    H = np.array([prof["halves"][h] for h in halves])
    centre = centre_value(prof, halves, o3)
    d = np.r_[0.0, prof["d"]]
    mean_prof = np.r_[centre, np.nanmean(H, 0)]
    ends = H[:, -1]
    # O4 (a): mean of the end ROIs; (b): each half to its own end, then averaged (normalized)
    end = np.nanmean(ends)
    if o4 == "a":
        norm_prof = mean_prof / end * 100
    else:
        norm_prof = np.r_[np.nanmean(centre / ends), np.nanmean(H / ends[:, None], 0)] * 100
    half_i = int(np.argmin(np.abs(d - d[-1] / 2)))
    return dict(d=d, profile=mean_prof, norm=norm_prof, centre=centre, end=end,
                halfway=mean_prof[half_i], halfway_norm=norm_prof[half_i], half_d=d[half_i])


# ---------------------------------------------------------------- the claims file's readings

READINGS = dict(o1=("a", "b"), w=("w1", "w2"), o2=("a", "d1", "d2"), o3=("a", "b"),
                o4=("a", "b"), o5=("a", "b"), o6=("a", "b"), o7=("raw", "lo25", "lo75"))
PRIMARY = dict(o1="a", w="w1", o2="a", o3="a", o4="a", o5="a", o6="a", o7="raw")
# The readings the paper, or the claims file, gives a basis for, used to decide a test when the
# readings disagree (the claims file's rule for readings). O1 and O4 have no basis and are
# always varied.
#   w   w1: the claims file calls square ROIs "a standard choice" and w2 "a check on sensitivity".
#   o2  a: both diagonals averaged, the one layout the paper states (Fig. 5B legend).
#   o3  a: the ROI nearest the geometric centre; Methods 2.4 measures "from the geometrical
#       center".
#   o5  a: the claims file: "tests on normalized values use (a)".
#   o6  a: raw intensity; Methods 2.4 names no background for the monolayers, where Methods 2.2
#       states the subtraction of F0 for the single cells.
#   o7  raw: tests are on per-dish ROI means; the LOESS fits are drawn over group means.
#   O8  paired: comparisons inside the same dishes (centre against trough or periphery) are
#       paired, the standard test for two measures of one dish (set in the notebook).
SUPPORTED = dict(w="w1", o2="a", o3="a", o5="a", o6="a", o7="raw")


def iter_readings(**fixed):
    """Every combination of the readings, with some fixed (a value or a tuple of values)."""
    keys = list(READINGS)
    opts = [fixed[k] if isinstance(fixed.get(k), tuple) else
            ((fixed[k],) if k in fixed else READINGS[k]) for k in keys]
    for combo in itertools.product(*opts):
        yield dict(zip(keys, combo))


def _trough(prof, sides_prof):
    """O9 on a mean profile (index 0 is the centre, the last the most peripheral ROI)."""
    inner = slice(1, len(prof) - 1)
    i_a = 1 + int(np.nanargmin(prof[inner]))
    i_b = [1 + int(np.nanargmin(p[inner])) for p in sides_prof]
    return i_a, i_b


def group_values(dishes, r, halves=None):
    """Values of a group of dishes under one combination of readings `r`.

    `dishes` are records with `prof` from `dish_profiles`. `halves` overrides O2 (Fig. 5A uses
    named half-diagonals). Per-dish values are on ROI means (O7 a); the group values follow O7.
    """
    hs = halves or half_set(r["o2"])
    dv = [dish_values(d["prof"][(r["o1"], r["w"], r["o6"])], hs, r["o3"], r["o4"]) for d in dishes]
    d = dv[0]["d"]
    P = np.array([v["profile"] for v in dv])
    N = np.array([v["norm"] for v in dv])
    mp, mn = np.nanmean(P, 0), np.nanmean(N, 0)
    # per-side mean profiles (for O9 b), centre included
    side = []
    for h in hs:
        sp = []
        for dd in dishes:
            pr = dd["prof"][(r["o1"], r["w"], r["o6"])]
            c = centre_value(pr, hs, r["o3"])
            sp.append(np.r_[c, pr["halves"][h]])
        side.append(np.nanmean(sp, 0))
    if r["o7"] != "raw":
        frac = {"lo25": 0.25, "lo75": 0.75}[r["o7"]]
        mp = lowess_profile(d, mp, frac)
        mn = lowess_profile(d, mn, frac)
        side = [lowess_profile(d, s, frac) for s in side]
    if r["o5"] == "b":
        mn = mp / mp[-1] * 100
    half_i = int(np.argmin(np.abs(d - d[-1] / 2)))
    i_a, i_b = _trough(mp, side)
    trough_a = mp[i_a]
    trough_b = float(np.mean([s[i] for s, i in zip(side, i_b)]))
    per_trough_a = P[:, i_a]
    return dict(
        d=d, profile=mp, norm_profile=mn, centre=mp[0], end=mp[-1], halfway=mp[half_i],
        norm_centre=mn[0], norm_halfway=mn[half_i], half_d=d[half_i],
        trough_a=trough_a, trough_b=trough_b, trough_d=d[i_a],
        centre_over_trough_a=mp[0] / trough_a, centre_over_trough_b=mp[0] / trough_b,
        dish_centre=P[:, 0], dish_end=P[:, -1], dish_halfway=P[:, half_i],
        dish_norm_centre=N[:, 0], dish_norm_halfway=N[:, half_i], dish_trough=per_trough_a,
        dish_profiles=P, dish_norm_profiles=N, n=len(dishes))


def peak_width(d, prof, trough_i=None):
    """Widths of the central peak: (a) full width at half height above the trough; (b) the
    distance between the troughs on either side (2 x the trough distance)."""
    inner = slice(1, len(prof) - 1)
    ti = trough_i if trough_i is not None else 1 + int(np.nanargmin(prof[inner]))
    level = prof[ti] + (prof[0] - prof[ti]) / 2
    below = np.nonzero(prof[:ti + 1] < level)[0]
    if len(below) == 0 or prof[0] <= prof[ti]:
        fwhm = np.nan
    else:
        j = below[0]
        fwhm = 2 * np.interp(level, [prof[j], prof[j - 1]], [d[j], d[j - 1]])
    return fwhm, 2 * d[ti]
