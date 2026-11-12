"""Loading and measures for dandiset 001871 (Brudner, Zhou et al. 2026, PNAS, doi:10.1073/pnas.2608896123).

The dandiset holds two kinds of NWB file, streamed here from the archive at the pinned version
into memory (nothing is written to disk):

- Behavior files, one per recording session (trial) of a fly cohort. Per fly trajectory
  (`full_trjn`) they hold the centroid position (mm), heading `theta` and `theta_smooth`
  (degrees, 180 = upwind), `dtheta` (degrees/s), `vx`, `vy`, `spd` (mm/s), and the odor signals
  at the antennae, `signal` (intensity), `spatial_gradient` and `odor_velocity` (motion), all at
  60 Hz; and a `turn_events` table (start, stop, direction, heading, x, y, trajectory).
  Smooth-plume files have "nagel-smoke" in their path, complex-plume files "smoke-1a" or
  "smoke-2a".
- Plume movies: the complex smoke plume (frames 300 to 1799 of smoke_1a_orig, 1500 x 1088 x 1728,
  float32, 0 to 255) and three freestream plumes, with a compact asset of Fig. S1 panel inputs.
  The smooth plume is not in the dandiset.

Where the parameters come from (claims file `claims/brudner-2026.yaml`, which cites the paper's
SI Appendix and the code github.com/emonetlab/GradientMotionMultiplePlumes at commit
effc7b0317f6d3b62136c2a07bcba3e80e778575, `src/gradient_motion_panels/summary_tables.py` and
`metadata/published_panel_params.json`):

- Turn filters (`TurnOptions`): heading 160 to 200 degrees (SI, Behavioral Analysis; the code uses
  150 to 210 in the complex plume, a named reading); walking upwind, the trajectory's vx
  low-passed by a 4th-order Butterworth at 0.2 Hz (filtfilt) and negative (code); turn position
  30 <= x <= 220 mm and 67 <= y <= 97 mm (code); the code's 15 mm margin inside the 1st and 99th
  percentiles of the plume's positions, a named reading.
- Predictors: `spatial_gradient`, `odor_velocity`, `signal`, each smoothed by the code's causal
  exponential filter (time constant 200 ms, NaN holds the last value), taken at the last frame at
  or before 50 ms before turn onset, within one frame (code `merge_asof`, SI).
- Turn onset: the dataset's turn start (what the code uses), or the SI's rule, the time the
  rotational speed crosses 20% of the turn's peak on the rising edge (`onset_20pct`). The search
  window for the peak, the event's start to stop, is a standard choice.
- Which complex-plume files: the code selects "smoke-2a" only; the paper does not say, and the
  Yale Dataverse deposit of the same sessions (doi:10.60600/YU/590UBV) files both "smoke_1a" and
  "smoke_2a" sessions as complex plume. Both are run (the notebook's readings).
- Logistic regression of turn direction (direction > 0 coded 1, as the code does) on the
  predictors with an intercept, cluster-robust SE grouped by trajectory (statsmodels, code).
  The four models of Fig. 5F and the cue dominance (LL_grad - LL_motion) / (LL_full - LL_base),
  LL per turn, are the code's `VARIANT_FORMULAS`.

Complex-plume movie measures (`complex_movie_pass`) are documented at the function.
"""

from __future__ import annotations

import io
import math
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, replace

import h5py
import numpy as np
import pandas as pd
import requests
from scipy.signal import butter, filtfilt

DANDISET_ID = "001871"
DANDISET_VERSION = "0.260630.1657"
API = "https://api.dandiarchive.org/api"

SERIES = ("theta", "theta_smooth", "dtheta", "vx", "vy", "spd", "signal", "spatial_gradient",
          "odor_velocity")
PREDICTORS = {"gradient": "spatial_gradient", "motion": "odor_velocity", "intensity": "signal"}


# ----------------------------------------------------------------------------------------------
# Archive access
# ----------------------------------------------------------------------------------------------

def list_assets() -> pd.DataFrame:
    """Every asset of the pinned version: path, asset_id, size (bytes)."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=200"
    rows = []
    while url:
        page = requests.get(url, timeout=60).json()
        rows += [{"path": a["path"], "asset_id": a["asset_id"], "size": a["size"]} for a in page["results"]]
        url = page.get("next")
    return pd.DataFrame(rows).sort_values("path").reset_index(drop=True)


def asset_url(asset_id: str) -> str:
    """The S3 URL of an asset (the archive's download endpoint, redirect followed)."""
    r = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60)
    return r.url


