"""Loading and measures for Peyrache et al. (2015) on DANDI:000056.

Every parameter says where it comes from: "criterion" (the claim's criterion in
claims/peyrache-2015.yaml, which cites the paper), "Methods" or another passage
of the paper (taken by the author, protocol step 1.6), "assumption" (a choice
the paper leaves open, with the reason), or "standard" (a detail that cannot
change a result).

Data are streamed from the archive with remfile and h5py; nothing is written to
disk.
"""
import numpy as np
import h5py
import remfile
import requests
from scipy import stats, optimize, signal
from scipy.ndimage import gaussian_filter1d

DANDISET = "000056"
VERSION = "0.261106.1949"
API = "https://api.dandiarchive.org/api"

ADN = "Anterodorsal nucleus"
POS = "Postsubiculum"

# Methods, Head direction cells: 1 degree bins, 6 degree s.d. smoothing.
NBINS = 360
SMOOTH_DEG = 6.0
# Methods, Head direction cells: kappa > 1, peak > 1 Hz, Rayleigh p < 0.001.
KAPPA_MIN, PEAK_MIN, RAYLEIGH_P = 1.0, 1.0, 1e-3
# Methods, Head direction cells, paragraph 2: 0.5 Hz in any of the three states.
RATE_MIN = 0.5
# Figure 3a legend: 300 ms bins in wake and REM, 50 ms in SWS.
CORR_BIN = {"wake": 0.3, "REM": 0.3, "SWS": 0.05}
# Methods, Bayesian reconstruction: 10 ms bins, 300 ms (wake, REM) and 50 ms
# (SWS) s.d. Gaussian smoothing.
DEC_BIN = 0.01
DEC_SMOOTH = {"wake": 0.3, "REM": 0.3, "SWS": 0.05}
STATES = ("wake", "SWS", "REM")


