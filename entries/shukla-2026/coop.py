"""Loading and measures for dandiset 001845 (Shukla, Rivera, Bladon & Jadhav 2026, J Neurosci).

The dandiset holds one NWB file per rat and session. Both files of a pair session hold the same
poke events of both rats (left maze wells 1, 2, 3 and right maze wells A, B, C), the pair's
matched and rewarded pokes, and each file the processed head, neck and body position of its own
rat (cm, full video frame). Wells A, B, C correspond to 1, 2, 3 (the event descriptions).

Where each parameter comes from:
- First 21 sessions at 100% and first 35 at 50%: Methods, "Behavioral quantification and
  statistical analysis" (claims file, opening comment).
- A visit is a run of pokes at one well; a transition a visit to a well other than the previous
  one; performance = 200 x matches / transitions of both rats (Methods, Eq. 1, as the claims
  file reads it).
- Cross-correlation: 40 px radius, 1 Hz, arrivals, normalisation by the norms, lags -20 to +20 s
  (Methods, "Cross-correlation analysis of well arrivals"; claims file fig4eg). 40 px is taken in
  each video's own pixels: the scale is measured per file by regressing the processed head position
  (cm) on the raw DeepLabCut head position (pixels), because the files' camera device gives
  0.0016 m per pixel for every file while the processed positions of some rats use 0.0025.
  Where a file holds no raw pose, the subject's median scale is used, and where a subject has none,
  the device's 0.0016 m per pixel (an assumption).
- Leader: the rat whose poke at its matched well began first (Methods, "Assignment of leader and
  follower identities").
- State-space model: Smith et al. (2004), Eqs. 4 to 8 of the Methods; b0 = 0 (claims file).
- Gaze: bearing angle of Eq. 11 from neck-to-head and head-to-partner-body, 40 degrees
  (Methods, "Quantification of peer-directed head orientation events").
"""

from __future__ import annotations

import json
import re
import urllib.request
from concurrent.futures import ProcessPoolExecutor
from functools import partial

import h5py
import numpy as np
import remfile

DANDISET = "001845"
VERSION = "0.260526.1807"
API = "https://api.dandiarchive.org/api"
N_SESSIONS = {"rc100": 21, "rc50": 35}  # Methods, Behavioral quantification
CM_PER_PX = 0.16  # camera_device meters_per_pixel 0.0016
RADIUS_CM = 40 * CM_PER_PX  # Methods, 40 pixels
LEFT = {"1": 1, "2": 2, "3": 3}
RIGHT = {"A": 1, "B": 2, "C": 3}


def _get(url):
    with urllib.request.urlopen(url) as r:
        return json.load(r)


def list_assets(version=VERSION):
    url = f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=1000"
    out = []
    while url:
        page = _get(url)
        out += page["results"]
        url = page["next"]
    return out


def session_table(assets):
    """One row per NWB file: subject, session number, contingency, asset id, size."""
    rows = []
    for a in assets:
        m = re.match(r"sub-([^/]+)/sub-[^_]+_ses-(\d+)-(rc\d+)_behavior\.nwb$", a["path"])
        if m:
            rows.append(dict(subject=m.group(1), session=int(m.group(2)), contingency=m.group(3),
                             asset_id=a["asset_id"], size=a["size"], path=a["path"]))
    return rows


def s3_url(asset_id):
    meta = _get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/{asset_id}/")
    return [u for u in meta["contentUrl"] if "s3" in u][0]


