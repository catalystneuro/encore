"""Loading and measures for dandiset 001341, barrel cortex recordings during tactile VR navigation.

Armstrong & Vlasov (2026), PNAS 123(18) e2514107123, doi:10.1073/pnas.2514107123.

Each NWB file holds one session: the units table (spike times, layer, unit type, waveform
duration, quality metrics), a trials table (closed-loop straight runs and open-loop turns,
`OL_L_1.dat` and `OL_R_2.dat`), and the ball tracking at 500 Hz (`distance_for`,
`distance_lat`, `speed_for_smooth`, `speed_lat_smooth`), with the trial number of each sample
(`trial`) and the time since the trial's start (`ts_local`). Files are streamed from the archive
at the pinned version; nothing is written to disk.

What the files show, and how this module handles it:

- `distance_lat` and `distance_for` restart at 0 at every trial. Positive lateral distance is to
  the left: OL_L trials end displaced to the positive side.
- In 62 (489) and 63 (503) OL trials the trials table's stop time is earlier than its start time,
  and the sample timestamps of those trials restart at the preceding straight trial's start.
  Their start times are right (the next trial starts 2.000 s later), so time within a trial is
  taken from `ts_local`, and the first sample of such a trial, which carries the previous trial's
  `ts_local`, is dropped (`trial_segments`).
- In session 489 the trials table rows from 999 on are copies of row 999 (same start, stop and
  label `OL_L_1.dat`), while the `trial` series gives these trials their own times and they
  alternate between 2 s turns and longer straight runs. Their labels and table times cannot be
  used; `intact` marks the rows before the first repeated start time, and analyses use those.
- The spike times are not on the clock of the trials table: there is no trial-locked modulation
  at the stored times, and the lag that best aligns them drifts through the session
  (`lag_scan`). The files hold no synchronisation signal.

Where the parameters come from:

- Run angle theta = atan(D_lat / D_for), positive for left turns (SI, Behavioral tactile virtual
  reality rig, Eq. 1), computed per sample from the lateral and forward speeds.
- Reaction time: "the largest peak in the time interval after the start of the turning trial" of
  "lateral acceleration (or run angle derivative)" (SI, Fitting of drift diffusion models). The
  claims file names the signals and the search windows (0 to 1 s, 0 to 1.8 s), and the peak is
  taken in the turn direction (positive for left turns, Fig. 2H).
- Correct trial: "achieves ±1cm clearance at t=1s from the trial start" (SI, Fitting of drift
  diffusion models); the two readings of "clearance" are the claims file's.
- Running: mean trial speed above 10 cm/s (Table S1 footnotes).
- `RT_DT` (5 ms) is the time step of the DDM fits, a standard choice for PyDDM that does not
  change a result at the precision compared.
"""

from __future__ import annotations

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient

DANDISET_ID = "001341"
DANDISET_VERSION = "0.260414.1316"
SESSIONS = {"489": "sub-489/sub-489_ses-20220708.nwb", "503": "sub-503/sub-503_ses-20220902.nwb"}
FS_BEHAVIOUR = 500.0          # Hz, SI Behavioral tactile virtual reality rig
RUN_THRESHOLD = 10.0          # cm/s, Table S1 footnotes
FS_DURATION_MS = 0.4          # waveform duration threshold for FS units, SI Spike sorting
LABELS = {"OL_L_1.dat": "OL_L", "OL_R_2.dat": "OL_R",
          "Straight 100cm A.dat": "CL", "Straight 100cm B.dat": "CL"}
RT_DT = 0.005


