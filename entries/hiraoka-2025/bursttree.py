"""Bursty trains, merging numbers and power-law fits for Hiraoka & Jo (2025) on DANDI:000044.

Paper: T. Hiraoka and H.-H. Jo, "Hierarchical organization of bursty trains in event
sequences", doi:10.1063/5.0296506 (text read: the arXiv preprint body under paper/).
Claims: claims/hiraoka-2025.yaml. Where a parameter comes from is said beside it:

- "Methods" means Section II of the paper, as the claims file's opening comment gives it.
- O1 to O4 are the open details named in the claims file's opening comment.
- "Assumption" marks a choice this attempt made where neither source fixes it.
- "Standard choice" marks a detail that cannot change an outcome.

Data are streamed from the DANDI archive at the pinned version (DANDI_VERSION); nothing is
written to disk.
"""
from __future__ import annotations

import warnings

import h5py
import numpy as np
import remfile
import requests

DANDISET = "000044"
# The version the paper cites (ref. 39: https://dandiarchive.org/dandiset/000044/0.210812.1516).
DANDI_VERSION = "0.210812.1516"
# The latest published version, read only to show how it differs from the cited one.
LATEST_VERSION = "0.261106.0236"
API = "https://api.dandiarchive.org/api"

# Methods: relevant timescales are those with max burst size >= 100 and >= 100 bursts.
MIN_MAX_BURST = 100
MIN_BURSTS = 100
# Claims file, O3: a power law is supported when R > 0 and p < 0.05 (Figure 2 legend).
P_SUPPORT = 0.05
# Claims file, O4: grid (a) geometric with ratio 1.82, grid (b) log10 step 0.052,
# both from the lower end of the relevant range.
GRIDS = {"a": np.log10(1.82), "b": 0.052}
# Figure 2 legend: merging-number pairs delta = r * delta' for the neuron.
NEURON_RATIOS = (3.3, 5.9, 11.0)
# Claims file, O3: the four fit readings (xmin by KS or xmin = 1; discrete or continuous).
# Assumption, the range of the exponent (raised by the round-1 verifier). The locked release of
# powerlaw, 2.0.0, bounds the power-law alpha to [0, 3] by default (Power_Law.DEFAULT_PARAMETER_RANGES),
# so no fit can exceed 3, and its find_xmin discards every candidate xmin whose fit reaches the
# bound. The estimator the paper cites (Clauset et al., ref. 36, Section 3) has no upper bound,
# and neither had the package as its paper describes it (Alstott et al., ref. 37; releases 1.x
# require only alpha > 1). The paper gives no version. Adopted: alpha in [1, inf), the method as
# cited. The release's default cap is run as a variant, the same readings with suffix "_cap3".
ALPHA_RANGES = {"": {"alpha": [1, None]}, "_cap3": None}
_BASE_READINGS = {
    "ks_discrete": dict(xmin=None, discrete=True),
    "ks_continuous": dict(xmin=None, discrete=False),
    "x1_discrete": dict(xmin=1, discrete=True),
    "x1_continuous": dict(xmin=1, discrete=False),
}
READINGS = {name + sfx: dict(kw, parameter_ranges=pr)
            for sfx, pr in ALPHA_RANGES.items() for name, kw in _BASE_READINGS.items()}
ADOPTED_READINGS = tuple(_BASE_READINGS)                       # unbounded exponent
CAPPED_READINGS = tuple(r + "_cap3" for r in _BASE_READINGS)    # powerlaw 2.0.0 default, a variant
CAP = 3.0


# ---------------------------------------------------------------- archive access
def list_assets(version: str = DANDI_VERSION) -> list[dict]:
    """Assets of the dandiset at a version: path, size, asset id and S3 URL."""
    url = f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=200"
    out = []
    while url:
        page = requests.get(url, timeout=60).json()
        for a in page["results"]:
            meta = requests.get(
                f"{API}/dandisets/{DANDISET}/versions/{version}/assets/{a['asset_id']}/", timeout=60
            ).json()
            s3 = [u for u in meta["contentUrl"] if "s3" in u][0]
            out.append(dict(path=a["path"], size=a["size"], asset_id=a["asset_id"], url=s3))
        url = page.get("next")
    return sorted(out, key=lambda a: a["path"])


