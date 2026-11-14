"""Streaming access to CRCNS pvc-10 (Scholl et al. 2015, doi:10.6080/K0GT5K3V).

The data set is unversioned on CRCNS; the files read are those of its published
folder `pvc-10/live/`, at the MD5 sums its `checksums.md5` gives (printed by the
notebook). Files are read anonymously from the public S3 bucket `crcnsarchive`
over range requests (fsspec), never downloaded to disk.

What the published folder holds, per the data descriptor (docs/crcns_pvc-10_data_description.pdf):
- `data/mouse<m>/mouse<m>depth<d>green.mat` and `...red.mat`: MATLAB 7.3 (HDF5) cell arrays
  `green` / `red`, one 2-D frame per element;
- `data/mouse<m>/mouse<m>depth<d>stim.mat`: two columns, the frame at which each stimulus
  starts and its condition (1 blank, 2 to 9 binocular phases 0:45:315, 10 ipsilateral,
  11 contralateral);
- `data/mouse<m>/mouse<m>stats.mat`: per depth, the stimulus duration (s) and the x and y shift
  (um) of the plane;
- `script/cellmasks.mat`: 50 example cell masks for mouse5 depth 260 (descriptor, "How to get
  started"; "a mixture of responsive and nonresponsive cells"), with no cell type.

Parameters and where they come from:
- DARKNOISE = -160: the offset the data set's own examplecode.m subtracts from raw intensity
  ("based on our calibration experiments"); used only in the data check.
- F0_FRAMES = 10: frames before each stimulus onset used for Fo. The paper's Methods say only "the
  gray screen (Fo) immediately before the stimulus came on"; examplecode.m defines a
  pre-stimulus window `stim(i,1):(stim(i,1)+9)` of 10 frames. A standard choice for the data
  check, which decides no claim.
- RESP_WINDOW = 0.5 s centred on the average peak: Methods, Data Imaging Analysis ("mean change
  in fluorescence (DF/F) was calculated in a 0.5 s window, centered around the global average
  peak").
"""

from __future__ import annotations

import io
import re
import time
import urllib.parse
import urllib.request

import fsspec
import h5py
import numpy as np
import scipy.io as sio

BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/"
DATASET = "pvc-10"
VERSION = "unversioned"  # CRCNS data sets are not versioned (docs/archives.md, CRCNS)
DOI = "10.6080/K0GT5K3V"
LIVE = f"{DATASET}/live/"

DARKNOISE = -160.0
F0_FRAMES = 10
RESP_WINDOW_S = 0.5

CONDITIONS = {1: "blank", **{k: f"binocular {45 * (k - 2)} deg" for k in range(2, 10)},
              10: "ipsilateral", 11: "contralateral"}


def list_bucket(prefix: str = f"{DATASET}/") -> list[tuple[str, int]]:
    """All (key, size) pairs under a prefix of the bucket, following continuation tokens."""
    out, token = [], None
    while True:
        url = f"{BUCKET}?list-type=2&prefix={prefix}"
        if token:
            url += "&continuation-token=" + urllib.parse.quote(token)
        xml = urllib.request.urlopen(url).read().decode()
        out += [(k, int(s)) for k, s in re.findall(r"<Key>(.*?)</Key>.*?<Size>(\d+)</Size>", xml, re.S)]
        m = re.search(r"<NextContinuationToken>(.*?)</NextContinuationToken>", xml)
        if not m:
            return out
        token = m.group(1)


def read_text(path: str) -> str:
    with fsspec.open(BUCKET + path, "rb").open() as f:
        return f.read().decode("utf-8", "replace")


def checksums() -> dict[str, str]:
    """MD5 sums published in live/checksums.md5, keyed by path relative to live/."""
    out = {}
    for line in read_text(LIVE + "checksums.md5").splitlines():
        parts = line.split()
        if len(parts) == 2:
            out[parts[1]] = parts[0]
    return out


def load_small_mat(path: str) -> dict:
    """A MATLAB 5 file read whole into memory (stim, stats and mask files are a few kB)."""
    with fsspec.open(BUCKET + path, "rb").open() as f:
        d = sio.loadmat(io.BytesIO(f.read()))
    return {k: v for k, v in d.items() if not k.startswith("__")}


