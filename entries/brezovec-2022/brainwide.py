"""Loading and measures for the whole-brain imaging of walking flies in dandiset 000727.

Brezovec, Berger, Druckmann & Clandinin (2022), bioRxiv, doi:10.1101/2022.03.20.485047.

Each NWB file holds one fly: raw two-photon volumes (GCaMP6f and tdTomato, 256 x 128 x 49
voxels, 3384 volumes at 1.88 Hz), the GCaMP6f volumes after motion correction, high-pass
filtering, z-scoring and warping into the Functional Drosophila Atlas (FDA, 314 x 146 x 91
voxels, `TwoPhotonSeriesFunctionalGreenProcessed`), a high-resolution anatomical scan, and the
FicTrac output of the treadmill ball at 50 Hz. Files are streamed from the archive at the pinned
version; nothing is written to disk.

The processed series is stored in gzip chunks of 54 volumes x one whole z-plane. A z-plane of
one fly (63 chunks, up to 300 MB compressed) is fetched with one HTTP range request per chunk
and decompressed here; this is about 40 times faster than reading through h5py over the
network, and gives the same values (checked in the notebook). Only the planes in `SLICES` are
read: the whole processed series is about 17.7 GB per fly, too much to stream in the time limit.

Where the parameters come from:

- Behaviour follows the paper's code, ClandininLab/brezovec_volition_2023 at commit
  8e2b275f1a95947212eacd3e511915039ffc5df4 (correlation_analysis.py, linear_filters.py,
  neural_histograms.py): forward velocity is FicTrac's `dRotLabY` and rotational velocity
  `dRotLabZ` (the lab-frame rotation deltas, radians per frame), each smoothed with a
  Savitzky-Golay filter of 25 frames (500 ms, as the Methods say) and order 3, then sampled at
  the neural times. Forward velocity is clipped at 0 (`Y_pos`); left turns are the positive part
  of `dRotLabZ` (`Z_pos`) and right turns the negative part, sign flipped (`Z_neg`); the code
  labels them "forward, left, and right". Conversion to mm/s uses the 4.5 mm ball radius of the
  Methods and the code; to deg/s, 180 / pi x 50.
- The walking state is the code's `make_walking_vector` (linear_filters.py) as it runs:
  `np.sqrt(a, b)` takes `b` as its output array, so the code's test reduces to
  |forward| / sd(forward) > 0.2. `walking_state(..., as_intended=True)` gives the norm of both
  standardised components the line was written to compute.
- Neural times: the files give only a volume rate and a start of 0 for imaging and FicTrac
  alike, and no per-plane times, so each volume is placed at its midpoint, (k + 0.5) / rate.
  The paper used the time of each plane (about 5 ms precision). Planes of the FDA space do not
  map onto acquired planes, so the error is up to half a volume, 0.27 s.
- `SLICES` (every 7th FDA plane from 10) and `BLOCK` (6 x 6 voxel squares within a plane, used
  in place of the paper's supervoxels, which are not in the dandiset) are choices of this
  attempt. A block is kept when at least half of its voxels are inside the brain in every fly.
- The raw GCaMP6f and tdTomato series (`TwoPhotonSeriesFunctionalGreen`, `...Red`, 256 x 128 x 49
  voxels, uint16, chunks of 152 volumes x one plane) are read for the planes in `RAW_SLICES`
  (a choice) and high-pass filtered as the code does (preprocessing_neural_data.py, Gaussian
  sigma 200 volumes, truncate 1). They are not motion corrected.
"""

from __future__ import annotations

import threading
import time
import zlib
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

import h5py
import numpy as np
import remfile
import requests
from dandi.dandiapi import DandiAPIClient
from scipy.signal import savgol_filter

DANDISET_ID = "000727"
DANDISET_VERSION = "0.240106.0043"

PROCESSED = "processing/ophys/TwoPhotonSeriesFunctionalGreenProcessed"
RAW_GREEN = "acquisition/TwoPhotonSeriesFunctionalGreen"
RAW_RED = "acquisition/TwoPhotonSeriesFunctionalRed"
FICTRAC = "processing/behavior/FicTrac"

