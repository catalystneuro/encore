"""Loading and measures for Elie & Theunissen (2019) on CRCNS aa-4.

Data. CRCNS aa-4 is unversioned; the files are read from the public S3 bucket
crcnsarchive under aa-4/live/data/, one tar.gz per bird. Each tar.gz is read as
a stream (tarfile mode "r|gz" over fsspec), each h5 member is opened in memory
with h5py, reduced to what the analysis needs, and dropped. Nothing is written
to disk.

Parameters and where they come from (claims file header, Methods R, B, P):
- Window 0 to 600 ms after stimulus onset, 60 bins of 10 ms (Methods B; paper,
  Methods, "Here, we analyzed the neural response in the first 600ms").
- Call stimuli: in the unit's Call group, stim_type "call" with call types Ag
  (Wsst, Ws), Be, DC, Di, LT, Ne, Te, Th, and the songs of the vocalization bank
  (So). Whines (Wh), noise and the search songs are dropped (claims header,
  selVoc.m; paper, S4 Fig legend).
"""
from __future__ import annotations

import io
import tarfile

from concurrent.futures import ProcessPoolExecutor

import fsspec
import h5py
import numpy as np

BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/aa-4/live/data/"
BIRDS = ["BlaBro09xxF", "GreBlu9508M", "LblBlu2028M", "WhiBlu5396M", "WhiWhi4522M", "YelBlu6903F"]
# md5 sums from aa-4/live/checksums.md5, read on 2026-11-13
MD5 = {
    "BlaBro09xxF": "ee387cc051e5fa5ee66a5f4db5d8bae6",
    "GreBlu9508M": "16f1bb223946288f8b426d6382f06510",
    "LblBlu2028M": "80c181eb8bd70ddbbd9b3aa46587dfb5",
    "WhiBlu5396M": "2ba7776cd4130d0090b13e5f5c0359fd",
    "WhiWhi4522M": "c47d6660019a2a0d1e3375ce7da68bf1",
    "YelBlu6903F": "6027933cdf765dd0b67f811b1a133095",
}
CALL_TYPES = ["Ag", "Be", "DC", "Di", "LT", "Ne", "Te", "Th", "So"]
T_MAX = 0.6  # s, analysis window (Methods B)
# Spikes are kept from KEEP[0] to KEEP[1] s around onset; the 600 ms before onset
# serve the check of the clock (protocol, author step 2). A standard choice.
KEEP = (-0.6, 0.6)


def _s(x):
    if hasattr(x, "item"):
        x = x.item()
    return x.decode() if isinstance(x, bytes) else x


def read_unit(h: h5py.File, name: str, bird: str) -> dict:
    """Reduce one unit's h5 file to its attributes, its stored coherence
    (class_info) and, for single units, the spike times of each trial of its call
    and song stimuli in KEEP, in seconds from stimulus onset, as stored."""
    u = {"bird": bird, "file": name.split("/")[-1]}
    for k, v in h.attrs.items():
        u[k] = _s(v)
    u["groups"] = list(h.keys())
    # spikes are kept for single units only; other files keep their metadata
    single = is_single(u)
    stims = []
    n_unsorted = 0  # trials whose stored spike times are not in increasing order
    for g in h.keys():
        if g in ("class_info", "extra_info"):
            continue
        for sn, sg in h[g].items():
            a = {k: _s(v) for k, v in sg.attrs.items()}
            st = {"group": g, "number": sn, **{k: a.get(k) for k in (
                "callid", "callerAge", "stim_type", "stim_class", "stim_source", "stim_source_sex",
                "stim_duration", "original_wavfile", "stim_md5")}}
            if not single or a.get("stim_type") not in ("call", "song"):
                # keep only metadata of non-call stimuli
                st["trials"] = None
                st["ntrials"] = len(sg)
                stims.append(st)
                continue
            trials = []
            for tn in sorted(sg.keys(), key=lambda x: int(x) if x.isdigit() else x):
                tg = sg[tn]
                t = np.asarray(tg["spike_times"][()], dtype=float).ravel()
                ids = np.asarray(tg["spike_ids"][()], dtype=float).ravel()
                if ids.size == 1 and ids[0] == -999:
                    t = np.empty(0)
                n_unsorted += int(np.any(np.diff(t) < 0))
                trials.append(np.sort(t[(t >= KEEP[0]) & (t < KEEP[1])]).astype(np.float32))
            st["trials"] = trials
            st["ntrials"] = len(trials)
            stims.append(st)
    u["stims"] = stims
    u["n_unsorted_trials"] = n_unsorted
    ci = {}
    if "class_info" in h:
        for g, cg in h["class_info"].items():
            c = cg["coherence"]
            ci[g] = {"mean_rate": float(cg["mean_rate"][()].ravel()[0]),
                     "info": float(c["info"]["mean"][()].ravel()[0]),
                     "info_lower": float(c["info"]["lower"][()].ravel()[0]),
                     "cutoff": float(c["cutoff_frequency"][()].ravel()[0]),
                     "f": c["frequencies"][()].ravel(), "c": c["mean"][()].ravel()}
    u["class_info"] = ci
    u["has_class_info"] = "class_info" in h
    u["has_extra_info"] = "extra_info" in h
    return u


