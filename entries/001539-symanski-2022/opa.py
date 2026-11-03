"""Loading and measures for dandiset 001539 (Symanski, Bladon et al. 2022, eLife 11:e79545).

The dandiset holds one NWB file per recording day: the task epochs of the day (no sleep epochs),
a trial table (odor port beam break on and off, rewarded, reward well entry and exit), position
from the overhead camera (x, y, speed), sorted units (spike times and one electrode value each)
and LFP at 1.5 kHz, two channels per tetrode ("Ref OFF", relative to the ground screw, and
"Ref ON", locally referenced).

Where each parameter comes from is said beside it:
- "criterion": the claim's criterion in claims/001539/10.7554-elife.79545.yaml (which cites the
  paper or its code);
- "paper, <passage>": a detail the claims file lacks, taken from the paper (protocol, author
  step 1.6);
- "assumption": a choice the paper leaves open, with the reason;
- "standard choice": a detail that cannot change a result.

Two properties of the files shape the loading (both are checked in the notebook):
- The units table's `electrodes` column holds the tetrode number (the number in the electrode
  table's `label`, "tetrodeN"), not a row index of the electrode table. The region of a unit is
  the location of the tetrode with that label.
- The trial table has no odor identity and no chosen well. The chosen side is read from the
  position after odor port exit (`choice_side`); the odor is the chosen side on rewarded trials
  and the other side on unrewarded ones (paper, Methods, Odor-place association task training:
  "Odor 1 ... indicated that the rat should go to Reward 1").
"""
from __future__ import annotations

import functools
import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy import signal, stats

DANDISET = "001539"
VERSION = "0.250815.1203"
API = "https://api.dandiarchive.org/api"
FS_LFP = 1500.0  # paper, Methods, Tetrode recordings ("LFP signals were sampled at 1.5 kHz")

BETA = (20.0, 30.0)  # criterion (Methods, Local field potential)
RR = (7.0, 8.0)  # criterion (Methods, Local field potential)

_session = requests.Session()


# ----------------------------------------------------------------------------------------------
# Archive


