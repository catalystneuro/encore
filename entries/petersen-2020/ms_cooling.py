"""Loading and measures for Petersen & Buzsaki (2020) on DANDI:000059.

Data are streamed from the DANDI archive at a pinned version (VERSION); nothing
is written to disk. Each session is reduced as it loads to what the analyses
need: the trial table, head tracking, MS temperature, theta of one CA1 LFP
channel during the trials, and the spikes of the curated units ('good') during
the trials.

Where each parameter comes from:
- Theta band 4 to 10 Hz, third order Butterworth, zero phase (filtfilt), Hilbert
  phase: STAR Methods, "Theta phase and phase precession".
- Theta channel: the channel the lab tagged for theta (electrodes column
  `theta_reference`, session.mat channelTags.Theta). The paper says only "An LFP
  channel located in CA1" (Methods); the lab's own tag, which the files carry,
  is taken as the paper's channel (a detail taken from the dataset's metadata). Where the tagged channel is not
  among the LFP columns, the non-bad channel with the largest 4 to 10 Hz power
  is used (standard choice).
- Oscillation frequency of a neuron: 1 ms raster convolved with an 80-point
  Gaussian window, autocorrelogram, peak between 50 and 150 ms, reciprocal of
  the lag (STAR Methods, "Oscillation Frequency of Neurons"). The window is
  MATLAB's gausswin(80) (alpha 2.5), the standard choice named in the claims
  file. The autocorrelogram of the convolved raster equals the histogram of
  spike-time differences convolved with the window's autocorrelation, which is
  how it is computed here. "Peak" is read as a local maximum inside 50 to 150
  ms (claims file, fig4b-fp-flfp-decrease).
- Pair cross-correlograms: 1 ms bins convolved with a 60-bin Gaussian window;
  phase cross-correlograms 0.01 pi bins with a 60-bin window (STAR Methods,
  "Spatial temporal compression"); gausswin(60) is the standard choice.
- Place fields, Figure 5 rule: at least 4 bins above 10% of the peak rate in
  the maze, peak rate above 8 Hz, spatial coherence above 0.6 (STAR Methods,
  "Place cell analysis"); bins of 3 to 5 cm (same passage). Rate maps are
  smoothed with a Gaussian of 1 bin SD (standard choice; the paper gives none).
- Running speed threshold of 10 cm/s: a reading named in the claims file, not
  stated by the paper.
- Fields are found on the map over all trials of an arm, states pooled
  (assumption; the paper does not say on which map).
"""

import io
import re
import json
import urllib.request

import numpy as np
import pandas as pd
import h5py
import remfile
from scipy import signal, stats

DANDISET = "000059"
VERSION = "0.261115.0311"
API = "https://api.dandiarchive.org/api"
LFP_FS = 1250.0
THETA_BAND = (4.0, 10.0)
RUN_SPEED = 10.0  # cm/s, the claims file's reading (b) of "running"


# ---------------------------------------------------------------- archive

def _get_json(url):
    with urllib.request.urlopen(url) as r:
        return json.load(r)


