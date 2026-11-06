"""Loading and measures for CRCNS ssc-7 (Yu, Gutnisky, Hires & Svoboda 2016, doi:10.1038/nn.4412).

The data set is one gzipped tar file, ``ssc-7/live/data.tar.gz`` (6.2 GB), of NWB 1.0 files, read
anonymously from the public S3 bucket ``crcnsarchive``. A gzip stream cannot be opened in place,
so the file is streamed once from the start with ``fsspec`` and ``tarfile`` (mode ``r|gz``); each
NWB member is read into memory, opened with ``h5py``, reduced to what the analysis needs and
dropped. Nothing is written to disk.

Where each parameter comes from:

- Whisker decomposition: band-pass 6 to 60 Hz, Butterworth, 4th order, Hilbert amplitude and
  phase (Online Methods, Data analysis, paragraph 2; claims file M-EPOCH). The Methods say 4th
  order; the dataset's example code (``DGMultipleDecomposition.m``) picks the order with
  ``buttord``. The Methods are followed (protocol, reader step 2). Filtering is zero-phase
  (``filtfilt``), as in that code. NaNs in the angle are linearly interpolated, as the code's
  ``naninterp`` does.
- Whisking epochs: cycles from one wrap of the phase (from +pi to -pi, the most retracted
  position) to the next whose amplitude at phase 0 exceeds 2.5 degrees, without samples within
  100 ms of a lick or within -10 to +100 ms of a touch onset (Methods; M-EPOCH).
- Nonwhisking epochs: runs of at least 100 ms with amplitude below 1.25 degrees, without touch or
  lick. Margin reading (a): the same margins as for whisking; reading (b): no margin beyond the
  absence of touch (onset to offset) and lick samples (M-EPOCH).
- Whisking onsets: the end of a nonwhisking epoch followed by a rise of the mean amplitude of at
  least 2 degrees, no touch within 250 ms; the rise is measured over the 250 ms after the onset
  (reading a) or 100 ms (reading b) against the last 100 ms of the epoch (M-EPOCH; the reference
  window is an assumption, the shortest nonwhisking epoch). In the onset Vm windows, Vm after a
  later touch is set to NaN (M-EPOCH).
- Touches: principal-whisker touch onsets and offsets as stored in the files; intertouch interval
  from the previous offset in the same trial (the first touch of a trial has no previous offset
  and is kept, as ``compute_touchNWB.m`` keeps it, where its ITI is its onset time); touches with
  ITI below the minimum are dropped (M-TOUCH).
- Spikes per touch, latency (M-TOUCH, M-LAT): as the Methods, Data analysis, paragraph 1.
- Spike removal and threshold (M-VM): threshold where dVm/dt exceeds 3 s.d. of the trial's
  dVm/dt, searched back from each stored spike time; Vm replaced by a line from 1 ms before to
  4 ms after the threshold time (Methods, Data analysis, paragraph 1). The per-trial threshold is
  a line fitted to thresholds against trial number (M-VM); where all thresholds fall in one trial
  the line is not defined and their mean is used. Variants for distance to threshold: the line
  held at its end values outside the trials with spikes, and one mean threshold per neuron.
- Drifting whole-cell trials: trials whose median Vm lies more than 20 mV from the neuron's
  median are left out of the Vm measures (``stable_trials``; an assumption after the Methods'
  rejection of recordings "with slow baseline drift (>20 mV)").
- Phase tuning (M-PHASE): equal phase bins over -pi to pi (8 or 16), sinusoid fit by least
  squares; coupling strength half the peak-to-trough of the fit.
- Spectra (M-SPEC): multitaper with 3 Slepian tapers (NW = 2, i.e. 4 Hz resolution on 500 ms),
  segments of 500 ms, mean removed, spikes removed, resampled to 4,096 Hz.
- The dataset's own ``good_trials`` mask is applied (VPM: ``good_trials_units`` for the unit and
  ``good_trials_whiskers`` for its principal whisker). This is a standard choice: the masks are
  the data set's own, undocumented, record of usable trials.
"""
from __future__ import annotations

import io
import tarfile
import time

import fsspec
import h5py
import numpy as np
from scipy import signal

BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-7/live/"
DATA_URL = BUCKET + "data.tar.gz"
DATASET_DOI = "10.6080/K0T43R01"
DATASET_VERSION = "unversioned"
# MD5 sums from ssc-7/live/checksums.md5, for the files read.
MD5 = {"data.tar.gz": "670a36de4916084ff3384d7e9450e6a8",
       "docs/yu_gutnisky_CellList.xlsx": "9b0d4c9f4749de6d30fe6a17726f4754"}

WHISKER_FS = 1000.0  # whisker video and touch annotations, 1,000 fps (Methods, Behavior)
VM_FS = 10000.0  # Vm kept at 10 kHz; 20 kHz recordings are averaged in pairs


def _s(x):
    if isinstance(x, bytes):
        return x.decode(errors="replace")
    if isinstance(x, np.ndarray):
        return [_s(v) for v in x.ravel()]
    if isinstance(x, np.bytes_):
        return bytes(x).decode(errors="replace")
    return x


def _get(h, path, default=None):
    return _s(h[path][()]) if path in h else default


def _segments(t, gap=0.5):
    """Start and stop indices of the contiguous runs of a timestamp vector."""
    br = np.flatnonzero(np.diff(t) > gap)
    starts = np.r_[0, br + 1]
    stops = np.r_[br + 1, len(t)]
    return starts, stops


def iter_members(folders=None, verbose=True):
    """Stream data.tar.gz once; yield (folder, filename, h5py.File) for every NWB member."""
    t0 = time.time()
    f = fsspec.open(DATA_URL, block_size=2 ** 22).open()
    tf = tarfile.open(fileobj=f, mode="r|gz")
    for m in tf:
        if not m.isfile() or not m.name.endswith(".nwb"):
            continue
        parts = m.name.split("/")
        folder, fname = parts[1], parts[-1]
        if folders is not None and folder not in folders:
            continue
        b = tf.extractfile(m).read()
        with h5py.File(io.BytesIO(b), "r") as h:
            yield folder, fname, h
        del b
        if verbose:
            print(f"  {time.time() - t0:6.0f} s  {folder}/{fname}", flush=True)


# ---------------------------------------------------------------------------------------------
# Reduction of one file
# ---------------------------------------------------------------------------------------------

def _whisker_series(h, vpm):
    P = h["processing/whisker/BehavioralTimeSeries"]
    out = {}
    for k in P:
        out[k] = (P[k]["timestamps"][:], P[k]["data"][:].astype(np.float32).ravel())
    return out


