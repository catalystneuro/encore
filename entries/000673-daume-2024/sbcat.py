"""Loading and measures for the Sternberg working memory recordings of dandiset 000673.

Daume, Kaminski, Schjetnan, Salimpour, Khan, Kyzar, Reed, Anderson, Valiante, Mamelak &
Rutishauser (2024), Nature 629, 393-401, doi:10.1038/s41586-024-07309-z.

Each NWB file holds one session: a trials table (load, picture IDs, timestamps of fixation,
encoding 1 to 3, maintenance, probe and response, response_accuracy, probe_in_out), the sorted
units (spike times, the electrode of each unit), the electrodes table (location, coordinates) and
the microwire LFP at 400 Hz (`acquisition/LFPs`). Files are streamed from the archive at the pinned
version; nothing is written to disk.

Where the parameters come from (claims file `claims/000673/10.1038-s41586-024-07309-z.yaml`,
general rules G1 to G4 and open details O1 to O11, and the paper's Methods):

- Areas: the electrode `location` with the hemisphere removed (criterion of cohort-counts, as
  condenseAreas.m of the paper's code merges left and right).
- Maintenance window 0 to 2.5 s after maintenance onset (Methods, Task; G3); baseline -0.9 to
  -0.3 s before picture 1 onset (Fig. 3b legend; G3). Only correct trials unless stated (G3).
- Category neurons: NWB_calcSelective_SB.m of github.com/rutishauserlab/SBCAT-release-NWB at
  commit a25e8cc3f61630a428f190381745257d4506f148, which the claim's criterion follows: rate in
  (0.2, 1.0) s after each encoding picture and each probe, category the first digit of the
  picture ID, permutation one-way ANOVA (2,000 permutations) p < 0.05, then an unpaired
  permutation t-test (2,000) of the category with the highest mean rate against all other
  presentations, two-sided p < 0.1. The chance count shuffles the category labels across
  presentations 500 times (Methods, Category cell selection).
- Permutation tests: statcond.m 'perm' (Methods, Statistics; G2), 10,000 permutations, paired
  tests by flipping the sign of the paired differences ("equivalent to computing pair-wise
  condition differences and testing the differences against zero", Methods, Statistics),
  two-sided p as the share of permuted |t| at least the observed |t|. The random draws are a
  standard choice that cannot change a result beyond permutation noise.
- LFP PAC: cfc_tort_comodulogram.m and NWB_samplePAC_LFP.m of the same code: epochs -0.5 to 3 s
  around maintenance onset, each trial filtered separately with pop_eegfiltnew's default
  windowed-sinc FIR (Hamming window, transition width min(max(0.25 x lower edge, 2), lower
  edge, Nyquist - upper edge), order 3.3 / (width / 400) rounded up to even, cutoffs half a
  transition width outside the pass band, edges padded with the first and last sample as
  firfilt.m does), Hilbert phase and amplitude, cut to 0 to 2.5 s, concatenated, 18 phase bins,
  MI of Tort et al.; phase centres 2 to 14 Hz with 2 Hz bandwidth, amplitude centres 30 to 150 Hz
  in 5 Hz steps with a bandwidth of twice the phase centre; 200 trial-shuffled surrogates,
  z-scored with the normal fitted to them (normfit: mean and s.d. with n - 1).
- LFP artefact rejection (Methods, LFP preprocessing; O1): per channel the signal is z-scored
  across all trials, capped at 6 s.d. and z-scored again; a trial is removed for the channel
  when any sample exceeds 4 s.d. in absolute value, or when the z-scored difference between
  every fourth sample of the capped signal exceeds 10 s.d. in absolute value. Reading (a) applies
  this to the -0.5 to 3 s epochs, reading (b) to whole trials (fixation to response). The visual
  inspection of the Methods cannot be repeated.
"""

from __future__ import annotations

import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from scipy.signal import hilbert

DANDISET_ID = "000673"
DANDISET_VERSION = "0.240118.2135"
API = "https://api.dandiarchive.org/api"

AREAS = ["hippocampus", "amygdala", "preSMA", "dACC", "vmPFC"]
MTL = ["hippocampus", "amygdala"]
FS_LFP = 400.0

MAINT_WIN = (0.0, 2.5)          # Methods, Task; G3
BASELINE_WIN = (-0.9, -0.3)     # Fig. 3b legend; G3, relative to picture 1 onset
SEL_WIN = (0.2, 1.0)            # NWB_calcSelective_SB.m: signalDelay 0.2, stimOffset 1
EPOCH = (-0.5, 3.0)             # Methods, PAC; NWB_samplePAC_LFP.m
N_PERM = 10000                  # Methods, Statistics


def area_of(location: str) -> str:
    """Area name with the hemisphere removed (condenseAreas.m)."""
    loc = location.lower()
    for key, name in [("hippocampus", "hippocampus"), ("amygdala", "amygdala"),
                      ("pre_supplementary", "preSMA"), ("anterior_cingulate", "dACC"),
                      ("ventral_medial", "vmPFC")]:
        if key in loc:
            return name
    return location


def hemisphere_of(location: str) -> str:
    return "left" if location.endswith("left") else ("right" if location.endswith("right") else "?")


def list_assets(version: str = DANDISET_VERSION) -> list[dict]:
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=200"
    out = []
    while url:
        with urllib.request.urlopen(url) as r:
            page = json.load(r)
        out += page["results"]
        url = page["next"]
    return sorted(out, key=lambda a: a["path"])


def asset_url(asset: dict) -> str:
    return f"{API}/assets/{asset['asset_id']}/download/"


def _open(asset: dict) -> h5py.File:
    return h5py.File(remfile.File(asset_url(asset)), "r")


def _str(x) -> str:
    return x.decode() if isinstance(x, bytes) else str(x)


