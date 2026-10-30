"""Per-session analyses of Athalye et al. (2023) on dandiset 000404, built on bmi.py.

Each function takes one session's binned data `B` (bmi.bin_session, with the command matrix `Kc`
added) and returns the numbers the notebook aggregates. Where a parameter comes from is given in
each docstring: the claims file's shared method or a claim's criterion (which cite the paper's
Methods and code), a passage of the paper, or a standard choice for a detail that cannot change
a result.
"""

from __future__ import annotations

import numpy as np
import scipy.sparse as sp
import scipy.stats

import bmi


# ---------------------------------------------------------------- tuples and Figure 3 distances

def tuple_weights(tups, key, nbins):
    """Sparse averaging matrix: row i averages the bins tups[i][key]."""
    rows, cols, vals = [], [], []
    for i, t in enumerate(tups):
        ix = t[key]
        rows.append(np.full(len(ix), i))
        cols.append(ix)
        vals.append(np.full(len(ix), 1.0 / len(ix)))
    return sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
                         shape=(len(tups), nbins))


def fig3_distances(B, tups, Nb, nshuff, rng, null="shuffle", chunk=50, masks=None):
    """Distances between condition-specific and matched condition-pooled mean activity.

    Rates in Hz (counts x 10, plot_fr_diffs.py 1509). Population distance: L2 norm in the
    decoder-null space divided by sqrt(N) (Methods, "Condition-specific neural activity distances").
    null="shuffle": the behavior-preserving shuffle (Methods step list); null="subsample": the
    condition's size drawn from the matched pool (Statistics Summary; plot_fr_diffs.py 1630-1636).
    Returns observed per-tuple population distance (T) and neuron distances (T x N), the null
    population distances (nshuff x T), the null mean over neurons per tuple (nshuff x T), and for
    each boolean mask of tuples in `masks` the null mean over those tuples per neuron (nshuff x N).
    """
    masks = masks or {}
    X = B["spk"] * 10.0
    N = X.shape[1]
    Wc = tuple_weights(tups, "ix", len(X))
    Wp = tuple_weights(tups, "ix_pool", len(X))
    mc, mp = Wc @ X, Wp @ X
    dn = np.abs(mc - mp)
    dp = np.linalg.norm((mc - mp) @ Nb, axis=1) / np.sqrt(N)
    T = len(tups)
    null_pop = np.zeros((nshuff, T))
    null_neur_mean = {k: np.zeros((nshuff, N)) for k in masks}
    null_neur_tuple = np.zeros((nshuff, T))
    if null == "shuffle":
        lab = _cmd_labels(B)
        for s0 in range(0, nshuff, chunk):
            for s in range(s0, min(nshuff, s0 + chunk)):
                perm = _perm_within(lab, rng)
                Xs = X[perm]
                d = Wc @ Xs - Wp @ Xs
                null_pop[s] = np.linalg.norm(d @ Nb, axis=1) / np.sqrt(N)
                ad = np.abs(d)
                for k, m in masks.items():
                    null_neur_mean[k][s] = ad[m].mean(0)
                null_neur_tuple[s] = ad.mean(1)
    else:
        for i, t in enumerate(tups):
            pool = t["ix_pool"]
            n = len(t["ix"])
            Xp = X[pool]
            gm = Xp.mean(0)
            sel = np.argsort(rng.random((nshuff, len(pool))), axis=1)[:, :n]
            sub = Xp[sel].mean(1)
            d = sub - gm
            null_pop[:, i] = np.linalg.norm(d @ Nb, axis=1) / np.sqrt(N)
            ad = np.abs(d)
            for k, m in masks.items():
                if m[i]:
                    null_neur_mean[k] += ad / m.sum()
            null_neur_tuple[:, i] = ad.mean(1)
    return dict(pop=dp, neur=dn, null_pop=null_pop, null_neur_mean=null_neur_mean,
                null_neur_tuple=null_neur_tuple)


def _cmd_labels(B):
    mb, ab = bmi.command_bins(B["cmd"], B["mags"])
    return mb * 8 + ab


def _perm_within(lab, rng):
    """Permutation that moves activity only among bins with the same command bin."""
    order = np.argsort(lab, kind="stable")
    shuffled = np.lexsort((rng.random(len(lab)), lab))
    perm = np.empty(len(lab), int)
    perm[order] = shuffled
    return perm


