"""Loading and measures for Semenov, Kim, Silkuniene & Pakhomov (2025), Cell Rep Phys Sci 6:102660.

Dandiset 001048, which names the paper, holds HEK-cell TIRF recordings of another study. The paper's
data are in the ten dandisets its "Data and code availability" lists (001030 to 001035 and 001271 to
001274); each is pinned below at its only published version. They are streamed with remfile and
h5py; nothing is written to disk.

Where each parameter comes from:
- F (soma emission), F0 (mean before the stimulus) and dF = 100 (F - F0) / F0: paper, Methods,
  "Recording of the optical APs and data analyses" (claims file F1).
- Stimulus onset: 50 ms into the recording for the 250-ms waves (paper, Results and Methods; and the
  session descriptions of 001032 to 001035, "Exposure was triggered 50 ms after the start"); 25 ms
  and 2 s for 001030 (its session descriptions). Claims file F3.
- Field: the session descriptions' "1V translates into 36 V/cm". In 001032 to 001035 the voltage is
  labelled "peak-to-peak"; whether 36 V/cm applies to the peak-to-peak value or to the amplitude
  (half of it) is not said, so both are kept (FIELD_READINGS). In 001030 it is the amplitude ("one
  polarity"). The files also say the labelled voltage "is not the actual amplitude measured on the
  oscilloscope, which will be somewhat smaller"; the calibration is not in the files.
- Soma ROI: claims file O1, readings (a) the Otsu component of the mean pre-stimulus image nearest
  the image centre, (b) that mask eroded by 2 pixels (Otsu and 2 pixels are the claims file's
  standard choices). When the erosion leaves fewer than 4 pixels, the erosion by 1 pixel is used,
  and if that also leaves fewer than 4, the uneroded mask (a choice made here; the count is reported).
- F0 window: claims file O2, readings (a) all frames before the onset (from frame 1; frame 0 is an
  artefact in every file, a bright first frame, and is dropped), (b) the last 20 ms before it.
- AP: claims file O3, a local maximum of dF with width at half height of 2 to 20 ms and at least 5 ms
  from a larger maximum, height above (a) 5% dF or (b) 5 SD of the pre-onset dF. The width is taken
  both at half the peak's height in dF and at half its prominence, and must be 2 to 20 ms under both
  (an assumption, see detect_aps: each measure alone fails on these traces; both are variants).
- Sustained depolarization: claims file O4, no AP in the last 100 ms of the stimulus and mean dF there
  above (a) 5 SD of the pre-onset dF, (b) half the median AP height of the neuron.
- Maximum firing rate: inverse of the interval between the first two APs (paper, Methods; F4).
- Thresholds: minimum field with at least 1 or 5 APs during the stimulus (Figure 2D legend; F5).
"""
import json
import re
import time
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
import requests
from scipy import ndimage, signal

API = "https://api.dandiarchive.org/api"
VERSIONS = {
    "001048": "0.250701.1624",
    "001030": "0.240520.1924",
    "001031": "0.240520.1924",
    "001032": "0.240527.1432",
    "001033": "0.240527.1432",
    "001034": "0.240527.1431",
    "001035": "0.240527.1432",
    "001271": "0.250805.1352",
    "001272": "0.250805.1358",
    "001273": "0.250805.1356",
    "001274": "0.250805.1401",
}
V_TO_VCM = 36.0  # session descriptions: "1V translates into 36 V/cm"
FIELD_READINGS = {"amplitude": 0.5, "peak_to_peak": 1.0}  # factor on the labelled peak-to-peak V

READINGS = [(o1, o2, o3) for o1 in "ab" for o2 in "ab" for o3 in "ab"]

_session = requests.Session()


def list_assets(dandiset):
    """Assets of the pinned version: list of dicts with asset_id, path, size."""
    url = f"{API}/dandisets/{dandiset}/versions/{VERSIONS[dandiset]}/assets/?page_size=1000"
    out = []
    while url:
        j = _session.get(url, timeout=120).json()
        out += [dict(asset_id=a["asset_id"], path=a["path"], size=a["size"]) for a in j["results"]]
        url = j["next"]
    return out


