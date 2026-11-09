**Verifier report, round 1: Johnson et al. 2019 (doi:10.3389/fnsys.2018.00065) on CRCNS fcx-3**

The claims file has 17 claims, and the notebook tests all of them; none is treated as blocked, so step 4 did not apply. I ran the helper's PSI and cluster-test code on synthetic data, using a scratch environment in `$TMPDIR` and no dataset files. I did not download the dataset or re-run the notebook.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| table1-electrodes | partially_reproduced | Cell 15 finds 187 channels against the paper's 192, because s4 has 5 parietal channels where Table 1 lists 10. It finds 1135 pairs against 1129. Both totals are within 10%, and the PFC mean is 19.0. |
| trial-counts | reproduced | Cell 17: correct trials 95.7 per subject; identity 32.1, spatial 32.9, temporal 30.7, all with ranges matching. Incorrect trials under reading (b) average 17.3 (4 to 25). |
| fig1b-accuracy | reproduced | Per-subject, per-condition accuracy runs from 0.625 to 0.975 (reading b). The logit mixed model on single trials gives p = 0.28, or 0.16 with two dummy terms. Both are above 0.05, though below the paper's p > 0.50. |
| fig1b-rt-identity-slower | reproduced | Reading (a): omnibus F(1,19) = 6.04, p = 0.024. Identity against spatial p = 0.005, identity against temporal p = 0.010, with identity longer in 7 of 7 subjects. Spatial against temporal p = 0.25. The F values sit just below the paper's bounds (6.50, 13.78, 10.95). |
| erp-no-condition-difference | reproduced | With adjacent neighbours, none of the 14 subject-contrasts has a cluster at p < 0.05 (smallest 0.053). With 0.025 per tail, none has one under any neighbour reading. With 0.05 per tail, the distance and no-neighbour readings each give one (0.028 and 0.033). 2 to 4 of 14 have p ≤ 0.10, against the paper's "all p > 0.10". |
| fig2-spatial-power | partially_reproduced | Counts of 5 and 2 match under the adjacent and distance readings. The percentages do not: 39.7 and 22.5 (adjacent) or 49.7 and 28.4 (distance), against 54 and 36. Every significant effect has p < 0.04. |
| fig3-temporal-power | partially_reproduced | Counts of 4 and 2 match only with adjacent neighbours, 0.025 per tail and assignment (b). The percentages are about 39 and 23 against 68 and 37. Other readings give counts within one subject. |
| power-difficulty-subjects | reproduced | Under reading (b)(i), every subject with an identity > other effect (s1, s4, s7, depending on the neighbour reading) has longer identity RT and lower identity accuracy. s3 also has both, so reading (ii) fails. This rests on power claims that are only partially reproduced. |
| power-low-frequencies | reproduced | Only one combination of the six (distance neighbours, mask reading (b)) meets every condition: 2–24 Hz larger than 25–40 Hz, and local maxima in both bands for all three effects. The result is fragile (problem 9). |
| fig4-maintenance-parietal-led | not_reproduced | Under P1 readings (a) and (b), the subject means are 0.03 and −0.12 (reading a) or −0.31 and 2.12 (reading b). No subject is below −1.96 in alpha-beta. Only the "code_rev" variant reaches the targets, and it is not a valid reading (problem 2). |
| fig4a-delta-theta-shift | partially_reproduced (by the letter of the criterion) | Reading (a): F = 1.2, p = 0.27, and 2 of 7 subjects above zero. Reading (b): processing exceeds maintenance (F = 59, p = 2e-14), with 4 of 7 subjects above zero and a mean of −0.17 against the paper's F of 1936 and mean of 6.01. Reading (b)'s z is uncalibrated (problem 1). |
| fig4c-alpha-beta-shift | not_reproduced | Under readings (a) and (b), 5 of 7 subjects are below zero (the partial bar needs 6). The means are −0.03 and −1.89 against −12.6. Again, only "code_rev" passes. |
| directional-pairs | reproduced (by the letter of the criterion) | Reading (b) gives 1014 delta-theta and 1043 alpha-beta pairs, within tolerance; reading (a) gives 264 and 118. But independent noise under reading (b) gives about 82% of pairs with \|z\| > 1.96 (problem 1), so the match carries no evidence of real directionality. |
| fig5a-delta-theta-epochs | not_reproduced | Reading (a) finds no significant time points. Reading (b) finds sustained runs at 110–230, 300–400 and 460–600 ms (spatial) and 120–250, 290–390 and 680–840 ms (temporal). There is no early epoch starting at 0, and the late epochs have the wrong sign. |
| fig5a-identity-direction | not_reproduced | None of the four epoch values meets the criterion under any averaging reading (a, b, c, B) for either P1 reading. Examples: 0.35 against > 2.62, and 4.44 against < −3.57. |
| fig5a-spatiotemporal-bidirectional | not_reproduced | Under reading (b), the reading whose pair selection matches directional-pairs, the grand mean passes \|z\| ≥ 1.96 at 42 and 40 of 91 points (maximum 5.44 and 6.36). Under reading (a) every \|z\| < 1.96, but (a) shows nothing anywhere, including where the paper reports \|z\| ≈ 40, so the absence there is uninformative. |
| fig5b-alpha-beta-no-sustained | reproduced | Reading (b): 66 and 75 of 91 points are FDR-significant, and the longest same-sign runs are 80 and 90 ms, so nothing is sustained. Reading (a) gives no significant points, which would be partial. |

