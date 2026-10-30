"""Loading and measures for Gao, Ramachandran, Yu and He (2025), J Neurosci 45(23) e2218242025.

The target is dandiset 000463. It holds broadband recordings of an S1 probe with no units, no trial
times and no brain locations, from four rats that are not in the paper's own deposit. The paper says
its data are in dandiset 000946 (Methods, "Data acquisition and preprocessing": "All experimental
data has been made public in a repository at the DANDI Archive
(https://dandiarchive.org/dandiset/000946)"), so the claims are tested there (`data: elsewhere`).
Both are streamed from the DANDI Archive at pinned versions; nothing is downloaded to disk.

Where each parameter comes from:

- Windows of 67 ms: the claims file (M3) and the Methods ("The normalized spiking rate which was
  normalized to 67 ms before each stimulation"). During sonication 0 to 67 ms, postsonication 201
  to 268 ms (claims file, M3, from the Figures 5 to 9 and 11 legends).
- Unit selection, more than 2000 spikes in the session: claims file M1, Methods ("Only neurons that
  fire >2,000 spikes for each session were considered").
- Normalization readings O2a and O2b, baseline readings O3a to O3c, Bonferroni readings O4a and
  O4b, alpha 0.01, Kruskal-Wallis then one-tailed two-sample Wilcoxon (rank-sum) tests: the claims
  file (M4, O2 to O4), from the Methods, "Statistical analysis".
- Sonication onset is the trial `start_time`: the files say "intervals contains each tFUS trial
  start and end timestamps" (general/stimulus); the notebook checks it against the spikes.
- PRF and PD of a recording are read from its identifier, as the dandiset's description says ("in
  BH494_1500_200_67_5, the PRF is 1500Hz and PD is 200us"). Recording area and stimulation target
  are read from `general/notes` ("Recording:S1; stim at:S1").
- Parallel reads (processes) and retries change no result; they are standard choices.
"""

from __future__ import annotations

import hashlib
import re
import time
from concurrent.futures import ProcessPoolExecutor
from functools import partial

import h5py
import numpy as np
import remfile
import requests
from scipy import stats

API = "https://api.dandiarchive.org/api"
DANDISET = "000463"
VERSION = "0.250829.1248"
PAPER_DANDISET = "000946"
PAPER_VERSION = "0.250829.1249"

WIN_PRE = (-0.067, 0.0)
WIN_PRE2 = (-0.134, -0.067)  # O3b baseline sample
WIN_DURING = (0.0, 0.067)
WIN_POST = (0.201, 0.268)
MIN_SPIKES = 2000  # M1
ALPHA = 0.01  # M4


def versions(dandiset):
    r = requests.get(f"{API}/dandisets/{dandiset}/versions/", timeout=60).json()
    return [v["version"] for v in r["results"]]


def assets(dandiset, version):
    url = f"{API}/dandisets/{dandiset}/versions/{version}/assets/?page_size=1000"
    out = []
    while url:
        d = requests.get(url, timeout=60).json()
        out += [dict(path=a["path"], size=a["size"], asset_id=a["asset_id"]) for a in d["results"]]
        url = d["next"]
    return sorted(out, key=lambda a: a["path"])


def metadata(dandiset, version):
    return requests.get(f"{API}/dandisets/{dandiset}/versions/{version}/", timeout=60).json()


def s3_url(asset_id):
    return requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60).url


def _str(x):
    x = x[0] if hasattr(x, "shape") and x.shape else x
    return x.decode() if isinstance(x, bytes) else str(x)


def _retry(fn, a, tries=4):
    for k in range(tries):
        try:
            return fn(a)
        except Exception as e:  # network errors; retried, then reported
            err = e
            time.sleep(2 + 2 * k)
    return dict(path=a["path"], error=repr(err))


def pmap(fn, items, workers=8):
    """Map over files in separate processes (h5py serializes reads within one process)."""
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(partial(_retry, fn), items, chunksize=4))


# ---------------------------------------------------------------- dandiset 000463 (the target)

def describe_000463_file(a):
    """Everything an analysis of the claims would need, read from one file's metadata."""
    f = h5py.File(remfile.File(s3_url(a["asset_id"])), "r")
    es = f["acquisition/ElectricalSeries"]
    el = f["general/extracellular_ephys/electrodes"]
    return dict(
        path=a["path"], identifier=_str(f["identifier"][()]),
        subject=_str(f["general/subject/subject_id"][()]),
        session_start=_str(f["session_start_time"][()])[:19],
        acquisition=",".join(f["acquisition"].keys()),
        samples=es["data"].shape[0], channels=es["data"].shape[1],
        rate_hz=float(es["starting_time"].attrs["rate"]), unit=es["data"].attrs["unit"],
        duration_s=es["data"].shape[0] / float(es["starting_time"].attrs["rate"]),
        lfp_rate_hz=float(f["processing/ecephys/LFP/ElectricalSeries/starting_time"].attrs["rate"]),
        intervals=",".join(f["intervals"].keys()) or "none",
        units="units" in f, stimulus=",".join(f["stimulus/presentation"].keys()) or "none",
        electrode_location=",".join(sorted({_str(x) for x in el["location"][:]})),
        group_location=_str(f["general/extracellular_ephys/shank1"].attrs["location"]),
        device=_str(f["general/devices/array"].attrs["description"]),
    )


# ---------------------------------------------------------------- dandiset 000946 (the paper's)

ID_RE = re.compile(r"BH(\d+)_(\d+)_([\dpoint]+)_(\d+)_(\d+)(.*)$")


