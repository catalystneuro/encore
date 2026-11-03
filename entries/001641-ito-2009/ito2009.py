"""Loading and measures for dandiset 001641 (Ito & Doya 2009, J Neurosci 29:9861).

Where each parameter comes from is said where it is defined:
- "claims": the claims file, claims/001641/10.1523-jneurosci.6157-08.2009.yaml (which cites the paper);
- "paper": a passage of the paper taken by the author (protocol, author step 1.6), cited;
- "assumption": a choice the paper leaves open, with the reason;
- "standard": a detail that cannot change a result.
"""

from __future__ import annotations

import concurrent.futures as cf
import os

import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET = "001641"
VERSION = "0.260922.0719"
API = "https://api.dandiarchive.org/api"

# Trial `result` codes. The file says only "Refer to the Discription in 'Result' column", and no
# such description is in the file. Their meaning is inferred from the other columns and the event
# series in the notebook's data check (state, action, reward, and which tone ended the trial).
RESULT_SUCCESS = 1      # tone A rewarded choice, or tone B success
RESULT_ERROR = 2        # error tone, no L/R choice recorded
RESULT_NOREWARD = 3     # tone A choice, not rewarded
RESULT_OTHER = 5        # rare; tone A, no action, no reward (see data check)


def list_assets(version: str = VERSION) -> pd.DataFrame:
    """Every asset of the pinned version: path, size, asset id."""
    url = f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=200"
    rows = []
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        d = r.json()
        rows += [dict(path=a["path"], size=a["size"], asset_id=a["asset_id"]) for a in d["results"]]
        url = d.get("next")
    df = pd.DataFrame(rows)
    df["subject"] = df.path.str.extract(r"sub-(\d+)/")[0]
    df["session"] = df.path.str.extract(r"ses-([^_]+)_")[0]
    return df.sort_values("path").reset_index(drop=True)


def _s3_url(asset_id: str) -> str:
    r = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60)
    return r.url


def _events(h5, name):
    g = h5["acquisition"][name]
    return np.asarray(g["timestamps"][:], float), np.asarray(g["data"][:], int)


EVENT_SERIES = ["SpSensor C", "SpSensor L", "SpSensor R", "SpTone A", "SpTone B", "SpTone Err",
                "SpTone Rwd", "ViDispenser", "ViTrial Start Tone"]


def load_session(asset_id: str) -> dict:
    """Stream one NWB file and read the trial table, the block table, the units and the event series.

    Read with h5py directly (no pynwb object tree) to keep it fast; the column names are those of
    the NWB tables.
    """
    f = remfile.File(_s3_url(asset_id))
    with h5py.File(f, "r") as h:
        tr = h["intervals"]["trials"]
        trials = pd.DataFrame({c: np.asarray(tr[c][:]) for c in tr.attrs["colnames"]})
        trials["trial_id"] = tr["id"][:]
        bd = h["processing"]["behavior"]["BlockDesign"]
        blocks = pd.DataFrame({c: np.asarray(bd[c][:]) for c in bd.attrs["colnames"]})
        blocks["block_id"] = bd["id"][:]
        dec = lambda a: [x.decode() if isinstance(x, bytes) else str(x) for x in a]
        if "units" in h:
            u = h["units"]
            idx = np.asarray(u["spike_times_index"][:])
            st = np.asarray(u["spike_times"][:])
            starts = np.r_[0, idx[:-1]]
            units = pd.DataFrame(dict(unit_name=dec(u["Unit_Name"][:]), area=dec(u["Area"][:]),
                                      electrode=np.asarray(u["Electrode_ID"][:]),
                                      neuron=np.asarray(u["Neuron_ID"][:])))
            units["spike_times"] = [st[a:b] for a, b in zip(starts, idx)]
        else:  # some files hold no units table
            units = pd.DataFrame(columns=["unit_name", "area", "electrode", "neuron", "spike_times"])
        events = {n: _events(h, n) for n in EVENT_SERIES if n in h["acquisition"]}
        meta = dict(session_id=h["general"]["session_id"][()].decode() if "session_id" in h["general"] else "",
                    subject=h["general"]["subject"]["subject_id"][()].decode())
    return dict(trials=trials, blocks=blocks, units=units, events=events, **meta)


