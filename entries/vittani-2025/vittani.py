"""Loading and measures for dandiset 001414 (Vittani, Herlo, Wang et al. 2025, PNAS 122, e2422069122).

The dandiset holds one-photon macroscope recordings (512 x 512 pixels, 5 Hz, 1600 frames for the LED
experiments), stored as raw uint16 movies. It holds no traces, no stimulus times and no analysis
results. Arteriole files add rectangular ROIs (`image_mask`) and "rotated" copies of the movie.

Streaming. Each movie is gzip-compressed in chunks of 10 whole frames. `read_movie` asks HDF5 for the
byte range of every chunk and fetches the chunks over HTTP range requests in parallel from the
dandiset's S3 blob, decompressing each in memory and reducing it at once (to an ROI mean, or to the
profiles across arterioles), so a movie is never held whole and nothing is written to disk.

Where the parameters come from:

- Frame rate 5 Hz, 65 s baseline (LED at frame 325), LED durations, 1600 frames: SI Appendix, In Vivo
  One-Photon Macroscopic Imaging, as the claims file's header gives them; checked against the data in
  the notebook (`led_frames`).
- Astrocyte signal pipeline: SI Appendix, Image Data Analysis (claims header): mean ROI intensity,
  Blood Offset from the darkest vessel in the first frame, Adjusted Offset, two-term exponential
  photobleaching fit on the baseline and the last 2 min (cAMP only), dF/F0, median filters of 20
  (anesthetized) and 50 (awake) frames, peak, rise time, 80% decay time, duration = rise + decay.
- The ROI "covering the thinned skull area with good signal quality" is not in the files. ASSUMPTION:
  a central disc of radius `ROI_RADIUS` pixels (about 1.6 mm of the 5.3 mm field), which lies inside
  the thinned skull window in the recordings; the whole frame is a variant. The Blood Offset is taken as
  the mean of the darkest `BLOOD_PERCENTILE` percent of the ROI's pixels in the first frame (smoothed
  over 5 x 5 pixels), a standard choice for "a small ROI over the darkest vessel".
- The across-recording "Corrected dF/F0" (an exponential fitted to recordings 1 and 4) is not applied:
  the passage does not say what is fitted against what (deviation in the record).
- Open readings named in the claims file's header (time origin, meaning of 80% decay, baseline F0,
  filtered or unfiltered peak) are all computed by `params`; none is chosen here.
- The arteriole movies are not analysed here (their "rotated" copies hold only 0 and 1; see the
  attempt record).
"""

from __future__ import annotations

import re
import threading
import time
import zlib
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy import ndimage, optimize, signal
from urllib3.util.retry import Retry

DANDISET_ID = "001414"
DANDISET_VERSION = "0.250603.1324"
API = "https://api.dandiarchive.org/api"

FPS = 5.0
LED_FRAME = 325                     # 65 s baseline at 5 Hz
ROI_RADIUS = 160                    # pixels; assumption, see the docstring
BLOOD_PERCENTILE = 0.5              # percent of ROI pixels; standard choice
THREADS = 24

_local = threading.local()


def _session():
    if not hasattr(_local, "s"):
        s = requests.Session()
        retry = Retry(total=8, backoff_factor=0.5, status_forcelist=(500, 502, 503, 504),
                      allowed_methods=None)
        s.mount("https://", requests.adapters.HTTPAdapter(pool_connections=4, pool_maxsize=THREADS,
                                                          max_retries=retry))
        _local.s = s
    return _local.s


# --------------------------------------------------------------------------------------------- assets

