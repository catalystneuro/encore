"""Loading and measures for Hulsey et al. (2024) on dandiset 000678.

Hulsey, Zumwalt, Mazzucato, McCormick & Jaramillo (2024), "Decision-making dynamics are
predicted by arousal and uninstructed movements", Cell Reports 43(1), 113709.

Where each parameter comes from:

- Trial inputs and choices: the paper's code, uobrainflex at commit ef48985 (the claims file,
  M1): ``loadbehavior.get_stim_vals`` for the stimulus value, and
  ``flex_hmm.format_choice_behavior_hmm`` for the choice (left, right, none) and the removal of
  distractor trials.
- Measures at stimulus onset: ``loadbehavior.read_behavior_measures`` and
  ``fetch_trial_beh_measures`` (claims file, M4; STAR Methods, "Pupillometry, face motion energy
  and locomotion"): each series is put on a 1 ms grid at the rounded sample times, linearly
  interpolated over gaps of up to 100 samples, filtered with a second-order Savitzky-Golay filter
  of 201 samples (face, locomotion) or 501 samples (pupil) with the code's mirrored padding; face
  motion energy is shifted to a minimum of 0 and divided by its maximum, pupil divided by its
  maximum, locomotion kept raw and sign-flipped when its median is negative. The value of a trial
  is the grid sample at round(stimulus_time / 1 ms). The 10-trial variability is
  pandas ``rolling(10).std()`` over the session's target trials.
- Evoked pupil response: FigureS1.py (claims file, figs1-iti-independence): from the pupil trace
  at stimulus onset (the code's trace starts 999 samples before onset, so its sample 1000 is
  onset + 1 ms) over 2500 samples, the larger in size of the largest rise and the largest fall.
- Session inclusion: STAR Methods, "Training and inclusion criteria" (claims file,
  cohort-inclusion).
- GLM-HMM: ``fit_glmhmm`` reimplements the expectation-maximisation of the paper's ssm fork
  (``hulsey2023/ssm_changes``) for the input-driven categorical observations: weights of shape
  (K, C-1, M) with the last category ("no response") as reference, random normal initial
  weights, transitions initialised at 0.95 I + 0.05 U(0, 1) normalised, uniform initial state
  distribution, M-step of the weights by damped Newton steps on the expected log joint (computed from the expected counts of each choice at each distinct input) with the
  Gaussian prior of standard deviation ``prior_sigma`` (1000 for MLE, 2 for MAP: ssm uses
  ``prior_sigma ** 2`` as the variance), "standard" transitions (expected counts) or "sticky"
  transitions with Dirichlet alpha 2 and kappa 0 (expected counts + alpha - 1), and stopping
  when the log joint (log likelihood plus log prior, as ssm computes it) changes by less than
  1e-4 or after 1000 iterations (2_n_states.py, 3_generate_hmms.py). A test log likelihood per
  trial is ssm's ``log_probability``, which adds the log prior.
"""

from concurrent.futures import ProcessPoolExecutor
import json
import math
import urllib.request

import h5py
import numpy as np
import pandas as pd
import remfile
from numba import njit
from scipy.signal import oaconvolve
import hashlib

DANDISET = "000678"
VERSION = "0.231004.2146"  # the version the paper cites (Key resources table)
API = "https://api.dandiarchive.org/api"

MEASURES = ["post_hoc_pupil_diameter", "face_energy", "running_speed"]
# Savitzky-Golay windows in 1 ms samples, normalisation and zeroing (loadbehavior.read_behavior_measures)
FILT = {"face_energy": 201, "running_speed": 201, "post_hoc_pupil_diameter": 501}
NORM = {"face_energy": True, "running_speed": False, "post_hoc_pupil_diameter": True}
ZERO = {"face_energy": True, "running_speed": False, "post_hoc_pupil_diameter": False}
EVOKED_SAMPLES = 2500  # FigureS1.py evoked_time_lim


def _get_json(url):
    with urllib.request.urlopen(url) as r:
        return json.load(r)


def list_assets(version=VERSION):
    """All assets of the pinned version, as a DataFrame with path, size, asset_id, subject."""
    url = f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=1000"
    rows = []
    while url:
        page = _get_json(url)
        rows += page["results"]
        url = page["next"]
    df = pd.DataFrame(rows)[["path", "size", "asset_id"]]
    df["subject"] = df["path"].str.split("/").str[0].str.replace("sub-", "")
    return df.sort_values("path").reset_index(drop=True)


def version_metadata(version=VERSION):
    return _get_json(f"{API}/dandisets/{DANDISET}/versions/{version}/")


def s3_url(asset_id):
    """The asset's S3 address, from its metadata (contentUrl)."""
    meta = _get_json(f"{API}/assets/{asset_id}/")
    return next(u for u in meta["contentUrl"] if "s3" in u)


def _maps(trials_group):
    """Code maps stored in the column descriptions ('... MAP:{...}'), as the code reads them."""
    maps = {}
    for key in trials_group.attrs["colnames"]:
        desc = trials_group[key].attrs.get("description", "")
        if isinstance(desc, bytes):
            desc = desc.decode()
        if "{" in desc:
            maps[key] = eval(desc[desc.find("{"):])
    return maps


