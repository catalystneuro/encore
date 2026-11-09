# Verifier report, round 1: Okubo et al. 2015 on CRCNS am-3

**Overall:** of the 42 claims in the claims file, I find 19 reproduced, 11 partially reproduced, 8 not reproduced and 4 blocked.

**How I checked:**
- I read all the notebook outputs, `hvc.py`, `hvcmodel.py` and the Methods passages each method relies on.
- I listed the am-3 bucket over S3 (`am-3/live/`). It holds no adult recordings. For each bird there is only a raw archive (sound and voltage), plus `Analysis_files.tar.gz`.
- I tested the helper functions on synthetic data:
  - `shift_test` on Poisson spikes gives a false-positive rate of 0.03 (wide reading) and 0.05 (circular).
  - `type_test(adjust=True)` gives 0.03.
  - `rhythmicity` calls 0 of 30 random-burst trains rhythmic. On trains with a 170 ms period it calls 30 of 30 rhythmic and returns a period of 174 ms.
- I checked the bout-onset parameters of the model port against the MATLAB code; they agree.

## A. Outcomes

| claim | outcome | reason |
|---|---|---|
| counts-neurons-birds | reproduced | The juvenile part, which is what the criterion judges: 1,116 neurons (expected 1,117), 32 birds, 210 HVCp (expected 211) (cell 11). The 32 adult neurons are not in the archive. |
| ed1a-stage-age | reproduced | Per-neuron reading: ρ = 0.615; medians 48, 58, 62 and 73 dph match exactly (cell 13). Counting the list's "young adult" as motif gives 378 motif neurons, the paper's number. |
| fig1-subsong-locking | not_reproduced | 39 subsong neurons, but 25 (wide shift) or 27 (circular shift) are locked against 19 ± 1.9 (cell 15). |
| fig1f-locking-increases | partially_reproduced | Juvenile stages only, so partial at best. The locked fraction rises 0.64 → 0.85 → 0.86 → 0.96; r = 0.196 with P = 3.8e-11 (cell 18). |
| fig1f-rhythmic-protosyllable | not_reproduced | Rhythmic neurons: 87–88 of 135 (expected 70 ± 7) and 6–7 of 39 in subsong (expected 3), under every reading (cell 20). |
| fig1fg-rhythm-increases | partially_reproduced | Juvenile only. Rhythmic vs stage r = 0.28–0.29; period vs stage r = 0.46–0.47; both P < 1e-20 with the right sign. The rhythmic total is 826–836 against 727 ± 72.7 (cell 22). |
| ed1c-burst-width-rate | blocked (data_missing) | The criterion compares each stage with adults, and the adult neurons (ref. 20) are not in am-3 (bucket listing). |
| fig1de-bout-related | not_reproduced | Post-only 158 (expected 98 ± 9.8), both 60 (expected 50 ± 5), total 342 (expected 285 ± 28.5). Only pre-only (124) is within tolerance (cell 26). |
| fig2b-protosequence | partially_reproduced | 55 locked neurons (expected 54) and coverage above 90% in all three birds. But latencies do not reach past the mean protosyllable offset in birds 1 and 4 ("spans … False", cell 30). |
| ed2st-coverage | partially_reproduced | 19 syllables kept, 17 above 90%, lowest 79.8%. The 17 and the lowest value are within tolerance, but "b1 B 81-112" (93.9%) lies outside its surrogate interval (94.5–100), and the criterion requires every syllable inside (cell 78). |
| ed2p-probabilistic | reproduced | Mean 52.3% against 53 ± 5.3%, which meets the criterion's condition (cell 32). It is computed over 87 rhythmic neurons, not 70. |
| ed2qr-pairs-independent | not_reproduced | 10 pairs in 4 birds; median r² = 0.119 (expected 0.072) and median MI = 0.083 bits (expected 0.056) (cell 34). |
| fig2c-latency-subsong-earlier | reproduced | Wide shift, latency reading (a): 64% vs 44% before onset, P = 0.038, subsong median earlier (cell 36). Fragile: under the circular shift P = 0.143, and the locked counts (25 and 115) are outside tolerance. |
| fig2c-latency-broadens-later | reproduced | IQR 52 → 101 ms and fraction before onset 44% → 36%; 851 neurons against 814 ± 81.4 (cell 38). |
| bird1-protosequence | reproduced | 16 neurons, 14 locked to protosyllable onsets under reading (a) (cell 58). |
| fig3g-bird1-shared-specific | reproduced | Only under the author's window-adjustment rule (problem 1): 96 / 37 / 39 / 20, against lower bounds of 94.5 / 36.9 / 37.8 / 19.8. Without the rule there are 32 shared (cell 42). |
| ed4a-shared-latency-bird1 | partially_reproduced | Early r = 0.852 (P = 1.8e-6) passes. Late r = 0.700 with P = 0.053 fails (cell 46). |
| ed3j-shared-ibi-specific-doubled | reproduced | Bin reading (b): specific/proto ratio 2.19 and shared/proto 1.03, both within tolerance (cell 48). The protosyllable group has 16 (or 12) neurons, not 9. |
| fig3h-bird1-shared-decrease | partially_reproduced | The late fraction is lower, P = 0.019. But late shared is 8 against 10 ± 1 (cell 44). |
| all-birds-shared-specific | partially_reproduced | Bird 3 cannot be tested (it has no labels). Totals: 167 shared (within tolerance) and 428 specific (outside 496 ± 49.6). No reading gets both totals within tolerance (cell 50). |
| all-birds-shared-decrease | reproduced | CMH P = 1.3e-4 (boundary a) and 1.7e-6 (boundary b); the pooled shared fraction is lower late (cell 52). |
| skipping-cycles | partially_reproduced | Found in birds 1, 3 and 4 under both readings, but not in bird 6 (cell 54). |
| fig4-bird2-before-beta | partially_reproduced | 125 / 35 / 28–29 all match. But there are 12 pre-bout neurons against 4. Only "pre-bout and outside the rhythmic set" gives 4, a reading the author chose after the fact (cell 56). |
| fig4h-bird2-shared-early | partially_reproduced | Offset-aligned counts are within tolerance: 20 shared, 23 specific. Latency r = 0.787 is below the 0.891 bound, and the two-peak neuron was not identified (cell 60). |
| fig4i-bird2-shared-decrease | not_reproduced | Late shared 6, outside even the partial band of 3–5; specific 25 (expected 28 ± 2.8). The decrease itself is significant, P = 0.016 (cell 62). |
| ed4bd-shared-latency-other | not_reproduced | Bird 1 D/B r = 0.99 passes. Bird 2 late r = −0.41 (P = 0.42) and bird 4 b2/d1 r = 0.76, so the partial condition (all positive and significant) fails (cell 64). |
| ed7-bird1-bd-shared-persist | reproduced | Late B/D shared fraction 0.74–0.77 against late B/C 0.09 (cell 66). |
| ed8-bird3-phase | blocked (metadata_insufficient) | Confirmed: only 1 of bird 3's 19 neurons has labels. Labels A–E were assigned by hand. `to3017.tar.gz` would give the sound phase but not syllable identity. |
| motif-strategy-shared | blocked (metadata_insufficient) | Bird 3's shared part needs the missing labels. Parts are testable and positive: bird 4 has 8 rhythmic protosyllable-stage neurons and every syllable a–f has neurons shared with another (cell 68); bird 3 has 3 rhythmic protosyllable-stage neurons (cell 54). |
| ed9-bird4-rhythms | not_reproduced | 18 neurons, but 8 rhythmic against 11 ± 1.1, and a 10 Hz / 5 Hz split of 3/5 against 5/6 (cell 70). |
| ed4j-bias | partially_reproduced | The shared mean fits (0.282). The specific mean (0.973, or 0.980) is outside 0.96 ± 0.011 under the criterion's readings. It fits only under the author's extra "early only" variant. Its s.d. is 0.07, against the paper's 0.011 (cell 72). |
| ed5-shared-acoustic-difference | blocked (too_large / methods_underspecified) | The sound exists, in about 30 GB of raw archives, so the notebook's stated reason "not_runnable" is not a valid reason. The gap-exclusion counts (24/120 shared, 9/59 obscured) need only segments and could have been tested. |
| ed5-shared-ra-x-proportion | reproduced | A claim of absence: P = 0.116 (reading a) and 0.085 (reading b). The fractions are 24%/34% and 14%/20%, against 19%/28% (cell 74). |
| ed2mo-ra-x-similar | reproduced | Juvenile stages, 11 comparisons: only the motif-stage period is significant after Bonferroni, under both period readings (cell 76). |
| model-fig5a-subsong-decay | reproduced | Back within 15% of baseline by lag 3 for seed 9038, and by lag 9 or earlier for all 10 other seeds (cell 82). |
| model-fig5b-chain | reproduced | 90 participating neurons at iteration 500 against 26 in subsong; latencies 2–10 all covered (cell 84). |
| model-fig5cd-split | reproduced | Iteration 992: 1 + 1 specific, 81 shared, all at the same latency. Shared fraction falls 0.98 → 0.00 by 2,500. Marginal: two of the 10 extra seeds have no specific neurons at 992 (cell 86). |
| model-fig5e-latency-broadens | reproduced | The s.d. reading rises 2.18 → 2.27 → 2.41. The IQR reading does not rise from protosyllable to splitting (4 → 4), and several extra seeds fail too (cell 88). |
| model-ed10gh-period | reproduced | Mean period 100 ms at iteration 500 and 200 ms at 2,500; specific neurons at 200 ms (cell 90). |
| model-ed10ad-bout-onset | reproduced | Iteration 600: 51 and 39 specific neurons; shared fraction 0.00, against 0.60 at iteration 130 (cell 92). |
| model-ed10eh-motif | not_reproduced | At 2,500 iterations, 13 non-seed neurons still take part in two groups, against "non-overlapping" sequences. Only reading (a) was run (cell 94). |
| model-ed10ik-new-chain | reproduced | Specific neurons for both elements (34 and 10); protosyllable seeds fire on every input (1.0) (cell 96). |

