"""Loading and per-unit measures for Senzai & Buzsaki (2017) on DANDI:000003.

Every file is streamed from the archive at the pinned version (remfile + h5py);
nothing is written to disk. `process_file` reads one session and returns, for
each unit, the measures the claims use, and for each pair of excitatory units
recorded together, the cross-correlogram tests. The notebook runs it on every
file and pools the results.

Where each parameter comes from (C = the claim's criterion in
claims/senzai-2017.yaml; M = the paper's STAR Methods, quoted; A = an
assumption, said why; S = a standard choice for a detail that cannot change a
result):

- Rates by state: the `brain_states` table; wake read as `awake` alone and as
  `awake` + `quiet` (C, claims file header). Overall rate: spikes over the
  span of the LFP (C, interneuron-rates reading a).
- Burst index: "the average number of spikes in the 3-5 ms bins of the spike
  autocorrelogram divided by the average number of spikes in the 200-300 ms
  bins" (M, Unit classification). Counted with both lags signs, per ms.
- Waveform: mean of the first 200 stored spikes (C), damaged spikes (all 0 or
  a sample beyond 20000 steps) left out (S); channel of largest peak-to-peak
  amplitude (M "recording site with the maximum amplitude"; peak-to-peak is S);
  cubic spline to 100 kHz (M "up-sampled to 100kHz with a spline
  interpolation"); trough-to-peak = trough to the largest later sample (S),
  and, as a variant, trough to the first local maximum after it (S), which
  slow drift of an unfiltered mean does not move. The files do not say
  whether the stored waveforms (the lab's .spk files) were filtered; the
  paper measures the latency on "the unfiltered waveform" (Results).
  Second derivative from the trough to 0.8 ms after it, waveform normalised to
  its trough (C, gc-mc-classification; M "0 to 0.8ms period of the second
  derivative").
- Wide-band site: in files holding the 20 kHz wide-band signal, the mean
  300 Hz high-passed signal around the unit's spikes in up to four 52 s
  blocks; the site is the channel of largest peak-to-peak (C, mc-deeper). The
  300 Hz cut-off and 4th-order Butterworth are S. The unit's waveform at the
  site is the mean of the unfiltered wide band (C, gc-mc-classification),
  over -1 to +2 ms (S: long enough for the peak after the trough); the
  high-passed mean is kept as a variant.
- Electrodes: each LFP column's shank and place in its shank's list
  (shank_electrode_number), to check against the DS2 profile whether the list
  is in depth order.
- DS2 amplitude per channel: LFP at the DS2 peak minus the mean of -36 to -16
  ms, the baseline of M ("lower than the baseline value (-36 ms to -16 ms)"),
  averaged over up to 600 DS2 events of the file (S: a sample for speed).
- DS2 histograms: 2 ms bins over +-100 ms (C); peak ratio = largest rate
  within +-20 ms over the mean rate in 50-100 ms on both sides (C, header);
  peak time = centre of that bin.
- Theta 4-10 Hz and gamma 30-80 Hz on the file's hilus reference channel
  (`hilus_reference`; M "periods with oscillation amplitude higher than
  criteria ... median+0.5 s.d. for theta, median+1 s.d. for gamma"), in
  `awake` periods of at least 2 s, up to one hour per file (C). Filters are
  3rd-order Butterworth, zero phase (S). Rayleigh p < 0.05 and kappa > 0.1
  (M). Kappa from the mean resultant length by the usual approximation
  (Fisher 1993) (S). Phase 0 is the peak of the filtered LFP (C).
- Optogenetic suppression: 20 ms pulses; rate in +2 to +15 ms against the
  20 ms before onset, or 50 to 200 ms after onset (C); suppressed when at
  least 20% below baseline (M "decreased by >= 20% of the baseline PETH in
  +2 to +15ms bins"). The PETH in 1 ms bins from -20 to +200 ms is kept for
  the per-bin and significance readings of the same passage (notebook).
- Gamma phases of each unit's spikes are kept, for a control with equal
  spike counts (MRL is biased upward at low counts).
- Cross-correlograms: 0.5 ms bins, baseline from convolution with a Gaussian
  of 10 ms SD, threshold the 99.9999 percentile of the Poisson distribution
  at the baseline rate, at least two consecutive bins within +1.5 to +5 ms
  (connection) or -1 to +1 ms (synchrony) (M, Detection of short-time scale
  interactions). The CCG spans +-50 ms (S; the Gaussian is reflected at the
  ends). The paper's manual inspection is not repeated (C).
- Transmission probability: CCG counts minus baseline at +1.5 to +5 ms, over
  the number of reference spikes (C, burst-facilitation); bursts are spikes
  at most 6 ms apart (C, header).
- Spatial maps: speed > 3 cm/s, 1.86 cm bins and 5.57 cm Gaussian on the
  linearised T-maze, 0.92 cm pixels and 1.84 cm Gaussian in the open field
  (M, Place fields); speed from positions smoothed with a 0.25 s Gaussian (C,
  header). T-maze fields: at least 5 bins above 50% of the local maximum with
  a peak above 1 Hz (M); open-field fields: at least 100 pixels above the
  larger of 20% of the local maximum and 1 Hz (M). The local maximum is taken
  iteratively: the highest remaining bin, its field, then the next (A: the
  paper does not say how local maxima are found; this is the usual way). In
  the open field the map's peak is the local maximum (C, header). The run on
  the T-maze is from entry into the central arm to within 10 cm of the reward
  port, on light-free trials (C, header); the port is 18 cm from the end of
  the 102 cm side arm (M, Behavioral procedures). The lab's `arm_start` lies
  about 27 cm into the central arm, so the run starts at the mouse's last
  entry into the arm before it (A: the Methods start at the gate opening,
  which the files do not mark; the entry is the nearest marked point). Runs
  from arm_start itself, and runs without the side-arm samples on the arm not
  chosen (the sign of side_arm_angle opposite to the run's end), are kept as
  variants, and so is a linearisation that puts each side-arm sample on the
  arm its angle's sign gives (positive is the left arm) in place of the
  trial's arm.
- Interneurons are the dentate ones (region DG) wherever the paper's counts
  are dentate counts: "narrow-waveform (n = 248) and wide-waveform (n = 268)
  putative interneurons ... Units recorded in CA3 were separately classified"
  (Results, Identification of granule cells and mossy cells, paragraph 1).
"""

