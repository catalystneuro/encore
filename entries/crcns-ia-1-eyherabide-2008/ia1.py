"""Loading and burst measures for CRCNS data set ia-1 (locust auditory receptors, Data1).

Eyherabide, Rokem, Herz & Samengo (2008), Frontiers in Computational Neuroscience,
doi:10.3389/neuro.10.003.2008.

The data set is one zip file in the public CRCNS bucket, streamed with fsspec and read in
place with zipfile; nothing is written to disk. CRCNS data sets are not versioned: the MD5 sum
of the zip in the data set's checksums.md5 (`ZIP_MD5`) is checked against the object's ETag
when the zip is opened, so that a change of the file is detected.

Data1 holds one directory per experiment (`03-04-23-aa`), each with two stimuli (`sig1`,
`sig2`). `*_spikes.dat` holds the spike times (microseconds from the stimulus trigger) of the
repeated 1 s presentations, trial after trial, each trial behind a `#` header; `cell.dat` names
the two stimulus files and the intensity they were played at (the maximal intensity, the mean
plus 3 SD, data descriptor); `singlecells.txt` lists the experiments made on one cell. The
stimulus files hold the AM signal in volts at 20 kHz for 10 s; `stimtodB.m` converts them to dB.

Where the parameters come from (claims file, opening comment, and the paper's Methods):

- `DT = 0.1 ms` bins and the analysis window 200 to 1000 ms: Methods, Burst identification,
  paragraph 2, and Electrophysiology and stimulus design, paragraph 5 ("the first 200 msec of
  each trial were discarded").
- The burst test (`burst_limit`): Methods, Burst identification, paragraphs 4 to 6: a first peak
  of C_s below 5 ms, bounded on its right by a minimum below 1.25 / cutoff that differs from
  the maximum by more than the sum of their error bars, Delta = sigma / sqrt(N). The readings
  of the open details (1) to (3) of the claims file are arguments: `peak` "a" (first local
  maximum for tau > 0), "b" (largest value in 0 < tau < 5 ms) or "c" (below); `minimum` "a"
  (first local minimum after the peak that differs significantly from the maximum) or "b" (lowest value
  between the peak and 1.25 / cutoff, required to differ significantly); `nmode` "a" (N the
  number of product terms at each tau) or "b" (N the number of trials), as the claims file
  gives them, and "c" (sigma the SD over trials of each trial's time-averaged C_s, N the number
  of trials), a third reading of "C_s (tau) can be interpreted as an average ... The error bar
  Delta of an average estimated from N samples reads Delta = sigma / sqrt(N)" (paragraph 6),
  added here because C_s is the trial average of per-trial averages. `peak` "c" is reading (a)
  with the refractory plateau left out: at lags below the shortest ISI C_s has no spike pairs
  and is flat, and edge effects there make spurious local maxima, so the search for the first
  local maximum starts at the first lag where C_s exceeds its value at the first lag by more
  than the sum of their error bars (added after verification, round 1).
- Bursts (`bursts_of_trial`): consecutive spikes whose ISIs are within the domain of the first
  peak, 0 to the position of the minimum (paragraph 7); a burst is dated by its first spike.
"""

from __future__ import annotations

import re
import zipfile
from dataclasses import dataclass, field

import fsspec
import numpy as np
import requests

CRCNS_ID = "ia-1"
VERSION = "unversioned"
DATASET_DOI = "10.6080/K0BG2KWB"
BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com"
ZIP_URL = f"{BUCKET}/{CRCNS_ID}/crcns-ia1.zip"
ZIP_MD5 = "f0740514fabc6995fe54b2a361b6c763"   # crcns-ia1.zip in ia-1/checksums.md5
ROOT = "crcns-ia1/Data1/"

DT = 1e-4                  # s, 0.1 ms bins (Methods, Burst identification)
T_TRIAL = 1.0              # s, stimulus length
T0, T1 = 0.2, 1.0          # s, analysis window (Methods: first 200 ms discarded)
STIM_RATE = 20000.0        # Hz, stimulus files (data descriptor)
PEAK_MAX = 5e-3            # s, first peak below 5 ms (Methods)
MIN_FACTOR = 1.25          # minimum below 1.25 / cutoff (Methods)

