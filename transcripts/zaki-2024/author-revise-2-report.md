No outcome changed in this round, and no change is proposed. The verifier agreed with all 26 outcomes: 6 tested and 20 blocked. The final `python tools/entry.py all entries/zaki-2024` run passed in 6.4 min with 0 check errors, and every number the record relies on came out the same as before. An earlier attempt at that run failed on a read timeout from the archive and passed when run again.

**Outcomes and findings**
- **fig5c-wake-overlap-neutral-coburst:** this now carries `assumed: true`, as the verifier asked. A new deviation says the outcome rests on reading wake alone, without the files' quiet wake, which is the worse match to the paper. Under the other reading, overlap co-bursts less with neutral than with aversive (25.9% against 35.3%). The notebook, summary and README now say this.
- **New finding 10** (`methods_unavailable`) asks the paper's authors whether the wake in Fig. 5c includes the epochs the files label quiet wake.
- **Finding 1** (the behaviour sessions of Ca_EEG2-1 are timestamped about 1 h off the telemetry clock) is changed from `major` to `critical`, the verifier's rating. The data show the 1 h offset, and an analysis that takes the timestamps as given would put the offline recordings in the wrong order. Under this round's `findings` it is recorded as the verifier gave it: `agrees: false`, `severity: critical`, because it reviewed the finding while it was still rated major. As a result the site will not show it as a checked critical finding until a later verifier reviews it at that rating.
- **offline-bursts-above-shuffle:** stays reproduced under reading (b). The verifier's view that this reading "cannot really fail" is recorded. The criterion counts a result under either reading, so switching to reading (a) is not an option. The question is already with a reader in `questions/zaki-2024.yaml`.

**Outputs added**
- The burst and skew shuffle tests now print the largest surrogate and the fraction at or above the true value for every seed, not just one. No surrogate reaches the true value under any seed.
- The movement analysis now prints movement by quarter of each recording and its correlation with time. This backs "movement declines over the recording" for Ca_EEG2-1 (Spearman rho −0.459).
- The sleep description now prints the same-clock-time reference for the window after aversive encoding: 82.7% awake.

**Text corrected**
- "Not lower" became "not significantly lower", with the medians given, including the two recordings where they are lower before the burst.
- The double negative in the summary ("no pre-burst slowing in 0 of 3") now reads "pre-burst slowing (p < 0.05) in 0 of 3 recordings".
- "p < 0.001" became "p = 0.000 with the first generator, 0.003 with the second".
- "Ensemble sizes agree with the source data" is gone, because no comparison was printed.
- The sleep comparison now gives "93% and 83%" as the references for the two windows.
- The README run time now reads four to seven minutes, and `runtime_minutes` in `entry.yaml` is 7.

**Not done**
- No new reader question was added, because the verifier reported no new place where the claims file misreads the paper.
- The verifier's point C5 is only that it did not have `questions/zaki-2024.yaml`, so there was nothing for me to fix.

Nothing is committed.
