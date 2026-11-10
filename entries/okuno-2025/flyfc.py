"""Loading and measures for testing Okuno et al. (2025) on dandiset 000727.

The dandiset holds the whole-brain two-photon imaging of Brezovec et al.: one NWB
file per fly with the raw GCaMP6f (green) and tdTomato (red) volumes, a processed
green series in the FDA space, and FicTrac walking data at 50 Hz.

The paper's structural connectivity (SC) and its ROI atlases are outside the
dataset. They come from

- the paper's code, github.com/takuto-okuno-riken/flywalk at commit 4b92add
  (CODE_COMMIT): the resized FDA template, brain mask, fibre mask, the hemibrain
  neuropil atlas (atlas/hemiroi, 114 ROIs), the ROI names (data/hemiroi.mat) and
  the FlyEM cf0.8 SC of the 114 ROIs (results/sc/hemiroi_connectlist.mat);
- the paper's Zenodo record 10.5281/zenodo.15532272 (ZENODO_URL), the version of
  2025-05-28 that the code's README cites: the FlyWire sc140 SC matrices of the
  hemibrain ROIs, the selected-synapse SC matrices, the 99 null SC matrices of each
  permutation test, per-ROI transmitter counts and post-synapse counts.

Where each parameter comes from:

- volume rate 1.879714 Hz, the green channel: the claims file (header, Data the
  paper used) and the NWB file's own rate.
- registration of the mean green image to the resized FDA template with ANTs SyN:
  Methods, Preprocessing ("the averaged NIfTI image was registered by ANTs to the
  resized FDA template"; Ext. Data Fig. 1-1a). Defaults of antspy's "SyN" are a
  standard choice (claims file, O2). The mean image is taken over three blocks of
  152 volumes (start, middle, end), a standard choice that cannot change which
  template voxel a native voxel maps to by more than the registration error.
- the axis orientation of the native volume against the template is not stated in
  the files. The notebook shows the native mean image beside the template: the
  dorsoventral (y) and anteroposterior (z) axes run the same way, so no flip is
  applied. Left and right cannot be told apart from a symmetric image (the
  correlation after an affine registration is printed for the eight flips); no flip
  is assumed, and the notebook shows the result with left and right ROIs swapped.
- ROI time series: the paper warps every volume to the template with linear
  interpolation and averages the voxels of each ROI (extractROItimeseries.m,
  Methods "The intensity of the voxels in the ROI was averaged"). Here the same
  linear map is applied as a sparse matrix from native voxels to ROI means, which
  gives the same ROI series without warping each volume (both are linear in the
  data). Template voxels outside the field of view count as 0, as the code's
  V(isnan(V)) = 0 does.
- nuisance regression, Poly-tCompCor: lib/getNuisancePolynomial.m (7 terms) and
  lib/getNuisancetCompCor.m (6 principal components of the 1000 voxels with the
  highest temporal SD, the SD taken on mean-centred data and the components after
  polynomial detrending), extractROItimeseries.m (each voxel mean-centred and
  regressed by OLS; the ROI series is the mean). Regressing the ROI mean equals
  the mean of the voxel residuals, since the regressors are the same for every
  voxel. Deviation: the 1000 voxels are taken among native voxels inside the
  template's field of view, not among template voxels (an assumption, stated in the
  notebook).
- FC, FC-SC correlation, per-region correlation: analyzeFuncConnectivity.m and the
  claims file (M3, M4): Pearson r per fly, atanh, mean over flies, infinite values
  set to the largest finite value; r between log10(SC) (log of 0 set to 0) and
  |mean z-FC| over all n x n elements; SC is the second ("Traced") layer.
- permutation test: plotFuncConnectivity.m checkRandSubsampleRankTestByHemiroi and
  the claims file (M6): normal fit to the 99 null values, two-tailed p, Bonferroni
  0.05/6.
- subjects: the code's subject list [1 2 3 4 5 6 8 9] of the flies in name order
  (claims file, header); all nine are shown as a variant.
"""

import gzip
import io
import os
import tarfile
import time
import zipfile
import zlib
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
import requests
import scipy.sparse as sp
from scipy import stats

