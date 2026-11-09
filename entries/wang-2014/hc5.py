"""Helpers for CRCNS hc-5 (rat i01) and the rate model of Wang et al. (2015).

Data access. The data set is 13 tar.gz files in the public S3 bucket
``crcnsarchive`` (docs/archives.md, "CRCNS"). A tar.gz cannot be read at an
offset, so each file is streamed once from the start (``tarfile`` mode
``r|gz`` over an HTTP response) and only the members needed are kept in
memory; nothing is written to disk. The processed file of each session
(``*_BehavElectrData.mat``, MATLAB 5, or ``*_BehavElectrDataLFP.mat``,
MATLAB 7.3) comes within the first ~1 GB of each tar, so reading it stops
early. A full inventory (every member, and the small text members such as
the ``.xml`` parameter file, which comes last) streams the whole file.

Parameters and where they come from:
- THETA_BAND (6-10 Hz) and the Thomson multitaper estimate with NW = 4: the
  paper, Online Methods, "LFP power" ("Thomson multi-taper methods (NW = 4,
  30). The peak power in the theta frequency range (6-10Hz) was detected").
  The 2 s window is a standard choice (the "30" after NW = 4 is not
  explained); it is used here only to describe the sessions, not to test a
  claim. DELTA_BAND (2-4 Hz) for a theta/delta ratio is a standard choice.
- Model equations and parameters: Supplementary Modeling, equations 1-3,
  "The network parameters used are: tau = 10 ms, J1 = 15, J0 = 30,
  tau_R = 0.1 s, tau_F = 0.3 s, U = 0.05, g = 1.5, k = 2.5, delta = 0.2 rad,
  N = 100", the Ornstein-Uhlenbeck noise "with a time constant of 10ms driven
  by white noise with a standard deviation sigma = 5", and the external
  currents of Supplementary Table 1 (in the claims' criteria).
- Model choices the paper leaves open, as the claims file lists them
  (fig3c-model-theta-builds-fields): duration 10 s, Euler step 0.1 ms,
  initial state uniform low rates (1 Hz plus up to 0.1 Hz of noise), seeds
  0-4; the first 1 s is discarded as a transient (an assumption: the
  initial state is arbitrary). The noise term is written eta(t), with no
  index for the unit. It is read as independent noise for each unit
  (noise="unit"), an assumption taken from the paper's Figure 3c,d, whose
  no-theta panels show activity scattered independently over the neurons,
  and from the Results ("Without the synchronized change in the network
  excitability, neurons in the network were activated randomly"); one
  process common to all units (noise="common", the equation as printed)
  is run as a variant. sigma is read as the stationary standard deviation
  of the process (an assumption).
- Model measures, fixed in the claims file's criterion and so a deviation
  from the paper (which gives none): the bump's position is the population
  vector angle; within each theta cycle (the cycles of the theta input) the
  bump's displacement is measured between the first and last time the
  population rate is at least half its peak in that cycle; a unit's field
  is the time over which its rate, smoothed with a boxcar one theta cycle
  long, stays at or above half its peak. "Half its peak" is read two ways,
  both reported: (a) the run that contains the unit's peak over the whole
  simulation (one field per unit), and (b) every run above half that peak
  (a unit may pass through the bump several times as it travels round the
  ring). The theta modulation of the population rate (the ratio of the
  population rate's minimum to its maximum, per cycle) tells whether the
  activity is chunked into theta cycles at all.
"""
from __future__ import annotations

import io
import re
import tarfile
import time
import urllib.request

import numpy as np

DATASET = "crcns:hc-5/unversioned"  # CRCNS data sets are not versioned (docs/archives.md); DOI 10.6080/K0KS6PHF
BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-5/"
FS = 1250  # LFP and tracking sampling rate, data descriptor ("The samplig rate is 1250Hz")
THETA_BAND = (6.0, 10.0)
SHIFTS_S = (-20, -10, -5, 5, 10, 20)  # clock check shifts, a standard choice
DELTA_BAND = (2.0, 4.0)

