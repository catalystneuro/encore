"""Loading and measures for CRCNS data set pfc-1 (Rodgers & DeWeese 2014, Neuron 82, 1157-1170).

The data set is one zip file, crcns_pfc-1_data.zip, in the public S3 bucket crcnsarchive. It is
streamed over range requests with fsspec and opened in place with zipfile; nothing is written to
disk. CRCNS data sets are unversioned, so the file is pinned by its MD5 sum in the data set's
checksums.md5 (`ZIP_MD5`), which `check_checksums` compares with the bucket's copy.

The spike files (`*.kkp`) are pickles of pandas DataFrames written by pandas 0.10 under Python 2,
which current pandas cannot read. `load_old_pickle` reads them with an unpickler that maps the old
pandas classes to stubs and rebuilds the columns from the pickled block arrays.

The unit table (which clusters are well-sorted single units, their region and their auditory
response class and window) and the session table come from the paper's code repository,
github.com/cxrodgers/Rodgers2014 at commit `CODE_COMMIT` (metadata/unit_db.csv,
metadata/sessions_df.csv), as the claims file says (its M1 and fig2a criterion). The code's
README says only units listed there with include True were analysed.

Where the parameters come from:

- Hold windows (`HOLD_MS`): 50 ms for CR12B, CR17B and YT6A, 250 ms for CR20B, CR21A and CR24A,
  ending at stimulus onset; claims file M3 (Figure 3C legend; 3-1-hold/main0.py).
- Trials for the hold analysis: hits of blocks 2 and 4, nonrandom 0, munged trials dropped, and
  holds of 50 ms or less dropped (claims file M2; 3-1-hold/main0.py keeps holds > 0.050 s).
- Spike counting windows include the start and exclude the end (kkpandas.utility.timelock uses
  np.searchsorted with side left on both ends).
- Tests: R's wilcox.test with exact=FALSE and its default continuity correction (my.stats.r_utest
  in the code) is scipy's mannwhitneyu with method asymptotic and use_continuity True; the paired
  form is scipy's wilcoxon with zero_method wilcox, correction True, method approx (claims M5).
  Benjamini-Hochberg is statsmodels' fdr_bh, which equals R's p.adjust BH.
"""

from __future__ import annotations

import io
import pickle
import zipfile
from concurrent.futures import ThreadPoolExecutor

import fsspec
import numpy as np
import pandas as pd
import requests
from scipy import stats
from statsmodels.stats.multitest import multipletests

BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-1"
DATASET_ID = "pfc-1"
DATASET_VERSION = "unversioned"
DATASET_DOI = "10.6080/K0W66HPJ"
ZIP_NAME = "crcns_pfc-1_data.zip"
ZIP_MD5 = "a8bc7ed90568c298ec4d134d53354a67"   # from pfc-1/checksums.md5
ROOT = "crcns_pfc-1_data/"

CODE_REPO = "cxrodgers/Rodgers2014"
CODE_COMMIT = "390b6089c429877dfea9c56de153bbea0380c20f"
CODE_RAW = f"https://raw.githubusercontent.com/{CODE_REPO}/{CODE_COMMIT}/"

HOLD_MS = {"CR12B": 50, "CR17B": 50, "YT6A": 50, "CR20B": 250, "CR21A": 250, "CR24A": 250}
RAT_NUMBER = {"CR12B": 1, "CR17B": 2, "YT6A": 3, "CR20B": 4, "CR21A": 5, "CR24A": 6}
MIN_HOLD_S = 0.050


# ---------------------------------------------------------------- archive access

_zip = None


def open_zip() -> zipfile.ZipFile:
    """The data set's zip, opened in place over HTTP range requests (cached)."""
    global _zip
    if _zip is None:
        _zip = zipfile.ZipFile(fsspec.open(f"{BUCKET}/{ZIP_NAME}", block_size=2**20).open())
    return _zip


def read_member(name: str) -> bytes:
    """Read one member of the zip. Each call opens its own handle so threads can share."""
    with fsspec.open(f"{BUCKET}/{ZIP_NAME}", block_size=2**20) as f:
        with zipfile.ZipFile(f) as z:
            return z.read(name)


