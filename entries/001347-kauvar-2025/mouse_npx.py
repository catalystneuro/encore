"""Mouse Neuropixels analyses (Figs. 4G, 4H, 4I, 5D, 5E, 5G to 5I, 6D, 6F, 6H, 6J, fig. S34) for Kauvar, Richman, Liu
et al. 2025 on DANDI:001326 (version 0.250528.1957), streamed through dandi_io.

Each function follows the paper's Methods (sections cited below) and, where the Methods leave a
detail open, the mouse analysis code, Zenodo record 14876694, analysis.py (md5
6cc7aa5059737c3bd753aad1f116019d; cited as "code" with the function name). The code is not
imported; what is needed is reimplemented here.

Parameters and where they come from
- BIN = 0.01 s, causal moving average over 5 bins (50 ms): Methods, "Neuropixels recording and
  processing" ("binned at 10 ms resolution and smoothed with a causal moving average filter over
  50 ms"); the brainwide-npix firing_rates_over_recording (rates in spikes/s) and its
  moving_avg_filter (first 4 bins left unsmoothed).
- Z-scored rates: the code works on "all_zfr" (session z-scored rates); the driver that makes it
  is not in the record. Assumption: each unit's smoothed rate is z-scored over the whole recording
  (0 to its last spike time). A projection that is itself z-scored (Figs. 6D, 6F, S34) does not
  depend on this.
- Puff window -1 s to +2 s around each puff (300 bins), the window index of a puff being the first
  bin starting at or after it (code, get_windowed_puff_psth: searchsorted(bins, t) - 100).
- Ketamine start: 30 s after the last puff of series 20 (code, get_windowed_puff_psth). In all 13
  files the 'Ketamine infusion start' timestamp falls between series 20 and 21.
- Units: all units in the files are labelled 'good' and have SNR > 2 and > 500 spikes, the
  Methods' criteria; the ISI criterion cannot be checked (no ISI metric in the files).
- Puff-modulated cells (Methods, "Significant modulation"; code, selective): paired t-tests over
  the 160 preinfusion puffs, p <= 0.01 (code; the Methods say "less than 0.01"), in any of: 1 s
  before vs 0 to 200 ms, vs 300 to 800 ms, vs 1 to 2 s after the puff; across the 20 series, 1 s
  before the first vs before the last puff, 1 s after the first vs after the last puff. Plus the
  code's has_min_spikes (summed rate over the preinfusion puffs > 250, i.e. more than 2.5 spikes).
- Coding dimension weights (Methods, "Coding dimension, mouse peri-puff"): mean difference
  between target and reference windows over trials, divided by sqrt(var_target + var_reference).
  Methods reading 'M': per-neuron variances over trials. Code reading 'C' (compute_cd_cov): the
  variance of the whole cells-by-trials matrix (pooled scalar). The scale (unit or L1 norm) does
  not change a z-scored projection.
- Epochs (Methods, "Comparison of rates"): Pre trials 1 to 20, Ketamine 22 to 32, Post 34 to 40
  ('M'); the code's slices are Ketamine 23 to 32, Post 35 to 40 ('C'; Table S3 gives 20, 10, 6
  trials). Tone epochs (code, plot_coding_dimension_early_late with stimulus 'tone'; Table S3,
  fig. S34: 10, 5, 3 trials): the first 10 tone series before ketamine start, tone series 2 to 6
  after it, and tone series 8 to 10 after it.
- Projections for Figs. 6D/6F/S34 (code, plot_coding_dimension_early_late): the trial-averaged
  projection is z-scored over its 3-s window and the mean of the 1 s before the stimulus is
  subtracted. Persistent puff projection uses the first puff of each series only (code, limit=1;
  the Methods do not say) with the all-puff average as a variant; fast and tone projections average
  all 8 stimuli (code).
- Windows (Methods): persistent puff dimension built on 0.5 to 1 s, quantified 1 to 2 s; fast
  0 to 70 ms (reference: Methods "1 s before each puff"; code 70 ms before, variant); tone
  persistent built on 150 to 350 ms, quantified 350 to 500 ms (Methods; the code's tone
  quantification bins 135:150 are 350 to 500 ms).
- Emotion-like dimension (Methods, "Emotion-like neural dimension"; code get_affective_projections,
  plot_affective_firstpuff_persist): target 1 s starting 5 s after the last puff onset of each
  preinfusion series (Methods) against 750 ms ending 250 ms before the first puff; fast dimension
  0 to 200 ms after against 200 ms before puffs 5 to 8 (the claims file's reading of "last 4
  trials"); QR orthogonalisation, sign set so that puff 8 exceeds puff 1 (code). Code variant:
  target 3 to 4 s after the last puff onset (inferred from bins 400:500 of a window that, from the
  plotting code, starts 1 s before the last puff) with pooled variance.
- Intrinsic timescale (Methods, "Intrinsic timescale analysis, mouse"; code extract_timescale):
  30 s before each series projected on the persistent dimension; autocorrelation
  (scipy.signal.correlate), normalised to its maximum over the fitted lags, a*exp(-x/b)+c fitted
  over 2.5 s with p0 = (1, 0.2, 0) (code stimulus_timescales uses t0=0.2), maxfev 2000 (code).
  Methods: fit from the peak (lag 0); code: from lag one bin. Series: code pre 11 to 20 and
  ketamine 23 to 32 (Table S3: 10 and 10), tone pre 1 to 10 and ketamine tone series 2 to 6
  (Table S3: 10 and 5).
- Coupling (Methods, "Baseline population coupling, mouse"): Pearson correlation over the
  concatenated 30-s windows before the series of an epoch, among cells with |w| above the 90th
  percentile of |w|, averaged. Code variant: signed w above that percentile and the median of
  |r|; code series pre 1 to 10 and ketamine 23 to 32.
- Clustering, regional rise and decay, the model and the behavioural dose fits: see the comments
  above cluster_cells, region_rise_decay, model_system and dose_trace. Standard choices that
  cannot change a result: Scanpy random_state 0 and numpy seed 42 (the code's), bootstrap seed 0.
"""
import re