def planes() -> dict[int, list[int]]:
    """Depths with a green, red and stim file, per mouse, from the bucket listing of live/data."""
    keys = [k for k, _ in list_bucket(LIVE + "data/")]
    out: dict[int, set] = {}
    for k in keys:
        m = re.search(r"mouse(\d+)depth(\d+)(green|red|stim)\.mat$", k)
        if m:
            out.setdefault(int(m.group(1)), set()).add(int(m.group(2)))
    return {m: sorted(d) for m, d in sorted(out.items())}


def plane_path(mouse: int, depth: int, kind: str) -> str:
    return f"{LIVE}data/mouse{mouse}/mouse{mouse}depth{depth}{kind}.mat"


def stim_table(mouse: int, depth: int) -> np.ndarray:
    """(n, 2) int array: onset frame (1-based, MATLAB) and condition 1 to 11."""
    d = load_small_mat(plane_path(mouse, depth, "stim"))
    (v,) = d.values()
    return np.asarray(v, dtype=int)


def stats_table(mouse: int) -> np.ndarray:
    """(n, 4): depth (um), stimulus duration (s), x shift (um), y shift (um)."""
    d = load_small_mat(f"{LIVE}data/mouse{mouse}/mouse{mouse}stats.mat")
    (v,) = d.values()
    return np.asarray(v, dtype=float)


class Movie:
    """One channel of one plane, opened in place over HTTP range requests.

    MATLAB stores the cell array as a (n_frames, 1) array of object references, each frame
    a (455, 256) float64 dataset in HDF5 order, i.e. 256 rows by 455 columns in MATLAB.
    `frame(i)` returns it in MATLAB orientation (rows, columns) = (256, 455).
    """

    def __init__(self, mouse: int, depth: int, channel: str = "green"):
        self.path = plane_path(mouse, depth, channel)
        self._fh = fsspec.open(BUCKET + self.path, "rb", block_size=2**22,
                               cache_type="readahead").open()
        self._h5 = h5py.File(self._fh, "r")
        self._var = self._h5[channel]
        self.refs = self._var[:, 0]
        self.n_frames = len(self.refs)

    def frame_dataset(self, i: int):
        return self._h5[self.refs[i]]

    def frame(self, i: int) -> np.ndarray:
        return self._h5[self.refs[i]][:].T

    def close(self):
        self._h5.close()
        self._fh.close()


def mask_traces(movie: Movie, masks: np.ndarray, frames=None) -> tuple[np.ndarray, float]:
    """Mean intensity in each mask, per frame, minus DARKNOISE (as examplecode.m does).

    masks: (256, 455, n) in MATLAB orientation. Returns (n, n_frames) and the seconds taken.
    Holds one frame at a time in memory.
    """
    frames = range(movie.n_frames) if frames is None else frames
    m = masks.astype(bool)
    n = m.shape[2]
    flat = m.reshape(-1, n)
    counts = flat.sum(0)
    out = np.empty((n, len(frames)))
    t0 = time.time()
    for j, i in enumerate(frames):
        f = movie.frame(i).reshape(-1)
        out[:, j] = (f @ flat) / counts - DARKNOISE
    return out, time.time() - t0


def trial_dff(trace: np.ndarray, stim: np.ndarray, n_post: int, shift: int = 0) -> np.ndarray:
    """dF/F for each trial: (F - Fo) / Fo, Fo the mean of F0_FRAMES frames before onset.

    trace: (n_cells, n_frames); stim onsets are 1-based. `shift` moves every onset by that many
    frames (used for the clock check). Returns (n_cells, n_trials, n_post).
    """
    on = stim[:, 0] - 1 + shift
    out = np.full((trace.shape[0], len(on), n_post), np.nan)
    for k, o in enumerate(on):
        if o - F0_FRAMES < 0 or o + n_post > trace.shape[1]:
            continue
        f0 = trace[:, o - F0_FRAMES:o].mean(1, keepdims=True)
        out[:, k] = (trace[:, o:o + n_post] - f0) / f0
    return out


