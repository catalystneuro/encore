"""Loading and measures for dandiset 000473 (Calvigioni, Fuzik, Le Merre et al. 2023).

The dandiset holds the Neuropixels recordings in the mPFC of 25 head-fixed mice (Fig. 4 and
Extended Data Figs. 7 to 9 of the paper). Files are streamed from the archive at the pinned
version; nothing is written to disk.

Where each parameter comes from:
- REGIONS, MIN_FR, MAX_ISI, the saturation margin of 1 s: Methods, "In vivo electrophysiological
  data analysis" (units in ACAd, PL, ILA, ORBm, firing rate > 0.1 Hz, ISI violations < 1 %, spikes
  within 1 s of saturation periods removed), as the claims file cites. The saturation periods are
  the files' 'spike saturation' series, which the paper's code reads for this step; the 'LFP
  saturation' series the Methods' wording points to is a variant (an assumption, see notebook).
- Region by substring of the main channel's location, main channel 0-indexed, ISI violations as
  the units table's quality[:, 0] count over the spike count: Fig4g_GLM_tuning.m of
  Esr1_NPX_code at commit 85187f3 (claims file, code-outputs-link and ed7a-unit-counts).
- GLM: 100 ms bins, regressors sound 1 and sound 2 (200 ms after onset), opto (500 ms after light
  onset), air puff (500 ms after onset), Poisson log link (Methods, "Generalized linear model");
  predictor order [sound 1, opto, sound 2, air puff] and the whole session as the fitted period
  (GLM_restrict = 0), the code. 1,000 circular shifts of the session at one random point each,
  tuning score and the 99.9th / 0.01th percentile rule (Methods, "Tuning scores"); percentiles as
  MATLAB's prctile computes them, as in Fig4g_Extended_Data_Fig8abfgjklm_GLM_Tuning_score.m.
- With mutually exclusive 0/1 regressors and an intercept, the Poisson maximum-likelihood fit has a
  closed form: each beta is the log of the mean count in the regressor's bins over the mean count
  in the bins with no regressor. glm_betas uses it (exact, not an approximation), and the shifted
  fits are computed for all shifts at once by FFT cross-correlation. A regressor with no spike in
  its bins has no finite maximum-likelihood beta (glmfit returns a large negative value after its
  iterations); here it is set to log(0.5 / n_bins) - log(baseline mean), a standard choice that
  only affects such rare cases, which are counted. In one session (147463) light trains outside
  block 2 overlap other regressors in 288 bins; the closed form needs exclusive regressors, so
  those bins are left out of that session's fit, a choice here.
"""
import json
import time
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET = "000473"
VERSION = "0.230417.1502"
API = "https://api.dandiarchive.org/api"
REGIONS = ["ACAd", "PL", "ILA", "ORBm"]
MIN_FR = 0.1
MAX_ISI = 0.01
SAT_MARGIN = 1.0
GENOTYPE_SHORT = {"C57BL/6J (JAX strain)": "Ctl", "Vglut2-cre": "Vglut2", "NPY-Cre": "Npy",
                  "Esr1-Cre": "Esr1"}
GENOTYPES = ["Ctl", "Vglut2", "Npy", "Esr1"]
PREDICTORS = ["sound1", "opto", "sound2", "airpuff"]


def list_assets():
    r = requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/",
                     params={"page_size": 200})
    r.raise_for_status()
    return sorted(r.json()["results"], key=lambda a: a["path"])


def asset_url(asset_id):
    """The public S3 URL of an asset, from its metadata."""
    r = requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/{asset_id}/")
    r.raise_for_status()
    return [u for u in r.json()["contentUrl"] if "amazonaws" in u][0]


