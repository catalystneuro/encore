"""Loading and physiology features for dandiset 001065 (Dembrow, Sawchuk et al. 2024, Cell Reports).

The dandiset holds one MIES current clamp NWB file per neuron. Per-cell labels (area,
preparation, subclass, virus) are not in the files; they come from the per-cell tables of the
paper's code (Zenodo record 13749343), matched by the file's cell_id, which is the tables'
cell_name.

Where each parameter comes from:

- Feature definitions: STAR Methods, "Neurophysiology features" (quoted in the docstring of
  each function), as summarised in the opening comment of the claims file.
- Spike threshold, 20 V/s: STAR Methods ("the voltage where the first derivative of the voltage
  response exceeded 20 V/s").
- MCx regions (M1, M1-trunk, M1-Hand-wrist, SFG): the code, UMAPprojections_020724.ipynb, as the
  claims file says.
- Standard choices for details that the paper and code leave open, named in the claims file's
  opening comment: the peak of a hyperpolarizing step is its most negative voltage and the
  steady state is the mean of its last 100 ms; the linear portion of the V-I relation is every
  hyperpolarizing step down to -200 pA (all negative steps when the protocol was scaled and
  fewer than two lie in that range); the impedance profiles of the chirp sweeps are averaged;
  the fAHP window runs from the spike peak to the next spike or 10 ms.
- Standard choices of this attempt (said so where used), for details that cannot be read from
  the paper: a spike is a crossing of 20 V/s whose peak, within 3 ms, is above -20 mV and more
  than 20 mV above threshold; voltage is low-pass filtered at 10 kHz (or 0.4 of the sampling
  rate when lower) before dV/dt, as is usual for patch clamp features; files hold several runs
  of a protocol (repeats, drug wash, a 200 pA series to 4 nA), and the first run is used (a run
  is a block of consecutive sweeps of one protocol), except for the 1 s depolarizing steps,
  where runs are split into series of increasing amplitude and the first series that reaches
  1 nA is used (else the longest), since in some cells the
  first series was stopped early and the paper's table follows a later complete one;
  impedance is computed from 0.2 Hz, smoothed with a 0.5 Hz running mean, and read between
  0.5 and 40 Hz; phase is in degrees.
"""
import re
import numpy as np
import pandas as pd
import requests
import h5py
import remfile
from scipy import signal

DANDISET = "001065"
VERSION = "0.241028.1559"
API = "https://api.dandiarchive.org/api"
ZENODO = "https://zenodo.org/records/13749343/files/"
MCX_REGIONS = ["M1", "M1-trunk", "M1-Hand-wrist", "SFG"]

DV_THRESH = 20.0  # V/s = mV/ms, STAR Methods


def list_assets():
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r.get("next")
    return pd.DataFrame(out)


def s3_url(asset_id):
    return requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True,
                         timeout=60).url


def zenodo_csv(name):
    return pd.read_csv(ZENODO + name + "?download=1")


def zenodo_pickle(name):
    import pickle, io
    return pickle.load(io.BytesIO(requests.get(ZENODO + name + "?download=1", timeout=120).content))


def protocol(desc):
    """Map a MIES stimulus name to a protocol class."""
    s = re.sub(r"_DA_0$", "", desc)
    s = re.sub(r"^DA\d\d_", "", s)
    s = re.sub(r"^X(?=\d)", "", s).lower()
    if "chirp" in s:
        return "chirp"
    if s.startswith("vi_fine") or s.startswith("iv_rest"):
        return "vi"
    if s in ("fi", "fi_short_rest"):
        return "fi"
    if s.startswith("short_squar"):
        return "short"
    if s.startswith("10s_spike") or s.startswith("10secmax"):
        return "s10"
    return None


def main_step(i, rate, largest=False):
    """Onset index, offset index and amplitude (pA) of the longest constant epoch of the
    command, which skips the test pulse (or, with largest, of the epoch of largest positive
    amplitude, for the 3 ms steps, which are shorter than the 10 ms test pulse)."""
    on = np.abs(i) > 1
    d = np.flatnonzero(np.diff(np.r_[0, on.astype(int), 0]))
    if len(d) == 0:
        return None, None, 0.0
    segs = [(d[j], d[j + 1]) for j in range(0, len(d), 2)]
    if largest:
        a, b = max(segs, key=lambda s: np.median(i[s[0]:s[1]]))
    else:
        a, b = max(segs, key=lambda s: s[1] - s[0])
    return a, b, float(np.median(i[a:b]))


