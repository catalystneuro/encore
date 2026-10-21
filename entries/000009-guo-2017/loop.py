"""Loading and measures for dandiset 000009, Guo, Inagaki, Daie, Druckmann, Gerfen & Svoboda (2017).

"Maintenance of persistent activity in a frontal thalamocortical loop", Nature 545, 181-186,
doi:10.1038/nature22324. Files are streamed from the archive at the pinned version; nothing is
written to disk.

The dandiset holds two kinds of file:

- `*_ecephys*.nwb`: one silicon-probe session each (ALM, thalamus or SNr), with a trial table
  (trial type, outcome, pole and cue times, photostimulus period, power and galvo position) and a
  Units table (spike times, mean waveform, a cell-type label, unit position). Unit positions are
  `unit_x` = medio-lateral, `unit_y` = dorso-ventral (negative, mm), `unit_z` = antero-posterior.
- `*_behavior+icephys+ogen.nwb`: one whole-cell recording of an ALM neuron each, with the raw
  membrane potential (20 kHz), a spike-removed copy (`processing/icephys`), the injected current,
  lick traces and a trial table whose `stim_present` column marks photostimulus trials.

Where the parameters come from (the claims file is claims/000009/10.1038-nature22324.yaml; its
opening comment names the conventions E, S, P, O, V, L cited here):

- Epochs (convention E): sample is 1.3 s from pole onset (`pole_in_time`), delay from there to the
  go cue (`cue_start_time`), response 1.3 s (reading R1) or 1.5 s (R2) from the go cue. In the
  extracellular files the photostimulus starts at the delay onset (conventions P and E),
  `pole_in_time + 1.3`; those files hold no laser trace, so this is the onset used for every
  extracellular latency.
- Spike storage: within a trial the extracellular files hold spikes only to about 4.8 s after pole
  onset, whatever the delay. A trial's stored span is taken to end at the last spike of any unit
  of the session in that trial; a window that ends later is counted as missing (NaN) for that
  trial, not as a count. This follows from the data, not from a choice that can change a result.
- Whole-cell photostimulus onset: readings E and M of the claims file (`WC_ONSETS`), and the onset
  of the deposited laser trace (`stimulus/presentation/photostim_on_*`, an OptogeneticSeries at
  20 kHz), reading "L": the first sample of the trial above `LASER_FRAC` of the file's maximum.
  The fraction is a standard choice; 1% and 20% are shown alongside and move the onset by at most
  about 2 ms.
- Trials: 'lick early' and 'no response' trials are left out of every analysis (Methods,
  Behavior). Contra trials are 'lick right' (recordings and photoinhibition in the left
  hemisphere).
- Photostimulus effect (convention P): rate 20 to 120 ms after onset, contra and ipsi pooled,
  outcomes correct and incorrect (T1) or correct only (T2), units with at least 5
  photostimulation trials.
- Onsets (conventions O and V) on 1 ms bins (spikes) or 20 kHz samples (Vm), 3 SD rule.
- Spike clipping (convention V): kink where dV/dt exceeds its mean plus 3 SD over 2.5 to 1.5 ms
  before the spike peak; -0.5 to 5 ms around the kink linearly interpolated. Spike peaks are taken
  from the deposited spike-removed trace (the maximum of the raw trace in each stretch where the
  two differ); that only locates spikes, the kink and the clipping are computed here.
- VM/VAL centre for reading L2: AP -1.5, ML 0.85, DV 4.0 mm (claims file, convention L).
- Unit classes: trough-to-peak width of the deposited mean waveform (Methods), and the dataset's
  own `cell_type` label (a reading the attempt asks about, because the deposited waveforms are cut
  short).
- `BIN_S` (100 ms bins summed in pairs for the 200 ms averaging window of the time courses) and
  `PSTH_SPAN` are standard choices that cannot change a result.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET_ID = "000009"
DANDISET_VERSION = "0.220126.1903"
API = "https://api.dandiarchive.org/api"

SAMPLE_S = 1.3            # convention E
RESP_S = {"R1": 1.3, "R2": 1.5}
PW = (0.020, 0.120)       # convention P, s after photostimulus onset
PW0 = (0.0, 0.100)        # fig6d reading w2
PSTH_SPAN = (-0.1, 1.3)   # 1 ms bins around photostimulus onset (s)
BIN_S = 0.1
TC_SPAN = (-0.5, 4.1)     # 100 ms bins from pole onset, for the time courses
VMVAL_CENTRE = (0.85, -4.0)   # ML, DV (mm), convention L reading L2
KEEP = ("correct", "incorrect")
WC_RATE = 20000.0
# Photostimulus onset in the whole-cell files: "E", the claims file's convention E, 1.3 s after pole
# onset; "M", the end of the sample epoch as the Methods define it, 0.1 s after the pole starts to
# retract (`pole_out_time`); "L", the onset of the deposited laser trace. Control trials have no
# laser, so under L they are aligned at the cell's median laser onset after pole onset.
WC_ONSETS = {"E": ("pole_in", 1.3), "M": ("pole_out", 0.1), "L": ("laser", None)}
LASER_FRAC = 0.05
MASKED_WINDOWS = ("sample", "delay", "R1", "R2", "pw", "pw0", "pre")
WIDE_SPAN = (1.0, 3.0)    # s from pole onset, 1 ms samples of the deposited spike-removed Vm


def list_assets() -> pd.DataFrame:
    """Assets of the pinned version: path, asset id, size."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=1000"
    rows = requests.get(url, timeout=60).json()["results"]
    return pd.DataFrame([{"path": r["path"], "asset_id": r["asset_id"], "size": r["size"]} for r in rows])


