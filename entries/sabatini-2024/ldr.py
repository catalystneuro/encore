"""Loading and measures for testing Sabatini & Kaufman (2024) on DANDI:000070.

The paper reanalyses the maze-task sessions of Churchland et al. (2010, 2012):
two monkeys (J, N), one PMd and one M1 Utah array each, analysed as four
datasets (M1-J, PMd-J, M1-N, PMd-N). Its Data availability statement names the
two sessions read here (SESSIONS).

Where each parameter comes from is said beside it:
- "claims": the claims file's criterion or shared method (claims/sabatini-2024.yaml),
  which cites the paper or its code (github.com/kaufmanlab/LDR-public at b65f28d).
- "paper": a passage of the paper (author, step 1.6), cited.
- "code": the paper's code at b65f28d, where the claims file defers to it.
- "assumption": a choice the paper leaves open, with the reason.
- "standard": a detail that cannot change a result.
"""
import zlib
import numpy as np
import requests
import h5py
import remfile
from scipy.ndimage import gaussian_filter1d
from scipy import stats

DANDISET = "000070"
VERSION = "0.261122.2046"   # most recent published version; the paper cites none
API = "https://api.dandiarchive.org/api"
SESSIONS = {  # paper, Data availability
    "J": "sub-Jenkins/sub-Jenkins_ses-20090918_behavior+ecephys.nwb",
    "N": "sub-Nitschke/sub-Nitschke_ses-20100923_behavior+ecephys.nwb",
}
DATASETS = ["M1-J", "PMd-J", "M1-N", "PMd-N"]
PAPER_KEY = "sabatini-2024"

# Time base (claims, shared method): -350 to +850 ms around movement onset, 1 ms
# bins, down-sampled every 10 ms to 121 bins. Dynamics are fitted from bin 20
# (MATLAB index; 0-based 19, -160 ms on this grid) on.
PRE_MS, POST_MS = 350, 850
NT = 121
T0 = 19          # 0-based index of MATLAB bin 20
TIMES = np.arange(-PRE_MS, POST_MS + 1, 10)  # ms, 121 values


def seed(claim, k=0):
    """Seed of a claim's generator (protocol, author step 3); k adds 0, 1000, ..."""
    return zlib.crc32(f"{PAPER_KEY}/{claim}".encode()) + k


def rng(claim, k=0):
    return np.random.default_rng(seed(claim, k))


# --------------------------------------------------------------------- loading
def asset(path, version=VERSION):
    r = requests.get(f"{API}/dandisets/{DANDISET}/versions/{version}/assets/",
                     params={"path": path}, timeout=60)
    r.raise_for_status()
    res = [a for a in r.json()["results"] if a["path"] == path]
    return res[0]["asset_id"]


def open_nwb(path, version=VERSION):
    aid = asset(path, version)
    return h5py.File(remfile.File(f"{API}/assets/{aid}/download/"), "r")


def trial_table(h):
    t = h["intervals/trials"]
    cols = ["maze_condition", "task_success", "maze_num_targets", "maze_num_barriers",
            "go_cue_time", "target_presentation_time", "move_begins_time",
            "offline_move_onset_time", "start_time", "stop_time", "discard_trial",
            "correct_reach", "trial_version", "unhittable"]
    import pandas as pd
    d = pd.DataFrame({c: t[c][:] for c in cols})
    d["delay"] = d.go_cue_time - d.target_presentation_time
    return d


def select_trials(d, reading="all"):
    """The 72 conditions and the trials (claims, shared method).

    Conditions: maze conditions 1 to 108 without the multiples of 3 (reading a;
    in this file these are exactly the 3-target versions, reading b). Condition 0
    (no maze condition) is left out. Trials: successful (reading 'all') or
    successful with delay above 400 ms (reading 'delay400')."""
    m = (d.maze_condition > 0) & (d.maze_condition % 3 != 0) & (d.task_success == 1)
    if reading == "delay400":
        m &= d.delay > 0.4
    return m.values


