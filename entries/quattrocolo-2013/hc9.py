"""Loading and sag measures for the O-LM current-step recordings of CRCNS data set hc-9.

Quattrocolo & Maccaferri (2013), J Neurosci 33:5486-5498, doi:10.1523/jneurosci.5680-12.2013.
Data set: Quattrocolo & Maccaferri (2016), CRCNS.org, doi:10.6080/K0HQ3WTH.

The data set is one zip, live/Maccaferri_data.zip, holding one ATF (Axon text) file per cell.
Each file has a time column (s) and, per sweep, the membrane potential (mV) and the injected
current (pA). The zip is read in place from the public S3 bucket over range requests (fsspec and
zipfile); nothing is written to disk.

Where the parameters come from:

- The step to examine is the -100 pA step, from the Figure 7A and 7D legends ("Notice the
  presence of a sag in the hyperpolarizing response. In both cases, -100/50 pA current pulses
  were used"), as the claim's criterion says. The +50 pA step is the legends' depolarizing pulse.
- Reading (a), from the claim's criterion: the sag is the relaxation from the peak
  hyperpolarization during the step to the mean voltage over the step's last 100 ms
  (`END_WINDOW_S`), and it is visible when larger than twice (`SD_FACTOR`) the SD of the
  pre-step baseline voltage.
- Reading (b), from the claim's criterion: the sag ratio (V_end - V_min) / (V_baseline - V_min)
  of at least 0.1 (`RATIO_THRESHOLD`).
- The pre-step baseline is all of the sweep before the current step (0 to 75 ms in these files).
  The criterion says "pre-step baseline" without a window; using all of it is a standard choice.
- V_min is the minimum of a 1 ms running mean (`SMOOTH_S`) of the trace during the step, a
  standard choice. The raw minimum is shown as a variant. The raw minimum picks the most negative
  noise sample, so it finds a "sag" of several baseline SDs in a trace that has none (the
  verifier's round-1 check, repeated in the notebook on a synthetic trace and on each cell's 0 pA
  sweep); the running mean removes most of that bias.
- Spikes are counted as upward crossings of 0 mV (`SPIKE_THRESHOLD_MV`), a standard choice used
  only to describe the +50 pA firing, which no outcome rests on.
"""

from __future__ import annotations

import hashlib
import io
import re
import zipfile

import fsspec
import numpy as np
import pandas as pd

DATASET = "hc-9"
VERSION = "unversioned"   # CRCNS data sets are not versioned; the files are pinned by their MD5 sums
EXPECTED_ZIP_MD5 = "4e3175055681b99ad5be06ba542a93b8"   # from live/checksums.md5, 2026-11-04
BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-9/live/"
ZIP_URL = BUCKET + "Maccaferri_data.zip"
CHECKSUMS_URL = BUCKET + "checksums.md5"
# Old documentation of the data set, kept by CRCNS under hc-9/old/.
OLD_DESCRIPTION_URL = ("https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-9/old/"
                       "crcns_data_description_Maccaferri.docx")

CELLS = ["1May2012_P3", "20Sept2011_P2", "24October2012_C2"]

HYPER_STEP_PA = -100.0     # Figure 7A and 7D legends
DEPOL_STEP_PA = 50.0       # Figure 7A and 7D legends
END_WINDOW_S = 0.100       # claim criterion, reading (a): last 100 ms of the step
SD_FACTOR = 2.0            # claim criterion, reading (a)
RATIO_THRESHOLD = 0.1      # claim criterion, reading (b)
SMOOTH_S = 0.001           # standard choice: V_min from a 1 ms running mean
STEP_DETECT_PA = 5.0       # current departing from its first sample by more than this is the step
SPIKE_THRESHOLD_MV = 0.0   # standard choice, descriptive only


def _open_zip() -> zipfile.ZipFile:
    return zipfile.ZipFile(fsspec.open(ZIP_URL, block_size=2**20).open())


def zip_md5() -> str:
    """MD5 of the whole zip, read in memory in 1 MiB blocks."""
    h = hashlib.md5()
    with fsspec.open(ZIP_URL, block_size=2**20).open() as f:
        while True:
            block = f.read(2**20)
            if not block:
                break
            h.update(block)
    return h.hexdigest()


def published_checksums() -> dict[str, str]:
    """The data set's checksums.md5, as {file: md5}."""
    with fsspec.open(CHECKSUMS_URL, "rt") as f:
        return {line.split()[1]: line.split()[0] for line in f if line.strip()}


def old_description_text() -> str:
    """Text of the superseded description under hc-9/old/ (a .docx, itself a zip of XML)."""
    with fsspec.open(OLD_DESCRIPTION_URL, block_size=2**20).open() as f:
        xml = zipfile.ZipFile(io.BytesIO(f.read())).read("word/document.xml").decode("utf8")
    paragraphs = re.findall(r"<w:p[ >].*?</w:p>", xml, flags=re.S)
    return "\n".join("".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p)) for p in paragraphs)


