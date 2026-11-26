"""Loading and measures for dandiset 001538 (Zhai et al. 2025, Science Advances).

Every file is streamed from the DANDI Archive with remfile and h5py; nothing is written to disk.
The paper's own tables (Zenodo record 17307059) and analysis notebooks (Zenodo records
14145776, 14163502 and 14163731) are read into memory from Zenodo.

Where each parameter comes from:

- Spike counts and rheobase: the paper's somatic script ("Input_output analysis ver2024.11",
  Zenodo 14145776) counts upward crossings of 0 mV over the whole sweep (count_events with
  threshold 0) and takes as rheobase the first positive step with a spike (rheobaseCal). The
  claims file fixes the same rule. When a cell holds a step more than once, the first sweep of
  that step is used: an assumption (the script numbers the sweeps in order and has no rule for
  a repeated step); the notebook shows how many cells it touches.
- Dendritic index: the paper's dendritic script ("PVAnalysis ver 2024.11", Zenodo 14163502):
  backgrounds of 55 (red) and 161 (green) subtracted, a 6-sample running mean, the three trials
  of a site averaged, R0 and G0 the means from 0.5 to 0.95 s, the area of (G - G0)/R0 from
  0.95 to 1.5 s, the index the distal area over the proximal area, and the basal ratio
  (G0/R0 distal over G0/R0 proximal). The claims file keeps pairs with a basal ratio between
  0.5 and 2, pairs proximal and distal sites by their number, and averages pairs within a cell.
- Sr2+-oEPSC events: the paper (Methods, "Data acquisition and statistical analysis") measures
  events from 40 to 400 ms after the light flash, with a detection threshold of five SD above
  the noise, using TaroTools in Igor Pro and visual checking. TaroTools cannot be run here.
  The detector below is a stand-in (an assumption): the current is smoothed with a 1 ms
  running mean, the noise SD is the MAD-based SD of the recorded trace minus its 20 ms running
  median from 500 to 900 ms after the flash (the SD of the smoothed trace is a variant), and an event is an inward peak whose prominence
  (within a 20 ms window) exceeds five noise SD, at least 3 ms after the previous event. The
  amplitude is the prominence. Frequency is events per second of analysed window (0.36 s per
  sweep), which reproduces the paper's per-cell frequencies as counts over 10 sweeps.
- GRAB-ACh3.0: the paper's script ("PVAnalysis-BOT for GRAB Ver 2024.11", Zenodo 14163731) and
  Methods: F0 the mean over the 1 s before the stimulus, the area of (F - F0)/(Fmax - Fmin)
  over the 2 s from the stimulus, the two trials of a condition averaged, Fmax the mean of the
  acetylcholine trial from 2 to 4 s, Fmin the smaller of the tetrodotoxin trial's mean from 2
  to 4 s and the quinpirole baseline. The PMT background cancels in (F - F0) and in
  (Fmax - Fmin), so its absence from the files does not matter. The ROI is a 50 um circle in
  the centre of the field (Methods); with 0.388 um pixels on a 128-pixel field this is the
  inscribed circle, computed here from the movies. The whole-frame brightness the files hold
  is a variant.
"""
import io
import re
import zipfile
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy import signal, stats

DANDISET = "001538"
VERSION = "0.261124.1858"
API = "https://api.dandiarchive.org/api"
TABLES_RECORD = "17307059"  # Zenodo, "Zhai et al. 2025 Datasets", latest version of 14589035
TABLES_FILE = "Zhai et al. 2025 Datasets.zip"

_session = requests.Session()