def list_assets():
    """Assets of the pinned version, sorted by path."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    out = []
    while url:
        d = json.load(urllib.request.urlopen(url))
        out += d["results"]
        url = d["next"]
    rows = []
    for a in out:
        p = a["path"]
        sub = p.split("/")[0].replace("sub-Symanski-", "")
        ses = p.split("_ses-")[1].split("_")[0]
        rows.append(dict(asset_id=a["asset_id"], path=p, size=a["size"], subject=sub, session=ses))
    return pd.DataFrame(rows).sort_values("path").reset_index(drop=True)


def s3_url(asset_id):
    r = _session.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True)
    return r.url


def _s(x):
    return x.decode() if isinstance(x, bytes) else str(x)


# ----------------------------------------------------------------------------------------------
# One recording day


class Session:
    """Everything the analyses use from one file, read by streaming.

    Attributes: subject, session, epochs (n x 2), epoch_types, trials (DataFrame), pos (DataFrame
    t, x, y, v), units (DataFrame: spikes, tetrode, region, row_region, group_region), channels (DataFrame of the
    LFP columns: col, tetrode, region, ref), lfp_ts (LFP timestamps), and the byte offset of the
    LFP array for range reads.
    """

    def __init__(self, asset_row):
        self.asset_id = asset_row["asset_id"]
        self.subject = asset_row["subject"]
        self.session = asset_row["session"]
        self.name = f"{self.subject}_{self.session}"
        self.url = s3_url(self.asset_id)
        f = h5py.File(remfile.File(self.url), "r")
        ep = f["intervals/epoch intervals"]
        self.epochs = np.c_[ep["start_time"][:], ep["stop_time"][:]]
        self.epoch_types = [_s(x) for x in ep["epoch_type"][:]]
        tr = f["intervals/trials"]
        self.trials = pd.DataFrame(
            dict(
                start=tr["start_time"][:],
                stop=tr["stop_time"][:],
                rewarded=tr["rewarded"][:],
                rstart=tr["reward_start_time"][:],
                rend=tr["reward_end_time"][:],
            )
        )
        self.trials["dur"] = self.trials.stop - self.trials.start
        p = f["processing/behavior/Position/SpatialSeries"]
        P = p["data"][:]
        self.pos = pd.DataFrame(dict(t=p["timestamps"][:], x=P[:, 0], y=P[:, 1], v=P[:, 2]))
        self.pos_unit = _s(p["data"].attrs["unit"])
        e = f["general/extracellular_ephys/electrodes"]
        labels = [_s(x) for x in e["label"][:]]
        locs = [_s(x) for x in e["location"][:]]
        refs = [_s(x) for x in e["referenced"][:]]
        self.channels = pd.DataFrame(
            dict(
                col=np.arange(len(labels)),
                tetrode=[int(x.replace("tetrode", "")) for x in labels],
                region=locs,
                ref=refs,
                group=[f[r].name.split("/")[-1] for r in e["group"][:]],
            )
        )
        self.ref_description = _s(e["referenced"].attrs.get("description", ""))
        tet_region = dict(zip(self.channels.tetrode, self.channels.region))
        # the third reading of a unit's electrodes value: the number N of the electrode group
        # "TetrodeN" (group names and labels disagree in every file; data check)
        grp_region = dict(zip(self.channels.group.str.replace("Tetrode", "").astype(int), self.channels.region))
        st = f["units/spike_times"][:]
        idx = f["units/spike_times_index"][:]
        uel = f["units/electrodes"][:]
        spikes = np.split(st, idx[:-1])
        self.units = pd.DataFrame(
            dict(
                spikes=spikes,
                tetrode=uel,
                region=[tet_region.get(int(u), "?") for u in uel],
                row_region=[locs[int(u)] if int(u) < len(locs) else "?" for u in uel],
                group_region=[grp_region.get(int(u), "?") for u in uel],
            )
        )
        # inventory of the file, to show what it does and does not hold (data check)
        def _keys(g):
            return sorted(g.keys()) if isinstance(g, h5py.Group) else []

        self.inventory = dict(
            acquisition=_keys(f["acquisition"]) if "acquisition" in f else [],
            stimulus=[k + "/" + x for k in _keys(f["stimulus"]) for x in _keys(f["stimulus"][k])] if "stimulus" in f else [],
            processing={m: _keys(f["processing"][m]) for m in _keys(f["processing"])} if "processing" in f else {},
            intervals=_keys(f["intervals"]) if "intervals" in f else [],
            units_columns=_keys(f["units"]),
            electrodes_columns=_keys(e),
            trials_columns=_keys(tr),
        )
        self.units["n_spikes"] = [len(s) for s in spikes]
        self.units["sorted"] = [bool(np.all(np.diff(s) >= 0)) for s in spikes]
        L = f["processing/ecephys/LFP/ElectricalSeries/data"]
        self.lfp_shape = L.shape
        self.lfp_offset = L.id.get_offset()
        self.lfp_unit = _s(L.attrs["unit"])
        self.lfp_chunks = L.chunks
        self.lfp_dtype = L.dtype
        self.lfp_ts = f["processing/ecephys/LFP/ElectricalSeries/timestamps"][:]
        A = f["acquisition/ElectricalSeries/data"]
        self.acq_shape = A.shape
        self.acq_unit = _s(A.attrs["unit"])
        # the acquisition series compared with the LFP on one stretch
        i0 = len(self.lfp_ts) // 2
        self.acq_equals_lfp = bool(np.array_equal(A[i0 : i0 + 2000], L[i0 : i0 + 2000]))
        f.close()
        self._derive()

    # ------------------------------------------------------------------------------------------
    def _derive(self):
        tr = self.trials
        pos = self.pos
        tr["epoch"] = np.searchsorted(self.epochs[:, 0], tr.start.values) - 1
        # odor port and wells per epoch: the camera frame can differ between epochs
        self.geom = {}
        for e in np.unique(tr.epoch):
            m = (tr.epoch == e).values
            x = np.interp(tr.start[m], pos.t, pos.x)
            y = np.interp(tr.start[m], pos.t, pos.y)
            port = np.array([np.median(x), np.median(y)])
            rw = m & (tr.rewarded == 1).values
            # wells located at reward well exit: on the mazes with wells beside the port the rat
            # breaks the reward beam before the head LED has moved far from the port
            wx = np.interp(tr.rend[rw], pos.t, pos.x)
            wy = np.interp(tr.rend[rw], pos.t, pos.y)
            left = wx < port[0]
            wells = {
                "L": np.array([np.median(wx[left]), np.median(wy[left])]),
                "R": np.array([np.median(wx[~left]), np.median(wy[~left])]),
            }
            self.geom[int(e)] = dict(port=port, wells=wells)
        g = [self.geom[int(e)] for e in tr.epoch]
        rx = np.interp(tr.rend, pos.t, pos.x)
        self.reward_side = np.array(
            ["" if np.isnan(a) else ("L" if abs(a - gg["wells"]["L"][0]) < abs(a - gg["wells"]["R"][0]) else "R") for a, gg in zip(rx, g)]
        )
        tr["side_pos"] = choice_side(self)
        # the rewarded well on rewarded trials, the position rule on the others
        tr["side"] = np.where(tr.rewarded == 1, self.reward_side, tr.side_pos)
        tr["odor"] = np.where(tr.rewarded == 1, tr.side, np.where(tr.side == "L", "R", np.where(tr.side == "R", "L", "")))
        g0 = self.geom[min(self.geom)]
        self.port = g0["port"]
        self.wells = g0["wells"]
        self.stem = float(np.median([gg["port"][1] - 0.5 * (gg["wells"]["L"][1] + gg["wells"]["R"][1]) for gg in self.geom.values()]))
        self.well_dx = float(np.median([abs(gg["wells"]["R"][0] - gg["wells"]["L"][0]) for gg in self.geom.values()]))

    def lfp_index(self, t):
        """Sample index of time t on the LFP timestamps (which have gaps between epochs)."""
        return np.searchsorted(self.lfp_ts, t)

    def read_lfp(self, t0, t1, cols):
        """Stream LFP rows between times t0 and t1 (HTTP range read of the contiguous array) and
        keep columns `cols`, as float32. Returns (times, data)."""
        i0 = max(int(self.lfp_index(t0)), 0)
        i1 = min(int(self.lfp_index(t1)), self.lfp_shape[0])
        return self.lfp_ts[i0:i1], read_rows(self.url, self.lfp_offset, self.lfp_shape[1], i0, i1, cols)


def read_rows(url, offset, ncols, i0, i1, cols):
    if i1 <= i0:
        return np.zeros((0, len(cols)), np.float32)
    rowb = ncols * 8
    for attempt in range(5):
        try:
            r = _session.get(url, headers={"Range": f"bytes={offset + i0 * rowb}-{offset + i1 * rowb - 1}"}, timeout=120)
            a = np.frombuffer(r.content, "<f8").reshape(-1, ncols)
            if a.shape[0] == i1 - i0:
                return a[:, cols].astype(np.float32)
        except Exception:  # retry on a dropped connection
            pass
    raise IOError(f"range read failed {url} {i0} {i1}")


def load_sessions(assets, workers=8):
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(Session, [r for _, r in assets.iterrows()]))


# ----------------------------------------------------------------------------------------------
# Behaviour


def choice_side(S, window=6.0):
    """Side ('L' or 'R') of the reward well the rat came closest to in the `window` seconds after
    odor port exit (bounded by the next trial's start). Assumption: the trial table has no chosen
    well, and on an unrewarded trial the well the rat approaches is its choice. Checked in the
    notebook against the well at reward exit on rewarded trials. '' when there is no position."""
    tr = S.trials
    pos = S.pos
    nxt = np.r_[tr.start.values[1:], np.inf]
    out = []
    for a, b, e in zip(tr.stop.values, nxt, tr.epoch.values):
        w = S.geom[int(e)]["wells"]
        m = (pos.t.values > a) & (pos.t.values < min(b, a + window))
        if not m.any():
            out.append("")
            continue
        px, py = pos.x.values[m], pos.y.values[m]
        dl = np.hypot(px - w["L"][0], py - w["L"][1])
        dr = np.hypot(px - w["R"][0], py - w["R"][1])
        k = np.argmin(np.minimum(dl, dr))
        out.append("L" if dl[k] < dr[k] else "R")
    return np.array(out)


def turn_direction(S, n=41, drop_end=40):
    """Turn direction away from the odor port, as F16/Behavior/cs_turnFromNPDirection.m (criterion):
    the 41 position samples from odor port exit, the one furthest in x from the odor port position,
    its sign. Trials within 40 samples of the epoch end are dropped."""
    pos = S.pos
    out = []
    for t in S.trials.stop.values:
        i = int(np.searchsorted(pos.t.values, t))
        ep = S.epochs[(S.epochs[:, 0] <= t) & (S.epochs[:, 1] >= t)]
        iend = np.searchsorted(pos.t.values, ep[0, 1]) if len(ep) else len(pos)
        if i + drop_end >= iend or i + n > len(pos):
            out.append("")
            continue
        dx = pos.x.values[i : i + n] - S.geom[int(S.trials.epoch.values[len(out)])]["port"][0]
        k = np.argmax(np.abs(dx))
        out.append("L" if dx[k] < 0 else "R")
    return np.array(out)


# ----------------------------------------------------------------------------------------------
# Spikes


def count_in(spk, a, b):
    """Spike counts of one unit in intervals [a, b)."""
    return np.searchsorted(spk, b) - np.searchsorted(spk, a)


def in_epochs(spk, epochs):
    return sum(count_in(spk, e[0], e[1]) for e in epochs)


def task_responsive(spk, tr, which):
    """Methods, Task responsiveness (criterion): per odor, Wilcoxon signed-rank test of the per-trial
    rate in the sampling period against a pre-odor window of the same length ending at odor onset;
    responsive when p < 0.05 for at least one odor. `which` is a boolean mask of trials used.
    Returns the smaller p of the two odors."""
    ps = []
    for od in ("L", "R"):
        m = which & (tr.odor.values == od)
        if m.sum() < 2:
            continue
        a = tr.start.values[m]
        b = tr.stop.values[m]
        d = b - a
        post = count_in(spk, a, b) / d
        pre = count_in(spk, a - d, a) / d
        if np.all(post == pre):
            ps.append(1.0)
            continue
        ps.append(stats.wilcoxon(post, pre).pvalue)
    return min(ps) if ps else np.nan


def si(rates, labels):
    """Selectivity index (criterion; Methods, Choice selectivity): (r1 - r2)/(r1 + r2), r the mean
    over trials of each trial's rate, for odor L (r1) and odor R (r2)."""
    r1 = rates[labels == "L"].mean()
    r2 = rates[labels == "R"].mean()
    return (r1 - r2) / (r1 + r2) if (r1 + r2) > 0 else np.nan


def choice_selective(rates, labels, rng, n=1000, k=1.5):
    """SI against a null from shuffling odor labels across trials, 1000 shuffles (criterion, from
    F16/OdorSelectivitySingleCell/cs_cellSelectivityTag.m); selective when SI lies 1.5 s.d. or more
    from the null mean (criterion; Methods)."""
    s = si(rates, labels)
    null = np.array([si(rates, rng.permutation(labels)) for _ in range(n)])
    null = null[np.isfinite(null)]
    return s, bool(np.isfinite(s) and abs(s - null.mean()) >= k * null.std()), null


# ----------------------------------------------------------------------------------------------
# Spectral measures


def dpss(n, nw, k):
    return signal.windows.dpss(n, nw, Kmax=k)


def tapered_fft(x, nw, k, fs=FS_LFP):
    """x: (..., n). Returns (freqs, X) with X (..., k, nf), multitaper Fourier coefficients."""
    n = x.shape[-1]
    w = dpss(n, nw, k)
    X = np.fft.rfft(x[..., None, :] * w, axis=-1)
    return np.fft.rfftfreq(n, 1 / fs), X


def mt_power(X):
    return (np.abs(X) ** 2).mean(axis=-2)


def mt_coherence(X, Y):
    sxy = (X * np.conj(Y)).mean(axis=-2)
    sxx = (np.abs(X) ** 2).mean(axis=-2)
    syy = (np.abs(Y) ** 2).mean(axis=-2)
    return np.abs(sxy) / np.sqrt(sxx * syy)


def moving_windows(x, win, step):
    """x (c, n) -> (c, w, win) sliding windows and their centre sample indices."""
    n = x.shape[-1]
    starts = np.arange(0, n - win + 1, step)
    idx = starts[:, None] + np.arange(win)[None, :]
    return x[:, idx], starts + win // 2


def bandpass(x, band, fs=FS_LFP, order=2):
    """Zero-phase IIR band-pass (Methods, Local field potential: "band pass filtered ... using a
    zero-phase IIR filter"); a Butterworth of order 2, applied forward and backward, is an
    assumption: the order is not given."""
    return signal.sosfiltfilt(_butter(order, tuple(band), fs), x, axis=-1)


@functools.lru_cache(maxsize=None)
def _butter(order, band, fs):
    return signal.butter(order, band, btype="band", fs=fs, output="sos")


def hilbert_phase(x):
    """Phase with zero at the peak (Methods): the angle of the analytic signal is 0 at peaks."""
    return np.angle(signal.hilbert(x, axis=-1))


def rayleigh(phases):
    """Rayleigh test for non-uniformity: (p, z, mean vector length), with the usual approximation
    (Zar 1999)."""
    n = len(phases)
    if n == 0:
        return np.nan, np.nan, np.nan
    r = np.abs(np.mean(np.exp(1j * phases)))
    z = n * r**2
    p = np.exp(np.sqrt(1 + 4 * n + 4 * (n**2 - (n * r) ** 2)) - (1 + 2 * n))
    return float(min(p, 1.0)), float(z), float(r)


def tort_mi(phase, amp, nbins=18):
    """Modulation index of Tort et al. 2010 (criterion; Methods, Cross-frequency coupling): phases
    in 18 bins of 20 degrees, mean amplitude per bin normalized to sum 1, MI = KL distance to the
    uniform divided by log(nbins)."""
    b = np.minimum(((phase + np.pi) / (2 * np.pi) * nbins).astype(int), nbins - 1)
    s = np.bincount(b, weights=amp, minlength=nbins)
    c = np.bincount(b, minlength=nbins)
    m = s / np.maximum(c, 1)
    p = m / m.sum()
    p = p[p > 0]
    return float((np.log(nbins) + np.sum(p * np.log(p))) / np.log(nbins))


# ----------------------------------------------------------------------------------------------
# LFP windows


def lfp_channels(S):
    """The LFP columns used, from the electrode table and the units' tetrodes.

    - `ca1`, `pfc`: the ground-referenced ("Ref OFF") channel of every tetrode of the region with
      cells that day (criterion, LFP reading A: "all tetrodes of a region with cells"; Methods:
      "raw LFP (with respect to GND)").
    - `ob`: the ground-referenced channels of the OB tetrodes (reading A: "all OB tetrodes").
    - `main`: per region the tetrode with the most cells that day (criterion; Methods, Phase
      locking); for OB the first OB channel.
    - `ca1_local`: the locally referenced ("Ref ON") channel of each CA1 tetrode with cells, for
      ripple detection (criterion and Methods, Sharp-wave ripple detection: "the locally referenced
      LFP signal from CA1 tetrodes"; "tetrodes are the CA1 tetrodes with cells").
    """
    ch = S.channels
    u = S.units
    out = {}
    for reg in ("CA1", "PFC"):
        tets = u.tetrode[u.region == reg].value_counts()
        cols = [int(ch.col[(ch.tetrode == t) & (ch.ref == "Ref OFF")].iloc[0]) for t in tets.index if ((ch.tetrode == t) & (ch.ref == "Ref OFF")).any()]
        out[reg.lower()] = cols
        out[reg.lower() + "_main"] = cols[0] if cols else None
    ob = ch[(ch.region == "OB") & (ch.ref == "Ref OFF")]
    out["ob"] = [int(c) for c in ob.drop_duplicates("tetrode").col]
    out["ob_main"] = out["ob"][0] if out["ob"] else None
    tets = u.tetrode[u.region == "CA1"].unique()
    out["ca1_local"] = [int(ch.col[(ch.tetrode == t) & (ch.ref == "Ref ON")].iloc[0]) for t in tets if ((ch.tetrode == t) & (ch.ref == "Ref ON")).any()]
    return out


def lfp_windows(S, seed=0, n_base=60, base_len=2.0, workers=16):
    """Stream the LFP the analyses need from one session, as float32, on the columns of
    `lfp_channels` only:

    - per trial, from (odor onset - max(sampling, 0.5 s) - 1 s) to (max(odor offset, onset + 3 s)
      + 1 s): the sampling period, the pre-odor window of the same length, the 500 ms before
      onset, 3 s after onset (criterion, fig2s1e-run-theta-shift), and 1 s of padding each side
      for the 1 s spectral windows and the filters (standard choice);
    - per rewarded trial, from reward well entry - 0.5 s to exit + 1 s;
    - `n_base` windows of `base_len` s at random times in the task epochs (seeded), to estimate the
      epoch mean and s.d. used for z-scoring and for the ripple threshold (assumption: the files
      are read in windows, not whole, to keep the run within its time limit; the epoch statistics
      are estimated from 120 s of each day).
    Returns a dict with the column map and lists of (t, data) windows."""
    chans = lfp_channels(S)
    cols = sorted(set(chans["ca1"] + chans["pfc"] + chans["ob"] + chans["ca1_local"]))
    pos = {c: i for i, c in enumerate(cols)}
    tr = S.trials
    pre = np.maximum(tr.dur.values, 0.5)
    t0 = tr.start.values - pre - 1.0
    t1 = np.maximum(tr.stop.values, tr.start.values + 3.0) + 1.0
    rw = np.nonzero((tr.rewarded == 1).values & np.isfinite(tr.rend.values))[0]
    r0 = tr.rstart.values[rw] - 0.5
    r1 = tr.rend.values[rw] + 1.0
    rng = np.random.default_rng(seed)
    lens = S.epochs[:, 1] - S.epochs[:, 0] - base_len
    pick = rng.choice(len(lens), n_base, p=lens / lens.sum())
    b0 = np.sort(S.epochs[pick, 0] + rng.uniform(0, lens[pick]))
    jobs = list(zip(t0, t1)) + list(zip(r0, r1)) + list(zip(b0, b0 + base_len))
    with ThreadPoolExecutor(workers) as ex:
        res = list(ex.map(lambda ab: S.read_lfp(ab[0], ab[1], cols), jobs))
    n = len(t0)
    m = len(r0)
    return dict(
        chans=chans,
        colpos=pos,
        trial=res[:n],
        reward=dict(zip(rw.tolist(), res[n : n + m])),
        base=res[n + m :],
    )


# ----------------------------------------------------------------------------------------------
# LFP measures per session


def _dft_matrix(n, freqs, fs=FS_LFP):
    t = np.arange(n) / fs
    return np.exp(-2j * np.pi * t[:, None] * np.asarray(freqs)[None, :])


# the 1 Hz bins of 1 s windows in the two bands (criterion: beta 20 to 30 Hz, RR 7 to 8 Hz)
SPEC_FREQS = np.r_[7, 8, np.arange(20, 31)]


# the frequency grid of Chronux with its default padding (pad 0: FFT length the next power of two,
# 2048 for 1 s at 1.5 kHz), up to 20 Hz (criterion, fig2s1e: fpass 0 to 20 Hz)
THETA_FREQS = np.arange(1, 28) * FS_LFP / 2048


def _band(freqs, band):
    return (freqs >= band[0]) & (freqs <= band[1])


def lfp_measures(S, W, ripple_band=(150.0, 250.0), ripple_sd=3.0, ripple_min=0.015, speed_max=4.0):
    """All LFP-derived values of one session, from the windows of `lfp_windows`.

    Reading A (criterion, LFP pipelines; F16/LFPAnalysis): moving 1 s windows stepped by 20 ms,
    power with tapers [1 1] and coherence with tapers [2 3] (Chronux [TW K]), every region tetrode
    with cells, all cross-region pairs averaged, each z-scored per frequency to its epoch mean and
    s.d. (from the baseline windows), a window's value the mean of the spectral windows whose
    centres fall in it. Reading B (criterion; F7/ClaireCrossCoherence.m): tapers [3 5] on one 500
    ms window, the main tetrode per region, the raw LFP z-scored over the recording (mean and s.d.
    from the baseline windows).

    Returns a dict of per-trial tables and per-unit spike phases."""
    tr = S.trials
    ch = W["chans"]
    cp = W["colpos"]
    regions = {"CA1": ch["ca1"], "PFC": ch["pfc"], "OB": ch["ob"]}
    main = {"CA1": ch["ca1_main"], "PFC": ch["pfc_main"], "OB": ch["ob_main"]}
    pairs = [("CA1", "PFC"), ("CA1", "OB"), ("PFC", "OB")]
    base = W["base"]
    # ---------------- baseline statistics
    bx = np.concatenate([b[1] for b in base], axis=0)
    mu = bx.mean(0)
    sd = bx.std(0)
    win, step = 1500, 30
    tpA = dpss(win, 1, 1)
    tpC = dpss(win, 2, 3)
    D = _dft_matrix(win, SPEC_FREQS)
    Dr, Di = np.ascontiguousarray(D.real), np.ascontiguousarray(D.imag)
    tpAC = np.vstack([tpA, tpC])

    def specA(x):
        """x (n, c) -> centres (w,), power (w, c, f), coef (w, c, k, f) with tapers [2 3]."""
        xs = (x - mu[None, : x.shape[1]]) if False else x
        if xs.shape[0] < win:
            return None
        Wn, cen = moving_windows(xs.T, win, step)  # (c, w, win)
        T = Wn[:, :, None, :] * tpAC[None, None]  # (c, w, 4, win)
        F = (T @ Dr) + 1j * (T @ Di)  # (c, w, 4, f)
        P = np.abs(F[:, :, :1]) ** 2  # (c, w, 1, f)
        C = F[:, :, 1:]  # (c, w, 3, f)
        return cen, P[:, :, 0, :], C

    def coh(Ca, Cb):
        sxy = (Ca * np.conj(Cb)).mean(-2)
        return np.abs(sxy) / np.sqrt((np.abs(Ca) ** 2).mean(-2) * (np.abs(Cb) ** 2).mean(-2))

    allcols = sorted(cp, key=lambda c: cp[c])
    regidx = {r: [cp[c] for c in cols] for r, cols in regions.items()}

    # baseline spectra for z-scoring (reading A)
    bP, bCoh = [], []
    for _, b in base:
        r = specA(b.astype(np.float64))
        if r is None:
            continue
        cen, P, C = r
        bP.append(P.transpose(1, 0, 2))  # (w, c, f)
        bc = {}
        for a, bb in pairs:
            ia, ib = regidx[a], regidx[bb]
            if not ia or not ib:
                continue
            bc[(a, bb)] = np.stack([coh(C[i], C[j]) for i in ia for j in ib], 1)  # (w, npairs, f)
        bCoh.append(bc)
    bP = np.concatenate(bP, 0)
    Pmu, Psd = bP.mean(0), bP.std(0)
    Cmu, Csd = {}, {}
    for k in bCoh[0]:
        cc = np.concatenate([b[k] for b in bCoh], 0)
        Cmu[k], Csd[k] = cc.mean(0), cc.std(0)

    def A_values(cen_t, P, C, a, b):
        """Reading A, mean over spectral windows with centre in [a, b]: dict of region power and
        pair coherence spectra (z-scored), or None if no window centre falls in it."""
        m = (cen_t >= a) & (cen_t <= b)
        if not m.any():
            # the nearest centre, for windows shorter than the 20 ms step
            m = np.zeros_like(cen_t, bool)
            m[np.argmin(np.abs(cen_t - (a + b) / 2))] = True
        out = {}
        Pz = (P[:, m, :].mean(1) - Pmu) / Psd  # (c, f)
        for r, idx in regidx.items():
            if idx:
                out["pow_" + r] = Pz[idx].mean(0)
        for (ra, rb) in Cmu:
            cc = np.stack([coh(C[i][m], C[j][m]).mean(0) for i in regidx[ra] for j in regidx[rb]], 0)
            out[f"coh_{ra}-{rb}"] = ((cc - Cmu[(ra, rb)]) / Csd[(ra, rb)]).mean(0)
        return out

    # reading B helpers
    tpB = dpss(750, 3, 5)
    fB = np.fft.rfftfreq(750, 1 / FS_LFP)

    def B_values(t, x, a):
        i = np.searchsorted(t, a)
        seg = x[i : i + 750]
        if seg.shape[0] < 750:
            return None
        out = {}
        X = {}
        for r, c in main.items():
            if c is None:
                continue
            z = (seg[:, cp[c]] - mu[cp[c]]) / sd[cp[c]]
            X[r] = np.fft.rfft(z[None, :] * tpB, axis=-1)  # (5, f)
            out["pow_" + r] = (np.abs(X[r]) ** 2).mean(0)
        for ra, rb in pairs:
            if ra in X and rb in X:
                out[f"coh_{ra}-{rb}"] = coh(X[ra], X[rb])
        return out

    bandsA = {"beta": _band(SPEC_FREQS, BETA), "rr": _band(SPEC_FREQS, RR)}
    bandsB = {"beta": _band(fB, BETA), "rr": _band(fB, RR)}

    def reduce(vals, bands, prefix):
        o = {}
        if vals is None:
            return o
        for k, v in vals.items():
            for bn, bm in bands.items():
                o[f"{prefix}_{k}_{bn}"] = float(np.mean(v[bm]))
        return o

    rows = []
    phases = []  # per trial: dict region -> (t, beta phase, rr phase, beta amp)
    offs = []
    theta = []
    sp_v = S.pos
    for i, (t, x) in enumerate(W["trial"]):
        x = x.astype(np.float64)
        st, sp_, du = tr.start.values[i], tr.stop.values[i], tr.dur.values[i]
        row = dict(trial=i)
        if len(t) < 3000:  # a trial at the edge of the recorded LFP
            rows.append(row)
            phases.append((t, {}))
            offs.append(dict(trial=i))
            theta.append(dict(trial=i))
            continue
        # spectral windows only where a centre can fall in the pre-odor or sampling period
        mA = (t >= st - du - 0.55) & (t <= sp_ + 0.55)
        r = specA(x[mA])
        if r is not None:
            cen, P, C = r
            cen_t = t[mA][cen]
            row.update(reduce(A_values(cen_t, P, C, st, sp_), bandsA, "A_odor"))
            row.update(reduce(A_values(cen_t, P, C, st - du, st), bandsA, "A_pre"))
            row.update(reduce(A_values(cen_t, P, C, sp_ - 0.5, sp_), bandsA, "A_last"))
        row.update(reduce(B_values(t, x, sp_ - 0.5), bandsB, "B_last"))
        row.update(reduce(B_values(t, x, st - 0.5), bandsB, "B_pre"))
        # filtered phases on the main channels
        ph = {}
        for reg, c in main.items():
            if c is None:
                continue
            xb = bandpass(x[:, cp[c]], BETA)
            xr = bandpass(x[:, cp[c]], RR)
            ab = signal.hilbert(xb)
            ar = signal.hilbert(xr)
            ph[reg] = (np.angle(ab), np.angle(ar), np.abs(ab))
        phases.append((t, ph))
        # phase offsets (criterion, fig2s2d): circular mean of the phase difference per trial
        o = dict(trial=i)
        for win_name, a in (("whole", st), ("last", sp_ - 0.5)):
            m = (t >= a) & (t < sp_)
            for ra, rb in pairs:
                if ra in ph and rb in ph:
                    for k, bn in ((0, "beta"), (1, "rr")):
                        d = ph[ra][k][m] - ph[rb][k][m]
                        o[f"{win_name}_{ra}-{rb}_{bn}"] = float(np.angle(np.mean(np.exp(1j * d)))) if m.any() else np.nan
        offs.append(o)
        # theta shift (criterion, fig2s1e): 1 s windows, tapers [3 5], 0-20 Hz, CA1 and PFC main
        th = dict(trial=i)
        for reg in ("CA1", "PFC"):
            c = main[reg]
            if c is None:
                continue
            xs = x[:, cp[c]]
            Wn, cen = moving_windows(xs[None, :], 1500, 75)  # 50 ms step
            Pw = (np.abs((Wn[0][:, None, :] * dpss(1500, 3, 5)[None]) @ _dft_matrix(1500, THETA_FREQS)) ** 2).mean(1)
            ct = t[cen] - st
            for name, (a, b) in (("a_odor", (0.0, 0.8)), ("a_run", (0.8, 3.0))):
                m = (ct >= a) & (ct < b)
                th[f"{name}_{reg}"] = Pw[m].mean(0) if m.any() else None
            m = (ct >= 0) & (ct <= du)
            th[f"b_odor_{reg}"] = Pw[m].mean(0) if m.any() else None
            v = np.interp(t[cen], sp_v.t, sp_v.v)
            m = (t[cen] > sp_) & (v > 3.0)
            th[f"b_run_{reg}"] = Pw[m].mean(0) if m.any() else None
        theta.append(th)
        rows.append(row)
    trials = pd.DataFrame(rows)
    # ---------------- reward windows: last 500 ms before reward well exit
    rrows = []
    for i, (t, x) in W["reward"].items():
        x = x.astype(np.float64)
        re_ = tr.rend.values[i]
        row = dict(trial=i)
        if len(t) < 1500:
            rrows.append(row)
            continue
        # reading A on [exit - 0.5, exit]: spectral windows need 0.5 s of data each side
        m = (t >= re_ - 1.0) & (t <= re_ + 0.5)
        r = specA(x[m])
        if r is not None:
            cen, P, C = r
            row.update(reduce(A_values(t[m][cen], P, C, re_ - 0.5, re_), bandsA, "A_rew"))
        row.update(reduce(B_values(t, x, re_ - 0.5), bandsB, "B_rew"))
        rrows.append(row)
    rew = pd.DataFrame(rrows)
    # ---------------- ripples (criterion and Methods, Sharp-wave ripple detection)
    loc = [cp[c] for c in ch["ca1_local"]]
    rip = dict(odor=np.full(len(tr), np.nan), reward=np.full(len(tr), np.nan), odor_stop=np.full(len(tr), np.nan), reward_stop=np.full(len(tr), np.nan), odor_stop_len=np.full(len(tr), np.nan), reward_stop_len=np.full(len(tr), np.nan))
    if loc:
        env_b = np.concatenate([np.abs(signal.hilbert(bandpass(b[:, loc].T.astype(np.float64), ripple_band, order=4), axis=-1)) for _, b in base], axis=1)
        thr = env_b.mean(1) + ripple_sd * env_b.std(1)

        def events(t, x):
            if len(t) < 300:  # a window outside the recorded LFP
                return np.zeros(0)
            env = np.abs(signal.hilbert(bandpass(x[:, loc].T.astype(np.float64), ripple_band, order=4), axis=-1))
            above = (env > thr[:, None]).any(0)
            d = np.diff(np.r_[0, above.astype(int), 0])
            on, off = np.nonzero(d == 1)[0], np.nonzero(d == -1)[0]
            keep = (off - on) / FS_LFP >= ripple_min
            ev = t[np.minimum(on[keep], len(t) - 1)]
            v = np.interp(ev, sp_v.t, sp_v.v)
            return ev[v < speed_max]

        def stop_period(tt, v, t_in, lo, hi, forward=False):
            """Contiguous period with speed under 4 cm/s containing t_in, within [lo, hi]; with
            `forward`, the first such period at or after t_in (the rat is often still moving when
            it breaks the reward beam)."""
            m = (tt >= lo) & (tt <= hi)
            tt, v = tt[m], v[m]
            if not len(tt):
                return t_in, t_in
            k = np.searchsorted(tt, t_in).clip(0, len(tt) - 1)
            slow = v < speed_max
            if forward:
                while k < len(tt) - 1 and not slow[k]:
                    k += 1
            a = k
            while a > 0 and slow[a - 1]:
                a -= 1
            b = k
            while b < len(tt) - 1 and slow[b + 1]:
                b += 1
            return tt[a], tt[b]

        for i, (t, x) in enumerate(W["trial"]):
            if len(t) < 3000:
                continue
            ev = events(t, x)
            st, sp_ = tr.start.values[i], tr.stop.values[i]
            rip["odor"][i] = ((ev >= st) & (ev <= sp_)).sum()
            a, b = stop_period(sp_v.t.values, sp_v.v.values, (st + sp_) / 2, t[0] + 0.25, t[-1] - 0.25)
            a, b = min(a, st), max(b, sp_)
            rip["odor_stop"][i] = ((ev >= a) & (ev <= b)).sum()
            rip["odor_stop_len"][i] = b - a
        for i, (t, x) in W["reward"].items():
            if len(t) < 1500:
                continue
            ev = events(t, x)
            rs, re_ = tr.rstart.values[i], tr.rend.values[i]
            rip["reward"][i] = ((ev >= rs) & (ev <= re_)).sum()
            a, b = stop_period(sp_v.t.values, sp_v.v.values, rs, t[0] + 0.25, t[-1] - 0.25, forward=True)
            if b - a < 1.0:
                b = a + 1.0
            rip["reward_stop"][i] = ((ev >= a) & (ev <= b)).sum()
            rip["reward_stop_len"][i] = b - a
    # ---------------- spike phases in the sampling periods, per unit and LFP region
    sph = []
    for u, row in S.units.iterrows():
        spk = row.spikes
        rec = {"unit": u}
        for reg in main:
            if main[reg] is None:
                continue
            pb, pr, tri = [], [], []
            for i, (t, ph) in enumerate(phases):
                if reg not in ph:
                    continue
                st, sp_ = tr.start.values[i], tr.stop.values[i]
                s = spk[(spk >= st) & (spk < sp_)]
                if not len(s):
                    continue
                k = np.searchsorted(t, s).clip(0, len(t) - 1)
                pb.append(ph[reg][0][k])
                pr.append(ph[reg][1][k])
                tri.append(np.full(len(s), i))
            rec[reg] = (np.concatenate(pb) if pb else np.zeros(0), np.concatenate(pr) if pr else np.zeros(0), np.concatenate(tri).astype(int) if tri else np.zeros(0, int))
        sph.append(rec)
    # ---------------- RR phase and beta amplitude in the sampling periods, per trial (CFC)
    cfc = []
    for i, (t, ph) in enumerate(phases):
        st, sp_ = tr.start.values[i], tr.stop.values[i]
        m = (t >= st) & (t < sp_)
        cfc.append({reg: (ph[reg][1][m][::3], ph[reg][2][m][::3]) for reg in ph})
    return dict(trials=trials, reward=rew, ripples=pd.DataFrame(rip), spike_phase=sph, cfc=cfc, offsets=pd.DataFrame(offs), theta=theta, freqsA=SPEC_FREQS)


# ----------------------------------------------------------------------------------------------
# Ensembles


def logit_fit(X, y, iters=30, ridge=1e-6):
    """Binomial GLM with the logit link (the code's fitglm, criterion), fitted by Newton's method; a
    tiny ridge keeps separable folds finite (standard choice). X without the intercept column."""
    X1 = np.c_[np.ones(len(X)), X]
    w = np.zeros(X1.shape[1])
    for _ in range(iters):
        p = 1 / (1 + np.exp(-np.clip(X1 @ w, -30, 30)))
        g = X1.T @ (p - y) + ridge * w
        H = (X1 * (p * (1 - p))[:, None]).T @ X1 + ridge * np.eye(len(w))
        try:
            step = np.linalg.solve(H, g)
        except np.linalg.LinAlgError:
            break
        w -= step
        if np.abs(step).max() < 1e-6:
            break
    return w


def cv_accuracy(X, y, rng, k=5):
    """Five-fold cross-validated accuracy (Methods, GLM): trials split at random into five sets,
    four train and one tests; the fraction of test trials predicted correctly, averaged over folds."""
    n = len(y)
    order = rng.permutation(n)
    folds = np.array_split(order, k)
    acc = []
    for f in folds:
        tr = np.setdiff1d(order, f)
        w = logit_fit(X[tr], y[tr])
        pr = (np.c_[np.ones(len(f)), X[f]] @ w) > 0
        acc.append(np.mean(pr == y[f]))
    return float(np.mean(acc))


# ----------------------------------------------------------------------------------------------
# Space


def outbound_runs(S, speed_min=3.0, start_delay=0.0, nbins=100, reach=0.15):
    """Outbound runs, odor port exit to the chosen well, linearized (Methods, Occupancy maps and Place
    field determination: positions of a run "assigned to one of 100 bins from the origin to the
    destination of that route"; speed over 3 cm/s).

    The route is the T-maze skeleton of the epoch: down the stem from the odor port to the level of
    the wells, then along the arm to the chosen well. A sample's linear position is its distance
    along that path (stem progress, then arm progress once the rat is within 15 cm of the wells'
    level), divided by the path length, in 100 bins. A run ends at reward well entry on rewarded
    trials and at the first sample within `reach` of the well separation from the chosen well on
    the others (assumption: the files give no arrival time on unrewarded trials). Samples from
    `start_delay` s after exit, at speed over `speed_min`. Returns a list of dicts per trial with
    side, times, bins and sample durations."""
    tr = S.trials
    pos = S.pos
    t = pos.t.values
    dt = np.r_[np.diff(t), np.median(np.diff(t))]
    runs = []
    for i in range(len(tr)):
        side = tr.side.values[i]
        if side == "":
            continue
        g = S.geom[int(tr.epoch.values[i])]
        port, well = g["port"], g["wells"][side]
        sep = np.hypot(*(g["wells"]["R"] - g["wells"]["L"]))
        a = tr.stop.values[i]
        if tr.rewarded.values[i] == 1 and np.isfinite(tr.rstart.values[i]):
            b = tr.rstart.values[i]
        else:
            m = (t > a) & (t < a + 10)
            d = np.hypot(pos.x.values[m] - well[0], pos.y.values[m] - well[1])
            k = np.nonzero(d < reach * sep)[0]
            b = t[m][k[0]] if len(k) else a + 6.0
        m = (t >= a + start_delay) & (t <= b) & (pos.v.values > speed_min)
        if m.sum() < 2:
            continue
        x, y = pos.x.values[m], pos.y.values[m]
        stem = max(port[1] - well[1], 0.0)
        arm = abs(well[0] - port[0])
        s1 = np.clip(port[1] - y, 0, stem)
        on_arm = (port[1] - y) > stem - 15
        s2 = np.where(on_arm, np.clip(np.abs(x - port[0]), 0, arm), 0.0)
        lin = (s1 + s2) / (stem + arm)
        bins = np.minimum((lin * nbins).astype(int), nbins - 1)
        runs.append(dict(trial=i, side=side, t=t[m], bins=bins, dt=dt[m], length=stem + arm, t0=a, t1=b))
    return runs


def gauss_smooth(x, sigma=2.0, axis=-1):
    """Gaussian smoothing over bins, sigma 2 bins (Methods)."""
    from scipy.ndimage import gaussian_filter1d

    return gaussian_filter1d(x, sigma, axis=axis, mode="nearest")


def flood_width(curve, frac=0.25):
    """Width in bins of the field around the peak: contiguous bins above 25% of the peak (Methods)."""
    k = int(np.argmax(curve))
    thr = frac * curve[k]
    a = k
    while a > 0 and curve[a - 1] >= thr:
        a -= 1
    b = k
    while b < len(curve) - 1 and curve[b + 1] >= thr:
        b += 1
    return b - a + 1


def skaggs_sparsity(rate, occ):
    p = occ / occ.sum()
    num = (p * rate).sum() ** 2
    den = (p * rate**2).sum()
    return float(num / den) if den > 0 else np.nan
