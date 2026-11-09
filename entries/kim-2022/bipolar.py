"""Loading and measures for the electroporation images of dandiset 000489.

Kim, Semenov, Kiester, Keppler, Ibey, Bixler & Pakhomov (2022), Bioelectrochemistry 149:108319,
doi:10.1016/j.bioelechem.2022.108319.

Each NWB file holds one dish: a stitched image of the whole glass bottom, 22323 x 22323 pixels,
stored as an ImageSeries `data` of shape (22323, 22323, 2), uint16, in gzip chunks of 175 x 349 x 1.
Channel 0 is MemBrite (ex/em 350/460 nm) and channel 1 YO-PRO-1 (YP, ex/em 480/535 nm), as the
series description lists them. Files are streamed from the archive at the pinned version: the
chunk index is read with h5py over `remfile`, and the chunks needed are fetched by HTTP range
requests and decompressed in memory. Nothing is written to disk.

Where the parameters come from:

- Electrode geometry and field: two parallel stainless-steel cylinders 1.5 mm in diameter, 3 mm
  apart side to side, touching the glass of a dish filled to 3.5 mm with a 1.6 S/m solution, the
  field taken 1 um above the glass for 1 V and scaled by the applied voltage (Methods 2.2 and
  2.3; claims file, opening comment). The electrodes span the whole depth of the solution and the
  glass and the free surface carry no current, so the potential does not vary with depth and the
  field is that of two parallel conducting cylinders in a plane, which has a closed form
  (`field_kv_cm`). The 35 mm dish wall, 15 mm or more from the electrodes, is left out
  (assumption); the notebook compares the model's field at the centre with the 15.1 kV/cm the
  paper cites. "3-mm side-to-side
  separation" (Methods 2.2) gives centres 4.5 mm apart; 3 mm between centres would give 34 kV/cm
  at the centre for 5.75 kV, against the 15.1 kV/cm the paper cites.
- First phase voltage 5.75 kV (Results 3.1).
- ROI: 200 um squares (Methods 2.5) along bb', the line at equal distance from both electrodes
  (Methods 2.3), tiled contiguously outward from the centre on both sides (claims file, opening
  comment, reading a), out to 3 mm (`N_ROI_SIDE`, 5.13 kV/cm). How far the paper's ROI extend is
  not given (assumption: past the weakest field the paper names, 6.7 kV/cm, to where uptake
  reaches background); the notebook shows fig2a-uptake-rises-with-field with the weakest ROI
  nearer the centre. The same squares along aa', the line through the electrode centres
  (Methods 2.3, Fig. 5 legend), out to 1.2 mm on each side, so that the outermost square ends
  0.2 mm short of the nominal footprint edge (a standard choice). The squares are aligned with the image axes (a standard choice; the
  electrodes lie within a few degrees of the image rows, so it cannot change a result).
- YP = YP_ROI x MB_0 / MB_ROI - YP_0, with YP_0 and MB_0 measured within the electrode
  footprints (Methods 2.5). The footprint is the dark disc in the YP image; the measuring area is
  a disc of radius `FOOTPRINT_MEASURE_MM` (0.5 mm, two thirds of the electrode radius) on the
  centre found, to keep away from its edge (a standard choice), and YP_0 and MB_0 are the means over both footprints (assumption: the paper
  says "within the electrodes' footprints", plural; the notebook gives each footprint).
- Pixel size: `UM_PER_PX` = 0.65 um, the ORCA-Flash4 sCMOS pixel (6.5 um) through the 10x objective
  (Methods 2.5 names both). The files give no pixel size (assumption). The variant
  `scale_from_electrodes` instead sets the scale so that the measured distance between electrode
  centres is 4.5 mm.
"""

from __future__ import annotations

import zlib
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

import h5py
import numpy as np
import remfile
import requests
from requests.adapters import HTTPAdapter
from scipy import ndimage
from urllib3.util.retry import Retry

DANDISET_ID = "000489"
DANDISET_VERSION = "0.230518.1811"
API = "https://api.dandiarchive.org/api"

SHAPE = 22323
CHUNK = (175, 349)
MB, YP = 0, 1                     # channel order in the files (series description)

