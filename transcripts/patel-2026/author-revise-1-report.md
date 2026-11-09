I've revised the attempt for every point in the round-1 report, re-run the entry (`tools/entry.py all`: 0 check errors, both notebooks pass in 7 and 4 min), and recorded round 1 under `verifications`. Nothing is committed.

**Outcomes that changed**
- **fig2c: partially reproduced → not reproduced**, as the verifier gave. With the 2022 cohort no step is Sidak-significant (smallest adjusted p 0.116) and the curves cross. It is still marked as resting on the 2022 cohort; all 37 neurons would pass.
- **fig2e: partially reproduced → reproduced**, marked as resting on the 2022 cohort and the new spike rule. With the corrected spike counting (below), females fire more at 16 and 14 of 26 steps, so "most steps" now holds at −20 mV too. The 5-mV variant still gives 12 of 26, which is stated.
- **fig3f: reproduced → not reproduced.** With cohort 9 left out the population-by-cluster test gives p = 0.88 and 0.26, and with a session-s.d. z p = 0.08 and 0.15. In the old result, 63 of the 66 nonspecific ROIs in the responsive cluster came from cohort 9.
- **fig2d, fig2-threeway, supt1-female: still blocked, now `data_missing`** (was `data_unreadable`). The 13 flat files hold only one voltage and one stimulus series, both from the amplifier's secondary channel (`VmSec`, never seen in a recorded file). Their size comes from histology images.

**Corrected or added**
- **Spike counting (B1):** the 5-mV re-arm is replaced by a 1-mV re-arm with a 1-ms dead time. Counting every crossing literally turns plateau noise into up to 98 "spikes" per step. No-re-arm and 5-mV variants are shown for every excitability claim.
- **Cohort 9 z-score (B3):** the Methods' baseline z cannot be computed sensibly on cohort 9's nonnegative traces. With the floor 62% of bout-neuron pairs are undefined and the rest biased downward; without it z reaches about 1e20. The BLA claims are now judged with cohort 9 left out (an assumption, leaving 4 nonspecific mice), with the old reading and a session-s.d. z as variants. The per-cohort diagnostics and a synthetic check are printed.
- **ed3c (B4):** added a pooled-error Tukey test. Rank 1 is still never below rank 2 (smallest p 0.065), so it stays partially reproduced.
- **Stimulation claims (B5):** nonstimulated trials are now type 3 only, as the criteria say. No outcome changed.
- **Trial types (B8):** every mismatching mPFC session is a clean swap of forced types 1 and 2. I dropped the "matched sessions" variants and corrected the finding.
- **Smaller points:**
  - `t0` is printed (0 in every file).
  - The ed9c files' footprints turn out to be every ROI (80 to 191 per session).
  - The single-lick limitation and the independent-ROI chi-square are now stated.
  - The questions for the authors now cover the z-score and spike counting.
  - I tightened my own reading of "falls back toward 0" for ed5d. It stays not reproduced under every reading.

**Not done, and why**
- **ed9c** stays blocked as `not_runnable`: CellReg is MATLAB, and a registration I wrote myself would not be the paper's method. The notes say the deposited data would allow the test.
- **ed6cd** stays `data_missing` (the verifier said `metadata_insufficient`): the tube-test ranks are measurements the dandiset doesn't hold, not a missing label.
- **The cohort-to-population and 2022-cohort assumptions** (B6, B7) can't be settled from the dandiset. They stay marked and are asked of the authors.
- **No reader questions** were added: the report names no place where the claims file misreads the paper.