def _txt(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def list_assets():
    """Assets of the pinned version: list of (path, asset_id, size)."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        out += [(a["path"], a["asset_id"], a["size"]) for a in r["results"]]
        url = r.get("next")
    return sorted(out)


def open_asset(asset_id):
    url = f"{API}/assets/{asset_id}/download/"
    s3 = requests.head(url, allow_redirects=True, timeout=60).url
    return h5py.File(remfile.File(s3), "r")


def _intervals(g):
    lab = [_txt(x) for x in g["label"][:]] if "label" in g else None
    return lab, g["start_time"][:], g["stop_time"][:]


def load_session(asset_id, path):
    """Read one session's units, head direction, epochs and sleep states.

    The LFP is not read here (see lfp_window)."""
    f = open_asset(asset_id)
    s = {"path": path, "asset_id": asset_id}
    s["session"] = _txt(f["general/session_id"][()]) if "general/session_id" in f else path
    s["subject"] = _txt(f["general/subject/subject_id"][()])
    import re
    s["thal_depth"] = None
    if "general/devices/thalamic_probe" in f:
        m = re.search(r"session ([0-9.]+) mm", _txt(f["general/devices/thalamic_probe"].attrs.get("description", "")))
        s["thal_depth"] = round(float(m.group(1)), 3) if m else None
    u = f["units"]
    idx = u["spike_times_index"][:]
    st = u["spike_times"][:]
    starts = np.r_[0, idx[:-1]]
    s["spikes"] = [st[a:b] for a, b in zip(starts, idx)]
    n = len(idx)
    for k in ["region", "cell_type", "buzcode_region"]:
        s[k] = (np.array([_txt(x) for x in u[k][:]]) if k in u
                else np.array(["absent"] * n))
    for k in ["shank", "cluster_id", "in_lab_cell_list", "is_hd_cell", "hd_kappa",
              "hd_p_value", "hd_peak_rate", "hd_preferred_direction", "max_waveform_channel"]:
        s[k] = u[k][:] if k in u else np.full(n, np.nan)
    s["columns"] = sorted(u.keys())
    s["waveform"] = (u["buzcode_mean_waveform"][:] if "buzcode_mean_waveform" in u
                     else np.full((n, 32), np.nan))
    eg = u["electrode_group"][:]
    s["electrode_group"] = np.array([f[r].name.split("/")[-1] for r in eg])
    # location and description of each electrode group holding units, and
    # the devices, so that the data check can show where units were recorded
    s["group_info"] = {}
    for r in set(eg):
        g = f[r]
        s["group_info"][g.name.split("/")[-1]] = (_txt(g.attrs.get("location", "")),
                                                  _txt(g.attrs.get("description", "")))
    s["devices"] = sorted(f["general/devices"].keys()) if "general/devices" in f else []
    s["epochs"] = []
    if "intervals/epochs" in f:
        ep = f["intervals/epochs"]
        ti = ep["tags_index"][:]
        tags = [_txt(x) for x in ep["tags"][:]]
        s["epochs"] = [(tags[a:b], t0, t1) for a, b, t0, t1 in
                       zip(np.r_[0, ti[:-1]], ti, ep["start_time"][:], ep["stop_time"][:])]
    s["sub_recordings"] = []
    if "intervals/sub_recordings" in f:
        sr = f["intervals/sub_recordings"]
        s["sub_recordings"] = list(zip([_txt(x) for x in sr["file_name"][:]],
                                       sr["start_time"][:], sr["stop_time"][:]))
    b = f["processing/behavior"] if "processing/behavior" in f else {}
    s["states"] = {}
    if "sleep_states" in b:
        lab, t0, t1 = _intervals(b["sleep_states"])
        for k in STATES:
            m = np.array([l == k for l in lab])
            s["states"][k] = np.c_[t0[m], t1[m]]
    s["states_buzcode"] = {}
    if "sleep_states_buzcode" in b:
        lab, t0, t1 = _intervals(b["sleep_states_buzcode"])
        for k in set(lab):
            m = np.array([l == k for l in lab])
            s["states_buzcode"][k] = np.c_[t0[m], t1[m]]
    if "head_direction" in b:
        hd = b["head_direction/head_direction"]
        rate = hd["starting_time"].attrs["rate"]
        t0 = hd["starting_time"][()]
        a = hd["data"][:]
        s["hd_rate"] = float(rate)
        s["hd_t"] = t0 + np.arange(len(a)) / rate
        s["hd"] = a
        rl = b["position/red_led/data"][:]
        bl = b["position/blue_led/data"][:]
        s["led_angle"] = np.arctan2(rl[:, 1] - bl[:, 1], rl[:, 0] - bl[:, 0]) % (2 * np.pi)
        s["red_led"] = rl * 0.01  # metres (conversion attribute 0.01)
    else:
        s["hd"] = None
    s["lfp_shape"] = (f["processing/ecephys/LFP/lfp/data"].shape
                      if "processing/ecephys/LFP/lfp" in f else None)
    f.close()
    return s


# ---------------------------------------------------------------- intervals

def total(iv):
    return float(np.sum(iv[:, 1] - iv[:, 0])) if len(iv) else 0.0


def in_iv(t, iv):
    """Boolean mask of times t inside any interval of iv (n x 2, sorted)."""
    if len(iv) == 0:
        return np.zeros(len(t), bool)
    i = np.searchsorted(iv[:, 0], t, side="right") - 1
    ok = i >= 0
    out = np.zeros(len(t), bool)
    out[ok] = t[ok] < iv[i[ok], 1]
    return out


def restrict(sp, iv):
    return sp[in_iv(sp, iv)]


def bin_edges(iv, width):
    """Bin edges laid within each interval (partial bins dropped)."""
    out = []
    for a, b in iv:
        n = int((b - a) // width)
        if n >= 1:
            out.append(a + np.arange(n + 1) * width)
    return out


def bin_counts(sp, iv, width, edges=None):
    """Counts of the sorted spike train sp in bins of `width` laid within each
    interval (partial bins dropped). Returns counts and bin centres."""
    edges = bin_edges(iv, width) if edges is None else edges
    if not edges:
        return np.zeros(0), np.zeros(0)
    cs = [np.diff(np.searchsorted(sp, e)) for e in edges]
    cen = [0.5 * (e[1:] + e[:-1]) for e in edges]
    return np.concatenate(cs), np.concatenate(cen)


def bin_matrix(spikes, iv, width):
    e = bin_edges(iv, width)
    out = [bin_counts(sp, iv, width, e)[0] for sp in spikes]
    return np.array(out, dtype=float)


# ---------------------------------------------------------------- tuning

def wake_hd(s):
    """Head direction samples within wake, LED-detected frames only (Methods)."""
    w = s["states"]["wake"]
    m = in_iv(s["hd_t"], w) & np.isfinite(s["hd"])
    return s["hd_t"][m], s["hd"][m]


def spike_hd(sp, t, a, rate):
    """Head direction at each spike, nearest sample within half a frame; NaN
    where the nearest sample is not a valid wake sample."""
    if len(sp) == 0 or len(t) == 0:
        return np.zeros(0)
    i = np.clip(np.searchsorted(t, sp), 1, len(t) - 1)
    j = np.where(np.abs(t[i - 1] - sp) < np.abs(t[i] - sp), i - 1, i)
    ok = np.abs(t[j] - sp) <= 0.5 / rate + 1e-9
    return a[j[ok]]


def circ_smooth(x, sd_bins):
    return gaussian_filter1d(x, sd_bins, mode="wrap")


def tuning_curve(sp_hd, occ_counts, dt):
    """Rate per 1 degree bin: spike histogram over time histogram, both smoothed
    with the 6 degree s.d. Gaussian (Methods). Smoothing the two histograms
    before the ratio, so that empty 1 degree bins are defined, is a standard
    choice."""
    c, _ = np.histogram(sp_hd, NBINS, (0, 2 * np.pi))
    occ = circ_smooth(occ_counts * dt, SMOOTH_DEG)
    return circ_smooth(c.astype(float), SMOOTH_DEG) / np.maximum(occ, 1e-9)


def occupancy(a):
    return np.histogram(a, NBINS, (0, 2 * np.pi))[0].astype(float)


ANG = (np.arange(NBINS) + 0.5) * 2 * np.pi / NBINS


def a1inv(r):
    """Inverse of A1 (ML von Mises concentration from mean resultant length;
    Fisher 1993 approximation, as in the circular statistics toolbox)."""
    r = np.asarray(r, float)
    k = np.where(r < 0.53, 2 * r + r ** 3 + 5 * r ** 5 / 6,
                 np.where(r < 0.85, -0.4 + 1.39 * r + 0.43 / (1 - r + 1e-12),
                          1 / (r ** 3 - 4 * r ** 2 + 3 * r + 1e-12)))
    return k


def rayleigh_p(R, n):
    """Rayleigh test p-value (Zar 1999, as in the circular statistics toolbox)."""
    z = n * R ** 2
    p = np.exp(np.sqrt(1 + 4 * n + 4 * (n ** 2 - (n * R) ** 2)) - (1 + 2 * n))
    return float(min(max(p, 0.0), 1.0)) if n > 0 else 1.0


def vm_fit_a(tc, nspk):
    """Reading (hd-a): the tuning curve as a distribution of angles; ML von
    Mises (circular mean, kappa from resultant length); Rayleigh test with the
    resultant length of that distribution and n = spike count; peak rate is the
    tuning curve maximum."""
    w = tc / max(tc.sum(), 1e-12)
    z = np.sum(w * np.exp(1j * ANG))
    R = np.abs(z)
    return dict(pref=np.angle(z) % (2 * np.pi), kappa=float(a1inv(R)), peak=float(tc.max()),
                p=rayleigh_p(R, nspk), R=R)


def vm_fit_b(tc, sp_hd):
    """Reading (hd-b): least-squares fit of A exp(kappa (cos(x - mu) - 1)) to the
    tuning curve (A, the fitted peak rate); Rayleigh test on the head
    directions at spike times."""
    z = np.mean(np.exp(1j * sp_hd)) if len(sp_hd) else 0j
    R = np.abs(z)
    mu0 = ANG[np.argmax(tc)]
    def f(x, A, k, mu):
        return A * np.exp(k * (np.cos(x - mu) - 1))
    try:
        (A, k, mu), _ = optimize.curve_fit(f, ANG, tc, p0=[tc.max(), 2.0, mu0], maxfev=4000)
        if A < 0:
            A, k = -A, k
    except Exception:
        A, k, mu = np.nan, np.nan, mu0
    return dict(pref=mu % (2 * np.pi), kappa=float(k), peak=float(A), p=rayleigh_p(R, len(sp_hd)), R=R)


def is_hd(fit):
    return bool(fit["kappa"] > KAPPA_MIN and fit["peak"] > PEAK_MIN and fit["p"] < RAYLEIGH_P)


def n_peaks(tc):
    """Unimodality readings of supfig2a: (a) another local maximum of at least
    50% of the maximum; (b) such a maximum separated from the main one by a
    trough below 50% of the maximum (criterion)."""
    m = tc.max()
    loc = np.where((tc > np.roll(tc, 1)) & (tc >= np.roll(tc, -1)))[0]
    imax = int(np.argmax(tc))
    other = [i for i in loc if i != imax and tc[i] >= 0.5 * m]
    a = len(other) > 0
    b = False
    for i in other:
        # trough on the shorter arc and on the longer arc between i and imax
        lo, hi = sorted((i, imax))
        arc1 = tc[lo:hi + 1]
        arc2 = np.r_[tc[hi:], tc[:lo + 1]]
        if min(arc1.min(), arc2.min()) < 0.5 * m and max(arc1.min(), arc2.min()) >= 0 :
            # separated if either path down to the other peak dips below 50%
            if arc1.min() < 0.5 * m and arc2.min() < 0.5 * m:
                b = True
    return a, b


# ---------------------------------------------------------------- information

def segments(iv, n=10):
    """Split the union of intervals into n segments of equal duration
    (Methods, Information measures: 10 segments)."""
    d = iv[:, 1] - iv[:, 0]
    cum = np.r_[0, np.cumsum(d)]
    T = cum[-1]
    cuts = np.linspace(0, T, n + 1)
    def to_t(x):
        k = np.clip(np.searchsorted(cum, x, side="right") - 1, 0, len(d) - 1)
        return iv[k, 0] + (x - cum[k])
    segs = []
    for a, b in zip(cuts[:-1], cuts[1:]):
        ka = np.clip(np.searchsorted(cum, a, side="right") - 1, 0, len(d) - 1)
        kb = np.clip(np.searchsorted(cum, b, side="left") - 1, 0, len(d) - 1)
        parts = []
        for k in range(ka, kb + 1):
            lo = max(iv[k, 0], to_t(a)) if k == ka else iv[k, 0]
            hi = min(iv[k, 1], to_t(b)) if k == kb else iv[k, 1]
            if hi > lo:
                parts.append((lo, hi))
        segs.append(np.array(parts))
    return segs


def hd_information(sp, t, a, rate, nseg=10):
    """Cross-validated HD information in bits/spike (Methods, Information
    measures): for each of 10 segments of wake, the tuning curve of the other 9
    is read at the test head direction; L = sum log f(t_s) - int f dt against a
    homogeneous rate at the training mean; summed over test segments and
    divided by the number of spikes (bits). Head-direction frames are the time
    base (25.6 ms), the frame at each spike giving f(t_s)."""
    dt = 1.0 / rate
    seg_id = np.full(len(t), -1)
    T0, T1 = t[0], t[-1] + dt
    # segments over the valid wake frames, by equal frame counts
    seg_id = (np.arange(len(t)) * nseg) // len(t)
    i = np.clip(np.searchsorted(t, sp), 1, len(t) - 1)
    j = np.where(np.abs(t[i - 1] - sp) < np.abs(t[i] - sp), i - 1, i)
    ok = np.abs(t[j] - sp) <= 0.5 * dt + 1e-9
    j = j[ok]
    spk_frame = np.bincount(j, minlength=len(t)).astype(float)
    bins = np.minimum((a / (2 * np.pi) * NBINS).astype(int), NBINS - 1)
    L = 0.0
    nsp = 0
    for k in range(nseg):
        tr = seg_id != k
        te = ~tr
        occ = np.bincount(bins[tr], minlength=NBINS).astype(float) * dt
        cnt = np.bincount(bins[tr], weights=spk_frame[tr], minlength=NBINS)
        tc = circ_smooth(cnt, SMOOTH_DEG) / np.maximum(circ_smooth(occ, SMOOTH_DEG), 1e-9)
        mean_rate = cnt.sum() / occ.sum()
        f = np.maximum(tc[bins[te]], 1e-6)
        n = spk_frame[te]
        L += np.sum(n * np.log2(f)) - np.sum(f) * dt / np.log(2) \
            - (np.sum(n) * np.log2(max(mean_rate, 1e-6)) - mean_rate * te.sum() * dt / np.log(2))
        nsp += n.sum()
    return L / nsp if nsp > 0 else np.nan


# ---------------------------------------------------------------- decoding

def gauss_smooth_counts(C, sd_s, dt=DEC_BIN):
    return gaussian_filter1d(C, sd_s / dt, axis=-1, mode="constant")


def bayes_decode(C, tcs, dt, refine=False):
    """Bayesian decoding (Zhang et al. 1998, basic method with a flat prior):
    C (cells x bins) smoothed counts in a window of dt seconds, tcs (cells x
    360) waking tuning curves in Hz. Returns the decoded angle (maximum of the
    posterior) per bin. Processes bins in chunks to bound memory.

    With `refine`, also returns the maximum located below the 1 degree grid
    by a parabola through the log posterior at the best bin and its two
    neighbours (standard sub-bin interpolation), for the decoded speed of
    fig2e at 10 ms steps, which the 1 degree grid quantises to 100 deg/s."""
    tcs = np.maximum(tcs, 1e-3)
    logt = np.log(tcs)  # cells x 360
    s = tcs.sum(0) * dt  # 360
    out = np.empty(C.shape[1])
    fine = np.empty(C.shape[1]) if refine else None
    step = 20000
    for a in range(0, C.shape[1], step):
        ll = C[:, a:a + step].T @ logt - s  # bins x 360
        im = np.argmax(ll, axis=1)
        out[a:a + step] = ANG[im]
        if refine:
            r = np.arange(len(im))
            l0, lm, lp = ll[r, im], ll[r, (im - 1) % NBINS], ll[r, (im + 1) % NBINS]
            den = lm - 2 * l0 + lp
            d = np.where(den < 0, 0.5 * (lm - lp) / np.where(den < 0, den, -1.0), 0.0)
            fine[a:a + step] = (ANG[im] + np.clip(d, -0.5, 0.5) * 2 * np.pi / NBINS) % (2 * np.pi)
    return (out, fine) if refine else out


def circ_diff(a, b):
    return np.angle(np.exp(1j * (a - b)))


# ---------------------------------------------------------------- session rule

def thalamic_rule(sessions):
    """Methods, Recording sessions: "we discarded from analysis sessions
    separated by less than three days during which the thalamic probe was not
    moved". Applied per mouse in date order: a session is kept when the
    thalamic probe depth (device description, from the CRCNS session table)
    differs from that of the last kept session, or when it is at least three
    days after it. Returns {session: kept}."""
    import datetime as dt
    out = {}
    by = {}
    for name, depth in sessions:
        m, d = name.split("-")
        by.setdefault(m, []).append((dt.datetime.strptime(d, "%y%m%d"), depth, name))
    for m, L in by.items():
        last = None
        for date, depth, name in sorted(L):
            keep = (last is None or depth is None or last[1] is None or depth != last[1]
                    or (date - last[0]).days >= 3)
            out[name] = keep
            if keep:
                last = (date, depth)
    return out


# ---------------------------------------------------------------- waveforms

def waveform_features(w, fs=20000.0):
    """Supplementary Fig. 6 / Methods, Classification of PoS neurons: (i) total
    duration = 1 / frequency of maximum power of a wavelet transform of the
    mean waveform; (ii) trough-to-peak time. The wavelet (complex Morlet, 6
    cycles, power summed over the waveform, 200 to 4000 Hz) and the 4x cubic
    upsampling are standard choices. Returns (duration_ms, trough_to_peak_ms)."""
    from scipy.interpolate import CubicSpline
    if not np.all(np.isfinite(w)):
        return np.nan, np.nan
    w = w - np.median(w)
    if abs(w.min()) < abs(w.max()):
        w = -w  # trough-first polarity
    n = len(w)
    x = np.arange(n) / fs
    xx = np.linspace(0, x[-1], 4 * n)
    ww = CubicSpline(x, w)(xx)
    fs2 = 1 / (xx[1] - xx[0])
    it = int(np.argmin(ww))
    ip = it + int(np.argmax(ww[it:]))
    t2p = (ip - it) / fs2 * 1e3
    freqs = np.linspace(200, 4000, 200)
    wpad = np.r_[np.zeros(len(ww)), ww, np.zeros(len(ww))]
    tt = (np.arange(len(wpad)) - len(wpad) / 2) / fs2
    pw = []
    for fr in freqs:
        sd = 6 / (2 * np.pi * fr)
        mw = np.exp(2j * np.pi * fr * tt) * np.exp(-tt ** 2 / (2 * sd ** 2))
        mw /= np.sqrt(np.sum(np.abs(mw) ** 2))
        c = np.convolve(wpad, mw, mode="same")
        pw.append(np.sum(np.abs(c) ** 2))
    fmax = freqs[int(np.argmax(pw))]
    return 1e3 / fmax, t2p


def pos_class(dur, t2p):
    """Methods: interneuron for duration < 0.9 ms and trough-to-peak < 0.42 ms;
    pyramidal for duration > 0.95 ms and trough-to-peak > 0.42 ms."""
    if dur < 0.9 and t2p < 0.42:
        return "int"
    if dur > 0.95 and t2p > 0.42:
        return "pyr"
    return "und"


# ---------------------------------------------------------------- correlograms

def ccg_counts(a, b, width, half):
    """Cross-correlogram of spike trains a (reference) and b: counts of b
    spikes at lags (b - a) in bins of `width` from -half to +half (bin centred
    on 0). Exact, by sorted search."""
    nb = int(round(half / width))
    edges = (np.arange(-nb, nb + 2) - 0.5) * width
    lo = np.searchsorted(b, a + edges[0])
    hi = np.searchsorted(b, a + edges[-1])
    cnt = hi - lo
    tot = int(cnt.sum())
    out = np.zeros(len(edges) - 1)
    if tot == 0:
        return out, 0.5 * (edges[1:] + edges[:-1])
    # chunk over reference spikes to bound memory
    step = max(1, int(2e7 // max(1, cnt.mean() + 1)))
    for s0 in range(0, len(a), step):
        lo_, hi_, a_ = lo[s0:s0 + step], hi[s0:s0 + step], a[s0:s0 + step]
        c_ = hi_ - lo_
        if c_.sum() == 0:
            continue
        rep = np.repeat(np.arange(len(a_)), c_)
        off = np.arange(c_.sum()) - np.repeat(np.cumsum(c_) - c_, c_)
        d = b[np.repeat(lo_, c_) + off] - a_[rep]
        out += np.histogram(d, edges)[0]
    return out, 0.5 * (edges[1:] + edges[:-1])


def mono_test(c, width, sd=0.01, hollow=False, pct=0.999, lag=(0.001, 0.01)):
    """Methods, Detection of mono-synaptic connections: CCG in 0.5 ms bins
    convolved with a 10 ms s.d. Gaussian as the baseline; bins above the 99.9th
    percentile of the Poisson distribution at the baseline; a connection when
    at least two consecutive bins pass at lags of 1 to 10 ms. Returns
    (excitatory at positive lags, at negative lags). `hollow` leaves the
    central bin out of the convolution (reading m-b, after ref 58)."""
    n = len(c)
    sdb = sd / width
    half = int(4 * sdb)
    k = np.exp(-0.5 * (np.arange(-half, half + 1) / sdb) ** 2)
    if hollow:
        k[half] = 0.0
    k /= k.sum()
    base = np.convolve(np.r_[c[half:0:-1], c, c[-2:-half - 2:-1]], k, mode="valid")
    thr = stats.poisson.ppf(pct, np.maximum(base, 1e-12))
    sig = c > thr
    mid = n // 2
    lags = (np.arange(n) - mid) * width
    def run(mask):
        m = mask.astype(int)
        return bool(np.any(m[:-1] & m[1:]))
    pos = (lags >= lag[0] - 1e-12) & (lags <= lag[1] + 1e-12)
    neg = (lags <= -lag[0] + 1e-12) & (lags >= -lag[1] - 1e-12)
    return run(np.where(pos, sig, False)), run(np.where(neg, sig, False))


def ang_corr(h1, h2):
    """Angular correlation of two tuning curves as a function of offset,
    normalised so that 1 is chance (Supplementary Fig. 4): rho(d) =
    mean(h1(x) h2(x + d)) / (mean h1 mean h2), for d in 1 degree steps."""
    F = np.fft.ifft(np.conj(np.fft.fft(h1)) * np.fft.fft(h2)).real / len(h1)
    return F / (h1.mean() * h2.mean())


_CHI_Q = stats.chi2.ppf((np.arange(200) + 0.5) / 200, 3) / 3.0  # speeds / mean speed


def expected_ccg(rho, lags, v):
    """Expected CCG at lags (s) for mean speed v (rad/s): the mean over a
    chi-squared (3 d.f.) speed distribution scaled to mean v of the angular
    correlation at offset speed x lag, averaged over the two turning directions
    (Methods, Estimation of angular velocity)."""
    th = np.abs(v) * _CHI_Q[None, :] * lags[:, None]  # rad
    idx = (np.round(np.degrees(th)).astype(int)) % NBINS
    r = 0.5 * (rho[idx] + rho[(-idx) % NBINS])
    return r.mean(1)


def fit_speed(rho, lags, ccg, with_residual=False):
    """Mean angular speed (rad/s) minimising the squared difference between
    the expected and observed CCG: coarse grid, then Nelder-Mead (Methods).
    With `with_residual`, also the residual sum of squares over the sum of
    squares of the CCG about its mean (fit quality; 0 is a perfect fit)."""
    grid = np.radians(np.geomspace(5, 5000, 80))
    cost = [np.sum((expected_ccg(rho, lags, v) - ccg) ** 2) for v in grid]
    v0 = grid[int(np.argmin(cost))]
    res = optimize.minimize(lambda x: np.sum((expected_ccg(rho, lags, abs(x[0])) - ccg) ** 2),
                            [v0], method="Nelder-Mead", options=dict(xatol=1e-4, fatol=1e-10))
    v = abs(float(res.x[0]))
    if not with_residual:
        return v
    ss = np.sum((ccg - ccg.mean()) ** 2)
    return v, float(res.fun / ss) if ss > 0 else np.nan


# ---------------------------------------------------------------- per session

def state_iv(s, k):
    return s["states"].get(k, np.zeros((0, 2)))


def _xcorr_lags(x, y, maxlag):
    """sum_t x(t) y(t + lag) / N for lag in -maxlag..maxlag bins (FFT)."""
    n = len(x)
    L = 1 << int(np.ceil(np.log2(2 * n + 1)))
    F = np.fft.irfft(np.conj(np.fft.rfft(x, L)) * np.fft.rfft(y, L), L)
    out = np.r_[F[-maxlag:], F[:maxlag + 1]] / n
    return out


def morlet_power(z, width, freqs, ncyc=5):
    """Mean power over lags of a complex Morlet transform of a correlogram
    (fig6a, reading o-c: complex Morlet, a standard choice)."""
    t = (np.arange(len(z)) - len(z) // 2) * width
    out = []
    for fr in freqs:
        sd = ncyc / (2 * np.pi * fr)
        w = np.exp(2j * np.pi * fr * t) * np.exp(-t ** 2 / (2 * sd ** 2))
        w /= np.sum(np.abs(w))
        c = np.convolve(z, w, mode="same")
        m = np.abs(t) <= 0.025
        out.append(np.mean(np.abs(c[m]) ** 2))
    return np.array(out)


FAST_FREQS = np.arange(50, 301, 5.0)
OLE_WINDOWS = np.array([0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.5, 1.0])


def analyze_session(s, parts=("cells", "pairs", "decode", "fast", "mono", "lfp")):
    """All per-session measures. Returns dict of lists of records."""
    out = {"cells": [], "pairs": [], "ens": [], "fast": [], "mono": [], "dec5b": [], "glm": [], "lfp": [],
           "summary": session_summary(s), "shift": {}}
    if s.get("hd") is not None and "wake" not in s["states"]:
        # No sleep scoring in the file: the open-field epoch is the paper's wake
        # (epochs table description); such sessions enter wake analyses only.
        of = np.array([(a, b) for tg, a, b in s["epochs"] if "open_field" in tg])
        if len(of):
            s["states"]["wake"] = of
    name = s["path"].split("_ses-")[1].split("_")[0]
    if s.get("hd") is None or "wake" not in s["states"]:
        # Connection detection needs no head direction (fig7, all ADn by all
        # PoS pairs), so it runs here too.
        if "mono" in parts:
            out["mono"] = mono_session(s, name, list(np.where(s["region"] == ADN)[0]),
                                       list(np.where(s["region"] == POS)[0]))
        return out
    keep = np.where(np.isin(s["region"], [ADN, POS]))[0]
    t, a = wake_hd(s)
    rate = s["hd_rate"]
    dt = 1.0 / rate
    occ = occupancy(a)
    W = s["states"]["wake"]
    has_sleep = len(state_iv(s, "SWS")) > 0 and len(state_iv(s, "REM")) > 0
    cells = []
    tcs = {}
    for u in keep:
        sp = s["spikes"][u]
        rec = dict(session=name, subject=s["subject"], unit=int(u), region="ADn" if s["region"][u] == ADN else "PoS",
                   shank=int(s["shank"][u]), lab_hd=bool(s["is_hd_cell"][u]) if np.isfinite(s["is_hd_cell"][u]) else None,
                   lab_pref=float(s["hd_preferred_direction"][u]))
        for k in STATES:
            iv = state_iv(s, k)
            rec["rate_" + k] = len(restrict(sp, iv)) / total(iv) if total(iv) > 0 else np.nan
        sh = spike_hd(restrict(sp, W), t, a, rate)
        tc = tuning_curve(sh, occ, dt)
        tcs[u] = tc
        fa, fb = vm_fit_a(tc, len(sh)), vm_fit_b(tc, sh)
        for nm, fz in (("a", fa), ("b", fb)):
            rec.update({f"pref_{nm}": fz["pref"], f"kappa_{nm}": fz["kappa"], f"peak_{nm}": fz["peak"],
                        f"p_{nm}": fz["p"], f"hd_{nm}": is_hd(fz)})
        rec["unimodal_fail_a"], rec["unimodal_fail_b"] = n_peaks(tc)
        rec["nspk_wake"] = len(sh)
        if "cells" in parts:
            rec["info"] = hd_information(restrict(sp, W), t, a, rate)
        d, tp = waveform_features(s["waveform"][u])
        rec["dur_ms"], rec["t2p_ms"] = d, tp
        rec["cls"] = pos_class(d, tp) if np.isfinite(d) else "und"
        rec["has_sleep"] = has_sleep
        rec["pass_rate_a"] = bool(all(np.isfinite(rec["rate_" + k]) and rec["rate_" + k] >= RATE_MIN for k in STATES))
        rec["pass_rate_b"] = bool(any(np.isfinite(rec["rate_" + k]) and rec["rate_" + k] >= RATE_MIN for k in STATES))
        cells.append(rec)
    out["cells"] = cells
    if not cells:
        return out
    U = [c["unit"] for c in cells]
    R = {c["unit"]: c for c in cells}
    # ---------------- pairs: binned correlations, speeds, noise correlations
    if "pairs" in parts:
        corr_bins = {}
        for k in STATES:
            iv = state_iv(s, k)
            corr_bins[k] = bin_matrix([s["spikes"][u] for u in U], iv, CORR_BIN[k]) if total(iv) > 0 else None
        cc = {}
        for k in STATES:
            M = corr_bins[k]
            if M is None or M.shape[1] < 10:
                cc[k] = None
                continue
            with np.errstate(invalid="ignore", divide="ignore"):
                cc[k] = np.corrcoef(M)
        # 10 ms counts per state for the speed CCGs
        c10 = {}
        for k in STATES:
            iv = state_iv(s, k)
            c10[k] = bin_matrix([s["spikes"][u] for u in U], iv, 0.01) if total(iv) > 0 else None
        # noise correlations, wake: 10 ms bins with valid head direction
        wb, wcen = bin_counts(np.zeros(0), W, 0.01)
        i = np.clip(np.searchsorted(s["hd_t"], wcen), 1, len(s["hd_t"]) - 1)
        j = np.where(np.abs(s["hd_t"][i - 1] - wcen) < np.abs(s["hd_t"][i] - wcen), i - 1, i)
        th = s["hd"][j]
        okb = np.isfinite(th)
        Xw = c10["wake"][:, okb] / 0.01
        thb = np.minimum((th[okb] / (2 * np.pi) * NBINS).astype(int), NBINS - 1)
        Fw = np.array([tcs[u][thb] for u in U])
        mlag = 5  # -50..+50 ms in 10 ms bins (Methods)
        hdu = [ii for ii, u in enumerate(U) if R[u]["hd_a"] or R[u]["hd_b"]]
        nW = Xw.shape[1]
        LW = 1 << int(np.ceil(np.log2(2 * nW + 1)))
        FX = np.fft.rfft(Xw, LW, axis=1)
        FF = np.fft.rfft(Fw, LW, axis=1)
        def xc(A, B, ml, n, L):
            F = np.fft.irfft(np.conj(A) * B, L)
            return np.r_[F[-ml:], F[:ml + 1]] / n
        FC = {}
        for k in STATES:
            X = c10[k]
            if X is None:
                continue
            Lk = 1 << int(np.ceil(np.log2(2 * X.shape[1] + 1)))
            FC[k] = (np.fft.rfft(X[hdu], Lk, axis=1), Lk, X.shape[1], {u: q for q, u in enumerate(hdu)})
        lagsec = {"wake": 2.0, "REM": 2.0, "SWS": 0.5}  # reading v-a
        for ii in range(len(U)):
            for jj in range(ii + 1, len(U)):
                ui, uj = U[ii], U[jj]
                ci, cj = R[ui], R[uj]
                rec = dict(session=name, subject=s["subject"], u1=ui, u2=uj,
                           kind="-".join(sorted([ci["region"], cj["region"]])),
                           same_shank=ci["shank"] == cj["shank"])
                for k in STATES:
                    rec["corr_" + k] = float(cc[k][ii, jj]) if cc[k] is not None else np.nan
                cs = xc(FX[ii], FX[jj], mlag, nW, LW)
                cf = xc(FF[ii], FF[jj], mlag, nW, LW)
                mi, mj = Xw[ii].mean(), Xw[jj].mean()
                nz = cs - cf
                rec["noise_avg_raw"] = float(nz.mean())
                rec["noise_0_raw"] = float(nz[mlag])
                rec["noise_avg_norm"] = float(nz.mean() / (mi * mj)) if mi * mj > 0 else np.nan
                rec["noise_0_norm"] = float(nz[mlag] / (mi * mj)) if mi * mj > 0 else np.nan
                if ii in hdu and jj in hdu and ci["region"] == cj["region"]:
                    rho = ang_corr(tcs[ui], tcs[uj])
                    for k in STATES:
                        X = c10[k]
                        if X is None or X[ii].sum() == 0 or X[jj].sum() == 0:
                            rec["v_" + k] = np.nan
                            continue
                        ml = int(round(lagsec[k] / 0.01))
                        Fk, Lk, nk, pos_ = FC[k]
                        cg = xc(Fk[pos_[ii]], Fk[pos_[jj]], ml, nk, Lk) / (X[ii].mean() * X[jj].mean())
                        lags = np.arange(-ml, ml + 1) * 0.01
                        v_, res_ = fit_speed(rho, lags, cg, with_residual=True)
                        rec["v_" + k], rec["res_" + k] = np.degrees(v_), res_
                out["pairs"].append(rec)
        del c10, corr_bins, Xw, Fw, FX, FF, FC
    # ---------------- decoding per structure
    if "decode" in parts:
        out["ens"], out["dec5b"] = decode_session(s, name, cells, tcs, t, a)
        out["shift"] = shifted_decoding(s, cells, tcs)
    # ---------------- fast synchrony (ADn HD pairs) per state
    if "fast" in parts:
        adn_hd = [u for u in U if R[u]["region"] == "ADn" and (R[u]["hd_a"] or R[u]["hd_b"])]
        w = 0.0005
        for k in STATES:
            iv = state_iv(s, k)
            if total(iv) == 0:
                continue
            sps = {u: restrict(s["spikes"][u], iv) for u in adn_hd}
            for x in range(len(adn_hd)):
                for y in range(x + 1, len(adn_hd)):
                    ux, uy = adn_hd[x], adn_hd[y]
                    c, lags = ccg_counts(sps[ux], sps[uy], w, 0.07)
                    nbox = int(round(0.01 / w))
                    box = np.ones(2 * nbox + 1) / (2 * nbox + 1)
                    m = np.convolve(c, box, mode="same")
                    sel = np.abs(lags) <= 0.05 + 1e-9
                    z = (c - m) / np.sqrt(np.maximum(m, 1e-9))
                    z = z[sel]
                    lg = lags[sel]
                    out["fast"].append(dict(session=name, subject=s["subject"], u1=ux, u2uy=uy, u2=uy, state=k,
                                            same_shank=R[ux]["shank"] == R[uy]["shank"],
                                            zpeak5=float(z[np.abs(lg) <= 0.005].max()),
                                            z0=float(z[np.argmin(np.abs(lg))]),
                                            power=morlet_power(z, w, FAST_FREQS),
                                            nspk=(len(sps[ux]), len(sps[uy]))))
    # ---------------- monosynaptic, ADn x PoS (whole recording)
    if "mono" in parts:
        out["mono"] = mono_session(s, name, [u for u in U if R[u]["region"] == "ADn"],
                                   [u for u in U if R[u]["region"] == "PoS"])
    if "glm" in parts:
        out["glm"] = glm_session(s, cells)
    if "glm_dense" in parts:
        out["glm"] = glm_session(s, cells, GLM_WINDOWS_DENSE, (("PoS", "ADn"),))
    if "lfp" in parts and s.get("lfp_shape") is not None:
        out["lfp"] = lfp_session(s, cells)
    return out


def mono_session(s, name, adn, pos):
    """Monosynaptic tests (mono_test) for every ADn by PoS pair of a session,
    cross-correlograms over the whole recording, all states."""
    out = []
    w = 0.0005
    for ua in adn:
        for up in pos:
            c, lags = ccg_counts(s["spikes"][ua], s["spikes"][up], w, 0.06)
            rec = dict(session=name, subject=s["subject"], adn=int(ua), pos=int(up))
            for hol in (False, True):
                f, b = mono_test(c, w, hollow=hol)
                rec[f"a2p_{'h' if hol else 'c'}"] = f
                rec[f"p2a_{'h' if hol else 'c'}"] = b
            # jittered baseline (m-d): expectation of the CCG with one train
            # jittered uniformly by +-10 ms is the CCG convolved with a 20 ms box
            nbox = int(round(0.01 / w))
            base = np.convolve(c, np.ones(2 * nbox + 1) / (2 * nbox + 1), mode="same")
            thr = stats.poisson.ppf(0.999, np.maximum(base, 1e-12))
            sig = c > thr
            pz = (lags >= 0.001 - 1e-9) & (lags <= 0.01 + 1e-9)
            nz_ = (lags <= -0.001 + 1e-9) & (lags >= -0.01 - 1e-9)
            run = lambda m_: bool(np.any(m_[:-1] & m_[1:]))
            rec["a2p_j"] = run(np.where(pz, sig, False))
            rec["p2a_j"] = run(np.where(nz_, sig, False))
            out.append(rec)
    return out


def _hd_at(s, cen):
    i = np.clip(np.searchsorted(s["hd_t"], cen), 1, len(s["hd_t"]) - 1)
    j = np.where(np.abs(s["hd_t"][i - 1] - cen) < np.abs(s["hd_t"][i] - cen), i - 1, i)
    return s["hd"][j]


def _tc_from_bins(C, thb, dtb):
    occ = np.bincount(thb, minlength=NBINS).astype(float) * dtb
    out = []
    for c in C:
        cnt = np.bincount(thb, weights=c, minlength=NBINS)
        out.append(circ_smooth(cnt, SMOOTH_DEG) / np.maximum(circ_smooth(occ, SMOOTH_DEG), 1e-9))
    return np.array(out)


def ole_fit(Rtr, thtr, Ftr=None, diag="observed"):
    """Optimal linear estimator (Salinas and Abbott 1994): D = Q^-1 L with
    L = <r e^{i theta}> and Q = <r r^T> (cov) or, when F (the tuning curves
    read at the head direction, smoothed as r) is given, a signal reading:
    diag="observed", Q = <F F^T> off the diagonal with the diagonal of
    <r r^T> (independent neurons with the observed variances; assumption);
    diag="signal", Q = <F F^T> throughout (the plain reading of "tuning curve
    covariances"). Returns complex weights."""
    n = Rtr.shape[1]
    L = Rtr.T @ np.exp(1j * thtr) / n
    Q = Rtr.T @ Rtr / n
    if Ftr is not None:
        Qs = Ftr.T @ Ftr / n
        if diag == "observed":
            np.fill_diagonal(Qs, np.diag(Q))
        Q = Qs
    return np.linalg.solve(Q + 1e-9 * np.eye(len(Q)), L)


def decode_session(s, name, cells, tcs, t, a):
    ens, dec5b = [], []
    W = s["states"]["wake"]
    R = {c["unit"]: c for c in cells}
    groups = {}
    for reg in ("ADn", "PoS"):
        groups[reg] = [c["unit"] for c in cells if c["region"] == reg and c["hd_a"]]
    for reg, hu in groups.items():
        if len(hu) < 6:
            continue
        TC = np.array([tcs[u] for u in hu])
        e = dict(session=name, subject=s["subject"], region=reg, n_hd=len(hu))
        dec = {}
        for k in STATES:
            iv = state_iv(s, k)
            if total(iv) == 0:
                continue
            C = bin_matrix([s["spikes"][u] for u in hu], iv, DEC_BIN)
            _, cen = bin_counts(np.zeros(0), iv, DEC_BIN)
            Cs = gauss_smooth_counts(C, DEC_SMOOTH[k])
            ang, angf = bayes_decode(Cs, TC, DEC_BIN, refine=True)
            dec[k] = (ang, cen, C)
            # steps within one interval of the state only
            ivid = np.searchsorted(iv[:, 0], cen, side="right") - 1
            same = ivid[1:] == ivid[:-1]
            sp_a = np.abs(circ_diff(ang[1:], ang[:-1]))[same] / DEC_BIN
            sp_af = np.abs(circ_diff(angf[1:], angf[:-1]))[same] / DEC_BIN
            ksub = int(round(DEC_SMOOTH[k] / DEC_BIN))
            sub, subid = ang[::ksub], ivid[::ksub]
            sp_b = np.abs(circ_diff(sub[1:], sub[:-1]))[subid[1:] == subid[:-1]] / (ksub * DEC_BIN)
            e[f"speed_a_{k}"] = float(np.degrees(np.median(sp_a)))
            e[f"speed_af_{k}"] = float(np.degrees(np.median(sp_af)))
            e[f"speed_afmean_{k}"] = float(np.degrees(np.mean(sp_af)))
            e[f"speed_b_{k}"] = float(np.degrees(np.median(sp_b)))
            e[f"speed_bmean_{k}"] = float(np.degrees(np.mean(sp_b)))
            if k == "wake":
                th = _hd_at(s, cen)
                ok = np.isfinite(th)
                e["err_full"] = float(np.degrees(np.median(np.abs(circ_diff(ang[ok], th[ok])))))
                # 10-segment cross-validation
                idx = np.where(ok)[0]
                seg = (np.arange(len(idx)) * 10) // len(idx)
                thb = np.minimum((th[idx] / (2 * np.pi) * NBINS).astype(int), NBINS - 1)
                errs = []
                for q in range(10):
                    tr, te = idx[seg != q], idx[seg == q]
                    tcq = _tc_from_bins(C[:, tr], thb[seg != q], DEC_BIN)
                    aq = bayes_decode(Cs[:, te], tcq, DEC_BIN)
                    errs.append(np.abs(circ_diff(aq, th[te])))
                e["err_cv"] = float(np.degrees(np.median(np.concatenate(errs))))
                # actual head speed (w-b): frames, and over ~300 ms
                ah = a
                da = np.abs(circ_diff(ah[1:], ah[:-1])) * s["hd_rate"]
                gap = np.diff(t) < 1.5 / s["hd_rate"]
                e["speed_a_actual"] = float(np.degrees(np.median(da[gap])))
                e["speed_afmean_actual"] = float(np.degrees(np.mean(da[gap])))
                kk = int(round(0.3 * s["hd_rate"]))
                db = np.abs(circ_diff(ah[kk:], ah[:-kk])) / (t[kk:] - t[:-kk])
                gb = (t[kk:] - t[:-kk]) < (kk + 0.5) / s["hd_rate"]
                e["speed_b_actual"] = float(np.degrees(np.median(db[gb])))
                e["speed_bmean_actual"] = float(np.degrees(np.mean(db[gb])))
                e.update(ole_errors(C, TC, th, idx, seg, thb))
        e["coherence"] = coherence(s, TC, hu, dec) if "wake" in dec else {}
        ens.append(e)
        # fig5b: tuning curves of the other structure's HD cells against decoded HD
        other = "PoS" if reg == "ADn" else "ADn"
        targets = [c["unit"] for c in cells if c["region"] == other and (c["hd_a"] or c["hd_b"])]
        for k, (ang, cen, _) in dec.items():
            iv = state_iv(s, k)
            T = bin_matrix([s["spikes"][u] for u in targets], iv, DEC_BIN) if targets else None
            ab = np.minimum((ang / (2 * np.pi) * NBINS).astype(int), NBINS - 1)
            ksub = int(round(DEC_SMOOTH[k] / DEC_BIN))
            nfull = (len(ab) // ksub) * ksub
            ab_b = ab[:nfull:ksub]
            for ti, u in enumerate(targets):
                tca = _tc_from_bins(T[ti:ti + 1], ab, DEC_BIN)[0]
                Tb = T[ti, :nfull].reshape(-1, ksub).sum(1)
                tcb = _tc_from_bins(Tb[None], ab_b, DEC_BIN * ksub)[0]
                dec5b.append(dict(session=name, subject=s["subject"], decoder=reg, target=u,
                                  target_region=other, state=k, hd_a=R[u]["hd_a"], hd_b=R[u]["hd_b"],
                                  r_a=float(np.corrcoef(tca, tcs[u])[0, 1]),
                                  r_b=float(np.corrcoef(tcb, tcs[u])[0, 1])))
    # Ensembles of HD cells under (hd-b), waking decoding only (decoding-tracks-hd,
    # fig4d,e), asked for by the round-2 verifier.
    for e in ens:
        e["reading"] = "hd-a"
    for reg in ("ADn", "PoS"):
        hb = [c["unit"] for c in cells if c["region"] == reg and c["hd_b"]]
        if len(hb) >= 6:
            eb_ = wake_ensemble(s, name, hb, tcs, reg)
            eb_["reading"] = "hd-b"
            ens.append(eb_)
    return ens, dec5b


def ole_errors(C, TC, th, idx, seg, thb):
    """fig4d,e: cross-validated waking median absolute error (degrees) of the
    covariance OLE, the two signal OLE readings (ole_fit) and the Bayesian
    decoder, per smoothing window of OLE_WINDOWS. C, 10 ms waking counts of
    the ensemble; TC, its tuning curves; th,
    head direction per bin; idx, bins with a valid head direction; seg, the
    10 segments of idx; thb, the 1 degree bin of th[idx]."""
    e = {}
    for wdw in OLE_WINDOWS:
        Cw = gauss_smooth_counts(C, wdw)[:, idx]
        Fw = gauss_smooth_counts(TC[:, np.minimum((np.nan_to_num(th) / (2 * np.pi) * NBINS).astype(int), NBINS - 1)] * DEC_BIN, wdw)[:, idx]
        eo, es, es2, eb = [], [], [], []
        for q in range(10):
            tr, te = seg != q, seg == q
            Dc = ole_fit(Cw[:, tr].T, th[idx][tr])
            Ds = ole_fit(Cw[:, tr].T, th[idx][tr], Fw[:, tr].T)
            Ds2 = ole_fit(Cw[:, tr].T, th[idx][tr], Fw[:, tr].T, diag="signal")
            thq = th[idx][te]
            eo.append(np.abs(circ_diff(np.angle(Cw[:, te].T @ Dc), thq)))
            es.append(np.abs(circ_diff(np.angle(Cw[:, te].T @ Ds), thq)))
            es2.append(np.abs(circ_diff(np.angle(Cw[:, te].T @ Ds2), thq)))
            tcq = _tc_from_bins(C[:, idx[tr]], thb[tr], DEC_BIN)
            eb.append(np.abs(circ_diff(bayes_decode(Cw[:, te], tcq, DEC_BIN), thq)))
        e[f"ole_cov_{wdw}"] = float(np.degrees(np.median(np.concatenate(eo))))
        e[f"ole_sig_{wdw}"] = float(np.degrees(np.median(np.concatenate(es))))
        e[f"ole_sig2_{wdw}"] = float(np.degrees(np.median(np.concatenate(es2))))
        e[f"bayes_{wdw}"] = float(np.degrees(np.median(np.concatenate(eb))))
    return e


def wake_ensemble(s, name, hu, tcs, region):
    """Waking decoding of one ensemble (decoding-tracks-hd, fig4d,e) without
    the sleep measures: used for the ensembles of HD cells under (hd-b),
    asked for by the round-2 verifier. Same steps as decode_session."""
    W = s["states"]["wake"]
    TC = np.array([tcs[u] for u in hu])
    e = dict(session=name, subject=s["subject"], region=region, n_hd=len(hu))
    C = bin_matrix([s["spikes"][u] for u in hu], W, DEC_BIN)
    _, cen = bin_counts(np.zeros(0), W, DEC_BIN)
    Cs = gauss_smooth_counts(C, DEC_SMOOTH["wake"])
    ang = bayes_decode(Cs, TC, DEC_BIN)
    th = _hd_at(s, cen)
    ok = np.isfinite(th)
    e["err_full"] = float(np.degrees(np.median(np.abs(circ_diff(ang[ok], th[ok])))))
    idx = np.where(ok)[0]
    seg = (np.arange(len(idx)) * 10) // len(idx)
    thb = np.minimum((th[idx] / (2 * np.pi) * NBINS).astype(int), NBINS - 1)
    errs = []
    for q in range(10):
        tr, te = idx[seg != q], idx[seg == q]
        tcq = _tc_from_bins(C[:, tr], thb[seg != q], DEC_BIN)
        errs.append(np.abs(circ_diff(bayes_decode(Cs[:, te], tcq, DEC_BIN), th[te])))
    e["err_cv"] = float(np.degrees(np.median(np.concatenate(errs))))
    e.update(ole_errors(C, TC, th, idx, seg, thb))
    return e


# ---------------------------------------------------------------- GLM (fig5d,e)

# Readout windows (reading g-d): 10 to 1000 ms on a log scale, 7 windows, for
# the best-window information of fig5d and fig5e-adn-predicts-pos.
GLM_WINDOWS = np.geomspace(0.01, 1.0, 7)
# fig5e-readout-windows (criterion): at least 20 windows per decade near 50 to
# 200 ms. Gaussian s.d. from 10^-1.7 (20 ms) to 10^-0.6 (251 ms) at 20 per
# decade, so that both the s.d. reading (a) and the full width reading (b,
# FWHM = 2.355 s.d.; 50 to 200 ms FWHM is 21 to 85 ms s.d.) are inside the
# dense part, with 10, 500 and 1000 ms outside it (standard choice for the
# ends). Run for PoS targets of ADn assemblies only, the claim's direction.
GLM_WINDOWS_DENSE = np.r_[0.01, 10 ** np.arange(-1.7, -0.6 + 1e-9, 0.05), 0.5, 1.0]
GLM_MAX_S = 1200.0  # at most the first 20 min of each state (time limit; deviation)


def _g(x):
    """Modified exponential link (Methods; ref 36): exp(x) below 0, 1 + x above."""
    return np.where(x < 0, np.exp(np.minimum(x, 0)), 1 + np.maximum(x, 0))


def _glm_fit(X, y, w0=None, iters=15, tol=1e-5):
    """Poisson maximum likelihood with the link _g, by Newton's method. The
    log-likelihood is concave (g convex and log-concave), so its maximum is
    the one the Methods' derivative-free search finds."""
    p = X.shape[1]
    w = np.zeros(p) if w0 is None else w0.copy()
    if w0 is None:
        w[0] = np.log(max(y.mean(), 1e-6))
    for _ in range(iters):
        x = X @ w
        g = _g(x)
        g1 = np.where(x < 0, g, 1.0)
        g2 = np.where(x < 0, g, 0.0)
        a = y / np.maximum(g, 1e-12)
        grad = X.T @ (a * g1 - g1)
        hw = a * (g2 - g1 ** 2 / np.maximum(g, 1e-12)) - g2
        H = (X * hw[:, None]).T @ X - 1e-6 * np.eye(p)
        step = np.linalg.solve(H, grad)
        # backtracking line search
        ll0 = np.sum(y * np.log(np.maximum(g, 1e-12)) - g)
        lam = 1.0
        for _ in range(20):
            wn = w - lam * step
            gn = _g(X @ wn)
            if np.sum(y * np.log(np.maximum(gn, 1e-12)) - gn) >= ll0 - 1e-9:
                break
            lam *= 0.5
        w = wn
        if np.max(np.abs(lam * step)) < tol:
            break
    return w


def glm_session(s, cells, windows=None, directions=(("PoS", "ADn"), ("ADn", "PoS"))):
    """fig5d,e: for each HD target of one structure, the information (bits per
    spike, 10-fold cross-validated) of a GLM of the other structure's HD cell
    assembly (reading g-b, HD cells; g-c, HD targets), 10 ms bins, assembly
    counts convolved with Gaussian readout windows of s.d. w (GLM_WINDOWS).
    Each fold is fitted to convergence on its 9 training segments (started
    from the fit to all segments, for speed; the likelihood is concave, so the
    start does not change the maximum). HD cells under either reading."""
    windows = GLM_WINDOWS if windows is None else windows
    out = []
    R = {c["unit"]: c for c in cells}
    hd_ = {reg: [c["unit"] for c in cells if c["region"] == reg and (c["hd_a"] or c["hd_b"])] for reg in ("ADn", "PoS")}
    if not hd_["ADn"] or not hd_["PoS"]:
        return out
    name = s["path"].split("_ses-")[1].split("_")[0]
    for k in STATES:
        iv = state_iv(s, k)
        if total(iv) == 0:
            continue
        # first GLM_MAX_S seconds of the state
        cum = np.cumsum(iv[:, 1] - iv[:, 0])
        n_iv = int(np.searchsorted(cum, GLM_MAX_S)) + 1
        iv = iv[:n_iv].copy()
        if cum[min(n_iv, len(cum)) - 1] > GLM_MAX_S:
            iv[-1, 1] -= cum[n_iv - 1] - GLM_MAX_S
        for treg, areg in directions:
            A = bin_matrix([s["spikes"][u] for u in hd_[areg]], iv, DEC_BIN)
            T = bin_matrix([s["spikes"][u] for u in hd_[treg]], iv, DEC_BIN)
            nb = A.shape[1]
            seg = (np.arange(nb) * 10) // nb
            for wdw in windows:
                Aw = gaussian_filter1d(A, wdw / DEC_BIN, axis=1, mode="constant")
                Aw = (Aw - Aw.mean(1, keepdims=True)) / np.maximum(Aw.std(1, keepdims=True), 1e-9)
                X = np.c_[np.ones(nb), Aw.T]
                for ti, u in enumerate(hd_[treg]):
                    y = T[ti]
                    if y.sum() < 20:
                        continue
                    wfull = _glm_fit(X, y, iters=25)
                    L = 0.0
                    for q in range(10):
                        tr, te = seg != q, seg == q
                        # started from the full fit for speed, and iterated to
                        # convergence: the likelihood is concave, so the result
                        # is the maximum on the training segments alone
                        wq = _glm_fit(X[tr], y[tr], wfull, iters=25)
                        f = _g(X[te] @ wq)
                        m0 = y[tr].mean()
                        L += (np.sum(y[te] * np.log2(np.maximum(f, 1e-12))) - np.sum(f) / np.log(2)
                              - (np.sum(y[te]) * np.log2(m0) - m0 * te.sum() / np.log(2)))
                    out.append(dict(session=name, subject=s["subject"], state=k, target=u, target_region=treg,
                                    n_assembly=len(hd_[areg]), window=float(wdw), info=L / y.sum(),
                                    hd_a=R[u]["hd_a"]))
    return out


# ---------------------------------------------------------------- LFP (fig7c)

def lfp_session(s, cells, chunk=1):
    """fig7c: PoS LFP around ADn HD cell spikes, in one HDF5 chunk of time
    (chunk index `chunk`, 1048576 samples, about 14 min; time limit,
    deviation). The PoS channel with the largest 80-250 Hz power (reading
    l-b) in that window; spike-triggered average +-20 ms (l-c), band-passed
    80-250 Hz; power within +-5 ms against (l-a) spikes jittered by +-10 ms
    (seeded) and random times in the window."""
    adn_hd = [c["unit"] for c in cells if c["region"] == "ADn" and c["hd_a"]]
    if not adn_hd:
        return []
    f = open_asset(s["asset_id"])
    el = f["general/extracellular_ephys/electrodes"]
    loc = np.array([_txt(x) for x in el["location"][:]])
    bad = el["bad_channel"][:] if "bad_channel" in el else np.zeros(len(loc), bool)
    lfp = f["processing/ecephys/LFP/lfp"]
    cols = lfp["electrodes"][:]
    d = lfp["data"]
    fs = float(lfp["starting_time"].attrs["rate"])
    t0 = float(lfp["starting_time"][()])
    cs = d.chunks[0]
    a, b = chunk * cs, min((chunk + 1) * cs, d.shape[0])
    pos_cols = [i for i, e in enumerate(cols) if loc[e] == POS and not bad[e]]
    if not pos_cols:
        f.close()
        return []
    X = d[a:b, min(pos_cols):max(pos_cols) + 1].astype(np.float32)
    f.close()
    X = X[:, [c - min(pos_cols) for c in pos_cols]]
    sos = signal.butter(4, [80, 250], btype="band", fs=fs, output="sos")
    Xf = signal.sosfiltfilt(sos, X, axis=0)
    ch = int(np.argmax(np.var(Xf, axis=0)))
    raw, bp = X[:, ch], Xf[:, ch]
    tw = t0 + np.arange(a, b) / fs
    half = int(round(0.02 * fs))
    inner = np.abs(np.arange(-half, half + 1)) <= int(round(0.005 * fs))
    rng = np.random.default_rng(7)
    def sta(ts):
        i = np.round((ts - t0) * fs).astype(int) - a
        i = i[(i > half) & (i < len(bp) - half - 1)]
        if len(i) < 50:
            return None, None
        idx = i[:, None] + np.arange(-half, half + 1)[None]
        return bp[idx].mean(0), raw[idx].mean(0)
    out = []
    name = s["path"].split("_ses-")[1].split("_")[0]
    for u in adn_hd:
        sp = s["spikes"][u]
        sp = sp[(sp > tw[0] + 0.05) & (sp < tw[-1] - 0.05)]
        m, mr = sta(sp)
        if m is None:
            continue
        mj, _ = sta(sp + rng.uniform(-0.01, 0.01, len(sp)))
        mrnd, _ = sta(np.sort(rng.uniform(tw[0] + 0.05, tw[-1] - 0.05, len(sp))))
        P = float(np.mean(m[inner] ** 2))
        out.append(dict(session=name, subject=s["subject"], unit=u, nspk=len(sp), channel=int(cols[pos_cols[ch]]),
                        p_sta=P, p_jit=float(np.mean(mj[inner] ** 2)), p_rand=float(np.mean(mrnd[inner] ** 2)),
                        sta_bp=m, sta_raw=mr))
    return out


# ---------------------------------------------------------------- coherence (fig3b)

def coherence(s, TC, hu, dec, n_time=3000, n_ref=5000, seed=11):
    """fig3b (Methods, Ensemble coherence; ref 34). Actual packet: sum of the
    normalised (peak 1) tuning curves weighted by the smoothed rates; expected
    packet at the decoded angle: the same sum with the rates the tuning curves
    give at that angle. For each degree, n_ref waking population vectors give
    the reference distribution of distances to the expected packet there; the
    coherence of a time bin is the fraction of reference distances at least as
    large as its own. Readings: distance (c-a) Euclidean or 1 - correlation;
    reference vectors (c-b) waking bins whose decoded HD is at that degree,
    whose actual HD is, or random waking bins; summary (c-d) mean or median.
    Windows: the decoder's own (c-c, 300 ms wake and REM, 50 ms SWS). Time
    bins: n_time drawn at random per state (seeded; standard choice). Keys
    with a reference ending in "_shuffled" are the negative control, with the
    decoded angles permuted across time bins."""
    rng = np.random.default_rng(seed)
    rng_shuf = np.random.default_rng(seed + 1)
    Hn = TC / TC.max(1, keepdims=True)  # cells x 360
    Qexp = TC.T @ Hn  # expected packet at each degree (360 x 360)
    def dist(P, Q, kind):
        if kind == "euc":
            return np.sqrt(np.maximum(((P - Q) ** 2).sum(-1), 0))
        Pc = P - P.mean(-1, keepdims=True)
        Qc = Q - Q.mean(-1, keepdims=True)
        return 1 - (Pc * Qc).sum(-1) / np.sqrt((Pc ** 2).sum(-1) * (Qc ** 2).sum(-1) + 1e-12)
    out = {}
    angw, cenw, Cw = dec["wake"]
    Rw = gauss_smooth_counts(Cw, DEC_SMOOTH["wake"]) / DEC_BIN  # Hz
    thw = _hd_at(s, cenw)
    dw = np.minimum((angw / (2 * np.pi) * NBINS).astype(int), NBINS - 1)
    aw = np.where(np.isfinite(thw), np.minimum((np.nan_to_num(thw) / (2 * np.pi) * NBINS).astype(int), NBINS - 1), -1)
    refs = {}
    for ref in ("decoded", "actual", "random"):
        for kind in ("euc", "corr"):
            D = np.empty((NBINS, n_ref))
            for deg in range(NBINS):
                if ref == "random":
                    pool = np.arange(Rw.shape[1])
                else:
                    lab = dw if ref == "decoded" else aw
                    pool = np.where(np.abs(((lab - deg + 180) % 360) - 180) <= 0)[0]
                    if len(pool) < 20:
                        pool = np.where(np.abs(((lab - deg + 180) % 360) - 180) <= 3)[0]
                    if len(pool) == 0:
                        pool = np.arange(Rw.shape[1])
                pick = rng.choice(pool, n_ref, replace=True)
                P = Rw[:, pick].T @ Hn
                D[deg] = np.sort(dist(P, Qexp[deg][None], kind))
            refs[(ref, kind)] = D
    for k, (ang, cen, C) in dec.items():
        Rk = gauss_smooth_counts(C, DEC_SMOOTH[k]) / DEC_BIN
        pick = rng.choice(Rk.shape[1], min(n_time, Rk.shape[1]), replace=False)
        P = Rk[:, pick].T @ Hn
        dd = np.minimum((ang[pick] / (2 * np.pi) * NBINS).astype(int), NBINS - 1)
        Q = Qexp[dd]
        for (ref, kind), D in refs.items():
            d = dist(P, Q, kind)
            coh = np.array([1 - np.searchsorted(D[x], v, side="left") / n_ref for x, v in zip(dd, d)])
            out[(k, ref, kind)] = (float(np.mean(coh)), float(np.median(coh)))
        # Negative control: the same packets against the expected packet at
        # decoded angles permuted across the drawn bins (own generator, so the
        # readings above keep their draws).
        dsh = rng_shuf.permutation(dd)
        for (ref, kind), D in refs.items():
            d = dist(P, Qexp[dsh], kind)
            coh = np.array([1 - np.searchsorted(D[x], v, side="left") / n_ref for x, v in zip(dsh, d)])
            out[(k, ref + "_shuffled", kind)] = (float(np.mean(coh)), float(np.median(coh)))
    return out


# ---------------------------------------------------------------- summaries

def session_summary(s):
    """What the data check prints for one session."""
    name = s["path"].split("_ses-")[1].split("_")[0]
    r = s["region"]
    tags = [tg for e in s["epochs"] for tg in e[0]]
    d = dict(session=name, subject=s["subject"], n_units=len(r), thal_depth=s.get("thal_depth"),
             n_adn=int((r == ADN).sum()), n_pos=int((r == POS).sum()),
             other_regions=";".join(sorted(set(r) - {ADN, POS})),
             has_hd=s.get("hd") is not None, has_states=len(s["states"]) > 0,
             open_field="open_field" in tags, sleep_pre="sleep_pre" in tags, sleep_post="sleep_post" in tags,
             homecage_s=sum(b - a for tg, a, b in s["epochs"] if ("sleep_pre" in tg or "sleep_post" in tg)),
             lfp=s["lfp_shape"] is not None,
             spikes_sorted=all(np.all(np.diff(x) >= 0) for x in s["spikes"]),
             spike_min=float(min((x[0] for x in s["spikes"] if len(x)), default=np.nan)),
             spike_max=float(max((x[-1] for x in s["spikes"] if len(x)), default=np.nan)),
             rec_end=float(max((b for _, a, b in s["sub_recordings"]), default=np.nan)))
    for k in STATES:
        d[k + "_s"] = total(state_iv(s, k)) if k in s["states"] else np.nan
    pos_groups = sorted(set(s["electrode_group"][r == POS]))
    d["pos_groups"] = ";".join(f"{g}: {s['group_info'].get(g, ('', ''))[1][:90]}" for g in pos_groups)
    d["has_pos_probe"] = "postsubicular_probe" in s.get("devices", [])
    # overlap of the scored wake interval with the open-field epochs
    of = np.array([(a, b) for tg, a, b in s["epochs"] if "open_field" in tg])
    if len(of) and "wake" in s["states"] and len(s["states"]["wake"]):
        w = s["states"]["wake"]
        ov = sum(max(0.0, min(b, y) - max(a, x)) for a, b in w for x, y in of)
        d["wake_in_open_field"] = ov / total(w)
        d["open_field_in_wake"] = ov / total(of)
    else:
        d["wake_in_open_field"] = d["open_field_in_wake"] = np.nan
    if "states" in s and len(s["states"]):
        # states inside the home-cage / open-field epochs
        hc = np.array([(a, b) for tg, a, b in s["epochs"] if ("sleep_pre" in tg or "sleep_post" in tg)])
        if len(hc):
            for k in ("SWS", "REM"):
                iv = state_iv(s, k)
                mid = iv.mean(1) if len(iv) else np.zeros(0)
                d[k + "_in_homecage"] = float(np.mean(in_iv(mid, hc))) if len(mid) else np.nan
    if s.get("hd") is not None:
        hdv = s["hd"]
        d["hd_min"], d["hd_max"] = float(np.nanmin(hdv)), float(np.nanmax(hdv))
        d["hd_rate"] = s["hd_rate"]
        w = state_iv(s, "wake") if "wake" in s["states"] else np.zeros((0, 2))
        m = in_iv(s["hd_t"], w)
        d["hd_valid_wake"] = float(np.mean(np.isfinite(hdv[m]))) if m.any() else np.nan
        # LED angle against head direction: circular s.d. of the difference
        n = min(len(hdv), len(s["led_angle"]))
        d["hd_len_minus_pos_len"] = int(len(hdv) - len(s["led_angle"]))
        ok = np.isfinite(hdv[:n]) & np.isfinite(s["led_angle"][:n])
        df = np.exp(1j * (s["led_angle"][:n][ok] - hdv[:n][ok]))
        d["led_minus_hd_deg"] = float(np.degrees(np.angle(df.mean())) % 360)
        d["led_hd_R"] = float(np.abs(df.mean()))
        if m.any():
            p = s["red_led"][:n][m[:n]]
            d["x_range_cm"] = float((np.nanmax(p[:, 0]) - np.nanmin(p[:, 0])) * 100)
            d["y_range_cm"] = float((np.nanmax(p[:, 1]) - np.nanmin(p[:, 1])) * 100)
    return d


SHIFTS = (-10.0, -2.0, -0.5, 0.0, 0.5, 2.0, 10.0)


def shifted_decoding(s, cells, tcs):
    """Clock check: median waking decoding error (ADn or PoS HD cells, the
    largest group with at least 6) with the head direction shifted by each of
    SHIFTS seconds; the tuning curves come from the unshifted data."""
    out = {}
    for reg in ("ADn", "PoS"):
        hu = [c["unit"] for c in cells if c["region"] == reg and c["hd_a"]]
        if len(hu) < 6:
            continue
        W = s["states"]["wake"]
        C = bin_matrix([s["spikes"][u] for u in hu], W, DEC_BIN)
        _, cen = bin_counts(np.zeros(0), W, DEC_BIN)
        ang = bayes_decode(gauss_smooth_counts(C, DEC_SMOOTH["wake"]), np.array([tcs[u] for u in hu]), DEC_BIN)
        for sh in SHIFTS:
            th = _hd_at(s, cen + sh)
            ok = np.isfinite(th)
            out[(reg, sh)] = float(np.degrees(np.median(np.abs(circ_diff(ang[ok], th[ok])))))
    return out


def _work(x):
    import time as _t
    t0 = _t.time()
    s = load_session(x[1], x[0])
    o = analyze_session(s)
    o["meta"] = dict(path=x[0], subject=s["subject"], seconds=_t.time() - t0)
    return o


def _work_glm(x):
    import time as _t
    t0 = _t.time()
    s = load_session(x[1], x[0])
    if len(x) > 3:
        # dense readout windows, PoS targets only (fig5e-readout-windows)
        o = analyze_session(s, parts=("glm_dense",))
    else:
        o = analyze_session(s, parts=("glm",))
    o["meta"] = dict(path=x[0], subject=s["subject"], seconds=_t.time() - t0)
    return o


def run_glm(subjects, workers=4, dense=False, sessions=None):
    """The GLM of fig5d,e on every session of the given mice (or only the
    named sessions), `workers` sessions at a time, largest files first; with
    `dense`, the dense windows of fig5e-readout-windows, PoS targets only."""
    from concurrent.futures import ProcessPoolExecutor
    A = sorted([a + ((True,) if dense else ()) for a in list_assets()
                if a[0].split("/")[0].replace("sub-", "") in subjects
                and (sessions is None or any(x in a[0] for x in sessions))],
               key=lambda x: -x[2])
    with ProcessPoolExecutor(workers) as ex:
        out = list(ex.map(_work_glm, A))
    return sorted(out, key=lambda o: o["meta"]["path"])


def run_all(workers=4):
    """Stream and analyse every session of the pinned version, `workers`
    sessions at a time (each worker holds one session, peak about 3.5 GB)."""
    from concurrent.futures import ProcessPoolExecutor
    A = sorted(list_assets(), key=lambda x: -x[2])
    with ProcessPoolExecutor(workers) as ex:
        out = list(ex.map(_work, A))
    return sorted(out, key=lambda o: o["meta"]["path"])
