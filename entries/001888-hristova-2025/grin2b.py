"""Loading and measures for dandiset 001888 (Hristova et al. 2025, Epilepsia, doi:10.1111/epi.18606).

The dandiset holds one NWB file per rat: the full 72 to 99 h wireless EEG (14 skull-surface
channels) and EMG (2 neck channels) at 250.4 Hz, an epochs table marking two consecutive 24-h
baseline windows (BL1, BL2), and per baseline window the lab's automated outputs: sleep scores in
5-s epochs, SWD (seizure) events, an SWD flag per 5-s epoch, per-hour seizure totals and per-state
spectra.

Where parameters come from:
- 5-s epochs, 24-h windows from Zeitgeber time 0 (07:00, lights on), values averaged over the two
  days, SWD state taken from the epoch before the SWD, wake-NREM transitions judged on the six
  epochs before it: the paper's Supplementary Methods.
- SWD epochs: the Methods exclude "SWD times" from the sleep states; here the epochs an SWD event
  overlaps (scored_states mode "events", the main choice). The lab's sleep scorer
  (AUTOMATIC-SLEEP-SCORER, commit 95b25fb, function correct.C) instead sets an epoch to SWD
  (code 4) where its per-epoch SWD file holds 6; the dandiset stores that file as
  `swd_epoch_counts` (mode "flag", a variant).
- Spectra: the Supplementary Methods (third-order 0.2 to 100 Hz Butterworth band-pass, 5-s
  epochs dropped when any sample exceeds 3000 (stated as mV; taken here as microvolts, as the
  amplifier's full range is 13 mV), Welch with a Hann window and 50% overlap, each epoch
  normalized to the animal's average spectrum over REM, NREM and wake). The Welch segment length
  (2 s) and the spectral-slope rejection, which the paper does not specify fully, are common
  choices made here; the slope rejection is not applied.
- Frequency bands: not defined in the paper. Common choices: delta 1-4, theta 4-8, sigma 10-15,
  beta 15-30, gamma 30-48 Hz (BANDS); a contiguous variant is in BANDS_ALT.
- Bouts: a run of consecutive epochs of one state; SWD epochs are a state of their own and so
  end a bout. The paper does not define a bout; this is a common choice.
"""

from __future__ import annotations

import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import signal, stats

DANDISET_ID = "001888"
DANDISET_VERSION = "draft"  # the dandiset has no published version
DRAFT_MODIFIED = "2026-07-31T09:37:44.644146Z"  # the draft read for this entry
N_ASSETS = 17


FS = 250.4                      # Hz, Methods
EPOCH_S = 5.0                   # s, Methods
EPOCHS_PER_DAY = 17280
STATES = {0: "Wake", 1: "NREM", 2: "REM", 4: "SWD"}
SWD_FLAG = 6                    # value of the per-epoch SWD file that marks an SWD epoch (scorer code)
DROPOUT = 32767                 # raw value written on all channels at once during signal loss
ADC_MAX = 4095                  # 12-bit amplifier: valid codes are 0 to 4095
ARTEFACT_UV = 3000.0            # Supplementary Methods
WELCH_SEG_S = 2.0               # common choice
BANDS = {"delta": (1, 4), "theta": (4, 8), "sigma": (10, 15), "beta": (15, 30), "gamma": (30, 48)}
BANDS_ALT = {"delta": (0.5, 4), "theta": (4, 8), "sigma": (8, 15), "beta": (15, 30), "gamma": (30, 100)}
SWD_CHANNEL = "S1_Tr_R"         # AP -3.0, ML 2.8 right: the SWD detection channel of the Methods
RAW_ZT_HOURS = (0, 4, 8, 12, 16, 20)  # one storage chunk (about 24 min) read at each of these ZT hours


# --- archive ------------------------------------------------------------------

def check_version() -> dict:
    """The draft's state; raises if it changed since this entry was written."""
    with urllib.request.urlopen(f"https://api.dandiarchive.org/api/dandisets/{DANDISET_ID}/versions/"
                                f"{DANDISET_VERSION}/info/") as r:
        info = json.load(r)
    if info["modified"] != DRAFT_MODIFIED or info["asset_count"] != N_ASSETS:
        raise RuntimeError(f"draft of {DANDISET_ID} changed: modified {info['modified']}, "
                           f"{info['asset_count']} assets (expected {DRAFT_MODIFIED}, {N_ASSETS})")
    return info