def version_info() -> dict:
    return requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/info/", timeout=60).json()


def _open(asset_id: str) -> h5py.File:
    return h5py.File(remfile.File(f"{API}/assets/{asset_id}/download/"), "r")


def _s(x):
    return x.decode() if isinstance(x, bytes) else x


def _strings(a) -> np.ndarray:
    return np.array([_s(x) for x in a], dtype=object)


def parse_location(text: str) -> dict:
    out = {}
    for part in text.split(";"):
        if ":" in part:
            k, v = part.split(":", 1)
            out[k.strip()] = v.strip()
    return out


def trial_table(group) -> pd.DataFrame:
    cols = {}
    for c in group.keys():
        a = group[c][()]
        cols[c] = _strings(a) if a.dtype.kind == "O" else a
    return pd.DataFrame(cols)


def spike_width_ms(waveform: np.ndarray, rate: float) -> tuple[float, bool]:
    """Trough-to-peak interval of a mean waveform (ms), and whether the peak is the last sample."""
    tr = int(np.argmin(waveform))
    pk = tr + int(np.argmax(waveform[tr:]))
    return (pk - tr) / rate * 1000.0, pk == len(waveform) - 1


def stim_label(row, site: str) -> str:
    """Photostimulus condition of a trial: 'none', or '<site>:<period>:<power>'."""
    if row.photo_stim_period == "N/A":
        return "none"
    if site == "ALM" and round(row.photo_loc_galvo_x, 2) == 0.5 and round(row.photo_loc_galvo_y, 2) == 0.5:
        where = "site0.5"
    else:
        where = site
    return f"{where}:{row.photo_stim_period}:{round(float(row.photo_stim_power), 2):g}"


# ---------------------------------------------------------------- extracellular sessions

