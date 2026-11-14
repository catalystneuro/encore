"""Loading and measures for CRCNS vim-2 (Nishimoto et al. 2011, Current Biology 21, 1641-1646).

The data set is not versioned (docs/archives.md, CRCNS); its files are read from the public S3
bucket crcnsarchive. Each file is a tar.gz holding one MATLAB 7.3 (HDF5) file. A gzip stream
cannot be read at random and h5py needs random access, so each member is streamed once
(HTTP -> gzip -> tar) into a buffer in memory and opened from there, without a copy; nothing is
written to disk. One large file is held at a time, and only the voxels or frames the analysis
needs are kept.

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
  by a factor of 2 inside the log offset, removed by the z-score (standard choice).
- Downsampling 15 Hz -> 1 Hz by the mean of the 15 frames of each second, z-score with the
  training statistics, clipping at 3 s.d.: Motion-Energy Encoding Model; the mean and the use of
  training statistics are the claims file's standard choices.
- Delays 3, 4, 5, 6 s (4 samples) and the single 4 s delay for decoding: Motion-Energy Encoding
  Model, last paragraph.
- Ridge regression in place of the paper's L1-regularized regression (an assumption, see the
  notebook); the penalty is chosen per voxel on a held-out 10% of the training data in 50 s
  blocks (claims file, Encoding model fit, reading a) or by 5-fold cross-validation over such
  blocks (reading b). The fits go through the kernel X X', which depends on the features only,
  so one eigendecomposition per model and split serves all three subjects.
- Probes for receptive fields and frequency tuning: Supplemental, Selectivity Estimation
  (17 x 17 grid of dynamic Gaussian white noise; full-field drifting gratings at the basis set's
  directions and frequencies; uniform gray as baseline). The noise contrast, the grating
  contrast, the gray level and the probe duration are not given; they are standard choices
  (L* 50 gray, noise s.d. 25 L*, grating amplitude 40 L*, 40 frames of which the middle 20 are
  scored), and only the shape of the predicted map is used.
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


class _BufferFile(io.RawIOBase):
    """Read-only, seekable file over a bytearray, without copying it (io.BytesIO copies)."""

    def __init__(self, buf):
        self._mv = memoryview(buf)
        self._pos = 0

    def readable(self):
        return True

    def seekable(self):
        return True

    def tell(self):
        return self._pos

    def seek(self, off, whence=0):
        base = (0, self._pos, len(self._mv))[whence]
        self._pos = base + off
        return self._pos

    def readinto(self, b):
        n = max(0, min(len(b), len(self._mv) - self._pos))
        b[:n] = self._mv[self._pos:self._pos + n]
        self._pos += n
        return n


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


def voxel_xyz(vox):
    """(x, y, z) of linear voxel indices in the 64 x 64 x 18 volume (ei.datasize), stored in
    MATLAB (column-major) order; z is the slice axis, which for the paper's 18 coronal slices
    (Experimental Procedures) runs posterior to anterior or the reverse."""
    vox = np.asarray(vox)
    return vox % 64, (vox // 64) % 64, vox // 4096


def load_subject(subject):
    """Responses of the V1-V3B voxels of one subject.

    Returns a dict with rt (7200 x V), rv (540 x V), rva (10 x 540 x V), the linear voxel index
    `vox`, the area and hemisphere of each voxel, every ROI's voxel count and mean slice, ei, and
    a few raw summaries over all 73,728 voxels.
    """
    name, size, buf = stream_member(f"VoxelResponses_subject{subject}.tar.gz")
    out = {"member": name, "member_bytes": size}
    with h5py.File(_BufferFile(buf), "r") as f:
        out["layout"] = {k: (f[k].shape, str(f[k].dtype)) for k in ("rt", "rv", "rva")}
        out["ei"] = {k: f["ei"][k][()].ravel().tolist() for k in f["ei"]}
        rois = {k: f["roi"][k][()].ravel() for k in f["roi"]}
        out["roi_values"] = sorted(set(np.unique(np.concatenate(list(rois.values())))))
        out["roi_counts"] = {k: int((v > 0).sum()) for k, v in rois.items()}
        out["roi_mean_slice"] = {k: float(voxel_xyz(np.flatnonzero(v > 0))[2].mean())
                                 for k, v in rois.items() if (v > 0).any()}
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


def frames_96(x):
    """Stored frames (n, rgb, w, h) uint8 -> (n, 96, 96, rgb) uint8, rows then columns.

    The MATLAB array 128 x 128 x 3 x N reads in C order as (N, 3, w, h): the image rows are the
    last stored axis, hence the swap. The orientation is shown on example frames in the
    notebook. Frames are downsampled from 128 to 96 pixels in RGB before conversion
    (Supplemental, Motion-Energy Encoding Model: "all movie frames are first spatially
    down-sampled to 96x96 pixels. The RGB pixel values are then converted into ... CIE L*A*B*").
    """
    A = _resample_matrix(128, 96).astype(np.float32)
    x = A @ np.swapaxes(x.astype(np.float32), 2, 3) @ A.T
    return np.clip(np.round(np.moveaxis(x, 1, -1)), 0, 255).astype(np.uint8)


def stimulus_motion_energy(filters, channels=("L",), chunk=1500, example_frames=()):
    """Motion energy at 1 Hz of the training and test movies, per CIE L*a*b* channel.

    The movies are read in blocks of one run (9,000 training frames, 900 test frames), so that
    no filter crosses a run boundary and only one block of frames is held. Returns
    {"st": {channel: (7200, F)}, "sv": {channel: (540, F)}}, the stored layout, the uint8 and
    L* ranges, and the 96 x 96 RGB frames listed in example_frames (training frame indices).
    """
    name, size, buf = stream_member("Stimuli.tar.gz")
    out = {"member": name, "member_bytes": size, "examples": {}}
    with h5py.File(_BufferFile(buf), "r") as f:
        out["layout"] = {k: (f[k].shape, str(f[k].dtype)) for k in f.keys()}
        for key, block in (("st", 9000), ("sv", 900)):
            d = f[key]
            n = d.shape[0]
            res = {c: np.empty((n // 15, len(filters)), np.float32) for c in channels}
            rng, lrng = [255, 0], [np.inf, -np.inf]
            for s in range(0, n, block):
                lab = {c: np.empty((block, 96, 96), np.float32) for c in channels}
                for s2 in range(s, s + block, chunk):
                    raw = d[s2:min(s2 + chunk, s + block)]
                    rng = [min(rng[0], int(raw.min())), max(rng[1], int(raw.max()))]
                    x = frames_96(raw)
                    if key == "st":
                        for i in example_frames:
                            if s2 <= i < s2 + chunk:
                                out["examples"][i] = x[i - s2]
                    L, a, b = rgb_to_lab(x)
                    lrng = [min(lrng[0], float(L.min())), max(lrng[1], float(L.max()))]
                    for c, v in zip(("L", "a", "b"), (L, a, b)):
                        if c in lab:
                            lab[c][s2 - s:s2 - s + len(v)] = v
                for c in channels:
                    res[c][s // 15:(s + block) // 15] = motion_energy(lab[c], filters, block)
                del lab
            out[key] = res
            out[key + "_range"] = rng
            out[key + "_L_range"] = lrng
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
    static: the 0 Hz filters. nondirectional: at each position, spatial frequency, spatial
    envelope, orientation and temporal frequency > 0, the two opposite directions summed. Filters
    at 0 Hz, and filters at 0 cycles/image (which have no direction, "zero spatial frequency
    filters occur only once (no orientation)", Gabor Wavelet Basis Set), are kept as they are.
    directional: every filter.
    """
    if model == "directional":
        return [np.array([i]) for i in range(len(filters))]
    if model == "static":
        return [np.array([i]) for i, f in enumerate(filters) if f["temporal_freq"] == 0]
    groups = {}
    for i, f in enumerate(filters):
        if f["temporal_freq"] == 0 or f["spatial_freq"] == 0:
            groups[("single", i)] = [i]
        else:
            k = (round(f["centerh"], 6), round(f["centerv"], 6), f["spatial_freq"],
                 round(f["spatial_env"], 6), f["temporal_freq"], f["direction"] % 180)
            groups.setdefault(k, []).append(i)
    return [np.array(v) for v in groups.values()]


def combine(me, cols):
    """Sum the filters of each model column."""
    return np.stack([me[:, c].sum(1) if len(c) > 1 else me[:, c[0]] for c in cols], 1)


def build_features(me_train, me_test, cols, return_stats=False):
    """Sum filters per model column, then z-score with training statistics and clip at 3."""
    tr, te = combine(me_train, cols), combine(me_test, cols)
    mu, sd = tr.mean(0), tr.std(0)
    sd[sd == 0] = 1
    tr = np.clip((tr - mu) / sd, -3, 3).astype(np.float32)
    te = np.clip((te - mu) / sd, -3, 3).astype(np.float32)
    return (tr, te, mu, sd) if return_stats else (tr, te)


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


def cv_folds(n_kept, rng, k=5, size=50):
    """Fold label of each sample: 50 s blocks assigned at random to k folds of near-equal size
    (claims file, Encoding model fit, reading b; the number of folds is a standard choice)."""
    blocks = np.arange(0, n_kept, size)
    lab = rng.permutation(np.arange(len(blocks)) % k)
    fold = np.empty(n_kept, int)
    for b, s in enumerate(blocks):
        fold[s:s + size] = lab[b]
    return fold


def eig_split(K, tr):
    """Eigendecomposition of the training block of the kernel K = X X'."""
    import scipy.linalg as sl
    w, U = sl.eigh(K[np.ix_(tr, tr)], driver="evd")
    return np.clip(w, 0, None).astype(np.float32), U.astype(np.float32)


def ridge_path_corr(w, U, Kev, Ytr, Yev, alphas):
    """Correlation of the held-out prediction with Yev, per penalty (rows) and voxel (columns),
    for ridge fit through the kernel: Kev is K[ev][:, tr], (w, U) the eigensystem of K[tr][:, tr].
    """
    UtY = U.T @ Ytr
    KU = Kev @ U
    return np.stack([corr_cols((KU * (1.0 / (w + a))) @ UtY, Yev) for a in alphas])


def ridge_dual(w, U, Ytr, alpha_index, alphas):
    """Dual coefficients C (n_tr x V) of ridge with a penalty per voxel: weights are X' C,
    predictions K[ev][:, tr] C."""
    UtY = U.T @ Ytr
    C = np.empty_like(Ytr)
    for ai, a in enumerate(alphas):
        sel = alpha_index == ai
        if sel.any():
            C[:, sel] = U @ (UtY[:, sel] / (w + a)[:, None])
    return C


def corr_cols(a, b):
    """Column-wise Pearson correlation."""
    a = a - a.mean(0)
    b = b - b.mean(0)
    den = np.sqrt((a * a).sum(0) * (b * b).sum(0))
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(den > 0, (a * b).sum(0) / den, 0.0)


def corr_pvalue(r, n):
    """Two-sided p of a Pearson correlation on n samples (t test)."""
    from scipy import stats
    r = np.clip(np.asarray(r, float), -0.999999, 0.999999)
    t = r * np.sqrt((n - 2) / (1 - r * r))
    return 2 * stats.t.sf(np.abs(t), n - 2)


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


# ---------------------------------------------------------------- probes

GRAY = 50.0  # L* of the uniform gray baseline (standard choice)


def probe_features(movies, filters, mu, sd, cols, n_keep=(10, 30)):
    """Model features of probe movies (list of (frames, 96, 96) L* arrays, all of one length,
    projected one after the other): log motion energy per frame, averaged over frames
    n_keep[0]..n_keep[1] of each movie (away from both ends, which the 10-frame filters see
    across), summed per model column and z-scored and clipped with the
    training statistics, as the training features. A probe held for many seconds drives every
    delay alike, so its predicted response is the features times the weights summed over
    delays."""
    import moten
    n = movies[0].shape[0]
    x = np.concatenate(movies).astype(np.float32)
    r = moten.core.project_stimulus_batched(
        x, filters, batch_size=512, stimulus_batch_size=min(900, len(x)), dtype="float32")
    me = r.reshape(len(movies), n, -1)[:, n_keep[0]:n_keep[1]].mean(1)
    return np.clip((combine(me, cols) - mu) / sd, -3, 3).astype(np.float32)


def noise_probes(rng, grid=17, n_frames=40, size=96, sd=25.0):
    """Dynamic Gaussian white noise in each cell of a grid x grid tiling of the display
    (Selectivity Estimation), on uniform gray; one movie per cell, row by row from the top
    left. Pixel noise s.d. in L* units is a standard choice."""
    edges = np.round(np.linspace(0, size, grid + 1)).astype(int)
    movies = []
    for i in range(grid):
        for j in range(grid):
            m = np.full((n_frames, size, size), GRAY, np.float32)
            h, w = edges[i + 1] - edges[i], edges[j + 1] - edges[j]
            m[:, edges[i]:edges[i + 1], edges[j]:edges[j + 1]] = np.clip(
                GRAY + sd * rng.standard_normal((n_frames, h, w)), 0, 100)
            movies.append(m)
    return movies


def grating_probes(sfs, tfs, directions, n_frames=40, size=96, fps=15, amp=40.0):
    """Full-field drifting gratings at the basis set's spatial frequencies (cycles/image),
    temporal frequencies (Hz) and directions (degrees), Selectivity Estimation. At 0 cycles/
    image the grating is a full-field flicker (direction has no effect). Returns movies and
    their (sf, tf, direction) labels."""
    yy, xx = np.mgrid[0:size, 0:size] / size
    t = np.arange(n_frames) / fps
    movies, labels = [], []
    for sf in sfs:
        for tf in tfs:
            for d in directions:
                th = np.deg2rad(d)
                ph = 2 * np.pi * sf * (xx * np.cos(th) - yy * np.sin(th))
                m = GRAY + amp * np.cos(ph[None] - 2 * np.pi * tf * t[:, None, None])
                movies.append(m.astype(np.float32))
                labels.append((sf, tf, d))
    return movies, labels


def gaussian_fit(maps, grid=17, centers=np.arange(-8.0, 24.5, 0.5),
                 sigmas=(0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0)):
    """Fit a 2D isotropic Gaussian plus offset to each spatial map (V x grid*grid, row by row)
    by searching centers and widths on a grid (in cell units, cell centers at 0..grid-1) and
    solving amplitude and offset by least squares; the template of highest positive
    correlation is chosen. Returns row, column and sigma of the center (cell units) and the
    correlation of map and fit."""
    gy, gx = np.mgrid[0:grid, 0:grid]
    gy, gx = gy.ravel().astype(np.float32), gx.ravel().astype(np.float32)
    M = maps - maps.mean(1, keepdims=True)
    M /= np.linalg.norm(M, axis=1, keepdims=True) + 1e-12
    best = np.full(len(maps), -np.inf, np.float32)
    par = np.zeros((len(maps), 3), np.float32)
    cy, cx = np.meshgrid(centers, centers, indexing="ij")
    cy, cx = cy.ravel(), cx.ravel()
    for s in sigmas:
        T = np.exp(-((gy[None] - cy[:, None]) ** 2 + (gx[None] - cx[:, None]) ** 2) / (2 * s * s))
        T = T - T.mean(1, keepdims=True)
        nrm = np.linalg.norm(T, axis=1)
        ok = nrm > 1e-6
        T = (T[ok] / nrm[ok, None]).astype(np.float32)
        c = M @ T.T
        k = c.argmax(1)
        v = c[np.arange(len(maps)), k]
        upd = v > best
        best[upd] = v[upd]
        par[upd] = np.stack([cy[ok][k[upd]], cx[ok][k[upd]], np.full(upd.sum(), s)], 1)
    return par[:, 0], par[:, 1], par[:, 2], best
