"""Loading and measures for dandiset 001968 (Nakagawa et al. 2026, Nature Neuroscience,
doi:10.1038/s41593-026-02260-w): LEC tetrode units and LEC dopamine-fiber photometry.

What the files hold (version 0.260914.1316):

- 3814 unit files. Each holds one sorted unit: its spike times (s), a source `meanFR` (Hz, "not
  recalculated"), the tetrode, the cluster and the name of the source MAT file. The name carries
  the strain label (WT, AD, NLGF), the mouse, the date, the odor set (for example ABEF) and a cell
  class label (RS or FS), as in `spikeFile_LEC_WT_mouse00364_190808_ABST_RS_TT5_01.mat`. There are
  no trial, odor or lick times and no waveforms.
- 41 photometry files, one per session. Each holds one column per trial of 6001 samples
  (`dFoverFGCaMP`), each trial's odor code (1 to 4) and action code (1 to 4), and four tables
  `zscore_A` to `zscore_D` with five columns each. The files give no sampling rate and no cue time.

Nothing is written to disk: each file is fetched from the archive into memory and opened with
h5py. The files are small (0.2 to 14 MB), and fetching them whole is about 20 times faster
than reading them by ranges with remfile.

Where the parameters come from:

- `FS_HZ = 1000` and `CUE_SAMPLE = 1000` are an assumption, checked in the notebook: every trial
  column has mean 0 and SD 1 over samples 0 to 999, as a trace z-scored to "the 1 s before cue"
  (ref. 16 of the paper, cited by the claims file, Shared method, Photometry) would, and the
  trials' noise spectrum peaks at 120 Hz with harmonics at 180, 240 and 300 Hz under this rate,
  the mains artefact of a US laboratory.
- Odor codes 1, 2, 3, 4 are read as Odor-A, Odor-B, Odor-1, Odor-2: each file's tables
  `zscore_A` to `zscore_D` are block means of the trials of codes 1 to 4 (checked in the
  notebook), and the paper names the novel odors Odor-1 and -2 after the prelearned A and B
  (Supplementary Table 1 uses C and D for the novel pair). Action codes 1 to 4 are read as hit,
  miss, false alarm and correct rejection: 1 and 2 occur only with codes 1 and 3 (rewarded),
  3 and 4 only with codes 2 and 4 (punished), and 1 and 4 dominate the prelearned odors.
- Timepoints T1 to T5 for photometry are blocks of 10 trials of each odor type, the k-th starting
  at round(k * (n - 10) / 4) among the n trials of that odor. This is what the dataset's own
  tables hold (notebook, data check); it agrees with the claims file's T1 (first 10), T3
  (middle 10) and T5 (last 10), and with its reading T-a for T2 and T4.
- `SMOOTH_SIGMA_MS = 200`: Gaussian filter of the photometry trace (claims file, Shared method,
  Photometry, from ref. 16). The columns are already z-scored to the precue second, so dF/F is
  not recomputed.
- Windows: G1 1 to 4 s after cue (Fig. 4d legend), G2 2 to 4 s (Supplementary Table 1),
  G4 2 to 3 s (the delay period of the Methods, Spike response), G3 0.5 to 3 s (ref. 16, a
  variant only); precue -1 to 0 s (claims file, Shared method, Photometry).
- Behaviour: a correct trial is a hit or a correct rejection (Methods, Behavioral analysis,
  "as previously described"); T5 performance under reading B1 is the trials of each odor pair
  among session trials 121 to 160, under B2 the last 40 trials of each odor pair (claims file,
  Shared method, Behavioral performance). A correct session has Odor-1/2 T5 performance above
  80% (Methods), or at or above 80% (Results), both run.
- Units: the peak rate uses 50 ms bins and a Gaussian of sigma 100 ms (Methods, Spike response,
  as the claims file reads the undefined "peak rate"). The rate over the whole recording uses
  the first to the last spike, since the files give no recording start or end; the source
  `meanFR` is shown beside it.
- Animal groups come from the paper (Supplementary Table 2 and Supplementary Fig. 2), since the
  files carry no genotype, age group or treatment; see `PAPER_GROUPS`.
"""

from __future__ import annotations

import io
import re
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import requests
from scipy import stats
from scipy.ndimage import gaussian_filter1d