DANDISET = "000727"
VERSION = "0.240106.0043"
API = "https://api.dandiarchive.org/api"
CODE_COMMIT = "4b92add4a44f641ab6add809ff6b0e0d6110b50c"
CODE_TARBALL = f"https://github.com/takuto-okuno-riken/flywalk/archive/{CODE_COMMIT}.tar.gz"
ZENODO_RECORD = "15532272"
ZENODO_URL = f"https://zenodo.org/api/records/{ZENODO_RECORD}/files/flywalkdemodata.zip/content"
GREEN = "acquisition/TwoPhotonSeriesFunctionalGreen/data"
SUBJECT_IDS = [1, 2, 3, 4, 5, 6, 8, 9]  # code's sbjids, 1-based, flies in name order
NATIVE_SPACING_MM = (0.00261117299, 0.00261117299, 0.005)  # NWB grid_spacing (m -> mm)


# --------------------------------------------------------------------------- archive
def list_assets():
    """NWB assets of the pinned version, sorted by path, with their S3 URLs."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        for a in r["results"]:
            if a["path"].endswith(".nwb"):
                out.append(a)
        url = r["next"]
    out.sort(key=lambda a: a["path"])
    for a in out:
        meta = requests.get(f"{API}/assets/{a['asset_id']}/", timeout=60).json()
        a["s3"] = [u for u in meta["contentUrl"] if "s3" in u][0]
        a["subject"] = a["path"].split("/")[0].replace("sub-", "")
    return out


def open_nwb(s3):
    return h5py.File(remfile.File(s3), "r")


class ChunkReader:
    """Reads chunks of a gzip-compressed dataset with parallel HTTP range requests.

    remfile and h5py read about 10 MB/s; asking S3 for each chunk's bytes directly and
    inflating them with zlib (which releases the GIL) reads 100 to 200 MB/s."""

    def __init__(self, s3, h5, path=GREEN, threads=16):
        self.s3 = s3
        d = h5[path]
        self.shape = d.shape
        self.chunks = d.chunks
        self.dtype = d.dtype
        n = d.id.get_num_chunks()
        self.infos = [d.id.get_chunk_info(i) for i in range(n)]
        self.threads = threads
        self.session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(pool_connections=threads, pool_maxsize=threads)
        self.session.mount("https://", adapter)
        self.bytes_read = 0

    def _get(self, ci):
        for attempt in range(5):
            try:
                r = self.session.get(self.s3, headers={
                    "Range": f"bytes={ci.byte_offset}-{ci.byte_offset + ci.size - 1}"}, timeout=120)
                raw = zlib.decompress(r.content)
                break
            except Exception:
                if attempt == 4:
                    raise
                time.sleep(2)
        self.bytes_read += ci.size
        n = len(raw) // (np.dtype(self.dtype).itemsize * self.chunks[1] * self.chunks[2])
        return ci.chunk_offset, np.frombuffer(raw, dtype=self.dtype).reshape(n, self.chunks[1], self.chunks[2])

    def slices(self, zs):
        """Yield (z, array (T, X, Y)) for each z in zs, prefetching the next slice."""
        T, X, Y, Z = self.shape
        byz = {}
        for ci in self.infos:
            byz.setdefault(ci.chunk_offset[3], []).append(ci)
        with ThreadPoolExecutor(self.threads) as ex:
            futs = {}
            order = list(zs)
            def submit(z):
                futs[z] = [ex.submit(self._get, ci) for ci in byz[z]]
            for z in order[:2]:
                submit(z)
            for i, z in enumerate(order):
                out = np.empty((T, X, Y), dtype=self.dtype)
                for f in futs.pop(z):
                    off, a = f.result()
                    a = a[:T - off[0]]  # the last chunk is stored padded
                    out[off[0]:off[0] + a.shape[0]] = a
                if i + 2 < len(order):
                    submit(order[i + 2])
                yield z, out

    def mean_image(self, tstarts):
        """Mean volume over the time chunks starting at tstarts."""
        T, X, Y, Z = self.shape
        sel = [ci for ci in self.infos if ci.chunk_offset[0] in tstarts]
        acc = np.zeros((X, Y, Z))
        cnt = np.zeros(Z)
        with ThreadPoolExecutor(self.threads) as ex:
            for off, a in ex.map(self._get, sel):
                a = a[:T - off[0]]
                acc[:, :, off[3]] += a.sum(0, dtype=np.float64)
                cnt[off[3]] += a.shape[0]
        return acc / cnt


# --------------------------------------------------------------------------- paper inputs
_code = None


def code_file(name):
    """A file of the paper's code repository at CODE_COMMIT, as bytes."""
    global _code
    if _code is None:
        b = requests.get(CODE_TARBALL, timeout=300).content
        t = tarfile.open(fileobj=io.BytesIO(b), mode="r:gz")
        _code = {}
        for m in t.getmembers():
            if m.isfile():
                _code[m.name.split("/", 1)[1]] = t.extractfile(m).read()
    return _code[name]


