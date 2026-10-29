I've revised the attempt for verifier round 1. The entry re-ran cleanly (`entry.py all`: 0 errors, notebook passes in 232 s), every number in the conclusions matches the new run, and `check` passes. Nothing is committed.

**Outcome changes (four, all as the verifier gave them)**
- **fig4-broad-near-zero**: partially_reproduced → not_reproduced. The criterion has no partial rule, and the condition that fails (interquartile range of r at least 0.3) is the one that tests breadth. The conditions that pass are also met when condition labels are shuffled.
- **fig6d-perimovement-best-j-array**: reproduced → partially_reproduced (still resting on the range reading of "tuning", O1a). The criterion must hold under every reading, and 32 of 96 readings are partial. No reading shows the peri-movement space ahead at p < 0.05 (p 0.47 to 0.98).
- **fig7c-anterior-posterior-performance**: not_reproduced → blocked (`other`). The upper limit used for normalising is at or below zero, so the normalised measure the criterion needs does not exist.
- **prep-activity-more-anterior**: not_reproduced → blocked (`metadata_insufficient`). The result flips with which array is PMd: not reproduced if prefix 1 is PMd, partial if prefix 2 is, in all 12 readings each way. Nothing in the file says which.

All other outcomes are unchanged and the verifier agreed with them.

**What I added or corrected**
- **Noise checks on the data** (problems 1 and 2):
  - With condition labels shuffled, 82 to 96 units pass the > 5 spikes/s range rule, against 93 with the true labels.
  - Shuffled labels meet the fig4e criterion in 18 to 20 of 20 shuffles and the suppfig1 criterion in 11 of 20.
  - With preparatory and peri-movement means taken from separate trials, fig4e is met in 4 to 9 of 12 readings (correlation at -200 ms only 0.12 to 0.18), and suppfig1 in 2 of 12.
  - fig4e and suppfig1 stay reproduced, but their conclusions and notes now say the pass carries little evidence. The selection-noise result is added to the `data_missing` finding.
- **Spread of the comparisons** (problem 3): fig6d and fig6-maze now print SEs and paired tests. Against a shuffled-label null, the fig6d performances are above noise even though below zero. fig7b leaves the ratio undefined when performance is not positive; its recorded value is now the SD-reading ratio, 0.501.
- **Second reading of the peri-movement space** (problem 6): the Methods restrict preparatory analyses to included units, so I also built the space from the included units only. Under the range reading this changes nothing. Under the SD reading the peri-movement space loses its lead in fig6d and fig6-maze. That reading is now a deviation, and the question is added to the `methods_unavailable` finding.
- **Array mapping** (problem 4): the anterior-posterior cells print results under both mappings, and the text no longer claims support for prefix 1 = PMd beyond the order of the electrode groups.
- **Partial runs** (problem 5): fig7a, fig7b and fig7d now cover all six onset/proto-trial settings, and fig7d covers both O1 readings. None changes an outcome: fig7a passes 24 of 24, and in fig7d segment directions beat the peri-movement space in 23 of 24.
- **Docstring** (problem 7): removed the unused `hold` from `simulate_rotation`, and its deviation from the record.
- Updated the notebook header and summary, the README, the attempt notes, and round 1 under `verifications`.

**Not done**
- I added no reader questions: the verifier reported no place where the claims file misreads the paper.
- The verifier's other unchecked items (whether this session is the paper's J-array session, and the figures) need provenance or visual inspection this run can't provide.
- The notebook now takes about 4 minutes instead of 2, mostly from running fig7d on every reading.
