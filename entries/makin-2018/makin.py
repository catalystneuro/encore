"""Loading and decoders for Makin, O'Doherty, Cardoso & Sabes (2018) on dandiset 000129.

Where each choice comes from is marked in the docstrings:
  [claims]  the criterion or the header of claims/000129/10.1088-1741-2552-aa9e95.yaml
  [paper]   a passage of the paper (Methods unless said otherwise)
  [code]    the paper's code, https://github.com/jgmakin/rbmish at commit 700062f5
  [assumed] an assumption, with the reason
  [standard] a standard choice for a detail that cannot change a result

The dandiset holds one session of monkey I (Indy, M1 array only). Its training file
holds 649.1 s of spikes and kinematics; its test file holds spikes only (the Neural
Latents Benchmark withholds the behaviour), so only the training file is used.
"""
import os

import h5py
import numpy as np
import remfile
import requests
from scipy.signal import butter, filtfilt

DANDISET = "000129"
VERSION = "0.241017.1444"
TRAIN_ASSET = "sub-Indy/sub-Indy_desc-train_behavior+ecephys.nwb"
TEST_ASSET = "sub-Indy/sub-Indy_desc-test_ecephys.nwb"
FS_KIN = 250.0  # [paper] Polhemus sampled at 250 Hz; the file upsampled it to 1 kHz
VARS = ["x", "y", "vx", "vy", "ax", "ay"]
DECODERS = ["linear", "kfobs", "kflatent", "kflatent_kf", "wf", "ukf", "refh", "refh_kf"]


def asset_url(path, version=VERSION):
    r = requests.get(
        f"https://api.dandiarchive.org/api/dandisets/{DANDISET}/versions/{version}/assets/",
        params={"path": path},
    )
    r.raise_for_status()
    aid = [a for a in r.json()["results"] if a["path"] == path][0]["asset_id"]
    return f"https://api.dandiarchive.org/api/assets/{aid}/download/"


def open_asset(path):
    return h5py.File(remfile.File(asset_url(path)), "r")


def load_session():
    """Stream the training file: spike times per unit, unit ids, and kinematics at 1 kHz."""
    f = open_asset(TRAIN_ASSET)
    u = f["units"]
    ids = u["id"][:]
    st = u["spike_times"][:]
    idx = u["spike_times_index"][:]
    spikes = np.split(st, idx[:-1])
    heldout = u["heldout"][:].astype(bool)
    b = f["processing/behavior"]
    d = {
        "unit_ids": ids,
        "heldout": heldout,
        "spikes": spikes,
        "finger_pos": b["finger_pos"]["data"][:, :2],
        "cursor_pos": b["cursor_pos"]["data"][:],
        "target_pos": b["target_pos"]["data"][:],
        "conversion": float(b["finger_pos"]["data"].attrs["conversion"]),
        "unit": b["finger_pos"]["data"].attrs["unit"],
        "session_description": f["session_description"][()].decode(),
        "session_start_time": f["session_start_time"][()].decode(),
        "trials_split": f["intervals/trials/split"][:].astype(str),
        "trials_start": f["intervals/trials/start_time"][:],
    }
    loc = f["general/extracellular_ephys/electrodes/location"][:]
    d["electrode_locations"] = [x.decode() if isinstance(x, bytes) else str(x) for x in loc]
    sts = b["finger_pos"]["starting_time"]
    d["t0"] = float(sts[()])
    d["rate"] = float(sts.attrs["rate"])
    f.close()
    return d


def segments(valid):
    """Start and stop indices of runs of True."""
    v = np.r_[False, valid, False].astype(int)
    starts = np.where(np.diff(v) == 1)[0]
    stops = np.where(np.diff(v) == -1)[0]
    return list(zip(starts, stops))


def kinematics(pos_1k, reading="methods"):
    """Position, velocity and acceleration at 250 Hz from the 1 kHz series.

    reading "methods" [paper, Data acquisition]: fingertip position low-pass filtered
    non-causally (4th-order Butterworth, 10 Hz), then velocity and acceleration as
    differences times the sampling rate. reading "code" [code, getLatentsBMI.m]: no
    filter. Either way the 1 kHz series is taken back to 250 Hz by keeping every 4th
    sample [assumed: the file says the 250 Hz record was upsampled]. Each run of valid
    samples between the file's NaN gaps is treated separately; the last difference is
    repeated as in the code [code, getLatentsBMI.m], and the samples lost at a gap are NaN.
    """
    p = pos_1k[::4].astype(float)
    out = np.full((len(p), 6), np.nan)
    valid = ~np.isnan(p).any(1)
    bb, aa = butter(4, 10.0 / (FS_KIN / 2))
    for s, e in segments(valid):
        seg = p[s:e]
        if reading == "methods":
            seg = filtfilt(bb, aa, seg, axis=0)
        v = np.diff(seg, axis=0) * FS_KIN
        v = np.vstack([v, v[-1:]])
        a = np.diff(v, axis=0) * FS_KIN
        a = np.vstack([a, a[-1:]])
        out[s:e] = np.hstack([seg, v, a])
    return out