def reduce_file(folder, fname, h):
    """Return a list of cell dicts (one per unit) holding per-trial arrays on the whisker clock."""
    vpm = folder.startswith("VPM")
    an = h["analysis"]
    tts = an["trial_type_string"][()]
    ttm = an["trial_type_mat"][()]
    if vpm:
        ttm = ttm.T
    names = [_s(x) for x in np.ravel(tts)]
    W = _whisker_series(h, vpm)
    # trial segmentation on the whisker clock
    k0 = [k for k in W if k.startswith("touch_onset_1")][0]
    tw = W[k0][0]
    if vpm:
        n_tr = len(an["trial_start_times"][()])
        starts = np.arange(n_tr) * 5000
        stops = starts + 5000
    else:
        starts, stops = _segments(tw)
    n_tr = len(starts)
    L = int(np.max(stops - starts))

    def per_trial(x):
        a = np.full((n_tr, L), np.nan, np.float32)
        for i, (s, e) in enumerate(zip(starts, stops)):
            a[i, : e - s] = x[s:e]
        return a

    t0 = tw[starts]  # session time of each trial's first whisker frame
    if not vpm:
        # In the cortical files the whisker timestamps are the trial start in milliseconds plus
        # the time within the trial in seconds (frame spacing 0.001, trial starts 1,000 times
        # the ephys trial starts). The trial start is converted to seconds; the data check
        # shows that it then matches the start of each ephys trial.
        t0 = t0 / 1000.0
    nwh = len([k for k in W if k.startswith("touch_onset_")])
    angle = {}
    ton = {}
    toff = {}
    for w in range(1, nwh + 1):
        ka = [k for k in W if k.startswith(f"whisker_angle_{w}")]
        angle[w] = per_trial(W[ka[0]][1]) if ka else None
        ton[w] = per_trial(W[f"touch_onset_{w}"][1]) > 0.5
        toff[w] = per_trial(W[f"touch_offset_{w}"][1]) > 0.5
    meta = dict(folder=folder, file=fname, n_trials=n_tr, n_whiskers=nwh,
                subject=_get(h, "general/subject/subject_id", ""),
                notes=_get(h, "general/notes", ""),
                genotype=_get(h, "general/subject/genotype", ""),
                description=_get(h, "general/subject/description", ""),
                whisker_configuration=_get(h, "general/whisker_configuration"),
                principal_whisker=_get(h, "analysis/principal_whisker"),
                trial_type_names=names, session_id=_get(h, "general/session_id", ""))
    trial_type = np.asarray(ttm, dtype=float)
    pole_in = h["stimulus/presentation/pole_in/timestamps"][()] if "stimulus/presentation/pole_in" in h else None
    pole_out = h["stimulus/presentation/pole_out/timestamps"][()] if "stimulus/presentation/pole_out" in h else None
    ppkey = [k for k in h["stimulus/presentation"] if k.startswith("pole_pos")]
    pole_pos = h[f"stimulus/presentation/{ppkey[0]}/data"][()] if ppkey else None
    # licks: VPM on the whisker clock; cortex on the ephys clock (threshold crossings)
    lt = h["acquisition/timeseries/lick_trace"]
    ld = lt["data"][()].ravel()
    lts = lt["timestamps"][()]
    on = np.flatnonzero((ld[1:] > 0.5) & (ld[:-1] <= 0.5)) + 1
    lick_times = lts[on]
    # per-trial epoch descriptions and tags (cortex: Go/Nogo with the stimulus type, such as
    # "GoStim_constant" or "NogoStim_shift"; tags "active touch" or "passive touch")
    ep_desc, ep_tag = [], []
    if "epochs" in h:
        eps = sorted(h["epochs"], key=lambda k: float(h[f"epochs/{k}/start_time"][()]))
        for k in eps:
            ep_desc.append(_s(h[f"epochs/{k}/description"][()]) if f"epochs/{k}/description" in h else "")
            tg = _s(h[f"epochs/{k}/tags"][()]) if f"epochs/{k}/tags" in h else [""]
            ep_tag.append(tg[0] if isinstance(tg, list) else tg)
    base = dict(meta=meta, t0=t0, epoch_description=ep_desc, epoch_tag=ep_tag, angle=angle, touch_on=ton, touch_off=toff,
                trial_type=trial_type, pole_in=pole_in, pole_out=pole_out, pole_pos=pole_pos,
                lick_times=lick_times, trial_len=L)
    cells = []
    if vpm:
        U = h["processing/extracellular_units/UnitTimes"]
        pw = np.atleast_1d(an["principal_whisker"][()]).astype(int)
        gu = an["good_trials_units"][()]
        gw = an["good_trials_whiskers"][()]
        units = sorted(u for u in U if isinstance(U[u], h5py.Group))
        for j, u in enumerate(units):
            c = dict(base)
            c["meta"] = dict(meta, unit=u, unit_description=_s(U[u]["unit_description"][()]),
                             kind="VPM", pw_index=int(pw[j]))
            c["spike_times"] = U[u]["times"][()]
            c["spike_trial_ids"] = U[u]["trial_ids"][()].ravel()
            c["good"] = (gu[:, j] > 0) & (gw[:, pw[j] - 1] > 0)
            c["stim"] = np.zeros(n_tr, bool)
            c["laser"] = None
            c["vm"] = None
            cells.append(c)
        return cells
    # cortex
    c = dict(base)
    us = h["processing/spike_times/UnitTimes"]
    units = sorted(u for u in us if isinstance(us[u], h5py.Group))
    st = np.atleast_1d(us[units[0]]["times"][()]) if units else np.array([])
    udesc = _s(us[units[0]]["unit_description"][()]) if units else ""
    good = an["good_trials"][()].ravel() > 0 if "good_trials" in an else np.ones(n_tr, bool)
    stim = trial_type[:, 4] > 0 if trial_type.shape[1] > 4 else np.zeros(n_tr, bool)
    acq = h["acquisition/timeseries"]
    vkey = "membrane_potential" if "membrane_potential" in acq else "juxta_potential"
    te = acq[vkey]["timestamps"][()]
    es, ee = _segments(te)
    n_e = len(es)
    ephys_fs = 1.0 / np.median(np.diff(te[: min(len(te), 10000)]))
    # laser and current per trial, as 1 ms maxima / means on the ephys clock, relative to t0
    lasers = {}
    for k in h["stimulus/presentation"]:
        if not k.startswith("photostim"):
            continue
        d = h[f"stimulus/presentation/{k}/data"][()].ravel()
        lasers[k] = d
    cur = acq["current"]["data"][()].ravel() if "current" in acq else None
    ex_lambda = {}
    if "general/optogenetics" in h:
        for s in h["general/optogenetics"]:
            ex_lambda[s] = (_get(h, f"general/optogenetics/{s}/excitation_lambda"),
                            _get(h, f"general/optogenetics/{s}/location"))
    sites = {k: _get(h, f"stimulus/presentation/{k}/site") for k in lasers}
    whole_cell = "whole_cell" in folder or vkey == "membrane_potential" and "loose" not in folder
    step = max(1, int(round(ephys_fs / VM_FS)))
    ms = int(round(ephys_fs / 1000))
    laser_ms = {k: np.zeros((n_tr, L), np.float32) for k in lasers}
    # light onset and offset of each trial at the ephys sampling rate (s, whisker clock)
    laser_on = {k: np.full((n_tr, 2), np.nan) for k in lasers}
    cur_ms = np.full((n_tr, L), np.nan, np.float32) if cur is not None else None
    vm = [] if "whole_cell" in folder else None
    vm_t0 = np.full(n_tr, np.nan)
    for i in range(min(n_tr, n_e)):
        s, e = es[i], ee[i]
        tt = te[s:e]
        off = tt[0] - t0[i]  # ephys start relative to the whisker trial start
        vm_t0[i] = off
        # 1 ms bins on the whisker clock
        nb = (e - s) // ms
        idx0 = int(round(off * 1000))
        for k, d in lasers.items():
            x = d[s:s + nb * ms].reshape(nb, ms).max(1)
            a0, b0 = max(0, idx0), min(L, idx0 + nb)
            if b0 > a0:
                laser_ms[k][i, a0:b0] = x[a0 - idx0:b0 - idx0]
            above = np.flatnonzero(d[s:e] > 0.05)
            if len(above):
                laser_on[k][i] = (tt[above[0]] - t0[i], tt[above[-1]] - t0[i])
        if cur is not None:
            x = cur[s:s + nb * ms].reshape(nb, ms).mean(1)
            a0, b0 = max(0, idx0), min(L, idx0 + nb)
            if b0 > a0:
                cur_ms[i, a0:b0] = x[a0 - idx0:b0 - idx0]
        if vm is not None:
            v = acq[vkey]["data"][s:e].astype(np.float32)
            if step > 1:
                n2 = len(v) // step
                v = v[: n2 * step].reshape(n2, step).mean(1)
            vm.append(v)
    # Every ephys trial, including any beyond the whisker trials (those are not paired with a
    # whisker trial and are not analysed): start time, and for whole-cell files the trial's median
    # Vm and largest injected current, so that depolarized trials can be found.
    e_med = np.full(n_e, np.nan)
    e_cur = np.full(n_e, np.nan)
    if vm is not None:
        for i in range(n_e):
            s, e = es[i], ee[i]
            e_med[i] = float(np.median(acq[vkey]["data"][s:e]))
            if cur is not None:
                e_cur[i] = float(np.max(np.abs(cur[s:e])))
    c["ephys_trials"] = dict(start=te[es], median_vm=e_med, max_abs_current=e_cur)
    c["meta"] = dict(meta, unit_description=udesc, kind=folder, ephys_fs=ephys_fs,
                     n_ephys_trials=n_e, vm_key=vkey, lasers=sites, opto_sites=ex_lambda,
                     location=_get(h, "general/intracellular_ephys/whole_cell_1/location", ""))
    c["spike_times"] = st
    c["good"] = good
    c["stim"] = stim
    c["laser"] = laser_ms
    c["laser_on"] = laser_on
    c["current"] = cur_ms
    c["vm"] = vm
    c["vm_t0"] = vm_t0
    return [c]


