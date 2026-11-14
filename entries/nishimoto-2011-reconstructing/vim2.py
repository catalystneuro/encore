"""Loading and measures for CRCNS vim-2 (Nishimoto et al. 2011, Current Biology 21, 1641-1646).

The data set is not versioned (docs/archives.md, CRCNS); its files are read from the public S3
bucket crcnsarchive. Each file is a tar.gz holding one MATLAB 7.3 (HDF5) file. A gzip stream
cannot be read at random and h5py needs random access, so each member is streamed once
(HTTP -> gzip -> tar) into a buffer in memory and opened from there; nothing is written to disk.
One large file is held at a time, and only the voxels or frames the analysis needs are kept.

Where each parameter comes from:
- Voxel areas V1, V2, V3, V3A, V3B: claims file, fig2de criterion; masks are the data set's
  `roi` structure (data descriptor).
- Discarding the first 6 s of each 600 s training block and of each 60 s test block (7,128 and
  486 samples): Supplemental Experimental Procedures, Model Fitting, paragraph 3.
- Motion-energy filter bank: Supplemental, Motion-Energy Encoding Model and Gabor Wavelet Basis
  Set. The bank is pymoten's MotionEnergyPyramid (the Gallant lab's implementation of this
  model) with spatial frequencies 0 to 32 cycles/image on a 96 x 96 image at 15 Hz; its default
  envelopes (spatial s.d. 0.6 wavelengths, 10-frame temporal window) give exactly the 6,555
  filters the paper states, which the claims file says the chosen reading should reproduce.
  Quadrature pairs are combined as the square root of the summed squares and log-compressed
  with log(x + 1e-5) (pymoten defaults); the paper's "squared and summed" then log differs only
  by a factor of 2, removed by the z-score (standard choice, cannot change a result).
- Downsampling 15 Hz -> 1 Hz by the mean of the 15 frames of each second, z-score with the
  training statistics, clipping at 3 s.d.: Motion-Energy Encoding Model; the mean and the use of
  training statistics are the claims file's standard choices.
- Delays 3, 4, 5, 6 s (4 samples) and the single 4 s delay for decoding: Motion-Energy Encoding
  Model, last paragraph.
- Ridge regression in place of the paper's L1-regularized regression: a deviation, for time
  (see the notebook); the penalty is chosen per voxel on a held-out 10% of the training data
  in 50 s blocks (claims file, Encoding model fit, reading a) or by 5-fold cross-validation
  over such blocks (reading b).
"""
import gzip
import io
import tarfile
import urllib.request

import h5py
import numpy as np

DATASET, VERSION = "vim-2", "unversioned"  # CRCNS data sets are not versioned (docs/archives.md)
BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/vim-2/"
AREAS = ["v1", "v2", "v3", "v3a", "v3b"]
TRAIN_BLOCK, TEST_BLOCK, DISCARD = 600, 60, 6
DELAYS = (3, 4, 5, 6)


def stream_member(fname):
    """Stream the single member of a tar.gz from the bucket into a bytearray (no disk)."""
    r = urllib.request.urlopen(BASE + fname, timeout=120)
    g = gzip.GzipFile(fileobj=r)
    t = tarfile.open(fileobj=g, mode="r|")
    m = next(iter(t))
    buf = bytearray(m.size)
    mv = memoryview(buf)
    fo = t.extractfile(m)
    pos = 0
    while pos < m.size:
        n = fo.readinto(mv[pos:pos + 2**24])
        if not n:
            raise IOError("short read")
        pos += n
    r.close()
    return m.name, m.size, buf


def keep_mask(n, block):
    """Boolean mask of samples kept: drop the first DISCARD s of each block."""
    k = np.ones(n, bool)
    for s in range(0, n, block):
        k[s:s + DISCARD] = False
    return k


