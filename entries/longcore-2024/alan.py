"""Loading and models for Dryad dataset t1g1jwtb0 (version 300765).

Longcore, Villanueva, Nguyen-Ngo, Ghiani, Harrison & Colwell (2024), J. Exp. Biol. 227,
jeb247235, doi:10.1242/jeb.247235.

The dataset holds three CSV files and a README: `SuppressionDataset.csv` (one row per mouse and
light treatment, the percent suppression of wheel running), `cFosdata.csv` (one cFos+ cell count
per animal) and `SPD.csv` (the lamps' spectra). Dryad needs a token to download, so the workflow
stages the files of the pinned version in `STAGED`, checked against the SHA-256 of Dryad's file
list; they are read from there into memory and never written.

Where the parameters come from:

- Suppression is used as deposited (percent; positive is less activity). The claims file's
  opening comment defines it as 100 x (prior day - exposure day) / prior day; the file holds the
  result, not the wheel counts, so the definition cannot be checked.
- The GLM: normal distribution, suppression as the response, CCT categorical, illuminance
  continuous, and CCT x illuminance (claims file, opening comment, from Methods, "Photic
  suppression of nocturnal activity", paragraph 3). The open readings the claims file names are
  all available: link `"log"` (the Methods) or `"identity"`; illuminance `"lux"` or `"loglux"`
  (log10 lux); likelihood-ratio or Wald effect tests.
- Coding: categorical terms are effect coded (each level's parameter is its deviation from the
  mean of levels, the last level minus the sum of the others) and continuous terms are centered
  at their mean in the crossing. This is how JMP's Fit Model parameterizes a model by default
  ("Center Polynomials"), and the paper fitted its models in JMP Pro 17 (Methods, paragraph 3).
  The centering changes the CCT main-effect test when the interaction is in the model, so
  `design(..., center=False)` gives the uncentered variant.
- Effect sizes: each factor centered at its mean and scaled by half its range (Methods,
  paragraph 3: "Effect sizes ... were compared by centering each factor at the mean and scaling
  by half of its range"), as JMP's scaled estimates do.
- Fitting: the identity link is ordinary least squares. The log link is fitted by least squares
  on the mean (the normal-distribution maximum likelihood), with scipy's trust-region solver
  started from four fixed points, keeping the best; this is a standard choice of optimizer,
  which only matters if it fails to find the optimum, and the notebook prints every start.
- Scale: the maximum-likelihood variance SSE/n in the log-likelihood (AICc), and SSE/(n - p) for
  Wald tests and confidence intervals, as is usual for a normal GLM with estimated dispersion.
  Likelihood-ratio statistics are n log(SSE_reduced / SSE_full), with the scale profiled out.
- AICc: -2 logL + 2k + 2k(k + 1)/(n - k - 1), with k the mean parameters plus the scale (the
  usual count for a normal model); `aicc(..., count_scale=False)` gives the other count.
- Tukey-Kramer HSD (Methods, paragraph 3) is statsmodels' `pairwise_tukeyhsd`, which uses the
  Tukey-Kramer standard error for unequal group sizes.
"""

from __future__ import annotations

import hashlib
import io
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import optimize, stats

DRYAD_ID = "t1g1jwtb0"
DRYAD_VERSION = "300765"
STAGED = Path("/tmp") / "dryad" / DRYAD_ID / DRYAD_VERSION  # where the workflow stages them (docs/archives.md)
SHA256 = {  # Dryad file list, https://datadryad.org/api/v2/versions/300765/files
    "cFosdata.csv": "9a77244c5b27bb0747831c5d9b6d5b5129c2ebba8528fada4a1e9311fa8dc964",
    "README.md": "b1466b96c9e140720496e7b26ba5a79e6a41d8693a5dee4a79dbc11b623ad8be",
    "SPD.csv": "98d9ea6de15fb9bc42060c24a80ace97e5c265b1a54143b3a084c638f019c9ae",
    "SuppressionDataset.csv": "11d5cd29d536b4d9782d47a9af7ba6849434820fb923a897f94543585fc116de",
}

LUX = [0.01, 0.5, 5.0, 50.0]
CCTS = [1750, 1950, 3000]


# ---------------------------------------------------------------- reading


def read_bytes(name: str) -> bytes:
    return (STAGED / name).read_bytes()


def check_staged() -> dict[str, str]:
    """SHA-256 of each staged file; raises if any differs from Dryad's file list."""
    found = {}
    for name, expected in SHA256.items():
        digest = hashlib.sha256(read_bytes(name)).hexdigest()
        if digest != expected:
            raise ValueError(f"{name}: SHA-256 {digest} is not Dryad's {expected}")
        found[name] = digest
    return found


