"""Loading and the identification pipeline of Kay, Naselaris, Prenger & Gallant (2008) for CRCNS vim-1.

Kay et al. (2008), Nature 452:352-355, doi:10.1038/nature06713. Files are streamed from the public
CRCNS bucket (crcnsarchive, vim-1/); nothing is written to disk.

The data set holds, per subject, the estimated (repeated-trial) responses of about 26,000 voxels to
the 1,750 model estimation images (`dataTrn`) and the 120 identification images (`dataVal`), z-scored
per voxel, with ROI labels (0 other, 1 V1, 2 V2, 3 V3, 4 V3A, 5 V3B, 6 V4, 7 LatOcc), and the
stimuli at full resolution (500 px over 20 degrees).

Where the parameters come from (claims file `claims/kay-2008.yaml`, opening comment, P1 to P6 and
O1 to O7, which cite the Supplementary Methods; SM below):

- Stimulus resolutions min(500, round(2 ** (9 - x / 8))), x = 0..24 (SM 6, "Stimulus
  pre-processing"); mean luminance over all stimuli subtracted (SM 6). Stimulus values are taken as
  linear in luminance (O4, an assumption: the goggles' response is not given).
- Down-sampling uses area averaging (a standard choice for a detail that should not change a
  result; SM 6 does not say how the stimuli were resampled).
- Gabor wavelet pyramid (SM 6, "Design of the wavelet pyramid"): f = 1, 2, 4, 8, 16 (and 32 at
  128 px) cycles per field of view, centres on an f x f grid at the cell centres (O3, standard
  choice), 8 orientations, 2 quadrature phases, isotropic Gaussian masks with a spatial frequency
  bandwidth of 1 octave (full width at half maximum), so the Gaussian SD is
  3 * sqrt(2 ln 2) / (2 pi) = 0.562 wavelengths (O3: the SD in pixels is fixed by the bandwidth only
  up to convention; this convention gives an orientation bandwidth of 37 degrees against the 41 the
  paper states), masks zeroed below 0.01 of peak, truncated at the image bounds, each wavelet
  zero-mean and unit-length within its mask; one luminance-only wavelet over the whole image whose
  channel is sqrt(2 * p ** 2) (SM 6, "Transformation from image to predicted response").
- A wavelet's projection is set to zero if more than half of its mask (by weight) lies beyond 90%
  of the stimulus radius (SM 6). The radius is that of the circular mask in `mask.mat`.
- Fitting (SM 6, "Estimation of model parameters"): 20% of the training responses drawn at random
  as a stopping set, responses mean-subtracted, channels z-scored, kernel from zero, step 0.001,
  normalized gradient with momentum 0.9 (both the error gradient and the sum normalized to unit
  length, our reading of the garbled formula), stop at the first iteration where the stopping-set
  error no longer decreases. One stopping set is drawn per fit and shared by all voxels fitted
  together (a standard choice for a random draw). The paper's 100 bootstrap fits, whose mean gives
  the final parameters, are not run here for time (a deviation; `n_boot` runs a smaller number).
- Rough localization (SM 5): orientation-invariant 128 px models over the full 20 degrees, the
  central 10.0 degrees (128 px of the 256 px image) and the central 5.12 degrees (128 px of the
  500 px image); the paper states 10.1 and 5.2 degrees, which the resolution list does not give
  exactly. The spatial envelope is the sum of the channel masks (each normalized to sum to 1)
  scaled by the absolute weights (SM 6, "Calculation of tuning curves"); an isotropic 2-D Gaussian
  with a constant offset (the offset is our choice; SM 5 says only "an isotropic two-dimensional
  Gaussian") is fitted to it at 32 x 32. The RF is the square of +/-2 SD; for the 10 and 5 degree
  models it is valid only if wholly within the field of view. The best initial model is the valid
  one with the least stopping-set error.
- Predictive power is Pearson r on the 120 identification images (SM 6); its one-tailed p-value is
  the fraction of 1,000 bootstrap resamples of the 120 image pairs with r <= 0 (O2, standard choice).
- Final model (SM 5): 64 px, not orientation invariant (2,729 channels and a DC offset). Its field
  of view is O5 reading (a), the square of +/-2 SD of the fitted Gaussian, taken from the
  resolution of the list at which that square is closest to 64 px, or (b), the best initial
  model's field of view at 64 px.
- Identification (main text; SM 7): for each measured pattern, the 500 voxels with highest
  predictive power over the other 119 images, then the image whose predicted pattern has the
  highest Pearson r with the measured pattern.
"""

