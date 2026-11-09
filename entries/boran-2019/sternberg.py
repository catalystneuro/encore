"""Loading and measures for dandiset 000574 (human MTL units, scalp EEG and iEEG, Sternberg task).

Boran, Fedele, Klaver, Hilfiker, Stieglitz, Grunwald & Sarnthein (2019), Science Advances 5,
eaav3687, doi:10.1126/sciadv.aav3687. Files are streamed from the archive at the pinned
version with remfile and h5py; nothing is written to disk.

Each NWB file holds one session of 50 trials. Only the 8 s of each trial are stored (trial
start = fixation onset, probe onset at +6 s, trial end at +8 s), so all times here are made
relative to probe onset, as in the paper ("Times are relative to probe onset"). Trial periods
are from the paper (Methods, Task): fixation [-6, -5] s, encoding [-5, -3] s, maintenance
[-3, 0] s, probe at 0 s.

Where the parameters come from:

- Regions of units: the units' `electrodes` column points at macroelectrode rows of the
  electrodes table; the microwire bundle is named by that row's label without its contact
  number (AHL, PHR, ECL, AL...). The claims file (neurons-recorded criterion, as amended after
  the question of 2026-10-30) takes the region of a unit from the tip contact of its
  electrode, where the microwires protrude: (a) its anatomical label as updated after visual
  inspection of MRI, (b) its Brainnetome label. That contact 1 is the tip is established from
  the coordinates (contact 1 is nearest the midline, checked in the notebook). The dandiset's
  `location` of a contact is the label of the G-Node deposit (doi:10.12751/g-node.d76994),
  where the four tip contacts flagged as manually entered carry the updated label, so
  `location` is reading (a); for reading (b) the units of a flagged tip contact have no
  Brainnetome label in either deposit and are left out (`gin_electrodes`, `tip_regions`).
  Hipp is hippocampus, PhG entorhinal cortex, Amyg amygdala. `region_of` gives the variant by
  electrode name: AH and PH hippocampus, EC entorhinal cortex, A amygdala (Table 1 of the
  data descriptor).
- IN/OUT: `response_type` holds 51 (IN) and 52 (OUT) on correct trials and 1 (IN) and 2 (OUT)
  on incorrect ones. The meaning is read from the data: with `solution`, every correct trial
  has 51 when the probe was in the set, and every incorrect trial has 1 when it was not
  (checked in the notebook). The codes are not described in the files.
- Spike times are sorted on loading; some units store them unsorted (counted in the notebook).
- Hippocampal iEEG: one bipolar signal per hippocampal macroelectrode from its two deepest
  contacts, contact 1 minus contact 2 (Methods, Recording setup, "Only one bipolar signal from a
  pair involving the deepest contacts of each macroelectrode"). That contact 1 is the deepest
  is an assumption from the coordinates (contact 1 is nearest the midline, checked in the
  notebook).
- Multitaper spectra: +/- 2 Hz smoothing with seven tapers on 2-s epochs (Methods, Frequency
  spectra). FieldTrip's mtmfft takes tapers = 2 * T * W - 1 = 7 for T = 2 s and W = 2 Hz, so
  DPSS with NW = 4 and K = 7; the frequency resolution is 0.5 Hz.
- PLV: Methods equation 3. How the tapers enter is not stated. `plv` follows FieldTrip (cited
  by the Methods for the spectra and the PLV): the cross-spectrum of each trial is averaged
  over tapers, then normalized and averaged over trials (assumption, the toolbox's standard
  path). `plv_tapers`, normalizing each taper on its own, is shown as a variant.
"""

from __future__ import annotations

import re
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy.signal.windows import dpss

DANDISET_ID = "000574"
DANDISET_VERSION = "0.250815.1108"
API = "https://api.dandiarchive.org/api"

FIX = (-6.0, -5.0)
ENC = (-5.0, -3.0)
MAINT = (-3.0, 0.0)
LAST2 = (-2.0, 0.0)          # last 2 s of maintenance (Methods, Frequency spectra)
PROBE_OFFSET = 6.0           # probe onset relative to trial start (Methods, Task)
IN_CODES = ("51", "1")    # IN on correct trials 51, on incorrect trials 1 (read from the data)