def list_sessions():
    """Assets of the pinned version, one row per NWB file."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    rows = []
    while url:
        d = _get_json(url)
        for a in d["results"]:
            p = a["path"]
            m = re.search(r"sub-(MS\d+)_ses-Peter-(MS\d+-\d+-\d+)", p)
            rows.append(dict(path=p, asset_id=a["asset_id"], size_gb=a["size"] / 1e9,
                             rat=m.group(1), session=m.group(2)))
        url = d["next"]
    return pd.DataFrame(rows).sort_values("session").reset_index(drop=True)


def open_asset(asset_id):
    meta = _get_json(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/{asset_id}/")
    s3 = [u for u in meta["contentUrl"] if "s3" in u][0]
    return h5py.File(remfile.File(s3), "r")


def _dec(a):
    return np.array([x.decode() if isinstance(x, bytes) else x for x in a], dtype=object)


# ---------------------------------------------------------------- filters

def gausswin(n, alpha=2.5):
    """MATLAB gausswin(n, alpha)."""
    k = np.arange(n) - (n - 1) / 2
    return np.exp(-0.5 * (alpha * k / ((n - 1) / 2)) ** 2)


def theta_filter(x, fs=LFP_FS):
    b, a = signal.butter(3, [THETA_BAND[0] / (fs / 2), THETA_BAND[1] / (fs / 2)], btype="band")
    return signal.filtfilt(b, a, x)


# ---------------------------------------------------------------- session loading

def _theta_column(f):
    e = f["general/extracellular_ephys/electrodes"]
    tag = np.where(e["theta_reference"][:])[0]
    bad = e["bad_channel"][:]
    cols = f["processing/ecephys/LFP/lfp/electrodes"][:]
    info = dict(theta_tag=[int(t) for t in tag], theta_tag_bad=[bool(bad[t]) for t in tag])
    for t in tag:
        hit = np.where(cols == t)[0]
        if len(hit):
            info["theta_source"] = "lab tag"
            return int(hit[0]), int(t), info
    info["theta_source"] = "largest theta power (tag not in LFP)"
    return None, None, info


def _pick_theta_by_power(f, t0):
    d = f["processing/ecephys/LFP/lfp/data"]
    cols = f["processing/ecephys/LFP/lfp/electrodes"][:]
    bad = f["general/extracellular_ephys/electrodes/bad_channel"][:]
    i0 = int(t0 * LFP_FS)
    x = d[i0:i0 + int(60 * LFP_FS), :].astype(float)
    fr, p = signal.welch(x, fs=LFP_FS, nperseg=2048, axis=0)
    band = (fr >= 4) & (fr <= 10)
    pw = p[band].mean(0)
    pw[bad[cols]] = -1
    j = int(np.argmax(pw))
    return j, int(cols[j])


def load_session(row, with_lfp=True, with_units=True):
    """Reduce one session to the arrays the analyses use."""
    f = open_asset(row["asset_id"])
    S = dict(rat=row["rat"], session=row["session"], asset_id=row["asset_id"])

    # trials
    t = f["intervals/trials"]
    tr = pd.DataFrame(dict(start=t["start_time"][:], stop=t["stop_time"][:],
                           state=_dec(t["cooling_state"][:]), error=t["error"][:].astype(bool),
                           condition=_dec(t["condition"][:])))
    # cooling intervals and onset
    c = f["intervals/cooling"]
    desc = c.attrs["description"]
    m = re.search(r"cooling onset at ([\d., ]+) s and offset at ([\d., ]+) s", desc)
    S["onsets"] = [float(v) for v in m.group(1).split(",")]
    S["offsets"] = [float(v) for v in m.group(2).split(",")]
    # the first cooling epoch is the session's cooling onset; 13 sessions have a second one
    S["onset"], S["offset"] = S["onsets"][0], S["offsets"][0]
    S["cooling_table"] = pd.DataFrame(dict(label=_dec(c["label"][:]), start=c["start_time"][:],
                                           stop=c["stop_time"][:]))

    # behaviour
    b = f["processing/behavior"]
    ts = b["SubjectPosition/SpatialSeries/timestamps"][:]
    xyz = b["SubjectPosition/SpatialSeries/data"][:]  # stored in cm (conversion 0.01 to m)
    lin = b["LinearizedPosition/LinearizedSpatialSeries/data"][:]  # cm
    lin_ts = b["LinearizedPosition/LinearizedSpatialSeries/timestamps"][:]
    spd = b["SubjectSpeed/data"][:]
    spd_ts = b["SubjectSpeed/timestamps"][:]
    S["pos_dt"] = float(np.median(np.diff(ts)))
    S["beh_desc"] = b["SubjectSpeed"].attrs["description"]
    S["beh"] = dict(t=ts, x=xyz[:, 0], y=xyz[:, 1], lin=np.interp(ts, lin_ts, lin) if not np.array_equal(ts, lin_ts) else lin,
                    speed=spd if np.array_equal(ts, spd_ts) else np.interp(ts, spd_ts, spd))
    S["lin_raw"] = (lin_ts, lin)

    # temperature
    if "MeasuredTemperature" in b:
        g = b["MeasuredTemperature"]
        T = g["data"][:]
        if "timestamps" in g:
            tt = g["timestamps"][:]
        else:
            tt = g["starting_time"][()] + np.arange(len(T)) / g["starting_time"].attrs["rate"]
        S["temp_kind"] = "measured"
        # the measured traces hold artefacts far outside any brain temperature
        # (up to 1354 C, down to -1751 C, and runs at the 0 and 50 C rails);
        # values outside 5 to 45 C are set to NaN (standard choice)
        S["temp_raw_range"] = (float(np.nanmin(T)), float(np.nanmax(T)))
        T = np.where((T >= 5) & (T <= 45), T, np.nan)
    else:
        g = b["ModelledTemperature"]
        T = g["data"][:]
        tt = g["timestamps"][:]
        S["temp_kind"] = "modelled"
    S["temp"] = (tt, T)

    # epoch metadata
    if "intervals/epochs" in f:
        ep = f["intervals/epochs"]
        S["epochs"] = pd.DataFrame({k: (_dec(ep[k][:]) if ep[k].dtype == object else ep[k][:])
                                    for k in ep if k in ("start_time", "stop_time", "environment", "behavioral_paradigm", "manipulation")})

    # per-trial behaviour
    run_arm = []
    for s0, s1 in zip(tr.start, tr.stop):
        mm = (ts >= s0) & (ts <= s1)
        l = S["beh"]["lin"][mm]
        run_arm.append("Right" if np.nanmax(l) > 220 else "Left" if np.isfinite(l).any() else "")
    tr["arm"] = run_arm
    tr["speed_all"] = [np.nanmean(S["beh"]["speed"][(ts >= a) & (ts <= z)]) for a, z in zip(tr.start, tr.stop)]
    def _run_mean(a, z):
        v = S["beh"]["speed"][(ts >= a) & (ts <= z)]
        v = v[v > RUN_SPEED]
        return np.nanmean(v) if len(v) else np.nan
    tr["speed_run"] = [_run_mean(a, z) for a, z in zip(tr.start, tr.stop)]
    tr["temp"] = [np.nanmean(T[(tt >= a) & (tt <= z)]) if ((tt >= a) & (tt <= z)).any() else np.nan
                  for a, z in zip(tr.start, tr.stop)]
    # aligned trial number: first trial starting at or after onset is 1, the last before is -1
    after = tr.start.values >= S["onset"]
    k = np.where(after, np.cumsum(after), 0)
    nb = (~after).sum()
    k[~after] = np.arange(-nb, 0)
    tr["aligned"] = k
    tr["dt_onset"] = tr.start - S["onset"]
    S["trials"] = tr

    t0, t1 = tr.start.min() - 5.0, tr.stop.max() + 5.0
    S["span"] = (t0, t1)

    # LFP theta
    S["has_lfp"] = with_lfp and ("processing/ecephys/LFP/lfp" in f)
    if S["has_lfp"]:
        col, ch, info = _theta_column(f)
        if col is None:
            col, ch = _pick_theta_by_power(f, tr.start.iloc[0])
        S["theta_info"] = dict(info, column=col, channel=ch)
        d = f["processing/ecephys/LFP/lfp/data"]
        conv = d.attrs["conversion"] * 1e6  # to microvolts
        lfp_t0 = f["processing/ecephys/LFP/lfp/starting_time"][()]
        i0 = int((t0 - lfp_t0) * LFP_FS)
        i1 = int((t1 - lfp_t0) * LFP_FS)
        i0 = max(i0, 0)
        x = d[i0:i1, col].astype(float) * conv
        lt = lfp_t0 + (i0 + np.arange(len(x))) / LFP_FS
        xf = theta_filter(x)
        h = signal.hilbert(xf)
        ph = np.unwrap(np.angle(h))
        amp = np.abs(h)
        inst = np.gradient(ph) * LFP_FS / (2 * np.pi)
        sp_l = np.interp(lt, ts, np.nan_to_num(S["beh"]["speed"]))
        S["lfp_t"] = (lt[0], LFP_FS, len(lt))
        # per-trial theta: reading (a) Hilbert, (b) spectral peak; all samples and running samples
        rows = []
        nfft = 2 ** 14
        for s0, s1 in zip(tr.start, tr.stop):
            j0, j1 = int((s0 - lt[0]) * LFP_FS), int((s1 - lt[0]) * LFP_FS)
            seg = slice(max(j0, 0), max(j1, 0))
            r = {}
            ff, aa, ss = inst[seg], amp[seg], sp_l[seg]
            run = ss > RUN_SPEED
            r["f_hil"] = np.mean(ff) if len(ff) else np.nan
            r["p_hil"] = np.mean(aa ** 2) if len(aa) else np.nan
            r["f_hil_run"] = np.mean(ff[run]) if run.sum() > 10 else np.nan
            r["p_hil_run"] = np.mean(aa[run] ** 2) if run.sum() > 10 else np.nan
            xs = x[seg]
            if len(xs) > 256:
                fr, pp = signal.periodogram(xs - xs.mean(), fs=LFP_FS, window="hann", nfft=nfft)
                band = (fr >= THETA_BAND[0]) & (fr <= THETA_BAND[1])
                jj = np.argmax(pp[band])
                r["f_spec"] = fr[band][jj]
                r["p_spec"] = pp[band][jj]
            else:
                r["f_spec"] = r["p_spec"] = np.nan
            rows.append(r)
        for kk in rows[0]:
            tr[kk] = [r[kk] for r in rows]
        # theta cycles: one cycle between successive wraps of the wrapped phase
        wraps = np.where(np.diff(np.floor((ph + np.pi) / (2 * np.pi))) > 0)[0] + 1
        cyc_t = lt[wraps]
        tid = np.full(len(cyc_t), -1)
        for i, (s0, s1) in enumerate(zip(tr.start, tr.stop)):
            tid[(cyc_t >= s0) & (cyc_t <= s1)] = i
        cyc = pd.DataFrame(dict(t0=cyc_t[:-1], t1=cyc_t[1:], trial=tid[:-1]))
        cyc = cyc[(tid[:-1] >= 0) & (tid[:-1] == tid[1:])].reset_index(drop=True)
        cyc["dur"] = cyc.t1 - cyc.t0
        mid = (cyc.t0 + cyc.t1) / 2
        cyc["lin"] = np.interp(mid, ts, np.nan_to_num(S["beh"]["lin"], nan=-1))
        cyc["speed"] = np.interp(mid, ts, np.nan_to_num(S["beh"]["speed"]))
        cyc["arm"] = tr.arm.values[cyc.trial.values]
        S["cycles"] = cyc
        S["_ph"], S["_inst"], S["_lt0"] = ph, inst, lt[0]
    S["trials"] = tr

    # units
    S["has_units"] = with_units and ("units" in f)
    if S["has_units"]:
        u = f["units"]
        q = _dec(u["quality"][:])
        ct = _dec(u["cell_type"][:])
        idx = u["spike_times_index"][:]
        good = np.where(q == "good")[0]
        st_all = u["spike_times"]
        U = []
        for i in good:
            a = idx[i - 1] if i > 0 else 0
            z = idx[i]
            s = st_all[a:z]
            s = s[(s >= t0) & (s <= t1)]
            U.append(dict(unit=int(u["id"][i]), cell_type=ct[i], spikes=s,
                          maxch=int(u["max_waveform_channel"][i])))
        S["units"] = U
        S["n_units_all"] = len(q)
        S["quality_counts"] = pd.Series(q).value_counts().to_dict()
    f.close()
    return S


def spike_table(S):
    """One row per spike of the curated units during trials, with position,
    speed, trial, theta phase (unwrapped, rad) and instantaneous theta frequency."""
    tr = S["trials"]
    out = []
    ts = S["beh"]["t"]
    for k, U in enumerate(S["units"]):
        s = U["spikes"]
        ti = np.searchsorted(tr.start.values, s, side="right") - 1
        ok = (ti >= 0) & (s <= tr.stop.values[np.clip(ti, 0, None)])
        s, ti = s[ok], ti[ok]
        df = pd.DataFrame(dict(t=s, u=k, trial=ti))
        out.append(df)
    if out:
        sp = pd.concat(out, ignore_index=True)
    else:
        sp = pd.DataFrame(dict(t=np.zeros(0), u=np.zeros(0, int), trial=np.zeros(0, int)))
    lin = S["beh"]["lin"]
    good = np.isfinite(lin)
    sp["lin"] = np.interp(sp.t, ts[good], lin[good])
    sp["speed"] = np.interp(sp.t, ts, np.nan_to_num(S["beh"]["speed"]))
    sp["arm"] = tr.arm.values[sp.trial.values]
    sp["state"] = tr.state.values[sp.trial.values]
    if S.get("has_lfp"):
        lt0 = S["_lt0"]
        j = np.clip(((sp.t - lt0) * LFP_FS).astype(int).values, 0, len(S["_ph"]) - 1)
        sp["phase_u"] = S["_ph"][j]
        sp["theta_f"] = S["_inst"][j]
    return sp


def drop_lfp_arrays(S):
    for k in ("_ph", "_inst"):
        S.pop(k, None)


# ---------------------------------------------------------------- states

def state_labels(tr, onset, reading):
    """Trial states under the readings of the claims file's opening comment:
    'lab' the dataset's labels (transition trials excluded), 'm12' / 'm10'
    cooling is the trials starting within 12 / 10 min after onset, pre before
    onset, post after."""
    if reading == "lab":
        s = tr.state.copy()
        s[~s.isin(["Pre", "Cooling", "Post"])] = None
        return s
    w = 12 * 60 if reading == "m12" else 10 * 60
    d = tr.start.values - onset
    s = np.where(d < 0, "Pre", np.where(d <= w, "Cooling", "Post"))
    return pd.Series(s, index=tr.index, dtype=object)


# ---------------------------------------------------------------- correlograms

def acg_frequency(spikes_ms_lists, max_lag=200):
    """Oscillation frequency from the autocorrelogram (Methods). spikes_ms_lists is
    a list of arrays of spike times in ms (one per pass, so that differences
    across passes are not counted). Returns (frequency Hz or nan, acg)."""
    h = np.zeros(2 * max_lag + 1)
    for s in spikes_ms_lists:
        s = np.round(np.asarray(s, float))
        if len(s) == 0:
            continue
        d = pair_diffs(s, s, max_lag).astype(int)
        h += np.bincount(d + max_lag, minlength=2 * max_lag + 1)
    g = gausswin(80)
    k = np.convolve(g, g)  # autocorrelation of the window (symmetric)
    a = np.convolve(h, k, mode="same")
    lags = np.arange(-max_lag, max_lag + 1)
    w = (lags >= 50) & (lags <= 150)
    seg = a[w]
    loc = np.where((seg[1:-1] > seg[:-2]) & (seg[1:-1] >= seg[2:]))[0] + 1
    if len(loc) == 0 or h.sum() == 0:
        return np.nan, a
    j = loc[np.argmax(seg[loc])]
    return 1000.0 / lags[w][j], a


def pair_diffs(a, b, max_lag, va=None, vb=None):
    """All differences b - a within +-max_lag (a, b sorted or not). With va, vb
    given, also returns the differences vb - va of the same spike pairs."""
    oa = np.argsort(a)
    ob = np.argsort(b)
    a = np.asarray(a)[oa]
    b = np.asarray(b)[ob]
    lo = np.searchsorted(b, a - max_lag, side="left")
    hi = np.searchsorted(b, a + max_lag, side="right")
    cnt = hi - lo
    tot = int(cnt.sum())
    if tot == 0:
        return (np.zeros(0), np.zeros(0)) if va is not None else np.zeros(0)
    ia = np.repeat(np.arange(len(a)), cnt)
    start = np.repeat(lo - np.concatenate([[0], np.cumsum(cnt)[:-1]]), cnt)
    ib = np.arange(tot) + start
    d = b[ib] - a[ia]
    if va is None:
        return d
    va = np.asarray(va)[oa]
    vb = np.asarray(vb)[ob]
    return d, vb[ib] - va[ia]


def ccg_counts(a, b, max_lag, binw):
    """Histogram of b - a differences within +-max_lag (same units), bins of binw."""
    nb = int(round(max_lag / binw))
    d = pair_diffs(a, b, max_lag)
    k = np.clip(np.round(d / binw).astype(int) + nb, 0, 2 * nb)
    return np.bincount(k, minlength=2 * nb + 1).astype(float)


def dominant_period(y, lags, pmin, pmax, trend_sd):
    """Period of the oscillation of a cross-correlogram: the slow trend (a Gaussian
    of trend_sd bins) is removed, the residual is Hann-windowed, and the period
    is that of the largest Fourier component between pmin and pmax (standard
    choice)."""
    from scipy.ndimage import gaussian_filter1d
    if y is None:
        return np.nan
    z = y - gaussian_filter1d(y, trend_sd)
    z = z * np.hanning(len(z))
    step = lags[1] - lags[0]
    nfft = 2 ** 16
    F = np.abs(np.fft.rfft(z, nfft))
    fr = np.fft.rfftfreq(nfft, step)
    with np.errstate(divide="ignore"):
        per = 1 / fr
    m = (per >= pmin) & (per <= pmax)
    if not m.any() or F[m].max() == 0:
        return np.nan
    return float(per[m][np.argmax(F[m])])


def smooth60(h):
    g = gausswin(60)
    g = g / g.sum()
    return np.convolve(h, g, mode="same")


def peaks(y):
    return np.where((y[1:-1] > y[:-2]) & (y[1:-1] >= y[2:]))[0] + 1


# ---------------------------------------------------------------- place fields

def rate_maps(sp_u, occ, binw, edges):
    cnt, _ = np.histogram(sp_u, bins=edges)
    with np.errstate(invalid="ignore", divide="ignore"):
        r = cnt / occ
    return cnt, r


def smooth_map(r, occ):
    r = np.where(occ > 0, r, np.nan)
    v = np.nan_to_num(r)
    w = (occ > 0).astype(float)
    k = signal.windows.gaussian(7, 1.0)
    num = np.convolve(v * w, k, mode="same")
    den = np.convolve(w, k, mode="same")
    with np.errstate(invalid="ignore", divide="ignore"):
        out = num / den
    out[occ == 0] = np.nan
    return out


def spatial_coherence(r):
    """Muller & Kubie (1989) coherence on a linear map: correlation of each bin's
    rate with the mean of its two neighbours (Fisher z in the original; R here)."""
    v = r.copy()
    nb = np.full_like(v, np.nan)
    nb[1:-1] = np.nanmean(np.vstack([v[:-2], v[2:]]), axis=0)
    ok = np.isfinite(v) & np.isfinite(nb)
    if ok.sum() < 5:
        return np.nan
    return stats.pearsonr(v[ok], nb[ok])[0]


def find_fields(r, raw, min_bins=4, frac=0.1, min_peak=8.0, min_coh=0.6):
    """Figure 5 rule (Methods). r is the smoothed rate map of one run direction.
    Fields are runs of contiguous bins above frac of the map's peak, with at
    least min_bins bins and a peak above min_peak; the map's coherence must
    exceed min_coh. Returns a list of (first bin, last bin, peak bin, peak rate)."""
    if not np.isfinite(r).any():
        return []
    pk = np.nanmax(r)
    if pk <= min_peak or not (spatial_coherence(raw) > min_coh):
        return []
    above = np.nan_to_num(r) > frac * pk
    out = []
    i = 0
    n = len(r)
    while i < n:
        if above[i]:
            j = i
            while j + 1 < n and above[j + 1]:
                j += 1
            seg = r[i:j + 1]
            if j - i + 1 >= min_bins and np.nanmax(seg) > min_peak:
                p = i + int(np.nanargmax(seg))
                out.append((i, j, p, float(np.nanmax(seg))))
            i = j + 1
        else:
            i += 1
    return out


def skaggs_info(rate, occ):
    ok = np.isfinite(rate) & (occ > 0)
    p = occ[ok] / occ[ok].sum()
    r = rate[ok]
    mr = np.sum(p * r)
    if mr <= 0:
        return np.nan
    with np.errstate(divide="ignore", invalid="ignore"):
        t = np.where(r > 0, p * r / mr * np.log2(r / mr), 0)
    return float(np.sum(t))


def circ_lin_slope(x, phi, smin=-2 * np.pi, smax=2 * np.pi, n=401):
    """Circular-linear regression (Kempter et al. 2012): slope a (rad per unit of
    x) maximising the mean resultant length of phi - 2 pi a x. x is scaled to
    the field's length (0 to 1), so a is in cycles per field."""
    a = np.linspace(smin / (2 * np.pi), smax / (2 * np.pi), n)
    R = np.abs(np.exp(1j * (phi[None, :] - 2 * np.pi * a[:, None] * x[None, :])).mean(1))
    j = int(np.argmax(R))
    # refine around the best grid point
    a2 = np.linspace(a[max(j - 1, 0)], a[min(j + 1, n - 1)], 101)
    R2 = np.abs(np.exp(1j * (phi[None, :] - 2 * np.pi * a2[:, None] * x[None, :])).mean(1))
    k = int(np.argmax(R2))
    return 2 * np.pi * a2[k], R2[k]


