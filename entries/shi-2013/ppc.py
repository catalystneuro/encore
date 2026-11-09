"""Loading and measures for CRCNS ppc-1 (Shi, Apker and Buneo 2013).

Dataset: crcns:ppc-1/unversioned (CRCNS data sets are not versioned; DOI
10.6080/K0CZ353K). The file read is ppc-1/live/data.tar.gz, MD5
bbb341b8947a6314b2618f0caa0b64f8 in the data set's checksums.md5.

The data set is one gzip-compressed tar file, ``ppc-1/live/data.tar.gz`` in the
public CRCNS bucket. A gzip stream cannot be read at random, so the file is
streamed once from the start (``tarfile`` in stream mode over ``fsspec``) and
each session's MATLAB file is reduced to a trial table and spike times as it
passes. Nothing is written to disk.

What the files hold (worked out from the data; the data descriptor describes
only the variable names):

- ``<session>.mat``: ``strobed`` (event times in seconds, event codes),
  ``data.<chan><unit>`` (spike times in milliseconds), ``waveforms``, ``nunits``.
- The event stream of each trial starts with code 0. After the trial's events
  a code 255 is followed by an ASCII text record, one character per strobe
  (codes 44 to 57 are ',', '-', '.', '0' to '9'), of 22 comma separated
  numbers. Field 13 is the target code, field 14 a two-valued code (4 or 7)
  that splits each session's completed trials into two halves of five trials
  per target, field 15 a counter, and fields 19 to 21 an x, y, z position in
  cm, the frame of the paper's Table 1.
- Target codes are a 3 by 3 grid, tens digit the row (4 bottom, 5 middle,
  6 top), units digit the column (4 left, 5 centre, 6 right); 55 is the
  central start position. The direction in degrees of each code, with 0
  rightward and counterclockwise positive (paper, Methods, Experimental
  paradigm), is ``TARGET_DEG``.
- Event codes used in a trial: 0 trial start, 1, 55 start position, 3 to 7 a
  burst at fixed 32 ms steps, 8, the target code, 10, then 12 and 13 on a
  completed trial or 14 on an aborted one. ``EventCodes.txt`` in the data set
  is a generic list whose names do not fit these codes, so their meaning is
  read from their timing (see the notebook): 12 is taken as the end of the
  static holding period, 8 as movement onset.
"""
import io
import re
import tarfile

import numpy as np
import pandas as pd
import scipy.io as sio

URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ppc-1/live/data.tar.gz"

# Target code -> direction (deg), 0 rightward, counterclockwise (paper, Methods).
TARGET_DEG = {56: 0, 66: 45, 65: 90, 64: 135, 54: 180, 44: 225, 45: 270, 46: 315}
TARGETS = [56, 66, 65, 64, 54, 44, 45, 46]  # in order 0..315 degrees

# A session file: <mmddyy>_<n>.mat (main sessions), d<n>.mat (early sessions,
# data descriptor, "Data format"), File<n>.mat. Files named <mmddyy>_<n>_<x>
# are behavioural training files, which the descriptor says were not used.
SESSION_RE = re.compile(r"^data/(\d{6})/((\d{6}_\d+)|(d\d+)|(File\d+))\.mat$")


def open_stream(url=URL, block_size=2**23):
    """Open the data set's tar.gz as a forward-only stream of members."""
    import fsspec
    f = fsspec.open(url, block_size=block_size).open()
    return tarfile.open(fileobj=f, mode="r|gz")


def parse_record(codes):
    """Decode the ASCII text record that follows a code 255."""
    txt = "".join(chr(int(c)) for c in codes if 32 <= c < 127)
    try:
        return [float(x) for x in txt.strip(",").split(",") if x != ""]
    except ValueError:
        return None