def assets():
    """Asset paths and ids of the pinned version, sorted by path."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=200"
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    rows = [(a["path"], a["asset_id"], a["size"]) for a in r.json()["results"]]
    return pd.DataFrame(rows, columns=["path", "asset_id", "size"]).sort_values("path").reset_index(drop=True)


def s3_url(asset_id):
    """The asset's S3 address (from its metadata); reading it directly avoids a redirect on
    every range request, which halves streaming time."""
    r = requests.get(f"{API}/assets/{asset_id}/", timeout=60)
    r.raise_for_status()
    return [u for u in r.json()["contentUrl"] if "amazonaws" in u][0]


def open_asset(asset_id):
    return h5py.File(remfile.File(s3_url(asset_id)), "r")


def _str(a):
    return np.array([x.decode() if isinstance(x, bytes) else x for x in a], dtype=object)


def _scalar(x):
    x = x[()]
    return x.decode() if isinstance(x, bytes) else x


def region_of(bundle):
    if bundle.startswith(("AH", "PH")):
        return "hippocampus"
    if bundle.startswith("EC"):
        return "entorhinal"
    if bundle.startswith("A"):
        return "amygdala"
    return "other"


ATLAS_REGION = {"Hipp": "hippocampus", "PhG": "entorhinal", "Amyg": "amygdala"}

# The G-Node deposit the data descriptor names (Data Records), pinned at a commit. Its NIX
# files hold, per contact, the anatomical label (the source of the dandiset's `location`) and
# a flag `iEEG_Electrode_Manual_Entry` marking labels entered by hand ("Anatomical label
# updated after visual inspection of MRI", data descriptor, Data Records). The server does not
# serve byte ranges, so a whole file is read into memory; the smallest session of each subject
# is used, since the electrodes of a subject are the same in all its sessions.
GIN = ("https://gin.g-node.org/USZ_NCH/Human_MTL_units_scalp_EEG_and_iEEG_verbal_WM/raw/"
       "0b27b34ecd0da217e4403bdd080b4a0d78f155fd/data_nix/")
GIN_SESSIONS = {1: 4, 2: 7, 3: 3, 4: 2, 5: 3, 6: 7, 7: 4, 8: 5, 9: 2}


def _gin_request(method, url, timeout):
    """A request to the G-Node server, retried on server errors (it returns 500 now and then)."""
    import time
    for attempt in range(5):
        r = requests.request(method, url, timeout=timeout, allow_redirects=True)
        if r.status_code < 500:
            break
        time.sleep(10 * (attempt + 1))
    r.raise_for_status()
    return r


def _gin_subject(s):
    import io
    sizes = {}
    for k in range(1, GIN_SESSIONS[s] + 1):
        r = _gin_request("HEAD", GIN + f"Data_Subject_{s:02d}_Session_{k:02d}.h5", 60)
        sizes[k] = int(r.headers["content-length"])
    k = min(sizes, key=sizes.get)
    r = _gin_request("GET", GIN + f"Data_Subject_{s:02d}_Session_{k:02d}.h5", 1800)
    with h5py.File(io.BytesIO(r.content), "r") as f:
        da = f[f"data/Data_Subject_{s:02d}_Session_{k:02d}/data_arrays"]
        me = da["iEEG_Electrode_Manual_Entry"]
        names = list(_str(me["dimensions/1/labels"][:]))
        manual = me["data"][:, 0].astype(bool)
        mp = da["iEEG_Electrode_Map/sources"]
        label_of = {}
        for g in mp.values():
            sub = [g["sources"][x].attrs["name"] for x in g["sources"]]
            sub = [x.decode() if isinstance(x, bytes) else x for x in sub]
            name = [x for x in sub if x in names][0]
            label_of[name] = [x for x in sub if x != name][0]
        mni = da["iEEG_Electrode_MNI_Coordinates/data"][:]
    return pd.DataFrame({"subject": f"{s:02d}", "session_read": f"{k:02d}", "label": [n[1:] for n in names],
                         "gin_location": [label_of[n] for n in names], "manual_entry": manual,
                         "mni_x": mni[:, 0], "mni_y": mni[:, 1], "mni_z": mni[:, 2]})


def gin_electrodes(workers=3):
    """Contacts of the G-Node deposit, one row per subject and contact: the contact label
    without the deposit's leading "m", the anatomical label, the manual-entry flag and the MNI
    coordinates."""
    with ThreadPoolExecutor(workers) as ex:
        return pd.concat(ex.map(_gin_subject, sorted(GIN_SESSIONS)), ignore_index=True)


def tip_regions(subject, bundle, location_of, manual_tips):
    """Region of a unit on `bundle` under readings (a) and (b) of the claims file: the label of
    the bundle's contact 1 (`location_of`, label -> dandiset location), and the same with the
    manually entered tip contacts (`manual_tips`, a set of (subject, label)) left out."""
    loc1 = location_of.get(bundle + "1", "?").split(",")[0]
    a = ATLAS_REGION.get(loc1, "other")
    b = "no Brainnetome label" if (subject, bundle + "1") in manual_tips else a
    return a, b, loc1


def load_session(path, asset_id):
    """Trials, trial stages, electrodes and units of one session (tables and spike times only)."""
    with open_asset(asset_id) as f:
        tr = f["intervals/trials"]
        trials = pd.DataFrame({
            "start": tr["start_time"][:], "stop": tr["stop_time"][:],
            "set_size": tr["set_size"][:], "solution": tr["solution"][:].astype(bool),
            "artifact": tr["artifact"][:].astype(bool), "response": _str(tr["response_type"][:]),
            "response_time": tr["response_time"][:], "correct_raw": tr["correct"][:],
            "probe_letter": _str(tr["probe_letter"][:]),
        })
        if "ttl_stage" in f["intervals"]:
            st = f["intervals/ttl_stage"]
            tags_idx = st["tags_index"][:]
            tags = _str(st["tags"][:])
            starts = np.concatenate([[0], tags_idx[:-1]])
            stages = pd.DataFrame({"start": st["start_time"][:], "stop": st["stop_time"][:],
                                   "trial": st["trial_number"][:],
                                   "tag": [",".join(tags[a:b]) for a, b in zip(starts, tags_idx)]})
        else:
            stages = pd.DataFrame(columns=["start", "stop", "trial", "tag"])
        el = f["general/extracellular_ephys/electrodes"]
        elec = pd.DataFrame({c: el[c][:] for c in ["x", "y", "z", "is_inside_soz"]})
        for c in ["label", "group_name", "location"]:
            elec[c] = _str(el[c][:])
        has_units = "units" in f
        if has_units:
            u = f["units"]
            sidx = u["spike_times_index"][:]
            spikes = u["spike_times"][:]
            eidx = u["electrodes_index"][:]
            uel = u["electrodes"][:]
            wm = u["waveform_mean"][:]
            wsd = u["waveform_sd"][:]
            obs = u["obs_intervals"][:]
            oidx = u["obs_intervals_index"][:]
        meta = {k: _scalar(f[p]) for k, p in [("subject", "general/subject/subject_id"),
                                               ("description", "general/subject/description"),
                                               ("start_time", "session_start_time"),
                                               ("identifier", "identifier")]}
        shapes = {k: f[f"acquisition/ecephys.{k}/data"].shape for k in ["eeg", "ieeg", "lfp"]}
    stage_probe = stages[stages.tag == "Probe"].groupby("trial")["start"].min()
    trials["probe"] = trials["start"] + PROBE_OFFSET
    trials["stage_probe"] = stage_probe.reindex(np.arange(len(trials))).to_numpy()
    trials["rt"] = trials["response_time"] - trials["probe"]
    trials["correct"] = trials["correct_raw"] == 1
    trials["is_in"] = trials["response"].isin(IN_CODES)
    units = []
    if not has_units:
        sidx = []
    else:
        sb = np.concatenate([[0], sidx])
        ob = np.concatenate([[0], oidx])
        eb = np.concatenate([[0], eidx])
    for i in range(len(sidx)):
        rows = uel[eb[i]:eb[i + 1]]
        label = elec.label[rows[0]]
        bundle = re.sub(r"\d+$", "", label)
        units.append({"unit": i, "electrode_row": int(rows[0]), "label": label, "bundle": bundle,
                      "region": region_of(bundle), "spikes": np.sort(spikes[sb[i]:sb[i + 1]]),
                      "sorted_in_file": bool(np.all(np.diff(spikes[sb[i]:sb[i + 1]]) >= 0)),
                      "obs": obs[ob[i]:ob[i + 1]], "waveform_mean": wm[i], "waveform_sd": wsd[i]})
    sub = path.split("/")[0].replace("sub-", "")
    ses = path.split("_ses-")[1].split(".")[0]
    return {"path": path, "asset_id": asset_id, "subject": sub, "session": ses, "meta": meta,
            "trials": trials, "stages": stages, "electrodes": elec, "units": units, "shapes": shapes}


def load_all(table, workers=12):
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(lambda r: load_session(r.path, r.asset_id), table.itertuples()))


def aligned_spikes(spk, probes, lo=-6.0, hi=2.0):
    """Spike times of one unit relative to each trial's probe onset, a list over trials."""
    out = []
    for p in probes:
        a, b = np.searchsorted(spk, [p + lo, p + hi])
        out.append(spk[a:b] - p)
    return out


