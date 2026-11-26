"""Loading and trial parsing for Gillespie et al. (2024) on DANDI:000115 and DANDI:000629.

The dandisets hold raw 30 kHz broadband ephys, head LED position, port digital events (DIO)
and the statescript logs. They hold no LFP, SWR detections, sorted spikes or decodes, and no
parsed trial table, so trials are parsed here from the DIO events. Where each parameter comes
from:

- Trial phases (pre-reward = center port entry to reward delivery, post-reward = reward
  delivery to leaving the port) and the selection of trials with a pre-reward period (no
  lockout, or a center port success followed by a lockout): the claims file header ("Trials"),
  from dfa_ripquantpertrial_allphase_NF.m of the paper's code.
- The trial parser itself (Frank lab filterframework) is not in the paper's repository. Its
  rules here are an assumption, stated in the attempt: a trial starts at a home port reward;
  its center port is the one whose pump delivers the small reward; the pre-reward period runs
  from the first beam break at that port after the home reward to the pump onset; the outer
  arm is the first arm beam break after the center reward and before the next home reward,
  rewarded when that arm's pump turns on before the next home reward; a trial with a center
  reward and no arm visit is a lockout after center success.
- Leaving the port (leaveRW): reading (a) the first beam-off after reward that lasts more than
  200 ms, the statescript's own allowance for a nose briefly out of the port
  ("int proxTime = 200 % amount of time allowed to be away from nose poke", the statescript
  logs in the files); reading (b) the last beam-off at that port before the first beam break
  at any other port. The paper does not define it; both are run.
- Task phase: the rules of label_trial_interval.m as the claims file header (via
  claims/gillespie-2021.yaml) describes them. The goal changes right after the block's last
  reward (the paper, Methods, Behavioral training: "After a certain number of rewards earned
  at the goal arm ... the goal arm will change"), so the first non-lockout trial after the
  last reward of a block closes the old block. A search trial is redundant (an error, -0.2)
  when its arm was already visited by an earlier search trial of the same block; this detail
  is an assumption.
- Speed: head position is the mean of the two LEDs, in cm from the series' conversion
  factor; speed is the derivative of position smoothed with a Gaussian kernel. The sd of the
  kernel is not given by the paper (the smoothing is in the position processing, not in the
  repository); SPEED_SIGMAS are the readings run, and the result is shown under each.
- Immobility cutoff 4 cm/s: the paper (Results; Methods, timefilter in dfs_rips_vsctrlrats.m).
"""

import numpy as np
import pandas as pd
import requests
import h5py
import remfile

API = "https://api.dandiarchive.org/api"
CONTROL = ("000115", "0.210914.1732")
NF = ("000629", "0.240627.0646")
CONTROL_RATS = ["jaq", "roquefort", "despereaux", "montague"]  # code order, rats 1 to 4
NF_RATS = ["remy", "gus", "bernard", "fievel"]
PROX_TIME = 0.2  # s, statescript proxTime
SPEED_SIGMAS = (0.1, 0.25, 0.5)  # s, readings of the position smoothing (assumption)
IMMOBILITY = 4.0  # cm/s
CLOCK_SHIFTS = (-20, -10, -5, -2, 0, 2, 5, 10, 20)  # s, a standard choice for the clock check


def assets(dandiset):
    """Assets of a pinned dandiset version, as a DataFrame with subject and session."""
    ds, ver = dandiset
    url = f"{API}/dandisets/{ds}/versions/{ver}/assets/?page_size=400"
    rows = []
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        j = r.json()
        rows += j["results"]
        url = j["next"]
    df = pd.DataFrame(rows)[["asset_id", "path", "size"]]
    df["subject"] = df.path.str.extract(r"sub-([a-z]+)/")[0]
    df["day"] = df.path.str.extract(r"ses-[a-z]+-(\d+)_")[0].astype(int)
    return df.sort_values(["subject", "day"]).reset_index(drop=True)


def open_nwb(asset_id):
    """Open an asset by streaming (no download)."""
    r = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60)
    return h5py.File(remfile.File(r.url), "r")


def epochs(f):
    ep = f["intervals/epochs"]
    return pd.DataFrame({"tag": [t.decode() for t in ep["tags"][:]],
                         "start": ep["start_time"][:], "stop": ep["stop_time"][:]})


def run_epochs(f):
    e = epochs(f)
    return e[e.tag.str.contains("_r")].reset_index(drop=True)


