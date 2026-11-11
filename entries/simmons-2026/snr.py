"""Loading and measures for dandiset 001777 (Simmons et al. 2026, Sci. Adv. 12, eadq8840).

The dandiset holds Clampex recordings of SNr neurons converted to NWB: one file per
Clampex file, each sweep a VoltageClampSeries. What each file is (virus, drugs, which
file is the control and which the drug) is written only in free text in the NWB
`notes` field, which this module parses.

Where each parameter comes from:

- VERSION: the only published version of the dandiset (no version is cited by the paper).
- Spike detection (`detect_spikes`): the paper detected spikes in Clampfit 10.3 with
  settings it does not give (claims file, M1). Here: a 4th-order 300 Hz high-pass
  (Butterworth, zero phase), a threshold of K_THRESH = 8 times the robust noise
  (median absolute deviation / 0.6745; Quiroga et al. 2004, Neural Comput.) on the
  polarity with the larger extreme, and a 4 ms dead time (the action currents have a
  second lobe 2 to 3 ms after the first, which a shorter dead time counts twice). The
  8 is a choice made here:
  in most recordings the amplitudes of threshold crossings fall into noise events under
  about 8 noise units and action currents above about 10 (shown in the notebook's data
  check), but in some files many crossings lie between 8 and 10, so there is no clean
  gap at 8 in every file. The notebook gives every rate result at 6 and 12 as well, and
  every cell's rates at the three thresholds side by side. The amplitude of each
  crossing (`spike_amplitudes`) is kept to show where a recording runs down.
- Rate per episode: spike count over the episode length (claims file, M1; code part 1).
  A cell's rate in a condition is the median of its episode rates (claims file, M1).
  Gap-free files are cut into 6-s episodes, the sweep length of the episodic files; a
  standard choice that only sets the number of episodes the median is taken over.
- Stable window: readings (a) all episodes and (b) for a drug the episodes from 6 min
  after the start of the drug's file (claims file, M1). The application time is not in
  the files; the start of the file the notes say the drug was applied in is taken as it
  (an assumption, stated in the notebook). For the control in reading (b) all control
  episodes are used, as M1 gives no rule for the control.
- IPSC amplitude: peak of the mean evoked current from the pre-stimulus baseline
  (claims file, fig1c criterion). Windows are read from the recordings: light pulses at
  0.55 s + k * 50 ms in the "20 Hz Light" protocol, the electrical pulse at 0.40 s in the
  "Five stim" protocol (shown in the notebook's data check).
"""
import hashlib
import json
import re
import urllib.request
from concurrent.futures import ProcessPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from scipy import signal

DANDISET = "001777"
VERSION = "0.260521.2201"
API = "https://api.dandiarchive.org/api"
FS = 20000.0
EPISODE_S = 6.0
K_THRESH = 8.0
THRESHOLDS = (6.0, 8.0, 12.0)
DEAD_S = 0.004
DRUG_STABLE_S = 360.0  # claims file, M1 reading (b): 6 min after the start of application


def list_assets():
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000"
    out = []
    while url:
        with urllib.request.urlopen(url, timeout=60) as r:
            d = json.load(r)
        out += d["results"]
        url = d["next"]
    return [{"path": a["path"], "asset_id": a["asset_id"], "size": a["size"]} for a in out]


def asset_url(asset_id):
    return f"{API}/assets/{asset_id}/download/"


def _open(asset_id):
    return h5py.File(remfile.File(asset_url(asset_id)), "r")


