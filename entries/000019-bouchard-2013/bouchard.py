"""Loading, high gamma and shared measures for dandiset 000019 (Bouchard et al. 2013).

Bouchard KE, Mesgarani N, Johnson K, Chang EF (2013). Functional organization of human
sensorimotor cortex for speech articulation. Nature 495, 327-332. doi:10.1038/nature11911.

The dandiset holds, per recording block, raw ECoG from a 256-channel grid at 3051.76 Hz, a trial
table (syllable spoken, start, consonant-to-vowel transition and stop times), a `bad` flag per
electrode, an anatomical label per electrode, and a rest period. It has no audio and no high gamma,
so high gamma is computed here from the raw voltage.

Files are streamed from the archive at the pinned version: each file's bytes are fetched into
memory with parallel HTTP range requests and opened with h5py from memory. Nothing is written to
disk. The files are 0.6 to 2.8 GB and every sample is needed (common average reference over all
good channels, and trials cover the whole block), so reading the whole file in large requests is
much faster than h5py's chunk-by-chunk reads over the network.

Where the parameters come from:

- Bad channels are the dataset's `bad` flags; the claims file's header says to use them. The
  common average reference is over the remaining channels (Methods, via the claims header).
- High gamma: eight Gaussian band-pass filters with centres log-spaced from 85 to 175 Hz (Methods)
  and standard deviations 0.39 * sqrt(centre) Hz, which grow semi-logarithmically. The paper gives
  no widths; the claims header calls the bank of Mesgarani and Chang (2012) the standard choice,
  and this form is the one used in the Chang lab's published preprocessing code. It is a standard
  choice that is not expected to change an outcome. The analytic amplitude is taken in the
  frequency domain (filter, keep positive frequencies, inverse transform), which is the Hilbert
  transform of the filtered signal. The inverse transform is taken on the bins below 400 Hz, which
  gives the amplitude sampled at about 400 Hz without aliasing (the filters fall to zero well below
  400 Hz); this is a computational shortcut, not a change of method. The mean amplitude over the
  eight bands is interpolated onto a 200 Hz grid (5 ms steps, Methods).
- z-scoring per channel against baseline data (Methods). The claims file leaves the baseline open
  and names three readings, all computed: (a) `pre`, the 500 ms windows from -1000 to -500 ms before
  each C-V transition, pooled over the block's trials; (b) `whole`, the whole block; (c) `rest`, the
  rest period the dataset marks as baseline (reading (c) was added to the claims file on 2026-10-22
  in answer to a question). Statistics are per block and channel.
- Epoch -500 to +750 ms around the C-V transition (claims header), 251 samples at 5 ms.
- Syllable labels: the dataset spells syllables as consonant + `aa`, `ee` or `oo` (/a/, /i/, /u/),
  and /j/ as `y`. Two labels differ only in spelling (`she` for `shee`, `ha` for `haa`) and are
  merged. Labels with no consonant (vowels alone) are not CV syllables and are left out.
- The articulator state matrix (Supplementary Figure 1d) and the phonetic feature matrix
  (Supplementary Figure 12) are given only as figures in the supplement; they are transcribed
  below from the supplement PDF (light cells 1, dark cells 0 in Supplementary Figure 1d, whose
  /b/ row has Lips light and Tongue dark; white 1 and black 0 in Supplementary Figure 12, as its
  legend says). They are the paper's definitions of its variables, not data.
"""

from __future__ import annotations

import io
import re
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import requests
import scipy.fft
from dandi.dandiapi import DandiAPIClient

DANDISET_ID = "000019"
DANDISET_VERSION = "0.220126.2148"
SUBJECTS = ["EC2", "GP31", "GP33"]   # EC9 is in the dandiset but not in the paper

HG_CENTRES = np.logspace(np.log10(85.0), np.log10(175.0), 8)
HG_SDS = 10 ** (np.log10(0.39) + 0.5 * np.log10(HG_CENTRES))
ENVELOPE_HZ = 400.0
HG_HZ = 200.0
EPOCH_MS = np.arange(-500, 751, 5)          # analysis epoch
PRE_MS = (-1000, -500)                      # baseline reading `pre`
BASELINES = ("pre", "whole", "rest")
VSMC_LABELS = ("precentral", "postcentral")

CONSONANTS = ["b", "d", "f", "g", "h", "k", "l", "m", "n", "p", "r", "s", "sh", "t", "th", "v",
              "w", "y", "z"]
