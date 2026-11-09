The verifier agreed with all 22 outcomes in round 2, and none changed. The 22 outcomes are 1 partially reproduced, 4 not reproduced and 17 blocked. Nothing is proposed for round 3. The entry re-ran cleanly with `python tools/entry.py all entries/000489-kim-2022` (passed in 559 s), every number is the same as before, and `entry.py check` reports 0 errors.

**Corrected**
- **fig2c-max-inhibition-50-75:** the conclusion (cell 27) and the record notes gave the "largest p at every ROI" sentence for 50% only. They now give it for both amplitudes: for 50%, 0.79 against unipolar and 0.072 against 25 and 100%; for 75%, 0.996 and 0.249.
- **fig4ac-ns-bipolar-20-25pct:** the Summary (cell 37) and the notes said the polynomial fits cross zero. That holds only at the 7 kV/cm cutoff (minimum −457.4%); at 8 kV/cm the ratio runs from 34.8 to 1537.4%. Both are now stated.
- **Cell 7:** removed the out-of-date mention of a "with 0-03" variant that no longer exists.
- **Cell 0:** the status table now shows fig2c-weaker-at-6-7 as analysed and blocked (other), no longer "tested".
- **Round-1 record:** the verifier noted that two of its round-1 points were missing from the claim reasons. Its problem 2 (dropping dish 0-03 leaves 2 unipolar dishes, and the invalid variant) and problem 11 (imaging dates confound amplitude) are now in fig2a's round-1 reason, in the verifier's words. The round-1 response now says what was done about them.
- **Round 2** is recorded under `verifications` for all 22 claims, with the verifier's reasons and my responses.

**Not done, and why**
- **The third unipolar dish:** dish 0-03's real image, which is in dandiset 000548, was not measured. Author step 1.4 allows outside data only where the claims file says the paper relies on it, and the claims file names no outside source for Fig. 2. The three Fig. 2C claims and fig2a therefore still rest on 2 unipolar dishes. The notes say so, and the existing finding says where the image is.
- **Two remaining judgement points:** where the p < 0.01 test of fig2c-max applies, and treating camera counts as the paper's units. Both stay stated assumptions, with every reading shown.
- **Questions file:** no question was added to `questions/000489.yaml`, because the verifier reported no misreading of the paper in the claims file.

Nothing is committed; the workflow commits the changes.
