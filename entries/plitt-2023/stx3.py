"""Loading and per-session measures for dandiset 001710 (Plitt, Kaganovsky et al.).

Where each parameter comes from:

- DANDISET / VERSION: the most recent published version (notebook header).
- Days. File names count days from 0 (``ymaze-day0`` ... ``day5``); the paper counts
  from 1. Checked in the notebook: Ctrl-3 file day4 holds 1208 cells, the paper's
  Ctrl-3 day 5 (Fig 2A legend). ``DAY_OFFSET = 1``.
- Activity. The files hold dF/F (``processing/ophys/dF``), raw fluorescence and
  neuropil, but not the deconvolved "activity rates" of the paper (Methods, In vivo
  imaging: "deconvolved with a canonical calcium kernel"). The authors' code for these
  files (GiocomoLab/Plitt_Kaganovsky_Stx3_CA1 at ``CODE_COMMIT``, session.py,
  ``_load_nwb_data_dense`` and every analysis module, ``ts_key='F_dff'``) uses this dF/F
  as the activity signal. Assumption: activity = deposited dF/F.
- Spatial bins: 30 bins of 10 cm of the spline parameter, positions 13 to 43 (Methods,
  VR novel arm Y-maze; position description in the file).
- Speed: the files label speed "10 cm/s", but its integral over a trial is about 290, the
  300 cm track in cm; it is used as cm/s (a metadata error, shown in the notebook).
- Shuffles: 1000 within-trial circular shifts (Methods, Place cell identification and
  Single place field analyses). The same random shift is applied to every cell in one
  shuffle (shifting the position trace against all cells at once); each cell's null is
  then still a within-trial circular shift of its own time series (standard choice).
- Single fields: bins above the 95th percentile of the null, contiguous runs of at least
  2 bins (20 cm); formation lap as in Methods, Single place field analyses, with
  "significant activity" = the trial's binned rate in a field bin above 20% of the
  cell's maximum binned rate in the field (the Methods' rule applied to binned rates,
  a standard choice).
- HSEs: Methods, HSEs (speed < 2 cm/s for >= 750 ms after a reward; transient = rising
  crossing of 20% of the cell's session maximum; coactive within 500 ms, taken as 8
  frames at 15.46 Hz; the speed series in the files jitters by about 7 cm/s from frame to
  frame while the position is constant, so the stopping speed is taken from the change in
  the spline position (linear in ball movement, Methods, VR novel arm Y-maze), smoothed
  with a centred 15-frame (1 s) moving mean, a standard choice the paper does not state;
  threshold = 95th percentile of 1000 per-cell circular shuffles
  within each stopping period, pooled over time points; a second reading shifts only the
  onsets that began inside the period, see `hse`).
- Seeds: every random step takes a seed derived from the session name (standard choice).
"""
from __future__ import annotations

import io
import json
import re
import zipfile
import zlib
from functools import lru_cache

import h5py
import numpy as np
import remfile
import requests
import pandas as pd
import scipy.sparse as sps

DANDISET = "001710"
VERSION = "0.260213.0329"
API = "https://api.dandiarchive.org/api"
FIGSHARE_ARTICLE = 31286365
FIGSHARE_VERSION = 5
FIGSHARE_DOI = "10.6084/m9.figshare.31286365.v5"
CODE_REPO = "GiocomoLab/Plitt_Kaganovsky_Stx3_CA1"
CODE_COMMIT = "f2ab24db8709a321d38576a1fa674f95035a2fec"
DAY_OFFSET = 1
NBINS = 30
POS_MIN = 13.0
FRAME_RATE = 15.4609375
N_SHUFFLE = 1000


# --------------------------------------------------------------------------- assets
def list_assets(version: str = VERSION) -> list[dict]:
    """All assets of the pinned version, with subject, day and scan parsed from the path."""
    out, url = [], f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=200"
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        d = r.json()
        for a in d["results"]:
            m = re.match(r"sub-([A-Za-z]+)-(\d+)/.*ses-ymaze-day(\d)-scan(\d)", a["path"])
            rec = dict(path=a["path"], asset_id=a["asset_id"], size=a["size"])
            if m:
                rec.update(group=m.group(1), mouse=f"{m.group(1)}-{m.group(2)}",
                           file_day=int(m.group(3)), scan=int(m.group(4)))
            out.append(rec)
        url = d.get("next")
    return out


def asset_url(asset_id: str) -> str:
    r = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60)
    return r.url


def open_asset(asset_id: str) -> h5py.File:
    return h5py.File(remfile.File(asset_url(asset_id)), "r")


def read_metadata(asset_id: str) -> dict:
    """Session metadata and array shapes only (no data). Multiplexed (sparse KO) files hold
    two channels and other names; their shapes are read where present."""
    def txt(f, k):
        return f[k][()].decode() if k in f else None
    with open_asset(asset_id) as f:
        meta = json.loads(f["acquisition/trial_cell_data/data"][0])
        oph = f["processing/ophys"]
        dkey = "dF/dF" if "dF" in oph else [k for k in oph if k.endswith(" df")][0] + "/" + [k for k in oph if k.endswith(" df")][0]
        out = dict(
            subject_id=txt(f, "general/subject/subject_id"),
            subject_description=txt(f, "general/subject/description"),
            experiment_description=txt(f, "general/experiment_description"),
            location=txt(f, "general/optophysiology/ImagingPlane/location"),
            imaging_rate=float(f["general/optophysiology"][list(f["general/optophysiology"])[0]]["imaging_rate"][()]),
            dff_shape=oph[dkey]["data"].shape,
            dff_rate=float(oph[dkey]["starting_time"].attrs["rate"]),
            n_rois=f["processing/ophys/ImageSegmentation/PlaneSegmentation/id"].shape[0]
            if "ImageSegmentation/PlaneSegmentation" in oph else -1,
            n_aligned=_first_shape(f["processing/behavior"], "position/data"),
            meta_day=meta["day"], novel_arm=meta["novel_arm"], mux=meta["mux"],
            n_trials=len(meta["trial_start_inds"]),
        )
    return out


