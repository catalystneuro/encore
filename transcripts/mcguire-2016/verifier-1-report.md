**Verifier report, round 1: McGuire et al. 2016 (doi:10.1371/journal.pbio.1002549) on CRCNS ssc-4**

The claims file holds 37 claims. Both notebooks test all 37 and treat none as blocked. My outcomes: 23 reproduced, 11 partially reproduced, 3 not reproduced, 0 blocked.

### A. Outcomes

| claim | outcome | reason |
|---|---|---|
| fig2ab-fms-smf-not-discriminated | partially_reproduced | In all 5 rats the data hold, FFF > SSS, FMS and SMF lie between them, and FMS vs SMF is not significant (p 0.10 to 0.87). 62SC is not in the data, and the criterion caps the outcome at partial (cell 13). |
| training-days | partially_reproduced | Over 5 rats: mean 14.8 (within 14.2±4.4) and max 20 (within 22±2.2), but min 11 (expected 8±0.8). The 8-day rat is one that was not recorded (cell 15). |
| fig2c-choice-follows-mean-speed | reproduced | All 5 rats order FFF > FMS,SMF > SSS, with r = 0.97 to 1.00 (cell 17). The S1 Data variant holds for all 8 rats. |
| fig2d-fixed-panel-impairs | reproduced | From S2 Data, the fixed-panel value is lower in 6 of 6 rats, paired t p = 0.0120 with the rat at 0 kept, which equals the paper's p = 0.012 (cell 19). |
| dprime-fff-sss-range | partially_reproduced | The lowest value, 0.45, is in tolerance and every rat lies in 0.45 to 1.65. The highest is 1.09 pooled or 1.23 as a session mean, short of 1.35 (cell 21). The missing rats hold the highest values in S1 Data. |
| fig3-fsfs-sffs-intensity-only | reproduced | From S1 Data: 69.98, 69.17, 51.74 and 53.02 % correct, and d-prime 1.004 / 0.130 as the mean of the two rats. All within tolerance (cell 23). |
| units-recorded | reproduced | 330 SU, 176 MU, 80 sessions, 5 rats, mean 4.12 SU per session, max 12. All within tolerance, though the total is 506 against the paper's 473 (cell 25). |
| baseline-rates | partially_reproduced | FS 7.59 to 30.18 Hz and the RS low of 5.93 are in tolerance. The RS high, 11.40 Hz in L5a, is above the 11.0 bound. MU is higher than RS in 5 of 5 layers (cell 27). |
| temporal-modulation-count | reproduced | Reading (a) gives 310 of 506 (61.3%), within 305±30.5 and 63.5±6.35% (cell 29). See B1. |
| modulated-higher-baseline | reproduced | Modulated RS units have a higher baseline in 5 of 5 layers. Layer × modulation chi-square p = 0.105. Columns cannot be tested (cell 32). |
| fig4d-evoked-modulation-by-layer | partially_reproduced | The best combination (absolute peak, per impulse) puts 4 of 5 layers in tolerance; L5a is 7.65 against 6.3±1.2. L5a and L6 are the two lowest under every combination (cell 34). |
| latency-by-layer | partially_reproduced | Latencies of 14.6 to 20.4 ms put 0 to 1 of 5 layers in tolerance. The ordering holds under 3 of 4 readings (cell 36). See B4. |
| fig4d-gradual-decrease | not_reproduced | L5a also decreases under both readings (slope −0.88 Hz/100 ms, p < 0.001; last 30 ms minus baseline −1.6 Hz) (cell 38). |
| fig6-regression-significant | reproduced | 194 of 310 units, within 204±20.4 (cell 40). |
| fig6e-unit-classes | partially_reproduced | Fast 160, Medium 48 and SlowPos 51 are in tolerance, as are 51.6% Fast and 42.9% with 5 to 10 ms windows. SlowNeg is 51 against 44±4.4. The deposited labels (160/53/51/46) are all in tolerance (cell 42). |
| fig6fg-laminar-classes | partially_reproduced | 4 of 6 values in tolerance: L6 Fast is 26.5 (expected 23±2.3) and L2/3+L4 Slow is 18.3 (expected 13±1.3). The gradient holds. Deposited labels give 6 of 6 (cell 45). |
| fig7c-fast-impulse-velocity | reproduced | F 9.59 > M 8.73 > S 7.42 Hz; paired F vs S p = 1.4e-5 (cell 49). |
| fig7c-fast-sequence-rate | reproduced | The ordering holds. FMS vs SMF is not significant with the 10-ms baseline (p = 0.31) but is with the 25-ms baseline (p = 0.046) (cell 51). |
| fig7-fff-adaptation | partially_reproduced | The ratio of population means, 0.79 / 0.80, is in tolerance. No combination makes 3/1 significant (p 0.09 to 0.64). The unit set is 34, not 61 (cell 53). See B2 and B3. |
| fig7-sss-no-adaptation | reproduced | With the 10-ms baseline the ratios are 0.84 / 0.76 and not significant; the ratio of means, 0.88, also fits (cell 55). This rests on 34 units, not 61. |
| s4-fms-middle-pulse | reproduced | FMS is lower than SMF (−1.6 Hz), p = 0.26 in the 34-unit set. All 63 Fast RS units give p = 0.087, against the paper's 0.08 (cell 57). |
| fig7de-medium-suppressed | not_reproduced | The F response is +0.05 Hz, so not all three means are negative. With deposited labels all three are negative but none differs from 0 (p ≥ 0.45), so suppression is not shown under either set (cell 59). |
| fig8a-slow-positive-no-sequence-difference | partially_reproduced | Sequence RM-ANOVA is not significant (p = 0.087 / 0.43) and F and M responses are positive, but the S response is also significantly positive (1.23 Hz, p = 0.027), which the criterion excludes (cell 61). |
| fig8b-slow-negative-no-impulse-response | reproduced | No impulse kind is significantly positive, and the PSTH slope is −5.5 Hz/100 ms (cell 63). |
| fig8d-slow-positive-right-choice-l5 | partially_reproduced | L5b is significant (p = 0.0045 / 0.0008) and L2/3, L4 and L6 are not, but L5a is not significant (p = 0.12, n = 6). Deposited labels with reading (a) pass (L5a p = 0.049) (cell 65). |
| fig8d-fast-medium-no-choice-bias | reproduced | Reading (b), 5-ms bins, has no significant time in 0 to 150 ms. Reading (a) has 5 isolated ms at 5 to 9 ms, about what uncorrected sliding tests give by chance (cell 69). |
| fig8e-choice-divergence-125ms | reproduced | Reading (a): a significant run from 122 ms that lasts to 150 ms. Withdrawals: min 153 ms, mean 193 ms. All within tolerance (cell 67). |
| s5-slow-positive-no-integration | reproduced | With the 25-ms baseline, the pulse 3 RM-ANOVA is not significant for both choices (p = 0.052, 0.32) and no correlation is significant. With the 10-ms baseline, left choice gives r = −0.97, p = 0.03 (cell 71). |
| s6-head-position-choice | reproduced | From S2 Data, head dx differs from 100.8 ms on, by −0.595 mm at 126 ms. Head angle and whisker tip are not significant at any frame (cell 73). |
| s7-no-fs-l5-slow-positive | reproduced | Every class holds all three unit types. The FS fraction of each Slow class is below Fast's, and L5 Slow Positive has 0 FS units (cell 75). |
| fig9b-stimulus-decoder-fast-medium | reproduced | C = 1: overall 84.1%, FMS 74.9%, FFF 84.4%, FMS/SMF 82.1% (reading A). All within tolerance; chance 25% matches the paper (decoders cell 5). |
| fig9c-best-units-short-windows | reproduced | The 5-ms group has the highest mean (32.7%), and 17 of the top 21 units have 5 or 10 ms windows (decoders cell 7). |
| fig9b-stimulus-decoder-slow-chance | reproduced | 30.1%, within 32±3.2. Test (a) p = 0.21. Test (b), the binomial, gives p ≈ 0, so this rests on the weaker test only (decoders cell 9). |
| fig9d-single-bin-decoder | reproduced | Fast/Medium single bin 39.4%, within 38.7 to 47.3 (at the edge). Slow single bin 26.5% does not exceed Slow 10-ms 30.1% (decoders cell 11). |
| fig9e-temporal-pattern-decoding | reproduced | Rate-normalized 79.4%. Scrambled 28.9%: below 32%, and test (a) p = 0.37 (decoders cell 13). |
| fig9f-choice-decoder | not_reproduced | Slow decoder: 80.1% (single bin) and 91.7% (last 100 ms) with C = 1; 74.6% and 79.2% with C by CV. Fast/Medium: 63.8 to 79.0%, so it is not "unable". Only unweighted training gives about 50%, and then for both decoders (decoders cell 15). |
| fig9g-l5b-slow-positive-best-choice | reproduced | L5b Slow Positive has the highest mean unit choice accuracy (59.8%) (decoders cell 17). |

