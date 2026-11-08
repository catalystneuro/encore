"""Loading and measures for the HD-MEA culture recordings of dandiset 002020.

Nakamuta et al., "Self-organization of high-dimensional geometry of neural activity in culture",
bioRxiv doi:10.1101/2025.01.14.630383 (version 1 read). Each NWB file holds one 30-minute
recording of one dish: unsorted channel-level spike detections (frame number, time from the
first detected spike, readout channel, amplitude) and the electrode table with chip-plane x and
y in micrometres. Files are streamed from the archive at the pinned version; nothing is written
to disk.

Where the parameters come from (the claims file's opening comment, "Shared method", cites the
paper for each; "claims" below means that comment or a claim's criterion):

- 100 ms bins over 30 minutes, 18,000 bins (claims; Methods, Data processing, paragraph 2).
  The bins start at the first detected spike, as the files give no recording-start frame.
- Selection at 0.03 Hz (claims; Methods, Data processing, paragraph 1), two readings: S1 keeps
  electrodes whose mean rate over the 30 minutes exceeds 0.03 Hz; S2 keeps recordings whose mean
  rate over electrodes exceeds 0.03 Hz, with all their electrodes.
- Variance spectrum: eigenvalues of the electrode by electrode covariance of the counts, in
  descending order, all positive ones (claims; Methods, paragraph 2).
- Fit f(x) = a x^-c exp(-b x), b >= 0, least squares (claims; Methods, Parameter fitting).
  F1 on log values, F2 on raw values. For avalanches, sizes 1 to 128 (Methods). Sizes with no
  cascade are left out of both fits (a standard choice: the log of zero is undefined for F1).
  A fit needs at least `MIN_POINTS` points (a standard choice).
- Shuffle: independent circular shift of each electrode's binned series (Figure 1D legend);
  the seed is a standard choice.
- Local Moran's I with w_ij = 1 within 200 um, row-normalized, threshold 0.0001 (Methods,
  Spatial structure of PCs). M1 Anselin's normalized form, M2 without the variance
  normalization; w_ii = 0 as the main reading and w_ii = 1 as a variant (claims). Locality
  slope: L1 slope of locality against log10 PC index, L2 slope of log10 locality against PC
  index, over PCs with a positive eigenvalue; for L2, PCs with locality 0 are left out (a
  standard choice, the log of zero being undefined).
- Avalanches: spikes of all kept electrodes pooled into one train; a cascade is a maximal run
  of spikes whose successive intervals are shorter than the train's mean interval (claims;
  Methods, Neuronal avalanches, citing ref. 22). Size A1 is the number of spikes, A2 the number
  of distinct electrodes.
- Synchrony (claim fig1b-async-to-bursts): (a) mean pairwise Pearson correlation of the
  100 ms counts, (b) the largest fraction of kept electrodes active in one 100 ms bin.
- PC time scales (claim no-temporal-structure): (a) the first lag at which the autocorrelation
  of a PC's projection falls below 1/e, (b) the integral of the autocorrelation from lag 0 to
  its first non-positive lag (the reading chosen here of "the integral of the positive part",
  a choice stated as one), both in seconds; lags up to `MAX_LAG_BINS`.
- Days in vitro are not in the dataset (the files say so). `day` is days since the dish's
  first recording in the dataset; DIV = day + d0 is an assumption made in the notebook.
"""

from __future__ import annotations

import datetime as dt
import zlib
from functools import lru_cache

import h5py
import numpy as np
import remfile
import requests
from scipy import optimize, sparse

DANDISET_ID = "002020"
DANDISET_VERSION = "0.261004.1410"
API = "https://api.dandiarchive.org/api"

BIN_S = 0.1
DURATION_S = 1800.0
N_BINS = int(round(DURATION_S / BIN_S))
RATE_HZ = 0.03
RADIUS_UM = 200.0
MORAN_THRESHOLD = 1e-4
AVALANCHE_MAX = 128
MIN_POINTS = 10
MAX_LAG_BINS = 3000      # 5 minutes of lags for the PC time scales, a standard choice
B_THRESHOLD = 0.1        # Results, Co-occurrence, paragraph 3


