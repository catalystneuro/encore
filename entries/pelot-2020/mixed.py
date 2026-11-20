"""Linear mixed models fitted by REML, with type III F tests and Tukey's HSD on
least squares means, for the mixed model ANOVAs of Pelot et al. (2020).

The paper's model (Methods, Statistics and Data Analyses): fixed effects
species, level and their interaction, a random effect of subject, and for
fascicle diameter a further random effect of sample, fitted in JMP Pro 14.3.0,
followed by Tukey's HSD. Details the paper does not state, and the choices made
here:

- Estimation by REML, JMP's method for models with random effects.
- Variance components either unbounded (JMP's Fit Model default, which
  allows a negative estimate) or bounded at zero; the claims file asks for both
  readings (nerve-diameter-anova), and `fit(..., bounded=)` selects one.
- Effect (sum-to-zero) coding of the fixed effects, as JMP codes nominal
  effects, so that the type III tests of main effects are those JMP prints.
- Denominator degrees of freedom by Satterthwaite's approximation (Fai and
  Cornelius 1996 for multi-df tests), from the numerical Hessian of the REML
  likelihood. JMP uses Kenward-Roger, which no Python package available here
  implements; the two coincide for balanced designs and differ little
  otherwise. This is an assumption, stated in the notebook.
- Tukey's HSD on least squares means: each pairwise difference over its
  standard error, referred to the studentized range for the number of means
  compared, with that difference's Satterthwaite degrees of freedom.
"""
import itertools

import numpy as np
import pandas as pd
from scipy import optimize, stats


def effect_coding(levels, values):
    """Columns coding a nominal factor with sum-to-zero contrasts (JMP's coding):
    level i < k-1 gets +1 in column i, the last level -1 in every column."""
    k = len(levels)
    m = np.zeros((len(values), k - 1))
    for i, v in enumerate(values):
        j = levels.index(v)
        if j < k - 1:
            m[i, j] = 1
        else:
            m[i, :] = -1
    return m


class Design:
    """Fixed-effect design for factors a (e.g. species) and b (level), main
    effects and interaction, with the columns of each term."""

    def __init__(self, df, a, b, a_levels, b_levels, interaction=True):
        self.a, self.b = a, b
        self.a_levels, self.b_levels = a_levels, b_levels
        self.interaction = interaction
        self.X, self.terms = self.build(df)

    def build(self, df):
        A = effect_coding(self.a_levels, list(df[self.a]))
        B = effect_coding(self.b_levels, list(df[self.b]))
        cols = [np.ones((len(df), 1)), A, B]
        terms = {"Intercept": [0]}
        terms[self.a] = list(range(1, 1 + A.shape[1]))
        terms[self.b] = list(range(1 + A.shape[1], 1 + A.shape[1] + B.shape[1]))
        if self.interaction:
            AB = np.einsum("ni,nj->nij", A, B).reshape(len(df), -1)
            start = 1 + A.shape[1] + B.shape[1]
            terms[f"{self.a}*{self.b}"] = list(range(start, start + AB.shape[1]))
            cols.append(AB)
        return np.hstack(cols), terms

    def row(self, a_val=None, b_val=None):
        """Row of the design for a cell (a_val, b_val); None averages over the
        factor's levels (least squares means, equal weights, as JMP)."""
        avals = self.a_levels if a_val is None else [a_val]
        bvals = self.b_levels if b_val is None else [b_val]
        rows = []
        for x, y in itertools.product(avals, bvals):
            d = pd.DataFrame({self.a: [x], self.b: [y]})
            rows.append(self.build(d)[0][0])
        return np.mean(rows, axis=0)


class MixedFit:
    pass


def _incidence(groups):
    codes, uniq = pd.factorize(pd.Series(groups))
    Z = np.zeros((len(groups), len(uniq)))
    Z[np.arange(len(groups)), codes] = 1
    return Z


