"""Loading and measures for dandiset 000226 (Severson et al. 2017, Neuron 94:666).

Each NWB file holds one recording: one afferent's spike times (`units`), or none for three EMG
sessions, and per-trial time series at 500 Hz in `processing/behavior`, one TimeSeries per trial
and variable (position, velocity, acceleration, jerk, phase, amplitude, setpoint, frequency, M0,
dM0, Faxial, Flateral, dFaxial, dFlateral, contact, distanceToPoleCenter, deltaKappa and others).

Files are streamed from the DANDI archive into memory, whole, and never written to disk: each file
holds thousands of small datasets, and reading them one HTTP range request at a time took 22 minutes
for the metadata alone, against about two minutes for the whole dandiset read in full.

Where parameters come from:
- Behavioural categories, the outlier percentiles, the WT/WT* rules: the paper's Glossary.
- 30 equal-count phase bins, Gaussian smoothing of sigma 4 ms, the viscoelastic model (Eqs. M1 to
  M4, q = 1,000 Hz/Pa, M0 scaled by the inverse of its 80th percentile): the STAR Methods.
- Bootstrap over trials (1,000 resamples) for the 95% CIs: a common choice; the Methods say only
  "bootstrap".
- The GAM substitute (cubic B-splines with 10 basis functions per variable, second-difference
  penalty lambda = 1, binomial model with two trials per 2 ms frame, at most 60,000 frames per
  fit): a common P-spline choice; the paper used mgcv with UBRE smoothing on 1 ms bins.
- Which recording belongs to which experiment, the afferent type and Merkel identity: Table S1 of
  the paper's Supplemental Information (transcribed below as TABLE_S1).
"""

from __future__ import annotations

import hashlib
import io
import itertools

import h5py
import numpy as np
import requests
from dandi.dandiapi import DandiAPIClient
from scipy import optimize
from scipy.interpolate import BSpline
from scipy.ndimage import gaussian_filter1d
from scipy.signal import butter, filtfilt, hilbert

DANDISET_ID = "000226"
DANDISET_VERSION = "0.230607.1747"
FRAME_HZ = 500.0
DT = 1 / FRAME_HZ
FRAMES_PER_TRIAL = 2500

# Variables read from every file (others in the files are not used).
VARIABLES = ["position", "velocity", "acceleration", "jerk", "phase", "amplitude", "setpoint",
             "frequency", "M0", "dM0", "Faxial", "Flateral", "dFaxial", "dFlateral", "contact",
             "distanceToPoleCenter", "deltaKappa"]
# The ten variables of the paper's "full" touch model, with the names used in the paper.
TOUCH_VARS = ["M0", "Faxial", "Flateral", "dM0", "dFaxial", "dFlateral",
              "position", "velocity", "acceleration", "jerk"]
PAPER_NAME = {"M0": "M0", "Faxial": "Fax", "Flateral": "Flat", "dM0": "M0'", "dFaxial": "Fax'",
              "dFlateral": "Flat'", "position": "theta", "velocity": "omega",
              "acceleration": "alpha", "jerk": "zeta"}
DYNAMIC = {"M0", "Faxial", "Flateral", "dM0", "dFaxial", "dFlateral"}   # outliers at 0.5/99.5
KINEMATIC_VARS = ["position", "velocity", "acceleration", "jerk"]       # outliers at 0.25/99.75

