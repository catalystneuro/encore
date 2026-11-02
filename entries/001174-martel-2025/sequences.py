"""Sequence detection of Martel et al. (2025), Fig. 4, after identify_sequences.m.

A Python (numba) port of the paper's MATLAB code, identify_sequences.m in the
Zenodo record doi:10.5281/zenodo.14963234 (method S of the claims file). What
follows the code, line for line:

- Events are put on a 1 ms grid: within the time slice, the slice is first
  narrowed to [first event, last event] over all cells, events at or before its
  start are dropped, and times are ceil(1000 * (t - start)) (find_sequences_v25).
- A pattern P of k = 2..5 cells occurs at an event h1 of P(1) when P(2) has an
  event in [h1 + t1, h1 + t2] ms, and so on. The search loops as the code does
  (find_pattern_2_v2, _3, _4, _5): the last event of the final window is taken,
  the 3-step search stops at the first second event that completes the chain,
  while the 4- and 5-step searches stop only the innermost loop, so one first
  event can give several rows. First events are limited to
  h1 <= L - t2 (k = 2) or h1 <= L - (k - 1) * t2 - (k - 1).
- Repetitions closer than `sep` to the previous row's start are dropped,
  comparing each row with the row before it (not with the last kept one); for
  k = 2 the first row is counted twice when sep <= 0, as the code's diff does.
- Candidate patterns (find_sequences_2_3_4_5): each set of k cells in ascending
  and in descending order (nchoosek and fliplr), and k repeats of one cell.
  `orders="all"` tests every ordering of distinct cells (a variant).
- A pattern is kept when its count passes `min_rep` (`rule=">"` as the code,
  `">="` as the Methods' "at least"), and its count's centile among `n_shuffle`
  shuffles exceeds `centile` (0.95). A shuffle circularly shifts each cell's
  1 ms series by randi(L) positions (shuffle_data); the centile is
  (#below + 0.5 #equal) / n (centile_value).
- Double counting (eliminate_double_counting_v2). As documented, sequences are
  taken in order of length, then of repetitions, both descending (stable, from
  the unique-row order); an occurrence is dropped when one of its events was
  already used, and a sequence is kept when at least `min_rep` occurrences
  remain. As the code runs, the step marks used events by writing 2 into the
  logical event array (`DA(...) = 2`), which MATLAB stores as true, so the test
  `DA(...) == 2` is never met and no occurrence is dropped; only the final
  `>= min_rep` filter acts. `dedupe="code"` does what the code does,
  `dedupe="documented"` what its comments say.

The parameters (t1, t2, sep, min_rep, the time slices) come from the claims
file's method S and the readings it lists; the number of shuffles and the
centile from the Methods. The random generator is given by the caller.
"""

from __future__ import annotations

import itertools

import numpy as np
from numba import njit, prange


# ------------------------------------------------------------------ data

def to_grid(event_times, ts):
    """Events (list of arrays of times in s, one per cell) to 1 ms integer times in slice ts.

    Cells without any event in the whole file are left out by the caller, as the
    code reads only cells present in the IDPS event export.
    """
    first = min(t[0] for t in event_times if len(t))
    last = max(t[-1] for t in event_times if len(t))
    t0 = max(ts[0], first)
    t1 = min(ts[1], last)
    out = []
    for t in event_times:
        t = t[t <= t1] - t0
        t = t[t > 0]
        out.append(np.ceil(np.round(t * 1000, 6)).astype(np.int64))
    L = int(np.ceil(np.round(1000 * t1, 6)) - np.ceil(np.round(1000 * t0, 6)))
    return out, L


def flatten(cells):
    off = np.zeros(len(cells) + 1, dtype=np.int64)
    off[1:] = np.cumsum([len(c) for c in cells])
    ev = np.concatenate(cells).astype(np.int64) if off[-1] else np.zeros(0, np.int64)
    return ev, off


# ------------------------------------------------------------------ pattern search