from __future__ import annotations

import io

import fsspec
import h5py
import numpy as np
import scipy.io as sio
from scipy import sparse
from scipy.optimize import least_squares

DATASET = "vim-1"            # CRCNS data set, doi:10.6080/K0QN64NG
VERSION = "unversioned"      # CRCNS data sets are not versioned (docs/archives.md); MD5s in the notebook
BASE = f"https://crcnsarchive.s3-us-west-2.amazonaws.com/{DATASET}/"
ROI_NAMES = {0: "other", 1: "V1", 2: "V2", 3: "V3", 4: "V3A", 5: "V3B", 6: "V4", 7: "LatOcc"}
STIM_DEG = 20.0
FULL_PX = 500
RESOLUTIONS = [min(500, round(2 ** (9 - x / 8))) for x in range(25)]
STEP, MOMENTUM, STOP_FRACTION = 0.001, 0.9, 0.2
N_VOXELS_ID = 500


def _open(name, block=2**23):
    return fsspec.open(BASE + name, block_size=block, cache_type="readahead").open()


# ---------------------------------------------------------------------------------------------
# Loading


def load_responses(subject, rois=(1, 2, 3, 6)):
    """Estimated responses of one subject ('S1' or 'S2') for the voxels in `rois`.

    Returns a dict with trn (1750 x V), val (120 x V), roi, vox_idx (the data set's index into the
    64 x 64 x 18 volume), and the counts per ROI over all voxels and of voxels dropped for NaNs.
    """
    with _open("EstimatedResponses.mat") as f, h5py.File(f, "r") as h:
        roi = h["roi" + subject][0].astype(int)
        vox = h["voxIdx" + subject][0].astype(int)
        counts_all = {ROI_NAMES[k]: int((roi == k).sum()) for k in range(8)}
        cols = np.where(np.isin(roi, rois))[0]
        trn = h["dataTrn" + subject][:, :][:, cols].astype(np.float32)
        val = h["dataVal" + subject][:, :][:, cols].astype(np.float32)
        n_total = roi.size
    bad = np.isnan(trn).any(0) | np.isnan(val).any(0)
    out = dict(trn=trn[:, ~bad], val=val[:, ~bad], roi=roi[cols][~bad], vox_idx=vox[cols][~bad],
               counts_all=counts_all, n_total=n_total,
               dropped_nan={ROI_NAMES[k]: int((bad & (roi[cols] == k)).sum()) for k in rois})
    return out


def load_stimuli():
    """Full-resolution stimuli (1870 x 500 x 500 float32: 1,750 training then 120 validation),
    the 128 px stimuli of Stimuli.mat, the presentation sequences, and the circular mask."""
    full = np.empty((1870, FULL_PX, FULL_PX), np.float32)
    i = 0
    for k in range(1, 16):
        with _open(f"Stimuli_Trn_FullRes_{k:02d}.mat") as f, h5py.File(f, "r") as h:
            a = h["stimTrn"][:]          # stored (500, 500, n): MATLAB n x 500 x 500
            a = np.transpose(a, (2, 1, 0))
            full[i:i + a.shape[0]] = a
            i += a.shape[0]
    with _open("Stimuli_Val_FullRes.mat") as f, h5py.File(f, "r") as h:
        full[i:] = np.transpose(h["stimVal"][:], (2, 1, 0))
    with _open("Stimuli.mat") as f:
        s = sio.loadmat(io.BytesIO(f.read()))
    with _open("mask.mat") as f:
        m = sio.loadmat(io.BytesIO(f.read()))["mask"]
    small = np.concatenate([s["stimTrn"], s["stimVal"]]).astype(np.float32)
    return dict(full=full, small=small, seq_trn=s["seqTrn"], seq_val=s["seqVal"], mask=m)


# ---------------------------------------------------------------------------------------------
# Resampling


def area_matrix(n_in, n_out):
    """n_out x n_in matrix that resamples by area averaging (overlap of output and input pixels)."""
    edges_out = np.linspace(0, n_in, n_out + 1)
    A = np.zeros((n_out, n_in))
    for o in range(n_out):
        a, b = edges_out[o], edges_out[o + 1]
        for j in range(int(np.floor(a)), int(np.ceil(b))):
            A[o, j] = min(b, j + 1) - max(a, j)
    return (A / A.sum(1, keepdims=True)).astype(np.float32)


