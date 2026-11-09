"""Loading and event detection for dandiset 001752 (postsynaptic currents of VENs and PCs in macaque AIC),
for the reproduction of Liu et al. (2026), Nature Cell Biology, doi:10.1038/s41556-026-02009-4, Fig. 5a-c.

Where each parameter comes from:

- Event detection threshold, 5 pA, or the recording's own RMS noise: the claims file's two readings of the
  Methods sentence "The event detection threshold was set at the maximus root mean squared noise level
  (5 pA)" (Methods, Electrophysiological recording, the paragraph on EPSCs and IPSCs).
- Direction of events: the holding potential the file records (claims file, fig5b-sipsc-frequency). The
  EPSC files and the miniature IPSC files hold inward currents; the spontaneous IPSC files are named
  "holding at +20mV" and hold outward currents.
- Frequency is the number of events over the duration analysed, in Hz, and amplitude the mean event
  amplitude, in pA (Methods, "Recordings of synaptic events were assessed for frequency (Hz) and amplitude
  (pA)"; the code's per-cell tables give one of each per cell).
- Duration analysed: the whole recording (the claims file's reading of the Methods), with the first 30 s as
  a variant (the code's mIPSC table, miniEPSCs_Fig7ab.xlsx sheet mIPSC_sum, gives 30 s for every cell).
- Cell types: the paper's code's table metadata_PSC.csv, which names each NWB file, since the files carry
  no cell type (see the notebook).
- Standard choices that are not the paper's (it used miniAnalysis, whose settings it does not give, and
  which is not reproduced here); they follow the scheme miniAnalysis uses, with common values. The trace
  is referred to a running median over 1 s (BASELINE_S). A candidate event is a local peak in the
  direction of the events that is the largest point within 10 ms (PEAK_SEARCH_S). Its amplitude is the
  peak minus the mean over 3 ms (BASELINE_AVERAGE_S) ending 5 ms (BASELINE_LEAD_S) before the peak, and
  it is an event when that amplitude reaches the threshold. No area threshold is applied. Trailing
  samples that are exactly zero (padding found in some files) are cut. Events above 500 pA
  (ARTIFACT_PA) are counted as artefacts (unclamped spikes or pulses) and left out of the frequency and
  the amplitude. The noise of a recording, for reading (b), is the robust standard deviation (1.4826
  times the median absolute deviation) of the trace referred to its running median.
- Group test: the two-tailed Wilcoxon rank-sum test as MATLAB's ranksum computes it by default (ranksum), the
  function the code's Fig. 5 scripts call (claims file, criteria of the Fig. 5 claims).
- Detector check, deciding nothing: peaks of the opposite polarity as a noise null, and synthetic events
  (inject_events, recovered) added to the real traces. Their rate, amplitudes and shape are standard choices.
"""
from __future__ import annotations

import io
import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from scipy import ndimage, signal

DANDISET = "001752"
VERSION = "0.260825.0222"
API = "https://api.dandiarchive.org/api"

CODE_REPO = "https://github.com/RFLiu2021/AIC_proj"
CODE_COMMIT = "44cd8a6dfbb1f1ce363d73742e4f3652086b0f9d"
RAW = f"https://raw.githubusercontent.com/RFLiu2021/AIC_proj/{CODE_COMMIT}/ephysio"
LABELS_FILE = "data_ephy/rawdata_ephysio/metadata_PSC.csv"
SPSC_SHEET = "data_ephy/sPSCs_Fig7ab.xlsx"
MINI_SHEET = "data_ephy/miniEPSCs_Fig7ab.xlsx"

BASELINE_S = 1.0
PEAK_SEARCH_S = 0.010
BASELINE_LEAD_S = 0.005
BASELINE_AVERAGE_S = 0.003
ARTIFACT_PA = 500.0
FIXED_THRESHOLD_PA = 5.0
CODE_WINDOW_S = 30.0


def _get(url: str) -> bytes:
    with urllib.request.urlopen(url, timeout=120) as r:
        return r.read()


def assets() -> list[dict]:
    """Every asset of the pinned version, with its path, id and size."""
    out, url = [], f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    while url:
        page = json.loads(_get(url))
        out += page["results"]
        url = page.get("next")
    return out


