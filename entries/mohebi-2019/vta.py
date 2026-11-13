"""Loading and measures for CRCNS data set vta-2 (Mohebi et al. 2019).

Mohebi, Pettibone, Hamid, Wong, Vinson, Patriarchi, Tian, Kennedy & Berke (2019), Nature 570,
65-70, doi:10.1038/s41586-019-1235-y. Data set: Mohebi & Berke (2019), CRCNS.org,
doi:10.6080/K0VQ30V9.

The data set is one zip, `vta-2/live/data_and_code.zip`, in the public S3 bucket `crcnsarchive`.
It holds `VTA_data.mat` (MATLAB 7.3, an HDF5 file) with a 29-element struct array `Unit`, one per
identified dopamine cell, and the authors' MATLAB scripts `pelletpermin.m`, `getFiringRate.m` and
`Fig5_replicate.m`. The zip is streamed over range requests (fsspec) and the .mat member is read
into memory; nothing is written to disk. CRCNS data sets are not versioned: the zip's MD5 from the
data set's `checksums.md5` is `ZIP_MD5`, and `zip_etag()` returns the bucket's ETag, which for this
single-part object is the MD5 of its content.

Each unit has `name` (rat, date, tetrode), `session` (rat and date), `FR` (the descriptor's
"session-wide average firing rate"), `meanWave` and `meanLightEvoked` (120 samples by 4 wires) and
`segments`, one per task: `RL` (bandit), `Pav` (Pavlovian), `Laser`, and `Sleep`. Spike times
(`ts`) and event times are in seconds from the start of each segment.

Bandit events (`boxts.event`, 7 rows, one column per attempt) are Light-On, Center-In, Go cue,
Center-Out, Side-In, Side-Out, Food-Port-In: the row names are those of `Fig5_replicate.m`
(`eventName`) and rows 2, 3, 5 and 7 equal the named fields `Center_NI`, `tone`, `Side_NI` and
`Food_NI`. Completed trials are the attempt rows in `behavData.trial_rows` (the same rows as
`Fig5_replicate.m`'s `validTrial`), with `outcome` 1 when rewarded.

Where the parameters come from:

- Reward rate (`leaky_rate`): a time-based leaky integrator, incremented at each reward and
  decaying exponentially with time constant tau (Methods, Behavior, paragraph 2), with tau chosen
  per session from 1 to 1200 s (Extended Data Fig. 1 legend) to make the correlation of reward
  rate with log(latency) most negative (Methods). `TAU_GRID` steps by 1 s, a standard choice that
  cannot change a result. The increment is 1 (any constant gives the same correlations and
  splits; claims file header). A reward is counted at the rewarded Side-In, the moment the paper
  says the food hopper clicks (Results, paragraph 1); this is a standard choice, as no trial
  starts between Side-In and Food-Port-In. A trial's reward rate is the value at the event the
  analysis is aligned to, before that trial's own outcome.
- Latency is Center-In minus Light-On from the event table. The `CNIlatency` field is not used:
  it is clipped at 65535 ms (see the notebook's data check).
- Spike density functions (`sdf`): spikes binned at 1 ms and convolved with a Gaussian. The
  Methods give "a Gaussian kernel with variance 20ms"; the authors' deposited `Fig5_replicate.m`
  calls `getFiringRate` with `twsize = 0.02` and `getFiringRate.m` uses `sigma = twsize` as the
  SD of `normpdf`. `SDF_SD` is therefore 0.020 s; the literal reading of the Methods (variance
  20 ms^2, SD 4.5 ms) is `SDF_SD_VARIANT`, run as a variant where a peak or valley is measured.
- Time to cue response (`cue_response`): 40 ms bins sliding in 20 ms steps, a shuffle test with
  10,000 shuffles of each bin against the rate in the 250 ms before the cue, p < 0.01 corrected
  for multiple comparisons (Methods, Analysis, paragraph 1). The shuffle exchanges, trial by trial,
  the post-cue bin rate and the baseline rate (a paired permutation of the two labels; the paper
  does not say what is shuffled, and this is the standard paired form). The correction is
  Bonferroni over the bins tested, and the post-cue window 0.5 s or 1 s (claims file header).
- Bursts (`bursts`): the 80/160 ms template (Methods, Analysis, paragraph 1).
- Ramp angle (`ramp_angle`): mean firing smoothed with a 50 ms Gaussian kernel (read as its SD),
  the maximum and minimum in the 0.5 s before the event, and the signed angle of the line joining
  them, positive when the later extremum is the higher (Methods, Analysis, paragraph 3). The angle
  is computed with time in seconds and rate in Hz; the axis scaling is open but does not change
  the sign (claims file, fig4a criterion).
- High and low reward blocks (`block_split`): a median split, per session, of the block-averaged
  leaky-integrator reward rate (Methods, Analysis, paragraph 3). Block averages are the mean of the
  trials' reward rate at Light-On. With an odd number of blocks the median block is left out
  (`median_block="drop"`), a standard choice; `median_block="low"` puts it with the low blocks, as
  a variant.
- Circular-shift nulls (`circular_shift_p`): a per-cell test that keeps the serial dependence of
  both series, for the per-cell tests of tonic firing and early-trial firing, whose 1 min bins and
  trials are not independent (asked for by the verifier). One series is shifted circularly
  against the other by every shift from `min_shift` to n - `min_shift` steps; p is two-sided. The
  minimum shifts (10 bins of 1 min, longer than a block of about 8 min; 20 trials) are standard
  choices that exclude shifts that leave the series nearly aligned.
- SALT (`salt`): the stimulus-associated latency test of Kvitsiani et al. 2013 (the paper's
  ref. 55), as in its published `salt.m`: first-spike latency histograms in 10 ms windows with
  1 ms bins, baseline windows taken from the period before each pulse, Jensen-Shannon distances
  between them, and p the fraction of baseline-baseline distances at least as large as the median
  test-baseline distance (claims file, fig2 criterion: the test's published defaults). The
  baseline period is the 400 ms before each pulse, which at 2 Hz stays clear of the previous
  pulse's 100 ms; this length is a standard choice. It gives 40 baseline windows and 780 null
  distances, so the smallest nonzero p is 1/780 = 0.0013 and p < 0.001 means p = 0.
"""

