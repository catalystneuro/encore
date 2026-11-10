"""Loading DANDI:000458 (Claar et al. 2023) and the per-unit measures of Burman et al. (2023),
Figure 4A to 4D and Figure S6.

Every method choice is the claims file's (claims/burman-2023.yaml, opening comment N1 to N8),
which takes it from the paper's Methods ("Pre-processing of Neuropixels dataset",
"Characterization of stimulus-evoked spiking responses") and the paper's analysis gist,
gist.github.com/paulbrodersen/a77bcf5e06ae27fa96923cb313a02ccf at revision
43a13d89441b7f56e835e84fa5811d9567917daf (burman_et_al_2023_neuropixel_data_analysis.py):

- SESSIONS: the 17 recordings the gist lists (N1).
- Units (N2): waveform_duration >= 0.4 ms (Methods; the gist's > 0.4 is a variant). Area reading
  A1, the Methods: location "SSp-ll" or "SSp-tr" when SSp was stimulated, "MOs" when MOs was;
  reading A2, the gist: location[:3] among the session's estim_target_region values of its
  electrical trials.
- Trials (N3): stimulus_type "electrical", is_valid true, behavioral_epoch "awake" or
  "isoflurane", all currents and depths pooled, times from stop_time (gist).
- Window (N4): spikes 2 to 12 ms after the stimulus, 1 ms bins.
- Entropy (N5), synchrony (N6) and the evoked rate (N7, readings F1 and F2) as the gist computes
  them; see each function.

Data are streamed with remfile and h5py from the pinned version; spikes are reduced, as they
load, to those within 0 to 20 ms of an electrical trial's stop_time.
"""
import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET = "000458"
VERSION = "0.230317.0039"  # the version the analysis gist names
API = "https://api.dandiarchive.org/api"
INTERVAL = (2, 12)  # ms after the stimulus (Methods; gist)
KEEP = (0.0, 20.0)  # ms after stop_time kept on loading, wider than every window used
SHIFTS = (-1500.0, 1500.0)  # ms: the clock check's windows away from the pulses (standard choice;
#                            inter-pulse intervals are 3.5 to 4.5 s, so these hold no evoked spikes)

SESSIONS = [
    "sub-546655_ses-20201023", "sub-551397_ses-20210211", "sub-551399_ses-20210128",
    "sub-569062_ses-20210218", "sub-569064_ses-20210408", "sub-569068_ses-20210304",
    "sub-569069_ses-20210312", "sub-569072_ses-20210422", "sub-569073_ses-20210415",
    "sub-569073_ses-20210416", "sub-571619_ses-20210319", "sub-571620_ses-20210513",
    "sub-575102_ses-20210603", "sub-586466_ses-20210729", "sub-586468_ses-20210819",
    "sub-590479_ses-20210921", "sub-590480_ses-20211111",
]
CONDITIONS = ("awake", "isoflurane")


def assets():
    """All assets of the pinned version: path, size and asset id."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    rows = []
    while url:
        page = requests.get(url, timeout=60).json()
        rows += [dict(path=a["path"], size=a["size"], asset_id=a["asset_id"])
                 for a in page["results"]]
        url = page["next"]
    return pd.DataFrame(rows)


def version_metadata():
    return requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/", timeout=60).json()


def open_asset(asset_id):
    url = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True,
                        timeout=60).url
    return h5py.File(remfile.File(url), "r")


def _str(a):
    return np.array([x.decode() if isinstance(x, bytes) else x for x in a], dtype=object)


def read_table(group, skip=()):
    """A DynamicTable's 1-D columns as a DataFrame (ragged and 2-D columns left out)."""
    cols = {}
    for k in group.keys():
        d = group[k]
        if k in skip or not isinstance(d, h5py.Dataset) or d.ndim != 1:
            continue
        if k + "_index" in group or k.endswith("_index"):
            continue
        if len(d) != len(group["id"]):
            continue
        v = d[:]
        cols[k] = _str(v) if v.dtype.kind in "OS" else v
    return pd.DataFrame(cols)


