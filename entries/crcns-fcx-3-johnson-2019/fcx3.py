"""Loading and measures for CRCNS data set fcx-3 (Johnson et al. 2019, Front. Syst. Neurosci. 12, 65,
doi:10.3389/fnsys.2018.00065).

The data set (doi:10.6080/K06971S9) holds, per subject, a tar.gz with the filtered continuous iEEG
(data_primary.mat), the channel names (elec_labels.mat), electrode positions (s<n>_MNI_grid.csv),
the preprocessed epochs (data_derived.mat, FieldTrip structures data_pre, data_encmain and
data_proc, MATLAB 7.3) and a trial table (summary_file_trial.csv). The tar files are streamed from
the public bucket and decompressed in memory, one subject at a time; nothing is written to disk.
A tar.gz cannot be read at random, so each subject's file is read once, start to end.

Where the parameters come from:

- Channels analysed, by region and hemisphere: docs/summary_channel_analysis.csv of the data set.
  The derived epochs carry more channels; only the listed ones are kept.
- Analysis windows, in the time axis of the derived epochs: processing [0.3, 1.2] s of data_proc,
  maintenance [0.6, 1.5] s of data_encmain, baseline [0.65, 0.85] s of data_pre. These are the
  latencies of the paper's deposited scripts (power_compute.m, erp_compute.m, psi_compute.m); the
  notebook checks them against the trial table and the continuous data.
- Power: Hanning-tapered windows of 3 cycles (3/f s), 2 to 40 Hz in 1-Hz steps, 10-ms steps
  (Methods, Spectral Decomposition; power_compute.m). The derived epochs run from -1.5 to 3.0 s,
  so every window of the analysis windows lies inside recorded data and no zero padding enters a
  window. The baseline z-score of zbaseline.m (mean and SD of the means of r baseline points drawn
  without replacement, r the number of correct trials) is computed in closed form, as the limit of
  the code's 1000 draws (a standard choice, which cannot change a result: the z-score is the same
  affine map for every trial at a channel and frequency, so the condition t-tests do not change).
- ERP: 30-Hz low-pass FIR, zero padded to 7.5 s, baseline the pretrial temporal mean over trials
  (Methods, Event-Related Potentials; erp_compute.m). The FIR order 3*fix(fs/30), applied forwards
  and backwards, is FieldTrip's default for a 'fir' low-pass, which the script uses (standard
  choice).
- Cluster test: independent-samples t per point, threshold two-tailed 0.05, cluster mass the sum
  of t, 1000 shuffles of the condition labels, connectivity across time and frequency within a
  channel and across neighbouring channels at the same time and frequency (Methods, ERPs,
  paragraph 2, and Spectral Decomposition, paragraph 3). Neighbours are not stated; the readings
  are in `neighbours`.
- PSI: ERP subtracted (mean over all correct trials for the task-induced PSI, per condition for the
  time-resolved PSI: psi_compute.m and subtracterp.m), one Hanning-tapered FFT of each 900-ms
  segment padded to 7.5 s read at the bins nearest to the integer frequencies (task-induced,
  psi_compute.m 'mtmfft'), or the 3-cycle windows at 10-ms steps (time-resolved, 'mtmconvol').
  Bands 2 to 7 and 9 to 24 Hz (Methods, Task-Induced PSI). The surrogate null follows
  psianalysis.m: the trial-mean normalised cross-spectrum with its frequencies shuffled, the slope
  summed over all bins, 1000 shuffles, one shuffle for all pairs; z per pair is the mean over the
  band's bins of the z against each bin's null (time-resolved: one null of 1000 shuffles per time
  point, a standard choice that changes only the Monte Carlo noise of the null).
"""

from __future__ import annotations

import io
import re
import tarfile

import fsspec
import h5py
import numpy as np
import pandas as pd
from scipy import ndimage, signal, stats
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components

DATASET = "crcns:fcx-3/unversioned"  # CRCNS data sets are not versioned (docs/archives.md)
BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-3/live"
SUBJECTS = [f"s{i}" for i in range(1, 8)]
BLOCK = 2**24

PROC_WIN = (0.3, 1.2)
MAIN_WIN = (0.6, 1.5)
BASE_WIN = (0.65, 0.85)
FOI = np.arange(2, 41)
TOI_STEP = 0.01
BANDS = {"delta-theta": (2, 7), "alpha-beta": (9, 24)}
PAD_S = 7.5
N_PERM = 1000


# --------------------------------------------------------------------------- archive files

def read_bytes(path):
    with fsspec.open(f"{BUCKET}/{path}", block_size=BLOCK) as f:
        return f.read()


def checksums():
    out = {}
    for line in read_bytes("checksums.md5").decode().splitlines():
        if line.strip():
            md5, name = line.split()
            out[name] = md5
    return out


def bucket_listing():
    """Keys and sizes of the data set's files, from the bucket's listing."""
    import urllib.request
    url = "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=fcx-3/"
    x = urllib.request.urlopen(url).read().decode()
    rows = re.findall(r"<Key>(.*?)</Key><LastModified>(.*?)</LastModified><ETag>(.*?)</ETag>.*?<Size>(\d+)</Size>", x)
    return pd.DataFrame([(k, int(s), lm, e.replace("&quot;", "")) for k, lm, e, s in rows],
                        columns=["key", "size", "modified", "etag"])


