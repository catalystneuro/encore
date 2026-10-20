"""Loading and measures for dandiset 000005 (Yu, Gutnisky, Hires & Svoboda 2016).

Yu J, Gutnisky DA, Hires SA, Svoboda K (2016). Layer 4 fast-spiking interneurons filter
thalamocortical signals during active somatosensation. Nat Neurosci 19:1647-1657,
doi:10.1038/nn.4412.

The dandiset holds two kinds of file, one session each:

- `behavior+ecephys`: chronic silicon probe recordings in VPM, a few sorted units per file
  (spike times), with whisker angle, curvature, touch onsets and offsets of the principal whisker
  and its neighbours at 1 kHz, and a lick trace.
- `behavior+icephys(+ogen)`: one L4 neuron per file, recorded whole-cell or cell-attached, as a
  `CurrentClampSeries` at 10 or 20 kHz, the injected current, whisker variables and touches at
  1 kHz (5 s per trial), a lick trace and, in most files, one or two photostimulation series.

Files are streamed from the archive at the pinned version; nothing is written to disk. Each file
is reduced as it loads (in a worker process) to what the claims use: spike times, the whisking
epochs of the principal whisker under both filter readings, touches, licks, light epochs and, for
whole-cell recordings, the membrane potential with spikes removed (averaged into the 1 ms bins of
the whisker clock), spike thresholds and full-rate event-aligned averages.

Where each parameter comes from. "Claims" means the claims file
(claims/000005/10.1038-nn.4412.yaml), whose header and criteria cite the paper's Online Methods,
legends and supplement. "Standard" marks a choice for a detail the claims file does not fix and
that the notebook either shows cannot change a result or runs under each reading.

- Whisking (claims, Measures): angle band-passed 6 to 60 Hz with a 4th-order Butterworth filter,
  zero-phase (`filtfilt`, reading O1 a) or a single forward pass (`lfilter`, O1 b); Hilbert
  amplitude and phase (phase 0 most protracted). Whisking epochs are whisking cycles (from one
  most-retracted point, phase wrapping from +pi to -pi, to the next) whose amplitude where the
  phase crosses 0 exceeds 2.5 degrees, leaving out 100 ms around licks and 10 ms before to 100 ms
  after touches. Nonwhisking periods are runs of at least 100 ms with amplitude below 1.25 degrees,
  outside touches and the same lick and touch windows. Standard: the touch window runs from 10 ms
  before a touch onset to 100 ms after its offset, and touches of every tracked whisker count;
  lick times are the rising edges of the lick trace.
- Whisking onsets (claims, Measures): the end of a nonwhisking period, when the mean amplitude
  100 to 300 ms after it exceeds the mean 0 to 200 ms before it by at least 2 degrees and no touch
  starts within 250 ms; data after a touch starting later are removed. Standard: the two windows
  over which the amplitude rise is judged are the paper's whisking-onset windows (Supplementary
  Fig. 4 legend), since the Methods give no window for "average whisking amplitude increased".
- Touches (claims): onsets of the principal whisker; intertouch interval (offset of the previous
  touch to this onset) at least 25 ms (Figs. 1 to 7) or 10 ms (Fig. 8e); the first touch of a
  trial counts as isolated.
- Spikes per touch (claims): cortical Fig. 5, spikes 0 to 50 ms after minus 2 x spikes 0 to 25 ms
  before; cortical Fig. 8e, spikes 4 to 20 ms after minus 0 to 16 ms before; VPM, 0 to 25 ms after
  minus 0 to 25 ms before; averaged over touches, 95% bootstrap interval over touches with 1,000
  draws.
- Spike latency (claims): touch PSTH in 1 ms bins, first difference (O8), first bin after onset
  where it exceeds 3 x its s.d. 0 to 25 ms before onset; cells without a 1 ms bin of at least 10
  spikes/s 0 to 100 ms after onset, or without a crossing, are left out. The time given to the
  crossing bin is either its left edge or its centre; both are returned (standard: the claims file
  does not say, see the notebook).
- Phase coupling (claims): 12 phase bins over -pi to pi, rate = spikes / time spent in each bin
  during whisking epochs (or mean Vm per bin); least-squares fit of a + b cos + c sin, r2 = 1 -
  SSres / SStot; coupling strength = half the peak-to-trough of the fit; for FS cells a fit with
  the second harmonic added is used when its r2 is at least 1.5 times that of the single fit.
- Whole-cell spikes (standard; the paper gives no detection rule): peaks of at least
  `WC_PROMINENCE_MV` prominence with a rate of rise of at least `WC_MIN_DVDT` in the 1 ms before.
  Cell-attached spikes (standard): the trace high-passed at 300 Hz, polarity from the larger tail,
  peaks above `JX_THRESHOLD_SD` robust s.d. Detection runs over the first 5 s of each trial (the
  whisker video) and stops before the series-resistance test pulse at the end of the trial.
- Spike threshold (claims, O3): the membrane potential at the first sample, in the 3 ms before a
  spike's peak, where dVm/dt exceeds its trial mean by 3 s.d. (O3 a) or exceeds 3 s.d. (O3 b);
  per trial from a linear fit of threshold against trial number; -42 mV for silent cells.
- Spike removal (claims): Vm interpolated from 1 ms before to 4 ms after each spike (standard:
  times taken from the spike's peak).
- Waveforms. Whole-cell: full width at half maximum of the mean spike (paper, Online Methods).
  Cell-attached (Supplementary Fig. 6, read from its inset; standard where the inset leaves it
  open): the mean spike of the trace high-passed at 300 Hz, its larger deflection made positive;
  peak = the positive maximum, trough = the minimum in the 1.5 ms after it, both from the baseline,
  ratio = peak / |trough|; duration = time from peak to trough (the Methods give an
  "extracellular ... spike peak to trough duration, 0.21 ms"). The FS boundary (claims header, an
  approximate reading of the figure) is duration below 0.27 ms and ratio below 2.8.
- Light (standard): light epochs are read from the photostimulation series (contiguous samples
  above zero); isolated 5 ms pulses are pulses shorter than 7.5 ms with no other pulse within
  100 ms. A cell is driven by light (claims header: "driven by 5 ms light pulses within 5 ms of
  onset") when the probability of a spike 0 to 5 ms after an isolated pulse exceeds that in the
  5 ms starting 50 ms before by a one-sided binomial test at p < 0.001 (standard) with at least
  10 pulses.
"""

from __future__ import annotations

import hashlib
import multiprocessing
import threading
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from dandi.dandiapi import DandiAPIClient
from scipy import signal, stats

DANDISET_ID = "000005"
DANDISET_VERSION = "0.220126.1853"

WHISK_HZ = 1_000
ANALYSIS_END_S = 5.0
# whisking (claims, Measures)
WHISK_BAND_HZ = (6.0, 60.0)
WHISK_ORDER = 4
WHISK_AMP_DEG = 2.5
NONWHISK_AMP_DEG = 1.25
NONWHISK_MIN_S = 0.100
LICK_GUARD_S = 0.100
TOUCH_GUARD_PRE_S = 0.010
TOUCH_GUARD_POST_S = 0.100
ONSET_RISE_DEG = 2.0
ONSET_NO_TOUCH_S = 0.250
PRE_ONSET_S = (-0.200, 0.0)
POST_ONSET_S = (0.100, 0.300)
PHASE_BINS = 12
R2_COUPLED = 0.25
FILTERS = ("filtfilt", "lfilter")       # readings O1 a and O1 b
# spikes (standard)
WC_PROMINENCE_MV = 20.0
WC_MIN_DVDT = 10.0                      # mV/ms
JX_HIGHPASS_HZ = 300.0
JX_THRESHOLD_SD = 6.0
REFRACTORY_S = 0.001
SILENT_THRESHOLD_MV = -42.0             # claims, Measures
# light (standard, see docstring)
TAG_WIN_S = 0.005                       # claims header: within 5 ms of onset
TAG_MIN_PULSES = 10
TAG_MAX_P = 0.001
FS_MAX_DURATION_MS = 0.27               # claims header, approximate reading of Supp. Fig. 6
FS_MAX_RATIO = 2.8
N_BOOT = 1000                           # claims: 1,000 bootstrap iterations
EVENT_PRE_S, EVENT_POST_S = 0.050, 0.150


