"""Loading and measures for the simulated mouse M1 of dandiset 001444.

Doherty, Chen, Smith, Wichmann, Chu & Lytton (2025), npj Parkinson's Disease 11, 230,
doi:10.1038/s41531-025-01070-4. Claims: claims/001444/10.1038-s41531-025-01070-4.yaml.

Each NWB file is one 4.3 s NetPyNE simulation. It holds a units table whose `_name` is
"<population> <gid>" (M1 cells and the Poisson input generators), one LFP trace
("Segment 0 LFP 0", 40 kHz, mV) and somatic membrane potentials of some PT5B cells
("Segment 0 PT5B <gid> <n>", 40 kHz, mV). Spike times are in seconds. Files are streamed from
the archive at the pinned version; nothing is written to disk.

Where the parameters come from:

- `WINDOW` (2.0 to 4.3 s): the claims file's window W, from the Fig. 2C and 5C legends ("the
  last 2.3 s of 4.3 s simulation") and the Fig. 3 and 6 legends ("2.3 s of activity starting
  2 s after simulation initiation").
- `SCH_BIN` (2 ms): the PT5B spike count histogram of the Fig. 2 and 5 legends ("2 ms bins").
- `M1_POPS` and their order: the 15 M1 populations of the model (claims file, cfg.py allpops).
  The files hold only cells that fired (data check), so the size of each population is taken
  from the data: gids are numbered in contiguous blocks per population (NetPyNE), and
  `population_blocks` bounds each block by the gids seen in all 16 files. Where a few gids
  between two blocks were never seen, the lower and upper sizes are both kept.
- Rate readings R1 (all cells of a population) and R2 (cells with a spike in W), and test
  readings T1 to T4: the claims file's definitions. R3 (the cells the file holds, those that
  fired at least once in the simulation) is a variant found in the data, shown beside them.
- `welch_peak`: Welch's method with 1 s segments, the claims file's standard choice.
- `morlet_spec`: a copy of netpyne/support/morlet.py of NetPyNE 1.0.5 (the version the Methods
  name), with the defaults of netpyne.analysis.lfp.prepareSpectrogram (1 to 100 Hz in 1 Hz
  steps, 7 cycles; the signal has its mean removed and is linearly detrended). Reading S1.
- `stft_spec`: reading S2. NetPyNE's fft option with its defaults (nperseg 256 at 40 kHz) has a
  frequency step of 156 Hz and cannot resolve any band of the claims, so S2 uses a 250 ms Hann
  window with 90% overlap (4 Hz steps), a standard choice stated in the notebook.
- `band_bursts`: the claims file's burst reading, epochs where band power is above halfway
  between its minimum and maximum in W (the half-height convention of Methods, Duty cycle).
- `duty_cycles`: Results, Control simulations, paragraph 4, and Methods, Duty cycle, with the
  readings of the claims file (half-height global or per period; mean of periods or total).
- `coincident_fraction`: Results, Control simulations, paragraph 7 ("within a 1 ms time window"),
  readings (a) another PT5B spike within 1 ms either side and (b) the same 1 ms bin.
- `unitary_events`: Methods, Identifying synchronous spiking, and the Fig. 4 and 7 legends
  (joint-surprise test, p < 0.05, "100 ms firing rate window"), readings of the claims file. The
  expected number of coincidences in a window assumes independent Poisson cells at the rates
  of that window (Grun et al. 2002); coincidence bins are 1 ms (Results).
"""

from __future__ import annotations

from functools import lru_cache

import h5py
import numpy as np
import remfile
import requests
import scipy.signal as sps
from scipy import stats

DANDISET_ID = "001444"
DANDISET_VERSION = "0.250805.2002"
API = "https://api.dandiarchive.org/api"

PAPER_SET = "sM1-12-12-2023"
CONDITIONS = {"01": "control rest", "02": "parkinsonian rest",
              "03": "control activated", "04": "parkinsonian activated"}
