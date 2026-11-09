I checked the claims file, corrected eight claims, added one new claim, and recorded a `checks` entry marking it ready. Nothing was committed.

**Checker result:** `45 claims, 42 quotes, 16 statistical values, 2 problems`. Both problems are formatting, not errors. The paper prints the two p-values as "2.30e-5" (fig3c-touch-spikes-l5) and "1.0e-5" (fig5-modulation-correlations), with trailing zeros the checker doesn't match. Both values are correct and I left them as they are. Every quote matches the text word for word.

**Changes, by claim:**
- **fig3c-touch-spikes-l4c2:** exploration time was not limited to the sample epoch. The Results define it as "whisking or touch in the sample epoch", so I added that limit.
- **fig3c-touch-spikes-outside** (fig3c-touch-spikes-l5, the fig3d claims and the Table 1 rows inherit this): the rule "cells without a latency count as 0%" is made up, and Table 1 contradicts it. Six of the ten L4 cells outside C2 have no latency, yet the group median is 3.6%, so they cannot all be at 0%. I replaced the rule with two readings for where such a cell's window starts, and kept the 0% rule only as a variant.
- **latency-determinable:** one reading searched for the latency up to the touch response cutoff. That is circular, because the cutoff is computed after the latency, so I removed it.
- **fig4a-touch-detection-c2:** the "equal error" threshold is not in the paper. The Methods use an "optimal threshold" found on half the data, which I read as the one maximizing percent correct.
- **fig5c-modulation-index:** the velocity reading "mean over 1 to 5 ms before onset" was invented. I replaced it with the frame before onset, from "just before touch" and "pretouch velocity".
- **example-cell-ff-around-touch:** Figure 6 calls its neuron "an example neuron" and never says it is the Figure 1 cell. I named this as open, with two readings: the Figure 1 cell, or any L4 C2 cell.
- **example-cell-sample-ff:** the paper does not say whose FF = 7.51 is. The statement no longer says it is the example cell's. Three readings are named: the example cell, the mean over the 41 L4 cells, and the mean over all 52 cells.
- **l5-higher-rates:** the paper compares L5 with L4 cells both inside and outside C2, but the criterion only compared with L4 C2. I added L4 outside C2.
- **example-cell-phase-modulation (new):** the example neuron's phase modulation depth "close to 1" (Results, paragraph 5; Figure 1G-H) had no claim. It now has one, with the protocol's default tolerance of 10%.

**Still open** (recorded in the file, not changed):
- **table1-l4-c2, table1-l4-outside, table1-l5:** the pass rules (at least 15 of 18, or 13 of 17, values within tolerance) are the claim writer's, not the paper's.
- **fig6s1b-clusters-less-variable:** the paper shows this test for one example neuron only. Requiring it in more than half the cells, and for the first group, is the claim writer's choice.
- **fig6d-not-refractory:** the paper compares data and model only in a figure. Both comparison rules in the criterion are invented.
- **fig4a-touch-detection-outside:** the rule used to judge detection as "poor" (a 95% bound) is not from the paper.
- **whisking-rate-l4-no-change:** the paper names the Wilcoxon signed-rank test only for L5. The claim assumes the same test for L4.

**Ready:** yes, `ready: true`. The remaining problems are judgement rules on a few secondary claims, and none affects the main findings, which all have claims.
