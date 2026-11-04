"""Loading and measures for CRCNS data set ac-2 (DeWeese and Zador 2004, J Neurophysiol 92:1840).

The data set is two gzipped tar files in the public S3 bucket crcnsarchive. A tar.gz cannot be
read by range, so `load()` streams the data tar once, in memory, and keeps only what the analyses
need; nothing is written to disk.

What the data set holds (checked in the notebook): for each of the 33 anesthetized neurons,
`rmat_and_lfpmat.mat` with `r` and `lfp` (one 150-ms trace per tone presentation, 600 samples at
4 kHz, tone onset at 15 ms, each relative to the mean of its first 15 ms; `rbaseline` and
`lfpbaseline` hold those means), `all_sweeps_both_channels.mat` with the 8-s sweeps (16 tones per
sweep), and `cell_specific_parameters.m` with the cycles of the stable epoch, a spike threshold
and the LFP gain correction. The docs tar holds `neuron_recording_info.mat` (anesthetic, access
resistance, depth, prepulse, gain corrections, LFP flag). Six TTX recordings and one awake
recording are Igor binary waves (`ep_*.ibw`).

Where the parameters come from:

- Tone order, sampling rate, trace layout, prepulse, gain corrections: the data set's
  documentation (Anesthetized_cell_info.txt, neuron_recording_info.mat).
- Trials used: the cycles `first_cycle` to `last_cycle` of each neuron's
  cell_specific_parameters.m. The paper requires "at least 10 consecutive repetitions" in a
  stable recording (Methods, LFP and whole cell patch-clamp recording, paragraph 3); the files
  give the stable epoch of each neuron, and its length is the number of repetitions (assumption,
  checked against the paper's 10 to 63 range in the notebook).
- PSP height (`heights`): Methods, Quantifying response variability: the peak of the trace in
  the 10-ms window centred on the peak of the trial-averaged PSP, minus the mean of the 15 ms
  before onset. The window searched for the mean's peak is open (claims file, open detail 1):
  `peak_window="after_onset"` (the whole trace after onset) or `"culling"` (the 100-ms culling
  window).
- q = variance / mean of the heights (`ddof=1`, open detail 3; `ddof=0` is the variant).
- Tone criteria: at least 10 trials and mean height above 3 mV (Methods, LFP-based culling and
  PSP-based culling procedures, paragraph 2).
- Spikes (open detail 6): the claims file names a standard threshold, "a fast rise to above
  -20 mV" (`spike_rule="claims"`): the trace, corrected by the paper's 12 mV junction potential
  (`r + rbaseline - 12`), exceeds -20 mV and its largest rise between samples exceeds 10 mV/ms
  (`SPIKE_DVDT`, a standard choice for the "fast rise"). The data set gives each neuron its own
  threshold, `spikethresh` in cell_specific_parameters.m ("height of threshold (mV) above
  BASELINE/REST for spike detection/removal", as the TTX cells' copies of the file describe it),
  applied here to `r` (`spike_rule="cell"`). Both readings are run; `"cell"`, the authors' own
  parameter, is adopted as an assumption.
- Culling (`cull`): Methods, LFP-based culling: scale factor f = (x, y)/(x, x) over the 100-ms
  window beginning 15 ms before onset, rms error to f x, threshold 0.35 times the
  peak-to-trough height of the tone's mean response (span: open detail 2, `span="culling"` or
  `"trace"`), negative scale factors removed (for PSP culling: open detail 4, `psp_negative`).
  The mean trace is over the trials that enter the culling (those without spikes).
- Heights are measured once, on the full ensemble, and are not re-measured after culling (a
  choice made here: the Methods say q is "recalculated", not that the heights are).
- When both cullings are applied, PSP-based culling comes first and LFP-based culling is then
  run on the trials it keeps, its mean LFP and threshold recomputed over them
  (`combine="sequential"`): the Figure 6 legend says "we repeat the above procedure after first
  performing the PSP-based culling procedure", and the Figure 7B legend "PSP-based culling
  followed by the LFP-based culling and estimation procedures". The variant
  `combine="intersection"` decides each culling on the full ensemble and keeps a trial when
  neither removes it.
- Estimation (`estimate_q`): Methods, LFP-based estimation procedure: linear regression of PSP
  height on the LFP scale factor over the trials left, residual sum of squares over N - 1, divided
  by the mean height. Overfitting correction: the same with heights shuffled against scale
  factors; the mean reduction over `N_SHUFFLES` shuffles (20, a standard choice; claims file,
  open detail 7) is added back. Added back per neuron or per tone, the tone average is the same
  (the mean of est + raw - shuf over tones equals mean(est) + mean(raw) - mean(shuf)), so detail
  7's per-tone reading needs no separate run.
"""