def dio(f, names=None):
    """Onset (data == 1) times of each DIO channel."""
    be = f["processing/behavior/behavioral_events"]
    out = {}
    for k in be:
        if names is not None and k not in names:
            continue
        d = be[k]["data"][:]
        t = be[k]["timestamps"][:]
        out[k] = (t[d == 1], t[d == 0])
    return out


def position(f, start, stop, px_cm=None):
    """Head position (cm) and its time for the position series covering [start, stop].

    px_cm: cm per pixel to use when the series' conversion factor is 0 (DANDI:000629)."""
    pos = f["processing/behavior/position"]
    for k in pos:
        ts = pos[k]["timestamps"]
        t0 = ts[0]
        if t0 >= start - 5 and t0 <= stop:
            t = ts[:]
            d = pos[k]["data"][:].astype(float)
            conv = float(pos[k]["data"].attrs["conversion"])
            if conv == 0 and px_cm is not None:
                conv = px_cm / 100
            desc = pos[k].attrs.get("description", "")
            cols = [c.strip() for c in str(desc).split(",")]
            ix = [cols.index(c) for c in ("xloc", "yloc", "xloc2", "yloc2")]
            d = d[:, ix]
            ok = np.isfinite(t)
            t, d = t[ok], d[ok]
            keep = np.r_[True, np.diff(t) > 0]  # drop repeated timestamps
            t, d = t[keep], d[keep]
            # missing LED samples (NaN) are filled by linear interpolation in time
            for c in range(4):
                bad = ~np.isfinite(d[:, c])
                if bad.all():
                    return None
                if bad.any():
                    d[bad, c] = np.interp(t[bad], t[~bad], d[~bad, c])
            xy = np.c_[(d[:, 0] + d[:, 2]) / 2, (d[:, 1] + d[:, 3]) / 2] * conv * 100
            return t, xy, conv, int((~ok).sum())
    return None


def speed(t, xy, sigma):
    """Speed (cm/s) from position smoothed with a Gaussian of sd sigma (s)."""
    from scipy.ndimage import gaussian_filter1d
    dt = np.median(np.diff(t))
    s = sigma / dt
    xs = gaussian_filter1d(xy[:, 0], s)
    ys = gaussian_filter1d(xy[:, 1], s)
    v = np.hypot(np.gradient(xs, t), np.gradient(ys, t))
    return v


def _first_after(arr, t, before=np.inf):
    i = np.searchsorted(arr, t, side="right")
    if i < len(arr) and arr[i] < before:
        return arr[i]
    return np.nan


def parse_trials(ev, start, stop):
    """Trials of one run epoch from DIO onsets/offsets (see module docstring)."""
    def on(k):
        a = ev[k][0]
        return np.sort(a[(a >= start) & (a <= stop)])

    def off(k):
        a = ev[k][1]
        return np.sort(a[(a >= start) & (a <= stop)])

    home = on("homepump")
    arms = [k[:4] for k in ev if k.startswith("arm") and k.endswith("beam")]
    arms = sorted(set(arms))
    armbeam = {int(a[3]): on(f"{a}beam") for a in arms}
    armpump = {int(a[3]): on(f"{a}pump") for a in arms if f"{a}pump" in ev}
    allbeams = {"home": on("homebeam"), "R": on("Rbeam"), "W": on("Wbeam")}
    allbeams.update({f"arm{k}": v for k, v in armbeam.items()})
    rows = []
    for port in ("R", "W"):
        for T in on(f"{port}pump"):
            hi = np.searchsorted(home, T) - 1
            if hi < 0:
                continue
            h = home[hi]
            nexth = home[hi + 1] if hi + 1 < len(home) else stop
            ups = allbeams[port]
            u = ups[(ups > h) & (ups <= T)]
            if len(u) == 0:
                continue
            rwstart = u[0]
            # leaving (a): first off after T with no re-entry within PROX_TIME
            offs = off(f"{port}beam")
            offs = offs[offs >= T]
            leave_a = np.nan
            for o in offs:
                nxt = _first_after(ups, o)
                if not (nxt - o <= PROX_TIME):
                    leave_a = o
                    break
            # leaving (b): last off at this port before the first beam break elsewhere
            others = np.concatenate([v[v > T] for k, v in allbeams.items() if k != port] + [[np.inf]])
            firstother = others.min()
            ob = offs[offs < firstother]
            leave_b = ob[-1] if len(ob) else np.nan
            # outer arm
            arm, armt, rew = np.nan, np.nan, False
            best = np.inf
            for k, v in armbeam.items():
                x = v[(v > T) & (v < nexth)]
                if len(x) and x[0] < best:
                    best, arm = x[0], k
            if np.isfinite(best):
                armt = best
                p = armpump.get(arm, np.array([]))
                rew = bool(np.any((p >= armt) & (p < nexth)))
            rows.append(dict(port=port, home=h, rwstart=rwstart, rwend=T, leave_a=leave_a,
                             leave_b=leave_b, arm=arm, armtime=armt, armrew=rew,
                             lockout=not np.isfinite(best)))
    tr = pd.DataFrame(rows)
    if len(tr) == 0:
        return tr
    tr = tr.sort_values("rwend").reset_index(drop=True)
    tr["pre"] = tr.rwend - tr.rwstart
    tr["post_a"] = tr.leave_a - tr.rwend
    tr["post_b"] = tr.leave_b - tr.rwend
    return tr