def _s(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def cm_per_px(beh, n=6000):
    """cm per raw video pixel: slope of the processed head position (cm) on the raw DeepLabCut head
    position (pixels), y coordinate, over the first `n` frames with confidence above 0.95. NaN when
    the file holds no raw pose."""
    pe = [k for k in beh if k.startswith("PoseEstimation")]
    if not pe:
        return np.nan
    g = beh[pe[0]]["PoseEstimationSeriesHead"]
    raw, rt, conf = g["data"][:n], g["timestamps"][:n], g["confidence"][:n]
    pr, pt = beh["processed_position/head/data"][:n], beh["processed_position/head/timestamps"][:n]
    idx = np.clip(np.searchsorted(rt, pt), 0, len(rt) - 1)
    ok = np.isfinite(pr).all(1) & (conf[idx] > 0.95) & (np.abs(rt[idx] - pt) < 1e-3) & np.isfinite(raw[idx]).all(1)
    if ok.sum() < 100:
        return np.nan
    A = np.c_[raw[idx][ok, 1], np.ones(ok.sum())]
    return float(np.linalg.lstsq(A, pr[ok, 1], rcond=None)[0][0])


def read_file(asset_id, positions=("head", "neck", "body")):
    """Stream one NWB file and return what the analyses use, reduced as it loads."""
    f = h5py.File(remfile.File(s3_url(asset_id)), "r")
    beh = f["processing/behavior"]
    ev = {k: beh["behavioral_events"][k]["timestamps"][:] for k in beh["behavioral_events"]}
    task = list(f["processing/tasks"].keys())[0]
    pos = {}
    for p in positions:
        pos[p] = beh["processed_position"][p]["data"][:].astype(np.float32)
    pos_t = beh["processed_position/head/timestamps"][:]
    tt = f[f"processing/tasks/{task}"]
    task_fields = {k: _s(tt[k][0]) for k in ("task_name", "task_environment", "led_configuration", "led_list")
                   if k in tt}
    rw = beh["reward_well_visits"]
    visits = {k: rw[k][:] for k in ("well_id", "start_time", "stop_time")}
    out = dict(
        subject=_s(f["general/subject/subject_id"][()]),
        genotype=_s(f["general/subject/genotype"][()]),
        description=_s(f["session_description"][()]),
        session_start=_s(f["session_start_time"][()]),
        side="left" if task.endswith("Left") else "right",
        epoch=(float(f["intervals/epochs/start_time"][0]), float(f["intervals/epochs/stop_time"][0])),
        events=ev, pos=pos, pos_t=pos_t, table_visits=visits,
        camera_m_per_px=float(f["general/devices/camera_device 0"].attrs.get("meters_per_pixel", np.nan)),
        cm_per_px=cm_per_px(beh) if positions else np.nan, task_fields=task_fields,
    )
    f.close()
    return out


def read_many(asset_ids, workers=12, **kw):
    """Read files in parallel processes (h5py serialises threads)."""
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(partial(read_file, **kw), asset_ids, chunksize=4))


def partner_of(description):
    m = re.search(r"subject (\S+) paired with (\S+) ", description)
    return m.group(1), m.group(2)


# ---------------------------------------------------------------- choice sequences


def pokes(ev, side):
    """Poke times and wells (1 to 3) of the rat on one maze, sorted."""
    names = LEFT if side == "left" else RIGHT
    t, w = [], []
    for k, well in names.items():
        ts = ev.get(f"reward_well_{k}", np.array([]))
        t.append(ts)
        w.append(np.full(len(ts), well))
    t = np.concatenate(t)
    w = np.concatenate(w)
    o = np.argsort(t, kind="stable")
    return t[o], w[o]


CLEAN_WINDOW_S = 0.5  # assumption: two wells 47 cm apart cannot be poked within 0.5 s


def clean_pokes(t, w, win=CLEAN_WINDOW_S):
    """Mask of pokes kept: a poke within `win` s of a poke at another well by the same rat is
    sensor crosstalk (both are dropped). An assumption of this attempt, not the paper's."""
    bad = np.zeros(len(t), bool)
    for k in (1, 2, 3):
        a = np.flatnonzero(w == k)
        b = np.flatnonzero(w != k)
        if len(a) == 0 or len(b) == 0:
            continue
        tb = t[b]
        j = np.searchsorted(tb, t[a])
        dprev = np.where(j > 0, t[a] - tb[np.clip(j - 1, 0, None)], np.inf)
        dnext = np.where(j < len(tb), tb[np.clip(j, None, len(tb) - 1)] - t[a], np.inf)
        bad[a] |= np.minimum(dprev, dnext) < win
    return ~bad


def visits(t, w):
    """Runs of consecutive pokes at one well: (well, first poke, last poke)."""
    if len(t) == 0:
        return np.zeros(0, int), np.zeros(0), np.zeros(0)
    new = np.r_[True, w[1:] != w[:-1]]
    idx = np.flatnonzero(new)
    ends = np.r_[idx[1:] - 1, len(t) - 1]
    return w[idx], t[idx], t[ends]


