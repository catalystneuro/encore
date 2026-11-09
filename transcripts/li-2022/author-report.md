I finished steps 1 to 6. Of the 39 claims, 4 were tested and none reproduced, and 35 are blocked. The entry passes `check`, and `all` ran it from a clean environment in 9.5 min. The handover package is in `executed/000689-li-2022/handover/`. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig3k-nt-sensor-sucrose-increase | not_reproduced, assumed. Right direction (area +3.0, paper +4.1), but p = 0.081 at best with 5 mice |
| fig3l-nt-sensor-airpuff-decrease | not_reproduced, assumed. Right direction (area -5.5, paper -3.5), but p = 0.074 at best |
| fig3-nt-sensor-early-dip | not_reproduced, assumed. Sucrose mean is below zero but airpuff is above it, under every reading |
| fig4-recording-count | not_reproduced. 1902 units (1739 after the 0.3 Hz cut) against 685; 31 mice against 30 is within tolerance |
| fig4d-seven-clusters | blocked, methods_underspecified. 8 to 14 clusters; 7 only with an 820 ms smoothing window under one reading |
| fig5dh-behavior-clusters | blocked, metadata_insufficient. The pose cannot be aligned with the trials |
| fig2c plus 12 group or projection claims (fig4c, ed8d, ed8fg, fig4e, ed8i, both fig4fg, fig5a, fig5b, fig5c, ed8e, fig5fi, ed8os) | blocked, metadata_insufficient |
| 20 claims whose experiments are not in the dataset (anatomy, slice physiology, behavior cohorts, terminal and somatic photometry, sensor validation) | blocked, data_missing |

## 2. What I found about the dataset
- **Version:** I pinned 0.240530.1923, the latest. The paper cites none, and the other published version lists the same 85 assets with the same IDs.
- **No group labels:** no file says which mice are CRISPR and which are controls, or which projection (NAc or CeA) was tagged. Every genotype reads "Wild type". This alone blocks 13 claims.
- **Units are not sorted single neurons:**
  - 21 of 31 sessions have exactly 64 units on 32 channels.
  - 1061 of 1902 units have more than 5% of spike intervals under 1 ms.
  - In each session 6 to 65% of spike times are shared with another unit.
  - The paper's light-tagging rule, run without the "fake" session, passes 1355 units against the paper's 71.
- **H17 spike times end at 249 s** of a 12118 s recording, so its spikes can't be lined up with its trials.
- **Pose has no timestamps** and drifts against the trial clock: the best match is off by a median of 80 s and changes within 28 of 29 sessions.
- **Light pulses:** each session has two blocks of about 427 pulses, fitting the paper's fake and real tagging sessions, but nothing says which is which. In H31 to H42 one block comes before the task.
- **Missing neutral cue:** H09 to H14 have 75 sucrose and 45 shock cues and no neutral cue, though the description says 2:1:1.
- **Mouse count:** there are 31 mice against the paper's 30. For H28 and H32 the recorded session may not be the last day, which is the only day the paper analyses.
- **Photometry format:** one 60 Hz series interleaves three frame types, and the third is undescribed. The cue events last 2 s against the paper's 4 s. Nothing marks the reward or airpuff, or whether a cue was paired.

**Assumption:** all photometry cues are treated as paired trials, with the outcome 2 s after cue onset (Methods). In late sucrose sessions 49 to 58 of about 60 cues are followed by licking, which supports this.

**Question for the paper's authors** (recorded as a finding): what smoothing window did MATLAB's "smoothing factor 0.85" produce, and was it applied to each cue trace or to the joined trace?

**Questions to a reader:** none.

## 3. Where the protocol was unclear
1. **A file defect that breaks an alignment.** The protocol says what to do when a clock can't be established, but not how to classify a claim blocked by the archive's own timing (pose without timestamps). I used metadata_insufficient.
2. **A method choice that isn't one of the criterion's readings** (the smoothing window). Step 1.6 covers it, but the claim's criterion said "reproduced when one reading gives seven". I counted only the criterion's readings for that rule and blocked the claim as methods_underspecified, since the 7 comes from one window choice.
3. **Claims with two missing pieces** (fig2c has both missing data and missing labels) need a choice of `blocked_by`. I picked the reason that blocks every reading.
4. **No test for a paper-specific light artifact or fake session.** The protocol's clock checks don't cover this, so I reported the rule's outcome without the fake-session test.

## 4. Runtime and failures
The run took about 1 h 40 min (12:52 to 14:32 UTC) and the notebook runs in 9.5 min.
- I first assigned photometry channels by frame order. That broke where one session shifted phase, so I switched to the LED event labels. The results were unchanged.
- I planned a behavior notebook using tsfresh, timed at about 15 min for all trials, and dropped it once the pose turned out not to align with the trials.
- Nothing else failed.