def label_task_phase(tr, include_closer=False):
    """Task phase of non-lockout trials, label_trial_interval.m rules (module docstring).

    0 search at a new arm, -0.2 redundant search, n the n-th reward of the block, n + 0.3 a
    repeat error, n + 0.9 the visit to the old goal on the trial that closes a block; NaN for
    lockout trials. Blocks are runs of rewards at one arm. Also returns each trial's block.
    include_closer: reading (b) of a redundant search, in which the arm visited on the trial
    that closed the previous block (usually the old goal) counts as already visited.
    """
    valid = np.where(~tr.lockout.values)[0]
    arm = tr.arm.values
    rew = tr.armrew.values
    phase = np.full(len(tr), np.nan)
    block = np.full(len(tr), -1)
    # rewarded trials define goals; a goal change is a reward at a different arm
    rewarded = [i for i in valid if rew[i]]
    goals = []  # (first reward index, last reward index, arm)
    for i in rewarded:
        if goals and goals[-1][2] == arm[i]:
            goals[-1][1] = i
        else:
            goals.append([i, i, arm[i]])
    if not goals:
        phase[valid] = 0
        return phase, block
    # closing trial of block k: first valid trial after its last reward (not for the last block)
    closers = {}
    for k in range(len(goals) - 1):
        after = [j for j in valid if j > goals[k][1]]
        if after and after[0] < goals[k + 1][0]:
            closers[after[0]] = k
    bi = 0
    nrew = 0
    visited = set()
    cur = -1  # block index currently in force (-1 before the first reward)
    searching = True
    for j in valid:
        if j in closers:
            k = closers[j]
            phase[j] = nrew + (0.9 if arm[j] == goals[k][2] else 0.3)
            block[j] = k
            searching, nrew = True, 0
            visited = {arm[j]} if include_closer else set()
            cur = k + 1
            continue
        if rew[j]:
            if cur < 0:
                cur = 0
            # which block does this reward belong to
            while cur < len(goals) - 1 and j > goals[cur][1]:
                cur += 1
                nrew = 0
            nrew = nrew + 1
            phase[j] = nrew
            block[j] = cur
            searching = False
            visited = set()
        else:
            if searching:
                phase[j] = -0.2 if arm[j] in visited else 0
                visited.add(arm[j])
            else:
                phase[j] = nrew + 0.3
            block[j] = max(cur, 0)
    return phase, block


def trial_mean_speed(tr, t, v, a, b):
    """Mean speed between columns a and b of each trial."""
    out = np.full(len(tr), np.nan)
    for i, (x, y) in enumerate(zip(tr[a].values, tr[b].values)):
        if np.isfinite(x) and np.isfinite(y) and y > x:
            m = (t >= x) & (t <= y)
            if m.any():
                out[i] = v[m].mean()
    return out


def task_names(f):
    """Task name of each epoch, by epoch index (1-based, as task_epochs gives it)."""
    out = {}
    for k in f["processing/tasks"]:
        g = f["processing/tasks"][k]
        for i in np.ravel(g["task_epochs"][:]):
            out[int(i)] = g["task_name"][0].decode()
    return out


