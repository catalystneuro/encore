"""Loading and per-plane measures for the zebrafish data of Costabile et al. (2023), eLife 12:e83289.

The four dandisets (000235 forebrain, 000236 midbrain, 000237 hindbrain, 000238 reticulospinal
backfills) hold one NWB file per fish. Each file has, for each imaging plane Z<k>: the raw
two-channel two-photon movie (acquisition/Z<k>_0 GCaMP, Z<k>_1 red), CaImAn's segmentation
(pixel masks), CaImAn's inferred calcium (CaUnitRespones_Z<k>) and dF/F, the temperature stimulus
at 20 Hz, and the 250 Hz tail tracking (segment angles and their sum, the cumulative tail angle).

Where each parameter comes from:
- Versions: the only published version of each dandiset (see VERSIONS).
- 5 Hz time base, interpolation, temperature at 20 Hz, bout-start binning, per-bout sums placed at
  the bout's start bin: the paper's code, github.com/haesemeyer/mine_pub at commit 368d756,
  rwave_data_fit.py (interp_times, bin_bout_starts, bin_time_discrete), as the claims file's
  opening comment states.
- Brightness criterion (mean photon count over imaging time of each component, below 0.1
  excluded): Methods, "Processing of zebrafish data", paragraph 2 ("all components for which the
  average brightness across imaging time was <0.1 photons were excluded"), computed as
  Experiment2P.avg_component_brightness in mine_pub/experiment.py (the unweighted mean of the
  time-average projection over the component's pixels). Assumption: the projection is taken of the
  movie the NWB files hold; whether it is CaImAn's motion-corrected movie is not stated.
- Bout detection and tail metrics: the dandisets hold no swim bouts, so they are re-derived. Methods,
  "Processing of zebrafish data", paragraph 1: bout starts from "the absolute angular derivative of
  the tail crossing an empirically determined threshold"; vigor "the sum of the absolute angular
  derivative across the swimbout"; directionality "the sum of the angles of the tip of the tail
  across the swimbout". The procedure is the lab's tail code, bitbucket.org/jcostabile/2p at commit
  5ffaa2d (helper_functions.py, anglePrep and detectBouts, default loThresh 2), which the claims
  file names but did not read. Assumptions: the NWB segment angles are relative, so the point
  angles are their cumulative sum; the tail-tip angle is the circular mean of points 5 to the
  second-last (anglePrep's default); the tip angle summed for directionality is the cumulative tail
  angle the files hold (the code's column name "sum_tail"); the minimum bout length, which the code
  does not fix, is a reading (BOUT_READINGS).
"""
from __future__ import annotations

import hashlib
from functools import lru_cache

import h5py
import numpy as np
import remfile
import requests

API = "https://api.dandiarchive.org/api"
# The only published version of each dandiset (all published on 2023-03-16); the paper cites none.
VERSIONS = {"000235": "0.230316.1600", "000236": "0.230316.2031", "000237": "0.230316.1655",
            "000238": "0.230316.1519"}
ZEBRAFISH_WHOLE_BRAIN = ("000235", "000236", "000237")

DT = 0.2  # 5 Hz common time base (rwave_data_fit.py)
TEMP_RATE = 20.0  # stimulus stored at 20 Hz (rwave_data_fit.py; NWB starting_time rate)
TAIL_RATE = 250.0  # Methods, "Zebrafish experiments"
BRIGHTNESS_CUT = 0.1  # Methods, "Processing of zebrafish data"
# Bout detection readings (loThresh in rad/s, minimum frames per bout at 250 Hz). The threshold is
# "empirically determined" (Methods) and its value for these data is not given; detectBouts' default
# of 2 rad/s lies inside the noise of the tracked tail here (the notebook shows the distribution),
# so 5 and 10 rad/s, above the noise, are the readings, with a minimum length of 10 frames (40 ms)
# or 5 frames (20 ms); the code does not fix the minimum. The default of 2 rad/s is run as a variant.
BOUT_READINGS = {"thr5_min10": (5.0, 10), "thr10_min10": (10.0, 10), "thr5_min5": (5.0, 5),
                 "thr2_min10_code_default": (2.0, 10)}
