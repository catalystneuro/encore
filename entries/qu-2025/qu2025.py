"""Loading and measures for dandiset 001340 (Qü et al. 2025, PLoS Comput Biol 21(7) e1013226).

Where each parameter comes from is said next to it:
- "claim": the claim's criterion in claims/001340/10.1371-journal.pcbi.1013226.yaml.
- "code": the paper's model code, github.com/Wilbrecht-Lab/cogmodels at commit 589555c
  (file and class named). The cognitive models below are a re-implementation of that code,
  compiled with numba for speed; the notebook checks that they give the same likelihood as the
  code itself on the dataset's trials.
- "Methods": a passage of the paper (section named).
- "assumption": a choice the paper leaves open, with the reason.
- "standard": a detail that cannot change a result.
"""
import json
import urllib.request
import warnings
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import scipy.optimize
import scipy.sparse
import scipy.sparse.linalg
from numba import njit

DANDISET = "001340"
VERSION = "0.250221.0527"
API = "https://api.dandiarchive.org/api"
COGMODELS_REPO = "https://github.com/Wilbrecht-Lab/cogmodels"
COGMODELS_COMMIT = "589555c49bd5ec3ea77b7d0979e644ab80716ae0"


# ----------------------------------------------------------------------------- loading

def list_assets():
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    out = []
    while url:
        d = json.load(urllib.request.urlopen(url))
        out += d["results"]
        url = d.get("next")
    return pd.DataFrame(out)[["asset_id", "path", "size"]]


def _open(asset_id):
    f = remfile.File(f"{API}/assets/{asset_id}/download/")
    return h5py.File(f, "r")


def _dec(v):
    return [x.decode() if isinstance(x, bytes) else x for x in v]


def _read_session(row):
    h = _open(row.asset_id)
    tr = h["intervals/trials"]
    df = {}
    for k in tr.keys():
        if k == "id":
            continue
        v = tr[k][:]
        df[k] = _dec(v) if v.dtype.kind == "O" else v
    df = pd.DataFrame(df)
    df["asset_id"] = row.asset_id
    df["path"] = row.path
    acq = list(h["acquisition"].keys()) if "acquisition" in h else []
    meta = {
        "asset_id": row.asset_id,
        "path": row.path,
        "subject": h["general/subject/subject_id"][()].decode(),
        "age": h["general/subject/age"][()].decode(),
        "sex": h["general/subject/sex"][()].decode(),
        "species": h["general/subject/species"][()].decode(),
        "session_description": h["general/session_description"][()].decode()
        if "general/session_description" in h else h["session_description"][()].decode(),
        "session_id": h["general/session_id"][()].decode(),
        "start": h["session_start_time"][()].decode(),
        "n_trials": len(df),
        "has_fp": "fp_series_470nm" in acq,
    }
    if meta["has_fp"]:
        meta["n_470"] = h["acquisition/fp_series_470nm/data"].shape[0]
        meta["n_415"] = h["acquisition/fp_series_415nm/data"].shape[0]
        ft = "general/fiber_photometry/fiber_photometry_table/"
        meta["location"] = ",".join(sorted(set(_dec(h[ft + "location"][:]))))
        meta["coordinates"] = str(h[ft + "coordinates"][:].tolist())
        meta["unit"] = h["acquisition/fp_series_470nm/data"].attrs["unit"]
    return df, meta


def load_trials(n_threads=8):
    """Stream every session's trial table (and file metadata) at the pinned version."""
    assets = list_assets()
    with ThreadPoolExecutor(n_threads) as ex:
        res = list(ex.map(_read_session, assets.itertuples()))
    trials = pd.concat([r[0] for r in res], ignore_index=True)
    meta = pd.DataFrame([r[1] for r in res]).sort_values("path").reset_index(drop=True)
    return trials, meta


def load_photometry(asset_id):
    """Both channels with their own timestamps (s, session clock)."""
    h = _open(asset_id)
    out = {}
    for ch in ("470", "415"):
        g = h[f"acquisition/fp_series_{ch}nm"]
        out[f"t{ch}"] = g["timestamps"][:]
        out[f"f{ch}"] = g["data"][:]
    return out


# ----------------------------------------------------------------------------- behaviour

