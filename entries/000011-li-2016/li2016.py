"""Loading and measures for dandiset 000011 (Li, Daie, Svoboda & Druckmann 2016).

Every file is streamed from the DANDI archive at the pinned version; nothing is
written to disk. Parameters and where they come from:

- Epoch boundaries (sample, delay, go) are the BehavioralEvents of each file.
- Photostimulus timing, power and site are read from the per-trial laser power
  traces in /stimulus/presentation (one 5 s chunk per photostimulus trial) and
  the photostim_start_time / photostim_stop_time events. Nothing about the
  condition of a trial is in the trials table.
- Spike width is the trough-to-peak interval of waveform_mean, at the stored
  sampling rate (claims file, convention U, from the Methods).
- Windows, steps and tests used by the measures are passed in by the notebook,
  which takes each from the claim's criterion.
"""
import functools
import json
import numpy as np
import pandas as pd
import requests
import h5py
import remfile

DANDISET = "000011"
VERSION = "0.220126.1907"
API = "https://api.dandiarchive.org/api"


def list_assets(version=VERSION):
    url = f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=200"
    out = []
    while url:
        r = HTTP.get(url, timeout=60).json()
        out += r["results"]
        url = r.get("next")
    df = pd.DataFrame([{"path": a["path"], "asset_id": a["asset_id"], "size": a["size"]} for a in out])
    df["subject"] = df.path.str.extract(r"sub-(\d+)/")[0]
    df["session"] = df.path.str.extract(r"_ses-(\d+)_")[0]
    return df.sort_values("path").reset_index(drop=True)


@functools.lru_cache(maxsize=None)
def s3_url(asset_id):
    r = HTTP.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60)
    return r.url


def open_nwb(asset_id):
    return h5py.File(remfile.File(s3_url(asset_id)), "r")


def _dec(v):
    return [x.decode() if isinstance(x, bytes) else x for x in v]


def _scalar(f, path):
    if path not in f:
        return None
    v = f[path][()]
    return v.decode() if isinstance(v, bytes) else v


def _in_trial(ts, starts, stops):
    """Index of the trial holding each timestamp (-1 if none)."""
    idx = np.searchsorted(starts, ts, side="right") - 1
    ok = (idx >= 0) & (ts < stops[np.clip(idx, 0, None)]) & np.isfinite(ts)
    return np.where(ok, idx, -1)


def _http():
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
    s = requests.Session()
    retry = Retry(total=8, backoff_factor=0.5, status_forcelist=[500, 502, 503, 504],
                  allowed_methods=["GET", "HEAD"])
    s.mount("https://", HTTPAdapter(max_retries=retry, pool_maxsize=32))
    return s


HTTP = _http()


def _range_read(url, offset, nbytes, dtype="<f8"):
    for attempt in range(5):
        try:
            r = HTTP.get(url, headers={"Range": f"bytes={offset}-{offset + nbytes - 1}"}, timeout=60)
            r.raise_for_status()
            return np.frombuffer(r.content, dtype=dtype)
        except requests.exceptions.RequestException:
            if attempt == 4:
                raise


def _laser_chunks(f, url, name, chunk=50000, workers=8):
    """Start time of each 50000-sample (5 s at 10 kHz) chunk of a laser power trace.

    The traces hold one chunk per photostimulus trial. The datasets are
    contiguous, so the first timestamp of each chunk is read directly by byte
    range from the archive (one small request per chunk). The chunk boundaries
    are checked against the timestamps in the data check of the notebook.
    """
    from concurrent.futures import ThreadPoolExecutor
    ts = f[f"/stimulus/presentation/{name}/timestamps"]
    n = ts.shape[0]
    off = ts.id.get_offset()
    idx = list(range(0, n, chunk))
    with ThreadPoolExecutor(workers) as ex:
        starts = list(ex.map(lambda i: _range_read(url, off + 8 * i, 8)[0], idx))
    return np.array(starts), n


