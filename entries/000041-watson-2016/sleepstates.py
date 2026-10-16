"""Loading and sleep-state measures for dandiset 000041 (Watson et al. 2016, Neuron).

The dandiset holds one NWB file per session: sorted units with spike times and a cell type,
a table of sleep states (Awake, Non-REM, REM, at 1 s resolution), LFP at 1250 Hz and spike
waveforms. Files are streamed from the DANDI Archive at a pinned version; nothing is
written to disk.

Where parameters come from:

- Microarousal (MA): an Awake epoch shorter than 40 s between two Non-REM epochs. Paper,
  Results ("Shorter epochs (<40 sec) ... restricted ... to only those which occur between
  nonREM periods").
- SLEEP: alternating nonREM and REM of at least 20 min, terminated by Awake longer than
  120 s; a WAKE-SLEEP cycle needs at least 7 min of WAKE before it. Paper, Results.
- Burst index: fraction of inter-spike intervals under 15 ms. Paper, Results.
- Frequency bands: delta 0.5-4 Hz, sigma 9-25 Hz, gamma 40-100 Hz. Paper, Results.
- Sextiles of WAKE rate over all pE cells of the dataset. Paper, Results and Methods.
- Choices the paper's main text leaves open, made here as common defaults: 10 bins of
  normalized time; 2 s Hann windows stepped by 1 s for LFP power; the LFP channel flagged
  `spindle_reference` in the electrodes table; packets of at least 20 s for time courses.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import h5py
import numpy as np
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import signal

DANDISET_ID = "000041"
DANDISET_VERSION = "0.250624.0419"

# Spike times of this file are whole seconds divided by 20000 (8451 distinct values from 0 to
# 0.4252 s, against a recording of 7959 s); the conversion set a 20 kHz rate on times already in
# seconds. Its spikes cannot be placed in time, so the session is left out of every analysis.
EXCLUDED = {
    "sub-Dino/sub-Dino_ses-Dino-072114_ecephys.nwb":
        "spike times are whole seconds divided by 20000",
}

LFP_RATE = 1250.0
BANDS = {"delta": (0.5, 4.0), "sigma": (9.0, 25.0), "gamma": (40.0, 100.0)}
MA_MAX = 40.0          # s, longest microarousal
SLEEP_BREAK = 120.0    # s, Awake longer than this ends SLEEP
SLEEP_MIN = 20 * 60.0  # s, shortest SLEEP period
WAKE_MIN = 7 * 60.0    # s, shortest WAKE before a WAKE-SLEEP cycle
BURST_ISI = 0.015      # s


def asset_urls() -> list[tuple[str, str]]:
    """(path, streaming URL) for every NWB file of the pinned version, sorted by path."""
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in ds.get_assets())


def open_nwb(url: str) -> h5py.File:
    return h5py.File(remfile.File(url), "r")


def _str(values) -> np.ndarray:
    return np.array([v.decode() if isinstance(v, bytes) else str(v) for v in values])


@dataclass
class Session:
    path: str
    subject: str
    session_id: str
    spikes: list            # one sorted array of spike times (s) per unit
    cell_type: np.ndarray   # 'excitatory', 'inhibitory' or 'unknown'
    starts: np.ndarray      # state table
    stops: np.ndarray
    labels: np.ndarray      # 'Awake', 'Non-REM', 'REM'
    state: np.ndarray = field(default=None)  # 'WAKE', 'MA', 'NREM', 'REM'
    lfp_channel: int = -1
    lfp_samples: int = 0
    lfp: dict = field(default_factory=dict)  # per packet index, band power series
    lfp_raw: list = field(default_factory=list)  # (start time, int16 samples) for the clock check

    @property
    def pe(self) -> np.ndarray:
        return np.where(self.cell_type == "excitatory")[0]

    @property
    def pi(self) -> np.ndarray:
        return np.where(self.cell_type == "inhibitory")[0]


def load_session(path: str, url: str, f: h5py.File | None = None) -> Session:
    """Units, states and the LFP reference channel of one file; LFP itself is not read."""
    f = f or open_nwb(url)
    u = f["units"]
    times = u["spike_times"][()]
    idx = u["spike_times_index"][()]
    bounds = np.concatenate([[0], idx])
    spikes = [np.sort(times[bounds[i]:bounds[i + 1]]) for i in range(len(idx))]
    st = f["processing/behavior/states"]
    el = f["general/extracellular_ephys/electrodes"]
    ref = np.where(el["spindle_reference"][()])[0]
    lfp_el = f["processing/ecephys/LFP/lfp/electrodes"][()]
    # column of the LFP matrix that holds the reference electrode
    col = int(np.where(lfp_el == ref[0])[0][0]) if len(ref) and ref[0] in lfp_el else -1
    s = Session(path=path,
                subject=_str([f["general/subject/subject_id"][()]])[0],
                session_id=_str([f["general/session_id"][()]])[0],
                spikes=spikes, cell_type=_str(u["cell_type"][()]),
                starts=st["start_time"][()].astype(float), stops=st["stop_time"][()].astype(float),
                labels=_str(st["label"][()]),
                lfp_channel=col, lfp_samples=f["processing/ecephys/LFP/lfp/data"].shape[0])
    s.state = classify_states(s.starts, s.stops, s.labels)
    return s


def classify_states(starts, stops, labels) -> np.ndarray:
    """WAKE, MA, NREM or REM for each row of the state table (MA as in the module docstring)."""
    out = np.array(["WAKE" if L == "Awake" else "NREM" if L == "Non-REM" else "REM" for L in labels],
                   dtype=object)
    dur = stops - starts
    for i in range(1, len(labels) - 1):
        if labels[i] == "Awake" and dur[i] < MA_MAX and labels[i - 1] == "Non-REM" and labels[i + 1] == "Non-REM":
            out[i] = "MA"
    return out


def nrem_episodes(state) -> list[tuple[int, int]]:
    """(first, last) row of each maximal run of NREM and MA, beginning and ending with NREM."""
    runs, i, n = [], 0, len(state)
    while i < n:
        if state[i] == "NREM":
            j = i
            while j + 1 < n and state[j + 1] in ("NREM", "MA"):
                j += 1
            while state[j] != "NREM":
                j -= 1
            runs.append((i, j))
            i = j + 1
        else:
            i += 1
    return runs


def sleep_periods(starts, stops, labels, require_wake_end: bool = True) -> list[dict]:
    """SLEEP periods as defined in the claims file. Awake rows longer than 120 s split the
    session into segments; in each, leading and trailing Awake rows are trimmed and what remains
    is a SLEEP period if it lasts at least 20 min. `pre` and `post` are the long Awake rows
    around it (None at the start or end of the recording)."""
    long_wake = np.where((labels == "Awake") & (stops - starts > SLEEP_BREAK))[0]
    cuts = [-1] + list(long_wake) + [len(labels)]
    out = []
    for lo, hi in zip(cuts[:-1], cuts[1:]):
        rows = [r for r in range(lo + 1, hi) if labels[r] != "Awake"]
        if not rows:
            continue
        first, last = rows[0], rows[-1]
        pre = lo if lo >= 0 else None
        post = hi if hi < len(labels) else None
        if post is None and require_wake_end:
            continue
        if stops[last] - starts[first] >= SLEEP_MIN:
            out.append(dict(first=first, last=last, start=starts[first], stop=stops[last],
                            pre=pre, post=post))
    return out


def cycles(s: Session, require_wake_end: bool = True) -> list[dict]:
    """WAKE-SLEEP cycles: SLEEP periods preceded by an Awake epoch of at least 7 min."""
    return [p for p in sleep_periods(s.starts, s.stops, s.labels, require_wake_end)
            if p["pre"] is not None and s.stops[p["pre"]] - s.starts[p["pre"]] >= WAKE_MIN]


def counts(spk: np.ndarray, starts, stops) -> np.ndarray:
    """Spike counts of one unit in each interval [start, stop)."""
    return np.searchsorted(spk, stops) - np.searchsorted(spk, starts)


def rates(spikes: list, units, starts, stops) -> np.ndarray:
    """Rate of each unit over the union of the intervals (Hz); intervals must not overlap."""
    starts, stops = np.atleast_1d(starts), np.atleast_1d(stops)
    T = float(np.sum(stops - starts))
    return np.array([counts(spikes[u], starts, stops).sum() / T for u in units])


def state_rates(s: Session, units, states) -> np.ndarray:
    m = np.isin(s.state, states)
    return rates(s.spikes, units, s.starts[m], s.stops[m])


def binned_intervals(start, stop, nbins, include=None):
    """For each of nbins equal bins of [start, stop), the sub-intervals that fall in `include`
    (a list of (start, stop)); all of the bin when include is None. Returns a list of
    (starts, stops) arrays, one per bin."""
    edges = np.linspace(start, stop, nbins + 1)
    out = []
    for a, b in zip(edges[:-1], edges[1:]):
        if include is None:
            out.append((np.array([a]), np.array([b])))
        else:
            ss = [max(a, x) for x, y in include if y > a and x < b]
            ee = [min(b, y) for x, y in include if y > a and x < b]
            out.append((np.array(ss), np.array(ee)))
    return out


def bin_rates(s: Session, units, bins) -> tuple[np.ndarray, np.ndarray]:
    """Rates (units x bins) and durations per bin for the output of binned_intervals."""
    dur = np.array([np.sum(e - a) for a, e in bins])
    r = np.full((len(units), len(bins)), np.nan)
    for k, (a, e) in enumerate(bins):
        if dur[k] > 0:
            r[:, k] = [counts(s.spikes[u], a, e).sum() / dur[k] for u in units]
    return r, dur


def isis_in(spk: np.ndarray, starts, stops):
    """Intervals between consecutive spikes whose two spikes lie in the same interval; returns
    (isi, time of the later spike, index of the interval)."""
    if len(spk) < 2:
        return np.array([]), np.array([]), np.array([], int)
    k = np.searchsorted(starts, spk, side="right") - 1
    inside = (k >= 0) & (spk < np.asarray(stops)[np.clip(k, 0, None)])
    same = inside[1:] & inside[:-1] & (k[1:] == k[:-1])
    return np.diff(spk)[same], spk[1:][same], k[1:][same]


def burst_index(spk, starts, stops, reading: str = "a", min_isi: int = 10) -> float:
    """Reading a: fraction of intervals under 15 ms. Reading b: fraction of spikes with an
    interval under 15 ms to the previous or next spike (same interval only)."""
    if len(spk) < 2:
        return np.nan
    starts, stops = np.asarray(starts), np.asarray(stops)
    k = np.searchsorted(starts, spk, side="right") - 1
    inside = (k >= 0) & (spk < stops[np.clip(k, 0, None)])
    same = inside[1:] & inside[:-1] & (k[1:] == k[:-1])
    if same.sum() < min_isi:
        return np.nan
    short = (np.diff(spk) < BURST_ISI) & same
    if reading == "a":
        return short.sum() / same.sum()
    part = np.zeros(len(spk), bool)
    part[1:] |= short
    part[:-1] |= short
    return part[inside].sum() / inside.sum()


def autocorrelogram(spk, starts, stops, max_lag=0.3, bin_ms=1.0) -> tuple[np.ndarray, int]:
    """Counts of spike-time differences in 1 ms bins from 0 to max_lag, pairs within the same
    interval, and the number of spikes inside the intervals."""
    starts, stops = np.asarray(starts), np.asarray(stops)
    k = np.searchsorted(starts, spk, side="right") - 1
    inside = (k >= 0) & (spk < stops[np.clip(k, 0, None)])
    t, k = spk[inside], k[inside]
    edges = np.arange(0, max_lag * 1000 + bin_ms, bin_ms) / 1000.0
    h = np.zeros(len(edges) - 1)
    lag = 1
    while lag < len(t):
        # rounded to 1 ns, so that float error does not move a lag that falls on a bin edge
        d = np.round(t[lag:] - t[:-lag], 9)
        ok = (k[lag:] == k[:-lag]) & (d < max_lag)
        if not ok.any() and np.min(d) >= max_lag:
            break
        h += np.histogram(d[ok], edges)[0]
        lag += 1
    return h, len(t)


def band_power(x: np.ndarray, fs: float = LFP_RATE):
    """Log10 mean power in each band for 2 s Hann windows stepped by 1 s; returns the window
    centres (s, from the start of x) and a dict of arrays."""
    nper = int(2 * fs)
    if len(x) < nper:
        return np.array([]), {b: np.array([]) for b in BANDS}
    f, t, S = signal.spectrogram(x.astype(float), fs=fs, window="hann", nperseg=nper,
                                 noverlap=nper - int(fs), detrend="constant", scaling="density")
    out = {}
    for b, (lo, hi) in BANDS.items():
        m = (f >= lo) & (f <= hi)
        out[b] = np.log10(S[m].mean(axis=0))
    return t, out


def read_packet_lfp(f: h5py.File, s: Session, min_dur: float = 2.0, raw_seconds: float = 300.0) -> None:
    """Band power series of every NREM packet of at least min_dur seconds, from the reference
    channel, into s.lfp[row] = (window centre times in s, dict of log10 band power). The raw
    samples of the first packets of at least 30 s, up to raw_seconds in all, are kept in
    s.lfp_raw for checking the LFP clock against the spikes."""
    d = f["processing/ecephys/LFP/lfp/data"]
    kept = 0.0
    for i in np.where(s.state == "NREM")[0]:
        a, b = s.starts[i], s.stops[i]
        if b - a < min_dur:
            continue
        i0, i1 = int(round(a * LFP_RATE)), min(int(round(b * LFP_RATE)), s.lfp_samples)
        if i1 - i0 < int(2 * LFP_RATE):
            continue
        x = d[i0:i1, s.lfp_channel]
        t, p = band_power(x)
        s.lfp[i] = (a + t, p)
        if b - a >= 30 and kept < raw_seconds:
            s.lfp_raw.append((i0 / LFP_RATE, x))
            kept += len(x) / LFP_RATE


def wake_sextiles(sessions: list[Session]) -> tuple[np.ndarray, dict]:
    """Sextile edges of WAKE rate over all pE cells, and for each session path the WAKE rate
    and sextile (1 to 6) of each of its pE cells."""
    wr = {s.path: state_rates(s, s.pe, ["WAKE"]) for s in sessions}
    allr = np.concatenate(list(wr.values()))
    edges = np.quantile(allr, np.linspace(0, 1, 7))
    out = {}
    for p, r in wr.items():
        g = np.searchsorted(edges[1:-1], r, side="right") + 1
        out[p] = (r, g)
    return edges, out


def _load_with_lfp(item) -> Session:
    path, url = item
    f = open_nwb(url)
    s = load_session(path, url, f)
    read_packet_lfp(f, s)
    return s


def load_all(workers: int = 4) -> tuple[list[Session], dict]:
    """Every usable session with its packet LFP power, streamed in parallel, in path order;
    and the excluded paths with the reason."""
    from concurrent.futures import ProcessPoolExecutor
    items = [(p, u) for p, u in asset_urls() if p not in EXCLUDED]
    with ProcessPoolExecutor(workers) as ex:
        sessions = list(ex.map(_load_with_lfp, items))
    return sessions, dict(EXCLUDED)
