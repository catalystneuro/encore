The claims file is ready for an attempt. I made six small fixes to the file and added a `checks` entry with `ready: true`.

**Checker result:** `38 claims, 38 quotes, 68 statistical values, 5 problems`. It still exits 1 because of those five. None is a wrong number: each is a p-value the checker could not match because of how the paper prints it (9.70 × 10−9, 3.9469x10-07, 8.85x10-05, 7.75x10-05, 6.45x10-05). I read each one in the text and all match the file. All 38 quotes and the schema pass.

**Checks against the paper:** statements, sources, statistics and expected values agree with the text. That includes the 595 pairs in group 1, which I found in Supplementary Table 2. I also cloned the paper's code at the commit the file cites (cdcec89) and spot-checked its code readings: the ANOVA and t-test directions, the REM and minimum-cell thresholds, the ripple-modulation threshold, the group sign error, and the one-sided tests. They match. Every main finding has a claim, and no claim comes from the data descriptor.

**Changes, by claim:**
- **fig1b-dz-speed-posthoc:** the text only states the post-run versus pre-run direction. The criterion now says the other directions come from the signs of t, which the code computes as current minus previous. It also notes that the paper never says how many tests its Bonferroni correction covers, so using 0.05/4 is a reading.
- **fig2c-bla-pyr-higher-in-sleep:** the criterion now says the code runs the signed-rank test only on the REM ratio, and the NREM ratio is tested the same way.
- **fig2c-skewed-rates:** the code does compute a skewness, but of the log REM/wake rate quotient, not of the rates. The criterion now says this does not settle how to measure the skew.
- **figs5a-hpc-bla-all-cells:** the 40–60 min z = −0.71 is marked "as printed". It repeats the REM test's z and does not fit p = 0.14458.
- **fig3e-cen-no-reactivation:** the outcome was undefined if a test came out significant with EV below REV. The absence is now judged on the paper's two-sided test alone, and the direction is reported.
- **bla-rates-safe-airpuff-absent:** the paper gives no n, so which sessions to use is also open. The criterion now names the sessions used (Figure 6 and Supplementary Figure 11b) and adds all sessions with BLA cells as a variant.

**Still open:**
- Supplementary Table 1 (cells per structure) is an image. The text does not carry its numbers and I could not render the PDF, because poppler is not installed. So the two ways of defining BLA still rest on the totals given in the Results.
- Four claims have no test in the paper: figs1c-habituation, fig2c-skewed-rates, figs6b-ev-nine-groups and figs9-ev-independent-of-rate. The pass/fail rules for these were chosen by the agent that wrote the file, and the file says so; the paper does not fix them.

Only `claims/crcns-hc-14/10.1038-nn.4637.yaml` was changed. Nothing is committed.
