"""Loading and measures for dandiset 000939 (Duszkiewicz et al. 2024, Nat Neurosci 27, 782-792).

Every file is streamed from the DANDI Archive at the pinned version (DANDISET, VERSION); nothing
is written to disk. Where each parameter comes from is said next to it:

- "Methods" is the paper's Methods section (paper/ in the registry, PMC11001581);
- "code" is the paper's MATLAB code, figshare doi:10.6084/m9.figshare.24921252 version 3,
  MatlabCode_Duszkiewicz2024.zip (md5 8f391dec0d3fa120ef58f3158443f5df), read while writing
  this module and not run here;
- "claim" is the claims file, claims/000939/10.1038-s41593-024-01588-5.yaml;
- "assumption" or "standard choice" marks what neither the paper nor its code fixes.
"""
from __future__ import annotations

import io
import tarfile
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
import requests
import scipy.io as sio
from scipy.ndimage import gaussian_filter1d

DANDISET = "000939"
VERSION = "0.261016.2310"
API = "https://api.dandiarchive.org/api"

# figshare item of the paper (Data availability), version 3; used only for the ADN recordings
FIGSHARE_ARTICLE = 24921252
FIGSHARE_VERSION = 3
FIGSHARE_ADN_FILE = 43857150  # Dataset_5.tar.gz, ADN recordings (claim, data: elsewhere)
FIGSHARE_OPTO_FILE = 43857159  # Dataset_6.tar.gz, optogenetic sessions (claim, data: elsewhere)
FIGSHARE_NPX_FILE = 43857156  # Dataset_4.tar.gz, Neuropixel session (claim, data: elsewhere)
FIGSHARE_CUE_FILE = 43857153  # Dataset_3.tar.gz, cue rotation sessions (claim, data: elsewhere)

NBINS = 360          # 1 degree bins (Methods, HD tuning curves)
SMOOTH_SD = 3        # Gaussian s.d. in bins (Methods; code smoothTC = 3)
SPEED_TH = 2.0       # cm/s (Methods, "speed exceeded 2 cm s-1"; code velTh = 2)
RATE_MIN = 0.5       # Hz over the square epoch (Methods; code GetCellTypes_PoSub gd)
FS_RATE = 10.0       # Hz (Methods; code)
TTP_CUT = 0.4        # ms (Methods); the code's 0.35 is a variant
HD_INFO_TH = 0.2     # bits per spike (Methods, Results; code)


# ----------------------------------------------------------------------------------------------
# Archive

def assets(version: str = VERSION) -> list[dict]:
    """The NWB assets of the pinned version, sorted by path."""
    url = f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=200"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r.get("next")
    return sorted(out, key=lambda a: a["path"])


def s3_url(asset_id: str) -> str:
    r = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60)
    return r.url


def _str(x):
    x = x[()]
    return x.decode() if isinstance(x, bytes) else str(x)


