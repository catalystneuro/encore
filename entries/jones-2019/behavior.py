"""Behavioral data of CRCNS hc-26 (Jones et al. 2019, Cell Reports 29, 2123-2133).

Loads the behavior summary spreadsheets of both cohorts, streamed from the public
CRCNS S3 bucket (nothing is written to disk), and returns tidy pandas DataFrames.

Sources
-------
* ``Cohort_1/Behavior.tar.gz``: ``Behavior/Morris Water Maze.xls`` (screen cohort,
  MWM at 13-19 months).
* ``Cohort_2/Behavior.tar.gz``: ``Behavior/6-9mo Morris Water Maze.xlsx``,
  ``Behavior/14-18mo Morris Water Maze.xls``, ``Behavior/Active Place Avoidance.xlsx``,
  ``Behavior/APA Mouse List.xlsx``, ``Behavior/Open Field.xlsx``,
  ``Behavior/Elevated Plus Maze.xlsx``, ``Behavior/Hot Plate.xlsx`` and the APA
  tracking files ``Behavior/APA Tracking/*.dat`` (used only for distance from the
  shock zone per movement bout, which is not in the spreadsheets).
* ``Cohort_1/animaldef.m`` and ``Cohort_2/animaldef.m``: ephys animal names and
  genotypes.

Methods references: "STAR Methods" of the paper (Behavior; Analysis of Behavioral
Data) and the claims file ``claims/jones-2019.yaml`` (methods C and D).

Identity linking (see :func:`link_table`)
-----------------------------------------
* Cohort 1: the MWM sheet labels mice ``"<ear tag> (<code>)"``; the code is the NN of
  the ephys name ``rX_NN_`` (all 29 ephys NN are unique, so the rack prefix is
  resolved; ear tags are not unique, e.g. 1386 and 1388 appear once as E3 and once as
  E4, so the label string, not the ear tag, identifies a mouse).
* Cohort 2: ``APA Mouse List.xlsx`` sheet ``IPA Manifest`` links ``Mouse #`` (ear tag),
  ``MWM Blind Code`` (the ID used by the 14-18 month MWM, APA ``Blinded Code``, open
  field ``Mouse`` and elevated plus maze ``Info A``) and ``Name`` (ephys name).  The
  6-9 month MWM uses its own ``MWM ID`` numbering, for which no file in the data set
  gives names, so 6-9 month MWM mice cannot be linked to ephys animals (``name`` is
  None).

Every returned frame has columns ``cohort``, ``mouse`` (the behavior ID of the source
file), ``name`` (ephys name or None) and ``genotype`` ('E3'/'E4'); mice of other lines
in the sheets (WT, APPKO, EKO, bumetanide controls) are dropped.
"""

from __future__ import annotations

import io
import math
import re
import tarfile

import fsspec
import numpy as np
import pandas as pd

BASE_URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-26/live/data"
TAR_URL = {c: f"{BASE_URL}/Cohort_{c}/Behavior.tar.gz" for c in (1, 2)}
ANIMALDEF_URL = {c: f"{BASE_URL}/Cohort_{c}/animaldef.m" for c in (1, 2)}

# Members of the tarballs that are parsed (summary spreadsheets).
EXCEL_MEMBERS = {
    1: {"mwm_13-19mo": "Behavior/Morris Water Maze.xls"},
    2: {
        "mwm_6-9mo": "Behavior/6-9mo Morris Water Maze.xlsx",
        "mwm_14-18mo": "Behavior/14-18mo Morris Water Maze.xls",
        "apa": "Behavior/Active Place Avoidance.xlsx",
        "manifest": "Behavior/APA Mouse List.xlsx",
        "open_field": "Behavior/Open Field.xlsx",
        "epm": "Behavior/Elevated Plus Maze.xlsx",
        "hot_plate": "Behavior/Hot Plate.xlsx",
    },
}
APA_TRACK_DIR = "Behavior/APA Tracking/"
MWM_AGES = {1: ("13-19mo",), 2: ("6-9mo", "14-18mo")}

# Parsed results, so that repeated calls stream each tarball only once.
_CACHE: dict = {}


# ----------------------------------------------------------------------------- helpers
def norm_name(s) -> str:
    """Case-, space-, underscore- and punctuation-insensitive key for a mouse name."""
    if s is None or (isinstance(s, float) and math.isnan(s)):
        return ""
    return re.sub(r"[^a-z0-9]", "", str(s).lower())


def _geno(s):
    """'E3'/'E4' from a genotype cell ('E3 Ki', 'E3/E3', 'E3Ki', 'E4'); None for other
    lines (WT, APPKO, EKO, 'E4Ki-Bumetanide Ctrls', ...)."""
    key = norm_name(s)
    for g in ("e3", "e4"):
        if key in (g, g + "ki", g + g):
            return g.upper()
    return None


def _num(v):
    """Float or NaN (strings such as 'Excluded' become NaN)."""
    try:
        f = float(v)
    except (TypeError, ValueError):
        return np.nan
    return f


def _is_int_like(v) -> bool:
    f = _num(v)
    return not math.isnan(f) and float(f).is_integer()


def _read_excel(data: bytes, member: str) -> dict:
    engine = "xlrd" if member.lower().endswith(".xls") else "openpyxl"
    return pd.read_excel(io.BytesIO(data), sheet_name=None, header=None, engine=engine)


def _sheet(book: dict, *keys: str) -> pd.DataFrame:
    """Sheet whose normalized name equals one of ``keys``."""
    for name, df in book.items():
        if norm_name(name) in keys:
            return df
    raise KeyError(f"no sheet {keys} in {list(book)}")


def _parse_dat(data: bytes) -> pd.DataFrame:
    """Tracker .dat file -> frame columns x, y (pixels), level, frameinfo.

    Record format (file header): FrameCount 1msTimeStamp RoomX RoomY Sectors State
    CurrentLevel MotorState Flags FrameInfo.
    """
    off = data.index(b"%%END_HEADER")
    off = data.index(b"\n", off) + 1
    df = pd.read_csv(io.BytesIO(data[off:]), sep="\t", header=None, usecols=[2, 3, 6, 9])
    df.columns = ["x", "y", "level", "frameinfo"]
    return df.astype("float32")


