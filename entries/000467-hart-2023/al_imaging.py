"""Loading and measures for the antennal lobe calcium imaging of dandiset 000467.

Hart, Frank, Lopes et al. (2023), Cell, doi:10.1016/j.cell.2023.05.025. The claims are in
claims/000467/10.1016-j.cell.2023.05.025.yaml, whose opening comment defines the shared
methods M1 to M4 used here.

Each NWB file holds one z-plane of one trial: acquisition "TwoPhotonSeries1", 40 volumes (120 in
the five 144 s recordings) of 512 x 512 pixels, stored as uncompressed contiguous float64 (raw
fluorescence, integer valued). The file name gives the ant, the session date, the concentration
("0-48x" is 48%, "1x" the undiluted vehicle or isopropanol), the odor, the number of volumes, the
trial number and the depth (0 to 160 um). Files are streamed from the archive at the pinned
version; nothing is written to disk. `open_nwb` reads a file with remfile, h5py and pynwb;
`read_frames` reads only the frames (and rows) an analysis needs, by HTTP range requests at the
byte offset of the data that h5py reports (`DATA_OFFSET`, the same in every file of a size; the
notebooks check it on a sample of files, and every read is checked to hold integers in the
detector's range, which a wrong offset would not give).

Where the parameters come from:

- F0 the mean of volumes 1 to 5, peak fold change the mean of dF/F0 over volumes 9 to 14
  (counted from 1), a 2-pixel Minimum filter, the maximum over the 33 planes, values clipped to
  [-1, 4]: the Methods, "Image processing and analysis" (claims file, M1). Clipping and the
  Minimum filter commute with each other and with the maximum (all are monotone), so the
  Methods' order and the macro's give the same map; there is no separate variant to run.
- Image Stabilizer (Fiji) is not available in Python. In its place each frame is aligned to the
  mean of the baseline frames by phase correlation on 2 x 2 binned images (whole-pixel
  translation in steps of 2 pixels), an assumption that stands for the Methods' translation
  stabilization; "max_shift" and "shift" report how far frames moved.
- The Minimum filter's footprint is ImageJ's for radius 2 (RankFilters: dx^2 + dy^2 <= r^2 + 1,
  21 pixels).
- The 1-sigma Gaussian blur of the Methods' first look (claims file, fig4-no-decreases).
- Per-plane maps are kept binned 4 x 4 (1.16 um bins) to fit in memory, a storage choice; the
  max projections and the ROIs drawn on them are kept at full resolution.
- ROIs (claims file, M2): the connected regions of at least 0.2 (`THRESHOLD`, the Methods' response
  threshold) in each trial's map that recur in another trial of the same odor at a concentration
  (claims file, drawing (a); `recurring_regions`), merged into connected regions; reading "a"
  keeps them all, reading "b" keeps those at least `GLOM_MIN_UM` across (10 um, the lower end of
  the 10 to 20 um glomerulus diameter in the Results, "Recording calcium responses to general
  odorants") and splits those wider than `GLOM_MAX_UM` (20 um) at local maxima at least 10 um
  apart. Regions of different odors that overlap are one ROI when their depths (the plane of
  their largest mean response) are within `SAME_DEPTH_PLANES` planes (10 um, the lower end of a
  glomerulus diameter, a choice made here since the Methods say only "the same z-depth"), and
  separate ROIs otherwise (Methods). ROI value "i" the mean of its pixels in a trial's max
  projection, "ii" their maximum; counting "x" the trial mean of the value at least 0.2,
  "y" the mean over trials of the per-trial count.
- Single glomeruli (claims file, M3): per volume, the maximum of raw fluorescence over the centre
  plane and its two neighbours, then the ROI's mean, then dF/F0 with F0 the mean of volumes 1 to
  5 (Methods, "For analyses of single glomeruli"). The ROI is a disc of `DISC_UM` (15 um)
  diameter on the glomerulus centre or the region of at least 0.2 there, the two ROIs the claims
  file names (M3). Each plane's row band is stabilized as the maps are (`stabilize_band`), as the
  claims file's M3 assumes; the unstabilized disc trace is kept for comparison.
- Onset: the first volume after stimulus start where dF/F0 exceeds the baseline mean plus 3 SD
  of the baseline (volumes 1 to 5); time to maximum: the volume of the largest dF/F0 (Methods,
  "Statistical analyses of odor responses"). Volume times are (index - 1) x VOLUME_S plus the
  plane's starting time in the file, a standard choice (claims file, figs7c-temporal-lme).
"""

from __future__ import annotations

