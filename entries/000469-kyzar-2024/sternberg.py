"""Loading and measures for dandiset 000469 (human single neurons, screening and Sternberg tasks).

Kyzar, Kaminski, Brzezicka, Reed, Chung, Mamelak & Rutishauser (2024), Sci Data 11, 89,
doi:10.1038/s41597-024-02943-8. Its code is github.com/rutishauserlab/workingmem-release-NWB at
commit f8594e0 (MATLAB, read, not run); "the code" below means that commit.

Each subject has a screening file (ses-1) and a Sternberg file (ses-2). Only the small arrays
are read (spike times, unit and electrode tables, trials, stimulus presentation, TTL events);
the spike waveforms, which make most of each file, are not. Files are streamed from the archive
at the pinned version; nothing is written to disk.

Where the parameters come from:

- Areas: the electrode `location`, left and right merged, as translateArea_SB.m (condenseFlag 1)
  and NWB_countAreas.m do (claims sternberg-unit-yield). MTL is amygdala and hippocampus, MFC is
  dACC, pre-SMA and vmPFC, as the code's summary in NWB_SB_import_main.m groups them.
- Quality metrics (claims isi-violations to isolation-distance): as NWB_QA_graphs.m computes
  them. ISI violations, consecutive spike time differences below 3 ms over the whole file; rate,
  spikes over the time from first to last spike; CV2 by calcCV2.m with ignoreMode 1 (pairs with
  an ISI over 1 s left out).
- Windows (claims and Methods, "Cell selection"): image response 200 to 1000 ms after onset;
  maintenance 0 to 2500 ms after maintenance onset; baseline 0 to 500 ms after fixation onset
  (length from the Methods, start from the code); probe 200 to 1000 ms after probe onset. Spikes
  are counted strictly inside the window, as the code's `>` and `<` do.
- Screening trial onsets are the trials table `start_time`, and the image of each trial is
  StimulusPresentation, as in NWB_calcSelective_SC.m.
- Permutation tests: 2000 permutations, the number in the code's commented permutation
  alternative (a resolution detail). The p-value is (exceedances + 1) / (permutations + 1), as
  the code's permutationTest.m computes it. The permuted ANOVA permutes the image labels across
  trials and compares the F statistic. The permutation t-test permutes the labels of the two
  groups and compares the difference of means, as permutationTest.m does.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient

DANDISET_ID = "000469"
DANDISET_VERSION = "0.240123.1806"

N_PERM = 2000
ALPHA = 0.05

AREA = {
    "hippocampus": "Hipp", "amygdala": "Amg",
    "dorsal_anterior_cingulate_cortex": "dACC",
    "pre_supplementary_motor_area": "pre-SMA",
    "ventral_medial_prefrontal_cortex": "vmPFC",
}
MTL = ("Hipp", "Amg")
MFC = ("dACC", "pre-SMA", "vmPFC")

ENC_WIN = (0.2, 1.0)      # image and probe response window, s after onset
MAINT_WIN = (0.0, 2.5)    # maintenance window, s after maintenance onset
FIX_WIN = (0.0, 0.5)      # baseline window, s after fixation onset

TRIAL_COLUMNS = [
    "loads", "loadsEnc1_PicIDs", "loadsEnc2_PicIDs", "loadsEnc3_PicIDs", "loadsProbe_PicIDs",
    "probe_in_out", "response_accuracy", "start_time", "stop_time", "timestamps_FixationCross",
    "timestamps_Encoding1", "timestamps_Encoding1_end", "timestamps_Encoding2",
    "timestamps_Encoding2_end", "timestamps_Encoding3", "timestamps_Encoding3_end",
    "timestamps_Maintenance", "timestamps_Probe", "timestamps_Response",
]


def asset_urls() -> list[tuple[str, str]]:
    """(path, streaming URL) of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in dandiset.get_assets() if a.path.endswith(".nwb"))


def _text(value) -> str:
    return value.decode() if isinstance(value, bytes) else str(value)


def condense_area(location: str) -> str:
    """Area of an electrode location label, left and right merged (translateArea_SB.m)."""
    for prefix, name in AREA.items():
        if location.startswith(prefix):
            return name
    return "NA"


