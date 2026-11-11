"""Loading and measures for Hernandez-Perez, Cooper and Newman (2020) on CRCNS hc-27.

Every parameter says where it comes from: "Methods, <section>" is the paper
(doi:10.7554/elife.52289), "O<n>" is the open detail of that number in the
claims file (claims/hernandez-perez-2020.yaml, header), "assumption" is a
choice the paper leaves open, and "standard choice" is a detail that cannot
change an outcome.
"""
import io
import zipfile

import fsspec
import h5py
import numpy as np
from scipy import signal, stats

DATASET = "hc-27"
DATASET_VERSION = "unversioned"  # CRCNS data sets are not versioned (docs/archives.md); the notebook prints the MD5 sums
URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-27/live/RawSignalTravelingWaveRats.zip"
FS = 500.0  # data descriptor, PRIMARY DATA: "The sampling rate of the data (fs) is 500Hz"
SPACING_MM = 0.566  # Methods, Electrode array construction: "net ~566 um" between adjacent shanks (O1a)
RATS = [1, 2, 3, 4, 5, 6]
INTAN_UV_PER_BIT = 0.195  # Intan RHD2000 step; used only for the unit reading "counts" (assumption)


def open_zip():
    """The data zip, read in place over range requests (docs/archives.md, CRCNS)."""
    return zipfile.ZipFile(fsspec.open(URL, block_size=2**20).open())


def load_rat(z, rat):
    """LFP of one rat as (channels, samples), channel 0 the most dorsal (data descriptor)."""
    with h5py.File(io.BytesIO(z.read(f"RawSignalTravelingWaveRats/rat{rat}.mat")), "r") as h:
        return np.ascontiguousarray(h[f"rat{rat}"][()].T)


def positions_mm(nch):
    """Distance from the dorsal-most electrode, 0.566 mm per channel (O1, reading a)."""
    return SPACING_MM * np.arange(nch)


def bandpass(x, lo, hi, order=4):
    """Zero-phase Butterworth (Methods, Data inclusion criteria and Theta phase estimation;
    MATLAB butter(order, band) through filtfilt, O8)."""
    b, a = signal.butter(order, [lo, hi], btype="band", fs=FS)
    return signal.filtfilt(b, a, x, axis=-1)


# ---------------------------------------------------------------- artefacts and epochs

def artefact_mask(x, k=5.0, buffer_s=0.5):
    """True where a channel is kept. Methods, Data inclusion criteria: swings over five times
    the RMS, 500 ms either side removed, repeated on the cleaned data until none remain. The
    swing is the absolute deviation from the mean of the kept data (O3, standard choice)."""
    keep = np.ones(x.size, bool)
    buf = int(round(buffer_s * FS))
    while True:
        xc = x[keep]
        mu = xc.mean()
        rms = np.sqrt(np.mean((xc - mu) ** 2))
        bad = (np.abs(x - mu) > k * rms) & keep
        if not bad.any():
            return keep
        idx = np.flatnonzero(bad)
        cover = np.zeros(x.size + 1, int)
        np.add.at(cover, np.clip(idx - buf, 0, x.size), 1)
        np.add.at(cover, np.clip(idx + buf + 1, 0, x.size), -1)
        keep &= np.cumsum(cover)[:-1] == 0


def runs(mask):
    """Start and stop (exclusive) of runs of True."""
    d = np.diff(np.concatenate([[0], mask.astype(int), [0]]))
    return np.flatnonzero(d == 1), np.flatnonzero(d == -1)


def theta_epochs(amp, keep, thr, min_s=0.5, gap_s=0.1):
    """High-amplitude theta (Methods, Data inclusion criteria): 6-12 Hz amplitude above thr for
    500 ms or longer, dips of 100 ms or less ignored, within the artefact-free data. Amplitude is
    the Hilbert magnitude of the 6-12 Hz signal (O3, standard choice)."""
    above = (amp > thr) & keep
    s, e = runs(~above)
    for a, b in zip(s, e):  # fill short dips that lie between two supra-threshold stretches
        if b - a <= gap_s * FS and a > 0 and b < above.size:
            above[a:b] = True
    above &= keep
    s, e = runs(above)
    out = np.zeros_like(above)
    for a, b in zip(s, e):
        if b - a >= min_s * FS:
            out[a:b] = True
    return out


