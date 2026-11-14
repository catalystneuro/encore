"""Loading and measures for Elie & Theunissen (2019) on CRCNS aa-4.

Data. CRCNS aa-4 is unversioned; the files are read from the public S3 bucket
crcnsarchive under aa-4/live/data/, one tar.gz per bird. Each tar.gz is read as
a stream (tarfile mode "r|gz" over fsspec), each h5 member is opened in memory
with h5py, reduced to what the analysis needs, and dropped. Nothing is written
to disk.

Parameters and where they come from (claims file header, Methods R, B, P):
- Window 0 to 600 ms after stimulus onset, 60 bins of 10 ms (Methods B; paper,
  Methods, "Here, we analyzed the neural response in the first 600ms").
- Call stimuli: in the unit's call protocol (the groups Call, Call1 to Call3,
  Call1b, Call1c), stim_type "call" with call types Ag (Wsst, Ws), Be, DC, Di, LT,
  Ne, Te, Th, and the songs of the vocalization bank (So). Whines (Wh), noise and
  the search songs are dropped (claims header, selVoc.m; paper, S4 Fig legend).
  The other protocols (Sel1 to Sel7, Mask1, STRF1) are read but not used as call
  stimuli; the notebook shows how many call and song stimuli each holds.
- Spike snippets: each site and protocol has a file "<site>... <protocol>
  waves.f32" of float32 snippets of 18 samples, indexed (from 1) by the
  spike_ids of the h5 files (CRCNSCode/h5_plot_one_spike.m in the archive's
  CRCNSCode.tar.gz). The single-unit SNR is "the difference between the maximum
  and the minimum of the average snippet" over "the standard deviation of this
  measure across all snippets", with single units at SNR > 5 (paper, Methods,
  Neurophysiological recordings; data description). Reading A takes the SD of
  each snippet's maximum minus minimum; reading B the SD, across snippets, of the
  snippet's value at the sample of the average's maximum minus its value at the
  sample of the average's minimum. Both are computed on all spikes of the unit's
  call protocol.
"""
from __future__ import annotations

import io
import re
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


def _paths(g: h5py.Group) -> list[str]:
    """Paths of the datasets under a group, with their shapes."""
    out = []
    g.visititems(lambda n, o: out.append(f"{n} {o.shape}") if isinstance(o, h5py.Dataset) else None)
    return out


def read_unit(h: h5py.File, name: str, bird: str) -> dict:
    """Reduce one unit's h5 file to its attributes, its stored coherence
    (class_info), the dataset paths of class_info and extra_info, and, for single
    units, the spike times of each trial of its call and song stimuli in KEEP, in
    seconds from stimulus onset, as stored. For spike-sorted files (_ss) the
    spike_ids of every protocol are kept in "ids" (all spikes of all trials), for
    the snippet SNR; stream_bird drops them once the SNR is computed."""
    u = {"bird": bird, "file": name.split("/")[-1]}
    for k, v in h.attrs.items():
        u[k] = _s(v)
    u["groups"] = list(h.keys())
    # spikes are kept for single units only; other files keep their metadata
    single = is_single(u)
    sorted_file = "_ss" in u["file"]
    stims = []
    ids_all = {}
    n_unsorted = 0  # trials whose stored spike times are not in increasing order
    for g in h.keys():
        if g in ("class_info", "extra_info"):
            continue
        if sorted_file:
            ids_g = []
            for sg in h[g].values():
                for tg in sg.values():
                    x = np.asarray(tg["spike_ids"][()]).ravel()
                    ids_g.append(x[x != -999].astype(np.int64))
            ids_all[g] = np.concatenate(ids_g) if ids_g else np.empty(0, np.int64)
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
    u["class_info_paths"] = _paths(h["class_info"]) if "class_info" in h else []
    u["extra_info_paths"] = _paths(h["extra_info"]) if "extra_info" in h else []
    u["ids"] = ids_all
    return u


def f32_key(name: str) -> tuple[str, str]:
    """(site, protocol) of a snippet file, e.g. "Site2_depthL2000R1600_Call2
    waves.f32" or "Site3 depth 4600 Call waves.f32" -> ("Site2", "Call2")."""
    stem = name.split("/")[-1].replace(" waves.f32", "")
    return re.match(r"Site\d+", stem).group(0), re.split(r"[ _-]", stem)[-1]