BALL_RADIUS_MM = 4.5            # Methods: 9 mm diameter ball; code: sphere_radius = 4.5e-3 m
FICTRAC_HZ = 50.0               # Methods and code
SAVGOL_FRAMES, SAVGOL_ORDER = 25, 3   # code; Methods: 500 ms window, order 3
WALK_THRESHOLD = 0.2            # code, make_walking_vector
SLICES = tuple(range(10, 91, 7))  # choice of this attempt: 12 of the 91 FDA planes
RAW_SLICES = (18, 30)           # choice of this attempt: 2 of the 49 raw planes, for the tdTomato check
HIGH_PASS_SIGMA = 200           # code, preprocessing_neural_data.py: gaussian_filter1d(sigma=200, truncate=1)
BLOCK = 6                       # choice of this attempt: 6 x 6 voxel blocks as supervoxels
X_CROP, Y_CROP = (1, 313), (1, 145)  # 52 x 24 blocks, centred on the FDA's left-right midline
N_THREADS = 16


def asset_urls() -> list[tuple[str, str]]:
    """(path, streaming URL) of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in dandiset.get_assets() if a.path.endswith(".nwb"))


def _text(value) -> str:
    return value.decode() if isinstance(value, bytes) else str(value)


def _session(path_url: tuple[str, str]) -> dict:
    """Metadata, FicTrac series and the chunk index of the processed planes of one file."""
    path, url = path_url
    f = h5py.File(remfile.File(url), "r")
    subject = {k: _text(f["general/subject"][k][()]) for k in f["general/subject"]}
    out = {"path": path, "url": url, "subject_id": subject["subject_id"], "subject": subject,
           "session_start": _text(f["session_start_time"][()]),
           "session_id": _text(f["general/session_id"][()])}
    series = {}
    for name in f[FICTRAC]:
        g = f[f"{FICTRAC}/{name}"]
        series[name] = {"data": g["data"][:], "rate": float(g["starting_time"].attrs["rate"]),
                        "start": float(g["starting_time"][()]), "unit": _text(g["data"].attrs["unit"]),
                        "conversion": float(g["data"].attrs["conversion"]),
                        "description": _text(g.attrs["description"])}
    out["fictrac"] = series
    for key, name in (("processed", PROCESSED), ("raw", RAW_GREEN)):
        g = f[name]
        out[key] = {"shape": g["data"].shape, "rate": float(g["starting_time"].attrs["rate"]),
                    "start": float(g["starting_time"][()]), "chunks": g["data"].chunks,
                    "dtype": str(g["data"].dtype), "description": _text(g.attrs["description"])}
        plane = _text(g["imaging_plane"].attrs.get("path", b"")) if "imaging_plane" in g else ""
        out[key]["imaging_plane"] = plane
    for key, name in (("processed", "ImagingPlaneFunctionalGreenProcessed"), ("raw", "ImagingPlaneGCaMP6fFunctional")):
        g = f[f"general/optophysiology/{name}"]
        out[key]["grid_spacing"] = g["grid_spacing"][()].tolist()
        out[key]["grid_spacing_unit"] = _text(g["grid_spacing"].attrs.get("unit", ""))
    out["anatomical"] = {"shape": f["acquisition/TwoPhotonSeriesAnatomicalRed/data"].shape,
                         "start": float(f["acquisition/TwoPhotonSeriesAnatomicalRed/starting_time"][()])}
    datasets = []

    def listing(name, obj):
        if isinstance(obj, h5py.Dataset) and obj.ndim >= 2 and obj.size > 1000:
            datasets.append({"dataset": name, "shape": obj.shape, "dtype": str(obj.dtype), "chunks": obj.chunks,
                             "compression": obj.compression})

    f.visititems(listing)
    out["datasets"] = datasets
    out["chunk_index"] = _chunk_index(f[f"{PROCESSED}/data"], SLICES)
    out["raw_chunk_index"] = {ch: _chunk_index(f[f"{name}/data"], RAW_SLICES)
                              for ch, name in (("green", RAW_GREEN), ("red", RAW_RED))}
    out["raw_red_description"] = _text(f[RAW_RED].attrs["description"])
    # Values read through h5py, to check the direct chunk reads against
    out["h5py_check"] = f[f"{PROCESSED}/data"][0:54, :, :, SLICES[len(SLICES) // 2]]
    f.close()
    return out


def _chunk_index(dataset, slices) -> dict:
    """(time offset, byte offset, size) of the chunks of each z-plane in slices; chunks hold one plane."""
    index = {}
    wanted = set(slices)

    def keep(info):
        t0, _, _, z = info.chunk_offset
        if z in wanted:
            index.setdefault(z, []).append((t0, info.byte_offset, info.size))

    dataset.id.chunk_iter(keep)
    return {z: sorted(v) for z, v in index.items()}


def load_sessions(workers: int = 9) -> list[dict]:
    """Every file's metadata, FicTrac and chunk index, read in parallel processes."""
    urls = asset_urls()
    with ProcessPoolExecutor(workers) as pool:
        return list(pool.map(_session, urls))