def resize_stack(imgs, n_out):
    if imgs.shape[1] == n_out:
        return imgs
    A = area_matrix(imgs.shape[1], n_out)
    return np.einsum("oi,nij,pj->nop", A, imgs, A, optimize=True)


def crop(imgs, cy, cx, size, fill):
    """Square crop of side `size` px centred at (cy, cx) px (floats), padded with `fill`."""
    n = imgs.shape[1]
    y0 = int(round(cy - size / 2)); x0 = int(round(cx - size / 2))
    out = np.full((imgs.shape[0], size, size), fill, np.float32)
    ys, xs = max(0, y0), max(0, x0)
    ye, xe = min(n, y0 + size), min(n, x0 + size)
    if ye > ys and xe > xs:
        out[:, ys - y0:ye - y0, xs - x0:xe - x0] = imgs[:, ys:ye, xs:xe]
    return out


# ---------------------------------------------------------------------------------------------
# Gabor wavelet pyramid

SD_PER_WAVELENGTH = 3 * np.sqrt(2 * np.log(2)) / (2 * np.pi)


def gwp(npx, n_levels):
    """Wavelet pyramid at `npx` px with `n_levels` spatial frequencies (1, 2, 4, ... cycles/FOV).

    Returns a sparse (npx*npx x n_wavelets) matrix with the wavelets in the order
    level, grid row, grid column, orientation, phase; and a table of the channels (one per
    quadrature pair, then the luminance channel last) with level, cycles per FOV, row and column
    centre in px, orientation index, and the normalized mask of each channel (sparse, sums to 1).
    """
    yy, xx = np.mgrid[0:npx, 0:npx].astype(np.float64) + 0.5
    rows, cols, vals = [], [], []
    mrows, mcols, mvals = [], [], []
    chan = []
    w = 0
    for lev in range(n_levels):
        f = 2 ** lev
        lam = npx / f
        sd = SD_PER_WAVELENGTH * lam
        for gy in range(f):
            for gx in range(f):
                cy = (gy + 0.5) * npx / f
                cx = (gx + 0.5) * npx / f
                g = np.exp(-((yy - cy) ** 2 + (xx - cx) ** 2) / (2 * sd ** 2))
                support = g >= 0.01
                idx = np.flatnonzero(support)
                gm = g.ravel()[idx]
                for o in range(8):
                    th = np.pi * o / 8
                    u = (xx.ravel()[idx] - cx) * np.cos(th) + (yy.ravel()[idx] - cy) * np.sin(th)
                    c = len(chan)
                    for ph in (0, np.pi / 2):
                        wv = gm * np.cos(2 * np.pi * u / lam + ph)
                        wv = wv - wv.mean()
                        wv = wv / np.linalg.norm(wv)
                        rows.append(idx); cols.append(np.full(idx.size, w)); vals.append(wv)
                        w += 1
                    mrows.append(np.full(idx.size, c)); mcols.append(idx); mvals.append(gm / gm.sum())
                    chan.append((lev, f, cy, cx, o))
    # luminance-only wavelet
    idx = np.arange(npx * npx)
    rows.append(idx); cols.append(np.full(idx.size, w)); vals.append(np.full(idx.size, 1 / npx))
    mrows.append(np.full(idx.size, len(chan))); mcols.append(idx); mvals.append(np.full(idx.size, 1 / npx ** 2))
    chan.append((-1, 0, npx / 2, npx / 2, -1))
    W = sparse.csc_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
                          shape=(npx * npx, w + 1), dtype=np.float32)
    M = sparse.csr_matrix((np.concatenate(mvals), (np.concatenate(mrows), np.concatenate(mcols))),
                          shape=(len(chan), npx * npx), dtype=np.float32)
    table = np.array(chan, dtype=float)
    return W, table, M


