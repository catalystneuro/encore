"""Loading and ROI profiles for dandiset 001027 (Pakhomov et al. 2023, Bioelectrochemistry 152:108437,
doi:10.1016/j.bioelechem.2023.108437).

Each NWB file holds one dish: a single stitched 10x YO-PRO-1 (YP) fluorescence image of a CHO cell
monolayer, 20480 x 20480 uint16 pixels, taken 10 min after a pulse protocol delivered through a
quadrupole array of four needle electrodes. The session description names the packet (Protocol1,
2 or 3) and the first-pulse amplitude (4 kV). The files are streamed from the archive at the pinned
version; nothing is written to disk.

Where the parameters come from:

- `BLOCK = 8`: each image is reduced to the mean of 8 x 8 pixel blocks as it is read (5.2 um at
  the assumed scale), and ROI means are taken from this reduced image by bilinear sampling on a
  grid of half a block. This is a standard choice to keep the analysis fast. ROI edges move by at
  most one block (5 um) against a 72-um ROI; it is not expected to change a result.
- `UM_PER_PX = 0.65`: an assumption. The files give no pixel size (the ImageSeries `resolution`
  is 96 with unit "n.a."). The Methods (Section 2.4) and the file's device description name a 10x
  objective and an ORCA-Flash4 camera, whose pixels are 6.5 um, so 0.65 um per pixel without
  binning. The stitched tiles repeat every 1848 to 1856 pixels, 90% of the camera's 2048, which
  fits unbinned tiles with a 10% overlap and no resampling.
- `HALF_SPAN_MM = 1.65`, `N_ROI_TOTAL = 92`: Methods, Section 2.4, "The measurements were
  performed in 92 or 224 regions of interest (ROI), placed along one or both diagonals, and covering
  a distance of +/- 1.65 mm or +/- 3.65 mm from the geometrical center for the small and large
  arrays". The arrays in these files are the small one (shown in the notebook). Reading 92 ROIs as
  46 along each diagonal is a reading of that sentence; 92 along each is run as well.
- `EXCLUDE_FRAC = 0.05`: Methods, Section 2.4, "Areas immediately adjacent to the electrodes (<5%
  of the diagonal length) were excluded". Used by the relative ROI geometry, which needs no pixel
  size: ROIs run from the array center to 5% of the edge-to-edge diagonal short of each electrode.
- The geometrical center is the mean of the four electrode centers (Methods, Section 2.4, "from
  the geometrical center of the electrode array"). The electrodes are found in the image as the
  four dark disks (no YP uptake under the needles), by a ring filter and a circle fit; nothing in
  the files gives their position.
- ROI shape: a square, side equal to the ROI spacing, centered on the diagonal. The paper gives no
  ROI size or shape; this is a standard choice, and the notebook shows ROIs twice as dense.
- Background: the files hold no cell-free region or sham dish. The median intensity inside the
  central 60% of the radius of each electrode footprint (cells under the needle, not exposed) is
  taken per dish as background in the background-subtracted reading. Whether the paper subtracted
  a background from monolayer images is not stated (an open reading, see the notebook).
"""

from __future__ import annotations

import itertools
import re
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import ndimage as ndi

DANDISET_ID = "001027"
DANDISET_VERSION = "0.240605.1859"

BLOCK = 8
UM_PER_PX = 0.65
HALF_SPAN_MM = 1.65
N_ROI_TOTAL = 92
EXCLUDE_FRAC = 0.05
SLAB = 640           # rows read at a time
DISK_R0 = 160        # expected electrode footprint radius, in blocks, for the ring filter
BG_RADIUS_FRAC = 0.6
SATURATED = 65000    # pixel values at or above this are counted as saturated (uint16 maximum 65535)


def list_assets():
    """Path, asset id, size and SHA-256 of every asset at the pinned version."""
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        out = []
        for a in ds.get_assets():
            md = a.get_raw_metadata()
            out.append({"path": a.path, "asset_id": a.identifier, "size": a.size,
                        "sha256": md["digest"]["dandi:sha2-256"],
                        "url": a.get_content_url(follow_redirects=1, strip_query=True)})
    return sorted(out, key=lambda r: int(re.search(r"sub-(\d+)", r["path"]).group(1)))


def _packet(description):
    m = re.search(r"Protocol(\d)", description)
    return int(m.group(1)) if m else None


def _kv(description):
    m = re.search(r"applied at ([\d.]+)kV", description)
    return float(m.group(1)) if m else None