def behaviour_frame(trials):
    """Trial frame in the paper code's format (code, base.CogModel.data_cols).

    Decision: right = 1, left = 0, no choice = -1 (code, base.py treats -1 as a miss).
    Sessions are numbered 1..n per mouse in order of postnatal day (Methods, 14 sessions per
    mouse). Timing measures from Methods, Task behavior analysis: MVMT = CI - SOf(t-1),
    center_dur = CO - CI, port_dur = SO1 - O, SO_lat = SO1 - SO0.
    """
    d = trials.copy()
    d["day"] = d["session"].str[1:].astype(int)
    d = d.sort_values(["animal", "day", "trial"]).reset_index(drop=True)
    d["Subject"] = d["animal"]
    d["ID"] = d["animal"]
    days = d.groupby("animal")["day"].transform(lambda x: x.rank(method="dense").astype(int))
    d["session_num"] = days
    d["Session"] = d["animal"] + "_" + d["session"]
    d["Trial"] = d["trial"].astype(int)
    d["Decision"] = d["action"].map({"right": 1, "left": 0}).fillna(-1).astype(int)
    d["Target"] = d["state"].map({"right": 1, "left": 0}).astype(int)
    d["Reward"] = d["rewarded"]
    d["blockTrial"] = d["trial_in_block"].astype(int)
    d["blockNum"] = d["block_num"].astype(int)
    d["valid"] = d["Decision"] >= 0
    prev_same = d["Session"].eq(d["Session"].shift(1))
    d["Switch"] = np.where(prev_same & d["valid"] & d["Decision"].shift(1).ge(0),
                           (d["Decision"] != d["Decision"].shift(1)).astype(float), np.nan)
    d["correct"] = np.where(d["valid"], (d["Decision"] == d["Target"]).astype(float), np.nan)
    d["center_dur"] = d["center_out"] - d["center_in"]
    d["port_dur"] = d["first_side_out"] - d["outcome"]
    d["SO_lat"] = d["first_side_out"] - d["zeroth_side_out"]
    d["MVMT"] = np.where(prev_same, d["center_in"] - d["last_side_out"].shift(1), np.nan)
    return d


def block_switch_measures(d):
    """trial2sw and trial2asymp per block switch (claim; S1 Fig legend).

    For each block after the first in a session, the block trial (first trial of the new block = 0)
    of the first choice of the new correct port (trial2sw), and of the first correct choice
    followed by 2 more correct choices (trial2asymp). Miss trials are skipped (Methods, Task
    behavior analysis: trials with no choice are dropped from behavioural measures). Blocks in
    which the event never happens are left out.
    """
    rows = []
    v = d[d["valid"]]
    for (subj, sess, blk), g in v.groupby(["Subject", "Session", "blockNum"], sort=False):
        if blk == 1:
            continue
        cor = g["correct"].values.astype(bool)
        bt = g["blockTrial"].values
        i_sw = np.flatnonzero(cor)
        t2sw = bt[i_sw[0]] if len(i_sw) else np.nan
        t2a = np.nan
        for i in range(len(cor) - 2):
            if cor[i] and cor[i + 1] and cor[i + 2]:
                t2a = bt[i]
                break
        rows.append(dict(Subject=subj, Session=sess, session_num=g["session_num"].iat[0],
                         blockNum=blk, trial2sw=t2sw, trial2asymp=t2a))
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------- models
# Model codes; parameter order, bounds and initial distributions follow the code's param_dict.
MODELS = {
    # name: (code, params, bounds)
    "RL4p": (0, ["beta", "a_pos", "a_neg", "st"], [(0, None), (0, 1), (0, 1), (0, None)]),
    "RLCF": (1, ["beta", "a_pos", "a_neg", "st"], [(0, None), (0, 1), (0, 1), (0, None)]),
    "RLFQ3p": (2, ["beta", "a_pos", "a_neg"], [(0, None), (0, 1), (0, 1)]),
    "RLFQ3p_methods": (3, ["beta", "a_pos", "a_neg"], [(0, None), (0, 1), (0, 1)]),
    "PearceHall": (4, ["beta", "a_pos", "a_neg", "st", "psi", "zeta"],
                   [(0, None), (0, 1), (0, 1), (0, None), (0, 1), (0, 1)]),
    "RL_meta": (5, ["beta", "a_pos", "a_neg", "st", "zeta", "alpha_nu", "psi"],
                [(0, None), (0, 1), (0, 1), (0, None), (0, 1), (0, 1), (0, 1)]),
    "BIfp": (6, ["beta", "st", "sw"], [(0, None), (0, None), (0.001, 1)]),
    "BRLfwr": (7, ["beta", "st", "sw", "alpha"], [(0, None), (0, None), (0.001, 1), (0, 1)]),
    "BRLfw": (8, ["beta", "st", "sw", "alpha"], [(0, None), (0, None), (0.001, 1), (0, 1)]),
    "BRLwrp": (9, ["beta", "st", "sw", "wr0", "p_rew", "alpha"],
               [(0, None), (0, None), (0.001, 1), (0, 1), (0, 1), (0, 1)]),
    "RFLR": (10, ["beta", "alpha", "tau"], [(0, None), (None, None), (1e-4, None)]),
}
# BIfp RPE as in the Methods (r - [rho1 b(c) + rho2 (1 - b(c))]); used only for RPEs, the
# choice model is BIfp's (claim, opening comment).
BIFP_METHODS_RPE = 11


