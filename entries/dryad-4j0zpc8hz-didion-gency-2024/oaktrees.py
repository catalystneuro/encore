"""Loading and statistics for the open-top chamber data of Dryad dataset 4j0zpc8hz.

Didion-Gency, Vitasse, Buchmann, Gessler, Gisler, Schaub & Grossiord (2024), Plant Physiology 194,
doi:10.1093/plphys/kiad565. Dataset doi:10.5061/dryad.4j0zpc8hz, version id 260590 in Dryad's API.

The dataset is one workbook, Dryad_Data_PlantPhy_MargauxDidionGency.xlsx, with the sheets "README.md"
(the column descriptions) and "Total Data" (one row per tree and measurement campaign, with the yearly
traits repeated on the three rows of a year), and a Metadata.csv that repeats the column descriptions.
Dryad lets no one download a file without a token, so the files of the pinned version are staged before
the notebook runs, in /tmp/dryad/<id>/<version id>/ (docs/archives.md, "Dryad"); they are read there, in
place, into memory, after checking each against the SHA-256 Dryad's file list gives.

Where the parameters come from:

- The treatment test, the interaction test, the phenology regression and the biodiversity effects
  follow the opening comment of the claims file (claims/dryad-4j0zpc8hz/10.1093-plphys-kiad565.yaml),
  which cites the paper's Methods, the footnotes of Supplemental Tables S1 to S3 and S6, and the
  figure legends. Readings it names (T1/T2, S1/S2, L1/L2, I1/I2, B1/B2, P1/P2) are arguments here.
- `anova_sequential` gives the sequential F tests of nlme's anova.lme (the claims file reads Table S1's
  F tests so): F of a term from the fixed effects rotated by the Cholesky factor of their inverse
  covariance, with nlme's denominator degrees of freedom (chamber-level terms: chambers minus the
  chamber-level coefficients and the intercept; other terms: rows minus chambers minus the other
  coefficients).
- `contrasts` gives multcomp-style Tukey contrasts: differences of model cell means, Wald z, and
  single-step adjusted p over the family (multcomp's default for lme models, which uses the
  multivariate normal). The family is the six treatment pairs within one year, as the claims file
  says contrasts are "among the four treatments within each year".
- Rows that are exact duplicates are counted once. Where a tree has two different rows for one
  campaign (one case), the two are averaged; a standard choice that changes one tree-campaign.
- The multivariate normal integration of the single-step p uses a fixed seed (a standard choice; it
  changes p only below its 1e-4 precision).
"""

from __future__ import annotations

import hashlib
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import patsy
import statsmodels.api as sm
from scipy import stats

DATASET_ID = "4j0zpc8hz"
VERSION_ID = "260590"
DOI = "10.5061/dryad.4j0zpc8hz"
WORKBOOK = "Dryad_Data_PlantPhy_MargauxDidionGency.xlsx"
# SHA-256 of each file of version 260590, from https://datadryad.org/api/v2/versions/260590/files
FILES = {
    WORKBOOK: "b18a8e25527e2f5ecc80a9d520913b38eafb4382fe7e6c5e8ee7232e243300a3",
    "Metadata.csv": "eaffc99d0e0a23c7e3bab236d4ecd951c92733cacbf9d7c8a57447a9b5ad0766",
}
STAGED_ROOT = Path("/tmp")   # where tools/stage_files.py puts the files of archives that need a token


def data_dir() -> Path:
    return STAGED_ROOT / "dryad" / DATASET_ID / VERSION_ID


def check_files() -> pd.DataFrame:
    rows = []
    for name, digest in FILES.items():
        data = (data_dir() / name).read_bytes()
        found = hashlib.sha256(data).hexdigest()
        rows.append({"file": name, "bytes": len(data), "sha256": found, "matches_dryad": found == digest})
    return pd.DataFrame(rows)