def parse_identifier(identifier):
    """PRF (Hz), PD (us), UD (ms), voltage and suffix from an identifier such as BH494_1500_200_67_5."""
    m = ID_RE.match(identifier)
    if not m:
        return None
    sub, prf, pd, ud, volt, suffix = m.groups()
    return dict(subject="BH" + sub, prf=int(prf), pd_us=float(pd.replace("point", ".")), ud_ms=int(ud),
                volt=volt, suffix=suffix.strip())


def parse_notes(notes):
    n = notes.lower().replace(" ", "")
    m = re.match(r"recording:([^;]*);(?:stimat|stimulation):(.*)", n)
    return (m.group(1), m.group(2)) if m else ("?", "?")


def describe_000946_file(a):
    """Metadata of one file of 000946, with a signature of its content to find duplicate deposits."""
    f = h5py.File(remfile.File(s3_url(a["asset_id"])), "r")
    r = dict(path=a["path"], asset_id=a["asset_id"], size=a["size"],
             identifier=_str(f["identifier"][()]), notes=_str(f["general/notes"][()]),
             description=_str(f["session_description"][()]),
             session_start=_str(f["session_start_time"][()])[:19])
    r["data_collection"] = _str(f["general/data_collection"][()]) if "general/data_collection" in f else ""
    r["unit_columns"] = ",".join(f["units"].attrs["colnames"]) if "units" in f else ""
    tr = f["intervals/trials"]
    st, sp = tr["start_time"][:], tr["stop_time"][:]
    r.update(n_trials=len(st), trial_len_s=float(np.median(sp - st)),
             isi_min=float(np.diff(st).min()), isi_max=float(np.diff(st).max()))
    h = hashlib.md5(st.tobytes())
    if "spike_times_index" in f["units"]:
        idx = f["units/spike_times_index"][:]
        r["spike_counts"] = np.diff(np.r_[0, idx]).astype(int)
        lab = f["units/celltype_label"][:] if "celltype_label" in f["units"] else None
        r["labels"] = lab
        r["label_description"] = (_str(f["units/celltype_label"].attrs["description"])
                                  if lab is not None else "")
        h.update(idx.tobytes())
        n = len(f["units/spike_times"])
        h.update(f["units/spike_times"][: min(n, 1000)].tobytes())
        h.update(f["units/spike_times"][max(0, n - 1000):].tobytes())
    else:
        r["spike_counts"] = None
        r["labels"] = None
        r["label_description"] = ""
        r["sttc_shape"] = f["units/STTC"].shape if "STTC" in f["units"] else None
        h.update(str(r["sttc_shape"]).encode())
    r["signature"] = h.hexdigest()
    rec, target = parse_notes(r["notes"])
    r["area"], r["target"] = rec, target
    p = parse_identifier(r["identifier"]) or {}
    r.update(p)
    return r


def describe_sttc_file(a):
    """Identifier, notes, units-table description and every units dataset of one STTC file of 000946."""
    f = h5py.File(remfile.File(s3_url(a["asset_id"])), "r")
    u = f["units"]
    return dict(path=a["path"], identifier=_str(f["identifier"][()]), notes=_str(f["general/notes"][()]),
                units_description=_str(u.attrs["description"]),
                datasets={k: (u[k].shape, _str(u[k].attrs.get("description", ""))) for k in u.keys()})


def load_spikes(a):
    """Spike times of every unit and the trial onsets of one file of 000946."""
    f = h5py.File(remfile.File(s3_url(a["asset_id"])), "r")
    idx = f["units/spike_times_index"][:]
    sp = f["units/spike_times"][:]
    units = np.split(sp, idx[:-1])
    return dict(path=a["path"], onsets=f["intervals/trials/start_time"][:], units=units,
                digest=hashlib.md5(sp.tobytes()).hexdigest())


# ---------------------------------------------------------------- measures

def window_counts(spikes, onsets, win):
    """Spike counts of one unit in [onset + win[0], onset + win[1]) for each trial."""
    lo = np.searchsorted(spikes, onsets + win[0])
    hi = np.searchsorted(spikes, onsets + win[1])
    return hi - lo


def normalized_rate(spikes, onsets, win, reading):
    """Normalized spiking rate in percent (claims file M3), under reading O2a or O2b.

    O2a: mean count in the window over trials / mean count in the 67 ms before onset over trials.
    O2b: mean over trials of the per-trial ratio, trials with no prestimulation spike left out.
    Returns nan when the unit has no prestimulation spike (O2a) or no usable trial (O2b).
    """
    c = window_counts(spikes, onsets, win).astype(float)
    b = window_counts(spikes, onsets, WIN_PRE).astype(float)
    if reading == "a":
        return 100 * c.mean() / b.mean() if b.sum() > 0 else np.nan
    keep = b > 0
    return 100 * np.mean(c[keep] / b[keep]) if keep.any() else np.nan


def baseline_test(x, x_pre2, reading, alternative="greater"):
    """Raw p of a window's normalized rates against baseline (claims file O3).

    O3a: two-sample rank-sum against the prestimulation window itself (100% for every unit).
    O3b: two-sample rank-sum against the units' normalized rate 134 to 67 ms before onset.
    O3c: one-sample signed-rank test against 100%.
    """
    x = np.asarray(x, float)
    if reading == "a":
        return stats.mannwhitneyu(x, np.full(len(x), 100.0), alternative=alternative).pvalue
    if reading == "b":
        return stats.mannwhitneyu(x, np.asarray(x_pre2, float), alternative=alternative).pvalue
    return stats.wilcoxon(x - 100.0, alternative=alternative).pvalue


def bonferroni(p, k):
    return min(1.0, p * k)
