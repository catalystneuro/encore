"""Loading and measures for Zaki et al. (2024) on DANDI:000718.

Zaki, Pennington, Morales-Rodriguez et al., "Offline ensemble co-reactivation links memories
across days", Nature 637, 145-155, doi:10.1038/s41586-024-08168-4.

Every file is streamed from the archive at the pinned version (``VERSION``) with remfile and h5py;
nothing is written to disk. Only the arrays an analysis needs are read (the raw Miniscope movies are
never touched).

Where each parameter comes from:

- Deconvolved activity is analysed (Methods, "Miniscope data processing and data alignment":
  "Deconvolved calcium activities were analysed in these studies"); claims file, method choices.
- Burst detection (``population_trace``, ``burst_events``): each cell z-scored over time, the mean
  over cells z-scored, and a burst is a maximal run of frames above z = 2 (Methods, "Burst
  participation analysis": "all cells that were recorded during that session were z-scored along
  the time dimension ... the mean population activity across the whole population was computed
  across the session and that one-dimensional trace was z-scored. Time periods when the mean
  population activity reached above a threshold of z = 2 were considered to be burst events").
  Cells with no activity (zero variance) cannot be z-scored and are left out (claims file).
- Surrogates (``circular_shift_surrogates``): each cell's trace circularly shifted by an independent
  random offset, the population trace recomputed and z-scored (Extended Data Fig. 3l legend:
  "Neuron activities were circularly shuffled 1000 times relative to one another and the mean
  population activity was re-computed each time"); claims offline-bursts-above-shuffle and
  offline-skew-above-shuffle. The offsets are drawn uniformly from 0 to T-1 frames: the legend does
  not give their range; a uniform draw over the whole recording is the standard choice and is an
  assumption stated in the record. With ``normalise=False`` (reading (b) of the burst claim's
  criterion) the surrogate trace keeps the true trace's mean and, for positively co-varying cells,
  has a smaller SD, so it rarely reaches the true trace's threshold whether or not the cells burst
  (the notebook's synthetic check).
- Ensembles (``ensembles_from_registration``): from the CellReg table, an offline cell is neutral
  (matched to neutral encoding only), aversive (to FC only), overlap (both) or remaining (neither)
  (Methods, "Ensemble reactivation analysis").
- Ensemble participation (``ensemble_traces``, ``coparticipation``): each ensemble's mean activity
  (mean over its cells of the z-scored traces) is z-scored, and the ensemble participates in a burst
  when it exceeds z = 2 at any frame of the burst (Methods, "Ensemble co-participation analysis":
  "the 'participation' of the neutral ensemble or aversive ensemble was measured on the basis of
  whether the ensemble's mean population activity was above the z = 2 threshold during the
  population level event"; for Fig. 5, "These mean activities were z-scored").
- Sleep state of a frame or burst: the SleepIntervals row containing it (Methods, "each frame of
  calcium activity was aligned with the sleep state the mouse was in at that time"); a burst takes
  the state of its peak frame (claims file, fig5c-wake-overlap-neutral-coburst).
- Freezing (``freezing_readings``): reading (a) the fraction of MotionSeries frames inside a
  FreezingIntervals row and (b) the summed interval duration over the MotionSeries duration
  (claims file, source-data-link). Frames are at ``starting_time + i / rate``.
- Sleep scoring (``epoch_features``, ``gmm2``, ``score_sleep``, ``sleep_features``): 6 s epochs, a
  two-state Gaussian mixture on the EMG (lower state sleep), then one on the theta (5-9 Hz) / delta
  (0.5-4 Hz) ratio of the sleep epochs (higher state REM) (Methods, "Sleep recordings and sleep
  scoring"). The EMG feature (log RMS) and the band power (periodogram) are not given by the paper
  and are assumptions; the ratio is fitted as given and, as a variant, as its log.
- Movement (``movement_bins``): the absolute ActivitySignal averaged in 100 ms bins (claims file,
  burst-locomotion-pause).
"""

from __future__ import annotations

