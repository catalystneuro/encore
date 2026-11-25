"""Loading and measures for Peterson et al. (2021) on DANDI:000055 (AJILE12).

Everything is streamed from the archive at a pinned version; nothing is written to disk.

Where each parameter comes from:

- Spectral method (claims file, opening comment, from the paper's Methods and code): Morlet
  wavelet power at 1 to 121 Hz in 5 Hz steps with n_cycles = frequency / 4, MNE's wavelet
  definition (sigma_t = n_cycles / (2 pi f), support of 5 sigma_t on each side, normalised;
  zero_mean False, the MNE 0.19 default of the code), decimated by 50 samples (10 Hz bins at
  500 Hz) aligned on the event, 10*log10 power. Because n_cycles / f is the same at every
  frequency, every wavelet spans +-0.2 s, so power is computed only at the time bins used here
  (-1.5 s to +1.0 s around onset); this gives the same values as convolving the whole 10 s
  segment.
- Baseline: each event's mean over the bins -1.5 to -1 s (inclusive) is subtracted, per
  electrode and frequency (claims file).
- Band power: bins 0 to 0.5 s (inclusive), LFB 11-31 Hz bins, HFB 76-96 Hz bins (claims file).
  The band mean (Methods) and the band median (code: median over time, then over frequency)
  are both returned.
- Segment rejection (Methods, "ECoG-event synchronization and segmentation": "discarding
  segments with power <0 dB or with abnormally high power at 115-125 Hz (>3 SDs) compared with
  all segments"). The paper does not say how power is pooled over electrodes and
  frequencies. Assumption: Welch PSD (1 s Hann windows) of the 10 s segment centred on the
  event, averaged over the session's good electrodes; the segment's power is 10*log10 of the
  mean PSD over 1-200 Hz, and its high-frequency power 10*log10 of the mean over 115-125 Hz,
  compared with the mean + 3 SD over all of the subject's segments. Segments that run past the
  ends of the recording, or that hold exact zeros on every electrode (the preprocessing zeroes
  artifacts and breaks), count as missing data.
- Good electrodes: the `good` column of each session's electrodes table (Methods: bad
  electrodes removed). It differs between sessions of a subject; each event uses the flags of
  its own session (assumption, stated in the notebook).
- Region projection (claims file; Methods "Projecting power into regions of interest"): the
  paper's own projection matrices from Figshare item 12114408 v1, rows matched to the
  electrodes by order, bad electrodes weight 0, each region's weights renormalised to sum 1.
- Pose windows for Extended Data Figure 2-1c: -1.5 to +1.5 s around onset at 30 Hz (claims
  file criterion: baseline -1.5 to -1 s, window 0 to 1.5 s).
"""

import io
import zlib
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET = "000055"
VERSION = "0.261123.1703"
API = "https://api.dandiarchive.org/api"
FIGSHARE_ITEM = 12114408  # ROI projection matrices and labels, version 1

FS = 500.0
FREQS = np.arange(1, 122, 5).astype(float)
N_CYCLES = FREQS / 4.0
DECIM = 50
BIN_T = np.round(np.arange(-1.5, 1.0001, 0.1), 1)  # time bins kept, s
BASE = (BIN_T >= -1.5) & (BIN_T <= -1.0)
WIN = (BIN_T >= 0.0) & (BIN_T <= 0.5)
LFB = (FREQS >= 8) & (FREQS <= 32)
HFB = (FREQS >= 76) & (FREQS <= 100)
SEG_HALF = 5.0  # 10 s segments centred on the event
SHIFT_S = -3.0  # pseudo-onset for the clock check: 3 s before the event, inside the same segment
ROIS = ["Frontal_Mid_L", "Precentral_L", "Postcentral_L", "Parietal_Inf_L",
        "SupraMarginal_L", "Temporal_Sup_L", "Temporal_Mid_L", "Temporal_Inf_L"]
ROI_NAMES = ["middle frontal", "precentral", "postcentral", "inferior parietal",
             "supramarginal", "superior temporal", "middle temporal", "inferior temporal"]
