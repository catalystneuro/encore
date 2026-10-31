# Gao, Ramachandran, Yu & He (2025) from dandiset 000946

Tests the findings of [Gao et al. (2025)](https://doi.org/10.1523/jneurosci.2218-24.2025) that can be
tested on [DANDI:000946](https://dandiarchive.org/dandiset/000946/0.250829.1249), which holds sorted spike
times from S1, POm, auditory cortex (AC) and M1 of anesthetized rats during transcranial focused
ultrasound (tFUS) aimed at S1, M1 or POm.

| Claim | Outcome |
|---|---|
| AC neurons respond during sonication to 1500 and 3000 Hz PRF and after it to 30, 1500, 3000 and 4500 Hz, least to 300 Hz (Fig. 11B) | Partially reproduced (assumed normalization) |
| RSU and FSU responses and counts in S1 and POm (Figs. 4, 6 to 9; 24 claims) | Blocked: data missing |
| Sham and CG1 control (Fig. 5) | Blocked: data missing |
| Directional and undirected spike time tiling coefficients (Figs. 10, 11C, 11D; 8 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper splits units into regular-spiking (RSU) and fast-spiking (FSU) units by k-means on spike
waveform measures. The files hold no waveforms, and their `celltype_label` column, described as 1 = RSU
and 2 = FSU, is 0 for every unit, so every claim about RSUs or FSUs is blocked. Most recordings are
deposited twice; the notebook checks that the copies are identical and counts each once. No session is
marked as sham or as tFUS aimed at CG1. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/000946-gao-2025-01.yaml`](../../attempts/000946-gao-2025-01.yaml).

- `reproduce_gao_2025.ipynb`: the data check, the clock check and the Figure 11B analysis. It takes about
  five minutes, most of it reading the headers of all 1920 files and checking the duplicates.
- `tfus.py`: listing and reading the files, removing duplicate deposits, window spike counts and the
  normalized rates and tests of the paper. Other notebooks on this dandiset can import it.