def _first_shape(g, suffix):
    found = []
    g.visititems(lambda n, o: found.append(o.shape[0]) if n.endswith(suffix) and isinstance(o, h5py.Dataset) else None)
    return found[0] if found else -1


def read_all_metadata(asset_ids: list[str], workers: int = 8) -> list[dict]:
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(read_metadata, asset_ids))


# --------------------------------------------------------------------------- ROI alignment
@lru_cache(maxsize=1)
def _aligner_zip() -> zipfile.ZipFile:
    d = requests.get(f"https://api.figshare.com/v2/articles/{FIGSHARE_ARTICLE}/versions/"
                     f"{FIGSHARE_VERSION}", timeout=60).json()
    url = [x["download_url"] for x in d["files"] if x["name"] == "roi_aligners.zip"][0]
    return zipfile.ZipFile(io.BytesIO(requests.get(url, timeout=300).content))


def load_aligner(mouse: str) -> dict:
    """The authors' across-session ROI matches (Figshare, pinned version)."""
    import dill
    z = _aligner_zip()
    return dill.loads(z.read(f"roi_aligners/{mouse.replace('-', '_')}/roi_aligner_results.pkl"))


@lru_cache(maxsize=1)
def ravel_index() -> dict:
    """(mouse, file_day, scan) -> index of the session in the aligner, from the authors'
    mouse_metadata.py at the pinned commit (parsed, not executed)."""
    txt = requests.get(f"https://raw.githubusercontent.com/{CODE_REPO}/{CODE_COMMIT}/"
                       "src/stx3_2p_analyses/mouse_metadata.py", timeout=60).text
    out, mouse = {}, None
    for line in txt.splitlines():
        m = re.match(r"\s*'((?:Ctrl|Cre|SparseKO)_\d+)'\s*:\s*\{", line)
        if m:
            mouse = m.group(1).replace("_", "-")
        m = re.search(r"'day':\s*(\d+),\s*'scan':\s*(\d+).*'ravel_ind':\s*(\d+)", line)
        if m and mouse:
            out[(mouse, int(m.group(1)), int(m.group(2)))] = int(m.group(3))
    return out


def common_rois(matches: dict, inds: list[int]) -> np.ndarray:
    """ROI indices present in every listed session (the authors' utilities.common_rois):
    array (len(inds), n_common), row 0 the reference session."""
    ref = matches[inds[0]]
    common = None
    for t in inds[1:]:
        s = set(ref[t]["ref_inds"])
        common = s if common is None else common & s
    common = sorted(common)
    out = np.zeros((len(inds), len(common)), dtype=int)
    out[0] = common
    for j, t in enumerate(inds[1:]):
        lut = dict(zip(ref[t]["ref_inds"], ref[t]["targ_inds"]))
        out[j + 1] = [lut[c] for c in common]
    return out


# --------------------------------------------------------------------------- loading
def _load_scan(asset_id: str) -> dict:
    with open_asset(asset_id) as f:
        meta = json.loads(f["acquisition/trial_cell_data/data"][0])
        g = f["processing/behavior/2P-aligned behavior"]
        s = dict(
            meta=meta,
            pos=g["position/data"][:],
            speed=g["speed/data"][:],                  # cm/s (see SPEED_UNIT_NOTE)
            reward=g["reward/data"][:],
            dff=f["processing/ophys/dF/dF/data"][:].astype(np.float32),
        )
        h = f["processing/behavior/Full temporal resolution behavior"]
        s["full"] = dict(
            t=h["position/timestamps"][:],
            pos=h["position/data"][:],
            speed=h["speed/data"][:],
            lick=h["non-consummatory licks/data"][:].astype(float),
            reward=h["reward/data"][:].astype(float),
            start=h["trial start/data"][:],
            end=h["trial end/data"][:],
            LR=h["left or right/data"][:],
            block=h["block/data"][:],
        )
        pm = f["processing/ophys/ImageSegmentation/PlaneSegmentation"]
        idx = pm["pixel_mask_index"][:]
        px = pm["pixel_mask"][:]
        lo = np.r_[0, idx[:-1]]
        s["centroid"] = np.array([[px["x"][a:b].mean(), px["y"][a:b].mean()] for a, b in zip(lo, idx)])
    return s


def _bins(pos):
    b = np.floor(pos - POS_MIN).astype(int)
    b[(b < 0) | (b >= NBINS)] = -1
    return b


def _full_res_trials(full: dict) -> dict:
    """Per-trial behaviour at full resolution: time, licks and mean speed per bin."""
    st = np.flatnonzero(full["start"] == 1)
    en = np.flatnonzero(full["end"] == 1)
    dt = np.diff(full["t"], append=full["t"][-1])
    n = min(len(st), len(en))
    T = np.zeros((n, NBINS)); L = np.zeros((n, NBINS)); S = np.full((n, NBINS), np.nan)
    LR = np.zeros(n); blk = np.zeros(n); dur = np.zeros(n); dist = np.zeros(n)
    rew_pos = np.full(n, np.nan)
    for i in range(n):
        sl = slice(st[i], en[i])
        b = _bins(full["pos"][sl]); ok = b >= 0
        T[i] = np.bincount(b[ok], weights=dt[sl][ok], minlength=NBINS)
        L[i] = np.bincount(b[ok], weights=full["lick"][sl][ok], minlength=NBINS)
        sw = np.bincount(b[ok], weights=(full["speed"][sl] * dt[sl])[ok], minlength=NBINS)
        with np.errstate(invalid="ignore", divide="ignore"):
            S[i] = np.where(T[i] > 0, sw / T[i], np.nan)
        LR[i] = np.median(full["LR"][sl]); blk[i] = np.median(full["block"][sl])
        dur[i] = dt[sl][ok].sum(); dist[i] = (full["speed"][sl] * dt[sl])[ok].sum()
        r = np.flatnonzero(full["reward"][sl] > 0)
        if len(r):
            rew_pos[i] = full["pos"][sl][r[0]]
    return dict(time=T, licks=L, speed=S, LR=LR, block=blk, dur=dur, dist=dist, reward_pos=rew_pos)