SETS = ["sM1-12-12-2023", "sM1-04-22-2024", "sM1-04-25-2024", "sM1-04-26-2024"]

DURATION = 4.3
WINDOW = (2.0, 4.3)
SCH_BIN = 0.002
FS = 40000.0
M1_POPS = ["IT2", "SOM2", "PV2", "IT4", "IT5A", "SOM5A", "PV5A", "IT5B", "PT5B", "SOM5B",
           "PV5B", "IT6", "CT6", "SOM6", "PV6"]
EXCITATORY = ["IT2", "IT4", "IT5A", "IT5B", "PT5B", "IT6", "CT6"]
FIRST_INPUT_GID = 10073


# ---------------------------------------------------------------- loading

@lru_cache(maxsize=1)
def assets() -> dict:
    """Path -> (asset id, blob id, size) for the pinned version."""
    out, url = {}, f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/"
    params = {"page_size": 200}
    while url:
        page = requests.get(url, params=params, timeout=60).json()
        for a in page["results"]:
            out[a["path"]] = (a["asset_id"], a.get("blob"), a["size"])
        url, params = page.get("next"), None
    return out


def path_of(set_name: str, cond: str) -> str:
    return f"sub-001/sub-001_ses-{set_name}-{cond}.nwb"


def open_nwb(path: str) -> h5py.File:
    asset_id = assets()[path][0]
    s3 = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60).url
    return h5py.File(remfile.File(s3), "r")


def read_units(f: h5py.File) -> dict:
    """Spike trains by gid, with population names. Times in seconds."""
    names = f["units/_name"][:].astype(str)
    st = f["units/spike_times"][:]
    idx = f["units/spike_times_index"][:]
    starts = np.r_[0, idx[:-1]]
    pops = np.array([n.rsplit(" ", 1)[0] for n in names])
    gids = np.array([int(n.rsplit(" ", 1)[1]) for n in names])
    trains = {int(g): np.sort(st[a:b]) for g, a, b in zip(gids, starts, idx)}
    return {"pop": dict(zip(gids.tolist(), pops.tolist())), "trains": trains,
            "unsorted": int(sum(np.any(np.diff(st[a:b]) < 0) for a, b in zip(starts, idx))),
            "obs_intervals": np.unique(f["units/obs_intervals"][:], axis=0)}


def read_meta(f: h5py.File) -> dict:
    g = lambda k: f[k][()].decode() if isinstance(f[k][()], bytes) else f[k][()]
    return {"session_id": g("general/session_id"), "description": g("session_description"),
            "start": g("session_start_time")}


def vm_names(f: h5py.File) -> list[str]:
    return [k for k in f["acquisition"] if " PT5B " in k]


def read_series(f: h5py.File, name: str, window=None) -> tuple[np.ndarray, float, str]:
    ts = f["acquisition"][name]
    rate = float(ts["starting_time"].attrs["rate"])
    t0 = float(ts["starting_time"][()])
    d = ts["data"]
    if window is None:
        x = d[:, 0]
    else:
        a, b = int(round((window[0] - t0) * rate)), int(round((window[1] - t0) * rate))
        x = d[a:b, 0]
    return np.asarray(x, float), rate, ts["data"].attrs["unit"]


def load_file(set_name: str, cond: str, lfp=True, vm=True) -> dict:
    path = path_of(set_name, cond)
    f = open_nwb(path)
    out = {"path": path, "set": set_name, "cond": cond, **read_meta(f), **read_units(f)}
    if lfp:
        out["lfp"], out["lfp_rate"], out["lfp_unit"] = read_series(f, "Segment 0 LFP 0")
        out["lfp_t0"] = float(f["acquisition/Segment 0 LFP 0/starting_time"][()])
    names = vm_names(f)
    out["vm_gids"] = [int(n.split()[3]) for n in names]
    if vm:
        out["vm"] = {int(n.split()[3]): read_series(f, n)[0] for n in names}
    out["n_acquisition"] = len(f["acquisition"])
    return out