def trial_table(strobed):
    """One row per trial (a run of events starting with code 0)."""
    t = strobed[:, 0]
    c = strobed[:, 1].astype(int)
    starts = np.flatnonzero(c == 0)
    rows = []
    for k, j in enumerate(starts):
        e = starts[k + 1] if k + 1 < len(starts) else len(c)
        cc, tt = c[j:e], t[j:e]
        r = np.flatnonzero(cc == 255)
        lim = r[0] if len(r) else len(cc)
        ev = {}
        for code, ti in zip(cc[:lim], tt[:lim]):
            ev.setdefault(int(code), float(ti))
        vals = parse_record(cc[r[0] + 1:]) if len(r) else None
        row = dict(t0=float(tt[0]), completed=12 in ev, aborted=14 in ev,
                   t3=ev.get(3, np.nan), t8=ev.get(8, np.nan), t10=ev.get(10, np.nan),
                   t12=ev.get(12, np.nan), t13=ev.get(13, np.nan), t14=ev.get(14, np.nan),
                   nrec=len(vals) if vals else 0)
        tcodes = [k2 for k2 in ev if k2 in TARGET_DEG]
        row["t_target"] = ev[tcodes[0]] if tcodes else np.nan
        if vals and len(vals) in (22, 24) and all(np.isfinite(vals[13:15])):
            row.update(target=int(vals[13]), cond=int(vals[14]), f15=vals[15],
                       f16=vals[16], f17=vals[17], f18=vals[18],
                       x=vals[19], y=vals[20], z=vals[21],
                       params=tuple(vals[:13]))
            if len(vals) == 24:
                row.update(f22=vals[22], f23=vals[23])
        rows.append(row)
    return pd.DataFrame(rows)


def read_session_mat(raw):
    """Spike times (s) of each unit and the trial table from a session .mat."""
    d = sio.loadmat(io.BytesIO(raw), squeeze_me=True)
    units = {}
    data = d.get("data")
    if data is not None and data.dtype.names:
        for name in data.dtype.names:
            v = np.atleast_1d(np.asarray(data[name].item(), dtype=float)) / 1000.0
            units[name] = v
    strobed = np.asarray(d["strobed"], dtype=float).reshape(-1, 2)
    return units, strobed


def stream_sessions(url=URL, keep=None):
    """Yield (path, units, strobed) for each session .mat, in tar order.

    ``keep(path)`` may skip members by name. Only one session is held at a
    time; members that are not session files are skipped without reading.
    """
    tf = open_stream(url)
    for m in tf:
        if not m.isfile() or not SESSION_RE.match(m.name):
            continue
        if keep is not None and not keep(m.name):
            continue
        raw = tf.extractfile(m).read()
        try:
            units, strobed = read_session_mat(raw)
        except Exception as exc:  # recorded by the caller as unreadable
            yield m.name, None, repr(exc)
            continue
        yield m.name, units, strobed


def counts_in(spikes, starts, ends):
    """Spike counts of one unit in windows [start, end)."""
    s = np.sort(spikes)
    return np.searchsorted(s, ends) - np.searchsorted(s, starts)


def spikes_in(spikes, start, end):
    s = np.sort(spikes)
    return s[np.searchsorted(s, start):np.searchsorted(s, end)]


# ---------------------------------------------------------------------------
# Condition labels. The trial record's field 14 takes the values 4 and 7, five
# completed trials per target each, and no file documents which is Vision.
# ASSUMPTION (see the notebook, "Data check"): 4 is Vision (V) and 7 is No
# Vision (NV), because aborts after event 10, when the conditions differ, are
# more frequent on code 7 trials while aborts before it are not, and the paper
# (Discussion, Additional factors, paragraph 1) reports more aborts without
# vision of the cursor. Every measure takes the mapping as an argument so that
# the notebook can show the other one.
V_CODE, NV_CODE = 4, 7

# Windows, relative to event 12 (end of the static holding period), seconds.
# "data analysis focused on the last 800 ms of the static holding period"
# (Methods, Experimental paradigm); first and last 400 ms of it (Results,
# Neurophysiology, paragraph 2).
WINDOWS = {"hold": (-0.8, 0.0), "first400": (-0.8, -0.4), "last400": (-0.4, 0.0)}
# Movement epoch: "a 500-ms epoch centered on movement onset" (Results,
# Neurophysiology, paragraph 2), movement onset read as event 8 (assumption,
# see the notebook).
MOVE_HALF = 0.25
SIGMA_PSTH = 0.050  # Gaussian kernel, sigma 50 ms (Methods, Analysis of neurophysiological data)
N_PER_CELL = 5      # "Five trials were performed for each target" (Methods)


