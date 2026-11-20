"""Loading and measures for Masset et al. (2025), "Multi-timescale reinforcement learning in the brain".

Data sources
------------
- DANDI:000251 (draft, the only version; no version has been published). It holds the VR task
  single units of Kim et al. (2020), one unit per file. Units of the open-loop sessions are in files
  named ``SU-VR-OL-*``; the ``SU-VR-ALL-OL-*`` files repeat 78 of them byte for byte
  (``dandi_vr_units`` keeps one copy of each spike train).
- Mendeley Data doi:10.17632/tc43t3s7c5.1, the paper's own deposit. ``DA_SU_ODOR_NEW_W_OL.h5``
  holds the cued delay task single units, which DANDI:000251 does not hold, and
  ``FinalAverageArray.mat`` holds the paper's per-neuron table (one row per neuron, with both tasks),
  used to link the two tasks' units (link claim) and to give the cue responses of the 11 cued delay
  neurons the HDF5 file lacks (``table_cue_responses``). Files are streamed into memory.

Where each parameter comes from is given at its definition: "claim" for the claims file's
criterion or its shared methods M1 to M8 (which cite the paper and its code), "paper" with the
passage, "assumption" with the reason, or "standard" for a choice that cannot change a result.
"""
import io
import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
import requests
import scipy.io as sio
from scipy import optimize, stats

DANDISET = "000251"
DANDI_VERSION = "draft"
DANDI_MODIFIED = "2023-06-20T00:56:22.602125Z"  # modification time of the draft that was read
MENDELEY_DOI = "10.17632/tc43t3s7c5.1"
MENDELEY = {  # file id in the Mendeley deposit, version 1, and its SHA-256 from the deposit's file list
    "DA_SU_ODOR_NEW_W_OL.h5": ("b05c4757-af6a-4974-adc3-c58ad121dd81",
                               "fc7c9c15934aea2cf28b79d10276d2e912877e6ca7136b14b5d420d9b081b95a"),
    "FinalAverageArray.mat": ("6c7af5ba-8768-4355-9861-ce27675e85eb",
                              "884733322721f9311d7e5ad10b93e05c1a6916d892f266875f67f5c462dbee2b"),
    "Valid_S.mat": ("9fb0babd-d502-4505-a944-26539e486ad3",
                    "b4d6d0ea4b6ea986072e12e3b5ea65256ba5978eaea8914686efca3e3e4257ea"),
}

# Claim, M6: the last 4.30 s before reward, 3.05 to 7.35 s after scene motion onset, 43 bins of 0.1 s.
VR_START, VR_END, VR_DT = 3.05, 7.35, 0.1
VR_NBINS = 43
EARLY_NORM = 15  # claim, M6: z-score mean over the first 15 bins (1.5 s, Methods)
RATE_MIN = 2.0  # claim, M3 and M6: spikes/s
ML_MAX = 900.0  # claim, M3 and M6: um
N_BOOT = 100  # claim, M2 and M6: 100 bootstraps of random half splits
DELAYS = np.array([0.6, 1.5, 3.75, 9.375])  # paper, Methods, Cued delay task
CUE_WIN = (0.1, 0.4)  # claim, M1
# Claim, M4: decoding grid of 120 points on 0 to 12 s (code linspace(0, 12, 120)); true delays at
# grid indices 7, 16, 38, 95 (1-based in the code).
T_GRID = np.linspace(0, 12, 120)
TRUE_IDX = np.array([7, 16, 38, 95]) - 1
ALPHA_TIKHONOV = 2.0  # claim, M4


# ----------------------------------------------------------------------------------------------
# DANDI


def dandi_assets():
    url = (f"https://api.dandiarchive.org/api/dandisets/{DANDISET}/versions/{DANDI_VERSION}/"
           "assets/?page_size=1000")
    out = {}
    while url:
        page = json.load(urllib.request.urlopen(url))
        out.update({a["path"]: a for a in page["results"]})
        url = page["next"]
    return out


def dandi_version_info():
    url = f"https://api.dandiarchive.org/api/dandisets/{DANDISET}/versions/{DANDI_VERSION}/info/"
    return json.load(urllib.request.urlopen(url))


