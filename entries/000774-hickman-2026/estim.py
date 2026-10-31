"""Loading and measures for dandiset 000774 (Hickman et al. 2026, Cell Reports 45, 117420).

The dandiset holds one NWB file per acute recording: spike times and Kilosort templates of the
units of three Neuropixels probes, with the CCF coordinates and region of each unit, and a trials
table of single electrical pulses (amplitude, polarity, pulse width, contacts and their CCF
coordinates). Files are streamed from the DANDI API at the pinned version; nothing is written to
disk.

Where each parameter comes from:

- The nine recordings of the paper are the nine sessions the paper's code loads
  (github.com/denmanlab/estim_populations at c4aaa608, figure4_figure5_figure6.ipynb cell 1);
  jlh41 is the tenth file of the dandiset and is left out (claims file header: 9 recordings,
  25 probes, probe A n = 7).
- Conditions (claims file header, "Method choices common to the claims on units"): single
  pulses (pulse_number 1) of 100 us per phase. In the files, "cathodal" is polarity
  "monopolar" with a negative amplitude, "anodal" monopolar with a positive amplitude, and
  "bipolar" bipolar with a negative amplitude (STAR Methods, Electrophysiological recordings:
  "Negative amplitudes indicate cathodal-leading pulses"). The trials are chosen as the code's
  choose_stim_parameter does: when the matching trials use more than one contact pair, those of
  the first cathodal contact in time; then the first 75 (claims file header).
- Units: Kilosort/phy group "good" and stable (claims file header). Stability follows the STAR
  Methods ("Single unit stability metric"): 60 s bins over the session, ordinary least squares
  of rate on time, y-intercept over mean rate, units beyond 1.5 IQR of the recording's quartiles
  removed. The time origin of the fit (the first bin, which starts at the first spike of the
  recording, as the code's bin_spikes in figure4_figure5_figure6.ipynb cell 7) and the set of
  units the quartiles are taken over (all units of the recording) are not stated in the paper;
  both are a standard choice and stated as such.
- Direct response probability (STAR Methods, "Calculating direct response probability"): the
  fraction of trials with a spike in [t, t + 2 ms]; nDRP subtracts the fraction for the 2 ms
  baseline (t - 7 ms, t - 5 ms] (claims file header, from figure4_figure5_figure6.ipynb cell 7).
  A unit with no spike between the first and last pulse of the condition has no value (code).
  Responder: nDRP > 0.15 (Methods).
- Distance from stimulation (claims file header, code Analysis.get_dists): Euclidean CCF
  distance from the unit to the cathodal contact of the recording's first trial. The dataset
  gives each unit's CCF coordinates (of its peak channel) and each trial's contact coordinates;
  those are used. The signed distance (the code's norm_distance) needs the CCF coordinates of
  every channel, which the dataset does not give (its electrodes table holds placeholders); the
  channel coordinates are reconstructed by a straight-line fit of the units' coordinates on
  their channel number, per probe (an assumption: the probes are straight shanks), the probe's
  minimum distance is subtracted, and channels at or above the closest one (toward the pia) are
  made negative, as in the code (figure4_figure5_figure6.ipynb cell 7).
- FS and RS classes: the waveform features of the code's classifier
  (github.com/denmanlab/dlab, utils.classify_waveform_shape and generalephys, at eaa5faa) on
  the peak-channel template. Two readings: "kmeans", the Methods' k-means (2 clusters on
  min-max normalised duration, peak-to-trough ratio and repolarisation slope, as dlab's k-means
  branch); "threshold", what the paper's code runs (kmeans=0: FS when duration < 0.4 ms).
  Units with peak-to-trough ratio >= 1 are "up", and narrow up units "axon" (Methods).
- Regions: cortical when the CCF name contains "area" (code classify_region,
  figure7.ipynb cell 29), with the code's curated subcortical list; the code's
  map_region_to_group (figure7.ipynb cell 5) for the circuit responders.
"""

import numpy as np
import pandas as pd
import requests
import h5py
import remfile
from scipy.signal import resample
from scipy.stats import linregress
from scipy.cluster.vq import kmeans2

DANDISET = "000774"
VERSION = "0.260520.1753"
API = "https://api.dandiarchive.org/api"

# the nine recordings the paper's code loads, in its order (figure4_figure5_figure6.ipynb cell 1)
PAPER_SESSIONS = ["jlh31", "jlh32", "jlh33", "jlh34", "jlh39", "jlh40", "jlh48", "jlh49v1",
                  "jlh53concat"]

