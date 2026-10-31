"""Whole-brain activity of the NeuroPAL paper, read from its Zenodo record (data: elsewhere).

Yemini et al. (2021), Cell 184:272-288, doi:10.1016/j.cell.2020.12.012. The record
doi:10.5281/zenodo.3906530 (one zip, "NeuroPAL data.zip") holds Head_Activity_OH16230.mat (21 heads)
and Tail_Activity_OH16230.mat (21 tails). The members are read from the zip over HTTP range
requests into memory; nothing is written to disk.

File layout (the record's README): per neuron class, 42 trace slots, 21 left then 21 right, each
ordered by file (an empty slot when the neuron was not recorded); `fps` (4 Hz heads, 3.87 Hz
tails); `stim_names`; `stim_times` (start, end in s); `stims` (per file, the stimulus order).

Where the parameters come from (STAR Methods, "Analysis of brainwide imaging data", unless said
otherwise):
- Histogram-normalised traces (`norm_traces`): "we used dNMF to normalize activity traces per
  neuron class" (STAR Methods) and the README recommends them.
- Response: mean during the 10 s stimulus against "an identical period immediately prior",
  two-tailed paired t test, q-values of Storey (2002) at 0.05; left and right pooled.
- Premotor interneurons (AVA, AVB, AVD, AVE, PVC) and ventral-cord motor neurons (AS, DA, DB, DD,
  VA, VB, VC, VD) are excluded from testing.
- Neurons within 5 um of each other whose traces correlate at 0.95 or more are removed (STAR
  Methods; the README says they are kept in the files). Both members of such a pair are removed,
  as the text does not say which one was kept: a choice that removes few traces.
- Post-stimulus: stimulus mean above the pre-stimulus mean, then post-stimulus mean above the
  stimulus mean by a one-tailed paired t test, FDR corrected. The post-stimulus window is taken as
  the 10 s after the stimulus, the length of the stimulus (the text does not give it).
- Asymmetry: two-tailed two-sample t test between left and right responses.
"""

from __future__ import annotations

import io
import re
import zipfile

import fsspec
import numpy as np
import scipy.io as sio
from scipy import stats

ZENODO_DOI = "10.5281/zenodo.3906530"
ZENODO_ZIP = "https://zenodo.org/records/3906530/files/NeuroPAL%20data.zip?download=1"
MEMBERS = {"head": "Whole-Brain Calcium Activity/Young Adults/Head_Activity_OH16230.mat",
           "tail": "Whole-Brain Calcium Activity/Young Adults/Tail_Activity_OH16230.mat"}
EXCLUDED = re.compile(r"^(AVA|AVB|AVD|AVE|PVC|AS\d+|DA\d+|DB\d+|DD\d+|VA\d+|VB\d+|VC\d+|VD\d+)$")
SIMILAR_UM, SIMILAR_R = 5.0, 0.95


def load(part: str) -> dict:
    zf = zipfile.ZipFile(fsspec.open(ZENODO_ZIP, block_size=2**22).open())
    return sio.loadmat(io.BytesIO(zf.read(MEMBERS[part])), squeeze_me=True, struct_as_record=False)


def tidy(m: dict) -> dict:
    """Traces per (class, side, file), with the order of stimuli per file."""
    n_files = len(m["files"])
    out = {"fps": float(m["fps"]), "files": [str(f) for f in m["files"]],
           "stim_names": [str(s) for s in m["stim_names"]], "stim_times": np.atleast_2d(m["stim_times"]),
           "stims": np.atleast_2d(m["stims"]).astype(int), "traces": {}, "raw": {}, "pos": {}}
    for i, name in enumerate(m["neurons"]):
        name = str(name)
        tr = np.atleast_1d(m["norm_traces"][i])
        raw = np.atleast_1d(m["traces"][i])
        ps = np.atleast_1d(m["positions"][i])
        isl = np.atleast_1d(m["is_L"][i]).astype(float)
        for slot in range(len(tr)):
            x = np.asarray(tr[slot], float).ravel()
            if x.size == 0:
                continue
            if len(tr) == 2 * n_files:
                side = "L" if isl[slot] == 1 else "R"
                f = slot % n_files
            else:
                side, f = "", slot
            p = np.asarray(ps[slot], float)
            out["traces"][(name, side, f)] = x
            out["raw"][(name, side, f)] = np.asarray(raw[slot], float).ravel()
            out["pos"][(name, side, f)] = p.reshape(-1, 3).mean(0) if p.size >= 3 else np.full(3, np.nan)
    return out


