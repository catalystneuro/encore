"""Loading and measures for the attempt on Clark, Abbott & Sompolinsky (2026) on DANDI:000939.

Every procedure here follows the paper's code, github.com/davidclark1/symmetries-continuous-attractors
at commit 245726fa78457e10cdcf17e6be36fba1dec98061 (the "ring" package), as the claims file
(claims/clark-2026.yaml) cites it. Each function names the function of the paper's code it
repeats. The paper's code imports torch; the parts used here are rewritten in numpy so that the
entry needs no GPU stack. Where a parameter comes from somewhere else it is said so.

Data are streamed from the DANDI archive (remfile and h5py); nothing is downloaded to disk.
"""
import hashlib
import io
import zlib

import h5py
import numpy as np
import remfile
import requests
from scipy.ndimage import gaussian_filter1d

DANDISET = "000939"
# The version the paper cites (claims file, opening comment).
VERSION = "0.240528.1542"
API = "https://api.dandiarchive.org/api"
PAPER_KEY = "clark-2026"

# Paper's code, ring/data.py: DATA_DT, process_file defaults.
DATA_DT = 0.01
N_THETA = 100
SIGMA_VALS = np.logspace(-1, 2, 100)
K_FOLDS = 4

# Zenodo record of the paper's cached results (claims file, tuning-curves-match-cache).
ZENODO_TAR = "https://zenodo.org/api/records/21827768/files/symmetries_caches_v1.tar/content"
ZENODO_MD5 = "https://zenodo.org/api/records/21827768/files/CHECKSUMS.md5/content"


def seed(claim_id, k=0):
    """Seed of a claim's k-th generator (protocol, "Take every random seed from the claim")."""
    return zlib.crc32(f"{PAPER_KEY}/{claim_id}".encode()) + k


def list_assets(version=VERSION):
    """All assets of the dandiset at the pinned version, as dicts (path, size, asset_id)."""
    url = f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=200"
    out = []
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        d = r.json()
        out += d["results"]
        url = d["next"]
    return out


def asset_s3_url(asset_id, version=VERSION):
    r = requests.get(f"{API}/dandisets/{DANDISET}/versions/{version}/assets/{asset_id}/", timeout=60)
    r.raise_for_status()
    return [u for u in r.json()["contentUrl"] if "amazonaws" in u][0]


def session_order(assets):
    """Sessions in the order of the paper's code (ring/data.py, get_session_info).

    The code takes one file per subject folder, the +ogen.nwb file where one exists, and
    sorts by the full path, which sorts by subject. Session index = position in this list.
    """
    by_subj = {}
    for a in assets:
        if not a["path"].endswith(".nwb"):
            continue
        subj = a["path"].split("/")[0].split("-")[-1]
        ogen = a["path"].endswith("+ogen.nwb")
        if subj not in by_subj or ogen:
            by_subj[subj] = (a["path"], a["asset_id"], ogen)
    return [(p, aid, subj, ogen) for subj, (p, aid, ogen) in sorted(by_subj.items(), key=lambda kv: kv[1][0])]


def _strs(x):
    return [v.decode() if isinstance(v, bytes) else str(v) for v in x]


def load_session(asset_id, hd_only=True, version=VERSION):
    """Read what the analysis needs from one NWB file, by streaming.

    Returns a dict with the epochs table, the head-direction series (data, timestamps), the
    unit labels (is_head_direction, is_excitatory, is_fast_spiking), the unit count, and the
    spike times of the head-direction units only (hd_only) or of all units.
    """
    f = h5py.File(remfile.File(asset_s3_url(asset_id, version)), "r")
    ep = f["intervals/epochs"]
    tags_idx = ep["tags_index"][:]
    tags = _strs(ep["tags"][:])
    starts = np.r_[0, tags_idx[:-1]]
    ep_tags = [",".join(tags[s:e]) for s, e in zip(starts, tags_idx)]
    hd_ss = f["processing/behavior/CompassDirection/head-direction"]
    out = dict(
        epochs=list(zip(ep_tags, ep["start_time"][:], ep["stop_time"][:])),
        hd=hd_ss["data"][:],
        hd_t=hd_ss["timestamps"][:],
        hd_unit=hd_ss["data"].attrs.get("unit"),
        is_hd=f["units/is_head_direction"][:].astype(bool),
        is_exc=f["units/is_excitatory"][:].astype(bool),
        is_fs=f["units/is_fast_spiking"][:].astype(bool),
        subject=f["general/subject/subject_id"][()].decode(),
        session_id=f["general/session_id"][()].decode(),
    )
    idx = f["units/spike_times_index"][:]
    out["n_units"] = len(idx)
    out["unit_ids"] = f["units/id"][:]
    st = f["units/spike_times"]
    first = np.r_[0, idx[:-1]]
    keep = np.where(out["is_hd"])[0] if hd_only else np.arange(len(idx))
    out["spike_units"] = keep
    out["spikes"] = [st[first[i]:idx[i]] for i in keep]
    f.close()
    return out