# ---------------------------------------------------------------- command subtrajectories (Figure S1D, S1E)

def subtrajectory_distances(B, tups, nboot, rng, kind="subtraj"):
    """Methods, "Comparing command subtrajectories"; criterion of figs1d/figs1e.

    kind="subtraj": bins -5..+5 around each occurrence (occurrences within 5 bins of a trial's
    start or end left out), distance the L2 norm of the 2 x 11 difference. kind="next": the command
    in the next bin (occurrences in a trial's last bin left out), 2-D distance. The null draws the
    condition's number of eligible occurrences from the matched pool's eligible occurrences, 1000
    times. Returns per tuple (observed distance, null mean, p) for tuples with eligible data.
    """
    C = B["cmd"]
    if kind == "subtraj":
        ok = (B["bin_num"] >= 5) & (B["rev_bin_num"] >= 5)
        offs = np.arange(-5, 6)
    else:
        ok = B["rev_bin_num"] >= 1
        offs = np.array([1])
    out = []
    for t in tups:
        ic = t["ix"][ok[t["ix"]]]
        ip = t["ix_pool"][ok[t["ix_pool"]]]
        if len(ic) == 0 or len(ip) <= len(ic):
            continue
        Sc = C[ic[:, None] + offs[None, :]].reshape(len(ic), -1)
        Sp = C[ip[:, None] + offs[None, :]].reshape(len(ip), -1)
        gm = Sp.mean(0)
        dist = np.linalg.norm(Sc.mean(0) - gm)
        sel = np.argsort(rng.random((nboot, len(ip))), axis=1)[:, :len(ic)]
        nd = np.linalg.norm(Sp[sel].mean(1) - gm, axis=1)
        out.append(dict(mag=t["mag"], ang=t["ang"], cond=t["cond"], dist=dist, null=nd,
                        n_conds=t["n_conds"]))
    return out


# ---------------------------------------------------------------- dynamics models

def pair_index(B):
    """Pairs of consecutive bins within a trial (Methods, "Invariant dynamics models")."""
    return bmi.pairs_in_trials(B)


def fit_predict(Xp, Xn, train, test, alpha):
    W, b = bmi.ridge_fit(Xp[train], Xn[train], alpha)
    res = Xn[train] - (Xp[train] @ W + b)
    Sigma = np.cov(res.T)
    return W, b, Sigma, Xp[test] @ W + b


def condition(pred, Sigma, Kc, cmd):
    return bmi.condition_on_command(pred, Sigma, Kc, cmd)


def cv_models(B, alpha, fold, Kc, Nb, leave=None):
    """5-fold predictions of the full model (Methods, "Invariant dynamics model: fitting and testing").

    Returns next-activity predictions (A x_{t-1} + b), predictions conditioned on the command, the
    command-only predictions (Methods, "Predicting current activity only with command"), the fold-0
    A, and the residual covariance.
    """
    tm1, t = pair_index(B)
    Xp, Xn = B["spk"][tm1], B["spk"][t]
    cmd = B["cmd"][t]
    nxt = np.zeros_like(Xn)
    cond = np.zeros_like(Xn)
    conly = np.zeros_like(Xn)
    A0 = None
    for k in range(5):
        tr, te = fold != k, fold == k
        W, b, Sig, pred = fit_predict(Xp, Xn, tr, te, alpha)
        nxt[te] = pred
        cond[te] = condition(pred, Sig, Kc, cmd[te])
        mu = Xn[tr].mean(0)
        Sx = np.cov(Xn[tr].T)
        conly[te] = condition(np.tile(mu, (te.sum(), 1)), Sx, Kc, cmd[te])
        if k == 0:
            A0 = W.T
    return dict(tm1=tm1, t=t, next=nxt, cond=cond, conly=conly, A0=A0)