def read_workbook() -> dict[str, pd.DataFrame]:
    """Every sheet of the workbook, as read (header row taken as the column names)."""
    return pd.read_excel(data_dir() / WORKBOOK, sheet_name=None)


def read_metadata() -> pd.DataFrame:
    return pd.read_csv(data_dir() / "Metadata.csv", encoding="utf-8-sig")


YEARLY = ["Flush_S1", "Dev_time", "Senes_10", "Senes_time", "Growth_length", "Tspring", "Tfall", "Tannual",
          "GDD", "Chill_days", "Height_growth", "Diameter_growth", "AGB_growth"]
LEAF = ["Photo", "Sugar", "Starch", "Predawn", "Midday"]
TREE = ["Tree", "Chamber", "Treatment", "Warming", "Soil moisture reduction", "Compartment", "Mixture", "Species"]
TREATMENTS = ["C", "MR", "W", "WMR"]
PHENOLOGY = ["Flush_S1", "Dev_time", "Senes_10", "Senes_time", "Growth_length"]
CARBON_GROWTH = ["Starch", "Sugar", "Photo", "Height_growth", "Diameter_growth", "AGB_growth"]
# Square root in Tables S1 to S3 (claims file, opening comment): starch, sugar, Asat, the increments and,
# in the interaction model, every trait of Tables S2 and S3.
SQRT_TREATMENT_TEST = set(CARBON_GROWTH)


def treatment_name(warming: str, reduction: str) -> str:
    """The paper's treatment name from the Warming and Soil moisture reduction columns (YES/NO)."""
    return {("NO", "NO"): "C", ("YES", "NO"): "W", ("NO", "YES"): "MR", ("YES", "YES"): "WMR"}[(warming, reduction)]


def load(raw: pd.DataFrame) -> pd.DataFrame:
    """The "Total Data" sheet with exact duplicate rows counted once, the paper's treatment names
    (`treat`), 0/1 indicators `W`, `M`, `I` (mixture), and the season (`season`, 1 to 3: the order of
    the campaign within its year)."""
    d = raw.drop_duplicates().copy()
    d["treat"] = [treatment_name(w, m) for w, m in zip(d["Warming"], d["Soil moisture reduction"])]
    d["W"] = (d["Warming"] == "YES").astype(int)
    d["M"] = (d["Soil moisture reduction"] == "YES").astype(int)
    d["I"] = (d["Mixture"] == "Mixture").astype(int)
    d["season"] = d["Campaign"] - 3 * (d["Year"] - 2019)
    return d


def campaign_table(d: pd.DataFrame) -> pd.DataFrame:
    """One row per tree and campaign; two different rows for one tree and campaign are averaged."""
    keys = TREE + ["treat", "W", "M", "I", "Year", "Campaign", "season"]
    return d.groupby(keys, as_index=False)[YEARLY + LEAF].mean()


def tree_year_table(d: pd.DataFrame) -> pd.DataFrame:
    """One row per tree and year: the yearly traits, and the leaf-level traits averaged over the
    campaigns of the year (the Methods' yearly tree means, reading L1)."""
    c = campaign_table(d)
    keys = TREE + ["treat", "W", "M", "I", "Year"]
    yearly = c.groupby(keys, as_index=False)[YEARLY].first()
    leaf = c.groupby(keys, as_index=False)[LEAF].mean()
    return yearly.merge(leaf, on=keys)


def transform(y: pd.Series, sqrt: bool, reading: str) -> tuple[pd.Series, str]:
    """The response of a model. Without the square root, unchanged. With it: when no value is negative,
    the square root; when some are, reading S1 leaves the trait untransformed and S2 takes the square root
    after adding the constant that brings the minimum to zero (claims file, opening comment)."""
    if not sqrt:
        return y, "none"
    low = y.min()
    if low >= 0:
        return np.sqrt(y), "sqrt"
    if reading == "S1":
        return y, "none (negatives, S1)"
    return np.sqrt(y - low), f"sqrt(x + {-low:.3g}) (S2)"