def _savgol_code(y, window, order=2):
    """loadbehavior.savitzky_golay: convolution with mirrored-difference padding at the ends."""
    half = (window - 1) // 2
    b = np.array([[k ** i for i in range(order + 1)] for k in range(-half, half + 1)], float)
    m = np.linalg.pinv(b)[0]
    first = y[0] - np.abs(y[1:half + 1][::-1] - y[0])
    last = y[-1] + np.abs(y[-half - 1:-1][::-1] - y[-1])
    z = np.concatenate((first, y, last))
    # np.convolve(m[::-1], z, "valid") computed by overlap-add; a NaN anywhere in the window
    # makes the output NaN, as np.convolve does
    bad = np.isnan(z)
    out = oaconvolve(np.where(bad, 0.0, z), m[::-1], mode="valid")
    out[oaconvolve(bad.astype(float), np.ones(window), mode="valid") > 0.5] = np.nan
    return out


def _to_grid(ts, data, n):
    """Samples at round(t / 1 ms), linear interpolation, at most 100 consecutive filled samples
    (pandas interpolate(limit=100), forward only)."""
    grid = np.full(n, np.nan)
    idx = np.round(ts / 0.001).astype(int)
    keep = idx < n
    grid[idx[keep]] = data[: len(idx)][keep]
    valid = np.flatnonzero(~np.isnan(grid))
    if len(valid) < 2:
        return grid
    out = np.interp(np.arange(n), valid, grid[valid])
    # samples before the first valid one stay NaN; in gaps, only the first 100 are filled
    out[: valid[0]] = np.nan
    gaps = np.diff(valid) - 1
    for g in np.flatnonzero(gaps > 100):
        out[valid[g] + 101: valid[g + 1]] = np.nan
    out[valid[-1] + 1:] = np.nan
    return out


def load_session(asset_id, path):
    """One session: its target trials with inputs, choices and measures, plus session facts."""
    f = h5py.File(remfile.File(s3_url(asset_id)), "r")
    meta = dict(f["general/metadata"].attrs)
    tg = f["intervals/trials"]
    maps = _maps(tg)
    cols = [c for c in tg.attrs["colnames"]]
    tr = pd.DataFrame({c: tg[c][:] for c in cols})
    acq = f["acquisition"]
    series = {}
    for k in MEASURES:
        if k in acq:
            series[k] = (acq[k]["timestamps"][:], acq[k]["data"][:])
    n_rew = {k: (acq[k]["data"].shape[0] if k in acq else 0) for k in ["reward_left", "reward_right"]}
    subj = f["general/subject/subject_id"][()].decode()
    # fingerprints to find recordings deposited twice
    fp_face = hashlib.md5(series["face_energy"][1].tobytes()).hexdigest() if "face_energy" in series else ""
    fp_trials = hashlib.md5(tr[["stimulus_time", "outcome"]].values.tobytes()).hexdigest()
    start = f["session_start_time"][()].decode()
    f.close()

    # stimulus values (loadbehavior.get_stim_vals)
    a_dir = tr["auditory_stim_id"].map({maps["auditory_stim_id"]["left"]: -1.0,
                                        maps["auditory_stim_id"]["right"]: 1.0}).astype(float)
    a_val = tr["auditory_stim_difficulty"].values
    aud = a_dir.values * (a_val - (1 - a_val) / 2)
    v_dir = tr["visual_stim_id"].map({maps["visual_stim_id"]["left"]: -1.0,
                                      maps["visual_stim_id"]["right"]: 1.0}).astype(float)
    v_val = tr["visual_stim_difficulty"].values
    v_id = np.zeros(len(tr))
    v_id[v_val == 1] = 0.8
    v_id[v_val == 2] = 0.6
    v_id[v_val == 0] = 1
    vis = v_dir.values * v_id
    tr["aud_stim"], tr["vis_stim"] = aud, vis
    tr["stage"] = meta.get("training_stage")
    distractor = maps["stimulus_type"]["distractor"]
    all_trials = tr.copy()

    # target trials and choices (flex_hmm.format_choice_behavior_hmm)
    t = tr[tr["stimulus_type"] != distractor].copy()
    modality = t["target_modality"].iloc[0]
    t["inpt"] = t["aud_stim"] if modality == maps["target_modality"]["auditory"] else t["vis_stim"]
    hit, err, nores = (maps["outcome"][k] for k in ["hit", "miss", "incorrect_reject"])
    left, right = maps["target_port"]["left"], maps["target_port"]["right"]
    ch = np.full(len(t), 2)
    o, p = t["outcome"].values, t["target_port"].values
    ch[(o == hit) & (p == left)] = 0
    ch[(o == err) & (p == right)] = 0
    ch[(o == hit) & (p == right)] = 1
    ch[(o == err) & (p == left)] = 1
    ch[o == nores] = 2
    t["hmm_choice"] = ch

    # measures on the 1 ms grid (loadbehavior.read_behavior_measures, fetch_trial_beh_measures)
    n = int(max(np.round(ts[-1] / 0.001) for ts, _ in series.values())) if series else 0
    samp = np.round(t["stimulus_time"].values / 0.001).astype(int)
    for k in MEASURES:
        if k not in series:
            t[k] = np.nan
            continue
        g = _savgol_code(_to_grid(*series[k], n), FILT[k])
        if NORM[k] and np.isfinite(g).any():
            if ZERO[k]:
                g = g - np.nanmin(g)
            g = g / np.nanmax(g)
        if k == "running_speed" and np.nanmedian(g) < 0:
            g = -g
        ok = samp <= n - 1
        vals = np.full(len(t), np.nan)
        vals[ok] = g[samp[ok]]
        t[k] = vals
        # clock check: change of the measure over 1.5 s from stimulus onset, and the same change
        # 4 s later (between trials)
        for name, off in (("d0", 0), ("d4", 4000)):
            a_, b_ = samp + off, samp + off + 1500
            okd = b_ <= n - 1
            dv = np.full(len(t), np.nan)
            dv[okd] = g[b_[okd]] - g[a_[okd]]
            t[f"{k}_{name}"] = dv
        if k == "post_hoc_pupil_diameter":
            ev = np.full(len(t), np.nan)
            for i, s in enumerate(samp):
                seg = g[s + 1: s + 1 + EVOKED_SAMPLES]
                if len(seg) == EVOKED_SAMPLES:
                    up, down = np.max(seg - seg[0]), np.min(seg - seg[0])
                    ev[i] = up if abs(up) >= abs(down) else down
            t["evoked_pupil"] = ev
    t["post_hoc_pupil_std10"] = t["post_hoc_pupil_diameter"].rolling(10).std()
    t["face_std_10"] = t["face_energy"].rolling(10).std()
    t["running_std10"] = t["running_speed"].rolling(10).std()
    t["trial_in_session"] = np.arange(len(t))
    info = dict(path=path, asset_id=asset_id, subject=subj, session_start=start,
                stage=meta.get("training_stage"), session_type=meta.get("session_type"),
                rig=meta.get("rig"), behavior_version=meta.get("behavior_version"),
                modality=int(modality), n_trials_file=len(all_trials), n_target=len(t),
                n_distractor=int((all_trials["stimulus_type"] == distractor).sum()),
                reward_left=n_rew["reward_left"], reward_right=n_rew["reward_right"],
                has_pupil=("post_hoc_pupil_diameter" in series),
                pupil_n=len(series["post_hoc_pupil_diameter"][0]) if "post_hoc_pupil_diameter" in series else 0,
                face_n=len(series["face_energy"][0]) if "face_energy" in series else 0,
                run_n=len(series["running_speed"][0]) if "running_speed" in series else 0,
                run_raw_median=float(np.nanmedian(series["running_speed"][1])) if "running_speed" in series else np.nan,
                run_raw_p99=float(np.nanpercentile(series["running_speed"][1], 99)) if "running_speed" in series else np.nan,
                pupil_raw_median=float(np.nanmedian(series["post_hoc_pupil_diameter"][1])) if np.isfinite(series.get("post_hoc_pupil_diameter", (0, [np.nan]))[1]).any() else np.nan,
                face_rate=1 / np.median(np.diff(series["face_energy"][0])) if "face_energy" in series else np.nan,
                run_rate=1 / np.median(np.diff(series["running_speed"][0])) if "running_speed" in series else np.nan,
                last_sample_s=n / 1000, fp_face=fp_face, fp_trials=fp_trials)
    all_trials["path"] = path
    t["path"] = path
    t["subject"] = subj
    return t, all_trials, info


