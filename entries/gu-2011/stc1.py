"""Loading and measures for CRCNS stc-1, MSTd pairs, for Gu et al. (2011), Neuron 71:750-761.

Gu, Liu, Fetsch, Yang, Fok, Sunkara, DeAngelis & Angelaki (2011), "Perceptual Learning Reduces
Interneuronal Correlations in Macaque Visual Cortex", doi:10.1016/j.neuron.2011.06.015.

The data set (doi:10.6080/K07P8WKF) is not versioned on CRCNS; it is read as `unversioned` from
the public bucket `crcnsarchive` under stc-1/live/, and each file is checked against the MD5 sum
in the data set's checksums.md5, so that a later change is detected. Files are streamed into
memory; nothing is written to disk.

MSTd.mat holds three structures (data descriptor, version 0.6). `experiment3.pairs` holds, per
pair and per condition (`ves`, `vis`), the signal correlation, the noise correlation and the
preferred headings of the two units, with the `file_id` of the recording (for example
`m17c26r1`, monkey 17). `experiment1.units` holds trial-averaged heading tuning curves and
`experiment2.units` the choice probability and neuronal threshold of 129 single units from
monkeys 2 and 5 (Gu et al. 2008).

Where the parameters come from:

- Training groups. The data set does not say which monkey is naive or trained. The paper gives
  the pairs per animal under 1 mm (Figure S2B legend: trained 35, 26, 18 and 8, and one trained
  animal with two pairs; naive 22, 11 and 5). `PAPER_PAIRS_PER_ANIMAL` holds these counts and
  `assign_groups` matches the monkeys to them by count (the link claim).
- Pooled noise correlation. The paper's main measure pools z-scored responses across the two
  conditions (Experimental Procedures, Noise and Signal Correlations, paragraph 2); the data set
  holds only the per-condition values. Since z-scoring per heading gives each condition's
  responses unit variance, the Pearson correlation of the pooled z-scores is the trial-weighted
  mean of the two per-condition correlations; with conditions interleaved and the same
  repetitions (Experimental Procedures, Experimental Protocol and Task), the weights are equal.
  `pooled_rnoise` is therefore the mean of the two values. This is an assumption: outliers
  removed differently in the two conditions would make the weights differ slightly.
- Type II regression (orthogonal distance) for the plane of equation 5: Experimental Procedures,
  Population Coding, last sentence.
- The simulations follow equations 2 to 5 of the Experimental Procedures and the Figure 6A
  legend (wrapped-Gaussian tuning, bandwidth 135 degrees, preferences uniform, reference heading
  0). Amplitude 30 spikes/s on a baseline of 10 spikes/s, counted over 1 s, and bandwidth as full
  width at half height, are the readings the claims file names (fig6a-population-thresholds);
  they are not from the paper. Preferences evenly spaced over the range is a standard choice.
  `RSIGNAL_HEADINGS_8` (8 headings 45 degrees apart) and a 1-degree grid are the two rsignal
  readings of the claims file.
- Preferred heading from a tuning curve (fig4dh, fig8ab): the vector sum, or the peak of a
  periodic cubic spline through the curve at 1 degree; the two readings of the claims file
  (fig4dh-lateral-more-sensitive). The experiment 1 headings are unevenly spaced (+-22.5 degrees
  added to the eight 45 degrees apart), so each response in the vector sum is weighted by the
  angle it covers (half the gaps to its two neighbours); an unweighted sum is pulled toward
  straight ahead (a choice made here, after the round-1 verification found that bias).
- Single-neuron threshold (fig4dh): equations 2 and 3 for one neuron, with variance equal to the
  mean (equation 4 for i = j), so that I = f'^2 / f + 0.5 (f' / f)^2, on the tuning curve in
  spikes/s read as the count of the middle 1 s (Experimental Procedures, Noise and Signal
  Correlations). The two interpolations are the claims file's readings. For the linear one, f'
  at 0, a sampled heading, is the slope between the two neighbouring headings (-22.5 and 22.5),
  a choice made here since a piecewise-linear curve has no derivative at a knot.
- Fore-aft and lateral groups: within 45 degrees of 0 or 180, or of -90 or 90 (Results, Effects
  of Training on Tuning Curves, paragraph 3). A preference at exactly 45 degrees from both is
  counted as lateral, a standard choice that affects no value in these data.
"""

from __future__ import annotations

import hashlib
import io
import re

import fsspec
import numpy as np
import pandas as pd
import scipy.io as sio
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq

DATASET_ID = "stc-1"
DATASET_VERSION = "unversioned"
DATASET_DOI = "10.6080/K07P8WKF"
BASE_URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/stc-1/live"
# MD5 sums from stc-1/live/checksums.md5, read on 2026-11-06.
MD5 = {"MSTd.mat": "cd4c13b360aa05689015f1bd2b88a05a", "VIP.mat": "8d7924e0a1ae86c56b78cd1e2f530e2d"}

# Figure S2B legend: pairs under 1 mm per animal.
PAPER_PAIRS_PER_ANIMAL = {"trained": [35, 26, 18, 8, 2], "naive": [22, 11, 5]}