CELL_LIST_URL = BUCKET + "docs/yu_gutnisky_CellList.xlsx"


def read_cell_list():
    """The data set's cell list (sheet AllCellsReported): one row per cell with its section
    heading (such as "Whole-cell units" or "Extracellular units"), depth, mouse and mouse type.
    Streamed from the bucket, not saved."""
    import pandas as pd
    with fsspec.open(CELL_LIST_URL).open() as f:
        raw = pd.read_excel(io.BytesIO(f.read()), sheet_name="AllCellsReported", header=None)
    rows, section = [], ""
    for r in raw.itertuples(index=False):
        name = r[0]
        if not isinstance(name, str) and not np.isfinite(name if isinstance(name, float) else 0):
            continue
        name = str(name).strip()
        if name == "cell" or name == "nan":
            continue
        if r[3] is None or (isinstance(r[3], float) and not np.isfinite(r[3])):
            if not name.startswith("ANM"):
                section = name.rstrip(":")
                continue
        rows.append(dict(section=section, cell=name, depth=r[1], mouse=r[3], mouse_type=r[4]))
    return pd.DataFrame(rows)


def load(folders=None, verbose=True):
    """Stream the archive once and return the reduced cells of the folders asked for."""
    cells = []
    failed = []
    for folder, fname, h in iter_members(folders, verbose=verbose):
        try:
            cells.extend(reduce_file(folder, fname, h))
        except Exception as e:  # reported, never silent
            failed.append((folder, fname, repr(e)))
            print(f"  could not read {folder}/{fname}: {e!r}")
    load.failed = failed
    return cells


# ---------------------------------------------------------------------------------------------
# Per-trial event tables
# ---------------------------------------------------------------------------------------------

PW_READING = "code"


def pw_index(c):
    """Index (1-based) of the principal whisker's tracked series.

    VPM: the file's per-unit ``principal_whisker``. Cortex: the files do not say which tracked
    series is the principal whisker. Reading "code" (the default, an assumption): series 1, as the
    data set's example code ``ConvertfromNWB.m`` sets ``mainwid = 0`` (the first whisker) for
    every file. Reading "config": the position of ``analysis/principal_whisker`` in
    ``general/whisker_configuration``. The data check shows the touch responses under both.
    """
    m = c["meta"]
    if m.get("kind") == "VPM":
        return m["pw_index"]
    nw = m["n_whiskers"]
    if nw == 1 or PW_READING == "code":
        return 1
    conf = [x.upper() for x in np.atleast_1d(m["whisker_configuration"])]
    pw = np.atleast_1d(m["principal_whisker"])[0].upper()
    if pw in conf and conf.index(pw) < nw:
        return conf.index(pw) + 1
    return 1


