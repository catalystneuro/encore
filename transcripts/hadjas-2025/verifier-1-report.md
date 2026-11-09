**A. Outcomes**

The claims file has 25 claims. The notebook tests 21 and treats the 4 human-tissue claims as blocked. My tally: 12 reproduced, 5 partially reproduced, 4 not reproduced, 4 blocked.

| Claim | Outcome | Reason |
|---|---|---|
| cohort-sizes | not_reproduced | 10 of 16 counts match (cell 21); the criterion needs 12 to reproduce. The Anxa1 counts match 4 of 4 only if the unsuffixed recordings are taken as DLS, which is a variant. Even with the Vglut2 STN count explained (B4), the total stays below 12. |
| fig2-gaba-excited | reproduced | 1 s trains: STN t 3.86, p 0.0083; PPN t 9.19, p 3.7e-5 (cell 23). These match the paper's t 3.8 and 9.2. |
| fig2-gaba-frequency | reproduced | Friedman STN 21.00, p 0.00011; PPN 18.15, p 0.00041. 40 Hz is above 5 Hz in every mouse (cell 25). |
| fig3b-da-stn-250ms-peak | partially_reproduced | With the 0 to 2.25 s window the mean latency is 0.786 ± 0.204 s, outside 0.50 ± 0.03. The peak is after offset and the net response is positive (p 0.0083). The 0 to 1.25 s variant gives 0.492 ± 0.033, which matches the paper (cell 27). |
| fig3c-da-stn-duration | reproduced | Reading (a) p 0.0011; reading (b) chi2 12.93, p 0.0048, matching the paper's F 13.0, p 0.005. In 4 s trains, 0 to 0.5 s is above 3 to 4 s (p 0.00071, 11 of 11 mice) (cell 29). |
| fig3d-da-stn-frequency-ns | reproduced | Friedman chi2 4.20, p 0.24, the paper's exact values (cell 31). |
| fig3g-da-ppn-duration | not_reproduced | Readings (a), (b) and (c) give p 0.26, 0.25 and 0.46 (cell 33). The paper's F 11.5 with p 0.009 implies 3 df, which is reading (b), and that reading gives chi2 4.07. |
| fig3h-da-ppn-frequency-ns | reproduced | Greenhouse-Geisser RM ANOVA: F 1.35, df 1.85 and 14.8, p 0.287. The paper reports F2,15 = 1.35, p 0.28 (cell 35). |
| fig4cf-ts-dls-opposite | reproduced | The signs are as stated (TS 6/6 and 9/9 mice above 0, DLS 7/7 and 9/9 below 0). Interaction F 40.9 (STN) and 36.4 (PPN), p < 1e-4, equal to the paper (cell 37). |
| fig4dg-ts-frequency | reproduced | 6 of 6 tests hold, with statistics close to the paper (7.62/7.5, 13.76/13.6, 17.31/16.9, 19.8/20.0, 24.3/24.0, 23.3/23.2) (cell 39). |
| fig4eh-dls-frequency | reproduced | 6 of 6 tests hold, with 40 Hz below 5 Hz in each (cell 41). |
| fig4eh-dls-5hz-increase | not_reproduced | 1 s trains at 5 Hz: STN p 0.22, PPN p 0.13 (cell 43). The paper also cites the 4 s panels S3F and S3L. There the variant gives STN p 0.0006 but PPN p 0.07, so that reading would give partially_reproduced (B2). |
| fig4cf-dls-rebound | partially_reproduced | 1 s trains, 1 s after offset: PPN mean 4.53%, p 0.017; STN mean 0.87%, p 0.29 (cell 45). |
| figs3-terminals-opposite | reproduced | TS +8.96% (9 of 9 mice), DLS −4.41% (7 of 8), interaction p 0.00013 (cell 47). |
| fig5-vglut2-excited | reproduced | 4 of 4 tests show a significant increase. STN W 43 (p 0.0078) at 0.25 s and 1 s; PPN t 2.89 and 3.42 (cell 49). The 4 s results also match (W −5, p 0.82; t 2.56, p 0.03). |
| fig5-vglut2-frequency | reproduced | The 4 core tests hold: STN 0.25 s p 0.0036; PPN p 0.011, 0.0005, 0.001. STN 1 s and 4 s are not significant, as in the paper (cell 51). |
| fig5-anxa1-dls-inhibited | not_reproduced | 2 of 6 significant with the DLS labels, n 5 and 4 (cell 53). Every mouse decreases except one in PPN 4 s, so the failure comes from sample size (B3). The unsuffixed-as-DLS variant gives 6 of 6. |
| fig5-anxa1-dls-frequency | partially_reproduced | 5 of 6 tests hold with the DLS labels; PPN 4 s RM ANOVA p 0.24 at n 4 (cell 55). |
| fig5-anxa1-dls-rebound | partially_reproduced | STN p 0.0044 (5 of 5 mice above 0); PPN p 0.14 at n 4 (cell 57). |
| figs4-anxa1-soma-inhibited | partially_reproduced | 5 of 6 significant decreases with the SNc labels; STN 0.25 s p 0.16 (cell 59). The dual-mice variant matches all six of the paper's t and p values. No rebound is found in either set (p 0.53 to 0.8), so that part of the statement is not supported. |
| fig5-opposite-subtypes | reproduced | Vglut2 +6.54% and +9.35% against Anxa1 DLS −1.73% and −1.48%. Welch p 0.0066 (STN) and 0.0032 (PPN) (cell 61). |
| fig1de-th-anxa1-reduced | blocked (data_missing) | Human tissue counts. The archive holds only mouse data (see C). |
| fig1f-anxa1-de-enriched | blocked (data_missing) | As above. |
| figs1-calb1-aldh1a1-counts | blocked (data_missing) | As above. |
| figs1-if-aldh1a1 | blocked (data_missing) | As above. |

