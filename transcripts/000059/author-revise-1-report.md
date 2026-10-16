I've handled round 1. One outcome changed. I re-ran the entry twice with `tools/entry.py all`; both runs passed with no check errors and printed the same numbers. The second run took 632 s, so I set the runtime in `entry.yaml` and the README to about 12 minutes. Nothing is committed.

**Outcome change**
- **fig5-speed-control-cooling:** changed from partially_reproduced to not_reproduced, as the verifier said. The criterion needs both speeds within tolerance under one reading and has no partial case. Under all frames, both speeds fall outside. Over frames above 10 cm/s, the control speed is inside but the cooling speed (76.0 cm/s) is just below the limit.
- **Totals:** 12 reproduced, 15 partially reproduced, 10 not reproduced, 1 blocked. This matches the verifier's count.
- **Verifications:** the round is recorded in the attempt record, one entry per claim, with the verifier's reason and my response.

**Fixes and the outputs the verifier asked for**
- **fig5d (pair period, problem 1):** I kept the outcome, because the criterion fixes the estimator. The verifier was right that it is biased: in 47.7% of pairs it picks the second neighbouring peak. I added per-pair histograms and the nearest-peak estimator as a variant. That variant gives a control period of 91.0 ms, inside 85 ± 8.5, and still lengthens during cooling (P = 0.031). Under it all three parts of the criterion hold, so the claim would be reproduced. The notes, the conclusion and a deviation say this.
- **fig3f (information, problem 3):** I added a variant with each state's spikes subsampled to the same count. Information still drops: pre against cooling P = 0.0073, pre against post P = 0.0092. The spike-count bias does not explain the result.
- **suppl1g (waveforms, problem 5):** I added the number of spikes averaged in each window. In the 208 units whose two means both use 300 spikes, the changes remain (amplitude P = 0.032, trough-to-peak P = 2.2e-05). Drift still cannot be separated from cooling.
- **fig5j and fig5k (problem 4):** I added session-level tests for all three comparisons, cycle durations, and cycle counts per session. The notes say the pooled tests reflect how the sessions are mixed. One new result: per session, spikes per cycle differ between pre and post (P = 0.02).
- **fig5cg (problem 2):** In 10.5% of pairs the lag changes when the window is narrowed to half a theta period, so the notes now say the compression size cannot be judged from this method. I also corrected an earlier error: the inverse-regression value I quoted (9.085 cm/ms) was a per-session median, and the pooled value is 7.175 cm/ms.
- **cooling-time-course:** I added the onset-aligned mean temperature trace. 90% of the drop comes a median 53 s after onset, close to the paper's 60 s, but the criterion measures time to the minimum (121 s), so the outcome stays partial. A variant without the five sessions with temperature artefacts gives 121.5 s.
- **Files and channels:** every series in all 100 files is now listed. The only temperature series is the medial septum one, which confirms the hippocampal-temperature block. The LFP channel is now looked up through the file's electrode map; it is correct in all 49 sessions with LFP read.
- **Second cooling blocks:** I printed the state sequences for the 12 sessions with two cooling blocks. The helper now stops the aligned series at any return to cooling; no number changed.
- **fig6c:** I added error rates for trials 21 to 40 and sessions per trial. The notes now say the peak at trial 7 is narrow, with a second rise to 0.186 at trial 20.
- **Code fixes:**
  - The fig4b 30-spike variant could not differ from the main result, so I replaced it with 100 and 200 spikes and corrected the notes.
  - An unused direction flag in the fig2i cell was inverted; fixed.
  - fig4a was dropping the last 20-trial window. It now gives fLFP R = 0.678 and slope 0.0716, and the notes say the overlapping windows overstate the P values.

**Not done**
- Problem 11 (theta power measured on the band-passed signal): I left it unchanged, since the verifier found it matches the paper's code. It is recorded as a deviation.
- Problem 7 (the time-to-minimum measure): the criterion fixes it, so I added the 90% time alongside it and did not change the measure.
- I downloaded no paper text, so there was nothing to save under `paper/`.