def init_params(name, rng):
    """Initial values drawn from the code's param_dict distributions (code)."""
    out = []
    for p in MODELS[name][1]:
        if p == "beta":
            out.append(rng.exponential(1.0))
        elif p == "st":
            out.append(rng.gamma(2, 0.2))
        elif p == "sw":
            out.append(max(rng.uniform(0, 0.05), 0.001))
        elif p in ("wr0", "p_rew"):
            out.append(rng.beta(90, 30))
        elif name == "RFLR" and p == "alpha":
            out.append(rng.normal(0, 1))
        elif p == "tau":
            out.append(max(rng.exponential(1.0), 1e-4))
        else:
            out.append(rng.uniform(0, 1))
    return np.array(out)


@njit(cache=True)
def _bayes(b, p_rew, p_eps, c, r, sw):
    # code, bayesian_base.BayesianModel.bayesian_step
    if c == 1:
        P0, P1 = p_eps, p_rew
    else:
        P0, P1 = p_rew, p_eps
    if r == 0:
        P0, P1 = 1 - P0, 1 - P1
    b = ((1 - sw) * b * P1 + sw * (1 - b) * P0) / (b * P1 + (1 - b) * P0)
    return min(max(b, 1e-15), 1 - 1e-15)


@njit(cache=True)
def _expit(x):
    return 1.0 / (1.0 + np.exp(-x))


@njit(cache=True)
def run_model(code, prm, c, r, trial1, out_p, out_rpe, out_extra):
    """Run a model on choices c (1, 0, -1 miss) and rewards r; trial1 marks session starts.

    Writes P(choice = 1) to out_p, the RPE of the chosen port (r - Q(c)) to out_rpe (nan on misses)
    and returns the negative log likelihood over trials with a choice (code, base.CogModel.fit,
    probabilities clipped to [1e-15, 1 - 1e-15]). Stickiness m is +1 / -1 for the previous choice,
    0 on the first trial of a session and after a miss (code, base.fit_marginal); RFLR keeps its
    own marginal, which is not reset between sessions (code, lr.RFLR.sim).
    """
    N = c.shape[0]
    nll = 0.0
    w = np.zeros(5)
    b = 0.5
    phi = 0.0
    m_rflr = 0.0
    for n in range(N):
        if trial1[n]:
            # session start: b = b0, w = w0 (gam = 1)
            w[:] = 0.0
            if code <= 5:
                b = 1.0
                if code == 4:
                    w[2] = 1.0
                if code == 5:
                    w[4] = prm[2]
            elif code <= 9 or code == 11:
                b = 0.5
                if code == 9:
                    w[0] = prm[3]
                elif code >= 7 and code <= 9:
                    w[0] = 0.75
                w[1] = 1e-4
            phi = 0.0
        # stickiness
        if code == 10:
            m = m_rflr
        else:
            if trial1[n] or c[n - 1] == -1:
                m = 0.0
            elif c[n - 1] == 1:
                m = 1.0
            else:
                m = -1.0
        # action values
        if code <= 5:
            q0, q1 = w[0], w[1]
        elif code == 6:
            q0, q1 = (1 - b) / 2, b / 2
        elif code == 11:
            q0, q1 = (1 - b) * 0.75 + b * 1e-4, (1 - b) * 1e-4 + b * 0.75
        elif code <= 9:
            q0 = (1 - b) * w[0] + b * w[1]
            q1 = (1 - b) * w[1] + b * w[0]
        # choice probability
        if code == 10:
            p = _expit(phi + m * prm[1])
        elif code == 2 or code == 3:
            p = _expit((q1 - q0) * prm[0])
        elif code <= 5:
            p = _expit((q1 - q0) * prm[0] + m * prm[3])
        else:
            p = _expit((q1 - q0) * prm[0] + m * prm[1])
        out_p[n] = p
        cn = c[n]
        if cn == -1:
            out_rpe[n] = np.nan
            if code == 10:
                phi = np.exp(-1 / prm[2]) * phi
                m_rflr = 0.0
            continue
        pc = min(max(p, 1e-15), 1 - 1e-15)
        if cn == 1:
            nll -= np.log(pc)
        else:
            nll -= np.log(1 - pc)
        rn = r[n]
        if code == 10:
            cbar = 2.0 * cn - 1.0
            phi = np.exp(-1 / prm[2]) * phi + cbar * rn * prm[0]
            m_rflr = cbar
            out_rpe[n] = np.nan
            continue
        qc = q1 if cn == 1 else q0
        qu = q0 if cn == 1 else q1
        rpe = rn - qc
        out_rpe[n] = rpe
        out_extra[n] = b
        if code <= 3:
            # code, rl.RL_4p.update_w; RLCF adds the counterfactual update of the other port
            a = prm[1] if rpe >= 0 else prm[2]
            w[cn] += a * rpe
            if code == 1:
                rcf = (1 - rn) - qu
                a2 = prm[1] if rcf >= 0 else prm[2]
                w[1 - cn] += a2 * rcf
            if code == 2:
                # code, rl.RL_Forgetting3p: zeta = 1 - (a_pos + a_neg) / 2
                w[1 - cn] *= (1 - prm[1] / 2 - prm[2] / 2)
            elif code == 3:
                # Methods, Eq for RLFQ3p: zeta = (a_pos + a_neg) / 2
                w[1 - cn] *= (prm[1] + prm[2]) / 2
        elif code == 4:
            # code, meta_rl.Pearce_Hall.update_w
            a = w[2] * (prm[1] if rpe >= 0 else prm[2])
            w[cn] += a * rpe
            w[1 - cn] = w[1 - cn] * prm[5]
            an = prm[4] * (abs(rpe) - w[2]) + w[2]
            w[2] = max(0.0, an)
        elif code == 5:
            # code, meta_rl.RL_Grossman.update_w
            a = prm[1] if rpe >= 0 else w[4]
            w[cn] += a * rpe
            w[1 - cn] = max(w[1 - cn] * prm[4], 1e-15)
            omega = w[2]
            nu = abs(rpe) - omega
            omega = omega + prm[5] * nu
            w[2] = omega
            w[3] = nu
            if rpe < 0:
                an = w[4] + prm[6] * ((nu + prm[2]) - w[4])
                w[4] = max(0.0, an)
        else:
            # Bayesian models: code, bimodel.*.update_w then update_b
            if code >= 7 and code <= 9:
                alpha = prm[5] if code == 9 else prm[3]
                dw = b if cn == 1 else 1 - b
                w[0] += alpha * rpe * dw
                if code == 8:
                    w[1] += alpha * rpe * (1 - dw)
            p_rew = prm[4] if code == 9 else 0.75
            b = _bayes(b, p_rew, 1e-4, cn, rn, prm[2])
    return nll


