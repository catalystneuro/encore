"""Loading and measures for the freely moving mouse session of dandiset 000691.

Scherrer, Lynch, Zhang & Fee (2023), Nature Methods, doi:10.1038/s41592-023-01806-1.

The dandiset holds one NWB file: the raw video of the large-FOV microscope (the Kiloscope), the
traces, masks and centroids of 2948 EXTRACT footprints, and the timestamps of a behaviour video
whose AVI is a second asset. Both are streamed from the archive at the pinned version: small
datasets through h5py and remfile, the AVI (105 MB), the masks (9 MB compressed) and the movie
(15 GB) by HTTP range requests into memory, whose chunks are decompressed here. Nothing is written
to disk.

Where the parameters come from. The claims file (claims/000691/10.1038-s41592-023-01806-1.yaml)
fixes the method; it cites the Methods of the paper and its code, GitHub
FeeLab/Feescope-Paper-Code at commit d596646b16a505907203828d8026feb7736ca69c (`CODE_COMMIT`).
Each constant below names its source. A detail that neither fixes and that cannot change a
result is marked "standard choice".

- Tracking (claims file, common method; f3+sf8/mouse_position_tracking.m): the video is read from
  64 s at the AVI's nominal 30 frames/s (frame 1920); each frame is rotated by 86.79 degrees
  (bilinear, MATLAB's imrotate with a loose bounding box) and cropped to rows 229 to 560 and
  columns 101 to 378; the mouse is the largest 8-connected region of pixels whose squared RGB
  distance from (0, 3, 4) is below 1600, and its centroid (1-based, as regionprops) is
  interpolated to the imaging timestamps. The quadrant is the nearest side of the rectangle x 44
  to 228, y 34 to 270; linear position runs around the loop at 0.508 m per 290 pixels; the octant
  halves each side at the rectangle's midline. Only the cropped region is rotated, by sampling the
  rotated frame's coordinates in the original (scipy's rotation geometry, checked in the notebook
  against a full rotation).
- Unwrapping. The claims file says linear position is unwrapped; here it is unwrapped by the loop
  length. The code calls MATLAB's unwrap(s*100, max(s)*100/2), which corrects each step larger
  than the tolerance by the multiple of 2 pi (in cm) that brings it within pi, so each lap's jump
  of the loop length leaves a residual step of up to 3.14 cm; `behaviour(..., unwrap="code")`
  gives that variant.
- Running, direction, activity (claims file; all decoding scripts): speed is the absolute change
  of unwrapped position per frame, moving mean over 30 frames (MATLAB movmean: 15 before, 14
  after, shrinking at the ends); running frames have speed above its median; direction is the
  sign of the moving mean of the change; activity is the moving maximum of each trace over 30
  frames.
- Decoders (claims file; quadrant_direction_decoding.m and the others): one-against-all linear
  SVMs minimizing the mean hinge loss plus lambda / 2 |w|^2 (MATLAB fitcecoc with templateLinear);
  lambda 3.2e-7 for quadrant and direction in quadrant_direction_decoding.m, 6.75e-8 elsewhere.
  Each fit circularly shifts frames and labels by round(rand * n), trains on the first half less
  1% at its end and tests on the second half less 1% at its end. MATLAB's solver, by its
  documented default, is dual SGD with 10 passes for more than 100 predictors and BFGS to
  convergence for 100 or fewer; here scikit-learn's SGDClassifier (hinge, alpha = lambda, 10
  passes) and LinearSVC (the same objective, exactly) take those places. A decoding matrix is the
  confusion matrix normalized by the count of each actual class, averaged over fits where the
  class occurs; its median accuracy is the median of the diagonal.
- Shuffle (claims file; Methods, paragraph 5): each footprint's activity is circularly shifted by
  its own offset, drawn uniformly over the n possible offsets; labels are not shifted.
- Footprint position (claims file, fig2l-local-decoding-map; subregion_map_quaddir.m): the first
  pixel, in MATLAB's column order, at which the footprint's weight equals 1. The NWB masks are
  stored transposed (axis 1 is MATLAB's column, axis 2 its row), so that pixel is the first one in
  C order of the stored mask; positions are returned as (MATLAB row, MATLAB column), 1-based.
- Local decoding maps (claims file, fig2l and ed9c; subregion_map_*.m): the code's grid, a point
  used when at least 32 footprints lie within the radius, the 32 nearest footprints decoded; the
  null decoders use 32 footprints drawn at random and shuffled. The reduced runs of the decoding
  notebooks (a coarser grid, fewer fits, fewer null decoders) are choices made here and decide no
  outcome.
- Pixel sizes: 5.94 um per pixel in sf3/widefield/analysis.m and 5.35 um per pixel in
  f2+sf4/wf_analysis_secondorder.m, both for the Kiloscope (claims file, abstract-kiloscope-fov).
  The NWB file gives none.
- NMF (claims file, ed8-coactive-distributed; ridgeline_nmf_grouping.m): 8 components,
  multiplicative updates, 4 replicates, the best kept. MATLAB's nnmf stops at 100 iterations by
  default; scikit-learn's NMF with solver "mu", max_iter 100 and tol 1e-7 is used, with random
  initial values (standard choice). As MATLAB does, H's rows are scaled to unit length.
- Place maps (claims file, ed10-localized-activity; sf9/place_cells.m): frames with speed above
  its 80th percentile; a footprint is active when its trace exceeds 1% of its maximum over those
  frames; maps of the fraction of time active per video pixel, smoothed by a Gaussian of 10
  pixels in a 101 pixel window (edges replicated) and divided by the smoothed occupancy mask plus
  0.001; entropy of mean activity over 100 bins of linear position between its 1st and 99th
  percentiles, over the bins the mouse occupies (standard choice: the code's division by an
  empty bin's zero occupancy would make every entropy 0).
- Motion (claims file, ed7-motion-small): rigid registration with NoRMCorre's defaults, written
  here after NoRMCorre's normcorre.m and dftregistration.m (no MATLAB): each frame is registered
  to a template by the peak of the cross-correlation within 50 pixels, refined by an upsampled
  DFT at 1/50 pixel; the template starts as the median of the 100 middle frames after registering
  them to their median, and is updated every 200 frames to the mean of the medians of the
  corrected frames of the last 50 such bins. These are NoRMCorre's defaults as recalled here
  (us_fac 50, max_shift 50, init_batch 100, bin_width 200, buffer_width 50): standard choices.
- PSF fits (claims file, fig1e and fig1f; f2+sf4/*_analysis_secondorder.m): a rotated 2D
  Gaussian with the code's second-order pixel correction, fitted by bounded least squares from
  the code's starting point (scipy's "trf", the closest analogue of lsqcurvefit's
  trust-region-reflective algorithm), with the code's tolerances and limits; FWHM is 2.355 times
  each width. The images are read in the order of their file number; the code sorts them by file
  date, which a git checkout does not keep, and the Featherscope regions name their image
  (beadsN is slice N + 1), which the notebook checks.
- Illumination profiles (claims file, ed2b and ed2c; sf3/*/analysis.m): images packed as RGB565
  are unpacked as green * 8 + blue / 8; the centre is the intensity-weighted mean pixel; profiles
  are binned at 1 um out to rLength (500 or 2000 um, exclusive), smoothed by a moving median and
  normalized to their 99th percentile (MATLAB's prctile, numpy's "hazen" method).
"""

