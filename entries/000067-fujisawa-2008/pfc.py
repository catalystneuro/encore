"""Loading and measures for dandiset 000067 (Fujisawa, Amarasingham, Harrison & Buzsaki 2008).

Fujisawa S, Amarasingham A, Harrison MT, Buzsaki G (2008). Behavior-dependent short-term
assembly dynamics in the medial prefrontal cortex. Nature Neuroscience 11, 823-833.
doi:10.1038/nn.2134.

Each NWB file is one recording session of one rat (EE, FF or GG). Working memory sessions hold
the spike times of every sorted cluster of the session, the trial table (correct trials only),
the linearized position, the x coordinate of the head LEDs, the LFP at 1250 Hz and, in most of
them, the wideband signal at 20 kHz. Files are streamed from the archive at the pinned version;
nothing is written to disk.

What the files do not say, and where it is taken from here:

- The units table holds spike times only: no shank, channel, brain region or cell type, and no
  flag for multi-unit clusters. The shank of each unit is found from the data: the mean
  wideband waveform (800 to 5000 Hz, the band the Methods give for spike sorting) of its spikes
  in a few windows of the raw signal, on every channel; the unit's channel is the one with the
  largest peak-to-trough amplitude. The region of a channel comes from the CRCNS pfc-2 data
  description (doi:10.6080/K01V5BWK, version 0.7 of the document): channels 1 to 64 are the
  64-site prefrontal probe (8 shanks of 8 sites, so shank = channel // 8 counting from 0) and
  the next 32 are the CA1 probe. The notebook checks this map against the LFP.
- Multi-unit clusters: the conversion read the clusters with spikeextractors'
  NeuroscopeSortingExtractor, which keeps cluster 1 (multi-unit activity) and puts it first in
  each shank's block of units, and puts the shanks one after another. Here a cluster is taken as
  multi-unit when more than `MAX_ISI_VIOLATION` of its inter-spike intervals are shorter than
  2 ms (a common choice); the conversion's rule, the first unit of each shank block, is a
  variant. The notebook shows the evidence for both.
- The trial table's columns are those of the CRCNS SessionNP matrix: `start_time` is the start
  of the first nose poke, `stop_time` the end of the last nose poke (the paper's trial start,
  position 0) and `reward_time` the start of reward consumption (the paper's trial end, position
  1). Here they are named nosepoke_start, run_start and run_end.
- The linearized position runs from 1 (start) to 2 (reward) and is 0 outside trials; the paper's
  normalized position is d - 1.

Parameters, and where they come from:

- JITTER_S = 0.005, N_JITTER = 1000, CCG window of +-5 ms, significance when the cross-
  correlogram breaks the 99% global band anywhere from 1 to 4 ms: the paper's Methods.
  The bin width of the cross-correlogram (1 ms) is not given in the main text and is chosen here.
- KERNEL_SIGMA = 0.05 (normalized length), the permutation test of left against right with
  pointwise and global bands at alpha 0.05: the paper's Methods. The number of permutations
  (N_PERM = 1000) and the position grid (101 points) are chosen here.
  The Poisson screen before the Monte Carlo test (`connections`) is chosen here, to save time.
- Coincidence lags of 1 to 4 ms for position dependence of monosynaptic interactions, and the
  one-sided global band at 0.01: the paper's Methods. The band is built from the surrogates'
  mean and s.d. (`band_test`, kind "sd"), chosen here because the Methods' rank band cannot
  reach 0.01 with 1000 surrogates.
- First spikes after at least 200 ms of silence and later spikes within 40 ms of the previous
  one, a permutation test of the labels at two-sided P < 0.10: the paper's Results and Figure 6
  legend. The measure of transmission (excess spikes from 1 to 4 ms per presynaptic spike, over
  the jitter expectation) is chosen here; the paper's "rate-normalized height" is defined in a
  supplementary figure that could not be retrieved.
- The 1 Hz minimum of peak rate in trials for position analyses is the "Cells" criterion of
  the CRCNS pfc-2 description, not the paper.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy.signal import butter, decimate, sosfiltfilt, welch

DANDISET_ID = "000067"
DANDISET_VERSION = "0.250624.0419"

RAW_HZ = 20000.0
LFP_HZ = 1250.0
RAW_CHUNK = 136719              # rows per HDF5 chunk of the wideband series (one channel each)
N_PFC_CHANNELS = 64             # CRCNS pfc-2: channels 1-64 are the prefrontal probe
# Channels are 0-based here. CRCNS pfc-2 gives, 1-based, 65-96 for CA1 and 97 (right) and 98
# (left) for the nose-poke sensors in every rat. The data agree for rats EE and FF; in rat GG
# the sensors are at 65 and 66 and the CA1 probe at 70-101 (see the notebook's data check), and
# the sensor at 66 is the one active on trials labelled Right.
CRCNS_CA1 = range(64, 96)
CRCNS_NOSEPOKE = (96, 97)                      # (right, left)
CA1_CHANNELS = {"EE": range(64, 96), "FF": range(64, 96), "GG": range(69, 101)}
NOSEPOKE_CHANNELS = {"EE": (96, 97), "FF": (96, 97), "GG": (65, 64)}
SENSOR_READ = (64, 65, 96, 97)                 # LFP columns read for the sensor checks
SPIKE_BAND = (800.0, 5000.0)
SHIFT_SAMPLES = 60              # 3 ms, for the clock check of spike times against the raw signal

JITTER_S = 0.005
N_JITTER = 1000
KERNEL_SIGMA = 0.05
N_PERM = 1000
GRID = np.linspace(0, 1, 101)
MIN_PEAK_HZ = 1.0
MAX_AUX_NEURAL_UV = 200.0     # largest on a sensor channel and below this on the probes: a sensor cluster
MAX_ISI_VIOLATION = 0.02      # fraction of ISIs < 2 ms above which a cluster is multi-unit (chosen here)

# Working memory sessions in CRCNS pfc-2's session table that have a trial table here.
WM_SESSIONS = ["EE.049", "EE.088", "EE.196", "FF.103", "FF.130", "FF.167", "GG.069", "GG.097",
               "GG.149"]


def asset_urls() -> dict[str, str]:
    """{path: streaming URL} of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return {a.path: a.get_content_url(follow_redirects=1, strip_query=True)
                for a in dandiset.get_assets() if a.path.endswith(".nwb")}


