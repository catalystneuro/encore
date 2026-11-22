"""Loading and population-coupling measures for the ALM silicon-probe recordings of DANDI:000010.

Gable et al. (2026), J Neurosci, doi:10.1523/jneurosci.0974-26.2026, reanalyse these recordings
(Li, Chen, Guo, Gerfen & Svoboda 2015) for Figure S4 and Table 5. Each ecephys NWB file holds one
session: a trials table (start and stop time, instructed side, early lick, outcome), the sample,
delay and GO times and the photostimulation onsets as BehavioralEvents, and spike-sorted units
with spike times, a quality label and the intervals in which each unit was observed (the trials).
Files are streamed from the archive at the pinned version; nothing is written to disk.

Where the parameters come from (the claims file, claims/gable-2026.yaml, names E1 to E8 and the
open details O1 to O5; it cites the paper's Methods, "Secondary analysis of electrophysiology
dataset" (SA), the Statistics section (ST), and the paper's code, github.com/kerlin-lab/Gable_2026
at commit 688e662, Figures/sled_glutamate_functions.py):

- `MIN_UNITS = 18` and `MIN_RATE_HZ = 0.5`: the session filter (E1, SA).
- Only units whose quality label is "good" (E2, SA: "Only high-quality units, as labeled in the
  original dataset").
- `BIN_S = 0.005`, `SIGMA_BINS = 2`, `RADIUS_BINS = 4`: 5 ms bins smoothed by a Gaussian of
  sigma 2 bins and 20 ms radius (E4, SA). Smoothing is applied within each trial's window (O4,
  a standard choice).
- `POST_GO_S = 2.0`: the window runs from sample onset to 2 s after the GO cue (E4, SA).
- Trial-specific activity subtracts the trial-type mean (E5; Methods, Activity extraction).
- Population coupling is the Pearson correlation of a neuron's flattened TSA with the summed TSA
  of all other neurons of the session (E6; code calculate_ephys_population_coupling), and the
  pooled values are cut at the k/7 percentiles, a value equal to an edge going to the lower bin.
- Pairs and their correlations follow E7 (code _ephys_cluster_synchy).
- The bootstrap follows E8 (code _spont_group_boot_iter and corrXCoupling_ephys_v3): each group
  is resampled on its own, `N_BOOT` = 10,000 kept draws; p = (count(d <= 0) + 1) / (n + 1); Holm
  across the 7 bins.
- Common window length (O5): windows from sample onset to GO + 2 s differ in length, as an early
  lick restarts the delay. Every trial takes `WINDOW_S` = 4.6 s from its sample onset, the
  window of a trial with the task's 1.3 s sample and 1.3 s delay epochs and the shortest
  window among the trials of the four types (the standard choice the claims file names). A
  trial whose GO + 2 s comes earlier, or whose window runs past the end of its observation
  interval (after which no spikes are stored), is dropped, as the code's NaN trial filter (E3)
  would drop it.
- Spike times are sorted on loading; a few units store them out of order.
"""

from __future__ import annotations

import itertools
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy.ndimage import gaussian_filter1d

DANDISET_ID = "000010"
DANDISET_VERSION = "0.220126.1905"

MIN_UNITS = 18
MIN_RATE_HZ = 0.5
BIN_S = 0.005
SIGMA_BINS = 2
RADIUS_BINS = 4
POST_GO_S = 2.0
WINDOW_S = 4.6
N_BINS = int(round(WINDOW_S / BIN_S))
N_SLICES = 7
N_BOOT = 10_000

# Strain labels of the subject description: KJ18 is the Sim1-Cre line, PL56 the Tlx3-Cre line.
SIM1_STRAIN = "kj18"
TLX_STRAIN = "pl56"


def _dec(x):
    return x.decode() if isinstance(x, bytes) else x


def ecephys_assets():
    """Path and S3 URL of every ecephys NWB file at the pinned version."""
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        out = [(a.path, a.get_content_url(follow_redirects=1, strip_query=True))
               for a in ds.get_assets() if "ecephys" in a.path]
    return sorted(out)


