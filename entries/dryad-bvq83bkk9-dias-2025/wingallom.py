"""Loading, model fitting and summaries for Dryad dataset bvq83bkk9 (version 333377).

Dias, Lemoine, Yanco, Zimova, Bay & Weeks (2025), Proc. R. Soc. B, doi:10.1098/rspb.2024.2556.

The dataset's Data.zip holds the specimens (`morphdata.csv`), the climate of each species and year
for the three classes (`ed_FHY.csv`, `ed_AHYspring.csv`, `ed_AHYfall.csv`, already scaled within
species), the phylogeny (`chitree.rds`) and catalogue numbers (`catnodata.csv`). Dryad needs a token
to download, so the workflow stages the files of the pinned version in `STAGED`, checked against the
SHA-256 of Dryad's file list; they are read from there into memory and never written.

Where the parameters come from (all from the claims file, which takes them from the paper's code,
Zenodo doi:10.5281/zenodo.14226724, Code.zip, Script01_MainAnalyses.R, Script02_SupplementAnalyses.R
and lm_mod.stan):

- Log transform and scaling within species over all specimens, the class split, the climate
  columns selected by number from the merged climate table, the dropping of species-years with a
  missing value, and the year coding: `prepare`, as Script01 (main models) and Script02
  (preliminary models) do. Column numbers are those of R's `merge` output, which `r_merge`
  rebuilds.
- The outlier filter of the Methods (five median absolute deviations), readings (a) to (d) of the
  claims file: `outlier_mask`.
- The hierarchical model: lm_mod.stan, read from Code.zip and ported to current Stan array syntax
  (`port_stan`, no change to the model), run with CmdStan's NUTS, adapt_delta 0.85, 4 chains of
  4000 iterations with 2000 warm-up, and the code's seeds (`fit_stan`). The code ran it with
  rstan, whose Stan version and random streams differ, so draws are not identical.
- The preliminary phylogenetic mixed models: MCMCglmm cannot be installed in this Python
  environment, so `gibbs_glmm` samples the same model (Gaussian, one random effect of species
  with the inverse of the scaled tip covariance of the phylogeny, inverse-Wishart priors V = 1,
  nu = 0.02, flat fixed-effect prior N(0, 1e10)) with the same blocked Gibbs scheme, 15 000
  iterations, 5000 burn-in and MCMCglmm's default thinning of 10. Its seeds are a standard
  choice (the code sets none).
- Summaries as the code prints them: quantiles of the pooled chains (summary of an mcmc.list),
  HPD intervals and pMCMC of chain 4 (summary of an MCMCglmm fit), the VIF function of Script02,
  lambda and its posterior mode (MCMCglmm's posterior.mode, a density with adjust 0.1).
- Probability of direction: the share of draws with the sign of the posterior median, a standard
  choice the claims file names (bayestestR's p_direction).
"""

from __future__ import annotations

import gzip
import hashlib
import io
import re
import urllib.request
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd

DRYAD_ID = "bvq83bkk9"
DRYAD_VERSION = "333377"
STAGED = Path("/tmp") / "dryad" / DRYAD_ID / DRYAD_VERSION  # where the workflow stages them (docs/archives.md)
SHA256 = {  # Dryad file list, https://datadryad.org/api/v2/versions/333377/files
    "Data.zip": "2185ac50e9a59c3a1dff59473216de2ab001d0d0044b1fa15442ae18a520d554",
    "README.md": "6c19de67b1c6c52802be42a6593c175a02bee0dab0ca2f6f958f08a0a3fa0482",
}
CODE_URL = "https://zenodo.org/api/records/14226724/files/Code.zip/content"
CODE_SHA256 = "cc9f58b9855aec4e3aca09be4138707d07fc34739ec5762e54e1f5bca48ddbc8"

SPECIES = ["Junco_hyemalis", "Melospiza_georgiana", "Melospiza_melodia", "Seiurus_aurocapilla",
           "Zonotrichia_albicollis"]
CLASSES = ["HY", "spring AHY", "autumn AHY"]
ED_FILE = {"HY": "ed_FHY.csv", "spring AHY": "ed_AHYspring.csv", "autumn AHY": "ed_AHYfall.csv"}

