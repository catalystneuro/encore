"""Loading and survey helpers for dandiset 000943 (Clark and Nolan 2024, eLife 12:RP89356).

Every file of the dandiset is one recording session of one mouse: the raw tetrode signal
(`acquisition/ElectricalSeries`, 16 channels at 30 kHz) and a position series
(`acquisition/position`). Virtual reality sessions (session_description "vr") hold three position
columns at 1 kHz; open arena sessions ("openfield") hold nine. The files are read by streaming them
from the archive with remfile and h5py at the pinned version below; nothing is written to disk.

Parameters and where they come from:
- DANDISET_VERSION: the only published version of the dandiset (the paper cites none).
- TRACK_LENGTH_CM = 200: the paper uses only 200 cm tracks (claims file, opening comment; the files'
  own notes say "in the published journal article only sessions with 200cm track lengths are used").
- MIN_TRIALS = 10: the paper's code keeps sessions with at least 10 trials (claims file, opening
  comment, from vr_grid_population_level_plots.py).
- STOP_SPEED_CM_S = 4.7: a stop is registered when speed drops below 4.7 cm/s (Methods, Analysis of
  behaviour; also the files' notes). Speed is taken over the previous 100 ms, as the notes say.
- The 600 to 6000 Hz band of the multi-unit check is the paper's spike sorting filter (Methods,
  Spike sorting). The 100 ms bins and the lag range of that check are standard choices for a
  synchronisation check; they cannot change any claim's outcome, as no claim is tested on them.
"""
from __future__ import annotations

import hashlib
import time
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import remfile
import requests
from scipy import signal

DANDISET_ID = "000943"
DANDISET_VERSION = "0.240614.0754"
API = "https://api.dandiarchive.org/api"
TRACK_LENGTH_CM = 200
MIN_TRIALS = 10
STOP_SPEED_CM_S = 4.7
FS_EPHYS = 30000.0
# docs/protocol.md, Author, step 3 ("Keep it fast"): "CI fails a notebook over sixty" minutes.
NOTEBOOK_LIMIT_MIN = 60

_session = requests.Session()