def _concat_scans(scans: list[dict], mapping: np.ndarray | None) -> dict:
    """One session from one or more scans of a day; cells restricted to `mapping`."""
    if len(scans) == 1:
        s = scans[0]
        s["trial_info"] = {k: np.array(v) for k, v in s["meta"]["trial_info"].items()}
        s["starts"] = np.array(s["meta"]["trial_start_inds"])
        s["ends"] = np.array(s["meta"]["teleport_inds"])
        s["full_trials"] = _full_res_trials(s.pop("full"))
        return s
    out = dict(meta=scans[0]["meta"], pos=[], speed=[], reward=[], dff=[], starts=[], ends=[],
               trial_info={"LR": [], "block_number": []}, full_trials=[], centroid=None)
    off = 0
    for j, s in enumerate(scans):
        out["pos"].append(s["pos"]); out["speed"].append(s["speed"]); out["reward"].append(s["reward"])
        out["dff"].append(s["dff"][:, mapping[j]])
        out["starts"].append(np.array(s["meta"]["trial_start_inds"]) + off)
        out["ends"].append(np.array(s["meta"]["teleport_inds"]) + off)
        # block numbers restart at 0 in a day's second scan; they are continued from the
        # first scan's last block, as the authors' code does when it joins the scans of one
        # day (session.py at CODE_COMMIT: block_number + previous scan's last block + 1)
        bn = np.array(s["meta"]["trial_info"]["block_number"])
        boff = int(out["trial_info"]["block_number"][-1][-1]) + 1 if j > 0 and len(bn) and bn[0] == 0 else 0
        out["trial_info"]["LR"].append(np.array(s["meta"]["trial_info"]["LR"]))
        out["trial_info"]["block_number"].append(bn + boff)
        ft = _full_res_trials(s["full"])
        ft["block"] = ft["block"] + boff
        out["full_trials"].append(ft)
        off += len(s["pos"])
    for k in ("pos", "speed", "reward", "starts", "ends"):
        out[k] = np.concatenate(out[k])
    out["dff"] = np.concatenate(out["dff"], axis=0)
    out["trial_info"] = {k: np.concatenate(v) for k, v in out["trial_info"].items()}
    ft = out["full_trials"]
    out["full_trials"] = {k: np.concatenate([x[k] for x in ft]) for k in ft[0]}
    out["centroid"] = scans[0]["centroid"][mapping[0]]
    # place-cell info: from the scan with more trials (see notebook)
    return out


# --------------------------------------------------------------------------- measures
def _trial_maps(dff, bins, starts, ends):
    """Mean dF/F per trial and bin: (trials, bins, cells), occupancy (frames)."""
    nT, nC = len(starts), dff.shape[1]
    R = np.full((nT, NBINS, nC), np.nan, np.float32)
    occ = np.zeros((nT, NBINS))
    tmean = np.full((nT, nC), np.nan, np.float32)
    for i, (a, b) in enumerate(zip(starts, ends)):
        bb = bins[a:b]; ok = bb >= 0
        X = np.nan_to_num(dff[a:b][ok])
        cnt = np.bincount(bb[ok], minlength=NBINS)
        M = sps.csr_matrix((np.ones(ok.sum()), (bb[ok], np.arange(ok.sum()))), shape=(NBINS, ok.sum()))
        S = M @ X
        with np.errstate(invalid="ignore", divide="ignore"):
            R[i] = S / cnt[:, None]
        R[i][cnt == 0] = np.nan
        occ[i] = cnt
        tmean[i] = X.mean(0) if ok.sum() else np.nan
    return R, occ, tmean


def _skaggs(maps, occ_p):
    """Spatial information (bits per unit activity), rates clipped at 0. maps (..., bins, cells)."""
    lam = np.clip(maps, 0, None)
    mu = np.nansum(lam * occ_p[:, None], axis=-2, keepdims=True)
    with np.errstate(invalid="ignore", divide="ignore"):
        r = lam / mu
        t = np.where(r > 0, r * np.log2(r), 0.0)
    return np.nansum(occ_p[:, None] * t, axis=-2)


