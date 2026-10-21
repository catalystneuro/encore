"""Loading and measures for dandiset 000013, Hires, Gutnisky, Yu, O'Connor & Svoboda (2015), eLife
4, e06619, "Low-noise encoding of active touch by layer 4 in the somatosensory cortex".

Each NWB file holds one loose-seal recording (one cell, one session): a 10 kHz spike train
(`SpikeTrain`, 0 or 1 per sample) with the voltage it was detected from, 1 kHz whisker tracking
(azimuthal angle `theta_at_base`, the 6 to 60 Hz Hilbert `amplitude` and `phase`, curvature change
`delta_kappa`, touch onset and offset, lick onsets `beam_break_times`, `pole_available`), and a
trials table. Trials are 4.5 s windows, stored one after another with gaps between them. Files are
streamed from the archive at the pinned version; nothing is written to disk.

Times. Every per-trial quantity is kept in "virtual milliseconds": trial k, sample j of its
behaviour segment is at ``k * TRIAL_STRIDE_MS + j``, so that a search for the nearest event never
crosses into another trial. Spikes are placed on the same axis from their own timestamps. In 36
files the `SpikeTrain` timestamps are 10 ms earlier than those of the voltage the spikes were
detected from (the samples themselves line up); ``CLOCKS`` names the two readings, and the notebook shows which
one agrees with the touch response.

Where the parameters come from (the claims file, claims/000013/10.7554-elife.06619.yaml, cites the
paper for each):

- Whisking amplitude > 2.5 deg, non-whisking < 1.25 deg for >= 100 ms with no touch or lick,
  cycles excluded during licking or within 70 ms after touch, monotonic phase for phase analyses,
  touches > 100 ms left out of exploration time: Methods, Whisker analysis; Spikes accounted by
  active sensation (claims file, opening comment).
- Onset latency from the 1 ms PCTH, pre-touch mean (-50 to 0 ms) plus two s.d., searched 0 to 50
  ms: claim latency-determinable.
- Touch spike window: the shuffle rule with 1000 surrogates, 95th percentile, degree-11
  polynomial, 1 ms steps: claim fig3c-touch-spikes-l4c2. The cutoff is the first increment
  below chance after the increment has been above it (the criterion, after the answer in
  questions/000013.yaml); the literal search from 1 ms is a variant. The longest window searched
  (``TMAX_READINGS``) is not given in the paper; the criterion's open detail (4) lists both
  values as readings.
- Phase tuning: 12 bins, A[1 + cos(theta - phi)] + B with A, B >= 0, least squares: claim
  table1-l4-c2 (least squares named there as the standard choice).
- Standard choices that cannot change a result: the polynomial is fitted on t rescaled to
  [-1, 1] (numerical conditioning only); random generators are seeded per claim in the notebook.
"""

from __future__ import annotations

import re
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass, field

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy.optimize import least_squares

DANDISET_ID = "000013"
DANDISET_VERSION = "0.220126.2143"
API = "https://api.dandiarchive.org/api"

TRIAL_STRIDE_MS = 100_000      # spacing of trials on the virtual axis; trials last 4.5 s
CLOCKS = ("spike", "voltage")   # SpikeTrain timestamps, or those of the voltage

WHISK_AMP = 2.5          # deg, whisking (Methods)
NONWHISK_AMP = 1.25      # deg, non-whisking (Methods)
NONWHISK_MIN_MS = 100    # ms, non-whisking periods (Methods)
LONG_TOUCH_MS = 100      # ms, prolonged touches left out of exploration (Methods)
AFTER_TOUCH_MS = 70      # ms, whisk cycles excluded after touch (Methods)
PRE_MS = 50              # ms, pre-touch baseline for latency (Methods)
LAT_SEARCH_MS = 50       # ms, latency searched 0 to 50 ms (claim latency-determinable)
N_SURROGATES = 1000      # Methods
POLY_DEGREE = 11         # Methods
TMAX_READINGS = (100, 200)  # ms, longest touch window searched: readings (r100), (r200) of the claims file
N_PHASE_BINS = 12        # Figure 3, figure supplement 1C
N_SPOT_CHECK = 40        # spikes per file whose stored timestamp is read back

GROUPS = {"L4C2": "L4 inside C2", "L4out": "L4 outside C2", "L5": "L5 near C2"}


# ----------------------------------------------------------------------------- loading

def list_assets() -> pd.DataFrame:
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=200"
    rows = []
    while url:
        page = requests.get(url, timeout=60).json()
        rows += [dict(asset_id=a["asset_id"], path=a["path"], size=a["size"]) for a in page["results"]]
        url = page.get("next")
    return pd.DataFrame(rows).sort_values("path").reset_index(drop=True)


def _text(x):
    x = x[()]
    return x.decode() if isinstance(x, bytes) else str(x)


@dataclass
class Cell:
    """One recording, reduced to what the analyses use."""
    asset_id: str
    path: str
    identifier: str
    subject: str
    genotype: str
    region: str
    layer: int
    depth: float
    location: str
    trials: pd.DataFrame
    # behaviour, concatenated over trials, one sample per ms
    vt: np.ndarray            # virtual ms of each sample
    trial_of: np.ndarray      # trial index of each sample
    theta: np.ndarray
    amp: np.ndarray
    phase: np.ndarray
    dkappa: np.ndarray
    touch_on: np.ndarray      # bool
    touch_off: np.ndarray     # bool
    lick: np.ndarray          # bool, lick onsets
    pole: np.ndarray          # bool, pole in reach
    seg_t0: np.ndarray        # session time (s) of the first behaviour sample of each trial
    seg_start: np.ndarray     # index of each trial's first sample in the concatenated arrays
    spike_t: np.ndarray       # session time (s) of each spike, SpikeTrain timestamps
    spike_block_t0: np.ndarray  # first SpikeTrain timestamp of each trial's block
    spike_block_n: np.ndarray   # samples per block
    volt_offset: float        # voltage timestamp minus SpikeTrain timestamp (s)
    n_spike_samples: int
    extra: dict = field(default_factory=dict)

    @property
    def group(self) -> str:
        if self.layer == 5:
            return "L5"
        return "L4C2" if self.region == "C2" else "L4out"

    @property
    def cell_no(self) -> int:
        return int(re.search(r"Cell(\d+)", self.identifier).group(1))

    def spikes_vt(self, clock: str = "spike") -> np.ndarray:
        """Spike times in virtual ms. Spikes outside their trial's behaviour segment are dropped."""
        t = self.spike_t + (self.volt_offset if clock == "voltage" else 0.0)
        k = np.searchsorted(self.seg_t0, t, side="right") - 1
        ok = k >= 0
        pos = np.full(t.shape, -1.0)
        pos[ok] = (t[ok] - self.seg_t0[k[ok]]) * 1000.0
        nseg = np.diff(np.r_[self.seg_start, len(self.vt)])
        ok &= (pos >= 0) & (pos < nseg[np.clip(k, 0, None)])
        return k[ok] * TRIAL_STRIDE_MS + pos[ok]


