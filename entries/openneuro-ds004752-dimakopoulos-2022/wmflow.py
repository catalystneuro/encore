"""Loading and measures for OpenNeuro ds004752 (Dimakopoulos et al. 2022, eLife 11:e78677).

Everything is streamed from the pinned snapshot 1.0.1: the file list comes from OpenNeuro's
GraphQL API, and each file is read at its ``urls[0]``, which points at the S3 object version
of that snapshot. EDF recordings are read by byte range, one trial at a time.

Where parameters come from:

- Trial windows (fixation [-6 -5] s, encoding [-5 -3] s, maintenance [-2 0] s, probe at 0 s):
  the claims file's GC method (Methods, Task). In the dataset a trial is an 8 s epoch starting
  at its ``onset``, so the probe is at 6 s into the epoch; this is checked in the notebook.
- Trials for GC: correct trials of set sizes 6 and 8 without the ``Artifact`` flag (claims
  file, GC method; Methods, Recording setup).
- Downsampling to 500 Hz for the LFP and ECoG (Methods, Recording setup), and to 40 Hz before
  GC (claims file, GC method, from the Methods' "Nyquist frequency=40 Hz" and the code's
  ``resamplefs = 40``). The anti-aliasing filter is scipy's polyphase FIR, a standard choice
  standing in for MATLAB's ``resample``.
- GC: FieldTrip ``mtmfft`` with one Hann taper and 20 s padding, nonparametric bivariate
  Wilson factorisation, Geweke's measure (claims file, GC method;
  ``calculateGranger_random_trial_sampling.m``). Each trial is demeaned before the taper,
  as FieldTrip's default ``polyremoval = 0`` does.
- Hippocampal channel (readings h1 to h3 of the claims file). The electrode and contact
  choices are assumptions, see ``hippocampal_channels``.
- White-matter reference: the first contact without an atlas label (``no_label_found``) on a
  hippocampal electrode, as ``MainSourceAnalysisConnectivity.m`` picks it
  (``nWM_contacts(hipp_chans_WM_contacts(1))``), except that contacts 1 and 2 are skipped
  (assumption: the code's rule can pick the deepest contact itself) and the contact is taken
  in the hemisphere of the hippocampal contact (assumption: a reference across the midline
  would mix in the other hemisphere's signal).
- PSD: multitaper, windows of 10 cycles, smoothing 0.2 x frequency (3 tapers), 0.1 s steps,
  relative to fixation (Methods, Power spectral density).
- PLV: multitaper Fourier transform with two tapers over 2 s epochs, 1 Hz resolution (Methods,
  Phase-locking value).
- Incorrect-trial sources: the derivative files hold none, so each period's LCMV filter is
  recovered by least squares from the file's own virtual sensors and scalp channels
  (``lcmv_weights``) and applied to the raw EEG (``eeg_sources``). That the paper used the
  correct-trial filters for the incorrect trials is an assumption; it does not say.
"""
from __future__ import annotations

import io
import json
import re
from concurrent.futures import ThreadPoolExecutor

import fsspec
import numpy as np
import pandas as pd
import requests
import scipy.io as sio
from scipy.signal import resample_poly

DATASET = "ds004752"
TAG = "1.0.1"
GRAPHQL = "https://openneuro.org/crn/graphql"

# Trial epoch: 8 s from onset; the probe is at 6 s (fixation starts at -6 s).
PROBE_S = 6.0
WINDOWS = {"fix": (-6.0, -5.0), "enc": (-5.0, -3.0), "maint": (-2.0, 0.0)}

_FILES: pd.DataFrame | None = None


def files() -> pd.DataFrame:
    """All files of the snapshot, with size, git-annex or git id and pinned URL."""
    global _FILES
    if _FILES is None:
        q = ('{ snapshot(datasetId: "%s", tag: "%s") { files(recursive: true) '
             '{ filename size annexed id urls } } }' % (DATASET, TAG))
        r = requests.post(GRAPHQL, json={"query": q}, timeout=120)
        r.raise_for_status()
        fl = r.json()["data"]["snapshot"]["files"]
        df = pd.DataFrame(fl)
        df["url"] = df.urls.str[0]
        _FILES = df.set_index("filename")
    return _FILES


def url(path: str) -> str:
    return files().loc[path, "url"]


def read_tsv(path: str) -> pd.DataFrame:
    return pd.read_csv(url(path), sep="\t")


def read_json(path: str) -> dict:
    r = requests.get(url(path), timeout=60)
    r.raise_for_status()
    return r.json()


def _pmap(fn, items, n=16):
    with ThreadPoolExecutor(n) as ex:
        return list(ex.map(fn, items))


def sessions() -> pd.DataFrame:
    """One row per (subject, session) with the iEEG and EEG file stems."""
    fl = files().index
    rows = []
    for p in fl:
        m = re.match(r"(sub-\d+)/(ses-\d+)/ieeg/(.*)_ieeg\.edf$", p)
        if m:
            rows.append(dict(sub=m[1], ses=m[2], ieeg=p[: -len("ieeg.edf")],
                             eeg=p.replace("/ieeg/", "/eeg/")[: -len("ieeg.edf")]))
    return pd.DataFrame(rows).sort_values(["sub", "ses"]).reset_index(drop=True)


