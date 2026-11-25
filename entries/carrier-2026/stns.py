"""Loading and measures for Carrier et al. (2026) on Zenodo records 17624449 and 17794764.

Carrier, Romano, Scaria, Palmer, O'Leary, Marder & Powell (2026), "The combined effects of
temperature and salinity on the stomatogastric nervous system of two species of decapod
crustacea", J Neurophysiol 135: 797-814, doi:10.1152/jn.00294.2025.

Record 17624449 (Part I, folder zenodo-17624449) holds the raw Spike2 recordings of the lobster
(H. americanus) temperature ramps (`Lobster STNS.zip`), half of the crab (C. borealis) raw data
(`Raw Crab Data 1.zip`), and the authors' analysis tables: `Crab Metadata.xlsx` (per crab
preparation: PD burst frequency at each step of each ramp, the salinity series, the crash
temperature of each neuron, phases), `Lobster Pyloric Frequencies.xlsx` (per lobster
preparation: PD burst frequency at each step of each ramp, with the crash step), three GraphPad
Prism 10 files (`.prism`, zip archives of JSON and CSV) and four MATLAB files. Record 17794764
(Part II, folder zenodo-17794764) holds the other half of the crab raw data and the in vivo PPG
recordings (Axon `.abf` files in zips inside zips).

Every file is read from the archive into memory with fsspec (block_size 2**20), at the pinned
record, and a file read whole is checked against the MD5 the record lists. Nothing is written
to disk.

Where the parameters come from:

- Q10. "Pyloric cycle frequency (F) was plotted against temperature (T) in a semi-log plot and
  the Q10 was the slope of the nonlinear regression (m) ... m = dlogF/dT, Q10 = 10^(10m)", fits
  in GraphPad Prism, slopes of two groups compared with Fisher's extra-sum-of-squares F test, a
  single slope against zero (paper, Methods, Data Analysis and Statistics). The claims file
  names two readings: Q-a, a least-squares fit of F = 10^(mT + b) to untransformed frequency
  (Prism's "semilog line" model; the deposited Prism outputs `Crab & Lobster Nonlin fit of
  *.csv` report a "Yintercept" and "Slope" of this model), and Q-b, a straight line fitted to
  log10 F. Both are computed. The shared-slope model keeps one intercept per group (claims
  file, opening comment). The 95% CI of the slope here is the asymptotic (Wald) interval;
  Prism reports a profile-likelihood interval. This is a standard choice for a detail that
  can move a bound slightly but not the fit.
- The final 30 s of each 2-min step, the PD burst frequency, the crash steps and the crash
  temperatures are the authors' own values from the deposited tables (see the notebook); the
  burst detection itself (custom Spike2 or MATLAB scripts, Methods) is not repeated.
- Phase (Fig. 3C, Table 1): the deposited Prism sheets of phase per preparation and step; the
  same semi-log fit and a slope compared with zero (Methods, "We then used a linear model ...
  assessing if the Q10 slope of a pyloric neuron's phase differed from a zero slope").
- In vivo spectra (Fig. 8): short-time Fourier transform of the PPG signal over 0 to 3 Hz
  (Methods, "computed the power associated with each frequency ranging from 0 Hz to 3 Hz").
  The 10-s window with 50% overlap, the 0.3 to 3 Hz band and the three-times-median rule are
  the claims file's standard choices, not the paper's (criterion of
  fig8-invivo-rhythm-maintained). Decimating each 2-min file to 50 Hz before the transform is a
  standard choice that cannot change the 0 to 3 Hz spectrum beyond the file edges. The shuffled
  trace (a flat spectrum with the same values) is a reference for the rule, and the 99th
  percentile of its peak ratio a stricter variant; both are this attempt's, not the paper's.
- Zenodo answered some range requests with HTTP 500 under load; `read_member` retries them.
"""

from __future__ import annotations

import hashlib
import io
import json
import re
import time
import zipfile

import fsspec
import numpy as np
import pandas as pd
import requests
from scipy import optimize, signal, stats