FEATURES = ["day", "time_of_day", "duration", "magnitude", "angle", "onset_speed",
            "speech_ratio", "bimanual_ratio", "bimanual_overlap", "bimanual_class"]


def list_assets():
    """Assets of the pinned version, with subject and session parsed from the path."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    rows = []
    while url:
        r = requests.get(url, timeout=60).json()
        rows += r["results"]
        url = r["next"]
    df = pd.DataFrame([{"path": a["path"], "asset_id": a["asset_id"], "size": a["size"]} for a in rows])
    df["subject"] = df.path.str.extract(r"sub-(\d+)/")[0].astype(int)
    df["session"] = df.path.str.extract(r"_ses-(\d+)_")[0].astype(int)
    return df.sort_values(["subject", "session"]).reset_index(drop=True)


def s3_url(asset_id):
    return requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60).url


def open_nwb(asset_id):
    url = s3_url(asset_id)
    return h5py.File(remfile.File(url), "r"), url


def _txt(v):
    return v.decode() if isinstance(v, bytes) else v


def load_session_meta(asset_id):
    """Small datasets of one file: subject, electrodes, reaches, epochs, series shapes."""
    f, _ = open_nwb(asset_id)
    e = f["general/extracellular_ephys/electrodes"]
    el = pd.DataFrame({k: e[k][:] for k in e.keys() if k != "group"})
    for c in ("group_name", "location"):
        el[c] = el[c].map(_txt)
    rt = f["intervals/reaches"]
    reaches = pd.DataFrame({k: rt[k][:] for k in rt.keys()})
    ep = f["intervals/epochs"]
    epochs = pd.DataFrame({k: ep[k][:] for k in ep.keys()})
    epochs["labels"] = epochs["labels"].map(_txt)
    groups = {k: _txt(v.attrs.get("description", "")) for k, v in f["general/extracellular_ephys"].items()
              if isinstance(v, h5py.Group) and v.attrs.get("neurodata_type") in (b"ElectrodeGroup", "ElectrodeGroup")}
    es = f["acquisition/ElectricalSeries"]
    pos = f["processing/behavior/Position"]
    out = dict(
        asset_id=asset_id,
        subject_id=_txt(f["general/subject/subject_id"][()]),
        age=_txt(f["general/subject/age"][()]),
        sex=_txt(f["general/subject/sex"][()]),
        session_id=_txt(f["general/session_id"][()]),
        session_start=_txt(f["session_start_time"][()]),
        session_description=_txt(f["session_description"][()]),
        electrodes=el, groups=groups, reaches=reaches, epochs=epochs,
        event_times=f["processing/behavior/ReachEvents/timestamps"][:],
        event_wrist=_txt(f["processing/behavior/ReachEvents"].attrs["description"]),
        ecog_shape=es["data"].shape,
        ecog_rate=float(es["starting_time"].attrs["rate"]),
        ecog_start=float(es["starting_time"][()]),
        ecog_conversion=float(es["data"].attrs["conversion"]),
        ecog_unit=_txt(es["data"].attrs["unit"]),
        ecog_chunks=es["data"].chunks,
        es_electrodes=es["electrodes"][:],
        pose_series=sorted(pos.keys()),
        pose_shape=pos["R_Wrist/data"].shape,
        pose_rate=float(pos["R_Wrist/starting_time"].attrs["rate"]),
        pose_start=float(pos["R_Wrist/starting_time"][()]),
        pose_unit=_txt(pos["R_Wrist/data"].attrs["unit"]),
    )
    f.close()
    return out


def load_all_meta(assets, workers=12):
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(load_session_meta, assets.asset_id))


def fold_angle(a):
    """Fold reach angles (degrees, -180 to 180) to -90..90 (Methods: 90-270 mapped to 90..-90).

    An angle a in (90, 270) (that is, a > 90 or a < -90) becomes 180 - a, wrapped to -90..90.
    """
    a = np.mod(np.asarray(a, float), 360.0)
    out = np.where(a <= 90, a, np.where(a >= 270, a - 360, 180 - a))
    return out


def event_table(metas):
    """One row per reach event, with the ten features of the paper."""
    rows = []
    for m in metas:
        r = m["reaches"].copy()
        r["subject"] = int(m["subject_id"])
        r["day"] = int(m["session_id"])
        r["asset_id"] = m["asset_id"]
        r["ev_index"] = np.arange(len(r))
        rows.append(r)
    ev = pd.concat(rows, ignore_index=True)
    ev["time_of_day"] = ev.start_time / 3600.0  # hours after midnight (session_description)
    ev["duration"] = ev.stop_time - ev.start_time
    ev["magnitude"] = ev.Reach_magnitude_px
    ev["angle_raw"] = ev.Reach_angle_degrees
    # The stored angle is in image coordinates (y grows downward; checked against the pose in
    # the notebook). The code negates it before folding, so that +90 is upward (Methods).
    ev["angle"] = fold_angle(-ev.Reach_angle_degrees.values)
    ev["onset_speed"] = ev.Onset_speed_px_per_sec
    ev["speech_ratio"] = ev.Speech_ratio
    ev["bimanual_ratio"] = ev.Bimanual_ratio.fillna(0.5)
    ev["bimanual_overlap"] = ev.Bimanual_overlap
    ev["bimanual_class"] = ev.Bimanual_class
    return ev


# ----------------------------------------------------------------------------- figshare inputs

def figshare_files():
    r = requests.get(f"https://api.figshare.com/v2/articles/{FIGSHARE_ITEM}/versions/1", timeout=60).json()
    return {f["name"]: f["download_url"] for f in r["files"]}, r


def load_projection(subject, files):
    """Projection matrix (rows = electrodes in file order, columns = AAL regions) and centroids."""
    m = pd.read_csv(io.StringIO(requests.get(files[f"aal_{subject:02d}_elecs2ROI.csv"], timeout=60).text))
    c = pd.read_csv(io.StringIO(requests.get(files[f"aal_{subject:02d}_ROIcentroids_Lside.csv"], timeout=60).text))
    return m, c


# ----------------------------------------------------------------------------- spectral

def morlet_bank():
    """MNE's Morlet wavelets (mne.time_frequency.morlet, zero_mean=False), one column per frequency."""
    sigma_t = N_CYCLES / (2.0 * np.pi * FREQS)
    ws = []
    for f, s in zip(FREQS, sigma_t):
        t = np.arange(0.0, 5.0 * s, 1.0 / FS)
        t = np.r_[-t[::-1], t[1:]]
        w = np.exp(2j * np.pi * f * t) * np.exp(-t ** 2 / (2.0 * s ** 2))
        w /= np.sqrt(0.5) * np.linalg.norm(w.ravel())
        ws.append(w)
    n = max(len(w) for w in ws)
    bank = np.zeros((n, len(FREQS)), complex)
    for i, w in enumerate(ws):
        o = (n - len(w)) // 2
        bank[o:o + len(w), i] = w
    return bank