### B. Problems

1. **[affects a conclusion]** `fcx3.psi_measures`: the null does not compute the same statistic as the observed PSI, so z is not calibrated under either reading.
   - In reading (b), the observed value is the mean over trials of per-trial unit-phasor slopes, while the null is the slope of the bin-shuffled trial-mean phasor, whose magnitude is about 1/√trials.
   - In reading (a), the observed value sums nf−1 adjacent bins, while the null sums nf randomly paired bins.
   - On independent filtered noise (33 trials, 60 pairs, delta-theta), the share of pairs with \|z\| > 1.96 is 20% under (a) (SD 1.5) and 82% under (b) (SD 14).
   - The paper says it "shuffled the frequencies in one signal and re-computed PSI". This bears on directional-pairs, fig4a, fig4c, fig4-maintenance and all four fig5 claims.
2. **[affects a conclusion]** `psi_measures(deposited=True)`, cells 33–36: the "code" and "code_rev" variants compute X·Y/√(X²·conj(Y²)), which equals ±e^{2iφ_Y}. That depends only on the second channel's phase.
   - Its sign is fixed by which channel is placed second.
   - Independent noise gives 92–100% "significant" pairs.
   - These variants must not count as a reading. They are the only route to the fig4-maintenance and fig4c targets.
   - If the paper's own code has this bug, it may explain the paper's very large z values. That is worth reporting, not testing.
3. **[does not affect a conclusion]** `psi_measures(null_per_bin=True)` averages nf identical replicate nulls. It is not a per-frequency null, despite the docstring and the paper's "at each … frequency point".
4. **[affects a conclusion]** Cells 22–26 and the `neighbours` function: the notebook says it read `analysis_scripts.zip`, but it never reports what the scripts set for neighbours or for the per-tail cluster alpha. Both decide the ERP and power outcomes; for example, the fig3 counts match under only one combination.
5. **[affects a conclusion]** `analyse_subject`, ERP section: the baseline is one mean per channel, taken over all trials and time. That constant cannot change the t-test, so the baseline has no effect.
   - The paper's "processing minus pretrial mean" also allows a per-trial baseline, which was not run.
   - The Results say "1–30 Hz bandpass" while the Methods give a 30-Hz low-pass; only the low-pass was run.
6. **[affects a conclusion]** `tfr_fourier`, power and time-resolved PSI: windows at low frequencies (up to ±750 ms at 2 Hz) take in data outside the 900-ms segment.
   - Processing windows reach back into the cue and forward into the response period, and identity RT is longer, so condition differences can leak in.
   - Baseline windows reach into the start screen.
   - The paper and both S1 readings describe zero-padded segments. The notebook cites power_compute.m for this choice, which I could not check, and runs neither S1 reading.
7. **[does not affect a conclusion]** Cell 10, jitter check: the 70–150 Hz processing-window response in 1150-ms trials is shifted by +0.21 to +0.26 s against 900-ms trials in s2, s3 and s4 ("clear"), and by +0.28 to +0.35 s, not clear, in s1, s5 and s6. s4's encoding window also shifts. The processing epochs may be misaligned for about half the trials. The notebook does not resolve this; whatever it said was in the removed summary.
8. **[does not affect a conclusion]** Claims-file misreading: P2 and fig5b say sustained means "at least 100 ms", but the Figure 5 legend says ">100 ms". No outcome changes either way.
9. **[does not affect a conclusion]** Cell 30: the local-maximum rule counts the 2-Hz edge as a maximum, and the claim passes in only one of six combinations. It is fragile.
10. **[does not affect a conclusion]** `paired_lme` treats 1135 pairs that share electrodes as independent. This follows the paper's degrees of freedom, but it inflates F and p in fig4 and fig5.

### C. What I could not check

- **The deposited scripts.** I could not see psianalysis.m (conjugate, null construction), power_compute.m (padding), erp_compute.m (baseline) or subtracterp.m. The notebook should print the relevant script lines and the cluster-test settings (neighbours, alpha per tail).
- **PSI calibration on the real data.** A surrogate run, such as PSI computed between trial-shuffled PFC and parietal data with its rate of \|z\| > 1.96 printed, would show whether readings (a) and (b) hold 5% on the real data.
- **The jitter shift.** Cue-locked 70–150 Hz traces per delay group, and a rerun of the processing analyses on 900-ms trials only, would show whether it matters.
- **Per-subject power percentages.** Only the adjacent reading is printed per subject. I could not compare with the paper's per-subject figure values, which the claims file did not read either.