PART1 = "17624449"   # Zenodo record (version) pinned: the only published version
PART2 = "17794764"   # Zenodo record (version) pinned: the only published version
FOLDER = {PART1: "zenodo-17624449", PART2: "zenodo-17794764"}

_FILES: dict[str, dict[str, dict]] = {}


def file_list(record: str) -> dict[str, dict]:
    """Key -> {size, md5} for every file of a record, from the Zenodo API."""
    if record not in _FILES:
        r = requests.get(f"https://zenodo.org/api/records/{record}", timeout=60)
        r.raise_for_status()
        meta = r.json()
        assert str(meta["id"]) == record, meta["id"]
        _FILES[record] = {f["key"]: {"size": f["size"], "md5": f["checksum"].split(":", 1)[1]}
                          for f in meta["files"]}
    return _FILES[record]


def url(record: str, key: str) -> str:
    return f"https://zenodo.org/api/records/{record}/files/{requests.utils.quote(key)}/content"


def read_file(record: str, key: str) -> bytes:
    """Read a whole file into memory and check its MD5 against the record's list."""
    with fsspec.open(url(record, key), block_size=2**20) as f:
        b = f.read()
    want = file_list(record)[key]["md5"]
    got = hashlib.md5(b).hexdigest()
    if got != want:
        raise ValueError(f"MD5 mismatch for {key}: {got} != {want}")
    return b


def open_zip(record: str, key: str):
    """A zipfile over the remote file, read in place by range requests (the caller closes f)."""
    f = fsspec.open(url(record, key), block_size=2**20).open()
    return f, zipfile.ZipFile(f)


def read_member(record: str, key: str, member: str, tries: int = 6) -> bytes:
    """Read one member of a remote zip, retrying when the server fails (Zenodo answers 500 or
    drops the connection under load); after the last try the error is raised."""
    for k in range(tries):
        try:
            f, z = open_zip(record, key)
            try:
                return z.read(member)
            finally:
                f.close()
        except Exception:
            if k == tries - 1:
                raise
            time.sleep(10 * 2 ** k)


# ---------------------------------------------------------------- Prism files

def prism_data(b: bytes) -> dict[str, dict]:
    """The data sheets of a Prism 10 .prism file (a zip of JSON and CSV).

    Returns, per sheet title: the table format, the data-set titles, the number of replicate
    sub-columns, and the CSV table as a DataFrame (no header; for XY tables column 0 is X).
    """
    z = zipfile.ZipFile(io.BytesIO(b))
    doc = json.loads(z.read("document.json"))
    out = {}
    for sid in doc["sheets"]["data"]:
        sheet = json.loads(z.read(f"data/sheets/{sid}/sheet.json"))
        table = sheet["table"]
        titles = []
        for ds in table.get("dataSets", []):
            d = json.loads(z.read(f"data/sets/{ds}.json"))
            t = d.get("title")
            titles.append(t.get("string") if isinstance(t, dict) else t)
        csv = z.read(f"data/tables/{table['uid']}/data.csv").decode("utf-8-sig")
        df = pd.read_csv(io.StringIO(csv), header=None) if csv.strip() else pd.DataFrame()
        df = df.dropna(how="all")
        out[sheet["title"]] = {"format": table["format"], "titles": titles,
                               "replicates": table.get("replicatesCount", 1), "table": df}
    return out


def prism_xy_groups(sheet: dict) -> dict[str, pd.DataFrame]:
    """Split an XY sheet with replicates into one wide frame per data set (rows: X)."""
    df = sheet["table"]
    has_row_titles = df.shape[1] > 0 and df[0].isna().all()
    if has_row_titles:
        df = df.drop(columns=0)
        df.columns = range(df.shape[1])
    x = df[0].astype(float)
    n = sheet["replicates"]
    out = {}
    for i, title in enumerate(sheet["titles"]):
        cols = list(range(1 + i * n, 1 + (i + 1) * n))
        cols = [c for c in cols if c in df.columns]
        g = df[cols].apply(pd.to_numeric, errors="coerce")
        g.index = x.values
        g.columns = range(len(cols))
        out[title or f"set{i}"] = g
    return out


# ---------------------------------------------------------------- Excel tables