def shuffle_maps(dff, bins, starts, ends, trial_idx, n_shuffle, rng):
    """Observed trial-averaged map and the 95th percentile of the null maps (within-trial
    circular shifts), plus the shuffled spatial information for each cell."""
    frames, rows_b, tr_of = [], [], []
    for i in trial_idx:
        bb = bins[starts[i]:ends[i]]
        frames.append(np.arange(starts[i], ends[i])); rows_b.append(bb); tr_of.append(np.full(len(bb), i))
    fr = np.concatenate(frames); X = np.nan_to_num(dff[fr]).astype(np.float32)
    lens = np.array([len(b) for b in rows_b]); offs = np.r_[0, np.cumsum(lens)[:-1]]
    nC = X.shape[1]

    def weights(bseq):
        # 1/(count of that bin in the trial * number of trials visiting the bin)
        cnt = np.zeros((len(rows_b), NBINS))
        for j, b in enumerate(bseq):
            ok = b >= 0
            cnt[j] = np.bincount(b[ok], minlength=NBINS)
        ntr = (cnt > 0).sum(0)
        rows, cols, vals = [], [], []
        for j, b in enumerate(bseq):
            ok = np.flatnonzero(b >= 0)
            rows.append(b[ok]); cols.append(ok + offs[j])
            vals.append(1.0 / (cnt[j, b[ok]] * ntr[b[ok]]))
        W = sps.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
                           shape=(NBINS, len(fr)))
        occ_p = ntr / max(ntr.sum(), 1)
        return W, occ_p

    W, occ_p = weights(rows_b)
    obs = np.asarray(W @ X)
    occ_frames = np.zeros(NBINS)
    for b in rows_b:
        ok = b >= 0
        occ_frames += np.bincount(b[ok], minlength=NBINS)
    pocc = occ_frames / occ_frames.sum()
    si_obs = _skaggs(obs, pocc)
    null = np.empty((n_shuffle, NBINS, nC), np.float32)
    si_null = np.empty((n_shuffle, nC), np.float32)
    for k in range(n_shuffle):
        sh = [np.roll(b, rng.integers(len(b))) for b in rows_b]
        Wk, _ = weights(sh)
        null[k] = Wk @ X
        si_null[k] = _skaggs(null[k], pocc)
    thr = np.percentile(null, 95, axis=0)
    p_si = (si_null >= si_obs[None]).mean(0)
    return obs, thr, si_obs, p_si


def find_fields(obs, thr, R_type, min_bins=2):
    """Candidate fields (contiguous significant bins, >= 20 cm) and their formation laps.
    R_type: (trials of the type, bins, cells) in chronological order."""
    sig = obs > thr
    fields = []
    nT = R_type.shape[0]
    for c in range(obs.shape[1]):
        s = np.r_[False, sig[:, c], False].astype(int)
        d = np.diff(s); a = np.flatnonzero(d == 1); b = np.flatnonzero(d == -1)
        for lo, hi in zip(a, b):
            if hi - lo < min_bins:
                continue
            inf = R_type[:, lo:hi, c]
            mx = np.nanmax(inf) if np.isfinite(inf).any() else np.nan
            act = np.nanmax(np.where(np.isfinite(inf), inf, -np.inf), axis=1) > 0.2 * mx
            form = -1
            for t in range(nT):
                rest = act[t + 1:]
                if act[t] and len(rest) >= 4 and rest.mean() >= 0.66:
                    form = t
                    break
            fields.append((c, lo, hi, form))
    return fields


def field_laps(dff, pos, speed, starts, ends, trial_idx, field):
    """COM (spline units) of a field's activity on each lap, and mean speed in the field."""
    c, lo, hi, form = field
    coms, spd = [], []
    for i in trial_idx:
        p = pos[starts[i]:ends[i]]; x = np.clip(np.nan_to_num(dff[starts[i]:ends[i], c]), 0, None)
        m = (p >= POS_MIN + lo) & (p < POS_MIN + hi)
        w = x[m].sum()
        coms.append((p[m] * x[m]).sum() / w if w > 0 else np.nan)
        spd.append(speed[starts[i]:ends[i]][m].mean() if m.any() else np.nan)
    return np.array(coms), np.array(spd)


