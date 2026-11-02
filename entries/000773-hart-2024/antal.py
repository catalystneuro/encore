"""Loading and measures for the antennal lobe calcium imaging of dandiset 000773.

Hart, Lopes, Frank & Kronauer (2024), Pheromone representation in the ant antennal lobe changes
with age, Current Biology 34, 3233. doi:10.1016/j.cub.2024.05.031.

Each NWB file of the dandiset holds one Z-plane of one odor trial of one ant: 40 frames (volumes)
of 512 x 512 raw fluorescence, stored as an uncompressed, contiguous float64 array. An ant has 22
trials (the seven odors three times and one paraffin oil trial) of 33 planes, 726 files. Files are
streamed from the archive at the pinned version with HTTP range requests on the public S3 blob
of each asset, which read only the frames needed; nothing is written to disk. The byte offset of
the array in the file is read with h5py for a sample of files (`check_offsets`), and the values
read by range are compared with h5py's on those files.

Where the parameters come from (claims file claims/000773/10.1016-j.cub.2024.05.031.yaml, its
shared methods, which quote the STAR Methods, "Image processing", and the macro
macro_calcium_imaging.txt of doi:10.5281/zenodo.11151724):

- Fold change (F - F0) / F0 with F0 the mean of frames 1 to 5; peak fold change, the mean fold
  change over frames 9 to 14 (Methods: "subtracting the baseline (the average of frames 1-5 ...)
  ... averaging fluorescence fold change from frames 9-14"). Frames here are numbered from 1.
- A 2-pixel minimum filter on each plane, a maximum projection through the Z-planes, and values
  clipped to [-1, 4] (Methods). The kernel of ImageJ's Minimum filter of radius 2 is the set of
  offsets with dx^2 + dy^2 <= r^2 + 1 (ImageJ RankFilters), 21 pixels; this is used here.
- Stabilisation. The paper uses the ImageJ Image Stabilizer (translation). Here each frame read
  is aligned to the mean of frames 1 to 5 of its plane by phase correlation, to the whole pixel,
  a standard stand-in for the plugin; the shifts are returned so that the amount of motion can
  be shown. Traces of focal glomeruli (all 40 frames, read for a small ROI) are stabilised with
  one set of shifts per trial, measured on all 40 frames of the middle plane (`trial_shifts`),
  as the full frames of every plane are not read for them (a deviation from per-plane
  stabilisation).
- Glomerulus AUC: the Z-plane through the glomerulus centre and the planes directly above and
  below, a maximum projection of the three, fold change as above, and the sum over frames 6 to
  40 (Methods). Two readings of the fold change (claims file): (a) the ROI mean of the projected
  raw signal turned into fold change, (b) fold change per pixel, then the ROI mean.
- ROI size for a focal glomerulus: the paper gives none. A disk of radius `ROI_RADIUS` pixels
  (8 px, 2.3 um at 0.289 um per pixel) is a standard choice; the notebook shows other radii.
"""

from __future__ import annotations

import io
import json
import re
import threading
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

import numpy as np
import pandas as pd
import requests
from scipy import ndimage

DANDISET_ID = "000773"
DANDISET_VERSION = "0.261004.1511"
# The earlier study's 90-day-old ants (Hart et al. 2023, Cell 186, 3079), named in the paper's key
# resources table; used for reading (a) of fig3d-pg-60-vs-90-days-same. Latest published version.
OLD_DANDISET = ("000467", "0.261004.1655")
API = "https://api.dandiarchive.org/api"
S3 = "https://dandiarchive.s3.amazonaws.com/blobs"

N_FRAMES, NY, NX = 40, 512, 512
FRAME_BYTES = NY * NX * 8
DATA_OFFSET = 3464            # byte offset of the data array, checked by check_offsets()
BASE = slice(0, 5)            # frames 1-5
PEAK = slice(8, 14)           # frames 9-14
AUC = slice(5, 40)            # frames 6-40
CLIP = (-1.0, 4.0)
ROI_RADIUS = 8
BLOCK = 4                     # block size of the per-plane maps kept for locating glomeruli

