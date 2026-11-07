"""Loading and measures for CRCNS hc-24 (Varela & Wilson 2020, eLife 9:e48881).

The data set is one zip file, `hc-24/live/data.zip`, in the public S3 bucket `crcnsarchive`. It is
opened in place over HTTP range requests (fsspec and zipfile) and each member is read into memory;
nothing is written to disk. CRCNS data sets are not versioned; the version is pinned by the MD5
sum of data.zip given in the data set's checksums.md5 (`DATA_ZIP_MD5`), which `verify_md5`
recomputes from the stream.

The zip holds three sessions from three rats (data descriptor, version 0.6):

- Session1_PETHphaseLocking: LFP of mPFC, thalamus and CA1 at 600 Hz; units and tetrode
  multi-unit spikes (MUA) from one thalamic (MD, from the title of the deposited script
  PeriEventHistogramsThreeSites.mlx), two mPFC and three CA1 tetrodes; derived sleep periods,
  KCs, spindle troughs and SWRs.
- Session2_ThalPairCorrelations: mPFC LFP only and two units, thalamic by the deposited script
  PairCorrelationSleep.mlx ("Spindle Co-activation of Thalamic Pairs"), no MUA; derived sleep
  periods, KCs, spindle troughs and spindle cycle start and end times.
- Session3_SleepAfterRun: LFP of the three regions, one mPFC unit and MUA, two thalamic units and
  MUA, and eight CA1 units split into "UnitsInRun" and "UnitsNotInRun" (no CA1 MUA); derived
  sleep periods, KCs, spindle troughs split into high and low ripple power cycles, SWRs inside
  spindle cycles and an equal sample of SWRs outside them.

Unit and MUA files are 5-column matrices, peak amplitudes on 4 wires and the time in seconds
(column 5).

Where the parameters come from (the claims file's labels, M-..., cite the paper):

- Filters (M-filter; Methods, LFP state and event detection, paragraph 1): zero-phase FIR
  band-pass, Blackman window, order 6 x fs / bandwidth; delta 1-4 Hz, spindle 6-14 Hz, ripple
  100-275 Hz. The deposited scripts use order 6 x fs / low cutoff; the Methods come first.
- KC (M-KC; Methods, paragraph 3): delta-filtered mPFC LFP, positive values set to 0, squared,
  local maxima above mean + 4 sd, mean and sd from the sleep periods (reading a) or all the
  recording (reading b, a stand-in for "quiet states", as the data set has no position data).
- Spindle troughs (M-spindle): reading (a) local minima of the spindle-filtered LFP below its
  mean - 3 sd (Methods); reading (b) local minima where the squared trace exceeds mean + 3 sd of
  the squared trace (Results). A cycle runs from the peak before to the peak after the trough
  (Results, Sparse thalamic firing, paragraph 5).
- SWR (M-SWR; Methods, paragraph 3): squared ripple-filtered CA1 LFP above mean + k sd for at
  least 20 ms, events closer than 20 ms merged, timestamp at the largest absolute filtered value;
  k = 3 (Methods) or 4 (Results).
- PETH (M-PETH; Methods, Correlation quantifications, paragraph 1): 15 ms bins, Gaussian of 15 ms
  sd, null from 100 shifts of all event times by one uniform random 1.5 to 2.5 s, z per bin from
  the null mean and sd. The window of +-1 s is a standard choice (claims file). The direction of
  the shift is open; `sign="forward"` (reading a) or `"random"` (reading b).
- Phase (M-phase; Methods, Phase-locking analyses): Hilbert phase of the delta- or
  spindle-filtered mPFC LFP, 0 at the peak and +-pi at the trough. The spike phase histogram is
  divided by the phase distribution of the whole filtered LFP in non-REM sleep. The deposited
  script PhaseLockingCA1UnitsPFCSpindles.mlx (Session 3) settles how the normalisation enters
  the Rayleigh test, the claims file's reading (a): the corrected histogram, rescaled to the spike
  count, is tested with circ_rtest on the bin angles as weights, with bins of 0.2 rad from -pi
  (31 bins; the script uses the left edges as the bin angles). `rayleigh_binned` follows it; the
  script passes no bin spacing to circ_rtest, so no bin-spacing correction is applied. Reading
  (b) tests the raw spike phases. The von Mises kappa is estimated from the mean resultant length
  (circ_kappa). `script_text` returns the code of a deposited live script, so the notebook can
  quote the lines it relies on.
- Sleep (M-sleep readings b and c; Methods, paragraph 2, and Figure 1C legend): mPFC delta power
  and CA1 ripple power, each the moving average of the squared filtered LFP over 1 s (b) or 10 s
  (c), both above their session mean for at least 2 min. The windows are the claims file's
  choices. Session 2 has no CA1 LFP, so there the rule uses delta power alone (a choice).
- Modulation index (fig6 family; Results, Spindle activation, paragraph 2): (max - min) / mean of
  the raw-rate peri-trough histogram (M-PETH bins and smoothing) in -100 to 100 ms. The
  histogram is built and smoothed over +-1 s (the M-PETH window) and then cropped, so that the
  smoothing has no edge effect inside the window.
- Bursts (M-burst): spikes with inter-spike intervals under 5 ms whose first spike follows at
  least 70 ms of silence; the leading spike counts.
- Statistics (M-stats): two-sided tests at alpha 0.05.
"""

