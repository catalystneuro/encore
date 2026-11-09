**Verifier report, round 1: Guan et al. 2022, DANDI:000252 @ 0.230408.2207**

The claims file has 19 claims. The notebook tests 11 and treats 8 as blocked (data_missing).

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| tenfinger-recording-counts | reproduced | Before the exclusion (cell 10, O1 none): N-PPC has 10 sessions, mean 111.4 (102–119); J-PPC 159.5 (159–160); J-MC 129.5 (120–139). The 139 is within 10% of the paper's 130. Every session has 100 trials. Under O1 a/b the N-PPC mean (94.3/93.0) is out of tolerance. |
| tenfinger-pooled-npcc-neurons | reproduced | 1114 before the exclusion (cell 10), against 1111 ± 111. It is 943/930 under O1 a/b, which is out of tolerance. |
| tenfinger-discriminative-fraction | not_reproduced | Under every O1 reading (cell 12): N-PPC 40–49%, J-PPC 38%, J-MC 64–66%, against 66/57/78 ± 10%. None of the three is within tolerance. Uncorrected p and FDR per session are also far below. |
| tenfinger-decoding-accuracy | reproduced | Every O1×O2 reading is within tolerance (cell 14). For example, O1a/O2a gives 72.2 / 69.5 / 78.5% against 70/66/75, with chance at 10%. |
| tenfinger-error-structure | reproduced | O1a/O2a gives 76.6 / 72.1 / 62.8% against 76±7.6, 66±6.6 and 68±6.8 (cell 14). O1a/O2b is also all within tolerance (74.9 / 67.1 / 64.6). |
| fig8b-matching-closer | reproduced | Under O4 (a), all O1 and O3 readings (cell 18): N-PPC 1.42–1.71 (BCa CI from 1.19–1.64), J-MC 2.99–3.38, J-PPC 0.19–0.22 with its CI including 0. This depends on the ×5 "precision of the mean" scaling (problem 1). Under O4 (b) and (a1) the sign and CI pattern hold, but the magnitudes are about 5× too small. |
| fig8a-npcc-index-distinct | reproduced | Under all 18 readings, in both hands, the index–middle and index–ring distances exceed middle–ring (cell 20). For example, R 2.16 / 2.96 > 0.62 and L 1.30 / 2.23 > 0.57. |
| fig8e-hand-ccgp | reproduced | Every array has p = 1/1002 (no shuffle reached the observed value) under all 8 readings. The CCGP/standard-accuracy ratio is ≥ 0.913, so both O9 (a) and (b) pass (cell 23). |
| fig8e-finger-ccgp | reproduced | N-PPC and J-MC have p = 1/1002 under all readings. Closeness passes O9 (b) (ratio > 0.55) but fails O9 (a) for J-MC (ratio 0.77–0.82) (cell 23). The outcome therefore rests on the O9 (b) reading. |
| jppc-finger-ccgp-low | partially_reproduced | p < 0.001 holds in only 1 of 8 readings (O1b/O6a/SVM: p = 1/1002, CCGP 38%, within tolerance). The other p values run from 0.002 to 0.038. The within-hand accuracy on the pseudo-population is 83–89% under every reading, against 65 ± 6.5. The per-session variant gives 69%, inside tolerance (problem 2). |
| figs11-jppc-lower-matched-size | reproduced | J-PPC is lowest at every size from 50 to 250 under all 4 O6×O7 readings (cell 26): about 0.25–0.33, against at least 0.47 for N-PPC and J-MC. |
| fig4c-contra-discriminative | blocked (data_missing) | I confirmed this against the archive: all 12 assets are "ten-finger press task, with delay", with 10 conditions and no No-Go. |
| fig4e-plan-vs-move | blocked (data_missing) | Same reason. A Delay-window ANOVA on the ten-finger task would be a different task and condition set, so not a test of this claim. |
| fig5a-contra-decoding | blocked (data_missing) | Same reason: there is no six-class contralateral task. |
| fig5bcd-npcc-data-requirements | blocked (data_missing) | Same reason. |
| fig5e-planning-decoding | blocked (data_missing) | Same reason. |
| fig6-online-bmi | blocked (data_missing) | There are no BMI sessions or decoder outputs. The trial table has no prediction column. |
| figs6-single-array-retrospective | blocked (data_missing) | The BMI sessions are absent. The archive's variableMeasured lists only ElectrodeGroup and Units, so there are no threshold crossings for O10 (a) either. |
| figs7-left-hand-bmi | blocked (data_missing) | Same reason. |

