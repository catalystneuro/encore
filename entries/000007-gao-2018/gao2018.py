"""Loading and measures for the ALM recordings of dandiset 000007.

Gao, Davis, Thomas, Economo, Abrego, Svoboda, De Zeeuw & Li (2018), Nature,
doi:10.1038/s41586-018-0633-x.

Each NWB file holds one session of ALM recording in a head-fixed mouse doing the delayed
response task: the sorted units (spike times, a cell type label, the mean waveform) and a trial
table with the times of pole in (sample start), pole out (delay start) and the go cue (delay
end), the outcome (`response`), early licks, and a photostimulation code (`photo_stim_id`).
The trial times are on the session clock, as are the spike times. Files are streamed from the
archive at the pinned version; nothing is written to disk.

Where the parameters come from:

- Epochs, from the Methods and the paper's CN analysis scripts (`analyses_scripts.zip` of Zenodo
  record doi:10.5281/zenodo.6653158, `analysis_compile_all_DCN_data.m`): sample is pole in to
  pole out, delay is pole out to the cue, response is the cue to 1.3 s after it.
- Trial selection, from the same scripts: trials with an early lick are left out, and for each
  unit only the trials from the first to the last trial in which it fired ("stable trials").
  The scripts also drop trials marked as not performing (`GoodTrials`); the dandiset has no such
  column (see the data check).
- Trial type: the R or L in `response` (HitR, ErrR, NoLickR) is the instructed side, as in the
  scripts, where "yes" trials are HitR or ErrR and the analysis of photostimulation groups
  correct and error trials by instructed type (Methods).
- Selectivity test: two-tailed t-test on spike rates of correct trials, lick right against lick
  left, in each epoch, p < 0.05 in any epoch (Methods and scripts). Preferred trial type from a
  random subset of trials (10 per type for ALM, Methods; the scripts use 20 for CN and require 30
  correct trials of each type), selectivity on the rest.
- Cell types: trough-to-peak width of the mean waveform, below 0.35 ms fast spiking, above
  0.45 ms putative pyramidal, in between left out (Methods).
- Photostimulation effect on a unit: two-tailed t-test of spike counts, control against
  photostimulation trials, trial types pooled (Methods); p < 0.01.
- Onset latency (Extended Data Fig. 9a): rate change in 10 ms bins stepped by 1 ms, the sign of
  suppressed units flipped, onset as the first bin where the population change differs from 0
  (t-test p < 0.01), resampled over units 10,000 times. The window searched (from photostimulus
  onset to 100 ms after it) is a choice made here; the Methods do not give one.
- Coding direction (Methods): mean spike counts in 400 ms windows stepped by 10 ms, the
  difference of the lick right and lick left means, averaged over the delay epoch, from correct
  control trials; projections on held-out trials.
- Behavioural performance: fraction correct, without early-lick and no-lick trials; the
  hierarchical bootstrap over mice, sessions and trials (Methods), one-tailed.
- Names of the photostimulation codes: from the data description of the paper's Zenodo records
  (`data description_ALM4_ver2022.pdf` in doi:10.5281/zenodo.6647629 and 6653158), not from the
  dandiset, which leaves them undescribed.
"""

from __future__ import annotations

import json
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import stats

DANDISET_ID = "000007"
DANDISET_VERSION = "0.220126.1903"

RESPONSE_S = 1.3            # length of the response epoch after the cue (scripts)
SELECTIVE_P = 0.05
PHOTOSTIM_P = 0.01
ALM_SCREEN_TRIALS = 10      # Methods: trials per type used to pick the preferred type in ALM
NARROW_MS, WIDE_MS = 0.35, 0.45

# Photostimulation codes, from the data description of the paper's Zenodo records.
STIM_CODES = {
    0: ("control", None, None, None),
    1: ("fastigial photo-activation", "fastigial", "sample", 0.5),
    2: ("fastigial photo-activation", "fastigial", "delay", 0.5),
    3: ("dentate photo-activation", "dentate", "sample", 0.5),
    4: ("dentate photo-activation", "dentate", "delay", 0.5),
    5: ("CN photo-inhibition", "CN", "delay", 0.5),
    6: ("CN photo-inhibition", "CN", "delay", 1.3),
}


def _text(x):
    x = x[()] if hasattr(x, "shape") else x
    if isinstance(x, bytes):
        x = x.decode()
    return x


def asset_urls() -> dict[str, str]:
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return {a.path: a.get_content_url(follow_redirects=1, strip_query=True) for a in ds.get_assets()}