import json
import urllib.request

import h5py
import numpy as np
import remfile
from scipy import ndimage, signal, stats
from scipy.interpolate import CubicSpline

DANDISET = "000003"
VERSION = "0.261122.2143"
API = "https://api.dandiarchive.org/api"
EXCLUDED_SUBJECT = "YutaMouse57"  # not in the paper (dandiset description)

FS_LFP = 1250.0
FS_WB = 20000.0
UV_PER_STEP = 0.3814697265625  # 10 V over 16 bits at x400, in uV (file attributes)

TYPES = {
    "granule cell": "GC",
    "mossy cell": "MC",
    "CA3 pyramidal cell": "CA3",
    "narrow-waveform interneuron": "nI",
    "wide-waveform interneuron (narrower)": "wI",
    "wide-waveform interneuron (wider)": "wI",
}


def list_assets():
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    out = []
    while url:
        with urllib.request.urlopen(url) as r:
            d = json.load(r)
        out += d["results"]
        url = d["next"]
    return sorted(out, key=lambda a: a["path"])


def open_asset(asset_id):
    url = f"{API}/assets/{asset_id}/download/"
    return h5py.File(remfile.File(url), "r")


def _ragged(index, data_len):
    starts = np.concatenate([[0], index[:-1]]).astype(np.int64)
    return starts, index.astype(np.int64)


def _intervals(table, label_col="label"):
    lab = table[label_col][:].astype(str)
    return lab, table["start_time"][:], table["stop_time"][:]


def count_in(spk, starts, stops):
    """Spikes of a sorted train inside intervals."""
    return int(np.sum(np.searchsorted(spk, stops) - np.searchsorted(spk, starts)))


def lag_counts(a, b, lo, hi):
    """All lags b - a within [lo, hi) for sorted trains a and b."""
    i0 = np.searchsorted(b, a + lo)
    i1 = np.searchsorted(b, a + hi)
    n = i1 - i0
    if n.sum() == 0:
        return np.zeros(0)
    rep = np.repeat(np.arange(len(a)), n)
    offs = np.arange(n.sum()) - np.repeat(np.cumsum(n) - n, n)
    return b[i0[rep] + offs] - a[rep]


def burst_index(spk):
    """M: mean count in 3-5 ms ACG bins over mean count in 200-300 ms bins."""
    if len(spk) < 10:
        return np.nan
    d = lag_counts(spk, spk, 0.0005, 0.3)
    near = np.sum((d >= 0.003) & (d < 0.005)) / 2.0
    far = np.sum((d >= 0.2) & (d < 0.3)) / 100.0
    return near / far if far > 0 else np.nan


# ---------------------------------------------------------------- waveforms
def mean_waveform(units, k, n_spikes=200):
    wii = units["waveforms_index_index"]
    wi = units["waveforms_index"]
    s0 = int(wii[k - 1]) if k > 0 else 0
    s1 = int(wii[k])
    n = min(n_spikes, s1 - s0)
    if n <= 0:
        return None
    ends = wi[s0:s0 + n]
    r0 = int(wi[s0 - 1]) if s0 > 0 else 0
    w = units["waveforms"][r0:int(ends[-1])].astype(np.float32)
    nch = int(ends[0] - r0)
    if nch <= 0 or w.shape[0] != n * nch:
        return None
    w = w.reshape(n, nch, 32)
    bad = (np.abs(w).max(axis=(1, 2)) > 20000) | (np.abs(w).max(axis=(1, 2)) == 0)
    if (~bad).sum() == 0:
        return None
    return w[~bad].mean(axis=0)  # channels x 32


def waveform_features(mw):
    """Trough-to-peak (ms), max channel, normalised 2nd-derivative segment."""
    p2p = mw.max(axis=1) - mw.min(axis=1)
    ch = int(np.argmax(p2p))
    y = mw[ch] - np.median(mw[ch, :5])
    t = np.arange(mw.shape[1]) / FS_WB
    tt = np.arange(0, t[-1] + 1e-9, 1e-5)  # 100 kHz
    yy = CubicSpline(t, y)(tt)
    it = int(np.argmin(yy))
    ip = it + int(np.argmax(yy[it:]))
    tp = (ip - it) * 1e-2  # ms
    at_end = ip >= len(yy) - 3
    # trough to the first local maximum after it (S): unlike the largest later
    # sample, it is not moved by slow drift of an unfiltered mean
    dy = np.diff(yy[it:])
    up = np.flatnonzero((dy[:-1] > 0) & (dy[1:] <= 0))
    tp_first = (up[0] + 1) * 1e-2 if len(up) else np.nan
    yn = yy / abs(yy[it]) if yy[it] != 0 else yy
    d2 = np.gradient(np.gradient(yn))
    seg = d2[it:it + 81]
    if len(seg) < 81:
        seg = np.concatenate([seg, np.full(81 - len(seg), np.nan)])
    return tp, ch, at_end, seg, tp_first


# ---------------------------------------------------------------- LFP
def _read_lfp(f, i0, i1, cols=None):
    d = f["processing/ecephys/LFP/lfp/data"]
    if cols is None:
        return d[i0:i1, :]
    return d[i0:i1, cols]