ODORS = ["4-methyl-3-heptanone", "4-methyl-3-heptanol", "3-hexanone", "isopropanol",
         "ethylpyrazine", "ethanol", "propionic-acid"]
ALARM = ODORS[:2]
GENERAL = ODORS[2:]

# The supplement of the paper, PMC Open Access version PMC11265976.1 (MD5 in the notebook).
PMC = "https://pmc-oa-opendata.s3.amazonaws.com/PMC11265976.1"
DATA_S1 = PMC + "/NIHMS1997610-supplement-MMC2.csv"
DATA_S2 = PMC + "/NIHMS1997610-supplement-MMC3.xlsx"
DATA_S1_MD5 = "22496279f60217c8781b673e82fb8ac7"
DATA_S2_MD5 = "54ff6698bf2b80098376d60ed3af467d"

_local = threading.local()


def _session():
    if not hasattr(_local, "s"):
        s = requests.Session()
        s.mount("https://", requests.adapters.HTTPAdapter(pool_connections=8, pool_maxsize=8,
                                                          max_retries=5))
        _local.s = s
    return _local.s


def _get(url, rng=None, tries=6):
    headers = {"Range": f"bytes={rng[0]}-{rng[1] - 1}"} if rng else {}
    for k in range(tries):
        try:
            r = _session().get(url, headers=headers, timeout=120)
            r.raise_for_status()
            if rng and len(r.content) != rng[1] - rng[0]:
                raise IOError("short read")
            return r.content
        except Exception:
            if k == tries - 1:
                raise
            time.sleep(1 + 2 * k)


def blob_url(blob):
    return f"{S3}/{blob[:3]}/{blob[3:6]}/{blob}"


# ---------------------------------------------------------------- assets

_NAME = re.compile(r"sub-(?P<sub>[^_/]+)_ses-m(?P<m>\d+)-d(?P<d>\d+)-y(?P<y>\d+)-ant(?P<ant>\d+)-"
                   r"(?P<conc>[\d-]+)x-(?P<odor>.+)-(?P<frames>\d+)-t(?P<t>\d+)-z(?P<z>\d+)um_ophys\.nwb$")


def list_assets(dandiset_id=DANDISET_ID, version=DANDISET_VERSION):
    """Every asset of the pinned version, with ant, concentration, odor, trial number and plane
    parsed from its path. The 90-day ants of Hart et al. 2023 (DANDI 000467, `OLD_DANDISET`) use
    the same layout and names."""
    url = f"{API}/dandisets/{dandiset_id}/versions/{version}/assets/?page_size=1000"
    rows = []
    while url:
        r = _session().get(url, timeout=120).json()
        for a in r["results"]:
            m = _NAME.search(a["path"].split("/")[-1])
            rows.append({"path": a["path"], "asset_id": a["asset_id"], "blob": a["blob"],
                         "size": a["size"], **({k: m.group(k) for k in _NAME.groupindex} if m else {})})
        url = r["next"]
    df = pd.DataFrame(rows)
    df["subject"] = df.path.str.split("/").str[0].str.replace("sub-", "", regex=False)
    df["conc"] = df.conc.str.replace("-", ".", regex=False).astype(float)
    df["t"] = df.t.astype(int)
    df["frames"] = df.frames.astype(int)
    df["z"] = df.z.astype(int)
    return df


def nwb_metadata(blob):
    """Subject and acquisition metadata of one file, read with h5py over the network."""
    import h5py
    import remfile
    with h5py.File(remfile.File(blob_url(blob)), "r") as f:
        def s(k):
            v = f[k][()]
            return v.decode() if isinstance(v, bytes) else v
        ts = f["acquisition/TwoPhotonSeries1"]
        plane = list(f["general/optophysiology"].keys())[0]
        ip = f["general/optophysiology"][plane]
        return {"age": s("general/subject/age"), "subject_id": s("general/subject/subject_id"),
                "species": s("general/subject/species"), "session_start": s("session_start_time"),
                "series_description": ts.attrs["description"],
                "unit": ts["data"].attrs["unit"], "shape": ts["data"].shape,
                "dtype": str(ts["data"].dtype), "rate_hz": float(ts["starting_time"].attrs["rate"]),
                "imaging_rate": float(ip["imaging_rate"][()]),
                "grid_spacing_um": list(np.round(ip["grid_spacing"][()], 4)),
                "plane": plane, "offset": ts["data"].id.get_offset(),
                "chunks": ts["data"].chunks, "compression": ts["data"].compression}


