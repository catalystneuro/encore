"""Loading, statistical atlas and identification for the NeuroPAL heads of dandiset 000715.

Yemini, Lin, Nejatbakhsh et al. (2021), Cell 184:272-288, doi:10.1016/j.cell.2020.12.012.
Method references are to the paper's Methods S1 ("MS1", semi-automated identification) and
Methods S2 ("MS2", optimal coloring), and to the code the paper links:
CELL_ID (github.com/amin-nejat/CELL_ID at d9f5df92d1bc218d0b8b105e3cd880c8bba30764) and
Optimal_Coloring (github.com/Eviatar/Optimal_Coloring at 990c597d1a7b0c38c4e7e99f8e8b60da411b3493).

Each NWB file holds one worm head: a 5-channel volume (x, y, z, channel) and a table of hand
annotated neurons, one voxel per neuron (its centre) with its name. Files are streamed from the
archive at the pinned version; nothing is written to disk.

Where the parameters come from:

- Colors (MS1 Figure 6.2 legend): the median of the z-scored image in a 1.5 x 1.5 x 0.75 um patch
  centred on the neuron. CELL_ID implements it as a patch of half size [3, 3, 0] voxels
  (Neurons/Image.m, `patch_hsize`) of the volume z-scored per channel over all voxels
  (Preprocess.zscore_frame). Features are position in um and the R, G, B landmark colors
  (mNeptune2.5, CyOFP1, mTagBFP2), as in CELL_ID AutoId.id (`colors(:,[1 2 3])`).
- Atlas (MS1 Algorithm 4, equations 4.13 and 4.14): means and block-diagonal covariances
  (position and color blocks, equation 4.1), alternated with an affine alignment of each worm
  (equations 4.15 and 4.16). The alignment is solved in closed form as one weighted regression on
  [y, 1] (CELL_ID AutoId.MCR_solver with no ridge), which is the fixed point of the coordinate
  descent of Algorithm 3. The initial worm is drawn with a fixed seed (the claims file's standard
  choice). Assumption: Algorithm 4 as written does not converge on these data (the atlas shrinks
  along its minor axes at every alternation), so the atlas is kept in the initial worm's frame
  (`gauge`) and the alternations stop at `ATLAS_ITER`; the tolerance 1e-6 is kept but never
  reached. The notebook shows the results without the gauge and at other numbers of
  alternations. Neurons missing from a worm are left out of that worm's
  alignment and of the moments; the moments are normalised by the number of worms holding the
  neuron (the claims file's equation 4.14 divides by m, which assumes every worm holds every
  neuron). `RIDGE` is added to every covariance so that neurons seen in few worms have an
  invertible covariance: a standard choice, not from the paper.
- Identification (MS1 Algorithm 5): alignment initialised at the identity, alternated with the
  Hungarian assignment on Mahalanobis distances (equation 4.18) until the transform changes by
  less than the tolerance; the log likelihoods are equation 5.4. Probabilities are the Sinkhorn
  iterations of Algorithm 6, 500 iterations (CELL_ID AutoId.iter_sinkhorn), square-padded as
  CELL_ID sinkhorn_logspace does. The CELL_ID variant (`code_alignment`) follows
  AutoId.global_alignment and AutoId.local_alignment: principal-axis alignment, rotations theta
  = 0:0.25:2*pi about the major axis with both signs, 10 alternations of assignment and
  regression (color ridge 1e5 towards the identity), mirror solutions rejected, lowest
  assignment cost kept.
- Annotation (MS1 section 6.5; CELL_ID AutoId.update_log_likelihood): an annotated neuron's row
  is set to -1e9 except its true identity, set to 1e5; the assignment and the Sinkhorn matrix are
  recomputed without re-alignment.
- Adjacency (MS2 section 2; Optimal_Coloring computeProbAdjacency.m): 1000 samples per neuron
  from its positional Gaussian, the 95% closest by Mahalanobis distance kept; neurons i and j
  are adjacent when one of i's points is closer to j's centre (in j's metric) than to i's in
  i's metric. The seed is fixed (numpy cannot reproduce MATLAB's rng(1)).
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
import requests
from scipy.optimize import linear_sum_assignment
from scipy.special import logsumexp

DANDISET_ID = "000715"
DANDISET_VERSION = "0.241009.1514"
API = "https://api.dandiarchive.org/api"

PATCH_HALF = (3, 3, 0)        # CELL_ID patch_hsize, about 1.5 x 1.5 x 0.75 um (MS1 Fig 6.2)
TOL = 1e-6                    # convergence tolerance (claims file, standard choice)
MAX_ITER = 300                # cap on the alternations of Algorithm 5; convergence is reported
ATLAS_ITER = 20               # Algorithm 4 alternations; its tolerance is never reached (assumption,
                              # see the notebook)
RIDGE = 1e-2                  # added to each covariance diagonal; standard choice
SINKHORN_ITER = 500           # CELL_ID AutoId.iter_sinkhorn
MIN_LL, MAX_LL = -1e9, 1e5    # CELL_ID AutoId.min/max_log_likelihood
THETAS = np.arange(0, 2 * np.pi + 1e-9, 0.25)   # CELL_ID AutoId.theta
ITER_RWC = 10                 # CELL_ID AutoId.iter_rwc
COLOR_RIDGE = 1e5             # CELL_ID local_alignment, MCR_solver lambda for colors


# ---------------------------------------------------------------- loading

def list_assets(version: str = DANDISET_VERSION) -> list[dict]:
    r = requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/",
                     params={"page_size": 200}, timeout=60)
    r.raise_for_status()
    out = [{"path": a["path"], "asset_id": a["asset_id"], "size": a["size"],
            "url": f"{API}/assets/{a['asset_id']}/download/"} for a in r.json()["results"]]
    return sorted(out, key=lambda a: a["path"])


def _decode(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def zscore_colors(image: np.ndarray, vox: np.ndarray, channels, half=PATCH_HALF) -> np.ndarray:
    """Median of the per-channel z-scored image in a patch around each voxel (CELL_ID subcube)."""
    out = np.full((len(vox), len(channels)), np.nan)
    sz = image.shape[:3]
    for c_i, ch in enumerate(channels):
        data = image[..., ch].astype(np.float64)
        z = (data - data.mean()) / data.std(ddof=1)
        for k, p in enumerate(vox):
            lo = [max(int(p[a]) - half[a], 0) for a in range(3)]
            hi = [min(int(p[a]) + half[a], sz[a] - 1) + 1 for a in range(3)]
            out[k, c_i] = np.median(z[lo[0]:hi[0], lo[1]:hi[1], lo[2]:hi[2]])
    return out


def load_worm(asset: dict, with_image: bool = True, voxel_offset: int = 0) -> dict:
    """Read one file: metadata, annotated neurons, and their colors from the image.

    `voxel_offset` is added to the stored voxel indices before the color readout (the data
    check compares 0 and -1, as the files do not say whether the indices are 0- or 1-based).
    """
    f = h5py.File(remfile.File(asset["url"]), "r")
    g = lambda p: f[p][()]
    seg = f["processing/NeuroPAL/NeuroPALSegmentation/NeuroPALNeurons"]
    chars = [_decode(c) for c in seg["ID_labels"][:]]
    idx = seg["ID_labels_index"][:]
    starts = np.r_[0, idx[:-1]]
    labels = ["".join(chars[s:e]) for s, e in zip(starts, idx)]
    vm = seg["voxel_mask"][:]
    vmi = seg["voxel_mask_index"][:]
    vox = np.stack([vm["x"], vm["y"], vm["z"]], axis=1).astype(int)
    imv = "general/optophysiology/NeuroPALImVol/"
    grid = g(imv + "grid_spacing").astype(float)
    rgbw = g("acquisition/NeuroPALImageRaw/RGBW_channels").astype(int)
    w = {
        "path": asset["path"], "subject": _decode(g("general/subject/subject_id")),
        "strain": _decode(g("general/subject/strain")),
        "subject_description": _decode(g("general/subject/description")),
        "growth_stage": _decode(g("general/subject/growth_stage")),
        "date_of_birth": _decode(g("general/subject/date_of_birth")),
        "session_start": _decode(g("session_start_time")),
        "location": _decode(g(imv + "location")),
        "device": list(f["general/devices"].keys()),
        "channels": [_decode(c) for c in g(imv + "order_optical_channels/channels")],
        "grid": grid, "rgbw": rgbw, "labels": labels, "vox": vox,
        "voxels_per_roi": np.unique(np.diff(np.r_[0, vmi])),
        "pos": vox * grid, "shape": f["acquisition/NeuroPALImageRaw/data"].shape,
    }
    if with_image:
        image = f["acquisition/NeuroPALImageRaw/data"][()]
        w["rgbw_colors"] = zscore_colors(image, vox + voxel_offset, rgbw)
        w["channel_mean"] = image.reshape(-1, image.shape[-1]).mean(axis=0)
        w["channel_range"] = (image.reshape(-1, image.shape[-1]).min(axis=0),
                              image.reshape(-1, image.shape[-1]).max(axis=0))
        # brightness of the panneuronal channel at the stored centre against offsets of -1, +1 voxel
        w["white_at_offset"] = {o: float(np.mean(zscore_colors(image, np.clip(vox + o, 0, None),
                                                               [rgbw[3]], (1, 1, 0))))
                                for o in (-1, 0, 1)}
    f.close()
    return w


def load_all(with_image: bool = True, workers: int = 5) -> list[dict]:
    assets = list_assets()
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(lambda a: load_worm(a, with_image), assets))


def worm_features(w: dict, color: bool = True) -> tuple[list[str], np.ndarray]:
    """Named neurons of a worm and their features (position um, then R, G, B colors)."""
    keep = [i for i, l in enumerate(w["labels"]) if l]
    feats = w["pos"][keep]
    if color:
        feats = np.hstack([feats, w["rgbw_colors"][keep, :3]])
    return [w["labels"][i] for i in keep], feats


# ---------------------------------------------------------------- regression and atlas

def blocks(d: int) -> list[slice]:
    return [slice(0, 3)] if d == 3 else [slice(0, 3), slice(3, d)]


def mcr_solver(Y, X, sigma, lam=0.0):
    """CELL_ID AutoId.MCR_solver: argmin_B sum_i (Y_i - X_i B) sigma_i^-1 (Y_i - X_i B)^T + ridge.

    X carries a trailing column of ones; the ridge pulls the linear part towards the identity.
    """
    ok = ~(np.isnan(X).any(1) | np.isnan(Y).any(1))
    X, Y, sigma = X[ok], Y[ok], sigma[ok]
    d1, d2 = Y.shape[1], X.shape[1]
    inv = np.linalg.inv(sigma)
    A = np.einsum("nab,ni,nj->aibj", inv, X, X).reshape(d1 * d2, d1 * d2)
    B = np.einsum("ni,nj,nja->ia", X, Y, inv)   # X_i^T Y_i sigma_i^-1, shape (d2, d1)
    # MATLAB vec is column-major: vec(B)[a*d2 + i] = B[i, a]; kron(inv, X^T X)[(a,i),(b,j)]
    if lam:
        A = A + lam * np.eye(d1 * d2)
        B = B + lam * np.vstack([np.eye(d2 - 1, d1), np.zeros((1, d1))])
    sol = np.linalg.solve(A, B.T.reshape(-1))
    return sol.reshape(d1, d2).T


def align_block(Yw, mu, sigma, lam=0.0):
    """Affine map of worm features Yw (n x d) onto atlas means, block-diagonal (eq 4.15-4.16)."""
    d = Yw.shape[1]
    T = np.zeros((d + 1, d))
    T[d, :] = 0
    for b in blocks(d):
        Xb = np.hstack([Yw[:, b], np.ones((len(Yw), 1))])
        Bb = mcr_solver(mu[:, b], Xb, sigma[:, b, b], lam)
        T[np.r_[np.arange(d)[b], d][:, None], np.arange(d)[b][None, :]] = Bb
    return T


def apply(T, Y):
    return np.hstack([Y, np.ones((len(Y), 1))]) @ T


def align_forward(Yw, mu, sigma):
    """Fit the generative model Y = mu beta + beta0 (equation 4.11) by weighted regression of the
    worm on the atlas means, block-diagonal, and return the inverse map from worm to atlas space
    in the form used by `apply`."""
    d = Yw.shape[1]
    T = np.zeros((d + 1, d))
    for b in blocks(d):
        Xb = np.hstack([mu[:, b], np.ones((len(mu), 1))])
        Fb = mcr_solver(Yw[:, b], Xb, sigma[:, b, b], 0)
        A, c = Fb[:-1], Fb[-1]
        Ainv = np.linalg.inv(A)
        idx = np.arange(d)[b]
        T[np.ix_(idx, idx)] = Ainv
        T[d, idx] = -c @ Ainv
    return T


def fit_atlas(worms: list[tuple[list[str], np.ndarray]], seed: int = 0, names=None,
              direction: str = "inverse", max_iter: int | None = None, gauge: bool = True,
              init: int | None = None):
    """MS1 Algorithm 4 on annotated worms. Returns names, mu (n x d), sigma (n x d x d), info.

    direction "inverse" regresses the atlas means on the worm (equations 4.15-4.16 as written);
    "forward" fits the generative model of equation 4.11 and inverts it (`align_forward`).
    With `gauge`, after each update the atlas is mapped back, by the block-wise affine transform
    that best maps its means onto the means of the initial worm (unweighted least squares), so
    that it stays in the initial worm's frame: the atlas is defined only up to an affine map, and
    without this it shrinks along the minor axes at every iteration (an assumption, see the
    notebook).
    """
    max_iter = max_iter or ATLAS_ITER
    align = align_forward if direction == "forward" else align_block
    if names is None:
        names = sorted(set().union(*[set(l) for l, _ in worms]))
    index = {n: i for i, n in enumerate(names)}
    m, n, d = len(worms), len(names), worms[0][1].shape[1]
    Y = np.full((m, n, d), np.nan)
    for j, (labs, F) in enumerate(worms):
        for l, f in zip(labs, F):
            if l in index:
                Y[j, index[l]] = f
    rng = np.random.default_rng(seed)
    j0 = int(rng.integers(m)) if init is None else init
    mu = Y[j0].copy()
    ref = Y[j0].copy()
    sigma = np.tile(np.eye(d), (n, 1, 1))
    mask = np.zeros((d, d), bool)
    for b in blocks(d):
        mask[b, b] = True
    for it in range(1, max_iter + 1):
        Z = np.full_like(Y, np.nan)
        for j in range(m):
            ok = ~np.isnan(Y[j]).any(1) & ~np.isnan(mu).any(1)
            T = align(Y[j][ok], mu[ok], sigma[ok])
            have = ~np.isnan(Y[j]).any(1)
            Z[j][have] = apply(T, Y[j][have])
        mu_new = np.nanmean(Z, axis=0)
        dev = Z - mu_new[None]
        cnt = (~np.isnan(Z).any(2)).sum(0)
        dev0 = np.nan_to_num(dev)
        sig_new = np.einsum("jna,jnb->nab", dev0, dev0) / np.maximum(cnt, 1)[:, None, None]
        sig_new = sig_new * mask
        if gauge:
            ok = ~np.isnan(ref).any(1) & ~np.isnan(mu_new).any(1)
            G = align_block(mu_new[ok], ref[ok], np.tile(np.eye(d), (ok.sum(), 1, 1)))
            mu_new = apply(G, mu_new)
            sig_new = np.einsum("ai,nab,bj->nij", G[:d], sig_new, G[:d])
        sig_new = sig_new + RIDGE * np.eye(d)
        dmu = np.linalg.norm(np.nan_to_num(mu_new - mu))
        dsig = np.linalg.norm(sig_new - sigma)
        mu, sigma = mu_new, sig_new
        if dmu <= TOL and dsig <= TOL:
            break
    info = {"iterations": it, "converged": bool(dmu <= TOL and dsig <= TOL), "init_worm": j0,
            "counts": cnt, "dmu": dmu, "dsig": dsig, "aligned": Z}
    return names, mu, sigma, info


# ---------------------------------------------------------------- identification

def maha(Z, mu, sigma):
    """Squared Mahalanobis distance of each row of Z to each atlas neuron (K x n)."""
    inv = np.linalg.inv(sigma)
    diff = Z[:, None, :] - mu[None, :, :]
    return np.einsum("kna,nab,knb->kn", diff, inv, diff)


def hungarian(cost):
    r, c = linear_sum_assignment(cost)
    a = np.full(cost.shape[0], -1)
    a[r] = c
    return a


def sinkhorn(logL, niter=SINKHORN_ITER):
    """CELL_ID sinkhorn_logspace: pad to square with ~0, alternate column and row normalisation.

    Run with scaling vectors on exp(logL - row maximum) for speed. Both converge to the same
    doubly stochastic matrix; after 500 iterations they differed by at most 0.001 on one worm
    checked while preparing this entry.
    """
    logL = logL.copy()
    finite = np.isfinite(logL)
    a = logL[finite].min()
    logL[~finite] = a - 10000
    n1, n2 = logL.shape
    s = max(n1, n2)
    P = np.full((s, s), -1e-100)
    P[:n1, :n2] = logL
    K = np.exp(P - P.max(axis=1, keepdims=True))
    r = np.ones(s)
    for _ in range(niter):
        c = 1.0 / (K.T @ r)
        r = 1.0 / (K @ c)
    return (r[:, None] * K * c[None, :])[:n1, :n2]


def identify_methods(F, mu, sigma):
    """MS1 Algorithm 5: identity start, alternate Hungarian (eq 4.18) and alignment (4.15-4.16)."""
    d = F.shape[1]
    T = np.vstack([np.eye(d), np.zeros((1, d))])
    for it in range(1, MAX_ITER + 1):
        Z = apply(T, F)
        a = hungarian(maha(Z, mu, sigma))
        ok = a >= 0
        T_new = align_block(F[ok], mu[a[ok]], sigma[a[ok]])
        change = np.linalg.norm(T_new - T)
        T = T_new
        if change <= TOL:
            break
    Z = apply(T, F)
    return Z, {"iterations": it, "converged": bool(change <= TOL)}


def _pca(P):
    m = P.mean(0)
    u, s, vt = np.linalg.svd(P - m, full_matrices=False)
    coeff = vt.T
    # MATLAB pca sign convention: largest absolute coefficient of each component positive
    sign = np.sign(coeff[np.argmax(np.abs(coeff), axis=0), np.arange(coeff.shape[1])])
    return coeff * sign, m


def major_axis_align(P, sgn):
    coeff, m = _pca(P)
    coeff = coeff * np.linalg.det(coeff)   # proper rotation, so that no candidate is a mirror image
    coeff[:, :2] *= sgn
    return (P - m) @ coeff


def code_alignment(F, mu, sigma):
    """CELL_ID AutoId.global_alignment / local_alignment (no annotated neurons)."""
    pos0, col0 = F[:, :3], F[:, 3:]
    has_color = F.shape[1] > 3
    # CELL_ID's atlas is centred on its principal axes; ours is in the initial worm's frame, so
    # it is first expressed in its own principal-axis frame (a rotation and translation).
    c_at, m_at = _pca(mu[:, :3])
    c_at = c_at * np.linalg.det(c_at)
    mu = mu.copy()
    mu[:, :3] = (mu[:, :3] - m_at) @ c_at
    sigma = sigma.copy()
    sigma[:, :3, :3] = np.einsum("ai,nab,bj->nij", c_at, sigma[:, :3, :3], c_at)
    coeff_mu, mu_mu = _pca(mu[:, :3])
    coeff_mu = coeff_mu * np.linalg.det(coeff_mu)
    best = (np.inf, None)
    for sgn in (+1, -1):
        for theta in THETAS:
            pos = major_axis_align(pos0, sgn)
            R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
            pos[:, 1:3] = pos[:, 1:3] @ R
            pos = pos @ coeff_mu.T + mu_mu
            pos = major_axis_align(pos, 1)
            col = col0.copy()
            bad = False
            for _ in range(ITER_RWC):
                Z = np.hstack([pos, col]) if has_color else pos
                a = hungarian(maha(Z, mu, sigma))
                ok = a >= 0
                Bp = mcr_solver(mu[a[ok], :3], np.hstack([pos[ok], np.ones((ok.sum(), 1))]),
                                sigma[a[ok]][:, :3, :3], 0)
                if np.linalg.det(Bp[:3, :3]) < 0:
                    bad = True
                    break
                pos = np.hstack([pos, np.ones((len(pos), 1))]) @ Bp
                if has_color:
                    Bc = mcr_solver(mu[a[ok], 3:], np.hstack([col[ok], np.ones((ok.sum(), 1))]),
                                    sigma[a[ok]][:, 3:, 3:], COLOR_RIDGE)
                    col = np.hstack([col, np.ones((len(col), 1))]) @ Bc
            if bad:
                continue
            Z = np.hstack([pos, col]) if has_color else pos
            D = maha(Z, mu, sigma)
            a = hungarian(D)
            cost = D[np.arange(len(a)), a].sum() / 2
            if cost < best[0]:
                best = (cost, Z)
    Z = best[1].copy()
    Z[:, :3] = Z[:, :3] @ c_at.T + m_at     # back to the atlas frame
    return Z, {"cost": best[0]}


def loglik(Z, mu, sigma):
    """Equation 5.4: log L = -1/2 Mahalanobis distance in atlas space (K x n)."""
    return -0.5 * maha(Z, mu, sigma)


def annotate(logL, k, true_i):
    """CELL_ID update_log_likelihood for one annotated neuron k with atlas identity true_i."""
    logL = logL.copy()
    logL[k, :] = MIN_LL
    logL[k, true_i] = MAX_LL
    return logL


def pair_class(name: str, names: set[str]) -> str:
    """Class of a left/right pair (RMFL, RMFR -> RMF); other neurons keep their name."""
    if name[-1:] in ("L", "R"):
        other = name[:-1] + ("R" if name[-1] == "L" else "L")
        if other in names:
            return name[:-1]
    return name


# ---------------------------------------------------------------- color violations

def prob_adjacency(pos, cov, prob=0.95, samples=1000, seed=1):
    """Optimal_Coloring computeProbAdjacency.m."""
    rng = np.random.default_rng(seed)
    n = len(pos)
    inv = np.linalg.inv(cov)
    pts = []
    for i in range(n):
        p = rng.multivariate_normal(pos[i], cov[i], samples)
        d = np.einsum("ka,ab,kb->k", p - pos[i], inv[i], p - pos[i])
        pts.append(p[np.argsort(d)[: int(samples * prob)]])
    A = np.zeros((n, n), int)
    for i in range(n):
        di = np.einsum("ka,ab,kb->k", pts[i] - pos[i], inv[i], pts[i] - pos[i])
        diff = pts[i][:, None, :] - pos[None, :, :]
        dj = np.einsum("kna,nab,knb->kn", diff, inv, diff)
        A[i] = (dj < di[:, None]).any(0)
    return A


def color_violations(colors, A, margin=1 / 3):
    """Share of adjacent pairs (off-diagonal) closer in color than the margin (MS2 section 4.3),
    and the code's mean shortfall below the margin (find_optimal_colors.m)."""
    A = A.copy().astype(float)
    np.fill_diagonal(A, 0)
    D = np.linalg.norm(colors[:, None, :] - colors[None, :, :], axis=2)
    share = float(((D < margin) * A).sum() / A.sum())
    shortfall = float(np.maximum(margin * A - D * A, 0).sum() / A.sum())
    return share, shortfall, int(A.sum())


