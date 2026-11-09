"""Data access and analysis helpers for dandiset 001097 (Liu, Nair et al. 2024, Nature).

The dandiset holds miniscope calcium imaging of VMHvl Esr1+ Npy2r- ("alpha") cells in female
mice mating with a male, with frame-by-frame annotations of male (channel Ch1) and female (Ch2)
behaviour. There is one file per recording, named
`sub-<mouse>_ses-<experiment>_ecephys+behavior.nwb`, and two older per-mouse files that also
carry rSLDS weights fitted by the authors. `session_table` lists the files and parses the
experiment from the name; `load_session` streams one file and returns its traces and
annotations.

Where a parameter comes from:

- Imaging at 10 Hz and annotations in seconds at 30 Hz: the files and the paper's Methods.
- Behaviour groups (accepting, resistance, appetitive, responsive, self-initiated, social):
  the paper's Methods, "Behavioural annotations".
- `smooth` (a 10-frame moving average, which becomes 9 frames as in MATLAB's `smooth`) and the
  z-scoring: the authors' code, `processing/data_processing.py` (`config_neural_activity`),
  github.com/neuralcomputation/hypothalamic-dynamics at commit 28fee70.
- `achw` (MATLAB-style autocorrelation; the lag whose value is closest to 0.5; up to 500 lags):
  the authors' code, `analysis/analysis_functions.py` (`sca_matlab`) and
  `processing/data_processing.py` (`autocorr_matlab`). The variant `first_crossing=True` takes
  the first lag at or below 0.5, the Methods' wording.
- Weighted cells, absolute weight above one SD of the weights: the authors' code,
  `plotting/rslds_plots.py` (`filter_weights`).
- Choice probability (1-s bins, ROC area, tuned above 0.7 or below 0.3 and beyond 2 SD of 1000
  shuffles): the paper's Methods. The comparison set (the other bins of the interaction) and
  the half-bin rule are choices here; the Methods do not fix them.
- Ridge GLM (tenfold cross-validation, lags of 0 to 10 s): the paper's Methods. Lags in 1-s
  steps, contiguous folds, the penalty chosen per cell on the last fifth of each training set,
  and R2 of the pooled held-out predictions are choices here.
"""

from __future__ import annotations

import re
import warnings
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy import stats

DANDISET = "001097"
VERSION = "0.260624.0330"
RATE = 10.0                 # Hz, imaging (files and Methods)
MAX_LAG = 500               # frames, for the ACHW (authors' code)

ACCEPT = ["lordose", "wiggle"]
RESIST = ["dart", "top_up", "kick", "turn"]
APPETITIVE = ["approach", "sniff"]
RESPONSIVE = ACCEPT + ["stay"] + RESIST
FEMALE_SELF = ["approach", "sniff", "check_genital"]
MALE_SELF = ["male_sniff", "mount", "intromission"]
SOCIAL = ACCEPT + RESIST + APPETITIVE
COPULATION = ["mount", "intromission"]
FEMALE_MATING = ["approach", "sniff", "lordose", "wiggle", "stay", "dart", "top_up", "kick",
                 "turn", "check_genital"]

NAME = re.compile(r"sub-(?P<subject>[^_/]+)_ses-(?P<session>.+)_ecephys\+behavior\.nwb$")


# --- the file list -------------------------------------------------------------------

def experiment_of(session: str) -> tuple[str, int | None]:
    """The experiment and day encoded in a session name."""
    s = session.lower()
    day = re.search(r"_d(\d)$", s)
    if s.startswith("wt_3d"):
        return "natural cycle (3 days)", int(day.group(1))
    if s.startswith("ovx_3d"):
        return "ovariectomy (3 days)", int(day.group(1))
    if s.startswith("wt_7d"):
        return "oestrogen-injected (7 days)", int(day.group(1))
    if s == "wt_proestrus_receptive_mating":
        return "receptive", None
    if s == "ovx_primed_receptive_mating":
        return "ovariectomised, primed", None
    if s == "wireless_opto":
        return "male inhibition", None
    raise ValueError(f"unknown session name {session}")