from __future__ import annotations

import hashlib
import io
import re
import struct
import tarfile

import fsspec
import numpy as np
import scipy.io as sio

DATASET = "ac-2"
DATASET_VERSION = "unversioned"
DATASET_DOI = "10.6080/K0G44N6R"
BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-2"
DATA_URL = f"{BUCKET}/crcns-ac-2.tar.gz"
DOCS_URL = f"{BUCKET}/crcns-ac-2-docs_and_scripts.tar.gz"
CHECKSUMS_URL = f"{BUCKET}/checksums.md5"
# From the data set's checksums.md5, read on 2026-11-04; the notebook compares them with the live file.
MD5 = {"crcns-ac-2.tar.gz": "af006ca3530e7f615a37d0548ba86cf2",
       "crcns-ac-2-docs_and_scripts.tar.gz": "6ffd46575e78b3f8a2ad3efb9f95008a"}

FS = 4000.0                    # samples per s (Anesthetized_cell_info.txt)
PRE = 60                       # 15 ms before tone onset in each trace
TRACE = 600                    # 150 ms
CULL_WIN = slice(0, 400)       # 100 ms beginning 15 ms before onset (Methods)
HALF_PEAK = 20                 # 10-ms window centred on the peak: +-5 ms
TONES_PER_SWEEP = 16
FIRST_ONSET = 800              # first tone 200 ms after sweep onset
TONE_STEP = 2000               # 500 ms between onsets
PRESTIM = 400                  # 100 ms before onset (Figure 8C legend)
MIN_TRIALS = 10
MIN_MEAN = 3.0                 # mV
LARGE_MEAN = 15.0              # mV, "mean responses of >= 15 mV"
CULL_THRESHOLD = 0.35
N_SHUFFLES = 20
SPIKE_ABS_MV = -20.0           # claims file, open detail 6, after the junction potential correction
JUNCTION_MV = 12.0             # Methods: "the liquid junction potential, which we calculated to be 12 mV"
SPIKE_DVDT = 10.0              # mV/ms, the "fast rise" of detail 6 (standard choice)
# Tone frequencies (Hz) in order of presentation: read from Anesthetized_cell_info.txt by `load()`.
TONE_ORDER = np.array([], int)
ANESTHETIC = {"P": "pentobarbital", "P_with_Diaz": "pentobarbital and diazepam", "U": "urethane"}


def _params(text: str) -> dict:
    out = {}
    for key, value in re.findall(r"^(\w+)\s*=\s*([^;]+);", text, re.M):
        try:
            out[key] = float(value)
        except ValueError:
            out[key] = value.strip()
    return out


def _scalar(value):
    arr = np.asarray(value)
    return float(arr) if arr.size == 1 and arr.dtype.kind in "fiu" else (str(value) if arr.dtype.kind in "UO" else np.nan)


def read_ibw(data: bytes) -> tuple[np.ndarray, float]:
    """An Igor binary wave, version 2, as the data set's readIgorFile.m reads it: (values, dx)."""
    version, = struct.unpack_from("<h", data, 0)
    if version != 2:
        raise ValueError(f"Igor binary version {version}, expected 2")
    wave = 16
    wtype, = struct.unpack_from("<h", data, wave)
    npnts, = struct.unpack_from("<i", data, wave + 2 + 4 + 20 + 8 + 8)
    hs_a, = struct.unpack_from("<d", data, wave + 2 + 4 + 20 + 8 + 8 + 4 + 2)
    dtype = {2: "<f4", 4: "<f8"}[wtype]
    values = np.frombuffer(data, dtype=dtype, count=npnts, offset=wave + 110).astype(float)
    return values, hs_a