UM_PER_PX = 0.65                  # 6.5 um camera pixel / 10x objective (assumption, see above)
ROI_UM = 200.0                    # Methods 2.5
ELECTRODE_RADIUS_MM = 0.75        # Methods 2.2, 2.3
ELECTRODE_GAP_MM = 3.0            # Methods 2.2, "3-mm side-to-side separation"
CENTRE_DISTANCE_MM = 2 * ELECTRODE_RADIUS_MM + ELECTRODE_GAP_MM
FIRST_PHASE_KV = 5.75             # Results 3.1
N_ROI_SIDE = 15                   # ROI centres from 0 to 3.0 mm along bb' on each side
N_ROI_AA = 6                      # ROI centres from 0 to 1.2 mm along aa', clear of the footprints
FOOTPRINT_MEASURE_MM = 0.5        # standard choice, see above

# Overview: block means of 25 x 23 pixels, 7 x 15 blocks per chunk.
BLOCK = (25, 23)
OV_SHAPE = (896, 960)


def _session() -> requests.Session:
    s = requests.Session()
    retry = Retry(total=10, backoff_factor=0.5, allowed_methods=None,
                  status_forcelist=[500, 502, 503, 504])
    s.mount("https://", HTTPAdapter(pool_maxsize=32, max_retries=retry))
    return s


# Dandiset 000548 (Effect of the number of pulses, Fig. 3 of the same paper) holds the 5-pulse
# unipolar dish 03, whose YP image in 000489 is a copy of dish 25-04's. It is read only for that check.
FIG3_DANDISET_ID = "000548"
FIG3_DANDISET_VERSION = "0.230519.1825"


def assets(dandiset: str = DANDISET_ID, version: str = DANDISET_VERSION) -> list[dict]:
    """Path, asset id, size and blob of every file at a pinned version."""
    url = f"{API}/dandisets/{dandiset}/versions/{version}/assets/?page_size=200"
    out = requests.get(url, timeout=60).json()["results"]
    return sorted(({"path": a["path"], "asset_id": a["asset_id"], "size": a["size"],
                    "blob": a.get("blob")} for a in out), key=lambda a: a["path"])


def dandiset_metadata(version: str = DANDISET_VERSION, dandiset: str = DANDISET_ID) -> dict:
    return requests.get(f"{API}/dandisets/{dandiset}/versions/{version}/", timeout=60).json()


def condition(path: str) -> tuple[str, int | None, str]:
    """(subject, second phase percent, dish label) from a path such as
    'sub-Fig2-50-10/sub-Fig2-50-10_ses-BPAE-bipolar-50 percent_image.nwb'."""
    subject = path.split("/")[0]
    parts = subject.split("-")
    if parts[1] != "Fig2":
        return subject, None, subject
    return subject, int(parts[2]), f"{parts[2]}%-{parts[3]}"


