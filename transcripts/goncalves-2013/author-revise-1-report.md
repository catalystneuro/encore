No outcome changed in this revision. I re-ran the entry with `python tools/entry.py all entries/crcns-ssc-8-goncalves-2013`: 0 errors, and the notebook passes in 307 s. The verifier's round 1 is now recorded under `verifications` in the attempt record. It agreed with every outcome. For each claim the record gives its reason in its own words and what I changed under `response`.

**One label changed.** `suppl4a-firing-vs-correlation` is still blocked, but the reason is now `metadata_insufficient`, not `data_missing`, as the verifier argued: the claim needs no EEG, and the data set does not mark which recordings were in the EEG subset. The notes add that the subset may not be deposited at all.

**What I added or corrected:**
- **"At least one spike" with rates per frame** (problem 1). I added the missing reading (rate ≥ 1) for both shuffles, with new seeds so the earlier readings' numbers do not change.
  - fig2b: still no difference (p = 0.82 and 0.96), so it stays reproduced.
  - fig2c: proportion per event is KO 0.437 against WT 0.391, p = 0.052 (0.053 with the other shuffle). That is close but not significant, and both means are outside tolerance, so it stays not reproduced. The notes say how close it came.
- **Rate unit** (problem 2). A new data check shows the non-zero rates are continuous and do not cluster near multiples of 1 or 3.9. So the data cannot settle the unit. The text now says that reading the rates as Hz rests only on the means matching the paper's values, which is partly circular.
- **fig1ef, Student versus Welch** (problem 3). New cell with the per-mouse P14-16 values and equal-variance tests (Levene p = 0.31, Bartlett 0.39, F-test 0.40), which support Student's t-test. Leaving out one mouse at a time gives p from 0.018 to 0.109. The notes call the outcome fragile: the data set has one WT mouse fewer than the paper, and that alone could move the test across 0.05.
- **fig1d** (problem 4). The four P14-16 mice with pairs over 200 µm have 28, 108, 72 and 1 such pairs. The post hoc test on only the 16 mice that have all three bins gives the same pattern: p = 0.0012, 0.022 and 1.
- **Pooled means** (problem 5). The conclusions and notes for both pooled claims now say the paper's s.e.m. point to the average of the three age means as its method, and that under it both means miss tolerance.
- **suppl4a variant** (problem 6). It now uses only the recordings of exactly 2160 frames (4 WT, 6 KO), and prints the brightness step at each 3-min boundary. It still decides nothing.
- **Handover** (problem 7). The summary was sharing a cell with the variant's conclusion, so the handover tool kept it. It now has its own `## Summary` cell. I also updated the header table, the summary and the README for the suppl4a change.

**Not done:**
- No questions added to `questions/crcns-ssc-8.yaml`: the verifier reported no misreading of the claims file.
- I did not trace which mice differ from the paper's sample, because the data set has no ages or IDs to do it with.
- I did not run the correlation on filtered dF/F, because there are no cell contours to build it from.
- I did not run cross-correlation at its peak lag, because the claims file fixes zero lag.
- Nothing is committed, as instructed.