def leftout_models(B, alpha, Kc, groups, drop_pairs, groups_next=None):
    """One model per group: trained without the pairs drop_pairs[g] (boolean over pairs) and tested
    on the left-out pairs; predictions collated (Methods, "Generalization of invariant dynamics").
    The prediction of activity given the command is tested on groups[g] (pairs whose second bin is
    left out); the prediction of the next activity and command on groups_next[g] (pairs whose first
    bin, the activity the prediction starts from, is left out), or groups[g] when not given."""
    tm1, t = pair_index(B)
    Xp, Xn = B["spk"][tm1], B["spk"][t]
    cmd = B["cmd"][t]
    cond = np.full_like(Xn, np.nan)
    nxt = np.full_like(Xn, np.nan)
    groups_next = groups_next or groups
    for g in groups:
        te_c, te_n = groups[g], groups_next[g]
        tr = ~drop_pairs[g]
        te = te_c | te_n
        if te.sum() == 0 or tr.sum() < 10:
            continue
        W, b = bmi.ridge_fit(Xp[tr], Xn[tr], alpha)
        Sig = np.cov((Xn[tr] - (Xp[tr] @ W + b)).T)
        pred = Xp @ W + b
        nxt[te_n] = pred[te_n]
        cond[te_c] = condition(pred[te_c], Sig, Kc, cmd[te_c])
    return dict(cond=cond, next=nxt)


def null_dynamics(B, fold, Nb, grid=bmi.RIDGE_GRID):
    """Decoder-null dynamics (Methods, "Decoder-null dynamics model"): activity projected with
    P = Nb Nb^T, ridge chosen on the projected data, 5-fold, the session mean of the decoder-space
    part added to the predictions."""
    tm1, t = pair_index(B)
    P = Nb @ Nb.T
    Xnull = B["spk"] @ P
    pot_mean = (B["spk"] - Xnull).mean(0)
    Xp, Xn = Xnull[tm1], Xnull[t]
    a, _ = bmi.choose_alpha(Xp, Xn, fold, grid)
    pred = np.zeros_like(Xn)
    for k in range(5):
        tr, te = fold != k, fold == k
        W, b = bmi.ridge_fit(Xp[tr], Xn[tr], a)
        pred[te] = Xp[te] @ W + b
    return dict(alpha=a, next=pred + pot_mean, Xp=Xp, Xn=Xn)


def shuffle_models(B, alpha, fold, Kc, nshuff, rng, tup_stats=None):
    """Shuffle dynamics (Methods, "Shuffle dynamics model"): fit on behavior-preserving shuffles,
    tested on the real held-out data. Returns per shuffle the R2 of the conditioned prediction, of
    the next activity and of the next command, and, when tup_stats is given, the per-tuple errors
    computed by tup_stats(cond_pred, next_pred)."""
    tm1, t = pair_index(B)
    X = B["spk"]
    Xp, Xn = X[tm1], X[t]
    cmd = B["cmd"][t]
    lab = _cmd_labels(B)
    out = dict(r2_cond=np.zeros(nshuff), r2_next=np.zeros(nshuff), r2_cmd=np.zeros(nshuff), tup=[])
    for s in range(nshuff):
        perm = _perm_within(lab, rng)
        Xs = X[perm]
        Sp, Sn = Xs[tm1], Xs[t]
        cond = np.zeros_like(Xn)
        nxt = np.zeros_like(Xn)
        for k in range(5):
            tr, te = fold != k, fold == k
            W, b = bmi.ridge_fit(Sp[tr], Sn[tr], alpha)
            res = Sn[tr] - (Sp[tr] @ W + b)
            Sig = np.cov(res.T)
            pred = Xp[te] @ W + b
            nxt[te] = pred
            cond[te] = condition(pred, Sig, Kc, cmd[te])
        out["r2_cond"][s] = bmi.r2_pooled(Xn, cond)
        out["r2_next"][s] = bmi.r2_pooled(Xn, nxt)
        out["r2_cmd"][s] = bmi.r2_pooled(cmd, nxt @ Kc.T)
        if tup_stats is not None:
            out["tup"].append(tup_stats(cond, nxt))
    return out


def eig_summary(A, dt=0.1):
    """Decay time -dt/ln|lambda| and frequency |angle|/(2 pi dt) (Methods, "Dimensionality and eigenvalues")."""
    ev = np.linalg.eigvals(A)
    mod = np.abs(ev)
    with np.errstate(divide="ignore"):
        tau = -dt / np.log(mod)
    freq = np.abs(np.angle(ev)) / (2 * np.pi * dt)
    return ev, tau, freq


def p_greater(obs, null):
    """Fraction of null values at least as large as the observed (per-item p-value, code)."""
    return float((np.asarray(null) >= obs).mean())


