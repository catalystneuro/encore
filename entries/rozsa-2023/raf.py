"""Loading and measures for the Rozsa et al. (2023) entry on DANDI:000341.

Files are streamed from the archive at a pinned version. Each NWB file is read
into memory with parallel HTTP range requests and opened with h5py from there;
nothing is written to disk. The files store each sweep as a separate contiguous
dataset with its metadata interleaved, so reading objects one by one over the
network is latency bound (about 2 MB/s); reading the whole file in large ranges
runs at well over 100 MB/s.
"""
import io
import json
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import requests

DANDISET = "000341"
VERSION = "0.241220.1312"
API = "https://api.dandiarchive.org/api"


def list_assets():
    """All assets of the pinned version, as dicts with path, size and asset_id."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r["next"]
    return out


def s3_url(asset_id):
    r = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60)
    return r.url


class _MemFile(io.RawIOBase):
    """A read-only file object over a bytearray, so h5py can open it without a copy."""

    def __init__(self, buf):
        self._mv = memoryview(buf)
        self._pos = 0

    def readable(self):
        return True

    def seekable(self):
        return True

    def tell(self):
        return self._pos

    def seek(self, pos, whence=0):
        if whence == 0:
            self._pos = pos
        elif whence == 1:
            self._pos += pos
        else:
            self._pos = len(self._mv) + pos
        return self._pos

    def readinto(self, b):
        n = min(len(b), len(self._mv) - self._pos)
        b[:n] = self._mv[self._pos:self._pos + n]
        self._pos += n
        return n


def fetch(asset, block=32 * 2**20, threads=16):
    """Read a whole asset into memory with parallel range requests; returns an h5py File."""
    url = s3_url(asset["asset_id"])
    size = asset["size"]
    buf = bytearray(size)

    def get(i):
        s = i * block
        e = min(size, s + block) - 1
        for _ in range(5):
            try:
                r = requests.get(url, headers={"Range": f"bytes={s}-{e}"}, timeout=300)
                if len(r.content) == e - s + 1:
                    buf[s:e + 1] = r.content
                    return
            except requests.RequestException:
                pass
        raise IOError(f"range {s}-{e} of {asset['path']} failed")

    with ThreadPoolExecutor(threads) as ex:
        list(ex.map(get, range((size + block - 1) // block)))
    return h5py.File(_MemFile(buf), "r")


# --- AP detection and per-AP measures ----------------------------------------------------------
#
# From the Methods ("Analysis of RAF patterns"): APs are detected on the unfiltered trace, the
# threshold is the point where dV/dt first exceeds 5 mV/ms, and the pre-AP slope is the slope of a
# linear fit to the last 1 ms before threshold. The claims file's header fixes the rest as a standard
# choice: an AP is an upstroke crossing 5 mV/ms followed by a peak above 0 mV (variant: a peak at
# least 30 mV above threshold). Spikes are found as peaks with a prominence of at least 20 mV at
# least 1 ms apart (a standard choice that only finds the candidates; the two rules above decide).
# The threshold is found by walking back from the steepest point of the upstroke, at most 5 ms, to
# the first sample of the run with dV/dt >= 5 mV/ms.

DVDT = 5.0          # mV/ms, Methods
SLOPE_MS = 1.0      # ms, Methods
SD_MS = 50.0        # ms, window of Figures 3F, 3K and 4F (claims file)
HIST_BINS = np.arange(-100, -19.99, 0.5)


def _ap_table(v, rate, i_stim):
    """APs of one sweep. v in mV, rate in Hz, i_stim in pA (same length as v, or None)."""
    from scipy.signal import find_peaks
    ms = rate / 1000.0
    dv = np.diff(v) * ms                       # mV/ms, dv[k] = v[k+1]-v[k]
    peaks, _ = find_peaks(v, prominence=20, distance=max(1, int(ms)))
    rows = []
    for p in peaks:
        lo = max(1, p - int(5 * ms))
        if p - lo < 2:
            continue
        k = lo + int(np.argmax(dv[lo:p]))      # steepest point of the upstroke
        if dv[k] < DVDT:
            continue
        j = k
        while j > lo and dv[j - 1] >= DVDT:
            j -= 1
        thr_i = j                              # first sample of the run with dV/dt >= 5 mV/ms
        n1 = int(round(SLOPE_MS * ms))
        if thr_i - n1 < 0:
            continue
        seg = v[thr_i - n1:thr_i + 1]
        tt = np.arange(len(seg)) / ms
        tt = tt - tt.mean()
        slope = float(np.dot(tt, seg - seg.mean()) / np.dot(tt, tt))   # least-squares line
        nsd = int(round(SD_MS * ms))
        pre_thr = v[max(0, thr_i - nsd):thr_i]
        pre_pk = v[max(0, p - nsd):p]
        full = thr_i - nsd >= 0
        rows.append(dict(
            idx=int(p), thr_idx=int(thr_i), t_thr=thr_i / rate, t_peak=p / rate,
            thr=float(v[thr_i]), peak=float(v[p]), slope=float(slope),
            sd_thr=float(np.std(pre_thr)) if full else np.nan,
            sd_peak=float(np.std(pre_pk)) if full else np.nan,
            vpre=float(np.mean(pre_thr)) if full else np.nan,
            i_thr=float(i_stim[thr_i]) if i_stim is not None else np.nan,
        ))
    for r in rows:
        r["main"] = r["peak"] > 0
        r["variant30"] = r["peak"] - r["thr"] >= 30
    return rows


def _steps(i_stim, tol=2.0):
    """Constant-current segments of a stimulus trace in pA: list of (start, stop, amplitude)."""
    nz = np.abs(i_stim) > tol
    if not nz.any():
        return []
    edges = np.flatnonzero(np.diff(np.r_[0, nz.astype(int), 0]))
    return [(int(a), int(b), float(np.median(i_stim[a:b]))) for a, b in zip(edges[::2], edges[1::2])]


def _sag(v, rate, steps):
    """Sag of the one hyperpolarizing step of a sweep, or None.

    Figure 2D marks the components on a hyperpolarizing step; the formula is not in the text. The
    readings of the claims file: (a) (steady - peak) / (base - peak), (b) (steady - peak) / (base -
    steady). Base: mean of the up to 50 ms before the step (at least 5 ms); peak: the minimum during the step (after a 1 ms
    smoothing); steady state: mean of the last 10% of the step (standard choices).
    """
    neg = [s for s in steps if s[2] < -5]
    if len(neg) != 1 or len(steps) != 1:
        return None
    a, b, amp = neg[0]
    ms = rate / 1000.0
    if a < int(5 * ms) or b - a < int(100 * ms):
        return None
    base = float(np.mean(v[max(0, a - int(50 * ms)):a]))
    w = max(1, int(ms))
    sm = np.convolve(v[a:b], np.ones(w) / w, mode="valid")
    peak = float(sm.min())
    ss = float(np.mean(v[b - (b - a) // 10:b]))
    if base - peak < 1:
        return None
    return dict(i_step=amp, base=base, vpeak=peak, vss=ss,
                sag_a=(ss - peak) / (base - peak),
                sag_b=(ss - peak) / (base - ss) if base - ss > 0.5 else np.nan,
                r_in=(base - ss) / -amp * 1000.0)   # MOhm, steady deflection over current


def extract(f, keep=()):
    """Per-AP and per-sweep tables of one open NWB file.

    Stimulus currents (imin, imax, i_thr, step amplitudes) are relative to the holding current at
    the start of each sweep, given as hold (pA).

    Voltage series are read in volts: the stored values are in volts although the files give a
    conversion factor of 1e-12 (checked in the data check). Stimulus series are in amperes.
    Returns (aps, sweeps, raw) where raw maps the name of each series whose channel starts with one
    of the prefixes in keep to (start, rate, trace in mV, float32).
    """
    import pandas as pd
    A = f["acquisition"]
    S = f["stimulus/presentation"] if "stimulus/presentation" in f else {}
    aps, sweeps, raw, bad_stim, pa_stim = [], [], {}, [], []
    for name in A:
        o = A[name]
        if "data" not in o:
            continue
        chan = re.sub(r"_?\d+$", "", name)
        start = float(o["starting_time"][()])
        rate = float(o["starting_time"].attrs["rate"])
        x = o["data"][:]
        if keep and chan.startswith(tuple(keep)):
            raw[name] = (start, rate, (x * 1000.0).astype(np.float32))
        if chan.startswith("LFP"):
            sweeps.append(dict(series=name, chan=chan, start=start, rate=rate, n=len(x)))
            continue
        v = x * 1000.0
        sname = name.replace("Vm", "Stim", 1)
        i_stim = S[sname]["data"][:] * 1e12 if sname in S and S[sname]["data"].shape == x.shape else None
        hold = np.nan
        if i_stim is not None and np.abs(i_stim).max() > 1e5:
            if np.abs(i_stim).max() < 1e16:
                i_stim = i_stim / 1e12         # values stored in pA although the unit is amperes
                pa_stim.append(name)
            else:
                i_stim = None                  # corrupt stimulus values; see the data check
                bad_stim.append(name)
        if i_stim is not None:
            # Many sweeps carry a holding current; steps are taken relative to the level at the
            # start of the sweep (median of its first 0.5 ms), a standard choice.
            hold = float(np.median(i_stim[:max(1, int(rate / 2000))]))
            i_stim = i_stim - hold
        steps = _steps(i_stim) if i_stim is not None else []
        sw = dict(series=name, chan=chan, start=start, rate=rate, n=len(x), hold=hold,
                  stim_bad=name in bad_stim, stim_in_pA=name in pa_stim,
                  vmin=float(v.min()), vmax=float(v.max()), vmed=float(np.median(v)),
                  imin=float(i_stim.min()) if i_stim is not None else np.nan,
                  imax=float(i_stim.max()) if i_stim is not None else np.nan,
                  nsteps=len(steps),
                  pos_ms=sum((b - a) for a, b, amp in steps if amp > 5) / rate * 1000,
                  neg_ends=[b / rate for a, b, amp in steps if amp < -5])
        if not steps:
            # Histogram of the membrane potential of sweeps without current (0.5 mV bins, -100
            # to -20 mV), for the up and down state readings of fig3-human-ap-states.
            sw["hist"] = np.histogram(v, bins=HIST_BINS)[0]
        sg = _sag(v, rate, steps)
        if sg:
            sw.update(sg)
        sweeps.append(sw)
        for r in _ap_table(v, rate, i_stim):
            r.update(series=name, chan=chan, rate=rate, sweep_start=start,
                     t_abs=start + r["t_thr"],
                     since_neg=min([r["t_thr"] - e for e in sw["neg_ends"] if r["t_thr"] >= e], default=np.inf))
            aps.append(r)
    return pd.DataFrame(aps), pd.DataFrame(sweeps), raw


def metadata(f):
    """The text metadata of a file: subject, session and the pharmacology table as key/value pairs."""
    def s(x):
        x = x[()]
        if isinstance(x, bytes):
            return x.decode()
        if hasattr(x, "tolist"):
            return [y.decode() if isinstance(y, bytes) else y for y in x.tolist()]
        return x
    g = f["general"]
    out = {"session_description": s(f["session_description"]), "identifier": s(f["identifier"])}
    for k in ("experiment_description", "keywords", "slices", "session_id"):
        if k in g:
            out[k] = s(g[k])
    for k in g["subject"]:
        out["subject_" + k] = s(g["subject"][k])
    pharm = {}
    if "pharmacology" in g:
        for line in s(g["pharmacology"]).splitlines():
            parts = re.split(r"\s{2,}", line.strip(), maxsplit=1)
            if len(parts) == 2 and not line.startswith("Name:"):
                pharm[parts[0]] = parts[1]
    out["pharmacology"] = pharm
    out["electrodes"] = [k for k in g["intracellular_ephys"] if k != "sweep_table"]
    return out


def process_group(assets, keep=(), threads=2):
    """Fetch and extract every asset of a list; returns {path: (meta, aps, sweeps, raw)}."""
    def one(a):
        f = fetch(a)
        try:
            return a["path"], (metadata(f),) + extract(f, keep)
        finally:
            f.close()
    import gc

    def one_gc(a):
        r = one(a)
        gc.collect()
        return r
    # Files over 1.5 GB are read one at a time, to keep within memory.
    small = [a for a in assets if a["size"] <= 1.5e9]
    big = [a for a in assets if a["size"] > 1.5e9]
    with ThreadPoolExecutor(threads) as ex:
        out = dict(ex.map(one_gc, small))
    for a in big:
        k, v = one_gc(a)
        out[k] = v
    return out


# --- Analysis ----------------------------------------------------------------------------------

def gmm_classes(aps, seed):
    """Reading (b) of the claims file's header: a two-component Gaussian mixture on threshold and
    pre-AP slope, fitted to the APs given (one preparation pooled). Returns a boolean array, True
    for RA-APs (the component with the lower mean threshold). Features are z-scored first (a
    standard choice); the seed is the claim's."""
    from sklearn.mixture import GaussianMixture
    X = aps[["thr", "slope"]].to_numpy(float)
    X = (X - X.mean(0)) / X.std(0)
    gm = GaussianMixture(2, random_state=seed, n_init=5).fit(X)
    lab = gm.predict(X)
    lo = int(np.argmin(gm.means_[:, 0]))
    return lab == lo