def events(modality: str = "ieeg") -> pd.DataFrame:
    """All trials of all sessions, from the ``*_events.tsv`` files of one modality."""
    ss = sessions()

    def rd(r):
        e = read_tsv(r[modality] + "events.tsv")
        e.insert(0, "ses", r.ses)
        e.insert(0, "sub", r["sub"])
        return e

    return pd.concat(_pmap(rd, [r for _, r in ss.iterrows()]), ignore_index=True)


def gc_trials(ev: pd.DataFrame, correct: int = 1) -> pd.Series:
    """Trials of the GC method: set sizes 6 and 8, correct (or incorrect), no artifact flag."""
    return (ev.SetSize.isin([6, 8])) & (ev.Correct == correct) & (ev.Artifact == 0)


# ---------------------------------------------------------------- EDF by byte range

def edf_header(path: str) -> dict:
    with fsspec.open(url(path), block_size=2**16) as fh:
        h = fh.read(256)
        ns = int(h[252:256])
        h2 = fh.read(ns * 256)

    def field(off, w, conv):
        return [conv(h2[off + i * w: off + (i + 1) * w].decode("latin-1").strip()) for i in range(ns)]

    o = 0
    lab = field(o, 16, str); o += ns * 16
    o += ns * 80
    dim = field(o, 8, str); o += ns * 8
    pmin = np.array(field(o, 8, float)); o += ns * 8
    pmax = np.array(field(o, 8, float)); o += ns * 8
    dmin = np.array(field(o, 8, float)); o += ns * 8
    dmax = np.array(field(o, 8, float)); o += ns * 8
    o += ns * 80
    nsamp = np.array(field(o, 8, int))
    gain = (pmax - pmin) / (dmax - dmin)
    return dict(path=path, labels=lab, dim=dim, gain=gain, offset=pmin - gain * dmin,
                nsamp=nsamp, hlen=256 * (ns + 1), nrec=int(h[236:244]),
                dur=float(h[244:252]), start=h[168:184].decode())


def edf_records(H: dict, r0: int, n: int, channels=None) -> np.ndarray:
    """Physical values of records r0..r0+n-1 (all channels share one rate), channels x samples."""
    fs = int(H["nsamp"][0])
    assert (H["nsamp"] == fs).all()
    ns = len(H["labels"])
    rb = ns * fs * 2
    with fsspec.open(url(H["path"]), block_size=n * rb + 16) as fh:
        fh.seek(H["hlen"] + r0 * rb)
        b = fh.read(n * rb)
    x = np.frombuffer(b, dtype="<i2").reshape(n, ns, fs).transpose(1, 0, 2).reshape(ns, n * fs)
    idx = np.arange(ns) if channels is None else np.asarray(channels)
    return x[idx].astype(np.float64) * H["gain"][idx, None] + H["offset"][idx, None]


