"""Loading and measures for CRCNS hc-11 (Grosmark & Buzsaki 2016, Science 351:1440).

Everything is read from the eight sessInfo .mat files in
NoveltySessInfoMatFiles.tar.gz, streamed from the public CRCNS bucket and
decompressed in memory, except the cluster quality of Figure S11, which streams
the .clu, .fet and .xml files of the per-session archives <session>.tar.gz. Sources of the parameters below:

- [M] the paper's supplement, Materials and Methods, as cited by the claims file's
  opening comment or by the section named;
- [A] an assumption, said what and why, and listed as a deviation in the record;
- [S] a standard choice for a detail that cannot change a result.
"""
import hashlib
import io
import tarfile
from concurrent.futures import ThreadPoolExecutor

import fsspec
import h5py
import numpy as np
from scipy.ndimage import gaussian_filter1d

BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-11/live/"
SESSINFO = "data/NoveltySessInfoMatFiles.tar.gz"
# From hc-11/live/checksums.md5 (CRCNS data sets are unversioned; this pins the file).
SESSINFO_MD5 = "2666ee13c8c1e3609c08c6f4ba444d11"

BIN_CM = 2.0          # [M] Place Field Analysis, 2 cm bins
SMOOTH_CM = 5.0       # [M] 5 cm Gaussian kernel, read as its SD (claims opening comment)
RUN_SPEED = 0.05      # [M] 5 cm/s running threshold (m/s)
N_PF_NULL = 5000      # [M] 5,000 null rate vectors
TAU = 0.02            # [M] Bayesian Replay Analysis, 20 ms bins
N_SHUF = 1000         # [M] 1,000 circular place-field shuffles
RATE_FLOOR = 1e-3     # [S] Hz added to rate maps so that log(0) never occurs
SPEED_SMOOTH_S = 0.5  # [S] SD of the Gaussian smoothing of speed, in seconds
OFFLINE_STATES = ("NREM", "Drowsy", "Intermediate")
# [A] "off-line" states, quiet waking and NREM: the data set's NREM, its
# Drowsy state (drowsy wake / light sleep, low movement; the quiet waking) and
# its Intermediate state (a sub-type of NREM, per the data descriptor).
N_THREADS = 4         # [S] threads for the shuffles (results do not depend on it)
MAZE_IMMOBILE = 0.05  # [A] on the maze, immobility is smoothed speed < 5 cm/s


# ---------------------------------------------------------------- loading
class _Hashing:
    """File wrapper that computes the MD5 of the bytes read through it."""

    def __init__(self, f):
        self.f, self.md5 = f, hashlib.md5()

    def read(self, n=-1):
        b = self.f.read(n)
        self.md5.update(b)
        return b


def load_sessions():
    """Stream the tar of sessInfo files; return one dict per session and the file's MD5."""
    f = _Hashing(fsspec.open(BUCKET + SESSINFO, block_size=2**22).open())
    out = []
    with tarfile.open(fileobj=f, mode="r|gz") as t:
        for m in t:
            if not m.isfile() or not m.name.endswith(".mat"):
                continue
            h = h5py.File(io.BytesIO(t.extractfile(m).read()), "r")
            out.append(_session(m.name.split("/")[-1].replace("_sessInfo.mat", ""), h["sessInfo"]))
    while f.read(2**22):  # hash the rest of the file
        pass
    return sorted(out, key=lambda s: s["name"]), f.md5.hexdigest()