def recording_info() -> dict:
    """neuron_recording_info.mat from the docs tar, one dict per cell name."""
    with fsspec.open(DOCS_URL, block_size=2**20) as f:
        raw = f.read()
    tf = tarfile.open(fileobj=io.BytesIO(raw), mode="r:gz")
    docs = {}
    for m in tf:
        if m.isfile():
            docs[m.name.split("/")[-1]] = tf.extractfile(m).read()
    mat = sio.loadmat(io.BytesIO(docs["neuron_recording_info.mat"]), squeeze_me=True, struct_as_record=False)
    global TONE_ORDER
    text = docs["Anesthetized_cell_info.txt"].decode("latin1")
    block = text.split("in order of presentation:")[1]
    TONE_ORDER = np.array([int(v) for v in block.split()[:32]])
    info = {}
    for rec in np.atleast_1d(mat["neuron_recording_info"]):
        info[rec.cell_name] = {f: _scalar(getattr(rec, f)) if f != "cell_name" else rec.cell_name
                               for f in rec._fieldnames}
    return {"info": info, "docs": docs, "md5": hashlib.md5(raw).hexdigest()}


class _Hashing:
    """A file object that computes the MD5 of what is read through it."""

    def __init__(self, f):
        self.f, self.md5, self.size = f, hashlib.md5(), 0

    def read(self, n=-1):
        b = self.f.read(n)
        self.md5.update(b)
        self.size += len(b)
        return b


def _members(url: str = DATA_URL, digest: dict | None = None):
    """(name, bytes) for each file of the data tar, streamed once; its MD5 goes in `digest`."""
    with fsspec.open(url, block_size=2**22) as f:
        hf = _Hashing(f)
        tf = tarfile.open(fileobj=hf, mode="r|gz")
        for m in tf:
            if m.isfile():
                yield m.name, tf.extractfile(m).read()
        while hf.read(2**22):
            pass
        if digest is not None:
            digest["crcns-ac-2.tar.gz"] = hf.md5.hexdigest()