def _stream(cohort: int) -> dict:
    """Stream ``Cohort_<cohort>/Behavior.tar.gz`` once; keep needed members in memory.

    Returns {'excel': {key: {sheet: DataFrame}}, 'apa_tracks': {(code, trial, frame,
    rerun): DataFrame}} (APA tracks for cohort 2 only).
    """
    key = ("tar", cohort)
    if key in _CACHE:
        return _CACHE[key]
    wanted = {v: k for k, v in EXCEL_MEMBERS[cohort].items()}
    excel, tracks = {}, {}
    pat = re.compile(r"(Arena|Room)Trac?k?_(\d{1,3})_([A-Za-z0-9]{1,5})_(Rerun_)?.*\.dat$")
    with fsspec.filesystem("http").open(TAR_URL[cohort], block_size=0) as f:
        with tarfile.open(fileobj=f, mode="r|gz") as tf:
            for m in tf:
                if not m.isfile():
                    continue
                if m.name in wanted:
                    excel[wanted[m.name]] = _read_excel(tf.extractfile(m).read(), m.name)
                elif cohort == 2 and m.name.startswith(APA_TRACK_DIR):
                    mt = pat.match(m.name[len(APA_TRACK_DIR):])
                    if mt:
                        k = (int(mt.group(2)), mt.group(3).upper(), mt.group(1).lower(),
                             bool(mt.group(4)))
                        tracks[k] = _parse_dat(tf.extractfile(m).read())
                if cohort == 1 and len(excel) == len(wanted):
                    break  # Cohort 1 needs only the summary sheet; stop streaming.
    missing = set(wanted.values()) - set(excel)
    if missing:
        raise RuntimeError(f"members not found in {TAR_URL[cohort]}: {missing}")
    _CACHE[key] = {"excel": excel, "apa_tracks": tracks}
    return _CACHE[key]


def _excel(cohort: int, key: str) -> dict:
    return _stream(cohort)["excel"][key]


# ----------------------------------------------------------------------------- ephys names
def ephys_animals(cohort: int) -> pd.DataFrame:
    """Ephys animals from ``Cohort_<c>/animaldef.m``.

    Columns: cohort, ephys_name (spelling of the first recording), key (normalized),
    genotype, ephys_ages (recording age groups), spellings (all spellings used),
    code (Cohort 1: NN of rX_NN_), age_comment (Cohort 1: the trailing comment, in
    months).
    """
    key = ("animaldef", cohort)
    if key not in _CACHE:
        with fsspec.filesystem("http").open(ANIMALDEF_URL[cohort], "rt") as f:
            text = f.read()
        rows = []
        for m in re.finditer(
            r"case\s+'([^']+)'\s*\n\s*animalinfo\s*=\s*\{'([^']+)','([^']*)','[^']*','(E\d)'[^}]*\};"
            r"[ \t]*(?:%[ \t]*(\S+))?", text):
            case, name, path, geno, comment = m.groups()
            age = re.search(r"/(\d+-\d+mo)/", path)
            rows.append({"name": name, "geno": geno, "age": age.group(1) if age else None,
                         "comment": comment})
        raw = pd.DataFrame(rows)
        raw["key"] = raw["name"].map(norm_name)
        out = []
        for k, g in raw.groupby("key", sort=False):
            r = {"cohort": cohort, "ephys_name": g["name"].iloc[0], "key": k,
                 "genotype": "/".join(sorted(set(g["geno"]))),
                 "ephys_ages": ",".join(a for a in g["age"] if a) or None,
                 "spellings": ",".join(dict.fromkeys(g["name"]))}
            if cohort == 1:
                nn = re.match(r"r\d+_(\d+)_", g["name"].iloc[0])
                r["code"] = int(nn.group(1)) if nn else None
                r["age_comment"] = g["comment"].iloc[0]
            out.append(r)
        _CACHE[key] = pd.DataFrame(out)
    return _CACHE[key].copy()


# ----------------------------------------------------------------------------- MWM parsing
_ID_LABELS = ("mouseblindcode", "mwmid")
_GENO_LABELS = ("apoe", "mouseline")


def _find_cols(df: pd.DataFrame, header_row: int):
    """(id column, genotype column) = first columns with the known header labels."""
    labels = [norm_name(v) for v in df.iloc[header_row]]
    idc = next(i for i, v in enumerate(labels) if v in _ID_LABELS)
    gc = next(i for i, v in enumerate(labels) if v.startswith(_GENO_LABELS))
    return idc, gc


def _valid_id(cohort: int, v) -> bool:
    if cohort == 1:
        return isinstance(v, str) and re.search(r"\(\d+\)", v) is not None
    return _is_int_like(v)


def _mouse_id(cohort: int, v):
    """Cohort 1: the label string ('1360 (12)'); Cohort 2: int ID."""
    return str(v).strip() if cohort == 1 else int(_num(v))


def _code_c1(label: str):
    """Cohort 1 '1360 (12)' -> (ear tag 1360 or None, code 12)."""
    m = re.match(r"\s*(\d+)?\s*\((\d+)\)", label)
    return (int(m.group(1)) if m.group(1) else None), int(m.group(2))


def _trial_blocks(df: pd.DataFrame, cohort: int):
    """Iterate (id, genotype, notes, rows) over the per-mouse blocks of a sheet laid out
    as ID / genotype / 'Session' columns with one row per session (Hidden and Visible
    sheets).  Notes are strings found in the ID/genotype columns of later rows."""
    h = next(i for i in range(len(df)) if "session" in [norm_name(v) for v in df.iloc[i]])
    idc, gc = _find_cols(df, h)
    sc = [norm_name(v) for v in df.iloc[h]].index("session")
    cur = None
    for i in range(h + 1, len(df)):
        sess = _num(df.iat[i, sc])
        if math.isnan(sess):
            continue
        if sess == 1 and _valid_id(cohort, df.iat[i, idc]):
            if cur:
                yield cur
            cur = {"id": _mouse_id(cohort, df.iat[i, idc]), "geno_cell": df.iat[i, gc],
                   "notes": [], "rows": []}
        if cur is None:
            continue
        if sess != 1:
            for c in (idc, gc):
                v = df.iat[i, c]
                if isinstance(v, str) and v.strip():
                    cur["notes"].append(v.strip())
        cur["rows"].append(i)
    if cur:
        yield cur


def _mwm_book(cohort: int, age):
    if age is None and cohort == 1:
        age = MWM_AGES[1][0]
    if cohort not in MWM_AGES or age not in MWM_AGES[cohort]:
        raise ValueError(f"MWM data exist for {MWM_AGES}; got cohort={cohort}, age={age}")
    return age, _excel(cohort, f"mwm_{age}")


def _names(cohort: int) -> dict:
    """Behavior ID -> ephys name, from :func:`link_table` (14-18 month MWM / APA / OF /
    EPM blind code for Cohort 2; MWM label for Cohort 1)."""
    if _CACHE.get("_building_link"):
        return {}
    lt = link_table()
    lt = lt[(lt["cohort"] == cohort) & lt["ephys_name"].notna()]
    if cohort == 1:
        return dict(zip(lt["mwm_label"], lt["ephys_name"]))
    lt = lt[lt["blind_code"].notna()]
    return dict(zip(lt["blind_code"].astype(int), lt["ephys_name"]))