class LME:
    """A linear mixed model with a random intercept per chamber, fitted by REML (as nlme's lme)."""

    def __init__(self, data: pd.DataFrame, response: str, rhs: str, group: str = "Chamber"):
        data = data.dropna(subset=[response]).reset_index(drop=True)
        self.data = data
        y, X = patsy.dmatrices(f"{response} ~ {rhs}", data, return_type="dataframe")
        self.design_info = X.design_info
        self.names = list(X.columns)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            model = sm.MixedLM(y.iloc[:, 0].to_numpy(), X.to_numpy(), groups=data[group].to_numpy())
            fit = None
            for method in ("lbfgs", "powell", "nm"):
                try:
                    fit = model.fit(reml=True, method=method)
                    if fit.converged:
                        break
                except Exception:   # noqa: BLE001  try the next optimiser
                    continue
        self.fit = fit
        self.converged = bool(fit is not None and fit.converged)
        p = X.shape[1]
        self.beta = np.asarray(fit.fe_params)
        # The covariance of the fixed effects as nlme gives it, (X' V^-1 X)^-1 with V = s2 I + t2 J per chamber
        # at the REML estimates (statsmodels' joint covariance is not positive definite when t2 is at 0).
        s2, t2 = float(fit.scale), float(np.asarray(fit.cov_re).ravel()[0])
        Xa, info = X.to_numpy(), np.zeros((p, p))
        for g in pd.unique(data[group]):
            Xg = Xa[(data[group] == g).to_numpy()]
            ng = len(Xg)
            Vinv = (np.eye(ng) - t2 / (s2 + ng * t2) * np.ones((ng, ng))) / s2
            info += Xg.T @ Vinv @ Xg
        self.cov = np.linalg.inv(info)
        self.s2, self.t2 = s2, t2
        self.n = len(data)
        self.groups = data[group].nunique()
        # Chamber-level columns: constant within every chamber.
        Xd = pd.DataFrame(X.to_numpy(), columns=self.names)
        Xd["_g"] = data[group].to_numpy()
        spread = Xd.groupby("_g").agg(lambda s: s.max() - s.min()).max()
        self.between = [n for n in self.names if n != "Intercept" and spread[n] == 0]

    def anova_sequential(self) -> pd.DataFrame:
        """Sequential F tests of each term, as nlme's anova.lme."""
        A = np.linalg.inv(self.cov)
        L = np.linalg.cholesky((A + A.T) / 2)
        c0 = L.T @ self.beta
        p_between = len(self.between)
        p_within = len(self.names) - 1 - p_between
        rows = []
        for term, cols in self.design_info.term_name_slices.items():
            if term == "Intercept":
                continue
            names = self.names[cols]
            k = len(names)
            between = all(n in self.between for n in names)
            df_den = self.groups - 1 - p_between if between else self.n - self.groups - p_within
            F = float(np.sum(c0[cols] ** 2) / k)
            rows.append({"term": term, "numDF": k, "denDF": df_den, "F": F, "p": stats.f.sf(F, k, df_den)})
        return pd.DataFrame(rows)

    def anova_marginal(self) -> pd.DataFrame:
        """Marginal F tests of each term (nlme's anova.lme with type = "marginal"): the Wald test of the
        term's coefficients given all others, with the same denominator degrees of freedom."""
        seq = self.anova_sequential().set_index("term")
        rows = []
        for term, cols in self.design_info.term_name_slices.items():
            if term == "Intercept":
                continue
            b = self.beta[cols]
            k = len(b)
            F = float(b @ np.linalg.solve(self.cov[cols, cols], b) / k)
            den = seq.loc[term, "denDF"]
            rows.append({"term": term, "numDF": k, "denDF": den, "F": F, "p": stats.f.sf(F, k, den)})
        return pd.DataFrame(rows)

    def rows_for(self, cells: pd.DataFrame) -> np.ndarray:
        return np.asarray(patsy.build_design_matrices([self.design_info], cells)[0])

    def cell_means(self, cells: pd.DataFrame) -> pd.DataFrame:
        X = self.rows_for(cells)
        out = cells.copy()
        out["mean"] = X @ self.beta
        out["se"] = np.sqrt(np.einsum("ij,jk,ik->i", X, self.cov, X))
        return out