def _str(x):
    v = x[()]
    if isinstance(v, bytes):
        return v.decode()
    if isinstance(v, np.ndarray):
        return [i.decode() if isinstance(i, bytes) else str(i) for i in v.ravel()]
    return v


def assets(version=DANDISET_VERSION):
    """Path, download URL and size of every asset of a version."""
    client = DandiAPIClient()
    ds = client.get_dandiset(DANDISET_ID, version)
    out = [{"path": a.path, "size": a.size, "url": a.get_content_url(follow_redirects=1, strip_query=True)}
           for a in ds.get_assets()]
    return sorted(out, key=lambda a: a["path"])


def versions_check():
    """The versions of the dandiset, and whether the draft holds the same asset paths and sizes as
    the pinned version."""
    client = DandiAPIClient()
    vs = [(v.identifier, str(v.modified)[:19]) for v in client.get_dandiset(DANDISET_ID).get_versions()]
    pinned = {(a.path, a.size) for a in client.get_dandiset(DANDISET_ID, DANDISET_VERSION).get_assets()}
    draft = {(a.path, a.size) for a in client.get_dandiset(DANDISET_ID, "draft").get_assets()}
    return {"versions": vs, "pinned_assets": len(pinned), "draft_assets": len(draft),
            "draft_same_paths_and_sizes": pinned == draft}


_session = threading.local()


def _open(url):
    f = h5py.File(remfile.File(url), "r")
    f.url = url
    return f


def read(f, name):
    """Read a whole dataset. The datasets of this dandiset are contiguous and uncompressed, so
    their bytes are fetched with one HTTP range request; other layouts are read through h5py."""
    d = f[name]
    off = d.id.get_offset()
    if off is None or d.chunks is not None or d.dtype.kind not in "biuf" or d.size == 0:
        return d[:]
    nbytes = d.size * d.dtype.itemsize
    if not hasattr(_session, "s"):
        _session.s = requests.Session()
    for attempt in range(5):
        try:
            r = _session.s.get(f.url, headers={"Range": f"bytes={off}-{off + nbytes - 1}"}, timeout=180)
            r.raise_for_status()
            if len(r.content) == nbytes:
                return np.frombuffer(r.content, dtype=d.dtype).reshape(d.shape)
        except requests.RequestException:
            if attempt == 4:
                raise
    raise IOError(f"incomplete read of {name}")


def _trials(f):
    t = f["intervals/trials"]
    df = pd.DataFrame({"start": t["start_time"][:], "stop": t["stop_time"][:]})
    for col in ["type", "response", "photo_stim_mode"]:
        df[col] = [v.decode() if isinstance(v, bytes) else str(v) for v in t[col][:]]
    for col in ["stim_present", "pole_in_time", "pole_out_time", "first_touch_time", "first_lick_time",
                "pole_position"]:
        df[col] = t[col][:]
    df["photo_stim_power"] = [float(v) if not isinstance(v, bytes) and v is not None else np.nan
                              for v in t["photo_stim_power"][:]]
    df.attrs["descriptions"] = {c: str(t[c].attrs.get("description", "")) for c in t if c not in ("id",) and "index" not in c}
    return df


def per_trial_index(t, trials):
    """Trial number of each timestamp (-1 when outside every trial)."""
    i = np.searchsorted(trials["start"].to_numpy(), t, side="right") - 1
    ok = (i >= 0) & (t < trials["stop"].to_numpy()[np.clip(i, 0, None)])
    return np.where(ok, i, -1)


# --------------------------------------------------------------------------- whisking

def _runs(mask):
    """Start and stop (exclusive) of each run of True."""
    d = np.diff(np.r_[0, mask.astype(np.int8), 0])
    return np.flatnonzero(d == 1), np.flatnonzero(d == -1)


def whisking_epochs(angle, tri, excl, filt="filtfilt"):
    """Amplitude, phase, whisking-epoch mask and nonwhisking-period mask, trial by trial.

    angle: whisker angle (deg) at 1 kHz; tri: trial of each sample; excl: True where licks or
    touches exclude a sample (see `exclusion_mask`); filt: 'filtfilt' (O1 a) or 'lfilter' (O1 b)."""
    b, a = signal.butter(WHISK_ORDER, np.array(WHISK_BAND_HZ) / (WHISK_HZ / 2), btype="band")
    n = len(angle)
    amp = np.full(n, np.nan, np.float32)
    phase = np.full(n, np.nan, np.float32)
    whisk = np.zeros(n, bool)
    for k in np.unique(tri[tri >= 0]):
        idx = np.flatnonzero(tri == k)
        x = angle[idx]
        good = np.isfinite(x)
        if good.sum() < 200:
            continue
        x = np.interp(np.arange(len(x)), np.flatnonzero(good), x[good])
        x = x - x.mean()
        y = signal.filtfilt(b, a, x) if filt == "filtfilt" else signal.lfilter(b, a, x)
        h = signal.hilbert(y)
        am, ph = np.abs(h), np.angle(h)
        am[~good] = np.nan
        amp[idx], phase[idx] = am, ph
        # cycles: from one wrap of the phase (+pi to -pi, most retracted) to the next
        wraps = np.flatnonzero(np.diff(ph) < -np.pi) + 1
        for c0, c1 in zip(wraps[:-1], wraps[1:]):
            seg = ph[c0:c1]
            z = int(np.argmin(np.abs(seg)))
            if np.isfinite(am[c0 + z]) and am[c0 + z] > WHISK_AMP_DEG:
                whisk[idx[c0:c1]] = True
    whisk &= ~excl
    quiet = (amp < NONWHISK_AMP_DEG) & ~excl & (tri >= 0)
    nonwhisk = np.zeros(n, bool)
    s0, s1 = _runs(quiet)
    # runs must also stay within one trial
    for a0, a1 in zip(s0, s1):
        tt = tri[a0:a1]
        brk = np.flatnonzero(np.diff(tt) != 0) + 1
        edges = np.r_[0, brk, a1 - a0]
        for e0, e1 in zip(edges[:-1], edges[1:]):
            if e1 - e0 >= int(NONWHISK_MIN_S * WHISK_HZ):
                nonwhisk[a0 + e0:a0 + e1] = True
    return amp, phase, whisk, nonwhisk


def exclusion_mask(n, whiskers, lick_idx):
    """True within 10 ms before to 100 ms after any touch of any tracked whisker (onset to offset
    included), and within 100 ms of any lick."""
    m = np.zeros(n, bool)
    pre, post = int(TOUCH_GUARD_PRE_S * WHISK_HZ), int(TOUCH_GUARD_POST_S * WHISK_HZ)
    for w in whiskers.values():
        on, off = w["touch_on"], w["touch_off"]
        for i in on:
            j = off[off >= i]
            end = j[0] if len(j) else i
            m[max(0, i - pre): min(n, end + post + 1)] = True
    g = int(LICK_GUARD_S * WHISK_HZ)
    for i in lick_idx:
        m[max(0, i - g): min(n, i + g + 1)] = True
    return m


