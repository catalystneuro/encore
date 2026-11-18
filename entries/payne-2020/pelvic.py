"""Loading and measures for SPARC:206 (Payne et al. 2020, pelvic nerve array in rats).

Every file is streamed from the public SPARC bucket at the object version that the
pinned dataset version's manifest gives (version 1, DOI 10.26275/kkmb-vun5); nothing
is written to disk.

Where each parameter comes from:

- ECAP threshold of 0.05 uV "in both recordings": Methods, "Electrically Evoked
  Compound Action Potentials and Impedance Testing" (via the claims file criteria).
- The two recordings at a current are the files' trial 1 and trial 2 ("Two sets of
  ECAPs ... were made", same Methods passage). Trials 3 and 4, present at a few
  currents, are not used (a choice; they are extra repeats).
- Peak detection (which local maxima are P1, P2 and P3): the paper does not say how
  peaks were found. Assumption, stated in the attempt: P1 to P3 are the first three
  positive local maxima, in time, after the end of the stimulus artefact, in the mean
  of the two recordings at the highest current, whose prominence is at least three
  times the noise SD (noise from the lowest-current traces after 1 ms) and whose
  amplitude is at least 0.05 uV. The factor of three is a standard detection margin,
  chosen here.
- Artefact end: the claims file's readings, (a) 1 ms after pulse onset, (b) the first
  return of the trace to baseline.
- Baseline: the traces start 0.6 ms after pulse onset, so there is no pre-stimulus
  segment. Assumption: the baseline is the median of the trace from 7 to 8.6 ms, after
  the responses have ended.
- Time origin: the files' StartTime (0.6 ms) is taken as time from pulse onset; the
  claims file's reading (b) shifts it by the 250 us of the biphasic pulse.
- Peak search window when following a peak to lower currents: +-0.3 ms around its
  latency at the highest current (a choice, about the spread of a peak across
  currents seen in the traces).
- Conduction distance: the claims file's readings, 2.85, 2.10 or 3.60 mm, from the
  array geometry in the Methods ("Design of a Custom Planar Four-Electrode Array").
- Cystometry: void parameters from the files' /Voids group and the derivative table
  cystometry-dataset.xlsx; mean of each rat's mean over three cycles with a t-based
  95% CI, as the dataset's own code (files/code/cystometry-analysis.rmd) does.
"""
import base64
import functools
import io
import json
import re
import xml.etree.ElementTree as ET

import fsspec
import h5py
import numpy as np
import pandas as pd
from scipy import signal, stats

BUCKET = "https://sparc-prod-aod-discover-publish50-use1.s3.amazonaws.com/206/"
MANIFEST_VERSION = "Ag7Kwl87aKqHqVTtho8dzikC2BfNyghN"  # version 1, 10.26275/kkmb-vun5

ACUTE = ["12-005", "12-006", "12-007", "12-008", "12-010"]
CHRONIC = ["12-050", "12-051", "12-052", "12-053", "12-055", "12-056", "12-057"]
COLON = ["12-019", "12-020", "15-758"]

DISTANCES_MM = {"a: 2.85 mm pair centres": 2.85, "b: 2.10 mm E2 to E3": 2.10,
                "c: 3.60 mm E1 to E4": 3.60}
THRESH_UV = 0.05


@functools.lru_cache()
def manifest():
    with fsspec.open(BUCKET + "manifest.json?versionId=" + MANIFEST_VERSION, "rb",
                     block_size=2**20) as f:
        m = json.load(f)
    return {f["path"]: f for f in m["files"]}


def url(path):
    return BUCKET + path + "?versionId=" + manifest()[path]["s3VersionId"]


def sha256_hex(path):
    return base64.b64decode(manifest()[path]["sha256"]).hex()


READ = []  # every file read, for the header


def read_bytes(path):
    """Read a whole (small) file into memory."""
    with fsspec.open(url(path), "rb", block_size=2**20) as f:
        b = f.read()
    if path not in READ:
        READ.append(path)
    return b