DANDISET_ID = "001968"
DANDISET_VERSION = "0.260914.1316"
API = "https://api.dandiarchive.org/api"

FS_HZ = 1000
CUE_SAMPLE = 1000
N_SAMPLES = 6001
SMOOTH_SIGMA_MS = 200
WINDOWS = {"G1": (1.0, 4.0), "G2": (2.0, 4.0), "G4": (2.0, 3.0), "G3": (0.5, 3.0)}
PRECUE = (-1.0, 0.0)
ODOR_NAMES = {1: "A", 2: "B", 3: "1", 4: "2"}
HIT, MISS, FA, CR = 1, 2, 3, 4

# Supplementary Table 2 (tetrode and photometry rows) and Supplementary Fig. 2 (young mice).
# Supplementary Table 2 lists 247, 690, 703, 925 and 941 as young APP-KI and 789, 1199, 1253,
# 1254 and 1517 as old APP-KI; Supplementary Fig. 2 and the Extended Data Fig. 3 legend list
# the second five as the young APP-KI mice, and the files' birth dates make the first five 7 to
# 12 months old at recording. The groups below follow Supplementary Fig. 2.
PAPER_GROUPS = {
    "young WT": ["00364", "00375", "00390", "01398", "01431"],
    "young APP-KI": ["00789", "01199", "01253", "01254", "01517"],
    "old WT": ["00210", "00310", "00346", "00387"],
    "old APP-KI": ["00247", "00690", "00703", "00925", "00941"],
    "L-DOPA": ["02427", "02474", "02475", "02477"],
    "saline": ["02490", "02491", "02492", "02493"],
    "DAT-Cre": ["00163", "00164", "00263", "00264", "00265", "00266"],
    "APP-KI x DAT-Cre": ["01028", "01029", "01416", "01451", "01477"],
}
# Sex per animal, Supplementary Table 2.
PAPER_SEX = {
    "00364": "M", "00375": "F", "00390": "F", "01398": "F", "01431": "M",
    "00247": "M", "00690": "F", "00703": "M", "00925": "M", "00941": "M",
    "00163": "M", "00164": "M", "00263": "F", "00264": "F", "00265": "M", "00266": "M",
    "01028": "F", "01029": "F", "01416": "F", "01451": "M", "01477": "M",
    "02490": "M", "02491": "M", "02492": "F", "02493": "F",
    "02427": "M", "02474": "M", "02475": "F", "02477": "F",
    "00210": "M", "00310": "F", "00346": "M", "00387": "M",
    "00789": "F", "01199": "M", "01253": "M", "01254": "M", "01517": "M",
}
# Hemispheres recorded per photometry mouse (Supplementary Table 2: * one hemisphere, else both).
PAPER_HEMISPHERES = {"00163": 1, "00164": 1, "00263": 2, "00264": 2, "00265": 2, "00266": 2,
                     "01028": 2, "01029": 2, "01416": 2, "01451": 1, "01477": 1}
# Principal cells per young mouse, Supplementary Fig. 2a.
PAPER_CELLS_PER_MOUSE = {"00364": 95, "00375": 48, "00390": 130, "01398": 112, "01431": 38,
                         "00789": 125, "01199": 52, "01253": 271, "01254": 89, "01517": 99}

_NAME = re.compile(r"LEC_(?P<label>[A-Za-z0-9]+)_mouse(?P<mouse>\d+)_(?P<date>\d{6})_"
                   r"(?P<odors>[A-Za-z0-9]+)_(?P<cls>[A-Z]+)_TT(?P<tt>\d+)_(?P<cl>\d+)(?P<sum>_Sum)?\.mat")


def group_of(mouse: str) -> str | None:
    for g, mice in PAPER_GROUPS.items():
        if mouse in mice:
            return g
    return None