# ----------------------------------------------------------------------------- archive
def list_assets():
    """All assets of the pinned version, with the session fields parsed from the file name."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000"
    rows = []
    while url:
        js = _get(url).json()
        rows += js["results"]
        url = js["next"]
    df = pd.DataFrame(rows)[["asset_id", "path", "size"]]
    df["nwb"] = df.path.str.endswith(".nwb")
    ses = df.path.str.extract(r"_ses-([^/]+?)\.nwb$")[0]
    parts = ses.str.split(r"\+\+", expand=True)
    df["cell_type"], df["group"], df["drug"], df["genotype"] = parts[0], parts[1], parts[2], parts[3]
    tail = parts[4].str.split("_", n=1, expand=True)
    df["date"] = tail[0]
    df["kind"] = tail[1].fillna("")
    df["subject"] = df.path.str.split("/").str[0]
    return df


def _get(url, tries=6, **kw):
    """GET with retries on server errors; raises when every try fails."""
    import time
    for k in range(tries):
        r = _session.get(url, timeout=120, **kw)
        if r.status_code < 500:
            r.raise_for_status()
            return r
        time.sleep(5 * (k + 1))
    r.raise_for_status()


def s3_url(asset_id):
    r = _session.get(f"{API}/assets/{asset_id}/download/", allow_redirects=False, timeout=60)
    return r.headers["Location"]


def open_h5(asset_id):
    return h5py.File(remfile.File(s3_url(asset_id)), "r")


def _str(x):
    return x.decode() if isinstance(x, bytes) else x


def pmap(fn, items, workers=8):
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(fn, items))


# ----------------------------------------------------------------------------- icephys
def recordings_table(h):
    """The intracellular recordings table, one row per sweep, with the response's slice."""
    ir = h["general/intracellular_ephys/intracellular_recordings"]
    cols = {}
    for k in ("cell_id", "site", "condition", "state", "drug", "stimulus_current_pA",
              "sweep_start_time", "protocol_run", "dendrite_type"):
        if k in ir:
            cols[k] = [_str(x) for x in ir[k][:]]
    df = pd.DataFrame(cols)
    resp = ir["responses/response"][:]
    df["r_start"] = resp["idx_start"]
    df["r_count"] = resp["count"]
    df["r_series"] = [h[ref].name for ref in resp["timeseries"]]
    return df


def _scaled(ds_group):
    d = ds_group["data"]
    conv = float(d.attrs.get("conversion", 1.0))
    off = float(d.attrs.get("offset", 0.0))
    return d, conv, off


def count_spikes(v_mV, threshold=0.0):
    """Upward crossings of the threshold over the sweep (the paper's count_events)."""
    above = v_mV > threshold
    return int(np.sum(above[1:] & ~above[:-1]) + (1 if above[0] else 0))


def somatic_file(asset, h=None):
    """Per sweep spike counts for every somatic current-step sweep of one file."""
    h = h if h is not None else open_h5(asset["asset_id"])
    t = recordings_table(h)
    t = t[t.site == "Soma"]
    t = t[t.r_series.str.contains("CurrentClampSeries")]
    rows = []
    for series, g in t.groupby("r_series"):
        d, conv, off = _scaled(h[series])
        v = d[:] * conv + off  # volts
        for _, r in g.iterrows():
            seg = v[r.r_start:r.r_start + r.r_count] * 1000.0
            rows.append(dict(path=asset["path"], date=asset["date"], cell_type=asset["cell_type"],
                             file_group=asset["group"], genotype=asset["genotype"],
                             cell=int(r.cell_id), condition=r.condition, drug=r.get("drug"),
                             step_pA=float(r.stimulus_current_pA), start=float(r.sweep_start_time),
                             n_spikes=count_spikes(seg), vmin=float(seg.min()), vmax=float(seg.max()),
                             n_samples=int(r.r_count)))
    return pd.DataFrame(rows)


def icephys_file(asset):
    """Somatic sweeps and dendritic pairs of one current-clamp file, opened once."""
    h = open_h5(asset["asset_id"])
    som = somatic_file(asset, h)
    den = dendritic_file(asset, h) if "ophys" in asset["kind"] else pd.DataFrame()
    return som, den


