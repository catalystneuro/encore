"""Loading and measures for dandiset 001177 and the behavioural data published with it.

Zhuang, Lemak, Sridhar & Nelson (2025), Brain 149:238, doi:10.1093/brain/awaf312.

The dandiset holds 56 NWB files of open-field recordings in the dorsomedial striatum of 18 mice
(D1-Cre or A2a-Cre, injected with 6-OHDA or saline), each with up to four pramipexole (PPX)
sessions and, in four mice, a saline session. Each file holds the raw 30 kHz voltage of 32
channels, split into one to six `ElectricalSeries` segments, a 1 kHz LFP, and, in 54 files, the
threshold crossings of each channel (`SpikeEvents_Electrode_<n>`: timestamps and 48-sample
waveforms). Two files (E0 day 4 and P4 day 1) hold a `units` table in place of the threshold
crossings. No file holds sorted units with cell types, optogenetic labels, laser times or the
time of the injection. Files are streamed from the archive at the pinned version; nothing is
written to disk.

The behavioural data, rotarod scores and histology the paper reports were deposited on Zenodo
(doi:10.5281/zenodo.15258978) and are read from there into memory.

Where the parameters come from:

- Firing-rate classification follows the paper's Supplementary methods ("In vivo
  electrophysiology"): 1-min bins; baseline -30 to 0 min; two post-injection periods, 241-270
  and 271-300 min; a Wilcoxon signed-rank test at p < 0.01 in each; "increase" or "decrease"
  when both periods change significantly in the same direction, otherwise "no change". The
  signed-rank test pairs the bins in their order, as the Methods name a paired test.
- The injection time is not in the files. `injection_minute` infers it from the recording
  segments and the subject description ("following a 30-minute baseline period"); this is an
  assumption of this attempt, checked against the firing rates in the notebook.
- Multi-unit activity is the count of threshold crossings per channel, a substitute chosen here
  because sorted units are not in the dandiset. `MIN_BASELINE_HZ` (a common choice) excludes
  channels with almost no crossings.
- Delay discounting follows the Supplementary methods and the paper's analysis code
  (ICD-Cognitive-Analysis, doi:10.5281/zenodo.10703140, commit 5528e22): free-choice blocks are
  B3, B6, B9 and B12 (delays 0, 3, 6 and 9 s, with 20 trials each, in the task software
  ICD-Cognitive-Arduino, doi:10.5281/zenodo.10703132, commit f7cff8b); a session's choice is the percentage of
  free-choice trials with a reward that delivered the large reward (omissions excluded);
  sessions are averaged per animal within a condition (Summary_Cognitive.m); the hyperbola
  V = A / (1 + K D) is fitted per animal by least squares from A = 1, K = 0.5
  (Summary_Cognitive.m fits the percentages; here V is a fraction, so A is the intercept as a
  fraction, as in the paper's V = 100 A / (1 + K D)); AUC is the trapezoid integral of the fitted
  curve over the four delays.
- The rotarod and histology tables are read as deposited; the corrected fluorescence follows
  the Supplementary methods ("Histology"): (RawIntDen - Area x mean background) / Area.
"""

from __future__ import annotations

import io
import re
import zipfile
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from dandi.dandiapi import DandiAPIClient
from scipy import optimize, stats

DANDISET_ID = "001177"
DANDISET_VERSION = "0.250902.2127"

ZENODO_DATA = "https://zenodo.org/records/15258978/files/"     # doi:10.5281/zenodo.15258978
COGNITIVE_ZIP = "Data_ICD_Fig1&2&5&6_CognitiveAssay.zip"
ROTAROD_XLSX = "Data_ICD_Fig1_Rotarod_PPX.xlsx"
HISTOLOGY_XLSX = "Data_ICD_Fig3_HistologyQuantification_striatum_raw.xlsx"

