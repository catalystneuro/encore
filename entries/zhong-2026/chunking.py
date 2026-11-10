"""Loading and measures for testing Zhong, Katkov & Tsodyks (2026) on DANDI:000207.

The paper (eLife reviewed preprint, doi:10.7554/eLife.109538.1) reanalyses the human
medial temporal lobe single-neuron recordings of Zheng et al. 2022 (ref. [41], Nat Neurosci
25:358) for its Figure 3 and Figure S3. Files are streamed from the DANDI archive with
remfile, h5py and pynwb; nothing is written to disk.

Where each parameter comes from:

- VERSION: the version the paper cites (Methods E, "Data analyzed in Fig. 3 is downloaded
  from the DANDI Archive at https://dandiarchive.org/dandiset/000207/0.220216.0323").
- Cut times. The encoding table gives boundary1_time to boundary3_time per clip and the clip
  category stimCategory (0 NB, 1 SB, 2 HB). How they map to cuts is taken from the
  dataset's own example code (rutishauserlab/cogboundary-zheng, commit 60f7ece,
  B01_raster_psth_encoding_BAligned_BSep_NWB.m): for SB clips boundary1 to boundary3 are
  soft boundaries, for HB clips boundary1 is the hard boundary and boundary2, boundary3 are
  soft boundaries within the clip, for NB clips boundary1 is the virtual boundary in the
  middle of the clip; boundaries that do not exist are set to the clip's start time in this
  version (the code prunes them).
- Selection of boundary and onset neurons (claims fig3a-dip-after-boundary reading 1b and
  fig3c-onset-control reading b): the Methods of [41] (read at PMC8966433), "Boundary cell",
  "Event cell" and the legend of its Extended Data Fig. 5 for clip onset cells. Spike counts
  in [0, 1] s after and [-1, 0] s before each boundary (or clip onset); permutation t-tests
  with 1000 permutations ([41], "Statistics": "permutation tests were conducted to generate
  a null distribution estimated from 1000 runs on data with scrambled labels"); p < 0.05.
  Whether the post-against-baseline test pairs the two windows of each trial is not said:
  both readings are run (`paired=True`, a sign-flip test on per-trial differences, and
  `paired=False`, a two-sample test with the window labels permuted). The comparisons
  between boundary types use different trials and are two-sample tests. "Significantly
  greater" is one-sided; "significantly different" two-sided; the onset test is one-tailed
  ([41], Extended Data Fig. 5 legend), taken as post greater than pre, since onset neurons
  "show a peak" (Zhong et al., Results on Fig. 3c).
- Pooling and z-scoring (claims file, from Methods E of the paper): per subject the raw rates
  of all neurons of a group are averaged over neurons and trials, the trace is z-scored, and
  the z-scored traces are averaged across subjects; the shade is one standard deviation
  across subjects.
- Bins (10 or 25 ms), Gaussian smoothing (none or 50 ms SD), the window (-1 to 2 s), the
  z-score reference (whole window or -1 to 0 s), and the dip, peak and ramp measures are
  the readings and measures fixed by the claims file's criteria.
- Random seeds are standard choices that cannot change a conclusion beyond the
  permutation noise; each call takes its own generator.
"""

from __future__ import annotations

import warnings
from dataclasses import dataclass, field

import h5py
import numpy as np
import remfile
import requests

DANDISET = "000207"
VERSION = "0.220216.0323"
API = "https://api.dandiarchive.org/api"

WINDOW = (-1.0, 2.0)  # s around the cut or onset; claims file, fig3a criterion (4)
N_PERM = 1000  # [41], Statistics paragraph


def list_assets(version: str = VERSION) -> list[dict]:
    url = f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=200"
    out = requests.get(url, timeout=60).json()["results"]
    return sorted(out, key=lambda a: int(a["path"].split("/")[0][4:]))


def asset_url(asset_id: str, version: str = VERSION) -> str:
    m = requests.get(f"{API}/dandisets/{DANDISET}/versions/{version}/assets/{asset_id}/",
                     timeout=60).json()
    return [u for u in m["contentUrl"] if "s3" in u][0]


