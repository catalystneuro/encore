"""Loading and measures for the Volebny Kompas datasets, Figshare item 24949470, version 1.

The files are streamed from Figshare (docs/archives.md, "Figshare") and read into memory;
nothing is written to disk. Where each parameter comes from:

- Row selections (`selections`). The paper's cleaning (Technical Validation, Data cleaning):
  rows with -1 in any of S1 to S39 are removed, "no opinion" (NA in the file) becomes 50.
  The deposited R code (Volebny_Kompas_code.R, lines "Identify and exclude rows where all
  values in columns S1 to S39 are the same") also removes rows that give one answer to all 39
  statements; the paper's text does not mention this, so it is the code's variant ("code").
  The factor analysis of the code runs on rows whose EMAIL_ID is given and occurs once
  ("FILTERING DATA WITH UNIQUE EMAIL ID"); that is the "code_email" selection.
- Likert coding 0, 25, 50, 75, 100 (Methods, Volebny Kompas implementation and usage).
- Weighted kappa: Cohen's weighted kappa (paper ref. 37) with linear or quadratic weights;
  the paper does not say which, so both are computed (claims file, coder-agreement-kappa).
- Dimension scores: Supplementary Table 1 of the dataset gives each statement's dimension and
  polarity. A statement of polarity -1 enters as 100 minus the position (Methods: "a negative
  polarity (-1) increases the dimension score when users do not support a statement"); the
  score is the mean over the dimension's statements (claims file, reading (a)).
- Parallel analysis (`reduced_eigenvalues`, `parallel_reference`) follows psych::fa.parallel with fa = "fa" given a
  correlation matrix: the observed values are the eigenvalues of the correlation matrix with the
  communalities of a one-factor solution on its diagonal; the reference values are the same for
  the correlation matrices of normal random data of the same size, averaged over iterations; the
  count is the number of leading observed values above the reference. Defaults (minres, 20
  iterations) are the claims file's reading; ML with 1000 (Pearson) or 100 (polychoric)
  iterations are the deposited R code's settings. The R code passes a correlation matrix and
  n.obs, so psych can only simulate normal data, as `parallel_reference` does. Given raw data
  with cor = "poly" (the claims file's default reading), psych instead resamples each column and
  takes polychoric correlations of the resampled data (`parallel_reference_resampled`).
- Polychoric correlations (`polychoric`): two-step estimate as in psych::polychoric, with each
  statement's thresholds from its own margins and the correlation by maximum likelihood on the
  5 by 5 table. Empty cells are not corrected; with tens of thousands of rows per table this is a
  standard choice that cannot change a factor count.
- Factor extraction: ML (minimising the ML discrepancy) and iterated principal axis (psych
  fm = "pa", communalities started at the squared multiple correlations, up to 50 iterations),
  with promax rotation (power 4, after varimax), as psych::fa with rotate = "promax".
"""

from __future__ import annotations

import hashlib
import io
import json
import urllib.request

import fsspec
import numpy as np
import pandas as pd
from scipy import optimize, stats

ARTICLE = "24949470"
VERSION = "1"
DOI = "10.6084/m9.figshare.24949470.v1"
API = f"https://api.figshare.com/v2/articles/{ARTICLE}/versions/{VERSION}"
STATEMENTS = [f"S{i}" for i in range(1, 40)]
LIKERT = {"Completely disagree": 0, "Tend to disagree": 25, "Neutral": 50,
          "Tend to agree": 75, "Completely agree": 100}
AGES = ["Under 18", "18-20", "21-24", "25-34", "35-44", "45-54", "55-64", "65-74", "75 or older"]
EDUCATIONS = ["No education", "Primary education", "Secondary education", "Applied higher education",
              "Vocational education", "University degree/Academic higher education"]
GENDERS = ["Female", "Male", "Other / Prefer not to say"]


def file_list() -> pd.DataFrame:
    """The files of the pinned version, from the Figshare API: id, name, size, MD5."""
    with urllib.request.urlopen(API, timeout=60) as r:
        meta = json.load(r)
    files = pd.DataFrame(meta["files"])[["id", "name", "size", "computed_md5"]]
    files.attrs["meta"] = meta
    return files


STREAMED_MD5: dict[int, str] = {}   # MD5 of the bytes of each streamed file, to check against the API's


def read_bytes(file_id: int) -> bytes:
    """Stream one file into memory from Figshare's downloader, which redirects to S3."""
    with fsspec.open(f"https://ndownloader.figshare.com/files/{file_id}", block_size=2**20) as f:
        b = f.read()
    STREAMED_MD5[file_id] = hashlib.md5(b).hexdigest()
    return b