from __future__ import annotations

import io
import time
import warnings
import zlib
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import png
import remfile
import requests
import scipy.fft as sfft
from dandi.dandiapi import DandiAPIClient
from joblib import Parallel, delayed
from scipy import ndimage
from scipy.optimize import least_squares
from sklearn.exceptions import ConvergenceWarning
from sklearn.linear_model import SGDClassifier
from sklearn.svm import LinearSVC

DANDISET_ID = "000691"
DANDISET_VERSION = "0.260827.1358"
NWB_PATH = "sub-4mm-mouse-1/sub-4mm-mouse-1_image+ophys.nwb"
VIDEO_SERIES = "acquisition/Video: home_arena_2021-07-26T13_50_50"
MOVIE = "acquisition/TwoPhotonSeries/data"
MASKS = "processing/ophys/ImageSegmentation/PlaneSegmentation/image_mask"

CODE_REPO = "https://raw.githubusercontent.com/FeeLab/Feescope-Paper-Code"
CODE_COMMIT = "d596646b16a505907203828d8026feb7736ca69c"

UM_PER_PIXEL_ILLUMINATION = 5.94   # sf3/widefield/analysis.m (Kiloscope)
UM_PER_PIXEL_BEADS = 5.35          # f2+sf4/wf_analysis_secondorder.m (Kiloscope)

# Tracking, mouse_position_tracking.m
FIRST_VIDEO_FRAME = 1920           # CurrentTime = 64 s at the AVI's nominal 30 frames/s
ROTATION_DEG = -3.21 + 90          # rAngle
CROP_ROWS = (229, 560)             # ymin, ymax (1-based, inclusive)
CROP_COLS = (101, 378)             # xmin, xmax
DARK_RGB = np.array([0, 3, 4])
DARK_LIMIT = 1600                  # squared RGB distance
RECT = (44, 228, 34, 270)          # xmin, xmax, ymin, ymax of the track, in the cropped frame
M_PER_PIXEL = 0.508 / 290          # lf
SMOOTH = 30                        # frames, for speed, direction and the moving maximum
LAMBDA_QUAD_DIR = 3.2e-7           # quadrant_direction_decoding.m
LAMBDA_OTHER = 6.75e-8             # octant_decoding.m, subset_sweep.m, subregion_map_*.m
HOLDOUT = 0.5
BUFFER = 0.01
SGD_EPOCHS = 10                    # MATLAB templateLinear default for > 100 predictors
EXACT_MAX_PREDICTORS = 100
EXACT_MAX_ITER = 10000


# --- archive -----------------------------------------------------------------------------------

def asset_urls(version: str = DANDISET_VERSION) -> dict[str, str]:
    """Path to streaming URL of every asset at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, version)
        return {a.path: a.get_content_url(follow_redirects=1, strip_query=True)
                for a in dandiset.get_assets()}


def _text(value) -> str:
    return value.decode() if isinstance(value, bytes) else str(value)


def open_nwb(urls: dict[str, str]) -> h5py.File:
    return h5py.File(remfile.File(urls[NWB_PATH]), "r")


def load_session(f: h5py.File) -> dict:
    """Traces, centroids, timestamps and descriptive metadata of the session."""
    ps = "processing/ophys/ImageSegmentation/PlaneSegmentation"
    rrs = "processing/ophys/DfOverF/RoiResponseSeries"
    ip = "general/optophysiology/ImagingPlane"
    video = f[VIDEO_SERIES]
    meta = {
        "session_description": _text(f["session_description"][()]),
        "experiment_description": _text(f["general/experiment_description"][()]),
        "device_description": _text(f["general/devices/Microscope/description"][()]),
        "imaging_series": _text(f["acquisition/TwoPhotonSeries"].attrs["neurodata_type"]),
        "imaging_description": _text(f["acquisition/TwoPhotonSeries"].attrs["description"]),
        "video_description": _text(video.attrs["description"]),
        "video_external_file": _text(video["external_file"][0]),
        "indicator": _text(f[ip + "/indicator"][()]),
        "location": _text(f[ip + "/location"][()]),
        "excitation_lambda": float(f[ip + "/excitation_lambda"][()]),
        "imaging_plane_fields": sorted(f[ip].keys()),
        "grid_spacing_present": "grid_spacing" in f[ip],
        "virus": _text(f["general/virus"][()]),
        "surgery": _text(f["general/surgery"][()]).strip(),
        "subject": {k: _text(f["general/subject"][k][()]) for k in f["general/subject"].keys()},
        "trace_description": _text(f[rrs].attrs["description"]),
        "trace_unit": _text(f[rrs + "/data"].attrs["unit"]),
        "segmentation_type": _text(f["processing/ophys/ImageSegmentation"].attrs["neurodata_type"]),
        "cellfind_min_snr": float(f["processing/ophys/ImageSegmentation"].attrs["cellfind_min_snr"]),
        "plane_segmentation_columns": [_text(c) for c in f[ps].attrs["colnames"]],
        "movie_shape": f[MOVIE].shape,
        "movie_dtype": str(f[MOVIE].dtype),
        "movie_chunks": f[MOVIE].chunks,
        "mask_shape": f[MASKS].shape,
    }
    return {
        "meta": meta,
        "t_img": f["acquisition/TwoPhotonSeries/timestamps"][:],
        "t_trace": f[rrs + "/timestamps"][:],
        "traces": f[rrs + "/data"][:].astype(np.float32),
        "rois": f[rrs + "/rois"][:],
        "ids": f[ps + "/id"][:],
        "centroids": f[ps + "/ROICentroids"][:],
        "t_video": video["timestamps"][:],
    }


def _chunk_index(dataset: h5py.Dataset) -> list[tuple[tuple, int, int]]:
    """(chunk offset, byte offset, size) of every stored chunk of a dataset."""
    out = []
    dataset.id.chunk_iter(lambda c: out.append((tuple(c.chunk_offset), c.byte_offset, c.size)))
    return out


def _get_range(url: str, lo: int, hi: int, parts: int = 8) -> bytes:
    """Bytes lo to hi (exclusive) of a URL, in `parts` parallel range requests."""
    edges = np.linspace(lo, hi, parts + 1).astype(np.int64)

    def get(a, b):
        for attempt in range(5):
            try:
                r = requests.get(url, headers={"Range": f"bytes={a}-{b - 1}"}, timeout=300)
                r.raise_for_status()
                if len(r.content) == b - a:
                    return r.content
            except requests.RequestException:
                pass
            time.sleep(2 * (attempt + 1))
        raise IOError(f"could not read bytes {a} to {b} of {url}")

    with ThreadPoolExecutor(parts) as ex:
        return b"".join(ex.map(get, edges[:-1], edges[1:]))


def read_masks(url: str, f: h5py.File) -> dict:
    """Every footprint's mask as sparse pixels: footprint, axis-1 index, axis-2 index, weight
    (non-zero weights only), read by downloading the masks' compressed chunks in one request."""
    ds = f[MASKS]
    n, d1, d2 = ds.shape
    c0, c1, c2 = ds.chunks
    index = _chunk_index(ds)
    lo = min(b for _, b, _ in index)
    hi = max(b + s for _, b, s in index)
    buf = _get_range(url, lo, hi, parts=4)
    roi, a1, a2, w = [], [], [], []
    for (o0, o1, o2), b, s in index:
        chunk = np.frombuffer(zlib.decompress(buf[b - lo:b - lo + s]), dtype="<f4").reshape(c0, c1, c2)
        chunk = chunk[:min(c0, n - o0), :min(c1, d1 - o1), :min(c2, d2 - o2)]
        k = np.nonzero(chunk)
        roi.append(k[0] + o0), a1.append(k[1] + o1), a2.append(k[2] + o2), w.append(chunk[k])
    roi, a1, a2, w = (np.concatenate(v) for v in (roi, a1, a2, w))
    order = np.lexsort((a2, a1, roi))
    return {"roi": roi[order], "a1": a1[order], "a2": a2[order], "w": w[order],
            "shape": (n, d1, d2), "n_chunks": len(index), "compressed_bytes": hi - lo}