def per_cell_somatic(sweeps):
    """One row per cell and condition: first sweep of each step, rheobase, summed spikes 20-300 pA."""
    s = sweeps.sort_values("start")
    key = ["path", "cell", "condition"]
    first = s.drop_duplicates(key + ["step_pA"], keep="first")
    out = []
    for k, g in first.groupby(key):
        g = g.sort_values("step_pA")
        pos = g[(g.step_pA > 0) & (g.n_spikes >= 1)]
        rheo = float(pos.step_pA.min()) if len(pos) else np.nan
        fi = g[(g.step_pA >= 20) & (g.step_pA <= 300)]
        counts = dict(zip(fi.step_pA.astype(int), fi.n_spikes))
        n_rep = int(s[(s.path == k[0]) & (s.cell == k[1]) & (s.condition == k[2])].duplicated("step_pA").sum())
        out.append(dict(path=k[0], date=g.date.iloc[0], cell_type=g.cell_type.iloc[0],
                        file_group=g.file_group.iloc[0], genotype=g.genotype.iloc[0], cell=k[1],
                        condition=k[2], rheobase=rheo, fi_sum=int(fi.n_spikes.sum()),
                        n_steps_20_300=len(fi), repeated_sweeps=n_rep, counts=counts))
    return pd.DataFrame(out)


# ----------------------------------------------------------------------------- dendritic
BG_RED, BG_GREEN = 55.0, 161.0


def _site_trace(h, rows, col):
    """Average over trials of the background-subtracted, 6-sample smoothed ROI profile."""
    traces, dts = [], []
    for _, r in rows.iterrows():
        st, n, ser = r[col]
        if st < 0:
            continue
        g = h[ser]
        x = g["data"][st:st + n].astype(float).ravel()
        if "timestamps" in g:
            ts = g["timestamps"][st:st + n]
            dt = float(np.median(np.diff(ts)))
        else:
            dt = 1.0 / float(g["starting_time"].attrs["rate"])
        traces.append(x)
        dts.append(dt)
    if not traces:
        return None, None, 0
    n = min(len(x) for x in traces)
    bg = BG_RED if "Alexa" in col or "alexa" in col else BG_GREEN
    sm = [pd.Series(x[:n] - bg).rolling(6).mean().to_numpy() for x in traces]
    return np.nanmean(np.vstack(sm), axis=0) if len(sm) > 1 else sm[0], float(np.median(dts)), len(sm)


def _areas(red, green, dt):
    a, c, d = int(0.5 / dt), int(0.95 / dt), int(1.5 / dt)
    r0 = np.nanmean(red[a:c])
    g0 = np.nanmean(green[a:c])
    dgr = (green - g0) / r0
    e = int(2.5 / dt)
    late = np.nansum(dgr[e:e + (d - c)]) * dt  # same length, 1.55 s later: a clock check
    return np.nansum(dgr[c:d]) * dt, g0, r0, late


def dendritic_file(asset, h=None):
    """One row per proximal/distal pair: areas, basal ratio and index."""
    h = h if h is not None else open_h5(asset["asset_id"])
    t = recordings_table(h)
    idx = h["processing/icephys/RecordingsIndexTable"]
    red = idx["roi_response_alexa568"][:]
    grn = idx["roi_response_fluo4"][:]
    irt_row = idx["irt_row"][:]
    t = t.copy()
    t["red"] = None
    t["grn"] = None
    for i, row in enumerate(irt_row):
        t.at[t.index[row], "red"] = (int(red[i]["idx_start"]), int(red[i]["count"]),
                                     h[red[i]["timeseries"]].name if red[i]["idx_start"] >= 0 else None)
        t.at[t.index[row], "grn"] = (int(grn[i]["idx_start"]), int(grn[i]["count"]),
                                     h[grn[i]["timeseries"]].name if grn[i]["idx_start"] >= 0 else None)
    t = t[t.site.str.contains("Prox|Dist")]
    sites = {}
    for (cell, cond, site), g in t.groupby(["cell_id", "condition", "site"]):
        r, dt, ntr = _site_trace(h, g, "red")
        gr, _, _ = _site_trace(h, g, "grn")
        if r is None:
            continue
        area, g0, r0, late = _areas(r, gr, dt)
        m = re.match(r"(Proximal|Distal)(\d+)(.*)", site)
        sites[(int(cell), cond, site)] = dict(kind=m.group(1), num=int(m.group(2)), extra=m.group(3),
                                              area=area, late=late, g0=g0, r0=r0, n_trials=ntr, dt=dt)
    rows = []
    for (cell, cond, site), p in sites.items():
        if p["kind"] != "Proximal":
            continue
        for (cell2, cond2, site2), d in sites.items():
            if cell2 != cell or cond2 != cond or d["kind"] != "Distal" or d["num"] != p["num"]:
                continue
            rows.append(dict(path=asset["path"], date=asset["date"], cell_type=asset["cell_type"],
                             file_group=asset["group"], genotype=asset["genotype"], cell=cell,
                             condition=cond, proximal=site, distal=site2,
                             prox_area=p["area"], dist_area=d["area"],
                             prox_late=p["late"], dist_late=d["late"],
                             basal_ratio=(d["g0"] / d["r0"]) / (p["g0"] / p["r0"]),
                             index=d["area"] / p["area"], n_trials_prox=p["n_trials"],
                             n_trials_dist=d["n_trials"]))
    return pd.DataFrame(rows)