def paper_test(a, b, paired=False):
    """The paper's rule (Methods, "Statistics"): a Kolmogorov-Smirnov test of normality, then a
    t test (paired or two-sample) for normal data and a Mann-Whitney U test otherwise. Normality is
    tested on each group (on the differences when paired) against a normal with the sample's mean
    and SD, at P < 0.05. Returns (test name, P)."""
    from scipy import stats
    a = np.asarray(a, float)
    b = np.asarray(b, float)

    def normal(x):
        if len(x) < 3 or np.std(x) == 0:
            return False
        z = (x - np.mean(x)) / np.std(x, ddof=1)
        return stats.kstest(z, "norm").pvalue >= 0.05
    if paired:
        if normal(a - b):
            return "paired t", stats.ttest_rel(a, b).pvalue
        return "Wilcoxon (paired, not normal)", stats.wilcoxon(a, b).pvalue
    if normal(a) and normal(b):
        return "two-sample t", stats.ttest_ind(a, b).pvalue
    return "Mann-Whitney U", stats.mannwhitneyu(a, b, alternative="two-sided").pvalue


def rayleigh(phases_deg):
    """Mean vector length, mean angle (degrees, 0 to 360) and Rayleigh P, as circ_rtest of the
    CircStat toolbox the Methods cite (ref. 49; Zar's approximation)."""
    a = np.deg2rad(np.asarray(phases_deg, float))
    n = len(a)
    if n == 0:
        return np.nan, np.nan, np.nan, 0
    c = np.exp(1j * a).mean()
    r = abs(c)
    R = n * r
    p = np.exp(np.sqrt(1 + 4 * n + 4 * (n ** 2 - R ** 2)) - (1 + 2 * n))
    return r, np.rad2deg(np.angle(c)) % 360, min(1.0, p), n