def edge_keep(table, M, npx, fov_deg, center_deg, radius_deg):
    """True for channels whose mask lies at most half beyond 90% of the stimulus radius (SM 6).

    The FOV of `fov_deg` spans `npx` px and is centred at `center_deg` (x, y) from the stimulus centre.
    """
    yy, xx = np.mgrid[0:npx, 0:npx].astype(np.float64) + 0.5
    deg_per_px = fov_deg / npx
    ry = (yy - npx / 2) * deg_per_px + center_deg[1]
    rx = (xx - npx / 2) * deg_per_px + center_deg[0]
    outside = (np.hypot(rx, ry) > 0.9 * radius_deg).ravel().astype(np.float32)
    frac_out = M @ outside
    keep = frac_out <= 0.5
    keep[-1] = True                                   # luminance wavelet: always kept
    return keep


def gwp_channels(imgs, W, table, keep, orientation_invariant):
    """Contrast-energy channels of `imgs` (n x npx x npx). Returns n x channels (float32)."""
    n = imgs.shape[0]
    if sparse.issparse(W):
        P = np.asarray((sparse.csr_matrix(W.T) @ imgs.reshape(n, -1).T).T, dtype=np.float32)
    else:                                                  # dense wavelets: faster for many images
        P = imgs.reshape(n, -1) @ W
    nq = (P.shape[1] - 1) // 2
    E = np.sqrt(P[:, 0:2 * nq:2] ** 2 + P[:, 1:2 * nq:2] ** 2)
    lum = np.sqrt(2 * P[:, -1:] ** 2)
    E = E * keep[:-1][None, :]
    if orientation_invariant:
        E = E.reshape(n, -1, 8).sum(2)
    return np.concatenate([E, lum], 1)


def orientation_invariant_table(table, M):
    """Channel table and masks after summing over orientation (one channel per position)."""
    t = table[:-1].reshape(-1, 8, 5)[:, 0]
    Mi = M[:-1][::8]
    return np.concatenate([t, table[-1:]]), sparse.vstack([Mi, M[-1:]]).tocsr()


# ---------------------------------------------------------------------------------------------
# Gradient descent with early stopping


def fit_gd(X, Y, stop_idx, max_iter=5000, n_iter=None):
    """Gradient descent with early stopping (SM 6), vectorized over voxels (columns of Y).

    X: n x q channels, Y: n x V responses, stop_idx: indices of the stopping set. Returns the
    kernel in channel units (q x V), the DC offset (V), the stopping-set squared error at the
    chosen iteration (V) and the iteration count (V). With `n_iter` (array, one per voxel) the
    fit runs that many iterations instead of early stopping (used for bootstraps).
    """
    n = X.shape[0]
    fit = np.setdiff1d(np.arange(n), stop_idx)
    Xf, Xs = X[fit], X[stop_idx]
    xm, xs = Xf.mean(0), Xf.std(0)
    xs[xs == 0] = 1
    Xf = ((Xf - xm) / xs).astype(np.float32)
    Xs = ((Xs - xm) / xs).astype(np.float32)
    ym = Y[fit].mean(0)
    Yf = Y[fit] - ym
    Ys = Y[stop_idx] - ym
    use_gram = Y.shape[1] > 50          # few voxels: the gradient from the samples is cheaper
    C = (Xf.T @ Yf).astype(np.float32)
    G = (Xf.T @ Xf).astype(np.float32) if use_gram else None
    q, V = C.shape
    h = np.zeros((q, V), np.float32)
    g = np.zeros((q, V), np.float32)
    best_h = h.copy()
    err = (Ys ** 2).sum(0)
    iters = np.zeros(V, int)
    active = np.ones(V, bool) if n_iter is None else n_iter > 0
    it = 0
    while active.any() and it < max_iter:
        a = np.flatnonzero(active)
        grad = (G @ h[:, a] if use_gram else Xf.T @ (Xf @ h[:, a])) - C[:, a]
        grad /= np.maximum(np.linalg.norm(grad, axis=0), 1e-12)
        gn = grad + MOMENTUM * g[:, a]
        gn /= np.maximum(np.linalg.norm(gn, axis=0), 1e-12)
        g[:, a] = gn
        h[:, a] -= STEP * gn
        it += 1
        if n_iter is None:
            e = ((Xs @ h[:, a] - Ys[:, a]) ** 2).sum(0)
            better = e < err[a]
            err[a[better]] = e[better]
            iters[a[better]] = it
            best_h[:, a[better]] = h[:, a[better]]
            active[a[~better]] = False
        else:
            best_h[:, a] = h[:, a]
            iters[a] = it
            active[a[n_iter[a] <= it]] = False
    k = best_h / xs[:, None]
    dc = ym - xm @ k
    return k, dc, err, iters