_local = threading.local()


def _get(url: str, start: int, size: int, tries: int = 4) -> bytes:
    if not hasattr(_local, "session"):
        _local.session = requests.Session()
    for attempt in range(tries):
        try:
            r = _local.session.get(url, headers={"Range": f"bytes={start}-{start + size - 1}"}, timeout=120)
            r.raise_for_status()
            if len(r.content) != size:
                raise OSError(f"short read: {len(r.content)} of {size} bytes")
            return r.content
        except (requests.RequestException, OSError):
            if attempt == tries - 1:
                raise
            time.sleep(2 ** attempt)


def read_plane(session: dict, z: int, pool: ThreadPoolExecutor, channel: str | None = None) -> np.ndarray:
    """One z-plane, (time, x, y) float32: of the processed series, or of a raw channel ('green', 'red')."""
    key = "processed" if channel is None else "raw"
    n_t, n_x, n_y, _ = session[key]["shape"]
    chunk_t = session[key]["chunks"][0]
    dtype = "<f4" if channel is None else "<u2"
    index = session["chunk_index"] if channel is None else session["raw_chunk_index"][channel]
    out = np.empty((n_t, n_x, n_y), dtype=np.float32)

    def fetch(entry):
        t0, offset, size = entry
        block = np.frombuffer(zlib.decompress(_get(session["url"], offset, size)), dtype=dtype)
        block = block.reshape(chunk_t, n_x, n_y)
        stop = min(t0 + chunk_t, n_t)
        out[t0:stop] = block[: stop - t0]

    list(pool.map(fetch, index[z]))
    return out


def neural_times(session: dict) -> np.ndarray:
    """Midpoint of each volume, seconds from the start of imaging."""
    n_t = session["processed"]["shape"][0]
    return (np.arange(n_t) + 0.5) / session["processed"]["rate"]


def smoothed_velocity(session: dict) -> dict:
    """Forward (mm/s) and rotational (deg/s, positive = left) velocity at 50 Hz, smoothed as the code does."""
    d = session["fictrac"]["SpatialSeriesRotationDeltaLabFrame"]["data"]
    y = savgol_filter(d[:, 1], SAVGOL_FRAMES, SAVGOL_ORDER)
    z = savgol_filter(d[:, 2], SAVGOL_FRAMES, SAVGOL_ORDER)
    t = np.arange(len(y)) / FICTRAC_HZ
    return {"t": t, "Y": y, "Z": z, "forward_mm_s": y * BALL_RADIUS_MM * FICTRAC_HZ,
            "rotation_deg_s": z * 180 / np.pi * FICTRAC_HZ}