def band_stats(spec):
    """spec: (..., n_freq, n_bins) dB. Returns band mean and code-style median for LFB and HFB."""
    w = spec[..., :, WIN]
    out = {}
    for name, sel in (("lfb", LFB), ("hfb", HFB)):
        b = w[..., sel, :]
        out[name + "_mean"] = b.mean(axis=(-2, -1))
        out[name + "_median"] = np.median(np.median(b, axis=-1), axis=-1)
    return out


def _segment_psd(seg):
    from scipy.signal import welch
    f, p = welch(seg, fs=FS, nperseg=int(FS), axis=-1)
    return f, p


def _range(sess, url, off, n):
    for attempt in range(5):
        try:
            r = sess.get(url, headers={"Range": f"bytes={off}-{off + n - 1}"}, timeout=300)
            r.raise_for_status()
            return r.content
        except Exception:
            if attempt == 4:
                raise


def chunk_index(ds, url, sess, n_threads=16):
    """Address and size of every chunk of a chunked 2-D dataset, read from the file's version 1
    B-tree with parallel range requests (h5py's own lookups go node by node over the network and
    take about 0.1 s each). Returns {(row offset, column offset): (address, size)}."""
    import struct
    parent, name = ds.name.rsplit("/", 1)
    addr = h5py.h5g.get_objinfo(ds.file[parent].id, name.encode()).objno[0]
    hdr = _range(sess, url, addr, 4096)
    assert hdr[0] == 1, "object header version 1 expected"
    nmsg = struct.unpack("<H", hdr[2:4])[0]
    blocks = [(hdr, 16, 16 + struct.unpack("<I", hdr[8:12])[0])]
    root = None
    seen = 0
    while blocks and root is None:
        buf, p, end = blocks.pop(0)
        while p + 8 <= end and seen < nmsg:
            mtype, msize = struct.unpack("<HH", buf[p:p + 4])
            data = buf[p + 8:p + 8 + msize]
            seen += 1
            if mtype == 8:  # data layout, version 3, chunked
                assert data[0] == 3 and data[1] == 2, "chunked layout version 3 expected"
                root = struct.unpack("<Q", data[3:11])[0]
                rank = data[2]
                break
            if mtype == 0x10:  # continuation
                caddr, clen = struct.unpack("<QQ", data[:16])
                blocks.append((_range(sess, url, caddr, clen), 0, clen))
            p += 8 + msize
    assert root is not None
    key_size = 8 + 8 * rank
    out = {}

    def read_node(a):
        head = _range(sess, url, a, 24)
        assert head[:4] == b"TREE" and head[4] == 1
        level, used = head[5], struct.unpack("<H", head[6:8])[0]
        body = _range(sess, url, a + 24, used * (key_size + 8) + key_size)
        items = []
        for i in range(used):
            k = body[i * (key_size + 8): i * (key_size + 8) + key_size]
            size = struct.unpack("<I", k[:4])[0]
            offs = struct.unpack("<" + "Q" * rank, k[8:8 + 8 * rank])
            child = struct.unpack("<Q", body[i * (key_size + 8) + key_size: (i + 1) * (key_size + 8)])[0]
            items.append((offs, size, child))
        return level, items
    level_nodes = [root]
    with ThreadPoolExecutor(n_threads) as ex:
        while level_nodes:
            nxt = []
            for level, items in ex.map(read_node, level_nodes):
                for offs, size, child in items:
                    if level == 0:
                        out[(offs[0], offs[1])] = (child, size)
                    else:
                        nxt.append(child)
            level_nodes = nxt
    return out


