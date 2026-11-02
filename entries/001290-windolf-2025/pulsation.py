"""Loading, spike detection, DREDge registration and the fast-motion spline for dandiset 001290.

Windolf et al. (2025), "DREDge: robust motion correction for high-density extracellular
recordings across species", Nature Methods, doi:10.1038/s41592-025-02614-5. The dandiset holds
one NWB file: a Neuropixels 1.0 recording (384 channels, AP band at 30 kHz and LF band at
2.5 kHz, about 600 s) in an anesthetized macaque, the "fast-motion NHP dataset of Extended Data
Fig. 3" (Data availability). The file is streamed from the archive at the pinned version, in
blocks that follow its HDF5 chunks (78,125 samples by 64 channels); nothing is written to disk.

Where the parameters come from (the claims file is claims/001290/10.1038-s41592-025-02614-5.yaml,
whose opening comment calls these steps "the pipeline"):

- Spike detection and localization, reading (ii) of pipeline step 1 of the claims file:
  SpikeInterface bandpass_filter (300 to 6,000 Hz, its defaults), common_reference (global
  median), detect_peaks (locally_exclusive, detect_threshold 6, peak_sign "both") and
  localize_peaks (monopolar_triangulation, radius 75 um), as in notebook/ap_registration.ipynb of
  github.com/evarol/dredge at commit ed236113. The noise levels for the threshold are the median
  absolute deviation per channel, scaled to a standard deviation, of the preprocessed signal,
  taken as the median over `N_NOISE_BLOCKS` blocks spread over the recording; SpikeInterface's
  get_noise_levels does the same on random chunks, so this is a standard choice that changes
  no result. Spikes are kept as detect_peaks returns them.
- Reading (i) of pipeline step 1 (IBL preprocessing, then DARTsort detection, denoising and
  localization) is not run: see the notebook's header.
- Registration, pipeline step 2: dredge_ap.register at commit ed236113 with bin 1 um by 1 s,
  amplitudes log(1 + x) transformed, summed and log(1 + x) transformed again (amp_scale_fn and
  post_transform np.log1p), Gaussian smoothing at 1 um and 1 s (Methods, "Preprocessing of AP
  band data" and "Setting parameters", paragraph 4; the claims file reads the code's default,
  None, as no smoothing, but motion_util.spike_raster replaces None with the bin size, 1 um and
  1 s, so the two are the same, as the notebook shows), mincorr 0.1, max_dt_s 1,000 s, lambda_t and lambda_s 1 (Methods, "Robust
  decentralized registration"). Reading (a) is nonrigid with the code's window defaults
  (win_step_um 400, win_scale_um 450, max_disp_um win_scale_um / 4); reading (b) is rigid.
- Workers: the blocks are split into contiguous runs over 4 processes, with linear-algebra
  threads limited to one (the notebook sets this before importing numpy).
- Template correlation (Methods, "Spike registration quality metrics"): raster of mean
  amplitude in 1 um by 1 s bins of the corrected depths, bins outside the probe after correction
  masked, the masked mean over time as template, the masked Pearson correlation of each time
  bin with it, averaged over time bins. Bins with no spike inside the probe are zero, not
  masked: the Methods mask only bins outside the probe.
- Fast motion, pipeline step 3 (Methods, "Tracking fast motion from spikes using clustering and
  splines"): HDBSCAN on registered location and amplitude features of high-amplitude spikes;
  centroid subtraction per cluster; removal of points more than five standard deviations from
  the cluster mean; one cubic spline with 2.5 knots per second (interior knots every 0.4 s) fit
  to all centred depths at once. The open readings (amplitude cut, coordinates,
  min_cluster_size, penalty) are those the claims file names; z-scored features and a cubic
  spline are its standard choices. The penalized reading is a P-spline (cubic B-splines on the
  same knots, second-difference penalty) with the penalty chosen by generalized
  cross-validation over a grid of 17 values from 1e-3 to 1e5 (a standard choice). The outlier
  rule is applied to depth, the coordinate the spline models (a standard choice).
- The scrambled control of claim edf3c-spline-subsecond (0.4 s bins, 100 permutations, 5%
  level) is the claims file's.
"""

from __future__ import annotations

import os
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import remfile

DANDISET_ID = "001290"
DANDISET_VERSION = "0.260827.1449"
ASSET_PATH = "sub-L11104/sub-L11104_ses-None_ecephys.nwb"
AP_PATH = "acquisition/ElectricalSeriesAPImec"
LF_PATH = "acquisition/ElectricalSeriesLFImec"

BLOCK = 78_125            # samples, the HDF5 chunk length of the AP series (2.604 s)
MARGIN = 3_000            # samples taken from the neighbouring blocks for filter edges (standard)
N_NOISE_BLOCKS = 12       # blocks used for the noise levels (standard)
DETECT_THRESHOLD = 6.0    # ap_registration.ipynb
LOCAL_RADIUS_UM = 75.0    # ap_registration.ipynb