def session_table(version: str = VERSION) -> pd.DataFrame:
    """One row per file of the dandiset version, with subject and experiment parsed from the name."""
    from dandi.dandiapi import DandiAPIClient

    rows = []
    with DandiAPIClient() as client:
        for asset in client.get_dandiset(DANDISET, version).get_assets():
            m = NAME.match(asset.path)
            row = dict(path=asset.path, asset_id=asset.identifier, size=asset.size)
            if m:
                experiment, day = experiment_of(m["session"])
                row.update(subject=m["subject"], session=m["session"], experiment=experiment, day=day)
            else:
                row.update(subject=asset.path.split("/")[0].removeprefix("sub-"), session=None,
                           experiment="per-mouse file", day=None)
            rows.append(row)
    return pd.DataFrame(rows).sort_values("path").reset_index(drop=True)


def digest(path: str, version: str) -> str:
    """The SHA-256 digest the archive records for a file."""
    from dandi.dandiapi import DandiAPIClient

    with DandiAPIClient() as client:
        meta = client.get_dandiset(DANDISET, version).get_asset_by_path(path).get_raw_metadata()
    return meta["digest"].get("dandi:sha2-256", "not recorded")


def _url(path: str, version: str) -> str:
    from dandi.dandiapi import DandiAPIClient

    with DandiAPIClient() as client:
        asset = client.get_dandiset(DANDISET, version).get_asset_by_path(path)
        return asset.get_content_url(follow_redirects=1, strip_query=True)


def _open(path: str, version: str):
    import h5py
    import remfile
    from pynwb import NWBHDF5IO

    io = NWBHDF5IO(file=h5py.File(remfile.File(_url(path, version)), "r"), mode="r",
                   load_namespaces=True)
    return io, io.read()


# --- one session ---------------------------------------------------------------------

@dataclass
class Session:
    path: str
    subject: str
    traces: np.ndarray | None   # frames x cells, as stored
    kind: str                   # "Fluorescence" (raw) or "DfOverF" (z-scored), as stored
    unit: str
    description: str
    timestamps: np.ndarray | None
    behaviour: pd.DataFrame     # channel, behavior, start, stop (s)
    n_frames: int
    n_cells: int
    meta: dict                  # descriptive metadata, for checking

    def interaction(self) -> tuple[float, float]:
        """Male entry (into_male_cage) to the end of the annotation, in seconds."""
        b = self.behaviour
        return float(b.loc[b.behavior == "into_male_cage", "start"].min()), float(b.stop.max())

    def receptive(self) -> bool:
        """The paper's definition of a receptive trial: the female shows accepting behaviour."""
        return bool(self.behaviour.behavior.isin(ACCEPT).any())

    def has_female(self) -> bool:
        return bool((self.behaviour.channel == "Ch2").any())


def load_session(path: str, neural: bool = True, version: str = VERSION) -> Session:
    """Stream one recording; with neural=False only the annotations are read."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        io, nwb = _open(path, version)
        ophys = nwb.processing["ophys"]
        kind = "DfOverF" if "DfOverF" in ophys.data_interfaces else "Fluorescence"
        series = ophys[kind]["RoiResponseSeries"]
        n_frames, n_cells = series.data.shape
        traces = series.data[:].astype(float) if neural else None
        timestamps = series.timestamps[:] if neural else None
        tables = []
        for name, table in nwb.intervals.items():
            df = table.to_dataframe()[["channel", "behavior", "start_time", "stop_time"]]
            tables.append(df.rename(columns={"start_time": "start", "stop_time": "stop"}))
        behaviour = pd.concat(tables, ignore_index=True).sort_values(["channel", "start"])
        plane = next(iter(nwb.imaging_planes.values()))
        meta = dict(device=next(iter(nwb.devices.values())).description,
                    excitation_nm=plane.excitation_lambda, indicator=plane.indicator, location=plane.location,
                    experimenter=tuple(nwb.experimenter or ()), lab=nwb.lab, institution=nwb.institution,
                    session_start=str(nwb.session_start_time.date()),
                    image_mask=tuple(ophys["ImageSegmentation"]["PlaneSegmentation"]["image_mask"].data.shape[1:]))
        session = Session(path=path, subject=nwb.subject.subject_id, traces=traces, kind=kind,
                          unit=series.unit, description=series.description, timestamps=timestamps,
                          behaviour=behaviour.reset_index(drop=True), n_frames=n_frames,
                          n_cells=n_cells, meta=meta)
        io.close()
    return session


def load_many(paths: list[str], neural: bool = True, workers: int = 8) -> dict[str, Session]:
    with ThreadPoolExecutor(workers) as pool:
        return dict(zip(paths, pool.map(lambda p: load_session(p, neural), paths)))


def load_weights(subject: str, version: str = VERSION) -> dict:
    """The authors' rSLDS weights per cell from a per-mouse file, with that file's traces."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        io, nwb = _open(f"sub-{subject}/sub-{subject}_behavior.nwb", version)
        weights = nwb.analysis["rSLDS"].to_dataframe()
        trace = nwb.processing["ophys"]["NeuralTrace"]
        out = dict(subject_id=nwb.subject.subject_id, weights=weights.to_numpy(),
                   columns=list(weights.columns), traces=trace.data[:], rate=trace.rate,
                   comments=trace.comments, session_description=nwb.session_description)
        io.close()
    return out


