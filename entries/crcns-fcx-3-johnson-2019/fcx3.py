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
  (Methods, Spectral Decomposition; power_compute.m). Main reading: the 900-ms segment alone,
  embedded in zeros, every window computed (Methods: "Data segments were zero-padded to 7,500 ms";
  claims file S1 reading (a)). Variant 'code': windows on the whole derived epoch (-1.5 to 3.0 s),
  so that long windows take in the data around the segment, as power_compute.m does (cfg.toi over
  the whole epoch, [0.3 1.2] s cut afterwards). The baseline z-score of zbaseline.m (mean and SD of
  the means of r baseline points drawn without replacement, r the number of correct trials) is
  computed in closed form, as the limit of the code's 1000 draws (a standard choice, which cannot
  change a result: the z-score is the same affine map for every trial at a channel and frequency,
  so the condition t-tests do not change).
- ERP: the 200-ms baseline and 900-ms processing segments zero padded to 7.5 s and low-passed at
  30 Hz, baseline the pretrial temporal mean over trials (Methods, Event-Related Potentials;
  erp_compute.m for the mean over trials). The FIR order 3*fix(fs/30), applied forwards and
  backwards, is FieldTrip's default for a 'fir' low-pass, which the script uses (standard choice).
  Variants: per-trial baseline, the Results' 1-30 Hz band-pass, the whole epoch filtered
  (erp_compute.m), and the 900-ms-delay trials only (see `erp_epochs`).
- Cluster test: independent-samples t per point, threshold two-tailed 0.05, cluster mass the sum
  of t, 1000 shuffles of the condition labels, connectivity across time and frequency within a
  channel and across neighbouring channels at the same time and frequency (Methods, ERPs,
  paragraph 2, and Spectral Decomposition, paragraph 3). The deposited scripts hold no cluster
  test, so neighbours and the alpha per tail are not stated anywhere; the readings are in
  `neighbours`.
- PSI: ERP subtracted (mean over all correct trials for the task-induced PSI, per condition for the
  time-resolved PSI: psi_compute.m and subtracterp.m), one Hanning-tapered FFT of each 900-ms
  segment padded to 7.5 s read at the bins nearest to the integer frequencies (task-induced,
  psi_compute.m 'mtmfft'), or the 3-cycle windows at 10-ms steps (time-resolved, 'mtmconvol', on
  the zero-padded segment, with the whole-epoch windows of the code as a variant). Bands 2 to 7
  and 9 to 24 Hz (Methods, Task-Induced PSI). The null shuffles the frequencies of one signal and
  recomputes the same statistic (Methods), 1000 shuffles, one shuffle for all pairs and trials;
  see `psi_z`.
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


def script_files():
    """The paper's MATLAB scripts deposited with the data (analysis_scripts.zip), read into memory:
    {path inside analysis_scripts/: text}."""
    import zipfile
    z = zipfile.ZipFile(io.BytesIO(read_bytes("analysis_scripts.zip")))
    return {n.split("analysis_scripts/")[-1]: z.read(n).decode(errors="replace")
            for n in z.namelist() if n.endswith(".m")}


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


def _unit(x):
    a = np.abs(x)
    return x / np.where(a > 0, a, 1)


