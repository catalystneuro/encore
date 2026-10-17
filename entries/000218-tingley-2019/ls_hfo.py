"""Loading and measures for dandiset 000218 (Tingley and Buzsaki 2019, lateral septum HFOs).

The files hold LFP at 1250 Hz on every channel, sorted units with a region label (in most
files), sleep states, epochs and trials. They hold no detected events, so LS high-frequency
oscillations (HFOs) and CA1 ripples are detected here from the LFP.

Where the parameters come from:

- Event detection follows the paper's Methods (Ripple detection): 120-200 Hz Butterworth
  band-pass of order 3, normalized squared signal, peak threshold 5 SD, start and stop at
  2 SD, durations 15 to 250 ms. What the Methods leave open is taken from the code they
  name, bz_FindRipples.m of buzcode at commit 5981194ee764436383269d5fbe09980ae852c6fe
  (15 October 2019): zero-phase filtering (filtfilt), an 11-sample moving average of the
  squared signal, z-scoring over the whole recording, merging events less than 30 ms
  apart, the event time taken at the trough of the filtered signal, amplitude as the
  peak normalized squared signal, and exclusion of events whose LFP-derived EMG at the
  event start exceeds 0.9.
- The EMG is computed as in bz_EMGFromLFP.m (same commit): the mean pairwise zero-lag
  correlation of the 300-600 Hz band between channels on different shanks, in windows of
  +-0.1 s every 0.1 s (the sampling bz_FindRipples asks for). One channel per shank is
  used, up to six shanks. This replaces the paper's "noise" channel, whose identity is
  not given; the Methods allow the EMG when there is no such channel.
- Instantaneous frequency follows the Methods: Hilbert phase of the band-passed LFP,
  unwrapped, median filtered over +-6 samples, differentiated at the sample of peak power.
- Phase locking follows the Methods: 120-200 Hz Butterworth of order 4, 7 ms RMS smoothing,
  epochs where the z-scored RMS stays above 2, Hilbert phase at each spike in those epochs,
  Rayleigh test, units with more than 50 such spikes, 10 circular shifts of the phase as
  the null.
- Channels are not named in the paper. The rule here (a common choice): in a 300 s sample
  (from the start of the longest NREM bout when sleep states exist, otherwise from the
  middle of the recording), drop channels whose broadband SD is below 0.2 or above 5 times
  the median of their region, then take the LS channel and the hippocampal channel with
  the highest 120-200 Hz SD. The hippocampal channel stands for the CA1 pyramidal layer,
  where ripple power peaks (Methods, Relative anatomical depth within CA1).
"""

from __future__ import annotations

import time
import zlib

import h5py
import numpy as np
import remfile
import requests
from scipy import signal, stats

DANDISET = "000218"
VERSION = "0.250624.0439"
FS = 1250.0
LFP = "processing/ecephys/LFP/ElectricalSeries_lfp/data"

# Detection parameters (see the module docstring for their sources).
BAND = (120.0, 200.0)
THRESHOLDS = (2.0, 5.0)
MIN_GAP_MS = 30.0
MIN_DUR_MS = 15.0
MAX_DUR_MS = 250.0
EMG_THRESH = 0.9
SAMPLE_S = 300.0
LOCALIZATION_S = 1800.0

_client = None


def dandiset():
    """The pinned version of the dandiset."""
    global _client
    from dandi.dandiapi import DandiAPIClient
    if _client is None:
        _client = DandiAPIClient()
    return _client.get_dandiset(DANDISET, VERSION)


def assets(version=None):
    """Path, size, asset id and blob id of every asset in the pinned (or the given) version."""
    from dandi.dandiapi import DandiAPIClient
    ds = dandiset() if version is None else DandiAPIClient().get_dandiset(DANDISET, version)
    return [{"path": a.path, "size": a.size, "asset_id": a.identifier, "blob": getattr(a, "blob", None)}
            for a in ds.get_assets()]