def walking_state(y: np.ndarray, z: np.ndarray, as_intended: bool = False) -> np.ndarray:
    """The code's binary walking vector (see the module docstring)."""
    if as_intended:
        norm = np.sqrt((y / np.std(y)) ** 2 + (z / np.std(z)) ** 2)
    else:
        norm = np.abs(y / np.std(y))
    return (norm > WALK_THRESHOLD).astype(float)


def behaviour_at(session: dict, times: np.ndarray) -> dict:
    """The behaviour variables of the paper at the given times (s): fwd, left, right, walk, and raw Y, Z."""
    v = smoothed_velocity(session)
    y = np.nan_to_num(np.interp(times, v["t"], v["Y"], left=np.nan, right=np.nan))
    z = np.nan_to_num(np.interp(times, v["t"], v["Z"], left=np.nan, right=np.nan))
    walk_hi = walking_state(v["Y"], v["Z"])
    walk = np.interp(times, v["t"], walk_hi) >= 0.5   # nearest-sample, as interp1d(kind='nearest')
    return {"fwd": np.clip(y, 0, None), "left": np.clip(z, 0, None), "right": -np.clip(z, None, 0),
            "walk": walk.astype(float), "Y": y, "Z": z}


def reduce_plane(x: np.ndarray, regressors: np.ndarray) -> dict:
    """What the analysis keeps of one plane of one fly.

    x: (time, 314, 146) processed plane; regressors: (k, time).
    Returns per-voxel sums for pooled correlations (sum x, sum x^2, sum x*b for each regressor),
    the in-brain mask (voxels that are not constant), and the block signals: the mean over the
    in-brain voxels of each 6 x 6 block, with the count of those voxels.
    """
    n_t = x.shape[0]
    flat = x.reshape(n_t, -1)
    sx = flat.sum(0, dtype=np.float64)
    sxx = np.einsum("ij,ij->j", flat, flat, dtype=np.float64)
    sxb = regressors.astype(np.float32) @ flat
    inside = (flat != flat[0]).any(0)
    xc = x[:, X_CROP[0]:X_CROP[1], Y_CROP[0]:Y_CROP[1]]
    nbx, nby = xc.shape[1] // BLOCK, xc.shape[2] // BLOCK
    m = inside.reshape(x.shape[1:])[X_CROP[0]:X_CROP[1], Y_CROP[0]:Y_CROP[1]]
    counts = m.reshape(nbx, BLOCK, nby, BLOCK).sum((1, 3))
    sums = (xc * m).reshape(n_t, nbx, BLOCK, nby, BLOCK).sum((2, 4))
    blocks = (sums / np.maximum(counts, 1)).reshape(n_t, -1).astype(np.float32)
    shape = x.shape[1:]
    return {"sx": sx.reshape(shape), "sxx": sxx.reshape(shape),
            "sxb": sxb.reshape((len(regressors),) + shape).astype(np.float64),
            "inside": inside.reshape(shape), "blocks": blocks, "counts": counts.ravel()}