@njit
def _win(ev, off, c, a, b):
    seg = ev[off[c]:off[c + 1]]
    lo = np.searchsorted(seg, a, side="left")
    hi = np.searchsorted(seg, b, side="right")
    return off[c] + lo, off[c] + hi


@njit
def _rows(ev, off, P, k, t1, t2, L, out, store):
    """Raw rows of pattern P (first events and members); returns the number of rows."""
    m = 0
    if k == 2:
        limit = L - t2
    else:
        limit = L - (k - 1) * t2 - (k - 1)
    c1 = P[0]
    for i1 in range(off[c1], off[c1 + 1]):
        h1 = ev[i1]
        if h1 > limit:
            break
        lo2, hi2 = _win(ev, off, P[1], h1 + t1, h1 + t2)
        if k == 2:
            if hi2 > lo2:
                if store:
                    out[m, 0] = h1
                    out[m, 1] = ev[hi2 - 1]
                m += 1
            continue
        for i2 in range(lo2, hi2):
            h2 = ev[i2]
            lo3, hi3 = _win(ev, off, P[2], h2 + t1, h2 + t2)
            if k == 3:
                if hi3 > lo3:
                    if store:
                        out[m, 0] = h1
                        out[m, 1] = h2
                        out[m, 2] = ev[hi3 - 1]
                    m += 1
                    break
                continue
            for i3 in range(lo3, hi3):
                h3 = ev[i3]
                lo4, hi4 = _win(ev, off, P[3], h3 + t1, h3 + t2)
                if k == 4:
                    if hi4 > lo4:
                        if store:
                            out[m, 0] = h1
                            out[m, 1] = h2
                            out[m, 2] = h3
                            out[m, 3] = ev[hi4 - 1]
                        m += 1
                        break
                    continue
                for i4 in range(lo4, hi4):
                    h4 = ev[i4]
                    lo5, hi5 = _win(ev, off, P[4], h4 + t1, h4 + t2)
                    if hi5 > lo5:
                        if store:
                            out[m, 0] = h1
                            out[m, 1] = h2
                            out[m, 2] = h3
                            out[m, 3] = h4
                            out[m, 4] = ev[hi5 - 1]
                        m += 1
                        break
    return m


@njit
def _sep_keep(first, m, k, sep):
    """Indices of rows kept by the separation rule (with the code's k = 2 quirk)."""
    keep = np.empty(m + 1, dtype=np.int64)
    n = 0
    if m == 0:
        return keep[:0]
    keep[n] = 0
    n += 1
    if k == 2:
        # ST = [r1; rows(diff([r1; rows]) >= sep)], the first diff being 0
        for i in range(m):
            d = first[i] - first[i - 1] if i > 0 else 0
            if d >= sep:
                keep[n] = i
                n += 1
    else:
        for i in range(1, m):
            if first[i] - first[i - 1] >= sep:
                keep[n] = i
                n += 1
    return keep[:n]


@njit
def count_pattern(ev, off, P, k, t1, t2, L, sep):
    """Repetitions of P after the separation rule, counted as the rows are found."""
    if k == 2:
        limit = L - t2
    else:
        limit = L - (k - 1) * t2 - (k - 1)
    n = 0
    m = 0
    prev = 0
    c1 = P[0]
    for i1 in range(off[c1], off[c1 + 1]):
        h1 = ev[i1]
        if h1 > limit:
            break
        lo2, hi2 = _win(ev, off, P[1], h1 + t1, h1 + t2)
        nrow = 0
        if k == 2:
            if hi2 > lo2:
                nrow = 1
        else:
            for i2 in range(lo2, hi2):
                lo3, hi3 = _win(ev, off, P[2], ev[i2] + t1, ev[i2] + t2)
                if k == 3:
                    if hi3 > lo3:
                        nrow = 1
                        break
                    continue
                for i3 in range(lo3, hi3):
                    lo4, hi4 = _win(ev, off, P[3], ev[i3] + t1, ev[i3] + t2)
                    if k == 4:
                        if hi4 > lo4:
                            nrow += 1
                            break
                        continue
                    for i4 in range(lo4, hi4):
                        lo5, hi5 = _win(ev, off, P[4], ev[i4] + t1, ev[i4] + t2)
                        if hi5 > lo5:
                            nrow += 1
                            break
        for _ in range(nrow):
            if m == 0:
                n = 2 if (k == 2 and 0 >= sep) else 1
            elif h1 - prev >= sep:
                n += 1
            prev = h1
            m += 1
    return n