import re
import threading
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy import ndimage

DANDISET_ID = "000467"
DANDISET_VERSION = "0.261004.1655"
API = "https://api.dandiarchive.org/api"

NX = 512
FRAME_BYTES = NX * NX * 8          # float64
DATA_OFFSET = 3464                 # byte offset of TwoPhotonSeries1/data (checked in the notebooks)
DETECTOR_MAX = 8191                # 13-bit range seen in the data
PIXEL_UM = 0.28886664              # grid_spacing in the files (claims file: 0.289 um per pixel)
PLANE_UM = 5.0
N_PLANES = 33
VOLUME_S = 1 / 0.83                # imaging_rate 0.83 volumes/s in the files
STIM_ON_S, STIM_OFF_S = 3.0, 8.0   # file descriptions and Methods
BASE = slice(0, 5)                 # volumes 1-5
PEAK = slice(8, 14)                # volumes 9-14
THRESHOLD = 0.2
CLIP = (-1.0, 4.0)
BIN = 4
GLOM_MIN_UM, GLOM_MAX_UM = 10.0, 20.0
SAME_DEPTH_PLANES = 2
DISC_UM = 15.0
MERGE_OVERLAP = 0.5

ODOR_SHORT = {
    "4-methyl-3-heptanone": "heptanone", "4-methyl-3-heptanol": "heptanol",
    "4-methyl-3-hexanol": "hexanol", "6-methyl-5-hepten-2-one": "6MHO",
    "paraffin-oil": "vehicle", "isopropanol": "isopropanol", "3-hexanone": "3-hexanone",
    "ethylpyrazine": "ethylpyrazine", "ethanol": "ethanol", "propionic-acid": "propionic acid",
}
PHEROMONES = ["heptanone", "heptanol", "hexanol", "6MHO"]
GENERAL = ["3-hexanone", "ethylpyrazine", "ethanol", "isopropanol", "propionic acid"]

_NAME = re.compile(r"^sub-(?P<sub>[^_]+)_ses-(?P<date>m\d+-d\d+-y\d+)-(?P<ant>ant\d+)-"
                   r"(?P<conc>[\d-]+x)-(?P<odor>.+)-(?P<nvol>\d+)-t(?P<trial>\d+)-z(?P<z>\d+)um_ophys\.nwb$")


# --- listing and reading ---------------------------------------------------------------------

def list_assets() -> pd.DataFrame:
    """Every asset of the pinned version, with the fields its file name gives."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=1000"
    rows = []
    while url:
        page = requests.get(url, timeout=60).json()
        for a in page["results"]:
            m = _NAME.match(a["path"].split("/")[-1])
            row = {"path": a["path"], "asset_id": a["asset_id"], "blob": a["blob"], "size": a["size"],
                   "parsed": m is not None}
            if m:
                row.update(m.groupdict())
            rows.append(row)
        url = page["next"]
    df = pd.DataFrame(rows)
    df["trial"] = df.trial.astype(int)
    df["z"] = df.z.astype(int)
    df["nvol"] = df.nvol.astype(int)
    df["plane"] = df.z // 5
    # "0-48x" -> 0.48, "0-0075x" -> 0.0075, "1x" -> 1
    df["conc"] = df.conc.str.rstrip("x").str.replace("-", ".", n=1).astype(float)
    df["odor_name"] = df.odor
    df["odor"] = df.odor.map(ODOR_SHORT)
    df["ant"] = df["sub"]
    return df


def trials(assets: pd.DataFrame) -> pd.DataFrame:
    """One row per trial (a volume series of 33 planes), with the planes' blobs in plane order."""
    g = assets.sort_values("plane").groupby(["ant", "trial", "odor", "conc", "nvol"])
    out = g.agg(n_planes=("plane", "size"), blobs=("blob", list), sizes=("size", list)).reset_index()
    return out


def s3_url(blob: str) -> str:
    return f"https://dandiarchive.s3.amazonaws.com/blobs/{blob[:3]}/{blob[3:6]}/{blob}"


def open_nwb(blob: str):
    """Open one file by streaming (remfile + h5py); returns the h5py file."""
    return h5py.File(remfile.File(s3_url(blob)), "r")


_local = threading.local()


def _session() -> requests.Session:
    if not hasattr(_local, "s"):
        _local.s = requests.Session()
    return _local.s


def _get(blob: str, start: int, stop: int) -> bytes:
    for attempt in range(5):
        try:
            r = _session().get(s3_url(blob), headers={"Range": f"bytes={start}-{stop - 1}"}, timeout=120)
            if r.status_code == 206 and len(r.content) == stop - start:
                return r.content
        except requests.RequestException:
            pass
    raise IOError(f"could not read {blob} bytes {start}-{stop}")


