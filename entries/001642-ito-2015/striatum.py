"""Loading and measures for dandiset 001642 (Ito & Doya 2015, J Neurosci 35:3499).

Data are streamed from the DANDI archive at the pinned version ``VERSION``; nothing is
written to disk. Where each parameter comes from:

- Task events E1 to E6 and the mean phase durations ``PHASE_DUR`` (0.75, 1.50, 0.54, 0.76,
  0.38 s; Phases 1 and 7 are 2 s each) are those of the paper (Methods, "Event-aligned spike
  histogram"). E1 = ``pokeC_on_time``, E2 = ``tone_on_time``, E3 = ``tone_off_time``, E4 =
  ``pokeC_off_time``, E5 = ``action_on_time``, E6 = ``action_off_time``, as the trial table
  describes its columns.
- Cue codes: the table describes ``state`` as 1 = left, 2 = right, 3 = choice tone, but the data
  show 2 = left tone, 3 = right tone and 1 = choice tone (see ``CUE_OF_STATE``; the notebook's
  data check shows the reward contingencies that settle it).
- Block types come from the reward rule of each block in ``BlockDesign`` (the paper's Fig. 1C):
  (50, 0) or (0, 50) single fixed (SF), (50, 50) double fixed (DF), (0, 0) extinction (EXT),
  any rule with 90 or 10 free choice (FREE).
- Mutual information: four firing levels per window, read as quartiles of the trial spike
  counts (claims file, O1, reading a); plug-in estimate from the 4 x 2 table, in bits/s. The
  shuffle threshold is the second largest of 100 region averages with random binary events
  (Methods, "Mutual information"). The random events are permutations of the real labels: a
  standard choice that keeps the proportion of the two events (the paper does not say how the
  random events were drawn).
"""
import concurrent.futures as cf
import json
import urllib.request

import h5py
import numpy as np
import pandas as pd
import remfile

DANDISET = "001642"
VERSION = "0.260205.0153"
API = "https://api.dandiarchive.org/api"

CUE_OF_STATE = {1: "choice", 2: "left", 3: "right"}
PHASE_DUR = np.array([2.0, 0.75, 1.50, 0.54, 0.76, 0.38, 2.0])  # Phases 1..7 (paper, Methods)
EDGES = np.concatenate([[0.0], np.cumsum(PHASE_DUR)])  # E0..E7 on the EASH axis
EVENT_COLS = ["pokeC_on_time", "tone_on_time", "tone_off_time", "pokeC_off_time",
              "action_on_time", "action_off_time"]  # E1..E6
REGIONS = ["DLS", "DMS", "VS"]


def list_assets():
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=500"
    with urllib.request.urlopen(url) as r:
        res = json.load(r)["results"]
    return sorted([(a["path"], a["asset_id"]) for a in res])


def _read_table(grp):
    out = {}
    for k in grp.keys():
        d = grp[k]
        if isinstance(d, h5py.Dataset) and k != "id" and not k.endswith("_index"):
            v = d[:]
            if v.dtype.kind in "SO":
                v = np.array([x.decode() if isinstance(x, bytes) else x for x in v])
            out[k] = v
    return pd.DataFrame(out)


def load_session(path, asset_id, keep_spikes=True):
    """Trials, blocks and units of one session, reduced to what the analyses use."""
    url = f"{API}/assets/{asset_id}/download/"
    with h5py.File(remfile.File(url), "r") as h:
        tr = _read_table(h["intervals/trials"])
        bd = _read_table(h["processing/behavior/BlockDesign"])
        if "units" in h:
            u = h["units"]
            units = pd.DataFrame({c: [x.decode() if isinstance(x, bytes) else x for x in u[c][:]]
                                  for c in ["Unit_Name", "Area", "Electrode_ID", "Neuron_ID", "PANs"]})
            idx = u["spike_times_index"][:]
            st = u["spike_times"][:] if keep_spikes else None
        else:  # a session without units
            units = pd.DataFrame({c: [] for c in ["Unit_Name", "Area", "Electrode_ID", "Neuron_ID", "PANs"]})
            idx = np.zeros(0, dtype=int)
            st = np.zeros(0)
        subject = h["general/subject/subject_id"][()].decode()
        session = h["general/session_id"][()].decode()
    spikes = []
    lo = 0
    for hi in idx:
        spikes.append(st[lo:hi] if keep_spikes else None)
        lo = hi
    units["n_spikes"] = np.diff(np.concatenate([[0], idx]))
    units["spikes"] = spikes
    tr["trial"] = np.arange(len(tr))
    # block type from the block's reward rule
    rule = {i + 1: (l, r) for i, (l, r) in enumerate(zip(bd.RewardRule_L, bd.RewardRule_R))}
    def btype(b):
        l, r = rule[b]
        if (l, r) == (0, 0):
            return "EXT"
        if (l, r) in [(50, 0), (0, 50)]:
            return "SF"
        if (l, r) == (50, 50):
            return "DF"
        return "FREE"
    tr["btype"] = [btype(b) for b in tr.block]
    tr["rule_L"] = [rule[b][0] for b in tr.block]
    tr["rule_R"] = [rule[b][1] for b in tr.block]
    tr["cue"] = tr.state.map(CUE_OF_STATE)
    tr["choice"] = tr.result.isin([1, 3]) & tr.action.isin([1, 2])
    ev = tr[EVENT_COLS].to_numpy()
    tr["events_ok"] = tr.choice & np.all(np.isfinite(ev), axis=1) & np.all(np.diff(ev, axis=1) > 0, axis=1)
    for df in (tr, bd, units):
        df["subject"] = subject
        df["session"] = session
    bd["block"] = np.arange(1, len(bd) + 1)
    return dict(path=path, subject=subject, session=session, trials=tr, blocks=bd, units=units)