def list_assets():
    """All NWB assets of the pinned version: path, asset id, dish, date."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=500"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        for a in r["results"]:
            if a["path"].endswith(".nwb"):
                ses = a["path"].split("_ses-")[1].split("_")[0]
                dish, date = ses.split("-")
                out.append(dict(path=a["path"], asset_id=a["asset_id"], size=a["size"],
                                dish=dish, date=dt.datetime.strptime(date, "%y%m%d").date()))
        url = r.get("next")
    out.sort(key=lambda d: (d["dish"], d["date"]))
    return out


def s3_url(asset_id):
    r = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60)
    return r.url


def load_recording(asset_id):
    """Spike times (s from first spike), electrode index per spike, electrode x, y (um), metadata."""
    with h5py.File(remfile.File(s3_url(asset_id)), "r") as f:
        ecp = "processing/ecephys/"
        el = f["general/extracellular_ephys/electrodes"]
        x = el["source_x_um"][:]
        y = el["source_y_um"][:]
        el_chan = el["source_channel"][:]
        el_id = el["source_electrode"][:]
        assoc = f[ecp + "channel_electrode_associations"]
        a_chan = assoc["source_channel"][:]
        a_el = assoc["electrode"][:]
        sp = f[ecp + "detected_spikes"]
        t = sp["time_from_first_spike_seconds"][:]
        ch = sp["source_channel"][:]
        frames = sp["source_frame_number"][:]
        prov = f[ecp + "conversion_provenance"]
        meta = dict(
            subject=f["general/subject/subject_id"][()].decode(),
            session=f["general/session_id"][()].decode(),
            start=f["session_start_time"][()].decode(),
            duration_s=float(prov["duration_s"][0]),
            fs=float(prov["sampling_rate_hz"][0]),
            first_frame=int(prov["first_spike_frame_number"][0]),
            unresolved_events=int(prov["unresolved_event_count"][0]),
            subject_age=f["general/subject/age"][()].decode(),
            mapping_xy=np.c_[f[ecp + "source_mapping/source_x"][:], f[ecp + "source_mapping/source_y"][:]],
            mapping_el=f[ecp + "source_mapping/source_electrode"][:],
        )
    lut = np.full(max(int(ch.max()), int(a_chan.max())) + 1, -1, dtype=np.int64)
    lut[a_chan] = a_el
    e = lut[ch]
    keep = e >= 0
    meta["n_spikes_total"] = len(t)
    meta["n_spikes_unmapped"] = int((~keep).sum())
    # Checks of the description against the values.
    meta["frames_match_times"] = bool(np.allclose((frames - frames.min()) / meta["fs"], t, atol=1e-6))
    meta["times_sorted"] = bool(np.all(np.diff(t) >= 0))
    meta["t_max"] = float(t.max())
    meta["grid_ok"] = bool(np.allclose(x, (el_id % 220) * 17.5) and np.allclose(y, (el_id // 220) * 17.5))
    meta["channels_unique"] = len(np.unique(el_chan)) == len(el_chan)
    return t[keep], e[keep], x, y, meta


def bin_counts(t, e, n_el):
    """Electrode by bin spike counts, 100 ms bins from the first spike; spikes after 1800 s dropped."""
    b = np.floor(t / BIN_S).astype(np.int64)
    ok = b < N_BINS
    X = np.zeros((n_el, N_BINS), dtype=np.float64)
    np.add.at(X, (e[ok], b[ok]), 1.0)
    return X


def circular_shuffle(X, rng):
    """Independent circular shift of each row (Figure 1D legend); returns the shifted X and shifts."""
    shifts = rng.integers(0, X.shape[1], X.shape[0])
    idx = (np.arange(X.shape[1])[None, :] - shifts[:, None]) % X.shape[1]
    return np.take_along_axis(X, idx, axis=1), shifts


def shuffle_spikes(t, e, shifts):
    """The same shuffle on spike times: each electrode's spikes shifted by its bin shift, modulo 30 min."""
    ok = t < DURATION_S
    return (t[ok] + shifts[e[ok]] * BIN_S) % DURATION_S, e[ok]