def epoch_bins(sess, tag="wake_square", N_theta=N_THETA):
    """Head-direction bin index per 10-ms sample in the epoch (ring/data.py, process_file).

    The epoch runs from the head-direction sample nearest the epoch start to the one nearest
    its stop; NaN samples get index -1 (dropped); bins are floor(hd / (2 pi / N_theta)).
    """
    ti_nom, tf_nom = [(s, e) for t, s, e in sess["epochs"] if t == tag][0]
    t_full = sess["hd_t"]
    ti_idx = np.argmin((ti_nom - t_full) ** 2)
    tf_idx = np.argmin((tf_nom - t_full) ** 2)
    ti, tf = t_full[ti_idx], t_full[tf_idx]
    hd = sess["hd"][ti_idx:tf_idx].copy()
    hd[np.isnan(hd)] = -1
    hd_idx = np.floor(hd / (2 * np.pi / N_theta)).astype(int)
    return hd_idx, ti, tf, ti_idx, tf_idx


def alternating_mask(N_bins, K=K_FOLDS):
    """ring/data.py, generate_alternating_mask: 2K contiguous chunks, alternating True/False."""
    chunk, rem = divmod(N_bins, 2 * K)
    mask = np.zeros(N_bins, dtype=bool)
    val, s = True, 0
    for _ in range(2 * K):
        n = chunk + (1 if rem > 0 else 0)
        rem -= 1
        mask[s:s + n] = val
        s += n
        val = not val
    return mask


def spike_counts(spike_times, ti, tf, N_bins):
    """10-ms spike counts from the epoch start (ring/data.py, process_file)."""
    s = spike_times[(spike_times >= ti) & (spike_times < tf)]
    idx = np.floor((s - ti) / DATA_DT).astype(int)
    idx = idx[(idx >= 0) & (idx < N_bins)]
    return np.bincount(idx, minlength=N_bins).astype(float)


def tuning_curves_session(sess, N_theta=N_THETA, sigma_vals=SIGMA_VALS, K=K_FOLDS):
    """Cross-validated tuning curves of the loaded units (ring/data.py, process_file).

    For each partition (the alternating mask and its complement): the occupancy-normalized
    curve, with zero bins set to 1e-3 times its mean (compute_tuning_curve); smoothed with a
    circular Gaussian of each width in sigma_vals; the width kept is the one maximizing the
    Poisson log-likelihood of the other partition's 10-ms counts. The log-likelihood is
    computed from per-angle sums of counts and occupancy, sum_a [S_a log(mu_a) - n_a mu_a],
    which differs from the code's sum of poisson.logpmf only by a term that does not depend
    on the curve (sum of log k!), so the chosen width is the same.

    Returns plain (n, 2, N_theta), opt (n, 2, N_theta), opt_sigma (n, 2), and the bin data.
    """
    hd_idx, ti, tf, _, _ = epoch_bins(sess, N_theta=N_theta)
    N_bins = len(hd_idx)
    m = alternating_mask(N_bins, K)
    valid = hd_idx >= 0
    folds = [m & valid, (~m) & valid]
    occ = [np.bincount(hd_idx[fm], minlength=N_theta).astype(float) for fm in folds]
    n = len(sess["spikes"])
    plain = np.zeros((n, 2, N_theta))
    opt = np.zeros((n, 2, N_theta))
    opt_sig = np.zeros((n, 2))
    # the smoothing operators, one per width, as matrices acting on a curve (mode wrap)
    eye = np.eye(N_theta)
    S = np.stack([gaussian_filter1d(eye, s, axis=0, mode="wrap") for s in sigma_vals])
    for u, st in enumerate(sess["spikes"]):
        counts = spike_counts(st, ti, tf, N_bins)
        sc = [np.bincount(hd_idx[fm], weights=counts[fm], minlength=N_theta) for fm in folds]
        for k in range(2):
            with np.errstate(invalid="ignore", divide="ignore"):
                tc = sc[k] / (occ[k] * DATA_DT)
            tc[tc == 0.0] = tc.mean() * 1e-3
            plain[u, k] = tc
            sm = np.einsum("sij,j->si", S, tc)  # (n_sigma, N_theta)
            mu = sm * DATA_DT
            other = 1 - k
            with np.errstate(divide="ignore"):
                ll = (sc[other][None, :] * np.log(mu)).sum(1) - (occ[other][None, :] * mu).sum(1)
            j = int(np.nanargmax(ll))
            opt[u, k] = sm[j]
            opt_sig[u, k] = sigma_vals[j]
    return plain, opt, opt_sig