def load_subject(subject):
    """Responses of the V1-V3B voxels of one subject.

    Returns a dict with rt (7200 x V), rv (540 x V), rva (10 x 540 x V), the linear voxel index
    `vox`, the area and hemisphere of each voxel, every ROI's voxel count, ei, and a few raw
    summaries over all 73,728 voxels.
    """
    name, size, buf = stream_member(f"VoxelResponses_subject{subject}.tar.gz")
    out = {"member": name, "member_bytes": size}
    with h5py.File(io.BytesIO(buf), "r") as f:
        out["layout"] = {k: (f[k].shape, str(f[k].dtype)) for k in ("rt", "rv", "rva")}
        out["ei"] = {k: f["ei"][k][()].ravel().tolist() for k in f["ei"]}
        rois = {k: f["roi"][k][()].ravel() for k in f["roi"]}
        out["roi_values"] = sorted(set(np.unique(np.concatenate(list(rois.values())))))
        out["roi_counts"] = {k: int((v > 0).sum()) for k, v in rois.items()}
        area = np.full(73728, "", object)
        hemi = np.full(73728, "", object)
        nlab = np.zeros(73728, int)
        for a in AREAS:
            for h in ("lh", "rh"):
                m = rois[a + h] > 0
                nlab[m] += 1
                area[m] = a
                hemi[m] = h
        # voxels in more than one of the V1-V3B masks
        out["n_multi_label"] = int((nlab > 1).sum())
        anyroi = np.zeros(73728, bool)
        for v in rois.values():
            anyroi |= v > 0
        vox = np.flatnonzero(nlab > 0)
        out["vox"], out["area"], out["hemi"] = vox, area[vox], hemi[vox]
        rt = np.empty((7200, len(vox)), np.float32)
        nan_rt_all = 0
        nan_rt_roi = 0
        step = 4096
        for s in range(0, 73728, step):
            blk = f["rt"][s:s + step]
            nan_rt_all += int(np.isnan(blk).any(1).sum())
            sel = (vox >= s) & (vox < s + step)
            rt[:, sel] = blk[vox[sel] - s].T
        out["n_nan_voxels_all_rt"] = nan_rt_all
        out["n_voxels_any_roi"] = int(anyroi.sum())
        out["rt"] = rt
        out["rv"] = f["rv"][()][vox].T.astype(np.float32)
        rva = np.empty((10, 540, len(vox)), np.float32)
        for s in range(0, 73728, step):
            sel = (vox >= s) & (vox < s + step)
            if sel.any():
                blk = f["rva"][s:s + step]
                rva[:, :, sel] = np.transpose(blk[vox[sel] - s], (1, 2, 0))
        out["rva"] = rva
    del buf
    return out


# ---------------------------------------------------------------- stimuli

def _resample_matrix(n_in, n_out):
    """Linear area-weighted resampling matrix (n_out x n_in): each output pixel is the mean of
    the input over its footprint (standard antialiased downsampling; cannot change a result)."""
    A = np.zeros((n_out, n_in))
    edges = np.linspace(0, n_in, n_out + 1)
    for i in range(n_out):
        a, b = edges[i], edges[i + 1]
        for j in range(int(np.floor(a)), int(np.ceil(b))):
            A[i, j] = max(0.0, min(b, j + 1) - max(a, j))
        A[i] /= A[i].sum()
    return A


def rgb_to_lab(rgb):
    """sRGB uint8 (..., 3) -> CIE L*a*b* (D65), as skimage.color.rgb2lab."""
    c = rgb.astype(np.float32) / 255.0
    c = np.where(c > 0.04045, ((c + 0.055) / 1.055) ** 2.4, c / 12.92)
    M = np.array([[0.412453, 0.357580, 0.180423],
                  [0.212671, 0.715160, 0.072169],
                  [0.019334, 0.119193, 0.950227]], np.float32)
    xyz = c @ M.T
    xyz /= np.array([0.95047, 1.0, 1.08883], np.float32)
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    L = np.where(xyz[..., 1] > 0.008856, 116 * np.cbrt(xyz[..., 1]) - 16, 903.3 * xyz[..., 1])
    a = 500 * (f[..., 0] - f[..., 1])
    b = 200 * (f[..., 1] - f[..., 2])
    return L, a, b