def whisking_onsets(amp, nonwhisk, tri, touch_on_idx):
    """Whisking onsets: ends of nonwhisking periods where the mean amplitude 100 to 300 ms after
    exceeds the mean 0 to 200 ms before by at least 2 degrees, with no touch onset within 250 ms.
    Returns the sample index of each onset and, for each, the first touch onset after it (or -1),
    after which data are removed."""
    s0, s1 = _runs(nonwhisk)
    on_sorted = np.sort(touch_on_idx)
    out, cut = [], []
    a0, a1 = int(PRE_ONSET_S[0] * WHISK_HZ), int(POST_ONSET_S[1] * WHISK_HZ)
    for e in s1:
        if e + a1 >= len(amp) or e + a0 < 0 or tri[e + a1 - 1] != tri[e - 1] or tri[e + a0] != tri[e - 1]:
            continue
        nxt = on_sorted[np.searchsorted(on_sorted, e):]
        nt = nxt[0] if len(nxt) and tri[nxt[0]] == tri[e - 1] else -1
        if nt >= 0 and nt - e < int(ONSET_NO_TOUCH_S * WHISK_HZ):
            continue
        pre = np.nanmean(amp[e + a0:e])
        post_seg = amp[e + int(POST_ONSET_S[0] * WHISK_HZ):e + a1].astype(float)
        if nt >= 0:
            post_seg[max(0, nt - e - int(POST_ONSET_S[0] * WHISK_HZ)):] = np.nan
        if np.all(np.isnan(post_seg)):
            continue
        if np.nanmean(post_seg) - pre >= ONSET_RISE_DEG:
            out.append(e)
            cut.append(nt)
    return np.array(out, int), np.array(cut, int)


# --------------------------------------------------------------------------- spikes and waveforms

def detect_spikes_whole_cell(v, fs):
    """Indices of action potential peaks in a whole-cell trace (mV)."""
    dv = np.gradient(v) * fs / 1000.0
    peaks, _ = signal.find_peaks(v, prominence=WC_PROMINENCE_MV, distance=max(1, int(REFRACTORY_S * fs)))
    n1 = int(0.001 * fs)
    keep = [p for p in peaks if p >= n1 and dv[p - n1:p + 1].max() >= WC_MIN_DVDT]
    return np.array(keep, int)


def detect_spikes_juxta(v, fs):
    """Indices of spikes in a cell-attached trace, and the polarity used (+1 or -1)."""
    b, a = signal.butter(3, JX_HIGHPASS_HZ / (fs / 2), btype="high")
    hp = signal.filtfilt(b, a, v - np.median(v))
    hi, lo = np.percentile(hp, [99.99, 0.01])
    pol = 1 if abs(hi) >= abs(lo) else -1
    x = pol * hp
    sd = np.median(np.abs(x - np.median(x))) / 0.6745
    peaks, _ = signal.find_peaks(x, height=JX_THRESHOLD_SD * sd, distance=max(1, int(REFRACTORY_S * fs)))
    return peaks, pol, hp


def spike_fwhm_ms(wave, pre, fs):
    """Full width at half maximum (ms) of a mean spike whose peak is at sample `pre`."""
    w = np.asarray(wave, float) - np.mean(wave[: max(pre - int(0.0005 * fs), 1)])
    up = 10
    fine = np.interp(np.arange((len(w) - 1) * up + 1) / up, np.arange(len(w)), w)
    ipk = pre * up
    half = fine[ipk] / 2
    if half <= 0:
        return np.nan
    left, right = ipk, ipk
    while left > 0 and fine[left] > half:
        left -= 1
    while right < len(fine) - 1 and fine[right] > half:
        right += 1
    return (right - left) / up / fs * 1000.0


def ca_waveform(wave, pre, fs):
    """Supplementary Fig. 6 measures of a high-passed mean spike whose peak (made positive) is at
    `pre`, read from the figure's inset: the peak height and the depth of the trough that follows
    it (the minimum in the 1.5 ms after the peak), both from the baseline (mean 1.5 to 0.8 ms
    before the peak); ratio = peak / |trough|; duration = time from peak to trough (ms)."""
    w = np.asarray(wave, float)
    base = w[: max(pre - int(0.0008 * fs), 1)].mean()
    w = w - base
    seg = w[pre:pre + int(0.0015 * fs) + 1]
    k = int(np.argmin(seg))
    trough = seg[k]
    ratio = w[pre] / abs(trough) if trough < 0 else np.nan
    return float(k / fs * 1000.0), float(ratio)


def spike_thresholds(v, dv, peaks, fs, crit):
    """Vm at the first sample in the 3 ms before each peak where dVm/dt exceeds `crit`."""
    n3 = int(0.003 * fs)
    out = []
    for p in peaks:
        seg = dv[max(0, p - n3):p + 1]
        j = np.flatnonzero(seg > crit)
        out.append(v[max(0, p - n3) + j[0]] if len(j) else np.nan)
    return np.array(out, float)


def remove_spikes(v, peaks, fs):
    """Vm with each spike replaced by a straight line from 1 ms before to 4 ms after its peak."""
    v = v.copy()
    a, b = int(0.001 * fs), int(0.004 * fs)
    for p in peaks:
        i0, i1 = max(0, p - a), min(len(v) - 1, p + b)
        v[i0:i1 + 1] = np.linspace(v[i0], v[i1], i1 - i0 + 1)
    return v


# --------------------------------------------------------------------------- loading

def _whiskers(f):
    """Angle and touch series of every tracked whisker; the principal one is flagged."""
    out = {}
    for name in f["acquisition"]:
        g = f["acquisition"][name]
        if "whisker_angle" not in g:
            continue
        out[name] = {"principal": name.lower().startswith("principal"), "name": name.split("_")[-1].upper(),
                     "t": read(f, f"acquisition/{name}/whisker_angle/timestamps"),
                     "angle": read(f, f"acquisition/{name}/whisker_angle/data").astype(float),
                     "touch_on": np.flatnonzero(read(f, f"acquisition/{name}/touch_onset/data")),
                     "touch_off": np.flatnonzero(read(f, f"acquisition/{name}/touch_offset/data"))}
    return out


def _iti(on, off, tri):
    """Intertouch interval (s): from the offset of the previous touch to this onset; infinite for
    the first touch of a trial."""
    j = np.searchsorted(off, on) - 1
    prev = np.where(j >= 0, off[np.clip(j, 0, None)], -1)
    same = (prev >= 0) & (tri[np.clip(prev, 0, None)] == tri[on])
    return np.where(same, (on - prev) / WHISK_HZ, np.inf)


def with_whisker(beh, name):
    """A copy of `beh` whose touches are those of another tracked whisker (same clock)."""
    w = beh["whisker_touches"][name]
    b = dict(beh)
    b["touch_on"], b["touch_off"] = w["on"], w["off"]
    b["touch_iti"] = _iti(w["on"], w["off"], beh["trial"])
    return b


def _licks(f):
    d = read(f, "acquisition/lick_trace/lick_trace/data").astype(np.int8)
    t = read(f, "acquisition/lick_trace/lick_trace/timestamps")
    return t[np.flatnonzero(np.diff(np.r_[0, d]) == 1)]


