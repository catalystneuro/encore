"""Loading and measures for Jarzebowski & Bendor (2026) on DANDI:000713 (Visual Behavior Neuropixels).

Where each parameter comes from:

- Dataset version 0.240702.1725: the version the paper's Methods cite ("Allen Brain Observatory data
  analysis", https://doi.org/10.48324/dandi.000713/0.240702.1725), and the only published one.
- Unit inclusion (D1 of the claims file; Methods, "Unit inclusion"): VISp, isi_violations <= 0.5,
  amplitude_cutoff <= 0.1, presence_ratio >= 0.9, snr > 1, firing rate > 0.2 Hz, quality "good".
- Responsive test (D2; Methods, "Unit inclusion"): spike count in the 250 ms after onset against the
  250 ms before, Wilcoxon paired test, p < 0.05, spikes on >= 20% of presentations. Readings O1.
- Putative pyramidal (D3; Methods, "Identification of pyramidal neurons"): waveform_duration > 0.4 ms,
  rate < 10 Hz, not optotagged (rate in 1 to 10 ms after light onset > 50 Hz and z > 2). Readings O2, O3.
- Windows and bursts (D4; Methods, "Spiking metrics and burst detection"): 250 ms from onset; a burst
  spike is one whose interval to a neighbouring spike in the same window is <= 10 ms.
- Locomotion (D7; Methods, "Locomotion detection"): running when mean speed > 5 cm/s and speed > 3 cm/s
  for 75% of the window; stationary when mean < 5 cm/s and speed < 3 cm/s for 75%. Readings O7.
- Layer (Methods, "Laminar classification", citing Siegle et al. 2021): the unit's peak-channel CCFv3
  coordinate looked up in the Allen CCFv3 2017 annotation volume at 10 um, the resolution Siegle et
  al. (2021) and the AllenSDK use. The voxel index is the coordinate divided by 10 and rounded, a
  standard choice. Structure ids are those of the Allen mouse ontology (VISp1 593, VISp2/3 821, VISp4
  721, VISp5 778, VISp6a 33, VISp6b 305).
- Spontaneous windows: consecutive 250 ms windows over each spontaneous (grey screen) block; which
  block the paper used is open and every reading is computed (see the notebook).
"""
import gzip
import hashlib
import json
import urllib.request

import h5py
import numpy as np
import pandas as pd
import remfile

DANDISET = "000713"
VERSION = "0.240702.1725"
API = f"https://api.dandiarchive.org/api/dandisets/{DANDISET}/versions/{VERSION}"

CCF_URL = ("http://download.alleninstitute.org/informatics-archive/current-release/mouse_ccf/"
           "annotation/ccf_2017/annotation_10.nrrd")
CCF_SHA256 = "a9e9654ef491f0af107dc0a61bd720dabe7f36e8f3e9239532bf3dbdc94ef24c"  # as fetched 2026-11-21
LAYER_IDS = {593: "L1", 821: "L2/3", 721: "L4", 778: "L5", 33: "L6a", 305: "L6b"}

WIN = 0.25        # Methods: "250-ms-long periods"
BURST_ISI = 0.010  # Methods: "inter-spike interval <= 10 ms"
OPTO_WIN = (0.001, 0.010)  # Methods: "1-10 ms window following stimulation onset"


def session_assets():
    """The 153 session files (not the per-probe LFP files nor the behaviour-only training files)."""
    url, out = f"{API}/assets/?page_size=1000", []
    while url:
        d = json.load(urllib.request.urlopen(url))
        out += d["results"]
        url = d["next"]
    ses = [a for a in out if a["path"].endswith(".nwb") and not a["path"].endswith("_image.nwb")
           and not a["path"].endswith("_ecephys.nwb")]
    return sorted(ses, key=lambda a: a["path"]), out


def s3_url(asset_id):
    m = json.load(urllib.request.urlopen(f"{API}/assets/{asset_id}/"))
    return [u for u in m["contentUrl"] if "s3.amazonaws.com" in u][0]