def load_all(assets, workers=16):
    """Stream every session in parallel. Returns (target trials, all trials, sessions)."""
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        with ProcessPoolExecutor(workers) as ex:
            res = list(ex.map(load_session, assets["asset_id"], assets["path"]))
    trials = pd.concat([r[0] for r in res], ignore_index=True)
    alltr = pd.concat([r[1] for r in res], ignore_index=True)
    sessions = pd.DataFrame([r[2] for r in res])
    return trials, alltr, sessions


# ---------------------------------------------------------------------------------------------
# GLM-HMM (reimplementation of the ssm fork's input-driven categorical HMM, fit by EM)
# ---------------------------------------------------------------------------------------------

@njit(cache=True)
def _forward_backward(log_pi0, P, loglik):
    """Scaled forward-backward for one sequence. Returns (gamma, xi_sum, marginal log lik)."""
    T, K = loglik.shape
    alpha = np.zeros((T, K))
    c = np.zeros(T)
    m = np.zeros(T)
    lik = np.zeros((T, K))
    for t in range(T):
        mx = loglik[t, 0]
        for k in range(1, K):
            if loglik[t, k] > mx:
                mx = loglik[t, k]
        m[t] = mx
        for k in range(K):
            lik[t, k] = math.exp(loglik[t, k] - mx)
    pi0 = np.exp(log_pi0 - np.max(log_pi0))
    pi0 = pi0 / pi0.sum()
    s = 0.0
    for k in range(K):
        alpha[0, k] = pi0[k] * lik[0, k]
        s += alpha[0, k]
    c[0] = s
    for k in range(K):
        alpha[0, k] /= s
    for t in range(1, T):
        s = 0.0
        for j in range(K):
            a = 0.0
            for i in range(K):
                a += alpha[t - 1, i] * P[i, j]
            alpha[t, j] = a * lik[t, j]
            s += alpha[t, j]
        c[t] = s
        for j in range(K):
            alpha[t, j] /= s
    beta = np.ones((T, K))
    xi = np.zeros((K, K))
    for t in range(T - 2, -1, -1):
        for i in range(K):
            b = 0.0
            for j in range(K):
                b += P[i, j] * lik[t + 1, j] * beta[t + 1, j]
            beta[t, i] = b / c[t + 1]
        for i in range(K):
            for j in range(K):
                xi[i, j] += alpha[t, i] * P[i, j] * lik[t + 1, j] * beta[t + 1, j] / c[t + 1]
    gamma = alpha * beta
    ll = 0.0
    for t in range(T):
        ll += math.log(c[t]) + m[t]
    return gamma, xi, ll