def check_offsets(blobs):
    """For each blob, the array's byte offset from h5py and whether frame 1 read by range equals
    frame 1 read by h5py."""
    import h5py
    import remfile
    out = []
    for b in blobs:
        with h5py.File(remfile.File(blob_url(b)), "r") as f:
            d = f["acquisition/TwoPhotonSeries1/data"]
            off = d.id.get_offset()
            ref = d[0]
        x = read_frames(b, 0, 1)[0]
        out.append({"blob": b, "offset": off, "range_equals_h5py": bool(np.array_equal(x, ref))})
    return pd.DataFrame(out)


def read_frames(blob, start, stop, rows=None):
    """Frames start..stop-1 (0-based) of one file, as float64 (n, 512, 512); with rows=(y0, y1),
    only those rows of each frame, one request per frame."""
    url = blob_url(blob)
    if rows is None:
        buf = _get(url, (DATA_OFFSET + start * FRAME_BYTES, DATA_OFFSET + stop * FRAME_BYTES))
        return np.frombuffer(buf, "<f8").reshape(stop - start, NY, NX)
    y0, y1 = rows
    out = np.empty((stop - start, y1 - y0, NX))
    for i, k in enumerate(range(start, stop)):
        a = DATA_OFFSET + k * FRAME_BYTES + y0 * NX * 8
        out[i] = np.frombuffer(_get(url, (a, a + (y1 - y0) * NX * 8)), "<f8").reshape(y1 - y0, NX)
    return out


# ---------------------------------------------------------------- peak maps

def _disk(r2):
    r = int(np.floor(np.sqrt(r2)))
    yy, xx = np.mgrid[-r:r + 1, -r:r + 1]
    return (yy ** 2 + xx ** 2) <= r2


MIN_FOOTPRINT = _disk(2 * 2 + 1)   # ImageJ Minimum, radius 2


def _shift(ref_f, img):
    f = np.fft.rfft2(img)
    r = ref_f * np.conj(f)
    r /= np.abs(r) + 1e-12
    c = np.fft.irfft2(r, s=img.shape)
    dy, dx = np.unravel_index(np.argmax(c), c.shape)
    dy = dy - NY if dy > NY // 2 else dy
    dx = dx - NX if dx > NX // 2 else dx
    return int(dy), int(dx)


MAX_SHIFT = 20   # pixels; a larger phase-correlation peak is taken as a failed estimate, not moved


def _apply(img, dy, dx):
    if (dy == 0 and dx == 0) or max(abs(dy), abs(dx)) > MAX_SHIFT:
        return img
    return ndimage.shift(img, (dy, dx), order=0, mode="nearest")


def plane_maps(blob, stabilise=True):
    """For one plane file: F0 (mean of frames 1-5), the peak fold change (mean over frames 9-14),
    each frame aligned to the F0 image when stabilise, and the size of each frame's shift
    (pixels, the larger of |dy| and |dx|; shifts above MAX_SHIFT are not applied)."""
    b = read_frames(blob, 0, 5).astype(np.float32)
    p = read_frames(blob, 8, 14).astype(np.float32)
    shifts = []
    if stabilise:
        ref = b.mean(0)
        ref_f = np.fft.rfft2(ref - ref.mean())
        bb, pp = [], []
        for src, dst in ((b, bb), (p, pp)):
            for img in src:
                dy, dx = _shift(ref_f, img - img.mean())
                shifts.append(max(abs(dy), abs(dx)))
                dst.append(_apply(img, dy, dx))
        b, p = np.array(bb), np.array(pp)
    f0 = b.mean(0)
    with np.errstate(divide="ignore", invalid="ignore"):
        pk = (p.mean(0) - f0) / f0
    pk = np.nan_to_num(pk, nan=0.0, posinf=CLIP[1], neginf=CLIP[0])
    return f0, pk, shifts


