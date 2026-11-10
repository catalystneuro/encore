"""Statistics for the reproduction of Jones et al. 2019 (Cell Reports 29, 2123-2133).

"Early hippocampal sharp-wave ripple deficits predict later learning and memory
impairments in an Alzheimer's disease mouse model", doi:10.1016/j.celrep.2019.10.056.

Sources of the methods
----------------------
* Paper, STAR Methods "Quantification and Statistical Analysis": Prism; two-tailed
  paired and unpaired t tests, two-way ANOVA, two-way mixed-effects analysis (for
  data sets with missing values), Pearson correlations reported as F tests; when
  assumptions were violated, two-tailed Mann-Whitney U tests, two-way ANOVA or
  mixed-effects analysis on aligned rank transformed data (Wobbrock et al. 2011;
  ARTool) and Spearman correlations; Sidak post hoc; Holm-Sidak in the replication
  cohort; performance scores built from metrics "Z scored across the population".
* Claims file ``claims/jones-2019.yaml``, header methods E (scores), F (tests,
  Holm-Sidak as Prism prints it) and G (predicted scores).
* Paper code (https://github.com/emilyasterjones/Jones_2019, commit ca056a8):
  ``fit_train_to_test.m`` (ported in :func:`predict_scores`) and ``loocv.m``
  (ported in :func:`loo_pearson`).

Only numpy, scipy, pandas and statsmodels are used.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats as _st


# ----------------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------------
def _pairs(x, y):
    x = np.asarray(x, dtype=float).ravel()
    y = np.asarray(y, dtype=float).ravel()
    if x.shape != y.shape:
        raise ValueError("x and y differ in length")
    ok = np.isfinite(x) & np.isfinite(y)
    return x[ok], y[ok]


def _clean(a):
    a = np.asarray(a, dtype=float).ravel()
    return a[np.isfinite(a)]


# ----------------------------------------------------------------------------
# correlations
# ----------------------------------------------------------------------------
def pearson(x, y):
    """Pearson correlation reported as the regression F test.

    Source: paper, Quantification and Statistical Analysis ("Pearson correlations",
    goodness of fit "shown by F test"); claims method F: F(1, n-2), two-sided.
    F = r^2 (n-2) / (1-r^2) with df (1, n-2); its p equals the two-sided p of r.
    Pairs with a NaN in either value are dropped (as Prism and MATLAB
    ``corr(...,'rows','complete')`` do).

    Returns dict(r, r2, F, df=(1, n-2), p, n).
    """
    x, y = _pairs(x, y)
    n = len(x)
    if n < 3 or np.std(x) == 0 or np.std(y) == 0:
        return dict(r=np.nan, r2=np.nan, F=np.nan, df=(1, n - 2), p=np.nan, n=n)
    r = float(np.corrcoef(x, y)[0, 1])
    r = max(-1.0, min(1.0, r))
    r2 = r * r
    dfd = n - 2
    F = np.inf if r2 == 1 else r2 * dfd / (1 - r2)
    p = float(_st.f.sf(F, 1, dfd)) if np.isfinite(F) else 0.0
    return dict(r=r, r2=r2, F=float(F), df=(1, dfd), p=p, n=n)


def spearman(x, y):
    """Spearman rank correlation, two-sided (scipy.stats.spearmanr, t approximation).

    Source: paper, Quantification and Statistical Analysis ("Spearman correlations"
    when assumptions were violated). Pairs with NaN are dropped.
    Returns dict(rho, p, n).
    """
    x, y = _pairs(x, y)
    n = len(x)
    if n < 3:
        return dict(rho=np.nan, p=np.nan, n=n)
    res = _st.spearmanr(x, y)
    return dict(rho=float(res.statistic), p=float(res.pvalue), n=n)


# ----------------------------------------------------------------------------
# multiplicity
# ----------------------------------------------------------------------------
def holm_sidak(p, monotone=False):
    """Holm-Sidak (step-down Sidak) adjusted p values, in the input order.

    Source: paper ("p values were adjusted using Holm-Sidak correction"); claims
    method F: the printed adjusted p are reproduced by step-down Sidak *without*
    enforced monotonicity, as Prism prints it. Sort ascending; the i-th smallest
    (i = 1..m) gets 1 - (1 - p_(i))^(m - i + 1). ``monotone=True`` adds the running
    maximum of the standard Holm procedure (statsmodels 'holm-sidak'). NaN entries
    are ignored (not counted in m) and returned as NaN.
    """
    p = np.asarray(p, dtype=float).ravel()
    out = np.full(p.shape, np.nan)
    idx = np.where(np.isfinite(p))[0]
    m = len(idx)
    if m == 0:
        return out.tolist()
    order = idx[np.argsort(p[idx], kind="mergesort")]
    adj = np.empty(m)
    for i, k in enumerate(order):  # i = 0..m-1, exponent m - i
        adj[i] = 1.0 - (1.0 - p[k]) ** (m - i)
    if monotone:
        adj = np.maximum.accumulate(adj)
    out[order] = np.clip(adj, 0.0, 1.0)
    return out.tolist()


def sidak(p, m):
    """Sidak adjustment 1 - (1-p)^m, clipped to [0, 1] (standard; paper: post hoc
    "Sidak correction for multiple comparisons"). Works on scalars or arrays."""
    p = np.asarray(p, dtype=float)
    out = np.clip(1.0 - (1.0 - p) ** m, 0.0, 1.0)
    return float(out) if out.ndim == 0 else out.tolist()


# ----------------------------------------------------------------------------
# two-sample tests
# ----------------------------------------------------------------------------
def ttest(a, b):
    """Unpaired two-tailed Student t test with pooled (equal) variance.

    Source: paper ("two-tailed ... unpaired t tests", Prism's default unpaired test
    assumes equal SD). t > 0 when mean(a) > mean(b). NaN dropped.
    Returns dict(t, df, p, mean_a, mean_b, n_a, n_b).
    """
    a, b = _clean(a), _clean(b)
    res = _st.ttest_ind(a, b, equal_var=True)
    return dict(t=float(res.statistic), df=len(a) + len(b) - 2, p=float(res.pvalue),
                mean_a=float(a.mean()), mean_b=float(b.mean()), n_a=len(a), n_b=len(b))


def paired_t(a, b):
    """Paired two-tailed t test on a - b (paper: "two-tailed paired ... t tests").
    Pairs with a NaN are dropped. Returns dict(t, df, p, mean_diff, n)."""
    a, b = _pairs(a, b)
    res = _st.ttest_rel(a, b)
    return dict(t=float(res.statistic), df=len(a) - 1, p=float(res.pvalue),
                mean_diff=float(np.mean(a - b)), n=len(a))


def mannwhitney(a, b, method="auto"):
    """Two-tailed Mann-Whitney U test (paper: "two-tailed Mann-Whitney U tests").

    U is reported as min(U1, U2), as Prism prints it; U1 is scipy's statistic for
    sample a (number of pairs with a > b, ties counted 1/2). p from
    scipy.stats.mannwhitneyu with method 'auto' by default (scipy 1.18: 'exact' when
    either sample has <= 8 values and there are no ties, otherwise 'asymptotic' with
    tie and continuity correction). Prism computes exact p for small samples
    (it documents exact p when total n is small, approximate otherwise), so for
    samples of 9-50 mice without ties pass method='exact' to match it more closely.
    The method actually used is returned. NaN dropped.
    """
    a, b = _clean(a), _clean(b)
    n1, n2 = len(a), len(b)
    allv = np.concatenate([a, b])
    ties = len(np.unique(allv)) < len(allv)
    if method == "auto":
        used = "asymptotic" if (n1 > 8 and n2 > 8) or ties else "exact"
    else:
        used = method
    res = _st.mannwhitneyu(a, b, alternative="two-sided", method=method)
    u1 = float(res.statistic)
    return dict(U=min(u1, n1 * n2 - u1), U1=u1, p=float(res.pvalue), n_a=n1, n_b=n2,
                method=used, ties=bool(ties))


def binom_greater(k, n, p0=0.05):
    """One-sided binomial test P(X >= k), X ~ Binomial(n, p0).

    Source: paper ("more than expected by chance (p < 0.016, binomial test; see
    Table S4)"); one-sided greater, chance rate alpha = 0.05 (standard choice)."""
    return float(_st.binom.sf(k - 1, n, p0))