### B. Problems

1. **[affects a conclusion]** Cells 29, 30 and 42 (`temporal_pvals`, `perm_pval`): the modulated set does not match the authors' set.
   - Reading (a) gives 310 modulated units, the same number as the deposited `TemporalPval < 0.05`, but the two sets agree on only 73.1% of units (136 differ).
   - Running the test on the deposited window (−50 to 300 ms) gives 363, not 310, so the uniform-redistribution null does not reproduce the authors' test.
   - The deposited labels sum to 310 (160/53/51/46) and look like the authors' own classes. All downstream claims use the recomputed set, and four outcomes change with it: fig6e, fig6fg and fig8d-slow-positive pass on deposited labels; fig7de passes only the letter of its criterion on them.
   - `perm_pval` itself is correct: on synthetic uniform spikes its false-positive rate at 0.05 is 0.05.
2. **[affects a conclusion]** Cell 53 (`f_responsive` / `ssc4.impulse_ttest`): the selection keeps 34 of 63 Fast RS single units. The paper (Results, Fast and Medium units, paragraph 3) says "Fast RS single units (n = 61)", so its 61 is close to all Fast RS units. The 0 to 10 ms pre-impulse baseline for pulses 2 and 3 lies inside the tail of the previous response, which plausibly makes the test stricter than the authors'. On all 63 units, s4 gives p = 0.087 (paper 0.08) and FFF 2/1 paired p = 0.039. The fig7 adaptation claims and s4 should be judged on that set as well.
3. **[affects a conclusion]** Cell 53 (`adaptation`): the filter `ok = p1 > 0` admits floating-point residues. With the 10-ms baseline this gives FFF per-unit ratios of about 1e13, so the "mean of per-unit ratios" reading and its one-sample test were never validly evaluated for FFF under that baseline.
4. **[affects a conclusion]** `ssc4.box10` / `evoked_peak` (cell 36): the centred boxcar is the author's own choice; the Methods say only "10 ms smoothing".
   - A forward window (value at t = mean of t to t+9) would shift latencies about 4.5 ms earlier. Every layer here is 3 to 7 ms later than the paper, so this reading could change the within-tolerance count. It was not run.
   - On ties, `argmax` returns the first sample: a synthetic spike at +12 ms returns a latency of 8 ms.