def _session_trials(row, px_cm=None, env=None):
    """Trials of every run epoch of one session, with pre-reward speeds and epoch info.

    env: keep only run epochs of this task name ("goal" for DANDI:000629)."""
    f = open_nwb(row.asset_id)
    ev = dio(f)
    names = task_names(f)
    out, info = [], []
    for i, e in run_epochs(f).iterrows():
        idx = int(e.tag.split("_")[0])
        if env is not None and names.get(idx) != env:
            continue
        tr = parse_trials(ev, e.start, e.stop)
        if len(tr) == 0:
            continue
        for inc in (False, True):
            ph, bl = label_task_phase(tr, include_closer=inc)
            tr["phase_b" if inc else "phase"] = ph
            tr["block"] = bl
        t, xy, conv, nnan = position(f, e.start, e.stop, px_cm)
        for s in SPEED_SIGMAS:
            v = speed(t, xy, s)
            tr[f"vel{s}"] = trial_mean_speed(tr, t, v, "rwstart", "rwend")
        # clock check: head position at reward delivery, and at shifted times
        for sh in CLOCK_SHIFTS:
            tr[f"x{sh}"] = np.interp(tr.rwend + sh, t, xy[:, 0])
            tr[f"y{sh}"] = np.interp(tr.rwend + sh, t, xy[:, 1])
        tr["rat"], tr["day"], tr["epoch"], tr["estart"] = row.subject, row.day, e.tag, e.start
        out.append(tr)
        hp = ev["homepump"][0]
        hp = hp[(hp >= e.start) & (hp <= e.stop)]
        info.append(dict(rat=row.subject, day=row.day, epoch=e.tag, start=e.start, stop=e.stop,
                         duration_min=(e.stop - e.start) / 60, ntrials=len(tr),
                         pos_conv=conv, pos_nan_ts=nnan,
                         pos_range_cm=float(np.ptp(xy[:, 0])),
                         fingerprint=tuple(np.round(np.diff(hp[:6]), 2))))
    return pd.concat(out) if out else pd.DataFrame(), info


def load_trials(dandiset, workers=6, a=None, px_cm=None, env=None):
    """Trials and epoch information of every run epoch of a dandiset (or of the assets a)."""
    from concurrent.futures import ThreadPoolExecutor
    if a is None:
        a = assets(dandiset)
    with ThreadPoolExecutor(workers) as ex:
        res = list(ex.map(lambda r: _session_trials(r, px_cm, env), [r for _, r in a.iterrows()]))
    trials = pd.concat([r[0] for r in res], ignore_index=True)
    info = pd.DataFrame([i for r in res for i in r[1]])
    info = info.sort_values(["rat", "day", "start"]).reset_index(drop=True)
    info["order"] = info.groupby("rat").cumcount() + 1
    trials = trials.merge(info[["rat", "day", "epoch", "order"]], on=["rat", "day", "epoch"])
    return trials, info


def raw_read_rate(asset_id, nchunks=8):
    """MB/s of streaming one channel of the raw ElectricalSeries (for the too_large estimate)."""
    import time
    f = open_nwb(asset_id)
    e = f["acquisition/e-series/data"]
    n = e.chunks[0]
    t0 = time.time()
    x = e[: n * nchunks, 0]
    dt = time.time() - t0
    return x.nbytes / 1e6 / dt, e.shape, e.chunks, e.dtype


def port_decoding(trials, shift):
    """Fraction of trials whose center port (R or W) is told by the head position at reward
    delivery + shift, with each epoch's port centroids taken at the true times (shift 0)."""
    ok = []
    for _, d in trials.groupby(["rat", "day", "epoch"]):
        c = {p: d.loc[d.port == p, ["x0", "y0"]].median().values for p in ("R", "W")}
        if any(np.isnan(v).any() for v in c.values()):
            continue
        xy = d[[f"x{shift}", f"y{shift}"]].values
        dist = np.c_[[np.hypot(*(xy - c[p]).T) for p in ("R", "W")]].T
        ok.append(np.where(dist[:, 0] < dist[:, 1], "R", "W") == d.port.values)
    return float(np.concatenate(ok).mean())


def dio_counts(row):
    """Per-epoch onset counts of the center port and home pumps, and file metadata (000629 check)."""
    f = open_nwb(row.asset_id)
    ep = epochs(f)
    ev = dio(f, names={"homepump", "Rpump", "Wpump", "t22"})
    pos = f["processing/behavior/position"]
    conv = sorted({float(pos[k]["data"].attrs["conversion"]) for k in pos})
    tasks = sorted({f["processing/tasks"][k]["task_description"][0].decode()
                    for k in f["processing/tasks"]})
    rows = []
    for _, e in ep.iterrows():
        d = dict(rat=row.subject, day=row.day, epoch=e.tag, sleep="_s" in e.tag,
                 minutes=(e.stop - e.start) / 60, pos_conversion=conv, task_descriptions=tasks,
                 session_start=f["session_start_time"][()].decode()[:10])
        for k in ("homepump", "Rpump", "Wpump", "t22"):
            on = ev.get(k, (np.array([]),))[0]
            d[k] = int(((on >= e.start) & (on <= e.stop)).sum())
        rows.append(d)
    return rows