def pattern_rows(ev, off, P, t1, t2, L, sep):
    P = np.asarray(P, dtype=np.int64)
    k = len(P)
    m = _rows(ev, off, P, k, t1, t2, L, np.zeros((1, 5), np.int64), False)
    out = np.zeros((max(m, 1), 5), dtype=np.int64)
    _rows(ev, off, P, k, t1, t2, L, out, True)
    keep = _sep_keep(out[:, 0], m, k, sep)
    return out[keep, :k]


@njit
def _chains(ev, off, cell_of, t1, t2, k, mode, keys, maxn):
    """Keys of the k-cell patterns realised by at least one chain of events.

    mode 0: ascending cells, 1: descending cells, 2: any order of distinct cells.
    Keys pack the cells in 6 bits each.
    """
    n = 0
    E = len(ev)
    order = np.argsort(ev)
    tev = ev[order]
    tcell = cell_of[order]
    stack_i = np.zeros(k, dtype=np.int64)
    for s in range(E):
        # depth-first over chains starting at event s
        stack_i[0] = s
        depth = 0
        nxt = np.zeros(k, dtype=np.int64)
        lo0 = np.searchsorted(tev, tev[s] + t1, side="left")
        nxt[1] = lo0
        while depth >= 0:
            if depth == k - 1:
                key = 0
                for d in range(k):
                    key = key * 64 + tcell[stack_i[d]]
                if n < maxn:
                    keys[n] = key
                n += 1
                depth -= 1
                continue
            j = nxt[depth + 1]
            cur = stack_i[depth]
            hi = tev[cur] + t2
            advanced = False
            while j < E and tev[j] <= hi:
                cj = tcell[j]
                ok = True
                cprev = tcell[cur]
                if mode == 0 and not cj > cprev:
                    ok = False
                elif mode == 1 and not cj < cprev:
                    ok = False
                elif mode == 2:
                    for d in range(depth + 1):
                        if tcell[stack_i[d]] == cj:
                            ok = False
                            break
                if ok:
                    nxt[depth + 1] = j + 1
                    depth += 1
                    stack_i[depth] = j
                    if depth + 1 < k:
                        nxt[depth + 1] = np.searchsorted(tev, tev[j] + t1, side="left")
                    advanced = True
                    break
                j += 1
            if not advanced:
                depth -= 1
    return n


def candidate_patterns(cells, k, t1, t2, orders="code"):
    """Patterns with at least one chain (a superset of those that can pass)."""
    ev, off = flatten(cells)
    cell_of = np.repeat(np.arange(len(cells)), np.diff(off)).astype(np.int64)
    modes = (0, 1) if orders == "code" else (2,)
    pats = set()
    for mode in modes:
        maxn = 1_000_000
        while True:
            keys = np.zeros(maxn, dtype=np.int64)
            n = _chains(ev, off, cell_of, t1, t2, k, mode, keys, maxn)
            if n <= maxn:
                break
            maxn = n
        for key in np.unique(keys[:n]):
            p = []
            for _ in range(k):
                p.append(int(key % 64))
                key //= 64
            pats.add(tuple(p[::-1]))
    # repeats of one cell (the code's [i i ...] rows)
    reps = [tuple([c] * k) for c in range(len(cells)) if len(cells[c])]
    return sorted(pats), reps


