"""Loading and measures for the reproduction of Elliott, Andrews et al. (2026) on DANDI:001132.

Raw recordings are streamed from dandiset 001132 at version DANDISET_VERSION. The curated spike
sortings the paper analysed are not in the dandiset; they are read into memory from the paper's
repository (github.com/braingeneers/human_hippocampus at commit CODE_COMMIT), the outside input
the claims file names. Which sorting file belongs to which recording is taken from the paper's
latency notebooks (figures/figure_3/latencies/t_test_try30_try3/*.ipynb at that commit), which
load one file per recording.

Where each parameter comes from is said beside it: the claims file (its criterion, which cites
the paper or its code), a passage of the paper (author, step 1.6), the paper's code, an
assumption, or a standard choice for a detail that cannot change a result.
"""
import io
import pickle
import zipfile

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy import signal, stats

DANDISET_ID = "001132"
DANDISET_VERSION = "0.241130.1903"
CODE_COMMIT = "0f83f704ee4c9b4d8d7f75eb53d94f525c85abb2"
CODE_RAW = f"https://raw.githubusercontent.com/braingeneers/human_hippocampus/{CODE_COMMIT}/"
FS = 20000.0  # sampling rate of the MaxOne recordings (Methods, Data acquisition; checked in the files)

# The eight recordings of Extended Data Table 1, with the sorting file each latency notebook loads.
# 'asset' is the dandiset file holding the raw recording; it is found by the link in the notebook
# (electrode layout and spike-triggered waveforms) and set here once established.
RECORDINGS = {
    1: dict(slice="S1", cond="KA", path="data/ephys/2023-12-03-e-Hc112823_avv9hckcr1/derived/kilosort2/Hc112823_avv9hckcr1_21841_120323_3_acqm.zip"),
    2: dict(slice="S1", cond="baseline", path="data/ephys/2023-12-03-e-Hc112823_avv9hckcr1/curated_base_acqm.pkl"),
    3: dict(slice="S2", cond="KA", path="data/ephys/2023-12-11-e-Hc120523_aav9hckcr1_chip21769/elliott/elliott_chip21769_2.zip"),
    4: dict(slice="S2", cond="baseline", path="data/ephys/2023-12-11-e-Hc120523_aav9hckcr1_chip21769/elliott/elliott_chip21769_base.zip"),
    5: dict(slice="S3", cond="no drug", path="data/ephys/2022-11-02-e-Hc11.1-chip16753/derived/kilosort2/hc11.1_plated-11.1_chip-16753_rec_11.2.22AM-immediate_curated.zip"),
    6: dict(slice="S4", cond="KA", path="data/ephys/2023-11-13-e-Hc110723_hckcr1_21841/hc110723_sd.pkl"),
    7: dict(slice="S5", cond="no drug", path="data/ephys/2023-04-02-e-hc328_unperturbed/sd_ca1_curated.pkl"),
    8: dict(slice="S6", cond="no drug", path="data/ephys/2023-05-10-e-hc52_18790_unperturbed/5-10-23s1-CutData.pkl"),
}


# ---------------------------------------------------------------- sortings (outside input)

class _Stub:
    """Stands in for braingeneers classes when reading the repository's pickles."""
    def __init__(self, *a, **k):
        pass

    def __setstate__(self, state):
        self.__dict__["_state"] = state


class _SafeUnpickler(pickle.Unpickler):
    """Reads pickled SpikeData objects without the braingeneers package; only numpy and
    builtins are rebuilt, every other class becomes an inert stub that keeps its fields."""
    def find_class(self, module, name):
        if module.startswith("numpy") or module in ("builtins", "collections", "_codecs", "copyreg"):
            return super().find_class(module, name)
        return type(name, (_Stub,), {})


def _fetch(path):
    r = requests.get(CODE_RAW + path, timeout=600)
    r.raise_for_status()
    return r.content


def _load_acqm(b):
    z = zipfile.ZipFile(io.BytesIO(b))
    d = np.load(z.open([n for n in z.namelist() if n.endswith(".npz")][0]), allow_pickle=True)
    fs = float(d["fs"])
    train = d["train"].item()
    nd = d["neuron_data"].item()
    keys = sorted(train.keys())
    # spike times are in samples in the acqm format (fs given); converted to ms
    trains = [np.sort(np.asarray(train[k], float)) / fs * 1e3 for k in keys]
    # neuron_data is indexed 0..N-1 in the order of the sorted train keys
    pos = np.array([np.asarray(nd[i]["position"], float) for i in range(len(keys))])
    return trains, pos, None