def fetch(asset_id: str) -> bytes:
    """An asset's bytes, streamed into memory (behavior files are 1 to 18 MB)."""
    for attempt in range(4):
        try:
            r = requests.get(f"{API}/assets/{asset_id}/download/", timeout=300)
            r.raise_for_status()
            return r.content
        except requests.RequestException:
            if attempt == 3:
                raise
    raise RuntimeError("unreachable")


def plume_of(path: str) -> str | None:
    """Plume group of a behavior file from its path (the code's path substrings)."""
    p = path.lower()
    if not p.endswith("_behavior.nwb") or "figs1" in p:
        return None
    if "nagel-smoke" in p:
        return "smooth"
    if "smoke-2a" in p:
        return "complex_2a"
    if "smoke-1a" in p:
        return "complex_1a"
    return None


# ----------------------------------------------------------------------------------------------
# Behavior files
# ----------------------------------------------------------------------------------------------

def _text(v) -> str:
    v = v[()] if hasattr(v, "shape") else v
    return v.decode() if isinstance(v, bytes) else str(v)


def read_behavior(path: str, asset_id: str) -> dict:
    """One behavior file: session metadata, per-trajectory frames (DataFrame) and turn events."""
    raw = fetch(asset_id)
    with h5py.File(io.BytesIO(raw), "r") as f:
        pos = f["processing/behavior/position"]
        der = f["processing/behavior/derived_signals"]
        frames = []
        rates = set()
        for name in pos:
            trj = int(name.rsplit("_", 1)[1])
            s = pos[name]
            xy = s["data"][:]
            if "timestamps" in s:
                t = s["timestamps"][:]
                rates.add("timestamps")
            else:
                st = s["starting_time"]
                rate = float(st.attrs["rate"])
                rates.add(round(rate, 3))
                t = float(st[()]) + np.arange(len(xy)) / rate
            d = {"trj": trj, "t": t, "x": xy[:, 0], "y": xy[:, 1]}
            for v in SERIES:
                ds = der[f"{v}_full_trjn_{trj}"]
                arr = ds["data"][:]
                if len(arr) != len(xy):
                    raise ValueError(f"{path}: {v} of trajectory {trj} has {len(arr)} samples, xy {len(xy)}")
                d[v] = arr
            frames.append(pd.DataFrame(d))
        te = f["intervals/turn_events"]
        turns = pd.DataFrame({k: te[k][:] for k in te if k not in ("id",)})
        units = {v: der[f"{v}_full_trjn_{frames[0].trj.iloc[0]}/data"].attrs.get("unit") for v in SERIES}
        info = {
            "path": path,
            "session_id": _text(f["general/session_id"]),
            "description": _text(f["session_description"]),
            "start": _text(f["session_start_time"]),
            "subject_id": _text(f["general/subject/subject_id"]),
            "n_bytes": len(raw),
            "units": units,
            "xy_unit": pos[next(iter(pos))]["data"].attrs.get("unit"),
            "rates": sorted(rates, key=str),
        }
    fr = pd.concat(frames, ignore_index=True)
    fr["session"] = info["session_id"]
    turns = turns.rename(columns={"full_trjn": "trj"})
    turns["session"] = info["session_id"]
    return {"info": info, "frames": fr, "turns": turns}


def load_behavior(assets: pd.DataFrame, workers: int = 4) -> list[dict]:
    """Read many behavior files in parallel threads (each is held in memory only while parsed)."""
    rows = list(assets[["path", "asset_id"]].itertuples(index=False))
    with ThreadPoolExecutor(workers) as ex:
        out = list(ex.map(lambda r: read_behavior(r.path, r.asset_id), rows))
    for s, r in zip(out, rows):
        s["info"]["plume"] = plume_of(r.path)
    return out


# ----------------------------------------------------------------------------------------------
# Turn table of Fig. 5
# ----------------------------------------------------------------------------------------------

