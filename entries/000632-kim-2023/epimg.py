"""Load and measure the stitched dish images of dandiset 000632 (Kim et al. 2023, Figure 3).

Each NWB file holds one ImageSeries, acquisition/ScaningImaging, whose data is a single
stitched image of the whole dish, shape (rows, cols, 2), uint16, stored in gzip chunks of
218 x 464 x 1. Channel 0 is MemBrite (DAPI cube, all cells) and channel 1 is YO-PRO-1 (FITC
cube, electroporated cells); the order is read from the ImageSeries description ("Channel 1
ex/em 350/460nm for MemBrite dye; ex/em 480/535nm for YOPRO-1") and checked in the notebook.

Reading. The files are 1.7 to 1.8 GB each. Streaming them chunk by chunk with remfile takes
about 0.05 s per chunk, so the module reads the HDF5 chunk index once with h5py and fetches
the chunks it needs as parallel HTTP range requests, decompressing each with zlib. Nothing is
written to disk.

Parameters and where they come from:
- ROI_UM = 200: the 200 x 200 um ROI at the center of the square array (Methods 4.4, "we used
  data from a single 200 x 200 um ROI placed in the center of the array").
- FOOTPRINT_OD_UM = 1500 and FOOTPRINT_ID_UM = 500: outer and inner diameters of the hollow
  needles (Methods 4.2, "outside and inside diameters of 1.5 and 0.5 mm"; the square array was
  "made of 1.5 mm hollow needles").
- UM_PER_PX = 0.65: the files give no pixel size. 0.65 um is the ORCA-Flash4 pixel (6.5 um)
  behind the 10x objective named in Methods 4.4; an assumption, checked in the notebook against
  the 1.5 mm footprint diameter, with center ROIs 25% smaller and larger as variants.
- Footprint background ROI: Methods 4.4 says spontaneous uptake was measured "within the hollow
  electrodes' footprints" without giving the ROI. As a stated choice the module measures a
  200 x 200 um square (the paper's ROI size) at the center of each footprint, which lies inside
  the 0.5 mm lumen; the mean of the four footprints is the dish's background. A variant uses
  the whole disc of each footprint inside 0.6 of its outer radius.
- Footprint detection (template matching on a reduced image) and the overview reduction are
  standard image-processing choices that only locate the electrodes; the notebook shows the
  located footprints for every dish.
"""
import re
import zlib
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
import requests

DANDISET = "000632"
VERSION = "0.231012.1930"
API = "https://api.dandiarchive.org/api"
DATA_PATH = "acquisition/ScaningImaging/data"
MEMBRITE, YP = 0, 1
ROI_UM = 200.0
FOOTPRINT_OD_UM = 1500.0
FOOTPRINT_ID_UM = 500.0
UM_PER_PX = 0.65
# overview reduction of each 218 x 464 chunk to 2 x 4 blocks of 109 x 116 pixels
RED_R, RED_C = 2, 4
THREADS = 32


def list_assets():
    """Assets of the pinned version, with the condition parsed from the path."""
    out = []
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        j = r.json()
        for a in j["results"]:
            m = re.search(r"ses-(Co|Cross)-directional-(1Hz|770kHz)", a["path"])
            out.append(dict(asset_id=a["asset_id"], path=a["path"], size=a["size"],
                            direction=m.group(1).lower(), freq=m.group(2)))
        url = j["next"]
    return out


def asset_url(asset_id):
    """The S3 address the archive redirects the asset's download to."""
    r = requests.get(f"{API}/assets/{asset_id}/download/", allow_redirects=False, timeout=60)
    assert r.status_code in (301, 302, 307), r.status_code
    return r.headers["Location"]