# The seven protocols of Table 1, (SD dB, cutoff Hz) -> protocol number.
PROTOCOLS = {(6, 200): 1, (3, 200): 2, (12, 200): 3, (6, 25): 4, (6, 100): 5, (6, 400): 6, (6, 800): 7}


def open_zip() -> zipfile.ZipFile:
    """Open the data set's zip in place, after checking its ETag against checksums.md5."""
    etag = requests.head(ZIP_URL, timeout=60).headers["ETag"].strip('"')
    if etag != ZIP_MD5:
        raise RuntimeError(f"crcns-ia1.zip has changed: ETag {etag}, checksums.md5 {ZIP_MD5}")
    return zipfile.ZipFile(fsspec.open(ZIP_URL, block_size=2**20).open())


@dataclass
class Session:
    """One cell (experiment directory) in one stimulus condition."""
    exp: str                  # experiment directory, e.g. 03-04-23-aa
    sig: int                  # 1 or 2
    stimulus: str             # stimulus file name without .dat, from cell.dat
    intensity: float          # dB, maximal intensity from cell.dat
    cell_cutoff: float        # Hz, from cell.dat
    trials: list = field(repr=False)   # spike times per trial, s, all spikes of the file
    header: dict = field(default_factory=dict)   # first trial's header, when an OEL header
    offline: bool = False     # off-line spike detection (OFFOEL header)

    @property
    def sd_cut(self):
        m = re.fullmatch(r"(?:gauss_)?st(\d+)_co(\d+)", self.stimulus)
        return (int(m.group(1)), int(m.group(2))) if m else None

    @property
    def protocol(self):
        return PROTOCOLS.get(self.sd_cut)

    @property
    def cutoff(self):
        return self.sd_cut[1] if self.sd_cut else self.cell_cutoff

    @property
    def name(self):
        return f"{self.exp}_sig{self.sig}"

    @property
    def n_trials(self):
        return len(self.trials)


def parse_spikes(text: str):
    """Split a *_spikes.dat file into trials (s) and return the first header's fields.

    Each trial starts with a block of `#` lines; spike times are in microseconds."""
    trials, header, current, in_header = [], {}, None, False
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("#"):
            if not in_header:
                current = []
                trials.append(current)
                in_header = True
            if len(trials) == 1 and ":" in line:
                k, v = line[1:].split(":", 1)
                header[k.strip()] = v.strip()
            continue
        in_header = False
        if line:
            current.append(float(line) * 1e-6)
    return [np.asarray(t) for t in trials], header


def parse_cell(text: str):
    """The two stimuli of an experiment from cell.dat: {sig: (name, intensity dB, cutoff Hz)}."""
    out = {}
    for m in re.finditer(r"Signal\s+(\d)\s*Name:\s*(\S+)\s*Intensity:\s*([\d.]+)\s*dB\s*"
                         r"Cut off frequency:\s*([\d.]+)", text):
        out[int(m.group(1))] = (m.group(2).removesuffix(".dat"), float(m.group(3)), float(m.group(4)))
    return out


def load_sessions(z: zipfile.ZipFile):
    """Every Data1 session, in directory order."""
    names = z.namelist()
    exps = sorted({n.split("/")[2] for n in names
                   if n.startswith(ROOT) and n.count("/") >= 3 and n.split("/")[2] != "stimuli"})
    sessions = []
    for exp in exps:
        cell = parse_cell(z.read(f"{ROOT}{exp}/cell.dat").decode("latin1"))
        for sig in (1, 2):
            path = f"{ROOT}{exp}/{exp}_sig{sig}_spikes.dat"
            if path not in names:
                continue
            text = z.read(path).decode("latin1")
            trials, header = parse_spikes(text)
            stim, inten, cut = cell[sig]
            sessions.append(Session(exp, sig, stim, inten, cut, trials, header,
                                    offline="OFFOEL" in text[:200]))
    return sessions


def load_singlecells(z: zipfile.ZipFile):
    """Rows of singlecells.txt as lists of experiment names (one row per cell)."""
    rows = []
    for line in z.read(f"{ROOT}singlecells.txt").decode("latin1").splitlines():
        parts = line.split()
        if parts:
            date = parts[0][:-2]
            rows.append([parts[0]] + [date + p for p in parts[1:]])
    return rows