def _str(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def unit_region(location):
    """Region of a main-channel location label, by substring as in the code; None if not one."""
    hits = [r for r in REGIONS if r in location]
    return hits[0] if len(hits) == 1 else None


def load_session(asset, keep_spikes="pfc"):
    """Stream one NWB file. Returns a dict with metadata, trials, stimuli, units table and the
    spike times of the units in the four PFC regions (all units when keep_spikes == "all")."""
    url = asset_url(asset["asset_id"])
    with h5py.File(remfile.File(url), "r") as f:
        s = {"path": asset["path"], "session_id": _str(f["general/session_id"][()])}
        subj = f["general/subject"]
        for k in ("subject_id", "genotype", "sex", "age"):
            s[k] = _str(subj[k][()])
        s["geno"] = GENOTYPE_SHORT[s["genotype"]]
        s["opto_site"] = _str(f["general/optogenetics/OptogeneticStimulusSite/location"][()])
        beh = f["processing"].get("behavior")
        s["behavior"] = {f"{k}/{kk}": f[f"processing/behavior/{k}/{kk}/data"].shape
                         for k in beh.keys() for kk in beh[k].keys()} if beh is not None else {}
        T = f["intervals/trials"]
        s["trials"] = pd.DataFrame({c: T[c][:] for c in T.keys()
                                    if c not in ("id", "opto_pulse_ts")})
        s["opto_pulse_ts"] = T["opto_pulse_ts"][:]
        stim = {}
        for k in f["stimulus/presentation"].keys():
            g = f["stimulus/presentation/" + k]
            stim[k] = (g["timestamps"][:], g["data"][:])
        s["stim"] = stim
        sat = {}
        for k in f["analysis"].keys():
            sat[k] = f["analysis/" + k + "/timestamps"][:]
        s["saturation"] = sat
        loc = np.array([_str(x) for x in f["general/extracellular_ephys/electrodes/location"][:]])
        idx = f["units/spike_times_index"][:].astype(np.int64)
        start = np.concatenate([[0], idx[:-1]])
        q = f["units/quality"][:]
        u = pd.DataFrame({
            "unit": np.arange(len(idx)),
            "id": f["units/id"][:],
            "electrode": f["units/electrodes"][:],
            "isi_count": q[:, 0],
            "isi_fp": q[:, 1],
            "n_spikes": idx - start,
            "FS": f["units/FS"][:],
            "RS": f["units/RS"][:],
            "peak_to_trough": f["units/Peak_to_Trough"][:],
        })
        u["location"] = loc[u["electrode"].values]
        u["region"] = [unit_region(x) for x in u["location"]]
        st = f["units/spike_times"][:]
        s["t_end"] = float(st.max())
        s["t_first"] = float(st.min())
        keep = u.index[u["region"].notna()] if keep_spikes == "pfc" else u.index
        s["spikes"] = {int(i): st[start[i]:idx[i]].copy() for i in keep}
        del st
    s["units"] = u
    return s


def load_all(assets, workers=6, **kw):
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(lambda a: load_session(a, **kw), assets))


def remove_saturation(spikes, sat_start, sat_stop, margin=SAT_MARGIN):
    """Drop spikes within `margin` s of an LFP saturation period."""
    keep = np.ones(len(spikes), bool)
    for a, b in zip(sat_start, sat_stop):
        keep &= ~((spikes >= a - margin) & (spikes <= b + margin))
    return spikes[keep]


def select_units(s, fr_denominator="t_end"):
    """The Methods' selection (ed7a-unit-counts). Adds columns isi_rate, mean_fr, selected.
    Mean session rate = spike count over the recording duration (last spike time), compared in
    the notebook with the code's Mean_FR outputs."""
    u = s["units"]
    dur = s["t_end"]
    u["isi_rate"] = u["isi_count"] / u["n_spikes"]
    u["mean_fr"] = u["n_spikes"] / dur
    u["selected"] = u["region"].notna() & (u["isi_rate"] < MAX_ISI) & (u["mean_fr"] > MIN_FR)
    return u


