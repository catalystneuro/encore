"""Loading and measures for dandiset 001538 (Zhai et al. 2025, Science Advances).

Every file is streamed from the DANDI archive with remfile and h5py; nothing is
written to disk. The parameters below say where they come from:

- [code-somatic] the paper's somatic script, "Input_output analysis ver2024.11"
  (doi:10.5281/zenodo.14145776): spikes are upward crossings of 0 mV over the
  whole sweep (count_events, threshold 0), and the rheobase is the first
  positive step that evokes a spike (rheobaseCal).
- [code-dendritic] the paper's dendritic script, "PVAnalysis ver 2024.11"
  (doi:10.5281/zenodo.14163502): line profiles minus PMT backgrounds of 55
  (red) and 161 (green), smoothed with a 6-sample running mean, the three
  trials of a site averaged, R0 and G0 the means from 0.5 to 0.95 s, the
  Ca2+ signal the sum of dG/R0 from 0.95 to 1.5 s times the sample interval,
  and the basal ratio (G0/R0 distal)/(G0/R0 proximal), "about 1".
- [methods-dendritic] Methods, "Imaging of spines and dendritic Ca2+
  transients": "Only data with similar baseline levels (G0/R0) for proximal and
  distal locations were included." The claims file fixes "similar" as a basal
  ratio between 0.5 and 2, pairs proximal and distal sites by their number and
  averages pairs within a cell.
- [code-grab] the paper's GRAB-ACh script, "PVAnalysis-BOT for GRAB Ver
  2024.11" (doi:10.5281/zenodo.14163731): F0 the mean over the 1 s before the
  stimulus, the AUC the sum of (F - F0)/(Fmax - Fmin) over the 2 s from the
  stimulus times the frame interval, the two trials of a condition averaged,
  Fmax and Fmin the means from 2 to 4 s of the acetylcholine and tetrodotoxin
  trials. [methods-grab] Methods, "Two-photon imaging of ACh sensor": Fmin is
  the TTX value "or from quinpirole-treated baselines, whichever was smaller",
  and the ROI is "a circle with a diameter of 50 um in the center of the
  imaging field". The PMT background the paper subtracts is not in the
  dandiset; it cancels in F - F0 and in Fmax - Fmin, so it does not change
  the normalised AUC.
- [methods-sr] Methods, "Data acquisition and statistical analysis": events
  "measured between 40 and 400 ms after photostimulation" and "greater than
  five SD above the noise". The paper used TaroTools in Igor Pro with visual
  verification; the detector here (detect_events) is a stand-in, and its
  filtering, noise estimate and event separation are assumptions (see its
  docstring). The frequency is the number of events over the 360 ms windows of
  all sweeps, which reproduces the paper's values such as 12.5 Hz (45 events in
  10 sweeps).
"""
import io
import json
import re
import urllib.error
import urllib.request
import zipfile

import h5py
import numpy as np
import pandas as pd
import remfile

DANDISET = "001538"
VERSION = "draft"
API = "https://api.dandiarchive.org/api"

# Outside inputs the claims file names (data: with_inputs and elsewhere claims).
TABLES_URL = ("https://zenodo.org/api/records/17307059/files/"
              "Zhai%20et%20al.%202025%20Datasets.zip/content")

RED_BG, GREEN_BG = 55.0, 161.0          # [code-dendritic]
SMOOTH = 6                              # [code-dendritic]
BASE_WIN = (0.5, 0.95)                  # [code-dendritic]
AUC_WIN = (0.95, 1.5)                   # [code-dendritic]
BASAL_RATIO_RANGE = (0.5, 2.0)          # claims file, from [methods-dendritic]
FI_STEPS = list(range(20, 301, 20))     # claims file: sum of spike counts 20 to 300 pA
SR_WIN = (0.040, 0.400)                 # [methods-sr], after the flash onset
SR_SD = 5.0                             # [methods-sr]
SR_LATE = (0.480, 0.840)                # clock check only, a standard choice
GRAB_F0 = 1.0                           # [code-grab], s before the stimulus
GRAB_AUC = 2.0                          # [code-grab], s from the stimulus
GRAB_FLIM = (2.0, 4.0)                  # [code-grab], s from the start of the ACh/TTX trial
GRAB_ROI_UM = 50.0                      # [methods-grab]


def _get(url):
    with urllib.request.urlopen(url) as r:
        return r.read()