def h5(path):
    """Open an HDF5 file from the bucket, in memory (the largest is 6 MB)."""
    return h5py.File(io.BytesIO(read_bytes(path)), "r")


def read_excel(path, **kw):
    return pd.read_excel(io.BytesIO(read_bytes(path)), **kw)


def read_csv(path, **kw):
    return pd.read_csv(io.BytesIO(read_bytes(path)), **kw)


# ---------------------------------------------------------------- ECAPs

def load_ecap(sub):
    """All averaged ECAP traces of one subject.

    Returns (table, X, t, attrs): one table row per trace (stim pair, CL, trial, current
    in mA), X in uV (the files are in mV), t in ms from pulse onset.
    """
    with h5(f"files/primary/sub-{sub}/sub-{sub}_ECAP.hdf5") as f:
        E = f["ECAPs"]
        names = list(E.keys())
        X = np.array([E[n][()].ravel() for n in names], dtype=float) * 1000.0
        a = {k: (v[0] if isinstance(v, np.ndarray) and v.size == 1 else v)
             for k, v in E[names[0]].attrs.items()}
        attrs_all = [dict(E[n].attrs) for n in names]
        S = {k: f["Stimuli"][k][()].ravel() for k in f["Stimuli"].keys()}
        sattrs = dict(f["Stimuli"].attrs)
    rows = []
    for n in names:
        m = re.match(r"Stim_(E\d\d)_CL(\d+)_trial(\d+)", n)
        rows.append((n, m.group(1), int(m.group(2)), int(m.group(3))))
    tab = pd.DataFrame(rows, columns=["name", "pair", "CL", "trial"])
    cur = {(int(c), int(tr)): s for c, tr, s in zip(S["StimCL"], S["Trial"], S["Stim"])}
    tab["mA"] = [cur[(c, tr)] for c, tr in zip(tab.CL, tab.trial)]
    # the attributes must be the same for every trace
    for k in ["SampleRate", "StartTime", "Duration", "WaveUnits", "TimeUnits"]:
        vals = {np.asarray(x[k]).ravel()[0] for x in attrs_all}
        assert len(vals) == 1, (sub, k, vals)
    n = X.shape[1]
    t = float(a["StartTime"]) + np.arange(n) / float(a["SampleRate"]) * 1000.0
    a["stim_attrs"] = sattrs
    return tab, X, t, a


def ecap_levels(tab, X):
    """Per current: the two recordings (trials 1 and 2) and their mean."""
    out = []
    for mA, g in tab.groupby("mA"):
        g = g.sort_values("trial")
        g = g[g.trial <= 2]
        if len(g) < 2:
            continue
        out.append((float(mA), X[g.index[0]], X[g.index[1]]))
    out.sort(key=lambda r: r[0])
    return out


def baseline(x, t):
    return float(np.median(x[(t >= 7.0) & (t <= 8.6)]))


def noise_sd(levels, t):
    """SD of the lowest-current traces after 1 ms, baseline removed."""
    _, r1, r2 = levels[0]
    m = t >= 1.0
    return float(np.std(np.r_[r1[m] - baseline(r1, t), r2[m] - baseline(r2, t)]))


def artefact_end(x, t, reading):
    """End of the stimulus artefact: (a) 1 ms, (b) first return of the trace to baseline."""
    if reading == "a":
        return 1.0
    y = x - baseline(x, t)
    s = np.sign(y)
    cross = np.where(s[1:] != s[:-1])[0]
    return float(t[cross[0] + 1]) if len(cross) else 1.0


def find_peaks_maxcurrent(levels, t, art, k_noise=3.0, tmax=7.0):
    """P1..P3 latencies (ms from onset) at the highest current; see module docstring."""
    mA, r1, r2 = levels[-1]
    m = (r1 + r2) / 2
    y = m - baseline(m, t)
    sd = noise_sd(levels, t)
    end = artefact_end(m, t, art)
    idx, prop = signal.find_peaks(y, prominence=k_noise * sd)
    keep = [i for i in idx if end < t[i] <= tmax and y[i] >= THRESH_UV]
    return [float(t[i]) for i in keep[:3]], sd, end