def load_ecephys(asset: dict) -> dict:
    """One silicon-probe session, reduced to what the analyses need.

    Returns metadata, the trial table (task trials only, with derived columns), a unit table, and
    per unit and trial the spike counts in each window (NaN outside the unit's trials), 100 ms bin
    counts from pole onset, the mask of the unit's trials, and 1 ms PSTH sums per (photostimulus
    condition, outcome) group with their trial counts.

    The files give no observation interval per unit, and most units hold spikes over only part of
    their session; a unit's trials are taken to run from the trial holding its first spike to the
    trial holding its last (a standard choice; the attempt records it as a deviation).
    """
    f = _open(asset["asset_id"])
    g = f["general"]
    eg = [parse_location(_s(v.attrs["location"])) for k, v in g["extracellular_ephys"].items() if k != "electrodes"]
    ogen = {}
    if "optogenetics" in g:
        for k, v in g["optogenetics"].items():
            ogen[k] = parse_location(_s(v["location"][()]))
    meta = {
        "path": asset["path"], "subject": _s(g["subject/subject_id"][()]), "genotype": _s(g["subject/genotype"][()]),
        "region": eg[0].get("brain_region"), "eg_location": eg[0], "ogen": ogen,
        "ogen_site": (list(ogen)[0].split("-", 1)[1] if ogen else None),
        "session_start": _s(f["session_start_time"][()]),
    }
    all_trials = trial_table(f["intervals/trials"])
    meta["n_rows"] = len(all_trials)
    meta["outcomes_all"] = all_trials.response.value_counts().to_dict()
    task = all_trials[np.isfinite(all_trials.pole_in_time.astype(float))].reset_index(drop=True)
    site = meta["ogen_site"] or "none"
    task["stim"] = [stim_label(r, site) for r in task.itertuples()]
    task["contra"] = task["type"] == "lick right"
    task["on"] = task.pole_in_time + SAMPLE_S
    task["cue"] = task.cue_start_time
    task["delay_s"] = task.cue - task.on

    U = f["units"]
    idx = U["spike_times_index"][()]
    st_all = U["spike_times"][()]
    starts = np.concatenate([[0], idx[:-1]])
    wf = U["waveform_mean"][()]
    rate = U["sampling_rate"][()]
    meta["unit_y_description"] = _s(U["unit_y"].attrs.get("description"))
    meta["units_description"] = _s(U.attrs.get("description"))
    units = pd.DataFrame({
        "unit_id": U["id"][()], "cell_type": _strings(U["cell_type"][()]),
        "ml": U["unit_x"][()], "dv": U["unit_y"][()], "ap": U["unit_z"][()],
        "sampling_rate": rate,
    })
    widths = [spike_width_ms(w, r) for w, r in zip(wf, rate)]
    units["width_ms"] = [w for w, _ in widths]
    units["peak_last"] = [p for _, p in widths]
    units["wf_len"] = wf.shape[1]

    on, cue, pin = task.on.values, task.cue.values, task.pole_in_time.values
    tstart, tstop = task.start_time.values, task.stop_time.values
    # end of the stored spikes in each trial: the last spike of any unit before the trial's stop
    st_sorted = np.sort(st_all)
    last = np.searchsorted(st_sorted, tstop, side="left") - 1
    last_t = st_sorted[np.clip(last, 0, len(st_sorted) - 1)] if len(st_sorted) else np.full(len(task), np.nan)
    stored_end = np.where((last >= 0) & (last_t >= tstart), last_t, np.nan)
    task["stored_end"] = stored_end
    task["stored_from_pole"] = stored_end - pin
    task["tc_ok"] = stored_end >= pin + TC_SPAN[1]
    psth_ok = stored_end >= on + PSTH_SPAN[1]
    windows = {
        "sample": (pin, pin + SAMPLE_S), "delay": (on, cue),
        "R1": (cue, cue + RESP_S["R1"]), "R2": (cue, cue + RESP_S["R2"]),
        "pw": (on + PW[0], on + PW[1]), "pw0": (on + PW0[0], on + PW0[1]),
        "pre": (on - 0.1, on), "trial": (tstart, tstop), "stored": (tstart, stored_end),
        "mid": (pin + 2.0, pin + 4.5), "late": (pin + 5.5, pin + 8.0),
    }
    nb_tc = int(round((TC_SPAN[1] - TC_SPAN[0]) / BIN_S))
    nb_ps = int(round((PSTH_SPAN[1] - PSTH_SPAN[0]) * 1000))
    groups = sorted(set(zip(task.stim, task.response)))
    counts = {k: np.full((len(units), len(task)), np.nan, dtype=np.float32) for k in windows}
    tc = np.zeros((len(units), len(task), nb_tc), dtype=np.int16)
    valid = np.zeros((len(units), len(task)), dtype=bool)
    psth = {gk: np.zeros((len(units), nb_ps), dtype=np.float32) for gk in groups}
    psth_n = {gk: np.zeros(len(units), dtype=np.int32) for gk in groups}
    gmask = {gk: (task.stim.values == gk[0]) & (task.response.values == gk[1]) for gk in groups}
    unsorted = 0
    span = []
    trial_no = np.arange(len(task))
    for i, (a, b) in enumerate(zip(starts, idx)):
        st = st_all[a:b]
        if np.any(np.diff(st) < 0):
            unsorted += 1
            st = np.sort(st)
        if not len(st):
            span.append((np.nan, np.nan))
            continue
        span.append((st[0], st[-1]))
        # the unit's trials: from the trial holding its first spike to the trial holding its last
        k0 = np.searchsorted(tstop, st[0], side="right")
        k1 = np.searchsorted(tstart, st[-1], side="right") - 1
        valid[i] = (trial_no >= k0) & (trial_no <= k1)
        for k, (lo, hi) in windows.items():
            ok = valid[i] & (hi <= stored_end) if k in MASKED_WINDOWS else valid[i] & np.isfinite(hi)
            counts[k][i, ok] = (np.searchsorted(st, hi) - np.searchsorted(st, lo))[ok]
        edges = pin[:, None] + TC_SPAN[0] + BIN_S * np.arange(nb_tc + 1)[None, :]
        c = np.searchsorted(st, edges)
        tc[i] = np.diff(c, axis=1)
        pedges = on[:, None] + PSTH_SPAN[0] + 0.001 * np.arange(nb_ps + 1)[None, :]
        pc = np.diff(np.searchsorted(st, pedges), axis=1)
        for gk, gm in gmask.items():
            ti = gm & valid[i] & psth_ok
            psth[gk][i] = pc[ti].sum(axis=0)
            psth_n[gk][i] = int(ti.sum())
    units["n_spikes"] = (idx - starts)
    units["n_trials"] = valid.sum(axis=1)
    units["trial_coverage"] = valid.mean(axis=1)
    units["first_spike"] = [s[0] for s in span]
    units["last_spike"] = [s[1] for s in span]
    meta["unsorted_units"] = unsorted
    meta["first_trial_start"] = float(all_trials.start_time.min())
    meta["last_trial_stop"] = float(all_trials.stop_time.max())
    f.close()
    return {"meta": meta, "trials": task, "units": units, "counts": counts, "tc": tc, "valid": valid,
            "psth": psth, "psth_n": psth_n}