# ---------------------------------------------------------------------------------------------
# Processed per-cell structs in pvc-10/original/to_remove/ (outside the published folder live/).
#
# These are MATLAB 7.3 structs `ce` (PV-) and `cePV` (PV+), one entry per cell, with the fields
# listed by the notebook. They are not in live/filelist.txt or live/checksums.md5; the notebook
# prints the S3 ETag of each file read (an MD5 of the content for single-part uploads) so that a
# change is detectable. Field layout, as read (MATLAB orientation):
# - peaks (11, 18): mean dF/F per condition (rows, 1 blank, 2 to 9 binocular 0:45:315 deg,
#   10 ipsilateral, 11 contralateral, as in the stim files) and trial (columns, NaN-padded);
# - standard (1, 11): per condition, a responsiveness index (0 for the blank);
# - dsi, disparitypref: scalars; xy (2, 1): mask centroid (column, row) in pixels;
# - xyshft (2, 1): the plane shift; depth: um; masks: (256, 455) binary mask;
# - neuropilpeaks (11, 18), dsineuropil: the same for a neuropil region of the plane.

ORIGINAL = f"{DATASET}/original/to_remove/"
STRUCT_FIELDS = ("peaks", "standard", "dsi", "disparitypref", "xy", "xyshft", "depth",
                 "neuropilpeaks", "dsineuropil", "date", "filename", "windowlength")


def etags(prefix: str = ORIGINAL) -> dict[str, tuple[int, str]]:
    """(size, ETag) per key under a prefix of the bucket, from the S3 listing."""
    out, token = {}, None
    while True:
        url = f"{BUCKET}?list-type=2&prefix={prefix}"
        if token:
            url += "&continuation-token=" + urllib.parse.quote(token)
        xml = urllib.request.urlopen(url).read().decode()
        for blk in re.findall(r"<Contents>(.*?)</Contents>", xml, re.S):
            k = re.search(r"<Key>(.*?)</Key>", blk).group(1)
            s = int(re.search(r"<Size>(\d+)</Size>", blk).group(1))
            e = re.search(r"<ETag>(.*?)</ETag>", blk).group(1).replace("&quot;", "").strip('"')
            out[k] = (s, e)
        m = re.search(r"<NextContinuationToken>(.*?)</NextContinuationToken>", xml)
        if not m:
            return out
        token = m.group(1)


def load_struct(mouse: int, pv: bool, masks: bool = False) -> dict:
    """Per-cell fields of binoc<mouse>[PV].mat as a dict of lists (one item per cell).

    Small fields are read whole; with masks=True the mask's pixel count and centroid are added
    (each mask is read and dropped, so memory stays small).
    """
    path = f"{ORIGINAL}binoc{mouse}{'PV' if pv else ''}.mat"
    fh = fsspec.open(BUCKET + path, "rb", block_size=2**20).open()
    h = h5py.File(fh, "r")
    g = h["cePV" if pv else "ce"]
    n = g["peaks"].shape[0]
    out = {f: [] for f in STRUCT_FIELDS}
    for f in STRUCT_FIELDS:
        refs = g[f][:, 0]
        for r in refs:
            v = h[r][()]
            if h[r].attrs.get("MATLAB_class") == b"char":
                v = "".join(map(chr, v.ravel()))
            else:
                v = np.asarray(v, dtype=float).T  # MATLAB orientation
            out[f].append(v)
    if masks:
        out["mask_npix"], out["mask_centroid"], out["mask_components"] = [], [], []
        from scipy import ndimage
        for r in g["masks"][:, 0]:
            m = h[r][()].T > 0
            ys, xs = np.nonzero(m)
            out["mask_npix"].append(int(m.sum()))
            out["mask_centroid"].append((xs.mean() + 1, ys.mean() + 1))  # 1-based (column, row)
            out["mask_components"].append(int(ndimage.label(m)[1]))
    h.close()
    fh.close()
    out["n"] = n
    return out


def binocmonocinds(mouse: int, pv: bool) -> np.ndarray:
    """The index list in binocmonocinds<mouse>[PV].mat (as stored, MATLAB 1-based)."""
    d = load_small_mat(f"{ORIGINAL}binocmonocinds{mouse}{'PV' if pv else ''}.mat")
    return np.asarray(d["inds"]).ravel().astype(int)