def list_assets() -> list[dict]:
    """All assets of the pinned version (path, size, asset_id)."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=1000"
    out = []
    while url:
        r = _session.get(url, timeout=60).json()
        out += r["results"]
        url = r["next"]
    return out


def version_info() -> dict:
    """Metadata of the pinned version and the list of the dandiset's versions."""
    meta = _session.get(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/", timeout=60).json()
    versions = _session.get(f"{API}/dandisets/{DANDISET_ID}/versions/", timeout=60).json()["results"]
    return {"meta": meta, "versions": versions}


def s3_url(asset: dict) -> str:
    r = _session.head(f"{API}/assets/{asset['asset_id']}/download/", allow_redirects=True, timeout=60)
    return r.url


def open_nwb(asset: dict) -> h5py.File:
    """Open an asset by streaming it (remfile over its S3 URL)."""
    return h5py.File(remfile.File(s3_url(asset)), "r")


def _retry(fn, asset, tries=4):
    for k in range(tries):
        try:
            return fn(asset)
        except Exception as e:  # network errors: retry, then report
            err = repr(e)
            time.sleep(2 + 3 * k)
    return {"path": asset["path"], "error": err}


def _contents(f: h5py.File) -> dict:
    """What each top-level group that could hold derived data contains."""
    out = {}
    for g in ("processing", "analysis", "stimulus", "intervals", "units", "scratch"):
        if g not in f:
            out[g] = None
        else:
            names = []
            f[g].visit(names.append)
            out[g] = names
    out["acquisition"] = sorted(f["acquisition"].keys())
    return out


def file_summary(asset: dict) -> dict:
    """Metadata and array shapes of one file, without reading its data."""
    return _retry(lambda a: _summary(open_nwb(a), a), asset)


def _summary(f: h5py.File, a: dict) -> dict:
    es = f["acquisition/ElectricalSeries"]
    pos = f["acquisition/position"]
    return {
        "path": a["path"], "size_gb": a["size"] / 1e9, "asset_id": a["asset_id"],
        "mouse": f["general/subject/subject_id"][()].decode(),
        "session_description": f["session_description"][()].decode(),
        "session_id": f["general/session_id"][()].decode(),
        "start": f["session_start_time"][()].decode(),
        "es_samples": es["data"].shape[0], "es_channels": es["data"].shape[1],
        "es_rate": float(es["starting_time"].attrs["rate"]),
        "es_conversion": float(es["data"].attrs["conversion"]),
        "es_unit": str(es["data"].attrs["unit"]),
        "pos_shape": tuple(pos["data"].shape),
        "pos_description": str(pos.attrs.get("description", "")),
        "contents": _contents(f),
    }


def survey_file(asset: dict) -> dict:
    """Metadata, contents and the position summary of one file, from one streamed open."""
    def one(a):
        f = open_nwb(a)
        out = _summary(f, a)
        out.update(_vr(f) if out["session_description"] == "vr" else _of(f))
        return out
    return _retry(one, asset)


def vr_behaviour(asset: dict) -> dict:
    """Per VR session: trials, trial types, track length, stops and a digest of the position data.

    Columns of acquisition/position/data in VR files are (position cm, trial number, trial type);
    the description gives "trials: non-zero indexed, trial types: 0-beaconed, 1-nonbeaconed, 2-probe".
    """
    return _retry(lambda a: dict(path=a["path"], **_vr(open_nwb(a))), asset)


def _vr(f: h5py.File) -> dict:
    d = f["acquisition/position/data"][:]
    ts = f["acquisition/position/timestamps"][:]
    es_dur = f["acquisition/ElectricalSeries/data"].shape[0] / FS_EPHYS
    x, trial, ttype = d[:, 0], d[:, 1].astype(int), d[:, 2]
    trials = np.unique(trial)
    # trial type of each trial: the most common value within it
    per_trial_type = {}
    bounds = np.flatnonzero(np.diff(trial)) + 1
    starts = np.r_[0, bounds]
    ends = np.r_[bounds, len(trial)]
    tt = []
    tmax = []
    for s, e in zip(starts, ends):
        vals, cnt = np.unique(ttype[s:e], return_counts=True)
        tt.append(vals[np.argmax(cnt)])
        tmax.append(x[s:e].max())
    tt = np.array(tt)
    for v in (0, 1, 2):
        per_trial_type[int(v)] = int((tt == v).sum())
    dt = np.median(np.diff(ts))
    # speed over the previous 100 ms (files' notes), from unwrapped position
    track = 10 * round(float(np.median(tmax)) / 10)
    unwrapped = x + track * (trial - trial.min())
    lag = int(round(0.1 / dt))
    speed = np.full_like(x, np.nan)
    speed[lag:] = (unwrapped[lag:] - unwrapped[:-lag]) / (lag * dt)
    stopped = speed < STOP_SPEED_CM_S
    n_stop_onsets = int(np.sum(stopped[1:] & ~stopped[:-1]))
    return {
        "n_samples": len(ts), "t_first": float(ts[0]), "t_last": float(ts[-1]),
        "dt": float(dt), "es_duration": es_dur,
        "x_min": float(np.nanmin(x)), "x_max": float(np.nanmax(x)),
        "median_trial_max_x": float(np.median(tmax)), "track_length": track,
        "trial_first": int(trials.min()), "trial_last": int(trials.max()),
        "n_trials": int(len(trials)), "n_trial_runs": int(len(starts)),
        "trial_monotonic": bool(np.all(np.diff(trial) >= 0)),
        "trial_types_present": sorted(int(v) for v in np.unique(ttype)),
        "n_beaconed": per_trial_type[0], "n_nonbeaconed": per_trial_type[1], "n_probe": per_trial_type[2],
        "trial_type_sequence": "".join("BNP"[int(v)] if v in (0, 1, 2) else "?" for v in tt[:30]),
        "median_speed": float(np.nanmedian(speed)), "n_stop_onsets": n_stop_onsets,
        "md5": hashlib.md5(np.ascontiguousarray(d).tobytes()).hexdigest(),
    }


def of_position(asset: dict) -> dict:
    """Per open arena session: ranges of the nine undescribed position columns and a digest."""
    return _retry(lambda a: dict(path=a["path"], **_of(open_nwb(a))), asset)


def _of(f: h5py.File) -> dict:
    d = f["acquisition/position/data"][:]
    ts = f["acquisition/position/timestamps"][:]
    es_dur = f["acquisition/ElectricalSeries/data"].shape[0] / FS_EPHYS
    return {
        "n_samples": len(ts), "t_first": float(ts[0]), "t_last": float(ts[-1]),
        "dt": float(np.median(np.diff(ts))), "es_duration": es_dur,
        "col_min": np.nanmin(d, axis=0).tolist(), "col_max": np.nanmax(d, axis=0).tolist(),
        "col_nan": np.isnan(d).mean(axis=0).tolist(),
        "md5": hashlib.md5(np.ascontiguousarray(d).tobytes()).hexdigest(),
    }


def file_text(asset: dict) -> dict:
    """The free-text metadata of one file: notes, experiment and session descriptions, protocol."""
    def one(a):
        f = open_nwb(a)
        out = {"path": a["path"]}
        for k in ("session_description", "general/notes", "general/experiment_description",
                  "general/protocol", "general/session_id"):
            out[k] = f[k][()].decode() if k in f else None
        return out
    return _retry(one, asset)


def map_files(fn, assets, workers=16):
    """Apply fn to each asset in worker processes (h5py holds a global lock, so threads serialise)."""
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(fn, assets))


def raw_block_digest(asset: dict, n_samples: int = 30000, offset: int = 3_000_000) -> dict:
    """Digest of a block of the raw signal, to tell whether two files hold the same recording."""
    def one(a):
        x = open_nwb(a)["acquisition/ElectricalSeries/data"][offset:offset + n_samples]
        return {"path": a["path"], "md5": hashlib.md5(x.tobytes()).hexdigest(), "std": float(x.std())}
    return _retry(one, asset)


def _timed_read(arg):
    a, n = arg
    ds = open_nwb(a)["acquisition/ElectricalSeries/data"]
    t = time.time()
    x = ds[1_000_000:1_000_000 + n]
    return x.nbytes, time.time() - t