def load_session(asset_id, laser=True):
    """Trials, units and metadata of one session."""
    url = s3_url(asset_id)
    f = h5py.File(remfile.File(url), "r")
    meta = {k: _scalar(f, p) for k, p in [
        ("identifier", "/identifier"), ("genotype", "/general/subject/genotype"),
        ("subject", "/general/subject/subject_id"), ("sex", "/general/subject/sex"),
        ("start", "/session_start_time")]}
    t = f["/intervals/trials"]
    tr = pd.DataFrame({
        "start": t["start_time"][:], "stop": t["stop_time"][:],
        "outcome": _dec(t["outcome"][:]), "instruction": _dec(t["trial_instruction"][:]),
        "early": _dec(t["early_lick"][:]), "task": _dec(t["task"][:]),
        "protocol": t["task_protocol"][:], "trial_id": t["id"][:]})
    meta["trials_unsorted"] = int(np.sum(np.diff(tr.start.values) < 0))
    tr = tr.sort_values("start", kind="stable").reset_index(drop=True)
    starts, stops = tr.start.values, tr.stop.values
    meta["trials_overlapping"] = int(np.sum(starts[1:] < stops[:-1]))
    ev = f["/acquisition/BehavioralEvents"]
    for e in ["sample", "delay", "go"]:
        tr[e] = np.nan
        if e in ev:
            ts = ev[e]["timestamps"][:]
            i = _in_trial(ts, starts, stops)
            tr.loc[i[i >= 0], e] = ts[i >= 0]
    tr["ps_on"] = np.nan; tr["ps_off"] = np.nan; tr["ps_power"] = np.nan
    tr["ps_site"] = None; tr["ps_events_nan"] = 0
    if "photostim_start_time" in ev:
        on = ev["photostim_start_time"]["timestamps"][:]
        pw = ev["photostim_start_time"]["data"][:]
        off = ev["photostim_stop_time"]["timestamps"][:]
        meta["ps_events"] = len(on)
        meta["ps_events_nan_time"] = int(np.isnan(on).sum())
        i = _in_trial(on, starts, stops)
        meta["ps_events_outside_trials"] = int(((i < 0) & np.isfinite(on)).sum())
        tr.loc[i[i >= 0], "ps_on"] = on[i >= 0]
        tr.loc[i[i >= 0], "ps_power"] = pw[i >= 0]
        j = _in_trial(off, starts, stops)
        tr.loc[j[j >= 0], "ps_off"] = off[j >= 0]
    sites = []
    if laser and "/stimulus/presentation" in f:
        for name in f["/stimulus/presentation"]:
            if not name.endswith("_laser_power"):
                continue
            site = name.replace(" ALM_laser_power", "")
            sites.append(site)
            cs, nsamp = _laser_chunks(f, url, name)
            nchunk = len(cs)
            meta[f"samples_{site}"] = nsamp
            i = _in_trial(cs, starts, stops)
            if (tr.loc[i[i >= 0], "ps_site"].notna()).any():
                raise ValueError("two laser sites in one trial")
            tr.loc[i[i >= 0], "ps_site"] = site
            tr.loc[i[i >= 0], "ps_chunk_start"] = cs[i >= 0]
            tr.loc[i[i >= 0], "ps_chunk"] = np.arange(nchunk)[i >= 0]
            # waveform of the light: mean and coefficient of variation of the power
            # from 0.1 to 0.5 s after onset, read for the first trial of each site
            # without an early lick (in early-lick trials the photostim event is
            # logged at a different time from the light in the trace)
            # (a 40 Hz sinusoid for one spot, constant for scanned spots, Methods)
            first = tr[(tr.ps_site == site) & tr.ps_on.notna() & (tr.ps_power > 1) & (tr.early != "early")]
            if len(first):
                r0 = first.iloc[0]
                k0 = int(round((r0.ps_on - r0.ps_chunk_start) * 1e4))
                doff = f[f"/stimulus/presentation/{name}/data"].id.get_offset()
                seg = _range_read(url, doff + 8 * (int(r0.ps_chunk) * 50000 + k0 + 1000), 8 * 4000)
                meta[f"shape_{site}"] = (float(seg.mean()), float(seg.std() / seg.mean()))
            meta[f"chunks_{site}"] = nchunk
            meta[f"chunks_outside_{site}"] = int((i < 0).sum())
    meta["sites"] = sites
    # units
    u = f["/units"]
    st = u["spike_times"][:]; sti = u["spike_times_index"][:]
    oi = u["obs_intervals"][:]; oii = u["obs_intervals_index"][:]
    n = len(sti)
    edges = np.r_[0, sti]; oedges = np.r_[0, oii]
    units = pd.DataFrame({
        "unit_id": u["id"][:], "cell_type": _dec(u["cell_type"][:]),
        "quality": _dec(u["quality"][:]), "fs": u["sampling_rate"][:],
        "posx": u["posx"][:], "posy": u["posy"][:]})
    raw = [st[edges[k]:edges[k + 1]] for k in range(n)]
    # spike times are not in time order in some units (format_error, reported in the data check);
    # they are sorted here, as the counting functions need
    meta["units_unsorted"] = int(sum(np.any(np.diff(x) < 0) for x in raw))
    units["spikes"] = [np.sort(x) for x in raw]
    units["obs"] = [oi[oedges[k]:oedges[k + 1]] for k in range(n)]
    units["waveform"] = list(u["waveform_mean"][:])
    f.close()
    return meta, tr, units


def spike_width_ms(w, fs):
    """Trough-to-peak interval of a mean waveform (Methods), in ms.

    Trough is the minimum; peak is the maximum after the trough.
    """
    w = np.asarray(w, float)
    i = int(np.argmin(w))
    j = i + int(np.argmax(w[i:]))
    return (j - i) / fs * 1e3


def unit_trials(obs, starts, stops):
    """Boolean per trial: was the unit observed over that trial."""
    ok = np.zeros(len(starts), bool)
    for a, b in obs:
        ok |= (starts < b) & (stops > a)
    return ok


def counts(spikes, t0, a, b):
    """Spike counts in [t0+a, t0+b) for each trial-aligned time t0."""
    t0 = np.asarray(t0, float)
    lo = np.searchsorted(spikes, t0 + a)
    hi = np.searchsorted(spikes, t0 + b)
    return (hi - lo).astype(float)


def binned(spikes, t0, centers, width):
    """Spike rate (Hz) in windows of `width` s centred at `centers` (s) around t0, trials x bins."""
    t0 = np.asarray(t0, float)[:, None]
    c = np.asarray(centers, float)[None, :]
    lo = np.searchsorted(spikes, (t0 + c - width / 2).ravel()).reshape(t0.shape[0], -1)
    hi = np.searchsorted(spikes, (t0 + c + width / 2).ravel()).reshape(t0.shape[0], -1)
    return (hi - lo) / width


# ---------------------------------------------------------------- conditions

EXP1_ONSETS = {"sample": -2.1, "early_delay": -1.3, "late_delay": -0.8}  # onset re go cue, s


def spots(power, shape):
    """Number of laser spots of a photostimulus.

    Methods: one spot is a 40 Hz sinusoid at 1.5 mW average; several spots are a
    constant photostimulus scanned over the sites at 1.5 mW average per site. A
    sinusoid (coefficient of variation of the power above 0.5) is one spot; a
    constant one has power / 1.5 mW spots, rounded to 2, 4 or 8 (the protocols
    of the Methods).
    """
    mean, cv = shape
    if cv > 0.5:
        return 1
    return int(2 ** round(np.log2(power / 1.5)))