class Rat:
    """One rat's data reduced to what the analyses use.

    unit reading (the files state no unit, see the notebook's data check):
      "file"   : the 400 uV threshold applied to the values as stored;
      "counts" : rats whose values are not integers are taken to be in uV and divided by the
                 Intan step of 0.195 uV, so all rats are in ADC counts, then 400 is applied;
      "none"   : no theta-amplitude restriction (all artefact-free data).
    """

    def __init__(self, rat, x):
        self.rat = rat
        self.isint = bool(np.all(x == np.round(x)))
        self.x = x - x.mean(axis=1, keepdims=True)
        self.nch, self.n = x.shape
        self.pos = positions_mm(self.nch)
        self.keep = np.array([artefact_mask(c) for c in self.x])
        self.theta = bandpass(self.x, 6, 12)  # Methods, Theta phase estimation (Hilbert method)
        an = signal.hilbert(self.theta, axis=1)
        self.phase = np.angle(an)
        self.amp = np.abs(an)
        self.broad = bandpass(self.x, 1, 25)  # Methods, Theta phase estimation (waveform method)

    def scale(self, unit):
        if unit == "counts" and not self.isint:
            return 1.0 / INTAN_UV_PER_BIT
        return 1.0

    def epochs(self, unit, thr=400.0):
        """Per-channel theta epochs, (channels, samples)."""
        if unit == "none":
            return self.keep.copy()
        a = self.amp * self.scale(unit)
        return np.array([theta_epochs(a[c], self.keep[c], thr) for c in range(self.nch)])

    def masks(self, unit, chan_reading):
        """Mask for the pair (0, j), for each j, under O3: "a" each channel's own epochs, pairwise
        intersection; "b" times kept on all channels; "c" epochs of the dorsal-most channel."""
        ep = self.epochs(unit)
        if chan_reading == "a":
            return [ep[0] & ep[j] for j in range(self.nch)]
        if chan_reading == "b":
            allm = ep.all(axis=0)
            return [allm] * self.nch
        if chan_reading == "c":
            return [ep[0]] * self.nch
        raise ValueError(chan_reading)


# ---------------------------------------------------------------- Hilbert phase measures

def circ_mean_diff(p0, pj, mask):
    """Circular mean (deg) and mean resultant length of p0 - pj over mask (Methods, Phase
    locking). Positive when channel j lags channel 0."""
    if mask.sum() == 0:
        return np.nan, np.nan
    z = np.exp(1j * (p0[mask] - pj[mask])).mean()
    return np.degrees(np.angle(z)), np.abs(z)


def lsq_slope(x, y, intercept=True):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    if intercept:
        return np.polyfit(x, y, 1)[0]
    return np.sum(x * y) / np.sum(x * x)


def signrank(v):
    """Exact two-sided Wilcoxon signed-rank test (O4). Returns (T+, p): T+ is the sum of the
    ranks of the positive values, the statistic the paper prints with its maximum."""
    v = np.asarray(v, float)
    v = v[v != 0]
    r = stats.rankdata(np.abs(v))
    tplus = r[v > 0].sum()
    p = stats.wilcoxon(v, method="exact").pvalue
    return tplus, p


def boot_ci(v, rng, nboot=500, stat=np.median):
    """95% bootstrap CI from 500 resamples (Methods, Statistics)."""
    v = np.asarray(v, float)
    b = [stat(rng.choice(v, v.size)) for _ in range(nboot)]
    return np.percentile(b, [2.5, 97.5])


# ---------------------------------------------------------------- coherence and power