def pca(X):
    """Eigenvalues (descending, positive) and eigenvectors of the covariance of the rows of X."""
    Xc = X - X.mean(axis=1, keepdims=True)
    C = Xc @ Xc.T / (X.shape[1] - 1)
    w, V = np.linalg.eigh(C)
    order = np.argsort(w)[::-1]
    w, V = w[order], V[:, order]
    pos = w > max(w[0], 0) * 1e-12
    return w[pos], V[:, pos], Xc


def neighbour_matrix(x, y, self_weight=False):
    """Row-normalized w_ij = 1 for electrodes within 200 um (Methods, Spatial structure of PCs)."""
    d2 = (x[:, None] - x[None, :]) ** 2 + (y[:, None] - y[None, :]) ** 2
    W = (d2 <= RADIUS_UM ** 2).astype(float)
    if not self_weight:
        np.fill_diagonal(W, 0.0)
    rs = W.sum(axis=1, keepdims=True)
    W = np.divide(W, rs, out=np.zeros_like(W), where=rs > 0)
    return sparse.csr_matrix(W)


def locality(V, W, normalized):
    """Number of electrodes with local Moran's I above 0.0001, for each PC (column of V)."""
    Z = V - V.mean(axis=0, keepdims=True)
    I = Z * (W @ Z)
    if normalized:
        m2 = (Z ** 2).sum(axis=0, keepdims=True) / Z.shape[0]
        I = np.divide(I, m2, out=np.zeros_like(I), where=m2 > 0)
    return (I > MORAN_THRESHOLD).sum(axis=0)


def locality_slopes(loc):
    """L1 slope against log10 PC index, L2 slope of log10 locality against PC index."""
    k = np.arange(1, len(loc) + 1, dtype=float)
    out = {}
    if len(loc) >= MIN_POINTS:
        out["L1"] = float(np.polyfit(np.log10(k), loc, 1)[0])
        nz = loc > 0
        out["L2"] = float(np.polyfit(k[nz], np.log10(loc[nz]), 1)[0]) if nz.sum() >= MIN_POINTS else np.nan
    else:
        out["L1"] = out["L2"] = np.nan
    return out


def avalanche_distribution(t, e):
    """P(S) for S = 1..128 under sizes A1 (spikes) and A2 (distinct electrodes); cascade count."""
    if not np.all(np.diff(t) >= 0):
        order = np.argsort(t, kind="stable")
        t, e = t[order], e[order]
    if len(t) < 3:
        return None
    isi = np.diff(t)
    misi = isi.mean()
    brk = np.flatnonzero(isi >= misi) + 1
    starts = np.r_[0, brk]
    ends = np.r_[brk, len(t)]
    sz_spk = ends - starts
    # Distinct electrodes per cascade: order spikes by electrode (stable, so by time within an
    # electrode); a spike whose predecessor is on the same electrode and in the same cascade repeats it.
    cid = np.repeat(np.arange(len(starts)), sz_spk)
    by_el = np.argsort(e, kind="stable")
    ce, cc = e[by_el], cid[by_el]
    dup = np.r_[False, (ce[1:] == ce[:-1]) & (cc[1:] == cc[:-1])]
    sz_el = sz_spk - np.bincount(cc[dup], minlength=len(starts))
    n = len(starts)
    res = {"n_cascades": n, "misi_ms": float(misi * 1e3)}
    for name, s in (("A1", sz_spk), ("A2", sz_el)):
        h = np.bincount(np.minimum(s, AVALANCHE_MAX + 1), minlength=AVALANCHE_MAX + 2)[1:AVALANCHE_MAX + 1]
        res[name] = h / n
        res[name + "_max"] = int(s.max())
    return res