def bin_data(d, bin_ms=64, reading="methods"):
    """Spike counts in non-overlapping bins from the first kinematic time stamp, and the
    kinematic state per bin.

    [code, binSpikeCounts.m] bins start at the first kinematic sample. The state is the
    last 250 Hz sample of each bin for the Methods reading ("subsampled" [paper];
    [claims] header: the last sample is the main choice) and the mean over the bin for
    the code's reading [code]. A bin whose samples include a NaN gap gets NaN kinematics
    and is left out of fitting and scoring (a deviation; 3 gaps of 0.1 s in the file).
    """
    pos = d["finger_pos"] if reading == "methods" else d["cursor_pos"]
    k = kinematics(pos, reading)
    m = int(round(FS_KIN * bin_ms / 1000))
    nb = len(k) // m
    kk = k[: nb * m].reshape(nb, m, 6)
    X = kk[:, -1, :] if reading == "methods" else kk.mean(1)
    X[np.isnan(kk).any((1, 2))] = np.nan
    edges = d["t0"] + np.arange(nb + 1) * bin_ms / 1000.0
    R = np.stack([np.histogram(s, edges)[0] for s in d["spikes"]], 1).astype(float)
    return R, X, edges


def unit_filter(R, bin_ms, ntrain):
    """[code, getLatentsBMI.m] drop units with mean rate <= 0.5 Hz over the session or no
    spikes, then units whose binned counts duplicate another unit's over the training or
    the test part. Returns a boolean mask over units."""
    rate = R.mean(0) / (bin_ms / 1000.0)
    keep = (rate > 0.5) & (R.sum(0) > 0)
    idx = np.where(keep)[0]
    dup = set()
    for part in (R[:ntrain], R[ntrain:]):
        P = part[:, idx]
        for i in range(len(idx)):
            for j in range(i + 1, len(idx)):
                if np.array_equal(P[:, i], P[:, j]):
                    dup.add(idx[j])
    keep[list(dup)] = False
    return keep


# ---------------------------------------------------------------- scores

def rsq(Xhat, X):
    """[claims] R2 = 1 - SSerr/SStot per variable, SStot about the test mean."""
    return 1 - ((Xhat - X) ** 2).sum(0) / ((X - X.mean(0)) ** 2).sum(0)


def snr(r2):
    """[paper, Results] SNR = -10 log10(1 - R2), in dB."""
    if not hasattr(r2, "values"):
        r2 = np.asarray(r2)
    return -10 * np.log10(1 - r2)


# ---------------------------------------------------------------- linear-Gaussian tools

def ridge(F, Y, lam=0.0, intercept=True):
    """Least squares of Y on F (with a column of ones); lam adds lam*I to F'F as in
    [code, tools/linregress.m] (the intercept is penalized there too when it is a column)."""
    if intercept:
        F = np.hstack([F, np.ones((len(F), 1))])
    G = F.T @ F + lam * np.eye(F.shape[1])
    return np.linalg.solve(G, F.T @ Y)


def apply(B, F):
    return np.hstack([F, np.ones((len(F), 1))]) @ B


def learn_lds(Z, Y):
    """Fully observed LGDS by regression [paper, KFobs]: state on its predecessor, and
    observations on the state, each with an intercept; initial cumulants from every time
    point [paper]. Z and Y are lists of contiguous runs (bins with NaN kinematics split runs)."""
    Zp = np.vstack([z[:-1] for z in Z])
    Zf = np.vstack([z[1:] for z in Z])
    Ba = ridge(Zp, Zf)
    A, a = Ba[:-1].T, Ba[-1]
    Qz = np.cov((Zf - apply(Ba, Zp)).T, bias=True)
    Za, Ya = np.vstack(Z), np.vstack(Y)
    Bc = ridge(Za, Ya)
    C, c = Bc[:-1].T, Bc[-1]
    Rr = np.cov((Ya - apply(Bc, Za)).T, bias=True)
    return dict(A=A, a=a, Q=np.atleast_2d(Qz), C=C, c=c, R=np.atleast_2d(Rr),
                mu0=Za.mean(0), S0=np.cov(Za.T))