# Script01: columns of the merged climate table (R, 1-based), and the rows it drops.
MAIN_COLUMNS = {
    "HY": [40, 41, *range(33, 39), *range(27, 33), *range(15, 21), *range(21, 27), 1, 2, 70],
    "spring AHY": [41, *range(28, 34), *range(16, 22), *range(22, 28), 6, 15, 1, 2, 70],
    "autumn AHY": [68, *range(54, 60), *range(60, 66), 66, 5, 1, 2, 70],
}
MAIN_DROPPED = {"HY": [3, 75], "spring AHY": [1, 37, 73, 109, 115, 145],
                "autumn AHY": [1, 36, 106, 111, 112, 142]}
# Script02: the same for the preliminary models.
PRELIM_COLUMNS = {
    "HY": [40, 41, 4, *range(33, 39), *range(27, 33), *range(15, 21), *range(21, 27), 5, 1, 2, 70],
    "spring AHY": [40, 41, 5, *range(34, 40), *range(28, 34), *range(16, 22), *range(22, 28), 6, 13,
                   15, 7, 1, 2, 70],
    "autumn AHY": [67, 68, 69, *range(42, 48), *range(48, 54), *range(54, 60), *range(60, 66), 66, 40,
                   41, 4, *range(33, 39), *range(27, 33), *range(15, 21), *range(21, 27), 5, 1, 2, 70],
}
PRELIM_DROPPED = {"HY": [3, 6, 39, 75, 78, 113, 146],
                  "spring AHY": [1, 4, 6, 7, 37, 39, 40, 73, 76, 78, 79, 109, 115, 145, 147, 148],
                  "autumn AHY": [1, 3, 4, 6, 7, 36, 38, 39, 73, 74, 76, 77, 106, 111, 112, 142, 144,
                                 145]}
YEAR_ORIGIN = {"HY": 1998, "spring AHY": 1999, "autumn AHY": 1998}

# Predictors of the main models (Script01) and the sensitivity models (Script02), in table order.
MAIN_PREDICTORS = {
    "HY": ["PrevTempWinMo", "PrevPrecipWinMo", "AvgTempPreBreedBase", "PrecipPreBreedBase",
           "TempBreedMoBase", "PrecipBreedMoBase", "y_id"],
    "spring AHY": ["PrevPrecipWinMo", "PrecipPreBreedBase", "TempBreedMoBase", "PrecipBreedMoBase",
                   "MinTempFallMig", "PrecipWinMo", "y_id"],
    "autumn AHY": ["PrevPrevPrecipWinMo", "PrevTempBreedBase", "PrevPrecipBreedBase",
                   "PrevMinTempFallMig", "MinTempFallMig", "y_id"],
}
STAN_SEEDS = {"HY": 9, "spring AHY": 5, "autumn AHY": 9}
SENSITIVITY_SEEDS = {"HY": 10, "spring AHY": 5, "autumn AHY": 9}


def sensitivity_predictors(cls: str, crop: str) -> list[str]:
    """Main-model predictors with the breeding-range variables taken over range `crop` (B1, B2)."""
    return [p.replace("Base", crop) for p in MAIN_PREDICTORS[cls]]


# Climate terms of the preliminary models (Script02), each also with its tarsus interaction.
PRELIM_TERMS = {
    "HY": ["PrevTempWinMo", "PrevPrecipWinMo", "MinTempSpringMig", "AvgTempPreBreedBase",
           "PrecipPreBreedBase", "TempBreedMoBase", "PrecipBreedMoBase", "MinTempFallMig", "y_id"],
    "spring AHY": ["PrevTempWinMo", "PrevPrecipWinMo", "MinTempSpringMig", "AvgTempPreBreedBase",
                   "PrecipPreBreedBase", "TempBreedMoBase", "PrecipBreedMoBase", "MinTempFallMig",
                   "TempWinMo", "PrecipWinMo", "MinTempNextSpringMig", "y_id"],
    "autumn AHY": ["PrevPrevTempWinMo", "PrevPrevPrecipWinMo", "PrevMinTempSpringMig",
                   "PrevAvgTempPreBreedBase", "PrevPrecipPreBreedBase", "PrevTempBreedBase",
                   "PrevPrecipBreedBase", "PrevMinTempFallMig", "PrevTempWinMo", "PrevPrecipWinMo",
                   "MinTempSpringMig", "AvgTempPreBreedBase", "PrecipPreBreedBase",
                   "TempBreedMoBase", "PrecipBreedMoBase", "MinTempFallMig", "y_id"],
}
TREND_VARIABLES = ["AvgTempPreBreedBase", "PrecipPreBreedBase", "TempBreedMoBase",
                   "PrecipBreedMoBase", "MinTempFallMig", "TempWinMo", "PrecipWinMo",
                   "MinTempSpringMig"]