# ---------------------------------------------------------------- leave-one-out


def run_loo(feats, alignment="methods", color=True, atlas_iter=ATLAS_ITER, seed=0, gauge=True):
    """Leave-one-out identification of the annotated neurons of each worm.

    alignment: "methods" (Algorithm 5), "code" (CELL_ID global alignment) or "oracle" (the
    held-out worm aligned with its true correspondences: an upper bound, not the paper's method).

    Returns one dict per held-out worm: atlas names, true names, true atlas index (-1 when the
    name is not in the training atlas), log likelihoods, Hungarian assignment, Sinkhorn matrix.
    """
    if not color:
        feats = [(l, F[:, :3]) for l, F in feats]
    out = []
    for j in range(len(feats)):
        train = [f for i, f in enumerate(feats) if i != j]
        names, mu, sigma, info = fit_atlas(train, seed=seed, max_iter=atlas_iter, gauge=gauge)
        labs, F = feats[j]
        idx = {n: i for i, n in enumerate(names)}
        true = np.array([idx.get(l, -1) for l in labs])
        if alignment == "methods":
            Z, ainfo = identify_methods(F, mu, sigma)
        elif alignment == "code":
            Z, ainfo = code_alignment(F, mu, sigma)
        else:
            ok = true >= 0
            Z, ainfo = apply(align_block(F[ok], mu[true[ok]], sigma[true[ok]]), F), {}
        L = loglik(Z, mu, sigma)
        a = hungarian(-L)
        out.append({"names": names, "labels": labs, "true": true, "logL": L, "assign": a,
                    "P": sinkhorn(L), "info": ainfo, "atlas_info": info})
    return out