def load_vm_subset(set_name: str, cond: str, n: int, window=None) -> dict:
    """The first `n` PT5B membrane potentials of a file (gid -> trace), optionally in a window."""
    f = open_nwb(path_of(set_name, cond))
    return {int(k.split()[3]): read_series(f, k, window)[0] for k in vm_names(f)[:n]}


def vm_match(vm: dict, trains: dict, t0: float = 0.0, spans=((0, 0.5), (0.5, 2.0), (2.0, 4.3)),
             tol: float = 0.0005) -> list[dict]:
    """For each trace, the share of the same gid's unit spikes that have an upward 0 mV crossing
    of the trace within `tol` s, in each span of time. `t0` is the time of the trace's first
    sample."""
    rows = []
    for g, v in vm.items():
        sv = vm_spikes(v) + t0
        su = trains.get(g, np.array([]))
        row = {"gid": g, "Vm spikes": len(sv), "unit spikes": len(su)}
        for a, b in spans:
            u = su[(su >= a) & (su < b)]
            if len(u) and len(sv):
                row[f"{a}-{b} s"] = float(np.mean([np.min(np.abs(sv - x)) < tol for x in u]))
            else:
                row[f"{a}-{b} s"] = np.nan
        rows.append(row)
    return rows


# ---------------------------------------------------------------- populations

def population_blocks(pop_maps: list[dict]) -> dict:
    """Bound each M1 population's gid block from the gids seen in any file.

    Returns pop -> (low_start, high_start, low_end, high_end, n_min, n_max): the block starts
    somewhere in [low_start, high_start] and ends in [low_end, high_end].
    """
    seen = {}
    for m in pop_maps:
        for g, p in m.items():
            if p in M1_POPS:
                lo, hi = seen.get(p, (g, g))
                seen[p] = (min(lo, g), max(hi, g))
    order = sorted(seen, key=lambda p: seen[p][0])
    assert order == M1_POPS, order
    out = {}
    for i, p in enumerate(order):
        lo, hi = seen[p]
        prev_hi = seen[order[i - 1]][1] if i else -1
        next_lo = seen[order[i + 1]][0] if i + 1 < len(order) else FIRST_INPUT_GID
        out[p] = (prev_hi + 1, lo, hi, next_lo - 1, hi - lo + 1, next_lo - prev_hi - 1)
    return out


def rates(d: dict, pop: str, blocks: dict, window=WINDOW, size="max") -> dict:
    """Per-cell rates (spikes/s) in `window`.

    R1: every gid of the block, silent cells at 0 (block of the largest size if `size`="max",
    smallest if "min"). R2: only cells with at least one spike in the window. R3 (a variant
    found in the data, not a reading of the claims file): the cells the file holds, which are
    the cells that fired at least once in the 4.3 s simulation.
    """
    b = blocks[pop]
    lo, hi = (b[0], b[3]) if size == "max" else (b[1], b[2])
    dur = window[1] - window[0]
    gids = np.arange(lo, hi + 1)
    r = np.zeros(len(gids))
    for i, g in enumerate(gids):
        t = d["trains"].get(int(g))
        if t is not None and d["pop"][int(g)] == pop:
            r[i] = np.count_nonzero((t >= window[0]) & (t < window[1])) / dur
    in_file = np.array([d["pop"].get(int(g)) == pop for g in gids])
    return {"gid": gids, "R1": r, "R2_mask": r > 0, "R3_mask": in_file}


def summary(r: np.ndarray) -> tuple[float, float, int]:
    return (float(np.mean(r)) if len(r) else np.nan,
            float(np.std(r, ddof=1)) if len(r) > 1 else np.nan, len(r))


def tests(a: np.ndarray, b: np.ndarray, paired_ok=True) -> dict:
    """T1 Wilcoxon signed-rank (paired), T2 paired t, T3 Mann-Whitney U, T4 Welch t; two-sided."""
    out = {}
    if paired_ok:
        diff = a - b
        out["T1 Wilcoxon"] = stats.wilcoxon(a, b).pvalue if np.any(diff != 0) else 1.0
        out["T2 paired t"] = stats.ttest_rel(a, b).pvalue
    out["T3 Mann-Whitney"] = stats.mannwhitneyu(a, b, alternative="two-sided").pvalue
    out["T4 Welch t"] = stats.ttest_ind(a, b, equal_var=False).pvalue
    return out