from __future__ import annotations

import hashlib
import html
import io
import re
import zipfile
from functools import lru_cache

import fsspec
import numpy as np
import scipy.io as sio
from scipy import signal, stats

URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-24/live/data.zip"
DATASET = "crcns:hc-24/unversioned"
DATASET_DOI = "10.6080/K0K35RVG"
DATA_ZIP_MD5 = "de9fd5ca07fe2b004342aedf18357b22"   # hc-24/live/checksums.md5
FS = 600.0

BANDS = {"delta": (1.0, 4.0), "spindle": (6.0, 14.0), "ripple": (100.0, 275.0)}
SESSIONS = ["Session1_PETHphaseLocking", "Session2_ThalPairCorrelations", "Session3_SleepAfterRun"]
SHORT = {"Session1_PETHphaseLocking": "S1", "Session2_ThalPairCorrelations": "S2",
         "Session3_SleepAfterRun": "S3"}

PETH_BIN = 0.015
PETH_SD = 0.015
PETH_WIN = 1.0
N_SHIFTS = 100
PHASE_BIN = 0.2


# ----------------------------------------------------------------------------- loading

@lru_cache(maxsize=1)
def _zip():
    f = fsspec.open(URL, block_size=2**20).open()
    return zipfile.ZipFile(f)


def members():
    return [i for i in _zip().infolist()]


def _mat(name):
    d = sio.loadmat(io.BytesIO(_zip().read(name)))
    return {k: v for k, v in d.items() if not k.startswith("__")}


def script_text(name):
    """Code and text of a deposited MATLAB live script (.mlx, itself a zip holding
    matlab/document.xml), one line per list item."""
    xml = zipfile.ZipFile(io.BytesIO(_zip().read(name))).read("matlab/document.xml").decode()
    xml = re.sub(r"<!\[CDATA\[(.*?)\]\]>", lambda m: html.escape(m.group(1)), xml, flags=re.S)
    text = html.unescape(re.sub(r"<[^>]+>", "\n", xml))
    return [ln.rstrip() for ln in text.splitlines() if ln.strip()]


def verify_md5(chunk=8 * 2**20):
    """MD5 of data.zip, streamed in chunks (nothing written to disk)."""
    h = hashlib.md5()
    with fsspec.open(URL, block_size=chunk) as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def _region(path):
    """Region of a spike file from its folder name; Session 2's folder names none."""
    p = path.upper()
    if "THAL" in p:
        return "THAL"
    if "PFC" in p:
        return "PFC"
    if "CA1" in p:
        return "CA1"
    return None


