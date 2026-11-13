**A. Outcomes** (22 claims in `park-2019.yaml`)

| Claim | My outcome | Reason |
|---|---|---|
| cell-counts | partially_reproduced | Cell 16 finds 115 head-direction cells from 13 rats under reading (a), and 110 pass the criteria under (b); both are within tolerance. The counts of 353 MEC cells and 556 pairs are blocked (data_missing): every TSD folder in the archive holds exactly the 115 head-direction units. Two per-rat counts differ from Table S1 (R029 40 vs 41, R523 2 vs 1). |
| hd-cell-rate | reproduced | Cell 18: 1.392 ± 0.207 AP/s in stable1 and 1.433 for the mean of the three trials, both within 1.41 ± 0.20. |
| fig1a-avoidance-learning | blocked (data_missing) | I checked the zip's member list: the DAT folders hold only the 44 recording sessions (SA1, SA2, and the rotating or TF trial in room and arena frames, 176 .dat files). There are no pretraining or training sessions, so no part of the claim can be tested. |
| fig1c-speed | reproduced | Cell 26: speed is lower in stable2 than in every other condition (p < 1e-4) under every reading. The other three conditions do not differ in reading a_filtered, in the clean variant, or with the between-groups Tukey. In unfiltered reading a with the repeated-measures Tukey, room vs arena gives p = 0.048. |
| fig1c-lfp-power | blocked (data_missing) | The archive holds no LFP (member list checked). |
| fig1c-firing-rate | reproduced | Cell 20: F(1.35, 154.10) = 1.76, p = 0.184 (paper: F(1.34, 153.21) = 1.89, p = 0.17). The clean variant gives p = 0.186. |
| fig1c-directionality | reproduced (fragile) | Cell 22: GG-corrected p = 9e-34; the repeated-measures Tukey gives S1 = S2 and S1 > RR, S2 > RR (p = 0.0019) and RR > RA, all at p < 0.01. The decisive pair S2 > RR fails with the between-groups Tukey (p = 0.055) and in the clean variant (p = 0.42). |
| fig1d-preference-change | partially_reproduced | Both ANOVAs are significant (p = 6.6e-8, p = 5.6e-12) and all three Dunnett tests are below 0.05. The order is the reverse of the legend's: stable1 vs arena frame has the largest change (91° against 58° and 60°), not the smallest. |
| fig1d-instability | partially_reproduced | Both ANOVAs are significant under both readings. "Every pair > halves" fails: stable1 vs room frame gives Dunnett p = 0.127 (counts) and 0.63 (rates), and stable1 vs stable2 gives 0.21 (rates). |
| fig2-decoding-stable-vs-rotating | reproduced (fragile) | Cell 32: 7 ensembles. Stable2 error is below the arena-frame error in 4 of 7 and below the room-frame error in 5 of 7, for both measures and both windows. The arena count meets the threshold only through 1022R029 and 1023R029. |
| figs2-frame-preference | reproduced (fragile) | Cell 38: 4 room and 2 arena under 1 of the 16 readings (45° bins, rotating trial, SD of ΔIdir, p05 margin). 14 of 16 readings have more room- than arena-preferring ensembles. |
| fig2c-proximity-anticorrelation | partially_reproduced | Cell 40: the mean r is negative under every reading (-0.05 to -0.09), but outside both tolerances (-0.141 ± 0.029, -0.132 ± 0.024). Only 7 to 10 of 14 correlations are negative with p < 1e-4. |
| figs3-no-head-direction-bias | reproduced | Cell 42: with 10° bins, rotating-trial probabilities and n = sum of weights, all 14 tests have p ≥ 0.346 and mean r = 0.166 (expected 0.17 ± 0.02). |
| fig3-hd-pair-correlations-preserved | reproduced | Cell 30: p = 0.906, 0.72 and 0.617 at 40, 250 and 1000 ms; the clean variant agrees. |
| figs4-all-pair-correlations-preserved | blocked (data_missing) | The archive has no non-head-direction cells (115 files per TSD folder). |
| figs5-hd-cells-high-model-information | blocked (data_missing) | Same reason; the 921 modelled cells are not deposited. |
| figs6-subclass-correlations-preserved | blocked (data_missing) | Same reason; it also depends on figs5. |
| no-angular-velocity-tuning | not_reproduced | Cell 28: more cells are significant than chance under every reading (signed, 30 Hz: 12 of 115, binomial p = 0.013; unsigned: 49 of 115). The rest on the criterion's per-sample test, whose p values ignore autocorrelation; all \|r\| < 0.07. |
| fig4-internal-tuning-preserved | not_reproduced | Cell 44, main readings: the KLD tests give repeated-measures p = 8e-5 and one-way p = 0.026; the criterion needs all four tests at p ≥ 0.05. All variants that use every pair fail too. Only the clean variant passes all four (0.099, 0.228, 0.227, 0.744). |
| fig4c-arena-registration-short-lived | not_reproduced | Cell 46: the ANOVA is significant at 10 s (p = 0.011). Under no variant is the arena frame below the room frame at 20 to 60 s; the room frame falls instead (at 20 to 40 s it is below the arena frame). |
| fig5-error-inhomogeneous | not_reproduced | Cell 34: error r is 0.17 (room) and 0.014 (arena, p = 0.06) pooled, against 0.589 and 0.653. No reading or window comes within tolerance. |
| fig5c-error-minima-at-cues | reproduced (fragile) | Cell 36: with 660 ms windows, pooled ensembles and reading (a), the minima fall at 105° and 345°, within ±10° of 110° and 350°. No other window, pooling or reading matches, and the two minima (63.2, 63.3) are barely below the rest of the curve. |

