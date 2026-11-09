"""Loading and measures for CRCNS data set hc-7 (Kohus et al. 2016, J Physiol, doi:10.1113/jp272231).

The data set is unversioned on CRCNS (version recorded as "unversioned"); it is one zip,
hc-7/live/Data.zip, streamed from the public S3 bucket crcnsarchive and opened in place with
fsspec and zipfile (docs/archives.md, "CRCNS"). Nothing is written to disk.

Layout (data descriptor, "Data files organization"): Data/IN_PC/<type>/PairNN and
Data/IN_IN/<type>/PairNN, each recording a base name sYYMMDD-RRRR with a .hda header (sample rate),
headerless little-endian float32 sweeps <base>_ch1_sNNNN.bin and <base>_ch2_sNNNN.bin (one channel
the presynaptic membrane potential in mV, the other the postsynaptic current in pA, the assignment
varying), and <base>_EPA.txt, the authors' per-sweep amplitude (pA) and success tables.

Where each parameter comes from is said where it is defined:
- "claims M<n>": the shared method details of the claims file (claims/crcns-hc-7/10.1113-jp272231.yaml).
- "paper": a passage of the paper, cited.
- "standard choice": a detail that the paper does not give; said so, and varied where it could
  change a result.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

import fsspec
import numpy as np
import pandas as pd
from scipy import optimize, signal

DATASET = "hc-7"
VERSION = "unversioned"
DATASET_DOI = "10.6080/K0MK69T5"
URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-7/live/Data.zip"
CHECKSUMS_URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-7/live/checksums.md5"

TYPE_LABEL = {
    "PVBC_to_PC": "PV+BC to PC", "AAC_to_PC": "AAC to PC", "CCKBC_to_PC": "CCK+BC to PC",
    "CCKDTI_to_PC": "CCK+DTI to PC", "PVBC_to_PVBC": "PV+BC to PV+BC",
    "CCKBC_to_CCKBC": "CCK+BC to CCK+BC", "CCKDTI_to_CCKDTI": "CCK+DTI to CCK+DTI",
    "PVBC_to_AAC": "PV+BC to AAC",
}
FREQS = [1, 5, 10, 20, 40, 80, 160, 320]
RECOVERY_INTERVALS = [50, 100, 200, 300, 500, 800, 1200]  # paper, Methods, protocols paragraph


def open_zip():
    import zipfile
    f = fsspec.open(URL, block_size=2**20).open()
    return zipfile.ZipFile(f)


def checksums() -> dict:
    with fsspec.open(CHECKSUMS_URL, "rt") as f:
        return {line.split()[1]: line.split()[0] for line in f if line.strip()}


# --- tables -----------------------------------------------------------------------------------

def experiments_table(z) -> pd.DataFrame:
    """Data/Experiments_description.txt as long rows: connection, pair (its numbering), protocol, entry."""
    text = z.read("Data/Experiments_description.txt").decode("latin1")
    rows, header, conn = [], None, None
    for line in text.splitlines():
        cells = line.rstrip("\r").split("\t")
        if not cells[0]:
            continue
        if not cells[0].startswith("Pair"):
            conn, header = cells[0].strip(), cells
            continue
        for col, val in zip(header[1:], cells[1:]):
            if col.strip():
                rows.append(dict(connection=conn, pair=int(cells[0].split()[1]), protocol=col.strip(),
                                 entry=val.strip()))
    return pd.DataFrame(rows)


def recordings_table(z) -> pd.DataFrame:
    """One row per recording (.hda header) in the zip, with the header's sweep count, length and rate."""
    rows = []
    bins = {}
    for info in z.infolist():
        m = re.match(r"(.*)_ch(\d)_s(\d+)\.bin$", info.filename)
        if m:
            bins.setdefault(m.group(1), {}).setdefault(int(m.group(2)), []).append(int(m.group(3)))
    for info in z.infolist():
        if not info.filename.endswith(".hda"):
            continue
        h = z.read(info.filename).decode("latin1")
        get = lambda key: float(re.search(key + r"\t\s*(\S+)", h).group(1))
        path = info.filename[:-4]
        _, side, folder, pair, base = path.split("/")
        nb = bins.get(path, {})
        rows.append(dict(side=side, folder=folder, type=TYPE_LABEL[folder], pair=pair, base=base, path=path,
                         n_sweeps=int(get("sweepnum")), sweep_ms=get("sweeplength"), rate=get("samplerate"),
                         n_ch1=len(nb.get(1, [])), n_ch2=len(nb.get(2, [])),
                         has_epa=(path + "_EPA.txt") in z.NameToInfo))
    return pd.DataFrame(rows)