AMPS = [5, 25, 50, 100]
POLARITIES = ["cathodal", "anodal", "bipolar"]

# code, figure7.ipynb cell 29
SUBCORTICAL = [
    "Postsubiculum", "dorsal hippocampal commissure",
    "Dentate gyrus molecular layer", "Dentate gyrus granule cell layer",
    "alveus", "Superior colliculus, motor related, intermediate gray layer",
    "Superior colliculus, motor related, intermediate white layer",
    "Hippocampal formation", "Midbrain", "brachium of the superior colliculus",
    "Field CA3", "Field CA2",
]


def list_assets():
    """Assets of the pinned version: list of dicts with path, asset_id, size, session."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=100"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        for a in r["results"]:
            ses = a["path"].split("_ses-")[1].split("-")[0]
            out.append(dict(path=a["path"], asset_id=a["asset_id"], size=a["size"], session=ses))
        url = r.get("next")
    return sorted(out, key=lambda a: a["path"])


def open_asset(asset_id):
    url = f"{API}/assets/{asset_id}/download/"
    return h5py.File(remfile.File(url), "r")


def _str(arr):
    return np.array([x.decode() if isinstance(x, bytes) else str(x) for x in arr])


def peak_waveform(template):
    """The channel of largest absolute value (dlab utils.get_peak_waveform_from_template)."""
    i = np.argmax(np.max(np.abs(template), axis=0))
    return template[:, i]


def waveform_features(w, fs=30000.0):
    """Duration (s), peak-to-trough ratio and repolarisation slope, as dlab generalephys."""
    r = resample(w, 200)
    time = np.linspace(0, len(w) / fs, 200)
    peak = int(np.argmax(r))
    trough = int(np.argmin(r))
    if r[peak] > abs(r[trough]):
        dur = time[peak:][np.argmin(r[peak:])] - time[peak]
    else:
        dur = time[trough:][np.argmax(r[trough:])] - time[trough]
    ratio = r[peak] / abs(r[trough])
    ratio = 1.0 if ratio > 1 else (ratio if np.isfinite(ratio) else 0.0)
    slope = linregress(time[trough:trough + 18], r[trough:trough + 18])[0] \
        if len(r[trough:trough + 18]) > 1 else np.nan
    return dur, ratio, slope


def classify_waveforms(dur, ratio, slope, rng_seed=0):
    """FS/RS/up/axon labels under the two readings (see the module docstring)."""
    dur, ratio, slope = map(np.asarray, (dur, ratio, slope))
    out = {}
    feats = []
    for v in (dur, ratio, np.nan_to_num(slope)):
        v0 = v - np.min(v)
        feats.append(v0 / np.max(v0))
    X = np.vstack(feats).T
    np.random.seed(rng_seed)  # kmeans2 with minit='points' draws from numpy's global generator
    _, lab = kmeans2(X, 2, iter=300, thresh=5e-6, minit="points", seed=rng_seed)
    fs_k = 0 if dur[lab == 0].mean() < dur[lab == 1].mean() else 1
    km = np.where(lab == fs_k, "fs", "rs")
    th = np.where(dur < 0.0004, "fs", "rs")
    for name, cls in [("kmeans", km), ("threshold", th)]:
        c = np.where(ratio < 1.0, cls, "up").astype(object)
        c[(c == "up") & (dur < 0.0004)] = "axon"
        out[name] = c
    return out


def stability_outliers(spike_trains, bin_size=60.0):
    """Unstable units of one recording (STAR Methods, Single unit stability metric)."""
    allsp = np.concatenate([s for s in spike_trains if len(s)])
    t0, t1 = allsp.min(), allsp.max()
    bins = np.arange(t0, t1 + bin_size, bin_size)
    x = (bins[:-1] - t0)[:, None]
    ratios = np.full(len(spike_trains), np.nan)
    X = np.hstack([np.ones_like(x), x])
    for i, s in enumerate(spike_trains):
        rate = np.histogram(s, bins)[0] / bin_size
        if rate.mean() <= 0:
            continue
        coef = np.linalg.lstsq(X, rate, rcond=None)[0]
        ratios[i] = coef[0] / rate.mean()
    q1, q3 = np.nanpercentile(ratios, [25, 75])
    iqr = q3 - q1
    out = (ratios < q1 - 1.5 * iqr) | (ratios > q3 + 1.5 * iqr) | ~np.isfinite(ratios)
    return out, ratios


def load_session(asset):
    """Units (DataFrame), spike trains (list) and trials (DataFrame) of one file."""
    f = open_asset(asset["asset_id"])
    u = f["units"]
    n = len(u["id"])
    idx = u["spike_times_index"][:]
    st = u["spike_times"][:]
    starts = np.concatenate([[0], idx[:-1]])
    trains = [np.sort(st[a:b]) for a, b in zip(starts, idx)]
    probe = np.array([p[-1] for p in _str(u["probe"][:])])
    units = pd.DataFrame(dict(
        session=asset["session"], unit=np.arange(n), probe=probe, ch=u["ch"][:],
        group=_str(u["group"][:]), KSlabel=_str(u["KSlabel"][:]),
        n_spikes=np.array([len(t) for t in trains]),
    ))
    if "ccf_coordinates" in u:
        cc = u["ccf_coordinates"][:]
        units["ap"], units["dv"], units["ml"] = cc[:, 0], cc[:, 1], cc[:, 2]
        units["region"] = _str(u["brain_reg"][:])
    T = u["template"][:]
    feats = np.array([waveform_features(peak_waveform(T[i])) for i in range(n)])
    units["wf_duration"], units["wf_ptratio"], units["wf_slope"] = feats.T
    cls = classify_waveforms(*feats.T)
    units["wf_kmeans"], units["wf_threshold"] = cls["kmeans"], cls["threshold"]
    unstable, ratio = stability_outliers(trains)
    units["unstable"], units["stability_ratio"] = unstable, ratio
    t = f["intervals/trials"]
    cols = {k: t[k][:] for k in t.keys() if k not in ("id",) and t[k].ndim == 1}
    trials = pd.DataFrame({k: (_str(v) if v.dtype.kind in "OS" else v) for k, v in cols.items()})
    if "contact_negative_coords" in t:
        trials[["neg_ap", "neg_dv", "neg_ml"]] = t["contact_negative_coords"][:]
    trials = trials.sort_values("start_time").reset_index(drop=True)
    meta = dict(session_id=f["general/session_id"][()].decode(),
                subject=f["general/subject/subject_id"][()].decode(),
                description=f["general/subject/description"][()].decode())
    f.close()
    return units, trials_label(trials), trains, meta


def trials_label(trials):
    pol = np.where(trials.polarity == "bipolar", "bipolar",
                   np.where(trials.amplitude < 0, "cathodal", "anodal"))
    trials["pol"] = pol
    trials["amp"] = trials.amplitude.abs()
    return trials


def condition_trials(trials, pol, amp, n=75, pulse_duration=100, contact=None):
    """Trials of a condition, chosen as the code's choose_stim_parameter, the first n.
    contact: a cathodal contact to use in place of the first one (the layer 5 reading)."""
    sub = trials[(trials.pol == pol) & (trials.amp == amp) & (trials.pulse_number == 1)
                 & (trials.pulse_duration == pulse_duration)]
    if len(sub) == 0:
        return sub
    if contact is not None and (sub.contact_negative == contact).any():
        sub = sub[sub.contact_negative == contact]
    elif sub.contact_positive.nunique() > 1:
        sub = sub[sub.contact_negative == sub.contact_negative.iloc[0]]
    return sub.iloc[:n] if n else sub


def contact_regions(units, trials):
    """For each cathodal contact, the region of the nearest unit and its distance (um): the
    dataset gives no region for the contacts."""
    out = {}
    xyz = units[["ap", "dv", "ml"]].to_numpy()
    for c in trials.contact_negative.unique():
        p = trials.loc[trials.contact_negative == c, ["neg_ap", "neg_dv", "neg_ml"]].iloc[0]
        d = np.linalg.norm(xyz - p.to_numpy(), axis=1)
        out[int(c)] = (units.region.iloc[int(np.argmin(d))], float(d.min()))
    return out


def signed_distances(units, contact):
    """Distance to the contact and the code's norm_distance (see the module docstring)."""
    xyz = units[["ap", "dv", "ml"]].to_numpy()
    dist = np.linalg.norm(xyz - contact, axis=1)
    norm = np.full(len(units), np.nan)
    for p in units.probe.unique():
        m = (units.probe == p).to_numpy()
        ch = units.ch.to_numpy()[m]
        if len(np.unique(ch)) < 2:
            continue
        chans = np.arange(0, 384)
        line = np.column_stack([np.polyval(np.polyfit(ch, xyz[m, k], 1), chans) for k in range(3)])
        d = np.linalg.norm(line - contact, axis=1)
        cross = int(np.argmin(d))
        dmin = d[cross]
        nd = dist[m] - dmin
        nd = np.where(ch >= cross, -np.abs(nd), nd)
        norm[m] = nd
    return dist, norm