def list_assets() -> pd.DataFrame:
    """Every asset of the pinned version: path, asset id, size."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=1000"
    rows = []
    while url:
        page = requests.get(url, timeout=60).json()
        rows += page["results"]
        url = page["next"]
    df = pd.DataFrame(rows)[["path", "asset_id", "size", "blob"]]
    df["subject"] = df.path.str.extract(r"sub-mouse(\d+)/")[0]
    return df


def version_summary() -> pd.DataFrame:
    """Published versions of the dandiset with their asset counts and sizes."""
    v = requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/", timeout=60).json()["results"]
    return pd.DataFrame([{"version": x["version"], "assets": x["asset_count"], "bytes": x["size"],
                          "created": x["created"][:19]} for x in v])


def version_paths(version: str) -> list[str]:
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=1000"
    out = []
    while url:
        page = requests.get(url, timeout=60).json()
        out += [a["path"] for a in page["results"]]
        url = page["next"]
    return out


def _open(asset_id: str) -> h5py.File:
    for attempt in range(4):
        try:
            r = requests.get(f"{API}/assets/{asset_id}/download/", timeout=120)
            r.raise_for_status()
            return h5py.File(io.BytesIO(r.content), "r")
        except Exception:
            if attempt == 3:
                raise


def _s(x):
    v = x[()]
    return v.decode() if isinstance(v, bytes) else v


def _read(row) -> dict:
    h = _open(row.asset_id)
    g = h["general"]
    sub = g["subject"]
    out = {"path": row.path, "subject": row.subject, "size": row.size,
           "sex": _s(sub["sex"]) if "sex" in sub else None,
           "dob": _s(sub["date_of_birth"])[:10] if "date_of_birth" in sub else None,
           "age_field": _s(sub["age"]) if "age" in sub else None,
           "genotype": _s(sub["genotype"]) if "genotype" in sub else None,
           "session_id": _s(g["session_id"]), "notes": _s(g["notes"]) if "notes" in g else "",
           "groups": sorted(h.keys())}
    if "units" in h:
        u = h["units"]
        src = u["source_file"] if "source_file" in u else u["source_mat_file"]
        rate = u["meanFR"] if "meanFR" in u else u["mean_firing_rate"]
        out.update(kind="unit", source=src[0].decode(),
                   meanFR=float(rate[0]), n_units=len(u["id"]),
                   spikes=u["spike_times"][()].astype(float))
        out["unit_columns"] = sorted(u.keys())
    elif "processing" in h and "photometry" in h["processing"]:
        p = h["processing/photometry"]
        d = p["dff_columns"]
        x = d["dFoverFGCaMP"][()]
        idx = d["dFoverFGCaMP_index"][()].astype(int)
        cols = np.split(x, idx[:-1])
        out.update(kind="photometry", trial_lengths=sorted({len(c) for c in cols}),
                   X=np.vstack(cols).astype(np.float32),
                   odor=d["odorID"][()].astype(int), action=d["actionID"][()].astype(int),
                   tables={t: p[f"zscore_{t}/z_score"][()].reshape(-1, N_SAMPLES)
                           for t in "ABCD"},
                   n_samples_axis=len(p["sample_axis/id"]))
    else:
        out.update(kind="empty", scratch="scratch" in h)
        if "notes" in g:
            m = _NAME.search(out["notes"])
            out["source"] = m.group(0) if m else None
    return out


def load_all(workers: int = 32) -> list[dict]:
    """Every file of the pinned version, read in parallel into memory."""
    assets = list_assets()
    with ThreadPoolExecutor(workers) as pool:
        return list(pool.map(_read, assets.itertuples()))


def unit_table(records: list[dict]) -> pd.DataFrame:
    """One row per unit file, with the fields parsed from its source file name."""
    rows = []
    for r in records:
        if r["kind"] != "unit":
            continue
        m = _NAME.search(r["source"])
        st = r["spikes"]
        rows.append({"path": r["path"], "mouse": r["subject"], "source": r["source"],
                     "label": m["label"], "date": m["date"], "odors": m["odors"], "cls": m["cls"],
                     "tetrode": int(m["tt"]), "cluster": int(m["cl"]), "sum_file": bool(m["sum"]),
                     "sex": r["sex"], "dob": r["dob"], "meanFR": r["meanFR"], "n_spikes": len(st),
                     "t_first": st[0] if len(st) else np.nan, "t_last": st[-1] if len(st) else np.nan,
                     "sorted": bool(np.all(np.diff(st) >= 0)),
                     "peak_rate": peak_rate(st)})
    df = pd.DataFrame(rows)
    df["session_date"] = pd.to_datetime("20" + df.date, format="%Y%m%d")
    df["age_months"] = (df.session_date - pd.to_datetime(df.dob)).dt.days / 30.44
    df["group"] = df.mouse.map(group_of)
    dur = df.t_last - df.t_first
    df["rate_span"] = np.where(dur > 0, df.n_spikes / dur, np.nan)
    return df


def peak_rate(spikes: np.ndarray, bin_s: float = 0.05, sigma_s: float = 0.1) -> float:
    """Maximum of the rate in 50 ms bins smoothed with a Gaussian of sigma 100 ms, in Hz."""
    if len(spikes) < 2:
        return np.nan
    edges = np.arange(spikes[0], spikes[-1] + bin_s, bin_s)
    counts, _ = np.histogram(spikes, edges)
    return float(gaussian_filter1d(counts.astype(float), sigma_s / bin_s).max() / bin_s)


def duplicate_units(df: pd.DataFrame) -> pd.DataFrame:
    """Pairs of unit files with the same spike train (count, first and last spike)."""
    key = list(zip(df.n_spikes, df.t_first.round(5), df.t_last.round(5)))
    d = df.assign(key=key)
    dup = d[d.duplicated("key", keep=False)].sort_values("key")
    return dup


# ---------------------------------------------------------------- photometry

def sessions_table(records: list[dict]) -> list[dict]:
    """The photometry sessions, each with its trials smoothed as in `SMOOTH_SIGMA_MS`."""
    out = []
    for r in records:
        if r["kind"] != "photometry":
            continue
        s = dict(r)
        s["mouse"] = r["subject"]
        s["date"] = r["session_id"].split("_")[-1]
        s["group"] = group_of(r["subject"])
        s["strain"] = "WT" if s["group"] == "DAT-Cre" else "APP-KI"
        s["Xs"] = gaussian_filter1d(r["X"].astype(float), SMOOTH_SIGMA_MS * FS_HZ / 1000, axis=1)
        out.append(s)
    return sorted(out, key=lambda s: (s["mouse"], s["date"]))


def block_starts(n: int) -> list[int]:
    """Start of T1 to T5 among the n trials of one odor (10 trials each)."""
    return [int(np.floor(k * (n - 10) / 4 + 0.5)) for k in range(5)]


def block_trials(session: dict, code: int, k: int, size: int = 10) -> np.ndarray:
    """Trial indices (in the session) of timepoint k (0 = T1) for odor `code`."""
    idx = np.flatnonzero(session["odor"] == code)
    start = block_starts(len(idx))[k]
    return idx[start:start + size]


def sub_block_trials(session: dict, code: int, which: str) -> np.ndarray:
    """T1a, T1b, T1c: trials 1-3, 4-6, 7-9 of an odor."""
    idx = np.flatnonzero(session["odor"] == code)
    a = {"T1a": 0, "T1b": 3, "T1c": 6}[which]
    return idx[a:a + 3]


def window_slice(t0: float, t1: float) -> slice:
    return slice(CUE_SAMPLE + int(round(t0 * FS_HZ)), CUE_SAMPLE + int(round(t1 * FS_HZ)))


def window_mean(trace: np.ndarray, window: str | tuple) -> np.ndarray:
    t0, t1 = WINDOWS[window] if isinstance(window, str) else window
    return trace[..., window_slice(t0, t1)].mean(-1)


def block_value(session: dict, code: int, k: int, window: str) -> float:
    """Mean over the block's trials of the trial-averaged signal in a window."""
    tr = block_trials(session, code, k)
    return float(window_mean(session["Xs"][tr].mean(0), window))