def content_url(path):
    return dandiset().get_asset_by_path(path).get_content_url(follow_redirects=1, strip_query=True)


def open_file(path):
    url = content_url(path)
    return h5py.File(remfile.File(url), "r"), url


def _s(x):
    return x.decode() if isinstance(x, bytes) else str(x)


# --- streaming -------------------------------------------------------------------

def chunk_table(d):
    """(offset, byte offset, size) of every chunk of a dataset. Loads its chunk index once."""
    out = []
    d.id.chunk_iter(lambda i: out.append((i.chunk_offset, i.byte_offset, i.size)))
    return out


def read_columns(url, d, cols, table, rows=None, threads=16, max_request=16 * 2**20):
    """Columns of a gzip-chunked int16 dataset, fetched as byte ranges in parallel.

    h5py reads one chunk per request through remfile; this asks for runs of adjacent
    chunks at once and decompresses them here, which is about 20 times faster.
    """
    ct, cc = d.chunks
    n = d.shape[0]
    r0, r1 = (0, n) if rows is None else (max(0, int(rows[0])), min(n, int(rows[1])))
    need = [t for t in table if any(t[0][1] <= c < t[0][1] + cc for c in cols)
            and t[0][0] < r1 and t[0][0] + ct > r0]
    need.sort(key=lambda t: t[1])
    groups, cur = [], []
    for t in need:
        if cur and (t[1] != cur[-1][1] + cur[-1][2] or t[1] + t[2] - cur[0][1] > max_request):
            groups.append(cur)
            cur = []
        cur.append(t)
    if cur:
        groups.append(cur)
    out = np.zeros((r1 - r0, len(cols)), dtype=np.int16)
    session = requests.Session()

    def get(group):
        a, b = group[0][1], group[-1][1] + group[-1][2] - 1
        err = None
        for k in range(6):
            try:
                r = session.get(url, headers={"Range": f"bytes={a}-{b}"}, timeout=120)
                r.raise_for_status()
                buf = r.content
                if len(buf) != b - a + 1:
                    raise IOError("short read")
                break
            except Exception as e:  # retried, then raised
                err = e
                time.sleep(2 * (k + 1))
        else:
            raise err
        return [(off, np.frombuffer(zlib.decompress(buf[bo - a:bo - a + sz]), dtype="<i2").reshape(ct, cc))
                for off, bo, sz in group]

    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(threads) as ex:
        for res in ex.map(get, groups):
            for (rr, c0), blk in res:
                a, b = max(rr, r0), min(rr + ct, r1)
                for j, c in enumerate(cols):
                    if c0 <= c < c0 + cc:
                        out[a - r0:b - r0, j] = blk[a - rr:b - rr, c - c0]
    return out


# --- metadata --------------------------------------------------------------------

def metadata(f):
    """Everything but the LFP samples: electrodes, units, states, epochs, trials."""
    m = {"subject": _s(f["general/subject/subject_id"][()]),
         "session_id": _s(f["general/session_id"][()]) if "general/session_id" in f else None}
    el = f["general/extracellular_ephys/electrodes"]
    m["el_location"] = np.array([_s(x) for x in el["location"][:]])
    m["el_group"] = np.array([_s(x) for x in el["group_name"][:]])
    m["el_shank_index"] = el["shank_electrode_number"][:]
    m["el_xyz"] = np.c_[el["x"][:], el["y"][:], el["z"][:]]
    d = f[LFP]
    m["lfp_shape"], m["lfp_chunks"] = d.shape, d.chunks
    m["lfp_rate"] = float(f[LFP.replace("/data", "/starting_time")].attrs["rate"])
    m["lfp_conversion"] = float(d.attrs["conversion"])
    m["lfp_unit"] = _s(d.attrs["unit"])
    m["lfp_electrodes"] = f[LFP.replace("/data", "/electrodes")][:]
    m["duration"] = d.shape[0] / m["lfp_rate"]
    units = {"spikes": [], "location": None, "group": None}
    if "units" in f:
        u = f["units"]
        st, idx = u["spike_times"][:], u["spike_times_index"][:]
        units["spikes"] = np.split(st, idx[:-1])
        if "location" in u:
            units["location"] = np.array([_s(x) for x in u["location"][:]])
        if "group_id" in u:
            units["group"] = np.array([_s(x) for x in u["group_id"][:]])
    m["units"] = units
    m["states"] = None
    if "processing/ecephys/sleep_states" in f:
        s = f["processing/ecephys/sleep_states"]
        m["states"] = {"start": s["start_time"][:], "stop": s["stop_time"][:],
                       "label": np.array([_s(x) for x in s["label"][:]])}
    m["epochs"] = None
    if "intervals/epochs" in f:
        e = f["intervals/epochs"]
        m["epochs"] = {"start": e["start_time"][:], "stop": e["stop_time"][:],
                       "tags": [_s(x) for x in e["tags"][:]]}
    m["trials"] = None
    if "intervals/trials" in f:
        t = f["intervals/trials"]
        m["trials"] = {"start": t["start_time"][:], "stop": t["stop_time"][:]}
    return m