def mask_positions(m: dict) -> dict:
    """Per footprint: the code's position (first pixel in MATLAB's column order where the weight
    equals 1; NaN where none does), the weighted centroid and the maximum weight, each as (MATLAB
    row, MATLAB column) = (axis 2, axis 1) + 1."""
    n = m["shape"][0]
    roi, a1, a2, w = m["roi"], m["a1"], m["a2"], m["w"]
    peak = np.full((n, 2), np.nan)
    is1 = w == 1
    first = {}
    for r, x, y in zip(roi[is1], a1[is1], a2[is1]):    # sorted by (roi, a1, a2): C order
        first.setdefault(r, (y + 1, x + 1))
    for r, v in first.items():
        peak[r] = v
    tot = np.bincount(roi, weights=w, minlength=n)
    cen = np.stack([np.bincount(roi, weights=w * (a2 + 1), minlength=n) / tot,
                    np.bincount(roi, weights=w * (a1 + 1), minlength=n) / tot], 1)
    wmax = np.zeros(n)
    np.maximum.at(wmax, roi, w)
    return {"peak": peak, "centroid": cen, "max_weight": wmax,
            "n_pixels": np.bincount(roi, minlength=n)}


# --- tracking and labels -----------------------------------------------------------------------

def crop_rotation_coords(frame_shape: tuple[int, int]) -> np.ndarray:
    """Coordinates, in the original frame, of the pixels of the code's crop of the rotated frame
    (scipy.ndimage.rotate's geometry with reshape=True)."""
    a = np.deg2rad(ROTATION_DEG)
    c, s = np.cos(a), np.sin(a)
    rot = np.array([[c, s], [-s, c]])
    ip = np.array(frame_shape[:2])
    corners = rot @ np.array([[0, 0, ip[0], ip[0]], [0, ip[1], 0, ip[1]]])
    op = (np.ptp(corners, axis=1) + 0.5).astype(int)
    offset = (ip - 1) / 2 - rot @ ((op - 1) / 2)
    rows, cols = np.mgrid[CROP_ROWS[0] - 1:CROP_ROWS[1], CROP_COLS[0] - 1:CROP_COLS[1]]
    return (rot @ np.stack([rows.ravel(), cols.ravel()]) + offset[:, None]).reshape(2, *rows.shape)


def rotate_crop(rgb: np.ndarray, coords: np.ndarray) -> np.ndarray:
    """The code's crop of the frame rotated bilinearly (zero outside), rounded to uint8. Same as
    ndimage.map_coordinates(order=1, cval=0) on each channel."""
    return _bilinear(rgb, _bilinear_weights(coords, rgb.shape[:2]))


def _bilinear_weights(coords: np.ndarray, shape: tuple[int, int]):
    r, c = coords
    r0, c0 = np.floor(r).astype(int), np.floor(c).astype(int)
    fr, fc = r - r0, c - c0
    taps = []
    for dr, dc, w in [(0, 0, (1 - fr) * (1 - fc)), (0, 1, (1 - fr) * fc), (1, 0, fr * (1 - fc)), (1, 1, fr * fc)]:
        rr, cc = r0 + dr, c0 + dc
        inside = (rr >= 0) & (rr < shape[0]) & (cc >= 0) & (cc < shape[1])
        taps.append((np.clip(rr, 0, shape[0] - 1), np.clip(cc, 0, shape[1] - 1),
                     np.where(inside, w, 0).astype(np.float32)[..., None]))
    return taps


def _bilinear(rgb: np.ndarray, taps) -> np.ndarray:
    out = sum(rgb[rr, cc].astype(np.float32) * w for rr, cc, w in taps)
    return np.clip(np.round(out), 0, 255).astype(np.uint8)


def _largest_dark_blob(crop: np.ndarray):
    dark = ((crop.astype(np.int32) - DARK_RGB) ** 2).sum(-1) < DARK_LIMIT
    labels, n = ndimage.label(dark, structure=np.ones((3, 3)))
    if n == 0:
        return np.nan, np.nan, 0
    sizes = np.bincount(labels.ravel())[1:]
    k = int(sizes.argmax()) + 1
    cy, cx = ndimage.center_of_mass(dark, labels, k)
    return cx + 1, cy + 1, int(sizes.max())