def _read_su(asset):
    url = f"https://api.dandiarchive.org/api/assets/{asset['asset_id']}/download/"
    with h5py.File(remfile.File(url), "r") as h:
        idx = h["units/spike_times_index"][:]
        st = h["units/spike_times"][:]
        tr = h["intervals/trials"]
        trials = {c: tr[c][:] for c in tr.keys() if c not in ("id",) and not c.endswith("_index")}
        trials["trial_type"] = np.array([x.decode() if isinstance(x, bytes) else x
                                         for x in trials["trial_type"]])
        licks = h["acquisition/lick_times/timestamps"][:]
        return dict(path=asset["path"], subject=h["general/subject/subject_id"][()].decode(),
                    start=h["session_start_time"][()].decode(), n_units=len(idx),
                    ml=float(h["units/implant_ML"][0]), spikes=st, trials=trials, licks=licks,
                    unit_desc=h["units"].attrs.get("description", ""))


def dandi_su_files(assets, kinds=("SU-VR-OL", "SU-VR-ALL-OL", "SU-VR-ALL-TP", "SU-VR-ALL-SPD")):
    """Read every single-unit file of the given kinds (file name between ``ses-`` and the number)."""
    paths = sorted(p for p in assets if "_ses-" in p and
                   p.split("_ses-")[1].rsplit("-", 1)[0] in kinds)
    with ThreadPoolExecutor(12) as ex:
        units = list(ex.map(lambda p: _read_su(assets[p]), paths))
    for u in units:
        u["kind"] = u["path"].split("_ses-")[1].rsplit("-", 1)[0]
        u["spike_key"] = hash(u["spikes"].tobytes())
        u["mouse"] = int(u["subject"])
    return units


def dandi_vr_units(files):
    """The open-loop units: the SU-VR-OL files, one copy of each spike train, with only the trial
    type of the standard track (``same=1.0``). A file whose trials include teleports is left out
    (claim, M6: sessions without teleport or speed manipulation)."""
    seen, out, dropped = set(), [], []
    for u in files:
        if u["kind"] != "SU-VR-OL" or u["spike_key"] in seen:
            continue
        seen.add(u["spike_key"])
        if set(u["trials"]["trial_type"]) != {"same=1.0"}:
            dropped.append(u["path"])
            continue
        out.append(u)
    return out, dropped


# ----------------------------------------------------------------------------------------------
# Mendeley


def mendeley_url(name):
    return (f"https://data.mendeley.com/public-files/datasets/tc43t3s7c5/files/"
            f"{MENDELEY[name][0]}/file_downloaded")


def _s(ds):
    return bytes(ds[:].ravel().astype(np.uint8)).decode("latin1")


def odor_units():
    """Cued delay units from DA_SU_ODOR_NEW_W_OL.h5. Times in the file are in ms; returned in s.
    Event columns follow metainfo/event_label (TRIAL_START, VSTIM_ON, ...); the odor onset is the
    VSTIM_ON column (checked in the notebook against the reward times and the delays)."""
    h = h5py.File(remfile.File(mendeley_url("DA_SU_ODOR_NEW_W_OL.h5")), "r")
    out = []
    for k in sorted(h.keys(), key=int):
        g = h[k]
        labels = _s(g["metainfo/event_label"]).strip(",").split(",")
        ev = g["event"][:] / 1000.0
        out.append(dict(key=int(k), mouse=int(g["metainfo/mid"][0, 0]),
                        ml=float(g["metainfo/implant_ML"][0, 0]),
                        session=_s(g["metainfo/session_datetime"]),
                        events={lab: ev[i] for i, lab in enumerate(labels)},
                        grp=g["grp_idx"][0].astype(int), grp_label=_s(g["metainfo/grp_label"]),
                        spikes=g["spike"][0] / 1000.0, licks=g["lick"][0] / 1000.0))
    h.close()
    return out


def table_cue_responses(row, win=CUE_WIN):
    """Per-trial cue response of a row of the paper's table, the mean of its 10 ms rates (time
    axis from odor onset) in ``win``, and the trial's delay. Used only for the cued delay units the
    Mendeley spike file lacks; the notebook compares it with the spike counts of the linked units."""
    o = row["odor"]
    k = (o["x"] >= win[0] - 1e-9) & (o["x"] < win[1] - 1e-9)
    return np.nanmean(o["rate"][:, k], 1), DELAYS[np.asarray(o["grp"]).astype(int) - 1]