# ----------------------------------------------------------------------------
# aligned rank transform, two-way split-plot design
# ----------------------------------------------------------------------------
def _sum_code(levels, values):
    """Sum-to-zero (deviation) coding: len(levels)-1 columns."""
    levels = list(levels)
    X = np.zeros((len(values), len(levels) - 1))
    for j, lv in enumerate(levels[:-1]):
        X[:, j] = (values == lv).astype(float)
    X[values == levels[-1], :] = -1.0
    return X


def _rss(X, y):
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    r = y - X @ beta
    return float(r @ r), int(np.linalg.matrix_rank(X))


def _splitplot_F(d, subject, between, within, dv, effect):
    """Classic split-plot ANOVA on complete data; returns (F, df1, df2) of one effect.

    Between effect: one-way ANOVA of subject means across groups (equivalent to
    MS_A / MS_S(A) when every subject has every within level). Within and
    interaction: type III (sum-coded) model comparison in OLS with subject dummies;
    error = subject x within residual, df (N - a)(b - 1).
    """
    y = d[dv].to_numpy(float)
    A = d[between].to_numpy()
    B = d[within].to_numpy()
    S = d[subject].to_numpy()
    la, lb, ls = sorted(pd.unique(A)), sorted(pd.unique(B)), list(pd.unique(S))
    a, b, N = len(la), len(lb), len(ls)
    if effect == "between":
        sm = d.groupby(subject).agg(m=(dv, "mean"), g=(between, "first"))
        groups = [g["m"].to_numpy(float) for _, g in sm.groupby("g")]
        res = _st.f_oneway(*groups)
        return float(res.statistic), a - 1, N - a
    XS = np.zeros((len(y), N))
    for j, s in enumerate(ls):
        XS[S == s, j] = 1.0
    XB = _sum_code(lb, B)
    XA = _sum_code(la, A)
    XAB = np.column_stack([XA[:, i] * XB[:, j] for i in range(XA.shape[1])
                           for j in range(XB.shape[1])])
    full = np.column_stack([XS, XB, XAB])
    rss_f, rk_f = _rss(full, y)
    dfe = len(y) - rk_f
    red = np.column_stack([XS, XAB]) if effect == "within" else np.column_stack([XS, XB])
    rss_r, rk_r = _rss(red, y)
    df1 = rk_f - rk_r
    F = ((rss_r - rss_f) / df1) / (rss_f / dfe)
    return float(F), df1, dfe