def snippet_snr(snips: np.ndarray) -> tuple[float, float]:
    """SNR of a unit's snippets (n x 18), readings A and B (module docstring)."""
    m = snips.mean(0)
    sig = m.max() - m.min()
    a = sig / (snips.max(1) - snips.min(1)).std(ddof=1)
    b = sig / (snips[:, m.argmax()] - snips[:, m.argmin()]).std(ddof=1)
    return float(a), float(b)


def unit_snr(u: dict, f32: dict) -> dict:
    """Snippet SNR of a spike-sorted unit on its call protocol: the Call group
    with a snippet file and the most spikes. When two files share a site and
    protocol, the largest that holds every spike_id is used."""
    best = None
    for g, ids in u["ids"].items():
        if not g.startswith("Call") or ids.size < 2:
            continue
        cands = [(a.shape[0], n) for n, a in f32.items() if f32_key(n) == (u.get("site"), g)]
        cands = [c for c in cands if c[0] >= ids.max()]
        if cands and (best is None or ids.size > best[1].size):
            best = (max(cands)[1], ids, len(cands))
    if best is None:
        return {"snr_a": np.nan, "snr_b": np.nan, "snr_file": None, "snr_n": 0, "snr_n_files": 0}
    a, b = snippet_snr(f32[best[0]][best[1] - 1])
    return {"snr_a": a, "snr_b": b, "snr_file": best[0].split("/")[-1], "snr_n": int(best[1].size),
            "snr_n_files": best[2]}


def stream_bird(bird: str, block_size: int = 2**23) -> list[dict]:
    """Stream one bird's tar.gz and return the reduced units of all its h5 files.
    The snippet files (.f32) come between the h5 files in the archive, so they
    are held in memory (float32, at most 1.4 GB per bird) until the end of the
    bird, when the SNR of each spike-sorted unit is computed and they and the
    spike_ids are dropped. Each unit gets "f32_files", the bird's snippet files
    and their numbers of snippets."""
    units = []
    f32 = {}
    with fsspec.open(BASE + bird + ".tar.gz", block_size=block_size).open() as f:
        with tarfile.open(fileobj=f, mode="r|gz") as tar:
            for m in tar:
                if not m.isfile():
                    continue
                if m.name.endswith(".h5"):
                    b = tar.extractfile(m).read()
                    with h5py.File(io.BytesIO(b), "r") as h:
                        units.append(read_unit(h, m.name, bird))
                elif m.name.endswith(".f32"):
                    f32[m.name] = np.frombuffer(tar.extractfile(m).read(), np.float32).reshape(-1, 18)
    files = {n.split("/")[-1]: a.shape[0] for n, a in f32.items()}
    for u in units:
        if u["ids"]:
            u.update(unit_snr(u, f32))
        u["f32_files"] = files
        del u["ids"]
    return units


def load_all(birds=BIRDS, workers: int = 3) -> list[dict]:
    """All units of all birds, the birds streamed in parallel processes. Three
    workers, as each holds up to 2.4 GB while it streams a large bird (measured
    on GreBlu9508M)."""
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


