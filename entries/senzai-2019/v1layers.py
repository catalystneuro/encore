"""Loading and unit measures for dandiset 000166 (Senzai, Fernandez-Ruiz and Buzsaki 2019).

Data are streamed from the DANDI Archive at the pinned version; nothing is written to disk.

Where each parameter comes from:

- Waveform classes (`waveform_features`, `classify_waveforms`): STAR Methods, "Classification of
  units based on spike waveforms" (sign of the largest amplitude, kurtosis of the second derivative
  of the normalized waveform beyond 5 SD of the mean as putative fibers, trough-to-peak latency
  above 0.55 ms as E, at most 0.55 ms as I). The Results (Assignment of Neurons to Physiologically
  Defined Layers, paragraph 1) say "the unfiltered waveform was quantified", so the main reading
  uses the wide-band signal; a 300 Hz high-pass (the Kilosort `ops.fshigh 300` of the STAR Methods,
  Spike sorting) is a variant. The dataset holds no waveforms, so they are averaged from the raw
  signal in `WAVEFORM_BLOCKS` (an assumption about how many spikes are needed: two 30 s blocks;
  the paper used all spikes). The snippet span (-1.5 to +2 ms) and the baseline (first 0.25 ms of
  the snippet) are standard choices that do not move a trough-to-peak latency.
- Monosynaptic detection (`detect_connections`): STAR Methods, "Detection of monosynaptic
  functional connectiveties": 0.5 ms bins, a Gaussian of 7 ms SD as the baseline predictor, the
  99.9999th percentile of the Poisson distribution at the predicted rate (and the 0.0001th for
  troughs, as the claims file reads "negative deviations"), at least two consecutive bins within
  +1.5 to +4 ms. The CCG half width, 50 ms, is the claims file's standard choice. Whether the
  Gaussian is hollowed is open (claims file); `hollow=0.6` is the buzcode `bz_cch_conv` variant.
  The kernel is cut at 5 SD and the CCG edges are padded by reflection, standard choices that do not
  reach the tested bins.
- Spike transmission probability (`transmission`): excess count over the predictor in +1.5 to +4 ms
  divided by the presynaptic spike count (English et al. 2017, as the claims file gives it).
- Opto tagging (`opto_tagged`): STAR Methods, "Optogenetic tagging of PV cells and VGAT cells":
  1 ms bins, the mean of the two largest bins in 1 to 6 ms after pulse onset above the mean plus
  8 SD of the -100 to 0 ms baseline bins.
- Brain states are the dataset's `Sleep states` intervals; waking is the label `Awake` (micro-arousals,
  `MA`, are kept apart), an assumption: the paper's state scoring (SleepScoreMaster) labels
  waking, non-REM and REM, and the dataset adds MA.
"""

import numpy as np
import h5py
import remfile
import requests
from numba import njit
from scipy import signal, stats

DANDISET_ID = "000166"
VERSION = "0.250624.0434"
API = "https://api.dandiarchive.org/api"

RAW_RATE = 20000.0
WAVEFORM_BLOCKS = ((1000.0, 30.0), (3000.0, 30.0))   # (start s, duration s) of raw signal averaged
SNIPPET = (-30, 40)                                  # samples around each spike, -1.5 to +2 ms
MIN_WAVEFORM_SPIKES = 10
MUA_BAND = (500.0, 5000.0)                           # landmark c, STAR Methods, Depth normalization
SITE_UM = 20.0                                       # site spacing, STAR Methods (H3 probe)
LANDMARK_BLOCK = 1000.0                              # s of LFP read around DOWN-UP transitions
CSD_WINDOWS = ((0.0, 0.1), (0.0, 0.05))              # readings of the claims file (fig1f-sink-b-deeper)

