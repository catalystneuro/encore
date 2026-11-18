I've worked through all ten points in the round-1 report and re-run the entry. The checks pass with 0 errors, the notebook runs in 549 s, and I checked the conclusions against the new numbers. Nothing is committed.

**Outcome changes**
- **figs5c-latency-order** is now not reproduced (was partially reproduced), as the verifier gave it. The criterion has no partial outcome, and its one test fails in OFC and ACC under every reading. The parts that do hold (DLPFC, and spatial attention coming first in ACC with the script's set of variables) are in the notes.
- **chose-on-partial-information** stays reproduced but is now marked as resting on an assumption. The paper doesn't define what counts as a cue "evaluated", and the result depends on it: the script's count gives 85.5/71.4, raw fixations 54/43, and the 250 ms rule 96/92. I added a finding asking the authors to confirm the script's count.
- Every other outcome is unchanged. The verifier agreed with all of them.

**Added or corrected, by point**
1. **Figure 6, point 1:** every reading is now also run with the Methods' two-column projection. fig6c and fig6d hold in all 36 readings under it.
2. **Figure 6, point 2:** every reading is now also run with the action weights at −200 ms. fig6e holds in 16 of 72 readings at −200 ms, 12 of 72 with the scripts' design and bin, and 6 of 72 with the Methods' projection. The 12 include the scripts' own choices.
3. **Figure 6 random halves:** the "100 random halves" reading now uses the halves the scripts stored in the data set. The weights computed from them match the stored ones to within 2.6e-07.
4. **Figure 6, point 6:** a new reading draws halves once per session so that units recorded together share them. It agrees with the others.
5. **Figure 5g-j, point 3:** all nine epoch-pair blocks are now computed, each with its own null, as the script does. Clusters now use 8-connectivity to match the script; they were 4-connected before, which was a bug. The single 183 × 183 map is shown as a variant. The criterion holds under both, though the two cue 3 option maps pass the 183 × 183 test only narrowly (1105 vs 1083, 817 vs 810).
6. **Fisher tests, point 4:** added a variant with units 87 and 653 put back and the paper's n. Five of six tests are still below p < 0.05.
7. **Figure 8, point 5:** the exact binomial test is now shown beside the script's formula. Only one fig8-spatial reading still passes under it, which is enough.
8. **Figure 8 validation:** the cue 1 regression matches the stored T-statistics to within 3.3e-07. The authors' stored significance flags give ACC 18.5% and DLPFC 17.2%, which would pass fig8-action-value. I kept that claim partially reproduced, because those flags are the paper's result and not something computed here. The flags differ from mine on 2.1% of ACC units, which looks like permutation noise.
9. **Supplementary Table 1, point 9:** compared session by session. It matches all units in all 53 sessions, but only 26 of 53 once units below 1 Hz are removed. So its caption ("above 1 Hz") is wrong, and I recorded that as a finding about the paper.
10. **Point 10:** the one-sample shift in `conv_same_200` matches MATLAB's `conv2 'same'` for an even-length kernel. The docstring now says so.

Other changes:
- **Script lines:** the data-check section now prints the script lines the verifier couldn't see: unit exclusions, the one-sided RSA test, the Supplementary Figure 5C variable set, the Figure 7 thresholds, the Figure 8 binomial formula, `ttR(30)` and the per-unit random halves.
- **Questions for a reader:** added two to `questions/hunt-2018.yaml`, for points 7 and 8. Neither claim was changed.
- **Records:** the round is recorded under `verifications` with all 40 claims, and the README and `entry.yaml` are updated (runtime raised from 14 to 16 minutes).

**Not done**
- I didn't read `info_gathering_ramp_to_choice.mat` (5.3 GB) to check the Figure 6 projections. The stored halves and weights in the smaller results file check the weights instead.
- The data set has no stored RSA output, so the RSA can't be checked against the authors' own results.