def load_all(workers=8, keep_spikes=True):
    assets = list_assets()
    with cf.ThreadPoolExecutor(workers) as ex:
        out = list(ex.map(lambda a: load_session(*a, keep_spikes=keep_spikes), assets))
    return out


# ---------------------------------------------------------------- event-aligned spikes
def warp_trials(spikes, trials):
    """Spike times of each trial mapped onto the EASH axis (seconds from E0, 0 to 7.93 s).

    Phases 2 to 6 are scaled linearly to the paper's mean durations; Phases 1 and 7 (2 s before
    E1 and after E6) are not scaled (Methods, EASH). Returns a list of arrays, one per trial.
    """
    ev = trials[EVENT_COLS].to_numpy()
    real = np.column_stack([ev[:, 0] - 2.0, ev, ev[:, 5] + 2.0])
    out = []
    lo = np.searchsorted(spikes, real[:, 0], "left")
    hi = np.searchsorted(spikes, real[:, 7], "right")
    for i in range(len(real)):
        s = spikes[lo[i]:hi[i]]
        out.append(np.interp(s, real[i], EDGES))
    return out, real


def counts_in_windows(warped, windows):
    """Spike counts per trial (rows) in each [start, stop) window (columns) of the EASH axis."""
    w = np.asarray(windows)
    out = np.zeros((len(warped), len(w)), dtype=np.int32)
    for i, s in enumerate(warped):
        a = np.searchsorted(s, w[:, 0], "left")
        b = np.searchsorted(s, w[:, 1], "left")
        out[i] = b - a
    return out


def counts_real_windows(spikes, starts, stops):
    """Spike counts per trial in real-time windows (arrays of shape trials x windows)."""
    return np.searchsorted(spikes, stops, "left") - np.searchsorted(spikes, starts, "left")


def eash(warped, binw=0.01):
    """Mean firing rate (Hz) over trials in bins of the EASH axis."""
    edges = np.arange(0, EDGES[-1] + 1e-9, binw)
    if edges[-1] < EDGES[-1] - 1e-9:
        edges = np.append(edges, EDGES[-1])
    h = np.zeros(len(edges) - 1)
    for s in warped:
        h += np.histogram(s, edges)[0]
    return h / len(warped) / np.diff(edges), edges


# ---------------------------------------------------------------- mutual information
def quartile_levels(counts):
    """Firing levels f1..f4 (0..3) per trial and window: quartiles of the counts over trials.

    Levels are cut at the 25th, 50th and 75th percentiles of each window's counts; tied counts
    share a level, so a window with many zero counts has fewer than four occupied levels.
    """
    q = np.percentile(counts, [25, 50, 75], axis=0)  # 3 x W
    lev = (counts[:, :, None] > q.T[None, :, :]).sum(axis=2)
    return lev


