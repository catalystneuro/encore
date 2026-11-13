"""Loading and encoding measures for CRCNS ofc-3 (Saez et al. 2018, Current Biology).

Saez, Lin, Stolk, Chang, Parvizi, Schalk, Knight & Hsu (2018), doi:10.1016/j.cub.2018.07.045.
Data set: CRCNS ofc-3, doi:10.6080/K0VM49GF, unversioned, read from the public S3 bucket
crcnsarchive under ofc-3/live/. Zip members are streamed over range requests with fsspec and
zipfile and loaded in memory; nothing is written to disk.

What the files hold (checked in the notebook):

- data.zip, data/data_ephys/sXX_ofc_hg_events.mat: HFA (70-200 Hz analytic amplitude) epochs of
  3,001 samples at 1 kHz, [-1, 2] s around game presentation (`game_*`) and around the
  "buttonpress" event (`buttonpress_*`), trials x samples x electrodes, and their 200-ms window
  averages at 50-ms steps (`*_window_events_hg`, 57 windows; window k is the mean of samples
  50k to 50k+200, so its centre is at -900 + 50k ms).
- data.zip, data/data_behav/gamble.data.sXX.csv: one row per round (event times, choice,
  outcome); gamble_choices.csv: the prize and the shown and hidden numbers of each round.
- ofc_behav_data.zip, sXX_behav_globals.mat: the authors' regressors, one value per HFA trial.

Where the parameters come from:

- Window grid, encoding rule (p < 0.05 in 5 or more consecutive windows, each epoch on its own),
  %EV as the R2 of a separate linear regression per electrode, regressor and window, and 1,000
  label shuffles for chance: the claims file's opening comment and fig3-present-encoding
  criterion (STAR Methods, ECoG analysis and behavioral regression).
- Regressor definitions: the authors' own values in sXX_behav_globals.mat (win probability
  (10 - shown)/10, risk p(1 - p), chosen value, gamble, win, loss, RPE, regret and their t-1
  versions). Lags t-2 to t-5 are built here by the convention the t-1 file values follow (the
  regressor of the round k rounds back, see `past_regressors`); STAR Methods, Behavioral
  Analysis: "We used the same parameterization as for current regressors, but derived using
  information from earlier trials (one trial back, t-1, through 5 trials back, t-5)".
- Matching of HFA trials to rounds (`align_trials`): the files give no round number for the HFA
  trials, which are fewer than the non-timeout rounds; each trial is matched to the first
  remaining non-timeout round whose win probability, choice, win and regret equal the trial's
  regressors (a choice made here; the notebook shows that every trial matches).
- Stepwise regression (`stepwise_*`): STAR Methods, Stepwise regression. The sum of F over the
  longest significant stretch is taken in each epoch and the larger of the two is used, and the
  model comparison runs at a stated time window; both are assumptions, stated in the notebook.
- Random seeds are standard choices that cannot change a result beyond permutation noise.
"""

from __future__ import annotations

import io
import zipfile

import fsspec
import numpy as np
import pandas as pd
import scipy.io as sio
from scipy import optimize, stats

BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ofc-3/live"
DATASET_DOI = "10.6080/K0VM49GF"
SUBJECTS = [f"s{i:02d}" for i in range(1, 11)]
N_WIN = 57
WIN_CENTRES_MS = -900 + 50 * np.arange(N_WIN)   # 200-ms windows from [-1000, -800] ms
EPOCHS = ("game", "buttonpress")
MIN_RUN = 5          # consecutive windows, claims file (STAR Methods)
ALPHA = 0.05

CURRENT = ["risk", "gamble_ind", "winprob", "exputil", "win_ind", "loss_ind", "rpe", "regret"]
LABELS = {"risk": "risk", "gamble_ind": "gamble", "winprob": "offer value (win prob.)",
          "exputil": "chosen value", "win_ind": "win index", "loss_ind": "loss index",
          "rpe": "RPE", "regret": "regret"}
CHOICE = CURRENT[:4]
OUTCOME = CURRENT[4:]


def _zip(name: str) -> zipfile.ZipFile:
    return zipfile.ZipFile(fsspec.open(f"{BASE}/{name}", block_size=2**20).open())


def checksums() -> dict:
    """MD5 sums the data set publishes in checksums.md5."""
    with fsspec.open(f"{BASE}/checksums.md5", "rt") as f:
        return {line.split()[1]: line.split()[0] for line in f if line.strip()}


