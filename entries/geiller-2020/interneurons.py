"""Data access and analysis helpers for dandiset 000625 (Geiller, Vancura et al. 2020).

The dandiset holds three random-foraging sessions of one VGAT-Cre mouse (tg19),
with dF/F traces of 231 hand-drawn ROIs, the molecular subtype assigned to each
ROI after post hoc immunohistochemistry, the position on a treadmill belt, and
reward and water intervals. `load_session` streams one file from the DANDI
Archive and returns it reduced to what the analyses use.

The files state an imaging rate of 5.7981 Hz for all three sessions, but in two
of them that rate puts the end of imaging two minutes before the end of the
behaviour. `fit_frame_rate` estimates each session's rate from the data (see
its docstring); the notebook shows why.

Parameters and where they come from (paper = STAR Methods of Geiller et al.
2020, full text):

- MAX_LAG = 5 s, the lag window for the velocity correlation: paper.
- RUN_STOP_SPEED = 0.2 cm/s, the threshold for run-start and run-stop events:
  paper. EVENT_SEPARATION = 5 s, the minimum time between events: the paper
  says "several seconds"; 5 s is our choice. EVENT_WINDOW = 3 s: paper.
- N_BINS = 100 position bins, RUN_SPEED = 5 cm/s, TUNING_SIGMA = 3 bins,
  N_SHUFFLES = 1000, FIELD_BINS = 10 consecutive bins, the 95th and 5th
  percentiles and PEAK_DFF = 1.0 (100% dF/F) for positive fields: paper.
  The dF/F values in the files are fractions (median about 0.12), so 100% is 1.0.
  Whether a field may wrap around the end of the belt is not stated; it may
  here, as the belt is a loop.
- VELOCITY_SIGMA = 0.5 s, the smoothing of the velocity trace: the paper says
  "smoothed" without a width; 0.5 s is our choice.
- Laps begin where the position wraps from the end of the belt to its start,
  as in the paper's code (functions.py, `data_preprocessing_laps_merging_classes`).
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
from scipy.ndimage import gaussian_filter1d

DANDISET = "000625"
VERSION = "0.231114.0019"

MAX_LAG = 5.0            # s
RUN_STOP_SPEED = 0.002   # m/s (0.2 cm/s)
EVENT_SEPARATION = 5.0   # s
EVENT_WINDOW = 3.0       # s
N_BINS = 100
RUN_SPEED = 0.05         # m/s (5 cm/s)
TUNING_SIGMA = 3         # bins
N_SHUFFLES = 1000
FIELD_BINS = 10
PEAK_DFF = 1.0           # dF/F as a fraction; 1.0 is 100%
VELOCITY_SIGMA = 0.5     # s

# The paper's six subtypes and the labels the dandiset uses for them.
SUBTYPES = {"PVBC": "PVBC", "AAC": "AAC", "BISTR": "BiC", "SOM": "SomC", "CCK": "CCKC",
            "NGFF": "IvC/NGFC", "AAC (RIGHT CELL)": "AAC"}
ORDER = ["PVBC", "SomC", "BiC", "AAC", "CCKC", "IvC/NGFC"]


@dataclass
class Session:
    path: str
    session_id: str
    start_time: str
    description: str
    stated_rate: float
    dff: np.ndarray            # frames x ROIs, float32, NaN for ROIs not imaged
    roi_ids: np.ndarray
    subtype: np.ndarray        # paper's subtype name per ROI, "" when not one of the six
    label: np.ndarray          # the label as stored in the file
    pos: np.ndarray            # m, as stored
    pos_t: np.ndarray          # s
    reward: np.ndarray         # (n, 2) start and stop times, s
    water: np.ndarray          # (n, 2)
    mask_area: np.ndarray      # pixels in each ROI's mask
    meta: dict = field(default_factory=dict)


def assets(version: str = VERSION) -> list[tuple[str, str]]:
    """(path, asset id) of every asset in a version of the dandiset."""
    from dandi.dandiapi import DandiAPIClient
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET, version)
        return sorted((a.path, a.identifier) for a in ds.get_assets())


def _intervals(group) -> np.ndarray:
    data, ts = group["data"][()], group["timestamps"][()]
    starts, stops = ts[data == 1], ts[data == -1]
    n = min(len(starts), len(stops))
    return np.column_stack([starts[:n], stops[:n]])


def _text(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def _tree(group, prefix: str = "") -> list[str]:
    """Every dataset under an HDF5 group, as 'path shape'."""
    import h5py
    out = []
    for k in group:
        if isinstance(group[k], h5py.Group):
            out += _tree(group[k], f"{prefix}{k}/")
        else:
            out.append(f"{prefix}{k} {group[k].shape}")
    return out


def load_session(path: str, version: str = VERSION) -> Session:
    """Stream one session. Only the traces, labels and behaviour are read, not the raw images."""
    import h5py
    import remfile
    from dandi.dandiapi import DandiAPIClient

    with DandiAPIClient() as client:
        asset = client.get_dandiset(DANDISET, version).get_asset_by_path(path)
        url = asset.get_content_url(follow_redirects=1, strip_query=True)
    f = h5py.File(remfile.File(url), "r")
    oph = f["processing/ophys"]
    dff_ds = oph["DfOverF/RoiResponseSeries"]
    roi_ids = oph["ImageSegmentation/CA1 plane segmentation/id"][()]
    table_ids = oph["Cell_Subtypes/id"][()]
    labels = np.array([_text(s) for s in oph["Cell_Subtypes/subtype"][()]])
    by_id = dict(zip(table_ids, labels))
    label = np.array([by_id.get(i, "") for i in roi_ids])
    seg = oph["ImageSegmentation/CA1 plane segmentation"]
    weights = seg["pixel_mask"]["weight"]
    ends = seg["pixel_mask_index"][()]
    mask_area = np.array([(weights[a:b] > 0).sum() for a, b in zip(np.r_[0, ends[:-1]], ends)])
    plane = f["general/optophysiology/CA1"]
    meta = {
        "dff unit": _text(dff_ds["data"].attrs["unit"]),
        "DfOverF and Fluorescence are one HDF5 object":
            dff_ds.id == oph["Fluorescence/RoiResponseSeries"].id,
        "subtype rows": len(table_ids),
        "ROIs": len(roi_ids),
        "subtype ids without a ROI": sorted(set(table_ids) - set(roi_ids)),
        "subtype column description": _text(oph["Cell_Subtypes/subtype"].attrs["description"]),
        "position unit": _text(f["acquisition/Position/SpatialSeries/data"].attrs["unit"]),
        "position reference frame": _text(f["acquisition/Position/SpatialSeries/reference_frame"][()]),
        "imaging rate (plane)": float(plane["imaging_rate"][()]),
        "indicator": _text(plane["indicator"][()]),
        "excitation (nm)": float(plane["excitation_lambda"][()]),
        "emission (nm)": float(plane["Green/emission_lambda"][()]),
        "raw image series": {k: f["acquisition"][k]["data"].shape
                             for k in f["acquisition"] if "TwoPhoton" in k},
        "subject": {k: _text(f["general/subject"][k][()]) for k in f["general/subject"]},
        "experiment description": " ".join(_text(f["general/experiment_description"][()]).split()),
    }
    meta.update({
        "PlaneSegmentation columns": sorted(k for k in seg if isinstance(seg[k], h5py.Dataset)),
        "pixel_mask fields": list(seg["pixel_mask"].dtype.names),
        "pixel_mask x range": (int(seg["pixel_mask"]["x"].min()), int(seg["pixel_mask"]["x"].max())),
        "pixel_mask y range": (int(seg["pixel_mask"]["y"].min()), int(seg["pixel_mask"]["y"].max())),
        "reference images": list(seg["reference_images"]),
        "imaging plane fields": sorted(plane),
        "imaging plane location": _text(plane["location"][()]),
        "imaging plane origin_coords (um)": plane["origin_coords"][()].tolist(),
        "imaging plane grid_spacing (um)": plane["grid_spacing"][()].tolist(),
        "acquisition": _tree(f["acquisition"]),
        "processing/behavior": _tree(f["processing/behavior"]),
        "raw image series starting_time (s)": {k: float(f["acquisition"][k]["starting_time"][()])
                                               for k in f["acquisition"] if "TwoPhoton" in k},
        "file_create_date": [_text(x) for x in f["file_create_date"][()]],
        "timestamps_reference_time": _text(f["timestamps_reference_time"][()]),
    })
    return Session(
        path=path,
        session_id=_text(f["general/session_id"][()]),
        start_time=_text(f["session_start_time"][()]),
        description=_text(f["session_description"][()]),
        stated_rate=float(dff_ds["starting_time"].attrs["rate"]),
        dff=dff_ds["data"][()].astype(np.float32),
        roi_ids=roi_ids,
        subtype=np.array([SUBTYPES.get(x, "") for x in label]),
        label=label,
        pos=f["acquisition/Position/SpatialSeries/data"][()],
        pos_t=f["acquisition/Position/SpatialSeries/timestamps"][()],
        reward=_intervals(f["processing/behavior/BehavioralEpochs/reward"]),
        water=_intervals(f["processing/behavior/BehavioralEpochs/water"]),
        mask_area=mask_area,
        meta=meta,
    )


# --- behaviour on the imaging clock -------------------------------------------

def belt_length(s: Session) -> float:
    return float(s.pos.max() - s.pos.min())


def behaviour(s: Session, rate: float, sigma: float = VELOCITY_SIGMA) -> dict:
    """Position, speed and laps on the imaging frames, for frame times i / rate.

    Position is stored only when it changes, so the value at a frame is the last
    sample at or before it (not an interpolation across a stationary gap).
    """
    n = s.dff.shape[0]
    t = np.arange(n) / rate
    L = belt_length(s)
    step = np.diff(s.pos)
    step[step < -L / 2] += L
    step[step > L / 2] -= L
    unwrapped = np.concatenate([[0.0], np.cumsum(step)])
    k = np.clip(np.searchsorted(s.pos_t, t, side="right") - 1, 0, len(s.pos) - 1)
    pos = s.pos[k] - s.pos.min()
    dist = unwrapped[k]
    speed = np.gradient(dist, t)
    if sigma > 0:
        speed = gaussian_filter1d(speed, sigma * rate)
    covered = t <= s.pos_t[-1]
    lap = np.concatenate([[0], np.cumsum(np.diff(pos) < -L / 2)])
    return dict(t=t, pos=pos, speed=speed, lap=lap, covered=covered, length=L)


def fit_frame_rate(s: Session, rates=np.arange(3.5, 6.5, 0.005)) -> tuple[float, np.ndarray]:
    """The frame rate at which the mean z-scored dF/F best follows running speed.

    For each candidate rate the frames are placed at i / rate, and the score is
    the largest correlation between the population mean and speed over lags
    within MAX_LAG. Returns the best rate and the score for every candidate.
    """
    X = s.dff[:, ~np.isnan(s.dff).all(0)]
    X = (X - X.mean(0)) / X.std(0)
    m = X.mean(1)
    scores = []
    for rate in rates:
        b = behaviour(s, rate)
        ok = b["covered"]
        best = -1.0
        for lag in range(-int(MAX_LAG * rate), int(MAX_LAG * rate) + 1):
            a, v = _shift(m, b["speed"], lag)
            okl = _shift(ok, ok, lag)[0] & _shift(ok, ok, lag)[1]
            best = max(best, np.corrcoef(a[okl], v[okl])[0, 1])
        scores.append(best)
    scores = np.array(scores)
    return float(rates[np.argmax(scores)]), scores


def _shift(a, v, lag):
    """Pairs a[i] with v[i + lag]: a positive lag means activity leads velocity."""
    if lag > 0:
        return a[:-lag], v[lag:]
    if lag < 0:
        return a[-lag:], v[:lag]
    return a, v


# --- velocity correlation and run events ---------------------------------------

def velocity_correlation(dff: np.ndarray, speed: np.ndarray, rate: float, ok: np.ndarray):
    """The paper's activity-velocity correlation of every ROI.

    Pearson r between dF/F and speed with the trace shifted one frame at a time
    from -MAX_LAG (activity lagging velocity) to +MAX_LAG (activity leading);
    the r of largest absolute value, and its lag in seconds. ROIs that were not
    imaged give NaN.
    """
    lags = np.arange(-int(MAX_LAG * rate), int(MAX_LAG * rate) + 1)
    R = np.full((len(lags), dff.shape[1]), np.nan)
    for j, lag in enumerate(lags):
        # lag > 0: activity at frame i paired with speed at frame i + lag (activity leads)
        if lag >= 0:
            a, v, k = dff[: len(dff) - lag], speed[lag:], ok[lag:] & ok[: len(ok) - lag]
        else:
            a, v, k = dff[-lag:], speed[:lag], ok[:lag] & ok[-lag:]
        a, v = a[k], v[k]
        az = (a - a.mean(0)) / a.std(0)
        vz = (v - v.mean()) / v.std()
        R[j] = (az * vz[:, None]).mean(0)
    imaged = ~np.isnan(dff).all(0)
    best = np.nanargmax(np.abs(np.where(np.isnan(R), 0, R)), axis=0)
    r = R[best, np.arange(dff.shape[1])]
    lag = lags[best] / rate
    return np.where(imaged, r, np.nan), np.where(imaged, lag, np.nan)


def run_events(speed: np.ndarray, rate: float, ok: np.ndarray, separation: float = EVENT_SEPARATION):
    """Frames where speed rises above (start) or falls below (stop) RUN_STOP_SPEED.

    An event is kept only if it is at least `separation` seconds after the
    previous kept event of either kind, and its window lies inside the session.
    """
    moving = speed > RUN_STOP_SPEED
    change = np.flatnonzero(np.diff(moving.astype(int))) + 1
    w = int(round(EVENT_WINDOW * rate))
    kept, last = {"start": [], "stop": []}, -np.inf
    for i in change:
        if i - last < separation * rate:
            continue
        last = i
        if i - w < 0 or i + w > len(speed) or not ok[i - w:i + w].all():
            continue
        kept["start" if moving[i] else "stop"].append(i)
    return {k: np.array(v, dtype=int) for k, v in kept.items()}


def event_response(dff: np.ndarray, events: np.ndarray, rate: float) -> np.ndarray:
    """Mean dF/F in the EVENT_WINDOW after each event minus the mean before it, averaged over events."""
    w = int(round(EVENT_WINDOW * rate))
    if len(events) == 0:
        return np.full(dff.shape[1], np.nan)
    post = np.stack([dff[i:i + w].mean(0) for i in events])
    pre = np.stack([dff[i - w:i].mean(0) for i in events])
    return (post - pre).mean(0)


# --- spatial tuning ---------------------------------------------------------------

def position_bins(pos: np.ndarray, length: float) -> np.ndarray:
    return np.minimum((pos / length * N_BINS).astype(int), N_BINS - 1)


def tuning_curves(dff: np.ndarray, bins: np.ndarray, smooth: bool = True) -> np.ndarray:
    """Mean dF/F per position bin (ROIs x bins), from the frames given; smoothed circularly."""
    onehot = np.zeros((len(bins), N_BINS))
    onehot[np.arange(len(bins)), bins] = 1.0
    counts = onehot.sum(0)
    with np.errstate(invalid="ignore", divide="ignore"):
        tc = (np.nan_to_num(dff).T @ onehot) / counts
    if smooth:
        tc = _nan_smooth(tc)
    return tc


def _nan_smooth(tc: np.ndarray) -> np.ndarray:
    """Gaussian smoothing over bins (circular) that ignores empty bins."""
    good = ~np.isnan(tc)
    num = gaussian_filter1d(np.where(good, tc, 0.0), TUNING_SIGMA, axis=-1, mode="wrap")
    den = gaussian_filter1d(good.astype(float), TUNING_SIGMA, axis=-1, mode="wrap")
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(den > 1e-6, num / den, np.nan)


def _run_starts(mask: np.ndarray, n: int, wrap: bool) -> np.ndarray:
    """For each row, which bins start n consecutive True values (circularly if wrap)."""
    m = np.concatenate([mask, mask[:, : n - 1]], axis=1) if wrap else mask
    c = np.cumsum(np.pad(m.astype(int), ((0, 0), (1, 0))), axis=1)
    return (c[:, n:] - c[:, :-n]) == n


def shuffle_bounds(dff: np.ndarray, bins: np.ndarray, rng: np.random.Generator,
                   n_shuffles: int = N_SHUFFLES) -> dict:
    """The tuning curves and the 5th and 95th percentiles of their shuffles, on running frames only.

    Each shuffle rotates the position circularly against dF/F by a random number of frames.
    """
    tc = tuning_curves(dff, bins)
    shuf = np.empty((n_shuffles,) + tc.shape, dtype=np.float32)
    for k, sh in enumerate(rng.integers(1, len(bins), n_shuffles)):
        shuf[k] = tuning_curves(dff, np.roll(bins, sh))
    return dict(tc=tc, hi=np.nanpercentile(shuf, 95, axis=0), lo=np.nanpercentile(shuf, 5, axis=0))


def place_fields(b: dict, field_bins: int = FIELD_BINS, peak: float | None = PEAK_DFF,
                 wrap: bool = True) -> dict:
    """The paper's place-field rule applied to the output of `shuffle_bounds`.

    A positive field is `field_bins` consecutive bins above the shuffles' 95th
    percentile, with a peak in the field above `peak` (no peak rule if None). A
    negative field is `field_bins` consecutive bins below the 5th percentile.
    """
    tc = b["tc"]
    starts = _run_starts(tc > b["hi"], field_bins, wrap)
    positive = starts.any(1)
    if peak is not None:
        for i in np.flatnonzero(positive):
            s = np.flatnonzero(starts[i])
            field = np.unique(np.concatenate([(x + np.arange(field_bins)) % N_BINS for x in s]))
            positive[i] = np.nanmax(tc[i, field]) > peak
    negative = _run_starts(tc < b["lo"], field_bins, wrap).any(1)
    return dict(positive=positive, negative=negative)


def sparsity_index(tc: np.ndarray) -> np.ndarray:
    """Selectivity index S = 1 - (sum r)^2 / (N sum r^2) (Acharya et al. 2016), per row."""
    r = np.clip(tc, 0, None)
    return 1 - np.nansum(r, 1) ** 2 / (N_BINS * np.nansum(r ** 2, 1))


def lap_tuning(dff: np.ndarray, bins: np.ndarray, laps: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Smoothed tuning curve of every ROI in every lap: samples (lap, bin) x ROIs, with the bin and lap of each."""
    X, y, g = [], [], []
    for lap in np.unique(laps):
        sel = laps == lap
        tc = tuning_curves(dff[sel], bins[sel])          # ROIs x bins
        visited = np.bincount(bins[sel], minlength=N_BINS) > 0
        X.append(tc[:, visited].T)
        y.append(np.flatnonzero(visited))
        g.append(np.full(visited.sum(), lap))
    return np.vstack(X), np.concatenate(y), np.concatenate(g)