def load_file(path: str, url: str) -> dict:
    """Read the parts of one NWB file the analysis uses."""
    with h5py.File(remfile.File(url), "r") as f:
        u = f["units"]
        spikes = u["spike_times"][:]
        ends = u["spike_times_index"][:].astype(int)
        starts = np.concatenate([[0], ends[:-1]])
        e = f["general/extracellular_ephys/electrodes"]
        locations = [_text(x) for x in e["location"][:]]
        electrode = u["electrodes"][:].astype(int)
        units = pd.DataFrame({
            "unit_id": u["id"][:].astype(int),
            "electrode": electrode,
            "location": [locations[i] for i in electrode],
            "cluster": u["clusterID_orig"][:],
            "isolation_distance": u["waveforms_isolation_distance"][:],
            "proj_dist": u["waveforms_mean_proj_dist"][:],
            "mean_snr": u["waveforms_mean_snr"][:],
            "peak_snr": u["waveforms_peak_snr"][:],
        })
        units["area"] = units["location"].map(condense_area)
        units["spike_times"] = [spikes[a:b] for a, b in zip(starts, ends)]
        electrodes = pd.DataFrame({
            "id": e["id"][:], "location": locations, "x": e["x"][:], "y": e["y"][:],
            "z": e["z"][:], "origChannel": e["origChannel"][:],
            "group_name": [_text(x) for x in e["group_name"][:]],
        })
        tr = f["intervals/trials"]
        trials = pd.DataFrame({c: tr[c][:] for c in TRIAL_COLUMNS if c in tr})
        sp = f["stimulus/presentation/StimulusPresentation"]
        out = {
            "path": path,
            "subject": int(_text(f["general/subject/subject_id"][()])),
            "session": int(_text(f["general/session_id"][()])),
            "identifier": _text(f["identifier"][()]),
            "age": _text(f["general/subject/age"][()]),
            "sex": _text(f["general/subject/sex"][()]),
            "session_start_time": _text(f["session_start_time"][()]),
            "units": units,
            "electrodes": electrodes,
            "trials": trials,
            "stim_ids": sp["data"][:].astype(int),
            "stim_times": sp["timestamps"][:],
            "templates": sorted(f["stimulus/templates/StimulusTemplates"].keys()),
            "events": f["acquisition/events/data"][:].astype(int),
            "event_times": f["acquisition/events/timestamps"][:],
        }
    return out


def load_all(workers: int = 8) -> list[dict]:
    """Every file of the pinned version, in path order."""
    urls = asset_urls()
    with ThreadPoolExecutor(workers) as pool:
        return list(pool.map(lambda pu: load_file(*pu), urls))


# ---------------------------------------------------------------- quality metrics (NWB_QA_graphs.m)

def isi_violation_pct(ts: np.ndarray, limit_ms: float = 3.0) -> float:
    isi = np.diff(ts) * 1e3
    return 100.0 * np.sum(isi < limit_ms) / len(isi)


def mean_rate(ts: np.ndarray) -> float:
    return len(ts) / (ts.max() - ts.min())


def cv2(ts: np.ndarray, upper: float = 1.0) -> float:
    """calcCV2.m with ignoreMode 1: mean of 2|dISI|/sum over pairs with both ISIs <= 1 s."""
    isi = np.diff(ts)
    a, b = isi[:-1], isi[1:]
    values = 2 * np.abs(b - a) / (a + b)
    valid = (a <= upper) & (b <= upper)
    return float(np.mean(values[valid]))


# ---------------------------------------------------------------- window rates

def window_rates(ts: np.ndarray, onsets: np.ndarray, window: tuple[float, float]) -> np.ndarray:
    """Rate (Hz) in (onset + window[0], onset + window[1]), strict bounds as the code counts."""
    lo = np.searchsorted(ts, onsets + window[0], side="right")
    hi = np.searchsorted(ts, onsets + window[1], side="left")
    return (hi - lo) / (window[1] - window[0])


def encoding_rate_pooled(ts: np.ndarray, trials: pd.DataFrame, enc3_from_enc2: bool = False):
    """Rate pooled over the 200-1000 ms windows of every encoding period shown in a trial.

    With enc3_from_enc2, the third window is taken at Encoding 2 onset, as the code's
    NWB_calcSelective_SB.m does (a defect noted in the claims file).
    """
    counts = np.zeros(len(trials))
    n = np.zeros(len(trials))
    width = ENC_WIN[1] - ENC_WIN[0]
    for k in (1, 2, 3):
        on = trials[f"timestamps_Encoding{k}"].to_numpy()
        shown = on > 0
        src = trials["timestamps_Encoding2"].to_numpy() if (k == 3 and enc3_from_enc2) else on
        counts[shown] += window_rates(ts, src[shown], ENC_WIN) * width
        n[shown] += 1
    return counts / (n * width)