def load_session(monkey, reading="all", onset="move_begins_time"):
    """Spike counts at 1 ms and hand position for the selected trials.

    Alignment on move_begins_time, the file's "movement onset time"
    (assumption: the paper says only "aligned to movement onset"); onset=
    "offline_move_onset_time" aligns on the file's offline estimate instead (the
    variant notebook 1 runs on a subset of the claims). Counts cover -355 to +855 ms so that both
    the smoothed grid (-350..850) and 10 ms count bins centred on it can be formed.
    Trials whose window runs past the end of the trial (spikes are stored within
    trials only) are dropped and counted."""
    h = open_nwb(SESSIONS[monkey])
    d = trial_table(h)
    sel = select_trials(d, reading).copy()
    on = d[onset].values
    sel &= np.isfinite(on)
    t0 = on - (PRE_MS + 5) / 1000
    t1 = on + (POST_MS + 5) / 1000
    covered = (t0 >= d.start_time.values) & (t1 <= d.stop_time.values)
    dropped = int((sel & ~covered).sum())
    sel &= covered
    idx = np.where(sel)[0]
    tr = d.iloc[idx].reset_index(drop=True)
    tr["trial_index"] = idx
    nb = PRE_MS + POST_MS + 11  # 1211 edges -> 1210 bins of 1 ms
    st_index = h["units/spike_times_index"][:]
    loc = h["general/extracellular_ephys/electrodes/location"][:].astype(str)
    uel = h["units/electrodes"][:]
    allsp = h["units/spike_times"][:]
    counts = np.zeros((len(idx), len(st_index), nb - 1), dtype=np.uint8)
    starts = np.r_[0, st_index[:-1]]
    for u in range(len(st_index)):
        sp = allsp[starts[u]:st_index[u]]
        i0 = np.searchsorted(sp, t0[idx])
        i1 = np.searchsorted(sp, t1[idx])
        for j in range(len(idx)):
            x = sp[i0[j]:i1[j]]
            if len(x):
                b = np.floor((x - t0[idx[j]]) * 1000).astype(int)
                b = b[(b >= 0) & (b < nb - 1)]
                np.add.at(counts[j, u], b, 1)
    del allsp
    # hand position, 1 kHz within trials (checked in the data check)
    hts = h["processing/behavior/Position/Hand/timestamps"]
    hd = h["processing/behavior/Position/Hand/data"]
    ts_all = hts[:]
    hand = np.zeros((len(idx), PRE_MS + POST_MS + 1, 2))
    grid = np.arange(-PRE_MS, POST_MS + 1) / 1000
    for j, k in enumerate(idx):
        a = np.searchsorted(ts_all, on[k] - 0.4)
        b = np.searchsorted(ts_all, on[k] + 0.9)
        x = hd[a:b]
        tt = ts_all[a:b]
        for c in range(2):
            hand[j, :, c] = np.interp(on[k] + grid, tt, x[:, c])
    del ts_all
    region = np.array(["PMd" if "Pre-Motor" in loc[e] else "M1" for e in uel])
    conds = np.sort(tr.maze_condition.unique())
    cond_index = np.searchsorted(conds, tr.maze_condition.values)
    h.close()
    return dict(monkey=monkey, trials=tr, counts=counts, hand=hand, region=region,
                conds=conds, cond=cond_index, dropped_uncovered=dropped,
                n_trials_file=len(d), table=d)


# --------------------------------------------------------------- preprocessing
def smooth(counts):
    """Claims, shared method; code preprocessTrials.m: 1 ms counts x 1000, Gaussian
    s.d. 20 ms over 111 taps (truncate 55/20), symmetric padding ('reflect' in
    scipy equals MATLAB 'symmetric'), every 10th sample. counts: (..., 1210) from
    -355 ms; the smoothed grid is -350..850 (bins 5..1205)."""
    x = counts[..., 5:5 + PRE_MS + POST_MS + 1].astype(np.float32) * 1000
    y = gaussian_filter1d(x, 20, axis=-1, mode="reflect", truncate=55 / 20)
    return y[..., ::10]


def smooth_trials(counts, chunk=200):
    out = np.zeros(counts.shape[:2] + (NT,), np.float32)
    for i in range(0, counts.shape[0], chunk):
        out[i:i + chunk] = smooth(counts[i:i + chunk])
    return out


def binned_counts(counts):
    """Code kinFromTBFSingleTrial / Methods, LDR-based decoding (claims): 1 ms counts
    summed in 10 ms bins centred on the grid times, scaled to spikes/s."""
    c = counts[..., :NT * 10].astype(np.float32)
    return c.reshape(c.shape[:-1] + (NT, 10)).sum(-1) * 100


