# Knierim, McNaughton & Poe (2000) from dandiset 001754

Tests the findings of [Knierim et al. (2000)](https://doi.org/10.1038/72910) on
[DANDI:001754](https://dandiarchive.org/dandiset/001754/0.260728.1352), version 0.260728.1352,
which holds sorted units, task epochs, the original rate and occupancy maps and the position at
spike times of three rats recorded before and during the Neurolab shuttle mission (STS-90). The
claims (`claims/001754/10.1038-72910.yaml`) were written from the paper's full text.

The entry streams version 0.260728.1352, the most recent published version; the paper cites none.
The draft holds a new conversion that fixes several findings of the earlier attempts, but it is
not published and has changed since the second attempt read it, so it is not used.

| Claim | Outcome |
|---|---|
| Normal spatially specific firing in flight (`flight-spatial-code`) | Blocked: methods underspecified |
| Rat 2, FD9 spatial information as preflight (`si-comparable-to-preflight`) | Partially reproduced |
| Rat 1, FD9 spatial information as preflight (`si-rat1-fd9-vs-preflight`) | Blocked: methods underspecified |
| Rat 3, FD4 spatial information as preflight (`si-rat3-fd4-vs-preflight`) | Reproduced |
| Abnormal selectivity on FD4 in rats 1 and 2 (`fd4-abnormal-selectivity`) | Partially reproduced |
| Fields kept from session 2 to session 3 (`fig3-stability-across-sessions`) | Blocked: methods underspecified |
| Counterclockwise-only fields (`direction-selectivity`) | Blocked: methods underspecified |
| Normal theta (`theta-normal`) | Blocked: data missing |
| Normal sharp waves and ripples (`ripples-normal`) | Blocked: data missing |
| Representations on three surfaces (`three-orthogonal-surfaces`) | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Rat 2's flight day 9 cells do not differ from its preflight cells, but their mean spatial
information on the deposited maps (1.377 bits per spike) is above the paper's 1.13 +/- 0.09. For
rat 1 the outcome depends on which preflight epoch is compared (p = 0.50 against ES, 0.0055
against MC), which the paper does not say. On flight day 4 rat 2's cells carry less information
than preflight and rat 1's do not. Rat 3's session 2 has 16 active units (11 deposited maps), not
the paper's 7; more than half keep their field under one of the four readings of the stability
claim (6 of 11 maps by correlation) and not under the others, so it stays blocked. The questions
this attempt asked, and the reader's answers of 2026-10-20, are in
[`questions/001754.yaml`](../../questions/001754.yaml); the answers moved the direction claim from
data missing to methods underspecified and changed no other outcome.

On this version the rate maps cannot be linked to units, the Rat1 and Rat2 files share one
position trace, position is given only at spike times and none preflight, and no file holds EEG.
The attempt records are
[`attempts/001754-knierim-2000-03.yaml`](../../attempts/001754-knierim-2000-03.yaml) (this one),
and the deprecated
[`attempts/001754-knierim-2000-02.yaml`](../../attempts/001754-knierim-2000-02.yaml) (the draft)
and [`attempts/001754-knierim-2000-01.yaml`](../../attempts/001754-knierim-2000-01.yaml) (version
0.260728.1352).

- `reproduce_knierim_2000.ipynb`: the analysis. It takes about two minutes; its last code cell
  prints the run time.
- `neurolab.py`: loading the files, the deposited maps and their spatial information (reading
  M-a), maps recomputed from spikes (reading M-b), and the tests. Other notebooks on this dandiset
  can import it.
