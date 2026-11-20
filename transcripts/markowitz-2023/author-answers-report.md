I re-ran all four answered questions under the amended claims file. Two outcomes would change (ed3c and ed10i) and two stay the same. The record cannot change an outcome that verification round 2 agreed with (`tools/entry.py check` fails), so I kept the verified outcomes for ed3c and ed10i and wrote each change under `proposed`, with its reason. A third verification round has to settle them. Each claim's notes say what the answer changed.

| Claim | Before | Now |
|---|---|---|
| ed10i-no-place-preference | reproduced | not reproduced (proposed) |
| ed3c-keypoint-velocity | reproduced | partially reproduced (proposed) |
| fig2e-not-autocorrelation | partially reproduced (assumed) | partially reproduced, seed-sensitive |
| fig2k-dlight-predicts-sequence-variability | reproduced | reproduced |

1. **ed10i-no-place-preference.** The experiment-wide test is now one Jensen-Shannon divergence (JSD) per mouse over the centroids at all syllable onsets, with all frames as a variant. Both tests must give P ≥ 0.05.
   - The target-onset test still finds no difference (P = 0.174 by pair, 0.425 by mouse).
   - The experiment-wide test does find one: 20 Opto-DA against 12 control mice, U = 48, f = 0.20, P = 0.005. The variants agree: own bin edges P = 0.025, all frames P = 0.003, all frames with own edges P = 0.007.
   - The difference goes the opposite way from a place preference. The Opto-DA mice's positions on stimulation days are closer to their other days than the controls' are.
   - To run the all-frames variant I added each frame's centroid to the helper (`pos_all` in `markowitz.py`).

2. **fig2k-dlight-predicts-sequence-variability.** The null is now the Methods' one: 1,000 shuffles of the dLight peak values within mouse and segment, before binning. The code's null is now a variant.
   - Reading (a), the Methods' bins per mouse and syllable, is significantly positive at n = 5 and 10 (Pearson P = 0.003 and 0.001). It holds under all four other seeds (P 0.005 to 0.020).
   - Reading (b), the code's equal-count bins, is significantly negative under all five seeds. The criterion accepts either reading, so the claim is still reproduced, but now on reading (a) alone.
   - The raw correlations are negative under both readings. They come out "positive" only in being less negative than the shuffles.
   - To fit the time limit I compute the shuffles at mouse level with numpy binning. The notebook checks that this gives the same bins and correlations as the original code, and it does.

3. **ed3c-keypoint-velocity.** dLight is now processed with the Methods' fit with slope and bias; the fit without intercept is a variant.
   - 2D velocity r = -0.170, within -0.16 ± 0.016.
   - Forelimb r = -0.026 (per mouse -0.027). That is outside -0.02 ± 0.002 and rounds to -0.03, so one expected value of two misses.
   - With the fit without intercept the values were -0.167 and -0.019, both within tolerance, which is why it was reproduced before.

4. **fig2e-not-autocorrelation.** The test is now the legend's one-sided test, with an explicit "partially reproduced" case; the bins are unchanged.
   - The autocorrelation is significantly positive only at n = 10. The velocity curve is significantly positive at every n from 30 to 390, so at no n have both declined, and the partial case applies.
   - The result depends on the seed. The velocity P at n = 390 is 0.046 under the claim's seed and 0.049 and 0.038 under two other seeds. Under the remaining two seeds it is 0.079 and 0.054, which would make the claim reproduced. The record marks it `seed_sensitive: true`; it no longer rests on an assumption.

`python tools/entry.py lock` and `all` ran without errors. In the clean run the photometry notebook took 47 minutes and optoda 13. Every number in the new conclusions matches the executed output. The check passes with 0 errors, and `python tools/entry.py handover entries/markowitz-2023` built the package in `executed/markowitz-2023/handover/`. Nothing is committed or pushed.