class DishImage:
    """One stitched image, read through its chunk index."""

    def __init__(self, asset_id):
        self.asset_id = asset_id
        self.url = asset_url(asset_id)
        self.h5 = h5py.File(remfile.File(self.url), "r")
        d = self.h5[DATA_PATH]
        assert d.compression == "gzip" and not d.shuffle and d.dtype == np.uint16
        self.shape = d.shape
        self.chunks = d.chunks
        self.index = {}
        d.id.chunk_iter(lambda s: self.index.__setitem__(s.chunk_offset, (s.byte_offset, s.size)))
        self.session = requests.Session()
        self.session.mount("https://", requests.adapters.HTTPAdapter(pool_maxsize=THREADS))

    def meta(self):
        f = self.h5
        g = lambda k: f[k][()].decode() if isinstance(f[k][()], bytes) else f[k][()]
        return dict(session_id=g("general/session_id"), subject_id=g("general/subject/subject_id"),
                    session_start_time=g("session_start_time"),
                    session_description=g("session_description"),
                    description=f["acquisition/ScaningImaging"].attrs["description"],
                    unit=f[DATA_PATH].attrs["unit"], shape=self.shape)

    def _chunk(self, key):
        bo, sz = self.index[key]
        for attempt in range(5):
            try:
                r = self.session.get(self.url, headers={"Range": f"bytes={bo}-{bo + sz - 1}"},
                                     timeout=60)
                r.raise_for_status()
                break
            except requests.RequestException:
                if attempt == 4:
                    raise
        return np.frombuffer(zlib.decompress(r.content), dtype="<u2").reshape(self.chunks[:2])

    def overview(self, channel):
        """Block means of 109 x 116 pixels over the whole image (edge chunks are padded)."""
        cr, cc = self.chunks[:2]
        nr, nc = -(-self.shape[0] // cr), -(-self.shape[1] // cc)
        keys = [(i * cr, j * cc, channel) for i in range(nr) for j in range(nc)]
        ov = np.zeros((nr * RED_R, nc * RED_C))

        def one(k):
            x = self._chunk(k).astype(float)
            return k, x.reshape(RED_R, cr // RED_R, RED_C, cc // RED_C).mean(axis=(1, 3))

        with ThreadPoolExecutor(THREADS) as ex:
            for k, b in ex.map(one, keys):
                i, j = k[0] // cr, k[1] // cc
                ov[i * RED_R:(i + 1) * RED_R, j * RED_C:(j + 1) * RED_C] = b
        return ov

    def region(self, channel, r0, r1, c0, c1):
        """Full-resolution pixels [r0:r1, c0:c1] of one channel."""
        cr, cc = self.chunks[:2]
        keys = [(i, j, channel) for i in range(r0 // cr * cr, r1, cr)
                for j in range(c0 // cc * cc, c1, cc)]
        with ThreadPoolExecutor(THREADS) as ex:
            blocks = dict(zip(keys, ex.map(self._chunk, keys)))
        R0, C0 = keys[0][0], keys[0][1]
        R1, C1 = keys[-1][0] + cr, keys[-1][1] + cc
        full = np.zeros((R1 - R0, C1 - C0), dtype=np.uint16)
        for (i, j, _), b in blocks.items():
            full[i - R0:i - R0 + cr, j - C0:j - C0 + cc] = b
        return full[r0 - R0:r1 - R0, c0 - C0:c1 - C0]

    def close(self):
        self.h5.close()


# ---- locating the electrodes on the overview ----

def ov_px_um():
    """Size of an overview pixel (rows, cols) in um, under UM_PER_PX."""
    return 218 // RED_R * UM_PER_PX, 464 // RED_C * UM_PER_PX


def find_footprints(ov):
    """Centers (overview row, col) and radii of the four dark electrode footprints.

    Template matching: for each pixel, the mean of a ring 1.2 to 1.6 footprint radii out minus
    the mean of the disc inside 0.7 radii, on the log YP overview; of the strongest separated
    maxima inside the central part of the dish, the four that form a square are the electrodes. Each center is then refined
    as the darkness-weighted centroid within 1.2 radii. The radius is where the azimuthally averaged profile crosses
    half-way between the disc and ring levels.
    """
    from scipy import ndimage
    pr, pc = ov_px_um()
    R = FOOTPRINT_OD_UM / 2
    yy, xx = np.mgrid[-30:31, -30:31]
    rr = np.hypot(yy * pr, xx * pc)
    disc = (rr < 0.7 * R).astype(float)
    ring = ((rr > 1.2 * R) & (rr < 1.6 * R)).astype(float)
    x = np.log(np.clip(ov, 1, None))
    score = ndimage.correlate(x, ring / ring.sum()) - ndimage.correlate(x, disc / disc.sum())
    # restrict to the central half of the image, away from the rim of the dish
    n0, n1 = ov.shape
    mask = np.zeros_like(score, bool)
    mask[n0 // 4:3 * n0 // 4, n1 // 4:3 * n1 // 4] = True
    score = np.where(mask, score, -np.inf)
    # candidate dark discs: the 12 strongest maxima at least 1.8 mm apart
    cand = []
    s = score.copy()
    for _ in range(12):
        i, j = np.unravel_index(np.argmax(s), s.shape)
        if not np.isfinite(s[i, j]):
            break
        cand.append((i, j, s[i, j]))
        s[max(0, i - 25):i + 26, max(0, j - 25):j + 26] = -np.inf
    # the electrodes: the four candidates that best form a square with sides of 3 to 4.5 mm
    # (a range wide enough to hold any array the overviews show; the paper gives no spacing)
    from itertools import combinations
    best = None
    for combo in combinations(cand, 4):
        p = np.array([(a * pr, b * pc) for a, b, _ in combo])
        c = p.mean(axis=0)
        p = p[np.argsort(np.arctan2(p[:, 0] - c[0], p[:, 1] - c[1]))]
        sides = np.hypot(*(p - np.roll(p, 1, axis=0)).T)
        diags = np.hypot(*(p[:2] - p[2:]).T)
        if not 3000 < sides.mean() < 4500:
            continue
        bad = sides.std() / sides.mean() + abs(diags.mean() / sides.mean() - np.sqrt(2))
        if bad > 0.15:
            continue
        total = sum(x[2] for x in combo)
        if best is None or total > best[0]:
            best = (total, combo)
    assert best is not None, "no square of footprints found"
    peaks = best[1]
    out = []
    for i, j, sc in peaks:
        # refine: intensity-weighted centroid of darkness within 1.2 R
        w = 9
        sub = x[i - w:i + w + 1, j - w:j + w + 1]
        yy2, xx2 = np.mgrid[-w:w + 1, -w:w + 1]
        inside = np.hypot(yy2 * pr, xx2 * pc) < 1.2 * R
        dark = np.where(inside, np.clip(np.percentile(sub[~inside], 50) - sub, 0, None), 0)
        ci = i + (dark * yy2).sum() / dark.sum()
        cj = j + (dark * xx2).sum() / dark.sum()
        # radius from the radial profile
        Y, X = np.mgrid[0:n0, 0:n1]
        rad = np.hypot((Y - ci) * pr, (X - cj) * pc)
        edges = np.arange(0, 2.0 * R, 50.0)
        prof = np.array([x[m].mean() if (m := (rad >= a) & (rad < a + 50)).any() else np.nan
                         for a in edges])
        lo = np.nanmean(prof[(edges > 0.25 * R) & (edges < 0.75 * R)])
        hi = np.nanmean(prof[(edges > 1.2 * R) & (edges < 1.6 * R)])
        # first crossing outside half the nominal radius (the lumen can be bright)
        k = np.argmax((prof > (lo + hi) / 2) & (edges > 0.5 * R))
        out.append(dict(row=ci, col=cj, radius_um=edges[k] + 25, score=sc))
    # order: by angle around the array center
    cr = np.mean([o["row"] for o in out])
    cc = np.mean([o["col"] for o in out])
    out.sort(key=lambda o: np.arctan2(o["row"] - cr, o["col"] - cc))
    # a footprint on a disrupted patch of monolayer can be misplaced. How far the four centers
    # are from a parallelogram (the distance of any corner from the one the other three
    # define; the same for all four) is reported, and the notebook shows the result without
    # dishes where it exceeds 400 um (a standard choice).
    p = np.array([(o["row"] * pr, o["col"] * pc) for o in out])
    dev = float(np.hypot(*(p[0] - (p[1] + p[3] - p[2]))))
    for o in out:
        o["parallelogram_dev_um"] = dev
    return out


def ov_to_px(row, col):
    """Overview coordinates (pixel centers) to full-resolution pixel coordinates."""
    return (row + 0.5) * (218 // RED_R), (col + 0.5) * (464 // RED_C)


# ---- measuring one dish ----

def _roi_mean(im, channel, r, c, half_px):
    r0, c0 = int(round(r - half_px)), int(round(c - half_px))
    n = int(round(2 * half_px))
    return float(im.region(channel, r0, r0 + n, c0, c0 + n).astype(float).mean())


def _disc_mean(im, channel, r, c, radius_px):
    n = int(np.ceil(radius_px))
    r0, c0 = int(round(r)) - n, int(round(c)) - n
    x = im.region(channel, r0, r0 + 2 * n + 1, c0, c0 + 2 * n + 1).astype(float)
    yy, xx = np.mgrid[r0:r0 + 2 * n + 1, c0:c0 + 2 * n + 1]
    return float(x[np.hypot(yy - r, xx - c) < radius_px].mean())


def measure_dish(asset):
    """All per-dish numbers the notebook uses, from one stitched image.

    center_yp, center_mb: mean YP and MemBrite intensity in the 200 x 200 um ROI at the center
    of the array (the mean of the four footprint centers); center_yp_150 and center_yp_250, YP in
    ROIs of 150 and 250 um sides at the same place.
    fp_yp, fp_mb: the same in a 200 x 200 um ROI at the center of each footprint (4 values).
    fp_disc_yp: mean YP inside 0.6 of the outer radius of each footprint (variant).
    diag_yp: mean YP on the overview within 250 um of the point half-way from the array center
    to each electrode (4 values, same order as the footprints), for the label check.
    """
    im = DishImage(asset["asset_id"])
    meta = im.meta()
    ov = im.overview(YP)
    fps = find_footprints(ov)
    half = ROI_UM / 2 / UM_PER_PX
    pts = [ov_to_px(f["row"], f["col"]) for f in fps]
    cr, cc = np.mean([p[0] for p in pts]), np.mean([p[1] for p in pts])
    out = dict(asset, **{k: meta[k] for k in ("session_id", "subject_id", "session_start_time")})
    out["center_px"] = (cr, cc)
    out["footprints"] = fps
    out["center_yp"] = _roi_mean(im, YP, cr, cc, half)
    out["center_mb"] = _roi_mean(im, MEMBRITE, cr, cc, half)
    # ROIs 25% smaller and larger, for the pixel size the files do not give
    out["center_yp_150"] = _roi_mean(im, YP, cr, cc, 0.75 * half)
    out["center_yp_250"] = _roi_mean(im, YP, cr, cc, 1.25 * half)
    out["fp_yp"] = [_roi_mean(im, YP, r, c, half) for r, c in pts]
    out["fp_mb"] = [_roi_mean(im, MEMBRITE, r, c, half) for r, c in pts]
    rad = 0.6 * FOOTPRINT_OD_UM / 2 / UM_PER_PX
    out["fp_disc_yp"] = [_disc_mean(im, YP, r, c, rad) for r, c in pts]
    pr, pc = ov_px_um()
    Y, X = np.mgrid[0:ov.shape[0], 0:ov.shape[1]]
    ocr = np.mean([f["row"] for f in fps])
    occ = np.mean([f["col"] for f in fps])
    diag = []
    for f in fps:
        mr, mc = (ocr + f["row"]) / 2, (occ + f["col"]) / 2
        diag.append(float(ov[np.hypot((Y - mr) * pr, (X - mc) * pc) < 250].mean()))
    out["diag_yp"] = diag
    out["overview"] = ov
    # fingerprint of the compressed chunk sizes of both channels, to find files deposited twice
    out["chunk_fingerprint"] = hash(tuple(sorted(im.index.items())))
    out["session_description"] = meta["session_description"]
    out["image_description"] = meta["description"]
    out["unit"] = meta["unit"]
    out["shape"] = meta["shape"]
    im.close()
    return out
