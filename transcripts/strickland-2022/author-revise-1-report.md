The verifier's round-1 points are all answered and the entry re-runs cleanly: `python tools/entry.py all entries/strickland-2022` gives 0 errors and the notebook passes in 5.9 min. Nothing is committed.

**Outcome changes**

| Claim | Before | Now | Why |
|---|---|---|---|
| fig4b-phasic-network | reproduced (assumption) | partially_reproduced | The criterion names Pearson r, and with r the network part fails (−0.329 within against 0.008 outside). The r² assumption is removed and r² is shown as a variant. A reader is asked whether the criterion should allow r², as the fig2e criterion does. |
| fig4b-tonic-network | reproduced (assumption) | partially_reproduced | Same reason (−0.250 against 0.000) and same question. |

Count is now 23 reproduced, 6 partially_reproduced, 1 not_reproduced, 0 blocked.

**Disagreements I kept, with the reason recorded**
- **fig2c-pc1-contribution stays reproduced.** The verifier gave partial because the L2 check rested on one k-means solution. I re-ran it on all 20 solutions: the nine largest clusters hold a median of 481 units, inside 505 ± 50.5 (single seeds range 360 to 590). The single solution used before gave 411.
- **fig5e-no-anatomical-bias stays reproduced, now marked as resting on an assumption.** It is judged on the k1–k5 reading (p-b), the computation behind the paper's figure, because a claim of absence is judged on the paper's own test. The notes now say p-b passes by construction. I added a permutation reference: under the k1–k3 reading the 9.82 gap is beyond chance (p = 0.001), and under p-b 4.48 gives p = 0.058. A reader is asked about the threshold and which clusters count as phasic.

**Added or corrected**
- **fig2d latency:** the false sentence that the Source Data latencies "follow" the 12-s variant is corrected in the notebook, the notes and the finding. No reading I tried reproduces them, and no script in the dataset computes a latency.
- **fig3c/3d lesions:** v-b now also runs on the script's lesion (s-c). Ten further s-c runs show the 0.264 against 0.268 result is stable (SD 0.0001). Weights scaled by each PC's variance are added as a variant: with them fig3c would fully hold, so a reader is asked about it.
- **cue-outcome-membership-independent:** the L2 tests now run on each of the 20 seeds. Under L2, independence holds in only 4 of 20 (median p 0.048 and 0.011). The outcome stays reproduced, judged on the paper's own clusters.
- **fig4f label swap:** the Source Data rows labelled k7 hold the 111 k7 values plus 60 k8 values, matching the script's hard-coded labels. Only the labels are swapped; the tests use the units' real clusters.
- **Data check:** the cube's 500-ms firing is now recomputed from the spike times (largest difference 9.5e-13). A new cell prints the cited passages of the paper's MATLAB scripts from the dataset.
- **Record and files:** `questions/strickland-2022.yaml` is new, with three questions (fig4b networks, fig5e, fig3c). The round-1 `verifications` block covers all 30 claims. README, summary and `runtime_minutes` (now 6) are updated.

**Not done**
- The `Shuffle` dimensions the verifier listed can't be settled from the scripts, because the `Shuffle` function isn't in the dataset. They are supported only by the exact match with Source Data.
- Other L2 variants (fig3b, fig3e, fig5b) still use the best of the 20 solutions. No outcome depends on them.
- Untracked dotfiles and a root `scripts/` directory appear in `git status`. They were already there and I left them alone.
