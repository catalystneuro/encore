"""Loading and spiking measures for dandiset 000637 (S1 spike times under tFUS).

Gao, Ramachandran, Yu & He (2025), J Neurosci 45(23):e2218242025, doi:10.1523/jneurosci.2218-24.2025.

Each NWB file holds one recording from one rat: a Units table with spike times only (no waveforms, no
electrode per unit, electrode locations "unknown"), and a trials table with start and stop times only.
The stimulation condition is coded in the file's identifier, `<subject>_<PRF Hz>_<PD us>_<UD ms>_<V>`
(for example BH401_1500_400_67_5V: PRF 1500 Hz, pulse duration 400 us, ultrasound duration 67 ms, 5 V),
with a trailing `_2`, `_3` on repeated recordings, and `<subject>_BASELINE` for recordings without a
condition. The dandiset's description says so for its sister dandiset 000946 ("in BH494_1500_200_67_5,
the PRF is 1500Hz and PD is 200us"); for 000637 it is read from the values, and the last field is read
as the input voltage (the paper's Methods use "5 V input voltage"). Files are streamed from the archive
at the pinned version; nothing is written to disk.

Where the parameters come from:

- Units with more than 2,000 spikes in the session (`MIN_SPIKES`): Methods, "Neuronal type
  classification and neuronal response quantification" ("Only neurons that fire >2,000 spikes for
  each session were considered").
- Windows of 67 ms aligned to the trial start, taken as the tFUS onset (`WINDOWS`): the claims file,
  Method S, from the Methods ("normalized to 67 ms before each stimulation") and the Results' windows.
  That the trial start is the onset is checked in the notebook (a response contrast), not given by
  the files.
- Normalized rate, readings N1 (sum over trials of window counts over sum of pre-stimulus counts) and
  N2 (mean over trials of the per-trial ratio, trials without a pre-stimulus spike left out): the
  claims file, Method S.
- The time shift of the clock check (`SHIFT_S`, 1.2 s, about half the 2.5 s intersonication
  interval) is a standard choice that cannot change a claim's outcome.
"""

from __future__ import annotations

import re
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient

DANDISET_ID = "000637"
DANDISET_VERSION = "0.250829.1249"

MIN_SPIKES = 2000
WIN_MS = 67.0
WINDOWS = {"pre": (-67.0, 0.0), "0-67": (0.0, 67.0), "67-134": (67.0, 134.0),
           "134-201": (134.0, 201.0), "201-268": (201.0, 268.0)}
SHIFT_S = 1.2

_IDENT = re.compile(r"^(BH\d+)_(\d+)_(\d+)_(\d+)_(\d+)V?(?:_(\d+))?$")


def parse_identifier(ident: str) -> dict:
    """Condition fields coded in a file's identifier."""
    if ident.endswith("_BASELINE"):
        return dict(subject=ident.split("_")[0], prf=np.nan, pd_us=np.nan, ud_ms=np.nan,
                    volt=np.nan, volt_field=None, repeat=1, baseline=True)
    m = _IDENT.match(ident)
    if m is None:
        raise ValueError(f"unparsed identifier {ident!r}")
    subj, prf, pd_us, ud, volt, rep = m.groups()
    # "55" and "35" are 5.5 V and 3.5 V; "5" and "7" are whole volts.
    v = float(volt) / 10 if len(volt) == 2 else float(volt)
    return dict(subject=subj, prf=int(prf), pd_us=int(pd_us), ud_ms=int(ud), volt=v, volt_field=volt,
                repeat=int(rep) if rep else 1, baseline=False)


def asset_urls() -> list[tuple[str, str]]:
    """(path, streaming URL) of every NWB file at the pinned version."""
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))
                      for a in ds.get_assets() if a.path.endswith(".nwb"))


def _str(x) -> str:
    x = x[()] if hasattr(x, "shape") else x
    return x.decode() if isinstance(x, bytes) else str(x)


def _tree(f) -> list[str]:
    """Every group and dataset path in the file."""
    out = []
    f.visit(out.append)
    return sorted(out)


def _texts(g) -> dict:
    """The scalar text datasets directly under group `g` (for example experiment_description, notes)."""
    out = {}
    for k, v in g.items():
        if isinstance(v, h5py.Dataset) and v.shape == () and v.dtype.kind in "OSU":
            out[k] = _str(v)
    return out