def load_session(path: str, url: str) -> dict:
    """Everything the analyses use from one file, read once."""
    f = h5py.File(remfile.File(url), "r")
    t = f["intervals/trials"]
    cols = [c.decode() if isinstance(c, bytes) else c for c in t.attrs["colnames"]]
    trials = pd.DataFrame({c: [_text(v) if isinstance(v, bytes) else v for v in t[c][:]] for c in cols
                           if c != "session_directory"})
    trials["stim"] = trials.pop("photo_stim_id").astype(int)
    trials["trial_type"] = trials.response.str[-1].map({"R": "R", "L": "L"})
    trials.loc[trials.response == "NoLickNoResponse", "trial_type"] = None
    trials["outcome"] = np.select([trials.response.str.startswith("Hit"), trials.response.str.startswith("Err")],
                                  ["hit", "error"], "nolick")
    u = f["units"]
    st = u["spike_times"][:]
    idx = u["spike_times_index"][:]
    spikes = np.split(st, idx[:-1])
    groups = [g for g in f["general/extracellular_ephys"] if g != "electrodes"]
    rec = json.loads(f["general/extracellular_ephys"][groups[0]].attrs["location"])
    opto = {g: json.loads(_text(f["general/optogenetics"][g]["location"])) for g in f["general/optogenetics"]}
    subject = path.split("/")[0].removeprefix("sub-")
    s = dict(
        path=path, subject=subject, session=path.split("_ses-")[1].removesuffix(".nwb"),
        genotype=_text(f["general/subject/genotype"]),
        virus=json.loads(_text(f["general/virus"]) or "[]"),
        opto=opto, probe=rec["probe_type"], rec_ml=float(rec["rec_coordinate_ml"]),
        trials=trials, spikes=spikes,
        cell_type=np.array([_text(x) for x in u["cell_type"][:]]),
        unit_rate_hz=u["sampling_rate"][:],
        waveform=u["waveform_mean"][:],
        obs=u["obs_intervals"][:],
        trial_descriptions={c: _text(t[c].attrs.get("description", "")) for c in cols},
        units_colnames=[c.decode() if isinstance(c, bytes) else c for c in u.attrs["colnames"]],
    )
    s["site"] = next(iter(opto)) if opto else None
    s["site_hemisphere"] = next(iter(opto.values()))["hemisphere"] if opto else None
    s["group"] = {"Fastigial": "FN", "Dentate": "DN"}.get(s["site"]) if s["genotype"] == "unknown" else "PI"
    f.close()
    return s


def load_all(workers: int = 8) -> list[dict]:
    urls = asset_urls()
    with ThreadPoolExecutor(workers) as ex:
        sessions = list(ex.map(lambda kv: load_session(*kv), sorted(urls.items())))
    return sessions


def spike_width_ms(waveform: np.ndarray, rate_hz: float) -> float:
    """Trough-to-peak interval of a mean waveform (Methods)."""
    trough = int(np.argmin(waveform))
    peak = trough + int(np.argmax(waveform[trough:]))
    return (peak - trough) / rate_hz * 1000.0


def counts(spikes: np.ndarray, starts, stops) -> np.ndarray:
    """Spike counts in [start, stop) for each pair, on the session clock."""
    starts, stops = np.asarray(starts, float), np.asarray(stops, float)
    return np.searchsorted(spikes, stops) - np.searchsorted(spikes, starts)


def stable_trials(spikes: np.ndarray, trials: pd.DataFrame) -> np.ndarray:
    """Trials from the first to the last one in which the unit fired (the scripts' rule)."""
    n = counts(spikes, trials.start_time, trials.stop_time)
    fired = np.flatnonzero(n > 0)
    keep = np.zeros(len(trials), bool)
    if len(fired):
        keep[fired[0]:fired[-1] + 1] = True
    return keep


def epoch_bounds(trials: pd.DataFrame) -> dict[str, tuple[np.ndarray, np.ndarray]]:
    return {"sample": (trials.pole_in_time.values, trials.pole_out_time.values),
            "delay": (trials.pole_out_time.values, trials.cue_time.values),
            "response": (trials.cue_time.values, trials.cue_time.values + RESPONSE_S)}


def epoch_rates(spikes, trials) -> pd.DataFrame:
    out = {}
    for name, (a, b) in epoch_bounds(trials).items():
        out[name] = counts(spikes, a, b) / (b - a)
    return pd.DataFrame(out, index=trials.index)