def session_spectral(asset_id, event_times, good, weights, n_threads=6, batch_chunks=6,
                     wrist_names=("L_Wrist", "R_Wrist")):
    """Spectral measures, segment checks and wrist windows for the events of one file.

    good: bool (n_ch,) good electrodes of this session. weights: (n_ch, n_roi) projection
    weights with bad electrodes already 0 and columns summing to 1.
    Returns a dict of arrays, one row per event.
    """
    f, url = open_nwb(asset_id)
    ds = f["acquisition/ElectricalSeries/data"]
    n_t, n_ch = ds.shape
    CH = ds.chunks[0]
    assert ds.chunks[1] == 1
    bank = morlet_bank()
    half = (bank.shape[0] - 1) // 2
    n_ev = len(event_times)
    s0 = np.round(np.asarray(event_times) * FS).astype(int)  # event sample (series starts at 0 s)
    seg_lo, seg_hi = s0 - int(SEG_HALF * FS), s0 + int(SEG_HALF * FS)
    inside = (seg_lo >= 0) & (seg_hi <= n_t)
    nb, nf, nr = len(BIN_T), len(FREQS), weights.shape[1]
    region = np.full((n_ev, nr, nf, nb), np.nan, np.float32)
    elec = {k: np.full((n_ev, n_ch), np.nan, np.float32) for k in
            ["lfb_mean", "hfb_mean", "lfb_median", "hfb_median", "lfb_mean_raw", "hfb_mean_raw",
             "lfb_mean_shift", "hfb_mean_shift"]}
    seg_db = np.full(n_ev, np.nan)
    hf_db = np.full(n_ev, np.nan)
    allzero = np.zeros(n_ev, bool)
    # chunks needed
    need = {}
    for i in np.flatnonzero(inside):
        for c in range(seg_lo[i] // CH, (seg_hi[i] - 1) // CH + 1):
            need.setdefault(c, []).append(i)
    tchunks = sorted(need)
    sess = requests.Session()
    sess.mount("https://", requests.adapters.HTTPAdapter(pool_connections=n_threads, pool_maxsize=n_threads))
    raw_bytes = CH * 4
    index = chunk_index(ds, url, sess)
    assert len(index) == -(-n_t // CH) * n_ch, "chunk index incomplete"

    def fetch(c):
        """All channels of time chunk c, read in one range request: the file stores the chunks
        of one time block one after another (with B-tree nodes between some of them)."""
        locs = [index[(c * CH, ch)] for ch in range(n_ch)]
        lo = min(a for a, _ in locs)
        hi = max(a + n for a, n in locs)
        buf = _range(sess, url, lo, hi - lo)
        cols = []
        for a, n in locs:
            out = zlib.decompress(buf[a - lo:a - lo + n])
            if len(out) != raw_bytes:
                raise ValueError(f"chunk {c}: decoded {len(out)} bytes")
            cols.append(np.frombuffer(out, dtype="<f4"))
        return c, np.stack(cols, axis=1)
    cache = {}
    done = np.zeros(n_ev, bool)
    bins_off = np.round(BIN_T * FS).astype(int)
    with ThreadPoolExecutor(n_threads) as ex:
        for b0 in range(0, len(tchunks), batch_chunks):
            batch = tchunks[b0:b0 + batch_chunks]
            args = [c for c in batch if c not in cache]
            for c, arr in ex.map(fetch, args):
                cache[c] = arr
            # events whose chunks are all present
            ready = [i for c in batch for i in need[c] if not done[i]
                     and all(cc in cache for cc in range(seg_lo[i] // CH, (seg_hi[i] - 1) // CH + 1))]
            for i in sorted(set(ready)):
                cs = range(seg_lo[i] // CH, (seg_hi[i] - 1) // CH + 1)
                block = np.concatenate([cache[c] for c in cs], axis=0)
                start = cs[0] * CH
                seg = block[seg_lo[i] - start: seg_hi[i] - start].T.astype(np.float64)  # (n_ch, 5000), uV
                done[i] = True
                allzero[i] = bool(np.all(seg[good] == 0, axis=0).any())
                fr, p = _segment_psd(seg[good])
                pm = p.mean(axis=0)
                seg_db[i] = 10 * np.log10(pm[(fr >= 1) & (fr <= 200)].mean())
                hf_db[i] = 10 * np.log10(pm[(fr >= 115) & (fr <= 125)].mean())
                centre = int(SEG_HALF * FS)
                taps = np.arange(-half, half + 1)[None, :]
                idx = centre + bins_off[:, None] + taps  # (nb, taps)
                # convolution: flip the kernel
                pw = np.abs(seg[:, idx] @ bank[::-1, :]) ** 2  # (n_ch, nb, nf)
                # control: the same measure around a pseudo-onset SHIFT_S before the event
                pws = np.abs(seg[:, idx + int(SHIFT_S * FS)] @ bank[::-1, :]) ** 2
                with np.errstate(divide="ignore"):
                    db = 10 * np.log10(pw).transpose(0, 2, 1)  # (n_ch, nf, nb)
                    dbs = 10 * np.log10(pws).transpose(0, 2, 1)
                sh = band_stats(dbs - dbs[:, :, BASE].mean(axis=-1, keepdims=True))
                elec["lfb_mean_shift"][i] = sh["lfb_mean"]
                elec["hfb_mean_shift"][i] = sh["hfb_mean"]
                bs = db - db[:, :, BASE].mean(axis=-1, keepdims=True)
                st = band_stats(bs)
                for k, v in st.items():
                    elec[k][i] = v
                raw = band_stats(db)
                elec["lfb_mean_raw"][i] = raw["lfb_mean"]
                elec["hfb_mean_raw"][i] = raw["hfb_mean"]
                dbg = np.where(np.isfinite(db), db, 0.0)
                region[i] = np.einsum("cr,cfb->rfb", weights, dbg)
            # keep only chunks needed later
            keep = {batch[-1]}
            for c in list(cache):
                if c not in keep:
                    del cache[c]
    # wrist windows, -1.5 to +1.5 s at 30 Hz
    pos = f["processing/behavior/Position"]
    prate = float(pos["R_Wrist/starting_time"].attrs["rate"])
    p0 = float(pos["R_Wrist/starting_time"][()])
    n_p = pos["R_Wrist/data"].shape[0]
    k = np.arange(-45, 46)
    wrist = {w: np.full((n_ev, len(k), 2), np.nan) for w in wrist_names}
    for w in wrist_names:
        d = pos[f"{w}/data"]
        for i, t in enumerate(event_times):
            c = int(round((t - p0) * prate))
            if c - 45 >= 0 and c + 46 <= n_p:
                wrist[w][i] = d[c - 45:c + 46, :]
    f.close()
    return dict(region=region, elec=elec, seg_db=seg_db, hf_db=hf_db, inside=inside, allzero=allzero,
                wrist=wrist, wrist_t=k / prate)


# ----------------------------------------------------------------------------- regression

def design_matrix(ev, log_speed=False):
    """Features as the Methods (and code) encode them. Returns (X, column feature names)."""
    cols, names = [], []
    for d in sorted(ev.day.unique()):
        cols.append((ev.day == d).astype(float).values)
        names.append("day")
    tod = np.digitize(ev.time_of_day.values, [8, 16])
    for b in range(3):
        cols.append((tod == b).astype(float))
        names.append("time_of_day")
    cont = {
        "duration": np.log(ev.duration.values),
        "magnitude": np.log(ev.magnitude.values + 1),
        "angle": ev.angle.values,
        "onset_speed": np.log(ev.onset_speed.values + 1) if log_speed else ev.onset_speed.values,
        "speech_ratio": ev.speech_ratio.values,
        "bimanual_ratio": ev.bimanual_ratio.values,
        "bimanual_overlap": ev.bimanual_overlap.values,
        "bimanual_class": ev.bimanual_class.values,
    }
    for k, v in cont.items():
        sd = v.std()
        cols.append((v - v.mean()) / sd if sd > 0 else v * 0)
        names.append(k)
    return np.column_stack(cols), np.array(names)


def forward_select(X, y):
    """Forward selection over single columns by OLS adjusted R2, starting from 0 and adding the
    best column while the score improves (code regression_utils._forward_selected_new, which
    selects among the columns of the design, one-hot day and time-of-day columns one by one).
    Runs on all of the subject's events, as the code does. Returns a boolean mask of columns."""
    n, p = X.shape
    chosen = np.zeros(p, bool)
    current = 0.0
    yc = y - y.mean()
    sst = yc @ yc
    while not chosen.all():
        best, best_j = -np.inf, None
        for j in np.flatnonzero(~chosen):
            sel = chosen.copy()
            sel[j] = True
            A = np.column_stack([np.ones(n), X[:, sel]])
            beta, *_ = np.linalg.lstsq(A, y, rcond=None)
            res = y - A @ beta
            k = sel.sum()
            adj = 1 - (res @ res / sst) * (n - 1) / (n - k - 1)
            if adj > best:
                best, best_j = adj, j
        if best > current:
            chosen[best_j] = True
            current = best
        else:
            break
    return chosen


def day_balanced_splits(days, n_splits, test_frac, rng):
    """Random splits with equal numbers of test events from each day (code train_test_split_day_balance)."""
    uniq = np.unique(days)
    per_day = min((days == d).sum() for d in uniq)
    n_test_total = int(round(test_frac * len(days)))
    k = max(1, min(per_day, n_test_total // len(uniq)))
    out = []
    for _ in range(n_splits):
        test = np.concatenate([rng.choice(np.flatnonzero(days == d), k, replace=False) for d in uniq])
        mask = np.zeros(len(days), bool)
        mask[test] = True
        out.append(mask)
    return out


def r2(y, p):
    return 1 - ((y - p) ** 2).sum() / ((y - y.mean()) ** 2).sum()


def fit_models(X, names, y, splits, chosen, delta=False, shuffle_rng=None, code_shuffle=False):
    """Huber models (sklearn HuberRegressor defaults, code) on the chosen columns over the
    splits. Returns the mean test R2, the mean coefficients (0 for columns not chosen) and,
    when delta is True, the mean Delta R2 per feature: the model refit with the feature's
    columns shuffled in the training events and scored on the unshuffled test events
    (Methods); with code_shuffle the test events are shuffled too and scored shuffled (code).
    A feature with no chosen column gets Delta R2 0 (code: its columns are zero)."""
    from sklearn.linear_model import HuberRegressor
    import warnings
    from sklearn.exceptions import ConvergenceWarning
    feats = list(dict.fromkeys(names))
    Xs = X[:, chosen]
    nonconv = [0]

    def fit(A, b):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always", ConvergenceWarning)
            m = HuberRegressor().fit(A, b)
        nonconv[0] += sum(issubclass(x.category, ConvergenceWarning) for x in w)
        return m
    nsel = names[chosen]
    r2s, coefs = [], []
    dr2 = {f: [] for f in feats}
    for test in splits:
        tr = ~test
        if chosen.sum() == 0:
            pred = np.full(test.sum(), np.mean(y[tr]))
            r2s.append(r2(y[test], pred))
            coefs.append(np.zeros(X.shape[1]))
            if delta:
                for f in feats:
                    dr2[f].append(0.0)
            continue
        m = fit(Xs[tr], y[tr])
        full = r2(y[test], m.predict(Xs[test]))
        r2s.append(full)
        c = np.zeros(X.shape[1])
        c[chosen] = m.coef_
        coefs.append(c)
        if delta:
            for f in feats:
                cols = nsel == f
                if not cols.any():
                    dr2[f].append(0.0)
                    continue
                Xtr = Xs[tr].copy()
                perm = shuffle_rng.permutation(tr.sum())
                Xtr[:, cols] = Xtr[perm][:, cols]
                Xte = Xs[test].copy()
                if code_shuffle:
                    pt = shuffle_rng.permutation(test.sum())
                    Xte[:, cols] = Xte[pt][:, cols]
                ms = fit(Xtr, y[tr])
                dr2[f].append(full - r2(y[test], ms.predict(Xte)))
    out = dict(r2=float(np.mean(r2s)), coef=np.mean(coefs, axis=0), fits=len(splits) * (1 + (len(feats) if delta else 0)),
               nonconverged=nonconv[0])
    if delta:
        out["delta"] = {f: float(np.mean(v)) for f, v in dr2.items()}
    return out


def retention(chosen, names):
    """Per feature, 1 when kept by forward selection; a day or time-of-day column counts as
    1 / number of its columns (code feat_select_prob)."""
    out = {}
    for f in dict.fromkeys(names):
        cols = names == f
        out[f] = float(chosen[cols].sum() / cols.sum())
    return out


def coef_summary(coef, names):
    """Coefficient per feature; for day and time of day the SD of their one-hot coefficients
    (Figure 6 legend; code np.std over those coefficients)."""
    out = {}
    for f in dict.fromkeys(names):
        c = coef[names == f]
        out[f] = float(np.std(c)) if f in ("day", "time_of_day") else float(c[0])
    return out


def regress_subject(args):
    """All models of one subject. args: dict with X, names, Y (n_ev, n_el, n_targets), days,
    seed, target names, which targets get Delta R2. Returns a list of per-model dicts."""
    import os
    os.environ["OMP_NUM_THREADS"] = "1"
    X, names, Y, days, seed = args["X"], args["names"], args["Y"], args["days"], args["seed"]
    rng = np.random.default_rng(seed)
    splits90 = day_balanced_splits(days, 200, 0.1, rng)
    splits80 = day_balanced_splits(days, 200, 0.2, np.random.default_rng(seed + 1))
    shuf = np.random.default_rng(seed + 2)
    out = []
    for k in range(Y.shape[1]):
        r2_lfb = -np.inf
        for t, tname in enumerate(args["targets"]):
            y = Y[:, k, t]
            chosen = forward_select(X, y)
            row = dict(subject=args["subject"], electrode=args["electrodes"][k], target=tname,
                       retention=retention(chosen, names))
            if tname in args["main_targets"]:
                main = fit_models(X, names, y, splits90, chosen)
                row["r2"] = main["r2"]
                row["nonconverged"] = main["nonconverged"]
                row["coef"] = coef_summary(main["coef"], names)
                row["r2_80"] = fit_models(X, names, y, splits80, chosen)["r2"]
                if tname.startswith("lfb"):
                    r2_lfb = main["r2"]
                # Delta R2 where the band's own R2 passes, or the LFB R2 (the code's selection)
                if max(main["r2"], r2_lfb) > args["delta_min_r2"]:
                    row["delta"] = fit_models(X, names, y, splits90, chosen, delta=True, shuffle_rng=shuf)["delta"]
                    row["delta_code"] = fit_models(X, names, y, splits80, chosen, delta=True, shuffle_rng=shuf,
                                                   code_shuffle=True)["delta"]
            else:
                row["r2"] = fit_models(X, names, y, splits90, chosen)["r2"]
            out.append(row)
    return out


def run_regression(jobs, workers=4):
    from concurrent.futures import ProcessPoolExecutor
    import multiprocessing as mp
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("spawn")) as ex:
        return [r for rows in ex.map(regress_subject, jobs) for r in rows]


def _spectral_job(args):
    import os
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    asset_id, times, good, weights = args
    return session_spectral(asset_id, times, good, weights)


def run_spectral(jobs, workers=8):
    """jobs: list of (asset_id, event_times, good, weights). Runs files in parallel processes."""
    from concurrent.futures import ProcessPoolExecutor
    import multiprocessing as mp
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("spawn")) as ex:
        return list(ex.map(_spectral_job, jobs))


def match_projection(m, positions_known):
    """Rows of a projection matrix matched to the file's electrodes, by the paper's code
    (tfr_utils.load_project_spectral_power, commit 04c6faf): it keeps the rows that are not all
    zero and drops the first of them (`np.nonzero(df.transpose().mean().values != 0)[0][1:]`),
    and applies the rest, in order, to the channels of its power files. Here they are applied,
    in order, to the electrodes whose positions are known (electrodes without a position get
    no weight). Returns (array n_electrodes x regions or None, note)."""
    a = m.values.astype(float)
    keep = np.flatnonzero(a.mean(axis=1) != 0)[1:]
    rows = a[keep]
    n_known = int(positions_known.sum())
    if len(rows) != n_known:
        return None, f"{len(rows)} rows for {n_known} electrodes with positions"
    out = np.zeros((len(positions_known), a.shape[1]))
    out[positions_known] = rows
    return out, f"{len(rows)} rows for {n_known} electrodes with positions"


def session_weights(proj, good):
    """Weights of the eight regions: bad electrodes 0, each region renormalised to sum 1."""
    w = proj.copy()
    w[~good] = 0
    s = w.sum(axis=0)
    return w / np.where(s > 0, s, np.nan)