def matches(ev):
    """Times and wells of the dataset's matched pokes."""
    t, w = [], []
    for k, well in (("A1", 1), ("B2", 2), ("C3", 3)):
        ts = ev.get(f"matched_poke_{k}", np.array([]))
        t.append(ts)
        w.append(np.full(len(ts), well))
    t = np.concatenate(t)
    w = np.concatenate(w)
    o = np.argsort(t)
    return t[o], w[o]


def shifted(s, e, shift, t0, period):
    """Circularly shift intervals [s, e] by `shift` within [t0, t0 + period)."""
    d = e - s
    s2 = (s - t0 + shift) % period + t0
    return s2, s2 + d


def count_overlaps(w1, s1, e1, w2, s2, e2):
    """Visits of rat 1 that overlap in time a visit of rat 2 at the corresponding well."""
    n = 0
    for well in (1, 2, 3):
        a = w1 == well
        b = w2 == well
        if not a.any() or not b.any():
            continue
        ov = (s1[a][:, None] <= e2[b][None, :]) & (s2[b][None, :] <= e1[a][:, None])
        n += int(ov.any(axis=1).sum())
    return n


# ---------------------------------------------------------------- sequences measures


def triplets(seq):
    """Nonoverlapping triplets from the first visit (Methods, Choice triplet counts)."""
    n = len(seq) // 3
    return [tuple(seq[3 * i:3 * i + 3]) for i in range(n)]


def is_optimal(tr, reading):
    """o1: visits all three wells; o2: only 1-2-3 and 1-3-2 (claims file, fig3c)."""
    if reading == "o1":
        return len(set(tr)) == 3
    return tr in ((1, 2, 3), (1, 3, 2))


def sample_entropy(x, m, r):
    """Sample entropy (Richman & Moorman 2000), Chebyshev distance, self-matches excluded."""
    x = np.asarray(x, float)
    n = len(x)
    if n <= m + 1:
        return np.nan

    def count(mm):
        emb = np.lib.stride_tricks.sliding_window_view(x, mm)[: n - m]
        d = np.max(np.abs(emb[:, None, :] - emb[None, :, :]), axis=2)
        return (np.sum(d <= r) - len(emb)) / 2

    b = count(m)
    a = count(m + 1)
    if a == 0 or b == 0:
        return np.nan
    return -np.log(a / b)


# ---------------------------------------------------------------- positions


def well_centres(pos, pos_t, t, w):
    """Median head position at the rat's poke times, per well (claims file, fig4eg reading)."""
    idx = np.clip(np.searchsorted(pos_t, t), 0, len(pos_t) - 1)
    out = {}
    for well in (1, 2, 3):
        p = pos[idx[w == well]]
        p = p[np.isfinite(p).all(axis=1)]
        out[well] = np.median(p, axis=0) if len(p) else np.array([np.nan, np.nan])
    return out


def occupancy(pos, centres, radius=RADIUS_CM):
    """Nearest well within the radius, else 0."""
    c = np.array([centres[k] for k in (1, 2, 3)])
    d = np.linalg.norm(pos[:, None, :] - c[None, :, :], axis=2)
    d = np.where(np.isfinite(d), d, np.inf)
    k = np.argmin(d, axis=1)
    occ = np.where(d[np.arange(len(d)), k] <= radius, k + 1, 0)
    return occ


def downsample_occ(occ, pos_t, t0, t1, mode):
    """1 Hz occupancy: 'frame' takes the frame nearest each second, 'modal' the modal value."""
    edges = np.arange(t0, t1 + 1e-9, 1.0)
    if mode == "frame":
        idx = np.clip(np.searchsorted(pos_t, edges[:-1]), 0, len(pos_t) - 1)
        return occ[idx]
    b = np.searchsorted(edges, pos_t, side="right") - 1
    ok = (b >= 0) & (b < len(edges) - 1)
    cnt = np.zeros((len(edges) - 1, 4))
    np.add.at(cnt, (b[ok], occ[ok]), 1)
    return np.argmax(cnt, axis=1)