def stimulus_file(stimulus: str) -> str:
    """The stimulus file a cell.dat name refers to (`st6_co200` is `gauss_st6_co200`)."""
    return stimulus if stimulus.startswith(("gauss", "lmd")) else "gauss_" + stimulus


def load_stimulus_shape(z: zipfile.ZipFile, stimulus: str, duration=1.05):
    """The AM signal in dB relative to its maximum over the whole 10 s file, at 20 kHz, over the
    first `duration` s. stimtodB.m computes 20 log10(v / 2e-5) and shifts it so that its maximum
    is the intensity played; adding the session's intensity (`Session.intensity`, from cell.dat)
    gives the stimulus in dB SPL. Reads 1.05 s so that windows up to 15 ms after a burst near the
    end of the 1 s trial are covered (the file is 10 s long)."""
    data = np.loadtxt(z.open(f"{ROOT}stimuli/{stimulus_file(stimulus)}.dat"))
    db = 20 / np.log(10) * np.log(data[:, 1] / 2.0e-5)
    keep = data[:, 0] * 1e-6 < duration
    return db[keep] - db.max()


# ---------------------------------------------------------------- spike-train measures

def binned(trials, t0=T0, t1=T1, dt=DT):
    """Spike counts per trial and bin over [t0, t1): an (n_trials, n_bins) uint8 array."""
    nb = int(round((t1 - t0) / dt))
    out = np.zeros((len(trials), nb), dtype=np.uint8)
    for i, t in enumerate(trials):
        k = np.floor((t[(t >= t0) & (t < t1)] - t0) / dt).astype(int)
        np.add.at(out[i], k, 1)
    return out


def trial_rates(trials, t0=T0, t1=T1):
    """Firing rate of each trial over [t0, t1), Hz."""
    return np.array([np.sum((t >= t0) & (t < t1)) / (t1 - t0) for t in trials])


def correlation(trials, max_lag, t0=T0, t1=T1, dt=DT):
    """C_s(tau) of Eq. 1 for tau = 0, dt, ..., max_lag, with its error bar.

    rho is 1/dt in a bin with a spike and 0 otherwise; the bar is the trial and time average of
    (rho(t) - rbar)(rho(t + tau) - rbar) over the pairs inside the window. Returns tau (s), C_s
    (Hz^2), the SD of the product terms, their number at each tau (n_trials * (n_bins - k)), the
    number of trials, and the SD over trials of each trial's time-averaged products."""
    x = (binned(trials, t0, t1, dt) > 0).astype(float) / dt
    n_tr, nb = x.shape
    rbar = x.mean()
    y = x - rbar
    nlag = int(round(max_lag / dt)) + 1
    # Sums of products and squared products for every lag, by FFT over time, summed over trials.
    nfft = 1 << int(np.ceil(np.log2(2 * nb)))
    f = np.fft.rfft(y, nfft, axis=1)
    s1 = np.fft.irfft((f.conj() * f).sum(0), nfft)[:nlag]
    f2 = np.fft.rfft(y ** 2, nfft, axis=1)
    s2 = np.fft.irfft((f2.conj() * f2).sum(0), nfft)[:nlag]
    count = n_tr * (nb - np.arange(nlag))
    c = s1 / count
    sd = np.sqrt(np.maximum(s2 / count - c ** 2, 0))
    # Reading (c): each trial's own time average of the products; their SD over trials.
    per_trial = np.fft.irfft(f.conj() * f, nfft, axis=1)[:, :nlag] / (nb - np.arange(nlag))
    sd_trials = per_trial.std(axis=0, ddof=1)
    return np.arange(nlag) * dt, c, sd, count, n_tr, sd_trials


def correlation_error(sd, count, n_tr, sd_trials, nmode):
    """Delta = sigma / sqrt(N) (Methods, Burst identification, paragraph 6) under reading
    "a" (sigma of the product terms, N their number), "b" (the same sigma, N the number of
    trials) or "c" (sigma over trials of each trial's C_s, N the number of trials)."""
    if nmode == "a":
        return sd / np.sqrt(count)
    if nmode == "b":
        return sd / np.sqrt(n_tr)
    return sd_trials / np.sqrt(n_tr)