def per_cell_dendritic(pairs, lo=0.5, hi=2.0):
    keep = pairs[(pairs.basal_ratio >= lo) & (pairs.basal_ratio <= hi)]
    g = keep.groupby(["path", "date", "cell_type", "file_group", "genotype", "cell", "condition"])
    return g.agg(index=("index", "mean"), n_pairs=("index", "size")).reset_index()


# ----------------------------------------------------------------------------- Sr2+-oEPSC
def detect_events(i_pA, fs, flash_s, win=(0.040, 0.400), k=5.0, noise_from="raw"):
    """Inward events in one sweep; returns amplitudes (pA, positive) of events in the window."""
    n1 = max(1, int(round(0.001 * fs)))
    sm = np.convolve(i_pA, np.ones(n1) / n1, mode="same")
    src = sm if noise_from == "smoothed" else i_pA
    base = pd.Series(src).rolling(int(0.020 * fs), center=True, min_periods=1).median().to_numpy()
    a, b = int((flash_s + 0.5) * fs), int((flash_s + 0.9) * fs)
    resid = (src - base)[a:b]
    sd = 1.4826 * np.median(np.abs(resid - np.median(resid)))
    s0, s1 = int((flash_s + win[0]) * fs), int((flash_s + win[1]) * fs)
    seg = -sm[s0:s1]
    pk, pr = signal.find_peaks(seg, prominence=k * sd, wlen=int(0.020 * fs), distance=int(0.003 * fs))
    return pr["prominences"], sd


def sr_file(asset):
    h = open_h5(asset["asset_id"])
    t = recordings_table(h)
    t = t[t.r_series.str.contains("VoltageClampSeries")]
    if t.empty:
        return pd.DataFrame()
    flashes = h["intervals/optogenetic_pulses_table/start_time"][:]
    rows = []
    for series, g in t.groupby("r_series"):
        d, conv, off = _scaled(h[series])
        x = d[:] * conv + off  # amperes
        ts = h[series]["timestamps"][:] if "timestamps" in h[series] else None
        for _, r in g.iterrows():
            seg = x[r.r_start:r.r_start + r.r_count] * 1e12
            tt = ts[r.r_start:r.r_start + r.r_count]
            fs = 1.0 / float(np.median(np.diff(tt)))
            fl = flashes[(flashes >= tt[0]) & (flashes <= tt[-1])]
            flash_s = float(fl[0] - tt[0]) if len(fl) else np.nan
            if not len(fl):
                continue
            amps, sd = detect_events(seg, fs, flash_s)
            amps_s, _ = detect_events(seg, fs, flash_s, noise_from="smoothed")
            late, _ = detect_events(seg, fs, flash_s, win=(0.500, 0.860))
            rows.append(dict(path=asset["path"], date=asset["date"], cell_type=asset["cell_type"],
                             file_group=asset["group"], cell=int(r.cell_id), condition=r.condition,
                             sweep_start=float(r.sweep_start_time), fs=fs, flash_s=flash_s,
                             noise_sd=sd, n_events=len(amps), amps=list(amps),
                             n_events_smoothed_sd=len(amps_s), amps_smoothed_sd=list(amps_s),
                             n_events_late=len(late)))
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------- GRAB-ACh3.0
def _trials(h):
    tr = h["intervals/trials"]
    df = pd.DataFrame({k: [_str(x) for x in tr[k][:]] for k in
                       ("start_time", "stop_time", "region", "drug", "stimulation", "stimulus_start_time")})
    tp = tr["two_photon_grabach3"][:]
    rr = tr["roi_response_grabach3"][:]
    df["tp_start"], df["tp_count"] = tp["idx_start"], tp["count"]
    df["tp_series"] = [h[x].name for x in tp["timeseries"]]
    df["rr_start"], df["rr_count"] = rr["idx_start"], rr["count"]
    df["rr_series"] = [h[x].name for x in rr["timeseries"]]
    return df