PRIMARY_BOUTS = "thr5_min10"


def list_assets(dandiset: str) -> list[dict]:
    """Assets of the pinned version: path, asset_id, size."""
    url = f"{API}/dandisets/{dandiset}/versions/{VERSIONS[dandiset]}/assets/?page_size=200"
    out = []
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        j = r.json()
        out += [dict(path=a["path"], asset_id=a["asset_id"], size=a["size"]) for a in j["results"]]
        url = j.get("next")
    return sorted(out, key=lambda a: a["path"])


def version_metadata(dandiset: str) -> dict:
    r = requests.get(f"{API}/dandisets/{dandiset}/versions/{VERSIONS[dandiset]}/", timeout=60)
    r.raise_for_status()
    return r.json()


@lru_cache(maxsize=None)
def s3_url(asset_id: str) -> str:
    r = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60)
    return r.url.split("?")[0]


def open_nwb(asset_id: str) -> h5py.File:
    """Stream an NWB file from the archive (no download to disk)."""
    return h5py.File(remfile.File(s3_url(asset_id)), "r")


def planes(f: h5py.File) -> list[int]:
    ks = [k for k in f["processing/ophys"].keys() if k.startswith("CaUnitRespones_Z")]
    return sorted(int(k.split("_Z")[1]) for k in ks)


def _s(x) -> str:
    return x.decode() if isinstance(x, bytes) else str(x)


def file_metadata(f: h5py.File) -> dict:
    g = f["general"]
    ip = g["optophysiology/Z0_0"]
    return dict(identifier=_s(f["identifier"][()]), subject_id=_s(g["subject/subject_id"][()]),
                genotype=_s(g["subject/genotype"][()]), location=_s(ip["location"][()]),
                imaging_rate=float(ip["imaging_rate"][()]), grid_spacing=float(ip["grid_spacing"][0]),
                session_start=_s(f["session_start_time"][()]),
                frame_duration=float(_s(g["experiment_description"][()]).split(
                    "Frame duration in seconds: ")[1].split("\n")[0]),
                n_zplanes_described=int(_s(g["experiment_description"][()]).split(
                    "Number of ZPlanes: ")[1].split("\n")[0]))