def single_step(z: np.ndarray, corr: np.ndarray, seed: int = 0) -> np.ndarray:
    """multcomp's single-step adjusted p-values (two-sided) for Wald z with correlation `corr`."""
    k = len(z)
    if k == 1:
        return 2 * stats.norm.sf(np.abs(z))
    mvn = stats.multivariate_normal(mean=np.zeros(k), cov=corr, allow_singular=True, seed=seed,
                                    maxpts=20000 * k, abseps=1e-5, releps=1e-4)
    out = []
    for t in np.abs(z):
        inside = mvn.cdf(np.full(k, t), lower_limit=np.full(k, -t))
        out.append(min(1.0, max(0.0, 1 - inside)))
    return np.array(out)


def contrasts(model: LME, cells: pd.DataFrame, pairs: list[tuple[int, int]], labels: list[str],
              seed: int = 0, weights: list[np.ndarray] | None = None) -> pd.DataFrame:
    """Contrasts of model cell means (row a minus row b of `cells` for each pair, or the weight vectors
    over the rows given in `weights`), Wald z and single-step p over the family given."""
    X = model.rows_for(cells)
    if weights is None:
        weights = []
        for a, b in pairs:
            w = np.zeros(len(cells))
            w[a], w[b] = 1, -1
            weights.append(w)
    K = np.array(weights) @ X
    est = K @ model.beta
    V = K @ model.cov @ K.T
    se = np.sqrt(np.diag(V))
    z = est / se
    corr = V / np.outer(se, se)
    return pd.DataFrame({"contrast": labels, "estimate": est, "se": se, "z": z,
                         "p_adj": single_step(z, corr, seed=seed)})


def treatment_test(data: pd.DataFrame, species: str, trait: str, years: list[int], sqrt: bool, s_reading: str,
                   seed: int = 0) -> dict:
    """Claims file, treatment test: monoculture trees of one species, lme(trait ~ (W + M + year)^3,
    random = ~1|Chamber), Tukey-type contrasts among the four treatments within each year.
    `data` is the tree-year table (L1) or the campaign table (L2)."""
    sub = data[(data.Species == species) & (data.Mixture == "Monoculture") & data.Year.isin(years)].copy()
    sub = sub.dropna(subset=[trait])
    sub["y"], how = transform(sub[trait], sqrt, s_reading)
    sub["Yr"] = sub["Year"].astype(str)
    m = LME(sub, "y", "(C(W) + C(M) + C(Yr))**3")
    order = [("C", 0, 0), ("MR", 0, 1), ("W", 1, 0), ("WMR", 1, 1)]
    out = []
    for i, yr in enumerate(sorted(set(years) & {2020, 2021})):
        cells = pd.DataFrame([{"W": w, "M": mm, "Yr": str(yr), "y": 0.0} for _, w, mm in order])
        pairs = [(a, b) for a in range(4) for b in range(4) if a > b]
        labels = [f"{order[a][0]}-{order[b][0]}" for a, b in pairs]
        c = contrasts(m, cells, pairs, labels, seed=seed + i)
        raw = sub[sub.Year == yr].groupby("treat")[trait].mean()
        c["raw_diff"] = [raw.get(order[a][0], np.nan) - raw.get(order[b][0], np.nan) for a, b in pairs]
        c["year"] = yr
        out.append(c)
    return {"contrasts": pd.concat(out, ignore_index=True), "anova": m.anova_sequential(),
            "anova_marginal": m.anova_marginal(),
            "transform": how, "n": len(sub), "converged": m.converged, "model": m}


