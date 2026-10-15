# Knierim, McNaughton & Poe (2000) from dandiset 001754

Tests the findings of [Knierim et al. (2000)](https://doi.org/10.1038/72910) that can be tested on
[DANDI:001754](https://dandiarchive.org/dandiset/001754/draft), which holds sorted units, task
epochs, the original rate maps and the position at spike times of three rats recorded before and
during the Neurolab shuttle mission (STS-90). The paper is not open access: the claims come from
its abstract, the titles of its figures, and the dandiset's description of its findings.

The entry streams the draft of the dandiset, as last modified on 2026-10-14 at 21:55 UTC. The draft
was asked for: it holds a new conversion that addresses the findings of the first attempt, which
read version 0.260728.1352, and it is not yet published. A draft can change; the notebook prints
the time the draft was last modified when it runs.

| Claim | Outcome |
|---|---|
| A robust spatial code on the Escher staircase in flight | Not reproduced |
| The code covers each of the three orthogonal surfaces | Blocked: metadata insufficient |
| Spatial information in flight comparable to preflight | Reproduced |
| Abnormal spatial selectivity on flight day 4 | Reproduced |
| Place fields stable across sessions | Reproduced |
| Normal theta in flight | Blocked: data missing |
| Normal sharp waves and ripples in flight | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

On the draft, the rate maps are linked to their units, and the units, epochs, unvisited bins, lost
positions and spike-time resolution are documented. The flight-day-4 result changed from the first
attempt because the draft leaves out three rate maps that were identical copies of others; with
them the test gives p = 0.055, without them 0.024; without Rat2 it gives 0.035 on either version.
The shuffle test, calibrated with Poisson spike trains, gives 0.074 false positives over all flight
ES epochs and up to 0.21 in one session, and the flight-day-9 outcome is the same against those
rates. Rat2's units are still not spatially selective
with the position trace in any window, and whose position the trace is in Rat2's task epochs is
not established. The description still places the preflight recordings on a flat rectangular
track and reports EEG, which no file holds. The attempt records, with the reasons and the
differences from the paper's method, are
[`attempts/001754-knierim-2000-02.yaml`](../../attempts/001754-knierim-2000-02.yaml) (the draft) and
[`attempts/001754-knierim-2000-01.yaml`](../../attempts/001754-knierim-2000-01.yaml) (version
0.260728.1352).

- `reproduce_knierim_2000.ipynb`: the analysis. It takes about five minutes; its last code cell
  prints the run time.
- `neurolab.py`: loading the files, the original rate maps and their spatial information, and the
  spike-based spatial information with its shuffle test. Other notebooks on this dandiset can import
  it.