def _segments(ts: np.ndarray, gap: float = 0.0015) -> np.ndarray:
    return np.r_[0, np.flatnonzero(np.diff(ts) > gap) + 1]


def load_cell(asset_id: str, path: str) -> Cell:
    url = f"{API}/assets/{asset_id}/download/"
    f = h5py.File(remfile.File(url), "r")
    g = f["general"]
    elec = list(g["intracellular_ephys"].keys())[0]
    loc = _text(g["intracellular_ephys"][elec]["location"])
    region = re.search(r"brain_subregion: (\w+)", loc).group(1)
    layer = int(re.search(r"cortical_layer: (\d)", loc).group(1))
    depth = float(re.search(r"depth: ([\d.]+)", loc).group(1))

    tt = f["intervals/trials"]
    trials = pd.DataFrame({k: tt[k][()] for k in tt.keys() if k != "id"})
    for c in trials.columns:
        if trials[c].dtype == object:
            trials[c] = [v.decode() if isinstance(v, bytes) else v for v in trials[c]]

    b = f["acquisition/behavior"]
    bts = b["theta_at_base/timestamps"][:]
    seg = _segments(bts)
    seg_t0 = bts[seg]
    # match behaviour segments to trials, by start time
    starts = trials["start_time"].to_numpy()
    if len(seg) != len(trials) or np.abs(seg_t0 - starts).max() > 0.01:
        raise ValueError(f"{path}: behaviour segments do not match the trials table")
    n = len(bts)
    trial_of = np.repeat(np.arange(len(seg)), np.diff(np.r_[seg, n]))
    within = np.arange(n) - seg[trial_of]
    vt = trial_of * TRIAL_STRIDE_MS + within

    def fl(name):
        return b[name + "/data"][:].astype(np.float32)

    def bo(name):
        return b[name + "/data"][:].astype(bool)

    sd = f["acquisition/SpikeTrain/data"]
    sts = f["acquisition/SpikeTrain/timestamps"]
    nsamp = sd.shape[0]
    idx = np.flatnonzero(sd[:])
    # The spike stream holds one block of regular 0.1 ms samples per trial, all of one length,
    # starting at a fixed offset from the trial's behaviour segment. Spike times are computed
    # from that layout, and checked against the stored timestamps of up to N_SPOT_CHECK spikes
    # (reading every timestamp over the network would take minutes per file).
    ntr = len(trials)
    if nsamp % ntr:
        raise ValueError(f"{path}: spike samples do not divide into equal blocks per trial")
    L = nsamp // ntr
    first_ts = float(sts[0])
    offset = round((first_ts - seg_t0[0]) * 1e4) / 1e4
    blk_t0 = seg_t0 + offset
    k = idx // L
    spike_t = blk_t0[k] + (idx - k * L) * 1e-4
    check = np.unique(np.linspace(0, len(idx) - 1, min(N_SPOT_CHECK, len(idx))).astype(int))
    stored = np.array([sts[int(i)] for i in idx[check]])
    spot_err = float(np.abs(stored - spike_t[check]).max()) if len(check) else 0.0
    vts0 = float(f["acquisition/CurrentClampSeries/timestamps"][0])
    cell = Cell(
        asset_id=asset_id, path=path, identifier=_text(f["identifier"]),
        subject=_text(g["subject/subject_id"]), genotype=_text(g["subject/genotype"]),
        region=region, layer=layer, depth=depth, location=loc, trials=trials,
        vt=vt, trial_of=trial_of.astype(np.int32),
        theta=fl("theta_at_base"), amp=fl("amplitude"), phase=fl("phase"), dkappa=fl("delta_kappa"),
        touch_on=bo("touch_onset"), touch_off=bo("touch_offset"), lick=bo("beam_break_times"),
        pole=bo("pole_available"), seg_t0=seg_t0, seg_start=seg,
        spike_t=spike_t, spike_block_t0=blk_t0, spike_block_n=np.full(ntr, L),
        volt_offset=vts0 - first_ts, n_spike_samples=int(nsamp),
        extra=dict(spike_offset=offset, spot_check_err=spot_err, n_spot_checked=len(check)),
    )
    f.close()
    return cell


def _load_row(row) -> Cell:
    return load_cell(row[0], row[1])


def load_all(max_workers: int = 8) -> list[Cell]:
    """Load every file, in separate processes (h5py serialises reads within one process)."""
    assets = list_assets()
    rows = list(zip(assets.asset_id, assets.path))
    ctx = multiprocessing.get_context("spawn")
    with ProcessPoolExecutor(max_workers, mp_context=ctx) as ex:
        cells = list(ex.map(_load_row, rows))
    return sorted(cells, key=lambda c: c.cell_no)


# ----------------------------------------------------------------------------- epochs

def runs(mask: np.ndarray) -> np.ndarray:
    """Start and stop (exclusive) indices of the runs of True in a boolean array."""
    m = np.r_[False, mask, False].astype(np.int8)
    d = np.diff(m)
    return np.c_[np.flatnonzero(d == 1), np.flatnonzero(d == -1)]


def split_by_trial(cell: Cell, mask: np.ndarray) -> np.ndarray:
    """Runs of a mask that do not cross trial boundaries."""
    m = mask.copy()
    r = runs(m)
    out = []
    bounds = np.r_[cell.seg_start, len(m)]
    for a, b in r:
        ka, kb = cell.trial_of[a], cell.trial_of[b - 1]
        if ka == kb:
            out.append((a, b))
        else:
            cuts = [a] + list(bounds[ka + 1:kb + 1]) + [b]
            out += list(zip(cuts[:-1], cuts[1:]))
    return np.array(out, dtype=int).reshape(-1, 2)


@dataclass
class Touches:
    on: np.ndarray        # sample index of onset
    off: np.ndarray       # sample index of offset (exclusive end)
    trial: np.ndarray
    order: np.ndarray     # order of the touch in its trial, 1 = first
    complete: np.ndarray  # offset found in the trial

    @property
    def dur(self):
        return self.off - self.on


