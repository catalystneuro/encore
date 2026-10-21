"""Loading and measures for DANDI:000010 (Li, Chen, Guo, Gerfen & Svoboda 2015, Nature 519:51).

The dandiset holds 99 extracellular sessions (left ALM, 19 mice) and 59 two-photon imaging
planes (left ALM, 4 mice) recorded during the object location discrimination task. Files are
streamed from the archive with remfile and h5py; nothing is written to disk.

Where parameters come from:
- Epochs (sample from pole movement onset for 1.3 s; delay the 1.3 s before the go cue; response
  1.3 s or 1.5 s after the go cue), the two-tailed t-test at P < 0.05, the spike width rule
  (trough to peak of the mean waveform, < 0.35 ms fast-spiking, > 0.45 ms putative pyramidal),
  200 ms windows, the neuropil factor 0.7 and F0 as the mean over 0.5 s before trial start, the
  Kruskal-Wallis test over 5-frame bins at P < 0.01, and the Wilcoxon rank sum test at P < 0.05
  all come from the claims file (claims/000010/10.1038-nature14178.yaml), which cites the
  paper's Methods.
- The window used to match a trial to its behavioural events (0.5 to 0.7 s after the trial
  start) is a reading of the data: the sample event falls 0.572 s (ephys) or 0.583 s (imaging)
  after the trial start in almost every trial. It is shown in the notebook's data check.
- The readings of reaction-time (a fixed threshold on the lick trace, or the baseline mean plus a
  number of s.d., with the delay epoch or its last 0.5 s as baseline) and of antidromic-latencies
  (the first spike in a window after the first pulse of a pair, without collision trials, or in
  the evoked peak) come from the claims file; the thresholds, numbers of s.d. and windows it
  leaves open are passed in from the notebook, which runs several.
- Thread counts for streaming are a standard choice that cannot change a result.
"""
import json
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET = "000010"
VERSION = "0.220126.1905"
API = "https://api.dandiarchive.org/api"

SAMPLE_LEN = 1.3   # s, sample epoch from pole movement onset (claims file, fig2-selective-fraction)
DELAY_LEN = 1.3    # s, delay epoch before the go cue
RESP_LENS = (1.3, 1.5)  # s, response epoch readings (i) and (ii)
MATCH_WIN = (0.5, 0.7)  # s after trial start where the sample event is looked for (data reading)