class Dish:
    """One file: its metadata, chunk index and a fetcher for pixel boxes."""

    def __init__(self, asset: dict):
        self.path = asset["path"]
        self.subject, self.amplitude, self.label = condition(self.path)
        self.url = requests.head(f"{API}/assets/{asset['asset_id']}/download/",
                                 allow_redirects=True, timeout=60).url
        f = h5py.File(remfile.File(self.url), "r")
        names = list(f["acquisition"].keys())
        self.series_name = names[0]
        g = f[f"acquisition/{self.series_name}"]
        d = g["data"]
        self.meta = {
            "acquisition": names,
            "shape": d.shape, "dtype": str(d.dtype), "chunks": d.chunks,
            "compression": d.compression, "unit": d.attrs.get("unit"),
            "conversion": float(d.attrs.get("conversion")),
            "rate": float(g["starting_time"].attrs.get("rate")),
            "description": g.attrs.get("description"),
            "session_description": f["session_description"][()].decode(),
            "session_id": f["general/session_id"][()].decode(),
            "subject_id": f["general/subject/subject_id"][()].decode(),
            "session_start": f["session_start_time"][()].decode(),
            "strain": f["general/subject/strain"][()].decode(),
            "processing": list(f["processing"].keys()),
            "analysis": list(f["analysis"].keys()),
            "stimulus": list(f["stimulus/presentation"].keys()),
        }
        index = []
        d.id.chunk_iter(lambda si: index.append((si.chunk_offset, si.byte_offset, si.size)))
        self.index = {off: (b, s) for off, b, s in index}
        f.close()
        self._s = _session()

    def chunk(self, row: int, col: int, channel: int) -> np.ndarray:
        """Full chunk with origin (row, col), as float; edge chunks are cut to the image."""
        b, s = self.index[(row, col, channel)]
        r = self._s.get(self.url, headers={"Range": f"bytes={b}-{b + s - 1}"}, timeout=120)
        r.raise_for_status()
        a = np.frombuffer(zlib.decompress(r.content), dtype="<u2").reshape(CHUNK)
        return a[: SHAPE - row, : SHAPE - col].astype(float)

    def overview(self, threads: int = 32) -> np.ndarray:
        """Both channels as block means of 25 x 23 pixels, shape (2, 896, 960)."""
        def one(key):
            row, col, ch = key
            a = self.chunk(row, col, ch)
            full = np.zeros(CHUNK)
            full[: a.shape[0], : a.shape[1]] = a
            return key, full[:, :345].reshape(7, 25, 15, 23).mean(axis=(1, 3))
        img = np.zeros((2,) + OV_SHAPE)
        with ThreadPoolExecutor(threads) as ex:
            for (row, col, ch), q in ex.map(one, list(self.index)):
                r, c = row // CHUNK[0] * 7, col // CHUNK[1] * 15
                img[ch, r: r + 7, c: c + 15] = q[: min(7, OV_SHAPE[0] - r)]
        return img

    def box(self, r0: int, r1: int, c0: int, c1: int, channel: int, threads: int = 16) -> np.ndarray:
        """Pixels [r0:r1, c0:c1] of one channel at full resolution."""
        rows = range(r0 // CHUNK[0] * CHUNK[0], r1, CHUNK[0])
        cols = range(c0 // CHUNK[1] * CHUNK[1], c1, CHUNK[1])
        keys = [(r, c) for r in rows for c in cols]
        out = np.zeros((r1 - r0, c1 - c0))
        with ThreadPoolExecutor(threads) as ex:
            parts = list(ex.map(lambda k: self.chunk(k[0], k[1], channel), keys))
        for (r, c), a in zip(keys, parts):
            rr0, cc0 = max(r, r0), max(c, c0)
            rr1, cc1 = min(r + a.shape[0], r1), min(c + a.shape[1], c1)
            out[rr0 - r0: rr1 - r0, cc0 - c0: cc1 - c0] = a[rr0 - r: rr1 - r, cc0 - c: cc1 - c]
        return out


# ---------------------------------------------------------------- electrode footprints

def find_footprints(yp_overview: np.ndarray) -> dict:
    """Centres (full-resolution pixels, row and column) and radius of the two electrode footprints.

    The footprints are dark discs in the YP image, ringed by the brightest uptake. A disc of
    radius 450 px darker than the ring from 700 to 1000 px around it is searched for in the
    overview; the two best centres more than 3000 px apart are kept and refined by `_segment`.
    """
    y = np.log1p(yp_overview)
    rr, cc = np.mgrid[-45:46, -45:46]
    dist = np.hypot(rr * BLOCK[0], cc * BLOCK[1])
    disc = (dist <= 450).astype(float)
    ring = ((dist >= 700) & (dist <= 1000)).astype(float)
    inside = ndimage.convolve(y, disc / disc.sum(), mode="constant")
    around = ndimage.convolve(y, ring / ring.sum(), mode="constant")
    score = around - inside
    # keep away from the rim of the glass bottom and the empty corners
    R, C = np.mgrid[: OV_SHAPE[0], : OV_SHAPE[1]]
    centre = (np.array(OV_SHAPE) - 1) / 2
    on_glass = np.hypot((R - centre[0]) * BLOCK[0], (C - centre[1]) * BLOCK[1]) < 7000
    score = np.where(on_glass, score, -np.inf)
    first = np.unravel_index(np.argmax(score), score.shape)
    far = np.hypot((R - first[0]) * BLOCK[0], (C - first[1]) * BLOCK[1]) > 3000
    second = np.unravel_index(np.argmax(np.where(far, score, -np.inf)), score.shape)
    centres, radii = [], []
    for p in sorted([first, second], key=lambda p: p[1]):
        c, r = _segment(y, p)
        centres.append(c)
        radii.append(r)
    return {"centres": np.array(centres), "radii": np.array(radii),
            "score": [float(score[first]), float(score[second])]}


def _segment(y: np.ndarray, p) -> tuple[tuple[float, float], float]:
    """Refine a footprint: the dark connected region around the coarse centre `p` (overview
    blocks) in the smoothed log YP image, thresholded halfway between its core and the median
    of a 3 mm window. Returns the centroid (full-resolution row, col) and the radius of the disc
    of equal area (px)."""
    w = 90
    r0, c0 = max(p[0] - w, 0), max(p[1] - w, 0)
    win = ndimage.gaussian_filter(y[r0: p[0] + w + 1, c0: p[1] + w + 1], 1.5)
    pr, pc = p[0] - r0, p[1] - c0
    core = np.median(win[pr - 5: pr + 6, pc - 5: pc + 6])
    thr = (core + np.median(win)) / 2
    lab, _ = ndimage.label(win < thr)
    target = lab[pr, pc]
    if target == 0:
        sub = lab[pr - 10: pr + 11, pc - 10: pc + 11]
        target = np.bincount(sub[sub > 0]).argmax()
    m = lab == target
    m = ndimage.binary_fill_holes(m)
    rr, cc = np.nonzero(m)
    centre = ((rr.mean() + r0 + 0.5) * BLOCK[0], (cc.mean() + c0 + 0.5) * BLOCK[1])
    area = m.sum() * BLOCK[0] * BLOCK[1]
    return centre, float(np.sqrt(area / np.pi))


# ---------------------------------------------------------------- field model

def field_kv_cm(x_mm, y_mm, kv: float = FIRST_PHASE_KV):
    """|E| (kV/cm) in the plane for two conducting cylinders at (+-h, 0) mm, radius a, with kv
    between them: the field of two line sources at +-c, c = sqrt(h^2 - a^2), whose
    equipotentials are the cylinders. |E| = V c / (acosh(h/a) r1 r2)."""
    a = ELECTRODE_RADIUS_MM
    h = CENTRE_DISTANCE_MM / 2
    c = np.sqrt(h * h - a * a)
    r1 = np.hypot(np.asarray(x_mm) - c, y_mm)
    r2 = np.hypot(np.asarray(x_mm) + c, y_mm)
    return kv * (c / 10) / (np.arccosh(h / a) * (r1 / 10) * (r2 / 10))  # mm -> cm


def roi_mean_field(centre_mm, axis, um_per_px: float, n: int = 21) -> float:
    """Mean model field over a 200 um square aligned with the image axes, centred at
    `centre_mm` (model coordinates); `axis` is the unit vector of the electrode axis in image
    (row, col) coordinates, used to rotate the square into the model frame."""
    half = ROI_UM / 1000 / 2
    s = np.linspace(-half, half, n)
    dr, dc = np.meshgrid(s, s, indexing="ij")
    # image offsets (row, col) -> model (x along electrodes, y along bb')
    perp = np.array([-axis[1], axis[0]])
    x = centre_mm[0] + dr * axis[0] + dc * axis[1]
    y = centre_mm[1] + dr * perp[0] + dc * perp[1]
    return float(field_kv_cm(x, y).mean())


# ---------------------------------------------------------------- ROI measures

def measure(dish: Dish, fp: dict, um_per_px: float = UM_PER_PX) -> dict:
    """Raw YP and MB means in each ROI along bb' and in each footprint, with each ROI's model
    field. ROI k (k = -N..N) is centred k x 200 um from the midpoint of the electrode centres,
    along the perpendicular to the electrode axis; negative k is towards the top of the image."""
    e1, e2 = fp["centres"]
    mid = (e1 + e2) / 2
    sep_px = float(np.hypot(*(e2 - e1)))
    axis = (e2 - e1) / sep_px
    perp = np.array([-axis[1], axis[0]])
    if perp[0] > 0:
        perp = -perp                       # perp points to the top of the image
    side = ROI_UM / um_per_px
    rois = []
    for k in range(-N_ROI_SIDE, N_ROI_SIDE + 1):
        cen = mid + (-k) * side * perp     # k < 0 towards the top (perp), k > 0 towards the bottom
        r0, c0 = int(round(cen[0] - side / 2)), int(round(cen[1] - side / 2))
        r1, c1 = r0 + int(round(side)), c0 + int(round(side))
        vals = {ch: dish.box(r0, r1, c0, c1, ch).mean() for ch in (MB, YP)}
        off = cen - mid
        x_mm = float(off @ axis) * um_per_px / 1000
        y_mm = float(off @ perp) * um_per_px / 1000
        rois.append({"k": k, "distance_mm": abs(k) * ROI_UM / 1000, "row": cen[0], "col": cen[1],
                     "field": roi_mean_field((x_mm, y_mm), axis, um_per_px),
                     "YP_roi": vals[YP], "MB_roi": vals[MB]})
    rois_aa = []
    for k in range(-N_ROI_AA, N_ROI_AA + 1):
        cen = mid + k * side * axis        # k < 0 towards the left electrode, k > 0 the right one
        r0, c0 = int(round(cen[0] - side / 2)), int(round(cen[1] - side / 2))
        r1, c1 = r0 + int(round(side)), c0 + int(round(side))
        vals = {ch: dish.box(r0, r1, c0, c1, ch).mean() for ch in (MB, YP)}
        x_mm = k * ROI_UM / 1000
        rois_aa.append({"k": k, "distance_mm": abs(x_mm), "row": cen[0], "col": cen[1],
                        "field": roi_mean_field((x_mm, 0.0), axis, um_per_px),
                        "YP_roi": vals[YP], "MB_roi": vals[MB]})
    feet = []
    for c in fp["centres"]:
        r = FOOTPRINT_MEASURE_MM * 1000 / um_per_px
        r0, c0 = int(c[0] - r), int(c[1] - r)
        r1, c1 = int(c[0] + r) + 1, int(c[1] + r) + 1
        RR, CC = np.mgrid[r0:r1, c0:c1]
        m = np.hypot(RR - c[0], CC - c[1]) <= r
        feet.append({ch: float(dish.box(r0, r1, c0, c1, ch)[m].mean()) for ch in (MB, YP)})
    return {"rois": rois, "rois_aa": rois_aa, "footprints": feet, "separation_px": sep_px, "axis": axis}


def yp_index(yp_roi, mb_roi, yp0, mb0):
    """Methods 2.5: YP = YP_ROI x MB_0 / MB_ROI - YP_0."""
    return yp_roi * mb0 / mb_roi - yp0


def load_dish(asset: dict) -> dict:
    """Everything the notebook uses from one file: metadata, overview, footprints, and the ROI
    measures at the camera pixel size and at the scale set by the electrode separation."""
    dish = Dish(asset)
    out = {"path": dish.path, "subject": dish.subject, "amplitude": dish.amplitude,
           "label": dish.label, "meta": dish.meta}
    ov = dish.overview()
    out["overview"] = ov
    if dish.amplitude is None:
        return out
    fp = find_footprints(ov[YP])
    out["footprints"] = fp
    out["measure"] = measure(dish, fp)
    sep_mm_nominal = CENTRE_DISTANCE_MM * 1000
    out["measure_scaled"] = measure(dish, fp, um_per_px=sep_mm_nominal / out["measure"]["separation_px"])
    return out


def load_all(workers: int = 4) -> list[dict]:
    """All files, one process per file at a time (decompression is CPU bound)."""
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(load_dish, assets()))


def session_descriptions(dandiset: str, version: str) -> list[dict]:
    """Path and NWB session_description of every file of a dandiset version (metadata only)."""
    out = []
    for a in assets(dandiset, version):
        url = requests.head(f"{API}/assets/{a['asset_id']}/download/", allow_redirects=True, timeout=60).url
        with h5py.File(remfile.File(url), "r") as f:
            out.append({"path": a["path"], "session_description": f["session_description"][()].decode()})
    return out


def roi_table(dishes: list[dict], which: str = "measure", side: str = "both",
              footprint: str = "both") -> "pd.DataFrame":
    """One row per dish and distance along bb': the YP index (Methods 2.5) and the ROI's model
    field. `side` is 'both' (the two ROI at the same distance averaged; claims file, reading a),
    'top' or 'bottom' (one side only, reading b). `footprint` is 'both' (YP_0 and MB_0 averaged
    over the two footprints), 'left' or 'right'."""
    import pandas as pd
    rows = []
    for d in dishes:
        if d["amplitude"] is None:
            continue
        m = d[which]
        feet = m["footprints"]
        use = {"both": feet, "left": feet[:1], "right": feet[1:]}[footprint]
        yp0 = np.mean([f[YP] for f in use])
        mb0 = np.mean([f[MB] for f in use])
        for r in m["rois"]:
            if side == "top" and r["k"] > 0 or side == "bottom" and r["k"] < 0:
                continue
            rows.append({"dish": d["label"], "subject": d["subject"], "amplitude": d["amplitude"],
                         "j": abs(r["k"]), "field": r["field"],
                         "YP": yp_index(r["YP_roi"], r["MB_roi"], yp0, mb0)})
    t = pd.DataFrame(rows)
    return (t.groupby(["dish", "subject", "amplitude", "j"], as_index=False)
             .agg(field=("field", "mean"), YP=("YP", "mean")))