def check_checksums() -> dict:
    """The bucket's checksums.md5, and whether it still lists the pinned MD5 of the zip."""
    text = requests.get(f"{BUCKET}/checksums.md5", timeout=60).text
    sums = {line.split()[1]: line.split()[0] for line in text.splitlines() if line.strip()}
    return {"sums": sums, "zip_matches_pin": sums.get(ZIP_NAME) == ZIP_MD5}


def list_files() -> pd.DataFrame:
    """Every file member of the zip (the macOS resource forks under __MACOSX/ left out)."""
    rows = [{"name": i.filename, "size": i.file_size, "compressed": i.compress_size}
            for i in open_zip().infolist()
            if not i.is_dir() and not i.filename.startswith("__MACOSX")]
    return pd.DataFrame(rows)


# ---------------------------------------------------------------- old pandas pickles

class _Stub:
    def __setstate__(self, state):
        self.state = state


class _Arr(np.ndarray):
    def __setstate__(self, state):
        if isinstance(state, tuple) and len(state) == 2 and isinstance(state[0], tuple):
            np.ndarray.__setstate__(self, state[0])
            self.extra = state[1]
        else:
            np.ndarray.__setstate__(self, state)


_stub_classes: dict = {}


class _Unpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module.startswith("pandas"):
            key = f"{module}.{name}"
            if key not in _stub_classes:
                base = _Arr if "Index" in name else _Stub
                _stub_classes[key] = type(name, (base,), {"_pandas_name": key})
            return _stub_classes[key]
        return super().find_class(module, name)


def _rebuild(obj):
    """Turn the stubs of an old pandas DataFrame, Series or Index back into pandas objects."""
    if isinstance(obj, np.ndarray):
        return np.asarray(obj)
    if not hasattr(obj, "state"):
        return obj
    kind = type(obj).__name__
    state = obj.state
    if kind == "DataFrame":
        mgr = state
        axes, values, items = mgr.state[:3]
        columns, index = (np.asarray(a) for a in axes)
        data = {}
        for vals, its in zip(values, items):
            for k, col in enumerate(np.asarray(its)):
                data[col] = np.asarray(vals)[k]
        return pd.DataFrame({c: data[c] for c in columns}, index=index)
    if kind == "Series":
        # state is ((ndarray state), index) or similar
        raise NotImplementedError("old Series pickles are not used here")
    return obj


def load_old_pickle(raw: bytes):
    """Load a Python 2 pickle that may hold pandas 0.10 objects; DataFrames are rebuilt."""
    obj = _Unpickler(io.BytesIO(raw), encoding="latin1").load()
    return _rebuild_any(obj)