def assets():
    ds = DandiAPIClient().get_dandiset(DANDISET_ID, DANDISET_VERSION)
    return sorted(ds.get_assets(), key=lambda a: a.path)


def _open(url):
    return h5py.File(remfile.File(url), "r")


def _str(x):
    v = x[()]
    return v.decode() if isinstance(v, bytes) else v


def _table(g) -> pd.DataFrame:
    cols = {}
    for k in g.attrs["colnames"]:
        v = g[k][:]
        if v.dtype == object:
            v = np.array([s.decode() if isinstance(s, bytes) else s for s in v], dtype=object)
        cols[k] = v
    return pd.DataFrame(cols)


def load_session(asset) -> dict:
    """Metadata and the processed tables of one file (not the raw signals)."""
    url = asset.get_content_url(follow_redirects=1, strip_query=True)
    f = _open(url)
    subj = {k: _str(f["general/subject"][k]) for k in f["general/subject"]}
    eeg, emg = f["acquisition/EEGElectricalSeries"], f["acquisition/EMGElectricalSeries"]
    elec = f["general/extracellular_ephys/electrodes"]
    channel_names = [s.decode() if isinstance(s, bytes) else s for s in elec["channel_name"][:]]
    beh, ece = f["processing/behavior"], f["processing/ecephys"]
    s = {
        "path": asset.path, "url": url,
        "subject_id": subj["subject_id"], "sex": subj.get("sex"), "age": subj.get("age"),
        "species": subj.get("species"), "strain": subj.get("strain"),
        "subject_fields": sorted(subj),
        "session_start_time": _str(f["session_start_time"]),
        "eeg_shape": eeg["data"].shape, "emg_shape": emg["data"].shape,
        "eeg_chunks": eeg["data"].chunks, "rate": float(eeg["starting_time"].attrs["rate"]),
        "starting_time": float(eeg["starting_time"][()]),
        "conversion": float(eeg["data"].attrs["conversion"]), "offset": float(eeg["data"].attrs["offset"]),
        "unit": eeg["data"].attrs["unit"],
        "eeg_channels": [channel_names[i] for i in eeg["electrodes"][:]],
        "emg_channels": [channel_names[i] for i in emg["electrodes"][:]],
        "epochs": _table(f["intervals/epochs"]).drop(columns=["tags_index"], errors="ignore"),
        "sleep_states": _table(beh["sleep_states"]),
        "swd_flags": _table(beh["swd_epoch_counts"]),
        "seizure_totals_by_zt": _table(beh["seizure_totals_by_zt"]),
        "seizures": (_table(beh["seizure_events"]) if "seizure_events" in beh
                     else pd.DataFrame(columns=["start_time", "stop_time", "duration", "baseline_window"])),
        "spectra": _table(ece["sleep_state_power_spectra"]),
        "descriptions": {k: beh[k].attrs.get("description", "") for k in beh} |
                        {k: ece[k].attrs.get("description", "") for k in ece},
    }
    g = subj.get("genotype")
    s["genotype"] = {"het": "Het", "wt": "WT"}[g.lower()] if g else None
    s["genotype_stored"] = g
    s["animal"] = int(s["subject_id"].split("-")[1])
    s["epochs"]["tags"] = [t.decode() if isinstance(t, bytes) else t
                           for t in f["intervals/epochs/tags"][:]]
    s["days"] = _days(s)
    return s


def load_all(max_workers: int = 6) -> list[dict]:
    with ThreadPoolExecutor(max_workers) as ex:
        return list(ex.map(load_session, assets()))


# --- one baseline day ---------------------------------------------------------