def load_session(path, url):
    """Read one session: subject, trials with their event times, and every unit's spikes."""
    f = h5py.File(remfile.File(url), "r")
    subj = f["general/subject"]
    tr = f["intervals/trials"]
    trials = pd.DataFrame({
        "start": tr["start_time"][:], "stop": tr["stop_time"][:],
        "instruction": [_dec(x) for x in tr["trial_instruction"][:]],
        "early_lick": [_dec(x) for x in tr["early_lick"][:]],
        "outcome": [_dec(x) for x in tr["outcome"][:]],
        "task": [_dec(x) for x in tr["task"][:]],
    })
    starts, stops = trials.start.to_numpy(), trials.stop.to_numpy()
    events = f["acquisition/BehavioralEvents"]
    n_unmatched = {}
    for name in ["sample", "delay", "go", "photostim_start_time"]:
        col = np.full(len(trials), np.nan)
        if name in events:
            ts = events[name]["timestamps"][:]
            i = np.searchsorted(starts, ts, side="right") - 1
            ok = (i >= 0) & (ts <= stops[np.clip(i, 0, None)])
            col[i[ok]] = ts[ok]
            n_unmatched[name] = int((~ok).sum())
        trials[name] = col
    u = f["units"]
    ids = u["id"][:]
    st_idx = u["spike_times_index"][:]
    st = u["spike_times"][:]
    oi_idx = u["obs_intervals_index"][:]
    oi = u["obs_intervals"][:]
    spikes, obs, unsorted = [], [], 0
    for j in range(len(ids)):
        a = st_idx[j - 1] if j else 0
        s = st[a:st_idx[j]]
        if np.any(np.diff(s) < 0):
            unsorted += 1
            s = np.sort(s)
        spikes.append(s)
        b = oi_idx[j - 1] if j else 0
        obs.append(oi[b:oi_idx[j]])
    units = pd.DataFrame({
        "id": ids, "quality": [_dec(x) for x in u["quality"][:]],
        "cell_type": [_dec(x) for x in u["cell_type"][:]],
        "n_spikes": [len(s) for s in spikes],
        "observed_s": [float(np.sum(o[:, 1] - o[:, 0])) for o in obs],
    })
    sub = path.split("/")[0]
    return {
        "path": path, "subject": sub, "session": path.split("_ses-")[1].split("_")[0],
        "genotype": _dec(subj["genotype"][()]), "strains": _dec(subj["description"][()]),
        "sex": _dec(subj["sex"][()]),
        "trials": trials, "units": units, "spikes": spikes, "obs": obs,
        "unmatched_events": n_unmatched, "unsorted_units": unsorted,
    }


def load_all(assets, workers=8):
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(lambda a: load_session(*a), assets))


def strain_group(strains):
    """'Sim1' for KJ18 mice, 'Tlx' for PL56 mice, else None (Rbp4 KL100)."""
    s = strains.lower()
    if SIM1_STRAIN in s:
        return "Sim1"
    if TLX_STRAIN in s:
        return "Tlx"
    return None


def trial_type(trials, reading):
    """Trial type per trial, or None for a trial left out.

    Reading "a" of O3 keeps the four types CL, CR, IL, IR (hit or miss, left or right
    instruction; early-lick and no-response trials left out). Reading "b" keeps every trial with
    a sample and GO time, the early-lick and no-response trials grouped by instruction and
    outcome with their own mean. Labelling by instruction or by lick side gives the same four
    groups, as an incorrect right trial is a left lick.
    """
    out = []
    for ins, early, oc in zip(trials.instruction, trials.early_lick, trials.outcome):
        if ins not in ("left", "right"):
            out.append(None if reading == "a" else f"{oc}-{ins}")
            continue
        side = "L" if ins == "left" else "R"
        if oc in ("hit", "miss") and early == "no early":
            out.append(("C" if oc == "hit" else "I") + side)
        elif reading == "b":
            out.append(f"{oc}-{early}-{side}")
        else:
            out.append(None)
    return out