# ---------------------------------------------------------------- statistics

def signrank(x, y=None):
    x = np.asarray(x, float)
    d = x if y is None else x - np.asarray(y, float)
    d = d[np.isfinite(d)]
    if len(d) < 1 or np.all(d == 0):
        return np.nan, len(d)
    return float(stats.wilcoxon(d).pvalue), len(d)


def ranksum(x, y):
    x = np.asarray(x, float); y = np.asarray(y, float)
    x = x[np.isfinite(x)]; y = y[np.isfinite(y)]
    return float(stats.ranksums(x, y).pvalue)


def corr(x, y, kind="pearson"):
    x = np.asarray(x, float); y = np.asarray(y, float)
    ok = np.isfinite(x) & np.isfinite(y)
    if ok.sum() < 3:
        return np.nan, np.nan, int(ok.sum())
    r = stats.pearsonr(x[ok], y[ok]) if kind == "pearson" else stats.spearmanr(x[ok], y[ok])
    return float(r[0]), float(r[1]), int(ok.sum())


# ---------------------------------------------------------------- whole dataset

def _load_one(row):
    S = load_session(row)
    if S["has_units"]:
        S["sp"] = spike_table(S)
    drop_lfp_arrays(S)
    return S


def load_all(sessions, workers=4):
    """Load and reduce every session, `workers` at a time (each holds one
    session's theta channel, about 1 GB at most)."""
    from concurrent.futures import ProcessPoolExecutor
    rows = [r for _, r in sessions.iterrows()]
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(_load_one, rows))


