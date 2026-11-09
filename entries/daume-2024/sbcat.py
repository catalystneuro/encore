"""Loading and measures for dandiset 001187 (Daume et al. 2024, Neuron 112, 3957-3968).

Sources of parameters, as cited in the claims file claims/001187/10.1016-j.neuron.2024.09.013.yaml
(shared methods S, U, L, C, M, B, O, G, P) or in the paper:

- Rate filter 0.1 Hz in both tasks, WM rate = spikes up to the last raw WM event over the time from
  the first to the last raw WM event, LTM rate = spikes from the first raw LTM event over the time
  from the first to the last (claims U; rateFilter_units.m of the paper's code).
- Area: amygdala_left/right are amygdala, the others hippocampus (claims U).
- Category selection: spike rate 0.2 to 1.2 s after every encoding picture and the probe, 1x5
  permutation ANOVA p < 0.05, then the preferred category against the rest by a two-sided
  permutation t-test at p < 0.1 (claims C; NWB_calcCatSelective_SB.m).
- Memory selection: counts 0.2 to 1.2 s after LTM picture onset, correct trials, old against new,
  two-sided permutation t-test p < 0.05 (claims M; NWB_calcMemSelective_SB.m).
- Permutation p-values follow EEGLAB statcond (unpaired: labels shuffled; paired: conditions
  swapped within a unit), with stat_surrogate_pvals.m: p = (#perm > obs + 0.5)/(N + 1), two-sided
  2*min(p, 1-p); the t statistic is the pooled-variance t (ttest2_cell.m) or the paired t
  (ttest_cell.m), the ANOVA statistic the one-way F (claims P; the paper's code). 10,000
  permutations (Methods, Statistics).
- Baseline -0.9 to -0.3 s before encoding picture 1, maintenance window 0 to 2.5 s after
  maintenance onset (claims B; NWB_computeGLM.m). Spikes are counted with strict inequalities as
  the code does.
- Mixed models: normal, identity link, maximum likelihood, random intercepts for patient and for
  neuron within patient (claims G). Fitted with statsmodels MixedLM (reml=False), which for a normal
  response with identity link is the same model fitglme fits with 'Laplace'. P-values from the
  t distribution on n - p degrees of freedom, as fitglme reports them (claims G).
- Cluster test: FieldTrip-style dependent-samples t, maxsum cluster statistic, sign-flip
  permutations, cluster-forming threshold two-sided 0.05 (FieldTrip default clusteralpha, a
  standard choice named in the claims file), significance 0.025 per one-sided cluster (Methods,
  Statistics).
- Random seeds are standard choices; each claim's section makes its own generator.
"""
import os
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy import stats

DANDISET = "001187"
VERSION = "0.240904.2347"
API = "https://api.dandiarchive.org/api"
NPERM = 10000


def list_assets():
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    out = []
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        d = r.json()
        out += d["results"]
        url = d["next"]
    return out


def s3_url(asset_id):
    r = requests.get(f"{API}/assets/{asset_id}/download/", allow_redirects=False, timeout=60)
    r.raise_for_status()
    return r.headers["Location"].split("?")[0]


def _str(x):
    x = x[()] if isinstance(x, h5py.Dataset) else x
    return x.decode() if isinstance(x, bytes) else str(x)


