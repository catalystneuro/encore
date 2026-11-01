"""Loading and measures for the optical recordings of Semenov, Kim, Silkuniene & Pakhomov (2025).

Cell Reports Physical Science 6, 102660, doi:10.1016/j.xcrp.2025.102660.

The paper deposited its raw images in ten dandisets (Data and code availability). The target,
DANDI:001274, holds the pulsed laser strobe images of Figures 5, 6 and S3. The claims file assigns
the fast optical recordings of Figures 1 to 3, S1 and S2 to other dandisets of the same paper
(`data: elsewhere`), read here at their pinned published versions (`VERSIONS`).

Every file holds one image stack (`acquisition/<name>/data`, frames x rows x columns, uint16) and
nothing else: no ROIs, no traces, no stimulus waveform and no trial table. The stimulus of a
session is read from its session description (frequency, modulation, voltage, tetrodotoxin).
Files are streamed from the archive; each stack is reduced to two traces as it loads.

Where the parameters come from:

- Stimulus timing. The fast recordings start the stimulus 50 ms after the start of imaging and
  last 250 ms (Methods, "Recording of the optical APs": "The standard imaging protocol started 50
  ms before sine wave stimulation and continued for 250 ms"; the files' descriptions say the same).
  The 2-s recordings of DANDI:001030 start it at 25 ms (their description). The first frame of
  every fast recording is a bright camera artifact (about 2.5 times the others) and is left out
  of F0, a standard choice that cannot change a result.
- F and dF. dF = 100% (F - F0) / F0 with F0 the mean before the stimulus (Methods). F is the
  emission "over the entire cell soma" (Methods); the files have 16 x 16 pixels and no soma
  outline, so two readings are run (assumption, see the notebook): `whole`, the mean of the
  whole frame, and `bright`, the mean of the pixels brighter than the median of the
  pre-stimulus mean image.
- AP detection. The Methods give "APs were readily identifiable as brief emission upticks" in
  neurons whose APs peak above 5% dF and last about 10 ms. The claims file names two readings:
  (a) a peak of dF above 5%; (b) a rise of at least 5% dF within 5 ms. In both, peaks closer
  than 8 ms are merged into one AP, as an AP lasts 8 ms (Methods: "typical values: 11.3% +-
  0.9% dF and 8 +- 0.7 ms duration"); this caps the rate the detection can see at 125 Hz, above
  the 60 to 90 Hz the paper reports. In (a) a peak must also rise 5% dF above the trace on
  both sides of it (scipy prominence, the Methods' AP level applied to the local baseline) and
  be at least 1 ms wide at half its prominence (Methods: APs are "brief emission upticks" that
  "lasted about 10 ms", "8 +- 0.7 ms duration"). This is an assumption: the claims file's
  reading (a) asks only a peak above 5% over F0, and without these two conditions noise on a
  depolarized plateau above 5% counts as APs (about 18 per 250 ms for a 6% plateau with the data's
  0.8% noise SD; the notebook shows the test). In the data, 99% of the first APs of a session
  have a prominence above 8.6% and a half-width above 1.6 ms, so the conditions keep real APs.
  The first round of this attempt used a prominence of 2.5% and no width, which the verifier
  showed lets plateau noise through.
- Field. The session descriptions give the generator voltage, peak to peak, and say "1V
  translates into 36 V/cm at the location of neurons" (DANDI:001030 says its voltages are of
  one polarity, "peak-to-peak would be two-fold larger"). The claims file takes the field from
  the dataset's metadata; two readings are run (assumption, see the notebook): `half`, field =
  36 V/cm x Vpp / 2, the peak field, and `full`, field = 36 V/cm x Vpp.
- Strobe images (DANDI:001274). RATIO image as in the Methods ("Pulsed laser fluorescence
  microscopy"): CONTROL is the mean of the frames before the pulse, POLARIZED the mean of the
  frames of the last 0.5 us of the pulse, both low-pass filtered over 12 x 12 pixels; RATIO =
  1000 x POLARIZED / CONTROL. The frame times are not in the files; their description says
  "Exposures began 1 us after the start of recording", and the Methods give 50-ns steps from 1
  us before the pulse, so frame i is at -1 + 0.05 i us (assumption, see the notebook).
"""

from __future__ import annotations

import json
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
from scipy.ndimage import uniform_filter
from scipy.signal import find_peaks