def interaction_test(data: pd.DataFrame, species: str, trait: str, years: list[int], s_reading: str,
                     seed: int = 0) -> dict:
    """Claims file, interaction test: monoculture and mixture trees of one species, square root,
    lme(trait ~ (W + M + year + I)^3, random = ~1|Chamber); mixture minus monoculture within each
    treatment and year (I1) and within each treatment over 2020 and 2021 (I2)."""
    sub = data[(data.Species == species) & data.Year.isin(years)].copy().dropna(subset=[trait])
    sub["y"], how = transform(sub[trait], True, s_reading)
    sub["Yr"] = sub["Year"].astype(str)
    m = LME(sub, "y", "(C(W) + C(M) + C(Yr) + C(I))**3")
    order = [("C", 0, 0), ("MR", 0, 1), ("W", 1, 0), ("WMR", 1, 1)]
    rows = []
    k = 0
    for name, w, mm in order:
        cells = pd.DataFrame([{"W": w, "M": mm, "Yr": str(yr), "I": i, "y": 0.0}
                              for yr in (2020, 2021) for i in (1, 0)])
        for j, yr in enumerate((2020, 2021)):
            c = contrasts(m, cells, [(2 * j, 2 * j + 1)], ["mix-mono"], seed=seed + k)
            k += 1
            r = sub[(sub.treat == name) & (sub.Year == yr)].groupby("Mixture")[trait].mean()
            rows.append({"treat": name, "year": str(yr), "estimate": c.estimate[0], "z": c.z[0], "p": c.p_adj[0],
                         "raw_mix_minus_mono": r.get("Mixture", np.nan) - r.get("Monoculture", np.nan)})
        wv = np.array([0.5, -0.5, 0.5, -0.5])
        c = contrasts(m, cells, [], ["mix-mono"], seed=seed + k, weights=[wv])
        k += 1
        r = sub[(sub.treat == name) & sub.Year.isin([2020, 2021])].groupby("Mixture")[trait].mean()
        rows.append({"treat": name, "year": "2020-21", "estimate": c.estimate[0], "z": c.z[0], "p": c.p_adj[0],
                     "raw_mix_minus_mono": r.get("Mixture", np.nan) - r.get("Monoculture", np.nan)})
    return {"contrasts": pd.DataFrame(rows), "anova": m.anova_sequential(),
            "anova_marginal": m.anova_marginal(), "transform": how, "n": len(sub),
            "converged": m.converged}


def biodiversity_effects(data: pd.DataFrame, trait: str, reference: str, by_campaign: bool) -> pd.DataFrame:
    """Per mixture tree (and campaign, for L2): the net biodiversity effect NBE = (FO*WO - FE*WO)*100,
    the complementarity effect CE = N*(FO*WO/FE - WO)*FE*100, and the selection effect
    SE = (dRY - mean dRY)*FE*100, dRY = FO*WO/FE - WO, the mean over the mixture trees of the species in
    the treatment and year; WO = 0.5, N = 2 (claims file, opening comment, Eqs. 2 to 4).
    FE is the mean of the monoculture trees of the species, treatment and year (B1) or of the
    monoculture tree of the species in the tree's own chamber (B2; the mean when the chamber has two)."""
    WO, N = 0.5, 2
    keys = ["Species", "treat", "Year"] + (["season"] if by_campaign else [])
    mono = data[data.Mixture == "Monoculture"]
    mix = data[data.Mixture == "Mixture"][TREE + ["treat", "Year"] + (["season"] if by_campaign else []) + [trait]]
    mix = mix.rename(columns={trait: "FO"})
    if reference == "B1":
        fe = mono.groupby(keys)[trait].mean().rename("FE").reset_index()
        out = mix.merge(fe, on=keys, how="left")
    else:
        fe = mono.groupby(keys + ["Chamber"])[trait].mean().rename("FE").reset_index()
        out = mix.merge(fe, on=keys + ["Chamber"], how="left")
    out = out.dropna(subset=["FO", "FE"])
    out["NBE"] = (out.FO * WO - out.FE * WO) * 100
    out["dRY"] = out.FO * WO / out.FE - WO
    out["CE"] = N * out.dRY * out.FE * 100
    mean_dry = out.groupby(["Species", "treat", "Year"])["dRY"].transform("mean")
    out["SE"] = (out.dRY - mean_dry) * out.FE * 100
    return out