def session_rates(ses, trial_mask, window_s):
    """Each unit's rate under the two readings of O2.

    (a) spike count over the time the unit was observed (the files hold spikes only within the
    trials' observation intervals, so this is the rate over the recording); (b) mean rate within
    the analysis windows of the included trials.
    """
    tr = ses["trials"][trial_mask]
    t0 = tr["sample"].to_numpy()
    rate_a = (ses["units"].n_spikes / ses["units"].observed_s).to_numpy()
    rate_b = np.array([
        np.sum([np.count_nonzero((s >= a) & (s < a + window_s)) for a in t0]) / (len(t0) * window_s)
        if len(t0) else np.nan for s in ses["spikes"]])
    return rate_a, rate_b


def binned_activity(spikes, onsets, n_bins):
    """Spike counts in 5 ms bins from each onset, smoothed within the trial (O4)."""
    edges = np.arange(n_bins + 1) * BIN_S
    out = np.empty((len(spikes), len(onsets), n_bins))
    for i, s in enumerate(spikes):
        for k, a in enumerate(onsets):
            lo, hi = np.searchsorted(s, [a, a + n_bins * BIN_S])
            out[i, k] = np.histogram(s[lo:hi] - a, edges)[0]
    return gaussian_filter1d(out, SIGMA_BINS, axis=2, mode="constant",
                             truncate=RADIUS_BINS / SIGMA_BINS)


def tsa(act, types):
    """Subtract each trial type's mean (neurons x trials x bins)."""
    out = act.copy()
    types = np.asarray(types)
    for t in np.unique(types):
        m = types == t
        out[:, m] -= act[:, m].mean(axis=1, keepdims=True)
    return out


def population_coupling(x):
    """Pearson r of each neuron's flattened TSA with the summed TSA of the others (E6)."""
    flat = x.reshape(x.shape[0], -1)
    total = flat.sum(0)
    return np.array([np.corrcoef(total - flat[i], flat[i])[0, 1] for i in range(len(flat))])


def coupling_bins(coupling_by_session, n_slices=N_SLICES):
    """Pooled k/n percentiles; a value equal to an edge goes to the lower bin (code)."""
    pooled = np.concatenate(coupling_by_session)
    edges = [np.nanpercentile(pooled, i * 100 / n_slices) for i in range(1, n_slices)]
    return [np.searchsorted(edges, c, side="left") for c in coupling_by_session], edges


def pair_correlations(x, labels, n_slices=N_SLICES):
    """Per bin, the same-range and different-range pair correlations of one session (E7)."""
    flat = x.reshape(x.shape[0], -1)
    r = np.corrcoef(flat)
    same = [[] for _ in range(n_slices)]
    diff = [[] for _ in range(n_slices)]
    for i, j in itertools.combinations(range(len(flat)), 2):
        a, b = int(labels[i]), int(labels[j])
        if a == b:
            same[a].append(r[i, j])
        else:
            diff[a].append(r[i, j])
            diff[b].append(r[i, j])
    return [np.array(v) for v in same], [np.array(v) for v in diff]


def group_bootstrap(values_by_session, rng, n_boot=N_BOOT, batch=20_000):
    """Kept bootstrap means of one group (code _spont_group_boot_iter).

    Draw as many sessions as there are, with replacement; pool their values; keep the draw only
    if the pool holds at least the observed number of values; reduce with nanmean.
    """
    n = np.array([len(v) for v in values_by_session])
    s = np.array([np.nansum(v) for v in values_by_session])
    c = np.array([np.count_nonzero(~np.isnan(v)) for v in values_by_session])
    n_obs, k = n.sum(), len(n)
    kept = []
    total = 0
    while total < n_boot:
        idx = rng.integers(0, k, size=(batch, k))
        ok = n[idx].sum(1) >= n_obs
        cnt = c[idx].sum(1)[ok]
        m = np.where(cnt > 0, s[idx].sum(1)[ok] / np.maximum(cnt, 1), np.nan)
        kept.append(m)
        total += len(m)
    return np.concatenate(kept)[:n_boot]


def holm(p):
    """Holm-adjusted p-values (as statsmodels multipletests 'holm')."""
    p = np.asarray(p, float)
    order = np.argsort(p)
    m = len(p)
    adj = np.empty(m)
    running = 0.0
    for rank, i in enumerate(order):
        running = max(running, (m - rank) * p[i])
        adj[i] = min(running, 1.0)
    return adj