SPLINE_KNOTS_PER_S = 2.5  # Methods
OUTLIER_SD = 5.0          # Methods


def asset_url() -> str:
    from dandi.dandiapi import DandiAPIClient

    with DandiAPIClient() as client:
        asset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION).get_asset_by_path(ASSET_PATH)
        return asset.get_content_url(follow_redirects=1, strip_query=True)


def open_file(url: str) -> h5py.File:
    return h5py.File(remfile.File(url), "r")


def probe_geometry(f: h5py.File):
    """Channel x and y (um) and inter-sample shift of the 384 AP channels."""
    rows = f[AP_PATH]["electrodes"][:]
    table = f["general/extracellular_ephys/electrodes"]
    x = table["rel_x"][:][rows]
    y = table["rel_y"][:][rows]
    shift = table["inter_sample_shift"][:][rows]
    return np.c_[x, y], shift


def _numpy_recording(traces_uv, fs, locations, shift=None):
    import spikeinterface.core as sc

    rec = sc.NumpyRecording(traces_uv, fs)
    rec.set_dummy_probe_from_locations(locations)
    if shift is not None:
        rec.set_property("inter_sample_shift", shift)
    return rec


def preprocess_ii(rec):
    """Reading (ii): bandpass 300 to 6,000 Hz and global median reference (ap_registration.ipynb)."""
    import spikeinterface.preprocessing as sp

    return sp.common_reference(sp.bandpass_filter(rec, freq_min=300.0, freq_max=6000.0))


def _read_block(dset, k, n_blocks, gain):
    start = k * BLOCK
    stop = min((k + 1) * BLOCK, dset.shape[0])
    return dset[start:stop, :].astype(np.float32) * gain


def _padded(prev, cur, nxt):
    parts, left = [], 0
    if prev is not None:
        parts.append(prev[-MARGIN:])
        left = MARGIN
    parts.append(cur)
    if nxt is not None:
        parts.append(nxt[:MARGIN])
    return np.concatenate(parts, axis=0), left


def _traces(rec):
    return rec.get_traces(segment_index=0)


def _mad_sd(x):
    return np.median(np.abs(x - np.median(x, axis=0)), axis=0) / 0.6744897501960817


def noise_levels(url, n_blocks_used=N_NOISE_BLOCKS):
    """Per-channel noise (sd from the MAD) of the preprocessed signal, median over blocks."""
    with open_file(url) as f:
        d = f[AP_PATH]["data"]
        gain = d.attrs["conversion"] * 1e6
        fs = float(f[AP_PATH]["starting_time"].attrs["rate"])
        locs, shift = probe_geometry(f)
        n_blocks = int(np.ceil(d.shape[0] / BLOCK))
        ks = np.linspace(1, n_blocks - 2, n_blocks_used).astype(int)
        out = []
        for k in ks:
            cur = _read_block(d, k, n_blocks, gain)
            rec = _numpy_recording(cur, fs, locs, shift)
            rec = preprocess_ii(rec)
            tr = _traces(rec)[MARGIN:-MARGIN]
            out.append(_mad_sd(tr))
    return np.median(np.array(out), axis=0)


def _detect_block(padded, left, n_core, fs, locs, shift, noise, block_index):
    from spikeinterface.sortingcomponents.peak_detection import detect_peaks
    from spikeinterface.sortingcomponents.peak_localization import localize_peaks

    rec = _numpy_recording(padded, fs, locs, shift)
    rec = preprocess_ii(rec)
    job = dict(n_jobs=1, progress_bar=False, chunk_duration="10s")
    peaks = detect_peaks(rec, method="locally_exclusive", method_kwargs=dict(
        detect_threshold=DETECT_THRESHOLD, peak_sign="both", noise_levels=noise,
        radius_um=50.0), job_kwargs=job)
    keep = (peaks["sample_index"] >= left) & (peaks["sample_index"] < left + n_core)
    peaks = peaks[keep]
    if len(peaks) == 0:
        return np.zeros((0, 6))
    locs_out = localize_peaks(rec, peaks, method="monopolar_triangulation",
                              method_kwargs=dict(radius_um=LOCAL_RADIUS_UM), job_kwargs=job)
    t = (peaks["sample_index"] - left + block_index * BLOCK) / fs
    return np.c_[t, np.abs(peaks["amplitude"]), locs_out["x"], locs_out["y"], locs_out["z"],
                 peaks["channel_index"]]


