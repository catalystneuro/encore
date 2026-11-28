I left all 34 outcomes as verified: 11 reproduced, 12 partially reproduced, 11 not reproduced. Two ratings went up to critical, and I proposed one outcome change for round 3. `python tools/entry.py all entries/sabatini-2024` ran from a clean environment and passed for all three notebooks, and `check` reports 0 errors. One wrong sentence remains in the notebook summary (see the end).

**Outcomes**
- **Proposed change (fig6e-kinematics-predict-location):** the verified outcome stays reproduced, with partially reproduced written under `proposed`. The cause is three bad units, described under Findings below, which the main analyses keep. A new companion notebook, `reproduce_sabatini_2024_stable_units.ipynb`, leaves them out. The paper used "single-units and stable multi-units". In that notebook, M1-N's kernel value is 90.9% (89.2 to 90.9% over the five seeds), above the 89.1% bound. That fig6e figure is the only outcome that changes there.
- **Shuffle span (tbf-shuffle-control):** the paper's code fixes it to the analysis window (`scrambleTrials.m` and `preprocessTrials.m`). I ran that span: shuffled values are 42.0, 29.4, 41.9 and 42.1%, and recoverability chance is 89.9, 86.8, 89.5 and 89.9%. PMd-J is still below its range, so neither outcome changes.

**Findings**
- **Finding 1 (overlapping clocks in the Nitschke file):** raised to critical, the verifier's rating. The segment bounds now quote the printed values.
- **Finding 3 (Jenkins unit 1):** the new output settles it, and it is now critical. Unit 0's spike train stops at 4259.0 s. 55 ms later the first of unit 1's two runs begins: 196,608 spikes running to the end of the session. The two runs share only 1,049 spike times. Neither run alone has intervals under 1 ms, but 3.5% of intervals are once merged. The first run matches other units' spike times the way unit 0 does (37.4% against 27.9%); the second run matches at most 2.5%. So unit 1's row appears to hold the rest of unit 0's train.
- **Finding 6 (segment 3):** rewritten and raised to major. It is not a change of the recorded units, as the old text said. One M1 unit (170) fires above 100 spikes/s on 229 of the 532 trials in segment 3. Without it, decoding within segment 3 rises from 0.179 to 0.425. The per-trial spike-count distributions the verifier asked for are printed and are similar across segments.

**Other corrections**
- Fixed the verifier's text slips in cell 64 (fig5a wording), cell 98 (four other seeds now 65.5 to 87.1%) and the fig3a row of the Summary.
- The fig7f-decoder-beats-standard notes now say the instantaneous baselines test little.
- Added round 2 under `verifications`: all 34 claims agreed, in the verifier's words, plus its review of findings 1 and 3.
- Also updated the units deviation on every outcome, the README, `entry.yaml`, and one of the questions to the paper's authors.

**Not done**
- **Wrong summary sentence:** the notebook Summary says unit 1's first run shares "0.4% of its times" with its own second run. The correct figure is 0.5% of the first run (1,049 of 196,608); 0.4% is the share of the second run. The full run takes 100 minutes and would not have finished before the 21:22 cutoff, so this was not corrected. The attempt record gives the correct count. It needs fixing in the next revision.
- GPFA decoders: not run.
- jPCA port fidelity: still unchecked, because the paper's code needs preprocessed files that are only available on request.
- The fig7f baselines keep the paper's length scale of 100.
- No new question for a reader: the verifier reported no new place where the claims file misreads the paper.
