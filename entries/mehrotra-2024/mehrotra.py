"""Loading and UP onset measures for Mehrotra, Levenstein et al. (2024), Current Biology 34, 3043.

doi:10.1016/j.cub.2024.05.048. The paper's retrosplenial cortex (RSC) data are dandiset 000987;
its postsubiculum (PoSub) data are dandiset 000939 (Duszkiewicz et al. 2024). Files are streamed
from the archive at a pinned version with remfile and h5py; nothing is written to disk.

Where the parameters come from:

- UP and DOWN state detection (`detect_down_states`) follows detectDOWNs_RSC.py of
  https://github.com/PeyracheLab/MehrotraLevenstein_2023 at commit
  4ee34f34793c147ac08bf5fffe44ff03d17f8e35, as the criterion of fig5f-rsc-pmr-onset gives it,
  and the STAR Methods (UP and DOWN state detection): spikes of all units in NREM in 10 ms bins,
  each unit smoothed by a Gaussian of 2 bins s.d. (pandas rolling window of 100 bins) and summed;
  DOWN states are the samples below the 20th percentile; intervals shorter than 10 ms dropped,
  those closer than 20 ms merged, then those shorter than 30 ms or longer than 500 ms dropped;
  UP states are the intervals between consecutive DOWN states; DOWN states are then restricted to
  NREM.
- The PETH, PMR and UP onset delay (`pmr_onset`) follow Figure5F.py and Figure5C.py at the same
  commit, as the criterion gives them: pynapple's compute_eventcorrelogram with 5 ms bins, a
  0.255 s window, ep = the UP states and norm = True; smoothed by a Gaussian of 2 bins s.d.
  (rolling window of 8 bins); cut to 0 to 0.155 s after DU; UP onset delay is the first time
  the normalized PETH exceeds 0.5 and PMR its maximum in that interval; a unit that never
  exceeds 0.5 is left out. The STAR Methods (Sequential Activation at UP onset) give the 50% of
  the mean rate and the 150 ms.
- `ONSET_THRESHOLD` (0.5) and `ONSET_WINDOW` come from the same passages.
- The putative excitatory (EX) rule (`EX_MAX_RATE_HZ`, `EX_MIN_TROUGH_TO_PEAK_MS`) is from the
  STAR Methods (Spike sorting and unit classification): trough-to-peak above 0.35 ms and mean
  rate below 10 Hz in open field exploration. The RSC files hold no waveforms, so only the rate
  half can be applied to them.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import pynapple as nap
import remfile
import requests

RSC_DANDISET = "000987"
RSC_VERSION = "0.261003.2342"
CODE_REPO = "https://github.com/PeyracheLab/MehrotraLevenstein_2023"
CODE_COMMIT = "4ee34f34793c147ac08bf5fffe44ff03d17f8e35"

API = "https://api.dandiarchive.org/api"

# detectDOWNs_RSC.py
BIN_SIZE = 0.01           # s
SMOOTH_SD_BINS = 2        # int(smoothing_window / bin_size) with smoothing_window = 0.02 s
SMOOTH_WINDOW_BINS = 100
DOWN_PERCENTILE = 20
# Figure5F.py
PETH_BIN = 0.005          # s
PETH_WINDOW = 0.255       # s
PETH_SMOOTH_WINDOW = 8    # bins
PETH_SMOOTH_SD = 2        # bins
ONSET_WINDOW = (0.0, 0.155)
ONSET_THRESHOLD = 0.5
# STAR Methods, Spike sorting and unit classification
EX_MAX_RATE_HZ = 10.0
EX_MIN_TROUGH_TO_PEAK_MS = 0.35


def list_assets(dandiset: str = RSC_DANDISET, version: str = RSC_VERSION) -> list[dict]:
    """Assets of a dandiset version, sorted by path."""
    url = f"{API}/dandisets/{dandiset}/versions/{version}/assets/?page_size=200"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r.get("next")
    return sorted(out, key=lambda a: a["path"])


def open_asset(asset: dict) -> h5py.File:
    return h5py.File(remfile.File(f"{API}/assets/{asset['asset_id']}/download/"), "r")


def _intervals(h, name) -> nap.IntervalSet:
    g = h[f"intervals/{name}"]
    return nap.IntervalSet(start=g["start_time"][:], end=g["stop_time"][:])


def _str(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def load_rsc_session(asset: dict) -> dict:
    """Spikes, NREM (SWS), the stored DOWN and UP states and the behavioural epochs of one file."""
    h = open_asset(asset)
    st = h["units/spike_times"][:]
    idx = h["units/spike_times_index"][:]
    ids = h["units/id"][:]
    bounds = np.concatenate([[0], idx])
    spikes = nap.TsGroup({int(i): nap.Ts(t=np.sort(st[bounds[k]:bounds[k + 1]]))
                          for k, i in enumerate(ids)})
    ep = h["intervals/epochs"]
    tags = [_str(t) for t in ep["tags"][:]]
    starts, ends = ep["start_time"][:], ep["stop_time"][:]
    epochs = {lab: nap.IntervalSet(start=[s for s, t in zip(starts, tags) if t == lab],
                                   end=[e for e, t in zip(ends, tags) if t == lab])
              for lab in sorted(set(tags))}
    out = dict(
        path=asset["path"],
        identifier=_str(h["identifier"][()]),
        subject=_str(h["general/subject/subject_id"][()]),
        genotype=_str(h["general/subject/genotype"][()]),
        spikes=spikes,
        sws=_intervals(h, "SWS"),
        down=_intervals(h, "DOWN"),
        up=_intervals(h, "UP"),
        epochs=epochs,
        unit_location=[_str(x) for x in h["units/location"][:]],
        unit_group=h["units/group"][:],
        spike_unsorted=int(sum(np.any(np.diff(st[bounds[k]:bounds[k + 1]]) < 0)
                               for k in range(len(ids)))),
    )
    pos = h["acquisition/Position/x/timestamps"][:]
    out["position_range"] = (float(pos[0]), float(pos[-1]), len(pos))
    return out


def load_all_rsc(n_threads: int = 7) -> list[dict]:
    with ThreadPoolExecutor(n_threads) as ex:
        return list(ex.map(load_rsc_session, list_assets()))


def detect_down_states(spikes: nap.TsGroup, sws: nap.IntervalSet,
                       percentile: float = DOWN_PERCENTILE, restrict_up: bool = False):
    """DOWN and UP states as detectDOWNs_RSC.py computes them (see the module docstring).

    With `restrict_up`, the UP states are also restricted to NREM, as detectDOWNs_PoSub.py does
    (`up_ep = new_sws_ep.intersect(up_ep)`); used for the PoSub re-detection."""
    rates = spikes.count(BIN_SIZE, sws)
    df = pd.DataFrame(rates.values, index=rates.index)
    total = df.rolling(window=SMOOTH_WINDOW_BINS, win_type="gaussian", center=True,
                       min_periods=1).mean(std=SMOOTH_SD_BINS).sum(axis=1)
    total = nap.Tsd(t=total.index.values, d=total.values)
    idx = total.threshold(np.percentile(total.values, percentile), "below")
    down = idx.time_support
    down = nap.IntervalSet(start=down["start"], end=down["end"])
    down = down.drop_short_intervals(BIN_SIZE)
    down = down.merge_close_intervals(BIN_SIZE * 2)
    down = down.drop_short_intervals(BIN_SIZE * 3)
    down = down.drop_long_intervals(BIN_SIZE * 50)
    up = nap.IntervalSet(start=down["end"][:-1], end=down["start"][1:])
    down = sws.intersect(down)
    if restrict_up:
        up = sws.intersect(up)
    return down, up


def du_peth(spikes: nap.TsGroup, up: nap.IntervalSet) -> pd.DataFrame:
    """Normalized, smoothed DU-PETH of each unit (lags as index), as Figure5F.py."""
    cc = nap.compute_eventcorrelogram(spikes, nap.Ts(t=up["start"]), binsize=PETH_BIN,
                                      windowsize=PETH_WINDOW, ep=up, norm=True)
    cc = pd.DataFrame(cc)
    return cc.rolling(window=PETH_SMOOTH_WINDOW, win_type="gaussian", center=True,
                      min_periods=1).mean(std=PETH_SMOOTH_SD)


def pmr_onset(peth: pd.DataFrame, threshold: float = ONSET_THRESHOLD,
              window: tuple = ONSET_WINDOW) -> pd.DataFrame:
    """UP onset delay (s) and PMR per unit from a DU-PETH; `entered` False when never above threshold."""
    lags = peth.index.values
    sel = peth.loc[(lags >= window[0] - 1e-9) & (lags <= window[1] + 1e-9)]
    rows = []
    for u in sel.columns:
        v = sel[u].values
        above = np.where(v > threshold)[0]
        rows.append(dict(unit=u, entered=len(above) > 0,
                         onset=sel.index.values[above[0]] if len(above) else np.nan,
                         pmr=np.nanmax(v) if len(above) else np.nan))
    return pd.DataFrame(rows).set_index("unit")


def interval_match(a: nap.IntervalSet, b: nap.IntervalSet, tol: float = 0.0101) -> dict:
    """Fraction of intervals of `a` with an interval of `b` whose start and end are within `tol` s."""
    sa, ea = a["start"], a["end"]
    sb, eb = b["start"], b["end"]
    j = np.clip(np.searchsorted(sb, sa), 1, len(sb) - 1)
    k = np.where(np.abs(sb[j - 1] - sa) < np.abs(sb[j] - sa), j - 1, j)
    same = (np.abs(sb[k] - sa) <= tol) & (np.abs(eb[k] - ea) <= tol)
    return dict(n_a=len(sa), n_b=len(sb), matched=int(same.sum()), fraction=float(same.mean()))


def rate_in(spikes: nap.TsGroup, ep: nap.IntervalSet) -> pd.Series:
    """Mean rate (Hz) of each unit within `ep`."""
    return pd.Series({u: len(spikes[u].restrict(ep)) / ep.tot_length() for u in spikes.keys()})


# ---------------------------------------------------------------------------------------------
# PoSub data, dandiset 000939 (Duszkiewicz et al. 2024), used by the claims with data: elsewhere.
#
# The 16 sessions are those for which the paper's code holds DOWN and UP event files
# (Analysis/OutputFiles/<session>.evt.py.dow and .upp, written by detectDOWNs_PoSub.py), read here
# from the repository at CODE_COMMIT. These files are the study's DOWN and UP states; the criterion
# of fig5c-posub-pmr-onset names them. Times in them are in ms from the start of the recording.
# Unit position along the probe is the `rel_y` of the electrode with the largest waveform
# (`units/electrode_index`); larger `rel_y` is taken as dorsal (see the notebook for the check).
# Putative excitatory units are the file's `is_excitatory` flag.

POSUB_DANDISET = "000939"
POSUB_VERSION = "0.261016.2310"
POSUB_SESSIONS = ["A3701-191119", "A3702-191126", "A3705-200306", "A3706-200313", "A3707-200317",
                  "A3708-200317b", "A3709-200601", "A3710-200609", "A3711-200810b", "A3712-200903a",
                  "A3713-200909a", "A3716-201015b", "A3717-201021", "A3723-201115", "A3728-210309b",
                  "A3730-210323b"]
RAW = f"https://raw.githubusercontent.com/PeyracheLab/MehrotraLevenstein_2023/{CODE_COMMIT}/Analysis/OutputFiles"


def read_event_file(session: str, ext: str) -> nap.IntervalSet:
    """DOWN (`dow`) or UP (`upp`) intervals from the paper's code repository, in seconds."""
    txt = requests.get(f"{RAW}/{session}.evt.py.{ext}", timeout=60).text
    t = np.array([float(line.split("\t")[0]) for line in txt.strip().splitlines()]) / 1000.0
    return nap.IntervalSet(start=t[0::2], end=t[1::2])