def load_session(session):
    """Everything in one session: LFPs, units, MUA and derived events, times in seconds."""
    names = [n for n in _zip().namelist() if n.startswith(f"data/{session}/") and n.endswith(".mat")]
    out = {"name": session, "short": SHORT[session], "lfp": {}, "units": [], "mua": [], "derived": {}}
    for n in names:
        base = n.split("/")[-1]
        if "Timestamp_LFP" in base:
            out["t"] = _mat(n)["timestamp"].ravel().astype(float)
        elif "_LFP_600Hz" in base:
            key = base.split("_")[0]          # PFC, THAL, HC
            out["lfp"][key] = _mat(n)[f"{key}_LFP"].ravel().astype(float)
        elif "PeakAmpTime" in base:
            d = _mat(n)
            arr = d.get("unitdata", d.get("muadata"))
            folder = n.split("/")[-2]
            region = _region(folder)
            if region is None:                 # Session 2: thalamic by its deposited script
                region = "THAL"
            rec = {"session": SHORT[session], "region": region, "folder": folder, "file": base,
                   "spikes": np.sort(arr[:, 4].astype(float)), "n_raw": len(arr),
                   "sorted": bool(np.all(np.diff(arr[:, 4]) >= 0)),
                   "amp": arr[:, :4]}
            if "InRun" in base or "InRun" in folder:
                rec["run"] = "NotInRun" not in folder
            m = re.match(r"(E\d)?cl-", base)
            rec["tetrode"] = folder if not (m and m.group(1)) else f"{folder}:{m.group(1)}"
            if region == "CA1" and session.startswith("Session3"):
                rec["tetrode"] = "CA1:" + (m.group(1) if m and m.group(1) else "?")
            rec["id"] = f"{SHORT[session]}/{folder}/{base.replace('PeakAmpTime', '').replace('.mat', '')}"
            (out["mua"] if base.startswith("mua") else out["units"]).append(rec)
        else:
            d = _mat(n)
            for k, v in d.items():
                out["derived"][k] = np.asarray(v, dtype=float).squeeze() if v.size else np.asarray(v)
    out["sleep"] = np.atleast_2d(out["derived"]["nremSleep"]).astype(float)
    out["kc_dep"] = np.sort(out["derived"]["KC_timestamp"].ravel())
    if "SP_timestamp" in out["derived"]:
        out["sp_dep"] = np.sort(out["derived"]["SP_timestamp"].ravel())
    else:  # Session 3: troughs split by ripple power
        out["sp_dep"] = np.sort(np.concatenate([out["derived"]["SpindleTroughsHiRiPow"].ravel(),
                                                out["derived"]["SpindleTroughsLoRiPow"].ravel()]))
    if "SWR_timestamp" in out["derived"]:
        out["swr_dep"] = np.sort(out["derived"]["SWR_timestamp"].ravel())
    return out


# ----------------------------------------------------------------------------- filters

def fir(band, fs=FS):
    lo, hi = band
    n = int(np.ceil(6 * fs / (hi - lo)))
    if n % 2:
        n += 1
    return signal.firwin(n + 1, [lo, hi], pass_zero=False, window="blackman", fs=fs)


def bandpass(x, band, fs=FS):
    b = fir(band, fs)
    return signal.filtfilt(b, [1.0], x)


def in_periods(t, periods):
    t = np.asarray(t)
    m = np.zeros(t.shape, bool)
    for a, b in periods:
        m |= (t >= a) & (t <= b)
    return m


def total_time(periods):
    return float(sum(b - a for a, b in periods))


def complement(periods, start, end):
    out, cur = [], start
    for a, b in sorted(map(tuple, periods)):
        if a > cur:
            out.append((cur, a))
        cur = max(cur, b)
    if cur < end:
        out.append((cur, end))
    return np.array(out)