def cond_average(trials_x, cond, n_cond=72):
    return np.stack([trials_x[cond == c].mean(0) for c in range(n_cond)])


def split_halves(cond, g, ratio=0.5):
    """Code cvConds.m: per condition, trials permuted and the first round(n*ratio)
    assigned to the first partition."""
    a = np.zeros(len(cond), bool)
    for c in np.unique(cond):
        ii = np.where(cond == c)[0]
        ii = ii[g.permutation(len(ii))]
        a[ii[: int(np.floor(len(ii) * ratio + 0.5))]] = True
    return a


# -------------------------------------------------------------------- measures
def var_explained(X, Xhat, clip=True):
    """Code getVarExplained.m ('ind'): per condition, 1 - summed variance over
    neurons of the residual over time / summed variance of the data, over the
    bins where Xhat is not NaN; negatives set to 0. X, Xhat: (C, N, T)."""
    ok = ~np.isnan(Xhat[0, 0])
    r = X[..., ok] - Xhat[..., ok]
    ve = 1 - r.var(-1, ddof=1).sum(-1) / X[..., ok].var(-1, ddof=1).sum(-1)
    return np.clip(ve, 0, None) if clip else ve


def alignment_index(D, S):
    """Code getAlignmentIndex.m: fraction of the variance of D (N x T) captured by
    projection onto span(S) (N x d), negatives 0."""
    ok = ~np.isnan(D[0])
    D = D[:, ok]
    P = S @ np.linalg.pinv(S)
    r = D - P @ D
    a = 1 - r.var(1, ddof=1).sum() / D.var(1, ddof=1).sum()
    return max(a, 0.0)


def bio_eigs(e):
    """Code bioEigs.m: |eigenvalue| capped at 0.9993 (half-life 10 s at 100 Hz; paper,
    Methods, Fitting dynamics to single conditions)."""
    e = e.copy()
    big = np.abs(e) > 0.9993
    e[big] = 0.9993 * e[big] / np.abs(e[big])
    return e


def freq_hz(e):
    """Code extractParams.m: angle / 2 pi x 100 Hz."""
    return 100 * np.abs(np.angle(e)) / (2 * np.pi)


def get_basis(X, k):
    """Code getBasisFxns.m: SVD of the (neurons x conditions)-by-time matrix of the
    unnormalised rates (claims); returns basis (T x k) and loadings (C, N, k)."""
    C, N, T = X.shape
    _, _, Vt = np.linalg.svd(X.reshape(C * N, T), full_matrices=False)
    B = Vt[:k].T
    L = X @ np.linalg.pinv(B.T)
    return B, L


def pair_ids(e):
    """Group eigenvalues into conjugate pairs and real modes; sorted by frequency
    (code pairID.m groups by real part and |imag|)."""
    key = np.round(np.real(e), 10) + 1j * np.round(np.abs(np.imag(e)), 10)
    uniq = []
    ids = np.zeros(len(e), int)
    for i, kk in enumerate(key):
        for j, u in enumerate(uniq):
            if abs(u - kk) < 1e-8:
                ids[i] = j
                break
        else:
            uniq.append(kk)
            ids[i] = len(uniq) - 1
    return ids