def load_posub_session(asset: dict, session: str) -> dict:
    """Units (spike times, EX flag, trough-to-peak, probe position), sleep states, epochs, events."""
    h = open_asset(asset)
    u = h["units"]
    st = u["spike_times"][:]
    idx = u["spike_times_index"][:]
    bounds = np.concatenate([[0], idx])
    n = len(idx)
    spikes = nap.TsGroup({k: nap.Ts(t=st[bounds[k]:bounds[k + 1]]) for k in range(n)})
    rel_y = h["general/extracellular_ephys/electrodes/rel_y"][:]
    el = u["electrode_index"][:]
    units = pd.DataFrame(dict(
        ex=u["is_excitatory"][:].astype(bool), fs=u["is_fast_spiking"][:].astype(bool),
        hd=u["is_head_direction"][:].astype(bool), trough_to_peak=u["trough_to_peak"][:],
        electrode=el, position=rel_y[el]))
    ss = h["intervals/sleep_states"]
    states = np.array([_str(x) for x in ss["state"][:]])
    s0, s1 = ss["start_time"][:].astype(float), ss["stop_time"][:].astype(float)
    nrem = nap.IntervalSet(start=s0[states == "nrem"], end=s1[states == "nrem"])
    ep = h["intervals/epochs"]
    epochs = pd.DataFrame(dict(tag=[_str(t) for t in ep["tags"][:]], start=ep["start_time"][:],
                               end=ep["stop_time"][:]))
    hc = epochs[epochs.tag == "home_cage"]
    home_cage = nap.IntervalSet(start=hc.start.values, end=hc.end.values)
    return dict(session=session, path=asset["path"], identifier=_str(h["identifier"][()]),
                spikes=spikes, units=units, nrem=nrem, epochs=epochs, home_cage=home_cage,
                # NREM within the home cage (sleep) epochs, as detectDOWNs_PoSub.py intersects the
                # sleep scoring with the sleep epochs (`newsleep_ep.intersect(sws_ep1)`).
                nrem_hc=nrem.intersect(home_cage),
                rel_y=rel_y, n_spikes=len(st),
                spike_unsorted=int(sum(np.any(np.diff(st[bounds[k]:bounds[k + 1]]) < 0) for k in range(n))),
                down=read_event_file(session, "dow"), up=read_event_file(session, "upp"))