def _behaviour(f, trials):
    """The principal whisker reduced to its epochs under both filters, touches and licks."""
    whiskers = _whiskers(f)
    licks = _licks(f)
    pname = next((k for k, w in whiskers.items() if w["principal"]), None)
    out = {"licks": licks, "whisker_names": [w["name"] for w in whiskers.values()], "principal": pname,
           "touch_counts": {w["name"]: len(w["touch_on"]) for w in whiskers.values()}}
    if pname is None:
        return out
    w = whiskers[pname]
    t = w["t"]
    tri = per_trial_index(t, trials)
    li = np.searchsorted(t, licks)
    li = li[(li < len(t))]
    excl = exclusion_mask(len(t), whiskers, li)
    # touches of all tracked whiskers (any) by trial, for the touch counts of behavior-touches
    out["any_touch_on_t"] = np.sort(np.concatenate([ww["t"][ww["touch_on"]] for ww in whiskers.values()]))
    on, off = w["touch_on"], w["touch_off"]
    iti = _iti(on, off, tri)
    out["whisker_touches"] = {ww["name"]: {"on": ww["touch_on"], "off": ww["touch_off"], "n_samples": len(ww["t"]),
                                           "same_clock": len(ww["t"]) == len(t) and bool(np.allclose(ww["t"], t))}
                              for ww in whiskers.values()}
    out.update(t=t, trial=tri.astype(np.int32), touch_on=on, touch_off=off, touch_iti=iti,
               angle_range=(float(np.nanmin(w["angle"])), float(np.nanmax(w["angle"]))),
               angle_nan=float(np.isnan(w["angle"]).mean()), dt_median=float(np.median(np.diff(t))),
               excl=excl)
    for filt in FILTERS:
        amp, phase, whisk, nonwhisk = whisking_epochs(w["angle"], tri, excl, filt)
        ons, cut = whisking_onsets(amp, nonwhisk, tri, on)
        out[filt] = {"amp": amp.astype(np.float16), "phase": phase.astype(np.float16), "whisk": whisk,
                     "nonwhisk": nonwhisk, "onsets": ons, "onset_cut": cut}
    return out


def _light(f):
    """Per photostimulation series, the light-on intervals (s), and the site's labelled region
    and wavelength."""
    out = {}
    info = {}
    g = f.get("general/optogenetics")
    if g is not None:
        for name in g:
            s = g[name]
            loc = _str(s["location"]) if "location" in s else ""
            info[name.replace("site_ ", "photostimulation_site_ ")] = {
                "region": loc.split(";")[0].replace("brain_region:", "").strip(),
                "lambda_nm": float(s["excitation_lambda"][()])}
    pres = f["stimulus/presentation"]
    for name in pres:
        if not name.startswith("photostimulation"):
            continue
        d = read(f, f"stimulus/presentation/{name}/data")
        on = np.flatnonzero(d > 0)
        rec = {"region": info.get(name, {}).get("region", ""), "lambda_nm": info.get(name, {}).get("lambda_nm", np.nan),
               "power_max": float(d[on].max()) if len(on) else 0.0, "pulses": np.zeros((0, 2)),
               "conversion": float(pres[name]["data"].attrs.get("conversion", np.nan))}
        if len(on):
            ts = read(f, f"stimulus/presentation/{name}/timestamps")
            brk = np.flatnonzero(np.diff(on) > 1)
            starts, stops = np.r_[on[0], on[brk + 1]], np.r_[on[brk], on[-1]]
            dt = np.median(np.diff(ts[:1000]))
            rec["pulses"] = np.c_[ts[starts], ts[stops] + dt]
            rec["pulse_power"] = np.array([d[a:b + 1].max() for a, b in zip(starts, stops)], np.float32)
        out[name] = rec
    return out


def light_windows(light, site, trials):
    """Per lit trial of a site: the span (s after the trial start) from its first to last light
    sample, and the number of pulses."""
    pulses = light.get(site, {}).get("pulses", np.zeros((0, 2)))
    if len(pulses) == 0:
        return pd.DataFrame(columns=["trial", "rel_start", "rel_stop", "n_pulses"])
    k = per_trial_index(pulses[:, 0], trials)
    rows = []
    for t in np.unique(k[k >= 0]):
        p = pulses[k == t]
        s0 = trials["start"].iloc[t]
        rows.append({"trial": int(t), "rel_start": p[:, 0].min() - s0, "rel_stop": p[:, 1].max() - s0,
                     "n_pulses": len(p)})
    return pd.DataFrame(rows)


def lit_trials(light, trials):
    """Boolean per trial: any light at any site."""
    lit = np.zeros(len(trials), bool)
    for site in light:
        w = light_windows(light, site, trials)
        lit[w["trial"].to_numpy(int)] = True
    return lit


def isolated_pulses(light, site, max_dur=0.0075, gap=0.1):
    """Onsets of single short light pulses at a site: no other pulse within `gap` s."""
    pulses = light.get(site, {}).get("pulses", np.zeros((0, 2)))
    if len(pulses) == 0:
        return np.zeros(0)
    on, dur = pulses[:, 0], pulses[:, 1] - pulses[:, 0]
    prev, nxt = np.r_[np.inf, np.diff(on)], np.r_[np.diff(on), np.inf]
    return on[(dur < max_dur) & (prev > gap) & (nxt > gap)]


def _event_average(v, vt, tri, fs, events, pre=EVENT_PRE_S, post=EVENT_POST_S):
    """Mean of the trace around each event (full rate), events whose window stays in one trial."""
    a, b = int(pre * fs), int(post * fs)
    idx = np.searchsorted(vt, events)
    segs = [v[i - a:i + b] for i in idx if i - a >= 0 and i + b < len(v) and tri[i - a] == tri[i + b] >= 0]
    if not segs:
        return None, 0
    return np.mean(segs, axis=0).astype(np.float32), len(segs)


