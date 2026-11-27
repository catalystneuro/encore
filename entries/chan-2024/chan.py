"""Loading and measures for Chan et al. (2024), Science 383, 607, on Dryad doi:10.5061/dryad.vt4b8gtzk.

The Dryad version read is 289757 (the only published version, 2024-04-22). Dryad downloads need a
token, so the files are staged before the run in /tmp/dryad/vt4b8gtzk/289757/ and read there, in
place (docs/archives.md, "Dryad"). Their SHA-256 digests are checked against Dryad's public file
list by `check_dryad_files`.

Data that the Dryad deposit lacks (the Fig. 2D raw Vocus traces, the Fig. 3B wind tunnel sheet, the
fruit-set counts in the Fig. 1E R script, and the GEOS-Chem output) are read from the paper's own
code release on Zenodo, record 8411927 (doi:10.5281/zenodo.8411927, the paper's ref. 41), streamed
from the record's zip. The recognition distances also need the model's bottom-level wind and the
Table S13 city coordinates, which neither deposit holds; they are read from GEOS-Chem's processed
MERRA-2 files and from the UN World Urbanization Prospects 2018 (`merra2_bottom_wind`,
`table_s13_cities`).

Where each parameter comes from is said beside it: the claim's criterion (claims/chan-2024.yaml),
a passage of the paper ("SM" is the Supplementary Materials, "MM" its Materials and Methods), the
paper's code (the Dryad notebook Fig_S4_Table_S9_VOCUS_analysis_and_plotting.ipynb, or the Zenodo
R script), an assumption, or a standard choice that cannot change a result.
"""
import hashlib
import io
import itertools
import zipfile
from functools import lru_cache
from pathlib import Path

import fsspec
import numpy as np
import pandas as pd
import requests
from scipy import stats

DRYAD_ID = "vt4b8gtzk"
DRYAD_VERSION = "289757"
DRYAD_DOI = "10.5061/dryad.vt4b8gtzk"
# Where tools/stage_files.py puts the pinned version's files before a run (STAGED in tools/archives,
# root / "dryad" / id / version); docs/archives.md, "Dryad", has notebooks read them there.
STAGED = Path("/tmp")
DRYAD_DIR = STAGED / "dryad" / DRYAD_ID / DRYAD_VERSION
DRYAD_FILES_API = f"https://datadryad.org/api/v2/versions/{DRYAD_VERSION}/files"

ZENODO_RECORD = "8411927"
ZENODO_DOI = "10.5281/zenodo.8411927"
ZENODO_KEY = "riffelllab/Chan-et-al-v1.zip"
ZENODO_URL = f"https://zenodo.org/api/records/{ZENODO_RECORD}/files/{ZENODO_KEY}/content"
ZIP_ROOT = "riffelllab-Chan-et-al-ffc1559/"


# ---------------------------------------------------------------- archives

def dryad_file_list():
    """Dryad's public file list of the pinned version: name -> (size, sha256)."""
    out, url = {}, DRYAD_FILES_API
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        j = r.json()
        for f in j["_embedded"]["stash:files"]:
            out[f["path"]] = (f["size"], f["digest"])
        nxt = j["_links"].get("next")
        url = "https://datadryad.org" + nxt["href"] if nxt else None
    return out


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(2**20), b""):
            h.update(block)
    return h.hexdigest()


def check_dryad_files():
    """Table of every file in the Dryad list, its digest, and whether the staged copy matches."""
    rows = []
    for name, (size, digest) in sorted(dryad_file_list().items()):
        p = DRYAD_DIR / name
        local = sha256(p) if p.exists() else None
        rows.append({"file": name, "bytes": size, "sha256": digest, "matches": local == digest})
    return pd.DataFrame(rows)


def dryad(name):
    return DRYAD_DIR / name


@lru_cache(maxsize=1)
def zenodo_zip():
    """The Zenodo record's zip, opened in place over HTTP (read by ranges, not downloaded)."""
    return zipfile.ZipFile(fsspec.open(ZENODO_URL, block_size=2**20).open())


def zenodo_md5():
    r = requests.get(f"https://zenodo.org/api/records/{ZENODO_RECORD}", timeout=60)
    r.raise_for_status()
    return {f["key"]: f["checksum"] for f in r.json()["files"]}


def zread(member):
    return zenodo_zip().read(ZIP_ROOT + member)


def zenodo_listing():
    return [(i.filename[len(ZIP_ROOT):], i.file_size) for i in zenodo_zip().infolist()
            if not i.is_dir()]


# ---------------------------------------------------------------- proportions

def r_prop_test(x1, n1, x2, n2, correct=True):
    """Two-sample test of proportions as R's prop.test: Pearson chi-square on the 2x2 table, with
    Yates' correction min(0.5, |p1 - p2| / (1/n1 + 1/n2)) when `correct` (R's default).
    The paper's Fig. 1E script calls pairwise.prop.test with these defaults (Zenodo R script)."""
    x = np.array([x1, x2], float)
    n = np.array([n1, n2], float)
    p = x.sum() / n.sum()
    obs = np.array([x, n - x])
    exp = np.array([n * p, n * (1 - p)])
    yates = 0.0
    if correct:
        yates = min(0.5, abs(x1 / n1 - x2 / n2) / (1 / n1 + 1 / n2))
    chi2 = (((np.abs(obs - exp) - yates) ** 2) / exp).sum()
    return chi2, stats.chi2.sf(chi2, 1)