def clean_spikes(s, series="spike"):
    """Spike times of the selected units with spikes within 1 s of a saturation period removed.
    series="spike" reads the files' 'spike saturation start/stop' series, as the paper's code does
    (RemoveSaturationSpikes in utilities/MS_suppl_functions.py, +- 1 s); series="LFP" reads the
    'LFP saturation' series, the Methods' words (see the notebook for why the first is used)."""
    a = s["saturation"].get(f"{series} saturation start", [])
    b = s["saturation"].get(f"{series} saturation stop", [])
    u = s["units"]
    return {int(i): remove_saturation(s["spikes"][int(i)], a, b) for i in u.index[u["selected"]]}


# ---------------------------------------------------------------- GLM

def session_bins(s, bin_sz=0.1):
    return int(np.ceil(s["t_end"] / bin_sz))


def train_onsets(times, gap=0.3):
    """First pulse of each light train in a pulse time series."""
    times = np.sort(times)
    return times[np.concatenate([[True], np.diff(times) > gap])]


def regressor_bins(s, opto="all", bin_sz=0.1, nbins=None):
    """0/1 regressor per 100 ms bin: sound 1 (pure tone) and sound 2 (blue noise) 200 ms from onset,
    opto 500 ms from light-train onset, air puff 500 ms from onset (Methods). opto="all" marks every
    light train of the session, "block2" those of block 2 only. Returns a (4, nbins) int array and
    the number of bins where two regressors overlap."""
    nb = nbins or session_bins(s, bin_sz)
    X = np.zeros((4, nb), int)
    st = s["stim"]
    ons = {
        "sound1": st["AudStim_10kHz"][0],
        "sound2": st["passive_bluenoise"][0],
        "airpuff": st["air_puff"][0],
    }
    otr = train_onsets(st["OptogeneticSeries"][0])
    if opto == "block2":
        tr = s["trials"]
        b2 = tr[tr.Block == 2]
        otr = np.array([o for o in otr if ((o >= b2.start_time.values) &
                                          (o <= b2.stop_time.values)).any()])
    ons["opto"] = otr
    dur = {"sound1": 0.2, "sound2": 0.2, "opto": 0.5, "airpuff": 0.5}
    for k, name in enumerate(PREDICTORS):
        for t in ons[name]:
            a = int(np.floor(t / bin_sz))
            b = int(np.ceil((t + dur[name]) / bin_sz))
            X[k, max(a, 0):min(b, nb)] = 1
    overlap = int((X.sum(0) > 1).sum())
    return X, overlap


def bin_counts(spikes, nbins, bin_sz=0.1):
    c = np.bincount(np.minimum((spikes / bin_sz).astype(np.int64), nbins - 1), minlength=nbins)
    return c[:nbins]


def matlab_prctile(x, p):
    """MATLAB prctile: sorted values at positions 100*(i-0.5)/n, linear between, clamped."""
    x = np.sort(x)
    n = len(x)
    pos = np.clip(n * p / 100.0 + 0.5, 1, n)
    lo = int(np.floor(pos))
    hi = min(lo + 1, n)
    return x[lo - 1] + (pos - lo) * (x[hi - 1] - x[lo - 1])


def _betas_from_sums(sums, nreg, base_sum, nbase):
    """Closed-form Poisson betas from the spike sums in each regressor's bins."""
    mb = base_sum / nbase
    m = sums / nreg
    floor = 0.5 / nreg
    zero = m <= 0
    m = np.where(zero, floor, m)
    return np.log(m) - np.log(mb), zero