# file name -> MD5 from hc-5/checksums.md5 (read 2026-11-09)
FILES = [
    "i01_maze05.005.tar.gz", "i01_maze06.002.tar.gz", "i01_maze06.005.tar.gz",
    "i01_maze08.001.tar.gz", "i01_maze08.003.tar.gz", "i01_maze08.004.tar.gz",
    "i01_maze8.006.tar.gz", "i01_maze09.002.tar.gz", "i01_maze13.002.tar.gz",
    "i01_maze13.003.tar.gz", "i01_maze15.001.tar.gz", "i01_maze15.002.tar.gz",
    "i01_maze16.002.tar.gz",
]

_SORT_FILES = re.compile(r"\.(clu|res|fet|spk|mm|m1m2|threshold)\.\d+(\.orig)?$")


def open_stream(fname: str) -> tarfile.TarFile:
    """Open one tar.gz of the bucket as a forward-only stream."""
    return tarfile.open(fileobj=urllib.request.urlopen(BUCKET + fname), mode="r|gz")


def read_text(url_tail: str) -> str:
    return urllib.request.urlopen(BUCKET + url_tail).read().decode()


def inventory(fname: str) -> dict:
    """Stream a whole tar: every member's name and size, and the text of the
    small parameter members (.xml, .meta, .cat.evt, .ParamWheel, .AddLedCoord).
    Keeps nothing large in memory."""
    t0 = time.time()
    members, texts = [], {}
    tf = open_stream(fname)
    for m in tf:
        members.append((m.name, m.size))
        if m.name.endswith((".xml", ".meta", ".cat.evt", ".ParamWheel", "maze_param", ".AddLedCoord")):
            texts[m.name] = tf.extractfile(m).read().decode(errors="replace")
    xml = next((v for k, v in texts.items() if k.endswith(".xml")), "")
    def tag(t):
        r = re.findall(rf"<{t}>(.*?)</{t}>", xml, re.S)
        return r[0].strip() if r else None
    return dict(
        file=fname, seconds=time.time() - t0, members=members, texts=texts,
        xml_date=tag("date"), xml_description=tag("description"), xml_notes=tag("notes"),
        xml_nchannels=int(tag("nChannels")) if tag("nChannels") else None,
        xml_lfp_rate=tag("lfpSamplingRate"),
    )


def processed_bytes(fname: str) -> tuple[str, bytes]:
    """Return the name and bytes of the session's processed file, stopping the stream there."""
    tf = open_stream(fname)
    for m in tf:
        if re.search(r"_BehavElectrData(LFP)?\.mat$", m.name):
            return m.name, tf.extractfile(m).read()
    raise FileNotFoundError(f"no processed file in {fname}")


def _h5(f, path):
    import h5py
    o = f[path]
    a = o[()]
    if o.attrs.get("MATLAB_class", b"") == b"char":
        return "".join(map(chr, np.asarray(a).ravel()))
    return np.asarray(a).squeeze()