def fit(df, y, design, random, bounded=True):
    """REML fit of y ~ design.X with random intercepts for each column name in
    `random` (e.g. ["subject"] or ["subject", "sample"]).

    bounded: variance components constrained to be >= 0 (True) or free, as long
    as the covariance matrix stays positive definite (False)."""
    yv = df[y].to_numpy(float)
    X = design.X
    n, p = X.shape
    G = [_incidence(df[r].to_numpy()) @ _incidence(df[r].to_numpy()).T for r in random]

    def V_of(theta):
        # theta = [log sigma2, tau2_1, ..., tau2_r]
        V = np.exp(theta[0]) * np.eye(n)
        for t, g in zip(theta[1:], G):
            V = V + t * g
        return V

    def nll(theta):
        V = V_of(theta)
        try:
            L = np.linalg.cholesky(V)
        except np.linalg.LinAlgError:
            return 1e10
        Li = np.linalg.solve(L, np.eye(n))
        Vi = Li.T @ Li
        XtVi = X.T @ Vi
        A = XtVi @ X
        try:
            LA = np.linalg.cholesky(A)
        except np.linalg.LinAlgError:
            return 1e10
        beta = np.linalg.solve(A, XtVi @ yv)
        r = yv - X @ beta
        return 0.5 * (2 * np.log(np.diag(L)).sum() + 2 * np.log(np.diag(LA)).sum()
                      + r @ Vi @ r)

    s0 = np.var(yv - X @ np.linalg.lstsq(X, yv, rcond=None)[0])
    best = None
    for frac in (0.1, 0.5, 0.9):
        th0 = np.r_[np.log(s0 * (1 - frac)), [s0 * frac / len(G)] * len(G)]
        bnds = [(None, None)] + [((0.0, None) if bounded else (None, None))] * len(G)
        res = optimize.minimize(nll, th0, method="L-BFGS-B", bounds=bnds)
        res2 = optimize.minimize(nll, res.x, method="Nelder-Mead" if not bounded else "L-BFGS-B",
                                 bounds=None if not bounded else bnds,
                                 options={"maxiter": 4000, "xatol": 1e-10, "fatol": 1e-12}
                                 if not bounded else {})
        r_ = res2 if res2.fun <= res.fun else res
        if best is None or r_.fun < best.fun:
            best = r_
    if bounded:
        # candidates with each subset of components at the bound, the other
        # parameters re-optimised (L-BFGS-B can stop short of the boundary)
        for mask in itertools.product([False, True], repeat=len(G)):
            if not any(mask):
                continue
            free = [0] + [i + 1 for i, m in enumerate(mask) if not m]

            def sub(t, free=free):
                th = np.zeros(len(G) + 1)
                th[free] = t
                return nll(th)
            x0 = best.x[free].copy()
            x0[1:] = np.maximum(x0[1:], s0 * 0.01)
            r_ = optimize.minimize(sub, x0, method="L-BFGS-B",
                                   bounds=[(None, None)] + [(0.0, None)] * (len(free) - 1),
                                   options={"ftol": 1e-14, "gtol": 1e-10})
            if r_.fun < best.fun - 1e-9:
                th = np.zeros(len(G) + 1)
                th[free] = r_.x
                best = optimize.OptimizeResult(x=th, fun=r_.fun)
    theta = best.x
    f = MixedFit()
    f.design, f.theta, f.nll, f.random, f.bounded, f.n = design, theta, best.fun, random, bounded, n
    f.sigma2 = float(np.exp(theta[0]))
    f.tau2 = dict(zip(random, map(float, theta[1:])))
    f.C, f.beta = _gls(V_of(theta), X, yv)
    f._Cfun = lambda th: _gls(V_of(th), X, yv)[0]
    # components at the bound are held fixed (no sampling variance) in the
    # Satterthwaite approximation, as for a component dropped from the model
    f.at_bound = [bool(bounded and t <= 1e-8 * s0) for t in theta[1:]]
    keep = [0] + [i + 1 for i, b in enumerate(f.at_bound) if not b]
    W = np.zeros((len(theta), len(theta)))

    def nll_free(t):
        th = theta.copy()
        th[keep] = t
        return nll(th)
    W[np.ix_(keep, keep)] = _theta_cov(nll_free, theta[keep])
    f.W = W
    return f