def hse(dff, pos, reward, starts, ends, rng, n_shuffle=N_SHUFFLE, min_stop=12, win=8, smooth=15, mode="series"):
    """HSEs in post-reward stopping periods. Returns per-trial HSE flag, list of HSE
    participant sets, threshold, and number of eligible periods.

    mode "series": each cell's activity is circularly shifted within the period and the
    onsets recomputed (the Methods' words). mode "onsets": each cell's onsets that began
    inside the period are circularly shifted (a reading in which only transients that
    began after the stop enter the null)."""
    nC = dff.shape[1]
    mx = np.nanmax(dff, axis=0)
    thr_act = 0.2 * mx
    periods = []
    for i, (a, b) in enumerate(zip(starts, ends)):
        r = np.flatnonzero(reward[a:b] > 0)
        if not len(r):
            continue
        r0 = a + r[0]
        v = np.r_[0.0, np.diff(np.nan_to_num(pos[a:b]))] * 10.0 * FRAME_RATE   # cm/s
        v = np.convolve(v, np.ones(smooth) / smooth, mode="same")[r0 - a:]
        still = np.abs(v) < 2.0
        s = np.r_[False, still, False].astype(int); d = np.diff(s)
        on = np.flatnonzero(d == 1); off = np.flatnonzero(d == -1)
        for lo, hi in zip(on, off):
            if hi - lo >= min_stop:
                periods.append((i, r0 + lo, r0 + hi))
    if not periods:
        return dict(trial_hse=np.zeros(len(starts), bool), events=[], thr=np.nan, n_periods=0,
                    frac_above=np.nan, period_s=np.nan)
    # rising edges: real (non-circular, j >= 1) and circular (for shuffles)
    real_on, circ = [], []
    for pid, (i, a, b) in enumerate(periods):
        A = np.nan_to_num(dff[a:b]) > thr_act[None]
        prev = np.vstack([np.zeros((1, nC), bool), A[:-1]])
        j, c = np.nonzero(A & ~prev); keep = j >= 1
        real_on.append((pid, j[keep], c[keep]))
        prevc = np.roll(A, 1, axis=0)
        j, c = np.nonzero(A & ~prevc)
        circ.append((np.full(len(j), pid), j, c, np.full(len(j), b - a)))
    L = np.array([b - a for _, a, b in periods]); off = np.r_[0, np.cumsum(L)[:-1]]
    tot = L.sum()

    def counts(pid, j):
        h = np.bincount(off[pid] + j, minlength=tot)
        out = np.empty(tot)
        for p in range(len(periods)):
            hp = np.r_[0, np.cumsum(h[off[p]:off[p] + L[p]])]
            k = np.arange(L[p])
            out[off[p]:off[p] + L[p]] = hp[np.minimum(k + win, L[p])] - hp[k]
        return out

    rp = np.concatenate([np.full(len(x[1]), x[0]) for x in real_on]).astype(int)
    rj = np.concatenate([x[1] for x in real_on]).astype(int)
    rc = np.concatenate([x[2] for x in real_on]).astype(int)
    if mode == "series":
        cp = np.concatenate([x[0] for x in circ]); cj = np.concatenate([x[1] for x in circ])
        cc = np.concatenate([x[2] for x in circ]); cL = np.concatenate([x[3] for x in circ])
    else:   # onsets live on 1..L-1
        cp, cj, cc = rp, rj - 1, rc
        cL = np.maximum(L[rp] - 1, 1)
    key = cp * nC + cc
    ukey, inv = np.unique(key, return_inverse=True)
    pooled = []
    for _ in range(n_shuffle):
        if len(cj) == 0:
            pooled.append(np.zeros(tot)); continue
        shift = rng.integers(0, 1 << 30, size=len(ukey))[inv] % cL
        nj = (cj + shift) % cL
        if mode == "series":
            keep = nj >= 1
            pooled.append(counts(cp[keep], nj[keep]))
        else:
            pooled.append(counts(cp, nj + 1))
    thr = np.percentile(np.concatenate(pooled), 95)
    cnt = counts(rp, rj)
    trial_hse = np.zeros(len(starts), bool)
    events = []
    for p, (i, a, b) in enumerate(periods):
        above = cnt[off[p]:off[p] + L[p]] > thr
        s = np.r_[False, above, False].astype(int); d = np.diff(s)
        for lo, hi in zip(np.flatnonzero(d == 1), np.flatnonzero(d == -1)):
            m = (rp == p) & (rj >= lo) & (rj < hi - 1 + win)
            events.append(dict(trial=i, cells=np.unique(rc[m])))
            trial_hse[i] = True
    return dict(trial_hse=trial_hse, events=events, thr=thr, n_periods=len(periods),
                frac_above=float((cnt > thr).mean()), period_s=float(L.mean() / FRAME_RATE))


def session_summary(asset_ids: list[str], mapping: np.ndarray | None = None, seed_name: str = "",
                    n_shuffle: int = N_SHUFFLE) -> dict:
    """Stream one day's scan(s) and reduce them to what the claims use."""
    seed = zlib.crc32(seed_name.encode())
    scans = [_load_scan(a) for a in asset_ids]
    pci_scans = [s["meta"]["place_cell_info"] for s in scans]
    ntr_scans = [len(s["meta"]["trial_start_inds"]) for s in scans]
    s = _concat_scans(scans, mapping)
    meta = s["meta"]
    novel = meta["novel_arm"]
    bins = _bins(s["pos"])
    R, occ, tmean = _trial_maps(s["dff"], bins, s["starts"], s["ends"])
    LR = s["trial_info"]["LR"]; block = s["trial_info"]["block_number"]
    nT = len(s["starts"])
    spd = np.full((nT, NBINS), np.nan)
    for i, (a, b) in enumerate(zip(s["starts"], s["ends"])):
        bb = bins[a:b]; ok = bb >= 0
        c = np.bincount(bb[ok], minlength=NBINS)
        with np.errstate(invalid="ignore", divide="ignore"):
            spd[i] = np.bincount(bb[ok], weights=s["speed"][a:b][ok], minlength=NBINS) / c
    # deposited place-cell info: the scan with most trials when a day is split
    j = int(np.argmax(ntr_scans))
    pci = pci_scans[j]
    dep = {}
    for arm in ("left", "right"):
        v = {k: np.array(x) for k, x in pci[arm].items()}
        if mapping is not None:
            v = {k: x[mapping[j]] for k, x in v.items()}
        dep[arm] = v
    nov_arm = "left" if novel == -1 else "right"
    fam_arm = "right" if novel == -1 else "left"
    out = dict(R=R, occ=occ, tmean=tmean, speed_bins=spd, LR=LR, block=block, novel_arm=novel,
               n_cells=s["dff"].shape[1], full=s["full_trials"], centroid=s["centroid"],
               dep_pc={"fam": dep[fam_arm], "nov": dep[nov_arm]}, n_scans=len(scans),
               scan_trials=ntr_scans)
    # shuffles, fields, SI recomputed, per trial type
    rng = np.random.default_rng(seed)
    out["fields"], out["si_p"], out["si_obs"], out["field_laps"] = {}, {}, {}, {}
    for tt, arm in (("fam", -novel), ("nov", novel)):
        idx = np.flatnonzero(LR == arm)
        if len(idx) < 2:
            continue
        obs, thr, si, p = shuffle_maps(s["dff"], bins, s["starts"], s["ends"], idx, n_shuffle, rng)
        out["si_p"][tt] = p
        out["si_obs"][tt] = si
        flds = find_fields(obs, thr, R[idx])
        out["fields"][tt] = flds
        laps = []
        for fl in flds:
            if fl[3] >= 0:
                com, fs = field_laps(s["dff"], s["pos"], s["speed"], s["starts"], s["ends"], idx, fl)
                laps.append(dict(field=fl, com=com, speed=fs))
        out["field_laps"][tt] = laps
    out["hse"] = hse(s["dff"], s["pos"], s["reward"], s["starts"], s["ends"],
                     np.random.default_rng(seed + 1))
    out["hse_on"] = hse(s["dff"], s["pos"], s["reward"], s["starts"], s["ends"],
                        np.random.default_rng(seed + 2), mode="onsets")
    # null check of the detector: each cell's whole dF/F series circularly shifted by its own
    # random offset, which removes synchrony between cells and keeps each cell's transients
    X = time_shuffled(s["dff"], np.random.default_rng(seed + 3))
    out["hse_null"] = hse(X, s["pos"], s["reward"], s["starts"], s["ends"], np.random.default_rng(seed + 4))
    out["hse_on_null"] = hse(X, s["pos"], s["reward"], s["starts"], s["ends"],
                             np.random.default_rng(seed + 5), mode="onsets")
    return out


