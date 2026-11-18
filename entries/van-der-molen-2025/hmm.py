"""Poisson hidden Markov models for van der Molen et al. (2025), in place of the SSM package.

The paper fits HMMs with Poisson observations using SSM (Supplementary Methods, "Hidden Markov
model analysis"), on spike counts in 30 ms bins, with 10 to 30 hidden states, by EM (the code's
tolerance 1e-3, at most 5000 iterations; claims file). SSM is not on PyPI in a form that installs in
a locked environment, so this module implements the same model: a stationary transition matrix, an
initial state distribution, and one Poisson rate per unit and state, fitted by Baum-Welch EM. The
initialisation (k-means on the binned counts, transitions with 0.9 on the diagonal) is a standard
choice; the iteration limit (300) is lower than the code's, a deviation stated in the notebook.
"""
import numba
import numpy as np
from scipy.special import gammaln

BIN_MS = 30  # Supplementary Methods
TOL = 1e-3  # claims file (the code's tolerance)
MAX_ITER = 300


def bin_counts(M, bin_ms=BIN_MS):
    """Spike counts per unit in bins of bin_ms frames of a 1 ms matrix: bins by units."""
    U, T = M.shape
    n = T // bin_ms
    return M[:, :n * bin_ms].reshape(U, n, bin_ms).sum(2).T.astype(np.float64)


def log_emissions(X, lam):
    """log P(x_t | state k) for Poisson rates lam (states by units): bins by states."""
    ll = X @ np.log(lam).T - lam.sum(1)[None, :]
    return ll - gammaln(X + 1).sum(1)[:, None]


def _forward_backward(logB, A, pi):
    m = logB.max(axis=1)
    B = np.exp(logB - m[:, None])
    gamma, xi, lc = _fb(np.ascontiguousarray(B), np.ascontiguousarray(A), np.ascontiguousarray(pi))
    return gamma, xi, lc + m.sum()


@numba.njit(cache=True)
def _fb(B, A, pi):
    T, K = B.shape
    alpha = np.zeros((T, K))
    beta = np.zeros((T, K))
    c = np.zeros(T)
    a = pi * B[0]
    c[0] = a.sum()
    alpha[0] = a / c[0]
    for t in range(1, T):
        a = (alpha[t - 1] @ A) * B[t]
        c[t] = a.sum()
        alpha[t] = a / c[t]
    beta[T - 1] = 1.0
    for t in range(T - 2, -1, -1):
        beta[t] = (A @ (B[t + 1] * beta[t + 1])) / c[t + 1]
    gamma = alpha * beta
    xi = np.zeros((K, K))
    for t in range(T - 1):
        bb = B[t + 1] * beta[t + 1]
        for i in range(K):
            for j in range(K):
                xi[i, j] += alpha[t, i] * A[i, j] * bb[j] / c[t + 1]
    return gamma, xi, np.log(c).sum()


@numba.njit(cache=True)
def _viterbi(logB, logA, logpi):
    T, K = logB.shape
    d = logpi + logB[0]
    ptr = np.zeros((T, K), np.int64)
    for t in range(1, T):
        nd = np.empty(K)
        for j in range(K):
            best, arg = -np.inf, 0
            for i in range(K):
                v = d[i] + logA[i, j]
                if v > best:
                    best, arg = v, i
            nd[j] = best + logB[t, j]
            ptr[t, j] = arg
        d = nd
    path = np.zeros(T, np.int64)
    path[T - 1] = np.argmax(d)
    for t in range(T - 1, 0, -1):
        path[t - 1] = ptr[t, path[t]]
    return path


def init_params(X, K, seed):
    from sklearn.cluster import KMeans
    km = KMeans(n_clusters=K, n_init=1, random_state=seed).fit(X)
    lam = np.array([X[km.labels_ == k].mean(0) if (km.labels_ == k).any() else X.mean(0) for k in range(K)])
    lam = np.maximum(lam, 1e-3)
    A = np.full((K, K), 0.1 / (K - 1))
    np.fill_diagonal(A, 0.9)
    pi = np.full(K, 1.0 / K)
    return lam, A, pi


def fit(X, K, seed=0, mask=None, max_iter=MAX_ITER, tol=TOL):
    """Baum-Welch EM. mask (bins by units, True = observed) leaves entries out of the likelihood,
    for the held-out cross-validation of the code's cv_scores."""
    lam, A, pi = init_params(X if mask is None else np.where(mask, X, 0), K, seed)
    Xm = X if mask is None else np.where(mask, X, 0.0)
    W = np.ones_like(X) if mask is None else mask.astype(np.float64)
    prev = -np.inf
    for it in range(max_iter):
        logB = (Xm @ np.log(lam).T) - W @ lam.T
        gamma, xi, ll = _forward_backward(logB, A, pi)
        lam = np.maximum((gamma.T @ Xm) / np.maximum(gamma.T @ W, 1e-12), 1e-6)
        A = xi / xi.sum(1, keepdims=True)
        A = np.maximum(A, 1e-12)
        A /= A.sum(1, keepdims=True)
        pi = np.maximum(gamma[0], 1e-12)
        pi /= pi.sum()
        if abs(ll - prev) < tol:
            break
        prev = ll
    return dict(lam=lam, A=A, pi=pi, iters=it + 1, loglik=ll)


def states(model, X):
    logB = log_emissions(X, model["lam"])
    return _viterbi(logB, np.log(model["A"]), np.log(model["pi"]))


def loglik(model, X, mask=None):
    """Log likelihood of X; with mask, of the masked entries' complement given the rest is the
    difference of two likelihoods (the code's cv_scores scores the held-out entries this way)."""
    lam = model["lam"]
    W = np.ones_like(X) if mask is None else mask.astype(np.float64)
    Xm = X * W
    logB = (Xm @ np.log(lam).T) - W @ lam.T - (gammaln(X + 1) * W).sum(1)[:, None]
    return _forward_backward(logB, model["A"], model["pi"])[2]