def load_all(assets: pd.DataFrame, workers: int = 8) -> list[dict]:
    """Load every session, in the order of `assets` (sorted by path: subject, then session number)."""
    with cf.ThreadPoolExecutor(workers) as ex:
        out = list(ex.map(load_session, assets.asset_id))
    for s, (_, a) in zip(out, assets.iterrows()):
        s["path"] = a.path
        s["session"] = a.session
        s["subject_file"] = a.subject
    return out


# ---------------------------------------------------------------------------------------------
# Behaviour
# ---------------------------------------------------------------------------------------------

def all_trials(sessions: list[dict]) -> pd.DataFrame:
    """One table of every trial, with the session index, subject and the block's reward rule."""
    out = []
    for i, s in enumerate(sessions):
        t = s["trials"].copy()
        b = s["blocks"].set_index("block_id")
        t["sess"] = i
        t["subject"] = s["subject"]
        t["rule_L"] = t.block.map(b.RewardRule_L)
        t["rule_R"] = t.block.map(b.RewardRule_R)
        t["block_finished"] = t.block.map(b.FinishedBlock)
        out.append(t)
    T = pd.concat(out, ignore_index=True)
    T["choice"] = (T.state == 1) & T.result.isin([RESULT_SUCCESS, RESULT_NOREWARD])
    T["nochoice"] = (T.state == 2) & (T.result == RESULT_SUCCESS)
    T["error"] = ~(T.choice | T.nochoice)
    return T


def choice_sequences(T: pd.DataFrame) -> list[pd.DataFrame]:
    """Per session, the choice trials only (Methods, Model-free behavioral analysis: "no-choice
    trials and error trials were removed and the remaining sequences of choice trials were used"),
    with a = 0 for left, 1 for right, r = 0/1 and e = 2a + (1 - r) coding L1=0, L0=1, R1=2, R0=3."""
    out = []
    for _, g in T[T.choice].groupby("sess", sort=True):
        g = g.sort_values("start_time")
        a = (g.action.values == 2).astype(int)
        r = g.reward.values.astype(int)
        out.append(pd.DataFrame(dict(a=a, r=r, e=2 * a + (1 - r), block=g.block.values,
                                     rule_L=g.rule_L.values, rule_R=g.rule_R.values,
                                     sess=g.sess.values, subject=g.subject.values)))
    return out


EXP = ["L1", "L0", "R1", "R0"]


def history_counts(seqs, d: int, within_block: bool):
    """For every history of d experiences (oldest first), the number of following L and R choices.

    within_block: True for reading O7 (a), histories and the following choice inside one block;
    False for O7 (b), within one session across block borders.
    Returns a dict history-tuple -> list of 0/1 left-choice indicators (with session index)."""
    out: dict = {}
    for k, s in enumerate(seqs):
        e, a, b = s.e.values, s.a.values, s.block.values
        for t in range(d, len(s)):
            if within_block and b[t - d] != b[t]:
                continue
            h = tuple(e[t - d:t])
            out.setdefault(h, []).append((1 - a[t], k))
    return out


def parse(h: str) -> tuple:
    return tuple(EXP.index(x) for x in h.split())


def window_counts(seqs, n: int, within_block: bool):
    """Counts of every sequence of n consecutive experiences (oldest first)."""
    c: dict = {}
    for s in seqs:
        e, b = s.e.values, s.block.values
        for t in range(n, len(s) + 1):
            if within_block and b[t - n] != b[t - 1]:
                continue
            h = tuple(e[t - n:t])
            c[h] = c.get(h, 0) + 1
    return c


