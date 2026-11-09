**Verification report, round 2: Varela & Wilson 2020 (eLife 48881) on CRCNS hc-24**

The claims file has 46 claims and the attempt record has 46 outcomes: 8 reproduced, 19 partially reproduced, 7 not reproduced and 12 blocked (6 data_missing, 1 metadata_insufficient, 5 other). The notebook summary, the README table and the record agree on these.

### 1. Outcomes and assumptions

**I agree with 43 of the 46 outcomes.**
- **fig2c-swr-around-kc (partially_reproduced).** I said not_reproduced in round 1 and now accept partial.
  - The criterion has no partial clause, but the attempt treats other such criteria the same way.
  - Both rises hold in every session and reading.
  - The failed parts are stated in the notes: the minimum falls 30–60 ms before the KC, and 3 of 5 values at most are in tolerance.
- **fig4-units-not-rhythmic (not_reproduced).** Now valid. The fixed finder returns 100 ms on the synthetic 10 Hz process under all six settings, and no reading meets the criterion. At smoothing 0 the "first minimum" of the MUA curves falls at 15–60 ms, so those lags (20–75 ms) sit on noise. The "measured" values come from that noisiest reading, but the outcome is the same under every reading.
- **fig6-modulation-with-ripple-power (not_reproduced).** I agree: no reading has a majority increasing, so even the criterion's partial clause fails. One caveat: on flat firing the corrected index is 0.07–0.17 for half the cycles. The two S3 units differ by only 0.03–0.08 between high and low cycles with the deposited troughs (cell 108), so their direction is within noise. Only the S1 unit's decrease is clearly larger than the noise.

**I disagree with 3 outcomes: modulation-amplitude-versus-ripple, fig6e-quartile-synergy and fig6f-quartile-versus-median.** All three stay "blocked: other (too few units)". The record now rates other claims whose test cannot reach p < 0.05 at this n on their values and directions, following the claims file's "Unit samples" paragraph: kc-regions-compared, thalamus-at-spindle-nested-swrs, swr-shift-control and fig3a. kc-regions-compared is itself a contrast of significant and non-significant tests, as is modulation-amplitude-versus-ripple. In round 1 I agreed these three were blocked, but their quantities did not exist then. Under the attempt's own rule they now have outcomes (cell 108):
- **modulation-amplitude-versus-ripple:** the amplitude split raises the index in 3, 2 and 2 of 3 units, the ripple split in 1, 1 and 0 of 3, and the similarity tests give p ≥ 0.25. The direction matches the paper, so this is about partially_reproduced.
- **fig6f:** the upper-quartile amplitude index is above the ripple-power index in every reading. Both means are within tolerance in the methods and results readings. The F ratio is larger for amplitude in 5 of 6 readings. This is about partially_reproduced.
- **fig6e:** the Spearman rho is negative in 5 of 6 readings, where the paper reports +0.51. 67–100% of units increase with amplitude in the top ripple-power quartile, where the paper reports 32%. This leans toward not_reproduced.

**Assumptions.** No outcome carries `assumed: true`. fig1s3 no longer rests on the scalogram scaling, because both scalings are shown. The methods_unavailable finding still says "This attempt assumed power relative to the mean power"; that is now only background, not the basis of the outcome.

**Claims file.** I found nothing new that misreads the paper. The round-1 notes on the claims file still stand: readings (i) and (ii) of the GLM are the same number, and the rebound criterion sets no minimum size for r. The question on the rebound criterion is put to a reader.

### 2. Statements the printed numbers do not support

- **Cell 166 (Summary):** "the claims blocked only because a test or tolerance band cannot be met at this n are now tested on their values and directions". Three claims are still blocked for exactly that reason (cells 112, 115, 118).
- **Cell 74 (fig3f):** "the z-scored reading (c) gives a negative thalamic mean". Cell 73 prints −0.027, +0.031 and −0.128, so one reading is positive. The record's "−0.128 to 0.031" is correct.
- **Cell 80 (fig4):** "thalamic unit peaks are not later than MUA peaks under any reading". In two readings the mean unit lag is later than the all-spike MUA lag: 143 vs 135 ms (5 ms bins, smoothing 2) and 84 vs 55 ms (10 ms bins, smoothing 0). Neither difference is significant (p ≥ 0.15). The sentence should say "not significantly later".
- **Record, fig3s1-ca1-mpfc-at-swrs deviation:** "depends on fig3c-thalamic-decrease-at-swrs, blocked for too few thalamic units". fig3c is now not_reproduced; this text is left over from round 1.
- **Record, glm-thalamus-anticorrelated-swrs:** "Wald p < 1e-10". Cell 50 prints p only to 5 decimals (0.00000), so the bound is not shown.

Every other conclusion sentence, the rest of the Summary, the README and the record notes match the printed outputs. That includes all "measured" lists, the fig4 counts ("3 of 12 readings", 5–52%), the fig6e/f ranges and the fig3a sleep variant (19 and 44 min, and S2's 11 min outside the deposited sleep).

The verification block states my round-1 reasons faithfully, as close paraphrases with my numbers. Where it folds a numbered problem into a claim's reason (REM in waking for fig1s3, the single shift for swr-shift-control, kappa for fig7b, the cell 67 wording for fig5c-delta), the attribution is right.

### 3. Round-1 points

**Resolved:**
- 1, the autocorrelogram peak finder.
- 2, the modulation-index edge bias: flat firing now gives 0.06–0.17.
- 3, the blocked status, except the three claims above. The cell 67 wording is fixed.
- 4, every missing quantity is now computed.
- 5, M-sleep readings (b) and (c): they find no sleep, and the fill-short-dips variant is shown.
- 6, the cycle-permutation control: the in-cycle peaks stay at z 7.09 and 4.18.
- 9, b1' = 4·b1.
- 11, 20 shift draws per SWR; REM and the shared S3 SWRs are stated.
- 7, kappa: answered; kappa is still about 125 in the sparse reading but is not used in any criterion.
- The deposited script lines are now quoted (cell 14): S1 is MD, the S2 units are a thalamic pair, and the phase binning and normalisation come from the script.
- The S3 mPFC epoch is recorded as a finding.

**Remaining that bears on a conclusion:**
- The blocked status of modulation-amplitude-versus-ripple, fig6e and fig6f, as in part 1.
- fig6: the per-unit direction for the two S3 units is within the noise of the index. This weakens "not reproduced" but does not reverse it.

**Remaining that does not bear on a conclusion:**
- Reference reading (b) of M-KC and M-SWR (all immobile time) was not run and the record does not answer it. The KC counts agree with the deposit, so this is unlikely to matter.
- The phase bins still drop (3.058, π], following the deposited script.
- I did not view the rendered figures.
