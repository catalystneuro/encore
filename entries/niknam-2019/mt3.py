"""Loading and response measures for CRCNS mt-3 (Niknam et al. 2019, PLoS Comput Biol).

The data set holds one MATLAB 7.3 file per MT neuron in ``data.zip`` (data descriptor,
"Data format"): ``stimcode`` (trial x ms, probe index 0-81, 0 = no probe), ``resp``
(trial x ms spikes, 1 ms bins), ``conds`` (condition per trial) and ``tsaccade``
(saccade onset per trial, ms from the start of the trial). The zip is streamed from the
public CRCNS bucket and opened in place; nothing is written to disk.

Where each parameter comes from:

- Probe index to grid position: ``[i, j] = ind2sub([9, 9], x)`` (data descriptor); the
  paper's code (``code2stim.m``) calls ``i`` x and ``j`` y.
- Saccade index: the paper's code reads the saccade-aligned samples as
  ``tsaccade(i) + times`` in MATLAB's 1-based indexing (``select_bases.m``), so the
  0-based index of saccade onset is ``tsaccade - 1``.
- Windows: fixation -500 to -100 ms, perisaccadic -30 to 0 ms (RF) and -50 to 0 ms (FF,
  ST) from saccade onset; early response 50-75 ms and late response 80-150 ms after probe
  onset (claims file D2; Methods, Statistical analysis of perisaccadic responses). Windows
  are taken inclusive at 1 ms, as ``get_mean_resp.m`` takes ``t:t+window``; a standard
  choice that cannot change a result beyond one bin.
- Test: one-sided Wilcoxon signed-rank on spike counts (D2). The pairs are open (claims
  file O1): ``pairing='trial'`` (a), ``'condition'`` (b), or ``'unpaired'`` (c, a
  one-sided rank-sum on all presentations, a variant). ``timebin_test`` adds a pairing
  outside O1, raised by the verifier: the mean count in each 1 ms bin of the response
  window, perisaccadic against fixation, paired by bin (Methods: "comparing the
  perisaccadic and fixation spike counts (during the same stimulus-aligned window)"). Its
  smoothed form pairs the curves smoothed as for plots, which the Methods exclude ("all
  statistical analyses were performed on spike counts ... (not estimates of firing
  rate)"); both are variants and decide no outcome.
- Presentations (O2): ``mode='onset'`` (i) takes the first ms of each run of a probe code;
  ``mode='every'`` (ii) takes every ms the probe is on, as ``get_mean_resp.m``.
- Normalized response (D3): mean stimulus-aligned spike train 0-150 ms after onset, as a
  rate; each neuron's fixation and perisaccadic responses divided by the mean of their two
  means over 0-150 ms. Smoothing for plots and peak latencies: Gaussian of FWHM 13 ms
  (Methods, same section, paragraph 2).
- RF, FF and ST probes: ``probe_list`` of ``assets/data/main_lists.mat`` in the paper's
  code repository at commit 1438dde, columns 3-4, 5-6 and 7-8 as ``fmodel.m`` reads them
  (claims file O3 a).
- S-model selection (benchmark only): B-spline bases from ``make_bases.m`` (knots every
  7 ms from min - 14 to max + 14, quadratic splines as ``make_bsplie_bases.m`` with
  ``n = 3``), the single-parameter fit of ``select_bases.m`` (gradient ascent, learning
  rate 1e-2 divided by 10 on failure, stop at relative change < 1e-2), r_max 1000 and b0
  from the mean rate in bins with a probe on screen (``make_params``).
"""

import io
import zipfile

import fsspec
import h5py
import numpy as np
import scipy.io
from scipy import stats

DATASET = "crcns:mt-3/unversioned"  # CRCNS data sets are not versioned (docs/archives.md)
DATA_URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/mt-3/live/data.zip"
CHECKSUMS_URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/mt-3/live/checksums.md5"
CODE_COMMIT = "1438dde9dd3207348ec0df1e5c4dd2a7b014e68e"
CODE_RAW = f"https://raw.githubusercontent.com/nnategh/SFA-Models/{CODE_COMMIT}/"
GRID = 9

FIX = (-500, -100)
PERI_RF = (-30, 0)
PERI_LATE = (-50, 0)
EARLY = (50, 75)
LATE = (80, 150)
RESP_SPAN = 150


def open_zip():
    """Open data.zip in place over range requests."""
    return zipfile.ZipFile(fsspec.open(DATA_URL, block_size=2**20).open())


def neuron_names(zf):
    return sorted(n for n in zf.namelist() if n.endswith(".mat"))