def stream_bird(bird: str, block_size: int = 2**23) -> list[dict]:
    """Stream one bird's tar.gz and return the reduced units of all its h5 files."""
    units = []
    with fsspec.open(BASE + bird + ".tar.gz", block_size=block_size).open() as f:
        with tarfile.open(fileobj=f, mode="r|gz") as tar:
            for m in tar:
                if not m.isfile():
                    continue
                if m.name.endswith(".h5"):
                    b = tar.extractfile(m).read()
                    with h5py.File(io.BytesIO(b), "r") as h:
                        units.append(read_unit(h, m.name, bird))
    return units


def load_all(birds=BIRDS, workers: int = 4) -> list[dict]:
    """All units of all birds, the birds streamed in parallel processes."""
    order = sorted(birds, key=lambda b: ["LblBlu2028M", "WhiBlu5396M"].count(b))
    with ProcessPoolExecutor(workers) as ex:
        res = dict(zip(order, ex.map(stream_bird, order)))
    return [u for b in birds for u in res[b]]


def is_single(u: dict) -> bool:
    """A unit whose file is labelled a single unit (sortType "single"; three
    files store it truncated as "singl")."""
    return str(u.get("sortType", "")).startswith("singl")


def iar(u: dict) -> float:
    """I_AR (bits/s) of the unit's call protocol, as stored in class_info."""
    v = [c["info"] for g, c in u["class_info"].items() if g.startswith("Call")]
    return max(v) if v else np.nan


def call_type(s: dict) -> str | None:
    """Call type of a stimulus. Songs of the vocalization bank (named after their
    caller) are So; the songs of the search set (files STRFxx..._So_*.wav) and the
    noises are not call stimuli (paper, S4 Fig legend; claims header)."""
    if s["stim_type"] == "call":
        return s["callid"] if s["callid"] in CALL_TYPES else None
    if s["stim_type"] == "song":
        w = (s.get("original_wavfile") or "").split("/")[-1]
        return None if w.startswith("STRF") else "So"
    return None


def call_stims(u: dict) -> list[dict]:
    """The call stimuli of a unit, with their call type in "ct"."""
    out = []
    for s in u["stims"]:
        ct = call_type(s)
        if ct is not None and s["trials"] is not None:
            out.append({**s, "ct": ct})
    return out


# ---------------------------------------------------------------------------
# Time-varying rate and information (claims header, Methods R, B and I)
# ---------------------------------------------------------------------------
from scipy.stats import poisson  # noqa: E402

R_MAX = 20      # spike counts summed from 0 to 20 (paper, Methods, The instantaneous information)
MU_MIN = 1 / 20  # lower bound on the Poisson mean of a bin (same paragraph; code, MuLims)