@njit(cache=True)
def _filter(log_pi0, P, loglik):
    """Filtered state probabilities p(z_t | y_1..t) for one sequence."""
    T, K = loglik.shape
    alpha = np.zeros((T, K))
    pi0 = np.exp(log_pi0 - np.max(log_pi0))
    pi0 = pi0 / pi0.sum()
    for t in range(T):
        lik = np.exp(loglik[t] - np.max(loglik[t]))
        if t == 0:
            a = pi0 * lik
        else:
            a = (alpha[t - 1] @ P) * lik
        alpha[t] = a / a.sum()
    return alpha


def _logits(W, X):
    """log p(y = c | z = k, x) for all trials: array (T, K, C). W is (K, C-1, M)."""
    eta = np.einsum("kcm,tm->tkc", W, X)
    eta = np.concatenate([eta, np.zeros(eta.shape[:2] + (1,))], axis=2)
    return eta - np.logaddexp.reduce(eta, axis=2, keepdims=True)


def _unique_inputs(Xs, ys):
    X = np.concatenate(Xs)
    U, ux = np.unique(X, axis=0, return_inverse=True)
    return U, ux.ravel(), np.concatenate(ys).astype(int).ravel()


def _log_prior_obs(W, sigma):
    K, C1, M = W.shape
    return float(-0.5 * M * np.log(2 * np.pi) * K * C1 - M * np.log(sigma) * K * C1
                 - 0.5 * np.sum(W ** 2) / sigma ** 2)


def _log_prior_trans(P, sticky, alpha=2.0):
    return float(np.sum((alpha - 1) * np.log(P))) if sticky else 0.0


@njit(cache=True)
def _table(W, U):
    """log p(c | k, U[u]) as (n_u, K, C), the last class the reference."""
    K, C1, M = W.shape
    n_u = U.shape[0]
    out = np.zeros((n_u, K, C1 + 1))
    for u in range(n_u):
        for k in range(K):
            mx = 0.0
            for c in range(C1):
                e = 0.0
                for d in range(M):
                    e += W[k, c, d] * U[u, d]
                out[u, k, c] = e
                if e > mx:
                    mx = e
            s = math.exp(-mx)
            for c in range(C1):
                s += math.exp(out[u, k, c] - mx)
            lse = mx + math.log(s)
            for c in range(C1 + 1):
                out[u, k, c] -= lse
    return out


@njit(cache=True)
def _obj_k(Wk, U, cnt, sigma):
    """Expected complete-data log likelihood of one state's weights plus its log prior."""
    tab = _table(Wk, U)
    f = 0.0
    for u in range(U.shape[0]):
        for c in range(cnt.shape[1]):
            if cnt[u, c] > 0:
                f += cnt[u, c] * tab[u, 0, c]
    f -= 0.5 * np.sum(Wk ** 2) / sigma ** 2
    return f