def load_dish(asset):
    """Stream one file and reduce its image to BLOCK x BLOCK means as it is read."""
    f = h5py.File(remfile.File(asset["url"]), "r")
    ims = f["acquisition/ScanningImaging"]
    d = ims["data"]
    n = d.shape[1]
    m = n // BLOCK
    img = np.zeros((m, m), np.float32)
    zero = np.zeros((m, m), np.float32)
    sat = np.zeros((m, m), np.float32)
    vmax = 0
    for r in range(0, n, SLAB):
        x = d[0, r:r + SLAB, :]
        vmax = max(vmax, int(x.max()))
        xf = x.astype(np.float32).reshape(SLAB // BLOCK, BLOCK, m, BLOCK)
        img[r // BLOCK:(r + SLAB) // BLOCK] = xf.mean(axis=(1, 3))
        zero[r // BLOCK:(r + SLAB) // BLOCK] = (x == 0).reshape(SLAB // BLOCK, BLOCK, m, BLOCK).mean(axis=(1, 3))
        sat[r // BLOCK:(r + SLAB) // BLOCK] = (x >= SATURATED).reshape(SLAB // BLOCK, BLOCK, m, BLOCK).mean(axis=(1, 3))
    desc = f["session_description"][()].decode()
    s = f["general/subject"]
    dish = {
        "path": asset["path"], "subject_id": s["subject_id"][()].decode(),
        "packet": _packet(desc), "kv": _kv(desc), "description": desc,
        "session_start": f["session_start_time"][()].decode(),
        "shape": d.shape, "dtype": str(d.dtype), "chunks": d.chunks, "max_value": vmax,
        "unit": d.attrs["unit"], "resolution": float(d.attrs["resolution"]),
        "conversion": float(d.attrs["conversion"]),
        "device": ims.attrs["description"],
        "species": s["species"][()].decode(), "strain": s["strain"][()].decode(),
        "age": s["age"][()].decode(),
        "img": img, "valid": zero < 0.5, "saturated": sat, "zero_frac": float((zero > 0.5).mean()),
    }
    f.close()
    return dish


def load_all(threads=5):
    assets = list_assets()
    with ThreadPoolExecutor(threads) as ex:
        dishes = list(ex.map(load_dish, assets))
    for a, d in zip(assets, dishes):
        d["sha256"] = a["sha256"]
    return dishes


def tile_step(valid):
    """Rows (in pixels) at which the left edge of the imaged area steps: the stitching tile grid."""
    left = np.array([np.argmax(r) for r in valid])
    return [int(i * BLOCK) for i in np.nonzero(np.diff(left))[0] + 1]


def _ring(r_in, r_out, size):
    yy, xx = np.mgrid[-size:size + 1, -size:size + 1]
    dd = np.hypot(yy, xx)
    return (dd <= r_in).astype(float), ((dd >= r_out[0]) & (dd <= r_out[1])).astype(float)


def _fit_circle(e):
    A = np.c_[2 * e[:, 0], 2 * e[:, 1], np.ones(len(e))]
    b = (e ** 2).sum(1)
    c = np.linalg.lstsq(A, b, rcond=None)[0]
    return c[0], c[1], np.sqrt(c[2] + c[0] ** 2 + c[1] ** 2)


def find_electrodes(img, valid):
    """The four electrode footprints, as (row, col, radius) in blocks, ordered by angle about their
    center (image rows point down, so the order is top left, top right, bottom right, bottom left).

    Candidates are dark disks under a ring filter (disk mean over the mean of a surrounding annulus,
    on a 4-fold coarser grid); of the ten best, the four that form the most regular square are kept.
    Each is refined by a circle fit to the steepest rise of intensity along 90 rays."""
    q = 4
    im = ndi.zoom(np.where(valid, img, 0.0), 1 / q, order=1)
    v = ndi.zoom(valid.astype(float), 1 / q, order=1)
    R = DISK_R0 / q
    kin, kout = _ring(0.8 * R, (1.15 * R, 1.6 * R), int(1.7 * R))
    with np.errstate(invalid="ignore", divide="ignore"):
        s_in = ndi.convolve(im, kin) / ndi.convolve(v, kin).clip(1e-6)
        s_out = ndi.convolve(im, kout) / ndi.convolve(v, kout).clip(1e-6)
        cov = ndi.convolve(v, kout) / kout.sum()
        score = np.where(cov > 0.95, s_in / s_out, np.inf)
    score[~np.isfinite(score)] = np.inf
    yy, xx = np.mgrid[:score.shape[0], :score.shape[1]]
    cands = []
    for _ in range(10):
        i = np.unravel_index(np.argmin(score), score.shape)
        if not np.isfinite(score[i]):
            break
        cands.append((i[0] * q, i[1] * q, score[i]))
        score[(yy - i[0]) ** 2 + (xx - i[1]) ** 2 < (2 * R) ** 2] = np.inf
    best = None
    for combo in itertools.combinations(cands, 4):
        c = np.array([(a, b) for a, b, _ in combo], float)
        cen = c.mean(0)
        c = c[np.argsort(np.arctan2(c[:, 0] - cen[0], c[:, 1] - cen[1]))]
        sides = [np.hypot(*(c[i] - c[(i + 1) % 4])) for i in range(4)]
        diags = [np.hypot(*(c[0] - c[2])), np.hypot(*(c[1] - c[3]))]
        irregular = (np.std(sides) / np.mean(sides) + abs(diags[0] - diags[1]) / np.mean(diags)
                     + abs(np.mean(diags) / np.mean(sides) - np.sqrt(2)))
        cost = 5 * irregular + sum(t for *_, t in combo)
        if best is None or cost < best[0]:
            best = (cost, c)
    sm = ndi.gaussian_filter(np.where(valid, img, np.median(img[valid])), 3)
    angs = np.linspace(0, 2 * np.pi, 90, endpoint=False)
    rr = np.arange(60, 260)
    out = []
    for cy, cx in best[1]:
        for _ in range(3):
            e = []
            for a in angs:
                p = ndi.map_coordinates(sm, [cy + rr * np.sin(a), cx + rr * np.cos(a)], order=1)
                j = np.argmax(np.gradient(p))
                e.append((cy + rr[j] * np.sin(a), cx + rr[j] * np.cos(a)))
            e = np.array(e)
            yc, xc, r = _fit_circle(e)
            dev = np.abs(np.hypot(e[:, 0] - yc, e[:, 1] - xc) - r)
            yc, xc, r = _fit_circle(e[dev < np.percentile(dev, 70)])
            cy, cx = yc, xc
        out.append((float(cy), float(cx), float(r)))
    cen = np.mean([(o[0], o[1]) for o in out], axis=0)
    out.sort(key=lambda o: np.arctan2(o[0] - cen[0], o[1] - cen[1]))
    return out


def geometry(electrodes):
    """Center-to-center and edge-to-edge diagonals and sides, in mm at UM_PER_PX."""
    c = np.array([(a, b) for a, b, _ in electrodes])
    R = np.array([r for *_, r in electrodes])
    mm = BLOCK * UM_PER_PX / 1000
    cc = [np.hypot(*(c[0] - c[2])), np.hypot(*(c[1] - c[3]))]
    ee = [cc[0] - R[0] - R[2], cc[1] - R[1] - R[3]]
    sides = [np.hypot(*(c[i] - c[(i + 1) % 4])) for i in range(4)]
    return {"diag_cc_mm": np.array(cc) * mm, "diag_edge_mm": np.array(ee) * mm,
            "side_cc_mm": np.array(sides) * mm, "disk_diameter_mm": 2 * R * mm}


def background(img, electrodes):
    """Median intensity inside the central BG_RADIUS_FRAC of each electrode footprint, and their mean."""
    yy, xx = np.ogrid[:img.shape[0], :img.shape[1]]
    vals = [float(np.median(img[(yy - cy) ** 2 + (xx - cx) ** 2 < (BG_RADIUS_FRAC * r) ** 2]))
            for cy, cx, r in electrodes]
    return float(np.mean(vals)), vals


def profiles(img, electrodes, geom="abs", n_per_diag=N_ROI_TOTAL // 2, roi_at_zero=False):
    """ROI means along both diagonals (electrodes 0 to 2, and 1 to 3).

    geom "abs": ROIs cover +/- HALF_SPAN_MM from the center at UM_PER_PX. geom "rel": they cover
    from the center to EXCLUDE_FRAC of the edge-to-edge diagonal short of each electrode footprint
    (the mean of the two half-lengths). With an even number of ROIs none sits at 0; with
    `roi_at_zero` one ROI is centered at 0 and there are n_per_diag + 1.
    Returns a list of two (positions in mm from the center, ROI means) pairs; positions run from
    the first electrode of the diagonal (negative) to the second (positive)."""
    c = np.array([(a, b) for a, b, _ in electrodes])
    R = np.array([r for *_, r in electrodes])
    cen = c.mean(0)
    mm = BLOCK * UM_PER_PX / 1000
    out = []
    for i, j in [(0, 2), (1, 3)]:
        u = c[j] - c[i]
        L = np.hypot(*u)
        u = u / L
        nrm = np.array([-u[1], u[0]])
        if geom == "abs":
            half = HALF_SPAN_MM / mm
        else:
            edge = L - R[i] - R[j]
            half = ((L / 2 - R[i]) + (L / 2 - R[j])) / 2 - EXCLUDE_FRAC * edge
        step = 2 * half / n_per_diag
        if roi_at_zero:
            ts = np.arange(-(n_per_diag // 2), n_per_diag // 2 + 1) * step
        else:
            ts = (np.arange(n_per_diag) - (n_per_diag - 1) / 2) * step
        g = np.linspace(-step / 2, step / 2, max(int(np.ceil(step * 2)) + 1, 3))
        A, B = np.meshgrid(g, g)
        A, B = A.ravel(), B.ravel()
        vals = []
        for t in ts:
            p = cen[None, :] + np.outer(t + A, u) + np.outer(B, nrm)
            vals.append(ndi.map_coordinates(img, [p[:, 0], p[:, 1]], order=1).mean())
        out.append((ts * mm, np.array(vals)))
    return out


def summary_values(prof, roi_at_zero=False):
    """Center and most peripheral values from `profiles` output.

    center: the ROI at 0 (roi_at_zero) or the mean of the two ROIs flanking 0, per diagonal.
    ends: the ROI closest to each electrode, in electrode order 0, 2, 1, 3."""
    centers, ends = [], []
    for t, v in prof:
        if roi_at_zero:
            centers.append(v[len(v) // 2])
        else:
            k = len(v) // 2
            centers.append((v[k - 1] + v[k]) / 2)
        ends += [v[0], v[-1]]
    return {"center_d1": centers[0], "center_d2": centers[1],
            "end_e0": ends[0], "end_e2": ends[1], "end_e1": ends[2], "end_e3": ends[3]}


# Readings of the open details for the Fig. 8 claims (see the claims file and the notebook).
GEOMS = ("abs", "rel")             # ROI span: +/- 1.65 mm at UM_PER_PX, or to 5% of the diagonal
ROI_COUNTS = (N_ROI_TOTAL // 2, N_ROI_TOTAL)   # ROIs per diagonal: 92 over both, or 92 on each
CENTERS = ("flank", "at0")         # center: mean of the two ROIs flanking 0, or one ROI at 0
BACKGROUNDS = ("raw", "bgsub")     # intensities as recorded, or less the per-dish background
DIAGONALS = ("both", "d1", "d2")   # mean of both diagonals, or one of them
MAIN = {"geom": "abs", "n_per_diag": N_ROI_TOTAL // 2, "center": "flank", "bg": "raw", "diag": "both"}


def dish_readings(dish):
    """Center, most peripheral (mean of the ROIs closest to the electrodes of the diagonals used)
    and per-electrode end values of one dish under every combination of readings."""
    e, bg = dish["electrodes"], dish["background"]
    rows, profs = [], {}
    for geom, n, center in itertools.product(GEOMS, ROI_COUNTS, CENTERS):
        z0 = center == "at0"
        pr = profiles(dish["img"], e, geom=geom, n_per_diag=n, roi_at_zero=z0)
        profs[(geom, n, center)] = pr
        sv = summary_values(pr, roi_at_zero=z0)
        for b, diag in itertools.product(BACKGROUNDS, DIAGONALS):
            off = bg if b == "bgsub" else 0.0
            if diag == "both":
                c = (sv["center_d1"] + sv["center_d2"]) / 2
                ends = [sv["end_e0"], sv["end_e2"], sv["end_e1"], sv["end_e3"]]
            elif diag == "d1":
                c, ends = sv["center_d1"], [sv["end_e0"], sv["end_e2"]]
            else:
                c, ends = sv["center_d2"], [sv["end_e1"], sv["end_e3"]]
            rows.append({"dish": dish["subject_id"], "packet": dish["packet"], "geom": geom,
                         "n_per_diag": n, "center": center, "bg": b, "diag": diag,
                         "center_au": c - off, "periph_au": float(np.mean(ends)) - off,
                         "periph_min_end_au": float(np.min(ends)) - off,
                         "periph_max_end_au": float(np.max(ends)) - off})
    return rows, profs


def mean_profile(profs, keys, bg=None):
    """Mean over dishes of the profile averaged over both diagonals, at the common positions."""
    out = []
    for p, b in zip(profs, bg if bg is not None else [0.0] * len(profs)):
        (t1, v1), (t2, v2) = p[keys]
        out.append((v1 + v2) / 2 - b)
    return t1, np.array(out)