def file_meta(f):
    """Subject and electrode metadata of an open file, and the sampling rates of its sweeps."""
    def rd(p):
        v = f[p][()]
        v = v[0] if hasattr(v, "__len__") and not isinstance(v, (bytes, str)) else v
        return v.decode() if isinstance(v, bytes) else v
    return dict(subject_id=rd("general/subject/subject_id"), species=rd("general/subject/species"),
                sex=rd("general/subject/sex"), age=rd("general/subject/age"),
                cell_id=rd("general/intracellular_ephys/electrode_0/cell_id"),
                n_sweeps=len(f["acquisition"]))


def read_cell(asset_id, want=("chirp", "vi", "fi", "short", "s10"), with_meta=False):
    """Stream one file and return the sweeps of the wanted protocols: a list of dicts with the
    protocol, sweep number, sampling rate, command (pA) and voltage (mV)."""
    f = h5py.File(remfile.File(s3_url(asset_id)), "r")
    acq, stim = f["acquisition"], f["stimulus/presentation"]
    out = []
    meta = file_meta(f)
    for k in sorted(acq.keys()):
        g = acq[k]
        p = protocol(g.attrs.get("stimulus_description", ""))
        if p not in want:
            continue
        sk = k.replace("_AD", "_DA")
        if sk not in stim:
            continue
        rate = float(g["starting_time"].attrs["rate"])
        dv = g["data"]
        v = dv[:].astype(float) * float(dv.attrs["conversion"]) * 1e3
        di = stim[sk]["data"]
        i = di[:].astype(float) * float(di.attrs["conversion"]) * 1e12
        n = min(len(v), len(i))
        fin = np.isfinite(v[:n]) & np.isfinite(i[:n])
        if not fin.any():
            continue
        n = int(np.flatnonzero(fin)[-1]) + 1  # sweeps stopped early end in NaN
        v, i = np.nan_to_num(v[:n], nan=np.nanmedian(v[:n])), np.nan_to_num(i[:n])
        out.append(dict(protocol=p, sweep=int(re.findall(r"\d+", k)[0]), rate=rate,
                        i=i[:n], v=v[:n], desc=g.attrs.get("stimulus_description")))
    f.close()
    if with_meta:
        return out, meta
    return out


def runs(sweeps, p):
    """Blocks of consecutive sweeps of protocol p (by sweep number order in the file)."""
    out, cur, last = [], [], None
    allsw = sorted(sweeps, key=lambda s: s["sweep"])
    for s in allsw:
        if s["protocol"] == p:
            cur.append(s)
        elif cur:
            out.append(cur)
            cur = []
    if cur:
        out.append(cur)
    return out


def fi_series(sweeps):
    """Series of 1 s depolarizing steps: each run of the FI protocol split where the step
    amplitude stops increasing (a run often holds a 50 pA series and then a 200 pA one)."""
    out = []
    for run in runs(sweeps, "fi"):
        cur, last = [], -np.inf
        for s in run:
            amp = main_step(s["i"], s["rate"])[2]
            if amp <= last and cur:
                out.append(cur)
                cur = []
            cur.append(s)
            last = amp
        if cur:
            out.append(cur)
    return out


# ---------------------------------------------------------------- spikes
def filt(v, rate):
    fc = min(10000.0, 0.4 * rate)
    b, a = signal.bessel(4, fc / (rate / 2), "low")
    return signal.filtfilt(b, a, v)