def burst_limit(trials, cutoff, peak="a", minimum="a", nmode="a", dt=DT):
    """The limiting ISI of a session (s), or 0 when the first peak is not separable.

    Methods, Burst identification: the first peak of C_s must lie below 5 ms; the minimum to its
    right below 1.25 / cutoff; the two must differ by more than the sum of their error bars,
    Delta = sigma / sqrt(N). Readings of the open details are given by `peak`, `minimum` and
    `nmode` (see the module docstring). Also returns the details used."""
    max_lag = max(MIN_FACTOR / cutoff, PEAK_MAX) + 2 * dt
    tau, c, sd, count, n_tr, sd_trials = correlation(trials, max_lag, dt=dt)
    err = correlation_error(sd, count, n_tr, sd_trials, nmode)
    info = dict(tau=tau, c=c, err=err)
    lim_i = int(np.floor(MIN_FACTOR / cutoff / dt + 1e-9))
    pk_i = int(np.floor(PEAK_MAX / dt + 1e-9))
    # The peak, excluding tau = 0 (the self term).
    if peak in ("a", "c"):
        start = 1
        if peak == "c":
            above = [i for i in range(2, min(pk_i, len(c) - 2) + 1) if c[i] - c[1] > err[i] + err[1]]
            if not above:
                return 0.0, info
            start = above[0]
        cand = [i for i in range(start, min(pk_i, len(c) - 2) + 1) if c[i] > c[i - 1] and c[i] >= c[i + 1]]
        if not cand:
            return 0.0, info
        ip = cand[0]
    else:
        ip = 1 + int(np.argmax(c[1:pk_i + 1]))
        if ip == pk_i or c[ip] < c[ip + 1]:        # no maximum inside (0, 5 ms)
            return 0.0, info
    info["peak"] = ip
    sig = lambda j: c[ip] - c[j] > err[ip] + err[j]
    if minimum == "a":
        ims = [j for j in range(ip + 1, min(lim_i, len(c) - 2) + 1)
               if c[j] < c[j - 1] and c[j] <= c[j + 1] and sig(j)]
        if not ims:
            return 0.0, info
        im = ims[0]
    else:
        if lim_i <= ip:
            return 0.0, info
        im = ip + 1 + int(np.argmin(c[ip + 1:lim_i + 1]))
        if not sig(im):
            return 0.0, info
    info["min"] = im
    return im * dt, info


def bursts_of_trial(t, limit):
    """Burst onsets and spike counts n of one trial: consecutive spikes with ISI <= limit form
    one burst, dated by its first spike. With limit 0 every spike is a 1-burst."""
    t = np.sort(t)
    if len(t) == 0:
        return t, np.zeros(0, int)
    new = np.r_[True, np.diff(t) > limit]
    starts = np.flatnonzero(new)
    n = np.diff(np.r_[starts, len(t)])
    return t[starts], n


def bursts(trials, limit, t0=T0, t1=T1):
    """Bursts of every trial whose onset is in [t0, t1): (trial index, onset s, n, spike times).

    Bursts are formed on the whole trial, so a burst that starts before t0 is not cut."""
    out = []
    for i, t in enumerate(trials):
        on, n = bursts_of_trial(t, limit)
        keep = (on >= t0) & (on < t1)
        out.append((np.full(keep.sum(), i), on[keep], n[keep]))
    tr = np.concatenate([o[0] for o in out]) if out else np.zeros(0, int)
    on = np.concatenate([o[1] for o in out]) if out else np.zeros(0)
    n = np.concatenate([o[2] for o in out]) if out else np.zeros(0, int)
    return tr, on, n


def burst_counts(trials, limit, t0=T0, t1=T1):
    """Number of n-bursts for n = 1, 2, ... (index n - 1) with onset in [t0, t1)."""
    _, _, n = bursts(trials, limit, t0, t1)
    return np.bincount(n, minlength=2)[1:]


def average_n(counts):
    """Mean and SD of n under the probability counts / total (Table 1 legend)."""
    n = np.arange(1, len(counts) + 1)
    p = counts / counts.sum()
    m = (p * n).sum()
    return m, np.sqrt((p * (n - m) ** 2).sum())