def _days(s) -> list[dict]:
    """Per baseline window: the epoch grid, scores, SWD flags and SWD events, times from its start."""
    out = []
    for _, ep in s["epochs"].iterrows():
        bl = ep["tags"]
        st = s["sleep_states"][s["sleep_states"].baseline_window == bl].sort_values("start_time")
        fl = s["swd_flags"][s["swd_flags"].baseline_window == bl].sort_values("start_time")
        sz = s["seizures"][s["seizures"].baseline_window == bl].sort_values("start_time")
        t0 = float(ep["start_time"])
        out.append({
            "bl": bl, "t0": t0, "t1": float(ep["stop_time"]),
            "epoch_start": st.start_time.to_numpy() - t0,
            "states": st.sleep_score.to_numpy().astype(int),
            "flags": fl.swd_count.to_numpy().astype(int),
            "flag_start": fl.start_time.to_numpy() - t0,
            "sz_start": sz.start_time.to_numpy(float) - t0, "sz_stop": sz.stop_time.to_numpy(float) - t0,
            "sz_dur": sz.duration.to_numpy(float),
        })
    return out


def scored_states(day, mode: str = "events") -> np.ndarray:
    """Sleep scores with SWD epochs as state 4.

    mode "events": where an SWD event overlaps the epoch (Methods; main).
    mode "flag": where the per-epoch SWD file holds 6 (the scorer code).
    mode "stored": the stored scores, which hold no SWD state.
    """
    s = day["states"].copy()
    if mode == "flag":
        s[day["flags"] == SWD_FLAG] = 4
    elif mode == "events":
        s[event_epochs(day)] = 4
    elif mode != "stored":
        raise ValueError(mode)
    return s


