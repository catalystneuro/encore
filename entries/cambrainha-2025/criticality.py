"""Loading and measures for Cambrainha et al. (2025) on dandiset 000713.

Cambrainha, Castro, de Vasconcelos, Carelli & Copelli (2025), "Criticality at Work: Scaling in
the Mouse Cortex Enhances Performance", PRX Life, doi:10.1103/w49n-2vz8. Claims in
claims/cambrainha-2025.yaml; the codes M1 to M8 and O1 to O11 below refer to the method notes
at the top of that file.

Dandiset 000713 (Allen Institute, Visual Behavior Neuropixels) holds one NWB file per session
(153 sessions, 81 mice) with the sorted units of all probes (`units`, with the peak channel of
each unit and the channel's brain structure in `electrodes/location`), the stimulus
presentations by block (`intervals/*_presentations`, column `stimulus_block`) and the task
trials (`intervals/trials`). LFP is in separate probe files, which are not read. Files are
streamed from the archive at the pinned version with remfile and h5py (pynwb is slow to open
these files over the network and adds nothing here); nothing is written to disk. Only the
spike times of V1 (VISp) units are read.

Where the parameters come from:

- `BIN_S` 50 ms, `WIN_S` 30 s, `CV_MAX` 5 (M1, Appendix 1); `NCUT_DIV` 16, the kurtosis at
  Ncutoff = N/16 (M3, Appendix 3); `KAPPA = <psi^4>/<psi^2>^2` (Appendix 3).
- Unit sets (O1). `all`: every unit whose peak channel is in VISp (the claims file's main
  reading). `good`: units with `quality == "good"`. `default`: the quality filters the Allen
  documentation gives as defaults (`isi_violations < 0.5`, `amplitude_cutoff < 0.1`,
  `presence_ratio > 0.95`).
- Phases (O4). Active is stimulus block 0 (natural images with `active` true); passive is block
  5. NNI (a) runs from the end of block 0 to the start of block 5 (gray screen, Gabors, gray
  screen, flashes); NNI (b) is the Gabor block and the flash block, each tiled on its own.
  Windows tile a phase from its start without overlap and the last partial window is dropped
  (a standard choice, O4).
- Units with no spike in a window are left out of that window's analysis (a standard choice:
  their binned activity has no variance, so they cannot be normalised in Eq. 5 nor correlated
  in Eq. 6). The number left out is kept per window.
- Surrogate (M2, Appendix 2): within each window and unit, the intervals between the window's
  start, the unit's spikes and the window's end are permuted (a standard implementation of
  "shuffling the interspike intervals ... within each time window"; it keeps the spike count
  and keeps every spike inside the window).
- Kurtosis pooling (O3): (a) all psi_i(t) pooled; (b) the mean over units of each unit's
  kurtosis. Ncutoff = floor(N/16) (O3).
- CV (O2): (a) the population count per bin; (b) the mean over units of each unit's CV;
  (c) all unit-bin counts pooled.
- Real-space coarse graining (M7, Appendix 4; O9): Pearson correlation between binned counts,
  recomputed among clusters at each step; pairs formed greedily from the most correlated pair
  down; the cluster left over when the count is odd is dropped. M2 is the variance of the
  cluster sums averaged over clusters (Eq. 7). P_silence (O9): (a) F = -log of the mean over
  clusters of each cluster's fraction of silent bins; (b) the mean over clusters of -log of that
  fraction. tau_c is where the cluster-averaged autocorrelation reaches 1/e, by linear
  interpolation between 50-ms lags (O9), searched up to `MAX_LAG` lags. Spectra (Eq. 9): for
  each cluster, the eigenvalues of the covariance of its K original units, averaged over the
  clusters of that size.
- Fits (O9) are least squares of log quantities on log K. K range (a) from K = 1 to the largest
  K with at least two clusters; (b) from K = 1 to N/16. F is fitted only where it is finite
  (where P_silence > 0), with at least three sizes (a standard choice: -log 0 cannot be
  fitted). mu (a) is one fit of log lambda on log(rank/K) pooled over all K >= 16; (b) the
  spectrum at K = 64, ranks 1 to 64. Windows with r^2 < 0.85 lose their mu (Appendix 4c).
  Variants of mu asked for by the verifier, not readings of O9: (c) as (a) and (d) as (b), over
  ranks 1 to K/2 only, leaving out the noise floor of the spectrum.
- Correlation-matrix variant (asked for by the verifier): the kurtosis of M3 with each unit's
  counts z-scored before Eq. 2 (`kappa_z`, real windows and the claim-seed surrogate).
"""