def open_nwb(url: str) -> h5py.File:
    """Open a streamed NWB file with h5py (read only)."""
    return h5py.File(remfile.File(url), "r")


def _str(a):
    return np.array([x.decode() if isinstance(x, bytes) else str(x) for x in a])


def load_units(f: h5py.File) -> dict:
    """The units table: ids, every column, and spike times per unit (seconds, as stored)."""
    u = f["units"]
    idx = u["spike_times_index"][:]
    st = u["spike_times"][:]
    start = np.r_[0, idx[:-1]]
    out = {"id": u["id"][:], "spikes": [st[a:b] for a, b in zip(start, idx)]}
    for k in u.keys():
        if k in ("id", "spike_times", "spike_times_index") or k.endswith("_index"):
            continue
        d = u[k]
        if d.ndim == 1 and d.shape[0] == len(idx):
            v = d[:]
            out[k] = _str(v) if v.dtype.kind in "OSU" else v
    return out


def load_epochs(f: h5py.File) -> dict:
    e = f["intervals/epochs"]
    return dict(label=_str(e["label"][:]), start=e["start_time"][:], stop=e["stop_time"][:])


# ---------------------------------------------------------------- bursts (Methods)
def iets(times_ms: np.ndarray) -> np.ndarray:
    """Interevent times tau_i = t_(i+1) - t_i (Methods)."""
    return np.diff(np.sort(times_ms))


def burst_sizes(tau: np.ndarray, delta: float) -> np.ndarray:
    """Sizes of the bursts at timescale delta: maximal runs whose IETs are all <= delta (Methods)."""
    cut = np.flatnonzero(tau > delta)
    edges = np.r_[0, cut + 1, len(tau) + 1]
    return np.diff(edges)


def merging_numbers(tau: np.ndarray, dprime: float, delta: float) -> np.ndarray:
    """Merging numbers k_j: bursts at delta' that make up the j-th burst at delta (Eqs. 2-3).

    Within a burst at delta, every IET in (delta', delta] separates two bursts at delta', so
    k_j = 1 + the number of such IETs inside burst j.
    """
    assert dprime < delta
    burst_of_iet = np.r_[0, np.cumsum(tau > delta)][:-1]
    inside = tau <= delta
    m = int((tau > delta).sum()) + 1
    k = 1 + np.bincount(burst_of_iet[inside], weights=(tau[inside] > dprime), minlength=m)
    return k.astype(np.int64)


def relevant_range(tau: np.ndarray) -> tuple[float, float]:
    """Relevant timescales (Methods), computed exactly from the IETs.

    Lower end: the smallest delta with max burst size >= 100, the smallest over all runs of
    100 consecutive events of their largest IET. Upper end: delta must stay below the 99th
    largest IET for m_delta >= 100; the returned bound is that IET (exclusive).
    """
    w = MIN_MAX_BURST - 1
    if len(tau) < max(w, MIN_BURSTS):
        return np.nan, np.nan
    lo = np.lib.stride_tricks.sliding_window_view(tau, w).max(axis=1).min()
    hi = np.sort(tau)[-(MIN_BURSTS - 1)]
    return float(lo), float(hi)


def grid(lo: float, hi: float, grid_name: str) -> np.ndarray:
    """Geometric grid of delta from the lower end of the relevant range (claims file, O4).

    Grid (a): ratio 1.82 from the lower end. Grid (b): log10 step "about 0.052" (O4), made
    exact by fitting a whole number of steps between the two ends of the range, as the
    Figure 2 legend says the values shown "span the entire range of relevant timescales";
    for the representative unit this gives 40 steps of 0.0514, of which every 5th point gives
    the delta' labels (55, 100, 180, 330, 590 ms) and every 8th the delta labels (55, 140,
    370, 940, 2400, 6300 ms). Points at or above the upper end are dropped (fewer than 100
    bursts, Methods).
    """
    if not np.isfinite(lo) or hi <= lo:
        return np.array([])
    span = np.log10(hi / lo)
    step = GRIDS[grid_name]
    if grid_name == "b":
        step = span / max(1, round(span / step))
    n = int(np.floor(span / step + 1e-9)) + 1
    g = lo * 10 ** (step * np.arange(n))
    return g[g < hi * (1 - 1e-12)]