@njit(cache=True)
def _em(W, P, log_pi0, U, ux, y, starts, sigma, sticky, num_iters, tol):
    """EM as ssm's HMM.fit(method="em"): E-step, then M-step of the initial distribution,
    transitions and weights; stops when the log joint changes by less than tol."""
    K, C1, M = W.shape
    C = C1 + 1
    n_u = U.shape[0]
    n_seq = len(starts) - 1
    lps = np.zeros(num_iters)
    it_done = 0
    for it in range(num_iters):
        tab = _table(W, U)
        counts = np.zeros((n_u, K, C))
        xi_tot = np.zeros((K, K))
        pi_acc = np.zeros(K)
        ll_tot = 0.0
        for s in range(n_seq):
            a, b = starts[s], starts[s + 1]
            T = b - a
            lik = np.zeros((T, K))
            mloc = np.zeros(T)
            for t in range(T):
                mx = -1e300
                for k in range(K):
                    v = tab[ux[a + t], k, y[a + t]]
                    if v > mx:
                        mx = v
                mloc[t] = mx
                for k in range(K):
                    lik[t, k] = math.exp(tab[ux[a + t], k, y[a + t]] - mx)
            pi0 = np.exp(log_pi0 - np.max(log_pi0))
            pi0 /= pi0.sum()
            alpha = np.zeros((T, K))
            cs = np.zeros(T)
            ssum = 0.0
            for k in range(K):
                alpha[0, k] = pi0[k] * lik[0, k]
                ssum += alpha[0, k]
            cs[0] = ssum
            for k in range(K):
                alpha[0, k] /= ssum
            for t in range(1, T):
                ssum = 0.0
                for j in range(K):
                    acc = 0.0
                    for i in range(K):
                        acc += alpha[t - 1, i] * P[i, j]
                    alpha[t, j] = acc * lik[t, j]
                    ssum += alpha[t, j]
                cs[t] = ssum
                for j in range(K):
                    alpha[t, j] /= ssum
            beta = np.ones(K)
            nb = np.zeros(K)
            # gamma at T-1
            for k in range(K):
                g = alpha[T - 1, k]
                counts[ux[a + T - 1], k, y[a + T - 1]] += g
            if T == 1:
                for k in range(K):
                    pi_acc[k] += alpha[0, k]
            v = np.zeros(K)
            for t in range(T - 2, -1, -1):
                for j in range(K):
                    v[j] = lik[t + 1, j] * beta[j] / cs[t + 1]
                for i in range(K):
                    acc = 0.0
                    for j in range(K):
                        q = P[i, j] * v[j]
                        xi_tot[i, j] += alpha[t, i] * q
                        acc += q
                    nb[i] = acc
                for k in range(K):
                    beta[k] = nb[k]
                    g = alpha[t, k] * beta[k]
                    counts[ux[a + t], k, y[a + t]] += g
                    if t == 0:
                        pi_acc[k] += g
            for t in range(T):
                ll_tot += math.log(cs[t]) + mloc[t]
        # log prior (ssm: Gaussian on each weight vector; Dirichlet on sticky transitions)
        lp = 0.0
        for k in range(K):
            for c in range(C1):
                sq = 0.0
                for d in range(M):
                    sq += W[k, c, d] ** 2
                lp += -0.5 * M * math.log(2 * math.pi) - M * math.log(sigma) - 0.5 * sq / sigma ** 2
        if sticky:
            for i in range(K):
                for j in range(K):
                    lp += math.log(P[i, j])
        lps[it] = ll_tot + lp
        it_done = it + 1
        if it > 0 and abs(lps[it] - lps[it - 1]) < tol:
            break
        # M-step
        pi_acc += 1e-8
        log_pi0 = np.log(pi_acc / pi_acc.sum())
        add = 1.0 if sticky else 1e-32
        for i in range(K):
            rs = 0.0
            for j in range(K):
                rs += xi_tot[i, j] + add
            for j in range(K):
                P[i, j] = (xi_tot[i, j] + add) / rs
        nprm = C1 * M
        for k in range(K):
            for newton in range(50):
                tabk = _table(W[k:k + 1], U)
                grad = np.zeros(nprm)
                H = np.zeros((nprm, nprm))
                for u in range(n_u):
                    tot = 0.0
                    for c in range(C):
                        tot += counts[u, k, c]
                    for c1 in range(C1):
                        p1 = math.exp(tabk[u, 0, c1])
                        r = counts[u, k, c1] - p1 * tot
                        for d in range(M):
                            grad[c1 * M + d] += r * U[u, d]
                        for c2 in range(C1):
                            p2 = math.exp(tabk[u, 0, c2])
                            wab = tot * p1 * ((1.0 if c1 == c2 else 0.0) - p2)
                            for d1 in range(M):
                                for d2 in range(M):
                                    H[c1 * M + d1, c2 * M + d2] -= wab * U[u, d1] * U[u, d2]
                for c1 in range(C1):
                    for d in range(M):
                        grad[c1 * M + d] -= W[k, c1, d] / sigma ** 2
                        H[c1 * M + d, c1 * M + d] -= 1.0 / sigma ** 2
                step = np.linalg.solve(H, grad)
                # Newton step, halved until the objective does not decrease (damped Newton)
                Wk = W[k:k + 1].copy()
                f0 = _obj_k(Wk, U, counts[:, k, :], sigma)
                scale = 1.0
                for _ in range(60):
                    Wn = Wk.copy()
                    for c1 in range(C1):
                        for d in range(M):
                            Wn[0, c1, d] -= scale * step[c1 * M + d]
                    if _obj_k(Wn, U, counts[:, k, :], sigma) >= f0 - 1e-12:
                        break
                    scale *= 0.5
                W[k] = Wn[0]
                mstep = scale * np.max(np.abs(step))
                if mstep < 1e-10:
                    break
    return W, P, log_pi0, lps[:it_done]



