"""Loading and measures for CRCNS hc-12 (and hc-21), the data of Wirth, Baraduc, Plante,
Pinede & Duhamel (2017), PLoS Biology 15(2), e2001045, doi:10.1371/journal.pbio.2001045.

The data sets are single tar.gz archives of MATLAB files, one file per cell, in the public S3
bucket crcnsarchive. They are streamed: the archive is decompressed as it is read and each
member is loaded in memory and reduced to what the analysis needs, one at a time. Nothing is
written to disk.

File layout (descriptor of hc-12, version 0.7, and the files themselves): spike times
(`file.elec`, or `file.newallo.elec` when the top level has none), the trial tables of the new
maze (`newallo.codematrix`, `newallo.timematrix`), learning curves, eye positions at 250 Hz
with `eye_times`, and `camera_data.time_60`, 60 Hz rows of [time, x, y, camera orientation
(deg), curvilinear abscissa on the maze branch (0 centre, 1 arm end), state-space curvilinear
abscissa, state-space polar angle, state-space radius, next, previous and current transition
tag, composite maze tag]. `time_60` sits under `newallo.camera_data` in some files.

Where the parameters come from:

- Successful trials only; maps unsmoothed; a bin is valid with at least four successful
  trials (Methods, Activity maps) and more than 400 ms of time in successful trials (Methods,
  Information Content). The resolution of each map is stepped until the number of valid bins
  is as close to 200 as possible (Methods, Information Content). The steps (square bins for
  position and state space, equal angular bins for direction) are a standard choice; the
  square grids follow the dataset's own scripts (simple_place_cell_square_script_theta_r.m,
  1 m squares of x, y; star_remapped_cell_r.m, squares of the planar state-space projection
  pol2cart(time_60 columns 7 and 8)), which also show that the state-space map is a map of
  that planar projection.
- Skaggs information in bits per spike and the sparsity index as written in the Methods
  (Information Content; Sparsity index). Normalized values subtract the mean of 999 surrogates.
- Surrogates (Methods, Permutation statistics): the recording time of the new-maze session is
  cut into 5 s chunks that are "randomly shifted", which "decorrelated the spikes from the
  animal's behavior while essentially preserving the structure of spike trains". Reading
  "permute" (claims file, Method W (a)): the order of the chunks of the spike train is
  permuted. Reading "shift" (Method W (b), each chunk displaced by an independent random time
  shift): the spikes of each chunk are shifted circularly within the chunk by an independent
  random offset, so that chunks do not overlap and every frame keeps one source. (Moving each
  chunk by an offset over the whole session, as the first version did, piles chunks on top of
  each other and leaves frames empty; on a train without any coding its surrogates had higher
  IC than the train itself, so it was replaced; an assumption.) The p-value is bilateral,
  twice the smaller tail fraction of the rank among 1,000 (claims file, a standard choice); the
  upper and lower tail fractions are kept as well.
- Trial windows (claims file, Method W): reading "full", trial start (code 21) to the next
  trial start, so the passive return after the trial belongs to it; reading "toreward",
  trial start to reward (code 11), no return; reading "toreward_ret", trial start to reward
  plus the return (tags 5xy) that follows the trial, which drops the time from reward to the
  start of the return (the claims file's reading (b), "from trial start to reward, return
  paths taken from the returns that follow correct trials", read with the returns kept).
- Maze centre: transition tags 2xy and 3xy (rotations at the centre); return paths: tags 5xy
  (descriptor, transition tags). Entry paths: tags 10x, the path x being the landmark identity.
- State-space selectivity (Methods, State-space selectivity): 3.6 degree bins, three move
  types, at least 400 ms in each of at least two types. The paper does not name the three
  moves; three typings are run (an assumption each): "arc", the 36 degree alignment (tags
  2xy), a 72 degree rotation to the right and one to the left (tags 3xy, split by the sign of
  the change of camera orientation); "align_dir", the 36 degree alignment to the right, to the
  left (2xy split by sign) and the 72 degree rotation (3xy, either way); "tag", each
  transition tag of the state-space graph (2xy or 3xy) as its own move, the edges of Fig 1F
  and Fig 4A ("compared on the different state-space transitions").
"""

from __future__ import annotations

import io
import tarfile

import fsspec
import numpy as np
import scipy.io as sio
from scipy import sparse

BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com"
ARCHIVES = {"hc-12": f"{BUCKET}/hc-12/live/data.tar.gz",
            "hc-21": f"{BUCKET}/hc-21/live/data.tar.gz"}
VERSION = "unversioned"       # CRCNS data sets are not versioned (docs/archives.md)
MD5 = {"hc-12": "426c7d00c0358f2cc9873e0dbb331e2f",   # checksums.md5 of each data set
       "hc-21": "dee5e8aa4a7b3c44b61b8cecfe622a0a"}

DT = 1 / 60                   # camera rows are 60 Hz
MIN_BIN_S = 0.4               # Methods, Information Content
MIN_TRIALS = 4                # Methods, Activity maps
TARGET_BINS = 200             # Methods, Information Content
CHUNK_S = 5.0                 # Methods, Permutation statistics
N_SURR = 999
SSI_BIN_DEG = 3.6             # Methods, State-space selectivity

POS_STEPS = np.round(np.arange(0.4, 8.01, 0.1), 2)          # m, square bins
STATE_STEPS = np.round(np.arange(0.02, 0.60, 0.005), 3)     # planar state-space units
DIR_STEPS = np.arange(8, 721)                                # number of angular bins


# ---------------------------------------------------------------- loading

def stream_members(dataset):
    """Yield (member name, loaded MATLAB dict) for every .mat file of a data set's archive."""
    f = fsspec.open(ARCHIVES[dataset], block_size=2**22).open()
    with tarfile.open(fileobj=f, mode="r|gz") as tf:
        for m in tf:
            if m.isfile() and m.name.endswith(".mat"):
                yield m.name.split("/")[-1], sio.loadmat(io.BytesIO(tf.extractfile(m).read()))