### B. Problems

1. [affects a conclusion] `crossnobis_rdm`, O4 "a" (cells 17–18). The per-partition precision is multiplied by the number of trials per condition (5). I tested this on synthetic data with a known distance: O4 a returns 5.46× the true value, while a1 and b return about 1.1×. The paper's 1.56 is matched only under this scaling.
   - The scaling follows rsatoolbox's documented convention for a list of noises, and I verified that docstring and code in rsatoolbox 0.3.2. So it is a defensible stated assumption, not an invention.
   - It is still an assumption that decides the magnitude part of fig8b. Without it fig8b would be partially_reproduced.
   - The claims file's O4 (a) does not mention it. That is a gap in the claims file, not an error in the notebook.
2. [affects a conclusion] `run_ccgp` / `standard_accuracy`, cells 21–23. The notebook computes standard (within-hand) accuracy on the pseudo-population, which is its own assumption, and runs the per-session accuracy only as a variant, for O1 a / O2 a alone.
   - The paper does not say which population it used. The criterion's O8 (a) does not settle it either, and the two choices change the jppc outcome: 83–89% on the pseudo-population against 69% per session (inside 65 ± 6.5).
   - Both should have been run as readings, under every O1/O6/O7 combination.
   - Under O1b/O6a/SVM with per-session accuracy, the claim would probably be fully reproduced, but that combination was not computed.
3. [affects a conclusion] The J-PPC finger-type p value is fragile (cell 23). It ranges from 0.001 to 0.038 across readings, and p < 0.001 is reached only at the 1/1002 floor, in one reading. The partially_reproduced outcome rests on that single reading.
4. [does not affect a conclusion] `run_ccgp`, O6 b. The observed CCGP is averaged over 100 matchings, but each null draw uses a single matching. This makes the null wider than the observed statistic's sampling distribution, so p is conservative. The notebook states it as an assumption.
5. [does not affect a conclusion] Cell 26 (figs11) runs only O1 a. The margins are large, so O1 b would not change the outcome.
6. [does not affect a conclusion] Cell 7 computes shuffled-label predictions (`Psh`) for the time course but never uses them. Only the per-session shuffled control is reported, and that control is sound: accuracy 0.07–0.17.
7. [does not affect a conclusion] The paper's per-session neuron counts match the pre-exclusion counts, not the post-0.5 Hz counts, yet all analyses use the post-exclusion counts (O1 a/b). This is consistent with the claims file's note on 466 against 472. The notebook does not comment on it.
8. [does not affect a conclusion] Helpers I checked and found correct:
   - `fdr_bh` matches statsmodels BH exactly.
   - `anova_eta2` matches scipy's `f_oneway` per unit.
   - `error_kinds` counts adjacent and matching errors correctly on a hand-built case.
   - `DiagLDA` is the pooled-variance Gaussian naive Bayes the paper describes.
   - There is no train/test leakage: the unit exclusion is label-free, and the zero-variance unit drop removes 1 unit.

### C. What I could not check, and which output would have let me

- **jppc-finger-ccgp-low with per-session accuracy.** I could not confirm the outcome under per-session within-hand accuracy for O1 b with O6/O7. The output needed is the per-session `finger_within` and `finger_both` accuracy for every O1×O6×O7 row of `ccgp_df`, printed next to `p_finger` and the finger CCGP.
- **fig8b scaling assumption.** I could not tell whether the paper's distances are in single-trial noise units (O4 b, a1) or fold-mean units (O4 a). One check would help: the per-session N-PPC mean RDM for O4 a1 alongside O4 a, compared with the Figure 8a colour-bar range. The paper's values are not in the text, so this stays open.
- **Ten-finger window for the discriminative fraction.** It is not reproduced in the Go window, and I could not test whether another window explains the gap. Only the 500 ms Cue, Delay and ITI variants were run (cell 12). Sweeping the window start through the Go phase would show whether any window approaches 66/57/78.
- **Exact p values.** These are shown rounded to 3 decimals. I inferred p = 1/1002 from the rounding: 2/1002 would print as 0.002. Printing the number of null values that reach the observed CCGP would settle it.
- **Blocked claims.** The archive's `Continues DANDI:000147` relation points to "PPC_Finger: human posterior parietal cortex recordings during attempted finger movements". It may hold N's contralateral-task data, but it is outside the dataset this claims file names, and I did not examine it.