from __future__ import annotations

import io
import zipfile

import fsspec
import h5py
import numpy as np
import requests
from scipy.ndimage import gaussian_filter1d

DATASET = "vta-2"
VERSION = "unversioned"   # CRCNS data sets are not versioned (docs/archives.md)
BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com"
ZIP_URL = f"{BUCKET}/vta-2/live/data_and_code.zip"
CHECKSUMS_URL = f"{BUCKET}/vta-2/live/checksums.md5"
MEMBER = "data_and_code/VTA_data.mat"
ZIP_MD5 = "693383b76465b128cb3190591ef43d2d"   # checksums.md5 of the data set

EVENTS = ["LightOn", "CenterIn", "Go", "CenterOut", "SideIn", "SideOut", "FoodIn"]
TAU_GRID = np.arange(1.0, 1201.0, 1.0)
SDF_SD = 0.020
SDF_SD_VARIANT = float(np.sqrt(20.0)) / 1000.0
DT = 0.001


# ----------------------------------------------------------------------------- loading

def zip_etag() -> str:
    return requests.head(ZIP_URL, timeout=60).headers["ETag"].strip('"')


def published_md5() -> dict:
    text = requests.get(CHECKSUMS_URL, timeout=60).text
    return {line.split()[1]: line.split()[0] for line in text.splitlines() if line.strip()}


def zip_listing() -> list[tuple[str, int]]:
    with fsspec.open(ZIP_URL, block_size=2**20).open() as f:
        return [(i.filename, i.file_size) for i in zipfile.ZipFile(f).infolist()]


