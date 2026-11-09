**Checker result:** `claims/000115/10.1016-j.neuron.2021.07.029.yaml: 33 claims, 33 quotes, 27 statistical values, 0 problems`. That was the result before my changes and is still the result after them.

I read every claim against the paper text, the legends and the supplement. I also checked the code each criterion cites against LorenFrankLab/Gillespie_Neuron_2021 at commit 1be6a6a, which is public. The criteria match the code except for the points below.

**Changes, by claim**
- **fig1d-sessions-blocks:** the criterion said a block counts when it has a trial of task phase 4. The code keeps any block with a task phase of 4 or more (`any(ctphase>=4)`), so I corrected it to match.
- **fig3b-search-prevgoal-enriched:** the paper says "roughly 20%" without saying whether that is a median or a mean. The criterion now reads both the session median and the session mean, and either one within tolerance passes.
- **fig4ab-current-goal-late:** the criterion said the Figure 4A counts equal the early correct plus early error counts of Supplementary Figure 7. That holds for subjects 1 to 3 only; subject 4 is off by one (793 against 515 + 277 = 792). I corrected the wording.
- **fig5b-future-correct-error:** I added which trials are used as an open detail.
  - The Methods and part 6 of the code exclude the first block, so that stays the main reading.
  - The legend's correct plus error counts equal the Figure 3E counts (923 + 424 = 1347, and likewise for the other subjects). Part 5 of the code builds those with the first block included, so that set is now run as a variant.
  - fig5c-current-goal-correct-error and figs7-early-late-correct-error inherit this. fig4c-current-goal-reward-correlation (whose n = 923 is the same correct count) and fig5d-glm-predict-chance now refer to it too.
- I added a `checks` entry at the end of the file.

**Still open** (listed in the checks entry)
- **fig4ab:** the paper gives no test for "did not differ substantially". The criterion's rule that the 99% intervals overlap in at least three of four subjects is the claims writer's own reading.
- **fig6a and fig6b:** "elevated replay before the transition" and "within a few trials" have no number in the paper. The criteria use readings: the figure's corrected tests, and bounds of +3 and +5 trials.
- **fig5a:** the Results say "for all subjects", but the legend says three of four. The claim follows the legend, which gives the test.
- **Figure 5A counts:** the repeat-trial counts in the Figure 5A legend (924, 1019, 894 and 1302) do not match the Figure 5B counts. Parts 6 and 7 of the code apply the same filter, and the code does not explain the gap.

Every main finding has a claim, and every claim comes from this paper.

**Ready:** yes, recorded as `ready: true`. Nothing was committed.
