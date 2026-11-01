# Semenov, Kim, Silkuniene & Pakhomov (2025) from dandiset 001271

Tests the findings of [Semenov et al. (2025)](https://doi.org/10.1016/j.xcrp.2025.102660) on
[DANDI:001271](https://dandiarchive.org/dandiset/001271/0.250805.1352), which holds the Figure S2
experiment: optical membrane potentials of 20 cultured hippocampal neurons stimulated by 250-ms,
2-kHz sine waves before and after the solution was replaced by one with tetrodotoxin (6 neurons) or
without it. Findings the paper deposited elsewhere are tested on DANDI:001030 (Figure 3C), 001032
to 001035 (Figures 1 and 2) and 001272 (Figure S1).

| Claim | Outcome |
|---|---|
| TTX experiment replicated in at least 4 neurons, with vehicle controls | Reproduced |
| Before TTX, APs at lower fields and sustained depolarization at the highest | Not reproduced |
| Sustained depolarization reverses when the stimulus ends | Blocked: other |
| TTX abolishes the APs | Blocked: methods underspecified |
| TTX blocks the sustained depolarization | Blocked: other |
| Vehicle neurons keep firing and depolarization | Blocked: methods underspecified |
| Typical APs 11.3% dF high and 8 ms long | Blocked: methods underspecified |
| Adiabatic heating 2.5, 1.24 and 4.1 C | Blocked: methods underspecified |
| 2-s sine wave in NaGlu, firing for the whole wave, then block (001030) | Not reproduced |
| Pure sine waves excite every neuron, ceiling 60 to 90 Hz (001032 to 001035) | Not reproduced |
| 20-kHz thresholds about twice the 2-kHz ones | Not reproduced |
| Modulated thresholds higher; 2-kHz threshold 57.7 V/cm | Not reproduced |
| Modulated firing locks to the beats | Reproduced (assumption; criterion amended after a reader's answer) |
| Pure sine waves give more APs than modulated ones | Reproduced (assumption) |
| Low conductivity halves thresholds | Blocked: metadata insufficient |
| Di-8-ANEPPS in eight neurons gives the same effects (001272) | Not reproduced |
| Figures 4 and 6 strobe imaging, and the threshold depolarization estimate (three claims and one dependent) | Blocked: other |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files hold 16 x 16 crops of the soma with no outline, so the claims file's ROI readings are
used, and they often disagree. The claims file's measure of sustained depolarization finds none
in these recordings, where the plateaus are smaller than its levels; whether this measure and the
ROI readings suit the data is asked of a reader in `questions/001271.yaml`. The stated voltages give the paper's fields at 18 V/cm per V, not
the 36 the files state. DANDI:001034 duplicates 001032, and 001272 holds 3 of the paper's 8
Di-8-ANEPPS neurons. The record, with the reasons and the differences from the paper's method, is
[`attempts/001271-semenov-2025-01.yaml`](../../attempts/001271-semenov-2025-01.yaml).

- `reproduce_semenov_2025.ipynb`: Figure S2 on 001271, and the heating estimate. About six minutes.
- `reproduce_fig3c_001030.ipynb`: Figure 3C on 001030. About a minute.
- `reproduce_fig1_fig2_001032.ipynb`: Figures 1, 2 and S1 on 001032 to 001035 and 001272. About 18
  minutes in the last run, most of it streaming.
- `sinewave.py`: loading, ROIs, dF, AP detection and the session measures; other notebooks on these
  dandisets can import it.