def model_arrays(df):
    c = df["Decision"].values.astype(np.int64)
    r = np.nan_to_num(df["Reward"].values.astype(float)).astype(np.int64)
    t1 = (df["Session"].values != np.roll(df["Session"].values, 1))
    t1[0] = True
    return c, r, t1


def model_nll(name, prm, c, r, t1, rpe_code=None):
    N = len(c)
    p, rpe, ex = np.zeros(N), np.zeros(N), np.zeros(N)
    code = MODELS[name][0] if rpe_code is None else rpe_code
    nll = run_model(code, np.asarray(prm, float), c, r, t1, p, rpe, ex)
    return nll, p, rpe


def fit_model(name, df, seed=230):
    """Maximum likelihood fit of one model to one subject's trials (code, base.CogModel.fit):
    L-BFGS-B, the code's bounds, tol 1e-6, one start drawn from the code's distributions.
    Returns the parameters, nll, AIC = 2k + 2 nll and BIC = k ln(N trials) + 2 nll."""
    code, pnames, bounds = MODELS[name]
    c, r, t1 = model_arrays(df)
    rng = np.random.default_rng(seed)
    x0 = init_params(name, rng)
    N = len(c)
    p, rpe, ex = np.zeros(N), np.zeros(N), np.zeros(N)

    def f(x):
        return run_model(code, x, c, r, t1, p, rpe, ex)

    res = scipy.optimize.minimize(f, x0, method="L-BFGS-B", bounds=bounds, tol=1e-6)
    k = len(pnames)
    out = dict(zip(pnames, res.x))
    out.update(model=name, nll=res.fun, aic=2 * k + 2 * res.fun,
               bic=k * np.log(N) + 2 * res.fun, k=k, success=bool(res.success), n=N)
    return out


def model_latents(name, prm, df):
    """P(right), RPE and belief of a fitted model run on the mouse's own choices and rewards."""
    c, r, t1 = model_arrays(df)
    N = len(c)
    p, rpe, ex = np.zeros(N), np.zeros(N), np.zeros(N)
    run_model(MODELS[name][0], np.asarray(prm, float), c, r, t1, p, rpe, ex)
    return p, rpe


def bifp_methods_rpe(prm, df):
    """BIfp RPE under the Methods' definition (claim opening comment, BIfp pseudo-RPE)."""
    c, r, t1 = model_arrays(df)
    N = len(c)
    p, rpe, ex = np.zeros(N), np.zeros(N), np.zeros(N)
    run_model(BIFP_METHODS_RPE, np.asarray(prm, float), c, r, t1, p, rpe, ex)
    return rpe


# ----------------------------------------------------------------------------- simulation