# --- signal processing -----------------------------------------------------------

def bandpass(x, lo, hi, order=3, fs=FS):
    b, a = signal.butter(order, [lo / (fs / 2), hi / (fs / 2)], "bandpass")
    return signal.filtfilt(b, a, np.asarray(x, dtype=float), axis=0)


def _moving_average(x, n):
    """Centred moving average with zero padding, as Filter0 in bz_FindRipples."""
    return np.convolve(x, np.ones(n) / n, mode="same")


def analytic(x, block=2**20, pad=2000):
    """Hilbert analytic signal computed in overlapping blocks, to keep memory low."""
    n = len(x)
    out = np.empty(n, dtype=np.complex64)
    for s in range(0, n, block):
        a, b = max(0, s - pad), min(n, s + block + pad)
        h = signal.hilbert(x[a:b])
        out[s:min(n, s + block)] = h[s - a:s - a + min(block, n - s)]
    return out


def emg_from_lfp(X, fs=FS):
    """Mean pairwise correlation of the 300-600 Hz band in +-0.1 s windows every 0.1 s.

    X is samples x channels, one channel per shank. Returns (times, emg)."""
    step = int(round(0.1 * fs))
    half = step
    n_samples, k = X.shape
    centres = np.arange(half, n_samples - half, step)
    emg = np.zeros(len(centres))
    sos = signal.butter(3, [300 / (fs / 2), 600 / (fs / 2)], "bandpass", output="sos")
    block, pad = 2 * 10**6, 5000
    for b0 in range(0, n_samples, block):
        a, b = max(0, b0 - pad), min(n_samples, b0 + block + pad)
        Y = signal.sosfiltfilt(sos, X[a:b].astype(np.float32), axis=0).astype(np.float32)
        sel = np.where((centres >= b0) & (centres < b0 + block))[0]
        if len(sel) == 0:
            continue
        idx = centres[sel] - a
        W = np.lib.stride_tricks.sliding_window_view(Y, 2 * half, axis=0)[idx - half]  # windows x ch x 2half
        W = W - W.mean(axis=2, keepdims=True)
        W /= np.sqrt((W ** 2).sum(axis=2, keepdims=True)) + 1e-12
        # sum over pairs of w_i.w_j = (|sum_i w_i|^2 - k) / 2 for unit vectors
        s = W.sum(axis=1)
        emg[sel] = ((s ** 2).sum(axis=1) - k) / 2
    return centres / fs, emg / max(k * (k - 1) / 2, 1)