def count_in(aligned, window):
    lo, hi = window
    return np.array([np.sum((s >= lo) & (s < hi)) for s in aligned], dtype=float)


def rate_in(aligned, window):
    return count_in(aligned, window) / (window[1] - window[0])


def binned(aligned, edges):
    return np.array([np.histogram(s, edges)[0] for s in aligned], dtype=float)


# ---- statistics -------------------------------------------------------------------------

def perm_t(a, b, n_perm=2000, paired=False, rng=None):
    """Permutation t test as in EEGLAB statcond (Methods, Statistics: values of the two
    distributions mixed 2000 times). Paired: signs of the differences flipped. Returns
    (t, two-sided P), P = (exceedances + 1) / (n_perm + 1)."""
    rng = rng if rng is not None else np.random.default_rng(0)
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    if paired:
        d = a - b
        def tstat(x):
            s = x.std(axis=-1, ddof=1)
            with np.errstate(divide="ignore", invalid="ignore"):
                return np.where(s > 0, x.mean(axis=-1) / (s / np.sqrt(x.shape[-1])), 0.0)
        t0 = tstat(d)
        signs = rng.choice([-1.0, 1.0], size=(n_perm, d.size))
        tn = tstat(signs * d)
    else:
        x = np.concatenate([a, b])
        na = a.size
        def tstat2(xa, xb):
            va = xa.var(axis=-1, ddof=1)
            vb = xb.var(axis=-1, ddof=1)
            se = np.sqrt(va / xa.shape[-1] + vb / xb.shape[-1])
            with np.errstate(divide="ignore", invalid="ignore"):
                return np.where(se > 0, (xa.mean(axis=-1) - xb.mean(axis=-1)) / se, 0.0)
        t0 = tstat2(a, b)
        perms = np.argsort(rng.random((n_perm, x.size)), axis=1)
        xp = x[perms]
        tn = tstat2(xp[:, :na], xp[:, na:])
    p = (np.sum(np.abs(tn) >= abs(t0)) + 1) / (n_perm + 1)
    return float(t0), float(p)