# ---------------------------------------------------------------- reading


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def check_staged() -> dict[str, str]:
    """SHA-256 of each staged file; raises if any differs from Dryad's file list."""
    found = {name: sha256(STAGED / name) for name in SHA256}
    for name, digest in found.items():
        if digest != SHA256[name]:
            raise ValueError(f"{name}: SHA-256 {digest} is not Dryad's {SHA256[name]}")
    return found


def data_zip() -> zipfile.ZipFile:
    return zipfile.ZipFile(STAGED / "Data.zip")


def read_csv(name: str) -> pd.DataFrame:
    """A CSV of Data.zip, by file name, as R's read.csv reads it (first column kept)."""
    with data_zip() as z:
        path = next(n for n in z.namelist() if n.endswith("/" + name) and "__MACOSX" not in n)
        return pd.read_csv(z.open(path))


def read_tree() -> dict:
    """chitree.rds, an ape `phylo` object: edges, edge lengths and tip labels."""
    import rdata
    with data_zip() as z:
        raw = z.read("Data/Files/chitree.rds")
    parsed = rdata.parser.parse_data(gzip.decompress(raw))
    obj = rdata.conversion.convert(parsed, default_encoding="utf8")
    return {"edge": np.asarray(obj["edge"], dtype=int), "edge_length": np.asarray(obj["edge.length"], float),
            "tip_label": [str(t) for t in obj["tip.label"]], "Nnode": int(np.asarray(obj["Nnode"]).ravel()[0])}


def tip_covariance(tree: dict, tips: list[str]) -> pd.DataFrame:
    """Shared branch length from the root for each pair of `tips` (ape::vcv.phylo, after drop.tip).

    Dropping tips does not change the shared root-to-tip lengths of the tips kept, so they are
    read from the full tree.
    """
    edge, length = tree["edge"], tree["edge_length"]
    parent = {c: (p, l) for (p, c), l in zip(edge, length)}

    def path(node):
        out = {}
        while node in parent:
            p, l = parent[node]
            out[(p, node)] = l
            node = p
        return out

    idx = {t: i + 1 for i, t in enumerate(tree["tip_label"])}
    paths = {t: path(idx[t]) for t in tips}
    cov = np.array([[sum(l for e, l in paths[a].items() if e in paths[b]) for b in tips] for a in tips])
    return pd.DataFrame(cov, index=tips, columns=tips)


def scaled_tip_inverse(tree: dict, tips: list[str]) -> np.ndarray:
    """MCMCglmm::inverseA(phy, nodes = "TIPS", scale = TRUE)$Ainv for an ultrametric tree.

    scale = TRUE divides the branch lengths by the root-to-tip distance, so the tip covariance
    has a unit diagonal; its inverse is returned, rows in the order of `tips`.
    """
    cov = tip_covariance(tree, tips).to_numpy()
    return np.linalg.inv(cov / cov[0, 0])


# ---------------------------------------------------------------- preparing


def outlier_mask(morph: pd.DataFrame, reading: str) -> pd.Series:
    """True for specimens the Methods' 5-MAD filter removes, under the claims file's readings.

    (a) no filter; (b) per species on raw tarsus and wing, R's mad() with constant 1.4826;
    (c) as (b) per species and sex; (d) as (b) with the unscaled MAD (constant 1).
    """
    out = pd.Series(False, index=morph.index)
    if reading == "a":
        return out
    groups = ["Taxon", "Sex"] if reading == "c" else ["Taxon"]
    const = 1.0 if reading == "d" else 1.4826
    for _, g in morph.groupby(groups):
        for v in ["Tarsus", "Wing"]:
            med = g[v].median()
            mad = const * np.median(np.abs(g[v] - med))
            out[g.index] |= np.abs(g[v] - med) > 5 * mad
    return out


def r_scale(x: pd.Series) -> pd.Series:
    return (x - x.mean()) / x.std(ddof=1)