def read_bytes(name: str) -> bytes:
    """Stream a file of the data set into memory and check its MD5 sum."""
    with fsspec.open(f"{BASE_URL}/{name}", "rb", block_size=2**20) as f:
        data = f.read()
    digest = hashlib.md5(data).hexdigest()
    if name in MD5 and digest != MD5[name]:
        raise ValueError(f"{name}: MD5 {digest} differs from checksums.md5 ({MD5[name]})")
    return data


def checksums() -> dict[str, str]:
    """The data set's checksums.md5, as published now."""
    text = read_bytes("checksums.md5").decode()
    return {line.split()[1]: line.split()[0] for line in text.splitlines() if line.strip()}


def load_mat(name: str = "MSTd.mat"):
    return sio.loadmat(io.BytesIO(read_bytes(name)), squeeze_me=True, struct_as_record=False)


def monkey_of(file_id: str) -> int:
    return int(re.match(r"m(\d+)c", file_id).group(1))


def pairs_table(mat) -> pd.DataFrame:
    """One row per pair of experiment3: monkey, recording, rsignal, rnoise, preferences."""
    rows = []
    for i, q in enumerate(np.atleast_1d(mat["experiment3"].pairs)):
        row = {"pair": i, "file_id": q.file_id, "monkey": monkey_of(q.file_id)}
        for cond in ("ves", "vis"):
            c = getattr(q, cond)
            row[f"rsig_{cond}"] = float(c.corr_signal)
            row[f"rnoise_{cond}"] = float(c.corr_noise)
            row[f"pref1_{cond}"], row[f"pref2_{cond}"] = (float(x) for x in c.heading_pref)
        rows.append(row)
    return pd.DataFrame(rows)


def assign_groups(counts: pd.Series) -> dict[int, str]:
    """Match monkeys to the paper's per-animal pair counts. Returns {} when the match is not unique."""
    wanted = {n: g for g, ns in PAPER_PAIRS_PER_ANIMAL.items() for n in ns}
    if len(wanted) != sum(len(v) for v in PAPER_PAIRS_PER_ANIMAL.values()):
        return {}
    if sorted(counts.values) != sorted(wanted):
        return {}
    return {int(m): wanted[int(n)] for m, n in counts.items()}


def pooled_rnoise(df: pd.DataFrame) -> pd.Series:
    """Noise correlation pooled across conditions: the mean of the two (see module docstring)."""
    return (df["rnoise_ves"] + df["rnoise_vis"]) / 2


def neurons_per_recording(df: pd.DataFrame) -> pd.Series:
    """Distinct units per recording, matching units across its pairs by both preferred headings."""
    out = {}
    for fid, g in df.groupby("file_id"):
        units = set()
        for _, r in g.iterrows():
            for k in ("1", "2"):
                units.add((round(r[f"pref{k}_ves"], 3), round(r[f"pref{k}_vis"], 3)))
        out[fid] = len(units)
    return pd.Series(out)


def unit_table(df: pd.DataFrame) -> pd.DataFrame:
    """Each pair entered twice, once at each unit's preferred heading (Figure 8C legend)."""
    rows = []
    for _, r in df.iterrows():
        for k in ("1", "2"):
            rows.append({"pair": r["pair"], "monkey": r["monkey"], "group": r.get("group"),
                         "pref_ves": r[f"pref{k}_ves"], "pref_vis": r[f"pref{k}_vis"],
                         "rnoise": r["rnoise_pooled"]})
    return pd.DataFrame(rows)


def wrap180(a):
    return (np.asarray(a, float) + 180.0) % 360.0 - 180.0


def preference_group(pref):
    """'fore-aft' within 45 degrees of 0 or 180, else 'lateral'."""
    d = np.abs(wrap180(pref))
    fore_aft = (d < 45) | (d > 135)
    return np.where(fore_aft, "fore-aft", "lateral")


def _sorted_circle(headings, resp):
    h = np.asarray(headings, float) % 360.0
    order = np.argsort(h)
    h, r = h[order], np.asarray(resp, float)[order]
    h, idx = np.unique(h, return_index=True)
    return h, r[idx]


def pref_vector_sum(headings, resp) -> float:
    """Vector sum, each response weighted by half the gaps to its two neighbouring headings."""
    h, r = _sorted_circle(headings, resp)
    gap = np.diff(np.append(h, h[0] + 360.0))
    w = r * (gap + np.roll(gap, 1)) / 2
    hr = np.deg2rad(h)
    return float(np.rad2deg(np.arctan2((w * np.sin(hr)).sum(), (w * np.cos(hr)).sum())))


def pref_spline_peak(headings, resp) -> float:
    h, r = _sorted_circle(headings, resp)
    cs = CubicSpline(np.append(h, h[0] + 360.0), np.append(r, r[0]), bc_type="periodic")
    grid = np.arange(0.0, 360.0, 1.0)
    return float(wrap180(grid[np.argmax(cs(grid))]))


