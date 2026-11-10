"""Loading and measures for the ALM recordings of dandiset 000007.

Gao, Davis, Thomas, Economo, Abrego, Svoboda, De Zeeuw & Li (2018), "A cortico-cerebellar loop for
motor planning", Nature 563, 113-116, doi:10.1038/s41586-018-0633-x. The claims are in
claims/gao-2018.yaml; method labels B1, E1 to E6 below are the shared methods of that file.

Each NWB file is one ALM recording session: a trials table (pole_in_time, pole_out_time,
cue_time, response, lick_early, photo_stim_id) and sorted units (spike_times, waveform_mean,
cell_type). Files are streamed from the archive at the pinned version; nothing is written to
disk. The files hold no lick times, no CN recordings and no description of the photo_stim_id
codes.

Where the parameters come from:

- Epochs (Methods, Behavior): sample from pole_in_time (pole movement onset) to pole_out_time,
  delay from pole_out_time to cue_time (1.3 s each in the files, as in the Methods), response
  from cue_time. The response epoch's length is open in the claims file (E2): readings 1.3 s
  and 1.5 s (`RESPONSE_WINDOWS`).
- Putative pyramidal neurons (E1; Methods, Electrophysiology data analysis): trough-to-peak
  width of the mean waveform > 0.45 ms, fast spiking < 0.35 ms. `spike_width_ms` computes it;
  the files' own `cell_type` column is compared with it in the notebook.
- Selectivity test (E2): two-tailed t-test (p < 0.05) on spike counts in each epoch, "lick left"
  against "lick right" trials.
- Photostimulation effect (E4): two-tailed t-test on spike counts, control against
  photostimulation trials, p < 0.01, lick left and lick right trials pooled.
- Population selectivity (E3): preferred trial type from 10 trials (ALM), the spike rate
  difference preferred minus non-preferred on the remaining trials, 200 ms averaging window.
- Latency (E5; Extended Data Fig. 9a legend): 10 ms bins in 1 ms steps, onset the first bin
  where the population change differs from 0 (two-tailed t-test, p < 0.01), neurons resampled
  10,000 times.
- Coding direction (E6; Methods, Analysis of ALM population dynamics): 400 ms windows in 10 ms
  steps, sessions with > 5 neurons and > 5 trials per condition.
- Lick early trials are left out of every neural analysis, as they are from performance (Methods,
  Behavioral data analysis). The paper does not say so for the neural analyses; it is a
  standard choice in this task (an early lick restarts the epoch, so its timing differs), and
  the notebook reports how many trials it drops.
- Neural analyses also leave out trials outside the units' observation intervals (`obs_intervals`
  of the units table). Only BAYLORCD8 20171020 has any: its spikes end at 7221 s and its last 127
  trials, to 8481 s, hold no spike of any unit.
- Time courses use trials whose sample and delay epochs last 1.3 s (within 10 ms), aligned to
  the go cue; trials with longer epochs are counted and dropped. A standard choice.
"""

from __future__ import annotations

import json
import warnings
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field

import h5py
import numpy as np
import pandas as pd
import remfile
from scipy import stats

DANDISET_ID = "000007"
DANDISET_VERSION = "0.220126.1903"

EPOCH_S = 1.3                    # sample and delay epoch length (Methods, Behavior)
RESPONSE_WINDOWS = (1.3, 1.5)    # E2 readings (a) and (b)
PYR_MIN_MS, FS_MAX_MS = 0.45, 0.35   # E1
P_SELECT = 0.05                  # E2
P_PHOTO = 0.01                   # E4, E5
PREF_TRIALS_ALM = 10             # E3


@dataclass
class Session:
    path: str
    subject: str
    genotype: str
    site: str            # ogen site name (Fastigial / Dentate)
    site_hemisphere: str
    rec_ml: str          # recording coordinate, mediolateral, from the electrode group
    trials: pd.DataFrame
    spikes: list = field(repr=False)     # one array of spike times (s) per unit
    waveforms: np.ndarray = field(repr=False)
    cell_type: np.ndarray = field(repr=False)
    wf_rate: float = 20000.0
    obs_intervals: list = field(default_factory=list, repr=False)   # per unit, [n, 2] array (s)
    units_columns: list = field(default_factory=list)
    groups: dict = field(default_factory=dict)   # top-level HDF5 groups and their members

    @property
    def n_units(self):
        return len(self.spikes)