def segment_starts(mask, nper, step):
    """Starts of windows of nper samples lying wholly inside mask."""
    s, e = runs(mask)
    out = []
    for a, b in zip(s, e):
        out.extend(range(a, b - nper + 1, step))
    return np.array(out, int)


def coherence_theta(x0, xj, mask, reading):
    """Mean magnitude-squared coherence over 6, 7, ... 12 Hz (Methods, Theta band coherence),
    from Hann-windowed segments inside the artefact-free mask. Window (fig2c-coherence): "a" 1 s
    windows, 50% overlap (bins fall on the integer frequencies); "b" MATLAB cohere's default, 256
    samples, no overlap, nfft 256, interpolated to the integer frequencies."""
    nper, step = (500, 250) if reading == "a" else (256, 256)
    st = segment_starts(mask, nper, step)
    if st.size < 2:
        return np.nan
    w = signal.windows.hann(nper, sym=False)
    idx = st[:, None] + np.arange(nper)[None, :]
    a = x0[idx]
    b = xj[idx]
    a = (a - a.mean(1, keepdims=True)) * w
    b = (b - b.mean(1, keepdims=True)) * w
    fa = np.fft.rfft(a, axis=1)
    fb = np.fft.rfft(b, axis=1)
    f = np.fft.rfftfreq(nper, 1 / FS)
    pxy = (fa * np.conj(fb)).mean(0)
    coh = np.abs(pxy) ** 2 / ((np.abs(fa) ** 2).mean(0) * (np.abs(fb) ** 2).mean(0))
    return float(np.mean(np.interp(np.arange(6, 13), f, coh)))


def theta_power_welch(x, mask):
    """Mean Welch PSD over 6-12 Hz from 1 s Hann windows, 50% overlap, inside mask
    (fig2g-power-no-change)."""
    st = segment_starts(mask, 500, 250)
    if st.size == 0:
        return np.nan
    w = signal.windows.hann(500, sym=False)
    seg = x[st[:, None] + np.arange(500)[None, :]]
    seg = (seg - seg.mean(1, keepdims=True)) * w
    p = (np.abs(np.fft.rfft(seg, axis=1)) ** 2).mean(0) / (FS * (w**2).sum())
    f = np.fft.rfftfreq(500, 1 / FS)
    return float(p[(f >= 6) & (f <= 12)].mean())


# ---------------------------------------------------------------- waveform method

def extrema(broad, theta, reading):
    """Alternating extrema of one channel, as (times, is_peak), O7.

    "a": local maxima and minima of the 1-25 Hz signal, each type at least 83 ms from the last
         of its type (MATLAB findpeaks MinPeakDistance), merged and made to alternate by keeping
         the more extreme of two of a kind in a row (Methods, Theta phase estimation).
    "b": as Cole and Voytek, one maximum of the 1-25 Hz signal between each rising and the next
         falling zero crossing of the 6-12 Hz signal, one minimum between each falling and the
         next rising crossing.
    The 83-250 ms limit on the cycle is applied in cycles()."""
    if reading == "a":
        mind = int(np.ceil(0.083 * FS))
        pk, _ = signal.find_peaks(broad, distance=mind)
        tr, _ = signal.find_peaks(-broad, distance=mind)
        t = np.concatenate([pk, tr])
        ispk = np.concatenate([np.ones(pk.size, bool), np.zeros(tr.size, bool)])
        o = np.argsort(t, kind="stable")
        t, ispk = t[o], ispk[o]
        keep = np.ones(t.size, bool)
        i = 0
        # resolve runs of the same type, keeping the most extreme
        same = np.flatnonzero(ispk[1:] == ispk[:-1])
        if same.size:
            val = np.where(ispk, broad[t], -broad[t])
            grp = np.concatenate([[0], np.cumsum(ispk[1:] != ispk[:-1])])
            best = {}
            for k in range(t.size):
                g = grp[k]
                if g not in best or val[k] > val[best[g]]:
                    best[g] = k
            keep[:] = False
            keep[list(best.values())] = True
        return t[keep], ispk[keep]
    s = np.signbit(theta)
    rise = np.flatnonzero(s[:-1] & ~s[1:]) + 1
    fall = np.flatnonzero(~s[:-1] & s[1:]) + 1
    ev = np.concatenate([rise, fall])
    isr = np.concatenate([np.ones(rise.size, bool), np.zeros(fall.size, bool)])
    o = np.argsort(ev)
    ev, isr = ev[o], isr[o]
    t = []
    ispk = []
    for k in range(ev.size - 1):
        a, b = ev[k], ev[k + 1]
        if b <= a + 1:
            continue
        if isr[k]:
            t.append(a + np.argmax(broad[a:b]))
            ispk.append(True)
        else:
            t.append(a + np.argmin(broad[a:b]))
            ispk.append(False)
    return np.array(t, int), np.array(ispk, bool)