def arrivals(occ1hz, null_return):
    """Binary arrival series. null_return True: every change into a well counts (as the text
    says); False: a return to the same well after null is not an arrival."""
    a = np.zeros(len(occ1hz))
    last = 0
    prev = 0
    for i, o in enumerate(occ1hz):
        if o and o != prev:
            if null_return or o != last:
                a[i] = 1
        if o:
            last = o
        prev = o
    return a


def xcorr(a1, a2, maxlag=None):
    """scipy.signal.correlate full mode over the product of norms; positive lag = rat 2 follows."""
    from scipy.signal import correlate, correlation_lags

    n = np.linalg.norm(a1) * np.linalg.norm(a2)
    c = correlate(a2, a1, mode="full") / n if n > 0 else np.full(len(a1) + len(a2) - 1, np.nan)
    lags = correlation_lags(len(a2), len(a1), mode="full")
    if maxlag is not None:
        k = np.abs(lags) <= maxlag
        return lags[k], c[k]
    return lags, c


def bearing(neck, head, partner_body):
    """Eq. 11: angle between neck-to-head and head-to-partner-body, degrees."""
    v1 = head - neck
    v2 = partner_body - head
    num = np.sum(v1 * v2, axis=1)
    den = np.linalg.norm(v1, axis=1) * np.linalg.norm(v2, axis=1)
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.degrees(np.arccos(np.clip(num / den, -1, 1)))


# ---------------------------------------------------------------- state-space model


def smith_ssm(n, b0=0.0, ve0=0.005, x0=0.0, iters=500, tol=1e-6):
    """Smith et al. (2004) state-space model for binary series (Methods, Eqs. 4 to 8).

    Forward filter with a Newton-Raphson posterior mode at each step, fixed-interval smoother,
    EM update of the process variance ve. The initial state x0 is fixed at 0 (b0 carries the
    chance level, claims file). Returns p_k (smoothed) and ve.
    """
    n = np.asarray(n, float)
    K = len(n)
    ve = ve0
    for _ in range(iters):
        xp = np.zeros(K); vp = np.zeros(K); xf = np.zeros(K); vf = np.zeros(K)
        xprev, vprev = x0, ve
        for k in range(K):
            xp[k] = xprev
            vp[k] = vprev + ve
            x = xp[k]
            for _nr in range(30):
                e = np.exp(b0 + x)
                p = e / (1 + e)
                f = x - xp[k] - vp[k] * (n[k] - p)
                fp = 1 + vp[k] * p * (1 - p)
                dx = f / fp
                x -= dx
                if abs(dx) < 1e-10:
                    break
            e = np.exp(b0 + x)
            p = e / (1 + e)
            xf[k] = x
            vf[k] = 1 / (1 / vp[k] + p * (1 - p))
            xprev, vprev = xf[k], vf[k]
        xs = xf.copy(); vs = vf.copy(); A = np.zeros(K)
        for k in range(K - 2, -1, -1):
            A[k] = vf[k] / vp[k + 1]
            xs[k] = xf[k] + A[k] * (xs[k + 1] - xp[k + 1])
            vs[k] = vf[k] + A[k] ** 2 * (vs[k + 1] - vp[k + 1])
        # EM update of ve: expected squared increments, with lag-one covariance A_k vs_{k+1}
        cov = A[:-1] * vs[1:]
        s = np.sum(vs[1:] + xs[1:] ** 2 - 2 * (cov + xs[1:] * xs[:-1]) + vs[:-1] + xs[:-1] ** 2)
        s += vs[0] + (xs[0] - x0) ** 2
        ve_new = s / K
        if abs(ve_new - ve) < tol:
            ve = ve_new
            break
        ve = ve_new
    pk = 1 / (1 + np.exp(-(b0 + xs)))
    return pk, ve


# ---------------------------------------------------------------- building the session table

MATCH_HOLD_S = 3.0  # default tolerance; the notebook picks the one that best fits the dataset matches