**B. Problems**

1. [does not affect a conclusion] `response_measures` / `trial_matrix`: for 1 s trains the pre-stimulus window (−1 to 0 s) is the same as the baseline window, so `pre` is always 0. Every "paired" 1 s test is therefore a one-sample test against 0, and in `mixed_2x2` the site F equals the interaction F (cells 37, 47). The paper shows the same pattern (F 40.9 and 40.8), and reading (b) of fig3c adds a column of zeros. The notebook never says this.
2. [affects a conclusion] fig4eh-dls-5hz-increase, cell 43: the criterion uses 1 s trains, but the paper's sentence cites Figure S3F and S3L, which are the 4 s DLS panels. It explains the effect as summation over successive pulses, which fits longer trains. The 4 s variant is already printed; the notebook should say which panel each reading follows.
3. [affects a conclusion] fig5-anxa1-dls-inhibited, cell 53: with n = 5 the smallest two-sided Wilcoxon p is 0.0625, and with n = 4 it is 0.125. So three of the six tests cannot pass whatever the data show. The paper's W = −36 and W = −55 equal −n(n+1)/2 for n = 8 and n = 10, and t 6.4 with p 0.0004 needs df 7. The paper therefore analysed 8 and 10 DLS mice. The variant with the unsuffixed recordings added does not reproduce these statistics (t 2.65, W −34 and −51), so those recordings are not the paper's DLS data. The outcome reflects data missing from the archive, which the notebook never states as such. The same small samples limit fig5-anxa1-dls-frequency: the paper's F2,15 for PPN 1 s implies n ≈ 10, against 4 here.
4. [does not affect a conclusion] Vglut2 STN count (cell 21): the dandiset has 9 mice and the legend says 10. The paper's W = 41, 43 and −5 with p 0.012, 0.008 and 0.82 are the exact values for n = 9; with n = 10 they would be 0.037, 0.027 and 0.85. This mismatch is a legend error, not missing data. Not checked in the notebook.
5. [does not affect a conclusion] fig5-vglut2-frequency, cell 51: for PPN the Friedman test keeps only complete rows, 7 of 10 mice, because three files lack 5 Hz trains (cell 7: 126 of 129 files). The paper's χ² 24.8 needs at least 9 mice, since the maximum is 3n. So these 5 Hz trials exist in the lab's data but not in the archive. The notebook does not say which mice are dropped.
6. [affects a conclusion] fig3b, cell 27: two mice (C4217 and B8612) peak at 2.03 s and 2.24 s, at the end of the 2.25 s window. They raise the mean latency from about 0.49 s to 0.79 s. The notebook does not inspect those two traces.
7. [does not affect a conclusion] figs4-anxa1-soma-inhibited, cell 59: the dual-mice variant matches the paper to two digits (3.13/0.035, 3.98/0.016, 7.26/0.002, 4.72/0.018, 8.35/0.004, 3.33/0.045). This identifies the paper's sample. The stated rebound is not found.
8. [does not affect a conclusion] There are inconsistencies inside the paper that the notebook partly flags (cells 41, 55). F1,11 is impossible for a one-way RM ANOVA in 7 mice. Friedman F 11.5 with p 0.0002 and F 15.5 with p 0.015 do not fit 3 df. The Figure 5 legend (N, O) says Anxa1 STN shows no frequency effect, while the Results report significant ones; the notebook does not note this.
9. [does not affect a conclusion] I tested the helpers on synthetic inputs. `rm_anova` (F, ε, GG p), `mixed_2x2` (site and interaction F) and `friedman` agree with pingouin and scipy. `wilcoxon_w` gives W −15, p 0.0625 for five negative differences. On a step input the windows give during 5, pre 0, post 0. The AUC includes the sample at t = duration, which has a negligible effect.
10. [does not affect a conclusion] Every number derives from the loaded files, the train and pulse checks are sound, no random numbers are drawn, and there is no training or test split, so leakage does not apply. Units are percent dF/F, inferred and confirmed by recomputation (cell 11).

**C. What I could not check**

- Blocked claims: the archive's 290 assets are 258 mouse photometry NWB files and 32 behaviour videos (mp4, sub-C4550 to C4608). `assetsSummary` lists only Mus musculus. No part of the four human claims can be tested from the dandiset. The paper's Supplemental Tables 2 and 3 list per-case counts, but they are outside the dandiset.
- fig3g: the clock-check table (cell 13) has no input column, so I cannot tell whether the failing pan-DA recordings (13 of the 23) are PPN mice. Adding input to that table, and the fig3g result without those mice, would show whether a clock or alignment problem explains the failure.
- fig3b: plots of the C4217 and B8612 traces over 0 to 3 s would show whether their late peaks are rebounds or drift.
- fig5-vglut2-frequency: the ids of the Vglut2 PPN mice without 5 Hz trains are not printed. A list of mice and conditions dropped per test would let me confirm problem 5.
- DAterm DLS (8 against the paper's 9): the paper gives no test statistic that pins its n. A per-subject list for each group would show which mouse is absent.
