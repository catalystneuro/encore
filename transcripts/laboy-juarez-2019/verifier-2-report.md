## Round 2 verification: Laboy-Juarez et al. 2019 (CRCNS ssc-9)

The claims file has 50 claims and the attempt record has 50 outcomes: 29 reproduced, 13 partially reproduced, 7 not reproduced and 1 blocked. The README table matches these counts (10/31/9 claims by experiment).

### 1. Outcomes and assumptions

I agree with all 50 stated outcomes. The ones that changed or that I disputed in round 1:

- **fig1e: reproduced (assumed).** I agree. Same-direction sequences give 0.694, 0.851 and 0.456 (cell 33), and sham reading (b) also passes. The assumption is stated and reasonable: the Methods' 261 stimuli are 9 singles plus 36 × 7 sequences, and the experiment 3 stimuli, called identical, are same-direction only. Cell 7 shows the opposite-direction trials are real stimuli with distinct timings, not a coding flip.
- **exp1-cw-sw-comparable-firing, supp4 and fig4c: partially reproduced.** I now agree, and withdraw my round-1 "not reproduced". In round 1 I already gave "partially reproduced" to fig7b, fig7c, fig7e and supp6. Their criteria also name no partial rule, and in each one part holds and another fails. The same standard applies to these three:
  - exp1: spontaneous rates hold, maximal evoked firing fails in the claims file's unit.
  - supp4: the peak test holds, the counts fail.
  - fig4c (reading b): SW-tuned beats CW-tuned at every size; CW-tuned is not above chance at N = 150.
- **fig3g: partially reproduced (assumed).** I agree. Cell 138 gives 0.633 at N = 10 and 0.857 at N = 100, which meets the criterion's partial rule. It is fragile: 0.003 above the band edge, with an s.d. over refits of 0.010.
- **fig7a: partially reproduced (assumed).** I agree. Leaving out sets with a constant best curve is stated and reasonable, since they have no best dt.
- **fig8c: not reproduced.** I agree. Cell 177 gives p = 0.0021, and the criterion's partial rule needs the test to hold.
- **supp8: not reproduced (assumed).** I agree. The mean over five refits is 0.584 against a lower bound of 0.585, with a Monte Carlo s.e. of 0.003 (cell 147). It is fragile.
- **exp1-units and exp1-cw-tuned-fraction (assumed: caudal singles).** Stated and reasonable. Pooling both directions breaks the counts (cell 15).
- **Selective-group assumption** (supp4, fig3g, fig6b-enhancement-not-different, fig7a, supp8). It is stated in each outcome and checked against the 187-set variant (cells 150–170).

### 2. Text against the printed outputs

Sentences the numbers do not support:

- **Cell 51 and the record's exp2-units notes:** "the other three readings give 237 to 240". Cell 50 prints anti-correlated = 236 under O2 (a), sham (b), so the range is 236 to 240. All values are still within tolerance, so the outcome is unaffected.
- **Cell 195, Summary table:** "fig1e-best-combination-includes-cw | reproduced (assumption: caudal singles)". The outcome rests on the same-direction sequence reading: variant (ii) gives 0.421, which fails (cell 44). Pooling both single directions (i) still passes (0.677, 0.826, 0.493). The record and cell 34 have this right; the summary table labels the wrong assumption.
- **README:** "...the inbound order preference and the awake results mostly reproduce." No experiment 2 order claim is reproduced:
  - fig7b, fig7e and fig7f are partially reproduced.
  - fig7g and supp8 are not reproduced.
  - Only the awake fig8j is reproduced.

Everything else checks against the outputs: every other "Result:" cell, the variant-section summary (cell 170), the Summary bullets, and the record's notes and findings. That includes the 0.246 null rate, 162 calibrated sets, the 74/113 split and 130 cells of the 187 group, the 5.6% late-spike epochs, and the latency of 30 against 70 ms.

On supralinear, cell 170 says "same outcome", but on the 187 sets the main reading O3 (a) gives 0.032 and only O3 (b) passes (0.080, cell 156). The criterion accepts any combination of readings, so the statement is correct as written. Both groups pass only at a band edge and under different readings, which leaves this outcome weak.

The attempt record states my round-1 reasons faithfully, mostly in my own wording. Only B10 (no sham trials in two recordings, no lick exclusion), which does not affect a conclusion, is missing from the reasons.

### 3. Round-1 points

Resolved:
- **B4:** the Hz variant was added and the question to the authors filed.
- **B5:** the main analysis now uses same-direction sequences.
- **B7, B8, B9:** stated in the notes, mirror-image dt ranges run, and O3 (b) run for supp4.
- **B10:** stated in the notebook.
- **B11:** needed no action.
- **C items:** all run except one. The real-data null, the experiment 3 fields, the raw 20170510 trials, sham (b) for experiment 1, Monte Carlo errors, and the 187-set group are all in the notebook now. Fig. 7b with constant-curve sets left out was not run; leaving them out would add only a constant to the best-curve mean, which cannot move its peak or minimum.
- **B2:** resolved for `derive` (responses over all dt), fig7a (excluded) and fig7f (reading c).
- **B3:** two more scoring readings were run, still with no unsmoothed curve. This is now an open question to the authors.

Remaining points that bear on a conclusion:

1. **B1, the selective group.** The main analyses still use the uncalibrated test: 318 sets, with 24.6% false positives on the real-data null.
   - Five outcomes depend on which group is used, and all are marked: supp4, fig7a, fig3g, supp8, and fig6b-enhancement-not-different under O3 (b).
   - The variant group fixes its size at the paper's 187. No claim was run on the calibrated group of 162 sets, which would be the less arbitrary alternative.
2. **B6, outcomes at a band edge**, each of which could flip within noise:
   - fig3g: 0.633 against a lower bound of 0.63.
   - supp8: 0.584 against a lower bound of 0.585.
   - supralinear: 0.0723 against a lower bound of 0.072.
3. **B3, methods-dt-modulation:** not reproduced, and no reason has been found.
4. **B4, a gap in the claims file:** it carries the paper's "4.8 spikes per stimulus" without noting that the value is most likely in Hz. The outcome correctly uses the claims file's unit.