def detect_spikes(v, rate, t0, t1):
    """Spikes between sample indices t0 and t1. Returns a list of dicts: threshold index and
    voltage, peak index and voltage, max and min dV/dt (V/s), half-width (ms) and fAHP (mV,
    relative to threshold). Threshold is where dV/dt exceeds 20 V/s (STAR Methods)."""
    vf = filt(v, rate)
    dvdt = np.gradient(vf) * rate / 1000.0  # mV/ms = V/s
    above = dvdt > DV_THRESH
    up = np.flatnonzero(above[1:] & ~above[:-1]) + 1
    up = up[(up >= t0) & (up < t1)]
    w3 = int(0.003 * rate)
    spikes, last_peak = [], -1
    for u in up:
        if u <= last_peak:
            continue
        pk = u + int(np.argmax(vf[u:u + w3]))
        if vf[pk] < -20 or vf[pk] - vf[u] < 20:
            continue
        spikes.append(dict(ti=u, tv=vf[u], pi=pk, pv=vf[pk]))
        last_peak = pk + int(0.0005 * rate)
    for j, s in enumerate(spikes):
        nxt = spikes[j + 1]["ti"] if j + 1 < len(spikes) else len(v)
        end = min(nxt, s["pi"] + int(0.010 * rate), len(v))
        s["max_dvdt"] = float(dvdt[s["ti"]:s["pi"] + 1].max())
        s["min_dvdt"] = float(dvdt[s["pi"]:end].min()) if end > s["pi"] else np.nan
        s["trough"] = float(vf[s["pi"]:end].min()) if end > s["pi"] else np.nan
        s["fahp"] = s["trough"] - s["tv"]
        half = s["tv"] + (s["pv"] - s["tv"]) / 2
        seg = vf[s["ti"]:end]
        k_pk = s["pi"] - s["ti"]
        rise = np.flatnonzero(seg[:k_pk + 1] >= half)
        fall = np.flatnonzero(seg[k_pk:] <= half)
        if len(rise) and len(fall):
            r0 = rise[0]
            f0 = k_pk + fall[0]
            # linear interpolation of the crossings
            tr = r0 - 1 + (half - seg[r0 - 1]) / (seg[r0] - seg[r0 - 1]) if r0 > 0 else r0
            tf = f0 - 1 + (seg[f0 - 1] - half) / (seg[f0 - 1] - seg[f0]) if f0 > 0 else f0
            s["hw"] = (tf - tr) / rate * 1000.0
        else:
            s["hw"] = np.nan
    return spikes


# ---------------------------------------------------------------- features
def fi_features(sweeps):
    """1 s depolarizing steps (STAR Methods: "We measured the number of spikes and the maximum
    instantaneous firing rate in response to each current injection. Maximum instantaneous
    firing rate was defined as 1/interspike interval(min) ... Maximum gain measurements
    corresponded to the maximum instantaneous slope and initial gain corresponded to the
    instantaneous slope where each neuron began firing. Single action potential properties were
    measured from the voltage response to the lowest current injection amplitude that produced a
    spike.") The first series that reaches 1 nA (else the longest); first sweep at each
    amplitude."""
    rr = fi_series(sweeps)
    out = {}
    if not rr:
        return out, None
    # the first run that reaches 1 nA, else the longest run (standard choice of this attempt:
    # the paper's tables use a complete series where a first one was stopped early)
    def top(run):
        return max([main_step(s["i"], s["rate"])[2] for s in run] + [0])
    full = [run for run in rr if top(run) >= 999]
    run0 = full[0] if full else max(rr, key=len)
    steps = {}
    for s in run0:
        a, b, amp = main_step(s["i"], s["rate"])
        if a is None or amp <= 0 or (b - a) / s["rate"] < 0.9:
            continue
        amp = round(amp)
        if amp in steps:
            continue
        sp = detect_spikes(s["v"], s["rate"], a, b)
        steps[amp] = (s, a, b, sp)
    if not steps:
        return out, None
    amps = np.array(sorted(steps))
    n = np.array([len(steps[a][3]) for a in amps])
    def maxhz(sp, rate):
        if len(sp) < 2:
            return float(len(sp) > 0)  # the code's tables give 1 for a single spike
        return float(rate / np.diff([x["ti"] for x in sp]).min())
    hz = np.array([maxhz(steps[a][3], steps[a][0]["rate"]) for a in amps])
    out["fi_amps"], out["fi_n"], out["fi_hz"] = amps, n, hz
    if len(amps) > 1:
        di = np.diff(amps).astype(float)
        g = np.diff(n) / di
        gh = np.diff(hz) / di
        out["max_gain"] = float(g.max())
        out["max_ifreq_gain"] = float(gh.max())
        out["i_max_gain"] = float(amps[:-1][np.argmax(g)])
        dn = np.diff(n)
        out["gain_CV"] = float(np.std(dn) / np.mean(dn)) if np.mean(dn) != 0 else np.nan
        dh = np.diff(hz)
        out["inst_gain_CV"] = float(np.std(dh) / np.mean(dh)) if np.mean(dh) != 0 else np.nan
    # clock check: spikes over the whole sweep of the largest step, inside and outside the
    # command epoch, and the latency of the first spike after the command onset
    s, a, b, _ = steps[amps[-1]]
    ta = np.array([x["ti"] for x in detect_spikes(s["v"], s["rate"], 0, len(s["v"]))])
    out["clk_in"] = int(((ta >= a) & (ta < b)).sum()) if len(ta) else 0
    out["clk_out"] = int(((ta < a) | (ta >= b)).sum()) if len(ta) else 0
    out["clk_lat_ms"] = float((ta[ta >= a][0] - a) / s["rate"] * 1000) if (ta >= a).any() else np.nan
    first = np.flatnonzero(n > 0)
    if len(first) == 0:
        return out, None
    k = first[0]
    rheo = amps[k]
    out["threshold_current"] = float(rheo)
    # the slope from the step before the first suprathreshold one (claims file, fig6h); when
    # the first step already fires, from 0 pA and 0 spikes (standard choice of this attempt)
    i0, n0, h0 = (amps[k - 1], n[k - 1], hz[k - 1]) if k > 0 else (0.0, 0.0, 0.0)
    dI = float(amps[k] - i0)
    out["initial_gain"] = float((n[k] - n0) / dI)
    out["initial_ifreq_gain"] = float((hz[k] - h0) / dI)
    s, a, b, sp = steps[rheo]
    x = sp[0]
    out.update(AP_threshold=x["tv"], AP_peak=x["pv"], AP_amp=x["pv"] - x["tv"],
               max_dvdt=x["max_dvdt"], min_dvdt=x["min_dvdt"], f_AHP=x["fahp"], AP_HW=x["hw"],
               threshold_t=(x["ti"] - a) / s["rate"] * 1000.0)
    out["up_down_ratio"] = -x["max_dvdt"] / x["min_dvdt"]
    # spike train measures: the first train with at least 10 spikes (STAR Methods)
    tr = [a_ for a_ in amps if len(steps[a_][3]) >= 10]
    if tr:
        s, a, b, sp = steps[tr[0]]
        t = np.array([y["ti"] for y in sp]) / s["rate"]
        isi = np.diff(t)
        out["train_current"] = float(tr[0])
        out["SFA"] = float(isi[1] / isi[-1])
        out["CV"] = float(isi.std() / isi.mean())
        base = np.median(s["v"][:a])
        out["mAHP"] = float(np.min(filt(s["v"], s["rate"])[b:b + int(s["rate"])]) - base)
    return out, steps