def detect_events(x, emg_t=None, emg=None, fs=FS):
    """Port of bz_FindRipples (buzcode 5981194) with the paper's Methods parameters.

    Returns a dict of arrays: start, peak, stop (s), amplitude (peak normalized squared
    signal), duration (s), frequency (Hz), peak_power_time (s), and counts dropped at
    each step."""
    filt = bandpass(x, *BAND, order=3, fs=fs)
    nss = _moving_average(filt ** 2, 11)
    nss -= nss.mean()
    nss /= nss.std()
    above = nss > THRESHOLDS[0]
    d = np.diff(above.astype(np.int8))
    start = np.where(d > 0)[0]
    stop = np.where(d < 0)[0]
    if len(stop) and len(start) and stop[0] < start[0]:
        stop = stop[1:]
    m = min(len(start), len(stop))
    start, stop = start[:m], stop[:m]
    counts = {"threshold": m}
    # merge events closer than MIN_GAP_MS
    gap = MIN_GAP_MS / 1000 * fs
    ms, me = [], []
    for a, b in zip(start, stop):
        if ms and a - me[-1] < gap:
            me[-1] = b
        else:
            ms.append(a)
            me.append(b)
    start, stop = np.array(ms, int), np.array(me, int)
    counts["merged"] = len(start)
    peak_idx = np.empty(len(start), int)
    ppow_idx = np.empty(len(start), int)
    amp = np.empty(len(start))
    for i, (a, b) in enumerate(zip(start, stop)):
        seg = nss[a:b + 1]
        j = int(np.argmax(seg))
        amp[i] = seg[j]
        ppow_idx[i] = a + j
        peak_idx[i] = a + int(np.argmin(filt[a:b + 1]))
    keep = amp > THRESHOLDS[1]
    start, stop, peak_idx, ppow_idx, amp = start[keep], stop[keep], peak_idx[keep], ppow_idx[keep], amp[keep]
    counts["peak"] = len(start)
    dur = (stop - start) / fs
    keep = (dur >= MIN_DUR_MS / 1000) & (dur <= MAX_DUR_MS / 1000)
    start, stop, peak_idx, ppow_idx, amp, dur = (v[keep] for v in (start, stop, peak_idx, ppow_idx, amp, dur))
    counts["duration"] = len(start)
    if emg is not None and len(start):
        k = np.clip(np.searchsorted(emg_t, start / fs), 0, len(emg_t) - 1)
        k0 = np.clip(k - 1, 0, len(emg_t) - 1)
        k = np.where(np.abs(emg_t[k0] - start / fs) < np.abs(emg_t[k] - start / fs), k0, k)
        keep = emg[k] <= EMG_THRESH
        start, stop, peak_idx, ppow_idx, amp, dur = (v[keep] for v in (start, stop, peak_idx, ppow_idx, amp, dur))
    counts["emg"] = len(start)
    freq = np.full(len(start), np.nan)
    pad = int(0.1 * fs)
    for i in range(len(start)):
        a, b = max(0, start[i] - pad), min(len(filt), stop[i] + pad)
        ph = np.unwrap(np.angle(signal.hilbert(filt[a:b])))
        ph = signal.medfilt(ph, 13)
        dph = np.diff(ph)
        j = min(ppow_idx[i] - a, len(dph) - 1)
        freq[i] = dph[j] * fs / (2 * np.pi)
    return {"start": start / fs, "stop": stop / fs, "peak": peak_idx / fs, "peak_power_time": ppow_idx / fs,
            "amplitude": amp, "duration": dur, "frequency": freq, "counts": counts}


