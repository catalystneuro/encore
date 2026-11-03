"""HMM-GLM and static decoders of Methods 17 (Padilla-Coreano et al. 2022), ported from MATLAB.

The HMM-GLM is a line-by-line port of `model_HMMGLM.m` and `run_model.m` of
github.com/Tyelab/HMMGLM at commit 3fc3567815b9c891402635664a844320136d2fac, the code the paper
links for this model, vectorised over trials. Everything below is as that code fixes it, including
its numerical guards:

- parameters `F_tr` (D+1, K, K) for the transitions and `F_em` (D+1, K, J) for the emissions, the
  last input being a constant 1; initial state prior `Pi`;
- initialisation (`parameter_initialization`, "gaussian_std"): every weight drawn from a normal
  of mean 0 and SD 0.001, `Pi` uniform;
- transition probabilities (`alpha`): exp(F_tr[:, c, c'] . x_t) + 1e-4, normalised over c';
  emission probabilities (`eta`): exp(F_em[:, c, j] . x_t) + 0.01, normalised over j;
- scaled forward and backward passes (`forward`, `backward`), with the code's floor of 1e-323;
  state marginals (`gamma`) and pair marginals (`zeta`, which uses the transition at t+1, as the
  code does);
- training ("baum_welch_auxilary", "gradient_ascent"): 100 epochs of full-batch gradient ascent on
  the Baum-Welch auxiliary function with learning rate 1e-6 / (1 + epoch / 128) and a Gaussian
  penalty of 1/0.001 on the weights, `Pi` renormalised after each step;
- prediction (`predict_likelihood_onestep`): at t the state distribution is `Pi` (t = 0) or the
  transition row of the previous step's state, the emission likelihood of each label is
  normalised over states (as in the code), and the state taken at t is the one under which the
  true label at t is most likely;
- held-out log-likelihood (`inference`, "log_likelihood"): minus the sum of the log scales of the
  forward pass;
- folds (`run_model.m`): 10 contiguous blocks of trials in the order given;
- AUC (`run_model.m`, MATLAB `perfcurve`): per label and fold, one against all over every time
  point of the held-out trials, without shift (`auc_roc`) and with the one-bin shift of
  `auc_ROC_delay` (labels at 1..T-1 against predictions at 2..T).

The static decoders follow the Methods 17 text ("Generalized Linear Model", "Ensemble of GLMs"):
a multinomial logit GLM with a 9-output softmax, and 9 binary logit GLMs, each fitted by maximum
likelihood on the neural activity of each time point. The paper names no regularisation or
solver; MATLAB's `mnrfit` and `glmfit` are unregularised maximum likelihood, and a ridge of 1e-4
is added here only to keep the fit finite on separable data (a standard choice). Inputs are scaled
per channel by the training set's SD for the static fits only, to help the solver.
"""

from __future__ import annotations

import io
import urllib.request
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import get_context

import numpy as np
from scipy.io import loadmat
from scipy.optimize import minimize
from scipy.stats import rankdata

# The paper's processed HMM-GLM input (965 trials x 32 channels x 70 bins, with labels), in the code
# repository at the pinned commit; a variant input only (claims file, fig1i criterion).
PAPER_INPUT_URL = ("https://raw.githubusercontent.com/Tyelab/HMMGLM/3fc3567815b9c891402635664a844320136d2fac/"
                   "dataset_forHMMGLM_proc.mat")

EPS_ALPHA = 1e-4
EPS_ETA = 0.01
FLOOR = 1e-323
SIGMA = 0.001        # init SD and penalty (1/SIGMA), "gaussian_std"
ETA0, TEMP = 1e-6, 128.0
N_EPOCHS = 100
K_STATES = 6
N_FOLDS = 10


def _aug(X: np.ndarray) -> np.ndarray:
    """(M, D, T) -> (M, T, D+1) with the constant input last."""
    M, D, T = X.shape
    return np.concatenate([np.transpose(X, (0, 2, 1)), np.ones((M, T, 1))], axis=2)


def paper_input() -> dict:
    """The paper's processed input, read into memory from the pinned commit (not written to disk)."""
    with urllib.request.urlopen(PAPER_INPUT_URL, timeout=120) as u:
        m = loadmat(io.BytesIO(u.read()))
    return {k: v for k, v in m.items() if not k.startswith("__")}