def read_zenodo_member(name):
    """Read one member of the Zenodo cache tar by range requests, and check its MD5.

    Returns (bytes, md5 computed, md5 listed in the record's CHECKSUMS.md5).
    """
    import fsspec
    import tarfile

    listed = {}
    for line in requests.get(ZENODO_MD5, timeout=60).text.splitlines():
        if line.strip():
            h, p = line.split()
            listed[p] = h
    with fsspec.open(ZENODO_TAR, block_size=2**20).open() as fh:
        tf = tarfile.open(fileobj=fh, mode="r:")
        for mem in tf:
            if mem.name.lstrip("./") == name:
                fh.seek(mem.offset_data)
                b = fh.read(mem.size)
                break
            if mem.offset_data > 3e9:
                raise KeyError(name)
    return b, hashlib.md5(b).hexdigest(), listed.get(name)


def load_npz_bytes(b):
    return np.load(io.BytesIO(b), allow_pickle=False)


# ---------------------------------------------------------------- tuning-curve statistics
# ring/analysis.py


def circular_center_of_mass(tcs):
    """ring/analysis.py, circular_center_of_mass; Methods equation (14)."""
    theta = np.linspace(0, 2 * np.pi, tcs.shape[1], endpoint=False)
    return np.arctan2((tcs * np.sin(theta)).sum(1), (tcs * np.cos(theta)).sum(1)) % (2 * np.pi)


def center_tuning_curves(tcs):
    """ring/analysis.py, center_tuning_curves: roll so the center of mass falls on bin 0."""
    n = tcs.shape[1]
    shifts = (-(n * circular_center_of_mass(tcs) / (2 * np.pi)).round()).astype(int)
    return np.stack([np.roll(t, s) for t, s in zip(tcs, shifts)])


def find_local_maxima(signal, z_thresh):
    """ring/analysis.py, find_local_maxima; Methods equation (17). Circular."""
    diff = np.concatenate(([signal[0] - signal[-1]], np.diff(signal)))
    sign_change = np.sign(np.roll(diff, -1)) - np.sign(diff)
    maxima = np.where(sign_change == -2)[0]
    return maxima[(signal[maxima] - signal.mean()) / signal.std() > z_thresh]


def peak_counts(tcs, z_thresh):
    return np.array([len(find_local_maxima(t, z_thresh)) for t in tcs])


def peak_count_hist(tcs, z_thresh, max_peaks=6):
    """ring/analysis.py, compute_peak_counts: histogram of 1 to 5 peaks, normalized over those."""
    pc = peak_counts(tcs, z_thresh)
    c = np.array([(pc == i).sum() for i in range(1, max_peaks)], float)
    return c / c.sum()


def get_peak_values(tcs, num_peaks=3):
    """ring/analysis.py, get_peak_values (zthresh 1)."""
    res = np.full((len(tcs), num_peaks), np.nan)
    for i, t in enumerate(tcs):
        v = np.sort(t[find_local_maxima(t, 1)])[::-1][:num_peaks]
        res[i, :len(v)] = v
    return res


def symmetry_scores(tcs):
    """ring/analysis.py, compute_symmetry_scores; Methods equation (15)."""
    out = []
    for x in tcs:
        theta = np.arange(len(x)) * 2 * np.pi / len(x)
        ang = np.mod(np.arctan2(np.average(np.sin(theta), weights=x), np.average(np.cos(theta), weights=x)), 2 * np.pi)
        com = int(np.round(ang * len(x) / (2 * np.pi)))
        rev = np.roll(x, -2 * com - 1)[::-1]
        out.append(np.corrcoef(x, rev)[0, 1])
    return np.array(out)


