I checked the CRCNS:pfc-6 claims file against the paper, made nine corrections, and it is ready for an attempt (`ready: true`).

**Checker result line:** `29 claims, 29 quotes, 19 statistical values, 3 problems`. All three problems are p-values printed as powers of ten in the extracted text, which the checker can't parse: 1e-5 in fig2b-pre-weaker, 1e-10 in fig5b-spwr-triggered and 1e-5 in replay-in-delta-spindle-periods. I found each of them in the paper by reading. The run after my edits gives the same line.

**Changes, by claim** (each is also recorded under `checks`):
- **supp5-sws-only:** The statement said replay was "restricted to" SWS; the paper's wording supports "concentrated in", so I changed it. The criterion used a paired t-test for post against pre outside SWS, but the paper gives no such test. It is now marked open, with paired t-test and Wilcoxon as the two readings. What the ANOVA's observations are is also marked as a reading.
- **supp6-pre-post-sws-alike:** The legend doesn't say whether firing rates are paired by session or by cell, so both are now listed.
- **fig2f-tail-contribution:** The expected value 45 ± 9 covered 36–54%, but the protocol's widened range for "40–50%" is 36–55%. Changed to 45.5 ± 9.5.
- **fig5a-spwr-bins:** The criterion correlated the SPWR minus non-SPWR difference with encoding strength. The figure the text cites (Supplementary Fig. 7B) plots the mean reactivation in SPWR bins instead. Both are now readings, and the text's p < 1e-20 is required.
- **fig5b-spwr-triggered:** Added a Wilcoxon reading next to the paired t-test, since the paper names no test. Tied n = 270 to the sessions with reliable ripple detection (8 + 37 + 225 in fig5a).
- **fig5d-population-asymmetric:** The windows and test were presented as standard choices, but they could change the outcome. The criterion now says the paper gives neither and offers two baselines as readings.
- **fig6c-spindles:** Added a second reading: each bin tested against the Figure 6a baseline (legend threshold p < 0.05), as the legend's "Same plots as in a" allows.
- **fig7c-choice-point:** The statement merged two findings. It now says the components appear mainly on the central platform (that sentence was added to the quote) and that the learning effect is significant only from the platform toward the target arm. The criterion now also checks that the profile after learning peaks on the platform.

**Still open:**
- I couldn't tell from the extracted text which of Fig. 6d's three r values (0.79, 0.53, 0.96) belongs to which event, and no figure could be rendered.
- In fig5e, supp10 and fig6b, the bin sizes, lag ranges and DOWN-state thresholds are the file's own choices, not the paper's. The criteria say so.
- A few minor findings have no claim: details of Supplementary Fig. 8C,E and 11C, the population activity around delta waves in Fig. 6a, and the Methods' first-versus-second-rule statement. All of the paper's main findings do have claims, and every claim comes from this paper.

Only `claims/crcns-pfc-6/10.1038-nn.2337.yaml` was modified. Nothing was committed or pushed.