def _session(name, s):
    ep = {k: s["Epochs"][k][()] for k in s["Epochs"]}
    st = s["Spikes/SpikeTimes"][()].ravel()
    ids = s["Spikes/SpikeIDs"][()].ravel().astype(int)
    pyr = s["Spikes/PyrIDs"][()].ravel().astype(int)
    intr = s["Spikes/IntIDs"][()].ravel().astype(int)
    order = np.argsort(ids, kind="stable")
    ids_s, st_s = ids[order], st[order]
    u, start = np.unique(ids_s, return_index=True)
    spikes = {int(c): np.sort(x) for c, x in zip(u, np.split(st_s, start[1:]))}
    maze = "".join(chr(c) for c in s["Position/MazeType"][()].ravel())
    ses = dict(
        name=name, animal=name.split("_")[0], maze=maze,
        circular=maze.startswith("Circular"),
        pre=tuple(ep["PREEpoch"].ravel()), mz=tuple(ep["MazeEpoch"].ravel()),
        post=tuple(ep["POSTEpoch"].ravel()), duration=float(ep["sessDuration"].ravel()[0]),
        states={k: ep[k].T.copy() for k in ("Wake", "Drowsy", "NREM", "Intermediate", "REM")},
        pos_t=s["Position/TimeStamps"][()].ravel(),
        x1d=s["Position/OneDLocation"][()].ravel(),
        xy=s["Position/TwoDLocation"][()].T,
        pyr=[int(c) for c in pyr], intn=[int(c) for c in intr],
        spikes={c: spikes.get(c, np.zeros(0)) for c in list(pyr) + list(intr)},
        n_spikes_total=len(st), last_spike=float(st.max()), sorted_times=bool(np.all(np.diff(st) >= 0)),
    )
    ses["shank"] = {c: c // 100 for c in ses["spikes"]}
    _behaviour(ses)
    return ses


# ---------------------------------------------------------------- intervals
def merge(iv):
    iv = np.asarray(iv, float).reshape(-1, 2)
    if len(iv) == 0:
        return iv
    iv = iv[np.argsort(iv[:, 0])]
    out = [iv[0].copy()]
    for a, b in iv[1:]:
        if a <= out[-1][1]:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append(np.array([a, b]))
    return np.array(out)


def intersect(a, b):
    a, b = merge(a), merge(b)
    out = []
    i = j = 0
    while i < len(a) and j < len(b):
        lo, hi = max(a[i, 0], b[j, 0]), min(a[i, 1], b[j, 1])
        if hi > lo:
            out.append((lo, hi))
        if a[i, 1] < b[j, 1]:
            i += 1
        else:
            j += 1
    return np.array(out).reshape(-1, 2)


def total(iv):
    iv = np.asarray(iv).reshape(-1, 2)
    return float(np.sum(iv[:, 1] - iv[:, 0]))


def in_intervals(t, iv):
    iv = merge(iv)
    if len(iv) == 0:
        return np.zeros(len(t), bool)
    k = np.searchsorted(iv[:, 0], t, side="right") - 1
    return (k >= 0) & (t < iv[np.clip(k, 0, None), 1])


def count_in(times, iv):
    iv = np.asarray(iv).reshape(-1, 2)
    return int(np.sum(np.searchsorted(times, iv[:, 1]) - np.searchsorted(times, iv[:, 0])))


def clip_to(iv, lo, hi):
    return intersect(iv, [[lo, hi]])


def first_T(iv, T):
    """The first T seconds of the intervals iv (counted in their own time)."""
    iv, out, acc = merge(iv), [], 0.0
    for a, b in iv:
        if acc >= T:
            break
        take = min(b - a, T - acc)
        out.append((a, a + take))
        acc += take
    return np.array(out).reshape(-1, 2)


def last_T(iv, T):
    iv = merge(iv)
    flip = -iv[::-1, ::-1]
    return -first_T(flip, T)[::-1, ::-1]


def offline(ses, epoch):
    """Offline intervals in an epoch ('pre', 'post'): the dataset's states [A]."""
    lo, hi = ses[epoch]
    return clip_to(np.vstack([ses["states"][k] for k in OFFLINE_STATES]), lo, hi)


def yoke(ses, reading):
    """PRE and POST windows yoked to the shorter epoch (claims opening comment, Y).

    Y-a: last T of PRE and first T of POST; Y-b: first T of each; Y-c: offline
    time limited to the smaller offline total, PRE nearest the maze and POST first.
    Returns (pre_offline, post_offline) intervals.
    """
    (a0, a1), (b0, b1) = ses["pre"], ses["post"]
    T = min(a1 - a0, b1 - b0)
    if reading == "a":
        return offline(ses, "pre") if a1 - a0 <= T else clip_to(offline(ses, "pre"), a1 - T, a1), \
            clip_to(offline(ses, "post"), b0, b0 + T)
    if reading == "b":
        return clip_to(offline(ses, "pre"), a0, a0 + T), clip_to(offline(ses, "post"), b0, b0 + T)
    pre, post = offline(ses, "pre"), offline(ses, "post")
    To = min(total(pre), total(post))
    return last_T(pre, To), first_T(post, To)


# ---------------------------------------------------------------- behaviour
def _behaviour(ses):
    t, x, xy = ses["pos_t"], ses["x1d"], ses["xy"]
    dt = float(np.median(np.diff(t)))
    ses["pos_dt"] = dt
    sig = SPEED_SMOOTH_S / dt
    # speed along the track, from the linearised position where it is defined
    v1 = np.full(len(t), np.nan)
    ok = ~np.isnan(x)
    dx = np.gradient(np.where(ok, x, np.nan)) / dt
    if ses["circular"]:
        # the circular track wraps; remove jumps across the end of the linearisation
        dx[np.abs(dx) > 2.0] = np.nan
    v1 = dx
    good = ~np.isnan(v1)
    num = gaussian_filter1d(np.where(good, v1, 0.0), sig)
    den = gaussian_filter1d(good.astype(float), sig)
    ses["vel1d"] = np.where(good, num / np.maximum(den, 1e-9), np.nan)
    # 2D speed for immobility on the maze
    okxy = ~np.isnan(xy[:, 0])
    v2 = np.full(len(t), np.nan)
    v2[1:] = np.hypot(*np.diff(xy, axis=0).T) / np.diff(t)
    g2 = ~np.isnan(v2)
    num = gaussian_filter1d(np.where(g2, v2, 0.0), sig)
    den = gaussian_filter1d(g2.astype(float), sig)
    ses["speed2d"] = np.where(den > 0.2, num / np.maximum(den, 1e-9), np.nan)
    # directions: linear mazes 'right' (x increasing) and 'left'; circular maze 'cw'
    run = ok & (np.abs(ses["vel1d"]) >= RUN_SPEED)
    if ses["circular"]:
        ses["dirs"] = {"cw": run}
    else:
        ses["dirs"] = {"right": run & (ses["vel1d"] > 0), "left": run & (ses["vel1d"] < 0)}
    ses["running"] = run


def mask_intervals(t, mask, dt):
    """Intervals of samples where mask is true (each sample covers dt)."""
    m = np.r_[False, mask, False].astype(int)
    on = np.flatnonzero(np.diff(m) == 1)
    off = np.flatnonzero(np.diff(m) == -1) - 1
    return np.c_[t[on] - dt / 2, t[off] + dt / 2]


def maze_immobile(ses, reading="notrun"):
    """Offline time on the maze [A]; the data set's states do not mark immobility there.

    'notrun': MAZE time outside running on the track (along-track speed >= 5 cm/s),
    the complement of the paper's running epochs; '2d': smoothed 2D head speed below
    5 cm/s (the 2D tracking is noisy in some sessions, see the data check).
    """
    t, dt = ses["pos_t"], ses["pos_dt"]
    if reading == "2d":
        return clip_to(mask_intervals(t, ses["speed2d"] < MAZE_IMMOBILE, dt), *ses["mz"])
    run = mask_intervals(t, ses["running"], dt)
    lo, hi = ses["mz"]
    edges = np.r_[lo, run.ravel(), hi].reshape(-1, 2)
    return clip_to(edges[edges[:, 1] > edges[:, 0]], lo, hi)


# ---------------------------------------------------------------- place fields
def smooth(v, axis=-1):
    return gaussian_filter1d(v, SMOOTH_CM / BIN_CM, axis=axis, mode="constant")


def place_maps(ses, rng):
    """Place fields per cell and direction [M, Place Field Analysis].

    Returns {dir: dict(edges, occ, maps{cell: smoothed rate}, raw{cell: unsmoothed rate},
    fields{cell: list of (start, stop) bin ranges}, null99{cell})}.
    """
    t, x = ses["pos_t"], ses["x1d"]
    dt = ses["pos_dt"]
    L = np.nanmax(x)
    nb = int(np.ceil(L * 100 / BIN_CM))
    edges = np.linspace(0, nb * BIN_CM / 100, nb + 1)
    out = {}
    for d, m in ses["dirs"].items():
        xb = np.clip(np.digitize(x, edges) - 1, 0, nb - 1)
        occ = np.bincount(xb[m], minlength=nb) * dt
        socc = smooth(occ)
        p = occ / occ.sum()
        res = dict(edges=edges, occ=occ, maps={}, raw={}, fields={}, nspk={}, peak={})
        for c in ses["pyr"]:
            sp = ses["spikes"][c]
            sp = sp[(sp >= t[0]) & (sp <= t[-1])]
            k = np.clip(np.searchsorted(t, sp), 1, len(t) - 1)
            k = np.where(np.abs(t[k - 1] - sp) < np.abs(t[k] - sp), k - 1, k)
            keep = m[k] & (np.abs(t[k] - sp) < dt)
            cnt = np.bincount(xb[k[keep]], minlength=nb).astype(float)
            n = int(cnt.sum())
            rate = smooth(cnt) / np.maximum(socc, 1e-9)
            raw = np.where(occ > 0, cnt / np.maximum(occ, 1e-9), 0.0)
            res["maps"][c], res["raw"][c], res["nspk"][c] = rate, raw, n
            fields = []
            if n > 0:
                null = rng.multinomial(n, p, size=N_PF_NULL).astype(float)
                null = smooth(null, axis=1) / np.maximum(socc, 1e-9)
                thr = np.percentile(null, 99, axis=0)
                above = rate > thr
                for a, b in _runs(above):
                    if b - a >= 5 and rate[a:b].max() >= 1.0:
                        fields.append((a, b))
            res["fields"][c] = fields
        out[d] = res
    return out


def _runs(mask):
    m = np.r_[0, mask.astype(int), 0]
    on = np.flatnonzero(np.diff(m) == 1)
    off = np.flatnonzero(np.diff(m) == -1)
    return list(zip(on, off))


# ---------------------------------------------------------------- ripple events
def ripple_events(ses):
    """Population synchrony events [M, Ripple Event Detection], without the LFP condition.

    All pyramidal spikes in 1 ms bins, Gaussian of SD 15 ms; trigger mean + 3 SD of
    the 1 ms bins in NREM of PRE and POST; bounds where the rate returns to that mean.
    Returns an array of (start, stop) for all candidate events, and the NREM mean.
    """
    allsp = np.concatenate([ses["spikes"][c] for c in ses["pyr"]])
    allsp = allsp[allsp <= ses["duration"]]  # spikes past sessDuration (one session) are left out
    n = int(np.ceil(ses["duration"] * 1000)) + 1
    r = np.bincount((allsp * 1000).astype(np.int64), minlength=n).astype(np.float32)
    r = gaussian_filter1d(r, 15.0, mode="constant")
    nrem = np.vstack([clip_to(ses["states"]["NREM"], *ses["pre"]), clip_to(ses["states"]["NREM"], *ses["post"])])
    msk = np.zeros(n, bool)
    for a, b in nrem:
        msk[int(a * 1000):int(b * 1000)] = True
    mu, sd = float(r[msk].mean()), float(r[msk].std())
    thr = mu + 3 * sd
    above = r > thr
    base = r > mu
    ev = []
    for a, b in _runs(base):
        if above[a:b].any():
            ev.append((a / 1000.0, b / 1000.0))
    return np.array(ev).reshape(-1, 2), mu, thr


def event_table(ses, ev, place_cells_by_dir):
    """Per event: duration, number of pyramidal cells firing, epoch, offline flag."""
    import pandas as pd
    st, en = ev[:, 0], ev[:, 1]
    npyr = np.zeros(len(ev), int)
    for c in ses["pyr"]:
        sp = ses["spikes"][c]
        npyr += (np.searchsorted(sp, en) - np.searchsorted(sp, st)) > 0
    mid = (st + en) / 2
    epoch = np.where(mid < ses["pre"][1], "PRE", np.where(mid < ses["mz"][1], "MAZE", "POST"))
    sleep = np.vstack([offline(ses, "pre"), offline(ses, "post")])
    off = in_intervals(mid, np.vstack([sleep, maze_immobile(ses, "notrun")]))
    off2 = in_intervals(mid, np.vstack([sleep, maze_immobile(ses, "2d")]))
    df = pd.DataFrame(dict(start=st, stop=en, dur=en - st, npyr=npyr, epoch=epoch, offline=off,
                           offline_2d=off2))
    return df


def ripple_selected(df):
    """Ripple events: 50 to 500 ms, offline (either MAZE reading), at least five pyramidal cells [M]."""
    return df[(df.dur >= 0.05) & (df.dur <= 0.5) & (df.offline | df.offline_2d) & (df.npyr >= 5)]


# ---------------------------------------------------------------- Bayesian replay
def bin_counts(ses, cells, starts, stops):
    """Spike counts in 20 ms bins for each event. Returns counts (B x n), event index per bin."""
    nb = np.floor((stops - starts) / TAU + 1e-9).astype(int)
    nb = np.maximum(nb, 0)
    ev_of_bin = np.repeat(np.arange(len(starts)), nb)
    off = np.concatenate([np.arange(k) for k in nb]) if len(nb) else np.zeros(0, int)
    b0 = starts[ev_of_bin] + off * TAU
    edges_lo = b0
    S = np.zeros((len(b0), len(cells)), np.float32)
    for j, c in enumerate(cells):
        sp = ses["spikes"][c]
        S[:, j] = np.searchsorted(sp, edges_lo + TAU) - np.searchsorted(sp, edges_lo)
    return S, ev_of_bin, nb


def rotate_smooth(raw, shifts):
    """Circularly translate unsmoothed maps (n x P) by shifts (n,), re-smooth [M]."""
    n, P = raw.shape
    idx = (np.arange(P)[None, :] - shifts[:, None]) % P
    return smooth(raw[np.arange(n)[:, None], idx], axis=1)


def _wcorr_from_moments(Ep, Ep2, ev, nb_ev, tb):
    """Weighted correlation per event from per-bin posterior moments (eqs. 3 to 5).

    Each time bin's posterior sums to one, so the weights per bin are 1.
    """
    seg = np.r_[0, np.cumsum(nb_ev)[:-1]]
    def s(v):
        return np.add.reduceat(v, seg, axis=0)
    W = nb_ev.astype(float)
    if Ep.ndim == 2:
        W = W[:, None]
        tbb = tb[:, None]
    else:
        tbb = tb
    mp = s(Ep) / W
    mt = s(np.broadcast_to(tbb, Ep.shape)) / W
    cpp = s(Ep2) / W - mp**2
    ctt = s(np.broadcast_to(tbb**2, Ep.shape)) / W - mt**2
    cpt = s(Ep * tbb) / W - mp * mt
    with np.errstate(invalid="ignore", divide="ignore"):
        return cpt / np.sqrt(cpp * ctt)


def decode_moments(S, logF, sumF):
    """Posterior mean and second moment of position per bin (eqs. 1, 2)."""
    L = S @ logF - TAU * sumF[None, :]
    L -= L.max(axis=1, keepdims=True)
    np.exp(L, out=L)
    L /= L.sum(axis=1, keepdims=True)
    P = logF.shape[1]
    pos = np.arange(P, dtype=np.float32)
    return L @ pos, L @ (pos**2), L


def replay_scores(S, ev_of_bin, nb_ev, maps, raw, rng, n_shuf=N_SHUF, null_shifts=None):
    """Observed r, null |r| mean and SD, rZ per event, and the posterior (eqs. 1 to 7)."""
    n, P = maps.shape
    tb = np.concatenate([np.arange(k) for k in nb_ev]).astype(np.float32)
    F = maps + RATE_FLOOR
    Ep, Ep2, post = decode_moments(S, np.log(F).astype(np.float32), F.sum(0).astype(np.float32))
    r_obs = _wcorr_from_moments(Ep, Ep2, ev_of_bin, nb_ev, tb)
    if null_shifts is None:
        null_shifts = rng.integers(0, P, size=(n_shuf, n))
    def one(sh):
        Fk = rotate_smooth(raw, sh) + RATE_FLOOR
        a, b, _ = decode_moments(S, np.log(Fk).astype(np.float32), Fk.sum(0).astype(np.float32))
        return np.abs(_wcorr_from_moments(a, b, ev_of_bin, nb_ev, tb)).astype(np.float32)

    with ThreadPoolExecutor(N_THREADS) as ex:
        absnull = np.stack(list(ex.map(one, null_shifts)), 1)
    mu = np.nanmean(absnull, 1)
    sd = np.nanstd(absnull, 1)
    rz = (np.abs(r_obs) - mu) / sd
    return dict(r=r_obs, null_mu=mu, null_sd=sd, rz=rz, absnull=absnull, post=post, tb=tb)


def pcc(S, ev_of_bin, nb_ev, maps, raw, null_mu, null_sd, rz_obs, rng, n_shuf=N_SHUF):
    """Per cell contribution (eq. 8) for every cell and every event it fired in.

    Each cell's map alone is circularly translated (1,000 draws); since a translation
    takes one of P values, rZ is computed for each distinct translation and averaged
    with the counts of the 1,000 random draws (identical to drawing them one by one).
    Returns {cell index: (event indices, PCC per event, mean cell-shuffled rZ per event)}.
    """
    n, P = maps.shape
    tb = np.concatenate([np.arange(k) for k in nb_ev]).astype(np.float32)
    F = maps + RATE_FLOOR
    logF = np.log(F).astype(np.float32)
    L0 = S @ logF - TAU * F.sum(0)[None, :]
    part = np.zeros((len(nb_ev), n), bool)
    np.logical_or.at(part, ev_of_bin, S > 0)
    npart = part.sum(1)
    pos = np.arange(P, dtype=np.float32)
    draws_all = [np.bincount(rng.integers(0, P, size=n_shuf), minlength=P) for _ in range(n)]

    def one(c):
        evs = np.flatnonzero(part[:, c])
        if len(evs) == 0:
            return evs, np.zeros(0), np.zeros(0)
        draws = draws_all[c]
        shifts = np.flatnonzero(draws)
        sel = np.isin(ev_of_bin, evs)
        Ls = L0[sel]
        sc = S[sel, c][:, None]
        evb = ev_of_bin[sel]
        nb_sel = nb_ev[evs]
        tbs = tb[sel]
        rz_sh = np.zeros((len(evs), len(shifts)))
        for k, s in enumerate(shifts):
            fc = smooth(np.roll(raw[c], s)) + RATE_FLOOR
            Lk = Ls + sc * (np.log(fc) - logF[c])[None, :] - TAU * (fc - F[c])[None, :]
            Lk -= Lk.max(1, keepdims=True)
            np.exp(Lk, out=Lk)
            Lk /= Lk.sum(1, keepdims=True)
            r = _wcorr_from_moments(Lk @ pos, Lk @ pos**2, evb, nb_sel, tbs)
            rz_sh[:, k] = (np.abs(r) - null_mu[evs]) / null_sd[evs]
        mean_sh = (rz_sh * draws[shifts][None, :]).sum(1) / draws.sum()
        return evs, (rz_obs[evs] - mean_sh) * npart[evs], mean_sh

    with ThreadPoolExecutor(N_THREADS) as ex:
        out = dict(enumerate(ex.map(one, range(n))))
    return out, part, npart


def direction_posterior(ses, cells, rates, S_ev, dur):
    """Equation 6: log posterior of each running direction for each event.

    rates: {dir: array of mean rates (Hz) of the cells while running in that direction}.
    S_ev: events x cells spike counts. Returns the direction with the higher posterior.
    """
    dirs = list(rates)
    ll = np.stack([S_ev @ np.log(rates[d] + RATE_FLOOR) - dur[:, 0] * rates[d].sum() for d in dirs], 1)
    return np.array(dirs)[np.argmax(ll, 1)]


# ---------------------------------------------------------------- spatial measures
def spatial_info(rate, occ):
    """Information per spike and per second [M, ref. 32, Skaggs]."""
    p = occ / occ.sum()
    mr = float(np.sum(p * rate))
    if mr <= 0:
        return np.nan, np.nan
    with np.errstate(divide="ignore", invalid="ignore"):
        t = np.where(rate > 0, p * rate / mr * np.log2(rate / mr), 0.0)
    return float(t.sum()), float(t.sum() * mr)


def coherence(rate):
    """Spatial coherence: correlation of each bin with the mean of its neighbours [ref. 32]."""
    nb = (np.r_[rate[1:], np.nan] + np.r_[np.nan, rate[:-1]])
    cnt = (~np.isnan(np.r_[rate[1:], np.nan])).astype(float) + (~np.isnan(np.r_[np.nan, rate[:-1]]))
    nbm = np.nansum(np.c_[np.r_[rate[1:], np.nan], np.r_[np.nan, rate[:-1]]], 1) / cnt
    r = np.corrcoef(rate, nbm)[0, 1]
    return float(np.arctanh(np.clip(r, -0.999999, 0.999999)))


def wilcoxon_1s(x, alternative="greater"):
    from scipy.stats import wilcoxon
    x = np.asarray(x)
    x = x[~np.isnan(x)]
    if len(x) < 2 or np.all(x == 0):
        return np.nan
    return float(wilcoxon(x, alternative=alternative).pvalue)


# ---------------------------------------------------------------- per-session pipeline
def min_participants(n_place):
    """At least 10% of place cells or 5, whichever is greater [M, Bayesian Replay Analysis]."""
    return max(5, int(np.ceil(0.1 * n_place)))


def replay_set(ses, events, cells, maps, raw, rng, n_shuf=N_SHUF, with_pcc=False):
    """Replay analysis of one template (one session and direction) on the ripple events.

    Applies the 100 ms and participation criteria for these cells, then scores the
    kept events. Returns a dict with the kept event table and the per-event scores.
    """
    cand = events[events.dur >= 0.1]
    S, evb, nb = bin_counts(ses, cells, cand.start.values, cand.stop.values)
    part = np.zeros((len(cand), len(cells)), bool)
    np.logical_or.at(part, evb, S > 0)
    keep = part.sum(1) >= min_participants(len(cells))
    kept = cand[keep].copy()
    if len(kept) == 0:
        return dict(events=kept, rz=np.zeros(0))
    S, evb, nb = bin_counts(ses, cells, kept.start.values, kept.stop.values)
    out = replay_scores(S, evb, nb, maps, raw, rng, n_shuf=n_shuf)
    kept["r"], kept["rz"] = out["r"], out["rz"]
    kept["null_mu"], kept["null_sd"] = out["null_mu"], out["null_sd"]
    kept["null_one"] = out["absnull"][:, 0]  # one null |r| per event (the first random template)
    kept["npart"] = part[keep].sum(1)
    kept["frac_part"] = kept["npart"] / len(cells)
    res = dict(events=kept, ncells=len(cells))
    if with_pcc:
        pc, _, _ = pcc(S, evb, nb, maps, raw, out["null_mu"], out["null_sd"], out["rz"], rng, n_shuf=n_shuf)
        res["pcc"] = {cells[k]: v for k, v in pc.items()}
    return res


def direction_of_events(ses, events):
    """Equation 6 on linear mazes: assign each event to LEFT or RIGHT [M]."""
    if ses["circular"]:
        return np.array(["cw"] * len(events))
    t, dt = ses["pos_t"], ses["pos_dt"]
    rates = {}
    cells = ses["pyr"]
    for d, m in ses["dirs"].items():
        iv = mask_intervals(t, m, dt)
        T = total(iv)
        rates[d] = np.array([count_in(ses["spikes"][c], iv) / T for c in cells])
    Sev = np.array([np.searchsorted(ses["spikes"][c], events.stop.values)
                    - np.searchsorted(ses["spikes"][c], events.start.values) for c in cells]).T
    return direction_posterior(ses, cells, rates, Sev.astype(float), events.dur.values[:, None])


def analyse_session(ses, seed, n_shuf=N_SHUF):
    """Place fields, ripple events, replay and PCC for one session."""
    rng = np.random.default_rng(seed)
    pm = place_maps(ses, rng)
    ev, mu, thr = ripple_events(ses)
    table = event_table(ses, ev, None)
    rip = ripple_selected(table).copy()
    rip["assigned"] = direction_of_events(ses, rip)
    rep = {}
    for d, r in pm.items():
        cells = [c for c in ses["pyr"] if r["fields"][c]]
        maps = np.array([r["maps"][c] for c in cells])
        raw = np.array([r["raw"][c] for c in cells])
        rep[d] = replay_set(ses, rip, cells, maps, raw, rng, n_shuf=n_shuf, with_pcc=True)
        rep[d]["cells"] = cells
    return dict(name=ses["name"], pm=pm, all_events=table, ripples=rip, rate_mu=mu, rate_thr=thr, rep=rep)


# ---------------------------------------------------------------- cluster quality (Figure S11)
FET_RATE = 20000.0   # [M] 20 kHz; the last .fet column is the spike time in samples (session .xml)
BURST_ISI = 0.006    # [M] Figure S11 legend, bursts are spikes within 6 ms of each other
MIN_COND_SPIKES = 10  # [S] spikes a cell needs in a condition for its quality and stability


def _burst_rules(t):
    """Masks of the spikes kept under the two readings of 'only the first spike of bursts'.

    'a' [A]: every spike not preceded by a spike of the cell within 6 ms (single spikes and
    first spikes of bursts); 'b' [A]: only first spikes of bursts (not preceded, and followed
    within 6 ms).
    """
    d = np.diff(t)
    not_prev = np.r_[True, d >= BURST_ISI]
    has_next = np.r_[d < BURST_ISI, False]
    return {"a": not_prev, "b": not_prev & has_next}


def _cell_quality(X, t, windows):
    """Quality and stability of one cell's cluster [M, Figure S11 legend].

    Quality: median Mahalanobis distance of the spikes of a condition to the cluster centre
    (mean over all kept spikes). Stability of two conditions: median distance of the spikes
    of one condition to the centre of the other, averaged over both orders. The covariance
    is that of all kept spikes of the cluster [A], which keeps it defined when a condition
    has few spikes.
    """
    out = {}
    for rule, keep in _burst_rules(t).items():
        Xk, tk = X[keep], t[keep]
        out[f"n_all_{rule}"] = len(tk)
        if len(tk) <= X.shape[1] + 1:
            continue
        mu = Xk.mean(0)
        P = np.linalg.pinv(np.cov(Xk, rowvar=False))
        cond = {}
        for name, iv in windows.items():
            m = in_intervals(tk, iv)
            out[f"n_{name}_{rule}"] = int(m.sum())
            if m.sum() >= MIN_COND_SPIKES:
                cond[name] = Xk[m]

        def dist(A, c):
            D = A - c
            return np.sqrt(np.maximum(np.einsum("ij,jk,ik->i", D, P, D), 0))

        for name, A in cond.items():
            out[f"q_{name}_{rule}"] = float(np.median(dist(A, mu)))
        names = list(windows)
        for i in range(len(names)):
            for j in range(i + 1, len(names)):
                a, b = names[i], names[j]
                if a in cond and b in cond:
                    out[f"s_{a}-{b}_{rule}"] = float(np.mean([np.median(dist(cond[a], cond[b].mean(0))),
                                                              np.median(dist(cond[b], cond[a].mean(0)))]))
    return out


def quality_windows(ses):
    """Conditions of Figure S11: PRE and POST ripple events (yoked windows Y-a) and MAZE running."""
    ev, _, _ = ripple_events(ses)
    rip = ripple_selected(event_table(ses, ev, None))
    mid = ((rip.start + rip.stop) / 2).values
    pre, post = yoke(ses, "a")
    iv = rip[["start", "stop"]].values
    run = clip_to(mask_intervals(ses["pos_t"], ses["running"], ses["pos_dt"]), *ses["mz"])
    return {"PRE": iv[in_intervals(mid, pre)], "MAZE": run, "POST": iv[in_intervals(mid, post)]}


def cluster_quality(ses):
    """Stream <session>.tar.gz (the .clu and .fet files of every shank, and the .xml) and return
    one row per pyramidal cell with its cluster quality and stability [M, Figure S11 legend].

    Cell ids of the sessInfo file are shank * 100 + cluster (checked by the spike counts
    returned). The PCA features are the first nFeatures (3) per channel of each .fet row, with
    the channels of each shank's group in the session's .xml (spikeDetection, in shank order);
    the columns after them and the time (last column) are not used.
    """
    import re
    import pandas as pd
    windows = quality_windows(ses)
    pyr = set(ses["pyr"])
    clu, cells, ncol, xml = {}, {}, {}, None
    f = fsspec.open(f"{BUCKET}data/{ses['name']}.tar.gz", block_size=2**22).open()
    with tarfile.open(fileobj=f, mode="r|gz") as t:
        for m in t:
            base = m.name.split("/")[-1]
            if base == f"{ses['name']}.xml":
                xml = t.extractfile(m).read().decode()
                continue
            parts = base.split(".")
            if len(parts) != 3 or parts[1] not in ("clu", "fet"):
                continue
            sh = int(parts[2])
            if parts[1] == "clu":
                clu[sh] = pd.read_csv(t.extractfile(m), header=None, dtype=np.int32, engine="c").values.ravel()[1:]
                continue
            fh = t.extractfile(m)
            nf = int(fh.readline())
            fet = pd.read_csv(fh, sep=r"\s+", header=None, dtype=np.int64, engine="c").values
            ncol[sh] = (nf, len(fet), len(clu[sh]) == len(fet))
            tt = fet[:, -1] / FET_RATE
            for c in sorted(x for x in pyr if x // 100 == sh):
                idx = np.flatnonzero(clu[sh] == c % 100)
                idx = idx[np.argsort(tt[idx], kind="stable")]
                cells[c] = (fet[idx, :-1].astype(np.float32), tt[idx])
            del fet, tt
            clu.pop(sh)
    groups = re.findall(r"<group>(.*?)</group>", xml.split("<spikeDetection>")[1].split("</spikeDetection>")[0], re.S)
    npca = {k + 1: len(re.findall(r"<channel>", g)) * int(re.search(r"<nFeatures>(\d+)</nFeatures>", g).group(1))
            for k, g in enumerate(groups)}
    info = pd.DataFrame([dict(session=ses["name"], shank=sh, n_spikes=n, n_columns=nf, n_pca=npca[sh], clu_matches=ok)
                         for sh, (nf, n, ok) in sorted(ncol.items())])
    rows = []
    for c, (X, tc) in sorted(cells.items()):
        row = dict(session=ses["name"], cell=c, n_fet=len(tc), n_sessinfo=len(ses["spikes"][c]))
        row.update(_cell_quality(X[:, :npca[c // 100]].astype(float), tc, windows))
        rows.append(row)
    return pd.DataFrame(rows), info
