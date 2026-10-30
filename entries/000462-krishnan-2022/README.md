# Krishnan, Heer, Cherian & Sheffield (2022) from dandiset 000462

Tests the findings of [Krishnan et al. (2022)](https://doi.org/10.1038/s41467-022-34465-5) that can be
tested on [DANDI:000462](https://dandiarchive.org/dandiset/000462/0.230416.2132), which holds raw suite2p
fluorescence and behaviour (position, reward, licks) of 10 of the paper's 12 wild-type mice in the
reward extinction task (Figures 1 to 3) and 4 of its 6 DAT-Cre mice with VTA DREADD inhibition
(Figure 4). The control mice, dark sessions, pupil data, tdTomato mice and VTA axon imaging are not
in it.

| Claim | Outcome |
|---|---|
| Lap counts per condition | Reproduced |
| Pre-licking lasts about 5 laps after reward removal | Not reproduced |
| Decoding fails later in UR, follows the lick stop, at all track positions (Fig. 1d, e, g) | Reproduced |
| Decoder R2 in R, RE high, RE low and RR (Fig. 1f) | Partially reproduced |
| Robust to the lick stop definition; lap-wise R2; not due to running speed (Supp. Figs. 4, 5) | Reproduced, partially, partially |
| Approach ratio; engaged lap counts | Not reproduced |
| Decoding in engaged laps; disengaged laps uniform | Reproduced |
| Population vector clusters (Fig. 2a) | Not reproduced |
| Remapping, overall and at all positions (Fig. 2c, d) | Partially reproduced |
| Place field fates (Fig. 2e); field numbers (Fig. 3a) | Not reproduced |
| Reliability (Fig. 3b) | Reproduced |
| Out/in ratio, width and intensity (Fig. 3b); all-mice medians (Supp. Fig. 11) | Not reproduced |
| Degradation at all positions (Fig. 3c) | Partially reproduced |
| Reward over-representation (Fig. 3d); reward zone field turnover | Not reproduced |
| Novel environment (Supp. Fig. 13) | Partially reproduced |
| DREADD running speed (Supp. Fig. 16); reliability and out/in (Fig. 4h) | Not reproduced |
| DREADD spatial correlation (Fig. 4f) | Partially reproduced |
| Saline slow laps (Supp. Fig. 18) | Not reproduced |
| DREADD over-representation (Fig. 4m) | Reproduced |
| Control mice, pupil, tdTomato and axon imaging claims (nine) | Blocked: data missing |
| Reward cells (Supp. Fig. 14) | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files hold raw fluorescence only, so dF/F, transients and place fields are computed here with
the rules of the paper's reference 75, an assumption; the fields come out 1.1 to 1.7 times as wide as the
paper's. Position has no scale in the files; the 30 Hz clock agrees with the 1.5 s pause after each
reward, yet laps take longer than the paper reports. Engaged laps are defined by the approach ratio
over the traversal of the track, which leaves 2 of the 5 R-UR-RR mice with enough engaged laps for
Figures 2 and 3 (the paper had 3 of 6). sub-014 lacks 6000 behaviour rows in the middle of the
file, located and corrected in the notebook, and the DREADD files carry an undocumented fluorescence
offset. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000462-krishnan-2022-01.yaml`](../../attempts/000462-krishnan-2022-01.yaml).

- `reproduce_krishnan_2022.ipynb`: the analysis. It takes about 13 minutes, most of it the per-mouse
  processing (two mice at a time).
- `krishnan.py`: loading the files, the condition boundaries, behaviour, dF/F, transients, the
  decoders and the place field search. Other notebooks on this dandiset can import it.
