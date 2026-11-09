"""Loading and waveform measures for OpenNeuro ds002778 (UC San Diego resting EEG in Parkinson's disease).

Jackson, Cole, Voytek & Swann (2019), eNeuro 6(3) ENEURO.0151-19.2019, doi:10.1523/ENEURO.0151-19.2019.

The dataset is BIDS: 15 patients recorded off (`ses-off`) and on (`ses-on`) medication and 16
controls (`ses-hc`), one BioSemi BDF file per session (32 scalp electrodes, 8 external EXG
channels, a Status channel, 512 Hz). Files are read from the pinned snapshot 1.0.5: the file list
comes from OpenNeuro's GraphQL API, each file is opened at its `urls[0]`, which is pinned to that
snapshot, and read into memory. Nothing is written to disk.

Where the parameters come from. "Claims" is the claims file `claims/openneuro-ds002778/`, whose
opening comment cites the paper's Methods and its code (SwannLab/Jackson_2019 at commit a7c89f5);
"Methods" is the paper's Materials and Methods.

- Preprocessing (`preprocess`): each electrode's mean removed, common average over the 32 scalp
  electrodes, high-pass at 0.5 Hz with a two-way FIR filter (Methods, Data preprocessing: "each
  electrode's mean was removed and then a common average reference was applied ... high pass
  filtered at 0.5 Hz ... using a two-way FIR filter, eegfilt"). The filter is eegfilt's: firls
  of order 3 * fix(512 / 0.5) = 3072 with a 15% transition band (claims, opening comment, a
  standard choice). It is applied forwards and backwards with FFT convolution, with the odd
  extension and steady-state start of MATLAB's and scipy's filtfilt (a standard choice that
  only changes rounding). No electrode is excluded and no sample rejected: the dataset holds no
  bad-channel marks (every channels.tsv says "good") and no artifact marks (claims, readings (b)
  for noisy electrodes and for artifact rejection).
- Peaks and troughs (`find_extrema`): band-pass with scipy firwin applied with filtfilt; the
  extremum of the raw signal between consecutive zero crossings of the filtered one; extrema
  within 100 samples of either end dropped (claims; code shape.findpt and utils.measure_shape,
  boundaryS=100). Filter length for 13 to 30 Hz: floor(3 * 512 / 13) = 118 taps (code; the
  Methods' 231 ms is the same 118 samples). For 8 to 12 Hz: 192 taps (3 cycles of 8 Hz, the
  code's rule) and 118 (the Methods' 231 ms), the two readings of the claims file.
- Sharpness (`shape_measures`): |mean(x[e] - x[e-3], x[e] - x[e+3])| (claims; code
  shape.ex_sharp, widthS=3). Steepness: largest first difference from a trough to the next peak
  (rise) and largest negative first difference from a peak to the next trough (decay), taking
  len(troughs) - 1 rises and len(peaks) - 1 decays as the code's rd_steep does. Sharpness ratio
  and steepness ratio are |log10| of the ratio of means; peak-to-trough ratio and rise-to-fall
  ratio are the signed log10 (claims; code utils.measure_shape and Figure_4).
- PAC (`pac_ozkurt`): firwin band-pass with filtfilt, Hilbert phase of the low band and
  amplitude of 50 to 150 Hz, |sum(a exp(i phi))| / (sqrt(N) sqrt(sum a^2)) (claims; code
  pac.ozkurt). Filter lengths: 118 and 123 samples (Methods, 231 ms and 240 ms at 512 Hz) and
  231 and 240 taps (code utils.measure_pac), the two readings of the claims file. For 8 to 12 Hz
  phase: 192, 231 and 118 taps (claims, readings a to c). The filtered edges are kept; a variant
  at C3 and C4 drops them, as pacpy's firf does with rmvedge.
- Bipolar signals C3 - CP1 and C4 - CP2 (claims, bipolar-off-on).
- Current source density (`csd`): spherical spline surface Laplacian with m = 3 (Methods: "CSDtoolbox
  in MATLAB, spline flexibility = 3"), lambda 1e-5 and 50 Legendre terms (the CSD toolbox's
  defaults, a standard choice per the claims file), computed with MNE on the BioSemi 32
  template positions (a standard choice: the dataset holds no digitized positions). Variants
  with m = 4 and lambda 1e-4 and 1e-6 show how far the CSD result rests on these choices.
- Welch spectra (`welch_psd`): Hamming window of 256 samples, overlap 128, nFFT 450 (Methods,
  Data analysis, pwelch), no detrending, as pwelch.
- Statistics: Wilcoxon signed rank with the normal approximation and no continuity correction
  (claims: the code's printed p-values match it), the exact test as a variant; rank sum z
  (scipy ranksums); Cohen's d with the code's effectsize formula; Benjamini-Hochberg FDR.
"""