@njit(cache=True)
def simulate(code, prm, n_trial, n_session, blk_lo, blk_hi, p_cor,
             emu_c, emu_r, emu_target, emu_t1, mode):
    """mode 0: generate fresh sessions; mode 1: emulate on given sessions (code, emulate:
    the model chooses; when it agrees with the mouse it gets the mouse's outcome, otherwise the
    outcome is drawn from the port's reward probability).
    Returns choices, rewards, targets, block trials, session-start flags and P(right)."""
    if mode == 0:
        N = n_trial * n_session
    else:
        N = emu_c.shape[0]
    C = np.zeros(N, np.int64)
    R = np.zeros(N, np.int64)
    T = np.zeros(N, np.int64)
    BT = np.zeros(N, np.int64)
    T1 = np.zeros(N, np.bool_)
    P = np.zeros(N)
    w = np.zeros(5)
    b = 0.5
    phi = 0.0
    m_rflr = 0.0
    c_prev = -1
    tgt = 0
    blen = 0
    nrew = 0
    bt = 0
    for n in range(N):
        if mode == 0:
            first = (n % n_trial) == 0
        else:
            first = emu_t1[n]
        T1[n] = first
        if first:
            w[:] = 0.0
            if code <= 5:
                b = 1.0
                if code == 4:
                    w[2] = 1.0
                if code == 5:
                    w[4] = prm[2]
            else:
                b = 0.5
                if code == 9:
                    w[0] = prm[3]
                elif code >= 7 and code <= 9:
                    w[0] = 0.75
                w[1] = 1e-4
            phi = 0.0
            c_prev = -1
            if mode == 0:
                tgt = np.random.randint(2)
                blen = np.random.randint(blk_lo, blk_hi + 1)
                nrew = 0
                bt = 0
                # code: generate resets the marginal at each session; RFLR's generate too
                m_rflr = 0.0
        if mode == 0:
            T[n] = tgt
            BT[n] = bt
        else:
            T[n] = emu_target[n]
        if code == 10:
            m = m_rflr
        else:
            if c_prev == -1:
                m = 0.0
            elif c_prev == 1:
                m = 1.0
            else:
                m = -1.0
        if code <= 5:
            q0, q1 = w[0], w[1]
        elif code == 6:
            q0, q1 = (1 - b) / 2, b / 2
        else:
            q0 = (1 - b) * w[0] + b * w[1]
            q1 = (1 - b) * w[1] + b * w[0]
        if code == 10:
            p = _expit(phi + m * prm[1])
        elif code == 2 or code == 3:
            p = _expit((q1 - q0) * prm[0])
        elif code <= 5:
            p = _expit((q1 - q0) * prm[0] + m * prm[3])
        else:
            p = _expit((q1 - q0) * prm[0] + m * prm[1])
        P[n] = p
        cn = 1 if np.random.random() <= p else 0
        # outcome
        if mode == 0:
            rn = 1 if (cn == tgt and np.random.random() < p_cor) else 0
            bt += 1
            if rn == 1:
                nrew += 1
                if nrew == blen:
                    blen = np.random.randint(blk_lo, blk_hi + 1)
                    bt = 0
                    tgt = 1 - tgt
                    nrew = 0
        else:
            if cn == emu_c[n]:
                rn = emu_r[n]
            else:
                rn = 1 if (cn == emu_target[n] and np.random.random() <= p_cor) else 0
        C[n] = cn
        R[n] = rn
        c_prev = cn
        if code == 10:
            cbar = 2.0 * cn - 1.0
            phi = np.exp(-1 / prm[2]) * phi + cbar * rn * prm[0]
            m_rflr = cbar
            continue
        qc = q1 if cn == 1 else q0
        qu = q0 if cn == 1 else q1
        rpe = rn - qc
        if code <= 3:
            a = prm[1] if rpe >= 0 else prm[2]
            w[cn] += a * rpe
            if code == 1:
                rcf = (1 - rn) - qu
                a2 = prm[1] if rcf >= 0 else prm[2]
                w[1 - cn] += a2 * rcf
            if code == 2:
                w[1 - cn] *= (1 - prm[1] / 2 - prm[2] / 2)
            elif code == 3:
                w[1 - cn] *= (prm[1] + prm[2]) / 2
        elif code == 4:
            a = w[2] * (prm[1] if rpe >= 0 else prm[2])
            w[cn] += a * rpe
            w[1 - cn] = w[1 - cn] * prm[5]
            an = prm[4] * (abs(rpe) - w[2]) + w[2]
            w[2] = max(0.0, an)
        elif code == 5:
            a = prm[1] if rpe >= 0 else w[4]
            w[cn] += a * rpe
            w[1 - cn] = max(w[1 - cn] * prm[4], 1e-15)
            omega = w[2]
            nu = abs(rpe) - omega
            omega = omega + prm[5] * nu
            w[2] = omega
            w[3] = nu
            if rpe < 0:
                an = w[4] + prm[6] * ((nu + prm[2]) - w[4])
                w[4] = max(0.0, an)
        else:
            if code >= 7 and code <= 9:
                alpha = prm[5] if code == 9 else prm[3]
                dw = b if cn == 1 else 1 - b
                w[0] += alpha * rpe * dw
                if code == 8:
                    w[1] += alpha * rpe * (1 - dw)
            p_rew = prm[4] if code == 9 else 0.75
            b = _bayes(b, p_rew, 1e-4, cn, rn, prm[2])
    return C, R, T, BT, T1, P