VOWELS = {"aa": "a", "ee": "i", "oo": "u"}
SPELLING = {"she": "shee", "ha": "haa"}

# Supplementary Figure 1d, consonant part: one string per articulator, one digit per consonant
# in the order of CONSONANTS (the figure's three vowel columns of a consonant are identical).
ARTICULATORS = ["Lips", "Tongue", "Larynx", "Jaw"]
_ARTIC_ROWS = {
    "Lips":   "1010000101000001100",
    "Tongue": "0101011010111110111",
    "Larynx": "1101001110100001111",
    "Jaw":    "1110001111111111111",
}
# Vowel part of Supplementary Figure 1d.
VOWEL_ARTICULATORS = ["Back Tongue", "High Tongue"]
_VOWEL_ROWS = {"Back Tongue": {"a": 1, "i": 0, "u": 1}, "High Tongue": {"a": 0, "i": 1, "u": 1}}

# Supplementary Figure 12: nine constriction location, six degree/shape and four vowel features.
LOCATION = ["Bilabial", "Secondary Labial", "Labiodental", "Dental", "Alveolar", "Post Alveolar",
            "Velar", "Voiced", "Mandibular"]
DEGREE = ["Oral Stop", "Fricative", "Approximate", "Nasal Stop", "Lateral", "Rhotic"]
VOWEL_FEATURES = ["Back Tongue", "High Tongue", "Lip Rounding", "Jaw Open"]
_FEATURE_ROWS = {
    "Bilabial":         "1000000101000000100",
    "Secondary Labial": "0000000000101000000",
    "Labiodental":      "0010000000000001000",
    "Dental":           "0000000000000010000",
    "Alveolar":         "0100001010010100001",
    "Post Alveolar":    "0000000000101000010",
    "Velar":            "0001010000000000100",
    "Voiced":           "1101001110100001111",
    "Mandibular":       "1110001111111111111",
    "Oral Stop":        "1101010111000100000",
    "Fricative":        "0010000000011011001",
    "Approximate":      "0000000000100000110",
    "Nasal Stop":       "0000000110000000000",
    "Lateral":          "0000001000000000000",
    "Rhotic":           "0000000000100000000",
}
_VOWEL_FEATURE_ROWS = {"Back Tongue": {"a": 1, "i": 0, "u": 1}, "High Tongue": {"a": 0, "i": 1, "u": 1},
                       "Lip Rounding": {"a": 0, "i": 0, "u": 1}, "Jaw Open": {"a": 1, "i": 0, "u": 0}}

# Major oral articulator of each consonant, read from the constriction location features
# (claims header). Reading (a) leaves /h/, /r/, /w/ and /j/ out; reading (b) puts /r/ with the
# coronal, /w/ with the labial and /j/ with the dorsal consonants, and leaves /h/ out.
_MAJOR_A = {"labial": ["b", "p", "m", "f", "v"],
            "coronal": ["d", "t", "n", "l", "s", "z", "th", "sh"],
            "dorsal": ["g", "k"]}
MAJOR = {"a": {c: k for k, cs in _MAJOR_A.items() for c in cs}}
MAJOR["b"] = {**MAJOR["a"], "r": "coronal", "w": "labial", "y": "dorsal"}
SIBILANTS = ["s", "z", "sh"]   # Fig. 5a legend groups: labial, coronal tongue, dorsal tongue, sibilant


def parse_label(label: str) -> tuple[str, str] | None:
    """(consonant, vowel) of a trial label, or None if it is not a CV syllable of the task."""
    label = SPELLING.get(label, label)
    m = re.fullmatch(r"([a-z]*?)(aa|ee|oo)", label)
    if not m or m.group(1) not in CONSONANTS:
        return None
    return m.group(1), VOWELS[m.group(2)]


def articulator_matrix(cvs: list[tuple[str, str]]) -> np.ndarray:
    """(n CV, 6) binary matrix: Lips, Tongue, Larynx, Jaw, Back Tongue, High Tongue."""
    rows = []
    for c, v in cvs:
        i = CONSONANTS.index(c)
        rows.append([int(_ARTIC_ROWS[a][i]) for a in ARTICULATORS]
                    + [_VOWEL_ROWS[a][v] for a in VOWEL_ARTICULATORS])
    return np.array(rows, dtype=float)


