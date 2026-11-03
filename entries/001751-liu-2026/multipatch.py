"""Loading and measures for the multi-patch recordings of dandiset 001751.

Liu, Huang, Shen, Shao, Jing et al. (2026), Nature Cell Biology, doi:10.1038/s41556-026-02009-4,
Fig. 5d-i. Each NWB file holds one connection test in one slice (`session_id`): up to eight
simultaneously recorded channels (`CurrentClampSeries_Repetition_<r>_Channel_<c>`), each sweep
a current-clamp trace, and one stimulus series. Files are streamed from the archive at the
pinned version into memory, reduced to sweep averages, and released; nothing is written to disk.

Where the parameters come from:

- `RATE_HZ`, 25 kHz: the paper's code (Fig5fg_plotConn.m resamples "from 25 kHz"; claims file,
  opening comment). The files state 1 Hz for the responses (`starting_time` rate) and 25 kHz
  for the stimulus; the stimulus pulse of 50 samples is 2 ms at 25 kHz, the 2 ms of the
  Methods ("2 nA for 2 ms at 0.01-0.1 Hz"), so 25 kHz is used for both.
- The presynaptic channel of a file is the one whose sweeps cross `SPIKE_MV` within
  `SPIKE_WINDOW_MS` of the first pulse. The files name Elec_8 as the stimulated electrode in
  every file, which the traces contradict (see the notebook), so the cell that fires is used.
  `SPIKE_MV` = 0 mV is a standard overshoot criterion for an action potential.
- A channel holds a cell when its pre-stimulus mean is below `CELL_MAX_MV` (-30 mV); an empty
  channel reads 0 mV. A standard choice: the Methods hold cells at -60 or -70 mV.
- Cell types, the presynaptic and postsynaptic channels tested, and the annotated connections
  (ConnType, connQuality) come from the paper's code, metadata_multiPatch.xlsx in
  https://github.com/RFLiu2021/AIC_proj at commit 44cd8a6dfbb1f1ce363d73742e4f3652086b0f9d
  (claims file, fig5d-connectivity-totals criterion, reading b). Its rows are matched to the
  dandiset through the NWB file name it lists.
- The averaged response is processed as in the paper's Fig5fg_plotConn.m (claims file,
  fig5fg-example-slice): averaged over sweeps and low-passed with a 2nd-order Butterworth at
  300 Hz applied forward and backward (PatchAnaLab filter_300Lowpass). It is kept at 25 kHz;
  the code's resampling to 1 kHz only changes the plotted sampling.
- `response_stats` measures, on the averaged postsynaptic trace, the peak deflection from the
  pre-pulse baseline in `RESP_WINDOW_MS` after the first pulse and the s.d. of the trace in
  `BASE_WINDOW_MS` before it. The paper gives no detection rule (claims file); these windows
  are a description chosen here (a 1 to 15 ms window holds the latency of a monosynaptic
  uPSP), and they decide no outcome.
"""

from __future__ import annotations

import hashlib
import io
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import requests
from dandi.dandiapi import DandiAPIClient
from scipy.signal import butter, filtfilt

DANDISET_ID = "001751"
DANDISET_VERSION = "0.260825.0222"

CODE_COMMIT = "44cd8a6dfbb1f1ce363d73742e4f3652086b0f9d"
CODE_TABLE_URL = ("https://raw.githubusercontent.com/RFLiu2021/AIC_proj/" + CODE_COMMIT
                  + "/ephysio/data_ephy/rawdata_ephysio/metadata_multiPatch.xlsx")

RATE_HZ = 25_000.0
PULSE_SAMPLE = 5000        # first pulse onset in every file (checked in the notebook)
SPIKE_MV = 0.0
SPIKE_WINDOW_MS = (0.0, 8.0)
CELL_MAX_MV = -30.0
BASE_WINDOW_MS = (-50.0, -1.0)
RESP_WINDOW_MS = (1.0, 15.0)
KEEP_MS = (-60.0, 200.0)   # part of each averaged trace that is kept around the first pulse
LOWPASS_HZ = 300.0