BIN_S = 60.0
BASELINE_MIN = (-30.0, 0.0)
POST_MIN = [(241.0, 270.0), (271.0, 300.0)]
ALPHA = 0.01
MIN_BASELINE_HZ = 0.5
FS = 30000.0

DELAYS = np.array([0.0, 3.0, 6.0, 9.0])
FREE_BLOCKS = {3: 0.0, 6: 3.0, 9: 6.0, 12: 9.0}


# --- the dandiset ---------------------------------------------------------------------------

def _text(value) -> str:
    if isinstance(value, bytes):
        return value.decode("utf-8", "replace")
    return str(value)


def asset_urls() -> list[tuple[str, str]]:
    """(path, streaming URL) of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in dandiset.get_assets() if a.path.endswith(".nwb"))


def _session_fields(path: str) -> dict:
    name = path.split("/")[1].removesuffix("_ecephys.nwb")
    m = re.search(r"-day(\d)", name)
    return {"session": name.split("_ses-")[1],
            "drug": "saline" if "Saline" in name else "PPX",
            "day": int(m.group(1)) if m else 0,
            "opto_only": "optoSession" in name}


def read_session(item: tuple[str, str]) -> dict:
    """Metadata, recording segments and the spike-event layout of one file (no spike data)."""
    path, url = item
    with h5py.File(remfile.File(url), "r") as f:
        subj = f["general/subject"]
        desc = _text(subj["description"][()])
        lesion = "6-OHDA" if "of 6-OHDA" in desc else ("saline" if "of saline" in desc else "?")
        segments = []
        for name, series in f["acquisition"].items():
            if name.startswith("ElectricalSeries"):
                start = float(series["starting_time"][()])
                rate = float(series["starting_time"].attrs["rate"])
                segments.append((start / 60, series["data"].shape[0] / rate / 60))
        segments.sort()
        events = {}
        for name, series in f["acquisition"].items():
            if name.startswith("SpikeEvents_Electrode_"):
                ts = series["timestamps"]
                assert ts.chunks is None and ts.compression is None and ts.dtype == "<f8"
                events[int(name.rsplit("_", 1)[1])] = (ts.id.get_offset(), ts.shape[0])
        n_units = f["units/id"].shape[0] if "units" in f else 0
        locations = sorted({_text(x) for x in f["general/extracellular_ephys/electrodes/location"][:]})
        stimulus = {k: sorted(f["stimulus"][k].keys()) for k in f["stimulus"]} if "stimulus" in f else {}
        unit_columns = sorted(f["units"].keys()) if "units" in f else []
        other = {"intervals": "intervals" in f, "analysis": sorted(f["analysis"].keys()),
                 "processing": {k: sorted(f["processing"][k].keys()) for k in f["processing"]}}
        return {"path": path, "url": url, "subject": _text(subj["subject_id"][()]),
                "genotype": "D1-Cre" if "Drd1" in _text(subj["genotype"][()]) else "A2a-Cre",
                "genotype_raw": _text(subj["genotype"][()]), "sex": _text(subj["sex"][()]),
                "lesion": lesion, "group": {"6-OHDA": "Park", "saline": "Ctrl"}.get(lesion, "?"),
                "description": desc, "start_time": _text(f["session_start_time"][()]),
                "session_id": _text(f["general/session_id"][()]),
                "segments": segments, "events": events, "n_units": n_units, "locations": locations,
                "stimulus": stimulus, "unit_columns": unit_columns, **other,
                **_session_fields(path)}


def sessions(workers: int = 16) -> list[dict]:
    """`read_session` for every file, in processes (h5py serialises threads)."""
    with ProcessPoolExecutor(workers) as pool:
        return list(pool.map(read_session, asset_urls()))


def injection_minute(segments: list[tuple[float, float]]) -> float:
    """Minute of the i.p. injection, inferred from the recording segments (an assumption).

    A recording that is one long segment (over 240 min) is taken to have its injection 30 min
    after the start, as the subject description says. Otherwise the injection is taken to fall
    in the first gap after at least 29 min have been recorded, and the post-injection clock
    starts at the beginning of the next segment.
    """
    first_start, first_len = segments[0]
    if first_len > 240:
        return first_start + 30.0
    for (s0, l0), (s1, _) in zip(segments, segments[1:]):
        if s0 + l0 - first_start >= 29.0:
            return s1
    return float("nan")


def _fetch(url: str, offset: int, n: int) -> np.ndarray:
    if n == 0:
        return np.zeros(0)
    r = requests.get(url, headers={"Range": f"bytes={offset}-{offset + 8 * n - 1}"}, timeout=600)
    r.raise_for_status()
    out = np.frombuffer(r.content, dtype="<f8")
    if out.shape[0] != n:
        raise IOError(f"short read: {out.shape[0]} of {n} timestamps")
    return out


def event_times(session: dict, threads: int = 16) -> dict[int, np.ndarray]:
    """Timestamps (s) of the threshold crossings of each channel, read as raw byte ranges.

    The timestamp datasets are contiguous and uncompressed (checked in `read_session`), so they
    are read directly at their offsets in the file; `check_event_read` compares this with h5py.
    """
    keys = sorted(session["events"])
    with ThreadPoolExecutor(threads) as pool:
        arrays = pool.map(lambda k: _fetch(session["url"], *session["events"][k]), keys)
        return dict(zip(keys, arrays))


def check_event_read(session: dict, channel: int) -> bool:
    with h5py.File(remfile.File(session["url"]), "r") as f:
        ref = f[f"acquisition/SpikeEvents_Electrode_{channel}/timestamps"][:]
    return bool(np.array_equal(ref, _fetch(session["url"], *session["events"][channel])))


def unit_times(session: dict) -> dict[int, np.ndarray]:
    with h5py.File(remfile.File(session["url"]), "r") as f:
        idx = np.r_[0, f["units/spike_times_index"][:]]
        st = f["units/spike_times"][:]
        ids = f["units/id"][:]
    return {int(i): st[a:b] for i, a, b in zip(ids, idx[:-1], idx[1:])}


def minute_counts(times: dict[int, np.ndarray], t0_min: float,
                  span_min: tuple[float, float] = (-60.0, 330.0)) -> pd.DataFrame:
    """Counts per 1-min bin, rows = minutes relative to the injection (bin start), cols = channel."""
    edges = (t0_min + np.arange(span_min[0], span_min[1] + 1)) * 60.0
    data = {k: np.histogram(v, bins=edges)[0] for k, v in times.items()}
    return pd.DataFrame(data, index=np.arange(span_min[0], span_min[1]).astype(int))


def covered_minutes(segments: list[tuple[float, float]], t0_min: float, index,
                    span: tuple[float, float] = (-np.inf, np.inf)) -> np.ndarray:
    """True for the 1-min bins that lie wholly inside a recorded segment and inside `span`
    (minutes), the time range the spike events actually cover."""
    rel = np.asarray(index, float)
    ok = np.zeros(rel.shape, bool)
    for s, l in segments:
        lo, hi = max(s, span[0]), min(s + l, span[1])
        ok |= (rel + t0_min >= lo) & (rel + 1 + t0_min <= hi)
    return ok


def change_point(total_per_min: np.ndarray, lo: int = 20, hi: int = 120) -> tuple[int, float]:
    """Minute (from the file start) after which the summed rate drops most: argmin over t of
    log(mean rate t+2..t+22 / mean rate t-20..t). Returns (minute, log ratio)."""
    best = (-1, np.inf)
    for t in range(lo, min(hi, len(total_per_min) - 22) + 1):
        pre, post = total_per_min[t - 20:t].mean(), total_per_min[t + 2:t + 22].mean()
        if pre > 0 and post > 0 and np.log(post / pre) < best[1]:
            best = (t, float(np.log(post / pre)))
    return best


def acute_drop(total_per_min: np.ndarray, t0: float) -> float:
    """log(mean rate 2-22 min after t0 / mean rate up to 30 min before t0), from absolute
    minutes; NaN when fewer than 20 min precede t0."""
    i = int(np.floor(t0))
    if i < 20 or i + 22 > len(total_per_min):
        return np.nan
    pre, post = total_per_min[max(0, i - 30):i].mean(), total_per_min[i + 2:i + 22].mean()
    return float(np.log(post / pre)) if pre > 0 and post > 0 else np.nan


def session_activity(session: dict) -> dict:
    """Everything the notebook needs from one file's threshold crossings, reduced as it loads.

    Absolute 1-min totals (all channels), the range of the timestamps, the share of events
    outside the recorded segments, the inferred and change-point injection times, and per-channel
    1-min counts relative to each of them (-60 to 330 min; `counts_rule`, `counts_cp`, with the
    bins inside the recording in `covered_rule`, `covered_cp`).
    """
    times = event_times(session)
    end = max(s + l for s, l in session["segments"])
    nonempty = [v for v in times.values() if len(v)]
    tmin = min(v[0] for v in nonempty) / 60 if nonempty else np.nan
    tmax = max(v[-1] for v in nonempty) / 60 if nonempty else np.nan
    allt = np.concatenate(nonempty) / 60 if nonempty else np.zeros(0)
    inside = np.zeros(allt.shape, bool)
    for s, l in session["segments"]:
        inside |= (allt >= s - 0.05) & (allt <= s + l + 0.05)
    edges = np.arange(0, np.ceil(end) + 1) * 60.0
    total = np.histogram(allt * 60, bins=edges)[0] / BIN_S
    t0 = injection_minute(session["segments"])
    cp = change_point(total)
    out = {"path": session["path"], "n_channels": len(times), "n_events": int(allt.size),
           "t_first_min": tmin, "t_last_min": tmax, "end_min": end,
           "outside_share": float((~inside).mean()) if allt.size else np.nan,
           "sorted": all(bool(np.all(np.diff(v) >= 0)) for v in nonempty),
           "total_per_min": total, "t0": t0, "cp": cp[0], "cp_drop": cp[1],
           "drop_at_t0": acute_drop(total, t0) if np.isfinite(t0) else np.nan}
    for key, t in (("rule", t0), ("cp", float(cp[0]))):
        if np.isfinite(t) and t >= 0:
            out["counts_" + key] = minute_counts(times, t)
            out["covered_" + key] = covered_minutes(session["segments"], t, out["counts_" + key].index,
                                                    span=(tmin, tmax))
    return out


def classify(counts: pd.Series, covered: np.ndarray | None = None, alpha: float = ALPHA,
             post=POST_MIN, paired: bool = True) -> tuple[str, float, float, float]:
    """The paper's response type of one channel or unit from its 1-min counts.

    Returns (type, baseline rate Hz, rate 241-300 min Hz, ratio). Bins outside the recording are
    dropped; a window with fewer than 25 recorded bins gives "missing". `paired=False` uses the
    rank-sum test as a variant.
    """
    c = counts if covered is None else counts[covered]
    idx = c.index.to_numpy()
    base = c[(idx >= BASELINE_MIN[0]) & (idx < BASELINE_MIN[1])].to_numpy(float)
    posts = [c[(idx >= lo - 1) & (idx < hi)].to_numpy(float) for lo, hi in post]
    if len(base) < 25 or any(len(p) < 25 for p in posts):
        return "missing", np.nan, np.nan, np.nan
    signs = []
    for p in posts:
        if paired:
            n = min(len(base), len(p))
            b, q = base[-n:], p[:n]
            if np.all(b == q):
                pval = 1.0
            else:
                pval = stats.wilcoxon(q, b).pvalue
        else:
            pval = stats.mannwhitneyu(p, base).pvalue
        signs.append(float(np.sign(p.mean() - base.mean())) if pval < alpha else 0.0)
    rb = base.mean() / BIN_S
    rp = np.concatenate(posts).mean() / BIN_S
    kind = "increase" if signs == [1, 1] else ("decrease" if signs == [-1, -1] else "no change")
    return kind, rb, rp, (rp / rb if rb > 0 else np.nan)


def fisher_freeman_halton(table: np.ndarray, n_perm: int, rng: np.random.Generator) -> float:
    """Monte Carlo p-value of the r x c exact test (Freeman-Halton), by the table probability."""
    table = np.asarray(table, int)
    rows = np.repeat(np.arange(table.shape[0]), table.sum(1))
    cols = np.repeat(np.arange(table.shape[1]), table.sum(0))

    def logp(t):
        from scipy.special import gammaln
        return (gammaln(t.sum(1) + 1).sum() + gammaln(t.sum(0) + 1).sum()
                - gammaln(t.sum() + 1) - gammaln(t + 1).sum())

    observed = logp(table)
    hits = 0
    for _ in range(n_perm):
        perm = np.zeros_like(table)
        np.add.at(perm, (rows, rng.permutation(cols)), 1)
        hits += logp(perm) <= observed + 1e-9
    return (hits + 1) / (n_perm + 1)


# --- the behavioural data on Zenodo ---------------------------------------------------------

def _get(name: str) -> bytes:
    r = requests.get(ZENODO_DATA + requests.utils.quote(name) + "?download=1", timeout=600)
    r.raise_for_status()
    return r.content


def cognitive_files() -> dict[str, dict[str, bytes]]:
    """{experiment: {file name: bytes}} of the delay-discounting sessions, kept in memory."""
    outer = zipfile.ZipFile(io.BytesIO(_get(COGNITIVE_ZIP)))
    out = {}
    for name in outer.namelist():
        if name.startswith("__MACOSX") or not name.endswith(".zip"):
            continue
        experiment = name.rsplit("/", 1)[1].removesuffix(".zip").removeprefix("Data_ICD_")
        inner = zipfile.ZipFile(io.BytesIO(outer.read(name)))
        out[experiment] = {n.rsplit("/", 1)[1]: inner.read(n) for n in inner.namelist()
                           if not n.startswith("__MACOSX") and n.lower().endswith(".csv")}
    return out


def readme_groups() -> dict[str, dict[str, list[str]]]:
    """Animal IDs per group, from README_ICD_CognitiveAssessment.txt on Zenodo."""
    text = _get("README_ICD_CognitiveAssessment.txt").decode("utf-8", "replace")
    section, out, last = None, {}, None
    for line in text.splitlines():
        line = line.strip()
        if line.endswith("-related experiments"):
            section, last = line.split("-related")[0], None
            out[section] = {}
        elif section and last and out[section][last][-1:] == [""]:
            out[section][last] = out[section][last][:-1] + [i.strip() for i in line.split(",")]
        elif section and ":" in line and not line.startswith(("-", "Citation")):
            label, ids = line.split(":", 1)
            last = label.split("(")[0].strip()
            out[section][last] = [i.strip() for i in ids.split(",")]
        else:
            last = None
    return {s: {g: [i for i in ids if i] for g, ids in groups.items()} for s, groups in out.items()}


def classify_file(name: str) -> tuple[str, str, str | None] | None:
    """(animal, condition, date as YYMMDD) of a delay-discounting session file, else None."""
    low = name.lower().replace(" ", "")
    if "delay" not in low:
        return None
    animal = name.split("_")[0]
    if "washout" in low or "washont" in low:
        cond = "washout"
    elif "ppx" in low or "a77636" in low or "cno" in low:
        cond = "drug"
    else:
        cond = "baseline"
    m = re.search(r"_(\d{6})(?=[_.]|csv)", name, re.I)
    date = None
    if m:
        mm, dd, yy = m.group(1)[:2], m.group(1)[2:4], m.group(1)[4:]
        date = yy + mm + dd
    return animal, cond, date


def parse_session(raw: bytes) -> dict[float, dict]:
    """Counts per free-choice block (B3, B6, B9, B12, at the paper's delays 0, 3, 6 and 9 s).

    Large and small rewards, centre and side omissions, trials, and the delay written in the
    block's own label when it has one (some sessions label their blocks "B3_free_0s" and so
    on; most write only "B3_"). Blocks after B12 are ignored.
    """
    out = {d: {"large": 0, "small": 0, "center_omission": 0, "side_omission": 0, "trials": 0,
               "present": False, "labelled_delay": np.nan} for d in FREE_BLOCKS.values()}
    block = None
    for line in raw.decode("utf-8", "replace").splitlines()[1:]:
        parts = [p.strip() for p in line.split(",")]
        if len(parts) < 3:
            continue
        event = parts[-2]
        m = re.fullmatch(r"B(\d+)_(.*)", event)
        if m:
            block = int(m.group(1))
            if block in FREE_BLOCKS:
                b = out[FREE_BLOCKS[block]]
                b["present"] = True
                lab = re.search(r"(\d+)s$", m.group(2))
                if lab:
                    b["labelled_delay"] = float(lab.group(1))
            continue
        if block not in FREE_BLOCKS:
            continue
        b = out[FREE_BLOCKS[block]]
        if event == "trial start":
            b["trials"] += 1
        elif event == "l reward delivery":
            b["large"] += 1
        elif event == "s reward delivery":
            b["small"] += 1
        elif event == "center omi":
            b["center_omission"] += 1
        elif event == "side omi":
            b["side_omission"] += 1
    return out


def session_table(files: dict[str, bytes]) -> pd.DataFrame:
    """One row per session file and free-choice block; `order` numbers the sessions of an
    animal within a condition by date."""
    rows = []
    for name, raw in files.items():
        c = classify_file(name)
        if c is None:
            continue
        animal, cond, date = c
        for delay, b in parse_session(raw).items():
            chosen = b["large"] + b["small"]
            rows.append({"file": name, "animal": animal, "condition": cond, "date": date,
                         "delay": delay, **b,
                         "pct_large": 100.0 * b["large"] / chosen if chosen else np.nan})
    df = pd.DataFrame(rows)
    order = (df.drop_duplicates("file").sort_values(["animal", "condition", "date", "file"])
             .assign(order=lambda d: d.groupby(["animal", "condition"]).cumcount() + 1))
    return df.merge(order[["file", "order"]], on="file")


def animal_curves(table: pd.DataFrame, animals: list[str], condition: str,
                  orders: list[int] | None = None) -> pd.DataFrame:
    """Animals x delays: the mean over an animal's sessions in a condition of the percentage of
    large-reward choices (Summary_Cognitive.m averages the rows of each animal). `orders`
    selects sessions by their date order within the condition (1 = first)."""
    t = table[table.animal.isin(animals) & (table.condition == condition)]
    if orders is not None:
        t = t[t.order.isin(orders)]
    wide = t.groupby(["animal", "delay"]).pct_large.mean().unstack("delay")
    return wide.reindex(columns=DELAYS)


def fit_table(curves: pd.DataFrame) -> pd.DataFrame:
    """A, K and AUC per animal (rows of `curves`)."""
    return pd.DataFrame([fit_curve(curves.loc[a].to_numpy()) for a in curves.index],
                        index=curves.index, columns=["A", "K", "AUC"])


def hyperbola(d, a, k):
    return a / (1.0 + k * d)


def fit_curve(pct: np.ndarray) -> tuple[float, float, float]:
    """A, K and AUC of V = A / (1 + K D) fitted to one animal's four choice fractions."""
    y = np.asarray(pct, float) / 100.0
    if np.any(~np.isfinite(y)):
        return np.nan, np.nan, np.nan
    try:
        (a, k), _ = optimize.curve_fit(hyperbola, DELAYS, y, p0=[1.0, 0.5], maxfev=10000)
    except RuntimeError:
        return np.nan, np.nan, np.nan
    auc = np.trapezoid(hyperbola(DELAYS, a, k), DELAYS)
    return a, k, auc