def load_session(asset):
    """Read what the analysis needs from one NWB file, streamed from S3. Waveforms and stimulus
    images are not read."""
    f = h5py.File(remfile.File(s3_url(asset["asset_id"])), "r")
    s = {"path": asset["path"]}
    s["subject_id"] = _str(f["general/subject/subject_id"])
    s["session_id"] = _str(f["general/session_id"])
    s["identifier"] = _str(f["identifier"])
    s["age"] = _str(f["general/subject/age"])
    s["sex"] = _str(f["general/subject/sex"])
    s["institution"] = _str(f["general/institution"])
    s["notes"] = _str(f["general/notes"])
    for task in ["WM", "LTM"]:
        g = f[f"intervals/{task}_trials"]
        s[task.lower()] = pd.DataFrame({k: g[k][:] for k in g.keys()
                                        if k != "id" and g[k].ndim == 1}).assign(id=g["id"][:])
        ts = f[f"acquisition/events_raw_{task}/timestamps"][:]
        s[f"raw_{task}"] = (ts[0], ts[-1])
        ev = f[f"acquisition/events_{task}"]
        s[f"events_{task}"] = pd.DataFrame({"t": ev["timestamps"][:], "code": ev["data"][:]})
        s[f"events_{task}_desc"] = _str(ev.attrs["description"]) if "description" in ev.attrs else ""
    loc = np.array([x.decode() for x in f["general/extracellular_ephys/electrodes/location"][:]])
    eid = f["general/extracellular_ephys/electrodes/id"][:]
    ue = f["units/electrodes"][:]
    st = f["units/spike_times"][:]
    idx = f["units/spike_times_index"][:]
    starts = np.r_[0, idx[:-1]]
    s["units"] = pd.DataFrame({
        "unit_id": f["units/id"][:],
        "cluster": f["units/clusterID_orig"][:],
        "location": [loc[np.where(eid == e)[0][0]] for e in ue],
        "electrode": ue,
    })
    raw = [st[a:b] for a, b in zip(starts, idx)]
    s["unsorted_units"] = [i for i, x in enumerate(raw) if np.any(np.diff(x) < 0)]
    s["spikes"] = [np.sort(x) for x in raw]
    s["units_spike_desc"] = _str(f["units/spike_times"].attrs.get("description", b""))
    f.close()
    return s


def load_all(threads=12):
    assets = sorted(list_assets(), key=lambda a: a["path"])
    with ThreadPoolExecutor(threads) as ex:
        return list(ex.map(load_session, assets))


def area_of(location):
    return "amygdala" if location in ("amygdala_left", "amygdala_right") else "hippocampus"


def count(spikes, t0, a, b):
    """Spike counts in (t0 + a, t0 + b), strict as in the paper's code; t0 an array."""
    t0 = np.asarray(t0, float)
    return (np.searchsorted(spikes, t0 + b, side="left")
            - np.searchsorted(spikes, t0 + a, side="right"))


def global_rates(spikes, raw_wm, raw_ltm):
    """Global WM and LTM rates as rateFilter_units.m computes them (claims U)."""
    wm = np.sum(spikes <= raw_wm[1]) / (raw_wm[1] - raw_wm[0])
    ltm = np.sum(spikes >= raw_ltm[0]) / (raw_ltm[1] - raw_ltm[0])
    return wm, ltm


# ---------------------------------------------------------------- permutation tests (statcond)

def _pval(null, obs, tail="both"):
    """stat_surrogate_pvals.m: p = 1 - (rank - 0.5) / (N + 1), two-sided 2*min(p, 1-p)."""
    null = np.asarray(null)
    p = (np.sum(null > obs, axis=0) + 0.5) / (null.shape[0] + 1)
    if tail == "both":
        p = 2 * np.minimum(p, 1 - p)
    return p


def t_paired(d):
    d = np.asarray(d, float)
    n = d.shape[-1]
    return d.mean(-1) / (d.std(-1, ddof=1) / np.sqrt(n))


def t_pooled(a, b):
    na, nb = a.shape[-1], b.shape[-1]
    va, vb = a.var(-1, ddof=1), b.var(-1, ddof=1)
    sp = np.sqrt(((na - 1) * va + (nb - 1) * vb) / (na + nb - 2))
    return (a.mean(-1) - b.mean(-1)) / (sp * np.sqrt(1 / na + 1 / nb))


def perm_ttest_paired(x, y, rng, nperm=NPERM):
    """Paired permutation t-test (statcond 'paired','on','perm'): returns t, p, df."""
    d = np.asarray(x, float) - np.asarray(y, float)
    t = t_paired(d)
    signs = rng.choice([-1.0, 1.0], size=(nperm, d.size))
    tn = t_paired(signs * d)
    return float(t), float(_pval(tn, t)), d.size - 1