def _mixedlm_F(d, subject, between, within, dv, effect):
    """Random-intercept LMM (REML) on the aligned ranks; Wald test of one effect.

    Returns dict with chi2 (Wald), q (numerator df), F = chi2 / q, p_chi2, and
    p_F using a containment-style denominator df: N_subjects - a for the between
    effect, n_obs - N_subjects - (b - 1) - (a - 1)(b - 1) for within/interaction
    (an approximation; Prism's mixed-effects analysis uses its own df, which we do
    not know exactly).
    """
    import statsmodels.formula.api as smf

    dd = d.rename(columns={dv: "y_", between: "A_", within: "B_", subject: "S_"})
    dd = dd[["y_", "A_", "B_", "S_"]].copy()
    dd["A_"] = dd["A_"].astype(str)
    dd["B_"] = dd["B_"].astype(str)
    model = smf.mixedlm("y_ ~ C(A_, Sum) * C(B_, Sum)", dd, groups=dd["S_"])
    res = model.fit(reml=True)
    names = list(res.fe_params.index)
    if effect == "between":
        sel = [i for i, n in enumerate(names) if n.startswith("C(A_") and ":" not in n]
    elif effect == "within":
        sel = [i for i, n in enumerate(names) if n.startswith("C(B_") and ":" not in n]
    else:
        sel = [i for i, n in enumerate(names) if ":" in n]
    k = len(names)
    beta = res.fe_params.to_numpy()[sel]
    cov = np.asarray(res.cov_params())[:k, :k][np.ix_(sel, sel)]
    chi2 = float(beta @ np.linalg.solve(cov, beta))
    q = len(sel)
    a = dd["A_"].nunique()
    b = dd["B_"].nunique()
    N = dd["S_"].nunique()
    if effect == "between":
        dfd = N - a
    else:
        dfd = len(dd) - N - (b - 1) - (a - 1) * (b - 1)
    F = chi2 / q
    return dict(F=F, df=(q, dfd), p=float(_st.f.sf(F, q, dfd)), chi2=chi2,
                p_chi2=float(_st.chi2.sf(chi2, q)), converged=bool(res.converged))