def circ_dist(a, b):
    return abs((a - b + 180) % 360 - 180)


def induction_sweeps(sw):
    """Sweeps of the RAF induction protocol: the Methods give 100 ms suprathreshold square pulses
    every 300 ms, so a sweep shorter than 1 s with one positive step of 50 to 300 ms (some
    recordings use 160 ms sweeps with a 100 ms pulse, others 350 ms sweeps with a 250 ms pulse).
    Standard choice for the bounds."""
    v = sw[sw.chan.str.startswith("Vm")]
    dur = v.n / v.rate
    return v[(dur < 1.0) & (v.nsteps == 1) & (v.pos_ms >= 50) & (v.pos_ms <= 300)]


def ra_aps_induction(aps, sw, rebound_s=0.3):
    """Reading (c) of the claims file's header for one induction recording. AIS-APs are the APs
    during positive current; RA-APs the APs without positive current (I <= 5 pA at threshold) after
    the first induction sweep, leaving out APs within 0.3 s of the end of a hyperpolarizing step
    (rebound APs; a standard choice). Returns (ais, ra, t_first_induction, run starts)."""
    ind = induction_sweeps(sw)
    if len(aps) == 0 or len(ind) == 0:
        return aps.iloc[:0], aps.iloc[:0], np.nan, []
    t0 = float(ind.start.min())
    starts = np.sort(ind.start.to_numpy())
    runs = [starts[0]] + [b for a, b in zip(starts[:-1], starts[1:]) if b - a > 5.0]
    ais = aps[aps.i_thr > 5]
    ra = aps[(aps.i_thr <= 5) & (aps.t_abs >= t0) & (aps.since_neg > rebound_s)]
    return ais, ra.sort_values("t_abs"), t0, runs


def epochs(ra_times, runs=None):
    """RAF epochs from RA-AP times: (i) one per cell, or (ii) one per induction run, the RA-APs
    from one run's start to the next. Per the Methods, duration is first to last RA-AP and
    frequency RA-APs over duration; persistent above 5 Hz. Epochs of one RA-AP are left out
    (criterion of fig1ab-raf-patterns)."""
    t = np.sort(np.asarray(ra_times, float))
    groups = [t] if runs is None else [
        t[(t >= a) & (t < b)] for a, b in zip(runs, list(runs[1:]) + [np.inf])]
    out = []
    for g in groups:
        if len(g) < 2:
            continue
        d = g[-1] - g[0]
        if d <= 0:
            continue
        out.append(dict(n=len(g), duration=d, freq=len(g) / d, t_first=g[0], t_last=g[-1]))
    return out