def midpoint(broad, a, b):
    """The sample between a and b where the signal is closest to the mean of broad[a] and
    broad[b] (Methods, Theta phase estimation, 90 and 270 deg)."""
    target = 0.5 * (broad[a] + broad[b])
    return a + int(np.argmin(np.abs(broad[a:b + 1] - target)))


def cycles(broad, t, ispk):
    """Peak-centred cycles: trough before, peak, trough after, next peak. Returns a dict of
    arrays, one entry per peak with a full neighbourhood, and 'valid' where the peak-to-peak
    period is 83 to 250 ms (Methods, Theta phase estimation).

    rise = peak - previous trough, decay = next trough - peak (Methods, Asymmetry analysis;
    Figure 5A). Falling midpoint F between peak and next trough, rising midpoint R between
    previous trough and peak; peak duration = F - R around the peak; trough duration = next R
    - F around the next trough (Figure 5A legend)."""
    # need sequence T P T P with the peak at index i
    idx = np.flatnonzero(ispk)
    idx = idx[(idx >= 1) & (idx + 3 < t.size)]
    tp = t[idx]
    tprev = t[idx - 1]
    tnext = t[idx + 1]
    pnext = t[idx + 2]
    tnext2 = t[idx + 3]
    R = np.array([midpoint(broad, a, b) for a, b in zip(tprev, tp)])
    F = np.array([midpoint(broad, a, b) for a, b in zip(tp, tnext)])
    Rn = np.array([midpoint(broad, a, b) for a, b in zip(tnext, pnext)])
    per = (pnext - tp) / FS
    return dict(
        peak=tp, fall=F, trough=tnext, rise_mid=Rn,
        rise=(tp - tprev) / FS * 1000, decay=(tnext - tp) / FS * 1000,
        peakdur=(F - R) / FS * 1000, troughdur=(Rn - F) / FS * 1000,
        period=per * 1000, valid=(per >= 0.083) & (per <= 0.250),
        _next_peak=pnext, _next_trough2=tnext2,
    )


# ---------------------------------------------------------------- robust regression

