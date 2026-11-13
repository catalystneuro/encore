# Verifier report, round 3: steinmetz-2019-01

The claims file has 40 claims and the attempt record has 40 outcomes. Only one outcome has a `proposed` change: ed5h-choice-shuffle-fpr, at line 603 of `steinmetz-2019-01.yaml`. It is the only claim reviewed here.

| Claim | Proposed outcome | Agree | My outcome | Reason |
|---|---|---|---|---|
| ed5h-choice-shuffle-fpr | reproduced | No | not_reproduced (keep the verified outcome) | See below |

## ed5h-choice-shuffle-fpr

**The numbers come from the data.** The analysis is in cells 118 to 120 and 127 to 131.

- **First shuffle (seed 97, cell 119):**
  - Main fits: 4 of 2,871 neurons pass, 0.14%.
  - Code's reading of the fits (cell 128): 6 of 3,142 pass, 0.19%.
- **Four more shuffles (seeds 971 to 974, cell 130):**
  - Main fits: 1, 12, 3 and 11 pass, giving 0.035%, 0.423%, 0.105% and 0.386%.
  - Code's reading: 4, 15, 2 and 12 pass, giving 0.127%, 0.479%, 0.064% and 0.383%.
- **Means over five shuffles:** 0.218% under the main fits and 0.249% under the code's reading. I recomputed both from the table in cell 130 and they are correct.
- **No sign of cherry-picking:** the four extra seeds are a plain sequence, and every result is shown, failures included. The new shuffles use the same permutation scheme, rerun from the start, entry rule (full-model VE ≥ 2%) and pass rule (nested VE > 2%) as cell 119.

**Why I don't agree:**

1. **The criterion is written for one shuffle.** It says the labels are permuted and "the whole kernel test K for Choice is rerun from the start", which is one rerun, as in the paper (Methods, "Estimation of false positive rate"). It then says "Reproduced when the fraction is within tolerance." The ±0.17% tolerance is two Poisson s.d. of a count of 14, and the file says it chose this "since 10% (1.4 neurons) is below the spread of one shuffle". So the tolerance was already sized for the spread of a single shuffle. Using the mean of five shuffles changes the criterion rather than estimating the same thing better. The record itself calls it "an assumption".
2. **The change was made after seeing the result.** The averaging came only after the first shuffle had failed and after my round-2 caution. The fallback, the first shuffle under the code's reading (0.19%), uses a variant reading. The attempt's primary analysis is the main fits, and they give 0.14% (cell 119).
3. **The spread does not undermine the criterion.** At this attempt's lower rate (about 6 of 2,850 neurons per shuffle), the 1-to-12 range of single counts is about what Poisson noise predicts. Single shuffles often land below the 0.16% lower bound because the attempt's own rate is low, not because one shuffle can't decide the outcome.
4. **Even taking five shuffles, the result is not clearly a reproduction:**
   - Only 2 of 5 single shuffles fall within tolerance under the main fits (3 of 5 under the code's reading).
   - Under the main fits, the five shuffles pooled give 31 of 14,317 neurons, 0.217%. Its Poisson 95% interval is about 0.15% to 0.31%, which spans the 0.16% lower bound and does not include the paper's 0.33%.
   - The standard error of the five-shuffle mean is about 0.08%, from the cell 130 values. So 0.22% is about one standard error above the lower bound.

The fair summary is the one in the record's notes: the outcome turns on which shuffle is drawn. Under the criterion as written, the attempt's analysis gives 0.14%, which is not reproduced.

**Caution from round 2, still open:** only 2,886 neurons enter the nested tests under the main fits (3,199 under the code's reading), against about 4,240 in the claims file (cell 128). The attempt finds a lower false-positive rate (about 0.22%) than the paper. That may come from this attempt's model rather than from the paper.

**Claims file against the paper:** I found no misreading for this claim. It matches the Extended Data Fig. 5h legend ("14, 0.33%") and the Methods' single-shuffle procedure. A reader could revise the criterion to name more than one shuffle and set a tolerance for that estimate. That decision belongs to the claims file, not to this attempt.