# ---------------------------------------------------------------- information (Eqs. 3 and 10)

def burst_rates(trials, limit, bin_s, t0=T0, t1=T1):
    """r_n(t): trial-averaged rate of n-burst onsets in bins of `bin_s` over [t0, t1), Hz,
    as a dict n -> array."""
    tr, on, n = bursts(trials, limit, t0, t1)
    return rates_of(on, n, len(trials), bin_s, t0, t1)


def rates_of(on, n, n_trials, bin_s, t0=T0, t1=T1):
    """r_n(t) from burst onsets and sizes pooled over `n_trials` trials, as in `burst_rates`."""
    nb = int(round((t1 - t0) / bin_s))
    k = np.minimum(((on - t0) / bin_s).astype(int), nb - 1)
    out = {}
    for m in np.unique(n):
        out[int(m)] = np.bincount(k[n == m], minlength=nb) / (n_trials * bin_s)
    return out


def circular_shift(tr, on, n_trials, rng, t0=T0, t1=T1):
    """Burst onsets with each trial shifted by its own random offset, wrapped within [t0, t1).
    Each trial keeps its bursts and their spacing but loses their locking to the stimulus, so
    the information computed from the result is the bias of the plug-in estimate (a baseline
    added after the first verification; the paper does not use one)."""
    off = rng.uniform(0, t1 - t0, n_trials)
    return t0 + (on - t0 + off[tr]) % (t1 - t0)


def information(rates, T=T1 - T0):
    """Per n: rbar_n (Hz), I_n(1) in bits per event (reading i: (1/T) times the integral of
    (r_n / rbar_n) log2(r_n / rbar_n)), and I'_n = rbar_n I_n(1) in bits/s (Eq. 10 divided by T).
    Reading ii, Eq. 10 as printed, is I_n(1) times T."""
    out = {}
    for n, r in rates.items():
        rbar = r.mean()
        q = r[r > 0] / rbar
        i1 = (q * np.log2(q)).sum() / len(r)
        out[n] = dict(rbar=rbar, i1=i1, rate=rbar * i1)
    return out


def line_fit(x, y):
    """Least-squares slope, its standard error, and the one- and two-sided p of slope != 0
    (t distribution, len(x) - 2 degrees of freedom; nan below three points)."""
    from scipy import stats
    x, y = np.asarray(x, float), np.asarray(y, float)
    if len(x) < 2:
        return np.nan, np.nan, np.nan, np.nan
    r = stats.linregress(x, y)
    if len(x) < 3:
        return r.slope, np.nan, np.nan, np.nan
    tval = r.slope / r.stderr if r.stderr > 0 else np.inf * np.sign(r.slope)
    p_two = 2 * stats.t.sf(abs(tval), len(x) - 2)
    p_greater = stats.t.sf(tval, len(x) - 2)
    return r.slope, r.stderr, p_greater, p_two


# ---------------------------------------------------------------- Pearson correlations (Eq. 11)

def burst_matrix(trials, limit, t0=T0, t1=T1, dt=DT):
    """n(t) per trial and bin: the spike count of the burst whose first spike is in the bin."""
    nb = int(round((t1 - t0) / dt))
    out = np.zeros((len(trials), nb), dtype=np.int16)
    for i, t in enumerate(trials):
        on, n = bursts_of_trial(t, limit)
        keep = (on >= t0) & (on < t1)
        np.add.at(out[i], ((on[keep] - t0) / dt).astype(int), n[keep])
    return out


def sq_pearson_by_lag(x, max_lag_bins, t_end_bins):
    """Mean over t < t_end_bins of c(t, tau)^2 for each lag 0..max_lag_bins, Eq. 11: the
    Pearson coefficient across trials between bin t and bin t + tau, set to 0 where the
    denominator vanishes (the numerator then vanishes too)."""
    x = x.astype(float)
    xc = x - x.mean(0)
    var = (xc ** 2).mean(0)
    out = np.empty(max_lag_bins + 1)
    for k in range(max_lag_bins + 1):
        a, b = xc[:, :t_end_bins], xc[:, k:k + t_end_bins]
        num = (a * b).mean(0)
        den = np.sqrt(var[:t_end_bins] * var[k:k + t_end_bins])
        c = np.where(den > 0, num / np.where(den > 0, den, 1), 0.0)
        out[k] = (c ** 2).mean()
    return out


