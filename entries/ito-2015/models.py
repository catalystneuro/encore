"""Choice models of Ito & Doya (2015), Fig. 2G, and the regression of Figs. 7 and 8.

The paper's model equations are images missing from its text; the forms here follow the
claims file (opening comment, O8) and the words around the equations (Methods, "DFQ-learning
model"):

- DFQ update: the chosen action's value moves toward kappa1 after a reward and toward -kappa2
  after no reward with rate alpha1; the unchosen value decays toward 0 with rate alpha2. Q
  learning is alpha2 = kappa2 = 0, FQ learning alpha1 = alpha2. P(left) = 1 / (1 + exp(-(QL -
  QR))). Initial Q values are 0 in each session (a standard choice; the paper refers to Ito and
  Doya, 2009).
- Constant-parameter models: alpha in [0, 1] and kappa in [0, 10], one set for all training
  sessions, fitted by maximum likelihood (L-BFGS-B from several starts; the bounds are a
  standard choice).
- Time-varying models: the parameters follow Gaussian random walks with SDs sigma_alpha and
  sigma_kappa (Methods); a particle filter of 5000 particles (Methods) estimates the predictive
  distribution of [QL, QR, alpha, kappa]; P(left) uses the means of the predictive QL and QR
  (Methods). The initial particles are drawn from alpha ~ U(0, 1) and kappa ~ U(0, 5), and alpha
  and kappa are clipped to their ranges after each step: an assumption, as the paper refers
  the priors to Ito and Doya (2009). sigma_alpha and sigma_kappa are chosen on a grid by the
  likelihood of the training sessions (the paper says they are free parameters).
- Markov model of order d: P(left | the last d experiences) for every experience sequence,
  estimated from training counts with one pseudo-count per action (a standard choice, so that
  unseen sequences give 0.5); the first trials of a session use the available shorter history.
- Actor-critic (Sutton and Barto, 1998), one state and two actions: delta = r - V, V += a_c
  delta, preference of the chosen action += a_a delta, P(left) = 1 / (1 + exp(-beta (pL - pR))),
  with (a) a_c = a_a or (b) separate rates (claims file, actor-critic-near-chance).
- Normalized likelihood: the geometric mean of the per-trial likelihoods of the observed
  choices, 0.5 at chance (claims file reading of the missing formula).
"""
import numpy as np
from scipy.optimize import minimize


def sig(x):
    return 1.0 / (1.0 + np.exp(-x))


# ---------------------------------------------------------------- constant-parameter Q models
def q_loglik(params, kind, a, r):
    """Per-trial log-likelihoods of choices a (1 left, 0 right) with rewards r, one session."""
    if kind == "Q":
        a1, k1 = params; a2, k2 = 0.0, 0.0
    elif kind == "FQ":
        a1, k1, k2 = params; a2 = a1
    else:
        a1, a2, k1, k2 = params
    QL = QR = 0.0
    out = np.empty(len(a))
    for t in range(len(a)):
        p = sig(QL - QR)
        p = min(max(p, 1e-12), 1 - 1e-12)
        out[t] = np.log(p if a[t] else 1 - p)
        tgt = k1 if r[t] else -k2
        if a[t]:
            QL = QL + a1 * (tgt - QL); QR = (1 - a2) * QR
        else:
            QR = QR + a1 * (tgt - QR); QL = (1 - a2) * QL
    return out


Q_BOUNDS = {"Q": [(0, 1), (0, 10)], "FQ": [(0, 1), (0, 10), (0, 10)],
            "DFQ": [(0, 1), (0, 1), (0, 10), (0, 10)]}


def fit_const(kind, sessions, rng, n_start=6, loglik=None, bounds=None):
    """ML fit of one parameter set over sessions [(a, r), ...]."""
    loglik = loglik or (lambda p, a, r: q_loglik(p, kind, a, r))
    bounds = bounds or Q_BOUNDS[kind]
    def nll(p):
        return -sum(loglik(p, a, r).sum() for a, r in sessions)
    best = None
    for _ in range(n_start):
        x0 = [rng.uniform(lo, min(hi, 3)) for lo, hi in bounds]
        res = minimize(nll, x0, method="L-BFGS-B", bounds=bounds)
        if best is None or res.fun < best.fun:
            best = res
    return best.x, -best.fun


# ---------------------------------------------------------------- actor-critic
def ac_loglik(params, shared, a, r):
    if shared:
        al, beta = params; ac = aa = al
    else:
        ac, aa, beta = params
    V = pL = pR = 0.0
    out = np.empty(len(a))
    for t in range(len(a)):
        p = sig(beta * (pL - pR))
        p = min(max(p, 1e-12), 1 - 1e-12)
        out[t] = np.log(p if a[t] else 1 - p)
        d = r[t] - V
        V += ac * d
        if a[t]:
            pL += aa * d
        else:
            pR += aa * d
    return out


AC_BOUNDS = {True: [(0, 1), (0, 50)], False: [(0, 1), (0, 1), (0, 50)]}