@njit
def _shift_all(ev, off, shifts, L):
    out = np.empty_like(ev)
    for c in range(len(off) - 1):
        seg = ev[off[c]:off[c + 1]]
        s = ((seg - 1 + shifts[c]) % L) + 1
        out[off[c]:off[c + 1]] = np.sort(s)
    return out


@njit
def _count_many(ev, off, pats, ks, t1, t2, L, sep):
    res = np.zeros(len(pats), dtype=np.int64)
    for i in range(len(pats)):
        res[i] = count_pattern(ev, off, pats[i, :ks[i]], ks[i], t1, t2, L, sep)
    return res


@njit(parallel=True)
def _null_counts(ev, off, pats, ks, t1, t2, L, sep, shifts):
    """Counts of every pattern in each shuffle; shifts is (n_shuffle x cells)."""
    out = np.zeros((shifts.shape[0], len(pats)), dtype=np.int64)
    for r in prange(shifts.shape[0]):
        evs = _shift_all(ev, off, shifts[r], L)
        for i in range(len(pats)):
            out[r, i] = count_pattern(evs, off, pats[i, :ks[i]], ks[i], t1, t2, L, sep)
    return out


def detect(cells, L, t1=0.05, t2=2.0, sep=0.05, min_rep=4, lengths=(2, 3, 4, 5),
           n_shuffle=1000, centile=0.95, orders="code", single_cell=True, rng=None):
    """Significant patterns of one time slice, before the repetition rule's variants.

    Patterns are tested when they repeat at least `min_rep` times (the Methods'
    rule; the code's "more than" rule is applied after, in `finalize`, as it
    does not change any pattern's centile). Single-cell repeats are kept here
    and can be left out in `finalize`. Returns a list of (cells, count, rows)
    and counts of what was tested.
    """
    rng = np.random.default_rng(0) if rng is None else rng
    t1m, t2m = int(round(t1 * 1000)), int(round(t2 * 1000))
    sepm = sep * 1000
    ev, off = flatten(cells)
    cand = []
    for k in lengths:
        pats, reps = candidate_patterns(cells, k, t1m, t2m, orders)
        cand += pats + (reps if single_cell else [])
    info = {"candidates": len(cand), "passing_reps": 0, "significant": 0}
    if not cand:
        return [], info
    P = np.zeros((len(cand), 5), dtype=np.int64)
    ks = np.array([len(p) for p in cand], dtype=np.int64)
    for i, p in enumerate(cand):
        P[i, :len(p)] = p
    obs = _count_many(ev, off, P, ks, t1m, t2m, L, sepm)
    sel = np.flatnonzero(obs >= min_rep)
    info["passing_reps"] = len(sel)
    if len(sel) == 0:
        return [], info
    Ps, kss, o = P[sel], ks[sel], obs[sel]
    shifts = rng.integers(1, L + 1, size=(n_shuffle, len(cells)))
    null = _null_counts(ev, off, Ps, kss, t1m, t2m, L, sepm, shifts)
    cent = ((null < o).sum(0) + 0.5 * (null == o).sum(0)) / n_shuffle
    sig = np.flatnonzero(cent > centile)
    info["significant"] = len(sig)
    out = [(tuple(int(c) for c in Ps[i, :kss[i]]), int(o[i]),
            pattern_rows(ev, off, Ps[i, :kss[i]], t1m, t2m, L, sepm)) for i in sig]
    return out, info


def finalize(sig, min_rep=4, rule=">=", single_cell=False, dedupe="code"):
    """Apply the repetition rule, the single-cell choice and the double-counting step."""
    keep = []
    for cells_, n, rows in sig:
        if rule == ">" and not n > min_rep:
            continue
        if not single_cell and len(set(cells_)) == 1:
            continue
        keep.append((cells_, rows))
    return eliminate_double_counting(keep, min_rep, dedupe == "documented")


