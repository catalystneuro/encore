"""Loading and morphometry for Pelot et al. (2020) on SPARC:60 and its sister datasets.

Every file is streamed from the public SPARC bucket at a pinned object version, taken
from the pinned version's manifest.json (docs/archives.md, "SPARC"). Nothing is written
to disk.

The morphometry repeats the paper's MATLAB code, which is in the dataset
(files/code/HumanRatSegmentationAnalysis_v2.m, PerineuriumComplexMatch_v2.m and
DataPlotting_v4.m of SPARC:60), as the Methods describe it ("Imaging and Image Analysis",
last paragraph): boundaries by bwboundaries, areas by polyarea, effective diameter as the
diameter of the circle of equal area, perineurium thickness as half the difference of the
outer and inner effective diameters. Where this module differs from the code it says so.
"""
import hashlib
import io
import json
import base64

import cv2
import fsspec
import numpy as np
import pandas as pd
import scipy.io as sio
import tifffile
from matplotlib.path import Path
from scipy import ndimage as ndi

BUCKET = "https://sparc-prod-aod-discover-publish50-use1.s3.amazonaws.com"

# Pinned versions: dataset id -> (version, DOI, object version of the version's manifest.json).
# SPARC:60 version 5 is the version the run was given (the latest, 2025-02-24). The sister
# datasets list the paper as IsDescribedBy. SPARC:65 is pinned at version 6, the version the
# paper's supplement cites (Pelot et al., 2020a, doi:10.26275/nluu-1ews), and SPARC:89 at
# version 1, which it also cites (2020b); for SPARC:64 the supplement's list stops before
# 2020f, so its latest version, 4 (2020-10-01), is pinned.
DATASETS = {
    "60": (5, "10.26275/lg3c-1kjf", "7StJiyPYtSBkyV9XnmU0AcrXETX4pUUS"),  # rat MT
    "65": (6, "10.26275/nluu-1ews", "jNXQGEZzLg_iftJTVomAAim2y47X_MsN"),  # human IHC
    "64": (4, "10.26275/maq2-eii4", "r5MEOSh3l2JKtHbFSUK3wQw4BNPRopiH"),  # pig MT
    "89": (1, "10.26275/8pc2-rhu2", "Eu20.3wWopX9n4CwwpIjyXbnls2PYuEU"),  # pig IF
}

_MANIFESTS = {}
READ = {}  # (dataset, path) -> sha256 hex of each file read, for the notebook header


def manifest(ds):
    if ds not in _MANIFESTS:
        url = f"{BUCKET}/{ds}/manifest.json?versionId={DATASETS[ds][2]}"
        with fsspec.open(url, block_size=2**20) as f:
            m = json.load(f)
        assert m["version"] == DATASETS[ds][0], (ds, m["version"])
        _MANIFESTS[ds] = m
    return _MANIFESTS[ds]


def files(ds):
    return {f["path"]: f for f in manifest(ds)["files"]}


def read(ds, path):
    """Read one file of a pinned dataset version into memory and check its SHA-256."""
    f = files(ds)[path]
    url = f"{BUCKET}/{ds}/{path}?versionId={f['s3VersionId']}"
    with fsspec.open(url, block_size=2**20) as fh:
        b = fh.read()
    h = hashlib.sha256(b)
    if f.get("sha256"):
        assert base64.b64encode(h.digest()).decode() == f["sha256"], path
    READ[(ds, path)] = h.hexdigest()
    return b


SUPPLEMENT_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7672126/supplementaryFiles"
SUPPLEMENT4_SHA256 = "2e8f9c6428c14df171dd97a2e378561848060beb0a0a7e3b347288495ef3a6a2"


def supplement4():
    """Supplement 4 of the paper (Data_Sheet_2.xlsx, "Summary statistics and literature
    review"), from the supplementary files of the version of record in Europe PMC
    (PMC7672126), read into memory. The zip is built on request, so the spreadsheet itself
    is checked against its SHA-256."""
    import requests
    import zipfile
    z = zipfile.ZipFile(io.BytesIO(requests.get(SUPPLEMENT_URL, timeout=300).content))
    b = z.read("Data_Sheet_2.xlsx")
    h = hashlib.sha256(b).hexdigest()
    assert h == SUPPLEMENT4_SHA256, h
    READ[("PMC7672126", "Data_Sheet_2.xlsx")] = h
    raw = pd.read_excel(io.BytesIO(b), header=None)
    rows, section, species, level, ref = [], None, None, None, None
    for _, r in raw.iloc[4:].iterrows():
        v0 = r[0]
        if isinstance(v0, str) and pd.isna(r[1]) and r[2:14].isna().all():
            section, species, level, ref = v0.strip(), None, None, None
            continue
        if isinstance(v0, str):
            species, level, ref = v0, r[1], None
            ours = dict(median=r[2], mean=r[3], sd=r[4], min=r[5], max=r[6])
        if isinstance(r[7], str):
            ref = r[7]
        if section is None or species is None:
            continue
        notes = r[15] if isinstance(r[15], str) else ""
        # A row with a mean but no reference, laterality or n continues the study above it:
        # its notes say it is that study's mean converted between diameter and area
        # ("Calculated mean(d_nerve) from mean(A_nerve)"), a second value for the same nerves.
        derived = not isinstance(r[7], str) and pd.isna(r[10]) and pd.isna(r[11]) and notes.startswith("Calculated mean(")
        lat = rows[-1]["laterality"] if derived and rows else r[10]
        rows.append(dict(section=section, species=species, level=level, ours_mean=ours["mean"], ours_sd=ours["sd"],
                         ours_min=ours["min"], ours_max=ours["max"], reference=ref, strain=r[8], sex=r[9],
                         laterality=lat, n=r[11], lit_mean=r[12], lit_var=r[13], var_kind=r[14],
                         derived=derived, notes=notes))
    return pd.DataFrame(rows)