def read_csv(name: str) -> pd.DataFrame:
    """A CSV of the dataset, read in memory; the files start with a UTF-8 byte-order mark."""
    return pd.read_csv(io.BytesIO(read_bytes(name)), encoding="utf-8-sig")


def suppression() -> pd.DataFrame:
    """SuppressionDataset.csv with short column names and log10 lux added."""
    d = read_csv("SuppressionDataset.csv").rename(columns={
        "Intensity (lx)": "lux", "CCT": "cct", "Sex": "sex", "Mouse Number": "mouse",
        "Suppression": "supp"})
    d["loglux"] = np.log10(d["lux"])
    return d


# ---------------------------------------------------------------- design


def effect_codes(values: pd.Series, levels: list) -> pd.DataFrame:
    """Effect coding: one column per level but the last, which is -1 in every column."""
    out = pd.DataFrame(index=values.index)
    for lev in levels[:-1]:
        out[str(lev)] = (values == lev).astype(float) - (values == levels[-1]).astype(float)
    return out


def design(d: pd.DataFrame, x: str = "lux", extra: str | None = None, center: bool = True,
           cct_continuous: bool = False, means: dict | None = None):
    """Design matrix of the paper's GLM: intercept, CCT, illuminance, CCT x illuminance [, extra].

    `x` is "lux" or "loglux"; `extra` is None, "sex" or "mouse"; `cct_continuous` puts CCT in as
    kelvin (effect-size reading b). Returns the matrix and the columns of each term.
    """
    means = means or {}
    cols = {"Intercept": pd.Series(1.0, index=d.index, name="Intercept").to_frame()}
    if cct_continuous:
        c = d["cct"] - (means.get("cct", d["cct"].mean()) if center else 0)
        cols["CCT"] = c.rename("cct").to_frame()
    else:
        cols["CCT"] = effect_codes(d["cct"], CCTS).add_prefix("cct[").add_suffix("]")
    xi = d[x] - (means.get(x, d[x].mean()) if center else 0)
    cols["illuminance"] = xi.rename(x).to_frame()
    cols["CCT x illuminance"] = cols["CCT"].mul(xi, axis=0).add_suffix(f":{x}")
    if extra == "sex":
        cols["sex"] = effect_codes(d["sex"], ["F", "M"]).add_prefix("sex[").add_suffix("]")
    elif extra == "mouse":
        mice = sorted(d["mouse"].unique())
        cols["mouse"] = effect_codes(d["mouse"], mice).add_prefix("mouse[").add_suffix("]")
    X = pd.concat(cols.values(), axis=1)
    terms, start = {}, 0
    for name, block in cols.items():
        terms[name] = list(range(start, start + block.shape[1]))
        start += block.shape[1]
    return X, terms


# ---------------------------------------------------------------- fitting


class Fit:
    """A normal-distribution GLM fitted by least squares on the mean."""

    def __init__(self, y, X, link, beta, converged, starts=None):
        self.y, self.X, self.link = np.asarray(y, float), np.asarray(X, float), link
        self.names = list(X.columns) if hasattr(X, "columns") else None
        self.beta, self.converged, self.starts = beta, converged, starts
        self.n, self.p = self.X.shape
        self.mu = self.mean(self.X)
        self.sse = float(np.sum((self.y - self.mu) ** 2))
        self.sigma2 = self.sse / (self.n - self.p)
        self.llf = -0.5 * self.n * (np.log(2 * np.pi * self.sse / self.n) + 1)
        J = self.jacobian(self.X)
        self.cov = self.sigma2 * np.linalg.pinv(J.T @ J)

    def mean(self, X):
        eta = X @ self.beta
        return np.exp(eta) if self.link == "log" else eta

    def jacobian(self, X):
        return self.mean(X)[:, None] * X if self.link == "log" else X

    def params(self) -> pd.Series:
        return pd.Series(self.beta, index=self.names)

    def se(self) -> pd.Series:
        return pd.Series(np.sqrt(np.diag(self.cov)), index=self.names)

    def predict(self, X, level=0.95) -> pd.DataFrame:
        """Predicted mean with a Wald interval on the link scale (t with n - p df)."""
        X = np.asarray(X, float)
        eta = X @ self.beta
        # for the log link, cov is that of beta, so this is the s.e. of the linear predictor
        se = np.sqrt(np.einsum("ij,jk,ik->i", X, self.cov, X))
        q = stats.t.ppf(0.5 + level / 2, self.n - self.p)
        lo, hi = eta - q * se, eta + q * se
        f = np.exp if self.link == "log" else (lambda v: v)
        return pd.DataFrame({"mean": f(eta), "low": f(lo), "high": f(hi)})