@dataclass(frozen=True)
class TurnOptions:
    heading: tuple[float, float] = (160.0, 200.0)   # SI; the code's complex reading is (150, 210)
    margin: bool = False                             # the code's 15 mm margin (not in the SI)
    zscore: str = "none"                             # "none" (code), "pooled", "per_trajectory"
    tau_ms: float = 200.0
    offset_s: float = 0.05
    x_range: tuple[float, float] = (30.0, 220.0)
    y_range: tuple[float, float] = (67.0, 97.0)
    margin_mm: float = 15.0
    bounds_quantile: float = 0.01
    vx_cutoff_hz: float = 0.2
    vx_order: int = 4


def exp_smooth(x: np.ndarray, fps: float, tau_ms: float) -> np.ndarray:
    """The code's causal exponential filter: y[0] = x[0] (0 if NaN); NaN holds the last value."""
    alpha = 1.0 - math.exp(-(1.0 / fps) / (tau_ms / 1000.0))
    y = np.empty(len(x))
    if len(x) == 0:
        return y
    prev = 0.0 if np.isnan(x[0]) else float(x[0])
    y[0] = prev
    for i in range(1, len(x)):
        v = x[i]
        if not np.isnan(v):
            prev = alpha * v + (1.0 - alpha) * prev
        y[i] = prev
    return y


def _exp_smooth_fast(x: np.ndarray, fps: float, tau_ms: float) -> np.ndarray:
    """Same as `exp_smooth`, vectorised with scipy.signal.lfilter where there are no NaNs."""
    if len(x) < 2 or np.isnan(x).any():
        return exp_smooth(x, fps, tau_ms)
    from scipy.signal import lfilter
    alpha = 1.0 - math.exp(-(1.0 / fps) / (tau_ms / 1000.0))
    # y[i] = alpha x[i] + (1 - alpha) y[i-1], with y[0] = x[0]
    y, _ = lfilter([alpha], [1.0, -(1.0 - alpha)], x[1:], zi=[(1.0 - alpha) * x[0]])
    return np.concatenate([[x[0]], y])


def _butter_vx(vx: np.ndarray, fps: float, cutoff: float, order: int) -> np.ndarray:
    """The code's `_butterworth_or_raw`: interpolate NaNs, then zero-phase low-pass."""
    arr = pd.Series(vx).interpolate(limit_direction="both").to_numpy(float)
    nyq = 0.5 * fps
    b, a = butter(order, cutoff / nyq, btype="low")
    if len(arr) <= 3 * max(len(a), len(b)):
        return arr
    return filtfilt(b, a, arr)


def onset_20pct(t: np.ndarray, rot_speed: np.ndarray, start: float, stop: float) -> tuple[float, float, float, int, int]:
    """SI turn onset: the time rotational speed crosses 20% of the turn's peak on the rising edge.

    The peak is the largest |dtheta| between the event's start and stop (a standard choice); the
    onset is the first frame of the run of frames at or above 20% of the peak that contains the
    peak. Returns (onset time, peak time, peak speed, first and last index of that run).
    """
    i0, i1 = np.searchsorted(t, [start - 1e-9, stop + 1e-9])
    if i1 <= i0 or np.all(np.isnan(rot_speed[i0:i1])):
        return np.nan, np.nan, np.nan, -1, -1
    ip = i0 + int(np.nanargmax(rot_speed[i0:i1]))
    peak = rot_speed[ip]
    j = ip
    while j > 0 and rot_speed[j - 1] >= 0.2 * peak:
        j -= 1
    e = ip
    while e < len(t) - 1 and rot_speed[e + 1] >= 0.2 * peak:
        e += 1
    return float(t[j]), float(t[ip]), float(peak), j, e