from __future__ import annotations

import io
import json
from functools import lru_cache

import mne
import numpy as np
import pandas as pd
import requests
from scipy import signal, stats
from scipy.signal._arraytools import odd_ext

DATASET_ID = "ds002778"
SNAPSHOT = "1.0.5"
SNAPSHOT_DOI = "10.18112/openneuro.ds002778.v1.0.5"
GRAPHQL = "https://openneuro.org/crn/graphql"
FS = 512.0

SCALP = ['Fp1', 'AF3', 'F7', 'F3', 'FC1', 'FC5', 'T7', 'C3', 'CP1', 'CP5', 'P7', 'P3', 'Pz', 'PO3',
         'O1', 'Oz', 'O2', 'PO4', 'P4', 'P8', 'CP6', 'CP2', 'C4', 'T8', 'FC6', 'FC2', 'F4', 'F8',
         'AF4', 'Fp2', 'Fz', 'Cz']
BETA = (13.0, 30.0)
ALPHA = (8.0, 12.0)
GAMMA = (50.0, 150.0)
BOUNDARY = 100        # code utils.measure_shape, boundaryS
WIDTH = 3             # code, widthS: samples either side of an extremum
SHAPE_TAPS = {"beta": {"118": 118}, "alpha": {"192": 192, "118": 118}}
# PAC filter readings: name -> (phase taps, amplitude taps)
PAC_BETA = {"methods": (118, 123), "code": (231, 240)}
PAC_ALPHA = {"a192": (192, 123), "b231": (231, 240), "c118": (118, 123)}
PAC_ALPHA_GAMMA = {"a192": "methods", "b231": "code", "c118": "methods"}
SIX = ['C3', 'C4', 'F7', 'F8', 'T7', 'T8']
# CSD readings: name -> (spline flexibility m, lambda); "m3" is the main one, the others variants
CSD_VARIANTS = {"m3": (3, 1e-5), "m4": (4, 1e-5), "m3 lambda 1e-4": (3, 1e-4), "m3 lambda 1e-6": (3, 1e-6)}


# ----------------------------------------------------------------------------- archive

@lru_cache(maxsize=1)
def listing() -> pd.DataFrame:
    """Every file of the pinned snapshot, with its size, checksum id and pinned URL."""
    query = ('{ snapshot(datasetId: "%s", tag: "%s") { files(recursive: true) '
             '{ filename size annexed id urls } } }' % (DATASET_ID, SNAPSHOT))
    r = requests.post(GRAPHQL, json={"query": query}, timeout=120)
    r.raise_for_status()
    body = r.json()
    if "errors" in body:
        raise RuntimeError(body["errors"])
    files = body["data"]["snapshot"]["files"]
    df = pd.DataFrame([{"filename": f["filename"], "size": f["size"], "annexed": f["annexed"],
                        "id": f["id"], "url": f["urls"][0]} for f in files])
    return df.set_index("filename")


def url(name: str) -> str:
    return listing().loc[name, "url"]


def fetch(name: str) -> bytes:
    r = requests.get(url(name), timeout=300)
    r.raise_for_status()
    return r.content


def read_tsv(name: str) -> pd.DataFrame:
    return pd.read_csv(io.BytesIO(fetch(name)), sep="\t")