# ---------------------------------------------------------------------------------------------
# Per-cell measures from the structs, and the paper's local network analysis.
#
# Sources of each parameter:
# - Responsiveness: (m_stim - m_blank) / (SE_stim + SE_blank) >= 1 for at least one monocular and
#   one binocular stimulus (Methods, Data Imaging Analysis). The structs' `standard` field holds
#   this index per condition; the notebook shows it equals the index recomputed from `peaks` for
#   most cells. The neuropil requirement ("larger than neuropil activity (> 95% confidence
#   interval)") is read as the cell's mean response above the neuropil's mean + 1.96 SE for the
#   same condition, a standard reading of a 95% CI; results are shown with and without it.
# - ODI = (R_ipsi - R_contra) / (R_contra + R_ipsi), conditions 10 and 11 (Methods; descriptor
#   for the condition codes). R is read as the mean dF/F minus the blank mean, the form that
#   reproduces the structs' stored DSI (shown in the notebook), with negative R set to zero so
#   that ODI stays in [-1, 1]; the other readings (as measured, without the blank subtracted) are
#   shown. MI = |ODI|.
# - DSI and disparity preference: the structs' stored values (vector strength of the blank
#   subtracted means over the eight binocular phases, Methods); recomputed variants shown.
# - Local network analysis: Methods, Local Network Analysis, and the claims file's opening
#   comment (radii 50, 75, 100, 125, 150 um, sphere then shells, at least 3 cells, individuals
#   at least 50 um from the image edges, positions shuffled within the session). Bootstrap and
#   shuffle counts are a standard choice (claims file, open reading 4).

RADII = (50, 75, 100, 125, 150)
FRAME_ROWS, FRAME_COLS, FIELD_UM = 256, 455, 300.0


def cell_table(structs: dict) -> dict:
    """Stack the struct entries of several (mouse, pv) keys into arrays, one row per cell."""
    rows = []
    for (mouse, pv), s in structs.items():
        for i in range(s["n"]):
            p = s["peaks"][i]
            mu = np.nanmean(p, 1)
            k = np.sum(~np.isnan(p), 1)
            se = np.nanstd(p, 1, ddof=1) / np.sqrt(k)
            npk = s["neuropilpeaks"][i]
            nmu = np.nanmean(npk, 1)
            nse = np.nanstd(npk, 1, ddof=1) / np.sqrt(np.sum(~np.isnan(npk), 1))
            rows.append(dict(mouse=mouse, pv=pv, idx=i + 1, depth=float(s["depth"][i].ravel()[0]),
                             col=float(s["xy"][i].ravel()[0]), row=float(s["xy"][i].ravel()[1]),
                             shift=s["xyshft"][i].ravel().astype(float), file=s["filename"][i],
                             mu=mu, se=se, nmu=nmu, nse=nse, standard=s["standard"][i].ravel(),
                             dsi=float(s["dsi"][i].ravel()[0]),
                             pref=float(s["disparitypref"][i].ravel()[0])))
    out = {k: np.array([r[k] for r in rows]) for k in rows[0]}
    return out


def responsive(T: dict, neuropil: bool, index: str = "stored") -> dict:
    """Monocular, binocular and joint responsiveness per cell (Methods criterion)."""
    if index == "stored":
        st = T["standard"]
    else:
        st = (T["mu"] - T["mu"][:, :1]) / (T["se"] + T["se"][:, :1])
    ok = st >= 1
    if neuropil:
        ok &= T["mu"] > T["nmu"] + 1.96 * T["nse"]
    mono = ok[:, 9:11].any(1)
    bino = ok[:, 1:9].any(1)
    return dict(mono=mono, bino=bino, joint=mono & bino)


def odi(T: dict, blank: bool = True, clip: bool = True) -> np.ndarray:
    r = T["mu"] - (T["mu"][:, :1] if blank else 0)
    if clip:
        r = np.clip(r, 0, None)
    ri, rc = r[:, 9], r[:, 10]
    with np.errstate(invalid="ignore", divide="ignore"):
        return (ri - rc) / (rc + ri)


def dsi_pref(T: dict, blank: bool = True, clip: bool = False) -> tuple[np.ndarray, np.ndarray]:
    """Vector strength and angle (deg) of the eight binocular phase responses."""
    r = T["mu"][:, 1:9] - (T["mu"][:, :1] if blank else 0)
    if clip:
        r = np.clip(r, 0, None)
    v = np.sum(r * np.exp(1j * np.deg2rad(np.arange(0, 360, 45))), 1)
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.abs(v) / r.sum(1), np.rad2deg(np.angle(v)) % 360