# ---- spectra and PLV ---------------------------------------------------------------------

def mt_fourier(x, fs, nw=4.0, k=7):
    """Multitaper Fourier coefficients of epochs x (... x samples): tapers x ... x freqs.
    Each epoch is demeaned first (as FieldTrip does by default for mtmfft with demean)."""
    x = np.asarray(x, float)
    x = x - x.mean(axis=-1, keepdims=True)
    n = x.shape[-1]
    tap = dpss(n, nw, k)
    tap = tap.reshape((k,) + (1,) * (x.ndim - 1) + (n,))
    F = np.fft.rfft(tap * x[None], axis=-1)
    freqs = np.fft.rfftfreq(n, 1 / fs)
    return F, freqs


def mt_power(x, fs):
    F, f = mt_fourier(x, fs)
    return (np.abs(F) ** 2).mean(axis=0), f   # epochs x freqs


def plv(Fi, Fj):
    """PLV (Methods eq. 3) from multitaper coefficients (tapers x epochs x ... x freqs). The
    cross-spectrum of each epoch is averaged over tapers, normalized, and averaged over epochs,
    as FieldTrip's ft_connectivityanalysis does with method 'plv' on mtmfft output (the
    toolbox the Methods cite; the cross-spectra per trial are taper averages)."""
    c = (Fi * np.conj(Fj)).mean(axis=0)
    with np.errstate(divide="ignore", invalid="ignore"):
        c = c / np.abs(c)
    return np.abs(np.nanmean(c, axis=0))


def plv_tapers(Fi, Fj):
    """Variant: each taper's cross-spectrum normalized on its own, averaged over tapers and epochs."""
    c = Fi * np.conj(Fj)
    with np.errstate(divide="ignore", invalid="ignore"):
        c = c / np.abs(c)
    return np.abs(np.nanmean(c, axis=(0, 1)))


# ---- vectorized permutation tests --------------------------------------------------------
# For a permutation test whose relabelings keep the pooled values (sign flips of paired
# differences, or reassigning pooled values to two groups), the permutation distribution of a
# relabeled data set is the same as that of the original. So the reference distribution is
# computed once per unit and reused for the relabeled ("scrambled") repetitions of a selection.