def load_all_posub(n_threads: int = 8) -> list[dict]:
    assets = list_assets(POSUB_DANDISET, POSUB_VERSION)
    by_subject = {a["path"].split("/")[0].replace("sub-", ""): a for a in assets}
    jobs = [(by_subject[s.split("-")[0]], s) for s in POSUB_SESSIONS]
    with ThreadPoolExecutor(n_threads) as ex:
        return list(ex.map(lambda j: load_posub_session(*j), jobs))


def peth_events(spikes: nap.TsGroup, events: np.ndarray, rate_ep: nap.IntervalSet,
                window: float = 0.255) -> pd.DataFrame:
    """PETH of spikes restricted to `rate_ep` around `events` (not restricted), divided by each
    unit's rate in `rate_ep` and smoothed as `du_peth`; as the UD and DOWN-duration PETHs of
    Figure1G.py and Figure1H.py (crossCorr of spikes restricted to the UP states, divided by the
    rate in the UP states)."""
    g = spikes.restrict(rate_ep)
    ev = nap.Ts(t=np.sort(events))
    cc = nap.compute_eventcorrelogram(g, ev, binsize=PETH_BIN, windowsize=window,
                                      ep=nap.IntervalSet(start=min(ev.t[0], g.time_support.start[0]) - 10,
                                                         end=max(ev.t[-1], g.time_support.end[-1]) + 10),
                                      norm=False)
    rates = pd.Series({k: len(g[k]) / rate_ep.tot_length() for k in g.keys()})
    cc = pd.DataFrame(cc) / rates
    return cc.rolling(window=PETH_SMOOTH_WINDOW, win_type="gaussian", center=True,
                      min_periods=1).mean(std=PETH_SMOOTH_SD)


