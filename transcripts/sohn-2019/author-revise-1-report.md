I've addressed every point in the round-1 report. One outcome changed, I added four questions for a reader, and the entry re-ran cleanly: both notebooks pass `python tools/entry.py all entries/sohn-2019` and the check reports 0 errors.

**Outcome changed**
- **beh-long-more-bias** is now `partially_reproduced`; it was `reproduced`. The Methods and the Table S1 legend both write the regression without an intercept (tp = βts + ε). My earlier choice to add an intercept went against the paper, so I now follow the paper. Through the origin, the Long slope is below the Short slope in 3 of 4 datasets (Eye Right is 1.027 against 1.016). The outcome is no longer marked `assumed`. I removed the `methods_unavailable` finding that asked about the intercept, since the paper answers it.
- **beh-slopes** now also uses the through-origin regression as its main reading and stays `not_reproduced`. No reading has all 8 slopes below 1.

**Added or corrected, all shown in the notebooks**
- **Table S3 (beh-bayes-model):** the fitted wm and wp are compared with the paper's values (wm 1.5 SD below to 1.3 SD above the session means; wp 0.2 to 1.0 SD above). The fits are interior: relaxing the lower bound changes nothing. With wm held at Table S3's means, bias R² still reaches 0.8 in 2 of 4 datasets, so the low Eye wm do not decide the outcome. A likelihood profile for Eye Right shows bias R² stays at or below 0.146 at any wm.
- **Narrower smoothing kernels (SD 20 ms and 17 ms):**
  - pca-dimensionality: 2 of 8 and 3 of 8 counts in range, still not reproduced.
  - encoding-bayes-beats-linear: these kernels would make it not reproduced. Its outcome stays partially reproduced, on the claims file's SD of 40 ms, with the difference in the notes and asked of a reader.
  - All other trajectory claims keep their outcomes.
- **GPFA z-scoring over all trials:** p = 0.074 (0.039 to 0.074 across seeds and dimensions), so the outcome is unchanged.
- **Production windows:** 36 of 40 windows that end at the shortest tp run past Go, by up to 121.5 ms. Ending them before Go changes no outcome.
- **alt-speed-unmodulated:** using only the longest-ts trials, so every bin averages the same trials, the slopes are negative in 7 of 8. The verifier was right that the positive slopes come from attrition. I added basic bootstrap intervals (1 of 8 exclude zero) and the share of bootstrap slopes below the point estimate (median 6.2%).
- **short-in-long-control:** I ran the paper's two-way ANOVA. The interaction is F(1,3) = 1.70, p = 0.284, against the paper's F(1,7) = 161.43.
- **alt-threshold-monotonic:**
  - In the Eye datasets, which keep one component, 12 of 16 minima are sign crossings, not convergence.
  - A variant keeping at least 2 components gives a median of 260 ms before Go, so the outcome holds.
- **Speed variants:** I replaced the double division with path length over the Set-to-Go duration, and kept the Methods' literal wording as a second variant. Outcomes unchanged.
- **Leaked conclusions:** I split the two cells where "Result" text was left in the handover, so the handover tool now strips them.
- **Written conclusions:** I rewrote all of them, plus the summary, the README and the attempt notes, to match the new numbers.
- **Record:** round 1 is recorded under `verifications`, with the verifier's reasons in its words and my response for each of the 23 claims.

**New file `questions/sohn-2019.yaml`, four questions for a reader**
- Whether "kernel width: 40 ms" means an SD of 40 ms.
- Whether a single session's 48 units can be compared with the paper's PCA, which pooled 536 units across sessions.
- Which z-scoring the Figure 6C legend means.
- Whether beh-bayes-model should compare the fit with Table S3, which the claims file says was unavailable.

**Not done, and why**
- No other outcome changed, including where the verifier found a reading of the paper that would change one (narrower kernel, z-scoring). The claims file fixes those choices, so they went to questions, as the protocol says.
- glm-prior-ts's tolerance is narrower than the binomial interval for 48 units. The criterion sets the tolerance, so I only stated this in the notes.
- What `tp` measures still can't be settled from the files; it stays a `metadata_insufficient` finding, now noting the windows that run past Go.

Nothing was committed, as asked.