def phase_locking(x, spike_trains, rng, fs=FS, min_spikes=50, n_shifts=10):
    """Phase locking of each spike train to the 120-200 Hz band in high-power epochs.

    Returns per unit: n spikes in epochs, Rayleigh p, resultant length, mean phase (rad,
    0 = peak, +-pi = trough of the band-passed LFP) and the resultant lengths with the
    phase circularly shifted (null). Units with too few spikes get NaN. Also returns the
    clock check of shifted_locking for all units pooled."""
    filt = bandpass(x, *BAND, order=4, fs=fs)
    rms = np.sqrt(_moving_average(filt ** 2, int(round(0.007 * fs))))
    inside = rms > rms.mean() + 2 * rms.std()
    del rms
    phase = np.angle(analytic(filt)).astype(np.float32)
    del filt
    n = len(phase)
    shifts = rng.integers(int(fs), n - int(fs), n_shifts)
    clock = shifted_locking(phase, inside, [np.asarray(st) for st in spike_trains])
    out = []
    for st in spike_trains:
        idx = np.round(np.asarray(st) * fs).astype(int)
        idx = idx[(idx >= 0) & (idx < n)]
        idx = idx[inside[idx]]
        rec = {"n": len(idx), "p": np.nan, "r": np.nan, "phase": np.nan, "r_null": [np.nan] * n_shifts}
        if len(idx) > min_spikes:
            ph = phase[idx].astype(float)
            c = np.exp(1j * ph).mean()
            r = np.abs(c)
            nn = len(ph)
            # Rayleigh test (Zar; as circ_rtest in CircStat)
            R = nn * r
            zstat = R ** 2 / nn
            p = np.exp(np.sqrt(1 + 4 * nn + 4 * (nn ** 2 - R ** 2)) - (1 + 2 * nn))
            rec.update(p=float(p), r=float(r), phase=float(np.angle(c)), z=float(zstat))
            rec["r_null"] = [float(np.abs(np.exp(1j * phase[(idx + s) % n].astype(float)).mean())) for s in shifts]
        out.append(rec)
    return out, clock


CLOCK_SHIFTS_MS = (-20, -10, -5, -2, 0, 2, 5, 10, 20)


def shifted_locking(phase, inside, spike_trains, shifts_ms=CLOCK_SHIFTS_MS, fs=FS):
    """Resultant length of the band phase at all spikes pooled, inside the marked samples, with
    the spikes shifted in time. Locking that peaks at zero shift shows the spike times and the
    LFP share a clock to within a few ms (one cycle of the band is about 7 ms)."""
    if not spike_trains:
        return None
    allsp = np.concatenate(spike_trains)
    n = len(phase)
    out = []
    for sh in shifts_ms:
        idx = np.round(allsp * fs + sh / 1000 * fs).astype(int)
        idx = idx[(idx >= 0) & (idx < n)]
        idx = idx[inside[idx]]
        out.append(float(np.abs(np.exp(1j * phase[idx].astype(float)).mean())) if len(idx) else np.nan)
    return {"shifts_ms": list(shifts_ms), "r": out}


# --- channel choice --------------------------------------------------------------

def sample_window(meta):
    """(start, stop) in seconds of the 300 s sample used to choose channels."""
    st = meta["states"]
    if st is not None and np.any(st["label"] == "Non-REM"):
        nrem = st["label"] == "Non-REM"
        dur = st["stop"] - st["start"]
        i = np.argmax(np.where(nrem, dur, -1))
        a = st["start"][i]
        return a, min(a + SAMPLE_S, meta["duration"])
    mid = meta["duration"] / 2
    return mid, min(mid + SAMPLE_S, meta["duration"])