# --- preprocessing -------------------------------------------------------------------

def zscore(x: np.ndarray) -> np.ndarray:
    return stats.zscore(x, axis=0)


def smooth(x: np.ndarray, window: int = 10) -> np.ndarray:
    """Moving average along time, as MATLAB's smooth (the authors' `smooth`), for every column."""
    if window % 2 == 0:
        window -= 1
    half = (window - 1) // 2
    kernel = np.ones(window) / window
    middle = np.apply_along_axis(lambda v: np.convolve(v, kernel, "valid"), 0, x)
    start = np.array([x[: 2 * k + 1].mean(0) for k in range(half)])
    end = np.array([x[-(2 * k + 1):].mean(0) for k in range(half)])[::-1]
    return np.vstack([start, middle, end])


def prepare(traces: np.ndarray, smoothed: bool = True) -> np.ndarray:
    """z-score, optionally smooth (authors' code: 10-frame window), and z-score again."""
    z = zscore(traces)
    return zscore(smooth(z)) if smoothed else z


# --- behaviour -----------------------------------------------------------------------

def intervals(behaviour: pd.DataFrame, labels: list[str], channel: str | None = None) -> np.ndarray:
    b = behaviour[behaviour.behavior.isin(labels)]
    if channel:
        b = b[b.channel == channel]
    return b[["start", "stop"]].to_numpy()


def raster(behaviour: pd.DataFrame, labels: list[str], n_frames: int, channel: str | None = None,
           rate: float = RATE) -> np.ndarray:
    """1 where any of the labels is annotated, at the imaging rate.

    An annotation covers frames from its start up to, not including, its stop; one shorter than a
    frame still marks the frame it starts in.
    """
    r = np.zeros(n_frames, bool)
    for start, stop in intervals(behaviour, labels, channel):
        a = int(round(start * rate))
        r[a: min(max(int(round(stop * rate)), a + 1), n_frames)] = True
    return r


def bouts(iv: np.ndarray, gap: float | None) -> np.ndarray:
    """Merge intervals separated by at most `gap` seconds (None: no merging)."""
    if len(iv) == 0:
        return iv.reshape(0, 2)
    iv = iv[np.argsort(iv[:, 0])]
    if gap is None:
        return iv
    merged = [list(iv[0])]
    for start, stop in iv[1:]:
        if start - merged[-1][1] <= gap:
            merged[-1][1] = max(merged[-1][1], stop)
        else:
            merged.append([start, stop])
    return np.array(merged)


# --- single-cell measures ------------------------------------------------------------

def autocorrelation(y: np.ndarray, max_lag: int = MAX_LAG) -> np.ndarray:
    """MATLAB-style autocorrelation of every column, lags 0..max_lag (authors' autocorr_matlab)."""
    y = y - y.mean(0)
    T = len(y)
    n = 1 << int(np.ceil(np.log2(2 * T)))
    f = np.fft.rfft(y, n, axis=0)
    c = np.fft.irfft(f * np.conj(f), n, axis=0)[: max_lag + 1] / T
    c0 = (y ** 2).sum(0) / (T - 1)
    return c / c0


