**Verifier report, round 2: Rich, Liaw & Lee 2014 (CRCNS hc-31)**

The claims file holds 27 claims and the attempt record gives 27 outcomes: 18 reproduced, 3 partially reproduced, 5 not reproduced and 1 blocked. Four outcomes rest on an assumption (`assumed: true`): figs6, fig3c-lomax and figs11-no-boundary-remapping on the pass reading P-a, and fig4c on the spacing G-a. I could not check the claim that "Author, step 1.6" lets the author adopt a reading when the readings disagree, because I do not have the protocol. I take that as the record states it.

### 1. Outcomes

| Claim | Agree? | Note |
|---|---|---|
| cell-counts, fig1, fig2, fig2bc, fig3b-overdispersion, fig3b-negbin, fig3c-recruitment-fraction, fig3c-extrapolation, figs11-propensity-stationary, fig3e, figs16, fig4a, fig4b, figs8, figs17 | yes | Cells 20–105 support each one. fig3c-extrapolation is still fragile: 472 m, while F-b gives 447 m and the printed parameters 436 m. |
| figs3-cluster-quality (blocked) | yes | Cell 23: all four `spEpochSep` columns have 0 of 253 units finite. |
| figs7a (now reproduced) | yes | Cell 43: 5 of 5 under P-a. This depends on the 20 cm end allowance (see 3a). |
| fig3d (now reproduced) | yes, but fragile | Cell 59: KS 0.0315 against an upper bound of 0.033, so the margin is 0.0015. It rests on the 20 cm allowance. The first version of P-a gave 0.044 and P-b gives 0.0366, both outside. |
| figs6 (reproduced, assumed P-a) | yes, given P-a | P-b gives 1 of 5 groups (adjusted p 0.044). |
| fig3c-lomax (partial, assumed P-a) | yes, given P-a | KS 0.0600, K-b p 0.062. |
| figs11-no-boundary-remapping (not reproduced, assumed P-a) | yes, given P-a | P-a p is 0.026–0.045, close to 0.05. The data set's own fields (F-b) split by reading: H-a gives 0.039 and 0.040, H-b gives 0.066 and 0.060. By the criterion that is neither outcome, so the "not reproduced" is marginal. |
| figs10 (not reproduced) | yes | Cell 64: panel A fails T-a under both P-a and P-b, and the five extra null sets give 3–4 and 3 bins outside. The round-1 pass under P-b came from the shared random generator. Fragile: it is 3 bins against 2 out of 12, there is no check of the 30° bin edges, and F-b passes A. |
| figs12 (not reproduced) | yes | Cell 74. |
| figs14 (not reproduced) | yes | Cell 80: every F-a reading has a p below 0.05; the smallest per reading is 0.006 to 0.031. |
| figs15, figs5 (partial) | yes | Cells 83 and 98. |
| fig4c (not reproduced, assumed G-a) | yes, given G-a | Under G-a with K-a the difference is −0.013, and across the 10 seeds it reaches 0.000 (cell 95). So "lower under every reading" is within seed noise for K-a. |

**Assumptions:**
- **P-a:** it is stated, and the support is now reasonable. It overlaps 842 of the data set's 887 fields against 787, gives all 5 Fig. S7A means against 3, and matches the data set's pass counts better (exact 0.503 against 0.392; mean absolute difference 1.16 against 2.25). However, part of that advantage comes from the 20 cm end allowance, which was chosen after round 1 and never varied.
- **G-a:** it is stated, but the reasons are only partly apt. The "several orders of magnitude" quote is about the recruitment curve of Fig. 3C, not the simulation. The Fig. S18 phrase "small environments" refers to the low-rate condition. The case is plausible but not decisive.

**Claims-file issue (reported, not corrected):**
- **fig4c:** the criterion admits that "the fitted equal rate does not recruit all cells by 50 m, so it does not test the paper's statement". The paper's argument rests on equal rates recruiting all cells in large enough environments (main text, p. 817). So the judged comparison, a share of pairs above a level against the fitted rate, is a construction of the reader's that the claims file itself says misses the statement. Under it, the gamma-Poisson model also has a lower mean XOR for pairs over 10 m under both spacings (cell 95).
- **fig4b (minor):** the `checks` note still says the printed parameters give "under a factor of 4". That contradicts the amended criterion (5.5 and 4.4) and cell 92 (5.53 and 4.34).

### 2. Text against outputs

Every number I checked in the "**Result:**" cells, the Summary, the README and the attempt-record notes and responses matches the printed outputs. The README outcomes match the record. Three statements go beyond the numbers:

- **Cell 65** (and the record's figs10 notes, and the Summary): *"Panel B has little power: … the shuffle fills only 3 of the 1 m distance bins under Y-a and 8 under Y-b."* Eight of ten bins does not show little power for Y-b. The claim holds for Y-a only.
- **Cell 75:** *"so the positive correlation is what the uneven field density within each animal gives (ANM228900 alone differs from uniform …)"*. The variant null shows the correlation is consistent with uneven density, not that density is its cause. The parenthesis points to only one animal with a significant departure from uniform.
- **Cell 96** / fig4c deviation: the "several orders of magnitude" quote is given as support for G-a, but it describes Fig. 3C (see above).

The attempt record states my round-1 reasons accurately and in my own terms for all 27 claims, including problems 2, 4, 5, 6, 7, 8, 9 and 10 where they apply.

### 3. Round-1 points

**Resolved:**
- **2:** the end allowance was added; 72 fields lie at a section end.
- **3:** diagnosed. 29 missed fields fail the pass rule and 16 the width rule; 1 inch bins do not explain the gap.
- **4:** T-b is now marked not applicable for panel A.
- **5:** the centreline plot in cell 62 shows a zig-zag track with corners at its vertices, so the corners are not tracking noise.
- **6:** pairs on different tetrodes and a density-keeping null were added.
- **7:** RUN1 cluster info checked; all NaN.
- **9:** each animal's own section lengths are now used.
- All of section C was addressed.

**Recorded only:**
- **1:** P-a is now a stated assumption with better support, but the claims file's rule that the outcome is "the one all its readings give" still conflicts with the author choosing a reading.
- **8:** the open-field scale is unexplained, but it does not matter for figs8.

**What remains that bears on a conclusion:**
- **a. 20 cm end allowance (`EDGE_CM`) never varied:** it decides fig3d (margin 0.0015), contributes to figs7a (5 of 5), moved fig3c-lomax's KS from 0.0396 to 0.0600, and makes up part of the case for P-a.
- **b. figs10 panel A:** the outcome hinges on 3 of 12 bins against 2, with bin edges fixed at 0°. There is no check of bin offset or width, and F-b passes.
- **c. figs11-no-boundary-remapping:** it rests on P-a with p close to 0.05, and F-b is split by H reading.
- **d. fig4c:** the outcome rests on G-a, the K-a margin is within seed noise, and the criterion admittedly does not test the paper's statement.
- **e. F-a in-field rates:** they are lower than the data set's (4.76–5.02 Hz against 5.45 Hz) and this was not diagnosed. It probably drives figs15's 38–44% of fields kept (F-b keeps 50.7%) and part of figs14.