def perm_ttest_1samp(x, mu, rng, nperm=NPERM):
    """One-sample permutation test against mu, as a paired test of x against mu."""
    return perm_ttest_paired(np.asarray(x, float), np.full(len(x), mu), rng, nperm)


def perm_ttest_unpaired(a, b, rng, nperm=NPERM):
    """Unpaired permutation t-test (statcond 'paired','off','perm'): returns t, p."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    t = t_pooled(a, b)
    x = np.r_[a, b]
    perm = np.argsort(rng.random((nperm, x.size)), axis=1)
    xp = x[perm]
    with np.errstate(invalid="ignore", divide="ignore"):
        tn = t_pooled(xp[:, :a.size], xp[:, a.size:])
    tn = np.nan_to_num(tn, nan=0.0)
    return float(t), float(_pval(tn, t))


def f_oneway_groups(x, onehot):
    """One-way F for each row of x (rows: permutations or units) with groups given by onehot
    (n x k), or a stack of onehots (P x n x k) for permuted labels."""
    n, k = onehot.shape[-2:]
    cnt = onehot.sum(-2)
    sums = x @ onehot if onehot.ndim == 2 else np.einsum("n,pnk->pk", x, onehot)
    mean_all = x.mean()
    ss_between = np.sum(sums ** 2 / cnt, -1) - n * mean_all ** 2
    ss_total = np.sum((x - mean_all) ** 2)
    ss_within = ss_total - ss_between
    with np.errstate(invalid="ignore", divide="ignore"):
        return (ss_between / (k - 1)) / (ss_within / (n - k))


# ------------------------------------------------------------------------- selections

def category_rates(sess):
    """Rates 0.2 to 1.2 s after encoding pictures 1 to 3 (where shown) and the probe of every
    WM trial, with the category as the leading digit of the picture ID (claims C)."""
    wm = sess["wm"]
    times, cats = [], []
    for ts, pid in [("timestamps_Encoding1", "PicIDs_Encoding1"),
                    ("timestamps_Encoding2", "PicIDs_Encoding2"),
                    ("timestamps_Encoding3", "PicIDs_Encoding3"),
                    ("timestamps_Probe", "PicIDs_Probe")]:
        ok = (wm[ts].values != 0) & (wm[pid].values != 0) & np.isfinite(wm[ts].values)
        times.append(wm[ts].values[ok])
        cats.append(wm[pid].values[ok] // 100)
    return np.concatenate(times), np.concatenate(cats)


def category_test(rate, cats, rng, nperm=NPERM):
    """Selection C for one unit: permutation ANOVA, then the max category against the rest.
    Returns (is_category_neuron, preferred category, p_anova, p_t)."""
    ucat = np.unique(cats)
    onehot = (cats[:, None] == ucat[None, :]).astype(float)
    F = f_oneway_groups(rate, onehot)
    means = np.array([rate[cats == c].mean() for c in ucat])
    pref = ucat[np.argmax(means)]
    if not np.isfinite(F):
        return False, pref, np.nan, np.nan
    perm = np.argsort(rng.random((nperm, rate.size)), axis=1)
    Fn = np.nan_to_num(f_oneway_groups(rate, onehot[perm]), nan=0.0)
    p_anova = float(_pval(Fn, F, tail="one"))
    if p_anova >= 0.05:
        return False, pref, p_anova, np.nan
    _, p_t = perm_ttest_unpaired(rate[cats == pref], rate[cats != pref], rng, nperm)
    return bool(p_t < 0.1), pref, p_anova, p_t


def memory_test(sess, spikes, rng, nperm=NPERM):
    """Selection M for one unit: returns (p, mean old - mean new)."""
    ltm = sess["ltm"]
    ok = ltm.response_accuracy.values == 1
    c = count(spikes, ltm.timestamps_PicOnset.values[ok], 0.2, 1.2)
    old = ltm.new_old.values[ok] == 1
    t, p = perm_ttest_unpaired(c[old], c[~old], rng, nperm)
    return p, c[old].mean() - c[~old].mean()


# ------------------------------------------------------------------------- statistics

def outliers_methods(values):
    """Rule O-M: per unit and condition value, a unit is removed when any of its values lies
    outside mean +- 3 SD of all units' values in the tested conditions. values: units x conds."""
    v = np.asarray(values, float)
    m, s = np.nanmean(v), np.nanstd(v, ddof=1)
    return np.any(np.abs(v - m) > 3 * s, axis=1)