def summary_file():
    """docs/summary_file.csv: per subject age, sex, accuracy and mean correct RT per condition."""
    cols = ["subject", "age", "sex", "acc_identity", "acc_spatial", "acc_temporal",
            "rt_identity", "rt_spatial", "rt_temporal"]
    return pd.read_csv(io.BytesIO(read_bytes("docs/summary_file.csv")), header=None, names=cols)


def channel_table():
    """docs/summary_channel_analysis.csv as one row per analysed channel."""
    rows = []
    text = read_bytes("docs/summary_channel_analysis.csv").decode()
    cols = [("PFC", "L"), ("PFC", "R"), ("parietal", "L"), ("parietal", "R")]
    subj = None
    for line in text.splitlines()[2:]:
        parts = line.split(",")
        if parts[0].strip():
            subj = parts[0].strip().lower()
        for (region, hemi), lab in zip(cols, parts[1:5]):
            if lab.strip():
                rows.append((subj, lab.strip(), region, hemi))
    return pd.DataFrame(rows, columns=["subject", "label", "region", "hemisphere"])


# --------------------------------------------------------------------------- MATLAB 7.3 helpers

def _cellstr(h, ds):
    return ["".join(map(chr, h[r][()].ravel())) for r in ds[()].ravel()]


def parse_grid(text):
    """Electrode positions of an s<n>_MNI_grid.csv (vtkpx multi-grid): {grid name: (dims, spacing, positions)}."""
    lines = text.splitlines()
    grids, name = {}, None
    for i, line in enumerate(lines):
        if line.startswith("#vtkpxElectrodeGridSource"):
            name = None
        elif line.startswith("#Description") and i + 1 < len(lines) and lines[i - 1].startswith("#vtkpxElectrodeGridSource"):
            name = lines[i + 1].strip()
            grids[name] = {"dims": None, "spacing": None, "pos": []}
        elif name and line.startswith("#Dimensions"):
            grids[name]["dims"] = tuple(int(v) for v in lines[i + 1].split())
        elif name and line.startswith("#Electrode Spacing"):
            grids[name]["spacing"] = float(lines[i + 1].split()[0])
        elif name and line.startswith("#Position"):
            grids[name]["pos"].append([float(v) for v in lines[i + 1].split()])
    for g in grids.values():
        g["pos"] = np.array(g["pos"])
    return grids


def split_label(lab):
    m = re.match(r"^(.*?)_?(\d+)$", lab)
    return m.group(1), int(m.group(2))


# --------------------------------------------------------------------------- streaming one subject

def stream_subject(sid, analysed, check_channels=2, check_trials=8, rng=None):
    """Stream one subject's tar.gz and return its trial table, the derived epochs of the analysed
    channels, and a check of the derived epochs against the continuous data.

    analysed: list of the subject's analysed channel labels, in the order to keep.
    """
    rng = rng or np.random.default_rng(0)
    out = {"subject": sid, "members": []}
    primary = None
    with fsspec.open(f"{BUCKET}/data/{sid}.tar.gz", block_size=BLOCK) as f:
        with tarfile.open(fileobj=f, mode="r|gz") as tf:
            for m in tf:
                if not m.isfile():
                    continue
                name = m.name.split("/")[-1]
                out["members"].append((name, m.size))
                b = tf.extractfile(m).read()
                if name == "data_primary.mat":
                    with h5py.File(io.BytesIO(b), "r") as h:
                        ds = h["gdat_clean_filt"]
                        out["primary_keys"] = [k for k in h.keys() if not k.startswith("#")]
                        out["primary_shape"] = ds.shape
                        primary = ds.astype("float32")[()]
                elif name == "elec_labels.mat":
                    out["elec_labels_format"] = b[:19].decode()
                    if b.startswith(b"MATLAB 7.3"):
                        with h5py.File(io.BytesIO(b), "r") as h:
                            out["elec_labels"] = _cellstr(h, h["elec_labels"])
                    else:  # s3 stores this file as a MATLAB 5 file
                        from scipy.io import loadmat
                        out["elec_labels"] = [str(v) for v in loadmat(io.BytesIO(b), squeeze_me=True)["elec_labels"]]
                elif name.endswith("_MNI_grid.csv"):
                    out["grid"] = parse_grid(b.decode(errors="replace"))
                elif name == "data_derived.mat":
                    out.update(_read_derived(b, analysed))
                elif name == "summary_file_trial.csv":
                    out["trials"] = pd.read_csv(io.BytesIO(b), header=None, names=[
                        "trial", "correct", "type", "condition", "jitter", "rt",
                        "pre_start", "encmain_start", "proc_start"])
                del b
    if primary is not None:
        if primary.shape[0] != len(out["elec_labels"]):
            primary = primary.T
        out["clock"] = _clock_check(out, primary, analysed, check_channels, check_trials, rng)
        out["primary_samples"] = primary.shape[1]
        del primary
    return out


