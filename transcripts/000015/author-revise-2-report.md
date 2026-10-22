I made no changes to outcomes. All 33 stay as verified (13 reproduced, 3 partially reproduced, 7 not reproduced, 10 blocked), and nothing is proposed under `proposed`. The verifier agreed with all 33. I re-ran `python tools/entry.py all entries/000015-chen-2017` and it passed in 20.4 min. Every number came out the same as in the copy the verifier saw. `entry.py check` reports 0 errors.

**Corrected or added, per point of the report:**
- **fraction-selective-alm-mm:** window W3 is the closest reading, not W1 (ALM 2,853, 32.3%; MM 1,736, 26.3%). Cell 30 now gives W3 first and W1 next. It also drops the false sentence "no other reading comes closer" under V2 and gives the V2 values for both windows. `measured` in the attempt record is now the W3 values, and the notes say why.
- **fig8d-pt-earlier-than-it:** the README row and the Summary text now name all three conditions it needs: rule S2, T2 bins and the bootstrap over cells.
- **Summary, fig6-lick-direction-spread:** the ALM peak is now given as at most 6.2% with T1 bins and 6.5% with T2.
- **fig8d-mm-object-location:**
  - Cell 77 now prints the value the ALM deep maximum would need to exceed for part (c) to pass for MM PT: 1.047, against 0.112 for ALM PT.
  - Its per-animal label is fixed. It now shows that 45 of the 47 MM PT ROIs with a baseline at or below zero are in mouse an064.
  - Cell 78, the Summary row and the notes now say part (c) looks unlikely to hold for PT.
- **Silicon probe data ("never made public"):** cell 14 now searches DANDI by the paper's DOI and by its authors, and finds only dandiset 000015. The README and the notebook header and Summary now say the data are "not public (placeholder DOI, not on DANDI)". The notes say the CRCNS search was done only while preparing and is not run in the notebook.
- **README runtime:** changed from "about fifteen minutes" to "about twenty".
- **Attempt record:** round 2 is recorded under `verifications` with all 33 claims, each with the verifier's reason and my response. The header comment now mentions round 2.

**Not done, and why:**
- **figs4-peak-shift:** the verifier says the claims file misreads the paper, and that the outcome would become reproduced if the peak were taken before the go cue. I proposed no change, because the criterion decides and the question about that window in `questions/000015.yaml` is still unanswered. The notebook already shows the peak before the go cue.
- **The dF/F outlier sensitivity** of fig8d-pt-contra-bias and fig8d-error-outnumber-correct needed no action. The reader's answer makes V1 (dF/F as computed) decide, and the V2 values are already reported as a check.
- **The verifier's round-1 reasons** still cite round-1 cell numbers. I left them as the verifier gave them.
- **Executed copy:** I changed the markdown cells after the run, so the executed copy (git-ignored) still shows the old conclusion text. The new code outputs are in it, and the numbers are unchanged.
- **Commits:** I committed nothing, as instructed.
