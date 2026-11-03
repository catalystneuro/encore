"""Loading and measures for the eBRIC cortical recordings of dandiset 001559.

Tian, Zhang, Du, Huang, Bizimana, Nishimura & Ai (2025), ACS Sensors 10(8) 5826-5833,
doi:10.1021/acssensors.5c01093, Figure 4.

The dandiset holds one mouse (sub-582364L) and only image series (NWB TwoPhotonSeries):

- 2025-04-07, three 40 Hz camera movies (1000 x 920 pixels, uint16), whose frames cycle
  through four exposures; laser speckle imaging (Figure 4C), as far as the data show.
- 2025-05-31, six ScanImage acquisitions of four channels each (512 x 512 pixels,
  4.228 frames/s, 1000 frames). Channel 1 is a stimulus marker (it drops from about -580 to
  about -1990 for 5 s); channels 3 and 4 carry the bioluminescence; channel 2 does not.
  These are the PMT recordings of Figure 4D, with the excitation laser blocked.
- 2025-06-09, two ScanImage stacks of four channels (1024 x 1024 pixels): a wide field of the
  window (channel 2 shows vessels, channels 3 and 4 the red expression) and a field of
  labelled cells (Figure 4B).

Files are streamed from the archive at the pinned version; nothing is written to disk.

Where the parameters come from:

- `SMOOTH_S` = 1 s moving average: the Figure 4D legend ("Traces are smoothed using a 1-s
  moving average"), as the claims file's criteria give it.
- `BASELINE_S` = 5 s before onset, the response windows (`WINDOWS`, 0 to 5 s and 0 to 10 s
  after onset), the k = 2 and 3 detection thresholds, the half-peak rise time and the
  0 to 10 s peak window: the claims file's criteria (fig4d-evoked-increase,
  fig4d-4ma-single-trials, fig4d-electrode-timing), which name them as readings or as
  standard choices, not the paper's.
- `STIM_S` = 5 s and `PULSE_HZ` = 5 Hz: the Methods ("Electrical stimulation (5 Hz, 5 s,
  2 mA and 4 mA)").
- `BIN_LINES` = 128 lines (about 59 ms, four bins per frame): a standard choice for the time
  base of the PMT signal, finer than a frame so that the 1 s smoothing and the peak and rise
  times are not set by the 0.24 s frame period. The signal of a bin is the mean of the pixels
  of its lines. It cannot change a response mean.
- `MARKER_THRESHOLD` = -1300: about halfway between the two levels of the marker channel
  (about -580 and -1990), read from the data (a standard choice). Only the frames in which a
  pulse starts or ends lie between the levels; `marker_onsets` places the edges within them.
- Line times are frame start plus line index over the scan line rate stored in the file
  (`scan_line_rate`, 2173.9 lines/s).
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient

DANDISET_ID = "001559"
DANDISET_VERSION = "0.250902.2058"

SMOOTH_S = 1.0
BASELINE_S = 5.0
STIM_S = 5.0
PULSE_HZ = 5.0
WINDOWS = {"a": (0.0, 5.0), "b": (0.0, 10.0)}
BIN_LINES = 128
MARKER_THRESHOLD = -1300.0
MARKER_CHANNEL = 1
BL_CHANNELS = (3, 4)

_client = None


def dandiset():
    global _client
    if _client is None:
        _client = DandiAPIClient()
    return _client.get_dandiset(DANDISET_ID, DANDISET_VERSION)


def assets():
    """All assets of the pinned version, sorted by path."""
    return sorted(dandiset().get_assets(), key=lambda a: a.path)


def open_asset(asset):
    url = asset.get_content_url(follow_redirects=1, strip_query=True)
    return h5py.File(remfile.File(url, verbose=False), "r")


def session_of(path):
    return path.split("ses-")[1][:15]


def _series(f):
    g = f["acquisition"]
    names = list(g)
    assert len(names) == 1, names
    return names[0], g[names[0]]


def describe(asset):
    """Metadata and array shape of one file, without reading its data."""
    f = open_asset(asset)
    name, s = _series(f)
    d = s["data"]
    plane = f["general/optophysiology"][list(f["general/optophysiology"])[0]]
    if "starting_time" in s:
        rate, n_ts = float(s["starting_time"].attrs["rate"]), None
    else:
        ts = s["timestamps"][:]
        rate, n_ts = 1.0 / float(np.median(np.diff(ts))), len(ts)
    return {
        "path": asset.path.split("/")[-1],
        "session": session_of(asset.path),
        "series": name,
        "channel": int(name[-1]) if name[-1].isdigit() else None,
        "shape": tuple(d.shape),
        "dtype": str(d.dtype),
        "rate_hz": rate,
        "timing": "rate" if n_ts is None else "timestamps",
        "scan_line_rate": float(s.attrs["scan_line_rate"]) if "scan_line_rate" in s.attrs else None,
        "grid_spacing": plane["grid_spacing"][()].tolist() if "grid_spacing" in plane else None,
        "grid_unit": plane["grid_spacing"].attrs.get("unit") if "grid_spacing" in plane else None,
        "indicator": plane["indicator"][()].decode(),
        "location": plane["location"][()].decode(),
        "emission_nm": [float(plane[k]["emission_lambda"][()]) for k in plane
                        if isinstance(plane[k], h5py.Group) and "emission_lambda" in plane[k]][0],
        "description": s.attrs.get("description"),
        "session_start": f["session_start_time"][()].decode(),
        "subject": f["general/subject/subject_id"][()].decode(),
        "date_of_birth": f["general/subject/date_of_birth"][()].decode(),
        "session_description": f["session_description"][()].decode(),
        "size_gb": asset.size / 1e9,
    }


def survey(workers=8):
    with ThreadPoolExecutor(workers) as ex:
        return pd.DataFrame(list(ex.map(describe, assets())))


# ---------------------------------------------------------------- PMT recordings (Figure 4D)

def _line_means(asset):
    f = open_asset(asset)
    name, s = _series(f)
    d = s["data"]
    step = d.chunks[0]
    L = np.concatenate([d[i:i + step].astype(np.float32).mean(axis=2)
                        for i in range(0, d.shape[0], step)])
    if "starting_time" in s:
        fr = float(s["starting_time"].attrs["rate"])
        frame_t = np.arange(d.shape[0]) / fr
    else:
        frame_t = s["timestamps"][:]
    lr = float(s.attrs["scan_line_rate"])
    t = (frame_t[:, None] + np.arange(d.shape[1])[None, :] / lr)
    return {"session": session_of(asset.path), "channel": int(name[-1]), "lines": L,
            "t": t, "frame_t": frame_t, "line_rate": lr}


def load_pmt(day="20250531", workers=6):
    """Per-line means of every channel of every acquisition of that day.

    Returns {session: {channel: dict(lines=(frames, lines), t=(frames, lines), frame_t)}}.
    """
    sel = [a for a in assets() if f"ses-{day}" in a.path]
    with ThreadPoolExecutor(workers) as ex:
        out = list(ex.map(_line_means, sel))
    rec = {}
    for r in out:
        rec.setdefault(r["session"], {})[r["channel"]] = r
    return rec


def binned(r, bin_lines=BIN_LINES):
    """Signal in bins of `bin_lines` lines: (bin times, bin means)."""
    L, t = r["lines"], r["t"]
    n = L.shape[1] // bin_lines
    x = L[:, :n * bin_lines].reshape(L.shape[0], n, bin_lines).mean(2).ravel()
    tt = t[:, :n * bin_lines].reshape(t.shape[0], n, bin_lines).mean(2).ravel()
    return tt, x


def marker_levels(r):
    x = r["lines"].mean(1)
    return np.median(x[x >= MARKER_THRESHOLD]), np.median(x[x < MARKER_THRESHOLD])


def marker_onsets(r):
    """Onset and offset times (s) of the marker pulses.

    The marker channel is constant within a frame (every line of a frame has the same value),
    so its value is the frame's average of the marker. A frame in which the stimulus started
    or stopped has a value between the two levels, in proportion to the part of the frame the
    stimulus was on. The onset is placed at the end of the frame before the first fully-on frame
    minus that frame's on fraction of a frame period, and the offset likewise (a standard
    interpolation; it moves an edge by less than one frame, 0.24 s).

    Returns refined onsets, refined offsets, and the first fully-on frame of each pulse.
    """
    x = r["lines"].mean(1)
    ft = r["frame_t"]
    per = float(np.median(np.diff(ft)))
    hi, lo = marker_levels(r) if (x < MARKER_THRESHOLD).any() else (np.median(x), np.nan)
    frac = np.clip((hi - x) / (hi - lo), 0, 1) if np.isfinite(lo) else np.zeros_like(x)
    full = x < MARKER_THRESHOLD
    d = np.diff(full.astype(int))
    st, en = np.where(d == 1)[0] + 1, np.where(d == -1)[0] + 1
    if full[0]:
        st = np.r_[0, st]
    if full[-1]:
        en = np.r_[en, x.size]
    # on time in the edge frames: the frame before the first full frame, and that frame itself
    # (a frame on for more than half its period also passes the threshold)
    on = np.array([ft[i] + (1 - frac[i]) * per - (frac[i - 1] * per if i > 0 else 0.0) for i in st])
    off = np.array([ft[j] + frac[j] * per - (1 - frac[j - 1]) * per if j < x.size else ft[-1] + per for j in en])
    return on, off, st


def smooth(x, dt, width_s=SMOOTH_S):
    n = max(1, int(round(width_s / dt)))
    k = np.ones(n) / n
    return np.convolve(x, k, mode="same"), n


def trial_table(t, x, onsets, windows=WINDOWS, baseline_s=BASELINE_S):
    """Per trial: baseline mean and s.d. (raw and smoothed), and the response in each window."""
    dt = float(np.median(np.diff(t)))
    xs, _ = smooth(x, dt)
    rows = []
    for i, t0 in enumerate(onsets):
        b = (t >= t0 - baseline_s) & (t < t0)
        row = {"trial": i, "onset_s": t0, "baseline": x[b].mean(), "baseline_sd_smoothed": xs[b].std(ddof=1),
               "n_baseline_bins": int(b.sum())}
        for k, (w0, w1) in windows.items():
            w = (t >= t0 + w0) & (t < t0 + w1)
            row[f"resp_{k}"] = x[w].mean() - x[b].mean()
            row[f"complete_{k}"] = bool(t0 + w1 <= t[-1])
        rows.append(row)
    return pd.DataFrame(rows)


def event_average(t, x, onsets, pre=BASELINE_S, post=15.0):
    """Trials aligned on onset, on a common grid of bin times; the 1 s smoothed signal."""
    dt = float(np.median(np.diff(t)))
    xs, _ = smooth(x, dt)
    grid = np.arange(-pre, post, dt)
    tr = []
    for t0 in onsets:
        if t0 - pre < t[0] or t0 + post > t[-1]:
            continue
        tr.append(np.interp(t0 + grid, t, xs))
    return grid, np.array(tr)


def peak_and_rise(grid, avg, baseline_s=BASELINE_S, peak_window=(0.0, 10.0)):
    """Time of the maximum within the peak window, and first time after onset above half peak.

    Both relative to the mean of the averaged trace in the 5 s before onset.
    """
    base = avg[(grid >= -baseline_s) & (grid < 0)].mean()
    y = avg - base
    w = (grid >= peak_window[0]) & (grid < peak_window[1])
    ip = np.argmax(np.where(w, y, -np.inf))
    half = y[ip] / 2
    after = np.where((grid >= 0) & (y > half))[0]
    return {"peak_time_s": grid[ip], "peak": y[ip], "rise_time_s": grid[after[0]] if after.size else np.nan}


def shifted_null(t, x, onsets, n=1000, seed=0, window=WINDOWS["a"]):
    """Mean response at onsets shifted by one common random offset (circular), as a null.

    Keeps the trials' spacing and moves them together, so it tests the alignment of the
    marker with the signal.
    """
    rng = np.random.default_rng(seed)
    span = t[-1] - t[0]
    out = np.empty(n)
    for i in range(n):
        s = rng.uniform(15.0, span - 15.0)
        sh = t[0] + (onsets - t[0] + s) % span
        sh = sh[(sh > t[0] + BASELINE_S) & (sh < t[-1] - window[1])]
        out[i] = trial_table(t, x, sh, windows={"x": window})["resp_x"].mean()
    return out


def pulse_fold(t, x, onsets, period=1 / PULSE_HZ, n_bins=20, stim_s=STIM_S):
    """Unsmoothed signal within the stimulation, folded on the 0.2 s pulse period.

    Each trial's stimulation segment is detrended (a line fit removed) first, so the slow
    rise of the response does not appear as a ramp across the fold.
    """
    prof = np.zeros(n_bins)
    cnt = np.zeros(n_bins)
    per_trial = []
    for t0 in onsets:
        sel = (t >= t0) & (t < t0 + stim_s)
        tt, xx = t[sel] - t0, x[sel]
        xx = xx - np.polyval(np.polyfit(tt, xx, 1), tt)
        b = ((tt % period) / period * n_bins).astype(int).clip(0, n_bins - 1)
        p = np.bincount(b, xx, n_bins) / np.maximum(np.bincount(b, minlength=n_bins), 1)
        per_trial.append(p)
        np.add.at(prof, b, xx)
        np.add.at(cnt, b, 1)
    return prof / cnt, np.array(per_trial)


# ---------------------------------------------------------------- images (Figure 4B, 4C)

def stack_projection(asset, step=2):
    """Mean over all frames, and per-frame mean, of one image stack, subsampled in space."""
    f = open_asset(asset)
    _, s = _series(f)
    d = s["data"]
    c = d.chunks[0]
    acc = None
    fm = []
    for i in range(0, d.shape[0], c):
        x = d[i:i + c, ::step, ::step].astype(np.float32)
        fm.append(x.mean((1, 2)))
        acc = x.sum(0) if acc is None else acc + x.sum(0)
    return acc / d.shape[0], np.concatenate(fm)


def speckle_head(asset, n_frames=400, block=8):
    """Block speckle contrast K = s.d./mean in `block` x `block` pixels, first frames only."""
    f = open_asset(asset)
    _, s = _series(f)
    d = s["data"]
    c = d.chunks[0]
    K, M = [], []
    for i in range(0, min(n_frames, d.shape[0]), c):
        x = d[i:i + c].astype(np.float32)
        h, w = x.shape[1] // block, x.shape[2] // block
        x = x[:, :h * block, :w * block].reshape(-1, h, block, w, block)
        m = x.mean((2, 4))
        K.append(x.std((2, 4)) / np.maximum(m, 1e-3))
        M.append(m)
    return np.concatenate(K), np.concatenate(M), float(s["starting_time"].attrs["rate"])
