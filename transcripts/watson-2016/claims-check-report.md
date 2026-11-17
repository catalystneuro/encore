I checked `claims/watson-2016.yaml` against the paper and made eight corrections. The file is ready for an attempt. Nothing is committed and only the claims file changed.

**Checker result (after the edits):** `claims/watson-2016.yaml: 53 claims, 52 quotes, 64 statistical values, 0 problems`

**Changes, by claim:**
- **tables1-state-durations:** The file said the 5918 s WAKE-SLEEP duration "cannot be" the sum of the two medians. A median of sums need not equal the sum of medians, so that was overstated. It now says the value is likely misprinted: it is far above 3613 s and its SD is too small. It is still not judged.
- **ma-fraction-over-nrem-episodes:** I removed the "10 bins" reading. The paper never gives it, and 10 bins cannot reach the reported p < 1e-10 at R = −0.85 (the best is about 0.002). I also corrected "few points" to "at least about 36".
- **fig2a-skewed-wide-distribution:** The statement now includes the supra-lognormal low tail, which the quoted sentence states. The shape and range are now judged on rates pooled over all states, as the Results ("Across all states") and the Figure S2C legend say, and no longer on WAKE alone.
- **first-last-packet-mean-rate, post-sleep-wake-lower:** The file fixed the Wilcoxon test as two-sided, which the paper never says. Sidedness is now named as open, with one-sided as a reading (the Fig. 3E legend uses one-tailed tests).
- **fig3f-within-up-changes:** The criterion required significance from a test the paper does not report, for changes it does not call significant. These are now judged by sign, with the test reported.
- **figs3a-first-last-rem-ma-slopes:** The S3A legend gives no confidence level for any of the three intervals, not just WAKE. The criterion now says so.
- **fig5c-wake-movement:** I removed "n = 24 triplets" from the statistics, since the paper gives no n for this correlation. The criterion now notes that 24 is consistent with the reported R and p.
- **fig4cd-packet-rate-lfp-correlations:** The statement says the other correlations are not significant, but the criterion never tested that. The Fig. 4C legend says low-rate cells show no significant correlation with the slow-wave measures, so those four checks are now judged at p < 0.05.

**Open (recorded in the file):**
- **fig4-updown-within-packets:** The Results say the fraction of time in neither UP nor DOWN "increased", but print R = −0.04. It stays reported and not judged.
- **fig4-spindles-within-nrem:** The packet spindle incidence R = 0.7 is probably a misprint for 0.07, so only its sign and p are judged.
- **fig3c-spindles-over-sleep:** Spindle incidence is 1.94/min in the Results but 0.049 Hz (2.94/min) in Table S1. It is judged on the Results value.
- **wake-sleep-cycles:** The paper says 2.0 episodes "per neuron recorded"; this is read as per session, the only reading that gives 2.0.
- **Coverage:** Every main finding has a claim, and every claim comes from this paper. Only minor interneuron remarks (Figure S2C–E) have none.

The `checks` entry is at the end of the file with `ready: true` and 13 lines: one per change and one per open problem.