def sim_frame(C, R, T, BT, T1, ident="SIM"):
    sess = np.cumsum(T1)
    trial = np.zeros(len(C), int)
    for s in np.unique(sess):
        idx = np.flatnonzero(sess == s)
        trial[idx] = np.arange(1, len(idx) + 1)
    return pd.DataFrame({"ID": ident, "Subject": ident, "Session": [f"{ident}_{s:03d}" for s in sess],
                         "Trial": trial, "Decision": C, "Reward": R, "Target": T, "blockTrial": BT})


# ----------------------------------------------------------------------------- photometry

def airpls(x, lam=5e4, porder=1, itermax=50):
    """Adaptive iteratively reweighted penalized least squares baseline (Zhang et al. 2010), as
    in the photometry procedure the paper cites (Methods, Fiber Photometry, ref 70, Martianova et
    al. 2019, whose code uses lambda = 5e4, porder = 1, itermax = 50)."""
    m = x.shape[0]
    D = scipy.sparse.eye(m, format="csc")
    for _ in range(porder):
        D = D[1:] - D[:-1]
    H = lam * (D.T @ D)
    w = np.ones(m)
    z = x
    for i in range(1, itermax + 1):
        W = scipy.sparse.diags(w, 0, shape=(m, m))
        z = scipy.sparse.linalg.spsolve((W + H).tocsc(), w * x)
        d = x - z
        dssn = np.abs(d[d < 0].sum())
        if dssn < 0.001 * np.abs(x).sum() or i == itermax:
            break
        w[d >= 0] = 0
        w[d < 0] = np.exp(i * np.abs(d[d < 0]) / dssn)
        w[0] = np.exp(i * (d[d < 0]).max() / dssn)
        w[-1] = w[0]
    return z


def continuous_segment(t, max_gap=1.0):
    """Index range of the longest stretch without a gap above max_gap s (standard: the files
    start with isolated samples, up to 140 s before the recording proper)."""
    gaps = np.flatnonzero(np.diff(t) > max_gap)
    edges = np.concatenate([[0], gaps + 1, [len(t)]])
    k = np.argmax(np.diff(edges))
    return edges[k], edges[k + 1]


def preprocess(fp, regression="huber"):
    """Z(DA) on the 470 nm timestamps (Methods, Fiber Photometry): airPLS trend removed from each
    channel, a robust linear regression of 415 nm onto 470 nm (assumption: Huber's T, the default
    robust estimator of statsmodels, which the paper names among its packages; the loss is not
    given), the fitted 415 nm signal subtracted from 470 nm, then z-scored over the session.
    With regression="lasso" the Martianova et al. 2019 procedure is used instead (each channel
    z-scored, then a positive Lasso with alpha 1e-4), as a variant.
    Returns t, Z, and the detrended 470 and rescaled 415 (for the AUC check)."""
    import statsmodels.api as sm
    i0, i1 = continuous_segment(fp["t470"])
    t = fp["t470"][i0:i1]
    f470 = fp["f470"][i0:i1]
    j0, j1 = continuous_segment(fp["t415"])
    f415 = np.interp(t, fp["t415"][j0:j1], fp["f415"][j0:j1])
    s = f470 - airpls(f470)
    ref = f415 - airpls(f415)
    if regression == "huber":
        X = sm.add_constant(ref)
        fit = sm.RLM(s, X, M=sm.robust.norms.HuberT()).fit()
        ref_fit = X @ fit.params
        dl = s - ref_fit
        z = (dl - dl.mean()) / dl.std()
    else:
        from sklearn.linear_model import Lasso
        zs = (s - s.mean()) / s.std()
        zr = (ref - ref.mean()) / ref.std()
        lin = Lasso(alpha=1e-4, precompute=True, max_iter=1000, positive=True,
                    random_state=9999, selection="random").fit(zr.reshape(-1, 1), zs)
        ref_fit = lin.predict(zr.reshape(-1, 1))
        z = zs - ref_fit
        z = (z - z.mean()) / z.std()
    return t, z, s, ref_fit


def roc_auc(sig, ref):
    """ROC AUC separating 470 nm samples from rescaled 415 nm samples (claim, opening comment)."""
    from sklearn.metrics import roc_auc_score
    y = np.r_[np.ones(len(sig)), np.zeros(len(ref))]
    return roc_auc_score(y, np.r_[sig, ref])


DT = 0.05  # interpolation grid step, s (standard: near the 20 Hz sampling)


def outcome_aligned(t, z, t_out, t_max=6.0):
    """De-based Z(DA) after outcome on a 0.05 s grid from 0 to t_max (Methods, Neural data
    analysis: interpolated around event times, minus the value at outcome)."""
    grid = np.arange(0, t_max + DT / 2, DT)
    tt = t_out[:, None] + grid[None, :]
    y = np.interp(tt.ravel(), t, z, left=np.nan, right=np.nan).reshape(tt.shape)
    return grid, y - y[:, :1]


