"""Loading and measures for dandiset 000128 (MC_Maze, monkey Jenkins, maze task, two Utah arrays).

Used by the reproduction of Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68:387-400.
Where a parameter comes from is said next to it: "M1" to "M9" are the method headers of the claims
file claims/000128/10.1016-j.neuron.2010.09.015.yaml (which cite the paper), and "standard choice"
marks a detail that the claims file calls a standard choice or that cannot change a result.

The data are streamed from the archive with remfile and h5py and read with pynwb; nothing is
written to disk.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import requests
import remfile
import h5py
import pynwb
from scipy.ndimage import gaussian_filter1d

DANDISET_ID = "000128"
VERSION = "0.220113.0400"          # the only published version; see the notebook header
API = "https://api.dandiarchive.org/api"
TRAIN_PATH = "sub-Jenkins/sub-Jenkins_ses-full_desc-train_behavior+ecephys.nwb"
TEST_PATH = "sub-Jenkins/sub-Jenkins_ses-full_desc-test_ecephys.nwb"

SIGMA_MS = 20        # M2, Gaussian of 20 ms, read as SD 20 ms (claims file: a standard choice)
STEP_MS = 10         # M2, rates sampled every 10 ms (claims file: a standard choice)
PREP_WIN = (-200, 100)     # M4, ms from the go cue
PERI_WIN = (-100, 350)     # M4, ms from movement onset
TMAT_WIN = (-150, 800)     # M5, maze peri-movement T-matrix, ms from movement onset
MIN_DELAY_MS = 400         # M1, trials with delay > 400 ms
PROTO_R = 0.9              # M1, correlation with the proto-trial
PROTO_WIN = (-150, 800)    # M1 (reading T2), window of the velocity profiles, ms from movement onset
PREP_TUNING_MIN = 5.0      # M6, J-array, more than 5 spikes/s of preparatory tuning
PERI_TUNING_RATIO = 1.5    # M6, peri-movement tuning at least 1.5 times the preparatory tuning


# ---------------------------------------------------------------- archive access

def list_assets(version: str = VERSION) -> list[dict]:
    """Assets of the dandiset at a version, from the DANDI REST API."""
    out, url = [], f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/"
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r.get("next")
    return out


def version_metadata(version: str = VERSION) -> dict:
    return requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{version}/", timeout=60).json()


def asset_s3_url(path: str, version: str = VERSION) -> str:
    """The S3 address of an asset at the pinned version (the API's download redirect)."""
    asset = next(a for a in list_assets(version) if a["path"] == path)
    r = requests.head(f"{API}/assets/{asset['asset_id']}/download/", allow_redirects=False, timeout=60)
    return r.headers["Location"].split("?")[0]


def open_nwb(path: str, version: str = VERSION):
    """Stream an NWB file; returns (nwbfile, io). Keep io open while reading."""
    f = h5py.File(remfile.File(asset_s3_url(path, version)), "r")
    io = pynwb.NWBHDF5IO(file=f, mode="r", load_namespaces=True)
    return io.read(), io


# ---------------------------------------------------------------- loading

def load_session(nwb) -> dict:
    """Trials, units, spike times and hand kinematics of the train file.

    Spike times are read as one flat array and split by the units' index. Hand position and
    velocity are read whole (1 kHz, mm and mm/s as the series descriptions say).
    """
    trials = nwb.trials.to_dataframe()
    tp = np.array([np.asarray(p)[a] for p, a in zip(trials.target_pos, trials.active_target)])
    trials["target_x"], trials["target_y"] = tp[:, 0], tp[:, 1]
    trials["condition"] = trials.groupby(["trial_type", "trial_version"]).ngroup()

    u = nwb.units
    flat = u.spike_times.data[:]
    idx = u.spike_times_index.data[:]
    starts = np.r_[0, idx[:-1]]
    spikes = [np.asarray(flat[a:b]) for a, b in zip(starts, idx)]
    el_idx = u.electrodes.data[:]
    el = nwb.electrodes.to_dataframe()
    units = pd.DataFrame({
        "unit_id": u.id.data[:],
        "heldout": u.heldout.data[:],
        "electrode_row": el_idx,
        "electrode_group": el["group_name"].values[el_idx],
        "n_spikes": [len(s) for s in spikes],
    })
    units["id_digit"] = units.unit_id // 1000          # leading digit of the unit id
    units["id_channel"] = (units.unit_id // 10) % 100   # next two digits

    beh = nwb.processing["behavior"]
    pos = beh["hand_pos"].data[:]
    vel = beh["hand_vel"].data[:]
    ts = beh["hand_pos"].timestamps[:]
    same_ts = np.array_equal(beh["hand_vel"].timestamps[:], ts)
    return dict(trials=trials, units=units, spikes=spikes, hand_pos=pos, hand_vel=vel,
                hand_t=ts, vel_shares_pos_timestamps=same_ts)


def kinematic_windows(sess: dict, event: np.ndarray, before_ms: int, after_ms: int):
    """Hand position and velocity (trials x ms x 2) from event-before to event+after, 1 ms steps.

    The behaviour series have timestamps on a 1 ms grid within trials and gaps between trials;
    the sample nearest each window start is found by its timestamp, and the largest difference
    between the timestamps used and the intended times is returned as a check (seconds).
    """
    t = sess["hand_t"]
    start = event - before_ms / 1000
    i0 = np.clip(np.searchsorted(t, start - 0.0005), 0, len(t) - 1)
    off = np.arange(before_ms + after_ms + 1)
    ii = np.clip(i0[:, None] + off[None, :], 0, len(t) - 1)
    err = np.abs(t[ii] - (start[:, None] + off[None, :] / 1000)).max()
    return sess["hand_pos"][ii], sess["hand_vel"][ii], err


# ---------------------------------------------------------------- trial selection (M1)

def proto_trial_keep(vel: np.ndarray, cond: np.ndarray, base: np.ndarray, reading: str) -> np.ndarray:
    """M1: keep trials whose velocity profile correlates with the condition's mean at r > 0.9.

    vel: trials x time x 2 over PROTO_WIN; base: trials eligible (delay > 400 ms), which also form
    the proto-trial (T1, T2: the condition's mean velocity over its trials). T1: each component at
    r > 0.9; T2: the two components concatenated. The claims file's answer of 2026-10-22 keeps T2
    alone; T1 stays here so its count can be shown.
    """
    keep = np.zeros(len(cond), bool)
    for c in np.unique(cond):
        m = np.where(base & (cond == c))[0]
        proto = vel[m].mean(0)
        for i in m:
            if reading == "T1":
                r = [np.corrcoef(vel[i, :, j], proto[:, j])[0, 1] for j in (0, 1)]
                keep[i] = min(r) > PROTO_R
            elif reading == "T2":
                keep[i] = np.corrcoef(vel[i].T.ravel(), proto.T.ravel())[0, 1] > PROTO_R
            else:
                raise ValueError(reading)
    return keep


# ---------------------------------------------------------------- firing rates (M2)

def averaging_matrix(cond: np.ndarray, keep: np.ndarray, n_cond: int) -> np.ndarray:
    """Rows average the kept trials of each condition; a condition with no kept trial gets a row of NaN."""
    A = np.zeros((n_cond, len(cond)))
    for c in range(n_cond):
        m = keep & (cond == c)
        if m.any():
            A[c, m] = 1.0 / m.sum()
        else:
            A[c] = np.nan
    return A


def condition_rates(spikes: list[np.ndarray], event: np.ndarray, before_ms: int, after_ms: int,
                    avg: dict[str, np.ndarray], pad_ms: int = 100) -> tuple[np.ndarray, dict]:
    """Condition-mean smoothed rates (spikes/s), units x conditions x samples, for each averaging matrix.

    Spikes are counted in 1 ms bins from event-before-pad to event+after+pad, smoothed with a
    Gaussian of SD 20 ms (M2), sampled every 10 ms from -before to +after, and averaged over the
    trials each matrix in `avg` selects. The pad keeps the edges free of the smoothing's boundary.
    """
    times = np.arange(-before_ms, after_ms + 1, STEP_MS)
    nb = before_ms + after_ms + 2 * pad_ms + 1
    lo_t = event - (before_ms + pad_ms) / 1000
    hi_t = event + (after_ms + pad_ms + 1) / 1000
    samp = pad_ms + before_ms + times
    out = {k: np.zeros((len(spikes), a.shape[0], len(times))) for k, a in avg.items()}
    ntr = len(event)
    for u, s in enumerate(spikes):
        lo = np.searchsorted(s, lo_t)
        hi = np.searchsorted(s, hi_t)
        cnt = hi - lo
        tot = cnt.sum()
        counts = np.zeros((ntr, nb))
        if tot:
            idx = np.repeat(lo - np.r_[0, np.cumsum(cnt)[:-1]], cnt) + np.arange(tot)
            tri = np.repeat(np.arange(ntr), cnt)
            b = np.floor((s[idx] - lo_t[tri]) * 1000).astype(int)
            ok = (b >= 0) & (b < nb)
            np.add.at(counts, (tri[ok], b[ok]), 1.0)
        sm = gaussian_filter1d(counts, SIGMA_MS, axis=1, mode="constant")[:, samp] * 1000.0
        for k, a in avg.items():
            out[k][u] = a @ sm
    return times, out


def window_mean(rates: np.ndarray, times: np.ndarray, win: tuple[int, int]) -> np.ndarray:
    m = (times >= win[0]) & (times <= win[1])
    return rates[..., m].mean(-1)


def tuning(x: np.ndarray, reading: str) -> np.ndarray:
    """M6 tuning of condition rates (units x conditions). S1 range, S2 SD over conditions.

    The claims file's answer of 2026-10-22 keeps S1 alone; S2 is not used by the notebook.
    """
    if reading == "S1":
        return x.max(1) - x.min(1)
    if reading == "S2":
        return x.std(1)
    raise ValueError(reading)


# ---------------------------------------------------------------- PD fits (M7)

def loo_performance(S: np.ndarray, Y: np.ndarray) -> np.ndarray:
    """M7: leave-one-condition-out performance of x = b0 + S b, for each column of Y (c x N).

    Performance = 1 - mean squared LOO error / variance over conditions (denominator c). The LOO
    residuals are the exact ones of least squares, e_i / (1 - h_ii).
    """
    c = Y.shape[0]
    X = np.column_stack([np.ones(c), S])
    H = X @ np.linalg.pinv(X)
    R = Y - H @ Y
    loo = R / (1 - np.diag(H))[:, None]
    return 1 - (loo ** 2).mean(0) / Y.var(0)


def pca_scores(T: np.ndarray, kmax: int) -> np.ndarray:
    """First kmax PCA scores of the rows of T (columns mean-centred)."""
    Tc = T - T.mean(0)
    U, s, _ = np.linalg.svd(Tc, full_matrices=False)
    return U[:, :kmax] * s[:kmax]


def gram_leave_one_out_scores(blocks: np.ndarray, kmax: int):
    """For each neuron n, PCA scores (c x kmax) of the T-matrix of all other neurons (M5).

    blocks: neurons x conditions x times. Uses the Gram matrix of the centred T-matrix, from which
    each neuron's own block is subtracted. Yields (n, scores).
    """
    B = blocks - blocks.mean(1, keepdims=True)
    G = np.einsum("nct,ndt->cd", B, B)
    for n in range(B.shape[0]):
        Gn = G - B[n] @ B[n].T
        w, V = np.linalg.eigh(Gn)
        order = np.argsort(w)[::-1][:kmax]
        yield n, V[:, order] * np.sqrt(np.clip(w[order], 0, None))


def peri_space_performance(blocks: np.ndarray, X: np.ndarray, kmax: int) -> np.ndarray:
    """Performance (neurons x k=1..kmax) of each neuron's preparatory rates X (c x neurons) in the
    peri-movement space built from the other neurons' blocks."""
    out = np.zeros((blocks.shape[0], kmax))
    for n, S in gram_leave_one_out_scores(blocks, kmax):
        for k in range(1, kmax + 1):
            out[n, k - 1] = loo_performance(S[:, :k], X[:, [n]])[0]
    return out


def space_performance_all_k(S_full: np.ndarray, X: np.ndarray, kmax: int) -> np.ndarray:
    """Performance (neurons x k) in one PCA space shared by all neurons."""
    return np.column_stack([loo_performance(S_full[:, :k], X) for k in range(1, kmax + 1)])


# ---------------------------------------------------------------- kinematic and task spaces

def unit_range(a: np.ndarray) -> np.ndarray:
    return a / (a.max() - a.min())


def kinematic_tmatrix(pos: np.ndarray, vel: np.ndarray, acc: np.ndarray, n_blocks: int | None):
    """Kinematic T-matrix (Methods, PCA-based spaces): horizontal and vertical position, velocity
    and acceleration of the condition means (conditions x times), each scaled to unit range over
    times and conditions. n_blocks None: the six variables once each (D1); otherwise the six in
    turn until there are n_blocks column blocks (D2)."""
    vars6 = [unit_range(v) for v in (pos[..., 0], pos[..., 1], vel[..., 0], vel[..., 1],
                                     acc[..., 0], acc[..., 1])]
    if n_blocks is None:
        return np.concatenate(vars6, axis=1)
    return np.concatenate([vars6[i % 6] for i in range(n_blocks)], axis=1)


def end_of_reach(speed: np.ndarray, start: int) -> int:
    """M9: when speed first falls below 5% of its peak after the peak (claims file standard choice);
    the last sample if it never does."""
    pk = start + int(np.argmax(speed[start:]))
    below = np.where(speed[pk:] < 0.05 * speed[pk])[0]
    return pk + int(below[0]) if len(below) else len(speed) - 1


def _resample_path(xy: np.ndarray, fractions: np.ndarray) -> np.ndarray:
    seg = np.r_[0, np.cumsum(np.linalg.norm(np.diff(xy, axis=0), axis=1))]
    s = fractions * seg[-1]
    return np.column_stack([np.interp(s, seg, xy[:, 0]), np.interp(s, seg, xy[:, 1])])


def task_features(pos: np.ndarray, vel: np.ndarray, onset_idx: int) -> dict:
    """M9 task-space features of one condition-mean trajectory (1 ms samples; onset at onset_idx)."""
    speed = np.linalg.norm(vel, axis=1)
    end = end_of_reach(speed, onset_idx)
    p, v = pos[onset_idx:end + 1], vel[onset_idx:end + 1]
    sp = speed[onset_idx:end + 1]
    start, endp = p[0], p[-1]
    d = endp - start
    dn = d / np.linalg.norm(d)
    rel = p - start
    perp = dn[0] * rel[:, 1] - dn[1] * rel[:, 0]          # positive to the left: counterclockwise
    i_abs = int(np.argmax(np.abs(perp)))
    i_ccw = int(np.argmax(perp))
    ipk = int(np.argmax(sp))
    ix, iy = int(np.argmax(np.abs(v[:, 0]))), int(np.argmax(np.abs(v[:, 1])))
    n = len(p)
    thirds_t = p[[0, n // 3, (2 * n) // 3, n - 1]]
    thirds_l = _resample_path(p, np.array([0, 1 / 3, 2 / 3, 1]))
    return dict(
        end_ms=end - onset_idx,
        endpoint=endp,
        max_speed=sp.max(),
        init_vel=vel[onset_idx:onset_idx + 150].mean(0),
        orth_excursion=perp[i_abs],
        viapoint=p[i_abs],
        maxvel_V1a=np.array([np.abs(v[:, 0]).max(), np.abs(v[:, 1]).max()]),
        maxvel_V1b=np.array([v[ix, 0], v[iy, 1]]),
        maxvel_V2=v[ipk],
        halfpoint=_resample_path(p, np.array([0.5]))[0],
        segdirs_G1=np.diff(thirds_l, axis=0).ravel(),
        segdirs_G2=np.diff(thirds_t, axis=0).ravel(),
        ccw_excursion=perp[i_ccw],
        ccw_point=p[i_ccw],
    )


def task_spaces(feats: list[dict], barriers: np.ndarray, distractors: np.ndarray) -> dict:
    """M9 task spaces (conditions x dims), with the readings V1 (a: magnitudes, b: signed value at
    the maximum magnitude), V2, G1 and G2 as separate entries."""
    F = lambda k: np.array([f[k] for f in feats])
    ep = F("endpoint")
    sp = {
        "endpoints + max speed": np.column_stack([ep, F("max_speed")]),
        "initial velocity": F("init_vel"),
        "endpoints + orthogonal excursion": np.column_stack([ep, F("orth_excursion")]),
        "endpoints + viapoint": np.column_stack([ep, F("viapoint")]),
        "endpoints + max velocity (V1a)": np.column_stack([ep, F("maxvel_V1a")]),
        "endpoints + max velocity (V1b)": np.column_stack([ep, F("maxvel_V1b")]),
        "endpoints + max velocity (V2)": np.column_stack([ep, F("maxvel_V2")]),
        "endpoints + halfpoint": np.column_stack([ep, F("halfpoint")]),
        "segment directions (G1)": F("segdirs_G1"),
        "segment directions (G2)": F("segdirs_G2"),
    }
    for g in ("G1", "G2"):
        sp[f"kitchen sink ({g})"] = np.column_stack([F(f"segdirs_{g}"), F("ccw_excursion"),
                                                     F("ccw_point"), barriers, distractors])
    return sp


# ---------------------------------------------------------------- tests

def mean_tests(r: np.ndarray) -> dict:
    """P1 to P3 of fig4d: tests of the mean correlation against zero, two-sided."""
    from scipy import stats
    return {
        "P1 t-test on r": stats.ttest_1samp(r, 0).pvalue,
        "P2 t-test on Fisher z": stats.ttest_1samp(np.arctanh(np.clip(r, -0.999999, 0.999999)), 0).pvalue,
        "P3 Wilcoxon": stats.wilcoxon(r).pvalue,
    }


def corr_rows(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Pearson correlation of matching rows of a and b."""
    a = a - a.mean(1, keepdims=True)
    b = b - b.mean(1, keepdims=True)
    return (a * b).sum(1) / np.sqrt((a * a).sum(1) * (b * b).sum(1))


def spearman_rows(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    from scipy.stats import rankdata
    return corr_rows(rankdata(a, axis=1), rankdata(b, axis=1))


# ---------------------------------------------------------------- the Figure 8 model

def oscillator(x0: np.ndarray, n_steps: int, exact: bool = False) -> np.ndarray:
    """x(t+1) = W x(t) from the Figure 8 legend (exact=True: the pure one-degree rotation).
    x0: conditions x 2. Returns conditions x 2 x n_steps (the states after 1..n_steps steps)."""
    a = 2 * np.pi / 360
    W = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]]) if exact else \
        np.array([[1, -a], [a, 1]])
    out = np.zeros((x0.shape[0], 2, n_steps))
    x = x0.copy()
    for t in range(n_steps):
        x = x @ W.T
        out[:, :, t] = x
    return out
