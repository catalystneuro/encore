I've worked through all of the round-2 points. No outcome changed and nothing is under `proposed`. The verifier agreed with all 39 outcomes, and nothing I found suggests one should change. The totals stay at 13 reproduced, 10 partially reproduced, 5 not reproduced and 11 blocked. `python tools/entry.py all entries/001950-su-2026` passes with 0 errors. The final run's printed numbers match the run before it, apart from timing and the new output lines.

**Output added to the notebook**
- **Check for antidromic stimulation events:** this is now a cell in the data check instead of an inspection outside the notebook. It scans the 165 files with spikes. None holds any stimulation object, no units column is about antidromic tests, and the metadata lists only the task or the go cue as stimulus. 56 files' metadata do name `antidromic_tagging` processing steps, but the stimulation tables those steps read are not in the files. This backs the block on fig6f-cortex-projecting-rpe-biased and the untested halves of fig5k, figs17i and fig6j.
- **fig5k quality threshold:** the notebook now prints Fisher's p at other thresholds. At 0.25 z it is 0.005 (94 sessions). At 1.0 z it is 0.38, which is not significant, but only 13 sessions from 3 mice pass. The outcome stays on the Methods' 0.5 z, and both numbers are in the notes and the stated assumption.

**Assumptions now stated**
- fig5k, figs15q and figs15t were marked as assumed without saying what was assumed. Each now has an "Assumed:" line. For figs15t it says the within-session null was chosen after the first result was seen, and gives the two failures under it (p = 0.18 and p = 0.048).
- fig5b and fig6f-outcome-angles-nonuniform are now marked as resting on the population, as fig5d already was. The conclusions and the summary say so.
- The ten claims that use the Q-learning model now cite the worst case of the recovery check (RPE r = 0.593, chosen value r = 0.190), not only the median.

**Text corrected**
- **fig5e:** the stale lag values are replaced with the printed ones: 15 lags 1.641 (1.458 to 1.823, 40 mice), 10 lags 2.011 (1.169 to 2.853, 41 mice).
- **fig6f notes:** the angle sectors are fixed. The 103 negative-outcome neurons are those beyond ±90°, 31 + 37 of them from ±135° to 180°. The 87 neurons from −45° to 0° belong to the RPE quadrant.
- **Run time:** the README and cell 0 now say 25 to 36 minutes, 6 to 12 of them loading, depending on the network. The last three runs took 36 minutes each.
- **README:** it now says the waveform change applies the Methods' band-pass filter.

**Recorded:** round 2 is under `verifications`, with the verifier's reasons in its own words and my response for each of the 39 claims. Its cell numbers refer to its own notebook, and the record notes that my two new cells move later cells by two.

**Not done**
- The two possible misreadings of the claims file (iti-mean and fig4c) were already questions in `questions/001950.yaml`, so I added nothing there. Those outcomes could change once a reader answers.
- I did not commit, as instructed.
- The repository root has untracked entries (`.bashrc`, `scripts`, `.idea` and others). They are sandbox mount points created when the run started, not files I made, so I left them alone.