def remove_similar(d: dict, which: str = "raw", both: bool = True) -> list:
    """Drop the members of any pair within 5 um whose traces correlate at 0.95 or more: both
    members, or with `both=False` only the second of each pair in the files' order.

    which: "raw" correlates the dF/F0 traces, "norm" the histogram-normalised ones."""
    removed = set()
    for f in range(len(d["files"])):
        keys = [k for k in d["traces"] if k[2] == f]
        for a in range(len(keys)):
            for b in range(a + 1, len(keys)):
                ka, kb = keys[a], keys[b]
                if np.linalg.norm(d["pos"][ka] - d["pos"][kb]) <= SIMILAR_UM:
                    x, y = d[which if which == "raw" else "traces"][ka], d[which if which == "raw" else "traces"][kb]
                    n = min(len(x), len(y))
                    ok = ~np.isnan(x[:n]) & ~np.isnan(y[:n])
                    if np.corrcoef(x[:n][ok], y[:n][ok])[0, 1] >= SIMILAR_R:
                        removed |= {ka, kb} if both else {kb}
    for k in removed:
        del d["traces"][k]
    return sorted(removed)


def stim_window(d: dict, f: int, stim: str, mapping: str = "order"):
    """(start, end) of a named stimulus in file f.

    mapping "order": stims[f, p] is the stimulus delivered p-th, at stim_times[p].
    mapping "name": stim_times row stims[f, k] - 1 is when stimulus k was delivered.
    """
    k = d["stim_names"].index(stim)
    row = d["stims"][f]
    if mapping == "order":
        p = int(np.flatnonzero(row - 1 == k)[0])
        return d["stim_times"][p]
    return d["stim_times"][row[k] - 1]


def window_means(d, key, stim, mapping="order"):
    x = d["traces"][key]
    t = np.arange(len(x)) / d["fps"]
    s, e = stim_window(d, key[2], stim, mapping)
    L = e - s
    pre = np.nanmean(x[(t >= s - L) & (t < s)])
    dur = np.nanmean(x[(t >= s) & (t < e)])
    post = np.nanmean(x[(t >= e) & (t < e + L)])
    return pre, dur, post


def storey_q(p: np.ndarray, lam: float = 0.5) -> np.ndarray:
    """q-values of Storey (2002), with pi0 estimated at lambda = 0.5 (a standard choice)."""
    p = np.asarray(p, float)
    m = len(p)
    pi0 = min(1.0, np.mean(p > lam) / (1 - lam)) if m else 1.0
    order = np.argsort(p)
    q = np.empty(m)
    prev = 1.0
    for rank, i in reversed(list(enumerate(order, start=1))):
        prev = min(prev, pi0 * m * p[i] / rank)
        q[i] = prev
    return q


def responses(d, stim, mapping="order"):
    """Per class (L and R pooled): paired two-tailed t test of stimulus against pre-stimulus."""
    rows = []
    classes = sorted({k[0] for k in d["traces"]})
    for c in classes:
        if EXCLUDED.match(c):
            continue
        keys = [k for k in d["traces"] if k[0] == c]
        v = np.array([window_means(d, k, stim, mapping) for k in keys])
        if len(v) < 4:
            continue
        diff = v[:, 1] - v[:, 0]
        p = stats.ttest_rel(v[:, 1], v[:, 0]).pvalue
        sp = v[:, 1] > v[:, 0]
        post = stats.ttest_rel(v[:, 2], v[:, 1], alternative="greater").pvalue
        rows.append({"neuron": c, "n": len(v), "mean_change": diff.mean(), "p": p,
                     "post_gate": bool(v[:, 1].mean() > v[:, 0].mean()), "p_post": post})
    if rows:
        q = storey_q(np.array([r["p"] for r in rows]))
        gated = [i for i, r in enumerate(rows) if r["post_gate"]]
        qp = np.full(len(rows), np.nan)
        if gated:
            qp[gated] = storey_q(np.array([rows[i]["p_post"] for i in gated]))
        for r, qq, qqp in zip(rows, q, qp):
            r["q"] = qq
            r["q_post"] = qqp
    return rows


def peak_rate(x, fps, prominence_sd=1.0):
    """Figure S1H: peaks per second of a trace median filtered at 0.5 s (3 samples at 4 Hz, the
    nearest odd window), NaN samples (the first second) dropped. The peak rule (a prominence of
    `prominence_sd` standard deviations of the filtered trace) is not given in the paper: an
    assumption, shown at several values."""
    from scipy.signal import find_peaks, medfilt
    x = np.asarray(x, float)
    x = x[~np.isnan(x)]
    y = medfilt(x, 3)
    pk, _ = find_peaks(y, prominence=prominence_sd * np.std(y))
    return len(pk) / (len(x) / fps)


def spectral_peak(x, fps, band=(0.05, 1.0)):
    """Frequency of the largest Welch power in the band (a check on the peak count)."""
    from scipy.signal import welch
    x = np.asarray(x, float)
    x = x[~np.isnan(x)]
    f, P = welch(x - x.mean(), fs=fps, nperseg=min(256, len(x)))
    i = (f >= band[0]) & (f <= band[1])
    return float(f[i][np.argmax(P[i])])