def scores(res, by_class=False):
    """Per-worm accuracy and pooled accuracy; by_class scores left/right pairs by class."""
    per, hits = [], []
    for r in res:
        names = r["names"]
        if by_class:
            nset = set(names) | set(r["labels"])
            pred = [pair_class(names[a], nset) for a in r["assign"]]
            true = [pair_class(l, nset) for l in r["labels"]]
        else:
            pred = [names[a] for a in r["assign"]]
            true = r["labels"]
        h = np.array([p == t for p, t in zip(pred, true)])
        per.append(h.mean())
        hits.append(h)
    return np.array(per), float(np.concatenate(hits).mean())


def guided_annotation(r, n_steps, order="entropy", rng=None, with_sinkhorn=True):
    """Annotate n_steps neurons one at a time (MS1 6.5) and return the accuracy after each step,
    over all neurons (annotated ones counted correct) and over the unannotated ones."""
    L = r["logL"].copy()
    true = r["true"]
    P = r["P"]
    done = np.zeros(len(true), bool)
    candidates = true >= 0
    acc_all, acc_rest = [], []
    if order == "random":
        seq = rng.permutation(np.flatnonzero(candidates))
    for step in range(n_steps):
        if order == "random":
            k = seq[step]
        else:
            Pn = P / np.clip(P.sum(1, keepdims=True), 1e-300, None)
            if order == "entropy":
                score = -(Pn * np.log(np.clip(Pn, 1e-300, None))).sum(1)
            else:                         # lowest top probability, CELL_ID add_to_image
                score = -Pn.max(1)
            score[done | ~candidates] = -np.inf
            k = int(np.argmax(score))
        L = annotate(L, k, true[k])
        done[k] = True
        a = hungarian(-L)
        hit = a == true
        acc_all.append(hit.mean())
        acc_rest.append(hit[~done].mean())
        if order != "random" and with_sinkhorn:
            P = sinkhorn(L)
    return np.array(acc_all), np.array(acc_rest)