def kde_rate(spike_times_ms: np.ndarray, n_trials: int, duration_ms: int) -> np.ndarray:
    """Locally adaptive KDE rate (spikes/ms) at 1 kHz, by ssvkernel (Shimazaki and
    Shinomoto; paper reference 42; Methods, Time-varying spike rate estimation),
    from the Python port in the adaptivekde package. The density is scaled by the
    number of spikes over the number of trials. A set with no spike gets
    1/(2*Ntrials*duration) per ms and one with a single spike 1/(Ntrials*duration)
    per ms (same paragraph)."""
    import warnings
    from adaptivekde import ssvkernel
    tin = np.arange(duration_ms) + 0.5
    x = np.asarray(spike_times_ms, dtype=float)
    if x.size == 0:
        return np.full(duration_ms, 1 / (2 * n_trials * duration_ms))
    if x.size == 1 or np.unique(x).size == 1:
        return np.full(duration_ms, x.size / (n_trials * duration_ms))
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        y = ssvkernel(x, tin, nbs=1)[0]  # nbs: bootstrap CI, unused
    return y * x.size / n_trials


def bin_means(rate_1khz: np.ndarray, bin_ms: int = 10) -> np.ndarray:
    """Poisson mean of each bin: the rate summed over the bin, bounded below by
    1/20 (claims header, Methods B)."""
    r = rate_1khz[: (rate_1khz.size // bin_ms) * bin_ms].reshape(-1, bin_ms).sum(1)
    return np.maximum(r, MU_MIN)


def _pyx(mu: np.ndarray) -> np.ndarray:
    """p(y|s) for y = 0..R_MAX; mu has shape (..., ) -> (..., R_MAX+1)."""
    y = np.arange(R_MAX + 1)
    return poisson.pmf(y, mu[..., None])


def inst_info(mu: np.ndarray, groups: np.ndarray | None = None) -> np.ndarray:
    """Instantaneous information (bits) per bin, mu of shape (n_stim, n_bins).

    With groups (a category per stimulus), p(y|c) is the mean of p(y|s) over the
    stimuli of the category and categories are weighted equally (claims header,
    code info_callsemantic.m)."""
    p = _pyx(mu)  # stim x bins x y
    if groups is not None:
        cats = np.unique(groups)
        p = np.stack([p[groups == c].mean(0) for c in cats])
    py = p.mean(0)
    with np.errstate(divide="ignore", invalid="ignore"):
        hy = -np.nansum(np.where(py > 0, py * np.log2(py), 0), -1)
        hys = -np.nansum(np.where(p > 0, p * np.log2(p), 0), -1).mean(0)
    return hy - hys


def cum_info_mc(mu: np.ndarray, n_samples: int, seed: int,
                groups: np.ndarray | None = None) -> np.ndarray:
    """Cumulative information (bits) from bin 1 to each bin, by Monte Carlo with
    importance sampling (paper, Methods, The cumulative information): samples
    are drawn from the proposal q, the product over bins of the marginal p(y_t),
    and the entropy of the response is the mean of -log2 p(y) weighted by p/q.
    The conditional entropy is exact, as bins are independent given the stimulus
    (or given the category, whose p(y|c) is then the mixture over its stimuli,
    computed by summing over stimuli).

    The uniform draws come from a generator seeded with `seed`, so that the
    jackknife replicates, called with the same seed, use common random numbers
    (an assumption: the paper does not say how the replicates are sampled, and
    independent draws multiply the Monte Carlo noise by about Ntrials in the
    bias-corrected value)."""
    rng = np.random.default_rng(seed)
    n_stim, T = mu.shape
    p = _pyx(mu)  # s, t, y
    if groups is None:
        groups = np.arange(n_stim)
    cats = np.unique(groups)
    pm = p.mean(0)  # marginal per bin (t, y)
    cdf = np.cumsum(pm, -1)
    u = rng.random((n_samples, T))
    ys = np.minimum((u[..., None] > cdf[None]).sum(-1), R_MAX)  # n x T
    logq = np.cumsum(np.log(pm[np.arange(T), ys]), 1)  # n x T
    lps = np.log(np.maximum(p[:, np.arange(T), ys], 1e-300))  # s x n x T
    cl = np.cumsum(lps, -1)  # s x n x T
    lp = np.logaddexp.reduce(cl, 0) - np.log(n_stim)  # log p(y_1..t)
    w = np.exp(lp - logq)
    hy = -(w * lp).mean(0) / np.log(2)
    # conditional entropy H(Y_1..t | C), with C the category (stimulus by default)
    hyc = np.zeros(T)
    for c in cats:
        idx = np.flatnonzero(groups == c)
        lc = np.logaddexp.reduce(cl[idx], 0) - np.log(idx.size)  # log p(y|c)
        hyc += -(w * np.exp(lc - lp) * lc).mean(0) / np.log(2) / cats.size
    return hy - hyc


# ---------------------------------------------------------------------------
# Spike-count measures (claims s2-spike-counts, fig2cd-fano-factor,
# fig2b-noise-correlations, s1-temporal-resolution); shown in the notebook as
# variants only, as the claims rest on the 404 units of units-404.
# ---------------------------------------------------------------------------
N_BINS = 60
BIN_S = 0.010


def counts(u: dict) -> list[np.ndarray]:
    """Per call stimulus, the trial x bin spike counts in the 60 bins of Methods B."""
    edges = np.arange(N_BINS + 1) * BIN_S
    return [np.stack([np.histogram(t, edges)[0] for t in s["trials"]]) for s in call_stims(u)]


def fano(cs: list[np.ndarray], zero_as_one: bool = True) -> float:
    """Time-averaged Fano factor: per bin and stimulus the variance (ddof 1, as
    MATLAB var) over the mean of the trial counts, averaged over stimuli, then
    over the 60 bins (claims, fig2cd-fano-factor). With zero_as_one the ratio is
    1 where variance equals mean, which covers bins with no spike (code,
    PoissonGaussianNeuralResponses.m, reading a); otherwise such stimuli are
    left out of the bin's average (reading b)."""
    m = np.stack([c.mean(0) for c in cs])
    v = np.stack([c.var(0, ddof=1) for c in cs])
    with np.errstate(divide="ignore", invalid="ignore"):
        ff = v / m
    if zero_as_one:
        ff[v == m] = 1.0
    return float(np.nanmean(np.nanmean(ff, 0)))


def noise_corr(cs: list[np.ndarray]) -> float:
    """Pearson correlation over trials of the counts in successive bins for the
    same stimulus, averaged across pairs of bins and stimuli (claims,
    fig2b-noise-correlations; paper, Methods, Testing the poisson assumptions).
    Pairs where a bin has no variance are left out (a standard choice)."""
    vals = []
    for c in cs:
        a, b = c[:, :-1], c[:, 1:]
        a = a - a.mean(0)
        b = b - b.mean(0)
        den = np.sqrt((a ** 2).sum(0) * (b ** 2).sum(0))
        with np.errstate(divide="ignore", invalid="ignore"):
            r = (a * b).sum(0) / den
        vals.append(r[den > 0])
    v = np.concatenate(vals)
    return float(v.mean()) if v.size else np.nan


def stim_corr(cs: list[np.ndarray]) -> tuple[float, float]:
    """Stimulus correlation of consecutive bins: (i) over stimuli, the Pearson
    correlation of the mean counts at bins t and t+1, averaged over bin pairs;
    (ii) within each stimulus, the correlation over bins of the mean count at t
    and t+1, averaged over stimuli (claims, fig2b-noise-correlations, both
    readings)."""
    m = np.stack([c.mean(0) for c in cs])  # stim x bins
    a, b = m[:, :-1] - m[:, :-1].mean(0), m[:, 1:] - m[:, 1:].mean(0)
    den = np.sqrt((a ** 2).sum(0) * (b ** 2).sum(0))
    with np.errstate(divide="ignore", invalid="ignore"):
        r1 = (a * b).sum(0) / den
    r2 = []
    for row in m:
        if row[:-1].std() > 0 and row[1:].std() > 0:
            r2.append(np.corrcoef(row[:-1], row[1:])[0, 1])
    return float(np.nanmean(r1[den > 0])), float(np.mean(r2)) if r2 else np.nan


def coherence_fraction(u: dict, f_max: float = 50.0) -> float:
    """Fraction of I_AR below f_max from the coherence stored in class_info:
    I_AR = -integral of log2(1 - coherence) over frequency (claims,
    s1-temporal-resolution; paper, S1 Fig legend). The stored curve integrates
    to the stored I_AR (checked in the notebook)."""
    g = [k for k in u["class_info"] if k.startswith("Call")][0]
    f, c = u["class_info"][g]["f"], u["class_info"][g]["c"]
    d = -np.log2(1 - np.clip(c, 0, 1 - 1e-12))
    return float(d[f <= f_max].sum() / d.sum())