def _text(value) -> str:
    value = value[()]
    if isinstance(value, np.ndarray):
        value = value.ravel()[0]
    return value.decode() if isinstance(value, bytes) else str(value)


def describe_file(path: str, url: str) -> dict:
    """What one file holds, without reading the large series."""
    with h5py.File(remfile.File(url), "r") as f:
        out = {"path": path, "session": _text(f["general/session_id"]),
               "subject": _text(f["general/subject/subject_id"]),
               "start": _text(f["session_start_time"])[:10]}
        el = f["general/extracellular_ephys/electrodes"]
        out["channels"] = len(el["id"])
        out["locations"] = sorted({v.decode() for v in el["location"][:]})
        out["groups"] = len({v.decode() for v in el["group_name"][:]})
        out["xyz_all_nan"] = bool(all(np.isnan(el[k][:]).all() for k in "xyz"))
        out["raw_s"] = (f["acquisition/ElectricalSeries/data"].shape[0] / RAW_HZ
                        if "acquisition/ElectricalSeries" in f else 0.0)
        out["lfp_s"] = f["processing/ecephys/LFP/LFP/data"].shape[0] / LFP_HZ
        out["units"] = len(f["units/id"]) if "units" in f else 0
        out["unit_columns"] = list(f["units"].attrs["colnames"]) if "units" in f else []
        out["spikes"] = len(f["units/spike_times"]) if "units" in f else 0
        out["trials"] = len(f["intervals/trials/id"]) if "intervals/trials" in f else 0
        out["position"] = "processing/behavior" in f
        # fingerprints used to look for recordings deposited twice
        lfp = f["processing/ecephys/LFP/LFP/data"]
        out["lfp_head"] = lfp[:1250, 0].astype(np.int64).tobytes().hex()[:64] if lfp.shape[0] else ""
        out["spike_head"] = (np.round(f["units/spike_times"][:50] * RAW_HZ).astype(np.int64).tobytes().hex()[:64]
                             if out["spikes"] else "")
    return out


def _sorted_trains(times: np.ndarray, index: np.ndarray):
    bounds = np.concatenate([[0], index]).astype(np.int64)
    trains, unsorted = [], []
    for i in range(len(index)):
        s = times[bounds[i]:bounds[i + 1]]
        if np.any(np.diff(s) < 0):
            unsorted.append(i)
            s = np.sort(s)
        trains.append(s)
    return trains, unsorted


def _raw_windows(trials: pd.DataFrame, n_chunks: int, n_windows: int) -> np.ndarray:
    """Chunks of the raw series that overlap trials most, spread over the session."""
    t0 = np.arange(n_chunks) * RAW_CHUNK / RAW_HZ
    t1 = t0 + RAW_CHUNK / RAW_HZ
    overlap = np.zeros(n_chunks)
    for a, b in zip(trials.nosepoke_start, trials.run_end):
        overlap += np.clip(np.minimum(t1, b) - np.maximum(t0, a), 0, None)
    candidates = np.flatnonzero(overlap > 0)
    if len(candidates) <= n_windows:
        return candidates
    picks = np.linspace(0, len(candidates) - 1, n_windows).round().astype(int)
    return candidates[picks]