def fit(y, X, link: str = "identity") -> Fit:
    """Fit by least squares; the log link from several starting points, keeping the best."""
    y = np.asarray(y, float)
    Xa = np.asarray(X, float)
    if link == "identity":
        beta = np.linalg.lstsq(Xa, y, rcond=None)[0]
        return Fit(y, X, link, beta, True)
    starts = []
    base = np.zeros(Xa.shape[1])
    base[0] = np.log(max(y.mean(), 1e-3))
    # second start: least squares of log(y) on X over the positive responses
    pos = y > 0
    b_logy = np.linalg.lstsq(Xa[pos], np.log(y[pos]), rcond=None)[0]
    top = np.zeros(Xa.shape[1])
    top[0] = np.log(y.max())
    inits = [base, b_logy, 0.5 * (base + b_logy), top]  # fixed starts, no random draws
    best = None
    for b0 in inits:
        res = optimize.least_squares(
            lambda b: np.exp(np.clip(Xa @ b, -50, 50)) - y, b0,
            jac=lambda b: np.exp(np.clip(Xa @ b, -50, 50))[:, None] * Xa,
            method="trf", xtol=1e-12, ftol=1e-12, gtol=1e-10, max_nfev=20000)
        sse = float(np.sum(res.fun ** 2))
        starts.append((sse, bool(res.success), res.status))
        if best is None or sse < best[0]:
            best = (sse, res)
    return Fit(y, X, link, best[1].x, bool(best[1].success), starts)


def drop_terms(X: pd.DataFrame, terms: dict, names: list[str]) -> pd.DataFrame:
    idx = [i for t in names for i in terms[t]]
    return X.drop(columns=X.columns[idx])


def lr_test(full: Fit, reduced: Fit):
    """Likelihood-ratio chi-square with the scale profiled out, n log(SSE_r / SSE_f)."""
    chi2 = full.n * np.log(reduced.sse / full.sse)
    df = full.p - reduced.p
    return chi2, df, stats.chi2.sf(chi2, df)


def wald_test(f: Fit, idx: list[int]):
    """Wald chi-square of the coefficients `idx` being zero."""
    b = f.beta[idx]
    V = f.cov[np.ix_(idx, idx)]
    chi2 = float(b @ np.linalg.solve(V, b))
    return chi2, len(idx), stats.chi2.sf(chi2, len(idx))


def effect_tests(d, x="lux", link="identity", extra=None, center=True) -> pd.DataFrame:
    """Whole-model and per-term tests, likelihood ratio and Wald, for one reading."""
    X, terms = design(d, x, extra, center)
    full = fit(d["supp"], X, link)
    rows = []
    null = fit(d["supp"], X[["Intercept"]], link)
    chi2, df, p = lr_test(full, null)
    rows.append({"term": "whole model", "df": df, "LR chi2": chi2, "LR p": p,
                 "Wald chi2": np.nan, "Wald p": np.nan})
    for t in [t for t in terms if t != "Intercept"]:
        red = fit(d["supp"], drop_terms(X, terms, [t]), link)
        chi2, df, p = lr_test(full, red)
        w2, _, wp = wald_test(full, terms[t])
        rows.append({"term": t, "df": df, "LR chi2": chi2, "LR p": p, "Wald chi2": w2, "Wald p": wp})
    out = pd.DataFrame(rows)
    out.attrs["fit"] = full
    return out


def aicc(f: Fit, count_scale: bool = True) -> float:
    k = f.p + (1 if count_scale else 0)
    return -2 * f.llf + 2 * k + 2 * k * (k + 1) / (f.n - k - 1)


# ---------------------------------------------------------------- summaries


def cell_means(d: pd.DataFrame) -> pd.DataFrame:
    """Mean, s.d. and count of suppression per treatment, over the mice that have it."""
    return d.groupby(["lux", "cct"])["supp"].agg(["count", "mean", "std", "median"])


def scaled_estimates(f: Fit, d: pd.DataFrame, x: str, cct_continuous: bool = False) -> dict:
    """JMP-style scaled estimates: continuous terms times half their range (centered fits)."""
    b = f.params()
    out = {"illuminance": b[x] * (d[x].max() - d[x].min()) / 2}
    if cct_continuous:
        out["CCT"] = b["cct"] * (d["cct"].max() - d["cct"].min()) / 2
    else:
        p = [b["cct[1750]"], b["cct[1950]"]]
        p.append(-sum(p))  # 3000 K, the last level
        out["CCT levels"] = dict(zip(CCTS, p))
        out["CCT"] = max(abs(v) for v in p)
    return out