def read_member(name: str) -> bytes:
    with fsspec.open(ZIP_URL, block_size=2**20).open() as f:
        return zipfile.ZipFile(f).read(name)


def _conv(h, obj, skip=()):
    """MATLAB 7.3 object to Python: structs to dicts, chars to str, cells and struct arrays to
    object arrays, numbers to arrays in MATLAB's orientation."""
    if isinstance(obj, h5py.Group):
        return {k: _conv(h, obj[k], skip) for k in obj if k not in skip and k != "#refs#"}
    if obj.attrs.get("MATLAB_empty", 0):
        return np.array([])
    cls = obj.attrs.get("MATLAB_class", b"")
    data = obj[()]
    if cls == b"char":
        return "".join(chr(c) for c in np.ravel(data.T))
    if data.dtype == h5py.ref_dtype:
        out = np.empty(data.shape, dtype=object)
        for idx in np.ndindex(data.shape):
            out[idx] = _conv(h, h[data[idx]], skip)
        return out.T
    return np.asarray(data).T


def load_units(port_status: bool = False) -> list[dict]:
    """The 29 units. Each segment is a dict with `ts`, `boxts` and `rex` (ratexperience).

    The Pavlovian food-port status (30 kHz, 12 s per trial) is large; with `port_status=True` it
    is kept at 1 kHz (every 30th sample) as `rex["port"]`, one unit at a time."""
    h = h5py.File(io.BytesIO(read_member(MEMBER)), "r")
    U = h["Unit"]
    units = []
    for i in range(U["name"].shape[0]):
        u = {k: _conv(h, h[U[k][i, 0]]) for k in ("name", "session", "FR", "meanWave", "meanLightEvoked")}
        u["FR"] = float(np.ravel(u["FR"])[0])
        u["rat"] = u["session"].split("_")[0]
        seg_ref = h[U["segments"][i, 0]]
        types = [_conv(h, h[r]) for r in np.ravel(seg_ref["Type"][()])]
        segs = {}
        for j, t in enumerate(types):
            ts = np.ravel(_conv(h, h[np.ravel(seg_ref["ts"][()])[j]]))
            box = _conv(h, h[np.ravel(seg_ref["boxts"][()])[j]])
            rex_obj = h[np.ravel(seg_ref["ratexperience"][()])[j]]
            rex = _conv(h, rex_obj, skip=("portStatus",)) if isinstance(rex_obj, h5py.Group) else {}
            if t == "Pav" and isinstance(rex_obj, h5py.Group) and "portStatus" in rex_obj:
                ps = rex_obj["portStatus"]
                rex["port_win"] = np.ravel(ps["Win"][()])
                if port_status:
                    rex["port"] = np.asarray(ps["value"][::30, :]).T  # trials x 1 kHz samples
            d = np.diff(ts.astype(float))
            segs[t] = {"ts": np.sort(ts.astype(float)), "boxts": box if isinstance(box, dict) else {}, "rex": rex,
                       "ts_sorted": bool(np.all(d >= 0)),
                       # number of descending steps, the largest, and the first as (earlier, later) spike time
                       "n_inversions": int(np.sum(d < 0)),
                       "max_inversion": float(-d.min()) if len(d) and d.min() < 0 else 0.0,
                       "first_inversion": (tuple(float(x) for x in ts[np.argmax(d < 0):np.argmax(d < 0) + 2])
                                           if np.any(d < 0) else None)}
        u["segments"] = segs
        units.append(u)
    h.close()
    return units


# ----------------------------------------------------------------------------- bandit trials