def art_align(df, subject, between, within, dv, effect):
    """Aligned response for one effect (Wobbrock et al. 2011, steps 1-3).

    residual = Y - cell mean (A_i, B_j); add the effect's estimate from observed
    marginal means: A: mean_i. - grand; B: mean_.j - grand;
    AB: cell_ij - mean_i. - mean_.j + grand. (ARTool also uses observed means.)
    Returns a numpy array aligned to the rows of ``df``.
    """
    y = df[dv].astype(float)
    grand = y.mean()
    cell = df.groupby([between, within])[dv].transform("mean")
    ma = df.groupby(between)[dv].transform("mean")
    mb = df.groupby(within)[dv].transform("mean")
    resid = y - cell
    if effect == "between":
        est = ma - grand
    elif effect == "within":
        est = mb - grand
    elif effect == "interaction":
        est = cell - ma - mb + grand
    else:
        raise ValueError(effect)
    return (resid + est).to_numpy(float)


def art_anova_rm(df, subject, between, within, dv, force=None):
    """Two-way ANOVA (or mixed-effects analysis) on aligned rank transformed data.

    Source: paper, Quantification and Statistical Analysis ("two-way ANOVA or
    mixed-effects analysis on aligned rank transformed data (Wobbrock et al.,
    2011)"; "two-way mixed-effects analysis (for datasets with missing values)");
    Methods: data "aligned rank transformed using ARTool". Figure legends: e.g.
    Figure 1G "Two-way repeated-measures ANOVA of aligned rank transformed data"
    (genotype x day), Figure S4A "Two-way mixed-effects analysis of aligned rank
    transformed data" (genotype x age).

    For each effect (between main, within main, interaction): align (see
    :func:`art_align`), rank with average ties over all observations, fit the
    model on the ranks and keep only that effect's F.
    * complete data (every subject has every within level, one observation per
      cell): classic split-plot ANOVA (see :func:`_splitplot_F`);
    * otherwise: statsmodels MixedLM with a random intercept per subject (REML),
      Wald test of the effect (see :func:`_mixedlm_F`).
    ``force`` = 'anova' or 'mixed' overrides the choice (ANOVA needs complete data).

    Returns dict effect -> dict(path, n_subjects, n_obs, F, df, p, ...).
    """
    d = df[[subject, between, within, dv]].dropna().reset_index(drop=True)
    counts = d.groupby([subject, within]).size()
    nb = d[within].nunique()
    per_subj = d.groupby(subject)[within].nunique()
    complete = bool((counts == 1).all() and (per_subj == nb).all())
    path = force or ("anova" if complete else "mixed")
    if path == "anova" and not complete:
        raise ValueError("split-plot ANOVA needs complete data")
    out = {}
    for eff in ("between", "within", "interaction"):
        dd = d.copy()
        dd["_rank"] = _st.rankdata(art_align(d, subject, between, within, dv, eff))
        if path == "anova":
            F, df1, df2 = _splitplot_F(dd, subject, between, within, "_rank", eff)
            r = dict(F=F, df=(df1, df2), p=float(_st.f.sf(F, df1, df2)))
        else:
            r = _mixedlm_F(dd, subject, between, within, "_rank", eff)
        r.update(path=path, n_subjects=int(d[subject].nunique()), n_obs=len(d),
                 effect_name={"between": between, "within": within,
                              "interaction": f"{between} x {within}"}[eff])
        out[eff] = r
    return out


# ----------------------------------------------------------------------------
# scores
# ----------------------------------------------------------------------------
def zscore(v, population_index=None):
    """z = (v - mean) / SD with the sample SD (ddof=1); a standard choice (the paper
    says only "Z scored"). NaN ignored in mean/SD. If ``population_index`` (boolean
    mask or positions) is given, mean and SD come from that subset and are applied
    to all values."""
    v = np.asarray(v, dtype=float)
    ref = v if population_index is None else v[population_index]
    ref = ref[np.isfinite(ref)]
    return (v - ref.mean()) / ref.std(ddof=1)