def load_session(path: str, url: str) -> dict:
    """One recording: metadata, trial starts and stops, and spike times per unit (seconds)."""
    with h5py.File(remfile.File(url), "r") as f:
        ident = _str(f["identifier"])
        st = f["units/spike_times"][:]
        idx = f["units/spike_times_index"][:]
        starts = f["intervals/trials/start_time"][:]
        stops = f["intervals/trials/stop_time"][:]
        loc = sorted({_str(x) for x in f["general/extracellular_ephys/electrodes/location"][:]})
        meta = dict(path=path, identifier=ident,
                    subject_id=_str(f["general/subject/subject_id"]),
                    description=_str(f["session_description"]),
                    start_time=_str(f["session_start_time"]),
                    unit_columns=list(f["units"].attrs["colnames"]),
                    trial_columns=list(f["intervals/trials"].attrs["colnames"]),
                    electrode_locations=loc,
                    n_electrodes=len(f["general/extracellular_ephys/electrodes/id"]),
                    device=[_str(f["general/devices"][k].attrs.get("description", ""))
                            for k in f["general/devices"]],
                    acquisition=list(f["acquisition"]), processing=list(f["processing"]),
                    h5_paths=_tree(f), general_text=_texts(f["general"]),
                    subject_text=_texts(f["general/subject"]),
                    units_description=_str(f["units"].attrs.get("description", "")),
                    electrode_z=sorted(set(f["general/extracellular_ephys/electrodes/z"][:].tolist())),
                    electrode_columns=list(f["general/extracellular_ephys/electrodes"].attrs["colnames"]),
                    electrode_groups={k: {a: _str(g.attrs[a]) for a in ("location", "description") if a in g.attrs}
                                      for k, g in f["general/extracellular_ephys"].items()
                                      if isinstance(g, h5py.Group) and k != "electrodes"})
    units = np.split(st, idx[:-1].astype(int))
    meta.update(parse_identifier(ident))
    meta.update(trial_start=starts, trial_stop=stops, units=units)
    return meta


def load_all(workers: int = 16) -> list[dict]:
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(lambda pu: load_session(*pu), asset_urls()))


def window_counts(spikes: np.ndarray, onsets: np.ndarray) -> np.ndarray:
    """Spike counts per trial (rows) in each window of `WINDOWS` (columns), windows in ms from onset."""
    out = np.empty((len(onsets), len(WINDOWS)), dtype=np.int64)
    for j, (a, b) in enumerate(WINDOWS.values()):
        lo = np.searchsorted(spikes, onsets + a / 1000.0, side="left")
        hi = np.searchsorted(spikes, onsets + b / 1000.0, side="left")
        out[:, j] = hi - lo
    return out


def unit_table(sessions: list[dict], shift_s: float = 0.0) -> pd.DataFrame:
    """One row per unit with more than `MIN_SPIKES` spikes: session fields, and for each window the
    summed count, the normalized rate N1 and N2 (percent of the pre-stimulus window), and the rate in
    Hz. With `shift_s`, the onsets are moved by that many seconds (the clock check)."""
    rows = []
    names = list(WINDOWS)
    for s in sessions:
        onsets = s["trial_start"] + shift_s
        for u, sp in enumerate(s["units"]):
            if len(sp) <= MIN_SPIKES:
                continue
            c = window_counts(sp, onsets)
            row = dict(identifier=s["identifier"], subject=s["subject"], prf=s["prf"], pd_us=s["pd_us"],
                       volt=s["volt"], baseline=s["baseline"], unit=u, n_spikes=len(sp), n_trials=len(onsets))
            pre = c[:, 0]
            for j, w in enumerate(names):
                row[f"count_{w}"] = int(c[:, j].sum())
                row[f"rate_{w}"] = c[:, j].sum() / (len(onsets) * WIN_MS / 1000.0)
                if j == 0:
                    continue
                row[f"n1_{w}"] = 100.0 * c[:, j].sum() / pre.sum() if pre.sum() > 0 else np.nan
                ok = pre > 0
                row[f"n2_{w}"] = 100.0 * np.mean(c[ok, j] / pre[ok]) if ok.any() else np.nan
            rows.append(row)
    return pd.DataFrame(rows)


def population_psth(sessions: list[dict], edges_s: np.ndarray) -> np.ndarray:
    """Per unit with more than `MIN_SPIKES` spikes (rows), the spike rate in Hz in each bin of
    `edges_s` (seconds from trial start), averaged over trials."""
    rows = []
    for s in sessions:
        on = s["trial_start"]
        for sp in s["units"]:
            if len(sp) <= MIN_SPIKES:
                continue
            idx = np.searchsorted(sp, on[:, None] + edges_s[None, :], side="left")
            rows.append(np.diff(idx, axis=1).sum(0) / (len(on) * np.diff(edges_s)))
    return np.array(rows)


def duty_cycle(prf, pd_us):
    """Duty cycle in percent: PRF times pulse duration (Figure 1B legend, "PDs were calculated by
    PRFs*DCs")."""
    return np.asarray(prf, dtype=float) * np.asarray(pd_us, dtype=float) * 1e-4