def load_stimuli(channels=("L",), chunk=1800):
    """Training and test frames, 96 x 96, in the CIE L*a*b* channels asked for (float16).

    Frames are downsampled from 128 to 96 pixels in RGB before conversion (Supplemental,
    Motion-Energy Encoding Model: "all movie frames are first spatially down-sampled to 96x96
    pixels. The RGB pixel values are then converted into ... CIE L*A*B*").
    """
    name, size, buf = stream_member("Stimuli.tar.gz")
    A = _resample_matrix(128, 96).astype(np.float32)
    out = {"member": name, "member_bytes": size}
    with h5py.File(io.BytesIO(buf), "r") as f:
        out["layout"] = {k: (f[k].shape, str(f[k].dtype)) for k in f.keys()}
        for key in ("st", "sv"):
            d = f[key]
            n = d.shape[0]
            res = {c: np.empty((n, 96, 96), np.float16) for c in channels}
            rng = [255, 0]
            for s in range(0, n, chunk):
                x = d[s:s + chunk]  # (n, 3, 128, 128) as stored; MATLAB order transposed
                rng = [min(rng[0], int(x.min())), max(rng[1], int(x.max()))]
                x = x.astype(np.float32)
                # stored (frame, rgb, w, h): MATLAB 128x128x3xN read in C order
                # rows of the image are the last stored axis (h), columns the third (w)
                x = A @ np.swapaxes(x, 2, 3) @ A.T  # (n, c, 96, 96), rows then columns
                x = np.moveaxis(x, 1, -1)
                x = np.clip(np.round(x), 0, 255)
                L, a, b = rgb_to_lab(x)
                for c, v in zip(("L", "a", "b"), (L, a, b)):
                    if c in res:
                        res[c][s:s + chunk] = v
            out[key] = res
            out[key + "_range"] = rng
    del buf
    return out


# ---------------------------------------------------------------- motion energy

def pyramid():
    import moten
    return moten.pyramids.MotionEnergyPyramid(
        stimulus_vhsize=(96, 96), stimulus_fps=15,
        spatial_frequencies=[0, 2, 4, 8, 16, 32])