def file_id(files: pd.DataFrame, name: str) -> int:
    return int(files.loc[files["name"] == name, "id"].iloc[0])


def load_responses(files: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """The user responses as read (all strings, nothing parsed), and S1 to S39 as numbers.

    In the numeric table "NA" (no opinion) is NaN and -1 (unanswered) is kept as -1."""
    raw = pd.read_csv(io.BytesIO(read_bytes(file_id(files, "data_without_email.csv"))), sep=";",
                      dtype=str, keep_default_na=False)
    likert = raw[STATEMENTS].replace("NA", np.nan).astype(float)
    return raw, likert


def selections(raw: pd.DataFrame, likert: pd.DataFrame) -> dict[str, pd.Series]:
    """Boolean row masks: all raw rows, the paper's cleaning, the R code's cleaning, and the code's
    unique-email rows (see the module docstring)."""
    incomplete = (likert == -1).any(axis=1)
    # R's unique() counts NA as a value, so a row of 39 NA is "all the same" too
    same = likert.fillna(-999).nunique(axis=1) == 1
    code = ~incomplete & ~same
    email = raw["EMAIL_ID"]
    counts = email[code].value_counts()
    unique_email = code & (email != "NA") & email.map(counts).eq(1)
    return {"raw": pd.Series(True, index=raw.index), "paper": ~incomplete, "code": code,
            "code_email": unique_email}


def _key(text: str) -> str:
    return " ".join(str(text).lower().split())[:40]


def load_party_positions(files: pd.DataFrame, supp: pd.DataFrame) -> tuple[dict[str, pd.DataFrame], pd.DataFrame]:
    """Every sheet of the party positions workbook, and the coded rows (those naming a party).

    `statement` is the statement's number found from its English wording in Supplementary
    Table 1; the workbook's own "Statement no." is kept as it is (the two disagree for some rows,
    which the notebook shows)."""
    b = read_bytes(file_id(files, "VAA_party_positions coded.xlsx"))
    sheets = pd.read_excel(io.BytesIO(b), sheet_name=None)
    coded = sheets["Codesheet"]
    coded = coded[coded["Party"].notna()].copy()
    coded["Statement no."] = coded["Statement no."].astype(int)
    by_text = {_key(t): int(n) for n, t in zip(supp["Statement Number"], supp["Statement (English)"])}
    coded["statement"] = coded["Statement in English"].map(_key).map(by_text)
    return sheets, coded


def load_supplementary_table(files: pd.DataFrame) -> pd.DataFrame:
    """Supplementary Table 1: each statement's uni-dimension and landscape dimension, with polarity."""
    t = pd.read_excel(io.BytesIO(read_bytes(file_id(files, "Supplementary Table 1.xlsx"))), sheet_name=None)
    assert len(t) == 1, list(t)
    return next(iter(t.values()))


def load_recoded(files: pd.DataFrame) -> pd.DataFrame:
    return pd.read_csv(io.BytesIO(read_bytes(file_id(files, "recoded_party_positions.csv")))).set_index("Party")


def dimension_assignments(supp: pd.DataFrame) -> pd.DataFrame:
    """One row per (statement, dimension, polarity), for the uni-dimensions and the landscape axes."""
    rows = []
    for _, r in supp.iterrows():
        s = int(r["Statement Number"])
        uni, upol = r["Uni-Dimension"], r["Statement Uni-Dimension Polarity"]
        if isinstance(uni, str) and uni != "N/A":
            rows.append((s, "uni", uni.split(":")[0].strip(), 1 if upol.strip() == "(+)" else -1))
        land, lpol = r["Political Landscape Dimension(s)"], r.iloc[5]
        if isinstance(land, str) and land != "N/A":
            for dim, pol in zip(land.split(" / "), lpol.split("/")):
                rows.append((s, "landscape", dim.split(":")[0].strip(), 1 if pol.strip() == "(+)" else -1))
    return pd.DataFrame(rows, columns=["statement", "kind", "dimension", "polarity"])


def dimension_scores(positions: pd.DataFrame, assign: pd.DataFrame) -> pd.DataFrame:
    """Score of each party (rows of `positions`, columns 1..39, NaN = left out) on each dimension:
    the mean over the dimension's statements of the position, or 100 minus it for polarity -1."""
    out = {}
    for dim, g in assign.groupby("dimension", sort=False):
        cols = []
        for _, r in g.iterrows():
            x = positions[r["statement"]]
            cols.append(x if r["polarity"] == 1 else 100 - x)
        out[dim] = pd.concat(cols, axis=1).mean(axis=1, skipna=True)
    return pd.DataFrame(out)


def weighted_kappa(a, b, categories, weights: str) -> float:
    """Cohen's weighted kappa for two raters over ordered categories (linear or quadratic weights)."""
    k = len(categories)
    idx = {c: i for i, c in enumerate(categories)}
    obs = np.zeros((k, k))
    for x, y in zip(a, b):
        obs[idx[x], idx[y]] += 1
    obs /= obs.sum()
    exp = np.outer(obs.sum(1), obs.sum(0))
    i, j = np.meshgrid(np.arange(k), np.arange(k), indexing="ij")
    w = np.abs(i - j) / (k - 1) if weights == "linear" else ((i - j) / (k - 1)) ** 2
    return 1 - (w * obs).sum() / (w * exp).sum()


# --- correlations and factor analysis -------------------------------------------------------------

def pearson(X: pd.DataFrame) -> np.ndarray:
    """Pearson correlations, pairwise complete (R's cor(use = "pairwise.complete.obs"))."""
    return X.corr(method="pearson").to_numpy()


def _bvn_cdf(h, k, rho):
    """Bivariate standard normal CDF at arrays of points (finite or +-inf)."""
    h = np.clip(h, -12, 12)
    k = np.clip(k, -12, 12)
    mvn = stats.multivariate_normal(mean=[0, 0], cov=[[1, rho], [rho, 1]])
    return mvn.cdf(np.column_stack([h.ravel(), k.ravel()])).reshape(h.shape)


def _thresholds(x: np.ndarray, levels) -> np.ndarray:
    counts = np.array([(x == v).sum() for v in levels], float)
    cum = np.cumsum(counts)[:-1] / counts.sum()
    return np.concatenate([[-np.inf], stats.norm.ppf(cum), [np.inf]])


def polychoric(X: pd.DataFrame, levels=(0, 25, 50, 75, 100)) -> np.ndarray:
    """Polychoric correlation matrix, pairwise complete, thresholds from each item's margins."""
    A = X.to_numpy()
    p = A.shape[1]
    taus = [_thresholds(A[~np.isnan(A[:, j]), j], levels) for j in range(p)]
    R = np.eye(p)
    L = len(levels)
    for i in range(p):
        for j in range(i + 1, p):
            ok = ~np.isnan(A[:, i]) & ~np.isnan(A[:, j])
            ai = np.searchsorted(levels, A[ok, i])
            aj = np.searchsorted(levels, A[ok, j])
            table = np.zeros((L, L))
            np.add.at(table, (ai, aj), 1)
            ti, tj = taus[i], taus[j]
            H, K = np.meshgrid(ti, tj, indexing="ij")

            def nll(r):
                F = _bvn_cdf(H, K, r)
                P = F[1:, 1:] - F[:-1, 1:] - F[1:, :-1] + F[:-1, :-1]
                return -(table * np.log(np.clip(P, 1e-300, None))).sum()

            r0 = np.corrcoef(A[ok, i], A[ok, j])[0, 1]
            res = optimize.minimize_scalar(nll, bounds=(max(-0.999, r0 - 0.3), min(0.999, r0 + 0.3)),
                                           method="bounded", options={"xatol": 1e-5})
            R[i, j] = R[j, i] = res.x
    return R


FITS: list[bool] = []   # whether each uniqueness fit converged, for the notebook to report


def _fit_uniquenesses(R: np.ndarray, nfactors: int, fm: str) -> np.ndarray:
    """Uniquenesses of an nfactors solution by minres (unweighted least squares) or ML, fitted as
    psych does: optimise the uniquenesses, with loadings from the eigen decomposition."""
    p = R.shape[0]
    smc = 1 - 1 / np.diag(np.linalg.inv(R))
    start = np.clip(1 - smc, 0.005, 1)

    def loadings(psi):
        if fm == "ml":
            sc = np.sqrt(psi)
            Rs = R / np.outer(sc, sc)
            e, v = np.linalg.eigh(Rs)
            e, v = e[::-1][:nfactors], v[:, ::-1][:, :nfactors]
            return v * np.sqrt(np.maximum(e - 1, 0)) * sc[:, None]
        Rr = R - np.diag(psi)
        e, v = np.linalg.eigh(Rr)
        e, v = e[::-1][:nfactors], v[:, ::-1][:, :nfactors]
        return v * np.sqrt(np.maximum(e, 0))

    def objective(psi):
        if fm == "ml":
            sc = np.sqrt(psi)
            e = np.linalg.eigvalsh(R / np.outer(sc, sc))[::-1][nfactors:]
            if e.min() <= 0:
                return -1e10
            return np.sum(np.log(e) - e) - nfactors + p
        Lm = loadings(psi)
        resid = R - Lm @ Lm.T
        np.fill_diagonal(resid, 0)
        return 0.5 * np.sum(resid ** 2)

    res = optimize.minimize(lambda x: -objective(x) if fm == "ml" else objective(x), start,
                            method="L-BFGS-B", bounds=[(0.005, 1)] * p,
                            options={"maxiter": 5000, "ftol": 1e-12, "gtol": 1e-8})
    FITS.append(bool(res.success))
    return res.x


def reduced_eigenvalues(R: np.ndarray, fm: str) -> np.ndarray:
    """Eigenvalues of R with the communalities of a one-factor solution on the diagonal (the
    factor values of psych::fa.parallel)."""
    psi = _fit_uniquenesses(R, 1, fm)
    return np.sort(np.linalg.eigvalsh(R - np.diag(psi)))[::-1]


def parallel_reference(n: int, p: int, fm: str, n_iter: int, rng: np.random.Generator) -> np.ndarray:
    """Mean factor values of n_iter correlation matrices of n by p standard normal data."""
    vals = []
    for _ in range(n_iter):
        Z = rng.standard_normal((n, p), dtype=np.float32).astype(np.float64)
        vals.append(reduced_eigenvalues(np.corrcoef(Z, rowvar=False), fm))
    return np.mean(vals, axis=0)


def parallel_reference_resampled(X: pd.DataFrame, fm: str, n_iter: int, rng: np.random.Generator) -> np.ndarray:
    """Factor values of n_iter polychoric matrices of resampled data, one row per iteration: each
    column is drawn with replacement from its own values (missing values included), which keeps the
    margins and removes the correlations. This is psych::fa.parallel's resampling reference, which
    it uses with cor = "poly" on raw data (the claims file's default reading)."""
    A = X.to_numpy()
    vals = []
    for _ in range(n_iter):
        S = np.column_stack([rng.choice(A[:, j], len(A)) for j in range(A.shape[1])])
        vals.append(reduced_eigenvalues(polychoric(pd.DataFrame(S)), fm))
    return np.array(vals)


def parallel_count(observed: np.ndarray, reference: np.ndarray) -> int:
    """Number of leading observed factor values above the reference (psych's nfact)."""
    above = observed > reference
    return int(np.argmin(above)) if not above.all() else len(above)


def fa_loadings(R: np.ndarray, nfactors: int, fm: str) -> np.ndarray:
    """Unrotated loadings by ML or iterated principal axis (psych fm = "pa")."""
    if fm == "ml":
        psi = _fit_uniquenesses(R, nfactors, "ml")
        sc = np.sqrt(psi)
        e, v = np.linalg.eigh(R / np.outer(sc, sc))
        e, v = e[::-1][:nfactors], v[:, ::-1][:, :nfactors]
        return v * np.sqrt(np.maximum(e - 1, 0)) * sc[:, None]
    h2 = 1 - 1 / np.diag(np.linalg.inv(R))
    for _ in range(50):
        Rr = R.copy()
        np.fill_diagonal(Rr, h2)
        e, v = np.linalg.eigh(Rr)
        e, v = e[::-1][:nfactors], v[:, ::-1][:, :nfactors]
        Lm = v * np.sqrt(np.maximum(e, 0))
        new = (Lm ** 2).sum(1)
        if np.max(np.abs(new - h2)) < 0.001:
            h2 = new
            break
        h2 = new
    return Lm


def varimax(L: np.ndarray, normalize: bool = True, eps: float = 1e-5) -> np.ndarray:
    """stats::varimax, with Kaiser normalisation."""
    p, k = L.shape
    if normalize:
        sc = np.sqrt((L ** 2).sum(1))
        L = L / sc[:, None]
    T = np.eye(k)
    d = 0
    for _ in range(1000):
        Z = L @ T
        B = L.T @ (Z ** 3 - Z @ np.diag((Z ** 2).sum(0)) / p)
        u, s, vt = np.linalg.svd(B)
        T = u @ vt
        dpast, d = d, s.sum()
        if d < dpast * (1 + eps):
            break
    Z = L @ T
    if normalize:
        Z = Z * sc[:, None]
    return Z


def promax(L: np.ndarray, m: int = 4) -> np.ndarray:
    """stats::promax (as psych calls it): varimax, then a target of loadings raised to the power m."""
    V = varimax(L)
    Q = V * np.abs(V) ** (m - 1)
    U = np.linalg.lstsq(V, Q, rcond=None)[0]
    d = np.diag(np.linalg.inv(U.T @ U))
    U = U @ np.diag(np.sqrt(d))
    return V @ U


def tucker_congruence(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    return (A.T @ B) / np.sqrt(np.outer((A ** 2).sum(0), (B ** 2).sum(0)))