def rm_anova_2x4(wide_a: pd.DataFrame, wide_b: pd.DataFrame) -> dict:
    """Two-way repeated-measures ANOVA (condition x delay, both within animal).

    wide_a and wide_b: animals x delays for the two conditions, same animals and order.
    """
    y = np.stack([wide_a.to_numpy(float), wide_b.to_numpy(float)], axis=1)   # n x 2 x 4
    n, a, b = y.shape
    gm = y.mean()
    ss = lambda arr: float((arr ** 2).sum())
    m_s = y.mean((1, 2)); m_a = y.mean((0, 2)); m_b = y.mean((0, 1))
    m_sa = y.mean(2); m_sb = y.mean(1); m_ab = y.mean(0)
    ss_a = n * b * ss(m_a - gm)
    ss_b = n * a * ss(m_b - gm)
    ss_ab = n * ss(m_ab - m_a[:, None] - m_b[None, :] + gm)
    ss_sa = b * ss(m_sa - m_s[:, None] - m_a[None, :] + gm)
    ss_sb = a * ss(m_sb - m_s[:, None] - m_b[None, :] + gm)
    resid = y - m_sa[:, :, None] - m_sb[:, None, :] - m_ab[None] + m_s[:, None, None] \
        + m_a[None, :, None] + m_b[None, None, :] - gm
    ss_sab = ss(resid)
    out = {}
    for name, s_eff, df_eff, s_err, df_err in [
            ("condition", ss_a, a - 1, ss_sa, (a - 1) * (n - 1)),
            ("delay", ss_b, b - 1, ss_sb, (b - 1) * (n - 1)),
            ("interaction", ss_ab, (a - 1) * (b - 1), ss_sab, (a - 1) * (b - 1) * (n - 1))]:
        f = (s_eff / df_eff) / (s_err / df_err)
        out[name] = (f, df_eff, df_err, stats.f.sf(f, df_eff, df_err))
    return out