def morph_prepared(reading: str = "a") -> pd.DataFrame:
    """morphdata.csv after the filter reading, with Script01's derived columns."""
    m = read_csv("morphdata.csv")
    m = m[~outlier_mask(m, reading)].reset_index(drop=True)
    m["spyear"] = pd.factorize(m.Taxon + " " + m.Year.astype(str), sort=True)[0] + 1
    m["Sex2"] = (m.Sex == "f").astype(int)
    m["Taxon2"] = m.Taxon.map({s: i + 1 for i, s in enumerate(SPECIES)})
    m["scaleTarsus"] = np.log(m.Tarsus).groupby(m.Taxon).transform(r_scale)
    m["scaleWing"] = np.log(m.Wing).groupby(m.Taxon).transform(r_scale)
    return m


def class_specimens(m: pd.DataFrame, cls: str) -> pd.DataFrame:
    if cls == "HY":
        return m[(m.Season == "Fall") & (m.NewAge == "HY")]
    if cls == "spring AHY":
        return m[m.Season == "Spring"]
    return m[(m.Season == "Fall") & (m.NewAge == "AHY")]


def r_merge(ed: pd.DataFrame, md: pd.DataFrame) -> pd.DataFrame:
    """R's merge(ed[,-1], unique(md[, c(Taxon, Year, spyear)]), by spec_id/y_id = Taxon/Year).

    Columns: the keys, then the other columns of the climate table, then spyear; rows sorted
    by the keys, as R sorts them.
    """
    ed = ed.iloc[:, 1:]
    sp = md[["Taxon", "Year", "spyear"]].drop_duplicates()
    out = ed.merge(sp, left_on=["spec_id", "y_id"], right_on=["Taxon", "Year"], how="inner",
                   suffixes=("", "_morph"))
    others = [c for c in ed.columns if c not in ("spec_id", "y_id")]
    out = out[["spec_id", "y_id", *others, "spyear"]]
    return out.sort_values(["spec_id", "y_id"]).reset_index(drop=True)


def prepare(m: pd.DataFrame, cls: str, which: str = "main") -> dict:
    """Script01 (`which` = "main") or Script02 ("prelim") data preparation for one class.

    Returns the specimens kept (`md`, with spyear2), the species-year table (`G`, with spyear2,
    species index and the coded year), and the rows dropped for missing values.
    """
    columns = (MAIN_COLUMNS if which == "main" else PRELIM_COLUMNS)[cls]
    dropped_code = (MAIN_DROPPED if which == "main" else PRELIM_DROPPED)[cls]
    md = class_specimens(m, cls)
    merged = r_merge(read_csv(ED_FILE[cls]), md)
    sel = merged.iloc[:, [c - 1 for c in columns]]
    missing = [i + 1 for i in np.flatnonzero(sel.isna().any(axis=1).to_numpy())]
    kept = sel.drop(index=[i - 1 for i in missing])
    md_new = md[md.spyear.isin(kept.spyear)].copy()
    md_new["spyear2"] = pd.factorize(md_new.Taxon + " " + md_new.Year.astype(str), sort=True)[0] + 1
    key = md_new[["Taxon", "Year", "spyear2"]].drop_duplicates()
    G = kept.merge(key, left_on=["spec_id", "y_id"], right_on=["Taxon", "Year"]).drop(
        columns=["Taxon", "Year"]).sort_values("spyear2").reset_index(drop=True)
    G["species"] = G.spec_id.map({s: i + 1 for i, s in enumerate(sorted(G.spec_id.unique()))})
    G["year"] = G.y_id
    G["y_id"] = (G.y_id - YEAR_ORIGIN[cls]) / 10
    return {"md": md_new.reset_index(drop=True), "G": G, "selected": list(sel.columns),
            "missing_rows": missing, "dropped_rows": dropped_code, "n_merged": len(sel)}


def stan_data(prep: dict, predictors: list[str]) -> dict:
    md, G = prep["md"], prep["G"]
    Gm = np.column_stack([np.ones(len(G)), G[predictors].to_numpy(float)])
    return {
        "N": len(md), "X": np.column_stack([np.ones(len(md)), md.scaleTarsus]),
        "Z": np.column_stack([md.Sex2, md.Sex2 * md.scaleTarsus]),
        "WL": md.scaleWing.to_numpy(float), "spyear": md.spyear2.to_numpy(int),
        "species_obs": md.Taxon2.to_numpy(int), "J": int(md.spyear2.max()), "E": Gm.shape[1],
        "G": Gm, "species": G.species.to_numpy(int), "K": int(G.species.max()),
    }