def ma_slope(x: np.ndarray, y: np.ndarray) -> float:
    """Major-axis (first principal component) slope of y on x (Methods, after Sokal and Rohlf)."""
    c = np.cov(x, y)
    sx, sy, sxy = c[0, 0], c[1, 1], c[0, 1]
    l1 = (sx + sy + np.sqrt((sx + sy) ** 2 - 4 * (sx * sy - sxy ** 2))) / 2
    return (l1 - sx) / sxy if sxy != 0 else 0.0


def boot_slope(x, y, rng, n_boot=1000):
    """Mean and SD of major-axis slopes over bootstrap resamples of the pairs."""
    n = len(x)
    s = np.array([ma_slope(x[i], y[i]) for i in rng.integers(0, n, (n_boot, n))])
    return float(np.mean(s)), float(np.std(s, ddof=1))


def positions_um(T: dict, square: bool) -> np.ndarray:
    """(x, y, z) in um: pixel centroid scaled, plus the plane shift, and depth.

    square=False: 300 um along each image axis (claims file reading 7a);
    square=True: 300 um along the 455-pixel axis, square pixels (reading 7b).
    """
    sx = FIELD_UM / FRAME_COLS
    sy = sx if square else FIELD_UM / FRAME_ROWS
    return np.stack([T["col"] * sx + T["shift"][:, 0], T["row"] * sy + T["shift"][:, 1],
                     T["depth"]], 1)


def edge_ok(T: dict, square: bool, margin=50.0) -> np.ndarray:
    """Cells at least `margin` um from every edge of their image (in that plane's own pixels)."""
    sx = FIELD_UM / FRAME_COLS
    sy = sx if square else FIELD_UM / FRAME_ROWS
    x, y = T["col"] * sx, T["row"] * sy
    return (x >= margin) & (x <= FRAME_COLS * sx - margin) & (y >= margin) & (y <= FRAME_ROWS * sy - margin)


def shells(ind_pos, pop_pos, same, radii=RADII):
    """Boolean (n_ind, n_pop, n_radii): pop cell in the sphere (first) or shell of each radius.

    `same` (n_ind, n_pop) marks pairs that are the same cell (excluded)."""
    d = np.linalg.norm(ind_pos[:, None, :] - pop_pos[None, :, :], axis=2)
    lo = (0,) + tuple(radii[:-1])
    out = np.stack([(d > a if a > 0 else d >= 0) & (d <= b) for a, b in zip(lo, radii)], 2)
    out &= ~same[:, :, None]
    return out


def boot_slopes(x, y, rng, n_boot=1000) -> np.ndarray:
    """Major-axis slopes of y on x over bootstrap resamples of the (x, y) pairs (vectorized)."""
    n = len(x)
    i = rng.integers(0, n, (n_boot, n))
    xs, ys = x[i], y[i]
    xm, ym = xs - xs.mean(1, keepdims=True), ys - ys.mean(1, keepdims=True)
    sx, sy, sxy = (xm ** 2).sum(1), (ym ** 2).sum(1), (xm * ym).sum(1)
    l1 = (sx + sy + np.sqrt((sx + sy) ** 2 - 4 * (sx * sy - sxy ** 2))) / 2
    with np.errstate(invalid="ignore", divide="ignore"):
        return (l1 - sx) / sxy


def local_values(T, ind, pop, ind_pos, pop_pos, values, plane="all", radii=RADII, min_cells=3):
    """Population average of `values` (real, or complex vectors) around each individual cell.

    ind, pop: indices into T; ind_pos, pop_pos: (len, 3) positions in um (pop_pos may be
    shuffled). Populations are drawn within the same mouse (the imaging session), from the 50 um
    sphere and the shells beyond it; the individual itself is left out. plane: "all", "other"
    (populations outside the individual's focal plane) or "same" (inside it). Returns
    (len(ind), len(radii)) with NaN where the population has fewer than `min_cells` cells.
    """
    out = np.full((len(ind), len(radii)), np.nan, dtype=complex if np.iscomplexobj(values) else float)
    for m in np.unique(T["mouse"][ind]):
        a = np.nonzero(T["mouse"][ind] == m)[0]
        b = np.nonzero(T["mouse"][pop] == m)[0]
        if len(b) == 0:
            continue
        same = ind[a][:, None] == pop[b][None, :]
        if plane == "other":
            same |= T["depth"][ind[a]][:, None] == T["depth"][pop[b]][None, :]
        elif plane == "same":
            same |= T["depth"][ind[a]][:, None] != T["depth"][pop[b]][None, :]
        sh = shells(ind_pos[a], pop_pos[b], same, radii)
        cnt = sh.sum(1)
        v = values[pop[b]]
        tot = np.einsum("ipr,p->ir", sh.astype(values.dtype), v)
        with np.errstate(invalid="ignore", divide="ignore"):
            avg = tot / cnt
        avg[cnt < min_cells] = np.nan
        out[a] = avg
    return out