def supplement_zip():
    """The supplementary files of the version of record (Europe PMC, PMC7672126): the
    zip's file list and the text of Data_Sheet_1.pdf (the supplement), page by page."""
    import requests
    import zipfile
    from pypdf import PdfReader
    z = zipfile.ZipFile(io.BytesIO(requests.get(SUPPLEMENT_URL, timeout=300).content))
    listing = [(i.filename, i.file_size) for i in z.infolist()]
    b = z.read("Data_Sheet_1.pdf")
    READ[("PMC7672126", "Data_Sheet_1.pdf")] = hashlib.sha256(b).hexdigest()
    pages = [p.extract_text() for p in PdfReader(io.BytesIO(b)).pages]
    return listing, pages


def excel(ds, path, **kw):
    return pd.read_excel(io.BytesIO(read(ds, path)), **kw)


def mat(ds, path):
    return sio.loadmat(io.BytesIO(read(ds, path)), squeeze_me=True)


def tif(ds, path):
    """A binary trace (TIFF) as a boolean array. These masks are the dataset's data."""
    with tifffile.TiffFile(io.BytesIO(read(ds, path))) as t:
        return t.pages[0].asarray() > 0


# ---------------------------------------------------------------- boundaries

def _label_colmajor(bw, conn):
    """bwlabel numbers components in column-major scan order; label the transpose."""
    st = np.ones((3, 3), int) if conn == 8 else ndi.generate_binary_structure(2, 1)
    lab, n = ndi.label(bw.T, structure=st)
    return lab.T, n


