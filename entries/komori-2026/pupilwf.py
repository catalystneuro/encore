"""Helpers for testing Komori et al. (2026) on the resting-state recordings of DANDI:001425.

The paper (bioRxiv doi:10.64898/2026.05.27.726399) decodes spontaneous pupil dilation from
independent components (ICs) of wide-field calcium imaging with a GRU, on resting-state recordings
of Kondo et al. (2025), DANDI:001425. The claims file (claims/komori-2026.yaml) names the open
details R1 to R10 in its opening comment; each parameter below says where it comes from:
[claim] the claims file's criterion or opening comment, [paper] a passage of the paper,
[assumption] a choice the paper leaves open (with the reason), [standard] a choice that cannot
change a result.

Everything is streamed from the archive (fsspec HTTP range reads into h5py); nothing is written
to disk.
"""
from __future__ import annotations

import os
import re
import sys
import zlib

# [standard] The same numerical kernels on every x86-64 machine. The ICA lands on different
# solutions when its input differs in the last bits, and the GRU fits drift apart likewise, so a
# run on another processor (AVX-512 or not) gave other ICs and other AUCs. The linear algebra
# (OpenBLAS in numpy and scipy, MKL in torch), numpy's own vector loops and torch's are pinned
# to their AVX2 code, which every machine that runs the registry has. This must happen before
# numpy is first imported: import pupilwf first. The L2 cache size is given because numpy's
# OpenBLAS, pinned to Haswell, crashes in matrix products when it detects the cache of an AMD Zen 5
# processor itself; the size given does not change the results (the same bits at 0.5, 1 and 2 MiB).
KERNELS = {"OPENBLAS_CORETYPE": "Haswell", "OPENBLAS_L2_SIZE": "1048576",
           "NPY_DISABLE_CPU_FEATURES": "X86_V4 AVX512_ICL",
           "ATEN_CPU_CAPABILITY": "avx2", "MKL_CBWR": "AVX2,STRICT", "ONEDNN_MAX_CPU_ISA": "AVX2"}
if "numpy" in sys.modules and any(os.environ.get(k) != v for k, v in KERNELS.items()):
    raise RuntimeError("import pupilwf before numpy, so that its kernel settings take effect")
os.environ.update(KERNELS)

import numpy as np
from scipy import signal, ndimage, stats

DANDISET = "001425"
VERSION = "0.250705.0947"  # most recent published version; the paper cites none
API = "https://api.dandiarchive.org/api"
PAPER_KEY = "komori-2026"

FS = 30.0             # imaging frames per second per excitation channel (file: imaging_rate 30.0)
WINDOW = 46           # [paper] Methods, Machine learning, Overview: "46 frames for resting-state data"
EPOCH_S = 40.0        # [paper] Methods, Pupil labels: "40 s epochs spanning 50-570 s"
EPOCH_START, EPOCH_END = 50.0, 570.0
PUPIL_LP = 0.2        # [paper] Methods, Pupil labels: "low-pass filtered at 0.2 Hz" for resting data
LABEL_PRE, LABEL_POST = 3.0, 0.5   # [paper] "the window from 3 s before to 0.5 s after the ... peak"
THRESH = 0.6          # [paper] "binarized at 0.6"
F0_WINDOW = (5.0, 15.0)  # [paper] Methods, Hemodynamic correction: "mean intensity ... 5-15 s after onset"
N_HEMO_SVD = 34       # [paper] "SVD ... to extract 34 spatial components"
HEMO_HP = 0.1         # [paper] "A 0.1 Hz high-pass filter was applied to both signals prior to regression"
N_SVD = 400           # [paper] Methods, ICA-based features: "SVD retaining 400 components"
N_SVD_ICA = 200       # [paper] "ICA was applied to the top 200 SVD temporal components"
N_ICA = 30            # [paper] "The target number of ICs was 30"
EVERY = 5             # [paper] "every fifth session was used to estimate the ICA decomposition"
VIF_MAX = 10.0        # [paper] "ICs were iteratively removed until the maximum VIF ... fell below 10"
BIN = 2               # [standard] 2x2 spatial binning of the 288x288 frames (144x144) for memory;
                      # the components are smooth at this scale. Recorded as a deviation.
GRID_STEP = 4         # [standard] common atlas grid: the 512x512 atlas sampled every 4 pixels


def seed_of(claim_id: str) -> int:
    """The claim's seed (protocol, Author step 3)."""
    return zlib.crc32(f"{PAPER_KEY}/{claim_id}".encode())


# --- archive -----------------------------------------------------------------------------------

def list_assets(version=VERSION):
    import requests
    url = f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=1000"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r["next"]
    return out


def s3_url(asset_id: str) -> str:
    import requests
    r = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60)
    return r.url


def open_nwb(asset_id: str, block_mb: int = 64):
    import fsspec
    import h5py
    fh = fsspec.filesystem("http").open(s3_url(asset_id), block_size=block_mb * 2**20,
                                        cache_type="readahead")
    return h5py.File(fh, "r")


def resting_table(assets):
    """One row per resting-state NWB file: subject, date, day label, whether it holds behaviour."""
    rows = []
    for a in assets:
        p = a["path"]
        if not p.endswith(".nwb") or "resting-state" not in p:
            continue
        m = re.search(r"sub-(VG1-GC#\d+)_ses-(\d{4}-\d{2}-\d{2})-resting-state-(day\d+)_(widefield(?:\+behavior)?)\.nwb", p)
        rows.append(dict(subject=m.group(1), date=m.group(2), day=m.group(3),
                         behavior=m.group(4) == "widefield+behavior", path=p,
                         asset_id=a["asset_id"], size_gb=a["size"] / 1e9))
    rows.sort(key=lambda r: (int(r["subject"].split("#")[1]), r["date"]))
    return rows