def amp_at(x, t, lat, reading, win=0.3):
    """Response amplitude of the peak nearest a latency.

    The peak is the local maximum within +-win ms of the latency that lies nearest to it
    (the largest value in the window when there is none). Amplitude (a) is its height
    above baseline; (b) its height above the preceding trough, the minimum from 0.5 ms
    before the window to the peak.
    """
    y = x - baseline(x, t)
    w = np.where((t >= lat - win) & (t <= lat + win))[0]
    pk, _ = signal.find_peaks(y[w])
    if len(pk):
        i = w[pk[np.argmin(np.abs(t[w[pk]] - lat))]]
    else:
        i = w[np.argmax(y[w])]
    if reading == "a":
        return float(y[i]), float(t[i])
    pre = (t >= lat - win - 0.5) & (t <= t[i])
    return float(y[i] - y[pre].min()), float(t[i])


def thresholds(levels, t, lats, amp_reading, step_reading, sustained=False):
    """Threshold per peak, in uA, or nan when the peak never passes.

    Pass at a current: amplitude >= 0.05 uV in both recordings (Methods). Step reading
    (a) the lowest current that passes; (b) linear interpolation in current between the
    last failing and the first passing current on the smaller of the two amplitudes.
    sustained=True takes the lowest current from which every higher current also passes.
    """
    res = []
    for lat in lats:
        a = np.array([min(amp_at(r1, t, lat, amp_reading)[0], amp_at(r2, t, lat, amp_reading)[0])
                      for _, r1, r2 in levels])
        cur = np.array([mA for mA, _, _ in levels]) * 1000.0
        ok = a >= THRESH_UV
        if sustained:
            j = None
            for k in range(len(ok) - 1, -1, -1):
                if ok[k]:
                    j = k
                else:
                    break
        else:
            j = int(np.argmax(ok)) if ok.any() else None
        if j is None:
            res.append(np.nan)
            continue
        if step_reading == "a" or j == 0:
            res.append(float(cur[j]))
        else:
            c0, c1, a0, a1 = cur[j - 1], cur[j], a[j - 1], a[j]
            res.append(float(c0 + (THRESH_UV - a0) / (a1 - a0) * (c1 - c0)) if a1 != a0 else float(c1))
    return res


def latencies_at(levels, t, lats, level_reading, thr_uA, origin):
    """Peak latencies under a stimulus-level reading.

    (a) the highest current; (b) the lowest current at which all three peaks pass
    threshold; (c) the mean over all currents at or above the P3 threshold.
    The time origin is (a) pulse onset or (b) the end of the 250 us biphasic pulse.
    """
    shift = 0.0 if origin == "a" else 0.25
    cur = np.array([mA for mA, _, _ in levels]) * 1000.0

    def lat_at(k):
        _, r1, r2 = levels[k]
        m = (r1 + r2) / 2
        return [amp_at(m, t, L, "a")[1] for L in lats]

    if level_reading == "a":
        out = lat_at(len(levels) - 1)
    else:
        top = np.nanmax(thr_uA) if np.isfinite(thr_uA).all() else np.nan
        if not np.isfinite(top):
            return [np.nan] * len(lats)
        ks = np.where(cur >= top - 1e-9)[0]
        if level_reading == "b":
            out = lat_at(ks[0])
        else:
            out = list(np.mean([lat_at(k) for k in ks], axis=0))
    return [x - shift for x in out]


# ---------------------------------------------------------------- cystometry

CYSTO = ["18-196", "18-208", "18-243", "18-248", "18-262", "18-270", "18-273", "18-290",
         "18-291", "18-294", "12-081", "12-083", "15-759", "15-760"]