def kf_pass(A, a, Q, C, c, Ri, mu0, S0, Y, loglik=False):
    """Kalman filter, equation (2) of the paper, with the update in information form.
    The covariances do not depend on the data; once the predicted covariance stops
    changing (to 1e-13 relative) its steady-state matrices are reused, which gives the
    same result to rounding error. Ri is the inverse observation covariance, or a vector
    for a diagonal one. Returns filtered means, predicted means, and per-step covariances
    (filtered, predicted) up to the step where they settle, then the settled ones."""
    diag = Ri.ndim == 1
    CtRi = (C.T * Ri) if diag else C.T @ Ri
    CtRiC = CtRi @ C
    T, n = len(Y), A.shape[0]
    mf = np.empty((T, n)); mp = np.empty((T, n))
    Sf, Sp = [], []
    m, S = mu0, S0
    ll = 0.0
    steady = None
    if loglik:
        logdetR = -np.sum(np.log(Ri)) if diag else -np.linalg.slogdet(Ri)[1]
    for t in range(T):
        if t > 0:
            m = A @ m + a
            if steady is None:
                Snew = A @ S @ A.T + Q
                if t > 1 and np.max(np.abs(Snew - Sp[-1])) < 1e-13 * np.max(np.abs(Snew)):
                    steady = (Sp[-1], Si, Sn, ldK)
                S = Snew
        mp[t] = m
        if steady is None:
            Si = np.linalg.inv(S)
            K = Si + CtRiC
            Sn = np.linalg.inv(K)
            ldK = np.linalg.slogdet(K)[1] + np.linalg.slogdet(S)[1] if loglik else 0.0
            Sp.append(S); Sf.append(Sn)
        else:
            _, Si, Sn, ldK = steady
        e = Y[t] - c
        if loglik:
            r = e - C @ m
            CtRir = CtRi @ r
            q = (r @ (Ri * r) if diag else r @ Ri @ r) - CtRir @ Sn @ CtRir
            ll += -0.5 * (q + logdetR + ldK + len(r) * np.log(2 * np.pi))
        m = Sn @ (Si @ m + CtRi @ e)
        S = Sn
        mf[t] = m
    return mf, mp, Sf, Sp, ll


def kalman_filter(p, Y):
    """Filtered means of the LGDS p for observations Y."""
    R = p["R"]
    Ri = 1 / np.diag(R) if p.get("diagR") else np.linalg.inv(R)
    return kf_pass(p["A"], p["a"], p["Q"], p["C"], p["c"], Ri, p["mu0"], p["S0"], Y)[0]


# ---------------------------------------------------------------- data split

class Split:
    """Training and test bins [paper, Training and testing data]: train on the first
    `train_s` seconds, test on the rest of the session. Bins with NaN kinematics are kept
    in the spike sequence (filters run through them) and left out of fitting and scoring."""

    def __init__(self, R, X, bin_ms, train_s=320.0, test_start_s=320.0):
        n_tr = int(np.floor(train_s / (bin_ms / 1000.0)))
        n_te0 = int(np.floor(test_start_s / (bin_ms / 1000.0)))
        self.bin_ms = bin_ms
        self.n_te0 = n_te0
        self.Rpre = R[:n_te0]  # bins before the test part, the history of the first test bins
        self.Rtr, self.Xtr = R[:n_tr], X[:n_tr]
        self.Rte, self.Xte = R[n_te0:], X[n_te0:]
        self.oktr = ~np.isnan(self.Xtr).any(1)
        self.okte = ~np.isnan(self.Xte).any(1)

    def runs(self, A, ok):
        return [A[s:e] for s, e in segments(ok) if e - s > 2]

    def score(self, Xhat, from_s=None):
        """R2 on the test bins; from_s scores only the test bins from that time on."""
        ok = self.okte.copy()
        if from_s is not None:
            ok[: max(0, int(np.floor(from_s / (self.bin_ms / 1000.0))) - self.n_te0)] = False
        return rsq(Xhat[ok], self.Xte[ok])


def dynamic_map(sp, Xhat_tr, Xhat_te):
    """[paper, Decoding the latent-state models, eq. 10] a KF whose observations are the
    six static reconstructions, fit by regression on the training data like KFobs."""
    p = learn_lds(sp.runs(sp.Xtr, sp.oktr), sp.runs(Xhat_tr, sp.oktr))
    return kalman_filter(p, Xhat_te)


# ---------------------------------------------------------------- decoders

def dec_linear(sp):
    """[paper, Results, decoder 1] static linear map on the current bin, with intercept
    [code, staticLinearDecoder]."""
    B = ridge(sp.Rtr[sp.oktr], sp.Xtr[sp.oktr])
    return apply(B, sp.Rte)


def dec_kfobs(sp):
    """[paper, KFobs] LGDS with the kinematic state as latent state, fit by regression."""
    p = learn_lds(sp.runs(sp.Xtr, sp.oktr), sp.runs(sp.Rtr, sp.oktr))
    return kalman_filter(p, sp.Rte)