# ---------------------------------------------------------------- permutation tests

def perm_matrix(n: int, rng: np.random.Generator, n_perm: int = N_PERM) -> np.ndarray:
    """n_perm random permutations of range(n), one per row."""
    return np.argsort(rng.random((n_perm, n)), axis=1)


def _f_stat(groups_sum: np.ndarray, counts: np.ndarray, total: float, ss_total: float,
            n: int) -> np.ndarray:
    k = len(counts)
    ss_between = np.sum(groups_sum ** 2 / counts, axis=-1) - total ** 2 / n
    ss_within = ss_total - ss_between
    with np.errstate(divide="ignore", invalid="ignore"):
        return (ss_between / (k - 1)) / (ss_within / (n - k))


def anova_f(y: np.ndarray, labels: np.ndarray) -> float:
    groups, inv = np.unique(labels, return_inverse=True)
    sums = np.bincount(inv, weights=y)
    counts = np.bincount(inv)
    return float(_f_stat(sums, counts, y.sum(), np.sum((y - y.mean()) ** 2), len(y)))


def perm_anova(y: np.ndarray, labels: np.ndarray, perms: np.ndarray) -> tuple[float, float]:
    """Permuted one-way ANOVA: (F, p) with p from permuting the labels across trials."""
    groups, inv = np.unique(labels, return_inverse=True)
    onehot = np.eye(len(groups))[inv]                      # n x G
    counts = onehot.sum(0)
    n = len(y)
    total, ss_total = y.sum(), np.sum((y - y.mean()) ** 2)
    f_obs = _f_stat(y @ onehot, counts, total, ss_total, n)
    if ss_total == 0:
        return float("nan"), 1.0
    f_perm = _f_stat(y[perms] @ onehot, counts, total, ss_total, n)
    p = (np.sum(f_perm > f_obs) + 1) / (len(perms) + 1)
    return float(f_obs), float(p)


def perm_ttest(a: np.ndarray, b: np.ndarray, perms: np.ndarray | None,
               rng: np.random.Generator | None = None,
               n_perm: int = N_PERM) -> tuple[float, float, float]:
    """Two-sample permutation test of mean(a) - mean(b), as permutationTest.m.

    Returns (difference, p two-sided, p one-sided larger). `perms` permutes len(a)+len(b) items;
    when it is None, it is drawn from rng.
    """
    allv = np.concatenate([a, b])
    if perms is None:
        perms = perm_matrix(len(allv), rng, n_perm)
    na = len(a)
    obs = a.mean() - b.mean()
    shuffled = allv[perms]
    diff = shuffled[:, :na].mean(1) - shuffled[:, na:].mean(1)
    n = len(perms)
    p_two = (np.sum(np.abs(diff) > abs(obs)) + 1) / (n + 1)
    p_larger = (np.sum(diff > obs) + 1) / (n + 1)
    return float(obs), float(p_two), float(p_larger)


def signflip_test(d: np.ndarray, rng: np.random.Generator, n_perm: int = N_PERM) -> float:
    """Paired permutation test, one-sided (mean of d larger than 0), by flipping signs."""
    obs = d.mean()
    signs = rng.choice([-1.0, 1.0], size=(n_perm, len(d)))
    null = (signs * d).mean(1)
    return float((np.sum(null > obs) + 1) / (n_perm + 1))


def concept_test(rates: np.ndarray, labels: np.ndarray, perms: np.ndarray,
                 rng: np.random.Generator, n_perm: int = N_PERM) -> dict:
    """Concept cell test of the Methods ("Cell selection: concept cells").

    Permuted one-way ANOVA on image identity, then a permutation t-test of the trials of the
    image with the highest mean rate against all other trials. The preferred image is the
    first image with the highest mean, as the code's find(mResp==max(mResp),1) takes it.
    """
    groups = np.unique(labels)
    means = np.array([rates[labels == g].mean() for g in groups])
    pref = groups[int(np.argmax(means))]
    f, p_anova = perm_anova(rates, labels, perms)
    is_pref = labels == pref
    diff, p_two, p_one = perm_ttest(rates[is_pref], rates[~is_pref], None, rng, n_perm)
    return {"pref": int(pref), "F": f, "p_anova": p_anova, "diff": diff,
            "p_t_two": p_two, "p_t_one": p_one,
            "concept_two": bool(p_anova < ALPHA and p_two < ALPHA),
            "concept_one": bool(p_anova < ALPHA and p_one < ALPHA and diff > 0)}


