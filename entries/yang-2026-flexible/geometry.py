"""Phenotype spaces and the cell-level and type-level measures of Yang (2026), on IPFX features.

Where each parameter comes from (the claims file, claims/yang-2026-flexible.yaml, cites the paper
or its code, https://github.com/zy-neuro/protocol-response-geometry at commit 61a5a41, for each):

- Phenotype space (claim table1-phenotype-spaces): per regime, cells with extract_ok = 1 and at
  least one non-missing value among the regime's features (the code's fit_full_cell_pca, reading
  2a); features with at most 30% missing and nonzero variance; mean imputation; z-scores with the
  population SD; PCA by SVD; k80 the smallest number of components reaching 80% of the variance.
- Spearman correlation as the code computes it (np.argsort(np.argsort(x)) ordinal ranks, ties in
  the order the sort leaves them), with the tie-corrected (average-rank) Spearman as a variant
  where the claims file asks for it.
- Pairs of cells: 80,000 sampled pairs (Methods, "Cross-regime phenotypic organization"); unique
  pairs are the main reading, the code's draw of random i < j pairs, which may repeat, a variant.
- kNN: 15 neighbours, self excluded, Euclidean distance, ties as np.argpartition leaves them.
- Every random draw uses a generator the notebook makes from the claim's seed (protocol).
"""

from __future__ import annotations

from collections import Counter

import numpy as np
from scipy.stats import rankdata

PAIRS = [("long_pulse", "ramp"), ("long_pulse", "brief_pulse"), ("ramp", "brief_pulse")]
REGIMES = ["long_pulse", "ramp", "brief_pulse"]
PREFIX = {"long_pulse": "feat.long_squares.", "ramp": "feat.ramps.", "brief_pulse": "feat.short_squares."}


# --- phenotype spaces ---------------------------------------------------------------------------

def feature_matrix(recs, columns):
    """Cells x features, NaN where missing, for the extract_ok cells."""
    ok = [r for r in recs if r.get("extract_ok") == 1]
    x = np.full((len(ok), len(columns)), np.nan)
    pos = {c: j for j, c in enumerate(columns)}
    for i, r in enumerate(ok):
        for c, v in r["features"].items():
            j = pos.get(c)
            if j is not None and v is not None:
                x[i, j] = v
    return [r["file_stem"] for r in ok], x


def rule_features(recs, regime, max_missing=0.30, denominator="present"):
    """The paper's rule for retained features (Methods, "Protocol-resolved cellular phenotype"):
    numeric, at most 30% missing, nonzero variance; missingness among cells with any value of the
    regime ("present", reading 2a) or among all extract_ok cells ("all", reading 2b)."""
    cols = sorted({c for r in recs if r.get("extract_ok") == 1 for c in r["features"] if c.startswith(PREFIX[regime])})
    stems, x = feature_matrix(recs, cols)
    if denominator == "present":
        x = x[np.isfinite(x).any(axis=1)]
    miss = 1 - np.isfinite(x).mean(axis=0)
    with np.errstate(all="ignore"):
        var = np.nanvar(x, axis=0)
    keep = [c for c, m, v in zip(cols, miss, var) if m <= max_missing and np.isfinite(v) and v > 0]
    return keep, dict(zip(cols, miss))


def phenotype_space(recs, columns):
    """z-score + PCA of one regime (the code's fit_full_cell_pca)."""
    stems, x = feature_matrix(recs, columns)
    present = np.isfinite(x).any(axis=1)
    x = x[present]
    stems = [s for s, p in zip(stems, present) if p]
    mu = np.nanmean(x, axis=0)
    xf = np.where(np.isfinite(x), x, mu)
    xc = xf - xf.mean(axis=0, keepdims=True)
    sd = xc.std(axis=0, keepdims=True)
    sd[sd == 0] = 1.0
    z = xc / sd
    u, s, vt = np.linalg.svd(z, full_matrices=False)
    var = s ** 2 / np.sum(s ** 2)
    cum = np.cumsum(var)
    k80 = int(np.searchsorted(cum, 0.80) + 1)
    return {"stems": stems, "scores": u * s, "var": var, "k80": k80, "loadings": vt, "columns": list(columns),
            "mu": mu, "sd": sd.ravel(), "missing": 1 - np.isfinite(x).mean(axis=0)}


