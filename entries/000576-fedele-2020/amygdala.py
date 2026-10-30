"""Loading and measures for dandiset 000576: iEEG and neurons of the human amygdala during aversive videos.

Fedele, Tzovara et al. (2020), NeuroImage 213, 116705, doi:10.1016/j.neuroimage.2020.116705.

The dandiset holds one session per patient, deposited twice: `*_ecephys.nwb` and `*_ecephys+image.nwb`,
which adds a link to the video and holds the same iEEG, spikes and trials (the notebook checks this).
Only the `_ecephys.nwb` files are read. Each holds the bipolar amygdala iEEG channels (`AL2-AL1`,
`AR2-AR1`) at 2 kHz as 17 epochs of 26 s laid end to end (0 to 442 s), the trial table (17 trials,
alternating NEUTRAL and AVERSIVE, 9 and 8), and for 5 patients a units table of spike times. Within
each 26 s epoch the first 2 s are the repeated neutral baseline clip and 2 to 26 s the 24 s block
(the trial table's start times for trials 2 to 17 are at 2 s into their epoch). Files are streamed at
the pinned version; nothing is written to disk.

Where the parameters come from:

- Bands, filter (IIR Butterworth of order 2), Hilbert amplitude, 1 s smoothing, baseline correction
  with the 1 s before the sequence, z-scoring within each trial: Methods 4.8, as the claims file's
  opening comment gives them. HGP is a high-pass at 60 Hz (reading (a) of the claims file).
- Zero-phase filtering (`sosfiltfilt`) and a boxcar smoothing window: standard choices that the
  claims file names; with 1 s smoothing they cannot change the outcome.
- Each epoch is filtered on its own, with 2 s of mirror padding at each end (a standard choice):
  the epochs are not contiguous in the files (the notebook shows jumps at the epoch boundaries).
- Baseline correction is a subtraction of the mean over the 1 s before block onset (Methods 4.8,
  "baseline corrected using 1 s window before the beginning of each sequence"); subtraction is
  the standard choice. Under z-scoring over the whole trial (reading a) it has no effect.
- Z-scoring readings (claims file): "trial" over the whole 26 s epoch; "baseline" over the 2 s
  baseline clip (Methods 4.8, "The baseline was a 2 s landscape clip"); "amygdala" over all epochs
  and time points of the amygdala.
- Envelopes are kept at 10 Hz (`STEP_S`) after the 1 s smoothing, which removes everything faster;
  a standard choice.
- Group test: Power ~ condition + (1|Patients) per time point (Methods 4.11). With every patient
  holding 8 AVERSIVE and 9 NEUTRAL trials per amygdala, the design is balanced, and the generalised
  least squares estimate of the condition effect equals the within-patient (patient fixed effect)
  estimate; `lmm_t` computes that t statistic for all time points at once. The notebook compares it
  with statsmodels' MixedLM at a few time points. Labels are permuted within each patient, the same
  permutation for both amygdalae of a patient (Methods 4.11, "permuted the labels of neutral and
  aversive trials across all participants"), 500 permutations. Cluster-forming threshold
  two-sided p < 0.05 of the t statistic, cluster statistic the sum of t (FieldTrip's maxsum,
  Oostenveld et al. 2011, which the paper cites) or, as the claims file's reading (b), the number
  of time points. The cluster p is (k + 1) / (n + 1), with k the permutations whose largest
  absolute cluster statistic reaches the observed one.
- Spike trains: 100 ms bins smoothed over 1 s (Fig. 3A legend), 15 s smoothing (Fig. 3D legend),
  or 1.5 s bins smoothed over 5 points (Methods 4.10), as the claims give the readings.
"""

from __future__ import annotations

import json
import urllib.request

import h5py
import numpy as np
import remfile
from scipy import signal, stats
from scipy.ndimage import uniform_filter1d

DANDISET_ID = "000576"
DANDISET_VERSION = "0.231010.1811"
API = "https://api.dandiarchive.org/api"