def list_assets():
    """All assets of the pinned version, as a DataFrame (path, asset_id, size)."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=500"
    rows = []
    while url:
        r = requests.get(url, timeout=60).json()
        rows += [dict(path=a["path"], asset_id=a["asset_id"], size=a["size"]) for a in r["results"]]
        url = r["next"]
    df = pd.DataFrame(rows).sort_values("path").reset_index(drop=True)
    df["subject"] = df.path.str.split("/").str[0].str.replace("sub-", "")
    df["kind"] = np.where(df.path.str.contains("ecephys"), "ephys", "ophys")
    return df


def version_metadata():
    return requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/", timeout=60).json()


def open_asset(asset_id):
    url = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60).url
    return h5py.File(remfile.File(url), "r")


def _s(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def _groups(f):
    """Names of the data objects under acquisition, stimulus, processing and analysis."""
    out = []
    for top in ("acquisition", "stimulus/presentation", "stimulus/templates", "processing", "analysis"):
        if top in f:
            for k in f[top]:
                obj = f[top][k]
                sub = list(obj.keys()) if isinstance(obj, h5py.Group) and top == "processing" else []
                out += [f"{top}/{k}/{x}" for x in sub] or [f"{top}/{k}"]
    return out


def lick_trace_check(asset_id):
    """Segments of the lick trace of one session, and its mean around the go cue of correct
    trials (5 ms bins from 0.2 s before to 0.3 s after), with the trial table."""
    f = open_asset(asset_id)
    lt = f["acquisition/BehavioralTimeSeries/lick_trace"]
    ts = lt["timestamps"][:]
    be = f["acquisition/BehavioralEvents"]
    tr = _trials(f, {k: be[k]["timestamps"][:] for k in be})
    gaps = np.where(np.diff(ts) > 0.001)[0]
    seg_start = ts[np.r_[0, gaps + 1]]
    seg_len = np.diff(np.r_[0, gaps + 1, len(ts)])
    go = tr.go[trial_sets(tr)["correct"]].values
    i = np.searchsorted(ts, go)
    win = np.arange(-2000, 3000)
    keep = (i + win[0] >= 0) & (i + win[-1] < len(ts))
    data = lt["data"]
    traces = np.array([data[k + win[0]:k + win[-1] + 1] for k in i[keep]])
    out = dict(n_samples=len(ts), rate=1 / np.median(np.diff(ts[:10000])), n_segments=len(seg_start),
               seg_len=np.unique(seg_len), seg_start_is_trial_start=np.isin(np.round(seg_start, 4),
                                                                            np.round(tr.start.values, 4)).mean(),
               n_trials=len(tr), mean_trace=traces.mean(0).reshape(-1, 50).mean(1),
               t_ms=(win.reshape(-1, 50)[:, 0]) / 10, unit=lt["data"].attrs["unit"],
               description=lt.attrs["description"])
    f.close()
    return out


def _read_contiguous(url, ds, parts=8):
    """All values of an uncompressed, contiguous HDF5 dataset `ds`, read from its byte offset in
    the file with parallel HTTP range requests (h5py serializes reads across threads)."""
    off, n, dt = ds.id.get_offset(), ds.shape[0], ds.dtype
    if off is None or ds.compression or ds.chunks:
        return ds[:]
    edges = off + np.linspace(0, n, parts + 1).astype(int) * dt.itemsize

    def get(i):
        r = requests.get(url, headers={"Range": f"bytes={edges[i]}-{edges[i + 1] - 1}"}, timeout=300)
        r.raise_for_status()
        return r.content
    with ThreadPoolExecutor(parts) as ex:
        buf = b"".join(ex.map(get, range(parts)))
    return np.frombuffer(buf, dt.newbyteorder("<") if dt.byteorder == "=" else dt)


def lick_windows(asset_id, go, post=0.4):
    """The lick trace (photodiode signal of mouth movements) around each go cue in `go`: the mean
    and s.d. over two baselines before the cue, the delay epoch (1.3 s) and its last 0.5 s (the
    examples the claims file gives under reaction-time), the value of the last sample before the
    cue, and the trace from the cue to `post` s after it (float32, NaN where not stored). The
    0.4 s span is a standard choice that cannot change a result: trials without a crossing in it
    are counted, not dropped silently."""
    url = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60).url
    f = h5py.File(remfile.File(url), "r")
    lt = f["acquisition/BehavioralTimeSeries/lick_trace"]
    ts = _read_contiguous(url, lt["timestamps"])
    x = _read_contiguous(url, lt["data"])
    f.close()
    rate = 1 / np.median(np.diff(ts[:10000]))
    n_post, n_delay, n_last = int(round(post * rate)), int(round(DELAY_LEN * rate)), int(round(0.5 * rate))
    i = np.searchsorted(ts, go)
    out = dict(rate=rate, base_delay_mean=[], base_delay_sd=[], base_last_mean=[], base_last_sd=[], at_go=[],
               trace=np.full((len(go), n_post), np.nan, np.float32))
    for n, k in enumerate(i):
        # Only windows stored without a gap (within one segment) are used.
        ok = (k - n_delay >= 0 and k + n_post <= len(ts) and np.isfinite(go[n])
              and abs(ts[k + n_post - 1] - ts[k - n_delay] - (n_post + n_delay - 1) / rate) < 2 / rate)
        d, l = (x[k - n_delay:k], x[k - n_last:k]) if ok else (np.array([np.nan]), np.array([np.nan]))
        out["base_delay_mean"].append(d.mean()); out["base_delay_sd"].append(d.std())
        out["base_last_mean"].append(l.mean()); out["base_last_sd"].append(l.std())
        out["at_go"].append(x[k - 1] if ok else np.nan)
        if ok:
            out["trace"][n] = x[k:k + n_post]
    for key in ("base_delay_mean", "base_delay_sd", "base_last_mean", "base_last_sd", "at_go"):
        out[key] = np.array(out[key])
    return out


def lick_all(sessions, threads=6):
    """`lick_windows` for the non-early trials (as `trial_sets`) of every extracellular session,
    with the session index and the correct and light flags of each trial."""
    def one(si):
        tr = sessions[si]["trials"]
        m = trial_sets(tr)["nonearly"]
        w = lick_windows(sessions[si]["asset_id"], tr.go[m].values)
        w.update(session=si, correct=trial_sets(tr)["correct"][m].values,
                 light=tr["light"][m].values.astype(bool) if "light" in tr else np.zeros(int(m.sum()), bool))
        return w
    with ThreadPoolExecutor(threads) as ex:
        return list(ex.map(one, range(len(sessions))))


def first_crossing_ms(trace, level, rate):
    """Time (ms) of the first sample of each row of `trace` above `level` (one value per row);
    NaN where none."""
    above = trace > np.asarray(level, float).reshape(-1, 1)
    first = above.argmax(1).astype(float)
    first[~above.any(1)] = np.nan
    return first / rate * 1000.0


def _trials(f, events):
    """Trial table with the sample, delay and go times matched to each trial.

    A trial gets the sample event that falls MATCH_WIN after its start, and the delay and go
    events that follow that sample event before the next sample event. Trials without a matched
    sample event keep NaN times.
    """
    t = f["intervals/trials"]
    df = pd.DataFrame(dict(
        start=t["start_time"][:], stop=t["stop_time"][:],
        instruction=[_s(x) for x in t["trial_instruction"][:]],
        early=[_s(x) for x in t["early_lick"][:]],
        outcome=[_s(x) for x in t["outcome"][:]],
    ))
    s = np.sort(events["sample"])
    j = np.searchsorted(s, df.start.values + MATCH_WIN[0])
    j = np.clip(j, 0, len(s) - 1)
    ok = (s[j] >= df.start.values + MATCH_WIN[0]) & (s[j] <= df.start.values + MATCH_WIN[1])
    df["sample"] = np.where(ok, s[j], np.nan)
    nxt = np.append(s[1:], np.inf)
    for name in ("delay", "go"):
        e = np.sort(events[name])
        k = np.clip(np.searchsorted(e, df["sample"].fillna(-1).values), 0, len(e) - 1)
        good = ok & (e[k] >= df["sample"].fillna(np.inf).values) & (e[k] < np.where(ok, nxt[j], -np.inf))
        df[name] = np.where(good, e[k], np.nan)
    return df


def _laser(f, trials):
    """Light pulses of the laser power series under stimulus/presentation: onset times (rising
    edges above half the series maximum), the power at each pulse and its width. Adds a `light`
    column to the trial table (any pulse within the trial window)."""
    out = {}
    pulses = []
    for k in f["stimulus/presentation"]:
        if not k.endswith("laser_power"):
            continue
        g = f["stimulus/presentation"][k]
        d = g["data"][:]
        ts = g["timestamps"][:]
        on = d > 0.5 * d.max()
        rise = np.where(on[1:] & ~on[:-1])[0] + 1
        fall = np.where(~on[1:] & on[:-1])[0] + 1
        fall = fall[np.searchsorted(fall, rise[0]):] if len(rise) else fall
        n = min(len(rise), len(fall))
        gaps = np.where(np.diff(ts) > 0.001)[0]
        out[k] = dict(onsets=ts[rise], power=d[np.minimum(rise + 3, len(d) - 1)], width_ms=(ts[fall[:n]] - ts[rise[:n]]) * 1000,
                      unit=_s(g["data"].attrs.get("unit", "")), max=float(d.max()), n_segments=len(gaps) + 1,
                      segment_samples=np.unique(np.diff(np.r_[0, gaps + 1, len(ts)])), n_samples=len(ts),
                      rate=float(1 / np.median(np.diff(ts[:1000]))))
        pulses.append(ts[rise])
    p = np.sort(np.concatenate(pulses)) if pulses else np.array([])
    k = np.searchsorted(trials.start.values, p, side="right") - 1
    inside = (k >= 0) & (p <= trials.stop.values[np.clip(k, 0, None)])
    trials["light"] = False
    trials.loc[trials.index[np.unique(k[inside])], "light"] = True
    return out, int((~inside).sum())


def load_ephys(asset_id):
    """One extracellular session: units, trials, light pulses and metadata. The lick trace is not
    read."""
    f = open_asset(asset_id)
    be = f["acquisition/BehavioralEvents"]
    events = {k: be[k]["timestamps"][:] for k in be}
    trials = _trials(f, events)
    laser, outside = _laser(f, trials)
    u = f["units"]
    idx = u["spike_times_index"][:]
    st = u["spike_times"][:]
    groups = [k for k in f["general/extracellular_ephys"] if k != "electrodes"]
    out = dict(
        asset_id=asset_id,
        subject=_s(f["general/subject/subject_id"][()]),
        genotype=_s(f["general/subject/genotype"][()]),
        identifier=_s(f["identifier"][()]),
        region=[json.loads(f["general/extracellular_ephys"][g].attrs["location"])["brain_regions"] for g in groups],
        optogenetics=list(f["general/optogenetics"].keys()) if "general/optogenetics" in f else [],
        trials=trials,
        laser=laser,
        pulses_outside_trials=outside,
        spikes=np.split(st, idx[:-1]),
        waveform=u["waveform_mean"][:],
        cell_type=np.array([_s(x) for x in u["cell_type"][:]]),
        quality=np.array([_s(x) for x in u["quality"][:]]),
        unit_rate=u["sampling_rate"][:],
        obs_intervals=u["obs_intervals"][:],
        obs_index=u["obs_intervals_index"][:],
        n_events={k: len(v) for k, v in events.items()},
        groups=_groups(f),
        trial_colnames=[_s(c) for c in f["intervals/trials"].attrs["colnames"]],
        unit_colnames=[_s(c) for c in u.attrs["colnames"]],
    )
    f.close()
    return out


def load_ophys(asset_id):
    """One imaging plane: raw and neuropil fluorescence, ROI labels and centroids, trials."""
    f = open_asset(asset_id)
    be = f["processing/behavior/BehavioralEvents"]
    events = {k: be[k]["timestamps"][:] for k in be}
    ps = f["processing/ophys/ImageSegmentation/PlaneSegmentation"]
    masks = ps["image_mask"][:]
    rr = f["processing/ophys/Fluorescence/RoiResponseSeries"]
    ip = f["general/optophysiology/ImagingPlane"]
    out = dict(
        asset_id=asset_id,
        subject=_s(f["general/subject/subject_id"][()]),
        genotype=_s(f["general/subject/genotype"][()]),
        identifier=_s(f["identifier"][()]),
        plane_description=_s(ip["description"][()]),
        plane_location=_s(ip["location"][()]),
        trials=_trials(f, events),
        F=rr["data"][:].astype(float),
        Fnp=f["processing/ophys/Fluorescence/NeuropilResponseSeries/data"][:].astype(float),
        rate=float(rr["starting_time"].attrs["rate"]),
        t0=float(rr["starting_time"][()]),
        roi_type=np.array([_s(x) for x in ps["cell_type"][:]]),
        included=ps["included"][:].astype(bool),
        centroid=np.array([np.argwhere(m).mean(0) for m in masks]),
        n_events={k: len(v) for k, v in events.items()},
        groups=_groups(f),
        trial_colnames=[_s(c) for c in f["intervals/trials"].attrs["colnames"]],
        roi_colnames=[_s(c) for c in ps.attrs["colnames"]],
    )
    f.close()
    return out


def load_all(assets, kind, threads=12):
    fn = load_ephys if kind == "ephys" else load_ophys
    ids = assets[assets.kind == kind].asset_id.tolist()
    with ThreadPoolExecutor(threads) as ex:
        res = list(ex.map(fn, ids))
    for r, p in zip(res, assets[assets.kind == kind].path):
        r["path"] = p
    return res


# ---------------------------------------------------------------- units

def spike_width_ms(waveform, rate):
    """Trough-to-peak interval of the mean waveform, in ms (claims file, units-classification)."""
    tr = int(np.argmin(waveform))
    pk = tr + int(np.argmax(waveform[tr:]))
    return (pk - tr) / rate * 1000.0, pk == len(waveform) - 1


def width_class(w):
    return np.where(w < 0.35, "FS", np.where(w > 0.45, "Pyr", "intermediate"))


def duplicate_pairs(spikes, cell_type):
    """Pairs (tagged unit, other unit) in one session whose spike trains are identical."""
    pairs = []
    for i, c in enumerate(cell_type):
        if c not in ("PT", "IT"):
            continue
        for j, sp in enumerate(spikes):
            if j != i and len(sp) == len(spikes[i]) and np.array_equal(sp, spikes[i]):
                pairs.append((i, j))
    return pairs


def unit_table(sessions):
    """One row per deposited unit, with width class, duplicate flag and the tag of its twin."""
    rows = []
    for si, s in enumerate(sessions):
        pairs = duplicate_pairs(s["spikes"], s["cell_type"])
        dup_of = {i: j for i, j in pairs}
        tag_of = {j: s["cell_type"][i] for i, j in pairs}
        for i in range(len(s["spikes"])):
            w, at_end = spike_width_ms(s["waveform"][i], s["unit_rate"][i])
            rows.append(dict(session=si, subject=s["subject"], unit=i, label=s["cell_type"][i],
                             width=w, peak_at_end=at_end, duplicate_of=dup_of.get(i, -1),
                             tag=tag_of.get(i, ""), n_spikes=len(s["spikes"][i])))
    df = pd.DataFrame(rows)
    df["width_class"] = width_class(df.width.values)
    df["is_duplicate"] = df.duplicate_of >= 0
    return df


# ---------------------------------------------------------------- spike counts

def counts(spikes, t0, t1):
    """Spike counts of one unit in windows [t0, t1) given per trial (arrays)."""
    return np.searchsorted(spikes, t1) - np.searchsorted(spikes, t0)


def epoch_windows(tr, resp_len):
    """(start, end) per trial for the sample, delay and response epochs."""
    return dict(
        sample=(tr["sample"].values, tr["sample"].values + SAMPLE_LEN),
        delay=(tr["go"].values - DELAY_LEN, tr["go"].values),
        response=(tr["go"].values, tr["go"].values + resp_len),
    )


def trial_sets(tr, light="any"):
    """Masks of trials used by the claims: correct (hit, no early lick) and error (miss, no early
    lick) trials, and all non-early trials, each with matched events and lick right/left.
    The imaging files mark no trial as an early lick, so there these masks cannot exclude them.
    light="none" also drops trials with a light pulse (tagging light, see `_laser`)."""
    has = tr["sample"].notna() & tr["go"].notna()
    lr = tr.instruction.isin(["right", "left"])
    noearly = tr.early.isin(["no early", "False"])
    # In trials without an early lick the go cue comes 2.6 s after the sample event; the few
    # trials where it does not are dropped (data check in the notebook).
    timing = (tr["go"] - tr["sample"] - (SAMPLE_LEN + DELAY_LEN)).abs() < 0.01
    noearly = noearly & timing
    if light == "none" and "light" in tr:
        has = has & ~tr["light"].astype(bool)
    return dict(
        correct=has & lr & noearly & (tr.outcome == "hit"),
        error=has & lr & noearly & (tr.outcome == "miss"),
        nonearly=has & lr & noearly & tr.outcome.isin(["hit", "miss"]),
    )


def ttest_p(a, b):
    """Two-tailed Student t-test P (scipy's default, equal variances); NaN when undefined."""
    from scipy.stats import ttest_ind
    if len(a) < 2 or len(b) < 2 or (np.var(a) == 0 and np.var(b) == 0):
        return np.nan
    return float(ttest_ind(a, b).pvalue)


# ---------------------------------------------------------------- imaging

def dff_trials(plane, r=0.7, base=0.5):
    """DF/F0 per ROI, with F = F_roi - r * F_neuropil and F0 the mean over `base` s before each
    trial start (claims file, imaging-selectivity-counts). Returns frame times and a function
    that averages DF/F of every ROI over [t0, t1) relative to each trial's own F0."""
    F = plane["F"] - r * plane["Fnp"]
    t = plane["t0"] + np.arange(F.shape[0]) / plane["rate"]
    tr = plane["trials"]
    starts = tr.start.values
    i0 = np.searchsorted(t, starts - base)
    i1 = np.searchsorted(t, starts)
    F0 = np.array([F[a:b].mean(0) if b > a else np.full(F.shape[1], np.nan) for a, b in zip(i0, i1)])
    return F, t, F0


def mean_dff(F, t, F0, rows, t0, t1):
    """Mean DF/F0 per (trial in rows, ROI) over [t0, t1) of each trial."""
    out = np.full((len(rows), F.shape[1]), np.nan)
    a = np.searchsorted(t, t0)
    b = np.searchsorted(t, t1)
    for n, k in enumerate(rows):
        if b[n] > a[n]:
            out[n] = (F[a[n]:b[n]].mean(0) - F0[k]) / F0[k]
    return out


# ---------------------------------------------------------------- per-unit measures

def epoch_stats(sessions, units, tset="correct", resp_len=1.3, light="any"):
    """Per unit: t-test P and mean rates (spikes/s) on lick right and lick left trials in the
    sample, delay and response epochs, with the trial counts."""
    rows = []
    for u in units.itertuples():
        s = sessions[u.session]
        tr = s["trials"]
        t = tr[trial_sets(tr, light)[tset]]
        sp = s["spikes"][u.unit]
        right = (t.instruction == "right").values
        d = dict(idx=u.Index, n_right=int(right.sum()), n_left=int((~right).sum()))
        for ep, (a, b) in epoch_windows(t, resp_len).items():
            c = counts(sp, a, b)
            d["p_" + ep] = ttest_p(c[right], c[~right])
            d["R_" + ep] = c[right].mean() / (b - a)[0] if right.any() else np.nan
            d["L_" + ep] = c[~right].mean() / (b - a)[0] if (~right).any() else np.nan
        rows.append(d)
    return pd.DataFrame(rows).set_index("idx")


def window_counts(sessions, units, starts, width=0.2, tset="correct", align="sample", light="any"):
    """Per unit: spike counts in windows [align + start, align + start + width) on lick right and
    lick left trials, as two (trials x windows) arrays."""
    out = {}
    for u in units.itertuples():
        s = sessions[u.session]
        tr = s["trials"]
        t = tr[trial_sets(tr, light)[tset]]
        sp = s["spikes"][u.unit]
        a = t[align].values[:, None] + np.asarray(starts)[None, :]
        c = np.searchsorted(sp, a + width) - np.searchsorted(sp, a)
        right = (t.instruction == "right").values
        out[u.Index] = (c[right], c[~right])
    return out


def window_diff(sessions, units, t0, t1, tset="correct", light="any"):
    """Per unit: mean rate (spikes/s) on lick right and lick left trials in [go + t0, go + t1)."""
    rows = []
    for u in units.itertuples():
        s = sessions[u.session]
        tr = s["trials"]
        t = tr[trial_sets(tr, light)[tset]]
        sp = s["spikes"][u.unit]
        right = (t.instruction == "right").values
        c = counts(sp, t.go.values + t0, t.go.values + t1) / (t1 - t0)
        rows.append(dict(idx=u.Index, R=c[right].mean(), L=c[~right].mean()))
    return pd.DataFrame(rows).set_index("idx")


def total_count_diff(sessions, units, tset="correct", resp_len=1.3, light="any"):
    """Per unit: mean spike count over the three epochs together, lick right minus lick left."""
    out = {}
    for u in units.itertuples():
        s = sessions[u.session]
        tr = s["trials"]
        t = tr[trial_sets(tr, light)[tset]]
        sp = s["spikes"][u.unit]
        right = (t.instruction == "right").values
        c = sum(counts(sp, a, b) for a, b in epoch_windows(t, resp_len).values())
        out[u.Index] = c[right].mean() - c[~right].mean()
    return pd.Series(out)


def boot_more_ipsi(contra, rng, n=10_000):
    """Fraction of resamples (neurons with replacement) with more ipsi- than contra-preferring
    neurons (claims file, fig3f-pt-contra-preferring; one-tailed)."""
    x = np.asarray(contra, bool)
    idx = rng.integers(0, len(x), (n, len(x)))
    k = x[idx].sum(1)
    return float(np.mean(len(x) - k > k))


# ---------------------------------------------------------------- imaging measures

def plane_trials(plane, tset, r=0.7, base=0.5):
    """DF/F0 of every ROI in each trial, as a (trials x frames x ROIs) array from the trial start
    to 2.0 s after the go cue, with frame times relative to the sample event and the lick right
    mask. F = F_roi - r * F_neuropil; F0 is the mean of F over `base` s before the trial start.
    Trials without `base` s of frames before their start are dropped."""
    F = plane["F"] - r * plane["Fnp"]
    rate = plane["rate"]
    t = plane["t0"] + np.arange(F.shape[0]) / rate
    tr = plane["trials"]
    tr = tr[trial_sets(tr)[tset]]
    i_start = np.searchsorted(t, tr.start.values)
    i_base = np.searchsorted(t, tr.start.values - base)
    i_s = np.searchsorted(t, tr["sample"].values)
    ok = (i_base < i_start) & (t[np.clip(i_base, 0, None)] >= tr.start.values - base - 1 / rate) & \
         (tr.start.values - base >= t[0])
    npre = int(np.min((i_s - i_start)[ok]))
    npost = int(np.floor((SAMPLE_LEN + DELAY_LEN + 2.0) * rate))
    ok &= i_s + npost <= F.shape[0]
    i_s, i_start, i_base = i_s[ok], i_start[ok], i_base[ok]
    F0 = np.array([F[a:b].mean(0) for a, b in zip(i_base, i_start)])
    idx = i_s[:, None] + np.arange(-npre, npost)[None, :]
    X = (F[idx] - F0[:, None, :]) / F0[:, None, :]
    rel = np.arange(-npre, npost) / rate
    right = (tr.instruction == "right").values[ok]
    return X, rel, right, int((~ok).sum())


def classify_plane(X, rel, right, included, resp_len, span, rank):
    """Task-related, selective and contra-preferring ROIs of one plane (claims file,
    imaging-selectivity-counts). span 'a': Kruskal-Wallis bins from sample onset to the end of the
    response epoch; 'b': the whole recorded trial. rank 'mean': rank sum test of the mean DF/F
    over the three epochs; 'each': each epoch, selective if any is significant."""
    from scipy.stats import kruskal, ranksums
    if span == "a":
        f0, f1 = np.searchsorted(rel, 0), np.searchsorted(rel, SAMPLE_LEN + DELAY_LEN + resp_len)
    else:
        f0, f1 = 0, len(rel)
    nb = (f1 - f0) // 5
    B = X[:, f0:f0 + 5 * nb, :].reshape(X.shape[0], nb, 5, -1).mean(2)
    p_kw = [kruskal(*[B[side, b, :] for b in range(nb)], axis=0).pvalue for side in (right, ~right)]
    task = (p_kw[0] < 0.01) | (p_kw[1] < 0.01)
    eps = [(0, SAMPLE_LEN), (SAMPLE_LEN, SAMPLE_LEN + DELAY_LEN),
           (SAMPLE_LEN + DELAY_LEN, SAMPLE_LEN + DELAY_LEN + resp_len)]
    Ep = np.stack([X[:, np.searchsorted(rel, a):np.searchsorted(rel, b), :].mean(1) for a, b in eps], 1)
    y = Ep.mean(1)
    if rank == "mean":
        sel = ranksums(y[right], y[~right], axis=0).pvalue < 0.05
    else:
        sel = np.any([ranksums(Ep[right, k], Ep[~right, k], axis=0).pvalue < 0.05 for k in range(3)], 0)
    contra = y[right].mean(0) > y[~right].mean(0)
    return dict(task=task & included, sel=task & sel & included, contra=contra, included=included)


def spatial_tests(planes, res, neighbours, shuffle, rng, n=10_000, chunk=500):
    """The two shuffle tests of fig4f-spatially-intermingled. For the selective ROIs of each plane:
    (1) the probability that a ROI's nearest neighbour (among selective ROIs, or among all
    included ROIs, a non-selective one counting as not the same) has the same preference, P the
    fraction of shuffles with a probability at least as large; (2) the mean distance (pixels) from
    each ROI to the nearest ROI of the same preference in its plane, P the fraction of shuffles
    with a distance at least as small. Labels are shuffled among selective ROIs within each plane
    or across all planes."""
    fov = []
    for pl, r in zip(planes, res):
        si = np.where(r["sel"])[0]
        if len(si) < 2:
            continue
        xy = pl["centroid"]
        cand = si if neighbours == "selective" else np.where(r["included"])[0]
        D = np.linalg.norm(xy[si][:, None] - xy[cand][None], axis=2)
        D[si[:, None] == cand[None, :]] = np.inf
        nn = cand[np.argmin(D, 1)]
        pos = {k: i for i, k in enumerate(si)}
        nnpos = np.array([pos.get(k, -1) for k in nn])
        Dss = np.linalg.norm(xy[si][:, None] - xy[si][None], axis=2).astype(np.float32)
        np.fill_diagonal(Dss, np.inf)
        fov.append((r["contra"][si], nnpos, Dss))
    sizes = np.array([len(f[0]) for f in fov])
    offs = np.r_[0, np.cumsum(sizes)]
    lab_all = np.concatenate([f[0] for f in fov])

    def stats_of(L_list):
        same = 0.0
        dsum = np.zeros(L_list[0].shape[0])
        dcnt = np.zeros(L_list[0].shape[0])
        for (lab0, nnpos, Dss), L in zip(fov, L_list):
            ok = nnpos >= 0
            same = same + (L[:, ok] == L[:, nnpos[ok]]).sum(1)
            M = np.where(L[:, :, None] == L[:, None, :], Dss[None], np.inf).min(2)
            fin = np.isfinite(M)
            dsum += np.where(fin, M, 0).sum(1)
            dcnt += fin.sum(1)
        return same / len(lab_all), dsum / dcnt

    obs_p, obs_d = stats_of([f[0][None, :] for f in fov])
    sp, sd = [], []
    done = 0
    while done < n:
        m = min(chunk, n - done)
        if shuffle == "within":
            Ls = [np.array([rng.permutation(f[0]) for _ in range(m)]) for f in fov]
        else:
            perm = np.argsort(rng.random((m, len(lab_all))), axis=1)
            G = lab_all[perm]
            Ls = [G[:, offs[i]:offs[i + 1]] for i in range(len(fov))]
        a, b = stats_of(Ls)
        sp.append(a)
        sd.append(b)
        done += m
    sp, sd = np.concatenate(sp), np.concatenate(sd)
    return dict(prob=float(obs_p[0]), P_prob=float(np.mean(sp >= obs_p[0])), prob_shuffle=float(sp.mean()),
                dist=float(obs_d[0]), P_dist=float(np.mean(sd <= obs_d[0])), dist_shuffle=float(sd.mean()),
                planes=len(fov), cells=int(len(lab_all)))


def pair_onsets(onsets, gap=0.05):
    """First pulse of each pulse pair (pulses with no other pulse in the preceding `gap` s)."""
    onsets = np.sort(onsets)
    return onsets[np.r_[True, np.diff(onsets) > gap]]


def first_spike_latency(spikes, onsets, window):
    """Latency (s) of the first spike within `window` (s) after each onset; NaN where none."""
    j = np.searchsorted(spikes, onsets)
    lat = np.full(len(onsets), np.nan)
    ok = j < len(spikes)
    d = spikes[np.clip(j, 0, len(spikes) - 1)] - onsets
    ok &= d < window
    lat[ok] = d[ok]
    return lat


def antidromic_latencies(spikes, onsets, window, reading="w", par=None, bin_ms=0.1):
    """Latencies (ms) kept under the readings of antidromic-latencies (claims file): (w) the first
    spike within `window` s after the first pulse of each pair; (c) as (w), without pulses that
    have a spike in the `par` ms before them (collision trials); (r) as (w), keeping only latencies
    within `par` ms of the peak of the neuron's latency histogram (`bin_ms` bins, a standard choice
    finer than the jitter tested). The claims file leaves the window and `par` open."""
    first = pair_onsets(onsets)
    lat = first_spike_latency(spikes, first, window) * 1000
    if reading == "c":
        j = np.searchsorted(spikes, first) - 1
        prev = np.where(j >= 0, (first - spikes[np.clip(j, 0, None)]) * 1000, np.inf)
        lat[prev < par] = np.nan
    lat = lat[~np.isnan(lat)]
    if reading == "r" and len(lat):
        h, e = np.histogram(lat, bins=np.arange(0, window * 1000 + bin_ms, bin_ms))
        peak = e[h.argmax()] + bin_ms / 2
        lat = lat[np.abs(lat - peak) <= par]
    return lat
