"""Loading and measures for Lesica et al. (2007), Neuron 55:479-491, on DANDI:002028.

Where each parameter comes from is said beside it:
  [claim]   the claims file (claims/lesica-2007.yaml), which cites the paper;
  [paper]   a passage of the paper taken by the author (protocol, author step 1.6), cited;
  [assume]  an assumption about a detail the paper leaves open, with the reason;
  [standard] a standard choice for a detail that cannot change a result.

Data streamed from the archive with remfile and h5py; nothing is written to disk.
"""
import json
import zlib

import h5py
import numpy as np
import remfile
import requests
import scipy.linalg
import scipy.ndimage
import scipy.optimize

DANDISET = "002028"
VERSION = "0.261102.1631"
API = "https://api.dandiarchive.org/api"
PAPER_KEY = "lesica-2007"

# The penetrations the paper's analyses can use. Expt1 holds the 15 min movie, the long white
# noise and the 12 s repeats; Expt2 holds the 15 min movie and the 90 s repeats (24 trials).
# Expt3 and Expt4 hold no 15 min movie at two contrasts (see the notebook's data check).
SESSIONS = {
    "Expt1": ["a11", "a13", "a14", "b11", "b13", "b14"],
    "Expt2": ["a11", "a12", "b11", "c11", "d11", "e21", "f31", "g31"],
}

FRAME_RATE = 59.958  # nominal; each recording's own rate is read from its frame series
BIN = 1.0 / 128  # [paper] "spike times were binned at 128 Hz" (Estimation of Receptive Fields, par. 4)
NLAGS = 12  # [assume] 12 lags of one 16.68 ms frame (200 ms), the frame-rate equivalent of the
#             paper's 24 lags of 8 ms (192 ms); see estimate_rf
WIN = 21  # [paper] "441 spatial points (21 x 21 grid)" (Estimation of Receptive Fields, par. 4)
RIDGE_REL = 10000.0  # [paper + assume] The paper's RLS with initial conditions g = 0 and K0 = D x I converges
#                     to the ridge solution with penalty 1/D (Haykin 2002), computed here in batch. The paper
#                     chose D as "the value of D that produced the RF estimates that provided the most
#                     accurate predictions of responses to natural scene movies" (Estimation of Receptive
#                     Fields, par. 3); the notebook applies the same rule (choose_ridge), which sets this
#                     value. [assume] The penalty is RIDGE_REL times the stimulus variance, the same relative
#                     to the stimulus in every condition. The paper's own value, D = 0.001 on its stimulus
#                     scale ("zero mean and possible values between -106 and 106", gray levels about the
#                     mean of 125), is a penalty of 1000 in gray levels; it is in the selection grid and is
#                     run as a variant (PENALTIES), where it gives RFs at the noise level (see the notebook)
RIDGE = 1000.0  # [paper] the literal penalty 1/D, in gray levels squared; a variant
PENALTIES = {"main": ("rel", None), "rel1000": ("rel", 1000.0), "paper": ("abs", RIDGE)}
#   [assume] the variants computed in the same pass: "main" RIDGE_REL x variance; "rel1000" 1000 x
#   variance, the lowest of the first round's grid and below the mean eigenvalue of X'X (so the
#   movie estimate stays decorrelated); "paper" the literal 1000 in gray levels
NLAGS8 = 24  # [paper] "24 temporal points spaced at 8 ms" (Estimation of Receptive Fields, par. 4)
WIN8 = 15  # [assume] the 128 Hz RF is estimated in a 15 x 15 window (3 deg) centred on the maximal point of
#            the frame-rate RF, smaller than the paper's 21 x 21 to fit the time limit; used for the
#            temporal properties only
NSEG = 9  # [paper] "Each response was broken into nine segments" (par. 4)
NL_GROUP = 250  # [paper] "separated into groups of 250 values" (Estimation of Static Nonlinearities)
MEAN_LUM = 125.0  # [paper] movies rescaled to a mean of 125 of 0-255 (Natural Scene Movie and WN Stimuli)
DEG_PER_PIXEL = 0.2  # [paper] "each pixel was a square measuring 0.2 deg"
WN_SECONDS = 360.0  # [paper] "a 6 min segment of a spatiotemporal binary white noise stimulus"


def seed(claim_id, extra=0):
    """The claim's seed (protocol, author step 3)."""
    return zlib.crc32(f"{PAPER_KEY}/{claim_id}".encode()) + extra


# ----------------------------------------------------------------------------------------------
# Archive access
# ----------------------------------------------------------------------------------------------

def assets():
    out, url = [], f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r["next"]
    return out


def open_asset(asset_id):
    url = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60).url
    return h5py.File(remfile.File(url), "r")


def _col(g, name):
    d = g[name][()]
    if d.dtype.kind in "OS":
        d = np.array([x.decode() if isinstance(x, bytes) else x for x in d], dtype=object)
    return d


def _ragged(g, name):
    data, idx = g[name][()], g[name + "_index"][()]
    starts = np.r_[0, idx[:-1]]
    return [data[a:b] for a, b in zip(starts, idx)]


def load_session(f):
    """Units, the stimulus recordings of the paper (NAT and SBN), and the repetitions of one file."""
    u = f["units"]
    units = {k: _col(u, k) for k in ["unit_name", "cell_number", "electrode_number", "LGN_layer",
                                     "xy_class", "xy_class_source", "possible_duplicate_of"]}
    units["spikes"] = _ragged(u, "spike_times")
    t = f["intervals/trials"]
    cols = ["trial_key", "modality", "regime", "code", "contrast", "contrast_rms", "start_time",
            "stop_time", "stim_template", "stim_start", "stim_stop", "stimulus_series", "n_reps",
            "derived", "duration_s"]
    trials = {k: _col(t, k) for k in cols}
    trials["frame_times"] = []
    for s in trials["stimulus_series"]:
        if s:
            g = f["stimulus/presentation"][s]
            n = g["data"].shape[0]
            if "timestamps" in g:
                ft = g["timestamps"][()]
            else:
                ft = g["starting_time"][()] + np.arange(n) / g["starting_time"].attrs["rate"]
            trials["frame_times"].append((ft, g["data"][()]))
        else:
            trials["frame_times"].append(None)
    reps = None
    if "repetitions" in f["intervals"]:
        r = f["intervals/repetitions"]
        reps = {k: _col(r, k) for k in ["start_time", "stop_time", "trial_key", "rep_index",
                                        "contrast", "rep_duration", "invalid_units"]}
    return {"units": units, "trials": trials, "reps": reps,
            "subject": f["general/subject/subject_id"][()].decode(),
            "session": f["general/session_id"][()].decode()}