def _load_phy(b):
    """As human_hip read_phy_files: clusters not labelled 'noise' in cluster_info.tsv, spike times
    in ms, position of the channel with the largest template amplitude."""
    z = zipfile.ZipFile(io.BytesIO(b))
    fs = FS
    for line in z.open("params.py").read().decode().splitlines():
        if "sample_rate" in line:
            fs = float(line.split()[-1])
    clusters = np.load(z.open("spike_clusters.npy")).squeeze()
    st = np.load(z.open("spike_times.npy")).squeeze() / fs * 1e3
    spike_templates = np.load(z.open("spike_templates.npy")).squeeze()
    templates = np.load(z.open("templates.npy"))
    wmi = np.load(z.open("whitening_mat_inv.npy"))
    positions = np.load(z.open("channel_positions.npy"))
    info = pd.read_csv(z.open("cluster_info.tsv"), sep="\t")
    keep = np.array(info["cluster_id"][info["group"] != "noise"])
    keep = np.intersect1d(keep, np.unique(clusters))
    cls_temp = dict(zip(clusters, spike_templates))
    trains, pos = [], []
    for c in keep:
        trains.append(np.sort(st[clusters == c]))
        t = templates[cls_temp[c]] @ wmi
        amp = t.max(0) - t.min(0)
        pos.append(positions[np.argmax(amp)])
    return trains, np.array(pos, float), positions


def _load_pickle(b):
    o = _SafeUnpickler(io.BytesIO(b)).load()
    st = o.__dict__.get("_state", o.__dict__)
    nd = st["_neuron_data"][0]
    keys = list(nd.keys())
    trains = [np.sort(np.asarray(t, float)) for t in st["train"]]  # SpikeData trains are in ms
    pos = np.array([np.asarray(nd[k]["position"], float) for k in keys])
    return trains, pos, float(st["length"])


def load_sorting(rec):
    """Curated units of one recording: dict with trains (ms), pos (um, N x 2), length_ms."""
    path = RECORDINGS[rec]["path"]
    b = _fetch(path)
    if path.endswith(".pkl"):
        trains, pos, length = _load_pickle(b)
    elif path.endswith("_acqm.zip"):
        trains, pos, length = _load_acqm(b)
    else:
        trains, pos, length = _load_phy(b)
    if length is None or isinstance(length, np.ndarray):
        length = max(t[-1] for t in trains if len(t))
    return dict(trains=trains, pos=pos, length_ms=float(length), n=len(trains))


# ---------------------------------------------------------------- dandiset

def list_assets():
    url = f"https://api.dandiarchive.org/api/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=200"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r["next"]
    return out


def asset_url(asset_id):
    r = requests.get(f"https://api.dandiarchive.org/api/assets/{asset_id}/download/", allow_redirects=False, timeout=60)
    return r.headers["Location"]


def open_nwb(asset_id):
    """Open a dandiset NWB file as a stream (h5py over remfile); nothing is written to disk."""
    return h5py.File(remfile.File(asset_url(asset_id)), "r")


def electrodes(f):
    e = f["general/extracellular_ephys/electrodes"]
    return pd.DataFrame(dict(channel=[c.decode() for c in e["channel_name"][:]], electrode=e["electrode"][:],
                             x=e["rel_x"][:], y=e["rel_y"][:]))


def raw_window(f, t0, t1, cols=None):
    """Raw voltage (uV) for seconds t0 to t1, all channels or the given column indices."""
    d = f["acquisition/ElectricalSeries/data"]
    conv = d.attrs["conversion"] * 1e6
    i0, i1 = int(t0 * FS), int(t1 * FS)
    x = d[i0:i1] if cols is None else d[i0:i1][:, cols]
    return x.astype(np.float32) * conv


# ---------------------------------------------------------------- spike measures

def population_rate(trains, length_ms, sigma_ms):
    """Population rate as the Methods define it (Spike rasters with population level firing
    activity): spikes of all units in 1 ms bins, Gaussian smoothing (sigma 10 to 20 ms), divided
    by the number of units, times 1000 (Hz per unit)."""
    from scipy.ndimage import gaussian_filter1d
    nb = int(np.ceil(length_ms)) + 1
    counts = np.zeros(nb)
    for t in trains:
        np.add.at(counts, np.clip(t.astype(int), 0, nb - 1), 1)
    return gaussian_filter1d(counts, sigma_ms) / len(trains) * 1000.0