def list_assets() -> pd.DataFrame:
    """Every asset of the pinned version, with the experiment it belongs to, read from its path."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=1000"
    rows = []
    while url:
        page = requests.get(url, timeout=60).json()
        rows += [{"path": a["path"], "asset_id": a["asset_id"], "size": a["size"]} for a in page["results"]]
        url = page["next"]
    df = pd.DataFrame(rows)
    parsed = df.path.map(parse_path).apply(pd.Series)
    return pd.concat([df, parsed], axis=1).sort_values("path").reset_index(drop=True)


KX_RECORDING = {"LED1s": 1, "LED200ms": 2, "LED3s": 3, "LED1s-2": 4}   # order of SI, 1 s, 0.2 s, 3 s, 1 s
LED_SECONDS = {1: 1.0, 2: 0.2, 3: 3.0, 4: 1.0}


def parse_path(path: str) -> dict:
    sub, ses = path.split("/")[0][4:], path.split("/")[1]
    out = {"subject": sub, "experiment": "other", "group": None, "genotype": None, "recording": None,
           "led_s": None}
    m = re.search(r"-(bPAC|ctrl)-", ses)
    if m:
        out["group"] = m.group(1)
    m = re.search(r"IP3R2-(KO|WT)", sub)
    if m:
        out["genotype"] = m.group(1)
    rec = re.search(r"-rec(\d+)_ophys", ses)
    if re.fullmatch(r"(PF|Ca)\d+", sub) and "-KX-LED" in ses and "25ms" not in ses:
        key = re.search(r"-KX-(LED[0-9a-z]+(?:-2)?)_ophys", ses).group(1)
        out.update(experiment=("camp" if sub.startswith("PF") else "ca") + "_kx", recording=KX_RECORDING[key],
                   led_s=LED_SECONDS[KX_RECORDING[key]])
    elif re.fullmatch(r"(PF|Ca)\d+", sub) and "-awake-rec" in ses:
        out.update(experiment=("camp" if sub.startswith("PF") else "ca") + "_awake", recording=int(rec.group(1)),
                   led_s=1.0)
    elif re.fullmatch(r"(PF|Ca)\d+-IP3R2-(KO|WT)", sub) and "-awake-rec" in ses:
        out.update(experiment=("camp" if sub.startswith("PF") else "ca") + "_ip3r2", recording=int(rec.group(1)),
                   led_s=1.0)
    elif sub.startswith("25ms-PF"):
        out.update(experiment="camp_mild", recording=int(rec.group(1)), led_s=0.025)
    elif re.fullmatch(r"Ca\d+", sub) and "LED25ms" in ses:
        out.update(experiment="ca_mild", recording=int(rec.group(1)), led_s=0.025)
    elif "startle" in ses:
        out.update(experiment="startle_ca" if sub.startswith("Ca") else
                   ("startle_camp_awake" if "awake" in ses else "startle_camp_kx"))
    elif sub.startswith("whisk-PF"):
        out.update(experiment="whisker_camp", led_s=None,
                   recording={"30sec": 0.5, "1min": 1.0, "2min": 2.0}[re.search(r"whisker(\w+?)_ophys", ses).group(1)])
    elif "alb" in sub:
        exp = ("alb_whisker" if sub.startswith("whisk") else "alb_mild" if sub.startswith("25ms")
               else "alb_kx" if sub.startswith("KX") else "alb_ip3r2" if "IP3R2" in sub else "alb_awake")
        out["experiment"] = exp if "fig" not in ses else "other"
        led = re.search(r"-LED(1s|200ms|3s)", ses)
        out["led_s"] = {"1s": 1.0, "200ms": 0.2, "3s": 3.0}[led.group(1)] if led else (0.025 if exp == "alb_mild" else 1.0)
        roi = re.search(r"-(ROI\w+?)-", ses + "-")
        out["recording"] = roi.group(1) if roi else None
    elif sub.startswith("PF-GCaMP"):
        out["experiment"] = "twophoton_gcamp"
    return out


def s3_url(asset_id: str) -> str:
    meta = requests.get(f"{API}/assets/{asset_id}/", timeout=60).json()
    return next(u for u in meta["contentUrl"] if "s3" in u)


def open_file(asset_id: str):
    url = s3_url(asset_id)
    return url, h5py.File(remfile.File(url), "r")


def file_info(f) -> dict:
    g = f["general"]
    return {"identifier": f["identifier"][()].decode(), "session_id": g["session_id"][()].decode(),
            "subject_id": g["subject/subject_id"][()].decode(), "strain": g["subject/strain"][()].decode(),
            "indicator": g["optophysiology/ImagingPlane/indicator"][()].decode(),
            "imaging_rate": float(g["optophysiology/ImagingPlane/imaging_rate"][()]),
            "series": {k: f["acquisition"][k]["data"].shape for k in f["acquisition"]}}


def read_movie(url: str, dset, reduce, first=None):
    """Fetch every chunk of a movie in parallel and apply `reduce` to each block of frames (frames, y, x).
    `first`, if given, is called on the first block before the others are read, and its result is
    passed to `reduce`. Returns the reduced blocks concatenated in frame order.

    Movies are stored (frames, 512, 512), except one file whose movie is stored (512, 512, frames)
    (`time_last`); its chunks are moved to (frames, 512, 512) as they are read."""
    time_last = dset.shape[0] == dset.shape[1] and dset.shape[2] > dset.shape[0] and dset.chunks[2] < dset.shape[2]
    axis = 2 if time_last else 0
    n_frames = dset.shape[axis]
    n = dset.id.get_num_chunks()
    info = sorted((dset.id.get_chunk_info(i) for i in range(n)), key=lambda c: c.chunk_offset[axis])
    chunk = dset.chunks

    def fetch(ci):
        for attempt in range(6):
            try:
                r = _session().get(url, timeout=120,
                                   headers={"Range": f"bytes={ci.byte_offset}-{ci.byte_offset + ci.size - 1}"})
                r.raise_for_status()
                break
            except requests.RequestException:
                if attempt == 5:
                    raise
                time.sleep(2 ** attempt)
        x = np.frombuffer(zlib.decompress(r.content), dtype="<u2").reshape(chunk)
        return np.moveaxis(x, 2, 0) if time_last else x

    block0 = fetch(info[0])
    ctx = first(block0) if first else None
    with ThreadPoolExecutor(THREADS) as ex:
        rest = list(ex.map(lambda ci: reduce(fetch(ci), ctx), info[1:]))
    out = np.concatenate([reduce(block0, ctx)] + rest)
    return out[:n_frames], ctx


# ------------------------------------------------------------------------------------ astrocyte traces

def _disc(shape, radius):
    yy, xx = np.mgrid[: shape[0], : shape[1]]
    return (yy - shape[0] / 2 + 0.5) ** 2 + (xx - shape[1] / 2 + 0.5) ** 2 <= radius ** 2


def astro_trace(asset_id: str, series: str | None = None) -> dict:
    """Mean intensity per frame over the ROI disc and over the whole frame, with the Blood Offset."""
    url, f = open_file(asset_id)
    info = file_info(f)
    name = series or next(iter(f["acquisition"]))
    dset = f["acquisition"][name]["data"]
    roi = _disc((512, 512), ROI_RADIUS)

    def first(block):
        frame0 = ndimage.uniform_filter(block[0].astype(float), 5)
        vals = frame0[roi]
        blood = float(vals[vals <= np.percentile(vals, BLOOD_PERCENTILE)].mean())
        return {"blood_offset": blood, "frame0_mean": float(block[0][roi].mean())}

    def reduce(block, ctx):
        b = block.astype(np.float32)
        return np.stack([b[:, roi].mean(1), b.reshape(len(b), -1).mean(1)], axis=1)

    tr, ctx = read_movie(url, dset, reduce, first)
    return {"roi": tr[:, 0].astype(float), "whole": tr[:, 1].astype(float), "series": name, **ctx, **info}


def led_frames(trace: np.ndarray, start=LED_FRAME - 8, stop=LED_FRAME + 30, z=8.0):
    """Frames lit by the LED: the light shows as a step in the recorded intensity. Returns (first, last)
    or None. A step is a first difference above `z` times the robust spread of the baseline differences."""
    d = np.diff(trace)
    base = d[: start - 5]
    spread = 1.4826 * np.median(np.abs(base - np.median(base))) + 1e-9
    seg = d[start:stop]
    up = np.flatnonzero(seg > z * spread)
    if up.size == 0:
        return None
    on = start + up[0] + 1
    down = np.flatnonzero(d[on:on + 25] < -z * spread)
    if down.size == 0:
        return None
    return on, on + down[-1] if down.size and down[-1] < 20 else on + down[0]


def exp2(t, a, b, c, d):
    return a * np.exp(b * t) + c * np.exp(d * t)


def dff(trace, blood_offset, led, bleach=True, baseline="a", led_frame=LED_FRAME, led_s=None):
    """dF/F0 in percent, with the LED frames removed (SI Image Data Analysis).

    Returns (t, y): t in seconds from the first frame after the LED (time-origin reading a), y the dF/F0.
    bleach: two-term exponential fitted to the baseline and the last 2 min and subtracted (cAMP only).
    Without it (Ca2+), the baseline mean is subtracted. Both are divided by the Adjusted Offset (mean of
    the first 10 frames minus the Blood Offset), the background-corrected baseline of the SI passage.
    baseline: "a" the whole pre-LED baseline, "b" the last 30 s before the LED (claims header).
    """
    if led is None:
        n = max(1, int(round((led_s or 0) * FPS)))     # nominal LED frames when no step is seen
        led = (led_frame, led_frame + n - 1)
    on, off = led
    keep = np.r_[0:on, off + 1:len(trace)]
    y = trace[keep].astype(float)
    t = (np.arange(len(trace))[keep] - (off + 1)) / FPS
    adjusted = trace[:10].mean() - blood_offset
    if bleach:
        sel = (t < 0) | (t >= t[-1] - 120)
        tt = (t - t[0]) / 100.0
        try:
            p0 = (y[0] - y[-1], -0.5, y[-1], -0.01)
            p, _ = optimize.curve_fit(exp2, tt[sel], y[sel], p0=p0, maxfev=20000)
            fit = exp2(tt, *p)
        except RuntimeError:
            fit = np.polyval(np.polyfit(tt[sel], y[sel], 2), tt)
        y = (y - fit) / adjusted * 100
    else:
        pre = t < 0 if baseline == "a" else (t < 0) & (t >= -30)
        y = (y - y[pre].mean()) / adjusted * 100
    pre = t < 0 if baseline == "a" else (t < 0) & (t >= -30)
    y = y - y[pre].mean()
    return t, y


def params(t, y, led_s, filt, window_s=200.0):
    """Peak, rise time, 80% decay time and duration of a transient, under each open reading.

    filt: median filter length in frames (20 anesthetized, 50 awake; SI Image Data Analysis).
    Peak is read on the filtered ("f") and the unfiltered ("u") trace; decay always on the filtered
    one. Time origin "a" is the first frame after the LED, "b" the LED onset (adds the LED duration).
    Decay "a" is the time from the peak until the signal falls below 80% of the peak, "b" below 20%.
    """
    post = (t >= 0) & (t <= window_s)
    ys = signal.medfilt(y, filt + 1 - filt % 2)
    out = {}
    for which, yy in (("f", ys), ("u", y)):
        i = np.flatnonzero(post)[np.argmax(yy[post])]
        peak, rise = yy[i], t[i]
        for dec, frac in (("a", 0.8), ("b", 0.2)):
            after = np.flatnonzero((t > t[i]) & (ys < frac * peak))
            decay = t[after[0]] - t[i] if after.size else np.nan
            for org, shift in (("a", 0.0), ("b", led_s)):
                out[(which, dec, org)] = {"peak": peak, "rise": rise + shift, "decay": decay,
                                          "duration": rise + shift + decay}
    return out


def params_table(t, y, led_s, filt) -> pd.DataFrame:
    p = params(t, y, led_s, filt)
    return pd.DataFrame([{"peak_on": k[0], "decay_reading": k[1], "origin": k[2], **v} for k, v in p.items()])


READINGS = [(b, pk, dec, org) for b in "ab" for pk in "fu" for dec in "ab" for org in "ab"]


def reading_name(r) -> str:
    return f"F0{r[0]}-peak{r[1]}-decay{r[2]}-t0{r[3]}"


def astro_params(traces: dict, assets: pd.DataFrame, filt: int, bleach: bool, led: bool = True) -> pd.DataFrame:
    """Peak, rise, decay and duration for every recording under every reading of the claims header.

    One row per file and reading. `led` False for sensory stimulation (no LED frames; onset at frame 325)."""
    rows = []
    meta = assets.set_index("path")
    for path, r in traces.items():
        if r.get("empty"):
            continue
        a = meta.loc[path]
        led_s = a.led_s if led else 0.0
        steps = led_frames(r["roi"]) if led else (LED_FRAME, LED_FRAME - 1)
        for base in "ab":
            t, y = dff(r["roi"], r["blood_offset"], steps, bleach=bleach, baseline=base, led_s=led_s)
            p = params(t, y, led_s, filt, window_s=t[-1])
            for (pk, dec, org), v in p.items():
                rows.append({"path": path, "subject": a.subject, "group": a.group, "genotype": a.genotype,
                             "recording": a.recording, "led_s": a.led_s,
                             "reading": reading_name((base, pk, dec, org)), **v})
    return pd.DataFrame(rows)


def mean_trace(traces: dict, paths, bleach: bool, baseline: str = "a", led: bool = True, led_s: float = 1.0):
    """Mean dF/F0 over recordings on a common time base (s from the first frame after the LED)."""
    ys = []
    for p in paths:
        r = traces[p]
        steps = led_frames(r["roi"]) if led else (LED_FRAME, LED_FRAME - 1)
        t, y = dff(r["roi"], r["blood_offset"], steps, bleach=bleach, baseline=baseline, led_s=led_s)
        grid = np.arange(-60, t[-1] - 5, 1 / FPS)
        ys.append(np.interp(grid, t, y))
    n = min(len(y) for y in ys)
    return grid[:n], np.mean([y[:n] for y in ys], axis=0)