def load_templates(lib, names=("NAT", "WN")):
    """Whole stimulus templates from the stimulus library (float32, frames x 48 x 48)."""
    return {n: lib["stimulus/templates"][n]["data"][()] for n in names}


# ----------------------------------------------------------------------------------------------
# Stimulus and response
# ----------------------------------------------------------------------------------------------

def scaled(template, rms):
    """Stimulus in gray levels about the mean: [paper] frames rescaled to the stated RMS contrast
    about a mean of 125 and set to zero mean for analysis. The NAT template holds frames of zero
    mean and unit SD and the WN template holds +-1 (library descriptions), so the deviation from
    the mean is 125 x rms x template. A common scale cancels from every percent change."""
    return (MEAN_LUM * rms) * template


def frame_counts(spikes, ft):
    """Spike counts in each frame interval of a recording (frame times ft)."""
    edges = np.r_[ft, ft[-1] + np.median(np.diff(ft))]
    return np.histogram(spikes, edges)[0].astype(float)


def bin_counts(spikes, t0, t1, width=BIN):
    n = int(np.floor((t1 - t0) / width))
    return np.histogram(spikes, t0 + width * np.arange(n + 1))[0].astype(float), t0 + width * (np.arange(n) + 0.5)


def frame_of(times, ft):
    """Index of the frame on screen at each time (sample and hold)."""
    return np.clip(np.searchsorted(ft, times, side="right") - 1, 0, len(ft) - 1)


# ----------------------------------------------------------------------------------------------
# Receptive fields
# ----------------------------------------------------------------------------------------------

def locate(stim, counts, lags=(2, 3, 4, 5, 6)):
    """Row and column of the RF peak from the spike-triggered average over the whole 48 x 48 frame,
    used only to place the 21 x 21 window [standard]."""
    T = len(counts)
    sta = np.zeros(stim.shape[1:])
    best = None
    for l in lags:
        a = np.tensordot(counts[l:], stim[:T - l], axes=(0, 0)) / counts[l:].sum()
        if best is None or np.abs(a).max() > np.abs(best).max():
            best = a
    sm = scipy.ndimage.gaussian_filter(best, 1.0)
    r, c = np.unravel_index(np.argmax(np.abs(sm)), sm.shape)
    return int(r), int(c)


def window(center, size=48, win=WIN):
    h = win // 2
    r0 = min(max(center[0] - h, 0), size - win)
    c0 = min(max(center[1] - h, 0), size - win)
    return r0, c0


def _xtx(S, a, b, nl):
    """Block-Toeplitz X'X for frames a..b-1 with nl lags; S is frames x pixels. The block for lags
    (l1, l2) is sum_t s[t-l1] s[t-l2]', taken over the segment with the shift of the lag
    difference (edge terms of at most nl frames are not exact; [standard])."""
    P = S.shape[1]
    lo = max(a, nl - 1)
    # C_d = sum_u s[u] s[u+d]'; the block for lags (i, j) is C_{i-j} when i >= j, else C_{j-i}'
    C = [S[lo:b - d].T @ S[lo + d:b] for d in range(nl)]
    M = np.empty((nl * P, nl * P), dtype=np.float32)
    for i in range(nl):
        for j in range(nl):
            M[i * P:(i + 1) * P, j * P:(j + 1) * P] = C[i - j] if i >= j else C[j - i].T
    return M


def _xtx_exact_sign_check():
    """Synthetic check of _xtx against an explicit design matrix (used in the notebook)."""
    rng = np.random.default_rng(0)
    S = rng.standard_normal((4000, 3))
    nl = 3
    X = np.stack([np.roll(S, l, axis=0) for l in range(nl)], axis=1)[nl - 1:].reshape(-1, nl * 3)
    return np.abs(_xtx(S, 0, 4000, nl) - X.T @ X).max() / np.abs(X.T @ X).max()


def _xty(S, r, a, b, nl):
    lo = max(a, nl - 1)
    return np.concatenate([S[lo - l:b - l].T @ r[lo:b] for l in range(nl)])


def estimate_rf(S, r, a, b, rngs=(), nl=NLAGS, nseg=NSEG, lams=None):
    """RF from frames (or bins) a..b-1 of stimulus S (samples x pixels) and counts r, as the mean of
    nseg segment estimates [paper, Estimation of Receptive Fields, par. 4]. Each estimate is the
    ridge solution (X'X + lam I)^-1 X'y, the converged value of the paper's RLS with g0 = 0 and
    K0 = D x I [paper, par. 3]. lams: the penalties, absolute (default [RIDGE_REL x the stimulus
    variance]). Returns one dict
    per penalty: the mean RF (lags x pixels), the SD over segments, and, for each generator in
    rngs, the mean RF from responses shuffled in time within each segment (the noise estimate of
    the inclusion rule and of the centre's error level [paper, Natural Scene Movie and White Noise
    Stimuli, par. 2; Definition of Center and Surround]). The shuffles are the same for every
    penalty."""
    if lams is None:
        lams = [RIDGE_REL * float(np.mean(np.square(S[a:b], dtype=np.float64)))]
    P = S.shape[1]
    bounds = np.linspace(a, b, nseg + 1).astype(int)
    rfs = [[] for _ in lams]
    shuf = [[[] for _ in rngs] for _ in lams]
    for k in range(nseg):
        s0, s1 = bounds[k], bounds[k + 1]
        M0 = _xtx(S, s0, s1, nl)
        Y = [r]
        for rng in rngs:
            rs = r.copy()
            rs[s0:s1] = rng.permutation(r[s0:s1])
            Y.append(rs)
        Y = np.array(Y, dtype=S.dtype).T
        XY = _xty(S, Y, s0, s1, nl)
        for i, lam in enumerate(lams):
            M = M0.copy()
            M[np.diag_indices_from(M)] += lam
            try:
                c = scipy.linalg.cho_factor(M, overwrite_a=True, check_finite=False)
                sol = scipy.linalg.cho_solve(c, XY, check_finite=False)
            except np.linalg.LinAlgError:  # not positive definite in single precision: solve in double
                M = M0.astype(np.float64)
                M[np.diag_indices_from(M)] += lam
                sol = scipy.linalg.solve(M, XY.astype(np.float64), assume_a="pos").astype(S.dtype)
            rfs[i].append(sol[:, 0])
            for j in range(len(rngs)):
                shuf[i][j].append(sol[:, j + 1])
    out = []
    for i in range(len(lams)):
        x = np.array(rfs[i]).reshape(nseg, nl, P)
        out.append({"rf": x.mean(0), "sd": x.std(0), "segments": x,
                    "shuffled": [np.array(y).reshape(nseg, nl, P).mean(0) for y in shuf[i]]})
    return out


