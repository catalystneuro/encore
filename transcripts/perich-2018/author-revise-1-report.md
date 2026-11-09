I've answered every point in the round-1 report. No outcome changed: the verifier agreed with all 28, and the new outputs support each one, though some now carry stated conditions. The re-run passed `python tools/entry.py all` with 0 errors, the notebook passed, and the numbers match my development run exactly. Nothing is committed.

**Outcomes (unchanged)**
- **methods-neuron-counts:** partially reproduced, assumed.
- **fig3b-pmd-higher-dimensional:** reproduced, assumed. It now states that it holds only with the kernel read as 100 ms full width at half maximum. Over the 2002 possible 16-session sets, the medians are within tolerance in 910. With the kernel read as a standard deviation they are within tolerance in none, though PMd stays above M1 in every session.
- **figs4d-dimensionality-robust-to-size:** reproduced, assumed.
- **figs4c-null-potent-index-centered:** reproduced, assumed.
- **fig6c-null-leads-potent:** partially reproduced. It now states that it rests on using all 21 candidate sessions. Over the 2002 possible 16-session sets, the main reading is significant in 763 (38%) and at least one of the 8 readings in 1013 (51%).
- **The other 23 claims:** blocked, data missing.

**Added or corrected**
- **Session descriptions:** the notebook now reads them. The record said they were empty in all 111 files, which was wrong. Seven Monkey C sessions (2016-09-09 to 2016-09-23) end in "Warning: This session with Monkey", cut off in both the files and the archive metadata. I replaced the finding. These are the same seven sessions where the cursor ends about 4.2 cm from the centre.
- **fig3b:**
  - Per-session values with the full-width kernel.
  - Medians over every 16-session set.
  - A synthetic check of known rank 5: the adopted noise scale with rule (b) returns 5 in all 9 runs, and rule (a) returns 16 to 45.
  - The kernel dependence is now a deviation. The claims file expected the kernel reading not to matter.
- **figs4d:** now run with both kernels and 100 subsamples per size, the claims file's number. Under rule (b), PMd beats M1 at every size under every reading, by 1.30 to 4.63 dimensions. The markdown no longer gives the wrong reason for its readings. Rule (a) now has one exception: 40 neurons, full-width kernel, window (b), a difference of −0.13.
- **figs4c:** the failing secondary reading's exact mean is 0.100085. Per-monkey means show a positive lean in Monkey M (0.109, above the 0.1 bound if judged alone) against Monkey C (0.028).
- **fig6c:** lags within one step of the search edge are now flagged. Without the two such sessions, the 50 ms reading gives −20.5 ms over 19 sessions (p = 0.034). Correlation curves are now plotted for all four window and resolution readings.
- **Data check:**
  - Signed reach errors are now printed. They back the statement the verifier said had no output (no large offset that decays).
  - A check of the assumed target-acquisition time: the reach ends 0.09 to 0.15 s after it in every session. That is consistent with the trial's stop time being the end of the hold, but does not prove it.
  - The pooled verdicts in the neuron-count table are now labelled as being for the whole set, not for 16 sessions.
- **Record and docs:**
  - The kernel question to the authors now includes the fig3b effect.
  - The `verifications` block holds all 28 claims with the verifier's reasons and my responses.
  - The README now says the notebook takes about 20 minutes. It ran in 19.3 here, against CI's 30-minute limit.

**Not done**
- **Reader questions:** none added to `questions/000688.yaml`. The verifier reported no misreading of the paper; it called the kernel expectation a wrong expectation in the claims file, not a misreading.
- **Unit sort:** whether the deposited units are the paper's spike sort can't be told from the files, so that point stays covered by the existing `selection_undocumented` finding.
- **figs4d noise repetitions:** still 100 per subsample, not 1000, to stay within the time limit. The notebook says so.