def call_stims(u: dict, protocol: str = "Call") -> list[dict]:
    """The call stimuli of a unit in the groups whose name starts with
    `protocol` (the call protocol by default; "" for every group), with their
    call type in "ct"."""
    out = []
    for s in u["stims"]:
        ct = call_type(s)
        if ct is not None and s["trials"] is not None and s["group"].startswith(protocol):
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
    The conditional entropy uses the same samples, weighted by p(y|c)/q.

    With groups (a category per stimulus), p(y_1..t|c) is the mixture over the
    stimuli of the category of the products over bins, and categories are
    weighted equally in p(y) and in the conditional entropy, as in inst_info
    (code info_model_Calculus_wrapper2.m). Without groups each stimulus is its
    own category.

    One set of draws serves every bin. The uniform draws come from a generator
    seeded with `seed`, so that jackknife replicates called with the same seed
    use common random numbers, as the paper's code does
    (cumulative_info_poisson_model_calculus_MCJK.m draws the samples once from
    the full data and evaluates every jackknife set on them)."""
    rng = np.random.default_rng(seed)
    n_stim, T = mu.shape
    p = _pyx(mu)  # s, t, y
    if groups is None:
        groups = np.arange(n_stim)
    cats = np.unique(groups)
    pm = np.stack([p[groups == c].mean(0) for c in cats]).mean(0)  # marginal per bin (t, y)
    cdf = np.cumsum(pm, -1)
    u = rng.random((n_samples, T))
    ys = np.minimum((u[..., None] > cdf[None]).sum(-1), R_MAX)  # n x T
    logq = np.cumsum(np.log(pm[np.arange(T), ys]), 1)  # n x T
    lps = np.log(np.maximum(p[:, np.arange(T), ys], 1e-300))  # s x n x T
    cl = np.cumsum(lps, -1)  # s x n x T
    lc = np.stack([np.logaddexp.reduce(cl[groups == c], 0) - np.log((groups == c).sum()) for c in cats])
    lp = np.logaddexp.reduce(lc, 0) - np.log(cats.size)  # log p(y_1..t)
    w = np.exp(lp - logq)
    hy = -(w * lp).mean(0) / np.log(2)
    hyc = -(np.exp(lc - logq[None]) * lc).mean((0, 1)) / np.log(2)
    return hy - hyc


def cum_info_exact(mu: np.ndarray, groups: np.ndarray | None = None) -> np.ndarray:
    """Cumulative information by enumerating every response sequence, for a few
    bins only (21**T sequences); the check of cum_info_mc. Categories as in
    cum_info_mc."""
    n_stim, T = mu.shape
    p = _pyx(mu)
    if groups is None:
        groups = np.arange(n_stim)
    cats = np.unique(groups)
    out = []
    for t in range(1, T + 1):
        ps = np.ones((n_stim, 1))
        for k in range(t):
            ps = (ps[:, :, None] * p[:, k][:, None, :]).reshape(n_stim, -1)  # s x sequences
        pc = np.stack([ps[groups == c].mean(0) for c in cats])
        py = pc.mean(0)
        with np.errstate(divide="ignore", invalid="ignore"):
            hy = -np.sum(np.where(py > 0, py * np.log2(py), 0))
            hyc = -np.sum(np.where(pc > 0, pc * np.log2(pc), 0)) / cats.size
        out.append(hy - hyc)
    return np.array(out)


def cum_info_mcjk(mu: np.ndarray, mu_jk: np.ndarray, n_trials: int, n_boot: int, seed: int,
                  chunk: int = 100_000, max_samples: int = 5_000_000, conv: float = 0.2,
                  stop: float = 0.6) -> dict:
    """Bias-corrected cumulative information for stimuli with the paper's
    procedure (Methods, The cumulative information, and Bias correction; code
    cumulative_info_poisson_model_MCJK_wrapper.m,
    cumulative_info_poisson_model_calculus_MCJK.m and the tutorial
    Tutorial_TimeVarying_Information.mlx, all at the pinned commit):

    - mu (stimulus x bin) is the full-data Poisson mean, mu_jk (set x stimulus x
      bin) the n_trials jackknife sets. Each of the n_boot bootstraps pairs the
      jackknife sets of the stimuli at random (a permutation of the sets per
      stimulus, as the tutorial's SetIndices_JK); the paper gives NB = 20.
    - For each end bin t from 2 on, a new Monte Carlo estimate over bins 1..t:
      chunks of `chunk` samples from the proposal of the full data, the
      jackknife sets evaluated on the same samples; entropies are averaged over
      chunks. After each chunk the pseudo-values N I - (N-1) I_jk give the
      bias-corrected value (their mean) and the error (the square root of the
      mean over bootstraps of their variance over sets, ddof 1). Sampling stops
      when the error is below `conv` bits or at `max_samples`.
    - The bins stop after the first one whose error is above `stop` bits (3 x
      0.2, the wrapper's rule; the paper's 0.6-bit rule).
    - Bin 1 is not estimated here; the tutorial sets it to the instantaneous
      value.
    Returns per bin (nan where not computed) "bc", "raw", "err", "n_samples",
    and "stopped_at" (the last bin computed, 1-based)."""
    rng = np.random.default_rng(seed)
    K, S, T = mu_jk.shape
    perm = np.stack([np.stack([rng.permutation(K) for _ in range(S)], 1) for _ in range(n_boot)])  # b, jk, s
    P = _pyx(mu)
    P = P / P.sum(-1, keepdims=True)  # ScaleY in the code
    PJ = _pyx(mu_jk)
    PJ = PJ / PJ.sum(-1, keepdims=True)
    lP = np.log(np.maximum(P, 1e-300))
    lPJ = np.log(np.maximum(PJ, 1e-300))
    pm = P.mean(0)  # proposal marginals from the full data (t, y)
    cdf = np.cumsum(pm / pm.sum(-1, keepdims=True), -1)
    out = {k: np.full(T, np.nan) for k in ("bc", "raw", "err", "n_samples")}
    sidx = np.arange(S)[None, :]
    ln2 = np.log(2)
    stopped = 1
    for t in range(2, T + 1):
        n_tot, err = 0, conv + 1
        acc = None
        while err > conv and n_tot < max_samples:
            u = rng.random((chunk, t))
            ys = np.minimum((u[..., None] > cdf[None, :t]).sum(-1), R_MAX)  # n x t
            lq = np.log(pm[np.arange(t), ys]).sum(1)  # n
            cl = np.zeros((S, chunk))
            clj = np.zeros((K, S, chunk))
            for k in range(t):
                cl += lP[:, k, ys[:, k]]
                clj += lPJ[:, :, k, ys[:, k]]

            def ent(c):  # c: (..., S, n) log p(y|s) -> H(Y), H(Y|S) for this chunk
                lp = np.logaddexp.reduce(c, -2) - np.log(S)
                hy = -(np.exp(lp - lq) * lp).mean(-1) / ln2
                hys = -(np.exp(c - lq) * c).mean((-1, -2)) / ln2
                return hy, hys

            hy, hys = ent(cl)
            cb = clj[perm, sidx[None]]  # b, jk, s, n
            hyj, hysj = ent(cb)
            new = np.array([hy, hys]), np.stack([hyj, hysj])
            acc = new if acc is None else ((acc[0] * n_tot + new[0] * chunk) / (n_tot + chunk),
                                           (acc[1] * n_tot + new[1] * chunk) / (n_tot + chunk))
            n_tot += chunk
            i_full = acc[0][0] - acc[0][1]
            i_jk = acc[1][0] - acc[1][1]  # b, jk
            pseudo = n_trials * i_full - (n_trials - 1) * i_jk
            err = float(np.sqrt(pseudo.var(1, ddof=1).mean()))
        out["bc"][t - 1], out["raw"][t - 1] = pseudo.mean(), i_full
        out["err"][t - 1], out["n_samples"][t - 1] = err, n_tot
        stopped = t
        if err > stop:
            break
    out["stopped_at"] = stopped
    return out


def inst_info_bootjk(mu: np.ndarray, mu_jk: np.ndarray, n_trials: int, n_boot: int, seed: int):
    """Bias-corrected instantaneous information and its error as the tutorial
    computes them (Info_bcorr, Info_err): per bootstrap a random pairing of the
    jackknife sets across stimuli, pseudo-values N I - (N-1) I_jk, the mean over
    sets and bootstraps, and the square root of the mean over bootstraps of their
    variance over sets (ddof 1)."""
    rng = np.random.default_rng(seed)
    K, S, T = mu_jk.shape
    full = inst_info(mu)
    bc, var = [], []
    for _ in range(n_boot):
        perm = np.stack([rng.permutation(K) for _ in range(S)], 1)  # jk, s
        ij = np.array([inst_info(mu_jk[perm[k], np.arange(S)]) for k in range(K)])
        ps = n_trials * full - (n_trials - 1) * ij
        bc.append(ps.mean(0))
        var.append(ps.var(0, ddof=1))
    return np.mean(bc, 0), np.sqrt(np.mean(var, 0))


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