# ---------------------------------------------------------------- detection (MS1 sections 2, 3)
# A port of CELL_ID Preprocess.filter_gut_lysosomes and AutoDetect.detect / fit_gaussian. The
# thresholds are CELL_ID's: 99th percentiles, a 0.7-voxel in-plane Gaussian blur, components
# under 130 voxels (green and blue artifacts), gut components over 1900 voxels with a convex
# volume over 6000 (or over 1000 voxels, centroid in the last 13 planes, convex volume over
# 1700), detection at 0.4 um for adults, 3 um neuron size, eigenvalue bounds 0.01 to 5, minimum
# eigenvalue 0.1 and exclusion radius 1.5 um (NeuroPALImage.m defaults). fmincon (interior
# point) is replaced by scipy's SLSQP with the same bounds and constraints.

MP_MIN_EIG = 0.1
MP_EXCLUSION_UM = 1.5
MP_DETECT_SCALE = 0.4
MATCH_UM = 3.0     # MS1 section 6.2


def _zscore_channels(v):
    out = np.empty(v.shape, float)
    for c in range(v.shape[-1]):
        d = v[..., c].astype(float)
        out[..., c] = (d - d.mean()) / d.std(ddof=1)
    return out


def _blur2d(v, sigma=0.7):
    from scipy.ndimage import gaussian_filter
    return gaussian_filter(v, sigma=(sigma, sigma, 0), truncate=2 * np.ceil(2 * sigma) / sigma)