def load_cysto(sub, wave=True):
    """Pressure waves (list of (t, p) in s and mmHg), voids table and stimuli table."""
    with h5(f"files/primary/sub-{sub}/sub-{sub}_cystometry.hdf5") as f:
        waves = []
        if wave:
            for n in f["Cystometry"]:
                d = f["Cystometry"][n]
                a = {k: np.asarray(v).ravel()[0] for k, v in d.attrs.items()}
                p = d[()].ravel()
                t = float(a["StartTime"]) + np.arange(p.size) / float(a["SampleRate"])
                waves.append(dict(name=n, t=t, p=p, attrs=a))
        V = pd.DataFrame({k: f["Voids"][k][()].ravel() for k in f["Voids"]})
        S = None
        if "Stimuli" in f:
            S = pd.DataFrame({k: f["Stimuli"][k][()].ravel() for k in f["Stimuli"]})
            S.attrs.update({k: np.asarray(v).ravel()[0] for k, v in f["Stimuli"].attrs.items()})
    return waves, V, S


def mean_ci(x, level=0.95):
    x = np.asarray(x, float)
    x = x[np.isfinite(x)]
    n = len(x)
    m = x.mean()
    h = stats.t.ppf((1 + level) / 2, n - 1) * x.std(ddof=1) / np.sqrt(n)
    return m, m - h, m + h, n


# ---------------------------------------------------------------- impedances

def read_pzfx(path):
    """The Y columns of the first table of a GraphPad Prism XML file, as lists."""
    root = ET.fromstring(read_bytes(path).decode("utf-8"))
    ns = {"p": "http://graphpad.com/prism/Prism.htm"}
    out = {}
    tab = root.find("p:Table", ns)
    for yc in tab.findall("p:YColumn", ns):
        title = yc.find("p:Title", ns).text
        vals = []
        for sc in yc.findall("p:Subcolumn", ns):
            d = sc.find("p:d", ns)
            vals.append(float(d.text) if d is not None and d.text else np.nan)
        out[title] = vals
    return out


# ---------------------------------------------------------------- ECAP analysis per rat

def analyse_ecap(sub, art="a", k_noise=3.0):
    """Peaks, thresholds under every reading, and latencies under every reading."""
    tab, X, t, a = load_ecap(sub)
    L = ecap_levels(tab, X)
    lats, sd, end = find_peaks_maxcurrent(L, t, art, k_noise=k_noise)
    out = dict(sub=sub, levels=L, t=t, lats=lats, sd=sd, art_end=end,
               max_mA=L[-1][0], min_mA=L[0][0], thr={}, lat={})
    for amp in "ab":
        for step in "ab":
            for sus in (False, True):
                out["thr"][(amp, step, sus)] = (thresholds(L, t, lats, amp, step, sus)
                                                if lats else [])
    for lev in "abc":
        for org in "ab":
            thr = np.array(out["thr"][("a", "a", False)], float)
            out["lat"][(lev, org)] = (latencies_at(L, t, lats, lev, thr, org) if len(lats) == 3
                                      else [np.nan] * 3)
    return out


def dunn_friedman(data):
    """Dunn's test on Friedman mean ranks. data: n blocks x k groups.

    Returns the Friedman statistic and p, the mean ranks, and for each pair (i, j) the
    z and two-sided unadjusted p: z = (Rbar_i - Rbar_j) / sqrt(k (k + 1) / (6 n)).
    """
    data = np.asarray(data, float)
    n, k = data.shape
    ranks = np.array([stats.rankdata(r) for r in data])
    rbar = ranks.mean(0)
    se = np.sqrt(k * (k + 1) / (6.0 * n))
    pairs = {}
    for i in range(k):
        for j in range(i + 1, k):
            z = (rbar[j] - rbar[i]) / se
            pairs[(i, j)] = (float(z), float(2 * stats.norm.sf(abs(z))))
    fr = stats.friedmanchisquare(*data.T)
    return float(fr.statistic), float(fr.pvalue), rbar, pairs