def _counts(spk, starts, win=WIN):
    """Spike count and burst-spike count of one unit in windows [start, start + win).

    Only spikes inside a window count toward its bursts (claims file, O4)."""
    starts = np.asarray(starts)
    order = np.argsort(starts)
    st = starts[order]
    w = np.searchsorted(st, spk, side="right") - 1
    ok = (w >= 0)
    ok[ok] &= spk[ok] < st[w[ok]] + win
    s, w = spk[ok], w[ok]
    n = np.bincount(w, minlength=len(st))
    close = (np.diff(s) <= BURST_ISI) & (np.diff(w) == 0)
    inb = np.zeros(len(s), bool)
    inb[:-1] |= close
    inb[1:] |= close
    nb = np.bincount(w[inb], minlength=len(st))
    out_n, out_b = np.empty_like(n), np.empty_like(nb)
    out_n[order], out_b[order] = n, nb
    return out_n.astype(np.uint16), out_b.astype(np.uint16)


def _running(ts, speed, starts, length):
    """Mean speed and the fractions of samples above and below 3 cm/s in each window."""
    i0 = np.searchsorted(ts, starts)
    i1 = np.searchsorted(ts, np.asarray(starts) + length)
    cs = np.concatenate([[0], np.cumsum(speed)])
    ca = np.concatenate([[0], np.cumsum(speed > 3)])
    cb = np.concatenate([[0], np.cumsum(speed < 3)])
    n = np.maximum(i1 - i0, 1)
    mean = (cs[i1] - cs[i0]) / n
    above = (ca[i1] - ca[i0]) / n
    below = (cb[i1] - cb[i0]) / n
    mean[i1 == i0] = np.nan
    return mean, above, below


def run_state(mean, above, below):
    """'run', 'stat' or '' (neither), Methods, 'Locomotion detection'."""
    st = np.full(len(mean), "", dtype=object)
    st[(mean > 5) & (above >= 0.75)] = "run"
    st[(mean < 5) & (below >= 0.75)] = "stat"
    return st


def _table(g, cols):
    return pd.DataFrame({c: g[c][:] for c in cols})


