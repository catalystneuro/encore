I've finished the round-2 revision. No verified outcome changed; three changes of outcome are proposed for a third round. `python tools/entry.py all` reported 0 errors and the notebook passed (2448 s). A second full run after the last code change gave the same outputs as the first, and `entry.py check` still reports 0 errors after the final text edits.

**Proposed changes (verified outcomes kept, as round 2 requires)**

| Claim | Current outcome | Proposed |
|---|---|---|
| fig4c-alpha-beta-shift | partially reproduced | not reproduced |
| fig5a-spatiotemporal-bidirectional | not reproduced | reproduced |
| fig5b-alpha-beta-no-sustained | reproduced | partially reproduced |

All three rested on PSI reading (b), which the verifier called weak. The new outputs confirm it is miscalibrated:
- **Offset on shuffled data.** When each PFC trial is paired with another trial's parietal data, reading (b)'s per-subject means (-1.25 to 0.52) nearly equal the observed fig4c means. Observed minus shuffled is -0.08 ± 0.09 (p = 0.061), so the "6 of 7 subjects below zero" is the null's offset, not an effect.
- **Offset on synthetic noise.** On independent synthetic signals, reading (b)'s mean z is -0.21 to -0.37.
- **Likely cause.** Moving the FFT's time origin to the segment's centre removes the offset. That points to the phase slope each trial's spectrum carries from where the segment sits in the padded window.
- **Per-trial permutation doesn't help.** Shuffling with one permutation per trial (the claims file's other null reading) leaves (b) miscalibrated (mean -0.51 in delta-theta).

Reading (a) is calibrated: on the shuffled data its mean z is -0.05 and 0.02, its SD is about 1, and 6.0% and 6.9% of pairs pass |z| > 1.96. It is also the first reading the claims file lists, so I adopted it. Under (a):
- **fig4c:** 5 of 7 subjects are below zero, under the 6 the partial match needs.
- **fig5b:** no time point is significant after FDR, which the criterion calls partial.
- **fig5a-spatiotemporal:** the grand means stay at or below 1.01, so it meets the criterion. The notes say this shows little, since the identity trials show no direction under this reading either.

**Added outputs**
- The shuffled-data check now prints the mean z, overall and per subject, under every reading.
- Both readings are also run with one permutation per trial, and the synthetic calibration test is in the notebook.
- **Random-trial control for the 900-ms analysis.** Power is re-run on a random draw of trials from both delays, with as many per condition as the 900-ms-only analysis. It loses about as many effects, so that loss comes from having fewer trials. These tests can't tell whether the 1150-ms timing matters.
- Plots of 70-150 Hz amplitude around the stimuli and test cue, per delay group.
- Task-induced PSI on the 900-ms trials alone.
- Subject-level tests for the time-resolved PSI. Under reading (b) they find no significant point either.

**Corrected text**
- The ERP note now says only the adopted reading's p (0.041) is near the threshold.
- The run time is now stated as 41 to 43 minutes, about 40 to 42 of them in the loading cell. It was 35, with "about 20" streaming.
- The README sentence on the deposited code now separates the code as deposited (99.5 to 100% of pairs on the real data) from its null with the conjugate added (about 90% on shuffled trials).
- The data-check cell now says 187 channels where it said 192.
- The fig2 notes now limit "every reading" to the main analysis.
- Recorded values for the PSI claims whose outcome doesn't depend on the reading now come from reading (a).
- A few counts against the deposited code's null moved slightly because of the new random draws (1042 to 1041, F 59.5 to 58.5), and the text matches the new numbers.

Round 2 is recorded under `verifications`: 16 claims agreed and fig4c disagreed. For fig4c I gave no verifier outcome, because the report doesn't state one.

**Not done**
- PSI with one permutation per trial is run only for the task-induced PSI, not the time-resolved PSI.
- No question was added to `questions/crcns-fcx-3.yaml`, since this report found no place where the claims file misreads the paper.
- Untracked dotfiles (`.bashrc`, `.idea`, `scripts` and others) appeared in the working tree during the session. I didn't create them on purpose and left them alone.

Nothing is committed.
