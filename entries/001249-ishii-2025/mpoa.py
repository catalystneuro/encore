"""Loading and measures for Ishii et al. (2025), eLife RP91765, on dandiset 001249.

The dandiset holds the whole-brain light-sheet volumes of Figure 2 (one NWB file per brain).
All other figures rest on the authors' Figshare deposit, doi:10.6084/m9.figshare.27642768.v1,
read here in place with range requests (docs/archives.md, Figshare). Nothing is written to disk.

Where each parameter comes from:
- Peri-event windows, the 0 to +5 s magnitude, the -5 to 0 s baseline and the responder
  threshold of 2 come from the Methods ("In vivo calcium imaging experiments and analysis", "z-scored signal was
  collected from -5 to +15 s around the behavior onset ... The magnitude of z-scored signal was
  quantified by averaging 0 to +5 s from onset. Cells that had larger than 2 d z-scored signal
  were classified as 'responding' cells"), as the claims file gives them.
- The 10 Hz rate and onset at index 50 of the deposited arrays are the code's parameter_dict
  (signal_framerate 10, before_frames 50), read from the deposit.
- The decay-length readings are those of the claims file (fig6c-decay-length).
- The clustering procedure is the claims file's (fig6k-late-cluster-vgat), taken from the
  Methods and "Figure 5 Spectral clustering.ipynb" at commit 4e98c43; the random seed is a
  standard choice.
"""
import io
import pickle
import zipfile

import fsspec
import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET = "001249"
VERSION = "0.241109.2357"
DANDI_API = "https://api.dandiarchive.org/api"

FIGSHARE_ARTICLE = 27642768
FIGSHARE_VERSION = 1
FIGSHARE_DOI = "10.6084/m9.figshare.27642768.v1"
# file ids of version 1, with the MD5 the version's file list gives
FIGSHARE_FILES = {
    "Figure 1 and S1,S2": (50336820, "e0fe143c8294c505637ae703cb314938"),
    "Figure 3, 4, 5, S6, S7, S8": (50336832, "0fd3e73da46d1d188ca666eb5bab4da1"),
    "Figure 6": (50336829, "7fa9c73c187f6dfbd668d8ac4bc3edf9"),
    "Figure S5": (50336838, "350df432df19c06fdd472c059b26b7d7"),
    "Figure S9": (50336835, "b210783cb73eb3a2715d0d49e32380cb"),
    "Figure S10": (50336826, "3c05cad5d99d8432808f8a10f8707587"),
    "Figure S11": (50336844, "88a30dd0316b65db134cd7aced6e6da6"),
    "Figure 2 and S3, S4": (50336841, "ce5ca1efe365689acd42d8975116f00b"),
}


# ---------------------------------------------------------------- DANDI
def dandi_assets():
    """Assets of the pinned version: path, size, asset id and S3 URL."""
    url = f"{DANDI_API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    rows = []
    while url:
        r = requests.get(url, timeout=60).json()
        for a in r["results"]:
            rows.append(dict(path=a["path"], size=a["size"], asset_id=a["asset_id"]))
        url = r["next"]
    df = pd.DataFrame(rows).sort_values("path").reset_index(drop=True)
    df["s3_url"] = [s3_url(a) for a in df.asset_id]
    return df


def s3_url(asset_id):
    md = requests.get(f"{DANDI_API}/dandisets/{DANDISET}/versions/{VERSION}/assets/{asset_id}/",
                      timeout=60).json()
    return [u for u in md["contentUrl"] if "s3" in u][0]


def open_nwb(url):
    """Open an NWB file by streaming (h5py over remfile)."""
    return h5py.File(remfile.File(url), "r")


# ---------------------------------------------------------------- Figshare
def figshare_file_list():
    r = requests.get(f"https://api.figshare.com/v2/articles/{FIGSHARE_ARTICLE}/versions/"
                     f"{FIGSHARE_VERSION}", timeout=60).json()
    return pd.DataFrame([(f["id"], f["name"], f["size"], f["computed_md5"]) for f in r["files"]],
                        columns=["id", "name", "size", "md5"])


_ZIPS = {}


def figshare_zip(name):
    """The zip of one figure, opened in place over range requests."""
    if name not in _ZIPS:
        fid = FIGSHARE_FILES[name][0]
        f = fsspec.open(f"https://ndownloader.figshare.com/files/{fid}",
                        block_size=2**20).open()
        _ZIPS[name] = zipfile.ZipFile(f)
    return _ZIPS[name]


def read_member(name, member):
    """Bytes of one member of a figure's zip; member is the path inside the figure folder."""
    return figshare_zip(name).read(f"{name}/{member}")


def read_csv(name, member, **kw):
    return pd.read_csv(io.BytesIO(read_member(name, member)), **kw)


def read_npy(name, member):
    return np.load(io.BytesIO(read_member(name, member)), allow_pickle=False)


def read_pickle(name, member):
    return pickle.loads(read_member(name, member))