def t_tests(effects: pd.DataFrame, columns=("NBE", "CE", "SE")) -> pd.DataFrame:
    """One-sample t-tests against zero per species, treatment and year (the Methods' t-tests)."""
    rows = []
    for (sp, tr, yr), g in effects.groupby(["Species", "treat", "Year"]):
        for col in columns:
            v = g[col].replace([np.inf, -np.inf], np.nan).dropna()
            t, p = stats.ttest_1samp(v, 0.0) if len(v) > 1 else (np.nan, np.nan)
            rows.append({"Species": sp, "treat": tr, "Year": yr, "effect": col, "n": len(v),
                         "mean": v.mean(), "t": t, "p": p})
    return pd.DataFrame(rows)


def linear_fit(x, y) -> dict:
    r = stats.linregress(np.asarray(x, float), np.asarray(y, float))
    return {"slope": r.slope, "intercept": r.intercept, "r2": r.rvalue ** 2, "p": r.pvalue, "n": len(x)}


def nls_exponential(x, y, form: str) -> dict:
    """Negative exponential fits of y on x by least squares (R's nls), with Wald t tests of the parameters
    on the residual degrees of freedom as summary.nls gives them. (e) y = a exp(b x); (f) y = a + b exp(c x).
    The rate parameter is b for (e) and c for (f). Starting values come from a log-linear fit (e) or a grid
    of rates with linear least squares for a and b (f); a standard choice that does not change the optimum
    when the fit converges."""
    from scipy.optimize import curve_fit
    x, y = np.asarray(x, float), np.asarray(y, float)
    if form == "e":
        f = lambda t, a, b: a * np.exp(b * t)                              # noqa: E731
        lb = np.polyfit(x, np.log(y), 1)
        p0 = [np.exp(lb[1]), lb[0]]
        names, rate = ["a", "b"], "b"
    else:
        f = lambda t, a, b, c: a + b * np.exp(c * t)                       # noqa: E731
        best = None
        for c in -np.logspace(-4, 0, 200):
            A = np.column_stack([np.ones_like(x), np.exp(c * x)])
            coef, res, *_ = np.linalg.lstsq(A, y, rcond=None)
            sse = float(np.sum((A @ coef - y) ** 2))
            if best is None or sse < best[0]:
                best = (sse, [coef[0], coef[1], c])
        p0 = best[1]
        names, rate = ["a", "b", "c"], "c"
    try:
        popt, pcov = curve_fit(f, x, y, p0=p0, maxfev=20000)
    except Exception as err:   # noqa: BLE001  reported as a failed fit
        return {"form": form, "converged": False, "error": str(err)}
    df = len(x) - len(popt)
    se = np.sqrt(np.diag(pcov))
    out = {"form": form, "converged": bool(np.all(np.isfinite(se))), "n": len(x), "df": df}
    for n, v, s in zip(names, popt, se):
        out[n] = v
        out[f"p_{n}"] = 2 * stats.t.sf(abs(v / s), df) if s > 0 else np.nan
    fitted = f(x, *popt)
    out["r2"] = 1 - np.sum((y - fitted) ** 2) / np.sum((y - y.mean()) ** 2)
    out["rate"] = popt[names.index(rate)]
    out["p_rate"] = out[f"p_{rate}"]
    grid = np.linspace(x.min(), x.max(), 50)
    out["decreasing"] = bool(np.all(np.diff(f(grid, *popt)) < 0))
    return out
