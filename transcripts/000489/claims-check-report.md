The claims file for 000489 is ready for an attempt, after the corrections below. Nothing was committed.

**Checker result:** `22 claims, 22 quotes, 7 statistical values, 0 problems` (it was 21 claims, also with 0 problems, before my changes).

The quotes, sources and the recorded p-values (p < 0.01, p < 0.05, p < 0.0001) all match the paper. The main fault was in the criteria. Where the paper leaves a method detail open (paired or unpaired t-test, which fit function), the file either let any one choice decide the outcome or required all of them to hold. The protocol says these choices must agree, and the claim is methods_underspecified when they do not.

**Changes, by claim**
- **fig2a-uptake-rises-with-field:** if paired and unpaired disagree, the claim is now methods_underspecified, not "not reproduced". I noted that the paper reports no test for this finding.
- **fig2a-vertical-scales:** the statement said uptake was "several-fold lower", which the paper does not say. It now gives only the axis limits (1200 and 250 a.u.).
- **fig2b-exponential-same-slope:** the rule for judging the exponential fit adequate is now marked as the file's own, not the paper's.
- **fig2c-inhibition-flat-above-8-7, fig5-ns-symmetric-along-aa, fig7-summation-without-buildup:** each had fixed the test as paired, which the paper does not say. Both paired and unpaired now run and must agree.
- **fig2c-weaker-at-6-7, fig5-us-anode-stronger:** paired and unpaired must now agree. For fig2c I also added a second reading of "compared to the higher field strengths": against the higher fields pooled.
- **fig3-uptake-linear-in-pulse-number:** the expected ratios 2 and 3 are now marked as read from the axis scaling, since the paper prints no ratio. The two ways of measuring the ratio must agree.
- **fig4ac-ns-bipolar-20-25pct, fig4d-1200ns-tenfold, fig6cf-833khz-thirtyfold:** the legends say fits were "either exponential or polynomial", so three fit choices now run and must agree. I noted that the 7 to 8 kV/cm cutoff comes from Fig. 3. In fig6cf the ratio of means is now a variant only, since the legend uses the ratio of fits.
- **fig4eg-us-bipolar-30-50pct:** the ratio only had to fall in 27 to 55% "at some field", which almost any curve would meet. It is now read as the mean over the range or the whole curve.
- **fig7-bipolar-overshoot:** "same polarization" used a rule of thumb about gaps between error bars. It now uses the paper's t-test (unpaired, as the cells differ), with the error-bar rule as a variant. The made-up "more than its s.e.m." threshold is replaced by a t-test at p < 0.05.
- **fig7-summation-without-buildup:** a later peak lower than the first now also counts as not reproduced. The s.e.m. threshold is replaced by a t-test, as above.
- **fig1e-heating:** the statement now includes that 833 kHz heating went above 30 °C but stayed below 44 °C, and that these were the worst-case settings.
- **Added fig6cf-cancellation-stronger-at-high-field:** the Discussion's finding that a stronger field increased cancellation for high-frequency bursts had no claim.

**Still open** (recorded under `checks`)
- The paper does not give the spacing of the regions of interest along the two lines, or a background cutoff for Fig. 4E to H and Fig. 6.
- Many criteria apply the paper's general t-test to comparisons where the paper reports no test. Those tests are the file's readings, not the paper's results.
- The field strength of each region comes from the paper's simulation, which is not deposited. If the dataset does not hold it, the author has to recompute it from Methods 2.3, and decide whether those claims should be marked `data: with_inputs`.