def wf_design(R, p):
    """Current and p-1 past bins of spike counts (zeros before the start)."""
    T, N = R.shape
    F = np.zeros((T, N * p))
    for k in range(p):
        F[k:, k * N:(k + 1) * N] = R[: T - k]
    return F


def dec_wf(sp, return_choice=False):
    """[paper, Wiener filter; code, tools/WFDecoder.m] ridge regression on 1 to
    round(0.4 s / bin) bins of history and penalty in {0, 800, ..., 4000}; both chosen on
    the last 20% of the training data by the mean R2 of x and y velocity, fitted on the
    first 80%. As in the code, the filter fitted on the 80% is the one applied to the test
    data. The penalty is added to F'F of the uncentred design with a column of ones, as
    in [code, linregress.m]. The history of the first test bins is the bins before them."""
    n = len(sp.Rtr)
    n80 = int(np.floor(0.8 * n))
    pmax = int(round(0.4 / (sp.bin_ms / 1000.0)))
    best = (-np.inf, None, None, None)
    for p in range(1, pmax + 1):
        F = wf_design(sp.Rtr, p)
        F1 = np.hstack([F, np.ones((n, 1))])
        tr = np.arange(n) < n80
        oktr = sp.oktr & tr
        okho = sp.oktr & ~tr
        G = F1[oktr].T @ F1[oktr]
        FY = F1[oktr].T @ sp.Xtr[oktr]
        w, V = np.linalg.eigh(G)
        VFY = V.T @ FY
        for lam in np.arange(0, 4001, 800):
            B = V @ (VFY / (w + lam)[:, None])
            r = rsq(F1[okho] @ B, sp.Xtr[okho])
            v = r[2:4].mean()
            if v > best[0]:
                best = (v, p, lam, B)
    _, p, lam, B = best
    F = wf_design(np.vstack([sp.Rpre[len(sp.Rpre) - (p - 1):], sp.Rte]), p)[p - 1:]
    out = np.hstack([F, np.ones((len(F), 1))]) @ B
    return (out, p, lam) if return_choice else out


def ukf_features(Xs):
    """[paper, UKF] tuning to the six states, the magnitudes of position, velocity and
    acceleration, and the interaction terms x xdot and y ydot."""
    p, v, a = Xs[..., 0:2], Xs[..., 2:4], Xs[..., 4:6]
    return np.concatenate([
        Xs,
        np.linalg.norm(p, axis=-1, keepdims=True),
        np.linalg.norm(v, axis=-1, keepdims=True),
        np.linalg.norm(a, axis=-1, keepdims=True),
        p[..., :1] * v[..., :1],
        p[..., 1:2] * v[..., 1:2],
    ], -1)


def dec_ukf(sp):
    """Unscented Kalman filter with nonlinear tuning, no taps [paper, UKF; code,
    filtersForNeuralData.m, 'ptaps' 1, 'ftaps' 0, 'htaps' 0]. Li's UKF2 package is not
    available here; this is a re-implementation [assumed]: linear state transition fit by
    regression; spike counts a linear function (with intercept) of the eleven tuning
    features, fit by least squares; full noise covariances from the residuals; the
    standard unscented transform with weights alpha 1, beta 0, kappa 0 [standard]."""
    Z = sp.runs(sp.Xtr, sp.oktr)
    Zp = np.vstack([z[:-1] for z in Z])
    Zf = np.vstack([z[1:] for z in Z])
    Ba = ridge(Zp, Zf)
    A, a = Ba[:-1].T, Ba[-1]
    Q = np.cov((Zf - apply(Ba, Zp)).T, bias=True)
    Xo, Ro = sp.Xtr[sp.oktr], sp.Rtr[sp.oktr]
    H = ridge(ukf_features(Xo), Ro)
    Rr = np.cov((Ro - apply(H, ukf_features(Xo))).T, bias=True)
    Ri = np.linalg.inv(Rr)
    n = 6
    lam = 0.0
    wm = np.full(2 * n + 1, 1.0 / (2 * (n + lam)))
    wm[0] = lam / (n + lam)
    m, S = Xo.mean(0), np.cov(Xo.T)
    out = np.empty((len(sp.Rte), n))
    for t in range(len(sp.Rte)):
        if t > 0:
            m = A @ m + a
            S = A @ S @ A.T + Q
        L = np.linalg.cholesky((n + lam) * S + 1e-9 * np.eye(n))
        sig = np.vstack([m, m + L.T, m - L.T])
        Ysig = apply(H, ukf_features(sig))
        ym = wm @ Ysig
        dY = Ysig - ym
        dX = sig - m
        Pxy = (dX * wm[:, None]).T @ dY
        # Pyy = dY' W dY + R; solve with the Woodbury identity (low-rank plus R)
        U = dY * np.sqrt(wm)[:, None]
        RiU = Ri @ U.T
        M = np.eye(2 * n + 1) + U @ RiU
        resid = sp.Rte[t] - ym
        Pyy_inv_resid = Ri @ resid - RiU @ np.linalg.solve(M, RiU.T @ resid)
        Pyy_inv_PxyT = Ri @ Pxy.T - RiU @ np.linalg.solve(M, RiU.T @ Pxy.T)
        m = m + Pxy @ Pyy_inv_resid
        S = S - Pxy @ Pyy_inv_PxyT
        S = (S + S.T) / 2
        out[t] = m
    return out