CCG_BIN = 0.0005
CCG_HALF = 0.05
NBINS = int(round(2 * CCG_HALF / CCG_BIN)) + 1       # 201 bins, centred on lags -50 ... +50 ms
LAGS = (np.arange(NBINS) - NBINS // 2) * CCG_BIN
SYN_WINDOW = (0.0015, 0.004)
GAUSS_SD = 0.007
P_HIGH = 0.999999
P_LOW = 0.000001

STATE_CODES = {"Awake": 1, "Non-REM": 2}             # states CCGs are split by; others are 0


def _dec(a):
    return [x.decode() if isinstance(x, bytes) else x for x in a]


def list_assets():
    """Assets of the pinned version, sorted by path."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{VERSION}/assets/?page_size=200"
    out = requests.get(url, timeout=60).json()["results"]
    return sorted(out, key=lambda a: a["path"])


def version_info():
    return requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{VERSION}/info/", timeout=60).json()


def open_asset(asset_id):
    r = requests.get(f"{API}/assets/{asset_id}/download/", allow_redirects=False, timeout=60)
    return h5py.File(remfile.File(r.headers["Location"]), "r")


def _intervals(f, name):
    path = f"processing/Neural states/{name}"
    if path not in f:
        return None
    g = f[path]
    out = {"start": g["start_time"][:], "stop": g["stop_time"][:]}
    if "label" in g:
        out["label"] = np.array(_dec(g["label"][:]))
    if "amplitude" in g:
        out["amplitude"] = np.asarray(g["amplitude"][:])
    return out


def load_session(asset):
    """Everything the analysis uses from one file: units, spike trains, intervals, file shapes."""
    f = open_asset(asset["asset_id"])
    u = f["units"]
    idx = u["spike_times_index"][:]
    st = u["spike_times"][:]
    trains = np.split(st, idx[:-1])
    cols = _dec(u.attrs["colnames"])
    n = len(idx)

    def col(name, default):
        return np.array(_dec(u[name][:])) if name in u else np.array([default] * n)

    s = {
        "path": asset["path"],
        "subject": f["general/subject/subject_id"][()].decode(),
        "genotype": f["general/subject/genotype"][()].decode(),
        "session_id": f["general/session_id"][()].decode(),
        "unit_ids": u["id"][:],
        "columns": cols,
        "trains": trains,
        "cell_type": col("cell_type", "missing"),
        "synaptic_effect": col("synaptic_effect", "missing"),
        "quality": col("quality", "missing"),
        "max_channel": u["max_channel"][:] if "max_channel" in u else np.full(n, -1),
        "states": _intervals(f, "Sleep states"),
        "updown": _intervals(f, "Up-Down states"),
        "laser": _intervals(f, "Laser diode"),
        "visual": _intervals(f, "Visual laser"),
        "raw_shape": f["acquisition/ElectricalSeries/data"].shape,
        "raw_rate": float(f["acquisition/ElectricalSeries/starting_time"].attrs["rate"]),
        "raw_conversion": float(f["acquisition/ElectricalSeries/data"].attrs["conversion"]),
        "lfp_shape": f["processing/ecephys/LFP/LFP/data"].shape,
        "lfp_rate": float(f["processing/ecephys/LFP/LFP/starting_time"].attrs["rate"]),
        "rel_y": f["general/extracellular_ephys/electrodes/rel_y"][:],
        "electrode_id": f["general/extracellular_ephys/electrodes/id"][:],
        "series_electrodes": f["acquisition/ElectricalSeries/electrodes"][:],
        "electrode_y": f["general/extracellular_ephys/electrodes/y"][:],
        "electrode_location": np.array(_dec(f["general/extracellular_ephys/electrodes/location"][:])),
        "electrode_imp": f["general/extracellular_ephys/electrodes/imp"][:],
    }
    s["duration"] = s["raw_shape"][0] / s["raw_rate"]
    s["groups"] = sorted(f"{top}/{k}" for top in ("acquisition", "processing", "intervals", "stimulus", "analysis")
                         if top in f for k in f[top])
    s["groups"] += sorted(f"{top}/{k}/{j}" for top in ("processing", "stimulus") if top in f
                          for k in f[top] for j in f[top][k])
    s["_file"] = f
    return s


# --- waveforms ------------------------------------------------------------------------------

def mean_waveforms(s, highpass=None):
    """Mean wide-band (or high-passed) waveform of each unit on all 64 sites, from WAVEFORM_BLOCKS.

    Returns (waveforms [unit, sample, site] in uV, spike counts used)."""
    raw = s["_file"]["acquisition/ElectricalSeries/data"]
    n = len(s["trains"])
    lo, hi = SNIPPET
    acc = {hp: np.zeros((n, hi - lo, raw.shape[1])) for hp in (None, 300.0)}
    counts = np.zeros(n, int)
    sos = signal.butter(3, 300.0, btype="high", fs=RAW_RATE, output="sos")
    sos_mua = signal.butter(3, MUA_BAND, btype="band", fs=RAW_RATE, output="sos")
    mua = np.zeros(raw.shape[1])
    for t0, dur in WAVEFORM_BLOCKS:
        i0 = int(t0 * RAW_RATE)
        i1 = min(i0 + int(dur * RAW_RATE), raw.shape[0])
        if i1 - i0 < RAW_RATE:
            continue
        block = raw[i0:i1, :].astype(np.float32) * s["raw_conversion"] * 1e6
        filt = signal.sosfiltfilt(sos, block, axis=0).astype(np.float32)
        mua += (signal.sosfiltfilt(sos_mua, block, axis=0) ** 2).mean(axis=0)
        for k, tr in enumerate(s["trains"]):
            si = np.round(tr[(tr >= t0) & (tr < t0 + dur)] * RAW_RATE).astype(np.int64) - i0
            si = si[(si + lo >= 0) & (si + hi <= i1 - i0)]
            if len(si) == 0:
                continue
            win = si[:, None] + np.arange(lo, hi)[None, :]
            for hp, x in ((None, block), (300.0, filt)):
                snip = x[win]                                   # spikes x samples x sites
                snip = snip - snip[:, :5, :].mean(axis=1, keepdims=True)
                acc[hp][k] += snip.sum(axis=0)
            counts[k] += len(si)
    with np.errstate(invalid="ignore"):
        out = {hp: acc[hp] / counts[:, None, None] for hp in acc}
    out["mua_power"] = mua
    return out, counts


def waveform_features(w):
    """Sign, trough-to-peak latency (ms), kurtosis of the second derivative and peak site of one
    mean waveform [sample, site]."""
    amp = w.max(axis=0) - w.min(axis=0)
    site = int(np.argmax(amp))
    x = w[:, site]
    i_min, i_max = int(np.argmin(x)), int(np.argmax(x))
    negative = abs(x[i_min]) >= abs(x[i_max])
    if negative:
        after = x[i_min:]
        tp = np.argmax(after) / RAW_RATE * 1e3
    else:
        tp = np.nan
    xn = x / np.max(np.abs(x))
    kurt = stats.kurtosis(np.diff(xn, 2))
    return {"negative": negative, "tp_ms": tp, "kurtosis": kurt, "site": site, "amp_uv": amp[site]}


def classify_waveforms(features, tp_threshold=0.55, kurt_sd=5.0):
    """'E', 'I', 'positive', 'fiber' or 'unclassified' (too few spikes) for each unit (STAR Methods)."""
    neg = np.array([f is not None and f["negative"] for f in features])
    kurt = np.array([f["kurtosis"] if f is not None else np.nan for f in features])
    k = kurt[neg]
    mu, sd = np.nanmean(k), np.nanstd(k)
    out = []
    for f, kv in zip(features, kurt):
        if f is None:
            out.append("unclassified")
        elif not f["negative"]:
            out.append("positive")
        elif abs(kv - mu) > kurt_sd * sd:
            out.append("fiber")
        elif f["tp_ms"] > tp_threshold:
            out.append("E")
        else:
            out.append("I")
    return np.array(out)


# --- LFP landmarks ----------------------------------------------------------------------------

def downup_csd(s, pre=0.2, post=0.3):
    """Average LFP and CSD (second spatial difference, sinks negative) around DOWN-UP transitions.

    Transitions are UP onsets that start where a DOWN interval ends, in the LANDMARK_BLOCK seconds of
    the session holding the most of them (a reduction for speed, standard choice)."""
    ud = s["updown"]
    if ud is None:
        return None
    up = ud["label"] == "UP"
    down_stop = ud["stop"][~up]
    onsets = ud["start"][up]
    onsets = onsets[np.isin(np.round(onsets, 4), np.round(down_stop, 4))]
    if len(onsets) == 0:
        return None
    edges = np.arange(0, s["duration"] + LANDMARK_BLOCK / 4, LANDMARK_BLOCK / 4)
    h = np.histogram(onsets, edges)[0]
    win = np.convolve(h, np.ones(4), mode="valid")
    t0 = edges[int(np.argmax(win))]
    rate = s["lfp_rate"]
    L = s["_file"]["processing/ecephys/LFP/LFP/data"]
    i0 = int(t0 * rate)
    i1 = min(i0 + int(LANDMARK_BLOCK * rate), L.shape[0])
    x = L[i0:i1, :].astype(np.float32) * s["raw_conversion"] * 1e6
    on = onsets[(onsets >= t0 + pre) & (onsets < t0 + (i1 - i0) / rate - post)]
    idx = np.round((on - t0) * rate).astype(int)
    lags = np.arange(-int(pre * rate), int(post * rate))
    avg = x[idx[:, None] + lags[None, :]].mean(axis=0)            # time x site
    # the same average with the onsets shifted by 10 s, a null for the clock check
    sh = idx + int(10 * rate)
    sh = sh[sh + lags[-1] < x.shape[0]]
    avg_shift = x[sh[:, None] + lags[None, :]].mean(axis=0)
    csd = csd_of(avg)                                              # sites 1 ... 62
    hp = signal.sosfiltfilt(signal.butter(3, [100, 500], btype="band", fs=rate, output="sos"),
                            x[: int(200 * rate)], axis=0)
    cc = np.corrcoef(hp.T)
    return {"t0": t0, "n": len(on), "lags": lags / rate, "lfp": avg, "lfp_shifted": avg_shift, "csd": csd,
            "neighbour_corr": cc}


def csd_of(lfp, step=1):
    """Second spatial difference over +-step sites, sinks negative; column k is site k + step."""
    return -(lfp[:, :-2 * step] - 2 * lfp[:, step:-step] + lfp[:, 2 * step:]) / step ** 2


def landmarks(csd, lags, mua_power, window, step=1):
    """Sites of landmarks a to e. c is the peak of MUA power; b the most negative CSD above c and d
    below it; a the most positive CSD above b and e below d; extremes taken over time in the window.
    CSD column k is site k + step. Site 0 is taken as the most superficial (the files' rel_y runs
    from -1 at site 0 to -64 at site 63)."""
    m = (lags >= window[0]) & (lags < window[1])
    sink = csd[m].min(axis=0)
    source = csd[m].max(axis=0)
    sites = np.arange(step, csd.shape[1] + step)
    c = int(np.argmax(mua_power))
    out = {"c": c}
    above, below = sites < c, sites > c
    if above.sum() == 0 or below.sum() == 0:
        return None
    out["b"] = int(sites[above][np.argmin(sink[above])])
    out["d"] = int(sites[below][np.argmin(sink[below])])
    a_m, e_m = sites < out["b"], sites > out["d"]
    if a_m.sum() == 0 or e_m.sum() == 0:
        return None
    out["a"] = int(sites[a_m][np.argmax(source[a_m])])
    out["e"] = int(sites[e_m][np.argmax(source[e_m])])
    return out


# --- spike-LFP phase coupling in waking (figs7) ---------------------------------------------

COUPLING_FREQS = np.logspace(np.log10(0.5), np.log10(100.0), 25)   # claims file: 0.5 to 100 Hz, log spaced
COUPLING_WAKE_MAX = 600.0      # s of waking LFP used per session (longest Awake epochs; reduction, standard)
COUPLING_MIN_EPOCH = 30.0      # s; shorter Awake epochs are not used
COUPLING_EDGE = 8.0            # s at each epoch edge where spikes are not used (beyond the +-4 SD of the 0.5 Hz wavelet, 7.6 s)
COUPLING_DECIMATE = 4          # LFP decimated to 312.5 Hz before the wavelet (above 2 x 100 Hz)
COUPLING_DISTANT = 10          # sites (200 um) between a unit and the LFP of reading 2 (standard choice)
MORLET_W0 = 6.0                # Torrence and Compo (1998), cited by the STAR Methods


def morlet_phase(x, fs, freqs, w0=MORLET_W0):
    """Phase [freq, sample] of the complex Morlet wavelet transform of x."""
    out = np.empty((len(freqs), len(x)))
    for i, f in enumerate(freqs):
        sd = w0 / (2 * np.pi * f)
        t = np.arange(-4 * sd, 4 * sd + 1 / fs, 1 / fs)
        k = np.exp(2j * np.pi * f * t) * np.exp(-t ** 2 / (2 * sd ** 2))
        out[i] = np.angle(signal.fftconvolve(x, k[::-1].conj(), mode="same"))
    return out


def spike_lfp_coupling(s, unit_sites, n_sites=64):
    """Mean resultant length and Rayleigh p of each unit's spike phases at COUPLING_FREQS in waking,
    on the LFP of the unit's own peak site (reading 1) and of the site COUPLING_DISTANT sites away,
    towards the longer side of the probe (reading 2, which keeps the unit's own spike out of the LFP)."""
    st = s["states"]
    if st is None:
        return None
    a, b = state_blocks(st, "Awake", COUPLING_WAKE_MAX)
    rate = s["lfp_rate"]
    fs = rate / COUPLING_DECIMATE
    L = s["_file"]["processing/ecephys/LFP/LFP/data"]
    n = len(s["trains"])
    unit_sites = np.asarray(unit_sites)
    distant = np.where(unit_sites < n_sites / 2, unit_sites + COUPLING_DISTANT, unit_sites - COUPLING_DISTANT)
    distant[unit_sites < 0] = -1
    use = {"own": unit_sites, "distant": distant}
    sites = sorted({int(x) for x in np.concatenate([unit_sites, distant]) if x >= 0})
    nf = len(COUPLING_FREQS)
    sums = {r: np.zeros((n, nf), complex) for r in use}
    counts = np.zeros(n, int)
    for t0, t1 in zip(a, b):
        i0, i1 = int(t0 * rate), int(t1 * rate)
        x = L[i0:i1, :][:, sites].astype(float)
        x = signal.decimate(x, COUPLING_DECIMATE, axis=0, zero_phase=True)
        idx = {}
        for k, tr in enumerate(s["trains"]):
            sp = tr[(tr >= t0 + COUPLING_EDGE) & (tr < t1 - COUPLING_EDGE)]
            idx[k] = np.minimum(np.round((sp - t0) * fs).astype(int), x.shape[0] - 1)
            if unit_sites[k] >= 0:
                counts[k] += len(sp)
        for j, site in enumerate(sites):
            ph = morlet_phase(x[:, j], fs, COUPLING_FREQS)
            for r, ref in use.items():
                for k in np.where(ref == site)[0]:
                    sums[r][k] += np.exp(1j * ph[:, idx[k]]).sum(axis=1)
    out = {"n_spikes": counts, "seconds": float((b - a).sum()), "sites": unit_sites, "distant": distant}
    for r in sums:
        with np.errstate(invalid="ignore", divide="ignore"):
            mrl = np.abs(sums[r]) / counts[:, None]
            nn = counts[:, None].astype(float)
            rn = nn * mrl                     # Rayleigh test, Zar (1999) approximation
            p = np.exp(np.sqrt(1 + 4 * nn + 4 * (nn ** 2 - rn ** 2)) - (1 + 2 * nn))
        out[f"mrl_{r}"] = mrl
        out[f"p_{r}"] = np.minimum(p, 1.0)
    return out


# --- cross-correlograms -------------------------------------------------------------------

@njit(cache=True)
def _ccg_counts(t, u, state, n_units, nbins, binsize, half):
    out = np.zeros((3, n_units, n_units, nbins), np.int32)
    mid = nbins // 2
    n = t.shape[0]
    for i in range(n):
        ti = t[i]
        ui = u[i]
        j = i + 1
        while j < n:
            d = t[j] - ti
            if d > half:
                break
            b = int(np.floor(d / binsize + 0.5))
            if b <= mid:
                uj = u[j]
                # spike j of unit uj at lag +d after spike i of unit ui (reference ui), and the reverse
                out[0, ui, uj, mid + b] += 1
                out[0, uj, ui, mid - b] += 1
                si = state[i]
                if si > 0:
                    out[si, ui, uj, mid + b] += 1
                sj = state[j]
                if sj > 0:
                    out[sj, uj, ui, mid - b] += 1
            j += 1
    return out


def state_of(times, states):
    """Code of the brain state (STATE_CODES) at each time; 0 outside them or when absent."""
    code = np.zeros(len(times), np.int8)
    if states is None:
        return code
    for lab, c in STATE_CODES.items():
        m = states["label"] == lab
        for a, b in zip(states["start"][m], states["stop"][m]):
            i0, i1 = np.searchsorted(times, [a, b])
            code[i0:i1] = c
    return code


def ccgs(s):
    """CCG counts [state (all, Awake, Non-REM), reference, target, lag] for all unit pairs.

    The state is that of the reference spike. Also returns spike counts per unit and state."""
    t = np.concatenate(s["trains"])
    u = np.concatenate([np.full(len(tr), k, np.int32) for k, tr in enumerate(s["trains"])])
    order = np.argsort(t, kind="stable")
    t, u = t[order], u[order]
    st = state_of(t, s["states"])
    n = len(s["trains"])
    c = _ccg_counts(t, u, st, n, NBINS, CCG_BIN, CCG_HALF)
    nspk = np.zeros((3, n), np.int64)
    nspk[0] = np.bincount(u, minlength=n)
    for code in (1, 2):
        nspk[code] = np.bincount(u[st == code], minlength=n)
    return c, nspk


def gaussian_kernel(hollow=0.0):
    sd = GAUSS_SD / CCG_BIN
    x = np.arange(-int(5 * sd), int(5 * sd) + 1)
    k = np.exp(-x ** 2 / (2 * sd ** 2))
    k[len(x) // 2] *= (1 - hollow)
    return k / k.sum()


def predictor(c, hollow=0.0):
    """Baseline predictor: each CCG convolved with the Gaussian, edges padded by reflection."""
    k = gaussian_kernel(hollow)
    pad = len(k) // 2
    cp = np.pad(c.astype(float), [(0, 0)] * (c.ndim - 1) + [(pad, pad)], mode="reflect")
    return signal.fftconvolve(cp, k.reshape((1,) * (c.ndim - 1) + (-1,)), mode="valid", axes=-1)


SYN_BINS = np.where((LAGS >= SYN_WINDOW[0] - 1e-9) & (LAGS <= SYN_WINDOW[1] + 1e-9))[0]


def _two_consecutive(m):
    return np.any(m[..., 1:] & m[..., :-1], axis=-1)


def detect_connections(c, hollow=0.0):
    """Excitatory and inhibitory connections [pre, post] from CCG counts [pre, post, lag]."""
    pred = predictor(c, hollow)
    cs, ps = c[..., SYN_BINS], np.maximum(pred[..., SYN_BINS], 1e-12)
    hi = stats.poisson.ppf(P_HIGH, ps)
    lo = stats.poisson.ppf(P_LOW, ps)
    exc = _two_consecutive(cs > hi)
    inh = _two_consecutive(cs < lo)
    n = c.shape[0]
    eye = np.eye(n, dtype=bool)
    return exc & ~eye, inh & ~eye, pred


def transmission(c, pred, n_pre):
    """Excess spikes over the predictor in +1.5 to +4 ms divided by presynaptic spikes."""
    ex = (c[..., SYN_BINS] - pred[..., SYN_BINS]).sum(axis=-1)
    with np.errstate(divide="ignore", invalid="ignore"):
        return ex / n_pre[:, None]


def dip(c, pred):
    """(predictor - CCG) / predictor at the deepest bin in +1.5 to +4 ms."""
    cs, ps = c[..., SYN_BINS].astype(float), pred[..., SYN_BINS]
    with np.errstate(divide="ignore", invalid="ignore"):
        r = (ps - cs) / ps
    r = np.where(np.isfinite(r), r, -np.inf)
    out = r.max(axis=-1)
    return np.where(np.isfinite(out), out, np.nan)


# --- light pulses ---------------------------------------------------------------------------

def psth_counts(train, onsets, lo=-0.1, hi=0.02, bin=0.001):
    """Spike counts in 1 ms bins from lo to hi around each onset, summed over onsets."""
    edges = np.arange(lo, hi + bin / 2, bin)
    out = np.zeros(len(edges) - 1)
    i0 = np.searchsorted(train, onsets + lo)
    i1 = np.searchsorted(train, onsets + hi)
    rel = np.concatenate([train[a:b] - o for a, b, o in zip(i0, i1, onsets)]) if len(onsets) else []
    if len(rel):
        out = np.histogram(rel, edges)[0].astype(float)
    return out, edges


def opto_tagged(train, onsets, n_sd=8.0):
    """STAR Methods rule; returns (tagged, peak, baseline mean, baseline SD) in spikes per bin."""
    h, edges = psth_counts(train, onsets)
    left = edges[:-1]
    base = h[(left >= -0.1) & (left < 0.0)]
    win = h[(left >= 0.001 - 1e-9) & (left < 0.006 - 1e-9)]
    peak = np.mean(np.sort(win)[-2:])
    mu, sd = base.mean(), base.std()
    return peak > mu + n_sd * sd, peak, mu, sd


def rate_in(train, starts, stops):
    """Spike rate within a set of intervals."""
    if len(starts) == 0:
        return np.nan
    i0 = np.searchsorted(train, starts)
    i1 = np.searchsorted(train, stops)
    return (i1 - i0).sum() / np.sum(stops - starts)


# --- laminar analyses: LFP blocks of each state, gamma ICA, spike-IC coupling ----------------
#
# Where the parameters come from:
# - ICA: STAR Methods, "Independent Component Analysis of LFPs": LFP band-passed 30-100 Hz, PCA
#   reduced to the first ten PCs, ICA (runica, Bell and Sejnowski 1995), ICs ranked by the variance
#   they explain in the original data (relative power), loadings as the columns of the mixing matrix.
#   runica (EEGLAB infomax) is not available in Python; scikit-learn's FastICA, which seeks the same
#   maximally non-Gaussian sources, is used instead (a substitution, stated in the notebook). The ICA
#   is fitted on waking (fig2c-six-gamma-ics names waking as a reading; Figure 5A is waking) and its
#   unmixing applied to non-REM.
# - Spike-IC coupling: STAR Methods, "Spectral analysis, cross-frequency coupling, and spike-LFP
#   coupling": wavelet phase at 20 log-spaced scales from 30 to 100 Hz at each spike, mean resultant
#   length, Rayleigh p < 0.05, preferred frequency as the largest mean vector length.
# - Coherence clustering: STAR Methods, "Gamma coherence and gradient descent clustering": energy
#   gap moves of single sites between clusters from random initial assignments, repeated.
# - Power by site and state: Welch spectra of each state's LFP (4096-sample Hann segments, a standard
#   choice for 0.3 Hz resolution); the band means equal those of a wavelet power average.
# - The blocks of each state are its longest epochs of at least 30 s, up to LAMINAR_MAX s in total, a
#   reduction for speed (standard choice), as for the waking coupling above.

LAMINAR_MAX = {"Awake": 600.0, "Non-REM": 600.0, "REM": 300.0}
GAMMA_BAND = (30.0, 100.0)
GAMMA_FREQS = np.logspace(np.log10(30.0), np.log10(100.0), 20)
N_PCS = 10
POWER_BANDS = {"0.5-3": (0.5, 3.0), "3-6": (3.0, 6.0), "6-9": (6.0, 9.0), "30-60": (30.0, 60.0),
               "60-100": (60.0, 100.0)}
F_36 = np.sqrt(3.0 * 6.0)       # centre (geometric) of the 3-6 Hz band for its wavelet phase


def state_blocks(states, label, max_s, min_epoch=COUPLING_MIN_EPOCH):
    """Longest epochs of a state, at least min_epoch s each, up to max_s s in total."""
    if states is None:
        return np.zeros(0), np.zeros(0)
    m = states["label"] == label
    a, b = states["start"][m], states["stop"][m]
    keep = (b - a) >= min_epoch
    a, b = a[keep], b[keep]
    order = np.argsort(-(b - a))
    sa, sb, used = [], [], 0.0
    for t0, t1 in zip(a[order], b[order]):
        if used >= max_s:
            break
        t1 = min(t1, t0 + max_s - used)
        if t1 - t0 >= min_epoch:
            sa.append(t0)
            sb.append(t1)
            used += t1 - t0
    return np.array(sa), np.array(sb)


def read_blocks(s, label):
    """LFP (uV, all sites) of the blocks of a state."""
    a, b = state_blocks(s["states"], label, LAMINAR_MAX[label])
    rate = s["lfp_rate"]
    L = s["_file"]["processing/ecephys/LFP/LFP/data"]
    out = []
    for t0, t1 in zip(a, b):
        x = L[int(t0 * rate):int(t1 * rate), :].astype(np.float32) * np.float32(s["raw_conversion"] * 1e6)
        out.append((t0, t1, x))
    return out


def welch_power(blocks, fs):
    """Mean power spectrum [freq, site] over blocks, weighted by length."""
    acc, w, f = None, 0, None
    for _, _, x in blocks:
        f, p = signal.welch(x, fs, nperseg=4096, axis=0)
        acc = p * len(x) if acc is None else acc + p * len(x)
        w += len(x)
    return f, acc / w


def gamma_coherence(blocks, fs, band=GAMMA_BAND, nperseg=1250):
    """Magnitude-squared coherence between all site pairs, averaged over the band."""
    win = signal.windows.hann(nperseg).astype(np.float32)
    freqs = np.fft.rfftfreq(nperseg, 1 / fs)
    fm = (freqs >= band[0]) & (freqs <= band[1])
    S = None
    for _, _, x in blocks:
        n = len(x) // nperseg
        if n == 0:
            continue
        seg = x[: n * nperseg].reshape(n, nperseg, -1)
        seg = seg - seg.mean(axis=1, keepdims=True)
        X = np.fft.rfft(seg * win[None, :, None], axis=1)[:, fm, :]
        part = np.einsum("sfi,sfj->fij", X.conj(), X)
        S = part if S is None else S + part
    d = np.real(np.einsum("fii->fi", S))
    coh = np.abs(S) ** 2 / (d[:, :, None] * d[:, None, :])
    return coh.mean(axis=0)


def coherence_clusters(C, n_init, rng, max_iter=200):
    """Energy-gap clustering of sites (STAR Methods): each site moves to the cluster B with the largest
    positive gap mean_{j in B} C_ij - mean_{k in A, k != i} C_ik, until no site moves. Starts from
    n_init random clusters; empty clusters disappear. Returns labels relabelled by depth order."""
    n = C.shape[0]
    lab = rng.integers(0, n_init, n)
    C = C.copy()
    np.fill_diagonal(C, 0.0)
    for _ in range(max_iter):
        moved = False
        for i in rng.permutation(n):
            ks = np.unique(lab)
            means = np.empty(len(ks))
            for q, k in enumerate(ks):
                m = lab == k
                cnt = m.sum() - (lab[i] == k)
                means[q] = C[i, m].sum() / cnt if cnt > 0 else -np.inf
            best = ks[int(np.argmax(means))]
            own = means[int(np.where(ks == lab[i])[0][0])]
            if best != lab[i] and means.max() > own:
                lab[i] = best
                moved = True
        if not moved:
            break
    # energy: -sum over clusters of mean pairwise coherence within, as the STAR Methods define it
    energy = 0.0
    for k in np.unique(lab):
        m = lab == k
        energy -= C[np.ix_(m, m)].sum() / m.sum()
    # relabel by the median site of each cluster
    ks = np.unique(lab)
    order = ks[np.argsort([np.median(np.where(lab == k)[0]) for k in ks])]
    out = np.empty(n, int)
    for q, k in enumerate(order):
        out[lab == k] = q
    return out, energy


def bandpass(x, band, fs, order=3):
    return signal.sosfiltfilt(signal.butter(order, band, btype="band", fs=fs, output="sos"), x, axis=0)


def gamma_ica(blocks, fs, seed=0):
    """FastICA on the first N_PCS PCs of the 30-100 Hz LFP of the blocks. Returns the mixing matrix
    [site, IC] (each column signed so that its largest absolute value is positive), the unmixing
    matrix [IC, site] and each IC's share of the band-passed LFP variance (relative power)."""
    from sklearn.decomposition import FastICA
    xs = [bandpass(x, GAMMA_BAND, fs).astype(np.float32)[::4] for _, _, x in blocks]
    X = np.concatenate(xs)
    X = X - X.mean(axis=0)
    cov = X.T @ X / len(X)
    ev, E = np.linalg.eigh(cov)
    E = E[:, np.argsort(ev)[::-1][:N_PCS]]
    Z = X @ E
    ica = FastICA(n_components=N_PCS, whiten="unit-variance", random_state=seed, max_iter=1000)
    Sx = ica.fit_transform(Z)
    A = E @ ica.mixing_                                   # site x IC
    var = (A ** 2).sum(axis=0) * Sx.var(axis=0)
    rel = var / np.trace(cov)
    sign = np.sign(A[np.argmax(np.abs(A), axis=0), np.arange(A.shape[1])])
    A = A * sign
    W = np.linalg.pinv(A)                                 # IC x site, applied to centred band-passed LFP
    return A, W, rel


def rayleigh_p(n, mrl):
    with np.errstate(invalid="ignore", divide="ignore", over="ignore"):
        rn = n * mrl
        p = np.exp(np.sqrt(1 + 4 * n + 4 * (n ** 2 - rn ** 2)) - (1 + 2 * n))
    return np.minimum(p, 1.0)


def spike_phase_sums(blocks, trains, signals, fs_lfp, freqs, decim=COUPLING_DECIMATE):
    """Sum of exp(i phase) at each spike [unit, signal, freq], and spikes used per unit, over blocks.
    `signals(x)` maps a block [sample, site] to the signals [sample, k] whose phases are taken."""
    fs = fs_lfp / decim
    sums, counts = None, np.zeros(len(trains), int)
    for t0, t1, x in blocks:
        y = signals(x)
        y = signal.decimate(y, decim, axis=0, zero_phase=True)
        if sums is None:
            sums = np.zeros((len(trains), y.shape[1], len(freqs)), complex)
        idx = []
        for k, tr in enumerate(trains):
            sp = tr[(tr >= t0 + COUPLING_EDGE) & (tr < t1 - COUPLING_EDGE)]
            idx.append(np.minimum(np.round((sp - t0) * fs).astype(int), y.shape[0] - 1))
            counts[k] += len(sp)
        for j in range(y.shape[1]):
            ph = np.exp(1j * morlet_phase(y[:, j], fs, freqs))
            for k in range(len(trains)):
                sums[k, j] += ph[:, idx[k]].sum(axis=1)
    return sums, counts


def wavelet_amplitude(x, fs, freqs, w0=MORLET_W0):
    """Amplitude [freq, sample] of the complex Morlet transform."""
    out = np.empty((len(freqs), len(x)))
    for i, f in enumerate(freqs):
        sd = w0 / (2 * np.pi * f)
        t = np.arange(-4 * sd, 4 * sd + 1 / fs, 1 / fs)
        k = np.exp(2j * np.pi * f * t) * np.exp(-t ** 2 / (2 * sd ** 2))
        k = k / np.abs(k).sum()
        out[i] = np.abs(signal.fftconvolve(x, k[::-1].conj(), mode="same"))
    return out


def laminar(s):
    """Per-state power and gamma coherence by site, gamma ICA (waking), spike-IC coupling in waking and
    non-REM, and spike phases on the 3-6 Hz LFP of a layer 4 site in waking."""
    if s["states"] is None:
        return None
    fs = s["lfp_rate"]
    trains = s["trains"]
    out = {"power": {}, "coherence": {}, "seconds": {}}
    blocks = {}
    for lab in ("Awake", "Non-REM", "REM"):
        blocks[lab] = read_blocks(s, lab)
        out["seconds"][lab] = float(sum(t1 - t0 for t0, t1, _ in blocks[lab]))
        if out["seconds"][lab] == 0:
            continue
        f, p = welch_power(blocks[lab], fs)
        out["power"][lab] = {k: p[(f >= a) & (f < b)].mean(axis=0) for k, (a, b) in POWER_BANDS.items()}
        out["coherence"][lab] = gamma_coherence(blocks[lab], fs)
    wake = blocks["Awake"]
    if out["seconds"]["Awake"] == 0:
        return out
    A, W, rel = gamma_ica(wake, fs)
    out.update(A=A, W=W, rel=rel)

    def ics(x):
        xb = bandpass(x, GAMMA_BAND, fs)
        return (xb - xb.mean(axis=0)) @ W.T

    for lab, key in (("Awake", "wake"), ("Non-REM", "nrem")):
        if out["seconds"][lab] == 0:
            continue
        sums, counts = spike_phase_sums(blocks[lab], trains, ics, fs, GAMMA_FREQS)
        with np.errstate(invalid="ignore", divide="ignore"):
            mrl = np.abs(sums) / counts[:, None, None]
        out[f"ic_mrl_{key}"] = mrl                      # unit x IC (all ten) x frequency
        out[f"ic_p_{key}"] = rayleigh_p(counts[:, None, None].astype(float), mrl)
        out[f"ic_n_{key}"] = counts

    # layer 4 site: peak loading of the third of the six highest-variance ICs ordered by depth
    top6 = np.argsort(rel)[::-1][:6]
    peaks = np.sort(np.argmax(A[:, top6], axis=0))
    l4 = int(peaks[2])
    out["l4_site"] = l4
    sums, counts = spike_phase_sums(wake, trains, lambda x: x[:, [l4]].astype(float), fs, np.array([F_36]))
    z = sums[:, 0, 0]
    with np.errstate(invalid="ignore", divide="ignore"):
        out["p36_mrl"] = np.abs(z) / counts
        out["p36_phase"] = np.angle(z)
    out["p36_p"] = rayleigh_p(counts.astype(float), out["p36_mrl"])
    out["p36_n"] = counts

    # 3-6 Hz and 6-9 Hz amplitude over time in waking (figs2c), at the layer 4 site and the deepest site
    fsd = fs / COUPLING_DECIMATE
    amp = {"l4_36": [], "l4_69": [], "deep_69": []}
    win = {"l4_36": [], "l4_69": [], "deep_69": []}
    for t0, t1, x in wake:
        y = signal.decimate(x[:, [l4, x.shape[1] - 1]].astype(float), COUPLING_DECIMATE, axis=0, zero_phase=True)
        e = int(COUPLING_EDGE * fsd)
        a36 = wavelet_amplitude(y[:, 0], fsd, np.linspace(3, 6, 4)).mean(axis=0)
        a69 = wavelet_amplitude(y[:, 0], fsd, np.linspace(6, 9, 4)).mean(axis=0)
        d69 = wavelet_amplitude(y[:, 1], fsd, np.linspace(6, 9, 4)).mean(axis=0)
        step = int(fsd / 10)                           # 10 Hz time base for the correlation
        for k, v in (("l4_36", a36), ("l4_69", a69), ("deep_69", d69)):
            amp[k].append(v[e:-e:step])
        # 10 s windows stepped by 1 s (state-scoring spectrogram time base)
        f10, t10, Z = signal.stft(y, fsd, nperseg=int(10 * fsd), noverlap=int(9 * fsd), axis=0,
                                  boundary=None, padded=False)
        P = np.abs(Z) ** 2                              # freq x site x time
        win["l4_36"].append(P[(f10 >= 3) & (f10 <= 6), 0].mean(axis=0))
        win["l4_69"].append(P[(f10 >= 6) & (f10 <= 9), 0].mean(axis=0))
        win["deep_69"].append(P[(f10 >= 6) & (f10 <= 9), 1].mean(axis=0))
    out["amp_time"] = {k: np.concatenate(v) for k, v in amp.items()}
    out["pow_win"] = {k: np.concatenate(v) for k, v in win.items()}

    # phase-amplitude coupling: 3-6 Hz phase at the layer 4 site in waking; slow oscillation phase in
    # non-REM at a layer 6 site, 15 sites (300 um) below c, the MUA peak in mid layer 5 (an assumption)
    out["pac_wake_36"] = pac(wake, fs, l4, (3.0, 6.0))
    if out["seconds"]["Non-REM"] > 0:
        l6 = int(min(np.argmax(s["mua_power"]) + 15, 63))
        out["l6_site"] = l6
        out["pac_nrem_13"] = pac(blocks["Non-REM"], fs, l6, (1.0, 3.0))
        out["pac_nrem_053"] = pac(blocks["Non-REM"], fs, l6, (0.5, 3.0))
    return out


# --- phase-amplitude coupling (Figure 3D) ---------------------------------------------------
#
# Tort et al. (2008) modulation index, cited by the STAR Methods (Spectral analysis, cross-frequency
# coupling, and spike-LFP coupling), with 18 phase bins of 20 degrees (the cited method's setting, as the
# claims file gives it). The phase band is band-passed (3rd-order Butterworth, zero phase) and its phase
# taken by the Hilbert transform, as Tort et al. do; amplitudes are Morlet wavelet amplitudes (w0 = 6)
# at PAC_FREQS, computed in the frequency domain, on every other site. 2 s at each block edge are left out.

PAC_FREQS = np.logspace(np.log10(5.0), np.log10(200.0), 24)    # Figure 3D axis, 5 to 200 Hz (claims file)
PAC_SITES = np.arange(0, 64, 2)
PAC_BINS = 18
PAC_EDGE = 2.0


def morlet_amplitudes(x, fs, freqs, w0=MORLET_W0):
    """Amplitude [freq, sample] of a Morlet transform done in the frequency domain (scale-free, as the
    modulation index does not depend on the amplitude's scale)."""
    n = len(x)
    X = np.fft.fft(x - x.mean())
    fr = np.fft.fftfreq(n, 1 / fs)
    out = np.empty((len(freqs), n), np.float32)
    for i, f in enumerate(freqs):
        g = np.exp(-0.5 * ((fr - f) / (f / w0)) ** 2) * (fr > 0)
        out[i] = np.abs(np.fft.ifft(X * g))
    return out


def pac(blocks, fs, phase_site, band):
    """Modulation index [site of PAC_SITES, freq of PAC_FREQS] of amplitude by the phase of `band` at
    `phase_site`, accumulated over blocks."""
    acc = np.zeros((len(PAC_SITES), len(PAC_FREQS), PAC_BINS))
    edges = np.linspace(-np.pi, np.pi, PAC_BINS + 1)
    for _, _, x in blocks:
        e = int(PAC_EDGE * fs)
        if len(x) <= 2 * e:
            continue
        ph = np.angle(signal.hilbert(bandpass(x[:, phase_site].astype(float), band, fs)))[e:-e]
        b = np.clip(np.digitize(ph, edges) - 1, 0, PAC_BINS - 1)
        for q, site in enumerate(PAC_SITES):
            a = morlet_amplitudes(x[:, site].astype(float), fs, PAC_FREQS)[:, e:-e]
            for j in range(PAC_BINS):
                acc[q, :, j] += a[:, b == j].sum(axis=1)
    P = acc / acc.sum(axis=2, keepdims=True)
    with np.errstate(divide="ignore", invalid="ignore"):
        H = -(P * np.log(P)).sum(axis=2)
    return (np.log(PAC_BINS) - H) / np.log(PAC_BINS)


# --- unit firing measures (Figures 6 and 8) -----------------------------------------------

ACG_BIN = 0.0005
ACG_MAX = 0.3


@njit(cache=True)
def _acg(t, nbins, binsize):
    out = np.zeros(nbins, np.int64)
    n = t.shape[0]
    for i in range(n):
        j = i + 1
        while j < n:
            d = t[j] - t[i]
            b = int(d / binsize)
            if b >= nbins:
                break
            out[b] += 1
            j += 1
    return out


@njit(cache=True)
def _xcorr(ref, tgt, nbins, binsize, half):
    out = np.zeros(nbins, np.int64)
    j0 = 0
    m = tgt.shape[0]
    for i in range(ref.shape[0]):
        r = ref[i]
        while j0 < m and tgt[j0] < r - half:
            j0 += 1
        j = j0
        while j < m and tgt[j] < r + half:
            b = int((tgt[j] - r + half) / binsize)
            if 0 <= b < nbins:
                out[b] += 1
            j += 1
    return out


def downup_onsets(ud):
    """UP onsets that start where a DOWN interval ends (DOWN-UP transitions)."""
    up = ud["label"] == "UP"
    on = ud["start"][up]
    return on[np.isin(np.round(on, 4), np.round(ud["stop"][~up], 4))]


def firing_measures(s):
    """Autocorrelogram (0.5 ms bins to 300 ms), PETH around DOWN-UP transitions (5 ms bins, -300 to
    +300 ms) and the median first-spike latency after them."""
    trains = s["trains"]
    nb = int(round(ACG_MAX / ACG_BIN))
    out = {"acg": np.array([_acg(tr, nb, ACG_BIN) for tr in trains])}
    ud = s["updown"]
    if ud is None:
        return out
    on = downup_onsets(ud)
    edges = np.arange(-0.3, 0.3 + 1e-9, 0.005)
    peth = np.zeros((len(trains), len(edges) - 1))
    first = np.full(len(trains), np.nan)
    for k, tr in enumerate(trains):
        i0 = np.searchsorted(tr, on - 0.3)
        i1 = np.searchsorted(tr, on + 0.3)
        rel = np.concatenate([tr[a:b] - o for a, b, o in zip(i0, i1, on)]) if len(on) else np.zeros(0)
        peth[k] = np.histogram(rel, edges)[0]
        j = np.searchsorted(tr, on)
        ok = j < len(tr)
        lat = tr[j[ok]] - on[ok]
        lat = lat[lat < 0.3]
        if len(lat):
            first[k] = np.median(lat)
    out.update(peth=peth / max(len(on), 1) / 0.005, peth_edges=edges, first_latency=first, n_onsets=len(on))
    return out


def long_ccgs(s, refs, half=1.0, binsize=0.01):
    """CCGs (10 ms bins, +-1 s) of each unit in refs against every unit, per state (Awake, Non-REM),
    with the reference spikes in that state, as counts."""
    trains = s["trains"]
    nb = int(round(2 * half / binsize))
    out = {}
    for lab in ("Awake", "Non-REM"):
        st = s["states"]
        if st is None:
            continue
        m = st["label"] == lab
        for r in refs:
            tr = trains[r]
            ins = np.zeros(len(tr), bool)
            for a, b in zip(st["start"][m], st["stop"][m]):
                i0, i1 = np.searchsorted(tr, [a, b])
                ins[i0:i1] = True
            ref = tr[ins]
            out[(lab, int(r))] = (np.array([_xcorr(ref, t, nb, binsize, half) for t in trains]), len(ref))
    return out


# --- one session, reduced to what the notebook uses ----------------------------------------

def process_session(asset):
    """Load one file and reduce it to per-unit and per-connection results (run in a worker)."""
    s = load_session(asset)
    n = len(s["trains"])
    out = {k: s[k] for k in ("path", "subject", "genotype", "session_id", "unit_ids", "columns",
                             "cell_type", "synaptic_effect", "quality", "max_channel", "states",
                             "updown", "laser", "visual", "raw_shape", "raw_rate", "lfp_shape",
                             "lfp_rate", "rel_y", "electrode_y", "electrode_location",
                             "electrode_imp", "duration", "electrode_id", "series_electrodes", "groups")}
    out["n_spikes"] = np.array([len(tr) for tr in s["trains"]])
    out["sorted_ok"] = np.array([bool(np.all(np.diff(tr) >= 0)) for tr in s["trains"]])
    out["t_range"] = (float(min(tr[0] for tr in s["trains"] if len(tr))),
                      float(max(tr[-1] for tr in s["trains"] if len(tr))))
    out["train_head"] = [tuple(np.round(tr[:5], 5)) for tr in s["trains"]]

    # waveforms, wide band (main) and 300 Hz high-pass (variant)
    W, cnt = mean_waveforms(s)
    out["wf_spikes"] = cnt
    out["mua_power"] = W["mua_power"]
    out["landmark"] = downup_csd(s)
    for key, hp in (("wf", None), ("wf_hp", 300.0)):
        out[key] = [waveform_features(W[hp][k]) if cnt[k] >= MIN_WAVEFORM_SPIKES else None
                    for k in range(n)]
    sites = np.array([f["site"] if f is not None else -1 for f in out["wf"]])
    out["coupling"] = spike_lfp_coupling(s, sites)

    # cross-correlograms and connections
    c, nspk = ccgs(s)
    out["nspk_state"] = nspk
    # connections detected within each state, with the reference spikes in that state (a diagnostic)
    out["conn_state"] = {}
    for code, name in ((1, "Awake"), (2, "Non-REM")):
        e_, i_, _ = detect_connections(c[code])
        out["conn_state"][name] = (int(e_.sum()), int(i_.sum()))
    for hollow in (0.0, 0.6):
        exc, inh, pred = detect_connections(c[0], hollow)
        key = "conn" if hollow == 0 else "conn_hollow"
        out[key] = {"exc": exc, "inh": inh}
        if hollow == 0:
            pairs = np.argwhere(exc | inh)
            res = {"pre": pairs[:, 0], "post": pairs[:, 1],
                   "exc": exc[pairs[:, 0], pairs[:, 1]], "inh": inh[pairs[:, 0], pairs[:, 1]], "ccg": c[0][pairs[:, 0], pairs[:, 1]],
                   "pred": pred[pairs[:, 0], pairs[:, 1]]}
            res["stp"] = transmission(c[0], pred, nspk[0])[pairs[:, 0], pairs[:, 1]]
            for code, name in ((1, "wake"), (2, "nrem")):
                cc = c[code][pairs[:, 0], pairs[:, 1]]
                pp = predictor(cc)
                res[f"ccg_{name}"] = cc
                res[f"dip_{name}"] = dip(cc, pp)
                with np.errstate(divide="ignore", invalid="ignore"):
                    res[f"ratio_{name}"] = (cc[:, SYN_BINS] / pp[:, SYN_BINS]).max(axis=-1)
                res[f"stp_{name}"] = ((cc[:, SYN_BINS] - pp[:, SYN_BINS]).sum(-1)
                                      / np.maximum(nspk[code][pairs[:, 0]], 1))
            out["pairs"] = res
    del c

    # light pulses: pooled and per intensity, true onsets and onsets shifted by 0.5 s (null)
    out["opto"] = None
    if s["laser"] is not None and len(s["laser"]["start"]):
        on = s["laser"]["start"]
        amp = np.round(s["laser"]["amplitude"], 1).ravel()
        if amp.shape != on.shape:                 # an amplitude per pulse is not given in every file
            amp = np.zeros(len(on))
        levels = np.unique(amp)
        res = {"levels": levels, "n_pulses": np.array([(amp == L).sum() for L in levels])}
        for key, shift in (("true", 0.0), ("shifted", 0.5)):
            tag_pool = np.zeros(n, bool)
            tag_any = np.zeros(n, bool)
            for k, tr in enumerate(s["trains"]):
                tag_pool[k] = opto_tagged(tr, on + shift)[0]
                tag_any[k] = any(opto_tagged(tr, on[amp == L] + shift)[0] for L in levels)
            res[f"{key}_pooled"] = tag_pool
            res[f"{key}_any"] = tag_any
        out["opto"] = res

    # UP and DOWN rates, with the labels shifted by 10 s as a null for the clock check
    out["updown_rates"] = None
    if s["updown"] is not None:
        ud = s["updown"]
        rates = {}
        for shift in (0.0, 10.0):
            for lab in ("UP", "DOWN"):
                m = ud["label"] == lab
                rates[(lab, shift)] = np.array([rate_in(tr, ud["start"][m] + shift, ud["stop"][m] + shift)
                                                for tr in s["trains"]])
        out["updown_rates"] = rates

    # firing measures, laminar LFP analyses, light-pulse PSTHs
    out["firing"] = firing_measures(s)
    s["mua_power"] = out["mua_power"]
    out["laminar"] = laminar(s)
    out["laser_psth"] = None
    if s["laser"] is not None and len(s["laser"]["start"]):
        out["laser_psth"] = np.array([psth_counts(tr, s["laser"]["start"], -0.1, 0.1)[0] for tr in s["trains"]]) \
            / len(s["laser"]["start"]) / 0.001
    out["visual_psth"] = None
    if s["visual"] is not None:
        vd = s["visual"]["stop"] - s["visual"]["start"]
        von = s["visual"]["start"][(vd > 0.39) & (vd < 0.41)]
        out["visual_psth"] = np.array([psth_counts(tr, von, -0.1, 0.5, 0.01)[0] for tr in s["trains"]]) \
            / len(von) / 0.01
    # DOWN state-active candidates (either reading of fig8-down-active-neurons) and their long CCGs
    out["long_ccg"], out["down_cand"] = {}, None
    if out["updown_rates"] is not None and out["firing"].get("peth") is not None:
        r = out["updown_rates"]
        cand_a = np.where(r[("DOWN", 0.0)] > r[("UP", 0.0)])[0]
        pe, ed = out["firing"]["peth"], out["firing"]["peth_edges"][:-1]
        pre, post = pe[:, (ed >= -0.1) & (ed < 0)].mean(1), pe[:, (ed >= 0) & (ed < 0.1)].mean(1)
        cand_b = np.where((pre > post) & (ed[np.argmax(pe, axis=1)] < 0))[0]
        out["down_cand"] = {"a": cand_a, "b": cand_b}
        out["long_ccg"] = long_ccgs(s, np.union1d(cand_a, cand_b))
    out["state_rates"] = None
    if s["states"] is not None:
        st = s["states"]
        out["state_rates"] = {lab: np.array([rate_in(tr, st["start"][st["label"] == lab],
                                                     st["stop"][st["label"] == lab]) for tr in s["trains"]])
                              for lab in np.unique(st["label"])}
    s["_file"].close()
    return out