FS = 2000.0              # Hz, iEEG sampling rate (file comment, Methods 4.7)
EPOCH_S = 26.0           # baseline clip (2 s) + block (24 s)
ONSET_S = 2.0            # block onset within the epoch
STEP_S = 0.1             # envelope sampling after smoothing (standard choice)
SMOOTH_S = 1.0           # Methods 4.8
PAD_S = 2.0              # mirror padding for filtering each epoch (standard choice)
BANDS = {                # Methods 4.8; HGP upper edge open, high-pass reading
    "delta": (1.0, 4.0), "theta": (4.0, 8.0), "alpha": (8.0, 15.0),
    "beta": (15.0, 30.0), "gamma": (30.0, 60.0), "hgp": (60.0, None),
}
N_PERM = 500             # Methods 4.11

# Table 2 numbers the amygdalae 1 to 14 by patient, left before right; SOZ marked with * (claims file).
TABLE2 = [(1, "L"), (1, "R"), (2, "L"), (2, "R"), (3, "L"), (4, "L"), (5, "R"), (6, "L"), (6, "R"),
          (7, "L"), (7, "R"), (8, "L"), (9, "L"), (9, "R")]
TABLE2_SOZ = {2, 4, 7, 9, 11, 13, 14}


def assets(version: str = DANDISET_VERSION) -> list[dict]:
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=200"
    out = []
    while url:
        with urllib.request.urlopen(url) as r:
            page = json.load(r)
        out += page["results"]
        url = page["next"]
    return out


def _s(x):
    return x.decode() if isinstance(x, bytes) else x


def open_asset(asset_id: str) -> h5py.File:
    return h5py.File(remfile.File(f"{API}/assets/{asset_id}/download/"), "r")


def load_session(asset: dict) -> dict:
    """Everything the analysis uses from one `_ecephys.nwb` file, as arrays in memory."""
    h = open_asset(asset["asset_id"])
    e = h["general/extracellular_ephys/electrodes"]
    lfp = h["processing/ecephys/LFP/ecephys.ieeg"]
    tr = h["intervals/trials"]
    s = {
        "path": asset["path"],
        "subject": int(_s(h["general/subject/subject_id"][()])),
        "age": _s(h["general/subject/age"][()]),
        "sex": _s(h["general/subject/sex"][()]),
        "description": _s(h["general/subject/description"][()]),
        "labels": [_s(x) for x in e["label"][:]],
        "locations": [_s(x) for x in e["location"][:]],
        "soz": [bool(x) for x in e["is_inside_soz"][:]],
        "filtering": [_s(x) for x in e["filtering"][:]],
        "lfp": lfp["data"][:],
        "lfp_unit": _s(lfp["data"].attrs["unit"]),
        "t": lfp["timestamps"][:],
        "conditions": [_s(c) for c in tr["condition"][:]],
        "trial_start": tr["start_time"][:],
        "trial_stop": tr["stop_time"][:],
        "trial_ts": [(int(a), int(b)) for a, b, _ in tr["timeseries"][:]],
        "units": [],
    }
    if "units" in h:
        u = h["units"]
        idx = np.r_[0, u["spike_times_index"][:]]
        st = u["spike_times"][:]
        el = u["electrodes"][:]
        oi, oidx = u["obs_intervals"][:], np.r_[0, u["obs_intervals_index"][:]]
        for k in range(len(idx) - 1):
            s["units"].append({"spikes": st[idx[k]:idx[k + 1]], "channel": int(el[k]),
                               "obs": oi[oidx[k]:oidx[k + 1]],
                               "waveform": u["waveform_mean"][k]})
    s["n_epochs"] = len(s["conditions"])
    s["aversive"] = np.array([c.lower().startswith("avers") for c in s["conditions"]])
    return s


def side(label: str) -> str:
    return label[1]           # "AL2-AL1" -> "L"


def table2_number(subject: int, label: str) -> int:
    return TABLE2.index((subject, side(label))) + 1


# --- iEEG power envelopes ---------------------------------------------------------------------