def extract_session(asset):
    """Stream one session and reduce it to per-window spike counts of its VISp units.

    Returns a dict with the session's units (metrics, CCF coordinates), its active-task and passive
    image presentations, spontaneous windows and optotagging pulses, and for each unit and window the
    spike count, burst-spike count, and (for presentations) the count in the 250 ms before."""
    f = h5py.File(remfile.File(s3_url(asset["asset_id"])), "r")
    out = {"path": asset["path"], "session": asset["path"].split("/")[-1].split("_")[1][4:],
           "subject": asset["path"].split("/")[0][4:],
           "genotype": f["general/subject/genotype"][()].decode(),
           "description": f["session_description"][()].decode()}
    e = f["general/extracellular_ephys/electrodes"]
    el = _table(e, ["id", "x", "y", "z", "probe_vertical_position"])
    el["location"] = e["location"][:].astype(str)
    u = f["units"]
    cols = ["id", "peak_channel_id", "isi_violations", "amplitude_cutoff", "presence_ratio", "snr",
            "firing_rate", "waveform_duration"]
    units = _table(u, cols)
    units["quality"] = u["quality"][:].astype(str)
    units = units.merge(el.rename(columns={"id": "peak_channel_id"}), on="peak_channel_id", how="left")
    out["n_units_file"] = len(units)
    out["n_visp_units_file"] = int((units.location == "VISp").sum())
    keep = np.where((units.location == "VISp") & (units.quality == "good") & (units.isi_violations <= 0.5)
                    & (units.amplitude_cutoff <= 0.1) & (units.presence_ratio >= 0.9) & (units.snr > 1))[0]
    units = units.iloc[keep].reset_index(drop=True)
    units["row"] = keep

    # stimulus tables
    ni_name = [k for k in f["intervals"] if k.startswith("Natural_Images")][0]
    out["image_set"] = ni_name
    ni = f["intervals"][ni_name]
    pres = _table(ni, ["start_time", "active", "stimulus_block", "flashes_since_change", "is_change",
                       "omitted", "is_image_novel", "is_sham_change"])
    pres["image_name"] = ni["image_name"][:].astype(str)
    spont = _table(f["intervals/spontaneous_presentations"], ["start_time", "stop_time", "stimulus_block"])
    out["spont_blocks"] = spont
    out["active_span"] = (pres.start_time[pres.active].min(), pres.start_time[pres.active].max() + 0.75)
    # spontaneous windows: consecutive 250 ms windows inside each spontaneous block
    sw = []
    for _, r in spont.iterrows():
        t = np.arange(r.start_time, r.stop_time - WIN + 1e-9, WIN)
        sw.append(pd.DataFrame({"start_time": t, "stimulus_block": int(r.stimulus_block)}))
    sw = pd.concat(sw, ignore_index=True)
    opto = _table(f["processing/optotagging/optogenetic_stimulation"], ["start_time", "duration", "level"])
    opto["name"] = f["processing/optotagging/optogenetic_stimulation/stimulus_name"][:].astype(str)

    rs = f["processing/running/speed"]
    ts, sp = rs["timestamps"][:], rs["data"][:]
    out["speed_unit"] = rs["data"].attrs.get("unit")
    out["speed_range"] = (float(np.nanmin(sp)), float(np.nanmax(sp)))
    for nm, d in [("pres", pres), ("spontw", sw)]:
        for L, tag in [(WIN, "250"), (0.75, "750")]:
            m, a, b = _running(ts, sp, d.start_time.values, L)
            d["speed_" + tag] = m
            d["state_" + tag] = run_state(m, a, b)
    out["pres"], out["spontw"], out["opto"] = pres, sw, opto

    # spikes of the kept units, read as one range of the ragged array
    idx = u["spike_times_index"]
    out["n_spikes_file"] = int(idx[-1])
    out["first_spikes"] = u["spike_times"][:5]
    rows = units.row.values
    n = len(rows)
    P, S, O = len(pres), len(sw), len(opto)
    early = np.zeros((n, P), np.uint16); early_pre = np.zeros((n, P), np.uint16)
    cnt = np.zeros((n, P), np.uint16); bst = np.zeros((n, P), np.uint16); pre = np.zeros((n, P), np.uint16)
    scnt = np.zeros((n, S), np.uint16); sbst = np.zeros((n, S), np.uint16)
    oresp = np.zeros((n, O), np.uint16); obase = np.zeros((n, O), np.uint16)
    oblock_rate = np.zeros(n); active_rate = np.zeros(n)
    if n:
        lo = int(idx[rows.min() - 1]) if rows.min() > 0 else 0
        ends = idx[rows.min():rows.max() + 1]
        allspk = u["spike_times"][lo:int(ends[-1])]
        a0, a1 = out["active_span"]
        o0, o1 = opto.start_time.min(), opto.start_time.max() + 1.5
        for i, r in enumerate(rows):
            b0 = (int(idx[r - 1]) if r > 0 else 0) - lo
            b1 = int(idx[r]) - lo
            s = np.sort(allspk[b0:b1])
            cnt[i], bst[i] = _counts(s, pres.start_time.values)
            pre[i], _ = _counts(s, pres.start_time.values - WIN)
            # 30 to 100 ms after onset and the 70 ms before it, for the clock check only
            early[i], _ = _counts(s, pres.start_time.values + 0.03, 0.07)
            early_pre[i], _ = _counts(s, pres.start_time.values - 0.07, 0.07)
            scnt[i], sbst[i] = _counts(s, sw.start_time.values)
            oresp[i], _ = _counts(s, opto.start_time.values + OPTO_WIN[0], OPTO_WIN[1] - OPTO_WIN[0])
            obase[i], _ = _counts(s, opto.start_time.values - (OPTO_WIN[1] - OPTO_WIN[0]),
                                  OPTO_WIN[1] - OPTO_WIN[0])
            # optotagging block rate, outside 0 to 1.1 s after each pulse onset (reading O3 b)
            ins = s[(s >= o0) & (s < o1)]
            k = np.searchsorted(opto.start_time.values, ins, side="right") - 1
            free = (k < 0) | (ins - opto.start_time.values[np.maximum(k, 0)] > 1.1)
            tfree = (o1 - o0) - 1.1 * O
            oblock_rate[i] = free.sum() / max(tfree, 1e-9)
            active_rate[i] = ((s >= a0) & (s < a1)).sum() / (a1 - a0)
        del allspk
    units["active_rate"] = active_rate
    units["opto_block_rate"] = oblock_rate
    out.update(units=units, cnt=cnt, bst=bst, pre=pre, early=early, early_pre=early_pre, scnt=scnt, sbst=sbst, oresp=oresp, obase=obase)
    f.close()
    return out