def t_paired_rows(Dm):
    """Paired t of each row of Dm (rows = sets of differences)."""
    n = Dm.shape[-1]
    m = Dm.mean(-1)
    v = Dm.var(-1, ddof=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(v > 0, m / np.sqrt(v / n), 0.0)


def t_groups(X, G):
    """Unequal-variance t of group A (G True) against B for each row of the masks G (P x N),
    for every column of X (N x K). Returns P x K."""
    G = G.astype(float)
    na = G.sum(1, keepdims=True)
    nb = X.shape[0] - na
    s1 = G @ X
    q1 = G @ (X ** 2)
    S1, Q1 = X.sum(0), (X ** 2).sum(0)
    ma, mb = s1 / na, (S1 - s1) / nb
    va = (q1 - na * ma ** 2) / (na - 1)
    vb = ((Q1 - q1) - nb * mb ** 2) / (nb - 1)
    se = np.sqrt(np.clip(va, 0, None) / na + np.clip(vb, 0, None) / nb)
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(se > 0, (ma - mb) / se, 0.0)


def random_masks(n_a, n, n_perm, rng):
    """n_perm random boolean masks with n_a of n entries True."""
    r = rng.random((n_perm, n))
    idx = np.argsort(r, axis=1)[:, :n_a]
    G = np.zeros((n_perm, n), bool)
    np.put_along_axis(G, idx, True, axis=1)
    return G


def perm_p(t_obs, t_ref):
    """Two-sided permutation P of each observed t against the reference |t| values."""
    t_ref = np.sort(np.abs(np.asarray(t_ref)))
    k = len(t_ref) - np.searchsorted(t_ref, np.abs(np.asarray(t_obs)) - 1e-12, side="left")
    return (k + 1) / (len(t_ref) + 1)


def cluster_masses(Tm, thr):
    """Masses (sum of t) of positive and negative supra-threshold runs in each row of Tm (P x K).
    Returns (max |mass| per row, list of (start, stop, mass) for row 0)."""
    P, K = Tm.shape
    out = np.maximum(cluster_max(Tm, thr, 1), cluster_max(Tm, thr, -1))
    row0 = []
    for sign in (1, -1):
        sup = sign * Tm[0] > thr
        i = 0
        while i < K:
            if sup[i]:
                j = i
                while j < K and sup[j]:
                    j += 1
                row0.append((i, j, float(Tm[0, i:j].sum())))
                i = j
            else:
                i += 1
    return out, row0


def cluster_max(Tm, thr, sign=1):
    """Largest mass of runs with sign * t > thr in each row of Tm (P x K); 0 when none."""
    P, K = Tm.shape
    sup = sign * Tm > thr
    start = sup & ~np.concatenate([np.zeros((P, 1), bool), sup[:, :-1]], 1)
    rid = np.cumsum(start, 1) * sup
    flat = (np.arange(P)[:, None] * (K + 1) + rid)[sup]
    mass = np.bincount(flat, weights=(sign * Tm)[sup], minlength=P * (K + 1)).reshape(P, K + 1)
    return mass[:, 1:].max(1)


def cluster_test(X, g, n_perm, rng, alpha=0.05, sign=1, extra=None):
    """Cluster-based permutation test (Maris & Oostenveld 2007, as in FieldTrip; Methods,
    Statistics): runs of points with two-sided t beyond the threshold at alpha, cluster mass =
    sum of t, null of the maximal |cluster mass| over label permutations. Group g (True)
    against the rest; rows of X are trials. Returns the P of the largest cluster in direction
    `sign` (1.0 when there is none) and, if `extra` masks (relabelings) are given, the P of each
    of them against the same null."""
    from scipy import stats as _st
    n = len(g)
    thr = _st.t.ppf(1 - alpha / 2, n - 2)
    G = random_masks(int(g.sum()), n, n_perm, rng)
    Tn = t_groups(X, G)
    null = np.sort(np.maximum(cluster_max(Tn, thr, 1), cluster_max(Tn, thr, -1)))

    def pval(m):
        k = len(null) - np.searchsorted(null, m - 1e-12, side="left")
        return np.where(m > 0, (k + 1) / (len(null) + 1), 1.0)

    T0 = t_groups(X, g[None, :])
    p0 = float(pval(cluster_max(T0, thr, sign))[0])
    if extra is None:
        return p0
    Te = t_groups(X, extra)
    return p0, pval(cluster_max(Te, thr, sign))


# ---- scalp EEG and hippocampal iEEG ------------------------------------------------------

EEG_FS = 200.0      # deposited sampling rate (checked in the notebook)
IEEG_FS = 2000.0


def _load_signals(args):
    from scipy.signal import decimate
    path, asset_id = args
    with open_asset(asset_id) as f:
        el = f["general/extracellular_ephys/electrodes"]
        labels = _str(el["label"][:])
        soz = el["is_inside_soz"][:].astype(bool)
        xyz = np.stack([el["x"][:], el["y"][:], el["z"][:]], 1)
        e = f["acquisition/ecephys.eeg"]
        erows = e["electrodes"][:]
        eeg = e["data"][:].astype(np.float32)
        ets = e["timestamps"][:]
        ie = f["acquisition/ecephys.ieeg"]
        irows = ie["electrodes"][:]
        ilab = labels[irows]
        bundles = sorted({re.sub(r"\d+$", "", l) for l in ilab if re.match(r"^(AH|PH)[LR]\d+$", l)})
        chans, cols = [], []
        for b in bundles:
            c1 = np.where(ilab == b + "1")[0]
            c2 = np.where(ilab == b + "2")[0]
            if len(c1) and len(c2):
                chans.append(b)
                cols += [int(c1[0]), int(c2[0])]
        raw = np.stack([ie["data"][:, c] for c in cols], 1) if cols else np.zeros((ie["data"].shape[0], 0))
        its = ie["timestamps"][:]
        tr = f["intervals/trials"]
        starts = tr["start_time"][:]
    n_tr = len(starts)
    ne, ni = int(8 * EEG_FS), int(8 * IEEG_FS)
    eeg_ep = eeg.reshape(n_tr, ne, -1).transpose(0, 2, 1)
    bip = raw[:, 0::2] - raw[:, 1::2]
    bip_ep = bip.reshape(n_tr, ni, -1).transpose(0, 2, 1)
    bip_ep = decimate(bip_ep, 10, axis=-1, zero_phase=True).astype(np.float32) if bip.shape[1] else np.zeros((n_tr, 0, ne), np.float32)
    lab_rows = {l: i for i, l in enumerate(labels)}
    meta = {"eeg_labels": list(labels[erows]), "hipp_channels": chans,
            "hipp_soz": [bool(soz[lab_rows[c + "1"]] or soz[lab_rows[c + "2"]]) for c in chans],
            "hipp_xyz1": [xyz[lab_rows[c + "1"]] for c in chans],
            "hipp_xyz12": [(xyz[lab_rows[c + "1"]] + xyz[lab_rows[c + "2"]]) / 2 for c in chans],
            "eeg_start_err": float(np.max(np.abs(ets[::ne] - starts))),
            "ieeg_start_err": float(np.max(np.abs(its[::ni] - starts))),
            "eeg_dt": float(np.median(np.diff(ets[:ne]))), "ieeg_dt": float(np.median(np.diff(its[:ni])))}
    return path, eeg_ep, bip_ep, meta


def load_signals(table, workers=16):
    """Scalp EEG (trials x channels x 1600 samples at 200 Hz) and hippocampal bipolar iEEG
    (contact 1 minus contact 2 of each AH and PH macroelectrode, decimated to 200 Hz with a
    zero-phase filter) of every session, from -6 to +2 s around probe onset. Read in parallel
    processes (h5py serializes threads)."""
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(workers) as ex:
        out = list(ex.map(_load_signals, [(r.path, r.asset_id) for r in table.itertuples()]))
    return {p: {"eeg": e, "ieeg": i, **m} for p, e, i, m in out}


# ---- pseudopopulation decoding (Methods, Neural decoding of firing rates) -----------------
# A support vector machine (linear kernel, C = 1, the NDT toolbox's libsvm default) trained and
# tested at each time step on pseudopopulations: in each resampling run, for each neuron, a
# number of trials per class is drawn at random and spread over the cross-validation splits
# (one trial per class per split, NDT's default), features are z-scored with the training
# mean and SD (NDT's zscore_normalize_FP), and the accuracy is averaged over the splits. The
# null runs scramble the labels of each neuron's trials before drawing.

_DEC = {}


def _decode_chunk(args):
    from sklearn.svm import SVC
    seed, n_runs, n_splits, per_class, scramble, zscore = args
    rng = np.random.default_rng(seed)
    feats, labels = _DEC["feats"], _DEC["labels"]     # per neuron: trials x times, trials
    n_t = feats[0].shape[1]
    classes = (0, 1)
    out = np.zeros((n_runs, n_t))
    for r in range(n_runs):
        # draw trials: for each class, per_class[c] trials per neuron, assigned to splits in turn
        Xc = {c: np.zeros((per_class[c], len(feats), n_t)) for c in classes}
        for j, (F, y) in enumerate(zip(feats, labels)):
            yy = rng.permutation(y) if scramble else y
            for c in classes:
                idx = np.flatnonzero(yy == c)
                pick = rng.choice(idx, per_class[c], replace=False)
                Xc[c][:, j, :] = F[pick]
        split_of = {c: np.arange(per_class[c]) % n_splits for c in classes}
        acc = np.zeros(n_t)
        for t in range(n_t):
            a_t = []
            for s in range(n_splits):
                tr = [Xc[c][split_of[c] != s, :, t] for c in classes]
                te = [Xc[c][split_of[c] == s, :, t] for c in classes]
                Xtr = np.concatenate(tr)
                ytr = np.concatenate([np.full(len(x), c) for c, x in zip(classes, tr)])
                Xte = np.concatenate(te)
                yte = np.concatenate([np.full(len(x), c) for c, x in zip(classes, te)])
                if zscore:
                    mu, sd = Xtr.mean(0), Xtr.std(0)
                    sd[sd == 0] = 1.0
                    Xtr, Xte = (Xtr - mu) / sd, (Xte - mu) / sd
                clf = SVC(kernel="linear", C=1.0).fit(Xtr, ytr)
                a_t.append(np.mean(clf.predict(Xte) == yte))
            acc[t] = np.mean(a_t)
        out[r] = acc
    return out


def decode(feats, labels, n_splits, n_runs, rng, scramble=False, zscore=True, per_class=None, workers=4):
    """Accuracy (runs x time steps). feats: list over neurons of trials x time-step features;
    labels: list over neurons of 0/1 class labels per trial. per_class: trials drawn per class
    (default n_splits each, balanced)."""
    from concurrent.futures import ProcessPoolExecutor
    import multiprocessing as mp
    per_class = per_class or {0: n_splits, 1: n_splits}
    _DEC["feats"], _DEC["labels"] = feats, labels
    chunks = np.array_split(np.arange(n_runs), workers)
    seeds = rng.integers(0, 2 ** 31, len(chunks))
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("fork")) as ex:
        res = list(ex.map(_decode_chunk, [(int(s), len(c), n_splits, per_class, scramble, zscore)
                                          for s, c in zip(seeds, chunks) if len(c)]))
    return np.concatenate(res)