API = "https://api.dandiarchive.org/api"
VERSIONS = {
    "001274": "0.250805.1401",  # strobe imaging, Figures 5, 6, S3 (the target)
    "001273": "0.250805.1356",  # 2-us pulse kinetics, Figure 4
    "001030": "0.240520.1924",  # 2-s ramped 2-kHz sine waves in NaGlu, Figure 3C
    "001032": "0.240527.1432",  # 2- and 20-kHz sine waves, modulated and not (Figures 1, 2)
    "001033": "0.240527.1432",
    "001034": "0.240527.1431",  # a second deposit of 001032 (see the notebook)
    "001035": "0.240527.1432",
    "001271": "0.250805.1352",  # tetrodotoxin, Figure S2
    "001272": "0.250805.1358",  # Di-8-ANEPPS, Figure S1
}
V_TO_V_PER_CM = 36.0          # session descriptions: "1V translates into 36 V/cm"
AP_LEVEL = 5.0                # % dF, Methods
AP_WIDTH_S = 0.005            # 5 ms: rise window of reading (b), claims file
AP_MERGE_S = 0.008            # 8 ms: AP duration, Methods
PROMINENCE = 5.0              # % dF, reading (a): the AP level over the local baseline (assumption)
MIN_WIDTH_S = 0.001           # s, reading (a): half-width; AP duration 8 ms, Methods (assumption)
STIM_START_S = 0.050          # fast recordings, Methods
STIM_DUR_S = 0.250
ROIS = ("whole", "bright")
AP_READINGS = ("a", "b")


def _get(url):
    with urllib.request.urlopen(url, timeout=120) as r:
        return json.load(r)


def list_assets(dandiset, threads=16):
    """Assets of a dandiset at its pinned version, with S3 URL, session start and description."""
    version = VERSIONS[dandiset]
    base = f"{API}/dandisets/{dandiset}/versions/{version}/assets/"
    assets, url = [], base + "?page_size=1000"
    while url:
        page = _get(url)
        assets += page["results"]
        url = page["next"]

    def meta(a):
        m = _get(base + a["asset_id"] + "/")
        ses = [w for w in m["wasGeneratedBy"] if w["schemaKey"] == "Session"][0]
        s3 = [u for u in m["contentUrl"] if "s3" in u][0]
        return dict(path=a["path"], size=a["size"], url=s3, session=ses["name"],
                    start_date=ses.get("startDate", ""), description=ses.get("description", ""))

    with ThreadPoolExecutor(threads) as ex:
        return sorted(ex.map(meta, assets), key=lambda r: r["path"])


def parse_fast(desc, session=""):
    """Stimulus of a fast recording from its session description."""
    d = dict(tetrodotoxin="presence of the sodium channel inhibitor" in desc,
             sham="sham" in desc.lower() or "sham" in session.lower())
    m = re.search(r"modulated at (\S+?)Hz frequency\) stimulation applied at (\S+?)Hz using "
                  r"([\d.,]+)V", desc)
    if m:
        d.update(modulated=True, carrier=m.group(2), voltage=float(m.group(3).replace(",", ".")))
        return d
    m = re.search(r"applied at (\S+?)Hz using ([\d.,]+)V", desc)
    if m:
        d.update(modulated=False, carrier=m.group(1), voltage=float(m.group(2).replace(",", ".")))
        return d
    m = re.search(r"sine wave at (\S+?)Hz with ([\d.,]+)V", desc)
    if m:
        d.update(modulated=False, carrier=m.group(1), voltage=float(m.group(2).replace(",", ".")))
        return d
    m = re.search(r"under ([\d.,]+)V amplitude", desc)      # DANDI:001030, one polarity
    if m:
        d.update(modulated=False, carrier="2k", voltage=2 * float(m.group(1).replace(",", ".")))
        return d
    d.update(modulated=False, carrier=None, voltage=0.0)
    return d


def field(vpp, reading="half"):
    """Electric field (V/cm) from the generator voltage, peak to peak (see module docstring)."""
    return V_TO_V_PER_CM * vpp * (0.5 if reading == "half" else 1.0)


def _reduce(stack, onset):
    """Two dF traces (%) from an image stack: whole frame and bright pixels."""
    a = stack.astype(np.float64)
    pre = a[1:onset].mean(0)
    mask = pre > np.median(pre)
    out = {}
    for name, s in (("whole", a.mean((1, 2))), ("bright", a[:, mask].mean(1))):
        f0 = s[1:onset].mean()
        out[name] = (100.0 * (s - f0) / f0).astype(np.float32)
    out["mean_image"] = pre.astype(np.float32)
    return out