def filter_gut_lysosomes(z):
    """CELL_ID Preprocess.filter_gut_lysosomes on the z-scored R, G, B, W volume; returns the mask."""
    from scipy import ndimage
    from skimage.measure import regionprops, label
    st = np.ones((3, 3, 3), bool)

    def small(ch):
        d = _blur2d(z[..., ch])
        lab, n = ndimage.label(d > np.percentile(d, 99), structure=st)
        sizes = np.bincount(lab.ravel())
        keep = np.flatnonzero(sizes < 130)
        keep = keep[keep > 0]
        return np.isin(lab, keep)

    mask_g, mask_b = small(1), small(2)
    g = _blur2d(z[..., 1]); r = _blur2d(z[..., 0]); b = _blur2d(z[..., 2])
    bw = (g > max(np.percentile(g, 99), 2.8)) & (r < np.percentile(r, 99)) & (b < max(np.percentile(b, 99), 2.8))
    lab = label(bw, connectivity=3)
    square = np.zeros(bw.shape, bool)
    for p in regionprops(lab):
        if p.area <= 1000:
            continue
        conv = p.area_convex
        late = p.area > 1000 and p.centroid[2] + 1 > z.shape[2] - 13 and conv > 1700
        if (p.area > 1900 and conv > 6000) or late:
            sl = p.slice
            square[sl] = True
    return square | mask_g | mask_b