def vm_spikes(v: np.ndarray, rate: float = FS, thr: float = 0.0) -> np.ndarray:
    """Times (s) of upward crossings of `thr` mV in a membrane potential trace."""
    up = np.flatnonzero((v[:-1] < thr) & (v[1:] >= thr)) + 1
    return up / rate


# ---------------------------------------------------------------- spectra

def pop_spikes(d: dict, pop: str) -> np.ndarray:
    return np.sort(np.concatenate([t for g, t in d["trains"].items() if d["pop"][g] == pop]
                                  or [np.array([])]))


def sch(spikes: np.ndarray, window=WINDOW, bin_s=SCH_BIN) -> tuple[np.ndarray, np.ndarray]:
    edges = np.arange(window[0], window[1] + bin_s / 2, bin_s)
    counts, _ = np.histogram(spikes, edges)
    return edges[:-1], counts.astype(float)


def welch_peak(x: np.ndarray, fs: float, fmin: float = 0.0, fmax: float = 100.0,
               seg_s: float = 1.0) -> tuple[float, np.ndarray, np.ndarray]:
    f, p = sps.welch(x - np.mean(x), fs=fs, nperseg=int(seg_s * fs))
    sel = (f > fmin) & (f <= fmax)
    return float(f[sel][np.argmax(p[sel])]), f, p


def morlet(sampr, freq, width=7.0):
    # netpyne/support/morlet.py (NetPyNE 1.0.5), Morlet()
    dt = 1.0 / sampr
    sf = freq / width
    st = 1.0 / (2.0 * np.pi * sf)
    t = np.arange(-3.5 * st, 3.5 * st, dt)
    a = 1.0 / (st * np.sqrt(2.0 * np.pi))
    return a * np.exp(-(t ** 2.0) / (2.0 * st ** 2.0)) * np.exp(1.0j * 2.0 * np.pi * freq * t)


def morlet_vec(sig, sampr, freq, width=7.0):
    # netpyne/support/morlet.py (NetPyNE 1.0.5), MorletVec()
    m = morlet(sampr, freq, width)
    y = sps.fftconvolve(sig, m)
    y = (2.0 * abs(y) / sampr) ** 2.0
    i_lower = int(np.ceil(len(m) / 2.0))
    i_upper = int(len(y) - np.floor(len(m) / 2.0) + 1)
    return y[i_lower:i_upper]


def morlet_spec(x: np.ndarray, fs: float, fmin=1, fmax=100, step=1, width=7.0):
    """Reading S1: MorletSpec of NetPyNE 1.0.5 with prepareSpectrogram's defaults."""
    sig = sps.detrend(x - np.mean(x))
    f = np.arange(fmin, fmax + 1, step)
    tfr = np.zeros((len(f), len(sig)))
    for j, fr in enumerate(f):
        tfr[j, :] = morlet_vec(sig, fs, fr, width)[: len(sig)]
    t = np.arange(len(sig)) / fs
    return f.astype(float), t, tfr


def stft_spec(x: np.ndarray, fs: float, win_s=0.25, overlap=0.9):
    """Reading S2: Hann-window spectrogram (standard choice; see module docstring)."""
    n = int(win_s * fs)
    f, t, s = sps.spectrogram(x - np.mean(x), fs=fs, window="hann", nperseg=n,
                              noverlap=int(n * overlap), mode="psd")
    sel = f <= 100
    return f[sel], t, s[sel]


def band_power(f, tfr, band):
    sel = (f >= band[0]) & (f <= band[1])
    return tfr[sel].mean(axis=0)