def _attach(df: pd.DataFrame, cohort: int, id_system: str | None = None) -> pd.DataFrame:
    """Add cohort/name columns; name only where the ID system is the linked one."""
    df.insert(0, "cohort", cohort)
    if cohort == 1 or id_system == "blind_code":
        names = _names(cohort)
        nm = df["mouse"].map(names).astype(object)
        df.insert(2, "name", nm.where(nm.notna(), None))
    else:
        df.insert(2, "name", None)
    if cohort == 1:
        tags = df["mouse"].map(_code_c1)
        df["ear_tag"] = [t[0] for t in tags]
        df["code"] = [t[1] for t in tags]
    return df


def _id_system(cohort, age):
    """Cohort 2: the 6-9 month MWM has its own ID numbering ('mwm_6-9mo_id'); the
    14-18 month MWM uses the manifest's MWM Blind Code."""
    if cohort == 1:
        return "mwm_label"
    return "mwm_6-9mo_id" if age == "6-9mo" else "blind_code"


def mwm_hidden(cohort: int = 1, age: str | None = None) -> pd.DataFrame:
    """Hidden-platform MWM escape latency, one row per mouse, hidden day and trial.

    Columns: cohort, mouse, name, genotype, day, trial, latency_s, id_system, notes
    (+ ear_tag, code for Cohort 1).

    Source: sheet 'Learning Hidden Trials'.  Layout (worked out from the sheet): the
    columns HD1..HDk are hidden days and the rows 'Session' 1-4 under each mouse are the
    4 daily trials (the sheet's own 'AVERAGE/mouse' HDk cell is the mean of the HDk
    column over the 4 rows; trial 1 of HD1 is at the 60 s ceiling for nearly all mice).
    Cohort 1 and the 14-18 month sheet have 7 hidden days (HD1-HD7), the 6-9 month sheet
    5.  The Methods (Behavior) describe 5 hidden days and all analyses use days 1-5 at
    most (the author's working 'Sheet1' of the 14-18 month file also averages only days
    1-5), so analyses should filter ``day <= 5``; days 6-7 are returned as recorded.
    Latencies are as exported from Ethovision (Methods, Analysis of Behavioral Data);
    60.06 s is the trial cutoff (60 s at 30 frames/s).  The daily escape latency of the
    paper is the mean of the 4 trials (Methods; claims method C), see
    :func:`mwm_daily`.
    """
    age, book = _mwm_book(cohort, age)
    df = _sheet(book, "learninghiddentrials")
    h = next(i for i in range(len(df)) if "session" in [norm_name(v) for v in df.iloc[i]])
    labels = [norm_name(v) for v in df.iloc[h]]
    sc = labels.index("session")
    days = []
    for c in range(sc + 1, len(labels)):
        m = re.fullmatch(r"hd(\d+)", labels[c])
        # the trial columns end at the first non-HD label or where the day numbers
        # restart (the sheet's 'AVERAGE/mouse' block follows directly in some files)
        if not m or (days and int(m.group(1)) <= days[-1][1]):
            break
        days.append((c, int(m.group(1))))
    rows = []
    for b in _trial_blocks(df, cohort):
        g = _geno(b["geno_cell"])
        if g is None:
            continue
        for i in b["rows"]:
            for c, d in days:
                rows.append({"mouse": b["id"], "genotype": g, "day": d,
                             "trial": int(_num(df.iat[i, sc])), "latency_s": _num(df.iat[i, c]),
                             "id_system": _id_system(cohort, age),
                             "notes": "; ".join(b["notes"]) or None})
    out = pd.DataFrame(rows)
    return _attach(out, cohort, _id_system(cohort, age))


def mwm_daily(cohort: int = 1, age: str | None = None, max_day: int = 5) -> pd.DataFrame:
    """Per mouse and hidden day: mean escape latency over the 4 daily trials (Methods:
    "Escape latency was averaged across the 4 daily trials"), days 1..``max_day``.
    Mice without data (all NaN, e.g. Cohort 1 1585 (19), euthanized) are dropped."""
    h = mwm_hidden(cohort, age)
    h = h[h["day"] <= max_day]
    keys = [c for c in ("cohort", "mouse", "name", "genotype", "ear_tag", "code") if c in h]
    out = h.groupby(keys + ["day"], dropna=False, sort=False)["latency_s"].mean().reset_index()
    return out[out["latency_s"].notna()].reset_index(drop=True)