def read_session(asset_id):
    """Trials, unit metadata and peri-stimulus spikes of one file.

    Returns a dict with `trials` (all trials), `units` (all units, with the electrode group
    name), `spikes` (per unit row: an array of (index into trials, time in ms after the
    trial's stop_time) for spikes within KEEP of an electrical trial), `n_spikes` (each unit's
    total spike count), `shifted` (for each lag in SHIFTS, arrays (unit row, index into trials)
    of the spikes 2 to 12 ms after stop_time + lag, for the clock check) and file metadata.
    """
    f = open_asset(asset_id)
    trials = read_table(f["intervals/trials"]) if "intervals/trials" in f else pd.DataFrame()
    if "units" not in f:
        gen = f["general"]
        meta = dict(subject_id=gen["subject/subject_id"][()].decode(),
                    session_id=gen["session_id"][()].decode(), has_units=False,
                    groups=sorted(f.keys()), acquisition=sorted(f["acquisition"].keys()))
        f.close()
        return dict(trials=trials, units=pd.DataFrame(), spikes={}, meta=meta)
    u = f["units"]
    units = read_table(u, skip=("electrode_group",))
    units["electrode_group"] = [f[r].name.split("/")[-1] for r in u["electrode_group"][:]]
    index = u["spike_times_index"][:].astype(np.int64)
    starts = np.r_[0, index[:-1]]
    units["n_spikes"] = index - starts
    el = trials.index[trials.stimulus_type == "electrical"].to_numpy()
    stops = trials.loc[el, "stop_time"].to_numpy()
    order = np.argsort(stops)
    el, stops = el[order], stops[order]
    st = u["spike_times"]
    spikes = {}
    chunk = 2_000_000
    # read the flat spike_times in chunks, keeping only spikes near electrical trials
    n_total = int(index[-1]) if len(index) else 0
    unit_of = np.repeat(np.arange(len(index)), units["n_spikes"].to_numpy())
    kept_unit, kept_trial, kept_time = [], [], []
    shift_parts = {lag: ([], []) for lag in SHIFTS}
    sorted_ok = True
    for a in range(0, n_total, chunk):
        t = st[a:a + chunk] * 1000.0  # s -> ms
        # candidate trial: the latest stop at or before t - KEEP[0]
        j = np.searchsorted(stops * 1000.0, t - KEEP[0], side="right") - 1
        ok = j >= 0
        rel = np.where(ok, t - stops[np.clip(j, 0, None)] * 1000.0, np.inf)
        m = ok & (rel >= KEEP[0]) & (rel < KEEP[1])
        kept_unit.append(unit_of[a:a + chunk][m])
        kept_trial.append(el[j[m]])
        kept_time.append(rel[m])
        for lag in SHIFTS:
            origin = stops * 1000.0 + lag
            j2 = np.searchsorted(origin, t, side="right") - 1
            rel2 = t - origin[np.clip(j2, 0, None)]
            m2 = (j2 >= 0) & (rel2 >= INTERVAL[0]) & (rel2 < INTERVAL[1])
            shift_parts[lag][0].append(unit_of[a:a + chunk][m2])
            shift_parts[lag][1].append(el[j2[m2]])
    ku = np.concatenate(kept_unit) if kept_unit else np.array([], int)
    kt = np.concatenate(kept_trial) if kept_trial else np.array([], int)
    kx = np.concatenate(kept_time) if kept_time else np.array([])
    for r in range(len(units)):
        m = ku == r
        spikes[r] = np.c_[kt[m], kx[m]]
    shifted = {lag: (np.concatenate(us) if us else np.array([], int),
                     np.concatenate(ts) if ts else np.array([], int))
               for lag, (us, ts) in shift_parts.items()}
    # spike times sorted within each unit (checked on a sample of units)
    for r in range(0, len(units), max(1, len(units) // 20)):
        s0, s1 = starts[r], index[r]
        if s1 - s0 > 1 and np.any(np.diff(st[s0:min(s1, s0 + 100000)]) < 0):
            sorted_ok = False
    gen = f["general"]
    meta = dict(
        subject_id=gen["subject/subject_id"][()].decode(),
        session_id=gen["session_id"][()].decode(),
        has_units=True,
        stimulus=gen["stimulus"][()].decode(),
        epochs=pd.DataFrame(dict(start=f["intervals/epochs/start_time"][:],
                                 stop=f["intervals/epochs/stop_time"][:],
                                 tags=_str(f["intervals/epochs/tags"][:]))),
        spike_times_sorted=sorted_ok,
        ids_are_rows=bool(np.array_equal(u["id"][:], np.arange(len(units)))),
    )
    f.close()
    return dict(trials=trials, units=units, spikes=spikes, shifted=shifted, meta=meta)


# ---------------------------------------------------------------- selection

def target_regions(trials):
    el = trials[trials.stimulus_type == "electrical"]
    return sorted(el.estim_target_region.unique())


def select_units(session, area="A1", wf="ge"):
    """Row indices of the regular spiking units of the stimulated area (N2)."""
    units = session["units"]
    regions = target_regions(session["trials"])
    if area == "A1":  # Methods
        allowed = set()
        for r in regions:
            if r.startswith("SSp"):
                allowed |= {"SSp-ll", "SSp-tr"}
            if r == "MOs":
                allowed |= {"MOs"}
        in_area = units.location.isin(allowed)
    elif area == "A2":  # gist
        in_area = units.location.map(lambda x: x[:3] in regions)
    else:
        raise ValueError(area)
    wd = units.waveform_duration
    rs = wd >= 0.4 if wf == "ge" else wd > 0.4
    return np.flatnonzero((in_area & rs).to_numpy())


def condition_trials(trials, condition):
    """Trial indices of valid electrical trials of one behavioral epoch (N3), in table order."""
    m = ((trials.stimulus_type == "electrical") & (trials.behavioral_epoch == condition)
         & trials.is_valid.astype(bool))
    return trials.index[m].to_numpy()


def peristimulus(session, rows, trial_idx, interval=INTERVAL, offset=0.0):
    """Spikes of the units `rows` within `interval` ms of the trials `trial_idx`, as arrays
    (unit row, trial position in trial_idx, time in ms after the stimulus). `offset` shifts
    the time origin from stop_time (offset = -0.4 would be start_time for a 0.4 ms pulse)."""
    pos = {t: k for k, t in enumerate(trial_idx)}
    us, ts, xs = [], [], []
    for r in rows:
        s = session["spikes"][r]
        if not len(s):
            continue
        t = s[:, 1] - offset
        m = np.isin(s[:, 0], trial_idx) & (t >= interval[0]) & (t < interval[1])
        us.append(np.full(m.sum(), r))
        ts.append(np.array([pos[int(x)] for x in s[m, 0]], dtype=int))
        xs.append(t[m])
    if not us:
        return np.array([], int), np.array([], int), np.array([])
    return np.concatenate(us), np.concatenate(ts), np.concatenate(xs)


# ---------------------------------------------------------------- measures

def histogram(times, interval=INTERVAL, bin_width=1):
    """The gist's peri-stimulus histogram: 1 ms bins from interval[0]."""
    bins = np.arange(interval[0], interval[1] + bin_width, bin_width)
    idx = np.digitize(times, bins) - 1
    n = interval[1] - interval[0]
    return np.bincount(idx[idx >= 0], minlength=n)[:n].astype(float)


def measures(session, rows, trial_idx, population=None, interval=INTERVAL, offset=0.0):
    """Per unit of `rows`: spike count, rate F1 (Methods: count / (trials x 10 ms)), rate F2
    (the gist's get_firing_rate: summed spike times in ms over (highest trial position with a
    population spike + 1) x 10 ms), entropy (N5; NaN with fewer than two spikes) and synchrony
    (N6; NaN with no spike). The synchrony population is `population` (default: `rows`), the
    gist's units of N2 before any exclusion."""
    population = rows if population is None else population
    allrows = np.union1d(rows, population)
    u, tr, x = peristimulus(session, allrows, trial_idx, interval, offset)
    in_pop = np.isin(u, population)
    n_trials = len(trial_idx)
    width_s = (interval[1] - interval[0]) / 1000
    pu, ptr = u[in_pop], tr[in_pop]
    gist_trials = int(ptr.max() + 1) if len(ptr) else 0
    out = []
    # population histogram per trial, normalized by the trial's total count (N6)
    pop_hist = {}
    for t in np.unique(ptr):
        h = histogram(x[in_pop][ptr == t], interval)
        pop_hist[t] = h / h.sum()
    for r in rows:
        m = u == r
        times, trs = x[m], tr[m]
        count = int(m.sum())
        f1 = count / (n_trials * width_s)
        f2 = (np.sum(times) / (gist_trials * width_s)) if gist_trials else np.nan
        if count > 1:
            h = histogram(times, interval)
            p = h / h.sum()
            p = p[p > 0]
            ent = float(-(p * np.log(p)).sum())
        else:
            ent = np.nan
        if count and r in population:
            vals = [pop_hist[t][int(tt - interval[0])] for t, tt in zip(trs, times)]
            syn = float(np.mean(vals))
        elif count:
            # a unit outside the population: its spikes are read against the population's
            # histogram where the population has spikes on that trial
            vals = [pop_hist[t][int(tt - interval[0])] for t, tt in zip(trs, times) if t in pop_hist]
            syn = float(np.mean(vals)) if vals else np.nan
        else:
            syn = np.nan
        out.append(dict(row=int(r), count=count, rate_F1=f1, rate_F2=f2, entropy=ent,
                        synchrony=syn))
    df = pd.DataFrame(out)
    df.attrs["n_trials"] = n_trials
    df.attrs["gist_trials"] = gist_trials
    return df


def unit_table(session, area="A1", wf="ge", population="selected", offset=0.0):
    """One row per selected unit with awake and isoflurane measures (suffixes _aw, _an).
    population: "selected" (the N2 units, the gist) or a callable giving rows to use."""
    rows = select_units(session, area, wf)
    res = {}
    for c, suffix in zip(CONDITIONS, ("_aw", "_an")):
        tr = condition_trials(session["trials"], c)
        pop = rows if population == "selected" else population(session, rows, c)
        m = measures(session, rows, tr, population=pop, offset=offset)
        res[suffix] = m.set_index("row").add_suffix(suffix)
        res[suffix + "_trials"] = len(tr)
        res[suffix + "_gist_trials"] = m.attrs["gist_trials"]
    df = res["_aw"].join(res["_an"]).reset_index()
    df["n_trials_aw"], df["n_trials_an"] = res["_aw_trials"], res["_an_trials"]
    df["gist_trials_aw"], df["gist_trials_an"] = res["_aw_gist_trials"], res["_an_gist_trials"]
    df["location"] = session["units"].location.to_numpy()[df.row] if len(df) else []
    return df


def excluded(df, rate="F1", low=0.1, high=200.0):
    """The Methods' exclusion (N7): evoked rate below 0.1 Hz or above 200 Hz in either
    condition."""
    a, b = df[f"rate_{rate}_aw"], df[f"rate_{rate}_an"]
    return (a < low) | (a > high) | (b < low) | (b > high)


# ---------------------------------------------------------------- readings and statistics

READINGS = {  # name: (area, waveform cut, rate) ; A1F1 is the claims file's main reading (N7)
    "A1F1": ("A1", "ge", "F1"), "A1F2": ("A1", "ge", "F2"), "A2F1": ("A2", "ge", "F1"),
    "A2F2": ("A2", "ge", "F2"), "A1F1 gist cut (> 0.4 ms)": ("A1", "gt", "F1"),
    "A2F2 gist cut (> 0.4 ms)": ("A2", "gt", "F2"),
}


def all_units(sessions, area="A1", wf="ge", population="selected", offset=0.0):
    """unit_table over every session, with a `session` and `subject` column."""
    parts = []
    for name, s in sessions.items():
        t = unit_table(s, area, wf, population, offset)
        t["session"] = name
        t["subject"] = name.split("_")[0]
        parts.append(t)
    return pd.concat(parts, ignore_index=True)


def paired(df, measure):
    """Mean and SEM per condition and the paired t test (scipy.stats.ttest_rel) over units with
    the measure defined in both conditions (N8)."""
    from scipy import stats
    a, b = df[measure + "_aw"], df[measure + "_an"]
    ok = a.notna() & b.notna()
    t = stats.ttest_rel(a[ok], b[ok])
    return dict(n=int(ok.sum()), awake=a[ok].mean(), awake_sem=a[ok].sem(),
                anesthetized=b[ok].mean(), anesthetized_sem=b[ok].sem(),
                t=float(t.statistic), p=float(t.pvalue), dropped=int((~ok).sum()))


# ---------------------------------------------------------------- the paper's own code

GIST_URL = ("https://gist.githubusercontent.com/paulbrodersen/a77bcf5e06ae27fa96923cb313a02ccf/raw/"
            "43a13d89441b7f56e835e84fa5811d9567917daf/burman_et_al_2023_neuropixel_data_analysis.py")


def run_gist(sessions):
    """Run the paper's analysis gist, unmodified, on sessions loaded by read_session, and return
    the table it writes per session (the CSV it would save), keyed by session name.

    The gist reads each file with pynwb and writes a CSV. Here pynwb's NWBHDF5IO is replaced by
    an object that returns the loaded trials table and a units table (location,
    waveform_duration, spike_times in s, indexed by id), and DataFrame.to_csv is captured. The
    spike times given are the spikes read_session keeps (0 to 20 ms after an electrical
    stop_time, rebuilt as stop_time + latency); the gist uses only spikes 2 to 12 ms after
    valid electrical trials, so its results are the same as with the full trains. The gist's
    list names all 17 sessions; `sessions` must hold them all.
    """
    import contextlib
    import io
    import sys
    import types

    src = requests.get(GIST_URL, timeout=60).text

    class _Table:
        def __init__(self, df):
            self.df = df

        def to_dataframe(self):
            return self.df.copy()

    def _nwb(s):
        stops = s["trials"].stop_time.to_numpy()
        u = s["units"][["location", "waveform_duration"]].copy()
        u["spike_times"] = [np.sort(stops[a[:, 0].astype(int)] + a[:, 1] / 1000.0) if len(a)
                            else np.array([]) for a in (s["spikes"][r] for r in range(len(u)))]
        u.index = pd.Index(np.arange(len(u)), name="id")
        return types.SimpleNamespace(units=_Table(u), intervals={"trials": _Table(s["trials"])})

    def _io(path, mode):
        name = path.name.replace("_behavior+ecephys.nwb", "")
        return types.SimpleNamespace(read=lambda: _nwb(sessions[name]))

    out = {}

    def _capture(self, path, index=False):
        out[path.name.replace("_behavior+ecephys.csv", "")] = self.copy()

    saved_mod, saved_csv = sys.modules.get("pynwb"), pd.DataFrame.to_csv
    sys.modules["pynwb"] = types.SimpleNamespace(NWBHDF5IO=_io)
    pd.DataFrame.to_csv = _capture
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            exec(compile(src, "burman_et_al_2023_neuropixel_data_analysis.py", "exec"),
                 {"__name__": "__main__"})
    finally:
        pd.DataFrame.to_csv = saved_csv
        if saved_mod is None:
            sys.modules.pop("pynwb", None)
        else:
            sys.modules["pynwb"] = saved_mod
    return out