def load_session(path: str, url: str, n_windows: int = 12) -> dict:
    """One working memory session: spikes, trials, position, unit channels and LFP checks."""
    s = {"path": path}
    with h5py.File(remfile.File(url), "r") as f:
        s["session"] = _text(f["general/session_id"])
        s["subject"] = _text(f["general/subject/subject_id"])
        s["trains"], s["unsorted_units"] = _sorted_trains(f["units/spike_times"][:],
                                                          f["units/spike_times_index"][:])
        tr = f["intervals/trials"]
        s["trials"] = pd.DataFrame({
            "nosepoke_start": tr["start_time"][:], "run_start": tr["stop_time"][:],
            "run_end": tr["reward_time"][:],
            "side": [v.decode() for v in tr["left_or_right"][:]]})
        s["trial_descriptions"] = {k: tr[k].attrs.get("description") for k in tr.attrs["colnames"]}
        beh = f["processing/behavior"]
        lin = beh["LinearizedPosition/LinearizedTimeSeries"]
        s["lin"] = lin["data"][:]
        s["lin_rate"] = float(lin["starting_time"].attrs["rate"])
        s["lin_unit"] = lin["data"].attrs["unit"]
        s["x1"] = beh["Position/SpatialSeries1/data"][:, 0]
        s["x2"] = beh["Position/SpatialSeries2/data"][:, 0]
        s["pos_unit"] = beh["Position/SpatialSeries1/data"].attrs["unit"]
        lfp = f["processing/ecephys/LFP/LFP/data"]
        s["lfp_rate"] = float(f["processing/ecephys/LFP/LFP/starting_time"].attrs["rate"])
        s["duration"] = lfp.shape[0] / s["lfp_rate"]
        s["n_channels"] = lfp.shape[1]
        cols = [c for c in SENSOR_READ if c < lfp.shape[1]]
        s["sensors"] = dict(zip(cols, lfp[:, cols].astype(np.float32).T))
        s["has_raw"] = "acquisition/ElectricalSeries" in f
        s["sta_amp"] = None
        if s["has_raw"]:
            raw = f["acquisition/ElectricalSeries/data"]
            s["raw_rate"] = float(f["acquisition/ElectricalSeries/starting_time"].attrs["rate"])
            windows = _raw_windows(s["trials"], raw.shape[0] // RAW_CHUNK, n_windows)
            s.update(_waveforms_and_theta(raw, windows, s["trains"]))
    return s


def _waveforms_and_theta(raw, windows, trains, per_window: int = 200) -> dict:
    """Mean wideband waveform amplitude of each unit on each channel, and LFP theta per channel.

    The same amplitude with every spike time moved 3 ms later (`sta_amp_shifted`) is the check
    that the spike times share the clock of the raw signal.
    Theta ratio: power from 6 to 10 Hz over power from 1 to 40 Hz of the raw signal decimated to
    1250 Hz, averaged over the windows (which overlap trials, when the rat runs).
    """
    sos = butter(3, SPIKE_BAND, btype="band", fs=RAW_HZ, output="sos")
    n_ch = raw.shape[1]
    acc = np.zeros((len(trains), n_ch, 32))
    shifted = np.zeros((len(trains), n_ch, 32))
    count = np.zeros(len(trains), int)
    spectra = []
    for w in windows:
        x = raw[w * RAW_CHUNK:(w + 1) * RAW_CHUNK, :].astype(np.float32)
        low = decimate(decimate(x, 4, axis=0), 4, axis=0)
        freq, p = welch(low, fs=RAW_HZ / 16, nperseg=1024, axis=0)
        spectra.append(p)
        hp = sosfiltfilt(sos, x, axis=0)
        a, b = w * RAW_CHUNK / RAW_HZ, (w + 1) * RAW_CHUNK / RAW_HZ
        for i, st in enumerate(trains):
            k = st[(st > a + 0.002) & (st < b - 0.006)]
            if len(k) == 0:
                continue
            k = np.round((k[:per_window] - a) * RAW_HZ).astype(int)
            acc[i] += hp[k[:, None] + np.arange(-12, 20)].sum(0).T
            shifted[i] += hp[k[:, None] + SHIFT_SAMPLES + np.arange(-12, 20)].sum(0).T
            count[i] += len(k)
    mean = acc / np.maximum(count, 1)[:, None, None]
    mean_shifted = shifted / np.maximum(count, 1)[:, None, None]
    power = np.mean(spectra, axis=0)
    theta = power[(freq >= 6) & (freq <= 10)].sum(0) / power[(freq >= 1) & (freq <= 40)].sum(0)
    return {"sta_amp": mean.max(2) - mean.min(2), "sta_count": count,
            "sta_amp_shifted": mean_shifted.max(2) - mean_shifted.min(2), "theta_ratio": theta,
            "raw_windows": list(map(int, windows))}


def load_sessions(paths: list[str], workers: int = 5, n_windows: int = 12) -> list[dict]:
    urls = asset_urls()
    with ThreadPoolExecutor(workers) as pool:
        return list(pool.map(lambda p: load_session(p, urls[p], n_windows), paths))


def neural_channels(subject: str) -> np.ndarray:
    """Channels of the two probes (0-based): the prefrontal 0-63 and the CA1 probe of the rat."""
    return np.r_[np.arange(N_PFC_CHANNELS), np.array(CA1_CHANNELS[subject])]


def assign_units(s: dict, min_spikes: int = 5) -> pd.DataFrame:
    """One row per unit: rate, refractory violations, best channel, shank, region, multi-unit flag.

    Channel: the neural channel with the largest peak-to-trough amplitude of the mean waveform,
    for units with at least `min_spikes` spikes in the raw windows. A unit with fewer takes the
    shank of its neighbours in the unit order when both neighbours share it (the units are stored
    shank by shank). A unit whose waveform is largest on a non-neural channel and below
    `MAX_AUX_NEURAL_UV` on every probe channel is a cluster of the sensor signals ("sensor").
    Multi-unit: more than `MAX_ISI_VIOLATION` of inter-spike intervals below
    2 ms (`mua`); `first_of_block` is the conversion's ordering rule, shown as a variant.
    """
    rows = []
    for i, st in enumerate(s["trains"]):
        isi = np.diff(st)
        rows.append({"unit": i, "n_spikes": len(st), "rate_hz": len(st) / s["duration"],
                     "isi_lt2ms": float(np.mean(isi < 0.002)) if len(isi) else 0.0})
    u = pd.DataFrame(rows)
    chans = neural_channels(s["subject"])
    amp, count = s["sta_amp"][:, chans], s["sta_count"]
    best = chans[amp.argmax(1)]
    u["sta_spikes"] = count
    u["channel"] = np.where(count >= min_spikes, best, -1)
    u["amp_uv"] = np.where(count >= min_spikes, amp.max(1), np.nan)  # int16 x 1e-6 V: microvolts
    sh = np.where(u.channel >= 0, u.channel // 8, -1)
    for i in np.flatnonzero(sh < 0):
        lo = sh[:i][sh[:i] >= 0]
        hi = sh[i + 1:][sh[i + 1:] >= 0]
        if len(lo) and len(hi) and lo[-1] == hi[0]:
            sh[i] = lo[-1]
    u["shank"] = sh
    u["region"] = np.where(sh < 0, "unassigned", np.where(sh < N_PFC_CHANNELS // 8, "PFC", "CA1"))
    aux = np.setdiff1d(np.arange(s["sta_amp"].shape[1]), chans)
    u["aux_amp_uv"] = s["sta_amp"][:, aux].max(1) if len(aux) else 0.0
    sensor = (s["sta_amp"].argmax(1) >= 0) & np.isin(s["sta_amp"].argmax(1), aux) & (amp.max(1) < MAX_AUX_NEURAL_UV)
    u.loc[sensor & (count > 0), "region"] = "sensor"
    u["first_of_block"] = np.r_[True, sh[1:] != sh[:-1]] & (sh >= 0)
    u["mua"] = u.isi_lt2ms > MAX_ISI_VIOLATION
    u["session"] = s["session"]
    u["subject"] = s["subject"]
    return u


# ---------------------------------------------------------------------------------------------
# Behaviour

def frame_times(s: dict) -> np.ndarray:
    return np.arange(len(s["lin"])) / s["lin_rate"]


def positions_at(s: dict, times: np.ndarray):
    """Normalized position (d - 1, 0 at the end of the nose poke, 1 at the reward) and trial index
    of each time; NaN and -1 outside runs (run_start to run_end) or where d is 0 (no position)."""
    tr = s["trials"]
    times = np.asarray(times, float)
    idx = np.searchsorted(tr.run_start.values, times, side="right") - 1
    ok = (idx >= 0) & (times <= tr.run_end.values[np.clip(idx, 0, None)])
    frame = np.clip(np.round(times * s["lin_rate"]).astype(int), 0, len(s["lin"]) - 1)
    d = s["lin"][frame]
    ok &= d > 0
    return np.where(ok, d - 1, np.nan), np.where(ok, idx, -1)


def sensor_activity(s: dict, channels=None) -> np.ndarray:
    """(samples, 2) absolute deviation from the session median of the (right, left) sensors."""
    right, left = channels or NOSEPOKE_CHANNELS[s["subject"]]
    x = np.stack([s["sensors"][right], s["sensors"][left]], axis=1)
    return np.abs(x - np.median(x, axis=0))


def sensor_check(s: dict, channels=None, shift_s: float = 0.0) -> pd.DataFrame:
    """Per trial, activity of the right and left nose-poke sensors in the nose-poke period and
    in the run. Activity is the mean absolute deviation from the session median of the LFP copy
    of each sensor channel; `shift_s` moves the trial times."""
    dev = sensor_activity(s, channels)
    x = dev
    rows = []
    for k, tr in s["trials"].iterrows():
        a = int((tr.nosepoke_start + shift_s) * s["lfp_rate"])
        b = int((tr.run_start + shift_s) * s["lfp_rate"])
        c = int((tr.run_end + shift_s) * s["lfp_rate"])
        if a < 0 or c > len(x) or b <= a:
            continue
        poke, run = dev[a:b].mean(0), dev[b:c].mean(0)
        rows.append({"trial": k, "side": tr.side, "right_poke": poke[0], "left_poke": poke[1],
                     "right_run": run[0], "left_run": run[1]})
    out = pd.DataFrame(rows)
    out["sensor_side"] = np.where(out.right_poke > out.left_poke, "Right", "Left")
    return out


def sensor_edges(s: dict, window: float = 1.0) -> pd.DataFrame:
    """Mean activity of the trial's own sensor around the start of the first nose poke and the
    end of the last one, each trial scaled to its maximum (the clock check of the trial table
    against the recorded signals)."""
    dev = sensor_activity(s)
    n = int(window * s["lfp_rate"])
    lags = np.arange(-n, n + 1) / s["lfp_rate"]
    on, off = [], []
    for _, tr in s["trials"].iterrows():
        col = 0 if tr.side == "Right" else 1
        for t, store in ((tr.nosepoke_start, on), (tr.run_start, off)):
            k = int(round(t * s["lfp_rate"]))
            if k - n >= 0 and k + n < len(dev):
                seg = dev[k - n:k + n + 1, col]
                store.append(seg / max(seg.max(), 1e-9))
    return pd.DataFrame({"lag_s": lags, "at_poke_start": np.mean(on, 0), "at_poke_end": np.mean(off, 0)})


# ---------------------------------------------------------------------------------------------
# Position-dependent firing

def _gauss(x: np.ndarray, sigma: float = KERNEL_SIGMA) -> np.ndarray:
    """Gaussian kernel of each value (rows) evaluated on GRID (columns)."""
    return np.exp(-0.5 * ((GRID[None, :] - x[:, None]) / sigma) ** 2) / (np.sqrt(2 * np.pi) * sigma)


def trial_densities(pos: np.ndarray, trial: np.ndarray, n_trials: int) -> np.ndarray:
    """(trials, GRID) kernel density of spike positions per trial (unnormalized sums)."""
    out = np.zeros((n_trials, len(GRID)))
    ok = trial >= 0
    if ok.any():
        np.add.at(out, trial[ok], _gauss(pos[ok]))
    return out


def band_test(stats: np.ndarray, alpha: float, two_sided: bool = True, kind: str = "rank"):
    """Pointwise and global bands from resampled statistics, as in the paper's Methods.

    `stats` is (1 + M, G): row 0 the original statistic, the others the resampled ones. The
    global band is the narrowest of a family of pointwise bands within which at least 1 - alpha
    of all 1 + M data sets lie completely. kind="rank": the pointwise bands are the quantiles of
    the resampled values at each point (the Methods' bands). kind="sd": the pointwise bands are
    the resampled mean plus or minus c times their s.d.; used where the rank family cannot reach
    the level (with 1000 surrogates and smooth statistics on 101 points, more than 1% of the data
    sets reach the most extreme rank somewhere, so no one-sided rank band reaches 0.01).
    Returns the positions where the original breaks the global band, and the global band's
    pointwise level (rank) or its c (sd).
    """
    n = stats.shape[0]
    if kind == "sd":
        mu = stats[1:].mean(0)
        sd = stats[1:].std(0)
        sd = np.where(sd > 0, sd, np.inf)
        z = (stats - mu) / sd
        z = np.abs(z) if two_sided else z
        m = np.sort(z.max(axis=1))
        c = m[int(np.ceil((1 - alpha) * n)) - 1]
        return z[0] > c, c
    srt = np.sort(stats, axis=0)
    p_up = np.empty_like(stats)
    p_lo = np.empty_like(stats)
    for g in range(stats.shape[1]):
        p_up[:, g] = (n - np.searchsorted(srt[:, g], stats[:, g], side="left")) / n
        p_lo[:, g] = np.searchsorted(srt[:, g], stats[:, g], side="right") / n
    p = np.minimum(1, 2 * np.minimum(p_up, p_lo)) if two_sided else p_up
    m = np.sort(p.min(axis=1))
    allowed = int(np.floor(alpha * n))
    level = 0.0
    for v in np.unique(m):
        if np.sum(m <= v) <= allowed:
            level = v
        else:
            break
    return p[0] <= level, level


def lr_test(dens: np.ndarray, is_left: np.ndarray, rng, n_perm: int = N_PERM, alpha: float = 0.05,
            kind: str = "rank"):
    """Permutation test of left against right spike-position densities (paper's Methods).

    Returns the positions (GRID) where the difference breaks the global band, and D0(x).
    """
    labels = np.vstack([is_left] + [rng.permutation(is_left) for _ in range(n_perm)]).astype(float)
    nl = labels.sum(1, keepdims=True)
    d = labels @ dens / nl - (1 - labels) @ dens / (len(is_left) - nl)
    sig, _ = band_test(d, alpha, kind=kind)
    return sig, d[0]


def rate_maps(s: dict, units: list[int], n_bins: int = 100) -> dict:
    """Occupancy-normalized rate maps (Hz) by side, smoothed with the paper's kernel (sigma 0.05)."""
    from scipy.ndimage import gaussian_filter1d
    t = frame_times(s)
    pos, trial = positions_at(s, t)
    side = s["trials"].side.values
    edges = np.linspace(0, 1, n_bins + 1)
    occ = {}
    for sd in ("Left", "Right"):
        m = (trial >= 0) & (side[np.clip(trial, 0, None)] == sd)
        occ[sd] = gaussian_filter1d(np.histogram(pos[m], edges)[0] / s["lin_rate"], KERNEL_SIGMA * n_bins,
                                    mode="nearest")
    maps = {}
    for u in units:
        p, tr = positions_at(s, s["trains"][u])
        maps[u] = {}
        for sd in ("Left", "Right"):
            m = (tr >= 0) & (side[np.clip(tr, 0, None)] == sd)
            c = gaussian_filter1d(np.histogram(p[m], edges)[0].astype(float), KERNEL_SIGMA * n_bins, mode="nearest")
            maps[u][sd] = c / np.maximum(occ[sd], 1e-9)
    return maps


def field_size(rate: np.ndarray, contiguous: bool = True) -> float:
    """Length (normalized) where the rate is at least half its peak: the contiguous run around the
    peak, or (contiguous=False) all bins."""
    above = rate >= 0.5 * rate.max()
    if not contiguous:
        return float(above.mean())
    k = int(rate.argmax())
    lo, hi = k, k
    while lo > 0 and above[lo - 1]:
        lo -= 1
    while hi < len(rate) - 1 and above[hi + 1]:
        hi += 1
    return (hi - lo + 1) / len(rate)


def active_fraction(s: dict, units: list[int], window: float = 0.1) -> pd.DataFrame:
    """For every 100 ms window inside a run: fraction of `units` firing at least one spike, and
    the window's position (at its centre)."""
    rows = []
    trains = [s["trains"][u] for u in units]
    for k, tr in s["trials"].iterrows():
        edges = np.arange(tr.run_start, tr.run_end - window / 2, window)
        if len(edges) < 2:
            continue
        edges = np.r_[edges, edges[-1] + window]
        active = np.zeros(len(edges) - 1)
        for st in trains:
            active += np.histogram(st, edges)[0] > 0
        pos, _ = positions_at(s, edges[:-1] + window / 2)
        rows.append(pd.DataFrame({"trial": k, "side": tr.side, "pos": pos, "fraction": active / len(units)}))
    return pd.concat(rows, ignore_index=True)


def decode_side(s: dict, units: list[int], offsets: np.ndarray, width: float = 1.0) -> pd.DataFrame:
    """Leave-one-out nearest-centroid decoding of the trial side from spike counts in windows of
    `width` s starting at run_start + offset (z-scored per unit). No random numbers."""
    tr = s["trials"]
    y = (tr.side.values == "Left").astype(int)
    rows = []
    for off in offsets:
        a = tr.run_start.values + off
        X = np.array([[np.searchsorted(s["trains"][u], b + width) - np.searchsorted(s["trains"][u], b)
                       for u in units] for b in a], float)
        sd = X.std(0)
        X = (X[:, sd > 0] - X[:, sd > 0].mean(0)) / sd[sd > 0]
        correct = 0
        for i in range(len(y)):
            keep = np.arange(len(y)) != i
            c0 = X[keep & (y == 0)].mean(0)
            c1 = X[keep & (y == 1)].mean(0)
            pred = int(np.sum((X[i] - c1) ** 2) < np.sum((X[i] - c0) ** 2))
            correct += pred == y[i]
        rows.append({"offset_s": off, "accuracy": correct / len(y), "n_trials": len(y)})
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------------------------
# Monosynaptic interactions

CCG_EDGES_MS = np.arange(-5, 6)          # 10 bins of 1 ms from -5 to 5 ms
TEST_BINS = [6, 7, 8]                    # [1,2), [2,3), [3,4) ms: lags of b after a
TEST_BINS_REVERSE = [3, 2, 1]            # the same lags for the other direction


def near_lags(a: np.ndarray, b: np.ndarray, max_lag: float):
    """All lags b_j - a_i with |lag| <= max_lag, with the indices i and j."""
    lo = np.searchsorted(b, a - max_lag, side="left")
    hi = np.searchsorted(b, a + max_lag, side="right")
    n = hi - lo
    i = np.repeat(np.arange(len(a)), n)
    start = np.repeat(np.cumsum(n) - n, n)
    j = np.arange(n.sum()) - start + np.repeat(lo, n)
    return b[j] - a[i], i, j


def ccg_counts(lags_s: np.ndarray) -> np.ndarray:
    return np.histogram(lags_s * 1000, CCG_EDGES_MS)[0]


def _tri_cdf(x_ms: np.ndarray) -> np.ndarray:
    """CDF of the difference of two independent uniform jitters on [-5, 5] ms."""
    x = np.clip(x_ms, -10, 10)
    return np.where(x <= 0, (x + 10) ** 2 / 200, 1 - (10 - x) ** 2 / 200)


def jitter_expectation(lags_s: np.ndarray) -> np.ndarray:
    """Expected CCG counts when both spike trains are jittered uniformly by +-5 ms (exact mean)."""
    d = lags_s * 1000
    lo, hi = CCG_EDGES_MS[:-1], CCG_EDGES_MS[1:]
    return (_tri_cdf(hi[None, :] - d[:, None]) - _tri_cdf(lo[None, :] - d[:, None])).sum(0)


def jitter_ccgs(lags_s, i, j, rng, n_jitter: int = N_JITTER, chunk: int = 100) -> np.ndarray:
    """CCG counts of `n_jitter` surrogates in which every spike of both trains is jittered
    independently and uniformly by +-5 ms (paper's Methods). Only spike pairs within 15 ms can
    reach the +-5 ms window, so only those are jittered."""
    ui, ii = np.unique(i, return_inverse=True)
    uj, jj = np.unique(j, return_inverse=True)
    out = np.zeros((n_jitter, len(CCG_EDGES_MS) - 1), int)
    for c0 in range(0, n_jitter, chunk):
        c = min(chunk, n_jitter - c0)
        ea = rng.uniform(-JITTER_S, JITTER_S, (c, len(ui)))
        eb = rng.uniform(-JITTER_S, JITTER_S, (c, len(uj)))
        lag = (lags_s[None, :] + eb[:, jj] - ea[:, ii]) * 1000
        k = np.floor(lag - CCG_EDGES_MS[0]).astype(int)
        ok = (k >= 0) & (k < len(CCG_EDGES_MS) - 1)
        rows = np.broadcast_to(np.arange(c)[:, None], lag.shape)
        out[c0:c0 + c] = np.bincount((rows[ok] * (len(CCG_EDGES_MS) - 1) + k[ok]),
                                     minlength=c * (len(CCG_EDGES_MS) - 1)).reshape(c, -1)
    return out


def _direction_result(ccg, upper, lower, test_bins):
    exc_bins = [b for b in test_bins if ccg[b] > upper]
    inh_bins = [b for b in test_bins if ccg[b] < lower]
    width = 0
    if exc_bins:   # width of the run of bins above the global band that holds a test bin
        b = exc_bins[0]
        lo, hi = b, b
        while lo > 0 and ccg[lo - 1] > upper:
            lo -= 1
        while hi < len(ccg) - 1 and ccg[hi + 1] > upper:
            hi += 1
        width = hi - lo + 1
    return bool(exc_bins), width, bool(inh_bins)


def connections(s: dict, units: list[int], rng, screen_p: float = 0.01, check_sample: int = 0) -> pd.DataFrame:
    """Jitter test of every ordered pair of `units` (paper's Methods).

    For each pair the exact jitter mean gives a Poisson screen (any test bin beyond the pointwise
    `screen_p` quantile in either direction); screened pairs get the Monte Carlo test with
    N_JITTER surrogates: global bands at 99% from the maximum and minimum of each surrogate over
    the +-5 ms window, excitatory when a bin from 1 to 4 ms is above the upper band, inhibitory
    when below the lower band. `check_sample` unscreened pairs also get the Monte Carlo test, to
    show that the screen misses nothing.
    """
    from scipy.stats import poisson
    rows = []
    unscreened = []
    for x in range(len(units)):
        for y in range(x + 1, len(units)):
            a, b = s["trains"][units[x]], s["trains"][units[y]]
            lags, i, j = near_lags(a, b, 0.0155)
            ccg = ccg_counts(lags)
            mu = jitter_expectation(lags)
            hi_q = poisson.ppf(1 - screen_p, mu)
            lo_q = poisson.ppf(screen_p, mu)
            cand = bool(np.any(ccg[TEST_BINS] > hi_q[TEST_BINS]) or np.any(ccg[TEST_BINS] < lo_q[TEST_BINS])
                        or np.any(ccg[TEST_BINS_REVERSE] > hi_q[TEST_BINS_REVERSE])
                        or np.any(ccg[TEST_BINS_REVERSE] < lo_q[TEST_BINS_REVERSE]))
            base = {"a": units[x], "b": units[y], "n_near": len(lags), "screened": cand}
            if not cand:
                unscreened.append((x, y))
                rows.append(base)
                continue
            rows.append({**base, **_mc_pair(lags, i, j, ccg, rng)})
    if check_sample and unscreened:
        pick = rng.choice(len(unscreened), min(check_sample, len(unscreened)), replace=False)
        for k in pick:
            x, y = unscreened[k]
            a, b = s["trains"][units[x]], s["trains"][units[y]]
            lags, i, j = near_lags(a, b, 0.0155)
            r = _mc_pair(lags, i, j, ccg_counts(lags), rng)
            rows.append({"a": units[x], "b": units[y], "n_near": len(lags), "screened": False,
                         "check": True, **r})
    out = pd.DataFrame(rows)
    out["check"] = out.get("check", False)
    out["check"] = out["check"].fillna(False).astype(bool)
    return out


def _mc_pair(lags, i, j, ccg, rng) -> dict:
    sur = jitter_ccgs(lags, i, j, rng)
    upper = np.quantile(sur.max(1), 0.99)
    lower = np.quantile(sur.min(1), 0.01)
    ab = _direction_result(ccg, upper, lower, TEST_BINS)
    ba = _direction_result(ccg, upper, lower, TEST_BINS_REVERSE)
    return {"upper": upper, "lower": lower,
            "exc_ab": ab[0], "width_ab": ab[1], "inh_ab": ab[2],
            "exc_ba": ba[0], "width_ba": ba[1], "inh_ba": ba[2]}


def directed(conn: pd.DataFrame, max_width: int = 2) -> pd.DataFrame:
    """One row per ordered pair (pre, post), with exc (narrow peak) and inh (trough) flags."""
    c = conn[~conn.check]
    ab = pd.DataFrame({"pre": c.a, "post": c.b, "exc_any": c.get("exc_ab", False), "width": c.get("width_ab", 0),
                       "inh": c.get("inh_ab", False)})
    ba = pd.DataFrame({"pre": c.b, "post": c.a, "exc_any": c.get("exc_ba", False), "width": c.get("width_ba", 0),
                       "inh": c.get("inh_ba", False)})
    d = pd.concat([ab, ba], ignore_index=True)
    d[["exc_any", "inh"]] = d[["exc_any", "inh"]].fillna(False).astype(bool)
    d["width"] = d.width.fillna(0)
    d["exc"] = d.exc_any & (d.width <= max_width)
    d["inh"] = d.inh & ~d.exc_any      # a trough beside a peak is not counted as inhibition
    return d


def coincidence_test(s: dict, pre: int, post: int, rng, trials_mask: np.ndarray | None = None,
                     n_jitter: int = N_JITTER, alpha: float = 0.01, kinds=("sd", "rank")) -> dict:
    """Position dependence of excess coincidences (post 1 to 4 ms after pre), paper's Methods.

    Coincidence rate along the track: kernel density (sigma 0.05) of the positions of coincident
    events (taken at the presynaptic spike). Surrogates jitter both trains by +-5 ms; the
    positions of the events are kept at the original presynaptic spike (a 5 ms shift moves the rat
    by well under 1% of the track). One-sided global band at `alpha`, of each kind of band_test.
    """
    a, b = s["trains"][pre], s["trains"][post]
    pos, trial = positions_at(s, a)
    keep = trial >= 0
    if trials_mask is not None:
        keep &= trials_mask[np.clip(trial, 0, None)]
    ia = np.flatnonzero(keep)
    lags, i, j = near_lags(a[ia], b, 0.0145)
    events = _gauss(pos[ia][i])                       # (K, G)
    obs = ((lags >= 0.001) & (lags <= 0.004)).astype(float)
    ui, ii = np.unique(i, return_inverse=True)
    uj, jj = np.unique(j, return_inverse=True)
    stats = np.zeros((n_jitter + 1, len(GRID)))
    stats[0] = obs @ events
    for c0 in range(0, n_jitter, 100):
        c = min(100, n_jitter - c0)
        ea = rng.uniform(-JITTER_S, JITTER_S, (c, len(ui)))
        eb = rng.uniform(-JITTER_S, JITTER_S, (c, len(uj)))
        lag = lags[None, :] + eb[:, jj] - ea[:, ii]
        stats[1 + c0:1 + c0 + c] = ((lag >= 0.001) & (lag <= 0.004)).astype(float) @ events
    out = {"n_coincidences": int(obs.sum())}
    for kind in kinds:
        sig, level = band_test(stats, alpha, two_sided=False, kind=kind)
        out.update({f"{kind}_sig": bool(sig.any()), f"{kind}_fraction": float(sig.mean()), f"{kind}_level": level})
    return out


def transmission(a: np.ndarray, b: np.ndarray, which: np.ndarray) -> np.ndarray:
    """Per presynaptic spike in `which`: post spikes 1 to 4 ms after it, minus the expectation
    when the post spikes are jittered uniformly by +-5 ms. The mean over a set of spikes is the
    excess transmission per presynaptic spike."""
    lags, i, j = near_lags(a[which], b, 0.0095)
    d = lags * 1000
    obs = ((d >= 1) & (d <= 4)).astype(float)
    exp = (np.clip(np.minimum(d + 5, 4) - np.maximum(d - 5, 1), 0, None)) / 10
    out = np.zeros(len(which))
    np.add.at(out, i, obs - exp)
    return out


def first_vs_later(a: np.ndarray, b: np.ndarray, rng, n_perm: int = 1000) -> dict:
    """Excess transmission of first spikes (after >= 200 ms of silence) against later spikes
    (< 40 ms after the previous spike), with a permutation test of the labels (two-sided)."""
    isi = np.diff(a, prepend=-np.inf)
    first = np.flatnonzero(isi >= 0.2)
    later = np.flatnonzero(isi < 0.04)
    if len(first) == 0 or len(later) == 0:
        return {"n_first": len(first), "n_later": len(later)}
    v = transmission(a, b, np.r_[first, later])
    lab = np.r_[np.ones(len(first), bool), np.zeros(len(later), bool)]
    diff0 = v[lab].mean() - v[~lab].mean()
    null = np.empty(n_perm)
    for k in range(n_perm):
        p = rng.permutation(lab)
        null[k] = v[p].mean() - v[~p].mean()
    p_two = min(1.0, 2 * min((np.sum(null >= diff0) + 1) / (n_perm + 1), (np.sum(null <= diff0) + 1) / (n_perm + 1)))
    return {"n_first": len(first), "n_later": len(later), "eff_first": v[lab].mean(),
            "eff_later": v[~lab].mean(), "diff": diff0, "p": p_two}


def coincidence_gain(pres: list[np.ndarray], post: np.ndarray, duration: float, window: float = 0.005) -> pd.DataFrame:
    """Transmission by the number of distinct presynaptic partners firing together.

    Spikes of all partners are merged; an event starts at a spike and takes every partner spike
    within `window` after it (events do not overlap). For each event, whether the post unit fires
    1 to 4 ms after the event's last spike. Excess = that probability minus the chance of a post
    spike in any 3 ms window (rate x 3 ms, Poisson).
    """
    t = np.concatenate(pres)
    who = np.concatenate([np.full(len(p), k) for k, p in enumerate(pres)])
    o = np.argsort(t, kind="stable")
    t, who = t[o], who[o]
    rows = []
    k = 0
    n = len(t)
    while k < n:
        e = np.searchsorted(t, t[k] + window, side="right")
        rows.append((t[e - 1], len(np.unique(who[k:e]))))
        k = e
    ev = np.array(rows)
    last, n_part = ev[:, 0], ev[:, 1].astype(int)
    hit = (np.searchsorted(post, last + 0.004, side="right") - np.searchsorted(post, last + 0.001, side="left")) > 0
    p0 = 1 - np.exp(-len(post) / duration * 0.003)
    out = pd.DataFrame({"n_partners": n_part, "hit": hit})
    g = out.groupby("n_partners").hit.agg(["mean", "size"]).rename(columns={"mean": "p_hit", "size": "events"})
    g["excess"] = g.p_hit - p0
    return g.reset_index()