def load_neuron(zf, member):
    """Read one neuron's file; arrays are stored transposed in the HDF5 layout."""
    with h5py.File(io.BytesIO(zf.read(member)), "r") as h:
        d = {
            "stimcode": h["stimcode"][()].T,
            "resp": h["resp"][()].T.astype(np.int8),
            "conds": h["conds"][()].ravel().astype(int),
            "tsaccade": h["tsaccade"][()].ravel().astype(int),
        }
    stem = member.split("/")[-1][:-4]
    d["session"], d["channel"] = int(stem[:8]), int(stem[8:])
    d["name"] = stem
    d["sacc"] = d["tsaccade"] - 1
    d["csum"] = np.concatenate(
        [np.zeros((d["resp"].shape[0], 1), np.int32), np.cumsum(d["resp"], 1, dtype=np.int32)], 1
    )
    return d


def load_code_file(path):
    """Read a file of the paper's code repository at the pinned commit, in memory."""
    with fsspec.open(CODE_RAW + path, "rb") as f:
        return f.read()


def load_probe_list():
    """probe_list of main_lists.mat: session, channel, RF x y, FF x y, ST x y (1-based)."""
    m = scipy.io.loadmat(io.BytesIO(load_code_file("assets/data/main_lists.mat")))
    return m


def sub2ind(x, y):
    """MATLAB sub2ind([9, 9], x, y), 1-based probe code."""
    return int(x) + GRID * (int(y) - 1)


def ind2sub(code):
    code = int(code) - 1
    return code % GRID + 1, code // GRID + 1


def presentations(d, probe, mode="onset"):
    """Trial index and 0-based ms of each presentation of a probe code.

    mode 'onset' (O2 i): the first ms of each run of the code; 'every' (O2 ii): every ms
    the probe is on.
    """
    on = d["stimcode"] == probe
    if mode == "every":
        tr, t = np.nonzero(on)
    else:
        start = on & ~np.concatenate([np.zeros((on.shape[0], 1), bool), on[:, :-1]], 1)
        tr, t = np.nonzero(start)
    keep = t + RESP_SPAN < on.shape[1]
    return tr[keep], t[keep]


def all_onsets(d):
    """Every probe onset (O2 i): trial, ms, code."""
    sc = d["stimcode"]
    prev = np.concatenate([np.zeros((sc.shape[0], 1), sc.dtype), sc[:, :-1]], 1)
    tr, t = np.nonzero((sc > 0) & (sc != prev))
    keep = t + RESP_SPAN < sc.shape[1]
    tr, t = tr[keep], t[keep]
    return tr, t, sc[tr, t]


def counts(d, tr, t, win):
    """Spike count in [t + win[0], t + win[1]] (inclusive)."""
    return d["csum"][tr, t + win[1] + 1] - d["csum"][tr, t + win[0]]


def in_window(d, tr, t, win):
    rel = t - d["sacc"][tr]
    return (rel >= win[0]) & (rel <= win[1])


def effect_test(d, probe, peri, resp_win, direction, pairing="trial", mode="onset"):
    """Perisaccadic against fixation spike counts for one probe (claims file D2, O1, O2).

    direction 'less' for suppression, 'greater' for remapping. Returns a dict with the
    one-sided p, the number of pairs or presentations, and the mean counts.
    """
    tr, t = presentations(d, probe, mode)
    c = counts(d, tr, t, resp_win).astype(float)
    fix = in_window(d, tr, t, FIX)
    per = in_window(d, tr, t, peri)
    out = {"n_fix": int(fix.sum()), "n_peri": int(per.sum())}
    if pairing == "unpaired":
        a, b = c[per], c[fix]
        out["n"] = (len(a), len(b))
        out["p"] = (
            stats.mannwhitneyu(a, b, alternative=direction).pvalue if len(a) and len(b) else np.nan
        )
        out["mean_peri"], out["mean_fix"] = (a.mean() if len(a) else np.nan), b.mean()
        return out
    key = tr if pairing == "trial" else d["conds"][tr]
    keys = np.intersect1d(np.unique(key[per]), np.unique(key[fix]))
    a = np.array([c[per & (key == k)].mean() for k in keys])
    b = np.array([c[fix & (key == k)].mean() for k in keys])
    out["n"] = len(keys)
    out["mean_peri"] = a.mean() if len(a) else np.nan
    out["mean_fix"] = b.mean() if len(b) else np.nan
    if len(keys) == 0 or np.all(a - b == 0):
        out["p"] = 1.0 if len(keys) else np.nan
    else:
        out["p"] = stats.wilcoxon(a, b, alternative=direction).pvalue
    return out