def average_array():
    """The paper's per-neuron table, FinalAverageArray.mat (version 5 MAT file, read in memory).
    For each row: mouse, ML position, and for the cued delay (OdorNew) and VR columns the unit name,
    trial count, time axis and per-trial rates at 10 ms."""
    raw = requests.get(mendeley_url("FinalAverageArray.mat"), timeout=600).content
    A = sio.loadmat(io.BytesIO(raw), squeeze_me=True, struct_as_record=False)["AverageArray"]
    rows = []
    for i in range(1, A.shape[0]):
        r = dict(row=i - 1, mouse=int(A[i, 0]), ml=float(A[i, 10]))
        for j, nm in ((2, "odor"), (3, "vr")):
            x = A[i, j]
            if hasattr(x, "_fieldnames"):
                r[nm] = dict(name=str(x.name), x=np.asarray(x.x, float),
                             rate=np.atleast_2d(np.asarray(x.rate_rsp, float)),
                             grp=np.atleast_1d(np.asarray(x.grp)))
        rows.append(r)
    del A, raw
    return rows


def valid_flags():
    """Valid.OdorNew and Valid.VR of Valid_S.mat (MATLAB 7.3, read in memory): the paper's flags of
    the neurons recorded in each task, one per row of FinalAverageArray (claims file, M3 and M6)."""
    raw = requests.get(mendeley_url("Valid_S.mat"), timeout=120).content
    with h5py.File(io.BytesIO(raw), "r") as h:
        return {k: h["Valid"][k][:].ravel() == 1 for k in h["Valid"].keys()}


def per_trial_counts(spikes, align, x, rate):
    """Spike count of each trial over the part of the table's time axis ``x`` where the table's
    per-trial rate is defined (trials differ in length; the table pads them with NaN)."""
    out = np.full(len(align), np.nan)
    for k, a in enumerate(align):
        v = x[~np.isnan(rate[k])]
        if np.isfinite(a) and len(v):
            out[k] = np.sum((spikes >= a + v[0]) & (spikes < a + v[-1] + 0.01))
    return out


def link_units(units, rows, task, align):
    """Match each unit to the row of the paper's table, same mouse and trial count, whose per-trial
    spike counts (sum of the 10 ms rates times 0.01 s) are closest (mean absolute difference).
    Returns, per unit, (row, difference, next best difference)."""
    out = []
    for u in units:
        al = align(u)
        cands = []
        for r in rows:
            if task not in r or r["mouse"] != u["mouse"] or r[task]["rate"].shape[0] != len(al):
                continue
            tab = r[task]
            c = per_trial_counts(u["spikes"], al, tab["x"], tab["rate"])
            ref = np.nansum(tab["rate"], 1) * 0.01
            ok = np.isfinite(c)
            cands.append((float(np.mean(np.abs(c[ok] - ref[ok]))), r["row"]))
        cands.sort()
        out.append((cands[0][1] if cands else None, cands[0][0] if cands else np.nan,
                    cands[1][0] if len(cands) > 1 else np.nan))
    return out


# ----------------------------------------------------------------------------------------------
# Binning


def counts_aligned(spikes, align, t0, t1, dt):
    """Spike counts per trial in bins of ``dt`` from ``t0`` to ``t1`` around ``align``."""
    edges = np.arange(int(round((t1 - t0) / dt)) + 1) * dt + t0
    out = np.zeros((len(align), len(edges) - 1))
    for k, a in enumerate(align):
        if np.isfinite(a):
            out[k] = np.histogram(spikes, edges + a)[0]
        else:
            out[k] = np.nan
    return out, edges


def vr_trial_rates(u):
    """Per-trial rate (spikes/s) in the 43 bins of 0.1 s from 3.05 to 7.35 s after scene motion
    onset (claim, M6). Equal to the 10 ms box-filtered rate (paper, Methods, VR task, paragraph 3)
    averaged in 0.1 s bins."""
    sm = u["trials"]["scene_move"]
    sm = sm[np.isfinite(sm)]
    c, _ = counts_aligned(u["spikes"], sm, VR_START, VR_END, VR_DT)
    return c / VR_DT