def shuffle_pop_pos(T, pop, pos, rng):
    """Positions of the population cells permuted among themselves within each mouse."""
    out = pos[pop].copy()
    for m in np.unique(T["mouse"][pop]):
        i = np.nonzero(T["mouse"][pop] == m)[0]
        out[i] = out[rng.permutation(i)]
    return out


def circ_corr_printed(a, b):
    """Methods' circular correlation: (1/N) |sum exp(i (a - b))| (angles in radians)."""
    return float(np.abs(np.mean(np.exp(1j * (a - b)))))


def circ_corrcc(a, b):
    """CircStat circ_corrcc (Berens 2009; Jammalamadaka and SenGupta), angles in radians."""
    ma = np.angle(np.mean(np.exp(1j * a)))
    mb = np.angle(np.mean(np.exp(1j * b)))
    sa, sb = np.sin(a - ma), np.sin(b - mb)
    return float(np.sum(sa * sb) / np.sqrt(np.sum(sa ** 2) * np.sum(sb ** 2)))


def circ_corrcl(alpha, x):
    """CircStat circ_corrcl: circular-linear correlation and its p-value (chi-square, 2 df)."""
    from scipy.stats import chi2
    rxs = np.corrcoef(x, np.sin(alpha))[0, 1]
    rxc = np.corrcoef(x, np.cos(alpha))[0, 1]
    rcs = np.corrcoef(np.sin(alpha), np.cos(alpha))[0, 1]
    rho = np.sqrt((rxc ** 2 + rxs ** 2 - 2 * rxc * rxs * rcs) / (1 - rcs ** 2))
    return float(rho), float(1 - chi2.cdf(len(alpha) * rho ** 2, 2))


def exp_fit(r, y, sigma=None):
    """Fit y = a exp(-r / lambda) (Methods); returns a, lambda and r2 (on the unweighted values)."""
    from scipy.optimize import curve_fit
    f = lambda rr, a, lam: a * np.exp(-rr / lam)
    try:
        (a, lam), _ = curve_fit(f, r, y, p0=(max(y[0], 1e-3) * 2, 70.0), sigma=sigma, maxfev=20000)
    except (RuntimeError, ValueError):
        return np.nan, np.nan, np.nan
    res = y - f(r, a, lam)
    return float(a), float(lam), float(1 - np.sum(res ** 2) / np.sum((y - y.mean()) ** 2))