def ud_time(peth: pd.DataFrame, threshold: float = ONSET_THRESHOLD) -> pd.Series:
    """Timing at the UD transition as Figure1G.py: the last bin between -150 and -5 ms above
    threshold, for units that also cross after +5 ms (others NaN)."""
    lags = np.round(peth.index.values, 6)
    pre = peth.loc[(lags >= -0.150) & (lags <= -0.005)] > threshold
    post = peth.loc[lags >= 0.005] > threshold
    out = {}
    for u in peth.columns:
        if pre[u].any() and post[u].any():
            out[u] = pre.index.values[np.where(pre[u].values)[0][-1]]
        else:
            out[u] = np.nan
    return pd.Series(out)


# ---------------------------------------------------------------------------------------------
# LFP high gamma around DU and UD transitions (Figure 2; no code in the repository).
#
# STAR Methods, Peri-Event Time Histograms, paragraph 2: LFP at 1.25 kHz further downsampled to
# 625 Hz (here every second sample, as detectDOWNs_PoSub.py downsamples with lfp[::5]), filtered
# 70 to 150 Hz with a third-order Butterworth filter (applied forward and backward, filtfilt, a
# standard choice), smoothed with a Gaussian of 32 ms s.d. and aligned to +/- 1 s around the event.
# How power is taken from the filtered signal is not given: the absolute value of the Hilbert
# transform and the square are both computed (claims file, fig2f-gamma-travels, reading 1).
# STAR Methods, Delta peak detection: LFP downsampled to 250 Hz (every fifth sample), filtered
# 0.5 to 4 Hz with a second-order Butterworth filter, peaks found with scipy.signal.find_peaks
# above 3 s.d. of the filtered NREM signal. The channel is not given; the channel at the middle of
# the probe is used (a standard choice; the delta waves are synchronous along the probe, Figure S2).
# Each NREM interval is filtered on its own, so no filter runs across a gap.

