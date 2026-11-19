I've worked through every point in the round-1 report. The entry re-runs cleanly with `python tools/entry.py all entries/martinez-conde-2019` (0 check errors, notebook passes in about 6 min, 1.1 GB peak memory). Every conclusion, note and measured value matches the final run. Nothing is committed.

**Outcome changes**

| Claim | Before | Now |
|---|---|---|
| table1-p180 | not reproduced | partially reproduced (4 of 5 values within tolerance) |
| table1-s90 | reproduced | not reproduced (at most 2 of 5 under any reading) |
| table1-s52 | partially reproduced | reproduced (5 of 5 under reading (ii)(a)) |

These changes come from a bug I found while revising, plus the new baseline placement:

- **The bug:** the authors' Square and Edge frame is 151 DU wide. Baseline squares centred on the corners of the 141.4 DU circumscribing square run past it, and the helper had read zeros there. Those squares are now read from the screen maps moved into a widened frame, averaged over the part that is on the screen.
- **Effect:** the Square and Edge baseline is higher, so every P180 and S90 value fell. fig4b stays partially reproduced, but the value outside tolerance is now S90 (8.39 against 10.69 ± 1.94) in place of P180 (now 4.03, within).

Round 1 does not bind outcomes, so I changed these three directly. The other 16 outcomes are unchanged, with their numbers recomputed.

**What I added or corrected, by point in the report**

- **B1, baseline placement:** each placement is compared with the files' own `BaseActivity`, file by file, with a scatter plot and with the squares moved inward step by step.
  - Squares centred on the corners match best for Square and Edge (median difference 0.46 spikes/s).
  - Squares inside the corners match best for the Star (0.39).
  - The main reading now takes that per-stimulus match. It is recorded as an assumption, with all placements shown.
  - I added two more Corners placements, plus s4 and Table 1 rerun on the 38 files that have `BaseActivity`.
- **B2, fig7c margin:** "within one step of 90%" is measured as a distance from 90, now stated as an assumption. The verifier's level-based reading is printed as a variant; it passes.
- **B3, cut Edges:** the Edge measures now use the 18 files whose Edge is wholly on the screen, since the Methods say the Edge was never off the display. All 22 are shown. table1-edge is 5 of 5 on the 18 files and 3 of 5 on all 22.
- **B5, failed registrations:** the three Corners failures were a bug in `register_shift`, which read the cross-correlation lag wrongly for large shifts. It is fixed, and all 60 files now register at r ≥ 0.986.
- **B6, fig7a:** the text no longer says the display luminance is absent. It gives 14.07 cd/m² at 50%, but not the black level.
- **B7 and B8:** the units check now prints that 98.5% of pixels with eye time are non-integer. The 7.07 DU S90 blocks are now sampled symmetrically.
- **C, the 0.943 and 90% coincidence:** I printed the Edge profile at 1% steps. The equal values came from a flat stretch of the profile.
- **The handover:** each Result cell had also carried the next claim's heading, so the handover dropped those headings (fig4b-pairwise had none at all) and left the summary in. I split the cells, and the handover now strips the conclusions and the summary.
- **Records:** the attempt record now has a `verifications` block for round 1, with the verifier's reasons and my responses for all 19 claims. I also updated the findings, the entry README and the runtime in `entry.yaml`.

**Not done, and why**

- **B4 (Star rests on 12 of 30 neurons):** this can't be fixed, because 15 Star files lack the authors' aligned frame. It remains a recorded finding and a deviation.
- **fig7d-dog-similar:** I kept it as `data_missing`, not the verifier's `other`. That is the reason the protocol gives for an outside input that is not public.
- **Reader questions:** none added, because the verifier reported no place where the claims file misreads the paper.