def load_all(workers=4):
    """Extract every session, `workers` at a time (each holds one session's spikes in memory)."""
    from concurrent.futures import ProcessPoolExecutor
    ses, assets = session_assets()
    with ProcessPoolExecutor(workers) as ex:
        res = list(ex.map(extract_session, ses))
    return res, assets


def ccf_lookup(points_um):
    """Annotation ids of the CCFv3 2017 10 um volume at the given (AP, DV, ML) points, in um.

    The gzip-encoded volume is streamed and decompressed in memory; only the voxels needed are kept.
    Returns the ids and the SHA-256 of the file as fetched."""
    pts = np.asarray(points_um, float)
    ijk = np.round(pts / 10.0).astype(np.int64)
    resp = urllib.request.urlopen(CCF_URL)
    sha = hashlib.sha256()
    head = b""
    while b"\n\n" not in head:
        c = resp.read(4096)
        sha.update(c)
        head += c
    hdr, rest = head.split(b"\n\n", 1)
    fields = dict(l.split(": ", 1) for l in hdr.decode().splitlines()[1:] if ": " in l)
    sizes = [int(v) for v in fields["sizes"].split()]
    assert fields["type"] in ("unsigned int", "uint32") and fields["encoding"] == "gzip", fields
    # nrrd stores the first axis fastest (AP, then DV, then ML)
    flat = ijk[:, 0] + sizes[0] * (ijk[:, 1] + sizes[1] * ijk[:, 2])
    order = np.argsort(flat)
    want = flat[order]
    ids = np.zeros(len(flat), np.int64)
    dec = __import__("zlib").decompressobj(16 + 15)
    pos, j = 0, 0  # pos in voxels decoded so far
    buf = b""

    def feed(raw):
        nonlocal pos, j, buf
        buf += dec.decompress(raw)
        nvox = len(buf) // 4
        if nvox == 0:
            return
        arr = np.frombuffer(buf[:nvox * 4], "<u4")
        k = np.searchsorted(want, pos + nvox, side="left")
        sel = want[j:k] - pos
        ids[order[j:k]] = arr[sel]
        j = k
        pos += nvox
        buf = buf[nvox * 4:]

    feed(rest)
    while True:
        c = resp.read(1 << 22)
        if not c:
            break
        sha.update(c)
        feed(c)
    assert pos == sizes[0] * sizes[1] * sizes[2], (pos, sizes)
    return ids, sha.hexdigest(), sizes


# ---------------------------------------------------------------------------------------------
# Cell selection

def opto_tagged(r, reading):
    """Optotagged units of one session (claims file D3 and O3; Methods, 'Identification of
    pyramidal neurons'): rate in the 1 to 10 ms after light onset above 50 Hz and z-score above 2
    against baseline, over all light pulses. Only Vip-Cre and Sst-Cre mice carry ChR2.

    Reading 'a': baseline is the count in the 9 ms before each pulse; z = (mean response - mean
    baseline) / sd of baseline, over pulses. Reading 'b': baseline is the rate over the optotagging
    block outside 1.1 s after each onset; its sd is that of a Poisson count in 9 ms at that rate."""
    n = len(r["units"])
    if "Ai32" not in r["genotype"] or n == 0:
        return np.zeros(n, bool)
    L = OPTO_WIN[1] - OPTO_WIN[0]
    resp = r["oresp"].mean(1) / L
    if reading == "a":
        mb = r["obase"].mean(1) / L
        sd = r["obase"].std(1) / L
    else:
        mb = r["units"]["opto_block_rate"].values
        sd = np.sqrt(mb * L) / L
    with np.errstate(divide="ignore", invalid="ignore"):
        z = np.where(sd > 0, (resp - mb) / sd, np.where(resp > mb, np.inf, 0))
    return (resp > 50) & (z > 2)