def asset_table() -> pd.DataFrame:
    """Path, size, subject and streaming URL of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        rows = []
        for a in ds.get_assets():
            if not a.path.endswith(".nwb"):
                continue
            rows.append(dict(path=a.path, file=a.path.split("/")[-1], size=a.size,
                             subject=a.path.split("/")[0].removeprefix("sub-"),
                             url=a.get_content_url(follow_redirects=1, strip_query=True)))
    return pd.DataFrame(rows).sort_values("path").reset_index(drop=True)


def _s(v):
    v = v[()] if isinstance(v, h5py.Dataset) else v
    if isinstance(v, bytes):
        return v.decode()
    if isinstance(v, np.ndarray) and v.dtype == object:
        return [x.decode() if isinstance(x, bytes) else x for x in v]
    return v


def lowpass(x: np.ndarray, fs: float = RATE_HZ) -> np.ndarray:
    """2nd-order Butterworth at 300 Hz, forward and backward (PatchAnaLab filter_300Lowpass)."""
    b, a = butter(2, LOWPASS_HZ / (fs / 2))
    return filtfilt(b, a, x, axis=-1)


def _ms(ms: float) -> int:
    return int(round(ms * RATE_HZ / 1000.0))


def read_file(url: str) -> dict:
    """Stream one file into memory and reduce it to metadata, per-channel sweep statistics and
    the averaged (unfiltered) trace around the first pulse."""
    raw = requests.get(url, timeout=600).content
    f = h5py.File(io.BytesIO(raw), "r")
    out = dict(session_id=_s(f["general/session_id"]),
               subject_id=_s(f["general/subject/subject_id"]),
               sex=_s(f["general/subject/sex"]), age=_s(f["general/subject/age"]),
               start=_s(f["session_start_time"])[0] if f["session_start_time"].shape else None)
    elec = {}
    for e, g in f["general/intracellular_ephys"].items():
        elec[e] = {k: _s(g[k]) for k in g if isinstance(g[k], h5py.Dataset)}
    out["electrodes"] = elec
    stims = []
    for name, g in f["stimulus/presentation"].items():
        d = g["data"][:]
        on = np.flatnonzero(np.diff((d > 0).astype(int)) == 1) + 1
        stims.append(dict(name=name, electrode=g.get("electrode", getlink=True).path,
                          n=len(d), unit=g["data"].attrs.get("unit"), max=float(d.max()),
                          onsets=on.tolist(),
                          widths=(np.flatnonzero(np.diff((d > 0).astype(int)) == -1) + 1 - on).tolist()
                          if len(on) else [],
                          rate=float(g["starting_time"].attrs.get("rate", np.nan)),
                          rate_unit=g["starting_time"].attrs.get("unit")))
    out["stimuli"] = stims
    sweeps: dict[int, dict[int, np.ndarray]] = {}
    resp_rate = set()
    for name, g in f["acquisition"].items():
        parts = name.split("_")
        r, ch = int(parts[2]), int(parts[4])
        sweeps.setdefault(ch, {})[r] = g["data"][:] * float(g["data"].attrs.get("conversion", 1.0))
        resp_rate.add((float(g["starting_time"].attrs.get("rate", np.nan)),
                       g["data"].attrs.get("unit")))
    out["response_rate_unit"] = sorted(resp_rate)
    lo, hi = PULSE_SAMPLE + _ms(KEEP_MS[0]), PULSE_SAMPLE + _ms(KEEP_MS[1])
    b0, b1 = PULSE_SAMPLE + _ms(BASE_WINDOW_MS[0]), PULSE_SAMPLE + _ms(BASE_WINDOW_MS[1])
    s0, s1 = PULSE_SAMPLE + _ms(SPIKE_WINDOW_MS[0]), PULSE_SAMPLE + _ms(SPIKE_WINDOW_MS[1])
    chans = {}
    for ch, reps in sorted(sweeps.items()):
        lens = {len(v) for v in reps.values()}
        n = min(lens)
        M = np.array([reps[r][:n] for r in sorted(reps)]) * 1e3   # mV
        chans[ch] = dict(
            n_sweeps=M.shape[0], n_samples=n,
            base_mv=float(M[:, b0:b1].mean()),
            vmin=float(M.min()), vmax=float(M.max()),
            frac_spiking=float((M[:, s0:s1].max(axis=1) > SPIKE_MV).mean()),
            peak_after_pulse=float(np.median(M[:, s0:s1].max(axis=1))),
            avg=M.mean(axis=0)[lo:hi].astype(np.float32),
            digest=hashlib.sha1(np.ascontiguousarray(M).tobytes()).hexdigest())
    out["channels"] = chans
    f.close()
    return out


def read_all(urls: list[str], workers: int = 8) -> list[dict]:
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(read_file, urls))


def presynaptic_channel(rec: dict) -> int | None:
    """The channel that fires on the first pulse in most sweeps (None if none does)."""
    cands = [(c["frac_spiking"], ch) for ch, c in rec["channels"].items()
             if c["base_mv"] < CELL_MAX_MV]
    best = max(cands, default=(0, None))
    return best[1] if best[0] >= 0.5 else None


def response_stats(avg: np.ndarray) -> dict:
    """Peak deflection after the first pulse and baseline s.d. of an averaged trace (mV), after
    the 300 Hz low-pass of Fig5fg_plotConn.m. `avg` starts KEEP_MS[0] before the pulse."""
    x = lowpass(avg.astype(float))
    z = -_ms(KEEP_MS[0])
    base = x[z + _ms(BASE_WINDOW_MS[0]): z + _ms(BASE_WINDOW_MS[1])]
    resp = x[z + _ms(RESP_WINDOW_MS[0]): z + _ms(RESP_WINDOW_MS[1])] - base.mean()
    i = int(np.argmax(np.abs(resp)))
    return dict(peak_mv=float(resp[i]), latency_ms=RESP_WINDOW_MS[0] + i * 1000.0 / RATE_HZ,
                base_sd_mv=float(base.std()), snr=float(abs(resp[i]) / base.std()))


def code_table() -> pd.DataFrame:
    """metadata_multiPatch.xlsx, one row per ordered pair, with the file-level columns filled
    down to every pair of the file."""
    raw = requests.get(CODE_TABLE_URL, timeout=120).content
    t = pd.read_excel(io.BytesIO(raw), sheet_name="metadata_multiPatch")
    t = t.rename(columns={"Session_ID/SliceID": "slice", "filename_original(.dat)": "dat",
                          "posySynChannel": "postSynChannel"})
    for c in ["Subject_id", "slice", "dat", "filename", "preSynChannel"]:
        t[c] = t[c].ffill()
    t["slice_nconn"] = t["Nr_Conn"]
    t = t.dropna(subset=["postSynChannel"]).copy()
    for c in ["preSynChannel", "postSynChannel"]:
        t[c] = t[c].astype(int)
    t["connected"] = t["ConnType"].notna()
    return t.reset_index(drop=True)


TYPE_NAME = {"PC": "PC", "VEN": "VEN", "GABA": "IN"}


def pair_class(pre: str, post: str) -> str:
    return f"{TYPE_NAME.get(pre, pre)}-to-{TYPE_NAME.get(post, post)}"