def equal_spike_stop(r1, r2):
    """[paper] "RF estimates for a given cell were estimated using the same number of spikes for
    high- and low-contrast responses" (par. 4): the response with more spikes is cut, from its
    end, to the number of spikes of the other. Returns the frame counts to use for each."""
    n = min(r1.sum(), r2.sum())
    e1 = int(np.searchsorted(np.cumsum(r1), n)) + 1
    e2 = int(np.searchsorted(np.cumsum(r2), n)) + 1
    return min(e1, len(r1)), min(e2, len(r2))


# ----------------------------------------------------------------------------------------------
# RF properties
# ----------------------------------------------------------------------------------------------

def center_surround(rf, err, win=WIN):
    """[paper, Definition of Center and Surround, after Lesica and Stanley 2004] The maximal point;
    the centre is the pixels at its latency, contiguous with it (4-connected [standard]), of its
    sign and above the error level err; the surround is a ring around the centre at most four
    pixels wide (four 8-connected dilations [standard])."""
    lag, pix = np.unravel_index(np.argmax(np.abs(rf)), rf.shape)
    sign = np.sign(rf[lag, pix])
    frame = rf[lag].reshape(win, win)
    ok = (frame * sign) > err
    lab, _ = scipy.ndimage.label(ok)
    center = lab == lab.reshape(-1)[pix]
    ring = scipy.ndimage.binary_dilation(center, structure=np.ones((3, 3)), iterations=4) & ~center
    return {"lag": int(lag), "pix": int(pix), "sign": float(sign), "center": center, "surround": ring}


def profiles(rf, cs):
    c = rf[:, cs["center"].reshape(-1)].mean(1)
    s = rf[:, cs["surround"].reshape(-1)].mean(1) if cs["surround"].any() else np.zeros(rf.shape[0])
    return c, s


def surround_ratio(rf, cs, reading="a"):
    """[paper, Measurement of RF and NL Properties] |peak of surround profile| / peak of centre
    profile. Reading (a) the surround's largest absolute value; (b) its extreme of the sign
    opposite to the centre [claim, fig3c-surround-contrast]."""
    c, s = profiles(rf, cs)
    sign = cs["sign"]
    cp = np.max(c * sign)
    if reading == "a":
        sp = np.max(np.abs(s))
    else:
        sp = max(np.max(-s * sign), 0.0)
    return sp / cp


def _half_width(y, k, dt):
    """Width at half height of the phase of y containing index k (peak, y[k] > 0), with linear
    interpolation of the crossings [claim, P6]."""
    h = y[k] / 2
    i = k
    while i > 0 and y[i - 1] > h:
        i -= 1
    left = (i - 1) + (h - y[i - 1]) / (y[i] - y[i - 1]) if i > 0 else float(i)
    j = k
    while j < len(y) - 1 and y[j + 1] > h:
        j += 1
    right = j + (y[j] - h) / (y[j] - y[j + 1]) if j < len(y) - 1 else float(j)
    return (right - left) * dt


def temporal_props(rf, cs, dt):
    """Temporal width (primary phase at half its peak), latency (lag of the peak) and biphasic ratio
    (|primary peak| / |secondary peak|, the opposite-sign extreme after the primary phase)
    [paper, Measurement of RF and NL Properties]. Lag l is the frame shown l frames before the
    response bin; latency is given as (l + 0.5) frames, the middle of that frame [standard]."""
    c, _ = profiles(rf, cs)
    y = c * cs["sign"]
    k = int(np.argmax(y))
    width = _half_width(y, k, dt)
    after = y[k:]
    sec = -after.min() if after.min() < 0 else np.nan
    return {"temporal_width": width, "latency": (k + 0.5) * dt, "biphasic": y[k] / sec if sec > 0 else np.nan}


def dog(xy, x0, y0, a1, s1, a2, s2):
    r2 = (xy[0] - x0) ** 2 + (xy[1] - y0) ** 2
    return a1 * np.exp(-r2 / (2 * s1 ** 2)) - a2 * np.exp(-r2 / (2 * s2 ** 2))


def spatial_width(rf, cs):
    """[paper] The spatial profile at the peak latency fitted with a symmetric 2D difference of
    Gaussians; width = full width of the fitted function at half its peak, in degrees."""
    frame = rf[cs["lag"]].reshape(WIN, WIN) * cs["sign"]
    yy, xx = np.mgrid[0:WIN, 0:WIN].astype(float)
    r0, c0 = np.unravel_index(cs["pix"], (WIN, WIN))
    p0 = [c0, r0, frame.max(), 1.0, frame.max() * 0.1, 3.0]
    lb = [0, 0, 0, 0.2, 0, 0.2]
    ub = [WIN - 1, WIN - 1, np.inf, 10, np.inf, 30]
    try:
        p, _ = scipy.optimize.curve_fit(dog, np.vstack([xx.ravel(), yy.ravel()]), frame.ravel(), p0=p0,
                                        bounds=(lb, ub), maxfev=20000)
    except RuntimeError:
        return np.nan
    a1, s1, a2, s2 = p[2:]
    rr = np.linspace(0, 15, 3001)
    f = a1 * np.exp(-rr ** 2 / (2 * s1 ** 2)) - a2 * np.exp(-rr ** 2 / (2 * s2 ** 2))
    if f[0] <= 0:
        return np.nan
    below = np.nonzero(f < f[0] / 2)[0]
    if len(below) == 0:
        return np.nan
    return 2 * rr[below[0]] * DEG_PER_PIXEL