def label_trials(meta, tr):
    """Add the condition of each trial.

    behaving: the trial has sample, delay and go events (non-performing trials
    have none). cond: "control"; for experiment 1 the epoch of the 0.5 s light
    ("sample", "early_delay", "late_delay", by its onset relative to the go
    cue); for experiments 2 and 3 "<site><spots>" (left1, right1, bilateral8,
    left4, right4, bilateral2); "no_light" for photostimulus trials whose peak
    power is below 1 mW; "unlabelled" in sessions with no photostimulus record.
    """
    tr = tr.copy()
    tr["behaving"] = tr.go.notna() & tr.delay.notna() & tr["sample"].notna() & tr.outcome.isin(["hit", "miss", "ignore"])
    tr["early_lick"] = tr.early == "early"
    tr["t_go"] = tr.go
    tr["ps_on_re_go"] = tr.ps_on - tr.go
    tr["ps_off_re_go"] = tr.ps_off - tr.go
    if not meta.get("sites"):
        tr["cond"] = "unlabelled"
        return tr
    has = tr.ps_site.notna() | tr.ps_on.notna()
    cond = pd.Series("control", index=tr.index, dtype=object)
    delay = np.nanmedian((tr.go - tr.delay)[tr.behaving])
    for i in tr.index[has]:
        r = tr.loc[i]
        if not (r.ps_power > 1):
            cond[i] = "no_light" if r.ps_power == r.ps_power else "ps_unknown"
            continue
        if abs(delay - 1.3) < 0.05:
            rel = r.ps_on_re_go
            name = min(EXP1_ONSETS, key=lambda k: abs(EXP1_ONSETS[k] - rel))
            cond[i] = name if abs(EXP1_ONSETS[name] - rel) < 0.05 else "ps_other"
        else:
            site = r.ps_site if isinstance(r.ps_site, str) else None
            if site is None:
                cond[i] = "ps_unknown"
                continue
            cond[i] = f"{site}{spots(r.ps_power, meta[f'shape_{site}'])}"
    tr["cond"] = cond
    return tr


def experiment(meta, tr):
    """Experiment of a session, from its delay and the conditions it holds."""
    beh = tr[tr.behaving & ~tr.early_lick]
    delay = np.median(beh.go - beh.delay) if len(beh) else np.nan
    conds = set(tr.cond)
    if not meta.get("sites"):
        return "exp1_unlabelled" if abs(delay - 1.3) < 0.05 else "no_photostim_record"
    if abs(delay - 1.3) < 0.05:
        return "exp1"
    if "bilateral8" in conds:
        return "exp2"
    if "bilateral2" in conds:
        return "exp3"
    return "other"


# ---------------------------------------------------------------- assembling

def load_all(version=VERSION, workers=8):
    """Load every ecephys file of the version, in parallel. Returns (assets, results)."""
    from concurrent.futures import ThreadPoolExecutor
    assets = list_assets(version)
    eph = assets[assets.path.str.contains("ecephys")]

    def one(r):
        m, tr, u = load_session(r.asset_id)
        return r.path, m, tr, u

    with ThreadPoolExecutor(workers) as ex:
        res = list(ex.map(one, list(eph.itertuples())))
    return assets, res


FS_MAX_MS, PYR_MIN_MS = 0.35, 0.45   # Methods, convention U


def assemble(results):
    """Session table, trial tables (labelled) and unit table."""
    sessions, units = {}, []
    for path, meta, tr, u in results:
        subj = path.split("/")[0].replace("sub-", "")
        ses = path.split("_ses-")[1].split("_")[0]
        sid = f"{subj}_{ses}"
        tr = label_trials(meta, tr)
        exp = experiment(meta, tr)
        if meta["trials_overlapping"] > 10:
            # interleaved trial sequences whose times overlap: events cannot be assigned to
            # trials, so no trial of the session enters an analysis (units are still counted)
            tr["behaving"] = False
        sessions[sid] = dict(sid=sid, subject=subj, session=ses, path=path, meta=meta,
                             trials=tr, exp=exp, genotype=meta["genotype"])
        u = u.copy()
        u["sid"] = sid; u["subject"] = subj; u["exp"] = exp
        u["genotype"] = "VGAT" if "VGAT" in meta["genotype"] else "PV"
        u["width_ms"] = [spike_width_ms(w, fs) for w, fs in zip(u.waveform, u.fs)]
        u["cls"] = np.where(u.width_ms < FS_MAX_MS, "FS", np.where(u.width_ms > PYR_MIN_MS, "pyr", "intermediate"))
        u["observed"] = [unit_trials(o, tr.start.values, tr.stop.values) for o in u.obs]
        u["n_spikes"] = [len(s) for s in u.spikes]
        units.append(u)
    units = pd.concat(units, ignore_index=True)
    units["uid"] = units.sid + "_" + units.unit_id.astype(str)
    return sessions, units


def trial_mask(tr, early="drop", outcomes=("hit", "miss")):
    """Behaving trials with the given outcomes; early-lick trials dropped or kept."""
    m = tr.behaving & tr.outcome.isin(outcomes)
    if early == "drop":
        m &= ~tr.early_lick
    return m.values


# ---------------------------------------------------------------- single-neuron measures

def epoch_bounds(tr, response=1.3):
    """Per-trial sample, delay and response epochs, in s relative to the go cue (from the events)."""
    return {"sample": np.c_[tr["sample"] - tr.go, tr.delay - tr.go],
            "delay": np.c_[tr.delay - tr.go, np.zeros(len(tr))],
            "response": np.c_[np.zeros(len(tr)), np.full(len(tr), response)]}


def counts_in(spikes, t0, lo, hi):
    """Spike counts between t0+lo and t0+hi (arrays per trial)."""
    a = np.searchsorted(spikes, t0 + lo)
    b = np.searchsorted(spikes, t0 + hi)
    return (b - a).astype(float)


def ttest(x, y, equal_var=True):
    from scipy import stats
    if len(x) < 2 or len(y) < 2:
        return np.nan
    if np.var(x) == 0 and np.var(y) == 0:
        return 1.0 if np.mean(x) == np.mean(y) else 0.0
    return stats.ttest_ind(x, y, equal_var=equal_var).pvalue


def selectivity_tests(units, sessions, response=1.3, outcomes=("hit",), early="drop", equal_var=True,
                      conds=("control",)):
    """Convention S: per unit and epoch, t-test of spike counts lick left against lick right trials."""
    rows = []
    for u in units.itertuples():
        tr = sessions[u.sid]["trials"]
        m = trial_mask(tr, early, outcomes) & tr.cond.isin(conds).values & u.observed
        t = tr[m]
        ep = epoch_bounds(t, response)
        r = {"uid": u.uid}
        right = (t.instruction == "right").values
        for e, b in ep.items():
            c = counts_in(u.spikes, t.go.values, b[:, 0], b[:, 1])
            r[e] = ttest(c[right], c[~right], equal_var)
        r["n_right"], r["n_left"] = int(right.sum()), int((~right).sum())
        rows.append(r)
    return pd.DataFrame(rows)


