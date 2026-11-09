**Verification report, round 1: Jackson et al. 2019 (eNeuro 0151-19.2019) on OpenNeuro ds002778 v1.0.5**

The claims file has 24 claims. The notebook tests all 24 and blocks none. My outcomes: 9 reproduced, 9 partially reproduced, 6 not reproduced, 0 blocked.

How I checked:
- I recomputed W, p, d and Spearman r from the per-patient values the notebook prints. They match to rounding.
- The helpers behave correctly on synthetic signals:
  - A sawtooth with a slow rise gives a negative rise-to-fall ratio.
  - Cusp-shaped peaks give a positive peak-to-trough ratio, and a sine gives about 0 for both.
  - Coupled PAC is 0.32 and uncoupled PAC is 0.002.
  - The FFT high-pass equals scipy's filtfilt to 2e-13.
  - `fdr_bh` equals statsmodels' BH.
- I queried the archive's file list. It has 331 files, with no artifact or bad-segment marks, every channels.tsv says "good", and events.tsv holds only a start trigger. So readings (a) and (b) for artifact rejection and noisy electrodes are the same here.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| fig2-sharpness-off-on | partially_reproduced | FDR p 0.0228; off higher in 13/15; W 13 is within 10.8–13.2. d 0.731 is outside 0.774–0.946 (cells 14, 16). |
| fig2-steepness-off-on | partially_reproduced | FDR p 0.0249; d 0.701 is within tolerance. W 16 is outside 8.1–9.9 (cell 18). |
| fig2-pac-off-on | partially_reproduced | FDR p 0.0228 and raw d 0.851/0.863 are within tolerance. W is 13 (Methods filters) or 12 (code filters), both outside 13.5–16.5 (cell 20). Reproduced if the criterion's last sentence, which drops W, applies (problem 1). |
| bipolar-off-on | reproduced | All three FDR p < 0.05 with off higher: 0.0106, 0.0044, 0.0096 (code filters 0.0081). Only steepness approaches the paper's p < 0.004 bound (cell 22). |
| temporalis-f7f8-null | reproduced | p = 0.69, 0.17, and 0.10 (Methods) or 0.078 (code); none below 0.05 (cell 24). |
| temporalis-t7t8-null | reproduced | p = 0.36, 0.95, 0.11 (cell 25). |
| fig2c-topography-sensorimotor | partially_reproduced | Smallest p for sharpness is at P8, outside the sensorimotor set. Steepness (C4) passes. PAC (Methods filters) has its minimum at CP6, but F7 is significant uncorrected (0.041). That gives 2/3 measures under the FDR reading and 1/3 uncorrected (cell 27). |
| offctrl-sharpness-null | reproduced | z 0.47, p 0.635 (paper 0.91, 0.363) (cell 29). |
| offctrl-steepness | not_reproduced | z 2.37 and d 0.855 are within tolerance, but FDR p over Table 2 is 0.0531 under every filter reading. The bipolar single test (p 0.0177) would hold, but the criterion needs the average-reference result first (cell 31). |
| offctrl-pac-null | reproduced | p 0.323 (Methods) and 0.286 (code) (cell 33). |
| offctrl-pac-csd | not_reproduced | Rank sum p 0.075 under both filter readings (cell 34). |
| updrs-improvement | reproduced | "Total UPDRS": W 3.5, p 0.0033, matching the paper exactly (cell 36). |
| fig1c-beta-alpha-peaks | not_reproduced | The C3/C4 mean spectrum has no local maximum in 8–12 or 13–30 Hz for off or on; only controls have both. The all-electrode variant gives off a beta maximum only. The off group's maximum sits at 7.96 Hz, just below the window (cell 38). |
| table1-alpha-shape-off-on | partially_reproduced | Both FDR p < 0.05 (0.026/0.032). Sharpness W and d are within tolerance. Steepness W 21 is outside 10.8–13.2 under both alpha filter readings (cell 40). |
| table1-alpha-pac-null | not_reproduced | Readings disagree: FDR p 0.061 (a192) and 0.078 (b231) are null, but 0.036 (c118) is significant. The criterion asks for the outcome all readings give. d is 0.66–0.72 against 0.51 ± 0.05 in every reading (cell 42). |
| table2-alpha-offctrl | not_reproduced | Steepness z 2.45 and d 0.89 are within tolerance, but FDR p is 0.0531 under all readings. Sharpness and PAC are null as expected (cell 44). |
| pac-beta-larger-than-alpha | partially_reproduced | Raw PAC: p 0.015, beta difference larger in 12/15, but W is 17–18 against 9.9–12.1. The log-PAC variant is not significant. The criterion has no partial clause (cell 46). |
| fig3-sharpness-pac-correlation | partially_reproduced | Both r are positive and significant. Methods filters: off r 0.586 is out of tolerance. Code filters: on r 0.843 is out. No reading puts both within tolerance (cell 48). |
| fig3-steepness-pac-correlation | partially_reproduced | Code filters: off r 0.796 is within tolerance; on r 0.532 (p 0.041) is significant but out of tolerance. Methods filters: on r 0.446 is not significant (p 0.095) (cell 49). |
| fig4a-sensorimotor-q4 | reproduced | 48/60 points in Q4 (cell 51). |
| q4-patient-counts | not_reproduced | C3 10, C4 10, both 7, at least one 13, against 9/8/8/9 ± 1. C4 and at-least-one are out in either electrode order (cell 53). |
| fig4b-temporalis-variable-shape | reproduced | Both readings agree: most-common-quadrant share is 0.68 at F7/F8 against 0.80 at C3/C4, and RMS distance to the centroid is 0.093 against 0.076 (cell 55). |
| controls-q4 | reproduced | 25/32 points in Q4 (cell 57). |
| table3-q4-effect-size | partially_reproduced | d rises for all three measures under every reading. Q4 sharpness d 0.994 is within tolerance; steepness 0.817 and PAC 0.95–1.06 are out. All-patient PAC d matches 0.75 only for log10 PAC with Methods filters (0.731). The Q4 subset has 13 patients, not the paper's 9 (cell 59). |

