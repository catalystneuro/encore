"""Loading and reactivation measures for CRCNS pfc-6 (Peyrache et al. 2009, Nat Neurosci 12:919).

The data set is one tar.gz on the public CRCNS bucket. It is streamed once, in order, and each
session's text files are parsed in memory; nothing is written to disk.

Where parameters come from:

- 100 ms bins, z-transform per cell within an epoch, C = QQ'/B, projectors p p', and
  R_l(t) = sum over i != j of Q_it P_ij Q_jt: Online Methods, "Computational methods", and
  Supplementary Figure 3 (cited in the claims file's opening comment).
- lambda_max/min = (1 +- sqrt(1/q))^2, q = B/n, Phi = lambda/lambda_max: Online Methods,
  "Signal and nonsignal components".
- Inclusion rule (at least ten cells, at least 4 min of SWS in each rest epoch): Results,
  paragraph 2, as the claims file quotes it.
- A bin counts as SWS when it lies wholly inside an SWS interval: standard choice named in the
  claims file's opening comment.
- Rest epochs: the data set gives SWS intervals and the awake epoch only. The pre epoch is taken
  as the time before the awake epoch and the post epoch as the time after it, each bounded by the
  first and last spike of the session (an assumption; the claims file's supp5 criterion says the
  rest epochs are taken from the data set's epoch times).
"""
import io
import tarfile

import fsspec
import numpy as np

DATASET = "crcns:pfc-6/unversioned"  # doi:10.6080/K0KH0KH5
URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-6/live/mPFC_Data.tar.gz"
MD5 = "2c255b44209ece01326dd09efaabd92a"  # from pfc-6/live/checksums.md5
BIN_MS = 100.0
DOCX = "https://crcnsarchive.s3-us-west-2.amazonaws.com/pfc-6/live/docs/crcns_pfc-6_data_description.docx"


def learning_trials_from_docs(url=DOCX):
    """The learning sessions and the trials at which the rule was acquired, as the data set's
    description lists them ("Trials during which learning occurred"). Read from the .docx in
    the bucket, so that nothing is copied by hand."""
    import re
    import zipfile
    with fsspec.open(url) as f:
        xml = zipfile.ZipFile(f).read("word/document.xml").decode()
    text = re.sub(r"<[^>]+>", "", re.sub(r"</w:p>", "\n", xml))
    i = text.find("These sessions are:")
    j = text.find("respective order):")
    sessions = re.findall(r"\d{6}", text[i:j])
    trials = [int(x) for x in re.findall(r"\d+", text[j + len("respective order):"):].split("\n\n")[0])]
    return dict(zip(sessions, trials))


def _parse(raw):
    if not raw.strip():
        return np.zeros((0,))
    return np.array(raw.split(), dtype=float)


def load_sessions(url=URL):
    """Stream the archive and return {session id: dict of arrays}.

    Keys: spikes_t (ms), spikes_id (cell id), celltype (per cell, 0 unknown, 1 interneuron,
    2 pyramidal), wake (2,), sws_pre (k, 2), sws_post (k, 2), behavior (trials, 6), pos (frames, 3).
    """
    sessions = {}
    names = {"SpikeData": 2, "WakeEpoch": 2, "SwsPRE": 2, "SwsPOST": 2, "Behavior": 6,
             "CellType": 1, "Pos": 3}
    with fsspec.open(url, block_size=2**22) as f:
        tf = tarfile.open(fileobj=f, mode="r|gz")
        for m in tf:
            if not m.isfile():
                continue
            sid, fname = m.name.split("/")[-2:]
            kind = fname[len(sid) + 1:-4]
            ncol = names[kind]
            a = _parse(tf.extractfile(m).read())
            a = a.reshape(-1, ncol) if ncol > 1 else a
            sessions.setdefault(sid, {})[kind] = a
    out = {}
    for sid in sorted(sessions):
        s = sessions[sid]
        sp = s["SpikeData"]
        out[sid] = dict(
            rat=int(sid[:2]),
            spikes_t=sp[:, 0],
            spikes_id=sp[:, 1].astype(int),
            celltype=s["CellType"].astype(int),
            wake=s["WakeEpoch"].reshape(-1, 2)[0],
            n_wake_rows=len(s["WakeEpoch"].reshape(-1, 2)),
            sws_pre=s["SwsPRE"].reshape(-1, 2),
            sws_post=s["SwsPOST"].reshape(-1, 2),
            behavior=s["Behavior"].reshape(-1, 6),
            pos=s["Pos"].reshape(-1, 3),
        )
    return out


def n_cells(s):
    return len(s["celltype"])