@dataclass
class EPA:
    columns: list            # e.g. T01S01 ...
    mean_amp: np.ndarray     # rows x APs, the file's "Relative ampl." block (pA; see notebook)
    tp: np.ndarray           # rows x APs, the file's "Transmission p." block
    n: np.ndarray            # sweeps per row
    sweeps: np.ndarray       # sweep numbers in table order (1-based)
    block: np.ndarray        # which row (block) each sweep belongs to
    success: np.ndarray      # sweeps x APs, 0/1
    amp: np.ndarray          # sweeps x APs, pA (0 for failures)
    ar_first: int | None     # first column marked "AR" in the mean row (0-based), None if none


def read_epa(z, path: str) -> EPA:
    """Parse an _EPA.txt table (data descriptor, "Data format"). Cells are kept by position; a blank
    cell is NaN."""
    text = z.read(path + "_EPA.txt").decode("latin1")
    sections, cur = [], None
    for line in text.splitlines():
        cells = [c.strip() for c in line.rstrip("\r").split("\t")]
        head = cells[0]
        if head in ("Relative ampl.", "Transmission p.", "Stimulation success", "Amplitude"):
            cur = [head, []]
            sections.append(cur)
        elif head and cur is not None:
            cur[1].append(cells)
    out = {}
    for name, rows in sections:
        out.setdefault(name, []).append(rows)
    ra = out["Relative ampl."][0]
    columns = [c for c in ra[0][1:] if c]
    k = len(columns)
    def val(v):   # blank, "AR" (not described; see notebook) or a stray label: NaN
        try:
            return float(v)
        except ValueError:
            return np.nan
    num = lambda rows: np.array([[val(v) for v in (r[1:] + [""] * k)[:k]] for r in rows])
    mean_amp = num(ra[1:])
    ar = [i for i, v in enumerate((ra[1][1:] + [""] * k)[:k]) if v == "AR"]
    tp = num(out["Transmission p."][0][1:])
    n = np.array([float(r[0]) for r in ra[1:]])
    sw, blk, succ, amp = [], [], [], []
    for b, rows in enumerate(out["Stimulation success"]):
        for r in rows:
            sw.append(int(r[0][3:]))
            blk.append(b)
        succ.append(num(rows))
    for rows in out["Amplitude"]:
        amp.append(num(rows))
    succ, amp = np.vstack(succ), np.vstack(amp) if amp else np.empty((0, k))
    if len(amp) < len(succ):   # a table with fewer amplitude rows than success rows: pad with NaN
        amp = np.vstack([amp, np.full((len(succ) - len(amp), k), np.nan)])
    order = np.argsort(sw)
    return EPA(columns, mean_amp, tp, n, np.array(sw)[order], np.array(blk)[order], succ[order], amp[order],
               ar[0] if ar else None)


# --- raw sweeps --------------------------------------------------------------------------------

@dataclass
class Recording:
    path: str
    rate: float
    pre_channel: int
    post: np.ndarray                 # sweeps x samples, pA
    pre_max: np.ndarray              # per sweep, max of presynaptic Vm (mV)
    ap: list                         # per sweep, AP peak times (ms)
    post_vrange: tuple = field(default=(0, 0))