def load_icephys(asset):
    """One L4 cell, reduced to what the analysis needs."""
    f = _open(asset["url"])
    trials = _trials(f)
    vd = f["acquisition/CurrentClampSeries/data"]
    v = read(f, "acquisition/CurrentClampSeries/data").astype(float)   # stored values (mV)
    vt = read(f, "acquisition/CurrentClampSeries/timestamps")
    fs = float(round(1.0 / np.median(np.diff(vt[:10000]))))
    tri = per_trial_index(vt, trials)
    rel = vt - trials["start"].to_numpy()[np.clip(tri, 0, None)]
    sd = _str(f["session_description"])
    rec = {"path": asset["path"], "kind": "L4", "subject": _str(f["general/subject/subject_id"]),
           "genotype": _str(f["general/subject/genotype"]), "session_description": sd,
           "label_mode": "whole-cell" if "whole-cell" in sd.split(";")[-1] else "juxtacellular",
           "vm_conversion": float(vd.attrs["conversion"]), "vm_unit": vd.attrs["unit"], "trials": trials,
           "light": _light(f), "vm_hz": fs, "n_vm": len(v),
           "vm_hash": hashlib.sha1(v.astype(np.float32).tobytes()).hexdigest()[:12],
           "vm_outside_trials": int((tri < 0).sum())}
    k0 = np.r_[0, np.flatnonzero(np.diff(tri) != 0) + 1]
    rec["vm_block_first_rel"] = float(np.abs(rel[k0][tri[k0] >= 0]).max())
    rec["vm_trial_s"] = float(np.median(np.bincount(tri[tri >= 0])) / fs)
    rec["vm_median"] = float(np.median(v))
    # injected current: stored values and their conversion
    if "CurrentClampStimulus" in f["stimulus/presentation"]:
        cd = f["stimulus/presentation/CurrentClampStimulus/data"]
        c = read(f, "stimulus/presentation/CurrentClampStimulus/data").astype(float)
        rec["current_conversion"] = float(cd.attrs["conversion"])
        rec["current_unit"] = cd.attrs["unit"]
        test = (rel >= 5.0) & (tri >= 0)
        rec["current_end_of_trial_median"] = float(np.median(c[test])) if test.any() else np.nan
        rec["current_trial_min"] = float(np.percentile(c[tri >= 0], 0.5))
        rec["current_trial_median"] = float(np.median(c[(tri >= 0) & (rel < 5.0)]))
    # mode from the trace: whole-cell when the median trace is below -20 mV
    trial_med = np.array([np.median(v[tri == k]) if np.any(tri == k) else np.nan for k in range(len(trials))])
    rec["trial_vm_median"] = trial_med.astype(np.float32)
    mode = "whole-cell" if rec["vm_median"] < -20 else "cell-attached"
    rec["mode"] = mode
    b, a = signal.butter(2, [1 / (fs / 2), 100 / (fs / 2)], "band")
    los = []
    for k in range(0, len(trials), max(1, len(trials) // 10)):
        x = v[(tri == k) & (rel < ANALYSIS_END_S)]
        if len(x) > fs:
            los.append(np.std(signal.filtfilt(b, a, x)))
    rec["lowfreq_sd_mv"] = float(np.median(los)) if los else np.nan
    keep = (tri >= 0) & (rel < ANALYSIS_END_S)
    spikes, thr_a, thr_b, waves, ca_waves, pols = [], [], [], [], [], []
    vclean = v.copy()
    pre, post = int(0.0015 * fs), int(0.003 * fs)
    for kk in np.unique(tri[keep]):
        idx = np.flatnonzero((tri == kk) & keep)
        x = v[idx]
        if mode == "whole-cell":
            p = detect_spikes_whole_cell(x, fs)
            dv = np.gradient(x) * fs / 1000.0
            thr_a.append(spike_thresholds(x, dv, p, fs, dv.mean() + 3 * dv.std()))
            thr_b.append(spike_thresholds(x, dv, p, fs, 3 * dv.std()))
            vclean[idx] = remove_spikes(x, p, fs)
            waves += [x[q - pre:q + post] for q in p if q >= pre and q < len(x) - post]
        else:
            p, pol, hp = detect_spikes_juxta(x, fs)
            pols.append((pol, len(p)))
            ca_waves.append((hp, p, pol))
        spikes.append(vt[idx[p]])
    rec["spikes"] = np.concatenate(spikes) if spikes else np.zeros(0)
    if mode == "whole-cell":
        rec["spike_thr"] = {"a": np.concatenate(thr_a) if thr_a else np.zeros(0),
                            "b": np.concatenate(thr_b) if thr_b else np.zeros(0)}
        rec["fwhm_ms"] = spike_fwhm_ms(np.mean(waves, axis=0), pre, fs) if len(waves) >= 5 else np.nan
        rec["ca_duration_ms"], rec["ca_ratio"] = np.nan, np.nan
    else:
        cnt = {}
        for pol, n in pols:
            cnt[pol] = cnt.get(pol, 0) + n
        polarity = max(cnt, key=cnt.get) if cnt else 1
        allw = []
        for hp, p, pol in ca_waves:
            if pol == polarity:
                allw += [pol * hp[q - pre:q + post] for q in p if q >= pre and q < len(hp) - post]
        rec["fwhm_ms"] = np.nan
        if len(allw) >= 5:
            rec["ca_duration_ms"], rec["ca_ratio"] = ca_waveform(np.mean(allw, axis=0), pre, fs)
        else:
            rec["ca_duration_ms"], rec["ca_ratio"] = np.nan, np.nan
        rec["polarity"] = polarity
    beh = _behaviour(f, trials)
    rec["beh"] = beh
    lit = lit_trials(rec["light"], trials)
    if mode == "whole-cell" and beh["principal"] is not None:
        # spike-removed Vm averaged into the 1 ms bins of the whisker clock
        t = beh["t"]
        j = np.searchsorted(t, vt, side="right") - 1
        ok = (j >= 0) & (np.abs(vt - t[np.clip(j, 0, None)]) < 1.0 / WHISK_HZ) & (tri >= 0)
        s = np.bincount(j[ok], weights=vclean[ok], minlength=len(t))
        n = np.bincount(j[ok], minlength=len(t))
        rec["vm1k"] = np.where(n > 0, s / np.maximum(n, 1), np.nan).astype(np.float32)
        # full-rate averages around principal-whisker touches (trials without light, ITI >= 25 ms)
        on_t = t[beh["touch_on"]]
        ttri = beh["trial"][beh["touch_on"]]
        good = (beh["touch_iti"] >= 0.025) & (ttri >= 0)
        good &= ~lit[np.clip(ttri, 0, None)]
        rec["touch_avg"], rec["touch_avg_n"] = _event_average(vclean, vt, tri, fs, on_t[good])
        # around light: the first light sample of each lit trial, and isolated 5 ms pulses
        rec["light_avg"] = {}
        for site, L in rec["light"].items():
            w = light_windows(rec["light"], site, trials)
            if len(w) == 0:
                continue
            first = trials["start"].to_numpy()[w.trial.to_numpy(int)] + w.rel_start.to_numpy()
            iso = isolated_pulses(rec["light"], site)
            rec["light_avg"][site] = {"first": _event_average(vclean, vt, tri, fs, first),
                                      "isolated": _event_average(vclean, vt, tri, fs, iso)}
    rec["general_fields"] = sorted(f["general"].keys())
    rec["subject_fields"] = sorted(f["general/subject"].keys())
    texts = [_str(f[k]) for k in ("session_description",) if k in f]

    def collect(name, obj):
        if isinstance(obj, h5py.Dataset) and obj.dtype.kind in "OSU":
            texts.append(_str(obj))
        texts.extend(str(x.decode() if isinstance(x, bytes) else x) for x in obj.attrs.values()
                     if isinstance(x, (str, bytes)))
    f["general"].visititems(collect)
    rec["metadata_text"] = " ".join(" ".join(t) if isinstance(t, list) else str(t) for t in texts)
    g = f["general/intracellular_ephys"]
    rec["ic_location"] = next((_str(g[k]["location"]) for k in g if "location" in g[k]), "")
    return rec


def load_vpm(asset):
    """One VPM session: every sorted unit, reduced to spike times."""
    f = _open(asset["url"])
    trials = _trials(f)
    u = f["units"]
    st = read(f, "units/spike_times")
    idx = u["spike_times_index"][:]
    starts = np.r_[0, idx[:-1]]
    units = [{"unit": i, "desc": _str(u["cell_desc"])[i], "spikes": st[a:b]} for i, (a, b) in enumerate(zip(starts, idx))]
    texts = [_str(f["session_description"])]
    rec = {"path": asset["path"], "kind": "VPM", "subject": _str(f["general/subject/subject_id"]),
           "genotype": _str(f["general/subject/genotype"]), "trials": trials, "units": units,
           "unit_sampling_rate": [float(x) for x in u["sampling_rate"][:]],
           "location": [f["general/extracellular_ephys"][k].attrs.get("location", "")
                        for k in f["general/extracellular_ephys"] if k != "electrodes"],
           "session_description": texts[0], "has_light": any(k.startswith("photostimulation") for k in f["stimulus/presentation"]),
           "beh": _behaviour(f, trials)}
    return rec


def load_one(a):
    return load_vpm(a) if "ecephys" in a["path"] else load_icephys(a)


def load_all(workers=8):
    """Load every file in parallel processes."""
    al = assets()
    with ProcessPoolExecutor(workers, mp_context=multiprocessing.get_context("fork")) as ex:
        return list(ex.map(load_one, al))


# --------------------------------------------------------------------------- measures

def spikes_to_samples(spikes, t):
    """Index of the whisker sample at or before each spike (whisker clock is 1 kHz)."""
    i = np.searchsorted(t, spikes, side="right") - 1
    ok = (i >= 0) & (np.abs(t[np.clip(i, 0, None)] - spikes) < 1.5 / WHISK_HZ)
    return i[ok]


def counts_1k(spikes, beh):
    """Spike count in each 1 ms whisker sample."""
    return np.bincount(spikes_to_samples(spikes, beh["t"]), minlength=len(beh["t"]))


def touches(beh, trial_mask=None, min_iti=0.025, rel_window=None, trials=None):
    """Sample indices of principal-whisker touch onsets with intertouch interval >= min_iti,
    in the trials of `trial_mask`, and (optionally) inside per-trial windows (s after start)."""
    on = beh["touch_on"]
    tri = beh["trial"][on]
    ok = (beh["touch_iti"] >= min_iti) & (tri >= 0)
    if trial_mask is not None:
        ok &= np.asarray(trial_mask)[np.clip(tri, 0, None)]
    if rel_window is not None:
        rel = beh["t"][on] - trials["start"].to_numpy()[np.clip(tri, 0, None)]
        lo = np.array([w[0] for w in rel_window])[np.clip(tri, 0, None)]
        hi = np.array([w[1] for w in rel_window])[np.clip(tri, 0, None)]
        ok &= (rel >= lo) & (rel < hi)
    return on[ok]


def _window_counts(count, tri, on, a_ms, b_ms):
    """Spikes in [on + a, on + b) ms for each onset; NaN where the window leaves the trial."""
    cs = np.r_[0, np.cumsum(count)]
    n = len(count)
    lo, hi = on + a_ms, on + b_ms
    ok = (lo >= 0) & (hi <= n)
    out = np.full(len(on), np.nan)
    i = np.flatnonzero(ok)
    same = (tri[lo[i]] == tri[on[i]]) & (tri[hi[i] - 1] == tri[on[i]])
    i = i[same]
    out[i] = cs[hi[i]] - cs[lo[i]]
    return out


SPT_DEFS = {"cortex5": ((0, 50), (-25, 0), 2.0), "cortex8": ((4, 20), (-16, 0), 1.0),
            "vpm": ((0, 25), (-25, 0), 1.0)}


def spikes_per_touch(count, tri, on, definition, rng=None):
    """Spikes per touch by one of the paper's definitions, and a 95% bootstrap interval over
    touches (N_BOOT draws) when `rng` is given."""
    (a0, a1), (b0, b1), k = SPT_DEFS[definition]
    post = _window_counts(count, tri, on, a0, a1)
    pre = _window_counts(count, tri, on, b0, b1)
    ok = np.isfinite(post) & np.isfinite(pre)
    d = post[ok] - k * pre[ok]
    out = {"n_touches": int(ok.sum()), "spt": float(d.mean()) if len(d) else np.nan,
           "post": post[ok], "pre": pre[ok]}
    if rng is not None and len(d) >= 2:
        bs = d[rng.integers(0, len(d), (N_BOOT, len(d)))].mean(axis=1)
        out["ci"] = (float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5)))
    else:
        out["ci"] = (np.nan, np.nan)
    return out