import numpy as np
import pandas as pd
import scipy.signal
import scipy.stats
from scipy.optimize import curve_fit

import dandi_io

BIN = 0.01
SMOOTH = 5
PRE_S = 1.0          # puff window starts 1 s before the puff
WIN = 300            # puff window length in bins (3 s)
POST_WIN = 5000      # post-series window, from 1 s before the last puff onset, 50 s
BASE_WIN = 3000      # 30 s before a series
N_PUFF_SERIES = 40   # series 1..40 are analysed (every file has at least 40)

# Epochs as 0-based series indices
PUFF_EPOCHS = {
    'pre': np.arange(0, 20),
    'ket_M': np.arange(21, 32), 'ket_C': np.arange(22, 32),
    'post_M': np.arange(33, 40), 'post_C': np.arange(34, 40),
}


def npx_paths():
    return sorted(dandi_io.list_assets(dandi_io.NPX_DANDISET, dandi_io.NPX_VERSION))


def _series(times, n=8):
    times = np.sort(times)
    assert len(times) % n == 0
    s = times.reshape(-1, n)
    return s


def read_session(path):
    """Read metadata, stimulus times and spike times of one session."""
    f = dandi_io.open_h5(path, dandi_io.NPX_DANDISET, dandi_io.NPX_VERSION)
    st = f['intervals/Stimulus presentations/stimulus'][:].astype(str)
    t0 = f['intervals/Stimulus presentations/start_time'][:]
    t1 = f['intervals/Stimulus presentations/stop_time'][:]
    spk = f['units/spike_times'][:]
    idx = f['units/spike_times_index'][:]
    out = dict(
        path=path,
        subject=f['general/subject/subject_id'][()].decode(),
        session=path.split('_ses-')[1].split('_')[0],
        n_probes=len(f['general/devices']),
        ket_time=float(f['acquisition/Ketamine infusion start/timestamps'][0]),
        region=f['units/brain_region'][:].astype(str),
        quality=f['units/quality'][:].astype(str),
        snr=f['units/snr'][:], n_spikes=f['units/n_spikes'][:],
        stim=st, stim_start=t0, stim_stop=t1,
        spikes=np.split(spk, idx[:-1]),
    )
    out['puff'] = _series(t0[st == 'puff'])
    out['tone'] = _series(t0[st == 'tone']) if np.any(st == 'tone') else None
    out['light'] = _series(t0[st == 'light']) if np.any(st == 'light') else None
    f.close()
    return out


def smoothed_rate(spikes, nbins):
    """Binned rate (spikes/s, 10 ms bins) with a causal 5-bin moving average (brainwide-npix)."""
    c = np.bincount(np.minimum((spikes / BIN).astype(np.int64), nbins - 1), minlength=nbins)
    fr = c.astype(np.float64) / BIN
    cs = np.cumsum(np.r_[0.0, fr])
    sm = fr.copy()
    sm[SMOOTH - 1:] = (cs[SMOOTH:] - cs[:-SMOOTH]) / SMOOTH
    return sm, c


def _windows(starts, length):
    return starts[..., None] + np.arange(length)


def selective(rates):
    """Code 'selective': rates (n_series=20, 8, 300) of one cell -> bool (p <= 0.01 in any test)."""
    r = rates
    pre = r[:, :, :100].reshape(-1, 100).mean(-1)
    ref = r[:, :, 100:120].reshape(-1, 20).mean(-1)
    aff = r[:, :, 130:180].reshape(-1, 50).mean(-1)
    lng = r[:, :, 200:300].reshape(-1, 100).mean(-1)
    eb = r[:, 0, :100].mean(-1); lb = r[:, -1, :100].mean(-1)
    er = r[:, 0, 100:200].mean(-1); lr = r[:, -1, 100:200].mean(-1)
    ps = []
    for a, b in ((pre, ref), (pre, aff), (pre, lng), (eb, lb), (er, lr)):
        p = scipy.stats.ttest_rel(a, b).pvalue
        ps.append(p)
    ps = np.array(ps)
    return bool(np.any(ps <= 0.01)), ps


def cd_weights(x, y, var='M'):
    """Coding dimension from x, y (cells, trials): Methods 'M' per-neuron variance; code 'C' pooled."""
    d = x.mean(1) - y.mean(1)
    if var == 'M':
        den = np.sqrt(x.var(1) + y.var(1))
        den[den == 0] = np.inf
        v = d / den
    else:
        v = d / np.sqrt(np.var(x) + np.var(y))
    return v / np.sum(np.abs(v))


def my_qr(mat):
    """Code my_qr: QR with the code's sign correction."""
    q, r = np.linalg.qr(mat)
    for i in range(1, r.shape[0]):
        if np.any(r[i, :] < 0):
            q[:, i] = -q[:, i]
    return q, r