def _reduce_neuron(name: str, raw: dict, info: dict) -> dict:
    """Keep the traces, the 100 ms before each tone from the sweeps, and sweep-level values."""
    r = raw["r"].astype(np.float32)
    lfp = raw["lfp"].astype(np.float32)
    rb = raw["rbaseline"][:, 0].astype(float)
    lb = raw["lfpbaseline"][:, 0].astype(float)
    sw = raw["all_sweeps"]
    swl = raw["all_sweeps_lfp"]
    n = r.shape[0]
    idx = np.arange(n)
    sweep, pos = np.divmod(idx, TONES_PER_SWEEP)
    start = FIRST_ONSET - PRE + TONE_STEP * pos
    # Locate each trace in its sweep: nominal position, else the best match within +-60 samples.
    offset = np.zeros(n, int)
    mismatch = np.zeros(n)
    for i in range(n):
        seg = sw[sweep[i], start[i]:start[i] + TRACE] - rb[i]
        err = np.abs(seg - r[i]).max()
        if err > 1e-3:
            errs = [np.abs(sw[sweep[i], start[i] + o:start[i] + o + TRACE] - rb[i] - r[i]).max()
                    for o in range(-60, 61)]
            offset[i] = int(np.argmin(errs)) - 60
            err = min(errs)
        mismatch[i] = err
    onset = start + offset + PRE
    pre_wc = np.stack([sw[sweep[i], onset[i] - PRESTIM:onset[i]] for i in idx]).astype(np.float32)
    pre_lfp = np.stack([swl[sweep[i], onset[i] - PRESTIM:onset[i]] for i in idx]).astype(np.float32)
    params = _params(raw["params"])
    cell = info[name]
    # Prepulse: onset and length in ms, height in pA (negative current step).
    pp_on = int(round(cell["prepulse_onset"] * FS / 1000))
    pp_len = int(round(cell["prepulse_length"] * FS / 1000))
    pp_base = int(round(cell["prepulse_baselength"] * FS / 1000))
    base = sw[:, pp_on - pp_base:pp_on].mean(1)
    steady = sw[:, pp_on + pp_len - pp_len // 5:pp_on + pp_len].mean(1)
    gain_lfp = cell["axogaincorrection_LFP"]
    gain_lfp = 1.0 if not np.isfinite(gain_lfp) else gain_lfp
    gain_wc = cell["axogaincorrection_wholecell"]
    return {
        "name": name, "params": params, "info": cell,
        "r": r / gain_wc, "lfp": lfp / gain_lfp, "rbaseline": rb / gain_wc, "lfpbaseline": lb / gain_lfp,
        "pre_wc": pre_wc / gain_wc, "pre_lfp": pre_lfp / gain_lfp,
        "sweep": sweep, "pos": pos, "cycle": idx // 32 + 1, "tone": TONE_ORDER[idx % 32],
        "onset_offset": offset, "trace_match_error": mismatch,
        "prepulse_dv": steady - base,                       # mV per sweep
        "sweep_rest": np.median(sw[:, pp_on + pp_len + int(0.05 * FS):], axis=1),  # mV per sweep
        "prestim_overlaps_prepulse": (onset - PRESTIM) < (pp_on + pp_len),
        "n_sweeps": sw.shape[0],
    }


def load(members=None) -> dict:
    """Stream the data set; return {"neurons": {name: dict}, "ttx": {name: dict}, "awake": [...], "docs": ...}."""
    meta = recording_info()
    info = meta["info"]
    neurons, ttx, awake, other = {}, {}, [], []
    pending: dict[str, dict] = {}
    digest = {"crcns-ac-2-docs_and_scripts.tar.gz": meta["md5"]}
    for name, data in (members if members is not None else _members(digest=digest)):
        parts = name.split("/")
        if "Anesthetized_wholecell_and_LFP_data" in name and len(parts) == 5:
            cell, fname = parts[3], parts[4]
            raw = pending.setdefault(cell, {})
            if fname.endswith(".m"):
                raw["params"] = data.decode("latin1")
            else:
                mat = sio.loadmat(io.BytesIO(data))
                raw.update({k: v for k, v in mat.items() if not k.startswith("__")})
            if all(k in raw for k in ("params", "r", "all_sweeps")):
                neurons[cell] = _reduce_neuron(cell, pending.pop(cell), info)
        elif "Unanesthetized_and_TTX_wholecell_data" in name and len(parts) >= 5:
            cell = parts[3]
            if cell == "121403md01":
                awake.append(parts[-1])
                continue
            rec = ttx.setdefault(cell, {"name": cell, "ep": {}, "n_stim_files": 0, "info": info.get(cell)})
            fname = parts[-1]
            if fname.endswith(".m"):
                rec["params"] = _params(data.decode("latin1"))
            elif fname.startswith("ep_") and fname.endswith(".ibw"):
                values, dx = read_ibw(data)
                rec["ep"][int(fname[3:-4])] = values.astype(np.float32)
                rec["dx"] = dx
            elif fname.startswith("tdt_"):
                rec["n_stim_files"] += 1
        else:
            other.append(name)
    for rec in ttx.values():
        g = rec["info"]["axogaincorrection_wholecell"] if rec["info"] else 1.0
        rec["ep"] = {k: v / g for k, v in sorted(rec["ep"].items())}
        rec["gain"] = g
    return {"neurons": dict(sorted(neurons.items())), "ttx": ttx, "awake_files": awake,
            "other_files": other, "info": info, "docs": meta["docs"], "unfinished": list(pending),
            "md5": digest}


# ----------------------------------------------------------------------------------------------
# Measures


def stable(neuron: dict) -> np.ndarray:
    """Trials in the stable epoch: cycles first_cycle..last_cycle of cell_specific_parameters.m."""
    p = neuron["params"]
    return (neuron["cycle"] >= p["first_cycle"]) & (neuron["cycle"] <= p["last_cycle"])


def max_rise(traces: np.ndarray) -> np.ndarray:
    """Largest rise between consecutive samples of each trace, in mV/ms."""
    return np.diff(traces, axis=1).max(1) * FS / 1000


def spikes(neuron: dict, rule: str = "claims") -> np.ndarray:
    """Trials with a spike: `claims`, a rise faster than SPIKE_DVDT and the corrected potential above
    -20 mV; `cell`, r above the cell's spikethresh."""
    if rule == "claims":
        corrected = neuron["r"] + neuron["rbaseline"][:, None] - JUNCTION_MV
        return (corrected.max(1) > SPIKE_ABS_MV) & (max_rise(neuron["r"]) > SPIKE_DVDT)
    return neuron["r"].max(1) > neuron["params"]["spikethresh"]


def heights(traces: np.ndarray, peak_window: str = "after_onset") -> tuple[np.ndarray, int, np.ndarray]:
    """PSP (or LFP) heights of the trials of one tone, with the peak index of the mean and the mean.

    Traces are already relative to the mean of their first 15 ms (checked in the notebook).
    For the LFP the peak is the largest absolute deflection of the mean, with its sign kept.
    """
    mean = traces.mean(0)
    lo, hi = (PRE, TRACE) if peak_window == "after_onset" else (PRE, CULL_WIN.stop)
    peak = lo + int(np.argmax(mean[lo:hi]))
    a, b = max(peak - HALF_PEAK, 0), min(peak + HALF_PEAK, TRACE)
    return traces[:, a:b].max(1), peak, mean


def lfp_heights(traces: np.ndarray, peak_window: str = "after_onset") -> np.ndarray:
    """LFP height: the value at the extreme of the mean LFP (largest absolute deflection) in the
    10-ms window around it, signed so that the mean response is positive."""
    mean = traces.mean(0)
    lo, hi = (PRE, TRACE) if peak_window == "after_onset" else (PRE, CULL_WIN.stop)
    peak = lo + int(np.argmax(np.abs(mean[lo:hi])))
    sign = np.sign(mean[peak]) or 1.0
    a, b = max(peak - HALF_PEAK, 0), min(peak + HALF_PEAK, TRACE)
    return (sign * traces[:, a:b]).max(1)


def q_index(h: np.ndarray, ddof: int = 1) -> float:
    return float(np.var(h, ddof=ddof) / np.mean(h))


def scale_and_error(traces: np.ndarray, span: str = "culling") -> tuple[np.ndarray, np.ndarray, float]:
    """Scale factor f = (x, y)/(x, x) and rms error of each trial to f x over the culling window,
    with the culling threshold (0.35 times the peak-to-trough height of the mean)."""
    x = traces.mean(0)
    xw = x[CULL_WIN]
    yw = traces[:, CULL_WIN]
    f = yw @ xw / (xw @ xw)
    rms = np.sqrt(((yw - f[:, None] * xw) ** 2).mean(1))
    ref = xw if span == "culling" else x
    return f, rms, CULL_THRESHOLD * float(ref.max() - ref.min())


def cull(traces: np.ndarray, span: str = "culling", drop_negative: bool = True) -> tuple[np.ndarray, np.ndarray]:
    """Boolean mask of trials kept by shape-based culling, and the scale factors."""
    f, rms, thr = scale_and_error(traces, span)
    keep = rms <= thr
    if drop_negative:
        keep &= f >= 0
    return keep, f


def estimate_q(h: np.ndarray, s: np.ndarray, ddof: int = 1) -> float:
    """q with the variance replaced by the residual of a linear fit of h on s, over N - 1."""
    if np.ptp(s) == 0:
        return q_index(h, ddof)
    m, b = np.polyfit(s, h, 1)
    resid = h - (m * s + b)
    return float((resid ** 2).sum() / (len(h) - ddof) / h.mean())


def shuffled_estimate_q(h: np.ndarray, s: np.ndarray, rng: np.random.Generator, n: int = N_SHUFFLES,
                        ddof: int = 1) -> float:
    return float(np.mean([estimate_q(rng.permutation(h), s, ddof) for _ in range(n)]))


# Main readings. spike_rule "cell" is an assumption (see the module docstring and the notebook).
DEFAULTS = {"peak_window": "after_onset", "span": "culling", "psp_negative": True,
            "spike_rule": "cell", "ddof": 1, "combine": "sequential"}


def analyse_neuron(neuron: dict, rng: np.random.Generator, with_lfp: bool = True, **options) -> list[dict]:
    """Per-tone values of every stage of the paper's procedure (Figure 6), for one neuron.

    Each row is one tone with its trials in the stable epoch, without spikes. Columns: `n`,
    `mean`, `q` (total), and for each stage the trials kept (`n_*`), the mean of their heights
    (`mean_*`) and q: `psp` (PSP-based culling), `lfp` (LFP-based culling), `lfp_est`
    (LFP-culled and estimation, uncorrected), `lfp_shuf` (the same with shuffled heights),
    `both` (PSP- and LFP-based culling), `both_est`, `both_shuf`. Inclusion is decided later.
    """
    o = {**DEFAULTS, **{k: v for k, v in options.items() if k in DEFAULTS}}
    ok = stable(neuron) & ~spikes(neuron, o["spike_rule"])
    rows = []
    for tone in TONE_ORDER:
        sel = np.flatnonzero(ok & (neuron["tone"] == tone))
        if len(sel) < 2:
            rows.append({"tone": int(tone), "n": len(sel)})
            continue
        r = neuron["r"][sel].astype(float)
        h, peak, mean = heights(r, o["peak_window"])
        row = {"tone": int(tone), "n": len(sel), "mean": float(h.mean()), "q": q_index(h, o["ddof"]),
               "cv": float(h.std(ddof=o["ddof"]) / h.mean()), "peak_ms": (peak - PRE) / FS * 1000,
               "mean_peak": float(mean[peak]), "trials": sel, "h": h}
        keep_psp, _ = cull(r, o["span"], o["psp_negative"])
        row.update(_stage("psp", h, keep_psp, o["ddof"]))
        if with_lfp:
            lf = neuron["lfp"][sel].astype(float)
            keep_lfp, s = cull(lf, o["span"], True)
            row["s"] = s
            row["lfp_h"] = lfp_heights(lf, "culling")
            row["keep_psp"], row["keep_lfp"] = keep_psp, keep_lfp
            row.update(_stage("lfp", h, keep_lfp, o["ddof"]))
            # Scale factors for the estimation after both cullings: against the mean LFP of the
            # PSP-culled trials when LFP-based culling follows PSP-based culling.
            both, s_both = keep_psp & keep_lfp, s
            if o["combine"] == "sequential":
                both, s_both = keep_psp.copy(), np.full(len(s), np.nan)
                if keep_psp.sum() >= 2:
                    both[keep_psp], s_both[keep_psp] = cull(lf[keep_psp], o["span"], True)
                else:
                    both[:] = False
            row["keep_both"] = both
            row.update(_stage("both", h, both, o["ddof"]))
            for stage, keep, sc in (("lfp", keep_lfp, s), ("both", both, s_both)):
                hk, sk = h[keep], sc[keep]
                if keep.sum() >= 3:
                    row[f"q_{stage}_est"] = estimate_q(hk, sk, o["ddof"])
                    row[f"q_{stage}_shuf"] = shuffled_estimate_q(hk, sk, rng, ddof=o["ddof"])
                    row[f"cv_{stage}_est"] = float(np.sqrt(row[f"q_{stage}_est"] * hk.mean()) / hk.mean())
        else:
            row["keep_psp"] = keep_psp
        rows.append(row)
    return rows


def _stage(name: str, h: np.ndarray, keep: np.ndarray, ddof: int) -> dict:
    hk = h[keep]
    out = {f"n_{name}": int(keep.sum())}
    if len(hk) >= 2:
        out[f"mean_{name}"] = float(hk.mean())
        out[f"q_{name}"] = q_index(hk, ddof)
        out[f"cv_{name}"] = float(hk.std(ddof=ddof) / hk.mean())
    return out


def included(row: dict, stage: str | None = None, criteria: str = "before", min_mean: float = MIN_MEAN) -> bool:
    """The tone criteria: at least 10 trials (after the stage's culling) and mean above 3 mV
    (of all trials, `criteria="before"`, or of the trials kept, `"after"`)."""
    if row["n"] < MIN_TRIALS or "mean" not in row:
        return False
    if stage is None:
        return row["mean"] > min_mean
    if row.get(f"n_{stage}", 0) < MIN_TRIALS or f"q_{stage}" not in row:
        return False
    m = row["mean"] if criteria == "before" else row[f"mean_{stage}"]
    return m > min_mean


def neuron_summary(rows: list[dict], criteria: str = "before", min_mean: float = MIN_MEAN) -> dict:
    """Tone averages <q>tones for each stage of one neuron, with the overfitting correction."""
    out = {}
    tot = [r for r in rows if included(r, None, criteria, min_mean)]
    out["n_tones"] = len(tot)
    out["q"] = np.mean([r["q"] for r in tot]) if tot else np.nan
    out["cv"] = np.mean([r["cv"] for r in tot]) if tot else np.nan
    on_both = [r for r in rows if included(r, "both", criteria, min_mean)]
    out["q_on_both_tones"] = np.mean([r["q"] for r in on_both]) if on_both else np.nan
    for stage in ("psp", "lfp", "both"):
        inc = [r for r in rows if included(r, stage, criteria, min_mean)]
        out[f"n_tones_{stage}"] = len(inc)
        out[f"q_{stage}"] = np.mean([r[f"q_{stage}"] for r in inc]) if inc else np.nan
        out[f"cv_{stage}"] = np.mean([r[f"cv_{stage}"] for r in inc]) if inc else np.nan
        if stage == "psp" or not inc or f"q_{stage}_est" not in inc[0]:
            continue
        est = np.array([r[f"q_{stage}_est"] for r in inc])
        shuf = np.array([r[f"q_{stage}_shuf"] for r in inc])
        raw = np.array([r[f"q_{stage}"] for r in inc])
        out[f"q_{stage}_est_uncorrected"] = est.mean()
        out[f"q_{stage}_shuf"] = shuf.mean()
        corr = raw.mean() - shuf.mean()
        out[f"q_{stage}_est"] = float(np.mean(est + corr))
        # CV after estimation: sqrt(corrected residual variance) / mean, per tone.
        means = np.array([r[f"mean_{stage}"] for r in inc])
        var_corr = np.clip((est + corr) * means, 0, None)
        out[f"cv_{stage}_est"] = float(np.mean(np.sqrt(var_corr) / means))
    return out


def has_lfp(neuron: dict) -> bool:
    """The data set's flag for a simultaneous LFP (`was_LFP_recorded`)."""
    return neuron["info"]["was_LFP_recorded"] == 1


def population(neurons: dict, seed: int, **options) -> dict:
    """Per-tone rows of `analyse_neuron` for every neuron; each neuron has its own generator."""
    return {name: analyse_neuron(n, np.random.default_rng([seed, i]), with_lfp=has_lfp(n), **options)
            for i, (name, n) in enumerate(neurons.items())}


def summarise(per_tone: dict, neurons: dict, criteria: str = "before", min_mean: float = MIN_MEAN):
    """One row per neuron of `neuron_summary`, with the anesthetic and the LFP flag."""
    import pandas as pd
    rows = []
    for name, tones in per_tone.items():
        s = neuron_summary(tones, criteria, min_mean)
        s.update(neuron=name, lfp=has_lfp(neurons[name]), anesthetic=neurons[name]["info"]["which_anesthetic"])
        rows.append(s)
    return pd.DataFrame(rows).set_index("neuron")


# ----------------------------------------------------------------------------------------------
# Miniature EPSPs in the TTX recordings. The paper gives no detection method (claims file,
# mepsp-size); everything below is a stated standard choice, and the notebook shows how the result
# moves with the threshold.

MINI_SKIP_S = 0.3        # skip the start of each sweep: the prepulse (25 ms + 100 ms) and its recovery
MINI_SMOOTH_MS = 1.0     # boxcar smoothing before detection
MINI_BASE_MS = 2.0       # local baseline before the event onset
MINI_PEAK_MS = 10.0      # window after onset searched for the peak
MINI_DEAD_MS = 5.0       # minimum interval between events
TEMPLATE_RISE_MS, TEMPLATE_DECAY_MS, TEMPLATE_LEN_MS = 0.5, 5.0, 20.0


def _smooth(x: np.ndarray, fs: float) -> np.ndarray:
    """Boxcar of MINI_SMOOTH_MS, with the sweep's end values repeated past its ends."""
    w = max(int(round(MINI_SMOOTH_MS * fs / 1000)), 1)
    padded = np.pad(x, (w // 2, w - 1 - w // 2), mode="edge")
    return np.convolve(padded, np.ones(w) / w, mode="valid")


def noise_sd(d: np.ndarray, rule: str = "clipped") -> float:
    """Noise SD of a derivative: `clipped`, the SD after removing values beyond 3 SD until none are
    left (the traces are digitized in 0.049-mV steps, so most differences are 0 and a median-based
    estimate can collapse); `mad`, the median absolute deviation / 0.6745."""
    if rule == "mad":
        return float(np.median(np.abs(d - np.median(d))) / 0.6745)
    x = d
    for _ in range(50):
        sd, m = x.std(), x.mean()
        kept = x[np.abs(x - m) <= 3 * sd]
        if len(kept) == len(x):
            break
        x = kept
    return float(x.std())


def _amplitudes(xs: np.ndarray, onsets: np.ndarray, fs: float) -> tuple[np.ndarray, np.ndarray]:
    """Peak in MINI_PEAK_MS after each onset minus the mean of MINI_BASE_MS before it; (onsets, sizes)."""
    b = int(MINI_BASE_MS * fs / 1000)
    p = int(MINI_PEAK_MS * fs / 1000)
    onsets = onsets[(onsets >= b) & (onsets + p < len(xs))]
    return onsets, np.array([xs[o:o + p].max() - xs[o - b:o].mean() for o in onsets])


def _dead_time(idx: np.ndarray, score: np.ndarray, fs: float) -> np.ndarray:
    dead = int(MINI_DEAD_MS * fs / 1000)
    keep, last = [], -10 ** 9
    for i in idx:
        if i - last >= dead:
            keep.append(i)
            last = i
        elif score[i] > score[keep[-1]]:
            keep[-1] = i
            last = i
    return np.array(keep, int)


def minis_derivative(x: np.ndarray, fs: float, k: float, noise: str = "clipped") -> dict:
    """Events whose smoothed derivative crosses k noise SDs (`noise_sd`): onsets, sizes, the SD."""
    xs = _smooth(x, fs)
    d = np.diff(xs)
    sd = noise_sd(d, noise)
    above = d > k * sd
    onsets = np.flatnonzero(above[1:] & ~above[:-1]) + 1
    onsets = _dead_time(onsets, d, fs)
    onsets, amps = _amplitudes(xs, onsets, fs)
    return {"onsets": onsets, "size": amps, "noise_sd": sd}


def minis_template(x: np.ndarray, fs: float, k: float) -> dict:
    """Clements and Bekkers (1997) template matching: events where the fitted scale over its
    standard error exceeds k. Sizes as peak minus local baseline, and the fitted template scale."""
    from scipy.signal import fftconvolve
    m = int(TEMPLATE_LEN_MS * fs / 1000)
    t = np.arange(m) / fs * 1000
    tmpl = (1 - np.exp(-t / TEMPLATE_RISE_MS)) * np.exp(-t / TEMPLATE_DECAY_MS)
    tmpl /= tmpl.max()
    xs = _smooth(x, fs)
    st, st2 = tmpl.sum(), (tmpl ** 2).sum()
    sy = fftconvolve(xs, np.ones(m), mode="valid")
    sy2 = fftconvolve(xs ** 2, np.ones(m), mode="valid")
    sty = fftconvolve(xs, tmpl[::-1], mode="valid")
    scale = (sty - st * sy / m) / (st2 - st ** 2 / m)
    offset = (sy - scale * st) / m
    sse = sy2 + scale ** 2 * st2 + m * offset ** 2 - 2 * scale * sty - 2 * offset * sy + 2 * scale * offset * st
    se = np.sqrt(np.clip(sse, 1e-12, None) / (m - 1))
    crit = scale / se
    above = crit > k
    starts = np.flatnonzero(above[1:] & ~above[:-1]) + 1
    # Take the best-fitting position within the dead time after each crossing.
    onsets = _dead_time(starts, crit, fs)
    dead = int(MINI_DEAD_MS * fs / 1000)
    onsets = np.array([o + int(np.argmax(crit[o:o + dead])) for o in onsets if o + dead <= len(crit)], int)
    onsets, amps = _amplitudes(xs, onsets, fs)
    return {"onsets": onsets, "size": amps, "scale": scale[onsets]}


def mini_sweeps(rec: dict, order: str = "numeric") -> dict[int, np.ndarray]:
    """The sweeps of a TTX recording in its stable epoch (first_trial..last_trial of its
    cell_specific_parameters.m), without their first MINI_SKIP_S, keyed by file number. Which file
    is trial k is not documented: `numeric`, ep_<k - 1>; `dir`, the k-th file in the name order
    that the documentation's Matlab code (dir('ep_*.ibw')) reads them in; `all`, every sweep."""
    p = rec["params"]
    skip = int(MINI_SKIP_S / rec["dx"])
    files = sorted(rec["ep"])
    if order == "dir":
        files = sorted(files, key=lambda k: f"ep_{k}.ibw")
    if order != "all":
        files = files[int(p["first_trial"]) - 1:int(p["last_trial"])]
    return {k: rec["ep"][k][skip:].astype(float) for k in files}
