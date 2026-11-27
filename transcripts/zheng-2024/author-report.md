I've finished steps 1 to 5 and the handover. Of the 32 claims, 14 reproduced, 7 partially reproduced, 8 did not reproduce and 3 are blocked. The entry passes `check` and a clean `run` in 31 minutes, and the handover is in `executed/zheng-2024/handover/`. I did not verify my own work and did not commit.

One decision you should know about first: I pinned version 0.261113.1035, not the 0.230630.2304 the paper cites. The cited version has no cell-type labels (needed to pick out pyramidal cells for every claim) and no light-responsive label (needed for the ChR2 claim). I checked one session in both versions: the spike times are identical. The notebook header says why.

**(1) Outcomes**

| Claim | Outcome |
|---|---|
| fig1d-pv-decorrelation | reproduced |
| fig1e-novel-drift-faster | reproduced (Cohen's d 0.51 against 0.58 ± 0.058) |
| fig1e-later-lags-no-difference | reproduced |
| fig1h-rate-decorrelates-location-stable | reproduced |
| fig1i-location-mse-increases | reproduced |
| switch-step-size-filter | not reproduced (2770 putative switching fields against 3184 ± 318; 191 removed is within tolerance) |
| fig2d-switch-fractions | not reproduced (familiar switching 1889 and the familiar and novel OFF fractions are low; the other 5 of 8 values are within tolerance) |
| fig2e-switch-fraction-by-experience | reproduced |
| fig3df-step-beats-polynomial-fields | partially reproduced (0.966, 0.951, 0.908 for K = 1, 2, 3) |
| fig3df-polynomial-beats-step-population | reproduced |
| figs4g-population-vectors-gradual | not reproduced (no bias toward the gradual model) |
| fig3k-switch-abrupt | reproduced under reading (a), passage times 0.808 and 0.813 |
| figs5-switchers-drive-drift | reproduced |
| fig4-glm-deviance | partially reproduced (deviance values hold; for OFF the top predictor is trial, not position) |
| fig4-delay-zone-more-switching | not reproduced (the delay zone has the least switching) |
| fig4-behavior-not-predictive | not reproduced (previous-trial choice predicts switching ON, p = 0.021) |
| fig4di-switching-decreases-with-trial | partially reproduced, resting on an assumption |
| figs8-speed-no-trend | not reproduced (speed against trial r = 0.154 and -0.148) |
| fig4no-head-scans-not-related | not reproduced |
| figs9-splitter-switching | reproduced |
| figs13-btsp-signatures | partially reproduced (3 of 5 parts hold) |
| fig5c-switchiness-not-intrinsic | reproduced (1006 neurons) |
| fig5d-nrem-rate-relations | reproduced |
| multifield-independent-switching | not reproduced (271 pairs against 781) |
| figs12-stability-after-switch-on | partially reproduced (all tests in the stated direction; only 3 of 12 medians within tolerance) |
| fig6-co-switching | not reproduced (familiar 0.36 and 0.31 against 0.17 and 0.20) |
| fig6f-switching-asynchronous | reproduced |
| figs14-preexisting-fields-ephys | partially reproduced (the OFF fraction is 0.43, expected 0.2) |
| figs2-chr2-no-effect | reproduced |
| fig7-preexisting-across-days, figs15-imaging-not-artifact | blocked, `data_missing` (imaging only available on request) |
| figs1-not-electrode-drift | blocked, `too_large` (about 77 GB of raw wide-band data to stream) |

**(2) The dataset, assumptions and questions**
- **Session missing:** e13_26m1_210913, one of the paper's 46 familiar sessions, is not in the dandiset, so 45 familiar and all 8 novel sessions were used.
- **Cited version:** besides the missing labels, it marks 28 of 30 familiar trials of e16_3m1_210201 as not familiar.
- **Linear-maze direction:** on the linear mazes, `visited_arm` holds the running direction without saying so.
- **Pyramidal counts:** six of the paper's familiar sessions have fewer than its required 50 pyramidal cells under the files' labels.
- **Clocks:** spikes and position share a clock in all 53 analysed tasks (one linear-maze task only to about a second).
- **Assumption:** for fig4di I took trials from the fourth on. The legend's counts (1,029 familiar and 281 novel trials) match this reading (1031 and 288 here); over all trials the claim would not reproduce.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings):
  - Which trials enter Figure 4D and 4I?
  - Which within-field quantity, and which single threshold value, select the fields of Figure S14?
  - Are the 781 same-neuron field pairs formed within a turn or across the whole maze?
- **Questions to a reader:** none.

**(3) Where the protocol was unclear or did not fit**
1. "Pin the cited version" has no rule for a cited version that lacks the variables the claims need. I pinned the later version, showed the difference and recorded it as a deviation.
2. Seeds: one random pipeline (field shuffles and switch permutations) underlies most claims. I used fig2d's seed for all of them, and the five-seed rule then meant re-running the whole pipeline. That takes 25 of the notebook's 31 minutes, well over the ten-minute target.
3. `measured` for a single expected value that applies across several model orders (fig3df, figs4g): I gave the smallest value and the order-1 value, and said so in the notes.
4. Some criteria cover neither the full nor the partial case (fig2d, fig4-glm-deviance). I chose not reproduced for fig2d and partially reproduced for fig4-glm-deviance, and explained each.
5. Several criteria judge on significance while the claim also lists expected effect sizes that miss (fig1e d, fig5c t values, figs5 medians). I followed the criterion and noted the misses.
6. The suggested clock checks (decoding a task variable) do not fit continuous maze running. I used spatial information with the spikes shifted against position instead.
7. Head-scan detection needed a track per turn, a detail the claims file lacks. I took it from the code (`find_tmaze_turns`) and cited it.

**(4) Runtime and failures**
- The run took from 07:55 to about 10:02 UTC. The notebook takes 31 minutes and peaks at 2.2 GB of memory.
- Nothing failed in the final run. During development I fixed bugs in reading spike times and in the NREM sleep label, and a head-scan track that averaged the two turns together.