def process_session(path, verbose=False):
    """Stream one session and reduce it to what the claims need.

    Returns a dict with metadata, the puff-modulated cell mask, per-series window means for
    building coding dimensions, epoch-averaged traces, and the projections and coupling values
    that need the full-length rates (30-s baseline windows), for puff and tone.
    """
    S = read_session(path)
    puff = S['puff']
    n_units = len(S['spikes'])
    t_end = max(s.max() for s in S['spikes'] if len(s)) + 1.0
    nbins = int(np.ceil(t_end / BIN))
    bins = np.arange(nbins) * BIN
    ket_start = puff[19, -1] + 30.0
    assert puff.shape[0] >= N_PUFF_SERIES
    # window start indices
    sta_puff = np.searchsorted(bins, puff[:N_PUFF_SERIES]) - int(PRE_S / BIN)      # (40, 8)
    sta_post = np.searchsorted(bins, puff[:N_PUFF_SERIES, -1]) - int(PRE_S / BIN)  # (40,)
    sta_base = np.searchsorted(bins, puff[:N_PUFF_SERIES, 0]) - BASE_WIN           # (40,)
    pre_span = (sta_puff[0, 0], sta_puff[20, 0] + 3)  # code has_min_spikes: sta[0]:sta[160]+3

    has_tone = S['tone'] is not None
    if has_tone:
        tone = S['tone']
        # 'code': split at the code's ketamine start (30 s after the last puff of series 20);
        # 'inj': split at the file's 'Ketamine infusion start' timestamp. Pre: up to 10 tone
        # series before the split; Ketamine: tone series 2 to 6 after it; Post: 8 to 10 after it.
        tsets = {}
        for name, split in (('code', ket_start), ('inj', S['ket_time'])):
            t_pre = np.where(tone[:, 0] < split)[0][-10:]
            t_post = np.where(tone[:, 0] > split)[0]
            tsets[name] = {'pre': t_pre, 'ket': t_post[1:6], 'post': t_post[7:10]}
        tone_use = np.unique(np.concatenate([v for d in tsets.values() for v in d.values()]))
        sta_tone = np.searchsorted(bins, tone[tone_use]) - int(PRE_S / BIN)
        sta_tbase = np.searchsorted(bins, tone[tone_use, 0]) - BASE_WIN
        S['tone_sets'] = {n: {k: np.searchsorted(tone_use, v) for k, v in d.items()}
                          for n, d in tsets.items()}
        S['tone_series_used'] = tone_use

    idx_puff = _windows(sta_puff, WIN)            # (40, 8, 300)
    idx_post = _windows(sta_post, POST_WIN)       # (40, 5000)
    idx_base = _windows(sta_base, BASE_WIN)       # (40, 3000)
    if has_tone:
        idx_tone = _windows(sta_tone, WIN)
        idx_tbase = _windows(sta_tbase, BASE_WIN)

    sel = np.zeros(n_units, bool); minspk = np.zeros(n_units, bool)
    pvals = np.zeros((n_units, 5))
    P, POST, T, BASE_ALL, TBASE_ALL, PALL = [], [], [], [], [], []
    rates_mean = np.zeros(n_units); rates_sd = np.zeros(n_units)
    sorted_ok = np.zeros(n_units, bool)
    for u, sp in enumerate(S['spikes']):
        sorted_ok[u] = np.all(np.diff(sp) >= 0)
        sm, c = smoothed_rate(np.sort(sp), nbins)
        rates_mean[u] = sm.mean(); rates_sd[u] = sm.std()
        z = ((sm - rates_mean[u]) / rates_sd[u]).astype(np.float32)
        minspk[u] = c[pre_span[0]:pre_span[1]].sum() > 2.5   # code: summed rate (Hz) > 250
        pw = z[idx_puff]
        PALL.append(pw[:20].mean(axis=(0, 1)))
        s, p = selective(pw[:20].astype(np.float64))
        pvals[u] = p
        sel[u] = s and minspk[u]
        BASE_ALL.append(z[idx_base])
        if has_tone:
            TBASE_ALL.append(z[idx_tbase])
        if sel[u]:
            P.append(pw)
            POST.append(z[idx_post[:32]])
            if has_tone:
                T.append(z[idx_tone])
    P = np.stack(P)            # (n_sel, 40, 8, 300)
    POST = np.stack(POST)      # (n_sel, 32, 5000)
    BASE_ALL = np.stack(BASE_ALL)  # (n_units, 40, 3000)
    out = {k: S[k] for k in ('path', 'subject', 'session', 'n_probes', 'ket_time', 'region',
                             'quality', 'snr', 'n_spikes')}
    out.update(puff=puff, tone=S['tone'], light=S['light'], ket_start=ket_start, n_units=n_units,
               sel=sel, minspk=minspk, pvals=pvals, n_sel=int(sel.sum()), t_end=t_end,
               spikes_sorted=sorted_ok, rate_mean=rates_mean, rate_sd=rates_sd)

    # clock check: mean preinfusion puff-window z-rate of all units and of the modulated cells
    out['pop_trace_all'] = np.mean(PALL, axis=0)
    out['pop_trace_sel'] = P[:, :20].mean(axis=(0, 1, 2))
    # ---- puff: per-series window means of the preinfusion series (cells, 20, 8)
    pre = P[:, :20]
    wm = lambda a, b: pre[..., a:b].mean(-1)
    out['win'] = {'b1s': wm(0, 100), 'b70': wm(93, 100), 'f70': wm(100, 107),
                  'p05_1': wm(150, 200), 'b200': wm(80, 100), 'f200': wm(100, 120),
                  'b750': pre[:, :, 0, 0:75].mean(-1)}
    # post-series window means (cells, 20) at 3-4 s and 5-6 s after the last puff onset
    out['postwin'] = {'3-4': POST[:, :20, 400:500].mean(-1), '5-6': POST[:, :20, 600:700].mean(-1)}
    # epoch-averaged traces
    out['ep'] = {k: P[:, v].mean(1) for k, v in PUFF_EPOCHS.items()}           # (cells, 8, 300)
    out['ep_post'] = {k: POST[:, v].mean(1) for k, v in PUFF_EPOCHS.items() if v.max() < 32}
    # first two puffs of series 1 to 32 (Fig. 4H, 4I) and the per-cell regions
    out['first2'] = P[:, :32, :2, :]                                             # (cells, 32, 2, 300)
    out['region_sel'] = S['region'][sel]
    # ---- persistent dimension and baseline windows (needs full-length rates of all units)
    sel_ix = np.where(sel)[0]
    out['cd_persist'] = {}
    for var in ('M', 'C'):
        w = cd_weights(out['win']['p05_1'].mean(2), out['win']['b1s'].mean(2), var)
        out['cd_persist'][var] = w
    out['base_proj'] = {var: np.tensordot(w, BASE_ALL[sel_ix], axes=([0], [0]))
                        for var, w in out['cd_persist'].items()}                  # (40, 3000)
    out['coupling'] = coupling_values(BASE_ALL[sel_ix], out['cd_persist'],
                                      {'pre_M': PUFF_EPOCHS['pre'], 'ket_M': PUFF_EPOCHS['ket_M'],
                                       'pre_C': np.arange(0, 10), 'ket_C': np.arange(22, 32)})
    out['coupling_series'] = coupling_per_series(BASE_ALL[sel_ix], out['cd_persist'])
    if has_tone:
        T = np.stack(T)                    # (n_sel, n_tone_series_used, 8, 300)
        TBASE_ALL = np.stack(TBASE_ALL)    # (n_units, n_tone_series_used, 3000)
        out['tone_sets'] = S['tone_sets']
        out['tone_series_used'] = S['tone_series_used']
        out['tone_win'], out['tone_ep'], out['cd_tone_persist'] = {}, {}, {}
        out['tone_base_proj'], out['tone_coupling'], out['tone_coupling_series'] = {}, {}, {}
        out['tone_coupling_puffwin'] = {}
        for name, ts in out['tone_sets'].items():
            tpre = T[:, ts['pre']]
            out['tone_win'][name] = {'b1s': tpre[..., 0:100].mean(-1),
                                     'b70': tpre[..., 93:100].mean(-1),
                                     'f70': tpre[..., 100:107].mean(-1),
                                     'p150_350': tpre[..., 115:135].mean(-1)}
            out['tone_ep'][name] = {k: T[:, v].mean(1) for k, v in ts.items()}
            cds = {var: cd_weights(out['tone_win'][name]['p150_350'].mean(2),
                                   out['tone_win'][name]['b1s'].mean(2), var) for var in ('M', 'C')}
            out['cd_tone_persist'][name] = cds
            out['tone_base_proj'][name] = {var: np.tensordot(w, TBASE_ALL[sel_ix], axes=([0], [0]))
                                           for var, w in cds.items()}
            out['tone_coupling'][name] = coupling_values(TBASE_ALL[sel_ix], cds,
                                                         {'pre': ts['pre'], 'ket': ts['ket']})
            out['tone_coupling_series'][name] = coupling_per_series(TBASE_ALL[sel_ix], cds)
            # code variant: tone dimension, windows before puff series 1-10 and 23-32
            out['tone_coupling_puffwin'][name] = coupling_values(
                BASE_ALL[sel_ix], cds, {'pre_C': np.arange(0, 10), 'ket_C': np.arange(22, 32)})
    if verbose:
        print(path, n_units, out['n_sel'])
    return out


