# Vittani, Herlo, Wang et al. (2025) from dandiset 001414

Tests the astrocyte findings of [Vittani et al. (2025)](https://doi.org/10.1073/pnas.2422069122) on
[DANDI:001414](https://dandiarchive.org/dandiset/001414/0.250603.1324), which holds the raw one-photon
movies of the paper's LED, whisker and startle experiments, the arteriole movies with their kymograph
rectangles, and two-photon stacks. Each movie is streamed and reduced to its mean intensity per frame,
and the paper's pipeline (Blood Offset, photobleaching fit, dF/F0, peak, rise, 80% decay, duration) is
run under every reading the paper leaves open.

| Claim | Outcome |
|---|---|
| cAMP rises with LED length in anesthetized mice (Figure 1B, C) | Reproduced |
| cAMP kinetics against Table S1 (Figure 1G to J) | Reproduced |
| Recordings 1 and 4 alike (Figure 1F) | Reproduced, on an assumption |
| awake cAMP, bPAC against control, Table S1 values (Figure 3B) | Partially reproduced |
| awake cAMP stable across recordings (Figure 3C, D) | Not reproduced |
| awake against anesthetized kinetics | Not reproduced, on an assumption |
| no cAMP difference between IP3R2 genotypes (Figure 4A to E) | Reproduced, on an assumption |
| IP3R2 cAMP values (Table S1) | Not reproduced |
| Ca2+ in anesthetized mice (Figure 5B to D) | Partially reproduced |
| Ca2+ rise and decay times (Figure S4F, G) | Not reproduced |
| Ca2+ in awake mice (Figure 5E to G) | Not reproduced |
| Ca2+ reduced in IP3R2-/- mice (Figure 5H to J) | Partially reproduced |
| mild stimulation, cAMP and Ca2+ (Figure 6C to H) | Partially reproduced (two claims) |
| whisker cAMP grows with stimulation length (Figure S1P) | Not reproduced |
| histology, two-photon and startle claims (five) | Blocked: metadata insufficient |
| arteriole claims and those resting on them (twenty) | Blocked: too large for the run |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files hold raw movies only: no ROIs, stimulus times or traces. The ROIs were chosen here, and the
LED onsets are found from the light's step in the recording. Eight pairs of files hold identical
movies, and the rotated arteriole movies hold only 0 and 1. The attempt record, with the reasons and
the differences from the paper's method, is
[`attempts/vittani-2025-01.yaml`](../../attempts/vittani-2025-01.yaml).

- `reproduce_vittani_2025.ipynb`: the analysis. It streams 283 files (191 GB) and takes about 35
  minutes, nearly all of it streaming.
- `vittani.py`: parallel chunk streaming of the movies, the astrocyte signal pipeline and its
  readings. Other notebooks on this dandiset can import it.