# ---------------------------------------------------------------------------------------------
# Models (Methods, Behavioral models). Q update readings O1 (claims file, opening comment):
#   form 0 = O1 (a): chosen Q <- (1 - a1) Q + a1 k1 after reward, (1 - a1) Q - a1 k2 after none;
#   form 1 = O1 (b): chosen Q <- (1 - a1) Q + k1 after reward, (1 - a1) Q - k2 after none;
#   both: unchosen Q <- (1 - a2) Q.
# Choice rule P(L) = 1 / (1 + exp(-(QL - QR))) (supplemental Methods, equation 1); the local
# matching law uses P(L) = QL / (QL + QR) (Methods), with P(L) = 0.5 when QL + QR = 0 (standard
# choice: the ratio is undefined there, and Qi(1) = 0 makes it so on the first trial).
# ---------------------------------------------------------------------------------------------
import numba as nb

PMIN = 1e-12  # floor on a predicted probability before taking its log (standard choice)


@nb.njit(cache=True)
def q_update(qc, qu, r, a1, a2, k1, k2, form):
    """Return the chosen and unchosen action values after one experience."""
    if form == 0:
        qc = (1 - a1) * qc + (a1 * k1 if r == 1 else -a1 * k2)
    else:
        qc = (1 - a1) * qc + (k1 if r == 1 else -k2)
    qu = (1 - a2) * qu
    return qc, qu


@nb.njit(cache=True)
def p_left(ql, qr, ratio):
    if ratio:
        s = ql + qr
        if s == 0.0:
            return 0.5
        p = ql / s
        return min(max(p, 0.0), 1.0)
    return 1.0 / (1.0 + np.exp(-(ql - qr)))


@nb.njit(cache=True)
def q_predict(a, r, a1, a2, k1, k2, q0, form, ratio):
    """P(L) at each trial of one session, from the experiences before it (fixed parameters)."""
    n = a.shape[0]
    out = np.empty(n)
    ql = q0
    qr = q0
    for t in range(n):
        out[t] = p_left(ql, qr, ratio)
        if a[t] == 0:
            ql, qr = q_update(ql, qr, r[t], a1, a2, k1, k2, form)
        else:
            qr, ql = q_update(qr, ql, r[t], a1, a2, k1, k2, form)
    return out


def loglik(pl, a):
    """Per-trial log likelihood of the observed choices (Methods, Parameter fitting)."""
    z = np.where(a == 0, pl, 1 - pl)
    return np.log(np.maximum(z, PMIN))


def norm_lik(logz):
    """Normalized likelihood (reading O2): exp of the mean per-trial log likelihood, the geometric
    mean of the per-trial likelihood; 0.5 at chance and 1 for exact deterministic prediction."""
    return float(np.exp(np.mean(logz)))


# Model definitions: which of (a1, a2, k1, k2) are free. Methods, Behavioral models: standard Q
# has a2 = k2 = 0; F-Q a1 = a2; DF-Q all four; local matching law a1 = a2, k1 = 1, k2 = 0.
def model_params(model: str, x):
    x = list(x)
    if model == "Q":
        return x[0], 0.0, x[1], 0.0
    if model == "FQ":
        return x[0], x[0], x[1], x[2]
    if model == "DFQ":
        return x[0], x[1], x[2], x[3]
    if model == "LM":
        return x[0], x[0], 1.0, 0.0
    raise ValueError(model)


N_FREE = {"Q": 2, "FQ": 3, "DFQ": 4, "LM": 1}
NAMES = {"Q": ["alpha1", "kappa1"], "FQ": ["alpha1", "kappa1", "kappa2"],
         "DFQ": ["alpha1", "alpha2", "kappa1", "kappa2"], "LM": ["alpha1"]}


def predict_sessions(model, x, seqs, form, q0=0.0):
    a1, a2, k1, k2 = model_params(model, x)
    return [q_predict(s.a.values, s.r.values, a1, a2, k1, k2, q0, form, model == "LM") for s in seqs]