def shared(space_a, space_b, k_a=None, k_b=None):
    """Scores of the cells in both spaces, in the order of space_b (as the code's align_pair)."""
    pos_a = {s: i for i, s in enumerate(space_a["stems"])}
    stems = [s for s in space_b["stems"] if s in pos_a]
    pos_b = {s: i for i, s in enumerate(space_b["stems"])}
    ia = np.array([pos_a[s] for s in stems], dtype=int)
    ib = np.array([pos_b[s] for s in stems], dtype=int)
    ka = k_a or space_a["k80"]
    kb = k_b or space_b["k80"]
    return stems, space_a["scores"][ia, :ka], space_b["scores"][ib, :kb]


# --- basic measures -----------------------------------------------------------------------------

def pairwise_euclidean(x):
    x = np.asarray(x, dtype=np.float64)
    nrm = np.sum(x * x, axis=1, keepdims=True)
    d2 = nrm + nrm.T - 2.0 * (x @ x.T)
    np.maximum(d2, 0.0, out=d2)
    d = np.sqrt(d2)
    np.fill_diagonal(d, 0.0)
    return d


def ordinal_ranks(x, axis=-1):
    return np.argsort(np.argsort(x, axis=axis), axis=axis).astype(float)


def spearman(a, b):
    """The code's Spearman: Pearson correlation of np.argsort(np.argsort(.)) ranks."""
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    if a.size < 3:
        return float("nan")
    ra, rb = ordinal_ranks(a), ordinal_ranks(b)
    if ra.std() == 0 or rb.std() == 0:
        return float("nan")
    return float(np.corrcoef(ra, rb)[0, 1])


def spearman_avg(a, b):
    """Tie-corrected Spearman (average ranks), a variant."""
    ra, rb = rankdata(a), rankdata(b)
    if ra.std() == 0 or rb.std() == 0:
        return float("nan")
    return float(np.corrcoef(ra, rb)[0, 1])