def detect_sleep(t, powers, window, min_dur=120.0, bridge=0.0, fs=FS):
    """Periods where every trace in `powers` (filtered LFPs) has moving-average power above its
    session mean for at least `min_dur` s (M-sleep readings b and c). `bridge` > 0 first fills
    dips shorter than `bridge` s (a variant, not the rule as written)."""
    n = max(int(round(window * fs)), 1)
    above = np.ones(len(t), bool)
    for x in powers:
        p = np.convolve(x ** 2, np.ones(n) / n, mode="same")
        above &= p > p.mean()
    d = np.diff(np.r_[0, above.astype(int), 0])
    st, en = np.where(d == 1)[0], np.where(d == -1)[0]
    if bridge > 0 and len(st) > 1:
        keep = np.r_[True, (st[1:] - en[:-1]) / fs >= bridge]
        st, en = st[keep], np.r_[en[:-1][keep[1:]], en[-1]]
    keep = (en - st) / fs >= min_dur
    return np.c_[t[st[keep]], t[en[keep] - 1]]


# ----------------------------------------------------------------------------- events

def local_extrema(x, kind):
    if kind == "max":
        return np.where((x[1:-1] > x[:-2]) & (x[1:-1] >= x[2:]))[0] + 1
    return np.where((x[1:-1] < x[:-2]) & (x[1:-1] <= x[2:]))[0] + 1


def detect_kc(t, delta, ref_mask, sleep_mask, k=4.0):
    r = np.minimum(delta, 0.0) ** 2
    thr = r[ref_mask].mean() + k * r[ref_mask].std()
    idx = local_extrema(r, "max")
    idx = idx[(r[idx] > thr) & sleep_mask[idx]]
    return t[idx], idx


def detect_spindle_troughs(t, sp, ref_mask, sleep_mask, reading="a", k=3.0):
    idx = local_extrema(sp, "min")
    if reading == "a":
        thr = sp[ref_mask].mean() - k * sp[ref_mask].std()
        keep = sp[idx] < thr
    else:
        sq = sp ** 2
        keep = sq[idx] > sq[ref_mask].mean() + k * sq[ref_mask].std()
    idx = idx[keep & sleep_mask[idx]]
    return t[idx], idx


def refine_to_trough(raw, idx, half=60):
    """Move each KC to the raw mPFC LFP minimum within +-100 ms (60 samples): the paper triggers KC
    histograms on the trough (Results, opening section, paragraph 1), and the deposited KC times
    sit on it (data check). The 100 ms half-window is a choice; the deposited times fit it."""
    out = []
    for k in idx:
        a, b = max(k - half, 0), min(k + half + 1, len(raw))
        out.append(a + np.argmin(raw[a:b]))
    return np.unique(np.array(out, int))


def spindle_cycles(t, sp, trough_idx):
    """Start and end of each cycle: the spindle-filtered peaks before and after each trough."""
    peaks = local_extrema(sp, "max")
    j = np.searchsorted(peaks, trough_idx)
    ok = (j > 0) & (j < len(peaks))
    st = np.full(len(trough_idx), np.nan)
    en = np.full(len(trough_idx), np.nan)
    st[ok] = t[peaks[j[ok] - 1]]
    en[ok] = t[peaks[j[ok]]]
    pk_before = np.full(len(trough_idx), -1)
    pk_after = np.full(len(trough_idx), -1)
    pk_before[ok] = peaks[j[ok] - 1]
    pk_after[ok] = peaks[j[ok]]
    return st, en, pk_before, pk_after