# ---------------------------------------------------------------- time courses

GRID_END = np.round(np.arange(-3.6, 1.6001, 0.05), 3)   # window ends, s re go cue; 50 ms steps (Methods)


def window_counts(spikes, t0, width, ends=GRID_END):
    """Spike counts in windows [end - width, end) re t0 (trials x windows)."""
    t0 = np.asarray(t0, float)[:, None]
    e = np.asarray(ends)[None, :]
    if t0.shape[0] == 0:
        return np.zeros((0, e.shape[1]), np.float32)
    a = np.searchsorted(spikes, (t0 + e - width).ravel()).reshape(t0.shape[0], -1)
    b = np.searchsorted(spikes, (t0 + e).ravel()).reshape(t0.shape[0], -1)
    return (b - a).astype(np.float32)


def labels(width, label, ends=GRID_END):
    """Time label of each window: its end ("end") or its centre ("centre")."""
    return np.round(ends - (width / 2 if label == "centre" else 0), 3)


def rate_change_tests(units, sessions, cond, width=0.4, early="drop", outcomes=("hit", "miss"),
                      equal_var=True, min_rate=None, min_trials=None):
    """Convention R: per unit and window, t-test of spike counts, control against `cond` trials,
    lick left and lick right pooled. Returns (p-values units x windows, info table)."""
    P, info = [], []
    for u in units.itertuples():
        tr = sessions[u.sid]["trials"]
        base = trial_mask(tr, early, outcomes) & u.observed
        c = base & (tr.cond == "control").values
        p = base & (tr.cond == cond).values
        go = tr.go.values
        cc = window_counts(u.spikes, go[c], width)
        pc = window_counts(u.spikes, go[p], width)
        # mean rate over the trial (sample onset to 1.3 s after the go cue) on control trials
        so = (tr["sample"] - tr.go).values[c]
        n_all = counts_in(u.spikes, go[c], so, np.full(c.sum(), 1.3))
        mean_rate = float(np.sum(n_all) / np.sum(1.3 - so)) if c.sum() else np.nan
        info.append({"uid": u.uid, "n_control": int(c.sum()), "n_cond": int(p.sum()), "mean_rate": mean_rate})
        if c.sum() < 2 or p.sum() < 2:
            P.append(np.full(len(GRID_END), np.nan)); continue
        from scipy import stats
        with np.errstate(all="ignore"):
            r = stats.ttest_ind(cc, pc, axis=0, equal_var=equal_var).pvalue
        same = (cc.var(0) == 0) & (pc.var(0) == 0)
        r[same] = np.where(cc.mean(0)[same] == pc.mean(0)[same], 1.0, 0.0)
        P.append(r)
    info = pd.DataFrame(info)
    keep = np.ones(len(info), bool)
    if min_rate is not None:
        keep &= info.mean_rate.values >= min_rate
    if min_trials is not None:
        keep &= (info.n_control.values >= min_trials) & (info.n_cond.values >= min_trials)
    info["included"] = keep
    return np.array(P), info


def rate_matrices(units, sessions, width, early="drop", outcomes=("hit", "miss")):
    """Per unit: rates (Hz, trials x windows) of its analysis trials, with their condition and
    instruction. Windows end at GRID_END."""
    out = {}
    for u in units.itertuples():
        tr = sessions[u.sid]["trials"]
        m = trial_mask(tr, early, outcomes) & u.observed
        t = tr[m]
        out[u.uid] = dict(rate=window_counts(u.spikes, t.go.values, width) / width,
                          cond=t.cond.values, right=(t.instruction == "right").values,
                          so=(t["sample"] - t.go).values, delay_on=(t.delay - t.go).values,
                          spikes=u.spikes, go=t.go.values)
    return out


def selectivity_courses(rm, conds, n_pref=10, draws=20, pref_window="trial", min_trials=3,
                        per_type=True, seed=0):
    """Convention D. For each unit: preferred trial type from `n_pref` random control trials
    (counts in `pref_window`: "trial" from sample onset to 1.3 s after the go cue, or "delay"),
    selectivity (preferred minus non-preferred rate) on the remaining control trials and on the
    trials of each condition; averaged over `draws` draws of the preference trials.
    Units need more than `min_trials` trials in every condition (per trial type if per_type).
    Returns {cond: units x windows} and the list of units kept."""
    rng = np.random.default_rng(seed)
    res = {c: [] for c in ("control",) + tuple(conds)}
    kept = []
    for uid, d in rm.items():
        ok = True
        for c in ("control",) + tuple(conds):
            m = d["cond"] == c
            if per_type:
                ok &= (m & d["right"]).sum() > min_trials and (m & ~d["right"]).sum() > min_trials
            else:
                ok &= m.sum() > min_trials and (m & d["right"]).sum() > 0 and (m & ~d["right"]).sum() > 0
        if not ok:
            continue
        ci = np.where(d["cond"] == "control")[0]
        if pref_window == "trial":
            lo, hi = d["so"], np.full(len(d["so"]), 1.3)
        else:
            lo, hi = d["delay_on"], np.zeros(len(d["so"]))
        cnt = counts_in(d["spikes"], d["go"], lo, hi) / (hi - lo)
        acc = {c: [] for c in res}
        for k in range(draws):
            for _ in range(100):
                pick = rng.choice(ci, size=min(n_pref, len(ci) - 2), replace=False)
                r = d["right"][pick]
                if r.any() and (~r).any():
                    break
            pref_right = cnt[pick][r].mean() >= cnt[pick][~r].mean()
            rest = np.setdiff1d(ci, pick)
            for c in res:
                idx = rest if c == "control" else np.where(d["cond"] == c)[0]
                rr = d["right"][idx]
                if not rr.any() or rr.all():
                    acc[c].append(np.full(d["rate"].shape[1], np.nan)); continue
                s = d["rate"][idx][rr].mean(0) - d["rate"][idx][~rr].mean(0)
                acc[c].append(s if pref_right else -s)
        for c in res:
            res[c].append(np.nanmean(acc[c], axis=0))
        kept.append(uid)
    return {c: np.array(v) for c, v in res.items()}, kept