def read_json(name: str):
    return json.loads(fetch(name).decode())


def bdf_name(sub: str, ses: str) -> str:
    return f"sub-{sub}/ses-{ses}/eeg/sub-{sub}_ses-{ses}_task-rest_eeg.bdf"


def read_bdf(sub: str, ses: str) -> mne.io.BaseRaw:
    """The session's BDF, read whole into memory from the pinned URL."""
    return mne.io.read_raw_bdf(io.BytesIO(fetch(bdf_name(sub, ses))), preload=True,
                               verbose="error")


def sessions() -> pd.DataFrame:
    """One row per recording: subject, session, group."""
    names = [n for n in listing().index if n.endswith("_eeg.bdf")]
    rows = []
    for n in names:
        sub, ses = n.split("/")[0][4:], n.split("/")[1][4:]
        rows.append({"sub": sub, "ses": ses, "group": {"hc": "control", "off": "off", "on": "on"}[ses]})
    return pd.DataFrame(rows).sort_values(["group", "sub"]).reset_index(drop=True)


# ----------------------------------------------------------------------------- filters

def _filtfilt_fft(x: np.ndarray, b: np.ndarray) -> np.ndarray:
    """filtfilt(b, 1, x) along the last axis, by FFT convolution.

    Same padding as scipy.signal.filtfilt (odd extension of 3 * len(b) samples) and the same
    steady-state start (the input held at its first value before the start), so the result
    equals scipy's to rounding error.
    """
    n = len(b)
    pad = 3 * n
    ext = odd_ext(x, pad, axis=-1)

    def causal(y):
        head = np.repeat(y[..., :1], n, axis=-1)
        z = signal.fftconvolve(np.concatenate([head, y], axis=-1), b.reshape((1,) * (y.ndim - 1) + (-1,)),
                               mode="full", axes=-1)
        return z[..., n:n + y.shape[-1]]

    y = causal(ext)
    y = causal(y[..., ::-1])[..., ::-1]
    return y[..., pad:-pad]


@lru_cache(maxsize=None)
def eegfilt_highpass_taps(locutoff: float = 0.5, fs: float = FS) -> np.ndarray:
    """eegfilt's high-pass: firls of order 3 * fix(fs / locutoff), transition 15% below locutoff."""
    order = 3 * int(fs / locutoff)
    nyq = fs / 2
    return signal.firls(order + 1, [0, locutoff * 0.85 / nyq, locutoff / nyq, 1], [0, 0, 1, 1])


@lru_cache(maxsize=None)
def bandpass_taps(f_range: tuple, ntaps: int, fs: float = FS) -> np.ndarray:
    """scipy firwin band-pass, as the paper's code (pacpy firf)."""
    return signal.firwin(int(ntaps), np.array(f_range) / (fs / 2), pass_zero=False)


def bandpass(x: np.ndarray, f_range: tuple, ntaps: int) -> np.ndarray:
    return signal.filtfilt(bandpass_taps(tuple(f_range), int(ntaps)), [1.0], x, axis=-1)


# ----------------------------------------------------------------------------- preprocessing

def preprocess(data_uv: np.ndarray) -> np.ndarray:
    """Mean removal, common average over the rows, 0.5 Hz two-way FIR high-pass."""
    x = data_uv - data_uv.mean(axis=1, keepdims=True)
    x = x - x.mean(axis=0, keepdims=True)
    return _filtfilt_fft(x, eegfilt_highpass_taps())


def csd(x: np.ndarray, stiffness: float = 3, lambda2: float = 1e-5) -> np.ndarray:
    """Spherical spline CSD (m = 3, lambda 1e-5, 50 Legendre terms) on the 32 scalp rows.

    stiffness and lambda2 are varied in CSD_VARIANTS to show how much the CSD result rests on them.
    """
    info = mne.create_info(SCALP, FS, "eeg")
    raw = mne.io.RawArray(x * 1e-6, info, verbose="error")
    raw.set_montage(mne.channels.make_standard_montage("biosemi32"), verbose="error")
    out = mne.preprocessing.compute_current_source_density(
        raw, stiffness=stiffness, lambda2=lambda2, n_legendre_terms=50, verbose="error")
    return out.get_data()