def choose_sessions(rows, n_mice=3, n_sessions=3):
    """[claim] R1 reading (a): three mice, their first 2 or 3 resting sessions in recording order.
    [assumption] Which three mice the paper used is not said. Mice are ordered by the date of
    their first resting session, then by their number, and the first three whose first
    `n_sessions` resting sessions all hold the pupil (widefield+behavior files) are taken."""
    by = {}
    for r in rows:
        by.setdefault(r["subject"], []).append(r)
    cands = []
    for s, rs in by.items():
        rs = sorted(rs, key=lambda r: r["date"])
        first = rs[:n_sessions]
        if len(first) == n_sessions and all(r["behavior"] for r in first):
            cands.append((rs[0]["date"], int(s.split("#")[1]), s, first))
    cands.sort()
    return [c[3] for c in cands[:n_mice]]


# --- filters -----------------------------------------------------------------------------------

def butter(x, cutoff, kind="low", fs=FS, order=4, axis=0):
    """4th-order Butterworth applied forward and backward [claim: opening comment, code read by
    the reader: 'Low-pass filters are 4th-order Butterworth, applied forward and backward']."""
    sos = signal.butter(order, cutoff, btype=kind, fs=fs, output="sos")
    return signal.sosfiltfilt(sos, x, axis=axis)


def fill_nan(x):
    x = np.asarray(x, dtype=np.float64).copy()
    bad = ~np.isfinite(x)
    if bad.any():
        idx = np.arange(len(x))
        x[bad] = np.interp(idx[bad], idx[~bad], x[~bad])
    return x, int(bad.sum())


# --- per-session reduction -----------------------------------------------------------------------