def detect_swr(t, rip, ref_mask, sleep_mask, k=3.0, min_dur=0.020, merge=0.020):
    sq = rip ** 2
    thr = sq[ref_mask].mean() + k * sq[ref_mask].std()
    above = (sq > thr) & sleep_mask
    d = np.diff(above.astype(int))
    st = np.where(d == 1)[0] + 1
    en = np.where(d == -1)[0] + 1
    if above[0]:
        st = np.r_[0, st]
    if above[-1]:
        en = np.r_[en, len(above)]
    # merge events closer than `merge`
    if len(st):
        gap = (st[1:] - en[:-1]) / FS
        keep = np.r_[True, gap >= merge]
        grp = np.cumsum(keep) - 1
        st2 = st[keep]
        en2 = np.array([en[grp == g].max() for g in range(grp.max() + 1)]) if len(st) else en
        st, en = st2, en2
    dur = (en - st) / FS
    st, en = st[dur >= min_dur], en[dur >= min_dur]
    peak = np.array([s + np.argmax(np.abs(rip[s:e])) for s, e in zip(st, en)], dtype=int)
    return t[peak] if len(peak) else np.array([]), np.c_[t[st], t[np.minimum(en, len(t) - 1)]] if len(st) else np.zeros((0, 2))


# ----------------------------------------------------------------------------- histograms

def _gauss_kernel(sd_bins):
    half = int(np.ceil(4 * sd_bins))
    x = np.arange(-half, half + 1)
    k = np.exp(-0.5 * (x / sd_bins) ** 2)
    return k / k.sum()


class SpikeGrid:
    """Sorted spike times; exact counts in windows around events (as MATLAB histcounts)."""

    def __init__(self, spikes, t0=None, t1=None):
        self.spikes = np.sort(np.asarray(spikes, float))

    def counts(self, events, edges):
        q = np.asarray(events)[:, None] + edges[None, :]
        return np.diff(np.searchsorted(self.spikes, q.ravel()).reshape(q.shape), axis=1)


def peth_counts(spikes, events, edges, grid=None):
    """Mean spike count per event per bin."""
    if len(events) == 0:
        return np.zeros(len(edges) - 1)
    g = grid if grid is not None else SpikeGrid(spikes, min(np.min(events), np.min(spikes)), max(np.max(events), np.max(spikes)))
    return g.counts(events, edges).mean(axis=0)


def peth_z(spikes, events, rng, win=PETH_WIN, bin=PETH_BIN, sd=PETH_SD, n_shifts=N_SHIFTS,
           sign="forward", smooth=True, null_events=None):
    """Peri-event histogram (spikes/s), smoothed, and its z score against shifted-event nulls.

    Every repetition shifts all events by one uniform random amount in 1.5 to 2.5 s (M-PETH), forward
    or with a random sign. `null_events` replaces the shifted events by given null sets.
    Returns centres, rate, z, null mean, null sd.
    """
    nb = int(round(win / bin))
    edges = (np.arange(-nb, nb + 2) - 0.5) * bin
    centres = (edges[:-1] + edges[1:]) / 2
    ker = _gauss_kernel(sd / bin) if smooth else np.array([1.0])
    f = lambda h: np.convolve(h, ker, mode="same") / bin
    if len(spikes) == 0 or len(events) == 0:
        nanv = np.full(len(centres), np.nan)
        return centres, nanv, nanv, nanv, nanv
    grid = SpikeGrid(spikes, min(np.min(events), np.min(spikes)) - 3, max(np.max(events), np.max(spikes)) + 3)
    obs = f(peth_counts(spikes, events, edges, grid))
    nulls = []
    if null_events is None:
        for _ in range(n_shifts):
            s = rng.uniform(1.5, 2.5)
            if sign == "random" and rng.random() < 0.5:
                s = -s
            nulls.append(f(peth_counts(spikes, events + s, edges, grid)))
    else:
        for ev in null_events:
            nulls.append(f(peth_counts(spikes, ev, edges, grid)))
    nulls = np.array(nulls)
    mu, sdv = nulls.mean(0), nulls.std(0, ddof=1)
    sdv = np.where(sdv > 0, sdv, np.nan)
    return centres, obs, (obs - mu) / sdv, mu, sdv