def asset_list():
    from dandi.dandiapi import DandiAPIClient
    client = DandiAPIClient()
    ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
    return sorted(ds.get_assets(), key=lambda a: a.path)


def _read(asset) -> Session:
    import pynwb
    url = asset.get_content_url(follow_redirects=1, strip_query=True)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        f = h5py.File(remfile.File(url), "r")
        io = pynwb.NWBHDF5IO(file=f, load_namespaces=True)
        nwb = io.read()
        trials = nwb.trials.to_dataframe().reset_index()
        st = f["units/spike_times"][:]
        idx = f["units/spike_times_index"][:]
        spikes = np.split(st, idx[:-1])
        wf = np.asarray(f["units/waveform_mean"][:])
        ct = np.array([c.decode() if isinstance(c, bytes) else c for c in f["units/cell_type"][:]])
        rate = float(f["units/sampling_rate"][0])
        oi = f["units/obs_intervals"][:]
        obs = np.split(oi, f["units/obs_intervals_index"][:][:-1])
        cols = [c.decode() if isinstance(c, bytes) else str(c) for c in f["units"].attrs["colnames"]]
        groups = {k: sorted(f[k].keys()) for k in f.keys() if isinstance(f[k], h5py.Group)}
        for k in ("stimulus/presentation", "stimulus/templates"):
            if k in f:
                groups[k] = sorted(f[k].keys())
        site = list(nwb.ogen_sites.values())[0]
        sloc = json.loads(site.location)
        eg = list(nwb.electrode_groups.values())[0]
        eloc = json.loads(eg.location)
        s = Session(path=asset.path, subject=nwb.subject.subject_id, genotype=nwb.subject.genotype,
                    site=site.name, site_hemisphere=sloc.get("hemisphere"),
                    rec_ml=eloc.get("rec_coordinate_ml"), trials=trials.drop(columns=["session_directory"]),
                    spikes=spikes, waveforms=wf, cell_type=ct, wf_rate=rate, obs_intervals=obs,
                    units_columns=cols, groups=groups)
        s.trials["session_file"] = trials["session_directory"].str.split("/").str[-1]
        io.close()
    return s


def load_all(max_workers: int = 6) -> list[Session]:
    assets = asset_list()
    with ThreadPoolExecutor(max_workers) as ex:
        return list(ex.map(_read, assets))


# ---------------------------------------------------------------- trials

def add_trial_fields(t: pd.DataFrame) -> pd.DataFrame:
    """Instructed side, choice, outcome and epoch durations from the trials table."""
    t = t.copy()
    r = t["response"].astype(str)
    t["instructed"] = np.where(r.isin(["HitR", "ErrL", "NoLickR"]), "R",
                               np.where(r.isin(["HitL", "ErrR", "NoLickL"]), "L", "?"))
    t["correct"] = r.str.startswith("Hit")
    t["error"] = r.str.startswith("Err")
    t["nolick"] = r.str.startswith("NoLick")
    t["lick"] = t["correct"] | t["error"]
    t["choice"] = np.where(r.isin(["HitR", "ErrR"]), "R", np.where(r.isin(["HitL", "ErrL"]), "L", "-"))
    t["sample_s"] = t["pole_out_time"] - t["pole_in_time"]
    t["delay_s"] = t["cue_time"] - t["pole_out_time"]
    t["standard"] = (t["sample_s"].sub(EPOCH_S).abs() < 0.01) & (t["delay_s"].sub(EPOCH_S).abs() < 0.01)
    t["stim"] = t["photo_stim_id"].astype(str)
    return t


# ---------------------------------------------------------------- units