def _read_binned(ds, mask_b, block=600):
    """Stream a (T, 288, 288) uint16 dataset in blocks, bin 2x2, keep the masked pixels (float32)."""
    T = ds.shape[0]
    out = np.empty((T, int(mask_b.sum())), dtype=np.float32)
    for i in range(0, T, block):
        x = ds[i:i + block].astype(np.float32)
        n, h, w = x.shape
        x = x.reshape(n, h // BIN, BIN, w // BIN, BIN).mean(axis=(2, 4))
        out[i:i + n] = x[:, mask_b]
    return out


def atlas_grid_coords(affine, shape_b):
    """Data coordinates (binned pixels) of the common atlas grid points.
    The file's affine maps 512x512 atlas (x=column, y=row) to 288x288 data (x, y); the convention
    is checked in the notebook by the overlap of the warped ROI masks across sessions."""
    g = np.arange(0, 512, GRID_STEP, dtype=np.float64)
    ay, ax = np.meshgrid(g, g, indexing="ij")
    A = np.asarray(affine, dtype=np.float64).reshape(2, 3)
    dx = A[0, 0] * ax + A[0, 1] * ay + A[0, 2]
    dy = A[1, 0] * ax + A[1, 1] * ay + A[1, 2]
    # binned pixel centres: data pixel p maps to (p + 0.5) / BIN - 0.5
    return (dy + 0.5) / BIN - 0.5, (dx + 0.5) / BIN - 0.5


def warp_maps(maps_b, coords, order=1):
    """Sample (k, H, W) maps at the atlas grid; returns (k, G, G)."""
    ry, rx = coords
    return np.stack([ndimage.map_coordinates(m, [ry, rx], order=order, mode="constant", cval=np.nan)
                     for m in maps_b])


def reduce_session(row, hemo_variant="fit_hp_subtract_raw", verbose=True):
    """Read one resting session and reduce it to what the analysis needs.

    Hemodynamic correction [paper, Methods, Hemodynamic correction]: dF/F to the mean of 5-15 s,
    SVD (34 components), F480 regressed on F405 by OLS after a 0.1 Hz high-pass, the estimate
    subtracted. [assumption] The paper computes the SVD for both channels without saying how;
    here the SVD is of the 470 nm dF/F, and both channels are projected on its spatial
    components, so the regression is per component. [assumption] The Methods fit the regression
    on high-passed signals and subtract the estimate "from the measured F480"; the main reading
    applies the fitted coefficients to the unfiltered signals (hemo_variant
    'fit_hp_subtract_raw'); the other keeps the high-passed corrected signal ('hp_corrected').
    Both are returned.
    """
    import time
    t0 = time.time()
    f = open_nwb(row["asset_id"])
    masks = f["processing/ophys/ImageSegmentation/ROIs/image_mask"][:]
    names = [x.decode() for x in f["processing/ophys/ImageSegmentation/ROIs/roi_name"][:]]
    affine = f["analysis/atlas_to_data_transform/affine_matrix"][:][0]
    tb = f["acquisition/widefield_blue/timestamps"][:]
    tv = f["acquisition/widefield_UV/timestamps"][:]
    tp = f["processing/downsampled/pupil_tracking/diameter/timestamps"][:]
    pupil_raw = f["processing/downsampled/pupil_tracking/diameter/data"][:]
    dff_dep = f["processing/ophys/DfOverF/dFF/data"][:]
    td = f["processing/ophys/DfOverF/dFF/timestamps"][:]
    # cortex mask: the union of the 44 atlas ROIs, minus the olfactory bulb [paper: "non-cortical
    # pixels were masked"]
    cortex = np.zeros(masks.shape[1:], bool)
    for m, n in zip(masks, names):
        if not n.startswith("OB"):
            cortex |= m
    h, w = cortex.shape
    cortex_b = cortex.reshape(h // BIN, BIN, w // BIN, BIN).mean(axis=(1, 3)) >= 0.5
    blue = _read_binned(f["acquisition/widefield_blue/data"], cortex_b)
    t_read_b = time.time() - t0
    uv = _read_binned(f["acquisition/widefield_UV/data"], cortex_b)
    t_read = time.time() - t0
    raw_mean_b, raw_mean_v = float(blue.mean()), float(uv.mean())
    rel = tb - tb[0]
    f0 = (rel >= F0_WINDOW[0]) & (rel < F0_WINDOW[1])
    for x in (blue, uv):
        base = x[f0].mean(axis=0)
        x /= base
        x -= 1.0
    # SVD of the 470 nm dF/F (randomized, 34 components)
    from sklearn.utils.extmath import randomized_svd
    U, S, Vt = randomized_svd(blue, N_HEMO_SVD, n_iter=4, random_state=0)  # [standard] seed
    # spatial components = rows of Vt (34 x pixels); temporal = projections
    P = Vt.astype(np.float32)
    Vb = blue @ P.T
    Vv = uv @ P.T
    var_b = resid_b = 0.0
    for i in range(0, len(blue), 2000):
        var_b += float((blue[i:i + 2000].astype(np.float64) ** 2).sum())
        resid_b += float(((blue[i:i + 2000] - Vb[i:i + 2000] @ P) ** 2).sum())
    del blue, uv
    Vb = Vb.astype(np.float64)
    Vv = Vv.astype(np.float64)
    hb = butter(Vb, HEMO_HP, "high")
    hv = butter(Vv, HEMO_HP, "high")
    coef = np.empty((N_HEMO_SVD, 2))
    corr_raw = np.empty_like(Vb)
    corr_hp = np.empty_like(Vb)
    for k in range(N_HEMO_SVD):
        X = np.column_stack([hv[:, k], np.ones(len(hv))])
        beta, *_ = np.linalg.lstsq(X, hb[:, k], rcond=None)
        coef[k] = beta
        corr_hp[:, k] = hb[:, k] - X @ beta
        corr_raw[:, k] = Vb[:, k] - beta[0] * Vv[:, k]
    # spatial maps in binned image space, then on the atlas grid
    maps_b = np.zeros((N_HEMO_SVD,) + cortex_b.shape, np.float32)
    maps_b[:, cortex_b] = P
    coords = atlas_grid_coords(affine, cortex_b.shape)
    maps_atlas = warp_maps(maps_b, coords)
    roi_b = np.stack([m.reshape(h // BIN, BIN, w // BIN, BIN).mean(axis=(1, 3)) for m in masks])
    roi_atlas = warp_maps(roi_b, coords) >= 0.5
    pupil, n_nan = fill_nan(pupil_raw)
    out = dict(
        subject=row["subject"], date=row["date"], day=row["day"], path=row["path"],
        t=tb - tb[0], t_uv_offset=float(np.median(tv - tb)), pupil=pupil, pupil_nan=n_nan,
        pupil_t_equal=bool(np.array_equal(tp, tb)), dff_t_equal=bool(np.array_equal(td, tb)),
        V={"fit_hp_subtract_raw": corr_raw, "hp_corrected": corr_hp, "uncorrected": Vb},
        maps_atlas=maps_atlas, roi_atlas=roi_atlas, roi_names=names, affine=affine,
        dff_deposited=dff_dep, coef=coef, svd_var_explained=1 - resid_b / var_b,
        n_frames=len(tb), n_pixels=int(cortex_b.sum()), raw_mean=(raw_mean_b, raw_mean_v),
        read_s=t_read, read_blue_s=t_read_b, total_s=time.time() - t0)
    f.close()
    if verbose:
        print(f"{row['subject']} {row['day']}: {len(tb)} frames, {out['n_pixels']} pixels, "
              f"read {t_read:.0f} s, total {out['total_s']:.0f} s, 34-SVD explains "
              f"{out['svd_var_explained']:.3f} of dF/F variance")
    return out


# --- global SVD and ICA ----------------------------------------------------------------------

def epochs_of(t):
    """[paper] 13 epochs of 40 s spanning 50-570 s; frame index ranges."""
    starts = np.arange(EPOCH_START, EPOCH_END - 1e-9, EPOCH_S)
    return [(int(np.searchsorted(t, s)), int(np.searchsorted(t, s + EPOCH_S))) for s in starts]


MAX_SWEEPS = 2000


def jade(X, m, rotation_seed=None):
    """JADE ICA (Cardoso), a port of jadeR (https://github.com/gbeckers/jadeR) [paper: Methods, ICA].
    X: (n_sensors, T) array. Returns B (m x n_sensors) so that B @ X are the m sources, whitened
    (unit variance), sorted by decreasing norm of their mixing columns, as jadeR does.
    rotation_seed: None starts the joint diagonalisation from the whitened data, as jadeR does;
    a seed first rotates the whitened data by a random orthogonal matrix, a restart of the
    algorithm from another starting point [standard: ICA restarts, to show how far the
    decomposition depends on where it starts]."""
    X = np.asarray(X, dtype=np.float64)
    n, T = X.shape
    X = X - X.mean(axis=1, keepdims=True)
    # whitening by PCA to m components
    D, U = np.linalg.eigh((X @ X.T) / T)
    k = np.argsort(D)[::-1][:m]
    PCs = U[:, k]
    scales = np.sqrt(D[k])
    B = (PCs / scales).T          # m x n
    X = B @ X                     # m x T, whitened
    if rotation_seed is not None:
        Qr, _ = np.linalg.qr(np.random.default_rng(rotation_seed).normal(size=(m, m)))
        X = Qr @ X
        B = Qr @ B
    # cumulant matrices
    nbcm = m * (m + 1) // 2
    CM = np.zeros((m, m * nbcm))
    R = np.eye(m)
    Xt = X.T
    Range = np.arange(m)
    for im in range(m):
        Xim = X[im]
        Xijm = Xim * Xim
        Qij = ((Xijm * X) @ Xt) / T - R - 2 * np.outer(R[:, im], R[:, im])
        CM[:, Range] = Qij
        Range = Range + m
        for jm in range(im):
            Xijm = Xim * X[jm]
            Qij = np.sqrt(2) * (((Xijm * X) @ Xt) / T - np.outer(R[:, im], R[:, jm])
                                - np.outer(R[:, jm], R[:, im]))
            CM[:, Range] = Qij
            Range = Range + m
    # joint diagonalisation
    V = np.eye(m)
    seuil = 1e-6 / np.sqrt(T)
    encore = True
    sweep = 0
    # [paper] jadeR sweeps until no rotation exceeds the threshold, with no cap. The cap here is
    # far above what is needed (the main decomposition converges in about 150 sweeps); an earlier
    # cap of 100 stopped before convergence, which left the ICs dependent on the last bits.
    while encore and sweep < MAX_SWEEPS:
        encore = False
        sweep += 1
        for p in range(m - 1):
            for q in range(p + 1, m):
                Ip = np.arange(p, m * nbcm, m)
                Iq = np.arange(q, m * nbcm, m)
                g = np.vstack([CM[p, Ip] - CM[q, Iq], CM[p, Iq] + CM[q, Ip]])
                gg = g @ g.T
                ton = gg[0, 0] - gg[1, 1]
                toff = gg[0, 1] + gg[1, 0]
                theta = 0.5 * np.arctan2(toff, ton + np.sqrt(ton * ton + toff * toff))
                if abs(theta) > seuil:
                    encore = True
                    c, s = np.cos(theta), np.sin(theta)
                    G = np.array([[c, -s], [s, c]])
                    pair = [p, q]
                    V[:, pair] = V[:, pair] @ G
                    CM[pair, :] = G.T @ CM[pair, :]
                    CM[:, np.concatenate([Ip, Iq])] = np.hstack(
                        [c * CM[:, Ip] + s * CM[:, Iq], -s * CM[:, Ip] + c * CM[:, Iq]])
    if encore:
        raise RuntimeError(f"JADE did not converge in {MAX_SWEEPS} sweeps")
    jade.sweeps = sweep
    B = V.T @ B
    A = np.linalg.pinv(B)
    order = np.argsort((A ** 2).sum(axis=0))[::-1]
    B = B[order]
    # signs: first column of B positive, as jadeR
    signs = np.sign(B[:, 0])
    signs[signs == 0] = 1
    return B * signs[:, None]


def common_mask(sessions):
    m = None
    for s in sessions:
        ok = np.isfinite(s["maps_atlas"]).all(axis=0) & (np.abs(s["maps_atlas"]).sum(axis=0) > 0)
        cortex = s["roi_atlas"][[i for i, n in enumerate(s["roi_names"]) if not n.startswith("OB")]].any(axis=0)
        ok &= cortex
        m = ok if m is None else (m & ok)
    return m


def decompose(sessions, hemo="fit_hp_subtract_raw", n_svd=N_SVD, n_svd_ica=N_SVD_ICA, n_ica=N_ICA,
              rotation_seed=None, scaling="code"):
    """Pixel-wise Z-scored images (per session) -> SVD on every fifth epoch -> JADE ICA.
    [paper code] scaling 'code' (main): the SVD temporal components are the projections of the
    frames on the spatial basis, U S, as in the paper's code (#03_ica/#01_svd.ipynb,
    normalize_svd: svt = frames @ VT.T @ inv(VT VT.T); commit 405a720), and jadeR's reduction to
    the target number of ICs then keeps the leading SVD components. scaling 'methods': each
    component divided by its singular value, as the Methods write ("obtained by dividing each
    component by its corresponding singular value"). On the frames the SVD was fitted to, those
    components are orthonormal, so their covariance is the identity and the 30 dimensions jadeR
    keeps out of 200 are set by rounding alone; this reading gives different ICs on different
    machines and is shown only to document that (eig_gap: the ratio of the 30th to the 31st
    eigenvalue of the covariance jadeR reduces).
    [standard] The inputs are rounded to float32 and the decomposition runs on one thread, with
    the kernels pinned (KERNELS), so that the same data give the same ICs on any machine.
    [paper] Methods, ICA-based cortical features. [assumption] For resting data the unit of
    "every fifth session" is the 40 s epoch (the resting analogue of a 40 s session); pixel
    Z-scoring uses each recording's own mean and SD. The data of a recording are of rank 34 after
    the hemodynamic correction, so the SVD keeps min(400, 34 x recordings) components."""
    from threadpoolctl import threadpool_limits
    with threadpool_limits(1):
        return _decompose(sessions, hemo, n_svd, n_svd_ica, n_ica, rotation_seed, scaling)


def _decompose(sessions, hemo, n_svd, n_svd_ica, n_ica, rotation_seed, scaling="code"):
    mask = common_mask(sessions)
    Ws, Vc, sel = [], [], []
    g = 0
    for s in sessions:
        V = s["V"][hemo].astype(np.float32).astype(np.float64)
        mu = V.mean(axis=0)
        Vcen = V - mu
        M = s["maps_atlas"][:, mask].astype(np.float32).astype(np.float64)       # 34 x P
        C = (Vcen.T @ Vcen) / len(Vcen)
        sd = np.sqrt(np.einsum("kp,kl,lp->p", M, C, M))
        W = M / sd                                          # 34 x P, z-scored maps
        ep = epochs_of(s["t"])
        idx = []
        for (a, b) in ep:
            if g % EVERY == 0:
                idx.append(np.arange(a, b))
            g += 1
        idx = np.concatenate(idx) if idx else np.array([], int)
        Ws.append(W)
        Vc.append(Vcen)
        sel.append(idx)
    # X = sum_s W_s^T Vsel_s^T : P x Tsel ; build a factor with the same left singular vectors
    blocks = []
    for W, V, idx in zip(Ws, Vc, sel):
        if len(idx) == 0:
            continue
        Q, Rr = np.linalg.qr(V[idx])             # Tsel x 34, 34 x 34
        blocks.append(W.T @ Rr.T)                # P x 34
    Mfac = np.hstack(blocks)
    Us, Ss, _ = np.linalg.svd(Mfac, full_matrices=False)
    k = min(n_svd, int((Ss > Ss[0] * 1e-10).sum()))
    Us, Ss = Us[:, :k], Ss[:k]
    var = Ss ** 2
    cum = np.cumsum(var) / var.sum()
    # temporal components of every frame of every session, divided by the singular values
    sc = Ss if scaling == "methods" else np.ones_like(Ss)
    temporal = [(V @ W @ Us) / sc for W, V in zip(Ws, Vc)]
    k2 = min(n_svd_ica, k)
    Xica = np.vstack([tc[idx, :k2] for tc, idx in zip(temporal, sel) if len(idx)])
    ev = np.sort(np.linalg.eigvalsh(np.cov(Xica.T)))[::-1]
    eig_gap = float(ev[n_ica - 1] / ev[n_ica])
    B = jade(Xica.T, n_ica, rotation_seed)
    ics = [tc[:, :k2] @ B.T for tc in temporal]
    # whiten on the decomposition frames
    allsel = np.vstack([ic[idx] for ic, idx in zip(ics, sel) if len(idx)])
    mu, sd = allsel.mean(axis=0), allsel.std(axis=0)
    ics = [(ic - mu) / sd for ic in ics]
    A = np.linalg.pinv(B) * sd                  # k2 x n_ica mixing, in units of the ICs
    spatial = (Us[:, :k2] * sc[:k2]) @ A         # P x n_ica
    maps = np.full((n_ica,) + mask.shape, np.nan)
    maps[:, mask] = spatial.T
    return dict(mask=mask, ics=ics, maps=maps, n_svd=k, cum_var=cum, n_sel_frames=len(Xica),
                svd_sv=Ss, sweeps=jade.sweeps, eig_gap=eig_gap)


def compactness(maps, mask):
    """[assumption] The paper keeps "ICs with spatially coherent and anatomically interpretable
    spatial components ... by visual inspection". As a repeatable stand-in, an IC map's
    compactness is the share of its squared weight that lies in its largest connected region
    of pixels above half its peak absolute value (sign taken at the peak)."""
    out = []
    for m in maps:
        x = np.where(mask, m, 0.0)
        pk = x.flat[np.nanargmax(np.abs(x))]
        x = x * np.sign(pk)
        hi = x >= 0.5 * np.nanmax(x)
        lab, n = ndimage.label(hi)
        if n == 0:
            out.append(0.0)
            continue
        e = np.array([(x[lab == i] ** 2).sum() for i in range(1, n + 1)])
        out.append(float(e.max() / (np.where(mask, m, 0.0) ** 2).sum()))
    return np.array(out)


def vif(X, centred=False):
    """VIF of each column, 1/(1-R2) of the column regressed on the others [paper: Methods,
    Permutation importance]. The paper's code (#05_deep_learning/#07_vif_calc.ipynb, commit
    405a720, compute_vif_time) calls statsmodels variance_inflation_factor on the features as
    they are, with no constant column, so the regression has no intercept and R2 is uncentred:
    VIF_j = (x_j'x_j) [(X'X)^-1]_jj. That is the default here. centred=True gives the VIF with an
    intercept (inverse correlation matrix), shown as a variant."""
    X = np.asarray(X, dtype=np.float64)
    if centred:
        C = np.corrcoef(X, rowvar=False)
        return np.diag(np.linalg.pinv(C))
    G = X.T @ X
    return np.diag(G) * np.diag(np.linalg.pinv(G))


def select_ics(feats, comp, n, reading="kept", centred=False):
    """IC selection [claim R6, rest-ic-count-and-window readings (a) and (b)].
    feats: (frames, n_ica) filtered features used for VIF. Candidates are ordered by compactness.
    reading 'initial' (b): the n most compact, then the one with the highest VIF removed until
    the maximum VIF < 10. reading 'kept' (a): as (b), then the next most compact ICs are added
    one at a time, each kept only if the maximum VIF stays below 10, until n are kept.
    The VIF is that of the paper's code (uncentred) unless centred=True."""
    order = list(np.argsort(comp)[::-1])
    keep = order[:n]
    removed = []
    while len(keep) > 1:
        v = vif(feats[:, keep], centred)
        if v.max() < VIF_MAX:
            break
        removed.append(keep.pop(int(np.argmax(v))))
    if reading == "kept":
        for c in order[n:]:
            if len(keep) >= n:
                break
            if c in removed:
                continue
            v = vif(feats[:, keep + [c]], centred)
            if v.max() < VIF_MAX:
                keep.append(c)
    return keep, removed


# --- labels and samples --------------------------------------------------------------------

def pupil_norm(p):
    """[paper] Pupil low-pass 0.2 Hz, Z-scored and min-max normalised with the whole recording."""
    x = butter(p, PUPIL_LP, "low")
    x = (x - x.mean()) / x.std()
    return (x - x.min()) / (x.max() - x.min())


def epoch_labels(t, pn, sample_reading="window", selection="none"):
    """Per epoch: the peak of the normalised pupil, the label frames and the sample frames.
    [claim R4] reading 'window' (a): samples are the frames from 3 s before to 0.5 s after the
    peak; reading 'epoch' (b): every frame of the epoch is a sample, positive only inside that
    window. [claim R5] 'none' (a) or 'rule' (b): keep epochs with more than 10 positive frames and
    no positive frame earlier than 1.5 s before the peak."""
    out = []
    n_pre, n_post = int(round(LABEL_PRE * FS)), int(round(LABEL_POST * FS))
    n_look = int(round(1.5 * FS))
    for e, (a, b) in enumerate(epochs_of(t)):
        pk = a + int(np.argmax(pn[a:b]))
        w0, w1 = max(pk - n_pre, WINDOW - 1), min(pk + n_post + 1, len(pn))
        lab = (pn > THRESH).astype(np.int8)
        win = np.arange(w0, w1)
        pos_win = lab[win]
        early = lab[w0:max(w0, pk - n_look)].sum()
        ok = True
        if selection == "rule":
            ok = pos_win.sum() > 10 and early == 0
        if sample_reading == "window":
            frames = win
            y = pos_win
        else:
            frames = np.arange(max(a, WINDOW - 1), b)
            y = np.where((frames >= w0) & (frames < w1), lab[frames], 0).astype(np.int8)
        out.append(dict(epoch=e, peak=pk, frames=frames, y=y, keep=ok,
                        peak_value=float(pn[pk]), edge=bool(pk == a or pk >= b - n_post)))
    return out


def normalise_features(ic, cutoff):
    """[paper/claim R6] IC time courses low-pass filtered (0.1 Hz for resting data, Results,
    Feature importance, paragraph 2), Z-scored and min-max normalised, per recording
    [assumption: per recording; the paper does not say over what span]."""
    x = butter(ic, cutoff, "low") if cutoff else ic
    x = (x - x.mean(axis=0)) / x.std(axis=0)
    return (x - x.min(axis=0)) / (x.max(axis=0) - x.min(axis=0))


def build_samples(feats, labels, window=WINDOW):
    """Samples of `window` frames ending at each label frame [paper: label at the final frame]."""
    Xs, ys = [], []
    for L in labels:
        fr = L["frames"]
        fr_ok = fr[fr >= window - 1]
        idx = fr_ok[:, None] + np.arange(-window + 1, 1)[None, :]
        Xs.append(feats[idx])
        ys.append(L["y"][fr >= window - 1])
    return Xs, ys


# --- GRU --------------------------------------------------------------------------------------

def gru_fit(Xtr, ytr, Xva, yva, seed, epochs=10, batch=256, smoothing=0.001, threads=2):
    """GRU(32) -> Dense(1) -> sigmoid, Adam (Keras default learning rate 1e-3), binary
    cross-entropy with label smoothing 0.001, batch 256, 10 epochs for resting data, the epoch
    of lowest validation loss kept [paper: Methods, Machine learning; claim R9]. Implemented in
    PyTorch [deviation: the paper uses Keras; the architecture and loss are the same].
    Returns the metrics at the best epoch and the best model."""
    import torch
    from sklearn.metrics import roc_auc_score
    torch.set_num_threads(threads)
    torch.backends.mkldnn.enabled = False      # [standard] torch's own kernels (see KERNELS)
    torch.manual_seed(seed)
    g = torch.Generator().manual_seed(seed)
    net = make_net(Xtr.shape[2])
    # Keras initialisers: glorot_uniform kernels, orthogonal recurrent kernels, zero biases
    for name, p in net.named_parameters():
        if "weight_ih" in name or name == "fc.weight":
            torch.nn.init.xavier_uniform_(p)
        elif "weight_hh" in name:
            for i in range(3):
                torch.nn.init.orthogonal_(p.data[i * 32:(i + 1) * 32])
        else:
            torch.nn.init.zeros_(p)
    opt = torch.optim.Adam(net.parameters(), lr=1e-3, eps=1e-7)
    Xt = torch.tensor(Xtr, dtype=torch.float32)
    yt = torch.tensor(ytr, dtype=torch.float32)
    Xv = torch.tensor(Xva, dtype=torch.float32)
    yv_np = np.asarray(yva, dtype=np.float64)
    ys = yt * (1 - smoothing) + 0.5 * smoothing
    lossf = torch.nn.BCEWithLogitsLoss()
    best = None
    hist = []
    for ep in range(epochs):
        net.train()
        perm = torch.randperm(len(Xt), generator=g)
        for i in range(0, len(Xt), batch):
            b = perm[i:i + batch]
            opt.zero_grad()
            loss = lossf(net(Xt[b]), ys[b])
            loss.backward()
            opt.step()
        net.eval()
        with torch.no_grad():
            pv = torch.sigmoid(torch.cat([net(Xv[i:i + 4096]) for i in range(0, len(Xv), 4096)])).numpy()
            ptr = torch.sigmoid(torch.cat([net(Xt[i:i + 4096]) for i in range(0, len(Xt), 4096)])).numpy()
        pvc = np.clip(pv.astype(np.float64), 1e-7, 1 - 1e-7)
        yvs = yv_np * (1 - smoothing) + 0.5 * smoothing
        vloss = float(-np.mean(yvs * np.log(pvc) + (1 - yvs) * np.log(1 - pvc)))
        auc = roc_auc_score(yv_np, pv) if 0 < yv_np.mean() < 1 else np.nan
        tauc = roc_auc_score(ytr, ptr) if 0 < np.mean(ytr) < 1 else np.nan
        acc = float(np.mean((pv >= 0.5) == (yv_np == 1)))
        rec = dict(epoch=ep + 1, val_loss=vloss, val_auc=auc, val_acc=acc, train_auc=tauc)
        hist.append(rec)
        if best is None or vloss < best["val_loss"]:
            best = dict(rec)
            best["state"] = {k: v.clone() for k, v in net.state_dict().items()}
    net.load_state_dict(best.pop("state"))
    return best, net, hist


def make_net(n_in):
    """GRU(32) -> Dense(1); the sigmoid is applied to its output."""
    import torch

    class Net(torch.nn.Module):
        def __init__(self, n_in):
            super().__init__()
            self.gru = torch.nn.GRU(n_in, 32, batch_first=True)
            self.fc = torch.nn.Linear(32, 1)

        def forward(self, x):
            h, _ = self.gru(x)
            return self.fc(h[:, -1]).squeeze(-1)

    return Net(n_in)


def _fit_task(args):
    """One fit in a worker process; returns the metrics, the history and the weights."""
    Xtr, ytr, Xva, yva, seed, epochs = args
    best, net, hist = gru_fit(Xtr, ytr, Xva, yva, seed, epochs=epochs, threads=1)
    return best, hist, {k: v.numpy() for k, v in net.state_dict().items()}


def _net_from(state, n_in):
    import torch
    net = make_net(n_in)
    net.load_state_dict({k: torch.tensor(v) for k, v in state.items()})
    net.eval()
    return net


_POOL = {}


def fit_pool(workers=4):
    """A pool of worker processes (spawned once, reused by every cross-validation)."""
    if workers not in _POOL:
        import multiprocessing as mp
        from concurrent.futures import ProcessPoolExecutor
        _POOL[workers] = ProcessPoolExecutor(workers, mp_context=mp.get_context("spawn"))
    return _POOL[workers]


def folds_by_mouse(units_by_mouse, seed, k=5):
    """[paper] Methods, Cross-validation: "Data from each mouse were randomly divided into five
    equal-sized partitions, which were pooled across animals to form five balanced folds"."""
    rng = np.random.default_rng(seed)
    fold = {}
    for mouse, units in units_by_mouse.items():
        units = list(units)
        perm = rng.permutation(len(units))
        for j, i in enumerate(perm):
            fold[units[i]] = j % k
    return fold


def integrated_gradients(net, X, baseline, steps=32):
    """SHAP-like attribution of the logit-free output (sigmoid) by integrated gradients from a
    single baseline. [deviation] The paper uses Deep SHAP (shap.DeepExplainer) with "the mean
    model output as the background reference"; DeepExplainer does not support PyTorch GRU layers.
    Integrated gradients from the mean input are the Aumann-Shapley values for that baseline,
    and like Deep SHAP they sum to f(x) - f(baseline)."""
    import torch
    X = torch.tensor(X, dtype=torch.float32)
    b = torch.tensor(baseline, dtype=torch.float32)[None]
    total = torch.zeros_like(X)
    for a in (np.arange(steps) + 0.5) / steps:
        xi = (b + a * (X - b)).requires_grad_(True)
        out = torch.sigmoid(net(xi)).sum()
        gr, = torch.autograd.grad(out, xi)
        total += gr
    return ((X - b) * total / steps).detach().numpy()


def _reduce_quiet(row):
    return reduce_session(row, verbose=False)


def reduce_all(rows, workers=3):
    """Reduce several sessions in parallel processes (each holds about 3.3 GB at its peak)."""
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(_reduce_quiet, rows))


# --- data sets and cross-validation ------------------------------------------------------------

def make_dataset(sessions, ics, ic_idx, cutoff=0.1, sample_reading="window", selection="none",
                 window=WINDOW, pupil_key="pupil"):
    """Samples of every kept epoch: X (n, window, n_ic), y, and the epoch and mouse of each."""
    X, y, unit, mouse, rec = [], [], [], [], []
    info = []
    for r, (s, ic) in enumerate(zip(sessions, ics)):
        feats = normalise_features(ic[:, ic_idx], cutoff)
        pn = pupil_norm(s[pupil_key])
        labs = epoch_labels(s["t"], pn, sample_reading, selection)
        for L in labs:
            info.append(dict(rec=r, subject=s["subject"], day=s["day"], epoch=L["epoch"],
                             keep=L["keep"], n_pos=int(L["y"].sum()), n=len(L["y"]),
                             peak_value=L["peak_value"], peak_frame=L["peak"], edge=L["edge"]))
        kept = [L for L in labs if L["keep"]]
        Xs, ys = build_samples(feats, kept, window)
        for L, xx, yy in zip(kept, Xs, ys):
            X.append(xx.astype(np.float32))
            y.append(yy)
            unit.append(np.full(len(yy), r * 100 + L["epoch"]))
            mouse.append(np.full(len(yy), s["subject"], dtype=object))
            rec.append(np.full(len(yy), r))
    return dict(X=np.concatenate(X), y=np.concatenate(y).astype(np.int8), unit=np.concatenate(unit),
                mouse=np.concatenate(mouse), rec=np.concatenate(rec), info=info)


def shuffle_within(y, unit, rng):
    """[paper] Null models: "pupil labels were randomly shuffled within sessions"; [claim R8]
    the unit is the 40 s epoch."""
    y = y.copy()
    for u in np.unique(unit):
        i = np.flatnonzero(unit == u)
        y[i] = y[i][rng.permutation(len(i))]
    return y


def run_cv(ds, seed, fold_unit="epoch", null_scope="train", k=5, epochs=10, keep_models=False,
           workers=4):
    """Five-fold cross-validation of the model and its null model [paper: Methods, Model
    evaluation; claim R7, R8]. fold_unit 'epoch' (R7 a) or 'recording' (R7 b); null_scope
    'train' (R8 a) or 'both' (R8 b). Model fits use seed + fold; null shuffles use the claim's
    second generator (seed + 1), null fits seed + 100 + fold."""
    units = ds["unit"] if fold_unit == "epoch" else ds["rec"]
    # [deviation] with 3 recordings per mouse, five equal parts per mouse are impossible when the
    # unit is the recording; the recordings are then pooled over mice before the split.
    groups = ds["mouse"] if fold_unit == "epoch" else np.full(len(units), "all", dtype=object)
    by_mouse = {}
    for u, m in zip(units, groups):
        by_mouse.setdefault(m, set()).add(int(u))
    by_mouse = {m: sorted(v) for m, v in sorted(by_mouse.items())}
    fold = folds_by_mouse(by_mouse, seed, k)
    fsample = np.array([fold[int(u)] for u in units])
    rng_null = np.random.default_rng(seed + 1)
    res, tasks, vals = [], [], []
    for f in range(k):
        tr, va = fsample != f, fsample == f
        r = {"fold": f, "n_train": int(tr.sum()), "n_val": int(va.sum()),
             "pos_train": float(ds["y"][tr].mean()), "pos_val": float(ds["y"][va].mean())}
        ytr_null = shuffle_within(ds["y"][tr], ds["unit"][tr], rng_null)
        yva_null = ds["y"][va]
        if null_scope == "both":
            yva_null = shuffle_within(ds["y"][va], ds["unit"][va], rng_null)
        r["null_changed"] = float(np.mean(ytr_null != ds["y"][tr]))
        tasks.append((ds["X"][tr], ds["y"][tr], ds["X"][va], ds["y"][va], seed + f, epochs))
        tasks.append((ds["X"][tr], ytr_null, ds["X"][va], yva_null, seed + 100 + f, epochs))
        res.append(r)
        vals.append(np.flatnonzero(va))
    # [standard] the ten fits run in parallel processes, one thread each; a fit gives the same
    # result on one thread as on several (checked while preparing), so this changes no number.
    out = list(fit_pool(workers).map(_fit_task, tasks))
    models = []
    n_in = ds["X"].shape[2]
    for f in range(k):
        (best, hist, st), (bnull, nhist, nst) = out[2 * f], out[2 * f + 1]
        res[f].update({"model_" + kk: v for kk, v in best.items()})
        res[f]["model_hist"] = hist
        res[f].update({"null_" + kk: v for kk, v in bnull.items()})
        res[f]["null_hist"] = nhist
        if keep_models:
            models.append((_net_from(st, n_in), _net_from(nst, n_in), vals[f]))
    import pandas as pd
    df = pd.DataFrame(res)
    return (df, models) if keep_models else df


def paired(df, metric):
    """Paired t-test over the folds, model against null [paper: Supplementary Figure 5 legend]."""
    a, b = df["model_" + metric].to_numpy(), df["null_" + metric].to_numpy()
    ok = np.isfinite(a) & np.isfinite(b)       # a fold whose validation labels are all one class has no AUC
    t, p = stats.ttest_rel(a[ok], b[ok]) if ok.sum() >= 3 else (np.nan, np.nan)
    return dict(model=float(np.mean(a[ok])), null=float(np.mean(b[ok])), t=float(t), p=float(p), n=int(ok.sum()))


def keypoint_pupil(row, t_img):
    """[claim R3 reading (b)] Horizontal pupil diameter from the eye keypoints, as the paper's own
    Methods define it ("Euclidean distance between the left and right boundary landmarks"): the
    file holds 30 pupil-edge keypoints without a stated position on the pupil, so the width is
    taken as the largest minus the smallest x of the edge points with confidence >= 0.5
    [assumption], in pixels, interpolated onto the imaging timestamps."""
    f = open_nwb(row["asset_id"], block_mb=8)
    g = f["processing/behavior/eye_video_keypoints"]
    names = sorted(k for k in g.keys() if k.startswith("pupiledge"))
    xs, cs = [], []
    t = None
    for n in names:
        xs.append(g[n]["data"][:, 0])
        cs.append(g[n]["confidence"][:])
        if t is None:
            t = g[n]["timestamps"][:]
    tb0 = f["acquisition/widefield_blue/timestamps"][0]
    f.close()
    x = np.array(xs)
    c = np.array(cs)
    x = np.where(c >= 0.5, x, np.nan)
    n_ok = np.isfinite(x).sum(axis=0)
    width = np.full(x.shape[1], np.nan)
    ok = n_ok >= 4
    width[ok] = np.nanmax(x[:, ok], axis=0) - np.nanmin(x[:, ok], axis=0)
    width, n_bad = fill_nan(width)
    return np.interp(t_img, t - tb0, width), n_bad, len(names)


def clean_pupil(p, factor=3.0):
    """[assumption] Failed detections in the deposited diameter. Some recordings hold values up to
    1e21 pixels. The paper's own outlier rule is for its DeepLabCut coordinates (Methods, Pupil
    diameter quantification); here a value above 3 times or below a third of the recording's
    median is taken as a failed detection and replaced by linear interpolation, as are missing
    values. Returns the cleaned trace and the number of frames replaced."""
    p = np.asarray(p, dtype=np.float64).copy()
    m = np.nanmedian(p)
    bad = ~np.isfinite(p) | (p > factor * m) | (p < m / factor)
    p[bad] = np.nan
    return fill_nan(p)[0], int(bad.sum())


def clean_session(s):
    s["pupil_filled"] = s["pupil"]
    s["pupil"], s["pupil_replaced"] = clean_pupil(s["pupil"])
    if "pupil_kp" in s:
        s["pupil_kp"], s["pupil_kp_replaced"] = clean_pupil(s["pupil_kp"])
    return s


def load_sessions(rows, workers=3):
    """Stream and reduce the chosen sessions, add the keypoint pupil of reading R3 (b), and
    replace failed pupil detections."""
    sessions = reduce_all(rows, workers)
    for s, r in zip(sessions, rows):
        s["pupil_kp"], s["pupil_kp_bad"], s["n_edge_points"] = keypoint_pupil(r, s["t"])
        clean_session(s)
    return sessions


def channel_check(row, start=3000, n=1500):
    """Which stored channel carries the calcium signal: the temporal SD of dF/F (mean over cortex
    pixels, 1500 frames) of each series, and the mean raw intensity. GCaMP fluorescence under
    470 nm excitation varies more than under 405 nm (near-isosbestic)."""
    f = open_nwb(row["asset_id"], block_mb=16)
    masks = f["processing/ophys/ImageSegmentation/ROIs/image_mask"][:]
    cortex = masks.any(axis=0)
    out = {}
    for ch in ("widefield_blue", "widefield_UV"):
        x = f["acquisition/" + ch + "/data"][start:start + n][:, cortex].astype(np.float64)
        d = x / x.mean(axis=0) - 1
        out[ch] = dict(dff_sd=float(d.std(axis=0).mean()), raw_mean=float(x.mean()),
                       excitation_lambda=float(f["general/optophysiology/ImagingPlane_" + ch.split("_")[1] + "/excitation_lambda"][()]))
    f.close()
    return out


def predict(net, X):
    import torch
    with torch.no_grad():
        Xt = torch.tensor(X, dtype=torch.float32)
        return torch.sigmoid(torch.cat([net(Xt[i:i + 4096]) for i in range(0, len(Xt), 4096)])).numpy()


def auc_by_mouse(ds, folds_models):
    """Validation AUC per mouse and fold, model and null, from run_cv(keep_models=True)."""
    from sklearn.metrics import roc_auc_score
    rows = []
    for f, (net, nnet, va) in enumerate(folds_models):
        pm, pn = predict(net, ds["X"][va]), predict(nnet, ds["X"][va])
        for m in np.unique(ds["mouse"][va]):
            i = ds["mouse"][va] == m
            y = ds["y"][va][i]
            if 0 < y.mean() < 1:
                rows.append(dict(fold=f, mouse=m, n=int(i.sum()), model_auc=roc_auc_score(y, pm[i]),
                                 null_auc=roc_auc_score(y, pn[i])))
    import pandas as pd
    return pd.DataFrame(rows)


def hemo_check(s, hemo="fit_hp_subtract_raw"):
    """Correlation, per atlas ROI, of this attempt's corrected dF/F averaged over the ROI (the
    34 corrected components projected on the ROI's pixels) with the deposited ROI dF/F
    (processing/ophys/DfOverF/dFF, the dataset's own hemodynamics-corrected signal), both
    low-pass filtered at 0.1 Hz. The uncorrected 470 nm dF/F is given as the reference."""
    M = s["maps_atlas"]
    out = {}
    for name, V in (("corrected", s["V"][hemo]), ("uncorrected", s["V"]["uncorrected"])):
        rs = []
        for i, n in enumerate(s["roi_names"]):
            if n.startswith("OB") or i >= s["dff_deposited"].shape[1]:
                continue
            m = s["roi_atlas"][i] & np.isfinite(M).all(axis=0)
            if m.sum() < 5:
                continue
            x = V @ M[:, m].mean(axis=1)
            dep, _ = fill_nan(s["dff_deposited"][:, i])
            rs.append(np.corrcoef(butter(x, 0.1), butter(dep, 0.1))[0, 1])
        out[name] = np.array(rs)
    return out