def _worker(args):
    url, ks, noise = args
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    with open_file(url) as f:
        d = f[AP_PATH]["data"]
        gain = d.attrs["conversion"] * 1e6
        fs = float(f[AP_PATH]["starting_time"].attrs["rate"])
        locs, shift = probe_geometry(f)
        n_blocks = int(np.ceil(d.shape[0] / BLOCK))
        out = []
        prev = _read_block(d, ks[0] - 1, n_blocks, gain) if ks[0] > 0 else None
        cur = _read_block(d, ks[0], n_blocks, gain)
        for i, k in enumerate(ks):
            nxt = _read_block(d, k + 1, n_blocks, gain) if k + 1 < n_blocks else None
            padded, left = _padded(prev, cur, nxt)
            out.append(_detect_block(padded, left, len(cur), fs, locs, shift, noise, k))
            prev, cur = cur, nxt
    return np.concatenate(out, axis=0)


def detect_spikes(url, blocks=None, noise=None, n_workers=4):
    """Detect and localize spikes block by block, streaming the AP series.

    Returns a dict of arrays: t (s), amp (uV, absolute peak amplitude), x, y (depth), z (um),
    channel. `blocks` limits the run to a subset of block indices (for development).
    """
    with open_file(url) as f:
        n_blocks = int(np.ceil(f[AP_PATH]["data"].shape[0] / BLOCK))
    if blocks is None:
        blocks = np.arange(n_blocks)
    blocks = np.asarray(blocks)
    if noise is None:
        noise = noise_levels(url)
    # contiguous runs of blocks per worker, so each block is read once
    runs = [r for r in np.array_split(blocks, n_workers * 3) if len(r)]
    with ProcessPoolExecutor(n_workers) as ex:
        parts = list(ex.map(_worker, [(url, r, noise) for r in runs]))
    a = np.concatenate(parts, axis=0)
    a = a[np.argsort(a[:, 0], kind="stable")]
    return dict(t=a[:, 0], amp=a[:, 1], x=a[:, 2], y=a[:, 3], z=a[:, 4],
                channel=a[:, 5].astype(int))


# --- registration -------------------------------------------------------------

def register(sp, rigid, smooth=True):
    """DREDge AP registration with the parameters of pipeline step 2 (see the docstring)."""
    from dredge.dredge_ap import register as dredge_register

    sigma = 1.0 if smooth else None
    me, extra = dredge_register(
        sp["amp"], sp["y"], sp["t"], rigid=rigid, bin_um=1.0, bin_s=1.0, max_dt_s=1000,
        mincorr=0.1, win_step_um=400, win_scale_um=450, amp_scale_fn=np.log1p,
        post_transform=np.log1p, gaussian_smoothing_sigma_um=sigma,
        gaussian_smoothing_sigma_s=sigma, thomas_kw=dict(lambda_t=1.0, lambda_s=1.0),
        device="cpu", pbar=False)
    return me


def displacement_at_spikes(me, sp):
    return me.disp_at_s(sp["t"], sp["y"])


# --- template correlation -----------------------------------------------------

def template_correlation(t, depth, amp, probe_lo_t, probe_hi_t, bin_s=1.0, bin_um=1.0,
                         t_max=None):
    """Mean template correlation (Methods, "Spike registration quality metrics").

    `depth` are the (corrected) spike depths; `probe_lo_t` and `probe_hi_t` are functions of
    time bin centres giving the extent of the probe in the same corrected coordinates, outside
    which bins are masked. Returns (mean correlation, per-bin correlations).
    """
    t_max = t.max() if t_max is None else t_max
    tedges = np.arange(0.0, t_max + bin_s, bin_s)
    tc = 0.5 * (tedges[1:] + tedges[:-1])
    lo, hi = probe_lo_t(tc), probe_hi_t(tc)
    dedges = np.arange(np.floor(lo.min()) - bin_um, np.ceil(hi.max()) + 2 * bin_um, bin_um)
    dc = 0.5 * (dedges[1:] + dedges[:-1])
    s, _, _ = np.histogram2d(depth, t, bins=(dedges, tedges), weights=amp)
    n, _, _ = np.histogram2d(depth, t, bins=(dedges, tedges))
    raster = np.divide(s, n, out=np.zeros_like(s), where=n > 0)
    mask = (dc[:, None] >= lo[None, :]) & (dc[:, None] <= hi[None, :])
    cnt = mask.sum(1)
    template = np.divide((raster * mask).sum(1), cnt, out=np.zeros(len(dc)), where=cnt > 0)
    corrs = np.full(len(tc), np.nan)
    for j in range(len(tc)):
        m = mask[:, j]
        a, b = raster[m, j], template[m]
        a = a - a.mean()
        b = b - b.mean()
        den = np.sqrt((a * a).sum() * (b * b).sum())
        if den > 0:
            corrs[j] = (a * b).sum() / den
    return np.nanmean(corrs), corrs