def factor_analysis(Y, k, n_iter=200, seed=0):
    """Factor analysis by EM [standard], used to initialize the LGDS EM [paper, KFlatent]."""
    rng = np.random.default_rng(seed)
    mu = Y.mean(0)
    Yc = Y - mu
    Syy = Yc.T @ Yc / len(Y)
    C = rng.standard_normal((Y.shape[1], k)) * np.sqrt(np.diag(Syy).mean() / k)
    psi = np.diag(Syy).copy()
    for _ in range(n_iter):
        Pi = 1 / psi
        G = np.linalg.inv(np.eye(k) + (C.T * Pi) @ C)
        beta = G @ (C.T * Pi)
        Ezz = G + beta @ Syy @ beta.T
        C = Syy @ beta.T @ np.linalg.inv(Ezz)
        psi = np.maximum(np.diag(Syy - C @ beta @ Syy), 1e-6)
    Ez = Yc @ beta.T
    return C, mu, psi, Ez


def lgds_em(Y, k, max_epochs=100, tol=1e-4, seed=0):
    """LGDS learned by EM with diagonal state and observation noise [paper, KFlatent],
    initialized by factor analysis; stopped when the log-likelihood gain of an epoch falls
    below 1/100 of a percent (tol = 1e-4) of the total gain so far, or at 100 epochs
    [paper, KFlatent: "a cross entropy decrease less than 1/100 of a percent of the total
    decrease"]. Y is one sequence. Returns the parameters, the number of E steps run and
    the log-likelihood after each."""
    T, N = Y.shape
    C, c, psi, Ez = factor_analysis(Y, k, seed=seed)
    Ba = ridge(Ez[:-1], Ez[1:])
    A, a = Ba[:-1].T, Ba[-1]
    Q = np.diag(np.maximum(np.var(Ez[1:] - apply(Ba, Ez[:-1]), 0), 1e-6))
    R = psi.copy()
    mu0, S0 = Ez.mean(0), np.cov(Ez.T)
    lls = []
    for ep in range(max_epochs):
        # E step: filter (information form, diagonal R) and RTS smoother
        mf, mp, Sf, Spr, ll = kf_pass(A, a, Q, C, c, 1 / R, mu0, S0, Y, loglik=True)
        lls.append(ll)
        nS = len(Sf)
        Jl = [Sf[t] @ A.T @ np.linalg.inv(Spr[t + 1]) for t in range(min(nS - 1, T - 1))]
        Jss = Sf[-1] @ A.T @ np.linalg.inv(Spr[-1])
        ms = mf.copy(); Ss = np.empty((T, k, k)); Scross = np.empty((T - 1, k, k))
        Ss[T - 1] = Sf[min(T - 1, nS - 1)]
        for t in range(T - 2, -1, -1):
            J = Jl[t] if t < len(Jl) else Jss
            Sft = Sf[min(t, nS - 1)]
            Spt = Spr[min(t + 1, nS - 1)]
            ms[t] = mf[t] + J @ (ms[t + 1] - mp[t + 1])
            Ss[t] = Sft + J @ (Ss[t + 1] - Spt) @ J.T
            Scross[t] = Ss[t + 1] @ J.T  # Cov(z_{t+1}, z_t)
        if len(lls) > 2 and (lls[-1] - lls[-2]) < tol * (lls[-1] - lls[0]):
            break
        # M step
        Ezz = Ss + np.einsum("ti,tj->tij", ms, ms)
        Ezz1 = Scross + np.einsum("ti,tj->tij", ms[1:], ms[:-1])
        # transition with intercept: [A a] = sum E[z_{t+1} [z_t;1]'] (sum E[[z_t;1][z_t;1]'])^-1
        P = np.zeros((k + 1, k + 1))
        P[:k, :k] = Ezz[:-1].sum(0); P[:k, k] = ms[:-1].sum(0); P[k, :k] = ms[:-1].sum(0); P[k, k] = T - 1
        Mx = np.zeros((k, k + 1))
        Mx[:, :k] = Ezz1.sum(0); Mx[:, k] = ms[1:].sum(0)
        Aa = Mx @ np.linalg.inv(P)
        A, a = Aa[:, :k], Aa[:, k]
        Qfull = (Ezz[1:].sum(0) - Aa @ Mx.T) / (T - 1)
        Q = np.diag(np.maximum(np.diag(Qfull), 1e-6))
        P2 = np.zeros((k + 1, k + 1))
        P2[:k, :k] = Ezz.sum(0); P2[:k, k] = ms.sum(0); P2[k, :k] = ms.sum(0); P2[k, k] = T
        My = np.zeros((N, k + 1))
        My[:, :k] = Y.T @ ms; My[:, k] = Y.sum(0)
        Cc = My @ np.linalg.inv(P2)
        C, c = Cc[:, :k], Cc[:, k]
        R = np.maximum((np.sum(Y ** 2, 0) - np.sum(Cc * My, 1)) / T, 1e-6)
        mu0, S0 = ms[0], Ss[0] + 1e-6 * np.eye(k)
    return dict(A=A, a=a, Q=Q, C=C, c=c, R=np.diag(R), mu0=mu0, S0=S0), len(lls), lls