class GLMHMM:
    """K-state GLM-HMM with categorical (C classes) emissions and inputs of dimension M."""

    def __init__(self, K, M=2, C=3, prior_sigma=1000.0, sticky=False, rng=None):
        rng = np.random.default_rng(rng)
        self.K, self.M, self.C = K, M, C
        self.prior_sigma, self.sticky = prior_sigma, sticky
        self.W = rng.standard_normal((K, C - 1, M))
        P = 0.95 * np.eye(K) + 0.05 * rng.random((K, K))
        self.P = P / P.sum(1, keepdims=True)
        self.log_pi0 = -np.log(K) * np.ones(K)

    def log_prior(self):
        return _log_prior_obs(self.W, self.prior_sigma) + _log_prior_trans(self.P, self.sticky)

    def _estep(self, Xs, ys, cache=None):
        if cache is None:
            cache = _unique_inputs(Xs, ys)
        U, ux, y = cache
        ll_all = _logits(self.W, U)[ux, :, y]
        out, start = [], 0
        for x in Xs:
            out.append(_forward_backward(self.log_pi0, self.P, ll_all[start:start + len(x)]))
            start += len(x)
        return out

    def log_likelihood(self, Xs, ys):
        U, ux, y = _unique_inputs(Xs, ys)
        ll_all = _logits(self.W, U)[ux, :, y]
        tot, start = 0.0, 0
        for x in Xs:
            tot += _forward_backward(self.log_pi0, self.P, ll_all[start:start + len(x)])[2]
            start += len(x)
        return tot

    def log_probability(self, Xs, ys):
        """ssm's HMM.log_probability: log likelihood plus log prior."""
        return self.log_likelihood(Xs, ys) + self.log_prior()

    def fit(self, Xs, ys, num_iters=1000, tolerance=1e-4):
        """EM (ssm's HMM.fit with method="em"); returns the log joint at each iteration."""
        U, ux, y = _unique_inputs(Xs, ys)
        starts = np.r_[0, np.cumsum([len(x) for x in Xs])].astype(np.int64)
        W, P, lp0, lps = _em(self.W.copy(), self.P.copy(), self.log_pi0.copy(), U.astype(float),
                             ux.astype(np.int64), y.astype(np.int64), starts, float(self.prior_sigma),
                             bool(self.sticky), num_iters, tolerance)
        self.W, self.P, self.log_pi0 = W, P, lp0
        self.n_iter = len(lps)
        self.lps = list(lps)
        return self.lps

    def posteriors(self, Xs, ys):
        return [e[0] for e in self._estep(Xs, ys)]

    def permute(self, perm):
        perm = np.asarray(perm)
        self.W = self.W[perm]
        self.P = self.P[np.ix_(perm, perm)]
        self.log_pi0 = self.log_pi0[perm]


def fit_one(args):
    """Fit one GLM-HMM; args = (K, Xs_train, ys_train, Xs_test, ys_test, map, seed).
    Returns (model, train log prob per trial, test log prob per trial or nan)."""
    K, Xtr, ytr, Xte, yte, use_map, seed = args
    m = GLMHMM(K, prior_sigma=2.0 if use_map else 1000.0, sticky=use_map, rng=seed)
    lps = m.fit(Xtr, ytr)
    ntr = sum(len(x) for x in Xtr)
    test = np.nan
    if Xte is not None:
        test = m.log_probability(Xte, yte) / sum(len(x) for x in Xte)
    return m, lps[-1] / ntr, test


def plateau(ll, threshold=0.001):
    """3_generate_hmms.plateu: among state counts whose step raises the test log likelihood by
    more than the threshold, the one with the highest log likelihood. Returns the number of states."""
    ind = np.where(np.diff(ll) > threshold)[0]
    if len(ind) == 0:
        return 1
    return int(ind[np.argmax(ll[ind + 1])] + 1) + 1


def sequences(trials):
    """Per session (in session order): inputs [stimulus value, 1] and choices (0 left, 1 right,
    2 none), as flex_hmm.get_inpts_from_hmm_trials and get_true_choices_from_hmm_trials."""
    Xs, ys = [], []
    for _, g in trials.groupby("path", sort=True):
        Xs.append(np.c_[g["inpt"].values, np.ones(len(g))])
        ys.append(g["hmm_choice"].values.astype(int))
    return Xs, ys


def run_parallel(func, tasks, workers=None):
    import os
    workers = workers or os.cpu_count()
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(func, tasks, chunksize=1))


def cv_tasks(Xs, ys, n_init, seed, max_states=7, n_folds=5):
    """2_n_states.py: KFold over sessions (shuffled), states 1 to max_states, n_init random
    initialisations, MLE and MAP fits. Returns task list and their (fold, K, init, map) keys."""
    from sklearn.model_selection import KFold
    rng = np.random.default_rng(seed)
    kf = KFold(n_splits=n_folds, shuffle=True, random_state=int(rng.integers(2**31)))
    tasks, keys = [], []
    for f, (tr_i, te_i) in enumerate(kf.split(np.arange(len(Xs)))):
        Xtr, ytr = [Xs[i] for i in tr_i], [ys[i] for i in tr_i]
        Xte, yte = [Xs[i] for i in te_i], [ys[i] for i in te_i]
        for K in range(1, max_states + 1):
            for z in range(n_init):
                for use_map in (False, True):
                    tasks.append((K, Xtr, ytr, Xte, yte, use_map, int(rng.integers(2**31))))
                    keys.append((f, K, z, use_map))
    return tasks, keys


def cv_test_ll(task):
    """Only the per-trial test log probability of one fit (keeps results small across processes)."""
    m, tr_ll, te_ll = fit_one(task)
    return tr_ll, te_ll, m.n_iter




# ---------------------------------------------------------------------------------------------
# State selection, final model, state labels (2_n_states.py, 3_generate_hmms.py, flex_hmm,
# Figure2.py)
# ---------------------------------------------------------------------------------------------