def aligned_series(SESS, col, k_range=(-40, 80), sel=None, onset_state=None):
    """Mean over sessions of a trial column at each trial aligned on cooling
    onset (first trial after onset is 1, the last before is -1). Returns a
    DataFrame indexed by aligned trial with the mean, SE and number of sessions."""
    rows = []
    for S in SESS:
        if sel is not None and not sel(S):
            continue
        tr = S["trials"]
        # trials after a second cooling onset are left out of the aligned series
        keep = np.ones(len(tr), bool)
        if len(S["onsets"]) > 1:
            keep &= tr.start.values < S["onsets"][1]
        v = tr.loc[keep, ["aligned", col]].copy()
        v["session"] = S["session"]
        rows.append(v)
    d = pd.concat(rows)
    d = d[(d.aligned >= k_range[0]) & (d.aligned <= k_range[1])]
    g = d.groupby("aligned")[col]
    out = pd.DataFrame(dict(mean=g.mean(), se=g.sem(), n=g.count()))
    return out, d


# ---------------------------------------------------------------- place fields of a session

STATES = ("Pre", "Cooling", "Post")


def occupancy(S, arm, edges, trial_mask, speed_min=None):
    """Time (s) per position bin in the trials of `arm` selected by trial_mask."""
    b = S["beh"]
    tr = S["trials"]
    t = b["t"]
    dt = np.gradient(t)
    ti = np.searchsorted(tr.start.values, t, side="right") - 1
    ok = (ti >= 0) & (t <= tr.stop.values[np.clip(ti, 0, None)])
    ok &= np.isfinite(b["lin"])
    sel = np.zeros(len(t), bool)
    sel[ok] = trial_mask[ti[ok]] & (tr.arm.values[ti[ok]] == arm)
    if speed_min is not None:
        sel &= np.nan_to_num(b["speed"]) > speed_min
    occ, _ = np.histogram(b["lin"][sel], bins=edges, weights=dt[sel])
    return occ