# ----------------------------------------------------------------------------- measures

def find_extrema(x: np.ndarray, f_range: tuple, ntaps: int, boundary: int = BOUNDARY):
    """Peaks and troughs of x between zero crossings of its band-passed copy (code findpt).

    A peak is the first maximum of x from a rising zero crossing to the next falling one, a
    trough the first minimum from a falling crossing to the next rising one.
    """
    xn = bandpass(x, f_range, ntaps)
    pos, neg = xn > 0, xn < 0
    falls = (pos[:-1] & ~pos[1:]).nonzero()[0]
    rises = (neg[:-1] & ~neg[1:]).nonzero()[0]
    cross = np.concatenate([rises, falls])
    is_rise = np.concatenate([np.ones(len(rises), bool), np.zeros(len(falls), bool)])
    order = np.argsort(cross, kind="stable")
    cross, is_rise = cross[order], is_rise[order]
    lens = np.diff(cross)
    sign = np.where(is_rise[:-1], 1.0, -1.0)
    seg = x[cross[0]:cross[-1]] * np.repeat(sign, lens)
    best = np.maximum.reduceat(seg, cross[:-1] - cross[0])
    seg_id = np.repeat(np.arange(len(lens)), lens)
    hit = np.nonzero(seg == best[seg_id])[0]
    ids, first = np.unique(seg_id[hit], return_index=True)
    ext = np.full(len(lens), -1)
    ext[ids] = hit[first] + cross[0]
    peak_seg = is_rise[:-1] & ~is_rise[1:]
    trough_seg = ~is_rise[:-1] & is_rise[1:]
    peaks, troughs = ext[peak_seg], ext[trough_seg]
    n = len(x)
    inside = lambda e: e[(e >= boundary) & (e <= n - boundary)]
    return inside(peaks), inside(troughs)


def shape_measures(x: np.ndarray, f_range: tuple, ntaps: int) -> dict:
    """Sharpness ratio, steepness ratio, peak-to-trough and rise-to-fall ratios of one trace."""
    P, T = find_extrema(x, f_range, ntaps)
    w = WIDTH
    psharp = np.abs(((x[P] - x[P - w]) + (x[P] - x[P + w])) / 2)
    tsharp = np.abs(((x[T] - x[T - w]) + (x[T] - x[T + w])) / 2)
    # rises (trough to next peak) and decays (peak to next trough), as code rd_steep
    E = np.sort(np.concatenate([P, T]))
    is_p = np.isin(E, P)
    d = np.diff(x)
    seg_max = np.maximum.reduceat(d, E[:-1])
    seg_min = np.minimum.reduceat(d, E[:-1])
    rise = seg_max[~is_p[:-1] & is_p[1:]][:len(T) - 1]
    decay = -seg_min[is_p[:-1] & ~is_p[1:]][:len(P) - 1]
    mp, mt, mr, md = psharp.mean(), tsharp.mean(), rise.mean(), decay.mean()
    return {"ShR": abs(np.log10(mp / mt)), "StR": abs(np.log10(mr / md)),
            "PTR": np.log10(mp / mt), "RDR": np.log10(mr / md),
            "n_peaks": len(P), "n_troughs": len(T)}


def pac_ozkurt(x: np.ndarray, f_lo: tuple, n_lo: int, f_hi: tuple = GAMMA, n_hi: int = 123,
               trim: bool = False) -> float:
    """Normalized modulation index (Ozkurt and Schnitzler 2011), as code pac.ozkurt.

    trim drops max(n_lo, n_hi) filtered samples at each end before the Hilbert transform, as
    pacpy's firf does with rmvedge (a variant; the main analysis keeps them).
    """
    lo, hi = bandpass(x, f_lo, n_lo), bandpass(x, f_hi, n_hi)
    if trim:
        k = max(int(n_lo), int(n_hi))
        lo, hi = lo[k:-k], hi[k:-k]
    pha = np.angle(signal.hilbert(lo))
    amp = np.abs(signal.hilbert(hi))
    return float(np.abs(np.sum(amp * np.exp(1j * pha))) / (np.sqrt(len(pha)) * np.sqrt(np.sum(amp ** 2))))


