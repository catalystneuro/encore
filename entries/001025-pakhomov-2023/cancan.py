"""Loading and ROI profiles for dandiset 001025 (Pakhomov et al. 2023, NG-CANCAN focusing).

The dandiset holds one stitched YO-PRO-1 (YP) fluorescence image per dish, taken 10 min after
nsEP exposure (paper, Section 2.4). The paper measured fluorescence in ROIs placed along the
diagonals of the quadrupole electrode array; the dandiset holds no ROIs, electrode positions or
pixel size, so this module finds the electrodes in each image and places the ROIs.

Where each parameter comes from:

- Span of the ROIs, +/- 1.65 mm (small array) and +/- 3.65 mm (large array) from the geometrical
  centre of the array, and 92 or 224 ROIs: paper, Section 2.4 ("The measurements were performed
  in 92 or 224 regions of interest (ROI), placed along one or both diagonals, and covering a
  distance of +/- 1.65 mm or +/- 3.65 mm from the geometrical center for the small and large
  arrays, respectively").
- ROI count over both diagonals or per diagonal (`N_ROI`), centre ROI (`center_value`),
  normalisation to the most peripheral ROI (`peripheral_value`), raw ROI means or a LOESS fit
  with span 0.75 (`loess`): readings named in the claims file's opening comment.
- ROIs are contiguous along the diagonal (claims file, opening comment, a standard choice) and
  square, as wide across the diagonal as along it: an assumption, the paper gives no ROI width;
  it changes only how many pixels are averaged.
- Pixel size: not in the files. Main reading, 0.65 um per pixel, from the camera and objective
  the files name (Hamamatsu ORCA-Flash4.0, 6.5 um pixels, behind a 10x objective; an
  assumption that the stitched image is not binned). It is checked against the needles: the
  radius of each needle's dark footprint (`footprint_radius`) is compared with the 0.75 mm
  radius of the 1.5 mm needles (paper, Section 2.3, "blunt, hollow, stainless-steel needles
  1.5-mm in diameter"). An earlier variant, the scale at which the mean centre-to-centre
  diagonal of the large array is 8.4 mm (paper, Section 3.5), is no longer run: with it the
  needle edge lies at 3.45 mm (large array) and 1.55 mm (small array) from the centre, inside
  the paper's ROI spans of 3.65 and 1.65 mm, so the end ROIs would lie on the needles.
- Exclusion zone: "Areas immediately adjacent to the electrodes (<5% of the diagonal length)
  were excluded" (paper, Section 2.4). On the camera scale the paper's spans end 0.12 mm (small
  array) and 0.22 mm (large array) from the needle edge, inside that zone. The span is kept as
  the paper states it; `inner_values` gives a variant that drops the end ROIs lying in the zone.
- Packet: the session descriptions name the CANCAN protocol with 12.5% decrements but not the
  packet; Packet 2 is assumed, as in Fig. 7 and the dandiset's title.
- Electrode detection (a dark disk of radius 52 px, small array, or 40 px, large array, at a
  downsampling of 16, four disks on the corners of a square): a choice made here to place the ROIs, checked on overlays in the
  notebook. The geometrical centre is the mean of the four electrode centres. The disk radii
  are detection templates, not the needle radius.
- LOESS: local-linear (statsmodels lowess) with no robustness iterations (`it=0`), fitted over
  the whole span of one diagonal with the standard span 0.75. A span this wide flattens a narrow
  centre peak, so the LOESS readings sit below the raw centre ROI; they are readings, not the
  main one.
- Mean of the non-zero pixels: the stitched images are zero outside the imaged tiles.
"""

from __future__ import annotations

import re
import zlib
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
import requests
from scipy import ndimage as ndi
from scipy.signal import fftconvolve

DANDISET = "001025"
VERSION = "0.240605.1826"
API = "https://api.dandiarchive.org/api"

F = 4  # block size of the stored image (2.6 um blocks at 0.65 um per pixel); sums are exact
FD = 16  # block size for electrode detection
DISK_R = {"small": 52, "large": 40}  # electrode footprint radius at FD, in pixels (read off the images)
HALF_DIAG = {"small": range(200, 280, 4), "large": range(400, 480, 4)}  # search ranges, FD pixels
CAMERA_UM_PER_PX = 6.5 / 10  # ORCA-Flash4.0 pixel behind a 10x objective
SPAN_MM = {"small": 1.65, "large": 3.65}  # paper, Section 2.4
N_ROI = {"small": 92, "large": 224}  # paper, Section 2.4
LARGE_DIAGONAL_MM = 8.4  # paper, Section 3.5
NEEDLE_RADIUS_MM = 0.75  # paper, Section 2.3, needles 1.5 mm in diameter
EXCLUDE_FRAC = 0.05  # paper, Section 2.4, areas within 5% of the diagonal length excluded