def decode_position(X: np.ndarray, y: np.ndarray, groups: np.ndarray, length: float) -> float:
    """Mean absolute decoding error (cm, around the loop) of a linear SVM, leaving one lap out.

    The paper names a linear support vector machine trained on n-1 laps and
    tested on the held-out lap; the multi-class scheme is not stated. This uses
    scikit-learn's SVC with a linear kernel (one-vs-one) and C = 1, with the
    features standardised on the training laps.
    """
    from sklearn.preprocessing import StandardScaler
    from sklearn.svm import SVC

    errors = []
    for lap in np.unique(groups):
        train, test = groups != lap, groups == lap
        scaler = StandardScaler().fit(X[train])
        clf = SVC(kernel="linear", C=1.0).fit(scaler.transform(X[train]), y[train])
        d = np.abs(clf.predict(scaler.transform(X[test])) - y[test])
        errors.append(np.minimum(d, N_BINS - d))
    return float(np.concatenate(errors).mean() * length / N_BINS * 100)


def odd_even_correlation(dff: np.ndarray, bins: np.ndarray, laps: np.ndarray) -> np.ndarray:
    """Within-session stability: Pearson r between the tuning curves of odd and even laps, per ROI."""
    odd = laps % 2 == 1
    return rowwise_corr(tuning_curves(dff[odd], bins[odd]), tuning_curves(dff[~odd], bins[~odd]))


