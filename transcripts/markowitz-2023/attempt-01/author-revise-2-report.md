No outcome changed and none is proposed for a round 3. The verifier agreed with all 24 outcomes, and the final run passes `entry.py check`. It took 13.3 min, and every claim's numbers came out the same as in round 2.

**What I added or corrected**
- **README run time:** now about 13 minutes, about 4 of them streaming 1,729 files. The run prints 13.3 min and 73 s plus 146 s of streaming. The new data check reads 6 extra files, so the count went up from 1,723.
- **dLight+ChrimsonR sessions and the 635-nm stimulator:** the notebook now also loads the 6 dLight+ChrimsonR closed-loop files that have no dLight series. Cell 6 prints all 236 of those mice's closed-loop files (8 mice). The 88 with stimulation all use 250-ms pulses, and all 236 state 635 nm, so the "only 250-ms sessions" and "every closed-loop file states 635 nm" statements now have printed support. Their wording did not change.
- **Rotated clocks:** `spontda.py` now records, for each file, the non-ascending steps, the largest backward step, repeated timestamps and the frame interval after sorting, and cells 5 and 6 print them. This showed the finding was not exact:
  - 573 of the 575 files have one backward step, at least 0.95 of the session length in 558 of them.
  - Two closed-loop files of mouse 3155 store every frame twice and have 2 and 3 steps.

  I corrected the format_error finding and the Summary, and added a second format_error finding for the duplicated frames.
- **Cell 38 wording:** "Ranking by the log2 fold change gives 10" now reads "Counting mice above the control maximum of the log2 fold change gives 10", in both the cell and the notes.
- **ed7-dms-no-usage-prediction:** the notes and cell 31 now say three things:
  - Extended Data Fig. 7 has no lagged future-usage test; it rests on the encoding model and the panel title. I checked this against the paper text, saved as `paper/markowitz-2023-nature.txt`, which is gitignored.
  - This attempt's DMS across-syllable count test agrees with the paper (r = 0.026, P = 0.170).
  - This attempt's lagged test probably differs from the paper's version.
- **Round 2 record:** added under `verifications` with all 24 claims and the verifier's reasons in its own words. The verifier's points about text outside the claim sections had no claim of their own, so I recorded them under fig1e-velocity-timescales.

**Not done**
- The causes of the fig1h H gap (266.40 against 209.29) and of 7 learners against 9 are still unknown. The verifier listed both as remaining but asked for no new output, and the notes already say the cause is not found.
- I did not show in the notebook that the duplicated frames of mouse 3155 carry identical labels. A check I ran outside the notebook found they do, so onset counts should be unaffected, but the record does not rely on that check.

I made no commits, as instructed.