def _s(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def read_meta(asset):
    """Metadata of one file, and a fingerprint of its first sweep to find duplicates."""
    for attempt in range(3):
        try:
            f = _open(asset["asset_id"])
            g = f["general"]
            r = dict(asset)
            r["protocol"] = _s(f["session_description"][()])
            r["start"] = pd.Timestamp(_s(f["session_start_time"][()]))
            r["notes"] = _s(g["notes"][()])
            sub = g["subject"]
            r["subject"] = _s(sub["subject_id"][()])
            r["genotype"] = _s(sub["genotype"][()])
            r["sex"] = _s(sub["sex"][()])
            r["age"] = _s(sub["age"][()])
            el = g["intracellular_ephys"]
            r["location"] = ";".join(
                _s(el[k]["location"][()]) for k in el if isinstance(el[k], h5py.Group) and "location" in el[k]
            )
            acq = f["acquisition"]
            keys = sorted(acq)
            r["n_sweeps"] = len(keys)
            d0 = acq[keys[0]]["data"]
            r["sweep_len"] = d0.shape[0]
            r["rate_hz"] = float(acq[keys[0]]["starting_time"].attrs["rate"])
            r["unit"] = _s(d0.attrs["unit"])
            r["conversion"] = float(d0.attrs["conversion"])
            r["last_sweep_t0"] = float(acq[keys[-1]]["starting_time"][()])
            first = d0[:4000]
            r["fingerprint"] = f"{len(keys)}-{d0.shape[0]}-" + hashlib.md5(first.tobytes()).hexdigest()
            r["first_mean"] = float(np.mean(first))
            return r
        except OSError:
            if attempt == 2:
                raise


def survey(assets, workers=12):
    with ProcessPoolExecutor(workers) as ex:
        rows = list(ex.map(read_meta, assets))
    return pd.DataFrame(rows).sort_values("path").reset_index(drop=True)


# ---------------------------------------------------------------- notes

def _nums(txt):
    return [int(n) for n in re.findall(r"\d{3}", txt)]


def parse_notes(notes):
    """Fields of the free-text notes: original file number, virus, drugs, file roles."""
    m = {}
    for line in notes.split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            m[k.strip()] = v.strip()
    p = re.sub(r"\s+", " ", m.get("Protocol notes", "")).replace("FIle", "File")
    out = {
        "orig": int(re.search(r"_(\d{4})\.abf", m.get("Original file", "_9999.abf")).group(1)),
        "orig_file": m.get("Original file"),
        "virus": m.get("Virus", "None"),
        "pnotes": p,
        "temperature": (re.search(r"Temperature: ([^.]*)\.", p) or [None, None])[1],
        "whole_cell": p.startswith("Whole cell"),
    }
    # windows given in the gap-free files' notes
    w = re.search(r"Baseline Rate Measurement from (\d+)s to (\d+)s? in File (\d+)", p)
    w2 = re.search(r"Gabazine Rate Measurement from (\d+)s to (\d+)s? in File (\d+)", p)
    out["note_ctrl_window"] = (int(w[1]), int(w[2]), int(w[3])) if w else None
    out["note_drug_window"] = (int(w2[1]), int(w2[2]), int(w2[3])) if w2 else None
    ctrl, drug1, drug2 = [], [], []
    applied = re.findall(r"applied (?:in )?\(?(?:Files?|Episodes?) ([\d, and]+)", p)
    if applied:
        drug1 = _nums(applied[0])
        if len(applied) > 1:
            drug2 = _nums(applied[1])
    c = re.search(r"\((?:Files?) ([\d, and]+)\)", p) or re.search(r"\bin File (\d+)\. ", p)
    if c:
        ctrl = _nums(c[1])
    if out["note_ctrl_window"]:
        ctrl = [out["note_ctrl_window"][2]]
        drug1 = [out["note_drug_window"][2]]
    if "(Part 2/2)" in p:
        out["part"] = 2
    elif "(Part 1/2)" in p:
        out["part"] = 1
    else:
        out["part"] = None
    out["ctrl_files"], out["drug1_files"], out["drug2_files"] = ctrl, drug1, drug2
    return out


def experiment(r):
    """The experiment a file belongs to, from its protocol, virus and notes."""
    p, v = r["pnotes"], r["virus"]
    if r["protocol"].startswith("20 Hz Light"):
        return "gpe_opto_ipsc_quinpirole"
    if r["protocol"].startswith("Five stim"):
        return "gpe_gi_ipsc_cno"
    if r["protocol"].startswith("30 Hz Light"):
        if "Rasagiline" in p:
            return "rasagiline_gabazine"
        return "gpe_train_quinpirole" if "Chronos" in v else "quinpirole_no_opsin"
    if "shRNA" in v:
        return "shrna_gabazine"
    if "GFAP-hM4Di" in v:
        return "astro_gi_gabazine_cno" if "Gabazine (File" in p else "astro_gi_cno"
    if "hM4D(Gi)" in v:
        return "gpe_gi_rate_cno"
    if "DIO-hM4Di" in v:
        return "snc_gi_snr_rate_cno"
    if "SNAP-5114" in p:
        return "snap5114_quinpirole" if "Quinpirole" in p else "snap5114"
    if "NNC-711 bath applied" in p:
        return "nnc711"
    if "NNC-711" in p:
        return "nnc711_gabazine"
    if "DEAB" in p:
        return "deab_gabazine" if "Gabazine" in p else "deab_baseline"
    if "Disulfiram bath applied" in p:
        return "disulfiram_acute"
    if "Disulfiram" in p:
        return "disulfiram_gabazine"
    if "Gabazine" in p:
        return "gabazine"
    return "other"


def build_files(meta):
    """One row per distinct recording: notes parsed, duplicates marked."""
    rows = []
    for _, r in meta.iterrows():
        d = dict(r)
        d.update(parse_notes(r["notes"]))
        d["date"] = r["start"].strftime("%Y-%m-%d")
        rows.append(d)
    df = pd.DataFrame(rows)
    df["experiment"] = df.apply(experiment, axis=1)
    df = df.sort_values(["subject", "start", "path"]).reset_index(drop=True)
    df["duplicate_of"] = None
    seen = {}
    for i, r in df.iterrows():
        if r["fingerprint"] in seen:
            df.at[i, "duplicate_of"] = seen[r["fingerprint"]]
        else:
            seen[r["fingerprint"]] = r["path"]
    return df


def build_cells(files):
    """Group the files of each experiment into cells, in recording order.

    Within a subject, date and experiment, files are taken in order of their start time.
    A file is a control when its number is a control file in its own notes (or its notes
    say Part 1/2), and a drug file otherwise. A new cell starts at a control file, or
    when the original file number does not increase. A file whose number is in neither
    list of its own notes is kept with the cell before it, and flagged.
    """
    f = files[files["duplicate_of"].isna()].copy()
    f["family"] = np.where(f["n_sweeps"] == 1, "gap-free", "episodic")
    cells = []
    for (subj, date, exp, fam), g in f.groupby(["subject", "date", "experiment", "family"], sort=True):
        g = g.sort_values("start")
        cur, prev = None, None
        for _, r in g.iterrows():
            n = r["orig"]
            if r["part"] == 1:
                role = "ctrl"
            elif r["part"] == 2:
                role = "drug1"
            elif r["note_ctrl_window"] and r["note_ctrl_window"][2] == r["note_drug_window"][2] == n:
                role = "both"
            elif n in r["ctrl_files"]:
                role = "ctrl"
            elif n in r["drug2_files"]:
                role = "drug2"
            elif n in r["drug1_files"]:
                role = "drug1"
            else:
                role = "unlisted"
            new = cur is None or role in ("ctrl", "both") or (prev is not None and n <= prev)
            if exp.startswith("gpe_opto"):
                # the 20 Hz IPSC protocol keeps several consecutive files per condition;
                # a gap in the file numbers starts a new cell
                new = cur is None or n - prev > 1
            if new:
                cur = {"subject": subj, "date": date, "experiment": exp, "family": fam, "ctrl": [], "drug1": [], "drug2": [],
                       "both": [], "unlabelled": [], "flags": [], "genotype": r["genotype"], "sex": r["sex"], "age": r["age"],
                       "virus": r["virus"], "temperature": r["temperature"]}
                cells.append(cur)
            if role == "unlisted":
                cur["flags"].append(f"file {n:04d} is not named in its own notes")
                role = "drug1" if (cur["ctrl"] or cur["drug1"]) else "ctrl"
                if exp.startswith("gpe_opto"):
                    role = "unlabelled"
            cur[role].append(r["path"])
            prev = n
    out = pd.DataFrame(cells)
    out["cell"] = [f"{r.subject}-{r.date}-{i}" for i, r in out.iterrows()]
    return out


# ---------------------------------------------------------------- spikes

_SOS = signal.butter(4, 300.0, btype="highpass", fs=FS, output="sos")


def detect_spikes(x, k=K_THRESH, polarity=None):
    """Spike sample indices in one trace (pA). Returns (indices, polarity, noise)."""
    y = signal.sosfiltfilt(_SOS, np.asarray(x, dtype=np.float64))
    noise = np.median(np.abs(y)) / 0.6745
    if polarity is None:
        polarity = -1 if -np.percentile(y, 0.01) > np.percentile(y, 99.99) else 1
    z = polarity * y
    above = z > k * noise
    on = np.flatnonzero(above[1:] & ~above[:-1]) + 1
    keep, last = [], -10**9
    dead = int(DEAD_S * FS)
    for i in on:
        if i - last >= dead:
            keep.append(i)
            last = i
    return np.asarray(keep, dtype=np.int64), polarity, noise


def spike_amplitudes(y, idx):
    """Peak (pA) of the high-passed current, on the spike polarity, in the 2 ms after each
    threshold crossing."""
    n = int(0.002 * FS)
    return np.array([y[i:i + n].max() for i in idx], dtype=np.float32)


def file_spikes(asset_id, ks=THRESHOLDS):
    """Spike times (s) and amplitudes (pA) of every sweep at several thresholds; gap-free
    files give one sweep.

    The polarity is fixed per file from its first sweep, so that a sweep without spikes
    does not flip it.
    """
    for attempt in range(3):
        try:
            f = _open(asset_id)
            acq = f["acquisition"]
            keys = sorted(acq)
            out = {"asset_id": asset_id, "n_sweeps": len(keys), "spikes": {k: [] for k in ks},
                   "amps": {k: [] for k in ks}, "noise": [], "sweep_s": None, "t0": []}
            pol = None
            for key in keys:
                x = acq[key]["data"][:]
                out["sweep_s"] = len(x) / FS
                out["t0"].append(float(acq[key]["starting_time"][()]))
                y = None
                for k in ks:
                    idx, p, noise = detect_spikes(x, k, pol)
                    if pol is None:
                        pol = p
                    if y is None:
                        y = pol * signal.sosfiltfilt(_SOS, np.asarray(x, dtype=np.float64))
                    out["spikes"][k].append(idx / FS)
                    out["amps"][k].append(spike_amplitudes(y, idx))
                out["noise"].append(noise)
            out["polarity"] = pol
            return out
        except OSError:
            if attempt == 2:
                raise


def all_spikes(asset_ids, workers=8):
    with ProcessPoolExecutor(workers) as ex:
        res = list(ex.map(file_spikes, asset_ids))
    return {r["asset_id"]: r for r in res}


def episode_rates(sp, k=K_THRESH, window=None):
    """Rates (Hz) per episode. Episodic files: one per sweep, over `window` (s) of the
    sweep or the whole sweep. Gap-free files: consecutive 6-s episodes.
    Returns (rates, episode start times in s from the file's start)."""
    if sp["n_sweeps"] == 1 and sp["sweep_s"] > 60:
        t = sp["spikes"][k][0]
        n = int(sp["sweep_s"] // EPISODE_S)
        counts = np.histogram(t, bins=np.arange(n + 1) * EPISODE_S)[0]
        return counts / EPISODE_S, np.arange(n) * EPISODE_S
    a, b = window if window else (0.0, sp["sweep_s"])
    rates = np.array([np.sum((t >= a) & (t < b)) / (b - a) for t in sp["spikes"][k]])
    return rates, np.asarray(sp["t0"])


def episode_amplitudes(sp, k=6.0):
    """Median amplitude (pA) of the threshold crossings in each episode, cut as in
    `episode_rates` (NaN for an episode without crossings)."""
    med = lambda a: float(np.median(a)) if len(a) else np.nan
    if sp["n_sweeps"] == 1 and sp["sweep_s"] > 60:
        t, a = sp["spikes"][k][0], sp["amps"][k][0]
        n = int(sp["sweep_s"] // EPISODE_S)
        return np.array([med(a[(t >= i * EPISODE_S) & (t < (i + 1) * EPISODE_S)]) for i in range(n)])
    return np.array([med(a) for a in sp["amps"][k]])


def failed_cells(rate_tables):
    """Cells whose rate in a condition falls under a quarter of their rate in the condition
    before it (drug1 against ctrl, drug2 against drug1), in any of the given rate tables.

    No drug in the paper is reported to change SNr rate by more than about 50%, and in
    the cells this finds the action currents shrink to the noise before the rate falls
    (shown in the notebook), so these are taken as recordings that failed (loss of the
    cell-attached seal or of the cell). The quarter is a choice made here; the outcomes
    are given with and without these cells."""
    bad = {}
    for x in rate_tables:
        for _, c in x.iterrows():
            if c["drug1"] < 0.25 * c["ctrl"] or c["drug2"] < 0.25 * c["drug1"]:
                bad.setdefault(c["cell"], c["experiment"])
    return bad


def condition_rate(sp_list, offsets, reading, drug=False, k=K_THRESH, window=None, explicit=None):
    """Median episode rate of a condition over its files (claims file, M1).

    `offsets`: start of each file in s from the start of the condition's first file.
    reading 'a': all episodes. reading 'b': for a drug, episodes from 6 min after the start
    of the first drug file (the whole drug period when shorter); for a control, all
    episodes. `explicit` = (t_start, t_end) restricts a single gap-free file to a window."""
    rates, times = [], []
    for sp, offset in zip(sp_list, offsets):
        r, t = episode_rates(sp, k, window)
        rates.append(r)
        times.append(t + offset)
    r = np.concatenate(rates) if rates else np.array([])
    t = np.concatenate(times) if times else np.array([])
    if explicit is not None:
        sel = (t >= explicit[0]) & (t + EPISODE_S <= explicit[1])
        return float(np.median(r[sel])) if sel.any() else np.nan
    if reading == "b" and drug:
        sel = t >= DRUG_STABLE_S
        if sel.any():
            r = r[sel]
    return float(np.median(r)) if len(r) else np.nan


# ---------------------------------------------------------------- evoked currents

def file_sweeps_mean(asset_id, t0=0.0, t1=None, max_sweeps=None):
    """Mean and per-sweep current (pA) over [t0, t1) s of each sweep."""
    for attempt in range(3):
        try:
            f = _open(asset_id)
            acq = f["acquisition"]
            keys = sorted(acq)[:max_sweeps]
            a = int(t0 * FS)
            b = None if t1 is None else int(t1 * FS)
            X = np.array([acq[k]["data"][a:b] for k in keys], dtype=np.float64)
            return {"asset_id": asset_id, "X": X, "t0": t0}
        except OSError:
            if attempt == 2:
                raise


def all_sweeps(asset_ids, t0, t1, workers=8):
    with ProcessPoolExecutor(workers) as ex:
        res = list(ex.map(file_sweeps_mean, asset_ids, [t0] * len(asset_ids), [t1] * len(asset_ids)))
    return {r["asset_id"]: r for r in res}


def ipsc_peak(trace, t0, stim, base=(-0.02, -0.001), win=(0.001, 0.025), base_trace_at=None):
    """Amplitude (pA, positive for an inward/outward peak of either sign measured as the
    largest deflection below baseline) of the evoked current after `stim` (s).

    Baseline: mean current over `base` relative to `stim`, or relative to `base_trace_at`
    when given (paired-pulse reading b). Peak: minimum of the current in `win` after
    `stim`. With a Cs+ CsCl/CsMeSO3 pipette at -60 to -70 mV GABA-A currents are inward,
    so the peak is the minimum."""
    i = lambda s: int(round((s - t0) * FS))
    ref = stim if base_trace_at is None else base_trace_at
    b = np.mean(trace[i(ref + base[0]):i(ref + base[1])])
    pk = np.min(trace[i(stim + win[0]):i(stim + win[1])])
    return b - pk


def cell_rates(cells, files, spikes, reading="a", k=K_THRESH, window=None, note_windows=False):
    """Rate (Hz) of every cell in each condition: ctrl, drug1, drug2.

    `files` is indexed by path. `window` restricts episodic sweeps to part of the sweep.
    `note_windows`: for gap-free files whose notes give the measurement windows, use them
    (a variant). A single file holding both conditions (role 'both') is always measured
    in the windows its notes give, the only record of when the drug was applied."""
    rows = []
    for _, c in cells.iterrows():
        row = {"cell": c["cell"], "subject": c["subject"], "experiment": c["experiment"],
               "family": c["family"], "date": c["date"]}
        if c["both"]:
            p = c["both"][0]
            sp = spikes[files.loc[p, "asset_id"]]
            cw, dw = files.loc[p, "note_ctrl_window"], files.loc[p, "note_drug_window"]
            row["ctrl"] = condition_rate([sp], [0.0], "a", k=k, explicit=cw[:2])
            row["drug1"] = condition_rate([sp], [0.0], "a", k=k, explicit=dw[:2])
            row["drug2"] = np.nan
            rows.append(row)
            continue
        for cond in ("ctrl", "drug1", "drug2"):
            paths = c[cond]
            if not paths:
                row[cond] = np.nan
                continue
            starts = [files.loc[p, "start"] for p in paths]
            offs = [(s - starts[0]).total_seconds() for s in starts]
            sps = [spikes[files.loc[p, "asset_id"]] for p in paths]
            explicit = None
            if note_windows and len(paths) == 1:
                w = files.loc[paths[0], "note_ctrl_window" if cond == "ctrl" else "note_drug_window"]
                if w is not None:
                    explicit = w[:2]
            row[cond] = condition_rate(sps, offs, reading, drug=cond != "ctrl", k=k, window=window,
                                       explicit=explicit)
        rows.append(row)
    return pd.DataFrame(rows)


def paired_summary(df, a="ctrl", b="drug1"):
    """Paired comparison of two conditions over cells: tests and the three readings of
    percent change of the claims file (M2): (a) mean over cells of each cell's percent
    change, (b) percent change of the group means, (c) median over cells of each cell's
    percent change. Cells with a control rate of zero have no percent change and are
    counted."""
    from scipy import stats

    d = df.dropna(subset=[a, b])
    x, y = d[a].to_numpy(float), d[b].to_numpy(float)
    ok = x > 0
    pc = (y[ok] - x[ok]) / x[ok] * 100
    out = {"n": len(d), "n_subjects": d["subject"].nunique() if "subject" in d else np.nan,
           f"mean_{a}": x.mean(), f"mean_{b}": y.mean(), "mean_diff": (y - x).mean()}
    if len(d) >= 2:
        t = stats.ttest_rel(y, x)
        out.update(t=t.statistic, p_paired_t=t.pvalue,
                   p_paired_t_greater=stats.ttest_rel(y, x, alternative="greater").pvalue,
                   p_paired_t_less=stats.ttest_rel(y, x, alternative="less").pvalue)
        try:
            out["p_wilcoxon"] = stats.wilcoxon(y, x).pvalue
        except ValueError:
            out["p_wilcoxon"] = np.nan
    out.update(pct_a_mean_of_cells=pc.mean() if len(pc) else np.nan,
               pct_b_of_means=(y.mean() - x.mean()) / x.mean() * 100,
               pct_c_median_of_cells=np.median(pc) if len(pc) else np.nan,
               n_zero_ctrl=int((~ok).sum()))
    return out


def evoked_amplitudes(X, t0, stim, base, win, sign=None):
    """Amplitude of the evoked current in the mean of sweeps X (pA): extreme of the mean
    current in `win` after `stim`, from the mean over `base` (both relative to `stim`, s).
    The sign (+1 outward, -1 inward) is fixed per cell from its control (`sign`); the
    IPSCs here are outward in some cells and inward in others (holding potentials in the
    notes run from -50 to -70 mV against a CsMeSO3 or CsCl pipette)."""
    m = X.mean(0)
    i = lambda s: int(round((s - t0) * FS))
    b = m[i(stim + base[0]):i(stim + base[1])].mean()
    seg = m[i(stim + win[0]):i(stim + win[1])] - b
    if sign is None:
        sign = 1 if seg.max() > -seg.min() else -1
    return float(sign * seg.max() if sign > 0 else -seg.min()), sign