def paired_by_delay(wide_a: pd.DataFrame, wide_b: pd.DataFrame) -> pd.DataFrame:
    """Per delay: means, paired t-test and Bonferroni-adjusted p (x4), and Wilcoxon as a variant."""
    rows = []
    for d in wide_a.columns:
        x, y = wide_a[d].to_numpy(float), wide_b[d].to_numpy(float)
        t = stats.ttest_rel(x, y)
        w = stats.wilcoxon(x, y) if np.any(x != y) else None
        rows.append({"delay_s": d, "n": len(x), "mean_a": x.mean(), "mean_b": y.mean(),
                     "diff": (y - x).mean(), "t": t.statistic,
                     "p_bonferroni": min(1.0, t.pvalue * len(wide_a.columns)),
                     "p_wilcoxon_bonferroni": min(1.0, w.pvalue * len(wide_a.columns)) if w else 1.0})
    return pd.DataFrame(rows)


def friedman_dunn(table: pd.DataFrame, pairs: list[tuple[str, str]]) -> tuple[float, dict]:
    """Friedman test over the columns of `table` (animals x conditions) and Dunn's post hoc.

    Dunn's z for two conditions is the difference of mean ranks over sqrt(k (k + 1) / (6 n));
    the p-values are multiplied by the number of pairs given.
    """
    t = table.dropna()
    n, k = t.shape
    fr = stats.friedmanchisquare(*[t[c] for c in t.columns]).pvalue if k > 2 else np.nan
    ranks = t.rank(axis=1).mean()
    se = np.sqrt(k * (k + 1) / (6.0 * n))
    out = {}
    for a, b in pairs:
        z = (ranks[b] - ranks[a]) / se
        out[(a, b)] = (z, min(1.0, 2 * stats.norm.sf(abs(z)) * len(pairs)))
    return fr, out