def parametric_concept(rates: np.ndarray, labels: np.ndarray) -> bool:
    """The code's version: anovan on the image, then anovan on preferred against the rest."""
    from scipy import stats
    groups = np.unique(labels)
    samples = [rates[labels == g] for g in groups]
    p1 = stats.f_oneway(*samples).pvalue
    if not p1 < ALPHA:
        return False
    means = np.array([s.mean() for s in samples])
    pref = groups[int(np.argmax(means))]
    p2 = stats.f_oneway(rates[labels == pref], rates[labels != pref]).pvalue
    return bool(p2 < ALPHA)


# ---------------------------------------------------------------- per-unit tests over sessions

def units_table(sessions: list[dict]) -> pd.DataFrame:
    """All units of the given files, with the subject, unit id and area."""
    return pd.concat([s["units"].assign(subject=s["subject"]) for s in sessions], ignore_index=True)


def screening_concept(sessions: list[dict], rng: np.random.Generator) -> pd.DataFrame:
    """Concept cell test of every screening unit (claims screening-concept-mtl and -mfc).

    Rates 200 to 1000 ms after each trial's start_time, grouped by the StimulusPresentation
    image, all presentations (NWB_calcSelective_SC.m). The code's parametric version is the
    column `parametric`.
    """
    rows = []
    for s in sessions:
        onsets, labels = s["trials"]["start_time"].to_numpy(), s["stim_ids"]
        perms = perm_matrix(len(onsets), rng)
        for _, u in s["units"].iterrows():
            r = window_rates(np.sort(u.spike_times), onsets, ENC_WIN)
            res = concept_test(r, labels, perms, rng)
            res.update(subject=s["subject"], unit_id=u.unit_id, area=u.area,
                       parametric=parametric_concept(r, labels))
            rows.append(res)
    return pd.DataFrame(rows)


def screening_concept_refined(sessions: list[dict], first: pd.DataFrame, rng: np.random.Generator,
                              n_perm: int = 20000, band: tuple[float, float] = (0.02, 0.10)) -> pd.DataFrame:
    """The screening concept test again, with n_perm permutations, for the units whose p-value
    from the first run (`first`) lies in `band` for either test, where the Monte Carlo error of
    2000 permutations (about 0.005 at p = 0.05) can move a unit across 0.05. Other units keep
    their first result. This only reduces the resolution error of the same test."""
    out = first.copy().set_index(["subject", "unit_id"])
    near = ((first[["p_anova", "p_t_two", "p_t_one"]] >= band[0]) & (first[["p_anova", "p_t_two", "p_t_one"]] <= band[1])).any(axis=1)
    todo = set(zip(first.subject[near], first.unit_id[near]))
    for s in sessions:
        onsets, labels = s["trials"]["start_time"].to_numpy(), s["stim_ids"]
        units = [u for _, u in s["units"].iterrows() if (s["subject"], u.unit_id) in todo]
        if not units:
            continue
        perms = perm_matrix(len(onsets), rng, n_perm)
        for u in units:
            r = window_rates(np.sort(u.spike_times), onsets, ENC_WIN)
            res = concept_test(r, labels, perms, rng, n_perm)
            for k, v in res.items():
                out.loc[(s["subject"], u.unit_id), k] = v
    out["refined"] = False
    out.loc[list(todo), "refined"] = True
    return out.reset_index()


def sternberg_rates(s: dict, ts: np.ndarray) -> dict:
    """Per-trial rates of one unit in the windows of the Methods."""
    t = s["trials"]
    ts = np.sort(ts)
    return {
        "enc1": window_rates(ts, t["timestamps_Encoding1"].to_numpy(), ENC_WIN),
        "maint": window_rates(ts, t["timestamps_Maintenance"].to_numpy(), MAINT_WIN),
        "fix": window_rates(ts, t["timestamps_FixationCross"].to_numpy(), FIX_WIN),
        "probe": window_rates(ts, t["timestamps_Probe"].to_numpy(), ENC_WIN),
        "enc_pooled": encoding_rate_pooled(ts, t),
        "enc_code": encoding_rate_pooled(ts, t, enc3_from_enc2=True),
    }


