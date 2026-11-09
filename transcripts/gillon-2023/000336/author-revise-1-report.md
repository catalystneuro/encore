No outcome changed: the verifier agreed with all 18 in round 1, and the re-run gives the same results. `python tools/entry.py all entries/000336-gillon-2023` passes. The main notebook ran in 712 s and the matching notebook in 780 s. `tools/entry.py check` reports 0 errors.

**What I added or corrected, by report point**
- **B1, SNR noise floor:** I added a pure-noise control. Gaussian noise alone scores an SNR of 2.06 (1.56 and 2.56 when the median sits 0.5 SD below or above). I also compute each ROI's own noise floor. Every group's median SNR is 0.31 to 1.37 above that floor. fig7a stays reproduced, as its criterion requires, and its notes now say that "SNR above 1" would also hold for noise.
- **C1, match to the paper's code:** the helper's SNR, rolling mean and correlations now run side by side with the paper's own `calculate_snr` and `rolling_mean`, taken from `colleenjg/util` at commit 2b05f954, on every ROI of two sessions. They agree to rounding. I listed that repository under `inputs`.
- **B2, B3 and C2, ROI matching (fig8-ordering-variation):**
  - The shortcut that combines pairwise matchings gives the same count as the package's own `NwayMatching.run` in all 12 orderings checked (two mice, six orderings each). The package's summary plots fail with the locked pandas, so they are skipped. They do not affect the matches.
  - A new per-mouse table counts three-session matches containing a pair of ROIs with no direct pairwise match: 19 to 307 per dendritic mouse.
  - A variant that applies the overlap threshold only to directly matched pairs keeps 5 to 28 more matches per mouse. The outcome is the same.
  - The overlap threshold read as intersection over union, not the linking rule, removes most matches. Dendritic counts stay well below the tracked counts in the files.
  - This run's dendritic counts differ slightly from the run the verifier read (433414: 18 to 22, against 18 to 21). The record says so.
- **B4, Fig. 5:** I added a Gabor ROI selection based on inconsistent sequences, as the Fig. 5b legend can be read. Under it, Gabor shows a difference only in L5-S, but every plane keeps a flow difference, so the outcome holds. Selected ROI counts and thresholds are now printed per session.
- **B5, stimulus blocks:** block counts are now printed per session. 2 of 33 sessions fall outside 27 to 33 for Gabor and 11 for flow; the criterion judges the session mean. The 0.387 s run is an 88.9 s consistent Gabor run in session 832883243. All 22 runs more than 0.25 s off their sampling grid are in the three sessions where runs overshoot their grid durations most. That fits a display running slightly slow there.
- **B6, Fig. 9:** I added `questions/000336.yaml`, asking a reader whether the claim should be judged on Gabor events alone, as the legends show it. The claim stays as the claims file has it. Its notes say the question is open and that on the Gabor-only variant it would not be reproduced.
- **B7, high-correlation pairs:** the fraction is now given by mouse (413663: 0.032%, 433414: 0.0030%) and with each mouse left out. Both stay outside the tolerance.
- **B8, the two unopened 000336 subjects:** all 16 subjects are now opened, using a raw file for the two that have no processed file. Their sessions run to 2023-11-15.
- **C3, the 433414 depths:** the raw location strings say depth '60', so 60 µm is the value in the files, not a parsing error.
- **C4, the code table:** `mouse_df.csv` is printed beside Table 2. It agrees on QC, date, depth, ROI count and tracked count in 50 of 50 sessions, and its session numbers run in date order within each mouse.

I updated the conclusion cells, the summary, the README runtime and the attempt notes and deviations. Round 1 is recorded under `verifications`, with the verifier's reasons and my responses.

**Not done**
- The dendritic overlap is still read as intersection over union. The package reports no overlap relative to the smaller ROI, so I could not run that reading. It remains a question for the paper's authors.
- The Fig. 9 question is left for a reader, as the protocol says. Its passage is the text and legend shown above.

Nothing is committed.