def responsive(r, sided, which):
    """Responsive units of one session (D2, O1). sided 'a' one-sided, 'b' two-sided with higher
    mean during; which 'a' active-task image presentations, 'b' those of the whole session."""
    from scipy.stats import wilcoxon
    p = r["pres"]
    m = (p.omitted.values != 1) & (p.active.values if which == "a" else True)
    out = np.zeros(len(r["units"]), bool)
    for i in range(len(r["units"])):
        a, b = r["cnt"][i, m].astype(float), r["pre"][i, m].astype(float)
        if (a > 0).mean() < 0.2 or np.all(a == b):
            continue
        if sided == "a":
            pv = wilcoxon(a, b, alternative="greater").pvalue
            out[i] = pv < 0.05
        else:
            pv = wilcoxon(a, b).pvalue
            out[i] = (pv < 0.05) and a.mean() > b.mean()
    return out


def select_cells(res, layer_of, o1="aa", o2="a", o3="a", responsive_only=True, sessions=None):
    """Putative pyramidal, image-responsive L2/3 and L5 units (D1 to D3) under readings O1 (two
    letters: sidedness, presentations), O2 (firing rate) and O3 (optotagging baseline).

    layer_of maps unit id to its CCF layer label. responsive_only=False skips the responsive test
    (D2), giving all putative pyramidal L2/3 and L5 units. sessions, when given, is the set of
    session indices to use. Returns one row per selected cell."""
    rows = []
    for si, r in enumerate(res):
        u = r["units"]
        if len(u) == 0 or (sessions is not None and si not in sessions):
            continue
        fr = u.firing_rate.values if o2 == "a" else u.active_rate.values
        lay = u.id.map(layer_of).values
        ok = (fr > 0.2) & (fr < 10) & (u.waveform_duration.values > 0.4) & ~opto_tagged(r, o3)
        ok &= np.isin(lay, ["L2/3", "L5"])
        if not ok.any():
            continue
        resp = np.zeros(len(u), bool)
        idx = np.where(ok)[0]
        sub = dict(r, units=u.iloc[idx], cnt=r["cnt"][idx], pre=r["pre"][idx])
        resp[idx] = responsive(sub, o1[0], o1[1]) if responsive_only else True
        for i in np.where(ok & resp)[0]:
            rows.append(dict(sess=si, session=r["session"], subject=r["subject"], unit=i,
                             unit_id=u.id.values[i], layer=lay[i]))
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------------------------
# Presentations and per-cell measures

def annotate(r):
    """Active-task presentations with the labels the claims use.

    rep: repetition ordinal, flashes_since_change + 1, for image presentations of blocks that begin
    with an image change (Figure 5B legend: Repetition 1 follows an image change); omissions do not
    advance it in the dataset. post_om / pre_om: the presentation right after / before an omission.
    img_block: for Repetition 1, how many blocks of that image the session has shown so far
    (Methods, 'Allen Brain Observatory data analysis', novelty)."""
    p = r["pres"].copy()
    p["i"] = np.arange(len(p))
    a = p[p.active].copy()
    om = a.omitted.values == 1
    a["post_om"] = np.r_[False, om[:-1]] & ~om
    a["pre_om"] = np.r_[om[1:], False] & ~om
    blk = np.cumsum(a.is_change.values == 1)
    a["block"] = blk
    a["rep"] = np.where((blk > 0) & ~om, a.flashes_since_change.values + 1, 0)
    first = a[(a.rep == 1)]
    nth = first.groupby("image_name").cumcount() + 1
    a["img_block"] = 0
    a.loc[first.index, "img_block"] = nth.values
    a["novel_session"] = bool((a.is_image_novel == 1).any())
    return a