def above_runs(x: np.ndarray, thr: float) -> list[tuple[int, int]]:
    """Index runs [start, stop) where x > thr."""
    on = np.r_[False, x > thr, False].astype(int)
    d = np.diff(on)
    return list(zip(np.flatnonzero(d == 1), np.flatnonzero(d == -1)))


def band_bursts(t: np.ndarray, power: np.ndarray, dt: float) -> dict:
    """Bursts as epochs above halfway between min and max of band power over the window."""
    thr = (power.min() + power.max()) / 2
    runs = above_runs(power, thr)
    dur = np.array([(b - a) * dt for a, b in runs])
    span = len(power) * dt
    return {"n": len(runs), "rate": len(runs) / span, "durations": dur,
            "median_ms": float(np.median(dur) * 1e3) if len(dur) else np.nan,
            "frac_above": float(np.mean(power > thr))}


# ---------------------------------------------------------------- PT5B patterns

def cv_isi(trains: list[np.ndarray], min_isi: int) -> np.ndarray:
    out = []
    for t in trains:
        isi = np.diff(t)
        if len(isi) >= min_isi:
            out.append(np.std(isi) / np.mean(isi))
    return np.array(out)


def duty_cycles(counts: np.ndarray, local: bool) -> dict:
    """Duty cycles of a spike count histogram.

    Periods run from one rising crossing of the global half-height (halfway between the
    histogram's minimum and maximum) to the next. With `local`, the half-height is recomputed
    within each period from its own trough and peak. Returns the mean of per-period duty cycles
    (x) and the total time above over total time of complete periods (y).
    """
    thr = (counts.min() + counts.max()) / 2
    above = counts > thr
    rises = np.flatnonzero(~above[:-1] & above[1:]) + 1
    per, on_total, len_total = [], 0, 0
    for a, b in zip(rises[:-1], rises[1:]):
        seg = counts[a:b]
        th = (seg.min() + seg.max()) / 2 if local else thr
        on = np.count_nonzero(seg > th)
        per.append(on / len(seg))
        on_total += on
        len_total += len(seg)
    per = np.array(per)
    return {"n_periods": len(per), "mean": float(per.mean() * 100) if len(per) else np.nan,
            "total": float(on_total / len_total * 100) if len_total else np.nan,
            "threshold": thr, "median_period_ms": float(np.median(np.diff(rises)) * SCH_BIN * 1e3)
            if len(rises) > 1 else np.nan}


def coincident_fraction(d: dict, pop: str, window, reading: str) -> tuple[float, int]:
    """Share of `pop` spikes in `window` coincident with a spike of another cell of `pop`.

    (a) another cell fires within 1 ms either side; (b) another cell fires in the same 1 ms bin
    (bins aligned to the window start).
    """
    ts, ids = [], []
    for g, t in d["trains"].items():
        if d["pop"][g] == pop:
            t = t[(t >= window[0]) & (t < window[1])]
            ts.append(t)
            ids.append(np.full(len(t), g))
    t = np.concatenate(ts)
    g = np.concatenate(ids)
    o = np.argsort(t, kind="stable")
    t, g = t[o], g[o]
    n = len(t)
    if reading == "a":
        coinc = np.zeros(n, bool)
        lo = np.searchsorted(t, t - 0.001, side="left")
        hi = np.searchsorted(t, t + 0.001, side="right")
        for i in range(n):
            if hi[i] - lo[i] > 1 and np.any(g[lo[i]:hi[i]] != g[i]):
                coinc[i] = True
    else:
        b = np.floor((t - window[0]) / 0.001).astype(int)
        # a spike is coincident when its bin holds a spike of another cell
        coinc = np.zeros(n, bool)
        starts = np.r_[0, np.flatnonzero(np.diff(b)) + 1]
        stops = np.r_[starts[1:], n]
        for a, c in zip(starts, stops):
            if c - a > 1 and len(np.unique(g[a:c])) > 1:
                coinc[a:c] = True
    return float(coinc.mean() * 100), n