# ---- dPCA (Kobak et al. 2016; Methods, dPCA of firing rates) -----------------------------

def _svd(M):
    """Thin SVD; falls back to LAPACK gesvd when gesdd does not converge (subsamples drawn with
    replacement repeat rows, which gesdd sometimes fails on)."""
    try:
        return np.linalg.svd(M, full_matrices=False)
    except np.linalg.LinAlgError:
        from scipy.linalg import svd
        return svd(M, full_matrices=False, lapack_driver="gesvd")


def dpca(X, n_comp=15, lam=0.0):
    """dPCA of trial-averaged data X (neurons x set sizes x times) with a time marginalization
    and a set-size marginalization (set size plus its interaction with time). For each
    marginalization the reduced-rank regression of Kobak et al. (2016): B = X_phi X' (X X' +
    mu I)^-1 with mu = (lam ||X||)^2 (lam = 0 uses the pseudo-inverse), decoder and encoder
    from the SVD of B X. Returns components ordered by explained variance: a list of dicts
    with marginalization, decoder (neurons), encoder, and explained variance (% of the total)."""
    N, Sn, Tn = X.shape
    Xc = X - X.mean(axis=(1, 2), keepdims=True)
    Xf = Xc.reshape(N, -1)
    Xt = np.broadcast_to(Xc.mean(1, keepdims=True), Xc.shape).reshape(N, -1)
    margs = {"time": Xt, "set size": Xf - Xt}
    total = np.sum(Xf ** 2)
    # X X' + mu I through the thin SVD of X: B = X_phi V S / (S^2 + mu) U' (mu = 0 is the
    # pseudo-inverse, singular values below 1e-10 of the largest dropped)
    U0, S0, Vt0 = _svd(Xf)
    keep = S0 > 1e-10 * S0[0]
    U0, S0, Vt0 = U0[:, keep], S0[keep], Vt0[keep]
    mu = (lam * np.sqrt(total)) ** 2
    comps = []
    for name, Xm in margs.items():
        B = ((Xm @ Vt0.T) * (S0 / (S0 ** 2 + mu))) @ U0.T
        U, s, Vt = _svd(B @ Xf)
        for k in range(min(n_comp, U.shape[1])):
            enc = U[:, k]
            dec = U[:, k] @ B
            z = dec @ Xf
            # ||X - enc z||^2 = ||X||^2 - 2 enc' X z + ||enc||^2 ||z||^2
            ev = 100 * (2 * enc @ (Xf @ z) - (enc @ enc) * (z @ z)) / total
            comps.append({"marg": name, "decoder": dec, "encoder": enc, "ev": ev,
                          "z": z.reshape(Sn, Tn)})
    comps.sort(key=lambda c: -c["ev"])
    return comps[:n_comp], Xf, total