def load_all(url=URL, check_plx="data/010609/010609_1"):
    """One pass over the tar: every session file, reduced to its trial table
    and spike times; the member list; and, for one session, the .plx file's
    events and spikes to check the .mat extraction against."""
    import struct
    tf = open_stream(url)
    members, sessions, errors, plx = [], {}, {}, None
    for m in tf:
        members.append((m.name, m.size))
        if not m.isfile():
            continue
        if check_plx and m.name == check_plx + ".plx":
            b = tf.extractfile(m).read()
            plx = read_plx_events_spikes(b)
            continue
        if not SESSION_RE.match(m.name):
            continue
        raw = tf.extractfile(m).read()
        try:
            units, strobed = read_session_mat(raw)
            sessions[m.name] = dict(units=units, trials=trial_table(strobed),
                                    n_strobes=len(strobed), strobed_head=strobed[:2000])
        except Exception as exc:
            errors[m.name] = repr(exc)
    return dict(members=members, sessions=sessions, errors=errors, plx=plx)


def read_plx_events_spikes(b):
    """Strobed events and spike timestamps from a Plexon .plx file (format of
    Plexon's published file header: 7504-byte file header, 1020-byte spike
    channel headers, 296-byte event and slow channel headers, then 16-byte
    data block headers). Timestamps are in ticks of the file's ADFrequency."""
    import struct
    adfreq, = struct.unpack_from("<i", b, 136)
    nd, ne, ns = struct.unpack_from("<iii", b, 140)
    off = 7504 + 1020 * nd + 296 * ne + 296 * ns
    ev, spk = [], {}
    n = len(b)
    while off + 16 <= n:
        typ, up, ts, ch, unit, nw, nwords = struct.unpack_from("<hHIhhhh", b, off)
        off += 16
        t = (up << 32) + ts
        if typ == 4 and ch == 257:
            ev.append((t / adfreq, unit))
        elif typ == 1:
            spk.setdefault((ch, unit), []).append(t / adfreq)
        off += 2 * nw * nwords
    return dict(adfreq=adfreq, strobed=np.array(ev), spikes={k: np.array(v) for k, v in spk.items()})


def select_sessions(sessions, n_per=N_PER_CELL):
    """Sessions whose completed trials cover all 8 targets x 2 codes (4, 7)
    with at least ``n_per`` trials each; the first ``n_per`` in time of each
    are kept. Returns {session: trial table of the kept trials} and a table of
    every session with the reason it was kept or not."""
    kept, rows = {}, []
    for name, s in sessions.items():
        tt = s["trials"]
        row = dict(session=name, n_trials=len(tt), n_units=len(s["units"]))
        if "target" not in tt or tt["target"].isna().all():
            row["status"] = "no trial record with target and position"
            rows.append(row)
            continue
        c = tt[tt.completed & tt.target.isin(TARGETS) & tt.cond.isin([4, 7])]
        row["n_completed"] = len(c)
        g = c.groupby(["target", "cond"]).size()
        row["n_cells"] = len(g)
        row["min_per_cell"] = int(g.min()) if len(g) else 0
        if len(g) < 16 or g.min() < n_per:
            row["status"] = "incomplete design"
        else:
            k = c.sort_values("t0").groupby(["target", "cond"], group_keys=False).head(n_per)
            kept[name] = k.sort_values("t0").reset_index(drop=True)
            row["status"] = "kept" if g.max() == n_per else "kept, first five per cell"
        rows.append(row)
    return kept, pd.DataFrame(rows)


def cell_array(trials, values, v_code=V_CODE, nv_code=NV_CODE, n_per=N_PER_CELL):
    """Arrange per-trial values as [condition (V, NV), target (0..315 deg), trial]."""
    out = np.full((2, 8, n_per) + np.shape(values)[1:], np.nan)
    for ci, code in enumerate((v_code, nv_code)):
        for ti, tg in enumerate(TARGETS):
            idx = np.flatnonzero((trials.cond.values == code) & (trials.target.values == tg))
            out[ci, ti] = np.asarray(values)[idx[:n_per]]
    return out


def unit_counts(trials, spikes, window, align="t12"):
    t = trials[align].values
    return counts_in(spikes, t + window[0], t + window[1])