def eig_transform(X, k):
    """Code eigTransform.m (claims, shared method): de-mix the raw SVD basis by an
    LDS fitted from bin 20 on, replace the basis by damped sinusoids of the fitted
    frequencies and half-lives (NaN before bin 20), and correct the loadings."""
    C, N, T = X.shape
    Braw, L = get_basis(X, k)
    A = Braw[T0 + 1:].T @ np.linalg.pinv(Braw[T0:-1].T)
    e = np.linalg.eigvals(A)
    e = bio_eigs(e)
    e = e[np.argsort(np.abs(np.angle(e)) / (2 * np.pi), kind="stable")]
    # within a conjugate pair put the positive-imaginary one first
    ids = pair_ids(e)
    Bsim = Braw.copy()
    for t in range(T0 + 1, T - 20):  # code: for t = 21:(T-20)
        Bsim[t] = A @ Bsim[t - 1]
    ff = np.zeros((k, 3))
    for el in np.unique(ids):
        inds = np.where(ids == el)[0]
        ue = e[inds[0]]
        if np.imag(ue) < 0:
            ue = np.conj(ue)
        f = np.angle(ue) / (2 * np.pi)
        tau = -np.log(np.abs(ue))
        ff[inds[0]] = [f, 0, tau]
        if len(inds) == 2:
            ff[inds[1]] = [f, -np.pi / 2, tau]
    ts = np.r_[np.full(T0, np.nan), np.arange(T - T0)]
    Bp = np.zeros((T, k))
    for c in range(k):
        Bp[:, c] = np.exp(-ff[c, 2] * ts) * np.cos(2 * np.pi * ff[c, 0] * ts + ff[c, 1])
    corr = np.linalg.pinv(Bsim[T0:]) @ Bp[T0:]
    Lc = L @ np.linalg.pinv(corr.T)
    raw = (corr.T @ Braw.T).T
    return dict(B=Bp, L=Lc, ids=ids, eig=e, freq=100 * ff[:, 0], halflife=np.where(
        ff[:, 2] > 0, np.log(2) / np.maximum(ff[:, 2], 1e-12) / 100, np.inf),
        Braw=Braw, Lraw=L, raw=raw, corr=corr)


def groups(tbf):
    """Rotation groups (pairs) and the offset (a real mode at zero frequency), by
    frequency; returns list of (freq, column indices)."""
    out = []
    for el in np.unique(tbf["ids"]):
        inds = np.where(tbf["ids"] == el)[0]
        out.append((float(tbf["freq"][inds[0]]), inds))
    return sorted(out, key=lambda x: x[0])


def reconstruct(L, B):
    return L @ B.T


def cv_tbf_k(Xtr, cond, g, folds=100, kmax=20, ratio=0.5):
    """Code crossValidateDimensionalityBasisFxns.m (claims): halves of trials,
    basis and loadings from one half, mean held-out variance explained per k;
    an even best k raised by one."""
    loss = np.zeros((kmax, folds))
    for f in range(folds):
        a = split_halves(cond, g, ratio)
        Xa = cond_average(Xtr[a], cond[a])
        Xb = cond_average(Xtr[~a], cond[~a])
        C, N, T = Xa.shape
        _, _, Vt = np.linalg.svd(Xa.reshape(C * N, T), full_matrices=False)
        for k in range(1, kmax + 1):
            B = Vt[:k].T
            loss[k - 1, f] = var_explained(Xb, (Xa @ B) @ B.T).mean()
    m = loss.mean(1)
    best = int(np.argmax(m)) + 1
    chosen = best + 1 if best % 2 == 0 else best
    return dict(loss=loss, mean=m, best=best, k=chosen)


# ----------------------------------------------------- single-condition LDS
def lds_fit(Xc, k, cap=True):
    """Code idDynamics.m: least-squares dynamics from bin 20 on, reduced to rank k
    by the top k left singular vectors of A X (reduced-rank regression); simulated
    forward from the state at bin 20. Eigenvalues capped at 10 s half-life
    (paper, Methods), also in the simulation (cap=True; the code caps only the
    reported eigenvalues). Returns eigenvalues sorted by frequency and the
    simulation (NaN before bin 20)."""
    X1 = Xc[:, T0:-1]
    X2 = Xc[:, T0 + 1:]
    A = X2 @ np.linalg.pinv(X1)
    U, _, _ = np.linalg.svd(A @ Xc[:, T0:], full_matrices=False)
    U = U[:, :k]
    Ak = U.T @ A @ U
    w, V = np.linalg.eig(Ak)
    if cap:
        wc = bio_eigs(w)
        if np.any(wc != w):
            Ak = np.real(V @ np.diag(wc) @ np.linalg.inv(V))
        w = wc
    else:
        w = bio_eigs(w)
    w = w[np.argsort(np.abs(np.angle(w)), kind="stable")]
    sim = np.full_like(Xc, np.nan)
    sim[:, T0] = Xc[:, T0]
    z = U.T @ A @ Xc[:, T0]
    for t in range(T0 + 1, Xc.shape[1]):
        sim[:, t] = U @ z
        z = Ak @ z
    return w, sim


