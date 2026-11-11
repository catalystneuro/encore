"""Loading and response measures for CRCNS vta-1 (Starkweather, Gershman & Uchida 2018).

The data set is CRCNS vta-1 (doi:10.6080/K01J97X6), which CRCNS does not version
(version "unversioned"). It is one zip, `vta-1/live/data.zip`, MD5
c5d2a9f8aaf699cbdd2bda1bace22e7e in the data set's `checksums.md5`, streamed
from the public S3 bucket `crcnsarchive` and opened in place with fsspec and
zipfile. Each member is one light-identified dopamine neuron, named
`<Saline|SalB>_Task<1|2>_<n>.mat`, holding `odor_onsets`, `reward_onsets`,
`spiketimes` (all in ms) and `trial_type` (data description, version 0.6).

Where each parameter comes from:

- Post-reward response, spikes 50 to 200 ms after reward onset; pre-reward
  response, spikes 0 to 400 ms before reward onset (Methods, Data analysis),
  with 0 to 200 ms as the other reading (Figure 4A legend); both
  baseline-subtracted, baseline 0 to 1 s before odor onset (Methods, Data
  analysis). These are fixed in the claims file's opening comment. Responses are
  rates in spikes/s, as the figures plot them (claims file).
- Omission response, spikes 0 to 1000 ms after the usual reward time (Methods,
  Data analysis); the usual time is 1.2 s for odor B and 2.8 s for odor C
  (Figure 3F; claim fig6cd-omission-dips-intact).
- Omission epochs, 200 ms from odor onset to 6 s (Figure S5D legend and axes;
  claim figs5d-omission-unchanged-by-salb).
- Baseline subtraction trial by trial, by the neuron's mean baseline, or none:
  the paper does not say which, and the claims file names all three as readings
  (fig5f-task2-slope-signs). Trial by trial is the default here, as the
  Methods describe responses "baseline-subtracted, with baseline taken 0-1 s
  prior to odor onset" for each response window.
- "We analyzed data recorded in the 40 minutes following recording onset"
  (Methods, Data analysis). The files hold no recording onset. Two readings:
  `window="file"` keeps every trial in the file (the files' trials span at most
  38.3 min, so they may already be cut to 40 min), `window="40min"` keeps the
  trials whose odor onset is within 40 min of the first spike of the session
  (the earliest spike of any neuron recorded in it), the only stand-in for the
  recording onset the files hold.
- Sessions are recovered as groups of files with identical `odor_onsets`;
  the files carry no session or subject identifier.
- Trial types 1 to 9 are odor A with ISIs 1.2 to 2.8 s, 10 and 11 odor B and C,
  13 to 15 omissions of A to C, 16 odor D (data description). Trials whose type
  is missing (NaN) are left out.
"""

import hashlib
import io
import re
import zipfile

import fsspec
import numpy as np
import pandas as pd
import scipy.io as sio
from scipy import stats

BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/vta-1/live/"
DATA_ZIP = BASE + "data.zip"
DATASET = "crcns:vta-1/unversioned"
DOI = "10.6080/K01J97X6"
EXPECTED_MD5 = "c5d2a9f8aaf699cbdd2bda1bace22e7e"

ISI_S = {t: round(1.0 + 0.2 * t, 1) for t in range(1, 10)}
USUAL_REWARD_S = {14: 1.2, 15: 2.8}

POST = (50, 200)        # ms after reward onset
PRE = {"400": 400, "200": 200}  # ms before reward onset
BASE_WIN = 1000         # ms before odor onset
OMIT = 1000             # ms after the usual reward time


def checksums():
    """The data set's checksums.md5, and the S3 ETag of data.zip (its MD5)."""
    fs = fsspec.filesystem("https")
    text = fs.cat(BASE + "checksums.md5").decode()
    md5 = dict(reversed(line.split()) for line in text.strip().splitlines())
    etag = fs.info(DATA_ZIP).get("ETag", "").strip('"')
    return md5, etag