def _trace(region, conn):
    """Boundary of one component as (row, col) pixel centres, closed.

    cv2.findContours follows the 8-connected outer border (as bwboundaries does for
    objects). For holes, which bwboundaries traces with 4-connectivity, each diagonal
    step is replaced by two 4-connected steps through the region pixel at the corner.
    """
    cs, _ = cv2.findContours(region.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    c = max(cs, key=len)[:, 0, :]  # (x, y)
    pts = np.c_[c[:, 1], c[:, 0]]
    if conn == 4 and len(pts) > 1:
        out = []
        H, W = region.shape
        for i in range(len(pts)):
            p, q = pts[i], pts[(i + 1) % len(pts)]
            out.append(p)
            d = q - p
            if abs(d[0]) == 1 and abs(d[1]) == 1:
                a, b = (p[0] + d[0], p[1]), (p[0], p[1] + d[1])
                ina = 0 <= a[0] < H and 0 <= a[1] < W and region[a]
                inb = 0 <= b[0] < H and 0 <= b[1] < W and region[b]
                if ina and inb:
                    # both are region pixels: take the one on the border (outside the turn)
                    cross = d[0] * 0
                    out.append(np.array(a) if _border(region, a) else np.array(b))
                elif ina:
                    out.append(np.array(a))
                elif inb:
                    out.append(np.array(b))
        pts = np.array(out)
    return np.vstack([pts, pts[:1]])


def _border(region, p):
    r, c = p
    H, W = region.shape
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        rr, cc = r + dr, c + dc
        if not (0 <= rr < H and 0 <= cc < W) or not region[rr, cc]:
            return True
    return False


def bwboundaries(bw):
    """Outer boundaries of the 8-connected objects, then boundaries of their holes
    (4-connected background components not touching the image edge), each in
    column-major label order, as MATLAB's bwboundaries(BW) returns them."""
    lab, n = _label_colmajor(bw, 8)
    objs = [_trace(lab == k, 8) for k in range(1, n + 1)]
    holes_bw = ndi.binary_fill_holes(bw) & ~bw
    hl, nh = _label_colmajor(holes_bw, 4)
    holes = [_trace(hl == k, 4) for k in range(1, nh + 1)]
    return objs, holes


def polyarea(rc):
    x, y = rc[:, 1].astype(float), -rc[:, 0].astype(float)
    return 0.5 * abs(np.dot(x[:-1], y[1:]) - np.dot(x[1:], y[:-1]))


def centroid(rc):
    x, y = rc[:, 1].astype(float), -rc[:, 0].astype(float)
    a = x[:-1] * y[1:] - x[1:] * y[:-1]
    A = a.sum() / 2
    return np.array([((x[:-1] + x[1:]) * a).sum() / (6 * A), ((y[:-1] + y[1:]) * a).sum() / (6 * A)])


def eff_d(area):
    return 2 * np.sqrt(area / np.pi)


def scale_um_per_px(scalemask, slength):
    """HumanRatSegmentationAnalysis_v2.m: ScalePixels = last - first column with any
    scale-bar pixel, plus one; micperpic = slength / ScalePixels."""
    cols = np.flatnonzero(scalemask.any(axis=0))
    return float(slength) / (cols[-1] - cols[0] + 1)


# ---------------------------------------------------------------- one sample

def analyze(outer, inner, nerve, um):
    """Morphometry of one sample from lists of outer and inner perineurium boundaries and
    a nerve boundary (pixel units), following HumanRatSegmentationAnalysis_v2.m.

    Each inner trace is assigned to the first outer trace containing its centroid
    (PerineuriumComplexMatch_v2.m). Outer traces with one inner trace are non-peanut
    fascicles, with a perineurium thickness; those with several are peanut fascicles.
    Returns a dict of areas (um2) and diameters (um), with fascicles in the code's order
    (non-peanut fascicles in outer-trace order, then the bundles of peanut fascicles)."""
    paths = [Path(np.c_[o[:, 1], -o[:, 0]]) for o in outer]
    groups = [[] for _ in outer]
    unmatched = 0
    for t in inner:
        c = centroid(t)
        for k, p in enumerate(paths):
            if p.contains_point(c):
                groups[k].append(t)
                break
        else:
            unmatched += 1
    a_out = [polyarea(o) * um**2 for o in outer]
    fin, fout, thk, peri_area = [], [], [], 0.0
    peanut_out, peanut_in = 0, 0
    for k, g in enumerate(groups):
        if len(g) == 1:
            ai = polyarea(g[0]) * um**2
            fin.append(ai)
            fout.append(a_out[k])
            thk.append((eff_d(a_out[k]) - eff_d(ai)) / 2)
            peri_area += a_out[k] - ai
    nonpeanut = len(fin)
    for k, g in enumerate(groups):
        if len(g) > 1:
            peanut_out += 1
            peri_area += a_out[k]
            fout.append(a_out[k])
            for t in g:
                ai = polyarea(t) * um**2
                fin.append(ai)
                peri_area -= ai
                peanut_in += 1
    a_nerve = polyarea(nerve) * um**2
    fin = np.array(fin)
    return dict(
        um_per_px=um,
        nerve_area=a_nerve, d_nerve=eff_d(a_nerve),
        fasc_in_area=fin, d_fasc=eff_d(fin),
        fasc_out_area=np.array(fout), d_fasc_out=eff_d(np.array(fout)),
        thk_peri=np.array(thk), d_fasc_nonpeanut=eff_d(fin[:nonpeanut]),
        endo_area=fin.sum(), peri_area=peri_area,
        n_fasc=len(fin), n_nonpeanut=nonpeanut, n_peanut_outer=peanut_out,
        n_peanut_inner=peanut_in, n_outer=len(outer), n_inner=len(inner),
        n_unmatched=unmatched,
    )


def _prefix(ds, sub, sam):
    for p in files(ds):
        if p.startswith(f"files/primary/sub-{sub}/sam-{sam}/") and p.endswith("ScaleLength.mat"):
            return p[: -len("ScaleLength.mat")]
    raise KeyError((ds, sub, sam))


def rat_sample(sub, sam):
    """A rat sample of SPARC:60. Rat traces are one mask of perineurial rings (PeriMask):
    its object boundaries are the outer, its hole boundaries the inner perineurium. With
    one fascicle the outer perineurium is the nerve boundary; with more, NerveMask
    (HumanRatSegmentationAnalysis_v2.m)."""
    pre = _prefix("60", sub, sam)
    peri = tif("60", pre + "PeriMask.tif")
    outer, inner = bwboundaries(peri)
    if len(outer) + len(inner) > 2:
        nb, _ = bwboundaries(tif("60", pre + "NerveMask.tif"))
        nerve = nb[0]
        has_nerve_mask = True
    else:
        nerve = outer[0]
        has_nerve_mask = False
    um = scale_um_per_px(tif("60", pre + "ScaleMask.tif"), mat("60", pre + "ScaleLength.mat")["slength"])
    r = analyze(outer, inner, nerve, um)
    r["nerve_from_mask"] = has_nerve_mask
    r["shape"] = peri.shape
    return r


def human_sample(sub, sam):
    """A human sample of SPARC:65: separate masks of the inner (PeriInnerMask) and outer
    (PeriExtMask) perineurium and of the nerve (NerveMask). In the code the nerve is the
    first boundary of NerveMask; for C47-2, C54-3, C55-3 and C63-1 NerveMask is the
    inner nerve trace the Figure 2 legend says was quantified (the all-tissue trace is
    in a separate NerveMask_AllTissue file)."""
    pre = _prefix("65", sub, sam)
    inner_bw = tif("65", pre + "PeriInnerMask.tif")
    outer_bw = tif("65", pre + "PeriExtMask.tif")
    inner, _ = bwboundaries(inner_bw)
    outer, _ = bwboundaries(outer_bw)
    nerve_bw = tif("65", pre + "NerveMask.tif")
    inverted = bool(nerve_bw[0].all() and nerve_bw[-1].all() and nerve_bw[:, 0].all() and nerve_bw[:, -1].all())
    if inverted:
        # C54-3: the published NerveMask is the complement of a nerve mask (white outside
        # the nerve, filling the frame), so its first boundary is the image frame. The nerve
        # is taken as the largest component of its complement that does not touch the edge.
        lab, n = _label_colmajor(~nerve_bw, 8)
        edge = set(np.unique(np.r_[lab[0], lab[-1], lab[:, 0], lab[:, -1]]))
        sizes = {k: (lab == k).sum() for k in range(1, n + 1) if k not in edge}
        nerve_bw = lab == max(sizes, key=sizes.get)
    nb, _ = bwboundaries(nerve_bw)
    um = scale_um_per_px(tif("65", pre + "ScaleMask.tif"), mat("65", pre + "ScaleLength.mat")["slength"])
    r = analyze(outer, inner, nb[0], um)
    r["n_nerve_objects"] = len(nb)
    r["nerve_mask_inverted"] = inverted
    r["shape"] = inner_bw.shape
    return r


def rat_plot_values(r):
    """The values DataPlotting_v4.m takes for a rat sample in the statistics: with more
    than one fascicle, the nerve diameter is the largest outer perineurium diameter and the
    fascicle diameter is that of the first inner trace in the code's order, which is not
    necessarily the largest fascicle; with one fascicle, the outer perineurium and its
    inner trace."""
    if r["n_fasc"] > 1:
        return dict(d_nerve=r["d_fasc_out"].max(), d_fasc=r["d_fasc"][0])
    return dict(d_nerve=r["d_nerve"], d_fasc=r["d_fasc"][0])


def largest_fascicle(r):
    """The largest fascicle by inner (endoneurial) area: its inner and outer effective
    diameters, thickness, and areas. This is the paper's text ("we only used the largest
    fascicle in each rat sample, using the outer perineurial boundary as the nerve
    boundary", Methods, Imaging and Image Analysis, paragraph 2)."""
    k = int(np.argmax(r["fasc_in_area"]))
    assert k < r["n_nonpeanut"]
    return dict(index=k, d_fasc=r["d_fasc"][k], d_nerve=r["d_fasc_out"][k],
                endo_area=r["fasc_in_area"][k], outer_area=r["fasc_out_area"][k],
                thk=r["thk_peri"][k])


# ---------------------------------------------------------------- statistics

def mixed_anova(df, y, groups="subject", sample=None, factors=("species", "level")):
    """Mixed model ANOVA as in the Methods ("Statistics and Data Analyses"): fixed
    effects species, level and their interaction, random effect of subject, and for
    fascicle diameter a further random effect of sample (nested in subject). Fitted by
    REML (statsmodels MixedLM), the standard choice and JMP's default. Effects are tested
    with Wald tests under sum-to-zero coding (type III): F = chi2 / df, p from chi2. JMP
    reports F tests with Kenward-Roger denominator degrees of freedom; that is not
    available here, and its p-values can be somewhat larger for small samples."""
    import statsmodels.formula.api as smf
    a, b = factors
    form = f"{y} ~ C({a}, Sum) * C({b}, Sum)"
    vc = {"sample": f"0 + C({sample})"} if sample else None
    md = smf.mixedlm(form, df, groups=df[groups], vc_formula=vc, re_formula="1")
    res = None
    for method in ("bfgs", "lbfgs", "powell", "nm"):
        try:
            res = md.fit(reml=True, method=method)
            break
        except np.linalg.LinAlgError:
            continue
    names = list(res.fe_params.index)
    cov = res.cov_params().loc[names, names].values
    b_ = res.fe_params.values
    out = []
    for term, test in ((a, lambda n: n.startswith(f"C({a}") and ":" not in n),
                       (b, lambda n: n.startswith(f"C({b}") and ":" not in n),
                       (f"{a}:{b}", lambda n: ":" in n)):
        idx = [i for i, n in enumerate(names) if test(n)]
        bb = b_[idx]
        V = cov[np.ix_(idx, idx)]
        chi2 = float(bb @ np.linalg.solve(V, bb))
        from scipy import stats
        out.append(dict(term=term, df=len(idx), F=chi2 / len(idx), p=float(stats.chi2.sf(chi2, len(idx)))))
    return res, pd.DataFrame(out)


def sm_fit(res):
    """The fixed effects of a statsmodels MixedLM fit, in the form tukey() takes."""
    names = list(res.fe_params.index)
    return dict(beta=res.fe_params, cov=res.cov_params().loc[names, names].values,
                dfres=int(res.model.nobs - len(names)))


def tukey(fit, df, pairs, which, factors=("species", "level")):
    """Tukey HSD on least squares means of a mixed model fit (dict of beta, cov, dfres).
    `which` is "a" for the main-effect means of the first factor (averaged over the levels
    of the second) or "cell" for the species by level cells. Each pair's t is the
    difference over its SE from the fixed-effect covariance; p from the studentized range
    with k means and dfres degrees of freedom, or, when fit["satt"] is set, the
    Satterthwaite degrees of freedom of each difference. When fit["use_kr"] is set, the SE
    comes from the Kenward-Roger adjusted covariance and the degrees of freedom are the
    Kenward-Roger ones of each difference, on the observed information when it is "obs"
    (the main test here, the one that gives the paper's F and p) and on the expected
    information otherwise (assumption, as the paper gives no settings)."""
    from scipy import stats
    import patsy
    a, b = factors
    beta = fit["beta"]
    names = list(beta.index)
    cov, beta = fit["cov"], beta.values
    la, lb = sorted(df[a].unique()), sorted(df[b].unique())
    grid = pd.DataFrame([(x, z) for x in la for z in lb], columns=[a, b])
    X = patsy.dmatrix(f"C({a}, Sum) * C({b}, Sum)", grid, return_type="dataframe")
    assert list(X.columns) == names, (list(X.columns), names)
    rows = {(x, z): X.values[i] for i, (x, z) in enumerate(zip(grid[a], grid[b]))}
    L = {x: np.mean([rows[(x, z)] for z in lb], axis=0) for x in la} if which == "a" else rows
    k = len(L)
    out = []
    for p, q in pairs:
        c = L[p] - L[q]
        est = float(c @ beta)
        if fit.get("use_kr"):
            krs = fit["kr_obs"] if fit["use_kr"] == "obs" else fit["kr"]
            se = float(np.sqrt(c @ krs["PhiA"] @ c))
            dfp = kr_test(krs, c)["ddf"]
        else:
            se = float(np.sqrt(c @ cov @ c))
            dfp = satterthwaite_df(fit, c) if fit.get("satt") else fit["dfres"]
        t = est / se
        pv = float(stats.studentized_range.sf(abs(t) * np.sqrt(2), k, dfp))
        out.append(dict(pair=f"{p} - {q}", diff=est, se=se, t=t, df=dfp, p_tukey=pv))
    means = {key: float(v @ beta) for key, v in L.items()}
    return pd.DataFrame(out), means


def pig_if_counts(sub, sam):
    """Trace counts of a pig anti-fibronectin IF sample of SPARC:89 (PeriInMask,
    PeriExtMask), with inner traces matched to outer traces as for the other species.
    The IF folders hold no ScaleLength file, so only counts are taken here; the IF
    diameters and thicknesses come from the paper's PigIFMorphology.mat."""
    pre = f"files/primary/sub-{sub}/sam-{sam}/sub-{sub}_sam-{sam}_P{sub}-{sam}"
    inner, _ = bwboundaries(tif("89", pre + "PeriInMask.tif"))
    outer, _ = bwboundaries(tif("89", pre + "PeriExtMask.tif"))
    nb, _ = bwboundaries(tif("89", pre + "NerveMask.tif"))
    r = analyze(outer, inner, nb[0], 1.0)
    out = {k: r[k] for k in ("n_fasc", "n_nonpeanut", "n_peanut_outer", "n_peanut_inner",
                             "n_outer", "n_inner", "n_unmatched")}
    # As SPARC:89's SegmentationAnalysis_v2.m counts: bwboundaries without 'noholes', so
    # hole boundaries count as traces too; each outer trace collects every inner trace whose
    # centroid it contains; outer traces with exactly one are non-peanut, the others (with
    # none or several) are counted as peanut fascicles (Nouterperi_peanut).
    io_, ih = bwboundaries(tif("89", pre + "PeriInMask.tif"))
    oo, oh = bwboundaries(tif("89", pre + "PeriExtMask.tif"))
    ins, outs = io_ + ih, oo + oh
    cents = [centroid(t) for t in ins]
    counts = [sum(Path(np.c_[o[:, 1], -o[:, 0]]).contains_point(c) for c in cents) for o in outs]
    out.update(code_inner=len(ins), code_inner_holes=len(ih), code_outer=len(outs), code_outer_holes=len(oh),
               code_nonpeanut=sum(c == 1 for c in counts), code_peanut_outer=sum(c != 1 for c in counts),
               code_outer_empty=sum(c == 0 for c in counts))
    out["code_bundles"] = out["code_inner"] - out["code_nonpeanut"]
    return out


def fit_poly1(x, y, intercept=True):
    """MATLAB fit(x, y, 'poly1') by linear least squares, with its goodness of fit:
    rsquare = 1 - SSE/SST, SST about the mean of y (also for the zero-intercept fit),
    and 95% confidence bounds of the coefficients (t quantile, n - p dof), as confint
    returns them."""
    from scipy import stats
    x, y = np.asarray(x, float), np.asarray(y, float)
    X = np.c_[x, np.ones_like(x)] if intercept else x[:, None]
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    sse = float(resid @ resid)
    sst = float(((y - y.mean()) ** 2).sum())
    dof = len(y) - X.shape[1]
    s2 = sse / dof
    cov = s2 * np.linalg.inv(X.T @ X)
    t = stats.t.ppf(0.975, dof)
    ci = np.c_[beta - t * np.sqrt(np.diag(cov)), beta + t * np.sqrt(np.diag(cov))]
    return dict(p1=beta[0], p2=beta[1] if intercept else 0.0, r2=1 - sse / sst,
                r2_uncentered=1 - sse / float(y @ y), ci=ci, n=len(y), sse=sse, dof=dof)


def reml_unbounded(df, y, groups, factors=("species", "level"), nested=None, x0=None):
    """REML fit of the same mixed model with unbounded variance components: the subject
    (and sample) variance components may be negative, as long as each subject's covariance
    matrix stays positive definite. JMP's REML uses unbounded variance components by default
    (Fit Model, "Unbounded Variance Components"), which statsmodels does not offer; this
    is the replacement. Fixed effects by generalised least squares; each effect is tested
    with a Wald F (type III, sum-to-zero coding). Returns the fixed-effect table and the
    variance components. Each effect is tested with the Kenward-Roger F on the observed
    information (F_kr_obs, ddf_kr_obs, p_kr_obs), the main result, which gives the paper's F
    and p; as variants, the Kenward-Roger F on the expected information (F_kr, ddf_kr,
    p_kr), the Wald F with
    Satterthwaite degrees of freedom from the observed REML information (as lmerTest),
    with the residual degrees of freedom (n minus the number of fixed parameters), and with
    the number of subjects minus the number of fixed parameters, an ad hoc conservative
    bound."""
    import patsy
    from scipy import optimize, stats
    a, b = factors
    X = patsy.dmatrix(f"C({a}, Sum) * C({b}, Sum)", df, return_type="dataframe")
    names = list(X.columns)
    Xv, yv = X.values, df[y].values.astype(float)
    g = df[groups].astype(str).to_numpy()
    blocks = [np.flatnonzero(g == k) for k in pd.unique(g)]
    nest = df[nested].astype(str).to_numpy() if nested else None

    def parts(theta):
        s2, tau = np.exp(theta[0]), theta[1:]
        out = []
        for idx in blocks:
            n = len(idx)
            V = s2 * np.eye(n) + tau[0] * np.ones((n, n))
            if nested:
                same = (nest[idx][:, None] == nest[idx][None, :]).astype(float)
                V = V + tau[1] * same
            out.append(V)
        return out

    def negll(theta):
        Vs = parts(theta)
        logdet, XtVX, XtVy, yVy = 0.0, 0, 0, 0.0
        for idx, V in zip(blocks, Vs):
            try:
                L = np.linalg.cholesky(V)
            except np.linalg.LinAlgError:
                return 1e12
            logdet += 2 * np.log(np.diag(L)).sum()
            Xi = np.linalg.solve(L, Xv[idx])
            yi = np.linalg.solve(L, yv[idx])
            XtVX = XtVX + Xi.T @ Xi
            XtVy = XtVy + Xi.T @ yi
            yVy += yi @ yi
        beta = np.linalg.solve(XtVX, XtVy)
        rss = yVy - XtVy @ beta
        sign, ld2 = np.linalg.slogdet(XtVX)
        return 0.5 * (logdet + ld2 + rss)

    if x0 is None:
        x0 = np.r_[np.log(np.var(yv) / 2), np.var(yv) / 4] if not nested else np.r_[np.log(np.var(yv) / 2), np.var(yv) / 4, np.var(yv) / 8]
    opt = optimize.minimize(negll, x0, method="Nelder-Mead", options=dict(xatol=1e-10, fatol=1e-12, maxiter=20000, maxfev=40000))
    Vs = parts(opt.x)
    XtVX, XtVy = 0, 0
    for idx, V in zip(blocks, Vs):
        Vi = np.linalg.inv(V)
        XtVX = XtVX + Xv[idx].T @ Vi @ Xv[idx]
        XtVy = XtVy + Xv[idx].T @ Vi @ yv[idx]
    cov = np.linalg.inv(XtVX)
    beta = cov @ XtVy
    nobs, p = len(yv), len(names)
    out = []
    for term, test in ((a, lambda n: n.startswith(f"C({a}") and ":" not in n),
                       (b, lambda n: n.startswith(f"C({b}") and ":" not in n),
                       (f"{a}:{b}", lambda n: ":" in n)):
        idx = [i for i, n in enumerate(names) if test(n)]
        bb = beta[idx]
        F = float(bb @ np.linalg.solve(cov[np.ix_(idx, idx)], bb)) / len(idx)
        out.append(dict(term=term, df=len(idx), F=F,
                        p_resid_df=float(stats.f.sf(F, len(idx), nobs - p)),
                        p_subject_df=float(stats.f.sf(F, len(idx), len(blocks) - p))))
    vc = dict(residual=float(np.exp(opt.x[0])), subject=float(opt.x[1]))
    if nested:
        vc["sample"] = float(opt.x[2])
    def cov_at(theta):
        M = 0
        for idx, V in zip(blocks, parts(theta)):
            M = M + Xv[idx].T @ np.linalg.solve(V, Xv[idx])
        return np.linalg.inv(M)

    # Hessian of -REML log-likelihood in theta, by central differences, for Satterthwaite
    th = opt.x
    k = len(th)
    h = np.maximum(np.abs(th) * 1e-3, 1e-5)
    H = np.zeros((k, k))
    for i in range(k):
        for j in range(k):
            ei, ej = np.eye(k)[i] * h[i], np.eye(k)[j] * h[j]
            H[i, j] = (negll(th + ei + ej) - negll(th + ei - ej) - negll(th - ei + ej) + negll(th - ei - ej)) / (4 * h[i] * h[j])
    fit = dict(beta=pd.Series(beta, names), cov=cov, converged=bool(opt.success),
               dfres=nobs - p, dfsub=len(blocks) - p, theta=th, cov_at=cov_at, H=H, h=h)
    G = [np.eye(nobs), (g[:, None] == g[None, :]).astype(float)]
    if nested:
        G.append((nest[:, None] == nest[None, :]).astype(float))
    fit["kr"] = kr_setup(Xv, yv, G, np.r_[np.exp(th[0]), th[1:]])
    # the same with the observed information (the Hessian H, mapped from theta to the linear
    # parameters), the information the Satterthwaite degrees of freedom use
    J = np.diag(np.r_[np.exp(th[0]), np.ones(k - 1)])
    fit["kr_obs"] = kr_setup(Xv, yv, G, np.r_[np.exp(th[0]), th[1:]], W=J @ np.linalg.inv(H) @ J)
    for row in out:
        idx = [i for i, n in enumerate(names) if (row["term"] == a and n.startswith(f"C({a}") and ":" not in n)
               or (row["term"] == b and n.startswith(f"C({b}") and ":" not in n) or (":" in row["term"] and ":" in n)]
        Lm = np.eye(p)[idx]
        kr = kr_test(fit["kr"], Lm)
        row["F_kr"], row["ddf_kr"], row["p_kr"] = kr["F"], kr["ddf"], kr["p"]
        kro = kr_test(fit["kr_obs"], Lm)
        row["F_kr_obs"], row["ddf_kr_obs"], row["p_kr_obs"] = kro["F"], kro["ddf"], kro["p"]
        row["df_satt"] = satterthwaite_multi_df(fit, Lm)
        row["p_satt"] = float(stats.f.sf(row["F"], len(idx), row["df_satt"]))
    return pd.DataFrame(out), vc, fit


def kr_setup(X, y, G, lin, W=None):
    """The quantities of Kenward and Roger (1997) for a REML fit whose covariance is
    linear in its parameters, V = sum_i lin_i G_i (here residual, subject and sample):
    Phi = (X'V^-1X)^-1, P_i = -X'V^-1 G_i V^-1 X, Q_ij = X'V^-1 G_i V^-1 G_j V^-1 X, and W
    the inverse of the expected REML information 0.5 tr(P G_i P G_j) (P the REML projection).
    The bias-adjusted covariance is Phi_A = Phi + 2 Phi (sum_ij W_ij (Q_ij - P_i Phi P_j)) Phi
    (R_ij = 0, as V is linear in lin). JMP's REML reports Kenward-Roger tests (JMP Fit Model
    documentation, "Restricted Maximum Likelihood (REML) Method"), the reason for using it;
    it is computed here with dense matrices. W may be given in place of the expected
    information's inverse, for the variant on the observed information."""
    Vi = np.linalg.inv(sum(l * Gi for l, Gi in zip(lin, G)))
    Phi = np.linalg.inv(X.T @ Vi @ X)
    beta = Phi @ X.T @ Vi @ y
    Pr = Vi - Vi @ X @ Phi @ X.T @ Vi
    k = len(G)
    PG = [Pr @ Gi for Gi in G]
    if W is None:
        W = np.linalg.inv(np.array([[0.5 * np.sum(PG[i] * PG[j].T) for j in range(k)] for i in range(k)]))
    ViG = [Vi @ Gi for Gi in G]
    Pm = [-X.T @ ViG[i] @ Vi @ X for i in range(k)]
    Lam = sum(W[i, j] * (X.T @ ViG[i] @ ViG[j] @ Vi @ X - Pm[i] @ Phi @ Pm[j]) for i in range(k) for j in range(k))
    return dict(beta=beta, Phi=Phi, PhiA=Phi + 2 * Phi @ Lam @ Phi, W=W, Pm=Pm, lin=lin)


def kr_test(s, L):
    """Kenward-Roger F test of L beta = 0 (Kenward and Roger, 1997, section 4, as pbkrtest
    computes it): the Wald F on the adjusted covariance, scaled by lambda, with m
    denominator degrees of freedom. Checked in the notebook on a balanced split-plot
    design, where it gives the exact F tests."""
    from scipy import stats
    L = np.atleast_2d(L)
    q = L.shape[0]
    Phi, W, Pm = s["Phi"], s["W"], s["Pm"]
    k = len(Pm)
    Th = L.T @ np.linalg.solve(L @ Phi @ L.T, L)
    M = [Th @ Phi @ Pm[i] @ Phi for i in range(k)]
    A1 = sum(W[i, j] * np.trace(M[i]) * np.trace(M[j]) for i in range(k) for j in range(k))
    A2 = sum(W[i, j] * np.trace(M[i] @ M[j]) for i in range(k) for j in range(k))
    B = (A1 + 6 * A2) / (2 * q)
    gg = ((q + 1) * A1 - (q + 4) * A2) / ((q + 2) * A2)
    den = 3 * q + 2 * (1 - gg)
    c1, c2, c3 = gg / den, (q - gg) / den, (q + 2 - gg) / den
    E = 1 / (1 - A2 / q)
    V = 2 / q * (1 + c1 * B) / ((1 - c2 * B) ** 2 * (1 - c3 * B))
    rho = V / (2 * E ** 2)
    m = 4 + (q + 2) / (q * rho - 1)
    lam = m / (E * (m - 2))
    b = s["beta"]
    F = lam * float(b @ L.T @ np.linalg.solve(L @ s["PhiA"] @ L.T, L @ b)) / q
    return dict(F=float(F), ddf=float(m), p=float(stats.f.sf(F, q, m)), lam=float(lam))


def satterthwaite_multi_df(fit, L):
    """Denominator degrees of freedom of a q-df Satterthwaite F test, as lmerTest computes
    it (Fai and Cornelius, 1996): the 1-df Satterthwaite df nu_m of the q orthogonal
    contrasts from the eigen-decomposition of L C L', E = sum nu_m / (nu_m - 2) over
    nu_m > 2, df = 2E / (E - q) when E > q."""
    L = np.atleast_2d(L)
    q = L.shape[0]
    if q == 1:
        return satterthwaite_df(fit, L[0])
    d, U = np.linalg.eigh(L @ fit["cov"] @ L.T)
    nus = [satterthwaite_df(fit, (U[:, m] @ L) / np.sqrt(d[m])) for m in range(q)]
    E = sum(nu / (nu - 2) for nu in nus if nu > 2)
    return float(2 * E / (E - q)) if E > q else float("nan")


def reml_dense(X, y, G, x0):
    """REML fit of y = X beta + e with covariance sum_i lin_i G_i, lin_0 (residual) kept
    positive through its log and the others unbounded as long as the covariance stays
    positive definite (as reml_unbounded, for small data with dense matrices). Returns
    kr_setup's quantities at the optimum, for kr_test."""
    from scipy import optimize

    def negll(t):
        lin = np.r_[np.exp(t[0]), t[1:]]
        V = sum(l * Gi for l, Gi in zip(lin, G))
        try:
            L = np.linalg.cholesky(V)
        except np.linalg.LinAlgError:
            return 1e12
        Xi, yi = np.linalg.solve(L, X), np.linalg.solve(L, y)
        A = Xi.T @ Xi
        b = np.linalg.solve(A, Xi.T @ yi)
        r = yi - Xi @ b
        return 0.5 * (2 * np.log(np.diag(L)).sum() + np.linalg.slogdet(A)[1] + r @ r)

    opt = optimize.minimize(negll, x0, method="Nelder-Mead", options=dict(xatol=1e-10, fatol=1e-12, maxiter=20000))
    s = kr_setup(X, y, G, np.r_[np.exp(opt.x[0]), opt.x[1:]])
    s["converged"] = bool(opt.success)
    return s


def satterthwaite_df(fit, c):
    """Satterthwaite degrees of freedom of the contrast c'beta of an unbounded REML fit:
    2 (c'Cc)^2 / (g' H^-1 g), g the gradient of c'C(theta)c in the variance parameters
    and H the Hessian of the -REML log-likelihood (both by central differences). JMP uses
    Kenward-Roger, which has these degrees of freedom when its bias correction is small."""
    th, h = fit["theta"], fit["h"]
    f0 = float(c @ fit["cov_at"](th) @ c)
    g = np.array([(c @ fit["cov_at"](th + np.eye(len(th))[i] * h[i]) @ c - c @ fit["cov_at"](th - np.eye(len(th))[i] * h[i]) @ c) / (2 * h[i])
                  for i in range(len(th))])
    return float(2 * f0 ** 2 / (g @ np.linalg.solve(fit["H"], g)))