def welch_psd(x: np.ndarray):
    """pwelch(x, 256, 128, 450, 512): Hamming window, no detrending."""
    return signal.welch(x, fs=FS, window="hamming", nperseg=256, noverlap=128, nfft=450,
                        detrend=False, axis=-1)


# ----------------------------------------------------------------------------- one recording

def analyse(sub: str, ses: str) -> dict:
    """All measures of one recording: per electrode, bipolar pairs and CSD at C3 and C4."""
    raw = read_bdf(sub, ses)
    names = raw.ch_names
    data = raw.get_data(picks=SCALP) * 1e6          # volts to microvolts
    exg = raw.get_data(picks=[c for c in names if c.startswith("EXG")]) * 1e6
    status = raw.get_data(picks=["Status"])[0] if "Status" in names else None
    info = {"sub": sub, "ses": ses, "n_times": raw.n_times, "sfreq": raw.info["sfreq"],
            "channels": names,
            "raw_mean_abs_uv": float(np.abs(data.mean(axis=1)).mean()),
            "raw_sum_over_channels_uv": float(np.abs(data.sum(axis=0)).max()),
            "raw_sd_uv": dict(zip(SCALP, data.std(axis=1))),
            "exg_sd_uv": exg.std(axis=1).tolist(),
            "raw_c3_head": data[SCALP.index("C3"), :2048].copy()}
    if status is not None:
        st = status.astype(np.int64)
        change = np.nonzero(np.diff(st))[0] + 1
        info["status_changes"] = [(int(i), int(st[i])) for i in change[:10]]
        info["status_first"] = int(st[0])
    x = preprocess(data)
    info["pre_sd_uv"] = dict(zip(SCALP, x.std(axis=1)))

    rows = []
    for i, ch in enumerate(SCALP):
        for band, taps in SHAPE_TAPS.items():
            f = BETA if band == "beta" else ALPHA
            for tname, nt in taps.items():
                m = shape_measures(x[i], f, nt)
                rows.append({"sub": sub, "ses": ses, "signal": ch, "band": band, "taps": tname, **m})
    shape = pd.DataFrame(rows)

    prow = []
    for i, ch in enumerate(SCALP):
        for rname, (nlo, nhi) in PAC_BETA.items():
            prow.append({"sub": sub, "ses": ses, "signal": ch, "band": "beta", "reading": rname,
                         "PAC": pac_ozkurt(x[i], BETA, nlo, GAMMA, nhi)})
        if ch in SIX:
            for rname, (nlo, nhi) in PAC_ALPHA.items():
                prow.append({"sub": sub, "ses": ses, "signal": ch, "band": "alpha", "reading": rname,
                             "PAC": pac_ozkurt(x[i], ALPHA, nlo, GAMMA, nhi)})

    # bipolar montage
    bip = {"C3-CP1": x[SCALP.index("C3")] - x[SCALP.index("CP1")],
           "C4-CP2": x[SCALP.index("C4")] - x[SCALP.index("CP2")]}
    brow = []
    for name, y in bip.items():
        m = shape_measures(y, BETA, 118)
        brow.append({"sub": sub, "ses": ses, "signal": name, "band": "beta", "taps": "118", **m})
        for rname, (nlo, nhi) in PAC_BETA.items():
            prow.append({"sub": sub, "ses": ses, "signal": name, "band": "beta", "reading": rname,
                         "PAC": pac_ozkurt(y, BETA, nlo, GAMMA, nhi)})
    shape = pd.concat([shape, pd.DataFrame(brow)], ignore_index=True)

    # beta PAC at C3 and C4 with the filter edges dropped (variant)
    for ch in ("C3", "C4"):
        for rname, (nlo, nhi) in PAC_BETA.items():
            prow.append({"sub": sub, "ses": ses, "signal": ch, "band": "beta", "reading": rname + " trimmed",
                         "PAC": pac_ozkurt(x[SCALP.index(ch)], BETA, nlo, GAMMA, nhi, trim=True)})

    # current source density: main ("m3", signal "CSD C3") and variants ("CSD m4 C3", ...)
    csd_psd = {}
    for vname, (m, lam) in CSD_VARIANTS.items():
        xc = csd(x, m, lam)
        tag = "CSD " if vname == "m3" else f"CSD {vname} "
        for ch in ("C3", "C4"):
            for rname, (nlo, nhi) in PAC_BETA.items():
                prow.append({"sub": sub, "ses": ses, "signal": tag + ch, "band": "beta", "reading": rname,
                             "PAC": pac_ozkurt(xc[SCALP.index(ch)], BETA, nlo, GAMMA, nhi)})
        if vname == "m3":
            _, p_ = welch_psd(xc[[SCALP.index("C3"), SCALP.index("C4")]])
            csd_psd = dict(zip(["C3", "C4"], p_))
    pac = pd.DataFrame(prow)

    freqs, psd = welch_psd(x)
    return {"info": info, "shape": shape, "pac": pac, "freqs": freqs,
            "psd": pd.DataFrame(psd, index=SCALP, columns=np.round(freqs, 4)),
            "csd_psd": pd.DataFrame(csd_psd, index=np.round(freqs, 4)).T}