def precue_value(session: dict, code: int, k: int) -> float:
    tr = block_trials(session, code, k)
    return float(window_mean(session["Xs"][tr].mean(0), PRECUE))


# ---------------------------------------------------------------- behaviour

def t5_performance(session: dict, reading: str) -> dict:
    """Percent correct in T5 for the A/B and 1/2 pairs, reading B1 or B2."""
    odor, act = session["odor"], session["action"]
    correct = np.isin(act, [HIT, CR])
    out = {}
    for pair, codes in (("AB", (1, 2)), ("12", (3, 4))):
        in_pair = np.flatnonzero(np.isin(odor, codes))
        if reading == "B1":
            sel = in_pair[(in_pair >= 120) & (in_pair < 160)]
        else:
            sel = in_pair[-40:]
        out[pair] = 100 * correct[sel].mean() if len(sel) else np.nan
    return out


def first_run(flags: np.ndarray, length: int = 5) -> float:
    """Index of the first element of the first run of `length` consecutive True values."""
    run = 0
    for i, f in enumerate(flags):
        run = run + 1 if f else 0
        if run == length:
            return float(i - length + 1)
    return np.nan


# ---------------------------------------------------------------- statistics

def tukey_cells(values: pd.DataFrame, factors: list[str], mse: float, df_resid: float) -> pd.DataFrame:
    """Tukey-Kramer comparisons between all cells of a factorial design, with the ANOVA's
    error term (MATLAB multcompare over all cells, the paper's 'Tukey post hoc')."""
    cells = values.groupby(factors)["y"].agg(["mean", "count"])
    k = len(cells)
    rows = []
    names = list(cells.index)
    for i in range(k):
        for j in range(i + 1, k):
            mi, ni = cells.iloc[i]
            mj, nj = cells.iloc[j]
            se = np.sqrt(mse / 2 * (1 / ni + 1 / nj))
            q = abs(mi - mj) / se
            rows.append({"a": names[i], "b": names[j], "diff": mi - mj,
                         "p": float(stats.studentized_range.sf(q, k, df_resid))})
    return pd.DataFrame(rows)