def track_mouse(url: str, keep_frames=()) -> dict:
    """Per video frame from FIRST_VIDEO_FRAME on: the centroid (x = column, y = row, 1-based, in
    the code's rotated crop) and area of the largest dark blob; the number of frames, the frame
    size and the nominal frame rate; and the rotated crops of the frames in `keep_frames`."""
    import av

    container = av.open(io.BytesIO(requests.get(url, timeout=600).content))
    stream = container.streams.video[0]
    nominal_rate = float(stream.average_rate)
    xs, ys, areas, kept, shape, coords, n = [], [], [], {}, None, None, 0
    keep_frames = set(keep_frames)
    for i, frame in enumerate(container.decode(video=0)):
        n += 1
        if i < FIRST_VIDEO_FRAME and i not in keep_frames:
            continue
        rgb = frame.to_ndarray(format="rgb24")
        if coords is None:
            shape, coords = rgb.shape, crop_rotation_coords(rgb.shape)
            taps = _bilinear_weights(coords, rgb.shape[:2])
        crop = _bilinear(rgb, taps)
        if i in keep_frames:
            kept[i] = (rgb, crop)
        if i < FIRST_VIDEO_FRAME:
            continue
        x, y, a = _largest_dark_blob(crop)
        xs.append(x), ys.append(y), areas.append(a)
    container.close()
    pad = np.full(FIRST_VIDEO_FRAME, np.nan)
    return {"x": np.concatenate([pad, xs]), "y": np.concatenate([pad, ys]),
            "area": np.concatenate([np.zeros(FIRST_VIDEO_FRAME), areas]), "n_frames": n,
            "frame_shape": shape, "nominal_rate": nominal_rate, "frames": kept}


def movmean(v: np.ndarray, k: int = SMOOTH) -> np.ndarray:
    """MATLAB movmean(v, k): k // 2 before, the rest after, shrinking at the ends."""
    before = k // 2
    after = k - 1 - before
    cs = np.concatenate([[0.0], np.cumsum(v, dtype=np.float64)])
    i = np.arange(len(v))
    lo, hi = np.maximum(i - before, 0), np.minimum(i + after + 1, len(v))
    return (cs[hi] - cs[lo]) / (hi - lo)


def moving_max(traces: np.ndarray) -> np.ndarray:
    """MATLAB movmax(traces, 30) along time (15 before, 14 after, shrinking at the ends)."""
    return ndimage.maximum_filter1d(traces, SMOOTH, axis=0, mode="nearest")


def behaviour(t_img: np.ndarray, t_video: np.ndarray, track: dict, unwrap: str = "loop") -> dict:
    """Position and labels at the imaging frames within the tracked video. `unwrap` is "loop"
    (the claims file: unwrap by the loop length) or "code" (MATLAB's unwrap of s * 100 with
    tolerance max(s) * 100 / 2, which brings each large step within pi cm by multiples of 2 pi;
    numpy's unwrap does the same)."""
    keep = np.isfinite(track["x"])
    tv = t_video[keep]
    sel = np.flatnonzero((t_img > tv[0]) & (t_img < tv[-1]))
    x = np.interp(t_img[sel], tv, track["x"][keep])
    y = np.interp(t_img[sel], tv, track["y"][keep])
    xmin, xmax, ymin, ymax = RECT
    xl, yl = xmax - xmin, ymax - ymin
    quadrant = np.stack([abs(x - xmin), abs(y - ymin), abs(x - xmax), abs(y - ymax)], 1).argmin(1)
    s = np.select([quadrant == 0, quadrant == 1, quadrant == 2, quadrant == 3],
                  [ymax - y, yl + x - xmin, yl + xl + y - ymin, 2 * yl + xl + xmax - x]) * M_PER_PIXEL
    xmid, ymid = (xmin + xmax) / 2, (ymin + ymax) / 2
    octant = np.select([quadrant == 0, quadrant == 1, quadrant == 2, quadrant == 3],
                       [0 + (y < ymid), 2 + (x > xmid), 4 + (y > ymid), 6 + (x < xmid)]).astype(int)
    perimeter = 2 * (xl + yl) * M_PER_PIXEL
    if unwrap == "loop":
        sunwrap = np.unwrap(s * 2 * np.pi / perimeter) * perimeter / (2 * np.pi)
    else:
        sunwrap = np.unwrap(s * 100, discont=s.max() * 100 / 2) / 100
    step = np.diff(sunwrap, append=sunwrap[-1])
    step[-1] = step[-2]
    speed = movmean(np.abs(step))
    direction = np.where(movmean(step) > 0, 1, -1)
    return {"sel": sel, "t": t_img[sel], "x": x, "y": y, "quadrant": quadrant, "octant": octant,
            "s": s, "sunwrap": sunwrap, "perimeter": perimeter, "speed": speed,
            "direction": direction, "running": speed > np.median(speed)}


def load_behaviour(urls: dict[str, str], S: dict, keep_frames=()) -> tuple[dict, dict]:
    """Track the mouse in the session's behaviour video and derive the labels: (track, behaviour)."""
    video_url = next(u for p, u in urls.items() if p.endswith(".avi"))
    track = track_mouse(video_url, keep_frames=keep_frames)
    return track, behaviour(S["t_img"], S["t_video"], track)


def quad_dir_labels(b: dict) -> np.ndarray:
    """Quadrant and direction as eight classes, 0-based: 2 * quadrant + (direction > 0)."""
    return 2 * b["quadrant"] + (b["direction"] > 0)


# --- decoders ----------------------------------------------------------------------------------

def _solver(X, solver):
    if solver is None:
        solver = "exact" if X.shape[1] <= EXACT_MAX_PREDICTORS else "sgd"
    return solver


def fit_sgd(X, y, lam, seed):
    """One-against-all linear SVM by SGD, `SGD_EPOCHS` passes: (weights, intercepts, classes)."""
    model = SGDClassifier(loss="hinge", penalty="l2", alpha=lam, max_iter=SGD_EPOCHS, tol=None,
                          random_state=seed).fit(X, y)
    return model.coef_, model.intercept_, model.classes_


def fit_exact(X, y, lam, seed, max_iter=EXACT_MAX_ITER):
    """One-against-all linear SVM minimizing mean hinge + lam / 2 |w|^2, solved by liblinear on
    features scaled by s: with C = 1 / (lam s^2 n) the scaled problem has the same solution.
    Returns (weights in the original units, intercepts, classes), and whether liblinear stopped by
    its tolerance before `max_iter`. LinearSVC also penalizes the intercept, weakly at an
    intercept scaling of 10; MATLAB does not."""
    s = 1 / X.std()
    model = LinearSVC(loss="hinge", C=1 / (lam * s * s * len(y)), intercept_scaling=10,
                      max_iter=max_iter, random_state=seed)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", ConvergenceWarning)
        model.fit(X * s, y)
    return (model.coef_ * s, model.intercept_, model.classes_), bool(model.n_iter_ < max_iter)


def predict(model, X):
    W, b, classes = model
    return classes[np.argmax(X @ W.T + b, axis=1)]


def _split(X, labels, shift):
    """Training and test parts after the circular shift, with the 1% buffers."""
    n = len(labels)
    Xs, ls = np.roll(X, shift, axis=0), np.roll(labels, shift)
    half, buffer = round(n * HOLDOUT), round(n * BUFFER)
    return Xs[:half - buffer], ls[:half - buffer], Xs[half:n - buffer], ls[half:n - buffer]