def dec_kflatent(sp, seed=0, return_info=False):
    """KFlatent [paper]: LGDS with floor(N/3) latent states learned by EM, static map D by
    regression (with intercept) from the filtered means [paper, eq. 4], and a dynamic map
    by a second KF [paper, eq. 10]. EM runs on the training bins as one sequence."""
    k = sp.Rtr.shape[1] // 3
    p, n_ep, lls = lgds_em(sp.Rtr, k, seed=seed)
    Ztr = kalman_filter(p, sp.Rtr)
    Zte = kalman_filter(p, sp.Rte)
    D = ridge(Ztr[sp.oktr], sp.Xtr[sp.oktr])
    st_tr, st_te = apply(D, Ztr), apply(D, Zte)
    dyn = dynamic_map(sp, st_tr, st_te)
    if return_info:
        gain = (lls[-1] - lls[-2]) / (lls[-1] - lls[0])
        return st_te, dyn, dict(epochs=n_ep, k=k, ll_first=lls[0], ll_last=lls[-1], last_rel_gain=gain,
                                converged=n_ep < 100 or gain < 1e-4)
    return st_te, dyn


# ---------------------------------------------------------------- rEFH

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


class REFH:
    """Recurrent exponential-family harmonium [paper, eq. 5-8; code, RBM/EFH.m,
    RBM/setParams.m case 'spikecounts', RBM/setLearningSchedules.m 'exp',
    RBM/secondOrderWeightUpdate.m, RBM/dynamical/recurrentize.m].

    Visible units: Nhid recurrent Bernoulli units (the previous hidden means) and N
    Poisson spike-count units ('normal' gives the standard-normal variant of figure 8).
    Hidden units: floor(4 N) Bernoulli. CD1; mini-batches of the same time step of 40
    random subsequences of 1000 bins, a new batch each epoch; max(floor(Ntrain/250), 20)
    epochs; sparsity target 0.05, cost 0.2, running estimate rate 0.95 [code, DBNtrain.m];
    weights initialized N(0, 0.005^2), biases 0; second-order (momentum and decay)
    updates with exponentially growing masses, mw0 = mean(muR N, 0.09 Nhid) 10000/Ntrain
    (200 for standard-normal units), recurrent mass 110, bias masses 0.55 times weights.
    """

    def __init__(self, n_vis, units="poisson", ratio=4, seed=0):
        self.N = n_vis
        self.H = int(np.floor(n_vis * ratio))
        self.units = units
        self.rng = np.random.default_rng(seed)

    def vis_mean(self, eta):
        return np.exp(np.minimum(eta, 30)) if self.units == "poisson" else eta

    def vis_sample(self, mu):
        if self.units == "poisson":
            return self.rng.poisson(mu).astype(mu.dtype)
        return mu + self.rng.standard_normal(mu.shape, mu.dtype)

    def fit(self, Rtrain, T=1000, ncases=40):
        rng = self.rng
        N, H = self.N, self.H
        ntr = len(Rtrain)
        T = min(T, ntr)
        ncases = int(np.floor(40000 / T))
        nep = max(int(np.floor(ntr / 250)), 20)
        Ts = 0.01
        if self.units == "poisson":
            mw0 = np.mean([Rtrain.mean() * N, 0.09 * H]) * 10000 / ntr
        else:
            mw0 = 200.0
        mr0 = 110.0
        wt2b = 0.55
        m0 = dict(w=mw0, vb=mw0 * wt2b, hb=mw0 * wt2b, rw=mr0, rb=mr0 * wt2b)
        Nv = H + N
        f32 = np.float32  # single precision for speed [standard]
        W = (0.005 * rng.standard_normal((Nv, H))).astype(f32)
        bh = np.zeros(H, f32)
        bv = np.zeros(Nv, f32)
        Rtrain = Rtrain.astype(f32)
        Wd = np.zeros_like(W); bhd = np.zeros_like(bh); bvd = np.zeros_like(bv)
        cost, target, rate = 0.2, 0.05, 0.95
        est = None

        def masses(ep, key):
            m = 1.10 ** ep * m0[key] * Ts ** 2
            b = m0[key] / 2 * Ts
            k = m0[key] / 500000
            return m, b, k

        for ep in range(1, nep + 1):
            i0 = np.ceil((ntr - T) * rng.random(ncases)).astype(int)
            i0 = np.clip(i0, 0, ntr - T)
            batch = np.stack([Rtrain[i:i + T] for i in i0], 0)  # cases x T x N
            mw, bw, kw = masses(ep, "w")
            mrw, brw, krw = masses(ep, "rw")
            mvb, bvb, kvb = masses(ep, "vb")
            mrb, brb, krb = masses(ep, "rb")
            mhb, bhb, khb = masses(ep, "hb")
            # per-row coefficients of the second-order update (recurrent rows, then spike rows)
            rows = lambda r, s_: np.r_[np.full(H, r), np.full(N, s_)].astype(f32)
            cWk, cWd, cWu = (rows(-krw / (mrw / Ts), -kw / (mw / Ts))[:, None],
                             rows(0.98 - brw / (mrw / Ts), 0.98 - bw / (mw / Ts))[:, None],
                             rows(1 / (mrw / Ts), 1 / (mw / Ts))[:, None] / ncases)
            cvk, cvd, cvu = (cWk[:, 0], cWd[:, 0],
                             rows(1 / (mrb / Ts), 1 / (mvb / Ts)) / ncases)
            cvk = rows(-krb / (mrb / Ts), -kvb / (mvb / Ts))
            cvd = rows(0.98 - brb / (mrb / Ts), 0.98 - bvb / (mvb / Ts))
            mmh = mhb / Ts
            zprev = np.zeros((ncases, H), f32)
            for t in range(T):
                pv = np.hstack([zprev, batch[:, t, :]])
                ph = sigmoid(pv @ W + bh)
                zprev = ph
                hs = (ph > rng.random(ph.shape, f32)).astype(f32)
                eta = hs @ W.T + bv
                qv = np.empty_like(pv)
                rmean = sigmoid(eta[:, :H])
                qv[:, :H] = rmean > rng.random(rmean.shape, f32)
                qv[:, H:] = self.vis_sample(self.vis_mean(eta[:, H:]))
                qh = sigmoid(qv @ W + bh)
                pW = pv.T @ hs
                ph_s = hs.sum(0)
                pv_s = pv.sum(0)
                gW = pW - qv.T @ qh
                gbh = ph_s - qh.sum(0)
                gbv = pv_s - qv.sum(0)
                if est is None:
                    est = [pW.copy(), ph_s.copy(), pv_s.copy()]
                else:
                    est[0] *= (1 - rate); est[0] += rate * pW
                    est[1] = rate * ph_s + (1 - rate) * est[1]
                    est[2] = rate * pv_s + (1 - rate) * est[2]
                gW += cost * target * est[2][:, None]
                gW -= cost * est[0]
                gbh = gbh + cost * (ncases * target - est[1])
                # wdot <- -k/m w + (0.98 - b/m) wdot + u/m ;  w <- w + Ts wdot  [code]
                Wd *= cWd; Wd += cWk * W; Wd += cWu * gW
                W += Ts * Wd
                bhd = (-khb / mmh) * bh + (0.98 - bhb / mmh) * bhd + gbh / ncases / mmh
                bh = bh + Ts * bhd
                bvd = cvk * bv + cvd * bvd + cvu * gbv
                bv = bv + Ts * bvd
        self.W, self.bh, self.bv = W.astype(float), bh.astype(float), bv.astype(float)
        self.epochs = nep
        return self

    def features(self, R):
        """[code, testEFHBMI.m LDSobsfxn, updownRDBN.m] run the rEFH over one sequence
        with mean propagation; return updated spike-unit means, updated recurrent-unit
        means and hidden means."""
        H = self.H
        Z = np.empty((len(R), H))
        z = np.zeros(H)
        Wr, Ws = self.W[:H], self.W[H:]
        for t in range(len(R)):
            z = sigmoid(z @ Wr + R[t] @ Ws + self.bh)
            Z[t] = z
        Vs = self.vis_mean(Z @ Ws.T + self.bv[H:])
        Vr = sigmoid(Z @ Wr.T + self.bv[:H])
        return Vs, Vr, Z