def probe_extent(me, y_lo, y_hi, extra=None):
    """Functions of time giving the corrected depths of the probe's two ends.

    `extra`, if given, is a function of time subtracted as well (the spline)."""
    def f(y):
        def g(tc):
            d = np.full(len(tc), float(y)) if me is None else me.correct_s(tc, np.full(len(tc), float(y)))
            return d - (0 if extra is None else extra(tc))
        return g
    return f(y_lo), f(y_hi)


# --- fast motion: clustering and spline ----------------------------------------

def select_high_amplitude(amp, top_fraction):
    return amp >= np.quantile(amp, 1.0 - top_fraction)


def cluster_spikes(features, min_cluster_size):
    """HDBSCAN (scikit-learn) on z-scored features; returns labels (-1 is noise)."""
    from sklearn.cluster import HDBSCAN

    z = (features - features.mean(0)) / features.std(0)
    return HDBSCAN(min_cluster_size=min_cluster_size).fit_predict(z)


def center_clusters(depth, labels, outlier_sd=OUTLIER_SD):
    """Subtract each cluster's mean depth and drop points over `outlier_sd` s.d. from it.

    Returns (keep mask over the input, centred depth, labels) for the kept points. The Methods
    say "points more than five standard deviations from the mean in each cluster"; the s.d. is
    taken on depth, the coordinate the spline models (a standard choice)."""
    keep = labels >= 0
    centred = np.zeros_like(depth)
    for c in np.unique(labels[keep]):
        m = labels == c
        mu, sd = depth[m].mean(), depth[m].std()
        out = m & (np.abs(depth - mu) > outlier_sd * sd)
        keep &= ~out
        mm = m & keep
        centred[mm] = depth[mm] - depth[mm].mean()
    return keep, centred[keep], labels[keep]


def _knots(t0, t1):
    step = 1.0 / SPLINE_KNOTS_PER_S
    return np.arange(t0 + step, t1 - step / 2, step)


def fit_spline(t, y, t0, t1, penalized=False, lambdas=None):
    """Cubic spline in time with interior knots every 0.4 s (2.5 per second).

    Least squares (penalized=False), or a P-spline on the same knots with a second-difference
    penalty chosen by generalized cross-validation. Returns (callable, info dict)."""
    from scipy.interpolate import BSpline
    from scipy.sparse import diags

    k = 3
    inner = _knots(t0, t1)
    knots = np.r_[[t0] * (k + 1), inner, [t1] * (k + 1)]
    B = BSpline.design_matrix(np.clip(t, t0, t1), knots, k).tocsc()
    nb = B.shape[1]
    BtB = (B.T @ B).toarray()
    Bty = B.T @ y
    if not penalized:
        # minimum-norm least squares: coefficients of knot intervals with no data (gaps in the
        # clustered spikes) are left near zero in place of arbitrary values (a numerical choice)
        coef, _, rank, _ = np.linalg.lstsq(BtB, Bty, rcond=1e-8)
        info = dict(lam=0.0, edf=float(rank))
    else:
        D = diags([1.0, -2.0, 1.0], [0, 1, 2], shape=(nb - 2, nb)).toarray()
        P = D.T @ D
        lambdas = np.logspace(-3, 5, 17) if lambdas is None else lambdas
        n = len(y)
        best = None
        gcvs = []
        for lam in lambdas:
            A = BtB + lam * P
            Ainv = np.linalg.inv(A)
            c = Ainv @ Bty
            rss = float(np.sum((y - B @ c) ** 2))
            edf = float(np.trace(Ainv @ BtB))
            gcv = n * rss / (n - edf) ** 2
            gcvs.append(gcv)
            if best is None or gcv < best[0]:
                best = (gcv, lam, c, edf)
        coef = best[2]
        info = dict(lam=float(best[1]), edf=best[3], gcv=np.array(gcvs), lambdas=lambdas)
    spl = BSpline(knots, coef, k, extrapolate=False)

    def f(tt):
        return np.nan_to_num(spl(np.clip(tt, t0, t1)))
    return f, info


def pooled_within_sd(values, labels):
    """Pooled within-cluster standard deviation."""
    ss, n, kk = 0.0, 0, 0
    for c in np.unique(labels):
        v = values[labels == c]
        ss += float(np.sum((v - v.mean()) ** 2))
        n += len(v)
        kk += 1
    return np.sqrt(ss / (n - kk))


def scrambled_traces(spline, t, t0, t1, n_perm, rng, bin_s=1.0 / SPLINE_KNOTS_PER_S):
    """The spline evaluated with its time bins (of `bin_s`) randomly permuted, at times t."""
    edges = np.arange(t0, t1 + bin_s, bin_s)
    nbin = len(edges) - 1
    b = np.clip(np.searchsorted(edges, t, side="right") - 1, 0, nbin - 1)
    offset = t - edges[b]
    for _ in range(n_perm):
        perm = rng.permutation(nbin)
        yield spline(edges[perm[b]] + offset)
