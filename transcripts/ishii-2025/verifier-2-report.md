**Verifier report, round 2: 001249-ishii-2025-01**

Counts come from the files themselves. The claims file has 27 claims, and the attempt record has 27 outcomes: 7 blocked (too_large), 19 reproduced and 1 partially_reproduced. Of the 19 reproduced, fig6c-decay-length is the only one with `assumed: true`. In the re-executed notebook, cell numbers have moved since round 1.

### 1. Outcomes

I agree with all 27 outcomes.

- **Figure 2, 7 claims, blocked (too_large).** I agree. Cell 3 prints 36.3 MB/s, and cell 78 prints 318 min to stream the TRAP channels and 635 min for both, against a 60-minute limit. The argument in cell 76 holds: every claim corrects over regions that cover the whole brain, so reading only a region would not test it. The missing ilastik classifier is now named as a second reason.
- **Figures 1, 3, 4 and 5, and fig6k (14 claims), reproduced.** Every value in the notes matches cells 9 to 57. For fig6k, the choice of type 1 as the "fast" cluster is better supported than the notebook says. The paper's Results call type 1 the "fast response" type. The Figure 6 legend gives Type 1 as 42 cells (26 Vgat, 16 Vglut2), which is the notebook's cluster 1. The legend's Type 5, which the Results call "negative response", has 46 cells (41/5); that is the notebook's earliest-peak cluster 4.
- **fig6c-decay-length, reproduced, `assumed: true`.** I agree. The assumption is stated in the deviations, the conclusion (cell 55) and a finding, and it is reasonable. The deposited table gives 120 s to all 44 cells whose trace never falls below 0 after the peak, and reading (c) matches the table at r = 1.000. The result is fragile: under the other treatments of those cells it is not significant (p = 0.111 and 0.299), and by animal p = 0.149. The record says all of this.
- **fig7fg-activation-suppresses, partially reproduced.** I agree under the claims file as written: cell 62 gives rank-sum p = 0.0157 for the consummatory group's transitions, so "only post-ejaculatory" fails.
- **fig7kl, fig7s1, fig7s2, fig7s3, reproduced.** Cells 65, 68, 71 and 74 support them. The place-preference p-values hard-coded from the legend in cell 71 match the paper's text exactly (0.2203, 1, 1 / 1, 1, 1 / 1, 0.8472, 0.8472).

### 2. Sentences the printed outputs do not support

All "**Result:**" conclusions, the Summary (cell 80) and the README match the outputs, except for the Figure 2 cost figures. These were carried over from an earlier run:

- **Attempt record, notes of all 7 Figure 2 claims.**
  - Claimed: "measured streaming at 37.0 MB/s in the executed notebook … 312 min … 623 min." Printed: 36.3 MB/s in cell 3, and 318 / 635 min in cell 78.
  - Claimed: "full-width bands of rows stream at 13.2 MB/s." Printed: 12.3 MB/s in cell 77.
  - Claimed: "every 25th (or 10th) background plane … takes 12 (31) min." Printed: 13 and 32 min in cell 77.
- **Finding "kind: other" on the volume sizes.** Claimed: "37 to 56 MB/s … TRAP channels 3.4 to 5.2 h and both channels 6.8 to 10.4 h", and "13.2 MB/s here". Cells 3 and 78 print 5.29 h and 10.58 h, both outside those ranges, and cell 77 prints 12.3 MB/s.
- **Cell 79.** Claimed: "a plane subsample … takes 12 to 31 min." Printed: 13 and 32 min. Its "about 5 h at the 37 MB/s" is close to the printed figure, but 36.3 MB/s is the rate this run measured.

None of these affects an outcome, since every figure is far over 60 minutes.

One sentence is supported but misleading. Cell 58 (and the fig6k notes) say "under that definition Vglut2 cells are not more often fast". The earliest-peak cluster is the paper's negative-response type, not a candidate fast type.

The attempt record restates my round-1 reasons accurately, in substance and with my numbers. The edits are small:
- the fig4h, fig4i, fig6c and fig6k reasons now include the related problems in brackets;
- the fig7s2 reason recasts my "I could not check" in the third person ("It could not check …").

### 3. Status of round-1 points

| # | Point | Status |
|---|---|---|
| 1 | Rank-sum test as the main reading for Figure 7 (fig7fg, fig7kl, fig7s3) | **Open; affects a conclusion.** The attempt kept the claims file's reading and passed the question to a reader, which is correct. I still judge it a misreading of the paper. The legend says "rank sum", but every legend p-value equals the paired signed-rank value, and the design is paired. Under the signed-rank test fig7fg would be reproduced. |
| 2 | Unpaired t-test as the main reading for fig7s1 | Passed to a reader. Does not affect the conclusion (both tests are significant). |
| 3 | 120 s convention in fig6c | Resolved as disclosure (`assumed: true`, with variants shown). **Still bears on the conclusion**: the outcome rests on a convention known only from the deposited table, not from the paper. |
| 4 | Magnitudes for five behaviors come from the deposited table | Resolved; stated in the notes and deviations. |
| 5 | Choice of the fast cluster and the neighbour count in fig6k | Resolved. The code is cited, a variant is shown, and the 55-neighbour result is stated as outside tolerance. The paper's own type labels and counts (section 1) support the choice further. |
| 6 | 0-based index from `elbow_pcs` | Resolved; documented as the code's rule. |
| 7 | Cells treated as units | Resolved. Animal-level tests were added for fig4h, fig4i, fig5 and fig6c. With animals as units, fig4h and fig6c are not significant; the record and README say so. |
| 8 | Figure 2 Figshare zip, grouping and batch effect | Resolved. The zip was opened, 14 of 14 brains match the subject table, the groups match the Stim labels, and the 2024 Mount batch is a finding. |
| C | Things I could not check in round 1 | Mostly resolved. The 12 fig6c cells are tabled, and the place-preference values were checked (and I checked them against the paper). The 60-minute limit is now cited to `docs/protocol.md`, which is not in my materials, so I still cannot verify it. Registration time was not measured, only read time; that does not change the too_large outcome. |

**What still bears on a conclusion:**
- point 1, the fig7fg outcome, which depends on the reader's answer about the test;
- point 3, fig6c's dependence on the 120 s convention, together with its loss of significance by animal;
- the animal-level non-significance in fig4h, which is disclosed, while the outcome follows the paper and the claims file in treating cells as units.
