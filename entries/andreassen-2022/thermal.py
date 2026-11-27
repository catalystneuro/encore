"""Loading and models for the derived data of Andreassen et al. (2022) on FIGSHARE:19640805.

Andreassen, Hall, Khatibzadeh, Jutfelt & Kermen (2022), "Brain dysfunction during warming is
linked to oxygen limitation in larval zebrafish", PNAS 119, e2207052119.

The Figshare item (version 4, doi:10.6084/m9.figshare.19640805.v4) holds ten CSV tables of
per-fish values, a Readme.txt that describes their columns, and the paper's R script
(Code_Andreassen_et_al_2022.R). Files are streamed from the archive into memory; nothing is
written to disk. Each file's MD5 is checked against the archive's `computed_md5`.

Where the parameters come from:

- The model formulas, the reference levels, the time and temperature variables and the outlier
  rule are those of the paper's R script, as the claims file asks (it names the script as the
  place where open details may be settled). Each function says which section of the script it
  follows.
- Outliers: the script uses rstatix::identify_outliers, "values above Q3 + 3xIQR or below Q1 -
  3xIQR", within groups (script, Fig 1C and Fig 5A sections; SI Statistical Analyses). R's
  default quantile (type 7) is numpy's default (linear).
- Mixed models: lme4::lmer with REML and a random intercept per fish (Methods, Statistical
  Analyses; script). The script's tables take p-values with `p.val = "kr"` (Kenward-Roger);
  the claims file names Satterthwaite (lmerTest) as the main reading. `lmm` gives Satterthwaite
  degrees of freedom and, as a second reading, the normal approximation (infinite degrees of
  freedom). Kenward-Roger is not implemented here; the notebook prints both readings for every
  term, and no outcome changes between them.
- Binomial mixed model: lme4::glmer, logit link, random intercept per fish, fitted by maximum
  likelihood with the Laplace approximation (glmer's default, `nagq=1` here); adaptive
  Gauss-Hermite quadrature with more nodes is a check of the approximation. Wald z p-values, as
  summary() of glmer gives them.
- Q10 = (R2 / R1) ** (10 / (T2 - T1)), the standard formula (claims file).
"""

from __future__ import annotations

import hashlib
import io
import json
import urllib.request

import fsspec
import numpy as np
import pandas as pd
import patsy
from scipy import optimize, stats

ARTICLE_ID = 19640805
VERSION = 4
DOI = "10.6084/m9.figshare.19640805.v4"
API = f"https://api.figshare.com/v2/articles/{ARTICLE_ID}/versions/{VERSION}"
DOWNLOAD = "https://ndownloader.figshare.com/files/{}"


def file_list() -> pd.DataFrame:
    """The files of the pinned version, with id, name, size and computed_md5, from the API."""
    with urllib.request.urlopen(API) as response:
        meta = json.load(response)
    files = pd.DataFrame(meta["files"])[["id", "name", "size", "computed_md5"]]
    files.attrs["meta"] = meta
    return files


def read_bytes(file_id: int, md5: str) -> bytes:
    """Stream one file into memory with fsspec and check its MD5."""
    with fsspec.open(DOWNLOAD.format(file_id), block_size=2**20) as handle:
        content = handle.read()
    digest = hashlib.md5(content).hexdigest()
    if digest != md5:
        raise ValueError(f"file {file_id}: MD5 {digest}, archive says {md5}")
    return content


def load_all() -> tuple[pd.DataFrame, dict[str, bytes]]:
    """Every file of the pinned version, as raw bytes keyed by name."""
    files = file_list()
    raw = {row.name: read_bytes(row.id, row.computed_md5) for row in files.itertuples()}
    return files, raw


def read_csv(raw: dict[str, bytes], name: str) -> pd.DataFrame:
    """A CSV table of the item. LightResponse.csv was written with R's row names, so its header
    has one field fewer than its rows; pandas then takes the first field as the index, which is
    dropped here."""
    table = pd.read_csv(io.BytesIO(raw[name]), encoding="utf-8-sig")
    return table.reset_index(drop=True)


def extreme_outliers(values: pd.Series) -> pd.Series:
    """rstatix::identify_outliers' is.extreme: below Q1 - 3 IQR or above Q3 + 3 IQR."""
    q1, q3 = np.nanpercentile(values, [25, 75])
    iqr = q3 - q1
    return (values < q1 - 3 * iqr) | (values > q3 + 3 * iqr)


def q10(rate1: float, rate2: float, temp1: float, temp2: float) -> float:
    return (rate2 / rate1) ** (10.0 / (temp2 - temp1))


# Linear mixed model with a random intercept (lme4::lmer, REML) ---------------------------------