def _temp_label(v) -> float:
    """Row labels of the temperature steps. The 10 C label is stored as a date (2024-10-11)."""
    if isinstance(v, (pd.Timestamp,)) or hasattr(v, "year"):
        return 10.0
    return float(v)


def crab_ramp_frequencies(x: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Tidy PD burst frequency of the crab ramps, sheet 'Burst Frequency' of Crab Metadata.xlsx.

    Four blocks: 1x ramps of the 0.75x set, 0.75x ramps, 1x ramps of the 1.25x set, 1.25x ramps.
    """
    df = x["Burst Frequency"]
    blocks = [(i, str(df.iat[i, 0])) for i in range(len(df)) if "temp ramps" in str(df.iat[i, 0])]
    rows = []
    for start, label in blocks:
        salinity = {"1x": 1.0, "0.75x": 0.75, "1.25x": 1.25}[label.split()[0]]
        cset = "0.75x" if ("0.75" in label) else "1.25x"
        preps = {c: str(df.iat[start, c]).split(" (")[0].strip() for c in range(1, df.shape[1])
                 if isinstance(df.iat[start, c], str) and re.match(r"\d{3}_\d{3}", str(df.iat[start, c]))}
        r = start + 1
        while r < len(df) and pd.notna(df.iat[r, 0]):
            t = _temp_label(df.iat[r, 0])
            for c, p in preps.items():
                v = df.iat[r, c]
                if pd.notna(v):
                    rows.append({"set": cset, "salinity": salinity, "prep": p, "temp": t, "freq": float(v)})
            r += 1
    return pd.DataFrame(rows)


def crab_saline_series(x: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Tidy sheet 'Burst Frequency Saline Only': 10 C, final 30 s of each 15-min application."""
    df = x["Burst Frequency Saline Only"]
    preps = {c: str(df.iat[0, c]).strip() for c in range(1, df.shape[1]) if str(df.iat[0, c]).startswith("888")}
    rows, series = [], "decreasing"
    for r in range(1, len(df)):
        lab = df.iat[r, 0]
        if pd.isna(lab):
            series = "increasing"
            continue
        sal = float(str(lab).rstrip("x"))
        for c, p in preps.items():
            v = df.iat[r, c]
            rows.append({"series": series, "salinity": sal, "prep": p,
                         "freq": float(v) if pd.notna(v) else np.nan})
    return pd.DataFrame(rows)


def crab_unit_crashes(x: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Tidy sheet 'Individual unit crashes': crash temperature of LP, PY and PD per ramp (NaN: no crash)."""
    df = x["Individual unit crashes"]
    rows = []
    for c0, sal, cset in [(0, 1.0, "0.75x"), (5, 0.75, "0.75x"), (10, 1.0, "1.25x"), (15, 1.25, "1.25x")]:
        assert str(df.iat[2, c0]) == "exp" and [df.iat[2, c0 + k] for k in (1, 2, 3)] == ["LP", "PY", "PD"]
        for r in range(3, len(df)):
            p = df.iat[r, c0]
            if pd.isna(p):
                continue
            rows.append({"set": cset, "salinity": sal, "prep": str(p).strip(),
                         **{n: (float(df.iat[r, c0 + k]) if pd.notna(df.iat[r, c0 + k]) else np.nan)
                            for k, n in ((1, "LP"), (2, "PY"), (3, "PD"))}})
    return pd.DataFrame(rows)


def rhythm_crash(row) -> float:
    """Crash of the rhythm: 'the point at which two of the three pyloric motor neurons failed to
    rhythmically burst' (Methods), so the second neuron crash; NaN if fewer than two crashed."""
    v = sorted(t for t in (row["LP"], row["PY"], row["PD"]) if pd.notna(t))
    return v[1] if len(v) >= 2 else np.nan


def _lobster_prep(v) -> str:
    if isinstance(v, str):
        return v.strip()
    return f"{int(v):06d}"


def lobster_ramp_frequencies(x: dict[str, pd.DataFrame]) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Tidy sheet 'Sheet4' of Lobster Pyloric Frequencies.xlsx.

    Returns (frequencies: salinity, prep, temp, freq) and (ramps: salinity, prep, crash_step,
    not_used), where crash_step is the step marked 'Crash' and not_used the sheet's 'Not used'.
    """
    df = x["Sheet4"]
    starts = [(i, str(df.iat[i, 0]).strip()) for i in range(len(df)) if str(df.iat[i, 0]).strip() in ("1X", "1.25X", "0.75X")]
    freq, ramps = [], []
    for i, lab in starts:
        sal = float(lab.rstrip("X"))
        not_used = {c for c in range(1, df.shape[1]) if str(df.iat[i, c]).strip() == "Not used"}
        hdr = i + 1
        preps = {c: _lobster_prep(df.iat[hdr, c]) for c in range(1, df.shape[1]) if pd.notna(df.iat[hdr, c])}
        crash = {c: np.nan for c in preps}
        r = hdr + 1
        while r < len(df) and pd.notna(df.iat[r, 0]) and str(df.iat[r, 0]).strip() not in ("1X", "1.25X", "0.75X"):
            t = float(df.iat[r, 0])
            for c, p in preps.items():
                v = df.iat[r, c]
                if isinstance(v, str) and v.strip().lower() == "crash":
                    if np.isnan(crash[c]):
                        crash[c] = t
                elif pd.notna(v):
                    freq.append({"salinity": sal, "prep": p, "temp": t, "freq": float(v), "col": c})
            r += 1
        for c, p in preps.items():
            ramps.append({"salinity": sal, "prep": p, "crash_step": crash[c], "not_used": c in not_used, "col": c})
    return pd.DataFrame(freq), pd.DataFrame(ramps)


# ---------------------------------------------------------------- Q10 fits

def _semilog(T, m, b):
    return 10 ** (m * T + b)


def semilog_fit(T, F, reading: str = "Q-a") -> dict:
    """Fit log10 F = m T + b (Q-b) or F = 10^(m T + b) by least squares (Q-a)."""
    T, F = np.asarray(T, float), np.asarray(F, float)
    ok = np.isfinite(T) & np.isfinite(F) & (F > 0)
    T, F = T[ok], F[ok]
    n = len(T)
    m0, b0 = np.polyfit(T, np.log10(F), 1)
    if reading == "Q-b":
        resid = np.log10(F) - (m0 * T + b0)
        sse = float(resid @ resid)
        sxx = ((T - T.mean()) ** 2).sum()
        se = np.sqrt(sse / (n - 2) / sxx)
        m, b = m0, b0
    else:
        (m, b), cov = optimize.curve_fit(_semilog, T, F, p0=(m0, b0), maxfev=20000)
        resid = F - _semilog(T, m, b)
        sse = float(resid @ resid)
        se = float(np.sqrt(cov[0, 0]))
    tq = stats.t.ppf(0.975, n - 2)
    return {"m": m, "b": b, "sse": sse, "n": n, "df": n - 2, "q10": 10 ** (10 * m),
            "q10_lo": 10 ** (10 * (m - tq * se)), "q10_hi": 10 ** (10 * (m + tq * se))}


def zero_slope_test(T, F, reading: str = "Q-a") -> dict:
    """Extra-sum-of-squares F test of the semi-log slope against zero."""
    T, F = np.asarray(T, float), np.asarray(F, float)
    ok = np.isfinite(T) & np.isfinite(F) & (F > 0)
    T, F = T[ok], F[ok]
    full = semilog_fit(T, F, reading)
    if reading == "Q-b":
        y = np.log10(F)
        sse0 = float(((y - y.mean()) ** 2).sum())
    else:
        sse0 = float(((F - F.mean()) ** 2).sum())   # F = 10^b, a constant: its best value is the mean
    Fstat = (sse0 - full["sse"]) / (full["sse"] / full["df"])
    return {**full, "F": Fstat, "df1": 1, "df2": full["df"], "p": float(stats.f.sf(Fstat, 1, full["df"]))}


def shared_slope_test(groups: dict[str, tuple], reading: str = "Q-a") -> dict:
    """Fisher's extra-sum-of-squares F test: one slope per group against one shared slope
    (an intercept per group in both). groups: name -> (T, F)."""
    data = []
    for g, (T, F) in groups.items():
        T, F = np.asarray(T, float), np.asarray(F, float)
        ok = np.isfinite(T) & np.isfinite(F) & (F > 0)
        data.append((g, T[ok], F[ok]))
    fits = {g: semilog_fit(T, F, reading) for g, T, F in data}
    sse_sep = sum(f["sse"] for f in fits.values())
    N = sum(len(T) for _, T, _ in data)
    k = len(data)
    df_sep = N - 2 * k
    idx = np.concatenate([np.full(len(T), i) for i, (_, T, _) in enumerate(data)])
    T_all = np.concatenate([T for _, T, _ in data])
    F_all = np.concatenate([F for _, _, F in data])
    if reading == "Q-b":
        X = np.column_stack([T_all] + [(idx == i).astype(float) for i in range(k)])
        y = np.log10(F_all)
        beta, *_ = np.linalg.lstsq(X, y, rcond=None)
        sse_sh = float(((y - X @ beta) ** 2).sum())
        m_sh = beta[0]
    else:
        p0 = [np.mean([f["m"] for f in fits.values()])] + [fits[g]["b"] for g, _, _ in data]

        def res(p):
            return F_all - 10 ** (p[0] * T_all + np.asarray(p[1:])[idx])
        sol = optimize.least_squares(res, p0, xtol=1e-14, ftol=1e-14, gtol=1e-14)
        sse_sh = float((sol.fun ** 2).sum())
        m_sh = sol.x[0]
    df1 = k - 1
    Fstat = ((sse_sh - sse_sep) / df1) / (sse_sep / df_sep)
    return {"fits": fits, "F": Fstat, "df1": df1, "df2": df_sep, "p": float(stats.f.sf(Fstat, df1, df_sep)),
            "n_points": N, "q10_shared": 10 ** (10 * m_sh)}


# ---------------------------------------------------------------- in vivo PPG

def abf_signal(b: bytes) -> tuple[np.ndarray, float]:
    """Read the first channel of an ABF2 file held in memory, with pyabf's own header and data
    readers (pyabf opens only paths, so the file object is handed to its readers directly)."""
    import pyabf
    abf = pyabf.ABF.__new__(pyabf.ABF)
    abf._preLoadData = True
    abf.abfFilePath = abf.abfFolderPath = abf.stimulusFileFolder = ""
    abf.abfID = "memory"
    abf._cacheStimulusFiles = False
    fb = io.BytesIO(b)
    abf.abfVersion = {"major": 2}
    abf._readHeadersV2(fb)
    abf._makeAdditionalVariables()
    # pyabf's _loadAndScaleData uses np.fromfile, which needs a real file: the same steps here
    raw = np.frombuffer(b, dtype=abf._dtype, count=abf.dataPointCount, offset=abf.dataByteStart)
    raw = raw.reshape(-1, abf.channelCount).T[0].astype(np.float32)
    if abf._dtype == np.int16:
        raw = raw * abf._dataGain[0] + abf._dataOffset[0]
    return raw, float(abf.sampleRate), abf.abfDateTime


DECIMATE_TO_HZ = 50.0   # standard choice: well above the 3 Hz band of the Methods
STFT_WINDOW_S = 10.0    # claims file's standard choice, 10-s windows with 50% overlap


def decimate_to(y: np.ndarray, fs: float) -> tuple[np.ndarray, float]:
    """Remove the mean and decimate to about 50 Hz (zero-phase FIR anti-alias filter)."""
    q = int(round(fs / DECIMATE_TO_HZ))
    y = y.astype(np.float64) - float(np.mean(y))
    if q > 1:
        y = signal.decimate(y, q, ftype="fir", zero_phase=True)
    return y.astype(np.float32), fs / q


def ppg_spectrogram(yd: np.ndarray, fsd: float):
    """STFT power over 0 to 3 Hz of a decimated PPG trace, 10-s windows, 50% overlap."""
    nper = int(STFT_WINDOW_S * fsd)
    f, t, S = signal.spectrogram(yd.astype(np.float64), fs=fsd, nperseg=nper, noverlap=nper // 2,
                                 detrend="linear", scaling="density")
    keep = f <= 3.0
    return f[keep], t, S[keep]


def band_present(f, S, lo=0.3, hi=3.0, ratio=3.0) -> np.ndarray:
    """Per window: the peak power between lo and hi Hz exceeds `ratio` times the median power
    over 0 to 3 Hz of the same window (claims file, reading B-a)."""
    band = (f >= lo) & (f <= hi)
    return S[band].max(axis=0) > ratio * np.median(S, axis=0)


INVIVO_ZIPS = ["Crab In Vivo Data 1.zip", "Crab In Vivo Data 2.zip",
               "Lobster In Vivo Data 1.zip", "Lobster In Vivo Data 2.zip"]


def parse_exposure(member: str) -> dict:
    """Species, animal, salinity and duration from a member name such as
    'Crab In Vivo/Crab18Mean0.75X1Hour.zip'."""
    m = re.search(r"(Crab|Lobster)(\d+)Mean([\d.]+)X(\d+)Hours?\.zip$", member)
    return {"species": m.group(1), "animal": int(m.group(2)), "salinity": float(m.group(3)),
            "hours": int(m.group(4))}


def process_exposure(outer_key: str, member: str, seeds=(), seconds_first: float = 1800.0) -> dict:
    """Read one in vivo exposure (a zip of 2-min ABF files inside an outer zip of record
    17794764), decimate each file, join them in time order, and summarise the 0 to 3 Hz
    spectrogram. `seeds`: generators for a reference, the same trace with its samples shuffled
    (a flat spectrum), to which the same band rule is applied."""
    b = read_member(PART2, outer_key, member)
    zi = zipfile.ZipFile(io.BytesIO(b))
    parts = []
    for n in zi.namelist():
        if n.lower().endswith(".abf"):
            raw = zi.read(n)
            y, fs, start = abf_signal(raw)
            yd, fsd = decimate_to(y, fs)
            parts.append((start, n, yd, fsd, len(y) / fs, fs, hashlib.md5(raw).hexdigest()))
    del b, zi
    parts.sort(key=lambda p: p[0])
    gaps = [(parts[i + 1][0] - parts[i][0]).total_seconds() - parts[i][4] for i in range(len(parts) - 1)]
    yd = np.concatenate([p[2] for p in parts])
    fsd = parts[0][3]
    fr, t, S = ppg_spectrogram(yd, fsd)
    present = band_present(fr, S)
    first = t <= seconds_first
    band = (fr >= 0.3) & (fr <= 3.0)
    peak_f = fr[band][S[band].argmax(axis=0)]
    ratio = S[band].max(axis=0) / np.median(S, axis=0)
    null, null_p99, frac_cal = [], [], []
    for seed in seeds:
        sh = np.random.default_rng(seed).permutation(yd)
        f0, t0, S0 = ppg_spectrogram(sh, fsd)
        null.append(float(band_present(f0, S0).mean()))
        r0 = S0[band].max(axis=0) / np.median(S0, axis=0)
        null_p99.append(float(np.percentile(r0, 99)))
        frac_cal.append(float((ratio > null_p99[-1]).mean()))
    return {**parse_exposure(member), "member": member, "files": len(parts),
            "fs": sorted({p[5] for p in parts}), "start": parts[0][0],
            "duration_min": sum(p[4] for p in parts) / 60, "max_gap_s": max(gaps) if gaps else 0.0,
            "windows": len(t), "frac_present": float(present.mean()),
            "frac_present_first30": float(present[first].mean()),
            "median_peak_hz": float(np.median(peak_f)), "median_ratio": float(np.median(ratio)),
            "null_frac_present": null, "null_ratio_p99": null_p99, "frac_above_null_p99": frac_cal,
            "frac_above_null_p99_first30": None if not seeds else float((ratio[first] > null_p99[0]).mean()),
            "file_md5": [p[6] for p in parts], "spectrogram": (fr, t, S.astype(np.float32))}