def dandiset_meta(dandiset):
    url = f"{API}/dandisets/{dandiset}/versions/{VERSIONS[dandiset]}/"
    return _session.get(url, timeout=120).json()


def s3_url(dandiset, asset_id):
    j = _session.get(f"{API}/dandisets/{dandiset}/versions/{VERSIONS[dandiset]}/assets/{asset_id}/",
                     timeout=120).json()
    return [u for u in j["contentUrl"] if "s3" in u][0]


def _read_one(args):
    dandiset, asset, with_data = args
    err = None
    for attempt in range(5):
        try:
            url = s3_url(dandiset, asset["asset_id"])
            with h5py.File(remfile.File(url), "r") as f:
                series = list(f["acquisition"].keys())[0]
                ts = f["acquisition"][series]
                rec = dict(asset,
                           dandiset=dandiset,
                           series=series,
                           shape=tuple(ts["data"].shape),
                           rate=float(ts["starting_time"].attrs["rate"]),
                           session_description=f["session_description"][()].decode(),
                           session_id=f["general/session_id"][()].decode(),
                           subject_id=f["general/subject/subject_id"][()].decode(),
                           species=f["general/subject/species"][()].decode(),
                           subject_description=f["general/subject/description"][()].decode(),
                           session_start_time=f["session_start_time"][()].decode(),
                           start=float(ts["starting_time"][()]))
                if with_data:
                    rec["data"] = ts["data"][:]
            return rec
        except Exception as e:  # network hiccups: retry
            err = repr(e)
            time.sleep(2 + 3 * attempt)
    return dict(asset, dandiset=dandiset, error=err)


def load_dandiset(dandiset, with_data=True, threads=32):
    """Stream every file of a time-lapse dandiset (16 x 16 pixel stacks) into memory."""
    assets = list_assets(dandiset)
    with ThreadPoolExecutor(threads) as ex:
        return list(ex.map(_read_one, [(dandiset, a, with_data) for a in assets]))


def parse_stimulus(rec):
    """Stimulus fields from the session description: kind, carrier (Hz), modulation (Hz), volts, ttx."""
    s = rec["session_description"]
    out = dict(kind=None, carrier=None, mod=None, volts=None, ttx="presence of the sodium channel inhibitor" in s)
    if "sham" in s:
        out["kind"] = "sham"
        return out
    g = re.search(r"modulated at ([\d.]+)\s*Hz frequency\) (?:stimulation applied|delivered) at ([\d.]+)\s*kHz "
                  r"(?:using|at) ([\d.,]+)\s*V", s)
    if g:
        out.update(kind="mod", mod=float(g[1]), carrier=float(g[2]) * 1000, volts=float(g[3].replace(",", ".")))
        return out
    g = (re.search(r"applied at ([\d.]+)\s*(k?Hz) using ([\d.,]+)\s*V", s)
         or re.search(r"sine wave at ([\d.]+)\s*(k?Hz) with ([\d.,]+)\s*V", s)
         or re.search(r"^([\d.]+)\s*(k?Hz) stimulation of hippocampal neurons under ([\d.,]+)V", s))
    if g:
        f = float(g[1]) * (1000 if g[2] == "kHz" else 1)
        out.update(kind="sine", carrier=f, volts=float(g[3].replace(",", ".").rstrip(".")))
    return out


def otsu(x):
    """Otsu threshold of an array (standard choice, claims file O1)."""
    v = np.sort(x.ravel())
    best, thr = -1, v[0]
    for t in np.unique(v)[:-1]:
        lo, hi = v[v <= t], v[v > t]
        w0, w1 = len(lo) / len(v), len(hi) / len(v)
        b = w0 * w1 * (lo.mean() - hi.mean()) ** 2
        if b > best:
            best, thr = b, t
    return thr