def survey_dio(dandiset, workers=8):
    from concurrent.futures import ThreadPoolExecutor
    a = assets(dandiset)
    with ThreadPoolExecutor(workers) as ex:
        res = list(ex.map(dio_counts, [r for _, r in a.iterrows()]))
    return pd.DataFrame([x for r in res for x in r])


# --- statistics of the paper (Methods, Statistical tests; allrat_lmeplot.m) -----------------

def lme_cohort(ctrl, manip):
    """Linear mixed model Variable ~ Cohort + (1|Indiv), control samples against one
    manipulation trial type. ctrl and manip map rat -> array. Returns (coefficient of the
    manipulation cohort, p)."""
    import statsmodels.formula.api as smf
    rows = [(v, 0, r) for r, a in ctrl.items() for v in np.asarray(a, float)]
    rows += [(v, 1, r) for r, a in manip.items() for v in np.asarray(a, float)]
    df = pd.DataFrame(rows, columns=["y", "cohort", "rat"]).dropna()
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        m = smf.mixedlm("y ~ cohort", df, groups=df["rat"]).fit(reml=True)
    return float(m.params["cohort"]), float(m.pvalues["cohort"])


def ranksums_bh(nf, delay):
    """Wilcoxon rank-sum NF against delay per rat, Benjamini-Hochberg over the rats."""
    from scipy.stats import ranksums
    from statsmodels.stats.multitest import multipletests
    rats = list(nf)
    p = [ranksums(np.asarray(nf[r], float)[np.isfinite(nf[r])],
                  np.asarray(delay[r], float)[np.isfinite(delay[r])]).pvalue for r in rats]
    q = multipletests(p, method="fdr_bh")[1]
    return pd.DataFrame({"rat": rats, "p": p, "p_bh": q,
                         "median_nf": [np.nanmedian(nf[r]) for r in rats],
                         "median_delay": [np.nanmedian(delay[r]) for r in rats]})


def sign_test(x, m=0.5):
    """Two-sided sign test of the values x against m (MATLAB signtest)."""
    from scipy.stats import binomtest
    x = np.asarray(x, float)
    x = x[np.isfinite(x) & (x != m)]
    if len(x) == 0:
        return np.nan
    return binomtest(int((x > m).sum()), len(x), 0.5).pvalue


def plateau_days(trials, rat, readings, paper_counts):
    """Days of each plateau reading for one neurofeedback rat.

    'matched': the final whole days whose NF (R port) and delay (W port) trial counts are
    closest to the paper's Figure 2C legend counts; 'last7', 'last10': the final 7 or 10
    days (Methods, "maintained at the maximum threshold for 7-10 days")."""
    d = trials[trials.rat == rat]
    days = sorted(d.day.unique())
    out = {}
    for name in readings:
        if name == "matched":
            c = d.groupby("day").port.value_counts().unstack().fillna(0).loc[days[::-1]].cumsum()
            err = (c["R"] - paper_counts[0]).abs() + (c["W"] - paper_counts[1]).abs()
            k = days[::-1].index(err.idxmin()) + 1
        else:
            k = int(name.replace("last", ""))
        out[name] = days[-k:]
    return out


def yoking(trials):
    """For each trial, the smallest |pre-reward duration - pre-reward duration of one of the 8
    previous trials at the other port|. Delay times are drawn from the latencies of the 8
    prior neurofeedback trials (Methods), so this is small at the delay port only."""
    out = {}
    for port, other in (("W", "R"), ("R", "W")):
        diffs = []
        for _, d in trials.groupby(["rat", "day", "epoch"]):
            d = d.sort_values("rwend")
            o = d[d.port == other]
            for _, t in d[d.port == port].iterrows():
                prev = o[o.rwend < t.rwstart].pre.values[-8:]
                if len(prev) == 8:
                    diffs.append(np.min(np.abs(prev - t.pre)))
        out[port] = np.array(diffs)
    return out