The paper states no chance levels, so there was nothing to compare.

### B. Problems

1. **[affects a conclusion]** In the claims file, the fig2-pac-off-on criterion contradicts itself. It says "As for fig2-sharpness-off-on", which requires W and d within tolerance, and then "holds when the test holds under one reading and d is within tolerance". It also lists an expected W. With W out (13 and 12) and d in, the outcome is partially_reproduced or reproduced depending on which sentence governs. I applied the stricter reading.
2. **[affects a conclusion]** The table1-alpha-pac-null criterion assumes the three phase-filter readings agree; they do not (cell 42). The outcome rests on the reading: 2/3 readings reproduce the null. The notebook reports every reading but does not flag the disagreement.
3. **[affects a conclusion]** In table3-q4-effect-size (cells 53, 59), the Q4 inclusion set is 13 patients against the paper's 9, so the Q4 d values come from a different subset than Table 3's. The notebook compares them to Table 3 without noting this.
4. **[does not affect a conclusion]** Cell 12's markdown says "Total UPDRS" exceeds "UPDRS 18-26" by "0 to 14"; cell 11 prints 1 to 14. Its identification of "Total UPDRS" as Part III is asserted as "consistent with the values, not shown". The "total of all parts" reading is not computed separately, but the dataset holds no other part. W = 3.5 matches either way.
5. **[does not affect a conclusion]** Two on sessions, pd6 and pd16, were exported from preprocessed EEGLAB files. pd6 is already average-referenced; pd16 has electrode SDs about 6 times the others and a high cutoff of 256 Hz. Both stay in the main analysis. Exclusion variants appear only in cells 16, 18 and 38, not for PAC, the correlations or Q4. The ratio measures do not depend on scale, but whatever preprocessing those files carry is unknown.
6. **[does not affect a conclusion]** `pac_ozkurt` keeps the filter-edge samples, whereas pacpy's `firf` (rmvedge) drops them. This is a few hundred samples out of 90k or more.
7. **[does not affect a conclusion]** `csd` uses MNE's spherical spline on template biosemi32 positions instead of the CSD toolbox's lookup positions. This is a stated, reasonable assumption, but untested. offctrl-pac-csd misses at p 0.075, so a sensitivity check would be informative.
8. **[does not affect a conclusion]** The paper's artifact rejection and noisy-electrode exclusion cannot be reproduced; I verified the archive holds no marks. This may explain the out-of-tolerance W and d values, but it is not an error in the notebook.

### C. What I could not check

- **CSD against the CSD toolbox.** I could not confirm MNE's output equals the toolbox's. A comparison of the CSD transform on one recording, or C3/C4 spectra before and after CSD, would let me.
- **The pd6 and pd16 sessions.** Whether they were artifact-cleaned or filtered differently is unknown. Off-on PAC, the correlations, the Q4 counts and Table 3 rerun without these two patients would show their influence.
- **Q4 membership.** Which patients the paper's 9 Q4 cases are is unknown, so I could not tell why the counts differ. Per-patient PTR/RDR values at C3 and C4 would help localise the gap.
- **Figure images.** I did not inspect the plots; I relied on the printed ranges, which show no points clipped.
- **Table 2's FDR method.** Whether the paper used BH for Table 2 is uncertain (its printed p = 1, noted in the claims file). offctrl-steepness and table2-alpha-offctrl hinge on BH giving 0.0531, so a sensitivity output under other correction procedures would show how fragile those two outcomes are.