def _read_derived(b, analysed):
    res = {}
    with h5py.File(io.BytesIO(b), "r") as h:
        for key in ["data_pre", "data_encmain", "data_proc"]:
            g = h[key]
            labels = _cellstr(h, g["label"])
            idx = [labels.index(lab) for lab in analysed]
            refs = g["trial"][()].ravel()
            trefs = g["time"][()].ravel()
            times = [h[r][()].ravel() for r in trefs]
            fs = float(g["fsample"][()].ravel()[0])
            # trials can differ by a sample or so in length: keep the samples common to all
            t0 = max(t[0] for t in times)
            t1 = min(t[-1] for t in times)
            lens = sorted({len(t) for t in times})
            x = np.stack([h[r][()][:, idx].T[:, (t >= t0 - 0.5 / fs) & (t <= t1 + 0.5 / fs)]
                          for r, t in zip(refs, times)]).astype("float32")  # trials x ch x time
            tm = times[0][(times[0] >= t0 - 0.5 / fs) & (times[0] <= t1 + 0.5 / fs)]
            res[key] = {"x": x, "time": tm, "lengths": lens, "starts": sorted({round(t[0], 6) for t in times}),
                        "time_all_equal": len(lens) == 1,
                        "trialinfo": g["trialinfo"][()].T, "labels_all": labels,
                        "fs": float(g["fsample"][()].ravel()[0]),
                        "hdr_nSamples": float(g["hdr"]["nSamples"][()].ravel()[0])}
    res["fs"] = res["data_proc"]["fs"]
    return res


def _best_lag(sig, y):
    sig = sig - sig.mean()
    yy = y - y.mean()
    num = signal.fftconvolve(sig, yy[::-1], mode="valid")
    c2 = np.cumsum(np.r_[0, sig.astype(float) ** 2])
    n = len(y)
    den = np.sqrt(c2[n:] - c2[:-n]) * np.linalg.norm(yy)
    r = num / np.where(den > 0, den, np.inf)
    k = int(np.argmax(r))
    return float(r[k]), k


def _clock_check(sub, primary, analysed, n_ch, n_tr, rng):
    """Where the derived epochs lie in the continuous data.

    1. For n_ch analysed channels and the first trial of each epoch, the derived trace is searched
       for within 4 s of the trial table's start column, against the difference of the channel's
       contact with every other contact; this gives the offset of each epoch from its column.
    2. At that offset, every analysed channel is matched, on n_tr random trials, against the
       difference with every other contact: the best one is the channel's bipolar reference, and
       its correlation shows whether the derived trace is that difference.
    """
    fs = sub["fs"]
    labs = sub["elec_labels"]
    cols = {"data_pre": "pre_start", "data_encmain": "encmain_start", "data_proc": "proc_start"}
    tt = sub["trials"]
    found = []
    offsets = {}
    for key, col in cols.items():
        ep = sub[key]
        for c in list(rng.choice(len(analysed), size=min(n_ch, len(analysed)), replace=False)):
            i = labs.index(analysed[c])
            y = ep["x"][0, c].astype(float)
            start = int(tt[col].iloc[0])
            lo = max(0, start - int(4 * fs))
            hi = min(primary.shape[1], start + int(4 * fs) + len(y))
            best = None
            for j in range(len(labs)):
                sig = primary[i, lo:hi] - (primary[j, lo:hi] if j != i else 0)
                r, k = _best_lag(sig, y)
                if best is None or r > best[0]:
                    best = (r, labs[j], lo + k)
            found.append({"epoch": key, "channel": analysed[c], "trial": int(tt["trial"].iloc[0]),
                          "r": best[0], "reference": best[1], "offset_s": (best[2] - start) / fs})
        offsets[key] = int(round(np.median([f["offset_s"] for f in found if f["epoch"] == key]) * fs))
    rows = []
    trials = rng.choice(len(tt), size=min(n_tr, len(tt)), replace=False)
    for c, lab in enumerate(analysed):
        i = labs.index(lab)
        rs = np.zeros(len(labs))
        n_ok = 0
        for key, col in cols.items():
            ep = sub[key]
            for t in trials:
                start = int(tt[col].iloc[t]) + offsets[key]
                y = ep["x"][t, c].astype(float)
                seg = primary[:, start:start + len(y)].astype(float)
                if seg.shape[1] != len(y):
                    continue
                d = seg[i][None, :] - seg
                d[i] = seg[i]
                d = d - d.mean(1, keepdims=True)
                yy = y - y.mean()
                rs += d @ yy / (np.linalg.norm(d, axis=1) * np.linalg.norm(yy) + 1e-12)
                n_ok += 1
        rs /= max(n_ok, 1)
        j = int(np.argmax(rs))
        rows.append({"channel": lab, "reference": labs[j], "r": float(rs[j]), "n_traces": n_ok})
    return {"search": pd.DataFrame(found), "offsets_s": {k: v / fs for k, v in offsets.items()},
            "channels": pd.DataFrame(rows)}


# --------------------------------------------------------------------------- neighbours

def neighbours(labels, grid=None, reading="adjacent", references=None):
    """Pairs of neighbouring channels (indices into labels), under the readings of the claims file
    (header S2): 'adjacent', contacts with consecutive numbers on the same lead or strip (an
    assumption: the paper says only "neighboring electrodes"); 'distance', bipolar midpoints within
    1.5 times the lead's stated contact spacing in the s<n>_MNI_grid.csv positions (an assumption);
    'none', no spatial clustering."""
    pairs = []
    if reading == "none":
        return np.zeros((0, 2), int)
    parsed = [split_label(lab) for lab in labels]
    if reading == "adjacent":
        for i in range(len(labels)):
            for j in range(i + 1, len(labels)):
                if parsed[i][0] == parsed[j][0] and abs(parsed[i][1] - parsed[j][1]) == 1:
                    pairs.append((i, j))
        return np.array(pairs, int).reshape(-1, 2)
    pos, spacing = bipolar_positions(labels, grid, references)
    for i in range(len(labels)):
        for j in range(i + 1, len(labels)):
            if np.isfinite(pos[i]).all() and np.isfinite(pos[j]).all():
                lim = 1.5 * max(spacing[i], spacing[j])
                if np.linalg.norm(pos[i] - pos[j]) <= lim:
                    pairs.append((i, j))
    return np.array(pairs, int).reshape(-1, 2)


