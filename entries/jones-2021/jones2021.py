"""Loading and measures for the hippocampal LFP and MUA of dandiset 000165.

Aery Jones, Rao, Zilberter, ..., Huang & Frank (2021), Cell Reports 37, 110159,
doi:10.1016/j.celrep.2021.110159.

Each NWB file is one session of one mouse: 0.1-300 Hz LFP at 1 kHz on 32 sites
(`processing/ecephys/LFP`, int16, microvolts), MUA spike times per site (`units`, one row per
electrode), head position in cm (`processing/behavior/Position`), and per site an anatomical
label (`electrodes.location`, for example "ca1-pyr 1 mua"). The subject's genotype, sex and
virus, and the session's treatment (`pharmacology`, "Vehicle" or "CNO") are in the file's
metadata. Files are streamed from the archive at the pinned version; nothing is written to disk.

Where the parameters come from (claims/jones-2021.yaml, "Method M", cites the paper and code;
"Methods" below is the paper's STAR Methods, Analysis of neural data):

- Rest is extended immobility: Gaussian-smoothed speed below 1 cm/s for 30 s or more
  (Methods, paragraph 2; code get2dstate, immobilitytime > 30, so the first 30 s of each still
  period are left out). Run is smoothed speed above 1 cm/s (Methods, paragraph 7). The
  smoothing width of the speed (Gaussian, SD 0.5 s, on positions resampled to 30 Hz) is not
  given anywhere; it is a standard choice that moves period edges by a fraction of a second.
- SWRs (Methods, paragraph 2): 125-200 Hz equiripple filter, Hilbert envelope smoothed with a
  4 ms Gaussian, above 3 SD for at least 15 ms, on the CA1 site closest to the centre of the
  pyramidal layer. The file labels that site "ca1-pyr 1" (the Methods' wording; there is one per
  file). Baseline mean and SD are taken over rest. An event runs from where the envelope rises
  above the mean to where it falls back to it (the Frank lab's extractripples convention, which
  the paper cites as Cheng and Frank 2008); this is an assumption, since the Methods only give
  the threshold. Events within 0.4 s of a rest period's edges, and events where 16 or more
  sites also cross 5 SD, are dropped (code getvalidrips.m, cited in the claims file). Size is
  the peak envelope in SD (code ripdescript.m, ripstds). The 5 SD variant keeps events whose
  size is 5 or more (code runcalcriprates.m, minstd 5).
- Filter lengths are not given; 101 taps for the ripple band and 301 for the 0-30 Hz SW band
  and the 5-100 Hz dentate spike band are standard choices; the filters are applied forwards and
  backwards (zero phase).
- MUA sites are the sites whose label ends in "mua" (Methods, paragraph 5: the site closest to
  the centre of the layer, by highest MUA), one each in CA1, CA3 and DG. Normalised SWR MUA is
  (rate in the SWR - mean rest rate) / SD of the rest rate in 100 ms bins (code RTMUA.m,
  normrate, cited in the claims file). Every unit's spike train starts with a spike at 0.0 s,
  which is dropped.
- Run spectra (Methods, paragraph 7): multitaper, 1 s windows, time-bandwidth 3 with 5 tapers
  (code continuous_specgram.m, tapers [3 5]), non-overlapping 1 s bins lying wholly in run.
  Bands theta 5-11 Hz, SG 20-50 Hz, FG 50-110 Hz. Band filters for frequency and comodulation
  are least-squares FIR (Methods); 1001, 301 and 151 taps are standard choices.
- Regions: CA1-pyr sites ("ca1-pyr..." labels), CA3 pyr and sr ("ca3-pyr", "ca3-sr"), DG hilus and
  granule cell layer, among sites with confirmed dentate spikes (labels "dg-val gc" and
  "dg-val hil"; the Methods keep only DG sites with visually confirmed dentate spikes, and "val"
  is read as that confirmation). A region's value is the mean over its sites (code
  run_continuous_specgram.m, avgSGpwr).
- Modulation index: normalised entropy of mean amplitude over 35 theta phase bins (claims file,
  code comod.m), per 1 s bin of run.
"""

from __future__ import annotations

import io
import time
import resource

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy import signal, stats, optimize
from scipy.ndimage import gaussian_filter1d
from scipy.fft import next_fast_len
import scipy.fft as sp_fft

DANDISET_ID = "000165"
DANDISET_VERSION = "0.211118.1526"
API = "https://api.dandiarchive.org/api"
FS = 1000.0

SPEED_SMOOTH_S = 0.5      # standard choice (see module docstring)
POS_HZ = 30.0
IMMOBILE_CM_S = 1.0       # Methods, paragraph 2
IMMOBILE_MIN_S = 30.0     # Methods, paragraph 2
RUN_CM_S = 1.0            # Methods, paragraph 7
EDGE_S = 0.4              # code getvalidrips.m
RIPPLE_BAND = (125.0, 200.0)
RIPPLE_SMOOTH_S = 0.004
RIPPLE_SD = 3.0
RIPPLE_MIN_S = 0.015
ARTIFACT_SD, ARTIFACT_SITES = 5.0, 16
CHAIN_S = 0.2
THETA, SG, FG = (5.0, 11.0), (20.0, 50.0), (50.0, 110.0)
REST_SG = (30.0, 50.0)    # Methods, paragraph 3
N_PHASE_BINS = 35


# ---------------------------------------------------------------- archive

def list_assets() -> pd.DataFrame:
    rows, url = [], f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=1000"
    while url:
        r = requests.get(url, timeout=60).json()
        rows += [{"path": a["path"], "asset_id": a["asset_id"], "size": a["size"]} for a in r["results"]]
        url = r["next"]
    df = pd.DataFrame(rows)
    df["subject"] = df.path.str.extract(r"sub-([^/]+)/")[0]
    df["kind"] = df.path.str.extract(r"(HomeCage|LinearTrack)")[0]
    df["session_number"] = df.path.str.extract(r"_ses-[A-Za-z]+(\d+)")[0].astype(int)
    return df.sort_values(["subject", "kind", "session_number", "path"]).reset_index(drop=True)


def s3_url(asset_id: str) -> str:
    return requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60).url