# ---------------------------------------------------------------------------------------------
# Markov model (Methods, Markov model): P(a | last d experiences) = (Na + 1) / (NL + NR + 2), counts
# from the training sessions, histories within a session.
# ---------------------------------------------------------------------------------------------

def markov_counts(seqs, d):
    NL = np.zeros(4 ** d)
    NR = np.zeros(4 ** d)
    for s in seqs:
        e, a = s.e.values, s.a.values
        for t in range(d, len(s)):
            k = 0
            for j in range(t - d, t):
                k = 4 * k + e[j]
            if a[t] == 0:
                NL[k] += 1
            else:
                NR[k] += 1
    return NL, NR


def markov_predict(NL, NR, d, seqs):
    """P(L) for each trial; trials t < d have an incomplete history and get NaN (reading O6
    decides what is done with them)."""
    out = []
    p = (NL + 1) / (NL + NR + 2)
    for s in seqs:
        e = s.e.values
        pl = np.full(len(s), np.nan)
        for t in range(d, len(s)):
            k = 0
            for j in range(t - d, t):
                k = 4 * k + e[j]
            pl[t] = p[k]
        out.append(pl)
    return out


# ---------------------------------------------------------------------------------------------
# Particle filter for the time-varying models (Methods, "For the time-varying parameter models";
# supplemental Methods, equations 9 to 16): h = [QL, QR, a1, a2, k1, k2]; 5000 particles; initial
# QL, QR, a1, a2 uniform on [0, 1] and k1, k2 uniform on [0, 4]; prediction P_L(t) is the mean over
# particles of 1/(1 + exp(-(QL - QR))) before e(t) is seen; importance weight P(a(t) | particle);
# resampling (systematic resampling, a standard choice for the offspring numbers N_i the
# supplement describes); then Q updated with the particle's parameters of trial t - 1 (formula A of
# the main text, reading O1) and a's and k's drifted by N(0, sigma_a^2), N(0, sigma_k^2)
# (supplemental equations 14, 15). Drift bounds are reading O5: clip = 0 none, 1 a's clipped to [0, 1].
# kind: 0 standard Q (a2 = k2 = 0), 1 F-Q (a2 = a1), 2 DF-Q.
# The particle filter restarts at the start of each session (initial distributions as above).
# ---------------------------------------------------------------------------------------------
N_PARTICLES = 5000


@nb.njit(cache=True)
def _pf_session(a, r, kind, sa, sk, form, clip, npart, seed, out_pl, out_pred, out_post):
    np.random.seed(seed)
    n = a.shape[0]
    QL = np.random.random(npart)
    QR = np.random.random(npart)
    A1 = np.random.random(npart)
    A2 = np.random.random(npart)
    K1 = 4 * np.random.random(npart)
    K2 = 4 * np.random.random(npart)
    if kind == 0:
        A2[:] = 0.0
        K2[:] = 0.0
    elif kind == 1:
        A2[:] = A1
    pl = np.empty(npart)
    w = np.empty(npart)
    idx = np.empty(npart, np.int64)
    for t in range(n):
        for i in range(npart):
            pl[i] = 1.0 / (1.0 + np.exp(-(QL[i] - QR[i])))
        out_pl[t] = pl.mean()
        out_pred[t, 0] = QL.mean(); out_pred[t, 1] = QR.mean(); out_pred[t, 2] = A1.mean()
        out_pred[t, 3] = A2.mean(); out_pred[t, 4] = K1.mean(); out_pred[t, 5] = K2.mean()
        ws = 0.0
        for i in range(npart):
            w[i] = pl[i] if a[t] == 0 else 1.0 - pl[i]
            ws += w[i]
        for i in range(npart):
            w[i] /= ws
        out_post[t, 0] = (w * QL).sum(); out_post[t, 1] = (w * QR).sum(); out_post[t, 2] = (w * A1).sum()
        out_post[t, 3] = (w * A2).sum(); out_post[t, 4] = (w * K1).sum(); out_post[t, 5] = (w * K2).sum()
        # systematic resampling
        u0 = np.random.random() / npart
        c = w[0]
        j = 0
        for i in range(npart):
            u = u0 + i / npart
            while u > c and j < npart - 1:
                j += 1
                c += w[j]
            idx[i] = j
        QL = QL[idx]; QR = QR[idx]; A1 = A1[idx]; A2 = A2[idx]; K1 = K1[idx]; K2 = K2[idx]
        for i in range(npart):
            if a[t] == 0:
                ql, qr = q_update(QL[i], QR[i], r[t], A1[i], A2[i], K1[i], K2[i], form)
                QL[i] = ql; QR[i] = qr
            else:
                qr, ql = q_update(QR[i], QL[i], r[t], A1[i], A2[i], K1[i], K2[i], form)
                QL[i] = ql; QR[i] = qr
            A1[i] += sa * np.random.standard_normal()
            K1[i] += sk * np.random.standard_normal()
            if kind == 2:
                A2[i] += sa * np.random.standard_normal()
                K2[i] += sk * np.random.standard_normal()
            elif kind == 1:
                K2[i] += sk * np.random.standard_normal()
            if clip == 1:
                A1[i] = min(max(A1[i], 0.0), 1.0)
                A2[i] = min(max(A2[i], 0.0), 1.0)
            if kind == 1:
                A2[i] = A1[i]