CODE_REPO = ("https://raw.githubusercontent.com/denmanlab/estim_populations/"
             "c4aaa608314c8e8e91aee422baa69cd1b443a682/recordings")
CODE_FOLDERS = {"jlh31": "jlh31_2023-01-24_14-30-23", "jlh32": "jlh32_2023-02-18_16-07-58",
                "jlh33": "jlh33_2023-02-22_15-24-35", "jlh34": "jlh34_2023-05-15_16-03-21",
                "jlh39": "jlh39_2023-08-16_11-52-30", "jlh40": "jlh40_2023-08-21_16-01-34",
                "jlh48": "jlh48_2024-11-05_13-08-08", "jlh49v1": "jlh49v1_2024-07-11_16-18-42",
                "jlh53concat": "jlh53concat_2024-09-03_16-08-54"}
# contact order of the code's stimulation coordinates (figure4_figure5_figure6.ipynb cell 1)
NN_CONTACTS = [6, 11, 3, 14, 1, 16, 2, 15, 5, 12, 4, 13, 7, 10, 8, 9]


def code_coords(session):
    """Per-channel CCF coordinates of each probe and of the 16 contacts, from the paper's code
    repository at commit c4aaa608 (final_coords/probe_coords_adj.pkl). An outside input, used
    only to check the dataset's coordinates and as a variant of the distances."""
    import pickle
    url = f"{CODE_REPO}/{CODE_FOLDERS[session]}/final_coords/probe_coords_adj.pkl"
    raw = requests.get(url, timeout=60).content
    return {k: np.asarray(v, float) for k, v in pickle.loads(raw).items()}