def code_nifti(name):
    import nibabel as nib
    b = code_file(name)
    if name.endswith(".gz"):
        b = gzip.decompress(b)
    img = nib.Nifti1Image.from_bytes(b)
    return np.asarray(img.dataobj).astype(np.float32), img.header.get_zooms()


_zip = None


def zenodo_member(name):
    """A member of the paper's Zenodo zip (read over range requests)."""
    global _zip
    import fsspec
    if _zip is None:
        _zip = zipfile.ZipFile(fsspec.open(ZENODO_URL, block_size=2 ** 20).open())
    return _zip.read("flywalkdemodata/" + name)


def load_mat(b):
    """Read a MATLAB file (v7.3 via h5py, transposed back to MATLAB order)."""
    try:
        import scipy.io as sio
        m = sio.loadmat(io.BytesIO(b))
        return {k: v for k, v in m.items() if not k.startswith("__")}
    except NotImplementedError:
        f = h5py.File(io.BytesIO(b), "r")
        out = {}
        for k in f.keys():
            if isinstance(f[k], h5py.Dataset):
                a = f[k][()]
                out[k] = a.T if a.ndim > 1 else a
        return out


def load_sc(b):
    """SC of a connect list: (ncount layer 2, sycount layer 2, primaryIds 0-based)."""
    m = load_mat(b)
    nc = np.asarray(m["ncountMat"], dtype=np.float64)
    sc = np.asarray(m["sycountMat"], dtype=np.float64)
    ids = np.asarray(m["primaryIds"]).ravel().astype(int) - 1
    return nc[:, :, 1], sc[:, :, 1], ids


def hemiroi_masks():
    """The 114 hemibrain ROI masks of the code repository (template space)."""
    masks = []
    for i in range(1, 115):
        v, _ = code_nifti(f"atlas/hemiroi/roi{i}.nii.gz")
        masks.append(v > 0)
    return masks


def hemiroi_names():
    m = load_mat(code_file("data/hemiroi.mat"))
    return [str(np.asarray(r).ravel()[0]) for r in m["roiname"][:, 0]]


# --------------------------------------------------------------------------- registration
FLIPS = [(fx, fy, fz) for fx in (1, -1) for fy in (1, -1) for fz in (1, -1)]


def _flip(a, fl):
    return a[::fl[0], ::fl[1], ::fl[2]].copy()


def choose_flip(mean, tmpl_img, seed=1):
    """Correlation with the template after an affine registration, for each flip."""
    import ants
    out = {}
    tm = tmpl_img.numpy().ravel()
    for fl in FLIPS:
        mov = ants.from_numpy(_flip(mean, fl).astype(np.float32), spacing=NATIVE_SPACING_MM)
        r = ants.registration(tmpl_img, mov, type_of_transform="Affine", random_seed=seed)
        out[fl] = float(np.corrcoef(tm, r["warpedmovout"].numpy().ravel())[0, 1])
    return out