def soma_mask(img, reading="a"):
    """Claims file O1. (a) Otsu component nearest the centre; (b) eroded by 2 pixels.

    Returns the mask and the erosion actually used (2, 1 or 0) for reading (b)."""
    m = img > otsu(img)
    lab, n = ndimage.label(m)
    c = (np.array(img.shape) - 1) / 2
    best, bd = None, np.inf
    for i in range(1, n + 1):
        yy, xx = np.nonzero(lab == i)
        d = np.min(np.hypot(yy - c[0], xx - c[1]))
        if d < bd:
            bd, best = d, i
    mask = lab == best
    if reading == "c":
        return np.ones_like(img, dtype=bool), 0
    if reading == "a":
        return mask, 0
    for k in (2, 1):
        e = ndimage.binary_erosion(mask, iterations=k)
        if e.sum() >= 4:
            return e, k
    return mask, 0


def trace(data, rate, onset_ms, o1="a", o2="a"):
    """dF (%) of the soma per frame, time (ms) per frame, and info. Frame 0 is dropped."""
    x = data[1:].astype(float)
    t = np.arange(1, len(data)) / rate * 1000.0
    pre = t < onset_ms
    mask, ero = soma_mask(x[pre].mean(0), o1)
    F = x[:, mask].mean(1)
    if o2 == "a":
        w = pre
    else:
        w = pre & (t >= onset_ms - 20)
    F0 = F[w].mean()
    dF = 100.0 * (F - F0) / F0
    return t, dF, dict(npix=int(mask.sum()), erosion=ero, pre_sd=float(dF[pre].std()))


def detect_aps(t, dF, onset_ms, stop_ms, pre_sd, o3="a", width_ref="both"):
    """Claims file O3. APs between onset and stop. Returns peak times (ms), heights (% dF), widths (ms).

    "Width at half height" can be measured two ways, and each alone fails on these traces:
    - at half the peak's height in dF, where dF falls below half the peak value ("height"). A small
      wiggle on the decaying tail of an AP then counts as a second AP 5 ms later, so the first two
      "APs" of a session are often 5 to 7 ms apart (maximum rates of 150 to 200 Hz);
    - at half the peak's prominence ("prominence", scipy's default, used in the first round). Small
      oscillations on a raised plateau then count as APs, so no session can show the claims file's
      sustained depolarization (no AP in the last 100 ms).
    The default ("both") asks for a width of 2 to 20 ms under both: a brief uptick that is distinct
    from its neighbours and returns below half its height within 20 ms (the paper's "brief emission
    upticks"). The returned width is the one at half the height. Each single measure is a variant."""
    dt = np.median(np.diff(t))
    h = 5.0 if o3 == "a" else 5.0 * pre_sd
    pk, _ = signal.find_peaks(dF, height=h, distance=max(1, int(round(5.0 / dt))))
    n = len(dF)
    wh = signal.peak_widths(dF, pk, rel_height=0.5,
                            prominence_data=(dF[pk].astype(float), np.zeros(len(pk), int),
                                             np.full(len(pk), n - 1, int)))[0] * dt
    wp = signal.peak_widths(dF, pk, rel_height=0.5)[0] * dt
    okh = (wh >= 2.0) & (wh <= 20.0)
    okp = (wp >= 2.0) & (wp <= 20.0)
    ok = {"both": okh & okp, "height": okh, "prominence": okp}[width_ref]
    ok = ok & (t[pk] >= onset_ms) & (t[pk] < stop_ms)
    return t[pk][ok], dF[pk][ok], (wh if width_ref != "prominence" else wp)[ok]


def return_duration(t, dF, peak_t):
    """Duration from the rise (last crossing of 0 before the peak) to the first return to 0 after it.

    Claims file, ap-selection, duration reading (b) (excluding the afterhyperpolarization)."""
    i = int(np.searchsorted(t, peak_t))
    a = i
    while a > 0 and dF[a] > 0:
        a -= 1
    b = i
    while b < len(dF) - 1 and dF[b] > 0:
        b += 1
    return t[b] - t[a]