def ds2_amplitude_profile(f, ds2_peaks, max_events=600):
    """Mean LFP at the DS2 peak minus -36..-16 ms baseline, per channel (uV)."""
    if len(ds2_peaks) == 0:
        return None, 0
    n_lfp = f["processing/ecephys/LFP/lfp/data"].shape[0]
    block = 1048576  # one chunk of rows
    samp = np.round(ds2_peaks * FS_LFP).astype(np.int64)
    blocks = np.bincount(samp // block)
    order = np.argsort(blocks)[::-1]
    amps, used = [], 0
    for b in order:
        if used >= max_events or blocks[b] == 0:
            break
        i0, i1 = b * block, min((b + 1) * block, n_lfp)
        x = _read_lfp(f, i0, i1).astype(np.float32) * UV_PER_STEP
        s = samp[(samp >= i0 + 50) & (samp < i1 - 50)] - i0
        s = s[: max_events - used]
        if len(s) == 0:
            continue
        bl0, bl1 = int(round(0.036 * FS_LFP)), int(round(0.016 * FS_LFP))
        for si in s:
            amps.append(x[si] - x[si - bl0:si - bl1].mean(axis=0))
        used += len(s)
        del x
    if not amps:
        return None, 0
    return np.mean(amps, axis=0), used


def phase_modulation(f, hil_col, awake, spikes, max_s=3600.0):
    """Per unit theta and gamma MRL, Rayleigh p, kappa and mean phase."""
    st, sp = awake
    keep, tot = [], 0.0
    for a, b in zip(st, sp):
        if b - a < 2:
            continue
        if tot >= max_s:
            break
        b = min(b, a + (max_s - tot))
        keep.append((a, b))
        tot += b - a
    out = {}
    if not keep:
        return out, 0.0
    bands = {"theta": (4, 10, 0.5), "gamma": (30, 80, 1.0)}
    sigs = {k: [] for k in bands}
    for a, b in keep:
        i0, i1 = int(a * FS_LFP), int(b * FS_LFP)
        x = _read_lfp(f, i0, i1, hil_col).astype(np.float64)
        for k, (lo, hi, _) in bands.items():
            bb, aa = signal.butter(3, [lo / (FS_LFP / 2), hi / (FS_LFP / 2)], btype="band")
            z = signal.hilbert(signal.filtfilt(bb, aa, x))
            sigs[k].append((i0, np.angle(z).astype(np.float32), np.abs(z).astype(np.float32)))
    for k, (lo, hi, nsd) in bands.items():
        allamp = np.concatenate([s[2] for s in sigs[k]])
        thr = np.median(allamp) + nsd * allamp.std()
        for u, spk in spikes.items():
            ph = []
            for i0, phase, amp in sigs[k]:
                idx = np.round(spk * FS_LFP).astype(np.int64) - i0
                idx = idx[(idx >= 0) & (idx < len(phase))]
                idx = idx[amp[idx] > thr]
                ph.append(phase[idx])
            ph = np.concatenate(ph) if ph else np.zeros(0)
            n = len(ph)
            if n < 2:
                out[(u, k)] = dict(n=n, mrl=np.nan, p=np.nan, kappa=np.nan, phase=np.nan)
                continue
            z = np.mean(np.exp(1j * ph))
            r = np.abs(z)
            R = n * r
            p = np.exp(np.sqrt(1 + 4 * n + 4 * (n ** 2 - R ** 2)) - (1 + 2 * n))
            out[(u, k)] = dict(n=n, mrl=r, p=min(p, 1.0), kappa=_kappa(r, n), phase=float(np.angle(z)))
            if k == "gamma":
                out[(u, k)]["ph"] = ph.astype(np.float32)  # for the count-matched control
    return out, tot


def _kappa(r, n):
    if r < 0.53:
        k = 2 * r + r ** 3 + 5 * r ** 5 / 6
    elif r < 0.85:
        k = -0.4 + 1.39 * r + 0.43 / (1 - r)
    else:
        k = 1 / (r ** 3 - 4 * r ** 2 + 3 * r)
    if n < 15:
        k = max(k - 2 / (n * k), 0) if k < 2 else (n - 1) ** 3 * k / (n ** 3 + n)
    return k


# ---------------------------------------------------------------- wide band
WB_PRE, WB_POST = 20, 40  # samples before and after the spike time: -1 to +2 ms (S)


def wideband_sites(f, spikes, n_blocks=4):
    """Channel (LFP column) of largest mean spike in the 300 Hz high-passed wide band.

    Returns, per unit, (column, spikes used, filtered mean at the column,
    unfiltered mean at the column); the means span -1 to +2 ms around the
    spike time. The unfiltered mean is the wide-band signal as stored (C,
    gc-mc-classification: "the unfiltered wide-band waveform")."""
    d = f["acquisition/ElectricalSeries/data"]
    n = d.shape[0]
    block = 1048576
    nb = n // block
    picks = np.linspace(1, max(nb - 2, 1), n_blocks).astype(int)
    bb, aa = signal.butter(4, 300 / (FS_WB / 2), btype="high")
    nw = WB_PRE + WB_POST
    sums = {u: np.zeros((nw, d.shape[1])) for u in spikes}
    raws = {u: np.zeros((nw, d.shape[1])) for u in spikes}
    cnt = {u: 0 for u in spikes}
    for b in np.unique(picks):
        i0, i1 = b * block, min((b + 1) * block, n)
        sel = {}
        for u, spk in spikes.items():
            s = np.round(spk * FS_WB).astype(np.int64) - i0
            sel[u] = s[(s >= WB_PRE) & (s < i1 - i0 - WB_POST)][:300]
            cnt[u] += len(sel[u])
        for c0 in range(0, d.shape[1], 16):  # 16 columns at a time, for memory
            xr = d[i0:i1, c0:c0 + 16].astype(np.float32)
            x = signal.filtfilt(bb, aa, xr, axis=0).astype(np.float32)
            for u, s in sel.items():
                if len(s):
                    idx = s[:, None] + np.arange(-WB_PRE, WB_POST)[None, :]
                    sums[u][:, c0:c0 + 16] += x[idx].sum(axis=0)
                    raws[u][:, c0:c0 + 16] += xr[idx].sum(axis=0)
            del x, xr
    out = {}
    for u in spikes:
        if cnt[u] >= 10:
            m = sums[u] / cnt[u]
            col = int(np.argmax(m.max(axis=0) - m.min(axis=0)))
            out[u] = (col, cnt[u], m[:, col], raws[u][:, col] / cnt[u])
        else:
            out[u] = (-1, cnt[u], None, None)
    return out


# ---------------------------------------------------------------- CCG
BIN = 0.0005
HALF = 0.05
EDGES = np.arange(-HALF, HALF + BIN / 2, BIN)
CENTRES = (EDGES[:-1] + EDGES[1:]) / 2
CONN = (CENTRES > 0.0015) & (CENTRES < 0.005)
SYNC = (CENTRES > -0.001) & (CENTRES < 0.001)


PETH_EDGES = np.round(np.arange(-0.020, 0.2005, 0.001), 6)  # 1 ms bins, -20 to +200 ms (S)


def ccg(a, b):
    return np.histogram(lag_counts(a, b, -HALF, HALF), EDGES)[0].astype(float)


def ccg_test(c):
    """Returns (baseline, significant-bin mask) for a CCG (M)."""
    base = ndimage.gaussian_filter1d(c, sigma=0.010 / BIN, mode="reflect")
    thr = stats.poisson.ppf(0.999999, np.maximum(base, 1e-12))
    return base, c > thr


def two_consecutive(mask):
    return bool(np.any(mask[:-1] & mask[1:]))


def transmission(a, b):
    """Excess b spikes at +1.5..+5 ms per a spike (C)."""
    if len(a) == 0:
        return np.nan
    c = ccg(a, b)
    base, _ = ccg_test(c)
    return float((c[CONN] - base[CONN]).sum() / len(a))


def burst_spikes(a, isi=0.006):
    """First and second spikes of bursts (spikes at most 6 ms apart)."""
    d = np.diff(a)
    prev_long = np.concatenate([[True], d > isi])
    next_short = np.concatenate([d <= isi, [False]])
    first = np.where(prev_long & next_short)[0]
    return a[first], a[first + 1]


# ---------------------------------------------------------------- spatial
def smooth_pos(t, xy, sd_s=0.25):
    dt = np.median(np.diff(t))
    out = np.empty_like(xy)
    for j in range(xy.shape[1]):
        v = xy[:, j].copy()
        ok = np.isfinite(v)
        if ok.sum() < 2:
            out[:, j] = np.nan
            continue
        v[~ok] = np.interp(np.flatnonzero(~ok), np.flatnonzero(ok), v[ok])
        out[:, j] = ndimage.gaussian_filter1d(v, sd_s / dt)
    return out


def speed(t, xy_cm):
    s = smooth_pos(t, xy_cm)
    v = np.sqrt((np.gradient(s[:, 0], t)) ** 2 + (np.gradient(s[:, 1], t)) ** 2)
    return v


def nan_smooth(rate, occ_ok, sd_bins):
    r = np.where(occ_ok, rate, 0.0)
    w = ndimage.gaussian_filter(occ_ok.astype(float), sd_bins, mode="constant")
    s = ndimage.gaussian_filter(r, sd_bins, mode="constant")
    with np.errstate(invalid="ignore", divide="ignore"):
        out = s / w
    out[~occ_ok] = np.nan
    return out


def fields_1d(m, min_bins=5, frac=0.5, min_peak=1.0):
    """Iterative local-maximum fields on a 1-D map (A, see docstring)."""
    m = np.where(np.isfinite(m), m, 0.0)
    free = np.ones(len(m), bool)
    out = []
    while free.any():
        i = int(np.argmax(np.where(free, m, -1)))
        pk = m[i]
        if pk <= min_peak:
            break
        lo = i
        while lo - 1 >= 0 and free[lo - 1] and m[lo - 1] > frac * pk:
            lo -= 1
        hi = i
        while hi + 1 < len(m) and free[hi + 1] and m[hi + 1] > frac * pk:
            hi += 1
        free[lo:hi + 1] = False
        if hi - lo + 1 >= min_bins:
            out.append((lo, hi, pk))
    return out


def field_2d(m, min_px=100, frac=0.2, min_rate=1.0):
    """Open-field field around the map's peak (M; C header): pixels connected
    to the peak above max(20% of peak, 1 Hz); returns (mask, peak) or None."""
    if not np.isfinite(m).any():
        return None
    mm = np.where(np.isfinite(m), m, 0.0)
    pk = mm.max()
    if pk < min_rate:
        return None
    above = mm > max(frac * pk, min_rate)
    lab, _ = ndimage.label(above)
    i = np.unravel_index(np.argmax(mm), mm.shape)
    mask = lab == lab[i]
    if mask.sum() < min_px:
        return None
    return mask, pk


def skaggs_info(occ_p, rate):
    ok = np.isfinite(rate) & (occ_p > 0)
    p = occ_p[ok] / occ_p[ok].sum()
    r = rate[ok]
    lam = np.sum(p * r)
    if lam <= 0:
        return np.nan
    with np.errstate(divide="ignore", invalid="ignore"):
        t = np.where(r > 0, p * r * np.log2(r / lam), 0.0)
    return float(t.sum())  # bits per second


def corr_maps(a, b):
    ok = np.isfinite(a) & np.isfinite(b)
    if ok.sum() < 10 or np.std(a[ok]) == 0 or np.std(b[ok]) == 0:
        return np.nan
    return float(np.corrcoef(a[ok], b[ok])[0, 1])


OF_BINS = int(round(46 / 0.92))  # 50 pixels of 0.92 cm


def of_map(t, xy_cm, spk, sl=slice(None)):
    """Smoothed open-field rate map (Hz) from samples sl, speed > 3 cm/s."""
    dt = np.median(np.diff(t))
    v = speed(t, xy_cm)
    good = np.zeros(len(t), bool)
    good[sl] = True
    good &= (v > 3) & np.isfinite(xy_cm).all(axis=1)
    ix = np.clip((xy_cm[:, 0] / 0.92).astype(int), 0, OF_BINS - 1)
    iy = np.clip((xy_cm[:, 1] / 0.92).astype(int), 0, OF_BINS - 1)
    occ = np.zeros((OF_BINS, OF_BINS))
    np.add.at(occ, (ix[good], iy[good]), dt)
    si = np.searchsorted(t, spk) - 1
    si = si[(si >= 0) & (si < len(t))]
    si = si[good[si]]
    sc = np.zeros_like(occ)
    np.add.at(sc, (ix[si], iy[si]), 1)
    ok = occ > 0
    with np.errstate(invalid="ignore", divide="ignore"):
        raw = np.where(ok, sc / occ, np.nan)
    return nan_smooth(raw, ok, 1.84 / 0.92), occ


TM_BIN = 1.86
CENTRAL_CM = 65.0
SIDE_CM = 102.0
RADIUS_CM = 32.5
PORT_CM = SIDE_CM - 18.0


def _tmaze_arrays(f):
    tr = f["intervals/trials"]
    T = {k: tr[k][:] for k in ["arm_start", "arm_end", "sens_pass", "left_run", "stim_run", "error_run", "stop_time"]}
    g = f["processing/behavior/t_maze_position"]
    pos = g["position/data"][:] * 32.5  # cm
    if "timestamps" in g["position"]:
        t = g["position/timestamps"][:]
        rate = 1 / np.median(np.diff(t))
    else:
        rate = g["position/starting_time"].attrs["rate"]
        t = g["position/starting_time"][()] + np.arange(len(pos)) / rate
    ca = g["central_arm_position/data"][:] * 32.5  # cm, 65 at entry, 0 at junction
    ang = f["processing/behavior/side_arm_angle/data"][:]
    return T, t, rate, ca, ang, speed(t, pos)


def tmaze_runs(f, start="entry", drop_other_arm=False, arm_by_angle=False, arrays=None):
    """Linearised outbound runs: list of (times, lin_cm, arm, speed, left).

    start="entry": from the mouse's last entry into the central arm before the
    lab's arm_start (A, main); start="arm_start": from arm_start itself (the
    other reading, a variant). Side-arm samples whose angle has the sign
    opposite to the run's end (an excursion into the arm not chosen) are
    counted in n_other; drop_other_arm=True leaves them out of the run's
    occupancy and spikes (a variant); arm_by_angle=True puts each side-arm
    sample on the arm the sign of its angle gives, not the trial's arm (a
    variant)."""
    T, t, rate, ca, ang, v = arrays if arrays is not None else _tmaze_arrays(f)
    runs = []
    for k in range(len(T["arm_start"])):
        if T["stim_run"][k]:
            continue
        a = T["arm_start"][k]
        i0 = np.searchsorted(t, a)
        at_start = CENTRAL_CM - ca[min(i0, len(ca) - 1)]  # cm into the central arm at arm_start
        # arm_start is ~27 cm into the central arm; go back to the entry (A)
        if start == "entry":
            while i0 > 0 and ca[i0 - 1] > 0:
                i0 -= 1
        i_end = np.searchsorted(t, T["stop_time"][k])
        side = np.abs(ang[i0:i_end]) * RADIUS_CM
        reach = np.flatnonzero((side >= PORT_CM - 10) & (ca[i0:i_end] == 0))
        if len(reach) == 0:
            continue
        i1 = i0 + reach[0]
        if i1 - i0 < 5:
            continue
        cen = CENTRAL_CM - ca[i0:i1]
        sd = np.abs(ang[i0:i1]) * RADIUS_CM
        on_side = (ca[i0:i1] == 0) & (sd > 0)
        other = on_side & (np.sign(ang[i0:i1]) != np.sign(ang[i1]))
        lin = np.where(on_side, CENTRAL_CM + sd, np.clip(cen, 0, CENTRAL_CM))
        valid = (on_side | (ca[i0:i1] > 0)) & np.isfinite(lin)
        if drop_other_arm:
            valid &= ~other
        lin = np.where(valid, lin, 0.0)
        runs.append(dict(t=t[i0:i1], lin=lin, side=on_side, v=np.where(valid, v[i0:i1], 0.0), left=bool(T["left_run"][k]),
                         error=bool(T["error_run"][k]), dt=1 / rate, arm_start_cm=float(at_start),
                         n_side=int(on_side.sum()), n_other=int(other.sum()),
                         other_max_cm=float(sd[other].max()) if other.any() else 0.0,
                         end_left=bool(ang[i1] > 0), side_left=(ang[i0:i1] > 0) if arm_by_angle else None))
    return runs


N_CEN = int(np.ceil(CENTRAL_CM / TM_BIN))
N_SIDE = int(np.ceil(PORT_CM / TM_BIN))


def tmaze_bin(run):
    """Bin index on a track central (0..N_CEN-1), left side, right side."""
    lin = run["lin"]
    b = np.where(run["side"], N_CEN + np.minimum(((lin - CENTRAL_CM) / TM_BIN).astype(int), N_SIDE - 1),
                 np.minimum((lin / TM_BIN).astype(int), N_CEN - 1))
    if run.get("side_left") is not None:  # each sample on the arm its angle gives (variant)
        return np.where(run["side"] & ~run["side_left"], b + N_SIDE, b)
    if not run["left"]:
        b = np.where(run["side"], b + N_SIDE, b)
    return b


N_TM = N_CEN + 2 * N_SIDE


def tmaze_maps(runs, spikes, subset=None):
    """Occupancy and spike counts per bin for each unit (speed > 3 cm/s)."""
    occ = np.zeros(N_TM)
    sc = {u: np.zeros(N_TM) for u in spikes}
    per_run = []
    for j, r in enumerate(runs):
        if subset is not None and j not in subset:
            continue
        b = tmaze_bin(r)
        good = r["v"] > 3
        o = np.bincount(b[good], minlength=N_TM) * r["dt"]
        occ += o
        rc = {}
        for u, spk in spikes.items():
            s = spk[(spk >= r["t"][0]) & (spk < r["t"][-1] + r["dt"])]
            si = np.clip(np.searchsorted(r["t"], s) - 1, 0, len(r["t"]) - 1)
            si = si[good[si]]
            c = np.bincount(b[si], minlength=N_TM).astype(float)
            sc[u] += c
            rc[u] = c
        per_run.append(dict(occ=o, counts=rc, left=r["left"]))
    return occ, sc, per_run


def tm_smooth(raw, occ):
    """Smooth each segment of the linear track separately (M: 5.57 cm Gaussian)."""
    out = np.full(N_TM, np.nan)
    sd = 5.57 / TM_BIN
    for lo, hi in [(0, N_CEN), (N_CEN, N_CEN + N_SIDE), (N_CEN + N_SIDE, N_TM)]:
        ok = occ[lo:hi] > 0
        r = np.where(ok, raw[lo:hi], 0.0)
        w = ndimage.gaussian_filter1d(ok.astype(float), sd, mode="constant")
        s = ndimage.gaussian_filter1d(r, sd, mode="constant")
        with np.errstate(invalid="ignore", divide="ignore"):
            seg = s / w
        seg[~ok] = np.nan
        out[lo:hi] = seg
    return out


def tm_fields(m):
    out = []
    for lo, hi in [(0, N_CEN), (N_CEN, N_CEN + N_SIDE), (N_CEN + N_SIDE, N_TM)]:
        for a, b, pk in fields_1d(m[lo:hi]):
            out.append((lo + a, lo + b, pk))
    return out


# ---------------------------------------------------------------- one file
def process_file(asset, do_waveforms=True, do_lfp=True, do_space=True):
    """All per-unit and per-pair measures of one session."""
    f = open_asset(asset["asset_id"])
    res = dict(path=asset["path"])
    subj = f["general/subject/subject_id"][()].decode()
    res["subject"] = subj
    res["genotype"] = f["general/subject/genotype"][()].decode()
    res["session"] = f["general/session_id"][()].decode() if "general/session_id" in f else asset["path"]
    u = f["units"]
    ct = u["cell_type"][:].astype(str)
    region = u["region"][:].astype(str)
    gid = u["global_id"][:]
    shank = u["shank"][:]
    drd2 = u["drd2_tagged"][:]
    sti = u["spike_times_index"][:].astype(np.int64)
    st_all = u["spike_times"][:]
    s0 = np.concatenate([[0], sti[:-1]])
    spikes = {k: np.sort(st_all[s0[k]:sti[k]]) for k in range(len(ct))}
    del st_all
    n_lfp = f["processing/ecephys/LFP/lfp/data"].shape[0]
    span = n_lfp / FS_LFP
    res["span"] = span
    lab, bst, bsp = _intervals(f["processing/behavior/brain_states"])
    dur = {s: float(np.sum((bsp - bst)[lab == s])) for s in ["awake", "quiet", "nrem", "rem"]}
    res["state_dur"] = dur
    rows = []
    for k in range(len(ct)):
        spk = spikes[k]
        r = dict(path=asset["path"], subject=subj, genotype=res["genotype"], unit=k, global_id=int(gid[k]),
                 cell_type=ct[k], type=TYPES.get(ct[k], "other"), region=region[k], shank=int(shank[k]),
                 drd2_tagged=bool(drd2[k]), n_spikes=len(spk), rate=len(spk) / span)
        for s in ["awake", "quiet", "nrem", "rem"]:
            m = lab == s
            r[f"n_{s}"] = count_in(spk, bst[m], bsp[m])
            r[f"rate_{s}"] = r[f"n_{s}"] / dur[s] if dur[s] > 0 else np.nan
        dw = dur["awake"] + dur["quiet"]
        r["rate_wake_aq"] = (r["n_awake"] + r["n_quiet"]) / dw if dw > 0 else np.nan
        rows.append(r)
    res["units"] = rows
    analyse = subj != EXCLUDED_SUBJECT
    typ = np.array([TYPES.get(c, "other") for c in ct])
    interest = [k for k in range(len(ct)) if typ[k] != "other"] if analyse else []
    for k in interest:
        rows[k]["burst_index"] = burst_index(spikes[k])

    # waveforms and sites
    elec = u["electrodes"][:]
    ei = u["electrodes_index"][:].astype(np.int64)
    e0 = np.concatenate([[0], ei[:-1]])
    lfp_el = f["processing/ecephys/LFP/lfp/electrodes"][:]
    el_to_col = {int(e): j for j, e in enumerate(lfp_el)}
    et = f["general/extracellular_ephys/electrodes"]
    gname = et["group_name"][:].astype(str)
    sen = et["shank_electrode_number"][:]
    res["electrodes"] = [dict(col=j, shank=gname[int(e)], shank_electrode_number=int(sen[int(e)]))
                         for j, e in enumerate(lfp_el)]
    res["has_waveforms"] = "waveforms_index_index" in u
    if do_waveforms and res["has_waveforms"]:
        for k in interest:
            mw = mean_waveform(u, k)
            if mw is None:
                continue
            rows[k]["mw"] = mw.astype(np.float32)  # for the same-day check
            if typ[k] not in ("GC", "MC", "nI", "wI"):
                continue
            tp, ch, at_end, seg, tp1 = waveform_features(mw)
            rows[k]["tp_ms"] = tp
            rows[k]["tp_first_ms"] = tp1
            rows[k]["tp_at_end"] = bool(at_end)
            rows[k]["d2"] = seg
            unit_el = elec[e0[k]:ei[k]]
            rows[k]["site_table"] = el_to_col.get(int(unit_el[ch]), -1) if ch < len(unit_el) else -1
    wide = "acquisition/ElectricalSeries" in f
    res["wideband"] = wide
    if do_waveforms and wide:
        exc = {k: spikes[k] for k in interest if typ[k] in ("GC", "MC", "nI", "wI")}
        if exc:
            ws = wideband_sites(f, exc)
            for k, (col, n, w, wr) in ws.items():
                rows[k]["site_wb"] = col
                rows[k]["site_wb_n"] = n
                if w is not None:
                    # filtered (300 Hz high-pass) mean at the site
                    tp, _, at_end, seg, tp1 = waveform_features(w[None, :])
                    rows[k]["tp_wbf_ms"] = tp
                    rows[k]["tp_wbf_first_ms"] = tp1
                    rows[k]["tp_wbf_at_end"] = bool(at_end)
                    rows[k]["d2_wbf"] = seg
                    # unfiltered mean at the site (C, gc-mc-classification)
                    tp, _, at_end, seg, tp1 = waveform_features(wr[None, :])
                    rows[k]["tp_wb_ms"] = tp
                    rows[k]["tp_wb_first_ms"] = tp1
                    rows[k]["tp_wb_at_end"] = bool(at_end)
                    rows[k]["d2_wb"] = seg
                    rows[k]["wb_raw"] = wr.astype(np.float32)

    # LFP: DS2 amplitude profile, DS2 histograms, phase modulation
    ds = f["processing/ecephys/dentate_spikes"]
    dtype = ds["type"][:].astype(str)
    ds2 = np.sort(ds["peak_time"][:][dtype == "DS2"])
    res["n_ds2"] = len(ds2)
    hil = np.flatnonzero(f["general/extracellular_ephys/electrodes/hilus_reference"][:])
    res["hilus_col"] = [el_to_col.get(int(h), -1) for h in hil]
    if do_lfp and analyse:
        prof, nused = ds2_amplitude_profile(f, ds2)
        res["ds2_profile"] = prof
        res["ds2_profile_n"] = nused
        for k in interest:
            if prof is not None:
                for key in ("site_table", "site_wb"):
                    c = rows[k].get(key, -1)
                    if c is not None and c >= 0:
                        rows[k]["ds2_amp_" + key.split("_")[1]] = float(prof[c])
        # DS2 peri-event histograms (2 ms bins, +-100 ms)
        edges = np.arange(-0.1, 0.1 + 1e-9, 0.002)
        cen = (edges[:-1] + edges[1:]) / 2
        for k in interest:
            if len(ds2) == 0:
                break
            d = lag_counts(ds2, spikes[k], -0.1, 0.1)
            h = np.histogram(d, edges)[0] / (len(ds2) * 0.002)
            pk = np.abs(cen) < 0.02
            bl = (np.abs(cen) > 0.05) & (np.abs(cen) < 0.1)
            base = h[bl].mean()
            rows[k]["ds2_ratio"] = h[pk].max() / base if base > 0 else np.nan
            rows[k]["ds2_peak_ms"] = float(cen[pk][np.argmax(h[pk])] * 1000)
            # control: DS2 times shifted by 0.5 s
            d2 = lag_counts(ds2 + 0.5, spikes[k], -0.1, 0.1)
            h2 = np.histogram(d2, edges)[0] / (len(ds2) * 0.002)
            b2 = h2[bl].mean()
            rows[k]["ds2_ratio_shift"] = h2[pk].max() / b2 if b2 > 0 else np.nan
        if len(hil) and res["hilus_col"][0] >= 0:
            m = lab == "awake"
            pm, tot = phase_modulation(f, res["hilus_col"][0], (bst[m], bsp[m]),
                                       {k: spikes[k] for k in interest if typ[k] in ("GC", "MC", "CA3")})
            res["phase_seconds"] = tot
            for (k, band), v in pm.items():
                for kk, vv in v.items():
                    rows[k][f"{band}_{kk}"] = vv

    # optogenetic suppression with 20 ms pulses
    if "intervals/light_pulses" in f and analyse:
        lp = f["intervals/light_pulses"]
        prot = lp["protocol"][:].astype(str)
        dur20 = np.isclose(lp["stop_time"][:] - lp["start_time"][:], 0.02, atol=0.002)
        on = np.sort(lp["start_time"][:][dur20 & (np.char.find(prot, "_20ms_") >= 0)])
        res["n_pulses20"] = len(on)
        if len(on):
            for k in interest:
                spk = spikes[k]

                def cnt(a, b):
                    return count_in(spk, on + a, on + b)
                resp = cnt(0.002, 0.015) / (0.013 * len(on))
                pre = cnt(-0.020, 0.0) / (0.020 * len(on))
                post = cnt(0.050, 0.200) / (0.150 * len(on))
                rows[k]["light_resp"] = resp
                rows[k]["light_pre"] = pre
                rows[k]["light_post"] = post
                # PETH in 1 ms bins from -20 to +200 ms, spike counts summed over pulses
                rows[k]["light_peth"] = np.histogram(lag_counts(on, spk, -0.020, 0.200),
                                                     PETH_EDGES)[0].astype(np.int64)
                rows[k]["light_n_pulses"] = len(on)

    # pairs: CCG tests on excitatory pairs recorded together
    pairs = []
    if analyse:
        gc = [k for k in interest if typ[k] == "GC"]
        mc = [k for k in interest if typ[k] == "MC"]
        ca3 = [k for k in interest if typ[k] == "CA3"]
        wake = (bst[lab == "awake"], bsp[lab == "awake"])
        nrem = (bst[lab == "nrem"], bsp[lab == "nrem"])

        def in_iv(spk, iv):
            a = np.searchsorted(iv[0], spk, side="right") - 1
            ok = a >= 0
            ok[ok] = spk[ok] < iv[1][a[ok]]
            return spk[ok]
        for a in gc:
            for b in mc:
                c = ccg(spikes[a], spikes[b])
                base, sig = ccg_test(c)
                fwd = two_consecutive(sig & CONN)
                rev_c = c[::-1]
                rb, rsig = ccg_test(rev_c)
                rev = two_consecutive(rsig & CONN)
                p = dict(pre=a, post=b, kind="GC-MC", same_shank=bool(shank[a] == shank[b]),
                         gc_to_mc=fwd, mc_to_gc=rev)
                if fwd:
                    p["tp_all"] = float((c[CONN] - base[CONN]).sum() / max(len(spikes[a]), 1))
                    f1, f2 = burst_spikes(spikes[a])
                    p["n_burst"] = len(f1)
                    p["tp_first"] = transmission(f1, spikes[b])
                    p["tp_second"] = transmission(f2, spikes[b])
                    wa = in_iv(spikes[a], wake)
                    na = in_iv(spikes[a], nrem)
                    p["n_wake"], p["n_nrem"] = len(wa), len(na)
                    p["tp_wake"] = transmission(wa, spikes[b])
                    p["tp_nrem"] = transmission(na, spikes[b])
                pairs.append(p)
        for group, name in [(gc, "GC-GC"), (mc, "MC-MC"), (ca3, "CA3-CA3")]:
            for i, a in enumerate(group):
                for b in group[i + 1:]:
                    c = ccg(spikes[a], spikes[b])
                    _, sig = ccg_test(c)
                    pairs.append(dict(pre=a, post=b, kind=name, same_shank=bool(shank[a] == shank[b]),
                                      sync=two_consecutive(sig & SYNC)))
    res["pairs"] = pairs
    # the authors' tables
    res["authors_mono"] = res["authors_sync"] = None
    if "processing/ecephys/monosynaptic_connections" in f:
        mono = f["processing/ecephys/monosynaptic_connections"]
        res["authors_mono"] = list(zip(mono["presynaptic_unit"][:].tolist(), mono["postsynaptic_unit"][:].tolist(),
                                       mono["connection"][:].astype(str).tolist()))
    if "processing/ecephys/zero_lag_synchrony" in f:
        zl = f["processing/ecephys/zero_lag_synchrony"]
        res["authors_sync"] = list(zip(zl["unit_1"][:].tolist(), zl["unit_2"][:].tolist()))

    # spatial
    if do_space and analyse:
        sp_units = {k: spikes[k] for k in interest if typ[k] in ("GC", "MC", "CA3")}
        if "intervals/trials" in f and "processing/behavior/t_maze_position" in f:
            res["tmaze"] = tmaze_session(f, sp_units)
        if "processing/behavior/open_field_position" in f:
            res["openfield"] = openfield_session(f, sp_units)
    f.close()
    return res


def tmaze_session(f, sp_units):
    arrays = _tmaze_arrays(f)
    runs = tmaze_runs(f, arrays=arrays)
    out = dict(n_runs=len(runs), n_left=sum(r["left"] for r in runs),
               arm_start_cm=[r["arm_start_cm"] for r in runs],
               other_arm=[(r["n_side"], r["n_other"], r["other_max_cm"], r["left"], r["end_left"], r["error"]) for r in runs])
    if len(runs) < 4:
        return out
    out.update(_tmaze_analyse(runs, sp_units))
    # variants on the run: from the lab's arm_start, and without excursions into the arm not chosen
    out["variants"] = {}
    for name, kw in [("arm_start", dict(start="arm_start")), ("chosen_arm_only", dict(drop_other_arm=True)),
                     ("arm_by_angle", dict(arm_by_angle=True))]:
        rv = tmaze_runs(f, arrays=arrays, **kw)
        if len(rv) >= 4:
            out["variants"][name] = _tmaze_analyse(rv, sp_units)
    return out


def _tmaze_analyse(runs, sp_units):
    occ, sc, per_run = tmaze_maps(runs, sp_units)
    out = dict(occ=occ, maps={}, fields={}, info={}, splitter={})
    ok = occ > 0
    for k in sp_units:
        raw = np.where(ok, sc[k] / np.where(ok, occ, 1), np.nan)
        m = tm_smooth(raw, occ)
        out["maps"][k] = m
        out["fields"][k] = tm_fields(m)
        out["info"][k] = skaggs_info(occ, m)
    # splitters: central-arm fields of the left-run or right-run maps
    for k in sp_units:
        res_k = []
        for side in (True, False):
            idx = [j for j, r in enumerate(per_run) if r["left"] == side]
            o = sum(per_run[j]["occ"] for j in idx) if idx else np.zeros(N_TM)
            s = sum(per_run[j]["counts"][k] for j in idx) if idx else np.zeros(N_TM)
            okk = o > 0
            m = tm_smooth(np.where(okk, s / np.where(okk, o, 1), np.nan), o)
            for a, b, pk in fields_1d(m[:N_CEN]):
                res_k.append((a, b))
        out["splitter"][k] = _splitter_test(per_run, k, res_k)
    return out


def _splitter_test(per_run, k, fields):
    """Two-way ANOVA (position x choice) on per-run rates in each central field (M).

    Returns the smallest choice P over the unit's fields; fields with too little
    to fit, a failed fit or a NaN P (a degenerate fit) are counted in n_failed
    and do not enter it."""
    import pandas as pd
    import statsmodels.api as sm
    from statsmodels.formula.api import ols
    best = None
    n_failed = 0  # fields with too little to fit, a failed fit or a NaN p
    for a, b in fields:
        rows = []
        for j, r in enumerate(per_run):
            for x in range(a, b + 1):
                if r["occ"][x] > 0:
                    rows.append(dict(rate=r["counts"][k][x] / r["occ"][x], pos=x, choice=int(r["left"])))
        d = pd.DataFrame(rows)
        if d.empty or d.choice.nunique() < 2 or d.pos.nunique() < 2:
            n_failed += 1
            continue
        try:
            t = sm.stats.anova_lm(ols("rate ~ C(pos) + C(choice)", data=d).fit(), typ=2)
            p = float(t.loc["C(choice)", "PR(>F)"])
        except Exception:
            n_failed += 1
            continue
        if not np.isfinite(p):  # a degenerate fit (no variance) gives NaN; it is not a test
            n_failed += 1
            continue
        best = p if best is None else min(best, p)
    return dict(n_fields=len(fields), p=best, n_failed=n_failed)


OF_SESSIONS = ["Old", "New", "Oldlast", "Old_Curtain", "New_Curtain", "Lroom_Old", "Lroom_New"]


def openfield_session(f, sp_units):
    g = f["processing/behavior/open_field_position"]
    out = {}
    for name in OF_SESSIONS:
        if name not in g:
            continue
        ss = g[name]
        if ss["data"].attrs.get("unit") != "meters":
            continue
        xy = ss["data"][:] * ss["data"].attrs["conversion"] * 100.0  # cm
        t = ss["timestamps"][:]
        half = len(t) // 2
        sess = dict(duration=float(t[-1] - t[0]), maps={}, half_r={}, field={})
        occ = None
        for k, spk in sp_units.items():
            m, occ = of_map(t, xy, spk)
            m1, _ = of_map(t, xy, spk, slice(0, half))
            m2, _ = of_map(t, xy, spk, slice(half, None))
            sess["maps"][k] = m.astype(np.float32)
            sess["half_r"][k] = corr_maps(m1, m2)
            fl = field_2d(m)
            sess["field"][k] = None if fl is None else (fl[0], fl[1])
        sess["occ"] = occ
        out[name] = sess
    return out