def _field(s, name):
    return s[name] if (s.dtype.names and name in s.dtype.names) else None


def reduce_file(name, d, maze="newallo"):
    """Reduce one cell file to the arrays used here; None when it has no `maze` trials."""
    fl = d["file"][0, 0]
    mz = _field(fl, maze)
    if mz is None or mz.dtype.names is None:
        return None
    mz = mz[0, 0]
    el = _field(fl, "elec")
    spike_src = "file.elec"
    if el is None or el.size == 0:
        el = _field(mz, "elec")
        spike_src = f"{maze}.elec"
    cd = _field(fl, "camera_data")
    if cd is None:
        cd = _field(mz, "camera_data")
    t60 = np.asarray(cd[0, 0]["time_60"], float)
    cm = np.asarray(mz["codematrix"], float)
    tm = np.asarray(mz["timematrix"], float)
    lc = _field(mz, "learning_curves")
    lt = _field(mz, "learningtrial")
    out = {"name": name, "monkey": name[:2], "session": name.split("_")[0],
           "spikes": np.sort(np.asarray(el, float).ravel()), "spike_src": spike_src,
           "cm": cm, "tm": tm,
           "lc": None if lc is None else np.asarray(lc, float),
           "learningtrial": None if lt is None or lt.size == 0 else float(lt.ravel()[0]),
           "reclocation": None if _field(fl, "reclocation") is None
           else np.asarray(fl["reclocation"], float).ravel()}
    # session window: first trial start to last trial end (as the dataset's scripts do)
    t0 = _code_times(cm, tm, 21)
    t0 = np.nanmin(t0)
    t1 = np.nanmax(np.where(cm[:, 1:] > 0, tm[:, 1:], np.nan))
    keep = (t60[:, 0] >= t0) & (t60[:, 0] <= t1 + 1.0) & np.isfinite(t60[:, 10])
    out["t60_shape_raw"] = t60.shape
    t60 = t60[keep]
    t60 = t60[np.argsort(t60[:, 0], kind="stable")]
    out["t60"] = t60.astype(np.float64)
    out["window"] = (t0, t1)
    et = _field(fl, "eye_times")
    if et is not None and et.size:
        et = np.asarray(et, float).ravel()
        w = (et >= t0 - 1) & (et <= t1 + 1)
        eyes = {}
        eye_units = set()
        for e in ("left_eye", "right_eye"):
            s = _field(fl, e)
            if s is None:
                continue
            s = s[0, 0]
            for c in ("hor", "ver"):
                v = s[c]
                if v.dtype.names:  # a Spike2 channel struct: take its values, keep its units
                    v = v[0, 0]
                    eye_units.add(str(np.asarray(v["units"]).ravel()[0]) if v["units"].size else "")
                    v = v["values"]
                v = np.asarray(v, float).ravel()
                n = min(len(v), len(et))
                eyes[f"{e[0]}_{c}"] = v[:n][w[:n]].astype(np.float32)
        n = min(len(v) for v in eyes.values()) if eyes else 0
        out["eye_t"] = et[w][:n]
        out["eye"] = {k: v[:n] for k, v in eyes.items()}
        out["eye_units"] = ",".join(sorted(eye_units)) or None
        # the files hold the eye signal on a +-5000 or a +-5 scale; the rail is that bound
        big = max(float(np.nanmax(np.abs(v))) for v in out["eye"].values()) if n else 0.0
        out["eye_rail"] = 5000.0 * 0.99997 if big > 10 else 5.0 * 0.99997
    else:
        out["eye_t"] = None
        out["eye"] = None
        out["eye_units"] = None
    return out


def _code_times(cm, tm, code):
    """Per trial, the time of the first occurrence of an event code (NaN if absent)."""
    hit = cm[:, 1:] == code
    first = np.where(hit.any(1), hit.argmax(1) + 1, -1)
    return np.where(first > 0, tm[np.arange(len(cm)), np.maximum(first, 0)], np.nan)


def trials(c):
    """Per-trial table: start arm (1-5), chosen arm (1-5), outcome, event times."""
    cm, tm = c["cm"], c["tm"]
    start_code = np.array([next((v for v in row[1:] if 40 <= v <= 44), np.nan) for row in cm])
    chosen = np.array([next((v for v in row[1:] if 50 <= v <= 54), np.nan) for row in cm])
    turns = [[int(v) for v in row[1:] if v in (1, 2)] for row in cm]
    turn_t = [[t for v, t in zip(row[1:], trow[1:]) if v in (1, 2)] for row, trow in zip(cm, tm)]
    return {"start_arm": start_code - 39, "chosen_arm": chosen - 49,
            "correct": (cm[:, 1:] == 11).any(1), "error": (cm[:, 1:] == 12).any(1),
            "t_start": _code_times(cm, tm, 21), "t_center": _code_times(cm, tm, 22),
            "t_reward": _code_times(cm, tm, 11), "t_end": _code_times(cm, tm, 23),
            "turns": turns, "turn_t": turn_t}


# ---------------------------------------------------------------- frames and bins

def frame_table(c, reading="full"):
    """Per camera frame: trial index (or -1), whether it is analysed (successful trial)."""
    t = c["t60"][:, 0]
    tr = trials(c)
    ts = tr["t_start"]
    n = len(ts)
    trial = np.full(len(t), -1)
    for i in range(n):
        if not np.isfinite(ts[i]):
            continue
        if reading == "full":
            nxt = ts[i + 1] if i + 1 < n and np.isfinite(ts[i + 1]) else tr["t_end"][i] + 1.0
            end = nxt
        else:  # "toreward" and "toreward_ret"
            end = tr["t_reward"][i]
            if not np.isfinite(end):
                continue
            if reading == "toreward_ret":
                nxt = ts[i + 1] if i + 1 < n and np.isfinite(ts[i + 1]) else tr["t_end"][i] + 1.0
                tag = c["t60"][:, 10]
                trial[(t >= tr["t_end"][i]) & (t < nxt) & (tag >= 500) & (tag < 600)] = i
        trial[(t >= ts[i]) & (t < end)] = i
    ok = (trial >= 0) & tr["correct"][np.maximum(trial, 0)]
    return trial, ok


