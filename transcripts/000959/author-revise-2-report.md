I've addressed every point in the round-2 report and re-run the entry: the notebook passes in 663 s and `tools/entry.py check` gives 0 errors. No outcome changed and nothing is under `proposed`: 23 reproduced, 5 partially reproduced, 2 not reproduced and 6 blocked.

**Saccade claims (the verifier's one objection to how outcomes are recorded)**
- Both saccade outcomes are now marked `assumed: true`. Each has a deviation stating the assumption: the detector runs on the files' unfiltered gaze, as the paper's code passes it, and that detection is taken to stand in for the paper's. The paper names the software but says nothing about filtering or about the saccades it found.
- I kept unfiltered gaze as the choice because it is what the paper's code does. I did not run a filtered variant.
- MATLAB isn't available here, so the port still has not been checked against the MATLAB code. Instead, a new notebook cell runs it on synthetic gaze:
  - With little noise it finds all 93 saccades, with median duration 38 ms both detected and true.
  - With white noise matching the data's velocity inside fixations (median 19.8 deg/s), it finds 86.7% of them and doubles their median duration (72.5 against 37.5 ms).
  - The real data's durations are longer still (median 147 ms), so the data's noise is not only white.
- I added a `methods_unavailable` finding that asks the paper's authors whether the gaze was filtered and what the detected saccades looked like.
- The data-check cell now also lists the groups of a social file, which hold no saccade tables. Before, this was shown only for a control file.
- The notebook conclusions, the summary, the README and the helper's docstring now state the assumption.

**Corrected text**
- **Causal-decomposition timings:** the record now uses this run's numbers.
  - One decomposition takes 15.9 s on one core and 6.8 s on four processes.
  - The 2,250 OFC or dmPFC epoch trials take about 159 CPU hours (68 h of wall time on four processes); ACCg takes about 166.
  - Every social trial takes about 1,380 CPU hours.
  - The timing changes from run to run (13.1 s in round 2), and the notes now say so. The outcome (blocked, too large) is the same either way.
- **Cell 93:** the sentence that compared CPU hours with the one-hour wall-time limit now says the 12 CPU-hour lower bound would fit in an hour only on a dozen or more cores, not on four.
- **Partner monkey:** the test count is now "1 of 18 tests" (was 21), in the notebook and the record.
- **Cell 90:** the five excluded days are now said to be named by the paper's code, since the paper gives only what they consist of.
- **Summary:** it now gives 6.3% of Eyes events outside the Eyes rectangle for social runs and 10.7% for control runs.
- **Record notes:** the dmPFC density sums are now −2.56 and −0.0027, and monkey T's control trials per day are 71 to 77.
- **Round 2 under `verifications`:** 34 agree. The two saccade claims are recorded as `agrees: false` with the same outcome, because the report says it agrees with them "as computed" but counts only 34 of 36 as agreed.

**Not done**
- **Eyes-against-RDM comparison:** still waiting on a reader, as in round 1. Nothing to add here.
- **Inter-looking interval:** still sits near the threshold (p = 0.044, or 0.058 if the 91 events starting on the trial sample are counted). The question is with the paper's authors.
- **Nothing committed:** the workflow does that.