def robustfit_slopes(x, Y, tune=4.685, maxit=50, tol=1e-6):
    """Slopes of MATLAB robustfit (bisquare, tuning 4.685, intercept) of each row of Y on x,
    vectorised over rows. Scale is the MAD of leverage-adjusted residuals (madsigma). Returns
    slopes and a converged flag (Methods, Conduction delays: rows that do not converge are
    dropped)."""
    x = np.asarray(x, float)
    n = x.size
    X = np.column_stack([np.ones(n), x])
    H = X @ np.linalg.pinv(X)
    h = np.clip(np.diag(H), 0, 1 - 1e-10)
    adj = 1 / np.sqrt(1 - h)
    p = 2
    beta = np.linalg.lstsq(X, Y.T, rcond=None)[0].T  # (rows, 2)
    conv = np.zeros(Y.shape[0], bool)
    eps = np.sqrt(np.finfo(float).eps)
    for _ in range(maxit):
        res = Y - beta @ X.T
        radj = res * adj
        srt = np.sort(np.abs(radj), axis=1)[:, p - 1:]
        s = np.median(srt, axis=1) / 0.6745
        s = np.maximum(s, eps * np.std(Y, axis=1) + 1e-12)
        u = radj / (tune * s[:, None])
        w = np.where(np.abs(u) < 1, (1 - u**2) ** 2, 0.0)
        # weighted least squares per row
        sw = w.sum(1)
        swx = (w * x).sum(1)
        swxx = (w * x * x).sum(1)
        swy = (w * Y).sum(1)
        swxy = (w * x * Y).sum(1)
        det = sw * swxx - swx**2
        ok = det > 1e-12
        b1 = np.where(ok, (sw * swxy - swx * swy) / np.where(ok, det, 1), np.nan)
        b0 = np.where(ok, (swy - b1 * swx) / np.where(sw > 0, sw, 1), np.nan)
        new = np.column_stack([b0, b1])
        d = np.abs(new - beta).max(1)
        newly = (d <= tol * np.maximum(np.abs(new).max(1), np.abs(beta).max(1)))
        conv |= newly & ok
        beta = np.where(conv[:, None], beta, new)
        if conv.all():
            break
    return beta[:, 1], conv & np.isfinite(beta[:, 1])


def nearest(ref, ev):
    """For each ref time, the nearest time in sorted ev (forward or backward)."""
    i = np.clip(np.searchsorted(ev, ref), 1, ev.size - 1)
    a, b = ev[i - 1], ev[i]
    return np.where(np.abs(ref - a) <= np.abs(b - ref), a, b)


# ---------------------------------------------------------------- per-rat measures

PHASES = ["fall", "trough", "rise_mid", "peak"]  # 90, 180, 270, 360 deg (Figure 6B legend)
PHASE_DEG = {"fall": 90, "trough": 180, "rise_mid": 270, "peak": 360}


def hilbert_measures(R, unit, chr_):
    """Phase offset (deg, positive when j lags the dorsal-most) and mean resultant length of
    each channel against the dorsal-most, and the MRL of every pair (Methods, Phase locking)."""
    ep = R.epochs(unit)
    m0 = R.masks(unit, chr_)
    off = np.zeros(R.nch)
    mrl = np.ones(R.nch)
    nsamp = np.zeros(R.nch, int)
    for j in range(1, R.nch):
        off[j], mrl[j] = circ_mean_diff(R.phase[0], R.phase[j], m0[j])
        nsamp[j] = m0[j].sum()
    pair = np.full((R.nch, R.nch), np.nan)
    allm = ep.all(0)
    for i in range(R.nch):
        for j in range(i + 1, R.nch):
            mk = {"a": ep[i] & ep[j], "b": allm, "c": ep[0]}[chr_]
            pair[i, j] = circ_mean_diff(R.phase[i], R.phase[j], mk)[1]
    return dict(offset=off, mrl=mrl, pair_mrl=pair, nsamp=nsamp)


def coherence_matrix(R, window, chr_):
    """Theta coherence of every pair on artefact-free data, not restricted to theta epochs
    (Methods, Theta band coherence). Pair mask: "a" both channels kept; "b" all channels kept."""
    out = np.full((R.nch, R.nch), np.nan)
    allk = R.keep.all(0)
    for i in range(R.nch):
        for j in range(i + 1, R.nch):
            mk = R.keep[i] & R.keep[j] if chr_ == "a" else allk
            out[i, j] = coherence_theta(R.x[i], R.x[j], mk, window)
    return out


def theta_power(R, unit, chr_):
    """Per channel theta power on the theta epochs: Welch (1 s Hann, 50% overlap, mean over 6-12
    Hz) and mean squared Hilbert amplitude (fig2g-power-no-change). Masks under O3: "a" own
    epochs, "b" all channels', "c" the dorsal-most's."""
    ep = R.epochs(unit)
    w = np.zeros(R.nch)
    h = np.zeros(R.nch)
    for c in range(R.nch):
        mk = {"a": ep[c], "b": ep.all(0), "c": ep[0]}[chr_]
        w[c] = theta_power_welch(R.x[c], mk)
        h[c] = np.mean(R.amp[c][mk] ** 2) if mk.any() else np.nan
    return dict(welch=w, hilbert=h)