def read_frames(blob: str, i0: int, i1: int, rows: tuple[int, int] | None = None) -> np.ndarray:
    """Volumes i0..i1-1 (0-based) of one plane file, as float32; optionally only rows r0..r1-1."""
    if rows is None:
        buf = _get(blob, DATA_OFFSET + i0 * FRAME_BYTES, DATA_OFFSET + i1 * FRAME_BYTES)
        x = np.frombuffer(buf, "<f8").reshape(i1 - i0, NX, NX)
    else:
        r0, r1 = rows
        x = np.stack([np.frombuffer(_get(blob, DATA_OFFSET + i * FRAME_BYTES + r0 * NX * 8,
                                         DATA_OFFSET + i * FRAME_BYTES + r1 * NX * 8), "<f8")
                      .reshape(r1 - r0, NX) for i in range(i0, i1)])
    if not (np.isfinite(x).all() and x.min() >= 0 and x.max() <= DETECTOR_MAX and (x == np.round(x)).all()):
        raise ValueError(f"{blob}: values outside the detector's integer range; wrong offset?")
    return x.astype(np.float32)


def file_metadata(blob: str) -> dict:
    """What a file says about itself, read with h5py (and the data's byte offset)."""
    with open_nwb(blob) as f:
        ts = f["acquisition/TwoPhotonSeries1"]
        d = ts["data"]
        plane = list(f["general/optophysiology"].values())[0]
        s = f["general/subject"]
        return {
            "shape": d.shape, "dtype": str(d.dtype), "chunks": d.chunks, "compression": d.compression,
            "offset": d.id.get_offset(), "unit": d.attrs["unit"],
            "starting_time": float(ts["starting_time"][()]),
            "imaging_rate": float(plane["imaging_rate"][()]),
            "grid_spacing": tuple(plane["grid_spacing"][()]),
            "location": plane["location"][()].decode(),
            "series_description": ts.attrs["description"],
            "experiment_description": f["general/experiment_description"][()].decode(),
            "age": s["age"][()].decode(), "subject_id": s["subject_id"][()].decode(),
            "strain": s["strain"][()].decode(),
        }


# --- per-plane peak maps (M1) ----------------------------------------------------------------

# ImageJ "Minimum" radius 2: RankFilters takes the pixels with dx^2 + dy^2 <= r^2 + 1, 21 pixels
DISC2 = (np.mgrid[-2:3, -2:3] ** 2).sum(0) <= 2 ** 2 + 1