def same_vs_diff_test(same_by_bin, diff_by_bin, rng, n_boot=N_BOOT):
    """E8 per bin: mean difference, one-tailed p (same > different), Holm across bins."""
    rows = []
    for k in range(len(same_by_bin)):
        a = group_bootstrap(same_by_bin[k], rng, n_boot)
        b = group_bootstrap(diff_by_bin[k], rng, n_boot)
        d = a - b
        d = d[~np.isnan(d)]
        p = (np.count_nonzero(d <= 0) + 1) / (len(d) + 1)
        rows.append({"bin": k, "n_same": int(sum(len(v) for v in same_by_bin[k])),
                     "n_diff": int(sum(len(v) for v in diff_by_bin[k])),
                     "same_mean": float(np.nanmean(a)), "diff_mean": float(np.nanmean(b)),
                     "mean_difference": float(d.mean()), "p_one_tailed": p})
    out = pd.DataFrame(rows)
    out["p_holm"] = holm(out.p_one_tailed)
    return out


def unique_units(ses):
    """Indices of units, counting once a unit whose spike train is stored twice in the file."""
    keep, seen = [], set()
    for j, s in enumerate(ses["spikes"]):
        key = (len(s), s.tobytes())
        if key not in seen:
            seen.add(key)
            keep.append(j)
    return np.array(keep)


def observed_until(ses):
    """End of the observation interval that starts at each trial's start (NaN when none).

    The units of a file share their observation intervals (checked in the notebook); they start
    at the trial start and last 5.5 s, while the trial's stop time can be earlier or later.
    """
    ob = ses["obs"][0]
    starts = ses["trials"]["start"].to_numpy()
    i = np.clip(np.searchsorted(ob[:, 0], starts), 0, len(ob) - 1)
    return np.where(np.isclose(ob[i, 0], starts), ob[i, 1], np.nan)


def included_trials(ses, o3):
    """Mask and types of the trials analysed: not photostimulated (E3), of a type kept under
    reading o3, with a full common window inside the trial (O5)."""
    tr = ses["trials"]
    types = trial_type(tr, o3)
    m = np.array([t is not None for t in types])
    m &= tr["sample"].notna().to_numpy() & tr["go"].notna().to_numpy()
    m &= tr["photostim_start_time"].isna().to_numpy()
    m &= (tr["go"] + POST_GO_S - tr["sample"] >= WINDOW_S - BIN_S / 2).to_numpy()
    m &= (tr["sample"] + WINDOW_S <= observed_until(ses)).to_numpy()
    return m, np.array(types, dtype=object)[m]


def select_session(ses, o1, o2, o3, dedupe=True):
    """Apply E1 to E3 under readings o1, o2 and o3; return the units and trials kept."""
    units = ses["units"]
    idx = unique_units(ses) if dedupe else np.arange(len(units))
    idx = idx[(units.quality.to_numpy()[idx] == "good")]
    m, types = included_trials(ses, o3)
    rate_a, rate_b = session_rates(ses, m, WINDOW_S)
    rate = (rate_a if o2 == "a" else rate_b)[idx]
    above = idx[rate > MIN_RATE_HZ]
    passes = len(above) >= MIN_UNITS
    chosen = idx if o1 == "a" else above
    return {"passes": bool(passes), "units": chosen, "n_good": len(idx), "n_above": len(above),
            "trial_mask": m, "types": types}


def session_tsa(ses, sel):
    """TSA array (neurons x trials x bins) of the selected units and trials."""
    onsets = ses["trials"]["sample"].to_numpy()[sel["trial_mask"]]
    act = binned_activity([ses["spikes"][j] for j in sel["units"]], onsets, N_BINS)
    return tsa(act, sel["types"])