def achw(y: np.ndarray, rate: float = RATE, max_lag: int = MAX_LAG,
         first_crossing: bool = False) -> np.ndarray:
    """Autocorrelation half-width of every column, in seconds."""
    acf = autocorrelation(y, max_lag)
    acf[0] = 1.0
    if first_crossing:
        below = acf <= 0.5
        lag = np.where(below.any(0), below.argmax(0), max_lag)
    else:
        lag = np.abs(acf - 0.5).argmin(0)
    return lag / rate


def bin_frames(x: np.ndarray, width: int) -> np.ndarray:
    n = len(x) // width
    return x[: n * width].reshape(n, width, *x.shape[1:]).mean(1)


def choice_probability(y: np.ndarray, labels: np.ndarray, rng: np.random.Generator,
                       shuffles: int = 1000) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """ROC area of each column for labelled against other rows, and its shuffle mean and SD."""
    ranks = stats.rankdata(y, axis=0)
    n1, n0 = labels.sum(), (~labels).sum()

    def auc(lab):
        return (lab.astype(float) @ ranks - n1 * (n1 + 1) / 2) / (n1 * n0)

    cp = auc(labels[None, :])[0]
    perms = np.array([rng.permutation(labels) for _ in range(shuffles)])
    null = auc(perms)
    return cp, null.mean(0), null.std(0)


# --- ridge GLM -----------------------------------------------------------------------

def lagged(rasters: np.ndarray, lags: np.ndarray) -> np.ndarray:
    """Columns of each raster delayed by each lag (frames): the value at t - lag."""
    T = len(rasters)
    cols = []
    for k in lags:
        shifted = np.zeros_like(rasters, dtype=float)
        shifted[k:] = rasters[: T - k]
        cols.append(shifted)
    return np.hstack(cols)


def _ridge_weights(G: np.ndarray, H: np.ndarray, alpha: float, exclude: np.ndarray | None):
    """Ridge weights for every target from Gram G = X'X and H = X'Y.

    With `exclude`, target i leaves out column exclude[i] of X (its own activity), using the
    inverse of the reduced matrix obtained from the full inverse.
    """
    M = np.linalg.inv(G + alpha * np.eye(len(G)))
    if exclude is None:
        return M @ H
    W = np.empty_like(H)
    for i, j in enumerate(exclude):
        Mi = M - np.outer(M[:, j], M[j, :]) / M[j, j]
        Mi[j, :] = 0.0
        Mi[:, j] = 0.0
        h = H[:, i].copy()
        h[j] = 0.0
        W[:, i] = Mi @ h
    return W


def cv_ridge(X: np.ndarray, Y: np.ndarray, exclude: np.ndarray | None = None, folds: int = 10,
             alphas=(1e0, 1e1, 1e2, 1e3, 1e4, 1e5), rng: np.random.Generator | None = None,
             return_pred: bool = False, inner_folds: int | None = None):
    """Cross-validated R2 of every column of Y from X.

    Folds are contiguous blocks of time; with `rng`, frames are assigned to folds at random
    instead. The penalty is chosen per target on a fifth of each training set (its last fifth,
    or a random fifth), then the model is refit on the whole training set. With `inner_folds`,
    the penalty is chosen instead by cross-validation over that many contiguous blocks of each
    training set, summing the held-out error over the blocks. R2 is computed on the pooled
    held-out predictions. With `return_pred`, the held-out predictions and the fold of each
    frame are returned too.
    """
    from threadpoolctl import threadpool_limits

    T = len(Y)
    if rng is None:
        fold_of = np.repeat(np.arange(folds), np.diff(np.linspace(0, T, folds + 1).astype(int)))
    else:
        fold_of = rng.permutation(np.arange(T) % folds)
    pred = np.empty_like(Y)
    with threadpool_limits(1):
        for f in range(folds):
            test = fold_of == f
            train = np.where(~test)[0]
            if rng is not None:
                train = rng.permutation(train)

            def fit(rows):
                mx, my = X[rows].mean(0), Y[rows].mean(0)
                Xc, Yc = X[rows] - mx, Y[rows] - my
                return Xc.T @ Xc, Xc.T @ Yc, mx, my

            if inner_folds is None:
                splits = [(train[: int(0.8 * len(train))], train[int(0.8 * len(train)):])]
            else:
                blocks = np.array_split(train, inner_folds)
                splits = [(np.concatenate(blocks[:k] + blocks[k + 1:]), blocks[k]) for k in range(inner_folds)]
            errs = np.zeros((len(alphas), Y.shape[1]))
            for inner, val in splits:
                G, H, mx, my = fit(inner)
                for n, a in enumerate(alphas):
                    W = _ridge_weights(G, H, a, exclude)
                    errs[n] += (((X[val] - mx) @ W + my - Y[val]) ** 2).sum(0)
            best = np.asarray(alphas)[np.argmin(errs, 0)]
            G, H, mx, my = fit(train)
            for a in np.unique(best):
                cols = np.where(best == a)[0]
                ex = None if exclude is None else exclude[cols]
                W = _ridge_weights(G, H[:, cols], a, ex)
                pred[np.ix_(test, cols)] = (X[test] - mx) @ W + my[cols]
    r2 = pooled_r2(Y, pred)
    return (r2, pred, fold_of) if return_pred else r2