# ---------------------------------------------------------------- the paper's code


def code_zip() -> zipfile.ZipFile:
    """Code.zip of Zenodo record 14226724, in memory, checked against its SHA-256."""
    with urllib.request.urlopen(CODE_URL, timeout=120) as r:
        raw = r.read()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != CODE_SHA256:
        raise ValueError(f"Code.zip SHA-256 {digest} is not {CODE_SHA256}")
    return zipfile.ZipFile(io.BytesIO(raw))


def port_stan(code: str) -> str:
    """lm_mod.stan in the array syntax of Stan 2.33 and later; the model is unchanged."""
    code = re.sub(r"vector\[(\w+)\] (\w+)\[(\w+)\];", r"array[\3] vector[\1] \2;", code)
    code = re.sub(r"int<lower=(\d)> (\w+)\[(\w+)\];", r"array[\3] int<lower=\1> \2;", code)
    return code


CMDSTAN_VERSION = "2.40.0"


def install_cmdstan(root: Path) -> str:
    """CmdStan at a fixed release, built under `root` (PyStan's httpstan does not load on Python
    3.13, so the Stan model runs through cmdstanpy)."""
    import cmdstanpy
    target = root / f"cmdstan-{CMDSTAN_VERSION}"
    if not (target / "bin" / "stanc").exists():
        cmdstanpy.install_cmdstan(version=CMDSTAN_VERSION, dir=str(root), cores=4, progress=False)
    cmdstanpy.set_cmdstan_path(str(target))
    return str(target)


def compile_stan(model_code: str, workdir: Path):
    import cmdstanpy
    path = workdir / "lm_mod.stan"
    path.write_text(model_code)
    # Script01 compiles with LOCAL_CPPFLAGS = '-march=native'
    return cmdstanpy.CmdStanModel(stan_file=str(path), cpp_options={"CXXFLAGS": "-march=native"})


def fit_stan(model, data: dict, seed: int, workdir: Path) -> dict:
    """NUTS as Script01 runs it: adapt_delta 0.85, 4 chains, 2000 warm-up and 2000 kept draws.

    Returns the draws of mu_i and mu_s (draws by column of G, the four chains one after another),
    the species-level I and S, the sampler diagnostics, and CmdStan's summary of mu_i and mu_s."""
    fit = model.sample(data=data, chains=4, parallel_chains=4, iter_warmup=2000, iter_sampling=2000,
                       adapt_delta=0.85, seed=seed, output_dir=str(workdir), show_progress=False)
    summary = fit.summary()
    keep = summary.index.str.match(r"^(mu_i|mu_s|sd_y|sd_b|sd_i|sd_s|mu_stl)\[?")
    divergent = fit.method_variables()["divergent__"]
    return {"mu_i": fit.stan_variable("mu_i"), "mu_s": fit.stan_variable("mu_s"),
            "I": fit.stan_variable("I"), "S": fit.stan_variable("S"), "chains": 4,
            "divergent": int(divergent.sum()),
            "divergent_per_chain": [int(d) for d in divergent.sum(axis=0)],
            "max_rhat": float(summary.loc[keep, "R_hat"].max()),
            "min_ess_bulk": float(summary.loc[keep, "ESS_bulk"].min()),
            "mu_summary": summary.loc[summary.index.str.match(r"^mu_[is]\["),
                                      ["Mean", "MCSE", "R_hat", "ESS_bulk", "ESS_tail"]]}


def pd_direction(draws: np.ndarray) -> float:
    """Share of draws with the sign of the median (bayestestR p_direction)."""
    med = np.median(draws)
    return float(np.mean(draws > 0) if med >= 0 else np.mean(draws < 0))


