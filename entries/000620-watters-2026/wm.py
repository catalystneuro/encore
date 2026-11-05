"""Loading and measures for dandiset 000620 (Watters, Gabel, Tenenbaum & Jazayeri 2026).

Where each parameter comes from is given next to it, as one of
- the claims file (claims/000620/10.64898-2026.01.27.702062.yaml), definitions T1 to T8,
  which cite the paper or its code,
- a passage of the paper (preprint v1, doi:10.64898/2026.01.27.702062), cited by section,
- the paper's code, https://github.com/jazlab/multi_object_memory_2025 at commit
  6e4b333b78cd4461e6373a42378535e8fd392cdb, cited by file,
- a standard choice, for a detail that cannot change a result.

Data are streamed from the DANDI archive with remfile and h5py; nothing is written to disk.
"""

import ast
import json
import urllib.request

import h5py
import numpy as np
import pandas as pd
import remfile

DANDISET = "000620"
# Most recent published version; the paper cites no version (notebook header).
VERSION = "0.261019.2000"
API = "https://api.dandiarchive.org/api"

# Arena coordinates: positions are in units of arena width (24 degrees), centre (0.5, 0.5)
# (trials table column descriptions; Methods, Fixation phase).
ARENA_DEG = 24.0
RADIUS = 0.35  # 8.4 degrees eccentricity (Methods, Stimulus phase; load_triangle_data.py)
TRIANGLE_THETAS = np.array([0.0, 2 * np.pi / 3, 4 * np.pi / 3])  # right, top-left, bottom-left
TRIANGLE_XY = np.stack([RADIUS * np.cos(TRIANGLE_THETAS), RADIUS * np.sin(TRIANGLE_THETAS)], 1)
# T2: correctness radius. Methods (Feedback phase) 2.4 degrees = 0.1 arena widths;
# code (load_triangle_data.py, load_ring_data.py) 0.2 arena widths.
RADII = {"methods_2.4deg": 0.1, "code_4.8deg": 0.2}
IDS = ["a", "b", "c"]  # apple, blueberry, orange (Methods, Stimulus phase; code constants.py)
MIN_RATE_HZ = 1.0  # T5, Methods, Data Processing ("less than 1Hz" excluded; code "> 1")
MIN_STABLE_TRIALS = 500  # T5, Methods, Data Processing


def _get_json(url):
    with urllib.request.urlopen(url) as r:
        return json.loads(r.read())