def select_states(test_ll):
    """test_ll: (init, K, fold) per-trial test log probabilities. As 3_generate_hmms.py: mean over
    folds, best initialisation, then the plateau rule."""
    curve = np.nanmax(np.nanmean(test_ll, axis=2), axis=0)
    return plateau(curve), curve


def final_tasks(Xs, ys, K, n_init, seed):
    rng = np.random.default_rng(seed)
    return [(K, Xs, ys, None, None, False, int(rng.integers(2**31))) for _ in range(n_init)]


def posterior_states(model, trials, occ_thresh=0.8):
    """flex_hmm.get_posterior_probs: posterior of each state per trial, and the state when its
    posterior is at least occ_thresh (NaN, indeterminate, otherwise)."""
    Xs, ys = sequences(trials)
    post = np.concatenate(model.posteriors(Xs, ys))
    order = trials.sort_values(["path", "trial_in_session"]).index
    out = pd.DataFrame(index=order)
    st = np.argmax(post, axis=1).astype(float)
    st[np.max(post, axis=1) < occ_thresh] = np.nan
    out["hmm_state"] = st
    for k in range(post.shape[1]):
        out[f"state_{k + 1}_prob"] = post[:, k]
    return out.loc[trials.index]


def psychos(trials, states):
    """flex_hmm.get_psychos: P(choice | state, input) for discrete states (state, choice, input)."""
    inp = np.unique(trials["inpt"])
    K = int(np.nanmax(states)) + 1
    ps = np.full((K, 3, len(inp)), np.nan)
    for k in range(K):
        sel = states == k
        for j, x in enumerate(inp):
            n = np.sum(sel & (trials["inpt"].values == x))
            if n > 0:
                for c in range(3):
                    ps[k, c, j] = np.sum(sel & (trials["inpt"].values == x) & (trials["hmm_choice"].values == c)) / n
    return ps, inp


def permutation_optimal_disengaged(ps):
    """flex_hmm.permute_hmm: state nearest a perfect psychometric first, nearest all no-response
    second (sum of absolute differences over inputs without missing values), others after."""
    perfect = np.zeros((2, ps.shape[1], ps.shape[2]))
    perfect[0, 0, : int(ps.shape[2] / 2)] = 1
    perfect[0, 1, int(ps.shape[2] / 2):] = 1
    perfect[1, 2, :] = 1
    miss = np.unique(np.where(ps != ps)[2])
    p1, p2 = np.delete(perfect, miss, axis=2), np.delete(ps, miss, axis=2)
    sim = np.array([[np.sum(np.abs(s - t)) for t in p1] for s in p2])
    perm = np.nanargmin(sim, axis=0)
    if len(perm) < ps.shape[0]:
        perm = np.append(perm, np.delete(np.arange(ps.shape[0]), perm))
    if len(np.unique(perm)) != len(perm):
        best = np.nanargmin(sim[:, 0])
        perm = np.concatenate(([best], np.delete(np.arange(sim.shape[0]), best)))
    return perm


STATE_NAMES = ["optimal", "disengaged", "bias left", "avoid right", "bias right", "avoid left", "no trials"]


def sort_templates():
    """Figure2.py sort_psychos: (template, choice, 6 inputs)."""
    s = np.zeros([6, 3, 6])
    s[0, 0, :3] = 1
    s[0, 1, 3:] = 1
    s[1, 2, :] = 1
    s[2, 0, :] = 1
    s[3, 0, :3] = 1
    s[3, 2, 3:] = 1
    s[4, 1, :] = 1
    s[5, 1, 3:] = 1
    s[5, 2, :3] = 1
    return s


def state_types(ps, fixed_first_two=True):
    """Figure2.py: each state's nearest template (nansum of absolute differences), with the
    code's loop resolving states assigned the same template. ps must have 6 inputs.

    With fixed_first_two (claims file, M3), states 0 and 1 are optimal and disengaged as
    flex_hmm.permute_hmm ordered them, and only the others are matched, to the four sub-optimal
    templates. A state with no trial in a discrete state has an all-missing psychometric, which
    the code's nansum would score 0 against every template; such a state is labelled -1 (no
    trials) and left out of the matching (a guard added here)."""
    if ps.shape[2] == 8:
        bad = np.unique(np.where(ps != ps)[-1])
        ps = np.delete(ps, bad, axis=2)
    if ps.shape[2] == 8:
        ps = np.delete(ps, [1, 6], axis=2)
    tmpl = sort_templates()
    sim = np.array([[np.nansum(np.abs(s - t)) for t in tmpl] for s in ps])
    empty = np.array([np.all(np.isnan(s)) for s in ps])
    sim[empty] = np.inf
    lab = np.full(len(ps), -1)
    if fixed_first_two:
        lab[0], lab[1] = 0, 1
        rows = [i for i in range(2, len(ps)) if not empty[i]]
        allowed = [2, 3, 4, 5]
    else:
        rows = [i for i in range(len(ps)) if not empty[i]]
        allowed = list(range(6))
    sub = sim[np.ix_(rows, allowed)]
    if len(rows):
        cur = np.argmin(sub, axis=1)
        guard = 0
        while len(np.unique(cur)) != len(cur) and guard < 100:
            vals, counts = np.unique(cur, return_counts=True)
            for v in vals[counts > 1]:
                idx = np.where(cur == v)[0]
                worst = idx[np.argmax(sub[idx, v])]
                cur[worst] = np.argsort(sub[worst])[1]
            guard += 1
        lab[rows] = np.array(allowed)[cur]
    return lab, sim


