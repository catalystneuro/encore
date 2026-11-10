The claims file is ready for an attempt (`ready: true`). I made nine corrections and recorded three problems that stay open. Only `claims/laboy-juarez-2019.yaml` changed, and nothing is committed or pushed.

**Checker result:** `claims/laboy-juarez-2019.yaml: 50 claims, 50 quotes, 24 statistical values, 0 problems` (the same before and after my edits).

**Changes, by claim**
- **exp2-units:** reading (b) tested responsiveness on two-whisker responses against sham, which the paper never does. The Methods use the nine single whiskers plus sham. I replaced it with the two direction readings (O2) and noted that only the first lets the correlated and anti-correlated counts differ.
- **fig1g-cwsw-sharper, supp2-sw-tuned-sharpest-cwsw:** the partial rule said "at most N", which is meaningless. It now says "at most values of N".
- **fig2f-shuffle-abolishes-tuning:** the paper does not say how the shuffled curves are aligned. I named two readings: aligned to the measured best combination, or to the shuffled curve's own peak. The flatness test applies only to the first, because aligning to a curve's own peak creates a peak by itself.
- **fig3g-binary-decoder:** the paper does not say which units this decoder samples. I named two readings: the 187 selective units (as in Fig. 3e and the Fig. 8k legend), or all 451.
- **fig6b-suppression-greater-selective:** the file paired P = 0.001 with rank 7 and P = 0.002 with rank 8. The text gives both values for "the two weakest" without saying which is which, and the `about` fields now say so.
- **fig7f-inbound-sharper:** the groups (121 + 56) cover 177 of the 187 selective units. I added a reading that drops units whose best-combination curve was set constant across dt, since those have no best dt.
- **fig7g-inbound-decoding:** the paper says this decoder is built "as in Fig. 4", and Fig. 4 decodes CW-tuned and SW-tuned units separately. I added that as a reading. I also stated that the [0, 9] range counts with the outbound ranges.
- **fig5c-sublinear-at-all-dt:** added an `about` to the statistics entry, because the legend's P < 0.001 marks several pairs without saying which.
- **Header, decoders:** the Fig. 3e legend says 1,000 resamplings where the Methods say 2,500. I noted it; the count cannot change the means.

The other claims match the paper: statements, sources, statistics (results, not counting thresholds), expected values and tolerances. Every main finding has a claim, and none comes from outside the paper.

**Still open (recorded in `checks`)**
- **No code:** the authors' code is only "available upon request", so all methods come from the text. The sparseness and supralinearity formulas are read from a garbled extraction.
- **Thresholds the file chose:** several criteria use cut-offs the paper does not give, and each criterion says so.
  - "Nearly all" and "virtually all" are read as at least 90% of units.
  - "Nearly absent" in fig7e is read as under a third of the effect in selective units.
  - fig8k requires accuracy above 0.7 at an ensemble of 25 units.
  - Several claims use s.e.m. or s.d. margins and partial-credit thresholds.
- **Experiment 3 smoothing:** the paper does not say whether dt smoothing is applied with only three dt values. exp3-combination-selective reads it as not applied, with no second reading.