def light_pulses(f) -> np.ndarray:
    """Onset and offset times (s) of the light pulses, from processing/ogen/optogenetic_stim.

    The series' length is either the session's sample count at the stated 20 kHz (one file,
    values 0 and 1) or four times it (values 0 to 16368 on every fourth sample), so it holds
    four channels interleaved in one dimension. It is read as (n, channels) at 20 kHz, with the
    number of channels the ratio of its length to that of the raw ElectricalSeries; the
    channel with the largest value is the light, high above half its maximum (standard choice).
    """
    d = f["processing/ogen/optogenetic_stim/data"]
    rate = float(f["processing/ogen/optogenetic_stim/starting_time"].attrs["rate"])
    n = d.shape[0]
    nch = int(round(n / f["acquisition/ElectricalSeries/data"].shape[0]))
    block = nch * 2 ** 22
    segs, top = [], 0
    for i in range(0, n, block):
        x = d[i:i + block]
        if x.max() <= 0:
            continue
        x = x[: len(x) // nch * nch].reshape(-1, nch)
        top = max(top, int(x.max()))
        segs.append((i // nch, x[:, np.argmax(x.max(0))]))
    on, off, prev = [], [], False
    for i0, x in segs:
        x = x > top / 2
        dx = np.diff(np.concatenate([[prev], x]).astype(int))
        on += list(i0 + np.where(dx == 1)[0])
        off += list(i0 + np.where(dx == -1)[0])
        prev = bool(x[-1])
    on = np.array(on) / rate
    off = np.array(off) / rate
    return np.c_[on[: len(off)], off[: len(on)]]


def load_session(asset: dict) -> dict:
    """Read what the analyses use from one NWB file, streamed.

    Kept: epochs, sleep states, head direction and position with their timestamps, and per
    unit the spike times, trough-to-peak, the dandiset's own labels (is_excitatory,
    is_fast_spiking, is_head_direction), the peak electrode, and the mean waveform on that
    electrode; light pulses where the file has an optogenetic series.
    """
    f = h5py.File(remfile.File(s3_url(asset["asset_id"])), "r")
    s = {"path": asset["path"], "subject": _str(f["general/subject/subject_id"]),
         "session_id": _str(f["general/session_id"])}
    probe = [f["general/devices"][k].attrs.get("description", "") for k in f["general/devices"]
             if "probe" in k.lower()]
    s["probe"] = probe[0] if probe else ""
    s["orientation"] = "vertical" if "vertically" in s["probe"] else "parallel"
    s["virus"] = _str(f["general/virus"]) if "general/virus" in f else ""
    s["genotype"] = _str(f["general/subject/description"])
    e = f["intervals/epochs"]
    s["epochs"] = {}
    tags = [t.decode() if isinstance(t, bytes) else t for t in e["tags"][:]]
    for tag, a, b in zip(tags, e["start_time"][:], e["stop_time"][:]):
        s["epochs"].setdefault(tag, []).append((float(a), float(b)))
    ss = f["intervals/sleep_states"]
    st = np.array([x.decode() for x in ss["state"][:]])
    s["sleep"] = {k: np.c_[ss["start_time"][:][st == k], ss["stop_time"][:][st == k]].astype(float)
                  for k in np.unique(st)}
    hd = f["processing/behavior/CompassDirection/head-direction"]
    s["hd_t"] = hd["timestamps"][:]
    s["hd"] = hd["data"][:]
    s["hd_unit"] = hd["data"].attrs.get("unit")
    pos = f["processing/behavior/Position/position"]
    s["pos_t"] = pos["timestamps"][:]
    s["pos"] = pos["data"][:]
    s["pos_unit"] = pos["data"].attrs.get("unit")
    u = f["units"]
    idx = u["spike_times_index"][:]
    st_all = u["spike_times"][:]
    s["spikes"] = np.split(st_all, idx[:-1])
    s["unit_id"] = u["id"][:]
    s["ttp"] = u["trough_to_peak"][:]
    s["lab_ex"] = u["is_excitatory"][:].astype(bool)
    s["lab_fs"] = u["is_fast_spiking"][:].astype(bool)
    s["lab_hd"] = u["is_head_direction"][:].astype(bool)
    s["peak_el"] = u["electrode_index"][:]
    wf = u["waveform_mean"]
    s["wf_shape"] = wf.shape
    w = wf[:]
    s["wf_peak"] = w[np.arange(len(w)), :, s["peak_el"]] if w.shape[2] > s["peak_el"].max() else None
    s["spike_res"] = u["spike_times"].attrs.get("resolution")
    if "processing/ogen/optogenetic_stim" in f:
        s["ogen_len"] = f["processing/ogen/optogenetic_stim/data"].shape[0]
        s["ephys_len"] = f["acquisition/ElectricalSeries/data"].shape[0]
        s["pulses"] = light_pulses(f)
    return s


def load_all(version: str = VERSION, workers: int = 8) -> list[dict]:
    a = [x for x in assets(version) if x["path"].endswith(".nwb")]
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(load_session, a))


# ----------------------------------------------------------------------------------------------
# Intervals

def in_intervals(t, iv) -> np.ndarray:
    iv = np.asarray(iv, float).reshape(-1, 2)
    m = np.zeros(len(t), bool)
    for a, b in iv:
        m |= (t >= a) & (t < b)
    return m


def tracked_epoch(s, tag: str):
    """The epoch from its first to its last tracked HD sample (code, GetHdTuning: ep is set to
    the range of the restricted angle)."""
    a, b = s["epochs"][tag][0]
    m = (s["hd_t"] >= a) & (s["hd_t"] < b) & np.isfinite(s["hd"])
    t = s["hd_t"][m]
    return (float(t[0]), float(t[-1]))


def speed(s) -> np.ndarray:
    """Speed (cm/s) at each position sample.

    The files hold no speed. It is computed from the position (cm) as the distance between
    successive samples over their time step, after smoothing each coordinate with a Gaussian of
    0.1 s s.d. (10 samples at 100 Hz). Assumption: the paper's Velocity series is not described;
    the smoothing only removes tracking jitter that would otherwise put the stationary animal
    above 2 cm/s.
    """
    t = s["pos_t"]
    p = s["pos"].copy()
    bad = ~np.isfinite(p).all(1)
    for k in range(2):
        x = p[:, k]
        if bad.any():
            x[bad] = np.interp(t[bad], t[~bad], x[~bad])
        p[:, k] = gaussian_filter1d(x, 10)
    v = np.r_[0, np.hypot(*np.diff(p, axis=0).T) / np.diff(t)]
    v[bad] = np.nan
    return v


def good_samples(s, tag="wake_square", speed_th=SPEED_TH, iv=None) -> np.ndarray:
    """Mask of HD samples used for tuning: inside the tracked epoch, HD finite, speed above
    the threshold (Methods; code GetHdTuning)."""
    t = s["hd_t"]
    a, b = tracked_epoch(s, tag) if iv is None else (None, None)
    m = np.isfinite(s["hd"])
    m &= in_intervals(t, [(a, b)]) if iv is None else in_intervals(t, iv)
    if speed_th:
        v = speed(s)
        if len(v) == len(t):
            m &= v > speed_th
        else:
            m &= np.interp(t, s["pos_t"], np.nan_to_num(v)) > speed_th
    return m


# ----------------------------------------------------------------------------------------------
# Tuning curves

def smooth_circ(h, sd):
    """Circular Gaussian smoothing along the first axis, s.d. in bins (code, gaussFiltAng)."""
    if not sd:
        return h
    return gaussian_filter1d(h, sd, axis=0, mode="wrap")


def tuning_curves(spikes, t, ang, mask, nbins=NBINS, sd=SMOOTH_SD, reverse=False):
    """HD tuning curves (Hz), shape (nbins, n units), from the HD samples where mask is true.

    As in the code's HeadDirectionField: each spike takes the angle of its nearest sample,
    spikes are kept only where that sample is used, counts over occupancy times the sampling
    rate, empty bins set to 0, then circular Gaussian smoothing. With reverse=True the angle
    values of the used samples are reversed in time, the time-reversed control (Methods; code).
    Bins are centred on 0, 1, ..., 359 degrees (code, hist with centres B).
    """
    tt = t[mask]
    aa = np.mod(ang[mask], 2 * np.pi)
    if reverse:
        aa = aa[::-1]
    dt = np.median(np.diff(t))
    b = np.round(aa / (2 * np.pi) * nbins).astype(int) % nbins
    occ = np.bincount(b, minlength=nbins).astype(float)
    # the used samples, as intervals of +-dt/2 around each
    out = np.zeros((nbins, len(spikes)))
    for i, sp in enumerate(spikes):
        j = np.searchsorted(tt, sp)
        j = np.clip(j, 1, len(tt) - 1)
        left = tt[j - 1]
        right = tt[j]
        jj = np.where(sp - left < right - sp, j - 1, j)
        ok = np.abs(sp - tt[jj]) <= dt / 2 + 1e-9
        out[:, i] = np.bincount(b[jj[ok]], minlength=nbins)
    with np.errstate(invalid="ignore", divide="ignore"):
        h = out / occ[:, None] / dt
    h[~np.isfinite(h)] = 0
    return smooth_circ(h, sd), occ


def hd_info(h, occ):
    """HD information in bits per spike (Methods formula; code SpatialInfo)."""
    p = occ / occ.sum()
    f = (p[:, None] * h).sum(0)
    with np.errstate(invalid="ignore", divide="ignore"):
        r = h / f
        v = np.where(r > 0, p[:, None] * r * np.log2(np.where(r > 0, r, 1)), 0)
    return v.sum(0)


def split_halves(t, mask):
    """Split the used samples into two halves of equal duration (code, regIntervals(ep, 2)).
    Assumption: the halves are halves of the used time, taken in order."""
    idx = np.where(mask)[0]
    k = len(idx) // 2
    m1 = np.zeros_like(mask)
    m2 = np.zeros_like(mask)
    m1[idx[:k]] = True
    m2[idx[k:]] = True
    return m1, m2


def peak_width(h):
    """Width (degrees) of each tuning curve: peak-aligned, max-normalized curve, the mean of
    its two sides, twice the first index (1-based) below 0.5 (code, Figure_Fourier tcWidth).
    Also the multipeak score, the mean of the normalized curve outside +-width of the peak
    (Methods; code offFR)."""
    n = h.shape[0]
    w = np.full(h.shape[1], np.nan)
    off = np.full(h.shape[1], np.nan)
    for i in range(h.shape[1]):
        if not np.any(h[:, i] > 0):
            continue
        x = np.roll(h[:, i], -np.argmax(h[:, i]))
        x = x / x.max()
        side = (x[: n // 2 + 1] + np.r_[x[n // 2:], x[:1]][::-1]) / 2
        k = np.where(side < 0.5)[0]
        if len(k):
            w[i] = (k[0] + 1) * 2
            wi = int(w[i])
            off[i] = x[wi - 1: n - wi].mean()
    return w, off


def fourier(h, ncomp=180):
    """Complex Fourier coefficients of each tuning curve on harmonics 1..ncomp (code,
    Figure_Fourier: basis cos(n t) + i sin(n t), divided by the number of bins)."""
    n = h.shape[0]
    t = np.deg2rad(np.arange(n))
    basis = np.exp(1j * np.outer(np.arange(1, ncomp + 1), t))
    return basis @ h / n


def power(ft, reading="sq"):
    """Power per harmonic: 'sq' the squared modulus (code, ft .* conj(ft)); 'rms' the root mean
    square of the sine and cosine projections (Methods' words), sqrt((re^2 + im^2) / 2)."""
    if reading == "sq":
        return np.abs(ft) ** 2
    return np.sqrt((ft.real ** 2 + ft.imag ** 2) / 2)


def norm10(p):
    q = p[:10]
    return q / q.sum(0)


def kl(p, q):
    """D_KL(p || q) along axis 0, natural log (Methods formula)."""
    return np.sum(p * np.log(p / q), axis=0)


def xval_autocorr(h1, h2):
    """Cross-validated tuning curve auto-correlogram: Pearson correlation between curve 1 and
    curve 2 circularly shifted by 0..359 bins (Methods; code GetTuningAutocorr_xval)."""
    z1 = (h1 - h1.mean(0)) / h1.std(0, ddof=1)
    z2 = (h2 - h2.mean(0)) / h2.std(0, ddof=1)
    n = h1.shape[0]
    f1 = np.fft.fft(z1, axis=0)
    f2 = np.fft.fft(z2, axis=0)
    # sum_k z1[k] z2[k - s] for circshift(z2, s)
    ac = np.real(np.fft.ifft(np.conj(np.conj(f1) * f2), axis=0))
    return ac / (n - 1)


def zero_lag_r(a, b):
    """Pearson correlation of matching columns."""
    a = a - a.mean(0)
    b = b - b.mean(0)
    return (a * b).sum(0) / np.sqrt((a * a).sum(0) * (b * b).sum(0))


def circ_xcorr_lag(h1, h2):
    """Lag (bins) of maximum circular cross-correlation of each column of h2 against h1:
    corr(h1, roll(h2, -lag)) is largest."""
    z1 = (h1 - h1.mean(0)) / h1.std(0)
    z2 = (h2 - h2.mean(0)) / h2.std(0)
    c = np.real(np.fft.ifft(np.conj(np.fft.fft(z1, axis=0)) * np.fft.fft(z2, axis=0), axis=0))
    return np.argmax(c, axis=0)


# ----------------------------------------------------------------------------------------------
# Spike counts

def bin_counts(spikes, edges):
    return np.stack([np.histogram(sp, edges)[0] for sp in spikes], 1).astype(float)


# ----------------------------------------------------------------------------------------------
# ADN recordings, figshare (claims with data: elsewhere)

def _tsd(obj):
    o = obj[0, 0]
    return np.asarray(o["t"]).ravel().astype(float), np.asarray(o["data"]).ravel().astype(float)


def _csv_cols(b: bytes, k: int) -> np.ndarray:
    """The first k numeric fields of each line of a CSV (some files end lines with empty fields)."""
    rows = []
    for line in b.decode().splitlines():
        f = [x for x in line.strip().split(",") if x.strip() != ""]
        if len(f) >= k:
            rows.append([float(x) for x in f[:k]])
    return np.array(rows)


def load_adn(workers: int = 1, file_id: int = FIGSHARE_ADN_FILE) -> list[dict]:
    """Stream a tarball of the figshare item (Dataset_5.tar.gz, ADN recordings, by default; or
    Dataset_6.tar.gz, optogenetic sessions) and read, per session,
    the spike times (Data/SpikeData.mat, S.C, in seconds), head direction and speed
    (Data/Angle.mat, Data/Velocity.mat, TStoolbox tsd objects), the epochs
    (Data/BehavEpochs.mat), the brain area (Data/BrainArea.mat), the files' own cell types
    (Data/CellTypes.mat), the group (Data/Groups.mat, 1 ArchT and 2 control) and the light
    pulses (Data/Opto_TS.csv, onset and offset in s). Nothing is written to disk."""
    url = f"https://ndownloader.figshare.com/files/{file_id}"
    r = requests.get(url, stream=True, timeout=120)
    r.raw.decode_content = True
    tf = tarfile.open(fileobj=r.raw, mode="r|gz")
    out: dict[str, dict] = {}
    for m in tf:
        if not m.isfile() or "/._" in m.name or m.name.count("/") < 3:
            continue
        _, ses, sub, fname = m.name.split("/", 3)
        if sub != "Data":
            continue
        b = tf.extractfile(m).read()
        d = out.setdefault(ses, {"session": ses})
        if fname == "SpikeData.mat":
            x = sio.loadmat(io.BytesIO(b))
            cells = x["S"][0, 0]["C"].ravel()
            d["spikes"] = []
            for c in cells:
                o = c[0, 0]["tsd"][0, 0]  # ts object holding a tsd; its t field is the spike times (s)
                d["spikes"].append(np.asarray(o["t"]).ravel().astype(float))
        elif fname == "Angle.mat":
            d["hd_t"], d["hd"] = _tsd(sio.loadmat(io.BytesIO(b))["ang"])
        elif fname == "Velocity.mat":
            d["vel_t"], d["vel"] = _tsd(sio.loadmat(io.BytesIO(b))["vel"])
        elif fname == "BrainArea.mat":
            x = sio.loadmat(io.BytesIO(b))
            d["adn"] = x["adn"].ravel().astype(bool)
            d["pos_area"] = x["pos"].ravel().astype(bool)
        elif fname == "BehavEpochs.mat":
            x = sio.loadmat(io.BytesIO(b))
            for k in x:
                if k.endswith("Ep") and not k.endswith("_Info"):
                    o = x[k][0, 0]
                    d.setdefault("eps", {})[k] = np.c_[np.ravel(o["start"]), np.ravel(o["stop"])].astype(float)
        elif fname == "CellTypes.mat":
            x = sio.loadmat(io.BytesIO(b))
            d["file_hd"] = x["hd"].ravel().astype(bool)
            d["file_types"] = {k: x[k].ravel().astype(bool) for k in ("gd", "hd", "fs", "ex", "nhd") if k in x}
        elif fname == "Groups.mat":
            d["group"] = int(np.ravel(sio.loadmat(io.BytesIO(b))["g"])[0])
        elif fname in ("WaveformFeatures.mat", "CellDepth.mat"):
            x = sio.loadmat(io.BytesIO(b))
            d.setdefault("mat", {}).update({k: v for k, v in x.items() if not k.startswith("__") and not k.endswith("_Info")})
        elif fname == "CueEpochs.mat":
            x = sio.loadmat(io.BytesIO(b))
            d["cueEp"] = x["cueEp"].astype(float)
            d["cueID"] = x["cueID"].ravel()
        elif fname == "LED1_TS.csv":
            d["led1"] = _csv_cols(b, 2)
        elif fname == "Tracking_data.csv" and file_id == FIGSHARE_CUE_FILE:
            d["track"] = np.loadtxt(io.BytesIO(b), delimiter=",", ndmin=2)
        elif fname == "Opto_TS.csv":
            d["pulses"] = np.loadtxt(io.BytesIO(b), delimiter=",", ndmin=2)
    return [out[k] for k in sorted(out)]


# ----------------------------------------------------------------------------------------------
# Classes and tests

def classify(U, cut=TTP_CUT, code=False):
    """Excitatory and FS masks over a unit table with columns gd, rate, ttp. Methods: FS below
    0.4 ms and above 10 Hz, excitatory above 0.4 ms and below 10 Hz. code=True follows
    GetCellTypes_PoSub (FS rate >= 10 and ttp <= cut, excitatory ttp > cut and rate <= 10)."""
    gd = U.gd
    if code:
        return gd & (U.ttp > cut) & (U.rate <= FS_RATE), gd & (U.rate >= FS_RATE) & (U.ttp <= cut)
    return gd & (U.ttp > cut) & (U.rate < FS_RATE), gd & (U.rate > FS_RATE) & (U.ttp < cut)


def signrank(x, y):
    """Two-sided Wilcoxon signed-rank test, with the normal-approximation z (as MATLAB's
    signrank reports it), on the pairs where both values are finite."""
    from scipy import stats
    x, y = np.asarray(x, float), np.asarray(y, float)
    ok = np.isfinite(x) & np.isfinite(y)
    r = stats.wilcoxon(x[ok], y[ok], method="approx")
    return dict(n=int(ok.sum()), median_a=float(np.median(x[ok])), median_b=float(np.median(y[ok])),
                z=float(r.zstatistic), p=float(r.pvalue))


def ranksum(x, y):
    """Two-sided Mann-Whitney U test with its normal-approximation z (positive when x ranks
    higher), on finite values."""
    from scipy import stats
    x, y = np.asarray(x, float), np.asarray(y, float)
    x, y = x[np.isfinite(x)], y[np.isfinite(y)]
    r = stats.mannwhitneyu(x, y, alternative="two-sided", method="asymptotic")
    n1, n2 = len(x), len(y)
    z = (r.statistic - n1 * n2 / 2) / np.sqrt(n1 * n2 * (n1 + n2 + 1) / 12)
    return dict(n_a=n1, n_b=n2, median_a=float(np.median(x)), median_b=float(np.median(y)),
                z=float(z), p=float(r.pvalue))


def show(d, label=""):
    print(label, ", ".join(f"{k}={v:.4g}" if isinstance(v, float) else f"{k}={v}" for k, v in d.items()))


def circ_corrcc(a, b):
    """Circular-circular correlation and its p-value (CircStat circ_corrcc, used by the code)."""
    from scipy import stats
    ma, mb = stats.circmean(a), stats.circmean(b)
    sa, sb = np.sin(a - ma), np.sin(b - mb)
    rho = np.sum(sa * sb) / np.sqrt(np.sum(sa ** 2) * np.sum(sb ** 2))
    n = len(a)
    l20, l02, l22 = np.mean(sa ** 2), np.mean(sb ** 2), np.mean(sa ** 2 * sb ** 2)
    ts = np.sqrt(n * l20 * l02 / l22) * rho
    return float(rho), float(2 * (1 - stats.norm.cdf(abs(ts))))


def contamination(sp, half=0.1, binw=0.001):
    """Cluster contamination score: spike autocorrelogram in 1 ms bins (centred on whole ms) over
    +-100 ms (Methods), the count in the bin next to zero (0.5 to 1.5 ms; code,
    GetClusterQualityScore takes the bin before the zero bin, which the code zeroes) over the
    highest bin."""
    sp = np.sort(sp)
    nb = int(round(half / binw))
    counts = np.zeros(nb + 1)
    k = 1
    while k < len(sp):
        d = sp[k:] - sp[:-k]
        d = d[d < (nb + 0.5) * binw]
        if not len(d):
            break
        counts += np.bincount(np.round(d / binw).astype(int), minlength=nb + 1)[: nb + 1]
        k += 1
    counts[0] = 0
    return counts[1] / counts.max() if counts.max() > 0 else np.nan


def adn_tuning(a, speed_th=SPEED_TH, sd=SMOOTH_SD):
    """Square-epoch tuning curves of an ADN session (figshare), as GetHdTuning: the epoch is
    wake1Ep (or wakeEp) from its first to last tracked sample, at speed above the threshold
    (the file's Velocity series)."""
    eps = a["eps"]
    ep = eps["wake1Ep"] if "wake1Ep" in eps and len(eps["wake1Ep"]) else eps["wakeEp"]
    t, ang = a["hd_t"], a["hd"]
    m = in_intervals(t, ep) & np.isfinite(ang)
    tt = t[m]
    m &= (t >= tt[0]) & (t <= tt[-1])
    v = np.interp(t, a["vel_t"], a["vel"])
    m_all = m.copy()
    if speed_th:
        m &= v > speed_th
    h, occ = tuning_curves(a["spikes"], t, ang, m, sd=sd)
    hr, occr = tuning_curves(a["spikes"], t, ang, m, sd=sd, reverse=True)
    m1, m2 = split_halves(t, m)
    h1, _ = tuning_curves(a["spikes"], t, ang, m1, sd=sd)
    h2, _ = tuning_curves(a["spikes"], t, ang, m2, sd=sd)
    dur = float(ep[:, 1].sum() - ep[:, 0].sum())
    rate = np.array([in_intervals(sp, ep).sum() for sp in a["spikes"]]) / dur
    return dict(h=h, h_rev=hr, info=hd_info(h, occ), info_rev=hd_info(hr, occr), h1=h1, h2=h2, rate=rate)


def rm_interaction(Y, X):
    """Within-subject factor by between-subject term interaction of a repeated-measures ANOVA
    (univariate test, as MATLAB's ranova): Y is (subjects, levels), X the between-subjects
    design without intercept (a numeric covariate, or dummies for a factor). Returns F, df1,
    df2, p."""
    from scipy import stats
    n, k = Y.shape
    D = Y - Y.mean(1, keepdims=True)
    Xd = np.c_[np.ones(n), X]
    beta, *_ = np.linalg.lstsq(Xd, D, rcond=None)
    fit = Xd @ beta
    ss_err = ((D - fit) ** 2).sum()
    ss_int = ((fit - D.mean(0)) ** 2).sum()
    q = Xd.shape[1] - 1
    df1, df2 = (k - 1) * q, (k - 1) * (n - q - 1)
    F = (ss_int / df1) / (ss_err / df2)
    return float(F), df1, df2, float(stats.f.sf(F, df1, df2))


def bayes_decode(tc, counts, dt):
    """One-dimensional Bayesian decoding with Poisson spiking and a flat prior (code,
    BayesReconstruction_1D): for each time bin the angle bin that maximizes
    sum_i n_i log f_i(theta) - dt sum_i f_i(theta). tc is (angle bins, cells) in Hz, counts
    (time bins, cells). A floor of 1e-6 Hz on the curves avoids log(0) (standard choice)."""
    f = np.maximum(tc, 1e-6)
    ll = counts @ np.log(f).T - dt * f.sum(1)[None, :]
    return np.argmax(ll, axis=1)


def angdiff(a, b):
    return np.angle(np.exp(1j * (a - b)))


ISO_FIT_MAX = 4000  # assumption: Isomap is fitted on at most this many population vectors


def isomap_embed(X, n_components, seed, fit_max=ISO_FIT_MAX):
    """Isomap with 12 neighbours (Methods). scikit-learn's Isomap stands in for the MATLAB
    Dimensionality Reduction Toolbox. Assumption, for time: when there are more than fit_max
    vectors, the embedding is fitted on fit_max of them drawn at random (seeded) and the others
    are placed by the fitted model's out-of-sample transform."""
    from sklearn.manifold import Isomap
    iso = Isomap(n_neighbors=12, n_components=n_components)
    if len(X) <= fit_max:
        return iso.fit_transform(X)
    rng = np.random.default_rng(seed)
    idx = np.sort(rng.choice(len(X), fit_max, replace=False))
    iso.fit(X[idx])
    return iso.transform(X)


def pop_vectors(spikes, edges, sd_bins=2):
    """Population vectors: counts in the bins, Gaussian smoothing of sd_bins bins (400 ms for
    200 ms bins), square root (Methods)."""
    Q = gaussian_filter1d(bin_counts(spikes, edges), sd_bins, axis=0)
    return np.sqrt(Q)


def virtual_hd(emb, real):
    """Virtual HD from the first two Isomap dimensions, atan2(dim1, dim2) as the code; direction
    chosen by the smaller circular variance of the difference from the real HD (Methods).
    real may hold NaN, which are ignored."""
    v = np.arctan2(emb[:, 0], emb[:, 1])
    ok = np.isfinite(real)
    cv = lambda d: 1 - np.abs(np.mean(np.exp(1j * d)))
    if cv(real[ok] + v[ok]) < cv(real[ok] - v[ok]):
        v = -v
    return v


def binned_tuning(spikes, edges, ang_bins, mask, nbins=NBINS, sd=SMOOTH_SD, dt=None):
    """Tuning curves from binned time: each time bin has one angle (ang_bins), counts per bin;
    rate = counts over occupancy (bins x bin width), as the code's isomap tuning curves."""
    dt = dt or float(np.median(np.diff(edges)))
    C = bin_counts(spikes, edges)[mask]
    a = ang_bins[mask]
    ok = np.isfinite(a)
    b = np.round(np.mod(a[ok], 2 * np.pi) / (2 * np.pi) * nbins).astype(int) % nbins
    occ = np.bincount(b, minlength=nbins).astype(float)
    h = np.zeros((nbins, C.shape[1]))
    np.add.at(h, b, C[ok])
    with np.errstate(invalid="ignore", divide="ignore"):
        h = h / (occ[:, None] * dt)
    h[~np.isfinite(h)] = 0
    return smooth_circ(h, sd)


def poisson_glm_batch(y, m, Z, iters=100, tol=1e-8):
    """Poisson GLM with log link, y ~ 1 + m + Z[:, k], fitted for every column k of Z at once by
    Newton-Raphson (the model of glmfit(X, y, 'poisson') in GetGLM_Forward.m). Returns the
    coefficients (3, K), a mask of good fits and a mask of fits that only converged. A fit is bad, standing for glmfit's warnings
    on which the code removes a pair, when it does not converge within 100 iterations (glmfit's
    iteration limit) or when its IRLS weights are ill-conditioned, the smallest fitted mean
    below eps^(4/3) of the largest (glmfit warns when sqrt of a weight is below eps^(2/3) of
    the largest)."""
    n, K = Z.shape
    b = np.zeros((3, K))
    b[0] = np.log(max(y.mean(), 1e-9))
    ok = np.ones(K, bool)
    for it in range(iters):
        eta = b[0] + np.outer(m, np.ones(K)) * b[1] + Z * b[2]
        mu = np.exp(np.clip(eta, -50, 50))
        r = y[:, None] - mu
        g = np.stack([r.sum(0), (m[:, None] * r).sum(0), (Z * r).sum(0)])
        muz = mu * Z
        h00 = mu.sum(0); h01 = (m @ mu); h02 = muz.sum(0)
        h11 = (m ** 2) @ mu; h12 = m @ muz; h22 = (muz * Z).sum(0)
        Hm = np.array([[h00, h01, h02], [h01, h11, h12], [h02, h12, h22]]).transpose(2, 0, 1)
        try:
            step = np.linalg.solve(Hm, g.T[:, :, None])[:, :, 0].T
        except np.linalg.LinAlgError:
            step = np.full_like(b, np.nan)
        b = b + step
        if np.all(np.abs(step[:, np.isfinite(step).all(0)]) < tol):
            break
    conv = np.isfinite(b).all(0) & (np.abs(step) < 1e-6).all(0)
    eta = b[0] + np.outer(m, np.ones(K)) * b[1] + Z * b[2]
    with np.errstate(over="ignore", invalid="ignore"):
        lr = eta.min(0) - eta.max(0)  # log of smallest over largest fitted mean
    well = lr > (4 / 3) * np.log(np.finfo(float).eps)
    return b, ok & conv & well, ok & conv


def ccg_counts(ref, tgt, binsize=0.0002, nbins=250):
    """Spike counts of tgt at lags from ref (s), bins of binsize centred on multiples of it, from
    -nbins/2 to +nbins/2 bins (code: CrossCorr with 0.2 ms bins and 250 bins, converted back to
    counts in GetSpikeCrosscorrs)."""
    half = nbins // 2
    w = (half + 0.5) * binsize
    lo = np.searchsorted(tgt, ref - w)
    hi = np.searchsorted(tgt, ref + w)
    n = hi - lo
    if n.sum() == 0:
        return np.zeros(nbins + 1)
    idx = np.repeat(lo, n) + (np.arange(n.sum()) - np.repeat(np.cumsum(n) - n, n))
    d = tgt[idx] - np.repeat(ref, n)
    k = np.round(d / binsize).astype(int) + half
    k = k[(k >= 0) & (k <= nbins)]
    return np.bincount(k, minlength=nbins + 1).astype(float)


def _hollow_gauss(W=41, HF=0.6):
    sdg = W / 2
    if round(sdg) == sdg:
        N, cidx = int(6 * sdg + 1), int(sdg * 3)
    else:
        N, cidx = int(6 * sdg + 2), None
    x = np.arange(N) - (N - 1) / 2
    win = np.exp(-(x ** 2) / 2 / sdg ** 2)
    if cidx is None:
        # odd W: the code multiplies win(cidx) with a fractional cidx, which MATLAB rejects;
        # assumption: the two central samples are hollowed
        c = N // 2
        win[c - 1:c + 1] *= (1 - HF)
    else:
        win[cidx] *= (1 - HF)
    return win / win.sum()


def cch_pred(cch, W=41, HF=0.6):
    """Baseline prediction of a CCG by convolution with a partially hollowed Gaussian (code,
    cch_conv: window W bins, s.d. W/2 bins, hollow fraction 0.6, reflected edges, zero-phase)."""
    from scipy.ndimage import convolve1d
    return convolve1d(cch, _hollow_gauss(W, HF), mode="reflect")


def find_synapse_exc(cch, binsize_ms=0.2, syn_win=(0, 2), alpha=0.01, W=41, exc_sig_win=0.4):
    """Excitatory monosynaptic peak in one CCG (reference spikes at lag 0), as FindSynapse_Exc
    with the parameters of GetSynapticPairs.m: bins within syn_win (absolute lag) tested
    against the 1 - alpha quantile of a Poisson at the largest predicted count there; a peak
    needs exc_sig_win/binsize consecutive bins above. Returns (latency_neg, strZ_neg,
    latency_pos, strZ_pos, strR_pos): positive lags mean the reference cell leads."""
    from scipy import stats
    cch = np.round(cch)
    n = len(cch)
    b = binsize_ms * (np.arange(n) - n // 2)
    bix = (np.abs(b) <= syn_win[1]) & (np.abs(b) >= syn_win[0])
    bb = b[bix]
    pred = cch_pred(cch, W)
    pr = pred[bix]
    hi = stats.poisson.ppf(1 - alpha, pr.max())
    hib = cch[bix] > hi
    k = int(round(exc_sig_win / binsize_ms))
    sh = np.ones(len(hib) - k + 1, bool)
    for i in range(k):
        sh &= hib[i:len(hib) - k + 1 + i]
    out = [np.nan] * 5
    if not sh.any():
        return out
    sb = sh.copy()
    sb[1:] = np.diff(sh.astype(int)) == 1
    sb = list(np.where(sb)[0])
    bbs = bb[sb]
    if (bbs <= 0).sum() > 1:
        ix = np.where(bbs <= 0)[0]
        sb = sb[ix[-2] + 1:]
        bbs = bb[sb]
    if (bbs > 0).sum() > 1:
        ix = np.where(bbs > 0)[0]
        sb = sb[:ix[1]]
    vals = cch[bix]
    for s0 in sb:
        seg = vals[s0:s0 + k]
        pk = int(np.argmax(seg))
        pp = pr[s0 + pk]
        z = (seg[pk] - pp) / np.sqrt(pp)
        t = bb[s0 + pk]
        if t > 0:
            out[2], out[3], out[4] = t, z, seg[pk] / pp
        else:
            out[0], out[1] = -t, z
    return out