def _lin(Xa, F):
    """(M, T, D+1) x (D+1, K, L) -> (M, T, K, L)."""
    M, T, D1 = Xa.shape
    return (Xa.reshape(-1, D1) @ F.reshape(D1, -1)).reshape(M, T, *F.shape[1:])


def _grad(w, Xa):
    """sum over m, t of w (M, T, K, L) times Xa (M, T, D+1) -> (D+1, K, L)."""
    D1 = Xa.shape[2]
    return (Xa.reshape(-1, D1).T @ w.reshape(-1, w.shape[2] * w.shape[3])).reshape(D1, w.shape[2], w.shape[3])


class HMMGLM:
    def __init__(self, D: int, K: int, J: int, rng: np.random.Generator):
        self.D, self.K, self.J = D, K, J
        n_tr, n_em = (D + 1) * K * K, (D + 1) * K * J
        p = rng.normal(0.0, SIGMA, n_tr + n_em)
        self.F_tr = p[:n_tr].reshape(D + 1, K, K)
        self.F_em = p[n_tr:].reshape(D + 1, K, J)
        self.Pi = np.full(K, 1.0 / K)

    def alpha(self, Xa):
        a = np.exp(_lin(Xa, self.F_tr)) + EPS_ALPHA
        return a / a.sum(-1, keepdims=True)

    def eta(self, Xa):
        with np.errstate(over="ignore"):
            e = np.exp(_lin(Xa, self.F_em)) + EPS_ETA
        e = np.where(np.isinf(e), np.exp(709.0), e)
        return e / e.sum(-1, keepdims=True)

    def _forward_backward(self, Xa, Y):
        M, T, _ = Xa.shape
        A, E = self.alpha(Xa), self.eta(Xa)
        Ey = np.take_along_axis(E, Y[:, :, None, None], axis=3)[..., 0]    # (M, T, K)
        a = np.zeros((M, T, self.K))
        c = np.zeros((M, T))
        a[:, 0] = self.Pi * Ey[:, 0]
        c[:, 0] = 1.0 / a[:, 0].sum(1)
        a[:, 0] *= c[:, 0, None]
        for t in range(1, T):
            v = np.einsum("mk,mkc->mc", a[:, t - 1], A[:, t - 1]) * Ey[:, t]
            v[v == 0] = FLOOR
            ct = 1.0 / v.sum(1)
            ct[np.isinf(ct)] = 1e308
            a[:, t] = v * ct[:, None]
            c[:, t] = ct
        b = np.zeros((M, T, self.K))
        b[:, T - 1] = 1.0
        for t in range(T - 2, -1, -1):
            v = np.einsum("mck,mk->mc", A[:, t], Ey[:, t + 1] * b[:, t + 1])
            v[v == 0] = FLOOR
            b[:, t] = v
        b *= c[:, :, None]
        return A, E, Ey, a, b, c

    def fit(self, X, Y, n_epochs: int = N_EPOCHS):
        """X (M, D, T), Y (M, T) with labels 0..J-1."""
        Xa = _aug(X)
        M, T, _ = Xa.shape
        onehot = np.eye(self.J)[Y]                                        # (M, T, J)
        for ep in range(n_epochs):
            lr = ETA0 / (1 + ep / TEMP)
            A, E, Ey, a, b, c = self._forward_backward(Xa, Y)
            g = a * b + FLOOR
            g /= g.sum(2, keepdims=True)                                  # gamma (M, T, K)
            z = a[:, :-1, :, None] * (b[:, 1:, None, :] * A[:, 1:] * Ey[:, 1:, None, :])
            z /= z.sum((2, 3), keepdims=True) + 1e-8                      # zeta at t = 0..T-2
            # gradient terms of run t = 1..T-1 use zeta at t (zero at T-1), alpha at t, gamma at t-1
            zt = np.concatenate([z[:, 1:], np.zeros((M, 1, self.K, self.K))], axis=1)
            w_tr = zt - A[:, 1:] * g[:, :-1, :, None]                       # (M, T-1, K, K)
            grad_tr = _grad(w_tr, Xa[:, 1:])
            w_em = (onehot[:, :, None, :] - E) * g[:, :, :, None]           # (M, T, K, J)
            grad_em = _grad(w_em, Xa)
            grad_pi = (g[:, 0] / self.Pi).sum(0)
            grad_tr -= self.F_tr / SIGMA
            grad_em -= self.F_em / SIGMA
            self.Pi = self.Pi + lr * grad_pi
            self.F_tr = self.F_tr + lr * grad_tr
            self.F_em = self.F_em + lr * grad_em
            self.Pi = self.Pi / self.Pi.sum()
        return self

    def loglik(self, X, Y) -> np.ndarray:
        """Per trial, minus the sum of the log forward scales (`inference`, "log_likelihood")."""
        c = self._forward_backward(_aug(X), Y)[5]
        return -np.log(c).sum(1)

    def predict_onestep(self, X, Y) -> np.ndarray:
        """(M, J, T) label likelihoods, as `predict_likelihood_onestep`."""
        Xa = _aug(X)
        M, T, _ = Xa.shape
        with np.errstate(over="ignore"):
            L = np.exp(_lin(Xa, self.F_em))
        L = L / L.sum(2, keepdims=True)                                   # normalised over states
        out = np.zeros((M, self.J, T))
        h = np.zeros(M, dtype=int)
        for t in range(T):
            if t == 0:
                sp = np.broadcast_to(self.Pi, (M, self.K))
            else:
                logit = np.einsum("md,mdk->mk", Xa[:, t - 1], self.F_tr[:, h, :].transpose(1, 0, 2))
                sp = np.exp(logit)
                sp = sp / sp.sum(1, keepdims=True)
            out[:, :, t] = np.einsum("mkj,mk->mj", L[:, t], sp)
            h = np.argmax(L[np.arange(M), t, :, Y[:, t]], axis=1)
        return out