from __future__ import annotations

import h5py
import numpy as np
import remfile

DANDISET_ID = "000713"
DANDISET_VERSION = "0.240702.1725"

BIN_S = 0.05
WIN_S = 30.0
CV_MAX = 5.0
NCUT_DIV = 16
MIN_UNITS = 128
MU_R2_MIN = 0.85
MAX_LAG = 40           # 2 s of lags for tau_c; a standard search limit

ACTIVE_BLOCK, PASSIVE_BLOCK = 0, 5


# ----------------------------------------------------------------------------- archive

def session_assets():
    """The session files (not the probe LFP files) at the pinned version, sorted by path."""
    from dandi.dandiapi import DandiAPIClient
    client = DandiAPIClient()
    ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
    out = []
    for a in ds.get_assets():
        p = a.path
        if p.endswith(".nwb") and "_probe-" not in p and not p.endswith("_image.nwb"):
            out.append(dict(path=p, asset_id=a.identifier, size=a.size))
    return sorted(out, key=lambda d: d["path"])


def asset_url(asset_id):
    import requests
    r = requests.head(f"https://api.dandiarchive.org/api/assets/{asset_id}/download/",
                      allow_redirects=False, timeout=60)
    return r.headers["Location"]


def open_nwb(asset_id):
    return h5py.File(remfile.File(asset_url(asset_id)), "r")


