I went through every point in the round-2 report, re-ran the entry and recorded round 2 under `verifications`. No outcome changed and nothing is under `proposed`. Nothing is committed.

**Outcomes.** None changed. The verifier agreed with 19 of the 21; for `speed-slope-steeper` and `speed-intercept` its agreement depended on a protocol rule it could not see. Both stay blocked because they depend on `speed`, which is blocked. Protocol step 1.5 says such a claim "is blocked for the same reason", so `blocked_by: methods_underspecified` is correct. The notebook, the notes and the README now quote that rule, and the disagreement stays recorded.

**Corrected text:**
- **`gridness-range-similar`:** the sentence "the difference lies among the deeper layers" is replaced. New pairwise tests show it comes mostly from layer III, against layer II (46 of 56 readings) as well as layers V and VI.
- **`deep-hd-conjunctive`:** the variant without rat 11265's files is now computed under chi-square reading (b) too. Under (b) it holds in only 8 of 112 readings, so the readings disagree and the variant would be methods_underspecified, not partially reproduced.
- **`layer2-grid`:** the conclusion now says that under a stricter grid threshold layer III has more grid cells than layer II, so the layer order behind the partial outcome does not survive it.
- **`hd-layers`:** the variant's "0 of 17" now says it rests on 6 layer II cells with plausible tracking (0 of 6 pass).
- **Summary and README:** they no longer claim the count-each-cell-once variant covers every claim; it now does (see below).
- **`hd-tuning-breadth-layers`:** this run gives 43 of 116 Kruskal-Wallis tests finding a difference for each angular measure, where the record said 45.

**Added outputs:**
- The variant with each (rat, depth, hemisphere, name) counted once, for every tested claim except the two that depend on `speed`. No outcome changes under it.
- Outcome lines in the three cells that lacked one.
- The 2.6 to 8.4 cm LED separation in the other 69 two-LED files is now printed.
- **`hd-stable-trials` without the third questionable-LED file:** the tuning-curve reading still reproduces. The circular-correlation reading falls to 0.538 and 0.645 under the first-trial readings, even though the cells dropped are unstable ones. The criterion excludes no file, so this does not decide the outcome, but the conclusion now says that reading is fragile here.
- **Rescaling of the circular files (the verifier's problem 7):** taking the low-speed bin as if the positions were scaled to the paper's 180 cm circle barely changes the 0 to 3 cm/s rates (1.22 to 1.90 Hz for grid cells, for example), and no row comes within 10% of the paper. This needed a small addition to the low-speed rate in `sargolini.py`.

**Counts differ between machines.** On this runner `grid-phase-orientation` holds in every layer under 90 of 224 readings (layer VI 35 and 23 of 56), and the t-test of `conj-tuning-similar` finds a difference in 98 of 112. The verifier saw 88 and 96. The unchanged code from before my edits, run here, gives the same 90 and 98, so my edits are not the cause. These counts rest on p-values near 0.05. I used this run's numbers and noted that the counts vary between machines; no outcome depends on them. I did not find the cause.

**Not done:**
- `entry.py all` still stops at its check step with 18 errors, all on the deprecated `-01` record, which the protocol says stays as it was. No error concerns `-02` or the entry, so I ran the `run` and `handover` steps separately. The notebook passes from a clean environment in 328 s, and the handover is in `executed/000582-sargolini-2006/handover/`.
- The two dependent `speed` claims did not get the count-each-cell-once variant.
- The verifier's own wrong layer VI figure from round 1 is left as it gave it, and the discrepancy is noted in the round-2 entry.