def _block(a, k=BLOCK):
    return a.reshape(a.shape[0] // k, k, a.shape[1] // k, k).mean((1, 3))


def volume_maps(blobs_by_z, keep_planes=False, stabilise=True, threads=12):
    """One trial: blobs ordered by plane. Returns the peak map (minimum filter, maximum
    projection over all planes, clipped), the same without the plane at 0 um (the macro's
    projection), the same without the minimum filter (to show the filter's offset), the maximum
    projection of F0, the shifts, and with keep_planes the per-plane
    peak maps (clipped, before the minimum filter) and F0 in BLOCK x BLOCK means."""
    with ThreadPoolExecutor(threads) as ex:
        res = list(ex.map(lambda b: plane_maps(b, stabilise), blobs_by_z))
    filt = np.array([ndimage.minimum_filter(pk, footprint=MIN_FOOTPRINT, mode="nearest")
                     for _, pk, _ in res])
    out = {"peak": np.clip(filt.max(0), *CLIP).astype(np.float32),
           "peak_no_z0": np.clip(filt[1:].max(0), *CLIP).astype(np.float32),
           "peak_no_min": np.clip(np.array([pk for _, pk, _ in res]).max(0), *CLIP).astype(np.float32),
           "raw_max": np.array([f0 for f0, _, _ in res]).max(0).astype(np.float32),
           "shifts": [s for _, _, s in res]}
    if keep_planes:
        out["planes_peak"] = np.array([_block(np.clip(pk, *CLIP)) for _, pk, _ in res], np.float32)
    return out


def _job(args):
    key, blobs, keep = args
    return key, volume_maps(blobs, keep_planes=keep)


def all_volume_maps(trials, keep_keys=(), processes=4, progress=None):
    """trials: dict key -> blobs ordered by plane. Runs volume_maps over processes."""
    jobs = [(k, b, k in set(keep_keys)) for k, b in trials.items()]
    out = {}
    with ProcessPoolExecutor(processes) as ex:
        for i, (k, r) in enumerate(ex.map(_job, jobs)):
            out[k] = r
            if progress and (i + 1) % progress == 0:
                print(f"  {i + 1} of {len(jobs)} trials", flush=True)
    return out


# ---------------------------------------------------------------- the paper's supplement

def fetch(url, md5=None):
    """Bytes of a supplement file, checked against its MD5."""
    import hashlib
    b = _get(url)
    if md5 and hashlib.md5(b).hexdigest() != md5:
        raise ValueError(f"{url}: MD5 differs from the pinned one")
    return b


_S2_ODOR = {"4-methyl-3-heptanone": "4-methyl-3-heptanone", "4-methyl-3-heptanol": "4-methyl-3-heptanol",
            "3hexanone": "3-hexanone", "isopropanol": "isopropanol", "ethylpyrazine": "ethylpyrazine",
            "ethanol": "ethanol", "propionicacid": "propionic-acid",
            "6m5h2one": "6-methyl-5-hepten-2-one", "4m3hexanol": "4-methyl-3-hexanol"}


def s2_subject(ant):
    """Data S2 ant name (a4-1-18-2023, a4-1-18-23) -> dataset subject (ant4-m1-d18-y2023)."""
    m = re.match(r"a(\d+)[.-](\d+)[.-](\d+)[.-](\d+)$", ant)
    if not m:
        return None
    a, mo, d, y = m.groups()
    y = "20" + y if len(y) == 2 else y
    return f"ant{a}-m{int(mo)}-d{int(d)}-y{y}"


def load_data_s2(raw):
    """Data S2 (per-glomerulus fold-change traces) as a long table, with the dataset subject, the
    odor named as in the dataset, the repeat number `rep` (1-3) and the frame number (1-40)."""
    d = pd.read_excel(io.BytesIO(raw))
    d["subject"] = d.ant.map(s2_subject)
    # Data S2 holds two quantifications of the same ants: names with a two-digit year
    # (a4-1-18-23) carry the PGb and PGa alarm traces of Figure 3C and 3D; names with a four-digit
    # year carry G1-G4 for all odors and PGb and PGa for the general odorants (Figures 3B, 4, S2,
    # S4). They may use different planes or ROIs; the notebook reports the link for each.
    d["set"] = np.where(d.ant.str.match(r".*[.-]\d{2}$"), "fig3cd", "main")
    d["odor_ds"] = d.odor.map(_S2_ODOR)
    num = d.trial.str.extract(r"\.(\d+)$")[0].astype(int)
    # the trailing number is the repeat (1-3) for most ants; for some 90-day ants it is the trial
    # number of the recording (t), kept as `t_s2`, and the repeat is its rank within the odor
    d["t_s2"] = num.where(num > 3)
    rank = d.assign(num=num).groupby(["ant", "glomerulus", "conc", "odor"]).num.rank(method="dense")
    d["rep"] = np.where(num > 3, rank, num).astype(int)
    d["frame"] = (d["time.s"] / 1.2).round().astype(int)
    d["glomerulus"] = d.glomerulus.str.replace("pgb", "PGb").str.replace("pga", "PGa")
    return d


def trial_table(assets):
    """One row per trial (ant and t number) with its odor, concentration and repeat `rep` (1-3, the
    order of the t numbers of that odor and concentration), and its blobs ordered by plane."""
    a = assets.copy()
    a["odor"] = a.odor.replace({"ethylyprazine": "ethylpyrazine"})
    rows = []
    for (sub, t), g in a.groupby(["subject", "t"]):
        g = g.sort_values("z")
        rows.append({"subject": sub, "t": t, "odor": g.odor.iloc[0], "conc": g.conc.iloc[0], "frames": g.frames.iloc[0],
                     "n_planes": len(g), "z": g.z.tolist(), "blobs": g.blob.tolist()})
    tt = pd.DataFrame(rows)
    tt["rep"] = tt.groupby(["subject", "conc", "odor"]).t.rank().astype(int)
    return tt


# ---------------------------------------------------------------- whole-AL ROI

def al_mask(raw_max, grow=0, sigma=4.0):
    """The AL outline from a maximum projection of raw fluorescence: Gaussian smoothing, Otsu's
    threshold, the largest connected region with holes filled, then grown (grow > 0) or shrunk
    (grow < 0) by |grow| pixels. The paper drew it by hand; this is a standard choice."""
    from skimage.filters import threshold_otsu
    s = ndimage.gaussian_filter(np.log1p(np.clip(raw_max, 0, None)), sigma)
    m = s > threshold_otsu(s)
    lab, n = ndimage.label(m)
    if n > 1:
        sizes = ndimage.sum(m, lab, range(1, n + 1))
        m = lab == (1 + int(np.argmax(sizes)))
    m = ndimage.binary_fill_holes(m)
    if grow > 0:
        m = ndimage.binary_dilation(m, _disk(grow ** 2), border_value=0)
    elif grow < 0:
        m = ndimage.binary_erosion(m, _disk(grow ** 2), border_value=0)
    return m


# ---------------------------------------------------------------- focal glomeruli

def s2_peaks(s2):
    """Per ant, glomerulus and trial of Data S2, the mean fold change over frames 9-14."""
    x = s2[(s2.frame >= 9) & (s2.frame <= 14)]
    return x.groupby(["subject", "glomerulus", "set", "odor_ds", "rep"]).dff.mean().rename("s2_peak").reset_index()


def smooth_planes(planes):
    """The value `locate` searches, for one trial's per-plane peak maps (33, 128, 128): the ROI
    disk in blocks, then the maximum over the plane and its neighbours, so that it is close to the
    ROI measure of the three-plane projection."""
    fp = _disk((ROI_RADIUS / BLOCK) ** 2)
    X = ndimage.uniform_filter(planes, size=(1,) + fp.shape, mode="nearest")
    return ndimage.maximum_filter(X, size=(3, 1, 1), mode="nearest")


def _corr_maps(X, V):
    """Pearson r of each row of V (k, trials) with every voxel of X (trials, z, by, bx)."""
    V = np.atleast_2d(np.asarray(V, float))
    V = (V - V.mean(1, keepdims=True)) / (V.std(1, keepdims=True) + 1e-12)
    Xc = (X - X.mean(0)).reshape(len(X), -1)
    sd = X.std(0).reshape(-1) + 1e-12
    return (V @ Xc) / X.shape[0] / sd                          # k, voxels


def locate(planes_peak, trial_keys, s2_vals, mask=None, smooth=True):
    """Find the voxel (plane, block row, block column) whose per-trial peak fold change best
    correlates (Pearson r) with the Data S2 per-trial peaks of one glomerulus.
    planes_peak: dict trial key -> (33, 128, 128), smoothed already when smooth is False;
    trial_keys and s2_vals aligned; mask (128, 128) restricts the search to the AL."""
    X = np.stack([smooth_planes(planes_peak[k]) if smooth else planes_peak[k] for k in trial_keys])
    r = _corr_maps(X, s2_vals)[0].reshape(X.shape[1:])
    if mask is not None:
        r = np.where(mask[None], r, -np.inf)
    z, by, bx = np.unravel_index(np.argmax(r), r.shape)
    slope = float(np.polyfit(np.asarray(s2_vals, float), X[:, z, by, bx], 1)[0])
    return {"z_index": int(z), "y": int(by * BLOCK + BLOCK // 2), "x": int(bx * BLOCK + BLOCK // 2),
            "r": float(r[z, by, bx]), "slope": slope}


def locate_null(planes_peak, trial_keys, s2_vals, mask=None, n=200, rng=None, smooth=True, odors=None,
                batch=25):
    """Chance level of `locate`: the best r over the same voxels when the Data S2 values are
    shuffled, n times; returns the n maxima. With odors=None the values are shuffled across trials.
    With odors (the odor of each trial), the odors are shuffled as blocks: each trial takes the
    Data S2 value of the same repeat of another odor (the mean of that odor's values when Data S2
    lacks that repeat), so the null keeps the structure of three repeats of an odor and asks whether
    a voxel follows this glomerulus's tuning better than a voxel follows another tuning. A
    placement is above chance when its r exceeds the 95th percentile of the maxima (a standard
    permutation test; the paper gives no placement procedure)."""
    rng = np.random.default_rng(0) if rng is None else rng
    X = np.stack([smooth_planes(planes_peak[k]) if smooth else planes_peak[k] for k in trial_keys]).astype(np.float32)
    v = np.asarray(s2_vals, float)
    keep = np.ones(X.shape[1:], bool) if mask is None else np.broadcast_to(mask[None], X.shape[1:])
    X = X[:, keep]                                             # trials, voxels in the AL
    if odors is not None:
        od = np.asarray(odors)
        names = sorted(set(od))
        rep = np.array([np.sum(od[:i] == o) for i, o in enumerate(od)])
        val = {(o, r): x for o, r, x in zip(od, rep, v)}
        mean = {o: v[od == o].mean() for o in names}

    def draw():
        if odors is None:
            return rng.permutation(v)
        pm = dict(zip(names, rng.permutation(names)))
        return np.array([val.get((pm[o], r), mean[pm[o]]) for o, r in zip(od, rep)])
    out = []
    for i in range(0, n, batch):
        V = np.array([draw() for _ in range(min(batch, n - i))])
        out.append(_corr_maps(X, V).max(1))
    return np.concatenate(out)


SHIFT_PLANE = 16     # the middle plane (80 um) of 33, used to measure motion over all 40 frames


def trial_shifts(blob):
    """Shift (dy, dx) of each of the 40 frames of one plane against the mean of frames 1-5,
    by phase correlation; applied to every plane of the trial for the glomerulus traces. Shifts
    above MAX_SHIFT are set to 0, as in plane_maps."""
    f = read_frames(blob, 0, N_FRAMES).astype(np.float32)
    ref = f[BASE].mean(0)
    ref_f = np.fft.rfft2(ref - ref.mean())
    sh = np.array([_shift(ref_f, img - img.mean()) for img in f])
    sh[np.abs(sh).max(1) > MAX_SHIFT] = 0
    return sh


def _shift_job(b):
    return trial_shifts(b)


def all_trial_shifts(blobs, processes=4):
    with ProcessPoolExecutor(processes) as ex:
        return list(ex.map(_shift_job, blobs))


def roi_trace(blobs_by_z, z_index, y, x, radius=ROI_RADIUS, radii=(), shifts=None, f0_floor=0.0):
    """All 40 frames of the planes z-1, z, z+1 around (y, x), read row by row; the maximum
    projection of the three planes; for each radius, the ROI fold change under reading (a) ROI
    mean of the projected raw signal, then fold change, and (b) fold change per pixel, then the
    ROI mean. The ROI follows the frame's shift (`shifts`, one (dy, dx) per frame, from
    `trial_shifts`), so the frames are stabilised by whole pixels. Under reading (b) a pixel whose
    baseline F0 is at or below f0_floor has no defined fold change and is left out (the notebook
    sets the floor to the ant's background level outside the AL, an assumption: a pixel at
    background level divides by noise); b is NaN when no pixel is left."""
    rr = sorted(set((radius,) + tuple(radii)))
    R = max(rr)
    sh = np.zeros((N_FRAMES, 2), int) if shifts is None else np.asarray(shifts, int)
    pad = int(np.abs(sh).max()) if len(sh) else 0
    pad = min(pad, 24)
    y0, y1 = max(0, y - R - pad), min(NY, y + R + pad + 1)
    zs = [k for k in (z_index - 1, z_index, z_index + 1) if 0 <= k < len(blobs_by_z)]
    stack = np.array([read_frames(blobs_by_z[k], 0, N_FRAMES, rows=(y0, y1)) for k in zs])
    proj = stack.max(0)                                          # frames, rows, NX
    yy, xx = np.mgrid[y0:y1, 0:NX]
    out = {}
    for rad in rr:
        f = []
        for i in range(N_FRAMES):
            dy, dx = (int(np.clip(sh[i, 0], -pad, pad)), int(np.clip(sh[i, 1], -pad, pad)))
            # the frame is aligned by shifting it by (dy, dx): the ROI at (y, x) of the
            # reference sits at (y - dy, x - dx) in the frame
            m = (yy - (y - dy)) ** 2 + (xx - (x - dx)) ** 2 <= rad ** 2
            f.append(proj[i][m])
        n = min(len(v) for v in f)
        f = np.array([v[:n] for v in f])                         # frames, pixels
        fa = f.mean(1)
        a = (fa - fa[BASE].mean()) / fa[BASE].mean()
        f0 = f[BASE].mean(0)
        ok = f0 > max(f0_floor, 0.0)
        with np.errstate(divide="ignore", invalid="ignore"):
            b = ((f[:, ok] - f0[ok]) / f0[ok]).mean(1) if ok.any() else np.full(N_FRAMES, np.nan)
        out[rad] = (a, b)
    return out


def _trace_job(args):
    key, blobs, z, y, x, radius, radii, shifts, floor = args
    return key, roi_trace(blobs, z, y, x, radius, radii, shifts, floor)


def _trace_chunk(args):
    jobs, threads = args
    with ThreadPoolExecutor(threads) as ex:
        return list(ex.map(_trace_job, jobs))


def all_roi_traces(jobs, processes=4, threads=16):
    """jobs: list of (key, blobs_by_z, z_index, y, x, radius, radii, shifts, f0_floor); run over processes, each
    with a pool of threads."""
    chunks = [(jobs[i::processes], threads) for i in range(processes)]
    out = {}
    with ProcessPoolExecutor(processes) as ex:
        for res in ex.map(_trace_chunk, chunks):
            out.update(dict(res))
    return out


# ---------------------------------------------------------------- behaviour (Data S1)

def logistic(x, ym, y0, k):
    """Table S1: Y = YM*Y0/((YM-Y0)*exp(-K*x)+Y0)."""
    return ym * y0 / ((ym - y0) * np.exp(-k * x) + y0)


def quadratic(x, b0, b1, b2):
    return b0 + b1 * x + b2 * x ** 2


def fit(model, x, y, p0):
    """Least squares fit; returns the parameters and the residual sum of squares. The starting
    values are a standard choice (Prism's are not given)."""
    from scipy.optimize import curve_fit
    if model is quadratic:
        p = np.polyfit(x, y, 2)[::-1]
    else:
        p, _ = curve_fit(model, x, y, p0=p0, maxfev=20000)
    return np.asarray(p), float(np.sum((y - model(x, *p)) ** 2))


def extra_ss_test(model, groups, p0):
    """Extra sum-of-squares F test of one shared curve against one curve per group.
    groups: dict name -> (x, y). Returns F, its degrees of freedom, p, and the parameters."""
    from scipy import stats
    x = np.concatenate([g[0] for g in groups.values()])
    y = np.concatenate([g[1] for g in groups.values()])
    k = len(p0)
    p_one, ss_one = fit(model, x, y, p0)
    sep = {n: fit(model, gx, gy, p0) for n, (gx, gy) in groups.items()}
    ss_sep = sum(v[1] for v in sep.values())
    df_sep = len(y) - k * len(groups)
    df_num = k * (len(groups) - 1)
    F = ((ss_one - ss_sep) / df_num) / (ss_sep / df_sep)
    return {"F": F, "df": (df_num, df_sep), "p": float(stats.f.sf(F, df_num, df_sep)),
            "shared": p_one, "separate": {n: v[0] for n, v in sep.items()}}


# ---------------------------------------------------------------- responding ROIs

RESPONSE = 0.2     # Methods: an ROI responds to an odor when its mean peak fold change is >= 0.2


def candidate_rois(maps, mask, diameter, thr=RESPONSE, min_trials=2, sigma=2.0):
    """Glomerulus-sized ROIs from the peak maps of one ant (claims file,
    fig2e-heptanone-breadth-falls: regions of a trial's map at >= thr that recur, overlapping, in
    at least two trials of any odor, split at glomerulus size). Here: in each trial, the local
    maxima of the map (Gaussian smoothing, sigma 2 px) at >= thr inside the AL, at least
    diameter/2 apart; maxima of different trials within diameter/2 of each other are one ROI
    (greedy, strongest first); an ROI found in at least min_trials trials is kept, as a disk of
    the given diameter around the mean position. Returns a list of boolean masks."""
    from skimage.feature import peak_local_max
    pts = []
    for t, m in enumerate(maps):
        sm = ndimage.gaussian_filter(m, sigma)
        for y, x in peak_local_max(np.where(mask, sm, -np.inf), min_distance=max(1, int(diameter // 2)),
                                   threshold_abs=thr, exclude_border=False):
            pts.append((sm[y, x], t, y, x))
    pts.sort(reverse=True)
    clusters = []        # [sum y, sum x, n, set of trials]
    r2 = (diameter / 2) ** 2
    for _, t, y, x in pts:
        for c in clusters:
            cy, cx = c[0] / c[2], c[1] / c[2]
            if (cy - y) ** 2 + (cx - x) ** 2 <= r2:
                c[0] += y; c[1] += x; c[2] += 1; c[3].add(t)
                break
        else:
            clusters.append([y, x, 1, {t}])
    yy, xx = np.mgrid[0:NY, 0:NX]
    rois = []
    for c in clusters:
        if len(c[3]) >= min_trials:
            cy, cx = c[0] / c[2], c[1] / c[2]
            rois.append(((yy - cy) ** 2 + (xx - cx) ** 2) <= r2)
    return rois


def count_responding(maps, odors, rois, thr=RESPONSE):
    """Per odor, the number of ROIs whose mean peak fold change, averaged over the odor's
    trials, is >= thr. maps and odors are aligned lists of trials; rois a list of masks."""
    if not rois:
        return {o: 0 for o in set(odors)}
    vals = np.array([[m[r].mean() for r in rois] for m in maps])               # trials, rois
    od = np.array(odors)
    return {o: int((vals[od == o].mean(0) >= thr).sum()) for o in sorted(set(odors))}