def event_epochs(day) -> np.ndarray:
    """Boolean per epoch: an SWD event overlaps it."""
    m = np.zeros(len(day["states"]), bool)
    for a, b in zip(day["sz_start"], day["sz_stop"]):
        m[int(a // EPOCH_S): int(np.ceil(b / EPOCH_S))] = True
    return m


def runs(states: np.ndarray):
    """(state, length in epochs) of each run of consecutive equal states."""
    change = np.flatnonzero(np.diff(states)) + 1
    starts = np.r_[0, change]
    lengths = np.diff(np.r_[starts, len(states)])
    return states[starts], lengths


def state_measures(states: np.ndarray) -> dict:
    """Minutes, number of bouts and mean bout duration (s) of wake, NREM and REM in one day."""
    codes, lengths = runs(states)
    out = {}
    for c, name in ((0, "wake"), (1, "nrem"), (2, "rem")):
        L = lengths[codes == c]
        out[f"{name}_min"] = (states == c).sum() * EPOCH_S / 60
        out[f"{name}_bouts"] = len(L)
        out[f"{name}_bout_s"] = L.mean() * EPOCH_S if len(L) else np.nan
    return out


def hourly_minutes(states: np.ndarray, code: int) -> np.ndarray:
    return (states.reshape(24, -1) == code).sum(1) * EPOCH_S / 60


def swd_measures(day) -> dict:
    n = len(day["sz_start"])
    hours = np.floor(day["sz_start"] / 3600).astype(int)
    return {"swd_n": n, "swd_mean_s": day["sz_dur"].mean() if n else np.nan,
            "swd_total_min": day["sz_dur"].sum() / 60,
            "swd_light": int((hours < 12).sum()), "swd_dark": int((hours >= 12).sum()),
            "swd_hourly": np.bincount(hours, minlength=24)[:24]}


def swd_onsets(day, nrem_rule: str = "prev") -> pd.DataFrame:
    """State before each SWD, from the stored scores.

    The state is that of the 5-s epoch before the epoch holding the SWD start. With nrem_rule "any6"
    an SWD is called NREM when any of the six epochs before it is NREM. `transition` is True when
    the six epochs before the SWD hold a change from wake to NREM.
    """
    st = day["states"]
    k = (day["sz_start"] // EPOCH_S).astype(int)
    rows = []
    for i in k:
        prev = st[i - 1] if i >= 1 else st[0]
        six = st[max(i - 6, 0):i]
        trans = bool(np.any((six[:-1] == 0) & (six[1:] == 1))) if len(six) > 1 else False
        state = prev
        if nrem_rule == "any6" and np.any(six == 1):
            state = 1
        rows.append({"state": int(state), "transition": trans})
    return pd.DataFrame(rows, columns=["state", "transition"])


# --- raw signals --------------------------------------------------------------

def raw_windows(s, zt_hours=RAW_ZT_HOURS) -> list[dict]:
    """For each baseline day, the storage chunk of raw EEG and EMG holding each ZT hour in zt_hours.

    Returns the SWD-detection EEG channel and both EMG channels as raw integer codes, with the
    time (s from the start of the day) of the first sample.
    """
    f = _open(s["url"])
    eeg, emg = f["acquisition/EEGElectricalSeries/data"], f["acquisition/EMGElectricalSeries/data"]
    chunk = eeg.chunks[0]
    ch = s["eeg_channels"].index(SWD_CHANNEL)
    out = []
    for day in s["days"]:
        for zt in zt_hours:
            i0 = int(round((day["t0"] + zt * 3600) * FS)) // chunk * chunk
            i1 = min(i0 + chunk, eeg.shape[0])
            out.append({"bl": day["bl"], "zt": zt, "t_start": i0 / FS - day["t0"],
                        "eeg": eeg[i0:i1, :][:, ch], "emg": emg[i0:i1, :]})
    return out


def _volts_uv(codes, s):
    """Microvolts with the DC level removed (the files store unsigned codes with offset 0).

    Samples that are not valid 12-bit codes (signal loss, 32767; negative or above 4095) are bad.
    """
    x = codes.astype(float)
    bad = (codes < 0) | (codes > ADC_MAX)
    x[bad] = np.nan
    x = (x - np.nanmedian(x)) * s["conversion"] * 1e6
    return x, bad


def window_epochs(win, s, day) -> pd.DataFrame:
    """Per whole 5-s epoch of the day's grid inside a raw window: EEG Welch PSD (Methods filter and
    artefact rule), EMG 60-90 Hz log power (right minus left), and whether the epoch is usable."""
    eeg, bad = _volts_uv(win["eeg"], s)
    emg_r, bad_r = _volts_uv(win["emg"][:, 0], s)
    emg_l, bad_l = _volts_uv(win["emg"][:, 1], s)
    bad = bad | bad_r | bad_l
    sos = signal.butter(3, [0.2, 100], btype="bandpass", fs=FS, output="sos")
    filled = np.where(bad, 0.0, eeg)
    filt = signal.sosfiltfilt(sos, filled)
    emg = np.where(bad, 0.0, emg_r - emg_l)
    n = len(filt)
    first = int(np.ceil(win["t_start"] / EPOCH_S))
    rows, psds = [], []
    nseg = int(WELCH_SEG_S * FS)
    pad = int(FS)  # one second around an epoch must be free of dropouts (filter edges)
    k = first
    while True:
        a = int(round((k * EPOCH_S - win["t_start"]) * FS))
        b = a + int(round(EPOCH_S * FS))
        if b > n:
            break
        if k >= len(day["states"]):
            break
        seg = filt[a:b]
        dropout = bad[max(a - pad, 0):min(b + pad, n)].any()
        artefact = np.abs(seg).max() > ARTEFACT_UV
        freq, p = signal.welch(seg, fs=FS, window="hann", nperseg=nseg, noverlap=nseg // 2)
        fe, pe = signal.welch(emg[a:b], fs=FS, window="hann", nperseg=nseg, noverlap=nseg // 2)
        emg_pow = np.log10(pe[(fe >= 60) & (fe <= 90)].mean() + 1e-12)
        rows.append({"epoch": k, "dropout": bool(dropout), "artefact": bool(artefact),
                     "emg_logpow": emg_pow})
        psds.append(p)
        k += 1
    df = pd.DataFrame(rows)
    df["psd"] = list(psds)
    return df


def welch_freq() -> np.ndarray:
    """Frequencies of the PSDs returned by window_epochs."""
    return np.fft.rfftfreq(int(WELCH_SEG_S * FS), 1 / FS)


def swd_band_series(win, s, bin_s: float = 0.5):
    """EEG 5-10 Hz power (log) in bins of bin_s seconds, and bin centre times from the day's start."""
    eeg, bad = _volts_uv(win["eeg"], s)
    sos = signal.butter(3, [5, 10], btype="bandpass", fs=FS, output="sos")
    y = signal.sosfiltfilt(sos, np.where(bad, 0.0, eeg)) ** 2
    m = int(round(bin_s * FS))
    nb = len(y) // m
    p = np.log10(y[:nb * m].reshape(nb, m).mean(1) + 1e-6)
    okb = ~bad[:nb * m].reshape(nb, m).any(1)
    t = win["t_start"] + (np.arange(nb) + 0.5) * m / FS
    return t, p, okb


def in_events(t, starts, stops, shift: float = 0.0) -> np.ndarray:
    """Boolean per time: inside an event once the events are shifted by `shift` seconds."""
    a, b = starts + shift, stops + shift
    i = np.searchsorted(a, t, side="right") - 1
    ok = i >= 0
    out = np.zeros(len(t), bool)
    out[ok] = t[ok] < b[i[ok]]
    return out


def band_power(freq, psd, bands=BANDS) -> dict:
    return {b: psd[(freq >= lo) & (freq < hi)].mean() for b, (lo, hi) in bands.items()}


# --- statistics ---------------------------------------------------------------

def split_plot_anova(df: pd.DataFrame, value: str, subject: str, between: str, within: str) -> pd.DataFrame:
    """F tests of a random-intercept model with one between-subject and one within-subject factor.

    For complete data this is the classical split-plot ANOVA, which a linear mixed model with a
    random intercept per animal (the paper's lmerTest) reproduces: the between factor is tested
    against the subject error, the within factor and the interaction against the residual.
    """
    d = df[[value, subject, between, within]].copy()
    grand = d[value].mean()
    a_lv, b_lv = sorted(d[between].unique()), sorted(d[within].unique())
    nb = len(b_lv)
    subj = d.groupby(subject).agg(m=(value, "mean"), g=(between, "first"))
    N = len(subj)
    gmean = d.groupby(between)[value].mean()
    n_g = subj.groupby("g").size()
    ss_a = sum(n_g[g] * nb * (gmean[g] - grand) ** 2 for g in a_lv)
    ss_s = nb * sum((subj.m - gmean[subj.g].to_numpy()) ** 2)
    cell = d.groupby([between, within])[value].mean()
    wmean = d.groupby(within)[value].mean()
    ss_b = N * sum((wmean - grand) ** 2)
    ss_ab = sum(n_g[g] * (cell[(g, w)] - gmean[g] - wmean[w] + grand) ** 2 for g in a_lv for w in b_lv)
    ss_t = ((d[value] - grand) ** 2).sum()
    ss_r = ss_t - ss_a - ss_s - ss_b - ss_ab
    df_a, df_s, df_b = len(a_lv) - 1, N - len(a_lv), nb - 1
    df_ab, df_r = df_a * df_b, (N - len(a_lv)) * (nb - 1)
    rows = []
    for name, ss, dfn, err, dfd in ((between, ss_a, df_a, ss_s, df_s), (within, ss_b, df_b, ss_r, df_r),
                                    (f"{between} x {within}", ss_ab, df_ab, ss_r, df_r)):
        F = (ss / dfn) / (err / dfd)
        rows.append({"effect": name, "F": F, "df": dfn, "df_error": dfd, "p": stats.f.sf(F, dfn, dfd)})
    return pd.DataFrame(rows)


def two_group(x_wt, x_het, test: str) -> dict:
    """The paper's two-group tests (WT first, as in its reported statistics)."""
    x_wt, x_het = np.asarray(x_wt, float), np.asarray(x_het, float)
    if test == "t":
        r = stats.ttest_ind(x_wt, x_het)
        return {"test": "t", "stat": r.statistic, "df": len(x_wt) + len(x_het) - 2, "p": r.pvalue}
    if test == "welch":
        r = stats.ttest_ind(x_wt, x_het, equal_var=False)
        return {"test": "Welch t", "stat": r.statistic, "df": r.df, "p": r.pvalue}
    if test == "wilcoxon":
        r = stats.mannwhitneyu(x_wt, x_het, alternative="two-sided")
        return {"test": "Wilcoxon rank-sum (W)", "stat": r.statistic, "df": np.nan, "p": r.pvalue}
    raise ValueError(test)