# ---------------------------------------------------------------- statistics as the paper's code runs them
def rm_anova(df, value, subject, within):
    """Repeated-measures ANOVA (statsmodels AnovaRM), as Figure 1.ipynb runs it."""
    from statsmodels.stats.anova import AnovaRM
    t = AnovaRM(data=df, depvar=value, subject=subject, within=[within]).fit().anova_table
    return dict(F=t["F Value"].iloc[0], df1=t["Num DF"].iloc[0], df2=t["Den DF"].iloc[0],
                p=t["Pr > F"].iloc[0])


def tukey(values, groups):
    """Tukey's HSD (statsmodels pairwise_tukeyhsd, FWER 0.05), as the paper's code runs it: the
    levels are treated as independent groups, also for repeated measures."""
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    r = pairwise_tukeyhsd(np.asarray(values, float), np.asarray(groups))
    t = pd.DataFrame(r.summary().data[1:], columns=r.summary().data[0])
    return t[["group1", "group2", "meandiff", "p-adj", "reject"]]


def paired(df, id_col, cond_col, a, b, value):
    """Values of conditions a and b matched by animal id (the code pairs by row order)."""
    x = df[df[cond_col] == a].set_index(id_col)[value]
    y = df[df[cond_col] == b].set_index(id_col)[value]
    ids = sorted(set(x.index) & set(y.index))
    return x.loc[ids].values.astype(float), y.loc[ids].values.astype(float), ids


def bonferroni(p):
    p = np.asarray(p, float)
    return np.minimum(p * len(p), 1.0)


# ---------------------------------------------------------------- calcium imaging measures
RATE_HZ = 10        # parameter_dict signal_framerate
ONSET = 50          # parameter_dict before_frames: index of the onset (-5 s at index 0)


def magnitude(trace):
    """Mean of 0 to +5 s after onset, of a baseline-subtracted peri-event trace (time x cells)."""
    return trace[ONSET:ONSET + 5 * RATE_HZ].mean(0)


def decay_length(long_trace, reading):
    """Decay length in seconds of -5 to +120 s ejaculation traces (time x cells), baseline
    (-5 to 0 s) subtracted first (Methods). Readings of the claims file (fig6c-decay-length):
    'a' time from onset to the first sample below 0 (120 s when it never falls below 0);
    'b' total time below 0 between 0 and +120 s;
    'c' (a variant, not a reading of the claims file) time from the peak after onset to the first
    sample below 0 (120 s when it never falls below 0), the Results' "time for the increased
    calcium signal to return to baseline" read from the peak."""
    x = long_trace - long_trace[:ONSET].mean(0)
    post = x[ONSET:]
    below = post < 0
    if reading == "a":
        first = np.where(below.any(0), below.argmax(0), post.shape[0])
        return first / RATE_HZ
    if reading == "b":
        return below.sum(0) / RATE_HZ
    if reading == "c":
        pk = post.argmax(0)
        out = []
        for i in range(post.shape[1]):
            after = np.where(post[pk[i]:, i] < 0)[0]
            out.append(after[0] if len(after) else post.shape[0])
        return np.array(out) / RATE_HZ
    raise ValueError(reading)


def elbow_pcs(explained_variance_ratio):
    """Number of PCs at the elbow of the scree plot, as Figure 5 Spectral clustering.ipynb
    computes it (distance below the line from the first to the last point)."""
    x = np.asarray(explained_variance_ratio)
    xprime = x - (x[0] + (x[-1] - x[0]) / (x.size - 1) * np.arange(x.size))
    return int(np.argmin(xprime))


def spectral_grid(X, n_clusters=range(2, 12), n_neighbors=np.linspace(10, 70, 13, dtype=int),
                  seed=0):
    """Silhouette (cosine) of spectral clustering (nearest_neighbors affinity) over the grid of
    Figure 5 Spectral clustering.ipynb. The seed is a standard choice; the code sets none."""
    from sklearn.cluster import SpectralClustering
    from sklearn.metrics import silhouette_score
    rows = []
    for k in n_clusters:
        for nn in n_neighbors:
            lab = SpectralClustering(n_clusters=k, affinity="nearest_neighbors",
                                     n_neighbors=int(nn), random_state=seed).fit_predict(X)
            rows.append(dict(n_clusters=k, n_neighbors=int(nn),
                             silhouette=silhouette_score(X, lab, metric="cosine"), labels=lab))
    return pd.DataFrame(rows)


def order_clusters(labels, traces):
    """Renumber clusters by mean response over 0 to +5 s, largest first (the code's
    reorder_clusters), so that cluster 0 is the strongest early response."""
    labels = np.asarray(labels)
    means = {c: traces[ONSET:ONSET + 5 * RATE_HZ, labels == c].mean() for c in np.unique(labels)}
    order = sorted(means, key=lambda c: -means[c])
    remap = {c: i for i, c in enumerate(order)}
    return np.array([remap[c] for c in labels])