def mixedlm(df, formula, dv="FR"):
    """Normal LMM with random intercepts for patient and neuron nested in patient, by maximum
    likelihood. Returns a table with beta, SE, t, df and p (t distribution on n - p df)."""
    import statsmodels.formula.api as smf
    import warnings
    df = df.reset_index(drop=True)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        md = smf.mixedlm(f"{dv} ~ {formula}", df, groups="patient", re_formula="1",
                         vc_formula={"neuron": "0 + C(neuron)"})
        # lbfgs alone can stop at a local optimum of the variance parameters; three
        # optimizers are run and the fit with the highest likelihood is kept.
        fits = []
        for m in ("bfgs", "lbfgs", "powell"):
            try:
                fits.append(md.fit(reml=False, method=m))
            except Exception:
                pass
        res = max(fits, key=lambda r: r.llf)
    k = len(res.fe_params)
    dfree = len(df) - k
    b, se = res.fe_params, res.bse_fe
    t = b / se
    p = 2 * stats.t.sf(np.abs(t), dfree)
    out = pd.DataFrame({"beta": b, "SE": se, "t": t, "p": p})
    out.attrs.update(n=len(df), df=dfree, neurons=df.neuron.nunique(),
                     patients=df.patient.nunique(), converged=res.converged)
    return out


def cluster_test(a, b, rng, nperm=NPERM, clusteralpha=0.05):
    """Paired cluster-based permutation test across units (rows) over time (columns), FieldTrip
    style: dependent-samples t, two-sided cluster-forming threshold at clusteralpha, maxsum
    statistic, sign flips. Returns the t of each time point and a list of clusters (sign, start index, end index, sum, p)."""
    d = np.asarray(a, float) - np.asarray(b, float)
    n = d.shape[0]
    crit = stats.t.ppf(1 - clusteralpha / 2, n - 1)

    def clusters(t):
        out = []
        for sign in (1, -1):
            above = sign * t > crit
            i = 0
            while i < len(t):
                if above[i]:
                    j = i
                    while j + 1 < len(t) and above[j + 1]:
                        j += 1
                    out.append((sign, i, j, float(np.sum(t[i:j + 1]))))
                    i = j + 1
                else:
                    i += 1
        return out

    def tstat(x):
        return x.mean(0) / (x.std(0, ddof=1) / np.sqrt(n))

    t_obs = tstat(d)
    obs = clusters(t_obs)
    maxpos, minneg = np.zeros(nperm), np.zeros(nperm)
    for k in range(nperm):
        s = rng.choice([-1.0, 1.0], size=(n, 1))
        cl = clusters(tstat(s * d))
        pos = [c[3] for c in cl if c[0] == 1]
        neg = [c[3] for c in cl if c[0] == -1]
        maxpos[k] = max(pos) if pos else 0.0
        minneg[k] = min(neg) if neg else 0.0
    res = []
    for sign, i, j, ssum in obs:
        if sign == 1:
            p = (np.sum(maxpos >= ssum) + 1) / (nperm + 1)
        else:
            p = (np.sum(minneg <= ssum) + 1) / (nperm + 1)
        res.append(dict(sign=sign, start=i, end=j, sum=ssum, p=p))
    return t_obs, res


# ------------------------------------------------------------------------- tables