def confusion(predicted, truth, n_class):
    """Counts (predicted, actual) and the matrix normalized by each actual class's count."""
    h = np.zeros((n_class, n_class))
    np.add.at(h, (predicted, truth), 1)
    count = h.sum(0)
    return h / np.where(count == 0, 1, count), count > 0


def one_fit(X, labels, n_class, lam, solver, shift, seed):
    """One decoder: its normalized confusion matrix, which classes occur in the test part, and
    whether the exact solver stopped by its tolerance (always True for SGD)."""
    Xtr, ytr, Xte, yte = _split(X, labels, shift)
    if solver == "exact":
        model, converged = fit_exact(Xtr, ytr, lam, seed)
    else:
        model, converged = fit_sgd(Xtr, ytr, lam, seed), True
    h, present = confusion(predict(model, Xte), yte, n_class)
    return h, present, converged


def shuffle_columns(X: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    """Each footprint's activity circularly shifted by its own offset, 1 to n (randi(n)), as
    MATLAB's circshift(x, k): element i moves to i + k. Returned in Fortran order; fastest when X
    is Fortran-ordered too (columns contiguous)."""
    n = len(X)
    offsets = rng.integers(1, n + 1, X.shape[1])
    out = np.empty_like(X, order="F")
    for j, k in enumerate(offsets % n):
        out[:k, j] = X[n - k:, j]
        out[k:, j] = X[:n - k, j]
    return out


def decoding_matrix(X, labels, n_class, lam, n_fits, rng, solver=None, n_jobs=1) -> dict:
    """The average decoding matrix of `n_fits` fits (each class averaged over the fits where it
    occurs), its median accuracy, and the per-fit diagonals. The random numbers are drawn in
    order before the fits, so `n_jobs` (parallel fits, in threads) does not change the result."""
    solver = _solver(X, solver)
    n = len(labels)
    draws = [(int(round(rng.random() * n)), int(rng.integers(2**31))) for _ in range(n_fits)]
    if n_jobs == 1:
        out = [one_fit(X, labels, n_class, lam, solver, *d) for d in draws]
    else:
        out = Parallel(n_jobs=n_jobs, prefer="threads")(
            delayed(one_fit)(X, labels, n_class, lam, solver, *d) for d in draws)
    H = np.array([h for h, _, _ in out])
    P = np.array([p for _, p, _ in out])
    avg = H.sum(0) / np.where(P.sum(0) == 0, np.nan, P.sum(0))[None, :]
    diag = np.diagonal(avg)
    return {"matrix": avg, "median": float(np.median(diag)), "diag": diag,
            "fit_diag": np.where(P, np.diagonal(H, axis1=1, axis2=2), np.nan),
            "absent": int((~P).sum()), "at_iteration_limit": int(sum(not c for _, _, c in out))}


def _null_one(X, labels, n_class, lam, solver, n_fits, seed):
    rng = np.random.default_rng(seed)
    return decoding_matrix(shuffle_columns(X, rng), labels, n_class, lam, n_fits, rng, solver)["median"]


def null_medians(X, labels, n_class, lam, n_null, n_fits, seed: int, solver=None, n_jobs=-1) -> np.ndarray:
    """Median accuracies of `n_null` decoders, each on its own shuffle and with `n_fits` fits,
    each from its own generator spawned from `seed`."""
    solver = _solver(X, solver)
    seeds = np.random.SeedSequence(seed).spawn(n_null)
    return np.array(Parallel(n_jobs=n_jobs, prefer="threads")(
        delayed(_null_one)(X, labels, n_class, lam, solver, n_fits, s) for s in seeds))


# --- local decoding maps (fig2l, ed9c) ----------------------------------------------------------

def map_grid(every: int = 1) -> np.ndarray:
    """The map points of subregion_map_*.m, (MATLAB row, column): r * 5 + 1 and c * 5 + 140 for r
    in 1 to round(607 / 5) and c in 1 to round(560 / 5). `every` keeps every k-th point along
    each axis (a coarser grid, for a reduced run)."""
    rs = np.arange(1, round((608 - 1) / 5) + 1)[every - 1::every]
    cs = np.arange(1, round((700 - 140) / 5) + 1)[every - 1::every]
    return np.array([(r * 5 + 1, c * 5 + 140) for r in rs for c in cs], dtype=float)


def map_values(X, labels, n_class, lam, positions, grid, radius, n_near, n_fits, rng, n_jobs=4):
    """At each grid point with at least `n_near` footprints within `radius` pixels, the median
    accuracy of the average matrix of `n_fits` fits on its `n_near` nearest footprints. Returns
    (used points, values); footprints without a position are left out."""
    ok = ~np.isnan(positions).any(1)
    idx, P = np.flatnonzero(ok), positions[ok]
    used, values = [], []
    for g in grid:
        d = np.hypot(P[:, 0] - g[0], P[:, 1] - g[1])
        if (d <= radius).sum() < n_near:
            continue
        cols = idx[np.argsort(d, kind="stable")[:n_near]]
        used.append(g)
        values.append(decoding_matrix(X[:, cols], labels, n_class, lam, n_fits, rng, n_jobs=n_jobs)["median"])
    return np.array(used), np.array(values)


def _null_local_one(X, labels, n_class, lam, n_cols, n_fits, seed):
    rng = np.random.default_rng(seed)
    cols = rng.choice(X.shape[1], n_cols, replace=False)
    return decoding_matrix(shuffle_columns(X[:, cols], rng), labels, n_class, lam, n_fits, rng)["median"]


def null_local(X, labels, n_class, lam, n_null, n_cols, n_fits, seed: int, n_jobs=4) -> np.ndarray:
    """Median accuracies of `n_null` decoders, each on `n_cols` footprints drawn anew and shuffled
    (Methods, paragraph 5), with `n_fits` fits each."""
    seeds = np.random.SeedSequence(seed).spawn(n_null)
    return np.array(Parallel(n_jobs=n_jobs, prefer="threads")(
        delayed(_null_local_one)(X, labels, n_class, lam, n_cols, n_fits, s) for s in seeds))


def benjamini_hochberg(p: np.ndarray, q: float = 0.05) -> np.ndarray:
    """Which p-values are significant at false discovery rate `q` (Benjamini-Hochberg)."""
    p = np.asarray(p, float)
    order = np.argsort(p)
    passed = p[order] <= q * np.arange(1, len(p) + 1) / len(p)
    k = np.flatnonzero(passed).max() + 1 if passed.any() else 0
    sig = np.zeros(len(p), bool)
    sig[order[:k]] = True
    return sig


# --- NMF and place maps ------------------------------------------------------------------------

def nmf_replicates(T: np.ndarray, n_components: int, replicates: int, seed: int) -> dict:
    """Multiplicative-update NMF of T (frames x footprints), `replicates` random starts, the one
    with the smallest error kept; H's rows scaled to unit length (MATLAB nnmf)."""
    from sklearn.decomposition import NMF

    rng = np.random.default_rng(seed)
    fits = []
    for _ in range(replicates):
        model = NMF(n_components, solver="mu", init="random", max_iter=100, tol=1e-7,
                    random_state=int(rng.integers(2**31)))
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ConvergenceWarning)
            W = model.fit_transform(T)
        fits.append((float(model.reconstruction_err_), W, model.components_, model.n_iter_))
    err, W, H, n_iter = min(fits, key=lambda z: z[0])
    norm = np.linalg.norm(H, axis=1)
    return {"W": W * norm[None, :], "H": H / norm[:, None], "errors": [z[0] for z in fits],
            "n_iter": [z[3] for z in fits]}