def performance_score(table, metrics, invert=(), population_index=None):
    """Performance score: mean over metrics of per-metric z scores (sign flipped
    for metrics where higher is worse).

    Source: paper, Quantification and Statistical Analysis (a Z score for each mouse
    and metric, "reversing the sign of any metric" where a higher value means worse
    performance, then "averaging all Z scores for each mouse"; "Z scored across the
    population"); claims method E (the population is open: E4 mice of the
    correlation, or all mice of the cohort - choose with ``population_index``, a
    boolean mask / index labels of ``table`` rows; default all rows).

    Returns (scores: pd.Series indexed like table, info dict with n_missing - rows
    with any missing metric, which get NaN - and the per-metric mean/SD used).
    """
    t = table[list(metrics)].astype(float)
    if population_index is None:
        pop = t
    else:
        pop = t.loc[population_index] if not (
            isinstance(population_index, (np.ndarray, pd.Series, list))
            and np.asarray(population_index).dtype == bool) else t[np.asarray(population_index)]
    z = pd.DataFrame(index=t.index)
    used = {}
    for m in metrics:
        ref = pop[m].dropna()
        mu, sd = ref.mean(), ref.std(ddof=1)
        z[m] = (t[m] - mu) / sd * (-1.0 if m in set(invert) else 1.0)
        used[m] = (float(mu), float(sd), int(len(ref)))
    missing = z.isna().any(axis=1)
    score = z.mean(axis=1)
    score[missing] = np.nan
    return score, dict(n_missing=int(missing.sum()), missing_rows=list(t.index[missing]),
                       mean_sd_n=used, z=z)


# ----------------------------------------------------------------------------
# method G and leave-one-out
# ----------------------------------------------------------------------------
def predict_scores(x_train, y_train, x_test, y_test):
    """Predicted scores (claims method G; Figures 2N, 2R, 3F, 3I, 4I, 4L).

    x (the SWR property) is z-scored within each cohort (train over train, test over
    test; ddof=1, :func:`zscore`; fit_train_to_test.m takes the feature as given, the
    z-scoring is from the paper's "Z scored" text and claims method G). OLS
    y_train = b0 + b1 z(x_train) (the .m file: ``[ones x] \\ y``); prediction
    yfit = b0 + b1 z(x_test). Pairs with NaN are dropped within each cohort (before
    z-scoring).

    Main result: pearson(yfit, y_test) (the .m file's ``fitlm(yfit, test(:,i))``,
    which is what the figures print). Variant, the .m file's out-of-sample F, ported
    exactly:
        SSE_F = sum((y_test - yfit)^2);  SSE_R = sum((y_test - mean(y_test))^2)
        DR = n - 1;  DFn = n - 2;  MSR = (SSE_R - SSE_F)/(DR - DFn)  (= SSE_R - SSE_F)
        MSE = SSE_F / DFn;  F = MSR / MSE;  p = 1 - fcdf(F, 1, DFn)
    F is negative (p = 1) when the predictions fit worse than the test mean.
    """
    xtr, ytr = _pairs(x_train, y_train)
    xte, yte = _pairs(x_test, y_test)
    ztr, zte = zscore(xtr), zscore(xte)
    b1, b0 = np.polyfit(ztr, ytr, 1)
    yfit = b0 + b1 * zte
    out = pearson(yfit, yte)
    n = len(yte)
    sse_f = float(np.sum((yte - yfit) ** 2))
    sse_r = float(np.sum((yte - yte.mean()) ** 2))
    DR, DFn = n - 1, n - 2
    MSR = (sse_r - sse_f) / (DR - DFn)
    MSE = sse_f / DFn
    F_oos = MSR / MSE
    p_oos = float(1.0 - _st.f.cdf(F_oos, 1, DFn)) if F_oos > 0 else 1.0
    out.update(slope=float(b1), intercept=float(b0), predicted=yfit,
               F_oos=float(F_oos), df_oos=(1, DFn), p_oos=p_oos,
               n_train=len(ytr), n_test=n)
    return out


