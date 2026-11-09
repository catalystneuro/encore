## Verifier report, round 3: Lohani, Moberly et al. 2022 on dandiset 001172 (0.260129.0829)

The claims file has 26 claims. The attempt record has 26 outcomes, and one of them carries a proposed change of outcome: fig2c-face-best-predictor-calcium. I reviewed only that one. I downloaded the paper text again (PMC10661869, BioC JSON and plain text) and saved it under `paper/`.

| Claim | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| fig2c-face-best-predictor-calcium | reproduced | yes | none | See below. |

**The numbers come from the data (cells 27, 33, 36).** Cell 27 fits the models per session on the file's ΔF/F, and the wheel predictor is the stored WheelSpeed (`wheel_frame`). Cell 33 averages the single-variable R² over the 23 left parcels per mouse, sets negative values to 0 and applies Friedman's test, with an exact p. In cell 36, face PC1 has the highest single-variable R² in all 4 mice:

- Face PC1 over wheel by 0.053, 0.016, 0.026 and 0.017.
- Means: face 0.112, wheel 0.084, pupil 0.010.
- Friedman χ² = 8.00, p = 0.018 (exact p = 0.0046).

The record's notes match these outputs. They also match the unique-contribution values (face 0.058, pupil 0.025, wheel 0.014; face largest in all 4 mice, by 0.002 over pupil in grabAM05; p = 0.039).

**The criterion is applied as written.** The criterion says reproduced when Friedman p < 0.05 and face PC1 has the highest single-variable R² in every mouse. Both hold. By the criterion, the unique contributions do not change the outcome.

**The signed-speed choice was not made to reach the result (cell 26; cells 41 and 42).** The choice follows the sources, not the outcome. I checked the Methods text again: "locomotion speed was computed as a differential of distance (cm/s)" after circular unwrapping, which keeps the sign. The code's `wheel_changepoints.m` uses a signed `db1SpeedMpS`. Cell 15 shows that the code's change-point method, run on the file's WheelSpeed, recovers every WheelActivation epoch to the sample.

The comparison with the paper's own `Fig2RawData.mat` (cells 41 and 42) also points to signed speed:

- Row 1 matches grabAM05 by full-model R² across parcels (Spearman 0.98 for ACh, 0.94 for calcium).
- In that row the calcium wheel R² is 0.0246. Here it is 0.0253 with signed speed and 0.0483 with |speed|.
- The ACh wheel R² gives the same picture: 0.0014 in the file, 0.0017 signed, 0.0031 with |speed|.

In grabAM07 and grabAM08 the two readings are closer to each other than to the file, so those mice do not decide it. The record says so correctly.

**Caveats.** These do not change the outcome:

- The outcome depends on how the wheel predictor is read. With |speed|, wheel beats face in grabAM06 (0.147 against 0.142, cell 38) and the claim would be partial. Cells 39 and 43 and the record state this openly.
- The external support from the paper's file rests on one mouse, grabAM05.
- The paper's file itself has face PC1 as the best single variable for calcium in all 6 mice (cell 41).
