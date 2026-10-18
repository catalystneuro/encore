"""Loading and measures for the freely moving mouse session of dandiset 000691.

Scherrer, Lynch, Zhang & Fee (2023), Nature Methods, doi:10.1038/s41592-023-01806-1.

The dandiset holds one NWB file: the raw video of the large-FOV microscope (the Kiloscope), the
traces and centroids of 2948 EXTRACT footprints, and the timestamps of a behaviour video whose AVI
is a second asset. Both are streamed from the archive at the pinned version; the AVI (105 MB) is
read into memory and decoded there. Nothing is written to disk.

Where the parameters come from. The paper's analysis code is
https://github.com/FeeLab/Feescope-Paper-Code at commit d596646b16a505907203828d8026feb7736ca69c
(`CODE`); the main text and Methods of the version of record were not available, and the bioRxiv
preprint's Methods (10.1101/2021.09.03.458947 v2) describe the same procedures.

- Tracking (f3+sf8/mouse_position_tracking.m): the mouse is the largest blob of pixels whose
  squared RGB distance from (0, 3, 4) is below 1600; the first 64 s of the video at its nominal 30
  frames/s (frame 1920) are skipped "to remove period of experimenter futzing"; positions are
  interpolated to the imaging timestamps; the quadrant is the nearest side of the loop's
  rectangle and the octant splits each side in half; linear position runs around the loop and is
  unwrapped. The code rotates and crops the frame by hand-set values; here the search is limited
  to `ARENA_ROWS` x `ARENA_COLS` of the unrotated frame and the rectangle's sides are the 2nd and
  98th percentiles of the interpolated positions (a choice made here, as the code's values apply
  to its rotated crop).
- Decoding (quadrant_direction_decoding.m, octant_decoding.m, subregion_map_octant.m): speed is
  the absolute change of unwrapped position per imaging frame averaged over 30 frames; frames
  above its median are "running"; direction is the sign of the change averaged over 30 frames;
  activity is the moving maximum of each trace over 30 frames; linear SVMs with a ridge penalty
  (lambda 3.2e-7 for quadrant and direction, 6.75e-8 for octant), one against all; each decoder is
  trained on the first half of the running frames after a random circular shift and tested on the
  second half, with 1% of frames left out at the end of each half. MATLAB's fitcecoc with
  templateLinear is replaced by scikit-learn's SGDClassifier with the hinge loss and the same
  lambda as `alpha` (the same objective); `SGD_EPOCHS` passes is a choice made here.
- Pixel size: 5.94 um per pixel, the value in sf3/widefield/analysis.m for the Kiloscope. The
  NWB file gives none.
- Radial illumination profiles (sf3/*/analysis.m): images packed as RGB565 are unpacked as green
  * 8 + blue / 8; the centre is the intensity-weighted mean pixel; profiles are binned at 1 um,
  smoothed with a moving median and normalized to their 99th percentile.
"""

from __future__ import annotations

import io

import h5py
import numpy as np
import png
import remfile
import requests
from dandi.dandiapi import DandiAPIClient
from scipy import ndimage
from sklearn.linear_model import SGDClassifier

DANDISET_ID = "000691"
DANDISET_VERSION = "0.260827.1358"
NWB_PATH = "sub-4mm-mouse-1/sub-4mm-mouse-1_image+ophys.nwb"
VIDEO_SERIES = "acquisition/Video: home_arena_2021-07-26T13_50_50"

CODE_REPO = "https://raw.githubusercontent.com/FeeLab/Feescope-Paper-Code"
CODE_COMMIT = "d596646b16a505907203828d8026feb7736ca69c"

UM_PER_PIXEL = 5.94          # sf3/widefield/analysis.m (Kiloscope)
FIRST_VIDEO_FRAME = 1920     # mouse_position_tracking.m: CurrentTime = 64 s at the AVI's nominal 30 frames/s
DARK_RGB = np.array([0, 3, 4])
DARK_LIMIT = 1600            # squared RGB distance, mouse_position_tracking.m
ARENA_ROWS = (95, 350)       # the maze in the unrotated 480 x 640 frame (a choice made here)
ARENA_COLS = (110, 420)
SMOOTH = 30                  # imaging frames, for speed, direction and the moving maximum
RUN_PERCENTILE = 50
LAMBDA_QUAD_DIR = 3.2e-7
LAMBDA_OCTANT = 6.75e-8
HOLDOUT = 0.5
BUFFER = 0.01
SGD_EPOCHS = 10