def rf_properties(rf, err, dt, reading="a"):
    cs = center_surround(rf, err)
    out = {"peak": float(np.abs(rf).max()), "sign": cs["sign"], "n_center": int(cs["center"].sum()),
           "spatial_width": spatial_width(rf, cs),
           "surround_ratio_a": surround_ratio(rf, cs, "a"), "surround_ratio_b": surround_ratio(rf, cs, "b")}
    out.update(temporal_props(rf, cs, dt))
    return out


# ----------------------------------------------------------------------------------------------
# Nonlinearities
# ----------------------------------------------------------------------------------------------

def filtered(S, rf, nl=NLAGS):
    """Stimulus (zero mean) convolved with the RF normalized to unit variance [paper, Estimation of
    Static Nonlinearities]; one value per frame (frames before nl-1 are NaN)."""
    g = rf / rf.std()
    y = np.full(S.shape[0], np.nan)
    acc = np.zeros(S.shape[0] - nl + 1)
    for l in range(nl):
        acc += S[nl - 1 - l:S.shape[0] - l] @ g[l]
    y[nl - 1:] = acc
    return y


def nonlinearity(y8, rate8, nseg=NSEG):
    """[paper] Filtered values sorted and grouped by 250; mean filtered value and mean rate of each
    group; one NL per segment, the mean of nine (groups aligned by rank)."""
    bounds = np.linspace(0, len(y8), nseg + 1).astype(int)
    xs, ys = [], []
    for k in range(nseg):
        yy, rr = y8[bounds[k]:bounds[k + 1]], rate8[bounds[k]:bounds[k + 1]]
        ok = np.isfinite(yy)
        yy, rr = yy[ok], rr[ok]
        o = np.argsort(yy)
        n = len(o) // NL_GROUP
        xs.append(yy[o[:n * NL_GROUP]].reshape(n, NL_GROUP).mean(1))
        ys.append(rr[o[:n * NL_GROUP]].reshape(n, NL_GROUP).mean(1))
    n = min(len(x) for x in xs)
    return np.mean([x[:n] for x in xs], 0), np.mean([y[:n] for y in ys], 0)


def fit_rectifier(x, y):
    """[claim, P4] Least-squares fit of f(x) = a (x - q) for x >= q, else 0, to the mean NL: for each
    q on a fine grid the best a is closed form; the best q is then refined."""
    def sse(q):
        z = np.maximum(x - q, 0)
        zz = z @ z
        a = (z @ y) / zz if zz > 0 else 0.0
        return ((y - a * z) ** 2).sum(), a
    grid = np.linspace(x.min(), x.max(), 400)
    errs = [sse(q)[0] for q in grid]
    q0 = grid[int(np.argmin(errs))]
    step = grid[1] - grid[0]
    res = scipy.optimize.minimize_scalar(lambda q: sse(q)[0], bounds=(q0 - step, q0 + step), method="bounded")
    q = float(res.x)
    return sse(q)[1], q


# ----------------------------------------------------------------------------------------------
# Repeats
# ----------------------------------------------------------------------------------------------

def rep_matrix(spikes, starts, dur, width=BIN):
    n = int(np.floor(dur / width))
    out = np.zeros((len(starts), n))
    for i, s0 in enumerate(starts):
        out[i] = np.histogram(spikes, s0 + width * np.arange(n + 1))[0]
    return (out / width).astype(np.float32)


def reliability(R, demean=False):
    """[paper, Measurement of Reliability and Sparseness, after Borst and Theunissen 1999] total power
    of the trial-averaged response over the mean over trials of the power of each trial minus
    the average. By Parseval the total power of a spectrum is the sum of squares. Reading P8 (a)
    keeps the mean (DC) in the signal, (b) removes it [claim]."""
    m = R.mean(0)
    sig = m - m.mean() if demean else m
    noise = ((R - m) ** 2).sum(1).mean()
    return (sig ** 2).sum() / noise


def sparseness(rate):
    """[paper, after Vinje and Gallant 2000] (1 - m^2/(m^2 + s^2)) / (1 - 1/n); population SD [claim, P7]."""
    m, s, n = rate.mean(), rate.std(), len(rate)
    if m == 0 and s == 0:
        return np.nan
    return (1 - m ** 2 / (m ** 2 + s ** 2)) / (1 - 1 / n)


