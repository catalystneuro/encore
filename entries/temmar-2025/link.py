"""Loading and measures for the LINK dataset (DANDI:001201), used by the notebooks of the
temmar-2025 entry, which test Temmar et al. (2025), NeurIPS Datasets and Benchmarks.

Where each parameter comes from is given next to it, as one of:
- "claim <id>": the claims file's criterion for that claim (claims/temmar-2025.yaml), which cites
  the paper or its code (github.com/chesteklab/LINK_dataset at 5e1c36a);
- "paper, <passage>": a detail the claims file lacks, taken from the paper (protocol, author 1.6);
- "assumption": a choice the paper leaves open, stated as such;
- "standard choice": a detail that cannot change a result.

The data are streamed from the archive (remfile + h5py); nothing is written to disk.
"""
from __future__ import annotations

import os
from functools import lru_cache

import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET = "001201"
VERSION = "0.261026.1912"   # most recent published version; the paper cites none
API = "https://api.dandiarchive.org/api"

BIN_S = 0.02                # 20 ms bins (paper, Section 3; checked on the timestamps)
TCR_TO_HZ = 50.0            # counts per 20 ms bin times 50 = Hz (claim fig2b-active-channels-decrease)
SBP_CODE_SCALE = 0.25       # claim fig2a-sbp-decline, reading (a): NWB values times 0.25
DAYS_PER_MONTH = 30.44      # claim fig2a-sbp-decline
KIN_NAMES = ["idx_pos", "mrs_pos", "idx_vel", "mrs_vel"]   # order of the code (utils/nwb_tools.py)
N_TRAIN_TRIALS = 300        # paper, Appendix C.1: first 300 trials train, last 75 test


# --------------------------------------------------------------------------------------------
# Archive
# --------------------------------------------------------------------------------------------

@lru_cache(maxsize=1)
def version_metadata() -> dict:
    return requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/", timeout=60).json()


