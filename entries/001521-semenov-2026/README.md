# Semenov et al. (2026) from dandiset 001521

Tests the findings of [Semenov et al. (2026)](https://doi.org/10.1016/j.bioelechem.2026.109283) that can
be tested on [DANDI:001521](https://dandiarchive.org/dandiset/001521/0.261006.1845), which holds the
Fluo-4 imaging of CHO cells after single 1-us pulses (Fig. 6A) and after 60-pulse 6 Hz trains (Fig. 6B).
The pulsed-laser potentiometric imaging of Figures 1 to 5 and 7 is not in it.

| Claim | Outcome |
|---|---|
| Clear Ca2+ entry after a single pulse at 1000 and 1200 V/cm | Reproduced |
| The Ca2+ signal stays elevated for 5 min | Not reproduced |
| No significant increase at 780 V/cm | Reproduced |
| Trains: 28% respond at 780 V/cm, nearly all above (224 cells) | Not reproduced |
| Trains: 2 cells (5.9%) respond at 650 V/cm, mean signal above zero | Not reproduced |
| Eq. 2: 2% and 12% IMP reduction for 10- and 100-fold conductivity | Partially reproduced (no recordings) |
| Potentiometric imaging, Figures 1 to 5 and 7 (21 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files give generator voltages, not field strengths, so every Fig. 6 claim is run under two readings
of the conversion; 3.9 V/cm per V, which fits the fields and group sizes of Fig. 6B, is adopted, and the
outcomes above hold under both. Unpulsed cells lose 12 to 16% of their Fluo-4 signal over a recording
(the raw cell signal, not the background), where the paper's Fig. 6A sham trace does not decline; this
decides the "stays elevated" claim. In the train session the same cells
were exposed at up to seven voltages, where the paper says each cell was tested once. The attempt record,
with the reasons and the differences from the paper's method, is
[`attempts/001521-semenov-2026-01.yaml`](../../attempts/001521-semenov-2026-01.yaml).

- `reproduce_semenov_2026.ipynb`: the analysis. It takes about four minutes, most of it streaming the files.
- `fluo4.py`: loading the files, the cell segmentation, the dF traces of Methods 2.4, and the two readings
  of the field conversion (3.9 V/cm per V adopted). Other notebooks on this dandiset can import it.
