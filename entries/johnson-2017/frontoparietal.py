"""Loading and measures for Johnson et al. (2017), "Bidirectional Frontoparietal Oscillatory
Systems Support Working Memory" (doi:10.1016/j.cub.2017.05.046), on CRCNS data set pfc-5
(doi:10.6080/K0ZC811B), read as crcns:pfc-5/unversioned from the public bucket crcnsarchive.

Where each parameter comes from:

- The claims file (claims/johnson-2017.yaml), "shared methods", gives the measures: correct
  trials, 3-cycle Hanning windows (3/f), 10 ms steps for power and 100 ms for PSI, zero padding
  to 7500 ms, bootstrapped Z against the pretrial baseline, PSI over 2-7 and 9-24 Hz Z scored on
  a frequency-shuffled null, then baseline corrected, and the cluster test (independent t,
  cluster-forming threshold 0.05 two-tailed, sum of t, 1000 shuffles).
- The paper's own code, deposited in the data set (pfc-5/live/analysis_scripts.tar.gz, read in
  the notebook), settles the details the claims file leaves open (the claims file allows this,
  "Where those scripts settle a detail named as open below, the author may follow them"):
  FieldTrip's biosemi64 neighbour template and minnbchan = 2 (O1; *_stat_group.m); the
  hemisphere index as 27 left minus right channels in the code's order (O3;
  *_stat_group_hem.m); the swap of 10 controls and the surface Laplacian already in
  data_derived.mat (O4, O5; the data descriptor); mtmconvol and mtmfft as FieldTrip computes them
  (tfr_compute.m, fft_compute.m, psi_compute.m); zbaseline.m draws r = the trial count of the data
  being scored (per visual hemifield); degree as FieldTrip's ft_networkanalysis 'degrees' with
  threshold 1.96 on the signed Z (psi_compute.m), which counts connections with Z > 1.96 in or
  out of a channel; the PSI group test per seed channel A, clustering over neighbours of B and
  time (psi_stat_group.m). FieldTrip's code is read at commit
  b3909bfecc5273652756ed2e41f84e9195f96186 (the last before release 20151205, the one the paper
  cites).
- Assumptions (step 1.6), each stated in the notebook with every reading run:
  * Window edges. FieldTrip's mtmconvol returns NaN wherever a 3/f window does not fit inside
    the segment; the deposited segments have no buffers (500, 1500 and 900 ms), so below 6 Hz
    no baseline value exists. Reading "fit" keeps FieldTrip's mask; reading "pad" keeps the
    convolution values over the zero padding the paper names ("zero-padded to 7,500 ms"). The
    two give identical values wherever the window fits.
  * The bootstrap of zbaseline.m is replaced by its exact expectation: the mean of r draws
    without replacement from N pooled baseline values has mean mu and standard deviation
    sd / sqrt(r) * sqrt((N - r) / (N - 1)). This removes the Monte Carlo noise of 1000 draws.
  * PSI. The Methods compute the cross-spectral density and PSI after Nolte et al. (2008)
    (reading "nolte": coherency of the trial-averaged cross-spectrum). psianalysis.m instead
    averages per-trial phase slopes and multiplies the Fourier coefficients without a complex
    conjugate; reading "trialwise" follows its structure with the conjugate. The null shuffles
    the frequency bins and recomputes PSI (Methods); psianalysis.m draws two independent
    permutations, which reading "trialwise" follows.
- Standard choices that cannot change a result: the random seeds; the FIR filter of the ERPs
  (FieldTrip's default order 3 * fix(fs / 30) with a Hamming window, applied forwards and
  backwards, to the trial average, which is the same as averaging filtered trials).
"""

from __future__ import annotations

import hashlib
import io
import os
import re
import tarfile
import urllib.request
import warnings

import numpy as np

BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-5/live/"
DATASET = "crcns:pfc-5/unversioned"
DATASET_DOI = "10.6080/K0ZC811B"
FIELDTRIP_COMMIT = "b3909bfecc5273652756ed2e41f84e9195f96186"
NEIGHBOURS_URL = ("https://raw.githubusercontent.com/fieldtrip/fieldtrip/"
                  f"{FIELDTRIP_COMMIT}/template/neighbours/biosemi64_neighb.mat")

CONTROLS = [f"ctrl{i:02d}" for i in range(1, 21)]
PATIENTS = [f"pfc{i:02d}" for i in range(1, 15)]
SUBJECTS = CONTROLS + PATIENTS

FS = 256.0
PAD = 7.5                     # seconds, cfg.pad = 7.5 in every *_compute.m
FREQS = np.arange(1, 41)      # 1 to 40 Hz (claims file, shared methods)
BANDS = {"dt": np.arange(2, 8), "ab": np.arange(9, 25)}   # PSI bands (psi_compute.m)

# One channel order for every subject (ctrl01's). The files do not share an order: an
# interpolated channel sits at the end of the list in some subjects.
CANON = ['Fp1', 'AF7', 'AF3', 'F1', 'F3', 'F5', 'F7', 'FT7', 'FC5', 'FC3', 'FC1', 'C1', 'C3', 'C5', 'T7',
         'TP7', 'CP5', 'CP3', 'CP1', 'P1', 'P3', 'P5', 'P7', 'P9', 'PO7', 'PO3', 'O1', 'Iz', 'Oz', 'POz', 'Pz',
         'CPz', 'Fpz', 'Fp2', 'AF8', 'AF4', 'AFz', 'Fz', 'F2', 'F4', 'F6', 'F8', 'FT8', 'FC6', 'FC4', 'FC2',
         'FCz', 'Cz', 'C2', 'C4', 'C6', 'T8', 'TP8', 'CP6', 'CP4', 'CP2', 'P2', 'P4', 'P6', 'P8', 'P10', 'PO8',
         'PO4', 'O2']

