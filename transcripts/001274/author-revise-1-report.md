I've revised the attempt for every point in the round-1 report. Seven outcomes changed, and on six of them I now agree with the verifier. On the seventh, `fig1-max-rate-ceiling`, I changed the outcome in a different direction from the one the verifier proposed. The entry re-ran cleanly with `python tools/entry.py all` (0 errors, 643 s), and `check` passes. I updated the notebook conclusions, the summary, the README and the record to the new numbers, and recorded round 1 under `verifications`. Nothing is committed.

**What changed in the outcomes**
- **Partial outcomes the criteria don't allow (problem 3):** five claims I had scored as partially reproduced are now not reproduced, as the verifier gave them. Their criteria have no partial outcome and each fails a required part: `fig1-pure-sine-excites-all`, `fig1-onset-delay`, `fig2d-20khz-twofold-threshold`, `fig3c-sustained-firing-2s` and `figs2-ttx-blocks-depolarization`.
- **`fig2-modulated-locks-to-beats`:** also now not reproduced. Part (iii) now uses the full block test (problem 4). The failing session ends at 5.9%, above its near-threshold session at -0.2%, so it still fails.
- **`fig1-max-rate-ceiling`:** changed from reproduced to not reproduced, marked as resting on an assumption. The verifier proposed blocked because the two AP readings disagreed (59.9 Hz against 42.9 Hz). After the fix to reading (a) below, the ceiling is 39.1 Hz under (a) and 42.9 Hz under (b). Both are now outside 54 to 99 Hz, so the readings agree. The record shows this disagreement with the verifier and says it has not yet seen the new numbers; round 2 should review it.
- Everything else is unchanged. `fig2c-pure-more-aps` stays reproduced (47 pairs against 0). `fig2d-modulated-thresholds-higher` stays partially reproduced, now with 2 of 3 pairs significant under both readings. The other claims stay blocked.

**What I added or corrected**
- **AP reading (a) (problem 1):** it now also asks a peak to rise 5% above the trace around it and to be at least 1 ms wide at half height. This is a stated assumption based on the AP size and duration in the paper's Methods. A new check runs the verifier's synthetic test:
  - The old rule finds about 18 false APs per 250 ms on a 6% plateau of pure noise; the revised rule finds 1.2.
  - The revised rule finds synthetic AP trains of 40 to 100 Hz at their true rate.
  - All first APs in the data pass both new conditions.
- **Traces with detected APs marked**, as the verifier asked:
  - the sessions that set each neuron's rate ceiling, with their dF levels;
  - the highest-field session of every neuron;
  - the modulated sessions with the most APs;
  - neuron c7 at 83 V/cm;
  - the 7 near-threshold sessions with a first AP before 20 ms. They show AP-shaped events, not stimulus artifacts.
- **The two neurons never excited at 20 kHz:** their traces and images are shown. One (sub-10-4) has small upticks below 5% at 324 V/cm. If they were counted, 16 of 17 neurons would be excited. No reading in the claims file counts them, so the outcome stands.
- **Field and calibration (problem 2):**
  - The paper's 63 and 81 V/cm match voltages the sessions use only under the half-voltage reading.
  - A 2-kHz calibration factor of 0.76 would bring the threshold to the paper's 57.7 V/cm. The only measured factors in the paper's dandisets, from pulse recordings in 001273, are 0.62 to 0.79.
  - The 20-kHz factor would have to be 0.64 to 0.97 times the 2-kHz one for the threshold ratios to fit.
  - The real factors aren't deposited, so these outcomes stand, with the caveat in their notes.
- **Sodium gluconate check (Figure 3B):** none of 47 neuron-carrier pairs shows a reversible drop in threshold of the kind a switch to sodium gluconate would cause. The claim stays blocked.
- **001034:** all 178 assets now match 001032 one to one by session start time and size.
- **Strobe variants (problem 7):** the 15-V pulse is now scaled to its own field, giving 19.5 ± 2.4. The plot of frame timing supports the assumed pulse onset. The biases the verifier pointed out (ROIs placed on the image they are measured on, phase fitted on ROI 1) are stated. These variants decide no outcome.
- **Smaller points:** I removed the variant count that was identical to the main one, and noted the bleaching drift, the unidentified vehicle neuron and the 3.6 to 11 min session gaps.

**What I did not do**
- I added no reader questions to `questions/001274.yaml`. The report names no place where the claims file misreads the paper.
- I did not build a rebuilt-ROI variant for Figure 4. Without the paper's ROIs or the cells' shape groups it could not decide any claim.
- I did not correct for bleaching the 250-ms recordings used in the window-mean tests (problem 10). The paper's Methods apply the correction only to the 2-s recordings, and the near-threshold sessions end at a median of -0.2%, so the effect is small.