def code_distances(units, coords, contact_label):
    """Distance and norm_distance as the paper's code computes them (cell 7 of
    figure4_figure5_figure6.ipynb), from the code's channel and contact coordinates."""
    stim = coords["stim"][NN_CONTACTS.index(int(contact_label))]
    dist = np.full(len(units), np.nan)
    norm = np.full(len(units), np.nan)
    for p in units.probe.unique():
        key = "probe" + p
        if key not in coords:
            continue
        d = np.linalg.norm(coords[key] - stim, axis=1)
        nd = d - d.min()
        cross = int(np.where(nd == 0)[0][0])
        nd[cross:] = -np.abs(nd[cross:])
        m = (units.probe == p).to_numpy()
        ch = np.minimum(units.ch.to_numpy()[m], len(d) - 1)
        dist[m] = d[ch]
        norm[m] = nd[ch]
    return dist, norm


def spike_prob(train, stims, win=0.002, base=(0.007, 0.005)):
    """DRP, baseline probability and nDRP (base = (start, end) before onset, in s)."""
    stims = np.asarray(stims)
    if np.sum((train >= stims[0]) & (train <= stims[-1])) == 0:
        return np.nan, np.nan, np.nan
    i0 = np.searchsorted(train, stims, side="left")
    i1 = np.searchsorted(train, stims + win, side="right")
    p = np.mean(i1 > i0)
    b0 = np.searchsorted(train, stims - base[0], side="right")
    b1 = np.searchsorted(train, stims - base[1], side="right")
    pb = np.mean(b1 > b0)
    return p, pb, p - pb


def first_latencies(train, stims, maxlat=0.5):
    """First spike latency (ms) after each pulse, within maxlat s."""
    i = np.searchsorted(train, stims, side="right")
    ok = i < len(train)
    lat = np.full(len(stims), np.nan)
    lat[ok] = train[i[ok]] - stims[ok]
    lat[lat > maxlat] = np.nan
    return lat[np.isfinite(lat)] * 1000


def counts_matrix(train, stims, edges):
    """Spike counts per trial and bin, edges relative to onset (s)."""
    out = np.zeros((len(stims), len(edges) - 1))
    for j, s in enumerate(stims):
        a, b = np.searchsorted(train, [s + edges[0], s + edges[-1]])
        out[j] = np.histogram(train[a:b] - s, edges)[0]
    return out


def mean_counts(train, stims, edges):
    """Trial-mean spike counts per bin, edges relative to onset (s)."""
    a = np.searchsorted(train, stims + edges[0])
    b = np.searchsorted(train, stims + edges[-1], side="right")
    rel = np.concatenate([train[i:j] - s for i, j, s in zip(a, b, stims)]) if len(stims) else []
    return np.histogram(rel, edges)[0] / max(len(stims), 1)