def spikes_by_trial(c):
    """Spike times relative to each trial's first whisker frame, as a list of arrays."""
    t0 = c["t0"]
    st = c["spike_times"]
    out = []
    if c["meta"].get("kind") == "VPM":
        ids = c["spike_trial_ids"]
        for i in range(len(t0)):
            out.append(st[ids == i + 1] - t0[i])
        return out
    edges = np.r_[t0, np.inf]
    for i in range(len(t0)):
        s = st[(st >= edges[i] - 0.5) & (st < edges[i + 1] - 0.5)] - t0[i]
        out.append(s)
    return out


def licks_by_trial(c):
    t0 = c["t0"]
    lt = c["lick_times"]
    edges = np.r_[t0, np.inf]
    return [lt[(lt >= edges[i] - 0.5) & (lt < edges[i + 1] - 0.5)] - t0[i] for i in range(len(t0))]


def touches(c, w=None):
    """Per-trial list of (onset_s, offset_s) arrays for whisker w (principal by default)."""
    w = w or pw_index(c)
    on, off = c["touch_on"][w], c["touch_off"][w]
    out = []
    for i in range(on.shape[0]):
        a = np.flatnonzero(on[i]) / WHISKER_FS
        b = np.flatnonzero(off[i]) / WHISKER_FS
        # pair each onset with the first offset at or after it
        bo = np.array([b[b >= x][0] if np.any(b >= x) else np.nan for x in a])
        out.append((a, bo))
    return out


def touch_table(c, min_iti=0.025, trials=None, t_end=4.9):
    """Touch onsets (trial, onset s) with ITI >= min_iti; the first touch of a trial is kept.

    The first touch of a trial tagged "passive touch" is left out, as ``compute_touchNWB.m``
    leaves it out (only active touches are analysed).
    """
    rows = []
    T = touches(c)
    tags = c.get("epoch_tag") or []
    for i, (a, b) in enumerate(T):
        if trials is not None and not trials[i]:
            continue
        passive = i < len(tags) and "passive" in str(tags[i])
        for k in range(len(a)):
            if k == 0 and passive:
                continue
            iti = a[k] if k == 0 else a[k] - b[k - 1]
            if not np.isfinite(iti) or iti < min_iti:
                continue
            if a[k] > t_end:
                continue
            rows.append((i, a[k]))
    return np.array(rows, dtype=float).reshape(-1, 2)


# ---------------------------------------------------------------------------------------------
# Whisking decomposition and epochs
# ---------------------------------------------------------------------------------------------

_BA = signal.butter(4, [6.0, 60.0], btype="bandpass", fs=WHISKER_FS)


def decompose(angle_row):
    x = np.asarray(angle_row, float)
    n = np.isfinite(x)
    if n.sum() < 200:
        return None, None
    last = np.flatnonzero(n)[-1] + 1
    x = x[:last]
    n = n[:last]
    if not n.all():
        x = np.interp(np.arange(len(x)), np.flatnonzero(n), x[n])
    bp = signal.filtfilt(*_BA, x)
    hb = signal.hilbert(bp)
    return np.abs(hb), np.angle(hb)


def _runs(mask):
    m = np.r_[False, mask, False]
    d = np.diff(m.astype(int))
    return np.flatnonzero(d == 1), np.flatnonzero(d == -1)


def trial_epochs(c, i, amp, phase, licks, tch, margin="a"):
    """Whisking cycles and nonwhisking runs (sample index pairs on the 1 ms clock) of trial i."""
    n = len(amp)
    excl = np.zeros(n, bool)
    for t in licks:
        k = int(round(t * 1000))
        excl[max(0, k - 100):min(n, k + 101)] = True
    a, b = tch
    for x in a:
        k = int(round(x * 1000))
        excl[max(0, k - 10):min(n, k + 101)] = True
    # touch contact itself (onset to offset)
    contact = np.zeros(n, bool)
    for x, y in zip(a, b):
        k0 = int(round(x * 1000))
        k1 = int(round(y * 1000)) if np.isfinite(y) else k0 + 1
        contact[max(0, k0):min(n, k1 + 1)] = True
    lickm = np.zeros(n, bool)
    for t in licks:
        k = int(round(t * 1000))
        if 0 <= k < n:
            lickm[k] = True
    wraps = np.flatnonzero(np.diff(phase) < -np.pi) + 1
    whisk = []
    for s, e in zip(wraps[:-1], wraps[1:]):
        k = s + np.argmin(np.abs(phase[s:e]))
        if amp[k] > 2.5 and not excl[s:e].any():
            whisk.append((s, e))
    low = amp < 1.25
    if margin == "a":
        ok = low & ~excl & ~contact
    else:
        ok = low & ~contact & ~lickm
    s0, e0 = _runs(ok)
    nonw = [(s, e) for s, e in zip(s0, e0) if e - s >= 100]
    return whisk, nonw


def onsets(amp, nonw, tch, rise=0.250):
    """Whisking onsets: ends of nonwhisking epochs followed by a >= 2 degree rise of mean amplitude
    over `rise` s against the last 100 ms of the epoch, with no touch within 250 ms."""
    out = []
    a = tch[0]
    n = len(amp)
    for s, e in nonw:
        r = int(rise * 1000)
        if e + r > n:
            continue
        if np.nanmean(amp[e:e + r]) - np.nanmean(amp[max(s, e - 100):e]) < 2.0:
            continue
        if np.any((a * 1000 >= e) & (a * 1000 < e + 250)):
            continue
        out.append(e)
    return out


def cell_epochs(c, trials=None, margin="a", rise=0.250):
    """Decompose every selected trial; return per-trial dicts with amp, phase, epochs."""
    w = pw_index(c)
    ang = c["angle"][w]
    T = touches(c, w)
    Lk = licks_by_trial(c)
    out = {}
    for i in range(ang.shape[0]):
        if trials is not None and not trials[i]:
            continue
        amp, ph = decompose(ang[i])
        if amp is None:
            continue
        wh, nw = trial_epochs(c, i, amp, ph, Lk[i], T[i], margin)
        out[i] = dict(amp=amp, phase=ph, whisk=wh, nonw=nw, onsets=onsets(amp, nw, T[i], rise),
                      onsets_b=onsets(amp, nw, T[i], 0.100))
    return out


def epoch_rates(spk, ep, kind):
    """Per-epoch (count, duration s) for 'whisk' or 'nonw' across trials."""
    rows = []
    for i, d in ep.items():
        s = spk[i]
        for a, b in d[kind]:
            n = np.sum((s >= a / 1000) & (s < b / 1000))
            rows.append((i, n, (b - a) / 1000))
    return np.array(rows, float).reshape(-1, 3)