def _s(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def open_file(asset_id: str) -> h5py.File:
    return h5py.File(remfile.File(s3_url(asset_id)), "r")


def read_meta(f: h5py.File) -> dict:
    g = lambda k: _s(f[k][()])
    return dict(subject_id=g("general/subject/subject_id"), genotype=g("general/subject/genotype"),
                sex=g("general/subject/sex"), age=g("general/subject/age"), virus=g("general/virus"),
                treatment=g("general/pharmacology"), session_id=g("general/session_id"),
                start=g("session_start_time"),
                probe=";".join(_s(f[f"general/devices/{k}"].attrs.get("description", "")) for k in f["general/devices"]))


# ---------------------------------------------------------------- signal helpers

def _zero_phase(x, taps):
    """Apply a symmetric FIR forwards and backwards along axis 0 (one convolution with taps * taps)."""
    k = np.convolve(taps, taps)
    return signal.oaconvolve(x, k[:, None] if x.ndim == 2 else k, mode="same", axes=0)


def remez_band(lo, hi, ntaps=101, tw=15.0):
    if lo <= 0:
        return signal.remez(ntaps, [0, hi, hi + tw, FS / 2], [1, 0], fs=FS)
    return signal.remez(ntaps, [0, lo - tw, lo, hi, hi + tw, FS / 2], [0, 1, 0], fs=FS)


def firls_band(lo, hi, ntaps):
    tw = max(1.0, 0.2 * lo)
    return signal.firls(ntaps, [0, lo - tw, lo, hi, hi + tw, FS / 2], [0, 0, 1, 1, 0, 0], fs=FS)


def envelope(x):
    n = next_fast_len(x.shape[0])
    X = sp_fft.fft(np.asarray(x, np.float32), n=n, axis=0)
    h = np.zeros(n, np.float32)
    h[0] = 1
    h[1:(n + 1) // 2] = 2
    if n % 2 == 0:
        h[n // 2] = 1
    X *= h[:, None] if X.ndim == 2 else h
    return np.abs(sp_fft.ifft(X, axis=0)[: x.shape[0]])


def runs(mask):
    """Start and stop indices (stop exclusive) of True runs."""
    d = np.diff(np.concatenate([[0], mask.astype(np.int8), [0]]))
    return np.flatnonzero(d == 1), np.flatnonzero(d == -1)


def speed_trace(f, n_lfp):
    """Smoothed speed (cm/s) at each LFP sample (Methods: Gaussian-smoothed velocity)."""
    ps = f["processing/behavior/Position/SpatialSeries"]
    t = ps["timestamps"][:]
    xy = ps["data"][:]
    ok = np.isfinite(t) & np.all(np.isfinite(xy), axis=1)
    t, xy = t[ok], xy[ok]
    t, idx = np.unique(t, return_index=True)
    xy = xy[idx]
    grid = np.arange(t[0], t[-1], 1 / POS_HZ)
    gx = np.interp(grid, t, xy[:, 0])
    gy = np.interp(grid, t, xy[:, 1])
    sig = SPEED_SMOOTH_S * POS_HZ
    gx, gy = gaussian_filter1d(gx, sig), gaussian_filter1d(gy, sig)
    sp = np.hypot(np.gradient(gx), np.gradient(gy)) * POS_HZ
    tl = np.arange(n_lfp) / FS
    return np.interp(tl, grid, sp, left=np.nan, right=np.nan), dict(pos_t0=float(t[0]), pos_t1=float(t[-1]),
                                                                   pos_hz=float(1 / np.median(np.diff(t))),
                                                                   x_range=(float(xy[:, 0].min()), float(xy[:, 0].max())),
                                                                   y_range=(float(xy[:, 1].min()), float(xy[:, 1].max())))


def rest_mask(speed):
    """Extended immobility: speed < 1 cm/s for 30 s or more, the first 30 s left out."""
    still = speed < IMMOBILE_CM_S
    st, en = runs(still)
    m = np.zeros_like(still)
    k = int(IMMOBILE_MIN_S * FS)
    for a, b in zip(st, en):
        if b - a > k:
            m[a + k:b] = True
    return m


def read_lfp(f):
    d = f["processing/ecephys/LFP/ElectricalSeries/data"]
    n = d.shape[0]
    out = np.empty(d.shape, dtype=np.int16)
    step = 400_000
    for a in range(0, n, step):
        out[a:a + step] = d[a:a + step]
    conv = float(d.attrs.get("conversion", 1.0))
    return out, conv


def read_units(f):
    st = f["units/spike_times"][:]
    idx = f["units/spike_times_index"][:]
    el = f["units/electrodes"][:]
    trains, a = {}, 0
    n_zero = 0
    for i, b in enumerate(idx):
        s = st[a:b]
        n_zero += int(np.sum(s == 0.0))
        trains[int(el[i])] = np.sort(s[s > 0.0])
        a = b
    return trains, n_zero


def site_table(f):
    loc = [_s(x) for x in f["general/extracellular_ephys/electrodes/location"][:]]
    grp = [_s(x) for x in f["general/extracellular_ephys/electrodes/group_name"][:]]
    return pd.DataFrame({"site": np.arange(len(loc)), "label": loc, "shank": grp})


def region_sites(sites: pd.DataFrame) -> dict:
    lab = sites.label
    out = {
        "ca1_ref": sites.site[lab.str.startswith("ca1-pyr 1")].tolist(),
        "ca1_pyr": sites.site[lab.str.startswith("ca1-pyr")].tolist(),
        "ca1_sr": sites.site[lab.str.match(r"^ca1-sr( mua)?$")].tolist(),
        "ca3": sites.site[lab.str.match(r"^ca3-(pyr|sr)( mua)?$")].tolist(),
        "dg": sites.site[lab.str.match(r"^dg-val (gc|hil)( mua)?$")].tolist(),
        "ca1_mua": sites.site[lab.str.startswith("ca1") & lab.str.endswith("mua")].tolist(),
        "ca3_mua": sites.site[lab.str.startswith("ca3") & lab.str.endswith("mua")].tolist(),
        "dg_mua": sites.site[lab.str.startswith("dg") & lab.str.endswith("mua")].tolist(),
    }
    # CA3 SWR site: the CA3 pyramidal-layer site closest to the layer centre; the labels mark the
    # highest-MUA CA3 site, which is used when it is in pyr, otherwise the first ca3-pyr site on its shank.
    c3 = sites[lab.str.startswith("ca3-pyr")]
    ref = None
    if out["ca3_mua"]:
        m = sites.loc[out["ca3_mua"][0]]
        if m.label.startswith("ca3-pyr"):
            ref = int(m.site)
        else:
            same = c3[c3.shank == m.shank]
            ref = int(same.site.iloc[0]) if len(same) else None
    if ref is None and len(c3):
        ref = int(c3.site.iloc[0])
    out["ca3_ref"] = [ref] if ref is not None else []
    # SW amplitude site: CA1-sr site on the shank of the SWR detection site (reading a)
    if out["ca1_ref"]:
        sh = sites.shank[out["ca1_ref"][0]]
        s = sites[(sites.shank == sh) & sites.site.isin(out["ca1_sr"])]
        out["ca1_sr_ref"] = [int(s.site.iloc[0])] if len(s) else out["ca1_sr"][:1]
    else:
        out["ca1_sr_ref"] = out["ca1_sr"][:1]
    return out


# ---------------------------------------------------------------- SWR detection

def detect_events(env, mask, mean, sd, thr_sd=RIPPLE_SD, min_s=RIPPLE_MIN_S):
    """Events where env exceeds mean + thr_sd*sd for min_s, extended to where env crosses the mean."""
    above = (env > mean + thr_sd * sd) & mask
    st, en = runs(above)
    keep = (en - st) >= int(round(min_s * FS))
    st, en = st[keep], en[keep]
    over_mean = env > mean
    ms, me = runs(over_mean)
    ev = []
    for a, b in zip(st, en):
        k = np.searchsorted(ms, a, side="right") - 1
        s0, e0 = (ms[k], me[k]) if k >= 0 and me[k] >= b else (a, b)
        ev.append((s0, e0))
    ev = sorted(set(ev))
    return np.array(ev, dtype=int).reshape(-1, 2)


def period_edges_ok(ev, mask):
    """Event lies inside one rest period and at least EDGE_S from its edges."""
    st, en = runs(mask)
    e = int(EDGE_S * FS)
    ok = np.zeros(len(ev), bool)
    pid = np.full(len(ev), -1)
    for i, (a, b) in enumerate(ev):
        k = np.searchsorted(st, a, side="right") - 1
        if k >= 0 and a >= st[k] + e and b <= en[k] - e:
            ok[i] = True
            pid[i] = k
    return ok, pid


def ripple_features(filt, env_z, ev):
    rows = []
    for a, b in ev:
        seg = filt[a:b]
        pk, _ = signal.find_peaks(seg)
        f = FS / np.diff(pk) if len(pk) > 1 else np.array([])
        rows.append((env_z[a:b].max(), (b - a) / FS, f.mean() if len(f) else np.nan))
    return np.array(rows).reshape(-1, 3)


def mua_norm(train, ev, mask):
    """Normalised MUA per event, code RTMUA.m normrate: (rate in event - mean rest rate) / SD rest rate (100 ms bins)."""
    if train is None or len(train) == 0:
        return np.full(len(ev), np.nan), np.nan, np.nan
    st, en = runs(mask)
    counts = []
    for a, b in zip(st, en):
        edges = np.arange(a / FS, b / FS + 1e-9, 0.1)
        if len(edges) > 1:
            counts.append(np.histogram(train, edges)[0])
    c = np.concatenate(counts) if counts else np.array([0])
    rate = c / 0.1
    mu, sd = rate.mean(), rate.std()
    n = np.searchsorted(train, ev[:, 1] / FS) - np.searchsorted(train, ev[:, 0] / FS)
    r = n / ((ev[:, 1] - ev[:, 0]) / FS)
    return (r - mu) / sd if sd > 0 else np.full(len(ev), np.nan), mu, sd


def minute_bins(mask, times_s):
    """Counts of event times in complete 1 min bins of each rest period."""
    st, en = runs(mask)
    return minute_bins_periods(np.c_[st, en] / FS, times_s)


def minute_bins_periods(periods, times_s):
    out = []
    for a, b in (periods * FS).astype(int):
        n = int((b - a) // (60 * FS))
        for j in range(n):
            t0 = (a + j * 60 * FS) / FS
            out.append(np.sum((times_s >= t0) & (times_s < t0 + 60)))
    return np.array(out, dtype=float)


def chain_flags(ev, pid, mask):
    """1 when another SWR starts within 200 ms of this one's end; NaN when that window leaves the rest period."""
    st, en = runs(mask)
    out = np.zeros(len(ev))
    starts = ev[:, 0]
    for i, (a, b) in enumerate(ev):
        nxt = starts[(starts > b) & (starts <= b + CHAIN_S * FS)]
        if len(nxt):
            out[i] = 1
        elif b + CHAIN_S * FS > en[pid[i]]:
            out[i] = np.nan
    return out


# ---------------------------------------------------------------- home cage session

def process_homecage(asset_id: str) -> dict:
    t0 = time.time()
    f = open_file(asset_id)
    meta = read_meta(f)
    sites = site_table(f)
    reg = region_sites(sites)
    lfp, conv = read_lfp(f)
    n = lfp.shape[0]
    speed, pinfo = speed_trace(f, n)
    rest = rest_mask(np.nan_to_num(speed, nan=99.0))
    trains, n_zero = read_units(f)
    rs, re_ = runs(rest)
    out = dict(meta=meta, sites=sites, regions=reg, n_samples=n, conv=conv, pos=pinfo, n_zero_spikes=n_zero,
               rest_s=rest.sum() / FS, rest_periods=np.c_[rs, re_] / FS, lfp_range=(int(lfp.min()), int(lfp.max())),
               n_spikes={k: len(v) for k, v in trains.items()})
    if not reg["ca1_ref"] or rest.sum() < 60 * FS:
        out["skipped"] = "no ca1-pyr 1 site" if not reg["ca1_ref"] else "less than 1 min of rest"
        return out
    # ripple band on all sites (artifact check) and on the reference site
    rtaps = remez_band(*RIPPLE_BAND)
    good = [s for s in range(lfp.shape[1]) if sites.label[s] not in ("", "dead")]
    gauss = lambda x: gaussian_filter1d(x, RIPPLE_SMOOTH_S * FS, axis=0)
    zall = np.zeros((n, len(good)), dtype=bool)     # site's ripple envelope above 5 SD
    for j0 in range(0, len(good), 4):
        cols = good[j0:j0 + 4]
        x = lfp[:, cols].astype(np.float32) * conv
        e = gauss(envelope(_zero_phase(x, rtaps)))
        mu, sd = e[rest].mean(0), e[rest].std(0)
        with np.errstate(invalid="ignore", divide="ignore"):
            zall[:, j0:j0 + len(cols)] = (e - mu) / sd > ARTIFACT_SD
    del x, e

    def swrs(site, keep_mask=rest):
        x = lfp[:, site].astype(np.float64) * conv
        filt = _zero_phase(x, rtaps)
        env = gauss(envelope(filt))
        mu, sd = env[rest].mean(), env[rest].std()
        ev = detect_events(env, rest, mu, sd)
        all_len = (ev[:, 1] - ev[:, 0]) / FS
        ok, pid = period_edges_ok(ev, rest)
        ev, pid = ev[ok], pid[ok]
        nart = np.array([zall[a:b].any(0).sum() for a, b in ev]) if len(ev) else np.array([])
        art = nart >= ARTIFACT_SITES
        feats = ripple_features(filt, (env - mu) / sd, ev)
        return dict(ev=ev, pid=pid, art=art, feats=feats, mu=mu, sd=sd, filt=filt, all_len=all_len)

    ca1 = swrs(reg["ca1_ref"][0])
    keep = ~ca1["art"]
    ev, pid, feats = ca1["ev"][keep], ca1["pid"][keep], ca1["feats"][keep]
    out["n_artifact"] = int(ca1["art"].sum())
    out["all_event_lengths"] = ca1["all_len"]     # every detected event, before the edge and artifact rules
    out["ripple_band"] = dict(mean=ca1["mu"], sd=ca1["sd"])
    # SW amplitude on CA1-sr: (a) the sr site on the detection shank, (b) every CA1-sr site
    sw_taps = remez_band(0, 30.0, ntaps=301)
    sw = {}
    for s in reg["ca1_sr"]:
        x = lfp[:, s].astype(np.float64) * conv
        e = envelope(_zero_phase(x, sw_taps))
        sw[s] = np.array([e[a:b].max() for a, b in ev])
    ev_df = pd.DataFrame({"start": ev[:, 0] / FS, "end": ev[:, 1] / FS, "size": feats[:, 0], "length": feats[:, 1],
                          "freq": feats[:, 2], "chain": chain_flags(ev, pid, rest) if len(ev) else []})
    if reg["ca1_sr_ref"]:
        ev_df["sw_amp"] = sw[reg["ca1_sr_ref"][0]]
    out["sw_all_sites"] = pd.DataFrame(sw) if sw else pd.DataFrame()
    out["swr"] = ev_df
    out["swr_minutes"] = minute_bins(rest, ev_df.start.values)
    out["swr_minutes_5sd"] = minute_bins(rest, ev_df.start.values[ev_df["size"].values >= 5])
    # CA3 SWRs
    if reg["ca3_ref"]:
        c3 = swrs(reg["ca3_ref"][0])
        k3 = ~c3["art"]
        e3, f3 = c3["ev"][k3], c3["feats"][k3]
        mids = (ev[:, 0] + ev[:, 1]) / 2
        ov = np.array([np.any((mids >= a) & (mids <= b)) for a, b in e3]) if len(e3) else np.array([], bool)
        out["ca3_swr"] = pd.DataFrame({"start": e3[:, 0] / FS, "end": e3[:, 1] / FS, "size": f3[:, 0],
                                       "length": f3[:, 1], "freq": f3[:, 2], "overlap": ov})
        out["ca3_minutes"] = minute_bins(rest, out["ca3_swr"].start.values)
        out["ca3_minutes_overlap"] = minute_bins(rest, out["ca3_swr"].start.values[ov])
    # rest SG power (30-50 Hz), (a) squared Hilbert envelope over rest, per region (mean over sites)
    sg_taps = remez_band(*REST_SG, ntaps=301, tw=5.0)
    rsg = {}
    for r in ("ca1_sr", "ca3", "dg"):
        vals = []
        for s in reg[r]:
            x = lfp[:, s].astype(np.float64) * conv
            p = envelope(_zero_phase(x, sg_taps)) ** 2
            vals.append((p[rest].mean(), p[rest].std()))
        if vals:
            v = np.array(vals)
            rsg[r] = dict(mean=v[:, 0].mean(), sd=v[:, 1].mean())
    out["rest_sg"] = rsg
    # (b) multitaper band power (1 s windows, tapers [3 5]) over 1 s bins wholly in rest
    nb1 = n // 1000
    idx = np.flatnonzero(rest[: nb1 * 1000].reshape(nb1, 1000).all(1))
    tap = _dpss()
    fr = np.fft.rfftfreq(1000, 1 / FS)
    band = (fr >= REST_SG[0]) & (fr <= REST_SG[1])
    rmt = {}
    for r in ("ca1_sr", "ca3", "dg"):
        vals = []
        for s in reg[r]:
            x = lfp[: nb1 * 1000, s].astype(np.float64).reshape(nb1, 1000)[idx] * conv
            x = x - x.mean(1, keepdims=True)
            P = 2 * (np.abs(np.fft.rfft(x[:, None, :] * tap[None], axis=2)) ** 2).mean(1)[:, band].mean(1) / FS
            vals.append((P.mean(), P.std()))
        if vals:
            v = np.array(vals)
            rmt[r] = dict(mean=v[:, 0].mean(), sd=v[:, 1].mean())
    out["rest_sg_mt"] = rmt
    # dentate spikes on the DG MUA site (Methods, paragraph 6)
    if reg["dg_mua"]:
        out["ds"] = dentate_spikes(lfp[:, reg["dg_mua"][0]].astype(np.float64) * conv, rest)
    mua_measures(out, trains, rest)
    out["seconds"] = time.time() - t0
    out["maxrss_kb"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return out


LAG_MAX_S, LAG_MIN_RATIO = 2.0, 3.0   # search range and the peak over median below which no offset is taken (choices)


def mua_lag(train, mids, max_lag=LAG_MAX_S, step=0.01):
    """Lag of the peak of the MUA cross-correlogram around SWR midpoints, and peak over median."""
    lags = np.arange(-max_lag, max_lag + step / 2, step)
    h = np.zeros(len(lags) - 1)
    for t in mids:
        a, b = np.searchsorted(train, [t - max_lag, t + max_lag])
        h += np.histogram(train[a:b] - t, lags)[0]
    h = np.convolve(h, np.ones(3) / 3, mode="same")
    c = lags[:-1] + step / 2
    return float(c[np.argmax(h)]), float(h.max() / max(np.median(h), 1))


def mua_measures(out, trains, rest):
    """Normalised MUA for SWRs, CA3 SWRs and dentate spikes, as deposited and with the session's spike
    times shifted so that CA1 MUA peaks at the CA1 SWR midpoints (the clock offset found in the data)."""
    reg = out["regions"]
    tr = {r: trains.get(reg[f"{r}_mua"][0]) if reg[f"{r}_mua"] else None for r in ("ca1", "ca3", "dg")}
    sw = out["swr"]
    lag, ratio = (np.nan, np.nan)
    if tr["ca1"] is not None and len(sw):
        lag, ratio = mua_lag(tr["ca1"], ((sw.start + sw.end) / 2).values)
    out["mua_lag"], out["mua_lag_peak_ratio"] = lag, ratio
    for version, shift in (("", 0.0), ("_aligned", lag)):
        if not np.isfinite(shift) or (version and not ratio >= LAG_MIN_RATIO):
            continue
        ttr = {r: (t - shift if t is not None else None) for r, t in tr.items()}
        evs = {"swr": out["swr"], "ca3_swr": out.get("ca3_swr"), "ds": out.get("ds")}
        regions = {"swr": ("ca1", "ca3", "dg"), "ca3_swr": ("ca3",), "ds": ("dg",)}
        for k, df in evs.items():
            if df is None or not len(df):
                continue
            ev = np.c_[df.start.values, df.end.values] * FS
            for r in regions[k]:
                m, mu, sd = mua_norm(ttr[r], ev.astype(int), rest)
                df[f"mua_{r}{version}"] = m
                if k == "swr" and version == "":
                    out[f"rest_mua_{r}"] = mu


def dentate_spikes(x, rest):
    taps = remez_band(5.0, 100.0, ntaps=301, tw=4.0)
    y = _zero_phase(x, taps)
    z = (y - y[rest].mean()) / y[rest].std()
    pk, _ = signal.find_peaks(z)
    mn, _ = signal.find_peaks(-z)
    if len(pk) < 3 or len(mn) < 3:
        return pd.DataFrame(columns=["t", "start", "end", "amp", "length"])
    j = np.searchsorted(mn, pk)
    ok = (j > 0) & (j < len(mn))
    pk, j = pk[ok], j[ok]
    before, after = mn[j - 1], mn[j]
    closest = np.where(pk - before <= after - pk, before, after)
    amp = z[pk] - z[closest]
    length = (after - before) / FS
    la = np.log(np.maximum(amp, 1e-9))
    za = (la - la.mean()) / la.std()
    ds = (za > 0.75) & (length >= 0.005) & (length <= 0.025) & rest[pk]
    st, en = runs(rest)
    ok2, _ = period_edges_ok(np.c_[before, after], rest)
    ds &= ok2
    return pd.DataFrame({"t": pk[ds] / FS, "start": before[ds] / FS, "end": after[ds] / FS, "amp": amp[ds],
                         "length": length[ds]})


# ---------------------------------------------------------------- linear track session

def _dpss(n=1000, nw=3.0, k=5):
    return signal.windows.dpss(n, nw, Kmax=k)


def process_track(asset_id: str) -> dict:
    t0 = time.time()
    f = open_file(asset_id)
    meta = read_meta(f)
    sites = site_table(f)
    reg = region_sites(sites)
    lfp, conv = read_lfp(f)
    n = lfp.shape[0]
    speed, pinfo = speed_trace(f, n)
    sp = np.nan_to_num(speed, nan=0.0)
    run = sp > RUN_CM_S
    trains, n_zero = read_units(f)
    out = dict(meta=meta, sites=sites, regions=reg, n_samples=n, conv=conv, pos=pinfo, n_zero_spikes=n_zero,
               run_s=run.sum() / FS, speed_run=float(sp[run].mean()) if run.any() else np.nan,
               speed_all=float(np.nanmean(speed)), lfp_range=(int(lfp.min()), int(lfp.max())))
    # MUA in 100 ms bins wholly in run
    nb = n // 100
    rb = run[: nb * 100].reshape(nb, 100).all(1)
    edges = np.arange(nb + 1) * 0.1
    mua = {}
    for r in ("ca1", "ca3", "dg"):
        s = reg[f"{r}_mua"]
        if s and s[0] in trains:
            mua[r] = np.histogram(trains[s[0]], edges)[0][rb] / 0.1
    out["mua_run"] = mua
    # 1 s bins wholly in run
    nb1 = n // 1000
    b1 = run[: nb1 * 1000].reshape(nb1, 1000).all(1)
    idx = np.flatnonzero(b1)
    out["n_bins"] = len(idx)
    tap = _dpss()
    freqs = np.fft.rfftfreq(1000, 1 / FS)
    keepf = freqs <= 120
    if reg["ca1_ref"]:
        x = lfp[: nb1 * 1000, reg["ca1_ref"][0]].astype(np.float64).reshape(nb1, 1000) * conv
        x = x - x.mean(1, keepdims=True)
        P = (np.abs(np.fft.rfft(x[:, None, :] * tap[None], axis=2)) ** 2).mean(1)
        th = np.log(P[:, (freqs >= THETA[0]) & (freqs <= THETA[1])].mean(1))
        spb = sp[: nb1 * 1000].reshape(nb1, 1000).mean(1)
        out["clock"] = {k: float(np.corrcoef(th[max(0, k):nb1 + min(0, k)], spb[max(0, -k):nb1 - max(0, k)])[0, 1])
                        for k in (-30, 0, 30)}
    fr = freqs[keepf]
    bands = {"theta": (fr >= THETA[0]) & (fr <= THETA[1]), "sg": (fr >= SG[0]) & (fr <= SG[1]),
             "fg": (fr >= FG[0]) & (fr <= FG[1])}
    use = sorted(set(reg["ca1_pyr"] + reg["ca3"] + reg["dg"] + reg["ca1_ref"]))
    spec = {}
    for s in use:
        x = lfp[: nb1 * 1000, s].astype(np.float64).reshape(nb1, 1000)[idx] * conv
        x = x - x.mean(1, keepdims=True)
        X = np.fft.rfft(x[:, None, :] * tap[None], axis=2)[:, :, keepf] / np.sqrt(FS)
        spec[s] = X
    def bandpow(s, b):
        return (np.abs(spec[s]) ** 2).mean(1)[:, bands[b]].mean(1) * 2
    bins = {}
    for r, key in (("ca1", "ca1_pyr"), ("ca3", "ca3"), ("dg", "dg")):
        ss = reg[key]
        if not ss:
            continue
        for b in ("theta", "sg", "fg"):
            bins[f"{b}_pow_{r}"] = np.mean([bandpow(s, b) for s in ss], axis=0)
        bins[f"sgfg_{r}"] = np.mean([bandpow(s, "sg") / bandpow(s, "fg") for s in ss], axis=0)
    # coherence, CA1 reference site with each site of CA3 and DG: (a) per 1 s bin, (b) over all run
    coh_sess = {}
    if reg["ca1_ref"]:
        a = spec[reg["ca1_ref"][0]]
        saa = (np.abs(a) ** 2).mean(1)
        for r, key in (("ca3", "ca3"), ("dg", "dg")):
            if not reg[key]:
                continue
            for b in ("theta", "sg", "fg"):
                cb, cs = [], []
                for s in reg[key]:
                    c = spec[s]
                    sab = (a * np.conj(c)).mean(1)
                    scc = (np.abs(c) ** 2).mean(1)
                    coh = np.abs(sab) / np.sqrt(saa * scc)
                    cb.append(coh[:, bands[b]].mean(1))
                    cs.append((np.abs(sab.mean(0)) / np.sqrt(saa.mean(0) * scc.mean(0)))[bands[b]].mean())
                bins[f"{b}_coh_{r}"] = np.mean(cb, axis=0)
                coh_sess[f"{b}_coh_{r}"] = float(np.mean(cs))
    out["coh_session"] = coh_sess
    del spec
    # band-filtered traces: instantaneous frequency (one site per region) and modulation index
    taps = {"theta": firls_band(*THETA, 1001), "sg": firls_band(*SG, 301), "fg": firls_band(*FG, 151)}
    freq_sites = {"ca1": reg["ca1_ref"][:1], "ca3": reg["ca3_mua"][:1] or reg["ca3"][:1], "dg": reg["dg_mua"][:1] or reg["dg"][:1]}
    ifreq = {}
    st, en = runs(run)
    seg_id = np.zeros(n, int) - 1
    for k, (a, b) in enumerate(zip(st, en)):
        seg_id[a:b] = k
    mi = {}
    for r, key in (("ca1", "ca1_pyr"), ("ca3", "ca3"), ("dg", "dg")):
        ss = reg[key]
        if not ss:
            continue
        mis = {"sg": [], "fg": []}
        for s in ss:
            x = lfp[:, s].astype(np.float64) * conv
            th = _zero_phase(x, taps["theta"])
            ph = np.angle(signal.hilbert(th, N=next_fast_len(n))[:n])
            pb = np.minimum(((ph + np.pi) / (2 * np.pi) * N_PHASE_BINS).astype(int), N_PHASE_BINS - 1)
            pbb = pb[: nb1 * 1000].reshape(nb1, 1000)[idx]
            filt = {"theta": th}
            for b in ("sg", "fg"):
                filt[b] = _zero_phase(x, taps[b])
                amp = envelope(filt[b])[: nb1 * 1000].reshape(nb1, 1000)[idx]
                M = np.zeros((len(idx), N_PHASE_BINS))
                C = np.zeros((len(idx), N_PHASE_BINS))
                rows = np.repeat(np.arange(len(idx)), 1000)
                np.add.at(M, (rows, pbb.ravel()), amp.ravel())
                np.add.at(C, (rows, pbb.ravel()), 1)
                mean_amp = M / np.maximum(C, 1)
                p = mean_amp / mean_amp.sum(1, keepdims=True)
                h = -(p * np.log(np.where(p > 0, p, 1))).sum(1)
                mis[b].append((np.log(N_PHASE_BINS) - h) / np.log(N_PHASE_BINS))
            if s in freq_sites[r]:
                for b in ("theta", "sg", "fg"):
                    pk, _ = signal.find_peaks(filt[b])
                    pk = pk[run[pk]]
                    same = seg_id[pk[1:]] == seg_id[pk[:-1]]
                    fq = FS / np.diff(pk)
                    ifreq[f"{b}_freq_{r}"] = fq[same].astype(np.float32)
        for b in ("sg", "fg"):
            bins[f"{b}_mi_{r}"] = np.mean(mis[b], axis=0)
    out["bins"] = pd.DataFrame(bins)
    out["ifreq"] = ifreq
    out["seconds"] = time.time() - t0
    out["maxrss_kb"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return out


# ---------------------------------------------------------------- linear mixed models

def cell_stats(df, value, animal="animal", treat="cno"):
    """Per animal and treatment: n, mean, within sum of squares."""
    g = df.groupby([animal, treat])[value]
    s = g.agg(["size", "mean", "var"]).reset_index()
    s["ss"] = s["var"].fillna(0) * (s["size"] - 1)
    return s.rename(columns={animal: "animal", treat: "cno"})


def _animal_blocks(cs, groups=None):
    blocks = []
    for a, g in cs.groupby("animal", sort=False):
        grp = groups.get(a, 0) if groups is not None else 0
        blocks.append((g["cno"].values.astype(float), g["size"].values.astype(float), g["mean"].values,
                       g["ss"].values, grp))
    return blocks


def _negll(theta, blocks, ngroups, return_beta=False):
    try:
        return _negll_core(theta, blocks, ngroups, return_beta)
    except (np.linalg.LinAlgError, FloatingPointError, OverflowError):
        if return_beta:
            raise
        return 1e20


def _negll_core(theta, blocks, ngroups, return_beta=False):
    # theta: log sigma, then per group the 3 Cholesky entries of G (2x2)
    s2 = np.exp(2 * theta[0])
    Ls = []
    for gi in range(ngroups):
        l11, l21, l22 = theta[1 + 3 * gi: 4 + 3 * gi]
        L = np.array([[np.exp(l11), 0], [l21, np.exp(l22)]])
        Ls.append(L @ L.T)
    p = 2 * ngroups
    XtVX = np.zeros((p, p))
    XtVy = np.zeros(p)
    logdet, wss, ntot = 0.0, 0.0, 0.0
    cache = []
    for t, nn, m, ss, grp in blocks:
        Z = np.c_[np.ones_like(t), t]
        G = Ls[grp]
        sq = np.sqrt(nn)
        V = (sq[:, None] * (Z @ G @ Z.T) * sq[None, :]) + s2 * np.eye(len(t))
        Vi = np.linalg.inv(V)
        X = np.zeros((len(t), p))
        X[:, 2 * grp] = sq
        X[:, 2 * grp + 1] = sq * t
        w = sq * m
        XtVX += X.T @ Vi @ X
        XtVy += X.T @ Vi @ w
        logdet += np.linalg.slogdet(V)[1] + (nn.sum() - len(t)) * np.log(s2)
        wss += ss.sum() / s2
        ntot += nn.sum()
        cache.append((X, w, Vi))
    beta = np.linalg.solve(XtVX, XtVy)
    q = wss
    for X, w, Vi in cache:
        r = w - X @ beta
        q += r @ Vi @ r
    nll = 0.5 * (ntot * np.log(2 * np.pi) + logdet + q)
    if return_beta:
        return nll, beta, np.linalg.inv(XtVX), ntot
    return nll


def fit_lmm(cs, groups=None, ngroups=1):
    """ML fit of feature ~ treatment + (treatment|animal) from cell statistics; with groups, one set of
    fixed effects and one random-effects covariance per group and a shared residual variance."""
    blocks = _animal_blocks(cs, groups)
    w = np.concatenate([b[1] for b in blocks])
    mu = np.average(np.concatenate([b[2] for b in blocks]), weights=w)
    var = (np.sum([b[3].sum() for b in blocks]) + np.sum([(b[1] * (b[2] - mu) ** 2).sum() for b in blocks])) / w.sum()
    best = None
    for scale in (0.3, 0.05, 1.0):
        th0 = [0.5 * np.log(var * 0.8)] + [0.5 * np.log(var * scale), 0.0, 0.5 * np.log(var * scale * 0.3)] * ngroups
        r = optimize.minimize(_negll, th0, args=(blocks, ngroups), method="L-BFGS-B")
        if best is None or r.fun < best.fun:
            best = r
    nll, beta, cov, ntot = _negll(best.x, blocks, ngroups, return_beta=True)
    return dict(ll=-nll, beta=beta, cov=cov, n=ntot, theta=best.x, converged=bool(best.success))


def treatment_test(cs):
    """F test of the treatment fixed effect (code calcLMM.m, coefTest; residual df n - 2)."""
    r = fit_lmm(cs)
    b, v = r["beta"][1], r["cov"][1, 1]
    F = b * b / v
    p = stats.f.sf(F, 1, r["n"] - 2)
    return dict(coef=b, intercept=r["beta"][0], se=np.sqrt(v), F=F, df2=r["n"] - 2, p=p, n_obs=int(r["n"]),
                n_animals=cs.animal.nunique(), converged=r["converged"])


def genotype_test(cs_a, cs_b):
    """LRT of feature ~ treatment + (treatment|animal) against feature ~ treatment:genotype +
    (treatment:genotype|animal), data of two genotypes pooled (Quantification, paragraph 2)."""
    cs = pd.concat([cs_a.assign(g=0), cs_b.assign(g=1)])
    groups = dict(zip(cs.animal, cs.g))
    r0 = fit_lmm(cs)
    r1 = fit_lmm(cs, groups, 2)
    lr = max(0.0, 2 * (r1["ll"] - r0["ll"]))
    return dict(LR=lr, p_df9=stats.chi2.sf(lr, 9), p_df5=stats.chi2.sf(lr, 5),
                coef_a=r1["beta"][1], coef_b=r1["beta"][3])


def log_values(x):
    """Log transform as the code (calcLMM.m): shift to a minimum of 0.001 when values reach 0 or below."""
    x = np.asarray(x, float)
    if np.nanmin(x) <= 0:
        x = x - np.nanmin(x) + 0.001
    return np.log(x)


def holm(pvals, m=None, alpha=0.05):
    """Holm-Bonferroni over the given p-values, with m the family size (uncomputed comparisons ranked last)."""
    p = np.asarray(pvals, float)
    m = max(m or len(p), len(p))
    order = np.argsort(p)
    sig = np.zeros(len(p), bool)
    for k, i in enumerate(order):
        if p[i] < alpha / (m - k):
            sig[i] = True
        else:
            break
    return sig


# ---------------------------------------------------------------- driver

def _safe(fn, asset_id):
    try:
        return fn(asset_id)
    except Exception as e:  # recorded and reported in the notebook, never replaced by a default
        return dict(error=f"{type(e).__name__}: {e}", asset_id=asset_id)


def process_many(asset_ids, kind, workers=4):
    from concurrent.futures import ProcessPoolExecutor
    fn = process_homecage if kind == "HomeCage" else process_track
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(_safe, [fn] * len(asset_ids), asset_ids))


# ---------------------------------------------------------------- tables and tests

GROUPS = {"PV": "PV-Cre", "SST": "SST-Cre", "PS": "PV-Cre/SST-Cre"}
REST_FAMILY, RUN_FAMILY = 24, 36   # Quantification, paragraph 3
SKEW_LOG = 1.0                     # reading (a): log when within-cell residual skewness exceeds 1 (assumption)


def group_of(meta):
    if meta["virus"] == "Empty Vector":
        return "EV"
    return {v: k for k, v in GROUPS.items()}[meta["genotype"]]


def session_table(results):
    rows = []
    for i, r in enumerate(results):
        if "error" in r:
            rows.append(dict(i=i, error=r["error"], asset_id=r["asset_id"]))
            continue
        m = r["meta"]
        rows.append(dict(i=i, animal=m["subject_id"], group=group_of(m), genotype=m["genotype"], virus=m["virus"],
                         sex=m["sex"], treatment=m["treatment"], cno=int(m["treatment"] == "CNO"),
                         session=m["session_id"], minutes=r["n_samples"] / FS / 60, skipped=r.get("skipped")))
    return pd.DataFrame(rows)


def long_table(results, sessions, getter):
    """One row per observation: animal, group, cno, sex, value, from getter(result) -> array."""
    parts = []
    for _, s in sessions.iterrows():
        v = getter(results[s.i])
        if v is None:
            continue
        v = np.asarray(v, float)
        v = v[np.isfinite(v)]
        if len(v):
            parts.append(pd.DataFrame({"animal": s.animal, "group": s.group, "cno": s.cno, "sex": s.sex,
                                       "session": s.session, "value": v}))
    return pd.concat(parts, ignore_index=True) if parts else pd.DataFrame(columns=["animal", "group", "cno", "sex", "session", "value"])


def within_skew(df):
    r = df.value - df.groupby(["animal", "cno"]).value.transform("mean")
    return float(stats.skew(r))


def test_feature(df, groups=("PV", "SST"), pairs=(("PV", "SST"),)):
    """Treatment F test per group and genotype LRT per pair, under reading (a) (log when right skewed) and
    (b) (log always). The skewness is taken over the PV-Cre and SST-Cre data."""
    out = []
    sk = within_skew(df[df.group.isin(("PV", "SST"))] if df.group.isin(("PV", "SST")).any() else df)
    for reading in ("a", "b"):
        use_log = reading == "b" or sk > SKEW_LOG
        d = df.copy()
        if use_log:
            d["value"] = log_values(d.value)
        cs = {g: cell_stats(d[d.group == g], "value") for g in groups}
        for g in groups:
            if cs[g].animal.nunique() < 2 or cs[g].cno.nunique() < 2:
                continue
            t = treatment_test(cs[g])
            out.append(dict(reading=reading, log=use_log, skew=sk, test=g, coef=t["coef"], p=t["p"], F=t["F"],
                            n_animals=t["n_animals"], n_obs=t["n_obs"]))
        for pair in pairs:
            if not all(p in cs and len(cs[p]) for p in pair):
                continue
            gt = genotype_test(cs[pair[0]], cs[pair[1]])
            out.append(dict(reading=reading, log=use_log, skew=sk, test=f"{pair[0]} vs {pair[1]}",
                            coef=gt["coef_b"] - gt["coef_a"], p=gt["p_df9"], F=gt["LR"], p_df5=gt["p_df5"],
                            n_animals=cs[pair[0]].animal.nunique() + cs[pair[1]].animal.nunique(),
                            n_obs=int(cs[pair[0]]["size"].sum() + cs[pair[1]]["size"].sum())))
    return pd.DataFrame(out)


def blup_changes(df, group):
    """Per animal, CNO minus vehicle of the fitted conditional response (beta1 + b1), code calcLMM.m."""
    cs = cell_stats(df[df.group == group], "value")
    r = fit_lmm(cs)
    th = r["theta"]
    s2 = np.exp(2 * th[0])
    l11, l21, l22 = th[1:4]
    L = np.array([[np.exp(l11), 0], [l21, np.exp(l22)]])
    G = L @ L.T
    beta = r["beta"]
    out = {}
    for a, g in cs.groupby("animal", sort=False):
        t, nn, m = g.cno.values.astype(float), g["size"].values.astype(float), g["mean"].values
        Z = np.c_[np.ones_like(t), t]
        sq = np.sqrt(nn)
        Zt = sq[:, None] * Z
        V = Zt @ G @ Zt.T + s2 * np.eye(len(t))
        X = np.c_[sq, sq * t]
        b = G @ Zt.T @ np.linalg.solve(V, sq * m - X @ beta)
        out[a] = beta[1] + b[1]
    return pd.Series(out)


def mean_changes(df, group):
    m = df[df.group == group].groupby(["animal", "cno"]).value.mean().unstack()
    return (m[1] - m[0]).dropna()


def paired(per_animal):
    """Paired test as Table S2's note: t test when the differences pass Shapiro-Wilk and the variances an F test, else Wilcoxon."""
    d = per_animal.dropna()
    a, b = d[0].values, d[1].values
    diff = b - a
    normal = stats.shapiro(diff).pvalue > 0.05 if len(diff) >= 3 else False
    F = np.var(b, ddof=1) / np.var(a, ddof=1)
    pf = 2 * min(stats.f.cdf(F, len(a) - 1, len(b) - 1), stats.f.sf(F, len(a) - 1, len(b) - 1))
    tt = stats.ttest_rel(b, a)
    wx = stats.wilcoxon(b, a)
    use_t = normal and pf > 0.05
    return dict(n=len(d), veh=a.mean(), cno=b.mean(), diff=diff.mean(), t=tt.statistic, p_t=tt.pvalue,
                p_wilcoxon=wx.pvalue, test="paired t" if use_t else "Wilcoxon",
                p=tt.pvalue if use_t else wx.pvalue)


def decide(p, family, m_sig=None):
    """'sig', 'ns' or by Holm when between the bounds (m_sig: Holm significance from the family)."""
    if p < 0.05 / family:
        return "sig"
    if p >= 0.05:
        return "ns"
    return "sig" if m_sig else "ns"


def scan_one(asset_id):
    try:
        f = open_file(asset_id)
        m = read_meta(f)
        m["n_samples"] = f["processing/ecephys/LFP/ElectricalSeries/data"].shape[0]
        m["n_spikes"] = f["units/spike_times"].shape[0]
        m["rate"] = float(f["processing/ecephys/LFP/ElectricalSeries/starting_time"].attrs["rate"])
        m["unit"] = _s(f["processing/ecephys/LFP/ElectricalSeries/data"].attrs["unit"])
        m["description"] = _s(f["session_description"][()])
        m["asset_id"] = asset_id
        return m
    except Exception as e:
        return dict(asset_id=asset_id, error=f"{type(e).__name__}: {e}")


def scan(asset_ids, workers=16):
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(workers) as ex:
        return pd.DataFrame(list(ex.map(scan_one, asset_ids)))


# ---------------------------------------------------------------- features and claim parts

def _col(key, col):
    def g(r):
        df = r.get(key)
        return None if df is None or col not in df else df[col]
    return g


def _minutes(key, mask_col=None, min_size=None):
    def g(r):
        df = r.get(key)
        if df is None or "rest_periods" not in r:
            return None
        t = df.start.values if "start" in df else df.t.values
        if mask_col is not None:
            t = t[df[mask_col].values.astype(bool)]
        if min_size is not None:
            t = t[df["size"].values >= min_size]
        return minute_bins_periods(r["rest_periods"], t)
    return g


def _sel(key, col, mask_col=None, min_size=None):
    def g(r):
        df = r.get(key)
        if df is None or col not in df:
            return None
        v = df[col].values
        if mask_col is not None:
            v = v[df[mask_col].values.astype(bool)]
        if min_size is not None:
            v = v[df["size"].values >= min_size]
        return v
    return g


# Main readings first; the family of each rest comparison is the paper's 24 (17 computed here).
REST_FEATURES = {
    "swr_rate": _minutes("swr"), "chain": _col("swr", "chain"), "length": _col("swr", "length"),
    "freq": _col("swr", "freq"), "sw_amp": _col("swr", "sw_amp"), "size": _col("swr", "size"),
    "mua_ca1": _col("swr", "mua_ca1_aligned"), "mua_ca3": _col("swr", "mua_ca3_aligned"),
    "mua_dg": _col("swr", "mua_dg_aligned"),
    "ca3_rate": _minutes("ca3_swr"), "ca3_length": _col("ca3_swr", "length"), "ca3_freq": _col("ca3_swr", "freq"),
    "ca3_mua": _col("ca3_swr", "mua_ca3_aligned"),
    "ds_rate": _minutes("ds"), "ds_length": _col("ds", "length"), "ds_amp": _col("ds", "amp"),
    "ds_mua": _col("ds", "mua_dg_aligned"),
}
REST_VARIANTS = {
    "swr_rate_5sd": ("swr_rate", _minutes("swr", min_size=5)), "chain_5sd": ("chain", _sel("swr", "chain", min_size=5)),
    "length_5sd": ("length", _sel("swr", "length", min_size=5)), "freq_5sd": ("freq", _sel("swr", "freq", min_size=5)),
    "sw_amp_5sd": ("sw_amp", _sel("swr", "sw_amp", min_size=5)), "size_5sd": ("size", _sel("swr", "size", min_size=5)),
    "mua_ca1_deposited": ("mua_ca1", _col("swr", "mua_ca1")), "mua_ca3_deposited": ("mua_ca3", _col("swr", "mua_ca3")),
    "mua_dg_deposited": ("mua_dg", _col("swr", "mua_dg")),
    "sw_amp_all_sr_sites": ("sw_amp", lambda r: r["sw_all_sites"].values.ravel() if len(r.get("sw_all_sites", [])) else None),
    "ca3_rate_overlap": ("ca3_rate", _minutes("ca3_swr", mask_col="overlap")),
    "ca3_length_overlap": ("ca3_length", _sel("ca3_swr", "length", mask_col="overlap")),
    "ca3_freq_overlap": ("ca3_freq", _sel("ca3_swr", "freq", mask_col="overlap")),
    "ca3_mua_overlap": ("ca3_mua", _sel("ca3_swr", "mua_ca3_aligned", mask_col="overlap")),
    "ca3_mua_deposited": ("ca3_mua", _col("ca3_swr", "mua_ca3")),
    "ds_mua_deposited": ("ds_mua", _col("ds", "mua_dg")),
}


def _bins(k):
    return lambda r: r["bins"][k] if k in r["bins"] else None


RUN_FEATURES = {}
for _r in ("ca1", "ca3", "dg"):
    RUN_FEATURES[f"mua_{_r}"] = (lambda r, k=_r: r["mua_run"].get(k))
    for _b in ("theta", "sg", "fg"):
        RUN_FEATURES[f"{_b}_pow_{_r}"] = _bins(f"{_b}_pow_{_r}")
        RUN_FEATURES[f"{_b}_freq_{_r}"] = (lambda r, k=f"{_b}_freq_{_r}": r["ifreq"].get(k))
    RUN_FEATURES[f"sgfg_{_r}"] = _bins(f"sgfg_{_r}")
    RUN_FEATURES[f"sg_mi_{_r}"] = _bins(f"sg_mi_{_r}")
    RUN_FEATURES[f"fg_mi_{_r}"] = _bins(f"fg_mi_{_r}")
for _r in ("ca3", "dg"):
    for _b in ("theta", "sg", "fg"):
        RUN_FEATURES[f"{_b}_coh_{_r}"] = _bins(f"{_b}_coh_{_r}")


def build_tables(results, sessions, features):
    return {name: long_table(results, sessions, getter) for name, getter in features.items()}


def test_all(tables, groups=("PV", "SST"), pairs=(("PV", "SST"),)):
    out = []
    for name, d in tables.items():
        if not len(d):
            continue
        t = test_feature(d, groups, pairs)
        t.insert(0, "feature", name)
        out.append(t)
    return pd.concat(out, ignore_index=True)


def add_decisions(res, family, main_features, counterpart=None):
    """Holm-Bonferroni at 0.05 over the family (the paper's m; uncomputed comparisons ranked last). A
    variant's p is judged in place of its main feature's p (counterpart: variant -> main feature)."""
    counterpart = counterpart or {}
    res = res.copy()
    dec = []
    for _, r in res.iterrows():
        main = counterpart.get(r.feature, r.feature)
        fam = res[(res.reading == r.reading) & (res.test == r.test) & res.feature.isin(main_features)
                  & (res.feature != main)]
        ps = np.r_[fam.p.values, r.p]
        dec.append(bool(holm(ps, family)[-1]))
    res["significant"] = dec
    return res


def show_parts(res, parts):
    """parts: list of (feature, test, expected) with expected 'up', 'down', 'ns' or 'sig'. Prints each part
    under both log readings and whether it holds."""
    rows = []
    for feat, test, exp in parts:
        for reading in ("a", "b"):
            r = res[(res.feature == feat) & (res.test == test) & (res.reading == reading)]
            if not len(r):
                rows.append(dict(feature=feat, test=test, expected=exp, reading=reading, holds=None))
                continue
            r = r.iloc[0]
            if exp == "ns":
                ok = not r.significant
            elif exp == "sig":
                ok = r.significant
            else:
                ok = r.significant and ((r.coef > 0) if exp == "up" else (r.coef < 0))
            rows.append(dict(feature=feat, test=test, expected=exp, reading=reading, log=r.log, coef=r.coef,
                             stat=r.F, p=r.p, significant=r.significant, holds=ok, animals=r.n_animals, n=r.n_obs))
    t = pd.DataFrame(rows)
    return t