def sample_pairs(n, rng, n_pairs=80000, unique=True):
    """80,000 cell pairs i < j: unique pairs (Methods) or the code's draw (``unique=False``)."""
    max_pairs = n * (n - 1) // 2
    take = min(n_pairs, max_pairs)
    if unique:
        flat = rng.choice(max_pairs, size=take, replace=False)
        # invert the row-major index of the strict upper triangle
        i = (n - 2 - np.floor(np.sqrt(-8 * flat + 4 * n * (n - 1) - 7) / 2.0 - 0.5)).astype(np.int64)
        j = (flat + i + 1 - n * (n - 1) // 2 + (n - i) * ((n - i) - 1) // 2).astype(np.int64)
        return i, j
    i = rng.integers(0, n, size=take * 3)
    j = rng.integers(0, n, size=take * 3)
    m = i < j
    return i[m][:take], j[m][:take]


def emp_p(null, obs):
    null = np.asarray(null, dtype=float)
    return float((1.0 + np.sum(null >= obs)) / (1.0 + null.size))


# --- cell level ---------------------------------------------------------------------------------

def distance_correlation(xa, xb, rng, n_shuffle=100, unique=True):
    """Spearman of the two regimes' distances over sampled pairs, with a cell-index permutation null."""
    n = xa.shape[0]
    da, db = pairwise_euclidean(xa), pairwise_euclidean(xb)
    ii, jj = sample_pairs(n, rng, unique=unique)
    ua, ub = da[ii, jj], db[ii, jj]
    rho = spearman(ua, ub)
    null = np.empty(n_shuffle)
    for t in range(n_shuffle):
        perm = rng.permutation(n)
        null[t] = spearman(ua, db[perm[ii], perm[jj]])
    if not n_shuffle:
        null = np.array([np.nan])
    return {"rho": rho, "p": emp_p(null, rho), "null_mean": float(null.mean()), "null_max": float(null.max()),
            "n": n, "n_pairs": int(ii.size), "n_unique_pairs": int(len(set(zip(ii.tolist(), jj.tolist()))))}


def knn_indices(d, k):
    n = d.shape[0]
    k = min(k, n - 1)
    idx = np.argpartition(d, kth=k, axis=1)[:, : k + 1]
    out = np.empty((n, k), dtype=np.int64)
    for i in range(n):
        row = idx[i][idx[i] != i]
        if row.size < k:
            full = np.argsort(d[i])
            row = full[full != i]
        out[i] = row[:k]
    return out


def membership(idx, n):
    m = np.zeros((idx.shape[0], n), dtype=bool)
    np.put_along_axis(m, idx, True, axis=1)
    return m


def jaccard_rows(ma, mb, k):
    inter = np.count_nonzero(ma & mb, axis=1)
    return inter / (2 * k - inter)


def knn_jaccard(xa, xb, k, rng, n_shuffle=100):
    """Mean Jaccard of each cell's k nearest neighbours in two spaces, and the index-shuffle chance
    (the code's q1_knn_scale: the second regime's neighbour lists permuted across cells)."""
    n = xa.shape[0]
    k = min(k, n - 1)
    ma = membership(knn_indices(pairwise_euclidean(xa), k), n)
    mb = membership(knn_indices(pairwise_euclidean(xb), k), n)
    jac = jaccard_rows(ma, mb, k)
    null = np.empty(n_shuffle)
    for t in range(n_shuffle):
        null[t] = jaccard_rows(ma, mb[rng.permutation(n)], k).mean()
    return {"k": k, "n": n, "mean": float(jac.mean()), "median": float(np.median(jac)), "chance": float(null.mean()),
            "chance_sd": float(null.std()), "adjusted": float(jac.mean() - null.mean()), "per_cell": jac}


def mobility(spaces):
    """One minus the mean, over the three regime pairs, of the Spearman correlation of a cell's
    distances to the other triple-shared cells (the code's compute_mobility)."""
    sets = [set(spaces[p]["stems"]) for p in REGIMES]
    stems = [s for s in spaces["long_pulse"]["stems"] if s in sets[1] and s in sets[2]]
    n = len(stems)
    ranks = {}
    off = ~np.eye(n, dtype=bool)
    for p in REGIMES:
        pos = {s: i for i, s in enumerate(spaces[p]["stems"])}
        idx = np.array([pos[s] for s in stems], dtype=int)
        d = pairwise_euclidean(spaces[p]["scores"][idx, : spaces[p]["k80"]])
        d = d[off].reshape(n, n - 1)
        r = ordinal_ranks(d, axis=1)
        r -= r.mean(axis=1, keepdims=True)
        r /= np.sqrt((r ** 2).sum(axis=1, keepdims=True))
        ranks[p] = r
        del d
    rhos = np.column_stack([np.sum(ranks[a] * ranks[b], axis=1) for a, b in PAIRS])
    return stems, 1.0 - rhos.mean(axis=1), rhos


# --- labels -------------------------------------------------------------------------------------

def labelled(space, join, key, k=None):
    """Scores (first k components) and labels of the space's cells with a non-empty label."""
    k = k or space["k80"]
    xi, labs = [], []
    for i, s in enumerate(space["stems"]):
        lab = (join.get(s, {}).get(key) or "").strip()
        if lab:
            xi.append(i)
            labs.append(lab)
    return space["scores"][np.array(xi, dtype=int), :k], np.array(labs, dtype=object), np.array(xi, dtype=int)


def encode(labels):
    uniq = {v: i for i, v in enumerate(sorted(set(labels.tolist())))}
    return np.array([uniq[v] for v in labels], dtype=int)


def eta2(x, labels):
    """Multivariate eta squared: between-group over total sum of squares (Methods, "Biological anchoring")."""
    x = np.asarray(x, dtype=float)
    grand = x.mean(axis=0)
    total = np.sum((x - grand) ** 2)
    between = 0.0
    for lab in np.unique(labels):
        sel = labels == lab
        between += sel.sum() * float(np.sum((x[sel].mean(axis=0) - grand) ** 2))
    return float(between / total)


def alignment(x, labels, rng, n_shuffle=100, average_ranks=False):
    """A_t: Spearman of binary label mismatch with phenotypic distance over 80,000 sampled pairs
    (the code's align_D, pairs drawn as its sample_pairs), with a label-permutation null."""
    n = x.shape[0]
    ii, jj = sample_pairs(n, rng, unique=False)
    xi, xj = x[ii], x[jj]
    ua = np.sqrt(np.sum((xi - xj) ** 2, axis=1))
    sp = spearman_avg if average_ranks else spearman
    lab = np.asarray(labels)
    rho = sp(ua, (lab[ii] != lab[jj]).astype(float))
    null = np.empty(n_shuffle)
    for t in range(n_shuffle):
        perm = rng.permutation(n)
        null[t] = sp(ua, (lab[perm[ii]] != lab[perm[jj]]).astype(float))
    if not n_shuffle:
        null = np.array([np.nan])
    return {"A": rho, "p": emp_p(null, rho), "null_mean": float(null.mean()), "null_max": float(null.max()), "n": n}


def residualize(x, groups):
    out = np.array(x, dtype=float, copy=True)
    for g in np.unique(groups):
        sel = groups == g
        out[sel] -= out[sel].mean(axis=0)
    return out


def knn_enrichment(x, labels, k=15):
    """Same-label fraction among each cell's k neighbours against chance (n_type - 1)/(n - 1)."""
    n = x.shape[0]
    idx = knn_indices(pairwise_euclidean(x), k)
    lab = np.asarray(labels)
    same = (lab[idx] == lab[:, None]).mean(axis=1)
    counts = Counter(lab.tolist())
    chance = np.array([(counts[v] - 1) / (n - 1) for v in lab])
    with np.errstate(divide="ignore", invalid="ignore"):
        per_cell = np.where(chance > 0, same / chance, np.nan)
    return {"ratio_of_means": float(same.mean() / chance.mean()), "mean_of_ratios": float(np.nanmean(per_cell)),
            "same": float(same.mean()), "chance": float(chance.mean()), "n": n}


# --- type level ---------------------------------------------------------------------------------

def centroid_distances(x, codes, n_types):
    """Euclidean distances between the centroids of types 0..n_types-1 (codes outside are ignored)."""
    sel = (codes >= 0) & (codes < n_types)
    sums = np.zeros((n_types, x.shape[1]))
    np.add.at(sums, codes[sel], x[sel])
    cnt = np.bincount(codes[sel], minlength=n_types).astype(float)
    m = sums / cnt[:, None]
    return pairwise_euclidean(m), cnt


def upper(s):
    i, j = np.triu_indices(s.shape[0], k=1)
    return s[i, j]


def type_codes(labels, types):
    pos = {t: i for i, t in enumerate(types)}
    return np.array([pos.get(v, -1) for v in labels], dtype=int)


def rank_norm(v):
    r = ordinal_ranks(v)
    return r / max(1.0, r.size - 1)


def pair_tags(s_by_regime, stable_cv=0.25, selective_range=0.55):
    """The code's tags: per type pair, CV and range of the three rank-normalized S values."""
    ranks = np.column_stack([rank_norm(upper(s_by_regime[p])) for p in REGIMES])
    mean = ranks.mean(axis=1)
    cv = np.where(mean > 1e-9, ranks.std(axis=1) / np.where(mean > 1e-9, mean, 1), 0.0)
    rng_r = ranks.max(axis=1) - ranks.min(axis=1)
    tags = np.where(cv < stable_cv, "stable", np.where(rng_r >= selective_range, "selective", "intermediate"))
    return tags, cv, rng_r, mean