def load_behaviour() -> dict:
    """Per subject: the rounds table (csv joined with gamble_choices.csv) and the globals."""
    z = _zip("data.zip")
    zb = _zip("ofc_behav_data.zip")
    games = pd.read_csv(z.open("data/data_behav/gamble_choices.csv"))
    out = {}
    for s in SUBJECTS:
        rounds = pd.read_csv(z.open(f"data/data_behav/gamble.data.{s}.csv"))
        rounds = pd.concat([rounds, games.iloc[: len(rounds)].reset_index(drop=True)], axis=1)
        g = sio.loadmat(io.BytesIO(zb.read(f"ofc_behav_data/{s}_behav_globals.mat")))
        glob = pd.DataFrame({k: v.ravel().astype(float) for k, v in g.items() if not k.startswith("__")})
        out[s] = {"rounds": round_regressors(rounds), "globals": glob}
    return out


def round_regressors(r: pd.DataFrame) -> pd.DataFrame:
    """Regressors of every round from the csv, with Table S1's definitions."""
    r = r.copy()
    r["timeout"] = r["choice.class"] == "Timeout"
    x = r["Risky.Bet.Amount"].astype(float)
    p = (10 - r["Risky.bet.shown.number"]) / 10.0
    win = r["Risky.bet.hidden.number"] > r["Risky.bet.shown.number"]
    gam = (r["choice.class"] == "Gamble").astype(float)
    reward = np.where(gam == 1, np.where(win, x, 0.0), 10.0)
    cv = np.where(gam == 1, p * x, 10.0)
    r["winprob"], r["risk"], r["gamble_ind"], r["exputil"] = p, p * (1 - p), gam, cv
    r["win_ind"], r["loss_ind"] = (gam * win).astype(float), (gam * ~win).astype(float)
    r["rpe"] = reward - cv
    r["regret"] = reward - np.where(win, np.maximum(x, 10.0), 10.0)
    r["gamble_won"] = win
    r["rt"] = r["buttonpress.time"] - r["choice.time"]
    r["left"] = (r["choice.location"] == "Left").astype(float)
    r.loc[r.timeout, ["gamble_ind", "exputil", "win_ind", "loss_ind", "rpe", "regret", "left"]] = np.nan
    return r


def align_trials(rounds: pd.DataFrame, glob: pd.DataFrame) -> np.ndarray:
    """Round index (0-based) of each HFA trial, by greedy matching on regressor values."""
    keys = ["winprob", "gamble_ind", "win_ind", "regret", "prev_winprob"]
    cand = np.where(~rounds.timeout.values)[0]
    rk = np.c_[rounds[keys[:4]].values, np.r_[-1.0, rounds["winprob"].values[:-1]]]
    gk = np.c_[glob[keys[:4]].values, np.nan_to_num(glob["previous_winprob"].values, nan=-1.0)]
    idx, j = [], 0
    for t in range(len(gk)):
        while j < len(cand) and not np.allclose(rk[cand[j]], gk[t]):
            j += 1
        if j == len(cand):
            raise ValueError("trial not matched")
        idx.append(cand[j])
        j += 1
    return np.array(idx)


def past_regressors(rounds: pd.DataFrame, idx: np.ndarray, lag: int) -> pd.DataFrame:
    """Each current regressor of the round `lag` rounds before each HFA trial's round.

    A timeout round k back gives its win probability and risk (defined by the shown number)
    and 0 for the choice and outcome regressors; rounds before the first give NaN. This is the
    convention of the t-1 values in sXX_behav_globals.mat, checked in the notebook.
    """
    src = idx - lag
    out = {}
    for k in CURRENT:
        v = np.nan_to_num(rounds[k].values.astype(float), nan=0.0)
        out[k] = np.where(src >= 0, v[np.clip(src, 0, None)], np.nan)
    return pd.DataFrame(out)