class LMM:
    """REML fit of y = X b + u[group] + e, u ~ N(0, s2u), e ~ N(0, s2e).

    Fixed effects are estimated by generalised least squares at the REML variance estimates,
    as lmer does. `table()` gives each coefficient with its SE, t, Satterthwaite degrees of
    freedom and p-value, and the p-value of the normal approximation.
    """

    def __init__(self, formula: str, data: pd.DataFrame, group: str):
        data = data.dropna(subset=[group])
        y, X = patsy.dmatrices(formula, data, return_type="dataframe", NA_action="drop")
        self.names = list(X.columns)
        self.y = y.values[:, 0]
        self.X = X.values
        groups = data.loc[X.index, group].astype(str).values
        self.levels, self.g = np.unique(groups, return_inverse=True)
        self.Z = (self.g[:, None] == np.arange(len(self.levels))[None, :]).astype(float)
        self.n, self.p = self.X.shape
        self._fit()

    def _V(self, theta):
        s2u, s2e = theta
        return s2e * np.eye(self.n) + s2u * (self.Z @ self.Z.T)

    def _reml(self, theta) -> float:
        """Minus twice the REML log-likelihood, without the constant."""
        V = self._V(theta)
        sign, logdet_v = np.linalg.slogdet(V)
        Vi = np.linalg.inv(V)
        xtvx = self.X.T @ Vi @ self.X
        sign2, logdet_x = np.linalg.slogdet(xtvx)
        beta = np.linalg.solve(xtvx, self.X.T @ Vi @ self.y)
        r = self.y - self.X @ beta
        return logdet_v + logdet_x + r @ Vi @ r

    def _fit(self):
        start = np.log([np.var(self.y) / 2, np.var(self.y) / 2])
        res = optimize.minimize(lambda t: self._reml(np.exp(t)), start, method="Nelder-Mead",
                                options={"xatol": 1e-9, "fatol": 1e-11, "maxiter": 4000})
        res = optimize.minimize(lambda t: self._reml(np.exp(t)), res.x, method="BFGS")
        self.theta = np.exp(res.x)
        self.converged = bool(res.success) or res.status == 2
        Vi = np.linalg.inv(self._V(self.theta))
        self.cov = np.linalg.inv(self.X.T @ Vi @ self.X)
        self.beta = self.cov @ self.X.T @ Vi @ self.y

    def _cov_beta(self, theta):
        Vi = np.linalg.inv(self._V(theta))
        return np.linalg.inv(self.X.T @ Vi @ self.X)

    def satterthwaite_df(self, contrast: np.ndarray) -> float:
        """Satterthwaite degrees of freedom for contrast' beta, as lmerTest computes them: the
        gradient of the contrast's variance in the variance parameters and their asymptotic
        covariance (twice the inverse Hessian of minus twice the REML log-likelihood)."""
        theta = self.theta.copy()
        steps = np.maximum(theta * 1e-4, 1e-8)
        f0 = contrast @ self._cov_beta(theta) @ contrast
        grad = np.zeros(2)
        for i in range(2):
            up, down = theta.copy(), theta.copy()
            up[i] += steps[i]
            down[i] = max(down[i] - steps[i], 1e-12)
            grad[i] = (contrast @ self._cov_beta(up) @ contrast
                       - contrast @ self._cov_beta(down) @ contrast) / (up[i] - down[i])
        hess = np.zeros((2, 2))
        for i in range(2):
            for j in range(2):
                e_i, e_j = np.eye(2)[i] * steps[i], np.eye(2)[j] * steps[j]
                hess[i, j] = (self._reml(theta + e_i + e_j) - self._reml(theta + e_i - e_j)
                              - self._reml(theta - e_i + e_j) + self._reml(theta - e_i - e_j)) \
                    / (4 * steps[i] * steps[j])
        acov = 2 * np.linalg.inv(hess)
        return float(2 * f0 ** 2 / (grad @ acov @ grad))

    def test(self, contrast) -> dict:
        contrast = np.asarray(contrast, dtype=float)
        est = float(contrast @ self.beta)
        se = float(np.sqrt(contrast @ self.cov @ contrast))
        t = est / se
        df = self.satterthwaite_df(contrast)
        return {"estimate": est, "se": se, "t": t, "df": df,
                "p": float(2 * stats.t.sf(abs(t), df)),
                "p_normal": float(2 * stats.norm.sf(abs(t)))}

    def table(self) -> pd.DataFrame:
        rows = [{"term": name, **self.test(np.eye(self.p)[i])} for i, name in enumerate(self.names)]
        return pd.DataFrame(rows).set_index("term")

    def summary(self) -> str:
        return (f"{self.n} observations, {len(self.levels)} fish; random intercept variance "
                f"{self.theta[0]:.4g}, residual variance {self.theta[1]:.4g}")