def feature_matrix(cvs: list[tuple[str, str]], which: str) -> np.ndarray:
    """Phonetic features of each CV: `location`, `degree` or `vowel` (Supplementary Figure 12)."""
    rows = []
    for c, v in cvs:
        i = CONSONANTS.index(c)
        if which == "vowel":
            rows.append([_VOWEL_FEATURE_ROWS[f][v] for f in VOWEL_FEATURES])
        else:
            names = LOCATION if which == "location" else DEGREE
            rows.append([int(_FEATURE_ROWS[f][i]) for f in names])
    return np.array(rows, dtype=float)


# ----------------------------------------------------------------------------------------------
# Reading the archive

def assets() -> list[dict]:
    """Path, size and streaming URL of every file at the pinned version."""
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        return sorted(({"path": a.path, "size": a.size,
                        "url": a.get_content_url(follow_redirects=1, strip_query=True)}
                       for a in ds.get_assets()), key=lambda a: a["path"])


def dandiset_metadata() -> dict:
    with DandiAPIClient() as client:
        return client.get_dandiset(DANDISET_ID, DANDISET_VERSION).get_raw_metadata()


_session = requests.Session()
_session.mount("https://", requests.adapters.HTTPAdapter(pool_maxsize=32))


def fetch(url: str, size: int, block: int = 32 * 2**20, threads: int = 16) -> bytes:
    """The whole file, into memory, by parallel range requests."""
    ranges = [(s, min(s + block, size) - 1) for s in range(0, size, block)]

    def get(r):
        for attempt in range(5):
            try:
                resp = _session.get(url, headers={"Range": f"bytes={r[0]}-{r[1]}"}, timeout=120)
                resp.raise_for_status()
                if len(resp.content) == r[1] - r[0] + 1:
                    return resp.content
            except requests.RequestException:
                if attempt == 4:
                    raise
        raise OSError(f"short read of {url} at {r}")

    buf = bytearray(size)
    with ThreadPoolExecutor(threads) as ex:
        for (s, e), part in zip(ranges, ex.map(get, ranges)):
            buf[s:e + 1] = part
    return bytes(buf)