def _str(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def unit_table(f):
    """Per unit: structure of the peak channel, quality label and the default-filter flag."""
    u = f["units"]
    e = f["general/extracellular_ephys/electrodes"]
    eid = e["id"][:]
    loc = dict(zip(eid, e["location"][:].astype(str)))
    valid = dict(zip(eid, e["valid_data"][:]))
    pc = u["peak_channel_id"][:]
    t = dict(
        location=np.array([loc[c] for c in pc]),
        valid_channel=np.array([bool(valid[c]) for c in pc]),
        quality=u["quality"][:].astype(str),
        isi_violations=u["isi_violations"][:],
        amplitude_cutoff=u["amplitude_cutoff"][:],
        presence_ratio=u["presence_ratio"][:],
        firing_rate=u["firing_rate"][:],
        spike_index=u["spike_times_index"][:].astype(np.int64),
    )
    t["default"] = ((t["isi_violations"] < 0.5) & (t["amplitude_cutoff"] < 0.1)
                    & (t["presence_ratio"] > 0.95))
    return t


def survey(asset):
    """Counts of V1 units per reading of O1, read from metadata only."""
    with open_nwb(asset["asset_id"]) as f:
        t = unit_table(f)
        v = t["location"] == "VISp"
        tr = f["intervals/trials"]
        return dict(
            path=asset["path"], subject=_str(f["general/subject/subject_id"][()]),
            session=_str(f["identifier"][()]), session_type=_str(f["session_description"][()]),
            n_units=len(v), visp_all=int(v.sum()), visp_good=int((v & (t["quality"] == "good")).sum()),
            visp_default=int((v & t["default"]).sum()),
            visp_valid=int((v & t["valid_channel"]).sum()),
            visp_good_valid=int((v & t["valid_channel"] & (t["quality"] == "good")).sum()),
            visp_spikes=int(np.diff(np.r_[0, t["spike_index"]])[v].sum()),
            total_spikes=int(t["spike_index"][-1]),
            n_trials=len(tr["start_time"]),
            locations=sorted(set(t["location"])),
        )


def load_session(asset):
    """V1 spike times, unit flags, phase boundaries, trials and flash onsets of one session."""
    with open_nwb(asset["asset_id"]) as f:
        t = unit_table(f)
        v = np.where(t["location"] == "VISp")[0]
        idx = t["spike_index"]
        starts = np.r_[0, idx][v]
        ends = idx[v]
        lo, hi = int(starts.min()), int(ends.max())
        st = f["units/spike_times"][lo:hi]
        spikes = [st[s - lo:e - lo] for s, e in zip(starts, ends)]
        blocks = {}
        flashes = None
        for name in f["intervals"]:
            g = f["intervals"][name]
            if "stimulus_block" not in g:
                continue
            b = g["stimulus_block"][:]
            s0, s1 = g["start_time"][:], g["stop_time"][:]
            for bb in np.unique(b):
                i = b == bb
                blocks[int(bb)] = (name, float(s0[i].min()), float(s1[i].max()), int(i.sum()))
            if name.startswith("Natural_Images"):
                act = (b == ACTIVE_BLOCK)
                om = g["omitted"][:].astype(float)
                flashes = dict(onset=s0[act], omitted=om[act] > 0)
        tr = f["intervals/trials"]
        trials = {k: tr[k][:] for k in ["start_time", "stop_time", "go", "catch", "aborted",
                                         "auto_rewarded", "hit", "miss",
                                         "change_time_no_display_delay"]}
        meta = dict(path=asset["path"], subject=_str(f["general/subject/subject_id"][()]),
                    session=_str(f["identifier"][()]))
    units = dict(good=t["quality"][v] == "good", default=t["default"][v])
    return dict(meta=meta, spikes=spikes, units=units, blocks=blocks, trials=trials,
                flashes=flashes)


def phase_spans(blocks):
    """Phase name -> list of (start, stop) spans to tile, following O4."""
    a, p = blocks[ACTIVE_BLOCK], blocks[PASSIVE_BLOCK]
    gab = [v for k, v in blocks.items() if v[0].startswith("gabor")]
    fla = [v for k, v in blocks.items() if v[0].startswith("flash")]
    return {
        "active": [(a[1], a[2])],
        "passive": [(p[1], p[2])],
        "nni_a": [(a[2], p[1])],
        "nni_b": [(g[1], g[2]) for g in gab] + [(x[1], x[2]) for x in fla],
    }


def tile(spans, win_s):
    out = []
    for s0, s1 in spans:
        n = int(np.floor((s1 - s0) / win_s + 1e-9))
        out += [(s0 + i * win_s, s0 + (i + 1) * win_s) for i in range(n)]
    return out


# ----------------------------------------------------------------------------- measures

def bin_window(spikes, t0, nbins):
    """Counts (units x bins) of 50-ms bins from t0."""
    t1 = t0 + nbins * BIN_S
    X = np.zeros((len(spikes), nbins), dtype=np.float64)
    for i, s in enumerate(spikes):
        a, b = np.searchsorted(s, [t0, t1])
        if b > a:
            k = ((s[a:b] - t0) / BIN_S).astype(np.int64)
            np.add.at(X[i], np.clip(k, 0, nbins - 1), 1)
    return X


def window_spikes(spikes, t0, t1):
    out = []
    for s in spikes:
        a, b = np.searchsorted(s, [t0, t1])
        out.append(s[a:b])
    return out


def isi_shuffle(wspikes, t0, t1, rng):
    """Surrogate (M2): permute the intervals between t0, the spikes and t1, per unit."""
    out = []
    for s in wspikes:
        if len(s) == 0:
            out.append(s)
            continue
        iv = np.diff(np.r_[t0, s, t1])
        iv = rng.permutation(iv)
        out.append(t0 + np.cumsum(iv[:-1]))
    return out


def bin_spikes(wspikes, t0, nbins):
    X = np.zeros((len(wspikes), nbins))
    for i, s in enumerate(wspikes):
        if len(s):
            k = np.clip(((s - t0) / BIN_S).astype(np.int64), 0, nbins - 1)
            X[i] = np.bincount(k, minlength=nbins)
    return X


def cv_readings(X):
    """CV of a window (O2): (a) population count per bin, (b) mean unit CV, (c) pooled."""
    pop = X.sum(0)
    cva = pop.std() / pop.mean() if pop.mean() > 0 else np.inf
    m = X.mean(1)
    ok = m > 0
    cvb = np.mean(X[ok].std(1) / m[ok]) if ok.any() else np.inf
    cvc = X.std() / X.mean() if X.mean() > 0 else np.inf
    return cva, cvb, cvc


def _kurt(psi):
    """Pooled (a) and mean-over-units (b) kurtosis of rows of psi (zero mean, unit variance)."""
    p2 = psi ** 2
    ka = np.mean(p2 ** 2) / np.mean(p2) ** 2
    kb = np.mean(np.mean(p2 ** 2, 1) / np.mean(p2, 1) ** 2)
    return ka, kb


def momentum_kurtosis(X, zscore=False):
    """Kurtosis after momentum-space coarse graining (M3, Eqs. 2 to 5), and before (kappa_0).

    X holds the binned counts of the units active in the window. Returns
    (kappa_a, kappa_b, kappa0_a, kappa0_b) under the two poolings of O3. With `zscore`, each
    unit's counts are z-scored before Eq. 2, so that C is the correlation matrix (a variant the
    verifier asked for, as in some momentum-space analyses; Eq. 2 prints the covariance).
    """
    N = X.shape[0]
    D = X - X.mean(1, keepdims=True)
    if zscore:
        D = D / D.std(1, keepdims=True)
    C = D @ D.T / X.shape[1]
    w, U = np.linalg.eigh(C)
    k = max(N // NCUT_DIV, 1)
    Uk = U[:, -k:]                      # top Ncutoff eigenvectors
    psi = Uk @ (Uk.T @ D)               # Eq. 5, sum over j of P_ij (phi_j - <phi_j>)
    sd = psi.std(1, keepdims=True)
    good = sd[:, 0] > 1e-12
    psi = psi[good] / sd[good]
    ka, kb = _kurt(psi)
    z0 = D / D.std(1, keepdims=True)
    k0a, k0b = _kurt(z0)
    return ka, kb, k0a, k0b


def _greedy_pairs(R):
    """Pairs of clusters from the most correlated down (Eq. 6); the odd one out is dropped."""
    n = R.shape[0]
    iu, ju = np.triu_indices(n, 1)
    r = R[iu, ju]
    r = np.where(np.isfinite(r), r, -np.inf)
    order = np.argsort(-r, kind="stable")
    used = np.zeros(n, bool)
    pairs = []
    target = n // 2
    for o in order:
        i, j = iu[o], ju[o]
        if not used[i] and not used[j]:
            used[i] = used[j] = True
            pairs.append((i, j))
            if len(pairs) == target:
                break
    return pairs


def _autocorr_tau(Y):
    """tau_c (s): where the cluster-averaged autocorrelation reaches 1/e (O9)."""
    Yc = Y - Y.mean(1, keepdims=True)
    var = (Yc ** 2).mean(1)
    ok = var > 0
    Yc, var = Yc[ok], var[ok]
    T = Y.shape[1]
    c = [1.0]
    for lag in range(1, MAX_LAG + 1):
        c.append(np.mean((Yc[:, :-lag] * Yc[:, lag:]).sum(1) / (T - lag) / var))
        if c[-1] < 1 / np.e:
            c0, c1 = c[-2], c[-1]
            return (lag - 1 + (c0 - 1 / np.e) / (c0 - c1)) * BIN_S
    return np.nan


def real_space(X):
    """Real-space coarse graining (M7, Eqs. 6 to 10) of one window's counts X (units x bins).

    Returns, per cluster size K = 1, 2, 4, ...: number of clusters, M2, mean silent fraction,
    mean -log silent fraction (inf when a cluster is never silent), tau_c, and for K >= 16 the
    mean within-cluster covariance spectrum (descending).
    """
    members = [[i] for i in range(X.shape[0])]
    Y = X.copy()
    out = dict(K=[], n=[], M2=[], Psil=[], Fb=[], tau=[], spectra={})
    K = 1
    while True:
        psil = (Y == 0).mean(1)
        with np.errstate(divide="ignore"):
            fb = np.mean(-np.log(psil))
        out["K"].append(K)
        out["n"].append(Y.shape[0])
        out["M2"].append(Y.var(1).mean())
        out["Psil"].append(psil.mean())
        out["Fb"].append(fb)
        out["tau"].append(_autocorr_tau(Y))
        if K >= 16:
            sp = []
            for m in members:
                Z = X[m]
                Z = Z - Z.mean(1, keepdims=True)
                ev = np.linalg.eigvalsh(Z @ Z.T / X.shape[1])[::-1]
                sp.append(ev)
            out["spectra"][K] = np.mean(sp, 0)
        if Y.shape[0] < 2:
            break
        sd = Y.std(1)
        Yc = Y - Y.mean(1, keepdims=True)
        with np.errstate(invalid="ignore", divide="ignore"):
            Z = Yc / sd[:, None]
            R = Z @ Z.T / Y.shape[1]
        pairs = _greedy_pairs(R)
        if not pairs:
            break
        Y = np.array([Y[i] + Y[j] for i, j in pairs])
        members = [members[i] + members[j] for i, j in pairs]
        K *= 2
    for k in ["K", "n", "M2", "Psil", "Fb", "tau"]:
        out[k] = np.array(out[k], dtype=float)
    return out


def _fit(x, y):
    ok = np.isfinite(x) & np.isfinite(y)
    if ok.sum() < 3:
        return np.nan, np.nan
    p = np.polyfit(x[ok], y[ok], 1)
    yy = np.polyval(p, x[ok])
    ss = np.sum((y[ok] - y[ok].mean()) ** 2)
    r2 = 1 - np.sum((y[ok] - yy) ** 2) / ss if ss > 0 else np.nan
    return p[0], r2


def fit_exponents(rs, N, krange="a", fsil="a", mu="a"):
    """alpha, beta, mu, mu's r^2 and z from one set of real-space quantities (O9 readings).

    `rs` is the output of `real_space` (or its average over windows). `N` is the number of
    units, which sets the K range of reading (b).
    """
    K = rs["K"]
    if krange == "a":
        sel = (rs["n"] >= 2)
    else:
        sel = K <= N / NCUT_DIV
    lk = np.log(K[sel])
    alpha, _ = _fit(lk, np.log(rs["M2"][sel]))
    with np.errstate(divide="ignore", invalid="ignore"):
        if fsil == "a":
            F = -np.log(rs["Psil"][sel])
        else:
            F = rs["Fb"][sel]
        beta, _ = _fit(lk, np.log(F))
    z, _ = _fit(lk, np.log(rs["tau"][sel]))
    m, r2 = np.nan, np.nan
    if mu == "a":
        xs, ys = [], []
        for k, sp in rs["spectra"].items():
            if k >= 16:
                rank = np.arange(1, len(sp) + 1)
                pos = sp > 0
                xs.append(np.log(rank[pos] / k))
                ys.append(np.log(sp[pos]))
        if xs:
            s, r2 = _fit(np.concatenate(xs), np.concatenate(ys))
            m = -s
    elif mu == "c":
        # variant asked for by the verifier: as (a), ranks 1 to K/2 only (upper half)
        xs, ys = [], []
        for k, sp in rs["spectra"].items():
            if k >= 16:
                rank = np.arange(1, len(sp) + 1)
                pos = (sp > 0) & (rank <= k // 2)
                xs.append(np.log(rank[pos] / k))
                ys.append(np.log(sp[pos]))
        if xs:
            s, r2 = _fit(np.concatenate(xs), np.concatenate(ys))
            m = -s
    else:
        # (b), and variant (d): as (b), ranks 1 to 32 only
        sp = rs["spectra"].get(64)
        if sp is not None:
            rank = np.arange(1, len(sp) + 1)
            pos = (sp > 0) & ((rank <= 32) if mu == "d" else True)
            s, r2 = _fit(np.log(rank[pos] / 64), np.log(sp[pos]))
            m = -s
    return dict(alpha=alpha, beta=beta, mu=m, mu_r2=r2, z=z)


EXP_READINGS = [(kr, fs, mu) for kr in "ab" for fs in "ab" for mu in "ab"]


def average_rs(rss):
    """O10 (b): the real-space quantities averaged over windows, per K (and spectrum)."""
    Ks = sorted(set(k for r in rss for k in r["K"]))
    out = dict(K=[], n=[], M2=[], Psil=[], Fb=[], tau=[], spectra={})
    for k in Ks:
        vals = {q: [] for q in ["n", "M2", "Psil", "Fb", "tau"]}
        sps = []
        for r in rss:
            i = np.where(r["K"] == k)[0]
            if len(i):
                for q in vals:
                    vals[q].append(r[q][i[0]])
                if k in r["spectra"]:
                    sps.append(r["spectra"][k])
        out["K"].append(k)
        out["n"].append(np.min(vals["n"]))
        for q in ["M2", "Psil", "tau"]:
            out[q].append(np.nanmean(vals[q]))
        fb = np.array(vals["Fb"])
        out["Fb"].append(np.mean(fb) if np.all(np.isfinite(fb)) else np.inf)
        if sps:
            L = min(len(s) for s in sps)
            out["spectra"][k] = np.mean([s[:L] for s in sps], 0)
    for q in ["K", "n", "M2", "Psil", "Fb", "tau"]:
        out[q] = np.array(out[q], dtype=float)
    return out


# ----------------------------------------------------------------------------- per session

def analyse_window(spikes, t0, t1, rng_list, do_real_space=True, surr_real_space=True):
    """Everything computed on one window: counts, CVs, kurtosis, surrogates, real space."""
    nb = int(round((t1 - t0) / BIN_S))
    ws = window_spikes(spikes, t0, t1)
    X = bin_spikes(ws, t0, nb)
    active = X.sum(1) > 0
    Xa = X[active]
    rec = dict(t0=t0, t1=t1, n_units=int(len(spikes)), N=int(active.sum()),
               n_silent=int((~active).sum()), rate=float(X.mean()),
               spikes=int(X.sum()))
    rec["cv_a"], rec["cv_b"], rec["cv_c"] = cv_readings(X)
    rec["kappa_a"], rec["kappa_b"], rec["kappa0_a"], rec["kappa0_b"] = momentum_kurtosis(Xa)
    if rng_list:
        rec["kappa_z"] = momentum_kurtosis(Xa, zscore=True)[0]
    if do_real_space:
        rec["rs"] = real_space(Xa)
    wa = [s for s, a in zip(ws, active) if a]
    for si, rng in enumerate(rng_list):
        S = bin_spikes(isi_shuffle(wa, t0, t1, rng), t0, nb)
        S = S[S.sum(1) > 0]
        ka, kb, _, _ = momentum_kurtosis(S)
        rec[f"surr{si}_kappa_a"], rec[f"surr{si}_kappa_b"] = ka, kb
        if si == 0:
            rec["surr0_kappa_z"] = momentum_kurtosis(S, zscore=True)[0]
        if si == 0 and do_real_space and surr_real_space:
            rec["surr_rs"] = real_space(S)
    return rec


def flash_contrast(spikes, flashes):
    """Clock check: V1 population spikes 30 to 130 ms after image onsets minus the 100 ms
    before, for shown images and for omitted flashes of the active block."""
    allsp = np.sort(np.concatenate(spikes))
    on = flashes["onset"]

    def cnt(a, b):
        return np.searchsorted(allsp, on + b) - np.searchsorted(allsp, on + a)
    resp = cnt(0.03, 0.13) - cnt(-0.10, 0.0)
    shown, om = resp[~flashes["omitted"]], resp[flashes["omitted"]]
    return dict(shown_mean=float(shown.mean()), shown_sd=float(shown.std()),
                n_shown=int(len(shown)), omitted_mean=float(om.mean()) if len(om) else np.nan,
                omitted_sd=float(om.std()) if len(om) else np.nan, n_omitted=int(len(om)))


def process_session(asset, surr_seeds, strict_seeds, strict_sets=()):
    """All per-window results of one session.

    `surr_seeds`: SeedSequences for the surrogate of each window (the first is the claim's
    seed, the others the four seed variants). `strict_seeds`: the same for the surrogate of
    the strict-unit analysis (figs2-strict-units). `strict_sets`: unit sets
    ("good", "default") for which the active phase is also analysed.
    """
    d = load_session(asset)
    spikes = d["spikes"]
    spans = phase_spans(d["blocks"])
    rows = []
    rngs = [np.random.default_rng(s) for s in surr_seeds]
    for phase in ["active", "passive", "nni_a", "nni_b"]:
        for wi, (t0, t1) in enumerate(tile(spans[phase], WIN_S)):
            r = analyse_window(spikes, t0, t1, rngs)
            r.update(phase=phase, win=wi, length=WIN_S, units="all")
            rows.append(r)
    for L in (10.0, 60.0):
        for wi, (t0, t1) in enumerate(tile(spans["active"], L)):
            r = analyse_window(spikes, t0, t1, [], do_real_space=False)
            r.update(phase="active", win=wi, length=L, units="all")
            rows.append(r)
    srngs = [np.random.default_rng(s) for s in strict_seeds]
    for uset in strict_sets:
        sub = [s for s, k in zip(spikes, d["units"][uset]) if k]
        for wi, (t0, t1) in enumerate(tile(spans["active"], WIN_S)):
            r = analyse_window(sub, t0, t1, srngs, do_real_space=False)
            r.update(phase="active", win=wi, length=WIN_S, units=uset)
            rows.append(r)
    for r in rows:
        r.update(d["meta"])
    sorted_ok = all(np.all(np.diff(s) >= 0) for s in spikes)
    return dict(meta=d["meta"], windows=rows, trials=d["trials"], blocks=d["blocks"],
                spans=spans, clock=flash_contrast(spikes, d["flashes"]),
                n_units=len(spikes), n_good=int(d["units"]["good"].sum()),
                n_default=int(d["units"]["default"].sum()), spikes_sorted=sorted_ok,
                rates=np.array([len(s) for s in spikes]))


def _work(args):
    asset, seeds, strict_seeds, strict_sets = args
    for attempt in range(3):
        try:
            return process_session(asset, seeds, strict_seeds, strict_sets)
        except Exception as e:  # network errors: retry, then report
            err = repr(e)
    return dict(meta=dict(path=asset["path"]), error=err)


def run_sessions(assets, surr_seed, strict_seed, strict_sets_of, workers=4, n_variants=5):
    """Process sessions in parallel. Seeds: each session's generators are children
    (SeedSequence.spawn) of the claim's seed, and of the claim's seed plus 1000, 2000, 3000 and
    4000 for the seed variants, in the order of `assets`."""
    from concurrent.futures import ProcessPoolExecutor
    n = len(assets)
    kids = [np.random.SeedSequence(surr_seed + 1000 * v).spawn(n) for v in range(n_variants)]
    skids = [np.random.SeedSequence(strict_seed + 1000 * v).spawn(n) for v in range(n_variants)]
    jobs = [(a, [kids[v][i] for v in range(n_variants)], [skids[v][i] for v in range(n_variants)],
             strict_sets_of(a))
            for i, a in enumerate(assets)]
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(_work, jobs))


# ----------------------------------------------------------------------------- analysis

def window_table(results):
    """All windows of all sessions as a table (the real-space results stay in the records)."""
    import pandas as pd
    rows = []
    for r in results:
        for w in r["windows"]:
            rows.append({k: v for k, v in w.items() if k not in ("rs", "surr_rs")})
    return pd.DataFrame(rows)


def session_trials(r, autoreward="a", anchor="change"):
    """Go trials with an outcome (O5): change trials that are hits or misses; catch and aborted
    trials left out. Auto-rewarded trials (a) left out or (b) kept as hits. Each trial is placed
    at its change time (main) or its start time (variant). Returns (times, hit) arrays."""
    t = r["trials"]
    go = t["go"].astype(bool) & ~t["aborted"].astype(bool) & (t["hit"].astype(bool)
                                                             | t["miss"].astype(bool))
    auto = t["auto_rewarded"].astype(bool) & ~t["aborted"].astype(bool)
    keep = go | auto if autoreward == "b" else go
    times = t["change_time_no_display_delay"] if anchor == "change" else t["start_time"]
    hit = t["hit"].astype(bool) | (auto if autoreward == "b" else False)
    return np.asarray(times)[keep], np.asarray(hit)[keep].astype(int)


def session_trials_counted(r, reading):
    """Trial-count variants for the trial density of Appendix 5 ("three to five trials" per
    30-s window), asked for by the verifier; not readings of O5. "go": O5 (a). "go+aborted":
    also aborted trials, as failures. "all": every trial (go, catch, aborted, auto-rewarded),
    a hit counting as success. Go trials are placed at their change time, the others at their
    start time. Returns (times, hit) arrays."""
    t = r["trials"]
    ab = t["aborted"].astype(bool)
    go = t["go"].astype(bool) & ~ab & (t["hit"].astype(bool) | t["miss"].astype(bool))
    hit = t["hit"].astype(bool)
    times = np.where(go, t["change_time_no_display_delay"], t["start_time"])
    if reading == "go":
        keep = go
    elif reading == "go+aborted":
        keep = go | ab
    else:
        keep = np.ones(len(hit), bool)
    return np.asarray(times)[keep], hit[keep].astype(int)


def trials_per_window(t0s, t1s, times, hit):
    """Hits and trials per window [t0, t1); trials outside every window are dropped."""
    h = np.zeros(len(t0s), int)
    n = np.zeros(len(t0s), int)
    order = np.argsort(t0s)
    s0, s1 = np.asarray(t0s)[order], np.asarray(t1s)[order]
    for tt, hh in zip(times, hit):
        if not np.isfinite(tt):
            continue
        i = np.searchsorted(s0, tt, side="right") - 1
        if i >= 0 and tt < s1[i]:
            n[order[i]] += 1
            h[order[i]] += hh
    return h, n


def hit_curves(kappa, h, n, grid):
    """Eqs. 11 and 12: pooled hit rate over windows above and below each threshold."""
    o = np.argsort(kappa)
    k, hh, nn = kappa[o], h[o].astype(float), n[o].astype(float)
    ch, cn = np.r_[0, np.cumsum(hh)], np.r_[0, np.cumsum(nn)]
    cut = np.searchsorted(k, grid, side="right")     # windows <= th are below
    hb, nb = ch[cut], cn[cut]
    ha, na = ch[-1] - hb, cn[-1] - nb
    with np.errstate(invalid="ignore", divide="ignore"):
        hra, hrb = ha / na, hb / nb
    return hra, hrb, na, nb


def boot_curves(kappa, h, n, grid, rng, B=10_000, chunk=1000, reading="a"):
    """Bootstrap SEs over windows (Appendix 5) of the scaling and no-scaling hit rates and of
    the relative gain (Eq. 13; O8 (c)). Resamples use Poisson(1) weights per window (the
    Poisson bootstrap, which draws each subset with replacement at random size; a standard
    approximation that lets one draw serve every threshold). Reading (a): the pooled hit rate
    of each resample; (b): the mean of the resampled windows' own hit rates (windows with
    trials only)."""
    o = np.argsort(kappa)
    k, hh, nn = kappa[o], h[o].astype(float), n[o].astype(float)
    if reading == "b":
        m = nn > 0
        k, hh, nn = k[m], hh[m] / nn[m], np.ones(m.sum())
    cut = np.searchsorted(k, grid, side="right")
    out_a, out_b, out_g = [], [], []
    for start in range(0, B, chunk):
        b = min(chunk, B - start)
        Wt = rng.poisson(1.0, size=(b, len(k))).astype(np.float32)
        ch = np.concatenate([np.zeros((b, 1), np.float32), np.cumsum(Wt * hh, 1)], 1)
        cn = np.concatenate([np.zeros((b, 1), np.float32), np.cumsum(Wt * nn, 1)], 1)
        hb, nb = ch[:, cut], cn[:, cut]
        ha, na = ch[:, -1:] - hb, cn[:, -1:] - nb
        with np.errstate(invalid="ignore", divide="ignore"):
            ra, rb = ha / na, hb / nb
            out_a.append(ra)
            out_b.append(rb)
            out_g.append((ra - rb) / rb)
    A, Bn, G = (np.concatenate(x, 0) for x in (out_a, out_b, out_g))
    with np.errstate(invalid="ignore"):
        return np.nanstd(A, 0), np.nanstd(Bn, 0), np.nanstd(G, 0)


def swap_shuffle(hit, rng, reps):
    """Appendix 6: for each trial, another trial of the session is drawn at random and their
    outcomes are swapped; `reps` independent repetitions (rows)."""
    n = len(hit)
    H = np.tile(hit, (reps, 1))
    rows = np.arange(reps)
    for i in range(n):
        j = rng.integers(0, n, size=reps)
        a, b = H[rows, i].copy(), H[rows, j].copy()
        H[rows, i], H[rows, j] = b, a
    return H


def session_exponents(rss, Ns, reading, agg="a"):
    """Session exponents (O10): (a) the mean over windows of per-window fits, mu only where
    r^2 >= 0.85; (b) one fit to the window quantities averaged over the session's windows."""
    if not rss:
        return dict(alpha=np.nan, beta=np.nan, mu=np.nan, z=np.nan, n_mu=0)
    if agg == "a":
        fs = [fit_exponents(r, N, *reading) for r, N in zip(rss, Ns)]
        mu = [f["mu"] for f in fs if np.isfinite(f["mu_r2"]) and f["mu_r2"] >= MU_R2_MIN]
        return dict(alpha=np.nanmean([f["alpha"] for f in fs]),
                    beta=np.nanmean([f["beta"] for f in fs]),
                    z=np.nanmean([f["z"] for f in fs]),
                    mu=np.mean(mu) if mu else np.nan, n_mu=len(mu))
    f = fit_exponents(average_rs(rss), int(np.median(Ns)), *reading)
    ok = np.isfinite(f["mu_r2"]) and f["mu_r2"] >= MU_R2_MIN
    return dict(alpha=f["alpha"], beta=f["beta"], z=f["z"], mu=f["mu"] if ok else np.nan,
                n_mu=int(ok))


def window_fits(rs, N):
    """Per-window exponents under every reading of O9, fitting each quantity once:
    alpha_<K range>, z_<K range>, beta_<K range><P_silence>, mu_<mu reading>, mu_r2_<mu reading>."""
    out = {}
    for kr in "ab":
        for fs in "ab":
            f = fit_exponents(rs, N, kr, fs, "a" if fs == "a" else "b")
            out[f"beta_{kr}{fs}"] = f["beta"]
            if fs == "a":
                out[f"alpha_{kr}"], out[f"z_{kr}"] = f["alpha"], f["z"]
                if kr == "a":
                    out["mu_a"], out["mu_r2_a"] = f["mu"], f["mu_r2"]
            elif kr == "a":
                out["mu_b"], out["mu_r2_b"] = f["mu"], f["mu_r2"]
    for v in "cd":
        f = fit_exponents(rs, N, "a", "a", v)
        out[f"mu_{v}"], out[f"mu_r2_{v}"] = f["mu"], f["mu_r2"]
    return out


def reading_columns(kr, fs, mu):
    return dict(alpha=f"alpha_{kr}", beta=f"beta_{kr}{fs}", z=f"z_{kr}", mu=f"mu_{mu}",
                mu_r2=f"mu_r2_{mu}")
