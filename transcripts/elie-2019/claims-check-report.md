I checked `claims/elie-2019.yaml` and it is ready for an attempt (`ready: true`). Only that file was changed; nothing was committed or pushed.

**Checker result:** `claims/elie-2019.yaml: 26 claims, 26 quotes, 10 statistical values, 1 problems`. The one problem is `VALUE NOT FOUND fig9b-cii-tau-ratio 2.37e-07`, and it is a false alarm. The text prints the value as "2.37 10 −7" (Results, Analysis of the categorical information, paragraph 3), and the checker doesn't match that format, so the value is right and stays.

**Changes, by claim:**
- **Header, Method A:** said the regressions print F(2,195) or F(1,195); all three print F(2,195). I recomputed the p-values: the printed 0.0042, 0.00258 and 0.0047, and the adjusted R2 values, match F(1,195) and not F(2,195). So the first reader's interpretation (one predictor, about 197 units) holds.
- **fig1-model-neurons:** the 1.8-bit threshold for "approaches the maximum" is not in the paper. It is now labelled a fixed choice.
- **fig2a-poisson-test:** the tolerance on the count of 5 units was 0.5, while the criterion allowed ±1 unit. Set to 1 so they agree.
- **fig2b-noise-correlations:**
  - The source said paragraphs 3 and 5; the stimulus-correlation sentence is in paragraph 4.
  - The criterion followed the code's noise correlation (deviations from the delete-one mean, pooled sums). The Methods say a Pearson correlation of spike counts in successive bins, averaged over bin pairs and stimuli. The Methods version now comes first and the code's is a variant.
- **fig7a-time-constants:** the 100 to 600 ms range in the statement was not tested; it is now reported.
- **fig10-cii-distance:** the adjusted R2 must now be within tolerance for "reproduced". Before, only the partial outcome depended on it.
- **fig10-cii-area-anova:**
  - Added an expected value for the adjusted R2 of 0.027.
  - The printed numbers contradict each other: F(4,185) = 2.77 gives p = 0.029 (not 0.042) and an adjusted R2 near 0.036 (not 0.027). The criterion now says so, holds the test to p < 0.05 and reports all three side by side.
- **fig10-tau-k300-distance:** the adjusted R2 values are now part of the outcome, and the partial cases are restated.
- **cii-unimodal:** the source is Discussion paragraph 8, not 7.
- **s2-spike-counts (new claim):** the S2 Fig results had no claim. They are: no 10 ms bin holds more than 8 spikes, one bin holds 8, and the mean count per bin is 0.108.

Every other claim matched the paper: statements, sources, quotes, statistics and tolerances.

**Still open (recorded in `checks`):**
- I did not open the code repository. The code details in the file (S1 Fig power and coherence steps, bins from 10 to 610 ms, the one-tailed p, CICRand, CsteRate) rest on the first reader's account.
- S3 Fig, a comparison of estimation methods on one example neuron, has no claim. That neuron is not identified in the paper.
- For the area ANOVA, the text cannot show which of the printed F, p and adjusted R2 is wrong.