import functools

import h5py
import numpy as np
import remfile
import requests

DANDISET = "000718"
VERSION = "0.261122.2159"
API = "https://api.dandiarchive.org/api"

# The paper's source-data repository (Data availability), read only for the link claim.
SOURCE_DATA_REPO = "denisecailab/RetrospectiveMemoryLinkingData_2024"
SOURCE_DATA_COMMIT = "a5081645d3d3e5743ade58ea632c28b003794345"

OFFLINE = {
    "Ca_EEG2-1 Day2 S1": "sub-Ca-EEG2-1/sub-Ca-EEG2-1_ses-OfflineDay2Session1_ophys.nwb",
    "Ca_EEG3-4 Day1 S1": "sub-Ca-EEG3-4/sub-Ca-EEG3-4_ses-OfflineDay1Session1_ophys.nwb",
    "Ca_EEG3-4 Day2 S1": "sub-Ca-EEG3-4/sub-Ca-EEG3-4_ses-OfflineDay2Session1_ophys.nwb",
}
WEEK = "sub-Ca-EEG2-1/sub-Ca-EEG2-1_ses-Week.nwb"
THRESHOLD = 2.0  # z, Methods "Burst participation analysis"


@functools.lru_cache(maxsize=None)
def assets(version: str = VERSION) -> dict:
    """Path -> asset record for every asset of the dandiset at ``version``."""
    out, url = {}, f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=200"
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        d = r.json()
        for a in d["results"]:
            out[a["path"]] = a
        url = d.get("next")
    return out


def asset_metadata(path: str, version: str = VERSION) -> dict:
    a = assets(version)[path]
    r = requests.get(f"{API}/dandisets/{DANDISET}/versions/{version}/assets/{a['asset_id']}/", timeout=60)
    r.raise_for_status()
    return r.json()


def s3_url(path: str, version: str = VERSION) -> str:
    a = assets(version)[path]
    r = requests.head(f"{API}/assets/{a['asset_id']}/download/", allow_redirects=True, timeout=60)
    return r.url


def open_h5(path: str, version: str = VERSION) -> h5py.File:
    """Stream one NWB file of the dandiset (no download)."""
    return h5py.File(remfile.File(s3_url(path, version)), "r")


def text(ds) -> str:
    v = ds[()]
    return v.decode() if isinstance(v, bytes) else str(v)


def table(group) -> dict:
    """Columns of a DynamicTable / TimeIntervals group as numpy arrays (strings decoded)."""
    out = {}
    for k, ds in group.items():
        if not isinstance(ds, h5py.Dataset) or ds.dtype.kind == "V" or k.endswith("_index"):
            continue
        v = ds[()]
        if v.dtype.kind in "OS":
            v = np.array([x.decode() if isinstance(x, bytes) else x for x in v])
        out[k] = v
    return out


# ---------------------------------------------------------------- behaviour

def freezing_readings(f: h5py.File) -> dict:
    """Freezing of a behaviour session from its FreezingIntervals and MotionSeries."""
    ms = f["processing/behavior/MotionSeries"]
    n = ms["data"].shape[0]
    t0 = float(ms["starting_time"][()])
    rate = float(ms["starting_time"].attrs["rate"])
    t = t0 + np.arange(n) / rate
    fi = table(f["processing/behavior/FreezingIntervals"])
    inside = np.zeros(n, bool)
    for s, e in zip(fi["start_time"], fi["stop_time"]):
        inside |= (t >= s) & (t <= e)
    return {
        "a_frames": 100 * inside.mean(),
        "b_duration": 100 * np.sum(fi["stop_time"] - fi["start_time"]) / (n / rate),
        "frame_times": t,
        "frozen": inside,
        "n_intervals": len(fi["start_time"]),
        "rate": rate,
        "motion": ms["data"][:],
    }