def load_all_ecephys(assets: pd.DataFrame, workers: int = 12) -> list[dict]:
    rows = assets[assets.path.str.contains("ecephys")].sort_values("path").to_dict("records")
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(load_ecephys, rows))


def unit_table(sessions: list[dict]) -> pd.DataFrame:
    """All units, one row each, with their session's metadata."""
    out = []
    for si, s in enumerate(sessions):
        u = s["units"].copy()
        m = s["meta"]
        u["session"] = si
        u["unit"] = np.arange(len(u))
        u["subject"] = m["subject"]
        u["genotype"] = m["genotype"]
        u["region"] = m["region"]
        u["ogen_site"] = m["ogen_site"]
        out.append(u)
    return pd.concat(out, ignore_index=True)


# ---------------------------------------------------------------- unit measures

def kept(trials: pd.DataFrame, outcomes=KEEP) -> np.ndarray:
    return trials.response.isin(outcomes).values


def ttest(a, b, equal_var: bool):
    """Two-sided t-test, p = 1 when either group is constant and equal or too small."""
    from scipy import stats
    a, b = np.asarray(a, float), np.asarray(b, float)
    a, b = a[~np.isnan(a)], b[~np.isnan(b)]
    if len(a) < 2 or len(b) < 2:
        return np.nan
    if np.var(a) == 0 and np.var(b) == 0:
        return 1.0 if np.mean(a) == np.mean(b) else 0.0
    return float(stats.ttest_ind(a, b, equal_var=equal_var).pvalue)


def ttest_rows(a: np.ndarray, b: np.ndarray, equal_var: bool) -> np.ndarray:
    """Row-wise two-sided t-tests (units x trials), ignoring NaN; p = 1 when both groups are constant
    and equal, 0 when constant and different, NaN with fewer than 2 values in a group."""
    from scipy import stats
    na, nb = np.sum(~np.isnan(a), axis=1), np.sum(~np.isnan(b), axis=1)
    with np.errstate(all="ignore"):
        ma, mb = np.nanmean(a, axis=1), np.nanmean(b, axis=1)
        va, vb = np.nanvar(a, axis=1, ddof=1), np.nanvar(b, axis=1, ddof=1)
        if equal_var:
            df = na + nb - 2
            sp = ((na - 1) * va + (nb - 1) * vb) / df
            se = np.sqrt(sp * (1 / na + 1 / nb))
        else:
            se = np.sqrt(va / na + vb / nb)
            df = (va / na + vb / nb) ** 2 / ((va / na) ** 2 / (na - 1) + (vb / nb) ** 2 / (nb - 1))
        t = (ma - mb) / se
        p = 2 * stats.t.sf(np.abs(t), df)
    const = (va == 0) & (vb == 0)
    p = np.where(const, np.where(ma == mb, 1.0, 0.0), p)
    p = np.where((na < 2) | (nb < 2), np.nan, p)
    return p


def selectivity_table(sessions, units: pd.DataFrame, resp: str = "R1", equal_var: bool = True,
                      outcomes=("correct",), trials_sel: str = "control") -> pd.DataFrame:
    """Convention S, per unit: epoch t-tests of spike counts, contra against ipsi trials.

    resp: response window R1 or R2; outcomes: ('correct',) for c1, ('correct','incorrect') for c2;
    trials_sel: 'control' (no photostimulus) or 'all'. Returns p per epoch, the selectivity class
    and the preference by total count over the three epochs.
    """
    parts = []
    for si, grp in units.groupby("session"):
        s = sessions[si]
        t = s["trials"]
        m = t.response.isin(outcomes).values.copy()
        if trials_sel == "control":
            m = m & (t.stim == "none").values
        con, ips = m & t.contra.values, m & ~t.contra.values
        ui = grp.unit.values
        out = pd.DataFrame(index=grp.index)
        tot_c = np.zeros(len(ui))
        tot_i = np.zeros(len(ui))
        for ep, name in (("sample", "p_sample"), ("delay", "p_delay"), (resp, "p_resp")):
            c = s["counts"][ep][ui]
            out[name] = ttest_rows(c[:, con].astype(float), c[:, ips].astype(float), equal_var)
            tot_c += np.nanmean(c[:, con], axis=1) if con.any() else np.nan
            tot_i += np.nanmean(c[:, ips], axis=1) if ips.any() else np.nan
        dur_c = (t.delay_s[con].mean() + SAMPLE_S + RESP_S[resp]) if con.any() else np.nan
        dur_i = (t.delay_s[ips].mean() + SAMPLE_S + RESP_S[resp]) if ips.any() else np.nan
        v = s["valid"][ui]
        out["n_contra"], out["n_ipsi"] = (v & con).sum(axis=1), (v & ips).sum(axis=1)
        out["contra_pref"] = tot_c > tot_i
        out["rate_contra"], out["rate_ipsi"] = tot_c / dur_c, tot_i / dur_i
        parts.append(out)
    df = pd.concat(parts).loc[units.index]
    prep = (df.p_sample < 0.05) | (df.p_delay < 0.05)
    peri = df.p_resp < 0.05
    df["selective"] = prep | peri
    df["kind"] = np.select([prep & ~peri, ~prep & peri, prep & peri], ["prep_only", "peri_only", "both"], "none")
    return df