def da_measures(grid, y, rewarded):
    """DA-PT: max of de-based Z(DA) in 0 to 1 s after outcome on rewarded trials, min on
    unrewarded (claim, opening comment; Fig 4B legend). Also the 0 to 1 s mean (claim reading)."""
    sel = (grid > 0) & (grid <= 1.0 + 1e-9)
    w = y[:, sel]
    pt = np.where(rewarded == 1, np.nanmax(w, axis=1), np.nanmin(w, axis=1))
    mean = np.nanmean(y[:, (grid >= 0) & (grid <= 1.0 + 1e-9)], axis=1)
    bad = np.isnan(w).any(axis=1)
    pt[bad] = np.nan
    mean[bad] = np.nan
    return pt, mean


# ----------------------------------------------------------------------------- statistics

def bootstrap_ci(x, rng, n=2000, stat=np.mean):
    x = np.asarray(x)
    x = x[~np.isnan(x)]
    bs = np.array([stat(rng.choice(x, len(x))) for _ in range(n)])
    return np.percentile(bs, [2.5, 97.5])


def holm(p):
    from statsmodels.stats.multitest import multipletests
    return multipletests(p, method="holm")[1]


# ----------------------------------------------------------------------------- trial measures

def history_counts(d, lags=4):
    """R_chosen and R_unchosen: rewarded trials among t-1..t-lags at the port chosen at t and at
    the other port (claim fig4i-lmer-switch; Methods, Linear mixed effects modeling, 4 lags).
    hist_ok marks trials whose previous lags trials are in the same session."""
    c = d["Decision"].values
    r = np.nan_to_num(d["Reward"].values.astype(float))
    s = d["Session"].values
    Rc = np.zeros(len(d))
    Ru = np.zeros(len(d))
    ok = np.ones(len(d), bool)
    for k in range(1, lags + 1):
        cs = np.roll(c, k)
        rs = np.roll(r, k)
        same = np.roll(s, k) == s
        same[:k] = False
        ok &= same
        Rc += (cs == c) & (rs == 1) & same
        Ru += (cs == 1 - c) & (cs >= 0) & (rs == 1) & same
    return Rc, Ru, ok


def cleaned(n, so_lat=1.0):
    """Cleaned trials (Methods, Neural data analysis, paragraph 2): center_dur <= 0.8 s,
    port_dur <= 6 s, MVMT <= 3 s, SO_lat <= so_lat (readings 1 s and 6 s, claim), a choice, and
    no missing neural or behavioural entry."""
    c = n[(n["center_dur"] <= 0.8) & (n["port_dur"] <= 6) & (n["MVMT"] <= 3)
          & (n["SO_lat"] <= so_lat) & n["valid"]]
    return c.dropna(subset=["DA_PT", "Reward", "MVMT", "center_dur", "port_dur"])


def three_trial_history(d):
    """Three-trial history of trial t (claim, opening comment): t-3 is A/a (rewarded or not);
    t-2 and t-1 are A/a when at the port of t-3 and B/b otherwise. Defined when t-3..t-1 are in
    the session and have a choice. Returns the label (or None) and whether t switched from t-1."""
    c = d["Decision"].values
    r = np.nan_to_num(d["Reward"].values.astype(float))
    s = d["Session"].values
    lab = np.array([None] * len(d), dtype=object)
    for i in range(3, len(d)):
        if not (s[i - 3] == s[i]) or min(c[i - 3], c[i - 2], c[i - 1]) < 0:
            continue
        base = c[i - 3]
        out = "A" if r[i - 3] == 1 else "a"
        for j in (i - 2, i - 1):
            same = c[j] == base
            ch = ("A" if same else "B") if r[j] == 1 else ("a" if same else "b")
            out += ch
        lab[i] = out
    return lab


def llk_cv(X, y, tr, te):
    """Gaussian test log-likelihood of an OLS fitted on tr, with the training residual variance
    (claim fig4f-bayesian-rpe-fit)."""
    b, *_ = np.linalg.lstsq(X[tr], y[tr], rcond=None)
    s2 = np.mean((y[tr] - X[tr] @ b) ** 2)
    e = y[te] - X[te] @ b
    return -0.5 * np.sum(np.log(2 * np.pi * s2) + e ** 2 / s2), b


def rpe_design(c, rpe):
    """Design of the Methods' regression (Neural data analysis): outcome_DA_PT ~ rpe:rpe_pos +
    rpe:rpe_neg + port_dur:rpe_pos + port_dur:rpe_neg + ego_action + session_num + log__MVMT +
    log__center_dur, with an intercept (statsmodels formulas add one)."""
    pos = (rpe >= 0).astype(float)
    neg = 1 - pos
    return np.column_stack([np.ones(len(c)), rpe * pos, rpe * neg, c["port_dur"] * pos,
                            c["port_dur"] * neg, c["ipsi"].astype(float), c["session_num"],
                            np.log(c["MVMT"]), np.log(c["center_dur"])])


# ----------------------------------------------------------------------------- simulations

@njit(cache=True)
def nb_seed(s):
    np.random.seed(s)


EMPTY_I = np.zeros(1, np.int64)
EMPTY_B = np.zeros(1, np.bool_)