def list_assets():
    """Assets of the pinned version with the conditions parsed from each session description."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r["next"]
    return sorted(out, key=lambda a: a["path"])


def s3_url(asset_id):
    return requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60).url


def parse_description(desc):
    """First-pulse voltage (kV) and packets per electrode, from the session description."""
    kv = float(re.search(r"applied at ([\d.]+)kV", desc).group(1))
    reps = int(re.search(r"repeated (\d+) times", desc).group(1))
    return kv, reps


def read_image(url, channel=0, workers=8):
    """Stream one channel and return per-block sums and counts of non-zero pixels at block F.

    The compressed chunks are located with h5py and fetched with HTTP range requests in
    parallel, then inflated here; the data are never written to disk.
    """
    f = h5py.File(remfile.File(url), "r")
    d = f["acquisition/ScanningImaging/data"]
    cy, cx = d.chunks[1], d.chunks[2]
    plist = d.id.get_create_plist()
    filters = [plist.get_filter(i)[0] for i in range(plist.get_nfilters())]
    assert filters == [h5py.h5z.FILTER_DEFLATE], filters
    infos = []
    d.id.chunk_iter(lambda si: infos.append((si.chunk_offset, si.byte_offset, si.size)))
    infos = sorted([i for i in infos if i[0][0] == channel], key=lambda i: i[1])
    groups, cur = [], []
    for i in infos:
        if cur and (i[1] + i[2] - cur[0][1] > 16e6 or i[1] - (cur[-1][1] + cur[-1][2]) > 1e5):
            groups.append(cur)
            cur = []
        cur.append(i)
    groups.append(cur)
    H, W = d.shape[1] // F, d.shape[2] // F
    s = np.zeros((H, W), np.float64)
    n = np.zeros((H, W), np.uint8)
    stats = {"zero_px": 0, "max": 0}

    def fetch(g):
        a, b = g[0][1], g[-1][1] + g[-1][2]
        for attempt in range(6):
            try:
                r = requests.get(url, headers={"Range": f"bytes={a}-{b - 1}"}, timeout=180)
                r.raise_for_status()
                break
            except Exception:
                if attempt == 5:
                    raise
        buf = r.content
        zp, mx = 0, 0
        for off, bo, sz in g:
            arr = np.frombuffer(zlib.decompress(buf[bo - a:bo - a + sz]), np.uint16).reshape(cy, cx)
            y, x = off[1], off[2]
            blk = arr.reshape(cy // F, F, cx // F, F)
            nz = blk > 0
            s[y // F:(y + cy) // F, x // F:(x + cx) // F] = blk.sum(axis=(1, 3), dtype=np.float64)
            n[y // F:(y + cy) // F, x // F:(x + cx) // F] = nz.sum(axis=(1, 3))
            zp += arr.size - int(nz.sum())
            mx = max(mx, int(arr.max()))
        return zp, mx

    with ThreadPoolExecutor(workers) as ex:
        for zp, mx in ex.map(fetch, groups):
            stats["zero_px"] += zp
            stats["max"] = max(stats["max"], mx)
    stats["shape"] = d.shape
    stats["n_chunks"] = len(infos)
    f.close()
    return s, n, stats


def coarse(s, n, k=FD // F):
    """Mean image of non-zero pixels and the zero fraction, at block FD."""
    H, W = s.shape[0] // k, s.shape[1] // k
    ss = s[:H * k, :W * k].reshape(H, k, W, k).sum(axis=(1, 3))
    nn = n[:H * k, :W * k].reshape(H, k, W, k).sum(axis=(1, 3)).astype(float)
    img = np.where(nn > 0, ss / np.maximum(nn, 1), 0)
    zero = 1 - nn / (k * k * F * F)
    return img, zero


def disk_contrast(img, zero, r):
    """(mean in a disk minus mean in a surrounding annulus) / annulus mean; negative on dark disks."""
    valid = (zero < 0.5).astype(float)
    a = np.where(valid > 0, img, 0)
    yy, xx = np.mgrid[-2 * r:2 * r + 1, -2 * r:2 * r + 1]
    rr = np.hypot(yy, xx)
    disk = (rr <= r * 0.8).astype(float)
    ann = ((rr >= r * 1.2) & (rr <= r * 1.8)).astype(float)

    def m(k):
        sm = fftconvolve(a, k, "same")
        nm = fftconvolve(valid, k, "same")
        return sm / np.maximum(nm, 1e-6), nm / k.sum()

    md, nd = m(disk)
    ma, na = m(ann)
    c = (md - ma) / np.maximum(ma, 1)
    c[(nd < 0.98) | (na < 0.95)] = 0
    return c


def fit_square(c, hs, angles=range(20, 71, 3), border=420):
    """Best square of four dark disks: grid search of centre, half-diagonal and angle, then
    each corner refined to the darkest point within 15 px."""
    cm = ndi.minimum_filter(c, size=9)
    H, W = c.shape
    best = (0.0, None)
    for h in hs:
        for th in angles:
            s = np.zeros((H, W))
            for k in range(4):
                a = np.deg2rad(th + 90 * k)
                dx, dy = int(round(h * np.cos(a))), int(round(h * np.sin(a)))
                s += np.roll(np.roll(cm, -dy, 0), -dx, 1)
            s[:border, :] = 0
            s[-border:, :] = 0
            s[:, :border] = 0
            s[:, -border:] = 0
            i = np.unravel_index(np.argmin(s), s.shape)
            if s[i] < best[0]:
                best = (s[i], (i[1], i[0], h, th))
    cx, cy, h, th = best[1]
    pts = []
    for k in range(4):
        a = np.deg2rad(th + 90 * k)
        px, py = cx + h * np.cos(a), cy + h * np.sin(a)
        y0, x0 = max(int(py) - 15, 0), max(int(px) - 15, 0)
        sub = c[y0:max(int(py) + 16, 0), x0:max(int(px) + 16, 0)]
        if sub.size == 0:  # corner outside the image: this size does not fit
            return 0.0, np.array([[px, py] for _ in range(4)])
        j = np.unravel_index(np.argmin(sub), sub.shape)
        pts.append((x0 + j[1], y0 + j[0]))
    return float(best[0]) / 4, np.array(pts, float)


def find_electrodes(img, zero):
    """Fit both array sizes; return the better fit. Electrode centres in FD pixels, in order
    around the square, so that (0, 2) and (1, 3) are the diagonals."""
    fits = {k: fit_square(disk_contrast(img, zero, DISK_R[k]), HALF_DIAG[k]) for k in ("small", "large")}
    size = min(fits, key=lambda k: fits[k][0])
    return size, fits[size][1], {k: v[0] for k, v in fits.items()}


def strip_histograms(s, n, pts_fd, half_len_px, half_width_px, bin_px=1.0):
    """For each diagonal, sums and counts of pixels binned by position along the diagonal (u,
    from the array centre, positive towards the second electrode) and distance across it (|v|).

    Coordinates in stored-block (F) pixels. Returns, per diagonal, arrays (n_u, n_v) of sums and
    counts, and the bin edges.
    """
    pts = pts_fd * (FD / F)
    ctr = pts.mean(0)
    nu = int(np.ceil(half_len_px / bin_px))
    nv = int(np.ceil(half_width_px / bin_px))
    out = []
    for i, j in [(0, 2), (1, 3)]:
        d = pts[j] - pts[i]
        e = d / np.hypot(*d)
        perp = np.array([-e[1], e[0]])
        # bounding box of the strip
        corners = [ctr + a * e * half_len_px + b * perp * half_width_px for a in (-1, 1) for b in (-1, 1)]
        corners = np.array(corners)
        x0, y0 = np.floor(corners.min(0)).astype(int) - 1
        x1, y1 = np.ceil(corners.max(0)).astype(int) + 2
        x0, y0 = max(x0, 0), max(y0, 0)
        yy, xx = np.mgrid[y0:y1, x0:x1]
        # block centres
        px, py = xx + 0.5 - ctr[0], yy + 0.5 - ctr[1]
        u = px * e[0] + py * e[1]
        v = np.abs(px * perp[0] + py * perp[1])
        iu = np.floor((u + half_len_px) / bin_px).astype(int)
        iv = np.floor(v / bin_px).astype(int)
        ok = (iu >= 0) & (iu < 2 * nu) & (iv < nv)
        idx = iu[ok] * nv + iv[ok]
        hs = np.bincount(idx, weights=s[y0:y1, x0:x1][ok], minlength=2 * nu * nv).reshape(2 * nu, nv)
        hn = np.bincount(idx, weights=n[y0:y1, x0:x1][ok].astype(float), minlength=2 * nu * nv).reshape(2 * nu, nv)
        out.append((hs, hn))
    return out, bin_px


def roi_profile(hist, bin_px, span_px, n_roi):
    """Mean of non-zero pixels in n_roi contiguous square ROIs over [-span, +span] along one
    diagonal. hist is (sums, counts) from strip_histograms, centred at its middle bin."""
    hs, hn = hist
    nu2 = hs.shape[0]
    w = 2 * span_px / n_roi
    centers_u = -span_px + w * (np.arange(n_roi) + 0.5)
    u_bins = (np.arange(nu2) + 0.5) * bin_px - nu2 * bin_px / 2
    v_bins = (np.arange(hs.shape[1]) + 0.5) * bin_px
    vals = np.full(n_roi, np.nan)
    vmask = v_bins < w / 2
    for k, cu in enumerate(centers_u):
        um = np.abs(u_bins - cu) < w / 2
        ss = hs[np.ix_(um, vmask)].sum()
        nn = hn[np.ix_(um, vmask)].sum()
        vals[k] = ss / nn if nn > 0 else np.nan
    return centers_u, vals, w


def roi_at(hist, bin_px, u0, w):
    """Mean of non-zero pixels in one square ROI of width w centred at u0 along a diagonal."""
    hs, hn = hist
    nu2 = hs.shape[0]
    u_bins = (np.arange(nu2) + 0.5) * bin_px - nu2 * bin_px / 2
    v_bins = (np.arange(hs.shape[1]) + 0.5) * bin_px
    um = np.abs(u_bins - u0) < w / 2
    vm = v_bins < w / 2
    nn = hn[np.ix_(um, vm)].sum()
    return hs[np.ix_(um, vm)].sum() / nn if nn > 0 else np.nan


def footprint_radius(s, n, pts_fd, rmax=600, step=4, inner=(0, 200), outer=(400, 550)):
    """Radius of each needle's dark footprint, in stored-block (F) pixels.

    Median of the non-zero pixel means in rings of `step` F pixels around each electrode
    centre; the radius is where the smoothed profile last rises through the level half-way
    between the inside (rings at `inner`) and the surround (rings at `outer`), within `outer[0]`.
    The ring windows (0 to 0.52 mm and 1.04 to 1.43 mm at the camera scale) bracket the 0.75 mm
    needle radius; they are a choice made here, used only to check the pixel size.
    """
    fine = np.where(n > 0, s / np.maximum(n, 1), np.nan)
    out = []
    for q in pts_fd * (FD / F):
        x0, y0 = int(q[0]), int(q[1])
        ya, xa = max(y0 - rmax, 0), max(x0 - rmax, 0)
        sub = fine[ya:y0 + rmax, xa:x0 + rmax]
        yy, xx = np.mgrid[ya:ya + sub.shape[0], xa:xa + sub.shape[1]]
        rr = np.hypot(yy + 0.5 - q[1], xx + 0.5 - q[0])
        edges = np.arange(0, rmax + step, step)
        idx = np.digitize(rr, edges) - 1
        ok = np.isfinite(sub) & (idx < len(edges) - 1)
        prof = np.array([np.median(sub[ok & (idx == k)]) if (ok & (idx == k)).any() else np.nan
                         for k in range(len(edges) - 1)])
        rc = edges[:-1] + step / 2
        lo = np.nanmedian(prof[(rc >= inner[0]) & (rc < inner[1])])
        hi = np.nanmedian(prof[(rc >= outer[0]) & (rc < outer[1])])
        sm = np.convolve(np.nan_to_num(prof, nan=lo), np.ones(5) / 5, "same")
        k = np.where((sm[:-1] < (lo + hi) / 2) & (sm[1:] >= (lo + hi) / 2) & (rc[1:] < outer[0]))[0]
        out.append(dict(r_px=float(rc[k[-1]] + step / 2) if len(k) else np.nan, inside=float(lo), outside=float(hi)))
    return out


def loess(x, y, frac=0.75):
    """LOESS fit (statsmodels lowess, span 0.75: a standard choice, the paper gives none)."""
    from statsmodels.nonparametric.smoothers_lowess import lowess

    ok = np.isfinite(y)
    fit = lowess(y[ok], x[ok], frac=frac, it=0, return_sorted=False)
    out = np.full_like(y, np.nan)
    out[ok] = fit
    return out


# Readings of the ROI layout (claims file, opening comment, and the pixel size above).
SCALES = ("camera",)  # the 8.4 mm scale is not run (module docstring)
COUNTS = ("both", "per")  # 92/224 ROIs over both diagonals, or per diagonal
DIAGONALS = ("both", "d1", "d2")  # both averaged, or one diagonal alone (electrodes unlabelled)
CENTERS = ("a", "b")  # a: one ROI centred on the array centre; b: mean of the two grid ROIs beside it
SOURCES = ("raw", "loess")


def diagonal_measures(hist, bin_px, span_px, n_per_diag):
    """Raw and LOESS values along one diagonal: the ROI grid, the centre ROI under readings (a)
    and (b), the two half-way ROIs and the two end (most peripheral) ROIs."""
    u, raw, w = roi_profile(hist, bin_px, span_px, n_per_diag)
    fit = loess(u, raw)
    u_half = (span_px - w / 2) / 2  # half-way from the centre to the most peripheral ROI's centre
    mid = n_per_diag // 2
    out = {"u": u, "w": w}
    out["raw"] = dict(
        profile=raw,
        center_a=roi_at(hist, bin_px, 0.0, w),
        center_b=np.nanmean(raw[mid - 1:mid + 1]) if n_per_diag % 2 == 0 else raw[mid],
        half=np.array([roi_at(hist, bin_px, -u_half, w), roi_at(hist, bin_px, u_half, w)]),
        ends=np.array([raw[0], raw[-1]]),
    )
    fc = float(np.interp(0.0, u, fit))
    out["loess"] = dict(
        profile=fit,
        center_a=fc,
        center_b=fc,
        half=np.array([np.interp(-u_half, u, fit), np.interp(u_half, u, fit)]),
        ends=np.array([fit[0], fit[-1]]),
    )
    return out


def summarize(dm, diagonals, center, source):
    """Centre, half-way and peripheral values of one dish under one reading, raw (a.u.) and
    normalised to the most peripheral ROI: norm 'a' divides by the mean of the end ROIs; norm
    'b' divides each half-diagonal by its own end ROI and averages the halves."""
    ds = {"both": [0, 1], "d1": [0], "d2": [1]}[diagonals]
    c = np.array([dm[i][source]["center_" + center] for i in ds])
    h = np.concatenate([dm[i][source]["half"] for i in ds])
    e = np.concatenate([dm[i][source]["ends"] for i in ds])
    cen = c.mean()
    return dict(
        center=cen,
        half=h.mean(),
        periph=e.mean(),
        nc_a=100 * cen / e.mean(),
        nh_a=100 * h.mean() / e.mean(),
        nc_b=100 * np.mean([c[k // 2] / e[k] for k in range(len(e))]),
        nh_b=100 * np.mean(h / e),
    )


def inner_values(hists, dm, half_diag_px, um_per_px):
    """Variant that respects the paper's exclusion zone (Section 2.4): on each diagonal, drop the
    end ROIs whose outer edge lies closer to the needle edge than 5% of the diagonal, take the
    outermost remaining ROIs as the most peripheral, and the half-way ROIs at half their
    distance from the centre. hists: strip_histograms of the two diagonals (bin of 1 F pixel);
    dm: their diagonal_measures; half_diag_px: half of each centre-to-centre diagonal, in F
    pixels. Raw ROI means, centre reading (a), both diagonals averaged, normalisation (a).
    Returns the values and the number of ROIs dropped at each end of each diagonal."""
    c, h, e, drop = [], [], [], []
    for hist, d, hd in zip(hists, dm, half_diag_px):
        u, w, raw = d["u"], d["w"], d["raw"]["profile"]
        limit = hd - NEEDLE_RADIUS_MM * 1000 / um_per_px / F - EXCLUDE_FRAC * 2 * hd
        k = int(np.argmax(np.abs(u) + w / 2 <= limit))  # first kept ROI; the grid is symmetric
        drop.append(k)
        e += [raw[k], raw[len(raw) - 1 - k]]
        uh = abs(u[k]) / 2
        c.append(d["raw"]["center_a"])
        h += [roi_at(hist, 1.0, -uh, w), roi_at(hist, 1.0, uh, w)]
    cen, half, per = np.mean(c), np.mean(h), np.mean(e)
    return dict(center=cen, half=half, periph=per, nc_a=100 * cen / per, nh_a=100 * half / per, dropped=drop)