def time_shuffled(dff, rng):
    """Each cell's series circularly shifted by an independent random offset over the session."""
    n = dff.shape[0]
    sh = rng.integers(0, n, dff.shape[1])
    idx = (np.arange(n)[:, None] - sh[None, :]) % n
    return np.take_along_axis(dff, idx, axis=0)


def synthetic_hse_check(rng, n_cells=300, n_trials=60, rate=0.02, stop_s=(1.0, 6.0), sync=0):
    """Detector check on synthetic sessions: independent cells with random transients
    (onset probability `rate` per frame, decaying 1 s), one post-reward stop per trial of
    random length; `sync` > 0 adds one synchronous event of that many cells in half the
    stops. Returns the fraction of trials flagged, under both null readings."""
    fr = FRAME_RATE
    run = int(8 * fr)
    starts, ends, rew, pos = [], [], [], []
    t = 0
    planted = []
    for i in range(n_trials):
        L = int(rng.uniform(*stop_s) * fr)
        p_run = np.linspace(POS_MIN, POS_MIN + 29, run)
        p_stop = np.full(L, POS_MIN + 29)
        pos.append(np.r_[p_run, p_stop]); r = np.zeros(run + L); r[run] = 1; rew.append(r)
        starts.append(t); ends.append(t + run + L)
        if sync and i % 2 == 0 and L > 20:
            planted.append(t + run + int(rng.integers(5, L - 10)))
        t += run + L
    pos = np.concatenate(pos); rew = np.concatenate(rew)
    on = rng.random((t, n_cells)) < rate
    for t0 in planted:
        on[t0:t0 + 3, rng.choice(n_cells, sync, replace=False)] = True
    k = np.exp(-np.arange(int(fr)) / (fr / 3))
    dff = np.apply_along_axis(lambda x: np.convolve(x, k)[:t], 0, on.astype(float)).astype(np.float32)
    dff += rng.normal(0, 0.05, dff.shape).astype(np.float32)
    out = {}
    for mode in ("series", "onsets"):
        h = hse(dff, pos, rew, np.array(starts), np.array(ends), rng, n_shuffle=200, mode=mode)
        out[mode] = dict(frac_trials=float(h["trial_hse"].mean()), n_hse=len(h["events"]), thr=h["thr"])
    return out


# --------------------------------------------------------------------------- driver
def day_groups(assets: list[dict], groups=("Ctrl", "Cre")) -> dict:
    """(mouse, file_day) -> asset records of that day, sorted by scan."""
    out = {}
    for a in assets:
        if a.get("group") in groups:
            out.setdefault((a["mouse"], a["file_day"]), []).append(a)
    return {k: sorted(v, key=lambda r: r["scan"]) for k, v in sorted(out.items())}


def split_mapping(mouse: str, recs: list[dict]) -> np.ndarray | None:
    """For a day split over two files, the ROIs present in both (authors' ROI matches)."""
    if len(recs) == 1:
        return None
    ri = ravel_index()
    inds = [ri[(mouse, r["file_day"], r["scan"])] for r in recs]
    return common_rois(load_aligner(mouse), inds)


def _summ_job(args):
    key, ids, mapping, n_shuffle = args
    return key, session_summary(ids, mapping, seed_name=f"{key[0]}-day{key[1]}", n_shuffle=n_shuffle)


def summarize_all(groups: dict, workers: int = 4, n_shuffle: int = N_SHUFFLE) -> dict:
    """Run session_summary on every day, in parallel processes."""
    from concurrent.futures import ProcessPoolExecutor
    jobs = [(k, [r["asset_id"] for r in v], split_mapping(k[0], v), n_shuffle) for k, v in groups.items()]
    out = {}
    with ProcessPoolExecutor(workers) as ex:
        for key, res in ex.map(_summ_job, jobs):
            out[key] = res
    return out


# --------------------------------------------------------------------------- statistics
CTRL = [f"Ctrl-{i}" for i in range(1, 10)]
CRE = [f"Cre-{i}" for i in range(1, 8)]


def virus_of(mouse: str) -> str:
    return "ctrl" if mouse.startswith("Ctrl") else "cre"


def mixed(df, dv, within="day"):
    """pingouin mixed ANOVA (virus between, `within` within, mouse subject); complete
    cases only. Returns dict of F, p, df for virus, within and interaction."""
    import pingouin as pg
    d = df.dropna(subset=[dv])
    n_lv = d[within].nunique()
    full = d.groupby("mouse")[within].nunique()
    d = d[d["mouse"].isin(full[full == n_lv].index)]
    a = pg.mixed_anova(data=d, dv=dv, within=within, between="virus", subject="mouse")
    out = {"n_ctrl": d.loc[d.virus == "ctrl", "mouse"].nunique(),
           "n_cre": d.loc[d.virus == "cre", "mouse"].nunique()}
    for src, name in ((["virus"], "virus"), ([within], within), (["Interaction"], "inter")):
        r = a[a["Source"].isin(src)].iloc[0]
        out[name] = dict(F=float(r["F"]), p=float(r["p_unc"] if "p_unc" in r.index else r["p-unc"]), df1=int(r["DF1"]), df2=int(r["DF2"]))
    return out