def prepare_frames(frames: pd.DataFrame, opts: TurnOptions) -> pd.DataFrame:
    """Per-trajectory derived columns: smoothed vx (`vx_smooth`) and the smoothed predictors
    (`gradient_s`, `motion_s`, `intensity_s`, and their z-scores over all frames of the group,
    `*_zp`, and per trajectory, `*_zt`)."""
    out = []
    for (_, _), g in frames.groupby(["session", "trj"], sort=False):
        g = g.sort_values("t").copy()
        dt = np.diff(g.t.to_numpy())
        dt = dt[np.isfinite(dt) & (dt > 0)]
        fps = 1.0 / np.median(dt) if dt.size else 60.0
        g["vx_smooth"] = _butter_vx(g.vx.to_numpy(float), fps, opts.vx_cutoff_hz, opts.vx_order)
        for name, col in PREDICTORS.items():
            v = _exp_smooth_fast(g[col].to_numpy(float), fps, opts.tau_ms)
            g[f"{name}_s"] = v
            sd = np.nanstd(v, ddof=1) if len(v) > 1 else np.nan
            g[f"{name}_zt"] = (v - np.nanmean(v)) / sd if sd and np.isfinite(sd) and sd > 0 else np.nan
        out.append(g)
    p = pd.concat(out, ignore_index=True)
    for name in PREDICTORS:
        v = p[f"{name}_s"]
        p[f"{name}_zp"] = (v - v.mean()) / v.std()
    return p


ZCOLS = {"none": "_s", "pooled": "_zp", "per_trajectory": "_zt"}


def turn_table(prepared: pd.DataFrame, turns: pd.DataFrame, onset: str = "rule20",
               offset_s: float = 0.05, opts: TurnOptions = TurnOptions()) -> pd.DataFrame:
    """Every turn event with what the Fig. 5 filters and models need (before filtering).

    `prepared` holds every frame of one plume group (from `prepare_frames`); the arena bounds of
    the code's margin are the 1st and 99th percentiles of those frames' positions. The flags and
    predictors are read at the frame matched to `onset` - 50 ms ("start": the dataset's turn
    start, as the code; "rule20": the SI's onset), the code's way (`merge_asof`).
    """
    q = opts.bounds_quantile
    xb = np.nanquantile(prepared.x, [q, 1 - q])
    yb = np.nanquantile(prepared.y, [q, 1 - q])
    pcols = [f"{n}{z}" for n in PREDICTORS for z in ZCOLS.values()]
    rows = []
    by_traj = {k: g for k, g in prepared.groupby(["session", "trj"], sort=False)}
    for (sess, trj), tg in turns.groupby(["session", "trj"], sort=False):
        g = by_traj.get((sess, trj))
        if g is None:
            continue
        t = g.t.to_numpy()
        dth = g.dtheta.to_numpy(float)
        rot = np.abs(dth)
        theta = g.theta.to_numpy(float)
        x, y, vxs = g.x.to_numpy(float), g.y.to_numpy(float), g.vx_smooth.to_numpy(float)
        P = g[pcols].to_numpy(float)
        fps = 1.0 / np.median(np.diff(t))
        for r in tg.itertuples(index=False):
            on20, tpk, pk, j0, j1 = onset_20pct(t, rot, r.start_time, r.stop_time)
            i_on = np.searchsorted(t, r.start_time - 1e-9)
            i_off = min(np.searchsorted(t, r.stop_time + 1e-9) - 1, len(t) - 1)
            ip = np.searchsorted(t, tpk) if np.isfinite(tpk) else -1
            row = {"session": sess, "trj": trj, "cluster": f"{sess}:{trj}", "start": r.start_time,
                   "stop": r.stop_time, "onset20": on20, "t_peak": tpk, "peak_speed": pk,
                   "dtheta_peak": dth[ip] if ip >= 0 else np.nan,
                   "direction": r.turn_direction, "turn_theta": r.turn_theta, "turn_x": r.turn_x,
                   "turn_y": r.turn_y,
                   "theta_start": theta[i_on] if i_on < len(t) else np.nan, "theta_stop": theta[i_off],
                   "int_dtheta": float(np.nansum(dth[i_on:i_off + 1]) / fps) if i_off >= i_on else np.nan,
                   "int_dtheta_20": float(np.nansum(dth[j0:j1 + 1]) / fps) if j0 >= 0 else np.nan}
            on = r.start_time if onset == "start" else on20
            # the code rounds the target time to 10 decimals, then takes the last frame at or
            # before it within one frame (pandas merge_asof, direction backward, tolerance 1/fps)
            target = round(on - offset_s, 10) if np.isfinite(on) else np.nan
            k = np.searchsorted(t, target, side="right") - 1 if np.isfinite(target) else -1
            if k >= 0 and target - t[k] <= 1.0 / fps:
                row.update({"matched": True, "theta_at": theta[k], "walking_upwind": vxs[k] < 0,
                            "near_margin": bool(x[k] < xb[0] + opts.margin_mm or x[k] > xb[1] - opts.margin_mm
                                                or y[k] < yb[0] + opts.margin_mm or y[k] > yb[1] - opts.margin_mm),
                            **dict(zip(pcols, P[k]))})
            else:
                row.update({"matched": False, "theta_at": np.nan, "walking_upwind": False,
                            "near_margin": False, **{c: np.nan for c in pcols}})
            rows.append(row)
    return pd.DataFrame(rows)