def kruskal_dunn(groups: dict[str, np.ndarray], pairs: list[tuple]) -> tuple[float, dict]:
    """Kruskal-Wallis over the groups and Dunn's post hoc for the given pairs (p x len(pairs)).

    A side of a pair may be a tuple of group names, which are pooled for that comparison
    using their ranks in the joint ranking.
    """
    names = list(groups)
    values = np.concatenate([np.asarray(groups[n], float) for n in names])
    labels = np.concatenate([[n] * len(groups[n]) for n in names])
    ranks = stats.rankdata(values)
    n_all = len(values)
    h = stats.kruskal(*[groups[n] for n in names]).pvalue
    out = {}
    for a, b in pairs:
        sel = lambda side: np.isin(labels, side if isinstance(side, tuple) else (side,))
        ra, rb = ranks[sel(a)], ranks[sel(b)]
        se = np.sqrt(n_all * (n_all + 1) / 12.0 * (1 / len(ra) + 1 / len(rb)))
        z = (ra.mean() - rb.mean()) / se
        out[(a, b)] = (z, min(1.0, 2 * stats.norm.sf(abs(z)) * len(pairs)))
    return h, out


def rotarod() -> pd.DataFrame:
    """Long table of latency to fall (s) per column group of the deposited rotarod sheet."""
    x = pd.read_excel(io.BytesIO(_get(ROTAROD_XLSX)), header=None)
    rows = []
    for col in x.columns:
        name = x.iloc[0, col]
        if not isinstance(name, str):
            continue
        vals = pd.to_numeric(x.iloc[2:, col], errors="coerce").dropna()
        rows += [{"column": name, "row": int(i), "latency_s": float(v)} for i, v in vals.items()]
    return pd.DataFrame(rows)