def mi_bits(levels, labels, pt=False):
    """Plug-in mutual information (bits) between levels (T x W, values 0..3) and binary labels.

    ``labels`` is T (one event) or T x S (S events at once). Returns W or S x W. With ``pt``,
    the Panzeri and Treves (1996) bias estimate, [sum_x (R_x - 1) - (R - 1)] / (2 N ln 2) with
    R the occupied firing levels (overall and given each event), is subtracted; the paper cites
    Panzeri and Treves (1996) for its MI (Results, "Information coding of state, action, and
    reward", paragraph 1).
    """
    lab = np.asarray(labels, dtype=float)
    single = lab.ndim == 1
    if single:
        lab = lab[:, None]
    T = levels.shape[0]
    onehot = (levels[:, :, None] == np.arange(4)[None, None, :]).astype(float)  # T W 4
    n_f = onehot.sum(axis=0)  # W 4
    n1 = np.einsum("ts,twk->swk", lab, onehot)  # S W 4 (x = 1)
    n0 = n_f[None] - n1
    p1 = lab.sum(axis=0) / T  # S
    p0 = 1 - p1
    pf = n_f / T
    out = np.zeros(n1.shape[:2])
    for nx, px in ((n1, p1), (n0, p0)):
        pj = nx / T
        with np.errstate(divide="ignore", invalid="ignore"):
            term = pj * np.log2(pj / (pf[None] * px[:, None, None]))
        out += np.nansum(term, axis=2)
    if pt:
        R = (n_f > 0).sum(axis=1)[None, :]  # 1 x W
        bias = (((n1 > 0).sum(2) - 1).clip(0) + ((n0 > 0).sum(2) - 1).clip(0) - (R - 1)) / (2 * T * np.log(2))
        out = out - bias
    return out[0] if single else out


def mi_with_shuffles(counts, labels, rng, n_shuffle=100, winlen=0.1):
    """MI (bits/s) of the real labels and of ``n_shuffle`` permutations, per window.

    Returns a dict with ``plugin`` and ``pt`` (Panzeri-Treves corrected), each a pair
    (real W, shuffles S x W as float32)."""
    lev = quartile_levels(counts)
    labels = np.asarray(labels).astype(int)
    perms = np.column_stack([rng.permutation(labels) for _ in range(n_shuffle)])
    out = {}
    for name, pt in (("plugin", False), ("pt", True)):
        out[name] = (mi_bits(lev, labels, pt) / winlen, (mi_bits(lev, perms, pt) / winlen).astype(np.float32))
    return out


def threshold(shuffle_means):
    """Second largest of the region averages of the shuffles (p < 0.01 with 100 repeats)."""
    return np.sort(shuffle_means, axis=0)[-2]


# ---------------------------------------------------------------- per-neuron event-aligned data
def neurons(D, select):
    """One record per unit for which ``select(unit_row)`` is true.

    Each record holds the unit's session trials with an L/R choice and the six events in order
    (``tr``), and its spikes on the EASH axis as one sorted key per spike, trial index x 100 +
    EASH time (``key``), so that counts in any window of any trial are two binary searches.
    """
    out = []
    for d in D:
        tr = d["trials"][d["trials"].events_ok].reset_index(drop=True)
        if len(tr) == 0:
            continue
        for _, u in d["units"].iterrows():
            if u.Area not in REGIONS or not select(u):
                continue
            warped, real = warp_trials(u.spikes, tr)
            key = np.concatenate([i * 100.0 + w for i, w in enumerate(warped)])
            out.append(dict(region=u.Area, session=d["session"], subject=d["subject"],
                            unit=u.Unit_Name, tr=tr, key=key, spikes=u.spikes, real=real))
    return out


def wcounts(nrn, windows, trials=None):
    """Spike counts (trials x windows) in [start, stop) windows of the EASH axis."""
    w = np.asarray(windows, dtype=float)
    idx = np.arange(len(nrn["tr"])) if trials is None else np.asarray(trials)
    base = idx[:, None] * 100.0
    return (np.searchsorted(nrn["key"], base + w[None, :, 1], "left")
            - np.searchsorted(nrn["key"], base + w[None, :, 0], "left"))


def rcounts(nrn, event, offsets, trials=None):
    """Spike counts in real-time windows [event + a, event + b) for (a, b) in ``offsets``.

    ``event`` is 0..7 for E0..E7."""
    idx = np.arange(len(nrn["tr"])) if trials is None else np.asarray(trials)
    t = nrn["real"][idx, event]
    o = np.asarray(offsets, dtype=float)
    return (np.searchsorted(nrn["spikes"], t[:, None] + o[None, :, 1], "left")
            - np.searchsorted(nrn["spikes"], t[:, None] + o[None, :, 0], "left"))


def bins(width):
    """Consecutive bins of the given width from E0 to E7 (the last one shorter)."""
    e = np.arange(0, EDGES[-1] + 1e-9, width)
    if e[-1] < EDGES[-1] - 1e-9:
        e = np.append(e, EDGES[-1])
    return np.column_stack([e[:-1], e[1:]])


def gauss_smooth(x, sd_bins):
    if not sd_bins:
        return x
    from scipy.ndimage import gaussian_filter1d
    return gaussian_filter1d(x, sd_bins, mode="nearest")