def fit_decay(y, method, x=None):
    """Fit y = a x^-c exp(-b x) with b >= 0; returns (a, b, c). F1 on log values, F2 on raw."""
    y = np.asarray(y, float)
    if x is None:
        x = np.arange(1, len(y) + 1, dtype=float)
    ok = y > 0
    x, y = x[ok], y[ok]
    if len(y) < MIN_POINTS:
        return (np.nan, np.nan, np.nan)
    # log y = log a - c log x - b x, linear in (log a, c, b).
    A = np.c_[np.ones_like(x), -np.log(x), -x]
    r = optimize.lsq_linear(A, np.log(y), bounds=([-np.inf, -np.inf, 0.0], [np.inf, np.inf, np.inf]))
    la, c, b = r.x
    if method == "F1":
        return (float(np.exp(la)), float(b), float(c))
    scale = y[0]

    def resid(p):
        return (np.exp(p[0]) * x ** (-p[2]) * np.exp(-p[1] * x) - y) / scale

    best = None
    for start in ([la, b, c], [np.log(y[0]), 0.0, 1.0], [np.log(y[0]), 0.1, 0.0]):
        try:
            rr = optimize.least_squares(resid, start, bounds=([-np.inf, 0.0, -np.inf], [np.inf, np.inf, np.inf]),
                                        max_nfev=2000)
        except Exception:
            continue
        if best is None or rr.cost < best.cost:
            best = rr
    if best is None:
        return (np.nan, np.nan, np.nan)
    return (float(np.exp(best.x[0])), float(best.x[1]), float(best.x[2]))


def fit_power(y, x=None):
    """Pure power law y = a x^-c on log values (claim fig1e-example-dish, reading c)."""
    y = np.asarray(y, float)
    if x is None:
        x = np.arange(1, len(y) + 1, dtype=float)
    ok = y > 0
    if ok.sum() < MIN_POINTS:
        return np.nan
    return float(-np.polyfit(np.log(x[ok]), np.log(y[ok]), 1)[0])


def time_scales(V, Xc):
    """Per PC, (a) first lag below 1/e and (b) integral to the first non-positive lag, in seconds."""
    P = V.T @ Xc
    n = P.shape[1]
    nfft = 1 << int(np.ceil(np.log2(2 * n)))
    F = np.fft.rfft(P, nfft, axis=1)
    ac = np.fft.irfft(F * np.conj(F), nfft, axis=1)[:, :MAX_LAG_BINS + 1]
    ac0 = ac[:, :1]
    ac = np.divide(ac, ac0, out=np.zeros_like(ac), where=ac0 > 0)
    below = ac < np.exp(-1)
    below[:, -1] = True
    tau_e = below.argmax(axis=1) * BIN_S
    nonpos = ac <= 0
    nonpos[:, -1] = True
    first = nonpos.argmax(axis=1)
    cum = np.cumsum(ac, axis=1)
    tau_i = cum[np.arange(len(first)), np.maximum(first - 1, 0)] * BIN_S
    return tau_e, tau_i


def synchrony(X):
    """(a) mean pairwise Pearson correlation, (b) largest fraction of electrodes active in one bin."""
    sd = X.std(axis=1)
    Y = X[sd > 0]
    if len(Y) < 2:
        return np.nan, np.nan
    R = np.corrcoef(Y)
    iu = np.triu_indices(len(Y), 1)
    frac = ((X > 0).sum(axis=0) / X.shape[0]).max()
    return float(R[iu].mean()), float(frac)