def split_halves(n, rng):
    """A random split of n trials in two halves (claim, M2 and M6, "random split of the trials in
    halves"). The code's split (PermutedOrder(1:floor(n/2)) and PermutedOrder(ceil(n/2):n)) shares
    one trial between the halves when n is odd; disjoint halves are used here, as the Methods
    describe. This is a deviation from the code (one trial of 25 to 125)."""
    p = rng.permutation(n)
    return p[: n // 2], p[n // 2:]


def norm_psth(b):
    """Modified z-score (claim, M6): minus the mean of the first 15 bins, over the s.d. of all 43."""
    return (b - b[:, :EARLY_NORM].mean(1, keepdims=True)) / b.std(1, ddof=1, keepdims=True)


def vr_bootstrap_psths(rates, rng, n_boot=N_BOOT):
    """Binned half-PSTHs: array (n_boot, 2, n_neurons, 43)."""
    out = np.zeros((n_boot, 2, len(rates), VR_NBINS))
    for b in range(n_boot):
        for i, r in enumerate(rates):
            h1, h2 = split_halves(len(r), rng)
            out[b, 0, i] = r[h1].mean(0)
            out[b, 1, i] = r[h2].mean(0)
    return out


def ramp_slopes(psths):
    """Slope per half (claim, fig3b): (mean of normalised bins 34 to 39 minus mean of bins 6 to 11,
    1-based) / 2.8 s. ``psths`` (n_boot, 2, N, 43) -> (2 n_boot, N), first halves first."""
    nb = psths.shape[0]
    flat = np.concatenate([psths[:, 0], psths[:, 1]], 0)
    out = np.zeros(flat.shape[:2])
    for k in range(2 * nb):
        z = norm_psth(flat[k])
        out[k] = (z[:, 33:39].mean(1) - z[:, 5:11].mean(1)) / 2.8
    return out


# ----------------------------------------------------------------------------------------------
# Common value function model (claim, M7; code Cost_VR_SingleValue_Norm_All_gain.m)


def _cv_unpack(x, n):
    return x[:n], x[n:2 * n], x[2 * n:3 * n], x[3 * n:]


def cv_sse(x, R, dt=VR_DT):
    """Sum of squared errors of delta_i(t) = b_i + a_i (dV/dt + ln(gamma_i) V(t)) on bins 1 to 42.
    The code minimises its square root, which has the same minimum."""
    n = R.shape[0]
    g, b, a, V = _cv_unpack(x, n)
    dV = np.diff(V) / dt
    lg = np.log(g)
    inner = dV[None, :] + lg[:, None] * V[None, :-1]
    E = b[:, None] + a[:, None] * inner - R[:, :-1]
    f = (E ** 2).sum()
    gg = 2 * (E * a[:, None] * V[None, :-1]).sum(1) / g
    gb = 2 * E.sum(1)
    ga = 2 * (E * inner).sum(1)
    w = 2 * E * a[:, None]
    gV = np.zeros_like(V)
    gV[:-1] += (w * (lg[:, None] - 1.0 / dt)).sum(0)
    gV[1:] += w.sum(0) / dt
    return f, np.concatenate([gg, gb, ga, gV])


def cv_initial(n, rng):
    """Initial values of the code: gamma 0.1 + 0.8 U, baseline and gain 3 U, V linear 0.05 to 1."""
    return np.concatenate([0.1 + 0.8 * rng.random(n), 3 * rng.random(n), 3 * rng.random(n),
                           np.linspace(0.05, 1, VR_NBINS)])


def cv_bounds(n):
    """Bounds of the code: gamma [0.05, 0.999999], baseline [0.05, 12], gain [0.05, 50], V [0.001, 1]."""
    return ([(0.05, 0.999999)] * n + [(0.05, 12)] * n + [(0.05, 50)] * n
            + [(0.001, 1)] * VR_NBINS)


B_BOUNDS, A_BOUNDS = (0.05, 12), (0.05, 50)  # code bounds of baseline and gain


def _ab_given(U, Y, b_lim=B_BOUNDS, a_lim=A_BOUNDS):
    """Per row, the box-bounded least squares fit of Y ~ b + a U (exact: the interior solution
    where it is feasible, otherwise the best of the solutions on each edge and the corners)."""
    um, ym = U.mean(1), Y.mean(1)
    vu = ((U - um[:, None]) ** 2).sum(1)
    cuy = ((U - um[:, None]) * (Y - ym[:, None])).sum(1)
    a = np.where(vu > 0, cuy / np.where(vu > 0, vu, 1), a_lim[0])
    b = ym - a * um
    bad = (a < a_lim[0]) | (a > a_lim[1]) | (b < b_lim[0]) | (b > b_lim[1])
    if not bad.any():
        return a, b
    Ub, Yb = U[bad], Y[bad]
    n = len(Ub)
    umb, ymb = um[bad], ym[bad]
    cands = []
    for af in a_lim:
        aa = np.full(n, af)
        cands.append((aa, np.clip(ymb - aa * umb, *b_lim)))
    s2 = (Ub ** 2).sum(1)
    for bf in b_lim:
        cands.append((np.clip(((Yb - bf) * Ub).sum(1) / np.where(s2 > 0, s2, 1), *a_lim),
                      np.full(n, bf)))
    best_a, best_b, best = None, None, None
    for ca, cb in cands:
        sse = ((cb[:, None] + ca[:, None] * Ub - Yb) ** 2).sum(1)
        if best is None:
            best_a, best_b, best = ca.copy(), cb.copy(), sse
        else:
            m = sse < best
            best_a[m], best_b[m], best[m] = ca[m], cb[m], sse[m]
    a, b = a.copy(), b.copy()
    a[bad], b[bad] = best_a, best_b
    return a, b


def _cv_projected(th, R):
    n = R.shape[0]
    g, V = th[:n], th[n:]
    U = (np.diff(V) / VR_DT)[None, :] + np.log(g)[:, None] * V[None, :-1]
    a, b = _ab_given(U, R[:, :-1])
    x = np.concatenate([g, b, a, V])
    f, gr = cv_sse(x, R)
    return f, np.concatenate([gr[:n], gr[3 * n:]]), x


CV_MAXITER = 10000  # assumption: iteration cap (the code caps fmincon at 2000 iterations); the notebook
# shows that 3000 and 30000 iterations give other results on a subset


def cv_fit(R, x0, maxiter=CV_MAXITER):
    """Fit the common value model to binned PSTHs R (neurons x 43). The code minimises with fmincon
    (interior point, MaxIter 2000) over all parameters. Here, for each value of the discount
    factors and the value function, the gains and baselines are solved exactly (variable
    projection, same bounds), and the discount factors and value function are optimised by L-BFGS-B
    with the analytic gradient, from the code's initial values. The optimiser is a substitute
    (deviation)."""
    n = R.shape[0]
    th0 = np.concatenate([x0[:n], x0[3 * n:]])
    res = optimize.minimize(lambda th: _cv_projected(th, R)[:2], th0, jac=True, method="L-BFGS-B",
                            bounds=[(0.05, 0.999999)] * n + [(0.001, 1)] * VR_NBINS,
                            options=dict(maxiter=maxiter, maxfun=2 * maxiter, ftol=1e-13,
                                         gtol=1e-9))
    x = _cv_projected(res.x, R)[2]
    g, b, a, V = _cv_unpack(x, n)
    # gain stored as in the code: a / gamma^dt
    return dict(gamma=g, base=b, gain=a / g ** VR_DT, a=a, V=V, sse=res.fun, ok=res.success,
                nit=res.nit)


def _cv_job(args):
    return cv_fit(*args)


def cv_fit_bootstraps(psths, x0, workers=4):
    """Fit both halves of each bootstrap with the same initial values (as the code); returns arrays
    (2 n_boot, ...) with first halves first."""
    from concurrent.futures import ProcessPoolExecutor
    nb = psths.shape[0]
    jobs = [(psths[k % nb, k // nb], x0) for k in range(2 * nb)]
    with ProcessPoolExecutor(workers) as ex:
        fits = list(ex.map(_cv_job, jobs))
    out = {k: np.array([f[k] for f in fits])
           for k in ("gamma", "base", "gain", "a", "V", "sse", "ok", "nit")}
    return out


# ----------------------------------------------------------------------------------------------
# Common reward expectation model (claim, ed9g; code Cost_VR_FoldedNormal_All.m, FoldedNormal.m,
# ValueConstraint.m)

HORIZON = np.linspace(0, 10, int(round(10 / VR_DT)))  # code: reward horizon 10 s, nrh points
_C_FOLDED = np.sqrt(2 / np.pi)


def _folded(x, mu, s):
    """Folded normal density (code FoldedNormal.m) and its derivative in s. Written as the sum of
    two Gaussians, which equals the code's exp(-(x^2 + mu^2) / 2s^2) cosh(x mu / s^2) but does not
    overflow at small s (the code sets the resulting non-finite values to 1e-4)."""
    A = np.exp(-(x - mu) ** 2 / (2 * s ** 2))
    B = np.exp(-(x + mu) ** 2 / (2 * s ** 2))
    F = _C_FOLDED / s * 0.5 * (A + B)
    dF = -F / s + _C_FOLDED / s * 0.5 * (A * (x - mu) ** 2 + B * (x + mu) ** 2) / s ** 3
    return F, dF


def fr_value(g, sig):
    """Value V (neurons x 43) and its derivatives in each neuron's gamma and in each bin's sigma."""
    times = np.linspace(VR_NBINS * VR_DT, 0, VR_NBINS)  # code: Time = linspace(T, 0, Nspace)
    F, dF = _folded(HORIZON[:, None], times[None, :], sig[None, :])  # (nrh, T)
    D = g[:, None] ** HORIZON[None, :]
    Dg = HORIZON[None, :] * g[:, None] ** (HORIZON[None, :] - 1)
    return D @ F, Dg @ F, D @ dF


def fr_sse(x, R, dt=VR_DT):
    """Sum of squared errors of the common reward expectation model on bins 1 to 42, and its
    analytic gradient (checked against finite differences in the notebook)."""
    n = R.shape[0]
    g, b, a, sig = _cv_unpack(x, n)
    V, Vg, Vs = fr_value(g, sig)
    gd = g ** dt
    lg = np.log(g)
    q = np.diff(V, axis=1) / dt + lg[:, None] * V[:, :-1]
    inner = gd[:, None] * q
    E = b[:, None] + a[:, None] * inner - R[:, :-1]
    W = 2 * E * a[:, None]
    GV = np.zeros_like(V)
    GV[:, :-1] += W * gd[:, None] * (lg[:, None] - 1 / dt)
    GV[:, 1:] += W * gd[:, None] / dt
    gg = ((W * (dt * g[:, None] ** (dt - 1) * q + gd[:, None] * V[:, :-1] / g[:, None])).sum(1)
          + (GV * Vg).sum(1))
    return (E ** 2).sum(), np.concatenate([gg, 2 * E.sum(1), 2 * (E * inner).sum(1), (GV * Vs).sum(0)])


def fr_constraint(x, n):
    """Code ValueConstraint.m: the mean value over neurons is at most 2 at every bin (>= 0 here)."""
    return 2 - fr_value(x[:n], x[3 * n:])[0].mean(0)


def fr_constraint_jac(x, n):
    _, Vg, Vs = fr_value(x[:n], x[3 * n:])
    J = np.zeros((VR_NBINS, len(x)))
    J[:, :n] = -Vg.T / n
    J[np.arange(VR_NBINS), 3 * n + np.arange(VR_NBINS)] = -Vs.mean(0)
    return J


def fr_fit(R, x0):
    """Constrained fit by SLSQP with analytic gradients, at most 2000 iterations as the code's
    fmincon (interior point); the optimiser is a substitute (deviation)."""
    n = R.shape[0]
    bounds = ([(0.05, 0.999999)] * n + [(0.05, 12)] * n + [(0.05, 50)] * n
              + [(0.1, 10)] * VR_NBINS)
    cons = dict(type="ineq", fun=fr_constraint, jac=fr_constraint_jac, args=(n,))
    res = optimize.minimize(fr_sse, x0, args=(R,), jac=True, method="SLSQP", bounds=bounds,
                            constraints=[cons], options=dict(maxiter=2000, ftol=1e-9))
    g, b, a, sig = _cv_unpack(res.x, n)
    return dict(gamma=g, base=b, gain=a, sigma=sig, sse=res.fun, ok=res.success, nit=res.nit,
                cmin=fr_constraint(res.x, n).min())


def _fr_job(args):
    return fr_fit(*args)


def fr_fit_halves(halves, x0, workers=4):
    """Fit each half PSTH (list of neurons x 43 arrays) from the same initial values."""
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(workers) as ex:
        fits = list(ex.map(_fr_job, [(R, x0) for R in halves]))
    return {k: np.array([f[k] for f in fits]) for k in fits[0]}


def fr_initial(n, rng):
    """Initial values of the code: gamma 0.1 + 0.8 U, baseline and gain 3 U, sigma 5 to 0.5."""
    return np.concatenate([0.1 + 0.8 * rng.random(n), 3 * rng.random(n), 3 * rng.random(n),
                           np.linspace(5, 0.5, VR_NBINS)])


# ----------------------------------------------------------------------------------------------
# Cued delay task


def cue_responses(u, win=CUE_WIN, align="VSTIM_ON"):
    """Per-trial rate in ``win`` after odor onset (claim, M1) and the trial's delay (s)."""
    on = u["events"][align]
    c, _ = counts_aligned(u["spikes"], on, win[0], win[1], win[1] - win[0])
    return c[:, 0] / (win[1] - win[0]), DELAYS[u["grp"] - 1]


def _exp(p, t):
    return p[0] + p[1] * np.exp(p[2] * t)


def _hyp(p, t):
    return p[0] + p[1] / (1 + p[2] * t)


EXP_START, EXP_LB, EXP_UB = [1, 1, -3e-4], [0, 0, -20], [50, 50, -0.0001]  # claim, M2
HYP_START, HYP_LB, HYP_UB = [1, 1, 1], [0, 0, 0], [50, 50, 20]  # claim, M2


def fit_exp(t, r):
    res = optimize.least_squares(lambda p: _exp(p, t) - r, EXP_START, bounds=(EXP_LB, EXP_UB))
    return res.x


def fit_hyp(t, r):
    res = optimize.least_squares(lambda p: _hyp(p, t) - r, HYP_START, bounds=(HYP_LB, HYP_UB))
    return res.x


def rsquare(y, f):
    """1 - residual over total sum of squares (claim, fig2f criterion). Undefined (NaN) when the
    held-out responses are all equal; a neuron's mean R2 is then taken over the other half-fits."""
    tot = ((y - y.mean()) ** 2).sum()
    return 1 - ((y - f) ** 2).sum() / tot if tot > 0 else np.nan


def draw_splits(n_trials, rng, n_boot=N_BOOT):
    """Random half splits for each neuron (claim, M2), drawn in order from one generator."""
    return [[split_halves(n, rng) for _ in range(n_boot)] for n in n_trials]


def fit_bootstraps(r, d, splits):
    """M2 for one neuron: for each split, each half fitted with both models. Returns per-half
    arrays (2 n_boot, ...) with first halves first: exponential (a, b, c), gamma, hyperbolic
    (a, b, k), held-out R2 of both models (fit of one half scored on the other), and the per-delay
    mean response of the half."""
    n_boot = len(splits)
    E = np.zeros((2, n_boot, 3))
    H = np.zeros((2, n_boot, 3))
    R2e = np.zeros((2, n_boot))
    R2h = np.zeros((2, n_boot))
    F = np.full((2, n_boot, 4), np.nan)
    for b, halves in enumerate(splits):
        for k in range(2):
            tr, te = halves[k], halves[1 - k]
            E[k, b] = fit_exp(d[tr], r[tr])
            H[k, b] = fit_hyp(d[tr], r[tr])
            R2e[k, b] = rsquare(r[te], _exp(E[k, b], d[te]))
            R2h[k, b] = rsquare(r[te], _hyp(H[k, b], d[te]))
            for j, x in enumerate(DELAYS):
                if np.any(d[tr] == x):
                    F[k, b, j] = r[tr][d[tr] == x].mean()

    def cat(x):
        return np.concatenate([x[0], x[1]], 0)

    E, H, R2e, R2h, F = map(cat, (E, H, R2e, R2h, F))
    return dict(exp=E, gamma=np.exp(E[:, 2]), hyp=H, r2_exp=R2e, r2_hyp=R2h, firing=F)


def _fit_job(args):
    return fit_bootstraps(*args)


def fit_neurons(responses, rng, workers=4):
    """M2 for every neuron: ``responses`` is a list of (rates, delays). Splits are drawn first, in
    order, from ``rng``; fits run in ``workers`` processes. Returns a dict of arrays
    (2 n_boot, neurons, ...)."""
    from concurrent.futures import ProcessPoolExecutor
    splits = draw_splits([len(r) for r, _ in responses], rng)
    with ProcessPoolExecutor(workers) as ex:
        fits = list(ex.map(_fit_job, [(r, d, s) for (r, d), s in zip(responses, splits)]))
    return {k: np.stack([f[k] for f in fits], 1) for k in fits[0]}


# ----------------------------------------------------------------------------------------------
# Decoding (claim, M4 and M5)


def decode(M, resp, alpha=ALPHA_TIKHONOV, n_comp=None):
    """Regularised SVD inverse of the discount matrix M (neurons x time), applied to the responses
    (neurons x 4 delays). n_comp None uses every component (reading a), 12 the first 12 (reading b).
    Negative values set to 0, each prediction normalised to sum 1."""
    U, s, Vt = np.linalg.svd(M, full_matrices=False)
    if n_comp is not None:
        U, s, Vt = U[:, :n_comp], s[:n_comp], Vt[:n_comp]
    filt = s ** 2 / (alpha ** 2 + s ** 2) / s
    P = (Vt.T * filt) @ (U.T @ resp)  # time x 4
    P = np.clip(P, 0, None).T
    tot = P.sum(1, keepdims=True)
    return np.where(tot > 0, P / np.where(tot > 0, tot, 1), np.nan)


def wasserstein_to_point(P, idx):
    """1-Wasserstein distance between each predicted distribution on T_GRID and the true delay at
    grid index ``idx``: the expected absolute distance. The code estimates it from 100,000 samples
    (hist2samples and ws_distance); the exact value is used here (standard; sampling error only)."""
    return (P * np.abs(T_GRID[None, :] - T_GRID[idx][:, None])).sum(1)


def single_discount_decode(resp_scaled, gamma_mean):
    """M5: t = log((r - a) / b) / log(gamma) per neuron (ratio floored at 1e-4), histogrammed with
    bin centres T_GRID (MATLAB hist), the last bin zeroed, normalised."""
    t = np.log(np.maximum(1e-4, resp_scaled)) / np.log(gamma_mean)
    edges = np.concatenate([[-np.inf], (T_GRID[1:] + T_GRID[:-1]) / 2, [np.inf]])
    out = np.zeros((resp_scaled.shape[1], len(T_GRID)))
    for d in range(resp_scaled.shape[1]):
        h = np.histogram(t[:, d], edges)[0].astype(float)
        h[-1] = 0
        out[d] = h / h.sum() if h.sum() > 0 else np.nan
    return out


def run_decoding(gam, base_for_resp, firing_test, rng, n_comp=None, matrix=None,
                 alpha=ALPHA_TIKHONOV, n_shuffle=1):
    """For each of the 2 n_boot decodings: discount matrix from ``gam`` (fits x neurons), test
    responses ``firing_test`` (fits x neurons x 4) minus ``base_for_resp`` (fits x neurons), each
    neuron scaled to its maximum over delays. Returns Wasserstein distances (fits x 4) for data and,
    for neurons shuffled in the test responses, (n_shuffle x fits x 4). Shuffle draw j takes one
    permutation per decoding, as the code (claim, M4); draw 0 is the test, the others show how much
    the draw matters. ``matrix`` may give the discount matrices directly (fits x neurons x time),
    for the hyperbolic decoder."""
    nf = gam.shape[0]
    W = np.zeros((nf, 4))
    WS = np.zeros((n_shuffle, nf, 4))
    perms = [[rng.permutation(gam.shape[1]) for _ in range(nf)] for _ in range(n_shuffle)]
    for k in range(nf):
        M = matrix[k] if matrix is not None else gam[k][:, None] ** T_GRID[None, :]
        x = firing_test[k] - base_for_resp[k][:, None]
        x = x / x.max(1, keepdims=True)
        P = decode(M, x, alpha, n_comp)
        W[k] = wasserstein_to_point(P, TRUE_IDX)
        for j in range(n_shuffle):
            WS[j, k] = wasserstein_to_point(decode(M, x[perms[j][k]], alpha, n_comp), TRUE_IDX)
    return W, WS


def signrank_less(x, y):
    """One-tailed Wilcoxon signed-rank test that x < y (MATLAB signrank, tail left), over the pairs
    where both are defined (a decoding whose predictions are all clipped to 0 has no distance)."""
    ok = np.isfinite(x) & np.isfinite(y)
    return stats.wilcoxon(x[ok], y[ok], alternative="less").pvalue