def fit_boot(X, Y, rng, n_boot=0):
    """Fit on the original responses with early stopping; then, with `n_boot` > 0, the paper's
    bootstrap: resample the responses, draw a new stopping set, run the same iteration count,
    and average the parameters (SM 6, "Estimation of variance")."""
    n = X.shape[0]
    stop = rng.choice(n, int(round(STOP_FRACTION * n)), replace=False)
    k, dc, err, iters = fit_gd(X, Y, stop)
    if n_boot == 0:
        return k, dc, err, iters
    ks, dcs = np.zeros_like(k), np.zeros_like(dc)
    for _ in range(n_boot):
        b = rng.integers(0, n, n)
        sb = rng.choice(n, int(round(STOP_FRACTION * n)), replace=False)
        kb, dcb, _, _ = fit_gd(X[b], Y[b], sb, n_iter=iters)
        ks += kb; dcs += dcb
    return ks / n_boot, dcs / n_boot, err, iters


# ---------------------------------------------------------------------------------------------
# Predictive power, significance, identification


def pearson_cols(a, b):
    a = a - a.mean(0); b = b - b.mean(0)
    return (a * b).sum(0) / np.sqrt((a ** 2).sum(0) * (b ** 2).sum(0))


def boot_p(meas, pred, rng, n_boot=1000):
    """One-tailed bootstrap p-value of r > 0 over images (O2): fraction of resamples with r <= 0."""
    n = meas.shape[0]
    cnt = np.zeros(meas.shape[1])
    for _ in range(n_boot):
        b = rng.integers(0, n, n)
        cnt += np.nan_to_num(pearson_cols(meas[b], pred[b]), nan=0) <= 0
    return cnt / n_boot


def loo_power(meas, pred):
    """Predictive power of each voxel with each image left out: 120 x V matrix of Pearson r."""
    n = meas.shape[0]
    out = np.empty(meas.shape, np.float64)
    for j in range(n):
        keep = np.arange(n) != j
        out[j] = pearson_cols(meas[keep], pred[keep])
    return out


def identify_repeated(meas, pred, power_loo, n_vox=N_VOXELS_ID, cand=None):
    """Repeated-trial identification: meas and pred are 120 x V; voxel selection for pattern j
    uses power_loo[j]. `cand` restricts the candidate voxels (boolean mask over V)."""
    n = meas.shape[0]
    choice = np.empty(n, int)
    selected = []
    for j in range(n):
        pw = np.where(cand, power_loo[j], -np.inf) if cand is not None else power_loo[j]
        pw = np.nan_to_num(pw, nan=-np.inf)
        sel = np.argsort(-pw)[:n_vox]
        selected.append(sel)
        m = meas[j, sel]; m = m - m.mean()
        p = pred[:, sel]; p = p - p.mean(1, keepdims=True)
        r = p @ m / np.sqrt((p ** 2).sum(1) * (m ** 2).sum())
        choice[j] = np.argmax(r)
    return choice, selected


# ---------------------------------------------------------------------------------------------
# Gaussian fit to the spatial envelope


def fit_gaussian(env):
    """Isotropic 2-D Gaussian with offset fitted to an envelope (k x k). Returns (y0, x0, sd) in px
    of the k x k grid (pixel centres at i + 0.5)."""
    k = env.shape[0]
    yy, xx = np.mgrid[0:k, 0:k] + 0.5
    e = env / env.max() if env.max() > 0 else env
    iy, ix = np.unravel_index(np.argmax(e), e.shape)

    def res(p):
        a, y0, x0, s, b = p
        return (a * np.exp(-((yy - y0) ** 2 + (xx - x0) ** 2) / (2 * s ** 2)) + b - e).ravel()

    p0 = [1 - np.median(e), iy + 0.5, ix + 0.5, k / 8, np.median(e)]
    r = least_squares(res, p0, bounds=([0, -k, -k, 0.25, -1], [10, 2 * k, 2 * k, 4 * k, 1]),
                      max_nfev=200)
    return r.x[1], r.x[2], abs(r.x[3])