def pairs_on_grid(g: np.ndarray, hi: float, ratios=NEURON_RATIOS) -> list[tuple[float, float, float]]:
    """(delta', delta, ratio) with delta' on the grid and delta = ratio * delta' inside the range."""
    return [(dp, r * dp, r) for r in ratios for dp in g if r * dp < hi]


# ---------------------------------------------------------------- fits (Methods, O3)
def fit(x: np.ndarray, reading: str) -> dict:
    """Maximum-likelihood power-law fit and likelihood-ratio test against an exponential.

    Uses the powerlaw package (Alstott et al., ref. 37 of the paper, implementing Clauset et al.,
    ref. 36): Fit(...) and distribution_compare('power_law', 'exponential'). The readings of the
    lower cutoff and of discreteness are those of the claims file, O3; the range of the exponent
    is unbounded, or capped at 3 in the "_cap3" variants (see READINGS). `at_cap` marks a capped
    fit within 0.01 of the cap.
    """
    import powerlaw

    x = np.asarray(x, dtype=float)
    kw = READINGS[reading]
    out = dict(reading=reading, n=len(x), xmax=float(x.max()) if len(x) else np.nan)
    if len(x) < 2 or np.unique(x).size < 2:
        out.update(alpha=np.nan, in_range=False, at_cap=False, sigma=np.nan, xmin=np.nan, n_tail=0, R=np.nan,
                   p=np.nan, supported=False)
        return out
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        F = powerlaw.Fit(x, verbose=False, **kw)
        try:
            R, p = F.distribution_compare("power_law", "exponential")
        except Exception:  # a failed test is counted as not supported and reported
            R, p = np.nan, np.nan
    a_ = float(F.power_law.alpha)
    out.update(
        alpha=a_,
        in_range=bool(F.power_law.in_range()),
        at_cap=bool(kw["parameter_ranges"] is None and a_ > CAP - 0.01),
        sigma=float(F.power_law.sigma),
        xmin=float(F.xmin),
        n_tail=int((x >= F.xmin).sum()),
        R=float(R),
        p=float(p),
        supported=bool(np.isfinite(R) and R > 0 and p < P_SUPPORT),
    )
    return out


def analyse_sequence(times_ms, grid_name="b", ratios=NEURON_RATIOS, readings=tuple(READINGS),
                     extra_pairs=()) -> dict:
    """Burst-size fits on the grid and merging-number fits on the pairs, under each reading.

    Returns relevant range, grid, a list of burst rows (delta, reading, fit) and of pair rows
    (delta', delta, ratio, reading, fit). Beta is also fitted at each pair's delta, which need
    not be on the grid. `extra_pairs` adds fixed (delta', delta, ratio) pairs, such as the
    labels of Figure 2.
    """
    tau = iets(np.asarray(times_ms, dtype=float))
    lo, hi = relevant_range(tau)
    g = grid(lo, hi, grid_name)
    prs = pairs_on_grid(g, hi, ratios) + list(extra_pairs)
    deltas = sorted(set(np.round(np.r_[g, [p[0] for p in prs], [p[1] for p in prs]], 9)))
    on_grid = set(np.round(g, 9))
    bursts, pairs = [], []
    for d in deltas:
        b = burst_sizes(tau, d)
        for r in readings:
            row = fit(b, r)
            row.update(delta=d, on_grid=d in on_grid, m=len(b), bmax=int(b.max()), bmean=float(b.mean()))
            bursts.append(row)
    for dp, d, ratio in prs:
        k = merging_numbers(tau, dp, d)
        for r in readings:
            row = fit(k, r)
            row.update(dprime=dp, delta=d, ratio=ratio, m=len(k), kmean=float(k.mean()),
                       extra=(dp, d, ratio) in list(extra_pairs))
            pairs.append(row)
    return dict(n=len(tau) + 1, tau_min=float(tau.min()), tau_max=float(tau.max()), lo=lo, hi=hi,
                grid=g, bursts=bursts, pairs=pairs)