def ess(x: np.ndarray) -> float:
    """Effective sample size of draws `x` (chains by draws), as Stan computes it (split R-hat
    variance and Geyer's initial monotone sequence; no rank normalisation)."""
    x = np.asarray(x, float)
    half = x.shape[1] // 2
    x = np.vstack([x[:, :half], x[:, half:2 * half]])          # split chains
    m, n = x.shape
    centred = x - x.mean(axis=1, keepdims=True)
    f = np.fft.rfft(centred, n=2 * n, axis=1)
    acov = np.fft.irfft(f * np.conj(f), axis=1)[:, :n] / n
    chain_var = acov[:, 0] * n / (n - 1)
    w_ = chain_var.mean()
    var_plus = w_ * (n - 1) / n + x.mean(axis=1).var(ddof=1)
    if var_plus == 0:
        return float("nan")
    rho = 1 - (w_ - acov.mean(axis=0)) / var_plus
    rho[0] = 1.0
    pairs = []
    for t in range(0, n - 1, 2):
        s = rho[t] + rho[t + 1]
        if s < 0:
            break
        pairs.append(min(s, pairs[-1]) if pairs else s)
    tau = -1 + 2 * sum(pairs)
    return float(m * n / max(tau, 1 / np.log10(m * n)))


def pd_mcse(draws: np.ndarray, chains: int) -> tuple[float, float]:
    """Monte Carlo standard error of pd_direction, from the effective sample size of the indicator
    of the median's sign, and that effective sample size (a standard choice, the MCSE of a
    probability)."""
    med = np.median(draws)
    ind = (draws > 0 if med >= 0 else draws < 0).astype(float).reshape(chains, -1)
    n_eff = ess(ind)
    p = ind.mean()
    return float(np.sqrt(p * (1 - p) / n_eff)), n_eff


def effect_table(fit: dict, predictors: list[str]) -> pd.DataFrame:
    """Posterior mean, s.d. and pd of mu_i and mu_s, one row per column of G (as Tables 1 to 3),
    with the Monte Carlo error of each pd and the pd of each chain."""
    rows = []
    mu_i, mu_s, chains = fit["mu_i"], fit["mu_s"], fit["chains"]
    for k, name in enumerate(["Intercept", *predictors]):
        row = {"term": name}
        for part, mu in (("int", mu_i), ("slope", mu_s)):
            x = mu[:, k]
            mcse, n_eff = pd_mcse(x, chains)
            positive = np.median(x) >= 0   # each chain's share of draws with the pooled median's sign
            row.update({f"{part}_mean": x.mean(), f"{part}_sd": x.std(ddof=1), f"{part}_pd": pd_direction(x),
                        f"{part}_pd_mcse": mcse, f"{part}_pd_ess": n_eff,
                        f"{part}_pd_chains": [float(np.mean(c > 0) if positive else np.mean(c < 0))
                                              for c in x.reshape(chains, -1)]})
        rows.append(row)
    return pd.DataFrame(rows).set_index("term")


# ---------------------------------------------------------------- preliminary models


def prelim_design(prep: dict, terms: list[str]) -> tuple[np.ndarray, list[str], np.ndarray, np.ndarray]:
    """Fixed-effect design of Script02's formulas: intercept, tarsus, sex, each term, then the
    tarsus interactions; and the species index of each specimen."""
    df = prep["md"].merge(prep["G"].drop(columns=["year"]), left_on=["Taxon", "spyear2"],
                          right_on=["spec_id", "spyear2"])
    t = df.scaleTarsus.to_numpy(float)
    cols = {"(Intercept)": np.ones(len(df)), "scaleTarsus": t, "Sex21": df.Sex2.to_numpy(float)}
    for term in terms:
        cols[term] = df[term].to_numpy(float)
    cols["scaleTarsus:Sex21"] = t * df.Sex2.to_numpy(float)
    for term in terms:
        cols[f"scaleTarsus:{term}"] = t * df[term].to_numpy(float)
    X = np.column_stack(list(cols.values()))
    return X, list(cols), df.scaleWing.to_numpy(float), df.Taxon.to_numpy()