# Table S1 (Supplemental Information of doi:10.1016/j.neuron.2017.03.045), transcribed.
# Columns: recording id, mouse id, sex, mouse line, date (mm/dd/yy), type (RA, SA or NA),
# identified Merkel (Y or -), whisking and touch class, viscoelastic fit (Y, N or NA), group.
# Groups: touch (initial 33), excluded (touch recordings used only for Figure S1), cutonly
# (whisker cut before recording, Figure 7F), whiskonly (whisking in air without touch),
# progressive (progressive cutting), emg.
TABLE_S1 = """
217F KSt95 M TrKC_CreER;Rosa_Ai32 04/29/15 RA - WT* NA touch
227A KSt107 F TrKC_CreER;Rosa_Ai32 05/15/15 RA - WT NA touch
145B KSt76 M TrKC_CreER;Rosa_Ai32 09/27/14 RA - WT NA touch
194A KSt88 M TrKC_CreER;Rosa_Ai32 03/20/15 RA - WT NA touch
202A KSt92 M TrKC_CreER;Rosa_Ai32 04/05/15 RA - WT NA touch
163B KSt77 M TrKC_CreER;Rosa_Ai32 11/10/14 RA - T NA touch
125B KSt66 M TrKC_CreER;Rosa_Ai32 07/11/14 RA - T NA touch
221B KSt106 F TrKC_CreER;Rosa_Ai32 05/14/15 SA - WT* Y touch
225D KSt107 F TrKC_CreER;Rosa_Ai32 05/14/15 SA - WT* Y touch
132A KSt69 M TrKC_CreER;Rosa_Ai32 07/25/14 SA - WT* Y touch
256B KSt119 M TrKC_CreER;Rosa_Ai32 07/06/15 SA - WT* Y touch
223B KSt101 F TrKC_CreER;Rosa_Ai32 05/11/15 SA - WT Y touch
161A KSt77 M TrKC_CreER;Rosa_Ai32 11/10/14 SA - WT* Y touch
167A KSt82 M TrKC_CreER;Rosa_Ai32 12/08/14 SA - WT* Y touch
128D KSt66 M TrKC_CreER;Rosa_Ai32 07/18/14 SA - WT* NA touch
221C KSt106 F TrKC_CreER;Rosa_Ai32 05/14/15 SA - WT Y touch
198B KSt89 F TrKC_CreER;Rosa_Ai32 03/31/15 SA - WT Y touch
216D KSt97 M CCK_Cre;Rosa_Ai32 04/27/15 SA - T Y touch
211A KSt96 F TrKC_CreER;Rosa_Ai32 04/20/15 SA - T Y touch
220B KSt99 M TrKC_CreER;Rosa_Ai32 05/06/15 SA Y WT* Y touch
286A KSt127 F TrKC_CreER;Rosa_Ai32 09/09/16 SA Y WT* Y touch
250A KSt115 F TrKC_CreER;Rosa_Ai32 06/22/15 SA Y WT* Y touch
251B KSt117 M CCK_Cre;Rosa_Ai32 06/29/15 SA Y WT* Y touch
254C KSt119 M TrKC_CreER;Rosa_Ai32 07/03/15 SA Y WT Y touch
207A KSt91 M TrKC_CreER;Rosa_Ai32 04/13/15 SA Y WT Y touch
154B KSt80 F TrKC_CreER;Rosa_Ai32 10/25/14 SA Y WT Y touch
265A KSt122 M TrKC_CreER;Rosa_Ai32 07/19/15 SA Y WT Y touch
234A KSt111 M TrKC_CreER;Rosa_Ai32 05/29/15 SA Y WT Y touch
231A KSt109 F TrKC_CreER;Rosa_Ai32 05/21/15 SA Y WT* Y touch
243B KSt112 M TrKC_CreER;Rosa_Ai32 06/10/15 SA Y WT Y touch
266B KSt124 F TrKC_CreER;Rosa_Ai32 07/21/15 SA Y WT Y touch
220C KSt99 M TrKC_CreER;Rosa_Ai32 05/06/15 SA Y WT Y touch
282A KSt126 M TrKC_CreER;Rosa_Ai32 08/31/16 SA Y T Y touch
227C KSt107 F TrKC_CreER;Rosa_Ai32 05/15/15 SA Y WT NA excluded
214A KSt94 F TrKC_CreER;Rosa_Ai32 04/24/15 SA Y WT NA excluded
271A KSt123 F TrKC_CreER;Rosa_Ai32 07/29/15 SA Y NA NA excluded
199B KSt89 F TrKC_CreER;Rosa_Ai32 04/01/15 SA Y putativeWT* NA cutonly
206A KSt91 M TrKC_CreER;Rosa_Ai32 04/13/15 SA Y putativeWT* NA cutonly
209A KSt93 M TrKC_CreER;Rosa_Ai32 04/16/15 SA Y putativeWT* NA cutonly
277A KSm31 M Rosa_Ai32 08/24/16 SA - putativeWT* NA cutonly
305A KSt137 M Rosa_Ai32 10/18/16 SA - putativeWT* NA cutonly
240A KSt112 M TrKC_CreER;Rosa_Ai32 06/06/15 SA - putativeWT* NA whiskonly
253A KSt119 M TrKC_CreER;Rosa_Ai32 07/02/15 SA - putativeWT* NA whiskonly
278B KSm30 M Rosa_Ai32 08/31/16 SA - putativeWT* NA progressive
288C KSt128 M TrKC_CreER;Rosa_Ai32 09/13/16 SA - putativeWT* NA progressive
295C KSt131 M TrKC_CreER;Rosa_Ai32 09/23/16 SA - putativeWT* NA progressive
303A KSt137 M Rosa_Ai32 10/15/16 SA - putativeWT* NA progressive
304B KSt137 M Rosa_Ai32 10/17/16 SA - putativeWT* NA progressive
305B KSt137 M Rosa_Ai32 10/18/16 SA - putativeWT* NA progressive
309B KSt135 M TrKC_CreER;Rosa_Ai32 10/24/16 SA - putativeWT* NA progressive
311C KSt135 M TrKC_CreER;Rosa_Ai32 10/27/16 SA - putativeWT* NA progressive
313A KSt138 M TrKC_CreER;Rosa_Ai32 11/20/16 SA - putativeWT* NA progressive
318A KSt140 M TrKC_CreER;Rosa_Ai32 12/01/16 SA - putativeWT* NA progressive
321A KSt140 M TrKC_CreER;Rosa_Ai32 12/05/16 SA - putativeWT* NA progressive
321B KSt140 M TrKC_CreER;Rosa_Ai32 12/05/16 SA - putativeWT* NA progressive
295A KSt130 M TrKC_CreER;Rosa_Ai32 09/23/16 RA - putativeWT* NA progressive
7A KSm6 M Rosa_Ai32 06/02/16 NA - NA NA emg
8A KSm8 M Rosa_Ai32 06/04/16 NA - NA NA emg
9A KSm9 M CCK_CreER;Rosa_Ai32 06/10/16 NA - NA NA emg
11A KSm11 F Rosa_Ai9 06/16/16 NA - NA NA emg
"""