def dwell_table(states):
    """flex_hmm.get_dwell_times for one session, line by line. A dwell is recorded as the run
    length plus one for every epoch ended inside the loop, and the final record uses the state of
    the second-to-last trial; last_trial is the index of the first trial after the epoch.
    'run' is the run length itself."""
    ts = np.asarray(states, float)
    rows = []
    n, state_start = 0, 0
    this_state = np.nan
    while n < len(ts) - 1:
        this_state, next_state = ts[n], ts[n + 1]
        if not (this_state == next_state):
            state_end = n + 1
            if not np.isnan(this_state):
                rows.append((this_state, state_end - state_start + 1, state_start, state_end, state_end - state_start))
            state_start = n + 1
        n += 1
    state_end = n
    if not np.isnan(this_state):
        rows.append((this_state, state_end - state_start, state_start, state_end, state_end - state_start + 1))
    return pd.DataFrame(rows, columns=["state", "dwell", "first_trial", "last_trial", "run"])


def stratified_kfold_random_order(class_index, n_folds, rng):
    """6_predictive_accuracy.stratified_kFold_random_order: StratifiedKFold on the session index
    (contiguous blocks of each session), with the order of the folds permuted per session."""
    from sklearn.model_selection import StratifiedKFold
    classes = np.unique(class_index)
    fold_index = np.array([rng.permutation(n_folds) for _ in classes])
    skf = StratifiedKFold(n_splits=n_folds)
    tr_idx, te_idx = [], []
    for a, b in skf.split(np.arange(len(class_index)), class_index):
        tr_idx.append(a)
        te_idx.append(b)
    new_tr, new_te = [], []
    for i in range(n_folds):
        t1, t2 = [], []
        for j, c in enumerate(classes):
            this = np.where(class_index == c)[0]
            a, b = tr_idx[fold_index[j, i]], te_idx[fold_index[j, i]]
            t1.append(a[np.isin(a, this)])
            t2.append(b[np.isin(b, this)])
        new_tr.append(np.concatenate(t1))
        new_te.append(np.concatenate(t2))
    return new_tr, new_te


def fit_map_one(args):
    """flex_hmm.choice_hmm_fit (MAP: prior_sigma 2, sticky transitions alpha 2, kappa 0) on one
    concatenated sequence; returns the model and its test log probability per trial."""
    K, Xtr, ytr, Xte, yte, seed = args
    m = GLMHMM(K, prior_sigma=2.0, sticky=True, rng=seed)
    m.fit([Xtr], [ytr])
    return m, m.log_probability([Xte], [yte]) / len(Xte)


def predict_choices(m, X, y):
    """6_predictive_accuracy.py: the first trial's state is the most likely initial state; later,
    the most likely next state from the transition matrix given the most likely filtered state of
    the preceding test trials; the choice is the most likely choice of that state's GLM."""
    U, ux, yy = _unique_inputs([X], [y])
    ll = _logits(m.W, U)[ux, :, yy]
    filt = _filter(m.log_pi0, m.P, ll)
    states = np.empty(len(X), int)
    states[0] = np.argmax(m.log_pi0)
    states[1:] = np.argmax(m.P[np.argmax(filt[:-1], axis=1)], axis=1)
    lg = _logits(m.W, X)  # (T, K, C)
    return np.argmax(lg[np.arange(len(X)), states], axis=1)


# ---------------------------------------------------------------------------------------------
# State decoding (5_decoding.py)
# ---------------------------------------------------------------------------------------------

DECODE_MEASURES = ['post_hoc_pupil_diameter', 'post_hoc_pupil_std10', 'face_energy', 'face_std_10',
                   'running_speed', 'running_std10', 'movement', 'movement_std']
# columns shuffled in the training set, by condition (5_decoding.py shuffle_schedule, by index),
# plus "M only" (keep the movement index value and SD, shuffle all others; Figure 5C legend)
SHUFFLE = {0: [6, 7], 1: [2, 3, 4, 5], 2: [2, 3, 4, 5, 6, 7], 3: [0, 1, 4, 5, 6, 7], 4: [0, 1, 2, 3, 6, 7],
           5: [1, 2, 3, 4, 5], 6: [0, 1, 6, 7], 7: [2, 3, 6, 7], 8: [4, 5, 6, 7], 13: [],
           14: [0, 1, 2, 3, 4, 5, 6, 7], "M only": [0, 1, 2, 3, 4, 5]}


def svm_task(args):
    """Fit an RBF SVC (scikit-learn defaults) on the training fold with the condition's columns
    permuted across training trials (one permutation per run, shared by the columns, as the code)
    and return the test accuracy."""
    from sklearn import svm
    Xtr, ytr, Xte, yte, cols, seed = args
    Xtr = Xtr.copy()
    if cols:
        perm = np.random.default_rng(seed).permutation(len(Xtr))
        Xtr[:, cols] = Xtr[perm][:, cols]
    return svm.SVC(kernel="rbf").fit(Xtr, ytr).score(Xte, yte)