@dataclass
class Session:
    path: str
    identifier: str  # e.g. P64CS_CBID12; the part before "_CBID" is the ID of [41]
    subject_id: str
    age: str
    sex: str
    clip_start: np.ndarray
    clip_stop: np.ndarray
    category: np.ndarray  # 0 NB, 1 SB, 2 HB
    b: np.ndarray  # (n_clips, 3) boundary1..3 times
    spikes: list = field(default_factory=list)  # one array per unit, s
    unit_location: list = field(default_factory=list)
    n_recog: int = 0
    n_timediscrim: int = 0
    recog_start: np.ndarray | None = None
    timediscrim_start: np.ndarray | None = None

    @property
    def patient(self) -> str:
        return self.identifier.split("_CBID")[0]

    def cuts(self, which: str = "all") -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Boundary times, their type (0 NB virtual, 1 SB, 2 HB) and clip index.

        which="all": every boundary, as in the dataset's example code (135 in a full
        session). which="first": boundary1 of each clip only (one per clip, 90).
        """
        t, k, c = [], [], []
        for i in range(len(self.category)):
            cat = self.category[i]
            cols = [0] if which == "first" else [0, 1, 2]
            for j in cols:
                bt = self.b[i, j]
                if j > 0 and (bt <= self.clip_start[i] + 1e-9 or cat == 0):
                    continue  # not a boundary (set to the clip start)
                if j == 0:
                    typ = {0: 0, 1: 1, 2: 2}[int(cat)]
                else:
                    typ = 1  # boundary2/3 are soft in SB and HB clips
                t.append(bt); k.append(typ); c.append(i)
        return np.array(t), np.array(k), np.array(c)


def load_session(asset: dict, version: str = VERSION) -> Session:
    import pynwb

    url = asset_url(asset["asset_id"], version)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        f = h5py.File(remfile.File(url), "r")
        io = pynwb.NWBHDF5IO(file=f, load_namespaces=True)
        nwb = io.read()
        enc = nwb.intervals["encoding_table"]
        start = np.asarray(enc["start_time"].data[:])
        stop = np.asarray(enc["stop_time"].data[:])
        cat = np.asarray(enc["stimCategory"].data[:]).astype(int)
        b = np.column_stack([np.asarray(enc[f"boundary{j}_time"].data[:]) for j in (1, 2, 3)])
        st = np.asarray(nwb.units["spike_times"].target.data[:])
        ends = np.asarray(nwb.units["spike_times"].data[:])
        elec = np.asarray(nwb.units["electrodes"].data[:]).astype(int)
        loc = np.asarray(nwb.electrodes["location"].data[:])
        loc = [x.decode() if isinstance(x, bytes) else str(x) for x in loc]
        spikes = np.split(st, ends[:-1])
        s = Session(
            path=asset["path"], identifier=nwb.identifier,
            subject_id=str(nwb.subject.subject_id), age=str(nwb.subject.age),
            sex=str(nwb.subject.sex), clip_start=start, clip_stop=stop, category=cat, b=b,
            spikes=[np.asarray(x) for x in spikes], unit_location=[loc[e] for e in elec],
            n_recog=len(nwb.intervals["recognition_table"]),
            n_timediscrim=len(nwb.intervals["timediscrimination_table"]),
            recog_start=np.asarray(nwb.intervals["recognition_table"]["start_time"].data[:]),
            timediscrim_start=np.asarray(nwb.intervals["timediscrimination_table"]["start_time"].data[:]),
        )
        io.close()
    return s


# ---------------------------------------------------------------- counts and tests

def window_counts(spikes: np.ndarray, times: np.ndarray, lo: float, hi: float) -> np.ndarray:
    """Spike counts of one unit in [t + lo, t + hi) for each t."""
    return (np.searchsorted(spikes, times + hi) - np.searchsorted(spikes, times + lo)).astype(float)


def _t_paired(d: np.ndarray) -> np.ndarray:
    # d: (..., n); one-sample t of the differences
    n = d.shape[-1]
    m = d.mean(-1)
    s = d.std(-1, ddof=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(s > 0, m / (s / np.sqrt(n)), 0.0)


def _t_two(x: np.ndarray, mask: np.ndarray) -> np.ndarray:
    # x: (n,), mask: (P, n) group membership; Welch-free pooled t of group1 - group0
    n1 = mask.sum(-1)
    n0 = mask.shape[-1] - n1
    s1 = (mask * x).sum(-1)
    s0 = x.sum() - s1
    q1 = (mask * x ** 2).sum(-1)
    q0 = (x ** 2).sum() - q1
    m1, m0 = s1 / n1, s0 / n0
    v = (q1 - n1 * m1 ** 2 + q0 - n0 * m0 ** 2) / (n1 + n0 - 2)
    with np.errstate(divide="ignore", invalid="ignore"):
        se = np.sqrt(v * (1 / n1 + 1 / n0))
        return np.where(se > 0, (m1 - m0) / se, 0.0)


def perm_paired(post: np.ndarray, pre: np.ndarray, rng, alternative="two-sided") -> float:
    """Permutation t-test on per-trial differences (random sign flips)."""
    d = post - pre
    if np.all(d == 0):
        return 1.0
    t0 = _t_paired(d)
    signs = rng.choice([-1.0, 1.0], size=(N_PERM, len(d)))
    tp = _t_paired(signs * d)
    return _pval(t0, tp, alternative)


def perm_two(a: np.ndarray, b: np.ndarray, rng, alternative="two-sided") -> float:
    """Two-sample permutation t-test of a against b (group labels permuted)."""
    x = np.concatenate([a, b])
    if np.all(x == x[0]):
        return 1.0
    obs = np.zeros(len(x), bool); obs[: len(a)] = True
    t0 = _t_two(x, obs[None, :])[0]
    masks = np.array([rng.permutation(obs) for _ in range(N_PERM)])
    tp = _t_two(x, masks)
    return _pval(t0, tp, alternative)


def _pval(t0, tp, alternative):
    if alternative == "greater":
        k = (tp >= t0).sum()
    else:
        k = (np.abs(tp) >= abs(t0)).sum()
    return (k + 1) / (len(tp) + 1)


def post_pre_test(post, pre, rng, paired, alternative="two-sided"):
    if paired:
        return perm_paired(post, pre, rng, alternative)
    return perm_two(post, pre, rng, alternative)


def classify_unit(spk: np.ndarray, cut_t: np.ndarray, cut_k: np.ndarray, onsets: np.ndarray,
                  rng, paired: bool, alpha: float = 0.05) -> dict:
    """Boundary (soft), event (hard) and onset classification of [41] for one unit."""
    post = window_counts(spk, cut_t, 0.0, 1.0)
    pre = window_counts(spk, cut_t, -1.0, 0.0)
    p = {}
    for k, name in ((0, "NB"), (1, "SB"), (2, "HB")):
        m = cut_k == k
        p[f"pp_{name}"] = post_pre_test(post[m], pre[m], rng, paired)
    nb, sb, hb = (post[cut_k == k] for k in (0, 1, 2))
    p["SB>NB"] = perm_two(sb, nb, rng, "greater")
    p["HB>NB"] = perm_two(hb, nb, rng, "greater")
    p["HB>SB"] = perm_two(hb, sb, rng, "greater")
    p["SBHB>NB"] = perm_two(np.concatenate([sb, hb]), nb, rng, "greater")
    a = alpha
    soft = (p["pp_SB"] < a and p["pp_HB"] < a and p["pp_NB"] >= a
            and p["SB>NB"] < a and p["HB>NB"] < a)
    soft_pooled = (p["pp_SB"] < a and p["pp_HB"] < a and p["pp_NB"] >= a
                   and p["SBHB>NB"] < a)
    hard = (p["pp_HB"] < a and p["pp_NB"] >= a and p["pp_SB"] >= a
            and p["HB>NB"] < a and p["HB>SB"] < a)
    on_post = window_counts(spk, onsets, 0.0, 1.0)
    on_pre = window_counts(spk, onsets, -1.0, 0.0)
    p["p_onset"] = post_pre_test(on_post, on_pre, rng, paired, "greater")
    return dict(p, soft=soft, soft_pooled=soft_pooled, hard=hard, onset=p["p_onset"] < a,
                rate=len(spk) / max(spk[-1] - spk[0], 1.0) if len(spk) > 1 else 0.0)


def classify_session(s: Session, rng, paired: bool, which: str = "all") -> list[dict]:
    t, k, _ = s.cuts(which)
    return [classify_unit(sp, t, k, s.clip_start, rng, paired) for sp in s.spikes]


# ---------------------------------------------------------------- traces

def unit_rates(spk: np.ndarray, times: np.ndarray, bin_s: float, smooth_sd: float | None):
    """Rates (Hz) of one unit, (n_trials, n_bins), over WINDOW around each time."""
    lo, hi = WINDOW
    edges = np.arange(lo, hi + bin_s / 2, bin_s)
    out = np.empty((len(times), len(edges) - 1))
    for i, t in enumerate(times):
        a, b = np.searchsorted(spk, [t + lo, t + hi])
        out[i] = np.histogram(spk[a:b] - t, edges)[0]
    out /= bin_s
    if smooth_sd:
        from scipy.ndimage import gaussian_filter1d
        out = gaussian_filter1d(out, smooth_sd / bin_s, axis=1, mode="nearest")
    return out, (edges[:-1] + edges[1:]) / 2


def pooled_trace(spikes: list, times: np.ndarray, bin_s: float, smooth_sd):
    """Raw rates of all given units pooled (averaged) over units and trials."""
    acc = None
    for sp in spikes:
        r, centers = unit_rates(sp, times, bin_s, smooth_sd)
        acc = r.mean(0) if acc is None else acc + r.mean(0)
    return acc / len(spikes), centers


def zscore(trace: np.ndarray, centers: np.ndarray, ref: str) -> np.ndarray:
    m = centers < 0 if ref == "pre" else np.ones_like(centers, bool)
    sd = trace[m].std()
    return (trace - trace[m].mean()) / sd if sd > 0 else trace * np.nan


def dip_ramp(bound: np.ndarray | None, rest: np.ndarray, centers: np.ndarray,
             peak_t: float | None = None) -> dict:
    """Measures fixed by the fig3a criterion.

    Peak: maximum of the boundary (or onset) trace after time zero. Dip: minimum of the
    other trace from the peak to 500 ms after it. Lag: dip time minus peak time. Dip present
    when its value is below the mean of the other trace from -1 to 0 s. Ramp present when a
    line fitted to the other trace from the dip to 1 s has positive slope.
    """
    if peak_t is None:
        after = centers > 0
        peak_t = centers[after][np.argmax(bound[after])]
    m = (centers >= peak_t) & (centers <= peak_t + 0.5)
    i = np.where(m)[0][np.argmin(rest[m])]
    dip_t, dip_v = centers[i], rest[i]
    base = rest[centers < 0].mean()
    r = (centers >= dip_t) & (centers <= 1.0)
    slope = np.polyfit(centers[r], rest[r], 1)[0] if r.sum() >= 2 else np.nan
    return dict(peak_t=peak_t, dip_t=dip_t, lag_ms=1000 * (dip_t - peak_t), dip_v=dip_v,
                base=base, depth=dip_v - base, dip=bool(dip_v < base), slope=slope,
                ramp=bool(slope > 0))


# ---------------------------------------------------------------- outside reference values

# Supplementary Table 2 of Zheng et al. 2022 (ref. [41]), "Subject information", page 16 of
# the Supplementary Information PDF (41593_2022_1020_MOESM1_ESM.pdf, doi:10.1038/s41593-022-01020-w).
# The table is an image in the PDF, so it is transcribed here by hand. Columns: subject ID
# (CBID), age, sex, all cells, boundary cells in MTL, boundary cells outside MTL, event cells
# in MTL, event cells outside MTL, clip-onset responsive cells. The table spells TWH103 as
# "THW103". Used only as reference values (link claim) and for reading (a) of the subject
# exclusion; it names no unit, so it cannot select neurons.
ZHENG_S2_COLUMNS = ("cbid", "age", "sex", "all_cells", "boundary_mtl", "boundary_out",
                    "event_mtl", "event_out", "onset")
ZHENG_S2 = {
    "P60CS": (1, 67, "M", 70, 1, 1, 2, 0, 3),
    "P61CS": (2, 52, "F", 74, 2, 0, 3, 0, 6),
    "TWH101": (3, 25, "F", 50, 1, 0, 0, 1, 7),
    "TWH103": (4, 49, "M", 57, 4, 1, 0, 1, 0),
    "TWH109": (5, 28, "M", 49, 3, 1, 2, 1, 0),
    "TWH110": (6, 38, "M", 31, 1, 0, 1, 0, 6),
    "TWH111": (7, 63, "F", 55, 3, 1, 1, 2, 0),
    "TWH113": (8, 36, "M", 54, 3, 1, 3, 1, 5),
    "P62CS": (9, 25, "F", 51, 3, 0, 2, 1, 3),
    "TWH116": (10, 25, "F", 44, 2, 0, 1, 0, 6),
    "TWH117": (11, 68, "F", 21, 2, 0, 0, 0, 4),
    "P64CS": (12, 63, "F", 70, 3, 1, 3, 0, 5),
    "P65CS": (13, 55, "F", 78, 4, 0, 5, 0, 4),
    "TWH120": (14, 25, "F", 49, 2, 0, 2, 1, 5),
    "TWH125": (15, 24, "M", 51, 3, 1, 2, 1, 0),
    "TWH126": (16, 25, "M", 22, 0, 0, 1, 0, 5),
    "TWH127": (17, 28, "M", 44, 2, 1, 2, 0, 4),
    "TWH129": (18, 25, "F", 47, 3, 0, 4, 0, 7),
    "TWH138": (19, 46, "F", 26, 0, 0, 2, 0, 6),
}


def zheng_table():
    import pandas as pd
    return pd.DataFrame.from_dict(ZHENG_S2, orient="index", columns=list(ZHENG_S2_COLUMNS))


# ---------------------------------------------------------------- sessions and selection

def spikes_on_trial_clock(s: Session) -> bool:
    """Whether the spike times fall within the span of the session's trial tables."""
    st = np.concatenate([x for x in s.spikes if len(x)])
    lo, hi = s.clip_start.min(), s.clip_stop.max()
    return bool(np.mean((st > lo - 60) & (st < hi + 3600)) > 0.5)