def analyse(sessions, o1, o2, o3, dedupe=True):
    """Selection, TSA, coupling, bins and pair correlations under one reading of O1 to O3.

    Only sessions of Sim1 (KJ18) and Tlx (PL56) mice are used (E1).
    """
    kept, x_by_session = [], []
    for ses in sessions:
        group = strain_group(ses["strains"])
        if group is None:
            continue
        sel = select_session(ses, o1, o2, o3, dedupe)
        if not sel["passes"]:
            continue
        kept.append({"subject": ses["subject"], "session": ses["session"], "path": ses["path"],
                     "group": group, "ai32": "ai32" in ses["strains"],
                     "n_units": len(sel["units"]), "n_trials": int(sel["trial_mask"].sum()),
                     "types": pd.Series(sel["types"]).value_counts().to_dict()})
        x_by_session.append(session_tsa(ses, sel))
    coupling = [population_coupling(x) for x in x_by_session]
    labels, edges = coupling_bins(coupling)
    same = [[] for _ in range(N_SLICES)]
    diff = [[] for _ in range(N_SLICES)]
    for x, lab in zip(x_by_session, labels):
        s, d = pair_correlations(x, lab)
        for k in range(N_SLICES):
            same[k].append(s[k])
            diff[k].append(d[k])
    return {"sessions": pd.DataFrame(kept), "coupling": coupling, "labels": labels,
            "edges": edges, "same": same, "diff": diff}


def decode_side(ses, units, trial_mask, align, windows, shift_labels=False, n_folds=5):
    """Balanced accuracy of decoding the instructed side of correct trials from spike counts.

    A clock check (protocol, step 2): nearest class mean on z-scored counts in each window
    (seconds from the `align` event), with interleaved folds (trial k in fold k mod n_folds), so
    no random draw is involved. With `shift_labels`, each trial takes the next trial's label.
    """
    tr = ses["trials"]
    m = trial_mask & (tr.outcome == "hit").to_numpy() & (tr.early_lick == "no early").to_numpy()
    y = (tr.instruction.to_numpy()[m] == "right").astype(int)
    if shift_labels:
        y = np.roll(y, -1)[:-1]
    t0 = tr[align].to_numpy()[m]
    out = []
    for a, b in windows:
        X = np.array([[np.count_nonzero((s >= t + a) & (s < t + b)) for t in t0]
                      for s in (ses["spikes"][j] for j in units)], float).T
        if shift_labels:
            X = X[:-1]
        fold = np.arange(len(y)) % n_folds
        pred = np.empty(len(y), int)
        for k in range(n_folds):
            tr_, te = fold != k, fold == k
            mu, sd = X[tr_].mean(0), X[tr_].std(0) + 1e-9
            Z = (X - mu) / sd
            c0, c1 = Z[tr_ & (y == 0)].mean(0), Z[tr_ & (y == 1)].mean(0)
            pred[te] = (((Z[te] - c1) ** 2).sum(1) < ((Z[te] - c0) ** 2).sum(1)).astype(int)
        out.append(0.5 * (np.mean(pred[y == 0] == 0) + np.mean(pred[y == 1] == 1)))
    return np.array(out)


def laser_max_per_trial(url, trials):
    """Largest laser power (the file's unit, mW) within each trial, from the stored trace."""
    f = h5py.File(remfile.File(url), "r")
    pres = f["stimulus/presentation"]
    names = [k for k in pres if k.endswith("laser_power")]
    out = np.zeros(len(trials))
    for name in names:
        d, t = pres[name]["data"][:], pres[name]["timestamps"][:]
        lo = np.searchsorted(t, trials.start.to_numpy())
        hi = np.searchsorted(t, trials.stop.to_numpy())
        out = np.maximum(out, [d[a:b].max() if b > a else 0.0 for a, b in zip(lo, hi)])
    return out, names


def by_mouse_differences(result):
    """Per mouse and bin, mean same-range minus mean different-range pair correlation (no test)."""
    rows = []
    subjects = result["sessions"].subject.to_numpy()
    for sub in np.unique(subjects):
        idx = np.where(subjects == sub)[0]
        row = {"subject": sub, "sessions": len(idx)}
        for k in range(N_SLICES):
            s = np.concatenate([result["same"][k][i] for i in idx])
            d = np.concatenate([result["diff"][k][i] for i in idx])
            row[f"bin{k + 1}"] = np.nanmean(s) - np.nanmean(d) if len(s) and len(d) else np.nan
            row[f"n_same{k + 1}"] = len(s)
        rows.append(row)
    return pd.DataFrame(rows)