def _circle_mask(ny, nx):
    yy, xx = np.mgrid[0:ny, 0:nx]
    cy, cx = (ny - 1) / 2, (nx - 1) / 2
    r = 50.0 / 0.388 / 2
    return (yy - cy) ** 2 + (xx - cx) ** 2 <= r ** 2


def grab_file(asset):
    """Per trial traces (circle ROI from the movie, and whole-frame brightness) of one file."""
    h = open_h5(asset["asset_id"])
    df = _trials(h)
    rows = []
    for _, r in df.iterrows():
        g = h[r.tp_series]
        ts = g["timestamps"][r.tp_start:r.tp_start + r.tp_count] if "timestamps" in g else None
        if ts is None:
            rate = float(g["starting_time"].attrs["rate"])
            ts = g["starting_time"][()] + np.arange(r.tp_start, r.tp_start + r.tp_count) / rate
        mov = g["data"][r.tp_start:r.tp_start + r.tp_count].astype(float)
        mask = _circle_mask(*mov.shape[1:])
        circ = mov[:, mask].mean(axis=1)
        whole = h[r.rr_series]["data"][r.rr_start:r.rr_start + r.rr_count].astype(float).ravel()
        rows.append(dict(path=asset["path"], date=asset["date"], group=asset["group"],
                         region=r.region, drug=r.drug, stimulation=r.stimulation,
                         start=float(r.start_time), stim=float(r.stimulus_start_time),
                         t=ts - float(r.start_time), circle=circ, whole=whole[:len(circ)],
                         n_frames=len(circ), frame_dt=float(np.median(np.diff(ts)))))
    return pd.DataFrame(rows)


