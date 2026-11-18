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
  peaks were found. Candidate peaks are the positive local maxima after the end of the
  stimulus artefact, in the mean of the two recordings at the highest current, whose
  prominence is at least k times the noise SD (noise from the lowest-current traces
  after 1 ms; k = 2, 3 or 5) and whose amplitude is at least 0.05 uV. Three rules then
  assign P1 to P3, all run (assumption; the Results say only that the peaks are
  positive and distinguished by latency): "first", the first three candidates in time
  (the main rule); "largest", the three largest candidates, in time order; "window",
  the three candidates in time order that lie inside the paper's ranges for P1, P2 and
  P3 (anaesthetised or awake, Results), each widened by 10% of its bounds as the
  criterion widens them, with the largest summed amplitude. The window rule
  uses the paper's own ranges, so it can only favour a match. A fourth reading, "inv",
  applies the first rule to the inverted traces, for files whose polarity may be
  reversed (the file means are anti-correlated between some files).
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


WINDOWS_ANES = [(1.65, 2.90), (2.51, 4.16), (3.25, 5.67)]   # Results, ECAPs, paragraph 1
WINDOWS_AWAKE = [(1.93, 2.65), (3.19, 4.44), (4.57, 6.72)]  # Results, ECAPs, paragraph 2
RULES = ["first", "largest", "window", "inv"]


def find_peaks_maxcurrent(levels, t, art, k_noise=3.0, tmax=7.0, rule="first", windows=None):
    """P1..P3 latencies (ms from onset) at the highest current; see module docstring.

    For rule "inv" the caller passes inverted levels; it is the first rule.
    """
    mA, r1, r2 = levels[-1]
    m = (r1 + r2) / 2
    y = m - baseline(m, t)
    sd = noise_sd(levels, t)
    end = artefact_end(m, t, art)
    idx, prop = signal.find_peaks(y, prominence=k_noise * sd)
    keep = [i for i in idx if end < t[i] <= tmax and y[i] >= THRESH_UV]
    if rule in ("first", "inv"):
        out = keep[:3]
    elif rule == "largest":
        out = sorted(sorted(keep, key=lambda i: -y[i])[:3])
    elif rule == "window":
        # the triple in time order, each inside its range widened by 10% of each bound,
        # with the largest summed amplitude
        W = [(lo * 0.9, hi * 1.1) for lo, hi in windows]
        best, out = -np.inf, []
        for a in keep:
            for b in keep:
                for c in keep:
                    if not (t[a] < t[b] < t[c]):
                        continue
                    if all(lo <= t[i] <= hi for i, (lo, hi) in zip((a, b, c), W)):
                        v = y[a] + y[b] + y[c]
                        if v > best:
                            best, out = v, [a, b, c]
    else:
        raise ValueError(rule)
    return [float(t[i]) for i in out], sd, end


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


def passes(levels, t, lats, amp_reading="a"):
    """Per current and peak: does the amplitude reach 0.05 uV in both recordings?"""
    return np.array([[min(amp_at(r1, t, L, amp_reading)[0], amp_at(r2, t, L, amp_reading)[0]) >= THRESH_UV
                      for L in lats] for _, r1, r2 in levels])


def latencies_at(levels, t, lats, level_reading, thr_uA, origin):
    """Peak latencies under a stimulus-level reading.

    (a) the highest current; (b) the lowest current at which all three peaks pass in both
    recordings (amplitude above baseline); (c) the mean over all currents at or above the
    P3 threshold (first-passing reading). The time origin is (a) pulse onset or (b) the
    end of the 250 us biphasic pulse.
    """
    shift = 0.0 if origin == "a" else 0.25
    cur = np.array([mA for mA, _, _ in levels]) * 1000.0

    def lat_at(k):
        _, r1, r2 = levels[k]
        m = (r1 + r2) / 2
        return [amp_at(m, t, L, "a")[1] for L in lats]

    if level_reading == "a":
        out = lat_at(len(levels) - 1)
    elif level_reading == "b":
        ok = passes(levels, t, lats).all(1)
        if not ok.any():
            return [np.nan] * len(lats)
        out = lat_at(int(np.argmax(ok)))
    else:
        p3 = thr_uA[-1] if len(thr_uA) else np.nan
        if not np.isfinite(p3):
            return [np.nan] * len(lats)
        ks = np.where(cur >= p3 - 1e-9)[0]
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


def _wave_at(W, t0):
    for w in W:
        if w["t"][0] <= t0 <= w["t"][-1]:
            return w
    return None


def ivi_min(W, V, k):
    """Minutes from the onset of void k-1 to that of void k, when both lie in one wave
    (a gap between waves is not an interval), else nan."""
    if k < 1:
        return np.nan
    t0, t1 = float(V.ThresholdTime.iloc[k - 1]), float(V.ThresholdTime.iloc[k])
    w = _wave_at(W, t1)
    return (t1 - t0) / 60 if w is not None and w["t"][0] <= t0 else np.nan


def smooth(p, fs, sec=1.0):
    """Moving mean over sec seconds (removes the HFPOs from the pressure)."""
    n = max(1, int(round(sec * fs)))
    return np.convolve(p, np.ones(n) / n, mode="same")