def analysed_rows(rows, extra=0):
    """The first 21 (100%) and 35 (50%) sessions of each subject, in session order."""
    rows = sorted(rows, key=lambda r: (r["subject"], r["contingency"], r["session"]))
    rank = {}
    keep = []
    for r in rows:
        k = (r["subject"], r["contingency"])
        rank[k] = rank.get(k, 0) + 1
        if rank[k] <= N_SESSIONS[r["contingency"]] + extra:
            keep.append(dict(r, rank=rank[k]))
    return keep


def build(rows, files):
    """One record per pair session, with both rats' pokes, visits and positions."""
    scale = {}
    for f in files:
        scale.setdefault(f["subject"], []).append(f.get("cm_per_px", np.nan))
    scale = {k: float(np.nanmedian(v)) if np.isfinite(v).any() else CM_PER_PX for k, v in scale.items()}
    by = {}
    for r, f in zip(rows, files):
        a, b = partner_of(f["description"])
        pair = tuple(sorted((a, b)))
        by.setdefault((pair, r["contingency"], r["rank"]), {})[f["side"]] = (r, f)
    out = []
    for (pair, cont, rank), d in sorted(by.items()):
        rl, fl = d["left"]
        rr, fr = d["right"]
        ev = fl["events"]
        rec = dict(pair=pair, contingency=cont, rank=rank, session=rl["session"],
                   date=fl["session_start"][:10], t0=fl["epoch"][0], t1=fl["epoch"][1],
                   genotype="WT" if fl["genotype"] == "WT" and fr["genotype"] == "WT" else
                   ("Fmr1" if fl["genotype"] != "WT" and fr["genotype"] != "WT" else "mixed"),
                   events_identical=all(np.array_equal(ev.get(k, []), fr["events"].get(k, []))
                                        for k in set(ev) | set(fr["events"])))
        rec["match_t"], rec["match_w"] = matches(ev)
        rec["rewarded_t"] = ev.get("rewarded_poke", np.array([]))
        rats = {}
        for side, f in (("left", fl), ("right", fr)):
            t, w = pokes(ev, side)
            raw = visits(t, w)
            ok = clean_pokes(t, w)
            vw, vs, ve = visits(t[ok], w[ok])
            rats[side] = dict(subject=f["subject"], genotype="WT" if f["genotype"] == "WT" else "Fmr1",
                              poke_t=t[ok], poke_w=w[ok], vw=vw, vs=vs, ve=ve, raw_vw=raw[0],
                              raw_poke_t=t, raw_poke_w=w, n_dropped=int((~ok).sum()),
                              pos=f["pos"], pos_t=f["pos_t"], table=f["table_visits"],
                              cm_per_px=f["cm_per_px"] if np.isfinite(f["cm_per_px"]) else scale[f["subject"]])
        rec["rats"] = rats
        out.append(rec)
    return out


def load(version=VERSION, workers=12):
    """Stream every analysed file of the pinned version and build the pair sessions."""
    rows = analysed_rows(session_table(list_assets(version)))
    files = read_many([r["asset_id"] for r in rows], workers=workers)
    return rows, files, build(rows, files)


def reconstructed_matches(r1, r2, hold=MATCH_HOLD_S, shift=0.0, t0=0.0, period=None):
    """Matches rebuilt from the pokes: visits at corresponding wells whose poke runs overlap
    (each widened by `hold` seconds for the nose hold the events do not record), counted in time
    order and skipping a match at the well of the previous match (the dataset's matches never
    repeat a well; the task's nonrepetition rule). Rat 2's visits can be circularly shifted."""
    w1, s1, e1 = r1
    w2, s2, e2 = r2
    if shift:
        s2, e2 = shifted(s2, e2, shift, t0, period)
    ev = []
    for w in (1, 2, 3):
        a = np.flatnonzero(w1 == w)
        b = np.flatnonzero(w2 == w)
        if len(a) == 0 or len(b) == 0:
            continue
        ov = (s1[a][:, None] <= e2[b][None, :] + hold) & (s2[b][None, :] <= e1[a][:, None] + hold)
        i, j = np.nonzero(ov)
        if len(i):
            ev.append(np.c_[np.maximum(s1[a][i], s2[b][j]), np.full(len(i), w)])
    if not ev:
        return 0
    ev = np.concatenate(ev)
    ev = ev[np.argsort(ev[:, 0], kind="stable")]
    w = ev[:, 1]
    keep = np.r_[True, w[1:] != w[:-1]]
    # consecutive duplicates collapse; a run at one well counts once
    return int(keep.sum())