def psth_latency(count, tri, on):
    """Touch PSTH (1 ms bins, -25 to 100 ms) and the dPSTH/dt latency (ms) with the paper's
    exclusion; returns (latency left edge, latency bin centre, reason when excluded)."""
    lags = np.arange(-25, 100)
    m = np.array([np.nanmean(_window_counts(count, tri, on, l, l + 1)) for l in lags]) * WHISK_HZ
    post = m[lags >= 0]
    if not np.isfinite(post).any() or np.nanmax(post) < 10:
        return np.nan, np.nan, "max rate below 10 spikes/s", m
    d = np.diff(m)                                  # d[i] = m[i+1] - m[i], the change into bin lags[i+1]
    lag_d = lags[1:]
    base = d[(lag_d >= -25) & (lag_d < 0)]
    thr = 3 * np.nanstd(base)
    after = np.flatnonzero((lag_d >= 0) & (d > thr))
    if len(after) == 0 or thr == 0 and not np.any(d[lag_d >= 0] > 0):
        return np.nan, np.nan, "no crossing", m
    k = lag_d[after[0]]
    return float(k), float(k + 0.5), "", m


def epoch_rates(count, beh, filt, use=None):
    """Rates (spikes/s) in whisking epochs and nonwhisking periods, with per-epoch and per-trial
    samples for the rank-sum test (readings O2 a and b). `use`: boolean per sample."""
    e = beh[filt]
    tri = beh["trial"]
    out = {}
    for name, m in (("whisk", e["whisk"]), ("nonwhisk", e["nonwhisk"])):
        mm = m & (tri >= 0) if use is None else m & use & (tri >= 0)
        T = mm.sum() / WHISK_HZ
        out[f"rate_{name}"] = count[mm].sum() / T if T > 0 else np.nan
        out[f"time_{name}"] = T
        s0, s1 = _runs(mm)
        out[f"epochs_{name}"] = np.array([count[a:b].sum() / ((b - a) / WHISK_HZ) for a, b in zip(s0, s1)])
        ks = tri[mm]
        c = np.bincount(ks, weights=count[mm], minlength=tri.max() + 1)
        n = np.bincount(ks, minlength=tri.max() + 1)
        out[f"trials_{name}"] = c[n > 0] / (n[n > 0] / WHISK_HZ)
    return out


def ranksum_change(r):
    """Per-cell Wilcoxon rank-sum of whisking against nonwhisking samples, readings O2 a and b:
    +1 significant increase, -1 decrease, 0 neither (p < 0.05)."""
    out = {}
    for key, tag in (("epochs", "a"), ("trials", "b")):
        x, y = r[f"{key}_whisk"], r[f"{key}_nonwhisk"]
        if len(x) < 2 or len(y) < 2:
            out[tag] = (np.nan, 0)
            continue
        p = stats.ranksums(x, y).pvalue
        out[tag] = (float(p), int(np.sign(np.mean(x) - np.mean(y))) if p < 0.05 else 0)
    return out


def phase_fit(values, occupancy=None, double=False):
    """Least-squares fit of a + b cos(phi) + c sin(phi) (+ second harmonic when `double`) to 12
    phase-binned values; returns r2, coupling strength (half the peak-to-trough of the fit) and
    preferred phase."""
    centers = np.linspace(-np.pi, np.pi, PHASE_BINS + 1)[:-1] + np.pi / PHASE_BINS
    y = np.asarray(values, float)
    ok = np.isfinite(y)
    if ok.sum() < 5 or np.nanstd(y) == 0:
        return {"r2": np.nan, "strength": np.nan, "pref": np.nan}
    cols = [np.ones_like(centers), np.cos(centers), np.sin(centers)]
    if double:
        cols += [np.cos(2 * centers), np.sin(2 * centers)]
    X = np.array(cols).T
    beta, *_ = np.linalg.lstsq(X[ok], y[ok], rcond=None)
    fit = X @ beta
    ss = np.sum((y[ok] - y[ok].mean()) ** 2)
    r2 = 1 - np.sum((y[ok] - fit[ok]) ** 2) / ss
    fine = np.linspace(-np.pi, np.pi, 721)
    Xf = np.array([np.ones_like(fine), np.cos(fine), np.sin(fine)] +
                  ([np.cos(2 * fine), np.sin(2 * fine)] if double else [])).T
    yf = Xf @ beta
    return {"r2": float(r2), "strength": float((yf.max() - yf.min()) / 2), "pref": float(fine[np.argmax(yf)])}


def phase_binned(beh, filt, count=None, vm=None, use=None):
    """Rate (spikes/s) or mean Vm in 12 phase bins during whisking epochs."""
    e = beh[filt]
    m = e["whisk"] & (beh["trial"] >= 0)
    if use is not None:
        m &= use
    ph = e["phase"].astype(float)
    m &= np.isfinite(ph)
    b = np.clip(((ph[m] + np.pi) / (2 * np.pi) * PHASE_BINS).astype(int), 0, PHASE_BINS - 1)
    occ = np.bincount(b, minlength=PHASE_BINS)
    if count is not None:
        c = np.bincount(b, weights=count[m], minlength=PHASE_BINS)
        return np.where(occ > 0, c / np.maximum(occ, 1) * WHISK_HZ, np.nan), occ
    x = vm[m]
    g = np.isfinite(x)
    s = np.bincount(b[g], weights=x[g], minlength=PHASE_BINS)
    n = np.bincount(b[g], minlength=PHASE_BINS)
    return np.where(n > 0, s / np.maximum(n, 1), np.nan), occ