def load():
    """Stream data.zip and return {name: dict of arrays} for every neuron file.

    Also returns the MD5 of the bytes read, so the notebook can compare it with
    checksums.md5 (the zip is 7.9 MB and is read once, in memory).
    """
    with fsspec.open(DATA_ZIP, block_size=2**20) as f:
        raw = f.read()
    md5 = hashlib.md5(raw).hexdigest()
    neurons = {}
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        for name in sorted(z.namelist()):
            if not name.endswith(".mat"):
                continue
            m = sio.loadmat(io.BytesIO(z.read(name)))
            neurons[name.split("/")[-1][:-4]] = {
                k: np.asarray(m[k], dtype=float).ravel()
                for k in ("odor_onsets", "reward_onsets", "spiketimes", "trial_type")
            }
    return neurons, md5


def neuron_table(neurons):
    """One row per neuron: drug, task, file number, session id and counts."""
    rows = []
    sessions = {}
    for name, d in neurons.items():
        drug, task, num = re.match(r"(Saline|SalB)_Task(\d)_(\d+)$", name).groups()
        key = d["odor_onsets"].tobytes()
        sessions.setdefault(key, f"S{len(sessions) + 1:02d}")
        rows.append(dict(neuron=name, drug=drug, task=int(task), num=int(num),
                         session=sessions[key], n_trials=len(d["trial_type"]),
                         n_spikes=len(d["spiketimes"])))
    df = pd.DataFrame(rows)
    first = {n: d["spiketimes"][0] for n, d in neurons.items()}
    df["session_start"] = df.groupby("session")["neuron"].transform(
        lambda s: min(first[n] for n in s))
    return df


def _count(spikes, starts, t0, t1):
    """Spikes in [start + t0, start + t1) ms for each start (NaN start gives NaN)."""
    starts = np.asarray(starts, dtype=float)
    out = np.full(len(starts), np.nan)
    ok = np.isfinite(starts)
    out[ok] = (np.searchsorted(spikes, starts[ok] + t1, "left")
               - np.searchsorted(spikes, starts[ok] + t0, "left"))
    return out


def trials(neurons, table, window="file"):
    """One row per trial with the response measures, in spikes/s.

    Columns: base (rate 0-1 s before odor), post_raw (rate 50-200 ms after
    reward), pre400_raw / pre200_raw (rate before reward), omit_raw (rate 0-1 s
    after the usual reward time, omission trials of B and C), and the
    baseline-subtracted versions without `_raw`.
    """
    out = []
    for row in table.itertuples():
        d = neurons[row.neuron]
        sp = d["spiketimes"]
        odor, rew, tt = d["odor_onsets"], d["reward_onsets"], d["trial_type"]
        df = pd.DataFrame(dict(neuron=row.neuron, drug=row.drug, task=row.task,
                               session=row.session, trial=np.arange(len(tt)),
                               type=tt, odor=odor, reward=rew))
        df["minutes"] = (odor - row.session_start) / 60000.0
        df["base"] = _count(sp, odor, -BASE_WIN, 0) / (BASE_WIN / 1000)
        df["post_raw"] = _count(sp, rew, *POST) / ((POST[1] - POST[0]) / 1000)
        for k, w in PRE.items():
            df[f"pre{k}_raw"] = _count(sp, rew, -w, 0) / (w / 1000)
        usual = odor + np.array([USUAL_REWARD_S.get(t, np.nan) for t in tt]) * 1000
        df["omit_raw"] = _count(sp, usual, 0, OMIT) / (OMIT / 1000)
        df["isi"] = [ISI_S.get(t, np.nan) for t in tt]
        df["isi_ms"] = rew - odor
        out.append(df)
    df = pd.concat(out, ignore_index=True)
    df = df[np.isfinite(df["type"])].copy()
    df["type"] = df["type"].astype(int)
    if window == "40min":
        df = df[df["minutes"] < 40].copy()
    elif window != "file":
        raise ValueError(window)
    df["base_mean"] = df.groupby("neuron")["base"].transform("mean")
    for c in ["post", "pre400", "pre200", "omit"]:
        df[c] = df[f"{c}_raw"] - df["base"]
    return df