def session_measures(t, dF, info, onset_ms, dur_ms, o3="a", width_ref="both"):
    """AP count, first latency, max rate, and the O4 inputs for one session and reading."""
    stop = onset_ms + dur_ms
    pt, ph, pw = detect_aps(t, dF, onset_ms, stop, info["pre_sd"], o3, width_ref)
    last = (t >= stop - 100) & (t < stop)
    post = (t >= stop) & (t < stop + 50)
    ret = np.array([return_duration(t, dF, x) for x in pt])
    return dict(n_ap=len(pt), ap_t=pt, ap_h=ph, ap_w=pw, ap_ret=ret,
                latency=(pt[0] - onset_ms) if len(pt) else np.nan,
                max_rate=(1000.0 / (pt[1] - pt[0])) if len(pt) > 1 else np.nan,
                n_ap_last100=int(((pt >= stop - 100) & (pt < stop)).sum()),
                mean_last100=float(dF[last].mean()) if last.any() else np.nan,
                mean_post50=float(dF[post].mean()) if post.sum() > 5 else np.nan,
                t_end=float(t[-1]), pre_sd=info["pre_sd"])


def sustained(row, neuron_median_h, o4):
    """Claims file O4: no AP in the last 100 ms and mean dF there above the level."""
    level = 5 * row["pre_sd"] if o4 == "a" else 0.5 * neuron_median_h
    return (row["n_ap_last100"] == 0) and (row["mean_last100"] > level), level


def threshold(volts, counts, k):
    """Minimum field (here volts) with at least k APs; nan if never reached (F5)."""
    v = [v for v, c in zip(volts, counts) if c >= k]
    return min(v) if v else np.nan


# ---------------------------------------------------------------------------------------------
# Time-lapse sessions: one record per session with its dF traces under every ROI and F0 reading.

ROI_READINGS = "abc"  # O1 (a), (b) of the claims file, and (c) the whole 16 x 16 crop deposited


def onset_and_duration(dandiset):
    """Stimulus onset and duration (ms): 001030 from its session descriptions, else the paper (F3)."""
    return (25.0, 2000.0) if dandiset == "001030" else (50.0, 250.0)


def build_records(dandiset, invert=False):
    """Stream a time-lapse dandiset and keep, per session, the stimulus fields and the dF traces.

    invert: Di-8-ANEPPS, whose emission falls with depolarization (paper, Methods; claims F1)."""
    recs = load_dandiset(dandiset, with_data=True)
    onset, dur = onset_and_duration(dandiset)
    out = []
    for r in recs:
        if "error" in r:
            out.append(r)
            continue
        x = r.pop("data")
        r["md5"] = __import__("hashlib").md5(x.tobytes()).hexdigest()
        r["stim"] = parse_stimulus(r)
        r["onset"], r["dur"] = onset, dur
        r["traces"] = {}
        for o1 in ROI_READINGS:
            for o2 in "ab":
                t, dF, info = trace(x, r["rate"], onset, o1, o2)
                if invert:
                    dF = -dF
                r["traces"][(o1, o2)] = (dF.astype(np.float32), info)
        r["t"] = t.astype(np.float32)
        r["n_frames"] = x.shape[0]
        r["frame0_ratio"] = float(x[0].mean() / x[1].mean())
        out.append(r)
    return out


def session_table(records, dandiset, width_ref="both"):
    """One row per session and reading (O1 x O2 x O3) with the session measures."""
    import pandas as pd
    rows = []
    for r in records:
        if "error" in r:
            continue
        st = r["stim"]
        for (o1, o2), (dF, info) in r["traces"].items():
            for o3 in "ab":
                m = session_measures(r["t"], dF, info, r["onset"], r["dur"], o3, width_ref)
                rows.append(dict(dandiset=dandiset, neuron=f"{dandiset}/{r['subject_id']}", path=r["path"],
                                 start=r["start"], session_start_time=r["session_start_time"],
                                 kind=st["kind"], carrier=st["carrier"], mod=st["mod"], volts=st["volts"],
                                 ttx=st["ttx"], o1=o1, o2=o2, o3=o3, npix=info["npix"], **m))
    return pd.DataFrame(rows)