def cumulative_ev(comps, Xf, total, k):
    """Variance of the data explained jointly by the first k components (% of the total)."""
    E = np.array([c["encoder"] for c in comps[:k]]).T
    Dm = np.array([c["decoder"] for c in comps[:k]])
    R = Xf - E @ (Dm @ Xf)
    return 100 * (total - np.sum(R ** 2)) / total


# ---- spike-field coherence ---------------------------------------------------------------

LFP_FS = 32000.0
SFC_FS = 1000.0


def _load_wire(args):
    """One microwire LFP column, its bundle's deepest bipolar iEEG pair and the scalp EEG of one
    session, as trials x samples, the LFP decimated to 1 kHz with zero-phase filters."""
    from scipy.signal import decimate
    asset_id, lfp_row, bundle, scalp = args
    with open_asset(asset_id) as f:
        labels = _str(f["general/extracellular_ephys/electrodes/label"][:])
        lf = f["acquisition/ecephys.lfp"]
        col = int(np.flatnonzero(lf["electrodes"][:] == lfp_row)[0])
        x = lf["data"][:, col].astype(np.float64)
        ie = f["acquisition/ecephys.ieeg"]
        il = labels[ie["electrodes"][:]]
        c1, c2 = np.flatnonzero(il == bundle + "1"), np.flatnonzero(il == bundle + "2")
        bip = (ie["data"][:, int(c1[0])] - ie["data"][:, int(c2[0])]) if len(c1) and len(c2) else None
        e = f["acquisition/ecephys.eeg"]
        el = list(labels[e["electrodes"][:]])
        eeg = e["data"][:, [el.index(scalp), el.index("A1"), el.index("A2")]] if scalp in el else None
        n_tr = len(f["intervals/trials/start_time"][:])
    lfp = decimate(decimate(x.reshape(n_tr, -1), 8, axis=-1, zero_phase=True), 4, axis=-1, zero_phase=True)
    out = {"lfp": lfp.astype(np.float32)}
    if bip is not None:
        out["ieeg"] = decimate(bip.reshape(n_tr, -1), 2, axis=-1, zero_phase=True).astype(np.float32)   # 1 kHz
    if eeg is not None:
        ref = eeg[:, 0] - eeg[:, 1:].mean(1)            # re-referenced to the averaged mastoids
        out["eeg"] = ref.reshape(n_tr, -1).astype(np.float32)                                   # 200 Hz
    return out