def _gls(V, X, y):
    Vi = np.linalg.inv(V)
    C = np.linalg.inv(X.T @ Vi @ X)
    return C, C @ X.T @ Vi @ y


def _theta_cov(nll, theta, h=1e-4):
    """Asymptotic covariance of the variance parameters: inverse of the
    numerical Hessian of the REML negative log-likelihood."""
    k = len(theta)
    H = np.zeros((k, k))
    steps = h * np.maximum(1.0, np.abs(theta))
    for i in range(k):
        for j in range(i, k):
            ei = np.zeros(k); ei[i] = steps[i]
            ej = np.zeros(k); ej[j] = steps[j]
            H[i, j] = H[j, i] = (nll(theta + ei + ej) - nll(theta + ei - ej)
                                 - nll(theta - ei + ej) + nll(theta - ei - ej)) / (4 * steps[i] * steps[j])
    try:
        return np.linalg.pinv(H)
    except np.linalg.LinAlgError:
        return np.full((k, k), np.nan)


def _df_contrast(f, l, h=1e-5):
    """Satterthwaite degrees of freedom for the 1-df contrast l'beta."""
    var = float(l @ f.C @ l)
    g = np.zeros(len(f.theta))
    for i in range(len(f.theta)):
        e = np.zeros(len(f.theta)); e[i] = h * max(1.0, abs(f.theta[i]))
        g[i] = (float(l @ f._Cfun(f.theta + e) @ l) - float(l @ f._Cfun(f.theta - e) @ l)) / (2 * e[i])
    den = float(g @ f.W @ g)
    return 2 * var ** 2 / den if den > 0 else np.inf


def ftest(f, term):
    """Type III Wald F test of a term, with Fai-Cornelius Satterthwaite df."""
    idx = f.design.terms[term]
    L = np.zeros((len(idx), len(f.beta)))
    for r, c in enumerate(idx):
        L[r, c] = 1
    M = L @ f.C @ L.T
    b = L @ f.beta
    q = len(idx)
    F = float(b @ np.linalg.solve(M, b)) / q
    w, P = np.linalg.eigh(M)
    nus = [_df_contrast(f, P[:, i] @ L) for i in range(q)]
    E = sum(nu / (nu - 2) for nu in nus if nu > 2)
    if E > q and all(nu > 2 for nu in nus):
        ddf = 2 * E / (E - q)
    else:
        ddf = float(np.mean(nus))
    return dict(term=term, F=F, df_num=q, df_den=ddf, p=float(stats.f.sf(F, q, ddf)))


def anova(f):
    rows = [ftest(f, t) for t in f.design.terms if t != "Intercept"]
    return pd.DataFrame(rows)


def lsmeans(f, by):
    """Least squares means of a factor ('a', 'b') or of the cells ('ab')."""
    d = f.design
    out = []
    if by == "a":
        keys = [(x, None) for x in d.a_levels]
    elif by == "b":
        keys = [(None, y) for y in d.b_levels]
    else:
        keys = list(itertools.product(d.a_levels, d.b_levels))
    for x, y in keys:
        l = d.row(x, y)
        out.append(dict(a=x, b=y, lsmean=float(l @ f.beta), se=float(np.sqrt(l @ f.C @ l)), l=l))
    return out


def tukey(f, by, df=None):
    """Tukey's HSD over the least squares means of `by` ('a', 'b' or 'ab').
    `df` replaces the Satterthwaite degrees of freedom by a fixed value (a
    variant, e.g. containment degrees of freedom)."""
    m = lsmeans(f, by)
    k = len(m)
    rows = []
    for i, j in itertools.combinations(range(k), 2):
        l = m[i]["l"] - m[j]["l"]
        diff = float(l @ f.beta)
        se = float(np.sqrt(l @ f.C @ l))
        nu = _df_contrast(f, l) if df is None else df
        q = abs(diff) / se * np.sqrt(2)
        p = float(stats.studentized_range.sf(q, k, min(nu, 1e4)))
        rows.append(dict(first=(m[i]["a"], m[i]["b"]), second=(m[j]["a"], m[j]["b"]),
                         diff=diff, se=se, df=nu, p=p))
    return pd.DataFrame(rows)