def detect_aps(v: np.ndarray, rate: float, thr: float = -20.0) -> np.ndarray:
    """AP peak times (ms): upward crossings of -20 mV, the peak within 2 ms after (standard choice)."""
    up = np.flatnonzero((v[1:] >= thr) & (v[:-1] < thr)) + 1
    w = int(2e-3 * rate)
    peaks = [i + int(np.argmax(v[i:i + w])) for i in up]
    return np.array(peaks) / rate * 1e3


def load_recording(z, path: str, n_sweeps: int, rate: float) -> Recording:
    """Read every sweep of both channels; the presynaptic channel is the one with APs (data descriptor,
    "the channel assignment of the pre and postsynaptic cell might change")."""
    ch = {c: np.array([np.frombuffer(z.read(f"{path}_ch{c}_s{s:04d}.bin"), "<f4")
                       for s in range(1, n_sweeps + 1)]) for c in (1, 2)}
    # The membrane potential has brief APs far above a narrow resting range; the current does not.
    def score(x):
        q1, q50, q99 = np.percentile(x, [1, 50, 99], axis=1)
        return np.median((x.max(1) - q50) / (q99 - q1 + 1.0))
    pre = 1 if score(ch[1]) >= score(ch[2]) else 2
    post = 3 - pre
    v = ch[pre]
    return Recording(path, rate, pre, ch[post].astype(np.float32), v.max(1), [detect_aps(x, rate) for x in v],
                     (float(ch[post].min()), float(ch[post].max())))


def classify(ap_ms: np.ndarray) -> str:
    """Protocol from the AP pattern of one sweep (data descriptor, "Stimulation protocols")."""
    n = len(ap_ms)
    isi = np.diff(ap_ms)
    if n == 10 and 900 < np.median(isi) < 1100:
        return "1 Hz"   # the 11th AP of the 1 Hz train falls after the end of the 9419 ms sweep
    if n == 11:
        f = 1000 / np.median(isi[:9])
        return f"{min(FREQS, key=lambda x: abs(np.log(x / f))):d} Hz"
    if n == 5:
        return "RIP"
    if n == 35:
        return "EPI"
    if n == 8:
        return "Recovery"
    return f"other ({n} APs)"


PROTO_BY_LENGTH = {9419.0: "1 Hz", 9420.0: "1 Hz", 3402.0: "5 Hz", 2502.0: "10 Hz", 2052.0: "20 Hz",
                   1827.0: "40 Hz", 1713.6: "80 Hz", 1657.8: "160 Hz", 1629.0: "320 Hz", 1836.0: "Recovery"}
N_AP = {"RIP": 5, "EPI": 35, "Recovery": 8, "1 Hz": 10}


def protocol_of(sweep_ms: float, rec: Recording) -> str:
    """Protocol from the sweep length (one length per protocol, except RIP and EPI, 2411 to 2419 ms,
    told apart by the AP count: 5 against 35)."""
    if sweep_ms in PROTO_BY_LENGTH:
        return PROTO_BY_LENGTH[sweep_ms]
    n = np.median([len(a) for a in rec.ap])
    return "EPI" if n >= 20 else "RIP"


def stim_template(rec: Recording, proto: str):
    """Stimulated AP times of a recording: the median AP times over the sweeps with exactly the expected
    AP count (11 for trains, 10 for 1 Hz, 5 RIP, 35 EPI). Per sweep, which of these APs is present (an AP
    within 1.5 ms); extra APs (spontaneous or doublets) are ignored. Standard choice. Not for the
    recovery protocol, whose interval changes from sweep to sweep (see recovery_sweeps)."""
    n = N_AP.get(proto, 11)
    mod = [a for a in rec.ap if len(a) == n]
    times = np.median(np.array(mod), 0) if mod else np.median(np.array([a[:n] for a in rec.ap if len(a) >= n]), 0)
    present = np.array([[np.any(np.abs(a - t) < 1.5) for t in times] for a in rec.ap])
    return times, present