def psi_z(A, B, ia, ib, rng, n_perm=N_PERM, code_null=False):
    """PSI z per pair and time point, A = PFC (positive: PFC leads), B = parietal.

    A: trials x nA x f x T, B: trials x nB x f x T complex spectra of the channels, ERP already
    removed (T = 1 for the task-induced PSI). ia, ib: channel indices of each pair into A and B.
    Returns {reading: z, pairs x T} for the readings of the claims file (header P1):

    - 'a': PSI from the trial-averaged coherency C_f = <A conj(B)> / sqrt(<|A|^2><|B|^2>), the sum
      over adjacent bins of Im(conj(C_f) C_{f+1}) (Nolte et al. 2008).
    - 'b': PSI per trial from the per-trial normalised cross-spectrum A conj(B) / |A B| (the
      structure of psianalysis.m, with the conjugate the Methods' cross-spectral density implies),
      averaged over trials.

    The null follows the Methods (Task-Induced PSI, paragraph 2): "we randomly shuffled the
    frequencies in one signal and re-computed PSI 1,000 times". Each shuffle permutes the frequency
    bins of the parietal signal B, the same permutation in every trial and pair (P1 null reading
    (a)), and the same statistic is recomputed from the shuffled spectra, so that the null and the
    observed value are the same measure; z = (observed - null mean) / null SD per pair and time
    point. The paper's "at each ... frequency point" is met by the one band value of P1 band
    reading (a); psianalysis.m repeats one null per bin, which only adds draws (a standard choice).

    code_null=True adds 'b_code': reading (b) z-scored against the null of psianalysis.m, the slope
    of the trial-mean normalised cross-spectrum with the bins of both factors shuffled
    independently and summed over all nf pairs of bins. That null is not the observed statistic
    (its spread shrinks with 1/sqrt(trials)); it is shown only to compare with the paper's code.
    """
    R, nA, nf, T = A.shape
    nB = B.shape[1]
    ia, ib = np.asarray(ia), np.asarray(ib)
    out = {}
    # (b) per-trial phasors: slope_r = Im sum_f DA_f conj(DB_f), DA_f = conj(ua_f) ua_{f+1}
    ua, ub = _unit(A).astype(np.complex64), _unit(B).astype(np.complex64)
    DA = np.conj(ua[:, :, :-1]) * ua[:, :, 1:]
    MA = DA.transpose(3, 1, 0, 2).reshape(T, nA, R * (nf - 1))

    def stat_b(p):
        DB = np.conj(ub[:, :, p[:-1]]) * ub[:, :, p[1:]]
        MB = np.conj(DB).transpose(3, 0, 2, 1).reshape(T, R * (nf - 1), nB)
        return (MA @ MB).imag[:, ia, ib].T / R

    # (a) coherency: Y[p, t, f, g] = <A_f conj(B_g)> / sqrt(<|A_f|^2> <|B_g|^2>) for every pair of bins
    Ar = A.transpose(3, 1, 2, 0).reshape(T, nA * nf, R)
    Br = B.transpose(3, 0, 1, 2).reshape(T, R, nB * nf)
    X = (Ar @ np.conj(Br) / R).reshape(T, nA, nf, nB, nf)
    Na = np.sqrt((np.abs(A) ** 2).mean(0))  # nA x f x T
    Nb = np.sqrt((np.abs(B) ** 2).mean(0))
    Y = X[:, ia, :, ib, :]  # pairs x T x f x g
    Y = Y / (Na[ia].transpose(0, 2, 1)[:, :, :, None] * Nb[ib].transpose(0, 2, 1)[:, :, None, :])
    Y = Y.astype(np.complex64)
    fidx = np.arange(nf)

    def stat_a(p):
        return _slope(Y[:, :, fidx, p])

    ident = np.arange(nf)
    obs = {"a": stat_a(ident), "b": stat_b(ident)}
    s1 = {k: np.zeros(v.shape) for k, v in obs.items()}
    s2 = {k: np.zeros(v.shape) for k, v in obs.items()}
    for _ in range(n_perm):
        p = rng.permutation(nf)
        for k, f in (("a", stat_a), ("b", stat_b)):
            v = f(p)
            s1[k] += v
            s2[k] += v * v
    for k in obs:
        mean = s1[k] / n_perm
        sd = np.sqrt(np.maximum(s2[k] - n_perm * mean ** 2, 0) / (n_perm - 1))
        out[k] = (obs[k] - mean) / sd
    if code_null:
        pp = (ua[:, ia] * np.conj(ub[:, ib])).mean(0).transpose(0, 2, 1)  # pairs x T x f
        c1, c2 = np.zeros(obs["b"].shape), np.zeros(obs["b"].shape)
        for _ in range(n_perm):
            v = np.imag(np.conj(pp[..., rng.permutation(nf)]) * pp[..., rng.permutation(nf)]).sum(-1)
            c1 += v
            c2 += v * v
        mean = c1 / n_perm
        sd = np.sqrt(np.maximum(c2 - n_perm * mean ** 2, 0) / (n_perm - 1))
        out["b_code"] = (obs["b"] - mean) / sd
    return out


