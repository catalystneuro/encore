"""Loading and measures for SPARC:75 and SPARC:108, the data of Xia et al. (2021), PNAS 118:e2023807118.

Both datasets are read from the public SPARC bucket at their pinned published version (version 1
of each, the only one), through the version's manifest.json and each file's S3 object version.
Files are opened with fsspec and read into memory; nothing is written to disk.

Where the parameters come from:

- Photobleaching correction: a monoexponential decay fit to the trace, each value divided by the
  curve's value (paper, Methods, "Animal Preparation and Imaging": "All data were corrected for
  photobleaching by first constructing a photobleaching curve using monoexponential decay ... then
  dividing by the number extracted from the curve"). Which frames the curve is fit to is open; the
  claims file names (a) the frames outside the response and (b) the whole trace, and both are run.
- dF/F baseline: open; (a) the mean of the frames before onset, (b) the first frame (claims file,
  opening comment).
- Initial rate: open; (a) a linear fit from the first frame after onset to the peak, (b) the slope
  over the first k = 2 to 5 frames after onset (claims file, opening comment).
- Frame interval: the paper gives 0.55 s (Results, "Ex vivo calibration": "within 0.55 s, the
  minimum sampling time used in our experiment"; the times of Fig. 7 are multiples of 0.55 s).
  The per-frame timestamps of the two in vivo files that keep them say 0.50 s. Both are run;
  `FRAME_S_FILE` is the files' value, `FRAME_S_PAPER` the paper's.
- Stimulation onset: 10.45 s, "Sti starts" in Fig. 6A and "Stim starts" in Fig. 7A, which is
  frame 19 on the paper's 0.55 s clock (`STIM_FRAME`). The files do not record it.
- Michaelis-Menten model V = Vmax [ACh] / (Km + [ACh]) (Fig. 4B legend).
- Background for puncta: mean plus 3 SD of the background (claims file, fig3d-sensor-on-soma,
  reading (b)). The background is taken here as the pixels at or below the image's median, a choice
  made here as the paper defines none.
- Cell-sized ROIs: square blocks of `BLOCK` pixels. The paper's ROIs are drawn by hand on one
  ganglion cell (Fig. 5B legend) and their coordinates are not given; the block size is a choice
  made here (about 17 um at an estimated 0.43 um per pixel, the size of an SMG cell body; the
  files carry no spatial scale).
"""

from __future__ import annotations

import base64
import io
import json
import re

import fsspec
import numpy as np
import tifffile
from scipy.optimize import curve_fit

BUCKET = "https://sparc-prod-aod-discover-publish50-use1.s3.amazonaws.com"
DATASETS = {
    "75": {"version": 1, "doi": "10.26275/prjd-jhoc", "manifest": "9A86cPo2rpNmUq4Drjtg5in4NKm0esVP"},
    "108": {"version": 1, "doi": "10.26275/w027-cisv", "manifest": "p7ncbGrUcVs96z5zpw6DMcVGwCP5ktfW"},
}
BLOCK = 2**20

FRAME_S_FILE = 0.50
FRAME_S_PAPER = 0.55
STIM_FRAME = 19          # 10.45 s / 0.55 s, Fig. 6A and Fig. 7A
BLOCK_PX = 40

_manifests: dict = {}
READ: dict = {}          # path -> sha256 (hex) of every file read, for the notebook header

SV = "files/primary/sensor_validation/"
SC = "files/primary/sensor_characterization/"
MOVIES = {
    "sub-2 3V": SV + "sub-2/sub-2 3V.tif",
    "sub-3 8V": SV + "sub-3/sub-3 8V.tif",
    "sub-4 10V": SV + "sub-4/sub-4 10V.tif",
    "sub-6 with drug": SV + "sub-6/sub-6_with drug 3v(00299).tif",
    "sub-6 without drug": SV + "sub-6/sub-6_without drug 3v(00300).tif",
}
CZI_SUB5 = SV + "sub-5/2019-11-01 ACh sensor staining in SMG 02 - Same Thresholds.czi"