def window(centres, lo, hi):
    return (centres >= lo - 1e-9) & (centres <= hi + 1e-9)


def modulation_index(counts_fn, half=0.1, win=PETH_WIN, bin=PETH_BIN, sd=PETH_SD):
    """(max - min) / mean of a histogram in -half..half, the histogram smoothed (Gaussian, M-PETH)
    over +-win and then cropped. `counts_fn(edges)` returns the counts in the given bin edges."""
    nb = int(round(win / bin))
    edges = (np.arange(-nb, nb + 2) - 0.5) * bin
    c = (edges[:-1] + edges[1:]) / 2
    h = np.convolve(counts_fn(edges), _gauss_kernel(sd / bin), mode="same")[window(c, -half, half)]
    return float((h.max() - h.min()) / h.mean()) if h.mean() > 0 else np.nan


def autocorr(spikes, bin, maxlag):
    """Autocorrelogram (spike counts at each lag, lag 0 removed), lags in bins to maxlag."""
    nb = int(round(maxlag / bin))
    edges = (np.arange(-nb, nb + 2) - 0.5) * bin
    q = spikes[:, None] + edges[None, :]
    c = np.searchsorted(spikes, q.ravel()).reshape(q.shape)
    h = np.diff(c, axis=1).sum(0).astype(float)
    centres = (edges[:-1] + edges[1:]) / 2
    h[np.argmin(np.abs(centres))] -= len(spikes)
    return centres, h


def xcorr(a, b, bin, maxlag, shift=0.0):
    """Cross-correlogram, exact counts (as MATLAB histcounts): spikes of b at each lag from the
    spikes of a, with b shifted by `shift`."""
    nb = int(round(maxlag / bin))
    edges = (np.arange(-nb, nb + 2) - 0.5) * bin
    q = (a - shift)[:, None] + edges[None, :]
    c = np.searchsorted(b, q.ravel()).reshape(q.shape)
    return (edges[:-1] + edges[1:]) / 2, np.diff(c, axis=1).sum(0).astype(float)


# ----------------------------------------------------------------------------- phase

def phase_at(t_lfp, phase, times):
    i = np.clip(np.searchsorted(t_lfp, times), 1, len(t_lfp) - 1)
    i = np.where(np.abs(t_lfp[i - 1] - times) < np.abs(t_lfp[i] - times), i - 1, i)
    return phase[i]


PHASE_EDGES = np.arange(-np.pi, np.pi + 1e-9, PHASE_BIN)   # as bins = -pi:0.2:pi in the scripts
PHASE_ANGLES = PHASE_EDGES[:-1]                             # the scripts use the left edges


def phase_hist(ph):
    return np.histogram(ph, PHASE_EDGES)[0].astype(float)


def normalized_hist(spike_ph, ref_ph):
    """Spike phase histogram divided by the reference phase distribution, rescaled to the count."""
    h = phase_hist(spike_ph)
    ref = phase_hist(ref_ph)
    ref = ref / ref.sum()
    c = np.where(ref > 0, h / ref, 0.0)
    return h.sum() * c / c.sum() if c.sum() > 0 else c


def circ_r(alpha, w=None, d=0.0):
    w = np.ones_like(alpha) if w is None else w
    r = np.abs(np.sum(w * np.exp(1j * alpha))) / np.sum(w)
    if d:
        r = r * (d / 2) / np.sin(d / 2)
    return r


def circ_mean(alpha, w=None):
    w = np.ones_like(alpha) if w is None else w
    return float(np.angle(np.sum(w * np.exp(1j * alpha))))


def circ_std(alpha, w=None):
    """Circular standard deviation sqrt(2 (1 - R)), as circ_std of the circular statistics toolbox."""
    return float(np.sqrt(2 * (1 - circ_r(alpha, w))))