## B. Problems

1. **[affects a conclusion]** `hvc.type_test(adjust=True)`. The rule standing in for the paper's visual adjustment is the author's own. The paper adjusted the interval only "if necessary to avoid the same burst being detected twice". The rule instead re-searches every peak that falls outside [0, mean duration], whether or not that burst is also detected in the neighbouring syllable. Several outcomes rest on it:
   - fig3g passes only under the rule, and only by 0.1–0.2 neurons on two counts (without it, 32 shared).
   - fig3h, ed4a, fig4h and ed4j also use it.

   The raw reading's wrong latency correlations (r = −0.21, cell 46) suggest double detection is real. But the notebook never shows on how many neurons the rule fired, or whether the burst was in fact also detected in the adjacent syllable.
2. **[affects a conclusion]** `hvc.coverage_patches` and cell 78. Each neuron's window uses its own mean syllable duration. The patches are then cut or padded with False to the median length before being combined by OR. This misaligns syllable time across neurons recorded on different days. The padding lowers coverage, and it can move a syllable out of its surrogate interval; that is the only failure for ed2st ("b1 B 81-112").
3. **[affects a conclusion]** Cell 60, `two_peaks`. The claims file asks for the shared neuron whose alpha histogram has two *significant* peaks. The author's rule (peaks above half the maximum, at least 30 ms apart) found none, so the legend's exclusion was never applied. r = 0.787 against the 0.891 bound may turn on one outlier; the per-neuron latencies are not printed.
4. **[affects a conclusion]** Cell 72, ed4j. The specific-neuron mean is within tolerance only under the author's added "early only" variant (b′). The criterion's readings (a) and (b) give 0.973 and 0.980. Choosing among sub-variants inflates the chance of a match.
5. **[affects a conclusion]** Cell 94, model-ed10eh. Reading (b), the GitHub code, was not run on the ground that "no commit is pinned". The author could have pinned one. Also, the groups get unequal numbers of pulses (4, 3, 3) under a threshold of more than 2 firings, which is the author's choice. The not_reproduced outcome rests on this one reading.
6. **[affects a conclusion]** Cell 56, fig4-bird2-before-beta. The criterion's bout-onset count is the pre-bout count, which is 12. The matching 4 comes from a subset ("outside the protosequence") that the author defined after seeing the data.
7. **[does not affect a conclusion]** `bout_classes`, cell 26. The pre-bout exclusion compares the pre-bout peak latency (−300 to 0 ms) with the syllable-locking peak, which is searched only in −50 to 200 ms. So the exclusion can only remove pre-bout peaks between −75 and 0 ms. The Methods refer to a peak in the syllable-onset histogram, which spans ±0.5 s. The claim fails on the post-bout counts, which this does not touch.
8. **[does not affect a conclusion]** Cell 99, ed5-acoustic. "not_runnable" is not one of the allowed blocked reasons. The sound is in the archive, about 30 GB. The sound-free part (shared-neuron counts and the silent-gap exclusion) could have been tested.
9. **[does not affect a conclusion]** Cell 68 uses `type_test` without the adjustment, which is inconsistent with the main reading. Bird 4's per-syllable shared counts are therefore inflated by double detection, though they are large (15 or more).
10. **[does not affect a conclusion]** Cell 54. Bird 6's base period comes from a single shared neuron (631 ms), which says nothing useful. Reading (a) also flags 242 of 318 bird-1 neurons, including long-period motif-stage neurons, so it is a weak test of cycle-skipping.
11. **[does not affect a conclusion]** Cell 48. The paper's protosyllable group of 9 neurons is not reconstructed (the notebook uses 16 or 12); both groups give the same median.
12. **[does not affect a conclusion]** Cell 50:
    - The "pairs counted" printout counts tables, not pairs.
    - Bird-1 neurons from 70–72 dph enter both the β/γ and the B/D pair.