def load_session(fname: str) -> dict:
    """Load what the data check uses from a session's processed file.

    Returns 1-D numpy arrays at 1250 Hz (eeg, speed, wheel speed, wheel-run
    index, x, y, theta phase), the spike sample index, cluster and position
    at each spike, the cluster table, and the session's labels. Field names
    are those of the file (two layouts exist; both are mapped here)."""
    name, b = processed_bytes(fname)
    out = dict(file=fname, member=name, header=b[:116].decode(errors="replace").strip())
    if b[:19] == b"MATLAB 7.3 MAT-file":
        import h5py
        f = h5py.File(io.BytesIO(b), "r")
        out.update(
            layout="v7.3", task=_h5(f, "Laps/taskType"),
            eeg=_h5(f, "Track/eeg").astype(np.float32),
            speed=_h5(f, "Track/speed_MMsec").astype(np.float32), speed_unit="mm/s",
            x=_h5(f, "Track/xMM").astype(np.float32), y=_h5(f, "Track/yMM").astype(np.float32),
            thetaph=_h5(f, "Track/thetaPhHilb").astype(np.float32),
            whl_speed=None, nlap_cw=None,
            res=_h5(f, "Spike/res").astype(np.int64), totclu=_h5(f, "Spike/totclu").astype(int),
            spike_x=_h5(f, "Spike/xMM"), spike_thph=_h5(f, "Spike/thPhaseHilb"),
            clu_isintern=_h5(f, "Clu/isIntern").astype(int),
            clu_shank=_h5(f, "Clu/shank").astype(int),
            xml_date=_h5(f, "xml/Date"), xml_file=_h5(f, "xml/FileName"),
            n_channels=int(_h5(f, "xml/nChannels")),
            behav_type=None, trial_type=None,
        )
        f.close()
    else:
        import scipy.io as sio
        d = sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False)
        P, T, L, S, C = d["Par"], d["Track"], d["Laps"], d["Spike"], d["Clu"]

        def g(o, *names):  # field names differ between sessions
            for nm in names:
                if hasattr(o, nm):
                    return getattr(o, nm)
            raise KeyError(f"none of {names} in {o._fieldnames}")
        bt = np.atleast_1d(P.BehavType)
        out.update(
            layout="v5", task=str(L.taskType), rat_name=str(P.RatName),
            eeg=T.eeg.astype(np.float32),
            speed=g(T, "speed", "speed_MMsec").astype(np.float32), speed_unit="file units (Track.speed)",
            x=g(T, "X", "xPix").astype(np.float32), y=g(T, "Y", "yPix").astype(np.float32),
            thetaph=g(T, "thetaPh", "thetaPhHilb").astype(np.float32),
            whl_speed=g(L, "WhlSpeedCW").astype(np.float32), nlap_cw=g(L, "NLapCW").astype(int),
            res=S.res.astype(np.int64), totclu=S.totclu.astype(int),
            spike_x=g(S, "X", "xPix"), spike_thph=g(S, "thPhase", "thPhaseHilb"),
            clu_isintern=C.isIntern.astype(int), clu_shank=C.shank.astype(int),
            behav_type=bt if bt.size else None,
            trial_type=np.atleast_1d(P.TrialType) if np.size(P.TrialType) else None,
            n_channels=int(P.totNch) if hasattr(P, "totNch") else None,
        )
    del b
    return out


def multitaper_psd(segs: np.ndarray, fs: float = FS, nw: float = 4.0) -> tuple[np.ndarray, np.ndarray]:
    """Thomson multitaper power spectrum (NW = 4, 2NW-1 tapers), averaged over segments."""
    from scipy.signal.windows import dpss
    n = segs.shape[1]
    tapers = dpss(n, nw, Kmax=int(2 * nw - 1))
    segs = segs - segs.mean(1, keepdims=True)
    spec = np.abs(np.fft.rfft(segs[:, None, :] * tapers[None], axis=-1)) ** 2
    return np.fft.rfftfreq(n, 1 / fs), spec.mean(axis=(0, 1))


def theta_summary(eeg: np.ndarray, mask: np.ndarray, win_s: float = 2.0) -> dict | None:
    """Theta peak power (6-10 Hz), its frequency and the theta/delta ratio over
    non-overlapping windows in which at least 90% of samples satisfy mask."""
    L = int(win_s * FS)
    n = len(eeg) // L
    m = mask[: n * L].reshape(n, L).mean(1) >= 0.9
    if m.sum() < 3:
        return None
    segs = eeg[: n * L].reshape(n, L)[m].astype(float)
    f, p = multitaper_psd(segs)
    tb = (f >= THETA_BAND[0]) & (f <= THETA_BAND[1])
    db = (f >= DELTA_BAND[0]) & (f < DELTA_BAND[1])
    return dict(n_windows=int(m.sum()), theta_peak_power=float(p[tb].max()),
                theta_peak_hz=float(f[tb][np.argmax(p[tb])]),
                theta_delta=float(p[tb].max() / p[db].mean()))


# ---------------------------------------------------------------- the model