def keep(tt: pd.DataFrame, opts: TurnOptions) -> pd.DataFrame:
    """The kept turns of Fig. 5 (code `filter_published_turns`), with the predictors of the
    reading's z-scoring in columns `gradient`, `motion`, `intensity`."""
    m = (tt.matched & tt.theta_at.between(*opts.heading) & tt.walking_upwind
         & tt.turn_x.between(*opts.x_range) & tt.turn_y.between(*opts.y_range))
    if opts.margin:
        m &= ~tt.near_margin
    k = tt[m].copy()
    for n in PREDICTORS:
        k[n] = k[f"{n}{ZCOLS[opts.zscore]}"]
    return k.dropna(subset=list(PREDICTORS))


MODELS = {"full": ["motion", "gradient", "intensity"], "motion": ["motion", "intensity"],
          "gradient": ["gradient", "intensity"], "base": ["intensity"]}


def fit_logit(kept: pd.DataFrame, predictors: list[str]):
    """Logistic regression of turn direction (> 0 coded 1) with trajectory-clustered SE."""
    import statsmodels.formula.api as smf
    df = kept.assign(y=(kept.direction > 0).astype(int))
    formula = "y ~ " + " + ".join(predictors)
    return smf.logit(formula, data=df).fit(disp=False, cov_type="cluster",
                                           cov_kwds={"groups": pd.factorize(df.cluster)[0]})


def fig5_models(kept: pd.DataFrame) -> dict:
    """The four models of Fig. 5F and S5D-E; mean log-likelihood per turn and cue dominance."""
    fits = {k: fit_logit(kept, v) for k, v in MODELS.items()}
    ll = {k: f.llf / f.nobs for k, f in fits.items()}
    dom = (ll["gradient"] - ll["motion"]) / (ll["full"] - ll["base"])
    return {"fits": fits, "ll": ll, "dominance": dom}


# ----------------------------------------------------------------------------------------------
# Complex plume movie (Figs. 2 and S1F-G)
# ----------------------------------------------------------------------------------------------

COMPLEX_MOVIE = ("sub-figs1-complex-smoke-1a/sub-figs1-complex-smoke-1a_ses-figure-s1_image.nwb",
                 "scratch/smoke_1a_orig_figs1_background_subtracted_window_frames")
COMPLEX_CENTERLINE = 590      # SI, Plume movies: centerline row of the complex plume
SPACINGS = (3, 6, 9, 12)      # Fig. S1F-G sensor spacings, pixels (claims file)
DELAYS = (1, 2, 4, 8, 15)     # Fig. S1G delays, frames (claims file)


def open_movie(assets: pd.DataFrame, path: str, dataset: str):
    """Stream an NWB movie: returns (h5py dataset, file handle)."""
    import remfile
    aid = assets.set_index("path").asset_id[path]
    f = h5py.File(remfile.File(asset_url(aid)), "r")
    return f[dataset], f


def _pair(frame: np.ndarray, d: int) -> tuple[np.ndarray, np.ndarray]:
    """Sensor pair d rows apart, aligned on the row between them: rows y - floor(d/2) and
    y + ceil(d/2), for y in [6, H - 7) (a fixed crop so maps of every spacing share pixels)."""
    h = frame.shape[0]
    lo, hi = d // 2, d - d // 2
    return frame[6 - lo:h - 7 - lo], frame[6 + hi:h - 7 + hi]