def load_trials(sub: str, ev: pd.DataFrame, channels: list[str], modality: str = "ieeg",
                t0: float = -6.0, t1: float = 0.0, fs_out: int = 500) -> dict:
    """Read [t0, t1) s around the probe of each trial in ``ev`` (rows of one subject).

    Returns data (trials x channels x samples) at ``fs_out`` and the time axis. Channel
    names are matched after stripping the leading 'm' or '_' of the dataset's labels.
    """
    ss = sessions().set_index(["sub", "ses"])
    heads = {}
    for ses in ev.ses.unique():
        H = edf_header(ss.loc[(sub, ses), modality] + modality + ".edf")
        heads[ses] = H
    jobs = []
    for i, r in enumerate(ev.itertuples()):
        H = heads[r.ses]
        names = [strip(l) for l in H["labels"]]
        ci = [names.index(c) for c in channels]
        fs = int(H["nsamp"][0])
        assert abs(H["dur"] - 1.0) < 1e-9
        rec0 = (r.nTrial - 1) * 8  # 8 records of 1 s per trial
        a = int(round(PROBE_S + t0))
        b = int(np.ceil(PROBE_S + t1))
        jobs.append((H, rec0 + a, b - a, ci, fs, a))

    def rd(job):
        H, r0, n, ci, fs, a = job
        x = edf_records(H, r0, n, ci)
        if fs != fs_out:
            from math import gcd
            g = gcd(fs, fs_out)
            x = resample_poly(x, fs_out // g, fs // g, axis=-1)
        i0 = int(round((PROBE_S + t0 - a) * fs_out))
        return x[:, i0: i0 + int(round((t1 - t0) * fs_out))]

    X = np.stack(_pmap(rd, jobs)).astype(np.float32)
    t = t0 + np.arange(X.shape[-1]) / fs_out
    return dict(data=X, time=t, fs=fs_out, channels=channels)


def strip(label: str) -> str:
    return re.sub(r"^[m_]", "", label)


# ---------------------------------------------------------------- electrodes

HIPP_ELECTRODES = ["AHL", "PHL", "HL", "AHR", "PHR", "HR"]


def electrodes(sub: str) -> pd.DataFrame:
    ss = sessions()
    stem = ss[ss["sub"] == sub].ieeg.iloc[0]
    e = read_tsv(stem + "electrodes.tsv")
    e["label"] = e.name.map(strip)
    e["electrode"] = e.label.str.replace(r"\d+$", "", regex=True)
    e["contact"] = e.label.str.extract(r"(\d+)$")[0].astype(int)
    e["ecog"] = e["size"] == 4.0
    return e


def hippocampal_channels(sub: str, side: str | None = None) -> dict:
    """Channels for the hippocampal readings (assumptions, stated in the notebook).

    - electrodes: depth electrodes named AH/PH/H followed by L or R (the code's
      ``contains(label,'AH')``, ``'PH'``); h1 uses the first present of AHL, PHL, HL, AHR,
      PHR, HR (left first: the paper's task is left-lateralised and Figure 1d shows the most
      distal contact of one electrode). ``side="R"`` (or ``"L"``) restricts h1 to h3 to the
      hippocampal electrodes of that side (Participant 3's right hippocampus).
    - h1: contact 1 (most distal, Methods, Electrode localization) re-referenced to ``ref``.
    - h2: contact 1 minus the next contact of the same electrode (contact 2; contact 3 where
      the files have no contact 2), a bipolar derivation as in GetDataInBipolar.m.
    - h3: contact 1 of every hippocampal electrode (of ``side``, if given), each re-referenced
      to ``ref``.
    - ref: a ``no_label_found`` contact numbered 3 or more in the hemisphere of h1, by the
      hemisphere letter of the electrode names: on h1's electrode if it has one, else on
      another hippocampal electrode of that hemisphere, else on any depth electrode of that
      hemisphere.
    - ecog_ref: the first such contact on a depth electrode that is not hippocampal, other than
      ``ref`` (Methods: the ECoG was re-referenced "against a different depth electrode
      contact"). In sub-10 and sub-12 no other depth electrode has one, and the next
      white-matter contact of the left hippocampal electrodes after their reference is used
      (sub-10 and sub-12 AHL4). It does not depend on ``side``.
    """
    e = electrodes(sub)
    allhel = [x for x in HIPP_ELECTRODES if x in set(e.electrode)]
    hel = [x for x in allhel if side is None or x.endswith(side)]
    main = hel[0]
    hemi = main[-1]
    wm = e[(~e.ecog) & (e.AnatomicalLocation == "no_label_found") & (e.contact >= 3)]

    def first_ref(main_el, hipp):
        for cand in (wm[wm.electrode == main_el],
                     wm[wm.electrode.isin([x for x in hipp if x.endswith(main_el[-1])])],
                     wm[wm.electrode.str.endswith(main_el[-1])]):
            if len(cand):
                return cand.label.iloc[0]
        raise ValueError(f"{sub}: no white-matter contact in hemisphere {main_el[-1]}")

    ref = first_ref(main, hel)
    ref0 = first_ref(allhel[0], allhel)  # the default (left-first) reference, for ecog_ref
    other = wm[(~wm.electrode.isin(allhel)) & (wm.label != ref0)]
    hwm = wm[wm.electrode.isin([x for x in allhel if x.endswith(allhel[0][-1])]) & (wm.label != ref0)]
    ecog_ref = other.label.iloc[0] if len(other) else hwm.label.iloc[0]
    con = sorted(e[e.electrode == main].contact)
    return dict(electrodes=hel, main=main, h1=f"{main}1", h2=(f"{main}1", f"{main}{con[1]}"),
                h3=[f"{x}1" for x in hel], ref=ref, ecog_ref=ecog_ref)


def hipp_signals(X: np.ndarray, chans: list[str], hc: dict) -> dict:
    """Hippocampal signals for readings h1, h2 and the h3 list, from trials x channels x time."""
    c = {n: i for i, n in enumerate(chans)}
    ref = X[:, c[hc["ref"]]]
    out = {"h1": X[:, c[hc["h1"]]] - ref,
           "h2": X[:, c[hc["h2"][0]]] - X[:, c[hc["h2"][1]]]}
    out["h3"] = [X[:, c[ch]] - ref for ch in hc["h3"]]
    return out


# ---------------------------------------------------------------- LCMV derivatives

def load_lcmv(sub: str) -> dict:
    """Virtual sensors and scalp channels of the derivative file, encoding and maintenance.

    ``variables`` lists what the file holds (scipy.io.whosmat) with the fields of each struct.
    """
    p = f"derivatives/{sub}/beamforming/{sub}-task-verbalWM-LCMVsources.mat"
    with fsspec.open(url(p), block_size=2**22) as fh:
        b = fh.read()
    m = sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False)
    out = {"variables": [(name, shape, cls, list(getattr(m[name], "_fieldnames", [])))
                         for name, shape, cls in sio.whosmat(io.BytesIO(b))]}
    for key, per in [("LCMV_encoding", "enc"), ("LCMV_maintenance", "maint")]:
        s = m[key]
        tr = np.atleast_1d(s.trial)
        tm = np.atleast_1d(s.time)
        out[per] = dict(label=[str(x) for x in s.label],
                        data=np.stack([np.asarray(x, dtype=np.float64) for x in tr]),
                        time=np.asarray(tm[0], dtype=float), fs=float(s.fsample))
    return out


# ---------------------------------------------------------------- resampling

def to_fs(x: np.ndarray, fs_in: float, fs_out: float = 40.0) -> np.ndarray:
    from fractions import Fraction
    fr = Fraction(fs_out / fs_in).limit_denominator(1000)
    return resample_poly(x, fr.numerator, fr.denominator, axis=-1)


def cut(x: np.ndarray, t: np.ndarray, win: tuple, fs: float) -> np.ndarray:
    i0 = int(np.argmin(np.abs(t - win[0])))
    n = int(round((win[1] - win[0]) * fs))
    return x[..., i0: i0 + n]


# ---------------------------------------------------------------- spectral Granger