# ---------------------------------------------------------------- particle filter
def pf_session(kind, a, r, s_alpha, s_kappa, rng, n=5000, return_q=False):
    """Particle filter for a time-varying Q, FQ or DFQ model over one session.

    Returns per-trial log-likelihoods of the choices and, optionally, the predictive means of
    QL and QR before each trial."""
    QL = np.zeros(n); QR = np.zeros(n)
    a1 = rng.uniform(0, 1, n); a2 = rng.uniform(0, 1, n) if kind == "DFQ" else None
    k1 = rng.uniform(0, 5, n); k2 = rng.uniform(0, 5, n) if kind != "Q" else None
    ll = np.empty(len(a)); mq = np.empty((len(a), 2))
    for t in range(len(a)):
        mL, mR = QL.mean(), QR.mean()
        mq[t] = mL, mR
        p = sig(mL - mR)
        ll[t] = np.log(p if a[t] else 1 - p)
        w = sig(QL - QR) if a[t] else sig(QR - QL)
        w = w / w.sum()
        idx = np.searchsorted(np.cumsum(w), (rng.random() + np.arange(n)) / n).clip(0, n - 1)
        QL, QR, a1, k1 = QL[idx], QR[idx], a1[idx], k1[idx]
        if a2 is not None:
            a2 = a2[idx]
        if k2 is not None:
            k2 = k2[idx]
        alpha2 = a1 if kind == "FQ" else (a2 if kind == "DFQ" else 0.0)
        kap2 = k2 if k2 is not None else 0.0
        tgt = k1 if r[t] else -kap2
        if a[t]:
            QL = QL + a1 * (tgt - QL); QR = (1 - alpha2) * QR
        else:
            QR = QR + a1 * (tgt - QR); QL = (1 - alpha2) * QL
        if s_alpha > 0:
            a1 = np.clip(a1 + rng.normal(0, s_alpha, n), 0, 1)
            if a2 is not None:
                a2 = np.clip(a2 + rng.normal(0, s_alpha, n), 0, 1)
        if s_kappa > 0:
            k1 = np.clip(k1 + rng.normal(0, s_kappa, n), 0, None)
            if k2 is not None:
                k2 = np.clip(k2 + rng.normal(0, s_kappa, n), 0, None)
    return (ll, mq) if return_q else ll


# ---------------------------------------------------------------- Markov models
def markov_fit(d, sessions):
    counts = {}
    for a, r in sessions:
        e = [f"{x}{y}" for x, y in zip(a, r)]
        for t in range(len(a)):
            for dd in range(0, d + 1):
                if t - dd < 0:
                    break
                key = (dd, tuple(e[t - dd:t]))
                c = counts.setdefault(key, [0, 0]); c[0 if a[t] else 1] += 1
    return counts


def markov_loglik(d, counts, a, r):
    e = [f"{x}{y}" for x, y in zip(a, r)]
    out = np.empty(len(a))
    for t in range(len(a)):
        dd = min(d, t)
        nl, nr = counts.get((dd, tuple(e[t - dd:t])), [0, 0])
        p = (nl + 1) / (nl + nr + 2)
        p = min(max(p, 1e-12), 1 - 1e-12)
        out[t] = np.log(p if a[t] else 1 - p)
    return out


def norm_lik(ll):
    """Geometric mean of the per-trial likelihoods."""
    return float(np.exp(np.mean(ll)))


# ---------------------------------------------------------------- regression with BIC selection
def bic_select(X, Y, names, always=("const",)):
    """For each column of Y, the subset of X's columns with the smallest BIC (columns in
    ``always`` kept in every subset), then the coefficients and two-sided t-test p-values of the
    selected model. BIC = N ln(RSS / N) + k ln N (Methods, Regression analysis).

    Returns a list (one per column of Y) of dicts name -> (coef, p) for the selected terms."""
    from scipy import stats
    N, P = X.shape
    fixed = [i for i, n in enumerate(names) if n in always]
    free = [i for i in range(P) if i not in fixed]
    best_bic = np.full(Y.shape[1], np.inf); best = [None] * Y.shape[1]
    for m in range(2 ** len(free)):
        cols = fixed + [free[j] for j in range(len(free)) if m >> j & 1]
        if not cols:
            continue
        Xs = X[:, cols]
        beta, _, rank, _ = np.linalg.lstsq(Xs, Y, rcond=None)
        if rank < len(cols):
            continue
        rss = ((Y - Xs @ beta) ** 2).sum(0)
        bic = N * np.log(np.maximum(rss, 1e-12) / N) + len(cols) * np.log(N)
        better = bic < best_bic
        for j in np.where(better)[0]:
            best[j] = cols
        best_bic = np.where(better, bic, best_bic)
    out = []
    for j, cols in enumerate(best):
        Xs = X[:, cols]
        beta, _, _, _ = np.linalg.lstsq(Xs, Y[:, j], rcond=None)
        res = Y[:, j] - Xs @ beta
        dof = N - len(cols)
        s2 = (res ** 2).sum() / dof
        cov = s2 * np.linalg.pinv(Xs.T @ Xs)
        se = np.sqrt(np.maximum(np.diag(cov), 1e-300))
        tval = beta / se
        p = 2 * stats.t.sf(np.abs(tval), dof)
        out.append({names[c]: (beta[i], p[i]) for i, c in enumerate(cols)})
    return out