def fmt_mixed(m, within="day"):
    v, w, i = m["virus"], m[within], m["inter"]
    return (f"N={m['n_ctrl']} ctrl, {m['n_cre']} cre; virus F({v['df1']},{v['df2']})={v['F']:.3g} "
            f"p={v['p']:.3g}; {within} F({w['df1']},{w['df2']})={w['F']:.3g} p={w['p']:.3g}; "
            f"interaction F({i['df1']},{i['df2']})={i['F']:.3g} p={i['p']:.3g}")


def ttest2(a, b):
    """Student's and Welch's unpaired t-tests of a against b."""
    from scipy import stats
    a, b = np.asarray(a, float), np.asarray(b, float)
    a, b = a[np.isfinite(a)], b[np.isfinite(b)]
    s = stats.ttest_ind(a, b); w = stats.ttest_ind(a, b, equal_var=False)
    return dict(t=float(s.statistic), p=float(s.pvalue), t_welch=float(w.statistic),
                p_welch=float(w.pvalue), n=(len(a), len(b)), diff=float(a.mean() - b.mean()))


def holm(p):
    p = np.asarray(p, float); n = len(p); o = np.argsort(p)
    adj = np.empty(n); run = 0
    for r, i in enumerate(o):
        run = max(run, (n - r) * p[i]); adj[i] = min(run, 1.0)
    return adj


def clock_check(asset_id: str, shifts=(-60, -30, -15, -8, -4, 0, 4, 8, 15, 30, 60)) -> pd.DataFrame:
    """Split-half (odd/even trial) reliability of the trial-averaged maps of all cells, with
    dF/F shifted against the position trace by `shifts` frames. Peaks at 0 when the
    imaging and the VR trace share a clock."""
    s = _concat_scans([_load_scan(asset_id)], None)
    rows = []
    for sh in shifts:
        d = np.roll(s["dff"], sh, axis=0)
        R, _, _ = _trial_maps(d, _bins(s["pos"]), s["starts"], s["ends"])
        fam = np.flatnonzero(s["trial_info"]["LR"] == -s["meta"]["novel_arm"])
        a = np.nanmean(R[fam[0::2]], 0); b = np.nanmean(R[fam[1::2]], 0)
        a = a - a.mean(0); b = b - b.mean(0)
        r = (a * b).sum(0) / np.sqrt((a * a).sum(0) * (b * b).sum(0))
        rows.append(dict(shift_frames=sh, shift_s=sh / FRAME_RATE, median_split_half_r=float(np.nanmedian(r))))
    return pd.DataFrame(rows)


# --------------------------------------------------------------------------- imaging measures
def _decoder_input(R):
    """The authors' decoder input (naive_bayes.py at CODE_COMMIT): dF/F x 10, minus its
    minimum over cells in each trial and bin, NaN -> 0, plus 1e-3, so rates are positive."""
    X = R * 10.0
    X = X - np.nanmin(X, axis=-1, keepdims=True)
    X = np.nan_to_num(X) + 1e-3
    return X


def decode_loo(R, occ, rng, n_cells=128, n_iter=50):
    """Leave-one-trial-out maximum likelihood decoding (Poisson log likelihood with
    continuous rates, uniform prior), n_cells drawn with replacement, n_iter draws
    (n_cells=None: every cell once).
    Returns the mean absolute error in cm over visited bins of every trial."""
    X = _decoder_input(R)
    n = X.shape[0]
    if n < 3:
        return np.nan
    valid = occ > 0
    errs = []
    for _ in range(n_iter):
        Y = X if n_cells is None else X[:, :, rng.integers(0, X.shape[2], n_cells)]
        lam = (Y.sum(0)[None] - Y) / (n - 1)
        LL = np.einsum("tbk,tjk->tbj", Y, np.log(lam)) - lam.sum(-1)[:, None, :]
        dec = LL.argmax(-1)
        err = np.abs(dec - np.arange(NBINS)[None]) * 10.0
        errs.append(err[valid].mean())
    return float(np.mean(errs))


def decode_cross(train_R, test_R, test_occ):
    """Decoder fit on the mean map of train_R (all its trials) and tested on every trial of test_R."""
    Xtr = _decoder_input(train_R); Xte = _decoder_input(test_R)
    lam = Xtr.mean(0)
    LL = np.einsum("tbk,jk->tbj", Xte, np.log(lam)) - lam.sum(-1)[None, None, :]
    err = np.abs(LL.argmax(-1) - np.arange(NBINS)[None]) * 10.0
    return float(err[test_occ > 0].mean())


def pv_corr(a, b, reading):
    """Population vector correlation of two (bins, cells) maps: reading 'a' Pearson of the
    flattened maps; 'b' mean over bins of the Pearson correlation of the cell vectors."""
    a = np.nan_to_num(a); b = np.nan_to_num(b)
    if reading == "a":
        return float(np.corrcoef(a.ravel(), b.ravel())[0, 1])
    a = a - a.mean(1, keepdims=True); b = b - b.mean(1, keepdims=True)
    with np.errstate(invalid="ignore", divide="ignore"):
        r = (a * b).sum(1) / np.sqrt((a * a).sum(1) * (b * b).sum(1))
    return float(np.nanmean(r))