def eliminate_double_counting(seqs, min_rep, active=True):
    """eliminate_double_counting_v2: longer, then more repeated, sequences claim events first."""
    if not seqs:
        return []
    width = 5
    # unique-row order of the zero-padded sequences (MATLAB unique(...,'rows') sorts rows)
    padded = [tuple(list(np.array(s) + 1) + [0] * (width - len(s))) for s, _ in seqs]
    order0 = sorted(range(len(seqs)), key=lambda i: padded[i])
    S = [seqs[i][0] for i in order0]
    T = [np.unique(seqs[i][1], axis=0) for i in order0]
    lens = [len(s) for s in S]
    idx = sorted(range(len(S)), key=lambda i: -lens[i])               # stable, by length
    final = []
    for L_ in range(max(lens), 1, -1):
        h = [i for i in idx if lens[i] == L_]
        h = sorted(h, key=lambda i: -len(T[i]))                       # stable, by repetitions
        final += h
    used = set()
    for i in final:
        for j in range(lens[i]):
            valid = np.ones(len(T[i]), dtype=bool)
            for r in range(len(T[i])):
                key = (S[i][j], int(T[i][r, j]))
                if active and key in used:
                    valid[r] = False
                else:
                    used.add(key)
            T[i] = T[i][valid]
    return [(S[i], T[i]) for i in range(len(S)) if len(T[i]) >= min_rep]


def summary(seqs, n_cells):
    """Fig. 4D measures: sequences per cell, median repetitions, % of cells in a sequence."""
    if not seqs:
        return {"n_seq": 0, "seq_per_cell": 0.0, "median_reps": 0.0, "pct_cells": 0.0}
    cells = set(c for s, _ in seqs for c in s)
    return {"n_seq": len(seqs), "seq_per_cell": len(seqs) / n_cells,
            "median_reps": float(np.median([len(t) for _, t in seqs])),
            "pct_cells": 100 * len(cells) / n_cells}


# ------------------------------------------------------------------ segments of the dandiset's files

READINGS = {"a": (0.05, 0.05), "b": (0.05, 0.0), "c": (0.0, 0.05)}
"""The claims file's readings of the paper's two 0.05 s rules: (a) both a 0.05 s lower bound
between successive events of a sequence and 0.05 s between the starts of repetitions, (b) the
first only, (c) the second only. Each is (t1, sep) in seconds; t2 is 2 s (Methods)."""

SEGMENT_S = 600.0


def event_times(x):
    """Event times (s) of each accepted cell with at least one event in the file."""
    ea = x["events"]
    fs = x["rate_ea"]
    times = [np.flatnonzero(ea[:, c] > 0) / fs for c in range(ea.shape[1])]
    keep = [c for c in range(ea.shape[1]) if len(times[c])]
    return [times[c] for c in keep], keep


def segments(x, task_reading="i"):
    """10-min slices of a file: spontaneous first 10 min and, where it lasts 20 min, the next 10;
    task first 10 min (reading i) or last 10 min (reading ii). A file shorter than 10 min is used
    whole."""
    dur = (x["events"].shape[0] - 1) / x["rate_ea"]
    if x["condition"] == "spontaneous":
        out = [("S1", (0.0, min(SEGMENT_S, dur)))]
        if dur >= 2 * SEGMENT_S - 1:
            out.append(("S2", (SEGMENT_S, 2 * SEGMENT_S)))
        return out
    if task_reading == "i" or dur <= SEGMENT_S:
        return [("RT", (0.0, min(SEGMENT_S, dur)))]
    return [("RT", (dur - SEGMENT_S, dur))]


def run_segment(x, ts, reading, rng, **kw):
    t1, sep = READINGS[reading]
    times, keep = event_times(x)
    cells, L = to_grid(times, ts)
    sig, info = detect(cells, L, t1=t1, sep=sep, rng=rng, **kw)
    # back to the file's cell indices
    sig = [(tuple(keep[c] for c in s), n, rows) for s, n, rows in sig]
    info.update({"L_ms": L, "cells_with_events": len(keep)})
    return sig, info