def _rebuild_any(obj):
    if hasattr(obj, "state") and type(obj).__name__ == "DataFrame":
        return _rebuild(obj)
    if isinstance(obj, dict):
        return {k: _rebuild_any(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return type(obj)(_rebuild_any(v) for v in obj)
    return obj


# ---------------------------------------------------------------- tables from the paper's code

def load_unit_db() -> pd.DataFrame:
    """metadata/unit_db.csv of the paper's code, indexed by ulabel (session-unit)."""
    return pd.read_csv(CODE_RAW + "metadata/unit_db.csv", index_col=0)


def load_sessions_df() -> pd.DataFrame:
    """metadata/sessions_df.csv of the paper's code, indexed by session name."""
    return pd.read_csv(CODE_RAW + "metadata/sessions_df.csv", index_col=0)


def load_figure_index() -> pd.DataFrame:
    """metadata/figures_generated_by_each_script.csv of the paper's code."""
    return pd.read_csv(CODE_RAW + "metadata/figures_generated_by_each_script.csv")


# ---------------------------------------------------------------- sessions

def session_paths() -> pd.DataFrame:
    """One row per session folder: rat, session, and the members it holds."""
    files = list_files()
    rows = {}
    for name in files.name:
        parts = name.split("/")
        if len(parts) < 4 or parts[1] == "miscellaneous":
            continue
        rat, sess, rest = parts[1], parts[2], "/".join(parts[3:])
        r = rows.setdefault(sess, {"rat": rat, "session": sess, "kkp": None, "kkp_extra": None})
        if rest == f"klusters0/{sess}.kkp":
            r["kkp"] = name
        elif rest.endswith(".kkp"):
            r["kkp_extra"] = name
        elif rest in ("trials_info", "trial_timings"):
            r[rest] = name
    return pd.DataFrame(list(rows.values())).set_index("session").sort_index()


def load_trials(session: str, rat: str) -> pd.DataFrame:
    """trial_timings joined to trials_info, as the descriptor says, with every trial kept.

    The trial table's index is the trial number. Munged trials are kept (column is_munged), so
    each claim drops them as its method says.
    """
    base = f"{ROOT}{rat}/{session}/"
    ti = pd.read_csv(io.BytesIO(read_member(base + "trials_info")), index_col=0)
    tt = pd.read_csv(io.BytesIO(read_member(base + "trial_timings")), index_col=0)
    df = tt.join(ti)
    df.index.name = "trial"
    return df


def load_raw_trials_info(session: str, rat: str) -> pd.DataFrame:
    base = f"{ROOT}{rat}/{session}/"
    return pd.read_csv(io.BytesIO(read_member(base + "trials_info")), index_col=0)


def load_spikes(member: str, units=None) -> dict:
    """Spike times (s) of each unit in one kkp file, sorted; only `units` when given."""
    df = load_old_pickle(read_member(member))
    out = {}
    for u, g in df.groupby("unit"):
        if units is None or int(u) in units:
            out[int(u)] = np.sort(g["time"].to_numpy(float))
    return out


def load_all(unit_db: pd.DataFrame, workers: int = 8) -> dict:
    """Every session: trials, and the spike times of its units with include True.

    Returns {session: {"rat", "trials", "spikes": {unum: times}, "kkp_units": all units in file}}.
    """
    paths = session_paths()
    inc = unit_db[unit_db.include]
    wanted = {s: set(g.unum.astype(int)) for s, g in inc.groupby("session_name")}

    def one(item):
        sess, row = item
        trials = load_trials(sess, row.rat)
        spikes, kunits = {}, []
        if isinstance(row.kkp, str):
            df = load_old_pickle(read_member(row.kkp))
            kunits = sorted(int(u) for u in df["unit"].unique())
            for u, g in df.groupby("unit"):
                if int(u) in wanted.get(sess, set()):
                    spikes[int(u)] = np.sort(g["time"].to_numpy(float))
        return sess, {"rat": row.rat, "trials": trials, "spikes": spikes, "kkp_units": kunits}

    with ThreadPoolExecutor(workers) as ex:
        return dict(ex.map(one, paths.iterrows()))


# ---------------------------------------------------------------- stimuli and trial categories

MIXED_STIMNAMES = ["le_hi_lc", "ri_hi_lc", "le_lo_lc", "ri_lo_lc",
                   "le_hi_pc", "ri_hi_pc", "le_lo_pc", "ri_lo_pc"]
CUE_STIMNAMES = ["le_lc_go", "ri_lc_no", "lo_pc_go", "hi_pc_no"]
ALL_STIMNAMES = CUE_STIMNAMES[:2] + CUE_STIMNAMES[2:] + MIXED_STIMNAMES
# Go stimuli of each non-cue block (localization: LEFT; pitch discrimination: LOW).
GO_STIMS = {"le_hi_lc", "le_lo_lc", "le_lo_pc", "ri_lo_pc"}

# Trial categories of 3-2-errhold/main2.py (interference, go-on-nogo error, hit by block).
ERR_CATEGORIES = {
    "hit_LB": [("le_hi_lc", "hit"), ("le_lo_lc", "hit"), ("ri_hi_lc", "hit"), ("ri_lo_lc", "hit")],
    "hit_PB": [("le_hi_pc", "hit"), ("le_lo_pc", "hit"), ("ri_hi_pc", "hit"), ("ri_lo_pc", "hit")],
    "interference_LB": [("ri_lo_lc", "wrong_port"), ("le_lo_lc", "wrong_port")],
    "interference_PB": [("le_hi_pc", "wrong_port"), ("le_lo_pc", "wrong_port")],
    "error_LB": [("ri_hi_lc", "error"), ("ri_lo_lc", "error")],
    "error_PB": [("le_hi_pc", "error"), ("ri_hi_pc", "error")],
}
# Trial categories of 3-2-errhold/main3.py (Figures S2C and S3C).
TYPE_CATEGORIES = {
    "go_LB": [("le_hi_lc", "hit"), ("le_lo_lc", "hit")],
    "nogo_LB": [("ri_hi_lc", "hit"), ("ri_lo_lc", "hit")],
    "gonogo_err_LB": [("ri_hi_lc", "error"), ("ri_lo_lc", "error")],
    "interf_LB": [("le_lo_lc", "wrong_port"), ("ri_lo_lc", "wrong_port")],
    "go_PB": [("le_lo_pc", "hit"), ("ri_lo_pc", "hit")],
    "nogo_PB": [("le_hi_pc", "hit"), ("ri_hi_pc", "hit")],
    "gonogo_err_PB": [("le_hi_pc", "error"), ("ri_hi_pc", "error")],
    "interf_PB": [("le_hi_pc", "wrong_port"), ("le_lo_pc", "wrong_port")],
}


def analysis_trials(trials: pd.DataFrame) -> pd.DataFrame:
    """Trials as the code's kkpandas.io.load_trials_info gives them: munged trials dropped."""
    return trials[~trials.is_munged.astype(bool)]


def count_in_windows(spikes: np.ndarray, starts, stops) -> np.ndarray:
    """Spike counts in [start, stop) for each window (kkpandas.utility.timelock)."""
    return np.searchsorted(spikes, stops) - np.searchsorted(spikes, starts)


# ---------------------------------------------------------------- hold period

def hold_trials(trials: pd.DataFrame, rat: str, **pick) -> pd.DataFrame:
    """Trials for a hold-period count: munged dropped, nonrandom 0, hold > 50 ms (claims M2)."""
    t = analysis_trials(trials)
    t = t[(t.nonrandom == 0) & t.stim_onset.notna()]
    t = t[(t.stim_onset - t.cpoke_start) > MIN_HOLD_S]
    for k, v in pick.items():
        t = t[t[k].isin(v)] if isinstance(v, (list, tuple, set)) else t[t[k] == v]
    return t


def hold_counts(spikes: np.ndarray, trials: pd.DataFrame, rat: str) -> np.ndarray:
    dt = HOLD_MS[rat] / 1000.0
    onset = trials.stim_onset.to_numpy()
    return count_in_windows(spikes, onset - dt, onset)


def mannwhitney_r(x, y) -> float:
    """Two-sided p of R's wilcox.test(x, y, exact=FALSE) (normal approximation, continuity
    corrected); 1.0 when all values are equal, as my.stats.r_utest's fix_nan does."""
    x, y = np.asarray(x, float), np.asarray(y, float)
    if len(np.unique(np.concatenate([x, y]))) < 2:
        return 1.0
    return float(stats.mannwhitneyu(x, y, alternative="two-sided", method="asymptotic",
                                    use_continuity=True).pvalue)


def signedrank_r(x, y=None) -> float:
    """Two-sided p of R's wilcox.test(x, y, paired=TRUE, exact=FALSE): zeros dropped, normal
    approximation with tie and continuity correction."""
    d = np.asarray(x, float) - (0 if y is None else np.asarray(y, float))
    d = d[d != 0]
    if len(d) == 0:
        return 1.0
    return float(stats.wilcoxon(d, zero_method="wilcox", correction=True, method="approx").pvalue)


def bh(p) -> np.ndarray:
    p = np.asarray(p, float)
    return multipletests(p, method="fdr_bh")[1] if len(p) else p


def hold_table(S: dict, unit_db: pd.DataFrame) -> pd.DataFrame:
    """Per included unit, the hold-period counts on hits of blocks 2 (LB) and 4 (PB), their
    means, the unadjusted Mann-Whitney p and the Benjamini-Hochberg p adjusted over all units
    of both regions (reading a of M3) and within each region (reading b)."""
    rows = []
    for ulabel, u in unit_db[unit_db.include].iterrows():
        d = S[u.session_name]
        sp = d["spikes"][int(u.unum)]
        lb = hold_trials(d["trials"], d["rat"], block=2, outcome="hit")
        pb = hold_trials(d["trials"], d["rat"], block=4, outcome="hit")
        clb, cpb = hold_counts(sp, lb, d["rat"]), hold_counts(sp, pb, d["rat"])
        rows.append({"ulabel": ulabel, "session": u.session_name, "rat": d["rat"],
                     "region": u.region, "win_s": HOLD_MS[d["rat"]] / 1000.0,
                     "LB_counts": clb, "PB_counts": cpb,
                     "LB_trials": lb.index.to_numpy(), "PB_trials": pb.index.to_numpy(),
                     "nLB": len(clb), "nPB": len(cpb), "n_spikes": int(clb.sum() + cpb.sum()),
                     "mLB": clb.mean(), "mPB": cpb.mean(), "p": mannwhitney_r(cpb, clb)})
    h = pd.DataFrame(rows).set_index("ulabel")
    h["p_adj"] = bh(h.p)
    h["p_adj_region"] = np.nan
    for reg, idx in h.groupby("region").groups.items():
        h.loc[idx, "p_adj_region"] = bh(h.loc[idx, "p"])
    h["LB_hz"] = h.mLB / h.win_s
    h["PB_hz"] = h.mPB / h.win_s
    h["pref"] = np.where(h.mPB > h.mLB, "PB", np.where(h.mLB > h.mPB, "LB", "tie"))
    return h


def category_counts(spikes, trials, rat, categories) -> dict:
    """Hold counts of the trials of each category (lists of (stim_name, outcome))."""
    t = hold_trials(trials, rat)
    out = {}
    for cat, pairs in categories.items():
        m = np.zeros(len(t), bool)
        for s, o in pairs:
            m |= (t.stim_name == s).to_numpy() & (t.outcome == o).to_numpy()
        out[cat] = hold_counts(spikes, t[m], rat)
    return out


# ---------------------------------------------------------------- spontaneous rate

def spont_rate(spikes: np.ndarray, trials: pd.DataFrame) -> float:
    """3-3-vs_spont/main2.py: the rate over the time between the first and last stimulus onset
    (all trials of trial_timings, munged included) lying more than 2 s from every onset, in
    0.1 s steps."""
    on = np.sort(trials.stim_onset.dropna().to_numpy())
    t0, t1 = on.min(), on.max()
    sp = spikes[(spikes > t0) & (spikes < t1)]
    bins = np.arange(t0, t1, 0.1)

    def far(x):
        i = np.searchsorted(on, x)
        prev = np.abs(x - on[np.clip(i - 1, 0, len(on) - 1)])
        nxt = np.abs(on[np.clip(i, 0, len(on) - 1)] - x)
        return (np.minimum(prev, nxt) > 2.0)

    n_sp = far(sp).sum()
    t_in = far(bins).sum() * 0.1
    return n_sp / t_in if t_in > 0 else np.nan


# ---------------------------------------------------------------- smoothing

def smoothed_trials(spikes, events, centers, sigma=0.05, lo=None, hi=None, discretize=True):
    """Per trial, the spikes within [lo, hi) of the event smoothed with a Gaussian of s.d. `sigma`
    (s) and sampled at `centers` (s from the event).

    With `discretize` (the default), as kkpandas.base.GaussianSmoother.smooth with
    DiscreteAnalyze.PointProc.smooth_event_train does: each spike is moved to the nearest
    sample point, and a Gaussian of s.d. sigma / spacing samples, truncated at 3 s.d. and
    normalized to sum to one, is added there. Without it, each Gaussian is evaluated at the
    sample points from the spike's exact time (a variant)."""
    centers = np.asarray(centers, float)
    events = np.asarray(events, float)
    step = np.mean(np.diff(centers))
    out = np.zeros((len(events), len(centers)))
    i0 = np.searchsorted(spikes, events + lo)
    i1 = np.searchsorted(spikes, events + hi)
    if discretize:
        sd = sigma / step
        half = int(np.rint(3 * sd))
        kern = np.exp(-np.arange(-half, half + 1) ** 2 / (2 * sd ** 2))
        kern /= kern.sum()
        n = len(centers)
        for k, (a, b) in enumerate(zip(i0, i1)):
            if b > a:
                idx = np.rint((spikes[a:b] - events[k] - centers[0]) / step).astype(int)
                idx = idx[(idx >= -half) & (idx < n + half)]
                h = np.bincount(idx + half, minlength=n + 2 * half)[: n + 2 * half]
                out[k] = np.convolve(h, kern, mode="full")[2 * half: 2 * half + n]
        return out
    norm = step / (sigma * np.sqrt(2 * np.pi))
    for k, (a, b) in enumerate(zip(i0, i1)):
        if b > a:
            rel = spikes[a:b] - events[k]
            out[k] = norm * np.exp(-0.5 * ((centers[None, :] - rel[:, None]) / sigma) ** 2).sum(0)
    return out


# ---------------------------------------------------------------- evoked responses

def evoked_counts(spikes, trials, t1, t2):
    on = trials.stim_onset.to_numpy()
    return count_in_windows(spikes, on + t1, on + t2)


def stim_equalized_bootstrap(lb_by_stim, pb_by_stim, n_boots, rng, min_bucket=5):
    """my.bootstrap.difference_CI_bootstrap_wrapper as 6-3-evokgain/main0.py calls it.

    Each draw takes N labels (N the number of localization trials) uniformly over the four
    stimulus pairs and, for each pair, that many trials with replacement from each block; the
    code draws the same number for both blocks (it reuses the localization labels), which is
    kept. Returns the mean over draws of (PB mean minus LB mean) and the two-sided p of a zero
    difference. None when a pair has fewer than `min_bucket` trials in a block.
    """
    if any(len(a) < min_bucket for a in lb_by_stim) or any(len(a) < min_bucket for a in pb_by_stim):
        return None
    k = len(lb_by_stim)
    n0 = sum(len(a) for a in lb_by_stim)
    labels = rng.integers(0, k, size=(n_boots, n0))
    sums = {0: np.zeros(n_boots), 1: np.zeros(n_boots)}
    for c in range(k):
        n_draw = (labels == c).sum(1)
        for g, data in ((0, lb_by_stim[c]), (1, pb_by_stim[c])):
            data = np.asarray(data, float)
            m = n_draw.max()
            idx = rng.integers(0, len(data), size=(n_boots, m))
            vals = data[idx]
            mask = np.arange(m)[None, :] < n_draw[:, None]
            sums[g] += (vals * mask).sum(1)
    diff = (sums[1] - sums[0]) / n0
    cdf = np.mean(diff < 0)
    return {"mdiff": diff.mean(), "p_boot": 2 * min(cdf, 1 - cdf)}


# ---------------------------------------------------------------- timecourses (Figure 5)

def hit_trials(trials: pd.DataFrame, stims=None, blocks=None) -> pd.DataFrame:
    """Hits with nonrandom 0, munged dropped, no hold-length cut (the code's trial pickers
    'random hits' and 'random hits by block', used by 5-1-timecourse and 5-2-timecourse_exemplars)."""
    t = analysis_trials(trials)
    t = t[(t.nonrandom == 0) & (t.outcome == "hit")]
    if stims is not None:
        t = t[t.stim_name.isin(stims)]
    if blocks is not None:
        t = t[t.block.isin(blocks)]
    return t


def first_bin_of_interval(p_adj, auroc, refbin):
    """5-2-timecourse_exemplars/main3.py: from a unit's per-bin adjusted p and AUROC (PB over LB),
    the first bin of the run of bins with p <= 0.05 and the direction of `refbin` that reaches
    back from the bin before `refbin` (t1, after the code's += 1), and the first bin from
    `refbin` on that loses it (t2)."""
    direction = auroc[refbin] > 0.5
    lost = (p_adj > 0.05) | ((auroc < 0.5) if direction else (auroc > 0.5))
    fwd = np.where(lost[refbin:])[0]
    end = refbin + fwd[0] if len(fwd) else len(p_adj)
    back = lost[:refbin][::-1]
    bidx = np.where(back)[0]
    begin = (refbin - 1 - bidx[0]) if len(bidx) else -1
    return begin + 1, end


# ---------------------------------------------------------------- video tracking, disruption, catch trials, model

VIDTRACK_SESSIONS = ["CR24A_121022_001_behaving", "CR20B_120602_001_behaving", "CR17B_110803_001_behaving"]


def load_head_angles(session: str) -> pd.DataFrame:
    """Ear positions of miscellaneous/vidtrack/<session>/<session>.pdict, one row per trial, and
    the head angle as vidtrack.vts_db2head_pos_df computes it (degrees): arctan(dx / dy) of the
    right minus left ear. Image names (some pickled as bytes) give the trial number, as the
    code's regex (\\d+).png does."""
    d = load_old_pickle(read_member(f"{ROOT}miscellaneous/vidtrack/{session}/{session}.pdict"))
    rows = []
    for k, v in d.items():
        name = k.decode() if isinstance(k, (bytes, np.bytes_)) else str(k)
        rows.append({"btrial": int(name.split(".")[0]), "Lx": v["left"][0], "Ly": v["left"][1],
                     "Rx": v["right"][0], "Ry": v["right"][1]})
    df = pd.DataFrame(rows).set_index("btrial").sort_index()
    df["angl"] = np.degrees(np.arctan((df.Rx - df.Lx) / (df.Ry - df.Ly)))
    return df


def stand_mad_uncentered(a, axis=0):
    """The median of |a| / 0.6745, without subtracting the median: what the comment in
    3-5-vidtrack/main5.py says statsmodels' stand_mad did (a variant)."""
    return np.median(np.abs(np.asarray(a)) / 0.6744897501960817, axis=axis)


def stand_mad_centered(a, axis=0):
    """Scaled median absolute deviation about the median, statsmodels.robust.mad's default
    (the claims file's 'statsmodels stand_mad')."""
    a = np.asarray(a)
    return np.median(np.abs(a - np.median(a, axis=axis, keepdims=True)) / 0.6744897501960817, axis=axis)


def _mw_greater_vs_pooled(post, pre_sorted, pre_vals, pre_counts, pre_tie):
    """Two-sided normal-approximation Mann-Whitney p (tie and continuity corrected, as R's
    wilcox.test with exact=FALSE) of each column of `post` against the pooled `pre` sample,
    and whether the column's values are the greater. Ranks come from searchsorted on the
    sorted pooled sample, so a pooled sample of 10^5 values costs one sort."""
    n1, n2 = post.shape[0], len(pre_sorted)
    lo = np.searchsorted(pre_sorted, post, side="left")
    hi = np.searchsorted(pre_sorted, post, side="right")
    # U of post: pairs where post > pre, plus half the ties (ties within post do not count)
    U = (lo + 0.5 * (hi - lo)).sum(0)
    p = np.empty(post.shape[1])
    n = n1 + n2
    for j in range(post.shape[1]):
        pv, pc = np.unique(post[:, j], return_counts=True)
        k = np.searchsorted(pre_vals, pv)
        k = np.clip(k, 0, len(pre_vals) - 1)
        match = pre_vals[k] == pv
        base = np.where(match, pre_counts[k], 0)
        tie = pre_tie - (base[match] ** 3 - base[match]).sum() + ((base + pc) ** 3 - (base + pc)).sum()
        sigma = np.sqrt(n1 * n2 / 12.0 * ((n + 1) - tie / (n * (n - 1))))
        z = U[j] - n1 * n2 / 2.0
        z = (z - np.sign(z) * 0.5) / sigma if sigma > 0 else 0.0
        p[j] = 2 * stats.norm.sf(abs(z))
    return p, U > n1 * n2 / 2.0


def onset_window(spikes, onsets, alpha=0.05, bin_s=0.0005, sigma=0.001, post_s=0.05, pre_s=0.05):
    """Reading (b) of claims M4, the Supplement's 'Calculation of evoked responses': spike trains
    smoothed per trial with a 1 ms Gaussian (the code's discretized smoother, sampled every
    0.5 ms), each 0.5 ms bin after onset compared with all 0.5 ms bins of the 50 ms before onset
    by an unpaired Mann-Whitney test; the first run of contiguous bins all significantly greater
    is the window. The paper leaves open the per-bin threshold, any correction and how far after
    onset to look: p < 0.05 uncorrected and 50 ms (the code's evoked folding window, 0 to 50 ms)
    are the choices here. Returns (t1, t2) in s, the window's start and end, or None."""
    centers = np.arange(-pre_s, post_s, bin_s) + bin_s / 2
    sm = smoothed_trials(spikes, onsets, centers, sigma, lo=-pre_s - 0.01, hi=post_s + 0.01)
    pre = np.sort(sm[:, centers < 0].ravel())
    vals, counts = np.unique(pre, return_counts=True)
    tie = float((counts.astype(float) ** 3 - counts).sum())
    post = sm[:, centers > 0]
    p, greater = _mw_greater_vs_pooled(post, pre, vals, counts.astype(float), tie)
    sig = (p < alpha) & greater
    if not sig.any():
        return None
    i0 = int(np.argmax(sig))
    i1 = i0 + (int(np.argmax(~sig[i0:])) if (~sig[i0:]).any() else len(sig) - i0)
    t_post = centers[centers > 0]
    return float(t_post[i0] - bin_s / 2), float(t_post[i1 - 1] + bin_s / 2)
