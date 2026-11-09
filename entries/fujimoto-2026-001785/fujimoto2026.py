"""Loading and measures for dandiset 001785 (Fujimoto, Fujimoto, Elorette et al. 2026,
Nature Neuroscience, doi:10.1038/s41593-026-02301-4).

The dandiset holds NIfTI and TIFF files, not NWB: per-session FA maps and T1w images
(MRI/FA), one seed connectivity map per session (MRI/FC), CC1 and DAPI immunofluorescence
images (IF) and electron micrographs (EM). Files are streamed from the archive into memory;
nothing is written to disk.

The paper's own deposit, DANDI:001773 version 0.260416.1939 (Data and Code availability),
holds its MATLAB scripts and source-data spreadsheets. Here it supplies only labels that the
dandiset lacks: which voxels form each tract, CB subregion or target ROI, and the behaviour
bins of the claims marked data elsewhere. The measurements analysed (FA, normalized seed
connectivity, cell counts) are read from the dandiset itself; the link claims of the notebook
show that the voxels can be matched.

Where each parameter comes from is said at the parameter: the claims file (which cites the
paper or its code), a passage of the paper (author, step 1.6), an assumption, or a standard
choice for a detail that cannot change a result.
"""
import gzip
import io
import re
from functools import lru_cache

import numpy as np
import pandas as pd
import requests
import statsmodels.formula.api as smf
from scipy import stats

DANDISET = "001785"
VERSION = "0.260615.1835"
SOURCE_DANDISET = "001773"
SOURCE_VERSION = "0.260416.1939"
API = "https://api.dandiarchive.org/api"

# Monkey codes of the paper's spreadsheets (1 N, 2 T, 3 D) and the stimulated (for D,
# implanted) hemisphere: left in N and D, right in T (Methods, SCC-DBS implantation surgery).
STIM_HEMI = {"N": "L", "T": "R", "D": "L"}


# ---------------------------------------------------------------- archive access

@lru_cache(maxsize=None)
def assets(dandiset=DANDISET, version=VERSION):
    """All assets of a published version, as a DataFrame (path, size, asset_id, blob)."""
    url = f"{API}/dandisets/{dandiset}/versions/{version}/assets/?page_size=1000"
    rows = []
    while url:
        page = requests.get(url, timeout=60).json()
        rows += page["results"]
        url = page["next"]
    return pd.DataFrame(rows)[["path", "size", "asset_id", "blob"]]


def fetch(path, dandiset=DANDISET, version=VERSION):
    """Stream one asset into memory and return its bytes."""
    a = assets(dandiset, version)
    aid = a.loc[a.path == path, "asset_id"].iloc[0]
    r = requests.get(f"{API}/assets/{aid}/download/", timeout=300)
    r.raise_for_status()
    return r.content


def load_nifti(path):
    import nibabel as nib
    raw = fetch(path)
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    return nib.Nifti1Image.from_bytes(raw)


def load_tiff(path):
    """A TIFF asset as an array (the data of the image, streamed into memory)."""
    import tifffile
    with tifffile.TiffFile(io.BytesIO(fetch(path))) as tif:
        return tif.asarray()


@lru_cache(maxsize=None)
def source_sheet(name, header=0):
    """A source-data spreadsheet of DANDI:001773 (the paper's deposit), first sheet."""
    raw = fetch(f"source_data/{name}", SOURCE_DANDISET, SOURCE_VERSION)
    df = pd.read_excel(io.BytesIO(raw), header=header, engine="openpyxl")
    df.columns = [str(c).strip() for c in df.columns]
    return df


# ---------------------------------------------------------------- FA voxels

def fa_map(monkey, session):
    """FA map of monkey N, T or D, session 'pre' or 'post' (MRI/FA/data_FA_mk*_*DBS)."""
    return load_nifti(f"MRI/FA/data_FA_mk{monkey}_{session}DBS.nii.gz")


def match_values(volume, values):
    """Locate each value in a volume by exact equality of float32 values.

    The dandiset has no tract masks. The paper's source data list the FA of each tract voxel
    without its position; FA values are continuous, so a value found once in the session's map
    identifies the voxel. Returns, per value, the flat voxel index (or -1 when not found) and
    the number of voxels holding that value.
    """
    flat = np.asarray(volume, dtype=np.float32).ravel()
    order = np.argsort(flat, kind="stable")
    sv = flat[order]
    v = np.asarray(values, dtype=np.float32)
    lo = np.searchsorted(sv, v, side="left")
    hi = np.searchsorted(sv, v, side="right")
    nmatch = hi - lo
    idx = np.where(nmatch > 0, order[np.clip(lo, 0, len(sv) - 1)], -1)
    return idx, nmatch


# ---------------------------------------------------------------- seed connectivity voxels

def fc_map(monkey, session):
    """Seed connectivity map (MRI/FC). File names differ by group: *_preDBS/_postDBS for N
    and T, *_preope/_postope for D, *_pre/_post for B, W and H."""
    suffix = {"N": "DBS", "T": "DBS", "D": "ope"}.get(monkey, "")
    return load_nifti(f"MRI/FC/data_FC_mk{monkey}_{session}{suffix}.nii.gz")