# Binomial mixed model with a random intercept (lme4::glmer) ------------------------------------

_LOG_SQRT_2PI = 0.5 * np.log(2 * np.pi)


class BinomialGLMM:
    """ML fit of logit P(success) = X b + u[group], u ~ N(0, s2), on counts of successes and
    failures per row, by adaptive Gauss-Hermite quadrature with `nagq` nodes (1 is the Laplace
    approximation, glmer's default). Parameters are the fixed effects and log s."""

    def __init__(self, formula: str, data: pd.DataFrame, successes: str, failures: str,
                 group: str, nagq: int = 1):
        data = data.dropna(subset=[successes, failures])
        X = patsy.dmatrix(formula, data, return_type="dataframe", NA_action="drop")
        data = data.loc[X.index]
        self.names = list(X.columns)
        self.X = X.values
        self.k = data[successes].values.astype(float)
        self.m = (data[successes] + data[failures]).values.astype(float)
        self.levels, self.g = np.unique(data[group].astype(str).values, return_inverse=True)
        self.G = len(self.levels)
        self.nodes, self.weights = np.polynomial.hermite.hermgauss(nagq)
        self.nagq = nagq
        self._fit()

    def _cond_loglik(self, eta):
        # binomial log-likelihood without the binomial coefficient
        return self.k * eta - self.m * np.logaddexp(0, eta)

    def _negloglik(self, params):
        beta, log_s = params[:-1], params[-1]
        s2 = np.exp(2 * log_s)
        fixed = self.X @ beta
        b = np.zeros(self.G)
        for _ in range(50):           # Newton steps for each fish's mode
            eta = fixed + b[self.g]
            prob = 1 / (1 + np.exp(-eta))
            grad = np.bincount(self.g, self.k - self.m * prob, self.G) - b / s2
            hess = -np.bincount(self.g, self.m * prob * (1 - prob), self.G) - 1 / s2
            step = grad / hess
            b = b - step
            if np.max(np.abs(step)) < 1e-10:
                break
        eta = fixed + b[self.g]
        prob = 1 / (1 + np.exp(-eta))
        hess = -np.bincount(self.g, self.m * prob * (1 - prob), self.G) - 1 / s2
        scale = 1 / np.sqrt(-hess)
        total = 0.0
        terms = []
        for x, w in zip(self.nodes, self.weights):
            bk = b + np.sqrt(2) * scale * x
            h = (np.bincount(self.g, self._cond_loglik(fixed + bk[self.g]), self.G)
                 - 0.5 * bk ** 2 / s2 - 0.5 * np.log(s2) - _LOG_SQRT_2PI)
            terms.append(np.log(w) + x ** 2 + h)
        terms = np.array(terms)
        per_group = np.logaddexp.reduce(terms, axis=0) + np.log(np.sqrt(2) * scale)
        total = per_group.sum()
        return -total

    def _fit(self):
        start = np.zeros(self.X.shape[1] + 1)
        res = optimize.minimize(self._negloglik, start, method="BFGS",
                                options={"gtol": 1e-7, "maxiter": 2000})
        res = optimize.minimize(self._negloglik, res.x, method="Nelder-Mead",
                                options={"xatol": 1e-8, "fatol": 1e-10, "maxiter": 20000})
        res = optimize.minimize(self._negloglik, res.x, method="BFGS", options={"gtol": 1e-8})
        self.params = res.x
        self.converged = bool(res.success) or res.status == 2
        self.loglik = -res.fun
        hess = _numeric_hessian(self._negloglik, res.x)
        self.cov = np.linalg.inv(hess)

    def table(self) -> pd.DataFrame:
        p = len(self.names)
        est = self.params[:p]
        se = np.sqrt(np.diag(self.cov)[:p])
        z = est / se
        return pd.DataFrame({"estimate": est, "se": se, "z": z,
                             "p": 2 * stats.norm.sf(np.abs(z))}, index=self.names)

    @property
    def sd_fish(self) -> float:
        return float(np.exp(self.params[-1]))


def _numeric_hessian(fun, x, step=1e-4):
    n = len(x)
    hess = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            e_i, e_j = np.eye(n)[i] * step, np.eye(n)[j] * step
            value = (fun(x + e_i + e_j) - fun(x + e_i - e_j) - fun(x - e_i + e_j)
                     + fun(x - e_i - e_j)) / (4 * step ** 2)
            hess[i, j] = hess[j, i] = value
    return hess


def inverse_logit(x):
    return 1 / (1 + np.exp(-np.asarray(x, dtype=float)))