def p_less(obs, null):
    return float((np.asarray(null) <= obs).mean())


# ---------------------------------------------------------------- per-tuple prediction statistics

CLASSES = {  # Methods, "Left-out Classes of Conditions"; generalization_plots.py 1161-1164
    "G": {"vertical": [2, 6], "horizontal": [0, 4], "diagonal 1": [1, 5], "diagonal 2": [3, 7]},
    # Monkey J: center-out targets by index, obstacle trial types as the code lists them
    "J": {"vertical": dict(co=[2, 6], obs=[2, 3, 4, 5]), "horizontal": dict(co=[0, 4], obs=[8, 9]),
          "diagonal 1": dict(co=[1, 5], obs=[6])},
}


def class_mask(B, monkey, name):
    spec = CLASSES[monkey][name]
    if monkey == "G":
        return np.isin(B["target"], spec)
    return ((B["task"] == 0) & np.isin(B["target"], spec["co"])) | ((B["task"] == 1) & np.isin(B["target"], spec["obs"]))


class TupleStats:
    """Per-tuple averages over the tuple's bins that have a prediction (bins after a trial's first)
    and over its next-command occurrences (bins before a trial's last). Used for Figures 4D-G, 5F,
    5H and S6 with the real and the shuffle models."""

    def __init__(self, B, tups, tm1, t):
        nb = len(B["spk"])
        self.N = B["spk"].shape[1]
        self.Nb = B["Nb"]
        self.Kc = B["Kc"]
        row_t = np.full(nb, -1)
        row_t[t] = np.arange(len(t))      # pair row whose second bin is the bin
        row_tm1 = np.full(nb, -1)
        row_tm1[tm1] = np.arange(len(tm1))  # pair row whose first bin is the bin
        self.keep = []
        rows_c, rows_n, rows_pn = [], [], []
        for i, tp in enumerate(tups):
            rc = row_t[tp["ix"]]
            rc = rc[rc >= 0]
            rn = row_tm1[tp["ix"]]
            rn = rn[rn >= 0]
            rp = row_tm1[tp["ix_pool"]]
            rp = rp[rp >= 0]
            if len(rc) == 0 or len(rn) == 0 or len(rp) == 0:
                continue
            self.keep.append(i)
            rows_c.append(rc)
            rows_n.append(rn)
            rows_pn.append(rp)
        self.Wc = _avg(rows_c, len(t))
        self.Wn = _avg(rows_n, len(t))
        self.Wpn = _avg(rows_pn, len(t))
        Xn = B["spk"][t]
        self.true_mean = self.Wc @ Xn * 10.0
        cmd_next = B["cmd"][t]                     # command at the second bin of each pair
        self.true_next = self.Wn @ cmd_next
        self.pool_next = self.Wpn @ cmd_next
        self.true_sign = np.sign(_cross(self.pool_next, self.true_next))
        self.true_ang = bmi.math_angle(self.pool_next, self.true_next)

    def __call__(self, cond, nxt, conly=None):
        pm = self.Wc @ cond * 10.0
        d = pm - self.true_mean
        pop = np.linalg.norm(d @ self.Nb, axis=1) / np.sqrt(self.N)
        neur = np.abs(d)
        pnext = self.Wn @ (nxt @ self.Kc.T)
        nerr = np.linalg.norm(pnext - self.true_next, axis=1)
        sign_ok = np.sign(_cross(self.pool_next, pnext)) == self.true_sign
        ang_err = np.abs(bmi.math_angle(self.pool_next, pnext) - self.true_ang)
        ang_err = np.minimum(ang_err, 360 - ang_err)
        out = dict(pop=pop, neur=neur, next_err=nerr, sign_ok=sign_ok, ang_err=ang_err, pred_mean=pm)
        return out


def _avg(rows, n):
    r = np.concatenate([np.full(len(x), i) for i, x in enumerate(rows)])
    c = np.concatenate(rows)
    v = np.concatenate([np.full(len(x), 1.0 / len(x)) for x in rows])
    return sp.csr_matrix((v, (r, c)), shape=(len(rows), n))


def _cross(a, b):
    return a[:, 0] * b[:, 1] - a[:, 1] * b[:, 0]