def gibbs_glmm(X: np.ndarray, y: np.ndarray, groups: np.ndarray, group_names: list[str],
               Ainv: np.ndarray, rng: np.random.Generator, nitt: int = 15000, burnin: int = 5000,
               thin: int = 10, V: float = 1.0, nu: float = 0.02, fixed_var: float = 1e10) -> dict:
    """Gaussian mixed model y = X b + Z u + e, u ~ N(0, s2u A), e ~ N(0, s2e), as MCMCglmm samples it.

    Each iteration draws (b, u) jointly from their full conditional, then each variance from its
    inverse-Wishart (scalar: inverse-gamma) full conditional with prior V, nu. Returns the kept
    draws of b (`Sol`) and of the two variances (`VCV`, columns species and units).
    """
    n, p = X.shape
    q = len(group_names)
    gidx = pd.Index(group_names).get_indexer(groups)
    Z = np.zeros((n, q))
    Z[np.arange(n), gidx] = 1.0
    W = np.hstack([X, Z])
    WtW, Wty, yty = W.T @ W, W.T @ y, y @ y
    s2e, s2u = float(np.var(y)), 1.0
    sol, vcv = [], []
    prior_prec = np.zeros((p + q, p + q))
    prior_prec[:p, :p] = np.eye(p) / fixed_var
    for it in range(nitt):
        C = WtW / s2e + prior_prec
        C[p:, p:] += Ainv / s2u
        L = np.linalg.cholesky(C)
        mean = np.linalg.solve(L.T, np.linalg.solve(L, Wty / s2e))
        theta = mean + np.linalg.solve(L.T, rng.standard_normal(p + q))
        u = theta[p:]
        sse = yty - 2 * theta @ Wty + theta @ WtW @ theta
        s2e = 1.0 / rng.gamma((nu + n) / 2, 2.0 / (nu * V + sse))
        s2u = 1.0 / rng.gamma((nu + q) / 2, 2.0 / (nu * V + u @ Ainv @ u))
        if it >= burnin and (it - burnin) % thin == 0:
            sol.append(theta[:p])
            vcv.append((s2u, s2e))
    return {"Sol": np.array(sol), "VCV": np.array(vcv), "X": X}


def hpd(x: np.ndarray, prob: float = 0.95) -> tuple[float, float]:
    """coda::HPDinterval."""
    v = np.sort(x)
    n = len(v)
    gap = max(1, min(n - 1, round(n * prob)))
    i = int(np.argmin(v[gap:] - v[:n - gap]))
    return float(v[i]), float(v[i + gap])


def pmcmc(x: np.ndarray) -> float:
    """MCMCglmm's pMCMC: twice the smaller tail share, at least 1/n."""
    n = len(x)
    return float(2 * max(0.5 / n, min(np.mean(x > 0), np.mean(x < 0))))


def posterior_mode(x: np.ndarray, adjust: float = 0.1) -> float:
    """MCMCglmm::posterior.mode: the peak of R's density(x, adjust = 0.1) (bw.nrd0, 512 points)."""
    n = len(x)
    lo = min(np.std(x, ddof=1), (np.quantile(x, 0.75) - np.quantile(x, 0.25)) / 1.34)
    bw = 0.9 * lo * n ** -0.2 * adjust
    grid = np.linspace(x.min() - 3 * bw, x.max() + 3 * bw, 512)
    dens = np.exp(-0.5 * ((grid[:, None] - x[None, :]) / bw) ** 2).sum(axis=1)
    return float(grid[np.argmax(dens)])


def vif(X: np.ndarray, names: list[str]) -> pd.Series:
    """vif.MCMCglmm of Script02: diagonal of the inverse correlation matrix of the fixed effects,
    intercept left out."""
    c = np.corrcoef(X[:, 1:], rowvar=False)
    return pd.Series(np.diag(np.linalg.inv(c)), index=names[1:])


def glmm_summary(chains: list[dict], names: list[str]) -> pd.DataFrame:
    """Per fixed effect: pooled mean and 2.5-97.5% quantiles (reading i), chain 4 mean, HPD and
    pMCMC (reading ii)."""
    pooled = np.vstack([c["Sol"] for c in chains])
    c4 = chains[3]["Sol"]
    rows = []
    for k, name in enumerate(names):
        lo, hi = hpd(c4[:, k])
        rows.append({"term": name, "mean_pooled": pooled[:, k].mean(),
                     "q2.5_pooled": np.quantile(pooled[:, k], 0.025),
                     "q97.5_pooled": np.quantile(pooled[:, k], 0.975),
                     "mean_c4": c4[:, k].mean(), "hpd_lo_c4": lo, "hpd_hi_c4": hi,
                     "pMCMC_c4": pmcmc(c4[:, k])})
    out = pd.DataFrame(rows).set_index("term")
    out["excl0_i"] = (out["q2.5_pooled"] > 0) | (out["q97.5_pooled"] < 0)
    out["excl0_ii"] = (out.hpd_lo_c4 > 0) | (out.hpd_hi_c4 < 0)
    return out