def session_fields(S, binw=5.0, pyr_only=True, min_peak=8.0):
    """Place fields of the pyramidal cells of a session by the Figure 5 rule,
    from rate maps over all trials of each arm (states pooled), one map per arm
    (left and right runs apart, Figure 3A, B). Returns a DataFrame of fields
    and the maps."""
    edges = np.arange(0, 350 + binw, binw)
    tr = S["trials"]
    sp = S["sp"]
    allm = np.ones(len(tr), bool)
    rows = []
    maps = {}
    for arm in ("Left", "Right"):
        occ = occupancy(S, arm, edges, allm)
        maps[("occ", arm)] = occ
        for k, U in enumerate(S["units"]):
            if pyr_only and U["cell_type"] != "Pyramidal Cell":
                continue
            s = sp[(sp.u == k) & (sp.arm == arm)]
            cnt, _ = np.histogram(s.lin, bins=edges)
            with np.errstate(invalid="ignore", divide="ignore"):
                raw = np.where(occ > 0, cnt / occ, np.nan)
            r = smooth_map(raw, occ)
            maps[(k, arm)] = r
            for (i, j, p, pk) in find_fields(r, raw, min_peak=min_peak):
                rows.append(dict(session=S["session"], rat=S["rat"], u=k, arm=arm,
                                 lo=edges[i], hi=edges[j + 1], peak_pos=(edges[p] + edges[p + 1]) / 2,
                                 peak_rate=pk, i0=i, i1=j))
    return pd.DataFrame(rows), maps, edges


