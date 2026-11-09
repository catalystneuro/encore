I've revised the 000409 attempt for round 1. The final clean run passed in 24.8 minutes and `tools/entry.py check` reports 0 errors. Nothing is committed.

**Outcomes changed**
- **traj-stim-regions:** blocked → not reproduced. The verifier was right that it fits the time limit, so I added a criterion to the claims file before running it, then tested all 201 canonical regions.
  - 46 regions are significant with Benjamini-Hochberg at q = 0.01 and 62 at uncorrected P < 0.01, against the paper's 104 ± 10.4.
  - The paper's code differs from its Methods in two ways: it merges the unbiased block with the 0.2 blocks when permuting, and it uses a Benjamini-Yekutieli correction. I added both as variants, plus a variant that includes the 64 sessions with broken block labels. These give 46 to 53 regions, so they don't explain the gap.
  - Only uncorrected P < 0.05 gets close (91 to 98). My result agrees with the paper's per-region significance column in 133 of 201 regions. I didn't find the cause.

The record now has 17 reproduced, 4 partially reproduced, 2 not reproduced and 7 blocked.

**Disagreement kept:** behav-zero-contrast stays partially reproduced. The verifier would call it not reproduced. The criterion only defines the reproduced case: the effect is present, the t statistic is within tolerance, and the mean misses its tolerance by 0.04 points. Restricting to the 454 sessions named in the Fig. 1d legend gives 58.27%, against the paper's 58.7 ± 0.4, so the session set doesn't explain the miss. The disagreement is recorded under `verifications`.

**Outputs added, none of which changed an outcome**
- **Decoder penalty (B1):** the notebook now prints scikit-learn 1.9.1 and shows the L1 penalty is in effect (0 of 13 nonzero coefficients at C = 0.01, against 12 with L2).
- **Nested null for VISp (B2):** run on all 35 sessions with 30 nulls each, reusing the original pseudo-sessions. VISp stays significant (Fisher p 1.8e-05).
- **Single-cell null (B3):** labels shuffled at random over the tested trials select 7.7e-4 of units (stimulus) and 5.7e-4 (choice). The product of the two tests' separate rates is 4.7e-5 and 3.3e-5, close to the paper's 5e-5. So the two tests not being independent is enough to break the paper's stated rate.
- **Oscillation (B5):** the correct-versus-incorrect power difference holds with each unit's PSTH z-scored (18 of 27 sessions, p = 0.028) and with power as a fraction of the 4 to 20 Hz band (26 of 27). 4 sessions peak at the 4 Hz edge, not the 6 the verifier counted.
- **454-session variants (B6):** they leave behav-performance and behav-zero-contrast as they were.
- **Confidence interval for fig1g (B7):** resampling mice gives 7.4 to 13.2 trials for the 90% adjustment time, against the 4.5 to 11 needed. The claim still passes on the point estimate.
- **Latencies (C list, B10):**
  - Including the 64 sessions leaves the visual latencies unchanged, so dropping them doesn't explain the VISam difference.
  - Extending the window to 200 ms leaves IRN at 117.9 ms and GRN at 109.5 ms.
  - The distance curves are now printed as numbers.
- **Truncated sessions (B9):** both were truncated to 457 and 460 trials, so neither reached the 400-trial floor.

**Corrections**
- **Canonical-window baseline (B8):** the variant now uses the full-window baseline, as `state_space_bwm.py` does.
- **Truncation rule:** `analysis_mask` now drops a session that fails even at 400 trials, as the paper's code does. No session fails, so nothing changes.
- **Clock check:** now run on all canonical units of all 454 sessions. The spikes share the trials' clock in 448; it couldn't be shown in 6.
- **Findings:** added a code_mismatch finding for the trajectory permutation classes and correction, and updated the single-cell rate finding.

**Not done**
- **Other blocked claims:** wheel-speed-decoding, encoding-feedback-largest, video-correlates and granger-interactions are still not attempted. The verifier agreed they stay blocked.
- **Runtime:** it went from about 11 to about 25 minutes, mostly from streaming every canonical unit for the all-region trajectories. That leaves about 5 minutes of margin under the 30-minute CI limit. To keep it down I used 30 nested nulls per VISp session instead of 50, which lets each session's p go no lower than 0.032.
- **Tests:** the B8 and truncation fixes have no standalone test that fails without them. The entry has no test suite.
- **Points left as they were:** B4 (the label permutation follows the paper's code) and B12 (the p-value floor) are recorded in the notes, not changed.

The paper text is saved under `paper/`.