def movie_pass1(ds, n_frames: int | None = None, col_step: int = 4) -> dict:
    """One streaming pass over the movie (frames are read in blocks of 20).

    Returns the per-pixel mean intensity (full resolution); for Fig. S1F-G the time-averaged
    crosswind gradient B - A of sensor pairs `SPACINGS` rows apart, and the time-averaged motion
    cue of each spacing and delay `DELAYS`, in two forms:
      - "grad_dt": -(B - A)(t) x (M(t) - M(t - tau)), M = (A + B) / 2, the Fig. 1 cue
        -(dI/dy)(dI/dt) with the spacing and delay widened (an assumption, see the notebook);
      - "corr": A(t - tau) B(t) - A(t) B(t - tau), the two-sensor correlator of the SI's motion
        feature (Logistic regression models), a reading.
    Cue maps keep every `col_step`-th column (a standard choice: the cue is crosswind, so
    columns are independent, and the Pearson r over a quarter of them estimates the whole).
    Frames are used as stored (0 to 255; no spatial smoothing, as the code's whole-window maps).
    """
    n = ds.shape[0] if n_frames is None else n_frames
    h, w = ds.shape[1:]
    total = np.zeros((h, w))
    grad = {d: 0.0 for d in SPACINGS}
    mot = {(form, d, tau): 0.0 for form in ("grad_dt", "corr") for d in SPACINGS for tau in DELAYS}
    nmot = {tau: 0 for tau in DELAYS}
    hist = []    # last 15 frames, column-subsampled
    lo, hi = np.inf, -np.inf
    i = 0
    while i < n:
        block = ds[i:min(i + 20, n)]
        for fr in block:
            fr = np.asarray(fr, np.float32)
            total += fr
            lo, hi = min(lo, float(fr.min())), max(hi, float(fr.max()))
            sub = fr[:, ::col_step]
            for d in SPACINGS:
                a, b = _pair(sub, d)
                grad[d] = grad[d] + (b - a)
                for tau in DELAYS:
                    if len(hist) >= tau:
                        pa, pb = _pair(hist[-tau], d)
                        mot[("grad_dt", d, tau)] = mot[("grad_dt", d, tau)] - (b - a) * (0.5 * (a + b) - 0.5 * (pa + pb))
                        mot[("corr", d, tau)] = mot[("corr", d, tau)] + (pa * b - a * pb)
            for tau in DELAYS:
                if len(hist) >= tau:
                    nmot[tau] += 1
            hist.append(sub)
            if len(hist) > max(DELAYS):
                hist.pop(0)
            i += 1
    return {"mean": total / n, "n_frames": n,
            "grad": {d: g / n for d, g in grad.items()},
            "motion": {k: m / nmot[k[2]] for k, m in mot.items()},
            "col_step": col_step, "frame_min": lo, "frame_max": hi}


def otsu_mask(mean_map: np.ndarray, bias: float, mode: str, radius: int = 9) -> np.ndarray:
    """Otsu mask of the SI (Plume movies): Otsu's threshold on the mean intensity map, lowered by
    the bias, then a binary opening and closing with a disk of `radius` pixels (claims file).
    mode "subtract": threshold - bias (intensity units, 0 to 255); "percent": threshold x
    (1 - bias / 100). Both are readings named in the claims file."""
    from skimage.filters import threshold_otsu
    from scipy.ndimage import binary_closing, binary_opening
    from skimage.morphology import disk
    th = threshold_otsu(mean_map)
    th = th - bias if mode == "subtract" else th * (1 - bias / 100.0)
    m = mean_map > th
    se = disk(radius)
    return binary_closing(binary_opening(m, structure=se), structure=se)


def sample_antennas(ds, rows: np.ndarray, cols: np.ndarray, n_frames: int | None = None,
                    sigma: float = 1.5) -> np.ndarray:
    """Signals at two antennae 3 pixels apart (rows r and r + 3, column c), facing upwind, from
    each frame filtered by a 2-D Gaussian of SD 1.5 pixels (SI, Plume movies). Returns
    (frames, locations, 2) float32 with antenna 0 at row r, antenna 1 at row r + 3."""
    from scipy.ndimage import gaussian_filter
    n = ds.shape[0] if n_frames is None else n_frames
    out = np.empty((n, len(rows), 2), np.float32)
    i = 0
    while i < n:
        block = ds[i:min(i + 20, n)]
        for fr in block:
            g = gaussian_filter(np.asarray(fr, np.float32), sigma)
            out[i, :, 0] = g[rows, cols]
            out[i, :, 1] = g[rows + 3, cols]
            i += 1
    return out