def histology_sheets() -> dict[str, pd.DataFrame]:
    return pd.read_excel(io.BytesIO(_get(HISTOLOGY_XLSX)), sheet_name=None, header=None)


def histology_rois(sheets: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """One row per ROI measurement: cohort, group, animal, slice, ROI label, Area, Mean, RawIntDen."""
    rows = []
    for cohort, df in sheets.items():
        r = 0
        while r < len(df):
            head = df.iloc[r, 0]
            if isinstance(head, str) and "sections" in head.lower():
                group = "Park" if head.lower().startswith("park") else "Ctrl"
                labels_row = r
                # find the label column (first column whose next rows hold "left str-1")
                block_end = r + 2
                while block_end < len(df) and isinstance(df.iloc[block_end, 0], str) \
                        and "sections" not in df.iloc[block_end, 0].lower() \
                        and not df.iloc[block_end, 0].lower().startswith("note"):
                    block_end += 1
                for c in range(1, df.shape[1]):
                    sl = df.iloc[labels_row, c]
                    if not isinstance(sl, str) or df.iloc[labels_row + 1, c] != "Area":
                        continue
                    animal = re.split(r"[_-]sl|[_ ]sli|_s", sl, maxsplit=1)[0].strip()
                    for rr in range(labels_row + 2, block_end):
                        lab = df.iloc[rr, 0]
                        vals = pd.to_numeric(df.iloc[rr, c:c + 3], errors="coerce").to_numpy()
                        if not isinstance(lab, str) or np.any(~np.isfinite(vals)):
                            continue
                        rows.append({"cohort": cohort, "group": group, "animal": animal,
                                     "slice": sl, "roi": re.sub(r"-\d+$", "", lab.strip()),
                                     "area": vals[0], "mean": vals[1], "rawintden": vals[2]})
                r = block_end
            else:
                r += 1
    return pd.DataFrame(rows)