def loo_pearson(x, y, alpha=0.05):
    """Leave-one-out check of a Pearson correlation (port of loocv.m).

    loocv.m deletes each row a in turn (x and y), computes
    ``corr(x_sub, y_sub, 'rows', 'complete')`` (Pearson, two-sided, NaN pairs
    dropped), and reports mean and SD (nanmean, nanstd: ddof=1) of R and p, and
    ``sum(p > 0.05)``: the number of deletions after which the correlation is NOT
    significant (the file's comment says "fell below significance"). Rows are
    deleted from the full vectors including rows with NaN, as in the .m file (a row
    with NaN gives the same R as the full data).

    Returns dict(r, p (lists), mean_r, sd_r, mean_p, sd_p, n_above_alpha).
    """
    x = np.asarray(x, dtype=float).ravel()
    y = np.asarray(y, dtype=float).ravel()
    rs, ps = [], []
    for a in range(len(y)):
        keep = np.arange(len(y)) != a
        res = pearson(x[keep], y[keep])
        rs.append(res["r"])
        ps.append(res["p"])
    rs_, ps_ = np.array(rs), np.array(ps)
    return dict(r=rs, p=ps, mean_r=float(np.nanmean(rs_)), sd_r=float(np.nanstd(rs_, ddof=1)),
                mean_p=float(np.nanmean(ps_)), sd_p=float(np.nanstd(ps_, ddof=1)),
                n_above_alpha=int(np.sum(ps_ > alpha)))