def spike_width_ms(wf: np.ndarray, rate: float) -> np.ndarray:
    """Trough-to-peak interval of each mean waveform (E1), in ms. The peak is the maximum after
    the trough."""
    out = np.full(len(wf), np.nan)
    for i, w in enumerate(wf):
        w = np.asarray(w, float)
        if not np.all(np.isfinite(w)) or w.size < 3:
            continue
        tr = int(np.argmin(w))
        if tr >= w.size - 1:
            continue
        pk = tr + int(np.argmax(w[tr:]))
        out[i] = (pk - tr) / rate * 1000.0
    return out


def counts(spk: np.ndarray, starts: np.ndarray, stops: np.ndarray) -> np.ndarray:
    """Spike counts of one unit in [start, stop) windows."""
    return np.searchsorted(spk, stops) - np.searchsorted(spk, starts)


def binned(spk: np.ndarray, align: np.ndarray, t0: float, t1: float, width: float, step: float):
    """Spike counts of one unit per trial in sliding windows [c - width/2, c + width/2), window
    centres from t0 to t1 in `step`, relative to the `align` time of each trial. Returns
    (centres, counts[trials, windows])."""
    centres = np.arange(t0, t1 + step / 2, step)
    lo = align[:, None] + centres[None, :] - width / 2
    hi = lo + width
    c = np.searchsorted(spk, hi.ravel()) - np.searchsorted(spk, lo.ravel())
    return centres, c.reshape(lo.shape)


def ttest_p(a: np.ndarray, b: np.ndarray, axis=0) -> np.ndarray:
    """Two-tailed t-test p (pooled variance, scipy default), nan-safe: 1 where
    both groups have zero variance and equal means."""
    with np.errstate(all="ignore"):
        p = stats.ttest_ind(a, b, axis=axis).pvalue
    p = np.asarray(p, float)
    p[~np.isfinite(p)] = 1.0
    return p


# ---------------------------------------------------------------- bootstrap

def hierarchical_bootstrap(trials: pd.DataFrame, value: str, condition: str, a, b, n_boot: int,
                           rng: np.random.Generator, group_cols=("subject", "session")):
    """B1: resample mice, then sessions within each mouse, then trials within each session, with
    replacement; return the observed change (mean of `value` in condition b minus a, pooled over
    the resampled trials) and the bootstrap distribution of the change. The one-tailed p-value
    is the fraction of resamples whose change has the sign opposite to the observed one."""
    m, s = group_cols
    data = {}
    for (mm, ss), g in trials.groupby([m, s]):
        va = g.loc[g[condition] == a, value].to_numpy(float)
        vb = g.loc[g[condition] == b, value].to_numpy(float)
        data.setdefault(mm, []).append((va, vb))
    mice = list(data)

    def change(sel):
        sa = sb = na = nb = 0.0
        for va, vb in sel:
            sa += va.sum(); na += va.size; sb += vb.sum(); nb += vb.size
        return (sb / nb if nb else np.nan) - (sa / na if na else np.nan)

    obs = change([x for mm in mice for x in data[mm]])
    out = np.empty(n_boot)
    for k in range(n_boot):
        sel = []
        for mm in rng.choice(len(mice), len(mice)):
            sess = data[mice[mm]]
            for si in rng.choice(len(sess), len(sess)):
                va, vb = sess[si]
                sel.append((va[rng.integers(0, va.size, va.size)] if va.size else va,
                            vb[rng.integers(0, vb.size, vb.size)] if vb.size else vb))
        out[k] = change(sel)
    out = out[np.isfinite(out)]
    p = float(np.mean(out >= 0)) if obs < 0 else float(np.mean(out <= 0))
    return obs, out, p