def load_fly(session: dict, regressors: np.ndarray, pool: ThreadPoolExecutor) -> dict:
    """Read and reduce every plane in SLICES for one fly."""
    planes = {}
    check_z = SLICES[len(SLICES) // 2]
    for z in SLICES:
        x = read_plane(session, z, pool)
        planes[z] = reduce_plane(x, regressors)
        if z == check_z:
            planes[z]["same_as_h5py"] = bool(np.array_equal(x[:54], session["h5py_check"]))
    return planes


def high_pass(x: np.ndarray) -> np.ndarray:
    """The code's high-pass filter along time (axis 0): x minus its Gaussian smoothing (sigma 200
    volumes, truncate 1, reflected edges), plus the mean. Done by FFT convolution for speed."""
    from scipy.signal import fftconvolve
    s = HIGH_PASS_SIGMA
    k = np.exp(-0.5 * (np.arange(-s, s + 1) / s) ** 2)
    k = (k / k.sum()).astype(np.float32)
    padded = np.concatenate([x[s - 1::-1], x, x[:-s - 1:-1]], 0)        # scipy 'reflect' mode
    smooth = fftconvolve(padded, k[:, None], mode="valid", axes=0)
    return x - smooth + x.mean(0)


def raw_correlations(session: dict, regressors: np.ndarray, pool: ThreadPoolExecutor) -> dict:
    """Within-fly correlations of raw GCaMP6f and raw tdTomato voxels with the regressors, per plane in RAW_SLICES.

    The raw volumes are not motion corrected. Each channel is high-pass filtered as the code does;
    voxels are those whose mean tdTomato is above the plane's median (a choice, to keep the brain).
    Returns {z: {"green": r (k, voxels), "red": r (k, voxels)}}.
    """
    out = {}
    b = regressors - regressors.mean(1, keepdims=True)
    b /= np.sqrt((b ** 2).sum(1, keepdims=True))
    for z in RAW_SLICES:
        red = read_plane(session, z, pool, "red").reshape(regressors.shape[1], -1)
        mask = red.mean(0) > np.median(red.mean(0))
        out[z] = {"voxels": int(mask.sum())}
        for ch in ("red", "green"):
            x = red[:, mask] if ch == "red" else read_plane(session, z, pool, "green").reshape(regressors.shape[1], -1)[:, mask]
            x = high_pass(x)
            x -= x.mean(0)
            with np.errstate(invalid="ignore", divide="ignore"):
                out[z][ch] = np.nan_to_num((b.astype(np.float32) @ x) / np.sqrt((x ** 2).sum(0)))
        del red
    return out


def pooled_r(sx, sxx, sxb, sb, sbb, n):
    """Pearson r of x and b pooled over flies, from per-fly sums (arrays summed over flies)."""
    cov = sxb - sx * sb / n
    vx = sxx - sx ** 2 / n
    vb = sbb - sb ** 2 / n
    with np.errstate(invalid="ignore", divide="ignore"):
        return cov / np.sqrt(vx * vb)


def r_threshold(p: float, n: int) -> float:
    """|r| above which a two-sided Pearson test on n samples has p below the given value."""
    from scipy import stats
    t = stats.t.isf(p / 2, n - 2)
    return float(t / np.sqrt(n - 2 + t ** 2))


def gcamp_toeplitz(n: int = 500) -> np.ndarray:
    """The code's GCaMP6f kernel (deconvolution.py) in a Toeplitz matrix, 20 ms steps."""
    from scipy.linalg import toeplitz
    x = np.arange(0, 50, 1)
    y = 1 * (1 - np.exp(-x / 4)) * (-1 * np.exp(-x / 8)) + 0
    kernel = np.pad(y * -1, (0, n - 50))
    return toeplitz(kernel, r=[0] * n)


def deconvolve(filters: np.ndarray, toe: np.ndarray) -> np.ndarray:
    """deconvolution.py: flip in time, least squares on the kernel, smooth (sigma 3), trim edges, flip back.

    filters: (n_filters, 500), in order of the time shifts.
    """
    from scipy.ndimage import gaussian_filter1d
    flipped = filters[:, ::-1]
    sol = np.linalg.lstsq(toe, flipped.T, rcond=None)[0]
    sol = gaussian_filter1d(sol, sigma=3, axis=0)
    sol[:5, :] = sol[5, :]
    sol[-5:, :] = sol[-5, :]
    return sol[::-1, :].T


def block_layout() -> tuple[int, int]:
    """Number of blocks along the left-right (x) and the other in-plane (y) axis."""
    return (X_CROP[1] - X_CROP[0]) // BLOCK, (Y_CROP[1] - Y_CROP[0]) // BLOCK


def mirror_block(index: np.ndarray) -> np.ndarray:
    """Index, within a plane, of the block mirrored across the midline (x -> 313 - x)."""
    nbx, nby = block_layout()
    bx, by = np.divmod(index, nby)
    return (nbx - 1 - bx) * nby + by


def ridge_scores(X: np.ndarray, y: np.ndarray, folds: list[np.ndarray], alphas) -> np.ndarray:
    """Held-out R2 of ridge regression with intercept, as sklearn's Ridge.score.

    y may be one target (time,) or several (time, m); returns (fold, alpha) or (fold, alpha, m).
    """
    Y = y[:, None] if y.ndim == 1 else y
    out = np.empty((len(folds), len(alphas), Y.shape[1]))
    every = np.arange(len(Y))
    for i, test in enumerate(folds):
        train = np.setdiff1d(every, test)
        xm, ym = X[train].mean(0), Y[train].mean(0)
        u, s, vt = np.linalg.svd(X[train] - xm, full_matrices=False)
        uy = u.T @ (Y[train] - ym)
        xt = X[test] - xm
        sst = ((Y[test] - Y[test].mean(0)) ** 2).sum(0)
        for j, a in enumerate(alphas):
            coef = vt.T @ ((s / (s ** 2 + a))[:, None] * uy)
            pred = xt @ coef + ym
            out[i, j] = 1 - ((Y[test] - pred) ** 2).sum(0) / sst
    return out[..., 0] if y.ndim == 1 else out


def ridge_fit(X: np.ndarray, y: np.ndarray, alpha: float) -> np.ndarray:
    """Ridge coefficients with intercept (intercept not returned)."""
    xm, ym = X.mean(0), y.mean()
    u, s, vt = np.linalg.svd(X - xm, full_matrices=False)
    return vt.T @ (s / (s ** 2 + alpha) * (u.T @ (y - ym)))


def contiguous_folds(n: int, k: int = 5) -> list[np.ndarray]:
    return [np.asarray(f) for f in np.array_split(np.arange(n), k)]


def multi_ridge_r2(D: np.ndarray, Y: np.ndarray, folds: list[np.ndarray], alpha: float) -> np.ndarray:
    """Mean held-out R2 over folds of ridge from design D (time, p) to every column of Y."""
    every = np.arange(len(D))
    r2 = np.zeros(Y.shape[1])
    for test in folds:
        train = np.setdiff1d(every, test)
        dm, ym = D[train].mean(0), Y[train].mean(0)
        dc = D[train] - dm
        coef = np.linalg.solve(dc.T @ dc + alpha * np.eye(D.shape[1]), dc.T @ (Y[train] - ym))
        pred = (D[test] - dm) @ coef + ym
        yt = Y[test]
        sst = ((yt - yt.mean(0)) ** 2).sum(0)
        r2 += 1 - ((yt - pred) ** 2).sum(0) / sst
    return r2 / len(folds)


SHIFTS_S = np.arange(-5000, 5000, 20) / 1000.0   # linear_filters.py: -5 to 5 s in 20 ms steps


def shifted_behaviour(session: dict, key: str, times: np.ndarray) -> np.ndarray:
    """(shift, time) matrix of a behaviour variable at times + each shift, as linear_filters.py.

    key: 'fwd' (Y clipped at 0), 'left' (Z clipped at 0) or 'right' (-Z clipped at 0).
    """
    v = smoothed_velocity(session)
    src = v["Y"] if key == "fwd" else v["Z"]
    at = np.interp(times[None, :] + SHIFTS_S[:, None], v["t"], src, left=np.nan, right=np.nan)
    at = np.nan_to_num(at)
    if key == "fwd" or key == "left":
        return np.clip(at, 0, None)
    return -np.clip(at, None, 0)


def fwhm(filters: np.ndarray, step_s: float = 0.02) -> np.ndarray:
    """Width (s) of the contiguous run around each filter's peak at or above half the peak value."""
    out = np.empty(len(filters))
    for i, f in enumerate(filters):
        p = int(np.argmax(f))
        half = f[p] / 2
        lo = p
        while lo > 0 and f[lo - 1] >= half:
            lo -= 1
        hi = p
        while hi < len(f) - 1 and f[hi + 1] >= half:
            hi += 1
        out[i] = (hi - lo + 1) * step_s
    return out