def component_r2(true_mean, pred_mean, conly_mean, Nb):
    """Figure 4F: R2 of the predicted condition-specific component against the true one, over
    tuples, in decoder-null coordinates (plot_pred_fr_diffs.py 1079-1081)."""
    tc = (true_mean - conly_mean) @ Nb
    pc = (pred_mean - conly_mean) @ Nb
    return 1 - ((tc - pc) ** 2).sum() / ((tc - tc.mean(0)) ** 2).sum()


def run_session(B, monkey, nshuff, seed):
    """Every per-session computation. Each analysis has its own generator derived from the seed."""
    R = {}
    N = B["spk"].shape[1]
    R["N"] = N
    tups_all = bmi.tuples(B, B["mags"])
    R["n_tuples_min15"] = len(tups_all)
    tups = [x for x in tups_all if len(x["ix_pool"]) > 0]
    R["n_tuples_dropped_match"] = len(tups_all) - len(tups)
    R["tups"] = [dict(mag=x["mag"], ang=x["ang"], cond=x["cond"], n=len(x["ix"]), n_pool=len(x["ix_pool"]),
                      n_conds=x["n_conds"]) for x in tups]
    # Figure 3, both nulls. A second pass with the same generator gives the neuron nulls over the
    # tuples significant at the population level (one of the readings of Figure 3E).
    min2 = np.array([x["n_conds"] >= 2 for x in tups])
    allm = np.ones(len(tups), bool)
    for null, sub in [("shuffle", 1), ("subsample", 2)]:
        f = fig3_distances(B, tups, B["Nb"], nshuff, np.random.default_rng([seed, 3, sub]), null,
                           masks={"all": allm, "min2": min2})
        sig = f["pop"] > np.percentile(f["null_pop"], 95, axis=0)
        f2 = fig3_distances(B, tups, B["Nb"], nshuff, np.random.default_rng([seed, 3, sub]), null,
                            masks={"sig_all": sig & allm if sig.any() else allm,
                                   "sig_min2": sig & min2 if (sig & min2).any() else min2})
        f["null_neur_mean"].update(f2["null_neur_mean"])
        f["sig"] = sig
        R["f3_" + null] = f
    # Figure S1D, S1E
    R["s1d"] = subtrajectory_distances(B, tups, 1000, np.random.default_rng([seed, 1, 4]), "subtraj")
    R["s1e"] = subtrajectory_distances(B, tups, 1000, np.random.default_rng([seed, 1, 5]), "next")
    # dynamics
    tm1, t = pair_index(B)
    fold = bmi.folds(len(t), B["task"][t], seed=0)
    Xp, Xn = B["spk"][tm1], B["spk"][t]
    alpha, _ = bmi.choose_alpha(Xp, Xn, fold)
    R["alpha"] = alpha
    cv = cv_models(B, alpha, fold, B["Kc"], B["Nb"])
    cmd_t = B["cmd"][t]
    R["r2"] = dict(cond=bmi.r2_pooled(Xn, cv["cond"]), next=bmi.r2_pooled(Xn, cv["next"]),
                   cmd=bmi.r2_pooled(cmd_t, cv["next"] @ B["Kc"].T), conly=bmi.r2_pooled(Xn, cv["conly"]))
    mb, ab = bmi.command_bins(B["cmd"], B["mags"])
    mb_t, ab_t, mb_p, ab_p = mb[t], ab[t], mb[tm1], ab[tm1]
    # Two readings of which pairs an R2 is scored on: "all" pairs, or "analysed" commands only
    # (Methods, "Command discretization": commands above the 95th percentile of magnitude are not
    # analysed), the command at t for predictions given the command and at t-1 for next predictions.
    an_c, an_n = mb_t < 4, mb_p < 4
    R["pair_masks"] = {"analysed_cond": an_c, "analysed_next": an_n}
    tab = {}

    def score(model, cond, nxt, test_c, test_n):
        for reading, sel_c, sel_n in [("all", None, None), ("analysed", an_c, an_n)]:
            mc = None if test_c is None else (test_c if sel_c is None else test_c & sel_c)
            mn = None if test_n is None else (test_n if sel_n is None else test_n & sel_n)
            if cond is not None and mc.sum() > 0:
                tab[(model, "cond", reading)] = bmi.r2_pooled(Xn[mc], cond[mc])
            if nxt is not None and mn.sum() > 0:
                tab[(model, "next", reading)] = bmi.r2_pooled(Xn[mn], nxt[mn])
                tab[(model, "cmd", reading)] = bmi.r2_pooled(cmd_t[mn], nxt[mn] @ B["Kc"].T)
    allp = np.ones(len(t), bool)
    score("full", cv["cond"], cv["next"], allp, allp)
    # left out command: transitions to and from the command are left out of training (Figure S4A legend)
    groups, groups_n, drops = {}, {}, {}
    for m in range(4):
        for a in range(8):
            g_t = (mb_t == m) & (ab_t == a)
            g_p = (mb_p == m) & (ab_p == a)
            groups[(m, a)], groups_n[(m, a)], drops[(m, a)] = g_t, g_p, g_t | g_p
    lo = leftout_models(B, alpha, B["Kc"], groups, drops, groups_n)
    score("command left out", lo["cond"], lo["next"], np.isfinite(lo["cond"][:, 0]), np.isfinite(lo["next"][:, 0]))
    groups, drops = {}, {}
    for c in np.unique(B["cond"]):
        g = B["cond"][t] == c
        groups[c], drops[c] = g, g
    lo = leftout_models(B, alpha, B["Kc"], groups, drops)
    score("condition left out", lo["cond"], lo["next"], np.isfinite(lo["cond"][:, 0]), np.isfinite(lo["next"][:, 0]))
    groups, drops = {}, {}
    for a in range(8):
        g = (ab_t == a) & (mb_t < 4)
        groups[a], drops[a] = g, g | ((ab_p == a) & (mb_p < 4))
    lo = leftout_models(B, alpha, B["Kc"], groups, drops)
    score("angle bin left out", lo["cond"], None, np.isfinite(lo["cond"][:, 0]), None)
    groups, drops = {}, {}
    for m in range(4):
        g = mb_t == m
        groups[m], drops[m] = g, g | (mb_p == m)
    lo = leftout_models(B, alpha, B["Kc"], groups, drops)
    score("magnitude bin left out", lo["cond"], None, np.isfinite(lo["cond"][:, 0]), None)
    R["class_pairs"] = {}
    for name in CLASSES[monkey]:
        g = class_mask(B, monkey, name)[t]
        if g.sum() == 0:
            continue
        lo = leftout_models(B, alpha, B["Kc"], {name: g}, {name: g})
        score(name, lo["cond"], None, g, None)
        R["class_pairs"][name] = int(g.sum())
    # decoder-null dynamics
    nd = null_dynamics(B, fold, B["Nb"])
    R["null_alpha"] = nd["alpha"]
    score("decoder-null", None, nd["next"], allp, allp)
    R["r2tab"] = tab
    # in-sample fits for eigenvalues (Figure S3)
    W, b = bmi.ridge_fit(Xp, Xn, alpha)
    R["A_full"] = W.T
    W2, _ = bmi.ridge_fit(nd["Xp"], nd["Xn"], nd["alpha"])
    R["A_null"] = W2.T
    # Figure 5D: eigenvector dimensions of the fold-0 A
    R["dims_r2"] = eig_dims_r2(cv["A0"], Xn, cv["next"])
    # Figure S3F: held-out residual norm per pair
    R["resid"] = np.linalg.norm(Xn - cv["next"], axis=1) / np.sqrt(N)
    R["resid_trl"], R["resid_bin"] = B["trl"][t], B["bin_num"][t]
    # tuple statistics, real model
    ts = TupleStats(B, tups, tm1, t)
    R["ts_keep"] = ts.keep
    real = ts(cv["cond"], cv["next"])
    R["ts_real"] = {k: v for k, v in real.items()}
    R["conly_mean"] = ts.Wc @ cv["conly"] * 10.0
    R["true_mean"] = ts.true_mean
    R["true_next"], R["pool_next"] = ts.true_next, ts.pool_next
    # shuffle models
    rng = np.random.default_rng([seed, 4, 1])

    sig = R["f3_shuffle"]["sig"][ts.keep]
    R["ts_masks"] = {"all": np.ones(len(ts.keep), bool), "sig": sig}
    sh = _shuffle_with_stats(B, alpha, fold, nshuff, rng, ts, R)
    R["shuffle"] = sh
    # shuffle-model ridge reading (a): the parameter selected on one shuffled dataset
    perm = _perm_within(_cmd_labels(B), np.random.default_rng([seed, 4, 2]))
    Xs = B["spk"][perm]
    R["alpha_shuffle"], _ = bmi.choose_alpha(Xs[tm1], Xs[t], fold)
    # reading (a) run with 200 shuffles (R2 only), as a variant of the 1000-shuffle reading (b)
    if R["alpha_shuffle"] != alpha:
        R["shuffle_a"] = shuffle_models(B, R["alpha_shuffle"], fold, B["Kc"], min(200, nshuff), np.random.default_rng([seed, 4, 3]))
    else:
        R["shuffle_a"] = None
    # behavior-encoding models (Figure S5B)
    R["s5b"] = behavior_models(B, monkey, tm1, t, fold)
    # pairs of conditions (Figure S6)
    R["pairs"] = pairwise(B, tups, ts, real, cv)
    return R