def analyse(asset, seed):
    """All per-recording measures under both selection readings. Returns a dict of arrays."""
    t, e, x, y, meta = load_recording(asset["asset_id"])
    n_el = len(x)
    X_all = bin_counts(t, e, n_el)
    rates = np.bincount(e, minlength=n_el) / DURATION_S
    out = dict(meta=meta, dish=asset["dish"], date=asset["date"], n_el=n_el,
               mean_rate=float(rates.mean()), n_above=int((rates > RATE_HZ).sum()),
               max_rate=float(rates.max()), pop=X_all.sum(axis=0).astype(np.int32))
    rng = np.random.default_rng(seed)
    shifts_X, shifts = circular_shuffle(X_all, rng)
    for sel in ("S1", "S2"):
        if sel == "S1":
            keep = rates > RATE_HZ
        else:
            keep = np.ones(n_el, bool) if rates.mean() > RATE_HZ else np.zeros(n_el, bool)
        res = {"n_kept": int(keep.sum())}
        if keep.sum() >= MIN_POINTS:
            X = X_all[keep]
            xs, ys = x[keep], y[keep]
            ev, V, Xc = pca(X)
            evs, Vs, _ = pca(shifts_X[keep])
            res["ev"], res["ev_shuf"] = ev, evs
            res["sync"] = synchrony(X)
            for sw in (False, True):
                W = neighbour_matrix(xs, ys, self_weight=sw)
                for mname, norm in (("M1", True), ("M2", False)):
                    key = f"{mname}{'_self' if sw else ''}"
                    res["loc_" + key] = locality(V, W, norm)
                    res["locshuf_" + key] = locality(Vs, W, norm)
            res["tau_e"], res["tau_i"] = time_scales(V, Xc)
            ks = np.isin(e, np.flatnonzero(keep))
            res["aval"] = avalanche_distribution(t[ks], e[ks])
            res["aval_shuf"] = avalanche_distribution(*shuffle_spikes(t[ks], e[ks], shifts))
        out[sel] = res
    return out


def seed_for(asset):
    """A fixed seed per recording, from its path (a standard choice), so results do not depend on order."""
    return zlib.crc32(asset["path"].encode())


def _work(asset):
    return analyse(asset, seed_for(asset))


def analyse_all(assets, workers=3):
    """Run `analyse` on every recording, in `workers` processes (each holds one file at a time)."""
    import os
    from concurrent.futures import ProcessPoolExecutor
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(_work, assets))


def day_index(results):
    """Days since each dish's first recording in the dataset (DIV is not in the files)."""
    first = {}
    for r in results:
        first[r["dish"]] = min(first.get(r["dish"], r["date"]), r["date"])
    return [(r["date"] - first[r["dish"]]).days for r in results]


def fit_table(results):
    """One row per recording, selection reading (S1, S2) and fit reading (F1, F2).

    Columns: PCA fit b, c on the original and shuffled spectra; for avalanche sizes A1 and A2,
    the fit b, c on the original and shuffled trains; synchrony; locality slopes for M1, M2
    (w_ii = 0 and w_ii = 1) and L1, L2 on the original and shuffled PCs.
    """
    import pandas as pd
    days = day_index(results)
    sizes = np.arange(1, AVALANCHE_MAX + 1, dtype=float)
    rows = []
    for r, day in zip(results, days):
        for sel in ("S1", "S2"):
            Q = r[sel]
            for F in ("F1", "F2"):
                d = dict(dish=r["dish"], date=r["date"], day=day, sel=sel, F=F, n_kept=Q["n_kept"],
                         mean_rate=r["mean_rate"])
                if "ev" not in Q:
                    rows.append(d)
                    continue
                d["n_pc"] = len(Q["ev"])
                _, d["b"], d["c"] = fit_decay(Q["ev"], F)
                _, d["b_shuf"], d["c_shuf"] = fit_decay(Q["ev_shuf"], F)
                for A in ("A1", "A2"):
                    for tag, av in (("", Q["aval"]), ("_shuf", Q["aval_shuf"])):
                        if av is None:
                            continue
                        _, d[f"av{A}_b{tag}"], d[f"av{A}_c{tag}"] = fit_decay(av[A], F, sizes)
                d["sync_corr"], d["sync_frac"] = Q["sync"]
                for key in ("M1", "M2", "M1_self", "M2_self"):
                    for tag in ("loc", "locshuf"):
                        s = locality_slopes(Q[f"{tag}_{key}"])
                        for L in ("L1", "L2"):
                            d[f"{tag}_{key}_{L}"] = s[L]
                rows.append(d)
    return pd.DataFrame(rows)
