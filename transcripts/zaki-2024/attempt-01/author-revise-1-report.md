The verifier's round-1 points are answered, and the entry re-runs cleanly: `tools/entry.py all` passes with 0 errors in about 2 minutes. One outcome changed. Nothing is committed.

**Outcome change**
- **`fig5c-wake-overlap-neutral-coburst`** goes from partially reproduced to not reproduced. The verifier argued that the Methods' sleep scoring has no quiet-wake class, so "wake plus quiet wake" is the faithful reading. I tested that by applying the Methods' own scoring to 12 h of Ca_EEG2-1's EMG (6 s epochs, a two-state model on log EMG RMS). It puts 94.1% of quiet-wake frames in wake, and all 87 bursts. Under that reading overlap-neutral co-bursting is below overlap-aversive: 26.4% against 35.6%, McNemar p = 0.13. The criterion had allowed the wake-only reading too, so judging on one reading is recorded as a deviation.
- Two limits are stated alongside it:
  - Only one of the 24 offline recordings is deposited, so the ensemble traces are z-scored within that recording, not over all 24 as in the Methods. The levels here (26 to 36%) are not comparable with the paper's 10.37% and 8.39% for this mouse.
  - The Methods don't name the EMG measure. Without the log, the model puts every epoch in one state.

**Unchanged outcomes**
- **`offline-bursts-above-shuffle`** stays blocked (methods underspecified). The record already had it that way; the verifier didn't see the record and suggested the same. A synthetic control now in the notebook confirms the criterion's shuffle test can't detect coordinated firing: 5.6 true bursts per minute against 34.98 in the shuffled data, even with coordination planted.
- **`offline-skew-above-shuffle`** stays reproduced. The same synthetic control shows this test does detect coordination.
- **`burst-locomotion-pause`** stays not reproduced. The notes now say the test gives p = 0.016 at random times in Ca_EEG2-1, so it is not calibrated, and that the result is weak evidence against the paper.
- **`ed9b-aversive-freezing-high-vs-low`** stays reproduced. The notes now say the 30 s bins are not independent, so the p-values overstate the evidence.

**Outputs added at the verifier's request**
- **Activity signal:** its description and value range, its correlation with EMG (r = 0.11 to 0.55), and that it is 4 to 15 times higher in wake than in quiet wake.
- **Sleep-state descriptions** from the files.
- **The full 27-row epoch table:** it supports Ca_EEG2-1's first offline recording being the first after fear conditioning.
- **Telemetry rate:** the files hold telemetry at 500 Hz, where the Methods say 100 Hz. This is now a new finding.

The co-bursting outside bursts now uses only windows where every frame is in the same state. With that fix the top value is 1.02%, so the earlier "under 1%" was corrected.

**Other edits**
- `memlink.py` has a new `emg_wake_gmm` helper, and scikit-learn was added to the requirements and the lock file.
- The README table and the notebook summary match the new outcomes.
- The attempt record has the round under `verifications` for all 26 claims, with the verifier's reasons and my responses.
- The paper's text is saved under `paper/`.

**Not done**
- **Partial tests the verifier said were possible on three blocked claims:**
  - Centroid-based registration for the low-shock fig5c claim: it would replace the paper's registration method with mine, and a "no difference" claim can't be judged on one recording of one mouse.
  - One-mouse sleep scoring for ED9/ED10: the claim compares mice across days and groups, so one mouse would only describe it.
  - A one-mouse SVM for ED7: the paper reports that analysis only for the one-hour cohort.

  All three stay blocked, with the reasons in the record.
- **Handover package:** I did not rebuild it, since round 2 gets the full executed notebook.