def fs_phase_fit(values):
    """Supplementary Fig. 7g: the double fit when its r2 is at least 1.5 times the single fit's."""
    s = phase_fit(values)
    d = phase_fit(values, double=True)
    if np.isfinite(s["r2"]) and np.isfinite(d["r2"]) and d["r2"] >= 1.5 * s["r2"]:
        return {**d, "kind": "double"}
    return {**s, "kind": "single"}


def light_pulse_response(light, spikes, site):
    """Spike probability 0 to 5 ms after each isolated pulse at a site against the same 5 ms
    starting 50 ms before, one-sided binomial (McNemar-type) test, median first-spike latency."""
    on = isolated_pulses(light, site)
    if len(on) == 0:
        return {"n_pulses": 0}
    sp = np.sort(spikes)

    def any_spike(t0, t1):
        return (np.searchsorted(sp, t1) - np.searchsorted(sp, t0)) > 0

    ev = np.array([any_spike(p, p + TAG_WIN_S) for p in on])
    base = np.array([any_spike(p - 0.05, p - 0.05 + TAG_WIN_S) for p in on])
    n10, n01 = int((ev & ~base).sum()), int((~ev & base).sum())
    p = stats.binomtest(n10, n10 + n01, 0.5, alternative="greater").pvalue if n10 + n01 > 0 else 1.0
    lat = []
    for t in on:
        j = np.searchsorted(sp, t)
        if j < len(sp) and sp[j] - t < 0.02:
            lat.append(sp[j] - t)
    return {"n_pulses": int(len(on)), "p_evoked": float(ev.mean()), "p_base": float(base.mean()), "p_value": float(p),
            "median_latency_ms": float(np.median(lat) * 1000) if lat else np.nan}


def trial_thresholds(rec, reading):
    """Spike threshold per trial (mV) from a linear fit of each spike's threshold against its
    trial number; -42 mV for cells without spikes."""
    n = len(rec["trials"])
    thr = rec["spike_thr"][reading]
    if len(thr) < 2 or np.isfinite(thr).sum() < 2:
        return np.full(n, SILENT_THRESHOLD_MV)
    k = per_trial_index(rec["spikes"], rec["trials"])
    ok = np.isfinite(thr) & (k >= 0)
    if len(np.unique(k[ok])) < 2:
        return np.full(n, float(np.nanmean(thr[ok])))
    b, a = np.polyfit(k[ok], thr[ok], 1)
    return a + b * np.arange(n)