def z_prop_test(x1, n1, x2, n2):
    """Two-proportion z-test with pooled variance and no continuity correction (Zar's test of
    population proportions, the reading (i) the criteria of the Fig. 3B claims name)."""
    p1, p2 = x1 / n1, x2 / n2
    p = (x1 + x2) / (n1 + n2)
    se = np.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
    if se == 0:
        return 0.0, 1.0
    z = (p1 - p2) / se
    return z, 2 * stats.norm.sf(abs(z))


def holm(p):
    """Holm adjustment, as R's p.adjust(method = "holm")."""
    p = np.asarray(p, float)
    order = np.argsort(p)
    m = len(p)
    adj = np.empty(m)
    running = 0.0
    for rank, i in enumerate(order):
        running = max(running, (m - rank) * p[i])
        adj[i] = min(1.0, running)
    return adj


def pairwise_prop_test(names, x, n, correct=True):
    """R's pairwise.prop.test: every pair by prop.test, Holm-adjusted over all pairs."""
    pairs = list(itertools.combinations(range(len(names)), 2))
    raw = [r_prop_test(x[i], n[i], x[j], n[j], correct)[1] for i, j in pairs]
    adj = holm(raw)
    return pd.DataFrame({"a": [names[i] for i, _ in pairs], "b": [names[j] for _, j in pairs],
                         "p_raw": raw, "p_holm": adj})


def fruit_set_counts():
    """Fruit-set counts and sample sizes, parsed from the prop.test call of the paper's Fig. 1E R
    script in the Zenodo release (the counts behind Table S3). Order as in the script's comments:
    total exclusion, crossed, nocturnal exclusion, unbagged, diurnal exclusion."""
    text = zread("Figure 1/Fig 1D R script for analyzing Opall fruit set clean.R").decode()
    line = [l for l in text.splitlines() if l.startswith("pairwise.prop.test(")][0]
    inner = line[line.index("(") + 1:line.rindex(")")]
    xs, ns = [list(map(int, part.split(")")[0].split(","))) for part in inner.split("c(")[1:]]
    names = ["total exclusion", "crossed", "nocturnal exclusion", "unbagged", "diurnal exclusion"]
    return pd.DataFrame({"treatment": names, "fruit": xs, "n": ns}), line


# ---------------------------------------------------------------- flowtube (Vocus PTR-ToF)

VOCUS_FILES = {
    "aldoxime": "Figure 2/aldoxime_20210423_VOCUS_PTR_OPall2n_Blend9_NO3_ox_Data_n_2021.05.10_16h50m03s_igor.txt",
    "b-pinene": "Figure 2/b-pinene_20210512_VOCUS_OPall2n_VOCs_NO3_ox_Data_n_2021.05.12_17h08m26s_igor.txt",
    "ocimene": "Figure 2/ocimene_20210512_VOCUS_OPall2n_VOCs_NO3_ox_Data_n_2021.05.12_19h36m49s_igor.txt",
    "benzaldehyde": "Figure 2/benzaldehyde_20210512_VOCUS_OPall2n_VOCs_NO3_ox_Data_n_2021.05.12_22h58m37s_igor.txt",
    "nonanal": "Figure 2/nonanal_20210517_VOCUS_OPall2n_VOCs_NO3_ox_Data_n_2021.05.18_03h43m35s_igor.txt",
}

# Processing of each trace, from the Table S9 cells (29 to 33) of the Dryad notebook
# Fig_S4_Table_S9_VOCUS_analysis_and_plotting.ipynb: the section of the file used, whether it is
# linearly detrended over the section, the baseline window it is divided by, and the windows the
# notebook compares (clean air, O3, NO3; indices into the section). For the aldoxime the notebook
# takes the clean mean over 0:300 and tests 100:200; both are kept.
VOCUS_CODE = {
    "b-pinene": dict(section=(350, 1750), detrend=False, norm=(0, 200),
                     clean=(0, 200), o3=(500, 800), no3=(1100, 1300)),
    "ocimene": dict(section=(50, 1450), detrend=False, norm=(150, 240),
                    clean=(100, 200), o3=(400, 800), no3=(1200, 1400)),
    "aldoxime": dict(section=(1155, 3654), detrend=True, norm=(1100, 1200),
                     clean=(0, 300), clean_test=(100, 200), o3=(800, 1400), no3=(2000, 2400)),
    "nonanal": dict(section=(0, 1240), detrend=True, norm=(0, 156),
                    clean=(0, 156), o3=(156, 634), no3=(634, 1240)),
    "benzaldehyde": dict(section=(930, 2600), detrend=False, norm=(0, 240),
                         clean=(0, 240), o3=(370, 740), no3=(740, 1670)),
}


def vocus_raw(compound):
    """Time (s, truncated to integers as the notebook does) and signal, first row skipped as
    np.loadtxt(skiprows=1) does in the notebook."""
    a = np.loadtxt(io.BytesIO(zread(VOCUS_FILES[compound])), skiprows=1)
    return a[:, 0].astype(int).astype(float), a[:, 1]