def coupling_values(base, cds, epochs):
    """Pairwise coupling among the top-decile cells of a coding dimension.

    base: (cells, n_series, 3000) z-scored rates of the puff-modulated cells.
    Returns {(var, rule, epoch): value}: rule 'M' = mean signed Pearson r among cells with |w|
    above the 90th percentile of |w| (Methods); rule 'C' = median |r| among cells with signed w
    above that percentile (code).
    """
    res = {}
    for var, w in cds.items():
        thr = np.percentile(np.abs(w), 90)
        tops = {'M': np.where(np.abs(w) > thr)[0], 'C': np.where(w > thr)[0]}
        for rule, top in tops.items():
            for ep, ser in epochs.items():
                if len(top) < 2:
                    res[(var, rule, ep)] = np.nan
                    res[(var, rule, ep, 'n_cells')] = len(top)
                    continue
                x = base[top][:, ser].reshape(len(top), -1).astype(np.float64)
                with np.errstate(invalid='ignore', divide='ignore'):
                    r = np.corrcoef(x)
                iu = ~np.eye(len(top), dtype=bool)
                vals = r[iu]
                res[(var, rule, ep)] = np.nanmean(vals) if rule == 'M' else np.nanmedian(np.abs(vals))
                res[(var, rule, ep, 'n_cells')] = len(top)
    return res