def glm_tuning(counts, X, n_shift=1000, rng=None):
    """True betas, tuning scores and tuned flags (+1, -1, 0) for one unit's binned counts.
    Shifts: spk_cnt_circshift = [spk_cnt(T+1:end) spk_cnt(1:T)], T = round(rand * nbins), as in
    Fig4g_GLM_tuning.m. Returns dict."""
    nb = len(counts)
    Xb = X.astype(bool)
    over = Xb.sum(0) > 1
    Xb = Xb & ~over  # bins where two regressors overlap are left out of the fit (one session)
    base = ~Xb.any(0) & ~over
    nreg = Xb.sum(1)
    nbase = base.sum()
    # sums over each set for every circular shift: S_k(T) = sum_i X_k[i] * y[(i + T) mod nb]
    fy = np.fft.rfft(counts.astype(float))
    sums_all = np.empty((5, nb))
    for k in range(4):
        fx = np.fft.rfft(Xb[k].astype(float))
        sums_all[k] = np.fft.irfft(np.conj(fx) * fy, nb)
    fx = np.fft.rfft(base.astype(float))
    sums_all[4] = np.fft.irfft(np.conj(fx) * fy, nb)
    sums_all = np.rint(sums_all)
    Ts = np.rint(rng.random(n_shift) * nb).astype(int) % nb
    true_b, true_zero = _betas_from_sums(sums_all[:4, 0], nreg, sums_all[4, 0], nbase)
    sb, s_zero = _betas_from_sums(sums_all[:4, Ts], nreg[:, None], sums_all[4, Ts], nbase)
    mu = sb.mean(1)
    sd = sb.std(1, ddof=1)
    score = (true_b - mu) / sd
    tuned = np.zeros(4, int)
    for k in range(4):
        up = matlab_prctile(sb[k], 99.9)
        lo = matlab_prctile(sb[k], 0.01)
        tuned[k] = 1 if true_b[k] >= up else (-1 if true_b[k] <= lo else 0)
    return {"beta": true_b, "score": score, "tuned": tuned,
            "zero_true": true_zero, "zero_shift": int(s_zero.sum())}


# ---------------------------------------------------------------- trial-aligned counts

def aligned_counts(spikes, onsets, t0, t1, bin_sz):
    """Spike counts (n_trials, n_bins) in bins from t0 to t1 around each onset."""
    edges = np.arange(t0, t1 + bin_sz / 2, bin_sz)
    nb = len(edges) - 1
    out = np.zeros((len(onsets), nb))
    for j, o in enumerate(onsets):
        a, b = np.searchsorted(spikes, [o + t0, o + t1])
        if b > a:
            out[j] = np.histogram(spikes[a:b] - o, edges)[0]
    return out


def block_onsets(s, block, every_other=False):
    tr = s["trials"]
    on = tr.loc[tr.Block == block, "start_time"].values
    if every_other:
        on = on[::2]
    return on


# ---------------------------------------------------------------- session table and outside inputs

CODE_REPO = "https://github.com/PierreLeMerre/Esr1_NPX_code"
CODE_COMMIT = "85187f3"  # the commit the claims file read
CODE_RAW = "https://raw.githubusercontent.com/PierreLeMerre/Esr1_NPX_code/" + CODE_COMMIT + "/"


def code_session_table():
    """utilities/Aversion_session_description.tsv of the paper's code: session -> genotype."""
    r = requests.get(CODE_RAW + "utilities/Aversion_session_description.tsv")
    r.raise_for_status()
    rows = [l.split("\t") for l in r.text.splitlines()[1:] if l.strip()]
    t = pd.DataFrame({"session_id": [x[0].replace(".nwb", "") for x in rows],
                      "code_genotype": [x[1] for x in rows],
                      "analyze": [int(x[2]) for x in rows]})
    t["geno_code"] = t["code_genotype"].map(
        lambda g: {"NPY-Cre": "Npy", "Vglut2-cre": "Vglut2", "C57BL-6J": "Ctl"}.get(g, "Esr1"))
    return t


def code_mat(path):
    """A .mat file of the paper's code repository at the pinned commit, read in memory."""
    import io
    import scipy.io as sio
    r = requests.get(CODE_RAW + path)
    if r.status_code == 404:
        return None
    r.raise_for_status()
    return sio.loadmat(io.BytesIO(r.content))


def glm_period_end(s):
    """End of the GLM period under the 'blocks 1 to 4' reading: 2 s before the first block-5 trial,
    the restriction written (commented out) in Fig4g_GLM_tuning.m (last_block = 4,
    stop_time = trial_ts(bb) - 2)."""
    tr = s["trials"]
    return float(tr.start_time[tr.Block == 5].min() - 2)