def load_session(asset: dict) -> dict:
    """Trials, units and electrodes of one file; no LFP and no waveforms."""
    f = _open(asset)
    g = f["general"]
    el = f["general/extracellular_ephys/electrodes"]
    loc = el["location"][:].astype(str)
    electrodes = pd.DataFrame({"location": loc, "x": el["x"][:], "y": el["y"][:], "z": el["z"][:],
                               "origChannel": el["origChannel"][:] if "origChannel" in el else np.nan})
    electrodes["area"] = [area_of(s) for s in loc]
    electrodes["hemisphere"] = [hemisphere_of(s) for s in loc]
    t = f["intervals/trials"]
    trials = pd.DataFrame({k: t[k][:] for k in t.keys()
                           if isinstance(t[k], h5py.Dataset) and t[k].shape == t["id"].shape and k != "id"})
    u = f["units"]
    st = u["spike_times"][:]
    idx = u["spike_times_index"][:]
    starts = np.r_[0, idx[:-1]]
    unit_el = u["electrodes"][:]
    units = pd.DataFrame({"unit": np.arange(len(idx)), "electrode": unit_el,
                          "clusterID_orig": u["clusterID_orig"][:]})
    units["location"] = loc[unit_el]
    units["area"] = [area_of(s) for s in units.location]
    units["hemisphere"] = [hemisphere_of(s) for s in units.location]
    spikes = [st[a:b] for a, b in zip(starts, idx)]
    # Spike times are not sorted in a few units; the paper's code selects spikes with logical
    # masks, which do not depend on order, so sorting them keeps its result.
    unsorted = {i: round(float(np.diff(sp).min()), 4) for i, sp in enumerate(spikes) if np.any(np.diff(sp) < 0)}
    spikes = [np.sort(sp) for sp in spikes]
    has_lfp = "LFPs" in f["acquisition"]
    lfp_el = f["acquisition/LFPs/electrodes"][:] if has_lfp else np.array([], int)
    lfp_info = None
    if has_lfp:
        d = f["acquisition/LFPs/data"]
        st0 = f["acquisition/LFPs/starting_time"]
        lfp_info = {"shape": d.shape, "rate": float(st0.attrs["rate"]), "start": float(st0[()]),
                    "unit": _str(d.attrs.get("unit", "")), "conversion": float(d.attrs.get("conversion", 1.0)),
                    "description": _str(f["acquisition/LFPs"].attrs.get("description", ""))}
    ev = f["acquisition/events"]
    events = pd.DataFrame({"code": ev["data"][:], "t": ev["timestamps"][:]})
    subj = g["subject"]
    out = {
        "path": asset["path"], "asset": asset,
        "subject": _str(subj["subject_id"][()]), "session": _str(g["session_id"][()]),
        "age": _str(subj["age"][()]) if "age" in subj else None, "sex": _str(subj["sex"][()]),
        "trials": trials, "units": units, "spikes": spikes, "electrodes": electrodes,
        "unsorted_units": unsorted, "lfp_electrodes": lfp_el, "lfp_info": lfp_info, "events": events,
    }
    f.close()
    out["trials"] = add_trial_columns(out["trials"])
    return out


def add_trial_columns(tr: pd.DataFrame) -> pd.DataFrame:
    tr = tr.copy()
    for k in ["Encoding1", "Encoding2", "Encoding3", "Probe"]:
        ids = tr[f"PicIDs_{k}"].astype(int)
        tr[f"cat_{k}"] = [int(str(v)[0]) if v > 0 else 0 for v in ids]   # first digit (code)
    tr["rt"] = tr["timestamps_Response"] - tr["timestamps_Probe"]       # Fig. 1d legend; code
    tr["correct"] = tr["response_accuracy"].astype(int) == 1
    tr["load"] = tr["loads"].astype(int)
    return tr


def load_all(assets: list[dict] | None = None, workers: int = 12) -> list[dict]:
    assets = assets if assets is not None else list_assets()
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(load_session, assets))


# ----------------------------------------------------------------------------- spike measures

def count_in(spikes: np.ndarray, starts: np.ndarray, stops: np.ndarray, closed: bool = False) -> np.ndarray:
    """Spikes in (start, stop) for each window; [start, stop) when closed is True."""
    if closed:
        return np.searchsorted(spikes, stops, "left") - np.searchsorted(spikes, starts, "left")
    return np.searchsorted(spikes, stops, "left") - np.searchsorted(spikes, starts, "right")


def maintenance_rates(s: dict, unit: int) -> np.ndarray:
    tr = s["trials"]
    t0 = tr["timestamps_Maintenance"].to_numpy()
    return count_in(s["spikes"][unit], t0 + MAINT_WIN[0], t0 + MAINT_WIN[1], closed=True) / (MAINT_WIN[1] - MAINT_WIN[0])


def baseline_rates(s: dict, unit: int) -> np.ndarray:
    tr = s["trials"]
    t0 = tr["timestamps_Encoding1"].to_numpy()
    return count_in(s["spikes"][unit], t0 + BASELINE_WIN[0], t0 + BASELINE_WIN[1], closed=True) / (BASELINE_WIN[1] - BASELINE_WIN[0])


def presentations(s: dict) -> tuple[np.ndarray, np.ndarray]:
    """Onsets and categories of every encoding picture and probe, in the order of the code."""
    tr = s["trials"]
    ts, cats = [], []
    for k in ["Encoding1", "Encoding2", "Encoding3", "Probe"]:
        t = tr[f"timestamps_{k}"].to_numpy()
        c = tr[f"cat_{k}"].to_numpy()
        keep = (t != 0) if k != "Encoding1" else np.ones(len(t), bool)
        ts.append(t[keep])
        cats.append(c[keep])
    return np.concatenate(ts), np.concatenate(cats)


# ----------------------------------------------------------------------------- statistics

def _t1(d: np.ndarray, axis=-1) -> np.ndarray:
    n = d.shape[axis]
    return d.mean(axis) / (d.std(axis, ddof=1) / np.sqrt(n))


def perm_ttest_1samp(d, rng, n_perm: int = N_PERM) -> dict:
    """Two-sided sign-flip permutation t-test of d against 0 (paired test of differences)."""
    d = np.asarray(d, float)
    d = d[np.isfinite(d)]
    n = len(d)
    if n < 2:
        return {"n": n, "t": np.nan, "df": n - 1, "p": np.nan, "mean": float(d.mean()) if n else np.nan}
    t_obs = float(_t1(d))
    signs = rng.choice([-1.0, 1.0], size=(n_perm, n))
    t_perm = _t1(signs * d[None, :], axis=1)
    p = (np.sum(np.abs(t_perm) >= abs(t_obs)) + 1) / (n_perm + 1)
    return {"n": n, "t": t_obs, "df": n - 1, "p": float(p), "mean": float(d.mean())}


def perm_ttest_paired(x, y, rng, n_perm: int = N_PERM) -> dict:
    x, y = np.asarray(x, float), np.asarray(y, float)
    ok = np.isfinite(x) & np.isfinite(y)
    r = perm_ttest_1samp(x[ok] - y[ok], rng, n_perm)
    r.update(mean_x=float(x[ok].mean()) if ok.any() else np.nan, mean_y=float(y[ok].mean()) if ok.any() else np.nan)
    return r


def _t2(a, b, axis=-1):
    na, nb = a.shape[axis], b.shape[axis]
    va, vb = a.var(axis, ddof=1), b.var(axis, ddof=1)
    sp = ((na - 1) * va + (nb - 1) * vb) / (na + nb - 2)
    return (a.mean(axis) - b.mean(axis)) / np.sqrt(sp * (1 / na + 1 / nb))