def rate_readings(rows):
    """(a) total spikes over total time; (b) mean of per-epoch rates."""
    if len(rows) == 0 or rows[:, 2].sum() == 0:
        return np.nan, np.nan
    return rows[:, 1].sum() / rows[:, 2].sum(), np.mean(rows[:, 1] / rows[:, 2])


def per_trial_rates(rows, n_trials):
    """Per-trial rate within the epochs of one kind (reading b of M-SIG)."""
    cnt = np.zeros(n_trials)
    dur = np.zeros(n_trials)
    for i, n, d in rows:
        cnt[int(i)] += n
        dur[int(i)] += d
    ok = dur > 0
    return cnt[ok] / dur[ok]


# ---------------------------------------------------------------------------------------------
# Touch responses
# ---------------------------------------------------------------------------------------------

def touch_psth(spk, tt, pre=0.1, post=0.1):
    """Spike counts in 1 ms bins from -pre to +post around each touch; returns (n_touch, bins)."""
    nb = int(round((pre + post) * 1000))
    out = np.zeros((len(tt), nb))
    for j, (i, t) in enumerate(tt):
        s = spk[int(i)] - t
        s = s[(s >= -pre) & (s < post)]
        out[j] = np.histogram(s, bins=nb, range=(-pre, post))[0]
    return out


def spikes_per_touch(spk, tt, kind="cortex5"):
    if len(tt) == 0:
        return np.nan
    if kind == "vpm":
        a, b, c0, d0, k = 0, 0.025, -0.025, 0, 1
    elif kind == "cortex5":
        a, b, c0, d0, k = 0, 0.050, -0.025, 0, 2
    elif kind == "cortex8":
        a, b, c0, d0, k = 0.004, 0.020, -0.016, 0, 1
    n_post = []
    n_pre = []
    for i, t in tt:
        s = spk[int(i)] - t
        n_post.append(np.sum((s >= a) & (s < b)))
        n_pre.append(np.sum((s >= c0) & (s < d0)))
    return np.mean(n_post) - k * np.mean(n_pre)


def spike_latency(psth_counts, n_touch, pre=0.1, centre=False):
    """M-LAT on a 1 ms PSTH (counts summed over touches). Returns latency ms or nan (excluded).

    The latency is the left edge of the first bin after the crossing; with ``centre`` it is the
    bin's centre (0.5 ms later), a variant: the paper does not say which edge it reports."""
    rate = psth_counts / n_touch * 1000.0
    z = int(round(pre * 1000))
    if rate[z:z + 100].max() < 10:
        return np.nan
    d = np.diff(rate)  # d[k] = rate[k+1] - rate[k]
    base = d[z - 25:z - 1]
    thr = 3 * np.std(base)
    post = d[z:z + 100]
    k = np.flatnonzero(post > thr)
    if len(k) == 0:
        return np.nan
    return float(k[0] + 1) + (0.5 if centre else 0.0)


def response_duration(psth_counts, n_touch, pre=0.1):
    """Reading of M-LAT for the VPM duration: time between the rise and fall crossings of
    baseline + 25% of (peak - baseline), on the 1 ms PSTH (ms)."""
    rate = psth_counts / n_touch * 1000.0
    z = int(round(pre * 1000))
    base = rate[z - 25:z].mean()
    seg = rate[z:z + 50]
    p = np.argmax(seg)
    lev = base + 0.25 * (seg[p] - base)
    a = p
    while a > 0 and seg[a - 1] >= lev:
        a -= 1
    b = p
    while b < len(seg) - 1 and seg[b + 1] >= lev:
        b += 1
    return float(b - a + 1)


# ---------------------------------------------------------------------------------------------
# Membrane potential
# ---------------------------------------------------------------------------------------------

def remove_spikes(v, spk_rel, fs=VM_FS):
    """Spike thresholds and spike-removed Vm of one trial (M-VM).

    For each stored spike time, the threshold is the last time before the spike peak at which
    dVm/dt rises above 3 s.d. of the trial's dVm/dt (searched back up to 3 ms); Vm is replaced by
    a line from 1 ms before to 4 ms after that time.
    """
    v = np.asarray(v, float).copy()
    if len(spk_rel) == 0:
        return v, np.array([]), np.array([])
    dv = np.gradient(v) * fs
    sd = np.nanstd(dv)
    thr_v, thr_i = [], []
    n = len(v)
    for t in spk_rel:
        k = int(round(t * fs))
        if k < 40 or k >= n - 50:
            continue
        lo = max(1, k - int(0.003 * fs))
        seg = dv[lo:k + int(0.001 * fs)]
        above = seg > 3 * sd
        if not above.any():
            continue
        j = np.flatnonzero(above)[0] + lo
        # walk back to the crossing start
        thr_i.append(j)
        thr_v.append(v[j])
    for j in thr_i:
        a = max(0, j - int(0.001 * fs))
        b = min(n - 1, j + int(0.004 * fs))
        v[a:b + 1] = np.linspace(v[a], v[b], b - a + 1)
    return v, np.array(thr_v), np.array(thr_i)


def prep_vm(c):
    """Spike-removed Vm per trial, thresholds per spike, and the per-trial threshold line."""
    spk = spikes_by_trial(c)
    vm_nospk, thr_all, thr_trial = [], [], []
    for i, v in enumerate(c["vm"]):
        off = c["vm_t0"][i]
        s = spk[i] - off if i < len(spk) else np.array([])
        s = s[(s >= 0) & (s < len(v) / VM_FS)]
        vn, tv, ti = remove_spikes(v, s)
        vm_nospk.append(vn.astype(np.float32))
        thr_all.append(tv)
        thr_trial.append(np.full(len(tv), i))
    tv = np.concatenate(thr_all) if thr_all else np.array([])
    tr = np.concatenate(thr_trial) if thr_trial else np.array([])
    n = len(c["vm"])
    if len(tv) >= 2 and len(np.unique(tr)) >= 2:
        p = np.polyfit(tr, tv, 1)
        line = np.polyval(p, np.arange(n))
        # Variant: the line is used only over the trials it was fitted on, and held at its end
        # values before the first and after the last trial with a spike (an assumption; the
        # Methods do not say how the line is used far from any spike).
        clamped = np.polyval(p, np.clip(np.arange(n), tr.min(), tr.max()))
        slope = float(p[0])
    elif len(tv) >= 1:
        line = clamped = np.full(n, float(np.mean(tv)))
        slope = 0.0
    else:
        line = clamped = np.full(n, -42.0)
        slope = np.nan
    const = np.full(n, float(np.mean(tv)) if len(tv) else -42.0)  # variant: one threshold per neuron
    return dict(vm=vm_nospk, thr=tv, thr_trial=tr, thr_line=line, thr_clamped=clamped, thr_const=const,
                thr_slope=slope, thr_trial_range=(int(tr.min()), int(tr.max())) if len(tr) else (-1, -1))