def binned_freezing(fr: dict, bin_s: float = 30.0) -> np.ndarray:
    """Per-bin freezing percentage (reading a), bins from the first frame.

    A 5 min session holds 8997 to 8999 frames (299.9 s at 30 Hz), so the number of bins is the
    duration over ``bin_s`` rounded (10 for 30 s bins, as the criterion has it); frames past the
    last full bin go into the last bin."""
    t, z = fr["frame_times"], fr["frozen"]
    nb = int(round(len(t) / fr["rate"] / bin_s))
    b = np.minimum(((t - t[0]) // bin_s).astype(int), nb - 1)
    return np.array([100 * z[b == i].mean() for i in range(nb)])


# ---------------------------------------------------------------- imaging

def deconvolved(f: h5py.File) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """(frames x cells deconvolved activity, frame times, plane-segmentation ROI ids per column)."""
    g = f["processing/ophys/Fluorescence/Deconvolved"]
    data = g["data"][()]
    ts = g["timestamps"][()]
    rois = f["processing/ophys/Fluorescence/Denoised/rois"][()]
    return data, ts, rois


def zscore_cells(X: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Each column z-scored over time; columns with zero variance are left out (returned mask)."""
    sd = X.std(axis=0)
    keep = sd > 0
    Z = (X[:, keep] - X[:, keep].mean(axis=0)) / sd[keep]
    return Z, keep


def zscore(x: np.ndarray) -> np.ndarray:
    return (x - x.mean()) / x.std()


def population_trace(Z: np.ndarray) -> np.ndarray:
    """z-scored mean of the z-scored cells."""
    return zscore(Z.mean(axis=1))


def burst_events(p: np.ndarray, thr: float = THRESHOLD) -> list[tuple[int, int, int]]:
    """Maximal runs of frames with p > thr, as (first frame, last frame inclusive, peak frame)."""
    above = p > thr
    d = np.diff(np.r_[0, above.astype(int), 0])
    starts, ends = np.flatnonzero(d == 1), np.flatnonzero(d == -1) - 1
    return [(int(s), int(e), int(s + np.argmax(p[s:e + 1]))) for s, e in zip(starts, ends)]


def burst_frequency(p: np.ndarray, duration_min: float, thr: float = THRESHOLD) -> float:
    above = p > thr
    n = int(np.sum(np.diff(np.r_[0, above.astype(np.int8)]) == 1))
    return n / duration_min


def skew(x: np.ndarray) -> float:
    """Sample skewness, as scipy.stats.skew (biased, the default)."""
    x = np.asarray(x, float)
    m = x.mean()
    d = x - m
    return float(np.mean(d ** 3) / np.mean(d ** 2) ** 1.5)


def circular_shift_surrogates(Z: np.ndarray, rng: np.random.Generator, n: int, measure,
                              normalise: bool = True) -> np.ndarray:
    """``measure(population trace)`` for ``n`` surrogates, each cell circularly shifted by an
    independent offset drawn uniformly from 0..T-1 (Extended Data Fig. 3l).

    With ``normalise`` (reading (a) of the criterion) the surrogate mean trace is z-scored as for
    the data; without it the raw mean over cells is passed to ``measure``, which for reading (b)
    thresholds it at the true trace's mean plus 2 SD. The paper does not say which was done."""
    T, N = Z.shape
    Zd = np.concatenate([Z, Z]).T.astype(np.float64, copy=False)  # N x 2T, row j doubled
    Zd = np.ascontiguousarray(Zd)
    out = np.empty(n)
    for i in range(n):
        s = rng.integers(0, T, N)
        acc = np.zeros(T)
        for j in range(N):
            acc += Zd[j, T - s[j]:2 * T - s[j]]
        out[i] = measure(zscore(acc / N) if normalise else acc / N)
    return out


# ---------------------------------------------------------------- ensembles and sleep

def ensembles_from_registration(reg: dict, offline_col: str, neutral_col: str, fc_col: str,
                                rois: np.ndarray) -> dict:
    """Ensemble label per column of the offline Deconvolved matrix, from a CellReg table.

    ``reg`` holds the table's columns (ROI ids per session, -9999 for none)."""
    off = reg[offline_col]
    m = off >= 0
    labels = {}
    for o, ne, fc in zip(off[m], reg[neutral_col][m], reg[fc_col][m]):
        n, a = ne >= 0, fc >= 0
        labels[int(o)] = "overlap" if (n and a) else "neutral" if n else "aversive" if a else "remaining"
    return {"labels": np.array([labels.get(int(r), "unregistered") for r in rois]),
            "n_rows": int(m.sum()), "n_unique": int(np.unique(off[m]).size)}


def ensemble_traces(Z: np.ndarray, labels: np.ndarray) -> dict:
    """z-scored mean of each ensemble's z-scored cells."""
    return {e: zscore(Z[:, labels == e].mean(axis=1)) for e in ("neutral", "aversive", "overlap", "remaining")
            if np.any(labels == e)}


def state_at(times: np.ndarray, sleep: dict) -> np.ndarray:
    """Sleep state of each time (the SleepIntervals row containing it; 'none' outside every row)."""
    out = np.full(len(times), "none", dtype=object)
    for s, e, st in zip(sleep["start_time"], sleep["stop_time"], sleep["sleep_state"]):
        out[(times >= s) & (times <= e)] = st
    return out


def coparticipation(events, traces: dict, thr: float = THRESHOLD) -> dict:
    """Per event, whether each ensemble's z-scored mean exceeds thr at any frame of the event."""
    part = {e: np.array([np.any(tr[s:f + 1] > thr) for s, f, _ in events]) for e, tr in traces.items()}
    return part


# ---------------------------------------------------------------- telemetry

def movement_bins(activity: np.ndarray, t0: float, rate: float, bin_s: float = 0.1):
    """Absolute ActivitySignal averaged in ``bin_s`` bins; returns (bin centres, values)."""
    per = int(round(bin_s * rate))
    nb = len(activity) // per
    a = np.abs(activity[:nb * per]).reshape(nb, per).mean(axis=1)
    centres = t0 + (np.arange(nb) + 0.5) * per / rate
    return centres, a


def epoch_features(f: h5py.File, epoch_s: float = 6.0, chunk_epochs: int = 800) -> dict:
    """Per-epoch telemetry features of a file's continuous EEG and EMG, read in chunks.

    6 s epochs (Methods, "Sleep recordings and sleep scoring": "the data were binned into 6 s
    epochs"). Per epoch: EMG RMS, EEG power in delta (0.5-4 Hz) and theta (5-9 Hz) (the bands of
    the same passage), and whether the EEG or EMG is exactly constant (the mouse off its
    receiver). Power is the periodogram summed over the band, a standard choice."""
    eeg, emg = f["acquisition/EEGSignal/data"], f["acquisition/EMGSignal/data"]
    fs = float(f["acquisition/EEGSignal/starting_time"].attrs["rate"])
    E = int(round(epoch_s * fs))
    n = eeg.shape[0] // E
    fr = np.fft.rfftfreq(E, 1 / fs)
    dl, th = (fr >= 0.5) & (fr < 4), (fr >= 5) & (fr <= 9)
    out = {k: np.empty(n) for k in ("rms", "delta", "theta")}
    out["flat"] = np.empty(n, bool)
    for i0 in range(0, n, chunk_epochs):
        i1 = min(n, i0 + chunk_epochs)
        a = eeg[i0 * E:i1 * E].reshape(-1, E).astype(np.float64)
        b = emg[i0 * E:i1 * E].reshape(-1, E).astype(np.float64)
        out["flat"][i0:i1] = (np.ptp(a, axis=1) == 0) | (np.ptp(b, axis=1) == 0)
        out["rms"][i0:i1] = np.sqrt(((b - b.mean(1, keepdims=True)) ** 2).mean(1))
        P = np.abs(np.fft.rfft(a - a.mean(1, keepdims=True), axis=1)) ** 2
        out["delta"][i0:i1], out["theta"][i0:i1] = P[:, dl].sum(1), P[:, th].sum(1)
    out["epoch_s"] = epoch_s
    return out


def gmm2(x: np.ndarray, iters: int = 300):
    """Two-component 1-D Gaussian mixture by EM; returns (means, SDs, weights, responsibilities),
    components ordered by mean. Starts from the 25th and 75th percentiles (a standard choice)."""
    x = np.asarray(x, float)
    mu, sd, pi = np.percentile(x, [25, 75]), np.full(2, x.std() / 2), np.array([0.5, 0.5])
    for _ in range(iters):
        ll = np.stack([np.log(pi[k]) - np.log(sd[k]) - 0.5 * ((x - mu[k]) / sd[k]) ** 2 for k in range(2)], 1)
        r = np.exp(ll - ll.max(1, keepdims=True))
        r /= r.sum(1, keepdims=True)
        nk = r.sum(0)
        pi, mu = nk / len(x), (r * x[:, None]).sum(0) / nk
        sd = np.sqrt((r * (x[:, None] - mu) ** 2).sum(0) / nk)
    o = np.argsort(mu)
    return mu[o], sd[o], pi[o], r[:, o]


def score_sleep(feat: dict, log_ratio: bool = False) -> np.ndarray:
    """Wake / nrem / rem per epoch ('none' where the telemetry is constant).

    Methods, "Sleep recordings and sleep scoring": "the EMG data were fit with a Gaussian mixture
    model with two states, in which the lower state represented sleep and the higher state
    represented wake", then "a ratio of theta to delta signal was calculated. A Gaussian mixture
    model was fit to this theta/delta ratio with two states, in which high theta/delta meant REM".
    The EMG is fitted as log RMS (an assumption: the Methods do not name the EMG feature, and
    amplitude is usually fitted on a log scale); the ratio as given, or its log with
    ``log_ratio``."""
    ok = ~feat["flat"]
    state = np.full(len(ok), "none", dtype=object)
    _, _, _, r = gmm2(np.log(feat["rms"][ok]))
    idx = np.flatnonzero(ok)
    sleep = idx[r[:, 0] > 0.5]
    state[idx] = "wake"
    ratio = feat["theta"][sleep] / feat["delta"][sleep]
    _, _, _, r2 = gmm2(np.log(ratio) if log_ratio else ratio)
    state[sleep] = np.where(r2[:, 1] > 0.5, "rem", "nrem")
    return state


def sleep_features(state: np.ndarray, epoch_s: float = 6.0) -> dict:
    """Percent time per state, mean bout length (s) per state, and transition probabilities
    between states, over the scored epochs of ``state`` (Extended Data Fig. 10 legend: "time
    spent in each sleep state", "bout length", "transition probabilities")."""
    ok = state != "none"
    out = {f"% {s}": 100 * np.mean(state[ok] == s) for s in ("wake", "nrem", "rem")}
    out["% sleep"] = out["% nrem"] + out["% rem"]
    b = np.flatnonzero(np.r_[True, state[1:] != state[:-1]])
    lab, ln = state[b], np.diff(np.r_[b, len(state)])
    for s in ("wake", "nrem", "rem"):
        out[f"bout {s} (s)"] = epoch_s * ln[lab == s].mean() if np.any(lab == s) else np.nan
    seq = [x for x in lab if x != "none"]
    pairs = list(zip(seq[:-1], seq[1:]))
    for a in ("wake", "nrem", "rem"):
        na = sum(1 for x, _ in pairs if x == a)
        for c in ("wake", "nrem", "rem"):
            if a != c:
                out[f"P({a}->{c})"] = sum(1 for x, y in pairs if x == a and y == c) / na if na else np.nan
    return out


def source_data_csv(path: str):
    """One CSV of the paper's source-data repository at the pinned commit."""
    import io

    import pandas as pd

    url = f"https://raw.githubusercontent.com/{SOURCE_DATA_REPO}/{SOURCE_DATA_COMMIT}/{path}"
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    return pd.read_csv(io.StringIO(r.text), index_col=0)