def picture_table(sess):
    """One row per encoding picture of every WM trial (slots 1 to 3 where shown), with its
    trial's load, WM accuracy and times, and, when the picture was shown in the LTM test, that
    trial's accuracy, confidence and picture onset."""
    wm, ltm = sess["wm"], sess["ltm"]
    lt = ltm.set_index("PicIDs")
    rows = []
    for i, tr in wm.iterrows():
        for slot in (1, 2, 3):
            pid = int(tr[f"PicIDs_Encoding{slot}"])
            if pid == 0:
                continue
            r = dict(trial=i, slot=slot, pic=pid, cat=pid // 100, load=int(tr.loads),
                     acc_WM=int(tr.response_accuracy), t_enc1=tr.timestamps_Encoding1,
                     t_maint=tr.timestamps_Maintenance, t_enc=tr[f"timestamps_Encoding{slot}"],
                     probe=int(tr.PicIDs_Probe))
            if pid in lt.index:
                m = lt.loc[pid]
                r.update(in_ltm=True, LTMacc=int(m.response_accuracy), conf=int(m.confidence),
                         t_ltm=float(m.timestamps_PicOnset))
            else:
                r.update(in_ltm=False, LTMacc=np.nan, conf=np.nan, t_ltm=np.nan)
            rows.append(r)
    return pd.DataFrame(rows)


def add_counts(pt, spikes):
    """Spike counts per picture row: maintenance 0 to 2.5 s, baseline -0.9 to -0.3 s before
    encoding picture 1, encoding picture 1 0 to 2 s (claims B; Methods, Relating WM maintenance
    activity to LTM formation), and LTM 0.2 to 1.2 s after the picture's LTM onset."""
    pt = pt.copy()
    pt["c_maint"] = count(spikes, pt.t_maint.values, 0.0, 2.5)
    pt["c_bsl"] = count(spikes, pt.t_enc1.values, -0.9, -0.3)
    pt["c_enc1"] = count(spikes, pt.t_enc1.values, 0.0, 2.0)
    ok = np.isfinite(pt.t_ltm.values)
    c = np.full(len(pt), np.nan)
    c[ok] = count(spikes, pt.t_ltm.values[ok], 0.2, 1.2)
    pt["c_ltm"] = c
    pt["r_maint"] = pt.c_maint / 2.5
    pt["r_bsl"] = pt.c_bsl / 0.6
    pt["r_enc1"] = pt.c_enc1 / 2.0
    return pt


def conf3_code(conf):
    """The Fig. 3a code's recoding (NWB_computeGLM.m): 4, 5, 6 to 1, 2, 3; 1, 2, 3 kept, so
    forgotten sure 1 ... guessing 3 and remembered guessing 1 ... sure 3 (claims, fig3a)."""
    conf = np.asarray(conf, float)
    return np.where(conf >= 4, conf - 3, conf)


def conf3_certainty(conf):
    """Certainty coding: sure 3 (1 or 6), unsure 2 (2 or 5), guessing 1 (3 or 4)."""
    conf = np.asarray(conf, float)
    return np.where(conf >= 4, conf - 3, 4 - conf)


def roc_auc(pos, neg, nthr=25):
    """ROC with nthr thresholds linearly spaced from the minimal to the maximal count of the
    two groups, AUC by the trapezoid rule (Methods, Single-neuron AUC analysis). pos is the
    group expected to fire more."""
    pos, neg = np.asarray(pos, float), np.asarray(neg, float)
    allv = np.r_[pos, neg]
    thr = np.linspace(allv.min(), allv.max(), nthr)
    tpr = np.r_[0.0, [np.mean(pos >= t) for t in thr[::-1]]]
    fpr = np.r_[0.0, [np.mean(neg >= t) for t in thr[::-1]]]
    return float(np.trapezoid(tpr, fpr))