def auc(y: np.ndarray, s: np.ndarray) -> float:
    """Area under the ROC curve of score s for binary y (ties count half, as perfcurve's trapezoid)."""
    ok = ~np.isnan(s)                 # perfcurve's default ProcessNaN 'ignore'
    y, s = y[ok].astype(bool), s[ok]
    n1, n0 = y.sum(), (~y).sum()
    if n1 == 0 or n0 == 0:
        return np.nan
    r = rankdata(s)
    return float((r[y].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))


def fold_aucs(Y: np.ndarray, P: np.ndarray, J: int) -> tuple[np.ndarray, np.ndarray]:
    """Per label, AUC without shift and with the one-bin shift (auc_ROC, auc_ROC_delay)."""
    a0 = np.array([auc(Y.ravel() == j, P[:, j, :].ravel()) for j in range(J)])
    a1 = np.array([auc(Y[:, :-1].ravel() == j, P[:, j, 1:].ravel()) for j in range(J)])
    return a0, a1


def folds(n: int, k: int = N_FOLDS, rng: np.random.Generator | None = None) -> list[np.ndarray]:
    """Contiguous blocks as run_model.m forms them (round((k-1)N/K)+1 : round(kN/K)), or random blocks."""
    order = np.arange(n) if rng is None else rng.permutation(n)
    edges = [int(np.floor(i * n / k + 0.5)) for i in range(k + 1)]   # MATLAB round, half away from zero
    return [order[edges[i]:edges[i + 1]] for i in range(k)]


# ---------------------------------------------------------------- static decoders