def refh_decode(sp, model, Rtr, Rte, hidden_only=False):
    """[paper, eq. 9-10; code, filterDecoder.m] static ridge map from [updated visible
    means, hidden means] with penalty (Nunits/Nsamples)^(10/3) [claims: exponent reading
    of eq. 10; code], then a KF on the six static outputs. hidden_only drops the updated
    visible units (the figure 8 variant). Also returns the R2 of the static map on the
    training bins it was fitted on."""
    out = []
    for R in (Rtr, Rte):
        Vs, Vr, Z = model.features(R)
        out.append(Z if hidden_only else np.hstack([Vs, Vr, Z]))
    Ftr, Fte = out
    nv = Ftr.shape[1] + 1
    lam = (nv / sp.oktr.sum()) ** (10 / 3)
    B = ridge(Ftr[sp.oktr], sp.Xtr[sp.oktr], lam=lam)
    st_tr, st_te = apply(B, Ftr), apply(B, Fte)
    r2_tr = rsq(st_tr[sp.oktr], sp.Xtr[sp.oktr])
    return st_te, dynamic_map(sp, st_tr, st_te), r2_tr


def dec_refh(sp, seed=0, units="poisson", variants=False):
    """Train the rEFH on the training bins and decode. units 'normal' trains the
    standard-normal variant on transformed counts (see transform_counts)."""
    Rtr, Rte = sp.Rtr, sp.Rte
    if units == "normal":
        Rtr, Rte = transform_counts(Rtr, Rte, units_reading=variants or "standardize")
    model = REFH(Rtr.shape[1], units=units, seed=seed).fit(Rtr)
    res = {"refh": None, "refh_kf": None}
    res["refh"], res["refh_kf"], res["train_r2"] = refh_decode(sp, model, Rtr, Rte)
    if units == "poisson" and variants:
        res["refh_hid"], res["refh_hid_kf"], _ = refh_decode(sp, model, Rtr, Rte, hidden_only=True)
    res["epochs"] = model.epochs
    return res