def neuron_of_001030(path):
    """001030 names a subject per session (sub-c7-1-45V); the neuron is the part before the voltage."""
    return re.match(r"sub-(c\d+)-", path)[1]


def split_before_after(g):
    """001271: sessions before and after the change of solution, for one neuron (rows sorted by start).

    TTX sessions are labelled; vehicle neurons are not, so the split is the longest pause between
    sessions (an assumption: the Figure S2 legend says 'about 5 min after' the change, and the pauses
    between blocks are about 300 s, those within blocks 15 to 60 s). Returns (before, after, gap_s)."""
    g = g.sort_values("start")
    if g.ttx.any():
        return g[~g.ttx], g[g.ttx], np.nan
    gaps = np.diff(g.start.values)
    i = int(np.argmax(gaps))
    return g.iloc[: i + 1], g.iloc[i + 1:], float(gaps[i])


# ---------------------------------------------------------------------------------------------
# Strobe imaging (001273, 001274). Paper, Methods, "Pulsed laser fluorescence microscopy".
#
# - Frame timing: 50-ns steps for pulses, 20-us steps for sine waves (paper); the pulse starts 1 us
#   into the recording (file descriptions, "Exposures began 1 us after the start"), so at frame 20,
#   and ends at frame 60. "Backward" recordings were taken in reverse order (session descriptions)
#   and are reversed here.
# - Flash intensity: the paper scales each frame to a "debris ROI"; the files mark none, so reading
#   (a) scales each frame to the median of the whole image (a choice made here, the image being
#   mostly background and unpolarized cell), reading (b) does not scale (claims file O5). Frames
#   whose median is below 0.8 of the file's median (missed flashes, such as frame 0) are dropped.
# - ROIs: the paper's RATIO image, POLARIZED (last 0.5 us of the pulse) over CONTROL (before the
#   pulse and the last 1.5 us), each low-pass filtered over 12 x 12 pixels; ROI 1 is centred on the
#   most hyperpolarized and ROI 2 on the most depolarized point inside the cell (pixels above the
#   Otsu threshold of the filtered CONTROL image). The ROI is a 12 x 12 pixel box, the filter's size
#   (a standard choice: the paper does not give the ROI size).
# - F0: mean before the pulse; for sine waves the mean of the first and last carrier cycles (0.5 ms
#   each), when the amplitude is minimal (paper).
# - Field: 257 V/cm for the 2-us pulses of 001274 and a 136 V/cm peak for its sine waves (paper,
#   Figures 5 and 6 legends; the files give the generator voltages, 10 V and 7 V peak to peak).
#   The modulated wave is E(t) = Epk sin^2(pi fm t) sin(2 pi 2000 t), starting at minimal amplitude
#   (paper, Methods) at zero carrier phase (the recording starts with the wave, file description).

PULSE_ON, PULSE_OFF = 20, 60


def read_strobe(url):
    with h5py.File(remfile.File(url), "r") as f:
        return f["acquisition/StrobeImaging/data"][:]


def frame_scale(X):
    med = np.median(X.reshape(len(X), -1), axis=1).astype(float)
    good = med > 0.8 * np.median(med)
    return med, good


def find_rois(stack, good, half=6):
    """ROI 1 (most hyperpolarized) and ROI 2 (most depolarized) centres from a pulse stack (frames x y x)."""
    n = len(stack)
    pol_i = [i for i in range(PULSE_OFF - 10, PULSE_OFF) if good[i]]
    ctl_i = [i for i in list(range(1, PULSE_ON)) + list(range(n - 30, n)) if good[i]]
    pol = ndimage.uniform_filter(stack[pol_i].mean(0), 12)
    ctl = ndimage.uniform_filter(stack[ctl_i].mean(0), 12)
    ratio = pol / ctl
    cell = ctl > otsu(ctl[::4, ::4])
    edge = np.zeros_like(cell)
    edge[half:-half, half:-half] = True
    r = np.where(cell & edge, ratio, np.nan)
    c1 = np.unravel_index(np.nanargmin(r), r.shape)
    c2 = np.unravel_index(np.nanargmax(r), r.shape)
    return c1, c2, ratio, cell