def _text(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def read_metadata(h5: h5py.File) -> dict:
    """Everything but the voltage: electrodes, trials, rest period, invalid times."""
    E = h5["general/extracellular_ephys/electrodes"]
    T = h5["intervals/trials"]
    ES = h5["acquisition/ElectricalSeries"]
    meta = {
        "subject": _text(h5["general/subject/subject_id"][()]),
        "session": _text(h5["general/session_id"][()]),
        "rate": float(ES["starting_time"].attrs["rate"]),
        "t0": float(ES["starting_time"][()]),
        "n_samples": ES["data"].shape[0],
        "n_channels": ES["data"].shape[1],
        "unit": _text(ES["data"].attrs["unit"]),
        "conversion": float(ES["data"].attrs["conversion"]),
        "electrode_ids": E["id"][:],
        "location": np.array([_text(x) for x in E["location"][:]]),
        "bad": E["bad"][:].astype(bool),
        "x": E["x"][:], "y": E["y"][:], "z": E["z"][:],
        "condition": np.array([_text(x) for x in T["condition"][:]]),
        "speak": T["speak"][:],
        "start": T["start_time"][:], "stop": T["stop_time"][:], "cv": T["cv_transition_time"][:],
        "rest": [(float(a), float(b)) for a, b in zip(h5["intervals/epochs/start_time"][:],
                                                    h5["intervals/epochs/stop_time"][:])],
        "rest_labels": [_text(x) for x in h5["intervals/epochs/label"][:]],
    }
    if "invalid_times" in h5["intervals"]:
        I = h5["intervals/invalid_times"]
        meta["invalid"] = np.c_[I["start_time"][:], I["stop_time"][:]]
    else:
        meta["invalid"] = np.zeros((0, 2))
    return meta


# ----------------------------------------------------------------------------------------------
# High gamma

def high_gamma(raw: np.ndarray, rate: float, good: np.ndarray, batch: int = 32) -> tuple[np.ndarray, float]:
    """High-gamma amplitude of every good channel, sampled at about 400 Hz.

    raw is (samples, channels). Returns (envelope, envelope_rate); bad channels are NaN.
    """
    n, nch = raw.shape
    car = raw[:, good].mean(axis=1, dtype=np.float64).astype(np.float32)
    freqs = np.fft.rfftfreq(n, 1.0 / rate)
    k = int(np.ceil(n * ENVELOPE_HZ / rate))
    gauss = np.exp(-0.5 * ((freqs[:k, None] - HG_CENTRES[None, :]) / HG_SDS[None, :]) ** 2)
    env = np.full((k, nch), np.nan, dtype=np.float32)
    idx = np.where(good)[0]
    for s in range(0, len(idx), batch):
        ch = idx[s:s + batch]
        x = raw[:, ch] - car[:, None]
        X = scipy.fft.rfft(x, axis=0, workers=4)[:k]
        acc = np.zeros((k, len(ch)), dtype=np.float32)
        for b in range(len(HG_CENTRES)):
            acc += np.abs(scipy.fft.ifft(X * gauss[:, b:b + 1].astype(np.float32), axis=0, workers=4))
        env[:, ch] = acc / len(HG_CENTRES)
    return env, k * rate / n


def resample_to(env: np.ndarray, env_rate: float, times: np.ndarray) -> np.ndarray:
    """Linear interpolation of the envelope (samples, channels) at the given times (s)."""
    pos = np.clip(times * env_rate, 0, env.shape[0] - 1.000001)
    i0 = np.floor(pos).astype(int)
    w = (pos - i0).astype(np.float32)
    shape = times.shape + (env.shape[1],)
    a = env[i0.ravel()].reshape(shape)
    b = env[(i0 + 1).ravel()].reshape(shape)
    return a + (b - a) * w[..., None]


def process_block(asset: dict, buf: bytes | None = None) -> dict:
    """One block: metadata, and per trial the z-scored high gamma in the epoch, per baseline.

    Returns metadata plus `epochs[baseline]` (trials, channels, 251) float32 for the trials whose
    window from -1000 to +750 ms lies inside the recording, `kept` (their trial indices), and
    `hg_stats` (per-channel baseline mean and SD of the 200 Hz high gamma, per baseline).
    """
    if buf is None:
        buf = fetch(asset["url"], asset["size"])
    with h5py.File(io.BytesIO(buf), "r") as h5:
        meta = read_metadata(h5)
        raw = h5["acquisition/ElectricalSeries/data"][:]
    del buf
    good = ~meta["bad"]
    env, env_rate = high_gamma(raw, meta["rate"], good)
    duration = raw.shape[0] / meta["rate"]
    del raw
    grid = np.arange(0, duration, 1 / HG_HZ)
    hg = resample_to(env, env_rate, grid)                  # whole block at 200 Hz
    cv = meta["cv"] - meta["t0"]
    kept = np.where((cv + PRE_MS[0] / 1000 >= 0) & (cv + EPOCH_MS[-1] / 1000 < duration))[0]
    pre_t = cv[kept, None] + np.arange(PRE_MS[0], PRE_MS[1], 5)[None, :] / 1000
    pre = resample_to(env, env_rate, pre_t)                # (trials, 100, channels)
    ep_t = cv[kept, None] + EPOCH_MS[None, :] / 1000
    ep = resample_to(env, env_rate, ep_t)                  # (trials, 251, channels)
    stats = {
        "pre": (np.nanmean(pre, axis=(0, 1)), np.nanstd(pre, axis=(0, 1))),
        "whole": (np.nanmean(hg, axis=0), np.nanstd(hg, axis=0)),
    }
    rest = np.zeros(len(grid), bool)
    for a, b in meta["rest"]:
        rest |= (grid >= a - meta["t0"]) & (grid < b - meta["t0"])
    stats["rest"] = (np.nanmean(hg[rest], axis=0), np.nanstd(hg[rest], axis=0))
    labels = [parse_label(c) for c in meta["condition"][kept]]
    sums = {}
    keys = sorted({p for p in labels if p is not None})
    for name, (m, s) in stats.items():
        z = ((ep - m) / s).transpose(0, 2, 1)
        sums[name] = {p: z[[i for i, q in enumerate(labels) if q == p]].sum(axis=0, dtype=np.float64)
                      for p in keys}
    meta.update(sums=sums, labels=labels, kept=kept, hg_stats=stats, duration=duration,
                rest_seconds=float(rest.sum() / HG_HZ), env_rate=env_rate)
    return meta


def process_blocks(block_assets: list[dict], log=print) -> list[dict]:
    """process_block over several files, fetching the next file while one is processed."""
    out = []
    with ThreadPoolExecutor(1) as ex:
        nxt = ex.submit(fetch, block_assets[0]["url"], block_assets[0]["size"])
        for i, a in enumerate(block_assets):
            buf = nxt.result()
            if i + 1 < len(block_assets):
                nxt = ex.submit(fetch, block_assets[i + 1]["url"], block_assets[i + 1]["size"])
            out.append(process_block(a, buf))
            del buf
            log(f"{a['path']}: {len(out[-1]['kept'])} trials")
    return out


def load_subject(blocks: list[dict]) -> dict:
    """Pool the blocks of one subject into per-syllable mean z-scored high gamma.

    Electrodes flagged bad in any block are left out of the subject's analyses (`good`). Returns
    `cvs` (sorted (consonant, vowel) pairs), `counts` (renditions per CV), `H[baseline]`
    (CV, channel, 251) means over renditions, and the electrode metadata of the first block.
    """
    first = blocks[0]
    good = ~np.any([b["bad"] for b in blocks], axis=0)
    cvs = sorted({p for b in blocks for p in b["labels"] if p is not None},
                 key=lambda p: (CONSONANTS.index(p[0]), "aiu".index(p[1])))
    counts = np.array([sum(q == p for b in blocks for q in b["labels"]) for p in cvs])
    H = {}
    for name in BASELINES:
        total = np.zeros((len(cvs), first["n_channels"], len(EPOCH_MS)))
        for b in blocks:
            for p, v in b["sums"][name].items():
                total[cvs.index(p)] += np.nan_to_num(v)
        H[name] = (total / counts[:, None, None]).astype(np.float32)
        H[name][:, ~good] = np.nan
    return {
        "subject": first["subject"], "cvs": cvs, "counts": counts,
        "n_unparsed": int(sum(q is None for b in blocks for q in b["labels"])), "H": H, "good": good,
        "location": first["location"], "x": first["x"], "y": first["y"], "z": first["z"],
        "electrode_ids": first["electrode_ids"],
        "vsmc": np.where(good & np.isin(first["location"], VSMC_LABELS))[0],
    }


# ----------------------------------------------------------------------------------------------
# Measures (the claim each comes from is named; the claims file cites the paper for each)

def ms_index(ms) -> np.ndarray:
    """Index into EPOCH_MS of a time or array of times in ms."""
    return np.searchsorted(EPOCH_MS, np.asarray(ms))


def _residuals(y: np.ndarray, X: np.ndarray) -> np.ndarray:
    """Residuals of least-squares regression of y (n, ...) on X (n, p) with an intercept."""
    X1 = np.c_[np.ones(len(X)), X]
    beta, *_ = np.linalg.lstsq(X1, y.reshape(len(y), -1), rcond=None)
    return (y.reshape(len(y), -1) - X1 @ beta).reshape(y.shape)


def partial_correlation(H: np.ndarray, A: np.ndarray) -> np.ndarray:
    """Methods Eq. 4. H (CV, electrode, time), A (CV, k). Returns rho (electrode, k, time)."""
    out = np.empty((H.shape[1], A.shape[1], H.shape[2]))
    for i in range(A.shape[1]):
        others = np.delete(A, i, axis=1)
        rh = _residuals(H, others)
        ra = _residuals(A[:, i], others)
        num = np.einsum("c,cet->et", ra, rh)
        out[:, i] = num / (np.sqrt((ra ** 2).sum()) * np.sqrt((rh ** 2).sum(axis=0)))
    return out


def timing(rho_e: np.ndarray, level: float) -> tuple[float, float, float]:
    """Onset, peak and offset times (ms) of one electrode's rho time course: the peak, and the
    first and last times of the contiguous run around it that stays above `level`."""
    p = int(np.argmax(rho_e))
    above = rho_e > level
    a = p
    while a > 0 and above[a - 1]:
        a -= 1
    b = p
    while b < len(rho_e) - 1 and above[b + 1]:
        b += 1
    return float(EPOCH_MS[a]), float(EPOCH_MS[p]), float(EPOCH_MS[b])


def glm(H: np.ndarray, Ac: np.ndarray):
    """Methods Eq. 2 by least squares at each electrode and time.

    H (CV, electrode, time), Ac (CV, 4). Returns beta (electrode, 4, time), the F-test p of the
    whole model (electrode, time), each coefficient's t-test p (electrode, 4, time) and R2.
    """
    from scipy import stats
    n, k = Ac.shape
    X = np.c_[np.ones(n), Ac]
    Y = H.reshape(n, -1)
    XtX_inv = np.linalg.inv(X.T @ X)
    beta = XtX_inv @ X.T @ Y
    resid = Y - X @ beta
    sse = (resid ** 2).sum(0)
    sst = ((Y - Y.mean(0)) ** 2).sum(0)
    df = n - k - 1
    r2 = 1 - sse / sst
    F = (r2 / k) / ((1 - r2) / df)
    pF = stats.f.sf(F, k, df)
    se = np.sqrt(np.outer(np.diag(XtX_inv), sse / df))
    pt = 2 * stats.t.sf(np.abs(beta / se), df)
    shape = H.shape[1:]
    return (beta[1:].reshape(k, *shape).transpose(1, 0, 2), pF.reshape(shape),
            pt[1:].reshape(k, *shape).transpose(1, 0, 2), r2.reshape(shape))


def zscore_for_pca(Hv: np.ndarray, mode: str) -> np.ndarray:
    """Hv (CV, electrode, time). `row`: each electrode's concatenated (CV x time) series z-scored;
    `time`: each electrode z-scored across syllables at each time."""
    if mode == "row":
        m = Hv.mean(axis=(0, 2), keepdims=True)
        s = Hv.std(axis=(0, 2), keepdims=True)
    else:
        m = Hv.mean(axis=0, keepdims=True)
        s = Hv.std(axis=0, keepdims=True)
    return (Hv - m) / s


def project(M: np.ndarray, X: np.ndarray) -> np.ndarray:
    """States K (CV, n_pc, time) = M' X (Methods Eq. 5), X (CV, electrode, time)."""
    return np.einsum("ep,cet->cpt", M, X)


def state_space(Hv: np.ndarray, mode: str, window=(EPOCH_MS[0], EPOCH_MS[-1]), n_pc: int = 9):
    """PCA of the (electrode x concatenated CV-time) matrix (Methods, PCA and Cortical-State
    Space). Returns M (electrode, n_pc), the fraction of variance of every PC, and the states
    K (CV, n_pc, time) of every CV at every epoch time, projected from the z-scored matrix given
    to the PCA (the claims header's projection reading (i); reading (ii), Hv itself as Eq. 5
    writes it, is `project(M, Hv)`)."""
    Z = zscore_for_pca(Hv, mode)
    sel = (EPOCH_MS >= window[0]) & (EPOCH_MS <= window[1])
    X = Z[:, :, sel].transpose(1, 0, 2).reshape(Z.shape[1], -1)
    U, s, _ = np.linalg.svd(X, full_matrices=False)
    frac = s ** 2 / (s ** 2).sum()
    M = U[:, :n_pc]
    return M, frac, project(M, Z)


def kmeans(X: np.ndarray, k: int, seed: int, n_init: int = 100) -> np.ndarray:
    """k-means labels, Euclidean, best of n_init random starts (a standard choice)."""
    from sklearn.cluster import KMeans
    return KMeans(k, n_init=n_init, random_state=seed).fit_predict(X)


def co_clustering(nc: np.ndarray, ac: np.ndarray) -> np.ndarray:
    """Supplementary Methods Eq. 1 for every token: 1 - |NC delta AC| / (|NC| + |AC|), with NC
    and AC the other members of the token's cluster in each assignment."""
    same_n = nc[:, None] == nc[None, :]
    same_a = ac[:, None] == ac[None, :]
    np.fill_diagonal(same_n, False)
    np.fill_diagonal(same_a, False)
    sym = (same_n ^ same_a).sum(1)
    tot = same_n.sum(1) + same_a.sum(1)
    with np.errstate(invalid="ignore", divide="ignore"):
        return 1 - sym / tot


def separability(D: np.ndarray, labels: np.ndarray, weights: np.ndarray | None = None) -> np.ndarray:
    """Mean between-cluster distance minus mean within-cluster distance (Methods, Cluster
    Separability). D (time, n, n) pairwise distances; labels per token, per time when 2-D
    (time, n). weights (B, n) are bootstrap counts of each token; returns (B, time) then."""
    n = D.shape[1]
    lab = labels if labels.ndim == 2 else np.broadcast_to(labels, (D.shape[0], n))
    same = (lab[:, :, None] == lab[:, None, :]).astype(float)
    if weights is None:
        weights = np.ones((1, n))
    w = np.asarray(weights, float)

    def quad(A):
        """sum over i, j of w[b, i] A[t, i, j] w[b, j], as one matrix product: (B, time)."""
        X = (w @ A.transpose(1, 0, 2).reshape(n, -1)).reshape(len(w), A.shape[0], n)
        return np.einsum("btj,bj->bt", X, w)

    total_pairs = w.sum(1) ** 2 - w.sum(1)                          # (B,)
    within_pairs = quad(same) - w.sum(1)[:, None]
    within_sum = quad(same * D)
    all_sum = quad(D)
    between = (all_sum - within_sum) / (total_pairs[:, None] - within_pairs)
    return between - within_sum / within_pairs