def _bin(x: np.ndarray, k: int) -> np.ndarray:
    return x.reshape(x.shape[0] // k, k, x.shape[1] // k, k).mean((1, 3))


def _shift(ref_f: np.ndarray, img: np.ndarray) -> tuple[int, int]:
    c = np.fft.ifft2(ref_f * np.conj(np.fft.fft2(img))).real
    i, j = np.unravel_index(np.argmax(c), c.shape)
    n, m = c.shape
    return (i - n if i > n // 2 else i), (j - m if j > m // 2 else j)


def _ratio(a, b):
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(b > 0, a / np.where(b > 0, b, 1), 0.0)


def plane_maps(blob: str, keep_frames: bool = False) -> dict:
    """M1 for one plane of one trial: the stabilized peak fold change map, minimum-filtered (full
    resolution) and Gaussian-blurred (binned), and the baseline F0 (binned)."""
    x = np.concatenate([read_frames(blob, 0, 5), read_frames(blob, 8, 14)] +
                       ([read_frames(blob, 7, 8)] if keep_frames else []))
    small = np.stack([_bin(f, 2) for f in x])
    ref = np.fft.fft2(small[:5].mean(0))
    shifts = [_shift(ref, s) for s in small]
    x = np.stack([np.roll(f, (2 * a, 2 * b), (0, 1)) for f, (a, b) in zip(x, shifts)])
    f0 = x[:5].mean(0)
    fp = x[5:11].mean(0)
    dff = _ratio(fp - f0, f0)
    blur = _ratio(ndimage.gaussian_filter(fp, 1.0) - ndimage.gaussian_filter(f0, 1.0),
                  ndimage.gaussian_filter(f0, 1.0))
    mn = ndimage.minimum_filter(dff, footprint=DISC2)
    return {"min": mn.astype(np.float32), "blur": _bin(blur, BIN).astype(np.float32),
            "f0": _bin(f0, BIN).astype(np.float32),
            "max_shift": int(2 * max(max(abs(a), abs(b)) for a, b in shifts)),
            "saturated": float((x[:5] >= DETECTOR_MAX).mean()),
            "frames": (np.stack([_bin(f, BIN) for f in np.concatenate([x[:5], x[11:]])]).astype(np.float16)
                       if keep_frames else None)}


def trial_maps(trial_rows: pd.DataFrame, workers: int = 24, progress=None, keep_frames: bool = False) -> dict:
    """M1 for many trials. Returns, keyed by trial index: the full-resolution max projection of the
    minimum-filtered maps clipped to [-1, 4] ("proj"), the plane of each pixel's maximum ("argmax",
    binned), per-plane binned minimum-filtered maps ("planes"), Gaussian-blurred maps ("blur"),
    baseline F0 ("f0"), the largest frame shift and the fraction of saturated baseline pixels; with
    keep_frames, also the binned raw volumes 1-5 and 8 of every plane ("frames"), for the first
    volume after the 5 s pulse (8.4 s)."""
    jobs = [(idx, p, b) for idx, r in trial_rows.iterrows() for p, b in enumerate(r.blobs)]
    out = {idx: {"proj": np.full((NX, NX), -np.inf, np.float32),
                 "planes": np.zeros((N_PLANES, NX // BIN, NX // BIN), np.float32),
                 "blur": np.zeros((N_PLANES, NX // BIN, NX // BIN), np.float32),
                 "f0": np.zeros((N_PLANES, NX // BIN, NX // BIN), np.float32),
                 "shift": np.zeros(N_PLANES, int), "saturated": np.zeros(N_PLANES),
                 "frames": (np.zeros((N_PLANES, 6, NX // BIN, NX // BIN), np.float16) if keep_frames else None)}
           for idx in trial_rows.index}
    lock = threading.Lock()
    done = [0]

    def work(job):
        idx, p, b = job
        m = plane_maps(b, keep_frames)
        with lock:
            o = out[idx]
            np.maximum(o["proj"], m["min"], out=o["proj"])
            o["planes"][p] = _bin(m["min"], BIN)
            o["blur"][p] = m["blur"]
            o["f0"][p] = m["f0"]
            o["shift"][p] = m["max_shift"]
            o["saturated"][p] = m["saturated"]
            if keep_frames:
                o["frames"][p] = m["frames"]
            done[0] += 1
            if progress and done[0] % 500 == 0:
                progress(done[0], len(jobs))

    with ThreadPoolExecutor(workers) as ex:
        list(ex.map(work, jobs))
    for o in out.values():
        o["proj"] = np.clip(o["proj"], *CLIP)
        o["argmax"] = o["planes"].argmax(0)
    return out


# --- ROIs and counts (M2) --------------------------------------------------------------------

def _split_wide(mask: np.ndarray, value: np.ndarray, reading: str, pixel_um: float = PIXEL_UM) -> list[np.ndarray]:
    """Connected regions of a mask; under reading b, drop those under 10 um across and split those
    over 20 um at local maxima at least 10 um apart (watershed on the value map)."""
    lab, n = ndimage.label(mask)
    regions = []
    for k in range(1, n + 1):
        reg = lab == k
        diam = 2 * np.sqrt(reg.sum() / np.pi) * pixel_um * BIN
        if reading == "a":
            regions.append(reg)
            continue
        if diam < GLOM_MIN_UM:
            continue
        if diam <= GLOM_MAX_UM:
            regions.append(reg)
            continue
        v = np.where(reg, value, -np.inf)
        size = int(round(GLOM_MIN_UM / pixel_um / BIN))
        peaks = (v == ndimage.maximum_filter(v, size=size)) & reg
        markers, nm = ndimage.label(peaks)
        if nm <= 1:
            regions.append(reg)
            continue
        from skimage.segmentation import watershed
        ws = watershed(-np.where(reg, value, 0), markers, mask=reg)
        for j in range(1, nm + 1):
            sub = ws == j
            if 2 * np.sqrt(sub.sum() / np.pi) * pixel_um * BIN >= GLOM_MIN_UM:
                regions.append(sub)
    return regions


def al_mask(maps: dict, index) -> np.ndarray:
    """The antennal lobe in binned pixels: the baseline fluorescence (maximum over planes, mean over
    the trials given) above Otsu's threshold on its logarithm, its largest connected region with holes filled. A
    standard choice, used to keep ROIs inside the AL; the Methods drew ROIs by eye on the AL."""
    from skimage.filters import threshold_otsu
    f0 = np.mean([maps[i]["f0"].max(0) for i in index], axis=0)
    lab, n = ndimage.label(np.log1p(f0) > threshold_otsu(np.log1p(f0)))
    if n == 0:
        return np.ones_like(f0, bool)
    big = 1 + int(np.argmax(ndimage.sum(np.ones_like(f0), lab, range(1, n + 1))))
    return ndimage.binary_fill_holes(lab == big)


def recurring_regions(proj: np.ndarray, mask_al: np.ndarray | None = None) -> np.ndarray:
    """Claims file, M2 drawing (a): the connected regions of at least 0.2 in each trial's map (inside
    the AL mask), kept when they recur in another trial of the same odor; returns the union of the
    kept regions. A region recurs when it and a region of another trial overlap by at least
    MERGE_OVERLAP (half) of the smaller of the two, the same rule as for one glomerulus responding to
    two odors (an assumption: the claims file does not say how much overlap makes a recurrence)."""
    labs = []
    for p in proj:
        m = p >= THRESHOLD
        if mask_al is not None:
            m = m & mask_al
        lab, n = ndimage.label(m)
        labs.append((lab, n, np.bincount(lab.ravel(), minlength=n + 1)))
    keep = np.zeros(proj.shape[1:], bool)
    for t, (lab, n, sizes) in enumerate(labs):
        if n == 0:
            continue
        kept = np.zeros(n + 1, bool)
        for u, (lab2, n2, sizes2) in enumerate(labs):
            if u == t or n2 == 0:
                continue
            both = (lab > 0) & (lab2 > 0)
            cnt = np.bincount(lab[both].astype(np.int64) * (n2 + 1) + lab2[both],
                              minlength=(n + 1) * (n2 + 1)).reshape(n + 1, n2 + 1)
            smaller = np.minimum(sizes[:, None], sizes2[None, :])
            kept |= ((cnt > 0) & (cnt >= MERGE_OVERLAP * smaller)).any(1)
        kept[0] = False
        keep |= kept[lab]
    return keep


def draw_rois(maps: dict, trial_rows: pd.DataFrame, reading: str, mask_al: np.ndarray | None = None,
              pixel_um: float = PIXEL_UM) -> list[dict]:
    """ROIs for one ant, drawn on the trials given (one concentration per odor). For each odor with at
    least two trials, the regions of at least 0.2 in its trials' max projections that recur in two
    trials (`recurring_regions`), inside the AL mask (Methods: "every glomerular region that responded
    to any odor in at least two trials"), form connected regions; under reading "b" they are filtered
    and split by size (`_split_wide`). Each region has a depth, the plane of its largest trial-mean response to its own
    odor. Regions of different odors that overlap at the same depth (`same_depth`) are one glomerulus
    and share a `group`; overlaps at different depths stay separate (Methods). Regions overlap when
    at least MERGE_OVERLAP (half) of the smaller lies in the larger, an assumption: adjacent
    glomeruli (PGb and 6G are 13 um apart) touch in the thresholded maps without being one."""
    regs = []
    for odor, g in trial_rows.groupby("odor"):
        if len(g) < 2:
            continue
        proj = np.stack([_bin(maps[i]["proj"], BIN) for i in g.index])
        mask = recurring_regions(proj, mask_al)
        mean_planes = np.mean([maps[i]["planes"] for i in g.index], axis=0)
        for reg in _split_wide(mask, proj.mean(0), reading, pixel_um):
            regs.append({"mask": reg, "odor": odor, "depth": int(np.argmax(mean_planes[:, reg].mean(1))),
                         "centroid": ndimage.center_of_mass(reg)})
    parent = list(range(len(regs)))

    def find(k):
        while parent[k] != k:
            parent[k] = parent[parent[k]]
            k = parent[k]
        return k
    for a in range(len(regs)):
        for b in range(a + 1, len(regs)):
            inter = (regs[a]["mask"] & regs[b]["mask"]).sum()
            smaller = min(regs[a]["mask"].sum(), regs[b]["mask"].sum())
            if regs[a]["odor"] != regs[b]["odor"] and inter >= MERGE_OVERLAP * smaller \
                    and abs(regs[a]["depth"] - regs[b]["depth"]) <= SAME_DEPTH_PLANES:
                parent[find(b)] = find(a)
    roots = sorted({find(k) for k in range(len(regs))})
    for k, r in enumerate(regs):
        r["group"] = roots.index(find(k))
    return regs


def n_groups(rois: list[dict]) -> int:
    return 1 + max((r["group"] for r in rois), default=-1)


def roi_values(maps: dict, rois: list[dict], idx) -> tuple[np.ndarray, np.ndarray]:
    """Values of each ROI region in one trial's max projection: (i) mean, (ii) maximum."""
    proj = _bin(maps[idx]["proj"], BIN)
    vi = np.array([proj[r["mask"]].mean() for r in rois])
    vii = np.array([proj[r["mask"]].max() for r in rois])
    return vi, vii


def responding(maps: dict, rois: list[dict], trial_index, value: str, counting: str):
    """Which glomeruli (ROI groups) respond to a set of trials of one odor and concentration, and
    how many. A group responds when any of its regions does. Counting "x": a region responds when
    its value, averaged over the trials, is at least 0.2 (Methods). Counting "y": the per-trial
    count of responding groups, averaged over trials (Figure S5 legend); the boolean returned
    under "y" marks groups responding in at least half of the trials."""
    ng = n_groups(rois)
    if ng == 0 or len(trial_index) == 0:
        return np.zeros(ng, bool), 0.0
    vals = np.array([roi_values(maps, rois, i)[0 if value == "i" else 1] for i in trial_index])
    groups = np.array([r["group"] for r in rois])

    def to_groups(region_bool):
        out = np.zeros(ng, bool)
        np.logical_or.at(out, groups, region_bool)
        return out
    if counting == "x":
        resp = to_groups(vals.mean(0) >= THRESHOLD)
        return resp, float(resp.sum())
    per_trial = np.array([to_groups(v >= THRESHOLD) for v in vals])
    return per_trial.mean(0) >= 0.5, float(per_trial.sum(1).mean())


def group_depths(maps: dict, rois: list[dict], trial_index) -> np.ndarray:
    """Per group, the plane of its largest trial-mean response for a set of trials (over the
    union of its regions)."""
    mean_planes = np.mean([maps[i]["planes"] for i in trial_index], axis=0)
    out = []
    for gi in range(n_groups(rois)):
        m = np.logical_or.reduce([r["mask"] for r in rois if r["group"] == gi])
        out.append(int(np.argmax(mean_planes[:, m].mean(1))))
    return np.array(out)


READINGS = [(d, v, c) for d in "ab" for v in ("i", "ii") for c in "xy"]


# --- single glomeruli (M3) -------------------------------------------------------------------

def disc_mask(center_rc: tuple[float, float], rows: tuple[int, int], diameter_um: float = DISC_UM):
    rr, cc = np.mgrid[rows[0]:rows[1], 0:NX]
    return np.hypot(rr - center_rc[0], cc - center_rc[1]) <= diameter_um / PIXEL_UM / 2


def band_stacks(jobs: list[tuple], workers: int = 32) -> dict:
    """Read, for each job (key, blob, n_volumes, rows), every volume of the row band of one plane."""
    def work(job):
        key, blob, nvol, rows = job
        return key, read_frames(blob, 0, nvol, rows)
    with ThreadPoolExecutor(workers) as ex:
        return dict(ex.map(work, jobs))


def m3_trace(stacks: list[np.ndarray], mask: np.ndarray) -> np.ndarray:
    """dF/F0 of a disc ROI on the per-volume maximum over three adjacent planes."""
    proj = np.maximum.reduce(stacks)
    f = proj[:, mask].mean(1)
    f0 = f[BASE].mean()
    return (f - f0) / f0


def peak_fold_change(trace: np.ndarray) -> float:
    return float(trace[PEAK].mean())


def onset_and_max(trace: np.ndarray, t: np.ndarray):
    """Onset latency and time to maximum from stimulus start (s), or (nan, nan) when the trace never
    exceeds baseline mean + 3 SD (Methods)."""
    base = trace[BASE]
    bound = base.mean() + 3 * base.std(ddof=1)
    after = np.where((t >= STIM_ON_S) & (trace > bound))[0]
    if len(after) == 0:
        return np.nan, np.nan
    post = t >= STIM_ON_S
    imax = np.where(post)[0][np.argmax(trace[post])]
    return float(t[after[0]] - STIM_ON_S), float(t[imax] - STIM_ON_S)


def same_depth(d1, d2) -> np.ndarray:
    """Responses of one ROI to two odors are one glomerulus when their depths are within
    SAME_DEPTH_PLANES planes, and different glomeruli otherwise (Methods)."""
    return np.abs(np.asarray(d1) - np.asarray(d2)) <= SAME_DEPTH_PLANES


# --- focal glomeruli (M4) and their traces (M3) ----------------------------------------------

def to_full(c_binned: tuple[float, float]) -> tuple[float, float]:
    """A binned-pixel coordinate in full-resolution pixels."""
    return tuple((np.asarray(c_binned) + 0.5) * BIN - 0.5)


def group_masks(rois: list[dict]) -> list[np.ndarray]:
    return [np.logical_or.reduce([r["mask"] for r in rois if r["group"] == g]) for g in range(n_groups(rois))]


def offsets_um(origin_rc, other_rc) -> tuple[float, float]:
    """(anterior, lateral) offset of `other` from `origin` in um. The files say "up is lateral, right
    is anterior": lateral is decreasing row, anterior increasing column."""
    return ((other_rc[1] - origin_rc[1]) * PIXEL_UM, (origin_rc[0] - other_rc[0]) * PIXEL_UM)


def identify_focal(maps: dict, rois: list[dict], hi: pd.DataFrame, value: str = "i", counting: str = "x",
                   adjacent_um: float = GLOM_MAX_UM) -> dict:
    """PGb, 6G and PGa among one ant's ROI groups at its higher concentration (claims file, M4).
    PGb: responds to heptanone, heptanol and hexanol at the same depth (the strongest such group if
    several). 6G: responds to 6MHO, lateral to PGb, centres within `adjacent_um` (adjacent: two
    touching glomeruli of at most 20 um have centres at most 20 um apart). PGa: responds to heptanol
    and hexanol, anterior to PGb and adjacent; a heptanone response only breaks a tie, then the
    nearest. Returns group ids (or None), full-resolution centroids and depths."""
    resp = {od: responding(maps, rois, hi[hi.odor == od].index, value, counting)[0] for od in PHEROMONES}
    dep = {od: group_depths(maps, rois, hi[hi.odor == od].index) for od in PHEROMONES}
    masks = group_masks(rois)
    cents = [to_full(ndimage.center_of_mass(m)) for m in masks]
    strength = np.zeros(len(masks))
    for od in ("heptanone", "heptanol", "hexanol"):
        for i in hi[hi.odor == od].index:
            proj = _bin(maps[i]["proj"], BIN)
            strength += np.array([proj[m].mean() for m in masks])
    out = {"PGb": None, "6G": None, "PGa": None, "centroid": {}, "depth": {}, "n_pgb_candidates": 0}
    cand = [g for g in range(len(masks)) if resp["heptanone"][g] and resp["heptanol"][g] and resp["hexanol"][g]
            and same_depth(dep["heptanone"][g], dep["heptanol"][g]) and same_depth(dep["heptanone"][g], dep["hexanol"][g])]
    out["n_pgb_candidates"] = len(cand)
    if not cand:
        return out
    pgb = max(cand, key=lambda g: strength[g])
    out["PGb"] = pgb

    def near(g):
        a, lat = offsets_um(cents[pgb], cents[g])
        return a, lat, float(np.hypot(a, lat))
    six = [g for g in range(len(masks)) if g != pgb and resp["6MHO"][g] and near(g)[1] > 0 and near(g)[2] <= adjacent_um]
    if six:
        out["6G"] = min(six, key=lambda g: near(g)[2])
    pga = [g for g in range(len(masks)) if g not in (pgb, out["6G"]) and resp["heptanol"][g] and resp["hexanol"][g]
           and near(g)[0] > 0 and near(g)[2] <= adjacent_um]
    if pga:
        out["PGa"] = min(pga, key=lambda g: (not resp["heptanone"][g], near(g)[2]))
    for name in ("PGb", "6G", "PGa"):
        g = out[name]
        if g is not None:
            out["centroid"][name] = cents[g]
            od = {"PGb": "heptanone", "6G": "6MHO", "PGa": "heptanol"}[name]
            out["depth"][name] = int(dep[od][g])
    return out


def band_for(centres: list[tuple[float, float]], margin_um: float = 20.0) -> tuple[int, int]:
    """Rows from `margin_um` above the highest centre to as far below the lowest, an even number of
    rows (for 2 x 2 binning in the stabilization). The margin (20 um) leaves room for the disc
    (7.5 um radius) and for shifts up to 12.5 um (43 pixels) before rows rolled in from the other
    edge of the band reach the disc; the largest shift measured in the maps is 42 pixels."""
    rows = [c[0] for c in centres]
    m = margin_um / PIXEL_UM
    r0, r1 = max(0, int(min(rows) - m)), min(NX, int(np.ceil(max(rows) + m)))
    if (r1 - r0) % 2:
        r1, r0 = (r1 + 1, r0) if r1 < NX else (r1, r0 - 1)
    return r0, r1


def stabilize_band(x: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Align each volume of one plane's row band to the mean of its baseline volumes, as
    `plane_maps` does for whole frames (phase correlation on 2 x 2 binned images, whole-pixel
    translation in steps of 2 pixels). Returns the aligned band and the shifts (rows, columns)."""
    small = np.stack([_bin(f, 2) for f in x])
    ref = np.fft.fft2(small[BASE].mean(0))
    shifts = 2 * np.array([_shift(ref, s_) for s_ in small])
    return np.stack([np.roll(f, tuple(int(v) for v in sh), (0, 1)) for f, sh in zip(x, shifts)]), shifts


def region_roi(stacks: list[np.ndarray], disc: np.ndarray, near: np.ndarray) -> np.ndarray:
    """The claims file's second M3 ROI: the region of at least 0.2 at the centre. On the peak fold
    change map of the three-plane maximum (minimum-filtered as in M1), the connected region of at
    least 0.2 within `near` that overlaps the disc most; the disc itself when no pixel of the disc is
    at least 0.2 (a trial without a response there)."""
    proj = np.maximum.reduce(stacks)
    f0 = proj[BASE].mean(0)
    pk = ndimage.minimum_filter(_ratio(proj[PEAK].mean(0) - f0, f0), footprint=DISC2)
    lab, n = ndimage.label((pk >= THRESHOLD) & near)
    if n == 0:
        return disc
    ov = np.bincount(lab[disc], minlength=n + 1)
    ov[0] = 0
    return lab == int(np.argmax(ov)) if ov.max() > 0 else disc


def trial_m3(blobs: list[str], nvol: int, rows: tuple[int, int], focals: dict[str, dict], window: int = 1) -> dict:
    """M3 for one trial, for one or more identifications of the focal glomeruli (`focals`, keyed by
    the M2 reading that identified them). For each glomerulus, the centre plane is chosen (a) where
    the glomerulus's area of at least 0.2 (peak fold change, within 20 um of its centre) is largest,
    or (b) where the disc's peak fold change is highest, among its higher-concentration depth +-
    `window` planes. The ROI is the 15 um disc ("disc") or the region of at least 0.2 at the centre
    ("region", `region_roi`), the two ROIs the claims file names. Each plane's band is stabilized
    (`stabilize_band`), the M3 reading of the claims file; the disc trace without stabilization is
    kept ("raw") to show what stabilization changes. Reads the needed planes as row bands, all
    volumes."""
    planes = sorted({p for f in focals.values() for d in f["depth"].values()
                     for p in range(d - window - 1, d + window + 2) if 0 <= p < N_PLANES})
    raw = band_stacks([(p, blobs[p], nvol, rows) for p in planes], workers=8)
    stab, shifts = {}, {}
    for p, x in raw.items():
        stab[p], shifts[p] = stabilize_band(x)
    out = {"_shift": shifts}
    for label, focal in focals.items():
        res_f = {}
        for name, d in focal["depth"].items():
            c = focal["centroid"][name]
            disc = disc_mask(c, rows)
            near = disc_mask(c, rows, 20.0 + DISC_UM)
            best = {}
            for p in range(d - window, d + window + 1):
                if p not in stab:
                    continue
                x = stab[p]
                f0 = x[BASE].mean(0)
                pk = _ratio(x[PEAK].mean(0) - f0, f0)
                area = int((pk[near] >= THRESHOLD).sum())
                disc_pk = float(_ratio(x[PEAK][:, disc].mean() - x[BASE][:, disc].mean(), x[BASE][:, disc].mean()))
                best[p] = (area, disc_pk)
            res = {}
            for rd, key in (("a", 0), ("b", 1)):
                p = max(best, key=lambda q: (best[q][key], -abs(q - d)))
                qs = [q for q in (p - 1, p, p + 1) if q in stab]
                three = [stab[q] for q in qs]
                reg = region_roi(three, disc, near)
                for roi_name, m in (("disc", disc), ("region", reg)):
                    tr = m3_trace(three, m)
                    res[rd, roi_name] = {"plane": p, "trace": tr, "peak": peak_fold_change(tr),
                                         "roi_px": int(m.sum())}
                if rd == "b":
                    tr = m3_trace([raw[q] for q in qs], disc)
                    res["b", "raw"] = {"plane": p, "trace": tr, "peak": peak_fold_change(tr), "roi_px": int(disc.sum())}
            res_f[name] = res
        out[label] = res_f
    return out
