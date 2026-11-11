**Verifier report, round 3: Park, Wong-Campos et al. 2025 on DANDI:001266 (0.250710.0758)**

The claims file has 55 claims and the attempt record has 55 outcomes: 8 reproduced, 14 not_reproduced and 33 blocked. Only one outcome carries a `proposed` change: fig3d-distal-first-bap. Cells are cited as [n] for `reproduce_park_2025.ipynb`.

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| fig3d-distal-first-bap | blocked (methods_underspecified) | Yes | — | See below. |

**Reason for fig3d-distal-first-bap**

- **The numbers come from the data.** The selection table [42] uses the same per-reading calls as the count table [13] and the per-bAP-position table [41], and the three tables agree.
  - File D4 has 84 bAPs at 5 s.d. under both filters and both regions. At 4 s.d. it has 88 with the median filter and 85 with the Butterworth.
  - At 5 s.d. and beyond 300 µm, the first bAP carries a dSpike in 32 of 54 trials with the median filter and 31 of 54 with the Butterworth [41, rows 16 and 20; 42, rows 0 and 4].
  - Against 35 ± 3.5, 32 is inside (|32−35| = 3) and 31 is outside (|31−35| = 4).
  - File D2 gives 0 to 3 under every reading, and none of its totals (105 to 110) matches 84.
- **The choice was not made to reach the result.** The proposal moves to the claims file's standard choices: 5 robust s.d. (header, item 4) and the region beyond 300 µm (shared method).
  - It drops the 4 s.d. deviation, which was what gave a pass under both filters (33 and 32).
  - It does not adopt the 300–400 µm variant, where both filters pass (33 and 33).
  - So the change goes against the author's interest, not towards it.
- **The criterion is applied as written.**
  - The claims file's choices (5 s.d., beyond 300 µm) give exactly the legend's 84 bAPs in file D4, so D4 is the reading whose totals match, as the criterion requires.
  - The filter is an open method detail with two readings. The header's Readings rule says the outcome is methods_underspecified when those readings give different outcomes, and here they do (32 passes, 31 fails).
  - The proposal's argument for setting aside 4 s.d. also holds. In [13] and [41], 4 s.d. matches the legend's totals in none of the three files: 85 to 88 against 84 here, 161 to 165 against 167 in the soma file, and 167 against 170 in D4+soma.
- **A caveat that does not change my agreement.** The Butterworth fail is one trial past the tolerance. It rests on the author's own rule for the dSpike threshold (the first density trough), which I noted in round 2 (B1) does not always follow its stated rule. A slightly different trough could move the count by one, so the result is close to the boundary either way. That supports "underspecified" rather than either a pass or a fail.

**Where the claims file may misread the paper (reported, not corrected)**

- The header, item 4, says the somatic threshold "cannot change the outcome" because Fig. S2 reports perfect somatic detection. In this recording it does change it: 4 s.d. passes under both filters, 5 s.d. splits them [41, 42]. The paper set its thresholds by hand, so this assurance is the claims file's inference, not the paper's. The attempt record says the question has been put to a reader.
- The fig3d criterion's phrase "the reading whose total counts match the legend" refers, through source-data-index, to choosing between file D2 and file D4. The author has stretched it to choose the somatic threshold too. Here this makes no difference, because 5 s.d. is the claims file's standard choice anyway.