def void_params(W, V, k, next_onset=np.inf, relax_frac=0.1, hfpo_factor=3.0):
    """Table 1 parameters of void k (a row of /Voids), recomputed from the pressure trace.

    The void's onset is the authors' /Voids ThresholdTime marker (the data hold no other
    mark of where a contraction starts). From the trace, with ps the 1 s moving mean:
    minimum = lowest ps from the peak to the next void's onset (minimum_60: lowest ps in
    the 60 s after the peak, a second reading of "after a voiding contraction"; the
    relative pressures are given against both, suffix _60 for the second); threshold (a) = ps at the
    onset; threshold (b) = ps at the start of the HFPOs, the proxy here for urine release
    (Methods: HFPOs come from the rhabdosphincter activity that permits urine flow), where
    the 0.5 s moving SD of the 3 to 30 Hz band-passed pressure (4th-order Butterworth,
    zero phase; hp) first reaches hfpo_factor times its median over the 30 s before onset; peak = highest raw p from the onset to the return; duration (a) = onset
    to the first time after the peak that ps is back within relax_frac of the contraction
    amplitude of the minimum; duration (b) = time from the onset until ps falls below
    threshold (a) after the peak; HFPO frequency (a) = largest peak of the Welch spectrum
    of hp between 3 and 30 Hz over the stretch above threshold, (b) local maxima of hp
    per second over the HFPO period (prominence at least the SD of hp there).
    relax_frac 0.1 and hfpo_factor 3 are choices (the paper defines neither).
    """
    r = V.iloc[k]
    w = _wave_at(W, float(r.ThresholdTime))
    out = dict(onset=float(r.ThresholdTime))
    if w is None:
        return out
    t, p = w["t"], np.asarray(w["p"], float)
    fs = float(w["attrs"]["SampleRate"])
    ps = smooth(p, fs)
    hp = signal.sosfiltfilt(signal.butter(4, [3, 30], btype="band", fs=fs, output="sos"), p)
    t_on = float(r.ThresholdTime)
    i_on = int(np.searchsorted(t, t_on))
    t_end = min(next_onset, t[-1])
    seg = (t >= t_on) & (t < t_end)
    i_pk = i_on + int(np.argmax(ps[seg][: int(120 * fs)]))
    after = (t >= t[i_pk]) & (t < t_end)
    if not after.any():
        return out
    i_min = np.where(after)[0][int(np.argmin(ps[after]))]
    pmin = float(ps[i_min])
    a60 = after & (t <= t[i_pk] + 60)
    pmin60 = float(np.min(ps[a60]))
    thr_a = float(ps[i_on])
    amp = float(ps[i_pk]) - pmin
    j = np.where(after & (ps <= pmin + relax_frac * amp))[0]
    t_ret = float(t[j[0]]) if len(j) else np.nan
    j = np.where(after & (ps < thr_a))[0]
    t_below = float(t[j[0]]) if len(j) else np.nan
    win = (t >= t_on) & (t <= (t_ret if np.isfinite(t_ret) else t[i_pk]))
    peak = float(np.max(p[win]))
    out.update(minimum=pmin, minimum_60=pmin60, thr_a=thr_a, peak=peak, peak_rel=peak - pmin,
               thr_a_rel=thr_a - pmin, peak_rel_60=peak - pmin60, thr_a_rel_60=thr_a - pmin60,
               dur_a=t_ret - t_on, dur_b=t_below - t_on, fs=fs)
    # HFPOs
    n5 = max(2, int(0.5 * fs))
    rsd = pd.Series(hp).rolling(n5, center=True).std().values
    pre = (t >= t_on - 30) & (t < t_on)
    lvl = hfpo_factor * np.nanmedian(rsd[pre]) if pre.any() else np.nan
    el = (t >= t_on) & (t <= (t_below if np.isfinite(t_below) else t[i_pk]))
    hf = el & (rsd >= lvl)
    if hf.any():
        i_h = np.where(hf)[0][0]
        out["thr_b"] = float(ps[i_h])
        out["thr_b_rel"] = float(ps[i_h]) - pmin
        out["thr_b_rel_60"] = float(ps[i_h]) - pmin60
    if el.sum() >= int(2 * fs) and fs >= 60:
        f, pw = signal.welch(hp[el], fs=fs, nperseg=min(el.sum(), int(2 * fs)))
        band = (f >= 3) & (f <= min(30, fs / 2))
        out["hfpo_a"] = float(f[band][np.argmax(pw[band])])
    if hf.sum() >= int(1 * fs):
        x = hp[hf]
        pk, _ = signal.find_peaks(x, prominence=np.std(x))
        out["hfpo_b"] = len(pk) / (hf.sum() / fs)
    return out


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

@functools.lru_cache(maxsize=None)
def _levels(sub):
    tab, X, t, a = load_ecap(sub)
    return ecap_levels(tab, X), t


def analyse_ecap(sub, art="a", k_noise=3.0, rule="first", windows=None):
    """Peaks, thresholds under every reading, and latencies under every reading."""
    L, t = _levels(sub)
    if rule == "inv":
        L = [(mA, -r1, -r2) for mA, r1, r2 in L]
    lats, sd, end = find_peaks_maxcurrent(L, t, art, k_noise=k_noise, rule=rule,
                                          windows=tuple(windows) if windows else None)
    out = dict(sub=sub, levels=L, t=t, lats=lats, sd=sd, art_end=end, rule=rule,
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