def selectivity_tests(s: dict, unit_mask=None) -> pd.DataFrame:
    """Per unit, t-test p of lick right against lick left (correct control trials) in each epoch."""
    tr = s["trials"]
    rows = []
    for i, sp in enumerate(s["spikes"]):
        if unit_mask is not None and not unit_mask[i]:
            continue
        ok = stable_trials(sp, tr) & (tr.lick_early == 0).values & (tr.stim == 0).values & (tr.outcome == "hit").values
        r = epoch_rates(sp, tr)
        right, left = ok & (tr.trial_type == "R").values, ok & (tr.trial_type == "L").values
        row = {"unit": i, "n_right": int(right.sum()), "n_left": int(left.sum())}
        for e in ("sample", "delay", "response"):
            if right.sum() >= 2 and left.sum() >= 2:
                row[f"p_{e}"] = stats.ttest_ind(r[e].values[right], r[e].values[left]).pvalue
                row[f"d_{e}"] = r[e].values[right].mean() - r[e].values[left].mean()
            else:
                row[f"p_{e}"], row[f"d_{e}"] = np.nan, np.nan
        rows.append(row)
    return pd.DataFrame(rows)


def psth(spikes, align, t_from, t_to, step=0.001, smooth=0.2):
    """Mean rate (spikes/s) around each alignment time, box-car of `smooth` s (the scripts' 200 ms)."""
    edges = np.arange(t_from - smooth, t_to + smooth + step / 2, step)
    h = np.zeros(len(edges) - 1)
    for t0 in align:
        lo, hi = np.searchsorted(spikes, [t0 + edges[0], t0 + edges[-1]])
        h += np.histogram(spikes[lo:hi] - t0, edges)[0]
    h = h / max(len(align), 1) / step
    k = int(round(smooth / step))
    sm = np.convolve(h, np.ones(k) / k, mode="same")
    centres = edges[:-1] + step / 2
    keep = (centres >= t_from) & (centres <= t_to)
    return centres[keep], sm[keep]


def binned_counts(spikes, align, centres, width):
    """Spike counts in windows of `width` s centred on `centres`, for each alignment time."""
    align = np.asarray(align, float)[:, None]
    a = align + np.asarray(centres)[None, :] - width / 2
    return (np.searchsorted(spikes, a + width) - np.searchsorted(spikes, a)).astype(float)


def performance(trials: pd.DataFrame) -> pd.DataFrame:
    """Trials that count for performance: no early lick, a lick after the cue."""
    t = trials[(trials.lick_early == 0) & (trials.outcome != "nolick") & trials.trial_type.notna()]
    return t.assign(correct=(t.outcome == "hit").astype(float))


def hierarchical_bootstrap(data: dict, n_conditions: int, n: int, rng: np.random.Generator) -> np.ndarray:
    """Resample mice, then sessions within mouse, then trials within session (Methods).

    `data` maps each mouse to a list of sessions, each a pair of arrays (y, k): a 0/1 outcome per
    trial and its condition (0 to n_conditions - 1). Returns, for each of the `n` resamples, the
    sum of y and the number of trials in each condition, shape (n, n_conditions, 2).
    """
    mice = list(data)
    out = np.zeros((n, n_conditions, 2))
    for b in range(n):
        for m in rng.choice(len(mice), len(mice)):
            sess = data[mice[m]]
            for j in rng.choice(len(sess), len(sess)):
                y, k = sess[j]
                pick = rng.integers(0, len(y), len(y))
                out[b, :, 0] += np.bincount(k[pick], weights=y[pick], minlength=n_conditions)
                out[b, :, 1] += np.bincount(k[pick], minlength=n_conditions)
    return out


def one_tailed_p(observed: float, resampled: np.ndarray) -> float:
    """Fraction of resamples whose change has the opposite sign to the observed one (Methods)."""
    resampled = resampled[np.isfinite(resampled)]
    return float((resampled >= 0).mean() if observed < 0 else (resampled <= 0).mean())


def onset_latency(change: np.ndarray, centres: np.ndarray, rng: np.random.Generator, n_boot: int = 10000,
                  p: float = 0.01, run: int = 1) -> tuple[float, float, np.ndarray]:
    """Onset of a population rate change (units x bins), as in Extended Data Fig. 9a.

    The onset is the first bin centre at which the change across units is above 0 (one-sample
    t-test, p < 0.01). With `run` > 1 (a variant here, not the paper's), the first of `run`
    consecutive such bins. Units are resampled with replacement `n_boot` times; returns the mean
    and standard deviation of the resampled onsets (the bootstrap standard error) and the onsets.
    """
    def first(x):
        t, pv = stats.ttest_1samp(x, 0.0, axis=0)
        ok = ((pv < p) & (t > 0)).astype(int)
        if run > 1:
            ok = (np.convolve(ok, np.ones(run, int), mode="full")[run - 1:] == run).astype(int)
        hit = np.flatnonzero(ok)
        return centres[hit[0]] if len(hit) else np.nan
    onsets = np.array([first(change[rng.integers(0, len(change), len(change))]) for _ in range(n_boot)])
    return float(np.nanmean(onsets)), float(np.nanstd(onsets)), onsets