def recovery_sweeps(rec: Recording):
    """Per sweep of the recovery protocol: the 8 AP times (two RIP bursts) and the interval between the
    last AP of the first burst and the first of the second, rounded to the nearest nominal interval
    (50 to 1200 ms; paper, Methods, protocols paragraph)."""
    out = []
    for a in rec.ap:
        if len(a) < 8:
            out.append((None, np.nan))
            continue
        gap = a[4] - a[3]
        nominal = min(RECOVERY_INTERVALS, key=lambda x: abs(x - gap))
        out.append((a[:8], nominal if abs(nominal - gap) < 15 else np.nan))
    return out


# --- measures on single APs (claims M1, M2) -------------------------------------------------

BASE_WIN = (-4.0, -0.8)   # ms before the AP peak, baseline; standard choice (before the 1 ms stimulus)
RESP_WIN = (0.3, 8.0)     # ms after the AP peak, response window; standard choice
DECAY_WINS = (20.0, 50.0)  # ms after the peak fitted by the single exponential; standard choices, both run


def snippets(rec: Recording, sweep_idx, ap_times, pre=10.0, post=60.0):
    """Baseline-subtracted, sign-flipped (inward positive) current around each (sweep, AP time)."""
    r = rec.rate / 1e3
    n0, n1 = int(pre * r), int(post * r)
    out = []
    for s, t in zip(sweep_idx, ap_times):
        i = int(round(t * r))
        x = rec.post[s, max(i - n0, 0):i + n1].astype(float)
        if len(x) < n0 + n1:
            x = np.pad(x, (0, n0 + n1 - len(x)), constant_values=np.nan)
        b = np.nanmean(x[int((pre + BASE_WIN[0]) * r):int((pre + BASE_WIN[1]) * r)])
        out.append(-(x - b))
    t = (np.arange(n0 + n1) - n0) / r
    return t, np.array(out)


def kinetics(t, y, decay_win=DECAY_WINS[0]):
    """Peak, 10 to 90% rise, latency and decay of an averaged uIPSC y(t) (inward positive, t from AP peak).
    Latency: the intersection of the baseline with the line through the 10 and 90% points
    (paper, Methods, Electrophysiological recordings and analysis, paragraph 6); decay: a single
    exponential fitted from the peak over `decay_win` ms, baseline fixed at 0 (standard choice)."""
    m = (t >= RESP_WIN[0]) & (t <= RESP_WIN[1])
    ip = np.flatnonzero(m)[np.argmax(y[m])]
    P = y[ip]
    res = dict(peak=P, t_peak=t[ip], rise=np.nan, latency=np.nan, tau=np.nan)
    if not np.isfinite(P) or P <= 0:
        return res
    i0 = np.flatnonzero(t >= 0)[0]
    seg = y[i0:ip + 1]

    def cross(level):
        below = np.flatnonzero(seg < level)
        if len(below) == 0:
            return np.nan
        k = below[-1]
        if k + 1 >= len(seg):
            return np.nan
        return t[i0 + k] + (level - seg[k]) / (seg[k + 1] - seg[k]) * (t[1] - t[0])

    t10, t90 = cross(0.1 * P), cross(0.9 * P)
    res["rise"] = t90 - t10
    res["latency"] = t10 - 0.1 * P * (t90 - t10) / (0.8 * P)
    md = (t >= t[ip]) & (t <= t[ip] + decay_win) & np.isfinite(y)
    td, yd = t[md] - t[ip], y[md]
    try:
        p, _ = optimize.curve_fit(lambda x, a, tau: a * np.exp(-x / tau), td, yd, p0=(P, 5.0),
                                  bounds=([0, 0.1], [np.inf, 500]), maxfev=5000)
        res["tau"] = p[1]
    except RuntimeError:
        pass
    return res


def detect_success(t, ys, k=3.0):
    """Claims M2 reading b: a uIPSC is a peak in the response window larger than k standard deviations
    of the pre-AP baseline (standard choice, not the paper's); the SD is taken over the 10 ms before the
    AP of each sweep."""
    mb = (t < BASE_WIN[1])
    mr = (t >= RESP_WIN[0]) & (t <= RESP_WIN[1])
    sd = np.nanstd(ys[:, mb], axis=1)
    return (np.nanmax(ys[:, mr], axis=1) > k * sd).astype(float)