def vi_features(sweeps):
    """1 s hyperpolarizing steps (STAR Methods: "Maximum and steady-state input resistance were
    calculated from the linear portion of the current voltage relationship in response to this
    protocol. Voltage sag was defined as the ratio of maximum to steady state input resistance.
    Rebound slope was defined as the slope of the rebound amplitude as a function of
    steady-state membrane potential.") Peak, steady state and the linear range are the claims
    file's standard choices."""
    rr = runs(sweeps, "vi")
    out = {}
    if not rr:
        return out
    rows = []
    seen = set()
    for s in rr[0]:
        a, b, amp = main_step(s["i"], s["rate"])
        if a is None or amp >= 0 or (b - a) / s["rate"] < 0.9:
            continue
        amp = round(amp)
        if amp in seen:
            continue
        seen.add(amp)
        vf = filt(s["v"], s["rate"])
        base = np.mean(vf[max(0, a - int(0.1 * s["rate"])):a])
        peak = np.min(vf[a:b])
        ss = np.mean(vf[b - int(0.1 * s["rate"]):b])
        post = vf[b:min(len(vf), b + int(0.3 * s["rate"]))]
        reb = np.max(post) - base if len(post) else np.nan
        rows.append((amp, base, peak - base, ss - base, ss, reb))
    if not rows:
        return out
    rows = np.array(rows)
    sel = rows[:, 0] >= -200
    if sel.sum() < 2:
        sel = np.ones(len(rows), bool)
    if sel.sum() >= 2:
        I = rows[sel, 0] / 1000.0  # nA
        out["MaxRn"] = float(np.polyfit(I, rows[sel, 2], 1)[0])  # mV/nA = MOhm
        out["SSRn"] = float(np.polyfit(I, rows[sel, 3], 1)[0])
        out["sag_ratio"] = out["MaxRn"] / out["SSRn"]
        ok = sel & np.isfinite(rows[:, 5])
        out["rebound"] = float(np.polyfit(rows[ok, 4], rows[ok, 5], 1)[0]) if ok.sum() >= 2 else np.nan
    out["rmp"] = float(np.median(rows[:, 1]))
    return out