def load_hfa(subject: str, rt_ms: np.ndarray | None = None, n_offset_trials: int = 10) -> dict:
    """Window-averaged HFA of both epochs (trials x 57 x electrodes, float32), with checks.

    The 1-kHz arrays are read for checks only: the maximum difference, per electrode, between
    the window arrays and the mean of samples 50k to 50k+200; electrode pairs whose 1-kHz traces
    or window arrays are identical; the grand mean trace. With rt_ms (the csv's button press
    minus game presentation, per trial), the offset between the two epochs is found for the
    first n_offset_trials trials as the shift that best superimposes the overlapping 1-kHz
    samples of the first electrode (the smallest SD of their difference).
    """
    z = _zip("data.zip")
    d = sio.loadmat(z.open(f"data/data_ephys/{subject}_ofc_hg_events.mat"))
    out = {e: d[f"{e}_window_events_hg"] for e in EPOCHS}
    ne = out["game"].shape[2]
    for e in EPOCHS:
        raw = d[f"{e}_events_hg"]
        win = np.stack([raw[:, 50 * k: 50 * k + 201, :].mean(1) for k in range(N_WIN)], 1)
        out[f"{e}_maxdiff"] = np.abs(win - out[e]).max((0, 1))
        out[f"{e}_mean_trace"] = raw.astype(float).mean((0, 2))
        out[f"{e}_raw_range"] = (float(raw.min()), float(raw.max()))
        out[f"{e}_nan"] = int(np.isnan(raw).sum())
        out[f"{e}_raw_identical"] = [(i, j) for i in range(ne) for j in range(i + 1, ne)
                                     if np.array_equal(raw[:, :, i], raw[:, :, j])]
        out[f"{e}_win_identical"] = [(i, j) for i in range(ne) for j in range(i + 1, ne)
                                     if np.array_equal(out[e][:, :, i], out[e][:, :, j])]
        flat = out[e].reshape(-1, ne).astype(float)
        c = np.corrcoef(flat.T) if ne > 1 else np.zeros((1, 1))
        np.fill_diagonal(c, 0)
        out[f"{e}_high_corr"] = [(i, j, round(float(c[i, j]), 4)) for i in range(ne)
                                 for j in range(i + 1, ne) if c[i, j] > 0.95]
    if rt_ms is not None:
        g, p = d["game_events_hg"][:, :, 0].astype(float), d["buttonpress_events_hg"][:, :, 0].astype(float)
        offs = []
        for t in range(min(n_offset_trials, len(rt_ms))):
            best = (None, np.inf)
            for s in range(0, 2700):
                j = np.arange(0, 3001 - s)
                if len(j) < 300:
                    break
                v = np.std(g[t, j + s] - p[t, j])
                if v < best[1]:
                    best = (s, v)
            offs.append({"trial": t, "rt_ms": int(rt_ms[t]), "offset_ms": best[0],
                         "offset_minus_rt": best[0] - int(rt_ms[t]), "sd_diff": round(best[1], 3)})
        out["offsets"] = pd.DataFrame(offs)
    del d
    return out


def r_critical(n: int, alpha: float = ALPHA) -> float:
    """|r| above which a simple regression on n points has two-sided p < alpha."""
    t = stats.t.ppf(1 - alpha / 2, n - 2)
    return float(t / np.sqrt(n - 2 + t * t))


def _zscore(a, axis=0):
    a = a - a.mean(axis, keepdims=True)
    s = np.sqrt((a * a).sum(axis, keepdims=True))
    s[s == 0] = np.inf
    return a / s


def correlations(y: np.ndarray, x: np.ndarray, n_perm: int, rng: np.random.Generator) -> np.ndarray:
    """Pearson r of regressor x with every column of y, for the data and n_perm label shuffles.

    y: trials x columns (NaN-free), x: trials. Returns (n_perm + 1) x columns, row 0 the data.
    """
    ys = _zscore(y.astype(np.float64))
    xs = np.empty((n_perm + 1, len(x)))
    xs[0] = x
    for i in range(n_perm):
        xs[i + 1] = x[rng.permutation(len(x))]
    xs = _zscore(xs, axis=1)
    return (xs @ ys).astype(np.float32)


def longest_run(sig: np.ndarray) -> np.ndarray:
    """Longest run of True along the last axis."""
    best = np.zeros(sig.shape[:-1], dtype=np.int16)
    cur = np.zeros_like(best)
    for k in range(sig.shape[-1]):
        cur = np.where(sig[..., k], cur + 1, 0)
        best = np.maximum(best, cur)
    return best


def run_bounds(sig: np.ndarray) -> tuple[int, int]:
    """(start, length) of the first longest run of True in a 1-D array."""
    best, start, cur = 0, -1, 0
    for k, v in enumerate(sig):
        cur = cur + 1 if v else 0
        if cur > best:
            best, start = cur, k - cur + 1
    return start, best