def bandit_trials(u: dict) -> dict:
    """Completed bandit trials of a unit's session: event times (s), outcome, choice, latency,
    block index, and the times of every attempt's Light-On (for block boundaries)."""
    seg = u["segments"]["RL"]
    rex, box = seg["rex"], seg["boxts"]
    bd = rex["behavData"]
    rows = np.ravel(bd["trial_rows"]).astype(int) - 1
    ev = np.asarray(box["event"], float)
    out = {name: ev[k, rows] for k, name in enumerate(EVENTS)}
    out["outcome"] = np.ravel(rex["outcome"]).astype(int)
    out["right"] = np.ravel(rex["R_choice"]).astype(int)
    out["latency"] = out["CenterIn"] - out["LightOn"]
    out["block"] = np.ravel(bd["block"])[rows].astype(int)
    out["attempt_lighton"] = ev[0]
    out["attempt_block"] = np.ravel(bd["block"]).astype(int)
    out["cni_field_ms"] = np.ravel(rex["CNIlatency"])
    out["rows"] = rows
    out["n_attempts"] = ev.shape[1]
    return out


def log_latency(tr: dict) -> np.ndarray:
    """log(latency); NaN where the latency is missing or not positive (one trial in session
    IM-1002_170118 has no latency), so that the trial is left out of every fit."""
    lat = tr["latency"]
    return np.where(lat > 0, np.log(np.where(lat > 0, lat, 1.0)), np.nan)


def reward_times(tr: dict) -> np.ndarray:
    return tr["SideIn"][tr["outcome"] == 1]


def leaky_rate(times: np.ndarray, rewards: np.ndarray, taus) -> np.ndarray:
    """Leaky-integrator reward rate at `times` (rewards strictly before each time), one row per
    tau. Increment 1 per reward."""
    taus = np.atleast_1d(np.asarray(taus, float))
    dt = times[:, None] - rewards[None, :]
    mask = dt > 0
    dtm = np.where(mask, dt, 0.0)
    out = np.empty((len(taus), len(times)))
    for k, tau in enumerate(taus):
        out[k] = np.where(mask, np.exp(-dtm / tau), 0.0).sum(1)
    return out


def best_tau(tr: dict, taus=TAU_GRID) -> tuple[float, float, np.ndarray]:
    """tau (s) making Pearson r(reward rate at Light-On, log latency) most negative; returns tau,
    r at that tau, and r for every tau."""
    rr = leaky_rate(tr["LightOn"], reward_times(tr), taus)
    y = log_latency(tr)
    ok = np.isfinite(y)
    yc = y[ok] - y[ok].mean()
    xc = rr[:, ok] - rr[:, ok].mean(1, keepdims=True)
    den = np.sqrt((xc**2).sum(1) * (yc**2).sum())
    r = np.where(den > 0, (xc @ yc) / np.where(den > 0, den, 1), np.nan)
    k = int(np.nanargmin(r))
    return float(taus[k]), float(r[k]), r


def trial_learning_values(tr: dict, alpha: float, model: str, init: float = 0.5) -> np.ndarray:
    """Trial-based reward expectation before each trial's outcome (Extended Data Fig. 8 legend):
    `ac`, actor-critic V' = V + alpha (reward - V); `q`, Q-learning with Q_left and Q_right,
    updating only the chosen side, returning Q_left + Q_right. Initial values 0.5 (claims file,
    ed8 criterion)."""
    o = tr["outcome"]
    n = len(o)
    out = np.empty(n)
    if model == "ac":
        v = init
        for t in range(n):
            out[t] = v
            v = v + alpha * (o[t] - v)
    else:
        q = np.array([init, init])
        for t in range(n):
            out[t] = q.sum()
            c = int(tr["right"][t])
            q[c] = q[c] + alpha * (o[t] - q[c])
    return out


def rewards_last10(tr: dict) -> np.ndarray:
    """Rewards in the previous 10 trials (fewer at the start), as `pelletpermin.m` counts them."""
    o = tr["outcome"]
    c = np.r_[0, np.cumsum(o)]
    idx = np.arange(len(o))
    return c[idx] - c[np.maximum(idx - 10, 0)]