def photo_effect(sessions, units: pd.DataFrame, stim: str | list, outcomes=KEEP, window: str = "pw",
                 min_trials: int = 5, equal_var: bool = True, max_delay: float | None = None) -> pd.DataFrame:
    """Convention P, per unit: rate in `window` under photostimulus `stim` against control trials.

    `stim` is a trial label (see stim_label) or a list of labels pooled. Contra and ipsi pooled.
    window: 'pw' (20 to 120 ms), 'pw0' (0 to 100 ms) or 'delay' (the whole delay epoch, W1).
    max_delay: if given, only trials whose delay epoch is at most this long (s) enter.
    """
    stims = [stim] if isinstance(stim, str) else list(stim)
    dur = {"pw": PW[1] - PW[0], "pw0": PW0[1] - PW0[0]}
    parts = []
    for si, grp in units.groupby("session"):
        s = sessions[si]
        t = s["trials"]
        m = t.response.isin(outcomes).values
        if max_delay is not None:
            m = m & (t.delay_s.values <= max_delay)
        ctrl = m & (t.stim == "none").values
        pi = m & t.stim.isin(stims).values
        ui = grp.unit.values
        if window in dur:
            c = s["counts"][window][ui] / dur[window]
        else:
            c = s["counts"]["delay"][ui] / t.delay_s.values[None, :]
        out = pd.DataFrame(index=grp.index)
        v = s["valid"][ui]
        out["n_pi"], out["n_ctrl"] = (v & pi).sum(axis=1), (v & ctrl).sum(axis=1)
        out["rate_ctrl"] = np.nanmean(c[:, ctrl], axis=1) if ctrl.any() else np.nan
        out["rate_pi"] = np.nanmean(c[:, pi], axis=1) if pi.any() else np.nan
        out["p"] = ttest_rows(c[:, pi].astype(float), c[:, ctrl].astype(float), equal_var)
        parts.append(out)
    cols = ["n_pi", "n_ctrl", "rate_ctrl", "rate_pi", "p"]
    df = pd.concat(parts).loc[units.index] if parts else pd.DataFrame(columns=cols, dtype=float)
    df = df[df.n_pi >= min_trials].copy()
    df["delta"] = df.rate_pi - df.rate_ctrl
    df["ratio"] = df.rate_pi / df.rate_ctrl.replace(0, np.nan)
    df["sig"] = df.p < 0.05
    return df


def ratio_readings(df: pd.DataFrame) -> dict:
    """'To X% of control', readings Q1 to Q3 (percent)."""
    r = df.ratio.dropna()
    return {"Q1": 100 * df.rate_pi.mean() / df.rate_ctrl.mean(), "Q2": 100 * r.mean(), "Q3": 100 * r.median(),
            "n_ratio_undefined": int(df.ratio.isna().sum())}


def effect_counts(df: pd.DataFrame) -> dict:
    return {"n": len(df), "inhibited": int((df.delta < 0).sum()), "activated": int((df.delta > 0).sum()),
            "unchanged": int((df.delta == 0).sum()),
            "sig_inhibited": int((df.sig & (df.delta < 0)).sum()), "sig_activated": int((df.sig & (df.delta > 0)).sum())}


def population_psth(sessions, units: pd.DataFrame, stims, outcomes=KEEP, with_n: bool = False):
    """Per unit mean rate (spikes/s) in 1 ms bins around photostimulus onset, for control and stim.

    Returns two arrays, units x bins; a unit with no trials of a condition gives NaN. With
    `with_n`, also the number of photostimulus trials per unit.
    """
    stims = [stims] if isinstance(stims, str) else list(stims)
    out_c, out_p, n_pi = [], [], []
    for r in units.itertuples():
        s = sessions[r.session]
        acc = {"c": 0.0, "p": 0.0}
        n = {"c": 0, "p": 0}
        for (st, resp), arr in s["psth"].items():
            if resp not in outcomes:
                continue
            key = "c" if st == "none" else ("p" if st in stims else None)
            if key is None:
                continue
            acc[key] = acc[key] + arr[r.unit]
            n[key] += int(s["psth_n"][(st, resp)][r.unit])
        out_c.append(acc["c"] / n["c"] * 1000 if n["c"] else np.full(len(next(iter(s["psth"].values()))[0]), np.nan))
        out_p.append(acc["p"] / n["p"] * 1000 if n["p"] else np.full(len(next(iter(s["psth"].values()))[0]), np.nan))
        n_pi.append(n["p"])
    if with_n:
        return np.array(out_c), np.array(out_p), np.array(n_pi)
    return np.array(out_c), np.array(out_p)