def envelopes(k, M, size, block):
    """Spatial envelopes (V x size/block x size/block) from kernels k (q x V) and masks M (q x px)."""
    E = (M.T @ np.abs(k)).T  # V x px
    V = E.shape[0]
    E = E.reshape(V, size // block, block, size // block, block).mean((2, 4))
    return E


# ---------------------------------------------------------------------------------------------
# The pipeline for one subject

FOVS = {"20": (128, STIM_DEG), "10": (256, STIM_DEG * 128 / 256), "5": (500, STIM_DEG * 128 / 500)}
FINAL_B = {"20": (64, STIM_DEG), "10": (128, STIM_DEG * 64 / 128), "5": (250, STIM_DEG * 64 / 250)}


def stimulus_radius_deg(mask):
    """Radius of the circular stimulus mask, from its area (degrees)."""
    return float(np.sqrt(mask.sum() / np.pi) / mask.shape[0] * STIM_DEG)


def fov_images(full, fill, res, npx):
    """Stimuli resampled to `res` px over 20 degrees, central `npx` px."""
    return crop(resize_stack(full, res), res / 2, res / 2, npx, fill)


def initial_channels(full, fill, radius):
    """Orientation-invariant 128 px channels for the three initial fields of view (SM 5)."""
    W, table, M = gwp(128, 6)
    ti, Mi = orientation_invariant_table(table, M)
    out = {}
    for name, (res, fov) in FOVS.items():
        keep = edge_keep(table, M, 128, fov, (0, 0), radius)
        out[name] = gwp_channels(fov_images(full, fill, res, 128), W, table, keep, True)
    return out, Mi


def final_b_channels(full, fill, radius):
    """64 px channels, not orientation invariant, over the three initial fields of view (O5 b)."""
    W, table, M = gwp(64, 5)
    out, keeps = {}, {}
    for name, (res, fov) in FINAL_B.items():
        keeps[name] = edge_keep(table, M, 64, fov, (0, 0), radius)
        out[name] = gwp_channels(fov_images(full, fill, res, 64), W, table, keeps[name], False)
    return out, keeps, (W, table, M)


def initial_models(D, chans, Mi, rng, n_boot_p=1000):
    """Fit the three initial models to every voxel of D, fit Gaussians to their envelopes, choose
    the best initial model (SM 5), and give its predictive power and bootstrap p-value (SM 6)."""
    Y, Yv = D["trn"], D["val"]
    V = Y.shape[1]
    stop = rng.choice(Y.shape[0], int(round(STOP_FRACTION * Y.shape[0])), replace=False)
    res = {}
    for name in FOVS:
        X = chans[name]
        k, dc, err, iters = fit_gd(X[:1750], Y, stop)
        pred = X[1750:] @ k + dc
        r = np.nan_to_num(pearson_cols(Yv, pred), nan=0.0)
        fov = FOVS[name][1]
        E = envelopes(k, Mi, 128, 4)
        gs = np.full((V, 3), np.nan)
        for v in np.flatnonzero(iters > 0):
            gs[v] = fit_gaussian(E[v])
        cx = (gs[:, 1] / 32 - 0.5) * fov
        cy = -(gs[:, 0] / 32 - 0.5) * fov
        sd = gs[:, 2] / 32 * fov
        inside = (np.abs(cx) + 2 * sd <= fov / 2) & (np.abs(cy) + 2 * sd <= fov / 2)
        valid = (iters > 0) & (inside if name != "20" else True)
        res[name] = dict(k=k, dc=dc, err=err, iters=iters, r=r, pred=pred, cx=cx, cy=cy, sd=sd,
                         valid=valid)
    names = list(FOVS)
    errs = np.stack([np.where(res[n]["valid"], res[n]["err"], np.inf) for n in names])
    best = np.argmin(errs, 0)
    has = np.isfinite(errs.min(0))
    pick = lambda key: np.stack([res[n][key] for n in names])[best, np.arange(V)]
    best_r = np.where(has, pick("r"), 0.0)
    best_pred = np.stack([res[n]["pred"] for n in names])[best, :, np.arange(V)].T
    p = boot_p(Yv, best_pred, rng, n_boot_p)
    p[~has] = 1.0
    return dict(models=res, best=np.array(names)[best], has=has, r=best_r, p=p, pred=best_pred,
                cx=pick("cx"), cy=pick("cy"), sd=pick("sd"))


def final_b(D, init, chans_b, rng, voxels, n_boot=0):
    """Final 64 px models over the best initial model's field of view (O5 b) for `voxels`."""
    V = D["trn"].shape[1]
    pred = np.zeros((120, V), np.float32)
    kern = {}
    for name in FINAL_B:
        vs = np.flatnonzero(voxels & (init["best"] == name))
        if vs.size == 0:
            continue
        X = chans_b[name]
        k, dc, err, iters = fit_boot(X[:1750], D["trn"][:, vs], rng, n_boot)
        pred[:, vs] = X[1750:] @ k + dc
        for j, v in enumerate(vs):
            kern[v] = (name, k[:, j], dc[j])
    return pred, kern


def final_a_plan(init, voxels):
    """Field of view of the final model under O5 (a): the +/-2 SD square, at the resolution of the
    list where that square is closest to 64 px (in log size). Returns resolution and the centre
    (row, column) in px of that resolution, per voxel."""
    side = 4 * init["sd"]
    want = 64 * STIM_DEG / np.maximum(side, 1e-6)
    resl = np.array(RESOLUTIONS)
    pick = np.abs(np.log(resl[None, :]) - np.log(want[:, None])).argmin(1)
    res = resl[pick]
    col = res / 2 + init["cx"] * res / STIM_DEG
    row = res / 2 - init["cy"] * res / STIM_DEG
    return np.where(voxels, res, 0), row, col


def final_a(D, init, full, fill, radius, rng, voxels, W64, log=None):
    """Final 64 px models over the +/-2 SD square of each voxel (O5 a), one voxel at a time."""
    W, table, M = W64
    W = W.toarray()
    V = D["trn"].shape[1]
    res, row, col = final_a_plan(init, voxels)
    pred = np.zeros((120, V), np.float32)
    kern = {}
    stop = rng.choice(1750, int(round(STOP_FRACTION * 1750)), replace=False)
    for r in sorted(set(res[voxels])):
        stack = resize_stack(full, int(r))
        fov = 64 * STIM_DEG / r
        for v in np.flatnonzero(voxels & (res == r)):
            imgs = crop(stack, row[v], col[v], 64, fill)
            centre = ((col[v] - r / 2) * STIM_DEG / r, (r / 2 - row[v]) * STIM_DEG / r)
            keep = edge_keep(table, M, 64, fov, centre, radius)
            X = gwp_channels(imgs, W, table, keep, False)
            k, dc, err, iters = fit_gd(X[:1750], D["trn"][:, [v]], stop)
            pred[:, v] = X[1750:] @ k[:, 0] + dc[0]
            kern[v] = (int(r), k[:, 0], dc[0], centre, fov, keep)
        del stack
        if log is not None:
            log(r)
    return pred, kern


# ---------------------------------------------------------------------------------------------
# Retinotopy-only model (SM 8)


def ro_channels(full, init, voxels, weighted=True, chunk=256):
    """The two RO channels for `voxels` at the original 500 px resolution (SM 8): the absolute
    spatially-weighted luminance and the spatially-weighted contrast (square root of the weighted
    variance), with the weights of the Gaussian G of the best initial model; with
    `weighted=False`, the standard metrics (mean and SD) over the +/-2 SD square of G.
    Returns two 1870 x V arrays (zero for voxels not in `voxels`)."""
    n = full.shape[0]
    flat = full.reshape(n, -1)
    sq = flat ** 2
    yy, xx = np.mgrid[0:FULL_PX, 0:FULL_PX] + 0.5
    px = FULL_PX / STIM_DEG
    vs = np.flatnonzero(voxels)
    L = np.zeros((n, voxels.size), np.float32)
    Cn = np.zeros((n, voxels.size), np.float32)
    for i in range(0, vs.size, chunk):
        v = vs[i:i + chunk]
        cx = FULL_PX / 2 + init["cx"][v] * px
        cy = FULL_PX / 2 - init["cy"][v] * px
        sd = init["sd"][v] * px
        if weighted:
            w = np.exp(-((yy.ravel()[:, None] - cy) ** 2 + (xx.ravel()[:, None] - cx) ** 2) / (2 * sd ** 2))
        else:
            w = ((np.abs(yy.ravel()[:, None] - cy) <= 2 * sd) & (np.abs(xx.ravel()[:, None] - cx) <= 2 * sd))
        w = w.astype(np.float32)
        tot = np.maximum(w.sum(0), 1e-12)
        m1 = (flat @ w) / tot
        m2 = (sq @ w) / tot
        L[:, v] = np.abs(m1)
        Cn[:, v] = np.sqrt(np.maximum(m2 - m1 ** 2, 0))
    return L, Cn


def fit_ro(D, L, C, rng, voxels):
    """Fit the RO model (gradient descent of SM 6) to `voxels`; predictions for the 120 images."""
    V = D["trn"].shape[1]
    pred = np.zeros((120, V), np.float32)
    stop = rng.choice(1750, int(round(STOP_FRACTION * 1750)), replace=False)
    for v in np.flatnonzero(voxels):
        X = np.stack([L[:, v], C[:, v]], 1)
        k, dc, err, iters = fit_gd(X[:1750], D["trn"][:, [v]], stop)
        pred[:, v] = X[1750:] @ k[:, 0] + dc[0]
    return pred


# ---------------------------------------------------------------------------------------------
# Tuning curves and envelopes of final models (SM 6, "Calculation of tuning curves")


def gratings(npx=64, n_phase=16, amplitude=0.5):
    """Sinusoidal gratings at the 8 orientations and 5 spatial frequencies (1 to 16 cycles per
    FOV) of the 64 px pyramid, at `n_phase` phases: array (8, 5, n_phase, npx, npx). The
    amplitude is a standard choice (the stimulus values span about +/-0.5); with the energy model
    it scales the curves but does not change their shape."""
    yy, xx = np.mgrid[0:npx, 0:npx] + 0.5
    out = np.empty((8, 5, n_phase, npx, npx), np.float32)
    for o in range(8):
        th = np.pi * o / 8
        u = xx * np.cos(th) + yy * np.sin(th)
        for s in range(5):
            f = 2 ** s
            for p in range(n_phase):
                out[o, s, p] = amplitude * np.cos(2 * np.pi * f * u / npx + 2 * np.pi * p / n_phase)
    return out


def tuning(kern_list, keep_list, W64, grat):
    """Orientation (8) and spatial frequency (5) tuning curves of final models: the model's
    response to each grating, averaged over phase, then over SF (orientation curve) or orientation
    (SF curve). `kern_list` holds (kernel, dc); `keep_list` the edge masks used for each."""
    W, table, M = W64
    n = grat.shape[0] * grat.shape[1] * grat.shape[2]
    imgs = grat.reshape(n, 64, 64)
    ori, sf = [], []
    for (k, dc), keep in zip(kern_list, keep_list):
        X = gwp_channels(imgs, W, table, keep, False)
        r = (X @ k + dc).reshape(grat.shape[:3]).mean(2)
        ori.append(r.mean(1)); sf.append(r.mean(0))
    return np.array(ori), np.array(sf)


def final_envelope(k, M):
    """Spatial envelope of a final model (64 x 64), masks normalized to sum to 1 (SM 6)."""
    return (M.T @ np.abs(k)).reshape(64, 64)


# ---------------------------------------------------------------------------------------------
# Image similarity (Supplementary Discussion 1)


def local_contrast(full_raw, block_px, relative=False):
    """RMS contrast in square blocks of `block_px` px (0.6 degrees is 15 px at 500 px): the SD of
    the values in each block, or with `relative` that SD over the block mean (values shifted to
    start at 0, as the absolute luminance is not given)."""
    n = full_raw.shape[0]
    nb = FULL_PX // block_px
    a = full_raw[:, :nb * block_px, :nb * block_px].reshape(n, nb, block_px, nb, block_px)
    sd = a.std((2, 4))
    if relative:
        sd = sd / np.maximum(a.mean((2, 4)), 1e-6)
    return sd.reshape(n, -1)


def corr_rows(a, b):
    a = a - a.mean(1, keepdims=True); b = b - b.mean(1, keepdims=True)
    a /= np.linalg.norm(a, axis=1, keepdims=True); b /= np.linalg.norm(b, axis=1, keepdims=True)
    return a @ b.T


def aperture(fov, centre, radius, npx=64):
    """True for the pixels of a field of view that lie inside the circular stimulus (radius in deg)."""
    yy, xx = np.mgrid[0:npx, 0:npx] + 0.5
    x = centre[0] + (xx - npx / 2) * fov / npx
    y = centre[1] - (yy - npx / 2) * fov / npx
    return np.hypot(x, y) <= radius