def nmf_groups(H: np.ndarray) -> np.ndarray:
    """ridgeline_nmf_grouping.m: each footprint goes to the component in which its weight ranks
    highest among footprints (first component on a tie)."""
    rank = np.argsort(np.argsort(H, axis=1, kind="stable"), axis=1, kind="stable")
    return rank.argmax(0)


def place_measures(traces: np.ndarray, b: dict, fast: np.ndarray, sigma: float = 10,
                   keep_maps: int = 12) -> dict:
    """place_cells.m: per footprint, the entropy of its mean activity over 100 bins of linear
    position and the peak of its smoothed map of the fraction of time active; the maps of the
    `keep_maps` footprints with the highest peaks."""
    A = traces[fast].astype(np.float64)
    s = b["s"][fast]
    smin, smax = np.percentile(s, [1, 99], method="hazen")
    sb = np.clip((s - smin) / (smax - smin), 0, 0.999)
    sb = np.floor(sb * 100).astype(int)
    occ = np.bincount(sb, minlength=100).astype(float)
    place = np.zeros((100, A.shape[1]))
    np.add.at(place, sb, A)
    # The code divides by the occupancy of every bin; an empty bin makes the column NaN and its
    # entropy 0. Here empty bins are left out (reported as `empty_bins`).
    used = occ > 0
    place = place[used] / occ[used, None]
    p = place / place.sum(0)
    with np.errstate(divide="ignore", invalid="ignore"):
        entropy = -np.nansum(np.where(p > 0, p * np.log2(p), 0), axis=0)
    x, y = b["x"], b["y"]
    xdim, ydim = int(np.ceil(x.max() - x.min())), int(np.ceil(y.max() - y.min()))
    xbin = np.minimum(np.floor(x[fast] - x.min()).astype(int), xdim - 1)
    ybin = np.minimum(np.floor(y[fast] - y.min()).astype(int), ydim - 1)
    res = np.zeros((ydim, xdim))
    np.add.at(res, (ybin, xbin), 1)
    smooth = dict(sigma=sigma, truncate=50 / sigma, mode="nearest")
    nannorm = ndimage.gaussian_filter((res > 0).astype(float), **smooth)
    events = A > 0.01 * A.max(0)
    flat = ybin * xdim + xbin
    peaks = np.zeros(A.shape[1])
    for start in range(0, A.shape[1], 64):
        cols = slice(start, start + 64)
        counts = np.zeros((ydim * xdim, events[:, cols].shape[1]))
        np.add.at(counts, flat, events[:, cols])
        with np.errstate(invalid="ignore", divide="ignore"):
            rate = counts.reshape(ydim, xdim, -1) / res[:, :, None]
        rate = np.nan_to_num(rate)
        filt = ndimage.gaussian_filter(rate, sigma=(sigma, sigma, 0), truncate=50 / sigma, mode="nearest")
        peaks[cols] = (filt / (nannorm[:, :, None] + 0.001)).max((0, 1))
    top = np.argsort(peaks)[::-1][:keep_maps]
    maps = {}
    for i in top:
        counts = np.zeros(ydim * xdim)
        np.add.at(counts, flat, events[:, i])
        with np.errstate(invalid="ignore", divide="ignore"):
            rate = np.nan_to_num(counts.reshape(ydim, xdim) / res)
        maps[int(i)] = ndimage.gaussian_filter(rate, **smooth) / (nannorm + 0.001)
    return {"entropy": entropy, "peak": peaks, "maps": maps, "occupancy": occ,
            "empty_bins": int((~used).sum()), "n_frames": int(fast.sum()),
            "max_entropy": float(np.log2(used.sum()))}


# --- motion ------------------------------------------------------------------------------------

def _dftups(X: np.ndarray, n_out: int, us: int, roff: float, coff: float) -> np.ndarray:
    """dftregistration.m's dftups: the upsampled inverse DFT of X in an n_out x n_out window."""
    nr, nc = X.shape
    kc = sfft.ifftshift(np.arange(nc)) - nc // 2
    kr = sfft.ifftshift(np.arange(nr)) - nr // 2
    o = np.arange(n_out)
    kern_c = np.exp((-2j * np.pi / (nc * us)) * np.outer(kc, o - coff))
    kern_r = np.exp((-2j * np.pi / (nr * us)) * np.outer(o - roff, kr))
    return kern_r @ X @ kern_c