def timebin_test(d, probe, peri, resp_win, direction, mode="onset", smooth=False):
    """Variant pairing: mean count per 1 ms bin of resp_win, perisaccadic against fixation,
    one-sided signed-rank over the bins (smooth=True: the FWHM 13 ms curves of D3)."""
    F, P = mean_trains(d, probe, peri, mode)
    f, p = F.mean(0), P.mean(0)
    if smooth:
        f, p = gauss_smooth(f), gauss_smooth(p)
    f, p = f[resp_win[0] : resp_win[1] + 1], p[resp_win[0] : resp_win[1] + 1]
    out = {"n": len(f), "n_fix": len(F), "n_peri": len(P), "mean_fix": f.mean() / 1000, "mean_peri": p.mean() / 1000}
    out["p"] = 1.0 if np.all(p == f) else stats.wilcoxon(p, f, alternative=direction).pvalue
    return out


def mean_trains(d, probe, peri, mode="onset"):
    """Mean stimulus-aligned spike trains (spk/s, 0-150 ms) for fixation and perisaccadic
    presentations, and the per-presentation spike trains for SEs."""
    tr, t = presentations(d, probe, mode)
    lags = np.arange(RESP_SPAN + 1)
    trains = d["resp"][tr[:, None], t[:, None] + lags[None, :]].astype(float) * 1000.0
    fix = in_window(d, tr, t, FIX)
    per = in_window(d, tr, t, peri)
    return trains[fix], trains[per]


def normalized(fix_trains, peri_trains):
    """D3: each response divided by the mean of the two means over 0-150 ms."""
    f, p = fix_trains.mean(0), peri_trains.mean(0)
    g = (f.mean() + p.mean()) / 2.0
    return f / g, p / g


def gauss_smooth(x, fwhm=13.0, axis=-1):
    from scipy.ndimage import gaussian_filter1d

    return gaussian_filter1d(x, fwhm / (2 * np.sqrt(2 * np.log(2))), axis=axis, mode="nearest")


def window_rate(trains, win):
    """Per-presentation mean rate (spk/s) over win (inclusive lags)."""
    return trains[:, win[0] : win[1] + 1].mean(1)


def rf_from_data(d, mode="onset"):
    """D1: the probe with the highest mean early-window count for fixation presentations."""
    tr, t, code = all_onsets(d)
    if mode == "every":
        tr, t = np.nonzero(d["stimcode"] > 0)
        keep = t + RESP_SPAN < d["stimcode"].shape[1]
        tr, t = tr[keep], t[keep]
        code = d["stimcode"][tr, t]
    fix = in_window(d, tr, t, FIX)
    c = counts(d, tr[fix], t[fix], EARLY)
    sums = np.bincount(code[fix], weights=c, minlength=GRID * GRID + 1)[1:]
    ns = np.bincount(code[fix], minlength=GRID * GRID + 1)[1:]
    m = sums / np.maximum(ns, 1)
    return int(np.argmax(m)) + 1, m


# --- S-model parameter selection, used only to time it -------------------------------


def bspline_bases(n_values, delta=14):
    """make_bases.m / make_knots.m / make_bsplie_bases.m: quadratic B-splines on knots
    min - delta : delta/2 : max + delta, evaluated on 1..n_values."""
    from scipy.interpolate import BSpline

    half = delta // 2
    knots = np.arange(1 - 2 * half, n_values + 2 * half + 1, half, dtype=float)
    x = np.arange(1, n_values + 1, dtype=float)
    nb = len(knots) - 3
    B = np.zeros((nb, len(x)))
    for i in range(nb):
        B[i] = BSpline.basis_element(knots[i : i + 4], extrapolate=False)(x)
    return np.nan_to_num(B)


def _phi(u):
    return 1000.0 / (1.0 + np.exp(-u))


def select_fit(BS, rsp, b0, trn, val, rng, shuffle=False):
    """One single-parameter fit of select_bases.m (fit_model, local function).

    BS: (trials, times) regressor for one basis; rsp: (trials, times) spikes.
    """
    if shuffle:
        rsp = rsp[rng.permutation(rsp.shape[0])]
    delta = 1e-3

    def ll(idx, x):
        lam = _phi(x * BS[idx] + b0)
        return np.sum(rsp[idx] * np.log((lam + 1e-16) * delta) - (lam + 1e-16) * delta)

    def grad(idx, x):
        lam = _phi(x * BS[idx] + b0)
        s = lam / 1000.0
        return np.sum((rsp[idx] / lam - delta) * 1000.0 * s * (1 - s) * BS[idx])

    lr, imp, x = 1e-2, np.inf, 1e-6
    while imp > 1e-2 and lr > 1e-8:
        tb, vb = ll(trn, x), ll(val, x)
        nx = x + lr * grad(trn, x)
        ta, va = ll(trn, nx), ll(val, nx)
        if ta <= tb or va <= vb or np.isnan(ta) or np.isnan(va):
            lr /= 10
        else:
            imp = abs(nx - x) / (abs(x) + 1e-16)
            x = nx
    return x