def lds_eigs(Xc, k):
    X1 = Xc[:, T0:-1]
    X2 = Xc[:, T0 + 1:]
    A = X2 @ np.linalg.pinv(X1)
    U, _, _ = np.linalg.svd(A @ Xc[:, T0:], full_matrices=False)
    U = U[:, :k]
    w = bio_eigs(np.linalg.eigvals(U.T @ A @ U))
    return w[np.argsort(np.abs(np.angle(w)), kind="stable")]


def sort_eigs(w):
    """Eigenvalues sorted by |frequency|, then the member of a pair with positive
    imaginary part first (correspondence between conditions)."""
    order = np.lexsort((-np.imag(w), np.round(np.abs(np.angle(w)), 8)))
    return w[order]


# ---------------------------------------------------------------------- jPCA
def skew_regress(dX, X):
    """Least-squares skew-symmetric M with dX ~ X M (jPCA codepack skewSymRegress)."""
    k = X.shape[1]
    iu = np.triu_indices(k, 1)
    H = np.zeros((k * k, len(iu[0])))
    for n, (i, j) in enumerate(zip(*iu)):
        Mm = np.zeros((k, k))
        Mm[i, j] = 1
        Mm[j, i] = -1
        H[:, n] = Mm.flatten(order="F")
    Xbig = np.kron(np.eye(k), X)
    p = np.linalg.lstsq(Xbig @ H, dX.flatten(order="F"), rcond=None)[0]
    return (H @ p).reshape(k, k, order="F")


def jpca(A_list, num_pcs=6, soften=10, mean_sub=True):
    """jPCA (Churchland et al. 2012 codepack, default parameters: 6 PCs, soft
    normalisation range+10, mean subtraction across conditions), on a list of
    (T x N) matrices. Returns the planes in high-d space (N x num_pcs, ordered
    by plane) and R2 of the skew-symmetric and unconstrained fits in the top plane."""
    A = np.stack(A_list)  # C x T x N
    if soften is not None:
        rng_ = A.reshape(-1, A.shape[-1]).max(0) - A.reshape(-1, A.shape[-1]).min(0)
        A = A / (rng_ + soften)
    if mean_sub:
        A = A - A.mean(0, keepdims=True)
    big = A.reshape(-1, A.shape[-1])
    mu = big.mean(0)
    _, _, Vt = np.linalg.svd(big - mu, full_matrices=False)
    P = Vt[:num_pcs].T
    red = (A - mu) @ P  # C x T x k
    pre = red[:, :-1].reshape(-1, num_pcs)
    dst = (red[:, 1:] - red[:, :-1]).reshape(-1, num_pcs)
    Mbest = np.linalg.lstsq(pre, dst, rcond=None)[0]
    Mskew = skew_regress(dst, pre)
    w, V = np.linalg.eig(Mskew)
    order = np.argsort(-np.abs(np.imag(w)), kind="stable")
    planes = []
    used = set()
    for i in order:
        if i in used or np.imag(w[i]) <= 0:
            continue
        v = V[:, i]
        j1, j2 = np.real(v), -np.imag(v)  # codepack: [v1+v2, (v1-v2)i] of the conjugate pair
        j1 /= np.linalg.norm(j1)
        j2 /= np.linalg.norm(j2)
        planes.append(np.c_[j1, j2])
        used.add(i)
    J = np.concatenate(planes, 1)
    J2 = J[:, :2]
    def r2(M):
        d2 = dst @ J2
        f2 = (pre @ M) @ J2
        return 1 - ((d2 - f2) ** 2).sum() / ((d2 - d2.mean(0)) ** 2).sum()
    return dict(jPCs_highD=P @ J, R2_Mskew_2D=r2(Mskew), R2_Mbest_2D=r2(Mbest),
                Mskew=Mskew, P=P, J=J)