@nb.njit(parallel=True, cache=True)
def _pf_all(a, r, offs, kind, sa, sk, form, clip, npart, seeds, out_pl, out_pred, out_post):
    for k in nb.prange(offs.shape[0] - 1):
        s, e = offs[k], offs[k + 1]
        _pf_session(a[s:e], r[s:e], kind, sa, sk, form, clip, npart, seeds[k],
                    out_pl[s:e], out_pred[s:e], out_post[s:e])


KIND = {"Q": 0, "FQ": 1, "DFQ": 2}


def particle_filter(seqs, model, sa, sk, form=0, clip=0, npart=N_PARTICLES, seed=0):
    """Run the filter on each session. Returns per-session lists of P_L, the predictive means of
    h (given e(1:t-1)) and the posterior means (after e(t)), columns QL, QR, a1, a2, k1, k2.
    Each session's random stream is seeded from `seed` and its own index (sess column)."""
    a = np.concatenate([s.a.values for s in seqs]).astype(np.int64)
    r = np.concatenate([s.r.values for s in seqs]).astype(np.int64)
    offs = np.r_[0, np.cumsum([len(s) for s in seqs])].astype(np.int64)
    seeds = np.array([seed * 100003 + int(s.sess.values[0]) for s in seqs], np.int64)
    n = len(a)
    pl = np.empty(n); pred = np.empty((n, 6)); post = np.empty((n, 6))
    _pf_all(a, r, offs, KIND[model], sa, sk, form, clip, npart, seeds, pl, pred, post)
    sp = lambda x: [x[offs[k]:offs[k + 1]] for k in range(len(seqs))]
    return sp(pl), sp(pred), sp(post)


# ---------------------------------------------------------------------------------------------
# Training and test split (reading O3). (a) alternate sessions in recording order over all rats
# (files sorted by subject and session number; even positions train); (b) alternate sessions within
# each rat; (c) a seeded random half (seed 0, a standard choice).
# ---------------------------------------------------------------------------------------------