def rayleigh(alpha, w=None, d=0.0):
    """Rayleigh test as circ_rtest (Berens 2009), with weights and bin spacing d."""
    w = np.ones_like(alpha) if w is None else w
    n = np.sum(w)
    r = circ_r(alpha, w, d)
    R = n * r
    z = R ** 2 / n
    p = np.exp(np.sqrt(1 + 4 * n + 4 * (n ** 2 - R ** 2)) - (1 + 2 * n))
    return float(min(p, 1.0)), float(z)


def rayleigh_binned(hist):
    """As the deposited script: circ_rtest(bins(1:end-1), hist), with no bin spacing given, so the
    toolbox applies no bin-spacing correction (d = 0)."""
    return rayleigh(PHASE_ANGLES, hist)


def circ_kappa(r, n=None):
    """Concentration from mean resultant length, as circ_kappa (Fisher 1993); r is capped just
    below 1."""
    r = min(float(r), 0.999)
    if r < 0.53:
        k = 2 * r + r ** 3 + 5 * r ** 5 / 6
    elif r < 0.85:
        k = -0.4 + 1.39 * r + 0.43 / (1 - r)
    else:
        k = 1 / (r ** 3 - 4 * r ** 2 + 3 * r)
    if n is not None and n < 15:
        k = max(k - 2 / (n * k), 0) if k < 2 else (n - 1) ** 3 * k / (n ** 3 + n)
    return float(k)


def phase_summary(spike_ph, ref_ph):
    """Mean phase, kappa and Rayleigh p, from the normalised histogram (reading a) and from raw
    spike phases (reading b)."""
    h = normalized_hist(spike_ph, ref_ph)
    pa, za = rayleigh_binned(h)
    ma = circ_mean(PHASE_ANGLES + PHASE_BIN / 2, h)
    ka = circ_kappa(circ_r(PHASE_ANGLES + PHASE_BIN / 2, h))
    pb, zb = rayleigh(spike_ph)
    mb = circ_mean(spike_ph)
    return {"n": len(spike_ph), "mean_a": ma, "kappa_a": ka, "p_a": pa, "z_a": za,
            "mean_b": mb, "p_b": pb, "z_b": zb}


# ----------------------------------------------------------------------------- bursts

def burst_mask(spikes, isi=0.005, silence=0.070):
    """Spikes that belong to bursts (M-burst): a run of ISIs < 5 ms whose first spike follows at
    least 70 ms of silence; the leading spike counts."""
    s = np.asarray(spikes)
    n = len(s)
    m = np.zeros(n, bool)
    if n < 2:
        return m
    d = np.diff(s)
    prev = np.r_[np.inf, d]
    i = 0
    while i < n - 1:
        if prev[i] >= silence and d[i] < isi:
            j = i
            while j < n - 1 and d[j] < isi:
                j += 1
            m[i:j + 1] = True
            i = j + 1
        else:
            i += 1
    return m


# ----------------------------------------------------------------------------- stats helpers

def wilcoxon(x, y=None):
    x = np.asarray(x, float)
    d = x if y is None else x - np.asarray(y, float)
    d = d[np.isfinite(d)]
    if len(d) == 0 or np.all(d == 0):
        return np.nan
    return float(stats.wilcoxon(d).pvalue)


def mannwhitney(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    x, y = x[np.isfinite(x)], y[np.isfinite(y)]
    if len(x) == 0 or len(y) == 0:
        return np.nan
    return float(stats.mannwhitneyu(x, y, alternative="two-sided").pvalue)


def min_wilcoxon_p(n):
    """Smallest two-sided p an exact Wilcoxon signed rank test can give with n pairs."""
    return 2.0 / 2 ** n if n > 0 else np.nan


def within(v, value, tol):
    return bool(np.isfinite(v) and abs(v - value) <= tol + 1e-12)