def recovery_time(sel_ctrl, sel_pi, t, offset, frac=0.8, until=0.0):
    """First window label after `offset` (s) at which the photoinhibition selectivity reaches
    `frac` of the time-matched control selectivity; ms after the offset, NaN if none up to `until`."""
    ok = (t > offset + 1e-9) & (t <= until + 1e-9)
    hit = ok & (sel_pi >= frac * sel_ctrl)
    if not hit.any():
        return np.nan
    return float((t[np.argmax(hit)] - offset) * 1000)


def bootstrap_recovery(S, cond, t, offset, n_boot=1000, seed=0, until=0.0):
    """Recovery time of the population mean, and its bootstrap over neurons
    (mean, s.d., and how many resamples recover)."""
    rng = np.random.default_rng(seed)
    ctrl, pi = S["control"], S[cond]
    point = recovery_time(np.nanmean(ctrl, 0), np.nanmean(pi, 0), t, offset, until=until)
    n = len(ctrl)
    boots = []
    for _ in range(n_boot):
        i = rng.integers(0, n, n)
        boots.append(recovery_time(np.nanmean(ctrl[i], 0), np.nanmean(pi[i], 0), t, offset, until=until))
    boots = np.array(boots)
    return dict(point=point, boot_mean=float(np.nanmean(boots)) if np.isfinite(boots).any() else np.nan,
                boot_sd=float(np.nanstd(boots)) if np.isfinite(boots).any() else np.nan,
                boot_recovered=float(np.isfinite(boots).mean()), n=n)


# ---------------------------------------------------------------- activity space (convention A)

A_ENDS = np.round(np.arange(-3.4, 1.0001, 0.01), 3)   # 400 ms windows in 10 ms steps (Methods)


def auc(x, y):
    """Area under the ROC curve for separating x (positive) from y."""
    from scipy.stats import mannwhitneyu
    if len(x) == 0 or len(y) == 0:
        return np.nan
    return mannwhitneyu(x, y).statistic / (len(x) * len(y))


def a_sessions(units, sessions, exp, conds, early="drop", per_type=False, min_trials=5, min_neurons=5,
               outcomes=("hit", "miss")):
    """Sessions with more than `min_neurons` putative pyramidal neurons, each with more than
    `min_trials` trials in every condition (per trial type if per_type). Returns {sid: [uid]}."""
    out = {}
    for sid, s in sessions.items():
        if s["exp"] != exp:
            continue
        tr = s["trials"]
        if s["meta"].get("trials_overlapping", 0) > 0:
            continue
        m = trial_mask(tr, early, outcomes)
        right = (tr.instruction == "right").values
        keep = []
        for u in units[(units.sid == sid) & (units.cls == "pyr")].itertuples():
            ok = True
            for c in conds:
                mm = m & (tr.cond == c).values & u.observed
                ok &= ((mm & right).sum() > min_trials and (mm & ~right).sum() > min_trials) if per_type \
                    else mm.sum() > min_trials
            if ok:
                keep.append(u.uid)
        if len(keep) > min_neurons:
            out[sid] = keep
    return out


def session_counts(units, sessions, sid, uids, early="drop", outcomes=("hit", "miss"), ends=A_ENDS, width=0.4):
    """Spike counts (trials x neurons x windows) of the session's analysis trials observed for every
    neuron, with the trial table."""
    tr = sessions[sid]["trials"]
    uu = units.set_index("uid").loc[uids]
    m = trial_mask(tr, early, outcomes)
    for o in uu.observed:
        m = m & o
    t = tr[m].reset_index(drop=True)
    X = np.stack([window_counts(sp, t.go.values, width, ends) for sp in uu.spikes], axis=1)
    return X, t


def split_train(t, frac, rng):
    """Training set: a random fraction of the correct control trials."""
    idx = np.where((t.cond == "control") & (t.outcome == "hit"))[0]
    n = int(round(len(idx) * frac))
    train = np.zeros(len(t), bool)
    train[rng.choice(idx, n, replace=False)] = True
    return train


def coding_direction(X, t, train, epoch_lo, epoch_hi=0.0, ends=A_ENDS, width=0.4):
    """cd: mean over windows inside [epoch_lo, epoch_hi] of w_t = mean(lick right) - mean(lick left),
    correct control training trials; unit length. Also returns the w_t."""
    right = (t.instruction == "right").values
    inside = (ends - width >= epoch_lo - 1e-9) & (ends <= epoch_hi + 1e-9)
    w = X[train & right][:, :, inside].mean(0) - X[train & ~right][:, :, inside].mean(0)   # neurons x windows
    cd = w.mean(1)
    return cd / np.linalg.norm(cd), w, inside


def decision_boundary(pr, pl):
    vr, vl = np.var(pr, ddof=1), np.var(pl, ddof=1)
    return (pr.mean() / vr + pl.mean() / vl) / (1 / vr + 1 / vl)


# ---------------------------------------------------------------- network models (Methods, Extended Data Fig. 1)
# Parameters are those of the Methods and the Extended Data Fig. 1 legend, as the claims'
# criteria list them. The integration step (1 ms, Euler or Euler-Maruyama), the target and
# feedback of the FORCE network, and the random seeds are standard choices the paper does not give.

DT, T_END = 0.001, 2.0
SILENCE = (0.2, 1.0)


def simple_integrator(n=100, tau=0.1, lam=0.99, transient=False, silence=None, seed=0):
    """Linear rate network whose connectivity has one eigenvalue `lam`, all others zero, with a
    task-selective persistent (0.1-1.9 s) or transient (0.05-0.1 s) input along the integrating
    mode. `silence`: indices of neurons held at zero from 0.2 to 1.0 s. Returns the output (the
    activity along the integrating mode) for a lick right (+) and lick left (-) trial."""
    rng = np.random.default_rng(seed)
    u = rng.standard_normal(n); u /= np.linalg.norm(u)
    W = lam * np.outer(u, u)
    t = np.arange(0, T_END, DT)
    out = {}
    for sign in (1, -1):
        r = np.zeros(n); z = []
        for ti in t:
            on = (0.05 < ti < 0.1) if transient else (0.1 < ti < 1.9)
            I = sign * u * (1.0 if on else 0.0)
            r = r + DT / tau * (-r + W @ r + I)
            if silence is not None and SILENCE[0] < ti < SILENCE[1]:
                r[silence] = 0
            z.append(u @ r)
        out[sign] = np.array(z)
    return t, out