def _beh_trial_index(S):
    if "_bti" not in S:
        b = S["beh"]
        tr = S["trials"]
        t = b["t"]
        ti = np.searchsorted(tr.start.values, t, side="right") - 1
        ok = (ti >= 0) & (t <= tr.stop.values[np.clip(ti, 0, None)]) & np.isfinite(b["lin"])
        S["_bti"] = np.where(ok, ti, -1)
    return S["_bti"]


def field_state_measures(S, F, edges, state_col="st_lab", min_spikes=1):
    """Per field and state: within-field rate, peak rate, fp, fLFP (at spikes and
    over the time in the field, from theta cycles), speed, field size,
    information and phase precession. States from the trial column state_col."""
    tr = S["trials"]
    sp = S["sp"]
    b = S["beh"]
    binw = edges[1] - edges[0]
    st_tr = tr[state_col].values
    st_sp = st_tr[sp.trial.values]
    bti = _beh_trial_index(S)
    dt = np.gradient(b["t"])
    cyc = S.get("cycles")
    cyc_state = st_tr[cyc.trial.values] if cyc is not None else None
    occ_cache = {}
    rows = []
    for _, f in F.iterrows():
        for s in STATES:
            key = (f.arm, s)
            if key not in occ_cache:
                m = (st_tr == s)
                occ_cache[key] = occupancy(S, f.arm, edges, m)
            occ = occ_cache[key]
            sel = (sp.u.values == f.u) & (sp.arm.values == f.arm) & (st_sp == s)
            su = sp[sel]
            cnt, _ = np.histogram(su.lin, bins=edges)
            with np.errstate(invalid="ignore", divide="ignore"):
                raw = np.where(occ > 0, cnt / occ, np.nan)
            rmap = smooth_map(raw, occ)
            inf = (su.lin.values >= f.lo) & (su.lin.values < f.hi)
            si = su[inf]
            t_in = occ[f.i0:f.i1 + 1].sum()
            r = dict(session=f.session, rat=f.rat, u=f.u, arm=f.arm, lo=f.lo, hi=f.hi, state=s,
                     n_spk=len(si), t_in=t_in)
            r["rate_in"] = len(si) / t_in if t_in > 0 else np.nan
            seg = rmap[f.i0:f.i1 + 1]
            r["peak"] = np.nanmax(seg) if np.isfinite(seg).any() else np.nan
            # field size in this state: contiguous bins around the state's peak above 10% of it
            if np.isfinite(r["peak"]) and r["peak"] > 0:
                p = f.i0 + int(np.nanargmax(seg))
                thr = 0.1 * r["peak"]
                v = np.nan_to_num(rmap)
                a_, z_ = p, p
                while a_ - 1 >= 0 and v[a_ - 1] > thr:
                    a_ -= 1
                while z_ + 1 < len(v) and v[z_ + 1] > thr:
                    z_ += 1
                r["size"] = (z_ - a_ + 1) * binw
                r["peak_pos_state"] = (edges[p] + edges[p + 1]) / 2
            else:
                r["size"] = np.nan
                r["peak_pos_state"] = np.nan
            r["info"] = skaggs_info(rmap, occ) if occ.sum() > 0 else np.nan
            # fp from the in-field spikes, one list per pass (trial)
            if len(si) >= min_spikes:
                lists = [g.t.values * 1000 for _, g in si.groupby("trial")]
                r["fp"] = acg_frequency(lists)[0]
            else:
                r["fp"] = np.nan
            if "theta_f" in si:
                r["flfp_spk"] = si.theta_f.mean() if len(si) else np.nan
            if cyc is not None and len(cyc):
                cm = (cyc.arm.values == f.arm) & (cyc_state == s) & (cyc.lin.values >= f.lo) & (cyc.lin.values < f.hi)
                r["flfp_time"] = np.mean(1 / cyc.dur.values[cm]) if cm.any() else np.nan
            # speed in the field: over the time in it and at the spikes
            bm = (bti >= 0)
            bm[bm] = (st_tr[bti[bm]] == s) & (tr.arm.values[bti[bm]] == f.arm)
            bm &= (b["lin"] >= f.lo) & (b["lin"] < f.hi)
            r["v_time"] = np.average(np.nan_to_num(b["speed"][bm]), weights=dt[bm]) if bm.any() else np.nan
            r["v_spk"] = si.speed.mean() if len(si) else np.nan
            # phase precession: circular-linear regression of phase on position in the field
            if "phase_u" in si and len(si) >= 10:
                x = (si.lin.values - f.lo) / (f.hi - f.lo)
                r["prec_slope"], r["prec_R"] = circ_lin_slope(x, np.mod(si.phase_u.values, 2 * np.pi))
            else:
                r["prec_slope"] = r["prec_R"] = np.nan
            rows.append(r)
    return pd.DataFrame(rows)