def manifest(ds: str) -> dict:
    if ds not in _manifests:
        u = f"{BUCKET}/{ds}/manifest.json?versionId={DATASETS[ds]['manifest']}"
        with fsspec.open(u, block_size=BLOCK) as f:
            _manifests[ds] = json.load(f)
    return _manifests[ds]


def entry(ds: str, path: str) -> dict:
    hits = [f for f in manifest(ds)["files"] if f["path"] == path]
    if len(hits) != 1:
        raise KeyError(f"{path} not in the manifest of {ds}")
    return hits[0]


def url(ds: str, path: str) -> str:
    return f"{BUCKET}/{ds}/{path}?versionId={entry(ds, path)['s3VersionId']}"


def sha_hex(ds: str, path: str) -> str:
    return base64.b64decode(entry(ds, path)["sha256"]).hex()


def read_bytes(ds: str, path: str) -> bytes:
    with fsspec.open(url(ds, path), block_size=BLOCK) as f:
        data = f.read()
    READ[f"{ds}/{path}"] = sha_hex(ds, path)
    return data


def open_file(ds: str, path: str):
    """A ranged-read file handle, for reading only part of a large file."""
    READ[f"{ds}/{path}"] = sha_hex(ds, path)
    return fsspec.open(url(ds, path), block_size=BLOCK).open()


# ---------------------------------------------------------------- in vitro

def hplc(channel: str) -> tuple[np.ndarray, np.ndarray]:
    """One HPLC channel (PHAB, 260_NM, 280_NM, 652_NM): time (min) and signal. UTF-16 text, tab separated."""
    raw = read_bytes("108", f"{SC}HPLC_{channel}.csv")
    text = raw.decode("utf-16") if raw[:2] in (b"\xff\xfe", b"\xfe\xff") else raw.decode()
    a = np.loadtxt(io.StringIO(text))
    return a[:, 0], a[:, 1]


def uvvis(name: str) -> list[dict]:
    """Spectra in a NanoDrop XML workbook: one dict per worksheet with title, time, wavelength, absorbance."""
    text = read_bytes("108", f"{SC}{name}").decode()
    out = []
    for ws in re.findall(r"<Worksheet.*?</Worksheet>", text, re.S):
        rows = re.findall(r"<Row.*?</Row>", ws, re.S)
        wl, ab, title, time = [], [], None, None
        for r in rows[1:]:
            cells = re.findall(r'<Data ss:Type="(\w+)">([^<]*)</Data>', r)
            if len(cells) >= 2 and cells[0][0] == "Number":
                wl.append(float(cells[0][1]))
                ab.append(float(cells[1][1]))
                if title is None and len(cells) >= 4:
                    title, time = cells[2][1], cells[3][1]
        out.append({"title": title, "time": time, "wavelength": np.array(wl), "absorbance": np.array(ab)})
    return out


def gel(channel: str) -> np.ndarray:
    """Gel image 2019-08-09_SENSOR_<channel>.tif (eb, PHAB, AF652) as float."""
    with tifffile.TiffFile(io.BytesIO(read_bytes("108", f"{SC}2019-08-09_SENSOR_{channel}.tif"))) as tf:
        return tf.asarray().astype(float)


# ---------------------------------------------------------------- confocal

def lsm(path: str) -> tuple[np.ndarray, list[str], dict]:
    """An LSM file of SPARC:75: array, dye name per channel (from the scan information), voxel size (um)."""
    with open_file("75", path) as fh:
        tf = tifffile.TiffFile(fh)
        md = tf.lsm_metadata
        arr = tf.series[0].asarray()
        dyes = []
        for tr in md["ScanInformation"]["Tracks"]:
            for d in tr["DetectionChannels"]:
                if d.get("Acquire", 1):
                    dyes.append(d.get("DyeName", "?"))
        vox = {k: md[f"VoxelSize{k}"] * 1e6 for k in "XYZ"}
    return arr, dyes, vox