def zip_listing() -> pd.DataFrame:
    z = _open_zip()
    return pd.DataFrame([(i.filename, i.file_size, "%04d-%02d-%02d" % i.date_time[:3])
                         for i in z.infolist()], columns=["member", "bytes", "date"])


def parse_atf(raw: bytes) -> dict:
    """Parse one ATF file: its header records and its data table."""
    text = raw.decode("latin1").splitlines()
    n_header, n_cols = (int(x) for x in text[1].split())
    header = text[2:2 + n_header]
    columns = [c.strip('"') for c in text[2 + n_header].split("\t")]
    data = pd.read_csv(io.StringIO("\n".join(text[3 + n_header:])), sep="\t", header=None,
                       names=columns)
    return {"version": text[0], "n_header": n_header, "n_cols": n_cols, "header": header,
            "columns": columns, "data": data}


def load_cells() -> dict[str, dict]:
    """Load every cell: time (s), voltage (mV) and current (pA), one column per sweep."""
    z = _open_zip()
    cells = {}
    for name in CELLS:
        atf = parse_atf(z.read(f"Maccaferri_data/{name}_raw.atf"))
        d = atf["data"]
        v_cols = [c for c in atf["columns"] if c.endswith("(mV)")]
        i_cols = [c for c in atf["columns"] if c.endswith("(pA)")]
        t = d.iloc[:, 0].to_numpy()
        cells[name] = {"t": t, "v": d[v_cols].to_numpy(), "i": d[i_cols].to_numpy(),
                       "fs": 1.0 / np.median(np.diff(t)), "atf": atf,
                       "raw_md5": hashlib.md5(z.read(f"Maccaferri_data/{name}_raw.atf")).hexdigest()}
    return cells


def step_table(cell: dict) -> pd.DataFrame:
    """Per sweep, the step's current level, onset and offset, taken from the current channel."""
    t, i = cell["t"], cell["i"]
    rows = []
    for k in range(i.shape[1]):
        dev = np.abs(i[:, k] - i[0, k]) > STEP_DETECT_PA
        idx = np.flatnonzero(dev)
        if len(idx):
            rows.append((k + 1, float(np.median(i[idx, k])), t[idx[0]], t[idx[-1]] + 1 / cell["fs"],
                         i[0, k]))
        else:
            rows.append((k + 1, 0.0, np.nan, np.nan, i[0, k]))
    return pd.DataFrame(rows, columns=["sweep", "step_pA", "on_s", "off_s", "holding_pA"])


def step_window(cell: dict) -> tuple[float, float]:
    """Onset and offset of the current step, common to all sweeps that have one."""
    st = step_table(cell).dropna()
    return float(st.on_s.median()), float(st.off_s.median())


def sweep_for(cell: dict, level_pa: float) -> int:
    """Column index of the sweep with the given step level."""
    st = step_table(cell)
    match = np.flatnonzero(np.isclose(st.step_pA, level_pa, atol=1.0))
    if len(match) != 1:
        raise ValueError(f"{len(match)} sweeps at {level_pa} pA")
    return int(match[0])


def sag_measures(t: np.ndarray, v: np.ndarray, on: float, off: float,
                 end_window: float = END_WINDOW_S, smooth: float = SMOOTH_S) -> dict:
    """Sag measures of one hyperpolarizing sweep.

    Baseline: all samples before the step. V_min: minimum during the step of a running mean of
    `smooth` seconds (of the raw trace when `smooth` is 0). V_end: mean over the last `end_window` seconds of the step.
    """
    fs = 1.0 / np.median(np.diff(t))
    pre = t < on
    during = (t >= on) & (t < off)
    end = (t >= off - end_window) & (t < off)
    vv = v
    if smooth > 0:
        n = max(1, int(round(smooth * fs)))
        vv = np.convolve(v, np.ones(n) / n, mode="same")
    v_base = float(v[pre].mean())
    sd_base = float(v[pre].std(ddof=1))
    k_min = np.flatnonzero(during)[np.argmin(vv[during])]
    v_min = float(vv[k_min])
    v_end = float(v[end].mean())
    sag = v_end - v_min
    return {"v_base": v_base, "sd_base": sd_base, "v_min": v_min, "t_min_ms": (t[k_min] - on) * 1e3,
            "v_end": v_end, "sag_mV": sag, "sag_over_sd": sag / sd_base,
            "sag_ratio": sag / (v_base - v_min)}


def spike_times(t: np.ndarray, v: np.ndarray, threshold: float = SPIKE_THRESHOLD_MV) -> np.ndarray:
    up = np.flatnonzero((v[1:] > threshold) & (v[:-1] <= threshold)) + 1
    return t[up]
