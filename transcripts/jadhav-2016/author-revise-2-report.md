No outcome changed and none is proposed. All 39 outcomes stay as the verifier agreed in round 2: 9 reproduced, 7 partially reproduced, 21 not reproduced and 2 blocked. The full entry ran twice with `python tools/entry.py all` (31 and 33 minutes) and passes, and the numbers were the same both times. `tools/entry.py check` reports 0 errors. Nothing is committed.

**Main fix: the "no variant rescues a failing claim" sentence.** The verifier found that the earlier set of variant tests left out several claims. I added a second set that runs each of them under the main reading, the mean-envelope reading and the reading without the `wtr2` runs. It covers fig3-transient-responses, the fig7c test of whether the inhibited relation is stronger, figs5, fig8bc, fig6e-theta-trained-glm, figs4c, fig8d, and figs6 (by regrouping the cells only). The sentence now holds for every downstream claim:
- **fig7c:** the difference test fails under both variants (p = 0.590 and 0.083).
- **figs4c, fig8d, figs6, fig6e-theta-trained-glm and fig3-transient-responses:** each fails under every reading.
- **fig8bc:** still holds under both variants.

**One new finding cuts the other way.** figs5-matched-selectivity, which is reproduced under the main reading, fails under both variants:
- Mean envelope: the inhibited relation is r = −0.40 (p = 0.29) and the shuffle finds a difference (p = 0.016).
- Without `wtr2`: the inhibited relation is r = 0.26 (p = 0.47).

I kept the verified outcome and did not propose a change, because the main reading is the one the record argues for and that the verifier accepted. The notes, the variant section, the Summary and the README now say figs5 holds only under the main reading. A third-round verifier could reasonably disagree with that call.

**Text the verifier quoted, now corrected:**
- fig3de notes: CA1 peak is 48 ms, not 46.
- fig4a (notebook and notes): now states the tied bins; none contains 180°.
- fig5c (notebook and notes): now gives the no-speed-filter values as printed.
- fig8a: the cell prints all 24 animal-days, and the notes give the range of 375 to 1297 pre-rest SWRs per day.
- The run time now reads about 32 minutes in the notebook header and README, and 33 in `entry.yaml`. The `",,"` typo is fixed.

**Round-1 reasons:** I added problem 5 (position units) to the wtrack-learning and figs2 reasons, and problem 2 (rate-map bins) to the fig8bc reason, in the verifier's round-1 words.

**Round 2 is recorded** under `verifications` in the attempt record: agreement and outcome for each of the 39 claims, the verifier's reasons, and my responses.

**Not done:**
- No question was added to `questions/crcns-hc-28.yaml`, because the verifier found no misreading of the paper.
- The 12 excited and 7 inhibited PFC cells behind the group comparisons, and the edge-of-rule results (fig4-theta-locked-fraction, theta-lag-past, fig6e-glm-swr-prediction), cannot be fixed by this attempt. Their notes already state them.

Untracked dotfiles and folders (`.bashrc`, `.idea`, `scripts` and others) are in the repository root. I did not create them and left them alone; the workflow should not commit them.