# Table S1 of the paper (supplement, page 7 to 8), reference values for claim table-s1-counts:
# session label, WM and LTM accuracy (%), and per area category-selective / memory-selective /
# recorded counts. The two sessions marked * in the paper (P87cs, P1901jh) were excluded there
# and are not in the dandiset.
TABLE_S1 = """
P54cs_2 93.6 76.8 3/0/7 5/2/17
P55cs 97.1 72.8 0/0/1 7/3/21
P55cs_2 97.1 74.8 2/2/8 13/1/25
P57cs_2 91.4 67.5 1/0/4 14/5/24
P58cs 97.9 86.3 0/1/2 9/4/27
P61cs 87.1 68.8 6/2/12 6/2/11
P61cs_2 97.9 72.3 0/0/2 7/3/8
P62cs 97.1 80.8 0/2/3 5/0/19
P64cs 78.6 56.8 0/0/0 3/0/17
P65cs 94.3 72 5/0/9 7/3/18
P67cs 97.9 80.8 0/0/0 5/1/12
P68cs 92.1 58 3/3/16 1/0/17
P69cs 75 64.8 3/2/8 4/0/7
P70cs 98.6 68.3 0/0/1 5/7/14
P70cs_2 96.4 73.9 0/0/1 0/0/5
P71cs 96.4 69 0/0/0 0/0/3
P73cs 92.1 60.5 0/1/5 7/1/17
P74cs 97.9 73 0/0/0 6/0/9
P76cs 99.3 78.5 4/0/6 12/1/25
P76cs_2 100 90 0/0/0 0/0/4
P77cs 94.3 73 2/2/4 12/12/41
P78cs 97.1 59.8 0/1/13 0/1/14
P79cs 97.9 68.8 6/2/17 14/4/28
P79cs_2 97.1 80.5 4/0/13 9/3/19
P80cs 100 82.3 4/7/13 20/9/49
P82cs 98.6 69.5 11/2/17 12/1/24
P88T 99.3 76.3 3/1/22 0/0/6
P89T 97.1 57 7/3/22 11/0/18
P90T_2 91.4 57.8 0/0/11 0/0/2
P90T_3 90.7 55.8 0/1/13 0/0/0
P93T 83.6 62.7 0/0/4 0/0/3
P96T 90 65 4/0/6 0/0/5
P101T 100 87 6/3/16 5/0/5
P101T_2 100 90 5/3/8 5/3/6
P103T 96.4 61.5 4/2/20 3/0/11
P106T 84.3 58.3 1/0/7 6/1/14
P109T 100 85.8 1/2/15 0/0/7
P110T 99.3 64.3 0/0/6 1/0/10
P113T_2 97.1 60.8 2/2/11 1/1/7
P116T 97.9 65 4/1/9 5/0/18
P1802jh 90.7 70.3 5/1/12 0/0/0
P1809jh 75.7 57 0/1/6 0/0/0
P1811jh 76.4 61 1/0/10 0/0/0
P1814jh 90.7 76.8 1/3/8 0/0/0
P1903jh 99.3 82 0/0/2 0/0/0
P1912jh 70.7 60.5 6/3/16 0/0/0
"""


def table_s1():
    rows = []
    for line in TABLE_S1.strip().split("\n"):
        lab, wm, ltm, h, a = line.split()
        h, a = [list(map(int, x.split("/"))) for x in (h, a)]
        rows.append(dict(label=lab, wm_acc=float(wm), ltm_acc=float(ltm), h_cat=h[0], h_ms=h[1],
                         h_rec=h[2], a_cat=a[0], a_ms=a[1], a_rec=a[2]))
    return pd.DataFrame(rows)


def s1_label(identifier):
    """Table S1 label of a session from the file's identifier: sub-1_ses-2_P54CS -> P54cs_2,
    sub-22_ses-1_P088TWH -> P88T, sub-34_ses-1_P1802JHU -> P1802jh. The session suffix is the
    session number when it is not 1."""
    _, ses, pat = identifier.split("_")
    num = int("".join(ch for ch in pat[1:] if ch.isdigit()))
    site = {"CS": "cs", "TWH": "T", "JHU": "jh"}[pat.lstrip("P0123456789")]
    s = int(ses.split("-")[1])
    return f"P{num}{site}" + ("" if s == 1 else f"_{s}")


def normalize(rate, base_mean):
    """Percent change to the mean baseline rate (claims B)."""
    return (rate / base_mean - 1.0) * 100.0