def stable_trials(c, max_dev=20.0):
    """Whole-cell trials whose median Vm lies within `max_dev` mV of the median over the neuron's
    trials. The Methods reject depolarized recordings "with slow baseline drift (>20 mV)" (Barrel
    cortex recordings, paragraph 3); the same 20 mV is applied here per trial, to leave out trials
    far from the neuron's usual Vm (such as the first trials of JY1139, near 0 mV while it fires).
    This is an assumption: the paper gives no trial-level rule."""
    if c["vm"] is None:
        return np.ones(c["meta"]["n_trials"], bool)
    med = np.array([float(np.median(v)) if len(v) else np.nan for v in c["vm"]])
    ok = np.abs(med - np.nanmedian(med)) <= max_dev
    out = np.zeros(c["meta"]["n_trials"], bool)
    out[: len(ok)] = ok
    return out


def vm_at(c, vmn, i, t_whisker_s):
    """Index into the Vm of trial i of a time on the whisker clock (s)."""
    return int(round((t_whisker_s - c["vm_t0"][i]) * VM_FS))


def touch_vm(c, vmn, tt, pre=0.05, post=0.1):
    """Touch-aligned spike-removed Vm (n_touch, samples) at 10 kHz."""
    a = int(pre * VM_FS)
    b = int(post * VM_FS)
    out = []
    for i, t in tt:
        i = int(i)
        if i >= len(vmn):
            continue
        k = vm_at(c, vmn, i, t)
        v = vmn[i]
        if k - a < 0 or k + b > len(v):
            continue
        out.append(v[k - a:k + b])
    return np.array(out).reshape(-1, a + b)


def vm_latency(avg, pre=0.05, fs=VM_FS):
    """M-LAT for Vm: first time after onset that dVm/dt exceeds 3 s.d. of dVm/dt 0-25 ms before."""
    z = int(pre * fs)
    d = np.gradient(avg) * fs
    base = d[z - int(0.025 * fs):z]
    thr = np.mean(base) + 3 * np.std(base)
    k = np.flatnonzero(d[z:z + int(0.05 * fs)] > thr)
    return np.nan if len(k) == 0 else 1000.0 * k[0] / fs


def psp_amplitude(avg, pre=0.05, win=0.05, fs=VM_FS):
    z = int(pre * fs)
    base = avg[z - int(0.005 * fs):z].mean()
    seg = avg[z:z + int(win * fs)]
    k = int(np.argmax(seg))
    return seg[k] - base, k / fs * 1000.0, base


def half_width(avg, pre=0.05, fs=VM_FS):
    z = int(pre * fs)
    base = avg[z - int(0.005 * fs):z].mean()
    seg = avg[z:z + int(0.1 * fs)] - base
    p = int(np.argmax(seg[: int(0.05 * fs)]))
    h = seg[p] / 2
    a = p
    while a > 0 and seg[a - 1] >= h:
        a -= 1
    b = p
    while b < len(seg) - 1 and seg[b + 1] >= h:
        b += 1
    return (b - a + 1) / fs * 1000.0


def epoch_vm(c, vmn, ep, kind, trials=None):
    """All spike-removed Vm samples (10 kHz) within the epochs of one kind, concatenated."""
    out = []
    for i, d in ep.items():
        if i >= len(vmn):
            continue
        v = vmn[i]
        for a, b in d[kind]:
            ka = vm_at(c, vmn, i, a / 1000)
            kb = vm_at(c, vmn, i, b / 1000)
            if ka < 0 or kb > len(v) or kb <= ka:
                continue
            out.append(v[ka:kb])
    return np.concatenate(out) if out else np.array([])


def onset_vm_change(c, vmn, ep, which="onsets", tch=None):
    """Per onset: mean Vm 100-300 ms after minus mean 0-200 ms before (Supplementary Fig. 4).

    Vm after a later touch is set to NaN (M-EPOCH, "data after a later touch are set to NaN");
    `tch` is the per-trial list of (onsets, offsets) from ``touches``. An onset whose 100 to
    300 ms window is wholly after a touch is left out."""
    out = []
    for i, d in ep.items():
        if i >= len(vmn):
            continue
        v = vmn[i]
        on = tch[i][0] if tch is not None else np.array([])
        for e in d[which]:
            k = vm_at(c, vmn, i, e / 1000)
            a, b = k - int(0.2 * VM_FS), k + int(0.3 * VM_FS)
            if a < 0 or b > len(v):
                continue
            pre = v[a:k].mean()
            post = v[k + int(0.1 * VM_FS):b].astype(float)
            later = on[on * 1000 > e]
            if len(later):
                kt = vm_at(c, vmn, i, later[0]) - (k + int(0.1 * VM_FS))
                if kt <= 0:
                    continue
                post[kt:] = np.nan
            out.append((pre, np.nanmean(post)))
    return np.array(out).reshape(-1, 2)


# ---------------------------------------------------------------------------------------------
# Phase tuning and spectra
# ---------------------------------------------------------------------------------------------

def phase_fit(ph, y, nbins=8, harmonic=False):
    """Bin y by phase and fit a sinusoid (and optionally a second harmonic); return
    (r2, coupling strength, preferred phase, binned means)."""
    edges = np.linspace(-np.pi, np.pi, nbins + 1)
    cen = (edges[:-1] + edges[1:]) / 2
    idx = np.clip(np.digitize(ph, edges) - 1, 0, nbins - 1)
    m = np.array([np.mean(y[idx == k]) if np.any(idx == k) else np.nan for k in range(nbins)])
    ok = np.isfinite(m)
    cols = [np.ones(nbins), np.cos(cen), np.sin(cen)]
    if harmonic:
        cols += [np.cos(2 * cen), np.sin(2 * cen)]
    X = np.column_stack(cols)[ok]
    beta, *_ = np.linalg.lstsq(X, m[ok], rcond=None)
    fit = X @ beta
    ss_res = np.sum((m[ok] - fit) ** 2)
    ss_tot = np.sum((m[ok] - m[ok].mean()) ** 2)
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else np.nan
    g = np.linspace(-np.pi, np.pi, 721)
    G = [np.ones_like(g), np.cos(g), np.sin(g)]
    if harmonic:
        G += [np.cos(2 * g), np.sin(2 * g)]
    fg = np.column_stack(G) @ beta
    return r2, (fg.max() - fg.min()) / 2, g[np.argmax(fg)], m