def coupling_per_series(base, cds):
    """Coupling computed within each 30-s window separately: {(var, rule): (n_series,)}."""
    res = {}
    for var, w in cds.items():
        thr = np.percentile(np.abs(w), 90)
        tops = {'M': np.where(np.abs(w) > thr)[0], 'C': np.where(w > thr)[0]}
        for rule, top in tops.items():
            vals = []
            iu = ~np.eye(len(top), dtype=bool)
            if len(top) < 2:
                res[(var, rule)] = np.full(base.shape[1], np.nan)
                continue
            for i in range(base.shape[1]):
                with np.errstate(invalid='ignore', divide='ignore'):
                    r = np.corrcoef(base[top, i].astype(np.float64))[iu]
                vals.append(np.nanmean(r) if rule == 'M' else np.nanmedian(np.abs(r)))
            res[(var, rule)] = np.array(vals)
    return res


# ---------------------------------------------------------------------------------------------
# Across-session summaries

def zproj(trace, base_bins=100):
    """Code: z-score a projection over its window, subtract the mean of the pre-stimulus bins."""
    z = scipy.stats.zscore(trace)
    return z - z[:base_bins].mean()


def fast_cd(R, var='M', ref='1s'):
    x = R['win']['f70'].reshape(R['n_sel'], -1)
    y = (R['win']['b1s'] if ref == '1s' else R['win']['b70']).reshape(R['n_sel'], -1)
    return cd_weights(x, y, var)


def persist_projection(R, var='M', first_only=True, ket='ket_M', post='post_M'):
    """Fig. 6D: z-scored projection of the epoch-mean traces on the persistent dimension."""
    w = R['cd_persist'][var]
    out = {}
    for name, ep in (('pre', 'pre'), ('ket', ket), ('post', post)):
        tr = np.tensordot(w, R['ep'][ep], axes=([0], [0]))   # (8, 300)
        tr = tr[0] if first_only else tr.mean(0)
        out[name] = zproj(tr)
    return out


def fast_projection(R, var='M', ref='1s', ket='ket_M', post='post_M'):
    w = fast_cd(R, var, ref)
    return {name: zproj(np.tensordot(w, R['ep'][ep], axes=([0], [0])).mean(0))
            for name, ep in (('pre', 'pre'), ('ket', ket), ('post', post))}


def paired(a, b):
    r = scipy.stats.ttest_rel(a, b)
    return float(r.statistic), float(r.pvalue)


def bh(p):
    from statsmodels.stats.multitest import multipletests
    return multipletests(p, method='fdr_bh')[1]


def affective_cd(R, target='5-6', var='M', eye='puffs5-8'):
    """Emotion-like dimension (Methods; code get_affective_projections)."""
    n = R['n_sel']
    w_aff = cd_weights(R['postwin'][target], R['win']['b750'], var)
    if eye == 'puffs5-8':
        x = R['win']['f200'][:, :, 4:].reshape(n, -1); y = R['win']['b200'][:, :, 4:].reshape(n, -1)
    else:  # the last 4 series of the preinfusion epoch, all puffs
        x = R['win']['f200'][:, 16:].reshape(n, -1); y = R['win']['b200'][:, 16:].reshape(n, -1)
    w_eye = cd_weights(x, y, var)
    q, _ = my_qr(np.vstack((w_eye, w_aff)).T)
    w = q[:, 1]
    tr = np.tensordot(w, R['ep']['pre'], axes=([0], [0]))   # (8, 300)
    if tr.mean(-1)[7] < tr.mean(-1)[0]:
        w = -w
    return w


def affective_signal(R, w, ep):
    """Concatenated series signal from 0.25 s before the first puff (code plot_affective_*):
    8 puff windows (each -1..+2 s) minus the first 0.75 s, then the post-series window from
    4 s after the last puff onset to 49 s after it (code start=500). Baseline: mean of the
    first 25 bins (250 ms before the first puff). Returns (signal, time axis relative to the
    first puff), with NaN in the 23 to 25 s gap the code leaves."""
    ser = np.tensordot(w, R['ep'][ep], axes=([0], [0])).reshape(-1)[75:]   # -0.25 .. 23 s
    post = np.tensordot(w, R['ep_post'][ep], axes=([0], [0]))              # 20 .. 70 s
    sig = np.r_[ser, np.full(200, np.nan), post[500:]]
    t = np.r_[np.arange(len(ser)) * BIN - 0.25, 23 + np.arange(200) * BIN,
              25 + np.arange(len(post) - 500) * BIN]
    base = ser[:25].mean()
    return sig - base, t


def extract_timescale(signal, fit_time=2.5, t0=0.2, start_lag=1):
    """Code extract_timescale. start_lag=1: the code (lags from one bin); 0: from the peak (lag 0).
    Returns b, or NaN when the fit fails."""
    sig = scipy.signal.correlate(signal, signal)
    mid = len(signal) - 1
    sig = sig[mid + start_lag:][:int(round(fit_time / BIN))]
    sig = sig / sig.max()
    x = np.arange(len(sig)) * BIN
    try:
        popt, _ = curve_fit(lambda x, a, b, c: a * np.exp(-x / b) + c, x, sig, p0=[1, t0, 0],
                            maxfev=2000)
    except RuntimeError:
        return np.nan
    return popt[1]