def asset_urls() -> dict[str, str]:
    """Path to streaming URL of every asset at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
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
    video = f[VIDEO_SERIES]
    meta = {
        "session_description": _text(f["session_description"][()]),
        "device_description": _text(f["general/devices/Microscope/description"][()]),
        "imaging_series": "TwoPhotonSeries",
        "imaging_description": _text(f["acquisition/TwoPhotonSeries"].attrs["description"]),
        "video_description": _text(video.attrs["description"]),
        "video_external_file": _text(video["external_file"][0]),
        "indicator": _text(f["general/optophysiology/ImagingPlane/indicator"][()]),
        "location": _text(f["general/optophysiology/ImagingPlane/location"][()]),
        "excitation_lambda": float(f["general/optophysiology/ImagingPlane/excitation_lambda"][()]),
        "grid_spacing_present": "grid_spacing" in f["general/optophysiology/ImagingPlane"],
        "virus": _text(f["general/virus"][()]),
        "surgery": _text(f["general/surgery"][()]).strip(),
        "subject": {k: _text(f["general/subject"][k][()]) for k in f["general/subject"].keys()},
        "trace_description": _text(f[rrs].attrs["description"]),
        "trace_unit": _text(f[rrs + "/data"].attrs["unit"]),
        "segmentation_type": _text(f["processing/ophys/ImageSegmentation"].attrs["neurodata_type"]),
        "cellfind_min_snr": float(f["processing/ophys/ImageSegmentation"].attrs["cellfind_min_snr"]),
        "plane_segmentation_columns": [_text(c) for c in f[ps].attrs["colnames"]],
        "movie_shape": f["acquisition/TwoPhotonSeries/data"].shape,
        "movie_dtype": str(f["acquisition/TwoPhotonSeries/data"].dtype),
        "movie_chunks": f["acquisition/TwoPhotonSeries/data"].chunks,
    }
    t_img = f["acquisition/TwoPhotonSeries/timestamps"][:]
    return {
        "meta": meta,
        "t_img": t_img,
        "t_trace": f[rrs + "/timestamps"][:],
        "traces": f[rrs + "/data"][:].astype(np.float32),
        "rois": f[rrs + "/rois"][:],
        "ids": f[ps + "/id"][:],
        "centroids": f[ps + "/ROICentroids"][:],
        "t_video": video["timestamps"][:],
    }


def track_mouse(url: str) -> dict:
    """Per video frame: centroid (x = column, y = row, pixels) and area of the largest dark blob
    in the maze, the number of frames, the frame size and the nominal frame rate."""
    import av

    container = av.open(io.BytesIO(requests.get(url, timeout=600).content))
    stream = container.streams.video[0]
    nominal_rate = float(stream.average_rate)
    r0, r1 = ARENA_ROWS
    c0, c1 = ARENA_COLS
    xs, ys, areas, shape = [], [], [], None
    for frame in container.decode(video=0):
        rgb = frame.to_ndarray(format="rgb24")
        shape = rgb.shape
        crop = rgb[r0:r1, c0:c1].astype(np.int32)
        dark = ((crop - DARK_RGB) ** 2).sum(-1) < DARK_LIMIT
        labels, n = ndimage.label(dark)
        if n == 0:
            xs.append(np.nan), ys.append(np.nan), areas.append(0)
            continue
        sizes = np.bincount(labels.ravel())[1:]
        k = int(sizes.argmax()) + 1
        cy, cx = ndimage.center_of_mass(dark, labels, k)
        xs.append(cx + c0), ys.append(cy + r0), areas.append(int(sizes.max()))
    container.close()
    return {"x": np.array(xs), "y": np.array(ys), "area": np.array(areas),
            "frame_shape": shape, "nominal_rate": nominal_rate}


def behaviour(t_img: np.ndarray, t_video: np.ndarray, track: dict) -> dict:
    """Position and derived labels at the imaging frames that overlap the tracked video."""
    keep = (np.arange(len(t_video)) >= FIRST_VIDEO_FRAME) & np.isfinite(track["x"])
    tv = t_video[keep]
    sel = np.flatnonzero((t_img > tv[0]) & (t_img < tv[-1]))
    x = np.interp(t_img[sel], tv, track["x"][keep])
    y = np.interp(t_img[sel], tv, track["y"][keep])
    xmin, xmax = np.percentile(x, [2, 98])
    ymin, ymax = np.percentile(y, [2, 98])
    xl, yl = xmax - xmin, ymax - ymin
    quadrant = np.stack([abs(x - xmin), abs(y - ymin), abs(x - xmax), abs(y - ymax)], 1).argmin(1)
    s = np.select([quadrant == 0, quadrant == 1, quadrant == 2, quadrant == 3],
                  [ymax - y, yl + x - xmin, yl + xl + y - ymin, 2 * yl + xl + xmax - x])
    xmid, ymid = (xmin + xmax) / 2, (ymin + ymax) / 2
    octant = np.select([quadrant == 0, quadrant == 1, quadrant == 2, quadrant == 3],
                       [0 + (y < ymid), 2 + (x > xmid), 4 + (y > ymid), 6 + (x < xmid)]).astype(int)
    perimeter = 2 * (xl + yl)
    sunwrap = np.unwrap(s * 2 * np.pi / perimeter) * perimeter / (2 * np.pi)
    step = np.diff(sunwrap, append=sunwrap[-1])
    step[-1] = step[-2]
    speed = ndimage.uniform_filter1d(np.abs(step), SMOOTH)
    direction = np.where(ndimage.uniform_filter1d(step, SMOOTH) > 0, 1, -1)
    return {"sel": sel, "t": t_img[sel], "x": x, "y": y, "rect": (xmin, xmax, ymin, ymax),
            "quadrant": quadrant, "octant": octant, "s": s, "sunwrap": sunwrap,
            "perimeter": perimeter, "speed": speed, "direction": direction,
            "running": speed > np.percentile(speed, RUN_PERCENTILE)}


def quad_dir_labels(b: dict) -> np.ndarray:
    """Quadrant and direction as eight classes: 2 * quadrant + (direction > 0)."""
    return 2 * b["quadrant"] + (b["direction"] > 0)


def moving_max(traces: np.ndarray) -> np.ndarray:
    return ndimage.maximum_filter1d(traces, SMOOTH, axis=0)


def decode_once(X: np.ndarray, labels: np.ndarray, n_class: int, lam: float, rng: np.random.Generator,
                null: bool = False) -> np.ndarray:
    """Per-class accuracy of one decoder (NaN for a class absent from the test half). For a null
    decoder the labels are first shifted against the activity by 10% to 90% of the frames."""
    n = len(labels)
    if null:
        labels = np.roll(labels, int(rng.integers(n // 10, n - n // 10)))
    shift = int(rng.integers(n))
    Xs, ls = np.roll(X, shift, axis=0), np.roll(labels, shift)
    half, buffer = round(n * HOLDOUT), round(n * BUFFER)
    model = SGDClassifier(loss="hinge", penalty="l2", alpha=lam, max_iter=SGD_EPOCHS, tol=None,
                          random_state=int(rng.integers(2**31)))
    model.fit(Xs[:half - buffer], ls[:half - buffer])
    test = ls[half:n - buffer]
    predicted = model.predict(Xs[half:n - buffer])
    return np.array([(predicted[test == c] == c).mean() if (test == c).any() else np.nan
                     for c in range(n_class)])


def decode_many(X, labels, n_class, lam, n, rng, null=False) -> np.ndarray:
    """(n, n_class) per-class accuracies of n decoders."""
    return np.array([decode_once(X, labels, n_class, lam, rng, null) for _ in range(n)])


# --- illumination profiles (Extended Data Fig. 2), images from the paper's code repository -----

def code_file_url(path: str) -> str:
    return f"{CODE_REPO}/{CODE_COMMIT}/{path}"


def read_png(url: str) -> np.ndarray:
    """Pixel values of a PNG measurement image as an array (rows, columns[, channels])."""
    width, height, rows, info = png.Reader(bytes=requests.get(url, timeout=120).content).read()
    a = np.vstack([np.asarray(r) for r in rows])
    planes = info["planes"]
    return a.reshape(height, width, planes) if planes > 1 else a.reshape(height, width)


def unpack_rgb565(rgb: np.ndarray) -> np.ndarray:
    """imImport.m: uint16(green) * 8 + uint16(blue) / 8, MATLAB rounding."""
    return rgb[..., 1].astype(np.float64) * 8 + np.round(rgb[..., 2].astype(np.float64) / 8)


def radial_profile(image: np.ndarray, um_per_pixel: float, max_um: int, median_um: int) -> np.ndarray:
    """analysis.m: mean intensity in 1 um rings about the intensity-weighted centre, smoothed by a
    moving median of `median_um` bins and normalized to its 99th percentile."""
    h, w = image.shape
    cols, rows = np.meshgrid(np.arange(1, w + 1), np.arange(1, h + 1))
    total = image.sum()
    xc, yc = (cols * image).sum() / total, (rows * image).sum() / total
    r = np.round(np.hypot(um_per_pixel * (cols - xc), um_per_pixel * (rows - yc))).astype(int).ravel()
    inside = r < max_um
    sums = np.bincount(r[inside], weights=image.ravel()[inside], minlength=max_um)
    counts = np.bincount(r[inside], minlength=max_um)
    with np.errstate(invalid="ignore", divide="ignore"):
        avg = sums / counts
    if np.isnan(avg[0]):
        avg[0] = avg[1]
    smoothed = _movmedian(avg, median_um)
    return smoothed / np.nanpercentile(smoothed, 99)


def _movmedian(v: np.ndarray, k: int) -> np.ndarray:
    """MATLAB smoothdata(v, 'movmedian', k): centred window, shrunk at the ends, NaN omitted."""
    before, after = (k - 1) // 2 if k % 2 else k // 2, (k - 1) // 2
    out = np.empty_like(v)
    for i in range(len(v)):
        window = v[max(0, i - before):i + after + 1]
        window = window[np.isfinite(window)]
        out[i] = np.median(window) if len(window) else np.nan
    return out