def streaming_rate(assets: list[dict], seconds_per_read: float = 20.0, workers: int = 8) -> dict:
    """Throughput of streaming the raw signal: each worker reads one block from a different file."""
    n = int(seconds_per_read * FS_EPHYS)
    t0 = time.time()
    res = map_files(_timed_read, [(a, n) for a in assets], workers)
    wall = time.time() - t0
    nbytes = sum(r[0] for r in res)
    per_file = [r[0] / r[1] / 1e6 for r in res]
    return {"bytes": nbytes, "wall_s": wall, "aggregate_mb_s": nbytes / wall / 1e6,
            "single_stream_mb_s": float(np.median(per_file)), "workers": workers}


def mua_and_speed(asset: dict, start_s: float, minutes: float, bin_s: float = 0.1) -> dict:
    """Multi-unit activity and running speed of one session in bins, on the ephys clock.

    The raw signal (all 16 channels) is re-referenced to the median across channels, filtered 600 to
    6000 Hz (the paper's sorting band, Methods, Spike sorting), and negative threshold crossings below
    4 robust SD (median absolute deviation / 0.6745) are counted per bin over all channels. Speed per
    bin comes from the position series, whose timestamps start at 0 like the ephys series
    (starting_time 0). For VR files position is column 0 unwrapped with the trial number (column 1);
    for open arena files columns 1 and 3 are read as x and y in cm (their ranges, 0 to about 100,
    fit the 100 cm arena; the columns are not described in the file).
    """
    f = open_nwb(asset)
    es = f["acquisition/ElectricalSeries/data"]
    i0 = int(start_s * FS_EPHYS)
    n = int(minutes * 60 * FS_EPHYS)
    raw = es[i0:i0 + n].astype(np.float32)
    raw -= np.median(raw, axis=1, keepdims=True)
    sos = signal.butter(3, [600, 6000], btype="bandpass", fs=FS_EPHYS, output="sos")
    filt = signal.sosfilt(sos, raw[::-1], axis=0)[::-1]
    filt = signal.sosfilt(sos, filt, axis=0)
    del raw
    thr = -4 * np.median(np.abs(filt), axis=0) / 0.6745
    below = filt < thr
    onsets = below[1:] & ~below[:-1]
    t_on = (np.nonzero(onsets)[0] + 1) / FS_EPHYS + start_s
    del filt, below, onsets
    nb = int(round(minutes * 60 / bin_s))
    edges = start_s + np.arange(nb + 1) * bin_s
    mua = np.histogram(t_on, edges)[0].astype(float)

    d = f["acquisition/position/data"][:]
    ts = f["acquisition/position/timestamps"][:]
    idx = np.clip(np.searchsorted(ts, edges), 0, len(ts) - 1)
    if d.shape[1] == 3:
        x, trial = d[:, 0], d[:, 1]
        track = 10 * round(float(np.nanmax(x)) / 10)
        unwrapped = x + track * (trial - trial.min())
        speed = np.diff(unwrapped[idx]) / bin_s
    else:
        xy = d[:, [1, 3]]
        step = np.hypot(*np.diff(xy, axis=0).T)
        cum = np.r_[0, np.nancumsum(step)]
        speed = np.diff(cum[idx]) / bin_s
    return {"edges": edges, "mua": mua, "speed": speed,
            "threshold_uv": thr * float(es.attrs["conversion"]) * 1e6}


def shifted_contrast(mua: np.ndarray, speed: np.ndarray, shifts, stop_speed: float = STOP_SPEED_CM_S):
    """Ratio of mean multi-unit counts in running bins to stopped bins, with the labels shifted.

    For a shift of sh bins, mua[t] is labelled by speed[t + sh], the same sign convention as
    lagged_corr(mua, speed); bins without a partner at the window ends are dropped (no wrap-around).
    """
    out = []
    n = len(mua)
    for sh in shifts:
        if sh >= 0:
            m, sp = mua[:n - sh], speed[sh:]
        else:
            m, sp = mua[-sh:], speed[:n + sh]
        ok = np.isfinite(sp)
        st = sp[ok] < stop_speed
        out.append(m[ok][~st].mean() / m[ok][st].mean())
    return np.array(out)


def lagged_corr(a: np.ndarray, b: np.ndarray, max_lag: int) -> tuple[np.ndarray, np.ndarray]:
    """Pearson correlation of a[t] with b[t + lag] for lag in -max_lag..max_lag bins."""
    lags = np.arange(-max_lag, max_lag + 1)
    out = []
    for L in lags:
        if L >= 0:
            x, y = a[:len(a) - L], b[L:]
        else:
            x, y = a[-L:], b[:len(b) + L]
        ok = np.isfinite(x) & np.isfinite(y)
        out.append(np.corrcoef(x[ok], y[ok])[0, 1])
    return lags, np.array(out)


def mua_check(asset: dict) -> dict:
    """mua_and_speed over five minutes from 300 s (a standard window for the clock check)."""
    return mua_and_speed(asset, start_s=300.0, minutes=5.0)