def mwm_probe(cohort: int = 1, age: str | None = None) -> pd.DataFrame:
    """MWM probe trials 1-3, one row per mouse and probe.

    Columns: cohort, mouse, name, genotype, probe, target_quadrant, target_quadrant_s,
    quadrant_total_s, pct_time_target_quadrant, target_crossings, velocity_cm_s,
    auc_first5s (cm*s), id_system.

    * target_quadrant_s and target_crossings: exported by Ethovision (Methods), sheet
      'Memory Probe N' (Cohort 1, 14-18 months) or 'Probe N' (6-9 months), columns
      '<Q> Quad Dur (s)' and '<Q> Plat Freq' of the quadrant marked 'TARGET' in the row
      above the header (SE for Cohort 1, NE for Cohort 2).  The sheets give no
      per-mouse percentage.
    * pct_time_target_quadrant = 100 * target_quadrant_s / 60, the 60 s probe duration
      of the Methods (Behavior).  This matches the sheets' group 'AVERAGE(%)' cells of
      both Cohort 2 files (AVERAGE(S)/60); in the Cohort 1 file 'AVERAGE(%)' equals
      AVERAGE(S)/44, an unexplained divisor, so the 60 s definition is used throughout
      (a constant factor cannot change a t test or a correlation).  quadrant_total_s
      (sum of the four quadrant durations, < 60 s when the mouse is outside all zones)
      is given for the alternative denominator.
    * auc_first5s: area under the distance-to-platform curve over the first 5 s by the
      trapezoid method (Methods; Figure 2H legend "during the first 5 s of probe 1";
      claims method C).  Sheets 'Probe N DistanceTime' / 'Probe N Distance Time' /
      'PROX Probe N' hold distance to the platform location in cm ('**Distance in cm')
      per 1 s time bin, columns labelled 1..60 (s).  The trapezoid is over the bins
      labelled 1-5 s (x in s, 4 intervals), the only samples in the first 5 s; there is
      no 0 s sample.
    """
    age, book = _mwm_book(cohort, age)
    rows = []
    for p in (1, 2, 3):
        q = _sheet(book, f"memoryprobe{p}", f"probe{p}")
        hdr = 1
        idc, gc = _find_cols(q, hdr)
        labels = [str(v) for v in q.iloc[hdr]]
        stop = next((c for c in range(idc + 1, len(labels))
                     if norm_name(labels[c]) in _ID_LABELS), len(labels))
        quad = {c: labels[c] for c in range(stop) if "Quad Dur" in labels[c]}
        freq = {c: labels[c] for c in range(stop) if "Plat Freq" in labels[c]}
        tq = [c for c in quad if norm_name(q.iat[0, c]) == "target"]
        tf_ = [c for c in freq if norm_name(q.iat[0, c]) == "target"]
        vel = next((c for c in range(stop) if labels[c].startswith("Velocity")), None)
        assert len(tq) == 1 and len(tf_) == 1, "target quadrant not found"
        tq, tf_ = tq[0], tf_[0]
        dt = _sheet(book, f"probe{p}distancetime", f"proxprobe{p}")
        didc, dgc = _find_cols(dt, 1)
        tcols = {c: _num(dt.iat[1, c]) for c in range(dt.shape[1])
                 if c > didc and not math.isnan(_num(dt.iat[1, c]))}
        first5 = sorted((t, c) for c, t in tcols.items() if t <= 5)
        auc = {}
        g_ff = None
        for i in range(2, len(dt)):
            gv = dt.iat[i, dgc]
            if isinstance(gv, str) and gv.strip():
                g_ff = gv
            if _valid_id(cohort, dt.iat[i, didc]):
                y = [_num(dt.iat[i, c]) for _, c in first5]
                auc[(_mouse_id(cohort, dt.iat[i, didc]), _geno(g_ff))] = float(
                    np.trapezoid(y, [t for t, _ in first5]))
        g_ff = None
        for i in range(hdr + 1, len(q)):
            gv = q.iat[i, gc]
            if isinstance(gv, str) and gv.strip():
                g_ff = gv
            if not _valid_id(cohort, q.iat[i, idc]):
                continue
            g = _geno(g_ff)
            if g is None:
                continue
            mid = _mouse_id(cohort, q.iat[i, idc])
            tsec = _num(q.iat[i, tq])
            rows.append({
                "mouse": mid, "genotype": g, "probe": p,
                "target_quadrant": quad[tq].split()[0],
                "target_quadrant_s": tsec,
                "quadrant_total_s": float(np.nansum([_num(q.iat[i, c]) for c in quad])),
                "pct_time_target_quadrant": 100.0 * tsec / 60.0,
                "target_crossings": _num(q.iat[i, tf_]),
                "velocity_cm_s": _num(q.iat[i, vel]) if vel is not None else np.nan,
                "auc_first5s": auc.get((mid, g), np.nan),
                "id_system": _id_system(cohort, age)})
    return _attach(pd.DataFrame(rows), cohort, _id_system(cohort, age))


def mwm_visible(cohort: int = 1, age: str | None = None) -> pd.DataFrame:
    """Visible-platform MWM latency, one row per mouse.

    Columns: cohort, mouse, name, genotype, visible_latency_s (mean over all visible
    trials), n_trials, id_system, notes.

    Methods (Behavior): "twice daily visible trials over 3 days" = 6 trials.  Cohort 1
    sheet 'Visible - 1 Day': rows 'Session' 1-3 (labelled V01-V03) x two columns 'VD1'
    = 6 trials (the sheet name says 1 day, its labels 3 sessions; immaterial for the
    mean).  Cohort 2 sheets 'Visible': rows 'Session' 1-6, one trial column.  The
    per-mouse value is the mean over all trials; the Figure S2 legend does not say how
    trials were combined, the mean over all 6 is the standard choice (it equals the mean
    of the 3 daily means).
    """
    age, book = _mwm_book(cohort, age)
    df = _sheet(book, "visible1day", "visible")
    h = next(i for i in range(len(df)) if "session" in [norm_name(v) for v in df.iloc[i]])
    labels = [norm_name(v) for v in df.iloc[h]]
    sc = labels.index("session")
    two = labels[sc + 1] == labels[sc + 2] == "vd1"
    tcols = [sc + 1, sc + 2] if two else [sc + 1]
    rows = []
    for b in _trial_blocks(df, cohort):
        g = _geno(b["geno_cell"])
        if g is None:
            continue
        vals = [_num(df.iat[i, c]) for i in b["rows"] for c in tcols]
        vals = [v for v in vals if not math.isnan(v)]
        rows.append({"mouse": b["id"], "genotype": g,
                     "visible_latency_s": float(np.mean(vals)) if vals else np.nan,
                     "n_trials": len(vals), "id_system": _id_system(cohort, age),
                     "notes": "; ".join(b["notes"]) or None})
    return _attach(pd.DataFrame(rows), cohort, _id_system(cohort, age))


# ----------------------------------------------------------------------------- Cohort 2 tables
def _manifest() -> pd.DataFrame:
    """'APA Mouse List.xlsx' sheet 'IPA Manifest' (Mouse #, MWM Blind Code, Name,
    Genotype, Implant, Notes, Blinded Genotype)."""
    m = _sheet(_excel(2, "manifest"), "ipamanifest")
    cols = [str(v).strip() for v in m.iloc[0]]
    m = m.iloc[1:].copy()
    m.columns = cols
    m = m[m["Mouse #"].map(_is_int_like)].copy()
    m["Mouse #"] = m["Mouse #"].astype(int)
    m["MWM Blind Code"] = m["MWM Blind Code"].astype(int)
    return m.reset_index(drop=True)


def blind_letter_map() -> dict:
    """Blinded genotype letter -> 'E3'/'E4', from the manifest's 'Genotype' and
    'Blinded Genotype' columns (must be one-to-one)."""
    m = _manifest()
    pairs = m.groupby("Blinded Genotype")["Genotype"].agg(lambda s: set(map(_geno, s)))
    out = {}
    for letter, gs in pairs.items():
        if len(gs) != 1:
            raise ValueError(f"letter {letter} maps to {gs}")
        out[str(letter).strip()] = gs.pop()
    if len(set(out.values())) != len(out):
        raise ValueError(f"letters not one-to-one: {out}")
    return out


def _simple_table(df: pd.DataFrame, header_row: int, id_label: str) -> pd.DataFrame:
    cols = [str(v).strip() if not (isinstance(v, float) and math.isnan(v)) else f"col{i}"
            for i, v in enumerate(df.iloc[header_row])]
    t = df.iloc[header_row + 1:].copy()
    t.columns = cols
    t = t.loc[:, ~t.columns.duplicated()]  # side blocks repeat labels; keep the first
    return t[t[id_label].map(_is_int_like)].copy()


