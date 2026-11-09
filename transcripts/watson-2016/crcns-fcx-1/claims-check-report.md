I checked the claims file against the paper and corrected it. The checker passes and the file is ready for an attempt. Nothing is committed.

**Checker:** `claims/crcns-fcx-1/10.1016-j.neuron.2016.03.036.yaml: 41 claims, 41 quotes, 64 statistical values, 0 problems`. That was 63 before; I added one statistic.

**Changes to the shared method notes at the top of the file (M2 to M7)**
- **M2:** Figure S2 numbers the sextiles from lowest rate (1) to highest, and the Figure S5 legend numbers them the other way.
- **M3:** added a third reading, 50 time bins. Every R and p printed in Figure S5A and S5B matches a Pearson test on exactly 50 points. The R and p printed in Figure S3C imply about 873 points, which fits one point per packet but doesn't prove it.
- **M4:** where the paper prints an exact p, the bound is now stated as the next power of ten above it. Some criteria already used this rule without saying so.
- **M6:** the R and p in Figures S5C to S5G imply one point per cell.
- **M7:** gave the reason for keeping 10% tolerances where the paper reports a median or mean ± SD.

**Changes by claim**
- **packet-duration:** added a criterion; it had none.
- **fig2a-pe-rate-distribution:** the 5th to 95th percentile range had been presented as the paper's; it is now one of two readings. I noted that 0.05 to 5 Hz is two orders of magnitude, while the paper says three.
- **fig2b-wake-nrem-slope:** the test is now "correlation", since the paper doesn't call it Pearson. I removed a rule that let the slope pass if its confidence interval merely overlapped the paper's, which widened the paper's interval without a source. The source now cites the figure legend.
- **fig2c-autocorrelogram:** the 100 to 150 ms window for the theta peak was made up; it is now an expected value of 125 ms with 10% tolerance. I added an exponential-fit reading, because the paper doesn't define "decay fit exponent".
- **updown-durations:** added two detection rules from the supplement that were missing.
- **fig1e-up-state-dynamics:** the gamma-then-sigma part of the statement was only reported; it is now judged. Choices the paper doesn't make are labelled as such.
- **fig2de-fast-before-slow:** the legends disagree on what is split in half (halves of SLEEP or halves of the session), so both are readings. Pearson and log rate are labelled as standard choices.
- **fig2f-rate-group-correlations:** the paper says the slowest group is also positively correlated within itself; this is now in the statement and the criterion.
- **first-last-packet-mean-rate, post-sleep-wake-lower:** the paper says only "Wilcoxon test", so signed-rank and rank-sum are both readings.
- **figs3a-first-last-rem-ma-slopes:** added the Pearson p < 1e-10 from the Figure S3A legend.
- **fig3f-within-up-changes:** the p bound is now stated (p < 1e-8).
- **fig3c-updown-over-sleep:** defined the "neither UP nor DOWN" time.
- **fig4-lfp-within-nrem:** the criterion counted five trends where the statement has six. The packet-length correlation now follows the Results, and the legend's 1 to 4 Hz delta band is a variant.
- **fig4-updown-within-packets:** the paper doesn't define the UP/DOWN ratio; two readings are named.
- **fig4e-late-packet-sigma:** each of the two tests now says what it compares.
- **fig4-sextiles-within-nrem:** extended the quote to cover the burst index statistics.
- **fig4e-within-up-sextiles:** the paper doesn't say whether its test compares UP states or cells; both are readings.
- **figs5-within-wake-rem:** the 20 bins were a free choice and are replaced by the 50 bins the printed statistics imply. "The fourth" sextile now follows the S5 legend's numbering, and the extracted S5A values are recorded.
- **fig5b-ma-nrem-ma:** the WAKE rate is read both as log10 and as linear.
- **fig5c-sigma-ma-change, fig5b-wake-between-packets, fig5b-rem-between-packets:** the sigma normalization and the movement measure are labelled as standard choices, and "REM theta power" has two readings.
- **burst-index-by-state:** labelled a handling choice as standard.

**Still open**
- The main paper PDF wasn't supplied, so values printed only inside Figures 2 to 5 remain unread. These are the per-sextile R and p of Fig. 3B and 4A-B iv, and the triplet counts and significance stars of Fig. 5B.
- The extracted Figure S5A values contradict the Results sentence on WAKE in either sextile order. The claim judges the Results sentence.
- Tolerances for values given as ± SD are 10%. The protocol's "stated spread" could mean the SD, but that would leave values such as the pE WAKE median (0.76 ± 1.53 Hz) untestable.
- The rise in sigma and fall in delta at the end of packets has no claim. It is a minor finding.

All 41 claim ids are unchanged. The file has no claim taken from outside this paper, and every main finding has a claim. The `checks` entry is dated 2026-11-07 with `ready: true`.