def generate_frame(name, prm, n_trial, n_session, blocks, seed, ident="SIM"):
    """Fresh sessions from a model (code, generate): blocks = (lo, hi) rewards per block."""
    nb_seed(seed)
    out = simulate(MODELS[name][0], np.asarray(prm, float), n_trial, n_session, blocks[0],
                   blocks[1], 0.75, EMPTY_I, EMPTY_I, EMPTY_I, EMPTY_B, 0)
    return sim_frame(*out[:5], ident=ident), out[5]


def emulate_frame(name, prm, df, seed):
    """The model chooses on a mouse's sessions (code, emulate)."""
    nb_seed(seed)
    c, r, t1 = model_arrays(df)
    out = simulate(MODELS[name][0], np.asarray(prm, float), 0, 0, 0, 0, 0.75, c, r,
                   df["Target"].values.astype(np.int64), t1, 1)
    return out


def _idjob(args):
    sim, prm, n_trial, blocks, seed, fit_models = args
    df, _ = generate_frame(sim, prm, n_trial, 1, blocks, seed)
    res = []
    for fm in fit_models:
        f = fit_model(fm, df, seed=seed)
        f["sim"] = sim
        f["rep"] = seed
        f["true"] = list(prm)
        res.append(f)
    return res


def identification(fits, models, n_rep, n_trial, blocks, seed0, processes=4):
    """Model identification and parameter recovery (Methods, Model identification; S2 Fig
    legend; code, utils_test.test_modelgen_recover_mp): parameters drawn uniformly between the
    minimum and maximum fitted over the mice, one session of n_trial trials simulated, every
    model fitted to it."""
    import multiprocessing as mp
    rng = np.random.default_rng(seed0)
    jobs = []
    for si, sim in enumerate(models):
        F = fits[fits["model"] == sim]
        for k in range(n_rep):
            prm = [rng.uniform(F[p].min(), F[p].max()) for p in MODELS[sim][1]]
            jobs.append((sim, prm, n_trial, blocks, seed0 * 100000 + si * 10000 + k, models))
    with mp.get_context("fork").Pool(processes) as pool:
        out = pool.map(_idjob, jobs, chunksize=20)
    return pd.DataFrame([r for o in out for r in o])


def fit_model_multistart(name, df, n_starts=10, seed=230):
    """The fit of fit_model repeated from n_starts starts (seeds seed .. seed + n_starts - 1),
    keeping the lowest nll; a check of the code's single start (standard choice), not used for
    the main results. Also returns the spread of the nll over the starts."""
    runs = [fit_model(name, df, seed=seed + k) for k in range(n_starts)]
    best = min(runs, key=lambda r: r["nll"])
    best = dict(best)
    best["nll_worst"] = max(r["nll"] for r in runs)
    best["n_starts"] = n_starts
    return best


def refit_recovery(R, model, n_trial, blocks, n_starts=10):
    """Parameter recovery of one model refitted from n_starts starts: each simulated session of
    an identification run (R, from identification) is regenerated from its seed and true
    parameters and fitted with its own model (check of the single start)."""
    rows = []
    for r in R[(R["sim"] == model) & (R["model"] == model)].itertuples():
        df, _ = generate_frame(model, r.true, n_trial, 1, blocks, int(r.rep))
        f = fit_model_multistart(model, df, n_starts, seed=int(r.rep))
        f["sim"] = model
        f["rep"] = r.rep
        f["true"] = list(r.true)
        rows.append(f)
    return pd.DataFrame(rows)


def session_bootstrap_dllk(C, models, n_boot, seed, ref="RL4p", y="DA_PT"):
    """Delta llk_CV against ref with the sessions as the resampled unit (a check of the
    bootstrap over repeated splits, which are not independent samples): in each bootstrap
    sample every animal's sessions are drawn with replacement, its trials split once 70/30 at
    random, and the per-animal Delta averaged over animals. C needs the columns of rpe_design
    and rpe_<model>."""
    rng = np.random.default_rng(seed)
    yy = C[y].values
    subj, sess = C["Subject"].values, C["Session"].values
    X = {m: rpe_design(C, C["rpe_" + m].values) for m in set(models) | {ref}}
    by = {s: [np.flatnonzero((subj == s) & (sess == se)) for se in np.unique(sess[subj == s])]
          for s in np.unique(subj)}
    out = np.zeros((n_boot, len(models)))
    for b in range(n_boot):
        acc = np.zeros(len(models))
        for s, ses in by.items():
            idx = np.concatenate([ses[i] for i in rng.integers(0, len(ses), len(ses))])
            perm = rng.permutation(len(idx))
            k = int(round(0.7 * len(idx)))
            tr, te = idx[perm[:k]], idx[perm[k:]]
            l0 = llk_cv(X[ref], yy, tr, te)[0]
            acc += [llk_cv(X[m], yy, tr, te)[0] - l0 for m in models]
        out[b] = acc / len(by)
    return pd.DataFrame(out, columns=list(models))