def czi_sub5(planes: str = "all"):
    """The sub-5 confocal stack (CZI): per channel the maximum projection over z, and the middle plane.

    Reads the file's subblocks one at a time through ranged reads. Returns (max_proj, mid, names,
    scale_um), with arrays indexed [channel, y, x].
    """
    import czifile

    fh = open_file("108", CZI_SUB5)
    cz = czifile.CziFile(fh)
    md = cz.metadata()
    names = re.findall(r"<DyeName>([^<]+)", md)
    scale = {k: float(re.findall(r'<Distance Id="%s">\s*<Value>([^<]+)' % k, md, re.S)[0]) * 1e6 for k in "XYZ"}
    nz = int(re.findall(r"<SizeZ>(\d+)</SizeZ>", md)[0])
    nc = int(re.findall(r"<SizeC>(\d+)</SizeC>", md)[0])
    mid_z = nz // 2
    mx, mid = None, None
    for d in cz.filtered_subblock_directory:
        idx = dict(zip(d.dims, d.start))
        plane = np.squeeze(d.read_segment_data(cz).data())
        if mx is None:
            mx = np.zeros((nc,) + plane.shape, plane.dtype)
            mid = np.zeros_like(mx)
        c = idx.get("C", 0)
        np.maximum(mx[c], plane, out=mx[c])
        if idx.get("Z", 0) == mid_z:
            mid[c] = plane
    fh.close()
    return mx, mid, names, scale, nz


def background_threshold(img: np.ndarray, k: float = 3.0) -> float:
    """Mean plus k SD of the background, the background being the pixels at or below the median."""
    bg = img[img <= np.median(img)]
    return float(bg.mean() + k * bg.std())


# ---------------------------------------------------------------- movies

def _sec(s: str) -> float:
    h, m, x = s.split(":")
    return int(h) * 3600 + int(m) * 60 + float(x)


def movie(key: str) -> dict:
    """An in vivo recording: frames (uint16), per-frame times from the camera (when kept), and halves.

    The camera's 512 x 512 frames hold the two W-VIEW GEMINI channels side by side; files that
    keep both are split into 'left' and 'right' halves. Files cropped to one channel are 'single'.
    """
    raw = read_bytes("108", MOVIES[key])
    tf = tifffile.TiffFile(io.BytesIO(raw))
    a = tf.asarray()
    if tf.imagej_metadata:
        descs = [tf.imagej_metadata.get("Info", "")]
    else:
        descs = [p.description or "" for p in tf.pages]
    times = [_sec(m.group(1)) for m in (re.search(r"Time_From_Start = (\S+)", d) for d in descs) if m]
    tf.close()
    del raw
    stamp = re.search(r"Created by Hamamatsu Inc\.\s*\n?\s*([^\r\n]+)", descs[0]) if descs else None
    out = {"key": key, "shape": a.shape, "times": np.array(times), "acquired": stamp.group(1).strip() if stamp else ""}
    if a.shape[-1] == 512:
        out["halves"] = {"left": a[:, :, :256], "right": a[:, :, 256:]}
    else:
        out["halves"] = {"single": a}
    return out


def tissue_mask(img: np.ndarray) -> np.ndarray:
    """Pixels above Otsu's threshold of the smoothed mean image (the stained tissue)."""
    from scipy.ndimage import gaussian_filter
    from skimage.filters import threshold_otsu

    s = gaussian_filter(img.astype(float), 3)
    return s > threshold_otsu(s)


def blocks(frames: np.ndarray, mask: np.ndarray, size: int = BLOCK_PX, min_cover: float = 0.8):
    """Mean trace of each size x size block whose pixels are mostly in the mask: (traces, origins)."""
    n, h, w = frames.shape
    tr, org = [], []
    for y in range(0, h - size + 1, size):
        for x in range(0, w - size + 1, size):
            if mask[y:y + size, x:x + size].mean() >= min_cover:
                tr.append(frames[:, y:y + size, x:x + size].reshape(n, -1).mean(1))
                org.append((y, x))
    return np.array(tr), org


def mono_exp(t, a, k, c):
    return a * np.exp(-k * t) + c