def asset_urls() -> dict[str, str]:
    """Streaming URL of each session's file at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        paths = {a.path: a for a in dandiset.get_assets()}
        return {s: paths[p].get_content_url(follow_redirects=1, strip_query=True)
                for s, p in SESSIONS.items()}


def open_session(url: str) -> h5py.File:
    return h5py.File(remfile.File(url), "r")


def _str(x):
    return x.decode() if isinstance(x, bytes) else x


def load_trials(f: h5py.File) -> pd.DataFrame:
    """Trials table with the file's label, a short label, duration and an `intact` flag.

    `intact` is False from the first row whose start time repeats an earlier one (session 489,
    rows 999 on); `negative` marks rows whose stop time precedes the start time.
    """
    g = f["intervals/trials"]
    tr = pd.DataFrame({"start_time": g["start_time"][:], "stop_time": g["stop_time"][:],
                       "trial_type": [_str(x) for x in g["trial_type"][:]]})
    tr["label"] = tr.trial_type.map(LABELS)
    tr["duration"] = tr.stop_time - tr.start_time
    rep = np.flatnonzero(np.diff(tr.start_time.values) <= 0)
    first_bad = rep[0] + 1 if len(rep) else len(tr)
    tr["intact"] = np.arange(len(tr)) < first_bad
    tr["negative"] = tr.duration < 0
    return tr


def load_behaviour(f: h5py.File) -> pd.DataFrame:
    """Per-sample ball tracking: trial row (0-based), time in trial, distances and speeds."""
    a = f["acquisition"]
    return pd.DataFrame({
        "row": a["trial/data"][:].astype(int) - 1,
        "ts": a["trial/timestamps"][:],
        "t_local": a["ts_local/data"][:],
        "d_for": a["distance_for/data"][:], "d_lat": a["distance_lat/data"][:],
        "v_for": a["speed_for_smooth/data"][:], "v_lat": a["speed_lat_smooth/data"][:],
    })


def trial_segments(beh: pd.DataFrame) -> dict[int, np.ndarray]:
    """Sample indices of each trial row, without a leading sample left from the previous trial."""
    row = beh.row.values
    tl = beh.t_local.values
    edges = np.r_[0, np.flatnonzero(np.diff(row) != 0) + 1, len(row)]
    seg = {}
    for a, b in zip(edges[:-1], edges[1:]):
        if b - a > 1 and tl[a] > tl[a + 1]:
            a += 1
        seg[int(row[a])] = np.arange(a, b)
    return seg


def trial_table_from_samples(beh: pd.DataFrame, seg: dict[int, np.ndarray]) -> pd.DataFrame:
    """Per trial row: first and last sample timestamp, samples, last time in trial, distances."""
    out = []
    for r, idx in seg.items():
        out.append((r, beh.ts.values[idx[0]], beh.ts.values[idx[-1]], len(idx),
                    beh.t_local.values[idx[-1]], beh.d_for.values[idx[-1]],
                    beh.d_lat.values[idx[-1]]))
    return pd.DataFrame(out, columns=["row", "t_first", "t_last", "n_samples", "t_local_end",
                                      "d_for_end", "d_lat_end"]).set_index("row")


def _on_grid(beh, idx, col, grid):
    t = beh.t_local.values[idx]
    y = beh[col].values[idx]
    ok = ~np.isnan(y)
    if ok.sum() < 2:
        return np.full(len(grid), np.nan)
    return np.interp(grid, t[ok], y[ok], left=np.nan, right=np.nan)


def lateral_traces(beh, seg, rows, t_grid):
    """Lateral position around each OL trial on `t_grid` (s from the turn start), two ways.

    stored: the file's `distance_lat`, which restarts at 0 at each trial; for t < 0 it is the
        preceding straight trial's value, for 0 <= t < 2 the OL trial's, for t >= 2 the next
        trial's (each from its own start).
    cl_start: integrated from the start of the preceding straight section; each trial's stored
        distance is added to the end values of the trials before it.
    """
    stored = np.full((len(rows), len(t_grid)), np.nan)
    cum = np.full_like(stored, np.nan)
    for k, r in enumerate(rows):
        if r - 1 not in seg or r + 1 not in seg:
            continue
        prev, cur, nxt = seg[r - 1], seg[r], seg[r + 1]
        dur_prev = beh.t_local.values[prev][-1]
        dur_cur = beh.t_local.values[cur][-1]
        lat_prev_end = beh.d_lat.values[prev][-1]
        lat_cur_end = beh.d_lat.values[cur][-1]
        m0 = t_grid < 0
        m1 = (t_grid >= 0) & (t_grid < dur_cur)
        m2 = t_grid >= dur_cur
        p = _on_grid(beh, prev, "d_lat", t_grid[m0] + dur_prev)
        c = _on_grid(beh, cur, "d_lat", t_grid[m1])
        n = _on_grid(beh, nxt, "d_lat", t_grid[m2] - dur_cur)
        stored[k, m0], stored[k, m1], stored[k, m2] = p, c, n
        cum[k, m0], cum[k, m1], cum[k, m2] = p, lat_prev_end + c, lat_prev_end + lat_cur_end + n
    return stored, cum


def lateral_at(beh, seg, rows, t):
    """Lateral displacement of each OL trial at time t (s) from its start, as stored."""
    return np.array([_on_grid(beh, seg[r], "d_lat", np.array([t]))[0] for r in rows])


def turn_signals(beh, idx):
    """Time in trial, run angle derivative (rad/s) and lateral acceleration (cm/s^2)."""
    t = beh.t_local.values[idx]
    vf = beh.v_for.values[idx]
    vl = beh.v_lat.values[idx]
    ok = ~(np.isnan(vf) | np.isnan(vl))
    t, vf, vl = t[ok], vf[ok], vl[ok]
    theta = np.arctan2(vl, vf)
    if len(t) < 3:
        return t, np.full(len(t), np.nan), np.full(len(t), np.nan)
    return t, np.gradient(theta, t), np.gradient(vl, t)


def reaction_time(beh, idx, sign, signal="angle", window=(0.0, 1.0)):
    """Time of the largest peak of the signal in the turn direction within the window."""
    t, dtheta, acc = turn_signals(beh, idx)
    y = sign * (dtheta if signal == "angle" else acc)
    m = (t >= window[0]) & (t <= window[1]) & ~np.isnan(y)
    if m.sum() == 0:
        return np.nan
    return t[m][np.argmax(y[m])]


def session_speed(beh, seg, rows=None):
    """Per-sample absolute speed (cm/s) and per-trial mean speed over the given rows."""
    sp = np.hypot(beh.v_for.values, beh.v_lat.values)
    rows = list(seg) if rows is None else rows
    per_trial = pd.Series({r: np.nanmean(sp[seg[r]]) for r in rows if r in seg})
    samples = np.concatenate([sp[seg[r]] for r in rows if r in seg])
    return samples, per_trial


def load_units(f: h5py.File) -> pd.DataFrame:
    u = f["units"]
    cols = ["id", "layer", "unit_type", "duration", "depth", "firing_rate", "amplitude_cutoff",
            "isi_viol", "presence_ratio"]
    df = pd.DataFrame({c: [_str(x) for x in u[c][:]] if u[c].dtype == object else u[c][:]
                       for c in cols})
    idx = u["spike_times_index"][:]
    df["n_spikes"] = np.diff(np.r_[0, idx])
    return df


def all_spikes(f: h5py.File) -> np.ndarray:
    """Spike times of all units, sorted."""
    return np.sort(f["units/spike_times"][:])


def population_psth(spikes, n_units, onsets, edges):
    """Population-averaged rate (Hz per unit) around onsets, for bin edges relative to onset."""
    h = np.zeros(len(edges) - 1)
    for t0 in onsets:
        a, b = np.searchsorted(spikes, [t0 + edges[0], t0 + edges[-1]])
        h += np.histogram(spikes[a:b] - t0, edges)[0]
    return h / len(onsets) / n_units / np.diff(edges)


def lag_scan(spikes, onsets, lags, dt=0.005, smooth=20):
    """Onset-triggered population count, averaged and smoothed (smooth bins), at each lag.

    Returns, for each lag l, the mean population rate at onset + l minus the session mean
    (Hz, all units summed). A trial-locked response at a fixed delay d appears as structure
    near l = d; the lag of the largest absolute value is reported by `best_lag`.
    """
    T = int(np.ceil((spikes.max() + lags.max() + 10) / dt))
    x = np.bincount((spikes / dt).astype(int), minlength=T)[:T].astype(float)
    x -= x.mean()
    e = np.zeros(T)
    e[(onsets / dt).astype(int)] = 1
    n = 2 * T
    c = np.fft.irfft(np.fft.rfft(x, n) * np.conj(np.fft.rfft(e, n)), n) / len(onsets) / dt
    k = np.round(lags / dt).astype(int) % n
    c = c[k]
    return np.convolve(c, np.ones(smooth) / smooth, "same")


def best_lag(lags, c):
    k = int(np.argmax(np.abs(c)))
    return lags[k], c[k], np.abs(c[k]) / c.std()


def fit_ddm(args):
    """Fit one drift diffusion model to reaction times with PyDDM (SI, Fitting of drift
    diffusion models), loss BIC as the paper reports. `args` is a tuple
    (key, rt, correct, model, sigma_free, t_dur).

    model "DDM": constant drift K, constant bounds +-B, noise sigma, non-decision time.
    model "GDDM": the DDM with exponentially collapsing bounds B exp(-t / tau) and a leaky
    integrator (drift K + leak * x), as the Results describe it (Ramping neural activity...,
    paragraph 1). Parameter ranges are standard wide ranges, not taken from the paper.
    sigma_free: sigma fitted with the others (reading a of the claims file), else fixed at 0.25
    (reading b). Returns the key, the fitted parameters and the BIC.
    """
    from pyddm import Fittable, Model, Sample, fit_adjust_model
    from pyddm.models import (BoundCollapsingExponential, BoundConstant, DriftConstant,
                              DriftLinear, LossBIC, NoiseConstant, OverlayNonDecision)
    import logging
    import warnings
    warnings.filterwarnings("ignore")
    logging.getLogger("pyddm").setLevel(logging.ERROR)
    key, rt, correct, model, sigma_free, t_dur = args
    sample = Sample.from_numpy_array(np.c_[rt, correct.astype(int)], [])
    noise = NoiseConstant(noise=Fittable(minval=0.01, maxval=2)) if sigma_free else NoiseConstant(noise=0.25)
    if model == "GDDM":
        drift = DriftLinear(drift=Fittable(minval=0, maxval=20), x=Fittable(minval=-10, maxval=10), t=0)
        bound = BoundCollapsingExponential(B=Fittable(minval=0.05, maxval=3), tau=Fittable(minval=0.05, maxval=10))
    else:
        drift = DriftConstant(drift=Fittable(minval=0, maxval=20))
        bound = BoundConstant(B=Fittable(minval=0.05, maxval=3))
    m = Model(drift=drift, noise=noise, bound=bound,
              overlay=OverlayNonDecision(nondectime=Fittable(minval=0, maxval=0.3)),
              dx=RT_DT, dt=RT_DT, T_dur=t_dur)
    np.random.seed(0)
    fit_adjust_model(sample, m, lossfunction=LossBIC, verbose=False, fitparams={"seed": 0})
    p = m.parameters()
    out = {"K": float(p["drift"]["drift"]), "B": float(p["bound"]["B"]),
           "sigma": float(p["noise"]["noise"]), "NDT": float(p["overlay"]["nondectime"]),
           "BIC": float(m.get_fit_result().value())}
    if model == "GDDM":
        out["leak"] = float(p["drift"]["x"])
        out["tau"] = float(p["bound"]["tau"])
    return key, out


def behaviour_time(beh, trials, seg):
    """Session time of each sample of the intact rows: the row's start time plus `ts_local`."""
    t = np.full(len(beh), np.nan)
    for r, idx in seg.items():
        if r < len(trials) and trials.intact.iloc[r]:
            t[idx] = trials.start_time.iloc[r] + beh.t_local.values[idx]
    return t