def _shuffle_with_stats(B, alpha, fold, nshuff, rng, ts, R):
    tm1, t = pair_index(B)
    X = B["spk"]
    Xp, Xn = X[tm1], X[t]
    cmd = B["cmd"][t]
    lab = _cmd_labels(B)
    T = len(ts.keep)
    N = X.shape[1]
    out = dict(r2_cond=np.zeros(nshuff), r2_next=np.zeros(nshuff), r2_cmd=np.zeros(nshuff),
               pop=np.zeros((nshuff, T)), neur_tuple=np.zeros((nshuff, T)), next_err=np.zeros((nshuff, T)),
               sign_ok=np.zeros((nshuff, T), bool), ang_err=np.zeros((nshuff, T)),
               comp_r2={k: np.zeros(nshuff) for k in R["ts_masks"]},
               neur_by_neuron={k: np.zeros((nshuff, N)) for k in R["ts_masks"]},
               analysed={m: np.zeros(nshuff) for m in ("cond", "next", "cmd")})
    Kc = B["Kc"]
    for s in range(nshuff):
        perm = _perm_within(lab, rng)
        Xs = X[perm]
        Sp, Sn = Xs[tm1], Xs[t]
        cond = np.zeros_like(Xn)
        nxt = np.zeros_like(Xn)
        for k in range(5):
            tr, te = fold != k, fold == k
            W, b = bmi.ridge_fit(Sp[tr], Sn[tr], alpha)
            res = Sn[tr] - (Sp[tr] @ W + b)
            Sig = np.cov(res.T)
            pred = Xp[te] @ W + b
            nxt[te] = pred
            cond[te] = condition(pred, Sig, Kc, cmd[te])
        out["r2_cond"][s] = bmi.r2_pooled(Xn, cond)
        out["r2_next"][s] = bmi.r2_pooled(Xn, nxt)
        out["r2_cmd"][s] = bmi.r2_pooled(cmd, nxt @ Kc.T)
        mc, mn = R["pair_masks"]["analysed_cond"], R["pair_masks"]["analysed_next"]
        out["analysed"]["cond"][s] = bmi.r2_pooled(Xn[mc], cond[mc])
        out["analysed"]["next"][s] = bmi.r2_pooled(Xn[mn], nxt[mn])
        out["analysed"]["cmd"][s] = bmi.r2_pooled(cmd[mn], nxt[mn] @ Kc.T)
        o = ts(cond, nxt)
        out["pop"][s] = o["pop"]
        out["neur_tuple"][s] = o["neur"].mean(1)
        out["next_err"][s] = o["next_err"]
        out["sign_ok"][s] = o["sign_ok"]
        out["ang_err"][s] = o["ang_err"]
        for k, m in R["ts_masks"].items():
            out["comp_r2"][k][s] = component_r2(ts.true_mean[m], o["pred_mean"][m], R["conly_mean"][m], B["Nb"]) if m.sum() > 1 else np.nan
            out["neur_by_neuron"][k][s] = o["neur"][m].mean(0) if m.any() else np.nan
    return out


