Round 3 is recorded. One outcome changed and no proposals remain open.

**Outcome changed**
- `ed4l-disappearing-decrease` went from partially reproduced to not reproduced. The verifier agreed with the proposal, and the `proposed` block is removed. The criterion has no partial clause: it requires the disappearing fraction to fall significantly both near and far from reward. Near reward it does (p = 0.020); far from reward it does not (p = 0.069). The OLS fit with errors clustered by mouse fails the same test the other way round (far p = 0.030, near p = 0.083).

**Proposals still standing:** none. This was the only one, and the verifier agreed.

**Other changes**
- I updated the attempt notes for ed4l, the notebook's result cell, header and summary table, and the README. The count is now 35 reproduced, 8 not reproduced and 7 blocked.
- Round 3 is recorded under `verifications` with the verifier's reason, including its caveat that only the raw fraction was fitted, not the logit fraction.
- I did not add a logit fit, because the protocol says a change that needs an analysis not yet run waits for a new attempt. I added the open question of whether the fig4m logit reading also applies to ed4l to `questions/001361.yaml`.
- The re-run reported 48.1 minutes, while the text said about 41, so the README, the notebook header and the notes on two blocked claims now say 41 to 48 minutes. I re-ran after that edit so the executed copy matches.

`python tools/entry.py all entries/001361-sosa-2025` passed both times with 0 errors, and the ed4l numbers did not change. Nothing is committed.