APA_SESSIONS = {"HAB": ("hab", 0), "T01": ("t1", 1), "T02": ("t2", 2), "T03": ("t3", 3),
                "T04": ("t4", 4), "PROBE": ("probe", 5), "REINSTATEMENT": ("reinstatement", 5)}
APA_SHEETS = {
    "entrances": "ofentrances",
    "shocks": "ofshocks",
    "latency_first_entrance_s": "latencyto1stentrances",
    "path_length_m": "pathlengthm",
    "pct_time_opp": "timeopp",
}


def apa(cohort: int = 2, with_tracking: bool = True) -> pd.DataFrame:
    """Active place avoidance (Cohort 2, 15-20 months), one row per mouse and session.

    Columns: cohort, mouse (Blinded Code = MWM Blind Code), name, genotype, mouse_number
    (ear tag 'Mouse #'), blinded_genotype, session ('hab', 't1'-'t4', 'probe',
    'reinstatement'), day (0 habituation, 1-4 training, 5 probe and reinstatement, which
    are the two 5 min halves of the day-5 trial), entrances, latency_first_entrance_s,
    path_length_m, pct_time_opp, shocks, pseudoshocks_per_entrance (probe rows only),
    dist_per_bout_cm (hab and t1-t4), excluded.

    Sources (all exported from Tracker, Methods "Analysis of Behavioral Data"), file
    'Active Place Avoidance.xlsx', columns HAB, T01-T04, PROBE, REINSTATEMENT of sheets
    '# of Entrances', '# of Shocks', 'Latency to 1st Entrance (s)' (no entrance: the
    session length is given, note in the sheet), 'Path Length (m)' (arena frame; Methods
    "path length relative to the arena"), '% Time - OPP' (stored as a fraction 0-1,
    multiplied by 100 here; a constant factor cannot change a result).  In the probe the
    shock is off, so '# of Shocks' counts pseudoshocks; pseudoshocks_per_entrance is the
    sheet's exported 'Probe - Shocks per Entrance' column of '# of Entrances' (= probe
    shocks / probe entrances, NaN for mice without a probe entrance; the claims exclude
    them).  dist_per_bout_cm (all bouts) and dist_per_bout_walk_cm (non-escape,
    non-avoid bouts; reproduces the Figure S3C U): see :func:`apa_distance_per_bout`.  Genotype: the blinded
    letter of the 'Genotype' sheet mapped with :func:`blind_letter_map`.  Mouse code 5
    is marked 'Excluded' from T03 on (the motor-impaired E4 mouse of the Methods, "excluded
    from APA and hot plate testing"); its HAB-T02 values are kept, ``excluded`` is True
    for all its rows (the paper's n = 13 E4 and t(23) on day 1 exclude it entirely) and
    ``excluded_from`` gives the first session marked.
    """
    if cohort != 2:
        raise ValueError("APA exists for Cohort 2 only")
    book = _excel(2, "apa")
    lm = blind_letter_map()
    gsheet = _simple_table(_sheet(book, "genotype"), 0, "Blinded Code")
    letter = dict(zip(gsheet["Blinded Code"].astype(int), gsheet["Genotype"].str.strip()))
    long = {}
    excluded, excluded_from = set(), {}
    probe_pse = {}
    for metric, sname in APA_SHEETS.items():
        t = _simple_table(_sheet(book, sname), 0, "Blinded Code")
        for _, r in t.iterrows():
            code = int(r["Blinded Code"])
            for col, (sess, day) in APA_SESSIONS.items():
                v = r[col]
                if isinstance(v, str) and "exclud" in v.lower():
                    excluded.add(code)
                    excluded_from[code] = sess
                val = _num(v)
                if metric == "pct_time_opp":
                    val *= 100.0
                long.setdefault((code, sess), {"mouse_number": int(r["Mouse #"])})[metric] = val
            if metric == "entrances":
                pc = next(c for c in t.columns if norm_name(c) == "probeshocksperentrance")
                probe_pse[code] = _num(r[pc])
    rows = []
    for (code, sess), d in long.items():
        day = next(dd for s, dd in APA_SESSIONS.values() if s == sess)
        rows.append({"mouse": code, "genotype": lm.get(letter.get(code)),
                     "mouse_number": d["mouse_number"], "blinded_genotype": letter.get(code),
                     "session": sess, "day": day,
                     **{k: d.get(k, np.nan) for k in APA_SHEETS},
                     "pseudoshocks_per_entrance": probe_pse.get(code, np.nan)
                     if sess == "probe" else np.nan,
                     "excluded": code in excluded,
                     "excluded_from": excluded_from.get(code)})
    out = pd.DataFrame(rows)
    order = {s: i for i, (s, _) in enumerate(APA_SESSIONS.values())}
    out = out.sort_values(["genotype", "mouse", "session"],
                          key=lambda s: s.map(order) if s.name == "session" else s)
    out = out[["mouse", "genotype", "mouse_number", "blinded_genotype", "session", "day",
               "entrances", "latency_first_entrance_s", "path_length_m", "pct_time_opp",
               "shocks", "pseudoshocks_per_entrance", "excluded",
               "excluded_from"]].reset_index(drop=True)
    if with_tracking:
        dpb = apa_distance_per_bout()
        keep = ["dist_per_bout_cm", "n_bouts", "dist_per_bout_walk_cm", "n_bouts_walk"]
        dpb = dpb[dpb["used"]][["mouse", "session"] + keep]
        out = out.merge(dpb, on=["mouse", "session"], how="left")
    return _attach(out, 2, "blind_code")


# Constants of pull_apa_metrics.py (Jones_2019 repository, commit ca056a8).
_FRAMESTEP = 30          # 30 frames/s; 1 s bins
_PIX2CM = 3.122          # Tracker resolution (also %TrackerResolution_PixPerCM in .dat)
_CENTER = 127.5 / _PIX2CM
_SHOCK_BORDER = np.array([0.0, 41.0])
_MOVE_CM_S = 2           # bouts are 1 s steps of >= 2 cm


def _track_xy(df: pd.DataFrame, room: bool) -> np.ndarray:
    """read_tracking() of pull_apa_metrics.py: frames with FrameInfo == 1 (tracking
    error) copy the previous frame; pixels -> cm; room frame centred on the arena."""
    xy = df[["x", "y"]].to_numpy(dtype=float) / _PIX2CM
    bad = df["frameinfo"].to_numpy() == 1
    xy[bad] = np.nan
    xy = pd.DataFrame(xy).ffill().to_numpy()
    if room:
        xy = xy - _CENTER
    return xy