def best_alpha(tr: dict, model: str, alphas=np.round(np.arange(0.01, 1.0001, 0.01), 2)):
    y = log_latency(tr)
    ok = np.isfinite(y)
    best = (None, np.inf)
    for a in alphas:
        v = trial_learning_values(tr, a, model)
        if np.std(v[ok]) == 0:
            continue
        r = np.corrcoef(v[ok], y[ok])[0, 1]
        if r < best[1]:
            best = (float(a), float(r))
    return best


# ----------------------------------------------------------------------------- spikes

def sdf(ts: np.ndarray, t_end: float, sd: float = SDF_SD) -> np.ndarray:
    """Spike density (Hz) on a 1 ms grid from 0 to t_end."""
    n = int(np.ceil(t_end / DT)) + 1
    counts = np.bincount(np.clip((ts / DT).astype(int), 0, n - 1), minlength=n).astype(float)
    return gaussian_filter1d(counts, sd / DT, mode="constant") / DT


def aligned(trace: np.ndarray, events: np.ndarray, t0: float, t1: float) -> np.ndarray:
    """Trials x samples of a 1 ms trace from t0 to t1 around each event (NaN where outside)."""
    offs = np.arange(int(round(t0 / DT)), int(round(t1 / DT)) + 1)
    out = np.full((len(events), len(offs)), np.nan)
    for k, e in enumerate(events):
        if not np.isfinite(e):
            continue
        idx = int(round(e / DT)) + offs
        ok = (idx >= 0) & (idx < len(trace))
        out[k, ok] = trace[idx[ok]]
    return out


def counts_in(ts: np.ndarray, starts: np.ndarray, ends: np.ndarray) -> np.ndarray:
    return np.searchsorted(ts, ends) - np.searchsorted(ts, starts)


def cue_response(ts, events, rng, post=0.5, base=0.25, width=0.04, step=0.02, n_shuffles=10000, alpha=0.01):
    """Time-to-cue-response shuffle test. Returns (responds, first significant bin start in s or
    NaN, p-values per bin, number of bins)."""
    ev = events[np.isfinite(events)]
    starts = np.arange(0.0, post - width + 1e-9, step)
    b = counts_in(ts, ev - base, ev) / base
    d = np.stack([counts_in(ts, ev + s, ev + s + width) / width - b for s in starts], 1)  # trials x bins
    obs = d.mean(0)
    signs = rng.choice(np.array([-1.0, 1.0]), size=(n_shuffles, len(ev)))
    null = signs @ d / len(ev)
    p = ((null >= obs[None, :]).sum(0) + 1) / (n_shuffles + 1)
    sig = p < alpha / len(starts)
    first = float(starts[np.argmax(sig)]) if sig.any() else np.nan
    return bool(sig.any()), first, p, len(starts)


def bursts(ts: np.ndarray, start_isi: float = 0.080, end_isi: float = 0.160) -> np.ndarray:
    """Start times of bursts by the 80/160 ms template."""
    isi = np.diff(ts)
    out = []
    k = 0
    while k < len(isi):
        if isi[k] <= start_isi:
            out.append(ts[k])
            k += 1
            while k < len(isi) and isi[k] < end_isi:
                k += 1
        else:
            k += 1
    return np.asarray(out)


def long_isi_time(ts: np.ndarray, intervals: list[tuple[float, float]], threshold: float) -> float:
    """Seconds, within the intervals, covered by inter-spike intervals longer than threshold."""
    isi_s, isi_e = ts[:-1], ts[1:]
    long = (isi_e - isi_s) > threshold
    s_l, e_l = isi_s[long], isi_e[long]
    total = 0.0
    for a, b in intervals:
        total += np.clip(np.minimum(e_l, b) - np.maximum(s_l, a), 0, None).sum()
    return float(total)