def bleach_correct(trace: np.ndarray, fit_idx: np.ndarray, with_method: bool = False):
    """Divide the trace by a monoexponential decay fit to the frames fit_idx (Methods).

    Returns (corrected, curve), and the method used ('exp', or 'line' when the exponential fit
    fails or is not positive) when with_method is set.
    """
    t = np.arange(len(trace), dtype=float)
    y = trace[fit_idx].astype(float)
    p0 = (max(y[0] - y[-1], 1e-6 * abs(y[0])), 1.0 / max(len(trace), 1), y[-1])
    try:
        p, _ = curve_fit(mono_exp, t[fit_idx], y, p0=p0, maxfev=20000)
        curve = mono_exp(t, *p)
        if not np.all(np.isfinite(curve)) or np.any(curve <= 0):
            raise RuntimeError
    except Exception:
        # A fit that fails falls back to a straight line (reported where used).
        q = np.polyfit(t[fit_idx], y, 1)
        curve = np.polyval(q, t)
        method = "line"
    else:
        method = "exp"
    return (trace / curve, curve, method) if with_method else (trace / curve, curve)


def dff(trace: np.ndarray, onset: int, baseline: str = "mean") -> np.ndarray:
    """dF/F in percent; baseline 'mean' (frames before onset) or 'first' (the first frame)."""
    f0 = trace[:onset].mean() if baseline == "mean" else trace[0]
    return 100.0 * (trace - f0) / f0


def initial_rate(d: np.ndarray, onset: int, dt: float, reading: str, peak_end: int | None = None) -> float:
    """Initial rate (%/s) of a dF/F trace d after the frame `onset` (the last frame before the response).

    reading 'peak': linear fit over the rising phase, from the onset frame (the last frame before
    the response, so that a rise within one frame is included) to the peak (within peak_end).
    reading 'k2'..'k5': slope of a linear fit over the onset frame and the next k frames.
    """
    end = len(d) if peak_end is None else min(len(d), peak_end)
    if reading == "peak":
        pk = onset + 1 + int(np.argmax(d[onset + 1:end]))
        idx = np.arange(onset, pk + 1)
    else:
        k = int(reading[1:])
        idx = np.arange(onset, onset + k + 1)
    return float(np.polyfit(idx * dt, d[idx], 1)[0])


def michaelis_menten(c, vmax, km):
    return vmax * c / (km + c)


def fit_mm(conc: np.ndarray, v: np.ndarray):
    """Least-squares Michaelis-Menten fit: (Vmax, Km, SE Vmax, SE Km, R2)."""
    p0 = (max(v.max(), 1e-3), float(np.median(conc)))
    p, cov = curve_fit(michaelis_menten, conc, v, p0=p0, bounds=([0, 0], [np.inf, np.inf]), maxfev=50000)
    se = np.sqrt(np.diag(cov)) if np.all(np.isfinite(cov)) else np.array([np.nan, np.nan])
    res = v - michaelis_menten(conc, *p)
    r2 = 1 - (res ** 2).sum() / ((v - v.mean()) ** 2).sum()
    return p[0], p[1], se[0], se[1], r2


def two_line_crossing(x: np.ndarray, y: np.ndarray, min_pts: int = 2):
    """Split sorted points into two runs, fit a line to each, minimise the summed squared residuals.

    Returns (crossing x, split index, residual) for the best split, or None when no split has
    at least min_pts points on each side.
    """
    best = None
    for s in range(min_pts, len(x) - min_pts + 1):
        p1 = np.polyfit(x[:s], y[:s], 1)
        p2 = np.polyfit(x[s:], y[s:], 1)
        r = ((np.polyval(p1, x[:s]) - y[:s]) ** 2).sum() + ((np.polyval(p2, x[s:]) - y[s:]) ** 2).sum()
        if p1[0] == p2[0]:
            continue
        xc = (p2[1] - p1[1]) / (p1[0] - p2[0])
        if best is None or r < best[2]:
            best = (xc, s, r)
    return best