def _gauss_filter(sz):
    from scipy.stats import multivariate_normal
    mu = (np.array(sz) + 1) / 2
    grid = np.stack(np.meshgrid(*[np.arange(1, s + 1) for s in sz], indexing="ij"), -1).reshape(-1, 3)
    f = multivariate_normal(mu, np.eye(3)).pdf(grid).reshape(sz)
    return f / np.sqrt((f * f).sum())


def _simulate(sz, mu, cov, props, baseline, trunc, grid):
    from scipy.stats import multivariate_normal
    try:
        p = multivariate_normal(mu, cov, allow_singular=True).pdf(grid)
    except Exception:
        p = np.zeros(len(grid))
    p = np.where(p < trunc, 0, p)
    return (p[:, None] * props[None, :] + baseline[None, :]).reshape(*sz, len(props))


def fit_gaussian(bpatch, colorvec, scale, fsize):
    """CELL_ID AutoDetect.fit_gaussian."""
    from scipy.optimize import minimize
    C = bpatch.shape[-1]
    norm = np.r_[scale, np.sqrt([scale[0], 1, 1, scale[1], 1, scale[2]]), 1, 1, np.ones(C), np.ones(C), 10000]
    colors = bpatch.reshape(-1, C).copy()
    colors[colors == 0] = np.finfo(float).eps
    noisevec = np.percentile(colors, 10, axis=0)
    colorvec = np.where(colorvec < 0, np.finfo(float).eps, colorvec)
    color_level = colorvec.sum()
    noise_level = abs(noisevec.sum())
    colorvec = colorvec / color_level
    noisevec = noisevec / noise_level
    x0 = np.r_[(np.array(fsize) + 1) * scale, np.sqrt([3, 0, 0, 3, 0, 3]), 1.5 * np.log(color_level),
               noise_level, colorvec, noisevec, 0]
    lb = np.r_[x0[:3] - 0.3, np.zeros(6), 0, 0, np.zeros(C), -np.ones(C), 0]
    ub = np.r_[x0[:3] + 0.3, 100 * np.ones(6), 20, 0.1, np.ones(2 * C), 1000]
    x0 = np.clip(x0, lb, ub)
    sz = bpatch.shape[:3]
    grid = np.stack(np.meshgrid(*[np.arange(1, s + 1) for s in sz], indexing="ij"), -1).reshape(-1, 3)
    tri = [(0, 0), (1, 0), (2, 0), (1, 1), (2, 1), (2, 2)]   # MATLAB L([1,2,3,5,6,9])

    def unpack(x):
        x = x / norm
        L = np.zeros((3, 3))
        for k, (i, j) in enumerate(tri):
            L[i, j] = x[3 + k]
        return x, L @ L.T

    def cost(x):
        xx, cov = unpack(x)
        props = xx[11:11 + C] * np.exp(xx[9])
        base = xx[11 + C:11 + 2 * C] * xx[10]
        rec = _simulate(sz, xx[:3], cov, props, base, xx[-1], grid)
        return np.sqrt(((bpatch - rec) ** 2).sum())

    def eigc(x):
        L = np.zeros((3, 3))
        for k, (i, j) in enumerate(tri):
            L[i, j] = x[3 + k]
        v = np.sort(np.linalg.eigvalsh(L @ L.T))
        return np.r_[v - 0.01, 5 - v]

    cons = [{"type": "eq", "fun": lambda x: x[11:11 + C].sum() - 1},
            {"type": "eq", "fun": lambda x: x[11 + C:11 + 2 * C].sum() + x[-1] - 1},
            {"type": "ineq", "fun": eigc}]
    res = minimize(cost, x0, method="SLSQP", bounds=list(zip(lb, ub)), constraints=cons,
                   options={"maxiter": 200, "ftol": 1e-6})
    xh = res.x
    xx, cov = unpack(xh)
    col = xx[11:11 + C] * np.exp(xx[9])
    shape = _simulate(sz, xx[:3], cov, np.ones(1), np.zeros(1), xx[-1], grid)[..., 0]
    rel = (xh[:3] - x0[:3]) / norm[:3]
    return shape, rel, cov, col