def single_ap_measures(t, ys, success, decay_win=DECAY_WINS[0]):
    """Claims M1: kinetics and potency on the average of successes; amplitude on the average of all
    sweeps; transmission probability the fraction of successes."""
    success = np.asarray(success, bool)
    out = dict(n=len(ys), tp=success.mean() if len(ys) else np.nan)
    allk = kinetics(t, np.nanmean(ys, 0), decay_win) if len(ys) else dict(peak=np.nan)
    out["amplitude"] = allk["peak"]
    if success.sum() >= 1:
        k = kinetics(t, np.nanmean(ys[success], 0), decay_win)
        out.update(potency=k["peak"], rise=k["rise"], latency=k["latency"], tau=k["tau"])
    else:
        out.update(potency=np.nan, rise=np.nan, latency=np.nan, tau=np.nan)
    return out


# --- filtering and the Eq. 6 template ---------------------------------------------------------------

def butter_lowpass(x, rate, fc=100.0, order=4):
    """100 Hz low-pass (paper, Methods, Asynchronous charge calculation); fourth-order zero-phase
    Butterworth is the claims file's named standard choice (fig10bd-be-async-charge)."""
    b, a = signal.butter(order, fc / (rate / 2))
    return signal.filtfilt(b, a, x)


def double_exp(t, A, tr, td):
    """Eq. 6 without the baseline (the averaged trace is baseline-subtracted first)."""
    return np.where(t >= 0, A * (np.exp(-t / td) - np.exp(-t / tr)), 0.0)


# --- asynchronous release (paper, Methods, Asynchronous charge calculation) -------------------------

def mean_trace(rec: Recording, sweeps, base_ms):
    """Sweep-averaged current, sign flipped (inward positive), baseline the mean over `base_ms` (a (start,
    end) window in ms, before the stimulation; standard choice)."""
    r = rec.rate / 1e3
    avg = -np.mean(rec.post[sweeps].astype(float), 0)
    return avg - avg[int(base_ms[0] * r):int(base_ms[1] * r)].mean()


def fit_template(t, y):
    """Eq. 6 (difference of two exponentials) fitted to an averaged IPSC y(t), t in ms from the AP peak;
    the delay is the latency of kinetics() (start of the rising phase; Methods). Fitted from the delay to
    50 ms after it (standard choice). Returns (delay, A, tau_r, tau_d) or None."""
    k = kinetics(t, y, 20.0)
    if not np.isfinite(k["latency"]) or k["peak"] <= 0:
        return None
    d = k["latency"]
    m = (t >= d) & (t <= d + 50) & np.isfinite(y)
    try:
        p, _ = optimize.curve_fit(double_exp, t[m] - d, y[m], p0=(2 * k["peak"], 0.5, 5.0),
                                  bounds=([0, 0.05, 0.3], [1e5, 20, 200]), maxfev=20000)
    except (RuntimeError, ValueError):
        return None
    if p[1] >= p[2]:
        p[1], p[2] = p[2], p[1]
    return (d, *p)


def reconstruct(n, rate, ap_ms, amps, template):
    """Synchronous trace: one template per AP at the AP time plus the delay, each scaled so that its peak is
    the averaged IPSC amplitude at that AP (Methods)."""
    d, A, tr, td = template
    r = rate / 1e3
    t = np.arange(n) / r
    shape = double_exp(np.arange(int(300 * r)) / r, 1.0, tr, td)
    shape = shape / shape.max()
    out = np.zeros(n)
    for ta, a in zip(ap_ms, amps):
        if not np.isfinite(a):
            continue
        i = int(round((ta + d) * r))
        seg = shape[:max(0, min(len(shape), n - i))]
        out[i:i + len(seg)] += a * seg
    return out