# ----------------------------------------------------------------------------
# self-test
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    rng = np.random.default_rng(1)

    # Holm-Sidak against hand computation and the Figure 4 / Table S4 family
    # (CA3 SG power at 5-8 months vs MWM learning at 14-18 months, F(1,9)).
    Fs = {"slope 1-2": 5.82, "slope 1-3": 10.89, "latency day 3": 11.08, "night 1": 2.30}
    ps = [float(_st.f.sf(F, 1, 9)) for F in Fs.values()]
    adj = holm_sidak(ps)
    srt = sorted(ps)
    hand = {srt[0]: 1 - (1 - srt[0]) ** 4, srt[1]: 1 - (1 - srt[1]) ** 3,
            srt[2]: 1 - (1 - srt[2]) ** 2, srt[3]: srt[3]}
    assert np.allclose(adj, [hand[p] for p in ps])
    print("Figure 4 family (printed adj p: slope 1-2 0.077, slope 1-3 0.027, day 3 0.035):")
    for (k, F), p, a, am in zip(Fs.items(), ps, adj, holm_sidak(ps, monotone=True)):
        print(f"  {k:14s} F={F:5.2f} p={p:.4f} adj={a:.3f} adj_monotone={am:.3f}")
    from statsmodels.stats.multitest import multipletests
    assert np.allclose(holm_sidak(ps, monotone=True),
                       multipletests(ps, method="holm-sidak")[1])

    # Pearson F identity
    x = rng.normal(size=11)
    y = x + rng.normal(size=11)
    r = pearson(x, y)
    assert abs(r["p"] - _st.pearsonr(x, y).pvalue) < 1e-10

    # ART: (1) on complete data the per-effect F equals a textbook split-plot
    # ANOVA (sums of squares) on the same aligned ranks (exact for every effect
    # with equal group sizes; with unequal sizes only for the between effect, since
    # the module uses type III / unweighted-means SS for within and interaction);
    # (2) on complete data the MixedLM path reproduces the ANOVA F.
    rows = []
    for g, n in (("E3", 6), ("E4", 7)):
        for s in range(n):
            u = rng.normal()
            for day in range(1, 5):
                rows.append((f"{g}{s}", g, day, u + (0.8 if g == "E4" else 0) * day / 4
                             + rng.normal()))
    d = pd.DataFrame(rows, columns=["mouse", "geno", "day", "lat"])
    art = art_anova_rm(d, "mouse", "geno", "day", "lat")

    def splitplot_textbook(dd, y):
        """Textbook SS formulas (valid with complete within and any n_i for A;
        for B and AB with equal n_i)."""
        g = dd.assign(y=y)
        gm = g.y.mean()
        b = g.day.nunique()
        N = g.mouse.nunique()
        a = g.geno.nunique()
        sm = g.groupby("mouse").agg(m=("y", "mean"), geno=("geno", "first"))
        gmean = g.groupby("geno").y.mean()
        ssA = b * sum(((sm.geno.map(gmean) - gm) ** 2))
        ssSA = b * sum((sm.m - sm.geno.map(gmean)) ** 2)
        ssB = N * sum((g.groupby("day").y.mean() - gm) ** 2)
        cell = g.groupby(["geno", "day"]).y.transform("mean")
        ma = g.groupby("geno").y.transform("mean")
        mb = g.groupby("day").y.transform("mean")
        ssAB = float(((cell - ma - mb + gm) ** 2).sum())
        sst = float(((g.y - gm) ** 2).sum())
        ssE = sst - ssA - ssSA - ssB - ssAB
        dfe = (N - a) * (b - 1)
        return dict(between=(ssA / (a - 1)) / (ssSA / (N - a)),
                    within=(ssB / (b - 1)) / (ssE / dfe),
                    interaction=(ssAB / ((a - 1) * (b - 1))) / (ssE / dfe))

    print("ART, complete design (13 mice x 4 days):")
    for eff in ("between", "within", "interaction"):
        rk = _st.rankdata(art_align(d, "mouse", "geno", "day", "lat", eff))
        Ft = splitplot_textbook(d, rk)[eff]
        print(f"  {eff:11s} F={art[eff]['F']:.4f} df={art[eff]['df']} p={art[eff]['p']:.4g}"
              f"  textbook F on aligned ranks={Ft:.4f}")
        if eff == "between":
            assert abs(Ft - art[eff]["F"]) < 1e-8
    # equal-n check for within / interaction (textbook formulas exact there)
    d2 = d[~d.mouse.isin(["E4" + "6"])]
    art2 = art_anova_rm(d2, "mouse", "geno", "day", "lat")
    for eff in ("between", "within", "interaction"):
        rk = _st.rankdata(art_align(d2, "mouse", "geno", "day", "lat", eff))
        assert abs(splitplot_textbook(d2, rk)[eff] - art2[eff]["F"]) < 1e-8
    mix = art_anova_rm(d2, "mouse", "geno", "day", "lat", force="mixed")
    for eff in ("between", "within", "interaction"):
        print(f"  equal n {eff:11s} ANOVA F={art2[eff]['F']:.3f}  MixedLM Wald F="
              f"{mix[eff]['F']:.3f} df={mix[eff]['df']}")
    # incomplete data -> mixed path
    d3 = d.drop(index=[0, 9, 30]).reset_index(drop=True)
    art3 = art_anova_rm(d3, "mouse", "geno", "day", "lat")
    assert art3["between"]["path"] == "mixed"
    print("  incomplete:", {k: (round(v["F"], 3), v["df"], round(v["p"], 4))
                            for k, v in art3.items()})

    # performance score
    tab = pd.DataFrame({"a": rng.normal(size=8), "b": rng.normal(size=8)})
    tab.loc[3, "b"] = np.nan
    sc, info = performance_score(tab, ["a", "b"], invert=["b"])
    assert info["n_missing"] == 1 and np.isnan(sc[3])
    za = zscore(tab["a"].to_numpy())
    assert abs(za.std(ddof=1) - 1) < 1e-12

    # predict_scores, loo, binomial, MWU
    xt, yt = rng.normal(size=16), rng.normal(size=16)
    yt = yt + xt
    xs, ys = rng.normal(size=11), rng.normal(size=11)
    ys = ys + xs
    pr = predict_scores(xt, yt, xs, ys)
    print(f"predict_scores: r={pr['r']:.3f} F={pr['F']:.2f} p={pr['p']:.4f} "
          f"F_oos={pr['F_oos']:.2f} p_oos={pr['p_oos']:.4f}")
    lo = loo_pearson(xs, ys)
    print("loo n p>0.05:", lo["n_above_alpha"])
    print("binom P(X>=3 | 18, 0.05) =", round(binom_greater(3, 18), 4))
    mw = mannwhitney([1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11])
    assert mw["U"] == 0 and mw["method"] == "exact"
    print("self-test passed")