def touches(cell: Cell) -> Touches:
    """Pairs each onset with the next offset in the same trial. An onset without one runs to the
    end of its trial and is marked incomplete."""
    on = np.flatnonzero(cell.touch_on)
    off = np.flatnonzero(cell.touch_off)
    ends = np.r_[cell.seg_start[1:], len(cell.vt)]
    out_off, comp = [], []
    for o in on:
        k = cell.trial_of[o]
        j = np.searchsorted(off, o, side="left")
        if j < len(off) and cell.trial_of[off[j]] == k and off[j] >= o:
            out_off.append(off[j] + 1)
            comp.append(True)
        else:
            out_off.append(ends[k])
            comp.append(False)
    tr = cell.trial_of[on]
    order = np.zeros(len(on), int)
    for k in np.unique(tr):
        w = np.flatnonzero(tr == k)
        order[w] = np.arange(1, len(w) + 1)
    return Touches(on=on, off=np.array(out_off, int), trial=tr, order=order, complete=np.array(comp, bool))


def touch_mask(cell: Cell, T: Touches, max_dur: float | None = None) -> np.ndarray:
    m = np.zeros(len(cell.vt), bool)
    for a, b in zip(T.on, T.off):
        if max_dur is None or b - a <= max_dur:
            m[a:b] = True
    return m


def exploration_mask(cell: Cell, T: Touches) -> np.ndarray:
    """Whisking epochs with touch epochs, leaving out touches > 100 ms, in the sample epoch."""
    touch = touch_mask(cell, T)
    long_touch = touch & ~touch_mask(cell, T, LONG_TOUCH_MS)
    return cell.pole & ~long_touch & ((cell.amp > WHISK_AMP) | touch)


def nonwhisk_mask(cell: Cell, T: Touches) -> np.ndarray:
    """Contiguous periods >= 100 ms with no touch or lick and amplitude < 1.25 deg."""
    base = (cell.amp < NONWHISK_AMP) & ~touch_mask(cell, T) & ~cell.lick
    out = np.zeros_like(base)
    for a, b in split_by_trial(cell, base):
        if b - a >= NONWHISK_MIN_MS:
            out[a:b] = True
    return out


def whisk_mask(cell: Cell, T: Touches, with_touch: bool) -> np.ndarray:
    """Whisking, amplitude > 2.5 deg; read with touch epochs added, or with them left out."""
    touch = touch_mask(cell, T)
    w = cell.amp > WHISK_AMP
    return (w | touch) if with_touch else (w & ~touch)


def cycles(cell: Cell) -> np.ndarray:
    """Whisk cycles: from one wrap of the phase (pi to -pi) to the next, inside one trial.
    Returns start, stop (exclusive) sample indices."""
    ph = cell.phase.astype(float)
    wrap = np.flatnonzero(np.diff(ph) < -np.pi) + 1
    st, en = wrap[:-1], wrap[1:]
    same = cell.trial_of[st] == cell.trial_of[en - 1]
    return np.c_[st[same], en[same]]


def cycle_table(cell: Cell, T: Touches) -> pd.DataFrame:
    """Each cycle with the properties the exclusions use."""
    cyc = cycles(cell)
    ph = cell.phase.astype(float)
    touch = touch_mask(cell, T)
    # samples within 70 ms after the end of a touch (or in it)
    after = touch.copy()
    for b in T.off:
        k = cell.trial_of[min(b, len(after) - 1)]
        e = min(b + AFTER_TOUCH_MS, len(after))
        seg_end = cell.seg_start[k + 1] if k + 1 < len(cell.seg_start) else len(after)
        after[b:min(e, seg_end)] = True
    lick_c = np.r_[0, np.cumsum(cell.lick)]
    after_c = np.r_[0, np.cumsum(after)]
    touch_c = np.r_[0, np.cumsum(touch)]
    pole_c = np.r_[0, np.cumsum(cell.pole)]
    rows = []
    for a, b in cyc:
        amp = cell.amp[a:b]
        d = np.diff(ph[a:b])
        rows.append((a, b, amp.min(), amp.max(), np.all(d >= 0),
                     lick_c[b] - lick_c[a], after_c[b] - after_c[a], touch_c[b] - touch_c[a],
                     pole_c[b] - pole_c[a]))
    df = pd.DataFrame(rows, columns=["start", "stop", "amp_min", "amp_max", "monotonic", "licks",
                                     "after_touch", "touch", "pole"])
    df["dur"] = df.stop - df.start
    df["whisking"] = df.amp_min > WHISK_AMP
    df["valid"] = df.whisking & (df.licks == 0) & (df.after_touch == 0)
    df["phase_ok"] = df.valid & df.monotonic
    df["in_sample"] = df.pole == df.dur
    return df


# ----------------------------------------------------------------------------- spikes