def od_local(T, ind, pop, odi_v, pos, rng, axis="a", drop_all=False, plane="all", pop_vals=None,
             n_boot=1000, n_shuf=1000):
    """Bootstrapped major-axis slope of individual and population ODI at each radius.

    axis "a": individual (y) on population (x); "b": population on individual. drop_all: keep
    only individuals with a population at every radius (claims file reading 3b). pop_vals: the
    values averaged over populations (default odi_v). Returns a list of dicts per radius: n, mean
    bootstrap slope, its SD (the SE), the slope of the data, and the shuffled slopes' mean and
    one- and two-sided p-values of the mean bootstrap slope against them.
    """
    pv = odi_v if pop_vals is None else pop_vals
    V = local_values(T, ind, pop, pos[ind], pos[pop], pv, plane)
    keep_all = np.isfinite(V).all(1)
    y_ind = odi_v[ind]

    def slopes(V):
        out = []
        for r in range(V.shape[1]):
            ok = np.isfinite(V[:, r]) & (keep_all if drop_all else True)
            x, y = V[ok, r], y_ind[ok]
            out.append((x, y) if axis == "a" else (y, x))
        return out

    true = slopes(V)
    sh = np.full((n_shuf, len(RADII)), np.nan)
    for s in range(n_shuf):
        Vs = local_values(T, ind, pop, pos[ind], shuffle_pop_pos(T, pop, pos, rng), pv, plane)
        keep_s = np.isfinite(Vs).all(1)
        for r in range(len(RADII)):
            ok = np.isfinite(Vs[:, r]) & (keep_s if drop_all else True)
            if ok.sum() >= 3:
                x, y = (Vs[ok, r], y_ind[ok]) if axis == "a" else (y_ind[ok], Vs[ok, r])
                sh[s, r] = ma_slope(x, y)
    res = []
    for r, (x, y) in enumerate(true):
        if len(x) < 3:
            res.append(dict(radius=RADII[r], n=len(x)))
            continue
        b = boot_slopes(x, y, rng, n_boot)
        b = b[np.isfinite(b)]
        m = float(np.mean(b))
        d = sh[:, r][np.isfinite(sh[:, r])]
        c = np.mean(d)
        res.append(dict(radius=RADII[r], n=len(x), slope=m, se=float(np.std(b, ddof=1)),
                        slope_data=ma_slope(x, y), shuf_mean=float(c),
                        shuf_95=float(np.percentile(d, 95)),
                        p_one=float((np.sum(d >= m) + 1) / (len(d) + 1)),
                        p_two=float((np.sum(np.abs(d - c) >= abs(m - c)) + 1) / (len(d) + 1))))
    return res


def disp_local(T, ind, pop, dsi_v, pref_v, pos, rng, corr="printed", plane="all", n_boot=1000,
               n_shuf=1000):
    """Shuffle-corrected circular correlation of individual preference and population angle.

    Population vectors are (1/n) sum DSI_n exp(i psi_n) over the population (Methods). corr:
    "printed" (the Methods' formula) or "corrcc" (CircStat). Returns per radius: n, the true
    correlation, the shuffled mean, the corrected value, its bootstrap SE (individuals resampled,
    shuffled mean held), the p-value of the true value against the shuffled ones (one-sided).
    """
    f = circ_corr_printed if corr == "printed" else circ_corrcc
    vec = dsi_v * np.exp(1j * np.deg2rad(pref_v))
    psi = np.deg2rad(pref_v[ind])
    V = local_values(T, ind, pop, pos[ind], pos[pop], vec, plane)
    sh = np.full((n_shuf, len(RADII)), np.nan)
    for s in range(n_shuf):
        Vs = local_values(T, ind, pop, pos[ind], shuffle_pop_pos(T, pop, pos, rng), vec, plane)
        for r in range(len(RADII)):
            ok = np.isfinite(Vs[:, r])
            if ok.sum() >= 3:
                sh[s, r] = f(psi[ok], np.angle(Vs[ok, r]))
    res = []
    for r in range(len(RADII)):
        ok = np.isfinite(V[:, r])
        n = int(ok.sum())
        if n < 3:
            res.append(dict(radius=RADII[r], n=n))
            continue
        a, z = psi[ok], np.angle(V[ok, r])
        t = f(a, z)
        d = sh[:, r][np.isfinite(sh[:, r])]
        c = float(np.mean(d))
        bs = [f(a[i], z[i]) - c for i in rng.integers(0, n, (n_boot, n))]
        res.append(dict(radius=RADII[r], n=n, corr=t, shuf_mean=c, corrected=t - c,
                        se=float(np.std(bs, ddof=1)),
                        p_one=float((np.sum(d >= t) + 1) / (len(d) + 1))))
    return res


def struct_field(mouse: int, pv: bool, entries: list[int], field: str) -> list[np.ndarray]:
    """One field of the given struct entries (0-based), each in MATLAB orientation."""
    path = f"{ORIGINAL}binoc{mouse}{'PV' if pv else ''}.mat"
    with fsspec.open(BUCKET + path, "rb", block_size=2**20).open() as fh, h5py.File(fh, "r") as h:
        refs = h["cePV" if pv else "ce"][field][:, 0]
        return [h[refs[i]][()].T for i in entries]


def struct_masks(mouse: int, pv: bool, entries: list[int]) -> np.ndarray:
    """Masks of the given struct entries (0-based), (256, 455, n) in MATLAB orientation."""
    return np.stack([m > 0 for m in struct_field(mouse, pv, entries, "masks")], 2)
