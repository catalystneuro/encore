Both answered questions changed their claims. After the re-run, fig4b-single-field-proportion goes from not reproduced to reproduced. fig4c-active-subsets stays not reproduced, but the outcome now rests on an assumption I made about how the simulated environment sizes were spaced. With the other spacing it would be reproduced.

The entry is locked, `entry.py all` passes (notebook runs in 210 s, 0 errors), `check` reports 0 errors, and the handover is in `executed/rich-2014/handover/`. I did not verify my own work, and nothing is committed or pushed.

| Claim | Earlier outcome | Outcome now |
|---|---|---|
| fig4b-single-field-proportion | not reproduced | reproduced |
| fig4c-active-subsets | not reproduced | not reproduced, `assumed: true` (logarithmic spacing) |

**Question 1, fig4b-single-field-proportion.** The criterion required the 5 to 10% band (widened to 4.5 to 11%) to hold over sizes spanning a factor of 10, which is not in the paper.
- **What the answer changed:** the reader agreed and amended the criterion. The required width is now what the paper's printed parameters give, less 10%: a factor of 5.0 when the proportion is of all cells (X-a), 3.9 when it is of place cells only (X-b).
- **Result:** the analysis is unchanged. With the main fit, the proportion stays in the band from 133 to 750 m under X-a, a factor of 5.66, and from 195 to 866 m under X-b, a factor of 4.44. Both pass.
- **Other readings:** the other definition of a "pass" through a field gives 5.75 and 4.49. The dataset's own fields give 5.59 and 4.39, and the printed parameters 5.53 and 4.34.
- **Caveat:** at the 48 m track itself the proportion is 16.5%, so the band holds for environments of roughly 130 to 750 m, not for the track.

**Question 2, fig4c-active-subsets.** The criterion compared the mean share of cells that tell two environments apart, over pairs both larger than 10 m, against the fitted equal-rate model.
- **What the answer changed:** the fitted equal-rate comparison stays. The measure is now the share of all pairs of environments in which more than a given fraction of cells tell them apart, at 0.1 (K-a) and 0.2 (K-b), under both log and linear spacing of the 300 sizes. The old mean is reported but not judged.
- **Result:** the spacings disagree, consistently across both fits, the dataset's fields, and 10 further seeds.

  | Spacing | Threshold | Gamma-Poisson | Equal rate |
  |---|---|---|---|
  | Log | 0.1 | 0.825 | 0.834 |
  | Log | 0.2 | 0.662 | 0.701 |
  | Linear | 0.1 | 0.999 | 0.980 |
  | Linear | 0.2 | 0.948 | 0.830 |

  The gamma-Poisson model is lower under log spacing and higher under linear.
- **Why log spacing:** following Author step 1.6, I assumed log spacing. The sizes run from 0.1 to 50 m, nearly three orders of magnitude. The paper describes recruitment "over spatial scales spanning several orders of magnitude", and the Fig. S18 legend discusses "small environments". A linear grid has only 6 of 300 sizes below 1 m, against 111 for log.
- **Recorded:** the assumption is a deviation in the record, and a new `methods_unavailable` finding asks the paper's authors how the sizes were spaced and what threshold they used.
- **Reported, not judged:** at 50 m the gamma-Poisson model has recruited 0.669 of cells and the equal-rate model 0.961. At twice the fitted rate, the share of cells telling apart environments over 20 m is 0.043, close to zero as the Fig. S18 legend says.

Each claim's notes in `attempts/rich-2014-01.yaml` say what the answer changed. I also updated the notebook's code, conclusions and summary for both claims, and the README rows. The `tools/` files were already modified before this run, and I left them alone.