def hann(n: int) -> np.ndarray:
    # MATLAB/FieldTrip hanning(n): 0.5*(1-cos(2*pi*k/(n+1))), k = 1..n
    k = np.arange(1, n + 1)
    return 0.5 * (1 - np.cos(2 * np.pi * k / (n + 1)))


def fourier(x: np.ndarray, fs: float = 40.0, pad: float = 20.0) -> tuple[np.ndarray, np.ndarray]:
    """Hann-tapered FFT, padded to ``pad`` s, of trials x channels x time; frequencies 0..fs/2."""
    n = x.shape[-1]
    nfft = int(round(pad * fs))
    x = x - x.mean(-1, keepdims=True)
    F = np.fft.rfft(x * hann(n), n=nfft, axis=-1)
    return F, np.fft.rfftfreq(nfft, 1 / fs)


def trial_csd(F: np.ndarray) -> np.ndarray:
    """Per-trial cross-spectra, trials x freqs x ch x ch, from trials x ch x freqs."""
    Ft = np.moveaxis(F, 1, -1)  # trials x freq x ch
    return Ft[..., :, None] * np.conj(Ft[..., None, :])


def _inv2(A):
    a, b, c, d = A[..., 0, 0], A[..., 0, 1], A[..., 1, 0], A[..., 1, 1]
    det = a * d - b * c
    out = np.empty_like(A)
    out[..., 0, 0] = d / det
    out[..., 0, 1] = -b / det
    out[..., 1, 0] = -c / det
    out[..., 1, 1] = a / det
    return out


def _mul2(A, B):
    out = np.empty(np.broadcast_shapes(A.shape, B.shape), dtype=np.result_type(A, B))
    for i in range(2):
        for j in range(2):
            out[..., i, j] = A[..., i, 0] * B[..., 0, j] + A[..., i, 1] * B[..., 1, j]
    return out


