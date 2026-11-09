"""Loading and measures for Kim, Atencio and Schreiner (2020) on CRCNS ac-5.

Data: CRCNS ac-5 (doi:10.6080/K07H1GSS), unversioned; files under ac-5/live/ in the public
bucket crcnsarchive. data.tar.gz and codes.tar.gz are streamed once each and opened in place
(tarfile over fsspec range reads); nothing is written to disk.

Where each parameter comes from is said next to it:
  [code]   the paper's own Matlab code, shipped in the data set's codes.tar.gz (file named);
  [paper]  the paper's Methods or Results (passage named);
  [claims] the claims file (claim or detail D1 to D17 named);
  [assumption] a choice the paper leaves open (why it was made is said);
  [standard] a choice that cannot change an outcome.
"""
import io
import tarfile

import fsspec
import numpy as np
import scipy.io
from scipy import optimize, special, stats

BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-5/live/"
DATASET = "crcns:ac-5/unversioned"
DOI = "10.6080/K07H1GSS"
# MD5 sums from ac-5/live/checksums.md5 for the files read (archives.md, CRCNS).
MD5 = {"data.tar.gz": "84c11d715bada8da5518fb8da9032505",
       "codes.tar.gz": "153e23136a08c8b45ecf422b459a620b",
       "docs/data_file_information.xlsx": "9515d32985fbbf27f0a6df1a384d8a5f"}
FS = 10000            # [paper] Methods: digitized at 10 kHz; data descriptor: fs = 10 kHz
SPR_DS = "rn1-500flo-40000fhi-4SM-40TM-40db-96khz-48DF-10min_DFt10_DFf5.spr"
TONE_PARAMS = ("freq_resp_area_stimulus_parameters_flo4000Hz_fhi40000Hz_nfreq45_natten8_"
               "nreps1_fs96000.mat")
# DMR envelope constants [code] rtwstrfdb.m and the _DFt10_DFf5_param.mat file
MDB = 40.0            # modulation depth (dB)
PP = MDB ** 2 / 8     # envelope variance of the moving ripple
NT, NF = 67, 64       # frames per block, frequency channels of the downsampled envelope
DT_ENV = 480 / 96000  # 5 ms per envelope frame (DF / Fs)
NLAG = 40             # [code] tbefore = 0.2 s, tafter = 0 (data_analysis_instructions.txt)


def stream_tar(name, want=None):
    """Yield (member name, bytes) for members of a tarball, streamed once from the bucket.

    want(name) -> bool selects members; others are skipped without being kept."""
    with fsspec.open(BASE + name, block_size=2 ** 24) as f:
        tf = tarfile.open(fileobj=f, mode="r|gz")
        for m in tf:
            if m.isfile() and (want is None or want(m.name)):
                yield m.name, tf.extractfile(m).read()


def loadmat_bytes(b):
    return {k: v for k, v in scipy.io.loadmat(io.BytesIO(b)).items() if not k.startswith("__")}


def load_codes():
    """The downsampled DMR envelope (frequency x frame, in dB about its mean) and the tone
    presentation order, from codes.tar.gz."""
    out = {}
    for name, b in stream_tar("codes.tar.gz",
                              lambda n: n.endswith(SPR_DS) or n.endswith(SPR_DS[:-4] + "_param.mat")
                              or n.endswith(TONE_PARAMS)):
        if name.endswith(".spr"):
            s = np.frombuffer(b, dtype="<f4")
            # [code] read_entire_spr_file.m: blocks of NF x NT (column-major), MdB*s - RMSP
            env = s.reshape(-1, NT, NF).reshape(-1, NF).T * MDB + MDB / 2
            out["env"] = np.ascontiguousarray(env, dtype=np.float64)
        elif name.endswith(TONE_PARAMS):
            p = loadmat_bytes(b)["params"][0, 0]
            order = np.asarray(p["stimulus_presentation_order"], float)
            out["tone_freq"] = order[:, 2]
            out["tone_atten"] = order[:, 3]
        else:
            p = loadmat_bytes(b)
            out["faxis"] = np.asarray(p["faxis"], float).ravel()
    return out