def sws_minutes(iv):
    return float(np.sum(iv[:, 1] - iv[:, 0])) / 60000.0 if len(iv) else 0.0


def bin_counts(s, t0, t1, bin_ms=BIN_MS):
    """Spike counts (cells x bins) in bins of bin_ms from t0, and the bin edges."""
    nb = int(np.floor((t1 - t0) / bin_ms))
    edges = t0 + bin_ms * np.arange(nb + 1)
    n = n_cells(s)
    t, c = s["spikes_t"], s["spikes_id"] - 1
    keep = (t >= edges[0]) & (t < edges[-1])
    b = ((t[keep] - t0) // bin_ms).astype(int)
    counts = np.zeros((n, nb))
    np.add.at(counts, (c[keep], b), 1)
    return counts, edges


def in_intervals(edges, iv):
    """True for bins [edges[k], edges[k+1]) wholly inside one of the intervals iv."""
    lo, hi = edges[:-1], edges[1:]
    m = np.zeros(len(lo), bool)
    for a, b in iv:
        m |= (lo >= a) & (hi <= b)
    return m


def zscore(counts):
    """z-transform each row; rows with zero variance become 0 (and are reported)."""
    mu = counts.mean(axis=1, keepdims=True)
    sd = counts.std(axis=1, ddof=1, keepdims=True)
    with np.errstate(invalid="ignore", divide="ignore"):
        q = (counts - mu) / sd
    q[~np.isfinite(q)] = 0.0
    return q


def mp_bounds(n, B):
    q = B / n
    return (1 - np.sqrt(1 / q)) ** 2, (1 + np.sqrt(1 / q)) ** 2


def template(q):
    """Eigen-decomposition of C = QQ'/B (descending eigenvalues), with the MP bounds."""
    n, B = q.shape
    C = q @ q.T / B
    lam, vec = np.linalg.eigh(C)
    order = np.argsort(lam)[::-1]
    lam, vec = lam[order], vec[:, order]
    lmin, lmax = mp_bounds(n, B)
    return lam, vec, lmin, lmax


def reactivation(q, vec):
    """R_l(t) = sum over i != j of Q_it P_ij Q_jt for each column of vec (components x bins)."""
    proj = vec.T @ q                      # (L, T): p' Q_t
    diag = (vec ** 2).T @ (q ** 2)        # (L, T): sum_i p_i^2 Q_it^2
    return proj ** 2 - diag


# ---------------------------------------------------------------- sessions and epochs

def included(s, min_cells=10, min_sws_min=4.0):
    """The paper's inclusion rule (Results, paragraph 2): at least ten cells and at least
    4 min of SWS in each rest epoch."""
    return (n_cells(s) >= min_cells and sws_minutes(s["sws_pre"]) >= min_sws_min
            and sws_minutes(s["sws_post"]) >= min_sws_min)


def rest_epochs(s):
    """(start, end) in ms of the pre and post rest epochs.

    The data set gives only the awake epoch and the SWS intervals. Pre runs from 0 to the start
    of the awake epoch; post from its end to the end of the position record (the video), or to
    the end of the last post SWS interval if that is later. Assumption, stated in the notebook.
    """
    w0, w1 = s["wake"]
    end = max(s["pos"][-1, 0], s["sws_post"][:, 1].max() if len(s["sws_post"]) else 0.0)
    return (0.0, w0), (w1, end)


# ---------------------------------------------------------------- reactivation per session

def session_reactivation(s, bin_ms=BIN_MS):
    """Awake template and reactivation strengths in the pre and post epochs of one session.

    Returns a dict with the eigenvalues, Phi, the MP bounds, and for each rest epoch and each
    z-transform reading ('epoch': z over the whole rest epoch, 'sws': z over its SWS bins only)
    the R_l(t) of every component over the SWS bins, plus over non-SWS bins for 'epoch'.
    """
    w0, w1 = s["wake"]
    cw, _ = bin_counts(s, w0, w1, bin_ms)
    qa = zscore(cw)
    lam, vec, lmin, lmax = template(qa)
    out = dict(lam=lam, vec=vec, lmin=lmin, lmax=lmax, phi=lam / lmax, n=qa.shape[0],
               B=qa.shape[1], q_awake=qa, silent_awake=int(np.sum(cw.sum(1) == 0)))
    for name, (t0, t1), iv in (("pre", rest_epochs(s)[0], s["sws_pre"]),
                               ("post", rest_epochs(s)[1], s["sws_post"])):
        c, edges = bin_counts(s, t0, t1, bin_ms)
        sws = in_intervals(edges, iv)
        qe = zscore(c)
        qs = zscore(c[:, sws])
        out[name] = dict(
            edges=edges, sws=sws,
            R_sws_epochz=reactivation(qe[:, sws], vec),
            R_nonsws_epochz=reactivation(qe[:, ~sws], vec),
            R_sws_swsz=reactivation(qs, vec),
            q_sws_epochz=qe[:, sws], q_sws_swsz=qs,
            counts_sws=c[:, sws],
            R_all_epochz=reactivation(qe, vec),
        )
    out["R_awake"] = reactivation(qa, vec)
    return out


def runs(mask):
    """Start and stop indices of runs of True in a boolean array."""
    d = np.diff(np.r_[0, mask.astype(int), 0])
    return np.flatnonzero(d == 1), np.flatnonzero(d == -1)


def xcorr_runs(x, y, starts, stops, maxlag):
    """Pearson cross-correlation of x and y (each 1-D over the same bins) at lags -maxlag..maxlag,
    using only pairs of bins inside the same run (y shifted by lag)."""
    out = []
    for lag in range(-maxlag, maxlag + 1):
        a, b = [], []
        for s0, s1 in zip(starts, stops):
            xs, ys = x[s0:s1], y[s0:s1]
            if lag >= 0:
                a.append(xs[:len(xs) - lag]); b.append(ys[lag:])
            else:
                a.append(xs[-lag:]); b.append(ys[:len(ys) + lag])
        a, b = np.concatenate(a), np.concatenate(b)
        out.append(np.corrcoef(a, b)[0, 1] if len(a) > 2 else np.nan)
    return np.array(out)


def xcorr_ratio_runs(x, y, starts, stops, maxlag):
    """Cross-correlogram <x(t) y(t+lag)> divided by <x><y> (chance one), within runs."""
    out = []
    for lag in range(-maxlag, maxlag + 1):
        a, b = [], []
        for s0, s1 in zip(starts, stops):
            xs, ys = x[s0:s1], y[s0:s1]
            if lag >= 0:
                a.append(xs[:len(xs) - lag]); b.append(ys[lag:])
            else:
                a.append(xs[-lag:]); b.append(ys[:len(ys) + lag])
        a, b = np.concatenate(a), np.concatenate(b)
        out.append(np.mean(a * b) / (np.mean(a) * np.mean(b)))
    return np.array(out)


def shuffle_expected_R(q, vec):
    """Mean of R_l(t) over all permutations of the cells within each bin (the limit of the
    Supplementary Figure 11 shuffle as the number of shuffles grows).

    For a random permutation, E[x_pi(i) x_pi(j)] for i != j is (S^2 - S2) / (n (n - 1)), with S
    and S2 the sum and the sum of squares of the bin's values, so
    E[R_l(t)] = (sum_{i != j} P_ij) (S^2 - S2) / (n (n - 1)).
    """
    n = q.shape[0]
    S = q.sum(0)
    S2 = (q ** 2).sum(0)
    offdiag = vec.sum(0) ** 2 - (vec ** 2).sum(0)      # sum_{i != j} p_i p_j per component
    return offdiag[:, None] * ((S ** 2 - S2) / (n * (n - 1)))[None, :]


def shuffle_R(q, vec, n_shuffles, rng):
    """Mean of R_l(t) over n_shuffles independent per-bin permutations of the cells."""
    n, T = q.shape
    acc = np.zeros((vec.shape[1], T))
    for _ in range(n_shuffles):
        perm = np.argsort(rng.random((n, T)), axis=0)
        acc += reactivation(np.take_along_axis(q, perm, axis=0), vec)
    return acc / n_shuffles


# ---------------------------------------------------------------- behaviour

def reached_criterion(correct):
    """True when a sequence of trials holds ten consecutive correct trials, or 12 consecutive
    trials with at most one error (Online Methods, Behavioral task)."""
    c = np.asarray(correct, int)
    run = 0
    for v in c:
        run = run + 1 if v else 0
        if run >= 10:
            return True
    for i in range(len(c) - 11):
        if c[i:i + 12].sum() >= 11:
            return True
    return False


def learning_point(correct, include_block=True):
    """First trial (1-based) of a block of at least three consecutive rewarded trials after which
    the performance until the end of the session is above 80% (Online Methods, Behavioral task).

    include_block: performance counted from the first trial of the block (reading a of the claim)
    or from the trial after the block (reading b). Returns None when no trial qualifies.
    """
    c = np.asarray(correct, int)
    n = len(c)
    for i in range(n - 2):
        if c[i] and c[i + 1] and c[i + 2]:
            j = i + 3
            while j < n and c[j]:
                j += 1                      # end of the block of consecutive rewarded trials
            rest = c[i:] if include_block else c[j:]
            if len(rest) and rest.mean() > 0.8:
                return i + 1
    return None