# ---------------------------------------------------------------- jitter

def jitter_events_a(onsets_by_trial, t0=T0, t1=T1, dt=DT):
    """Reading (a): events are the peaks of the onset histogram (0.1 ms bins), each event's
    onsets those between the troughs (local minima) on either side. Returns the mean over
    events with at least two onsets of the SD of onset times (s), or nan."""
    allon = np.concatenate(onsets_by_trial) if onsets_by_trial else np.zeros(0)
    if len(allon) < 2:
        return np.nan
    nb = int(round((t1 - t0) / dt))
    h = np.bincount(((allon - t0) / dt).astype(int).clip(0, nb - 1), minlength=nb).astype(float)
    # Troughs: bins where h is not above either neighbour; events are the stretches between.
    trough = np.r_[True, (h[1:-1] <= h[:-2]) & (h[1:-1] <= h[2:]), True]
    seg = np.cumsum(trough)
    k = ((allon - t0) / dt).astype(int).clip(0, nb - 1)
    sds = [allon[seg[k] == g].std(ddof=1) for g in np.unique(seg[k]) if (seg[k] == g).sum() >= 2]
    return np.mean(sds) if sds else np.nan


def jitter_events_b(onsets_by_trial, limit, dt=DT, t0=T0, t1=T1):
    """Reading (b): event centres are the bins of the onset histogram (0.1 ms), taken from the
    highest down; an event is the onsets not yet assigned that fall within the first-peak
    domain (the limiting ISI) centred on the bin, that is within limit / 2 of its centre. Mean
    over events with at least two onsets of their SD (s), or nan."""
    allon = np.sort(np.concatenate(onsets_by_trial)) if onsets_by_trial else np.zeros(0)
    if len(allon) < 2 or limit <= 0:
        return np.nan
    nb = int(round((t1 - t0) / dt))
    k = ((allon - t0) / dt).astype(int).clip(0, nb - 1)
    h = np.bincount(k, minlength=nb)
    free = np.ones(len(allon), bool)
    sds = []
    for b in np.argsort(-h, kind="stable"):
        if h[b] < 2:
            break
        c = t0 + (b + 0.5) * dt
        lo, hi = np.searchsorted(allon, [c - limit / 2, c + limit / 2], side="left")
        idx = np.arange(lo, hi)[free[lo:hi]]
        if len(idx) >= 2:
            sds.append(allon[idx].std(ddof=1))
        free[idx] = False
    return np.mean(sds) if sds else np.nan


# ---------------------------------------------------------------- burst-triggered averages

PRE, POST = 0.025, 0.015     # s, -25 to +15 ms around burst onset (Methods, nBTA ANOVA)


def segments(stim, onsets, pre=PRE, post=POST, rate=STIM_RATE):
    """Stimulus segments (rows) from onset - pre to onset + post, at the stimulus rate."""
    i0 = np.round(onsets * rate).astype(int)
    off = np.arange(-int(round(pre * rate)), int(round(post * rate)))
    return stim[i0[:, None] + off[None, :]], off / rate


def two_way_anova(groups):
    """Two-way ANOVA, factors group and column (frequency bin), for a list of (n_obs, n_cols)
    arrays: each observation has one value per column, so the design is proportional and the
    sums of squares are exact. Returns p of the group main effect and of the interaction."""
    from scipy import stats
    allx = np.concatenate(groups)
    N, F = allx.shape
    G = len(groups)
    m = allx.mean()
    mf = allx.mean(0)
    ss_g = sum(len(g) * F * (g.mean() - m) ** 2 for g in groups)
    ss_f = N * ((mf - m) ** 2).sum()
    ss_cells = sum(len(g) * ((g.mean(0) - m) ** 2).sum() for g in groups)
    ss_int = ss_cells - ss_g - ss_f
    ss_err = sum(((g - g.mean(0)) ** 2).sum() for g in groups)
    df_g, df_int, df_err = G - 1, (G - 1) * (F - 1), N * F - G * F
    ms_err = ss_err / df_err
    p_g = stats.f.sf(ss_g / df_g / ms_err, df_g, df_err)
    p_int = stats.f.sf(ss_int / df_int / ms_err, df_int, df_err) if df_int > 0 else 1.0
    return p_g, p_int