**B. Problems**

1. [affects a conclusion] Cells 32 to 46. Cell 8 says every analysis that uses a rotating or stable2 trial shows a clean variant. Decoding, Idir, proximity, Figure 5 and fig4c do not. 1023R029 is one of the seven ensembles, and its rotating tracks lag the tracker by up to 1500 samples (cell 12). It counts toward the fig2 thresholds (S2 below RA in 4 of 7), is classed "arena" in the only matching figs2 reading, and enters the fig2c, fig5 and fig5c pools. The pairs from the four R029 sessions with warped rotating tracks also enter fig4c.
2. [affects a conclusion] Cells 22 and 44: the outcome flips between the as-deposited data and the clean variant (fig4 fails as deposited and passes clean; fig1c-directionality loses S2 > RR when clean). The notebook never says which governs. I used as-deposited, since n = 142 pairs matches the paper.
3. [affects a conclusion] `hc20.tukey_rm` is made the main post hoc by the author. The paper names Tukey-Kramer, which in JMP is the between-groups procedure. For directionality, S2 vs RR is p = 0.0019 under one and 0.055 under the other. Both are shown, but the choice of main is not marked as an assumption.
4. [affects a conclusion] Possible misreading in the claims file, fig5. The paper compares the "polar distribution of directional error" with the sampled head-direction distribution by Kuiper's test, and Figure 5C places its minima at 110° and 350° "in the room frame". That suggests a distribution over head direction, as in fig5c reading (a), not the Rayleigh test on signed error angles. No such reading was run.
5. [affects a conclusion] Cell 38 (figs2): the one matching reading depends on 1117R157 classed "room" with p+ = 0.054 against p− = 0.030, and on 1121R157 classed "arena" with 0.041 against 0.061, both straddling the 0.05 margin. It also depends on the warped 1023R029.
6. [affects a conclusion] Cell 32 (fig2): the 5-minute-shifted reference shows stable2 decoding at chance in 1026R157 (135° against 134°) and 1117R157 (102° against 102°), and near chance in 1121R157. The paper reports one ensemble with poor stable2 decoding; here there are three or four. Under the criterion the claim still passes, on that thin margin.
7. [affects a conclusion] Cell 44: at 5 s, KLD from stable1 is lower in the arena frame than in the room frame (0.156 vs 0.214). The two frames share identical spikes and differ by at most 30° of rotation over 5 s, and this gap drives the significant KLD ANOVA. The notebook does not check it.
8. [does not affect a conclusion] `internal_tuning`, `norm="sum_offsets"`: dividing by the sum of offsets is a single scale factor per curve. KLD is computed on counts and the argmax and Rayleigh length do not depend on scale, so the main reading is the raw displacement histogram. Its "strength" (about 0.7 at 3 s in every condition) then reflects how slowly head direction changes, more than the cell pairs. This follows the Methods but is not stated.
9. [does not affect a conclusion] Cell 26: the 100 cm/s speed filter is the author's own choice (labelled "standard"). The result holds without it under the between-groups Tukey and in the clean variant. There are 44 sessions, where the paper's degrees of freedom imply about 38.
10. [does not affect a conclusion] Cell 28: the binomial criterion with per-sample p values is anticonservative and confounded by how head direction is sampled. The criterion fixes this test, so the not_reproduced outcome rests on it, as the claims file says.
11. [does not affect a conclusion] `decode` labels each estimate by its bin start, as the paper's code does, which biases error by about -5°. I confirmed this on synthetic cells (median absolute error 12°, mean signed error -5.3°).
12. [does not affect a conclusion] Cell 40: each shock zone is taken as the centre point of its sector. The assumption is stated, but it may weaken the proximity correlations.

Helper checks on synthetic data, all passed: `rm_anova` F matches statsmodels AnovaRM, and its GG epsilon matches the double-centred covariance formula. `rayleigh_p` and `kuiper_two` give false-positive rates of 0.055 and 0.049 under the null. `tukey_rm` has a familywise rate of 0.058. `internal_tuning` matches a brute-force loop for both window sides. `kld` gives 0 for identical curves.

**C. What I could not check, and the outputs that would settle it**

- Whether fig2, figs2, fig2c, fig5, fig5c and fig4c survive without 1023R029 and the other flagged sessions. A clean variant of each would settle it.
- The cause of the arena-vs-room KLD gap in fig4: per pair, the number of spikes with a valid direction in each frame, and the KLD between the room-frame and arena-frame histograms directly.
- Robustness of the fig5c minima: the full 36-bin curve of mean absolute error by head direction, the third-deepest minimum, and a null for the minima positions (for example, errors circularly shifted against head direction).
- fig5 under the head-direction reading of problem 4: the head-direction distribution of accurately decoded windows, with its Rayleigh and Kuiper tests.
- The Table S1 per-rat differences (R029, R523): the session dates and file headers of 1001R523 and 1001R029.
- The paper's 38 speed units: no output identifies which sessions the paper used.

For the blocked claims, the archive's member list (data.zip central directory, `filelist.txt`, `checksums.md5`) confirms that no part of fig1a, the LFP claim, figs4, figs5 or figs6 can be tested.
