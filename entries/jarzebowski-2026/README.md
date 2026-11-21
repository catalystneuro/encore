# Jarzebowski & Bendor (2026) from dandiset 000713

Tests the findings of [Jarzebowski and Bendor (2026)](https://doi.org/10.64898/2026.06.26.734797) on
[DANDI:000713](https://dandiarchive.org/dandiset/000713/0.240702.1725), the Allen Institute's Visual
Behavior Neuropixels recordings, which the paper reuses, and on the paper's two-compartment model,
simulated from its Methods.

| Claims | Outcome |
|---|---|
| Model, Figures 1 to 4 (14 claims) | 11 reproduced, 1 partially reproduced, 2 not reproduced |
| Layer link to the CCFv3 annotation | Reproduced |
| Cell counts | Reproduced over the sessions of the optotagged mice; not over all sessions |
| Figure 5 and Figure S1 (bursting with repetition, omission and novelty) | 6 reproduced, 1 not reproduced |
| Figure 6 (omission against spontaneous activity) | 2 partially reproduced, resting on which spontaneous block is meant |
| Figure S2 (noise correlations) | 1 reproduced, 1 not reproduced |
| Figure 7 (running) | 2 reproduced, 1 partially reproduced, 1 not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Units carry no layer in the files; the layer comes from the CCFv3 annotation volume and the units'
CCF coordinates, so the claims on recorded data use this outside input. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/jarzebowski-2026-01.yaml`](../../attempts/jarzebowski-2026-01.yaml).

- `reproduce_jarzebowski_2026.ipynb`: the analysis. It takes about 25 minutes: four to nine to stream
  the 153 session files, four at a time, and six to run the claims on all 16 cell selections.
- `vbn.py`: streaming the sessions, per-window spike and burst counts, the CCF layer lookup, cell
  selection, and the mixed-effects model. Other notebooks on this dandiset can import it.
- `seta_model.py`: the two-compartment model of the Methods, in NumPy.