def cascaded_integrator(n=100, tau=0.1, lam=0.99, silence=None, seed=0):
    """Extended Data Fig. 1f, right: a transient input to one integrator whose output drives a
    second identical integrator, which ramps. Silencing holds half of the neurons of both at zero."""
    rng = np.random.default_rng(seed)
    u1 = rng.standard_normal(n); u1 /= np.linalg.norm(u1)
    u2 = rng.standard_normal(n); u2 /= np.linalg.norm(u2)
    W1, W2 = lam * np.outer(u1, u1), lam * np.outer(u2, u2)
    t = np.arange(0, T_END, DT)
    out = {}
    for sign in (1, -1):
        r1 = np.zeros(n); r2 = np.zeros(n); z = []
        for ti in t:
            I = sign * u1 * (20.0 if 0.05 < ti < 0.1 else 0.0)
            r1 = r1 + DT / tau * (-r1 + W1 @ r1 + I)
            r2 = r2 + DT / tau * (-r2 + W2 @ r2 + u2 * (u1 @ r1))
            if silence is not None and SILENCE[0] < ti < SILENCE[1]:
                r1[silence] = 0; r2[silence] = 0
            z.append(u2 @ r2)
        out[sign] = np.array(z)
    return t, out


def force_network(n=400, tau=0.2, p=0.1, g=1.5, iters=30, seed=0, alpha=1.0, learn_every=2):
    """Random recurrent network (tanh, sparse, gain g) trained with FORCE (recursive least squares
    on the readout, output fed back) to ramp to +1 or -1 at 2 s after a transient input
    (0.05-0.1 s) of opposite sign on the two trial types."""
    rng = np.random.default_rng(seed)
    from scipy import sparse
    mask = rng.random((n, n)) < p
    J = sparse.csr_matrix(np.where(mask, rng.standard_normal((n, n)) * g / np.sqrt(p * n), 0.0))
    w_in = rng.standard_normal(n)            # variance 1 (Methods)
    w_fb = rng.uniform(-1, 1, n)
    w_out = np.zeros(n)
    P = np.eye(n) / alpha
    t = np.arange(0, T_END, DT)
    target = {s: s * np.clip((t - 0.1) / (T_END - 0.1), 0, None) for s in (1, -1)}
    x0 = rng.standard_normal(n) * 0.5
    for it in range(iters):
        for s in (1, -1):
            x = x0.copy(); r = np.tanh(x); z = 0.0
            for k, ti in enumerate(t):
                I = s * w_in * (1.0 if 0.05 < ti < 0.1 else 0.0)
                x = x + DT / tau * (-x + J @ r + w_fb * z + I)
                r = np.tanh(x)
                z = w_out @ r
                if k % learn_every == 0 and ti > 0.1:
                    Pr = P @ r
                    c = 1.0 / (1.0 + r @ Pr)
                    P -= c * np.outer(Pr, Pr)
                    w_out -= c * (z - target[s][k]) * Pr
    return dict(J=J, w_in=w_in, w_fb=w_fb, w_out=w_out, x0=x0, tau=tau, target=target)


def run_force(net, silence=None, input_kind="transient"):
    t = np.arange(0, T_END, DT)
    out = {}
    for s in (1, -1):
        x = net["x0"].copy(); r = np.tanh(x); z = 0.0; zs = []
        for ti in t:
            on = (0.05 < ti < 0.1) if input_kind == "transient" else (0.1 < ti < 1.9)
            I = s * net["w_in"] * (1.0 if on else 0.0)
            x = x + DT / net["tau"] * (-x + net["J"] @ r + net["w_fb"] * z + I)
            r = np.tanh(x)
            if silence is not None and SILENCE[0] < ti < SILENCE[1]:
                r[silence] = 0
            z = net["w_out"] @ r
            zs.append(z)
        out[s] = np.array(zs)
    return t, out


def modular_attractor(trial, silence=(), seed=0, tau=0.1, noise_var=0.01, noise="em", n_trials=1):
    """Fig. 6b. Two modules of two units (right- and left-preferring); self-excitation 0.5235,
    inhibition -0.5235 within a module, 0.3 to the like-preferring unit of the other module;
    f(x) = g(x) - g(0), g(x) = 1.4 / (1 + exp(-(x - 0.5) / 0.3)); input 0.1 (0.05-0.1 s) to the
    instructed units; tonic 0.5; noise of variance 0.01. noise="em": white noise of intensity
    0.01 integrated by Euler-Maruyama (increment sd sqrt(0.01 dt) / tau); noise="sample": a sample
    of variance 0.01 drawn each 1 ms step and integrated like an input (increment dt / tau times it).
    Units 0, 1 are module 1 (right, left), units 2, 3 module 2. `silence`: units held at zero
    from 0.2 to 1.0 s. Returns the activity (n_trials x time x 4)."""
    rng = np.random.default_rng(seed)
    a, b, c = 0.5235, -0.5235, 0.3
    W = np.array([[a, b, c, 0], [b, a, 0, c], [c, 0, a, b], [0, c, b, a]])
    g = lambda x: 1.4 / (1 + np.exp(-(x - 0.5) / 0.3))
    f = lambda x: g(x) - g(0)
    t = np.arange(0, T_END, DT)
    r = np.zeros((n_trials, 4)); R = np.empty((n_trials, len(t), 4))
    sel = np.array([1, 0, 1, 0]) if trial == "right" else np.array([0, 1, 0, 1])
    sig = np.sqrt(noise_var)
    for k, ti in enumerate(t):
        I = 0.1 * sel * (0.05 < ti < 0.1)
        xi = rng.standard_normal((n_trials, 4))
        step = sig / tau * np.sqrt(DT) * xi if noise == "em" else DT / tau * sig * xi
        r = r + DT / tau * (-r + f(r) @ W.T + I + 0.5) + step
        if len(silence) and SILENCE[0] < ti < SILENCE[1]:
            r[:, list(silence)] = 0
        R[:, k] = r
    return t, R