def rai_to_index(img, x, y, z):
    """Voxel indices of AFNI (RAI, DICOM order) coordinates in mm on a NIfTI (RAS) grid.

    The paper's spreadsheets give voxel centres as AFNI prints them, x and y with the sign of
    the RAI convention; the NIfTI affine is RAS, so x and y change sign. The notebook shows
    that this places every listed voxel on a grid centre.
    """
    xyz = np.c_[-np.asarray(x), -np.asarray(y), np.asarray(z), np.ones(len(x))]
    ijk = np.linalg.solve(img.affine, xyz.T).T[:, :3]
    r = np.round(ijk).astype(int)
    return r, np.abs(ijk - r).max()


# ---------------------------------------------------------------- MATLAB anovan and multcompare

def anovan(df, y, factors, terms):
    """MATLAB anovan with type III sums of squares (its default 'sstype' 3).

    `terms` are tuples of factor names, as the rows of the scripts' model matrices. Effects are
    coded sum-to-zero, which gives MATLAB's type III tests. Returns the table (F, df, p, partial
    eta squared) and the fitted model.
    """
    rhs = " + ".join(":".join(f"C({f}, Sum)" for f in t) for t in terms)
    model = smf.ols(f"{y} ~ {rhs}", data=df).fit()
    import statsmodels.api as sm
    tab = sm.stats.anova_lm(model, typ=3)
    names = {":".join(f"C({f}, Sum)" for f in t): " x ".join(t) for t in terms}
    tab = tab.rename(index=names)
    ss_err = tab.loc["Residual", "sum_sq"]
    tab["eta_p2"] = tab["sum_sq"] / (tab["sum_sq"] + ss_err)
    return tab.drop(index="Intercept"), model


def tukey_kramer(df, model, cell_factors, pairs, other=()):
    """MATLAB multcompare (Tukey-Kramer, its default) on population marginal means.

    The marginal mean of a cell of `cell_factors` is the model's prediction averaged with equal
    weight over the levels of the factors in `other` (the monkey term), as MATLAB computes it.
    The critical value is the studentized range for all cells of `cell_factors` (the
    'Dimension' argument) and the error df. `pairs` lists (cell_a, cell_b) tuples of level
    tuples; returns mean_a, mean_b, difference (b - a) and p for each.
    """
    levels = [sorted(df[f].unique()) for f in cell_factors]
    k = int(np.prod([len(l) for l in levels]))
    beta = model.params.values
    cov = model.cov_params().values
    dfe = model.df_resid
    X = np.asarray(model.model.exog)
    keys = df[list(cell_factors) + list(other)].to_numpy()

    def lvec(cell):
        # One design row per combination of the other factors' levels; every combination
        # occurs in these data, so a row of the data gives it.
        sel = np.all(keys[:, :len(cell_factors)] == np.asarray(cell), axis=1)
        _, first = np.unique(keys[sel][:, len(cell_factors):], axis=0, return_index=True)
        return X[np.flatnonzero(sel)[first]].mean(axis=0)

    out = []
    for a, b in pairs:
        la, lb = lvec(a), lvec(b)
        ma, mb = la @ beta, lb @ beta
        l = lb - la
        se = np.sqrt(l @ cov @ l)
        q = abs(mb - ma) / se * np.sqrt(2)
        p = float(stats.studentized_range.sf(q, k, dfe))
        out.append(dict(a=a, b=b, mean_a=ma, mean_b=mb, diff=mb - ma, se=se, p=p))
    return pd.DataFrame(out), k, dfe


# ---------------------------------------------------------------- immunofluorescence counts

def parse_if_name(path):
    """Section, hemisphere (L/R) and field number of an IF file name.

    Names come in three styles: 'N633_LW_1', 'N423-LW-1' (with a trailing 'r' in one file) and
    'N102 LW1' (with a trailing 'B' in one file)."""
    stem = path.rsplit("/", 1)[-1].rsplit(".", 1)[0]
    m = re.match(r"^([NTD]\d+)[ _-]([LR])W[ _-]?(\d+)([A-Za-z]?)$", stem)
    if not m:
        return None
    return dict(section=m.group(1), hemi=m.group(2), field=int(m.group(3)), mark=m.group(4))


def section_threshold(pixels, method):
    """Automatic threshold of one channel over all fields of a section.

    The Methods (Immunofluorescence of myelinating oligodendrocytes) say counts were made in
    FIJI 'using section-specific intensity thresholds for each channel' and give no method; the
    claims file ([IF]) names the readings: 'isodata' (FIJI's default method) and 'otsu'.
    """
    from skimage import filters
    return float(getattr(filters, f"threshold_{method}")(pixels))


def count_cells(channel, threshold, min_area):
    """Number of connected objects above threshold with at least `min_area` pixels.

    The paper gives no particle size filter; the notebook runs 10 and 50 pixels as readings
    (an assumption: 10 drops noise specks only; 50 is about half the median object area).
    No watershed split is applied (the paper names none)."""
    from skimage import measure
    lab = measure.label(channel > threshold, connectivity=2)
    areas = np.bincount(lab.ravel())[1:]
    return int(np.sum(areas >= min_area))