def calibration_movies() -> list[dict]:
    """The ex vivo calibration recordings of sub-1: concentration (uM, final, from the file name), frames, start time."""
    out = []
    for f in manifest("108")["files"]:
        p = f["path"]
        if "/sub-1/" not in p:
            continue
        conc = float(p.split("_")[-1].split(" ")[0])
        with tifffile.TiffFile(io.BytesIO(read_bytes("108", p))) as tf:
            a = tf.asarray()
            info = (tf.imagej_metadata or {}).get("Info", "")
        stamp = re.search(r"Created by Hamamatsu Inc\.\s*\n?\s*([^\r\n]+)", info)
        out.append({"path": p, "conc_uM": conc, "frames": a, "acquired": stamp.group(1).strip() if stamp else ""})
    return sorted(out, key=lambda d: d["conc_uM"])


# ---------------------------------------------------------------- gels

def lane_segments(g: np.ndarray, y0: int, y1: int, frac: float = 0.2, min_width: int = 40) -> list[tuple[int, int]]:
    """Lanes as runs of columns whose median signal (rows y0:y1, above the image median) exceeds frac of its maximum."""
    from scipy.ndimage import gaussian_filter1d

    col = gaussian_filter1d(np.median(g[y0:y1], axis=0) - np.median(g), 2)
    on = col > frac * col.max()
    segs, x = [], 0
    while x < len(on):
        if on[x]:
            s = x
            while x < len(on) and on[x]:
                x += 1
            if x - s >= min_width:
                segs.append((s, x))
        x += 1
    return segs


def lane_profile(g: np.ndarray, seg: tuple[int, int], y0: int, y1: int) -> np.ndarray:
    """Mean over the central half of a lane, rows y0:y1, minus the image median, smoothed (3 px)."""
    from scipy.ndimage import gaussian_filter1d

    a, b = seg
    q = (b - a) // 4
    return gaussian_filter1d(g[y0:y1, a + q:b - q].mean(1) - np.median(g), 3)


def bands(profile: np.ndarray, rel_prominence: float = 0.05) -> tuple[np.ndarray, np.ndarray]:
    """Band positions (rows) and prominences: peaks with prominence above rel_prominence of the profile's range."""
    from scipy.signal import find_peaks

    pk, pr = find_peaks(profile, prominence=rel_prominence * (profile.max() - profile.min()))
    return pk, pr["prominences"]


# ---------------------------------------------------------------- puncta

def puncta(img: np.ndarray, px_um: float, min_um2: float = 0.1, max_um2: float = 25.0):
    """Connected components above the background threshold (mean + 3 SD of the below-median pixels).

    The area limits (0.1 to 25 um^2) keep spots and drop single-pixel noise and large structures;
    they are a choice made here, as the paper does not define a punctum. Returns (labels, kept
    component ids, threshold).
    """
    from scipy import ndimage as ndi

    thr = background_threshold(img)
    lab, n = ndi.label(img > thr)
    area = np.bincount(lab.ravel())[1:] * px_um ** 2
    keep = np.flatnonzero((area >= min_um2) & (area <= max_um2)) + 1
    return lab, keep, thr


def soma_mask(gfp: np.ndarray, px_um: float, rule: str = "otsu", min_um2: float = 50.0) -> np.ndarray:
    """GFP-positive somata: Gaussian smoothing (1 um), a threshold, holes filled, objects of 50 um^2 or less removed.

    rule 'otsu': Otsu's threshold; rule 'background': mean plus 3 SD of the background (as for the
    puncta), which also takes in dim somata. Both are choices made here; the paper draws no mask.
    """
    from scipy import ndimage as ndi
    from skimage.filters import threshold_otsu
    from skimage.morphology import remove_small_objects

    s = ndi.gaussian_filter(gfp.astype(float), 1.0 / px_um)
    thr = threshold_otsu(s) if rule == "otsu" else background_threshold(s)
    m = ndi.binary_fill_holes(s > thr)
    return remove_small_objects(m, max_size=max(1, int(min_um2 / px_um ** 2)))