def unit_pattern(times_ms, grid_name, reading, ratios=NEURON_RATIOS) -> dict:
    """Claim fig2-other-neurons-similar: does one unit show the pattern under one reading?

    Pattern (criterion): power law supported for burst sizes at more than half of the unit's
    relevant timescales on the grid, and for merging numbers at more than half of its pairs.
    Units whose relevant range holds fewer than three grid points are not used.
    """
    tau = iets(np.asarray(times_ms, dtype=float))
    lo, hi = relevant_range(tau)
    g = grid(lo, hi, grid_name)
    out = dict(n=len(tau) + 1, lo=lo, hi=hi, n_grid=len(g))
    if len(g) < 3:
        out.update(used=False)
        return out
    bf = [fit(burst_sizes(tau, d), reading) for d in g]
    prs = pairs_on_grid(g, hi, ratios)
    kf = [fit(merging_numbers(tau, dp, d), reading) for dp, d, _ in prs]
    nb = sum(x["supported"] for x in bf)
    nk = sum(x["supported"] for x in kf)
    betas = [x["alpha"] for x in bf if np.isfinite(x["alpha"])]
    out.update(used=True, n_pairs=len(prs), b_supported=nb, k_supported=nk,
               n_at_cap=sum(x["at_cap"] for x in bf + kf), n_fits=len(bf) + len(kf),
               b_frac=nb / len(g), k_frac=nk / len(prs) if prs else np.nan,
               median_beta=float(np.median(betas)) if betas else np.nan,
               pattern=bool(nb > len(g) / 2 and len(prs) > 0 and nk > len(prs) / 2))
    return out


# ---------------------------------------------------------------- the model (Section IV)
def timescales(series: str, L: int, delta0=1.0, w=None) -> np.ndarray:
    """delta_l for l = 0..L: linear (Eq. 12), quadratic (Eq. 13) or exponential (Eq. 14).

    Section IV: delta_0 = 1, w = 100 for linear and quadratic, w = 2 for exponential.
    """
    l = np.arange(L + 1, dtype=float)
    if series == "linear":
        return delta0 + (100 if w is None else w) * l
    if series == "quadratic":
        return delta0 + (100 if w is None else w) * l ** 2
    if series == "exponential":
        return delta0 * (2 if w is None else w) ** l
    raise ValueError(series)


def _q_exact_zeta(gamma: float, kmax: int = 1 << 16) -> np.ndarray:
    """Eq. 9 applied to the zeta distribution of Eq. 15: q(kappa) = zeta(gamma, kappa+1) / zeta(gamma, kappa)
    (Hurwitz zeta), for kappa = 0..kmax (index 0 unused). A variant; Section IV uses Eq. 16."""
    from scipy.special import zeta

    k = np.arange(1, kmax + 2, dtype=float)
    z = zeta(gamma, k)
    return np.r_[np.nan, z[1:] / z[:-1]]


def simulate_incremental(n: int, series: str, gamma: float, rng: np.random.Generator,
                         memory: str = "eq16") -> np.ndarray:
    """Algorithm 2 (incremental), with uniform IETs on [delta_l, delta_(l+1)] (Eq. 10).

    memory="eq16": q(kappa) = (kappa/(kappa+1))^(gamma-1), Eq. 16, as Section IV uses.
    memory="eq9_zeta": q(kappa) from Eq. 9 applied exactly to the zeta distribution (Eq. 15),
    a variant. Returns n event times, t_1 = 0.
    """
    L = 400
    d = timescales(series, L)
    qx = _q_exact_zeta(gamma) if memory == "eq9_zeta" else None
    kappa = np.zeros(L, dtype=np.int64)  # 0 = not set
    t = np.empty(n)
    t[0] = 0.0
    i, l = 1, 0
    e = gamma - 1.0
    buf = rng.random(1 << 20)
    bi = 0
    while i < n:
        if bi >= len(buf) - 2:
            buf = rng.random(1 << 20)
            bi = 0
        if kappa[l] == 0:
            kappa[l] = 1
        r = buf[bi]; bi += 1
        kp = kappa[l]
        if qx is None:
            q = (kp / (kp + 1.0)) ** e
        elif kp < len(qx) - 1:
            q = qx[kp]
        else:
            q = (kp / (kp + 1.0)) ** e  # beyond the table the two agree to within 1e-9
        if r < q:
            u = buf[bi]; bi += 1
            t[i] = t[i - 1] + d[l] + (d[l + 1] - d[l]) * u
            i += 1
            kappa[l] = kp + 1
            l = 0
        else:
            kappa[l] = 1
            l += 1
    return t