5. **[does not affect a conclusion]** Decoders cell 15 (`choice_decoder`, `balanced=True`): class-balanced training is an author assumption, and it moves the Slow decoder from 51% to 92%. Neither setting gives 65% with Fast/Medium unable, so the outcome is not_reproduced either way.
6. **[does not affect a conclusion]** fig9b-slow-chance test (a) (decoders cell 9) measures how much repeats spread around 25%; it is not a null distribution. The claims file allows it, but the "not different from chance" outcome depends on it alone, since test (b) gives p ≈ 0.
7. **[does not affect a conclusion]** Cell 71: impulse speeds come from an assumed ramp on the Table 1 amplitudes, while the criterion names the S1 Fig speed profiles. Those profiles were loaded (S2 Data sheet "Fig S1") but not used. The F, M and S spacing is nearly even, so r should change little, though the correlations have n = 4.
8. **[does not affect a conclusion]** Cell 15: the count uses distinct dates. The paper's "12–22 d of recording" matches session counts per rat (12, 12, 15, 19, 22), so it likely counted sessions. That gives mean 16.0, min 12, max 22: still partial.
9. **[does not affect a conclusion]** Cells 25 and 27 onward: all analyses include 506 units, against the paper's 473. The descriptor says to drop A1 and B2 column units using `MapPosition`, which `AllRats.mat` does not contain. The archive holds only `AllRats.mat`, `checksums.md5`, `filelist.txt` and the descriptor (S3 listing checked), so this cannot be fixed from the archive.
10. **[does not affect a conclusion]** Cells 11 and 13: trial readings (i) and (ii) select the same 14,186 trials, because every trial with a choice is completed and over 250 ms. This is correct, but only one reading was effectively run.
11. **[does not affect a conclusion]** Cell 67 uses centred sliding windows. A trailing window would move the onset to about 127 ms, still within tolerance.

No claim is blocked, so step 4 did not apply. I found no train/test leakage in `stim_decoder` or `choice_decoder`. Every number derives from `AllRats.mat` or from S1/S2 Data. I found no place where the claims file misreads the paper.

### C. What I could not check, and the output that would settle it

- **Unit-set dependence (B1).** I could not see whether the remaining claims change on the deposited modulated set. The notebook should print fig4d, latency, gradual-decrease and baseline-by-modulation on that set. It should also print a temporal-modulation run with a per-trial bin-shuffle null on the −50 to 300 ms window, and its agreement with `TemporalPval`.
- **Latency (B4).** Latency per layer under a forward and a trailing 10-ms boxcar, with unsmoothed argmax as a third variant.
- **Adaptation (B2, B3).** The full adaptation and s4 tables for all 63 Fast RS units, under both baselines, with a guard such as p1 > 1 Hz in place of p1 > 0.
- **Choice decoder.** Population accuracy against the number of units in the decoder, and per-unit choice accuracy for Fast/Medium units, to see whether the gap from 65% comes from summing about 100 to 200 independent units.
- **Baseline rates.** S1 Table (DOCX, not loaded): the per-layer baseline rates, set beside the notebook's table.
- **s5 speeds.** Impulse mean speeds from S2 Data "Fig S1", and the s5 correlations recomputed with them.
