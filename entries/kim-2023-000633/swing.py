"""Loading and measures for the whole-sample YO-PRO-1 images of dandiset 000633.

Kim, Semenov, Kiester, Keppler, Ibey, Bixler, Colunga Biancatelli & Pakhomov (2023), Int. J.
Mol. Sci. 24, 10921, doi:10.3390/ijms241310921.

The dandiset holds two NWB files, one per BPAE cell monolayer of the paper's Figure 4: a train of
five single 600 ns pulses (`Single-pulse_trains`, Figure 4A) and a train of five paired
600 + 600 ns pulses applied to the two base electrodes in alternation (`Paired-pulse_trains`,
Figure 4B,C). Each holds one stitched image, `acquisition/ScaningImaging/data`, of shape
(22323, 22323, 2), uint16: channel 0 is MemBrite (DAPI cube, all cells) and channel 1 is YO-PRO-1
(FITC cube), as the file's description lists them; the notebook checks this. No pixel size is
stored.

Loading. The files are streamed from the archive at the pinned version: the HDF5 chunk index is
read through `remfile`, the bytes holding the chunks are fetched with HTTP range requests into
memory (nothing is written to disk), each gzip chunk is inflated, and the full-resolution image is
reduced by averaging blocks of `BIN` x `BIN` pixels. `BIN` is a standard choice that cannot change
a result: it is far below the 200 um ROI of Methods 4.4.

Where the parameters come from:

- `ROI_UM = 200`: the 200 x 200 um ROIs of Methods 4.4 ("a total of 32 ROIs (200 x 200 um)").
- `NEEDLE_OD_UM = 1500`: the electrodes' outside diameter, Methods 4.2 ("outside and inside
  diameters of 1.5 and 0.5 mm"). The image scale is set from the measured footprint diameter, as
  the claims file says ("The 1.5 mm outside diameter of the needles fixes the image scale if the
  files do not").
- Background: "To account for 'spontaneous' YP uptake, measurements were also performed within
  the hollow electrodes' footprints, where cells were shielded from the electric field" (Methods
  4.4). The background is the median YP over the inner part of the footprints (`FOOTPRINT_CORE`,
  a standard choice that keeps the footprint's edge, where it meets exposed cells, out).
- The readings of the criteria (distances of 100 and 500 um from the footprint edge, half and
  quarter maximum, Spearman correlation, the order of the electrode neighbourhoods) are the claims
  file's.
- `DEBRIS_FACTOR = 10`: objects with MemBrite above ten times the dish median are left out before
  the maximum of the comet claim is taken (an assumption; the notebook shows 5 and 20 too).
  `DEBRIS_DILATE` is a standard choice.
- The field map is computed here (`field_map`), as the paper's Sim4Life map (Methods 4.3) is not
  deposited. Electrodes span the 3.5 mm solution from the glass up, so the field in the plane
  1 um above the glass is the two-dimensional field between three equipotential discs of 1.5 mm
  diameter. It is solved with a finite-difference relaxation on the image grid, with the dish wall
  far away; this substitutes for the paper's solver (an assumption, stated in the notebook).
"""

from __future__ import annotations

import zlib
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
import requests
from dandi.dandiapi import DandiAPIClient

DANDISET_ID = "000633"
DANDISET_VERSION = "0.231013.2226"
DATA_PATH = "acquisition/ScaningImaging/data"
BIN = 16                 # full-resolution pixels per side of a binned pixel (standard choice)
ROI_UM = 200.0           # Methods 4.4
NEEDLE_OD_UM = 1500.0    # Methods 4.2
FOOTPRINT_CORE = 0.7     # fraction of the footprint radius used for the background (standard choice)
BLOCK_BYTES = 32 * 2**20


def assets():
    """Path, session id and S3 URL of each asset at the pinned version."""
    client = DandiAPIClient()
    ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
    out = []
    for a in sorted(ds.get_assets(), key=lambda a: a.path):
        out.append({"path": a.path, "size": a.size,
                    "url": a.get_content_url(follow_redirects=1, strip_query=True)})
    return out