def register(mean, tmpl_img, fl, seed=1):
    """SyN registration of the flipped mean image to the template.

    The affine start is the better of two affine registrations (mean squares and
    Mattes mutual information, on the image scaled to its 99.5th percentile): with
    antspy's default affine stage the optimiser stopped at its start for several
    flies (correlation with the template 0.3). The SyN stage then starts from it.

    Returns the native continuous coordinates (n, 3) of every template voxel (NaN
    outside the field of view), the correlations with the template after the
    affine and the SyN stages, and the warped mean image."""
    import ants
    m = _flip(mean, fl).astype(np.float32)
    m = np.clip(m / np.percentile(m, 99.5), 0, 1)
    mov = ants.from_numpy(m, spacing=NATIVE_SPACING_MM)
    tm = tmpl_img.numpy().ravel()
    aff = {}
    for metric in ("meansquares", "mattes"):
        r = ants.registration(tmpl_img, mov, type_of_transform="Affine", aff_metric=metric,
                              random_seed=seed, aff_iterations=(2100, 1200, 1200, 10),
                              aff_shrink_factors=(6, 4, 2, 1), aff_smoothing_sigmas=(3, 2, 1, 0))
        aff[metric] = (float(np.corrcoef(tm, r["warpedmovout"].numpy().ravel())[0, 1]),
                       r["fwdtransforms"][0])
    best = max(aff, key=lambda k: aff[k][0])
    r = ants.registration(tmpl_img, mov, type_of_transform="SyNOnly",
                          initial_transform=aff[best][1], random_seed=seed)
    cc = {"affine_" + k: v[0] for k, v in aff.items()}
    cc["syn"] = float(np.corrcoef(tm, r["warpedmovout"].numpy().ravel())[0, 1])
    shp = mean.shape
    coords = []
    for ax in range(3):
        g = np.zeros(shp, np.float32)
        idx = np.arange(shp[ax], dtype=np.float32)
        sh = [1, 1, 1]
        sh[ax] = -1
        g[:] = idx.reshape(sh)
        ci = ants.from_numpy(g, spacing=NATIVE_SPACING_MM)
        w = ants.apply_transforms(tmpl_img, ci, r["fwdtransforms"], interpolator="linear",
                                  defaultvalue=-1e6).numpy()
        coords.append(w.ravel())
    c = np.stack(coords, 1).astype(np.float64)
    c[(c < -0.5).any(1)] = np.nan
    # back from the flipped grid to native indices
    for ax in range(3):
        if fl[ax] == -1:
            c[:, ax] = shp[ax] - 1 - c[:, ax]
    for f in r["fwdtransforms"] + r["invtransforms"] + [v[1] for v in aff.values()]:
        if os.path.exists(f):
            try:
                os.remove(f)
            except OSError:
                pass
    return c, cc, r["warpedmovout"].numpy()


def interp_matrix(coords, shp):
    """Sparse (template voxels x native voxels) trilinear interpolation matrix.

    Native voxels are ordered z-major, then x, then y (index z*X*Y + x*Y + y), the
    order in which slices are streamed."""
    X, Y, Z = shp
    n = coords.shape[0]
    ok = ~np.isnan(coords).any(1)
    rows, cols, vals = [], [], []
    c = coords[ok]
    r_ok = np.nonzero(ok)[0]
    c = np.clip(c, 0, np.array([X - 1, Y - 1, Z - 1]))
    f = np.floor(c).astype(int)
    d = c - f
    for dx in (0, 1):
        for dy in (0, 1):
            for dz in (0, 1):
                ix = np.minimum(f[:, 0] + dx, X - 1)
                iy = np.minimum(f[:, 1] + dy, Y - 1)
                iz = np.minimum(f[:, 2] + dz, Z - 1)
                w = ((d[:, 0] if dx else 1 - d[:, 0]) * (d[:, 1] if dy else 1 - d[:, 1])
                     * (d[:, 2] if dz else 1 - d[:, 2]))
                keep = w > 0
                rows.append(r_ok[keep])
                cols.append((iz * X * Y + ix * Y + iy)[keep])
                vals.append(w[keep])
    P = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
                      shape=(n, X * Y * Z))
    return P, ok


def roi_weights(masks, P):
    """Rows: the mean over each mask's template voxels, mapped to native voxels."""
    n = P.shape[0]
    rows, cols, vals = [], [], []
    for i, m in enumerate(masks):
        idx = np.nonzero(m.ravel())[0]
        rows.append(np.full(idx.size, i))
        cols.append(idx)
        vals.append(np.full(idx.size, 1.0 / max(idx.size, 1)))
    A = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
                      shape=(len(masks), n))
    return (A @ P).tocsc().astype(np.float32)