def onset_latency(delta: np.ndarray, centres_ms: np.ndarray, p: float, n_boot: int,
                  rng: np.random.Generator, search_from_ms: float = 0.0):
    """E5: `delta` is [neurons, bins] of sign-flipped firing rate change. Onset is the first bin
    centre at or after `search_from_ms` where the mean over neurons differs from 0 by a
    two-tailed one-sample t-test at p. Neurons are resampled with replacement `n_boot` times;
    returns the observed onset, the bootstrap mean and s.d., and the number of resamples with no
    onset."""
    keep = centres_ms >= search_from_ms

    def first(d):
        with np.errstate(all="ignore"):
            pv = stats.ttest_1samp(d[:, keep], 0.0, axis=0).pvalue
        m = d[:, keep].mean(0)
        hit = np.where((pv < p) & (m > 0))[0]
        return centres_ms[keep][hit[0]] if hit.size else np.nan

    obs = first(delta)
    boots = np.array([first(delta[rng.integers(0, len(delta), len(delta))]) for _ in range(n_boot)])
    return obs, float(np.nanmean(boots)), float(np.nanstd(boots)), int(np.isnan(boots).sum())


# ---------------------------------------------------------------- sessions and groups

# The files do not describe photo_stim_id. The codes are read from the data (notebook, data
# check): the ALM response to codes 1 and 3 starts at sample onset and to codes 2, 4, 5 and 6
# at delay onset; codes 1 and 2 occur only in sessions whose ogen site is the fastigial nucleus
# in wild-type mice, 3 and 4 only with the dentate site, 5 and 6 only in L7-cre x Ai32 mice.
# This matches the Methods: CN photo-activation at the start of the sample or delay epoch
# (0.455 s) and CN photo-inhibition from delay onset for 1.3 s at 1.5 or 4.5 mW (two codes;
# which power is which is not known, and the claims pool them).
CODE_EPOCH = {"1": "sample", "2": "delay", "3": "sample", "4": "delay", "5": "delay", "6": "delay"}
ACTIVATION_S = 0.455     # Methods, CN ChR2 photo-activation
INHIBITION_S = 1.3       # Methods, CN photo-inhibition during ALM recordings


def session_group(s: Session) -> str:
    codes = set(s.trials["photo_stim_id"].astype(str)) - {"0"}
    if codes <= {"5", "6"}:
        return "inhibition"
    if codes <= {"1", "2"}:
        return "fastigial"
    if codes <= {"3", "4"}:
        return "dentate"
    return "mixed"


def delay_code(group: str) -> list[str]:
    return {"inhibition": ["5", "6"], "fastigial": ["2"], "dentate": ["4"]}[group]


def sample_code(group: str) -> list[str]:
    return {"fastigial": ["1"], "dentate": ["3"]}.get(group, [])


@dataclass
class Prep:
    """One session reduced to what the analyses use: trials without lick early, putative
    pyramidal units (E1) and their epoch spike counts."""
    idx: int
    path: str
    subject: str
    group: str
    hemisphere: str
    t: pd.DataFrame
    units: np.ndarray          # unit indices into Session.spikes
    spikes: list = field(repr=False)
    ep: dict = field(repr=False)   # epoch name -> counts [units, trials]
    n_unobserved: int = 0      # trials (no lick early) left out as outside the units' obs_intervals


def epoch_windows(t: pd.DataFrame) -> dict:
    w = {"sample": (t.pole_in_time, t.pole_out_time), "delay": (t.pole_out_time, t.cue_time),
         "delay_last500": (t.cue_time - 0.5, t.cue_time),
         "delay_first500": (t.pole_out_time, t.pole_out_time + 0.5),
         "delay_after_act": (t.pole_out_time + ACTIVATION_S, t.cue_time),
         "act_period": (t.pole_out_time, t.pole_out_time + ACTIVATION_S)}
    for r in RESPONSE_WINDOWS:
        w[f"response{r}"] = (t.cue_time, t.cue_time + r)
    return {k: (np.asarray(a, float), np.asarray(b, float)) for k, (a, b) in w.items()}


def observed(s: Session) -> np.ndarray:
    """Trials that lie inside the observation intervals of every unit of the session. Spikes
    are only recorded inside them (in one session the recording ends before the behavior does)."""
    t = s.trials
    a, b = t["start_time"].to_numpy(float), t["stop_time"].to_numpy(float)
    ok = np.ones(len(t), bool)
    for iv in s.obs_intervals:
        inside = np.zeros(len(t), bool)
        for lo, hi in iv:
            inside |= (a >= lo - 1e-6) & (b <= hi + 1e-6)
        ok &= inside
    return ok