def table_s1():
    """Table S1 as a list of dicts."""
    keys = ["rec", "mouse", "sex", "line", "date", "type", "merkel", "cls", "visco", "group"]
    rows = []
    for line in TABLE_S1.strip().splitlines():
        r = dict(zip(keys, line.split()))
        r["line"] = r["line"].replace("_", " ")
        r["merkel"] = r["merkel"] == "Y"
        rows.append(r)
    return rows


# --- loading ------------------------------------------------------------------------------------

def assets():
    """(path, size, url) of every asset of the pinned version."""
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return sorted((a.path, a.size, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in ds.get_assets())


def _text(f, key):
    if key not in f:
        return None
    v = f[key][()]
    return v.decode() if isinstance(v, bytes) else v


def load(url):
    """Read one NWB file into memory and return its contents as arrays (trials x frames)."""
    content = requests.get(url, timeout=600).content
    f = h5py.File(io.BytesIO(content), "r")
    beh = f["processing/behavior"]
    g0 = beh["BehavioralTimeSeries_position"]
    index = sorted(int(n.split("_")[-1]) for n in g0.keys())
    s = {"identifier": _text(f, "identifier"), "session_start": _text(f, "session_start_time"),
         "subject_id": _text(f, "general/subject/subject_id"), "sex": _text(f, "general/subject/sex"),
         "strain": _text(f, "general/subject/strain"),
         "related_publications": [x.decode() for x in f["general/related_publications"][:]],
         "series_present": sorted(k.replace("BehavioralTimeSeries_", "") for k in beh.keys()),
         "acquisition": list(f["acquisition"].keys()), "bytes": len(content)}
    s["starting_time"] = np.array([g0[f"position_{i}"]["starting_time"][()] for i in index])
    s["rates"] = sorted({float(g0[f"position_{i}"]["starting_time"].attrs["rate"]) for i in index})
    s["lengths"] = sorted({g0[f"position_{i}"]["data"].shape[0] for i in index})
    s["units"] = {}
    for v in VARIABLES:
        name = "BehavioralTimeSeries_" + v
        if name not in beh:
            s[v] = None
            continue
        g = beh[name]
        s[v] = np.stack([g[f"{v}_{i}"]["data"][:].astype(np.float32) for i in index])
        u = g[f"{v}_{index[0]}"]["data"].attrs["unit"]
        s["units"][v] = u.decode() if isinstance(u, bytes) else u
    t = f["intervals/trials"]
    s["trial_start"], s["trial_stop"] = t["start_time"][:], t["stop_time"][:]
    s["MOI"] = t["MOI"][:]
    s["cutting_group"] = [x.decode() for x in t["cuttingGroup"][:]]
    s["trial_columns"] = [c.decode() if isinstance(c, bytes) else c for c in t.attrs["colnames"]]
    if "units" in f:
        s["spike_times"] = f["units/spike_times"][:]
        s["unit_columns"] = list(f["units"].attrs["colnames"])
    else:
        s["spike_times"] = None
    f.close()
    return s


def spike_counts(s):
    """Spikes per 2 ms frame (trials x frames), and the spikes that fall outside the frames."""
    n = len(s["starting_time"])
    counts = np.zeros((n, FRAMES_PER_TRIAL), np.float32)
    st = np.sort(s["spike_times"])
    k = np.searchsorted(s["starting_time"], st, side="right") - 1
    frame = np.floor((st - s["starting_time"][np.clip(k, 0, None)]) * FRAME_HZ).astype(int)
    inside = (k >= 0) & (frame >= 0) & (frame < FRAMES_PER_TRIAL)
    np.add.at(counts, (k[inside], frame[inside]), 1)
    in_trial = (k >= 0) & (st < s["trial_stop"][np.clip(k, 0, None)])
    return counts, {"in_frames": int(inside.sum()), "in_trial_after_frames": int((in_trial & ~inside).sum()),
                    "outside_trials": int((~in_trial).sum())}


# --- categories and measures --------------------------------------------------------------------

def categories(s):
    """Boolean frame masks of the Glossary's behavioural categories."""
    amp = s["amplitude"]
    dpole = s["distanceToPoleCenter"]
    if dpole is None:
        dpole = np.full_like(amp, np.inf)
    dpole = np.where(np.isfinite(dpole), dpole, np.inf)
    contact_flag = s["contact"] == 1
    contact = contact_flag & (dpole < 1)
    whisking = amp > 2.5
    return {"contact": contact & whisking,                     # contact without whisking is left out
            "wia": whisking & ~contact_flag & (dpole > 2),
            "nonwhisking": (amp < 1) & ~contact & (dpole > 2),
            "whisking": whisking}


def outlier_free(s, mask, variables):
    """`mask` without frames that are outliers (Glossary) on any of `variables`."""
    keep = mask.copy()
    for v in variables:
        x = s[v]
        lo, hi = (0.5, 99.5) if v in DYNAMIC else (0.25, 99.75)
        vals = x[mask & np.isfinite(x)]
        if len(vals) == 0:
            return np.zeros_like(mask)
        a, b = np.percentile(vals, [lo, hi])
        keep &= np.isfinite(x) & (x >= a) & (x <= b)
    return keep


def category_rates(counts, masks, rng, n_boot=1000):
    """Mean rate (Hz) per category, with a 95% bootstrap CI over trials and a Poisson CI."""
    from scipy.stats import chi2
    out = {}
    for name, m in masks.items():
        spikes = (counts * m).sum(1)
        frames = m.sum(1).astype(float)
        if frames.sum() == 0:
            out[name] = {"rate": np.nan, "lo": np.nan, "hi": np.nan, "seconds": 0.0, "spikes": 0}
            continue
        rate = spikes.sum() / (frames.sum() * DT)
        idx = rng.integers(0, len(frames), (n_boot, len(frames)))
        bf = frames[idx].sum(1)
        boot = spikes[idx].sum(1) / np.where(bf > 0, bf * DT, np.nan)
        lo, hi = np.nanpercentile(boot, [2.5, 97.5])
        k, t = spikes.sum(), frames.sum() * DT
        plo = chi2.ppf(0.025, 2 * k) / 2 / t if k > 0 else 0.0
        phi = chi2.ppf(0.975, 2 * k + 2) / 2 / t
        out[name] = {"rate": rate, "lo": lo, "hi": hi, "plo": plo, "phi": phi,
                     "seconds": float(t), "spikes": int(k)}
    return out


def classify(r, ci=("lo", "hi"), min_spikes=1000, spikes_key="total_spikes"):
    """T, WT, WT* or none by the Glossary, from category_rates output `r` (with total spikes)."""
    lo, hi = ci
    c, w, n = r["contact"], r["wia"], r["nonwhisking"]
    touch = (c["rate"] > w["rate"]) and (c["rate"] > n["rate"]) and c[lo] > w[hi] and c[lo] > n[hi]
    whisk = (w[lo] > n[hi]) or (w[hi] < n[lo])
    if not touch:
        return "none"
    if not whisk:
        return "T"
    if w["rate"] > 1 and r[spikes_key] >= min_spikes:
        return "WT*"
    return "WT"


def equal_count_edges(x, n_bins=30):
    return np.quantile(x, np.linspace(0, 1, n_bins + 1))


def phase_tuning(phase, counts, n_bins=30):
    """Rates (Hz) in n_bins phase bins with equal numbers of frames, and the bin centres."""
    edges = equal_count_edges(phase, n_bins)
    b = np.clip(np.searchsorted(edges, phase, side="right") - 1, 0, n_bins - 1)
    spikes = np.bincount(b, weights=counts, minlength=n_bins)
    frames = np.bincount(b, minlength=n_bins)
    centres = np.array([np.median(phase[b == i]) for i in range(n_bins)])
    return spikes / np.maximum(frames, 1) / DT, centres, b


def bin_means(values, b, n_bins=30):
    return np.bincount(b, weights=values, minlength=n_bins) / np.maximum(np.bincount(b, minlength=n_bins), 1)


def circ_diff(a, b):
    return np.abs(np.angle(np.exp(1j * (a - b))))


def contact_episodes(s, counts, contact):
    """Each run of contact frames within a trial: mean M0, spikes and frames."""
    rows = []
    for i in range(contact.shape[0]):
        m = contact[i].astype(np.int8)
        d = np.diff(np.concatenate([[0], m, [0]]))
        starts, stops = np.flatnonzero(d == 1), np.flatnonzero(d == -1)
        for a, b in zip(starts, stops):
            m0 = s["M0"][i, a:b]
            rows.append((np.nanmean(m0) if np.isfinite(m0).any() else np.nan,
                         counts[i, a:b].sum(), b - a, s["velocity"][i, a]))
    return np.array(rows, dtype=float).reshape(-1, 4)


def derivative_ratios(s, masks):
    """Median ratio of each stored derivative to the change of its variable per 2 ms frame.
    A ratio near 0.5 means the derivative is per ms; near 500, per s."""
    out = {}
    for d, v, m in (("velocity", "position", masks["whisking"]), ("acceleration", "velocity", masks["whisking"]),
                    ("jerk", "acceleration", masks["whisking"]), ("dM0", "M0", masks["contact"]),
                    ("dFaxial", "Faxial", masks["contact"]), ("dFlateral", "Flateral", masks["contact"])):
        if s[d] is None or not m.any():
            continue
        g = np.gradient(s[v], axis=1)
        ok = m & np.isfinite(g) & np.isfinite(s[d])
        if ok.sum() < 100:
            continue
        ok &= np.abs(g) > np.median(np.abs(g[ok]))
        out[d] = float(np.median(s[d][ok] / g[ok]))
    return out


def phase_direction(s, masks, n_trials=20):
    """Correlation of sin(stored phase) with sin(Hilbert phase of 8 to 30 Hz band-passed position),
    over whisking frames of the first trials. +1: the stored phase advances with time; -1: it runs
    backwards."""
    b, a = butter(2, [8 / 250, 30 / 250], "band")
    x, y = [], []
    for i in range(min(n_trials, s["position"].shape[0])):
        th = s["position"][i]
        if not np.isfinite(th).all():
            continue
        ph = np.angle(hilbert(filtfilt(b, a, th)))
        m = masks["whisking"][i] & np.isfinite(s["phase"][i])
        x.append(np.sin(ph[m]))
        y.append(np.sin(s["phase"][i][m]))
    if not x or sum(len(v) for v in x) < 100:
        return np.nan
    return float(np.corrcoef(np.concatenate(x), np.concatenate(y))[0, 1])


def file_signature(s):
    """Hashes for finding recordings deposited twice."""
    pos = np.nan_to_num(s["position"][:5]).tobytes()
    spk = b"" if s["spike_times"] is None else np.sort(s["spike_times"]).tobytes()
    return hashlib.md5(pos).hexdigest(), hashlib.md5(spk).hexdigest()


# --- spline models ------------------------------------------------------------------------------

def bspline_basis(x, lo, hi, n_basis=10, degree=3):
    """Cubic B-spline basis with n_basis functions and equally spaced knots on [lo, hi]."""
    inner = np.linspace(lo, hi, n_basis - degree + 1)
    knots = np.concatenate([[lo] * degree, inner, [hi] * degree])
    xc = np.clip(x, lo, hi - 1e-12 * max(abs(hi), 1))
    return BSpline.design_matrix(xc, knots, degree).toarray()


class SplineModel:
    """Additive model: one cubic B-spline per variable, penalized binomial IRLS (logit link).

    Each 2 ms frame is treated as two 1 ms Bernoulli trials (y = spike count, capped at 2), so p is
    the spike probability per ms as in the paper's 1 ms GAMs. Second-difference penalty `lam` on each
    variable's coefficients, and a small ridge (0.01) to fix the level of each spline against the
    intercept. Newton steps are halved until the penalized deviance does not increase.
    """

    def __init__(self, n_basis=10, lam=1.0, ridge=1e-2, max_iter=50, tol=1e-7):
        self.n_basis, self.lam, self.ridge, self.max_iter, self.tol = n_basis, lam, ridge, max_iter, tol

    def _design(self, X):
        cols = [np.ones((X.shape[0], 1))]
        for j, (lo, hi) in enumerate(self.ranges):
            cols.append(bspline_basis(X[:, j], lo, hi, self.n_basis))
        return np.hstack(cols)

    def fit(self, X, y):
        self.ranges = [(float(np.min(X[:, j])), float(np.max(X[:, j])) + 1e-9) for j in range(X.shape[1])]
        B = self._design(X)
        nv, nb = X.shape[1], self.n_basis
        D = np.diff(np.eye(nb), 2, axis=0)
        P = np.zeros((B.shape[1], B.shape[1]))
        for j in range(nv):
            sl = slice(1 + j * nb, 1 + (j + 1) * nb)
            P[sl, sl] = self.lam * D.T @ D + self.ridge * np.eye(nb)
        y = np.minimum(y, 2.0)
        m = 2.0

        def deviance(beta):
            eta = np.clip(B @ beta, -30, 30)
            p = 1 / (1 + np.exp(-eta))
            ll = y * np.log(np.maximum(p, 1e-300)) + (m - y) * np.log(np.maximum(1 - p, 1e-300))
            return -2 * ll.sum() + beta @ P @ beta, p

        p0 = np.clip(y.mean() / m, 1e-6, 1 - 1e-6)
        beta = np.zeros(B.shape[1])
        beta[0] = np.log(p0 / (1 - p0))
        dev, p = deviance(beta)
        self.converged = False
        for self.n_iter in range(1, self.max_iter + 1):
            eta = B @ beta
            w = np.maximum(m * p * (1 - p), 1e-10)
            z = eta + (y - m * p) / w
            A = B.T @ (B * w[:, None]) + P
            proposal = np.linalg.solve(A, B.T @ (w * z))
            step = 1.0
            while True:                      # step halving: the penalized deviance must not increase
                cand = beta + step * (proposal - beta)
                dev_new, p_new = deviance(cand)
                if dev_new <= dev or step < 1e-4:
                    break
                step /= 2
            change = dev - dev_new
            beta, dev, p = cand, dev_new, p_new
            if 0 <= change < self.tol * max(abs(dev), 1):
                self.converged = True
                break
        self.beta = beta
        return self

    def predict(self, X):
        """Spike probability per 1 ms bin."""
        return 1 / (1 + np.exp(-np.clip(self._design(X) @ self.beta, -30, 30)))


def fit_r(X, y, smooth, **kw):
    """Fit a SplineModel and return (Pearson r of prediction with smoothed spikes, model)."""
    model = SplineModel(**kw).fit(X, y)
    pred = model.predict(X)
    if np.std(pred) == 0 or np.std(smooth) == 0:
        return np.nan, model
    return float(np.corrcoef(pred, smooth)[0, 1]), model


# --- viscoelastic model -------------------------------------------------------------------------

def visco_predict(params, x, xdot):
    """Predicted rate (Hz) from scaled moment x and its rate of change xdot (per s), Eqs. M1 to M4."""
    k, c, eps_lim, E, eta = params
    u = np.clip(-k * x + c, -50, 50)
    eu = np.exp(u)
    eps = 2 / (1 + eu) - 1
    deps_dx = 2 * k * eu / (1 + eu) ** 2
    eps_spring = np.clip(eps, -eps_lim, eps_lim)
    sigma = E * eps_spring + eta * deps_dx * xdot
    return np.clip(1000.0 * sigma, 0, 1000.0)


def fit_visco(m0, dm0, rate, rng, n_starts=8):
    """Least-squares fit of the five parameters (k, C, eps_lim, E, eta); M0 scaled by its 80th
    percentile of |M0|. dm0 is in N m per second. For a well-conditioned fit, the rate of change is
    also divided by the 80th percentile of its absolute value, and eta is fitted in those units and
    converted back. Returns (params, loss, success, scale), with eta per second."""
    scale = np.percentile(np.abs(m0), 80)
    x, xdot = m0 / scale, dm0 / scale
    sdot = np.percentile(np.abs(xdot), 80)
    u = xdot / sdot

    def loss(p):
        return np.mean((visco_predict(p, x, u) - rate) ** 2)
    bounds = [(-100, 100), (-20, 20), (1e-3, 1.0), (0, 100), (0, 100)]
    best = None
    starts = [(2, 0, 0.5, 0.5, 0.5), (-2, 0, 0.5, 0.5, 0.5)]
    while len(starts) < n_starts:
        starts.append((rng.uniform(-10, 10), rng.uniform(-3, 3), rng.uniform(0.05, 1),
                       10 ** rng.uniform(-2, 1), 10 ** rng.uniform(-2, 1)))
    for p0 in starts:
        res = optimize.minimize(loss, p0, method="L-BFGS-B", bounds=bounds)
        if best is None or res.fun < best.fun:
            best = res
    k, c, eps_lim, E, eta_u = best.x
    return np.array([k, c, eps_lim, E, eta_u / sdot]), float(best.fun), bool(best.success), scale


# --- per-recording reduction --------------------------------------------------------------------

def reduce(path, url, seed, keep_touch=False, keep_wia=False, n_fit=60000, n_wia_keep=400000):
    """Load one file and reduce it to what the notebook uses."""
    s = load(url)
    rng = np.random.default_rng(seed)
    n_trials = len(s["starting_time"])
    r = {"path": path, "identifier": s["identifier"], "subject_id": s["subject_id"], "sex": s["sex"],
         "strain": s["strain"], "session_start": s["session_start"], "n_trials": n_trials,
         "related_publications": s["related_publications"], "series_present": s["series_present"],
         "acquisition": s["acquisition"], "units": s["units"], "bytes": s["bytes"],
         "rates": s["rates"], "lengths": s["lengths"],
         "trial_duration": (float(np.min(s["trial_stop"] - s["trial_start"])),
                            float(np.max(s["trial_stop"] - s["trial_start"]))),
         "start_offset": float(np.max(np.abs(s["starting_time"] - s["trial_start"]))),
         "MOI_values": sorted({float(x) for x in s["MOI"] if np.isfinite(x)}),
         "MOI_nan": int(np.isnan(s["MOI"]).sum()),
         "cutting_groups": sorted(set(s["cutting_group"])), "trial_columns": s["trial_columns"],
         "signature": file_signature(s), "has_spikes": s["spike_times"] is not None}
    r["ranges"] = {v: (float(np.nanmin(s[v])), float(np.nanmax(s[v])), float(np.isfinite(s[v]).mean()))
                   for v in VARIABLES if s[v] is not None}
    masks = categories(s)
    r["category_seconds"] = {k: float(m.sum() * DT) for k, m in masks.items()}
    r["derivative_ratios"] = derivative_ratios(s, masks)
    r["phase_direction"] = phase_direction(s, masks)
    if s["distanceToPoleCenter"] is not None and (s["contact"] == 1).any():
        d = s["distanceToPoleCenter"][(s["contact"] == 1) & np.isfinite(s["distanceToPoleCenter"])]
        r["dpole_contact_pct"] = np.percentile(d, [1, 50, 99]).tolist()
        d = s["distanceToPoleCenter"][(s["contact"] == 0) & np.isfinite(s["distanceToPoleCenter"])]
        r["dpole_free_pct"] = np.percentile(d, [1, 50, 99]).tolist() if len(d) else None
    # Curvature noise (sigma kappa).
    dk = np.abs(s["deltaKappa"])
    dpole = s["distanceToPoleCenter"]
    dpole = np.full_like(dk, np.inf) if dpole is None else np.where(np.isfinite(dpole), dpole, np.inf)
    air = (dpole > 1) & (s["amplitude"] > 2.5) & np.isfinite(dk)
    con_a = (s["contact"] == 1) & (dpole < 1) & np.isfinite(dk)
    con_b = (s["contact"] == 1) & np.isfinite(dk)
    r["sigma_kappa"] = {"a": 100 * dk[air].mean() / dk[con_a].mean() if con_a.any() and air.any() else np.nan,
                        "b": 100 * dk[air].mean() / dk[con_b].mean() if con_b.any() and air.any() else np.nan}
    # Whisking frames: velocity by phase (for the EMG recording).
    wh = masks["whisking"] & np.isfinite(s["phase"]) & np.isfinite(s["velocity"])
    if wh.sum() > 3000:
        edges = np.linspace(-np.pi, np.pi, 13)
        b = np.clip(np.digitize(s["phase"][wh], edges) - 1, 0, 11)
        r["kinematics_by_phase"] = {"centres": (edges[:-1] + edges[1:]) / 2,
                                    "position": bin_means(s["position"][wh] - np.nanmean(s["position"][wh]), b, 12),
                                    "velocity": bin_means(s["velocity"][wh], b, 12)}
    if not r["has_spikes"]:
        return r
    st = s["spike_times"]
    r["n_spikes"] = len(st)
    r["spikes_sorted"] = bool(np.all(np.diff(st) >= 0))
    counts, where = spike_counts(s)
    r["spike_placement"] = where
    r["category_rates"] = category_rates(counts, {k: masks[k] for k in ("contact", "wia", "nonwhisking")}, rng)
    r["total_spikes"] = int(counts.sum())
    wia_s = (counts * masks["wia"]).sum(1)
    wia_f = masks["wia"].sum(1)
    r["wia_rate_fifths"] = [float(a.sum() / max(b.sum() * DT, 1e-9)) for a, b in
                            zip(np.array_split(wia_s, 5), np.array_split(wia_f, 5))]
    r["wia_spikes"] = int(counts[masks["wia"]].sum())
    # Clock contrast: responses with spikes shifted by 0.5 s within each trial.
    shifted = np.roll(counts, 250, axis=1)
    def contrast(c):
        cr = c[masks["contact"]].mean() / DT if masks["contact"].any() else np.nan
        wr = c[masks["wia"]].mean() / DT if masks["wia"].any() else np.nan
        ph = s["phase"][masks["wia"]]
        tc = phase_tuning(ph, c[masks["wia"]])[0] if masks["wia"].sum() > 3000 else np.array([np.nan])
        return {"contact_minus_wia": cr - wr, "phase_depth": float(np.nanmax(tc) - np.nanmin(tc)),
                "wia_rate": wr}
    r["clock"] = {"true": contrast(counts), "shifted": contrast(shifted)}
    # Phase tuning in whisking in air, and in halves split by amplitude, frequency and setpoint.
    wia = masks["wia"] & np.isfinite(s["phase"])
    if wia.sum() > 3000:
        tc, centres, b = phase_tuning(s["phase"][wia], counts[wia])
        r["phase_tuning"] = (tc, centres)
        r["velocity_by_tuning_bin"] = bin_means(np.nan_to_num(s["velocity"][wia]), b)
        halves = {}
        for v in ("amplitude", "frequency", "setpoint"):
            x = s[v][wia]
            ok = np.isfinite(x)
            med = np.median(x[ok])
            prefs = []
            for part in (ok & (x <= med), ok & (x > med)):
                t2, c2, _ = phase_tuning(s["phase"][wia][part], counts[wia][part])
                prefs.append(float(c2[np.argmax(t2)]))
            halves[v] = prefs
        r["phase_halves"] = halves
    # Whisking frames by phase, for the EMG recording: spike rate, positive and negative velocity.
    if wh.sum() > 3000:
        tcw, cw, bw = phase_tuning(s["phase"][wh], counts[wh])
        vel = s["velocity"][wh]
        r["whisk_phase_curves"] = {"rate": tcw, "centres": cw,
                                   "vel_pos": bin_means(np.maximum(vel, 0), bw),
                                   "vel_neg": bin_means(np.maximum(-vel, 0), bw)}
    smooth = np.stack([gaussian_filter1d(c, 2.0, mode="constant") for c in counts])  # sigma 4 ms
    if keep_touch and s["M0"] is not None:
        con = outlier_free(s, masks["contact"], TOUCH_VARS)
        r["contact_frames_clean"] = int(con.sum())
        idx = np.flatnonzero(con.ravel())
        if len(idx) > n_fit:
            idx = np.sort(rng.choice(idx, n_fit, replace=False))
        r["touch"] = {"X": np.column_stack([s[v].ravel()[idx] for v in TOUCH_VARS]).astype(np.float64),
                      "y": counts.ravel()[idx].astype(np.float64),
                      "smooth": smooth.ravel()[idx].astype(np.float64)}
        r["episodes"] = contact_episodes(s, counts, masks["contact"])
    if keep_wia:
        w = outlier_free(s, masks["wia"] & np.isfinite(s["phase"]), KINEMATIC_VARS)
        idx = np.flatnonzero(w.ravel())
        if len(idx) > n_wia_keep:
            idx = np.sort(rng.choice(idx, n_wia_keep, replace=False))
        r["wia_frames"] = {"X": np.column_stack([s[v].ravel()[idx] for v in KINEMATIC_VARS]).astype(np.float64),
                           "phase": s["phase"].ravel()[idx].astype(np.float64),
                           "y": counts.ravel()[idx].astype(np.float64)}
    return r


def model_subsets(variables, size):
    return list(itertools.combinations(variables, size))