def select_units(sessions: list, paired: bool, which: str, seed: int):
    """Classify every unit of the given sessions; one generator per call."""
    import pandas as pd
    rng = np.random.default_rng(seed)
    rows = []
    for s in sessions:
        for u, r in enumerate(classify_session(s, rng, paired, which)):
            rows.append(dict(patient=s.patient, unit=u, location=s.unit_location[u], **r))
    return pd.DataFrame(rows)


def shuffled_selection_rate(sessions: list, n_shuffle: int, seed: int, paired: bool = True):
    """Fraction of units classified as boundary (soft) or event (hard) cells when the boundary
    labels (NB, SB, HB) are shuffled across boundaries, as in [41], "Chance level for cell
    response analyses" (1000 shuffles there; fewer here, see the notebook)."""
    rng = np.random.default_rng(seed)
    soft, hard, n = [], [], 0
    for _ in range(n_shuffle):
        ns = nh = n = 0
        for s in sessions:
            t, k, _ = s.cuts("all")
            kk = rng.permutation(k)
            for sp in s.spikes:
                r = classify_unit(sp, t, kk, s.clip_start, rng, paired)
                ns += r["soft"]; nh += r["hard"]; n += 1
        soft.append(ns / n); hard.append(nh / n)
    return np.array(soft), np.array(hard), n