# --------------------------------------------------------------------------- per fly
def process_fly(asset, tmpl_img, masks, n_top=1000, flip=(1, 1, 1)):
    """Stream one fly's green series once and reduce it to ROI series.

    Returns a dict with the ROI mean series (rows = masks, T columns), the series of
    the n_top native voxels with the highest temporal SD (for tCompCor), the
    registration diagnostics and the field-of-view coverage of each mask."""
    t0 = time.time()
    h5 = open_nwb(asset["s3"])
    rd = ChunkReader(asset["s3"], h5)
    T, X, Y, Z = rd.shape
    rate = float(h5["acquisition/TwoPhotonSeriesFunctionalGreen/starting_time"].attrs["rate"])
    spd = h5["processing/behavior/FicTrac/SpatialSeriesMovementSpeed"]
    speed = spd["data"][:, 0]
    speed_rate = float(spd["starting_time"].attrs["rate"])
    ct = rd.chunks[0]
    tstarts = {0, ct * ((T // ct) // 2), ct * ((T - 1) // ct)}
    mean = rd.mean_image(tstarts)
    fl = flip
    coords, cc, warped = register(mean, tmpl_img, fl)
    P, inside = interp_matrix(coords, (X, Y, Z))
    W = roi_weights(masks, P)
    cover = np.array([inside[m.ravel()].mean() if m.any() else np.nan for m in masks])
    fov = np.asarray(P.sum(0)).ravel() > 0  # native voxels that reach the template grid
    t_reg = time.time() - t0
    R = np.zeros((T, W.shape[0]))
    top_sd = np.empty(0)
    top_ts = np.empty((0, T), np.float32)
    nvox = X * Y
    for z, a in rd.slices(range(Z)):
        xz = a.reshape(T, nvox).astype(np.float32)
        cols = slice(z * nvox, (z + 1) * nvox)
        Wz = W[:, cols]
        if Wz.nnz:
            R += xz @ Wz.toarray().T
        m = fov[cols]
        if m.any():
            mu = xz.mean(0, dtype=np.float64)
            sd = np.sqrt(np.maximum(np.einsum("ij,ij->j", xz, xz, dtype=np.float64) / T - mu ** 2, 0))
            sd[~m] = -1
            k = min(n_top, int(m.sum()))
            sel = np.argpartition(-sd, k - 1)[:k]
            top_sd = np.concatenate([top_sd, sd[sel]])
            top_ts = np.concatenate([top_ts, xz[:, sel].T])
            if top_sd.size > n_top:
                keep = np.argpartition(-top_sd, n_top - 1)[:n_top]
                top_sd, top_ts = top_sd[keep], top_ts[keep]
    h5.close()
    return dict(subject=asset["subject"], R=R.T, top_ts=top_ts, top_sd=top_sd,
                flip=fl, cc=cc, cover=cover, coords=coords.astype(np.float32),
                speed=speed, speed_rate=speed_rate, rate=rate, T=T, shape=(X, Y, Z),
                mean=mean, warped=warped, t_reg=t_reg, t_total=time.time() - t0,
                mb_read=rd.bytes_read / 1e6)


# --------------------------------------------------------------------------- nuisance and FC
def poly_regressors(n):
    """lib/getNuisancePolynomial.m: 2 linear, 4 quadratic and a constant term."""
    X = np.empty((n, 7))
    X[:, 0] = np.linspace(0, 1, n)
    X[:, 1] = np.linspace(1, 0, n)
    X[:, 2] = X[:, 0] ** 2
    X[:, 3] = X[::-1, 2]
    X[:, 4] = 1 - X[:, 2]
    X[:, 5] = 1 - X[:, 3]
    X[:, 6] = 1
    return X


def residualize(Y, Xn):
    """OLS residuals of each column of Y (T x k) on Xn (T x p)."""
    beta, *_ = np.linalg.lstsq(Xn, Y, rcond=None)
    return Y - Xn @ beta


def tcompcor(top_ts, Sd, ncomp=6):
    """lib/getNuisancetCompCor.m: PCA scores of the high-SD voxels after detrending."""
    V = top_ts.astype(np.float64).T  # T x voxels
    V = V - V.mean(0)
    V = residualize(V, Sd)
    V = V - V.mean(0)
    U, S, _ = np.linalg.svd(V, full_matrices=False)
    return U[:, :ncomp] * S[:ncomp]


def roi_series(fly, nuisance):
    """ROI series (T x ROIs) for nuisance '' (none) or 'poltcomp'."""
    Y = fly["R"].T.copy()
    Y = Y - Y.mean(0)
    if nuisance == "poltcomp":
        Sd = poly_regressors(Y.shape[0])
        Xn = np.hstack([Sd, tcompcor(fly["top_ts"], Sd)])
        Y = residualize(Y, Xn)
    elif nuisance != "":
        raise ValueError(nuisance)
    return Y - Y.mean(0)


def mean_zfc(series_list):
    """Fisher-z FC averaged over flies (analyzeFuncConnectivity.m)."""
    Z = []
    for Y in series_list:
        with np.errstate(invalid="ignore", divide="ignore"):
            C = np.corrcoef(Y.T)
            Z.append(np.arctanh(C))
    Z = np.stack(Z, 2)
    with np.errstate(invalid="ignore"):
        m = np.nanmean(Z, 2)
    fin = np.isfinite(m)
    m[np.isinf(m)] = np.max(m[fin])
    return m


def log_sc(S):
    with np.errstate(divide="ignore"):
        L = np.log10(S)
    L[L < 0] = 0
    return L


def fcsc_r(S, mFz, ids, kind="pearson"):
    """FC-SC correlation over every element of the ids x ids matrices (code's R)."""
    a = log_sc(S[np.ix_(ids, ids)]).ravel()
    b = np.abs(mFz[np.ix_(ids, ids)]).ravel()
    ok = np.isfinite(b)
    if kind == "spearman":
        return stats.spearmanr(a[ok], b[ok])[0]
    return np.corrcoef(a[ok], b[ok])[0, 1]


def fcsc_roi_r(S, mFz, ids):
    """Per-region FC-SC correlation (code's roiR column 7)."""
    L = log_sc(S[np.ix_(ids, ids)])
    F = np.abs(mFz[np.ix_(ids, ids)])
    out = np.empty(len(ids))
    for i in range(len(ids)):
        a = np.concatenate([L[i, :], L[:, i]])
        b = np.concatenate([F[i, :], F[:, i]])
        out[i] = np.corrcoef(a, b)[0, 1]
    return out


def normal_p(x, null):
    """Two-tailed p of x against a normal fitted to the null (MATLAB fitdist)."""
    mu, sd = np.mean(null), np.std(null, ddof=1)
    return 2 * stats.norm.cdf(-abs(x - mu) / sd), mu, sd


# --------------------------------------------------------------------------- GLM
def speed_per_volume(speed, frames=3384, offset_ms=104.654892, rate=1.879714):
    """checkBehavior.m: mean 50 Hz speed within each volume, imaging starting
    104.654892 ms after the behaviour."""
    TR = 1000 / rate
    out = np.empty(frames)
    for i in range(frames):
        st = int(np.ceil((offset_ms + TR * i) / 20))
        ed = int(np.floor((offset_ms + TR * (i + 1)) / 20))
        ed = min(ed, speed.size)
        out[i] = speed[st - 1:ed].mean()  # MATLAB 1-based st:ed
    return out


def gamma_crf(dt, a=1.7, b=0.25, kernel=5.0):
    """lib/getGlmCRF.m with checkBehavior.m's shape 1.7 and scale 0.25 s."""
    t = np.arange(0, kernel + dt / 2, dt)
    h = stats.gamma.pdf(t, a, scale=b)
    return h / h.sum()


def walking_regressors(speeds, rate=1.879714, binary=False):
    """checkBehavior.m: per-volume speed clipped at th (mean over flies of each fly's
    SD), minus b (mean over flies of each fly's 10th percentile), negatives set to
    0, scaled to [0 1], convolved with the CRF at 25 times the volume rate.
    binary=True is the claims file's O1 variant: 1 where the speed is at or above
    b + th, else 0, before the convolution."""
    MS = [s for s in speeds]
    th = np.mean([np.std(s) for s in MS])
    bsp = np.mean([np.percentile(s, 10, method="hazen") for s in MS])
    TR = 1 / rate
    res = 25
    h = gamma_crf(TR / res)
    out, mscal = [], []
    for s in MS:
        v = speed_per_volume(s)
        mscal.append(v)
        if binary:
            mb = (v >= bsp + th).astype(float)
        else:
            mb = np.minimum(v, th) - bsp
            mb[mb < 0] = 0
            mb = mb / (th - bsp)
        n = mb.size
        x = np.arange(n) * TR
        xq = np.arange((n - 1) * res + 1) * TR / res
        vq = np.interp(xq, x, mb)
        U = np.convolve(vq, h)
        out.append(U[0:res * n:res][:n])
    return np.array(out), np.array(mscal), th, bsp


def glm_betas(asset, fly, regressors):
    """First-level OLS betas per native voxel (second pass over the green series).

    Design as glmFlyMB1st.m: [walking regressor, 7 polynomial terms, 6 tCompCor
    components divided by their overall SD]. For each regressor given (the main one
    and variants) returns the betas of the walking regressor and the six tCompCor
    terms (the columns glmFlyMB2nd.m keeps), mapped to the template grid by the
    fly's interpolation matrix. Smoothing is applied to these template maps
    afterwards (glm_smooth), which for OLS equals fitting the smoothed data.
    Deviation: no Tukey-taper pre-whitening, and tCompCor from the unsmoothed native
    voxels (assumptions, stated in the notebook)."""
    T = fly["T"]
    Sd = poly_regressors(T)
    tc = tcompcor(fly["top_ts"], Sd)
    tc = tc / np.std(tc)
    keep = [0] + list(range(8, 14))
    pk = np.vstack([np.linalg.pinv(np.column_stack([r, Sd, tc]))[keep] for r in regressors])
    pk = pk.astype(np.float32)
    h5 = open_nwb(asset["s3"])
    rd = ChunkReader(asset["s3"], h5)
    _, Xn, Yn, Z = rd.shape
    nvox = Xn * Yn
    B = np.zeros((pk.shape[0], nvox * Z), np.float32)
    for z, a in rd.slices(range(Z)):
        xz = a.reshape(T, nvox).astype(np.float32)
        xz -= xz.mean(0)
        B[:, z * nvox:(z + 1) * nvox] = pk @ xz
    h5.close()
    P, _ = interp_matrix(fly["coords"].astype(np.float64), fly["shape"])
    Bt = np.asarray((P @ B.T.astype(np.float64)).T, np.float32)
    return [Bt[i * 7:(i + 1) * 7] for i in range(len(regressors))]


def glm_smooth(vol, fwhm_vox=8.0):
    """Gaussian of FWHM n voxels along y (2.28 um) and the same width along x and z
    (extractROItimeseries.m / glmFlyMB1st.m), filter size 2*ceil(2*sigma)+1."""
    from scipy.ndimage import gaussian_filter
    fwhm = np.array([fwhm_vox / (2.45 / 2.28), fwhm_vox, fwhm_vox / (3.715 / 2.28)])
    sigma = fwhm / np.sqrt(8 * np.log(2))
    trunc = np.ceil(2 * sigma) / sigma
    out = np.empty_like(vol)
    # gaussian_filter takes one truncate; apply one axis at a time
    tmp = vol
    for ax in range(3):
        tmp = gaussian_filter(tmp, sigma=[sigma[ax] if i == ax else 0 for i in range(3)],
                              truncate=trunc[ax], mode="constant")
    out[:] = tmp
    return out


def second_level(betas):
    """glmFlyMB2nd.m without the Tukey taper: the flies' kept betas stacked, design
    of stacked identity blocks, OLS; t of the walking coefficient with the pooled
    residual variance (df = flies x 7 - 7)."""
    B = np.stack(betas)  # flies x 7 x voxels
    n, k, v = B.shape
    mean = B.mean(0)
    rss = ((B - mean) ** 2).sum((0, 1))
    df = n * k - k
    se = np.sqrt(rss / df / n)
    with np.errstate(invalid="ignore", divide="ignore"):
        t = mean[0] / se
    return t, df


def clusters(mask, connectivity=18):
    from scipy import ndimage
    if connectivity == 18:
        st = ndimage.generate_binary_structure(3, 2)
    elif connectivity == 26:
        st = ndimage.generate_binary_structure(3, 3)
    else:
        st = ndimage.generate_binary_structure(3, 1)
    lab, n = ndimage.label(mask, structure=st)
    sizes = np.bincount(lab.ravel())[1:]
    return lab, sizes