def version_info():
    """The pinned version's metadata (name, modified time, asset count)."""
    return json.loads(_get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/info/"))


def list_assets():
    """All assets of the pinned version, as a DataFrame with the session fields parsed."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000"
    rows = []
    while url:
        page = json.loads(_get(url))
        rows += page["results"]
        url = page["next"]
    df = pd.DataFrame(rows)[["asset_id", "path", "size"]]
    df = df[df.path.str.endswith(".nwb")].copy()
    ses = df.path.str.extract(r"_ses-([^/]+)\.nwb$")[0]
    parts = ses.str.split("_", n=1, expand=True)
    fields = parts[0].str.split(r"\+\+", expand=True)
    df["cell_type"], df["state"], df["drug"], df["genotype"], df["date"] = (
        fields[0], fields[1], fields[2], fields[3], fields[4])
    df["kind"] = parts[1].fillna("")
    df["subject"] = df.path.str.split("/").str[0].str.replace("sub-", "", regex=False)
    return df.reset_index(drop=True)


def open_asset(asset_id):
    """Open an asset as an h5py file, streamed from S3."""
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *args, **kwargs):
            return None
    opener = urllib.request.build_opener(NoRedirect)
    try:
        opener.open(f"{API}/assets/{asset_id}/download/")
        raise RuntimeError(f"no redirect for asset {asset_id}")
    except urllib.error.HTTPError as e:
        if e.code not in (301, 302, 303, 307):
            raise
        s3 = e.headers["Location"]
    return h5py.File(remfile.File(s3), "r")


def _str(a):
    return np.array([x.decode() if isinstance(x, bytes) else x for x in a], dtype=object)


def count_spikes(v_mv, threshold=0.0):
    """Upward crossings of the threshold over the whole sweep [code-somatic]."""
    above = v_mv > threshold
    return int(np.sum(above[1:] & ~above[:-1]) + (1 if above[0] else 0))


def _series_values(f, ref_row, cache):
    """Data of one row of a TimeSeriesReference column, in the series' units."""
    start, count, ref = ref_row
    ds = f[ref]
    name = ds.name
    if name not in cache:
        data = ds["data"]
        values = data[:] * float(data.attrs.get("conversion", 1.0))
        if values.ndim == 2 and values.shape[1] == 1:
            values = values[:, 0]
        cache[name] = (values, _timestamps(ds))
    data, ts = cache[name]
    return data[start:start + count], ts[start:start + count]


def _timestamps(ds):
    if "timestamps" in ds:
        return ds["timestamps"][:]
    n = ds["data"].shape[0]
    st = ds["starting_time"]
    return st[()] + np.arange(n) / float(st.attrs["rate"])


def load_patch_file(asset):
    """Read one patch-clamp (current clamp) file.

    Returns (somatic, dendritic): one row per somatic sweep with its spike count,
    and one row per dendritic trial with its red and green profiles (arrays) and
    their time from the trial start.
    """
    f = open_asset(asset.asset_id)
    t = f["processing/icephys/RecordingsIndexTable"]
    irt = f["general/intracellular_ephys/intracellular_recordings"]
    resp = irt["responses/response"][:]
    stim = irt["stimuli/stimulus"][:]
    cols = {k: t[k][:] for k in ["cell_id", "dendrite_type", "site", "condition",
                                 "stimulus_current_pA", "sweep_start_time_s", "irt_row"]}
    for k in ["dendrite_type", "site", "condition"]:
        cols[k] = _str(cols[k])
    drug = _str(irt["drug"][:])
    cache = {}
    som, den = [], []
    has_roi = "roi_response_fluo4" in t
    red_col = t["roi_response_alexa568"][:] if has_roi else None
    grn_col = t["roi_response_fluo4"][:] if has_roi else None
    base = dict(path=asset.path, subject=asset.subject, date=asset.date,
                cell_type=asset.cell_type, file_state=asset.state)
    for i in range(len(cols["cell_id"])):
        row = dict(base, cell=int(cols["cell_id"][i]), condition=cols["condition"][i],
                   drug=drug[cols["irt_row"][i]], site=cols["site"][i],
                   current_pA=float(cols["stimulus_current_pA"][i]),
                   sweep_start=float(cols["sweep_start_time_s"][i]))
        if cols["dendrite_type"][i] == "Soma":
            v, ts = _series_values(f, resp[cols["irt_row"][i]], cache)
            row["n_samples"] = len(v)
            row["fs"] = 1.0 / float(np.median(np.diff(ts)))
            row["n_spikes"] = count_spikes(v * 1000.0)
            up = np.where((v[1:] > 0) & (v[:-1] <= 0))[0] + 1
            row["spike_times"] = ts[up] - ts[0]
            c, cts = _series_values(f, stim[cols["irt_row"][i]], cache)
            on = np.where(np.abs(c) > 0)[0]
            row["step_on"] = float(cts[on[0]] - ts[0]) if len(on) else np.nan
            row["step_off"] = float(cts[on[-1]] - ts[0]) if len(on) else np.nan
            row["v_min"], row["v_max"] = float(v.min() * 1000), float(v.max() * 1000)
            som.append(row)
        elif has_roi and grn_col[i][0] >= 0:
            g, ts = _series_values(f, grn_col[i], cache)
            r, _ = _series_values(f, red_col[i], cache)
            row["green"], row["red"], row["t"] = g, r, ts - ts[0]
            row["region"] = cols["dendrite_type"][i]
            row["t_offset"] = float(ts[0] - cols["sweep_start_time_s"][i])
            den.append(row)
    f.close()
    return pd.DataFrame(som), pd.DataFrame(den)


def cell_fi(somatic):
    """Per cell and condition: spikes per step, rheobase and the 20-300 pA sum.

    A step recorded twice keeps its first sweep; the count of such repeats is kept.
    The rheobase is the smallest positive step with a spike [code-somatic].
    """
    out = []
    keys = ["path", "subject", "date", "cell_type", "file_state", "cell", "condition", "drug"]
    for k, g in somatic.groupby(keys, sort=False):
        g = g.sort_values("sweep_start")
        first = g.drop_duplicates("current_pA", keep="first").set_index("current_pA")
        spikes = first.n_spikes
        pos = spikes[(spikes.index > 0) & (spikes > 0)]
        rec = dict(zip(keys, k))
        rec["rheobase"] = float(pos.index.min()) if len(pos) else np.nan
        steps = [s for s in FI_STEPS if s in spikes.index]
        rec["fi_sum"] = float(spikes.loc[steps].sum())
        rec["n_steps_20_300"] = len(steps)
        rec["n_repeated_steps"] = int(len(g) - len(first))
        for s in FI_STEPS:
            rec[f"s{s}"] = float(spikes.loc[s]) if s in spikes.index else np.nan
        out.append(rec)
    return pd.DataFrame(out)


def _smooth(x, n=SMOOTH):
    return pd.Series(x).rolling(n).mean().to_numpy()


def site_signal(trials):
    """Ca2+ signal of one dendritic site from its trials [code-dendritic].

    Returns (area dG/R0, G0, R0, n_trials). Trials are cut to the shortest one
    and averaged after background subtraction and smoothing.
    """
    n = min(len(x) for x in trials.green)
    if n < 10:
        return np.nan, np.nan, np.nan, 0
    t = trials.t.iloc[0][:n]
    g = np.mean([_smooth(x[:n] - GREEN_BG) for x in trials.green], axis=0)
    r = np.mean([_smooth(x[:n] - RED_BG) for x in trials.red], axis=0)
    dt = float(np.median(np.diff(t)))
    ia, ic, idd = int(BASE_WIN[0] / dt), int(BASE_WIN[1] / dt), int(AUC_WIN[1] / dt)
    r0, g0 = np.nanmean(r[ia:ic]), np.nanmean(g[ia:ic])
    area = np.nansum((g[ic:idd] - g0) / r0) * dt
    return float(area), float(g0), float(r0), len(trials)


def _site_key(site):
    """'Proximal1Spot2' -> ('Proximal', 1, 'Spot2')."""
    m = re.match(r"(Proximal|Distal)(\d+)(Spot\d)?", site)
    return m.group(1), int(m.group(2)), m.group(3) or ""


def dendritic_index(dendritic, basal_range=BASAL_RATIO_RANGE, pairing="number"):
    """Per cell and condition: the dendritic excitability index.

    Sites imaged at two spots keep the second ('Spot2', which the lab marked
    'real'). Proximal and distal sites are paired by number (pairing='number',
    the claims file) or every proximal with every distal site
    (pairing='all', a variant); pairs with a basal ratio outside basal_range are
    dropped, and the remaining distal/proximal ratios averaged within the cell.
    Returns (cells, pairs).
    """
    keys = ["path", "subject", "date", "cell_type", "file_state", "cell", "condition", "drug"]
    sites = []
    for k, g in dendritic.groupby(keys + ["site"], sort=False):
        area, g0, r0, n = site_signal(g)
        region, num, spot = _site_key(k[-1])
        sites.append(dict(zip(keys, k[:-1]), site=k[-1], region=region, num=num, spot=spot,
                          area=area, g0r0=g0 / r0 if r0 else np.nan, n_trials=n))
    sites = pd.DataFrame(sites)
    pairs = []
    for k, g in sites.groupby(keys, sort=False):
        g = g[(g.spot == "") | (g.spot == "Spot2") |
              ~g.duplicated(["region", "num"], keep=False)]
        prox = g[g.region == "Proximal"]
        dist = g[g.region == "Distal"]
        for _, d in dist.iterrows():
            cands = prox[prox.num == d.num] if pairing == "number" else prox
            for _, p in cands.iterrows():
                pairs.append(dict(zip(keys, k), prox=p.site, dist=d.site,
                                  ratio=d.area / p.area, basal=d.g0r0 / p.g0r0,
                                  prox_area=p.area, dist_area=d.area))
    pairs = pd.DataFrame(pairs)
    if pairs.empty:
        return pd.DataFrame(), pairs, sites
    pairs["kept"] = pairs.basal.between(*basal_range)
    cells = (pairs[pairs.kept].groupby(keys, sort=False)
             .agg(index=("ratio", "mean"), n_pairs=("ratio", "size")).reset_index())
    return cells, pairs, sites


# ---------------------------------------------------------------- Sr2+-oEPSCs

def smooth_sweep(i_pa, fs, smooth_ms=1.0):
    """1 ms running mean of a current sweep (an assumption, see detect_events)."""
    k = max(1, int(round(smooth_ms * 1e-3 * fs)))
    return np.convolve(i_pa, np.ones(k) / k, mode="same")


def baseline_sd(x, fs, flash_t):
    """SD of the smoothed current from 2 ms after the sweep start to 1 ms before the flash."""
    return float(np.std(x[int(0.002 * fs):int((flash_t - 0.001) * fs)]))


def detect_events(x, fs, flash_t, sd, n_sd=SR_SD, win=SR_WIN, min_sep_ms=3.0, base_ms=2.0):
    """Asynchronous EPSCs in one smoothed voltage-clamp sweep [methods-sr], a stand-in for TaroTools.

    Assumptions (the paper does not give them): the sweep is smoothed with a 1 ms
    running mean (smooth_sweep); the noise SD is the cell's median, over its
    sweeps, of the SD of the smoothed current before the flash (baseline_sd);
    an event is a local minimum of the smoothed current more than n_sd noise SDs
    below the local baseline (the mean over base_ms ending 1 ms before the
    point where the threshold is crossed), with peaks at least min_sep_ms
    apart; its amplitude is the local baseline minus the minimum, in pA.
    Events whose threshold crossing falls between 40 and 400 ms after the
    flash onset are kept. Returns an array of amplitudes (pA, positive for inward currents).
    """
    a, b = int((flash_t + win[0]) * fs), int((flash_t + win[1]) * fs)
    nb, lag, sep = int(base_ms * 1e-3 * fs), int(1e-3 * fs), int(min_sep_ms * 1e-3 * fs)
    amps = []
    i = a
    while i < b:
        base = x[max(0, i - lag - nb):i - lag].mean()
        if base - x[i] > n_sd * sd:
            j = i
            while j + 1 < len(x) and x[j + 1] <= x[j]:
                j += 1
            amps.append(base - x[j])
            i = j + sep
        else:
            i += 1
    return np.array(amps)


def load_sr_file(asset, n_sd_list=(SR_SD,)):
    """Sweeps of an Sr2+-oEPSC file, with the events found at each threshold in n_sd_list.

    Returns one row per cell: the number of sweeps, the noise SD, and for each
    threshold the event amplitudes, their count, mean and median, and the frequency.
    """
    f = open_asset(asset.asset_id)
    irt = f["general/intracellular_ephys/intracellular_recordings"]
    resp = irt["responses/response"][:]
    cell = irt["cell_id"][:]
    cond = _str(irt["condition"][:])
    pulses = f["intervals/optogenetic_pulses_table"]
    p_start, p_cell = pulses["start_time"][:], pulses["cell_id"][:]
    cache, sweeps = {}, {}
    for i in range(len(resp)):
        v, ts = _series_values(f, resp[i], cache)
        fs = 1.0 / float(np.median(np.diff(ts)))
        mine = p_start[(p_cell == cell[i]) & (p_start >= ts[0]) & (p_start <= ts[-1])]
        if len(mine) == 0:
            continue
        x = smooth_sweep(v * 1e12, fs)
        sweeps.setdefault((int(cell[i]), cond[i]), []).append((x, fs, float(mine[0] - ts[0])))
    f.close()
    rows = []
    for (c, cnd), sw in sweeps.items():
        sd = float(np.median([baseline_sd(x, fs, ft) for x, fs, ft in sw]))
        r = dict(path=asset.path, subject=asset.subject, date=asset.date,
                 cell_type=asset.cell_type, cell=c, condition=cnd, n_sweeps=len(sw),
                 noise_sd=sd, fs=sw[0][1], flash_t=float(np.median([s[2] for s in sw])))
        for n_sd in n_sd_list:
            amps = np.concatenate([detect_events(x, fs, ft, sd, n_sd=n_sd) for x, fs, ft in sw])
            r[f"amps_{n_sd:g}"] = amps
            r[f"n_events_{n_sd:g}"] = len(amps)
            r[f"mean_amp_{n_sd:g}"] = float(np.mean(amps)) if len(amps) else np.nan
            r[f"median_amp_{n_sd:g}"] = float(np.median(amps)) if len(amps) else np.nan
            r[f"freq_{n_sd:g}"] = len(amps) / (len(sw) * (SR_WIN[1] - SR_WIN[0]))
        # Clock check: the same detector over a 360 ms window late in the sweep,
        # 480 to 840 ms after the flash, before the test step at 920 ms.
        late = np.concatenate([detect_events(x, fs, ft, sd, win=SR_LATE) for x, fs, ft in sw])
        r["n_events_late"] = len(late)
        rows.append(r)
    return pd.DataFrame(rows)


# ---------------------------------------------------------------- GRAB-ACh3.0

def _circle_mask(shape, spacing_um, diam_um=GRAB_ROI_UM):
    ny, nx = shape
    yy, xx = np.mgrid[:ny, :nx]
    r = diam_um / 2.0
    return ((yy - (ny - 1) / 2) * spacing_um[0]) ** 2 + ((xx - (nx - 1) / 2) * spacing_um[1]) ** 2 <= r ** 2


def load_grab_file(asset):
    """Per trial of a GRAB-ACh3.0 file: the 50 um circle trace and the whole-frame botData trace."""
    f = open_asset(asset.asset_id)
    tr = f["intervals/trials"]
    n = len(tr["id"][:])
    col = {k: tr[k][:] for k in ["start_time", "stop_time", "stimulus_start_time"]}
    for k in ["region", "drug", "stimulation"]:
        col[k] = _str(tr[k][:])
    mov = tr["two_photon_grabach3"][:]
    bot = tr["roi_response_grabach3"][:]
    rows = []
    masks = {}
    for i in range(n):
        start, count, ref = mov[i]
        ds = f[ref]
        if ds.name not in masks:
            plane = ds["imaging_plane"]
            sp = plane["grid_spacing"][:] if "grid_spacing" in plane else np.array([0.388, 0.388])
            masks[ds.name] = (_circle_mask(ds["data"].shape[1:], sp), sp)
        mask, sp = masks[ds.name]
        frames = ds["data"][start:start + count].astype(float)
        trace = frames[:, mask].mean(axis=1)
        ts = _timestamps(ds)[start:start + count]
        b, _ = _series_values(f, bot[i], {})
        rows.append(dict(path=asset.path, subject=asset.subject, date=asset.date,
                         state=asset.state, region=col["region"][i], drug=col["drug"][i],
                         stimulation=col["stimulation"][i], start=col["start_time"][i],
                         stim=col["stimulus_start_time"][i], t=ts, circle=trace, whole=b,
                         spacing=float(sp[0]), mask_px=int(mask.sum())))
    f.close()
    return pd.DataFrame(rows)


def grab_auc(trials, signal="circle", fmin_rule="min"):
    """Normalised single-pulse AUC per region and drug [code-grab, methods-grab].

    fmin_rule: 'min' (TTX or the quinpirole baseline, whichever is smaller,
    the Methods), 'ttx' (TTX only, as the script), 'quin' (quinpirole baseline only).
    Returns one row per region and drug, with Fmax, Fmin and the number of trials averaged.
    """
    out = []
    for (path, region), g in trials.groupby(["path", "region"], sort=False):
        def plateau(drug):
            h = g[g.drug.str.contains(drug)]
            if h.empty:
                return np.nan
            vals = []
            for _, r in h.iterrows():
                tt = r.t - r.start
                sel = (tt >= GRAB_FLIM[0]) & (tt < GRAB_FLIM[1])
                vals.append(np.mean(r[signal][sel]))
            return float(np.mean(vals))
        fmax = plateau("acetylcholine")
        fttx = plateau("tetrodotoxin")
        fmax_from = "region"
        if np.isnan(fmax):
            # No acetylcholine trial at this region: use the other regions of the
            # same slice (an assumption; the paper does not say).
            sl = region.split("Roi")[0]
            others = trials[(trials.path == path) & (trials.region.str.startswith(sl + "Roi")) &
                            (trials.region != region) & trials.drug.str.contains("acetylcholine")]
            vals = [np.mean(r[signal][((r.t - r.start) >= GRAB_FLIM[0]) & ((r.t - r.start) < GRAB_FLIM[1])])
                    for _, r in others.iterrows()]
            fmax = float(np.mean(vals)) if vals else np.nan
            fmax_from = "same slice" if vals else "none"
        single = g[g.stimulation.str.startswith("single")]
        quin = single[single.drug.str.contains("quinpirole")]
        fq = np.nan
        if len(quin):
            fq = float(np.mean([np.mean(r[signal][(r.t >= r.stim - GRAB_F0) & (r.t < r.stim)])
                                for _, r in quin.iterrows()]))
        fmin = {"min": np.nanmin([fttx, fq]) if not (np.isnan(fttx) and np.isnan(fq)) else np.nan,
                "ttx": fttx, "quin": fq}[fmin_rule]
        for drug, h in single[~single.drug.str.contains("tetrodotoxin")].groupby("drug", sort=False):
            aucs = []
            for _, r in h.iterrows():
                x, t = r[signal], r.t
                dt = float(np.median(np.diff(t)))
                f0 = np.mean(x[(t >= r.stim - GRAB_F0) & (t < r.stim)])
                sel = (t >= r.stim) & (t < r.stim + GRAB_AUC)
                aucs.append(np.sum(x[sel] - f0) * dt)
            out.append(dict(path=path, subject=g.subject.iloc[0], state=g.state.iloc[0],
                            region=region, drug=drug, n_trials=len(h), fmax=fmax, fmax_from=fmax_from, fttx=fttx,
                            fquin=fq, fmin=fmin, raw_auc=float(np.mean(aucs)),
                            auc=float(np.mean(aucs)) / (fmax - fmin)))
    return pd.DataFrame(out)


# ---------------------------------------------------------------- AIM scores

def load_aim_file(asset):
    """AIM scores of one session file: one row per time point and category."""
    f = open_asset(asset.asset_id)
    g = f["events/aim_scores"]
    df = pd.DataFrame(dict(time=g["timestamp"][:], behavior=_str(g["behavior"][:]),
                           score=g["score"][:]))
    desc = f["session_description"][()]
    desc = desc.decode() if isinstance(desc, bytes) else desc
    sd = f["general/subject/description"][()]
    sd = sd.decode() if isinstance(sd, bytes) else sd
    f.close()
    m = re.search(r"session (\d) of (\d) of mouse (\d+) \(([^,]+), Figure (\d+)\)", desc)
    df["session"] = int(m.group(1)) if m else np.nan
    df["mouse"] = int(m.group(3)) if m else np.nan
    df["group"] = m.group(4) if m else ""
    df["figure"] = int(m.group(5)) if m else np.nan
    df["path"], df["subject"], df["genotype"] = asset.path, asset.subject, asset.genotype
    df["subject_description"] = sd
    return df


# ---------------------------------------------------------------- paper tables

def paper_tables():
    """The paper's per-cell and per-mouse tables (Zenodo doi:10.5281/zenodo.17307059), read in memory."""
    z = zipfile.ZipFile(io.BytesIO(_get(TABLES_URL)))
    out = {}
    for name in z.namelist():
        if name.endswith(".xlsx") and "__MACOSX" not in name and "~$" not in name:
            key = name.split("/")[-1].replace(" datasets.xlsx", "")
            out[key] = pd.read_excel(io.BytesIO(z.read(name)), sheet_name=None)
    return out
