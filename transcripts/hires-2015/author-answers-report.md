I re-ran the claims each answer bears on, then updated the notebook, helper, README and attempt record. The entry passes `lock` and `all` (0 errors, the notebook runs in 8.7 min), and the handover is in `executed/000013-hires-2015/handover/`. Nothing is committed and nothing was verified.

Four outcomes changed. The record now has 22 reproduced, 5 partially reproduced, 4 not reproduced and 14 blocked, against 20, 5, 5 and 15 before.

**Q1: where the cutoff search starts.** The answer is the transition where the curve levels off; the literal search from 1 ms is now a variant only.

| Claim | Before | Now |
|---|---|---|
| table1-l4-c2 | blocked | reproduced: 15 of 18 values in all 64 reading combinations |
| table1-l5 | blocked | partially reproduced: 11 to 13 of 18 in every combination |
| table1-l4-outside | blocked | blocked: 7 to 9 of 17, which straddles its threshold of 9 |
| fig3c-touch-spikes-l4c2 | blocked | blocked, now only on the curve's range (Q2) |
| fig3c-touch-spikes-outside, fig3c-touch-spikes-l5, the four fig3d claims | blocked | blocked: they depend on a blocked claim, and their own readings disagree or fail |
| fig5c-modulation-index | reproduced | reproduced: means 0.677, 0.713, 0.672 (before 0.853, 0.857, 0.827, from the literal cutoff) |
| fig5-modulation-correlations | blocked | blocked: holds in 16 of 64 combinations |
| example-cell-touch-window | partially | partially: cell 23 gets the same window under either start |
| text-spikes-per-touch | reproduced | reproduced |
| l4-outside-weaker-touch | reproduced | reproduced |

For table1-l4-c2, the 15 rests on reading whisking periods as outside touch epochs. The Table 1 criterion doesn't name this reading. I took it from the claims file's own definitions, which the Q5 answer also quotes. With touch epochs counted in, the count is 14, which is partially reproduced. A verifier may question this choice.

**Q2: the range of the cutoff curve.** The paper doesn't give it, so 100 and 200 ms are both readings, as already run. For fig3c-touch-spikes-l4c2, all 4 readings with 100 ms pass but only 1 of 4 with 200 ms does. It stays blocked, now only on this detail.

**Q3: the pre-touch window for touch detection.** The answer adds a third reading, all pre-touch windows. fig4a-touch-detection-c2 stays blocked: the population sizes reaching 95% run from 1 to 30 neurons and none is within 15 ± 1.5. Adding the reading changed the random draws, so three earlier values moved by 1 to 3 neurons. fig4a-touch-detection-outside stays blocked, because the two performance measures still disagree.

**Q4: the time decoder's classes and smoothing.** Both class sets were already run; I added a smaller pseudocount (0.01) as a variant. fig4b-touch-time-precision stays not reproduced: the minimum RMS error is 1.09 to 1.40 ms, or 1.18 to 1.48 ms with the variant, against 0.55 ms.

**Q5: the phase decoder's cycles and empty bins.** The decoder now uses the phase-tuning cycles, and empty bins are filled by add-one smoothing or a floor rate. fig4c-phase-decoding goes from not reproduced to blocked:
- With held-out cycle counts and add-one smoothing, it never reaches 76% correct.
- With Poisson rates and add-one smoothing, C2 reaches it at 60 to 84 deg.
- With the floor rate, C2 reaches it at 12 to 15 deg.

So C2 falls on both sides of the paper's 24 deg, which is the criterion's fallback. The floor value is my own choice, as the paper gives none.

**Q6: the refractory model's rate.** The rate is now raised to make up for the refractory period (Berry and Meister's free rate), and the model's mean count matches the data's (ratio 1.00 to 1.03). fig6d-not-refractory stays blocked. Under one comparison the data FF is never below the model's by more than the error bars. Under the other it is below in only 4 of the 6 touch readings; without the compensation it was below in all 6.

**Q7: the L5 whisking increase.** The measure is now the median of the per-cell differences, which is +1.88 and +1.79 spikes/s, with p = 0.024 and 0.014. whisking-rate-l5-increase goes from partially reproduced to reproduced.

Each affected claim's notes in the attempt record say what the answer changed.