def perm_ttest_unpaired(a, b, rng, n_perm: int = N_PERM) -> dict:
    a, b = np.asarray(a, float), np.asarray(b, float)
    allv = np.r_[a, b]
    na = len(a)
    t_obs = float(_t2(a, b))
    idx = np.argsort(rng.random((n_perm, len(allv))), axis=1)
    perm = allv[idx]
    t_perm = _t2(perm[:, :na], perm[:, na:], axis=1)
    p = (np.sum(np.abs(t_perm) >= abs(t_obs)) + 1) / (n_perm + 1)
    return {"n_a": na, "n_b": len(b), "t": t_obs, "p": float(p), "mean_a": float(a.mean()), "mean_b": float(b.mean())}


def fdr_bh(p) -> np.ndarray:
    p = np.asarray(p, float)
    n = len(p)
    order = np.argsort(p)
    q = p[order] * n / np.arange(1, n + 1)
    q = np.minimum.accumulate(q[::-1])[::-1]
    out = np.empty(n)
    out[order] = np.minimum(q, 1)
    return out


# ----------------------------------------------------------------------------- category neurons

def _anova_f(groups_sum, groups_n, total_ss, grand_sum, N, k):
    ss_between = (groups_sum ** 2 / groups_n).sum(-1) - grand_sum ** 2 / N
    ss_within = total_ss - (groups_sum ** 2 / groups_n).sum(-1)
    return (ss_between / (k - 1)) / (ss_within / (N - k))


def category_selection(rates: np.ndarray, cats: np.ndarray, rng, n_perm: int = 2000,
                       label_sets: np.ndarray | None = None) -> dict:
    """Category neuron test of NWB_calcSelective_SB.m for one neuron.

    rates: rate per presentation; cats: category codes. If label_sets (L x N) is given, the test
    is also applied to each relabelling (the shuffled-label null); the permutation null of each
    statistic depends only on the values and group sizes, so it is drawn once and reused.
    """
    rates = np.asarray(rates, float)
    N = len(rates)
    ucat = np.unique(cats)
    k = len(ucat)
    total_ss = float((rates ** 2).sum())
    grand = float(rates.sum())
    perms = np.argsort(rng.random((n_perm, N)), axis=1)

    def stats_for(labels_matrix):
        # labels_matrix: L x N category codes
        oh = (labels_matrix[:, :, None] == ucat[None, None, :]).astype(float)       # L x N x k
        gsum = np.einsum("n,lnk->lk", rates, oh)
        gn = oh.sum(1)
        F = _anova_f(gsum, gn, total_ss, grand, N, k)
        means = gsum / gn
        imax = means.argmax(1)
        return F, imax, gn

    labels_all = cats[None, :] if label_sets is None else np.vstack([cats[None, :], label_sets])
    F, imax, gn = stats_for(labels_all)
    # permutation null of F: permute the labels of the observed labelling (group sizes are fixed)
    gsum_p = np.stack([np.bincount(np.searchsorted(ucat, cats[p]), weights=rates, minlength=k) for p in perms])
    F_null = _anova_f(gsum_p, np.bincount(np.searchsorted(ucat, cats), minlength=k).astype(float),
                      total_ss, grand, N, k)
    p_anova = (np.sum(F_null[None, :] >= F[:, None] - 1e-12, axis=1)) / n_perm
    # post hoc: max category against all others, unpaired, two-sided p < 0.1
    sizes = gn[np.arange(len(imax)), imax].astype(int)
    t_null = {}
    for na in np.unique(sizes):
        pr = rates[perms]
        t_null[na] = _t2(pr[:, :na], pr[:, na:], axis=1)
    p_post = np.empty(len(imax))
    for i, (lab, im) in enumerate(zip(labels_all, imax)):
        sel = lab == ucat[im]
        t_obs = _t2(rates[sel], rates[~sel])
        p_post[i] = np.sum(np.abs(t_null[sizes[i]]) >= abs(t_obs) - 1e-12) / n_perm
    is_cat = (p_anova < 0.05) & (p_post < 0.1) & np.isfinite(F)
    return {"is_category": bool(is_cat[0]), "preferred": int(ucat[imax[0]]),
            "p_anova": float(p_anova[0]), "p_posthoc": float(p_post[0]),
            "null_is_category": is_cat[1:] if label_sets is not None else None}


# ----------------------------------------------------------------------------- LFP

def read_lfp(asset: dict) -> tuple[np.ndarray, float, float]:
    """The whole LFP array (samples x channels, microvolts as stored), its rate and start time."""
    import fsspec
    with fsspec.filesystem("http").open(asset_url(asset), "rb", block_size=16 * 2 ** 20, cache_type="readahead") as fh:
        f = h5py.File(fh, "r")
        d = f["acquisition/LFPs/data"]
        st0 = f["acquisition/LFPs/starting_time"]
        x = d[:].astype(np.float32)
        rate, start = float(st0.attrs["rate"]), float(st0[()])
        f.close()
    return x, rate, start


def epochs(x: np.ndarray, rate: float, start: float, onsets: np.ndarray, win=EPOCH) -> np.ndarray:
    """Epochs (trials x samples x channels) from win[0] to win[1] s around each onset."""
    n = int(round((win[1] - win[0]) * rate)) + 1
    i0 = np.round((onsets + win[0] - start) * rate).astype(int)
    idx = i0[:, None] + np.arange(n)[None, :]
    return x[idx]


def artefact_mask(segments: list[np.ndarray]) -> np.ndarray:
    """Trials (rows) kept for one channel; segments are the trial signals of that channel.

    Methods, LFP preprocessing (O1): z-score across all trials, cap at 6 s.d., z-score again;
    reject when any |z| > 4 or when the z-scored difference of every fourth sample exceeds 10.
    """
    allv = np.concatenate(segments)
    z = (allv - allv.mean()) / allv.std()
    zc = np.clip(z, -6, 6)
    zc = (zc - zc.mean()) / zc.std()
    lens = np.array([len(s) for s in segments])
    bounds = np.r_[0, np.cumsum(lens)]
    diffs = [np.diff(zc[a:b][::4]) for a, b in zip(bounds[:-1], bounds[1:])]
    alld = np.concatenate(diffs)
    md, sd = alld.mean(), alld.std()
    keep = np.ones(len(segments), bool)
    for i, (a, b) in enumerate(zip(bounds[:-1], bounds[1:])):
        if np.any(np.abs(zc[a:b]) > 4) or np.any(np.abs((diffs[i] - md) / sd) > 10):
            keep[i] = False
    return keep


def eegfiltnew_kernel(lo: float, hi: float, srate: float = FS_LFP) -> np.ndarray:
    """pop_eegfiltnew's default band-pass kernel (windowed sinc, Hamming)."""
    nyq = srate / 2
    max_df = min(lo, nyq - hi)
    df = min(max(lo * 0.25, 2.0), max_df)
    order = int(np.ceil(3.3 / (df / srate) / 2) * 2)
    c1, c2 = (lo - df / 2) / nyq, (hi + df / 2) / nyq
    m = np.arange(-order / 2, order / 2 + 1)
    # firws: band-pass as difference of two low-pass sinc kernels
    def lp(fc):
        h = np.where(m == 0, fc, np.sin(np.pi * fc * m) / (np.pi * np.where(m == 0, 1, m)))
        return h
    b = (lp(c2) - lp(c1)) * np.hamming(order + 1)
    return b