def load_fast(assets, stim_start_s=STIM_START_S, threads=24):
    """Stream every fast recording and reduce it to dF traces as it loads."""
    def one(a):
        for attempt in range(4):
            try:
                with h5py.File(remfile.File(a["url"]), "r") as f:
                    g = f["acquisition"][list(f["acquisition"].keys())[0]]
                    stack = g["data"][:]
                    rate = float(g["starting_time"].attrs["rate"])
                    start = f["session_start_time"][()].decode()
                break
            except OSError:
                if attempt == 3:
                    raise
        onset = int(round(stim_start_s * rate))
        r = dict(a, rate=rate, start=start, n_frames=stack.shape[0], shape=stack.shape,
                 onset=onset, first_frame_ratio=float(stack[0].mean() / stack[1:onset].mean()),
                 raw_f0=float(stack[1:onset].mean()))
        r.update(_reduce(stack, onset))
        return r

    with ThreadPoolExecutor(threads) as ex:
        return list(ex.map(one, assets))


def detect_aps(dF, rate, reading="a", level=AP_LEVEL, invert=False, prominence=PROMINENCE,
               min_width_s=MIN_WIDTH_S):
    """Frame indices of AP peaks under reading (a) or (b) (module docstring). `prominence`
    and `min_width_s` apply to reading (a); at levels other than 5% (the SD readings of
    Di-8-ANEPPS) the prominence follows the level."""
    x = -dF if invert else dF
    w = int(round(AP_WIDTH_S * rate))
    dist = int(round(AP_MERGE_S * rate))
    if reading == "a":
        prom = prominence * level / AP_LEVEL
        p, _ = find_peaks(x, height=level, distance=dist, prominence=prom,
                          width=(min_width_s * rate, None))
    else:
        p, _ = find_peaks(x, distance=dist)
        p = np.array([i for i in p if i >= w and x[i] - x[i - w:i].min() >= level], dtype=int)
    return p


def aps_in_window(dF, rate, onset, dur_s=STIM_DUR_S, reading="a", level=AP_LEVEL, invert=False):
    """AP peak times (s from stimulus onset) during the stimulus, plus 5 ms for the last AP."""
    p = detect_aps(dF, rate, reading, level, invert)
    end = onset + int(round((dur_s + AP_WIDTH_S) * rate))
    p = p[(p >= onset) & (p < end)]
    return (p - onset) / rate


def window_mean(dF, rate, onset, t0, t1, invert=False):
    """Mean dF (%) from t0 to t1 s after stimulus onset."""
    x = -dF if invert else dF
    return float(x[onset + int(round(t0 * rate)):onset + int(round(t1 * rate))].mean())


# --- strobe images (DANDI:001274) ---------------------------------------------------------

def frame_times_pulse(n):
    """Frame times (us from pulse onset) of a 2-us pulse recording: 50-ns steps from -1 us."""
    return -1.0 + 0.05 * np.arange(n)


def ratio_image(stack, t):
    """RATIO image of the Methods (1000 = no change) from a pulse stack and its frame times."""
    a = stack.astype(np.float64)
    control = a[t < 0].mean(0)
    polarized = a[(t >= 1.5) & (t < 2.0)].mean(0)
    control = uniform_filter(control, 12)
    polarized = uniform_filter(polarized, 12)
    return 1000.0 * polarized / control, control


def rebuilt_rois(ratio, control, size=8, cell_quantile=0.75):
    """ROI 1 and 2 rebuilt from the RATIO image: size x size pixel squares centred on its
    minimum (most hyperpolarized) and maximum (most depolarized) within the cell, the cell
    being the pixels of the filtered CONTROL image above `cell_quantile`. A variant only: the
    paper's ROIs were drawn by hand and are not in the dataset."""
    cell = control > np.quantile(control, cell_quantile)
    r = np.where(cell, ratio, np.nan)
    i1 = np.unravel_index(np.nanargmin(r), r.shape)
    i2 = np.unravel_index(np.nanargmax(r), r.shape)
    h = size // 2

    def box(i):
        m = np.zeros(r.shape, bool)
        m[max(i[0] - h, 0):i[0] + h, max(i[1] - h, 0):i[1] + h] = True
        return m

    return box(i1), box(i2), cell


def load_strobe(url, rois=None):
    """Stream a strobe stack; return the stack's per-frame means in the given masks, or the
    stack itself when no masks are given."""
    with h5py.File(remfile.File(url), "r") as f:
        stack = f["acquisition/StrobeImaging/data"][:]
    if rois is None:
        return stack
    return {k: stack[:, m].mean(1) for k, m in rois.items()}