def modulation_index(train, stims, start, stop, bin_size):
    """MI per bin (code figure7.ipynb cells 11 and 28): trial-mean rate in [start, stop) after
    onset against the median rate from 1 s to 0.5 s before onset, same bin size."""
    nb = int(round((stop - start) / bin_size))
    resp = mean_counts(train, stims, start + np.arange(nb + 1) * bin_size) / bin_size
    nbb = int(round(0.5 / bin_size))
    base = np.median(mean_counts(train, stims, -1.0 + np.arange(nbb + 1) * bin_size)) / bin_size
    return (resp - base) / (resp + base + np.finfo(float).eps)


def classify_region(region):
    """Code figure7.ipynb cell 29."""
    if "area" in region:
        return "Cortical"
    if region in SUBCORTICAL:
        return "Subcortical"
    return None


def map_region_to_group(region):
    """Code figure7.ipynb cell 5, as written (its 'posteromedial area' matches no CCF name)."""
    if "Primary visual area" in region:
        return "Primary Visual Area"
    for k in ["Anterior area", "Lateral visual area", "Rostrolateral visual area",
              "posteromedial area", "Anteromedial visual area"]:
        if k in region:
            return "Higher Visual Area"
    if "Retrosplenial" in region:
        return "Retrosplenial"
    if "optic radiation" in region:
        return "Optic Radiation"
    if "corpus" in region:
        return "Corpus Callosum"
    if "Unknown" in region:
        return "Unknown"
    if "area" not in region:
        return "subcortical"
    return None


def _zeta_one(args):
    import logging
    import warnings
    import scipy.signal
    import scipy.signal.windows
    if not hasattr(scipy.signal, "gaussian"):
        # zetapy 2.7 imports scipy.signal.gaussian, which newer scipy keeps in scipy.signal.windows
        scipy.signal.gaussian = scipy.signal.windows.gaussian
    import zetapy
    logging.disable(logging.WARNING)
    train, stims, seed = args
    np.random.seed(seed)  # zetapy draws from numpy's global generator
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        try:
            out = zetapy.getZeta(train, stims, dblUseMaxDur=0.3)
        except Exception:
            return np.nan
    return float(out[0] if isinstance(out, tuple) else out)


def zeta_pvalues(jobs, processes=None):
    """ZETA p-values, zetapy 2.7.2 getZeta with dblUseMaxDur = 0.3 s, as the paper's code
    (jlh_ephys/analysis.py, get_zetas; Methods "Determining circuit responders"). The code does
    not pin zetapy; 2.7.2, the last release with getZeta, matches the code's cached p-values
    (checked in the notebook). jobs: list of (spike train, onsets, seed). Runs in parallel; each
    call has its own seed, so the result does not depend on the number of processes."""
    import multiprocessing as mp
    import os
    ctx = mp.get_context("fork")
    processes = processes or os.cpu_count()
    with ctx.Pool(processes) as pool:
        return np.array(pool.map(_zeta_one, jobs, chunksize=8))


def code_zeta(session):
    """The paper's cached ZETA p-values (recordings/<session>/zetascores300ms.pkl in the code
    repository at c4aaa608): dict run -> p-value per unit, in the NWB units order. An outside
    input, used only to compare with the p-values recomputed here."""
    import pickle
    url = f"{CODE_REPO}/{CODE_FOLDERS[session]}/zetascores300ms.pkl"
    d = pickle.loads(requests.get(url, timeout=120).content)
    return {int(k): np.array([v[0] for v in vals], float) for k, vals in d.items()}


def holm_sidak(p):
    p = np.asarray(p, float)
    order = np.argsort(p)
    m = len(p)
    adj = np.empty(m)
    run = 0.0
    for k, i in enumerate(order):
        run = max(run, 1 - (1 - p[i]) ** (m - k))
        adj[i] = min(run, 1.0)
    return adj


def participation_ratio(X):
    """X: trials x neurons. PR of the neuron covariance, and components for 95% variance."""
    Xc = X - X.mean(0)
    s = np.linalg.svd(Xc, compute_uv=False)
    lam = s ** 2 / max(X.shape[0] - 1, 1)
    if lam.sum() <= 0:
        return np.nan, np.nan
    pr = lam.sum() ** 2 / np.sum(lam ** 2)
    cum = np.cumsum(lam) / lam.sum()
    ed = int(np.searchsorted(cum, 0.95) + 1)
    return pr, ed