def _dist_to_sz(point) -> float:
    """Shortest distance (cm) from a room-frame point to the line through the shock-zone
    border, as in pull_apa_metrics.py (norm(cross(border, -point)) / norm(border))."""
    p = -np.asarray(point, dtype=float)
    return abs(_SHOCK_BORDER[0] * p[1] - _SHOCK_BORDER[1] * p[0]) / np.linalg.norm(_SHOCK_BORDER)


def _angle_from_shock(v) -> float:
    """angle_from_shock() of pull_apa_metrics.py (0 to -2 pi from the border vector)."""
    v1 = _SHOCK_BORDER
    angle = math.atan2(v1[0] * v[1] - v1[1] * v[0], v1[0] * v[0] + v1[1] * v[1])
    if v[0] < 0:
        angle -= 2 * math.pi
    return angle


def _bouts_travel_away(arena: np.ndarray, room: np.ndarray, level: np.ndarray):
    """Port of the bout loop of pull_apa_metrics.py.  Returns one (escape, avoid,
    delta_dist_to_shock) per bout: delta = distance from the shock zone at bout end minus
    the closest approach over the second before and the first second of the bout;
    escape = shocked in that window (the script tests column 6, CurrentLevel, == 2 of
    the arena file); avoid = came within 60 deg of the border without a shock."""
    n = int(len(arena) / _FRAMESTEP) - 1
    a0 = arena[0:n * _FRAMESTEP:_FRAMESTEP]
    a1 = arena[_FRAMESTEP:(n + 1) * _FRAMESTEP:_FRAMESTEP]
    vel = np.sqrt(((a0 - a1) ** 2).sum(axis=1))
    last_zero = last_nonzero = 0
    dist_to_shock = escape = avoid = None
    out = []
    for i in range(1, len(vel)):
        if vel[i] < _MOVE_CM_S:
            if last_nonzero == i - 1 and i - last_zero > 2:  # just ended a bout
                r = (i - 1) * _FRAMESTEP - 1
                out.append((escape, avoid, _dist_to_sz(room[r]) - dist_to_shock))
            last_zero = i
        elif i == len(vel) - 1:  # last second of trial, still moving
            if dist_to_shock is not None:
                r = i * _FRAMESTEP - 1
                out.append((escape, avoid, _dist_to_sz(room[r]) - dist_to_shock))
        else:
            if last_zero == i - 1:  # new bout
                w = slice((i - 1) * _FRAMESTEP, (i + 1) * _FRAMESTEP - 1)
                escape = int(np.any(level[w] == 2))
                seg = room[w]
                dist_to_shock = min(_dist_to_sz(p) for p in seg)
                ang = min(_angle_from_shock(p) for p in seg)
                avoid = int(ang > -math.radians(60) and escape != 1)
            last_nonzero = i
    return out


def apa_distance_per_bout() -> pd.DataFrame:
    """Distance travelled away from the shock zone per movement bout (cm), from the APA
    tracking files.

    Definition: the paper's "distance traveled relative to the shock zone per movement
    bout" was "extracted using custom Python scripts" (Methods); this is a port of
    pull_apa_metrics.py (github.com/emilyasterjones/Jones_2019, commit ca056a8), output
    column 'Avg Travel Away from SZ (cm)' (the first, all-bouts one): 1 s steps of the
    arena-frame track; a step is movement when it is >= 2 cm; a bout is a run of moving
    seconds of at least 2 s, closed by a still second (or by the trial end); for each
    bout, the distance from the shock zone (perpendicular distance of the room-frame
    position to the shock-zone border line) at the end minus its minimum over the second
    before and the first second of the bout; the metric is the mean over bouts (claims
    method D).  Only that column is ported (escape/avoid classification does not enter
    it).  Habituation and training trials (HAB, T01-T04) are computed; the 'Probe' file
    holds the whole 10 min day-5 trial (probe and reinstatement) and is not used.

    Columns: mouse (blinded code), session, rerun, used, dist_per_bout_cm and n_bouts
    (all bouts: the script's first 'Avg Travel Away from SZ (cm)' column), and the same
    for the script's bout classes: _escape (shocked at bout start), _avoid (came within
    60 deg of the shock zone without a shock), _walk (neither); these are the script's
    2nd, 3rd and 4th 'Avg Travel Away from SZ (cm)' columns.  The paper does not say
    which column was used.  On training day 1 the _walk column gives Mann-Whitney U = 30
    (12 E3, 13 E4; the Figure S3C legend prints U = 30, p = 0.008) and the all-bouts
    column U = 45, so _walk is probably the paper's metric; the direction is E3 > E4 for
    both (the Results say E4 "moved further from the shock zone in bouts").
    Data quirks handled: the room file of mouse 4 HAB is named 'RoomTrac_4_...'; mouse 37
    HAB has an original and a 'Rerun' pair, the rerun is used (``used``) as in the
    spreadsheet's 'Raw Data' sheet, which lists the rerun files.
    """
    if "apa_dpb" in _CACHE:
        return _CACHE["apa_dpb"].copy()
    tracks = _stream(2)["apa_tracks"]
    sess = {"HAB": "hab", "T01": "t1", "T02": "t2", "T03": "t3", "T04": "t4"}
    rows = []
    keys = sorted({(c, t, rr) for (c, t, fr, rr) in tracks if t in sess})
    for code, trial, rerun in keys:
        a = tracks.get((code, trial, "arena", rerun))
        r = tracks.get((code, trial, "room", rerun))
        if a is None or r is None:
            continue
        b = np.array(_bouts_travel_away(_track_xy(a, room=False), _track_xy(r, room=True),
                                        a["level"].to_numpy()), dtype=float).reshape(-1, 3)
        types = {"": np.ones(len(b), bool), "_escape": b[:, 0] == 1,
                 "_avoid": (b[:, 0] != 1) & (b[:, 1] == 1),
                 "_walk": (b[:, 0] != 1) & (b[:, 1] != 1)}
        row = {"mouse": code, "session": sess[trial], "rerun": rerun}
        for t, sel in types.items():
            row[f"dist_per_bout{t}_cm"] = float(b[sel, 2].mean()) if sel.any() else np.nan
            row[f"n_bouts{t}"] = int(sel.sum())
        rows.append(row)
    out = pd.DataFrame(rows)
    has_rerun = set(out.loc[out["rerun"], "mouse"].astype(str) + out.loc[out["rerun"], "session"])
    out["used"] = out["rerun"] | ~(out["mouse"].astype(str) + out["session"]).isin(has_rerun)
    _CACHE["apa_dpb"] = out
    return out.copy()