def sample_merging(size: int, gamma: float, rng: np.random.Generator, dist: str = "zeta") -> np.ndarray:
    """Merging numbers k >= 1. dist="zeta": Eq. 15, as Section IV states for P(k).
    dist="eq16": the distribution whose memory function is Eq. 16, P(K >= k) = k^-(gamma-1),
    sampled as floor(U^(-1/(gamma-1))); a variant."""
    from scipy.stats import zipf

    if dist == "zeta":
        return zipf.rvs(gamma, size=size, random_state=rng)
    u = 1.0 - rng.random(size)  # in (0, 1]
    return np.floor(u ** (-1.0 / (gamma - 1.0))).astype(np.int64)


def simulate_decremental(n: int, series: str, gamma: float, rng: np.random.Generator,
                         dist: str = "zeta") -> np.ndarray:
    """Algorithm 1 (decremental), merging numbers from sample_merging, uniform IETs (Eq. 10)."""
    L = 400
    d = timescales(series, L)
    kappa = np.full(L, -1, dtype=np.int64)  # -1 = not set
    t = np.empty(n)
    t[0] = 0.0
    i, l = 1, 0
    ks = sample_merging(1 << 20, gamma, rng, dist)
    ki = 0
    us = rng.random(1 << 20)
    ui = 0
    while i < n:
        if kappa[l] <= 0:
            if ki >= len(ks):
                ks = sample_merging(1 << 20, gamma, rng, dist); ki = 0
            kappa[l] = ks[ki]; ki += 1
        elif kappa[l] == 1:
            kappa[l] = 0
            l += 1
        else:
            if ui >= len(us):
                us = rng.random(1 << 20); ui = 0
            t[i] = t[i - 1] + d[l] + (d[l + 1] - d[l]) * us[ui]; ui += 1
            i += 1
            kappa[l] -= 1
            l = 0
    return t


def unit_all_patterns(times_ms, readings=ADOPTED_READINGS, grids=tuple(GRIDS)) -> list[dict]:
    """unit_pattern under the given grids (O4) and fit readings (O3), for a worker pool."""
    out = []
    for g in grids:
        for r in readings:
            row = unit_pattern(times_ms, g, r)
            row.update(grid=g, reading=r)
            out.append(row)
    return out


def capped_patterns(times_ms) -> list[dict]:
    """The capped variant (powerlaw 2.0.0 default range) on grid (a) alone, for a worker pool."""
    return unit_all_patterns(times_ms, CAPPED_READINGS, ("a",))


def cdf_int(x: np.ndarray) -> np.ndarray:
    """Empirical CDF of positive integers at 0, 1, ..., max(x)."""
    c = np.bincount(x).cumsum()
    return c / c[-1]


def ks_d_int(c1: np.ndarray, c2: np.ndarray) -> float:
    """Two-sample KS statistic from two integer CDFs (cdf_int), padded with 1."""
    n = max(len(c1), len(c2))
    return float(np.abs(np.pad(c1, (0, n - len(c1)), constant_values=1) - np.pad(c2, (0, n - len(c2)), constant_values=1)).max())


def ccdf_at(x: np.ndarray, at: np.ndarray) -> np.ndarray:
    """P(X >= a) for each a in `at` (complementary cumulative distribution)."""
    xs = np.sort(x)
    return 1.0 - np.searchsorted(xs, at, side="left") / len(xs)


def spike_counts(times_s: np.ndarray, edges: np.ndarray) -> np.ndarray:
    return np.histogram(times_s, edges)[0]