13. **[does not affect a conclusion]** Cell 11. The HVCp reading "211 spanning all stages" is not shown, though the criterion asks for both readings.
14. **[does not affect a conclusion]** Cell 76. Only the wide-shift locking and the aa rhythmicity readings are used.

I found no leakage problem (there is no train/test split) and no unit errors. Every number traces back to the loaded files or to the model runs.

## C. What I could not check, and the output that would settle it

- **Problem 1:** for each pair, how many neurons the adjustment rule fired on, and whether the replaced peak was also significant for the adjacent syllable.
- **Problem 3:** bird 2's 20 shared neurons with their α and β latencies, and their α histograms or peak P values.
- **Problem 2:** the per-neuron mean durations in each coverage syllable, and coverage recomputed on one common warped window.
- **Locking and bout-related failures:** the distribution of post-bout peak latencies, and the subsong locking histograms. These would show why there are 158 post-only and 25 locked neurons rather than 98 and 19.
- **ed3j:** which of bird 1's protosyllable-stage neurons make up the paper's 9; the IBI count per neuron would let one test that.
- **Model port:** whether it matches MATLAB beyond the code reading. No MATLAB was available and the random streams differ, so only the 10-seed spread speaks to robustness.
- **Adult recordings:** whether they exist in any other public archive. I checked am-3 only.