def open_field() -> pd.DataFrame:
    """Open field (Cohort 2, 14-18 months), one row per mouse.

    Source: 'Open Field.xlsx' sheet 'Summary Data' (Photobeam Activity System counts
    summed over the 30 bins '1 to 30').  Columns: pct_center = 'CenT/TotT' (centre
    movements / total movements, in percent; the paper's "percent time in center"
    (Figure S2A) - the file has beam-break movement counts only, no time, so this ratio
    is the only centre measure), fine_movements = 'TotF', ambulatory_movements = 'TotA',
    total_movements = 'TotT' (Figure S2B "Number of instances of detected movement
    ... fine ... ambulatory ... total"), plus center_* and rears.  mouse = 'Mouse'
    (MWM blind code); genotype from the unlabelled first column.
    """
    t = _simple_table(_sheet(_excel(2, "open_field"), "summarydata"), 1, "Mouse")
    out = pd.DataFrame({
        "mouse": t["Mouse"].astype(int), "genotype": t["col0"].map(_geno),
        "pct_center": t["CenT/TotT"].map(_num),
        "fine_movements": t["TotF"].map(_num), "ambulatory_movements": t["TotA"].map(_num),
        "total_movements": t["TotT"].map(_num), "center_fine": t["CenF"].map(_num),
        "center_ambulatory": t["CenA"].map(_num), "center_total": t["CenT"].map(_num),
        "rears": t["Rear"].map(_num)})
    out = out[out["genotype"].notna()].reset_index(drop=True)
    return _attach(out, 2, "blind_code")


def elevated_plus() -> pd.DataFrame:
    """Elevated plus maze (Cohort 2, 14-18 months), one row per mouse.

    Source: 'Elevated Plus Maze.xlsx' sheet 'Open v closed' (MotorMonitor export).
    mouse = 'Info A' (MWM blind code), genotype = 'Info B'.  pct_time_open =
    'Open:Closed Time' = 100 * open / (open + closed) arm time (exported; Figure S2C
    "Percent time in open arm"); dist_open_in = 'Open Arms<Distance(in)>',
    dist_closed_in = 'Closed Arms<Distance(in)>', dist_total_in = open + closed arms
    (the sheet's unlabelled column; Figure S2D "Distance travelled in elevated plus arms
    ... open arms ... closed arms ... total"); distances in inches as exported.  Also
    time_open_s, time_closed_s, entries_open, entries_closed.
    """
    t = _simple_table(_sheet(_excel(2, "epm"), "openvclosed"), 1, "Info A")
    out = pd.DataFrame({
        "mouse": t["Info A"].astype(int), "genotype": t["Info B"].map(_geno),
        "pct_time_open": t["Open:Closed Time"].map(_num),
        "dist_open_in": t["Open Arms<Distance(in)>"].map(_num),
        "dist_closed_in": t["Closed Arms<Distance(in)>"].map(_num),
        "time_open_s": t["Open Arms<TotTime(sec)>"].map(_num),
        "time_closed_s": t["Closed Arms<TotTime(sec)>"].map(_num),
        "entries_open": t["Open Arms<Entries>"].map(_num),
        "entries_closed": t["Closed Arms<Entries>"].map(_num)})
    out["dist_total_in"] = out["dist_open_in"] + out["dist_closed_in"]
    out = out[out["genotype"].notna()].reset_index(drop=True)
    return _attach(out, 2, "blind_code")


def hot_plate() -> pd.DataFrame:
    """Hot plate (Cohort 2, 15-20 months), one row per mouse.

    Source: 'Hot Plate.xlsx' sheet 'Hot Plate': 'Mouse #' (ear tag), 'Blinded Genotype'
    (A/B, mapped with :func:`blind_letter_map`), 'Latency to Hind Paw Withdrawal' (s,
    live observation, Methods).  mouse = MWM blind code via the manifest's Mouse #.
    ``excluded``: the mouse excluded from APA (Methods: excluded "from APA and hot plate
    testing"), which nevertheless has a hot plate value in the sheet.
    """
    t = _simple_table(_sheet(_excel(2, "hot_plate"), "hotplate"), 2, "Mouse #")
    lm = blind_letter_map()
    m = _manifest()
    code = dict(zip(m["Mouse #"], m["MWM Blind Code"]))
    out = pd.DataFrame({
        "mouse": t["Mouse #"].astype(int).map(code),
        "mouse_number": t["Mouse #"].astype(int),
        "blinded_genotype": t["Blinded Genotype"].str.strip(),
        "latency_s": t["Latency to Hind Paw Withdrawal"].map(_num)})
    out.insert(1, "genotype", out["blinded_genotype"].map(lm))
    a = apa(with_tracking=False)
    out["excluded"] = out["mouse"].isin(set(a.loc[a["excluded"], "mouse"]))
    return _attach(out.reset_index(drop=True), 2, "blind_code")


# ----------------------------------------------------------------------------- linking
def _mwm_ids(cohort, age):
    """(id, genotype, notes) of the mice of an MWM hidden sheet."""
    h = mwm_hidden(cohort, age)
    return h.groupby("mouse", sort=False).agg(genotype=("genotype", "first"),
                                              notes=("notes", "first"),
                                              has_data=("latency_s", lambda s: s.notna().any()))


def _all_set(vals):
    return sorted({v for v in vals if isinstance(v, str) and v})


def link_table() -> pd.DataFrame:
    """Mouse identity table of both cohorts.

    Columns: cohort, ephys_name (spelling of animaldef.m, first recording), ephys_key
    (normalized), ephys_spellings, ephys_ages, genotype_ephys; Cohort 1: mwm_label
    ('1360 (12)'), ear_tag, code, genotype_mwm, mwm_has_data, mwm_notes, age_comment;
    Cohort 2: mouse_number (ear tag), blind_code (MWM Blind Code = APA Blinded Code =
    OF Mouse = EPM Info A = 14-18 month MWM ID), manifest_name, genotype_manifest,
    blinded_letter (manifest), genotype_mwm_14_18, genotype_apa (Genotype sheet letter,
    mapped), genotype_open_field, genotype_epm, genotype_hot_plate (letter, mapped),
    in_mwm_14_18_sheet1 (name listed in the 14-18 month file's 'Sheet1'), mwm_6_9_id
    and genotype_mwm_6_9 (6-9 month MWM, own numbering, not linkable: separate rows),
    in_* membership flags, genotype_disagree, genotype (consensus, if no disagreement).

    Rules: Cohort 1 joins ephys rX_NN_ to the MWM label code '(NN)' (all NN unique).
    Cohort 2 joins ephys names to manifest 'Name' on normalized names, and behavior
    files on blind code / ear tag through the manifest.  Mice with behavior only keep
    ephys_name empty; ephys animals without behavior are kept too.
    """
    if "link" in _CACHE:
        return _CACHE["link"].copy()
    _CACHE["_building_link"] = True
    try:
        out = _build_link_table()
    finally:
        _CACHE.pop("_building_link", None)
    _CACHE["link"] = out
    return out.copy()