def version_metadata() -> dict:
    return json.loads(_get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/"))


def _text(h, path):
    if path not in h:
        return None
    v = h[path][()]
    if isinstance(v, np.ndarray):
        v = v.ravel()[0]
    return v.decode() if isinstance(v, bytes) else str(v)


def read_file(asset: dict) -> dict:
    """Stream one NWB file and return its metadata and current trace (pA)."""
    url = f"{API}/assets/{asset['asset_id']}/download/"
    with h5py.File(remfile.File(url), "r") as h:
        ts = h["acquisition/VoltageClampSeries"]
        data = ts["data"]
        rate = float(ts["starting_time"].attrs["rate"])
        unit = data.attrs["unit"]
        unit = unit.decode() if isinstance(unit, bytes) else unit
        conv = float(data.attrs.get("conversion", 1.0))
        x = data[:] * conv
        stim = h["stimulus/presentation/VoltageClampStimulusSeries/data"][:]
        rec = dict(
            file=asset["path"].split("/")[-1],
            path=asset["path"],
            subject=_text(h, "general/subject/subject_id"),
            sex=_text(h, "general/subject/sex"),
            age=_text(h, "general/subject/age"),
            session=_text(h, "general/session_id"),
            session_description=_text(h, "session_description"),
            experiment_description=_text(h, "general/experiment_description"),
            stimulus_description=ts.attrs["stimulus_description"],
            cell_id=_text(h, "general/intracellular_ephys/IntracellularElectrode/cell_id"),
            rate=rate, unit=unit, n_samples=len(x),
            stimulus_values=np.unique(stim).tolist(),
        )
    if unit != "amperes":
        raise ValueError(f"{rec['file']}: unit {unit}")
    rec["trace_pA"] = x * 1e12
    return rec


def read_all(asset_list: list[dict], workers: int = 16) -> list[dict]:
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(read_file, asset_list))


def experiment_of(description: str) -> str:
    """sEPSC, sIPSC, mEPSC or mIPSC, from the file's session description."""
    d = description.lower()
    kind = "m" if "miniature" in d else "s" if "spontaneous" in d else "?"
    return kind + ("EPSC" if "epsc" in d else "IPSC" if "ipsc" in d else "?")


def labels() -> pd.DataFrame:
    """The code's table of NWB files with cell type and experiment."""
    return pd.read_csv(io.BytesIO(_get(f"{RAW}/{LABELS_FILE}")))


def sheet(name: str, sheet_name: str) -> pd.DataFrame:
    return pd.read_excel(io.BytesIO(_get(f"{RAW}/{name}")), sheet_name=sheet_name, header=None)


def trim_padding(x: np.ndarray) -> tuple[np.ndarray, int]:
    """Cut a trailing run of samples that are exactly zero; return the trace and how many were cut."""
    nz = np.flatnonzero(x != 0)
    end = nz[-1] + 1 if len(nz) else 0
    return x[:end], len(x) - end