def rowwise_corr(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    out = np.full(len(a), np.nan)
    for i in range(len(a)):
        ok = ~np.isnan(a[i]) & ~np.isnan(b[i])
        if ok.sum() > 2 and a[i, ok].std() > 0 and b[i, ok].std() > 0:
            out[i] = np.corrcoef(a[i, ok], b[i, ok])[0, 1]
    return out


# --- clock check -------------------------------------------------------------------

def shifted_label_decoding(dff: np.ndarray, running: np.ndarray, ok: np.ndarray, rate: float,
                           shifts_s: np.ndarray, n_folds: int = 5) -> np.ndarray:
    """Balanced accuracy of decoding running from the population, with the labels shifted in time.

    For each shift, frame i of dF/F is paired with the running label of frame
    i + shift. Logistic regression on z-scored dF/F of the imaged ROIs, with
    contiguous folds. If the clocks agree, accuracy peaks near zero shift
    (within the calcium indicator's lag).
    """
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import balanced_accuracy_score

    X = dff[:, ~np.isnan(dff).all(0)]
    X = (X - X.mean(0)) / X.std(0)
    out = []
    for shift in shifts_s:
        k = int(round(shift * rate))
        idx = np.arange(len(X))
        j = idx + k
        keep = (j >= 0) & (j < len(X))
        keep[keep] &= ok[j[keep]]
        xi, yi = X[idx[keep]], running[j[keep]]
        folds = np.array_split(np.arange(len(xi)), n_folds)
        pred = np.empty(len(xi), dtype=bool)
        for f in folds:
            train = np.ones(len(xi), bool)
            train[f] = False
            clf = LogisticRegression(C=0.1, max_iter=500).fit(xi[train], yi[train])
            pred[f] = clf.predict(xi[f])
        out.append(balanced_accuracy_score(yi, pred))
    return np.array(out)