# ---------------------------------------------------------------------------------------------
# Clusters of puff-modulated cells (Fig. 4E, 4G; Methods "Unsupervised clustering of peri-puff
# firing rates"; code get_cell_clusters). Scanpy PCA (arpack), neighbours (30, 20 PCs), UMAP,
# Leiden (leidenalg, resolution 1, scanpy's default seed); seeds fixed as in the code (42).

def cluster_cells(Rs, resolution=1.0):
    import anndata
    import scanpy as sc
    X = np.vstack([R['ep']['pre'].mean(1) for R in Rs]).astype(np.float64)
    X = X - X[:, :100].mean(1, keepdims=True)
    np.random.seed(42)
    ad = anndata.AnnData(X.astype(np.float32))
    sc.tl.pca(ad, svd_solver='arpack')
    sc.pp.neighbors(ad, n_neighbors=30, n_pcs=20, random_state=0)
    sc.tl.umap(ad, random_state=0)
    sc.tl.leiden(ad, flavor='leidenalg', resolution=resolution, random_state=0)
    lab = ad.obs['leiden'].astype(int).values
    sess = np.concatenate([[i] * R['n_sel'] for i, R in enumerate(Rs)])
    return lab, sess


def find_decay(trace, thresh=0.25):
    """Code plot_cluster_distribution.find_decay: time (s) after puff onset at which |trace|,
    normalised to its post-onset maximum, falls below 0.25 after its peak; 2 s when the peak's
    z-score is below 1 or the trace never falls below the threshold within 2 s."""
    z = scipy.stats.zscore(trace)
    a = np.abs(trace / np.nanmax(np.abs(trace[100:])))
    peak = np.argmax(a[100:])
    below = np.where(a[100:][peak:] < thresh)[0]
    if np.abs(z[100:][peak]) < 1 or len(below) == 0:
        return 2.0
    return BIN * (peak + below[0])


def cluster_condition_traces(Rs, lab, ket='ket_M'):
    """Fig. 4G: per cluster, each cell's trial-averaged per-puff trace (mean of 8 puffs over the
    epoch's series), baseline subtracted by its 1 s before the puff; the cluster and condition
    mean trace sets a z-transform (mean and s.d. over the 3-s window) applied to every cell, then
    the 1 s baseline of the transformed trace is subtracted. Returns {cluster: {cond: (mean, ci)}}
    with ci = 1.96 s.e.m. over cells."""
    out = {}
    pre = np.vstack([R['ep']['pre'].mean(1) for R in Rs])
    kt = np.vstack([R['ep'][ket].mean(1) for R in Rs])
    for c in np.unique(lab):
        out[c] = {}
        for name, X in (('pre', pre), ('ket', kt)):
            x = X[lab == c] - X[lab == c][:, :100].mean(1, keepdims=True)
            mu, sd = x.mean(0).mean(), x.mean(0).std()
            z = (x - mu) / sd
            z = z - z[:, :100].mean(1, keepdims=True)
            out[c][name] = (z.mean(0), 1.96 * z.std(0, ddof=1) / np.sqrt(len(z)), len(z))
    return out


# ---------------------------------------------------------------------------------------------
# Regional rise and decay times (Fig. 4H, 4I; Methods "Regional rise and decay time"; code
# region_time_course): first two puffs of each series, regions with at least 30 modulated cells
# (Methods; the code uses more than 30), cluster-weighted, d' normalised, 25% thresholds, peaks
# later than 750 ms dropped, regions with peak d' below a threshold (1.3 Methods and code; 2
# Table S3) dropped, 1000 bootstrap resamples of puff replicates.


def reduce_region(s):
    m = re.match(r'(?!CA[123])(.*?)(2/3|1|5|6a|6b|pc)$', s)
    return m.groups()[0] if m else s


def _dprime(x):
    """Code calculate_dprime (region_time_course): x (..., n_rep, 300) -> (..., 300)."""
    bm = x[..., :100].mean(axis=(-1, -2))
    bs = np.nanstd(x[..., :100].reshape(x.shape[:-2] + (-1,)), axis=-1)
    rm = x.mean(-2)
    rs = np.nanstd(x, axis=-2)
    den = np.sqrt(.5 * (bs[..., None] ** 2 + rs ** 2))
    return np.abs(rm - bm[..., None]) / den


def _rise_decay(x, thresh=0.25):
    """Code _find_rise_decay on x (n_boot, n_rep, 300) -> rise, decay (n_boot,)."""
    d = _dprime(x)
    d = d - d[:, :100].mean(1, keepdims=True)
    d = d / d.max(1, keepdims=True)
    post = d[:, 100:]
    peak = np.argmax(post, 1)
    rise = np.full(len(d), np.nan); decay = np.full(len(d), np.nan)
    for i in range(len(d)):
        a = np.where(post[i] > thresh)[0]
        if len(a):
            rise[i] = BIN * a[0]
        b = np.where(post[i, peak[i]:] < thresh)[0]
        if len(b):
            decay[i] = BIN * (peak[i] + b[0])
    bad = peak > 75
    rise[bad] = np.nan; decay[bad] = np.nan
    return rise, decay