def box(X, c, half=6):
    """Mean over a (2 half) x (2 half) box centred on c, clipped at the image edge. The 12 x 12 box
    (half 6) is an assumption: the paper drew ROIs by hand and gives no size; 6 x 6 and 20 x 20 are
    shown as a variant."""
    return X[:, max(c[0] - half, 0):c[0] + half, max(c[1] - half, 0):c[1] + half].astype(float).mean((1, 2))


def pulse_dF(F, good, base):
    F = F.copy()
    F[~good] = np.nan
    return 100.0 * (F / np.nanmean(F[base]) - 1.0)


def fit_charging(t_us, dF):
    """dF = A (1 - exp(-t / tau)) over the pulse; returns A, tau (us)."""
    from scipy.optimize import curve_fit
    ok = np.isfinite(dF)
    p, _ = curve_fit(lambda t, A, tau: A * (1 - np.exp(-t / tau)), t_us[ok], dF[ok],
                     p0=(dF[ok][-5:].mean() or 1.0, 0.7), bounds=([-np.inf, 0.01], [np.inf, 20]), maxfev=20000)
    return p


def fit_discharging(t_us, dF, A_fixed=None):
    """dF = A exp(-t / tau) after the pulse; A free (reading a) or fixed (reading b). Returns A, tau."""
    from scipy.optimize import curve_fit
    ok = np.isfinite(dF)
    if A_fixed is None:
        p, _ = curve_fit(lambda t, A, tau: A * np.exp(-t / tau), t_us[ok], dF[ok],
                         p0=(dF[ok][:5].mean() or 1.0, 0.9), bounds=([-np.inf, 0.01], [np.inf, 20]), maxfev=20000)
        return p
    p, _ = curve_fit(lambda t, tau: A_fixed * np.exp(-t / tau), t_us[ok], dF[ok], p0=(0.9,), bounds=([0.01], [20]), maxfev=20000)
    return A_fixed, p[0]


def sine_field(n, fm, epk=0.136, dt=20e-6, fc=2000.0, phase=0.0):
    t = np.arange(n) * dt
    env = np.sin(np.pi * fm * t) ** 2
    return t, epk * env * np.sin(2 * np.pi * fc * t + phase), env


def loess(x, y, span, degree=2):
    """R's loess with family "gaussian" (its default): at each point a weighted least-squares fit of
    degree 2 (R's default) over the nearest span * n points, with tricube weights, no robustness
    iterations. The paper ran its LOESS in RStudio (Table S1); the span is the claims file's O6."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    n = len(x)
    q = max(degree + 2, int(np.floor(span * n)))
    out = np.empty(n)
    for i in range(n):
        d = np.abs(x - x[i])
        idx = np.argpartition(d, q - 1)[:q]
        h = d[idx].max()
        w = (1 - (d[idx] / (h * 1.0000001)) ** 3) ** 3
        X = np.vander(x[idx] - x[i], degree + 1, increasing=True)
        sw = np.sqrt(w)
        beta = np.linalg.lstsq(X * sw[:, None], y[idx] * sw, rcond=None)[0]
        out[i] = beta[0]
    return out


def carrier_phase(t, osc, env, fc=2000.0):
    """Phase (rad) and amplitude of the carrier in an oscillation trace: least squares of osc on
    env sin(2 pi fc t) and env cos(2 pi fc t). Phase 0 means in phase with the assumed field, pi in
    antiphase."""
    X = np.c_[env * np.sin(2 * np.pi * fc * t), env * np.cos(2 * np.pi * fc * t)]
    a, b = np.linalg.lstsq(X, osc, rcond=None)[0]
    return float(np.arctan2(b, a)), float(np.hypot(a, b))