def list_assets():
    """All assets of the pinned version, as a DataFrame (path, size, asset_id)."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=400"
    rows = []
    while url:
        page = _get_json(url)
        rows += page["results"]
        url = page["next"]
    df = pd.DataFrame(rows)[["path", "size", "asset_id"]]
    parts = df.path.str.extract(r"sub-(\w+)/sub-\w+_ses-([\d-]+)_(.+)\.nwb")
    df["subject"], df["session"], df["kind"] = parts[0], parts[1], parts[2]
    return df


def s3_url(asset_id):
    meta = _get_json(f"{API}/assets/{asset_id}/")
    return [u for u in meta["contentUrl"] if "s3" in u][0]


def open_h5(asset_id):
    return h5py.File(remfile.File(s3_url(asset_id)), "r")


def _decode(arr):
    return [ast.literal_eval(x.decode() if isinstance(x, bytes) else x)
            for x in arr]


def load_trials(asset_id):
    """Trials table of a behavior+task file, with derived columns.

    completed: not broken fixation and finite response time (T1; run_cache_data.py).
    reaction_time: response_time minus phase_cue_time (T3; load_triangle_data.py).
    """
    with open_h5(asset_id) as h:
        t = h["intervals/trials"]
        cols = ["broke_fixation", "phase_stimulus_time", "phase_delay_time", "phase_cue_time",
                "phase_response_time", "phase_reveal_time", "response_time",
                "closed_loop_response_time", "reward_time", "start_time", "stop_time"]
        df = pd.DataFrame({c: t[c][:] for c in cols})
        resp = t["response_position"][:]
        clr = t["closed_loop_response_position"][:]
        pos = _decode(t["stimulus_object_positions"][:])
        ids = _decode(t["stimulus_object_identities"][:])
        targ = [ast.literal_eval(x.decode().replace("true", "True").replace("false", "False"))
                for x in t["stimulus_object_target"][:]]
        blanks = t["delay_object_blanks"][:]
        vel = _decode(t["stimulus_object_velocities"][:])
    df["delay_object_blanks"] = blanks
    df["max_speed"] = [np.abs(np.array(v)).max() for v in vel]
    df["n_obj"] = [len(p) for p in pos]
    df["completed"] = ~df.broke_fixation & np.isfinite(df.response_time)
    df["reaction_time"] = df.response_time - df.phase_cue_time
    df["resp_x"], df["resp_y"] = resp[:, 0] - 0.5, resp[:, 1] - 0.5
    df["cl_x"], df["cl_y"] = clr[:, 0] - 0.5, clr[:, 1] - 0.5
    df["rewarded"] = np.isfinite(df.reward_time)
    for i in range(3):
        df[f"x{i}"] = [p[i][0] - 0.5 if len(p) > i else np.nan for p in pos]
        df[f"y{i}"] = [p[i][1] - 0.5 if len(p) > i else np.nan for p in pos]
        df[f"id{i}"] = [d[i] if len(d) > i else None for d in ids]
    df["target"] = [int(np.argmax(x)) for x in targ]
    df["n_target_flags"] = [int(np.sum(x)) for x in targ]
    # Triangle location of each object (load_triangle_data.py, run_cache_data.py:
    # radius within 0.01 of 0.35 and angle within 0.01 rad of a vertex)
    on_tri = np.ones(len(df), bool)
    for i in range(3):
        x, y = df[f"x{i}"].values, df[f"y{i}"].values
        r = np.hypot(x, y)
        th = np.arctan2(y, x) % (2 * np.pi)
        exists = np.isfinite(x)
        d = np.abs((th[:, None] - TRIANGLE_THETAS[None] + np.pi) % (2 * np.pi) - np.pi)
        close = (d < 0.01) & (np.abs(r - RADIUS) < 0.01)[:, None]
        loc = np.where(close.any(1), close.argmax(1), -1)
        on_tri &= ~exists | (loc >= 0)
        df[f"loc{i}"] = np.where(exists, loc, -9)
        df[f"theta{i}"] = th
    df["on_triangle"] = on_tri
    # Target and response geometry
    tx = np.choose(df.target.values, [df.x0.fillna(0).values, df.x1.fillna(0).values,
                                      df.x2.fillna(0).values])
    ty = np.choose(df.target.values, [df.y0.fillna(0).values, df.y1.fillna(0).values,
                                      df.y2.fillna(0).values])
    df["target_x"], df["target_y"] = tx, ty
    df["target_err"] = np.hypot(df.resp_x - tx, df.resp_y - ty)
    df["target_err_closed_loop"] = np.hypot(df.cl_x - tx, df.cl_y - ty)
    df["target_id"] = [r[f"id{t}"] for t, (_, r) in zip(df.target, df.iterrows())]
    df["target_theta"] = np.arctan2(ty, tx) % (2 * np.pi)
    for name, rad in RADII.items():
        df[f"correct_{name}"] = df.target_err < rad
    return df


def task_of(trials):
    """Triangle when more than 20% of trials have 3 objects, Ring when none do
    (run_cache_data.py)."""
    f3 = np.mean(trials.n_obj == 3)
    if f3 > 0.2:
        return "triangle"
    if f3 == 0:
        return "ring"
    return "unknown"


def response_location(trials, radius):
    """Triangle vertex within `radius` of the response, or -1 (load_triangle_data.py)."""
    d = np.hypot(trials.resp_x.values[:, None] - TRIANGLE_XY[None, :, 0],
                 trials.resp_y.values[:, None] - TRIANGLE_XY[None, :, 1])
    close = d < radius
    return np.where(close.any(1), close.argmax(1), -1)


# Windows, as (start event, offset s, end event, offset s). Delay phase from delay onset to
# cue onset and stimulus phase from stimulus onset to delay onset (T4;
# run_firing_rates_per_phase.py; Extended Data Fig. 2 legend). The pre and early windows are
# for the clock check only (standard choice).
WINDOWS = {
    "stimulus": ("phase_stimulus_time", 0.0, "phase_delay_time", 0.0),
    "delay": ("phase_delay_time", 0.0, "phase_cue_time", 0.0),
    "pre": ("phase_stimulus_time", -0.3, "phase_stimulus_time", 0.0),
    "early": ("phase_stimulus_time", 0.05, "phase_stimulus_time", 0.35),
}


def load_units(asset_id, trials, windows=WINDOWS):
    """Units table and per-trial rates (Hz) of every unit in each window.

    A rate is NaN where the trial is not completed (T1) or the unit is not marked stable on
    it (obs_trials; T5: spikes outside the stable interval are excluded), as in
    run_spikes_per_trial.py.
    """
    with open_h5(asset_id) as h:
        g = h["processing/ecephys/units"]
        st = g["spike_times"][:]
        sti = g["spike_times_index"][:]
        obs = g["obs_trials"][:]
        obsi = g["obs_trials_index"][:]
        units = pd.DataFrame({
            "unit": g["id"][:],
            "probe": [x.decode() if isinstance(x, bytes) else x for x in g["electrodes_group"][:]],
            "quality": [x.decode() if isinstance(x, bytes) else x for x in g["quality"][:]],
            "depth": g["depth"][:],
        })
        ois = g["obs_intervals_start"][:]
        oisi = g["obs_intervals_start_index"][:]
        oie = g["obs_intervals_end"][:]
        locs = sorted({x.decode() if isinstance(x, bytes) else x for x in h["general/extracellular_ephys/electrodes/location"][:]})
    units["area"] = np.where(units.probe.str.startswith("vprobe"), "FEF", "DMFC")
    n_tr = len(trials)
    starts = np.r_[0, sti[:-1]]
    ostarts = np.r_[0, obsi[:-1]]
    istarts = np.r_[0, oisi[:-1]]
    obs_mat = np.zeros((len(units), n_tr), bool)
    rates = {w: np.full((len(units), n_tr), np.nan) for w in windows}
    edges = {}
    for w, (e0, o0, e1, o1) in windows.items():
        edges[w] = (trials[e0].values + o0, trials[e1].values + o1)
    comp = trials.completed.values
    n_sorted_bad = 0
    n_spikes_outside = 0
    for u in range(len(units)):
        s = st[starts[u]:sti[u]]
        if np.any(np.diff(s) < 0):
            n_sorted_bad += 1
            s = np.sort(s)
        lo, hi = ois[istarts[u]:oisi[u]], oie[istarts[u]:oisi[u]]
        inside = np.zeros(len(s), bool)
        for a, b in zip(lo, hi):
            inside |= (s >= a) & (s <= b)
        n_spikes_outside += int((~inside).sum())
        s = s[inside]
        o = obs[ostarts[u]:obsi[u]]
        if len(o) != n_tr:
            raise ValueError("obs_trials length differs from trial count")
        obs_mat[u] = o
        ok = o & comp
        for w, (a, b) in edges.items():
            c = np.searchsorted(s, b) - np.searchsorted(s, a)
            r = c / (b - a)
            rates[w][u] = np.where(ok, r, np.nan)
    units["n_obs_trials"] = obs_mat.sum(1)
    units["n_spikes"] = sti - starts
    units.attrs["n_unsorted_units"] = n_sorted_bad
    units.attrs["electrode_locations"] = locs
    units.attrs["n_spikes_outside_intervals"] = n_spikes_outside
    return units, rates, obs_mat


def load_session(assets, subject, session, windows=WINDOWS):
    """Trials, units, rates and stability mask of one session."""
    a = assets[(assets.subject == subject) & (assets.session == session)]
    trials = load_trials(a[a.kind == "behavior+task"].asset_id.iloc[0])
    ss = a[a.kind == "spikesorting"]
    if len(ss) == 0:
        return dict(subject=subject, session=session, trials=trials, task=task_of(trials),
                    units=None, rates=None, obs=None)
    units, rates, obs = load_units(ss.asset_id.iloc[0], trials, windows)
    return dict(subject=subject, session=session, trials=trials, task=task_of(trials),
                units=units, rates=rates, obs=obs)


def ring_sector(theta):
    """Nearest triangle vertex of an angle (three 120-degree sectors centred on the vertices;
    Methods, Receiver-Operator Characteristics; run_cache_selectivity.py)."""
    th = (theta + np.pi / 3) % (2 * np.pi)
    return np.minimum(2, np.floor(3 * th / (2 * np.pi)).astype(int))


# ---------------------------------------------------------------- AUC (T6)

def _midranks(v):
    from scipy.stats import rankdata
    return rankdata(v)


def auc_pair(v0, v1):
    """AUC of v1 against v0 by ranks (ties as half), folded to at least 0.5.
    The code's trapezoid ROC on value-sorted labels equals this up to how ties are ordered
    (standard choice)."""
    n0, n1 = len(v0), len(v1)
    r = _midranks(np.r_[v0, v1])
    a = (r[n0:].sum() - n1 * (n1 + 1) / 2) / (n0 * n1)
    return max(a, 1 - a)


def auc_p_methods(v0, v1, rng, n_shuffle=1000):
    """Methods: shuffle the trial labels 1,000 times; p is the fraction of shuffled folded
    AUCs greater than the empirical folded AUC."""
    n0, n1 = len(v0), len(v1)
    r = _midranks(np.r_[v0, v1])
    a = (r[n0:].sum() - n1 * (n1 + 1) / 2) / (n0 * n1)
    a = max(a, 1 - a)
    perm = rng.permuted(np.tile(np.arange(n0 + n1), (n_shuffle, 1)), axis=1)
    s1 = r[perm[:, n0:]].sum(1)
    an = (s1 - n1 * (n1 + 1) / 2) / (n0 * n1)
    an = np.maximum(an, 1 - an)
    return a, float(np.mean(an > a))


def auc_p_code(v0, v1, rng, n_boot=5000):
    """phys_processing/selectivity/auc.py: values sorted, labels drawn with replacement in
    the sorted order (so the resampled AUC is a null), p = fraction of resampled unfolded
    AUCs at or above the empirical one, folded to at most 0.5."""
    n0, n1 = len(v0), len(v1)
    vals = np.r_[v0, v1]
    lab = np.r_[np.zeros(n0, int), np.ones(n1, int)]
    order = np.argsort(vals, kind="stable")
    lab_sorted = lab[order]
    pos = np.arange(1, n0 + n1 + 1)
    # empirical: area = P(group0 before group1) on the sorted sequence (auc.py orientation)
    def area(labs):
        g1 = labs == 1
        m1 = g1.sum(-1)
        m0 = labs.shape[-1] - m1
        s1 = (g1 * pos).sum(-1)
        with np.errstate(invalid="ignore", divide="ignore"):
            return (s1 - m1 * (m1 + 1) / 2) / (m0 * m1)
    a = float(area(lab_sorted[None])[0])
    idx = rng.integers(0, n0 + n1, size=(n_boot, n0 + n1))
    boot = area(lab_sorted[idx])
    p = float(np.mean(boot >= a))
    p = 1 - p if p > 0.5 else p
    return max(a, 1 - a), p


def unit_auc(rates_1obj, labels, rng, method):
    """Position or identity AUC of one unit (T6): largest folded AUC among the three label
    pairs with p < 0.05, else the largest overall (Methods) or the one of lowest p (code)."""
    aucs, ps = [], []
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        v0, v1 = rates_1obj[labels == i], rates_1obj[labels == j]
        if len(v0) < 2 or len(v1) < 2:
            aucs.append(np.nan); ps.append(np.nan); continue
        if method == "methods":
            a, p = auc_p_methods(v0, v1, rng)
        else:
            a, p = auc_p_code(v0, v1, rng)
        aucs.append(a); ps.append(p)
    aucs, ps = np.array(aucs), np.array(ps)
    sig = ps < 0.05
    if sig.any():
        k = np.nanargmax(np.where(sig, aucs, -1))
    elif method == "methods":
        k = np.nanargmax(aucs)
    else:
        k = np.nanargmin(ps)
    return aucs[k], ps[k]


# ---------------------------------------------------------------- correlations

def pairwise_corr(X, Y=None):
    """Pearson correlation between rows of X and rows of Y over columns where both are
    finite (pairwise complete). Returns (corr, n)."""
    if Y is None:
        Y = X
    Mx, My = np.isfinite(X).astype(float), np.isfinite(Y).astype(float)
    X0, Y0 = np.nan_to_num(X), np.nan_to_num(Y)
    n = Mx @ My.T
    sx = X0 @ My.T
    sy = Mx @ Y0.T
    sxx = (X0 ** 2) @ My.T
    syy = Mx @ (Y0 ** 2).T
    sxy = X0 @ Y0.T
    with np.errstate(invalid="ignore", divide="ignore"):
        cov = n * sxy - sx * sy
        vx = n * sxx - sx ** 2
        vy = n * syy - sy ** 2
        c = cov / np.sqrt(vx * vy)
    c[(vx <= 1e-9) | (vy <= 1e-9)] = np.nan
    return c, n


def mean_ci(x):
    """Mean and 95% normal interval of the mean (standard choice, as seaborn's default
    interval in the paper's plots is a bootstrap of the mean)."""
    x = np.asarray(x)
    x = x[np.isfinite(x)]
    if len(x) < 2:
        return np.nan, np.nan, np.nan, len(x)
    m = x.mean()
    se = x.std(ddof=1) / np.sqrt(len(x))
    return m, m - 1.96 * se, m + 1.96 * se, len(x)


def bin_means(sig, noise, edges):
    """Mean noise correlation per signal-correlation bin with 95% interval; the end bins are
    open (plot_noise_vs_signal_correlation.ipynb clips into the end bins)."""
    sig, noise = np.asarray(sig), np.asarray(noise)
    ok = np.isfinite(sig) & np.isfinite(noise)
    sig, noise = sig[ok], noise[ok]
    k = np.clip(np.digitize(sig, edges[1:-1]), 0, len(edges) - 2)
    rows = []
    for b in range(len(edges) - 1):
        m, lo, hi, n = mean_ci(noise[k == b])
        rows.append(dict(bin=b, lo_edge=edges[b] if b > 0 else -np.inf,
                         hi_edge=edges[b + 1] if b < len(edges) - 2 else np.inf,
                         n_pairs=n, mean_noise=m, ci_lo=lo, ci_hi=hi))
    return pd.DataFrame(rows)


def bin_means_clustered(sig, noise, cluster, edges):
    """As bin_means, with the 95% interval of each bin's mean from a cluster-robust standard
    error, rows of the same cluster (a pair of units) counted as one sample: the code variant
    of Fig. 2d gives a pair up to 18 rows and the Ring pairs are ordered, so each pair appears
    twice (run_compute_ring.py loops over unit_0 and unit_1). A standard choice for the
    interval, which the paper does not give."""
    sig, noise, cluster = np.asarray(sig), np.asarray(noise), np.asarray(cluster)
    ok = np.isfinite(sig) & np.isfinite(noise)
    sig, noise, cluster = sig[ok], noise[ok], cluster[ok]
    k = np.clip(np.digitize(sig, edges[1:-1]), 0, len(edges) - 2)
    rows = []
    for b in range(len(edges) - 1):
        v, c = noise[k == b], cluster[k == b]
        n = len(v)
        if n < 2:
            m = lo = hi = np.nan; g = len(set(c))
        else:
            m = v.mean()
            _, ci = np.unique(c, return_inverse=True)
            g = ci.max() + 1
            res = np.bincount(ci, weights=v - m)
            se = np.sqrt((res ** 2).sum() * g / max(g - 1, 1)) / n
            lo, hi = m - 1.96 * se, m + 1.96 * se
        rows.append(dict(bin=b, n_rows=n, n_pairs=g, mean_noise=m, ci_lo=lo, ci_hi=hi))
    return pd.DataFrame(rows)


def triangle_noise_methods(x, min_rate=MIN_RATE_HZ):
    """Methods, Noise Correlations: signal correlation across the 9 1-object condition means
    (each unit at least 3 trials in each), noise correlation the mean over the 18 2-object
    conditions (at least 3 shared trials) of the across-trial correlation. Delay-phase rates
    (T4) of units above 1 Hz (T5). Returns one row per unordered pair."""
    tr = x["trials"]
    keep = np.nanmean(x["rates"]["delay"], 1) > min_rate
    R = x["rates"]["delay"][keep]
    base = tr.completed.values & tr.on_triangle.values
    one = base & (tr.n_obj == 1).values
    means, ok1 = [], np.ones(keep.sum(), bool)
    for loc in range(3):
        for i in IDS:
            m = one & (tr.loc0.values == loc) & (tr.id0.values == i)
            sub = R[:, m]
            ok1 &= np.isfinite(sub).sum(1) >= 3
            means.append(np.nanmean(sub, 1))
    M = np.stack(means, 1)
    sig = np.corrcoef(M)
    two = base & (tr.n_obj == 2).values
    lo_first = tr.loc0.values < tr.loc1.values
    key = np.where(lo_first, tr.loc0.astype(str) + tr.id0.astype(str) + tr.loc1.astype(str) + tr.id1.astype(str),
                   tr.loc1.astype(str) + tr.id1.astype(str) + tr.loc0.astype(str) + tr.id0.astype(str))
    conds = sorted(set(key[two]))
    s_sum = np.zeros_like(sig); s_n = np.zeros_like(sig)
    for c in conds:
        m = two & (key == c)
        cc, n = pairwise_corr(R[:, m])
        good = (n >= 3) & np.isfinite(cc)
        s_sum += np.where(good, cc, 0); s_n += good
    with np.errstate(invalid="ignore"):
        noise = s_sum / s_n
    iu = np.triu_indices(len(R), 1)
    ok = ok1[iu[0]] & ok1[iu[1]]
    return pd.DataFrame(dict(signal=sig[iu][ok], noise=noise[iu][ok], n_conditions=s_n[iu][ok])), len(conds)


def triangle_noise_code(x, rng, min_rate=MIN_RATE_HZ, n_shuffle=10, min_trials=5):
    """figures/figure_2/noise_correlations/run_compute_triangle.py: per pair and per triple of
    two 1-object conditions and their 2-object composite, the signal correlation of the
    concatenated rates of the two 1-object conditions with one unit's trials shuffled within
    condition (mean of 10 shuffles), and the noise correlation on the composite; rows kept
    with more than 5 trials in each condition (plot_noise_vs_signal_correlation.ipynb). Here
    the shuffle permutes trials for all units at once and the pair's shared trials are taken
    after it (vectorised)."""
    tr = x["trials"]
    keep = np.nanmean(x["rates"]["delay"], 1) > min_rate
    R = x["rates"]["delay"][keep]
    base = tr.completed.values & tr.on_triangle.values
    iu = np.triu_indices(len(R), 1)
    out = []
    for l0 in range(2):
        for l1 in range(l0 + 1, 3):
            for i0 in IDS:
                for i1 in IDS:
                    if i0 == i1:
                        continue
                    c0 = np.where(base & (tr.n_obj == 1).values & (tr.loc0.values == l0) & (tr.id0.values == i0))[0]
                    c1 = np.where(base & (tr.n_obj == 1).values & (tr.loc0.values == l1) & (tr.id0.values == i1))[0]
                    cm = base & (tr.n_obj == 2).values & (
                        ((tr.loc0.values == l0) & (tr.id0.values == i0) & (tr.loc1.values == l1) & (tr.id1.values == i1))
                        | ((tr.loc1.values == l0) & (tr.id1.values == i0) & (tr.loc0.values == l1) & (tr.id0.values == i1)))
                    noise, nc = pairwise_corr(R[:, cm])
                    _, n0 = pairwise_corr(R[:, c0]); _, n1 = pairwise_corr(R[:, c1])
                    cols = np.r_[c0, c1]
                    sigs = []
                    for _ in range(n_shuffle):
                        perm = np.r_[rng.permutation(c0), rng.permutation(c1)]
                        s, _ = pairwise_corr(R[:, cols], R[:, perm])
                        sigs.append(s)
                    sig = np.nanmean(np.stack(sigs), 0) if len(cols) else np.full_like(noise, np.nan)
                    ok = (n0[iu] > min_trials) & (n1[iu] > min_trials) & (nc[iu] > min_trials)
                    out.append(pd.DataFrame(dict(unit_0=iu[0][ok], unit_1=iu[1][ok], signal=sig[iu][ok], noise=noise[iu][ok])))
    return pd.concat(out, ignore_index=True)


def ring_embedding(tr):
    """6-d stimulus embedding [apple x, y, blueberry x, y, orange x, y], 0 when absent
    (Methods, Ring Dataset Signal and Noise Correlations; run_compute_ring.py uses arena
    coordinates)."""
    E = np.zeros((len(tr), 6))
    for i in range(2):
        for k, idn in enumerate(IDS):
            m = (tr[f"id{i}"] == idn).values
            E[m, 2 * k] = tr[f"x{i}"].values[m] + 0.5
            E[m, 2 * k + 1] = tr[f"y{i}"].values[m] + 0.5
    return E


def _nn(E, k):
    D = np.linalg.norm(E[:, None] - E[None], axis=-1)
    np.fill_diagonal(D, np.inf)
    return np.argsort(D, 1)[:, :k] if k > 1 else np.argmin(D, 1)


def ring_noise(x, min_rate=MIN_RATE_HZ, k=10, min_1obj=50, min_2obj=200):
    """Ring signal and noise correlations for ordered pairs of units above 1 Hz, on the trials
    both units were stably recorded on. Signal: one unit's rate on each 1-object trial against
    the other's on the nearest-neighbour trial. Noise (a), Methods: per 2-object trial, the
    correlation of the two units over its 10 nearest-neighbour trials, averaged over trials.
    Noise (b), run_compute_ring.py: each trial's rate minus the mean over its 10 neighbours,
    one correlation of these residuals across trials. Neighbours exclude the trial itself
    (code). Pairs kept with at least 50 1-object and 200 2-object trials
    (noise_correlations.ipynb)."""
    tr = x["trials"]
    keep = np.where(np.nanmean(x["rates"]["delay"], 1) > min_rate)[0]
    R = x["rates"]["delay"][keep]
    F = np.isfinite(R)
    E = ring_embedding(tr)
    n_obj = tr.n_obj.values
    # Neighbour order of every completed trial among the completed trials with the same
    # number of objects, sorted once (the trial itself last); the neighbours within a pair's
    # shared trials are the first ones of this order that are shared, which is what the
    # code's per-pair search gives.
    comp = tr.completed.values
    order = {}
    for n in (1, 2):
        idx = np.where(comp & (n_obj == n))[0]
        D = np.linalg.norm(E[idx][:, None] - E[idx][None], axis=-1)
        np.fill_diagonal(D, np.inf)
        order[n] = (idx, idx[np.argsort(D, 1, kind="stable")])
    def neighbours(shared, n, kk):
        idx, o = order[n]
        rows_ = shared[idx]
        t = idx[rows_]
        oo = o[rows_]
        m = shared[oo]
        c = np.cumsum(m, 1)
        sel = m & (c <= kk)
        return t, oo[sel].reshape(len(t), kk)
    pats, inv = np.unique(F, axis=0, return_inverse=True)
    inv = inv.ravel()
    rows = []
    for a in range(len(pats)):
        for b in range(len(pats)):
            shared = pats[a] & pats[b]
            if (shared & (n_obj == 1)).sum() < min_1obj or (shared & (n_obj == 2)).sum() < min_2obj:
                continue
            ua, ub = np.where(inv == a)[0], np.where(inv == b)[0]
            t1, nn1 = neighbours(shared, 1, 1)
            sig, _ = pairwise_corr(R[ua][:, t1], R[ub][:, nn1[:, 0]])
            t2, nn2 = neighbours(shared, 2, k)
            Ga, Gb = R[ua][:, nn2], R[ub][:, nn2]
            nb, _ = pairwise_corr(R[ua][:, t2] - Ga.mean(-1), R[ub][:, t2] - Gb.mean(-1))
            Ga = Ga - Ga.mean(-1, keepdims=True); Gb = Gb - Gb.mean(-1, keepdims=True)
            with np.errstate(invalid="ignore", divide="ignore"):
                Za = Ga / np.sqrt((Ga ** 2).sum(-1))[..., None]
                Zb = Gb / np.sqrt((Gb ** 2).sum(-1))[..., None]
            fa = np.isfinite(Za[..., 0]); fb = np.isfinite(Zb[..., 0])
            Za0 = np.where(fa[..., None], Za, 0.0); Zb0 = np.where(fb[..., None], Zb, 0.0)
            csum = np.einsum("itk,jtk->ij", Za0, Zb0, optimize=True)
            with np.errstate(invalid="ignore", divide="ignore"):
                na = csum / (fa.astype(float) @ fb.astype(float).T)
            I, J = np.meshgrid(np.arange(len(ua)), np.arange(len(ub)), indexing="ij")
            same = ua[I] == ub[J]
            rows.append(pd.DataFrame(dict(unit_0=ua[I][~same], unit_1=ub[J][~same], signal=sig[~same],
                                          noise_a=na[~same], noise_b=nb[~same],
                                          n_1obj=len(t1), n_2obj=len(t2))))
    return pd.concat(rows, ignore_index=True) if rows else pd.DataFrame()



# ---------------------------------------------------------------- decoding (Extended Data Fig. 3)

def get_simultaneous(presence, keep_units_weight=1.0):
    """Greedy removal of the worst-covered unit or trial until every remaining unit is
    observed on every remaining trial (figures/supp_fig_decoding/modeling/dataset.py)."""
    presence = presence.copy()
    unit_idx = list(range(presence.shape[1]))
    trial_idx = list(range(presence.shape[0]))
    while True:
        pu = presence.mean(0); pt = presence.mean(1)
        wu, wt = int(np.argmin(pu)), int(np.argmin(pt))
        if pu[wu] == 1 and pt[wt] == 1:
            break
        if pt[wt] < keep_units_weight * pu[wu]:
            presence = np.delete(presence, wt, 0); trial_idx.pop(wt)
        else:
            presence = np.delete(presence, wu, 1); unit_idx.pop(wu)
    return np.array(unit_idx, int), np.array(trial_idx, int)


def decoding_data(x, units, phase, kind, feature, min_trials_per_unit=50, min_units_per_trial=5, info=False):
    """Neural matrix (trials x units) and labels as dataset.py and labelers.py build them.
    kind "1": 1-object Triangle trials, one-hot location or identity; "complement": 2-object
    Triangle trials, the location or identity absent; "2obj": 2-object trials with one label
    per object (Triangle one-hot location, Ring 2x - 1 and 2y - 1 in arena coordinates).
    Triangle trials are on the triangle; all trials are completed. `units` are the indices of
    the units entering the models (T7). The rates are not normalised: dataset.py has the per-unit
    z-scoring commented out ("# Normalize neural data"), so the code's decoders get rates in Hz.
    With info=True also returns the units and trials left after each of the code's filters."""
    tr = x["trials"]
    m = tr.completed.values.copy()
    if x["task"] == "triangle":
        m &= tr.on_triangle.values
    n_need = 1 if kind == "1" else 2
    m &= (tr.n_obj == n_need).values
    idx = np.where(m)[0]
    if kind in ("1", "complement"):
        if feature == "position":
            oh = [np.eye(3)[tr[f"loc{i}"].values[idx].clip(0)] for i in range(n_need)]
        else:
            oh = [np.eye(3)[tr[f"id{i}"].map({"a": 0, "b": 1, "c": 2}).fillna(0).astype(int).values[idx]] for i in range(n_need)]
        Y = oh[0] if kind == "1" else 1 - oh[0] - oh[1]
    else:
        if x["task"] == "triangle":
            Y = np.stack([np.eye(3)[tr[f"loc{i}"].values[idx].clip(0)] for i in range(2)], 1)
        else:
            Y = np.stack([np.stack([2 * tr[f"x{i}"].values[idx], 2 * tr[f"y{i}"].values[idx]], 1)
                          for i in range(2)], 1)
    X = x["rates"][phase][units][:, idx].T
    counts = dict(units_in=X.shape[1], trials_in=X.shape[0])
    ku = np.isfinite(X).sum(0) >= min_trials_per_unit
    X = X[:, ku]
    kt = np.isfinite(X).sum(1) >= min_units_per_trial
    X, Y = X[kt], Y[kt]
    counts.update(units_min_trials=X.shape[1], trials_min_units=X.shape[0])
    u_keep, t_keep = get_simultaneous(np.isfinite(X))
    counts.update(units_simultaneous=len(u_keep), trials_simultaneous=len(t_keep))
    if info:
        return X[t_keep][:, u_keep], Y[t_keep], counts
    return X[t_keep][:, u_keep], Y[t_keep]


def synthetic_2obj(X, Y, task, mode, rng):
    """Receptive Field and Orthogonal synthetic data of dataset.py, scaled per unit to the
    mean and variance of the real data. Triangle: log-normal receptive fields over the three
    locations; Ring: units with centres uniform in [-1, 1]^2 and response exp(-distance)
    (and, for Orthogonal, scales uniform in [1, 30]). Orthogonal: each object drives half of
    the units, the halves assigned at random per trial."""
    n, u = X.shape
    half = u // 2
    if task == "triangle":
        rf = np.exp(rng.normal(0, 1, size=(3, u)))
        if mode == "receptive_fields":
            Z = Y.sum(1) @ rf
        else:
            Z = np.stack([Y[:, 0] @ rf, Y[:, 1] @ rf], 1)
            for i in range(n):
                if rng.random() < 0.5:
                    Z[i, 1, :half] = 0; Z[i, 0, half:] = 0
                else:
                    Z[i, 0, :half] = 0; Z[i, 1, half:] = 0
            Z = Z.sum(1)
    else:
        c = rng.uniform(-1, 1, size=(2, u))
        prox = np.stack([np.linalg.norm(c[None] - Y[:, j, :, None], axis=1) for j in range(2)], -1)
        if mode == "receptive_fields":
            Z = np.exp(-prox).sum(-1)
        else:
            Z = np.exp(-prox) * rng.uniform(1, 30, size=u)[None, :, None]
            for i in range(n):
                if rng.random() < 0.5:
                    Z[i, :half, 0] = 0; Z[i, half:, 1] = 0
                else:
                    Z[i, :half, 1] = 0; Z[i, half:, 0] = 0
            Z = Z.sum(-1)
    Z = (Z - Z.mean(0)) / np.sqrt(Z.var(0) + 1e-8) * np.sqrt(X.var(0)) + X.mean(0)
    return Z


def _sig(z):
    return 1 / (1 + np.exp(-z))


class _Opt:
    """SGD or Adam (torch defaults: betas 0.9, 0.999, eps 1e-8) on a list of arrays."""
    def __init__(self, params, kind, lr):
        self.p, self.kind, self.lr, self.t = params, kind, lr, 0
        self.m = [np.zeros_like(q) for q in params]
        self.v = [np.zeros_like(q) for q in params]

    def step(self, grads):
        self.t += 1
        for q, g, m, v in zip(self.p, grads, self.m, self.v):
            if self.kind == "sgd":
                q -= self.lr * g
            else:
                m *= 0.9; m += 0.1 * g
                v *= 0.999; v += 0.001 * g * g
                mh = m / (1 - 0.9 ** self.t); vh = v / (1 - 0.999 ** self.t)
                q -= self.lr * mh / (np.sqrt(vh) + 1e-8)


def train_linear(Xtr, Ytr, rng, opt="sgd", lr=0.01, l1=0.003, steps=10000, batch=512):
    """LinearModel1Object of models.py, batched over F fits: Xtr (F, n, U), Ytr (F, n, K);
    sigmoid outputs, mean squared error, L1 on weights and bias, batches of 512 drawn with
    replacement. Configs: config_1_triangle.py (SGD, lr 0.01), config_2_triangle_complement.py
    (Adam, lr 0.001); 10,000 steps, L1 weight 0.003. Initialisation as torch.nn.Linear."""
    F, n, U = Xtr.shape; K = Ytr.shape[-1]
    bound = 1 / np.sqrt(U)
    W = rng.uniform(-bound, bound, (F, U, K)).astype(np.float32)
    b = rng.uniform(-bound, bound, (F, 1, K)).astype(np.float32)
    o = _Opt([W, b], opt, lr)
    fi = np.arange(F)[:, None]
    for _ in range(steps):
        idx = rng.integers(0, n, (F, batch))
        xb, yb = Xtr[fi, idx], Ytr[fi, idx]
        out = _sig(xb @ W + b)
        gz = 2 * (out - yb) / (batch * K) * out * (1 - out)
        gW = np.transpose(xb, (0, 2, 1)) @ gz + l1 * np.sign(W)
        gb = gz.sum(1, keepdims=True) + l1 * np.sign(b)
        o.step([gW, gb])
    return W, b


def train_linear_2obj(Xtr, Ytr, rng, lr=0.001, l1=0.003, steps=10000, batch=512, output="sigmoid"):
    """LinearModel2Objects of models.py, batched over F fits: two sigmoid linear decoders and a
    per-trial logit choosing which decoder reads which object (loss weighted by the sigmoid of
    the logit, as in the code), MSE per decoder and object, L1 on both decoders. Config
    config_2_triangle.py / config_2_ring.py: Adam, lr 0.001, L1 0.003, 10,000 steps. Ytr is
    (F, n, 2, K). models.py applies the sigmoid for the Ring too, whose targets 2x - 1, 2y - 1
    (labelers.py) lie in [-0.7, 0.7]; output="linear" drops it, a variant that is not the
    code's, for checking how much the angles depend on it."""
    F, n, U = Xtr.shape; K = Ytr.shape[-1]
    act = _sig if output == "sigmoid" else (lambda z: z)
    dact = (lambda o: o * (1 - o)) if output == "sigmoid" else (lambda o: 1.0)
    bound = 1 / np.sqrt(U)
    W0 = rng.uniform(-bound, bound, (F, U, K)).astype(np.float32)
    b0 = rng.uniform(-bound, bound, (F, 1, K)).astype(np.float32)
    W1 = rng.uniform(-bound, bound, (F, U, K)).astype(np.float32)
    b1 = rng.uniform(-bound, bound, (F, 1, K)).astype(np.float32)
    lg = np.zeros((F, n), np.float32)
    o = _Opt([W0, b0, W1, b1, lg], "adam", lr)
    fi = np.arange(F)[:, None]
    for _ in range(steps):
        idx = rng.integers(0, n, (F, batch))
        xb, yb = Xtr[fi, idx], Ytr[fi, idx]
        o0 = act(xb @ W0 + b0); o1 = act(xb @ W1 + b1)
        l00 = ((o0 - yb[:, :, 0]) ** 2).mean(-1); l11 = ((o1 - yb[:, :, 1]) ** 2).mean(-1)
        l10 = ((o1 - yb[:, :, 0]) ** 2).mean(-1); l01 = ((o0 - yb[:, :, 1]) ** 2).mean(-1)
        ps = _sig(lg[fi, idx])
        # d loss / d outputs
        g0 = (ps[..., None] * 2 * (o0 - yb[:, :, 0]) + (1 - ps)[..., None] * 2 * (o0 - yb[:, :, 1])) / (batch * K)
        g1 = (ps[..., None] * 2 * (o1 - yb[:, :, 1]) + (1 - ps)[..., None] * 2 * (o1 - yb[:, :, 0])) / (batch * K)
        gz0 = g0 * dact(o0); gz1 = g1 * dact(o1)
        xt = np.transpose(xb, (0, 2, 1))
        gW0 = xt @ gz0 + l1 * np.sign(W0); gb0 = gz0.sum(1, keepdims=True) + l1 * np.sign(b0)
        gW1 = xt @ gz1 + l1 * np.sign(W1); gb1 = gz1.sum(1, keepdims=True) + l1 * np.sign(b1)
        gps = ((l00 + l11) - (l10 + l01)) / batch * ps * (1 - ps)
        glg = np.zeros_like(lg)
        np.add.at(glg, (np.repeat(np.arange(F), batch), idx.ravel()), gps.ravel())
        o.step([gW0, gb0, gW1, gb1, glg])
    return W0, W1


def angles_deg(W0, W1):
    """Angle between corresponding columns of the two decoders (orthogonality.ipynb)."""
    c = (W0 * W1).sum(-2) / (np.linalg.norm(W0, axis=-2) * np.linalg.norm(W1, axis=-2))
    return np.degrees(np.arccos(np.clip(c, -1, 1)))