def region_rise_decay(Rs, lab, ket_series, min_cells=30, dprime_min=1.3, n_boot=1000, seed=0,
                      exclude=('NA', 'STR', 'MB', 'HY')):
    rng = np.random.default_rng(seed)
    reg = np.array([reduce_region(r) for R in Rs for r in R['region_sel']])
    pre = np.concatenate([R['first2'][:, :20] for R in Rs])          # (cells, 20, 2, 300)
    kt = np.concatenate([R['first2'][:, ket_series] for R in Rs])    # (cells, n, 2, 300)
    clusters = np.unique(lab)
    res = {}
    for r in np.unique(reg):
        f = reg == r
        if f.sum() < min_cells or r in exclude:
            continue
        dmax = np.max(np.abs(_dprime(pre[f].mean(0).reshape(-1, WIN)[None])[0][100:]))
        if dmax < dprime_min:
            continue
        w = np.array([np.sum(f & (lab == c)) for c in clusters], float)
        w[w <= 1] = 0
        w = w / w.sum()
        out = {}
        for name, X in (('pre', pre), ('ket', kt)):
            n_rep = X.shape[1] * 2
            ix = rng.integers(0, n_rep, size=(n_boot, n_rep))
            rise = np.zeros(n_boot); decay = np.zeros(n_boot)
            for j, c in enumerate(clusters):
                if w[j] == 0:
                    continue
                x = np.nanmean(X[f & (lab == c)], 0).reshape(n_rep, WIN)
                x = x - x[:, :100].mean(1, keepdims=True)
                ri, de = _rise_decay(x[ix])
                rise += np.nan_to_num(w[j] * ri); decay += np.nan_to_num(w[j] * de)
            out[name] = (rise, decay)
        res[r] = dict(n=int(f.sum()), dmax=dmax, **out)
    return res


# ---------------------------------------------------------------------------------------------
# Two-phase first-order model (Methods "Theoretical model"; code model_system, theoretical_*,
# compare_model, compare_models). 10 ms bins; 8 inputs of 250 ms every 3 s after 1 s of
# silence, then 47 s of decay; the fitted segment is -0.25 to 23 s and 25 to 70 s after the
# first puff, as the neural signal; parameters in [0, 100], condition multipliers in [0, 1]
# (null model: multipliers fixed near 1).

_inputs = np.hstack([np.concatenate([np.zeros(100), np.ones(25), np.zeros(175)]) for _ in range(8)])
_inputs = np.hstack([_inputs, np.zeros(int(47 / BIN))])
_segments = np.hstack([np.hstack([(i * 300), (i * 300) + 100, (i * 300) + 100, (i * 300) + 125,
                                  (i * 300) + 125, (i * 300) + 300]) for i in range(8)])
_segments = np.hstack([_segments, [300 * 8, 300 * 8 + int(47 / BIN)]]).reshape(-1, 2)


def model_system(S, tB, tP):
    Sin = S * _inputs
    out = np.zeros_like(Sin)
    x0 = Sin[0]
    for a, b in _segments:
        t = np.arange(b - a) * BIN
        if Sin[a] != 0:
            xt = (Sin[a] - x0) * (1 - np.exp(-t / tB)) + x0
        else:
            xt = x0 * np.exp(-t / tP)
        out[a:b] = xt
        x0 = xt[-1]
    return out


def _cut(o):
    return np.hstack([o[75:300 * 8], o[300 * 8 + 200:300 * 8 + int(49 / BIN)]])


def theoretical(kind):
    def f(x, S, tB, tP, *cs):
        tr = []
        for c in cs:
            if kind == 'persist':
                o = model_system(S, tB, tP * c)
            elif kind == 'broadcast':
                o = model_system(S, tB * c, tP)
            else:  # saturation
                o = model_system(S * c, tB, tP)
            tr.append(_cut(o))
        return np.hstack(tr)
    return f


def compare_model(kind, data, n_cond=2):
    """Code compare_model: variance explained = 1 - MSE(model) / MSE(null)."""
    f = theoretical(kind)
    p0 = [1, 1, 1] + [1] * n_cond
    b = ([0, 0, 0] + [0] * n_cond, [100, 100, 100] + [1] * n_cond)
    bn = ([0, 0, 0] + [0.99999] * n_cond, [100, 100, 100] + [1] * n_cond)
    x = np.arange(len(data))
    pm, _ = curve_fit(f, x, data, p0=p0, maxfev=5000, bounds=b)
    pn, _ = curve_fit(f, x, data, p0=p0, maxfev=5000, bounds=bn)
    pred = f(x, *pm); predn = f(x, *pn)
    return dict(varexp=1 - np.mean((data - pred) ** 2) / np.mean((data - predn) ** 2),
                params=pm, pred=pred, pred_null=predn)


# ---------------------------------------------------------------------------------------------
# Per-session tables for the notebook

EPOCH_READINGS = {'Methods (22-32, 34-40)': ('ket_M', 'post_M'),
                  'code / Table S3 (23-32, 35-40)': ('ket_C', 'post_C')}


def _df(pop, rows):
    d = pd.DataFrame(rows)
    d.insert(0, 'session', [f"sub-{R['subject']}_{R['session']}" for R in pop])
    d.insert(1, 'mouse', [R['subject'] for R in pop])
    return d


def persist_table(pop, var, first_only, ket, post):
    rows = []
    for R in pop:
        p = persist_projection(R, var, first_only, ket, post)
        rows.append({k: v[200:300].mean() for k, v in p.items()})
    return _df(pop, rows)