def simulate(I=2.0, I_theta=0.0, I_L=0.0, f_theta=7.0, cue_speed=2 * np.pi / 5, T=10.0, dt=1e-4,
             N=100, seed=0, noise="common", tau=0.01, J1=15.0, J0=30.0, tau_R=0.1, tau_F=0.3, U=0.05,
             g=1.5, k=2.5, delta=0.2, sigma=5.0, tau_n=0.01, rec_dt=1e-3):
    """Euler integration of Supplementary Modeling equations 1-3 (1D ring).

    tau m' = -m + g[I_R + I_E]+, I_R = (1/N) sum W m x u,
    W = J1 exp(k cos(theta - theta' - delta)) / I0(k) - J0,
    x' = (1 - x)/tau_R - u x m, u' = (U - u)/tau_F + U (1 - u) m,
    I_E = I + I_theta cos(2 pi f t) + I_L cos(theta - theta_ext(t)) + eta(t),
    theta_ext(t) = cue_speed * t. Returns rates (Hz) sampled every rec_dt."""
    from scipy.special import i0
    rng = np.random.default_rng(seed)
    th = 2 * np.pi * np.arange(N) / N
    W = J1 * np.exp(k * np.cos(th[:, None] - th[None, :] - delta)) / i0(k) - J0
    m = 1.0 + 0.1 * rng.random(N)
    x = np.ones(N)
    u = np.full(N, U)
    eta = np.zeros(N if noise == "unit" else 1)
    a = np.exp(-dt / tau_n)
    b = sigma * np.sqrt(1 - a * a)
    nstep = int(round(T / dt))
    every = int(round(rec_dt / dt))
    R = np.empty((nstep // every, N))
    for s in range(nstep):
        t = s * dt
        IR = W @ (m * x * u) / N
        IE = I + I_theta * np.cos(2 * np.pi * f_theta * t) + I_L * np.cos(th - cue_speed * t) + eta
        m_new = m + dt / tau * (-m + g * np.maximum(IR + IE, 0.0))
        x = x + dt * ((1 - x) / tau_R - u * x * m)
        u = u + dt * ((U - u) / tau_F + U * (1 - u) * m)
        m = m_new
        eta = a * eta + b * rng.standard_normal(eta.shape)
        if s % every == 0:
            R[s // every] = m
    return R


def model_measures(R, f_cycle, rec_dt=1e-3, burn=1.0, cue_speed=None):
    """Measures of the claims file's criterion (see the module docstring).

    f_cycle: the theta frequency of the condition; for a condition without
    theta, the frequency of the matching theta condition, so that windows of
    the same length are compared."""
    N = R.shape[1]
    th = 2 * np.pi * np.arange(N) / N
    R = R[int(burn / rec_dt):]
    tot = R.sum(1)
    pos = np.angle((R * np.exp(1j * th)).sum(1))
    upos = np.unwrap(pos)
    L = int(round(1 / f_cycle / rec_dt))
    ncyc = len(R) // L
    sweeps, mod = [], []
    for c in range(ncyc):
        sl = slice(c * L, (c + 1) * L)
        tt = tot[sl]
        mod.append(tt.min() / tt.max() if tt.max() > 0 else np.nan)
        act = np.where(tt >= 0.5 * tt.max())[0]
        sweeps.append(upos[sl][act[-1]] - upos[sl][act[0]] if (tt.max() > 0 and len(act) > 1) else np.nan)
    sweeps = np.array(sweeps)
    # mean travel of the bump (rad/s): the slope of the unwrapped rate-weighted
    # position of each window, so that near-silent samples between cycles do not
    # enter; the concentration |sum m e^{i theta}| / sum m is 1 for activity at
    # one place and near 0 for activity spread over the ring
    zc = np.array([(R[c * L:(c + 1) * L] * np.exp(1j * th)).sum() for c in range(ncyc)])
    wpos = np.unwrap(np.angle(zc))
    drift = float(np.polyfit(np.arange(ncyc) * L * rec_dt, wpos, 1)[0])
    conc = np.abs((R * np.exp(1j * th)).sum(1)) / np.maximum(tot, 1e-12)
    concentration = float(np.average(conc, weights=tot))
    ker = np.ones(L) / L
    peak_field, all_runs = [], []
    for i in range(N):
        r = np.convolve(R[:, i], ker, mode="same")
        if r.max() <= 0:
            continue
        above = (r >= 0.5 * r.max()).astype(int)
        d = np.diff(np.r_[0, above, 0])
        on, off = np.where(d == 1)[0], np.where(d == -1)[0]
        dur = (off - on) * rec_dt
        all_runs += list(dur)
        ip = int(np.argmax(r))
        j = np.where((on <= ip) & (off > ip))[0]
        peak_field.append(dur[j[0]])
    out = dict(
        mean_rate_hz=float(R.mean()),
        cycle_s=1 / f_cycle,
        pop_min_over_max=float(np.nanmedian(mod)),
        bump_concentration=concentration,
        sweep_rad=float(np.nanmedian(np.abs(sweeps))),
        frac_cycles_forward=float(np.nanmean(np.sign(drift) * sweeps > 0)),
        drift_rad_s=float(drift),
        field_peak_s=float(np.median(peak_field)),
        field_peak_cycles=float(np.median(peak_field) * f_cycle),
        field_all_s=float(np.median(all_runs)),
        field_all_cycles=float(np.median(all_runs) * f_cycle),
    )
    if cue_speed is not None:
        cue = cue_speed * (np.arange(len(R)) * rec_dt + burn)
        lag = np.angle(np.exp(1j * (pos - cue)))
        out["bump_cue_lag_mad_rad"] = float(np.abs(np.angle(np.exp(1j * (lag - np.angle(np.exp(1j * lag).mean())))).mean()))
        out["drift_over_cue_speed"] = float(drift / cue_speed)
    return out


# ------------------------------------------------------- per-session check

def _runs(mask):
    d = np.diff(np.r_[0, mask.astype(int), 0])
    return np.where(d == 1)[0], np.where(d == -1)[0]


def clock_xcorr(eeg: np.ndarray, run: np.ndarray, win_s: float = 1.0, max_lag_s: int = 30) -> dict:
    """Clock check: the correlation, over 1-s windows, between log theta/delta of
    the LFP and the fraction of the window spent running, with the running
    series shifted by -30 to +30 s. LFP and behaviour on one clock give the
    peak at a lag near 0. Power from a Hann-windowed FFT per window (a
    standard choice)."""
    L = int(win_s * FS)
    n = len(eeg) // L
    seg = eeg[: n * L].reshape(n, L).astype(float)
    seg = (seg - seg.mean(1, keepdims=True)) * np.hanning(L)
    p = np.abs(np.fft.rfft(seg, axis=1)) ** 2
    f = np.fft.rfftfreq(L, 1 / FS)
    td = np.log((p[:, (f >= THETA_BAND[0]) & (f <= THETA_BAND[1])].mean(1) + 1e-12)
                / (p[:, (f >= DELTA_BAND[0]) & (f < DELTA_BAND[1])].mean(1) + 1e-12))
    rf = run[: n * L].reshape(n, L).mean(1)
    lags = np.arange(-max_lag_s, max_lag_s + 1)
    r = []
    for lg in lags:
        a, b = (td[lg:], rf[: n - lg]) if lg >= 0 else (td[: n + lg], rf[-lg:])
        r.append(np.corrcoef(a, b)[0, 1] if a.std() > 0 and b.std() > 0 else np.nan)
    r = np.array(r)
    if np.all(np.isnan(r)):
        return dict(r_at_0=None, best_lag_s=None, r_best=None)
    i = int(np.nanargmax(r))
    return dict(r_at_0=float(r[lags == 0][0]), best_lag_s=int(lags[i]) * win_s, r_best=float(r[i]),
                r_at_pm30=float(np.nanmean(r[[0, -1]])))


def summarize_session(fname: str) -> dict:
    """Small summary of one session for the data check (no large arrays returned).

    - counts: clusters, putative interneurons (Clu.isIntern), spikes, duration;
    - laps and trial outcomes (Par.BehavType, Par.TrialType) for the maze task;
    - wheel runs: contiguous periods with a wheel-run index (Laps.NLapCW > 0),
      their durations;
    - theta during running (wheel speed > 10 file units, or speed smoothed over
      1 s above the 75th percentile of nonzero speed) and during stillness
      (smoothed speed below its 25th percentile, wheel still); the running mask
      shifted by -20 to 20 s; and the clock check of clock_xcorr;
    - theta in the first and last third of the session;
    - consistency of the spike table with the tracking table: the position and
      theta phase stored at each spike against Track at the spike's sample.
    """
    s = load_session(fname)
    n = len(s["eeg"])
    out = dict(file=fname, member=s["member"], layout=s["layout"], task=s["task"],
               header=s["header"], minutes=n / FS / 60, n_channels=s.get("n_channels"),
               n_clusters=len(s["clu_isintern"]), n_interneurons=int(s["clu_isintern"].sum()),
               n_shanks=len(np.unique(s["clu_shank"])), n_spikes=len(s["res"]),
               xml_date=s.get("xml_date"), xml_file=s.get("xml_file"), rat_name=s.get("rat_name"))
    sp = np.nan_to_num(s["speed"], nan=-1)
    # speed smoothed over 1 s (a standard choice) so that a 2-s window can be classed as running
    sp = np.where(sp < 0, -1, np.convolve(np.clip(sp, 0, None), np.ones(FS) / FS, mode="same"))
    pos_sp = sp[sp > 0]
    hi, lo = (np.percentile(pos_sp, 75), np.percentile(pos_sp, 25)) if len(pos_sp) else (np.inf, -np.inf)
    out["speed_range"] = (float(np.nanmin(s["speed"])), float(np.nanmax(s["speed"])))
    out["x_range"] = (float(np.nanmin(s["x"])), float(np.nanmax(s["x"])))
    out["y_range"] = (float(np.nanmin(s["y"])), float(np.nanmax(s["y"])))
    wheel = s["whl_speed"] if s["whl_speed"] is not None else np.zeros(n, np.float32)
    # running: on the wheel (wheel speed > 10) or moving fast in the maze or arena
    run = (wheel > 10) | (sp >= hi)
    if s["nlap_cw"] is not None and s["nlap_cw"].max() > 0:
        on, off = _runs(s["nlap_cw"] > 0)
        out["wheel_run_s"] = ((off - on) / FS).round(1).tolist()
        out["wheel_speed_max"] = float(wheel.max())
    else:
        out["wheel_run_s"] = []
    still = (sp >= 0) & (sp <= lo) & (wheel <= 1)
    out["theta_run"] = theta_summary(s["eeg"], run)
    out["theta_still"] = theta_summary(s["eeg"], still)
    out["theta_run_shifted"] = {sh: theta_summary(s["eeg"], np.roll(run, int(sh * FS))) for sh in SHIFTS_S}
    out["clock_xcorr"] = clock_xcorr(s["eeg"], run)
    thirds = np.zeros(n, int)
    thirds[n // 3: 2 * n // 3] = 1
    thirds[2 * n // 3:] = 2
    out["theta_run_thirds"] = [theta_summary(s["eeg"], run & (thirds == k)) for k in range(3)]
    if s["behav_type"] is not None:
        bt = s["behav_type"]
        out["behav_type_counts"] = {int(k): int((bt == k).sum()) for k in np.unique(bt)}
        out["trial_type_counts"] = {int(k): int((s["trial_type"] == k).sum()) for k in np.unique(s["trial_type"])}
        out["n_laps"] = int(len(bt))
    # Spike.res is a MATLAB (1-based) sample index: Track row res - 1 (checked)
    r = np.clip(s["res"] - 1, 0, n - 1)
    out["spike_field_lengths"] = dict(res=len(s["res"]), totclu=len(s["totclu"]), x=len(s["spike_x"]), theta_phase=len(s["spike_thph"]))
    if len(s["spike_x"]) == len(r):
        ok = np.isfinite(s["spike_x"]) & np.isfinite(s["x"][r])
        out["spike_x_matches_track"] = float(np.mean(np.abs(s["spike_x"][ok] - s["x"][r][ok]) < 1e-3))
    else:
        out["spike_x_matches_track"] = None
    if len(s["spike_thph"]) == len(r):
        out["spike_phase_matches_track"] = float(np.mean(np.abs(np.angle(np.exp(1j * (s["spike_thph"] - s["thetaph"][r])))) < 1e-3))
    else:
        out["spike_phase_matches_track"] = None
    out["res_range"] = (int(s["res"].min()), int(s["res"].max()), n)
    return out