def epochs(lfp_channel: np.ndarray) -> np.ndarray:
    n = int(EPOCH_S * FS)
    return lfp_channel.reshape(-1, n)


def envelope(ep: np.ndarray, band) -> np.ndarray:
    """Hilbert amplitude in a band (a name in BANDS, or (low, high) in Hz with high None for a
    high-pass), smoothed over 1 s, per epoch, sampled at STEP_S (epochs x time)."""
    lo, hi = BANDS[band] if isinstance(band, str) else band
    sos = (signal.butter(2, [lo, hi], btype="bandpass", fs=FS, output="sos") if hi
           else signal.butter(2, lo, btype="highpass", fs=FS, output="sos"))
    pad = int(PAD_S * FS)
    x = np.pad(ep, ((0, 0), (pad, pad)), mode="reflect")
    y = signal.sosfiltfilt(sos, x, axis=1)
    a = np.abs(signal.hilbert(y, axis=1))
    a = uniform_filter1d(a, int(SMOOTH_S * FS), axis=1, mode="nearest")[:, pad:-pad]
    step = int(STEP_S * FS)
    return a[:, step // 2::step]


def times() -> np.ndarray:
    """Time of each envelope sample relative to block onset (s)."""
    return np.arange(int(EPOCH_S / STEP_S)) * STEP_S + STEP_S / 2 - ONSET_S


def normalise(env: np.ndarray, zscore: str) -> np.ndarray:
    """Baseline correction (subtract the mean of the 1 s before onset), then z-scoring by reading."""
    t = times()
    base1 = (t >= -1.0) & (t < 0.0)
    x = env - env[:, base1].mean(axis=1, keepdims=True)
    if zscore == "trial":
        return (x - x.mean(1, keepdims=True)) / x.std(1, keepdims=True)
    if zscore == "baseline":
        b = t < 0.0
        return (x - x[:, b].mean(1, keepdims=True)) / x[:, b].std(1, keepdims=True)
    if zscore == "trialsd":
        return x / x.std(1, keepdims=True)
    if zscore == "amygdala":
        return (x - x.mean()) / x.std()
    raise ValueError(zscore)


# --- group statistics ---------------------------------------------------------------------------

def lmm_t(y: np.ndarray, x: np.ndarray, groups: np.ndarray) -> tuple[np.ndarray, int]:
    """t of the condition effect with patient intercepts, for every column of y (trials x time)."""
    yr = y.astype(float).copy()
    xr = x.astype(float).copy()
    for g in np.unique(groups):
        m = groups == g
        yr[m] -= yr[m].mean(0)
        xr[m] -= xr[m].mean()
    sxx = xr @ xr
    beta = xr @ yr / sxx
    resid = yr - np.outer(xr, beta)
    df = len(x) - len(np.unique(groups)) - 1
    se = np.sqrt((resid ** 2).sum(0) / df / sxx)
    return beta / se, df


def ttest_t(y: np.ndarray, x: np.ndarray, groups=None) -> tuple[np.ndarray, int]:
    """Unpaired t (equal variances) of AVERSIVE against NEUTRAL trials, pooled, per time point."""
    a, b = y[x == 1], y[x == 0]
    t = stats.ttest_ind(a, b, axis=0).statistic
    return t, len(a) + len(b) - 2


def clusters(t: np.ndarray, thr: float) -> list[tuple[int, int, int]]:
    """Runs of |t| > thr with one sign: (start, stop, sign)."""
    out = []
    for sign in (1, -1):
        above = np.r_[False, sign * t > thr, False]
        d = np.diff(above.astype(int))
        for a, b in zip(np.where(d == 1)[0], np.where(d == -1)[0]):
            out.append((a, b, sign))
    return sorted(out)


def cluster_stat(t, cl, stat):
    a, b, _ = cl
    return abs(t[a:b].sum()) if stat == "mass" else b - a


def cluster_test(y, x, groups, rng, model="lmm", stat="mass", perm_groups=None, alpha=0.05,
                 linked=None, n_perm=N_PERM):
    """Cluster-based permutation test over time (columns of y).

    `linked`: an array giving, for each row, a key for rows that share a label sequence (a
    patient's two amygdalae see the same blocks): a permutation is drawn once per patient and
    applied to every amygdala of that patient. Rows are ordered by trial within each amygdala.
    """
    fn = lmm_t if model == "lmm" else ttest_t
    t, df = fn(y, x, groups)
    thr = stats.t.ppf(1 - alpha / 2, df)
    obs = clusters(t, thr)
    obs_stat = [cluster_stat(t, c, stat) for c in obs]
    pg = groups if perm_groups is None else perm_groups
    null = np.zeros(n_perm)
    keys = linked if linked is not None else np.arange(len(x))
    # one permutation per patient: permute trial positions of the patient's first amygdala and
    # copy to its others
    for p in range(n_perm):
        xp = x.copy()
        for g in np.unique(pg):
            rows = np.where(pg == g)[0]
            if linked is None:
                xp[rows] = rng.permutation(x[rows])
                continue
            sub_keys = keys[rows]
            first = rows[sub_keys == sub_keys[0]]
            order = rng.permutation(len(first))
            for k in np.unique(sub_keys):
                r = rows[sub_keys == k]
                xp[r] = x[r][order]
        tp, _ = fn(y, xp, groups)
        cs = [cluster_stat(tp, c, stat) for c in clusters(tp, thr)]
        null[p] = max(cs) if cs else 0.0
    res = []
    for c, s in zip(obs, obs_stat):
        res.append({"start": c[0], "stop": c[1], "sign": c[2], "stat": s,
                    "p": (np.sum(null >= s) + 1) / (n_perm + 1)})
    return t, df, res


# --- spikes -------------------------------------------------------------------------------------

def observed_epochs(spikes: np.ndarray, n_epochs: int) -> np.ndarray:
    """Epochs in which the unit fired at least once. The units' obs_intervals cover all 17 epochs,
    but some units have no spike at all in whole epochs at rates of 1 to 16 Hz elsewhere (shown in
    the notebook); those epochs are taken as not recorded. A choice made here, stated as one."""
    counts = np.histogram(spikes, np.arange(n_epochs + 1) * EPOCH_S)[0]
    return counts > 0


def binned_rate(spikes: np.ndarray, n_epochs: int, bin_s: float = 0.1) -> np.ndarray:
    """Firing rate (Hz) in bins over the concatenated session (n_epochs x bins per epoch)."""
    nb = int(round(EPOCH_S / bin_s))
    edges = np.arange(n_epochs * nb + 1) * bin_s
    c = np.histogram(spikes, edges)[0] / bin_s
    return c.reshape(n_epochs, nb)


def smooth_session(x: np.ndarray, width_bins: int) -> np.ndarray:
    """Boxcar smoothing over the concatenated session (epochs x bins), returned in the same shape."""
    flat = uniform_filter1d(x.reshape(-1).astype(float), max(int(width_bins), 1), mode="nearest")
    return flat.reshape(x.shape)


def smooth_epochs(x: np.ndarray, width_bins: int) -> np.ndarray:
    return uniform_filter1d(x.astype(float), max(int(width_bins), 1), axis=1, mode="nearest")


def spearman(a, b) -> float:
    a, b = np.asarray(a, float), np.asarray(b, float)
    if np.std(a) == 0 or np.std(b) == 0 or len(a) < 3:
        return np.nan
    return stats.spearmanr(a, b).statistic


def clopper_pearson(k: int, n: int, level: float = 0.95) -> tuple[float, float]:
    a = 1 - level
    lo = stats.beta.ppf(a / 2, k, n - k + 1) if k > 0 else 0.0
    hi = stats.beta.ppf(1 - a / 2, k + 1, n - k) if k < n else 1.0
    return lo, hi


# --- per-unit measures ----------------------------------------------------------------------------

def units(sessions: list[dict]) -> list[dict]:
    """One record per unit: its amygdala (Table 2 number), observed epochs and 100 ms binned rate."""
    out = []
    for s in sessions:
        for k, u in enumerate(s["units"]):
            label = s["labels"][u["channel"]]
            obs = observed_epochs(u["spikes"], s["n_epochs"])
            out.append({"subject": s["subject"], "unit": k, "label": label,
                        "amygdala": table2_number(s["subject"], label), "spikes": u["spikes"],
                        "obs": obs, "aversive": s["aversive"],
                        "rate100": binned_rate(u["spikes"], s["n_epochs"], 0.1)})
    return out


def frv(u: dict, window: str = "block", only_observed: bool = True) -> float:
    """Firing Rate Variability: AVERSIVE minus NEUTRAL mean rate (Hz) (Methods 4.11), over the 24 s
    blocks ("block") or the 26 s trials ("trial")."""
    r = u["rate100"]
    t = np.arange(r.shape[1]) * 0.1 + 0.05 - ONSET_S
    cols = t >= 0 if window == "block" else np.ones(r.shape[1], bool)
    o = u["obs"] if only_observed else np.ones(len(u["obs"]), bool)
    av = u["aversive"]
    return r[o & av][:, cols].mean() - r[o & ~av][:, cols].mean()


def series(x100: np.ndarray, obs: np.ndarray, base: str) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """A 100 ms series (epochs x 260 bins) on one of the time bases of the claims file, over the
    observed epochs laid end to end. Returns the series, the epoch of each sample and its time from
    block onset. Bases: "1s" (100 ms bins smoothed over 1 s, Fig. 3A legend), "15s" (100 ms bins
    smoothed over 15 s, Fig. 3D legend), "1.5s" (1.5 s bins smoothed over 5 points, Methods 4.10)."""
    ep = np.where(obs)[0]
    x = x100[ep]
    nb = x.shape[1]
    ep_of = np.repeat(ep, nb)
    t_of = np.tile(np.arange(nb) * 0.1 + 0.05 - ONSET_S, len(ep))
    flat = x.reshape(-1).astype(float)
    if base == "1s":
        return uniform_filter1d(flat, 10, mode="nearest"), ep_of, t_of
    if base == "15s":
        return uniform_filter1d(flat, 150, mode="nearest"), ep_of, t_of
    if base == "1.5s":
        n = len(flat) // 15
        y = flat[:n * 15].reshape(n, 15).mean(1)
        mid = np.arange(n) * 15 + 7
        return uniform_filter1d(y, 5, mode="nearest"), ep_of[mid], t_of[mid]
    raise ValueError(base)


def block_series(x100: np.ndarray, epoch: int, base: str) -> np.ndarray:
    """A 100 ms series within one 24 s block on a time base (used for per-block correlations)."""
    t = np.arange(x100.shape[1]) * 0.1 + 0.05 - ONSET_S
    x = x100[epoch, t >= 0].astype(float)
    if base == "1s":
        return uniform_filter1d(x, 10, mode="nearest")
    if base == "15s":
        return uniform_filter1d(x, 150, mode="nearest")
    if base == "1.5s":
        return uniform_filter1d(x.reshape(16, 15).mean(1), 5, mode="nearest")
    raise ValueError(base)


def condition_corr(a100, b100, obs, aversive, base, span):
    """Spearman r of two 100 ms series (epochs x bins) within one condition's blocks: "concat" over
    the blocks laid end to end (smoothing over the observed session), or "block" per block and
    averaged. Returns (r in AVERSIVE, r in NEUTRAL)."""
    out = []
    for cond in (True, False):
        if span == "concat":
            xa, ep_of, t_of = series(a100, obs, base)
            xb, _, _ = series(b100, obs, base)
            m = (aversive[ep_of] == cond) & (t_of >= 0)
            out.append(spearman(xa[m], xb[m]))
        else:
            rs = [spearman(block_series(a100, e, base), block_series(b100, e, base))
                  for e in np.where(obs & (aversive == cond))[0]]
            out.append(np.nanmean(rs))
    return tuple(out)