def all_cycles(R, ext):
    out = []
    for c in range(R.nch):
        t, pk = extrema(R.broad[c], R.theta[c], ext)
        cy = cycles(R.broad[c], t, pk)
        cy["prev_period"] = np.concatenate([[np.nan], np.diff(cy["peak"]) / FS * 1000])
        out.append(cy)
    return out


def asymmetry_by_channel(R, cyc, unit, chr_):
    """Median over valid cycles in the theta epochs of log10(rise/decay) and log10(peak/trough
    duration), per channel (Methods, Asymmetry analysis; Figure 5A legend)."""
    ep = R.epochs(unit)
    rd = np.zeros(R.nch)
    pt = np.zeros(R.nch)
    n = np.zeros(R.nch, int)
    for c in range(R.nch):
        cy = cyc[c]
        mk = {"a": ep[c], "b": ep.all(0), "c": ep[0]}[chr_]
        sel = cy["valid"] & mk[cy["peak"]] & (cy["peakdur"] > 0) & (cy["troughdur"] > 0)
        rd[c] = np.median(np.log10(cy["rise"][sel] / cy["decay"][sel]))
        pt[c] = np.median(np.log10(cy["peakdur"][sel] / cy["troughdur"][sel]))
        n[c] = sel.sum()
    return dict(rise_decay=rd, peak_trough=pt, n=n)


def delays(R, cyc, unit, chr_):
    """Per-cycle conduction delays (Methods, Conduction delays of specific theta phases). The
    dorsal-most channel's valid cycles inside the theta mask ("b" all channels' epochs, "c" the
    dorsal-most's) are the reference; for each phase, the nearest same-phase time on every other
    channel; robust regression of offset (ms) on position (mm), the dorsal point (0, 0)
    included. Also the asymmetry-related delay of each channel (Methods, Asymmetry-corrected
    data): (D_fall(0) - D_rise(0)) - (D_fall(j) - D_rise(j)) on the cycle whose peak is nearest
    the reference peak, and the corrected per-cycle peak delay."""
    ep = R.epochs(unit)
    mk = ep.all(0) if chr_ in ("a", "b") else ep[0]
    c0 = cyc[0]
    sel = c0["valid"] & mk[c0["peak"]]
    out = dict(n_ref=int(sel.sum()), pos=R.pos)
    offs = {}
    for ph in PHASES:
        ref = c0[ph][sel]
        O = np.zeros((ref.size, R.nch))
        for j in range(1, R.nch):
            ev = np.sort(cyc[j][ph])
            O[:, j] = (nearest(ref, ev) - ref) / FS * 1000
        offs[ph] = O
        s, ok = robustfit_slopes(R.pos, O)
        out[ph] = s[ok]
        out[ph + "_dropped"] = int((~ok).sum())
    # asymmetry-related delay
    refp = c0["peak"][sel]
    A = np.zeros((refp.size, R.nch))
    asym0 = (c0["decay"] - c0["rise"])[sel]
    for j in range(1, R.nch):
        pj = cyc[j]["peak"]
        k = np.clip(np.searchsorted(pj, refp), 1, pj.size - 1)
        k = np.where(np.abs(pj[k - 1] - refp) <= np.abs(pj[k] - refp), k - 1, k)
        A[:, j] = asym0 - (cyc[j]["decay"] - cyc[j]["rise"])[k]
    out["asym_matrix"] = A
    out["peak_matrix"] = offs["peak"]
    sa, oka = robustfit_slopes(R.pos, A)
    out["asym_cycle"] = sa[oka]
    sr, okr = robustfit_slopes(R.pos, offs["peak"] - A)
    out["resid_cycle"] = sr
    out["resid_ok"] = okr
    out["period"] = c0["period"][sel]
    out["prev_period"] = c0["prev_period"][sel]
    return out