# Hemisphere index channels, in the order of *_stat_group_hem.m
LEFT = ['Fp1', 'AF7', 'AF3', 'F1', 'F3', 'F5', 'F7', 'FT7', 'FC5', 'FC3', 'FC1', 'C1', 'C3', 'C5',
        'T7', 'TP7', 'CP5', 'CP3', 'CP1', 'P1', 'P3', 'P5', 'P7', 'P9', 'PO7', 'PO3', 'O1']
RIGHT = ['Fp2', 'AF8', 'AF4', 'F2', 'F4', 'F6', 'F8', 'FT8', 'FC6', 'FC4', 'FC2', 'C2', 'C4', 'C6',
         'T8', 'TP8', 'CP6', 'CP4', 'CP2', 'P2', 'P4', 'P6', 'P8', 'P10', 'PO8', 'PO4', 'O2']


# ----------------------------------------------------------------------------- reading

def fetch(name: str) -> bytes:
    """A small file of the data set, whole (docs, checksums, scripts)."""
    with urllib.request.urlopen(BUCKET + name) as r:
        return r.read()


def stream_subject_files(sid: str) -> dict:
    """Stream <sid>.tar.gz from the bucket and return data_derived.mat (bytes) and
    summary_file_trial.csv (bytes). The tar is read as a gzip stream; the raw .bdf that comes
    first is decompressed and skipped, never kept or written. A tar.gz can only be read in
    order, so it is read as one HTTP stream (urllib), not with fsspec's range requests, which
    were four times slower here (35 s against 9 s for pfc02)."""
    out = {"members": []}
    with urllib.request.urlopen(BUCKET + f"data/{sid}.tar.gz") as f:
        with tarfile.open(fileobj=f, mode="r|gz") as tf:
            for m in tf:
                out["members"].append((m.name, m.size))
                if m.name.endswith("data_derived.mat"):
                    out["derived"] = tf.extractfile(m).read()
                elif "summary_file_trial" in m.name and m.isfile():
                    out.setdefault("csv_all", []).append((m.name, tf.extractfile(m).read()))
    return out


def read_derived(raw: bytes) -> dict:
    """data_derived.mat (MATLAB 7.3) into arrays: per segment, data (trials, 64, samples),
    time, trialinfo (trials, 7), fsample; and the labels."""
    import h5py
    f = h5py.File(io.BytesIO(raw), "r")
    out = {}
    for seg in ("pretrial", "encmain", "proc"):
        g = f[seg]
        refs = g["trial"][()].ravel()
        trials = [f[r][()].T for r in refs]          # stored (samples, 64): transpose
        lens = {t.shape[1] for t in trials}
        times = [f[r][()].ravel() for r in g["time"][()].ravel()]
        out[seg] = {
            "data": np.stack(trials) if len(lens) == 1 else trials,
            "lengths": sorted(lens),
            "time": times[0],
            "time_first": sorted({round(float(t[0]), 6) for t in times}),
            "trialinfo": g["trialinfo"][()].T,
            "fsample": float(g["fsample"][()].ravel()[0]),
        }
    out["label"] = ["".join(chr(c) for c in f[r][()].ravel()) for r in f["encmain"]["label"][()].ravel()]
    return out


def read_trial_csv(raw: bytes):
    import pandas as pd
    cols = ["trial", "correct", "vhf", "type", "condition", "jitter", "rt", "t_pre", "t_enc", "t_proc"]
    return pd.read_csv(io.BytesIO(raw), header=None, names=cols)


def neighbours(labels: list[str]) -> np.ndarray:
    """FieldTrip's biosemi64 neighbour template (what ft_prepare_neighbours with
    layout biosemi64.lay and method 'template' loads), as a boolean adjacency over labels."""
    import scipy.io
    with urllib.request.urlopen(NEIGHBOURS_URL) as r:
        m = scipy.io.loadmat(io.BytesIO(r.read()), squeeze_me=True)
    idx = {l.lower(): i for i, l in enumerate(labels)}
    A = np.zeros((len(labels), len(labels)), bool)
    for n in m["neighbours"]:
        a = idx.get(str(n["label"]).lower())
        if a is None:
            continue
        for b in np.atleast_1d(n["neighblabel"]):
            b = idx.get(str(b).lower())
            if b is not None:
                A[a, b] = A[b, a] = True
    return A


# ----------------------------------------------------------------------------- spectral

def hanning(n: int) -> np.ndarray:
    """MATLAB hanning(n): no zero end points."""
    k = np.arange(1, n + 1)
    return 0.5 * (1 - np.cos(2 * np.pi * k / (n + 1)))