def load_wires(jobs, workers=20):
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(_load_wire, jobs))


def spike_phases_setup(x, fs, freqs, cycles):
    """Complex convolution of each trial (trials x samples) with Hanning-tapered complex
    exponentials of `cycles` cycles per frequency, as FieldTrip's spike-triggered spectrum
    (ft_spiketriggeredspectrum_convol) uses around each spike. NaN where the window passes the
    trial's edges. Returns trials x samples x freqs (complex64)."""
    from scipy.signal import fftconvolve
    n_tr, n = x.shape
    out = np.full((n_tr, n, len(freqs)), np.nan + 0j, dtype=np.complex64)
    for k, f in enumerate(freqs):
        L = int(round(cycles / f * fs))
        L += (L % 2 == 0)
        t = (np.arange(L) - L // 2) / fs
        w = np.hanning(L) * np.exp(-2j * np.pi * f * t)
        c = fftconvolve(x, w[None, ::-1], mode="same", axes=1)
        h = L // 2
        c[:, :h] = np.nan
        c[:, n - h:] = np.nan
        out[:, :, k] = c
    return out


def ppc2(Z, trial_of):
    """P-hat-2 of Vinck et al. (2012) per frequency: unit vectors Z (spikes x freqs) whose
    pairs are counted only across trials."""
    Z = Z / np.abs(Z)
    ok = np.isfinite(Z).all(1)
    Z, trial_of = Z[ok], trial_of[ok]
    if len(np.unique(trial_of)) < 2:
        return np.full(Z.shape[1], np.nan)
    tr = np.unique(trial_of, return_inverse=True)[1]
    Sm = np.zeros((tr.max() + 1, Z.shape[1]), complex)
    np.add.at(Sm, tr, Z)
    Nm = np.bincount(tr).astype(float)
    num = np.abs(Sm.sum(0)) ** 2 - (np.abs(Sm) ** 2).sum(0)
    den = Nm.sum() ** 2 - (Nm ** 2).sum()
    return num / den