def _build_link_table() -> pd.DataFrame:
    # Cohort 1
    e1 = ephys_animals(1)
    m1 = _mwm_ids(1, "13-19mo").reset_index()
    m1["ear_tag"] = [(_code_c1(x))[0] for x in m1["mouse"]]
    m1["code"] = [(_code_c1(x))[1] for x in m1["mouse"]]
    c1 = m1.rename(columns={"mouse": "mwm_label", "genotype": "genotype_mwm",
                            "notes": "mwm_notes", "has_data": "mwm_has_data"}).merge(
        e1.rename(columns={"genotype": "genotype_ephys", "key": "ephys_key",
                           "spellings": "ephys_spellings"}).drop(columns="cohort"),
        on="code", how="outer")
    c1["cohort"] = 1
    c1["ambiguous_code"] = c1.duplicated("code", keep=False)
    c1["ear_tag_shared"] = c1["ear_tag"].notna() & c1.duplicated("ear_tag", keep=False)
    gcols1 = ["genotype_ephys", "genotype_mwm"]
    # Cohort 2
    e2 = ephys_animals(2).rename(columns={"genotype": "genotype_ephys", "key": "ephys_key",
                                          "spellings": "ephys_spellings"}).drop(columns="cohort")
    man = _manifest()
    lm = blind_letter_map()
    mm = pd.DataFrame({"mouse_number": man["Mouse #"], "blind_code": man["MWM Blind Code"],
                       "manifest_name": man["Name"], "genotype_manifest": man["Genotype"].map(_geno),
                       "blinded_letter": man["Blinded Genotype"].str.strip(),
                       "manifest_implant": man["Implant"], "manifest_notes": man["Notes"]})
    mm["ephys_key"] = mm["manifest_name"].map(norm_name).replace("", np.nan)
    c2 = mm.merge(e2, on="ephys_key", how="outer")
    m14 = _mwm_ids(2, "14-18mo")
    apa_t = apa(with_tracking=False).groupby("mouse").first()
    of, ep, hp = open_field().set_index("mouse"), elevated_plus().set_index("mouse"), hot_plate()
    # behavior codes not in the manifest
    extra = (set(m14.index) | set(apa_t.index) | set(of.index) | set(ep.index)) - set(
        c2["blind_code"].dropna().astype(int))
    if extra:
        c2 = pd.concat([c2, pd.DataFrame({"blind_code": sorted(extra)})], ignore_index=True)
    bc = c2["blind_code"]
    c2["genotype_mwm_14_18"] = bc.map(m14["genotype"])
    c2["mwm_14_18_notes"] = bc.map(m14["notes"])
    c2["genotype_apa"] = bc.map(apa_t["genotype"])
    c2["genotype_open_field"] = bc.map(of["genotype"])
    c2["genotype_epm"] = bc.map(ep["genotype"])
    hpn = dict(zip(hp["mouse_number"], hp["genotype"]))
    c2["genotype_hot_plate"] = c2["mouse_number"].map(hpn)
    for col, src in (("in_mwm_14_18", m14.index), ("in_apa", apa_t.index),
                     ("in_open_field", of.index), ("in_epm", ep.index)):
        c2[col] = bc.isin(set(src))
    c2["in_hot_plate"] = c2["mouse_number"].isin(set(hp["mouse_number"]))
    sheet1 = _sheet(_excel(2, "mwm_14-18mo"), "sheet1")
    s1 = {norm_name(v) for v in sheet1.iloc[0] if isinstance(v, str) and v.strip()}
    c2["in_mwm_14_18_sheet1"] = c2["ephys_key"].isin(s1)
    s1_unmatched = s1 - set(c2["ephys_key"].dropna())
    # 6-9 month MWM: own ID numbering, no names anywhere -> separate rows
    m69 = _mwm_ids(2, "6-9mo").reset_index()
    c2b = pd.DataFrame({"mwm_6_9_id": m69["mouse"], "genotype_mwm_6_9": m69["genotype"]})
    c2 = pd.concat([c2, c2b], ignore_index=True)
    c2["cohort"] = 2
    gcols2 = ["genotype_ephys", "genotype_manifest", "genotype_mwm_14_18", "genotype_apa",
              "genotype_open_field", "genotype_epm", "genotype_hot_plate", "genotype_mwm_6_9"]
    out = pd.concat([c1, c2], ignore_index=True)
    gcols = list(dict.fromkeys(gcols1 + gcols2))
    sets = out[gcols].apply(lambda r: _all_set(r.values), axis=1)
    out["genotype_disagree"] = sets.map(len) > 1
    out["genotype"] = sets.map(lambda s: s[0] if len(s) == 1 else None)
    first = ["cohort", "ephys_name", "ephys_key", "genotype", "genotype_disagree"]
    out = out[first + [c for c in out.columns if c not in first]]
    out.attrs["sheet1_names_unmatched"] = sorted(s1_unmatched)
    out.attrs["blind_letter_map"] = lm
    return out


def counts() -> pd.DataFrame:
    """Mice per cohort, data set and genotype (mice with at least one value)."""
    rows = []

    def add(label, df, col):
        d = df[df[col].notna()].drop_duplicates("mouse")
        for g, n in d["genotype"].value_counts().sort_index().items():
            rows.append({"dataset": label, "genotype": g, "n": n})

    add("C1 MWM hidden 13-19mo", mwm_hidden(1), "latency_s")
    add("C2 MWM hidden 6-9mo", mwm_hidden(2, "6-9mo"), "latency_s")
    add("C2 MWM hidden 14-18mo", mwm_hidden(2, "14-18mo"), "latency_s")
    add("C2 open field", open_field(), "pct_center")
    add("C2 EPM", elevated_plus(), "pct_time_open")
    a = apa()
    a = a[~a["excluded"]]
    add("C2 APA t1 (excluded dropped)", a[a["session"] == "t1"], "entrances")
    add("C2 APA t4 (excluded dropped)", a[a["session"] == "t4"], "entrances")
    hp = hot_plate()
    add("C2 hot plate (all rows)", hp, "latency_s")
    add("C2 hot plate (excluded dropped)", hp[~hp["excluded"]], "latency_s")
    return pd.DataFrame(rows).pivot(index="dataset", columns="genotype", values="n")