def mtmconvol(x: np.ndarray, freqs, toi_step: float, fs: float = FS, pad: float = PAD):
    """FieldTrip ft_specest_mtmconvol (commit above) with a Hanning taper and t_ftimwin = 3/f.
    x: (..., nsamples), demeaned first (ft_freqanalysis polyremoval 0). Returns the complex
    spectrum (..., nfreq, ntime), the boolean mask of the points FieldTrip keeps (window inside
    the data), and the times. Outside the mask the values are the convolution over the zero
    padding ("pad" reading); FieldTrip sets them to NaN ("fit" reading)."""
    x = x - x.mean(axis=-1, keepdims=True)
    nd = x.shape[-1]
    N = int(round(pad * fs))
    tend = (nd - 1) / fs
    toi = np.unique(np.round(np.arange(0, tend + 1e-9, toi_step) * fs) / fs)
    tb = np.round(toi * fs).astype(int) + 1                      # 1-based sample of each time
    import scipy.fft as sfft
    X = sfft.fft(x.astype(np.float32), n=N, axis=-1)                 # complex64
    out = np.empty(x.shape[:-1] + (len(freqs), len(toi)), np.complex64)
    mask = np.zeros((len(freqs), len(toi)), bool)
    for i, f in enumerate(freqs):
        tw = 3.0 / f
        L = int(round(tw * fs))
        tap = hanning(L)
        tap = tap / np.linalg.norm(tap)
        tappad = int(np.ceil(N / 2) - np.floor(L / 2))
        ang = np.arange(-(L - 1) / 2, (L - 1) / 2 + 1) * (2 * np.pi / fs) * f
        w = np.zeros(N, complex)
        w[tappad:tappad + L] = tap * np.exp(1j * ang)
        dum = sfft.ifft(X * sfft.fft(w).astype(np.complex64), axis=-1)
        # fftshift then take samples tb - 1: the same as taking (tb - 1 + N // 2) mod N
        out[..., i, :] = dum[..., (tb - 1 + N // 2) % N] * np.sqrt(2.0 / L)
        ns = tw * fs
        mask[i] = (tb >= ns / 2) & (tb < nd - ns / 2)
    return out, mask, toi


def mtmfft_power(x: np.ndarray, freqs, fs: float = FS, pad: float = PAD) -> np.ndarray:
    """FieldTrip ft_specest_mtmfft, Hanning taper over the whole segment, padded to 7.5 s;
    power |F|^2 at the requested frequencies. x: (..., nsamples)."""
    x = x - x.mean(axis=-1, keepdims=True)
    nd = x.shape[-1]
    N = int(round(pad * fs))
    tap = hanning(nd)
    tap = tap / np.linalg.norm(tap)
    F = np.fft.fft(x * tap, n=N, axis=-1) * np.sqrt(2.0 / nd)
    idx = np.round(np.asarray(freqs) * pad).astype(int)
    return np.abs(F[..., idx]) ** 2


def lowpass_fir(x: np.ndarray, fc: float = 30.0, fs: float = FS) -> np.ndarray:
    """FieldTrip's default FIR low-pass (order 3 * fix(fs / fc), fir1, two-pass), with
    mirror padding to 7.5 s as cfg.padding = 7.5 asks."""
    from scipy.signal import firwin, filtfilt
    order = 3 * int(fs // fc)
    b = firwin(order + 1, fc / (fs / 2))
    nd = x.shape[-1]
    npad = max(0, (int(round(PAD * fs)) - nd) // 2)
    xp = np.pad(x, [(0, 0)] * (x.ndim - 1) + [(npad, npad)], mode="reflect") if npad < nd else \
        np.pad(x, [(0, 0)] * (x.ndim - 1) + [(npad, npad)], mode="symmetric")
    y = filtfilt(b, [1.0], xp, axis=-1)
    return y[..., npad:npad + nd]


# ----------------------------------------------------------------------------- PSI

def _perm_matrix(nf: int, n_perm: int, rng, mode: str) -> np.ndarray:
    """Indicator matrix (nf*nf, n_perm): which (i, j) frequency pairs enter each null PSI.
    'adjacent': one shuffle of the bins, PSI over adjacent pairs (Methods).
    'code': two independent shuffles, nf pairs (psianalysis.m)."""
    P = np.zeros((nf * nf, n_perm), np.float32)
    for p in range(n_perm):
        if mode == "adjacent":
            pi = rng.permutation(nf)
            i, j = pi[:-1], pi[1:]
        else:
            i, j = rng.permutation(nf), rng.permutation(nf)
        np.add.at(P[:, p], i * nf + j, 1.0)
    return P


def _z_from_M(M: np.ndarray, obs: np.ndarray, P: np.ndarray) -> np.ndarray:
    """M: (rows, nf*nf) of Im(conj(C_i) C_j); obs: (rows,). Z of obs on the null M @ P
    (MATLAB std, ddof 1)."""
    z = np.empty(M.shape[0], np.float32)
    step = 4096
    for s in range(0, M.shape[0], step):
        null = M[s:s + step] @ P
        mu = null.mean(axis=1)
        sd = null.std(axis=1, ddof=1)
        with np.errstate(invalid="ignore", divide="ignore"):
            z[s:s + step] = (obs[s:s + step] - mu) / sd
    return z


def psi_z(F: np.ndarray, n_perm: int = 1000, seed: int = 0) -> dict:
    """PSI Z for every ordered channel pair and time point. F: (trials, chan, nf, nt) complex.
    Returns {'nolte', 'trialwise', 'literal'}, each (chan, chan, nt). PSI(a, b) = Im sum_f
    conj(C_ab(f)) C_ab(f+1) with C_ab built from X_a conj(X_b), so positive Z(a, b) means a leads
    b (Nolte et al. 2008). 'literal' is psianalysis.m as written (see psianalysis_literal_pp)."""
    ntr, nc, nf, nt = F.shape
    rng = np.random.default_rng(seed)
    P_adj = _perm_matrix(nf, n_perm, rng, "adjacent")
    P_code = _perm_matrix(nf, n_perm, rng, "code")
    out = {k: np.empty((nc, nc, nt), np.float32) for k in ("nolte", "trialwise", "literal")}
    for t in range(nt):
        X = F[..., t].astype(np.complex128)                       # (tr, c, f)
        # Nolte: coherency of the trial-averaged cross-spectrum
        S = np.einsum("raf,rbf->abf", X, X.conj()) / ntr
        p = np.real(np.einsum("raf,raf->af", X, X.conj())) / ntr
        C = S / np.sqrt(p[:, None, :] * p[None, :, :])
        M = np.imag(C.conj()[..., :, None] * C[..., None, :]).reshape(nc * nc, nf * nf).astype(np.float32)
        obs = np.imag(C[..., :-1].conj() * C[..., 1:]).sum(-1).reshape(-1).astype(np.float32)
        out["nolte"][..., t] = _z_from_M(M, obs, P_adj).reshape(nc, nc)
        # trialwise (psianalysis.m structure, with the conjugate)
        Z = X / np.abs(X)
        D = Z[..., :-1].conj() * Z[..., 1:]                       # (tr, c, f-1)
        Dr = np.moveaxis(D, 1, -1).reshape(-1, nc)               # (tr*(f-1), c)
        obs2 = (Dr.imag.T @ Dr.real - Dr.real.T @ Dr.imag) / ntr  # Im(d_a conj d_b)
        pp = np.einsum("raf,rbf->abf", Z, Z.conj()) / ntr
        M2 = np.imag(pp.conj()[..., :, None] * pp[..., None, :]).reshape(nc * nc, nf * nf).astype(np.float32)
        out["trialwise"][..., t] = _z_from_M(M2, obs2.reshape(-1).astype(np.float32), P_code).reshape(nc, nc)
        # literal psianalysis.m: no conjugate in the cross-spectrum
        # U = X_a X_b / sqrt(X_a^2 conj(X_b)^2) = exp(i psi), psi = phi_a + phi_b - w,
        # w = principal angle of 2 (phi_a - phi_b), halved (MATLAB's principal square root)
        ph = np.angle(X).astype(np.float32)                       # (tr, c, f)
        dif = 2 * (ph[:, :, None, :] - ph[:, None, :, :])
        w = (np.mod(dif + np.pi, 2 * np.pi) - np.pi) / 2
        psi = ph[:, :, None, :] + ph[:, None, :, :] - w
        del dif, w
        obs3 = np.sin(np.diff(psi, axis=-1)).sum(-1).mean(0)
        pp3 = np.cos(psi).mean(0) + 1j * np.sin(psi).mean(0)
        del psi
        M3 = np.imag(pp3.conj()[..., :, None] * pp3[..., None, :]).reshape(nc * nc, nf * nf).astype(np.float32)
        out["literal"][..., t] = _z_from_M(M3, obs3.reshape(-1).astype(np.float32), P_code).reshape(nc, nc)
    for k in out:
        for c in range(nc):
            out[k][c, c, :] = np.nan
    return out


def psianalysis_literal_pp(Xa: np.ndarray, Xb: np.ndarray) -> np.ndarray:
    """The normalised cross-spectrum of psianalysis.m for one trial, as written: csd = X_a .* X_b
    (no conjugate), divided by sqrt(diag(cs) * diag(cs)') where ' is MATLAB's conjugate
    transpose."""
    return (Xa * Xb) / np.sqrt((Xa * Xa) * np.conj(Xb * Xb))


# ----------------------------------------------------------------------------- per subject

def process_subject(sid: str, n_perm_psi: int = 1000) -> dict:
    """Stream one subject and reduce it to what the claims use. Everything returned is small."""
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    files = stream_subject_files(sid)
    raw = files["derived"]
    d = read_derived(raw)
    csv = None
    if files.get("csv_all"):
        import pandas as pd
        csv = pd.concat([read_trial_csv(b).assign(block=n.split("/")[-1]) for n, b in sorted(files["csv_all"])],
                        ignore_index=True)
        csv = csv.dropna(subset=["trial", "correct", "vhf"]).astype({"trial": int, "correct": int, "vhf": int,
                                                                       "condition": int, "jitter": int})
    res = {"sid": sid, "members": files["members"], "derived_md5": hashlib.md5(raw).hexdigest(),
           "csv": csv, "label": d["label"]}
    for seg in ("pretrial", "encmain", "proc"):
        res[f"{seg}_lengths"] = d[seg]["lengths"]
        res[f"{seg}_trialinfo"] = d[seg]["trialinfo"]
        res[f"{seg}_fsample"] = d[seg]["fsample"]
        res[f"{seg}_time_first"] = d[seg]["time_first"]
    ti = d["encmain"]["trialinfo"]
    # align proc to encmain by trial number (proc is stored in another order)
    order = {int(t): i for i, t in enumerate(d["proc"]["trialinfo"][:, 0])}
    pidx = np.array([order[int(t)] for t in ti[:, 0]])
    pre = d["pretrial"]["data"].astype(np.float64)
    enc = d["encmain"]["data"].astype(np.float64)
    proc = d["proc"]["data"].astype(np.float64)
    proc_al = proc[pidx]
    correct = ti[:, 1] == 1
    hemi = ti[:, 2].astype(int)          # 1 intact, 2 lesioned (descriptor)
    res["n_trials"] = len(ti)
    # fingerprint and Laplacian check
    res["fingerprint"] = float(np.abs(enc[0]).sum())
    A = neighbours(d["label"])
    cc = np.corrcoef(enc[:, :, :].transpose(1, 0, 2).reshape(64, -1))
    res["neighbour_corr"] = float(np.nanmean(cc[A]))
    # ---------------- ERP
    base = lowpass_fir(pre[correct].mean(0)).mean(-1)
    res["erp_base"] = base.astype(np.float32)
    for h in (1, 2):
        sel = correct & (hemi == h)
        res[f"erp_enc_{h}"] = (lowpass_fir(enc[sel].mean(0)) - base[:, None]).astype(np.float32)
        res[f"erp_proc_{h}"] = (lowpass_fir(proc_al[sel].mean(0)) - base[:, None]).astype(np.float32)
        # the code's selection: encmain indices applied to proc in its stored order
        res[f"erp_proc_codeidx_{h}"] = (lowpass_fir(proc[sel].mean(0)) - base[:, None]).astype(np.float32)
    # ---------------- baseline FFT, all trials
    res["fft"] = mtmfft_power(pre, FREQS).mean(0).astype(np.float32)
    # ---------------- TFR power, correct trials
    Fp, mp, tp = mtmconvol(pre[correct], FREQS, 0.01)
    Pp = np.abs(Fp) ** 2                                         # (tr, ch, f, t)
    del Fp
    res["tfr_pre_time"] = tp
    for rd, m in (("pad", np.ones_like(mp)), ("fit", mp)):
        vals = np.where(m[None, None], Pp, np.nan)
        n = np.sum(m, axis=-1) * Pp.shape[0]                     # per freq
        with np.errstate(invalid="ignore", divide="ignore"), warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)   # no baseline value below 6 Hz under "fit"
            res[f"tfr_base_mu_{rd}"] = np.nanmean(vals, axis=(0, 3)).astype(np.float32)
            res[f"tfr_base_sd_{rd}"] = np.nanstd(vals, axis=(0, 3), ddof=1).astype(np.float32)
        res[f"tfr_base_N_{rd}"] = n
    del Pp
    res["n_correct"] = int(correct.sum())
    for seg, x in (("enc", enc), ("proc", proc_al)):
        for h in (1, 2):
            sel = correct & (hemi == h)
            F, m, tt = mtmconvol(x[sel], FREQS, 0.01)
            res[f"tfr_{seg}_{h}"] = (np.abs(F) ** 2).mean(0).astype(np.float32)
            res[f"tfr_{seg}_mask"] = m
            res[f"tfr_{seg}_time"] = tt
            res[f"n_{seg}_{h}"] = int(sel.sum())
            del F
    res["tfr_pre_mask"] = mp
    # ---------------- PSI, correct trials, trial mean subtracted (subtracterp.m)
    for band, fr in BANDS.items():
        x = pre[correct] - pre[correct].mean(0)
        F, m, tt = mtmconvol(x, fr, 0.1)
        res[f"psi_{band}_pre_mask"] = m
        res[f"psi_{band}_pre_time"] = tt
        z = psi_z(F, n_perm_psi, seed=1)
        for k, v in z.items():
            res[f"psi_{band}_pre_{k}"] = v
        for seg, xx in (("enc", enc), ("proc", proc_al)):
            for h in (1, 2):
                sel = correct & (hemi == h)
                x = xx[sel] - xx[sel].mean(0)
                F, m, tt = mtmconvol(x, fr, 0.1)
                res[f"psi_{band}_{seg}_mask"] = m
                res[f"psi_{band}_{seg}_time"] = tt
                z = psi_z(F, n_perm_psi, seed=2 + h)
                for k, v in z.items():
                    res[f"psi_{band}_{seg}_{h}_{k}"] = v
    return canonical(res)


def canonical(res: dict) -> dict:
    """Put every channel axis of a subject's results in the order CANON (the subject's own order
    is kept as 'label_file')."""
    lab = res["label"]
    if "label_file" in res or lab == CANON:
        res.setdefault("label_file", list(lab))
        res["label"] = list(CANON)
        return res
    idx = np.array([lab.index(c) for c in CANON])
    for k, v in list(res.items()):
        if not isinstance(v, np.ndarray) or v.dtype == bool:
            continue
        if k.startswith(("erp_", "tfr_enc_", "tfr_proc_", "tfr_base_mu", "tfr_base_sd")) or k == "fft":
            if v.ndim >= 1 and v.shape[0] == 64:
                res[k] = v[idx]
        elif k.startswith("psi_") and v.ndim == 3 and v.shape[:2] == (64, 64):
            res[k] = v[np.ix_(idx, idx)]
    res["label_file"] = list(lab)
    res["label"] = list(CANON)
    return res


# ----------------------------------------------------------------------------- cluster test

def _label(mask: np.ndarray, edges: np.ndarray):
    """Connected components of mask (nodes, *grid): face connectivity along the grid axes,
    and between nodes joined by `edges` (E, 2) at the same grid point."""
    from scipy import ndimage
    from scipy.sparse import coo_matrix
    from scipy.sparse.csgraph import connected_components
    st = np.zeros((3,) * mask.ndim, bool)
    c = (1,) * mask.ndim
    st[c] = True
    for ax in range(1, mask.ndim):
        for o in (0, 2):
            idx = list(c)
            idx[ax] = o
            st[tuple(idx)] = True
    lab, n = ndimage.label(mask, structure=st)
    if n == 0:
        return lab, 0
    if len(edges):
        L1 = lab[edges[:, 0]].reshape(len(edges), -1)
        L2 = lab[edges[:, 1]].reshape(len(edges), -1)
        both = (L1 > 0) & (L2 > 0)
        a, b = L1[both], L2[both]
        if a.size:
            g = coo_matrix((np.ones(a.size), (a, b)), shape=(n + 1, n + 1))
            _, comp = connected_components(g, directed=False)
            remap = comp
            # component ids: relabel to 1..k keeping 0 as background
            u, inv = np.unique(remap[1:], return_inverse=True)
            newid = np.concatenate([[0], inv + 1])
            lab = newid[lab]
            n = len(u)
    return lab, n


def cluster_test(x1: np.ndarray, x2: np.ndarray, adjacency, n_perm: int = 1000,
                 alpha: float = 0.05, minnbchan: int = 2, seed: int = 0, node_groups=None) -> dict:
    """FieldTrip ft_*statistics, montecarlo with cluster correction as the paper's scripts
    set it: ft_statfun_indepsamplesT (group 1 minus group 2), clusteralpha 0.05 two-tailed,
    maxsum, 1000 shuffles, correcttail 'prob' (p doubled), minnbchan. x1: (n1, nodes, *grid),
    x2: (n2, nodes, *grid). adjacency: (nodes, nodes) boolean or None (no spatial
    clustering), dense or scipy.sparse. node_groups: optional integer group of each node; each
    group is then a separate test with its own maximum (psi_stat_group.m tests each seed channel
    on its own). NaN points are left out of every cluster."""
    from scipy import sparse
    from scipy import stats
    n1, n2 = len(x1), len(x2)
    X = np.concatenate([x1, x2]).astype(np.float64)
    shape = X.shape[1:]
    Xf = X.reshape(len(X), -1)
    valid = np.all(np.isfinite(Xf), axis=0)
    Xf = np.where(valid, Xf, 0.0)
    df = n1 + n2 - 2
    crit = stats.t.ppf(1 - alpha / 2, df)
    if adjacency is not None:
        A = sparse.csr_matrix(adjacency, dtype=np.float32)
        tri = sparse.triu(A, 1).tocoo()
        edges = np.stack([tri.row, tri.col], 1)
    else:
        edges = np.zeros((0, 2), int)
        A = None
    S1, S2 = Xf, Xf ** 2

    def tstat(g):            # g: (k, n) boolean group-1 membership
        g = g.astype(np.float64)
        s1 = g @ S1
        q1 = g @ S2
        s2 = S1.sum(0) - s1
        q2 = S2.sum(0) - q1
        m1, m2 = s1 / n1, s2 / n2
        v1 = (q1 - n1 * m1 ** 2) / (n1 - 1)
        v2 = (q2 - n2 * m2 ** 2) / (n2 - 1)
        sp = ((n1 - 1) * v1 + (n2 - 1) * v2) / df
        with np.errstate(invalid="ignore", divide="ignore"):
            t = (m1 - m2) / np.sqrt(sp * (1 / n1 + 1 / n2))
        t[:, ~valid] = 0.0
        return np.nan_to_num(t)

    def clusters(t):
        t = t.reshape(shape)
        res = []
        for sign in (1, -1):
            m = (sign * t) > crit
            if A is not None and minnbchan > 0:
                cnt = (A @ m.reshape(m.shape[0], -1).astype(np.float32)).reshape(m.shape)
                m = m & (cnt >= minnbchan)
            lab, n = _label(m, edges)
            if n:
                sums = np.bincount(lab.ravel(), weights=t.ravel(), minlength=n + 1)[1:]
                if groups is not None:
                    first = np.zeros(n + 1, int)
                    first[lab.ravel()] = node_of.ravel()
                    grp = groups[first[1:]]
                else:
                    grp = np.zeros(n, int)
            else:
                sums, grp = np.zeros(0), np.zeros(0, int)
            res.append((lab, sums, grp))
        return res

    groups = None if node_groups is None else np.asarray(node_groups)
    node_of = np.broadcast_to(np.arange(shape[0]).reshape((-1,) + (1,) * (len(shape) - 1)), shape)
    ng = 1 if groups is None else int(groups.max()) + 1
    g0 = np.zeros((1, n1 + n2), bool)
    g0[0, :n1] = True
    t_obs = tstat(g0)[0]
    (labp, sp_, gp_), (labn, sn_, gn_) = clusters(t_obs)
    rng = np.random.default_rng(seed)
    maxp = np.zeros((n_perm, ng))
    maxn = np.zeros((n_perm, ng))
    chunk = 50
    for s in range(0, n_perm, chunk):
        k = min(chunk, n_perm - s)
        G = np.zeros((k, n1 + n2), bool)
        for i in range(k):
            G[i, rng.permutation(n1 + n2)[:n1]] = True
        T = tstat(G)
        for i in range(k):
            (_, a, ga), (_, b, gb) = clusters(T[i])
            if a.size:
                np.maximum.at(maxp[s + i], ga, a)
            if b.size:
                np.minimum.at(maxn[s + i], gb, b)
    out = {"t": t_obs.reshape(shape), "crit": crit, "clusters": [], "valid": valid.reshape(shape)}
    for sign, lab, sums, grp, null in ((1, labp, sp_, gp_, maxp), (-1, labn, sn_, gn_, maxn)):
        for i, sm in enumerate(sums):
            nl = null[:, grp[i]]
            p = np.mean(nl >= sm) if sign > 0 else np.mean(nl <= sm)
            out["clusters"].append({"sign": sign, "stat": float(sm), "p": float(min(1.0, 2 * p)),
                                    "group": int(grp[i]), "mask": lab == i + 1})
    out["clusters"].sort(key=lambda c: c["p"])
    return out


def pair_adjacency(adj: np.ndarray, mode: str):
    """Adjacency over ordered channel pairs (a, b), a != b, for the PSI group test.
    mode 'pairs': (a, b) ~ (a', b') when a and a' are equal or neighbours and so are b and b'.
    mode 'seed': (a, b) ~ (a, b') when b and b' are neighbours (psi_stat_group.m, per seed a).
    Returns (pairs (P, 2), adjacency (P, P) boolean)."""
    nc = len(adj)
    pairs = np.array([(a, b) for a in range(nc) for b in range(nc) if a != b])
    idx = -np.ones((nc, nc), int)
    idx[pairs[:, 0], pairs[:, 1]] = np.arange(len(pairs))
    near = adj | np.eye(nc, dtype=bool)
    P = np.zeros((len(pairs), len(pairs)), bool)
    for k, (a, b) in enumerate(pairs):
        if mode == "pairs":
            aa = np.flatnonzero(near[a])
            bb = np.flatnonzero(near[b])
            j = idx[np.ix_(aa, bb)].ravel()
        else:
            j = idx[a, np.flatnonzero(adj[b])]
        j = j[(j >= 0) & (j != k)]
        P[k, j] = True
    P = P | P.T
    return pairs, P


def _safe(sid):
    try:
        return process_subject(sid)
    except Exception as e:          # reported, not hidden: the notebook prints every failure
        return {"sid": sid, "error": repr(e)}


def process_all(subjects=SUBJECTS, workers: int = 4, done=None) -> dict:
    """process_subject for every subject, a few at a time (each worker holds one subject).
    A subject that fails is returned with its error. `done` is called with each result."""
    from concurrent.futures import ProcessPoolExecutor, as_completed
    for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
        os.environ[v] = "1"
    out = {}
    with ProcessPoolExecutor(workers) as ex:
        futs = {ex.submit(_safe, s): s for s in subjects}
        for f in as_completed(futs):
            r = f.result()
            out[futs[f]] = r
            if done:
                done(r)
    return {s: out[s] for s in subjects}


# ----------------------------------------------------------------------------- derived measures

def power_z(r: dict, seg: str, h: int, reading: str = "pad", r_mode: str = "hemifield") -> np.ndarray:
    """Task power Z scored on the pretrial baseline (zbaseline.m), in its exact expectation:
    (mean power over the r trials - baseline mean) / (baseline sd / sqrt(r) * sqrt((N - r) /
    (N - 1))), N pooled baseline values (correct trials by time points). r_mode 'hemifield':
    r = trials of the data being scored (zbaseline.m); 'all': r = all correct trials of the
    subject (the Methods' "number of trials in that subject's dataset"). reading 'fit' sets to
    NaN every point FieldTrip leaves NaN (window outside the segment, here or in the baseline).
    Returns (64, 40, ntime)."""
    mu = r[f"tfr_base_mu_{reading}"].astype(np.float64)
    sd = r[f"tfr_base_sd_{reading}"].astype(np.float64)
    N = r[f"tfr_base_N_{reading}"].astype(np.float64)[None, :]
    n = r[f"n_{seg}_{h}"] if r_mode == "hemifield" else r["n_correct"]
    with np.errstate(invalid="ignore", divide="ignore"):
        s = sd / np.sqrt(n) * np.sqrt((N - n) / (N - 1))
        z = (r[f"tfr_{seg}_{h}"] - mu[..., None]) / s[..., None]
    if reading == "fit":
        z = np.where(r[f"tfr_{seg}_mask"][None], z, np.nan)
    return z


def hem_index(x: np.ndarray, labels: list[str], axis: int = 1) -> np.ndarray:
    """Lesioned minus intact homolog (left minus right after the swap), 27 channels in the
    order of *_stat_group_hem.m."""
    li = [labels.index(c) for c in LEFT]
    ri = [labels.index(c) for c in RIGHT]
    return np.take(x, li, axis=axis) - np.take(x, ri, axis=axis)


def psi_bc(r: dict, band: str, seg: str, h: int, reading: str, window: str = "pad") -> np.ndarray:
    """Baseline-corrected PSI Z (64, 64, ntime): Z minus its temporal mean over the pretrial
    baseline (psi_compute.m). window 'fit': points whose 3/f windows do not all fit inside the
    segment are NaN, and the baseline mean is over the baseline points that fit (FieldTrip)."""
    pre = r[f"psi_{band}_pre_{reading}"].astype(np.float64)
    z = r[f"psi_{band}_{seg}_{h}_{reading}"].astype(np.float64)
    if window == "fit":
        pre = np.where(r[f"psi_{band}_pre_mask"].all(0), pre, np.nan)
        z = np.where(r[f"psi_{band}_{seg}_mask"].all(0), z, np.nan)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        base = np.nanmean(pre, axis=-1)
    return z - base[..., None]


def psi_raw(r: dict, band: str, seg: str, h: int | None, reading: str) -> np.ndarray:
    key = f"psi_{band}_pre_{reading}" if seg == "pre" else f"psi_{band}_{seg}_{h}_{reading}"
    return r[key].astype(np.float64)


def degree(z: np.ndarray, mode: str) -> np.ndarray:
    """Network degree per channel from PSI Z (64, 64, nt), before baseline correction.
    'ft_count': ft_networkanalysis 'degrees' on Z > 1.96, directed: in-degree plus out-degree
    (psi_compute.m), i.e. connections with |Z| > 1.96 in either direction. Readings of the
    claims file: 'out_signed' (a) sum of Z over connections leaving the channel with |Z| >
    1.96; 'out_count' (b) their count; 'abs_both' (c) sum of |Z| over true connections in
    either direction."""
    z = np.nan_to_num(z)
    if mode == "ft_count":
        g = (z > 1.96).astype(float)
        return g.sum(0) + g.sum(1)
    true = np.abs(z) > 1.96
    if mode == "out_signed":
        return np.where(true, z, 0).sum(1)
    if mode == "out_count":
        return true.sum(1).astype(float)
    if mode == "abs_both":
        return np.where(true, np.abs(z), 0).sum(1) + np.where(true, np.abs(z), 0).sum(0)
    raise ValueError(mode)


# ----------------------------------------------------------------------------- behaviour

def ancova_rm(Y: np.ndarray, B: np.ndarray, names: list[str]) -> list[dict]:
    """Repeated-measures ANCOVA as SPSS GLM computes it (Type III, sphericity assumed).
    Y: (n, 2, 3) accuracy by visual hemifield (lesion, intact) and condition. B: (n, k)
    between-subject terms without the intercept (factors effect coded +-1, covariates raw).
    Between-subject terms are tested on the subject mean; within-subject effects on orthonormal
    contrasts of the within cells, regressed on the same terms (their intercept is the
    within-subject main effect, each slope its interaction with that term)."""
    n = len(Y)
    X = np.column_stack([np.ones(n), B])
    XtXi = np.linalg.pinv(X.T @ X)
    dfe = n - np.linalg.matrix_rank(X)
    c_v = np.array([1, -1]) / np.sqrt(2)
    c_c = np.array([[1, -1, 0], [1, 1, -2]], float)
    c_c = c_c / np.linalg.norm(c_c, axis=1, keepdims=True)
    blocks = {
        "": [Y.mean(axis=(1, 2)) * np.sqrt(6)],
        "Visual Hemifield": [np.einsum("v,nvc->n", c_v, Y) / np.sqrt(3)],
        "Condition": [np.einsum("kc,nvc->nk", c_c, Y)[:, k] / np.sqrt(2) for k in range(2)],
        "Visual Hemifield x Condition": [np.einsum("v,kc,nvc->nk", c_v, c_c, Y)[:, k] for k in range(2)],
    }
    out = []
    for within, ys in blocks.items():
        ss_h = np.zeros(X.shape[1])
        sse = 0.0
        for y in ys:
            beta = XtXi @ X.T @ y
            res = y - X @ beta
            sse += res @ res
            ss_h += beta ** 2 / np.diag(XtXi)
        q = len(ys)
        for j, nm in enumerate(["(intercept)"] + names):
            if within == "" and j == 0:
                continue
            label = within if j == 0 else (nm if within == "" else f"{within} x {nm}")
            F = (ss_h[j] / q) / (sse / (q * dfe))
            from scipy import stats
            out.append({"term": label, "F": F, "df1": q, "df2": q * dfe,
                        "p": float(stats.f.sf(F, q, q * dfe)),
                        "partial_eta2": ss_h[j] / (ss_h[j] + sse)})
    return out


def lmm_wald(df, formula: str, group: str = "subject") -> dict:
    """Linear mixed model with a random intercept per subject (statsmodels MixedLM, REML);
    F = (beta / se)^2 per fixed effect, p from F(1, n - p) (fitglme's residual degrees of
    freedom)."""
    import statsmodels.formula.api as smf
    from scipy import stats
    m = smf.mixedlm(formula, df, groups=df[group]).fit(reml=True)
    fe = m.fe_params
    se = m.bse_fe
    dfe = len(df) - len(fe)
    return {k: {"beta": float(fe[k]), "F": float((fe[k] / se[k]) ** 2), "df2": dfe,
                "p": float(stats.f.sf((fe[k] / se[k]) ** 2, 1, dfe))} for k in fe.index if k != "Intercept"}


def glmm_binomial(k: np.ndarray, n: np.ndarray, X: np.ndarray, groups: np.ndarray, names: list[str],
                  nq: int = 30) -> dict:
    """Logit mixed model with a random intercept per subject, fitted by maximum likelihood
    with Gauss-Hermite quadrature; Wald F = (beta / se)^2, p from F(1, rows - p)."""
    from scipy import optimize, special, stats
    gh_x, gh_w = np.polynomial.hermite.hermgauss(nq)
    ug = np.unique(groups)
    gi = np.searchsorted(ug, groups)
    p = X.shape[1]
    lc = special.gammaln(n + 1) - special.gammaln(k + 1) - special.gammaln(n - k + 1)

    def nll(th):
        b, ls = th[:p], th[p]
        eta = X @ b
        u = np.sqrt(2) * np.exp(ls) * gh_x[None, :]
        e = eta[:, None] + u
        ll = k[:, None] * e - n[:, None] * np.logaddexp(0, e) + lc[:, None]
        G = np.zeros((len(ug), nq))
        np.add.at(G, gi, ll)
        m = G.max(1, keepdims=True)
        return -np.sum(m[:, 0] + np.log((np.exp(G - m) * gh_w[None]).sum(1) / np.sqrt(np.pi)))

    th0 = np.zeros(p + 1)
    th0[0] = special.logit(np.clip(k.sum() / n.sum(), 0.01, 0.99))
    th0[p] = np.log(0.5)
    opt = optimize.minimize(nll, th0, method="BFGS")
    th = opt.x
    h = 1e-4
    H = np.zeros((p + 1, p + 1))
    for i in range(p + 1):
        for j in range(i, p + 1):
            ei = np.eye(p + 1)[i] * h
            ej = np.eye(p + 1)[j] * h
            H[i, j] = H[j, i] = (nll(th + ei + ej) - nll(th + ei - ej) - nll(th - ei + ej) + nll(th - ei - ej)) / (4 * h * h)
    cov = np.linalg.inv(H)
    dfe = len(k) - p
    out = {}
    for i, nm in enumerate(names):
        if nm == "Intercept":
            continue
        F = th[i] ** 2 / cov[i, i]
        out[nm] = {"beta": float(th[i]), "F": float(F), "df2": dfe, "p": float(stats.f.sf(F, 1, dfe))}
    out["_converged"] = bool(opt.success)
    return out


def link_trials(csv, ti: np.ndarray) -> np.ndarray:
    """Row of the trial table (csv, all blocks) for each derived trial: same trial number and
    response time; failing that, the one row with the same response time, condition, jitter
    and accuracy. -1 where no single row matches. Two-block subjects number their trials in
    ways that overlap between blocks, so the trial number alone does not identify a row."""
    out = -np.ones(len(ti), int)
    tr = csv["trial"].to_numpy()
    rt = csv["rt"].to_numpy()
    key = np.stack([csv["rt"], csv["condition"], csv["jitter"], csv["correct"]], 1)
    for i, row in enumerate(ti):
        j = np.flatnonzero((tr == int(row[0])) & (rt == row[6]))
        if len(j) != 1:
            j = np.flatnonzero((key == row[[6, 4, 5, 1]]).all(1))
        if len(j) == 1:
            out[i] = j[0]
    return out