def sttc(trains, length_ms, dt=20.0):
    """Spike time tiling coefficient (Cutts and Eglen 2014) for all pairs, window dt ms (20 ms, the
    braingeneers default the paper's code uses; claims file)."""
    n = len(trains)
    T = length_ms
    tA = np.zeros(n)
    for i, t in enumerate(trains):
        if len(t) == 0:
            continue
        # fraction of the recording within dt of a spike
        s = np.clip(t - dt, 0, T)
        e = np.clip(t + dt, 0, T)
        # merge overlapping intervals
        cover = 0.0
        cs, ce = s[0], e[0]
        for a, b in zip(s[1:], e[1:]):
            if a > ce:
                cover += ce - cs
                cs, ce = a, b
            else:
                ce = max(ce, b)
        cover += ce - cs
        tA[i] = cover / T
    P = np.zeros((n, n))  # P[i, j]: fraction of spikes of i within dt of a spike of j
    for i in range(n):
        for j in range(n):
            if i == j or len(trains[i]) == 0 or len(trains[j]) == 0:
                continue
            tj = trains[j]
            k = np.searchsorted(tj, trains[i])
            left = np.abs(trains[i] - tj[np.clip(k - 1, 0, len(tj) - 1)])
            right = np.abs(tj[np.clip(k, 0, len(tj) - 1)] - trains[i])
            P[i, j] = np.mean(np.minimum(left, right) <= dt)
    S = np.ones((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            a = (P[i, j] - tA[j]) / (1 - P[i, j] * tA[j]) if P[i, j] * tA[j] != 1 else 0.0
            b = (P[j, i] - tA[i]) / (1 - P[j, i] * tA[i]) if P[j, i] * tA[i] != 1 else 0.0
            S[i, j] = 0.5 * (a + b)
    return S


def nearest_latencies(t1, t2, window=30.0):
    """For each spike of t1 the signed time to the nearest spike of t2 (ms), kept when within
    +-window (Methods, Definition of circuit diagram propagation vector)."""
    if len(t1) == 0 or len(t2) == 0:
        return np.array([])
    k = np.searchsorted(t2, t1)
    lo = t2[np.clip(k - 1, 0, len(t2) - 1)] - t1
    hi = t2[np.clip(k, 0, len(t2) - 1)] - t1
    lat = np.where(np.abs(lo) <= np.abs(hi), lo, hi)
    return lat[np.abs(lat) <= window]


def significant_pairs(trains, S, sttc_min=0.01, window=30.0, min_events=25, min_abs_mean=1.0, alpha=0.05):
    """Circuit pairs (Methods, Definition of circuit diagram propagation vector, with the code's
    details in the claims file): unordered pairs with STTC above 0.01, latencies to the nearest
    spike within +-30 ms, at least 25 of them, absolute mean above 1 ms, one-sample two-sided
    t-test against 0 at p < 0.05; a pair with negative mean latency is reversed and recomputed so
    that it runs from the sending to the receiving unit. Returns rows (send, recv, n_events, mean, p)."""
    n = len(trains)
    rows = []
    for i in range(n):
        for j in range(i + 1, n):
            if not S[i, j] > sttc_min:
                continue
            lat = nearest_latencies(trains[i], trains[j], window)
            a, b = i, j
            # as the code's curate_latencies: test the forward direction first, then reverse a pair
            # with negative mean and require the reversed mean above 1 ms with at least 25 events
            if len(lat) < min_events or abs(lat.mean()) <= min_abs_mean:
                continue
            if lat.mean() < 0:
                a, b = j, i
                lat = nearest_latencies(trains[a], trains[b], window)
                if len(lat) < min_events or lat.mean() <= min_abs_mean:
                    continue
            p = stats.ttest_1samp(lat, 0.0).pvalue
            if p < alpha:
                rows.append((a, b, len(lat), lat.mean(), p))
    return pd.DataFrame(rows, columns=["send", "recv", "n_events", "mean_lat", "p"])


def layer_position(pos, n_samples=100):
    """Position along the cell layer (Methods, Statistical test of circuit geometry; code
    figures/figure_3/haussler): degree-2 polynomial y(x) fitted to all unit positions, sampled at
    100 evenly spaced x from the smallest to the largest unit x; each unit takes the index of the
    nearest sample point."""
    c = np.polyfit(pos[:, 0], pos[:, 1], 2)
    xs = np.linspace(pos[:, 0].min(), pos[:, 0].max(), n_samples)
    curve = np.c_[xs, np.polyval(c, xs)]
    d = ((pos[:, None, :] - curve[None, :, :]) ** 2).sum(-1)
    return d.argmin(1)


def butter_band(x, lo, hi, fs, order=5, axis=0):
    """Zero-phase Butterworth band-pass (human_hip butter_filter: order 5, sosfiltfilt)."""
    sos = signal.butter(order, [lo, hi], btype="band", fs=fs, output="sos")
    return signal.sosfiltfilt(sos, x, axis=axis)


def lowpass_decimate(x, fs_in=FS, fs_out=1000.0, cutoff=100.0):
    """Low-pass then downsample to 1 kHz (Methods, Local field potential signal processing:
    0.1 to 100 Hz before the spectrogram; the paper's raw pickles are at 1 kHz). The low-pass is
    an order-5 Butterworth at 100 Hz, zero phase, as the code's filters."""
    sos = signal.butter(5, cutoff, btype="low", fs=fs_in, output="sos")
    y = signal.sosfiltfilt(sos, x, axis=0)
    step = int(fs_in / fs_out)
    return y[::step]


# ---------------------------------------------------------------- bursts (readings named in the claims file)

def detect_bursts(rate, threshold, merge_ms=50, epoch_gap_s=5.0):
    """Bursts as the claims file reads them (fig1g-ka-synchronized-bursting): peaks of the
    population rate above a threshold, peaks less than 50 ms apart merged (the higher kept), and
    epochs (superbursts) as runs of bursts separated by gaps under 5 s. Returns burst times (s)
    and a list of epochs (arrays of burst times)."""
    from scipy.signal import find_peaks
    pk, _ = find_peaks(rate, height=threshold, distance=merge_ms)
    t = pk / 1000.0
    if len(t) == 0:
        return t, []
    epochs = np.split(t, np.where(np.diff(t) >= epoch_gap_s)[0] + 1)
    return t, epochs


def burst_synchrony(trains, burst_times_s, length_ms, half_window_ms=50.0):
    """Fraction of units whose rate within +-50 ms of each burst peak exceeds their mean rate over
    the recording (claims file, fig1g: 'a burst raises the rate of most units'; the window is a
    standard choice). Returns one fraction per burst."""
    mean_rate = np.array([len(t) / length_ms for t in trains])  # spikes per ms
    out = []
    for b in burst_times_s * 1000:
        c = np.array([np.sum((t >= b - half_window_ms) & (t < b + half_window_ms)) for t in trains])
        out.append(np.mean(c / (2 * half_window_ms) > mean_rate))
    return np.array(out)


# ---------------------------------------------------------------- link of sortings to raw files

def offset_scan(asset_id, sorting, n_units=3):
    """Find where a sorting sits in a raw file: for the n most active units, the high-passed
    (300 to 6000 Hz) trace of the electrode nearest the unit is correlated with the unit's spike
    train at every offset (FFT); a sorting from this file gives a sharp negative peak (the spike
    trough) at its offset. Returns (offset_s, peak_score, null_score), scores in units of the
    median absolute deviation of the correlation, summed over units; null_score is the 100th most
    negative value, the level of chance alignments."""
    sos = signal.butter(3, [300, 6000], btype="band", fs=FS, output="sos")
    f = open_nwb(asset_id)
    e = electrodes(f)
    d = f["acquisition/ElectricalSeries/data"]
    trains = sorting["trains"]
    top = np.argsort([len(t) for t in trains])[::-1][:n_units]
    L = int(max(t[-1] for t in trains if len(t)) * FS / 1000) + 2
    tot = None
    for u in top:
        x, y = sorting["pos"][u]
        col = int(np.argmin((e.x - x) ** 2 + (e.y - y) ** 2))
        v = d[:, col].astype(np.float32)
        v = signal.sosfiltfilt(sos, v - v.mean()).astype(np.float32)
        ind = np.zeros(L, np.float32)
        ind[np.round(trains[u] * FS / 1000).astype(int)] = 1
        c = signal.fftconvolve(v, ind[::-1], mode="full")
        c = (c - np.median(c)) / (np.median(np.abs(c - np.median(c))) + 1e-12)
        tot = c if tot is None else tot + c
    k = int(np.argmin(tot))
    return (k - (L - 1)) / FS, float(tot[k]), float(np.sort(tot)[100])


# ---------------------------------------------------------------- LFP

STEP = 312500  # four HDF5 chunk rows (78125 samples each), a multiple of 20 samples


def _block_lfp(job):
    """Read one 64-channel chunk column of a file between two sample indices and reduce it to
    1 kHz by averaging blocks of 20 samples. A 20-sample mean has zeros at every multiple of 1 kHz,
    so what would alias into the theta and delta bands is suppressed; the bands analysed (0.5 to
    100 Hz) are passed with less than 0.3% loss. Returns (columns, array n_ms x k) in uV."""
    asset_id, cols, i0, i1 = job
    f = open_nwb(asset_id)
    d = f["acquisition/ElectricalSeries/data"]
    conv = d.attrs["conversion"] * 1e6
    c0, c1 = min(cols), max(cols) + 1
    out = []
    for a in range(i0, i1, STEP):
        b = min(a + STEP, i1)
        x = d[a:b, c0:c1][:, np.asarray(cols) - c0].astype(np.float32)
        n = (x.shape[0] // 20) * 20
        out.append(x[:n].reshape(-1, 20, x.shape[1]).mean(1))
    return cols, np.concatenate(out) * conv


def lfp_1khz(asset_id, channels, t0_s, t1_s, n_channels, pool=None):
    """1 kHz LFP of the given channel indices of a file from t0_s to t1_s (file time), read by
    chunk column, in parallel when a process pool is given. Returns array n_ms x len(channels)."""
    channels = np.asarray(channels)
    i0 = int(round(t0_s * FS / 20)) * 20
    i1 = int(round(t1_s * FS / 20)) * 20
    jobs = []
    for blk in np.unique(channels // 64):
        cols = sorted(set(channels[channels // 64 == blk].tolist()))
        jobs.append((asset_id, cols, i0, i1))
    res = list(pool.map(_block_lfp, jobs)) if pool is not None else [_block_lfp(j) for j in jobs]
    col_index = {}
    arrays = []
    k = 0
    for cols, arr in res:
        for j, c in enumerate(cols):
            col_index[c] = k + j
        k += len(cols)
        arrays.append(arr)
    n = min(a.shape[0] for a in arrays)
    allarr = np.concatenate([a[:n] for a in arrays], axis=1)
    return allarr[:, [col_index[c] for c in channels]]


def theta(x, fs=1000.0, order=5):
    """Theta band 4 to 8 Hz, zero-phase Butterworth (order 5 as human_hip butter_filter; the
    Methods' theta plots say fourth order, run as a variant where it matters)."""
    return butter_band(x, 4.0, 8.0, fs, order=order, axis=0)


def phase_lock_unit(spk_ms, th, mode="envelope"):
    """Phase locking of one unit to the theta of its electrode (Methods, Phase locking neurons to
    theta wave activity). th: theta at 1 kHz on the same clock as spk_ms (list of window arrays,
    each with its start in ms). Methods reading ('envelope'): spikes kept while the Hilbert
    envelope exceeds the RMS of the theta series over the analysed span. Code reading ('cycle'):
    spikes kept within theta cycles (trough to trough) whose envelope peak exceeds the RMS of the
    envelope. Returns (n_spikes_kept, rayleigh_p, circular_mean)."""
    from astropy.stats import rayleightest, circmean
    import astropy.units as u
    allth = np.concatenate([w for _, w in th])
    rms_sig = np.sqrt(np.mean(allth ** 2))
    env_all = np.concatenate([np.abs(signal.hilbert(w)) for _, w in th])
    rms_env = np.sqrt(np.mean(env_all ** 2))
    phases = []
    for start, w in th:
        an = signal.hilbert(w)
        ph = np.angle(an)
        env = np.abs(an)
        idx = np.round(spk_ms - start).astype(int)
        idx = idx[(idx >= 0) & (idx < len(w))]
        if mode == "envelope":
            keep = env[idx] > rms_sig
        else:
            troughs = signal.find_peaks(-w)[0]
            ok = np.zeros(len(w), bool)
            for a, b in zip(troughs[:-1], troughs[1:]):
                if env[a:b].max() > rms_env:
                    ok[a:b] = True
            keep = ok[idx]
        phases.append(ph[idx[keep]])
    ph = np.concatenate(phases) if phases else np.array([])
    if len(ph) < 2:
        return len(ph), np.nan, np.nan
    p = float(rayleightest(ph * u.rad))
    return len(ph), p, float(circmean(ph * u.rad).value)


def lag_matrix(th, max_lag=40):
    """Pairwise theta lags (Methods, Electrode spatial clustering algorithm): for every electrode
    pair the lag in ms (1 kHz samples) within +-40 ms that maximises the absolute cross-correlation
    (as scipy correlate on the window). th: T x N theta of one window. L[i, j] > 0 means that
    electrode j follows electrode i. Also returns the correlation at that lag."""
    x = (th - th.mean(0)) / (th.std(0) + 1e-12)
    T, N = x.shape
    best = np.zeros((N, N), np.float32)
    lag = np.zeros((N, N), np.int16)
    for l in range(-max_lag, max_lag + 1):
        if l >= 0:
            c = x[: T - l].T @ x[l:] / T
        else:
            c = x[-l:].T @ x[: T + l] / T
        upd = np.abs(c) > np.abs(best)
        best[upd] = c[upd]
        lag[upd] = l
    return lag.astype(float), best


def spatial_coherence(xy, labels, k=8, n_shuffle=1000, rng=None):
    """Measure named in the claims file (ext4-electrode-lag-clusters): the fraction of electrodes
    whose label equals the majority label of their 8 nearest electrodes, and the same fraction for
    labels shuffled over positions (1000 shuffles)."""
    from scipy.spatial import cKDTree
    nn = cKDTree(xy).query(xy, k + 1)[1][:, 1:]

    def frac(lab):
        maj = (lab[nn].mean(1) > 0.5).astype(int)
        tie = lab[nn].mean(1) == 0.5
        return np.mean((maj == lab) & ~tie)

    lab = np.asarray(labels).astype(int)
    obs = frac(lab)
    null = np.array([frac(rng.permutation(lab)) for _ in range(n_shuffle)])
    return obs, null


def plane_direction(xy, lag):
    """Direction of propagation (claims file reading for fig1j): each electrode's mean lag to all
    others is how far it leads; arrival time is its negative; a plane fitted to arrival time over
    electrode positions gives the gradient, the direction of travel. Returns (angle in degrees
    in the electrode coordinate frame, R^2 of the plane, speed slope in ms per mm)."""
    arrival = -lag.mean(1)
    Xd = np.c_[xy, np.ones(len(xy))]
    coef, *_ = np.linalg.lstsq(Xd, arrival, rcond=None)
    pred = Xd @ coef
    r2 = 1 - np.sum((arrival - pred) ** 2) / np.sum((arrival - arrival.mean()) ** 2)
    return float(np.degrees(np.arctan2(coef[1], coef[0]))), float(r2), float(np.hypot(coef[0], coef[1]) * 1000)


def layer_axes(pos):
    """Long axis of the cell layer (the chord of the degree-2 fit of unit positions between the
    smallest and largest unit x, as in layer_position) and the normal pointing to the convex side
    of the fit, away from the hilus that the dentate granule cell layer curves around (an
    assumption: the hilus lies on the concave side of the layer)."""
    c = np.polyfit(pos[:, 0], pos[:, 1], 2)
    xs = np.array([pos[:, 0].min(), pos[:, 0].max()])
    p0, p1 = np.c_[xs, np.polyval(c, xs)]
    axis = (p1 - p0) / np.linalg.norm(p1 - p0)
    normal = np.array([-axis[1], axis[0]])
    xm = xs.mean()
    mid_curve = np.array([xm, np.polyval(c, xm)])
    mid_chord = (p0 + p1) / 2
    # the curve bulges from the chord toward the convex side
    if np.dot(mid_curve - mid_chord, normal) < 0:
        normal = -normal
    return axis, normal


def angle_between(a_deg, b_deg, axial=False):
    d = abs(a_deg - b_deg) % 360
    d = min(d, 360 - d)
    return min(d, 180 - d) if axial else d