def pairwise_pv(R, reading):
    """Mean over trial pairs (upper triangle) of the PV correlation of single-trial maps."""
    X = np.nan_to_num(R)
    n = X.shape[0]
    if n < 2:
        return np.nan
    if reading == "a":
        C = np.corrcoef(X.reshape(n, -1))
    else:
        Z = X - X.mean(2, keepdims=True)
        nr = np.sqrt((Z * Z).sum(2))
        with np.errstate(invalid="ignore", divide="ignore"):
            C = np.nanmean(np.einsum("ibk,jbk->ijb", Z, Z) / (nr[:, None, :] * nr[None, :, :]), axis=2)
    iu = np.triu_indices(n, 1)
    return float(np.nanmean(C[iu]))


def xcorr_shift(a, b, clip_negative=False):
    """Spatial cross-correlation of two (bins, cells) maps at lags -29..29 bins (PV
    correlation over the overlapping bins) and its centre of mass in cm. Negative = b is
    shifted backward (to earlier positions) relative to a."""
    a = np.nan_to_num(a); b = np.nan_to_num(b)
    lags = np.arange(-(NBINS - 1), NBINS)
    c = np.full(len(lags), np.nan)
    for k, L in enumerate(lags):
        if L >= 0:
            x, y = a[:NBINS - L], b[L:]
        else:
            x, y = a[-L:], b[:NBINS + L]
        x = x.ravel(); y = y.ravel()
        if x.std() > 0 and y.std() > 0:
            c[k] = np.corrcoef(x, y)[0, 1]
    # b[b0 + L] matches a[b0]: a field that moved backward in b matches at L < 0
    c = np.nan_to_num(c)
    if clip_negative:
        c = np.clip(c, 0, None)
    if c.sum() == 0:
        return np.nan
    return float((lags * c).sum() / c.sum() * 10.0)


def initial_shift(Rn, clip_negative=False, n_first=5):
    """Mean of the upper triangle of the trial x trial COM matrix of the first five trials."""
    X = Rn[:n_first]
    vals = [xcorr_shift(X[i], X[j], clip_negative) for i in range(len(X)) for j in range(i + 1, len(X))]
    return float(np.nanmean(vals)) if vals else np.nan


def cell_trial_corr(R):
    """Per cell, mean Pearson correlation of its single-trial maps over all trial pairs."""
    X = np.nan_to_num(R)                      # (n, bins, cells)
    n = X.shape[0]
    Z = X - X.mean(1, keepdims=True)
    nr = np.sqrt((Z * Z).sum(1))              # (n, cells)
    with np.errstate(invalid="ignore", divide="ignore"):
        C = np.einsum("ibc,jbc->ijc", Z, Z) / (nr[:, None, :] * nr[None, :, :])
    iu = np.triu_indices(n, 1)
    return np.nanmean(C[iu[0], iu[1], :], axis=0)


def logit_prop(k, n):
    """logit of k/n with 0 and 1 moved by half a cell (standard choice)."""
    p = np.clip(k, 0.5, n - 0.5) / n
    return np.log(p / (1 - p))


def _hse_job(args):
    key, ids, mapping = args
    seed = zlib.crc32(f"{key[0]}-day{key[1]}".encode())
    s = _concat_scans([_load_scan(a) for a in ids], mapping)
    return key, {m: hse(s["dff"], s["pos"], s["reward"], s["starts"], s["ends"],
                        np.random.default_rng(seed + (1 if m == "series" else 2)), mode=m)
                 for m in ("series", "onsets")}


def cross_pv(Ra, Rb, reading):
    """Mean PV correlation over all pairs of a single trial of Ra and a single trial of Rb
    (trials, bins, cells), readings as `pv_corr`."""
    A = np.nan_to_num(Ra); B = np.nan_to_num(Rb)
    if len(A) == 0 or len(B) == 0:
        return np.nan
    if reading == "a":
        a = A.reshape(len(A), -1); b = B.reshape(len(B), -1)
        a = a - a.mean(1, keepdims=True); b = b - b.mean(1, keepdims=True)
        with np.errstate(invalid="ignore", divide="ignore"):
            C = (a @ b.T) / np.outer(np.sqrt((a * a).sum(1)), np.sqrt((b * b).sum(1)))
        return float(np.nanmean(C))
    a = A - A.mean(2, keepdims=True); b = B - B.mean(2, keepdims=True)
    na = np.sqrt((a * a).sum(2)); nb = np.sqrt((b * b).sum(2))
    with np.errstate(invalid="ignore", divide="ignore"):
        C = np.einsum("ibk,jbk->ijb", a, b) / (na[:, None, :] * nb[None, :, :])
    return float(np.nanmean(C))


def synthetic_shift_check(rng, true_shift_bins=-3, n_cells=200, noise=0.5, n_rep=20):
    """`xcorr_shift` on synthetic maps: Gaussian fields (width 2 bins) at random centres,
    the second map moved by `true_shift_bins`, both with Gaussian noise. Returns the
    recovered shifts (cm) for the raw and the clipped centre of mass."""
    x = np.arange(NBINS)
    out = {"raw": [], "clipped": []}
    for _ in range(n_rep):
        c = rng.uniform(0, NBINS, n_cells)
        a = np.exp(-0.5 * ((x[:, None] - c[None]) / 2.0) ** 2)
        b = np.exp(-0.5 * ((x[:, None] - c[None] - true_shift_bins) / 2.0) ** 2)
        a = a + rng.normal(0, noise, a.shape); b = b + rng.normal(0, noise, b.shape)
        out["raw"].append(xcorr_shift(a, b)); out["clipped"].append(xcorr_shift(a, b, True))
    return {k: np.array(v) for k, v in out.items()}