GRID_ALIAS = {"RH": "HD_Grid"}  # s3: contacts RH1..RH256 are the 256-contact grid 'HD_Grid' of its MNI file


def bipolar_positions(labels, grid, references=None):
    """Midpoint of a bipolar channel's two contacts (the channel's contact and the reference contact
    the clock check finds in the continuous data), taking contact n as the n-th electrode of the grid
    with the label's prefix in the MNI file (an assumption: the files do not say how grid contacts are
    numbered)."""
    pos = np.full((len(labels), 3), np.nan)
    spacing = np.full(len(labels), np.nan)

    def contact(lab):
        pre, num = split_label(lab)
        g = grid.get(pre, grid.get(GRID_ALIAS.get(pre, ""))) if grid else None
        if g is None or not 1 <= num <= len(g["pos"]):
            return None, None
        return g["pos"][num - 1], g["spacing"]

    for i, lab in enumerate(labels):
        p1, sp = contact(lab)
        ref = references[i] if references is not None else None
        p2, _ = contact(ref) if ref else (None, None)
        if p1 is None or p2 is None:
            continue
        pos[i] = (p1 + p2) / 2
        spacing[i] = sp
    return pos, spacing


# --------------------------------------------------------------------------- spectral measures

def hanning_ft(n):
    """MATLAB hanning(n), as FieldTrip uses: 0.5*(1-cos(2*pi*k/(n+1))), k = 1..n."""
    k = np.arange(1, n + 1)
    return 0.5 * (1 - np.cos(2 * np.pi * k / (n + 1)))


def win_index(time, win):
    return np.where((time >= win[0] - 1e-9) & (time <= win[1] + 1e-9))[0]


def toi_index(time, win, step=TOI_STEP):
    toi = np.arange(win[0], win[1] + step / 2, step)
    return np.array([int(np.argmin(np.abs(time - t))) for t in toi]), toi


def tfr_fourier(x, time, fs, foi, toi_idx):
    """Complex 3-cycle Hanning spectra (mtmconvol) at the samples toi_idx: trials x ch x f x t."""
    n_tr, n_ch, n_t = x.shape
    nfft = int(2 ** np.ceil(np.log2(n_t + int(3 / foi.min() * fs) + 1)))
    X = np.fft.fft(x.reshape(-1, n_t).astype("float64"), n=nfft, axis=1)
    out = np.empty((n_tr * n_ch, len(foi), len(toi_idx)), np.complex64)
    for fi, f in enumerate(foi):
        n = int(round(3 / f * fs))
        tap = hanning_ft(n)
        tk = (np.arange(n) - (n - 1) / 2) / fs
        kern = tap * np.exp(-2j * np.pi * f * tk)
        # correlation with the window centred at each sample
        K = np.fft.fft(kern[::-1], n=nfft)
        y = np.fft.ifft(X * K[None, :], axis=1)
        shift = (n - 1) // 2
        out[:, fi, :] = y[:, toi_idx - shift + n - 1]
    return out.reshape(n_tr, n_ch, len(foi), len(toi_idx))


def fft_segment(x, time, fs, win, foi, pad=PAD_S):
    """Hanning-tapered FFT of one window, zero padded to pad s, at the bins nearest to foi
    (FieldTrip mtmfft): trials x ch x f."""
    idx = win_index(time, win)
    seg = x[:, :, idx].astype("float64")
    seg = seg * hanning_ft(len(idx))[None, None, :]
    nfft = int(round(pad * fs))
    F = np.fft.rfft(seg, n=nfft, axis=2)
    freqs = np.fft.rfftfreq(nfft, 1 / fs)
    bins = [int(np.floor(f * pad + 0.5)) for f in foi]
    return F[:, :, bins], freqs[bins]