def unitary_events(d: dict, pop: str, span, step_s: float, win_s=0.1, bin_s=0.001,
                   alpha=0.05) -> dict:
    """Population coincidences (bins of `bin_s` holding 2 or more spikes of distinct cells) in
    windows of `win_s` moved by `step_s`; expected count from independent Poisson cells at each
    cell's rate in the window; joint-surprise p = P(N >= observed | expected). Returns the
    significant windows' union (total duration and clusters)."""
    edges = np.arange(span[0], span[1] + bin_s / 2, bin_s)
    nb = len(edges) - 1
    cells = [t[(t >= span[0]) & (t < span[1])] for g, t in d["trains"].items() if d["pop"][g] == pop]
    # per-bin count of distinct cells firing
    occ = np.zeros(nb)
    per_cell_counts = []
    for t in cells:
        c, _ = np.histogram(t, edges)
        occ += c > 0
        per_cell_counts.append(c)
    coinc = occ >= 2
    C = np.array(per_cell_counts)  # cells x bins
    w = int(round(win_s / bin_s))
    s = int(round(step_s / bin_s))
    sig = np.zeros(nb, bool)
    starts = np.arange(0, nb - w + 1, s)
    pvals, obs_all, exp_all = [], [], []
    cs = np.cumsum(np.c_[np.zeros((C.shape[0], 1)), C], axis=1)
    cco = np.r_[0, np.cumsum(coinc)]
    for a in starts:
        lam = (cs[:, a + w] - cs[:, a]) / w          # spikes per bin, per cell
        p1 = np.clip(lam, 0, 1)
        # probability that 2 or more distinct cells fire in a bin
        log0 = np.sum(np.log1p(-p1[p1 < 1]))
        p0 = np.exp(log0)
        p1sum = p0 * np.sum(p1[p1 < 1] / (1 - p1[p1 < 1]))
        pc = max(0.0, 1 - p0 - p1sum)
        expct = pc * w
        obs = cco[a + w] - cco[a]
        p = stats.poisson.sf(obs - 1, expct) if expct > 0 else (0.0 if obs > 0 else 1.0)
        pvals.append(p)
        obs_all.append(obs)
        exp_all.append(expct)
        if p < alpha:
            sig[a:a + w] = True
    runs = above_runs(sig.astype(float), 0.5)
    dur = np.array([(b - a) * bin_s for a, b in runs])
    return {"total_s": float(sig.sum() * bin_s), "clusters_ms": dur * 1e3, "runs": runs,
            "n_windows": len(starts), "n_sig_windows": int(np.sum(np.array(pvals) < alpha)),
            "obs": np.array(obs_all), "exp": np.array(exp_all), "sig": sig, "edges": edges,
            "coinc_share_bins": float(coinc.mean())}


def periodicity(spikes: np.ndarray, runs, span, bin_s=SCH_BIN, reading="x", fmin=5.0) -> list:
    """Periodicity of the PT5B SCH within each significant period (index runs in 1 ms bins).

    (x) the frequency of the largest peak of the periodogram of the SCH within the period,
    above `fmin`; (y) the inverse of the mean interval between SCH peaks (scipy find_peaks on the
    SCH, peaks at least 20 ms apart, a standard choice)."""
    out = []
    for a, b in runs:
        t0, t1 = span[0] + a * 0.001, span[0] + b * 0.001
        if t1 - t0 < 0.05:
            continue
        _, c = sch(spikes, (t0, t1), bin_s)
        if reading == "x":
            n = max(len(c), int(1.0 / bin_s))  # zero-pad to 1 Hz steps
            f = np.fft.rfftfreq(n, bin_s)
            p = np.abs(np.fft.rfft(c - c.mean(), n)) ** 2
            sel = (f > fmin) & (f <= 100)
            out.append(float(f[sel][np.argmax(p[sel])]))
        else:
            pk, _ = sps.find_peaks(c, distance=int(0.02 / bin_s))
            if len(pk) > 1:
                out.append(float(1.0 / (np.mean(np.diff(pk)) * bin_s)))
    return out