def wilson(S: np.ndarray, tol: float = 1e-5, maxit: int = 100):
    """Wilson's spectral factorisation of 2x2 spectra (batch x freqs 0..Nyquist x 2 x 2).

    Follows FieldTrip's sfactorization_wilson: two-sided spectrum, Cholesky start from the
    lag-0 covariance, plus-operator with the upper triangle of half the lag-0 term, at most
    100 iterations (FieldTrip's default ``niter``), each spectrum stopping when its psi changes
    by less than 1e-5 of its size (a standard tolerance; on these data GC then differs from the
    fully converged value by less than 1e-5, far below the ΔGranger values at stake). Returns
    the transfer function H (unit lag-0) and the noise covariance Z (up to a constant, which
    GC does not depend on).
    """
    S = np.asarray(S)
    B, nf = S.shape[:2]
    N = 2 * (nf - 1)
    Sf = np.concatenate([S, np.conj(S[:, -2:0:-1])], axis=1)
    gam = np.fft.ifft(Sf, axis=1).real
    g0 = gam[:, 0]
    h = np.linalg.cholesky(g0).swapaxes(-1, -2)  # upper, h' h = g0 (MATLAB chol)
    psi = np.repeat(h[:, None].astype(complex), N, axis=1)
    I = np.eye(2)
    active = np.arange(B)
    for _ in range(maxit):
        ps = psi[active]
        pinv = _inv2(ps)
        g = _mul2(_mul2(pinv, Sf[active]), np.conj(pinv).swapaxes(-1, -2)) + I
        gm = np.fft.ifft(g, axis=1)
        b0 = 0.5 * gm[:, 0]
        gm[:, 0] = np.triu(b0)
        gm[:, N // 2 + 1:] = 0
        gp = np.fft.fft(gm, axis=1)
        new = _mul2(ps, gp)
        err = np.abs(new - ps).sum(-2).max(-1).max(-1) / np.abs(ps).sum(-2).max(-1).max(-1)
        psi[active] = new
        active = active[err >= tol]
        if len(active) == 0:
            break
    A = np.fft.ifft(psi, axis=1).real
    A0 = A[:, 0]
    Z = A0 @ A0.swapaxes(-1, -2)
    H = _mul2(psi[:, : nf], _inv2(A0.astype(complex))[:, None])
    return H, Z


def granger_from_csd(S: np.ndarray) -> np.ndarray:
    """GC spectra of a 2x2 CSD (batch x freqs x 2 x 2): out[:, 0] is 0->1, out[:, 1] is 1->0."""
    H, Z = wilson(S)
    Smod = _mul2(_mul2(H, Z[:, None]), np.conj(H).swapaxes(-1, -2))
    out = np.empty((S.shape[0], 2, S.shape[1]))
    for to, frm, k in [(1, 0, 0), (0, 1, 1)]:
        Sii = Smod[..., to, to].real
        zz = Z[:, frm, frm] - Z[:, to, frm] ** 2 / Z[:, to, to]
        out[:, k] = np.log(Sii / (Sii - zz[:, None] * np.abs(H[..., to, frm]) ** 2))
    return out


def granger(x_hipp: np.ndarray, x_ctx: np.ndarray, fs: float = 40.0):
    """GC hipp->cortex and cortex->hipp over trials (trials x time at ``fs``)."""
    F, f = fourier(np.stack([x_hipp, x_ctx], axis=1), fs)
    S = trial_csd(F).mean(0)
    g = granger_from_csd(S[None])[0]
    return dict(freq=f, hc=g[0], ch=g[1], dg=g[0] - g[1])


def granger_direction_null(x_hipp, x_ctx, n_perm: int, rng, fs: float = 40.0, batch: int = 50):
    """ΔGranger null: the two channels swapped at random in each trial (Methods, Statistics 1)."""
    F, f = fourier(np.stack([x_hipp, x_ctx], axis=1), fs)
    Si = trial_csd(F)  # trials x freq x 2 x 2
    ntr, nf = Si.shape[:2]
    a = Si.reshape(ntr, -1)
    b = Si[..., ::-1, ::-1].reshape(ntr, -1)
    out = []
    for b0 in range(0, n_perm, batch):
        nb = min(batch, n_perm - b0)
        sw = (rng.random((nb, ntr)) < 0.5).astype(float)
        S = ((sw @ b + (1 - sw) @ a) / ntr).reshape(nb, nf, 2, 2)
        g = granger_from_csd(S)
        out.append(g[:, 0] - g[:, 1])
    return np.concatenate(out), f


def band_value(f, dg, band=(4, 8), how="mean", period="enc"):
    """ΔGranger over a band: mean (reading d1) or the extreme (d2: min in encoding, max in maintenance)."""
    sel = (f >= band[0]) & (f <= band[1])
    v = dg[..., sel]
    if how == "mean":
        return v.mean(-1)
    return v.min(-1) if period == "enc" else v.max(-1)


def runs(mask: np.ndarray, f: np.ndarray) -> list[tuple[float, float]]:
    """Contiguous runs of True in ``mask`` as (first, last) frequency."""
    out, start = [], None
    for i, m in enumerate(mask):
        if m and start is None:
            start = i
        if (not m or i == len(mask) - 1) and start is not None:
            end = i if m else i - 1
            out.append((round(float(f[start]), 2), round(float(f[end]), 2)))
            start = None
    return out


# ---------------------------------------------------------------- tests

def paired_signflip(a: np.ndarray, b: np.ndarray, n_perm: int | None, rng=None) -> float:
    """Two-sided paired permutation test of mean(a - b) by sign flips.

    ``n_perm=None`` enumerates all 2^n flips (exact p); otherwise ``n_perm`` random flips
    (Methods, Statistics, paragraph 5: N = 200), with p = (1 + #|null| >= |obs|) / (1 + n).
    """
    d = np.asarray(a) - np.asarray(b)
    obs = abs(d.mean())
    n = len(d)
    if n_perm is None:
        signs = 1 - 2 * ((np.arange(2 ** n)[:, None] >> np.arange(n)) & 1)
        null = np.abs((signs * d).mean(1))
        return float((null >= obs - 1e-15).mean())
    signs = rng.choice([-1, 1], size=(n_perm, n))
    null = np.abs((signs * d).mean(1))
    return float((1 + (null >= obs - 1e-15).sum()) / (1 + n_perm))


# ---------------------------------------------------------------- PSD and PLV

def tfr_power(x: np.ndarray, fs: float, freqs: np.ndarray, t: np.ndarray, tstep: float = 0.1):
    """Per-trial multitaper power (Methods, Power spectral density), trials x ch x freqs x times.

    Windows of 10 cycles and 0.2 x f smoothing give 3 tapers, i.e. MNE's time_bandwidth = 4.
    """
    from mne.time_frequency import tfr_array_multitaper
    dec = int(round(tstep * fs))
    P = tfr_array_multitaper(x, sfreq=fs, freqs=freqs, n_cycles=np.full(len(freqs), 10.0),
                             time_bandwidth=4.0, output="power", decim=dec, n_jobs=1, verbose=False)
    return P, t[::dec][: P.shape[-1]]


def baseline_mask(freqs: np.ndarray, tt: np.ndarray, t_first: float = -6.0) -> np.ndarray:
    """Fixation times [-6 -5) whose 10-cycle window lies inside the data (freqs x times).

    The epochs start at -6 s, so at -6 s half of each window would fall before the data; those
    times are left out of the baseline (a standard choice).
    """
    fix = (tt >= WINDOWS["fix"][0]) & (tt < WINDOWS["fix"][1])
    return fix[None] & ((tt[None] - 5.0 / freqs[:, None]) >= t_first - 1e-9)


def relative(P: np.ndarray, freqs: np.ndarray, tt: np.ndarray) -> np.ndarray:
    """(P - P_fix) / P_fix of trial-averaged power (Methods, PSD), ch x freqs x times."""
    Pm = P.mean(0)
    m = baseline_mask(freqs, tt)
    base = np.stack([Pm[:, i, m[i]].mean(-1) for i in range(len(freqs))], axis=1)[..., None]
    return (Pm - base) / base


def tf_mean(R: np.ndarray, freqs, tt, band, win, how="mean"):
    """Mean (or max) of a relative TFR over a band and a time window, per channel."""
    fm = (freqs >= band[0]) & (freqs <= band[1])
    tm = (tt >= win[0]) & (tt < win[1])
    v = R[..., fm, :][..., tm]
    return v.mean((-1, -2)) if how == "mean" else v.max((-1, -2))


def multitaper_fourier(x: np.ndarray, fs: float, n_tapers: int = 2):
    """Fourier coefficients with ``n_tapers`` DPSS tapers at 1 Hz resolution (pad to 1 s)."""
    from scipy.signal.windows import dpss
    n = x.shape[-1]
    nw = (n_tapers + 1) / 2
    tap = dpss(n, nw, n_tapers)
    x = x - x.mean(-1, keepdims=True)
    nfft = max(n, int(fs))
    F = np.fft.rfft(x[..., None, :] * tap, n=nfft, axis=-1)  # ... x tapers x freq
    return F, np.fft.rfftfreq(nfft, 1 / fs)


def plv(Fa: np.ndarray, Fb: np.ndarray) -> np.ndarray:
    """PLV over trials and tapers (Methods, Phase-locking value): |mean(Xa Xb* / |Xa Xb|)|.

    Fa, Fb: trials x tapers x freqs. With ``per_trial`` unit phasors the PLV of any subset of
    trials is the modulus of their mean, which the permutation tests use.
    """
    return np.abs(phasors(Fa, Fb).mean(0))


def phasors(Fa: np.ndarray, Fb: np.ndarray) -> np.ndarray:
    """Per-trial unit cross-phasors averaged over tapers (trials x freqs)."""
    c = Fa * np.conj(Fb)
    return (c / np.abs(c)).mean(1)


# ---------------------------------------------------------------- one subject

ECOG_SUBJECTS = {"sub-10": 1, "sub-11": 2, "sub-12": 3, "sub-13": 4}  # paper's Participants 1 to 4


def load_subject(sub: str, ev: pd.DataFrame) -> dict:
    """Everything the GC, PSD and PLV analyses use for one subject.

    - ``lcmv``: the derivative file; its trials are matched to the events in order
      (``deriv_rows``, checked against the raw EEG in the notebook).
    - ``ieeg``: [-6 2) s of each trial of set size 6 or 8 (any response), at 500 Hz. For the
      four ECoG participants every depth and ECoG contact is read, otherwise only the contacts
      the hippocampal readings use.
    """
    e = ev[ev["sub"] == sub]
    hc = hippocampal_channels(sub)
    el = electrodes(sub)
    if sub in ECOG_SUBJECTS:
        chans = list(el.label)
    else:
        chans = sorted({hc["h1"], *hc["h2"], *hc["h3"], hc["ref"]})
    rows = e[e.SetSize.isin([6, 8])]
    D = load_trials(sub, rows, chans, t0=-6.0, t1=2.0)
    L = load_lcmv(sub)
    n = L["enc"]["data"].shape[0]
    cand = e[e.SetSize.isin([6, 8]) & (e.Correct == 1)]
    if len(cand[cand.Artifact == 0]) == n:
        deriv = cand[cand.Artifact == 0]
    else:
        deriv = cand
    return dict(sub=sub, hc=hc, electrodes=el, rows=rows.reset_index(drop=True), ieeg=D,
                lcmv=L, deriv_rows=deriv.reset_index(drop=True))


# ---------------------------------------------------------------- GC with the derivative sources

AREAS = ["AC", "DLPFC", "OFC", "PPC", "V1"]


def matched_trials(S: dict) -> tuple[np.ndarray, np.ndarray]:
    """Indices into the derivative trials and into the iEEG trials of the GC method's trials.

    The derivative trials are matched to the events in order; trials flagged ``Artifact`` are
    dropped (the GC method's trial set).
    """
    key = S["rows"].ses + ":" + S["rows"].nTrial.astype(str)
    pos = {k: i for i, k in enumerate(key)}
    dr = S["deriv_rows"]
    keep = np.flatnonzero(dr.Artifact.values == 0)
    ii = np.array([pos[f"{dr.ses[j]}:{dr.nTrial[j]}"] for j in keep])
    return keep, ii


def hipp40(S: dict, idx: np.ndarray) -> dict:
    """Hippocampal readings at 40 Hz, cut to encoding and maintenance; h3 is a list."""
    D = S["ieeg"]
    hs = hipp_signals(D["data"][idx].astype(float), D["channels"], S["hc"])
    t40 = -6.0 + np.arange(int(8 * 40)) / 40
    out = {}
    for h in ["h1", "h2", "h3"]:
        xs = hs[h] if h == "h3" else [hs[h]]
        for per in ["enc", "maint"]:
            out[(h, per)] = [cut(to_fs(x, D["fs"]), t40, WINDOWS[per], 40) for x in xs]
    return out


def source40(S: dict, keep: np.ndarray, label: str, per: str) -> np.ndarray:
    L = S["lcmv"][per]
    x = L["data"][keep, L["label"].index(label)]
    return to_fs(x, L["fs"])[:, :80]


def gc_reading(hx: list, cx: np.ndarray, trials=None) -> dict:
    """GC spectra for one hippocampal reading (h3: mean of the spectra over its channels)."""
    gs = [granger(h if trials is None else h[trials], cx if trials is None else cx[trials]) for h in hx]
    f = gs[0]["freq"]
    hc = np.mean([g["hc"] for g in gs], 0)
    ch = np.mean([g["ch"] for g in gs], 0)
    return dict(freq=f, hc=hc, ch=ch, dg=hc - ch)


def gc_subsample(hx: list, cx: np.ndarray, frac: float, n_draws: int, rng) -> dict:
    """GC on ``frac`` of the trials drawn at random, ``n_draws`` times (Methods, Statistics 4).

    Returns the per-draw direction spectra (draws x freqs), averaged over h3's channels.
    """
    ntr = cx.shape[0]
    k = max(2, int(round(frac * ntr)))
    draws = np.stack([rng.choice(ntr, k, replace=False) for _ in range(n_draws)])
    hcs, chs = [], []
    for h in hx:
        F, f = fourier(np.stack([h, cx], axis=1))
        Si = trial_csd(F)
        S = Si[draws].mean(1)
        g = granger_from_csd(S)
        hcs.append(g[:, 0]); chs.append(g[:, 1])
    return dict(freq=f, hc=np.mean(hcs, 0), ch=np.mean(chs, 0), k=k)


# ---------------------------------------------------------------- ECoG participants

def ecog_signals(S: dict, idx: np.ndarray) -> dict:
    """ECoG contacts (trials x time at 500 Hz) re-referenced to the ECoG reference contact."""
    D = S["ieeg"]
    c = {n: i for i, n in enumerate(D["channels"])}
    ref = D["data"][idx, c[S["hc"]["ecog_ref"]]].astype(float)
    el = S["electrodes"]
    return {r.label: D["data"][idx, c[r.label]].astype(float) - ref for r in el[el.ecog].itertuples()}


def window40(x: np.ndarray, per: str, fs: int = 500) -> np.ndarray:
    t40 = -6.0 + np.arange(int(8 * 40)) / 40
    return cut(to_fs(x, fs), t40, WINDOWS[per], 40)


def gc_test(hx: list, cx: np.ndarray, n_perm: int, seed: int) -> dict:
    """ΔGranger and its direction-swap null for one hippocampal reading (h3: mean over channels).

    The same random swaps are used for each channel of h3.
    """
    dg, nulls = [], []
    for h in hx:
        r = granger(h, cx)
        nl, f = granger_direction_null(h, cx, n_perm, np.random.default_rng(seed))
        dg.append(r["dg"]); nulls.append(nl)
    return dict(freq=f, dg=np.mean(dg, 0), null=np.mean(nulls, 0))


def significant_bands(f, dg, null, period: str, lo=5, hi=95, fmin=4, fmax=20):
    """Frequencies where ΔGranger is beyond the null percentile in the period's direction.

    Reading c1 of the claims file (per frequency). Returns the runs of significant bins and
    a cluster-mass p for each run (reading c2: contiguous bins, the mass of (dg - threshold)
    compared with the largest cluster mass of each null draw).
    """
    sel = (f >= fmin) & (f <= fmax)
    f, dg, null = f[sel], dg[sel], null[:, sel]
    if period == "enc":
        thr = np.percentile(null, lo, axis=0); sig = dg < thr; ex = thr - dg
        nex = thr[None] - null
    else:
        thr = np.percentile(null, hi, axis=0); sig = dg > thr; ex = dg - thr
        nex = null - thr[None]

    def masses(e):
        out, cur = [], 0.0
        for v in e:
            if v > 0:
                cur += v
            elif cur > 0:
                out.append(cur); cur = 0.0
        if cur > 0:
            out.append(cur)
        return out

    nullmax = np.array([max(masses(e), default=0.0) for e in nex])
    clusters = []
    for (a, b), m in zip(runs(sig, f), masses(np.where(sig, ex, 0))):
        clusters.append(dict(band=(a, b), mass=m, p=float((1 + (nullmax >= m).sum()) / (1 + len(nullmax)))))
    return dict(bands=runs(sig, f), clusters=clusters)


# ---------------------------------------------------------------- group statistics

def group_spectra_test(a: np.ndarray, b: np.ndarray, n_rand: int, rng, paired: bool = False,
                       alpha: float = 0.05) -> dict:
    """Monte Carlo t-test per frequency of a against b (participants x freqs), FDR corrected.

    As FieldTrip's ft_freqstatistics with method 'montecarlo', correctm 'fdr', two-sided
    (claims file, fig4a-group-gc-reversal; code statistics_fr.m): independent-samples t by
    default (labels shuffled across the pooled values), dependent-samples t when ``paired``
    (signs flipped within participants). Returns t, the Monte Carlo p and the FDR mask.
    """
    def tstat(x, y):
        if paired:
            d = x - y
            return d.mean(0) / (d.std(0, ddof=1) / np.sqrt(len(d)))
        nx, ny = len(x), len(y)
        sp = ((nx - 1) * x.var(0, ddof=1) + (ny - 1) * y.var(0, ddof=1)) / (nx + ny - 2)
        return (x.mean(0) - y.mean(0)) / np.sqrt(sp * (1 / nx + 1 / ny))

    t = tstat(a, b)
    null = np.empty((n_rand, a.shape[1]))
    for i in range(n_rand):
        if paired:
            s = rng.choice([-1, 1], size=(len(a), 1))
            d = (a - b) * s
            null[i] = tstat(d, np.zeros_like(d))
        else:
            pool = np.concatenate([a, b])
            perm = rng.permutation(len(pool))
            null[i] = tstat(pool[perm[: len(a)]], pool[perm[len(a):]])
    p = (1 + (np.abs(null) >= np.abs(t)[None]).sum(0)) / (1 + n_rand)
    # Benjamini-Hochberg
    m = len(p)
    order = np.argsort(p)
    passed = p[order] <= alpha * np.arange(1, m + 1) / m
    k = np.max(np.flatnonzero(passed)) + 1 if passed.any() else 0
    sig = np.zeros(m, bool)
    sig[order[:k]] = True
    return dict(t=t, p=p, sig=sig)


def dunn_bonferroni(groups: dict) -> pd.DataFrame:
    """Dunn's test after Kruskal-Wallis, Bonferroni corrected over all pairs."""
    from itertools import combinations
    from scipy.stats import norm, rankdata
    names = list(groups)
    vals = np.concatenate([groups[k] for k in names])
    r = rankdata(vals)
    N = len(vals)
    _, cnt = np.unique(vals, return_counts=True)
    tie = (cnt ** 3 - cnt).sum() / (12 * (N - 1))
    mean_r, pos = {}, 0
    for k in names:
        n = len(groups[k]); mean_r[k] = r[pos: pos + n].mean(); pos += n
    rows = []
    pairs = list(combinations(names, 2))
    for a, b in pairs:
        se = np.sqrt((N * (N + 1) / 12 - tie) * (1 / len(groups[a]) + 1 / len(groups[b])))
        z = (mean_r[a] - mean_r[b]) / se
        rows.append(dict(a=a, b=b, z=z, p_bonf=min(1.0, 2 * norm.sf(abs(z)) * len(pairs))))
    return pd.DataFrame(rows)


def trial_csds(hx: np.ndarray, cx: np.ndarray) -> np.ndarray:
    F, _ = fourier(np.stack([hx, cx], axis=1))
    return trial_csd(F)


def spatial_test(csd_task: dict, csd_fix: dict, n_iter: int, rng, band=(4, 8), fix_scale: float = 1.0) -> dict:
    """Scalar product of grid ΔGranger vectors from two random halves of the trials (Methods,
    Statistics, paragraph 2), and its null with each trial's window drawn at random from
    fixation or the task period.

    csd_task, csd_fix: contact -> per-trial CSDs (trials x freqs x 2 x 2). ΔGranger of a
    contact is the mean over ``band`` (reading d1). ``fix_scale`` multiplies the fixation CSDs
    so that windows of different length enter the null on one scale: with the same 20 s
    padding, the power of a window grows with its number of samples, so a 1 s fixation window
    is scaled by 2 against a 2 s task window (a standard choice).
    """
    contacts = list(csd_task)
    ntr = csd_task[contacts[0]].shape[0]
    h = ntr // 2
    WA = np.zeros((n_iter, ntr)); WB = np.zeros((n_iter, ntr))
    for k in range(n_iter):
        p = rng.permutation(ntr)
        WA[k, p[:h]] = 1.0 / h
        WB[k, p[h: 2 * h]] = 1.0 / h
    choice = rng.random((n_iter, ntr)) < 0.5  # True: fixation window in the null
    f = np.fft.rfftfreq(800, 1 / 40.0)
    sel = (f >= band[0]) & (f <= band[1])
    vecs = {k: np.zeros((n_iter, len(contacts))) for k in ["A", "B", "A0", "B0"]}
    for j, c in enumerate(contacts):
        T = csd_task[c].reshape(ntr, -1)
        Fx = fix_scale * csd_fix[c].reshape(ntr, -1)
        nf = csd_task[c].shape[1]
        batch = []
        for W in (WA, WB):
            batch.append(W @ T)
        for W in (WA, WB):
            batch.append((W * ~choice) @ T + (W * choice) @ Fx)
        S = np.concatenate(batch).reshape(4 * n_iter, nf, 2, 2)
        g = granger_from_csd(S)
        dg = (g[:, 0] - g[:, 1])[:, sel].mean(1).reshape(4, n_iter)
        for i, k in enumerate(["A", "B", "A0", "B0"]):
            vecs[k][:, j] = dg[i]
    true = (vecs["A"] * vecs["B"]).sum(1)
    null = (vecs["A0"] * vecs["B0"]).sum(1)
    return dict(true=true, null=null)


# ---------------------------------------------------------------- LCMV filters from the derivatives

def lcmv_weights(S: dict) -> dict:
    """Spatial filter of each virtual sensor, per period, recovered from the derivative file.

    Each virtual sensor is fitted by least squares on the file's own scalp channels over all
    trials and samples; R² = 1 means the sensor is a fixed linear combination of the scalp
    channels (an LCMV filter is one). Returns {(period, area): (weights, R²)}.
    """
    out = {}
    for per in ["enc", "maint"]:
        L = S["lcmv"][per]
        X = L["data"]
        A = X[:, 5:].transpose(1, 0, 2).reshape(X.shape[1] - 5, -1).T
        for k, area in enumerate(L["label"][:5]):
            y = X[:, k].ravel()
            w = np.linalg.lstsq(A, y, rcond=None)[0]
            out[(per, area)] = (w, 1 - np.sum((y - A @ w) ** 2) / np.sum((y - y.mean()) ** 2))
    return out


def eeg_sources(sub: str, S: dict, rows: pd.DataFrame, W: dict, areas=("AC",)) -> dict:
    """Virtual sensors computed from the raw scalp EEG of ``rows`` with the recovered filters.

    The raw EEG ([-6 2) s at 500 Hz, as the iEEG) is re-referenced to the averaged mastoids, as the
    derivative's scalp channels are (A1 = -A2, checked in the notebook), and each period's
    filter is applied. Returns {(area, period): trials x samples at 40 Hz, cut to the period}.
    """
    scalp = S["lcmv"]["enc"]["label"][5:]
    D = load_trials(sub, rows, scalp, modality="eeg", t0=-6.0, t1=2.0, fs_out=500)
    x = D["data"].astype(float)
    x = x - x[:, [scalp.index("A1"), scalp.index("A2")]].mean(1, keepdims=True)
    out = {}
    for area in areas:
        for per in ["enc", "maint"]:
            src = np.einsum("c,tcs->ts", W[(per, area)][0], x)
            out[(area, per)] = window40(src, per)
    return out
