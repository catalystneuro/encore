## 1. Outcomes

The claims file lists 24 claims, and the attempt record gives an outcome for each of the 24: 21 tested and 3 blocked.

| claim | record | agree? |
|---|---|---|
| beh-slopes | not_reproduced | Yes. No reading gives 8 of 8 (cell 13). |
| beh-overlap-prior | not_reproduced | Yes |
| beh-sigmoid-increments | reproduced | Yes |
| beh-long-more-bias | partially_reproduced | Yes under the stated reading, but the outcome depends on that reading (see below). |
| beh-bayes-model | partially_reproduced | Yes. The new cell 27 shows the outcome does not depend on wm. |
| glm-prior-ts | not_reproduced | Yes |
| dfr-overlap-support | reproduced | Yes |
| pca-dimensionality | not_reproduced | Yes by the criterion. The population question remains open (section 3). |
| encoding-r2 | reproduced | Yes by the criterion. The criterion cannot tell u from a random axis (cell 43). |
| encoding-bayes-beats-linear | partially_reproduced | Yes under the claims file's SD of 40 ms. It becomes not reproduced at SD 20 or 17 ms (cell 56). |
| short-in-long-control | reproduced | Yes by the criterion, which cannot fail. |
| neural-long-more-bias | partially_reproduced | Yes |
| speed-vs-projection | partially_reproduced | Yes |
| initial-speed-biased | not_reproduced | Yes (p = 0.0547) |
| speed-predicts-tp | partially_reproduced | Yes |
| alt-speed-unmodulated | reproduced | Yes by the criterion, which cannot fail. |
| alt-transient-parallel | reproduced | Yes |
| alt-threshold-monotonic | not_reproduced | Yes |
| gpfa-variance-inverted-u | not_reproduced | Yes, borderline (0.039 to 0.098 across variants). |
| gpfa-mean-sigmoid | reproduced | Yes |
| rnn-curved-manifold, rnn-perturbation, monkey-g | blocked (data_missing) | Yes |

**Assumptions.** No outcome is now marked `assumed: true`. One outcome still rests on a choice the claims file leaves open: beh-long-more-bias.
- Its criterion says only "weighted linear regression". The regression through the origin follows the Methods and the Table S1 legend literally (tp = βts + ε), and it gives 3 of 4 (partial).
- With an intercept, every variant gives 4 of 4 (reproduced) (cell 23).
- The two readings carry different meaning. Through the origin, the slope absorbs the constant offset that the paper's own Bayesian model fits as b (fitted b of up to 50 and −81 ms, cell 26). That makes the slope mostly mean tp/ts. The deciding difference is Eye Right, 1.027 against 1.016. The intercept reading is at least as plausible.
- My round-1 problem 3 pushed toward the literal reading. The record should restore `assumed: true` for this outcome and add this question for a reader. beh-slopes is unaffected, since no reading passes.

## 2. Sentences the printed outputs do not support

- **Notebook cell 78 (Summary):** "about 80% of the session's trials are analysed." The analysis uses 983 of 1443 trials, which is 68% (cell 4). 80% (1160 of 1443) is the share of trials in the train file.
- **README:** "no signed-rank test over datasets can fall below p = 0.125, and the three claims of absence are reproduced by tests that cannot find an effect." This holds for short-in-long-control and alt-speed-unmodulated. alt-transient-parallel tests 8 dataset-priors (cell 72), so it could reach p = 0.0078 and could have failed.
- **Attempt record deviations:** the sentence "a signed-rank test over 4 values cannot fall below p = 0.125" is attached to claims whose tests run over 8 values or use no signed-rank test at all:
  - initial-speed-biased, 8 values, p = 0.0547
  - alt-transient-parallel, 8 values
  - gpfa-variance-inverted-u and gpfa-mean-sigmoid, 8 values
  - encoding-r2, speed-vs-projection and speed-predicts-tp, Pearson correlations
  - alt-threshold-monotonic, median time of the minimum

  For initial-speed-biased this misstates the test that decided the outcome.
- **Record (gpfa-variance-inverted-u deviation) and GPFA notebook cell 16:** "The paper used one high-yield session of 48 units for H." The paper says "high-yield sessions (N=48 for monkey H)". It does not say this was one session.
- **Cell 70 and the README** ("slopes positive only with attrition"): "this follows from attrition." The control (cell 69) changes more than attrition. It uses fewer trials (18 to 31) and only the longest-ts trials. "Consistent with attrition" is what the numbers support. Calling the basic bootstrap the one "which correct[s] for that" also overstates it: the point estimate itself carries the attrition bias.
- **Robustness results cited selectively (cells 41, 54 against cells 45, 60, 66).** The unsmoothed variant is cited where it favours the claim: 5 of 8 for pca-dimensionality and 4 of 4 for neural-long-more-bias. Where it reverses outcomes, cell 56 is not mentioned:
  - speed-vs-projection: r = +0.255 and −0.036
  - speed-predicts-tp: r = −0.103 and −0.310
  - encoding-r2: Hand Left Long 0.581; 4-dataset mean 0.847 and 0.813

  With outlier trials included, speed-predicts-tp Long is r = −0.439. I computed p ≈ 0.053 (n = 20), so that variant would be not reproduced. No stated outcome changes, because neither variant is the claims file's method, but the conclusions should report these variants in both directions.

I checked every other "Result:" sentence (cells 10, 15, 18, 21, 24, 29, 33, 36, 41, 45, 48, 51, 54, 60, 63, 66, 70, 73, 76; GPFA cells 11 and 14), the rest of the Summary, the README and the record's notes against the printed outputs. The numbers match, including the Table S3 z-scores, the profile range and the narrow-kernel values.

**My round-1 reasons in the record:** they are stated faithfully and in my terms, with the B-problems attached to the right claims. Problem 1 (pooled population) is attached only to pca-dimensionality, though I also tied it to the tolerances of the trajectory claims. This is minor.

## 3. Round-1 points

**Resolved:**
- 3, Table S3: compared; the relaxed bound and the profile were run. My claim that a low wm drives the poor Eye R² was wrong: R² stays at or below 0.146 over the whole profile.
- 4, GPFA z-scoring: run; p = 0.074, outcome unchanged.
- 5, attrition: a control without attrition and basic bootstrap intervals were added.
- 6, ANOVA: run; interaction F(1,3) = 1.70, p = 0.284.
- 7, windows past Go: 36 of 40 run past Go; the variant ending at Go changes no outcome.
- 8, crossings with one component: counted, plus a variant with at least 2 components.
- 9, double division in speed: fixed.
- 10, GLM tolerance: stated.
- 11, conclusions left in round 1: noted in the record.

**Partly resolved:** 2, kernel width. The variants are run and a question is asked. encoding-bayes-beats-linear still flips to not reproduced under SD 20 or 17 ms, so that outcome depends on the reader's answer.

**Remaining issues that bear on a conclusion:**
1. beh-long-more-bias depends on the intercept reading. It should be marked assumed and asked of a reader (section 1).
2. pca-dimensionality, and the tolerances of the correlation claims, are compared against a 536-unit pooled population, while this session has 48 units. This is open as a question and cannot be tested.
3. Under the open kernel-width question, encoding-bayes-beats-linear moves from partially reproduced to not reproduced.
4. The README's statement that all three claims of absence cannot fail is wrong for alt-transient-parallel. The misapplied p ≥ 0.125 sentence in the record's deviations should be removed where the test is over 8 values.