def chirp_features(sweeps):
    """Chirp, 0.2 to 40 Hz in 20 s (STAR Methods: "Impedance amplitude (ZAP) and phase profiles
    (ZPP) were calculated as the ratio of the Fourier transform of the voltage response to the
    Fourier transform of the chirp. The frequency at which the maximum impedance occurred was
    defined as the resonant frequency (fR). Resonance strength was defined as the ratio of the
    maximum impedance to the impedance at .5 Hz. The 3 dB cutoff was defined as the frequency at
    which the ZAP attenuated to (sqrt(.5) Zmax). Total inductive phase was defined as the area
    under the inductive portion of the ZPP. Synchrony phase was defined the frequency at which
    the ZPP was 0.") Profiles of the valid sweeps of the first run are averaged (claims file,
    standard choice); sweeps with spikes or without a 20 s command are skipped."""
    rr = runs(sweeps, "chirp")
    out = {}
    Zs = []
    for run in rr:
        for s in run:
            i, v, rate = s["i"], s["v"], s["rate"]
            on = np.flatnonzero(np.abs(i) > 1)
            if len(on) == 0:
                continue
            a, b = on[0], on[-1]
            if (b - a) / rate < 19 or (b - a) / rate > 21:
                continue
            if len(detect_spikes(v, rate, a, b)):
                continue
            step = max(1, int(rate // 2000))  # 2 kHz is ample for 40 Hz
            vv = v[a:b:step] - np.mean(v[a:b:step])
            ii = i[a:b:step] - np.mean(i[a:b:step])
            fs = rate / step
            F = np.fft.rfftfreq(len(vv), 1 / fs)
            Z = np.fft.rfft(vv) / np.fft.rfft(ii) * 1e3  # mV/pA*1e3 = MOhm
            Zs.append((F, Z))
        if Zs:
            break  # first run with a valid sweep
    if not Zs:
        return out
    n = min(len(z[0]) for z in Zs)
    F = Zs[0][0][:n]
    Z = np.mean([z[1][:n] for z in Zs], axis=0)
    m = (F >= 0.2) & (F <= 40)
    F, Z = F[m], Z[m]
    df = F[1] - F[0]
    w = max(1, int(round(0.5 / df)))
    amp = pd.Series(np.abs(Z)).rolling(w, center=True, min_periods=1).mean().to_numpy()
    ph = pd.Series(np.degrees(np.angle(Z))).rolling(w, center=True, min_periods=1).mean().to_numpy()
    m = F >= 0.5
    F, amp, ph = F[m], amp[m], ph[m]
    k = int(np.argmax(amp))
    out["Fr"] = float(F[k])
    out["MaxZ"] = float(amp[k])
    out["RQ"] = float(amp[k] / amp[0])
    below = np.flatnonzero(amp[k:] <= np.sqrt(0.5) * amp[k])
    out["cutoff"] = float(F[k + below[0]]) if len(below) else np.nan
    pos = ph > 0
    out["Iphase"] = float(np.sum(ph[pos]) * df)
    cross = np.flatnonzero(pos[:-1] & ~pos[1:])
    out["phase0"] = float(F[cross[0]]) if len(cross) else np.nan
    out["n_chirp"] = len(Zs)
    return out


def short_features(sweeps):
    """3 ms steps (STAR Methods: "From this protocol, we measured the same single spike
    properties as described for the 1 s current step protocol"): the lowest amplitude of the
    first run that evokes a spike."""
    rr = runs(sweeps, "short")
    out = {}
    if not rr:
        return out
    best = None
    for s in rr[0]:
        a, b, amp = main_step(s["i"], s["rate"], largest=True)
        if a is None or amp <= 0:
            continue
        sp = detect_spikes(s["v"], s["rate"], a, min(len(s["v"]), b + int(0.01 * s["rate"])))
        if sp and (best is None or amp < best[0]):
            best = (amp, sp[0])
    if best:
        amp, x = best
        out.update(AP_short_i=float(amp), threshold_short=x["tv"], AP_peak_short=x["pv"],
                   AP_amp_short=x["pv"] - x["tv"], max_dvdt_short=x["max_dvdt"],
                   min_dvdt_short=x["min_dvdt"], halfwidth_short=x["hw"])
    return out


def extended_fi(sweeps):
    """1 s steps by 200 pA up to 4 nA (STAR Methods: "We measured the properties of each spike
    in response to this stimulus set. For each step amplitude we calculated the ratio of the
    last to first spike property."). The first series of 1 s steps that rise by 200 pA and
    reach at least 1.4 nA (series stopped at depolarization block end early); first sweep at each amplitude. Per step: spike count, maximum
    instantaneous rate, and last-to-first ratios of half-width and max dV/dt."""
    for run in fi_series(sweeps):
        steps = {}
        for s in run:
            a, b, amp = main_step(s["i"], s["rate"])
            if a is None or amp <= 0 or (b - a) / s["rate"] < 0.9:
                continue
            amp = round(amp)
            if amp not in steps:
                steps[amp] = (s, a, b)
        # the 200 pA grid up to 4 nA (STAR Methods: "increased in amplitude by 200 pA up to a
        # maximum value of 4 nA"); some files hold commands beyond 4 nA, which are left out
        amps = np.array(sorted(a_ for a_ in steps if a_ % 200 == 0 and a_ <= 4000))
        if len(amps) < 5 or amps.max() < 1400 or np.median(np.diff(amps)) != 200:
            continue
        rows = []
        for amp in amps:
            s, a, b = steps[amp]
            sp = detect_spikes(s["v"], s["rate"], a, b)
            n = len(sp)
            hz = s["rate"] / np.diff([x["ti"] for x in sp]).min() if n > 1 else float(n > 0)
            wr = sp[-1]["hw"] / sp[0]["hw"] if n > 1 else np.nan
            ur = sp[-1]["max_dvdt"] / sp[0]["max_dvdt"] if n > 1 else np.nan
            rows.append(dict(i_inject=amp, num_spikes=n, max_freq=hz, width_ratio=wr,
                             upstroke_ratio=ur))
        out = pd.DataFrame(rows)
        out.attrs["max_command_pA"] = float(max(steps))  # before the 4 nA limit
        return out
    return None


def oscillation_segments(v, rate, a, b, sp):
    """Interspike segments of one 10 s sweep, for the subthreshold oscillation analysis (STAR
    Methods: "Segments were further isolated from the AHP by fitting a curve to identify the
    return to baseline, and the 50 ms preceding the subsequent AP was dropped ... Prior to FFT
    analysis, segments were filtered at a lower bound of 3 Hz and an upper bound of 50 Hz.
    Segments of a duration greater than 650ms were then individually analyzed using fast-Fourier
    transforms (FFT) ... For segments of duration greater than 1 s, autocorrelation analysis
    was restricted to the last 1 s of the segment."). Open details, standard choices named in
    the claims file: an exponential fitted from the AHP trough, baseline reached within 1 mV of
    its asymptote; a zero-phase 4th-order Butterworth band-pass; autocorrelogram frequency as 1
    over the lag of its first peak after zero lag. Standard choices of this attempt: the trace is
    resampled to 1 kHz; the AHP trough is the minimum within 200 ms of the spike peak; FFT
    strength is the peak amplitude of the spectrum of the mean-subtracted, Hann-windowed
    segment (mV)."""
    from scipy.optimize import curve_fit
    q = max(1, int(rate // 1000))
    vd = signal.decimate(v, q, ftype="fir") if q > 1 else v
    fs = rate / q
    bb, aa = signal.butter(4, [3 / (fs / 2), 50 / (fs / 2)], "band")
    out = []
    pk = [x["pi"] // q for x in sp]
    th = [x["ti"] // q for x in sp]
    for j in range(len(sp) - 1):
        p0, nxt = pk[j], th[j + 1] - int(0.05 * fs)
        if nxt - p0 < int(0.65 * fs):
            continue
        w = vd[p0:min(p0 + int(0.2 * fs), nxt)]
        tr = p0 + int(np.argmin(w))
        y = vd[tr:nxt]
        t = np.arange(len(y)) / fs
        try:
            popt, _ = curve_fit(lambda t, vi, A, tau: vi - A * np.exp(-t / tau), t, y,
                                p0=(y[-1], y[-1] - y[0], 0.05), maxfev=2000)
            vinf, A, tau = popt
            ok = np.flatnonzero(np.abs((vinf - A * np.exp(-t / max(tau, 1e-4))) - vinf) < 1.0)
            st = tr + (int(ok[0]) if len(ok) else 0)
        except Exception:
            st = tr
        seg = vd[st:nxt]
        dur = len(seg) / fs
        if dur <= 0.65:
            continue
        vm = float(np.mean(seg))
        segf = signal.filtfilt(bb, aa, seg - seg.mean(), padlen=min(3 * max(len(aa), len(bb)), len(seg) - 1))
        win = np.hanning(len(segf))
        S = np.abs(np.fft.rfft(segf * win)) * 2 / win.sum()
        Fq = np.fft.rfftfreq(len(segf), 1 / fs)
        m = (Fq >= 3) & (Fq <= 50)
        k = int(np.argmax(S[m]))
        ac_f = np.nan
        if dur > 1.0:
            z = segf[-int(fs):]
            ac = np.correlate(z, z, "full")[len(z) - 1:]
            ac = ac / ac[0]
            peaks = signal.find_peaks(ac[int(fs / 50):int(fs / 3) + 1])[0]
            if len(peaks):
                ac_f = fs / (peaks[0] + int(fs / 50))
        out.append(dict(vm=vm, dur=dur, fft_f=float(Fq[m][k]), fft_p=float(S[m][k]), ac_f=ac_f))
    return out


def long_steps(sweeps):
    """10 s steps near rheobase (STAR Methods). Per complete sweep: amplitude, spike times (s
    from step onset), and, for sweeps with 1 to 200 spikes (STAR Methods), the interspike
    segments of oscillation_segments."""
    out = []
    for s in sorted([x for x in sweeps if x["protocol"] == "s10"], key=lambda x: x["sweep"]):
        a, b, amp = main_step(s["i"], s["rate"])
        if a is None or amp <= 0 or (b - a) / s["rate"] < 9.9:
            continue
        sp = detect_spikes(s["v"], s["rate"], a, b)
        segs = oscillation_segments(s["v"], s["rate"], a, b, sp) if 1 <= len(sp) <= 200 else []
        out.append(dict(sweep=s["sweep"], amp=amp, desc=s["desc"],
                        t=np.array([x["ti"] - a for x in sp]) / s["rate"], segs=segs))
    return out


def cell_features(asset_id):
    """All features of one cell, the extended FI table (or None) and the 10 s sweeps."""
    sw, meta = read_cell(asset_id, with_meta=True)
    meta["rates"] = sorted({s["rate"] for s in sw})
    f = {}
    fi, _ = fi_features(sw)
    f.update({k: v for k, v in fi.items() if not k.startswith("fi_")})
    f.update(vi_features(sw))
    f.update(chirp_features(sw))
    f.update(short_features(sw))
    ext = extended_fi(sw)
    s10 = long_steps(sw)
    curve = {k: fi.get(k) for k in ("fi_amps", "fi_n", "fi_hz")}
    return f, curve, ext, s10, meta


def cell_job(row):
    """Features of one asset row (for a process pool); errors are returned, not raised."""
    try:
        f, curve, ext, s10, meta = cell_features(row["asset_id"])
        return dict(path=row["path"], feats=f, curve=curve, ext=ext, s10=s10, meta=meta, err=None)
    except Exception as e:  # reported in the notebook as a dropped cell
        return dict(path=row["path"], feats={}, curve={}, ext=None, s10=[], meta={}, err=repr(e))


def load_all(assets, workers=6):
    """Features of every file, streamed in parallel processes."""
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(cell_job, assets.to_dict("records")))


# ---------------------------------------------------------------- statistics
# The 40 features of the code's list (UMAPprojections_020724.ipynb, flist); zap_tau has no
# definition in the paper and is not computed here, so 39 are used.
FLIST = ['initial_gain', 'max_gain', 'initial_ifreq_gain', 'max_ifreq_gain', 'train_current',
         'SFA', 'CV', 'mAHP', 'threshold_current', 'threshold_t', 'AP_threshold', 'AP_peak',
         'AP_amp', 'max_dvdt', 'min_dvdt', 'f_AHP', 'AP_HW', 'i_max_gain', 'Fr', 'RQ', 'cutoff',
         'Iphase', 'phase0', 'MaxZ', 'MaxRn', 'SSRn', 'sag_ratio', 'rebound', 'rmp',
         'threshold_short', 'AP_peak_short', 'AP_amp_short', 'max_dvdt_short', 'min_dvdt_short',
         'halfwidth_short', 'AP_short_i', 'gain_CV', 'inst_gain_CV', 'up_down_ratio']


def anova(df, y, factors):
    """OLS with all interactions of the factors and type II sums of squares, as the code's
    AOV_Two_way and AOV_Three_way. Adds the standard partial eta squared,
    SS_effect / (SS_effect + SS_residual) (the Methods' measure), and the code's formula as
    `eta_code` (partial_eta and partial_eta_3way: SS_a / (SS_total - (SS_b - SS_c - ...)))."""
    import statsmodels.api as sm
    from statsmodels.formula.api import ols
    d = df[[y] + factors].dropna()
    rhs = " * ".join(f"C({f})" for f in factors)
    m = ols(f"Q('{y}') ~ {rhs}", data=d).fit()
    t = sm.stats.anova_lm(m, typ=2)
    ssr = t.loc["Residual", "sum_sq"]
    t["eta_p"] = t["sum_sq"] / (t["sum_sq"] + ssr)
    eff = t.index[:-1]
    tot = t["sum_sq"].sum()
    code = {}
    for e in eff:
        others = [t.loc[o, "sum_sq"] for o in eff if o != e]
        code[e] = t.loc[e, "sum_sq"] / (tot - (others[0] - sum(others[1:])))
    t["eta_code"] = pd.Series(code)
    t.loc["Residual", ["eta_p", "eta_code"]] = np.nan
    t.attrs["n"] = len(d)
    return t


def anova_table(df, feats, factors):
    """Per-feature ANOVAs; returns p, BH-corrected p (across features, per term, as the code's
    fdr and fdr_3way), standard and code partial eta squared, and n."""
    from statsmodels.stats.multitest import fdrcorrection
    rows = []
    for f in feats:
        if df[f].notna().sum() < 10:
            continue
        t = anova(df, f, factors)
        for term in t.index[:-1]:
            rows.append(dict(feature=f, term=term, F=t.loc[term, "F"], p=t.loc[term, "PR(>F)"],
                             eta_p=t.loc[term, "eta_p"], eta_code=t.loc[term, "eta_code"],
                             n=t.attrs["n"]))
    r = pd.DataFrame(rows)
    r["p_bh"] = np.nan
    for term, g in r.groupby("term"):
        ok = g["p"].notna()
        r.loc[g.index[ok], "p_bh"] = fdrcorrection(g.loc[ok, "p"])[1]
    return r


def cohen_d(a, b):
    """Cohen's d with the pooled SD, as ExtendedFI.ipynb and morphology.ipynb."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    n1, n2 = len(a), len(b)
    s = np.sqrt(((n1 - 1) * a.var(ddof=1) + (n2 - 1) * b.var(ddof=1)) / (n1 + n2 - 2))
    return (a.mean() - b.mean()) / s


def preprocess(df, feats, prep_col="Prep"):
    """STAR Methods, Physiology UMAP and classification: "We excluded neurons with more than 75%
    of physiology features missing. For the remaining cells we imputed missing feature values as
    the mean of the two nearest neighbors (KNNImputer). Features were then transformed to
    z-scores (StandardScaler). Z score transformations were performed separately for neurons
    recorded in acute versus culture." Imputation is also done per preparation, as the code
    calls simpleimpute on acute and culture separately."""
    from sklearn.impute import KNNImputer
    from sklearn.preprocessing import StandardScaler
    keep = df[feats].isna().mean(axis=1) <= 0.75
    d = df[keep].copy()
    parts = []
    for p, g in d.groupby(prep_col):
        X = KNNImputer(n_neighbors=2).fit_transform(g[feats].astype(float))
        X = StandardScaler().fit_transform(X)
        parts.append(pd.DataFrame(X, index=g.index, columns=feats))
    Z = pd.concat(parts).loc[d.index]
    return d, Z, int((~keep).sum())


def classifier_scores(X, y, frac, reps, rng, stratify=False, C=1.0):
    """Multiclass logistic regression (STAR Methods) trained on a random fraction of cells and
    tested on the held-out ones (on all cells when frac is 1), repeated, predictions pooled.
    Returns per-class f1, per-class recall and the support-weighted mean of each. Solver and
    regularization: scikit-learn defaults (claims file, standard choice), max_iter raised."""
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import f1_score, recall_score
    from sklearn.model_selection import train_test_split
    y = np.asarray(y)
    yt, yp = [], []
    redraws = 0
    for _ in range(reps):
        if frac >= 1:
            tr = te = np.arange(len(y))
        else:
            while True:  # a training draw holding one class only is drawn again (counted)
                tr, te = train_test_split(np.arange(len(y)), train_size=frac,
                                          random_state=int(rng.integers(1 << 31)),
                                          stratify=y if stratify else None)
                if len(set(y[tr])) > 1:
                    break
                redraws += 1
        m = LogisticRegression(C=C, max_iter=5000).fit(X[tr], y[tr])
        yt.append(y[te]); yp.append(m.predict(X[te]))
    yt, yp = np.concatenate(yt), np.concatenate(yp)
    labels = sorted(set(y))
    f1 = f1_score(yt, yp, labels=labels, average=None)
    rec = recall_score(yt, yp, labels=labels, average=None)
    w = np.array([(yt == l).mean() for l in labels])
    return dict(labels=labels, f1=f1, recall=rec, f1_w=float((f1 * w).sum()),
                recall_w=float((rec * w).sum()), redraws=redraws)