def register_frames(frames: np.ndarray, template_ft: np.ndarray, us: int = 50, max_shift: int = 50,
                    workers: int = -1) -> tuple[np.ndarray, np.ndarray]:
    """Rigid shifts (row, column, in pixels) that align each frame to the template, by
    dftregistration (peak of the cross-correlation within `max_shift`, refined by an upsampled DFT
    at 1 / `us` pixel), and the frames shifted by them (Fourier shift). The returned shift is the
    correction: minus the frame's displacement from the template."""
    F = sfft.fft2(frames.astype(np.float32), axes=(1, 2), workers=workers)
    X = np.conj(F)
    X *= template_ft.astype(np.complex64)[None]
    cc = sfft.ifft2(X, axes=(1, 2), workers=workers)
    nf, nr, nc = F.shape
    rr = np.r_[0:max_shift + 1, nr - max_shift:nr]
    cr = np.r_[0:max_shift + 1, nc - max_shift:nc]
    window = np.abs(cc[:, rr][:, :, cr])
    flat = window.reshape(nf, -1).argmax(1)
    r0 = np.where(rr[flat // len(cr)] > nr // 2, rr[flat // len(cr)] - nr, rr[flat // len(cr)])
    c0 = np.where(cr[flat % len(cr)] > nc // 2, cr[flat % len(cr)] - nc, cr[flat % len(cr)])
    n_out = int(np.ceil(us * 1.5))
    centre = n_out // 2

    def refine(i):
        up = np.abs(_dftups(np.conj(X[i]), n_out, us, centre - r0[i] * us, centre - c0[i] * us))
        k = up.argmax()
        return r0[i] + (k // n_out - centre) / us, c0[i] + (k % n_out - centre) / us

    with ThreadPoolExecutor(4) as ex:
        shifts = np.array(list(ex.map(refine, range(nf))))
    F *= np.exp(-2j * np.pi * shifts[:, 0, None, None] * np.fft.fftfreq(nr)[None, :, None]).astype(np.complex64)
    F *= np.exp(-2j * np.pi * shifts[:, 1, None, None] * np.fft.fftfreq(nc)[None, None, :]).astype(np.complex64)
    corrected = sfft.ifft2(F, axes=(1, 2), workers=workers).real
    return shifts, corrected


def _median_frames(frames: np.ndarray, parts: int = 4) -> np.ndarray:
    """Median over frames, computed on row bands in parallel threads."""
    bands = np.array_split(np.arange(frames.shape[1]), parts)
    with ThreadPoolExecutor(parts) as ex:
        out = list(ex.map(lambda b: np.median(frames[:, b[0]:b[-1] + 1], 0), bands))
    return np.concatenate(out, 0)


class MovieReader:
    """Blocks of the imaging movie, read by HTTP range requests and decompressed in memory."""

    def __init__(self, url: str, f: h5py.File):
        ds = f[MOVIE]
        self.url, self.shape, self.chunks = url, ds.shape, ds.chunks
        t0 = time.time()
        self.index = _chunk_index(ds)
        self.index_seconds = time.time() - t0
        self.blocks = sorted({o[0] for o, _, _ in self.index})

    def block(self, start: int) -> np.ndarray:
        cs = [c for c in self.index if c[0][0] == start]
        lo = min(b for _, b, _ in cs)
        hi = max(b + s for _, b, s in cs)
        buf = _get_range(self.url, lo, hi)
        n = min(self.chunks[0], self.shape[0] - start)
        out = np.empty((n, *self.shape[1:]), np.uint16)
        c0, c1, c2 = self.chunks

        def put(c):
            (o0, o1, o2), b, s = c
            a = np.frombuffer(zlib.decompress(buf[b - lo:b - lo + s]), dtype="<u2").reshape(c0, c1, c2)
            out[:, o1:o1 + c1, o2:o2 + c2] = a[:n, :min(c1, self.shape[1] - o1), :min(c2, self.shape[2] - o2)]

        with ThreadPoolExecutor(4) as ex:
            list(ex.map(put, cs))
        return out


def normcorre_rigid(reader: MovieReader, init_batch: int = 100, bin_width: int = 200,
                    buffer_width: int = 50, batch: int = 50, blocks=None, prefilter=None, log=print,
                    block_stats=None) -> dict:
    """Rigid shifts of every frame of the movie (or of the frames of `blocks`, a list of block
    starts), with NoRMCorre's template scheme (see the module docstring). Blocks are fetched one
    ahead of the registration. `prefilter`, a function of a stack of frames, is applied before
    registration (a variant; NoRMCorre's default applies none). `block_stats`, a function of a
    block of raw frames, is applied to each block as it is read; its results are returned under
    "stats", in block order."""
    starts = reader.blocks if blocks is None else list(blocks)
    frames_of = {s: min(reader.chunks[0], reader.shape[0] - s) for s in starts}
    frame_ids = np.concatenate([np.arange(s, s + frames_of[s]) for s in starts])
    T = len(frame_ids)
    prep = (lambda a: a.astype(np.float32)) if prefilter is None else (lambda a: prefilter(a.astype(np.float32)))
    mid = frame_ids[np.arange(int(np.ceil(T / 2 - init_batch / 2)), int(np.floor(T / 2 + init_batch / 2)))]
    first_block = max(s for s in starts if s <= mid[0])
    blk = reader.block(first_block)
    if mid[-1] >= first_block + len(blk):
        blk = np.concatenate([blk, reader.block(first_block + len(blk))])
    init = prep(blk[mid - first_block])
    del blk
    template = _median_frames(init)
    _, corrected = register_frames(init, sfft.fft2(template))
    template = _median_frames(corrected)
    template_ft = sfft.fft2(template)
    shifts = np.zeros((T, 2))
    memory, buffer, buffered, done, t0, stats = [], [], 0, 0, time.time(), []
    with ThreadPoolExecutor(1) as ex:
        pending = ex.submit(reader.block, starts[0])
        for k, start in enumerate(starts):
            frames = pending.result()
            if k + 1 < len(starts):
                pending = ex.submit(reader.block, starts[k + 1])
            if block_stats is not None:
                stats.append(block_stats(frames))
            pos = 0
            while pos < len(frames):
                n = min(batch, len(frames) - pos, bin_width - buffered)
                sh, corr = register_frames(prep(frames[pos:pos + n]), template_ft)
                shifts[done:done + n] = sh
                buffer.append(corr)
                buffered += n
                pos += n
                done += n
                if buffered == bin_width or done == T:
                    memory.append(_median_frames(np.concatenate(buffer)))
                    memory = memory[-buffer_width:]
                    template_ft = sfft.fft2(np.mean(memory, 0))
                    buffer, buffered = [], 0
            if log and k % 5 == 0:
                log(f"  block {k + 1} of {len(starts)} registered, {time.time() - t0:.0f} s")
    return {"shifts": shifts, "frames": frame_ids, "template": np.mean(memory, 0), "seconds": time.time() - t0,
            "stats": stats}


def fourier_shift_frames(frames: np.ndarray, shifts: np.ndarray, batch: int = 100) -> np.ndarray:
    """Frames moved by sub-pixel `shifts` (row, column; content moves by +shift) with Fourier
    shifts, rounded and clipped back to 16-bit counts: what a sub-pixel motion correction written
    back as integers does to the values. For checks of the registration and of the movie."""
    nr, nc = frames.shape[1:]
    fr = np.fft.fftfreq(nr)[None, :, None]
    fc = np.fft.fftfreq(nc)[None, None, :]
    out = np.empty(frames.shape, np.uint16)
    for i in range(0, len(frames), batch):
        s = shifts[i:i + batch]
        F = sfft.fft2(frames[i:i + batch].astype(np.float32), axes=(1, 2), workers=-1)
        F *= np.exp(-2j * np.pi * (s[:, 0, None, None] * fr + s[:, 1, None, None] * fc)).astype(np.complex64)
        out[i:i + batch] = np.clip(np.round(sfft.ifft2(F, axes=(1, 2), workers=-1).real), 0, 65535)
    return out


def histogram_roughness(counts: np.ndarray, min_count: int = 1000) -> float:
    """Mean relative difference between the count of each value and the mean count of its two
    neighbours, over values whose neighbours' mean count is at least `min_count`. The histogram of
    raw sensor counts carries the converter's unequal code widths; resampling the frames (a
    sub-pixel shift) mixes neighbouring pixels and smooths it. A check chosen here."""
    h = np.asarray(counts, dtype=float)
    m = (h[:-2] + h[2:]) / 2
    ok = m >= min_count
    return float(np.mean(np.abs(h[1:-1][ok] - m[ok]) / m[ok]))


def highpass(frames: np.ndarray, sigma: float = 10) -> np.ndarray:
    """Each frame minus its Gaussian blur of `sigma` pixels (a variant's prefilter, chosen here)."""
    return frames - ndimage.gaussian_filter(frames, sigma=(0, sigma, sigma))


# --- optical measurements in the paper's code repository ----------------------------------------

def code_file_url(path: str) -> str:
    return f"{CODE_REPO}/{CODE_COMMIT}/{path}"


def read_png(url: str) -> np.ndarray:
    """Pixel values of a PNG measurement image as an array (rows, columns[, channels])."""
    width, height, rows, info = png.Reader(bytes=requests.get(url, timeout=120).content).read()
    a = np.vstack([np.asarray(r) for r in rows])
    planes = info["planes"]
    return a.reshape(height, width, planes) if planes > 1 else a.reshape(height, width)


def list_code_dir(path: str) -> list[str]:
    """File names in a directory of the code repository at the pinned commit (GitHub API)."""
    r = requests.get(f"https://api.github.com/repos/FeeLab/Feescope-Paper-Code/contents/{path}",
                     params={"ref": CODE_COMMIT}, timeout=60)
    r.raise_for_status()
    return [item["name"] for item in r.json()]


def unpack_rgb565(rgb: np.ndarray) -> np.ndarray:
    """imImport.m: uint16(green) * 8 + uint16(blue) / 8, MATLAB rounding."""
    return rgb[..., 1].astype(np.float64) * 8 + np.round(rgb[..., 2].astype(np.float64) / 8)


def weighted_centre(image: np.ndarray) -> tuple[float, float]:
    """Intensity-weighted mean (column, row) of an image, counted from 1 as in MATLAB."""
    h, w = image.shape
    cols, rows = np.meshgrid(np.arange(1, w + 1), np.arange(1, h + 1))
    total = image.sum()
    return (cols * image).sum() / total, (rows * image).sum() / total


def radial_profile(image: np.ndarray, um_per_pixel: float, r_length: int, median_um: int,
                   centre: tuple[float, float] | None = None) -> np.ndarray:
    """analysis.m: mean intensity in 1 um rings (0 to r_length - 1) about the intensity-weighted
    centre, smoothed by a moving median of `median_um` bins and normalized to its 99th percentile.
    `centre` (column, row, from 1) replaces the weighted centre, for a check of sensitivity."""
    h, w = image.shape
    cols, rows = np.meshgrid(np.arange(1, w + 1), np.arange(1, h + 1))
    xc, yc = weighted_centre(image) if centre is None else centre
    r = np.round(np.hypot(um_per_pixel * (cols - xc), um_per_pixel * (rows - yc))).astype(int).ravel()
    inside = r < r_length
    sums = np.bincount(r[inside], weights=image.ravel()[inside], minlength=r_length)
    counts = np.bincount(r[inside], minlength=r_length)
    with np.errstate(invalid="ignore", divide="ignore"):
        avg = sums / counts
    if np.isnan(avg[0]):
        avg[0] = avg[1]
    smoothed = _movmedian(avg, median_um)
    return smoothed / np.nanpercentile(smoothed, 99, method="hazen")


def _movmedian(v: np.ndarray, k: int) -> np.ndarray:
    """MATLAB smoothdata(v, 'movmedian', k): k // 2 before, the rest after, shrunk at the ends,
    NaN omitted."""
    before = k // 2
    after = k - 1 - before
    out = np.empty_like(v)
    for i in range(len(v)):
        window = v[max(0, i - before):i + after + 1]
        window = window[np.isfinite(window)]
        out[i] = np.median(window) if len(window) else np.nan
    return out


def _psf_model(x, gx, gy, dp):
    """The code's rotated Gaussian with second-order pixel correction (fun in *_secondorder.m)."""
    th, x0, sx, y0, sy = x[1], x[2], x[3], x[4], x[5]
    a = np.cos(th) ** 2 / (2 * sx ** 2) + np.sin(th) ** 2 / (2 * sy ** 2)
    b = -np.sin(2 * th) / (4 * sx ** 2) + np.sin(2 * th) / (4 * sy ** 2)
    c = np.sin(th) ** 2 / (2 * sx ** 2) + np.cos(th) ** 2 / (2 * sy ** 2)
    dx, dy = gx - x0, gy - y0
    g = np.exp(-(a * dx ** 2 + 2 * b * dx * dy + c * dy ** 2))
    fx2 = 2 * g * (2 * a ** 2 * dx ** 2 + a * (-1 + 4 * b * dx * dy) + 2 * b ** 2 * dx ** 2)
    fy2 = 2 * g * (2 * c ** 2 * dy ** 2 + c * (-1 + 4 * b * dy * dx) + 2 * b ** 2 * dy ** 2)
    return x[0] + x[6] * (g + fx2 * dp ** 2 / 24 + fy2 * dp ** 2 / 24)


def fit_bead(roi: np.ndarray, dp: float, start_at_max: bool, ftol: float, max_nfev: int,
             x_scale="code") -> dict:
    """Fit of one bead region as in *_secondorder.m: x0 = [median, 0, x, 2, y, 2, max] with x, y
    at 0 (Featherscope script) or at the brightest pixel (Kiloscope script); bounds as the code's.
    x_scale "code" is scipy's default scaling (1), the closest to lsqcurvefit; "jac" scales by the
    Jacobian (a variant). Returns the two FWHM (minor, major), the fit and its status."""
    h, w = roi.shape
    hh, hw = (h - 1) / 2, (w - 1) / 2
    gx = np.tile(dp * np.arange(-hw, hw + 1), (h, 1)).ravel(order="F")
    gy = np.tile(dp * np.arange(-hh, hh + 1)[:, None], (1, w)).ravel(order="F")
    v = roi.astype(np.float64).ravel(order="F")
    k = int(np.argmax(v))
    x0 = np.array([np.median(v), 0, gx[k] if start_at_max else 0, 2, gy[k] if start_at_max else 0, 2, v.max()])
    lb = np.array([0, -np.inf, -hw * dp, 0, -hh * dp, 0, 0])
    ub = np.array([np.inf, np.inf, hw * dp, np.inf, hh * dp, np.inf, np.inf])
    x0 = np.clip(x0, lb + 1e-9, ub - 1e-9)
    res = least_squares(lambda x: _psf_model(x, gx, gy, dp) - v, x0, bounds=(lb, ub), method="trf",
                        max_nfev=max_nfev, ftol=ftol, xtol=1e-6, x_scale=1.0 if x_scale == "code" else x_scale)
    fw = 2.355 * np.sort([res.x[3], res.x[5]])
    return {"fwhm_minor": fw[0], "fwhm_major": fw[1], "cost": res.cost, "status": res.status,
            "nfev": res.nfev}