def psi_deposited(Fa, Fb, rng, n_perm=N_PERM):
    """psianalysis.m as deposited (task-induced): the 'cross-spectrum' is X*Y without the conjugate,
    normalised by sqrt(X^2 conj(Y^2)), which equals +-exp(2i phase(Y)) and so depends on the second
    channel only; z against the code's null (see psi_z, code_null). 'code': PFC first; 'code_rev':
    parietal first, sign reversed. Not a reading of the paper: shown only for the code_mismatch
    finding. Fa, Fb: trials x pairs x f."""
    out = {}
    nf = Fa.shape[-1]
    for key, (X, Y) in {"code": (Fa, Fb), "code_rev": (Fb, Fa)}.items():
        ptr = X * Y / np.sqrt((X ** 2) * np.conj(Y ** 2))
        obs = _slope(ptr).mean(0)
        pp = ptr.mean(0)
        s1, s2 = np.zeros(obs.shape), np.zeros(obs.shape)
        for _ in range(n_perm):
            v = np.imag(np.conj(pp[..., rng.permutation(nf)]) * pp[..., rng.permutation(nf)]).sum(-1)
            s1 += v
            s2 += v * v
        mean = s1 / n_perm
        sd = np.sqrt((s2 - n_perm * mean ** 2) / (n_perm - 1))
        out[key] = (obs - mean) / sd * (-1 if key == "code_rev" else 1)
    return out


# --------------------------------------------------------------------------- group models