def local_amplitudes(y, rate, ap_ms, end_after=10.0):
    """Peak of y between each AP and the next above the current just before the AP (claims M4 b)."""
    r = rate / 1e3
    out = []
    for j, ta in enumerate(ap_ms):
        tn = ap_ms[j + 1] if j + 1 < len(ap_ms) else ta + end_after
        b = y[int(round((ta - 1.3) * r)):int(round((ta - 0.8) * r))].mean()
        seg = y[int(round((ta + 0.3) * r)):int(round(tn * r)) + 1]
        out.append(seg.max() - b if len(seg) else np.nan)
    return np.array(out)


def window_charge(x, rate, t0, t1):
    """Integral of x (pA) from t0 to t1 ms, in pC."""
    r = rate / 1e3
    return x[int(round(t0 * r)):int(round(t1 * r))].sum() / r * 1e-3


def decay_after(y, rate, t_last, mode):
    """Single exponential (with zero offset) fitted to the decay after the last AP: from the peak within
    10 ms of the AP to (a) 500 ms after the AP, or (b) the first point within 5% of the peak (claims,
    decay-epi-vs-160)."""
    r = rate / 1e3
    i0 = int(round(t_last * r))
    ip = i0 + int(np.argmax(y[i0:i0 + int(10 * r)]))
    P = y[ip]
    if mode == "a":
        i1 = i0 + int(500 * r)
    else:
        below = np.flatnonzero(y[ip:] < 0.05 * P)
        i1 = ip + (below[0] if len(below) else len(y) - ip)
    seg = y[ip:min(i1, len(y))]
    tt = np.arange(len(seg)) / r
    if len(seg) < 5 or P <= 0:
        return np.nan
    try:
        p, _ = optimize.curve_fit(lambda x, a, tau: a * np.exp(-x / tau), tt, seg, p0=(P, 20.0),
                                  bounds=([0, 0.1], [np.inf, 5000]), maxfev=20000)
        return p[1]
    except RuntimeError:
        return np.nan


# --- model fits, vectorized over trains (paper, Methods, Modelling, Eqs. 1 to 5) -------------------

MODELS = {"TM dep": (False, False), "TM dep+fac": (False, True), "UDR dep": (True, False), "UDR dep+fac": (True, True)}


def tm_batch(dt, U0, tau_r, tau_f=None, tau_e=None, a_e=None, k_e=None):
    """n(t_j) p(t_j) before each spike for many trains at once. dt: rows x spikes, the interval (s) from the
    previous spike (first column ignored; NaN after the last spike of a row). U0, tau_f: per row; tau_r,
    tau_e, a_e, k_e: scalars. Between spikes the equations are integrated in closed form: 1 - n relaxes with
    rate 1/tau_r, plus k_e ke(t) under UDR (Eq. 3), with ke decaying with tau_e (Eq. 4); p relaxes to p0 with
    tau_f (Eq. 2). At a spike n drops by p n, p rises by p0 (1 - p) and ke by a_e (1 - ke). n = 1 and
    p = p0 before the first spike (Methods)."""
    rows, ns = dt.shape
    n = np.ones(rows)
    p = np.array(U0, float).copy()
    ke = np.zeros(rows)
    out = np.full((rows, ns), np.nan)
    for j in range(ns):
        if j > 0:
            d = np.nan_to_num(dt[:, j])
            if tau_f is not None:
                p = U0 + (p - U0) * np.exp(-d / tau_f)
            if tau_e is None:
                n = 1 - (1 - n) * np.exp(-d / tau_r)
            else:
                n = 1 - (1 - n) * np.exp(-d / tau_r - k_e * ke * tau_e * (1 - np.exp(-d / tau_e)))
                ke = ke * np.exp(-d / tau_e)
        out[:, j] = n * p
        n = n - p * n
        if tau_f is not None:
            p = p + U0 * (1 - p)
        if tau_e is not None:
            ke = ke + a_e * (1 - ke)
    out[np.isnan(dt) & (np.arange(ns) > 0)] = np.nan
    return out