def pooled_r2(Y: np.ndarray, pred: np.ndarray) -> np.ndarray:
    """R2 of every column over all frames, against the mean of the whole column."""
    return 1 - ((Y - pred) ** 2).sum(0) / ((Y - Y.mean(0)) ** 2).sum(0)


def intercept_predictions(Y: np.ndarray, fold_of: np.ndarray) -> np.ndarray:
    """Held-out predictions of a model with only an intercept: the mean of the training frames."""
    pred = np.empty_like(Y)
    for f in np.unique(fold_of):
        pred[fold_of == f] = Y[fold_of != f].mean(0)
    return pred


def within_fold_r2(Y: np.ndarray, pred: np.ndarray, fold_of: np.ndarray) -> np.ndarray:
    """R2 of every column computed within each held-out fold, against that fold's own mean,
    averaged over folds."""
    out = []
    for f in np.unique(fold_of):
        y, p = Y[fold_of == f], pred[fold_of == f]
        out.append(1 - ((y - p) ** 2).sum(0) / ((y - y.mean(0)) ** 2).sum(0))
    return np.mean(out, 0)


# --- clock check ---------------------------------------------------------------------

def shifted_decoding(y: np.ndarray, labels: np.ndarray, shifts: list[int], rng: np.random.Generator,
                     folds: int = 5, components: int = 20) -> np.ndarray:
    """Balanced accuracy of decoding `labels` from rows of y, with the labels shifted by each lag.

    Rows are 1-s bins. A positive shift pairs the activity at t with the label at t - shift, so
    activity that follows behaviour peaks at small positive shifts. Contiguous folds, logistic
    regression on the leading principal components of the training rows.
    """
    from sklearn.decomposition import PCA
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import balanced_accuracy_score

    out = []
    T = len(y)
    for s in shifts:
        if s >= 0:
            yy, ll = y[s:], labels[: T - s]
        else:
            yy, ll = y[: T + s], labels[-s:]
        edges = np.linspace(0, len(yy), folds + 1).astype(int)
        pred = np.zeros(len(yy), bool)
        for f in range(folds):
            test = np.zeros(len(yy), bool)
            test[edges[f]:edges[f + 1]] = True
            if ll[~test].all() or (~ll[~test]).all():
                pred[test] = ll[~test].mean() > 0.5
                continue
            pca = PCA(min(components, yy.shape[1]), random_state=int(rng.integers(1 << 31)))
            xtr = pca.fit_transform(yy[~test])
            clf = LogisticRegression(class_weight="balanced", max_iter=1000).fit(xtr, ll[~test])
            pred[test] = clf.predict(pca.transform(yy[test]))
        out.append(balanced_accuracy_score(ll, pred))
    return np.array(out)


# --- file contents -------------------------------------------------------------------

def list_objects(path: str, version: str = VERSION, under=("analysis", "processing")) -> list[tuple]:
    """Every group and dataset under the given top-level groups of a file: name, shape, type."""
    import h5py
    import remfile

    out = []
    with h5py.File(remfile.File(_url(path, version)), "r") as f:
        def visit(name, obj):
            if name.split("/")[0] in under:
                out.append((name, getattr(obj, "shape", None), obj.attrs.get("neurodata_type", "")))
        f.visititems(visit)
    return out