def spike_counts(c):
    """Spikes per camera frame, frame k covering [t_k, t_k + 1/60)."""
    t = c["t60"][:, 0]
    sp = c["spikes"]
    lo = np.searchsorted(sp, t)
    hi = np.searchsorted(sp, t + DT)
    return (hi - lo).astype(np.float64)


def space_coords(c):
    t60 = c["t60"]
    th, rho = t60[:, 6], t60[:, 7]
    return {"position": (t60[:, 1], t60[:, 2]),
            "direction": (np.mod(t60[:, 3], 360.0),),
            "state": (rho * np.cos(th), rho * np.sin(th))}


def _bin_index(coords, step, kind):
    if kind == "direction":
        nb = int(step)
        b = np.floor(coords[0] / (360.0 / nb)).astype(int)
        return np.clip(b, 0, nb - 1), nb
    x, y = coords
    lo = -25.0 if kind == "position" else -3.0
    nx = int(np.ceil(2 * -lo / step))
    bx = np.floor((x - lo) / step).astype(int)
    by = np.floor((y - lo) / step).astype(int)
    good = np.isfinite(x) & np.isfinite(y)
    b = np.where(good, by * nx + bx, -1)
    return b, nx * nx


def valid_bins(b, nb, ok, trial):
    """Occupancy (s) per bin over analysed frames and the valid mask (>400 ms, >=4 trials)."""
    sel = ok & (b >= 0)
    occ = np.bincount(b[sel], minlength=nb) * DT
    pairs = np.unique(b[sel].astype(np.int64) * 100000 + trial[sel])
    ntr = np.bincount((pairs // 100000).astype(int), minlength=nb)
    return occ, (occ > MIN_BIN_S) & (ntr >= MIN_TRIALS)


def choose_resolution(coords, kind, ok, trial):
    """Step the resolution until the number of valid bins is closest to 200."""
    steps = {"position": POS_STEPS, "state": STATE_STEPS, "direction": DIR_STEPS}[kind]
    best = None
    for s in steps:
        b, nb = _bin_index(coords, s, kind)
        occ, val = valid_bins(b, nb, ok, trial)
        d = abs(int(val.sum()) - TARGET_BINS)
        if best is None or d < best[0]:
            best = (d, s, b, nb, occ, val)
    _, s, b, nb, occ, val = best
    return {"step": s, "bins": b, "nb": nb, "occ": occ, "valid": val}


def design(mask_frames, b, valid):
    """Sparse frames x valid-bins indicator for the frames in mask_frames."""
    vidx = -np.ones(len(valid), int)
    vidx[valid] = np.arange(valid.sum())
    rows = np.nonzero(mask_frames & (b >= 0))[0]
    cols = vidx[b[rows]]
    keep = cols >= 0
    return sparse.csr_matrix((np.ones(keep.sum()), (rows[keep], cols[keep])),
                             shape=(len(b), int(valid.sum())))


# ---------------------------------------------------------------- measures

def skaggs_ic(counts, occ):
    """Skaggs information (bits/spike); counts (..., M) spikes per bin, occ (M,) seconds."""
    p = occ / occ.sum()
    lam = counts / occ
    mean = (lam * p).sum(-1, keepdims=True)
    with np.errstate(divide="ignore", invalid="ignore"):
        r = lam / mean
        term = np.where(r > 0, p * r * np.log2(r), 0.0)
    out = term.sum(-1)
    return np.where(mean[..., 0] > 0, out, np.nan)


def sparsity(counts, occ):
    """(M - (sum rate)^2 / sum rate^2) / (M - 1), Methods, Sparsity index."""
    lam = counts / occ
    m = lam.shape[-1]
    with np.errstate(divide="ignore", invalid="ignore"):
        s = (m - lam.sum(-1) ** 2 / (lam ** 2).sum(-1)) / (m - 1)
    return s


def uncentered_corr(a, b):
    with np.errstate(divide="ignore", invalid="ignore"):
        return (a * b).sum(-1) / np.sqrt((a ** 2).sum(-1) * (b ** 2).sum(-1))


def surrogate_counts(s, rng, reading, n=N_SURR, batch=111):
    """Yield batches of surrogate spike-count series (batch x T)."""
    T = len(s)
    L = int(round(CHUNK_S / DT))
    nch = T // L
    done = 0
    while done < n:
        k = min(batch, n - done)
        out = np.empty((k, T))
        for i in range(k):
            if reading == "permute":
                perm = rng.permutation(nch)
                body = s[: nch * L].reshape(nch, L)[perm].ravel()
                out[i] = np.concatenate([body, s[nch * L:]])
            else:  # "shift": each chunk shifted circularly within itself by its own offset
                out[i] = s[shift_index(T, L, rng)]
        done += k
        yield out


def shift_index(T, L, rng):
    """Source frame of each frame when every L-frame chunk (and the shorter remainder) is
    rotated by an independent random offset within itself."""
    src = np.arange(T)
    ch = src // L
    start = ch * L
    length = np.minimum(L, T - start)
    offs = rng.integers(0, L, size=ch[-1] + 1)
    return start + (src - start + offs[ch]) % length


def tail_p(actual, surr):
    """Rank p-values among actual + surrogates: (bilateral, upper, lower)."""
    surr = np.asarray(surr)
    n = surr.shape[0] + 1
    up = (1 + np.sum(surr >= actual, 0)) / n
    lo = (1 + np.sum(surr <= actual, 0)) / n
    return np.minimum(1.0, 2 * np.minimum(up, lo)), up, lo


def lower_bound_criterion(lc_lower, chance=0.25):
    """First trial (1-based) at which the lower bound exceeds chance, or NaN (S3B legend)."""
    i = np.nonzero(lc_lower > chance)[0]
    return float(i[0] + 1) if len(i) else np.nan


def binom_upper(k, n, p):
    from scipy.stats import binom
    return float(binom.sf(k - 1, n, p))


# ---------------------------------------------------------------- per-cell analysis

WINDOWS = ("full", "toreward", "toreward_ret")
TYPINGS = ("arc", "align_dir", "tag")
SHIFTS_S = (-5.0, -2.0, -1.0, -0.5, -0.25, 0.0, 0.25, 0.5, 1.0, 2.0, 5.0)


def turn_types(c, typing="arc"):
    """Per frame, the index of the rotational move at the centre (-1 elsewhere) and the number
    of move types. "arc": 0 for a 36 degree alignment (tag 2xy), 1 for a 72 degree rotation to
    the right, 2 to the left (tags 3xy). "align_dir": 0 and 1 for a 36 degree alignment to the
    right and to the left, 2 for a 72 degree rotation. "tag": one type per transition tag (2xy
    and 3xy). The side is the sign of the orientation change over the run of frames carrying
    the tag; a right turn (code 1) lowers the camera orientation, as the notebook shows."""
    tag = c["t60"][:, 10]
    th = c["t60"][:, 3]
    is2 = (tag >= 200) & (tag < 300)
    is3 = (tag >= 300) & (tag < 400)
    out = np.full(len(tag), -1)
    if typing == "tag":
        vals = np.unique(tag[is2 | is3])
        out[is2 | is3] = np.searchsorted(vals, tag[is2 | is3])
        return out, max(len(vals), 1)
    right = np.zeros(len(tag), bool)
    rot = is2 | is3
    if rot.any():
        brk = np.nonzero(np.diff(np.r_[0, rot.astype(int), 0]))[0]
        dth = np.r_[0, (np.diff(th) + 180) % 360 - 180]
        for a, b in zip(brk[::2], brk[1::2]):
            vals = tag[a:b]
            for v in np.unique(vals):  # one run per tag value
                idx = np.arange(a, b)[vals == v]
                right[idx] = dth[idx[1:]].sum() < 0
    if typing == "arc":
        out[is2] = 0
        out[is3] = np.where(right[is3], 1, 2)
    else:  # "align_dir"
        out[is2] = np.where(right[is2], 0, 1)
        out[is3] = 2
    return out, 3


class Session:
    """Behaviour-only quantities shared by the cells of one session (same trial table)."""

    def __init__(self, c):
        self.t60 = c["t60"]
        self.tag = c["t60"][:, 10]
        self.coords = space_coords(c)
        self.tables = {r: frame_table(c, r) for r in WINDOWS}
        self.res = {}
        for r, (trial, ok) in self.tables.items():
            for kind, xy in self.coords.items():
                self.res[(r, kind)] = choose_resolution(xy, kind, ok, trial)
        trial, ok = self.tables["full"]
        self.center = ok & (self.tag >= 200) & (self.tag < 400)
        self.ret = ok & (self.tag >= 500) & (self.tag < 600)
        self.entry = ok & (self.tag >= 100) & (self.tag < 200)
        # common direction resolution for centre and return maps
        best = None
        d = self.coords["direction"]
        for nb in DIR_STEPS:
            b, _ = _bin_index(d, nb, "direction")
            oc, vc = valid_bins(b, nb, self.center, trial)
            orr, vr = valid_bins(b, nb, self.ret, trial)
            k = abs(int((vc & vr).sum()) - TARGET_BINS)
            if best is None or k < best[0]:
                best = (k, nb, b, oc, vc, orr, vr)
        _, nb, b, oc, vc, orr, vr = best
        self.cr = {"nb": nb, "bins": b, "occ_c": oc, "val_c": vc, "occ_r": orr, "val_r": vr}
        # state-space selectivity layout: 3.6 degree bins x move types, centre frames
        nbin = int(round(360 / SSI_BIN_DEG))
        db = np.clip(np.floor(np.mod(self.t60[:, 3], 360) / SSI_BIN_DEG).astype(int), 0, nbin - 1)
        self.ssi = {}
        for ty in TYPINGS:
            types, k = turn_types(c, ty)
            col = np.where(self.center & (types >= 0), db * k + np.maximum(types, 0), -1)
            occ = np.bincount(col[col >= 0], minlength=nbin * k).reshape(nbin, k) * DT
            self.ssi[ty] = {"col": col, "occ": occ, "nbin": nbin, "k": k}
        # designs
        self.designs = {}
        for (r, kind), rr in self.res.items():
            okr = self.tables[r][1]
            self.designs[(r, kind)] = design(okr, rr["bins"], rr["valid"])
        self.designs["center"] = design(self.center, b, vc)
        self.designs["return"] = design(self.ret, b, vr)
        both = vc & vr
        self.designs["center_common"] = design(self.center, b, both)
        self.designs["return_common"] = design(self.ret, b, both)
        self.occ_common = (oc[both], orr[both])
        self.ssi_designs = {}
        for ty, sv in self.ssi.items():
            col = sv["col"]
            good = col >= 0
            self.ssi_designs[ty] = sparse.csr_matrix(
                (np.ones(good.sum()), (np.nonzero(good)[0], col[good])), shape=(len(col), nbin * sv["k"]))


def _occ(sess, key):
    if key in sess.res:
        rr = sess.res[key]
        return rr["occ"][rr["valid"]]
    if key == "center":
        return sess.cr["occ_c"][sess.cr["val_c"]]
    if key == "return":
        return sess.cr["occ_r"][sess.cr["val_r"]]
    raise KeyError(key)


def ssi_index(counts, occ):
    """SSI over bins with >= 400 ms in each of >= 2 move types (Methods, State-space
    selectivity); counts (..., nbin*k), occ (nbin, k)."""
    nbin, k = occ.shape
    cnt = counts.reshape(counts.shape[:-1] + (nbin, k))
    good_t = occ >= MIN_BIN_S
    good_b = good_t.sum(1) >= 2
    with np.errstate(divide="ignore", invalid="ignore"):
        lam = np.where(good_t, cnt / occ, np.nan)
    lam = lam[..., good_b, :]
    mx = np.nanmax(lam, -1)
    mn = np.nanmin(lam, -1)
    with np.errstate(divide="ignore", invalid="ignore"):
        return (mx - mn).sum(-1) / (mx + mn).sum(-1), int(good_b.sum())


def analyse_cell(c, sess, seed):
    """All map measures of one cell with their surrogates, both surrogate readings."""
    s = spike_counts(c)
    out = {"name": c["name"], "monkey": c["monkey"], "session": c["session"],
           "n_spikes_window": int(s.sum()), "n_spikes_file": int(len(c["spikes"])),
           "spike_src": c["spike_src"]}
    keys = [k for k in sess.designs if isinstance(k, tuple)] + ["center", "return"]
    actual = {k: s @ sess.designs[k] for k in keys}
    act_cc = (s @ sess.designs["center_common"], s @ sess.designs["return_common"])
    act_ssi = {ty: s @ dm for ty, dm in sess.ssi_designs.items()}
    for k in keys:
        occ = _occ(sess, k)
        out[f"ic|{k}"] = float(skaggs_ic(actual[k], occ)) if len(occ) else np.nan
        out[f"sp|{k}"] = float(sparsity(actual[k], occ)) if len(occ) > 1 else np.nan
        out[f"nbins|{k}"] = int(len(occ))
    for r in WINDOWS:
        out[f"frames|{r}"] = int(sess.tables[r][1].sum())
    oc_c, oc_r = sess.occ_common
    out["corr"] = float(uncentered_corr(act_cc[0] / oc_c, act_cc[1] / oc_r)) if len(oc_c) else np.nan
    out["n_common"] = int(len(oc_c))
    ssi_a = {}
    for ty in TYPINGS:
        a, nb_ssi = ssi_index(act_ssi[ty], sess.ssi[ty]["occ"])
        ssi_a[ty] = float(a)
        out[f"ssi|{ty}"] = float(a)
        out[f"ssi_bins|{ty}"] = nb_ssi
    for sr, sub in (("permute", 1), ("shift", 2)):
        rng = np.random.default_rng([seed, sub])
        surr = {k: [] for k in keys}
        surr_cc, surr_ssi = [], {ty: [] for ty in TYPINGS}
        for S in surrogate_counts(s, rng, sr):
            St = S.T
            for k in keys:
                surr[k].append((sess.designs[k].T @ St).T)
            surr_cc.append(((sess.designs["center_common"].T @ St).T,
                            (sess.designs["return_common"].T @ St).T))
            for ty, dm in sess.ssi_designs.items():
                surr_ssi[ty].append((dm.T @ St).T)
        stats = {}
        for k in keys:
            occ = _occ(sess, k)
            cnts = np.vstack(surr[k])
            if len(occ) < 2:
                continue
            ic_s = skaggs_ic(cnts, occ)
            sp_s = sparsity(cnts, occ)
            stats[k] = (ic_s, sp_s)
            for meas, a, sv in (("ic", out[f"ic|{k}"], ic_s), ("sp", out[f"sp|{k}"], sp_s)):
                sv = sv[np.isfinite(sv)]
                p2, pu, pl = tail_p(a, sv)
                out[f"{meas}n|{k}|{sr}"] = float(a - sv.mean()) if len(sv) else np.nan
                out[f"{meas}p|{k}|{sr}"] = float(p2)
                if meas == "ic":
                    out[f"icup|{k}|{sr}"], out[f"iclo|{k}|{sr}"] = float(pu), float(pl)
        # sparsity and IC differences, state space minus another space (per trial reading)
        for r in WINDOWS:
            st = (r, "state")
            for other in ("position", "direction"):
                ok_ = (r, other)
                if st in stats and ok_ in stats:
                    for j, meas in ((1, "sp"), (0, "ic")):
                        a = out[f"{meas}|{st}"] - out[f"{meas}|{ok_}"]
                        d = stats[st][j] - stats[ok_][j]
                        d = d[np.isfinite(d)]
                        p2, pu, pl = tail_p(a, d)
                        out[f"{meas}diffp|{r}|{other}|{sr}"] = float(p2)
        if len(oc_c):
            cc = np.vstack([x[0] for x in surr_cc]) / oc_c
            rr = np.vstack([x[1] for x in surr_cc]) / oc_r
            cs = uncentered_corr(cc, rr)
            cs = cs[np.isfinite(cs)]
            p2, pu, pl = tail_p(out["corr"], cs)
            out[f"corr_up|{sr}"], out[f"corr_lo|{sr}"] = float(pu), float(pl)
            out[f"corrn|{sr}"] = float(out["corr"] - cs.mean()) if len(cs) else np.nan
        for ty in TYPINGS:
            ss, _ = ssi_index(np.vstack(surr_ssi[ty]), sess.ssi[ty]["occ"])
            ss = ss[np.isfinite(ss)]
            if np.isfinite(ssi_a[ty]) and len(ss):
                p2, pu, pl = tail_p(ssi_a[ty], ss)
                out[f"ssin|{ty}|{sr}"] = float(ssi_a[ty] - ss.mean())
                out[f"ssi_up|{ty}|{sr}"], out[f"ssi_lo|{ty}|{sr}"] = float(pu), float(pl)
    # clock check: state-space IC with the spikes shifted in time
    key = ("full", "state")
    occ = _occ(sess, key)
    t = c["t60"][:, 0]
    for sh in SHIFTS_S:
        sp = c["spikes"] + sh
        cnt = (np.searchsorted(sp, t + DT) - np.searchsorted(sp, t)).astype(float)
        out[f"shift_ic|{sh}"] = float(skaggs_ic(cnt @ sess.designs[key], occ))
    return out, s


# ---------------------------------------------------------------- landmark analyses

def landmark_tables(c, s, sess, laps="successful"):
    """Per lap rates for the landmark ANOVAs.

    Two-way (Methods, ANOVA for landmark identity and relative distance): entry-path frames
    (tags 10x) of successful trials, cut by the curvilinear abscissa (0 centre, 1 arm end)
    into RD1 (1 to 0.75, 16 to 12 m) ... RD4 (0.25 to 0); identity is the entry path x, whose
    view faces one landmark. One-way at the centre (claims file, readings): (a) centre frames
    whose camera orientation lies within the 3.6 degree bin of the heading of entry path x
    (the landmark straight ahead on arrival), one rate per trial; (b) the 36 degree alignment
    after arriving from path x (tags 2xy), one rate per visit."""
    import pandas as pd
    t60 = c["t60"]
    trial, ok = sess.tables["full"]
    if laps == "all":  # every trial, rewarded or not
        ok = trial >= 0
    tag = sess.tag
    ab = t60[:, 4]
    entry = ok & (tag >= 100) & (tag < 200)
    center = ok & (tag >= 200) & (tag < 400)
    ent = entry & np.isfinite(ab)
    seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
    key = pd.DataFrame({"trial": trial[ent], "lm": (tag[ent] % 100).astype(int),
                        "rd": seg[ent], "n": s[ent]})
    two = key.groupby(["trial", "lm", "rd"]).agg(spk=("n", "sum"), fr=("n", "size")).reset_index()
    two["rate"] = two.spk / (two.fr * DT)
    # one-way (b): 2xy visits
    m2 = ok & (tag >= 200) & (tag < 300)
    df2 = pd.DataFrame({"trial": trial[m2], "lm": ((tag[m2] // 10) % 10).astype(int), "n": s[m2]})
    oneb = df2.groupby(["trial", "lm"]).agg(spk=("n", "sum"), fr=("n", "size")).reset_index()
    oneb["rate"] = oneb.spk / (oneb.fr * DT)
    # one-way (a): heading of each entry path, then centre frames facing it
    th = np.mod(t60[:, 3], 360)
    heads = {}
    for x in np.unique(tag[entry] % 100).astype(int):
        mm = entry & (tag % 100 == x)
        a = np.deg2rad(th[mm])
        heads[x] = np.rad2deg(np.arctan2(np.sin(a).mean(), np.cos(a).mean())) % 360
    reca = []
    for x, h in heads.items():
        d = np.abs((th - h + 180) % 360 - 180)
        mm = center & (d <= SSI_BIN_DEG / 2)
        reca.append(pd.DataFrame({"trial": trial[mm], "lm": x, "n": s[mm]}))
    onea = pd.concat(reca).groupby(["trial", "lm"]).agg(spk=("n", "sum"), fr=("n", "size")).reset_index()
    onea["rate"] = onea.spk / (onea.fr * DT)
    return two, onea, oneb, heads


def anova_two(two):
    import warnings
    import statsmodels.api as sm
    from statsmodels.formula.api import ols
    if two.lm.nunique() < 2 or two.rd.nunique() < 2 or two.rate.var() == 0:
        return None
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        fit = ols("rate ~ C(lm) * C(rd)", data=two).fit()
        tab = sm.stats.anova_lm(fit, typ=2)
        # type III, MATLAB anovan's default, with sum-to-zero contrasts
        fit3 = ols("rate ~ C(lm, Sum) * C(rd, Sum)", data=two).fit()
        tab3 = sm.stats.anova_lm(fit3, typ=3)
    return {"p_lm": tab.loc["C(lm)", "PR(>F)"], "p_rd": tab.loc["C(rd)", "PR(>F)"],
            "p_int": tab.loc["C(lm):C(rd)", "PR(>F)"], "F_int": tab.loc["C(lm):C(rd)", "F"],
            "df_int": tab.loc["C(lm):C(rd)", "df"], "df_res": tab.loc["Residual", "df"],
            "p_lm3": tab3.loc["C(lm, Sum)", "PR(>F)"], "p_rd3": tab3.loc["C(rd, Sum)", "PR(>F)"],
            "p_int3": tab3.loc["C(lm, Sum):C(rd, Sum)", "PR(>F)"],
            "n_lm": int(two.lm.nunique())}


def anova_one(df):
    from scipy.stats import f_oneway
    groups = [g.rate.values for _, g in df.groupby("lm") if len(g) >= 2]
    if len(groups) < 2 or np.var(np.concatenate(groups)) == 0:
        return np.nan, len(groups)
    return float(f_oneway(*groups).pvalue), len(groups)


# ---------------------------------------------------------------- eye

EYE_RAIL = 0.9999  # samples at the rail (+-4999.85 or +-4.99985) are saturated (notebook)


def eye_mean(c, t0, t1, which="mean"):
    """Mean horizontal eye signal in [t0, t1), raw file units; saturated samples dropped."""
    if c["eye"] is None:
        return np.nan
    et = c["eye_t"]
    i0, i1 = np.searchsorted(et, t0), np.searchsorted(et, t1)
    if i1 <= i0:
        return np.nan
    if which == "mean":
        v = np.vstack([c["eye"]["l_hor"][i0:i1], c["eye"]["r_hor"][i0:i1]])
        v = np.where(np.abs(v) < EYE_RAIL * c["eye_rail"], v, np.nan)
        n = np.isfinite(v).sum(0)
        v = np.where(n > 0, np.nansum(v, 0) / np.maximum(n, 1), np.nan)
    else:
        v = c["eye"][f"{which}_hor"][i0:i1]
        v = np.where(np.abs(v) < EYE_RAIL * c["eye_rail"], v, np.nan)
    v = v[np.isfinite(v)]
    return float(v.mean()) if len(v) else np.nan


def eye_velocity(c, t0, t1):
    """Median horizontal eye velocity in [t0, t1), raw file units per second, of the mean of
    both eyes; saturated samples dropped. The median of the sample-to-sample velocity follows
    the slow phases of nystagmus and smooth pursuit, as quick phases and saccades are brief."""
    if c["eye"] is None:
        return np.nan
    et = c["eye_t"]
    i0, i1 = np.searchsorted(et, t0), np.searchsorted(et, t1)
    if i1 - i0 < 3:
        return np.nan
    v = np.vstack([c["eye"]["l_hor"][i0:i1], c["eye"]["r_hor"][i0:i1]]).astype(float)
    v = np.where(np.abs(v) < EYE_RAIL * c["eye_rail"], v, np.nan)
    vel = np.diff(v, axis=1) / np.diff(et[i0:i1])
    vel = np.nanmean(vel, 0)
    vel = vel[np.isfinite(vel)]
    return float(np.median(vel)) if len(vel) else np.nan


def return_turns(c):
    """Per trial, the passive return after it (tags 5xy before the next trial start): the sign
    of the total change of camera orientation (negative = to the right, as for code 1) and
    its start and end times."""
    t60 = c["t60"]
    tr = trials(c)
    ts = tr["t_start"]
    out = []
    dth = np.r_[0, (np.diff(t60[:, 3]) + 180) % 360 - 180]
    for i in range(len(ts) - 1):
        a, b = tr["t_end"][i], ts[i + 1]
        if not (np.isfinite(a) and np.isfinite(b)):
            continue
        m = (t60[:, 0] >= a) & (t60[:, 0] < b) & (t60[:, 10] >= 500) & (t60[:, 10] < 600)
        if m.sum() < 5:
            continue
        idx = np.nonzero(m)[0]
        tot = dth[idx[1:]].sum()
        out.append({"trial": i, "correct": bool(tr["correct"][i]), "t0": t60[idx[0], 0],
                    "t1": t60[idx[-1], 0], "dtheta": tot})
    return out


# ---------------------------------------------------------------- one pass over a data set

EYE_LAGS = np.round(np.arange(-1.0, 1.51, 0.1), 2)   # clock check, s from the turn code


def behaviour(c):
    """Session behaviour: trial table, learning curves, eye before turns and on returns."""
    tr = trials(c)
    turns = []
    for i, (ty, tt) in enumerate(zip(tr["turns"], tr["turn_t"])):
        for j, (code, t) in enumerate(zip(ty, tt)):
            row = {"trial": i, "k": j, "code": code, "correct": bool(tr["correct"][i])}
            for w in (0.5, 0.3):
                for which in ("mean", "l", "r"):
                    row[f"eye{int(w * 1000)}_{which}"] = eye_mean(c, t - w, t, which)
            for lag in EYE_LAGS:
                row[f"lag{lag}"] = eye_mean(c, t + lag, t + lag + 0.1)
            row["vel_0_600ms"] = eye_velocity(c, t, t + 0.6)
            row["vel_pre500"] = eye_velocity(c, t - 0.5, t)
            i0 = np.searchsorted(c["t60"][:, 0], t)
            i1 = np.searchsorted(c["t60"][:, 0], t + 0.6)
            if i1 < len(c["t60"]):
                row["dtheta_0_600ms"] = ((c["t60"][i1, 3] - c["t60"][i0, 3] + 180) % 360) - 180
            turns.append(row)
    t60 = c["t60"]
    clock = {}
    for nm, tt in (("start", tr["t_start"]), ("center", tr["t_center"]), ("reward", tr["t_reward"])):
        for sh in (0.0, -1.0, 1.0):
            i = np.searchsorted(t60[:, 0], tt[np.isfinite(tt)] + sh)
            i = i[i < len(t60)]
            clock[(nm, sh)] = float(np.nanmedian(t60[i, 4])) if len(i) else np.nan
    rets = return_turns(c)
    for r in rets:
        for which in ("mean", "l", "r"):
            r[f"eye_{which}"] = eye_mean(c, r["t0"], r["t1"], which)
        r["vel"] = eye_velocity(c, r["t0"], r["t1"])
    eye_sat = None
    if c["eye"] is not None:
        v = np.concatenate([c["eye"]["l_hor"], c["eye"]["r_hor"]])
        eye_sat = float(np.mean(np.abs(v) >= EYE_RAIL * c["eye_rail"]))
        eye_rng = (float(np.percentile(v, 1)), float(np.percentile(v, 99)))
    else:
        eye_rng = None
    # position at each trial start (the end of the start arm) and at reward (end of the chosen arm)
    pos = {}
    for nm, tt in (("start", tr["t_start"]), ("reward", tr["t_reward"])):
        i = np.searchsorted(t60[:, 0], np.where(np.isfinite(tt), tt, t60[0, 0]))
        i = np.minimum(i, len(t60) - 1)
        pos[nm] = np.where(np.isfinite(tt)[:, None], t60[i, 1:3], np.nan)
    nxt = np.r_[tr["t_start"][1:], np.nan]
    timing = {"reward_to_end": float(np.nanmedian(tr["t_end"] - tr["t_reward"])),
              "end_to_next_start": float(np.nanmedian(nxt - tr["t_end"]))}
    return {"monkey": c["monkey"], "session": c["session"], "n_trials": len(c["cm"]), "timing": timing,
            "pos_start": pos["start"], "pos_reward": pos["reward"],
            "start_arm": tr["start_arm"], "chosen_arm": tr["chosen_arm"],
            "correct": tr["correct"], "lc": c["lc"], "learningtrial": c["learningtrial"],
            "turns": turns, "returns": rets, "abscissa_at_events": clock, "eye_saturated": eye_sat, "eye_range": eye_rng,
            "has_eye": c["eye"] is not None,
            "eye_scale": None if c["eye"] is None else ("+-5000" if c["eye_rail"] > 10 else "+-5")}


def entry_headings(t60):
    """Circular mean camera orientation (degrees, 0 to 360) on each entry path (tags 10x)."""
    tag, th = t60[:, 10], np.deg2rad(t60[:, 3])
    out = {}
    for x in np.unique(tag[(tag >= 100) & (tag < 200)]).astype(int):
        m = tag == x
        out[x % 100] = int(round(np.rad2deg(np.arctan2(np.sin(th[m]).mean(), np.cos(th[m]).mean())) % 360))
    return out


def file_meta(name, d, c):
    fl = d["file"][0, 0]
    row = {"file": name, "monkey": name[:2], "session": name.split("_")[0],
           "fields": ",".join(fl.dtype.names), "has_newallo": c is not None}
    if c is not None:
        t60 = c["t60"]
        row.update({"spike_src": c["spike_src"], "n_spikes_file": len(c["spikes"]),
                    "n_trials": len(c["cm"]), "n_correct": int(trials(c)["correct"].sum()),
                    "t_start": c["window"][0], "t_end": c["window"][1],
                    "frames": len(t60), "frame_dt_ms": float(np.median(np.diff(t60[:, 0])) * 1000),
                    "x_min": float(np.nanmin(t60[:, 1])), "x_max": float(np.nanmax(t60[:, 1])),
                    "y_min": float(np.nanmin(t60[:, 2])), "y_max": float(np.nanmax(t60[:, 2])),
                    "theta_min": float(np.nanmin(t60[:, 3])), "theta_max": float(np.nanmax(t60[:, 3])),
                    "abscissa_min": float(np.nanmin(t60[:, 4])), "abscissa_max": float(np.nanmax(t60[:, 4])),
                    "abscissa_over_1": float(np.mean(t60[:, 4] > 1.001)),
                    "t60_cols": int(c["t60_shape_raw"][1]), "t60_rows_raw": int(c["t60_shape_raw"][0]),
                    "ss_angle_min": float(np.nanmin(t60[:, 6])), "ss_angle_max": float(np.nanmax(t60[:, 6])),
                    "ss_radius_min": float(np.nanmin(t60[:, 7])), "ss_radius_max": float(np.nanmax(t60[:, 7])),
                    "tag_next_min": float(np.nanmin(t60[:, 8])), "tag_next_max": float(np.nanmax(t60[:, 8])),
                    "tag_min": float(np.nanmin(t60[:, 10])), "tag_max": float(np.nanmax(t60[:, 10])),
                    "tag_hundreds": tuple(sorted(set((t60[:, 10] // 100).astype(int)))),
                    "entry_headings": entry_headings(t60),
                    "has_eye": c["eye"] is not None, "eye_units": c["eye_units"],
                    "eye_dt_ms": float(np.median(np.diff(c["eye_t"])) * 1000) if c["eye"] is not None else np.nan,
                    "spikes_in_window": int(np.sum((c["spikes"] >= c["window"][0]) & (c["spikes"] <= c["window"][1]))),
                    "spikes_sorted": bool(np.all(np.diff(np.asarray(fl["elec"] if "elec" in fl.dtype.names else c["spikes"], float).ravel()) >= 0)),
                    "reclocation": None if c["reclocation"] is None else tuple(np.round(c["reclocation"], 2)),
                    "learningtrial": c["learningtrial"],
                    "lc_order_ok": None if c["lc"] is None else bool(np.all(c["lc"][:, 1] <= c["lc"][:, 0] + 1e-9) and np.all(c["lc"][:, 0] <= c["lc"][:, 2] + 1e-9)),
                    "first_spikes": tuple(np.round(c["spikes"][:5], 4))})
    return row


def collect(dataset="hc-12", limit=None, log=print):
    """Stream a data set once and compute every per-cell and per-session quantity."""
    import time
    import zlib
    metas, cells, beh, lmk = [], [], {}, []
    sess_key, sess = None, None
    t0 = time.time()
    for i, (name, d) in enumerate(stream_members(dataset)):
        c = reduce_file(name, d)
        metas.append(file_meta(name, d, c))
        del d
        if c is None:
            continue
        key = (c["session"], len(c["cm"]), round(c["window"][0], 3))
        if key != sess_key:
            sess_key, sess = key, Session(c)
        out, s = analyse_cell(c, sess, zlib.crc32(name.encode()))
        two, onea, oneb, heads = landmark_tables(c, s, sess)
        a2 = anova_two(two) or {}
        out.update({f"lm2_{k}": v for k, v in a2.items()})
        out["lm1a_p"], out["lm1a_groups"] = anova_one(onea)
        out["lm1b_p"], out["lm1b_groups"] = anova_one(oneb)
        out["n_entry_frames_abscissa_over_1"] = int(np.sum(np.isfinite(c["t60"][:, 4]) & (c["t60"][:, 4] > 1.001)
                                                          & (sess.tag >= 100) & (sess.tag < 200)))
        out["n_laps"] = int(two.trial.nunique())
        two, onea, oneb, _ = landmark_tables(c, s, sess, laps="all")
        a2 = anova_two(two) or {}
        out.update({f"lm2all_{k}": v for k, v in a2.items()})
        out["lm1aall_p"], _ = anova_one(onea)
        out["lm1ball_p"], _ = anova_one(oneb)
        out["n_laps_all"] = int(two.trial.nunique())
        out["n_trials"] = len(c["cm"])
        cells.append(out)
        b = beh.get(c["session"])
        if b is None or b["n_trials"] < len(c["cm"]):
            beh[c["session"]] = behaviour(c)
        if log and (i % 20 == 0):
            log(f"{i + 1} files, {time.time() - t0:.0f} s")
        if limit and i + 1 >= limit:
            break
    return metas, cells, beh


def fingerprint(dataset, maze="newallo", log=print):
    """Per file of a data set: spike count and first spike times, trial count and first trial
    start in `maze`, for finding recordings deposited twice."""
    rows = []
    for name, d in stream_members(dataset):
        c = reduce_file(name, d, maze)
        fl = d["file"][0, 0]
        row = {"file": name, "session": name.split("_")[0], "fields": ",".join(fl.dtype.names),
               "has_maze": c is not None}
        if c is not None:
            row.update({"n_spikes": len(c["spikes"]), "spikes_head": tuple(np.round(c["spikes"][:20], 3)),
                        "n_trials": len(c["cm"]), "t_first": round(float(c["window"][0]), 3),
                        "codes_head": tuple(c["cm"][:10, 1].astype(int))})
        rows.append(row)
    return rows