def pref_masks(t: pd.DataFrame, pref: int) -> dict:
    """Trials with the preferred image: as Encoding 1 (`enc1`) or in any encoding period (`any`)."""
    enc1 = (t["loadsEnc1_PicIDs"] == pref).to_numpy()
    shown = ((t["loadsEnc1_PicIDs"] == pref) | (t["loadsEnc2_PicIDs"] == pref)
             | (t["loadsEnc3_PicIDs"] == pref)).to_numpy()
    return {"enc1": enc1, "any": shown}


def sternberg_concept(sessions: list[dict], rng: np.random.Generator) -> pd.DataFrame:
    """Concept cell test of every Sternberg unit on the Encoding 1 image (claim sternberg-concept-mtl),
    with the mean maintenance and Encoding 1 rates on preferred and non-preferred trials under both
    readings of preferred trials (claim persistent-activity)."""
    rows = []
    for s in sessions:
        t = s["trials"]
        labels = t["loadsEnc1_PicIDs"].to_numpy()
        perms = perm_matrix(len(t), rng)
        for _, u in s["units"].iterrows():
            r = sternberg_rates(s, u.spike_times)
            res = concept_test(r["enc1"], labels, perms, rng)
            res.update(subject=s["subject"], unit_id=u.unit_id, area=u.area,
                       parametric=parametric_concept(r["enc1"], labels))
            for name, mask in pref_masks(t, res["pref"]).items():
                res[f"maint_pref_{name}"] = r["maint"][mask].mean()
                res[f"maint_nonpref_{name}"] = r["maint"][~mask].mean()
                res[f"enc1_pref_{name}"] = r["enc1"][mask].mean()
                res[f"enc1_nonpref_{name}"] = r["enc1"][~mask].mean()
            rows.append(res)
    return pd.DataFrame(rows)


def sternberg_maintenance(sessions: list[dict], concept: pd.DataFrame,
                          rng: np.random.Generator) -> pd.DataFrame:
    """Maintenance tests of every Sternberg unit (claim maintenance-cells-mfc).

    One-sided tests that the maintenance rate exceeds the baseline, by (a) label shuffling
    (permutationTest.m, 'larger') and (b) sign flipping of per-trial differences, and the code's
    paired one-sided t-test (`t`). The extra test for concept cells is on non-preferred trials,
    read as (i) Encoding 1 image not preferred (`enc1`) and (ii) preferred image not shown in any
    encoding period (`any`). `concept` gives each unit's preferred image.
    """
    from scipy import stats
    rows = []
    pref = concept.set_index(["subject", "unit_id"])["pref"]
    for s in sessions:
        t = s["trials"]
        for _, u in s["units"].iterrows():
            r = sternberg_rates(s, u.spike_times)
            m, f = r["maint"], r["fix"]
            res = {"subject": s["subject"], "unit_id": u.unit_id, "area": u.area,
                   "maint_mean": m.mean(), "fix_mean": f.mean(),
                   "p_shuffle": perm_ttest(m, f, None, rng)[2],
                   "p_flip": signflip_test(m - f, rng),
                   "p_t": stats.ttest_rel(m, f, alternative="greater").pvalue}
            for name, mask in pref_masks(t, pref[(s["subject"], u.unit_id)]).items():
                non = ~mask
                res[f"p2_shuffle_{name}"] = perm_ttest(m[non], f[non], None, rng)[2]
                res[f"p2_flip_{name}"] = signflip_test(m[non] - f[non], rng)
                res[f"p2_t_{name}"] = stats.ttest_rel(m[non], f[non], alternative="greater").pvalue
            rows.append(res)
    return pd.DataFrame(rows)