def encoding_scan(hfa: dict, x: np.ndarray, n_perm: int, rng: np.random.Generator) -> dict:
    """Per electrode, the regression of window HFA on one regressor, in both epochs.

    Trials where x is NaN are dropped. Returns r and r2 (data, epochs x 57 x electrodes), sig
    (p < 0.05), run (longest significant run per epoch, data), encoding (run >= 5 in either
    epoch), and for the shuffles (the same shuffle of trials for both epochs) perm_encoding
    (n_perm x electrodes), perm_sig_count and perm_r2_enc (see below).
    """
    ok = ~np.isnan(x)
    n = int(ok.sum())
    ne = hfa["game"].shape[2]
    y = np.concatenate([hfa[e][ok].reshape(n, -1) for e in EPOCHS], axis=1)
    r = correlations(y, x[ok], n_perm, rng).reshape(n_perm + 1, 2, N_WIN, ne)
    rc = r_critical(n)
    sig = np.abs(r) > rc
    runs = longest_run(np.moveaxis(sig, 2, -1))          # (P+1) x 2 x electrodes
    enc = (runs >= MIN_RUN).any(1)
    r2 = r * r
    # for the shuffles: per window, the number of electrodes with p < 0.05, and the summed r2
    # profile of the electrodes classified as encoding
    perm_sig_count = sig[1:].sum(3)                        # P x 2 x 57
    perm_r2_enc = np.einsum("pewk,pk->pew", r2[1:], enc[1:].astype(np.float32))
    # per electrode, the 95th percentile of the longest run (either epoch) under its own shuffles
    run95 = np.percentile(runs[1:].max(1), 95, axis=0) if n_perm else np.full(ne, np.nan)
    return {"n": n, "r": r[0], "r2": r2[0], "sig": sig[0], "run": runs[0], "encoding": enc[0],
            "perm_encoding": enc[1:], "perm_sig_count": perm_sig_count, "perm_r2_enc": perm_r2_enc,
            "run95": run95}


def fstat_from_r(r, n):
    r2 = np.minimum(r * r, 0.999999)
    return r2 / (1 - r2) * (n - 2)


def stepwise_sumF(hfa: dict, x: np.ndarray, n_perm: int, rng: np.random.Generator,
                  chunk: int = 1000) -> tuple[np.ndarray, np.ndarray]:
    """Sum of F over the longest significant stretch, per electrode; data and permutation p.

    The stretch is found in each epoch and the larger sum of the two epochs is taken
    (assumption). Permutation p = share of shuffles with a sum at least the data's, (k+1)/(P+1).
    """
    ok = ~np.isnan(x)
    n = int(ok.sum())
    ne = hfa["game"].shape[2]
    y = np.concatenate([hfa[e][ok].reshape(n, -1) for e in EPOCHS], axis=1)
    ys = _zscore(y.astype(np.float64)).astype(np.float32)
    rc = r_critical(n)
    xv = x[ok]

    def sums(rows):
        r = (_zscore(rows, axis=1).astype(np.float32) @ ys).reshape(len(rows), 2, N_WIN, ne)
        f = fstat_from_r(r, n)
        sig = np.abs(r) > rc
        best = np.zeros((len(rows), 2, ne), np.float32)
        bestlen = np.zeros((len(rows), 2, ne), np.int16)
        cur = np.zeros_like(best)
        curlen = np.zeros_like(bestlen)
        for k in range(N_WIN):
            s = sig[:, :, k, :]
            cur = np.where(s, cur + f[:, :, k, :], 0)
            curlen = np.where(s, curlen + 1, 0)
            better = curlen > bestlen
            best = np.where(better, cur, best)
            bestlen = np.where(better, curlen, bestlen)
        return best.max(1)

    data = sums(xv[None, :].astype(np.float64))[0]
    exceed = np.zeros(ne)
    done = 0
    while done < n_perm:
        m = min(chunk, n_perm - done)
        rows = np.stack([xv[rng.permutation(n)] for _ in range(m)]).astype(np.float64)
        exceed += (sums(rows) >= data[None, :]).sum(0)
        done += m
    return data, (exceed + 1) / (n_perm + 1)


def ols_rss(y, X):
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    res = y - X @ beta
    return float(res @ res)


def forward_select(y: np.ndarray, X: pd.DataFrame, order_first: str, alpha: float = ALPHA) -> list:
    """Forward selection by nested-model F test (ANOVA), starting from `order_first`.

    At each step the candidate that most lowers the residual sum of squares is added when the
    F test of the larger model against the smaller has p < alpha.
    """
    n = len(y)
    chosen = [order_first]
    rest = [c for c in X.columns if c != order_first]
    ones = np.ones((n, 1))
    while rest:
        base = np.hstack([ones, X[chosen].values])
        rss0 = ols_rss(y, base)
        trials = [(ols_rss(y, np.hstack([base, X[[c]].values])), c) for c in rest]
        rss1, c = min(trials)
        df2 = n - base.shape[1] - 1
        F = (rss0 - rss1) / (rss1 / df2) if rss1 > 0 else np.inf
        if stats.f.sf(F, 1, df2) < alpha:
            chosen.append(c)
            rest.remove(c)
        else:
            break
    return chosen


