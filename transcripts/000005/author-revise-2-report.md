The round-2 report agreed with all 33 outcomes, and no outcome changed. I found no reason to propose a change, so nothing is under `proposed`. I re-ran the notebook twice from a clean environment, and every number cited in the record, notebook and README matches the new output. Both runs gave the same numbers.

**Corrected (the sentences the verifier said the outputs do not support):**
- **`exc-thalamus-photoinhibition`** (cell 73 and the record notes): I removed the claim that the thalamic latency is "still not longer" past the onset transient. The text now says the 2 ms diagnostic uses different thresholds for the two averages (−0.0206 against −0.0557 mV), so it cannot compare them. The 1 ms bins (5.0 against 3.0 ms) and the 0.5 ms averages both put the thalamic onset later. None of these decides; by the criterion's rule the thalamic latency is still not longer.
- **`ion-cut-exc-no-touch`** (record notes and cell 20): anm281589, anm281592 and anm318531 are now described as lacking a 1 mV touch PSP while each has a cell with spike touch input. That makes them weak candidates at most, out of at most 7.
- **README:** it now names both flag rules (no touch input, or performance below 0.5). It says `auc-weak-strong` fails only on reading (b), which matches in 8 of 20 seeds against 19 for reading (a). The run time is now about 10 minutes, and a note says round 2 changed no outcome.
- **`exc-vm-touch-whisking`:** the measured whisking change is now 0.83 mV, the first reading the criterion lists, where it was 0.87, the best of 16 readings. I removed values no current output prints (−61.61, −34.9, 0.74, 4.36).
- **Minor:** cell 99 now says 5.54, and cells 52 and 73 say "above" where they said "below".
- **Untested cells:** the summary, the `exc-mainly-touch` deviation and the `exc-vm-touch-whisking` notes now say that two of the 26 untested VGAT-ChR2 cells are likely FS. Both appear in the list cell 13 already prints. The summary and `exc-mainly-touch` notes also say whole-cell E cells fire 0.70 spikes/s without whisking, above the paper's 0.4.
- **Round-1 reasons:** I added the verifier's ION-cut point (B1) to `fs-touch-response`, `exc-mainly-touch`, `exc-threshold-touch-vs-whisking` and `fs-vm-touch-whisking`. I added the spike-detection point (B4) to `fs-suppress-movement-spiking` and `auc-groups`.

**Added:**
- **Round 2 under `verifications`:** all 33 claims, each with agreement, the verifier's outcome, its reason paraphrased from the report, and my response.
- **Three questions for a reader** in `questions/000005.yaml`, from the claims-file issues the verifier raised:
  - Whether one-sample dVm/dt crossings should count in the latency rule.
  - Whether `behavior-false-alarms` "reproduced under a reading" overrides the header rule that readings must agree.
  - Whether the r2 > 0.25 share of cells needs a comparison against chance.

  I did not change the claims file.

**Not done:**
- **ION-cut cells in the control groups and the waveform boundary:** these cannot be fixed, because the files do not mark the ION-cut mice. Both stay stated as limits.
- **Check failures:** `python tools/entry.py all` stops at the check, which reports 25 errors. All of them are in the earlier record `attempts/000005-yu-2016-01.yaml`, whose claims were rewritten; this record adds none. I ran `entry.py run` directly to execute the notebook.

Nothing is committed.