def force_test(seed, iters=30):
    """Train one FORCE network (transient input) and silence a random half of its units from 0.2
    to 1.0 s. Returns the outputs at 2 s, unperturbed and perturbed, for both trial types."""
    net = force_network(iters=iters, seed=seed)
    sil = np.random.default_rng(10_000 + seed).choice(400, 200, replace=False)
    _, o = run_force(net)
    _, p = run_force(net, silence=sil)
    return {"seed": seed, "unpert_right": o[1][-1], "unpert_left": o[-1][-1], "pert_right": p[1][-1], "pert_left": p[-1][-1],
            "train_err": float(np.mean([abs(o[s][-1] - net["target"][s][-1]) for s in (1, -1)]))}


W_MODULAR_INTEGRATOR = np.array([
    [0, -1, 0, 0, 0, 0, 0.5, 0],
    [-1, 0, 0, 0, 0, 0, -0.5, 0],
    [1, -1, 0, 0, 0, 0, 0, -6],
    [1, -1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0.5, 0, 0, -1, 0, 0],
    [0, 0, -0.5, 0, -1, 0, 0, 0],
    [0, 0, 0, -6, 1, -1, 0, 0],
    [0, 0, 0, 0, 1, -1, 0, 0]])   # Methods, as printed (row i receives from column j)


def modular_integrator(trial, silence=(), tau=0.01):
    """Fig. 6c. Linear units with rates kept non-negative; constant input +-0.04 (0.1-1.9 s) to the
    right- and left-preferring integrator units of both modules; tonic input 40 to the integrator
    units. Units 0-3 module 1 (right, left, recovery, inhibitory), 4-7 module 2. Returns time x 8."""
    t = np.arange(0, T_END, DT)
    s = 1 if trial == "right" else -1
    tonic = np.array([40, 40, 0, 0, 40, 40, 0, 0], float)
    r = np.array([20, 20, 0, 0, 20, 20, 0, 0], float); R = []
    for ti in t:
        on = 0.1 < ti < 1.9
        I = 0.04 * s * np.array([1, -1, 0, 0, 1, -1, 0, 0]) * on
        r = np.maximum(r + DT / tau * (-r + W_MODULAR_INTEGRATOR @ r + I + tonic), 0)
        if len(silence) and SILENCE[0] < ti < SILENCE[1]:
            r[list(silence)] = 0
        R.append(r.copy())
    return t, np.array(R)


# ---------------------------------------------------------------- convention D over its readings

S_READINGS = [dict(response=r, outcomes=o, equal_var=e) for r in (1.3, 1.5)
              for o in (("hit",), ("hit", "miss")) for e in (True, False)]


def s_key(r):
    return f"R{'1' if r['response'] == 1.3 else '2'}-{'O1' if r['outcomes'] == ('hit',) else 'O2'}-{'student' if r['equal_var'] else 'welch'}"


def selective_sets(units, sessions, early):
    """Selective units (convention S, control trials) under each of its readings."""
    out = {}
    for r in S_READINGS:
        st = selectivity_tests(units, sessions, r["response"], r["outcomes"], early, r["equal_var"])
        out[s_key(r)] = set(st.uid[(st[["sample", "delay", "response"]] < 0.05).any(axis=1)])
    return out


def recovery_readings(units, sessions, offsets, sel_sets, early, no_recovery=(), n_boot=200, seed=0,
                      widths=(0.2, 0.4), pref_windows=("trial", "delay"), per_types=(True, False)):
    """Recovery time (convention D) of each condition in `offsets` ({cond: offset re go cue, s}),
    for every reading. Conditions in `no_recovery` are also judged by whether photoinhibition
    selectivity stays below 80% of control up to the go cue."""
    union = set().union(*sel_sets.values())
    base = units[units.uid.isin(union)]
    rows, courses = [], {}
    for w in widths:
        rm = rate_matrices(base, sessions, w, early)
        for pw in pref_windows:
            for pt in per_types:
                Sel, kept = selectivity_courses(rm, list(offsets), pref_window=pw, per_type=pt, seed=seed)
                kept = np.array(kept)
                for sk, ss in sel_sets.items():
                    idx = np.isin(kept, list(ss))
                    sub = {c: v[idx] for c, v in Sel.items()}
                    for lab in ("centre", "end"):
                        tl = labels(w, lab)
                        row = dict(early=early, S=sk, bin=w, label=lab, pref=pw,
                                   trials_rule="per type" if pt else "per condition", n=int(idx.sum()))
                        for c, o in offsets.items():
                            b = bootstrap_recovery(sub, c, tl, o, n_boot=n_boot, seed=seed, until=GRID_END[-1])
                            row[c] = b["point"]; row[c + "_boot"] = b["boot_mean"]; row[c + "_sd"] = b["boot_sd"]
                            if c in no_recovery:
                                ctrl, pi = np.nanmean(sub["control"], 0), np.nanmean(sub[c], 0)
                                ok = (tl > o) & (tl <= 0)
                                row[c + "_max_ratio_to_go"] = float(np.nanmax(pi[ok] / ctrl[ok]))
                                row[c + "_recovers_by_go"] = bool(np.any(pi[ok] >= 0.8 * ctrl[ok]))
                        rows.append(row)
                        courses[(w, pw, pt, sk, lab)] = (tl, {c: np.nanmean(v, 0) for c, v in sub.items()})
    return pd.DataFrame(rows), courses


def _orth(vectors):
    """Orthonormal basis of the span of `vectors` (Gram-Schmidt, in order)."""
    Q = []
    for v in vectors:
        w = v - sum((q @ v) * q for q in Q)
        nrm = np.linalg.norm(w)
        if nrm > 1e-12:
            Q.append(w / nrm)
    return np.array(Q)