def two_way(values: pd.DataFrame, a: str, b: str):
    """Ordinary two-way ANOVA with interaction (type II sums of squares) and Tukey over cells."""
    import statsmodels.api as sm
    from statsmodels.formula.api import ols
    model = ols(f"y ~ C({a}) * C({b})", data=values).fit()
    table = sm.stats.anova_lm(model, typ=2)
    tk = tukey_cells(values, [a, b], model.mse_resid, model.df_resid)
    return table, tk


# ---------------------------------------------------------------- tables for the claims

def block_table(sessions: list[dict]) -> pd.DataFrame:
    """One row per session, odor and timepoint (T1 to T5, and T1a to T1c): the precue and window
    means of the block's trial-averaged signal, and the session's T5 Odor-1/2 performance."""
    rows = []
    for s in sessions:
        perf = {rd: t5_performance(s, rd)["12"] for rd in ("B1", "B2")}
        for code in (1, 2, 3, 4):
            for k in range(5):
                tr = block_trials(s, code, k)
                rows.append(_block_row(s, code, f"T{k + 1}", tr, perf))
            for sub in ("T1a", "T1b", "T1c"):
                rows.append(_block_row(s, code, sub, sub_block_trials(s, code, sub), perf))
    return pd.DataFrame(rows)


def _block_row(s, code, tp, tr, perf):
    m = s["Xs"][tr].mean(0)
    r = {"mouse": s["mouse"], "date": s["date"], "session": f"{s['mouse']}_{s['date']}",
         "strain": s["strain"], "odor": ODOR_NAMES[code], "T": tp, "n_trials": len(tr),
         "pre": float(window_mean(m, PRECUE)), "perf_B1": perf["B1"], "perf_B2": perf["B2"]}
    for w in WINDOWS:
        r[w] = float(window_mean(m, w))
    return r


def per_unit(df: pd.DataFrame, unit: str) -> pd.DataFrame:
    """Sessions as units, or the mean over a mouse's sessions (unit 'mouse')."""
    if unit == "session":
        return df.assign(unit=df.session)
    cols = ["pre"] + list(WINDOWS)
    return (df.groupby(["strain", "mouse", "odor", "T"], as_index=False)[cols].mean()
            .assign(unit=lambda d: d.mouse))


def is_correct(df: pd.DataFrame, reading: str, cut: str) -> pd.Series:
    p = df[f"perf_{reading}"]
    return p > 80 if cut == ">" else p >= 80


def behaviour_table(sessions: list[dict]) -> pd.DataFrame:
    rows = []
    for s in sessions:
        for rd in ("B1", "B2"):
            p = t5_performance(s, rd)
            rows.append({"mouse": s["mouse"], "session": f"{s['mouse']}_{s['date']}",
                         "strain": s["strain"], "reading": rd, "AB": p["AB"], "12": p["12"],
                         "n_trials": len(s["odor"])})
    return pd.DataFrame(rows)