def baseline(x: np.ndarray, rate: float) -> np.ndarray:
    """Running median over BASELINE_S, computed on a 10-fold decimated copy and interpolated (speed)."""
    step = 10
    xs = x[: len(x) // step * step].reshape(-1, step).mean(axis=1)
    size = max(3, int(BASELINE_S * rate / step) | 1)
    b = ndimage.median_filter(xs, size=size, mode="nearest")
    t = (np.arange(len(b)) + 0.5) * step
    return np.interp(np.arange(len(x)), t, b)


def robust_sd(y: np.ndarray) -> float:
    return float(1.4826 * np.median(np.abs(y - np.median(y))))


def detect(x: np.ndarray, rate: float, sign: int, threshold: float | None = None,
           window_s: float | None = None) -> dict:
    """Detect events in a trace (pA). sign = -1 for inward events, +1 for outward.

    threshold None means the recording's own RMS noise (reading b); a number is in pA (reading a).
    window_s limits the analysis to the first window_s seconds.

    The event definition follows the scheme of miniAnalysis, which the paper used, with standard
    parameters (not the paper's, which it does not give): a peak is the largest point within
    PEAK_SEARCH_S around it, and its amplitude is measured from a baseline averaged over
    BASELINE_AVERAGE_S ending BASELINE_LEAD_S before the peak. No area threshold is applied."""
    if window_s is not None:
        x = x[: int(window_s * rate)]
    z = sign * (x - baseline(x, rate))
    noise = robust_sd(z)
    thr = noise if threshold is None else threshold
    half = max(1, int(round(PEAK_SEARCH_S / 2 * rate)))
    lead = int(round(BASELINE_LEAD_S * rate))
    avg = max(1, int(round(BASELINE_AVERAGE_S * rate)))
    peaks, _ = signal.find_peaks(z, distance=2 * half)
    peaks = peaks[(peaks >= lead + avg) & (peaks < len(z) - half)]
    csum = np.concatenate([[0.0], np.cumsum(z)])
    base = (csum[peaks - lead + 1] - csum[peaks - lead - avg + 1]) / avg
    amp = z[peaks] - base
    ok = amp >= thr
    peaks, amp = peaks[ok], amp[ok]
    keep = amp <= ARTIFACT_PA
    duration = len(x) / rate
    return dict(
        n_events=int(keep.sum()), n_artifacts=int((~keep).sum()), duration_s=duration,
        frequency_hz=keep.sum() / duration, amplitude_pa=float(amp[keep].mean()) if keep.any() else np.nan,
        median_amplitude_pa=float(np.median(amp[keep])) if keep.any() else np.nan,
        noise_pa=noise, threshold_pa=thr, peaks=peaks[keep], amplitudes=amp[keep])


def name_key(name: str, experiment: str) -> str:
    """A common key for the original file names in metadata_PSC.csv and the cell names in the code's
    per-cell sheets: month and day, then slice and cell, lower case ('vens' and 'vs' are the same)."""
    import re
    n = str(name).strip().lower()
    n = re.split(r"[-+]\d+mv$", n)[0]
    if experiment in ("sEPSC", "sIPSC"):
        n = re.split(r"_|trace", n)[0]
        if n.startswith("2020"):
            n = n[4:]
    elif experiment == "mEPSC":
        n = n[8:] if n.startswith("20210403") else n
        n = "0403" + (n if n.startswith("a") else "a" + n)
    elif experiment == "mIPSC":
        n = n[8:] if n.startswith("20250904") else n
        n = "0904" + n
    return n.replace("vens", "vs")


def code_tables() -> pd.DataFrame:
    """The paper's per-cell values from its code's sheets: one row per entry, with the sheet's cell type,
    frequency (Hz) and amplitude (pA). Amplitudes of the sPSC and mEPSC sheets are stored times 1e10 A
    (the code's comments), so are multiplied by 100 to give pA."""
    rows = []
    s = sheet(SPSC_SHEET, "summary")
    for exp, r0, r1 in (("sEPSC", 3, 14), ("sIPSC", 21, 29)):
        for i in range(r0, r1):
            for name_col, f_col, a_col, ctype in ((0, 2, 3, "PC"), (10, 11, 12, "VEN")):
                name = s.iat[i, name_col]
                if isinstance(name, str) and name.strip():
                    rows.append(dict(experiment=exp, sheet_name=name.strip(), sheet_type=ctype,
                                     sheet_freq=float(s.iat[i, f_col]), sheet_amp=100 * float(s.iat[i, a_col])))
    m = sheet(MINI_SHEET, "mEPSC_sum")
    for i in range(1, 9):
        for name_col, f_col, a_col, ctype in ((0, 1, 2, "VEN"), (4, 5, 6, "PC")):
            rows.append(dict(experiment="mEPSC", sheet_name=str(m.iat[i, name_col]).strip(), sheet_type=ctype,
                             sheet_freq=float(m.iat[i, f_col]), sheet_amp=100 * float(m.iat[i, a_col])))
    mi = sheet(MINI_SHEET, "mIPSC_sum")
    for i in range(1, len(mi)):
        if isinstance(mi.iat[i, 0], str):
            rows.append(dict(experiment="mIPSC", sheet_name=mi.iat[i, 0].strip(), sheet_type=mi.iat[i, 1],
                             sheet_n_events=int(mi.iat[i, 2]), sheet_duration_s=float(mi.iat[i, 3]),
                             sheet_freq=float(mi.iat[i, 4]), sheet_amp=float(mi.iat[i, 5])))
    df = pd.DataFrame(rows)
    df["key"] = [name_key(n, e) for n, e in zip(df.sheet_name, df.experiment)]
    return df


def decay_time_ms(x: np.ndarray, rate: float, sign: int, peaks: np.ndarray, amplitudes: np.ndarray) -> float:
    """Time from the peak of the average event to 37% of its amplitude, in ms (a check of the time base).
    Uses events with no other event within 30 ms after them."""
    z = sign * (x - baseline(x, rate))
    w = int(0.030 * rate)
    iso = [p for k, p in enumerate(peaks) if (k + 1 == len(peaks) or peaks[k + 1] - p > w) and p + w < len(z) and p > 10]
    if len(iso) < 5:
        return np.nan
    avg = np.mean([z[p - 10: p + w] - np.mean(z[p - 10: p - 5]) for p in iso], axis=0)
    after = avg[10:]
    below = np.flatnonzero(after < 0.37 * after[0])
    return float(below[0] * 1000.0 / rate) if len(below) else np.nan


def ranksum(x, y) -> tuple[float, float, str]:
    """Two-tailed Wilcoxon rank-sum test as MATLAB's ranksum computes it by default, the function the code's
    Fig5ab_ana_sPSC.m and Fig5ab_ana_mPSC.m call: the exact distribution when min(nx, ny) < 10 and
    nx + ny < 20, otherwise the normal approximation with continuity and tie corrections (MATLAB
    documentation of ranksum, 'method'). Returns U, p and the method used."""
    from scipy import stats
    x, y = np.asarray(x, float), np.asarray(y, float)
    exact = min(len(x), len(y)) < 10 and len(x) + len(y) < 20
    method = "exact" if exact else "asymptotic"
    t = stats.mannwhitneyu(x, y, alternative="two-sided", method=method, use_continuity=True)
    return float(t.statistic), float(t.pvalue), method


# Synthetic events for the positive control (a check of the detector, not a parameter of the analysis):
# a difference of exponentials with 1 ms rise and the decay of the experiment's average event (data check),
# amplitudes log-normal around INJECT_MEDIAN_PA, Poisson times at INJECT_RATE_HZ. Standard choices.
INJECT_RATE_HZ = 2.0
INJECT_MEDIAN_PA = 10.0
INJECT_SIGMA = 0.4
INJECT_RISE_MS = 1.0


def inject_events(x: np.ndarray, rate: float, sign: int, decay_ms: float, rng: np.random.Generator):
    """Add synthetic events to a real trace; return the new trace, the event times (samples) and amplitudes."""
    n = rng.poisson(INJECT_RATE_HZ * len(x) / rate)
    times = np.sort(rng.integers(int(0.05 * rate), len(x) - int(0.2 * rate), n))
    amps = INJECT_MEDIAN_PA * np.exp(INJECT_SIGMA * rng.standard_normal(n))
    t = np.arange(int(0.2 * rate)) / rate * 1000.0
    k = np.exp(-t / decay_ms) - np.exp(-t / INJECT_RISE_MS)
    k /= k.max()
    y = x.astype(float).copy()
    kick = np.zeros(len(x))
    np.add.at(kick, times, amps)
    y += sign * signal.fftconvolve(kick, k)[: len(x)]
    return y, times + int(np.argmax(k)), amps


def recovered(peaks: np.ndarray, times: np.ndarray, tol: int) -> np.ndarray:
    """For each injected event, whether a detected peak lies within tol samples of its peak."""
    if len(peaks) == 0:
        return np.zeros(len(times), bool)
    j = np.clip(np.searchsorted(peaks, times), 1, len(peaks) - 1)
    d = np.minimum(np.abs(peaks[j] - times), np.abs(peaks[j - 1] - times))
    return d <= tol