def pct_change(a, b):
    """[claim, P1] Percent change from condition a to b: (a) of the sample means, (b) mean of each
    cell's percent change; (c) the ratio of the means, in percent (the claim's (c) reads 'increased
    by X%' as a ratio of X/100, so it is compared with X directly)."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    ok = np.isfinite(a) & np.isfinite(b)
    a, b = a[ok], b[ok]
    return {"a": 100 * (b.mean() - a.mean()) / a.mean(), "b": float(np.mean(100 * (b - a) / a)),
            "c": 100 * b.mean() / a.mean()}


# ----------------------------------------------------------------------------------------------
# One pass over a penetration: every measure the claims use, per unit
# ----------------------------------------------------------------------------------------------

STIMRES = 0.00833911056439  # display refresh period (s), from the files' stimulus_display device
REP_DT = 2 * STIMRES  # one stimulus frame per two refreshes; frame k of a repetition starts at k x REP_DT


def _trial(tr, code_prefix, contrast, regime="unique", modality="NAT"):
    for i in range(len(tr["trial_key"])):
        if (tr["modality"][i] == modality and tr["regime"][i] == regime and tr["contrast"][i] == contrast
                and str(tr["code"][i]).startswith(code_prefix) and "test" not in str(tr["code"][i])
                and not tr["derived"][i]
                and tr["stim_template"][i] in ("NAT", "WN")):
            return i
    return None


def _rep_rows(reps, key, unit):
    m = reps["trial_key"] == key
    starts, durs, inval = reps["start_time"][m], reps["rep_duration"][m], reps["invalid_units"][m]
    order = np.argsort(reps["rep_index"][m])
    keep = [j for j in order if unit not in json.loads(inval[j])]
    return starts[keep], float(np.median(durs))


def penalty(kind, value, var):
    if kind == "abs":
        return value
    return (RIDGE_REL if value is None else value) * var


def condition(St, ft, spikes, a, b, rngs, variants=True):
    """RF and NL of one unit in one stimulus condition, from frames a..b-1 (St frames x pixels in the
    unit's window). rngs: generators for the shuffled-response noise estimate (one per seed). The
    main estimate uses the penalty PENALTIES["main"]; with variants, the other PENALTIES are
    computed from the same shuffles and returned under "variants"."""
    r = frame_counts(spikes, ft)
    if r[a:b].sum() < NSEG:
        return {"n_spikes": float(r[a:b].sum()), "frames": (a, b), "failed": "fewer spikes than segments"}
    var = float(np.mean(np.square(St[a:b], dtype=np.float64)))
    names = list(PENALTIES) if variants else ["main"]
    lams = [penalty(*PENALTIES[n], var) for n in names]
    ests = estimate_rf(St, r, a, b, rngs=rngs, lams=lams)
    t0, t1 = ft[max(a, NLAGS - 1)], ft[b - 1] + (ft[1] - ft[0])
    c8, tc = bin_counts(spikes, t0, t1)
    fi = frame_of(tc, ft)
    outs = []
    for est, lam in zip(ests, lams):
        rf = est["rf"]
        errs = [x.std() for x in est["shuffled"]]
        y = filtered(St, rf)
        try:
            xs, ys = nonlinearity(y[fi], c8 / BIN)
            gain, q = fit_rectifier(xs, ys)
        except ValueError:  # fewer than 250 bins in a segment: no NL
            xs, ys, gain, q = np.array([]), np.array([]), np.nan, np.nan
        yv = y[max(a, NLAGS - 1):b]
        outs.append({"rf": rf, "rf_sd": est["sd"], "err": errs[0], "errs": errs, "nl_x": xs, "nl_y": ys,
                     "gain": gain, "offset": q, "y_sd": float(np.nanstd(yv)), "frames": (a, b),
                     "n_spikes": float(r[a:b].sum()), "lam": lam})
    out = outs[0]
    out["variants"] = dict(zip(names[1:], outs[1:]))
    return out


def rf8(F, rms, w8, ft, spikes, a, b, rng):
    """[paper] The RF at the paper's resolution: "spike times were binned at 128 Hz ... 24 temporal
    points spaced at 8 ms" (Estimation of Receptive Fields, par. 4), nine segments.
    The stimulus of each 128 Hz bin is the frame on screen at its centre (sample and hold). Window:
    WIN8 x WIN8 pixels at w8 [assume, see WIN8]. Frames a..b-1 as in the frame-rate estimate (same
    number of spikes at HC and LC). Penalty [assume]: RIDGE_REL x stimulus variance x (frame period /
    BIN), the same penalty per second of data as the frame-rate estimate. Returns the temporal properties of the centre, its sign and the
    surround/center ratios."""
    r0, c0 = w8
    S = np.ascontiguousarray(F[:b, r0:r0 + WIN8, c0:c0 + WIN8]).reshape(b, -1) * np.float32(MEAN_LUM * rms)
    t1 = ft[b - 1] + (ft[1] - ft[0])
    c8, tc = bin_counts(spikes, ft[a], t1)
    Sb = np.ascontiguousarray(S[frame_of(tc, ft)])
    if c8.sum() < NSEG:
        return {"failed": "fewer spikes than segments"}
    lam = RIDGE_REL * float(np.mean(np.square(S[a:b], dtype=np.float64))) / (FRAME_RATE * BIN)
    est = estimate_rf(Sb, c8, 0, len(c8), rngs=[rng], nl=NLAGS8, lams=[lam])[0]
    rf, err = est["rf"], est["shuffled"][0].std()
    cs = center_surround(rf, err, win=WIN8)
    out = {"rf": rf, "err": err, "sign": cs["sign"], "snr": float(np.abs(rf).max() / err),
           "surround_ratio_a": surround_ratio(rf, cs, "a"), "surround_ratio_b": surround_ratio(rf, cs, "b")}
    out.update(temporal_props(rf, cs, BIN))
    return out


def _frames(tmpl, idx):
    """The template frames shown, as a view when they are a contiguous run (always so here)."""
    if len(idx) and np.all(np.diff(idx) == 1):
        return tmpl[idx[0]:idx[-1] + 1]
    return tmpl[idx]


def process_session(f, T, seeds, wn_seconds=WN_SECONDS, ns_skip=0, wn=True, key=(0, 0), variants=True, do8=True, units_only=None):
    """All per-unit measures of one penetration. T: templates {'NAT', 'WN'} (frames x 48 x 48).
    seeds: the seeds of the shuffles (the claim's seed and the four others); each unit's
    generators are seeded with [seed, *key, unit] so that the result does not depend on the
    order in which penetrations are processed. ns_skip: first frames of the 15 min movie left
    out of RF and NL estimation (Expt2, whose 90 s repeats show movie frames 0-5400; see the
    notebook). wn: whether to estimate white-noise RFs. variants: whether to compute the variant
    penalties (see condition).
    do8: whether to estimate the 128 Hz RFs (rf8), in a window centred on the maximal point of the
    HC movie RF, for all four stimuli. units_only: process only these unit indices (development)."""
    s = load_session(f)
    tr, units = s["trials"], s["units"]
    iH, iL = _trial(tr, "ns", "H"), _trial(tr, "ns", "L")
    wH, wL = _trial(tr, "wn", "H", modality="SBN"), _trial(tr, "wn", "L", modality="SBN")
    out = []
    for u in range(len(units["unit_name"])):
        if units_only is not None and u not in units_only:
            continue
        rngs = [np.random.default_rng([sd, *key, u]) for sd in seeds]
        sp = units["spikes"][u]
        d = {k: units[k][u] for k in ["unit_name", "electrode_number", "LGN_layer", "xy_class", "possible_duplicate_of"]}
        d.update(subject=s["subject"], session=s["session"], unit=u)
        if iH is None or iL is None:
            out.append(d)
            continue
        try:
            ftH, idxH = tr["frame_times"][iH]
            ftL, idxL = tr["frame_times"][iL]
            rH, rL = frame_counts(sp, ftH), frame_counts(sp, ftL)
            d["rate_ns_H"], d["rate_ns_L"] = rH.sum() / (ftH[-1] - ftH[0]), rL.sum() / (ftL[-1] - ftL[0])
            FH = _frames(T["NAT"], idxH)
            center = locate(FH[ns_skip:], rH[ns_skip:])
            r0, c0 = window(center)
            d["window"] = (r0, c0)

            def cut(F, rms):
                return np.ascontiguousarray(F[:, r0:r0 + WIN, c0:c0 + WIN]).reshape(len(F), -1) * np.float32(MEAN_LUM * rms)

            SH = cut(FH, float(tr["contrast_rms"][iH]))
            SL = cut(_frames(T["NAT"], idxL), float(tr["contrast_rms"][iL]))
            eH, eL = equal_spike_stop(rH[ns_skip:], rL[ns_skip:])
            d["ns_H"] = condition(SH, ftH, sp, ns_skip, ns_skip + eH, rngs, variants)
            d["ns_L"] = condition(SL, ftL, sp, ns_skip, ns_skip + eL, rngs, variants)
            d["rms"] = {"ns_H": float(tr["contrast_rms"][iH]), "ns_L": float(tr["contrast_rms"][iL])}
            w8 = None
            if do8 and "rf" in d["ns_H"]:
                pix = int(np.argmax(np.abs(d["ns_H"]["rf"]).max(0)))
                w8 = window((r0 + pix // WIN, c0 + pix % WIN), win=WIN8)
                d["window8"] = w8
                rng8 = np.random.default_rng([seeds[0], *key, u, 8])
                d["ns_H_8"] = rf8(FH, d["rms"]["ns_H"], w8, ftH, sp, ns_skip, ns_skip + eH, rng8)
                d["ns_L_8"] = rf8(_frames(T["NAT"], idxL), d["rms"]["ns_L"], w8, ftL, sp, ns_skip, ns_skip + eL, rng8)
            if wn and wH is not None and wL is not None:
                ftWH, idxWH = tr["frame_times"][wH]
                ftWL, idxWL = tr["frame_times"][wL]
                nW = int(round(wn_seconds * FRAME_RATE))
                rWH, rWL = frame_counts(sp, ftWH)[:nW], frame_counts(sp, ftWL)[:nW]
                d["rate_wn_H"], d["rate_wn_L"] = rWH.sum() / (ftWH[nW - 1] - ftWH[0]), rWL.sum() / (ftWL[nW - 1] - ftWL[0])
                fH, fL = equal_spike_stop(rWH, rWL)
                FWH, FWL = _frames(T["WN"], idxWH[:nW]), _frames(T["WN"], idxWL[:nW])
                d["wn_H"] = condition(cut(FWH, float(tr["contrast_rms"][wH])), ftWH, sp, 0, fH, rngs, variants)
                d["wn_L"] = condition(cut(FWL, float(tr["contrast_rms"][wL])), ftWL, sp, 0, fL, rngs, variants)
                d["rms"].update(wn_H=float(tr["contrast_rms"][wH]), wn_L=float(tr["contrast_rms"][wL]))
                d["wn_trials"] = {"H": str(tr["trial_key"][wH]), "L": str(tr["trial_key"][wL])}
                if w8 is not None:
                    d["wn_H_8"] = rf8(FWH, d["rms"]["wn_H"], w8, ftWH, sp, 0, fH, rng8)
                    d["wn_L_8"] = rf8(FWL, d["rms"]["wn_L"], w8, ftWL, sp, 0, fL, rng8)
            if s["reps"] is not None:
                d.update(repeats(s, u, T, None, (ftH, rH)))
        except Exception as e:  # recorded, and the unit counted as dropped
            d["error"] = repr(e)
        out.append(d)
    return s, out


_T = None


def _worker(job):
    from threadpoolctl import threadpool_limits
    path, asset_id, seeds, kw = job
    import time
    t = time.time()
    with threadpool_limits(1):
        f = open_asset(asset_id)
        s, out = process_session(f, _T, seeds, **kw)
    print(f"{path}: {len(out)} units, {time.time() - t:.0f} s", flush=True)
    s["units"].pop("spikes")
    return path, s, out


def run_all(T, jobs, procs=4):
    """process_session over penetrations in parallel (fork; one BLAS thread per process)."""
    import multiprocessing as mp
    global _T
    _T = T
    with mp.get_context("fork").Pool(procs) as pool:
        res = pool.map(_worker, jobs, chunksize=1)
    _T = None
    return res


def repeats(s, u, T, cut, unique_H):
    """Measures from the repeated segments of one unit. Expt1: 120 repetitions of three 250-frame
    blocks per stimulus (the paper's "120 repeated trials of different 12 s segments"); per block,
    the 8 ms rate of each valid repetition. Expt2: 24 repetitions of 90 s (frames 0-5400 of the
    movie) at each contrast, for the LN predictions; also the clock check against the unique movie."""
    tr, reps = s["trials"], s["reps"]
    sp = s["units"]["spikes"][u]
    out = {}
    keys = list(tr["trial_key"])
    blocks = {}
    for i, k in enumerate(keys):
        code = str(tr["code"][i])
        if tr["regime"][i] != "repeat" or tr["derived"][i]:
            continue
        if code[:2] in ("nr", "wr") and str(tr["stim_template"][i]).startswith("clip_"):
            stim = ("ns" if code[:2] == "nr" else "wn") + "_" + tr["contrast"][i]
            starts, dur = _rep_rows(reps, k, u)
            blocks.setdefault(stim, []).append(rep_matrix(sp, starts, dur))
        elif code == "nr" and int(tr["n_reps"][i]) == 24:
            starts, dur = _rep_rows(reps, k, u)
            out["rep90_" + tr["contrast"][i]] = rep_matrix(sp, starts, dur)
            out["rep90_frames"] = (int(tr["stim_start"][i]), int(tr["stim_stop"][i]))
            if tr["contrast"][i] == "H":
                # clock check: per-frame PSTH of the repeats against the first 5400 frames of the
                # unique movie, at shifts of -6..6 frames
                R = rep_matrix(sp, starts, dur, width=REP_DT).mean(0) * REP_DT
                ftH, rH = unique_H
                n = min(len(R), 5400)
                cc = []
                for sh in range(-6, 7):
                    a, b = (sh, n) if sh >= 0 else (0, n + sh)
                    cc.append(np.corrcoef(R[a:b], rH[a - sh:b - sh])[0, 1])
                out["clock_cc"] = np.array(cc)
    for k, v in blocks.items():
        out["rep12_" + k] = v
    return out



def choose_ridge(cases, specs):
    """[paper, Estimation of Receptive Fields, par. 3] "the value of D that produced the RF estimates
    that provided the most accurate predictions of responses to natural scene movies was used".
    For each case (stimulus frames x pixels, frame counts), the RF is estimated as in the Methods
    (nine segments) from the first 90% of the movie and its linear prediction is correlated with
    the frame counts of the last 10%. specs: penalties as (kind, value), see penalty. Returns the
    correlations, cases x penalties."""
    out = np.zeros((len(cases), len(specs)))
    for i, (S, r) in enumerate(cases):
        ntr = int(0.9 * len(r))
        var = float(np.mean(np.square(S[:ntr], dtype=np.float64)))
        ests = estimate_rf(S, r, 0, ntr, lams=[penalty(k, v, var) for k, v in specs])
        for j, est in enumerate(ests):
            y = filtered(S[ntr - NLAGS + 1:], est["rf"])[NLAGS - 1:]
            out[i, j] = np.corrcoef(y, r[ntr:])[0, 1]
    return out


# ----------------------------------------------------------------------------------------------
# Tables for the claims
# ----------------------------------------------------------------------------------------------

CONDITIONS = ["ns_H", "ns_L", "wn_H", "wn_L"]
PROPS = ["spatial_width", "surround_ratio_a", "surround_ratio_b", "temporal_width_8", "temporal_width", "latency_8",
         "latency", "biphasic_8", "biphasic", "gain", "offset", "norm_offset"]


def unit_table(results, dt=1 / FRAME_RATE, which="main"):
    """One row per unit: rates, RF peak over noise under each seed, and the RF and NL properties of
    each condition. The noise is the SD of the RF estimated from shuffled responses. which: the
    penalty (a key of PENALTIES). The 128 Hz RF's properties (rf8) are added with the suffix _8."""
    rows = []
    for path, s, out in results:
        for d in out:
            r = {k: d.get(k) for k in ["subject", "session", "unit_name", "unit", "xy_class", "electrode_number",
                                       "LGN_layer", "possible_duplicate_of", "rate_ns_H", "rate_ns_L",
                                       "rate_wn_H", "rate_wn_L", "error"]}
            for c in CONDITIONS:
                x = d.get(c)
                if not x:
                    continue
                if which != "main" and "variants" in x:
                    x = x["variants"][which]
                x8 = d.get(c + "_8")
                if x8 and "failed" not in x8:
                    for k in ["snr", "sign", "temporal_width", "latency", "biphasic", "surround_ratio_a", "surround_ratio_b"]:
                        r[c + "_" + k + "_8"] = x8[k]
                if "failed" in x:
                    r[c + "_snr"] = 0.0
                    r[c + "_snrs"] = [0.0] * 5
                    continue
                pk = float(np.abs(x["rf"]).max())
                r[c + "_snr"] = pk / x["err"]
                r[c + "_snrs"] = [pk / e for e in x["errs"]]
                p = rf_properties(x["rf"], x["err"], dt)
                for k, v in p.items():
                    r[c + "_" + k] = v
                r[c + "_gain"], r[c + "_offset"], r[c + "_ysd"] = x["gain"], x["offset"], x["y_sd"]
                r[c + "_norm_offset"] = x["offset"] / x["y_sd"]
                r[c + "_n_spikes"] = x["n_spikes"]
                r[c + "_seconds"] = (x["frames"][1] - x["frames"][0]) / FRAME_RATE
            rows.append(r)
    return rows


def repeat_measures(d):
    """Reliability (readings P8 a and b), sparseness and mean rate of the 12 s repeats of one unit,
    per stimulus. Per block: signal = total power of the trial average, noise = mean over trials of
    the total power of trial minus average; the three blocks' powers are summed (the same as
    concatenating each repetition's three blocks). Sparseness is of the three blocks' trial
    averages joined."""
    out = {}
    for c in CONDITIONS:
        blocks = d.get("rep12_" + c)
        if not blocks:
            continue
        sig_a = sig_b = noise = 0.0
        psth = []
        rates = []
        for R in blocks:
            R = R.astype(float)
            m = R.mean(0)
            sig_a += (m ** 2).sum()
            sig_b += ((m - m.mean()) ** 2).sum()
            noise += ((R - m) ** 2).sum(1).mean()
            psth.append(m)
            rates.append(R.mean())
        out[c] = {"rel_a": sig_a / noise, "rel_b": sig_b / noise, "sparse": sparseness(np.concatenate(psth)),
                  "rate": float(np.mean(rates)), "n_reps": [len(R) for R in blocks]}
    return out


# ----------------------------------------------------------------------------------------------
# Figure 5: RFs and NLs from the periods of high and low contrast within the RF
# ----------------------------------------------------------------------------------------------

CONTRAST_WINDOW = 60  # [assume] reading (b): sliding window of 60 frames (1 s) for each pixel's temporal
#                       RMS contrast; the paper gives no length


def rf_contrast(F, rms, weights, reading):
    """[claim, fig5 readings] Contrast within the RF for each frame of the HC movie F (frames x pixels,
    template units), in RMS contrast (SD / mean of luminance, mean 125). weights: one per pixel
    (a mask, or the RF's absolute spatial profile). Reading (a): per frame, the weighted RMS
    contrast over the RF pixels. Reading (b): per pixel, the RMS contrast of its luminance over a
    sliding window of CONTRAST_WINDOW frames, averaged over the RF pixels with the weights."""
    w = weights / weights.sum()
    sel = w > 0
    lum = np.clip(MEAN_LUM * (1 + rms * F[:, sel].astype(np.float64)), 0, 255)  # [standard] as displayed, 0-255
    w = w[sel]
    if reading == "a":
        mu = lum @ w
        return np.sqrt(np.maximum((lum ** 2) @ w - mu ** 2, 0)) / np.maximum(mu, 1.0)
    k = CONTRAST_WINDOW
    m1 = scipy.ndimage.uniform_filter1d(lum, k, axis=0, mode="nearest")
    m2 = scipy.ndimage.uniform_filter1d(lum ** 2, k, axis=0, mode="nearest")
    return (np.sqrt(np.maximum(m2 - m1 ** 2, 0)) / np.maximum(m1, 1.0)) @ w


def estimate_rf_rows(S, r, rows, lam, nl=NLAGS, nseg=NSEG):
    """Ridge RF from the response frames in rows only (sorted frame indices >= nl - 1), as the mean
    of nseg estimates from consecutive groups of rows [paper, par. 4, applied to a subset of
    frames]. The design matrix is built explicitly."""
    P = S.shape[1]
    out = []
    for g in np.array_split(rows, nseg):
        X = np.empty((len(g), nl * P), dtype=S.dtype)
        for l in range(nl):
            X[:, l * P:(l + 1) * P] = S[g - l]
        M = X.T @ X
        M[np.diag_indices_from(M)] += lam
        c = scipy.linalg.cho_factor(M, overwrite_a=True, check_finite=False)
        out.append(scipy.linalg.cho_solve(c, X.T @ r[g].astype(S.dtype), check_finite=False))
    return np.mean(out, 0).reshape(nl, P)


def thirds(asset_id, jobs, seed0):
    """Figure 5 analysis for units of one penetration. jobs: (unit index, window, ns_skip, frame-rate
    HC RF, its error level, readings). For each reading: the contrast trace over the HC movie frames
    used for the RF, its range in each 150 s segment (stepped by 30 s), and the RF and NL from the
    response frames whose stimulus (at the RF's peak lag) lies in the top and bottom thirds of all
    values. The noise level of each third's RF (for its centre) is from a shuffled response."""
    from threadpoolctl import threadpool_limits
    f = open_asset(asset_id)
    s = load_session(f)
    tr = s["trials"]
    iH = _trial(tr, "ns", "H")
    ft, idx = tr["frame_times"][iH]
    rms = float(tr["contrast_rms"][iH])
    F = _frames(_T["NAT"], idx)
    out = []
    with threadpool_limits(1):
        for u, (r0, c0), skip, rf, err, readings in jobs:
            sp = s["units"]["spikes"][u]
            r = frame_counts(sp, ft)
            Fw = np.ascontiguousarray(F[:, r0:r0 + WIN, c0:c0 + WIN]).reshape(len(F), -1)
            S = Fw * np.float32(MEAN_LUM * rms)
            cs = center_surround(rf, err)
            lag = cs["lag"]
            prof = np.abs(rf[lag])
            weights = {"center": cs["center"].reshape(-1).astype(float), "weighted": prof}
            lam = RIDGE_REL * float(np.mean(np.square(S[skip:], dtype=np.float64)))
            t0, t1 = ft[skip], ft[-1] + (ft[1] - ft[0])
            c8, tc = bin_counts(sp, t0, t1)
            fi = frame_of(tc, ft)
            res = {"unit": u}
            for rd, wname in readings:
                ctr = rf_contrast(Fw, rms, weights[wname], rd)
                seg = 9000
                rng_ = [(ctr[a:a + seg].min(), ctr[a:a + seg].max()) for a in range(skip, len(ctr) - seg + 1, 1800)]
                frames = np.arange(max(skip, NLAGS - 1), len(r))
                cval = ctr[frames - lag]
                lo, hi = np.percentile(cval, [100 / 3, 200 / 3])
                d = {"ranges": np.array(rng_), "mean": float(ctr[skip:].mean()), "cuts": (float(lo), float(hi))}
                y = filtered(S, rf)
                for name, rows in (("top", frames[cval >= hi]), ("bottom", frames[cval <= lo])):
                    est = estimate_rf_rows(S, r, rows, lam)
                    rs = r.copy()
                    rs[rows] = np.random.default_rng([seed0, u, len(rows)]).permutation(r[rows])
                    e = estimate_rf_rows(S, rs, rows, lam).std()
                    p = rf_properties(est, e, 1 / FRAME_RATE)
                    yy = filtered(S, est)
                    keep = np.isin(fi, rows)
                    try:
                        xs, ys = nonlinearity(yy[fi][keep], c8[keep] / BIN)
                        p["gain"], p["offset"] = fit_rectifier(xs, ys)
                    except ValueError:
                        p["gain"], p["offset"] = np.nan, np.nan
                    p["n_frames"], p["n_spikes"] = len(rows), float(r[rows].sum())
                    d[name] = p
                res[rd + "_" + wname] = d
            out.append(res)
    f.close()
    return out


def _thirds_worker(job):
    return thirds(*job)


def run_thirds(T, jobs, procs=4):
    import multiprocessing as mp
    global _T
    _T = T
    with mp.get_context("fork").Pool(procs) as pool:
        res = pool.map(_thirds_worker, jobs, chunksize=1)
    _T = None
    return res