def paired_lme(y1, y2, subject):
    """Linear mixed model y ~ condition + (1|subject) + (1|pair) on two values per pair.

    With every pair holding both values, the REML estimate of the condition effect is the mean of
    the paired differences and its test the paired t-test over pairs (the subject and pair
    intercepts cancel in the differences); the F is reported with the residual degrees of freedom
    2n - 2, as MATLAB's fitlme does. The notebook checks this against statsmodels' MixedLM. As in the
    paper's degrees of freedom (F(1,2256) for 1129 pairs), pairs that share electrodes are treated as
    independent, which inflates F; the notebook prints subject-level tests beside it.
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


def bandpass_fir(x, fs, lo=1.0, hi=30.0, pad=PAD_S):
    """FieldTrip-style FIR band-pass (order 3*fix(fs/lo), forwards and backwards) on the epoch
    zero padded to pad s: the Results' "1-30 Hz bandpass" (Event-Related Potentials), a variant."""
    order = 3 * int(fs // lo)
    b = signal.firwin(order + 1, [lo / (fs / 2), hi / (fs / 2)], pass_zero=False)
    n = x.shape[-1]
    left = max(0, (int(round(pad * fs)) - n) // 2)
    xp = np.zeros(x.shape[:-1] + (n + 2 * left,))
    xp[..., left:left + n] = x
    return signal.filtfilt(b, [1.0], xp, axis=-1, padtype=None)[..., left:left + n]


def erp_epochs(pre, proc, sel, fs, config):
    """Processing-interval ERPs (trials x ch x time) under one reading.

    'methods': the 200-ms pretrial and 900-ms processing segments cut first, each zero padded to
    7.5 s and low-passed at 30 Hz (Methods, Event-Related Potentials: "The correct-trial 200-ms
    pretrial baseline and 900-ms post-cue processing data segments were zero-padded to 7,500 ms ...
    and passed through a 30-Hz low-pass finite impulse response filter"); baseline the pretrial
    temporal mean averaged over trials, one value per channel, as erp_compute.m computes it
    (nanmean over trials of the per-trial temporal means). A constant per channel cannot change the
    t-tests. 'per_trial_baseline': as 'methods', each trial corrected on its own pretrial mean (the
    Methods' "post-cue processing - pretrial mean" allows it). 'bandpass': as 'methods' with the
    Results' "1-30 Hz bandpass". 'code': the whole derived epoch filtered, then the windows cut
    (erp_compute.m)."""
    if config == "code":
        base = lowpass_fir(pre["x"][sel].astype("float64"), fs)[:, :, win_index(pre["time"], BASE_WIN)]
        erp = lowpass_fir(proc["x"][sel].astype("float64"), fs)[:, :, win_index(proc["time"], PROC_WIN)]
    else:
        filt = bandpass_fir if config == "bandpass" else lowpass_fir
        base = filt(pre["x"][sel][:, :, win_index(pre["time"], BASE_WIN)].astype("float64"), fs)
        erp = filt(proc["x"][sel][:, :, win_index(proc["time"], PROC_WIN)].astype("float64"), fs)
    if config == "per_trial_baseline":
        return erp - base.mean(axis=2)[:, :, None]
    return erp - base.mean(axis=(0, 2))[None, :, None]


def processing_tfr(proc, sel, fs, foi, config):
    """3-cycle Hanning spectra of the processing interval at 10-ms steps: trials x ch x f x 91.

    'methods': the 900-ms segment alone, embedded in zeros, every window computed (Methods,
    Spectral Decomposition: "Data segments were zero-padded to 7,500 ms"; S1 reading (a), the
    claims file's main reading). 'code': windows on the whole derived epoch, so that windows longer
    than the segment take in the data around it (power_compute.m and psi_compute.m compute
    ft_freqanalysis with cfg.toi over the whole epoch and cut [0.3 1.2] s afterwards), a variant:
    where the Methods and the code differ the Methods come first (protocol, Reader step 2)."""
    if config == "code":
        tidx, _ = toi_index(proc["time"], PROC_WIN)
        return tfr_fourier(proc["x"][sel], proc["time"], fs, foi, tidx)
    w = win_index(proc["time"], PROC_WIN)
    seg = proc["x"][sel][:, :, w]
    tidx, _ = toi_index(proc["time"][w], PROC_WIN)
    return tfr_fourier(seg, proc["time"][w], fs, foi, tidx)


ERP_CONFIGS = ("methods", "per_trial_baseline", "bandpass", "code", "methods_900")
POWER_CONFIGS = ("methods", "code", "methods_900")
PSI_T_CONFIGS = ("methods", "code")


def _power_clusters(pz, ccond, nb, sid, name, config, n_perm):
    m = (ccond == 1) | (ccond == {"spatial": 2, "temporal": 3}[name])
    rng = np.random.default_rng(seed("power", sid, name, config))
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
    return {"clusters": out}


def analyse_subject(S, chan, n_perm=N_PERM, do_time_resolved=True):
    """All per-subject measures used by the claims. chan: the subject's rows of channel_table()."""
    sid = S["subject"]
    fs = S["fs"]
    labels = list(chan.label)
    info = S["data_proc"]["trialinfo"]
    correct = info[:, 1] == 1
    cond = info[:, 3]
    jit = info[:, 4]
    R = {"subject": sid, "fs": fs, "labels": labels, "n_trials": len(info),
         "n_correct": int(correct.sum()), "n_incorrect": int((~correct).sum()),
         "n_correct_by_cond": {c: int((correct & (cond == c)).sum()) for c in (1, 2, 3)},
         "n_correct_900_by_cond": {c: int((correct & (cond == c) & (jit == 900)).sum()) for c in (1, 2, 3)}}
    refs = list(S["clock"]["channels"].reference) if "clock" in S else None
    nb = {k: neighbours(labels, S.get("grid"), k, refs) for k in NB_READINGS}
    R["neighbours"] = {k: len(v) for k, v in nb.items()}
    ccond = cond[correct]
    j900 = jit[correct] == 900
    contrasts = {"spatial": 2, "temporal": 3}
    pre, proc = S["data_pre"], S["data_proc"]

    # ERP under each reading; 'methods_900' is 'methods' on the trials with a 900-ms delay only
    R["erp"] = {}
    for config in ERP_CONFIGS:
        base_cfg = "methods" if config == "methods_900" else config
        erp = erp_epochs(pre, proc, correct, fs, base_cfg)
        keep = j900 if config == "methods_900" else np.ones(len(ccond), bool)
        R["erp"][config] = {}
        for name, c2 in contrasts.items():
            m = keep & ((ccond == 1) | (ccond == c2))
            rng = np.random.default_rng(seed("erp", sid, name, config))
            res, _ = cluster_test(erp[m][:, :, None, :], ccond[m] == 1, nb, rng, n_perm)
            R["erp"][config][name] = {k: {s: [(mm, p) for mm, p, _ in v[s]] for s in v} for k, v in res.items()}
        del erp

    # Power: 3-cycle Hanning windows, 10-ms steps. The baseline z-score (zbaseline.m, closed form) is
    # one affine map per channel and frequency, so it is applied for the record but cannot change a
    # t-test; the baseline spectra are those of the 200-ms segment zero padded (Methods).
    _, toi = toi_index(proc["time"], PROC_WIN)
    R["power_toi"] = toi - toi[0]
    wb = win_index(pre["time"], BASE_WIN)
    bidx, _ = toi_index(pre["time"][wb], BASE_WIN)
    Fb = tfr_fourier(pre["x"][correct][:, :, wb], pre["time"][wb], fs, FOI, bidx)
    bp = (np.abs(Fb) ** 2).transpose(1, 2, 0, 3).reshape(len(labels), len(FOI), -1)
    del Fb
    r = int(correct.sum())
    N = bp.shape[-1]
    bmean = bp.mean(-1)
    bsd = bp.std(-1, ddof=1) * np.sqrt((N - r) / (N - 1)) / np.sqrt(r)
    R["power"] = {}
    Fp = {}
    for config in ("methods", "code"):
        Fp[config] = processing_tfr(proc, correct, fs, FOI, config)
        pz = (np.abs(Fp[config]) ** 2 - bmean[None, :, :, None]) / bsd[None, :, :, None]
        R["power"][config] = {name: _power_clusters(pz, ccond, nb, sid, name, config, n_perm) for name in contrasts}
        if config == "methods":
            R["power"]["methods_900"] = {name: _power_clusters(pz[j900], ccond[j900], nb, sid, name, "methods_900", n_perm)
                                         for name in contrasts}
        del pz

    # Task-induced PSI: one FFT of each 900-ms segment, ERP (mean over all correct trials) removed
    pairs = pairs_same_hemisphere(chan)
    R["pairs"] = [(labels[i], labels[j], chan.hemisphere[i]) for i, j in pairs]
    pfc = sorted({i for i, _ in pairs})
    par = sorted({j for _, j in pairs})
    ia = np.array([pfc.index(i) for i, _ in pairs])
    ib = np.array([par.index(j) for _, j in pairs])
    enc = S["data_encmain"]
    R["psi"], R["psi_surrogate"], R["psi_deposited"] = {}, {}, {}
    for band, (lo, hi) in BANDS.items():
        foi = np.arange(lo, hi + 1)
        res, sur, dep = {}, {}, {}
        for interval, (ep, win) in {"maintenance": (enc, MAIN_WIN), "processing": (proc, PROC_WIN)}.items():
            F, freqs = fft_segment(ep["x"][correct], ep["time"], fs, win, foi)
            F = F - F.mean(0, keepdims=True)
            A, B = F[:, pfc, :, None], F[:, par, :, None]
            rng = np.random.default_rng(seed("psi", sid, band, interval))
            res[interval] = {k: v[:, 0] for k, v in psi_z(A, B, ia, ib, rng, code_null=True).items()}
            rng = np.random.default_rng(seed("psi_deposited", sid, band, interval))
            dep[interval] = psi_deposited(F[:, [pfc[i] for i in ia]], F[:, [par[j] for j in ib]], rng)
            if interval == "processing":
                # surrogate: parietal trials paired with other trials' PFC data (no trial-locked coupling)
                rng = np.random.default_rng(seed("psi_surrogate", sid, band))
                order = rng.permutation(A.shape[0])
                sur = {k: v[:, 0] for k, v in psi_z(A, B[order], ia, ib, rng, code_null=True).items()}
                sur["same_trial_fraction"] = float(np.mean(order == np.arange(len(order))))
        res["freqs"] = freqs
        R["psi"][band] = res
        R["psi_surrogate"][band] = sur
        R["psi_deposited"][band] = dep

    # time-resolved PSI per condition (ERP of the condition removed), mtmconvol, under each spectra reading
    if do_time_resolved:
        R["psi_t"] = {}
        for config in PSI_T_CONFIGS:
            R["psi_t"][config] = {}
            for band, (lo, hi) in BANDS.items():
                fsel = [list(FOI).index(f) for f in range(lo, hi + 1)]
                R["psi_t"][config][band] = {}
                for c in (1, 2, 3):
                    F = Fp[config][ccond == c][:, :, fsel, :]
                    F = F - F.mean(0, keepdims=True)
                    rng = np.random.default_rng(seed("psi_t", sid, band, c, config))
                    R["psi_t"][config][band][c] = psi_z(F[:, pfc], F[:, par], ia, ib, rng)
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