def eig_dims_r2(A, Xn, pred):
    """Figure 5D: true and predicted activity projected onto the eigenvectors of A (complex pairs
    split into real and imaginary parts, projection by the pseudo-inverse; generalization_plots.py
    2116-2195), R2 per dimension, sorted from high to low."""
    ev, V = np.linalg.eig(A)
    cols, done = [], set()
    for i in range(len(ev)):
        if i in done:
            continue
        if abs(ev[i].imag) > 1e-10:
            j = [k for k in range(len(ev)) if k not in done and k != i and abs(ev[k] - np.conj(ev[i])) < 1e-8]
            cols.extend([V[:, i].real, V[:, i].imag])
            done.add(i)
            if j:
                done.add(j[0])
        else:
            cols.append(V[:, i].real)
            done.add(i)
    E = np.array(cols).T
    P = np.linalg.pinv(E)
    yt, yp = Xn @ P.T, pred @ P.T
    r2 = 1 - ((yt - yp) ** 2).sum(0) / ((yt - yt.mean(0)) ** 2).sum(0)
    return np.sort(r2)[::-1]


def behavior_models(B, monkey, tm1, t, fold):
    """Figure S5B (Methods, "Estimation of behavior-encoding models"): activity at t from the command
    at t, cursor position and velocity at t-1, target position (the cursor at reward, which lies in
    the target) and one-hot target and task, z-scored, ridge with the cross-validated parameter;
    and the same plus activity at t-1. Held-out R2 pooled over neurons."""
    last = {}
    for tr in np.unique(B["trl"]):
        last[tr] = B["pos"][np.where(B["trl"] == tr)[0][-1]]
    tpos = np.vstack([last[x] for x in B["trl"][t]])
    cats = np.array([f"{a}_{b}" for a, b in zip(B["cond"][t], B["task"][t])])
    onehot = (cats[:, None] == np.unique(cats)[None, :]).astype(float)
    beh = np.hstack([B["cmd"][t], B["pos"][tm1], B["vel"][tm1], tpos, onehot])
    Xn = B["spk"][t]
    out = {}
    for name, Xb in [("behavior", beh), ("behavior_plus_dynamics", np.hstack([beh, B["spk"][tm1]]))]:
        sd = Xb.std(0)
        sd[sd == 0] = 1
        Z = (Xb - Xb.mean(0)) / sd
        a, r2 = bmi.choose_alpha(Z, Xn, fold)
        out[name] = r2
        out[name + "_alpha"] = a
    return out