def fast_table(pop, var, ref, ket, post):
    rows = []
    for R in pop:
        p = fast_projection(R, var, ref, ket, post)
        rows.append({k: v[100:107].mean() for k, v in p.items()})
    return _df(pop, rows)


def three_way_tests(d):
    """Paired t-tests pre vs ket and ket vs post, BH over the two (code multiple_tests)."""
    t1, p1 = paired(d['pre'], d['ket'])
    t2, p2 = paired(d['ket'], d['post'])
    q = bh([p1, p2])
    return dict(t_pre_ket=t1, p_pre_ket=p1, q_pre_ket=q[0], t_ket_post=t2, p_ket_post=p2, q_ket_post=q[1])


def mean_sem(x):
    x = np.asarray(x, float)
    x = x[~np.isnan(x)]
    return x.mean(), x.std() / np.sqrt(len(x))   # code: np.std (ddof 0) / sqrt(n)


def by_mouse(d, cols):
    return d.groupby('mouse')[cols].mean().reset_index()


def affective_table(pop, target, var, eye, ket):
    rows, sigs = [], {'pre': [], 'ket': []}
    for R in pop:
        w = affective_cd(R, target, var, eye)
        row = {}
        for k, ep in (('pre', 'pre'), ('ket', ket)):
            s, t = affective_signal(R, w, ep)
            row[f'{k}_early'] = s[25:50].mean()      # 0 to 0.25 s after the first puff
            row[f'{k}_late'] = s[225:325].mean()     # 2 to 3 s after the first puff
            sigs[k].append(s)
        rows.append(row)
    return _df(pop, rows), {k: np.array(v) for k, v in sigs.items()}, t


def timescale_table(pop, var, pre_series, ket_series, start_lag, mode, key='base_proj'):
    rows, nfail = [], 0
    for R in pop:
        bp = R[key][var] if not callable(key) else key(R)[var]
        row = {}
        for k, ser in (('pre', pre_series(R) if callable(pre_series) else pre_series),
                       ('ket', ket_series(R) if callable(ket_series) else ket_series)):
            if mode == 'per-series':
                v = np.array([extract_timescale(bp[i], start_lag=start_lag) for i in ser])
                nfail += int(np.isnan(v).sum())
                row[k] = np.nanmean(v)
            else:
                row[k] = extract_timescale(bp[ser].ravel(), start_lag=start_lag)
                nfail += int(np.isnan(row[k]))
        rows.append(row)
    return _df(pop, rows), nfail


# ---------------------------------------------------------------------------------------------
# Behavioural dose fits (Fig. 5H, 5I; Methods "Model fitting, behavioral data"; code
# theoretical_behavior, filter_reflex; trace processing of ketmouse eye_trace_utils
# get_mean_traces as called in mouse_eyepuff/scripts/fig1_dose.py). Eye closure at 200 frames/s,
# 40 trials of 81 s with the first puff at 6 s; each trial minus the mean of its first 400 frames
# (prox_norm), scaled by 1/(1 - baseline of trial 1); the median over trials 23 to 37 (code
# which_post = 22..36, agg_fn = np.median); averaged across mice (Methods); resampled to 10 ms by
# averaging frame pairs; -1 s to 43 s around the first puff (the model's 4400 bins); the 750 ms
# after each puff removed (filter_reflex).

FRAMES_PER_TRIAL = 16200
FPS_BEH = 200


def dose_trace(expids, which=np.arange(22, 37)):
    traces = []
    for e in expids:
        f = dandi_io.open_h5(f'sub-mouse/sub-mouse_ses-{e}_behavior.nwb')
        x = f['acquisition/eye_closure/data'][:]
        f.close()
        bt = x[:FRAMES_PER_TRIAL * 40].reshape(40, -1)
        bt = bt - bt[:, :400].mean(1, keepdims=True)
        base = bt[0, :400].mean()
        tr = (np.median(bt[which], 0) - base) / (1 - base)
        traces.append(tr)
    tr = np.mean(traces, 0)
    seg = tr[5 * FPS_BEH:5 * FPS_BEH + 8800]          # -1 s to 43 s
    return seg.reshape(-1, 2).mean(1), np.array(traces)


def filter_reflex(trace):
    out = [trace[:100]]
    for i in range(8):
        out.append(trace[100 + i * 300 + 75:100 + i * 300 + 300])
    out.append(trace[100 + 7 * 300 + 300:])
    return np.hstack(out)


def fit_behaviour(traces):
    """Persistence model fitted jointly to several conditions' eye-closure traces (code
    theoretical_behavior); variance explained against the model with no condition multiplier."""
    data = np.hstack([filter_reflex(t) for t in traces])
    k = len(traces)

    def f(x, S, tB, tP, *cs):
        return np.hstack([filter_reflex(model_system(S, tB, tP * c)[:4400]) for c in cs])
    p0 = [1, 1, 1] + [1] * k
    b = ([0, 0, 0] + [0] * k, [100, 100, 100] + [1] * k)
    bn = ([0, 0, 0] + [0.99999] * k, [100, 100, 100] + [1] * k)
    x = np.arange(len(data))
    pm, _ = curve_fit(f, x, data, p0=p0, maxfev=5000, bounds=b)
    pn, _ = curve_fit(f, x, data, p0=p0, maxfev=5000, bounds=bn)
    return dict(varexp=1 - np.mean((data - f(x, *pm)) ** 2) / np.mean((data - f(x, *pn)) ** 2), params=pm)