def fsb(n, b, mode):
    """Fraction of spikes in bursts over a set of windows (D4, O4). 'a': burst spikes summed over
    windows / all spikes; 'b': mean over windows with spikes of the per-window fraction. A cell
    with no spikes in the windows gets 0 (claims file, fig6c criterion); with no windows, NaN."""
    n = np.asarray(n, float); b = np.asarray(b, float)
    if len(n) == 0:
        return np.nan
    if mode == "a":
        return b.sum() / n.sum() if n.sum() > 0 else 0.0
    k = n > 0
    return float(np.mean(b[k] / n[k])) if k.any() else 0.0


def rate(n):
    n = np.asarray(n, float)
    return n.mean() / WIN if len(n) else np.nan


def mod_index(x, ctrl):
    """(x - ctrl) / (x + ctrl), Methods, 'Spiking metrics'; NaN when both are 0."""
    x, ctrl = np.asarray(x, float), np.asarray(ctrl, float)
    with np.errstate(invalid="ignore", divide="ignore"):
        return np.where(x + ctrl > 0, (x - ctrl) / (x + ctrl), np.nan)


def mixed(df, formula="y ~ 1", group="session"):
    """Mixed-effects model with a random intercept of session (D8). t from the coefficient and its
    standard error; df = observations - fixed effects, p and 95% CI from the t distribution
    (Methods, 'Quantification and statistical analysis'). Returns a table of fixed effects."""
    import warnings
    import statsmodels.formula.api as smf
    from scipy import stats
    df = df.dropna(subset=["y"])
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        m = smf.mixedlm(formula, df, groups=df[group]).fit()
    fe = m.fe_params
    se = m.bse_fe
    dof = len(df) - len(fe)
    t = fe / se
    tc = stats.t.ppf(0.975, dof)
    out = pd.DataFrame({"coef": fe, "t": t, "df": dof, "p": 2 * stats.t.sf(np.abs(t), dof),
                        "ci_low": fe - tc * se, "ci_high": fe + tc * se})
    out["n"] = len(df)
    out["groups"] = df[group].nunique()
    out["converged"] = m.converged
    return out


def noise_residuals(r, a, cells_s, cond, fsb_mode):
    """Trial-by-trial population residuals of one session (D9; Methods, 'Spiking metrics' and
    'Unit inclusion'). cells_s: the session's cells (rows of select_cells). cond 'rep1' for
    Repetition 1 presentations, 'post' for presentations right after an omission. Each cell's mean
    response to that image at that repetition ordinal is subtracted from its trial value, and the
    residuals are averaged over the cells of a layer. L5 FSB uses only trials with spikes: reading
    'a' leaves cells without spikes on the trial out of the mean; 'b' gives them FSB 0 and leaves out
    trials on which no L5 cell spiked."""
    t = a[(a.rep == 1) if cond == "rep1" else (a.post_om & (a.rep > 0))]
    ix = t.i.values
    key = t.image_name.values + "_" + t.rep.astype(str).values
    out = pd.DataFrame({"trial": ix})
    for lay in ["L2/3", "L5"]:
        u = cells_s[cells_s.layer == lay].unit.values
        n = r["cnt"][u][:, ix].astype(float)
        b = r["bst"][u][:, ix].astype(float)
        fr = n / WIN
        res_fr = fr - pd.DataFrame(fr.T).groupby(key).transform("mean").values.T
        out[lay + "_fr"] = res_fr.mean(0)
        if lay == "L5":
            with np.errstate(invalid="ignore", divide="ignore"):
                f = np.where(n > 0, b / n, np.nan if fsb_mode == "a" else 0.0)
            m = pd.DataFrame(f.T).groupby(key).transform("mean").values.T
            res_f = f - m
            if fsb_mode == "a":
                out["L5_fsb"] = np.nanmean(np.where(np.isnan(res_f), np.nan, res_f), 0) \
                    if np.isfinite(res_f).any() else np.nan
            else:
                v = res_f.mean(0)
                v[(n > 0).sum(0) == 0] = np.nan
                out["L5_fsb"] = v
    return out