def time_base(n_frames: int, frame_duration: float):
    """Imaging frame times and the 5 Hz interpolation times (rwave_data_fit.py)."""
    ca_t = np.arange(n_frames) * frame_duration
    i_t = np.arange((ca_t[-1] * 1000) // 200) * DT
    return ca_t, i_t


def temperature_5hz(f: h5py.File, p: int, i_t: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    raw = f[f"stimulus/presentation/Temperature_Z{p}/data"][:]
    t = np.arange(raw.size) / TEMP_RATE
    return raw, np.interp(i_t, t, raw)


def mean_projection(f: h5py.File, p: int, channel: int = 0) -> np.ndarray:
    d = f[f"acquisition/Z{p}_{channel}/data"]
    acc = np.zeros(d.shape[1:], dtype=np.float64)
    step = d.chunks[0] if d.chunks else 100
    for i in range(0, d.shape[0], step):
        acc += d[i:i + step].sum(0, dtype=np.float64)
    return acc / d.shape[0]


def masks(f: h5py.File, p: int):
    seg = f[f"processing/ophys/ImageSegmentation/Segmentation_Z{p}"]
    pm = seg["pixel_mask"][:]
    idx = seg["pixel_mask_index"][:].astype(np.int64)
    st = np.r_[0, idx[:-1]]
    return pm, st, idx


def component_brightness(pm, st, idx, proj: np.ndarray) -> np.ndarray:
    """Unweighted mean of the projection over each component's pixels (experiment.py). The NWB
    pixel mask's x is the column and y the row (checked in the notebook)."""
    return np.array([proj[pm["y"][a:b], pm["x"][a:b]].mean() if b > a else np.nan for a, b in zip(st, idx)])


def _filtfilt(x: np.ndarray, w: int) -> np.ndarray:
    """Zero-phase boxcar (2p helper_functions.filtfilt)."""
    if w < 3:
        return x
    s = np.r_[x[w - 1:0:-1], x, x[-1:-w:-1]]
    k = np.ones(w) / w
    y = np.convolve(k, s, mode="valid")
    y = np.convolve(k, y[::-1], mode="valid")
    return y[::-1]


def tail_metrics(seg: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """2p helper_functions.anglePrep on point angles (cumulative sum of the NWB segment angles):
    median filter over 3 frames, circular mean of points 5 to the second-last, absolute frame-to-frame
    change times the frame rate, boxcar of 5 forward and back. Returns the per-frame absolute angular
    derivative (rad/s, before smoothing) and its smoothed version used for bout detection."""
    from scipy.ndimage import median_filter
    ang = np.cumsum(seg, axis=1)
    ang = median_filter(ang, size=(3, 1), mode="nearest")
    ya = np.mean(np.sin(ang[:, 5:-1]), axis=1)
    xa = np.mean(np.cos(ang[:, 5:-1]), axis=1)
    u = np.c_[xa[:-1], ya[:-1]]
    v = np.c_[xa[1:], ya[1:]]
    d = np.arctan2(u[:, 0] * v[:, 1] - u[:, 1] * v[:, 0], np.sum(u * v, axis=1))
    d[np.isnan(d)] = 0
    deriv = np.abs(d * TAIL_RATE)
    sm = np.insert(_filtfilt(deriv, 5), 0, 0)
    return np.insert(deriv, 0, 0), sm


def detect_bouts(metric: np.ndarray, min_frames: int, lo_thresh: float, zero_limit: int = 2) -> np.ndarray:
    """2p helper_functions.detectBouts (hiThresh None): start, peak, end frame of each bout."""
    max_at_peak = 0.02 * TAIL_RATE
    s = metric.copy()
    s[np.isnan(s)] = 0
    s[s < lo_thresh] = 0
    nz = np.nonzero(s)[0]
    out = []
    n = s.size
    k = 0
    while k < nz.size:
        i = nz[k]
        b_start = i
        j = i + 1
        zc = 0
        while j < n and zc <= zero_limit:
            zc = zc + 1 if s[j] == 0 else 0
            j += 1
        b = s[b_start:j]
        b_end = j - (zero_limit + 1)
        pk = b.max()
        if np.sum(b == pk) <= max_at_peak and b.size >= min_frames:
            peak = b_start + int(np.argmax(b))
            bs = b_start - 1 if b_start == peak else b_start
            out.append((bs, peak, b_end))
        k = np.searchsorted(nz, j)
    return np.array(out, dtype=np.int64).reshape(-1, 3)


def behavior_5hz(bouts: np.ndarray, tail_t: np.ndarray, deriv: np.ndarray, tip: np.ndarray,
                 i_t: np.ndarray) -> np.ndarray:
    """Swim starts (count per 5 Hz bin), vigor and direction (per-bout sums placed at the start bin),
    as bin_bout_starts and bin_time_discrete in rwave_data_fit.py. Returns 3 x len(i_t). When two
    bouts start in the same 0.2 s bin the count adds and vigor and direction keep the later bout's
    sum, as the code does (bin_time_discrete assigns, out[di] = np.sum(...); bin_bout_starts counts)."""
    out = np.zeros((3, i_t.size))
    if bouts.size == 0:
        return out
    st = bouts[:, 0].clip(0, tail_t.size - 1)
    en = np.minimum(bouts[:, 2], tail_t.size)
    t0 = tail_t[st]
    ok = (t0 >= 0) & (st < tail_t.size - 1)
    for s, e, t in zip(st[ok], en[ok], t0[ok]):
        bi = int(t // DT)
        if bi >= i_t.size:
            continue
        out[0, bi] += 1
        out[1, bi] = np.sum(deriv[s:e])
        out[2, bi] = np.sum(tip[s:e])
    return out


def digest(a: np.ndarray) -> str:
    return hashlib.sha1(np.ascontiguousarray(a).tobytes()).hexdigest()[:16]


def lagged_corr(x: np.ndarray, Y: np.ndarray, lags: np.ndarray) -> np.ndarray:
    """Pearson correlation of predictor x (T) with each column of Y (T x n) for x leading Y by each lag
    (in samples). Returns len(lags) x n."""
    out = np.full((lags.size, Y.shape[1]), np.nan)
    for i, L in enumerate(lags):
        if L >= 0:
            a, b = x[:x.size - L], Y[L:]
        else:
            a, b = x[-L:], Y[:Y.shape[0] + L]
        a = (a - a.mean()) / (a.std() + 1e-12)
        bz = (b - b.mean(0)) / (b.std(0) + 1e-12)
        out[i] = a @ bz / a.size
    return out


def displaced(x_ext: np.ndarray, o: int, T: int) -> np.ndarray:
    """The first T samples of x displaced by o samples (o > 0 delays x), without wrap-around: sample t
    is x_ext[t - o], NaN where that lies outside x_ext. x_ext may run past T (an advance then reads
    the samples after the end of imaging)."""
    i = np.arange(T) - int(o)
    out = np.full(T, np.nan)
    ok = (i >= 0) & (i < x_ext.size)
    out[ok] = x_ext[i[ok]]
    return out


def heldout_shift_r(x: np.ndarray, Y: np.ndarray, offsets: np.ndarray, hist: int = 50, alpha: float = 1e-4,
                    x_ext: np.ndarray | None = None) -> np.ndarray:
    """Clock check by decoding with the labels shifted in time: Ridge regression (alpha 1e-4, as the
    paper's comparison model) of every component on the predictor x shifted by 0 to hist-1 samples,
    fit on the first two-thirds and scored by the test correlation on the last third; x is first
    displaced by each offset (samples; positive delays x). The displacement does not wrap around:
    rows whose history reaches outside the trace are dropped. (Round 1 wrapped circularly, which put
    a step into the last test rows for every advance and made the advanced curve collapse.) When
    x_ext is given, it is x sampled on the same 5 Hz grid but continued past the end of imaging
    (the temperature trace runs about 10.5 s longer), and advances read it instead of dropping rows.
    Returns len(offsets) x n test correlations."""
    T = x.size
    tr = (T * 2) // 3
    out = np.full((offsets.size, Y.shape[1]), np.nan)
    Yv = Y[hist - 1:]
    rows = np.arange(hist - 1, T)
    src = x if x_ext is None else x_ext
    for i, o in enumerate(offsets):
        xs = displaced(src, int(o), T)
        Xm = np.stack([xs[h:T - hist + 1 + h] for h in range(hist)], axis=1)
        ok = np.isfinite(Xm).all(1)
        trm, tem = ok & (rows < tr), ok & (rows >= tr)
        mu, sd = Xm[trm].mean(0), Xm[trm].std(0) + 1e-9
        A = np.c_[np.ones(trm.sum()), (Xm[trm] - mu) / sd]
        W = np.linalg.solve(A.T @ A + alpha * np.eye(A.shape[1]), A.T @ Yv[trm])
        P = np.c_[np.ones(tem.sum()), (Xm[tem] - mu) / sd] @ W
        Yt = Yv[tem]
        Pz = (P - P.mean(0)) / (P.std(0) + 1e-12)
        Yz = (Yt - Yt.mean(0)) / (Yt.std(0) + 1e-12)
        out[i] = (Pz * Yz).mean(0)
    return out


# Displacements of the temperature for the clock check, samples at 5 Hz: -15 to +10 s at 0.2 s steps
# (the extra 10.5 s of temperature would put the best displacement near -10.5 s if it lay at the
# start), and coarse steps out to +-30 s.
CLOCK_OFFSETS = np.r_[-150, -100, np.arange(-75, 51), 75, 100, 150]


def lm_test_r(P: np.ndarray, Y: np.ndarray, hist: int = 50, alpha: float = 1e-4) -> np.ndarray:
    """The paper's linear comparison model, all components of a plane at once (rwave_data_fit.py,
    analyze_experiment, and utilities.create_time_shifted_predictor_matrix at mine_pub 368d756): the
    standardized predictors (T x m) shifted by 0 to hist-1 samples, the m*hist columns orthonormalized
    by modified Gram-Schmidt, sklearn Ridge(alpha=1e-4) with an intercept fit on the first
    train_frames rows of the shifted matrix and scored on the rows after them, train_frames being
    two-thirds of the calcium frames (the code indexes the shifted matrix by it, as here). Y is the
    T x n z-scored, smoothed calcium; returns the n test correlations."""
    from mine_cnn import modified_gram_schmidt
    T, m = P.shape
    X = np.empty((T - hist + 1, m * hist))
    for j in range(m):
        for h in range(hist):
            X[:, j * hist + h] = P[h:T - hist + 1 + h, j]
    X = modified_gram_schmidt(X)
    tr = (T * 2) // 3
    y = Y[hist - 1:]
    Xa, ya = X[:tr], y[:tr]
    xm, ymu = Xa.mean(0), ya.mean(0)
    Xc = Xa - xm
    W = np.linalg.solve(Xc.T @ Xc + alpha * np.eye(Xc.shape[1]), Xc.T @ (ya - ymu))
    pred = (X[tr:] - xm) @ W + ymu
    yt = y[tr:]
    pz = (pred - pred.mean(0)) / (pred.std(0) + 1e-12)
    yz = (yt - yt.mean(0)) / (yt.std(0) + 1e-12)
    return (pz * yz).mean(0)


def plane_pass(asset_id: str, dandiset: str, p: int, with_movie: bool = True) -> dict:
    """Everything the notebook uses from one plane, reduced as it loads."""
    with open_nwb(asset_id) as f:
        md = file_metadata(f)
        ca = f[f"processing/ophys/CaUnitRespones_Z{p}"]
        C = ca["data"][:]
        rate = float(ca["starting_time"].attrs["rate"])
        n_frames = C.shape[0]
        ca_t, i_t = time_base(n_frames, md["frame_duration"])
        traw, t5 = temperature_5hz(f, p, i_t)
        pl_all = planes(f)
        p_other = pl_all[(pl_all.index(p) + 1) % len(pl_all)]
        _, t5_other = temperature_5hz(f, p_other, i_t)
        tg = f[f"processing/behavior/Raw Tail Behavior Data/Tail_Z{p}"]
        seg = tg["data"][:]
        tail_t = tg["timestamps"][:]
        cum = f[f"processing/behavior/Cumulative Tail Angle/TailCumAngle_Z{p}/data"][:]
        tg_st = f[f"stimulus/presentation/Temperature_Z{p}/starting_time"]
        clocks = dict(ca_start=float(ca["starting_time"][()]), temp_start=float(tg_st[()]),
                      temp_rate=float(tg_st.attrs["rate"]), tail_first=float(tail_t[0]))
        pm, st, idx = masks(f, p)
        rois = f[f"processing/ophys/CaUnitRespones_Z{p}/rois"][:]
        proj = mean_projection(f, p, 0) if with_movie else None
        mshape = f[f"acquisition/Z{p}_0/data"].shape
        mshape1 = f[f"acquisition/Z{p}_1/data"].shape if f"Z{p}_1" in f["acquisition"] else None
    dtail = np.diff(tail_t)
    jump = int(np.argmax(np.abs(dtail - np.median(dtail))))
    clocks.update(tail_max_step=float(dtail[jump]), tail_max_step_at=float(tail_t[jump]),
                  tail_max_step_index=jump, tail_steps_over_1s=int(np.sum(np.abs(dtail) > 1)))
    deriv, sm = tail_metrics(seg)
    beh = {}
    nb = {}
    for name, (thr, mn) in BOUT_READINGS.items():
        b = detect_bouts(sm, mn, thr)
        nb[name] = int(b.shape[0])
        beh[name] = behavior_5hz(b, tail_t, deriv, cum, i_t)
    out = dict(dandiset=dandiset, asset_id=asset_id, fish=md["subject_id"], plane=p, n_rois=C.shape[1],
               n_rois_masks=int(st.size), rois_ok=bool(np.array_equal(rois, np.arange(C.shape[1]))),
               n_frames=n_frames, ca_rate=rate, frame_duration=md["frame_duration"], movie_shape=mshape,
               movie_shape_red=mshape1, temp_n=traw.size, temp_min=float(traw.min()), temp_max=float(traw.max()),
               temp5=t5, tail_n=tail_t.size, tail_t0=float(tail_t[0]), tail_t1=float(tail_t[-1]),
               tail_dt=float(np.median(np.diff(tail_t))), tail_nan=int(np.isnan(seg).sum()),
               cum_matches_sum=float(np.nanmax(np.abs(seg.sum(1) - cum))), n_bouts=nb, behavior=beh,
               ca_min=float(C.min()), ca_max=float(C.max()), ca_nan=int(np.isnan(C).sum()),
               digest_ca=digest(C), digest_temp=digest(traw), digest_tail=digest(cum),
               mask_x_max=int(pm["x"].max()) if pm.size else -1, mask_y_max=int(pm["y"].max()) if pm.size else -1,
               clocks=clocks, n_bins_multi_bout={k: int(np.sum(v[0] > 1)) for k, v in beh.items()})
    if proj is not None:
        br = component_brightness(pm, st, idx, proj)
        out["brightness"] = br
        out["proj_mean"] = float(proj.mean())
        # Clock check: bright components, z-scored and smoothed as rwave_data_fit.py, on the 5 Hz base.
        from scipy.ndimage import gaussian_filter1d
        keep = br >= BRIGHTNESS_CUT
        if keep.sum() >= 5:
            Ci = np.vstack([np.interp(i_t, ca_t, c) for c in C[:, keep].T]).T
            Ci = (Ci - Ci.mean(0)) / (Ci.std(0) + 1e-9)
            Ci = gaussian_filter1d(Ci, 2.5, axis=0)
            lags = np.arange(-50, 151, 5)  # -10 s to +30 s
            rt = lagged_corr(t5, Ci, lags)
            out["clock_lags_s"] = lags * DT
            ntop = max(1, keep.sum() // 20)
            out["clock_temp_top"] = np.sort(np.abs(rt), axis=1)[:, -ntop:].mean(1)
            # mismatch control: the temperature trace of the next plane of the same fish
            ro = lagged_corr(t5_other, Ci, lags)
            out["clock_temp_other_top"] = np.sort(np.abs(ro), axis=1)[:, -ntop:].mean(1)
            # the temperature on the 5 Hz grid over its whole length (it runs past the end of imaging)
            t5_ext = np.interp(np.arange(int(traw.size / TEMP_RATE / DT)) * DT, np.arange(traw.size) / TEMP_RATE, traw)
            ho = heldout_shift_r(t5, Ci, CLOCK_OFFSETS, x_ext=t5_ext)
            out["clock_ho_temp"] = np.sort(ho, axis=1)[:, -ntop:].mean(1)
            out["clock_ho_temp_mean"] = ho.mean(1)
            out["clock_ho_offsets_s"] = CLOCK_OFFSETS * DT
            # The linear comparison model of the paper on every bright component, under each bout reading
            from mine_cnn import prepare_predictors
            out["lm_r"] = {}
            for name in BOUT_READINGS:
                r_ = np.full(C.shape[1], np.nan)
                r_[keep] = lm_test_r(prepare_predictors(t5, beh[name]).astype(np.float64), Ci)
                out["lm_r"][name] = r_
            ho_o = heldout_shift_r(t5_other, Ci, CLOCK_OFFSETS[CLOCK_OFFSETS == 0])
            out["clock_ho_temp_other"] = float(np.sort(ho_o[0])[-ntop:].mean())
            s5 = beh[PRIMARY_BOUTS][0]
            if s5.sum() >= 3:
                lags_b = np.arange(-25, 51, 1)  # -5 s to +10 s
                rb = lagged_corr(s5, Ci, lags_b)
                out["clock_bout_lags_s"] = lags_b * DT
                out["clock_bout_top"] = np.sort(rb, axis=1)[:, -ntop:].mean(1)
    return out