def spike_samples(cell: Cell, svt: np.ndarray) -> np.ndarray:
    """Sample index of each spike given in virtual ms."""
    k = (svt // TRIAL_STRIDE_MS).astype(int)
    return cell.seg_start[k] + np.floor(svt - k * TRIAL_STRIDE_MS).astype(int)


def pcth(cell: Cell, svt: np.ndarray, onsets: np.ndarray, pre: int = PRE_MS, post: int = 50):
    """Peri-contact time histogram, 1 ms bins from -pre to post ms, in spikes per touch per bin.
    Onsets whose window leaves the trial are dropped."""
    on_vt = cell.vt[onsets].astype(float)
    k = (on_vt // TRIAL_STRIDE_MS).astype(int)
    pos = on_vt - k * TRIAL_STRIDE_MS
    nseg = np.diff(np.r_[cell.seg_start, len(cell.vt)])
    keep = (pos - pre >= 0) & (pos + post <= nseg[k])
    on_vt = on_vt[keep]
    edges = np.arange(-pre, post + 1)
    h = np.zeros(len(edges) - 1)
    s = np.sort(svt)
    for o in on_vt:
        a, b = np.searchsorted(s, [o - pre, o + post])
        h += np.histogram(s[a:b] - o, edges)[0]
    return edges[:-1], h / max(len(on_vt), 1), len(on_vt)


def onset_latency(cell: Cell, svt: np.ndarray, onsets: np.ndarray) -> float | None:
    """First 1 ms bin, 0 to 50 ms after onset, above the pre-touch mean plus two s.d."""
    t, h, n = pcth(cell, svt, onsets)
    if n == 0:
        return None
    pre = h[t < 0]
    thr = pre.mean() + 2 * pre.std(ddof=1)
    post = (t >= 0) & (t < LAT_SEARCH_MS)
    above = np.flatnonzero(h[post] > thr)
    return float(t[post][above[0]]) if len(above) else None


def isi_min(cell: Cell, clock: str = "spike") -> float:
    """Shortest interval between spikes of one trial, in ms."""
    t = cell.spike_t
    blk = np.searchsorted(cell.spike_block_t0, t, side="right") - 1
    d = np.diff(t) * 1000
    same = blk[1:] == blk[:-1]
    return float(d[same].min()) if same.any() else np.nan


def nearest_onset_dist(svt: np.ndarray, on_vt: np.ndarray, nearest: str) -> np.ndarray:
    """Time (ms) from the closest touch onset to each spike: 'before' takes the latest onset at
    or before the spike, 'either' the nearest on either side (negative when it follows)."""
    on_vt = np.sort(on_vt)
    j = np.searchsorted(on_vt, svt, side="right") - 1
    d_before = np.where(j >= 0, svt - on_vt[np.clip(j, 0, None)], np.inf)
    if nearest == "before":
        return d_before
    j2 = np.clip(j + 1, 0, len(on_vt) - 1)
    d_after = np.where(j + 1 < len(on_vt), svt - on_vt[j2], -np.inf)
    return np.where(np.abs(d_after) < np.abs(d_before), d_after, d_before)


def _poly_slopes(curves: np.ndarray, tmax: int) -> np.ndarray:
    """Fit each curve (rows) on t = 0..tmax with a degree-11 polynomial; return the increments
    of the fit at t = 1..tmax."""
    t = np.arange(tmax + 1)
    x = 2 * t / tmax - 1
    V = np.polynomial.polynomial.polyvander(x, POLY_DEGREE)
    coef, *_ = np.linalg.lstsq(V, curves.T, rcond=None)
    fit = (V @ coef).T
    return np.diff(fit, axis=1)


def explore_sample_lists(cell: Cell, E: np.ndarray):
    idx = np.flatnonzero(E)
    return idx, cell.trial_of[idx]


def surrogate_spikes(cell: Cell, E_idx: np.ndarray, E_trial: np.ndarray, spk_E: np.ndarray,
                     shuffle: str, rng: np.random.Generator, n: int) -> np.ndarray:
    """n surrogate sets of exploration spike times (virtual ms), shape (n, n_spikes).
    'uniform': spike times drawn uniformly over exploration time. 'circular': each trial's
    spikes shifted by one random amount, circularly, within that trial's exploration time."""
    ns = len(spk_E)
    vt = cell.vt
    if shuffle == "uniform":
        pick = rng.integers(0, len(E_idx), size=(n, ns))
        return vt[E_idx[pick]] + rng.random((n, ns))
    # circular: rank of each spike within its trial's exploration samples
    out = np.empty((n, ns))
    trials_E = np.unique(E_trial)
    first = {k: np.searchsorted(E_trial, k) for k in trials_E}
    count = {k: np.searchsorted(E_trial, k, side="right") - first[k] for k in trials_E}
    E_vt = vt[E_idx].astype(float)
    sk = (spk_E // TRIAL_STRIDE_MS).astype(int)
    for k in np.unique(sk):
        w = np.flatnonzero(sk == k)
        a, m = first[k], count[k]
        ev = E_vt[a:a + m]
        r = np.searchsorted(ev, np.floor(spk_E[w]))  # rank of the sample holding each spike
        frac = spk_E[w] - np.floor(spk_E[w])
        shift = rng.integers(0, m, size=(n, 1))
        rr = (r[None, :] + shift) % m
        out[:, w] = ev[rr] + frac[None, :]
    return out


def _cutoff(slope_d: np.ndarray, p95: np.ndarray, start: str) -> tuple[int, bool]:
    """Index into t = 1..tmax of the cutoff. 'cross', the criterion's: the first increment below
    chance after the increment has been above chance (the transition where the curve levels off,
    Results, paragraph on Figure 3; claim fig3c-touch-spikes-l4c2); when it is never above
    chance, the literal cutoff is used and the second value is False. 'first', a variant only:
    the first increment below chance, read literally from t = 1."""
    below = slope_d < p95
    lit = int(np.flatnonzero(below)[0]) if below.any() else len(below) - 1
    if start == "first":
        return lit, True
    above = np.flatnonzero(~below)
    if len(above) == 0:
        return lit, False
    after = np.flatnonzero(below[above[0]:])
    return (int(above[0] + after[0]) if len(after) else len(below) - 1), True


def window_mask(cell: Cell, T: Touches, latency: float, t_on: float) -> np.ndarray:
    """Samples within [onset + latency, onset + latency + t_on] of any touch, inside its trial."""
    win = np.zeros(len(cell.vt), bool)
    ends = np.r_[cell.seg_start[1:], len(cell.vt)]
    for o in T.on:
        e = ends[cell.trial_of[o]]
        win[o + int(np.ceil(latency)):min(o + int(np.floor(latency + t_on)) + 1, e)] = True
    return win


def _curves(d: np.ndarray, tmax: int) -> np.ndarray:
    """Cumulative counts y(t) = #(0 <= d <= t) for t = 0..tmax, per row of d. Spike and touch
    times lie on a 0.1 ms grid, so d is counted on that grid."""
    d = np.atleast_2d(d)
    q = np.round(d * 10)
    ok = np.isfinite(q) & (q >= 0) & (q <= tmax * 10)
    rows = np.broadcast_to(np.arange(d.shape[0])[:, None], d.shape)[ok]
    K = tmax * 10 + 1
    h = np.bincount(rows * K + q[ok].astype(np.int64), minlength=d.shape[0] * K).reshape(d.shape[0], K)
    return np.cumsum(h, axis=1)[:, ::10].astype(float)


def _cutoffs(y: np.ndarray, ys: np.ndarray, tmax: int) -> dict:
    slope_d = _poly_slopes(y[None, :], tmax)[0]
    p95 = np.percentile(_poly_slopes(ys, tmax), 95, axis=0)
    out = {}
    for start in ("first", "cross"):
        i, crossed = _cutoff(slope_d, p95, start)
        out[start] = (i + 1, crossed)
    return out


def touch_window(cell: Cell, svt: np.ndarray, T: Touches, E: np.ndarray, latency: float,
                 shuffle: str, nearest: str, tmax: int, rng: np.random.Generator,
                 n_sur: int = N_SURROGATES) -> dict:
    """Touch response cutoff t_on and the touch-coupled fractions (Methods, Spikes accounted by
    active sensation; claim fig3c-touch-spikes-l4c2), for both readings of where the search for
    the cutoff starts (see _cutoff). Returns {start: result}."""
    si = spike_samples(cell, svt)
    spk_E = svt[E[si]]
    on_vt = cell.vt[T.on].astype(float)
    d = nearest_onset_dist(spk_E, on_vt, nearest) - latency
    y = _curves(d, tmax)[0]
    E_idx, E_trial = explore_sample_lists(cell, E)
    base = dict(n_spikes=len(spk_E), explore_ms=int(E.sum()), latency=latency)
    if len(spk_E) == 0:
        return {k: dict(base, t_on=np.nan, frac_spikes=np.nan, frac_time=np.nan, crossed=False)
                for k in ("first", "cross")}
    sur = surrogate_spikes(cell, E_idx, E_trial, spk_E, shuffle, rng, n_sur)
    ds = nearest_onset_dist(sur.ravel(), on_vt, nearest).reshape(sur.shape) - latency
    ys = _curves(ds, tmax)
    out = {}
    for start, (t_on, crossed) in _cutoffs(y, ys, tmax).items():
        win = window_mask(cell, T, latency, t_on)
        out[start] = dict(base, t_on=t_on, n_touch_spikes=int(y[t_on]),
                          frac_spikes=y[t_on] / len(spk_E),
                          frac_time=(win & E).sum() / E.sum(), crossed=crossed)
    return out


def preferred_phase_times(cell: Cell, cyc: pd.DataFrame, phi: float) -> tuple[np.ndarray, np.ndarray]:
    """Virtual time at which each cycle's phase first reaches phi (linear interpolation), and the
    row of the cycle it belongs to; cycles that never reach it are left out."""
    ph = cell.phase.astype(float)
    times, rows = [], []
    for r, (a, b) in enumerate(zip(cyc.start.to_numpy(), cyc.stop.to_numpy())):
        seg = ph[a:b]
        j = np.flatnonzero(seg >= phi)
        if len(j) == 0:
            continue
        j = j[0]
        if j == 0:
            times.append(float(cell.vt[a]))
        else:
            p0, p1 = seg[j - 1], seg[j]
            times.append(float(cell.vt[a + j - 1]) + (phi - p0) / (p1 - p0 if p1 != p0 else 1))
        rows.append(r)
    return np.array(times), np.array(rows, int)


def phase_window(cell: Cell, svt: np.ndarray, T: Touches, E: np.ndarray, latency: float,
                 t_on_by_start: dict, nearest: str, phi: float, cyc: pd.DataFrame, shuffle: str,
                 tmax: int, width: str, rng: np.random.Generator, n_sur: int = N_SURROGATES) -> dict:
    """Spikes coupled to whisking phase after the touch spikes are taken out (Methods; claim
    fig3d-touch-phase-l4c2). The spikes left are indexed by the time to the closest preferred-phase
    time of a whisking cycle; the cutoff t_w follows the same rule as for touch, for each reading
    of where the search starts (t_on_by_start gives the touch cutoff of the same reading). width
    'pm' reads the window as +-t_w around the preferred phase, 'total' as t_w wide in all.
    Phase windows are truncated at the margins of their cycle (Figure 3B legend)."""
    si = spike_samples(cell, svt)
    spk_E = svt[E[si]]
    on_vt = cell.vt[T.on].astype(float)
    d_touch = nearest_onset_dist(spk_E, on_vt, nearest) - latency
    pt, prow = preferred_phase_times(cell, cyc, phi)
    pt_sorted = np.sort(pt)
    scale = 1.0 if width == "pm" else 2.0
    starts, stops = cyc.start.to_numpy()[prow], cyc.stop.to_numpy()[prow]
    out = {}
    for start, t_on in t_on_by_start.items():
        twin = window_mask(cell, T, latency, t_on)
        is_touch = (d_touch >= 0) & (d_touch <= t_on)
        rest = spk_E[~is_touch]
        n_touch = int(is_touch.sum())
        if len(rest) == 0 or len(pt) == 0:
            out[start] = dict(t_w=np.nan, frac_spikes=n_touch / max(len(spk_E), 1),
                              frac_time=(twin & E).sum() / E.sum(), crossed=False)
            continue

        def dist(x):
            j = np.clip(np.searchsorted(pt_sorted, x), 1, len(pt_sorted) - 1)
            return scale * np.minimum(np.abs(x - pt_sorted[j - 1]), np.abs(pt_sorted[j] - x))
        y = _curves(dist(rest), tmax)[0]
        space = E & ~twin
        E_idx, E_trial = explore_sample_lists(cell, space)
        sur = surrogate_spikes(cell, E_idx, E_trial, rest, shuffle, rng, n_sur)
        ys = _curves(dist(sur.ravel()).reshape(sur.shape), tmax)
        t_w, crossed = _cutoffs(y, ys, tmax)[start]
        half = t_w / scale
        pwin = np.zeros(len(E), bool)
        vt0 = cell.vt.astype(float)
        for p, a, b in zip(pt, starts, stops):
            base = p - vt0[a]
            lo = a + max(int(np.ceil(base - half)), 0)
            hi = a + min(int(np.floor(base + half)) + 1, b - a)
            if hi > lo:
                pwin[lo:hi] = True
        n_phase = int(y[t_w])
        out[start] = dict(t_w=t_w, n_phase_spikes=n_phase, crossed=crossed,
                          frac_spikes=(n_touch + n_phase) / len(spk_E),
                          frac_time=((twin | pwin) & E).sum() / E.sum())
    return out


def spikes_per_touch(cell: Cell, svt: np.ndarray, T: Touches, latency: float, t_on: float):
    """Spike count in [onset + latency, onset + latency + t_on] for each touch."""
    s = np.sort(svt)
    on_vt = cell.vt[T.on].astype(float)
    a = np.searchsorted(s, on_vt + latency, side="left")
    b = np.searchsorted(s, on_vt + latency + t_on, side="right")
    return b - a


def counts_in(svt_sorted: np.ndarray, start_vt: np.ndarray, length: float) -> np.ndarray:
    a = np.searchsorted(svt_sorted, start_vt, side="left")
    b = np.searchsorted(svt_sorted, start_vt + length, side="left")
    return b - a


def fano(x: np.ndarray) -> float:
    x = np.asarray(x, float)
    m = x.mean() if len(x) else np.nan
    return x.var(ddof=1) / m if len(x) > 1 and m > 0 else np.nan


def binomial_limit(m):
    """Smallest possible Fano factor of whole-number counts with mean m (1 - m for m < 1)."""
    m = np.asarray(m, float)
    f = m - np.floor(m)
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(m > 0, f * (1 - f) / m, np.nan)


# ----------------------------------------------------------------------------- phase

def spike_phase(cell: Cell, svt: np.ndarray) -> np.ndarray:
    """Phase at each spike by linear interpolation between samples (unwrapped across a wrap)."""
    si = spike_samples(cell, svt)
    frac = svt - np.floor(svt)
    p0 = cell.phase[si].astype(float)
    nxt = np.minimum(si + 1, len(cell.phase) - 1)
    p1 = cell.phase[nxt].astype(float)
    dp = np.angle(np.exp(1j * (p1 - p0)))
    return np.angle(np.exp(1j * (p0 + frac * dp)))


def cos_fit(centers: np.ndarray, rate: np.ndarray):
    """Fit A[1 + cos(x - phi)] + B with A, B >= 0 by least squares; return A, B, phi, depth."""
    def resid(p):
        A, B, phi = p
        return A * (1 + np.cos(centers - phi)) + B - rate
    best = None
    for phi0 in np.linspace(-np.pi, np.pi, 8, endpoint=False):
        r = least_squares(resid, [max(rate.max() - rate.min(), 1e-6) / 2, max(rate.min(), 0), phi0],
                          bounds=([0, 0, -10], [np.inf, np.inf, 10]))
        if best is None or r.cost < best.cost:
            best = r
    A, B, phi = best.x
    phi = float(np.angle(np.exp(1j * phi)))
    depth = A / (A + B) if A + B > 0 else np.nan
    return A, B, phi, depth


def phase_tuning(cell: Cell, svt: np.ndarray, cyc: pd.DataFrame, sample_mask: np.ndarray,
                 nbins: int = N_PHASE_BINS):
    """Rate in phase bins over the samples of the given cycles that are also in sample_mask."""
    m = np.zeros(len(cell.vt), bool)
    for a, b in zip(cyc.start, cyc.stop):
        m[a:b] = True
    m &= sample_mask
    edges = np.linspace(-np.pi, np.pi, nbins + 1)
    occ = np.histogram(cell.phase[m], edges)[0] / 1000.0   # s
    si = spike_samples(cell, svt)
    sp = svt[m[si]]
    cnt = np.histogram(spike_phase(cell, sp), edges)[0]
    with np.errstate(invalid="ignore", divide="ignore"):
        rate = cnt / occ
    centers = (edges[:-1] + edges[1:]) / 2
    return centers, rate, cnt, occ


# ----------------------------------------------------------------------------- behaviour

def bandpassed_theta(cell: Cell) -> np.ndarray:
    """The 6 to 60 Hz band-passed angle, rebuilt from the stored Hilbert amplitude and phase
    (amplitude * cos(phase)); in 38 of the 52 files the stored `theta_filt` is not that signal."""
    return cell.amp.astype(float) * np.cos(cell.phase.astype(float))


def bouts(cell: Cell, T: Touches, touch_breaks: bool, cyc: pd.DataFrame) -> pd.DataFrame:
    """Contiguous runs of amplitude > 2.5 deg inside one trial (touch samples break a run when
    touch_breaks). Per bout: duration (ms), maximum Hilbert amplitude, number of complete
    whisking cycles inside, and the largest range of band-passed theta over those cycles (over
    the whole bout when it holds no complete cycle)."""
    m = cell.amp > WHISK_AMP
    if touch_breaks:
        m &= ~touch_mask(cell, T)
    bp = bandpassed_theta(cell)
    wc = cyc[cyc.whisking]
    cs, ce = wc.start.to_numpy(), wc.stop.to_numpy()
    rows = []
    for a, b in split_by_trial(cell, m):
        i0, i1 = np.searchsorted(cs, a), np.searchsorted(cs, b)
        inside = [(s, e) for s, e in zip(cs[i0:i1], ce[i0:i1]) if e <= b]
        if inside:
            p2p = max(bp[s:e].max() - bp[s:e].min() for s, e in inside)
        else:
            p2p = bp[a:b].max() - bp[a:b].min()
        rows.append((a, b, b - a, float(cell.amp[a:b].max()), len(inside), float(p2p)))
    return pd.DataFrame(rows, columns=["start", "stop", "dur", "amp_max", "n_cycles", "p2p_cycle"])


def rate_in(cell: Cell, svt: np.ndarray, mask: np.ndarray) -> float:
    si = spike_samples(cell, svt)
    n = mask.sum()
    return float(mask[si].sum() / (n / 1000.0)) if n else np.nan


# ----------------------------------------------------------------------------- touch responses

def touch_responses(cell: Cell, svt: np.ndarray, T: Touches, pre: int = 30, post: int = 50,
                    exclude_next: int = 50) -> np.ndarray:
    """Spike counts in 1 ms bins from -pre to +post ms around each touch onset, leaving out
    touches followed by another onset within exclude_next ms, and touches whose window leaves
    the trial (Methods, Population decoding). Shape (n_touches, pre + post)."""
    s = np.sort(svt)
    on_vt = cell.vt[T.on].astype(float)
    nxt = np.r_[on_vt[1:] - on_vt[:-1], np.inf]
    same_next = np.r_[T.trial[1:] == T.trial[:-1], False]
    k = (on_vt // TRIAL_STRIDE_MS).astype(int)
    pos = on_vt - k * TRIAL_STRIDE_MS
    nseg = np.diff(np.r_[cell.seg_start, len(cell.vt)])
    keep = ~(same_next & (nxt <= exclude_next)) & (pos - pre >= 0) & (pos + post <= nseg[k])
    edges = np.arange(-pre, post + 1)
    out = []
    for o in on_vt[keep]:
        a, b = np.searchsorted(s, [o - pre, o + post])
        out.append(np.histogram(s[a:b] - o, edges)[0])
    return np.array(out, dtype=np.int16).reshape(-1, pre + post)


def causal_integrate(r: np.ndarray, w: int = 10) -> np.ndarray:
    """Sum of the last w bins at each bin (the first w - 1 bins are partial sums)."""
    c = np.cumsum(r, axis=-1)
    out = c.copy()
    out[..., w:] = c[..., w:] - c[..., :-w]
    return out


def ici(T: Touches, cell: Cell, since: str) -> np.ndarray:
    """Inter-contact interval before each touch (ms): from the previous touch's offset
    ('offset') or onset ('onset') in the same trial; infinite for the first touch of a trial."""
    prev = np.r_[-1, np.arange(len(T.on) - 1)]
    same = np.r_[False, T.trial[1:] == T.trial[:-1]]
    ref = T.off if since == "offset" else T.on
    out = np.full(len(T.on), np.inf)
    out[same] = T.on[same] - ref[prev[same]]
    return out


def touch_velocity(cell: Cell, T: Touches, frame: str) -> np.ndarray:
    """d theta / dt in deg/ms, at the onset frame ('onset': theta[on] - theta[on-1]) or in the
    frame before it ('before': theta[on-1] - theta[on-2])."""
    th = cell.theta.astype(float)
    on = T.on
    if frame == "onset":
        return th[on] - th[np.maximum(on - 1, 0)]
    return th[np.maximum(on - 1, 0)] - th[np.maximum(on - 2, 0)]


def touch_max_dkappa(cell: Cell, T: Touches, span: str) -> np.ndarray:
    """Maximum |delta kappa| over the whole touch ('touch') or 0 to 20 ms after onset ('0-20')."""
    dk = np.abs(cell.dkappa.astype(float))
    ends = np.r_[cell.seg_start[1:], len(cell.vt)]
    out = np.empty(len(T.on))
    for i, (a, b) in enumerate(zip(T.on, T.off)):
        e = b if span == "touch" else min(a + 21, ends[cell.trial_of[a]])
        out[i] = dk[a:max(e, a + 1)].max()
    return out


# ----------------------------------------------------------------------------- touch groups

def optics_groups(X: np.ndarray, n_per: int, n_groups: int, min_samples: int) -> list[np.ndarray]:
    """Methods, Analysis of spike count variance: order the points with OPTICS, take the run of
    n_per consecutive ordered points with the smallest sum of pairwise distances as a group,
    remove it and repeat. Returns the indices of each group (fewer groups when points run out)."""
    from sklearn.cluster import OPTICS
    from scipy.spatial.distance import pdist, squareform
    left = np.arange(len(X))
    groups = []
    for _ in range(n_groups):
        if len(left) < n_per:
            break
        ms = min(max(min_samples, 2), len(left))
        order = OPTICS(min_samples=ms).fit(X[left]).ordering_
        P = X[left][order]
        D = squareform(pdist(P))
        # sum over pairs inside each window of n_per consecutive points
        c = np.cumsum(np.cumsum(D, 0), 1)
        c = np.pad(c, ((1, 0), (1, 0)))
        i = np.arange(len(P) - n_per + 1)
        j = i + n_per
        s = c[j, j] - c[i, j] - c[j, i] + c[i, i]
        best = int(np.argmin(s))
        g = left[order[best:best + n_per]]
        groups.append(g)
        left = np.setdiff1d(left, g)
    return groups


def window_counts(cell: Cell, svt: np.ndarray, onsets: np.ndarray, starts: np.ndarray,
                  width: float) -> np.ndarray:
    """Spike counts in [onset + s, onset + s + width) for each onset (rows) and start s (cols)."""
    s = np.sort(svt)
    on_vt = cell.vt[onsets].astype(float)
    st = on_vt[:, None] + starts[None, :]
    return counts_in(s, st.ravel(), width).reshape(st.shape)


# ----------------------------------------------------------------------------- decoders

def nontouch_windows(cell: Cell, svt: np.ndarray, T: Touches, E: np.ndarray, w: int = 10,
                     guard_before: int = 50, guard_after: int = 100) -> np.ndarray:
    """Spike counts in every non-overlapping w ms window of exploration time that holds no touch
    and lies more than guard_after ms after and guard_before ms before any touch onset (a
    standard choice for "epochs without touch", claim fig4a reading (1b))."""
    near = np.zeros(len(E), bool)
    ends = np.r_[cell.seg_start[1:], len(cell.vt)]
    for o in T.on:
        e = ends[cell.trial_of[o]]
        near[max(o - guard_before - w, cell.seg_start[cell.trial_of[o]]):min(o + guard_after, e)] = True
    ok = E & ~near & ~touch_mask(cell, T)
    s = np.sort(svt)
    starts = []
    for a, b in split_by_trial(cell, ok):
        starts += list(range(a, b - w + 1, w))
    starts = np.array(starts, int)
    return counts_in(s, cell.vt[starts].astype(float), w) if len(starts) else np.zeros(0, int)


def touch_detection(I_list, Q_list, N, rng, n_resp=1000, reps=50):
    """Pooled-count touch detector (Methods, Population decoding). I_list: per neuron, causally
    integrated touch responses (n_touch x n_bins); Q_list: per neuron, dict of non-touch count
    arrays by reading. For each repetition, N neurons drawn with replacement and n_resp responses
    per neuron with replacement; the threshold maximising percent correct on the first half, the
    performance on the second half. Returns {reading: (reps, n_post_bins, 2)} with the hit rate
    and percent correct at each post-touch bin."""
    keys = list(Q_list[0].keys())
    post = slice(30, None)
    out = {k: [] for k in keys}
    h = n_resp // 2
    for _ in range(reps):
        neu = rng.integers(0, len(I_list), N)
        P = 0
        Q = {k: 0 for k in keys}
        for i in neu:
            Ii = I_list[i]
            P = P + Ii[rng.integers(0, len(Ii), n_resp)][:, post]
            for k in keys:
                q = Q_list[i][k]
                Q[k] = Q[k] + q[rng.integers(0, len(q), n_resp)]
        for k in keys:
            q = Q[k]
            res = np.empty((P.shape[1], 2))
            for j in range(P.shape[1]):
                p = P[:, j]
                cand = np.unique(np.r_[p[:h], q[:h]]) + 0.5
                cand = np.r_[cand.min() - 1, cand]
                hit = (p[:h, None] > cand[None, :]).mean(0)
                cr = (q[:h, None] < cand[None, :]).mean(0)
                th = cand[np.argmax((hit + cr) / 2)]
                hit_t = (p[h:] > th).mean()
                cr_t = (q[h:] < th).mean()
                res[j] = hit_t, (hit_t + cr_t) / 2
            out[k].append(res)
    return {k: np.array(v) for k, v in out.items()}


def time_decoding(I_list, rng, N=200, n_resp=1000, reps=100, split="half", t0_bin=9, alpha=1.0):
    """Multinomial naive Bayes decoding of the time since touch from the 10 ms integrated
    responses of N neurons (Methods, Population decoding), written out as scikit-learn's
    MultinomialNB with its default smoothing alpha = 1 and equal class priors. Classes are the
    bins from t0_bin to the last (bin j holds the window ending at j - 30 + 1 ms, labelled j - 30
    ms). Training and test sets are the two halves of n_resp draws ('half') or two independent
    sets of n_resp draws ('independent'). Returns decoded and true times (ms) of the test
    samples, pooled over repetitions, and the repetition index."""
    nb = I_list[0].shape[1]
    cls = np.arange(t0_bin, nb)
    tt = cls - 30
    dec_all, true_all, rep_all = [], [], []
    for r in range(reps):
        neu = rng.integers(0, len(I_list), N)

        def draw(n):
            return np.stack([I_list[i][rng.integers(0, len(I_list[i]), n)][:, cls] for i in neu],
                            axis=2).astype(np.float32)   # (n, n_cls, N)
        if split == "half":
            X = draw(n_resp)
            Xtr, Xte = X[: n_resp // 2], X[n_resp // 2:]
        else:
            Xtr, Xte = draw(n_resp), draw(n_resp)
        fc = Xtr.sum(0) + alpha                                  # (n_cls, N)
        flp = np.log(fc) - np.log(fc.sum(1, keepdims=True))
        ll = Xte.reshape(-1, N) @ flp.T                          # (n_test * n_cls, n_cls)
        d = tt[np.argmax(ll, axis=1)]
        dec_all.append(d)
        true_all.append(np.broadcast_to(tt, Xte.shape[:2]).ravel())
        rep_all.append(np.full(d.shape, r))
    return np.concatenate(dec_all), np.concatenate(true_all), np.concatenate(rep_all)


def cycle_bin_counts(cell: Cell, svt: np.ndarray, cyc: pd.DataFrame, nbins: int = 120):
    """Spike counts per whisk cycle (rows) and phase bin (120 bins over -pi to pi)."""
    si = spike_samples(cell, svt)
    starts, stops = cyc.start.to_numpy(), cyc.stop.to_numpy()
    j = np.searchsorted(starts, si, side="right") - 1
    ok = (j >= 0) & (si < stops[np.clip(j, 0, None)])
    ph = spike_phase(cell, svt[ok])
    b = np.clip(((ph + np.pi) / (2 * np.pi) * nbins).astype(int), 0, nbins - 1)
    C = np.zeros((len(cyc), nbins), np.int16)
    np.add.at(C, (j[ok], b), 1)
    return C


def phase_discrimination(C_list, pref, rng, N=1000, reps=100, model="cycles", shifts="random",
                         deltas=np.arange(2, 61, 2), M=50, smooth="add_one"):
    """Naive Bayes (Poisson) discrimination of two whisking phases from N neurons drawn with
    replacement, their tuning circularly shifted to give uniformly distributed preferred phases
    (Methods, Population decoding). C_list: per recorded cell, cycles x 120 bins counts; pref:
    preferred phase (rad). model 'cycles': test responses are the counts of held-out cycles, the
    rates learned on the other half (one split per recorded cell and repetition, shared by the
    neurons drawn from it); 'poisson': responses drawn as Poisson counts with the cycle-averaged
    rates. Returns per repetition the phase difference (deg) reaching 76% correct (nan when none
    does) and the percent-correct curves.

    Bins with no spikes (claim fig4c-phase-decoding, open detail 3, which the paper does not
    treat): 'add_one' adds one spike to every bin's count over the training cycles (Laplace);
    'floor' raises each bin's rate to at least one spike over all of the cell's training cycles
    and bins, 1 / (120 n), a value of our choosing as the paper gives none; 'spread' adds one
    spike spread over the 120 bins (the earlier run's choice, kept as a variant)."""
    nbins = C_list[0].shape[1]
    res, curves = [], []
    for _ in range(reps):
        neu = rng.integers(0, len(C_list), N)
        target = rng.uniform(-np.pi, np.pi, N) if shifts == "random" else np.linspace(-np.pi, np.pi, N, endpoint=False)
        sh = np.round((target - pref[neu]) / (2 * np.pi) * nbins).astype(int)
        lam_cell, test_cell = [], []
        for C in C_list:
            if model == "cycles":
                perm = rng.permutation(len(C))
                tr, te = C[perm[: len(C) // 2]], C[perm[len(C) // 2:]]
            else:
                tr, te = C, None
            n = max(len(tr), 1)
            if smooth == "add_one":
                lam_cell.append((tr.sum(0) + 1.0) / n)
            elif smooth == "floor":
                lam_cell.append(np.maximum(tr.sum(0) / n, 1.0 / (nbins * n)))
            else:
                lam_cell.append((tr.sum(0) + 1.0 / nbins) / n)
            test_cell.append(te)
        lam_cell = np.array(lam_cell)
        bins = np.arange(nbins)
        lam = lam_cell[neu[:, None], (bins[None, :] - sh[:, None]) % nbins]   # (N, nbins)
        loglam = np.log(lam)
        groups = [np.flatnonzero(neu == i) for i in range(len(C_list))]
        pc = []
        for dl in deltas:
            b1 = rng.integers(0, nbins, M)
            b2 = (b1 + dl) % nbins
            correct = 0.0
            for true_b, other_b in ((b1, b2), (b2, b1)):
                if model == "cycles":
                    X = np.zeros((M, N))
                    for i, g in enumerate(groups):
                        if len(g) == 0:
                            continue
                        te = test_cell[i]
                        rc = rng.integers(0, len(te), (M, len(g)))
                        X[:, g] = te[rc, (true_b[:, None] - sh[g][None, :]) % nbins]
                else:
                    X = rng.poisson(lam[:, true_b].T)
                w = loglam[:, true_b].T - loglam[:, other_b].T     # (M, N)
                c = lam[:, true_b].T - lam[:, other_b].T
                llr = (X * w).sum(1) - c.sum(1)
                correct += np.sum(llr > 0) + 0.5 * np.sum(llr == 0)
            pc.append(correct / (2 * M))
        pc = np.array(pc)
        ok = np.flatnonzero(pc >= 0.76)
        if len(ok) == 0:
            res.append(np.nan)
        elif ok[0] == 0:
            res.append(deltas[0] * 360 / nbins)
        else:
            i = ok[0]
            x0, x1 = deltas[i - 1], deltas[i]
            y0, y1 = pc[i - 1], pc[i]
            res.append((x0 + (0.76 - y0) / (y1 - y0) * (x1 - x0)) * 360 / nbins)
        curves.append(pc)
    return np.array(res), np.array(curves)


# ----------------------------------------------------------------------------- per-file checks

def _check_series(row) -> dict:
    """theta_filt against amplitude * cos(phase) over the first 20 s of behaviour, and the
    voltage range over the first 10 s, with its stated conversion and unit."""
    asset_id, path = row
    f = h5py.File(remfile.File(f"{API}/assets/{asset_id}/download/"), "r")
    b = f["acquisition/behavior"]
    n = 20000
    tf = b["theta_filt/data"][:n]
    bp = b["amplitude/data"][:n] * np.cos(b["phase/data"][:n])
    sp = b["set_point/data"][:n]
    th = b["theta_at_base/data"][:n]
    v = f["acquisition/CurrentClampSeries"]
    vv = v["data"][:100000]
    out = dict(path=path, theta_filt_r=float(np.corrcoef(tf, bp)[0, 1]), theta_filt_maxdiff=float(np.abs(tf - bp).max()),
               set_point_r=float(np.corrcoef(sp, th - bp)[0, 1]),
               volt_ptp_stored=float(np.ptp(vv)), volt_conversion=float(v["data"].attrs["conversion"]),
               volt_unit=str(v["data"].attrs["unit"]), file_name_ogen="ogen" in path,
               stimulus_groups=len(f["stimulus/presentation"].keys()))
    f.close()
    return out


def check_series_all(max_workers: int = 8) -> pd.DataFrame:
    assets = list_assets()
    ctx = multiprocessing.get_context("spawn")
    with ProcessPoolExecutor(max_workers, mp_context=ctx) as ex:
        rows = list(ex.map(_check_series, list(zip(assets.asset_id, assets.path))))
    return pd.DataFrame(rows)