def om_remove(df, conds, value="FR", unit="neuron", zero_col=None, marginal=False):
    """Rule O-M (Methods, Statistics) for a table of rows: per unit and condition (the
    combinations of the columns conds), the mean of value; a unit is removed when it has no
    spikes in a tested condition (zero_col summed over the condition's rows is 0) or when any
    condition mean lies outside mean +- 3 SD of all unit and condition means. Returns the set
    of removed units."""
    if marginal:
        # conditions are the levels of each factor separately
        ms = [df.groupby([unit, c])[value].mean() for c in conds]
        allv = np.concatenate([m.values for m in ms])
        mu, sd = allv.mean(), allv.std(ddof=1)
        bad = set()
        for m in ms:
            bad |= set(m.index.get_level_values(0)[np.abs(m.values - mu) > 3 * sd])
    else:
        m = df.groupby([unit] + conds)[value].mean()
        bad = set(m.index.get_level_values(0)[np.abs(m.values - m.mean()) > 3 * m.std()])
    g = df.groupby([unit] + conds)
    if zero_col is not None:
        z = g[zero_col].sum()
        bad |= set(z.index.get_level_values(0)[z.values == 0])
    return bad


def og_remove(df, value="FR", unit="neuron"):
    """Rule O-G (claims O, the reading for the GLMs of Figures 2 and 3): each unit's mean value
    over all its rows, as NWB_computeGLM.m computes it; units whose mean lies outside the mean
    +- 3 SD of the unit means are removed ("differed ±3 SD from the mean", Methods, Statistics)."""
    m = df.groupby(unit)[value].mean()
    return set(m.index[np.abs(m - m.mean()) > 3 * m.std()])


def oc_remove(df, value="FR", unit="neuron"):
    """Rule O-C (NWB_computeGLM.m): units whose mean value over all their rows exceeds 3 SD of
    the unit means, without centring and on the upper side only."""
    m = df.groupby(unit)[value].mean()
    return set(m.index[m > 3 * m.std()])


def binned_counts(spikes, t0, centres, width):
    """Spike counts in windows [c - width/2, c + width/2) around each centre, per event."""
    t0 = np.asarray(t0, float)[:, None]
    lo = t0 + np.asarray(centres)[None, :] - width / 2
    return (np.searchsorted(spikes, lo + width, side="left")
            - np.searchsorted(spikes, lo, side="left"))


def read_images(path, ids):
    """Stimulus images of one session (stimulus/templates/StimulusTemplates, named image_<ID>),
    for the picture IDs given that the file holds."""
    asset = next(a for a in list_assets() if a["path"] == path)
    f = h5py.File(remfile.File(s3_url(asset["asset_id"])), "r")
    g = f["stimulus/templates/StimulusTemplates"]
    out = {i: g[f"image_{i}"][:] for i in ids if f"image_{i}" in g}
    f.close()
    return out


def contact_sheet(images, old_ids, new_ids, w=60, h=80):
    """JPEG of the images, one band per category 1 to 5: the old pictures whose leading digit
    is the category, then the new pictures of the matching block of 40 IDs, each with its ID.
    Images are drawn as stored in the file."""
    from io import BytesIO
    from PIL import Image, ImageDraw
    cols = 20
    bands = []
    for k in range(1, 6):
        old = [i for i in old_ids if i // 100 == k and i in images]
        new = [i for i in new_ids if (i - 1001) // 40 + 1 == k and i in images]
        bands.append([("old %d" % k, old), ("new %d" % k, new)])
    nrows = sum(-(-len(ids) // cols) for b in bands for _, ids in b)
    sheet = Image.new("RGB", (40 + cols * w, nrows * (h + 12)), "white")
    draw = ImageDraw.Draw(sheet)
    y = 0
    for b in bands:
        for label, ids in b:
            for r in range(0, len(ids), cols):
                draw.text((2, y + h // 2), label, fill="black")
                for j, i in enumerate(ids[r:r + cols]):
                    x = 40 + j * w
                    sheet.paste(Image.fromarray(images[i]).resize((w, h)), (x, y + 12))
                    draw.text((x + 2, y), str(i), fill="black")
                y += h + 12
    buf = BytesIO()
    sheet.save(buf, format="JPEG", quality=80)
    return buf.getvalue()