# --- random-effects logistic regression by maximum likelihood (Gauss-Hermite quadrature) ---

def glmm_logit(y, X, groups, random_slope_col=None, n_points=20):
    """Logistic regression with a random intercept (and optionally a random slope) per group.

    Fitted by maximum likelihood with Gauss-Hermite quadrature over the random effects
    (independent intercept and slope). X includes the intercept column. Returns a DataFrame of
    estimates, Wald standard errors (numerical Hessian) and two-sided p-values for the fixed
    effects, and the random-effect standard deviations.
    """
    y = np.asarray(y, float)
    X = np.asarray(X, float)
    g = pd.factorize(np.asarray(groups))[0]
    G = g.max() + 1
    k = X.shape[1]
    nodes, weights = np.polynomial.hermite.hermgauss(n_points if random_slope_col is None else 12)
    z = nodes * np.sqrt(2)
    w = weights / np.sqrt(np.pi)
    if random_slope_col is None:
        Z = z[:, None]
        W = w
    else:
        za, zb = np.meshgrid(z, z, indexing="ij")
        Z = np.c_[za.ravel(), zb.ravel()]
        W = np.outer(w, w).ravel()
    nre = Z.shape[1]

    def negll(theta):
        beta = theta[:k]
        sd = np.exp(theta[k:k + nre])
        eta0 = X @ beta
        ll = 0.0
        for j in range(G):
            m = g == j
            e = eta0[m][:, None] + sd[0] * Z[:, 0][None, :]
            if nre == 2:
                e = e + sd[1] * Z[:, 1][None, :] * X[m, random_slope_col][:, None]
            lp = np.where(y[m][:, None] == 1, -np.logaddexp(0, -e), -np.logaddexp(0, e)).sum(0)
            mx = lp.max()
            ll += mx + np.log(np.sum(W * np.exp(lp - mx)))
        return -ll

    beta0 = np.linalg.lstsq(X, (y - 0.5) * 4, rcond=None)[0]
    theta0 = np.r_[beta0, np.full(nre, np.log(0.5))]
    res = optimize.minimize(negll, theta0, method="BFGS")
    res = optimize.minimize(negll, res.x, method="Nelder-Mead",
                            options={"maxiter": 4000, "xatol": 1e-6, "fatol": 1e-8}) if not res.success else res
    th = res.x
    h = 1e-4
    npar = len(th)
    H = np.zeros((npar, npar))
    for a in range(npar):
        for b in range(a, npar):
            ea = np.zeros(npar); eb = np.zeros(npar)
            ea[a] = h; eb[b] = h
            H[a, b] = H[b, a] = (negll(th + ea + eb) - negll(th + ea - eb) - negll(th - ea + eb)
                                 + negll(th - ea - eb)) / (4 * h * h)
    cov = np.linalg.pinv(H)
    se = np.sqrt(np.clip(np.diag(cov)[:k], 0, None))
    zval = th[:k] / se
    out = pd.DataFrame({"estimate": th[:k], "se": se, "z": zval,
                        "p": 2 * stats.norm.sf(np.abs(zval))})
    out.attrs["re_sd"] = np.exp(th[k:]).tolist()
    out.attrs["converged"] = bool(res.success)
    out.attrs["loglik"] = -res.fun
    return out


def scan_all(hfa: dict, regressor: dict, n_perm: int, rng: np.random.Generator) -> dict:
    """encoding_scan over all subjects for one regressor, pooled over electrodes.

    hfa: subject -> {epoch: trials x 57 x electrodes}; regressor: subject -> values per trial.
    Shuffle i of every subject is pooled into shuffle i of the whole set.
    """
    parts = [encoding_scan(hfa[s], np.asarray(regressor[s], float), n_perm, rng) for s in hfa]
    cat = lambda k, ax: np.concatenate([p[k] for p in parts], axis=ax)
    out = {"subject": np.concatenate([[s] * hfa[s]["game"].shape[2] for s in hfa]),
           "n": {s: p["n"] for s, p in zip(hfa, parts)},
           "r": cat("r", 2), "r2": cat("r2", 2), "sig": cat("sig", 2), "run": cat("run", 1),
           "encoding": cat("encoding", 0), "run95": cat("run95", 0)}
    if n_perm:
        out["perm_count"] = sum(p["perm_encoding"].sum(1) for p in parts)
        out["perm_sig_count"] = sum(p["perm_sig_count"] for p in parts)
        out["perm_r2_enc"] = sum(p["perm_r2_enc"] for p in parts)
        out["perm_count_by_subject"] = {s: p["perm_encoding"].sum(1) for s, p in zip(hfa, parts)}
    return out
