I've answered every point in the verifier's round-1 report, re-run the entry, and recorded the round under `verifications`. `python tools/entry.py all` passes in 1048 s with 0 errors, and the executed outputs match my development run apart from timings. Nothing is committed.

**Outcomes changed (round 1, so changes are allowed).** The totals are still 48 claims: 24 reproduced, 13 partially reproduced (was 14), 6 not reproduced (was 5), 5 blocked.

| Claim | Before | Now | Why |
|---|---|---|---|
| l4e-example-e24-e32 | partial | reproduced | As the verifier gave it. With the 100 ms rise reading, +1.07 and -1.75 mV are both within tolerance, and the criterion accepts one reading. |
| l4e-reversal-potential | partial | reproduced | Vm after a later touch is now set to NaN in the whisking-onset windows, as the claims file's method asks. The whisking reversal is then 4.9 mV above rest, just inside the 5 mV margin. |
| ion-cut-l4e-whisking | reproduced | partial | The same fix puts the control mean at 1.337 mV, 0.003 below its bound. The reduction is still significant under 3 of 4 readings. |
| enphr-auc | reproduced | not reproduced (assumed) | The touch-detection (AUC) analysis now leaves out the first touch of trials tagged passive, as every other measure does. That gives p = 0.16 and p = 0.09 under the two readings. Keeping those touches gives p = 0.038, shown as a variant, so this outcome rests on that choice. |

**Added or corrected:**
- **Depolarized trials.** All whole-cell files have as many ephys trials as whisker trials, so none was dropped. JY0978, the cell list's Fig. 3 example, has no depolarized trial. The near-0 mV trials are JY1139's first 18; it keeps firing in them with no injected current, so this is a drifting recording, not the Fig. 3 protocol. Both Fig. 3 claims stay blocked.
- **Drift rule.** Trials more than 20 mV from a neuron's median Vm are now left out of the Vm measures (13 trials, all JY1139), with keeping them shown as a variant. No FS outcome changes either way.
- **Distance to threshold.** A threshold line fitted through thresholds that all fall in one trial was ill-defined; their mean is used instead. I added two variants: the line held at its end values, and one threshold per neuron. The outcome stays partial; only the per-neuron threshold, which is not the paper's method, matches both means.
- **Other variants, none of which changes an outcome:**
  - the principal whisker taken from the whisker configuration, for the L4 E claims;
  - the highest light power only, for thalamus-inhibition-fs;
  - smoothing and hold windows for the light-onset latency;
  - light trials only, for thalamus-inhibition-dose;
  - latency read at the bin centre;
  - a chance level for fs-hf-fluctuations;
  - each mouse left out in turn, for enphr-behavior;
  - a split-half check of regression to the mean for enphr-auc.
- **Data check outputs.** Trial-type column names per folder (Hit/Miss/CR/FA everywhere, VPM included), pole-time ranges, and the cortical neurons against the data set's cell list. The cell list does not name JY1268 and lists JY0781, which has no eNpHR light in its file, among the eNpHR neurons; this is recorded as a new finding.
- **Header.** The outcome column is removed from the notebook header table; outcomes now appear only in the summary.
- **Questions for a reader.** `questions/crcns-ssc-7.yaml` is new. It asks about the three criteria the verifier found unable to tell the effect from its null: ion-cut-l4e-touch, thalamus-inhibition-dose and enphr-auc. Those claims stay as the claims file has them.
- **Files changed besides the notebook.** `ssc7.py`, the attempt record, `README.md`, and `entry.yaml` (runtime set to 18 minutes). `openpyxl` was added to the requirements and locked, for reading the cell list.

**Not done:**
- The spike-threshold search (verifier's problem 13) is unchanged. A forward difference, tried while preparing and not run in the notebook, moves E No. 1's threshold s.d. only from 8.91 to 7.98 mV, against the paper's 3.7.
- The 1 ms gap in the VPM median latency is still unexplained.
- enphr-behavior stays not reproduced, not blocked: leaving out any one of the 9 mice gives 3 or 4 decreases, never the paper's 6 ± 1.
- After the last run I changed one header sentence (streaming takes about twelve to fourteen minutes). No output depends on it, so I did not re-run.