# ---------------------------------------------------------------- traces per unit

def unit_mean_rates(s: Session, times: np.ndarray, bin_s: float):
    """Trial-averaged rate (Hz) of every unit of a session, (n_units, n_bins), no smoothing.

    Pooling over neurons and trials (Methods E) is then the mean of these rows, because
    every unit of a session has the same trials; smoothing, which is linear, is applied to
    the pooled trace.
    """
    out = []
    for sp in s.spikes:
        r, centers = unit_rates(sp, times, bin_s, None)
        out.append(r.mean(0))
    return np.array(out), centers


def smooth(trace: np.ndarray, bin_s: float, sd: float | None) -> np.ndarray:
    if not sd:
        return trace
    from scipy.ndimage import gaussian_filter1d
    return gaussian_filter1d(trace, sd / bin_s, mode="nearest")


# ---------------------------------------------------------------- clock check

def clock_decoding(s: Session, shift: float = 0.0, seed: int = 0) -> float:
    """Cross-validated accuracy of decoding the window after clip onset (0 to 1 s) from the
    window before it (-1 to 0 s), from the population's spike counts. With the onset times
    shifted (shift > 0) the two windows are no longer tied to the onsets and accuracy falls
    to chance. A standard check of the protocol, not a method of the paper."""
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import StratifiedKFold, cross_val_score
    t = s.clip_start + shift
    post = np.column_stack([window_counts(sp, t, 0, 1) for sp in s.spikes])
    pre = np.column_stack([window_counts(sp, t, -1, 0) for sp in s.spikes])
    X = np.vstack([post, pre]); y = np.r_[np.ones(len(t)), np.zeros(len(t))]
    if X.sum() == 0:
        return float("nan")
    X = np.log1p(X)
    cv = StratifiedKFold(5, shuffle=True, random_state=seed)
    return float(cross_val_score(LogisticRegression(C=0.1, max_iter=2000), X, y, cv=cv).mean())


def clock_population_t(s: Session, shift: float = 0.0, times: np.ndarray | None = None) -> float:
    """Paired t statistic, over trials, of the population's summed spike count in the 1 s after
    trial onset (clip onset by default) minus the 1 s before it. A standard check, not a
    method of the paper."""
    t = (s.clip_start if times is None else times) + shift
    d = sum(window_counts(sp, t, 0, 1) - window_counts(sp, t, -1, 0) for sp in s.spikes)
    return float(_t_paired(np.asarray(d)[None, :])[0])