def psth_time_ms() -> np.ndarray:
    nb = int(round((PSTH_SPAN[1] - PSTH_SPAN[0]) * 1000))
    return PSTH_SPAN[0] * 1000 + np.arange(nb) + 0.5


def onset_ms(ctrl: np.ndarray, pi: np.ndarray, reading: str = "O1", direction: int = -1) -> float:
    """Convention O on population PSTHs (1 ms bins): first bin after photostimulus onset where the
    photostimulus PSTH departs from control by more than 3 SD of the control PSTH over the delay
    epoch (0 to 1.3 s). O1 compares with control in the same bin, O2 with the control mean over the
    delay. direction -1 looks for a fall, +1 for a rise. Returns the bin's start in ms, or NaN."""
    t = psth_time_ms()
    delay = (t > 0) & (t < 1300)
    sd = np.nanstd(ctrl[delay])
    ref = ctrl if reading == "O1" else np.full_like(ctrl, np.nanmean(ctrl[delay]))
    hit = (direction * (pi - ref) > 3 * sd) & (t > 0)
    return float(t[np.argmax(hit)] - 0.5) if hit.any() else np.nan


def bootstrap_onset(ctrl_u: np.ndarray, pi_u: np.ndarray, reading: str, rng, n_boot: int = 1000, direction: int = -1):
    """Onset of the population PSTH, and its SEM from resampling units with replacement."""
    est = onset_ms(np.nanmean(ctrl_u, 0), np.nanmean(pi_u, 0), reading, direction)
    vals = []
    n = len(ctrl_u)
    for _ in range(n_boot):
        k = rng.integers(0, n, n)
        vals.append(onset_ms(np.nanmean(ctrl_u[k], 0), np.nanmean(pi_u[k], 0), reading, direction))
    vals = np.array(vals)
    return est, float(np.nanstd(vals)), int(np.isnan(vals).sum())


def onset_reliability(ctrl_u: np.ndarray, n_pi: np.ndarray, reading: str, rng, n_sim: int = 200,
                      step_ms: float | None = None, step_ratio: float = 1.0) -> np.ndarray:
    """Onsets that convention O returns on simulated photostimulus PSTHs, for a check of the rule.

    Each unit's photostimulus trials are drawn as Poisson counts from its own control PSTH, with its
    own number of photostimulus trials; with `step_ms`, the rate is multiplied by `step_ratio` from
    that time on. Without a step any onset found is a false one. Returns one onset (ms) per run."""
    t = psth_time_ms()
    keep = np.isfinite(ctrl_u).all(axis=1) & (n_pi > 0)
    lam = ctrl_u[keep] / 1000.0
    if step_ms is not None:
        lam = lam * np.where(t >= step_ms, step_ratio, 1.0)[None, :]
    n = n_pi[keep][:, None]
    mc = np.nanmean(ctrl_u[keep], 0)
    out = []
    for _ in range(n_sim):
        sim = rng.poisson(lam * n) / n * 1000.0
        out.append(onset_ms(mc, sim.mean(0), reading))
    return np.array(out)


def vmval_distance(units: pd.DataFrame) -> np.ndarray:
    """Distance (mm) in the coronal plane from the VM/VAL centre of reading L2."""
    return np.hypot(np.abs(units.ml.values) - VMVAL_CENTRE[0], units.dv.values - VMVAL_CENTRE[1])


# ---------------------------------------------------------------- whole-cell recordings

def kink_clip(v: np.ndarray, peaks: np.ndarray, rate: float = WC_RATE):
    """Convention V: for each spike peak, the kink is the first sample after the window 2.5 to 1.5 ms
    before the peak where dV/dt exceeds the window's mean plus 3 SD; Vm from -0.5 to 5 ms around the
    kink is replaced by a straight line. Returns the clipped trace and the Vm at each kink (the
    threshold), NaN where no kink was found, and whether the kink is the first sample searched (the
    derivative already above the limit 1.5 ms before the peak)."""
    dv = np.diff(v, prepend=v[0])
    out = v.copy()
    thr = np.full(len(peaks), np.nan)
    edge = np.zeros(len(peaks), dtype=bool)
    a0, a1 = int(2.5e-3 * rate), int(1.5e-3 * rate)
    pre, post = int(0.5e-3 * rate), int(5e-3 * rate)
    for i, p in enumerate(peaks):
        if p - a0 < 1 or p + post >= len(v):
            continue
        base = dv[p - a0:p - a1]
        lim = base.mean() + 3 * base.std()
        seg = dv[p - a1:p + 1]
        hit = np.flatnonzero(seg > lim)
        k = p - a1 + (hit[0] if len(hit) else 0)
        if not len(hit):
            continue
        thr[i] = v[k]
        edge[i] = hit[0] == 0
        lo, hi = max(k - pre, 0), min(k + post, len(v) - 1)
        out[lo:hi + 1] = np.linspace(out[lo], v[hi], hi - lo + 1)
    return out, thr, edge