def matlab_smooth(y, span=100000):
    """Matlab smooth(y, span): moving average, even span reduced by one, shrinking at the ends.
    [code] read_data.m / data_analysis_instructions.txt step (1): processed = raw - smooth(raw, 1e5)."""
    if span % 2 == 0:
        span -= 1
    n = len(y)
    cs = np.concatenate([[0.0], np.cumsum(y, dtype=np.float64)])
    i = np.arange(n)
    h = np.minimum(np.minimum(i, n - 1 - i), span // 2)
    return (cs[i + h + 1] - cs[i - h]) / (2 * h + 1)


def peakfinder(x0, sel, thresh=None, extrema=1, interpolate=True):
    """Port of Nathanael Yoder's peakfinder.m as shipped in codes.tar.gz, with
    includeEndpoints = false [code] read_data.m: peakfinder(response, 3, -10, 1, false, true).
    Returns (peak indices, 0-based and interpolated; peak magnitudes)."""
    x0 = extrema * np.asarray(x0, dtype=np.float64)
    if thresh is not None:
        thresh = thresh * extrema
    len0 = len(x0)
    dx0 = np.diff(x0)
    dx0[dx0 == 0] = -np.finfo(float).eps
    ind = np.nonzero(dx0[:-1] * dx0[1:] < 0)[0] + 1
    x = x0[ind]
    minMag = x.min()
    leftMin = min(x[0], x0[0])
    n = len(x)
    locs, mags = [], []
    tempMag, tempLoc, foundPeak = minMag, 0, False
    ii = -1 if x[0] >= x[1] else 0
    xl = x.tolist()
    while ii < n - 1:
        ii += 1
        if foundPeak:
            tempMag = minMag
            foundPeak = False
        xi = xl[ii]
        if xi > tempMag and xi > leftMin + sel:
            tempLoc, tempMag = ii, xi
        if ii == n - 1:
            break
        ii += 1
        xv = xl[ii]
        if not foundPeak and tempMag > sel + xv:
            foundPeak = True
            leftMin = xv
            locs.append(tempLoc)
            mags.append(tempMag)
        elif xv < leftMin:
            leftMin = xv
    if not foundPeak:
        if xl[-1] > tempMag and xl[-1] > leftMin + sel:
            locs.append(n - 1)
            mags.append(xl[-1])
        elif tempMag > min(x0[-1], xl[-1]) + sel:
            locs.append(tempLoc)
            mags.append(tempMag)
    pk = ind[np.asarray(locs, dtype=int)].astype(float)
    mg = np.asarray(mags, dtype=float)
    if thresh is not None:
        keep = mg > thresh
        pk, mg = pk[keep], mg[keep]
    if interpolate and len(pk):
        p = pk.astype(int)
        mid = (p > 0) & (p < len0 - 1)
        q = p[mid]
        magDiff = x0[q + 1] - x0[q - 1]
        magSum = x0[q - 1] + x0[q + 1] - 2 * x0[q]
        with np.errstate(divide="ignore", invalid="ignore"):
            ratio = np.where(magSum != 0, magDiff / magSum, 0.0)
        pk[mid] = pk[mid] - ratio / 2
        mg[mid] = mg[mid] - ratio * magDiff / 8
    return pk, extrema * mg


# ----------------------------------------------------------------------------------------
# Events
# ----------------------------------------------------------------------------------------
PEAK_SEL_CC = 3.0     # [code] read_data.m, peakfinder(response, 3, -10, 1, false, true);
                      # [paper] Methods, Data analysis: "~3 mV for current-clamp recordings"
PEAK_THRESH = -10.0   # [code] read_data.m
PEAK_SEL_VC = (20.0, 40.0)  # [paper] Methods, Data analysis: "~20-40 pA for voltage-clamp"; both run


def detect_events(raw, sel, sign=1, pr=None):
    """Peaks of sign * processed by peakfinder. processed is the data set's _processed.mat
    trace when given (the data descriptor: 'a derived data used to produce Figures'), else
    raw - smooth(raw, 1e5) [code] read_data.m.
    Returns peak sample positions (float, 0-based) and amplitudes (sign * processed value at
    the peak, the code's Amp_dist: "all the events used the same absolute baseline",
    Methods, Data analysis)."""
    if pr is None:
        pr = raw - matlab_smooth(raw)
    pk, mg = peakfinder(sign * pr, sel, PEAK_THRESH)
    return pk, mg, pr


def spike_cut_gap(amp, min_gap=5.0, floor=15.0):
    """D1 reading (a): the per-neuron cut between the PSP and spike groups of the amplitude
    histogram, taken at the widest empty gap (at least min_gap mV) among amplitudes above
    `floor` mV; no gap means no spikes. [assumption] The paper shows the two groups (Fig. 2a, b)
    but gives no rule; min_gap and floor are set from the gap the histograms show (5 mV is
    narrower than every gap seen, 15 mV is above the PSP groups' modes)."""
    a = np.sort(amp[amp > floor])
    if len(a) < 2:
        return np.inf
    g = np.diff(a)
    i = int(np.argmax(g))
    if g[i] < min_gap:
        return np.inf
    return (a[i] + a[i + 1]) / 2


def spike_mask_dvdt(raw, pk, thr=10.0):
    """D1 reading (b): an action potential criterion on the trace, peak rate of rise in the
    2 ms before the peak above `thr` mV/ms. [assumption] 10 mV/ms is a common spike criterion."""
    p = np.round(pk).astype(int)
    d = np.diff(raw) * FS / 1000.0  # mV/ms
    out = np.zeros(len(p), bool)
    for j, q in enumerate(p):
        lo = max(q - 20, 0)
        if q > lo:
            out[j] = d[lo:q].max() > thr
    return out


def baseline_sd(pr, pk, trig0, reading):
    """D3: the s.d. of 'unresponsive baseline segments'. Reading 'pre': the processed trace
    before the first DMR trigger (no stimulus). Reading 'quiet': samples during the DMR
    farther than 50 ms from any detected peak [standard 50 ms]."""
    if reading == "pre":
        return float(np.std(pr[:trig0]))
    m = np.ones(len(pr), bool)
    m[:trig0] = False
    p = np.round(pk).astype(int)
    for q in p:
        m[max(q - 500, 0):q + 500] = False
    return float(np.std(pr[m]))


def kde_modes(x, grid=None):
    """Gaussian KDE (Scott bandwidth) [standard]; returns grid, density and indices of maxima."""
    if grid is None:
        grid = np.linspace(x.min(), x.max(), 400)
    d = stats.gaussian_kde(x)(grid)
    mx = np.nonzero((d[1:-1] > d[:-2]) & (d[1:-1] >= d[2:]))[0] + 1
    return grid, d, mx


def bimodal_trough(x, min_rel=0.1):
    """D4 reading (a): two maxima separated by a trough. The two highest KDE maxima, the smaller
    at least min_rel of the larger [assumption, to ignore ripples of the tail]; returns the
    trough position or None."""
    if len(x) < 10:
        return None
    grid, d, mx = kde_modes(x)
    mx = [m for m in mx if d[m] >= min_rel * d[mx].max()]
    if len(mx) < 2:
        return None
    top = sorted(sorted(mx, key=lambda m: d[m])[-2:])
    seg = slice(top[0], top[1] + 1)
    j = top[0] + int(np.argmin(d[seg]))
    return float(grid[j])


def dip_test_p(x):
    """D4 reading (b): Hartigan's dip test p-value (package diptest)."""
    import diptest
    return float(diptest.diptest(np.asarray(x, float))[1])


# ----------------------------------------------------------------------------------------
# STRFs
# ----------------------------------------------------------------------------------------
def event_frames(pk, trig):
    """Global envelope frame of each event, as rtwstrfdb.m maps it [code]: events between
    trigger k and k+1 (k = 2 .. NTrig-2, 1-based) fall in block k, frame
    ceil((spet - Trig(k) + 1) * Fs / Fss / DF). Events outside these blocks are dropped."""
    spet = np.round(pk).astype(np.int64) + 1   # Matlab sample numbers (1-based)
    trig = np.asarray(trig, np.int64).ravel()
    b = np.searchsorted(trig, spet, side="right") - 1   # 0-based block
    ok = (b >= 1) & (b <= len(trig) - 3)
    fr = np.ceil((spet[ok] - trig[b[ok]] + 1) * 96000 / FS / 480).astype(np.int64)  # 1..67
    fr = np.clip(fr, 1, NT)
    return b[ok] * NT + fr - 1


class Envelope:
    """FFT of the envelope, for event-triggered averages at every circular shift."""

    def __init__(self, env):
        self.env = env
        self.N = env.shape[1]
        self.E = np.fft.rfft(env, axis=1)

    def xcorr(self, frames):
        """C[f, tau] = sum_events env[f, L - tau] (circular), all tau."""
        n = np.bincount(frames, minlength=self.N).astype(float)
        Nn = np.fft.rfft(n)
        return np.fft.irfft(self.E.conj() * Nn[None, :], n=self.N, axis=1)


def strf_from_events(envf, frames, trig, niter=100, p=0.05):
    """STRF = W0/PP * mean pre-event envelope [code] rtwstrfdb.m (W0 = events / duration of the
    triggers). Significance [paper] Methods, Data analysis: event trains circularly shifted at
    regular intervals of N/niter, pixels of all shifted STRFs pooled into a null distribution,
    p < 0.05 (two-tailed, on |pixel|). niter = 100 [claims] D6."""
    n0 = len(frames)
    T = (np.max(trig) - np.min(trig)) / FS
    if n0 == 0:
        z = np.zeros((NF, NLAG))
        return dict(rf=z, sig=z, n0=0, w0=0.0, thr=np.inf, mass_thr=np.inf)
    w0 = n0 / T
    C = envf.xcorr(frames) * (w0 / PP / n0)
    lags = np.arange(NLAG)
    rf = C[:, lags]
    shifts = (np.arange(1, niter) * envf.N) // niter
    null = np.concatenate([C[:, (lags[None, :] - s) % envf.N] for s in shifts], axis=1)
    thr = np.quantile(np.abs(null), 1 - p)
    sig = np.where(np.abs(rf) > thr, rf, 0.0)
    # null distribution of the largest positive cluster mass, for the cluster criterion of
    # subfields() [assumption, see there]
    from scipy import ndimage
    masses = []
    for s in shifts:
        nl_ = C[:, (lags - s) % envf.N]
        pos = nl_ > thr
        lab, n = ndimage.label(pos, structure=np.ones((3, 3)))
        masses.append(ndimage.sum(nl_, lab, range(1, n + 1)).max() if n else 0.0)
    mass_thr = float(np.quantile(masses, 0.95))
    return dict(rf=rf, sig=sig, n0=n0, w0=w0, thr=thr, mass_thr=mass_thr)


def strf_analytic_sig(rf, n0, dur, p):
    """[code] significant_strf.m: |rf| > norminv(1 - p/2) sqrt(n0) / (sigma dur)."""
    thr = stats.norm.ppf(1 - p / 2) * np.sqrt(n0) / (np.sqrt(PP) * dur)
    return np.where(np.abs(rf) > thr, rf, 0.0)


def noise_sd(pr, pk, t0, t1, seg=500):
    """D3 reading (b), as implemented here: the baseline noise during the DMR, the pooled
    within-segment s.d. of the 50-ms segments [standard segment length] that hold no detected
    peak. Each segment is taken about its own mean, so slow drifts of the membrane potential
    do not count as noise."""
    p = np.round(pk).astype(int)
    p = p[(p >= t0) & (p < t1)]
    nseg = (t1 - t0) // seg
    has = np.zeros(nseg + 1, bool)
    has[(p - t0) // seg] = True
    X = pr[t0:t0 + nseg * seg].reshape(nseg, seg)[~has[:nseg]]
    return float(np.sqrt(np.mean(X.var(axis=1))))


# ----------------------------------------------------------------------------------------
# STRF measures
# ----------------------------------------------------------------------------------------
OCT_PER_CH = np.log2(40000 / 500) / (NF - 1)   # 0.1003 octave per envelope channel


def faxis_default():
    return 500 * 2 ** (np.arange(NF) * OCT_PER_CH)


def subfields(sig, min_pix=2, rel=0.0, mass_thr=None):
    """Positive subfields of a significant STRF: 8-connected components of significant positive
    pixels with at least `min_pix` pixels [claims] D7 reading (b). At p < 0.05 per pixel about
    5% of pixels pass by chance, in streaks, so a component is kept as a subfield only when its
    mass (sum of its pixel values) exceeds the 95th percentile of the largest component mass of
    the circularly shifted STRFs (`mass_thr`) [assumption: the paper's own null, applied to
    subfields as a cluster test; without it noise components make nearly every STRF
    double-peaked]. Alternative reading: components whose peak is at least `rel` of the STRF's
    largest significant value. Components whose
    frequency spans overlap are merged into one band. Returns bands sorted by peak value, each
    a dict with channel range lo..hi, peak channel and delay, peak value."""
    from scipy import ndimage
    pos = sig > 0
    if not pos.any():
        return []
    lab, nl = ndimage.label(pos, structure=np.ones((3, 3)))
    vmax = sig.max()
    comps = []
    for k in range(1, nl + 1):
        m = lab == k
        if m.sum() < min_pix:
            continue
        v = np.where(m, sig, -np.inf)
        i, j = np.unravel_index(np.argmax(v), v.shape)
        if sig[i, j] < rel * vmax:
            continue
        if mass_thr is not None and sig[m].sum() <= mass_thr:
            continue
        rows = np.nonzero(m.any(axis=1))[0]
        comps.append(dict(lo=rows.min(), hi=rows.max(), ch=i, lag=j, peak=sig[i, j], mask=m))
    comps.sort(key=lambda c: c["lo"])
    bands = []
    for c in comps:
        if bands and c["lo"] <= bands[-1]["hi"]:
            b = bands[-1]
            b["hi"] = max(b["hi"], c["hi"])
            b["mask"] = b["mask"] | c["mask"]
            if c["peak"] > b["peak"]:
                b.update(ch=c["ch"], lag=c["lag"], peak=c["peak"])
        else:
            bands.append(dict(c))
    bands.sort(key=lambda b: -b["peak"])
    return bands


def profile_double(sig, rel=0.5):
    """D9 reading (b): two maxima of the frequency profile (largest significant positive value
    over delay) separated by a dip below half of the smaller maximum; both maxima at least
    `rel` of the largest [assumption, as in subfields]. Returns list of peak channels."""
    P = np.clip(sig, 0, None).max(axis=1)
    if P.max() <= 0:
        return []
    mx = [i for i in range(NF) if P[i] >= rel * P.max()
          and (i == 0 or P[i] > P[i - 1]) and (i == NF - 1 or P[i] >= P[i + 1])]
    mx.sort(key=lambda i: -P[i])
    if len(mx) < 2:
        return mx[:1]
    a = mx[0]
    for b in mx[1:]:
        lo, hi = sorted((a, b))
        if P[lo:hi + 1].min() < 0.5 * min(P[a], P[b]):
            return [a, b]
    return [a]


def half_max_width(v, i):
    """Number of contiguous bins around i with v >= v[i] / 2."""
    h = v[i] / 2
    lo = i
    while lo > 0 and v[lo - 1] >= h:
        lo -= 1
    hi = i
    while hi < len(v) - 1 and v[hi + 1] >= h:
        hi += 1
    return hi - lo + 1


def strf_measures(rf, sig, faxis, cf=None, min_pix=2, mass_thr=None, rel=0.0):
    """BF, bands, bandwidths, latency and duration of one STRF.

    BF [paper] Methods: the frequency of the strongest response; for two bands, the band whose
    peak is closest to the TRF CF when one is given ([paper] Results, Frequency selectivity,
    paragraph 1). Bandwidths in octaves, n channels x 0.1003 octave [standard: a band of one
    channel has the width of one channel]:
      total_a  [claims] D8 (a): from the lowest to the highest channel of the (one or two) bands;
      single_a D8 (a): each band's own extent;
      total_b  D8 (b): frequency profile above half its maximum around the BF channel.
    Latency [claims] D10 (a): delay of the STRF maximum; (b): shortest delay of a significant
    positive pixel of the main band. Duration D10 (a): contiguous significant positive delays at
    the BF channel; (b): delay profile at the BF channel above half its maximum.
    Delays in ms (5 ms bins, delay of bin j = 5 j ms) [code]."""
    out = dict(sig_any=bool((sig > 0).any()))
    bands = subfields(sig, min_pix=min_pix, rel=rel, mass_thr=mass_thr)
    out["sig_sub"] = len(bands) > 0
    out["nbands"] = min(len(bands), 2)
    out["double_b"] = len(profile_double(sig)) == 2
    if not bands:
        return out
    use = bands[:2]
    main = use[0]
    if cf is not None and len(use) == 2:
        main = min(use, key=lambda b: abs(np.log2(faxis[b["ch"]] / cf)))
    out["bf"] = faxis[main["ch"]]
    out["bf_strongest"] = faxis[use[0]["ch"]]
    out["peak_freqs"] = sorted(faxis[b["ch"]] for b in use)
    lo = min(b["lo"] for b in use)
    hi = max(b["hi"] for b in use)
    out["total_a"] = (hi - lo + 1) * OCT_PER_CH
    out["total_a_khz"] = (faxis[hi] - faxis[lo]) / 1000
    out["single_a"] = [(b["hi"] - b["lo"] + 1) * OCT_PER_CH for b in use]
    out["single_main"] = (main["hi"] - main["lo"] + 1) * OCT_PER_CH
    P = np.clip(sig, 0, None).max(axis=1)
    out["total_b"] = half_max_width(P, int(np.argmax(P))) * OCT_PER_CH
    i, j = main["ch"], main["lag"]
    out["lat_a"] = 5.0 * j
    out["lat_b"] = 5.0 * np.nonzero(main["mask"].any(axis=0))[0].min()
    row = sig[i] > 0
    a = b = j
    while a > 0 and row[a - 1]:
        a -= 1
    while b < NLAG - 1 and row[b + 1]:
        b += 1
    out["dur_a"] = 5.0 * (b - a + 1)
    out["dur_b"] = 5.0 * half_max_width(np.clip(rf[i], 0, None), j)
    return out


def rtf_best_mod(strf, tm_max=40.0, sm_max=4.0, bandpass="a"):
    """bTMF (Hz) and bSMF (cyc/oct) from the ripple transfer function, |2-D FFT| of the STRF
    [paper] Methods; the temporal MTF is the RTF summed over spectral modulation, the spectral
    MTF summed over temporal modulation [paper] Methods, positive and negative modulations
    folded together [claims] D11. Only modulations the DMR holds (|TM| <= 40 Hz,
    |SM| <= 4 cyc/oct, [paper] Methods, Stimuli) are summed and searched [standard]; the native
    FFT grid (5 Hz, 0.156 cyc/oct) is used, with the 3 dB cutoff interpolated linearly.
    Bandpass, [claims] D11 reading (a): the maximum is away from zero, best = the peak; else
    lowpass, best = the mean of 0 and the 3 dB cutoff (where the MTF falls below max / sqrt 2)
    [paper] Methods. Reading (b): bandpass when the value at zero is > 3 dB below the maximum."""
    R = np.abs(np.fft.fft2(strf))
    sm = np.fft.fftfreq(strf.shape[0], d=OCT_PER_CH)
    tm = np.fft.fftfreq(strf.shape[1], d=DT_ENV)
    R = R[np.abs(sm) <= sm_max + 1e-9][:, np.abs(tm) <= tm_max + 1e-9]
    sm = sm[np.abs(sm) <= sm_max + 1e-9]
    tm = tm[np.abs(tm) <= tm_max + 1e-9]
    tmtf = R.sum(axis=0)
    smtf = R.sum(axis=1)

    def fold(m, ax):
        x = np.unique(np.round(np.abs(ax), 9))
        y = np.array([m[np.isclose(np.abs(ax), v)].mean() for v in x])
        return x, y

    def best(x, y):
        k = int(np.argmax(y))
        bp = (k > 0) if bandpass == "a" else (y[0] < y[k] / np.sqrt(2))
        if bp:
            return float(x[k])
        h = y.max() / np.sqrt(2)
        j = k
        while j < len(y) - 1 and y[j + 1] >= h:
            j += 1
        if j == len(y) - 1:
            return float(x[-1] / 2)
        cut = x[j] + (y[j] - h) / (y[j] - y[j + 1]) * (x[j + 1] - x[j])
        return float(cut / 2)

    xt, yt = fold(tmtf, tm)
    xs, ys = fold(smtf, sm)
    return best(xt, yt), best(xs, ys)


# ----------------------------------------------------------------------------------------
# Nonlinearity and feature selectivity
# ----------------------------------------------------------------------------------------
def projections(envf, strf):
    """z[L] = sum_{f, lag} strf[f, lag] env[f, L - lag] for every frame L
    [code] ripple_spet_strf_to_projection.m."""
    k = np.zeros((NF, envf.N))
    k[:, :NLAG] = strf
    K_ = np.fft.rfft(k, axis=1)
    return np.fft.irfft((envf.E * K_).sum(axis=0), n=envf.N)


def ringach_malone(x, A, th, s):
    """[code] ringach_malone_func.m (with its exp(-(x - theta)^2 / sqrt(2) / sigma^2) term)."""
    return (A * (x - th) / 2) * (1 + special.erf((x - th) / s / np.sqrt(2))) + \
        (A * s / np.sqrt(2 * np.pi)) * np.exp(-(x - th) ** 2 / np.sqrt(2) / s ** 2)


def nonlinearity(envf, strf, frames, trig, rng, nbins=15, nstarts=50):
    """[code] fio_projection_to_nonlinearity.m, fio_projection_bins.m and fio_to_fio_fit.m:
    projections of every analysed frame (prior) and the event locator; x in s.d. units of the
    prior; 15 equal bins from min to max; P(event|x) = P(event) P(x|event) / P(x); fit of the
    Ringach-Malone function to P(event|x)/dt by least squares from 50 random starts
    a0 = [mean(fx) 1 1] * rand, keeping the lowest normalized m.s.e. Threshold = theta,
    transition = sigma."""
    lo, hi = NT, (len(np.asarray(trig).ravel()) - 2) * NT   # blocks 2 .. NTrig-2 (1-based)
    z = projections(envf, strf)[lo:hi]
    loc = np.bincount(frames, minlength=envf.N)[lo:hi].astype(float)
    if z.std() == 0 or loc.sum() == 0:
        return dict(theta=np.nan, sigma=np.nan, nmse=np.nan)
    x = (z - z.mean()) / z.std()
    edges = np.linspace(x.min(), x.max(), nbins + 1)
    idx = np.clip(np.searchsorted(edges, x, side="right") - 1, 0, nbins - 1)
    px = np.bincount(idx, minlength=nbins) / len(x)
    pxs = np.bincount(idx, weights=loc, minlength=nbins) / loc.sum()
    pspk = loc.sum() / len(loc)
    with np.errstate(divide="ignore", invalid="ignore"):
        pspkx = np.where(px > 0, pspk * pxs / px, 0.0)
    xb = (edges[:-1] + edges[1:]) / 2
    fx = pspkx / DT_ENV
    best = None
    for _ in range(nstarts):
        a0 = np.array([fx.mean(), 1.0, 1.0]) * rng.random()
        try:
            res = optimize.least_squares(lambda a: ringach_malone(xb, *a) - fx, a0, method="lm")
        except Exception:
            continue
        r = ringach_malone(xb, *res.x) - fx
        nmse = np.mean(r ** 2) / np.var(fx)
        if np.isfinite(nmse) and (best is None or nmse < best[0]):
            best = (nmse, res.x)
    if best is None:
        return dict(theta=np.nan, sigma=np.nan, nmse=np.nan)
    return dict(theta=float(best[1][1]), sigma=float(best[1][2]), gain=float(best[1][0]),
                nmse=float(best[0]), xb=xb, fx=fx)


def fsi(envf, sig, frames, trig, rng, nrand=10000):
    """Feature selectivity index [code] calculate_whole_cell_fsi.m (get_fsi_mono, rtwstrfdbvar,
    fsi): for each event, the correlation coefficient between the significant STRF pixels and
    the pre-event envelope at those pixels; the same for 10,000 random times; CDFs of both
    over bins -3:0.0626:1; FSI = sum(CDFr - CDF) / sum(CDFr - CDFideal). The CDF is the
    cumulative sum of the normalized histogram (the code integrates it by FFT, intfft)."""
    pix = np.nonzero(sig != 0)
    if len(pix[0]) < 2 or len(frames) == 0:
        return np.nan
    w = sig[pix]
    trig = np.asarray(trig).ravel()
    lo, hi = NT, (len(trig) - 2) * NT
    rnd = rng.integers(lo, hi, nrand)

    def corr(fr):
        fr = fr[(fr >= NLAG) & (fr < envf.N)]
        seg = envf.env[pix[0][None, :], fr[:, None] - pix[1][None, :]]
        a = seg - seg.mean(1, keepdims=True)
        b = w - w.mean()
        return (a @ b) / (np.sqrt((a ** 2).sum(1)) * np.sqrt((b ** 2).sum()) + 1e-300)

    bins = np.arange(-3, 1 + 1e-9, 0.0626)
    edges = np.concatenate([[-np.inf], (bins[:-1] + bins[1:]) / 2, [np.inf]])
    def cdf(p):
        h = np.histogram(p, edges)[0].astype(float)
        c = np.cumsum(h / h.sum())
        return (c - c.min()) / (c.max() - c.min())
    C, Cr = cdf(corr(np.asarray(frames))), cdf(corr(rnd))
    Ci = np.zeros(len(bins))
    Ci[-1] = 1
    return float(np.sum(Cr - C) / np.sum(Cr - Ci))


# ----------------------------------------------------------------------------------------
# Pure tones
# ----------------------------------------------------------------------------------------
PRE_MS = 50       # [claims] D3: the baseline for tones is the trace before each tone onset;
                  # 50 ms [standard]
ONSET_MS = (5, 50)  # [paper] Methods, Data analysis: onset latency 5-50 ms
RESP_MS = 100     # window for the PSP peak and spikes after onset [assumption: the onset must
                  # fall in 5-50 ms; the peak follows it, rise times are ~30 ms (Results)]


def tone_analysis(raw, trig, tone_freq, tone_atten, spike_amp_cut=None, sd_reading="pooled"):
    """TRF of one current-clamp tone recording.

    Each of the 360 triggers marks a tone onset; row j of the stimulus presentation order
    gives tone j's frequency and attenuation [code] plot_tuning_curve.m; level = 70 dB SPL -
    attenuation [code] (attenuation 0 to 70 dB, 'from attenuation 0 ... to 70 dB') and
    [paper] Methods, Stimuli (0 to 70 dB SPL).
    Spikes: peakfinder events of raw - smooth(raw) [code], above the spike cut (D1 (a), as for
    the DMR), one per tone [paper] Methods. A tone's PSP response: the trace minus its 50-ms
    pre-tone mean first exceeds 4 x the baseline s.d. 5 to 50 ms after onset [paper] Methods.
    Baseline s.d. readings: 'pooled', the s.d. of all pre-tone samples about each tone's own
    pre-tone mean; 'pertone', each tone's own pre-tone s.d."""
    fs = FS
    trig = np.asarray(trig, int).ravel()
    pk, mg, pr = detect_events(raw, PEAK_SEL_CC)
    cut = spike_cut_gap(mg) if spike_amp_cut is None else spike_amp_cut
    spk = np.round(pk[mg > cut]).astype(int)
    npre = PRE_MS * fs // 1000
    n = len(trig)
    pre = np.stack([raw[t - npre:t] for t in trig])
    pre_mean = pre.mean(1)
    if sd_reading == "pooled":
        sd = np.full(n, np.sqrt(np.mean(pre.var(1))))
    else:
        sd = pre.std(1)
    w = RESP_MS * fs // 1000
    post = np.stack([raw[t:t + w] for t in trig]) - pre_mean[:, None]
    # spikes clipped out of the PSP trace: values above the spike threshold set to the median
    # filtered trace over 3 ms [standard: amplitudes and kinetics are of PSPs]
    from scipy.ndimage import median_filter
    has_spk = np.array([np.any((spk >= t + ONSET_MS[0] * fs // 1000) & (spk < t + w)) for t in trig])
    above = post > (4 * sd)[:, None]
    first = np.where(above.any(1), above.argmax(1), -1)
    lat = first / fs * 1000
    resp = (first >= 0) & (lat >= ONSET_MS[0]) & (lat <= ONSET_MS[1])
    freq = np.asarray(tone_freq, float)
    level = 70 - np.asarray(tone_atten, float)
    return dict(freq=freq, level=level, resp=resp, spike=has_spk & resp, post=post,
                has_spk=has_spk, lat=lat, sd=sd, pre_mean=pre_mean, cut=cut, nspk=len(spk))


def psp_amp_kinetics(post, resp, spike):
    """Per responsive tone without spikes [claims] D16 (kinetics on PSPs without spikes): peak
    amplitude in the 100-ms window, 10-90% rise time before the peak, and 90-10% decay time
    after it, the decay followed up to 250 ms when the trace is given that long."""
    amps, rises, decays = [], [], []
    for k in np.nonzero(resp & ~spike)[0]:
        y = post[k]
        i = int(np.argmax(y))
        a = y[i]
        if a <= 0:
            continue
        r10 = np.nonzero(y[:i + 1] < 0.1 * a)[0]
        r90 = np.nonzero(y[:i + 1] >= 0.9 * a)[0]
        if len(r10) and len(r90):
            rises.append((r90[0] - r10[-1]) / FS * 1000)
        amps.append(a)
    return np.array(amps), np.array(rises)


def trf_summary(t, region="a", bw="a"):
    """CF, threshold level, bandwidth30 (PSP and spike), NDR [paper] Methods:
    CF = the frequency with a response at the lowest level (several at that level: the one
    with the largest response [standard]); bandwidth30 30 dB above that level [paper] Methods,
    Stimuli. [claims] D15 readings: region (a) the responsive tones, (b) all tones inside the
    outline (between the lowest and highest responsive frequency at each level from threshold
    up); bandwidth (a) log2(highest / lowest responsive frequency) at threshold + 30 dB, (b)
    the contiguous responsive range around the CF at that level. NDR = tones with a spike over
    tones with a PSP, within the region, one spike per tone [paper] Methods."""
    f, L, r, s = t["freq"], t["level"], t["resp"], t["spike"]
    out = dict(cf=np.nan, thr=np.nan, bw_psp=np.nan, bw_spk=np.nan, ndr=np.nan,
               bw_psp_khz=np.nan, bw_spk_khz=np.nan, n_resp=int(r.sum()))
    if not r.any():
        return out
    thr = L[r].min()
    atthr = np.nonzero(r & (L == thr))[0]
    k = atthr[np.argmax(t["post"][atthr].max(1))]
    cf = f[k]
    out.update(cf=cf, thr=thr)
    if region == "a":
        reg = r.copy()
    else:
        reg = np.zeros_like(r)
        for lv in np.unique(L[L >= thr]):
            m = r & (L == lv)
            if m.any():
                reg |= (L == lv) & (f >= f[m].min()) & (f <= f[m].max())
    npsp = (r & reg).sum()
    out["ndr"] = (t["has_spk"] & r & reg).sum() / npsp if npsp else np.nan
    lv = thr + 30
    freqs = np.unique(f)

    def width(mask):
        m = mask & (L == lv)
        if not m.any():
            return np.nan, np.nan
        fr = np.sort(f[m])
        if bw == "a":
            lo, hi = fr.min(), fr.max()
        else:
            on = np.isin(freqs, fr)
            c = int(np.argmin(np.abs(np.log2(freqs / cf))))
            if not on[c]:
                c = int(np.argmin(np.where(on, np.abs(np.log2(freqs / cf)), np.inf)))
            a = b = c
            while a > 0 and on[a - 1]:
                a -= 1
            while b < len(freqs) - 1 and on[b + 1]:
                b += 1
            lo, hi = freqs[a], freqs[b]
        return np.log2(hi / lo), (hi - lo) / 1000

    out["bw_psp"], out["bw_psp_khz"] = width(r)
    out["bw_spk"], out["bw_spk_khz"] = width(t["has_spk"] & r)
    return out


# ----------------------------------------------------------------------------------------
# One pass over data.tar.gz
# ----------------------------------------------------------------------------------------
def classify(path):
    """Kind of recording from its path in data.tar.gz."""
    if "/pure_tones/" in path:
        return "tones"
    if "/Main/DMR/" in path:
        return "cc_dmr"
    if "reliability_for_suppl_Fig2" in path:
        return "supp2"
    if "intensity_test_for_suppl_Fig3" in path:
        return "supp3"
    if "/excitation_DMR/" in path:
        return "vc_exc"
    if "/inhibition_DMR/" in path:
        return "vc_inh"
    return "other"


def reduce_dmr(raw, trig, kind, proc=None):
    """Reduce one DMR recording to its events and baseline measures. Events are detected on
    the processed trace `proc` (the authors' derived data) when given."""
    trig = np.asarray(trig, int).ravel()
    t0, t1 = int(trig[0]), int(trig[-1])
    out = dict(trig=trig, n=len(raw), rest=float(np.median(raw[t0:t1])),
               pre_median=float(np.median(raw[:t0])))
    if kind.startswith("vc"):
        sign = -1 if kind == "vc_exc" else 1
        for sel in PEAK_SEL_VC:
            pk, mg, pr = detect_events(raw, sel, sign=sign, pr=proc)
            a = mg   # magnitude: peakfinder ran on sign * processed
            out[f"pk{int(sel)}"] = pk
            out[f"amp{int(sel)}"] = a
            out[f"noise{int(sel)}"] = noise_sd(pr, pk, t0, t1)
            out[f"pre{int(sel)}"] = float(np.std(pr[:t0]))
        return out
    pk, mg, pr = detect_events(raw, PEAK_SEL_CC, pr=proc)
    out.update(pk=pk, amp=mg, vpeak=raw[np.round(pk).astype(int)],
               noise=noise_sd(pr, pk, t0, t1), pre=float(np.std(pr[:t0])),
               quiet=baseline_sd(pr, pk, t0, "quiet"),
               dvdt=spike_mask_dvdt(raw, pk))
    return out


def stream_data(log=print):
    """One pass over data.tar.gz. Tone recordings are kept as float32 traces; DMR recordings
    are reduced to events as they load. For each folder, the processed file is compared with
    raw - smooth(raw, 1e5) (the data descriptor's recipe), and every response trace is hashed
    to find recordings deposited twice."""
    import hashlib
    rec, pending = {}, {}
    for name, b in stream_tar("data.tar.gz", lambda n: n.endswith(".mat")):
        d = loadmat_bytes(b)
        del b
        folder, fname = name.rsplit("/", 1)
        fid = fname.split("_")[0]
        kind = classify(name)
        key = (kind, folder)
        is_proc = fname.endswith("_processed.mat")
        sig = np.asarray(d["response" if is_proc else "response_signal"], float).ravel()
        trig = np.asarray(d["trigger"]).ravel()
        r = rec.setdefault(key, dict(kind=kind, folder=folder, file=fid,
                                     fs=int(np.asarray(d["fs"]).ravel()[0])))
        r["md5_" + ("processed" if is_proc else "raw")] = hashlib.md5(
            sig.astype(np.float32).tobytes()).hexdigest()
        if kind == "tones":
            r.update(raw=sig.astype(np.float32), trig=trig)
            continue
        if key not in pending:
            pending[key] = (is_proc, sig, trig)
            continue
        other_is_proc, other, other_trig = pending.pop(key)
        raw, pr = (other, sig) if is_proc else (sig, other)
        dd = np.abs(pr - (raw - matlab_smooth(raw)))
        r["proc_maxdiff"], r["proc_ndiff"] = float(dd.max()), int((dd > 0.01).sum())
        r["trig_proc_equal"] = bool(np.array_equal(np.ravel(trig), np.ravel(other_trig)))
        r.update(reduce_dmr(raw, trig, kind, proc=pr))
        log(f"{kind} {fid} events reduced")
    return list(rec.values())


# ----------------------------------------------------------------------------------------
# Per-neuron analysis
# ----------------------------------------------------------------------------------------
MAIN = dict(sd="noise", spike="gap", modality="kde", amp="proc")


def split_events(r, cfg=MAIN, k_sd=4.0):
    """Classify the events of one current-clamp DMR recording.
    Spikes per [claims] D1 ('gap' reading (a), 'dvdt' reading (b)). Non-spiking events below
    k_sd x the baseline s.d. are dropped [paper] Results, Spectrotemporal receptive fields,
    paragraph 3 (4 x s.d.); s.d. per D3 ('noise' (b) as implemented in noise_sd, 'quiet' (b)
    with 50-ms exclusion and slow drifts kept, 'pre' (a)). Amplitudes per D2 ('proc', the
    code's peakfinder magnitude above the 10-s running mean; 'rest', peak membrane potential
    minus the median potential during the DMR). Large and small PSPs split at the trough of a
    bimodal histogram, else at the median [paper] Results, paragraph 2; bimodality per D4
    ('kde' (a), 'dip' (b))."""
    amp = r["amp"] if cfg["amp"] == "proc" else r["vpeak"] - r["rest"]
    if cfg["spike"] == "gap":
        sp = r["amp"] > spike_cut_gap(r["amp"])
    else:
        sp = r["dvdt"].copy()
    sd = r[cfg["sd"]]
    ns = ~sp & (amp > k_sd * sd)
    x = amp[ns]
    trough = None
    if cfg["modality"] == "kde":
        trough = bimodal_trough(x) if len(x) >= 10 else None
        bimodal = trough is not None
    else:
        bimodal = len(x) >= 10 and dip_test_p(x) < 0.05
        if bimodal:
            trough = bimodal_trough(x, min_rel=0.0)
            if trough is None:
                trough = float(np.median(x))
    cut = trough if trough is not None else (float(np.median(x)) if len(x) else np.inf)
    large = ns & (amp > cut)
    small = ns & (amp <= cut)
    return dict(spike=sp, large=large, small=small, all=sp | ns, amp=amp, bimodal=bimodal,
                cut=cut, sd=sd)


def analyse_strfs(r, envf, faxis, ev, cf=None, classes=("spike", "large", "small", "all"),
                  sig_reading="shuffle", min_pix=2, cluster=True, rel=0.0, key=None):
    """STRF and measures for each event class. sig_reading 'shuffle' [paper] Methods
    (p < 0.05 against circularly shifted trains), or 'analytic' [code] plot_strf_single.m
    (p = 0.005, significant_strf.m)."""
    trig = r["trig"]
    out = {}
    for c in classes:
        fr = event_frames(r[key or "pk"][ev[c]], trig)
        s = strf_from_events(envf, fr, trig)
        if sig_reading == "analytic" and s["n0"] > 0:
            s["sig"] = strf_analytic_sig(s["rf"], s["n0"], (trig[-1] - trig[0]) / FS, 0.005)
        m = strf_measures(s["rf"], s["sig"], faxis, cf=cf, min_pix=min_pix,
                          mass_thr=s["mass_thr"] if cluster else None, rel=rel)
        m["n0"] = s["n0"]
        m["rate"] = s["w0"]
        m["frames"] = fr
        m["rf"], m["sig"] = s["rf"], s["sig"]
        out[c] = m
    return out


def add_rtf_nl_fsi(strfs, envf, trig, rng, classes, rtf=True, nl=True, do_fsi=True):
    """bTMF, bSMF (readings D11), nonlinearity threshold and transition (D12, on the
    significant STRF, reading (a); full STRF reading (b)) and FSI (D13)."""
    for c in classes:
        m = strfs[c]
        if m["n0"] == 0 or not m["sig"].any():
            continue
        if rtf:
            m["btmf"], m["bsmf"] = rtf_best_mod(m["sig"])
            m["btmf_full"], m["bsmf_full"] = rtf_best_mod(m["rf"])
            m["btmf_b"], m["bsmf_b"] = rtf_best_mod(m["sig"], bandpass="b")
        if nl:
            n = nonlinearity(envf, m["sig"], m["frames"], trig, rng)
            m["theta"], m["trans"], m["nl_nmse"] = n["theta"], n["sigma"], n["nmse"]
            n2 = nonlinearity(envf, m["rf"], m["frames"], trig, rng)
            m["theta_full"], m["trans_full"] = n2["theta"], n2["sigma"]
        if do_fsi:
            m["fsi"] = fsi(envf, m["sig"], m["frames"], trig, rng)
    return strfs


def cc_neurons(recs, envf, faxis, cfg=MAIN, cfs=None, cluster=True, rel=0.0, min_pix=2,
               sig_reading="shuffle"):
    """Events and STRF measures for every current-clamp DMR neuron (no RTF, nonlinearity or
    FSI; see add_rtf_nl_fsi). cfs maps a DMR file id to the TRF CF of the same neuron."""
    out = []
    for r in recs:
        ev = split_events(r, cfg)
        cf = None if cfs is None else cfs.get(r["file"])
        st = analyse_strfs(r, envf, faxis, ev, cf=cf, cluster=cluster, rel=rel,
                           min_pix=min_pix, sig_reading=sig_reading)
        dur = (r["trig"][-1] - r["trig"][0]) / FS
        out.append(dict(file=r["file"], folder=r["folder"], ev=ev, strf=st,
                        n_events={c: int(ev[c].sum()) for c in ev if c in
                                  ("spike", "large", "small", "all")},
                        rate={c: st[c]["n0"] / ((len(r["trig"]) - 3) * NT * DT_ENV) for c in st},
                        dur=dur, rest=r["rest"]))
    return out


def vc_events(r, sel=20, k_sd=3.0, sd="noise"):
    """Voltage-clamp events: peakfinder on the inverted processed current for excitation
    (inward currents at about -80 mV) and on the processed current for inhibition (outward at
    about 0 mV) [assumption: the paper's 'peak currents' of each sign], selectivity `sel` pA
    [paper] Methods (~20-40 pA), kept above k_sd = 3 x the baseline s.d. [paper] Results,
    DMR-evoked currents, paragraph 1 (s.d. per D3 as for current clamp)."""
    a = r[f"amp{int(sel)}"]
    s = r[f"noise{int(sel)}"] if sd == "noise" else r[f"pre{int(sel)}"]
    keep = a > k_sd * s
    return keep, a, s