def spike_phase_data(spk, ep):
    """Phase at each spike and occupancy within whisking epochs; returns (phase per ms, spikes per ms)."""
    ph, y = [], []
    for i, d in ep.items():
        s = spk[i]
        cnt = np.histogram(s, bins=len(d["phase"]), range=(0, len(d["phase"]) / 1000))[0]
        for a, b in d["whisk"]:
            ph.append(d["phase"][a:b])
            y.append(cnt[a:b] * 1000.0)
    if not ph:
        return np.array([]), np.array([])
    return np.concatenate(ph), np.concatenate(y)


def vm_phase_data(c, vmn, ep):
    ph, y = [], []
    for i, d in ep.items():
        if i >= len(vmn):
            continue
        v = vmn[i]
        for a, b in d["whisk"]:
            ka = vm_at(c, vmn, i, a / 1000)
            kb = ka + (b - a) * 10
            if ka < 0 or kb > len(v):
                continue
            vv = v[ka:kb].reshape(b - a, 10).mean(1)
            ph.append(d["phase"][a:b])
            y.append(vv)
    if not ph:
        return np.array([]), np.array([])
    return np.concatenate(ph), np.concatenate(y)


def segments_500ms(c, vmn, ep, kind):
    """Non-overlapping 500 ms Vm segments inside epochs of one kind (whisking epochs are merged
    when consecutive cycles touch), resampled to 4,096 Hz, mean removed."""
    segs = []
    for i, d in ep.items():
        if i >= len(vmn):
            continue
        v = vmn[i]
        runs = []
        for a, b in d[kind]:
            if runs and a <= runs[-1][1]:
                runs[-1][1] = b
            else:
                runs.append([a, b])
        for a, b in runs:
            t = a
            while t + 500 <= b:
                ka = vm_at(c, vmn, i, t / 1000)
                kb = ka + 5000
                if ka >= 0 and kb <= len(v):
                    x = signal.resample(v[ka:kb], 2048)
                    segs.append(x - x.mean())
                t += 500
    return np.array(segs).reshape(-1, 2048)


_TAPERS = signal.windows.dpss(2048, NW=2.0, Kmax=3)


def multitaper(segs, fs=4096.0):
    """Mean power over segments and tapers; jackknife 95% interval over segments x tapers."""
    if len(segs) == 0:
        return None
    X = np.fft.rfft(segs[:, None, :] * _TAPERS[None], axis=-1)
    P = (np.abs(X) ** 2) / fs
    f = np.fft.rfftfreq(2048, 1 / fs)
    P = P.reshape(-1, P.shape[-1])
    m = P.mean(0)
    n = P.shape[0]
    if n > 2:
        loo = (P.sum(0)[None] - P) / (n - 1)
        lm = np.log(loo)
        se = np.sqrt((n - 1) / n * np.sum((lm - lm.mean(0)) ** 2, 0))
        lo, hi = np.exp(np.log(m) - 1.96 * se), np.exp(np.log(m) + 1.96 * se)
    else:
        lo = hi = m * np.nan
    return f, m, lo, hi


# ---------------------------------------------------------------------------------------------
# Cell groups and per-cell spike summary
# ---------------------------------------------------------------------------------------------

def group(c):
    """Cell group from the data set's folder (the folder names are the data set's own labels)."""
    f = c["meta"]["folder"]
    return {"VPM_silicon_probe": "VPM", "L4E_whole_cell": "L4E_wc", "L4E_loose_seal": "L4E_ca",
            "L4FS_whole_cell": "FS_wc", "L4FS_loose_seal": "FS_ca",
            "L4E_whole_cell_ION_cut": "L4E_ion", "L4FS_loose_seal_ION_cut": "FS_ion"}[f]


def cell_name(c):
    m = c["meta"]
    if m.get("kind") == "VPM":
        return m["unit_description"].split("#")[-1].strip()
    return m["file"].replace(".nwb", "")


def laser_power(c, i, key=None):
    """Peak laser power (mW) in trial i over the whisker period, all photostimulus series or one."""
    if not c["laser"]:
        return 0.0
    ks = [key] if key else list(c["laser"])
    return float(max(np.nanmax(c["laser"][k][i]) for k in ks))


def control_trials(c):
    """Good trials without photostimulation (the Stimtrials flag and no laser above 0.05 mW)."""
    g = c["good"].copy()
    if c["laser"]:
        lp = np.array([laser_power(c, i) for i in range(len(g))])
        g &= ~c["stim"] & (lp < 0.05)
    return g


def spike_summary(c, trials=None, margin="a", rise=0.250, min_iti=0.025, nbins=(8, 16)):
    """Rates in epochs, spikes per touch, touch PSTH and latency, and phase fits for one cell."""
    if trials is None:
        trials = control_trials(c)
    spk = spikes_by_trial(c)
    ep = cell_epochs(c, trials, margin, rise)
    w = epoch_rates(spk, ep, "whisk")
    n = epoch_rates(spk, ep, "nonw")
    out = dict(name=cell_name(c), group=group(c), n_trials=int(trials.sum()),
               whisk_s=w[:, 2].sum() if len(w) else 0.0, nonw_s=n[:, 2].sum() if len(n) else 0.0,
               n_whisk_epochs=len(w), n_nonw_epochs=len(n))
    out["whisk_a"], out["whisk_b"] = rate_readings(w)
    out["nonw_a"], out["nonw_b"] = rate_readings(n)
    out["w_rows"], out["n_rows"] = w, n
    out["w_trial"] = per_trial_rates(w, len(trials))
    out["n_trial"] = per_trial_rates(n, len(trials))
    tt = touch_table(c, min_iti, trials)
    out["n_touch"] = len(tt)
    kind = "vpm" if c["meta"].get("kind") == "VPM" else "cortex5"
    out["spt"] = spikes_per_touch(spk, tt, kind)
    ps = touch_psth(spk, tt)
    out["psth"] = ps.sum(0)
    out["latency"] = spike_latency(out["psth"], max(1, len(tt))) if len(tt) else np.nan
    out["duration"] = response_duration(out["psth"], max(1, len(tt))) if len(tt) else np.nan
    ph, y = spike_phase_data(spk, ep)
    for nb in nbins:
        if len(ph) > 100:
            out[f"phase{nb}"] = phase_fit(ph, y, nb)
            out[f"phase{nb}h"] = phase_fit(ph, y, nb, harmonic=True)
        else:
            out[f"phase{nb}"] = out[f"phase{nb}h"] = (np.nan, np.nan, np.nan, None)
    out["ep"] = ep
    out["spk"] = spk
    out["tt"] = tt
    return out