def speed_lag_scan(spikes, t_beh, speed, t0, t1, lags, dt=0.01, smooth=10):
    """Correlation of the population spike count (smoothed over `smooth` bins) with the
    absolute running speed, both in `dt` bins over [t0, t1) of the trial clock, with the
    spike train shifted by each lag (s). A standard check of a shared clock; bins and smoothing
    are standard choices."""
    n = int((t1 - t0) / dt)
    m = (t_beh >= t0) & (t_beh < t1) & ~np.isnan(speed)
    k = ((t_beh[m] - t0) / dt).astype(int)
    s = np.bincount(k, weights=speed[m], minlength=n)[:n]
    c = np.bincount(k, minlength=n)[:n]
    good = c > 0
    v = np.where(good, s / np.maximum(c, 1), 0.0)
    v[good] -= v[good].mean()
    v[~good] = 0
    out = np.empty(len(lags))
    for i, lag in enumerate(lags):
        a = np.searchsorted(spikes, [t0 + lag, t1 + lag])
        x = np.bincount(((spikes[a[0]:a[1]] - t0 - lag) / dt).astype(int), minlength=n)[:n].astype(float)
        x = np.convolve(x, np.ones(smooth) / smooth, "same")
        x = x - x[good].mean()
        out[i] = np.sum(x[good] * v[good]) / np.sqrt(np.sum(x[good] ** 2) * np.sum(v[good] ** 2))
    return out


def decode_accuracy(X, y, rng, folds=5):
    """Five-fold cross-validated accuracy of a nearest-class-mean decoder on z-scored features
    (a standard choice for a clock check, not a method of the paper)."""
    X = (X - X.mean(0)) / np.where(X.std(0) > 0, X.std(0), 1)
    order = rng.permutation(len(y))
    hits = 0
    for f in range(folds):
        test = order[f::folds]
        train = np.setdiff1d(order, test)
        means = {c: X[train][y[train] == c].mean(0) for c in np.unique(y[train])}
        cls = np.array(list(means))
        d = np.stack([((X[test] - means[c]) ** 2).sum(1) for c in cls], 1)
        hits += (cls[d.argmin(1)] == y[test]).sum()
    return hits / len(y)