def psp_measures(avg, n, fs):
    """Touch-aligned average Vm (full rate, starting EVENT_PRE_S before onset): amplitude (peak 0 to
    50 ms after minus the mean 0 to 5 ms before), the peak time, and the latency by the dVm/dt rule:
    the first point after onset where the unsmoothed first difference (reading O8) exceeds 3 s.d. of
    its values 0 to 25 ms before onset. The claims file does not fix the resolution of the
    derivative, so it is taken at the full sampling rate (`latency_ms`) and on the average in 1 ms
    bins (`latency_1ms_edge`, `latency_1ms_centre`, the bin's left edge or centre)."""
    nan = {"latency_ms": np.nan, "latency_1ms_edge": np.nan, "latency_1ms_centre": np.nan, "amp_mv": np.nan, "peak_ms": np.nan}
    if avg is None or n < 5:
        return nan
    i0 = int(EVENT_PRE_S * fs)
    a = avg.astype(float)
    d = np.diff(a) * fs / 1000.0
    base = d[i0 - int(0.025 * fs):i0]
    post = np.flatnonzero(d[i0:] > 3 * base.std())
    lat = post[0] / fs * 1000 if len(post) else np.nan
    k1 = int(fs / 1000)
    b = a[: len(a) // k1 * k1].reshape(-1, k1).mean(axis=1)       # 1 ms bins, bin j starts j - 50 ms
    db = np.diff(b)                                                # db[j] is the change into bin j + 1
    lags = np.arange(len(b))[1:] - int(EVENT_PRE_S * 1000)
    thr = 3 * db[(lags >= -25) & (lags < 0)].std()
    hit = np.flatnonzero((lags >= 0) & (db > thr))
    pre = a[i0 - int(0.005 * fs):i0].mean()
    seg = a[i0:i0 + int(0.050 * fs)]
    k = int(np.argmax(seg))
    return {"latency_ms": float(lat), "latency_1ms_edge": float(lags[hit[0]]) if len(hit) else np.nan,
            "latency_1ms_centre": float(lags[hit[0]] + 0.5) if len(hit) else np.nan,
            "amp_mv": float(seg[k] - pre), "peak_ms": float(k / fs * 1000)}


def neg_onset_latency(avg, n, fs, binned=False):
    """Onset latency (ms) of a hyperpolarization in an event-aligned average (starting EVENT_PRE_S
    before the event): the touch-latency rule turned downward, the first point after the event
    where the first difference falls below -3 s.d. of its values 0 to 25 ms before. With
    `binned`, on the average in 1 ms bins (latency = the bin's left edge)."""
    if avg is None or n < 3:
        return np.nan
    a = avg.astype(float)
    if binned:
        k1 = int(fs / 1000)
        a = a[: len(a) // k1 * k1].reshape(-1, k1).mean(axis=1)
        fs = 1000.0
    i0 = int(EVENT_PRE_S * fs)
    d = np.diff(a)                      # d[i] is the change into sample i + 1
    thr = 3 * d[i0 - int(0.025 * fs) - 1:i0 - 1].std()
    post = np.flatnonzero(d[i0 - 1:] < -thr)
    return float(post[0] / fs * 1000) if len(post) else np.nan


def roc_auc(before, after, rng, n_resample=5000):
    """AUC of touch detection: touch trials give (after - before) counts in 250 ms windows around
    the first touch, no-touch trials the same difference in the sample epoch; both resampled
    `n_resample` times, and the ROC built by sweeping the threshold on the difference."""
    t, nt = np.asarray(after[0]) - np.asarray(before[0]), np.asarray(after[1]) - np.asarray(before[1])
    if len(t) < 2 or len(nt) < 2:
        return np.nan
    ts = t[rng.integers(0, len(t), n_resample)]
    ns = nt[rng.integers(0, len(nt), n_resample)]
    thr = np.unique(np.r_[ts, ns, ts.max() + 1, ns.min() - 1])
    hit = np.array([(ts >= c).mean() for c in thr])
    fa = np.array([(ns >= c).mean() for c in thr])
    o = np.argsort(fa)
    return float(np.trapezoid(hit[o], fa[o]))


def shift_spikes(spikes, trials, by=1):
    """Each spike moved to the trial `by` places later, at the same time after the trial start."""
    starts = trials["start"].to_numpy()
    k = per_trial_index(spikes, trials)
    ok = (k >= 0) & (k + by < len(starts))
    return spikes[ok] - starts[k[ok]] + starts[k[ok] + by]


# --------------------------------------------------------------------------- the paper's supplement

SUPPLEMENT_URL = ("https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fnn.4412/"
                  "MediaObjects/41593_2016_BFnn4412_MOESM61_ESM.pdf")
# Mouse line IDs of the paper's Supplementary Table 2, named from the JAX stock numbers given there:
# 014548 VGAT-ChR2-EYFP, 017320 PV-IRES-Cre, 012569 Ai32, 012355 PV-ChR2, 013044 SOM-IRES-Cre.
LINES = {1: "VGAT-ChR2-EYFP", 2: "PV-IRES-Cre", 3: "PV-IRES-Cre x Ai32", 4: "C57BL/6", 5: "PV-ChR2",
         6: "SOM-IRES-Cre x Ai32"}


def supplement_mouse_lines():
    """The mouse line of each mouse, read from Supplementary Table 1 of the paper (the PDF
    supplement on the publisher's site, part of doi:10.1038/nn.4412)."""
    import io
    import re
    import pypdf
    r = requests.get(SUPPLEMENT_URL, timeout=120)
    r.raise_for_status()
    text = "\n".join(p.extract_text() or "" for p in pypdf.PdfReader(io.BytesIO(r.content)).pages)
    rows = re.findall(r"^(\d{6}) (\d) ", text, re.M)
    if len(rows) == 0:
        raise ValueError("Supplementary Table 1 not found in the supplement")
    return pd.DataFrame({"subject": ["anm" + a for a, _ in rows], "line": [LINES[int(b)] for _, b in rows]})


# --------------------------------------------------------------------------- per-cell summaries

def spike_measures(spikes, beh, trial_mask, definition, rng, fs_fit=False, filters=FILTERS):
    """Every spike measure of one unit or cell over the trials of `trial_mask` (claims, Measures):
    spikes per touch with its bootstrap interval, the PSTH latency, nonwhisking and whisking rates
    with the per-cell rank-sum tests (O2 a, b) and the phase fit, under each filter (O1)."""
    count = counts_1k(spikes, beh)
    tri = beh["trial"]
    use = (tri >= 0) & np.asarray(trial_mask)[np.clip(tri, 0, None)]
    count = np.where(use, count, 0)
    on = touches(beh, trial_mask, 0.025)
    s = spikes_per_touch(count, tri, on, definition, rng)
    lat_edge, lat_centre, why, _ = psth_latency(count, tri, on)
    out = {"n_spikes": int(count.sum()), "n_touches": s["n_touches"], "spt": s["spt"], "spt_lo": s["ci"][0],
           "spt_hi": s["ci"][1], "lat_edge": lat_edge, "lat_centre": lat_centre, "lat_excluded": why}
    for filt in filters:
        r = epoch_rates(count, beh, filt, use)
        rs = ranksum_change(r)
        vals, occ = phase_binned(beh, filt, count=count, use=use)
        fit = fs_phase_fit(vals) if fs_fit else phase_fit(vals)
        single = phase_fit(vals)
        out.update({f"{filt}:rate_nonwhisk": r["rate_nonwhisk"], f"{filt}:rate_whisk": r["rate_whisk"],
                    f"{filt}:time_nonwhisk": r["time_nonwhisk"], f"{filt}:time_whisk": r["time_whisk"],
                    f"{filt}:O2a_p": rs["a"][0], f"{filt}:O2a": rs["a"][1], f"{filt}:O2b_p": rs["b"][0],
                    f"{filt}:O2b": rs["b"][1], f"{filt}:r2": fit["r2"], f"{filt}:fit": fit.get("kind", "single"),
                    f"{filt}:r2_single": single["r2"], f"{filt}:strength": fit["strength"],
                    f"{filt}:whisk_spikes": int(count[beh[filt]["whisk"] & use].sum())})
    return out


def vm_measures(rec, trial_mask, filt, reading):
    """Membrane-potential measures of one whole-cell cell (claims, Measures; spikes removed):
    resting Vm (mean and median in nonwhisking periods, O4), the whisking change (a: 100 to 300 ms
    after whisking onsets minus 0 to 200 ms before; b: whisking-epoch minus nonwhisking mean), the
    10th percentile of distance to threshold in nonwhisking, whisking and touch (4 to 50 ms) epochs
    with threshold reading O3 `reading`, Vm phase coupling, and the per-event values of the
    effective reversal (Supplementary Fig. 4)."""
    beh = rec["beh"]
    vm = rec["vm1k"].astype(float)
    tri = beh["trial"]
    use = (tri >= 0) & np.asarray(trial_mask)[np.clip(tri, 0, None)] & np.isfinite(vm)
    e = beh[filt]
    nw, wh = e["nonwhisk"] & use, e["whisk"] & use
    out = {"rest_mean": float(np.mean(vm[nw])) if nw.any() else np.nan,
           "rest_median": float(np.median(vm[nw])) if nw.any() else np.nan,
           "whisk_epoch_change": float(np.mean(vm[wh]) - np.mean(vm[nw])) if nw.any() and wh.any() else np.nan}
    pre_w, d_w = [], []
    for o, c in zip(e["onsets"], e["onset_cut"]):
        if not use[o - 1]:
            continue
        pre = vm[o - 200:o]
        post = vm[o + 100:o + 300].copy()
        if c >= 0:
            post[max(0, c - o - 100):] = np.nan
        if np.isfinite(pre).sum() < 100 or np.isfinite(post).sum() < 20:
            continue
        pre_w.append(np.nanmean(pre))
        d_w.append(np.nanmean(post) - np.nanmean(pre))
    out["n_onsets"] = len(d_w)
    out["whisk_onset_change"] = float(np.mean(d_w)) if d_w else np.nan
    out["whisk_pre"], out["whisk_dvm"] = np.array(pre_w), np.array(d_w)
    # distance to threshold
    thr = trial_thresholds(rec, reading)
    dist = thr[np.clip(tri, 0, None)] - vm
    on = touches(beh, trial_mask, 0.025)
    tmask = np.zeros(len(vm), bool)
    for i in on:
        tmask[i + 4:i + 50] = True
    tmask &= use & (np.r_[tri[4:], np.full(4, -1)] >= 0)
    for name, m in (("nonwhisk", nw), ("whisk", wh), ("touch", tmask)):
        out[f"p10_{name}"] = float(np.percentile(dist[m], 10)) if m.sum() > 10 else np.nan
    out["shift_whisk"] = out["p10_nonwhisk"] - out["p10_whisk"]
    out["shift_touch"] = out["p10_nonwhisk"] - out["p10_touch"]
    out["threshold_median"] = float(np.median(thr))
    vals, _ = phase_binned(beh, filt, vm=vm, use=use)
    fit = phase_fit(vals)
    out["vm_phase_r2"], out["vm_phase_strength"] = fit["r2"], fit["strength"]
    # per-touch values for the effective reversal: pre 0 to 5 ms before onset, post at the peak
    # time of the cell's average PSP
    p = psp_measures(rec.get("touch_avg"), rec.get("touch_avg_n", 0), rec["vm_hz"])
    pre_t, d_t = [], []
    if np.isfinite(p["peak_ms"]):
        k = int(round(p["peak_ms"]))
        for i in on:
            if i - 5 < 0 or i + k >= len(vm) or tri[i - 5] != tri[i] or tri[i + k] != tri[i]:
                continue
            a, b = np.nanmean(vm[i - 5:i]), vm[i + k]
            if np.isfinite(a) and np.isfinite(b):
                pre_t.append(a)
                d_t.append(b - a)
    out["touch_pre"], out["touch_dvm"] = np.array(pre_t), np.array(d_t)
    # touch epoch mean against the pre-touch mean (ion-cut-exc-no-touch's measure)
    out.update(p)
    return out


def reversal(pre, dvm):
    """Effective reversal potential: where a line fitted to dVm against pre-Vm crosses zero."""
    pre, dvm = np.asarray(pre, float), np.asarray(dvm, float)
    ok = np.isfinite(pre) & np.isfinite(dvm)
    if ok.sum() < 5 or np.ptp(pre[ok]) == 0:
        return np.nan, np.nan
    b, a = np.polyfit(pre[ok], dvm[ok], 1)
    return (float(-a / b) if b != 0 else np.nan), float(b)