def choose_channels(meta, X):
    """LS channel, hippocampal channel and EMG channels from a sample X (samples x all channels)."""
    loc, grp = meta["el_location"], meta["el_group"]
    broad = X.std(axis=0)
    band = bandpass(X, *BAND, order=3).std(axis=0)
    good = np.ones(len(loc), bool)
    for region in set(loc):
        sel = loc == region
        med = np.median(broad[sel])
        good &= ~sel | ((broad > 0.2 * med) & (broad < 5 * med))
    out = {"band_sd": band, "broad_sd": broad, "good": good}
    for name, regions in (("ls", ("ls",)), ("hpc", ("hpc",)), ("ca3", ("ca3",))):
        sel = np.where(good & np.isin(loc, regions))[0]
        out[name] = int(sel[np.argmax(band[sel])]) if len(sel) else None
    shanks = []
    for g in dict.fromkeys(grp):  # in order of first appearance
        sel = np.where(good & (grp == g))[0]
        if len(sel):
            shanks.append(int(sel[len(sel) // 2]))
    if len(shanks) > 6:
        shanks = [shanks[i] for i in np.linspace(0, len(shanks) - 1, 6).round().astype(int)]
    out["emg"] = shanks
    return out


# --- per-session job -------------------------------------------------------------

def state_of(times, states):
    """Sleep-state label at each time ('' outside every scored interval)."""
    lab = np.full(len(times), "", dtype=object)
    if states is None:
        return lab
    order = np.argsort(states["start"])
    s0, s1, sl = states["start"][order], states["stop"][order], states["label"][order]
    k = np.searchsorted(s0, times, side="right") - 1
    ok = (k >= 0) & (times <= s1[np.clip(k, 0, None)])
    lab[ok] = sl[k[ok]]
    return lab


def coherence_around(a, b, centres, half=0.1, fs=FS):
    """Phase-locking value across events of the phase difference between two band-passed
    signals (complex analytic arrays), at each lag in +-half s around the given times."""
    h = int(round(half * fs))
    idx = np.round(np.asarray(centres) * fs).astype(int)
    idx = idx[(idx > h) & (idx < len(a) - h)]
    lags = np.arange(-h, h + 1)
    if len(idx) == 0:
        return lags / fs, np.full(len(lags), np.nan), 0
    M = idx[:, None] + lags[None, :]
    d = np.angle(a[M]) - np.angle(b[M])
    return lags / fs, np.abs(np.exp(1j * d).mean(axis=0)), len(idx)


def session_job(path, seed=None, full_channels=None):
    """Everything the notebook needs from one file, computed while streaming.

    Reads the metadata, a 300 s sample of all channels, then the whole LS channel, the
    hippocampal channel and one channel per shank for the EMG. Returns events, phase
    locking and coherence. full_channels also reads up to 30 min of all channels from the
    sample's start and returns their HFO-triggered band power (localization claim); by
    default it does so for files with electrodes outside LS and the hippocampus. The seed
    defaults to a checksum of the path, so each file has its own fixed generator."""
    t0 = time.time()
    f, url = open_file(path)
    meta = metadata(f)
    if seed is None:
        seed = zlib.crc32(path.encode())
    if full_channels is None:
        full_channels = bool(set(meta["el_location"]) - {"ls", "hpc", "ca3", "unknown"})
    rng = np.random.default_rng(seed)
    res = {"path": path, "meta": meta}
    if not np.any(meta["el_location"] == "ls"):
        res["skipped"] = "no LS electrodes"
        res["seconds"] = time.time() - t0
        return res
    d = f[LFP]
    table = chunk_table(d)
    w0, w1 = sample_window(meta)
    X = read_columns(url, d, list(range(d.shape[1])), table, rows=(w0 * FS, w1 * FS)).astype(np.float32)
    ch = choose_channels(meta, X)
    del X
    res["channels"] = {k: ch[k] for k in ("ls", "hpc", "ca3", "emg")}
    res["channel_stats"] = {"band_sd": ch["band_sd"], "broad_sd": ch["broad_sd"], "good": ch["good"]}
    res["sample_window"] = (w0, w1)
    cols = [ch["ls"]] + ([ch["hpc"]] if ch["hpc"] is not None else []) + list(ch["emg"])
    cols = list(dict.fromkeys(cols))
    Y = read_columns(url, d, cols, table)
    res["fingerprint"] = int(zlib.crc32(Y[: int(10 * FS), 0].tobytes()))
    emg_cols = [cols.index(c) for c in ch["emg"]]
    emg_t, emg = emg_from_lfp(Y[:, emg_cols]) if len(emg_cols) >= 2 else (None, None)
    res["emg_summary"] = None if emg is None else {"n_channels": len(emg_cols), "frac_above": float(np.mean(emg > EMG_THRESH)),
                                                  "median": float(np.median(emg))}
    ls = Y[:, cols.index(ch["ls"])].copy()
    hp = Y[:, cols.index(ch["hpc"])].copy() if ch["hpc"] is not None else None
    del Y
    res["ls_events"] = detect_events(ls, emg_t, emg)
    res["ls_events"]["state"] = state_of(res["ls_events"]["peak"], meta["states"])
    spikes = meta["units"]["spikes"]
    uloc = meta["units"]["location"]
    res["ls_units"] = [] if uloc is None else [i for i in range(len(spikes)) if uloc[i] == "ls"]
    res["phase_locking"], res["clock_ls"] = phase_locking(ls, [np.sort(spikes[i]) for i in res["ls_units"]], rng)
    if hp is not None:
        res["hpc_events"] = detect_events(hp, emg_t, emg)
        res["hpc_events"]["state"] = state_of(res["hpc_events"]["peak"], meta["states"])
        # CA1-LS 120-180 Hz phase coherence around CA1 ripples, and around jittered times
        a = analytic(bandpass(hp, 120, 180, 3))
        b = analytic(bandpass(ls, 120, 180, 3))
        rp = res["hpc_events"]["peak"]
        lags, plv, n = coherence_around(a, b, rp)
        inside = np.zeros(len(a), bool)
        for e0, e1 in zip(np.round(res["hpc_events"]["start"] * FS).astype(int), np.round(res["hpc_events"]["stop"] * FS).astype(int)):
            inside[e0:e1 + 1] = True
        hpc_trains = [np.sort(spikes[i]) for i in range(len(spikes)) if uloc is not None and uloc[i] == "hpc"]
        res["clock_hpc"] = shifted_locking(np.angle(a), inside, hpc_trains)
        del inside
        jit = [coherence_around(a, b, rp + rng.uniform(-1, 1, len(rp)))[1] for _ in range(20)]
        res["coherence"] = {"lags": lags, "plv": plv, "n": n, "jitter": np.array(jit)}
        del a, b
    del ls, hp
    if full_channels:
        r0, r1 = w0 * FS, min(meta["duration"], w0 + LOCALIZATION_S) * FS
        X = read_columns(url, d, list(range(d.shape[1])), table, rows=(r0, r1))
        res["localization"] = triggered_band_power(X, w0, res["ls_events"]["peak"], rng)
        res["localization"]["window"] = (r0 / FS, r1 / FS)
        del X
    res["seconds"] = time.time() - t0
    f.close()
    return res


def triggered_band_power(X, w0, peaks, rng, half=0.02, fs=FS):
    """Per channel, 120-200 Hz power in +-20 ms around the LS HFO peaks inside a block X
    that starts at w0 s, divided by the power at as many random times in the block."""
    n = len(X)
    h = int(round(half * fs))
    idx = np.round((np.asarray(peaks) - w0) * fs).astype(int)
    idx = idx[(idx > h) & (idx < n - h)]
    if len(idx) == 0:
        return {"n_events": 0, "ratio": np.full(X.shape[1], np.nan)}
    rnd = rng.integers(h + 1, n - h - 1, len(idx))
    win = np.arange(-h, h + 1)
    ratio = np.empty(X.shape[1])
    for j in range(X.shape[1]):
        p2 = bandpass(X[:, j], *BAND, order=3) ** 2
        ratio[j] = p2[idx[:, None] + win].mean() / p2[rnd[:, None] + win].mean()
    return {"n_events": len(idx), "ratio": ratio}


def _job(path):
    import os
    for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
        os.environ.setdefault(k, "1")
    try:
        return session_job(path)
    except Exception as e:  # reported by run_all, never replaced by a default result
        return {"path": path, "error": repr(e)}


def run_all(paths, workers=6):
    """session_job on every path, in parallel processes. Most of the time per file is spent
    loading its chunk index over the network, so more workers than cores help."""
    import multiprocessing as mp
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("spawn")) as ex:
        return list(ex.map(_job, paths))


# --- spike measures ----------------------------------------------------------------

def sorted_spikes(res, region):
    """{unit index: sorted spike times} of the units with this region label."""
    loc = res["meta"]["units"]["location"]
    if loc is None:
        return {}
    return {i: np.sort(s) for i, s in enumerate(res["meta"]["units"]["spikes"]) if loc[i] == region}


def counts_in(spikes, starts, stops):
    """Spike count of a sorted train inside each [start, stop]."""
    return np.searchsorted(spikes, stops, side="right") - np.searchsorted(spikes, starts, side="left")


def in_intervals(spikes, starts, stops):
    """The spikes inside any of the (sorted, non-overlapping) intervals."""
    if len(starts) == 0:
        return spikes[:0]
    k = np.searchsorted(starts, spikes, side="right") - 1
    ok = (k >= 0) & (spikes <= np.asarray(stops)[np.clip(k, 0, None)])
    return spikes[ok]


def peth(spikes, times, half=0.1, bin_s=0.001):
    """Spikes per event in each bin around the times (spike probability per bin)."""
    edges = np.arange(-half, half + bin_s / 2, bin_s)
    lo = np.searchsorted(spikes, times - half)
    hi = np.searchsorted(spikes, times + half)
    if (hi - lo).sum() == 0:
        return np.zeros(len(edges) - 1)
    d = np.concatenate([spikes[a:b] - t for a, b, t in zip(lo, hi, times)])
    return np.histogram(d, edges)[0] / max(len(times), 1)


def ccg(s1, s2, half=0.4, bin_s=0.001):
    """Cross-correlogram counts of s2 relative to s1, bins centred on 0 (2*half/bin_s + 1)."""
    nb = int(round(half / bin_s))
    lo = np.searchsorted(s2, s1 - half - bin_s / 2)
    hi = np.searchsorted(s2, s1 + half + bin_s / 2)
    n = hi - lo
    if n.sum() == 0:
        return np.zeros(2 * nb + 1)
    idx = np.repeat(lo - np.r_[0, np.cumsum(n)[:-1]], n) + np.arange(n.sum())
    d = s2[idx] - np.repeat(s1, n)
    b = np.round(d / bin_s).astype(int) + nb
    b = b[(b >= 0) & (b <= 2 * nb)]
    return np.bincount(b, minlength=2 * nb + 1).astype(float)


def gauss_smooth_at_zero(c, sd_bins):
    """Gaussian-weighted mean of a CCG around its centre bin, the kernel truncated to the window
    and divided by its mass inside it."""
    nb = (len(c) - 1) // 2
    lags = np.arange(-nb, nb + 1)
    w = np.exp(-0.5 * (lags / sd_bins) ** 2)
    return float((w * c).sum() / w.sum())


def excess_correlation(c_norm):
    """Fast (5 ms) minus slow (200 ms) smoothed CCG at zero lag (Cheng and Frank 2008)."""
    return gauss_smooth_at_zero(c_norm, 5) - gauss_smooth_at_zero(c_norm, 200)


def cv_mse(y, X, folds):
    """5-fold cross-validated MSE of a linear regression with intercept of each column of y
    (ripples x neurons) on each column of X (ripples x features). Returns neurons x features."""
    out = np.zeros((y.shape[1], X.shape[1]))
    for k in np.unique(folds):
        tr, te = folds != k, folds == k
        xm, ym = X[tr].mean(0), y[tr].mean(0)
        xc = X[tr] - xm
        vx = (xc ** 2).sum(0)
        b = (xc.T @ (y[tr] - ym)) / np.where(vx > 0, vx, np.inf)[:, None]  # features x neurons
        a = ym[None, :] - b * xm[:, None]
        for j in range(X.shape[1]):
            pred = a[j][None, :] + X[te, j][:, None] * b[j][None, :]
            out[:, j] += ((y[te] - pred) ** 2).sum(0)
    return out / len(y)