def regressors_from_stim(s, t_stop, bin_sz=0.1):
    """Regressor bins over [0, t_stop) from the stimulus series."""
    nb = int(round(t_stop / bin_sz))
    X, ov = regressor_bins(s, "all", bin_sz, nbins=nb)
    return X, ov, nb


def run_glm(S, period="blocks1to4", clean=True, min_count=0.2, seed=0):
    """GLM tuning for every selected unit whose mean count per 100 ms bin exceeds min_count.
    period: "blocks1to4" (0 to glm_period_end) or "session" (0 to the last spike).
    Returns a DataFrame, one row per selected unit, with fitted flag, scores and tuned flags."""
    rows = []
    for s in S:
        rng = np.random.default_rng([seed, int(s["subject_id"])])
        u = s["units"]
        t_stop = glm_period_end(s) if period == "blocks1to4" else s["t_end"]
        X, ov, nb = regressors_from_stim(s, t_stop)
        sp = s["clean"] if clean else s["spikes"]
        for i in u.index[u["selected"]]:
            x = sp[int(i)]
            c = bin_counts(x[x < nb * 0.1], nb)
            row = {"session_id": s["session_id"], "unit": int(i), "geno": s["geno_code"],
                   "region": u.at[i, "region"], "mean_count": c.mean(),
                   "fitted": c.mean() > min_count, "overlap_bins": ov}
            if row["fitted"]:
                r = glm_tuning(c, X, rng=rng)
                for k, p in enumerate(PREDICTORS):
                    row["beta_" + p] = r["beta"][k]
                    row["score_" + p] = r["score"][k]
                    row["tuned_" + p] = r["tuned"][k]
                row["zero_true"] = int(r["zero_true"].sum())
                row["zero_shift"] = r["zero_shift"]
            rows.append(row)
    return pd.DataFrame(rows)


def primary_secondary(g, signed=False):
    """Primary and secondary tuning (index into PREDICTORS) per unit: the largest and second
    largest absolute tuning score (Methods), or signed score (the code's variant)."""
    sc = g[["score_" + p for p in PREDICTORS]].values
    key = sc if signed else np.abs(sc)
    order = np.argsort(-key, axis=1)
    return order[:, 0], order[:, 1]


def trial_avg(spikes, onsets, t0, t1, bin_sz):
    """Trial-averaged rate (Hz) in bins from t0 to t1 around the onsets (vectorized)."""
    nb = int(round((t1 - t0) / bin_sz))
    a = np.searchsorted(spikes, onsets + t0)
    b = np.searchsorted(spikes, onsets + t1)
    if (b - a).sum() == 0:
        return np.zeros(nb)
    rel = np.concatenate([spikes[i:j] - o for i, j, o in zip(a, b, onsets)])
    k = np.floor((rel - t0) / bin_sz + 1e-9).astype(int)
    k = k[(k >= 0) & (k < nb)]
    return np.bincount(k, minlength=nb)[:nb] / (len(onsets) * bin_sz)


def block_psths(s, units, t0, t1, bin_sz, every_other_b2=True):
    """(n_units, 4 blocks, n_bins) trial-averaged rates for blocks 1 to 4. Block 2: every other trial
    when every_other_b2 (as the clustering code and the Methods for heatmaps), else all trials."""
    on = [block_onsets(s, b, every_other=(b == 2 and every_other_b2)) for b in (1, 2, 3, 4)]
    nb = int(round((t1 - t0) / bin_sz))
    out = np.zeros((len(units), 4, nb))
    for j, i in enumerate(units):
        for b in range(4):
            out[j, b] = trial_avg(s["clean"][i], on[b], t0, t1, bin_sz)
    return out


def window_rates(spikes, onsets, t0, t1):
    """Rate (Hz) in [onset + t0, onset + t1) for each onset."""
    a = np.searchsorted(spikes, onsets + t0)
    b = np.searchsorted(spikes, onsets + t1)
    return (b - a) / (t1 - t0)