def motion_energy(frames, filters, block=9000):
    """Log motion energy per frame, downsampled to 1 Hz by the mean over each second.

    Frames are processed in blocks (`block` frames: 9,000 for the 600 s training runs, 900 for
    the 60 s test blocks) so that no filter crosses a run boundary; within a block pymoten's
    batched projection overlaps its frame batches by the temporal filter width. The edge
    frames fall in the first 6 s of each block, which are discarded.
    """
    import moten
    n = frames.shape[0]
    out = np.empty((n // 15, len(filters)), np.float32)
    for s in range(0, n, block):
        x = frames[s:s + block].astype(np.float32)
        r = moten.core.project_stimulus_batched(
            x, filters, batch_size=512, stimulus_batch_size=min(900, len(x)), dtype="float32")
        out[s // 15:(s + len(x)) // 15] = r.reshape(-1, 15, r.shape[1]).mean(1)
    return out


def model_columns(filters, model):
    """Feature construction for the three models (Supplemental, Gabor Wavelet Basis Set).

    Returns a list of index arrays; each output feature is the sum of the listed filters.
    static: the 0 Hz filters. nondirectional: at each position, spatial frequency and
    orientation and temporal frequency > 0, the two opposite directions summed; 0 Hz filters
    kept. directional: every filter.
    """
    keys = []
    for i, f in enumerate(filters):
        keys.append((round(f["centerh"], 6), round(f["centerv"], 6), f["spatial_freq"],
                     f["temporal_freq"], f["direction"]))
    if model == "directional":
        return [np.array([i]) for i in range(len(filters))]
    if model == "static":
        return [np.array([i]) for i, k in enumerate(keys) if k[3] == 0]
    groups = {}
    for i, k in enumerate(keys):
        if k[3] == 0:
            groups[(k, i)] = [i]
        else:
            groups.setdefault(k[:4] + (k[4] % 180,), []).append(i)
    return [np.array(v) for v in groups.values()]


def build_features(me_train, me_test, cols):
    """Sum filters per model column, then z-score with training statistics and clip at 3."""
    def comb(me):
        return np.stack([me[:, c].sum(1) if len(c) > 1 else me[:, c[0]] for c in cols], 1)
    tr, te = comb(me_train), comb(me_test)
    mu, sd = tr.mean(0), tr.std(0)
    sd[sd == 0] = 1
    tr = np.clip((tr - mu) / sd, -3, 3).astype(np.float32)
    te = np.clip((te - mu) / sd, -3, 3).astype(np.float32)
    return tr, te


def delayed(X, delays, block):
    """Concatenate copies of X shifted by each delay (in samples) within blocks of `block`
    samples, zero before the block start, so a delay never crosses a run boundary."""
    n, p = X.shape
    out = np.zeros((n, p * len(delays)), np.float32)
    for j, d in enumerate(delays):
        for s in range(0, n, block):
            e = min(s + block, n)
            if d < e - s:
                out[s + d:e, j * p:(j + 1) * p] = X[s:e - d]
    return out


# ---------------------------------------------------------------- regression

def holdout_blocks(n_kept, rng, frac=0.1, size=50):
    """Held-out samples: 50 s blocks chosen at random until 10% are held out
    (Supplemental, Voxel Selection, paragraph 2)."""
    blocks = np.arange(0, n_kept, size)
    order = rng.permutation(len(blocks))
    held = np.zeros(n_kept, bool)
    for b in order:
        held[blocks[b]:blocks[b] + size] = True
        if held.sum() >= frac * n_kept:
            break
    return held


def _eig_kernel(Xtr):
    import scipy.linalg as sl
    K = Xtr @ Xtr.T
    w, U = sl.eigh(K, driver="evd")
    return np.clip(w, 0, None).astype(np.float32), U.astype(np.float32)


def kernel_ridge_path(Xtr, Ytr, Xev, alphas):
    """Predictions on Xev at each penalty of ridge regression fit on (Xtr, Ytr).

    Uses the eigendecomposition of the n x n kernel X X'. Returns (n_alpha, n_ev, V)."""
    w, U = _eig_kernel(Xtr)
    UtY = U.T @ Ytr
    Kev = (Xev @ Xtr.T) @ U
    return np.stack([(Kev * (1.0 / (w + a))) @ UtY for a in alphas])


def ridge_fit_predict(Xtr, Ytr, Xev, alpha_index, alphas, residuals=False):
    """Fit ridge with the penalty chosen per voxel (index into alphas); predict Xev.

    With residuals=True also returns the training residuals."""
    w, U = _eig_kernel(Xtr)
    UtY = U.T @ Ytr
    Kev = (Xev @ Xtr.T) @ U
    P = np.empty((Xev.shape[0], Ytr.shape[1]), np.float32)
    R = np.empty_like(Ytr) if residuals else None
    for ai, a in enumerate(alphas):
        sel = alpha_index == ai
        if sel.any():
            c = UtY[:, sel] / (w + a)[:, None]
            P[:, sel] = Kev @ c
            if residuals:
                R[:, sel] = Ytr[:, sel] - U @ (w[:, None] * c)
    return (P, R) if residuals else P


def corr_cols(a, b):
    """Column-wise Pearson correlation."""
    a = a - a.mean(0)
    b = b - b.mean(0)
    den = np.sqrt((a * a).sum(0) * (b * b).sum(0))
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(den > 0, (a * b).sum(0) / den, 0.0)


def identify(obs, pred, cov, lam):
    """Index of the candidate of maximum Gaussian log-likelihood for each observed pattern.

    obs (T x N), pred (C x N), cov (N x N) the training residual covariance; its inverse is
    estimated with Tikhonov regularization, inv(cov + lam * mean(diag) * I) (Supplemental,
    Likelihood Estimation)."""
    N = cov.shape[0]
    Pinv = np.linalg.inv(cov + lam * np.trace(cov) / N * np.eye(N, dtype=cov.dtype))
    a = pred @ Pinv
    # -(r - p) S (r - p)' up to the term in r alone
    ll = 2 * obs @ a.T - (a * pred).sum(1)[None, :]
    return ll.argmax(1)