def bits_per_spike(tcs):
    """ring/analysis.py, compute_bits_per_spike; Methods equation (16)."""
    return (tcs * np.log2(tcs)).mean(1)


def calc_C(X):
    """ring/fn.py, calc_C: mean over rows of |rfft(norm forward)|^2, and its inverse transform."""
    C_ft = np.mean(np.abs(np.fft.rfft(X, axis=1, norm="forward")) ** 2, axis=0)
    return np.fft.irfft(C_ft, norm="forward"), C_ft


def softplus(x, beta=1.0):
    """ring/fn.py, softplus, numerically stable."""
    return np.where(x >= 0, x + np.log1p(np.exp(-beta * np.abs(x))) / beta,
                    np.log1p(np.exp(-beta * np.abs(x))) / beta)


def inv_softplus(y, beta=1.0):
    return np.log(np.expm1(beta * y)) / beta


def wrapped_gaussian_ft(scale, N_theta=N_THETA, eq_var=1.0):
    """ring/tc.py, wrapped_gaussian_cov (Fourier side)."""
    n = np.arange(N_theta // 2 + 1)
    return (eq_var / np.sqrt(2 * np.pi) / scale) * np.exp(-n ** 2 / (2 * scale ** 2))


def sample_z(rng, N_samples, N_freq, dtype=np.float64):
    """ring/gp_opt.py, sample_z (numpy branch), from a seeded Generator."""
    z = (rng.standard_normal((N_samples, N_freq), dtype=dtype)
         + 1j * rng.standard_normal((N_samples, N_freq), dtype=dtype)) / np.sqrt(2)
    z[:, 0] = z[:, 0].real * np.sqrt(2)
    return z


def gen_Phi_m(scale, bias, beta, N_samples, rng, N_theta=N_THETA, normalize=True, z=None):
    """ring/gp_opt.py, gen_Phi_m: wrapped-Gaussian process through softplus(x - b, beta)."""
    if z is None:
        z = sample_z(rng, N_samples, N_theta // 2 + 1)
    X = np.fft.irfft(z * np.sqrt(wrapped_gaussian_ft(scale, N_theta))[None, :], axis=1, norm="forward")
    Phi = softplus(X - bias, beta)
    if normalize:
        Phi = Phi / (Phi.mean(1, keepdims=True) + 1e-30)
    return Phi


# ---------------------------------------------------------------- measures chosen in the claims file


def circulant_projection(M):
    """Average of a square matrix along its circular diagonals (claims file, fig3c criterion)."""
    n = M.shape[0]
    i = np.arange(n)
    prof = np.array([M[i, (i + d) % n].mean() for d in range(n)])
    return prof[(i[None, :] - i[:, None]) % n]


def rel_dist_from_circulant(M):
    """||M - circ(M)||_F / ||M||_F (claims file, fig3c criterion)."""
    return np.linalg.norm(M - circulant_projection(M)) / np.linalg.norm(M)


def fourier_purity(v):
    """Fraction of a vector's power at its dominant frequency, counting +k and -k together,
    and that frequency (claims file, fig3c criterion)."""
    F = np.abs(np.fft.fft(v)) ** 2
    n = len(v)
    p = np.array([F[0]] + [F[k] + F[n - k] for k in range(1, n // 2)] + ([F[n // 2]] if n % 2 == 0 else []))
    k = int(np.argmax(p))
    return p[k] / p.sum(), k


def circ_diff(a, b):
    """Absolute circular difference in [0, pi]."""
    return np.abs(np.angle(np.exp(1j * (np.asarray(a) - np.asarray(b)))))


def ks_distance(a, b):
    from scipy.stats import ks_2samp
    return ks_2samp(a, b).statistic


def tv_distance(p, q):
    return 0.5 * np.abs(np.asarray(p) - np.asarray(q)).sum()


def hellinger(p, q):
    return np.sqrt(0.5 * ((np.sqrt(p) - np.sqrt(q)) ** 2).sum())


# ---------------------------------------------------------------- loading every session at once


def load_all_curves(version=VERSION):
    """Stream every session and compute its tuning curves (as ring/data.py process_all_tcs).

    Returns (sessions, Phi_data, mouse_nums, names): Phi_data holds the partition-averaged
    curves of the head-direction units with a non-zero curve, each divided by its mean
    (data_and_generative_model.ipynb cell 3; data_driven.load_data_Phi).
    """
    order = session_order(list_assets(version))
    sessions = []
    for i, (path, aid, subj, ogen) in enumerate(order):
        s = load_session(aid, version=version)
        plain, opt, sig = tuning_curves_session(s)
        hd_idx, ti, tf, _, _ = epoch_bins(s)
        sessions.append(dict(idx=i, subject=subj, path=path, ogen=ogen, sess=s, plain=plain, opt=opt,
                             sig=sig, hd_idx=hd_idx, ti=ti, tf=tf))
    Phi, mn = [], []
    for d in sessions:
        o = d["opt"].mean(1)
        o = o[~np.all(o == 0, axis=1)]
        Phi.append(o / o.mean(1, keepdims=True))
        mn += [d["idx"]] * len(o)
    names = np.array([d["subject"] for d in sessions])
    return sessions, np.concatenate(Phi), np.array(mn), names


# ---------------------------------------------------------------- the data-derived network
# ring/data_driven.py, ring/regression.py, ring/sim.py


def nonlin(x, beta=2.0):
    """data_driven.nonlin: softplus with beta 2."""
    return softplus(x, beta)


def resample_curves_fft(X, N_new):
    """data_driven.resample_curves_fft (zero-padded Fourier resampling)."""
    N0, Nc = X.shape
    F = np.fft.rfft(X, axis=0)
    G = np.zeros((N_new // 2 + 1, Nc), dtype=complex)
    k = min(F.shape[0], G.shape[0])
    G[:k] = F[:k]
    G *= N_new / N0
    return np.fft.irfft(G, n=N_new, axis=0)


def prepare_network_curves(Phi_data, N_theta=10000, sigma=2, n_sinkhorn=1000):
    """data_driven.prepare_smoothed_normalized_resampled_tuning_curves (Supplementary Note 3,
    section 8.1): inverse softplus (beta 2), circular Gaussian smoothing of 2 bins, softplus,
    Sinkhorn-Knopp normalization of both axes (1,000 sweeps), inverse softplus, Fourier
    resampling to N_theta angles, softplus. Input (N, 100); returns X, Phi of shape (N_theta, N)."""
    P = Phi_data.T.copy()
    X = inv_softplus(P, 2.0)
    Ps = nonlin(gaussian_filter1d(X, sigma=sigma, axis=0, mode="wrap"))
    for _ in range(n_sinkhorn):
        Ps /= Ps.mean(1, keepdims=True)
        Ps /= Ps.mean(0, keepdims=True)
    Xr = resample_curves_fft(inv_softplus(Ps, 2.0), N_theta)
    return Xr, nonlin(Xr)


def compute_J(X, Phi, lamda):
    """regression.compute_J (method opt): primal when N_theta >= N, else dual. Zero diagonal."""
    N_theta, N = Phi.shape
    if N_theta >= N:
        M = (Phi.T @ Phi) / N_theta + np.eye(N) * (N * lamda)
        Mi = np.linalg.inv(M)
        J_uc = ((X.T @ Phi) / N_theta) @ Mi
        return J_uc - Mi * (np.diag(J_uc) / np.diag(Mi))[:, None]
    K = (Phi @ Phi.T) / N + (lamda * N_theta) * np.eye(N_theta)
    Ki = np.linalg.inv(K)
    A = np.eye(N) - (1 / N) * (Phi.T @ Ki @ Phi)
    J_uc = (1 / N) * (X.T @ Ki @ Phi)
    return J_uc - A * (np.diag(J_uc) / np.diag(A))[:, None]


def compute_weights(X, Phi, lamda=1e-8):
    """data_driven.compute_weights: J, and J' for the angular derivative of X (Methods eq. 41)."""
    J = compute_J(X, Phi, lamda)
    dth = 2 * np.pi / X.shape[0]
    dX = np.concatenate(((X[0:1] - X[-1:]) / dth, np.diff(X, axis=0) / dth), axis=0)
    return J, compute_J(dX, Phi, lamda)


def simulate(J, x0, T, tau=0.05, dt=0.001, c=1.0, save_every=None, J_prime=None, omega=None,
             on_save=None, dtype=np.float32):
    """sim.run_sim as data_driven.run_simulation calls it: Euler steps of
    tau dx/dt = -x + J phi(x) + c (1 - mean_i phi(x)) [+ tau omega(t) J' phi(x)],
    phi the softplus of beta 2, in float32 as the paper's torch tensors. x0 (N, B).
    omega, when given, is a function of time returning one value or one per column.
    on_save(t, x) is called at t = 0 and every save_every seconds. Returns the final state.
    Steps are numbered as in run_sim: i = 1 .. int(T/dt) - 1, so the last state is at
    t = T - dt (run_sim's loop is range(1, N_t))."""
    J = J.astype(dtype)
    Jp = J_prime.astype(dtype) if J_prime is not None else None
    x = x0.astype(dtype).copy()
    N_t = int(round(T / dt))
    every = int(round(save_every / dt)) if save_every else None
    if on_save:
        on_save(0.0, x)
    a = dtype(dt / tau)
    with np.errstate(over="ignore", invalid="ignore"):
        for i in range(1, N_t):
            r = nonlin(x)
            drive = J @ r + dtype(c) * (dtype(1.0) - r.mean(0))[None, :]
            if Jp is not None:
                w = np.asarray(omega(i * dt), dtype=dtype)
                drive += dtype(tau) * w * (Jp @ r)
            x += a * (-x + drive)
            if every and i % every == 0 and on_save:
                on_save(i * dt, x)
    return x


def nearest_target(Phi_t, r, Phi_sq=None, refine=50):
    """Index of the nearest target firing-rate point and the distance / sqrt(N)
    (data_driven.compute_distances_to_ring). Phi_t (N_theta, N), r (N, B).
    The nearest point is first located with the expansion |a|^2 + |b|^2 - 2 a.b in the dtype
    of the inputs (float32), whose rounding hides distances below about 1e-3; the distance is
    then computed directly, as the paper's code does (norm of the difference), in float64, to
    the 2 * refine + 1 target points around that one, and the nearest of these is kept."""
    if Phi_sq is None:
        Phi_sq = (Phi_t ** 2).sum(1)
    d2 = Phi_sq[:, None] + (r ** 2).sum(0)[None, :] - 2 * (Phi_t @ r)
    idx = d2.argmin(0)
    n_t, N = Phi_t.shape
    cols = np.arange(r.shape[1])
    if not refine:
        dist = np.sqrt(np.maximum(d2[idx, cols], 0)) / np.sqrt(N)
        return idx, dist
    cand = (idx[None, :] + np.arange(-refine, refine + 1)[:, None]) % n_t
    rr = r.T.astype(np.float64)
    d = np.stack([np.linalg.norm(Phi_t[cand[k]].astype(np.float64) - rr, axis=1) for k in range(cand.shape[0])])
    j = d.argmin(0)
    return cand[j, cols], d[j, cols] / np.sqrt(N)


def circularized_profile(J_sorted):
    """First row of data_driven_attractor.ipynb create_circularized_matrix: mean over i of
    np.roll(J_sorted[i], -i), the mean of the sorted matrix along each circular diagonal."""
    n = J_sorted.shape[0]
    i = np.arange(n)
    return np.array([J_sorted[i, (i + d) % n].mean() for d in range(n)])


def count_states(pos, n, width):
    """Number of distinct final positions on a ring of n sites, for the readings of the claims
    file's merging rule (positions within `width` of each other are one state): single linkage
    (chains of gaps up to width), greedy (a new state when farther than width from the first
    member of the current one), and bins (occupied bins of width `width`)."""
    p = np.sort(np.asarray(pos) % n)
    if len(p) == 0:
        return dict(single=0, greedy=0, bins=0)
    gaps = np.diff(np.r_[p, p[0] + n])
    single = max(int((gaps > width).sum()), 1)
    # greedy, starting after the largest gap so a state does not straddle the start
    s = int(np.argmax(gaps)) + 1
    q = np.r_[p[s:], p[:s] + n]
    greedy, start = 1, q[0]
    for v in q[1:]:
        if v - start > width:
            greedy += 1
            start = v
    bins = len(np.unique(np.floor(p / width).astype(int)))
    return dict(single=single, greedy=greedy, bins=bins)