# ---------------------------------------------------------------- waveforms

def unit_waveforms(S, n_chunks=(2, 3, 2), pre_ms=1.0, post_ms=2.0):
    """Mean high-pass filtered (300 Hz, third order Butterworth, zero phase;
    standard choice) waveform of each curated unit on its largest channel
    (CellExplorer maxWaveformCh), in pre and post trials together and in
    cooling trials, from a few 52 s blocks of the 20 kHz wide-band signal
    (n_chunks blocks centred in pre, cooling and post; a subset, as the whole
    signal is 3 TB). Returns a DataFrame with trough-to-peak latency (ms) and
    peak-to-peak amplitude (uV) per unit and condition."""
    f = open_asset(S["asset_id"])
    d = f["acquisition/ElectricalSeries/data"]
    fs = d.parent["starting_time"].attrs["rate"]
    t0 = d.parent["starting_time"][()]
    conv = d.attrs["conversion"] * 1e6
    cols = f["acquisition/ElectricalSeries/electrodes"][:]
    chunk = d.chunks[0]
    tr = S["trials"]
    b, a = signal.butter(3, 300 / (fs / 2), btype="high")
    nb, na = int(pre_ms * fs / 1000), int(post_ms * fs / 1000)
    units = [(k, U) for k, U in enumerate(S["units"]) if U["maxch"] >= 0]
    acc = {}
    for cond, states, n in [("control", ["Pre"], n_chunks[0]), ("cooling", ["Cooling"], n_chunks[1]), ("control", ["Post"], n_chunks[2])]:
        tt = tr[tr.state.isin(states)]
        if not len(tt):
            continue
        times = np.quantile(np.concatenate([tt.start.values, tt.stop.values]), np.linspace(0.2, 0.8, n))
        for tc in times:
            i0 = (int((tc - t0) * fs) // chunk) * chunk
            seg_t0 = t0 + i0 / fs
            chans = sorted(set(U["maxch"] for _, U in units))
            groups = sorted(set(int(np.where(cols == c)[0][0]) // d.chunks[1] for c in chans if (cols == c).any()))
            for gi in groups:
                X = d[i0:i0 + chunk, gi * d.chunks[1]:(gi + 1) * d.chunks[1]].astype(float) * conv
                X = signal.filtfilt(b, a, X, axis=0)
                for k, U in units:
                    hit = np.where(cols == U["maxch"])[0]
                    if not len(hit) or hit[0] // d.chunks[1] != gi:
                        continue
                    c = hit[0] - gi * d.chunks[1]
                    s = U["spikes"]
                    s = s[(s >= seg_t0 + pre_ms / 1000) & (s < seg_t0 + (chunk - na - 1) / fs)]
                    # keep spikes inside trials of these states
                    ti = np.searchsorted(tr.start.values, s, side="right") - 1
                    ok = (ti >= 0) & (s <= tr.stop.values[np.clip(ti, 0, None)])
                    ok[ok] = tr.state.values[ti[ok]] == states[0]
                    s = s[ok]
                    if not len(s):
                        continue
                    j = np.round((s - seg_t0) * fs).astype(int)
                    W = X[j[:, None] + np.arange(-nb, na)[None, :], c]
                    key = (k, cond)
                    tot, cnt = acc.get(key, (0, 0))
                    acc[key] = (tot + W.sum(0), cnt + len(j))
    f.close()
    rows = []
    for (k, cond), (tot, cnt) in acc.items():
        w = tot / cnt
        it = int(np.argmin(w))
        ip = it + int(np.argmax(w[it:]))
        rows.append(dict(session=S["session"], u=k, cell_type=S["units"][k]["cell_type"], cond=cond, n=cnt,
                         trough_to_peak_ms=(ip - it) / fs * 1000, p2p_uV=float(w.max() - w.min())))
    return pd.DataFrame(rows)