def get_rotations(L, B, plane_num, conds=None):
    """Code getRotations.m (claims): activity reconstructed from the basis,
    mean-subtracted over conditions, soft-normalised by range + 5, jPCA on bins
    20 to 40 (0-based 19..39); the retained planes reconstruct the activity."""
    Xr = L @ B.T  # NaN before bin 20, as the code's de-mixed basis
    if conds is not None:
        Xr = Xr[conds]
    mean = Xr.mean(0)
    Ac = np.transpose(Xr - mean, (0, 2, 1))  # C x T x N
    flat = Ac.reshape(-1, Ac.shape[-1])
    sn = 1 / (np.nanmax(flat, 0) - np.nanmin(flat, 0) + 5)
    use = [a[T0:40] * sn for a in Ac]
    jp = jpca(use)
    J = jp["jPCs_highD"][:, :2 * plane_num]
    Xn = (Xr - mean) * sn[None, :, None]
    rot = np.einsum("nk,cnt->ckt", J, Xn)
    recon = np.einsum("nk,ckt->cnt", J, rot) / sn[None, :, None]
    ve = var_explained(Xr, recon)          # code: reconstruction without the mean
    ve_with_mean = var_explained(Xr, recon + mean)   # variant
    return dict(jp=jp, rot=rot, recon=recon, ve=ve, ve_with_mean=ve_with_mean, sn=sn, mean=mean, Xr=Xr)


# ---------------------------------------------------------------- statistics
def auc_folded(a, b):
    """ROC-AUC of two samples (Mann-Whitney U / n1 n2), folded to >= 0.5 (code
    compareTrialSimilarity.m)."""
    u = stats.mannwhitneyu(a, b).statistic
    auc = u / (len(a) * len(b))
    return 0.5 + abs(auc - 0.5), auc


def ridge(X, Y, lam, intercept=True):
    """Ridge regression Y ~ X W (+ b), lambda on W only."""
    if intercept:
        mx, my = X.mean(0), Y.mean(0)
        Xc, Yc = X - mx, Y - my
    else:
        mx = np.zeros(X.shape[1]); my = np.zeros(Y.shape[1]); Xc, Yc = X, Y
    W = np.linalg.solve(Xc.T @ Xc + lam * np.eye(X.shape[1]), Xc.T @ Yc)
    return lambda Z: (Z - mx) @ W + my


def kernel_ou(A, B, ls):
    d = np.sqrt(((A[:, None, :] - B[None, :, :]) ** 2).sum(-1))
    return np.exp(-d / ls)


def kernel_gauss(A, B, ls):
    d2 = ((A[:, None, :] - B[None, :, :]) ** 2).sum(-1)
    return np.exp(-d2 / (2 * ls ** 2))


def kernel_ridge(X, Y, kern, lam):
    """Kernel ridge regression (centred targets); lam = 0 uses the pseudo-inverse."""
    my = Y.mean(0)
    K = kern(X, X)
    if lam > 0:
        alpha = np.linalg.solve(K + lam * np.eye(len(K)), Y - my)
    else:
        alpha = np.linalg.pinv(K) @ (Y - my)
    return lambda Z: kern(Z, X) @ alpha + my


def folds_over(n, k, g):
    p = g.permutation(n)
    return [np.sort(p[i::k]) for i in range(k)]


# ------------------------------------------------------------- datasets
def build(reading="all", monkeys=("J", "N"), onset="move_begins_time"):
    """Load both sessions and form the four datasets: smoothed single trials
    (trials x units x 121), condition averages (72 x units x 121), 1 ms counts,
    hand position (start-subtracted, mm) and condition means of the hand."""
    out = {}
    for m in monkeys:
        S = load_session(m, reading, onset)
        sm = smooth_trials(S["counts"])
        hand = S["hand"] - S["hand"][:, :1, :]   # assumption: position relative to the start
        hand10 = hand[:, ::10]
        kin = np.stack([hand10[S["cond"] == c].mean(0) for c in range(72)])  # 72 x 121 x 2
        for reg in ("M1", "PMd"):
            u = S["region"] == reg
            name = f"{reg}-{m}"
            Xt = sm[:, u]
            out[name] = dict(name=name, monkey=m, region=reg, units=np.where(u)[0],
                             Xt=Xt, X=cond_average(Xt, S["cond"]), cond=S["cond"],
                             counts=S["counts"][:, u], hand10=hand10, kin=kin,
                             trials=S["trials"], conds=S["conds"],
                             dropped=S["dropped_uncovered"], n_trials_file=S["n_trials_file"],
                             table=S["table"])
        del sm
    return out