def prepare(S: list[Session], use_file_cell_type: bool = False) -> list[Prep]:
    """Neural analyses use trials without lick early inside the units' observation intervals;
    the behavior analyses take every trial of the session (notebook)."""
    out = []
    for i, s in enumerate(S):
        t = add_trial_fields(s.trials)
        keep = (t["lick_early"] == 0).to_numpy()
        n_out = int((keep & ~observed(s)).sum())
        t = t[keep & observed(s)].reset_index(drop=True)
        if use_file_cell_type:
            units = np.where(s.cell_type == "pyramidal")[0]
        else:
            units = np.where(spike_width_ms(s.waveforms, s.wf_rate) > PYR_MIN_MS)[0]
        wins = epoch_windows(t)
        ep = {k: np.array([counts(s.spikes[u], a, b) for u in units]).reshape(len(units), len(t))
              for k, (a, b) in wins.items()}
        out.append(Prep(i, s.path, s.subject, session_group(s), s.site_hemisphere, t, units,
                        [s.spikes[u] for u in units], ep, n_out))
    return out


def selective(p: Prep, trials: str, response_s: float, mask=None) -> np.ndarray:
    """E2 per unit, on control trials: any of sample, delay, response epochs with p < 0.05,
    "lick right" against "lick left". trials 'correct' (reading a) or 'all' (reading b, trials
    with a lick, by instructed side). Returns a boolean array and the per-epoch p-values."""
    t = p.t
    base = (t.stim == "0") & (t.correct if trials == "correct" else t.lick)
    if mask is not None:
        base &= mask
    r = (base & (t.instructed == "R")).to_numpy()
    l = (base & (t.instructed == "L")).to_numpy()
    ps = {}
    for e in ("sample", "delay", f"response{response_s}"):
        c = p.ep[e]
        ps[e] = ttest_p(c[:, r], c[:, l], axis=1) if r.sum() > 1 and l.sum() > 1 else np.ones(len(c))
    sel = np.zeros(len(p.units), bool)
    for v in ps.values():
        sel |= v < P_SELECT
    return sel, ps


def pop_selectivity(rates_by_type: dict, pref_counts: dict, rng: np.random.Generator,
                    n_pref: int, per_type: bool):
    """E3 for one unit. rates_by_type: {'R': [trials, bins], 'L': [...]} of rates for the
    trials the selectivity is computed on (control); pref_counts: {'R': counts, 'L': counts} per
    trial in the epoch that fixes the preference. `n_pref` trials (of each type if per_type,
    else in all, split evenly) fix the preferred type and are left out. Returns the
    held-out trial indices, the preferred side and the selectivity time course."""
    used = {}
    for side in ("R", "L"):
        n = len(pref_counts[side])
        k = n_pref if per_type else n_pref // 2
        used[side] = rng.choice(n, min(k, n), replace=False)
    m = {side: pref_counts[side][used[side]].mean() for side in ("R", "L")}
    pref = "R" if m["R"] >= m["L"] else "L"
    non = "L" if pref == "R" else "R"
    keep = {side: np.setdiff1d(np.arange(len(pref_counts[side])), used[side]) for side in ("R", "L")}
    sel = rates_by_type[pref][keep[pref]].mean(0) - rates_by_type[non][keep[non]].mean(0)
    return keep, pref, sel


def boot_mean_ci(x: np.ndarray, rng: np.random.Generator, n_boot: int = 1000, axis0=True):
    """Mean over rows and the bootstrap 95% interval over rows (neurons or sessions)."""
    x = np.asarray(x, float)
    idx = rng.integers(0, len(x), (n_boot, len(x)))
    bm = np.array([x[i].mean(0) for i in idx])
    return x.mean(0), np.percentile(bm, 2.5, axis=0), np.percentile(bm, 97.5, axis=0), bm.std(0)