def lowpass_fir(x, fs, fc=30.0, pad=PAD_S):
    """FieldTrip-style FIR low-pass: order 3*fix(fs/fc), applied forwards and backwards, on the epoch
    zero padded to pad s."""
    order = 3 * int(fs // fc)
    b = signal.firwin(order + 1, fc / (fs / 2))
    n = x.shape[-1]
    tot = int(round(pad * fs))
    left = max(0, (tot - n) // 2)
    xp = np.zeros(x.shape[:-1] + (n + 2 * left,))
    xp[..., left:left + n] = x
    y = signal.filtfilt(b, [1.0], xp, axis=-1, padtype=None)
    return y[..., left:left + n]


# --------------------------------------------------------------------------- cluster test

def _tstat(Xc, Xc2, g, n1, n2, S, Q):
    S1 = g @ Xc
    Q1 = g @ Xc2
    S2 = S - S1
    Q2 = Q - Q1
    m1, m2 = S1 / n1, S2 / n2
    v1 = (Q1 - n1 * m1 ** 2) / (n1 - 1)
    v2 = (Q2 - n2 * m2 ** 2) / (n2 - 1)
    sp = ((n1 - 1) * v1 + (n2 - 1) * v2) / (n1 + n2 - 2)
    with np.errstate(invalid="ignore", divide="ignore"):
        return (m1 - m2) / np.sqrt(sp * (1 / n1 + 1 / n2))


_STRUCT = np.zeros((3, 3, 3), bool)
_STRUCT[1] = ndimage.generate_binary_structure(2, 1)


def _clusters(t, thr, sign, nb):
    """Clusters of t*sign > thr in a ch x f x time array; returns (label array, masses)."""
    mask = (sign * t) > thr
    lab, n = ndimage.label(mask, structure=_STRUCT)
    if n == 0:
        return lab, np.zeros(0)
    if len(nb):
        a = lab[nb[:, 0]].ravel()
        b = lab[nb[:, 1]].ravel()
        keep = (a > 0) & (b > 0)
        if keep.any():
            g = coo_matrix((np.ones(keep.sum()), (a[keep], b[keep])), shape=(n + 1, n + 1))
            k, comp = connected_components(g, directed=False)
            remap = np.arange(k)
            remap[comp[0]], remap[0] = 0, comp[0]
            lab = remap[comp][lab]
            n = k - 1
    mass = np.bincount(lab.ravel(), weights=t.ravel(), minlength=n + 1)[1:]
    return lab, mass


def cluster_test(X, groups, nb_readings, rng, n_perm=N_PERM, alpha=0.05):
    """Per-subject cluster-based permutation test of two groups of trials.

    X: trials x ch x f x time (f may be 1). groups: bool array, True for the first condition.
    nb_readings: {name: neighbour pairs}. Positive t means first condition > second.
    Returns {reading: {'pos': [(mass, p, mask)], 'neg': [...]}} and the observed t.
    """
    n_tr = X.shape[0]
    shape = X.shape[1:]
    Xf = X.reshape(n_tr, -1).astype("float32")
    Xf = Xf - Xf.mean(0, keepdims=True)
    Xc2 = Xf ** 2
    S, Q = Xf.sum(0), Xc2.sum(0)
    g = groups.astype("float32")
    n1, n2 = groups.sum(), (~groups).sum()
    df = n1 + n2 - 2
    thr = stats.t.ppf(1 - alpha / 2, df)
    t_obs = _tstat(Xf, Xc2, g, n1, n2, S, Q).reshape(shape)
    obs = {k: {s: _clusters(t_obs, thr, sg, nb) for s, sg in (("pos", 1), ("neg", -1))}
           for k, nb in nb_readings.items()}
    null = {k: {"pos": np.zeros(n_perm), "neg": np.zeros(n_perm)} for k in nb_readings}
    for p in range(n_perm):
        gp = rng.permutation(groups).astype("float32")
        tp = _tstat(Xf, Xc2, gp, n1, n2, S, Q).reshape(shape)
        for k, nb in nb_readings.items():
            _, mp = _clusters(tp, thr, 1, nb)
            _, mn = _clusters(tp, thr, -1, nb)
            null[k]["pos"][p] = mp.max() if len(mp) else 0.0
            null[k]["neg"][p] = mn.min() if len(mn) else 0.0
    res = {}
    for k in nb_readings:
        res[k] = {}
        for s in ("pos", "neg"):
            lab, mass = obs[k][s]
            cl = []
            for i, m in enumerate(mass):
                if s == "pos":
                    pv = np.mean(null[k]["pos"] >= m)
                else:
                    pv = np.mean(null[k]["neg"] <= m)
                cl.append((float(m), float(pv), lab == i + 1))
            cl.sort(key=lambda c: c[1])
            res[k][s] = cl
    return res, t_obs


# --------------------------------------------------------------------------- PSI

def pairs_same_hemisphere(chan):
    """PFC-parietal pairs within a hemisphere: list of (pfc index, parietal index) into chan rows."""
    out = []
    for i, a in chan.iterrows():
        if a.region != "PFC":
            continue
        for j, b in chan.iterrows():
            if b.region == "parietal" and b.hemisphere == a.hemisphere:
                out.append((i, j))
    return out


def _slope(c):
    """Sum over adjacent bins of Im(conj(c_f) c_{f+1}), over the last axis."""
    return np.imag(np.conj(c[..., :-1]) * c[..., 1:]).sum(-1)


def psi_measures(Fa, Fb, rng, n_perm=N_PERM, null_per_bin=True, deposited=False):
    """PSI z per pair, A = PFC (positive: PFC leads), B = parietal.

    Fa, Fb: trials x pairs x f (x time) complex spectra, ERP already removed.
    Returns {'a': z, 'b': z} for the readings of the claims file (header P1): (a) PSI from the
    trial-averaged coherency (Nolte et al. 2008); (b) PSI per trial from the per-trial normalised
    cross-spectrum, averaged over trials (psianalysis.m, with the conjugate the Methods' cross-
    spectral density implies). The null shuffles the bins of the trial-mean normalised spectrum
    (psianalysis.m): coherency for (a), the mean per-trial phasor for (b). With deposited=True also
    'code': psianalysis.m as deposited, whose cross-spectrum lacks the conjugate, with PFC as its first
    channel, and 'code_rev' the same with parietal as its first channel, sign reversed so that
    positive still means PFC leads.
    """
    # move frequency to the last axis
    Fa = np.moveaxis(Fa, 2, -1)
    Fb = np.moveaxis(Fb, 2, -1)
    S_ab = (Fa * np.conj(Fb)).mean(0)
    S_aa = (np.abs(Fa) ** 2).mean(0)
    S_bb = (np.abs(Fb) ** 2).mean(0)
    C = S_ab / np.sqrt(S_aa * S_bb)
    ptr = Fa * np.conj(Fb)
    ptr = ptr / np.abs(ptr)
    pp = ptr.mean(0)
    obs = {"a": _slope(C), "b": _slope(ptr).mean(0)}
    ref = {"a": C, "b": pp}
    if deposited:
        for key, (X, Y) in {"code": (Fa, Fb), "code_rev": (Fb, Fa)}.items():
            cs = X * Y
            den = np.sqrt((X ** 2) * np.conj(Y ** 2))
            ptr_c = cs / den
            obs[key] = _slope(ptr_c).mean(0)
            ref[key] = ptr_c.mean(0)
    nf = Fa.shape[-1]
    n_sets = nf if null_per_bin else 1
    out = {}
    for k in obs:
        zs = []
        for _ in range(n_sets):
            s1 = np.zeros(obs[k].shape)
            s2 = np.zeros(obs[k].shape)
            for p in range(n_perm):
                p1 = rng.permutation(nf)
                p2 = rng.permutation(nf)
                v = np.imag(np.conj(ref[k][..., p1]) * ref[k][..., p2]).sum(-1)
                s1 += v
                s2 += v * v
            mean = s1 / n_perm
            sd = np.sqrt((s2 - n_perm * mean ** 2) / (n_perm - 1))
            zs.append((obs[k] - mean) / sd)
        out[k] = np.mean(zs, axis=0) * (-1 if k == "code_rev" else 1)
    return out


# --------------------------------------------------------------------------- group models

def paired_lme(y1, y2, subject):
    """Linear mixed model y ~ condition + (1|subject) + (1|pair) on two values per pair.

    With every pair holding both values, the REML estimate of the condition effect is the mean of
    the paired differences and its test the paired t-test over pairs (the subject and pair
    intercepts cancel in the differences); the F is reported with the residual degrees of freedom
    2n - 2, as MATLAB's fitlme does. The notebook checks this against statsmodels' MixedLM.
    Returns (effect y2 - y1, F, p, n pairs).
    """
    d = np.asarray(y2) - np.asarray(y1)
    n = len(d)
    t = d.mean() / (d.std(ddof=1) / np.sqrt(n))
    F = t ** 2
    p = stats.f.sf(F, 1, 2 * n - 2)
    return float(d.mean()), float(F), float(p), n


def mixedlm_check(y1, y2, subject, pair):
    """statsmodels MixedLM fit of y ~ condition with subject groups and a pair variance component."""
    import statsmodels.formula.api as smf
    df = pd.DataFrame({"y": np.r_[y1, y2], "cond": np.r_[np.zeros(len(y1)), np.ones(len(y2))],
                       "subject": np.r_[subject, subject], "pair": np.r_[pair, pair]})
    m = smf.mixedlm("y ~ cond", df, groups="subject", vc_formula={"pair": "0 + C(pair)"})
    r = m.fit(reml=True)
    t = r.tvalues["cond"]
    return float(r.params["cond"]), float(t ** 2), float(stats.f.sf(t ** 2, 1, len(df) - 2))


def fdr_bh(p, q=0.05):
    p = np.asarray(p)
    n = len(p)
    order = np.argsort(p)
    ranked = p[order] * n / np.arange(1, n + 1)
    crit = np.where(ranked <= q)[0]
    sig = np.zeros(n, bool)
    if len(crit):
        sig[order[:crit.max() + 1]] = True
    return sig


def runs(mask, times):
    """Runs of True in mask: list of (start, end) times."""
    out = []
    i = 0
    while i < len(mask):
        if mask[i]:
            j = i
            while j + 1 < len(mask) and mask[j + 1]:
                j += 1
            out.append((times[i], times[j]))
            i = j + 1
        else:
            i += 1
    return out


def logit_mixed(k, n, cond_codes, subject, n_quad=30):
    """Random-intercept logistic model fitted by maximum likelihood with Gauss-Hermite quadrature.

    k successes of n trials per row; fixed effects: intercept and the columns of cond_codes.
    Returns (beta, se, loglik).
    """
    from scipy.optimize import minimize
    X = np.column_stack([np.ones(len(k)), cond_codes])
    subs = pd.factorize(subject)[0]
    xs, ws = np.polynomial.hermite.hermgauss(n_quad)

    def nll(theta):
        beta, ls = theta[:-1], theta[-1]
        s = np.exp(ls)
        eta = X @ beta
        tot = 0.0
        for g in np.unique(subs):
            m = subs == g
            u = np.sqrt(2) * s * xs
            e = eta[m][:, None] + u[None, :]
            ll = (k[m][:, None] * e - n[m][:, None] * np.logaddexp(0, e)).sum(0)
            mx = ll.max()
            tot += mx + np.log((ws * np.exp(ll - mx)).sum() / np.sqrt(np.pi))
        return -tot

    x0 = np.zeros(X.shape[1] + 1)
    x0[-1] = np.log(0.5)
    r = minimize(nll, x0, method="BFGS")
    # numerical Hessian for standard errors
    h = 1e-4
    p = len(r.x)
    H = np.zeros((p, p))
    for i in range(p):
        for j in range(p):
            e_i = np.eye(p)[i] * h
            e_j = np.eye(p)[j] * h
            H[i, j] = (nll(r.x + e_i + e_j) - nll(r.x + e_i - e_j) - nll(r.x - e_i + e_j)
                       + nll(r.x - e_i - e_j)) / (4 * h * h)
    cov = np.linalg.inv(H)
    return r.x[:-1], np.sqrt(np.diag(cov))[:-1], -r.fun


# --------------------------------------------------------------------------- one subject, all measures

NB_READINGS = ("adjacent", "distance", "none")


def seed(*keys):
    """A fixed seed per claim section and subject, so that each has its own generator."""
    import zlib
    return zlib.crc32("/".join(map(str, keys)).encode())


JITTER_WINDOWS = {"data_pre": (0.6, 1.6), "data_encmain": (-0.3, 1.0), "data_proc": (-0.9, 0.7)}


def jitter_check(S, max_lag=0.4, n_shuffle=20):
    """Timing contrast between the trials with 900-ms and 1150-ms delays.

    The trial table puts the encoding epoch (data_encmain) at a fixed 1.9 s after the pretrial start
    and the processing epoch at 0.6 s + jitter + 0.8 s after the encoding start, so if the columns
    mark the events, the responses inside each window below occur at the same times in both groups:
    the start screen (data_pre, 0.6 to 1.6 s), the two stimuli (data_encmain, -0.3 to 1.0 s) and
    the test cue and its offset (data_proc, -0.9 to 0.7 s; the cue is on from -0.5 to 0.3 s). The
    measure is the 70-150 Hz amplitude (Hilbert envelope of a 4th-order Butterworth band, smoothed at
    10 Hz, each trace divided by its mean), averaged over trials per group; the shift of the
    1150-ms group that best aligns it with the 900-ms group over all channels is reported, with
    the shifts found for shuffled jitter labels as the reference. (A check, not a method of the
    paper; the band and windows are standard choices.)"""
    out = {}
    fs = S["fs"]
    for key, win in JITTER_WINDOWS.items():
        e = S[key]
        jit = e["trialinfo"][:, 4]
        x = e["x"].astype("float64")
        b, a = signal.butter(4, [70, min(150, fs / 2 - 20)], btype="band", fs=fs)
        env = np.abs(signal.hilbert(signal.filtfilt(b, a, x, axis=-1), axis=-1))
        env = signal.filtfilt(*signal.butter(2, 10, fs=fs), env, axis=-1)
        env = env / env.mean(-1, keepdims=True)
        w = win_index(e["time"], win)
        lags = np.arange(-int(max_lag * fs), int(max_lag * fs) + 1)

        def best(j):
            A = env[j == 900].mean(0)[:, w]
            A = (A - A.mean(1, keepdims=True)).ravel()
            B = env[j == 1150].mean(0)
            r = []
            for L in lags:
                Bb = B[:, w + L]
                Bb = (Bb - Bb.mean(1, keepdims=True)).ravel()
                r.append(A @ Bb / np.sqrt((A @ A) * (Bb @ Bb)))
            k = int(np.argmax(r))
            return float(lags[k] / fs), float(r[k])

        rng = np.random.default_rng(seed("jitter", S["subject"], key))
        lag, r = best(jit)
        sh = [best(rng.permutation(jit)) for _ in range(n_shuffle)]
        out[key] = {"lag_s": lag, "r": r, "shuffled_abs_lag_max_s": max(abs(v[0]) for v in sh),
                    "shuffled_r_max": max(v[1] for v in sh)}
        del env, x
    return out


def analyse_subject(S, chan, n_perm=N_PERM, do_time_resolved=True):
    """All per-subject measures used by the claims. chan: the subject's rows of channel_table()."""
    sid = S["subject"]
    fs = S["fs"]
    labels = list(chan.label)
    info = S["data_proc"]["trialinfo"]
    correct = info[:, 1] == 1
    cond = info[:, 3]
    R = {"subject": sid, "fs": fs, "labels": labels, "n_trials": len(info),
         "n_correct": int(correct.sum()), "n_incorrect": int((~correct).sum()),
         "n_correct_by_cond": {c: int((correct & (cond == c)).sum()) for c in (1, 2, 3)}}
    refs = list(S["clock"]["channels"].reference) if "clock" in S else None
    nb = {k: neighbours(labels, S.get("grid"), k, refs) for k in NB_READINGS}
    R["neighbours"] = {k: len(v) for k, v in nb.items()}
    ccond = cond[correct]
    contrasts = {"spatial": 2, "temporal": 3}

    # ERP: low-pass the whole epoch, baseline on the pretrial mean, processing window
    pre, proc = S["data_pre"], S["data_proc"]
    base = lowpass_fir(pre["x"][correct].astype("float64"), fs)[:, :, win_index(pre["time"], BASE_WIN)]
    erp = lowpass_fir(proc["x"][correct].astype("float64"), fs)[:, :, win_index(proc["time"], PROC_WIN)]
    erp = erp - base.mean(axis=(0, 2))[None, :, None]
    R["erp"] = {}
    for name, c2 in contrasts.items():
        m = (ccond == 1) | (ccond == c2)
        rng = np.random.default_rng(seed("erp", sid, name))
        res, _ = cluster_test(erp[m][:, :, None, :], ccond[m] == 1, nb, rng, n_perm)
        R["erp"][name] = {k: {s: [(mm, p) for mm, p, _ in v[s]] for s in v} for k, v in res.items()}
    del erp, base

    # Power: 3-cycle Hanning windows, 10-ms steps
    tidx, toi = toi_index(proc["time"], PROC_WIN)
    Fp = tfr_fourier(proc["x"][correct], proc["time"], fs, FOI, tidx)
    bidx, _ = toi_index(pre["time"], BASE_WIN)
    Fb = tfr_fourier(pre["x"][correct], pre["time"], fs, FOI, bidx)
    pw = np.abs(Fp) ** 2
    bp = (np.abs(Fb) ** 2).transpose(1, 2, 0, 3).reshape(len(labels), len(FOI), -1)
    r = int(correct.sum())
    N = bp.shape[-1]
    bmean = bp.mean(-1)
    bsd = bp.std(-1, ddof=1) * np.sqrt((N - r) / (N - 1)) / np.sqrt(r)
    pz = (pw - bmean[None, :, :, None]) / bsd[None, :, :, None]
    R["power_toi"] = toi - toi[0]
    R["power"] = {}
    for name, c2 in contrasts.items():
        m = (ccond == 1) | (ccond == c2)
        rng = np.random.default_rng(seed("power", sid, name))
        res, t_obs = cluster_test(pz[m], ccond[m] == 1, nb, rng, n_perm)
        out = {}
        for k, v in res.items():
            out[k] = {}
            for s in ("pos", "neg"):
                out[k][s] = [{"mass": mm, "p": p,
                              "elec_mask": mk.any(axis=(1, 2)),
                              "tsum_by_elec": np.where(mk, t_obs, 0).sum(axis=(1, 2)),
                              "t_masked": np.where(mk, t_obs, 0).astype("float32")} for mm, p, mk in v[s] if p < 0.05]
                out[k][s + "_minp"] = min([p for _, p, _ in v[s]], default=1.0)
        R["power"][name] = {"clusters": out, "t": t_obs.astype("float32")}
    del pw, pz, Fb

    # PSI
    pairs = pairs_same_hemisphere(chan)
    R["pairs"] = [(labels[i], labels[j], chan.hemisphere[i]) for i, j in pairs]
    ia = [i for i, _ in pairs]
    ib = [j for _, j in pairs]
    enc = S["data_encmain"]
    R["psi"] = {}
    for band, (lo, hi) in BANDS.items():
        foi = np.arange(lo, hi + 1)
        res = {}
        for interval, (ep, win) in {"maintenance": (enc, MAIN_WIN), "processing": (proc, PROC_WIN)}.items():
            F, freqs = fft_segment(ep["x"][correct], ep["time"], fs, win, foi)
            F = F - F.mean(0, keepdims=True)  # ERP (mean over all correct trials) removed
            rng = np.random.default_rng(seed("psi", sid, band, interval))
            res[interval] = psi_measures(F[:, ia], F[:, ib], rng, deposited=True)
        res["freqs"] = freqs
        R["psi"][band] = res
    # time-resolved PSI per condition (ERP of the condition removed), mtmconvol
    if do_time_resolved:
        R["psi_t"] = {}
        for band, (lo, hi) in BANDS.items():
            fsel = [list(FOI).index(f) for f in range(lo, hi + 1)]
            R["psi_t"][band] = {}
            for c in (1, 2, 3):
                F = Fp[ccond == c][:, :, fsel, :]
                F = F - F.mean(0, keepdims=True)
                rng = np.random.default_rng(seed("psi_t", sid, band, c))
                R["psi_t"][band][c] = psi_measures(F[:, ia], F[:, ib], rng, null_per_bin=False)
    del Fp
    return R


def load_subject(sid, chan):
    """Stream one subject and reduce it to what the claims use: (meta, results)."""
    S = stream_subject(sid, list(chan.label))
    meta = {k: S[k] for k in ["members", "primary_keys", "primary_shape", "primary_samples", "fs",
                              "trials", "clock", "elec_labels", "elec_labels_format"]}
    meta["grid"] = {g: (v["dims"], v["spacing"], len(v["pos"])) for g, v in S["grid"].items()}
    meta["epochs"] = {}
    for k in ["data_pre", "data_encmain", "data_proc"]:
        e = S[k]
        meta["epochs"][k] = {"shape": e["x"].shape, "t0": float(e["time"][0]), "t1": float(e["time"][-1]),
                             "lengths": e["lengths"], "starts": e["starts"], "n_labels": len(e["labels_all"]),
                             "fs": e["fs"], "hdr_nSamples": e["hdr_nSamples"],
                             "min": float(e["x"].min()), "max": float(e["x"].max()), "sd": float(e["x"].std()),
                             "trialinfo_equals_table": bool(np.array_equal(e["trialinfo"], S["trials"].iloc[:, :6].values))}
    meta["jitter"] = jitter_check(S)
    R = analyse_subject(S, chan)
    del S
    return meta, R