def _softmax(z):
    z = z - z.max(1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(1, keepdims=True)


def fit_mnlogit(x: np.ndarray, y: np.ndarray, J: int, ridge: float = 1e-4) -> np.ndarray:
    """Multinomial logit (softmax over J labels, label 0 as reference); x (n, D) with no constant."""
    n, D = x.shape
    xa = np.c_[x, np.ones(n)]
    Y = np.eye(J)[y]

    def f(w):
        W = np.c_[np.zeros(D + 1), w.reshape(D + 1, J - 1)]
        P = _softmax(xa @ W)
        ll = np.sum(Y * np.log(P + 1e-300))
        g = xa.T @ (Y - P)
        return -ll / n + ridge * np.sum(w ** 2), (-g[:, 1:].ravel() / n + 2 * ridge * w)

    r = minimize(f, np.zeros((D + 1) * (J - 1)), jac=True, method="L-BFGS-B", options={"maxiter": 500})
    return np.c_[np.zeros(D + 1), r.x.reshape(D + 1, J - 1)]


def predict_mnlogit(W, x):
    return _softmax(np.c_[x, np.ones(len(x))] @ W)


def fit_logit(x: np.ndarray, y: np.ndarray, ridge: float = 1e-4) -> np.ndarray:
    n, D = x.shape
    xa = np.c_[x, np.ones(n)]

    def f(w):
        z = xa @ w
        p = 1 / (1 + np.exp(-z))
        ll = np.sum(y * z - np.logaddexp(0, z))
        return -ll / n + ridge * np.sum(w ** 2), -(xa.T @ (y - p)) / n + 2 * ridge * w

    return minimize(f, np.zeros(D + 1), jac=True, method="L-BFGS-B", options={"maxiter": 500}).x


def static_predictions(Xtr, Ytr, Xte, J: int) -> dict[str, np.ndarray]:
    """GLM, 9 GLMs and the frequency table, each as (M_test, J, T) likelihoods."""
    M, D, T = Xte.shape
    xtr = np.transpose(Xtr, (0, 2, 1)).reshape(-1, D)
    ytr = Ytr.ravel()
    xte = np.transpose(Xte, (0, 2, 1)).reshape(-1, D)
    sd = xtr.std(0)
    sd[sd == 0] = 1
    xtr, xte = xtr / sd, xte / sd
    back = lambda p: p.reshape(M, T, J).transpose(0, 2, 1)
    out = {"GLM": back(predict_mnlogit(fit_mnlogit(xtr, ytr, J), xte))}
    nine = np.zeros((len(xte), J))
    for j in range(J):
        w = fit_logit(xtr, (ytr == j).astype(float))
        nine[:, j] = 1 / (1 + np.exp(-(np.c_[xte, np.ones(len(xte))] @ w)))
    out["9 GLMs"] = back(nine)
    freq = np.bincount(ytr, minlength=J) / len(ytr)
    out["FT"] = np.broadcast_to(freq[None, :, None], (M, J, T)).copy()
    return out


def _fold(args):
    X, Y, J, te, seed, k_states, static, n_epochs = args
    tr = np.setdiff1d(np.arange(len(X)), te)
    m = HMMGLM(X.shape[1], k_states, J, np.random.default_rng(seed)).fit(X[tr], Y[tr], n_epochs)
    preds = {"HMM-GLM": m.predict_onestep(X[te], Y[te])}
    ll = float(m.loglik(X[te], Y[te]).mean())
    if static:
        preds.update(static_predictions(X[tr], Y[tr], X[te], J))
    return ll, {name: fold_aucs(Y[te], P, J) for name, P in preds.items()}


def cross_validate(X, Y, J: int, seed: int, k_states: int = K_STATES, contiguous: bool = True,
                   static: bool = True, n_epochs: int = N_EPOCHS, workers: int = 4,
                   test_sets: list[np.ndarray] | None = None) -> dict:
    """10-fold CV (or the given test sets, such as one animal each). Returns per-model AUC arrays (folds x labels) without and with the shift,
    and the HMM-GLM's mean held-out log-likelihood per fold. Each fold has its own seed, drawn
    from `seed`, so the result does not depend on the number of workers."""
    rng = np.random.default_rng(seed)
    fs = test_sets if test_sets is not None else folds(len(X), rng=None if contiguous else rng)
    seeds = rng.integers(0, 2 ** 31, len(fs))
    jobs = [(X, Y, J, te, int(s), k_states, static, n_epochs) for te, s in zip(fs, seeds)]
    if workers > 1:
        with ProcessPoolExecutor(workers, mp_context=get_context("fork")) as ex:
            out = list(ex.map(_fold, jobs))
    else:
        out = [_fold(j) for j in jobs]
    res = {"auc": {}, "auc_delay": {}, "loglik": [ll for ll, _ in out]}
    for _, a in out:
        for name, (a0, a1) in a.items():
            res["auc"].setdefault(name, []).append(a0)
            res["auc_delay"].setdefault(name, []).append(a1)
    for key in ("auc", "auc_delay"):
        res[key] = {k: np.array(v) for k, v in res[key].items()}
    return res


def train_test(Xtr, Ytr, Xte, Yte, J: int, seed: int, k_states: int = K_STATES) -> tuple[np.ndarray, np.ndarray]:
    """HMM-GLM trained on one set and tested on another: per-label AUCs without and with the shift."""
    m = HMMGLM(Xtr.shape[1], k_states, J, np.random.default_rng(seed)).fit(Xtr, Ytr)
    return fold_aucs(Yte, m.predict_onestep(Xte, Yte), J)