def deposited_spikes(raw: np.ndarray, proc: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Spike peaks located from the deposited spike-removed trace: the maximum of the raw trace in
    each run of samples where raw and spike-removed differ. Also returns each run's first sample."""
    diff = raw != proc
    d = np.diff(diff.astype(np.int8), prepend=0, append=0)
    starts, stops = np.flatnonzero(d == 1), np.flatnonzero(d == -1)
    peaks = np.array([a + int(np.argmax(raw[a:b])) for a, b in zip(starts, stops)], dtype=int)
    return peaks, starts


def load_wholecell(asset: dict) -> dict:
    """One whole-cell recording, reduced: per trial Vm and spike measures around the photostimulus,
    the Vm trace from -50 to +150 ms (clipped by the kink rule and as deposited) for each onset
    reading of WC_ONSETS, basal Vm, the spike thresholds, and the deposited spike-removed Vm from 1 to
    3 s after pole onset at 1 ms, for the clock check."""
    f = _open(asset["asset_id"])
    g = f["general"]
    cell = [k for k, v in g["intracellular_ephys"].items() if isinstance(v, h5py.Group)]
    site = {k: parse_location(_s(v["location"][()])) for k, v in g["optogenetics"].items()}
    raw_ds = f["acquisition/PatchClampSeries/data"]
    meta = {"path": asset["path"], "subject": _s(g["subject/subject_id"][()]), "genotype": _s(g["subject/genotype"][()]),
            "description": _s(f["session_description"][()]), "cell": cell[0] if cell else None,
            "cell_location": parse_location(_s(g["intracellular_ephys"][cell[0]]["location"][()])) if cell else {},
            "ogen_site": list(site)[0] if site else None,
            "vm_unit": raw_ds.attrs.get("unit"), "vm_conversion": float(raw_ds.attrs.get("conversion")),
            "rate": float(f["acquisition/PatchClampSeries/starting_time"].attrs["rate"]),
            "t0": float(f["acquisition/PatchClampSeries/starting_time"][()])}
    raw = raw_ds[()].astype(np.float64)
    proc = f["processing/icephys/icephys/data"][()].astype(np.float64)
    cur = f["stimulus/presentation/CurrentClampStimulus/data"][()]
    trials = trial_table(f["intervals/trials"])
    rate, t0 = meta["rate"], meta["t0"]
    meta["n_samples"] = len(raw)
    meta["vm_range"] = (float(np.nanmin(raw)), float(np.nanmax(raw)))
    meta["current_values_nA"] = sorted(set(np.round(np.unique(cur), 3).tolist()))[:10]
    meta["frac_current_nonzero"] = float(np.mean(np.abs(cur) > 0.01))
    peaks, run_starts = deposited_spikes(raw, proc)
    clipped, thr, edge = kink_clip(raw, peaks, rate)
    meta["n_spikes"] = len(peaks)
    meta["threshold_mV"] = thr
    meta["kink_at_edge"] = edge
    meta["deposited_kink_mV"] = raw[np.clip(run_starts + int(0.5e-3 * rate), 0, len(raw) - 1)]
    meta["clip_vs_deposited_mad"] = float(np.median(np.abs(clipped - proc)))
    spk_t = peaks / rate + t0

    def idx(t):
        return np.clip(np.round((np.asarray(t) - t0) * rate).astype(int), 0, len(raw) - 1)

    trials["order_ok"] = trials.pole_in_time.between(trials.start_time, trials.stop_time)
    trials["cue"] = trials.cue_start_time
    trials["contra"] = trials["type"] == "lick right"
    trials["pi"] = trials.stim_present == 1
    # the deposited laser trace: per trial, first and last sample above LASER_FRAC of the file's
    # maximum between 0.5 s before and 4.5 s after pole onset (also at 1% and 20%, for the check)
    ls = [k for k in f["stimulus/presentation"].keys() if k.startswith("photostim")]
    lz = f[f"stimulus/presentation/{ls[0]}"]
    laser = lz["data"][()].astype(np.float64)
    meta["laser_series"] = ls
    meta["laser_unit"], meta["laser_conversion"] = _s(lz["data"].attrs.get("unit")), float(lz["data"].attrs.get("conversion"))
    meta["laser_max"] = float(laser.max())
    lt0 = float(lz["starting_time"][()])
    for frac in (0.01, LASER_FRAC, 0.2):
        ons, offs, peak = [], [], []
        for r in trials.itertuples():
            a = int(np.clip(np.round((r.pole_in_time - 0.5 - lt0) * rate), 0, len(laser)))
            b = int(np.clip(np.round((r.pole_in_time + 4.5 - lt0) * rate), 0, len(laser)))
            h = np.flatnonzero(laser[a:b] > frac * meta["laser_max"])
            ons.append((a + h[0]) / rate + lt0 if len(h) else np.nan)
            offs.append((a + h[-1]) / rate + lt0 if len(h) else np.nan)
            peak.append(float(laser[a:b].max()) if b > a else np.nan)
        trials[f"laser_on_{frac:g}"] = ons
        if frac == LASER_FRAC:
            trials["laser_on"], trials["laser_off"], trials["laser_peak"] = ons, offs, peak
    lag = float(np.nanmedian((trials.laser_on - trials.pole_in_time)[trials.pi]))
    meta["laser_lag_from_pole"] = lag
    w0, w1 = int(PW[0] * rate), int(PW[1] * rate)
    pre_n, post_n = int(0.05 * rate), int(0.15 * rate)
    traces, traces_dep = {}, {}
    for name, onset in WC_ONSETS.items():
        if onset[0] == "laser":
            on = trials.laser_on.where(trials.pi & trials.laser_on.notna(), trials.pole_in_time + lag)
        else:
            on = trials.pole_in_time + onset[1] if onset[0] == "pole_in" else trials.pole_out_time + onset[1]
        trials["on_" + name] = on
        on_i = idx(on)
        tr, trd, vm, vmd, sp, cu = [], [], [], [], [], []
        for k, t_on in enumerate(on.values):
            i = on_i[k]
            tr.append(clipped[i - pre_n:i + post_n].astype(np.float32))
            trd.append(proc[i - pre_n:i + post_n].astype(np.float32))
            vm.append(clipped[i + w0:i + w1].mean())
            vmd.append(proc[i + w0:i + w1].mean())
            sp.append(int(((spk_t >= t_on + PW[0]) & (spk_t < t_on + PW[1])).sum()))
            cu.append(float(np.mean(cur[i - pre_n:i + post_n])))
        traces[name], traces_dep[name] = np.array(tr), np.array(trd)
        trials["vm_pw_" + name], trials["vm_pw_dep_" + name] = vm, vmd
        trials["spikes_pw_" + name], trials["current_nA_" + name] = sp, cu
    basal, delay_vm, wide = [], [], []
    wide_t = np.arange(WIDE_SPAN[0], WIDE_SPAN[1], 0.001)
    for r in trials.itertuples():
        b0, b1 = idx(r.start_time - 0.5), idx(r.start_time)
        basal.append(clipped[b0:b1].mean() if b1 > b0 else np.nan)
        d0, d1 = idx(r.pole_in_time + SAMPLE_S), idx(r.cue)
        delay_vm.append(clipped[d0:d1].mean() if d1 > d0 else np.nan)
        wide.append(proc[idx(r.pole_in_time + wide_t)].astype(np.float32))
    trials["basal_vm"], trials["delay_vm"] = basal, delay_vm
    # lick traces around the go cue, for the clock check
    lick = {}
    for side in ("left", "right"):
        ds = f[f"acquisition/lick_trace/lick_trace_{side}/data"][()]
        before, after = [], []
        for k, r in enumerate(trials.itertuples()):
            c = idx(r.cue)
            seg = ds[max(c - int(0.5 * rate), 0):c + int(0.5 * rate)]
            half = len(seg) // 2
            before.append(np.ptp(seg[:half]) if half else np.nan)
            after.append(np.ptp(seg[half:]) if half else np.nan)
        lick[side] = (np.array(before), np.array(after))
    trials["lick_ptp_before_cue"] = np.nanmax([lick["left"][0], lick["right"][0]], axis=0)
    trials["lick_ptp_after_cue"] = np.nanmax([lick["left"][1], lick["right"][1]], axis=0)
    f.close()
    return {"meta": meta, "trials": trials, "trace": traces, "trace_dep": traces_dep, "wide": np.array(wide)}


def load_all_wholecell(assets: pd.DataFrame, workers: int = 4) -> list[dict]:
    rows = assets[assets.path.str.contains("icephys")].sort_values("path").to_dict("records")
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(load_wholecell, rows))


def vm_onset_ms(trace: np.ndarray) -> float:
    """Convention V on a mean trace sampled at 20 kHz from -50 ms: first sample at or after the
    photostimulus onset where Vm differs from the mean of -20 to +2 ms by more than 3 SD of it."""
    t = (np.arange(len(trace)) - int(0.05 * WC_RATE)) / WC_RATE * 1000
    base = (t >= -20) & (t <= 2)
    mu, sd = trace[base].mean(), trace[base].std()
    hit = (np.abs(trace - mu) > 3 * sd) & (t >= 0)
    return float(t[np.argmax(hit)]) if hit.any() else np.nan