# ------------------------------------------------------------- kinematics
def kin_basis(kins, reading="svd"):
    """Kinematic basis functions (paper, Methods, Extracting kinematic basis
    functions): SVD of the x and y hand velocity of all conditions of all datasets;
    the top two velocity singular vectors, integrated to position. Reading 'svd'
    uses the raw vectors; reading 'skewnormal' fits a skew-normal curve to the first
    and the derivative of a skew-normal to the second, integrated analytically.
    kins: list of (72 x 121 x 2) condition-mean positions (mm). Returns position
    basis (121 x 2), velocity basis (121 x 2, per 10 ms)."""
    V = np.concatenate([np.gradient(k, axis=1).transpose(0, 2, 1).reshape(-1, NT) for k in kins])
    _, _, Vt = np.linalg.svd(V, full_matrices=False)
    v = Vt[:2].T.copy()
    for i in range(2):  # sign: first positive at its peak, second positive first lobe
        j = np.argmax(np.abs(v[:, i])) if i == 0 else np.argmax(np.abs(v[:, i]) > 0.5 * np.abs(v[:, i]).max())
        v[:, i] *= np.sign(v[j, i])
    if reading == "skewnormal":
        from scipy.optimize import curve_fit
        t = TIMES.astype(float)
        f1 = lambda t, a, al, lo, sc: a * stats.skewnorm.pdf(t, al, lo, sc)
        p1, _ = curve_fit(f1, t, v[:, 0], p0=[v[:, 0].max() * 200, 2, 100, 200], maxfev=20000)
        def f2(t, a, al, lo, sc):
            h = 1e-3 * sc
            return a * (stats.skewnorm.pdf(t + h, al, lo, sc) - stats.skewnorm.pdf(t - h, al, lo, sc)) / (2 * h)
        best = None
        for s0 in (1, -1):
            try:
                p2, _ = curve_fit(f2, t, v[:, 1], p0=[s0 * 1e4, 2, 150, 150], maxfev=20000)
                err = ((f2(t, *p2) - v[:, 1]) ** 2).sum()
                if best is None or err < best[1]:
                    best = (p2, err)
            except RuntimeError:
                pass
        p2 = best[0]
        vel = np.c_[f1(t, *p1), f2(t, *p2)]
        # velocity is per 10 ms bin and the pdf per ms, so the integral over bins is 1/10 of it
        pos = np.c_[p1[0] * stats.skewnorm.cdf(t, *p1[1:]), p2[0] * stats.skewnorm.pdf(t, *p2[1:])] / 10
        return pos - pos[0], vel, dict(p1=p1, p2=p2, raw=v)
    pos = np.cumsum(v, 0)
    pos -= pos[0]
    return pos, v, dict(raw=v)


def reach_params(pos_basis, kin):
    """Code predictDataUsingTBFandKinCondStructure.m: pinv(kinFxns) * [X Y] per
    condition; returned as [x b1, y b1, x b2, y b2] (code getCorrelationsWithFrequency
    labels: x-extent, y-extent, x-curve, y-curve). kin: (..., 121, 2)."""
    P = np.linalg.pinv(pos_basis) @ kin  # (..., 2 basis, 2 axis)
    return P.reshape(P.shape[:-2] + (4,))


def params_to_path(pos_basis, p):
    P = p.reshape(p.shape[:-1] + (2, 2))
    return pos_basis @ P


# --------------------------------------------------------- subspace angles
def principal(F, G):
    """Principal angles between span(F) and span(G) (as subspacea.m), ascending,
    with the bases U (in F) and V (in G) that realise them."""
    QF, _ = np.linalg.qr(F)
    QG, _ = np.linalg.qr(G)
    Y, s, Zt = np.linalg.svd(QF.T @ QG, full_matrices=False)
    s = np.clip(s, -1, 1)
    return np.arccos(s), QF @ Y, QG @ Zt.T