@lru_cache(maxsize=1)
def assets() -> pd.DataFrame:
    """Every asset of the pinned version, with its session date from the file name."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000"
    rows = []
    while url:
        r = requests.get(url, timeout=60).json()
        rows += r["results"]
        url = r.get("next")
    df = pd.DataFrame([{"path": a["path"], "asset_id": a["asset_id"], "size": a["size"]} for a in rows])
    df["date"] = pd.to_datetime(df["path"].str.extract(r"ses-(\d{8})")[0], format="%Y%m%d")
    return df.sort_values(["date", "path"]).reset_index(drop=True)


def s3_url(asset_id: str) -> str:
    r = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60)
    return r.url


def open_asset(asset_id: str) -> h5py.File:
    return h5py.File(remfile.File(s3_url(asset_id)), "r")


def _str(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def read_session(asset_id: str, neural=True, tcr=True, kin=True, meta=False) -> dict:
    """One session file, reduced to what the analyses use. Arrays are float32 except time.

    trial_index is the bin at which each trial starts, found as the code does
    (np.searchsorted of the start times in the timestamps, utils/nwb_tools.py)."""
    out = {}
    with open_asset(asset_id) as f:
        an = f["analysis"]
        ts = an["SpikingBandPower/timestamps"][:]
        out["t"] = ts
        if neural:
            out["sbp"] = an["SpikingBandPower/data"][:].astype(np.float32)
        if tcr:
            out["tcr"] = an["ThresholdCrossings/data"][:].astype(np.float32)
        if kin:
            out["kin"] = np.column_stack([an[n + "/data"][:].ravel() for n in
                                          ("index_position", "mrs_position", "index_velocity",
                                           "mrs_velocity")]).astype(np.float32)
        tr = f["intervals/trials"]
        trials = pd.DataFrame({k: tr[k][:] for k in
                               ("start_time", "stop_time", "trial_number", "trial_count", "run_id",
                                "index_target_position", "mrs_target_position", "trial_timeout")})
        trials["target_style"] = [_str(s) for s in tr["target_style"][:]]
        out["trials"] = trials
        out["trial_index"] = np.searchsorted(ts, trials["start_time"].to_numpy())
        out["style"] = trials["target_style"].iloc[0]
        out["identifier"] = _str(f["identifier"][()])
        out["start"] = _str(f["session_start_time"][()])
        if meta:
            out["series"] = {n: {"shape": an[n]["data"].shape, "unit": _str(an[n]["data"].attrs.get("unit")),
                                 "conversion": float(an[n]["data"].attrs.get("conversion")),
                                 "n_timestamps": an[n]["timestamps"].shape[0],
                                 "same_t": bool(np.array_equal(an[n]["timestamps"][:], ts))}
                             for n in an}
            out["trial_columns"] = [_str(c) for c in tr.attrs["colnames"]]
            e = f["general/extracellular_ephys/electrodes"]
            out["electrode_columns"] = [_str(c) for c in e.attrs["colnames"]]
            out["electrodes"] = pd.DataFrame({k: ([(_str(v) if isinstance(v, bytes) else v) for v in e[k][:]]
                                                  if k in e else [np.nan] * e["id"].shape[0])
                                              for k in ("id", "array_name", "bank", "row", "col", "imp")})
    return out


def read_layout(asset_id: str) -> dict:
    """Metadata, shapes and attributes of a file, without reading its large arrays."""
    with open_asset(asset_id) as f:
        an = f["analysis"]
        series = {}
        for name in an:
            d = an[name]["data"]
            t = an[name]["timestamps"]
            series[name] = {"shape": d.shape, "unit": _str(d.attrs.get("unit")),
                            "conversion": float(d.attrs.get("conversion")),
                            "n_timestamps": t.shape[0],
                            "description": _str(an[name].attrs.get("description"))}
        e = f["general/extracellular_ephys/electrodes"]
        el = pd.DataFrame({k: [(_str(v) if isinstance(v, bytes) else v) for v in e[k][:]]
                           for k in ("id", "array_name", "group_name", "bank", "pin", "row", "col",
                                     "imp", "location")})
        tr = f["intervals/trials"]
        cols = list(tr.attrs["colnames"])
        trials = pd.DataFrame({k: tr[k][:] for k in ("start_time", "stop_time", "trial_count")})
        trials["target_style"] = [_str(s) for s in tr["target_style"][:]]
        return {"series": series, "electrodes": el, "trial_columns": [_str(c) for c in cols],
                "n_trials": tr["id"].shape[0], "trials": trials,
                "identifier": _str(f["identifier"][()]),
                "session_start_time": _str(f["session_start_time"][()]),
                "subject": {k: _str(f["general/subject/" + k][()]) for k in
                            ("subject_id", "date_of_birth", "sex", "species")},
                "first_t": float(f["analysis/SpikingBandPower/timestamps"][0]),
                "dt": np.unique(np.round(np.diff(f["analysis/SpikingBandPower/timestamps"][:]), 4))}


# --------------------------------------------------------------------------------------------
# Signal measures
# --------------------------------------------------------------------------------------------

def participation_ratio(x: np.ndarray) -> tuple[float, np.ndarray]:
    """PR of samples x (n_samples, n_channels), mean-subtracted and not z-scored, with the
    eigenvalues of the covariance (claim fig2c-pr-decline; code signal_utils.participation_ratio)."""
    x = x.astype(np.float64)
    x = x - x.mean(0)
    ev = np.linalg.eigvalsh(x.T @ x)[::-1]
    ev = np.clip(ev, 0, None)
    return float(ev.sum() ** 2 / (ev ** 2).sum()), ev


def linfit(x, y):
    from scipy.stats import linregress
    r = linregress(np.asarray(x, float), np.asarray(y, float))
    return r


def channel_tuning(sbp: np.ndarray, pos: np.ndarray, max_lag=10) -> np.ndarray:
    """Preferred tuning per channel (claim fig3b-two-channels; code tuning_utils.compute_channel_tuning):
    each channel's SBP z-scored; for each lag 0..max_lag (behaviour at t + lag), the slopes of a
    linear regression with intercept of IDX and MRS position on the channel; the lag with the
    largest norm is kept. Returns (n_channels, 2) coefficients (idx, mrs)."""
    x = sbp.astype(np.float64)
    sd = x.std(0)
    sd[sd < 1e-8] = 1.0
    z = (x - x.mean(0)) / sd
    y = pos.astype(np.float64)
    best = np.zeros((x.shape[1], 2))
    bestn = np.full(x.shape[1], -1.0)
    n = len(z)
    for lag in range(max_lag + 1):
        zx = z[: n - lag]
        yy = y[lag:]
        zc = zx - zx.mean(0)
        yc = yy - yy.mean(0)
        coef = (zc.T @ yc) / (zc ** 2).sum(0)[:, None]
        nrm = np.linalg.norm(coef, axis=1)
        upd = nrm > bestn
        best[upd] = coef[upd]
        bestn[upd] = nrm[upd]
    return best


def circ_median(theta: np.ndarray) -> float:
    """Circular median, by brute-force minimisation of Fisher's d(theta) (paper, Appendix C.2,
    equation 1), over the observed angles (radians)."""
    th = np.asarray(theta, float)
    th = th[np.isfinite(th)]
    d = np.pi - np.abs(np.pi - np.abs(th[:, None] - th[None, :]) % (2 * np.pi))
    return float(th[np.argmin(d.sum(0))])


def wrap(a):
    return (a + np.pi) % (2 * np.pi) - np.pi


def circ_iqr(theta: np.ndarray) -> float:
    """Circular IQR (paper, Appendix C.2): shift the circular median to 0, take the quartiles
    of the angles, and return their difference (radians)."""
    m = circ_median(theta)
    s = wrap(np.asarray(theta, float) - m)
    q1, q3 = np.percentile(s, [25, 75])
    return float(q3 - q1)


# --------------------------------------------------------------------------------------------
# Trials: direction, onset, alignment, throughput
# --------------------------------------------------------------------------------------------

DIRECTIONS = np.arange(8) * 45.0     # paper, Appendix C.3 and Figure S6: eight 45-degree sectors


def trial_directions(trials: pd.DataFrame) -> np.ndarray:
    """Direction class 0..7 (centre angle k*45 degrees, IDX on x, MRS on y) of the vector from the
    previous trial's targets to this trial's targets; -1 for the first trial of a session, whose
    starting targets are not in the file (paper, Appendix C.3)."""
    tg = trials[["index_target_position", "mrs_target_position"]].to_numpy(float)
    d = np.diff(tg, axis=0)
    ang = np.degrees(np.arctan2(d[:, 1], d[:, 0])) % 360
    cls = (np.floor((ang + 22.5) / 45) % 8).astype(int)
    cls[np.linalg.norm(d, axis=1) == 0] = -1
    return np.concatenate([[-1], cls])


def mrs_dominant(cls: int) -> bool:
    """Directions centred on +-90 degrees are MRS-only movements (paper, Appendix C.3)."""
    return cls in (2, 6)


def onset_and_jerk(vel: np.ndarray, k_sd: float):
    """Movement onset: first bin where velocity leaves mean +- k_sd * SD of the first 10% of the
    trial's velocities; alignment: bin of maximum absolute jerk (second difference of velocity)
    before onset (paper, Appendix C.3; k_sd 1 in the paper, 2 in the code). Returns (onset, align)
    or (None, None)."""
    n = len(vel)
    nb = max(int(np.ceil(0.1 * n)), 2)
    base = vel[:nb]
    mu, sd = base.mean(), base.std()
    out = np.where((vel > mu + k_sd * sd) | (vel < mu - k_sd * sd))[0]
    out = out[out >= nb]
    if len(out) == 0:
        return None, None
    on = int(out[0])
    jerk = np.concatenate([[0, 0], np.diff(vel, 2)])
    if on < 1:
        return on, None
    return on, int(np.argmax(np.abs(jerk[:on])))


def throughput(trials: pd.DataFrame, reading: str, width=0.15, hold_s=0.75) -> np.ndarray:
    """Fitts' law throughput per trial, bits/s (claim figs2-throughput-improves, readings a, b, c;
    target width 0.15 from paper, Appendix A.1). The first trial of a session, whose starting
    targets are unknown, is NaN. Trial length is stop_time - start_time."""
    tg = trials[["index_target_position", "mrs_target_position"]].to_numpy(float)
    d = np.diff(tg, axis=0)
    length = (trials["stop_time"] - trials["start_time"]).to_numpy(float)[1:]
    if reading == "a":
        idd, t = np.log2(1 + np.linalg.norm(d, axis=1) / width), length - hold_s
    elif reading == "b":
        idd, t = np.log2(1 + np.linalg.norm(d, axis=1) / width), length
    elif reading == "c":
        idd, t = np.log2(1 + np.abs(d) / width).sum(1), length - hold_s
    else:
        raise ValueError(reading)
    tp = np.where(t > 0, idd / np.where(t > 0, t, 1), np.nan)
    return np.concatenate([[np.nan], tp])


# --------------------------------------------------------------------------------------------
# Decoders (paper, Section 4.3 and Appendix C.1; claim fig4a-sameday-stable; code
# bci_decoding/train_models_singleday.py, data_utils.py, nn_utils.py)
# --------------------------------------------------------------------------------------------

RR_HIST = 8           # bins of history for ridge regression
RR_ALPHA = 0.1
LSTM_SEQ = 20
LSTM_HIDDEN = 300
LSTM_ITERS = 2000
LSTM_BATCH = 64
LSTM_LR = (2e-4, 1e-5)
LSTM_WD = 1e-3
NOISE_WHITE = 0.1     # claim fig4a-sameday-stable: 0.1 per sample (the code passes it as bias, see notebook)
NOISE_BIAS = 0.2      # claim fig4a-sameday-stable: 0.2 per sequence and channel


def split(sess: dict):
    """Training bins (first 300 trials) and test bins (the 75 trials after them, to the end of the
    file), as Appendix C.1 states."""
    i = sess["trial_index"][N_TRAIN_TRIALS]
    return (sess["sbp"][:i], sess["kin"][:i]), (sess["sbp"][i:], sess["kin"][i:])


def zparams(x):
    mu = x.mean(0).astype(np.float64)
    sd = x.std(0).astype(np.float64)
    sd[sd < 1e-8] = 1.0
    return mu, sd


def history(x: np.ndarray, k: int) -> np.ndarray:
    """(n, k, ch) windows ending at each bin, zero-padded before the start of the segment, as
    data_utils.add_history does (padding is applied to the normalised data here)."""
    pad = np.concatenate([np.zeros((k - 1, x.shape[1]), x.dtype), x])
    idx = np.arange(len(x))[:, None] + np.arange(k)[None, :]
    return pad[idx]


def rr_fit(xz: np.ndarray, y: np.ndarray):
    from sklearn.linear_model import Ridge
    m = Ridge(alpha=RR_ALPHA, fit_intercept=True)
    m.fit(history(xz, RR_HIST).reshape(len(xz), -1), y)
    return m.coef_.astype(np.float64), m.intercept_.astype(np.float64)


def rr_predict(model, xz):
    W, b = model
    return history(xz, RR_HIST).reshape(len(xz), -1) @ W.T + b


def r2_per_output(y, p):
    from sklearn.metrics import r2_score
    return np.array([r2_score(y[:, j], p[:, j]) for j in range(y.shape[1])])


def _lstm_modules(torch):
    class LSTMModel(torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.lstm = torch.nn.LSTM(96, LSTM_HIDDEN, 1, batch_first=True)
            self.fc = torch.nn.Linear(LSTM_HIDDEN, 4)

        def forward(self, x):
            o, _ = self.lstm(x)
            return self.fc(o[:, -1])
    return LSTMModel


def lstm_train(segments, seed=42, iters=LSTM_ITERS, init_state=None, out_norm=None, lr=LSTM_LR):
    """Train (or fine-tune, from init_state) the LSTM on a list of (xz, y) segments, xz already
    normalised. Windows of 20 bins never cross a segment boundary. Batches of 64 are drawn without
    replacement within an epoch, as the code's shuffled DataLoader does. Outputs are z-scored on
    the training data unless out_norm is given (kept for fine-tuning). Noise: white noise of SD
    NOISE_WHITE per bin and channel, and a bias of SD NOISE_BIAS per sequence and channel.
    Returns (state_dict, out_norm)."""
    import torch
    torch.set_num_threads(1)
    torch.manual_seed(seed)
    rng = np.random.default_rng(seed)
    X = np.concatenate([np.concatenate([np.zeros((LSTM_SEQ - 1, 96), np.float32), xz.astype(np.float32)])
                        for xz, _ in segments])
    Y = np.concatenate([y for _, y in segments]).astype(np.float64)
    starts, off = [], 0
    for xz, _ in segments:
        starts.append(off + np.arange(len(xz)))
        off += len(xz) + LSTM_SEQ - 1
    starts = np.concatenate(starts)
    if out_norm is None:
        out_norm = zparams(Y)
    Yz = ((Y - out_norm[0]) / out_norm[1]).astype(np.float32)
    Xt = torch.from_numpy(X)
    Yt = torch.from_numpy(Yz)
    model = _lstm_modules(torch)()
    if init_state is not None:
        model.load_state_dict(init_state)
    opt = torch.optim.Adam(model.parameters(), lr=lr[0], weight_decay=LSTM_WD)
    sch = torch.optim.lr_scheduler.LinearLR(opt, start_factor=1.0, end_factor=lr[1] / lr[0], total_iters=iters)
    ar = torch.arange(LSTM_SEQ)
    it = 0
    model.train()
    while it < iters:
        perm = rng.permutation(len(starts))
        for b in range(0, len(perm), LSTM_BATCH):
            if it >= iters:
                break
            sel = perm[b:b + LSTM_BATCH]
            st = torch.from_numpy(starts[sel])
            xb = Xt[st[:, None] + ar[None, :]]
            xb = xb + NOISE_WHITE * torch.randn_like(xb) + NOISE_BIAS * torch.randn(xb.shape[0], 1, 96)
            loss = torch.nn.functional.mse_loss(model(xb), Yt[sel])
            opt.zero_grad()
            loss.backward()
            opt.step()
            sch.step()
            it += 1
    return {k: v.detach().clone() for k, v in model.state_dict().items()}, out_norm


def lstm_predict(state, out_norm, xz: np.ndarray, every=1, batch=2048) -> np.ndarray:
    """Predictions at every `every`-th bin of a normalised segment, inverse-transformed to the
    kinematics' units."""
    import torch
    torch.set_num_threads(1)
    model = _lstm_modules(torch)()
    model.load_state_dict(state)
    model.eval()
    X = np.concatenate([np.zeros((LSTM_SEQ - 1, 96), np.float32), xz.astype(np.float32)])
    idx = np.arange(0, len(xz), every)
    Xt = torch.from_numpy(X)
    ar = torch.arange(LSTM_SEQ)
    out = []
    with torch.no_grad():
        for b in range(0, len(idx), batch):
            st = torch.from_numpy(idx[b:b + batch])
            out.append(model(Xt[st[:, None] + ar[None, :]]).numpy())
    p = np.concatenate(out).astype(np.float64)
    return p * out_norm[1] + out_norm[0]


def pool(n=None):
    """A process pool for LSTM fits, one linear-algebra thread per process."""
    from concurrent.futures import ProcessPoolExecutor
    import multiprocessing as mp
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    return ProcessPoolExecutor(max_workers=n or min(4, os.cpu_count() or 1),
                               mp_context=mp.get_context("spawn"))