LFP_FS = 1250.0
GAMMA_FS = 625.0
GAMMA_BAND = (70.0, 150.0)
GAMMA_ORDER = 3
GAMMA_SMOOTH_SD = 0.032   # s
DELTA_FS = 250.0
DELTA_BAND = (0.5, 4.0)
DELTA_ORDER = 2
DELTA_SD = 3.0
LFP_HALF_WINDOW = 1.0     # s


def lfp_event_averages(asset: dict, nrem: nap.IntervalSet, events: dict,
                       max_chunk_s: float = 600.0) -> dict:
    """Event-averaged high-gamma power per channel, for each event set in `events` (name ->
    times, s) and for delta peaks, under both power readings.

    Returns dict with 'lags' (s), 'channels' (indices kept, not faulty), 'rel_y',
    'delta_peaks' (s), 'delta_channel', and 'avg'[(power, event)] = array (lags x channels),
    with 'n'[(power, event)] the number of events averaged."""
    from scipy.ndimage import gaussian_filter1d
    from scipy.signal import butter, filtfilt, find_peaks, hilbert, sosfiltfilt

    h = open_asset(asset)
    el = h["general/extracellular_ephys/electrodes"]
    faulty = el["is_faulty"][:] if "is_faulty" in el else np.zeros(len(el["id"]), bool)
    rel_y = el["rel_y"][:]
    keep = np.where(~faulty)[0]
    mid = keep[np.argsort(rel_y[keep])[len(keep) // 2]]
    d = h["processing/ecephys/LFP/LFP/data"]
    t0 = float(h["processing/ecephys/LFP/LFP/starting_time"][()])
    sos_g = butter(GAMMA_ORDER, GAMMA_BAND, btype="band", fs=GAMMA_FS, output="sos")
    b_d, a_d = butter(DELTA_ORDER, DELTA_BAND, btype="band", fs=DELTA_FS)
    half = int(round(LFP_HALF_WINDOW * GAMMA_FS))
    lags = np.arange(-half, half + 1) / GAMMA_FS
    sigma = GAMMA_SMOOTH_SD * GAMMA_FS
    sums, counts = {}, {}
    delta_parts = []
    gamma_store = []   # (start time, power arrays) kept to align delta peaks after the threshold
    scale = {}         # one constant per channel and power reading, so float16 storage cannot overflow
    for s0, s1 in zip(nrem["start"], nrem["end"]):
        a = int(np.ceil((s0 - t0) * LFP_FS))
        b = min(int(np.floor((s1 - t0) * LFP_FS)), d.shape[0])
        if b - a < 4 * LFP_FS:
            continue
        a -= a % 10  # common grid for 625 Hz and 250 Hz samples
        raw = d[a:b, :]
        x = raw[::2, :][:, keep].astype(np.float32)
        tg = t0 + (a + 2 * np.arange(len(x))) / LFP_FS
        xd = raw[::5, mid].astype(np.float64)
        td = t0 + (a + 5 * np.arange(len(xd))) / LFP_FS
        delta_parts.append((td, filtfilt(b_d, a_d, xd)))
        g = sosfiltfilt(sos_g, x, axis=0).astype(np.float32)
        pw = {"abs_hilbert": np.abs(hilbert(g, axis=0)).astype(np.float32),
              "square": (g ** 2).astype(np.float32)}
        del g
        for k in pw:
            pw[k] = gaussian_filter1d(pw[k], sigma, axis=0)
        for ev_name, ev in events.items():
            _accumulate(sums, counts, pw, ev, tg, half, ev_name)
        for k, v in pw.items():
            if k not in scale:
                scale[k] = np.maximum(v.max(0), 1e-6)
        gamma_store.append((tg, {k: (v / scale[k]).astype(np.float16) for k, v in pw.items()}))
        del pw, raw, x
    sd = np.std(np.concatenate([p for _, p in delta_parts]))
    peaks = []
    for td, p in delta_parts:
        i, _ = find_peaks(p, height=DELTA_SD * sd)
        peaks.append(td[i])
    peaks = np.concatenate(peaks) if peaks else np.array([])
    for tg, pw in gamma_store:
        _accumulate(sums, counts, {k: v.astype(np.float32) * scale[k] for k, v in pw.items()}, peaks, tg, half,
                    "delta_peak")
    avg = {k: sums[k] / counts[k] for k in sums}
    return dict(lags=lags, channels=keep, rel_y=rel_y[keep], delta_peaks=peaks, delta_channel=int(mid),
                avg=avg, n=dict(counts))


def _accumulate(sums, counts, pw, ev, tg, half, ev_name):
    ev = np.asarray(ev)
    sel = ev[(ev >= tg[0]) & (ev <= tg[-1])]
    idx = np.round((sel - tg[0]) * GAMMA_FS).astype(int)
    idx = idx[(idx - half >= 0) & (idx + half < len(tg))]
    for k, v in pw.items():
        key = (k, ev_name)
        if len(idx):
            w = np.stack([v[i - half:i + half + 1] for i in idx]).sum(0)
            sums[key] = sums.get(key, 0) + w
        counts[key] = counts.get(key, 0) + len(idx)


def max_slope_time(avg: np.ndarray, lags: np.ndarray, window: tuple, sign: int = 1) -> np.ndarray:
    """Per channel, the lag at which the derivative of the averaged power is largest (sign=+1) or
    most negative (sign=-1) within `window` (s); Methods, Sequential Activation at UP onset."""
    der = np.gradient(avg, lags, axis=0) * sign
    w = (lags >= window[0] - 1e-9) & (lags <= window[1] + 1e-9)
    return lags[w][np.argmax(der[w], axis=0)]


# ---------------------------------------------------------------------------------------------
# HD tuning and behavioural correlates (Figure 1B, Figure S1D to S1F).
#
# STAR Methods, HD tuning curves and tuning metrics: tuning curves are spike counts over time
# spent per 1 degree bin, smoothed with a Gaussian of 3 s.d. (here 3 bins, circular); HD
# information is sum_i lambda_i log2(lambda_i / lambda) p_i (bits/s as printed; bits/spike, the
# same divided by lambda, is shown as a variant); speed and AHV scores are Pearson correlations of
# the spike train in 0.01 s bins smoothed with a Gaussian of 50 ms s.d. with linear speed and
# angular head velocity, the AHV score computed separately for clockwise and counterclockwise turns
# and the larger absolute value kept. Resultant vector length and peak rate are taken from the
# tuning curve (the Methods do not define them; the standard definitions are used). The square
# arena epoch (`wake_square`) is the open field exploration (Methods, Behavioral procedures).
# Spike counts are taken in the bins of the 100 Hz tracking frames (0.01 s).

def hd_metrics(asset: dict, spikes: nap.TsGroup, epoch: nap.IntervalSet) -> pd.DataFrame:
    from scipy.ndimage import gaussian_filter1d
    h = open_asset(asset)
    hd_t = h["processing/behavior/CompassDirection/head-direction/timestamps"][:]
    hd = h["processing/behavior/CompassDirection/head-direction/data"][:]
    xy = h["processing/behavior/Position/position/data"][:]
    inside = np.zeros(len(hd_t), bool)
    for s0, s1 in zip(epoch["start"], epoch["end"]):
        inside |= (hd_t >= s0) & (hd_t <= s1)
    t, a, p = hd_t[inside], hd[inside], xy[inside]
    ok = np.isfinite(a) & np.all(np.isfinite(p), 1)
    dt = np.median(np.diff(t))
    edges = np.concatenate([t - dt / 2, [t[-1] + dt / 2]])
    okt = ok & np.r_[True, np.diff(t) < 1.5 * dt]   # frames not following a tracking gap
    occ = np.histogram(np.mod(a[okt], 2 * np.pi), bins=360, range=(0, 2 * np.pi))[0] * dt
    speed = np.r_[0, np.hypot(np.diff(p[:, 0]), np.diff(p[:, 1])) / np.diff(t)]   # cm/s
    ahv = np.r_[0, np.angle(np.exp(1j * np.diff(a))) / np.diff(t)]                  # rad/s
    good = ok & np.r_[False, np.diff(t) < 1.5 * dt] & np.isfinite(speed) & np.isfinite(ahv)
    sig = 0.05 / dt
    centers = (np.arange(360) + 0.5) * 2 * np.pi / 360
    rows = []
    T = epoch.tot_length()
    for u in spikes.keys():
        st = spikes[u].t
        cnt = np.histogram(st, edges)[0].astype(float)
        tc_cnt = np.histogram(np.mod(a[okt], 2 * np.pi), bins=360, range=(0, 2 * np.pi), weights=cnt[okt])[0]
        tc = gaussian_filter1d(tc_cnt, 3, mode="wrap") / np.maximum(gaussian_filter1d(occ, 3, mode="wrap"), 1e-9)
        pocc = occ / occ.sum()
        lam = (tc * pocc).sum()
        with np.errstate(divide="ignore", invalid="ignore"):
            info = np.nansum(tc * np.log2(tc / lam) * pocc)
        rvl = np.abs((tc * np.exp(1j * centers)).sum()) / tc.sum() if tc.sum() > 0 else np.nan
        sm = gaussian_filter1d(cnt, sig)
        sp_score = np.corrcoef(sm[good], speed[good])[0, 1]
        cw, ccw = good & (ahv > 0), good & (ahv < 0)
        a1 = np.corrcoef(sm[cw], ahv[cw])[0, 1]
        a2 = np.corrcoef(sm[ccw], ahv[ccw])[0, 1]
        ahv_score = a1 if abs(a1) >= abs(a2) else a2
        n_ep = len(spikes[u].restrict(epoch))
        rows.append(dict(unit=u, rate=n_ep / T, hd_info=info, hd_info_per_spike=info / lam if lam > 0 else np.nan,
                         rvl=rvl, peak_rate=tc.max(), speed_score=sp_score, ahv_score=ahv_score))
    return pd.DataFrame(rows).set_index("unit")


# ---------------------------------------------------------------------------------------------
# Bayesian decoding of HD from dorsal and ventral PoSub (Figure S1J; no code in the repository).
#
# STAR Methods, Isomap Projection and Decoding, last paragraph: Bayesian decoding as pynapple's
# decode_1d (Poisson spike counts, uniform prior; reimplemented here in matrix form) in 50 ms bins,
# keeping UP state bins where at least 5 HD cells spike in both the dorsal and the ventral
# population. Tuning curves come from the square arena epoch in 60 bins of 6 degrees (pynapple's
# usual binning for decoding; a standard choice), without smoothing.

DECODE_BIN = 0.05
DECODE_MIN_CELLS = 5
TC_BINS = 60


def hd_tuning_curves(asset: dict, spikes: nap.TsGroup, epoch: nap.IntervalSet, nb: int = TC_BINS):
    h = open_asset(asset)
    t = h["processing/behavior/CompassDirection/head-direction/timestamps"][:]
    a = h["processing/behavior/CompassDirection/head-direction/data"][:]
    feat = nap.Tsd(t=t, d=np.mod(a, 2 * np.pi)).restrict(epoch)
    feat = feat[np.isfinite(feat.values)]
    tc = nap.compute_1d_tuning_curves(spikes, feat, nb_bins=nb, minmax=(0, 2 * np.pi))
    return tc  # DataFrame, index bin centres, columns units


def decode_hd(counts: np.ndarray, tc: np.ndarray, centres: np.ndarray, tau: float = DECODE_BIN) -> np.ndarray:
    """Maximum a posteriori HD per bin, Poisson likelihood and uniform prior (as decode_1d).
    `counts` is bins x cells, `tc` angle bins x cells (Hz)."""
    f = np.maximum(tc, 1e-6).T
    logp = counts @ np.log(f) - tau * f.sum(0)[None, :]
    return centres[np.argmax(logp, axis=1)]


# ---------------------------------------------------------------------------------------------
# Rat frontal cortex, CRCNS fcx-1 (Watson et al. 2016), for fig5e-fc-pmr-onset.
#
# The data set's tar.gz archives are streamed from the public CRCNS bucket (docs/archives.md,
# CRCNS) and read only up to the members needed: <session>_SStable.mat (spike times in seconds
# of the stable, good units), <session>_CellIDs.mat (EAll: excitatory units, 1-based indices into
# SStable), <session>_UPDOWNINtervals.mat (the data set's UP and DOWN states, and the spike-based ON
# and OFF periods). Figure5E.py reads the same recordings in another format (buzcode files
# *.SlowWaves.events.mat and *.CellClass.cellinfo.mat), which the data set does not hold.

CRCNS = "https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-1/live"
FCX_MEMBERS = ("SStable", "CellIDs", "UPDOWNINtervals")


def fcx_sessions() -> list[str]:
    import re
    txt = requests.get(f"{CRCNS[:-len('/fcx-1/live')]}/?list-type=2&prefix=fcx-1/live/data/", timeout=60).text
    return sorted(k.split("/")[-1].replace(".tar.gz", "") for k in re.findall(r"<Key>(.*?\.tar\.gz)</Key>", txt))


def fcx_checksums() -> dict:
    txt = requests.get(f"{CRCNS}/checksums.md5", timeout=60).text
    out = {}
    for line in txt.splitlines():
        p = line.split()
        if len(p) == 2:
            out[p[1].split("/")[-1]] = p[0]
    return out


def load_fcx_session(session: str) -> dict:
    import io
    import tarfile
    import fsspec
    import scipy.io as sio
    f = fsspec.open(f"{CRCNS}/data/{session}.tar.gz", block_size=2 ** 22).open()
    tf = tarfile.open(fileobj=f, mode="r|gz")
    got = {}
    for mem in tf:
        for k in FCX_MEMBERS:
            if mem.name.endswith(f"_{k}.mat"):
                got[k] = sio.loadmat(io.BytesIO(tf.extractfile(mem).read()), squeeze_me=True, struct_as_record=False)
        if len(got) == len(FCX_MEMBERS):
            break
    f.close()
    st = got["SStable"]
    cells = [np.atleast_1d(np.asarray(c, dtype=float)) for c in np.atleast_1d(st["S_CellFormat"])]
    spikes = nap.TsGroup({i: nap.Ts(t=np.sort(c)) for i, c in enumerate(cells)})
    ids = got["CellIDs"]["CellIDs"]
    eall = np.atleast_1d(ids.EAll).astype(int) - 1
    ud = got["UPDOWNINtervals"]
    def iset(key):
        a = np.atleast_2d(ud[f"{key}TimePairFormat"]).astype(float)
        return nap.IntervalSet(start=a[:, 0], end=a[:, 1]) if a.size else nap.IntervalSet(start=[], end=[])
    return dict(session=session, spikes=spikes, ex=eall, edef=np.atleast_1d(ids.EDefinite).astype(int) - 1,
                up=iset("UPInts"), down=iset("DNInts"), on=iset("ONInts"), off=iset("OFFInts"))


def time_fcx_fetch(session: str = "Dino_072414_mPFC", nbytes: int = 300 * 2 ** 20) -> dict:
    """Stream and decompress the first `nbytes` of one fcx-1 archive; the rate bounds how fast
    the members needed can be reached, since a gzip stream can only be read from its start."""
    import time
    import zlib
    import fsspec
    t0 = time.time()
    f = fsspec.open(f"{CRCNS}/data/{session}.tar.gz", block_size=2 ** 22).open()
    z = zlib.decompressobj(16 + zlib.MAX_WBITS)
    read = out = 0
    while read < nbytes:
        b = f.read(2 ** 22)
        if not b:
            break
        read += len(b)
        out += len(z.decompress(b))
    f.close()
    dt = time.time() - t0
    return dict(session=session, compressed_MB=read / 1e6, decompressed_MB=out / 1e6, seconds=dt, rate_MB_s=read / dt / 1e6)


def crcns_sizes() -> dict:
    import re
    txt = requests.get(f"{CRCNS[:-len('/fcx-1/live')]}/?list-type=2&prefix=fcx-1/live/data/", timeout=60).text
    return {k.split("/")[-1]: int(v) for k, v in re.findall(r"<Key>(.*?\.tar\.gz)</Key>.*?<Size>(\d+)</Size>", txt)}