def psth_rate(trials, spikes, window, sigma=SIGMA_PSTH, align="t12"):
    """Mean of the Gaussian-smoothed rate over the window (the paper's PSTH,
    sigma 50 ms, averaged over the window): each spike adds the part of its
    kernel that falls inside the window."""
    from scipy.special import ndtr
    s = np.sort(spikes)
    out = np.empty(len(trials))
    for i, t in enumerate(trials[align].values):
        a, b = t + window[0], t + window[1]
        sp = s[np.searchsorted(s, a - 5 * sigma):np.searchsorted(s, b + 5 * sigma)]
        out[i] = np.sum(ndtr((b - sp) / sigma) - ndtr((a - sp) / sigma)) / (b - a)
    return out


def anova2(y):
    """Balanced two-factor ANOVA with interaction. ``y[cond, target, trial]``.
    Returns p values (target, condition, interaction); NaN when the error
    variance is zero. Balanced, so type I, II and III sums of squares agree."""
    from scipy.stats import f as fdist
    a, b, n = y.shape
    gm = y.mean()
    ma = y.mean(axis=(1, 2))
    mb = y.mean(axis=(0, 2))
    mab = y.mean(axis=2)
    ss_a = b * n * np.sum((ma - gm) ** 2)
    ss_b = a * n * np.sum((mb - gm) ** 2)
    ss_ab = n * np.sum((mab - ma[:, None] - mb[None, :] + gm) ** 2)
    ss_e = np.sum((y - mab[:, :, None]) ** 2)
    df_a, df_b, df_ab, df_e = a - 1, b - 1, (a - 1) * (b - 1), a * b * (n - 1)
    if ss_e <= 0:
        return np.nan, np.nan, np.nan
    mse = ss_e / df_e
    p_cond = fdist.sf(ss_a / df_a / mse, df_a, df_e)
    p_targ = fdist.sf(ss_b / df_b / mse, df_b, df_e)
    p_int = fdist.sf(ss_ab / df_ab / mse, df_ab, df_e)
    return p_targ, p_cond, p_int


def hotelling2(x1, x2):
    """Two-sample Hotelling T^2 test, the exact one-factor MANOVA for two
    groups (every MANOVA statistic gives this F). Returns (F, p); NaN when
    the pooled covariance is singular."""
    from scipy.stats import f as fdist
    x1, x2 = np.asarray(x1, float), np.asarray(x2, float)
    n1, n2, p = len(x1), len(x2), x1.shape[1]
    d = x1.mean(0) - x2.mean(0)
    S = ((n1 - 1) * np.cov(x1, rowvar=False) + (n2 - 1) * np.cov(x2, rowvar=False)) / (n1 + n2 - 2)
    try:
        t2 = n1 * n2 / (n1 + n2) * d @ np.linalg.solve(S, d)
    except np.linalg.LinAlgError:
        return np.nan, np.nan
    F = (n1 + n2 - p - 1) / (p * (n1 + n2 - 2)) * t2
    return F, fdist.sf(F, p, n1 + n2 - p - 1)


def decode(train, test, eps=1e-3, loo=True):
    """Poisson maximum-likelihood decoder (paper, Eqs. 3 and 4).

    ``train`` and ``test`` are spike counts [cell, target, trial] (five trials
    per target). Leave-one-out as the Methods give it: for test trial k the
    model lambda[cell, target] is the mean of the other four training trials
    (when train and test are the same data) and the test trial is assigned to
    the target of maximal likelihood. With ``loo=False`` lambda is the mean of
    all five training trials (cross-condition reading (b)). A lambda of 0 is
    replaced by ``eps`` (a standard choice). Returns the confusion counts
    [true, predicted]."""
    c, t, n = train.shape
    conf = np.zeros((t, t), int)
    same = train is test
    for k in range(n):
        if not loo:
            lam = train.mean(axis=2)
        elif same:
            lam = (train.sum(axis=2) - train[:, :, k]) / (n - 1)
        else:
            lam = np.delete(train, k, axis=2).mean(axis=2)
        lam = np.maximum(lam, eps)
        r = test[:, :, k]  # [cell, true target]
        ll = r.T @ np.log(lam) - lam.sum(axis=0)[None, :]  # [true, candidate]
        pred = np.argmax(ll, axis=1)
        for tt_, pp in enumerate(pred):
            conf[tt_, pp] += 1
    return conf
