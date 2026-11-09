No outcome changed in this round. I proposed three changes for a third verification round, re-ran the entry, and the notebook passed in 43 minutes. `python tools/entry.py check` reports 0 errors, and nothing is committed.

**Proposed changes** (each keeps its recorded outcome and adds a `proposed` block with the reason):
- **fig1e-reward-outcome-not-pre:** reproduced, proposed not reproduced. The criterion names both W1 and W2, and under W2 7 of 14 DA mice differ before side entry, which is not fewer than half. The verifier is also right that the Fig. 1 scripts' own window includes the side-entry sample, so they don't support choosing W1.
- **ed8g-vls-telc-ach-suppressed:** reproduced, proposed not reproduced. The criterion requires Ach to be lower "under each reading", and the z-scored reading fails (S952 is significantly higher).
- **ed11-cko-glm-r2:** partially reproduced, proposed not reproduced. No part of the criterion holds under every reading: R2 matches only with one model per genotype, the Ach kernels are larger only when averaged over shifts, and "comparable" DA kernels fail everywhere.

**Disagreement kept:**
- **fig2a-rdah-smaller-than-dlight:** stays partially reproduced. The rewarded-trial amplitude part holds in all 3 mice under every reading, and 5 of 6 trace correlations are above 0.8 (the sixth is 0.788). The verifier's view that it is not reproduced is recorded.

**Assumption flags:**
- **fig1f-cue-omission:** now marked `assumed`. It relies on the paper's script to say which sessions had the cues off, and the files can't confirm this.
- **ed11j-cko-switching-impaired:** the assumption is removed. The outcome follows from the criterion, so no resampling unit needs to be chosen.

**Added outputs:**
- A count of channels with no raw trace: 193 channel-sessions in 30 mice. The finding said 23 mice and is corrected.
- The channel metadata and the export table's virus codes for the cortical and thalamic input groups. The thalamic controls carry virus 349 ("retro mCherry") at the striatal fibres, the same virus as the cortical controls. No file records an injection into the thalamus, where the Fig. 5f legend describes one. This is recorded as a deviation on both fig5ef claims and ed13, and in the finding.
- Results from 3 GLM runs (instead of 10) for ed5f, fig2h and ed11. None changes a conclusion. ed5f's criterion fixes 10 runs, so its 3-run results are shown as a variant only.

**Text corrected:**
- ed4bc now counts DA mice out of the 12 that can be tested, not 14. The result is more than half under both windows; the outcome doesn't change.
- ed5f said "all 12 readings" where 6 per signal is right.
- ed7e now says the data don't explain the dip in the left-hemisphere DA trace during the laser.
- The Summary's sentence about readings is rewritten.
- The README and the notebook summary table show the proposed changes.

**Questions and record:**
- I added a fig2h question for a reader to `questions/001767.yaml`. The criterion's lag direction conflicts with the paper's finding that DA leads Ach. The claim is unchanged, and the outcome doesn't depend on it, because the R2 part fails anyway.
- Round 2 is recorded under `verifications`, with the verifier's reasons and my responses.

**Not done:**
- The fig4g delta-Ach versus mean-Ach question and the ed8f sensor question were already with a reader and are still unanswered.
- The extra DA mouse in fig1e can't be identified from the data.
- `tools/build_site.py` and `tools/site_assets/app.css` were already modified before this run; I left them alone.