def central_peak(bta, t, search=None):
    """Index of the central maximum of a BTA and of the minima flanking it (the nearest local
    minima on each side, or the window's ends). The maximum is taken over the whole window
    unless `search` gives limits: Methods, "The time tau_n between the maximum of nBTA and
    tau = 0 (burst generation) is the average latency of the n-burst"."""
    w = np.arange(len(t)) if search is None else np.flatnonzero((t >= search[0]) & (t <= search[1]))
    ip = w[np.argmax(bta[w])]
    left = ip
    while left > 0 and bta[left - 1] <= bta[left]:
        left -= 1
    right = ip
    while right < len(bta) - 1 and bta[right + 1] <= bta[right]:
        right += 1
    return ip, left, right


def fwhm(bta, ip, baseline):
    """Full width at half height of the peak at ip above `baseline`, in samples."""
    half = baseline + (bta[ip] - baseline) / 2
    a = ip
    while a > 0 and bta[a - 1] > half:
        a -= 1
    b = ip
    while b < len(bta) - 1 and bta[b + 1] > half:
        b += 1
    return b - a + 1


# ---------------------------------------------------------------- direct method (Strong et al., 1998)

def nsb_entropy(counts_list, K, n_beta=200):
    """NSB entropy estimate (bits; Nemenman, Shafee & Bialek 2002, Nemenman et al. 2004) of each
    histogram in `counts_list` (arrays of the non-zero counts), for K possible words. The
    posterior over the Dirichlet concentration beta under the prior uniform in the expected
    entropy xi(beta) is evaluated on a log grid of beta, and the posterior mean entropy is its
    weighted average."""
    from scipy.special import gammaln, digamma, polygamma
    betas = np.logspace(-6, 4, n_beta)
    dxi = K * polygamma(1, K * betas + 1) - polygamma(1, betas + 1)
    lw = np.log(np.gradient(betas)) + np.log(np.abs(dxi))
    out = np.empty(len(counts_list))
    for j, c in enumerate(counts_list):
        c = np.asarray(c, float)
        N = c.sum()
        kb = K * betas
        ll = (gammaln(kb) - gammaln(N + kb)
              + (gammaln(c[:, None] + betas[None, :]) - gammaln(betas)[None, :]).sum(0))
        s = digamma(N + kb + 1) - ((c[:, None] + betas[None, :]) * digamma(c[:, None] + betas[None, :] + 1)).sum(0) / (N + kb) \
            - (K - len(c)) * betas * digamma(betas + 1) / (N + kb)
        lp = ll + lw
        w = np.exp(lp - lp.max())
        out[j] = (w * s).sum() / w.sum() / np.log(2)
    return out


def direct_information(trials, word_bins, bin_s=4e-4, t0=T0, t1=T1):
    """Information rate (bits/s) of binary words of `word_bins` bins of `bin_s` over [t0, t1):
    total entropy of the words over all times and trials minus the mean over time of the
    entropy of the words at that time across trials, both NSB-corrected, divided by the word
    duration. Words start at every bin."""
    x = (binned(trials, t0, t1, bin_s) > 0).astype(np.int64)
    n_tr, nb = x.shape
    L = word_bins
    words = np.zeros((n_tr, nb - L + 1), dtype=np.int64)
    for j in range(L):
        words = words * 2 + x[:, j:nb - L + 1 + j]
    K = 2 ** L
    _, tot = np.unique(words, return_counts=True)
    h_tot = nsb_entropy([tot], K)[0]
    hists = {}
    for col in words.T:
        _, c = np.unique(col, return_counts=True)
        key = tuple(sorted(c))
        hists[key] = hists.get(key, 0) + 1
    keys = list(hists)
    h = nsb_entropy([np.array(k) for k in keys], K)
    h_noise = sum(hists[k] * hk for k, hk in zip(keys, h)) / words.shape[1]
    return (h_tot - h_noise) / (L * bin_s)