# --- session tables and per-neuron measures (fast recordings) ------------------------------

def neuron_of(dandiset, path):
    """Neuron of a fast recording. Subjects are neurons; DANDI:001030 makes one subject per
    session (`sub-c7-1-45V`), whose neuron is the `c7` part."""
    sub = path.split("/")[0]
    if dandiset == "001030":
        sub = re.match(r"sub-(c\d+)", sub).group(1)
    return f"{dandiset}/{sub}"


def session_table(recs, dandiset, dur_s=STIM_DUR_S, invert=False, sd_levels=(), traces=None):
    """One row per session: stimulus, AP times under each ROI and AP reading, and window means.

    `invert` flips traces whose dye loses emission on depolarization (Di-8-ANEPPS, Methods).
    `sd_levels` adds AP readings at a level of k pre-stimulus SDs (suffix `<k>sd`).
    `traces` replaces the stored traces by name (used for the bleaching correction of Figure 3C).
    """
    import pandas as pd
    rows = []
    for r in recs:
        p = parse_fast(r["description"], r["session"])
        row = dict(dandiset=dandiset, neuron=neuron_of(dandiset, r["path"]), path=r["path"],
                   start=r["start"], carrier=p["carrier"], modulated=p["modulated"],
                   voltage=p["voltage"], ttx=p["tetrodotoxin"], sham=p["sham"], rate=r["rate"],
                   onset=r["onset"], n_frames=r["n_frames"])
        for roi in ROIS:
            dF = r[roi] if traces is None else traces[r["path"]][roi]
            rate, on = r["rate"], r["onset"]
            sd = float(dF[1:on].std())
            row[f"pre_sd/{roi}"] = sd
            for rd in AP_READINGS:
                row[f"aps/{roi}/{rd}"] = aps_in_window(dF, rate, on, dur_s, rd, invert=invert)
                pre = detect_aps(dF, rate, rd, invert=invert)
                row[f"pre_aps/{roi}/{rd}"] = int(((pre >= 1) & (pre < on)).sum())
                for k in sd_levels:
                    row[f"aps/{roi}/{rd}{k:g}sd"] = aps_in_window(dF, rate, on, dur_s, rd,
                                                                  level=k * sd, invert=invert)
            end = min(dur_s, (len(dF) - on) / rate)
            row[f"last100/{roi}"] = window_mean(dF, rate, on, end - 0.1, end, invert)
            row[f"half2/{roi}"] = window_mean(dF, rate, on, end / 2, end, invert)
        rows.append(row)
    df = pd.DataFrame(rows)
    for c in [c for c in df.columns if c.startswith("aps/")]:
        df["n" + c] = df[c].apply(len)
    return df.sort_values(["neuron", "start"]).reset_index(drop=True)


def per_field(df, key, field_reading="half"):
    """Per neuron, carrier and field: mean AP count, first-AP latency (s, mean over sessions
    with APs), highest first-two-AP rate (Hz, Methods: "the inverse of the peak-to-peak time
    interval between the first two APs"), and mean dF of the last 100 ms and the second half.
    Sessions repeated at one field are averaged (a standard choice). `key` is `<roi>/<reading>`."""
    roi = key.split("/")[0]
    aps = df[f"aps/{key}"]
    d = df.assign(field=field(df.voltage, field_reading), n=df[f"naps/{key}"],
                  lat=aps.apply(lambda a: a[0] if len(a) else np.nan),
                  rate_hz=aps.apply(lambda a: 1 / (a[1] - a[0]) if len(a) > 1 else np.nan),
                  last=df[f"last100/{roi}"], half2=df[f"half2/{roi}"])
    return d.groupby(["neuron", "carrier", "field"]).agg(
        n=("n", "mean"), lat=("lat", "mean"), rate_hz=("rate_hz", "max"), last=("last", "mean"),
        half2=("half2", "mean"), sessions=("n", "size")).reset_index()


def thresholds(df, key, field_reading="half"):
    """Per neuron and stimulus, the lowest field of a session with at least 1 and at least 5
    APs during the 250-ms stimulus (Figure 2D legend). `bracketed` says whether a session at a
    lower field was recorded (it then had fewer APs)."""
    import pandas as pd
    d = df.assign(field=field(df.voltage, field_reading), n=df[f"naps/{key}"],
                  stim=df.carrier + np.where(df.modulated, "/mod", "/unmod"))
    rows = []
    for (nr, s), g in d.groupby(["neuron", "stim"]):
        for k in (1, 5):
            ok = g[g.n >= k]
            thr = ok.field.min() if len(ok) else np.nan
            rows.append(dict(neuron=nr, stim=s, aps=k, thr=thr,
                             bracketed=bool(len(ok) and (g.field < thr).any())))
    return pd.DataFrame(rows)