def _fetch(url, start, stop):
    r = requests.get(url, headers={"Range": f"bytes={start}-{stop - 1}"}, timeout=300)
    r.raise_for_status()
    return start, r.content


def load_binned(url, bin_=BIN, workers=16):
    """Stream one file and return its metadata and the binned image, float32 (channel, y, x).

    The image is cut to a multiple of `bin_` (at most bin_ - 1 pixels lost at the far edges).
    """
    f = h5py.File(remfile.File(url), "r")
    d = f[DATA_PATH]
    meta = {
        "session_id": f["general/session_id"][()].decode(),
        "subject_id": f["general/subject/subject_id"][()].decode(),
        "strain": f["general/subject/strain"][()].decode(),
        "session_description": f["session_description"][()].decode(),
        "image_description": d.parent.attrs["description"],
        "shape": d.shape, "dtype": str(d.dtype), "chunks": d.chunks,
        "unit": d.attrs["unit"], "rate": float(d.parent["starting_time"].attrs["rate"]),
    }
    plist = d.id.get_create_plist()
    filters = [plist.get_filter(i)[3] for i in range(plist.get_nfilters())]
    assert filters == [b"deflate"], filters
    infos = []
    d.id.chunk_iter(lambda s: infos.append((s.chunk_offset, s.byte_offset, s.size)))
    shape, chunks = d.shape, d.chunks
    f.close()

    lo = min(i[1] for i in infos)
    hi = max(i[1] + i[2] for i in infos)
    starts = list(range(lo, hi, BLOCK_BYTES))
    buf = bytearray(hi - lo)
    with ThreadPoolExecutor(workers) as ex:
        for start, content in ex.map(lambda s: _fetch(url, s, min(s + BLOCK_BYTES, hi)), starts):
            buf[start - lo:start - lo + len(content)] = content
    meta["bytes_fetched"] = len(buf)

    ny, nx, nc = shape
    full = np.zeros((nc, ny, nx), dtype=np.uint16)
    for (y0, x0, c), off, size in infos:
        raw = zlib.decompress(bytes(buf[off - lo:off - lo + size]))
        block = np.frombuffer(raw, dtype="<u2").reshape(chunks)[:, :, 0]
        h, w = min(chunks[0], ny - y0), min(chunks[1], nx - x0)
        full[c, y0:y0 + h, x0:x0 + w] = block[:h, :w]
    del buf
    my, mx = (ny // bin_) * bin_, (nx // bin_) * bin_
    binned = np.empty((nc, my // bin_, mx // bin_), dtype=np.float32)
    for c in range(nc):
        binned[c] = full[c, :my, :mx].reshape(my // bin_, bin_, mx // bin_, bin_).mean(axis=(1, 3), dtype=np.float64)
    meta["full_stats"] = [{"min": int(full[c].min()), "max": int(full[c].max()),
                           "mean": float(full[c].mean(dtype=np.float64)),
                           "zero_fraction": float((full[c] == 0).mean())} for c in range(nc)]
    del full
    return meta, binned


# ---------------------------------------------------------------- electrode footprints

def _sector_contrast(img, r, n_sectors=8):
    """Contrast of a dark disc of radius 0.8 r against the darkest of the ring sectors at
    1.15 r to 1.5 r. Taking the darkest sector keeps a gradient of uptake from hiding a footprint."""
    from scipy.signal import fftconvolve
    yy, xx = np.mgrid[-2 * r:2 * r + 1, -2 * r:2 * r + 1]
    rr, th = np.hypot(yy, xx), np.arctan2(yy, xx)
    disc = (rr <= 0.8 * r).astype(float)
    inner = fftconvolve(img, disc / disc.sum(), mode="same")
    sectors = []
    for k in range(n_sectors):
        m = ((rr > 1.15 * r) & (rr <= 1.5 * r)
             & (np.floor((th + np.pi) / (2 * np.pi / n_sectors)) % n_sectors == k)).astype(float)
        sectors.append(fftconvolve(img, m / m.sum(), mode="same"))
    outer = np.min(sectors, axis=0)
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(outer > 0, (outer - inner) / outer, -1.0)


def fit_circle(x, y, n_iter=3):
    """Least-squares circle (Kasa), refitted after dropping points whose residual exceeds
    3 median absolute deviations. Returns (xc, yc, r, n_used, residual_sd)."""
    keep = np.ones(len(x), bool)
    for _ in range(n_iter):
        A = np.c_[2 * x[keep], 2 * y[keep], np.ones(keep.sum())]
        b = x[keep] ** 2 + y[keep] ** 2
        (xc, yc, c), *_ = np.linalg.lstsq(A, b, rcond=None)
        r = np.sqrt(c + xc ** 2 + yc ** 2)
        res = np.hypot(x - xc, y - yc) - r
        mad = np.median(np.abs(res[keep] - np.median(res[keep]))) + 1e-9
        keep = np.abs(res) < 3 * 1.4826 * mad + 1.0
    return xc, yc, r, int(keep.sum()), float(np.std(res[keep]))


def find_footprints(yp, n=3, radius_guess=65, search_radius=0.35):
    """The `n` electrode footprints in a binned YP image: dark discs found by `_sector_contrast`
    within `search_radius` of the image width from the centre, then refined by fitting a circle to
    the edge found on 72 rays (the radius where YP first rises halfway from the footprint's
    interior to its surroundings). Returns a list of dicts (x, y, r in binned pixels, the
    coarse contrast, the edge points used)."""
    from scipy.ndimage import median_filter, gaussian_filter
    v = median_filter(yp, 3)
    ny, nx = v.shape
    Y, X = np.mgrid[:ny, :nx]
    score = _sector_contrast(v, radius_guess)
    score[np.hypot(Y - ny / 2, X - nx / 2) > search_radius * nx] = -1
    g = gaussian_filter(yp, 1.5)
    out = []
    sc = score.copy()
    for _ in range(n):
        iy, ix = np.unravel_index(np.argmax(sc), sc.shape)
        contrast = float(sc[iy, ix])
        sc[max(0, iy - 2 * radius_guess):iy + 2 * radius_guess, max(0, ix - 2 * radius_guess):ix + 2 * radius_guess] = -1
        xc, yc = float(ix), float(iy)
        for _ in range(2):
            ex, ey = [], []
            for a in np.linspace(0, 2 * np.pi, 72, endpoint=False):
                rs = np.arange(0, 1.8 * radius_guess, 0.5)
                ys, xs = yc + rs * np.sin(a), xc + rs * np.cos(a)
                ok = (ys >= 0) & (ys < ny - 1) & (xs >= 0) & (xs < nx - 1)
                prof = g[ys[ok].round().astype(int), xs[ok].round().astype(int)]
                rr = rs[ok]
                if len(prof) < len(rs):
                    continue
                inner = np.median(prof[rr < 0.5 * radius_guess])
                outer = np.median(prof[(rr > 1.3 * radius_guess)])
                half = inner + 0.5 * (outer - inner)
                above = np.nonzero((prof > half) & (rr > 0.5 * radius_guess))[0]
                if len(above) and outer > inner:
                    ex.append(xc + rr[above[0]] * np.cos(a))
                    ey.append(yc + rr[above[0]] * np.sin(a))
            xc, yc, r, used, sd = fit_circle(np.array(ex), np.array(ey))
        out.append({"x": xc, "y": yc, "r": r, "contrast": contrast, "edge_points": used,
                    "edge_sd": sd})
    return out


# ---------------------------------------------------------------- field map (Methods 4.3, substituted)

DISH_RADIUS_UM = 17500.0   # Methods 4.3: a 35 mm dish
FIELD_GRID_UM = 40.0       # grid of the finite-difference solve (standard choice)


def solve_potential(electrodes_um, potentials, dish_center_um, h=FIELD_GRID_UM,
                    dish_radius=DISH_RADIUS_UM, electrode_radius=NEEDLE_OD_UM / 2):
    """Potential in the plane of the monolayer for a set of electrode potentials.

    Two-dimensional conduction (uniform depth of a uniform 1.6 S/m solution, electrodes spanning
    it from the glass up, Methods 4.2 and 4.3): Laplace's equation on a square grid of spacing
    `h` um, electrodes as discs of fixed potential, no current through the dish wall. Several
    sets of potentials can be given (a list of lists); they share one factorisation.
    Returns the grid origin (um), `h`, and the potentials, shape (n_sets, ny, nx), NaN outside
    the dish."""
    import scipy.sparse as sp
    from scipy.sparse.linalg import splu
    cx, cy = dish_center_um
    n = int(np.ceil(2 * dish_radius / h)) + 3
    x0, y0 = cx - (n // 2) * h, cy - (n // 2) * h
    ys, xs = y0 + h * np.arange(n), x0 + h * np.arange(n)
    X, Y = np.meshgrid(xs, ys)
    inside = np.hypot(X - cx, Y - cy) <= dish_radius
    elec = np.full(X.shape, -1, int)
    for k, (ex, ey) in enumerate(electrodes_um):
        elec[np.hypot(X - ex, Y - ey) <= electrode_radius] = k
    free = inside & (elec < 0)
    idx = np.full(X.shape, -1, int)
    idx[free] = np.arange(free.sum())
    nf = int(free.sum())
    rows, cols, vals = [], [], []
    diag = np.zeros(nf)
    rhs_links = []  # (row, electrode)
    fy, fx = np.nonzero(free)
    for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ny_, nx_ = fy + dy, fx + dx
        ok = inside[ny_, nx_]
        r = idx[fy[ok], fx[ok]]
        diag[r] += 1
        nb_free = free[ny_[ok], nx_[ok]]
        rows.append(r[nb_free]); cols.append(idx[ny_[ok][nb_free], nx_[ok][nb_free]])
        rhs_links.append((r[~nb_free], elec[ny_[ok][~nb_free], nx_[ok][~nb_free]]))
    rows = np.concatenate(rows); cols = np.concatenate(cols)
    A = sp.csc_matrix((np.r_[diag, -np.ones(len(rows))],
                       (np.r_[np.arange(nf), rows], np.r_[np.arange(nf), cols])), shape=(nf, nf))
    lu = splu(A)
    sets = np.atleast_2d(np.asarray(potentials, float))
    out = np.full((len(sets),) + X.shape, np.nan)
    for s, pots in enumerate(sets):
        b = np.zeros(nf)
        for r, e in rhs_links:
            np.add.at(b, r, pots[e])
        phi = np.full(X.shape, np.nan)
        phi[free] = lu.solve(b)
        for k in range(len(electrodes_um)):
            phi[elec == k] = pots[k]
        out[s] = phi
    return (x0, y0), h, out


def field_from_potential(phi, h):
    """Field vector (Ex, Ey) in V/um per volt applied, as -grad phi, by central differences."""
    gy, gx = np.gradient(phi, h)
    return -gx, -gy


# ---------------------------------------------------------------- geometry and ROI measures

def label_electrodes(fps):
    """Name the three footprints: the apex is the one opposite the shortest side of the
    triangle (Figure 1: the base electrodes are energized, the apex is ground). Returns
    (apex, base_a, base_b) with base_a the base electrode with the larger x."""
    pts = [np.array([f["x"], f["y"]]) for f in fps]
    sides = {k: np.linalg.norm(pts[(k + 1) % 3] - pts[(k + 2) % 3]) for k in range(3)}
    apex = min(sides, key=sides.get)
    bases = sorted([k for k in range(3) if k != apex], key=lambda k: -pts[k][0])
    return fps[apex], fps[bases[0]], fps[bases[1]]


def disc_mask(shape, x, y, r):
    Y, X = np.mgrid[:shape[0], :shape[1]]
    return np.hypot(X - x, Y - y) <= r


def background(yp, fps, r_bin):
    """Median YP inside the cores of the footprints (Methods 4.4: 'spontaneous' uptake measured
    within the hollow electrodes' footprints). One value per footprint and their median."""
    vals = [float(np.median(yp[disc_mask(yp.shape, f["x"], f["y"], FOOTPRINT_CORE * r_bin)])) for f in fps]
    return float(np.median(vals)), vals


def roi_mean(img, x, y, side_bin):
    """Mean of `img` over a square ROI of side `side_bin` (binned pixels) centred at (x, y)."""
    h = side_bin / 2
    y0, y1 = int(round(y - h)), int(round(y + h))
    x0, x1 = int(round(x - h)), int(round(x + h))
    return float(np.nanmean(img[max(y0, 0):y1, max(x0, 0):x1]))


def sample(grid, origin, h, x_um, y_um):
    """Bilinear sample of a field-grid quantity at points given in um."""
    from scipy.ndimage import map_coordinates
    gx = (np.asarray(x_um) - origin[0]) / h
    gy = (np.asarray(y_um) - origin[1]) / h
    return map_coordinates(np.nan_to_num(grid), [np.atleast_1d(gy), np.atleast_1d(gx)], order=1)


def comet_region(smoothed, threshold, apex, bases, um_per_bin, valid):
    """The electroporated region of the comet claim: pixels of `smoothed` above `threshold`,
    inside `valid`, in the connected components that touch the apex footprint (within 2 binned
    pixels of its 750 um edge). Its extent is given in um in the frame of the bisecting line:
    u from the apex centre toward the midpoint of the base electrodes, v across it."""
    from scipy.ndimage import label
    ny, nx = smoothed.shape
    Yg, Xg = np.mgrid[:ny, :nx]
    reg = (smoothed > threshold) & valid
    lab, _ = label(reg)
    d_apex = np.hypot(Xg - apex["x"], Yg - apex["y"]) * um_per_bin
    ring = (d_apex > NEEDLE_OD_UM / 2) & (d_apex <= NEEDLE_OD_UM / 2 + 2 * um_per_bin)
    ids = np.unique(lab[ring & reg])
    ids = ids[ids > 0]
    R = np.isin(lab, ids) & reg
    A = np.array([apex["x"], apex["y"]])
    bm = np.mean([[b["x"], b["y"]] for b in bases], axis=0)
    u = (bm - A) / np.linalg.norm(bm - A)
    v = np.array([-u[1], u[0]])
    out = {"pixels": int(R.sum()), "area_mm2": float(R.sum() * (um_per_bin / 1000) ** 2),
           "touches_apex": bool(len(ids))}
    if R.sum():
        py, px = np.nonzero(R)
        U = ((px - A[0]) * u[0] + (py - A[1]) * u[1]) * um_per_bin
        V = ((px - A[0]) * v[0] + (py - A[1]) * v[1]) * um_per_bin
        out.update({"reach_toward_base": float(U.max()), "reach_away": float(-U.min()),
                    "reach_across": float(np.abs(V).max()), "u_extent": float(U.max() - U.min()),
                    "v_extent": float(V.max() - V.min()),
                    "touches_base": [bool((R & (np.hypot(Xg - b["x"], Yg - b["y"]) * um_per_bin
                                                <= NEEDLE_OD_UM / 2 + 2 * um_per_bin)).any()) for b in bases]})
    return R, out


def bisector_points(apex, bases, um_per_bin, step_um=ROI_UM):
    """Centres (binned pixels) of contiguous ROIs of side `step_um` on the bisecting line, from
    the midpoint of the base electrodes to the edge of the apex footprint (Figure 1; Methods
    4.4 places the ROIs 'along the dashed line' of Figure 7B). Returns x, y and the distance
    from the base midpoint in um."""
    A = np.array([apex["x"], apex["y"]])
    bm = np.mean([[b["x"], b["y"]] for b in bases], axis=0)
    L = np.linalg.norm(A - bm) * um_per_bin
    u = (A - bm) / np.linalg.norm(A - bm)
    n = int((L - NEEDLE_OD_UM / 2) // step_um)
    d = step_um / 2 + step_um * np.arange(n)
    pts = bm[None, :] + u[None, :] * (d[:, None] / um_per_bin)
    return pts[:, 0], pts[:, 1], d


def vector_angle(e1, e2):
    """Angle in degrees between two field vectors given as (ex, ey) arrays."""
    dot = e1[0] * e2[0] + e1[1] * e2[1]
    n = np.hypot(*e1) * np.hypot(*e2)
    return np.degrees(np.arccos(np.clip(dot / n, -1, 1)))


def roi_grid(shape, fps, um_per_bin, radius_um=6000.0, margin_um=150.0, side_um=ROI_UM):
    """Centres (binned pixels) of a grid of contiguous ROIs of side `side_um` covering the image
    within `radius_um` of its centre (the glass window is about 14 mm across, so 6 mm keeps the
    ROIs off its rim), leaving out ROIs whose centre lies within `margin_um` of a footprint's
    750 um edge. The radius and margin are choices; the notebook shows how they change the result."""
    side = side_um / um_per_bin
    ny, nx = shape
    out = []
    for yc in np.arange(side / 2, ny, side):
        for xc in np.arange(side / 2, nx, side):
            if np.hypot(xc - nx / 2, yc - ny / 2) * um_per_bin > radius_um:
                continue
            if any(np.hypot(xc - f["x"], yc - f["y"]) * um_per_bin < NEEDLE_OD_UM / 2 + margin_um for f in fps):
                continue
            out.append((xc, yc))
    return np.array(out)


def roi_field(mag, origin, h, centres, um_per_bin, side_um=ROI_UM):
    """Mean of a field-grid quantity over each square ROI, from a 5 x 5 set of points in it."""
    offs = np.linspace(-0.4, 0.4, 5) * side_um
    dx, dy = np.meshgrid(offs, offs)
    out = []
    for x, y in centres:
        out.append(np.mean(sample(mag, origin, h, x * um_per_bin + dx.ravel(), y * um_per_bin + dy.ravel())))
    return np.array(out)


def thin_rois(centres, um_per_bin, step_um, side_um=ROI_UM):
    """Indices of the ROIs of a contiguous grid (from `roi_grid`) that lie on a coarser grid of
    spacing `step_um`, so that neighbouring ROIs kept are `step_um` apart. Used to test a rank
    correlation with fewer, less spatially dependent ROIs (the spacing is a choice; the notebook
    shows two)."""
    side = side_um / um_per_bin
    k = int(round(step_um / side_um))
    ix = np.round((centres[:, 0] - centres[:, 0].min()) / side).astype(int)
    iy = np.round((centres[:, 1] - centres[:, 1].min()) / side).astype(int)
    return np.nonzero((ix % k == 0) & (iy % k == 0))[0]


# ---------------------------------------------------------------- bright objects off the monolayer

DEBRIS_FACTOR = 10.0   # MemBrite above this multiple of the dish median marks an object (assumption)
DEBRIS_DILATE = 3      # binned pixels (about 30 um) added around each object (standard choice)


def load_crop(url, x0, y0, x1, y1):
    """Full-resolution crop (channel, y, x) of the stitched image, streamed from the archive."""
    f = h5py.File(remfile.File(url), "r")
    c = f[DATA_PATH][y0:y1, x0:x1, :]
    f.close()
    return np.moveaxis(c, 2, 0)


def debris_mask(membrite, valid, factor=DEBRIS_FACTOR, dilate=DEBRIS_DILATE):
    """Binned pixels on objects that are bright in the MemBrite channel: above `factor` times the
    median MemBrite inside `valid`, grown by `dilate` binned pixels. MemBrite stains the membranes
    of all cells about evenly, so an object many times brighter than the monolayer in it is not a
    monolayer cell (an assumption: the notebook shows the brightest such object at full resolution,
    and how the result changes with `factor`)."""
    from scipy.ndimage import binary_dilation
    m = membrite > factor * np.median(membrite[valid])
    if dilate:
        m = binary_dilation(m, iterations=dilate)
    return m


def masked_mean_filter(img, mask, size):
    """Mean of `img` over a `size` x `size` window, using only pixels inside `mask` (normalised
    convolution), so that masked-out pixels (footprints, the dark corners, objects) do not enter
    the mean. NaN outside `mask`."""
    from scipy.ndimage import uniform_filter
    w = uniform_filter(mask.astype(float), size)
    s = uniform_filter(np.where(mask, img, 0.0), size)
    with np.errstate(divide="ignore", invalid="ignore"):
        out = s / w
    out[~mask] = np.nan
    return out