# ----------------------------------------------------------------------------- statistics

def signed_rank(a, b, method: str = "approx"):
    """Wilcoxon signed rank of paired a and b: statistic min(W+, W-) and two-sided p.

    method "approx" is the normal approximation without continuity correction (old scipy
    default, which the paper's printed p-values match); "exact" is a variant.
    """
    a, b = np.asarray(a, float), np.asarray(b, float)
    if method == "approx":
        r = stats.wilcoxon(a, b, method="approx", correction=False, zero_method="wilcox")
    else:
        r = stats.wilcoxon(a, b, method="exact", zero_method="wilcox")
    return float(r.statistic), float(r.pvalue)


def rank_sum(a, b):
    r = stats.ranksums(np.asarray(a, float), np.asarray(b, float))
    return float(r.statistic), float(r.pvalue)


def cohen_d(m1, m2) -> float:
    """(mean1 - mean2) / sqrt((sd1^2 + sd2^2) / 2), sample SDs (code effectsize)."""
    m1, m2 = np.asarray(m1, float), np.asarray(m2, float)
    return float((m1.mean() - m2.mean()) / np.sqrt((m1.std(ddof=1) ** 2 + m2.std(ddof=1) ** 2) / 2))


def fdr_bh(p) -> np.ndarray:
    """Benjamini-Hochberg adjusted p-values."""
    p = np.asarray(p, float)
    n = len(p)
    order = np.argsort(p)
    adj = p[order] * n / np.arange(1, n + 1)
    adj = np.minimum.accumulate(adj[::-1])[::-1]
    out = np.empty(n)
    out[order] = np.minimum(adj, 1)
    return out


def p_adjust(p, method: str = "bh") -> np.ndarray:
    """Adjusted p-values: "bh" (Benjamini-Hochberg), "by" (Benjamini-Yekutieli), "holm", "bonferroni".

    Only "bh" is the paper's (Methods: FDR); the others show how far a result rests on the procedure.
    """
    p = np.asarray(p, float)
    n = len(p)
    if method == "bh":
        return fdr_bh(p)
    if method == "by":
        return np.minimum(fdr_bh(p) * np.sum(1.0 / np.arange(1, n + 1)), 1)
    if method == "bonferroni":
        return np.minimum(p * n, 1)
    if method == "holm":
        order = np.argsort(p)
        adj = np.maximum.accumulate(p[order] * (n - np.arange(n)))
        out = np.empty(n)
        out[order] = np.minimum(adj, 1)
        return out
    raise ValueError(method)