def sternberg_probe(sessions: list[dict], rng: np.random.Generator,
                    areas: tuple[str, ...] | None = None) -> pd.DataFrame:
    """Probe tests of every Sternberg unit (claim probe-cells-mfc).

    The probe rate against the encoding rate and against the maintenance rate, each one-sided.
    Encoding rate (i) pooled over the encoding periods shown (`pooled`) or (ii) Encoding 1 only
    (`enc1`); permutation (a) label shuffling or (b) sign flipping. A unit's p is the larger of
    its two tests. `p_code` is the code's paired t-tests with its Encoding 3 window.
    """
    from scipy import stats
    rows = []
    for s in sessions:
        for _, u in s["units"].iterrows():
            if areas is not None and u.area not in areas:
                continue
            r = sternberg_rates(s, u.spike_times)
            p, m = r["probe"], r["maint"]
            res = {"subject": s["subject"], "unit_id": u.unit_id, "area": u.area,
                   "probe_mean": p.mean(), "maint_mean": m.mean()}
            for name, e in (("pooled", r["enc_pooled"]), ("enc1", r["enc1"])):
                res[f"p_shuffle_{name}"] = max(perm_ttest(p, e, None, rng)[2],
                                               perm_ttest(p, m, None, rng)[2])
                res[f"p_flip_{name}"] = max(signflip_test(p - e, rng), signflip_test(p - m, rng))
            res["p_code"] = max(stats.ttest_rel(p, r["enc_code"], alternative="greater").pvalue,
                                stats.ttest_rel(p, m, alternative="greater").pvalue)
            rows.append(res)
    return pd.DataFrame(rows)


# ---------------------------------------------------------------- checks of the data

def ttl_mismatch(s: dict) -> dict:
    """For each trial-table timestamp column, how many trials have no TTL of the expected code
    within 1 ms (Tables 2 and 3 of the paper give the codes)."""
    ev, times = s["events"], s["event_times"]
    if s["session"] == 1:
        cols = {"start_time": 1}
    else:
        cols = {"timestamps_FixationCross": 11, "timestamps_Encoding1": 1,
                "timestamps_Maintenance": 6, "timestamps_Probe": 7, "timestamps_Response": 8}
    out = {}
    for col, code in cols.items():
        ref = np.sort(times[ev == code])
        v = s["trials"][col].to_numpy()
        i = np.clip(np.searchsorted(ref, v), 1, len(ref) - 1)
        gap = np.minimum(np.abs(ref[i] - v), np.abs(ref[i - 1] - v))
        out[col] = int(np.sum(gap > 1e-3))
    return out


def selectivity_by_shift(s: dict, shifts: tuple[float, ...]) -> dict:
    """Fraction of a file's units whose rate 200-1000 ms after image onset differs by image
    (one-way ANOVA, p < 0.05), with the onsets shifted by each value (s). With the right clock
    the fraction peaks at shift 0 and falls to about 0.05 away from it."""
    from scipy import stats
    if s["session"] == 1:
        onsets, labels = s["trials"]["start_time"].to_numpy(), s["stim_ids"]
    else:
        onsets = s["trials"]["timestamps_Encoding1"].to_numpy()
        labels = s["trials"]["loadsEnc1_PicIDs"].to_numpy()
    groups = np.unique(labels)
    out = {}
    for shift in shifts:
        n_sig = 0
        for ts in s["units"]["spike_times"]:
            r = window_rates(np.sort(ts), onsets + shift, ENC_WIN)
            if r.std() > 0 and stats.f_oneway(*[r[labels == g] for g in groups]).pvalue < ALPHA:
                n_sig += 1
        out[shift] = n_sig / len(s["units"])
    return out


# ---------------------------------------------------------------- behaviour (NWB_QA_graphs.m)

def rt_medians(sessions: list[dict], correct_only: bool = True) -> np.ndarray:
    """Median reaction time (timestamps_Response - timestamps_Probe) per session (rows) and load
    1 to 3 (columns); correct trials only by default, as the code's filter_correct = 1."""
    out = []
    for s in sessions:
        t = s["trials"]
        if correct_only:
            t = t[t["response_accuracy"] == 1]
        rt = t["timestamps_Response"] - t["timestamps_Probe"]
        out.append([np.median(rt[t["loads"] == load]) for load in (1, 2, 3)])
    return np.array(out)


def rm_anova_load(m: np.ndarray) -> tuple[float, int, int, float]:
    """F, df1, df2 and p of the load effect in an additive session (random) by load (fixed) ANOVA
    on a sessions x loads matrix, the model of the code's anovan call."""
    from scipy import stats
    n, k = m.shape
    grand = m.mean()
    ss_load = n * np.sum((m.mean(0) - grand) ** 2)
    ss_sess = k * np.sum((m.mean(1) - grand) ** 2)
    ss_err = np.sum((m - grand) ** 2) - ss_load - ss_sess
    df1, df2 = k - 1, (k - 1) * (n - 1)
    f = (ss_load / df1) / (ss_err / df2)
    return float(f), df1, df2, float(stats.f.sf(f, df1, df2))
