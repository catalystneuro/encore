I've finished steps 1 to 5 of the Author protocol and run the handover. The entry is `entries/000011-li-2016/` and the record is `attempts/000011-li-2016-01.yaml`. I also wrote `questions/000011.yaml`. The final `tools/entry.py all` passed with 0 check errors, and its outputs match the earlier full run line for line. I have not verified my own work.

### 1. Outcomes per claim

| claim | outcome |
|---|---|
| unit-classification | partially reproduced (979 units, 890 putative pyramidal as in the paper; 15 intermediate units against 50) |
| selective-fraction | partially reproduced (the sample-epoch count is never inside its band) |
| fig1d-late-delay-ipsilateral-bias, fig1d-earlier-photoinhibition-minimal, ed3-behaviour-recovery-interval, fig2b-unilateral-performance, fig2b-bilateral-performance | blocked, data_missing |
| ed4-return-to-trajectory | not reproduced |
| fig1f-spike-rate-recovery | reproduced (0.101) |
| fig1g-selectivity-recovery | blocked, methods_underspecified (my readings of the open details disagree) |
| ed5-photoactivation-recovery, ed5-photoactivation-rate-changes, ed2d-spatial-extent | blocked, data_missing |
| ed2b-silencing-strength | partially reproduced (one-spot silencing in VGAT mice leaves 18 to 25% of the control rate) |
| ed2e-no-rebound | not reproduced |
| ed6a-bilateral-inconsistent-bias | reproduced |
| fig2-recordings-recovery | partially reproduced |
| fig2e-selectivity-recovery-times | not reproduced |
| ed7-larger-photoinhibition | blocked, methods_underspecified |
| ed7e-roc-larger-photoinhibition, ed8-roc-during-photoinhibition | partially reproduced |
| cd-stable-over-epochs, fig3c-cd-predicts-movement, fig4-bilateral-cd-predicts-movement, ed9c-cd-window-robust | reproduced |
| fig3c-cd-recovery-roc, cd-captures-selectivity, fig3d-persistent-mode, fig3e-ramping-mode, ed6b-session-bias-predicted | not reproduced |
| ed9f-reaction-time | blocked, methods_underspecified |
| fig5b-callosotomy-control-performance | blocked, data_missing |
| fig5b-callosotomy-unilateral-sensitivity, ed10-callosotomy-preparatory-activity, fig5-callosotomy-no-recovery, fig5f-callosotomy-cd-reduced | blocked, metadata_insufficient |
| ed1-monolithic-models-fail | reproduced (simulation) |
| fig6-modular-models-recover | partially reproduced (simulation) |

Totals: 7 reproduced, 7 partially, 8 not reproduced, 16 blocked.

### 2. What was found about the dataset, and questions asked
- **Pinned version:** 0.220126.1907. The paper cites no DANDI version and this is the only published one.
- **Contents:** 58 sessions of the 12 control mice, which split into experiment 1 (20 sessions, 4 mice where the paper says 6), experiment 2 (26 sessions, 7 mice) and experiment 3 (12 sessions, 3 mice). There are also 33 sessions of 7 mice that match the callosotomy group, though no file says so. The behaviour-only sessions, the photoactivation mice, the untrained mice and any pre-callosotomy session are absent. The one behaviour-only file is empty.
- **No photostimulus column in the trial table.** Site, number of laser spots and timing can only be read from the per-site laser traces and the photostimulus events.
- **36 sessions have no photostimulus record at all** (the 33 callosotomy-group sessions and 3 in experiment 1). Most of them still contain trials where activity is silenced, so their control trials cannot be identified.
- **In lick-early trials the photostimulus events are logged at the restarted delay**, up to 1.6 s after the light in the trace.
- **Format problems:** one session has two interleaved, overlapping trial sequences; 28 units have spike times out of order.
- **Units:** the `cell_type` column labels intermediate-width units as FS, and about 33 intermediate units are missing.
- **Neuron and session counts:** the paper's counts (55, 143 and 40 neurons; 16 sessions) cannot be reached with the selection rules the paper states.
- **Questions asked (10):**
  1. Whether lick-early trials enter the neural analyses.
  2. Which window sets a neuron's preferred trial type.
  3. What "more than 3 trials in all conditions" counts, and whether a further selection lies behind the legend counts.
  4. Whether a selectivity bin is labelled by its centre or its end, and how far the recovery search runs.
  5. Which sessions and neurons make up the paper's 16.
  6. For ed4, the selection test and the time-course bin.
  7. Which 2 x 2 table the ed6a Fisher test uses.
  8. How the modes are built: the trial split, which trials are decomposed, and the sign of the ramping mode.
  9. How a lick is read from the analogue `lick_trace`.
  10. How the fig6 noise scales with the integration step.

### 3. Where the protocol was unclear or missing something
1. It doesn't say how to combine the claims file's "holds under any reading" rule with readings of details the author found open. I applied the Reader step 3 rule: if my readings give different outcomes, the claim is blocked as methods_underspecified. This is what blocks fig1g and ed7.
2. Readings multiply quickly (up to 256 combinations per claim), and there is no guidance on how to report that many. I printed the full table plus a summary per combination of open details.
3. The claims file's literal "trials per condition" was not something I could leave open, so I followed it and showed per-trial-type counting as a variant only.
4. Two claims are simulations that use no data, and there is no `data` kind for that. I left them as the default and tested them.
5. Unlabelled photoinhibition trials fit both data_missing and metadata_insufficient. I used metadata_insufficient for the callosotomy claims, and data_missing where whole sessions are absent (no pre-callosotomy sessions).
6. The data settled one of the claims file's own open points: the recorded "late delay" light ends 0.3 s before the go cue. There is no channel for passing that back, so I noted it in the notebook.
7. The protocol's rule for selections only covers chance levels. When a selection count is far from the paper's (55 against 138 to 173 neurons), I recorded a deviation and did not block.
8. Whether the measured recovery time is the point estimate or the bootstrap mean is not specified. I used the point estimate and printed the bootstrap mean beside it.
9. The header table only allows "tested" or "blocked". fig1g and ed7 were run but their outcome is blocked; I marked them as tested.
10. The questions files in the repo each name a single claim. Several of my questions apply to many claims, so I listed them all in the `claim` field.

### 4. Runtime and failures
- The notebook runs in about 11.5 minutes, of which about 3 minutes is streaming 91 files, which misses the protocol's 10-minute aim. It stays within the 30-minute limit.
- One run failed after I stripped bold markup with a regex that also removed `**` operators from the code. I restored them, re-ran, and the outputs matched the earlier run exactly.
- The repository root has untracked files I did not create (`.bashrc`, `.profile`, `.idea`, `scripts` and others). I left them alone; the workflow commit may pick them up.