def neuron_threshold(headings, resp, interp: str = "spline", window: float = 1.0) -> float:
    """Threshold (degrees) of one neuron at straight ahead, equations 2 and 3 with variance = mean.

    interp "spline" (periodic cubic spline) or "linear" (slope between the neighbours of 0).
    resp in spikes/s, counted over `window` seconds. Infinite when the curve is flat at 0.
    """
    resp = np.asarray(resp, float) * window
    h, r = _sorted_circle(headings, resp)
    if interp == "spline":
        cs = CubicSpline(np.append(h, h[0] + 360.0), np.append(r, r[0]), bc_type="periodic")
        f, fp = float(cs(0.0)), float(cs(0.0, 1))
    else:
        if h[0] != 0.0:
            raise ValueError("the linear reading needs a response at 0 degrees")
        f, fp = r[0], (r[1] - r[-1]) / (h[1] - h[-1] + 360.0)
    info = fp**2 / f + 0.5 * (fp / f) ** 2
    return float(np.sqrt(2.0) / np.sqrt(info)) if info > 0 else np.inf


def tls_plane(X: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, float]:
    """Type II (orthogonal distance) fit of y = X @ coef + intercept."""
    Z = np.column_stack([X, y])
    mu = Z.mean(0)
    normal = np.linalg.svd(Z - mu)[2][-1]
    coef = -normal[:-1] / normal[-1]
    return coef, float(mu[-1] - mu[:-1] @ coef)


# --- Simulations (equations 2 to 5) ---------------------------------------------------------

AMPLITUDE = 30.0     # spikes/s, claims file reading, not from the paper
BASELINE = 10.0      # spikes/s, claims file reading, not from the paper
WINDOW_S = 1.0       # counting window, the middle 1 s (Experimental Procedures)
BANDWIDTH = 135.0    # degrees, Figure 6A legend, read as full width at half height
RSIGNAL_HEADINGS_8 = np.arange(0.0, 360.0, 45.0)
RSIGNAL_HEADINGS_CONT = np.arange(0.0, 360.0, 1.0)
NAIVE = (0.12, 0.091, 0.072)     # equation 5 coefficients for naive animals (Results)
TRAINED = (0.12, 0.091, 0.005)   # and for trained animals


def _wrapped_gaussian(theta, pref, sigma):
    d = np.deg2rad(np.asarray(theta, float)[None, :] - np.asarray(pref, float)[:, None])
    k = 2 * np.pi * np.arange(-3, 4)
    return np.exp(-((d[..., None] + k) ** 2) / (2 * np.deg2rad(sigma) ** 2)).sum(-1)


def sigma_for_fwhm(fwhm: float) -> float:
    """Sigma (degrees) of the wrapped Gaussian whose modulation has the given full width at half height."""
    def half(s):
        g = _wrapped_gaussian([0.0, fwhm / 2, 180.0], [0.0], s)[0]
        return (g[1] - g[2]) / (g[0] - g[2]) - 0.5
    return brentq(half, 5.0, 200.0)


SIGMA = sigma_for_fwhm(BANDWIDTH)


def tuning(prefs, theta, amplitude=AMPLITUDE, baseline=BASELINE):
    """Mean spike count in the window, shape (neurons, headings)."""
    return WINDOW_S * (baseline + amplitude * _wrapped_gaussian(np.atleast_1d(theta), prefs, SIGMA))


def signal_corr(prefs, headings):
    return np.corrcoef(tuning(prefs, headings))


def threshold(prefs, coefs=None, headings=RSIGNAL_HEADINGS_8, x_ref=0.0,
              amplitude=AMPLITUDE, baseline=BASELINE, trace=True) -> float:
    """Discrimination threshold (degrees), equations 2 to 5; coefs None is independent noise.

    coefs = (a_vestibular, a_visual, b). With congruent tuning both signal correlations equal the
    one of the shared tuning curve, so r = (a_vestibular + a_visual) * rsignal + b.
    """
    prefs = np.asarray(prefs, float)
    f = tuning(prefs, x_ref, amplitude, baseline)[:, 0]
    h = 1e-3
    fp = (tuning(prefs, x_ref + h, amplitude, baseline)[:, 0]
          - tuning(prefs, x_ref - h, amplitude, baseline)[:, 0]) / (2 * h)
    if coefs is None:
        R = np.eye(len(prefs))
    else:
        a_ves, a_vis, b = coefs
        R = (a_ves + a_vis) * signal_corr(prefs, headings) + b
        np.fill_diagonal(R, 1.0)
    s = np.sqrt(f)
    Q = R * np.outer(s, s)
    Qp = R * (np.outer(fp, f) + np.outer(f, fp)) / (2 * np.outer(s, s))
    Qi = np.linalg.inv(Q)
    info = fp @ Qi @ fp
    if trace:
        M = Qp @ Qi
        info += 0.5 * np.sum(M * M.T)
    return float(np.sqrt(2.0) / np.sqrt(info))


def uniform_prefs(n, lo=-180.0, hi=180.0):
    """n preferences evenly spaced over [lo, hi] (the full circle excludes the repeated end)."""
    return np.linspace(lo, hi, n, endpoint=(hi - lo) < 360.0)