def vocus_trace(compound):
    """The normalized trace as the Dryad notebook builds it: the section, a linear detrend over
    the whole section (the notebook's `detrend`, slope only) where it uses one, and division by
    the mean of the baseline window."""
    c = VOCUS_CODE[compound]
    t, y = vocus_raw(compound)
    s, e = c["section"]
    t, y = t[s:e].copy(), y[s:e].copy()
    if c["detrend"]:
        m, _ = np.polyfit(t, y, 1)
        y = y - m * (t - s)
    a, b = c["norm"]
    return t, y / np.mean(y[a:b])


def table_s9_test(a, b):
    """The Table S9 test as the Dryad notebook's `ttest`: Student t when both samples pass
    Shapiro-Wilk and Levene (p > 0.05), Welch t when only Levene fails, else Mann-Whitney U."""
    s1, s2 = stats.shapiro(a).pvalue, stats.shapiro(b).pvalue
    lev = stats.levene(a, b).pvalue
    if s1 > 0.05 and s2 > 0.05 and lev > 0.05:
        return stats.ttest_ind(a, b).pvalue, "t-test"
    if s1 > 0.05 and s2 > 0.05:
        return stats.ttest_ind(a, b, equal_var=False).pvalue, "Welch t-test"
    return stats.mannwhitneyu(a, b, alternative="two-sided").pvalue, "Mann-Whitney U-test"


def step_onset(y, level_before, level_after, lo, hi, smooth=15):
    """Index in [lo, hi) where the trace, smoothed by a centred running mean of `smooth` points,
    first crosses half-way between the stage levels before and after the step (a standard way to
    place a step). The search lies between the code's windows of the two stages."""
    ys = pd.Series(y).rolling(smooth, center=True, min_periods=1).mean().to_numpy()
    mid = (level_before + level_after) / 2
    seg = ys[lo:hi]
    crossed = seg < mid if level_after < level_before else seg > mid
    idx = np.nonzero(crossed)[0]
    return lo + int(idx[0]) if len(idx) else None


