No outcome changed. All 25 stay as verified in round 2, and nothing was proposed for a third round. I re-ran the entry twice with `python tools/entry.py all entries/000055-peterson-2021`. Both runs passed the checks with 0 errors and printed the same numbers as before; the full run takes about 41 min.

**Added or corrected, point by point:**
- **Overlap with the paper's own R2 (fig6b-d).** I added the two outputs the verifier asked for in a new cell, with refits for the 12 electrodes it needed. The electrodes above R2 0.05 here and those above 0.05 by the R2 stored in the files share 18 in LFB (22 here, 23 stored) and 12 in HFB (14 here, 22 stored).
  - With the stored selection, the fig6b-d results still hold. 22 of 23 LFB and 18 of 22 HFB electrodes are frontoparietal, angle and day have the two largest median Delta R2 in both bands, and the median angle coefficient is -1.026 in LFB and +0.498 in HFB. Angle and the day SD remain the two largest coefficient values.
  - These are recorded in the notes as a sensitivity check, not the criterion.
- **Day coefficient definition.** The record now states it is the mean over splits of the per-split SD. The helper and notebook also print the other definition, the SD of the split-averaged coefficients: 0.658 against 0.660 in LFB and 0.729 against 0.733 in HFB, with the same top two.
- **False positives in the ECoG claims.** The fig3 claim has a new deviation saying the events include the paper's false positives, and every ECoG claim that refers to fig3 carries it. The summary and README now say this too.
- **Cell 59 and the fig3 notes.** They now name middle temporal (-0.005 and +0.003 dB). They also say that at the onset bin, supramarginal's high-frequency value and middle temporal's low-frequency value are 0.000. The verifier only flagged supramarginal; the new run shows middle temporal is also 0.000 there.
- **Run-time wording.** The ECoG step took 34.6 and 35.4 min in these runs, against 19.8 min before, so no single figure is right. Cell 0 now says 20 to 35 minutes, and the README says 30 to 45 minutes for the whole notebook.
- **Round 2 record.** It is under `verifications` with all 25 claims marked as agreed, the verifier's reasons, and my responses.

**Not done:**
- I added no question to `questions/000055.yaml`, because the report names no place where the claims file misreads the paper.
- I made no changes for the points the verifier listed as disclosed and not bearing on outcomes: fig2-event-counts reading b, the fig4 tie-break and the fig2 KDE criterion.
- The unrelated edits already in the working tree under `tools/` were left untouched.
- Nothing was committed, as instructed.