def response(df, measure, baseline="trial"):
    """A response column under one baseline reading: trial, mean or none."""
    raw = df[f"{measure}_raw"]
    if baseline == "trial":
        return raw - df["base"]
    if baseline == "mean":
        return raw - df["base_mean"]
    if baseline == "none":
        return raw
    raise ValueError(baseline)


def isi_anova(df, measure, baseline="trial"):
    """Additive two-way ANOVA (ISI, neuron) on one mean per neuron and ISI.

    Rewarded odor A trials (types 1 to 9). The claims file fixes this design
    from the paper's degrees of freedom (opening comment). Returns F, df1, df2,
    p, the slope of the neuron-averaged response on ISI (spikes/s per s), the
    neuron count and the per-ISI means.
    """
    import statsmodels.formula.api as smf
    from statsmodels.stats.anova import anova_lm

    a = df[df["type"].between(1, 9)].assign(y=response(df, measure, baseline))
    cell = a.groupby(["neuron", "isi"], as_index=False)["y"].mean()
    fit = smf.ols("y ~ C(isi) + C(neuron)", cell).fit()
    tab = anova_lm(fit, typ=2)
    by_isi = cell.groupby("isi")["y"].mean()
    slope = stats.linregress(by_isi.index.values, by_isi.values).slope
    return dict(F=tab.loc["C(isi)", "F"], df1=int(tab.loc["C(isi)", "df"]),
                df2=int(tab.loc["Residual", "df"]), p=tab.loc["C(isi)", "PR(>F)"],
                slope=slope, n=cell["neuron"].nunique(), by_isi=by_isi)


def two_level_anova(cell, factor):
    """Additive two-way ANOVA (factor, neuron) on a long table with column y."""
    import statsmodels.formula.api as smf
    from statsmodels.stats.anova import anova_lm

    tab = anova_lm(smf.ols(f"y ~ C({factor}) + C(neuron)", cell).fit(), typ=2)
    return dict(F=tab.loc[f"C({factor})", "F"], df1=int(tab.loc[f"C({factor})", "df"]),
                df2=int(tab.loc["Residual", "df"]), p=tab.loc[f"C({factor})", "PR(>F)"])


def slopes(df, baseline="trial"):
    """Per neuron, least-squares line of post-reward response on ISI (s).

    Over the neuron's rewarded odor A trials (Results, Individual Neurons; Figure
    5 legend). A slope is significant when p < 0.05 for the slope coefficient
    (Figure 5 legend; the same as a 95% interval excluding 0).
    """
    a = df[df["type"].between(1, 9)].assign(y=response(df, "post", baseline))
    rows = []
    for (n, drug, task, sess), g in a.groupby(["neuron", "drug", "task", "session"]):
        r = stats.linregress(g["isi"].values, g["y"].values)
        rows.append(dict(neuron=n, drug=drug, task=task, session=sess,
                         slope=r.slope, p=r.pvalue, n_trials=len(g)))
    return pd.DataFrame(rows)


def auroc(x, y):
    """Area under the ROC curve for x against y (0.5 is chance)."""
    x, y = np.asarray(x), np.asarray(y)
    if len(x) == 0 or len(y) == 0:
        return np.nan
    u = stats.mannwhitneyu(x, y, alternative="two-sided").statistic
    return u / (len(x) * len(y))


def epoch_rates(neurons, df, types, t_end=6000, width=200):
    """Per neuron and trial type, baseline-subtracted rate in epochs after odor onset.

    200 ms epochs from odor onset to 6 s (Figure S5D). Returns a long table
    with neuron, drug, type, epoch start (ms) and the mean over the neuron's
    trials of that type.
    """
    edges = np.arange(0, t_end, width)
    rows = []
    sel = df[df["type"].isin(types)]
    for (n, drug, t), g in sel.groupby(["neuron", "drug", "type"]):
        sp = neurons[n]["spiketimes"]
        for e in edges:
            r = _count(sp, g["odor"].values, e, e + width) / (width / 1000) - g["base"].values
            rows.append(dict(neuron=n, drug=drug, type=t, epoch=e, y=r.mean(),
                             n_trials=len(g)))
    return pd.DataFrame(rows)