def stage_windows(compound, y):
    """Windows for the criterion. The code's own windows (clean-air mean over `clean`, test on
    `clean_test` where the notebook uses a different window) are the paper's method, as the
    criterion says. The variants: (b) whole stage, clean air from the section start to the O3
    onset, O3 from its onset to the NO3 onset, NO3 from its onset to the section end; (a) the last
    half of each. Onsets are found from the step in the monoterpene traces (a standard choice);
    for compounds that show no step the stage extents are the code's windows."""
    c = VOCUS_CODE[compound]
    code = {"clean": c["clean"], "o3": c["o3"], "no3": c["no3"],
            "clean_test": c.get("clean_test", c["clean"])}
    if compound in ("b-pinene", "ocimene"):
        lv = {k: np.mean(y[slice(*c[k])]) for k in ("clean", "o3", "no3")}
        o3_on = step_onset(y, lv["clean"], lv["o3"], c["clean"][1], c["o3"][0])
        no3_on = step_onset(y, lv["o3"], lv["no3"], c["o3"][1], c["no3"][0])
        whole = {"clean": (0, o3_on), "o3": (o3_on, no3_on), "no3": (no3_on, len(y))}
    else:
        whole = {"clean": c["clean"], "o3": c["o3"], "no3": c["no3"]}
    half = {k: ((a + b) // 2, b) for k, (a, b) in whole.items()}
    for w in (whole, half):
        w["clean_test"] = w["clean"]
    return {"a (last half of stage)": half, "b (whole stage)": whole, "code windows": code}


def oxidation_table(compound):
    t, y = vocus_trace(compound)
    rows = []
    for reading, w in stage_windows(compound, y).items():
        clean, o3, no3, clean_t = (y[slice(*w[k])] for k in ("clean", "o3", "no3", "clean_test"))
        p_o3, t_o3 = table_s9_test(clean_t, o3)
        p_no3, t_no3 = table_s9_test(clean_t, no3)
        p_no3o3, t_no3o3 = table_s9_test(o3, no3)
        rows.append({
            "compound": compound, "reading": reading,
            "clean": w["clean"], "o3": w["o3"], "no3": w["no3"],
            "O3 vs clean %": 100 * (o3.mean() / clean.mean() - 1), "p O3": p_o3, "test O3": t_o3,
            "NO3 vs clean %": 100 * (no3.mean() / clean.mean() - 1), "p NO3": p_no3,
            "test NO3": t_no3,
            "NO3 vs O3 %": 100 * (no3.mean() / o3.mean() - 1), "p NO3 vs O3": p_no3o3,
            "test NO3 vs O3": t_no3o3,
        })
    return pd.DataFrame(rows)


def fig2d_tof():
    """The Dryad file Fig2D_ToFdata.txt (normalized Fig. 2D traces)."""
    return pd.read_csv(dryad("Fig2D_ToFdata.txt"), sep="\t")


def blend_cims(name):
    """A benzene-cation CIMS trace of the blend (Dryad Fig_S4_<name>_NO3_oxidation_...)."""
    a = np.loadtxt(dryad(f"Fig_S4_{name}_NO3_oxidation_benzene_cation_CIMS.txt"))
    return a[:, 0], a[:, 1]


# ---------------------------------------------------------------- EAG and behaviour

def eag():
    """The EAG file in long form. Its two column pairs are Manduca and Hyles; row r of each pair is
    a value at a concentration (floral equivalents)."""
    raw = pd.read_csv(dryad("Fig_S5_Manduca_Hyles_EAG_dose_response_mean_of_largest.csv"))
    raw.columns = ["conc_manduca", "manduca", "conc_hyles", "hyles"]
    long = pd.concat([
        pd.DataFrame({"species": "Manduca", "row": raw.index + 2, "conc": raw.conc_manduca,
                      "mV": raw.manduca}),
        pd.DataFrame({"species": "Hyles", "row": raw.index + 2, "conc": raw.conc_hyles,
                      "mV": raw.hyles})]).dropna()
    return raw, long


def wind_tunnel_fig3b():
    return pd.read_excel(io.BytesIO(zread("Figure 3/Fig 3B Hyles and Manduca wind tunnel behavior data.xlsx")),
                         sheet_name=None)


def wind_tunnel_s7c():
    return pd.read_excel(dryad("Fig_S5C_Manduca_dose_response_wind_tunnel_behavior_data.xlsx"),
                         sheet_name=None)


def proportion_tests(x1, n1, x2, n2):
    """Both readings the Fig. 3B criteria name: (i) z-test, pooled, no correction; (ii) R
    prop.test with Yates' correction."""
    z, pz = z_prop_test(x1, n1, x2, n2)
    _, py = r_prop_test(x1, n1, x2, n2, correct=True)
    return {"z": z, "p (i) z-test": pz, "p (ii) prop.test Yates": py}


# ---------------------------------------------------------------- field visits (Table S10)

def table_s10():
    sheets = pd.read_excel(dryad("Table_S10.xlsx"), sheet_name=None)
    (name, df), = sheets.items()
    return name, df.set_index(df.columns[0])


# ---------------------------------------------------------------- field conditions (Table S1)

def load_o3():
    """Ozone monitor logs: column 1 is O3 (ppb), then date (dd/mm/yy) and time (README)."""
    out = []
    for name in sorted(p.name for p in DRYAD_DIR.glob("FigS3_O3_LOG*.txt")):
        d = pd.read_csv(dryad(name), skiprows=[1])
        d["time"] = pd.to_datetime(d["date"] + " " + d["timestamp"], format="%d/%m/%y %H:%M:%S")
        d["file"] = name
        out.append(d[["file", "time", "O3"]])
    return pd.concat(out, ignore_index=True)


def load_caps():
    """CAPS NO2 files: comma-separated after '%' header lines; the Timestamp column is the clock."""
    out = []
    for name in sorted(p.name for p in DRYAD_DIR.glob("TableS1_FigS3_CAPS_*.dat")):
        d = pd.read_csv(dryad(name), comment="%", skipinitialspace=True, na_values=["NaN"])
        d.columns = [c.strip() for c in d.columns]
        d["time"] = pd.to_datetime(d["Timestamp"].str.strip(), format="%Y/%m/%d %H:%M:%S")
        d["file"] = name
        for col in ("NO2", "RawLoss"):
            d[col] = pd.to_numeric(d[col].astype(str).str.strip(), errors="coerce")
        out.append(d[["file", "time", "IgorTime", "NO2", "RawLoss", "Status"]])
    return pd.concat(out, ignore_index=True)


def load_ibutton():
    """iButton logs: Excel serial date-time (local time, 'Timezone -7'), temperature, RH."""
    out = []
    for name in sorted(p.name for p in DRYAD_DIR.glob("FigS3_2018*_OPALL_*.csv")):
        d = pd.read_csv(dryad(name), header=None, names=["serial", "temp_C", "RH"],
                        encoding="latin-1", on_bad_lines="skip")
        d = d.apply(pd.to_numeric, errors="coerce").dropna()
        d["time"] = pd.Timestamp("1899-12-30") + pd.to_timedelta(d.serial, unit="D")
        d["file"] = name
        out.append(d)
    return pd.concat(out, ignore_index=True)


def anemometer_header():
    with open(dryad("Table_S1_anemometer_data.txt"), "rb") as f:
        return f.readline().decode("latin-1").strip()


def load_anemometer():
    """Sonic anemometer: u, v, w (cm/s) and temperature (K) at 32 Hz (README), read as float32."""
    d = pd.read_csv(dryad("Table_S1_anemometer_data.txt"), sep=r"\s+", skiprows=1, header=None,
                    names=["u", "v", "w", "T"], on_bad_lines="skip", dtype="float32",
                    engine="c")
    return d


def night_mask(times, start_h=0, end_h=6):
    """Midnight to 6 am (Table S1)."""
    h = times.dt.hour
    return (h >= start_h) & (h < end_h)


# ---------------------------------------------------------------- GEOS-Chem

def geos_chem():
    """GEOS-Chem 12.1.0 bottom-level monthly fields, Jan 2013 to Feb 2014 (14 months)."""
    import scipy.io
    m = scipy.io.loadmat(io.BytesIO(zread("Figure 4/GEOS-Chem 12.1.0 Jan 2013 - Feb 2014.mat")))
    return {k: v for k, v in m.items() if not k.startswith("__")}


def factor_map(species):
    """13.2.1 preindustrial / 2013 factor map (12 months, 4 x 5 degrees)."""
    import h5py
    h = h5py.File(io.BytesIO(zread(f"Figure 4/GEOS-Chem 13.2.1 {species}_pi_pd_factor_map 2013.nc4")), "r")
    return {"lat": h["lat"][:], "lon": h["lon"][:], "time": h["time"][:],
            "factor": h[f"SpeciesConc_{species}"][:]}


# Bottom-level wind. The paper's distances are "degradation times ... multiplied by the mean
# horizontal wind speed of the bottom vertical grid" (SM, GEOS-Chem code availability) of the
# 12.1.0 run, driven by MERRA-2 2013 meteorology (SM, Global models); the deposited output holds
# no wind. GEOS-Chem reads that wind from its processed MERRA-2 files (A3dyn, U and V, 3-hourly
# means, level 1 the lowest). The 2 x 2.5 degree files for 2013 are not on the public GEOS-Chem
# bucket; the 0.5 x 0.625 files, from which the 2 x 2.5 files are made, are. They are read by
# ranges (level 1 only) and averaged to the 2 x 2.5 grid by block means (`to_gc_grid`), an
# assumption stated in the record. Source collection: MERRA-2 tavg3_3d_asm_Nv (M2T3NVASM),
# doi:10.5067/SUOQESM06LPK.
MERRA2_URL = "https://gcgrid.s3.amazonaws.com/GEOS_0.5x0.625/MERRA2/{y}/{m:02d}/MERRA2.{y}{m:02d}{d:02d}.A3dyn.05x0625.nc4"
MERRA2_LAT = np.arange(-90, 90.01, 0.5)
MERRA2_LON = np.arange(-180, 180, 0.625)


def _merra2_day(args):
    import h5py
    y, m, d = args
    with fsspec.open(MERRA2_URL.format(y=y, m=m, d=d), block_size=2**20).open() as fh:
        f = h5py.File(fh, "r")
        u, v = f["U"][:, 0].astype("f8"), f["V"][:, 0].astype("f8")
    return u.sum(0), v.sum(0), np.hypot(u, v).sum(0), u.shape[0]


def merra2_bottom_wind(month, year=2013, workers=4):
    """Monthly means (m/s) of U, V and of the speed sqrt(U^2 + V^2) of the lowest model level,
    over every 3-hourly field of the month, on the 0.5 x 0.625 grid (lat, lon)."""
    import calendar
    from concurrent.futures import ThreadPoolExecutor
    days = [(year, month, d) for d in range(1, calendar.monthrange(year, month)[1] + 1)]
    with ThreadPoolExecutor(workers) as ex:
        parts = list(ex.map(_merra2_day, days))
    n = sum(p[3] for p in parts)
    u, v, s = (sum(p[i] for p in parts) / n for i in range(3))
    return {"u": u, "v": v, "speed": s, "n_fields": n, "n_days": len(days)}


def to_gc_grid(a, lat, lon, dlat=2.0, dlon=2.5):
    """Block mean of a 0.5 x 0.625 field (lat, lon) over each cell of the GEOS-Chem 2 x 2.5 grid,
    returned as (lon, lat) like the 12.1.0 arrays. A fine cell counts when its centre lies in the
    coarse cell (half-open bounds); the polar half-cells take the points within 1 degree. A
    standard choice."""
    out = np.empty((len(lon), len(lat)))
    for j, la in enumerate(lat):
        mi = (np.abs(MERRA2_LAT - la) <= 1) if abs(la) > 89 else ((MERRA2_LAT >= la - dlat / 2) & (MERRA2_LAT < la + dlat / 2))
        sub = a[mi]
        for i, lo in enumerate(lon):
            dd = (MERRA2_LON - lo + 180) % 360 - 180
            out[i, j] = sub[:, (dd >= -dlon / 2) & (dd < dlon / 2)].mean()
    return out


# City coordinates. Table S13 says "City coordinates were obtained from (79)", the UN World
# Population Prospects 2019 Highlights, which give no city coordinates. The UN Population
# Division's file of agglomerations with coordinates is World Urbanization Prospects 2018, file
# F22 (annual populations, 1950 to 2035, in thousands, with latitude and longitude); its 2018
# column holds Table S13's populations for Tokyo (37,468,000), Delhi (28,514,000) and Kinshasa
# (13,171,000). It is no longer served by the UN site and is read from the Internet Archive's
# copy, pinned by snapshot time and SHA-256. Using it is an assumption stated in the record.
WUP_F22_URL = ("https://web.archive.org/web/20240824204902id_/https://population.un.org/wup/"
               "Download/Files/WUP2018-F22-Cities_Over_300K_Annual.xls")
WUP_F22_SHA256 = "4366cc15ecdda4d9ab420adfe730da6a7e35a8334615f50172a08d60b121c11c"

# The 97 cities of Table S13 (names as the table spells them, in alphabetical order), each with
# its agglomeration and country in WUP 2018 where the names differ or are shared. Labels only.
TABLE_S13_CITIES = {
    "Abidjan": None, "Abuja": None, "Addis Ababa": None, "Ahmedabad": ("Ahmadabad", "India"),
    "Alexandria": ("Al-Iskandariyah (Alexandria)", "Egypt"), "Ankara": None,
    "Asuncion": ("Asunción", "Paraguay"), "Athens": ("Athínai (Athens)", "Greece"),
    "Baghdad": None, "Bangalore": None, "Bangkok": ("Krung Thep (Bangkok)", "Thailand"),
    "Barcelona": ("Barcelona", "Spain"), "Beijing": None, "Belo Horizonte": None, "Berlin": None,
    "Bogota": ("Bogotá", "Colombia"), "Brasilia": ("Brasília", "Brazil"), "Buenos Aires": None,
    "Cairo": ("Al-Qahirah (Cairo)", "Egypt"), "Cape Town": None,
    "Casablanca": ("Dar-el-Beida (Casablanca)", "Morocco"), "Chennai": ("Chennai (Madras)", "India"),
    "Chongqing": None, "Dakar": None, "Dar Es Salaam": ("Dar es Salaam", "United Republic of Tanzania"),
    "Dehli": ("Delhi", "India"), "Dhaka": None, "Douala": None,
    "Durban": ("Durban (Ethekwini)", "South Africa"),
    "Guangzhou": ("Guangzhou, Guangdong", "China"), "Guatemala City": ("Ciudad de Guatemala (Guatemala City)", "Guatemala"),
    "Guayaquil": None, "Hanoi": ("Hà Noi", "Viet Nam"),
    "Ho Chi Minh City": ("Thành Pho Ho Chí Minh (Ho Chi Minh City)", "Viet Nam"), "Hong Kong": None,
    "Hyderabad": ("Hyderabad", "India"), "Ibadan": None, "Istanbul": None, "Jakarta": None,
    "Jiddah": None, "Johannesburg": None, "Kabul": None, "Kampala": None, "Kano": None,
    "Karachi": None, "Khartoum": ("Al-Khartum (Khartoum)", "Sudan"), "Kiev": ("Kyiv (Kiev)", "Ukraine"),
    "Kinshasa": None, "Kolkata": ("Kolkata (Calcutta)", "India"), "Kuala Lumpur": None, "Kumasi": None,
    "Kuwait City": ("Al Kuwayt (Kuwait City)", "Kuwait"), "Lagos": None, "Lahore": None,
    "Lima": ("Lima", "Peru"), "London": ("London", "United Kingdom"),
    "Los Angeles": ("Los Angeles-Long Beach-Santa Ana", "United States of America"), "Luanda": None,
    "Lusaka": None, "Madrid": None, "Manila": None, "Mashhad": None, "Medellin": ("Medellín", "Colombia"),
    "Melbourne": ("Melbourne", "Australia"), "Mexico City": ("Ciudad de México (Mexico City)", "Mexico"),
    "Milan": ("Milano (Milan)", "Italy"), "Montereal": ("Montréal", "Canada"), "Monterrey": None,
    "Moscow": ("Moskva (Moscow)", "Russian Federation"), "Mumbai": ("Mumbai (Bombay)", "India"),
    "Nairobi": None, "New York": ("New York-Newark", "United States of America"),
    "Osaka": ("Kinki M.M.A. (Osaka)", "Japan"), "Ouagadougou": None, "Paris": None,
    "Porto Alegre": ("Pôrto Alegre", "Brazil"), "Puebla": None, "Pyongyang": ("P'yongyang", "Dem. People's Republic of Korea"),
    "Recife": None, "Rio De Janeiro": ("Rio de Janeiro", "Brazil"), "Riyadh": ("Ar-Riyadh (Riyadh)", "Saudi Arabia"),
    "Rome": ("Roma (Rome)", "Italy"), "Sanaa": ("Sana'a'", "Yemen"), "Santiago": ("Santiago", "Chile"),
    "Santo Domingo": ("Santo Domingo", "Dominican Republic"), "Sao Paulo": ("São Paulo", "Brazil"),
    "Seoul": None, "Shanghai": None, "Singapore": None, "Sydney": None,
    "Tehran": None, "Tel Aviv": ("Tel Aviv-Yafo (Tel Aviv-Jaffa)", "Israel"), "Tokyo": None,
    "Toronto": None, "Xinbei": None, "Yangon": None, "Yaonde": ("Yaoundé", "Cameroon"),
}


# Table S13 as printed in the Supplementary Materials (page 33 on): city, population, present
# recognition distance (m) and present percentage of the preindustrial distance, in the table's
# order (impact rank 1 to 97). Copied from the paper's text for the regressions of Fig. S9.
TABLE_S13_PRINTED = [
    ("Hong Kong", 7684801, 1326.6, 4.9), ("Tokyo", 37468000, 1014.6, 6.7), ("Jakarta", 10517000, 2859.5, 7.2),
    ("Kuwait City", 3297759, 433.9, 7.9), ("Osaka", 19013434, 1561.7, 8.0),
    ("Shanghai", 25582000, 1512.9, 8.2), ("Guangzhou", 14284353, 2144.9, 8.8),
    ("Xinbei", 4504147, 2109.3, 9.3), ("Los Angeles", 12458000, 452.4, 9.5),
    ("Guayaquil", 3142466, 1280.8, 10.1), ("Chongqing", 17340704, 1028.9, 11.0),
    ("Riyadh", 6907000, 245.4, 11.3), ("Chennai", 11776147, 2818.8, 11.4), ("Madrid", 6497000, 240.9, 12.3),
    ("Tehran", 8896000, 622.2, 12.4), ("Seoul", 9963000, 1972.5, 12.4), ("New York", 18819000, 751.0, 12.5),
    ("Dhaka", 19578000, 2236.9, 13.3), ("Jiddah", 4862941, 382.4, 13.9), ("Kolkata", 15332793, 1804.3, 14.8),
    ("Buenos Aires", 14967000, 678.3, 15.2), ("Barcelona", 5687356, 177.4, 15.9),
    ("Paris", 10901000, 282.8, 16.6), ("Berlin", 3573938, 706.4, 17.6), ("Rome", 4315671, 451.1, 18.0),
    ("Mashhad", 3367852, 855.3, 18.2), ("Dehli", 28514000, 557.9, 18.4), ("London", 9046000, 532.4, 18.4),
    ("Bangalore", 13607800, 4751.5, 18.6), ("Singapore", 5792000, 1508.4, 18.7),
    ("Toronto", 6371958, 612.3, 19.0), ("Milan", 3154570, 157.6, 19.0), ("Lahore", 13979390, 330.5, 19.6),
    ("Rio De Janeiro", 13727720, 1972.1, 19.8), ("Johannesburg", 5486000, 716.8, 20.2),
    ("Athens", 3154563, 1148.4, 20.5), ("Manila", 13482000, 2494.3, 21.9),
    ("Hyderabad", 10801163, 5567.2, 22.1), ("Casablanca", 3892837, 1159.8, 23.3),
    ("Mexico City", 21581000, 1076.1, 24.0), ("Beijing", 21766214, 870.0, 24.7),
    ("Ahmedabad", 8650605, 3795.0, 25.0), ("Medellin", 4102308, 1649.8, 25.1),
    ("Guatemala City", 3095099, 923.5, 25.7), ("Ho Chi Minh City", 9320866, 6404.8, 25.7),
    ("Belo Horizonte", 6247889, 1687.4, 26.5), ("Santo Domingo", 3523890, 5568.6, 26.5),
    ("Lima", 10391000, 3579.9, 26.6), ("Sao Paulo", 21650000, 1878.9, 26.6),
    ("Pyongyang", 3157538, 2293.2, 27.5), ("Dakar", 3429536, 2512.1, 27.6), ("Sanaa", 3292497, 980.4, 29.4),
    ("Ankara", 5397098, 1386.5, 29.8), ("Moscow", 12410000, 1249.8, 30.3), ("Hanoi", 5253385, 3956.9, 30.7),
    ("Kiev", 3016789, 2119.9, 30.7), ("Puebla", 3344761, 2403.9, 31.6), ("Santiago", 6903392, 101.8, 32.5),
    ("Istanbul", 14751000, 1795.0, 32.6), ("Bangkok", 10156000, 6504.7, 35.1),
    ("Recife", 4263940, 7011.8, 35.6), ("Bogota", 10574000, 1944.3, 35.8),
    ("Kuala Lumpur", 7564000, 2370.3, 36.2), ("Baghdad", 7711305, 1975.3, 39.2),
    ("Khartoum", 6344348, 2787.1, 42.3), ("Monterrey", 5116647, 4061.2, 45.0),
    ("Melbourne", 5235407, 2874.4, 45.1), ("Porto Alegre", 4211933, 3815.9, 46.7),
    ("Durban", 3228003, 2053.5, 47.5), ("Montereal", 4307958, 1806.7, 47.6),
    ("Cairo", 20076000, 1345.8, 48.6), ("Tel Aviv", 4420855, 2615.9, 50.8), ("Kano", 4348481, 2729.2, 51.5),
    ("Alexandria", 5588477, 3350.2, 52.0), ("Lagos", 13463000, 4912.6, 52.6), ("Kabul", 4588666, 73.1, 52.7),
    ("Brasilia", 4873048, 3239.1, 53.3), ("Cape Town", 4890280, 12313.0, 56.7),
    ("Asuncion", 3510511, 3060.7, 59.2), ("Yangon", 5610241, 11357.8, 59.4),
    ("Sydney", 5231147, 1678.4, 60.2), ("Kampala", 3846102, 1206.3, 60.6),
    ("Mumbai", 21296516, 16212.5, 62.2), ("Karachi", 15400000, 10303.0, 63.3),
    ("Dar Es Salaam", 6048000, 9636.5, 63.4), ("Ibadan", 3874908, 5703.5, 64.2),
    ("Abuja", 3839646, 4049.4, 64.6), ("Nairobi", 5325160, 9510.7, 70.8), ("Lusaka", 3181250, 3598.3, 73.9),
    ("Ouagadougou", 3203923, 4788.6, 75.1), ("Douala", 4063200, 5189.3, 75.4),
    ("Yaonde", 4509287, 3575.6, 76.4), ("Kumasi", 3768239, 7512.6, 78.7), ("Luanda", 9292336, 6196.0, 78.9),
    ("Abidjan", 5686350, 7639.9, 81.3), ("Addis Ababa", 5460591, 7535.6, 82.5),
    ("Kinshasa", 13171000, 1892.5, 89.8),
]


def table_s13_printed():
    """Table S13 as the paper prints it, with the impact rank (row order)."""
    t = pd.DataFrame(TABLE_S13_PRINTED, columns=["city", "population", "distance_m", "percent_of_preindustrial"])
    t["rank"] = np.arange(1, len(t) + 1)
    return t


def table_s13_cities():
    """The Table S13 cities with WUP 2018 coordinates and 2018 population (persons). Every city
    must match exactly one agglomeration."""
    r = requests.get(WUP_F22_URL, timeout=300)
    r.raise_for_status()
    if hashlib.sha256(r.content).hexdigest() != WUP_F22_SHA256:
        raise ValueError("WUP 2018 F22 file differs from the pinned copy")
    w = pd.read_excel(io.BytesIO(r.content), header=16, engine="xlrd")
    rows = []
    for name, key in TABLE_S13_CITIES.items():
        agg, country = key if key else (name, None)
        m = w[w["Urban Agglomeration"] == agg]
        if country:
            m = m[m["Country or area"] == country]
        if len(m) != 1:
            raise ValueError(f"{name}: {len(m)} matches in WUP 2018")
        m = m.iloc[0]
        rows.append({"city": name, "wup_name": m["Urban Agglomeration"], "country": m["Country or area"],
                     "lat": float(m["Latitude"]), "lon": float(m["Longitude"]),
                     "population_2018": float(m[2018]) * 1000})
    return pd.DataFrame(rows)


def land_fraction(lat, lon, dlat=2.0, dlon=2.5, step=0.1):
    """Share of land points within each cell of the 2 x 2.5 grid, from global-land-mask 1.0.0
    (the package the SM name, Global models: a cell is land when any of it is land). The
    sampling step of 0.1 degree is a standard choice."""
    from global_land_mask import globe
    frac = np.zeros((len(lon), len(lat)))
    for j, la in enumerate(lat):
        lo_lat, hi_lat = max(la - dlat / 2, -90), min(la + dlat / 2, 90)
        plat = np.arange(lo_lat + step / 2, hi_lat, step)
        for i, lo in enumerate(lon):
            plon = np.arange(lo - dlon / 2 + step / 2, lo + dlon / 2, step)
            plon = (plon + 180) % 360 - 180
            gl, go = np.meshgrid(plat, plon)
            frac[i, j] = globe.is_land(gl, go).mean()
    return frac


# Table S12 of the SM: rate constants (cm3 molecule-1 s-1) with O3 and NO3 of the 23 floral
# volatiles of Fig. S8B, and their class. These are literature constants the paper tabulates;
# the criterion of figs8-no3-faster-than-o3 takes them from Table S12.
TABLE_S12 = [
    ("b-pinene", "monoterpene", 1.50e-17, 2.51e-12),
    ("(Z/E)-ocimene", "monoterpene", 3.74e-16, 2.20e-11),
    ("b-myrcene", "monoterpene", 4.70e-16, 1.10e-11),
    ("D-limonene", "monoterpene", 2.10e-16, 1.22e-11),
    ("a-pinene", "monoterpene", 8.40e-17, 6.16e-12),
    ("linalool", "monoterpene", 4.30e-16, 1.12e-11),
    ("2-carene", "monoterpene", 2.30e-16, 1.90e-11),
    ("3-carene", "monoterpene", 3.70e-17, 9.10e-12),
    ("camphene", "monoterpene", 9.00e-19, 6.60e-13),
    ("a-phellandrene", "monoterpene", 3.00e-15, 7.30e-11),
    ("b-phellandrene", "monoterpene", 4.70e-17, 8.00e-12),
    ("sabinene", "monoterpene", 8.30e-17, 1.00e-11),
    ("a-terpinene", "monoterpene", 2.10e-14, 1.40e-10),
    ("g-terpinene", "monoterpene", 1.40e-16, 2.90e-11),
    ("terpinolene", "monoterpene", 1.90e-15, 9.70e-11),
    ("b-caryophyllene", "sesquiterpene", 1.16e-14, 1.90e-11),
    ("a-cedrene", "sesquiterpene", 2.80e-17, 8.20e-12),
    ("longifolene", "sesquiterpene", 5.00e-19, 6.80e-13),
    ("a-copaene", "sesquiterpene", 1.60e-16, 1.60e-11),
    ("a-humulene", "sesquiterpene", 1.17e-14, 3.90e-11),
    ("cis-3-hexen-1-ol", "green leaf volatile", 6.40e-17, 2.72e-13),
    ("cis-3-hexenylacetate", "green leaf volatile", 5.40e-17, 2.46e-13),
    ("trans-2-hexenal", "green leaf volatile", 2.00e-18, 1.21e-14),
]

# Air number density implied by Table S12's own rates (37 ppb O3 times 1.5e-17 gives 1.37e-5 s-1
# for b-pinene), the reading (2) of fig4ab-no3-shortens-recognition.
AIR_DENSITY_TABLE_S12 = 2.46e19


def number_density(mixing_ratio, pres_hpa=None, temp_k=None):
    """Molecules per cm3 from a mixing ratio (v/v): at the cell's pressure and temperature when
    given (reading 1), else at the fixed density of Table S12 (reading 2)."""
    if pres_hpa is None:
        return mixing_ratio * AIR_DENSITY_TABLE_S12
    kb = 1.380649e-19  # hPa cm3 K-1
    return mixing_ratio * pres_hpa / (kb * temp_k)