def pairwise(B, tups, ts, real, cv):
    """Figure S6: for each command, each pair of conditions with 15 or more occurrences: true and
    predicted distances between the conditions' mean activity (per neuron, Hz, and the population
    in the decoder-null space over sqrt(N)), between mean next commands (true and predicted), and
    between command subtrajectories (2 x 11, occurrences away from trial edges)."""
    N = B["spk"].shape[1]
    keep = ts.keep
    tk = [tups[i] for i in keep]
    true_m, pred_m = ts.true_mean, real["pred_mean"]
    pnext = ts.Wn @ (cv["next"] @ B["Kc"].T)
    tnext = ts.true_next
    C = B["cmd"]
    ok = (B["bin_num"] >= 5) & (B["rev_bin_num"] >= 5)
    offs = np.arange(-5, 6)
    sub = []
    for x in tk:
        ic = x["ix"][ok[x["ix"]]]
        sub.append(C[ic[:, None] + offs[None, :]].reshape(len(ic), -1).mean(0) if len(ic) else None)
    rows = []
    bycmd = {}
    for i, x in enumerate(tk):
        bycmd.setdefault((x["mag"], x["ang"]), []).append(i)
    for cmdk, idx in bycmd.items():
        nconds = len(idx)
        for a in range(len(idx)):
            for b2 in range(a + 1, len(idx)):
                i, j = idx[a], idx[b2]
                rows.append(dict(
                    command=f"{cmdk[0]}_{cmdk[1]}", n_conds=nconds,
                    neur_true=np.abs(true_m[i] - true_m[j]), neur_pred=np.abs(pred_m[i] - pred_m[j]),
                    pop_true=np.linalg.norm((true_m[i] - true_m[j]) @ B["Nb"]) / np.sqrt(N),
                    pop_pred=np.linalg.norm((pred_m[i] - pred_m[j]) @ B["Nb"]) / np.sqrt(N),
                    next_true=np.linalg.norm(tnext[i] - tnext[j]), next_pred=np.linalg.norm(pnext[i] - pnext[j]),
                    beh=(np.linalg.norm(sub[i] - sub[j]) if sub[i] is not None and sub[j] is not None else np.nan)))
    return rows