def activity_session(X, t, frac, conds, ipsi, rng, ends=A_ENDS, baseline="pre-sample", cd_window=None,
                     orient="positive-sum"):
    """Convention A on one session. X: trials x neurons x windows (400 ms windows ending at `ends`).
    `frac`: fraction of correct control trials (and of ipsilateral trials) used to build cd, the
    modes and the decision boundary; projections use the other trials. Returns a dict of results."""
    out = {}
    right = (t.instruction == "right").values
    hit = (t.outcome == "hit").values
    licked_right = np.where(hit, right, ~right)
    cond = t.cond.values
    so = float(np.median(t["sample"] - t.go)); do = float(np.median(t.delay - t.go))
    j = {name: int(np.argmin(abs(ends - e))) for name, e in
         {"go": 0.0, "late_sample": do, "delay_start": do + 0.4, "pre_sample": so}.items()}
    train = split_train(t, frac, rng)
    # ipsilateral trials split the same way (for modes 2 and 3)
    ii = np.where(cond == ipsi)[0]
    ipsi_train = np.zeros(len(t), bool)
    ipsi_train[rng.choice(ii, int(round(len(ii) * frac)), replace=False)] = True
    lo, hi = (so, 0.0) if cd_window is None else cd_window
    cd, w, inside = coding_direction(X, t, train, lo, hi, ends)
    out["n_neurons"] = X.shape[1]
    # correlation of w, late sample against late delay, all correct control trials and training trials
    cc = (cond == "control") & hit
    for name, m in (("all", cc), ("train", train)):
        wa = X[m & right][:, :, j["late_sample"]].mean(0) - X[m & ~right][:, :, j["late_sample"]].mean(0)
        wb = X[m & right][:, :, j["go"]].mean(0) - X[m & ~right][:, :, j["go"]].mean(0)
        out[f"w_corr_{name}"] = np.corrcoef(wa, wb)[0, 1]
    p = np.einsum("tnw,n->tw", X, cd)
    held = ~train & ~ipsi_train
    out["roc_go"] = {c: auc(p[held & (cond == c) & right, j["go"]], p[held & (cond == c) & ~right, j["go"]]) for c in conds}
    # during photoinhibition (0.8 s from delay onset): (a)/(b) the 400 ms window ending at the start of
    # the ramp (centred on the light), (c) the mean over the windows inside the light
    j_ramp = int(np.argmin(abs(ends - (do + 0.6))))
    in_light = (ends - 0.4 >= do - 1e-9) & (ends <= do + 0.8 + 1e-9)
    pm = p[:, in_light].mean(1)
    out["roc_light_ab"] = {c: auc(p[held & (cond == c) & right, j_ramp], p[held & (cond == c) & ~right, j_ramp]) for c in conds}
    out["roc_light_c"] = {c: auc(pm[held & (cond == c) & right], pm[held & (cond == c) & ~right]) for c in conds}
    # decision boundary (training trials, last 400 ms before the go cue)
    db = decision_boundary(p[train & right, j["go"]], p[train & ~right, j["go"]])
    out["trials"] = pd.DataFrame({"cond": cond[held], "right": right[held], "hit": hit[held], "licked_right": licked_right[held],
                                  "d": p[held, j["go"]] - db})
    # modes
    cr = train & right; cl = train & ~right
    ir = ipsi_train & hit & right; il = ipsi_train & hit & ~right
    out["modes"] = out["captured"] = out["m2"] = out["m4"] = None
    if min(ir.sum(), il.sum(), cr.sum(), cl.sum()) == 0:
        return out      # a mode cannot be built without trials of each kind
    m2 = X[ir][:, :, j["go"]].mean(0) - X[cr][:, :, j["go"]].mean(0)
    m3 = X[il][:, :, j["go"]].mean(0) - X[cl][:, :, j["go"]].mean(0)
    m2 = m2 / np.linalg.norm(m2)
    m3 = _orth([m2, m3])[1] if len(_orth([m2, m3])) > 1 else np.zeros_like(m2)
    psth_r = X[cr][:, :, inside].mean(0); psth_l = X[cl][:, :, inside].mean(0)
    if baseline == "pre-sample":
        base = X[train][:, :, j["pre_sample"]].mean(0)[:, None]
    else:
        base = np.concatenate([psth_r, psth_l], 1).mean(1, keepdims=True)
    Y = np.concatenate([psth_r - base, psth_l - base], 1)
    uvec = np.linalg.svd(Y, full_matrices=False)[0]
    Q13 = _orth([cd, m2, m3])
    m45 = []
    for k in range(2):
        v = uvec[:, k] - Q13.T @ (Q13 @ uvec[:, k]) - sum((m @ uvec[:, k]) * m for m in m45)
        m45.append(v / np.linalg.norm(v))
    m4, m5 = m45
    if orient == "positive-sum" and m4.sum() < 0:
        m4 = -m4
    out["modes"] = dict(cd=cd, m2=m2, m3=m3, m4=m4, m5=m5)
    # captured selectivity and variance (trial-averaged, correct control trials of the training set)
    D = psth_r - psth_l
    rms = lambda A: np.sqrt(np.mean(A ** 2))
    Pcd = np.outer(cd, cd)
    Q15 = _orth([cd, m2, m3, m4, m5]); P15 = Q15.T @ Q15
    out["captured"] = {"sel_cd": rms(Pcd @ D) / rms(D), "var_cd": rms(Pcd @ Y) / rms(Y),
                       "sel_15": rms(P15 @ D) / rms(D), "var_15": rms(P15 @ Y) / rms(Y)}
    # projections of the held-out trials on modes 2 and 4
    for name, m in (("m2", m2), ("m4", m4)):
        q = np.einsum("tnw,n->tw", X, m)
        dbm = decision_boundary(q[train & right, j["go"]], q[train & ~right, j["go"]])
        ctl_h = held & (cond == "control")
        pred = (q[ctl_h, j["go"]] > dbm) if np.mean(q[train & right, j["go"]]) > np.mean(q[train & ~right, j["go"]]) \
            else (q[ctl_h, j["go"]] < dbm)
        out[name] = {"roc": auc(q[ctl_h & right, j["go"]], q[ctl_h & ~right, j["go"]]),
                     "n_pred": int(len(pred)), "n_correct_pred": int(np.sum(pred == licked_right[ctl_h])),
                     "diff_go": {c: q[held & (cond == c), j["go"]].mean() - q[ctl_h, j["go"]].mean() for c in conds if c != "control"},
                     "rise_delay": q[ctl_h, j["go"]].mean() - q[ctl_h, j["delay_start"]].mean()}
    return out