# --- sine wave strobe measures (variant only) -----------------------------------------------

SINE_STEP_US = 20.0           # Methods: "with 20-us steps for sine wave stimuli"
CARRIER_HZ = 2000.0
LOESS_SPANS = (0.75, 0.5, 0.25)   # claims file O2: R's loess default span 0.75, and 0.5, 0.25


def loess(y, span=0.75):
    """Local quadratic regression with tricube weights over the nearest span x n points, as R's
    loess(degree = 2, family = "gaussian") computes it at the data points (claims file O2)."""
    n = len(y)
    x = np.arange(n, dtype=float)
    k = int(np.ceil(span * n))
    out = np.empty(n)
    for i in range(n):
        d = np.abs(x - x[i])
        h = np.sort(d)[k - 1]
        w = np.clip(1 - (d / h) ** 3, 0, None) ** 3
        X = np.vstack([np.ones(n), x - x[i], (x - x[i]) ** 2]).T
        sw = np.sqrt(w)
        beta = np.linalg.lstsq(X * sw[:, None], y * sw, rcond=None)[0]
        out[i] = beta[0]
    return out


def sine_dF(trace):
    """dF (%) of a sine wave stack trace: F0 is the mean of the first and the last carrier
    cycle (Methods), leaving out frame 0, an artifact as in the fast recordings."""
    per = int(round(1e6 / CARRIER_HZ / SINE_STEP_US))
    f = np.asarray(trace, float)
    f0 = np.r_[f[1:1 + per], f[-per:]].mean()
    return 100 * (f - f0) / f0


def cycle_regression(sub, peak_field, intercept=True):
    """Claims file O3 reading (b): per carrier cycle, half the peak-to-peak of the LOESS-subtracted
    dF against the peak field of that cycle, for a single beat whose envelope rises from zero to
    `peak_field` and back as a half sine (an assumption: the files hold no waveform). Returns
    slope (% per V/cm), its p-value and the number of cycles."""
    from scipy import stats
    per = int(round(1e6 / CARRIER_HZ / SINE_STEP_US))
    n = (len(sub) - 1) // per
    amp, fld = [], []
    for c in range(n):
        seg = sub[1 + c * per:1 + (c + 1) * per]
        amp.append((seg.max() - seg.min()) / 2)
        tc = (c + 0.5) / n
        fld.append(peak_field * np.sin(np.pi * tc))
    amp, fld = np.array(amp), np.array(fld)
    if intercept:
        r = stats.linregress(fld, amp)
        return r.slope, r.pvalue, n
    slope = (fld @ amp) / (fld @ fld)
    resid = amp - slope * fld
    se = np.sqrt(resid @ resid / (n - 1) / (fld @ fld))
    p = 2 * stats.t.sf(abs(slope / se), n - 1)
    return slope, p, n


def signed_field(n, peak_field, phase):
    """Instantaneous field (V/cm) of a single 2-kHz beat over n frames at 20-us steps: a half-sine
    envelope peaking at `peak_field` times the carrier at the given phase (assumption: the files
    hold no waveform; frame 0 is taken as the start of the beat)."""
    t = np.arange(n) * SINE_STEP_US * 1e-6
    T_beat = n * SINE_STEP_US * 1e-6
    return peak_field * np.sin(np.pi * t / T_beat) * np.sin(2 * np.pi * CARRIER_HZ * t + phase)


def fit_phase(sub, peak_field):
    """Carrier phase that best fits a LOESS-subtracted trace (least squares on the sine and cosine
    components under the envelope); frame 0 is left out."""
    n = len(sub)
    a = signed_field(n, 1.0, 0.0)[1:]
    b = signed_field(n, 1.0, np.pi / 2)[1:]
    coef = np.linalg.lstsq(np.vstack([a, b]).T, sub[1:], rcond=None)[0]
    return float(np.arctan2(coef[1], coef[0]))


def frame_regression(sub, fld):
    """Claims file O3 reading (a): dF after LOESS subtraction on the signed field, frame by frame
    (frame 0 left out). Returns slope (% per V/cm), its standard error and p-value."""
    from scipy import stats
    r = stats.linregress(fld[1:], sub[1:])
    return r.slope, r.stderr, r.pvalue