def sea(Xs, n_angles=25):
    """Subspace excursion angles (code subspaceExcursionAngles.m with maxTol 0):
    seed with the pair of subspaces at the largest principal angle, add the vector of
    the subspace at the largest angle to the augmented seed, repeat; of the tied
    sequences (the seed pair in both orders) the one with the largest summed angles.
    Xs: (nSubs, nDims, nVecs). Returns angles in degrees."""
    n = len(Xs)
    nv = Xs.shape[2]
    n_angles = min(n_angles, nv * n - 1)
    Q = [np.linalg.qr(x)[0] for x in Xs]
    first = np.zeros((n, n))
    for i in range(n - 1):
        for j in range(i + 1, n):
            s = np.linalg.svd(Q[i].T @ Q[j], compute_uv=False)
            first[i, j] = first[j, i] = np.arccos(np.clip(s.min(), -1, 1))
    i, j = np.unravel_index(np.argmax(first), first.shape)
    best = None
    for a, b in ((i, j), (j, i)):
        th, U, V = principal(Xs[a], Xs[b])
        S = np.c_[U, V[:, -1]]
        angs = [first[a, b]]
        for _ in range(1, n_angles):
            QS = np.linalg.qr(S)[0]
            vals = np.zeros(n)
            for m in range(n):
                s = np.linalg.svd(QS.T @ Q[m], compute_uv=False)
                vals[m] = np.arccos(np.clip(s.min(), -1, 1))
            m = int(np.argmax(vals))
            _, _, V = principal(S, Xs[m])
            S = np.c_[S, V[:, -1]]
            angs.append(vals[m])
        if best is None or sum(angs) > sum(best):
            best = angs
    return np.degrees(best)


def pca_dims(cols):
    """PCs to 80% of the variance and participation ratio of the rows' covariance;
    cols: (observations, N)."""
    c = cols - cols.mean(0)
    lam = np.linalg.svd(c, compute_uv=False) ** 2
    frac = np.cumsum(lam) / lam.sum()
    return int(np.searchsorted(frac, 0.8) + 1), float(lam.sum() ** 2 / (lam ** 2).sum())


def circ_corr(a, b):
    """Circular correlation (Jammalamadaka & SenGupta) with its normal-approximation p."""
    from scipy.stats import circmean
    sa, sb = np.sin(a - circmean(a)), np.sin(b - circmean(b))
    r = (sa * sb).sum() / np.sqrt((sa ** 2).sum() * (sb ** 2).sum())
    n = len(a)
    l20, l02, l22 = (sa ** 2).mean(), (sb ** 2).mean(), (sa ** 2 * sb ** 2).mean()
    z = r * np.sqrt(n * l20 * l02 / l22)
    return r, 2 * stats.norm.sf(abs(z))


def lds_batch(X, ks):
    """lds_fit/lds_eigs for all conditions at once (X: C x N x T): the least-squares
    dynamics A, the subspace U of A X from bin 20 on, and for each k the
    eigenvalues (capped) and the simulation from bin 20 (NaN before)."""
    W = X[:, :, T0:]
    A = X[:, :, T0 + 1:] @ np.linalg.pinv(X[:, :, T0:-1])
    U = np.linalg.svd(A @ W, full_matrices=False)[0]
    out = {}
    for k in ks:
        Uk = U[:, :, :k]
        Ak = np.transpose(Uk, (0, 2, 1)) @ A @ Uk
        w, V = np.linalg.eig(Ak)
        wc = bio_eigs(w.ravel()).reshape(w.shape)
        capped = np.any(wc != w, axis=1)
        if capped.any():
            Ak = Ak.copy()
            for c in np.where(capped)[0]:
                Ak[c] = np.real(V[c] @ np.diag(wc[c]) @ np.linalg.inv(V[c]))
        z = np.einsum("cnk,cnm,cm->ck", Uk, A, W[:, :, 0])
        sim = np.full(X.shape, np.nan)
        sim[:, :, T0] = W[:, :, 0]
        for t in range(T0 + 1, X.shape[2]):
            sim[:, :, t] = np.einsum("cnk,ck->cn", Uk, z)
            z = np.einsum("cij,cj->ci", Ak, z)
        out[k] = (np.stack([sort_eigs(e) for e in wc]), sim)
    return out


def lds_eigs_batch(X, k):
    W = X[:, :, T0:]
    A = X[:, :, T0 + 1:] @ np.linalg.pinv(X[:, :, T0:-1])
    U = np.linalg.svd(A @ W, full_matrices=False)[0][:, :, :k]
    w = np.linalg.eigvals(np.transpose(U, (0, 2, 1)) @ A @ U)
    w = bio_eigs(w.ravel()).reshape(w.shape)
    return np.stack([sort_eigs(e) for e in w])