def detect(image, rgbw, grid_um, k):
    """CELL_ID BatchDetect + AutoDetect.detect for k neurons; returns centres in voxels (0-based)."""
    from scipy.ndimage import convolve
    from skimage.transform import resize
    z = _zscore_channels(image[..., rgbw])
    z[filter_gut_lysosomes(z)] = 0
    factor = min(grid_um) / max(MP_DETECT_SCALE, min(grid_um))
    scale = np.asarray(grid_um) / factor
    new = np.round(np.array(z.shape[:3]) * factor).astype(int)
    vol = np.stack([resize(z[..., c], new, order=1, anti_aliasing=True, preserve_range=True) for c in range(4)], -1)
    vol = _zscore_channels(vol)
    hnsz = (np.round(np.round(3 / scale) / 2) * 2 + 1).astype(int)
    filt = _gauss_filter(tuple(hnsz))
    fsize = np.array(filt.shape) - 1
    rho = np.stack([convolve(vol[..., c], filt, mode="constant") for c in range(4)], -1)
    szext = np.array(vol.shape[:3])
    centres, n_fits = [], 0
    while len(centres) < k and n_fits < 3 * k:
        mag = rho.max(-1)
        loc = np.array(np.unravel_index(np.argmax(mag), mag.shape))
        lo = np.maximum(loc - fsize, 0)
        hi = np.minimum(loc + fsize, szext - 1) + 1
        patch = vol[lo[0]:hi[0], lo[1]:hi[1], lo[2]:hi[2]]
        shape, rel, cov, col = fit_gaussian(patch, rho[tuple(loc)], scale, loc - lo)
        n_fits += 1
        fshape = convolve(np.pad(shape, [(s // 2, s // 2) for s in filt.shape]), filt, mode="constant")
        # place fshape centred at loc (CELL_ID placement)
        res = np.zeros(szext)
        c = np.array(fshape.shape) // 2 + (np.array(loc - lo) - np.array(shape.shape) // 2)
        a0 = np.maximum(loc - c, 0); a1 = np.minimum(loc - c + np.array(fshape.shape), szext)
        b0 = a0 - (loc - c); b1 = b0 + (a1 - a0)
        res[a0[0]:a1[0], a0[1]:a1[1], a0[2]:a1[2]] = fshape[b0[0]:b1[0], b0[1]:b1[1], b0[2]:b1[2]]
        rho -= res[..., None] * col[None, None, None, :]
        far = not centres or np.min(np.linalg.norm((np.array(centres) - loc) * scale, axis=1)) > MP_EXCLUSION_UM
        big = np.min(np.real(np.linalg.eigvals(cov * scale[None, :]))) > MP_MIN_EIG
        if big and far:
            centres.append(loc + rel)
    centres = np.array(centres)
    orig = (centres + 0.5) / factor - 0.5      # decimated voxel centre to original voxel index
    return orig, n_fits


def match_detections(det_um, ann_um, radius=MATCH_UM):
    """MS1 section 6.2: Hungarian matching on distances, distances over the radius excluded."""
    D = np.linalg.norm(det_um[:, None] - ann_um[None], axis=2)
    big = 1e6
    r, c = linear_sum_assignment(np.where(D > radius, big, D))
    ok = D[r, c] <= radius
    tp = int(ok.sum())
    fp, fn = len(det_um) - tp, len(ann_um) - tp
    return {"tp": tp, "fp": fp, "fn": fn, "accuracy": tp / (tp + fp + fn), "precision": tp / (tp + fp),
            "recall": tp / (tp + fn), "pairs": (r[ok], c[ok])}


def _detect_asset(args):
    asset, k = args
    w = load_worm(asset, with_image=False)
    with h5py.File(remfile.File(asset["url"]), "r") as f:
        image = f["acquisition/NeuroPALImageRaw/data"][()]
    centres, n_fits = detect(image, w["rgbw"], w["grid"], k)
    vox = np.clip(np.round(centres).astype(int), 0, np.array(image.shape[:3]) - 1)
    colors = zscore_colors(image, vox, w["rgbw"][:3])
    return {"subject": w["subject"], "centres": centres, "n_fits": n_fits, "colors": colors}


def detect_all(k, workers=4):
    """Run the detection on every head, k detections each, in parallel processes."""
    from concurrent.futures import ProcessPoolExecutor
    import os
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(_detect_asset, [(a, k) for a in list_assets()]))


def run_loo_detections(feats, worms, detections, alignment="methods", atlas_iter=ATLAS_ITER):
    """Reading b of fig7bc: identify the automatic detections of each held-out worm; a named
    annotation is correct when the detection matched to it (within 3 um) gets its name, and
    annotations with no matched detection count as wrong. Returns per-worm (hits, n_named,
    by-class hits)."""
    out = []
    for j in range(len(feats)):
        train = [f for i, f in enumerate(feats) if i != j]
        names, mu, sigma, _ = fit_atlas(train, max_iter=atlas_iter)
        w, d = worms[j], detections[j]
        F = np.hstack([d["centres"] * w["grid"], d["colors"]])
        Z = identify_methods(F, mu, sigma)[0] if alignment == "methods" else code_alignment(F, mu, sigma)[0]
        a = hungarian(maha(Z, mu, sigma))
        keep = [i for i, l in enumerate(w["labels"]) if l]
        labs = [w["labels"][i] for i in keep]
        m = match_detections(F[:, :3], w["pos"][keep])
        nset = set(names) | set(labs)
        hits = sum(names[a[di]] == labs[ai] for di, ai in zip(*m["pairs"]))
        chits = sum(pair_class(names[a[di]], nset) == pair_class(labs[ai], nset) for di, ai in zip(*m["pairs"]))
        out.append({"subject": w["subject"], "hits": hits, "class_hits": chits, "named": len(labs),
                    "matched": len(m["pairs"][0])})
    return out