def window_features(traces: np.ndarray, delays=(1,), history: int = 30, threshold: float = 5.0) -> dict:
    """Features of every 30-frame window at every location (code centerline_models.py):
    nan_to_num, then log(1 + max(I - 5, 0)); sum 0.5 mean(R + L), gradient mean(R - L), motion
    mean(R(t) L(t + d) - R(t + d) L(t)). Antenna 0 is taken as R (a convention; AUC and |weights|
    do not depend on it). Returns arrays (windows, locations)."""
    x = np.log1p(np.maximum(np.nan_to_num(traces.astype(np.float64)) - threshold, 0.0))
    r, l = x[..., 0], x[..., 1]
    nwin = x.shape[0] - history + 1

    def wmean(series, length):
        c = np.concatenate([np.zeros((1, series.shape[1])), np.cumsum(series, axis=0)])
        return (c[length:length + nwin] - c[:nwin]) / length

    out = {"sum": 0.5 * wmean(r + l, history), "gradient": wmean(r - l, history)}
    for d in delays:
        prod = r[:-d] * l[d:] - r[d:] * l[:-d]
        out[f"motion{d}"] = wmean(prod, history - d)
    return out


def choose_locations(valid: np.ndarray, n: int, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    """`n` locations drawn uniformly, without replacement, among pixels where both antennae
    (rows r and r + 3) are in the valid region (SI, Plume movies: 1000 random locations)."""
    both = valid.copy()
    both[-3:] = False
    both[:-3] &= valid[3:]
    rr, cc = np.nonzero(both)
    idx = rng.choice(len(rr), n, replace=False)
    return rr[idx], cc[idx]


def draw_samples(F: dict, labels: np.ndarray, sampling: str, rng: np.random.Generator,
                 keys=("sum", "gradient", "motion1"), n_train: int = 2_400_000, n_test: int = 600_000):
    """Training and test samples of Fig. 2 from the windows of one repeat's locations.

    sampling "random": windows (location, start) drawn uniformly with replacement and split at
    random; "location": 80% of the locations give the training windows, the rest the test
    windows; "mirror": as "random", with each drawn sample paired with its left-right mirror
    (antennae swapped, so sum is unchanged, gradient and motion change sign, and the label flips).
    Returns X_train, y_train, X_test, y_test (features in the order of `keys`)."""
    nwin, nloc = F["sum"].shape
    n = n_train + n_test
    sign = np.array([1.0 if k == "sum" else -1.0 for k in keys])
    if sampling == "location":
        perm = rng.permutation(nloc)
        ntr = int(round(0.8 * nloc))
        loc = np.concatenate([rng.choice(perm[:ntr], n_train), rng.choice(perm[ntr:], n_test)])
        win = rng.integers(0, nwin, n)
    else:
        m = n // 2 if sampling == "mirror" else n
        loc = rng.integers(0, nloc, m)
        win = rng.integers(0, nwin, m)
    X = np.column_stack([F[k][win, loc] for k in keys])
    y = labels[loc].astype(int)
    if sampling == "mirror":
        X = np.vstack([X, X * sign])
        y = np.concatenate([y, 1 - y])
        p = rng.permutation(len(y))
        X, y = X[p], y[p]
    return X[:n_train], y[:n_train], X[n_train:], y[n_train:]


def fit_fig2(Xtr, ytr, Xte, yte, names=("sum", "gradient", "motion")) -> dict:
    """Unpenalised logistic regressions on features standardised with training statistics (code
    centerline_models.py): test AUC of each single-feature model, and of the combined model with
    its weights."""
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import roc_auc_score
    mu, sd = Xtr.mean(0), Xtr.std(0)
    Ztr, Zte = (Xtr - mu) / sd, (Xte - mu) / sd
    out = {}
    for j, nm in enumerate(names):
        m = LogisticRegression(C=np.inf, max_iter=1000).fit(Ztr[:, [j]], ytr)
        out[f"auc_{nm}"] = roc_auc_score(yte, m.predict_proba(Zte[:, [j]])[:, 1])
    if len(names) > 1:
        m = LogisticRegression(C=np.inf, max_iter=1000).fit(Ztr, ytr)
        out["auc_all"] = roc_auc_score(yte, m.predict_proba(Zte)[:, 1])
        out.update({f"w_{nm}": float(w) for nm, w in zip(names, m.coef_[0])})
    return out