def splits(seqs) -> dict:
    n = len(seqs)
    subj = np.array([s.subject.values[0] for s in seqs])
    a = np.arange(n) % 2 == 0
    b = np.zeros(n, bool)
    for sb in np.unique(subj):
        ii = np.where(subj == sb)[0]
        b[ii[::2]] = True
    c = np.zeros(n, bool)
    c[np.random.default_rng(0).permutation(n)[: n // 2]] = True
    return {"a": a, "b": b, "c": c}


# ---------------------------------------------------------------------------------------------
# Fitting the constant-parameter models by maximum likelihood on the training sessions (reading O4):
# (b) a continuous optimizer (L-BFGS-B from several starts, a standard choice); (a) the best point
# of a grid on the steps of Table 2 (0.05 for alpha and kappa), searched exhaustively within
# +-3 grid steps of the continuous optimum in every free parameter (an assumption: the likelihood
# is smooth, so the grid optimum lies next to the continuous one; a full grid over four parameters
# would take hours here).
# Bounds: alpha in [0, 1] (rates), kappa1 in [0, 10], kappa2 in [-10, 10] (kappa2 may be negative,
# Methods: "a large negative kappa2").
# ---------------------------------------------------------------------------------------------
from scipy.optimize import minimize
import itertools

BOUNDS = {"Q": [(0, 1), (0, 10)], "FQ": [(0, 1), (0, 10), (-10, 10)],
          "DFQ": [(0, 1), (0, 1), (0, 10), (-10, 10)], "LM": [(0, 1)]}
STARTS = {"Q": [(0.3, 1.0), (0.6, 2.0)], "FQ": [(0.3, 1.0, 0.3), (0.6, 2.0, 1.0)],
          "DFQ": [(0.3, 0.3, 1.0, 0.3), (0.6, 0.4, 2.0, 1.0), (0.55, 0.55, 1.2, 0.5)], "LM": [(0.05,), (0.3,)]}


def total_loglik(model, x, seqs, form, q0=0.0):
    pls = predict_sessions(model, x, seqs, form, q0)
    return float(sum(loglik(p, s.a.values).sum() for p, s in zip(pls, seqs)))


def fit_constant(model, seqs, form, q0=0.0):
    """Return dict(cont=x_continuous, grid=x_grid) maximizing the training likelihood."""
    f = lambda x: -total_loglik(model, x, seqs, form, q0)
    best = None
    starts = list(STARTS[model])
    if model == "DFQ":  # also start from the F-Q optimum, a point of the DF-Q space
        fq = fit_constant("FQ", seqs, form)["cont"]
        starts.append((fq[0], fq[0], fq[1], fq[2]))
    for x0 in starts:
        res = minimize(f, x0, method="L-BFGS-B", bounds=BOUNDS[model])
        if best is None or res.fun < best.fun:
            best = res
    xc = best.x
    step = 0.01 if model == "LM" else 0.05  # Table 2 prints the local matching law's alpha as 0.01
    centre = np.round(xc / step) * step
    axes = []
    for v, (lo, hi) in zip(centre, BOUNDS[model]):
        ax = v + step * np.arange(-3, 4)
        axes.append(np.round(ax[(ax >= lo - 1e-9) & (ax <= hi + 1e-9)], 4))
    gbest, gx = np.inf, None
    for x in itertools.product(*axes):
        v = f(np.array(x))
        if v < gbest:
            gbest, gx = v, np.array(x)
    return dict(cont=xc, grid=gx, ll_cont=-best.fun, ll_grid=-gbest)


def session_normlik(pls, seqs, skip=0):
    """Per-session normalized likelihood, leaving out the first `skip` trials of each session."""
    return np.array([norm_lik(loglik(p[skip:], s.a.values[skip:])) for p, s in zip(pls, seqs)])


def pooled_normlik(pls, seqs, skip=0):
    return norm_lik(np.concatenate([loglik(p[skip:], s.a.values[skip:]) for p, s in zip(pls, seqs)]))


# ---------------------------------------------------------------------------------------------
# Neural analysis
# ---------------------------------------------------------------------------------------------

def outcome_tone_onsets(session: dict, trials: pd.DataFrame) -> np.ndarray:
    """Onset of the reward or no-reward tone of each trial (phase 5 of Fig. 8A): the first onset of
    `SpTone Rwd` (reward tone) or of a short `SpTone Err` tone (the no-reward tone, 500 Hz 250 ms, is
    stored in the `SpTone Err` series; see the data check) within 1 s after L or R entry."""
    ev = session["events"]
    on = []
    for name in ["SpTone Rwd", "SpTone Err"]:
        ts, d = ev[name]
        a, b = ts[d == 1], ts[d == -1]
        m = min(len(a), len(b))
        dur = b[:m] - a[:m]
        keep = dur < 1.5 if name == "SpTone Err" else np.ones(m, bool)  # error tone lasts ~2 s
        on.append(a[:m][keep])
    on = np.sort(np.concatenate(on))
    x = trials.action_on_time.values
    out = np.full(len(x), np.nan)
    ok = ~np.isnan(x)
    k = np.searchsorted(on, x[ok] - 0.01)
    k = np.minimum(k, len(on) - 1)
    d = on[k] - x[ok]
    out[np.where(ok)[0][(d >= -0.01) & (d <= 1.0)]] = on[k][(d >= -0.01) & (d <= 1.0)]
    return out


# Fig. 8A legend (claims file, opening comment): phase 1, 1 s before center-hole entry; phase 2,
# 1 s after cue onset; phase 3, 1 s before center-hole exit; phase 4, 1 s after center-hole exit;
# phase 5, 1 s after reward or no-reward tone onset.
PHASES = {1: ("pokeC_on_time", -1.0), 2: ("tone_on_time", 0.0), 3: ("pokeC_off_time", -1.0),
          4: ("pokeC_off_time", 0.0), 5: ("outcome_tone", 0.0)}


def count_spikes(st: np.ndarray, starts: np.ndarray, width: float) -> np.ndarray:
    """Spikes in [start, start + width) for each start (NaN start gives NaN)."""
    out = np.full(starts.shape, np.nan)
    ok = ~np.isnan(starts)
    s = starts[ok]
    out[ok] = np.searchsorted(st, s + width) - np.searchsorted(st, s)
    return out


def phase_counts(session: dict, trials: pd.DataFrame) -> dict:
    """For each unit of the session, a (n_trials, 5) array of spike counts in phases 1 to 5."""
    t = trials.copy()
    t["outcome_tone"] = outcome_tone_onsets(session, t)
    starts = np.stack([t[c].values + off for c, off in PHASES.values()], axis=1)
    return {i: count_spikes(np.sort(st), starts, 1.0) for i, st in enumerate(session["units"].spike_times)}


from scipy.stats import mannwhitneyu


def mw_p(x, y):
    """Two-sided Mann-Whitney U test (Methods, Comparison of perievent time histograms); scipy's
    default method (exact for small samples without ties, else normal approximation with tie
    and continuity correction, a standard choice). NaN when a group is empty or all values equal."""
    x = np.asarray(x, float); y = np.asarray(y, float)
    x = x[~np.isnan(x)]; y = y[~np.isnan(y)]
    if len(x) == 0 or len(y) == 0:
        return np.nan
    if np.all(np.r_[x, y] == np.r_[x, y][0]):
        return 1.0
    return float(mannwhitneyu(x, y, alternative="two-sided").pvalue)


def mw_indicator_p(k1, n1, k2, n2):
    """Reading O9: two-sided Mann-Whitney U test on per-neuron 0/1 coding indicators of two groups,
    normal approximation with tie correction (no continuity correction)."""
    x = np.r_[np.ones(k1), np.zeros(n1 - k1)]
    y = np.r_[np.ones(k2), np.zeros(n2 - k2)]
    if k1 + k2 == 0 or k1 + k2 == n1 + n2:
        return 1.0
    return float(mannwhitneyu(x, y, alternative="two-sided", method="asymptotic", use_continuity=False).pvalue)


# ---------------------------------------------------------------------------------------------
# Mutual information (Methods, Information analysis): 500 ms windows, step 100 ms; spike count in
# four classes whose borders minimize the variance of the class sizes, found by exhaustive search;
# plug-in estimate minus the first-order bias (Panzeri and Treves 1996); per second (divided by
# 0.5 s); averaged over neurons of a region. Bits (log base 2, a standard choice of unit).
# ---------------------------------------------------------------------------------------------
MI_WIDTH = 0.5
MI_STEP = 0.1
N_CLASSES = 4


@nb.njit(cache=True)
def class_index(counts):
    """Assign each value of `counts` (non-negative integers) to one of 4 classes [N_i, N_i+1) whose
    borders minimize the variance of the class sizes, testing all combinations of borders among
    the distinct values. With fewer than 4 distinct values each value is its own class."""
    vals = np.unique(counts)
    k = vals.shape[0]
    n = counts.shape[0]
    freq = np.zeros(k)
    for i in range(n):
        j = np.searchsorted(vals, counts[i])
        freq[j] += 1
    cls = np.empty(n, np.int64)
    if k <= 4:
        for i in range(n):
            cls[i] = np.searchsorted(vals, counts[i])
        return cls
    cum = np.zeros(k + 1)
    for j in range(k):
        cum[j + 1] = cum[j] + freq[j]
    best = 1e300
    b1 = 1; b2 = 2; b3 = 3
    mean = n / 4.0
    for i1 in range(1, k - 2):
        for i2 in range(i1 + 1, k - 1):
            for i3 in range(i2 + 1, k):
                l0 = cum[i1]; l1 = cum[i2] - cum[i1]; l2 = cum[i3] - cum[i2]; l3 = n - cum[i3]
                v = (l0 - mean) ** 2 + (l1 - mean) ** 2 + (l2 - mean) ** 2 + (l3 - mean) ** 2
                if v < best:
                    best = v; b1 = i1; b2 = i2; b3 = i3
    for i in range(n):
        j = np.searchsorted(vals, counts[i])
        cls[i] = 0 if j < b1 else (1 if j < b2 else (2 if j < b3 else 3))
    return cls


@nb.njit(cache=True)
def mi_bias_corrected(cls, x):
    """Plug-in MI (bits) between class index (0..3) and binary x (0/1), minus the first-order bias
    (R_FX - R_F - R_X + 1) / (2 M ln 2)."""
    M = cls.shape[0]
    m = np.zeros((4, 2))
    for i in range(M):
        m[cls[i], x[i]] += 1
    mf = m.sum(axis=1); mx = m.sum(axis=0)
    I = 0.0
    rfx = 0; rf = 0; rx = 0
    for i in range(4):
        if mf[i] > 0:
            rf += 1
        for j in range(2):
            if m[i, j] > 0:
                rfx += 1
                I += m[i, j] / M * np.log2(m[i, j] * M / (mf[i] * mx[j]))
    for j in range(2):
        if mx[j] > 0:
            rx += 1
    return I - (rfx - rf - rx + 1) / (2.0 * M * np.log(2.0))


@nb.njit(cache=True)
def classes_matrix(C):
    """Class index of every trial in every window; C is (n_trials, n_windows) spike counts."""
    out = np.empty(C.shape, np.int64)
    for w in range(C.shape[1]):
        out[:, w] = class_index(C[:, w])
    return out


@nb.njit(cache=True)
def mi_curve(K, x):
    """MI per second in each window, K (n_trials, n_windows) class indices, x binary per trial."""
    out = np.empty(K.shape[1])
    for w in range(K.shape[1]):
        out[w] = mi_bias_corrected(K[:, w], x) / 0.5
    return out


def window_starts(times, placement):
    """Start of the 500 ms window for each time point (reading O12): 'centre', 'end' (window ends
    at the point) or 'start' (window starts at it)."""
    return times - {"centre": MI_WIDTH / 2, "end": MI_WIDTH, "start": 0.0}[placement]


def window_counts_matrix(st, align, times, placement):
    """(n_trials, n_windows) integer spike counts in 500 ms windows around `align`."""
    w0 = window_starts(times, placement)
    starts = align[:, None] + w0[None, :]
    c = np.searchsorted(st, starts + MI_WIDTH) - np.searchsorted(st, starts)
    return c.astype(np.int64)