def follower_trials(a, b, shift=0.0, t0=0.0, period=None):
    """Follower trials (Methods, Partner behavior history analysis: "one rat (the leader) enters an
    arm first; the other rat (the follower) then decides whether to choose the matching arm").
    `a`, `b`: (subject, visit wells, visit starts) of the two rats. A trial opens at the next
    arrival at a new well by either rat (that rat leads) and closes at the other rat's next arrival
    (its choice); the follower cooperates when its new well corresponds to the leader's current well.
    Rat b's visits can be circularly shifted (the null). Returns (follower, leader, time, coop,
    impossible, leader-to-follower latency); impossible marks trials whose leader went to the well
    corresponding to the follower's own, where the follower cannot choose it."""
    sa, wa, s_a = a
    sb, wb, s_b = b
    if shift:
        s_b = (s_b - t0 + shift) % period + t0
        o = np.argsort(s_b, kind="stable")
        wb, s_b = wb[o], s_b[o]
    ev = sorted([(t, 0, sa, w) for t, w in zip(s_a, wa)] + [(t, 1, sb, w) for t, w in zip(s_b, wb)])
    cur, leader, out = {}, None, []
    for t, _, subj, w in ev:
        if leader is None:
            leader, tl = subj, t
        elif subj != leader:
            out.append((subj, leader, t, int(w == cur[leader]), int(cur.get(subj) == cur[leader]), t - tl))
            leader = None
        cur[subj] = w
    return out


# ---------------------------------------------------------------- statistics

def anova_A(df, dv, unit="unit"):
    """Reading A: ordinary two-way ANOVA genotype x session, one value per unit and session
    (the denominator df the paper prints). Returns {term: (F, df1, df2, p)}."""
    import statsmodels.formula.api as smf
    from statsmodels.stats.anova import anova_lm

    d = df.dropna(subset=[dv])
    fit = smf.ols(f"{dv} ~ C(genotype) * C(rank)", data=d).fit()
    a = anova_lm(fit, typ=2)
    out = {}
    for term, name in (("C(genotype)", "genotype"), ("C(rank)", "session"), ("C(genotype):C(rank)", "interaction")):
        out[name] = (a.loc[term, "F"], int(a.loc[term, "df"]), int(a.loc["Residual", "df"]), a.loc[term, "PR(>F)"])
    return out


def anova_B(df, dv, unit="unit"):
    """Reading B: mixed design, genotype between units, session within. The genotype test is the
    between-units F of the split-plot ANOVA, computed as a one-way ANOVA of the unit means (the
    same F when every unit has every session; it keeps units that miss a session). Session and
    interaction terms come from pingouin's mixed_anova on the units with every session."""
    import pingouin as pg
    from scipy import stats

    d = df.dropna(subset=[dv])
    m = d.groupby([unit, "genotype"])[dv].mean().reset_index()
    groups = [m[m.genotype == g][dv].values for g in sorted(m.genotype.unique())]
    f, p = stats.f_oneway(*groups)
    out = {"genotype": (f, 1, len(m) - 2, p)}
    full = d.groupby(unit)["rank"].nunique()
    keep = full[full == d["rank"].nunique()].index
    dd = d[d[unit].isin(keep)]
    try:
        a = pg.mixed_anova(data=dd, dv=dv, within="rank", between="genotype", subject=unit)
        for src, name in (("rank", "session"), ("Interaction", "interaction")):
            row = a[a["Source"] == src].iloc[0]
            out[name] = (row["F"], int(row["DF1"]), int(row["DF2"]), row["p_unc"] if "p_unc" in row else row["p-unc"])
    except Exception:
        out["session"] = out["interaction"] = (np.nan, 0, 0, np.nan)
    return out


def fmt(res):
    return "; ".join(f"{k} F({v[1]},{v[2]}) = {v[0]:.3f}, p = {v[3]:.3g}" for k, v in res.items())