def vm_summary(c, trials=None, margin="a", min_iti=0.025, drop_drift=True):
    """Vm measures of one whole-cell neuron (M-VM, M-LAT, M-DTT, M-PHASE), control trials.

    With ``drop_drift`` (the default), trials far from the neuron's usual Vm are left out
    (``stable_trials``)."""
    if trials is None:
        trials = control_trials(c)
    trials = trials & (np.arange(len(trials)) < len(c["vm"]))
    if drop_drift:
        trials = trials & stable_trials(c)
    P = prep_vm(c)
    vmn = P["vm"]
    ep = cell_epochs(c, trials, margin)
    out = dict(name=cell_name(c), group=group(c), n_trials=int(trials.sum()),
               n_spikes_thr=len(P["thr"]), thr_slope=P["thr_slope"], thr_trial_range=P["thr_trial_range"])
    out["thr_mean"] = float(np.mean(P["thr"])) if len(P["thr"]) else np.nan
    nw = epoch_vm(c, vmn, ep, "nonw")
    wv = epoch_vm(c, vmn, ep, "whisk")
    out["rest_a"] = float(np.mean(nw)) if len(nw) else np.nan
    # reading (b): median Vm outside touch (-10 to 100 ms around touch onsets excluded) in the
    # whisker period of the selected trials
    T = touches(c)
    rest_b = []
    for i in ep:
        v = vmn[i]
        m = np.ones(len(v), bool)
        k0 = vm_at(c, vmn, i, 0.0)
        k1 = vm_at(c, vmn, i, 5.0)
        m[:max(0, k0)] = False
        m[k1:] = False
        for x in T[i][0]:
            k = vm_at(c, vmn, i, x)
            m[max(0, k - 100):k + 1000] = False
        rest_b.append(v[m])
    out["rest_b"] = float(np.median(np.concatenate(rest_b))) if rest_b else np.nan
    out["whisk_mean"] = float(np.mean(wv)) if len(wv) else np.nan
    out["wdep_b"] = out["whisk_mean"] - out["rest_a"]
    oc = onset_vm_change(c, vmn, ep, "onsets", T)
    ocb = onset_vm_change(c, vmn, ep, "onsets_b", T)
    out["onset_pre_post"] = oc
    out["wdep_a"] = float(np.mean(oc[:, 1] - oc[:, 0])) if len(oc) else np.nan
    out["wdep_a_sd"] = float(np.std(oc[:, 1] - oc[:, 0])) if len(oc) else np.nan
    out["wdep_a_rise100"] = float(np.mean(ocb[:, 1] - ocb[:, 0])) if len(ocb) else np.nan
    out["n_onsets"] = len(oc)
    tt = touch_table(c, min_iti, trials)
    X = touch_vm(c, vmn, tt)
    out["n_touch"] = len(X)
    if len(X):
        avg = X.mean(0)
        out["avg_touch"] = avg
        out["amp50"], out["peak_ms"], _ = psp_amplitude(avg, win=0.05)
        out["amp25"], _, _ = psp_amplitude(avg, win=0.025)
        out["lat"] = vm_latency(avg)
        out["hw"] = half_width(avg)
        z = int(0.05 * VM_FS)
        pk = z + int(round(out["peak_ms"] / 1000 * VM_FS))
        base = X[:, z - int(0.005 * VM_FS):z].mean(1)
        out["touch_pre"] = base
        out["touch_post"] = X[:, pk]
        out["amp_sd"] = float(np.std(X[:, z:z + int(0.05 * VM_FS)].max(1) - base))
        out["amp_each_mean"] = float(np.mean(X[:, z:z + int(0.05 * VM_FS)].max(1) - base))
    else:
        for k in ("amp50", "peak_ms", "amp25", "lat", "hw", "amp_sd", "amp_each_mean"):
            out[k] = np.nan
    # distance to threshold (M-DTT): threshold of the trial minus Vm, 10th percentile
    spk = spikes_by_trial(c)
    # Threshold readings: "line", the per-trial line of M-VM; "clamp", the line held at its end
    # values outside the trials with spikes; "const", the neuron's mean threshold (variants).
    for rem, tk in [(r, t) for t in ("line", "clamp", "const") for r in ("a", "b")]:
        key = {"line": "thr_line", "clamp": "thr_clamped", "const": "thr_const"}[tk]
        sfx = rem if tk == "line" else f"{rem}_{tk}"
        dd = {"nonw": [], "whisk": [], "touch": []}
        for i, d in ep.items():
            v = vmn[i] if rem == "a" else c["vm"][i]
            th = P[key][i]
            for kind in ("nonw", "whisk"):
                for a, b in d[kind]:
                    ka, kb = vm_at(c, vmn, i, a / 1000), vm_at(c, vmn, i, b / 1000)
                    if ka >= 0 and kb <= len(v):
                        dd[kind].append(th - v[ka:kb])
            for x in T[i][0]:
                ka, kb = vm_at(c, vmn, i, x + 0.004), vm_at(c, vmn, i, x + 0.05)
                if ka >= 0 and kb <= len(v):
                    dd["touch"].append(th - v[ka:kb])
        p10 = {k: (np.percentile(np.concatenate(x), 10) if x else np.nan) for k, x in dd.items()}
        out[f"dtt_{sfx}"] = p10
        out[f"shift_whisk_{sfx}"] = p10["nonw"] - p10["whisk"]
        out[f"shift_touch_{sfx}"] = p10["nonw"] - p10["touch"]
    ph, y = vm_phase_data(c, vmn, ep)
    for nb in (8, 16):
        out[f"vphase{nb}"] = phase_fit(ph, y, nb) if len(ph) > 100 else (np.nan, np.nan, np.nan, None)
    # spikes per touch and whisking rate of the same neuron
    out["spk_counts_touch"] = [int(np.sum((spk[int(i)] - t >= 0) & (spk[int(i)] - t < 0.05))) for i, t in tt]
    w = epoch_rates(spk, ep, "whisk")
    n = epoch_rates(spk, ep, "nonw")
    out["whisk_rate"], _ = rate_readings(w)
    out["nonw_rate"], _ = rate_readings(n)
    sn = segments_500ms(c, vmn, ep, "nonw")
    sw = segments_500ms(c, vmn, ep, "whisk")
    out["spec_nonw"] = multitaper(sn)
    out["spec_whisk"] = multitaper(sw)
    out["n_seg"] = (len(sn), len(sw))
    return out