def transform_counts(Rtr, Rte, units_reading="standardize"):
    """Inputs of the standard-normal rEFH. 'standardize' [paper, Results, Variant decoders:
    standardized counts], z-scored with the training mean and SD; 'anscombe' [code,
    getLatentsBMI.m] 2 sqrt(R + 3/8)."""
    if units_reading == "anscombe":
        return 2 * np.sqrt(Rtr + 3 / 8), 2 * np.sqrt(Rte + 3 / 8)
    mu, sd = Rtr.mean(0), Rtr.std(0)
    sd[sd == 0] = 1
    return (Rtr - mu) / sd, (Rte - mu) / sd


def run_all(sp, seed, decoders=DECODERS, info=None):
    """Fit the decoders on one split; returns test-set predictions per decoder. The
    stochastic fits (EM initialization, rEFH) take seeds derived from `seed`. A dict
    passed as `info` receives the EM run of KFlatent and the training R2 of the static
    rEFH map."""
    out = {}
    info = {} if info is None else info
    if "linear" in decoders:
        out["linear"] = dec_linear(sp)
    if "kfobs" in decoders:
        out["kfobs"] = dec_kfobs(sp)
    if "kflatent" in decoders or "kflatent_kf" in decoders:
        out["kflatent"], out["kflatent_kf"], info["kflatent"] = dec_kflatent(sp, seed=seed, return_info=True)
    if "wf" in decoders:
        out["wf"] = dec_wf(sp)
    if "ukf" in decoders:
        out["ukf"] = dec_ukf(sp)
    if "refh" in decoders or "refh_kf" in decoders:
        r = dec_refh(sp, seed=seed + 1)
        out["refh"], out["refh_kf"] = r["refh"], r["refh_kf"]
        info["refh_train_r2"] = r["train_r2"]
    return out


def prepare(d, bin_ms=64, reading="methods", train_s=320.0, fraction=1.0, test_start_s=None):
    """Bin, filter units [code, getLatentsBMI.m] and split. For f < 1 the first
    floor(f N) units in file order are kept after the rate filter [claims; code]."""
    R, X, _ = bin_data(d, bin_ms, reading)
    ntr = int(np.floor(train_s / (bin_ms / 1000.0)))
    keep = unit_filter(R, bin_ms, ntr)
    if fraction < 1:
        idx = np.where(keep)[0]
        keep[:] = False
        keep[idx[: int(np.floor(len(idx) * fraction))]] = True
    ts = train_s if test_start_s is None else test_start_s
    return Split(R[:, keep], X, bin_ms, train_s=train_s, test_start_s=ts)