def fir_filter_trials(data: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Zero-phase FIR per trial (rows) with edge padding of the group delay, as firfilt.m."""
    gd = (len(b) - 1) // 2
    padded = np.concatenate([np.repeat(data[:, :1], gd, 1), data, np.repeat(data[:, -1:], gd, 1)], axis=1)
    n = padded.shape[1] + len(b) - 1
    nfft = int(2 ** np.ceil(np.log2(n)))
    y = np.fft.irfft(np.fft.rfft(padded, nfft, axis=1) * np.fft.rfft(b, nfft)[None, :], nfft, axis=1)
    # full convolution; output aligned to input sample j is at j + gd (padded) + gd (delay)
    return y[:, 2 * gd: 2 * gd + data.shape[1]]


# ----------------------------------------------------------------------------- neuron tables

def category_table(sessions: list[dict], seed: int, n_shuffles: int = 500) -> tuple[pd.DataFrame, np.ndarray]:
    """Category selection for every unit, and the selection under n_shuffles label shuffles.

    The category labels of all presentations of a session are shuffled together (one shuffle
    applied to every unit of the session), 500 times (Methods, Category cell selection).
    Returns the unit table and a (units x shuffles) boolean array of null selections.
    """
    rng = np.random.default_rng(seed)
    rows, nulls = [], []
    for si, s in enumerate(sessions):
        ts, cats = presentations(s)
        labels = np.array([rng.permutation(cats) for _ in range(n_shuffles)])
        for u in range(len(s["spikes"])):
            r = count_in(s["spikes"][u], ts + SEL_WIN[0], ts + SEL_WIN[1]) / (SEL_WIN[1] - SEL_WIN[0])
            out = category_selection(r, cats, rng, label_sets=labels)
            nulls.append(out.pop("null_is_category"))
            rows.append({"session": si, "path": s["path"], "subject": s["subject"], "unit": u,
                         "area": s["units"].area[u], "hemisphere": s["units"].hemisphere[u],
                         "electrode": int(s["units"].electrode[u]), **out})
    return pd.DataFrame(rows), np.array(nulls)


def trial_rates(sessions: list[dict], table: pd.DataFrame) -> list[dict]:
    """Per unit: maintenance and baseline rates of every trial, and trial attributes."""
    out = []
    for _, r in table.iterrows():
        s = sessions[r.session]
        tr = s["trials"]
        enc = tr[["cat_Encoding1", "cat_Encoding2", "cat_Encoding3"]].to_numpy()
        pref = (enc == r.preferred).any(1)
        out.append({"maint": maintenance_rates(s, r.unit), "base": baseline_rates(s, r.unit),
                    "correct": tr.correct.to_numpy(), "load": tr.load.to_numpy(), "rt": tr.rt.to_numpy(),
                    "pref": pref})
    return out


def rt_split(load: np.ndarray, rt: np.ndarray, use: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Fast and slow trials by a median split of RT within each load, among `use` trials.

    Trials at or below the load's median are fast, above it slow (a standard choice for the
    split, which the paper does not detail).
    """
    fast = np.zeros(len(rt), bool)
    slow = np.zeros(len(rt), bool)
    for L in (1, 3):
        m = use & (load == L)
        if m.sum() < 2:
            continue
        med = np.median(rt[m])
        fast |= m & (rt <= med)
        slow |= m & (rt > med)
    return fast, slow


# ----------------------------------------------------------------------------- PAC engine

PHASE_CENTRES = np.arange(2, 15, 2)          # Methods, PAC; cfc_tort_comodulogram.m defaults
AMP_CENTRES = np.arange(30, 151, 5)
N_BINS = 18
N_SURR = 200
EPOCH_N = 1400                                # -0.5 to 3 s at 400 Hz
CUT = 200                                     # 0.5 s cut at each edge (tcutEdge = 0.5)
THETA = (4, 6)                                # O3: phase centres of theta (3 to 7 Hz)
HIGH_GAMMA = (70, 140)                        # O3: amplitude centres 70 to 140 Hz
LOW_GAMMA = (30, 55)                          # O3: amplitude centres 30 to 55 Hz
SLOW_THETA, FAST_THETA = (2, 4), (6, 8)       # tables1 reading (a)

_KERNELS: dict = {}


def _kernel(lo, hi):
    key = (round(lo, 3), round(hi, 3))
    if key not in _KERNELS:
        _KERNELS[key] = eegfiltnew_kernel(lo, hi)
    return _KERNELS[key]


class TrialFilter:
    """Filters every trial of one channel once; zero-phase FIR with edge padding as firfilt.m.

    Padding with more copies of the edge sample than a kernel's group delay does not change the
    output inside the epoch, so one padded FFT serves every kernel.
    """

    def __init__(self, data: np.ndarray, max_gd: int = 660):
        from scipy import fft as sfft
        self.sfft = sfft
        self.n = data.shape[1]
        self.G = max_gd
        padded = np.concatenate([np.repeat(data[:, :1], max_gd, 1), data, np.repeat(data[:, -1:], max_gd, 1)], axis=1)
        self.nfft = int(sfft.next_fast_len(padded.shape[1] + 2 * max_gd + 1))
        self.X = sfft.rfft(padded.astype(np.float32), self.nfft, axis=1)
        self._kf = {}

    def analytic(self, lo, hi) -> np.ndarray:
        b = _kernel(lo, hi)
        gd = (len(b) - 1) // 2
        key = (lo, hi)
        if key not in self._kf:
            self._kf[key] = self.sfft.rfft(b.astype(np.float32), self.nfft)
        y = self.sfft.irfft(self.X * self._kf[key][None, :], self.nfft, axis=1)
        y = y[:, self.G + gd: self.G + gd + self.n]
        return hilbert(y, axis=1)


def mi_from_bins(sums: np.ndarray, counts: np.ndarray) -> np.ndarray:
    """Tort's MI from summed amplitudes (..., bins, amps) and sample counts (..., bins)."""
    mean_amp = sums / counts[..., None]
    P = mean_amp / mean_amp.sum(-2, keepdims=True)
    return 1 + (P * np.log(P)).sum(-2) / np.log(N_BINS)


def channel_pac(data: np.ndarray, phase_centres=PHASE_CENTRES, amp_centres=AMP_CENTRES, tf=None):
    """Per-trial bin sums for one channel: data is trials x EPOCH_N samples (-0.5 to 3 s).

    Returns, per phase centre, M (trials x bins x trials x amps: amplitude of trial u summed
    over the samples of trial t in each phase bin of t), C (trials x bins counts), and the
    per-trial mean squared amplitude (power) of the phase and amplitude signals.
    """
    tf = tf or TrialFilter(data)
    out = {}
    T = data.shape[0]
    for p in phase_centres:
        ph_an = tf.analytic(p - 1, p + 1)[:, CUT:EPOCH_N - CUT]
        ph = np.angle(ph_an)
        deg = np.degrees(ph)
        bins = np.clip(np.digitize(deg, np.linspace(-180, 180, N_BINS + 1)) - 1, 0, N_BINS - 1)
        S = bins.shape[1]
        B = np.zeros((T, N_BINS, S), np.float32)
        B[np.arange(T)[:, None], bins, np.arange(S)[None, :]] = 1
        amps = np.empty((T, S, len(amp_centres)), np.float32)
        for j, a in enumerate(amp_centres):
            amps[:, :, j] = np.abs(tf.analytic(a - p, a + p))[:, CUT:EPOCH_N - CUT]
        M = (B.reshape(T * N_BINS, S) @ amps.transpose(1, 0, 2).reshape(S, T * len(amp_centres))
             ).reshape(T, N_BINS, T, len(amp_centres))
        C = B.sum(2)
        ph_amp = np.abs(ph_an)
        out[int(p)] = {"M": M, "C": C, "phase_power": (ph_amp ** 2).mean(1), "amp_power": (amps.astype(np.float64) ** 2).mean(1),
                       "bins": bins, "amp_mean": amps.mean(1)}
    return out


THETA_BANDS = {"slow": (2.0, 5.0), "fast": (5.0, 9.0)}   # tables1 reading (b)
BAND_AMPS = AMP_CENTRES[(AMP_CENTRES <= LOW_GAMMA[1]) | (AMP_CENTRES >= HIGH_GAMMA[0]) & (AMP_CENTRES <= HIGH_GAMMA[1])]


def channel_pac_bands(data: np.ndarray, tf=None) -> dict:
    """As channel_pac for the phase bands of THETA_BANDS (tables1 reading (b)); the amplitude
    bandwidth is twice the band's centre, as for the comodulogram's phase centres."""
    tf = tf or TrialFilter(data.astype(np.float64))
    out = {}
    T = data.shape[0]
    for key, (lo, hi) in THETA_BANDS.items():
        pc = (lo + hi) / 2
        ph = np.angle(tf.analytic(lo, hi))[:, CUT:EPOCH_N - CUT]
        bins = np.clip(np.digitize(np.degrees(ph), np.linspace(-180, 180, N_BINS + 1)) - 1, 0, N_BINS - 1)
        S = bins.shape[1]
        B = np.zeros((T, N_BINS, S), np.float32)
        B[np.arange(T)[:, None], bins, np.arange(S)[None, :]] = 1
        amps = np.empty((T, S, len(BAND_AMPS)), np.float32)
        for j, a in enumerate(BAND_AMPS):
            amps[:, :, j] = np.abs(tf.analytic(a - pc, a + pc))[:, CUT:EPOCH_N - CUT]
        M = (B.reshape(T * N_BINS, S) @ amps.transpose(1, 0, 2).reshape(S, T * len(BAND_AMPS))
             ).reshape(T, N_BINS, T, len(BAND_AMPS))
        out[key] = {"M": M, "C": B.sum(2)}
    return out


def pac_condition(res_p: dict, trials: np.ndarray, rng, n_surr: int = N_SURR):
    """MI over the given trials (indices) for one phase centre, and its z against trial shuffles.

    Surrogates pair the phase of each trial with the amplitude of a randomly permuted trial
    (randperm, as cfc_tort_comodulogram.m); z uses the normal fitted to the surrogates.
    Returns raw MI (amps), z (amps), surrogate MIs (n_surr x amps) and P (bins x amps).
    """
    M, C = res_p["M"], res_p["C"]
    tr = np.asarray(trials)
    sums = M[tr, :, tr, :].sum(0)                    # bins x amps
    counts = C[tr].sum(0)
    mi = mi_from_bins(sums, counts)
    perms = np.array([rng.permutation(tr) for _ in range(n_surr)])     # n_surr x n
    s_sums = M[tr[None, :], :, perms, :].sum(1)      # n_surr x bins x amps
    s_mi = mi_from_bins(s_sums, np.broadcast_to(counts, (n_surr, N_BINS)))
    mu, sd = s_mi.mean(0), s_mi.std(0, ddof=1)
    P = (sums / counts[:, None]) / (sums / counts[:, None]).sum(0)
    return {"mi": mi, "z": (mi - mu) / sd, "surr_z": (s_mi - mu) / sd, "P": P}


def single_trial_mi(res_p: dict) -> np.ndarray:
    """MI of each trial alone (trials x amps), O5 reading (a)."""
    M, C = res_p["M"], res_p["C"]
    T = M.shape[0]
    d = M[np.arange(T), :, np.arange(T), :]          # trials x bins x amps
    return mi_from_bins(d, C)


def circ_kappa_weighted(P: np.ndarray) -> float:
    """circ_kappa of CircStat on the 18 bin centres weighted by P (no small-sample correction)."""
    centres = np.radians(np.linspace(-180, 180, N_BINS + 1)[:-1] + 180 / N_BINS)
    R = np.abs(np.sum(P * np.exp(1j * centres))) / np.sum(P)
    if R < 0.53:
        return 2 * R + R ** 3 + 5 * R ** 5 / 6
    if R < 0.85:
        return -0.4 + 1.39 * R + 0.43 / (1 - R)
    return 1 / (R ** 3 - 4 * R ** 2 + 3 * R)


def nesting(raw: np.ndarray, theta_phase: np.ndarray, gamma: np.ndarray) -> dict:
    """Theta-gamma nesting after Vaz et al. (Methods, PAC, last paragraph).

    raw: trials x EPOCH_N raw LFP; theta_phase: trials x samples of 0 to 2.5 s from a 3-7 Hz
    filter; gamma: the analytic 70-140 Hz signal over the same samples. The preferred phase bin
    is the bin of maximal mean gamma amplitude; in each run of consecutive samples in that bin
    one time point is taken: reading 'amp', the sample of maximal gamma amplitude (the Methods'
    words); reading 'peak', the sample of maximal gamma-filtered signal (a gamma peak), which
    keeps the gamma phase aligned across windows. 500 ms of raw LFP centred on each are
    averaged; a channel is nested if at least three local maxima of the average fall within 45
    ms around the centre.
    """
    amp = np.abs(gamma)
    real = gamma.real
    bins = np.clip(np.digitize(np.degrees(theta_phase), np.linspace(-180, 180, N_BINS + 1)) - 1, 0, N_BINS - 1)
    mean_amp = np.array([amp[bins == b].mean() for b in range(N_BINS)])
    pb = int(np.argmax(mean_amp))
    half = 100                                         # 250 ms at 400 Hz
    out = {}
    for name, sig in [("amp", amp), ("peak", real)]:
        windows = []
        for t in range(raw.shape[0]):
            inb = bins[t] == pb
            edges = np.flatnonzero(np.diff(np.r_[0, inb.astype(int), 0]))
            for a, b in zip(edges[::2], edges[1::2]):
                k = a + int(np.argmax(sig[t, a:b])) + CUT
                if k - half >= 0 and k + half < raw.shape[1]:
                    windows.append(raw[t, k - half:k + half + 1])
        if not windows:
            out[name] = {"nested": False, "n_maxima": 0, "n_windows": 0}
            continue
        avg = np.mean(windows, 0)
        c, w = half, 9                                 # 22.5 ms each side (45 ms window)
        seg = avg[c - w - 1:c + w + 2]
        n_max = int(((seg[1:-1] > seg[:-2]) & (seg[1:-1] > seg[2:])).sum())
        out[name] = {"nested": n_max >= 3, "n_maxima": n_max, "n_windows": len(windows)}
    return out


def process_session_lfp(s: dict, seed: int, si: int) -> dict:
    """Everything the LFP claims need from one session, channel by channel.

    Readings of the artefact rejection (O1): 'a' on the -0.5 to 3 s epochs, 'b' on whole trials.
    For each reading, correct clean trials are subsampled to equal counts in load 1 and load 3
    (O2), and MI is computed for both loads together ('all') and each load.
    """
    import os
    from scipy.signal import welch
    x, rate, start = read_lfp(s["asset"])
    tr = s["trials"]
    onsets = tr.timestamps_Maintenance.to_numpy()
    i0 = np.round((onsets - 0.5 - start) * rate).astype(int)
    E = x[i0[:, None] + np.arange(EPOCH_N)[None, :]]               # trials x samples x channels
    fix = np.round((tr.timestamps_FixationCross.to_numpy() - start) * rate).astype(int)
    resp = np.round((tr.timestamps_Response.to_numpy() - start) * rate).astype(int)
    el = s["electrodes"].iloc[s["lfp_electrodes"]].reset_index(drop=True)
    correct = tr.correct.to_numpy()
    load = tr.load.to_numpy()
    T = len(tr)
    # clock check: LFP response to the probe, at the true and at earlier (maintenance) onsets;
    # ratio of the RMS of the trial-averaged LFP 0.1 to 0.6 s after the onset to that of -0.6 to -0.1 s
    probe = np.round((tr.timestamps_Probe.to_numpy() - start) * rate).astype(int)
    evoked = {}
    for sh in [-2.0, -1.0, 0.0]:
        k = probe + int(sh * rate)
        ep = x[k[:, None] + np.arange(-240, 241)[None, :]].astype(np.float64).mean(0)
        ep = ep - ep[:200].mean(0)
        evoked[sh] = np.sqrt((ep[280:441] ** 2).mean(0)) / (np.sqrt((ep[0:201] ** 2).mean(0)) + 1e-9)
    chans = []
    theta_hg = [(p, j) for p in THETA for j, a in enumerate(AMP_CENTRES) if HIGH_GAMMA[0] <= a <= HIGH_GAMMA[1]]
    hg_idx = np.where((AMP_CENTRES >= HIGH_GAMMA[0]) & (AMP_CENTRES <= HIGH_GAMMA[1]))[0]
    lg_idx = np.where((AMP_CENTRES >= LOW_GAMMA[0]) & (AMP_CENTRES <= LOW_GAMMA[1]))[0]
    freqs = None
    for ch in range(E.shape[2]):
        data = E[:, :, ch].astype(np.float64)
        masks = {"a": artefact_mask([data[t] for t in range(T)]),
                 "b": artefact_mask([x[fix[t]:resp[t] + 1, ch].astype(np.float64) for t in range(T)])}
        # MI and its surrogates only ever pair correct trials, so the per-trial matrices are
        # built on the correct trials (indices into them are mapped below)
        cidx = np.where(correct)[0]
        pos = -np.ones(T, int)
        pos[cidx] = np.arange(len(cidx))
        tfc = TrialFilter(data[cidx])
        res = channel_pac(data[cidx], tf=tfc)
        res_b = channel_pac_bands(data[cidx], tf=tfc)
        bhg = np.where(BAND_AMPS >= HIGH_GAMMA[0])[0]
        blg = np.where(BAND_AMPS <= LOW_GAMMA[1])[0]
        st = {p: single_trial_mi(res[p]) for p in THETA}
        f, psd = welch(data[:, CUT:EPOCH_N - CUT], fs=rate, nperseg=400, noverlap=200, axis=1)
        freqs = f
        info = {"session": si, "path": s["path"], "subject": s["subject"], "channel": ch,
                "location": el.location[ch], "area": el.area[ch], "hemisphere": el.hemisphere[ch],
                "sd_uV": float(data.std()), "p99_abs_uV": float(np.percentile(np.abs(data), 99)),
                "evoked": {sh: float(v[ch]) for sh, v in evoked.items()},
                "trial_index": cidx,
                "st_thetaHG": np.mean([st[p][:, hg_idx].mean(1) for p in THETA], 0),
                "theta_power": np.mean([res[p]["phase_power"] for p in THETA], 0),
                "hg_power": np.mean([res[p]["amp_power"][:, hg_idx].mean(1) for p in THETA], 0),
                "masks": masks, "readings": {}}
        for reading in ["a", "b"]:
            rng = np.random.default_rng([seed, si, ch, ord(reading)])
            ok = masks[reading] & correct
            l1, l3 = np.where(ok & (load == 1))[0], np.where(ok & (load == 3))[0]
            n = min(len(l1), len(l3))
            if n < 3:
                info["readings"][reading] = None
                continue
            l1s, l3s = np.sort(rng.choice(l1, n, replace=False)), np.sort(rng.choice(l3, n, replace=False))
            out = {"n_per_load": n, "trials_l1": l1s, "trials_l3": l3s}
            l1s, l3s = pos[l1s], pos[l3s]          # positions among the correct trials
            both = np.r_[l1s, l3s]
            phases_all = PHASE_CENTRES if reading == "a" else np.array([2, 4, 6, 8])
            z_all, surr_hg, surr_lg = {}, [], []
            for p in phases_all:
                c = pac_condition(res[int(p)], both, rng)
                z_all[int(p)] = c["z"]
                if int(p) in THETA:
                    surr_hg.append(c["surr_z"][:, hg_idx].mean(1))
                    surr_lg.append(c["surr_z"][:, lg_idx].mean(1))
            out["z_all"] = z_all
            band = {}
            for key in THETA_BANDS:
                for cname, trs in [("all", both), ("l1", l1s), ("l3", l3s)]:
                    c = pac_condition(res_b[key], trs, rng)
                    band[(key, "HG", cname)] = float(c["z"][bhg].mean())
                    band[(key, "LG", cname)] = float(c["z"][blg].mean())
            out["bands"] = band
            out["surr_thetaHG"] = np.mean(surr_hg, 0)
            out["surr_thetaLG"] = np.mean(surr_lg, 0)
            for name, trs in [("l1", l1s), ("l3", l3s)]:
                zz, mm, PP = {}, {}, {}
                for p in [2, 4, 6, 8]:
                    c = pac_condition(res[p], trs, rng)
                    zz[p], mm[p], PP[p] = c["z"], c["mi"], c["P"]
                out[f"z_{name}"], out[f"mi_{name}"] = zz, mm
                out[f"P_thetaHG_{name}"] = np.mean([PP[p][:, hg_idx].mean(1) for p in THETA], 0)
                out[f"psd_{name}"] = psd[cidx[trs]].mean(0)
            if el.area[ch] == "hippocampus":
                lo = tfc
                th = np.angle(lo.analytic(3, 7))[:, CUT:EPOCH_N - CUT]
                ga = lo.analytic(70, 140)[:, CUT:EPOCH_N - CUT]
                cc = pos[np.where(ok)[0]]
                out["nesting"] = nesting(data[cidx][cc], th[cc], ga[cc])
                # n:m phase locking of theta (3-7 Hz) and high gamma (70-140 Hz) phase, ratio 1:21
                # (band centres 5 and 105 Hz, the claim's first reading), per load
                gph = np.angle(ga)
                for name, trs in [("l1", l1s), ("l3", l3s)]:
                    out[f"ppc_{name}"] = float(np.abs(np.mean(np.exp(1j * (21 * th[trs] - gph[trs])))))
            info["readings"][reading] = out
        chans.append(info)
    return {"path": s["path"], "subject": s["subject"], "session": si, "channels": chans, "freqs": freqs,
            "lfp_shape": x.shape, "lfp_fingerprint": float(np.round(x[:4000, 0].astype(np.float64).sum(), 3))}


def _lfp_job(args):
    s, seed, si = args
    return process_session_lfp(s, seed, si)


def run_all_lfp(sessions: list[dict], seed: int, workers: int = 6) -> list[dict]:
    """process_session_lfp on every session with LFP, in parallel processes (largest first)."""
    from concurrent.futures import ProcessPoolExecutor
    jobs = [(s, seed, si) for si, s in enumerate(sessions) if len(s["lfp_electrodes"])]
    jobs.sort(key=lambda j: -len(j[0]["lfp_electrodes"]) * j[0]["lfp_info"]["shape"][0])
    with ProcessPoolExecutor(workers) as ex:
        out = list(ex.map(_lfp_job, jobs))
    return sorted(out, key=lambda r: r["session"])


# ----------------------------------------------------------------------------- PAC neurons

GAMMA_WAVELETS = np.arange(70, 141, 5)      # Methods, Selection of PAC neurons: 70-140 Hz, 5 Hz steps
WAVELET_CYCLES = 7
N_PHASE_BINS_NEURON = 10                     # 36 degree bins
PAC_NEURON_ALPHA = 0.01                      # P < 0.01 after FDR (Methods)


def morlet_amplitude(data: np.ndarray, freqs=GAMMA_WAVELETS, cycles=WAVELET_CYCLES, srate=FS_LFP) -> np.ndarray:
    """|complex Morlet convolution| per trial (trials x samples x freqs), 'same' alignment."""
    from scipy import fft as sfft
    T, n = data.shape
    out = np.empty((T, n, len(freqs)), np.float32)
    for j, f in enumerate(freqs):
        sd = cycles / (2 * np.pi * f)
        t = np.arange(-4 * sd, 4 * sd + 1 / srate, 1 / srate)
        w = np.exp(2j * np.pi * f * t) * np.exp(-t ** 2 / (2 * sd ** 2))
        w /= np.abs(w).sum()
        m = n + len(w) - 1
        nfft = sfft.next_fast_len(m)
        y = sfft.ifft(sfft.fft(data, nfft, axis=1) * sfft.fft(w, nfft)[None, :], axis=1)
        h = (len(w) - 1) // 2
        out[:, :, j] = np.abs(y[:, h:h + n])
    return out


def neuron_design() -> dict:
    """Design matrices of the three Poisson GLMs over the 20 theta x gamma bins (Methods).

    Theta as cos and sin of each bin's left phase edge (claims file, criterion of
    pac-neuron-counts); gamma as 0 (low) and 1 (high), MATLAB's reference coding of a two-level
    categorical predictor.
    """
    edges = np.radians(-180 + 36 * np.arange(N_PHASE_BINS_NEURON))
    c, s = np.tile(np.cos(edges), 2), np.tile(np.sin(edges), 2)
    g = np.repeat([0.0, 1.0], N_PHASE_BINS_NEURON)
    one = np.ones(20)
    return {"m1": np.c_[one, c, s, g, c * g, s * g], "m2": np.c_[one, c, s, g], "m3": np.c_[one, c, s, c * g, s * g]}


def poisson_fit_batch(X: np.ndarray, Y: np.ndarray, n_iter: int = 30) -> tuple[np.ndarray, np.ndarray]:
    """Poisson GLMs (log link) with one design X (n x p) for many responses Y (K x n), by IRLS.

    Returns the deviance (K) and the fitted means (K x n)."""
    K, n = Y.shape
    beta = np.zeros((K, X.shape[1]))
    beta[:, 0] = np.log(np.maximum(Y.mean(1), 1e-3))
    for _ in range(n_iter):
        eta = np.clip(beta @ X.T, -30, 30)
        mu = np.exp(eta)
        z = eta + (Y - mu) / mu
        XtWX = np.einsum("kn,np,nq->kpq", mu, X, X) + 1e-8 * np.eye(X.shape[1])[None]
        XtWz = np.einsum("kn,np,kn->kp", mu, X, z)
        beta = np.linalg.solve(XtWX, XtWz[..., None])[..., 0]
    mu = np.exp(np.clip(beta @ X.T, -30, 30))
    with np.errstate(divide="ignore", invalid="ignore"):
        term = np.where(Y > 0, Y * np.log(Y / mu), 0.0)
    dev = 2 * (term - (Y - mu)).sum(1)
    return dev, mu


def pac_neuron_tests(Y: np.ndarray) -> dict:
    """Likelihood-ratio tests of model 1 against models 2 and 3 for spike counts Y (K x 20)."""
    from scipy.stats import chi2
    D = neuron_design()
    dev1, mu1 = poisson_fit_batch(D["m1"], Y)
    dev2, _ = poisson_fit_batch(D["m2"], Y)
    dev3, _ = poisson_fit_batch(D["m3"], Y)
    p12 = chi2.sf(np.maximum(dev2 - dev1, 0), 2)
    p13 = chi2.sf(np.maximum(dev3 - dev1, 0), 1)
    yc = Y - Y.mean(1, keepdims=True)
    mc = mu1 - mu1.mean(1, keepdims=True)
    with np.errstate(divide="ignore", invalid="ignore"):
        r2 = (yc * mc).sum(1) ** 2 / ((yc ** 2).sum(1) * (mc ** 2).sum(1))
    return {"p12": p12, "p13": p13, "r2": r2}


def process_session_pac_neurons(s: dict, seed: int, si: int, n_shuffles: int = 200) -> dict:
    """Spike counts in the 20 theta-gamma bins for every MTL neuron and LFP channel of its bundle.

    Bundle: the electrodes of a session with the same location and coordinates. Correct trials of
    one load, clean for the channel under artefact reading (a) (O1); -0.5 to 3 s epochs cut to 0 to
    2.5 s; theta phase from pop_eegfiltnew 3-7 Hz and Hilbert; gamma from 7-cycle Morlet wavelets at
    70-140 Hz, each z-scored over the concatenated samples, averaged, median split. Also the counts
    with spikes and LFP paired from randomly permuted trials (n_shuffles).
    """
    x, rate, start = read_lfp(s["asset"])
    tr = s["trials"]
    onsets = tr.timestamps_Maintenance.to_numpy()
    i0 = np.round((onsets - 0.5 - start) * rate).astype(int)
    el = s["electrodes"]
    lfp_el = s["lfp_electrodes"]
    units = s["units"]
    correct, load = tr.correct.to_numpy(), tr.load.to_numpy()
    T = len(tr)
    rng = np.random.default_rng([seed, si])
    key = el.location.astype(str) + "|" + el.x.round(2).astype(str) + "|" + el.y.round(2).astype(str) + "|" + el.z.round(2).astype(str)
    rows, counts = [], []
    mtl_units = np.where(units.area.isin(MTL))[0]
    lfp_cache = {}
    for u in mtl_units:
        bundle = key[units.electrode[u]]
        chans = [ci for ci, e in enumerate(lfp_el) if key[e] == bundle]
        for ci in chans:
            if ci not in lfp_cache:
                data = x[i0[:, None] + np.arange(EPOCH_N)[None, :], ci].astype(np.float64)
                clean = artefact_mask([data[t] for t in range(T)])
                tf = TrialFilter(data)
                ph = np.angle(tf.analytic(3, 7))[:, CUT:EPOCH_N - CUT]
                amp = morlet_amplitude(data)[:, CUT:EPOCH_N - CUT, :]
                lab = {}
                for L in (1, 3):
                    trs = np.where(correct & clean & (load == L))[0]
                    a = amp[trs]
                    z = (a - a.mean((0, 1))) / a.std((0, 1))
                    g = z.mean(2)
                    hi = (g > np.median(g)).astype(int)
                    pb = np.clip(((np.degrees(ph[trs]) + 180) // 36).astype(int), 0, 9)
                    lab[L] = (trs, (hi * 10 + pb).astype(np.int8))
                # single-trial theta-high-gamma MI of every trial (O5 reading a), for fig4c
                hg = AMP_CENTRES[(AMP_CENTRES >= HIGH_GAMMA[0]) & (AMP_CENTRES <= HIGH_GAMMA[1])]
                st = []
                for p in THETA:
                    pbin = np.clip(np.digitize(np.degrees(np.angle(tf.analytic(p - 1, p + 1))[:, CUT:EPOCH_N - CUT]),
                                               np.linspace(-180, 180, N_BINS + 1)) - 1, 0, N_BINS - 1)
                    oh = (pbin[:, :, None] == np.arange(N_BINS)[None, None, :]).astype(np.float32)   # T x S x bins
                    cnt = oh.sum(1)
                    mis = []
                    for a in hg:
                        am = np.abs(tf.analytic(a - p, a + p))[:, CUT:EPOCH_N - CUT].astype(np.float32)
                        sums = np.einsum("tsb,ts->tb", oh, am)
                        with np.errstate(divide="ignore", invalid="ignore"):
                            mis.append(mi_from_bins(sums[:, :, None], cnt)[:, 0])
                    st.append(np.nanmean(mis, 0))
                lab["st_mi"] = np.mean(st, 0)
                lab["clean"] = clean
                lfp_cache[ci] = lab
            for L in (1, 3):
                trs, lab = lfp_cache[ci][L]
                sp = s["spikes"][u]
                tt, ss = [], []
                for k, t in enumerate(trs):
                    a, b = np.searchsorted(sp, [onsets[t], onsets[t] + 2.5])
                    idx = np.minimum(np.round((sp[a:b] - onsets[t]) * rate).astype(int), lab.shape[1] - 1)
                    tt.append(np.full(len(idx), k)); ss.append(idx)
                tt, ss = np.concatenate(tt) if tt else np.array([], int), np.concatenate(ss) if ss else np.array([], int)
                Y = np.empty((n_shuffles + 1, 20))
                Y[0] = np.bincount(lab[tt, ss], minlength=20)
                for r_ in range(n_shuffles):
                    perm = rng.permutation(len(trs))
                    Y[r_ + 1] = np.bincount(lab[perm[tt], ss], minlength=20)
                rows.append({"session": si, "subject": s["subject"], "unit": int(u), "area": units.area[u],
                             "electrode": int(units.electrode[u]), "channel": int(ci), "lfp_electrode": int(lfp_el[ci]),
                             "load": L, "n_trials": len(trs), "n_spikes": int(len(tt))})
                counts.append(Y)
    return {"session": si, "rows": rows, "counts": np.array(counts) if counts else np.zeros((0, n_shuffles + 1, 20)),
            "mtl_units": [int(u) for u in mtl_units],
            "st_mi": {ci: v["st_mi"] for ci, v in lfp_cache.items()}, "clean": {ci: v["clean"] for ci, v in lfp_cache.items()}}


def _pacn_job(args):
    s, seed, si = args
    return process_session_pac_neurons(s, seed, si)


def run_all_pac_neurons(sessions: list[dict], seed: int, workers: int = 6) -> list[dict]:
    from concurrent.futures import ProcessPoolExecutor
    jobs = [(s, seed, si) for si, s in enumerate(sessions)
            if len(s["lfp_electrodes"]) and s["units"].area.isin(MTL).any()]
    jobs.sort(key=lambda j: -int(j[0]["units"].area.isin(MTL).sum()))
    with ProcessPoolExecutor(workers) as ex:
        out = list(ex.map(_pacn_job, jobs))
    return sorted(out, key=lambda r: r["session"])