def ramp_angle(mean_rate: np.ndarray, times: np.ndarray) -> float:
    """Signed angle (degrees) of the line joining the max and min of mean_rate, positive when the
    later extremum is the higher."""
    i_max, i_min = int(np.argmax(mean_rate)), int(np.argmin(mean_rate))
    a, b = sorted([i_max, i_min])
    if a == b:
        return 0.0
    return float(np.degrees(np.arctan2(mean_rate[b] - mean_rate[a], times[b] - times[a])))


# ----------------------------------------------------------------------------- blocks

def block_intervals(tr: dict) -> dict:
    """Per block: (start, end) from its first attempt's Light-On to the next block's first
    Light-On; the last block ends at the last completed trial's Side-Out (or Side-In)."""
    lo, blk = tr["attempt_lighton"], tr["attempt_block"]
    blocks = np.unique(tr["block"])
    end_session = np.nanmax(np.r_[tr["SideOut"], tr["SideIn"]])
    out = {}
    for b in blocks:
        first = np.nanmin(lo[blk == b])
        later = lo[blk > b]
        end = np.nanmin(later) if np.isfinite(later).any() else end_session
        out[int(b)] = (float(first), float(end))
    return out


def block_split(tr: dict, tau: float, median_block: str = "drop") -> tuple[list, list, dict]:
    """High and low blocks by a median split of the block-mean reward rate at Light-On."""
    rr = leaky_rate(tr["LightOn"], reward_times(tr), [tau])[0]
    means = {int(b): float(rr[tr["block"] == b].mean()) for b in np.unique(tr["block"])}
    med = np.median(list(means.values()))
    high = [b for b, m in means.items() if m > med]
    low = [b for b, m in means.items() if m < med]
    if median_block == "low":
        low += [b for b, m in means.items() if m == med]
    return high, low, means


def circular_shift_p(x: np.ndarray, y: np.ndarray, stat, min_shift: int) -> tuple[float, float, int]:
    """Two-sided p of stat(x, y) against stat(roll(x, k), y) for k = min_shift .. n - min_shift.
    Returns (observed statistic, p, number of shifts)."""
    obs = stat(x, y)
    null = np.array([stat(np.roll(x, k), y) for k in range(min_shift, len(x) - min_shift + 1)])
    return float(obs), float((np.sum(np.abs(null) >= abs(obs)) + 1) / (len(null) + 1)), len(null)


# ----------------------------------------------------------------------------- SALT

def _jsd(p, q):
    m = 0.5 * (p + q)

    def kl(a, b):
        nz = a > 0
        return np.sum(a[nz] * np.log2(a[nz] / b[nz]))
    return 0.5 * kl(p, m) + 0.5 * kl(q, m)


def salt(ts: np.ndarray, pulses: np.ndarray, base: float = 0.4, wn: float = 0.010, dt: float = 0.001):
    """Stimulus-associated latency test (Kvitsiani et al. 2013, salt.m). Returns (p, I)."""
    nb = int(round(wn / dt))
    nwin = int(round(base / wn))

    def first_latency_hist(starts):
        idx = np.searchsorted(ts, starts)
        nxt = np.where(idx < len(ts), ts[np.minimum(idx, len(ts) - 1)], np.inf) - starts
        lat = np.where(nxt < wn, np.floor(nxt / dt).astype(int) + 1, 0)  # 1..nb, 0 = no spike
        h = np.bincount(lat, minlength=nb + 1)[: nb + 1].astype(float)
        return h / h.sum()

    hists = [first_latency_hist(pulses - base + k * wn) for k in range(nwin)]
    hists.append(first_latency_hist(pulses))
    kn = len(hists)
    d = np.full((kn, kn), np.nan)
    for a in range(kn):
        for b in range(a + 1, kn):
            d[a, b] = np.sqrt(2 * _jsd(hists[a], hists[b]))
    null = d[: kn - 1, : kn - 1]
    null = null[np.isfinite(null)]
    test = np.median(d[: kn - 1, kn - 1])
    return float(np.mean(null >= test)), float(test - np.median(null))
