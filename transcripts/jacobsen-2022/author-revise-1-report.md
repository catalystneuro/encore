No outcome changed. The verifier agreed with all 28 (7 tested, 21 blocked as data missing), and the new outputs did not move any of them. The entry re-ran cleanly with `python tools/entry.py all entries/jacobsen-2022` (201 s) and `tools/entry.py check` reports 0 errors. Round 1 is recorded under `verifications` for all 28 claims, quoting the verifier's reasons, with my reply under `response`. Nothing is committed.

**What I changed, by report point:**
- **B1, dandiset versions:** the header said the earlier versions hold the same 9 files. It now says version 0.220426.0814 holds 18 (the 9 sessions twice, under real and hashed subject ids), and a new data-check cell lists the files in every version. I also added this as a finding.
- **B2, shuffle:** I quoted Rowland et al.'s "random interval between ± 20 s" sentence in the notebook and helper. The analysis code that paper links has no spatial shuffle, so it does not settle the question. I printed the shuffled score distribution for the head direction cell T4 C16: the literal reading's 95th percentile is 0.762 and its largest value equals the observed 0.912. The standard shuffle stays the stated assumption. The conclusion now also says the standard shuffle is lenient for weakly tuned cells.
- **B3, the two laser epochs of day 17:** a new cell shows that the file cannot tell them apart. Both have power "N/A" and the same pulse widths (1.0625 ms) and intervals. It also lists each unit's spikes, latency and fidelity per epoch. The text now says that choosing an epoch per cell goes beyond the criterion, which only allows trying each session.
- **B4, open-field span:** using the whole position series is now a stated assumption. The first-1800 s reading (the Methods' "approximately 30 min") is run for all 12 units, with rates and classes:
  - no class changes;
  - no other rate moves by more than 0.001 Hz;
  - for figs3-stable-input-cell, all 18 values match under that reading (1.064 Hz, 2.951 ms, 48.00%).

  I kept that claim at partially reproduced. The paper states no cut, and the 1800 s reading was found by matching the expected values. Both results are shown, and the verifier gave partially reproduced too.
- **B5, the T4 C16 head direction values:** I ran 48 tuning settings (bins of 2 to 10°, smoothing 0 to 20°, with and without the speed filter). The 9.02 Hz peak is matched only with smoothing of 4 to 14°, against 10.62 Hz with the setting from the Rowland code. No setting matches both the peak and a 0.81 score.
  - The measured head direction score in the record is now 0.912, the tuning-curve vector length that Rowland et al. call the head direction score. It replaces 0.880, which the verifier showed does not identify the score.
  - I updated the question to the paper's authors.
- **B6:** the conclusion now says the waveform does not identify the cell. The identity rests on each file holding one curated unit and on the Methods saying the tetrodes were not moved between these sessions.
- **B7:** the notes say the deposit is curated and that the mec-inputs test cannot fail on the early side.
- **B8:** the border-score baseline is now described in the helper; the method is unchanged.

**Not done:**
- B9 needed no change. A spike exactly at the pulse time is not counted, which the verifier called immaterial at the 48 kHz spike clock.
- I added no questions to `questions/jacobsen-2022.yaml`, because the report found no place where the claims file misreads the paper.
- The verifier could not see the rate-map images. I did not add more, since the grid and border judgements rest on the printed scores.

I also changed the runtime in `entry.yaml` and the README from 2 to 4 minutes.