def fit_model(dt, y, conn, model, weight=None, starts=4, rng=None):
    """Fit one of the four models to the mean amplitudes y (rows x spikes, pA) of trains with intervals dt
    (s), row r belonging to connection conn[r]. Per connection: U0, A (Imax) and, with facilitation, tau_f;
    per type (shared): tau_r and, with UDR, tau_e, a_e, k_e (Table 4 legend). weight: per-row factor on
    the residuals (claims fig11-model-pv-udr reading b), None for unweighted. Several starting points
    (a standard choice); the best fit by the summed squared error is returned. BIC = N ln(SSE/N) + k ln N
    (claims fig11-model-pv-udr reading a)."""
    udr, fac = MODELS[model]
    nc = int(conn.max()) + 1
    w = np.ones(len(y)) if weight is None else weight
    mask = np.isfinite(y) & np.isfinite(np.where(np.arange(y.shape[1]) == 0, 0, dt))
    sig = lambda x: 1 / (1 + np.exp(-x))

    def unpack(th):
        i = 0
        U0 = sig(th[i:i + nc]); i += nc
        A = np.exp(th[i:i + nc]); i += nc
        tf = None
        if fac:
            tf = np.exp(th[i:i + nc]); i += nc
        tr = np.exp(th[i]); i += 1
        te = ae = ke = None
        if udr:
            te, ae, ke = np.exp(th[i]), sig(th[i + 1]), np.exp(th[i + 2]); i += 3
        return U0, A, tf, tr, te, ae, ke

    def resid(th):
        U0, A, tf, tr, te, ae, ke = unpack(th)
        m = tm_batch(dt, U0[conn], tr, None if tf is None else tf[conn], te, ae, ke)
        r = (A[conn][:, None] * m - y) * w[:, None]
        return np.where(mask, r, 0.0)[mask]

    rng = rng or np.random.default_rng(0)
    best = None
    for s in range(starts):
        th0 = [np.log(np.full(nc, 0.3) / 0.7) + rng.normal(0, 0.5, nc),
               np.log(np.nanmax(y, 1).max() * np.ones(nc) * 1.5)]
        if fac:
            th0.append(np.log(np.full(nc, 0.05)) + rng.normal(0, 1, nc))
        th0.append([np.log(rng.uniform(0.1, 3.0))])
        if udr:
            th0.append([np.log(rng.uniform(0.005, 0.05)), rng.normal(0, 1), np.log(rng.uniform(1, 30))])
        th0 = np.concatenate([np.ravel(x) for x in th0])
        try:
            res = optimize.least_squares(resid, th0, method="trf", max_nfev=3000, x_scale="jac")
        except (ValueError, FloatingPointError):
            continue
        if best is None or res.cost < best.cost:
            best = res
    U0, A, tf, tr, te, ae, ke = unpack(best.x)
    r = resid(best.x)
    n_obs = len(r)
    k = len(best.x)
    sse = float((r ** 2).sum())
    return dict(model=model, sse=sse, n=n_obs, k=k, bic=n_obs * np.log(sse / n_obs) + k * np.log(n_obs),
                U0=U0, A=A, tau_f=tf, tau_r=tr, tau_e=te, a_e=ae, k_e=ke)


def refit_A(dt, y, conn, fit):
    """Test data: model shape with the fitted parameters, only A refitted per connection (Fig. 11 legend);
    returns the mean squared error over the test amplitudes."""
    m = tm_batch(dt, fit["U0"][conn], fit["tau_r"], None if fit["tau_f"] is None else fit["tau_f"][conn],
                 fit["tau_e"], fit["a_e"], fit["k_e"])
    err = []
    for c in np.unique(conn):
        rows = conn == c
        mm, yy = m[rows], y[rows]
        ok = np.isfinite(mm) & np.isfinite(yy)
        A = (mm[ok] * yy[ok]).sum() / (mm[ok] ** 2).sum()
        err.append((A * mm[ok] - yy[ok]) ** 2)
    e = np.concatenate(err)
    return float(e.mean())