def grab_areas(trials, roi="circle", stim="single 1 ms pulse", fmin_rule="smaller", max_trials=None):
    """Normalised area per region and drug, as in the paper's script.

    Fmax and Fmin average the calibration trials whose 2-4 s window holds frames (a trial
    shorter than 2 s has none). All trials of a condition are averaged; max_trials keeps the
    first ones (the paper averaged two)."""
    out = []
    for (path, region), g in trials.groupby(["path", "region"]):
        def window_mean(tr, a, b):
            m = (tr.t >= a) & (tr.t < b)
            return float(np.mean(tr[roi][m])) if m.any() else np.nan
        ach = g[g.drug.str.contains("acetylcholine")]
        ttx = g[g.drug.str.contains("tetrodotoxin")]
        fmax = np.nanmean([window_mean(r, 2, 4) for _, r in ach.iterrows()]) if len(ach) else np.nan
        f_ttx = np.nanmean([window_mean(r, 2, 4) for _, r in ttx.iterrows()]) if len(ttx) else np.nan
        res = {}
        for drug, d in g[g.stimulation == stim].groupby("drug"):
            d = d.sort_values("start")
            if max_trials:
                d = d.head(max_trials)
            # align the trials on the first frame at or after the stimulus; 1 s before, 2 s after
            dt = float(np.median(d.frame_dt))
            nb, na = int(round(1.0 / dt)), int(round(2.0 / dt))
            segs = []
            for _, r in d.iterrows():
                k0 = int(np.searchsorted(r.t, r.stim - r.start))
                segs.append(np.asarray(r[roi][k0 - nb:k0 + na], float))
            n = min(len(x) for x in segs)
            avg = np.mean([x[:n] for x in segs], axis=0)
            f0 = float(np.mean(avg[:nb]))
            res[drug] = dict(avg=avg, f0=f0, nb=nb, dt=dt, n_trials=len(d))
        quin_f0 = res["10 µM quinpirole"]["f0"] if "10 µM quinpirole" in res else np.nan
        if fmin_rule == "smaller":
            fmin = np.nanmin([f_ttx, quin_f0]) if not (np.isnan(f_ttx) and np.isnan(quin_f0)) else np.nan
        elif fmin_rule == "ttx":
            fmin = f_ttx
        else:
            fmin = quin_f0
        for drug, v in res.items():
            dfn = (v["avg"] - v["f0"]) / (fmax - fmin)
            out.append(dict(path=path, date=g.date.iloc[0], group=g.group.iloc[0], region=region,
                            drug=drug, auc=float(np.sum(dfn[v["nb"]:]) * v["dt"]), n_trials=v["n_trials"],
                            fmax=fmax, fmin=fmin, f_ttx=f_ttx, quin_f0=quin_f0))
    return pd.DataFrame(out)


# ----------------------------------------------------------------------------- AIMs
def aim_file(asset):
    h = open_h5(asset["asset_id"])
    desc = _str(h["session_description"][()])
    m = re.search(r"session (\d) of 5 of mouse (\d+) \(([^,]+), (Figure \d+)", desc)
    if "events/aim_scores" not in h:
        return pd.DataFrame()
    e = h["events/aim_scores"]
    d = pd.DataFrame(dict(behavior=[_str(x) for x in e["behavior"][:]], score=e["score"][:],
                          timestamp=e["timestamp"][:]))
    d["path"] = asset["path"]
    d["session"] = int(m.group(1)) if m else np.nan
    d["mouse"] = int(m.group(2)) if m else np.nan
    d["group_label"] = m.group(3) if m else None
    d["figure"] = m.group(4) if m else None
    d["genotype"] = asset["genotype"]
    return d


# ----------------------------------------------------------------------------- paper's tables
def paper_tables():
    """The paper's per-cell and per-mouse tables, read into memory from Zenodo."""
    url = f"https://zenodo.org/api/records/{TABLES_RECORD}/files/{TABLES_FILE}/content"
    z = zipfile.ZipFile(io.BytesIO(_get(url).content))
    out = {}
    for n in z.namelist():
        if n.endswith(".xlsx") and "__MACOSX" not in n and "~$" not in n:
            x = pd.ExcelFile(io.BytesIO(z.read(n)))
            for s in x.sheet_names:
                out[s] = pd.read_excel(x, sheet_name=s)
    return out


# ----------------------------------------------------------------------------- statistics
def mw(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    a, b = a[~np.isnan(a)], b[~np.isnan(b)]
    res = stats.mannwhitneyu(a, b, alternative="two-sided")
    return dict(n1=len(a), n2=len(b), median1=float(np.median(a)), median2=float(np.median(b)),
                U=float(res.statistic), p=float(res.pvalue))


def mixed_anova_group(df, subject, group, within, value):
    """Between-subject F of a mixed (split-plot) ANOVA with one within factor.

    With complete data the between-subject test equals a one-way ANOVA on subject means."""
    w = df.pivot_table(index=[subject, group], columns=within, values=value)
    w = w.dropna()
    means = w.mean(axis=1).reset_index()
    groups = [g[0].to_numpy() for _, g in means.groupby(group)]
    F, p = stats.f_oneway(*groups)
    return dict(F=float(F), p=float(p), df1=len(groups) - 1, df2=len(means) - len(groups),
                n=len(means), n_sessions=w.shape[1])
