**Verifier report, round 2: Hasnain, Han & Economo 2025 on DANDI:000363 (0.231012.2129)**

The claims file has 19 claims and the attempt record has 19 outcomes: 11 blocked, 3 not reproduced (fig4d ×2, fig4e) plus map-session-selection not reproduced, 3 partially reproduced and 1 reproduced. Cell indices below are 0-based. "nb1" is `reproduce_hasnain_2025.ipynb` and "nb2" is `reproduce_hasnain_2025_g2.ipynb`.

### 1. Outcomes and assumptions

| Claim | Agree? | Assumption |
|---|---|---|
| 11 own-recording claims, blocked (data_missing) | Yes | None needed |
| map-session-selection, not reproduced | Yes. nb1 cell 12: no reading (G1, G2 at 0/20/40 µm, U2) gives both the session and the unit counts | G1 as main reading and 20 µm label transfer: stated and reasonable. The outcome does not depend on either. |
| fig4b-medulla-selectivity, partial | Yes. nb1 cell 17: under E1 the order holds for every seed and both thresholds; every value is outside tolerance | Leaving out ignore, stim, early-lick and other-delay trials, and G1: stated and reasonable |
| fig4c-alm-null-potent-similar, partial | Yes under G1 (cell 20: main p = 0.086 to 0.194, no reading with both means in tolerance) | G1 is stated. See the point on consistency below. |
| fig4c-medulla-null-smaller, reproduced (seed_sensitive) | Yes by the letter of the criterion. G1, B2, V2: 28.40 / 51.88, p = 0.017 (cell 20). Potent is 52.28 under offsets 2000 and 4000, outside the 51.92 bound (cell 22). | G1 + B2 + V2: stated, and the fragility (1 of 15 combinations) is disclosed |
| fig4d-alm-predicts-medulla-null, not reproduced | Yes (cells 30, 31, 33, 35) | Stated |
| fig4d-decoding-asymmetry, not reproduced | Yes | Stated |
| fig4e-medulla-null-lower-dimension, not reproduced | Yes under G1 (cell 25: N1 p = 0.741, N2 p = 0.087) | G1 is stated. See the consistency point. |
| fig4f-medulla-null-not-spanning-alm, partial | I now agree with partial, changing my round-1 not_reproduced. The within-session shuffle (cell 38) answers my session-clumping objection. In every seed, 23 to 33% of ALM units have no medulla neighbour, against 0.1% under the shuffle. Without the d_null = 1 session, 20 of 62 medulla cells lie outside the ALM cells, so the second part of the criterion does not hold robustly. Note that the criterion defines no "partial" level. | Pooling units over sessions: stated |

**Consistency of the readings (affects how the outcomes read).** For fig4c-medulla the attempt applies "under one reading" across 15 G1 combinations to reach reproduced. For fig4c-ALM and fig4e it declines G2, under which both meet their criteria:
- fig4c-ALM under G2 (nb2 cell 10): 34.13 / 42.89, p = 0.251.
- fig4e under G2 (nb2 cell 15): N2 p = 0.0255.

Holding G1 fixed is defensible: G2 brings units with |z| up to 53615 and transferred labels. But the record should say plainly that G1 is held fixed while the M3 to M6 readings are searched. Read the same way for every claim, fig4c-ALM would be reproduced and fig4e reproduced under N2. I do not ask for a change, only for the asymmetry to be stated in the README and the record.

### 2. Sentences the printed outputs do not support

**nb1 cell 36 (fig4d), and the same numbers in the record's notes and responses:**
- ALM to ALM "−6098.6 to −2191.3%". Cell 30 shows −6039.6 to −2188.1.
- Median ALM to medulla "−364.9 to −178.8%". Cell 33 shows −364.05 to −178.77.
- Span "−320.8 to −120.3%". Cell 33 shows −320.48 to −120.27.
- example.m "−1828.9 to −1512.9%". Cell 33 shows −1829.17 to −1512.92.
- Medulla to ALM "−517.9 to −290.4%". Cell 30 shows −517.84 to −287.97.
- λ = 100 asymmetry "6.2 points (p = 0.091)". Cell 35 shows 6.17, p = 0.0943. The record's response claims this text "now matches the output".

**nb1 cell 39 (fig4f), and the record's notes and response.** This is a different run from the output in cell 38:

| Text | Cell 38 output |
|---|---|
| 25.7% of ALM units with no medulla neighbour | 33.3% |
| "21.3 to 27.3% over the five seeds" | 23.3 to 33.3% |
| "6 of the 26" ALM grid cells hold no medulla unit | 3 of 28 |
| "0 of 20" medulla cells outside the ALM cells | 2 of 27 |
| 59.4% of medulla units have an ALM neighbour | 57.4% |
| "58.2 to 62.6%" over seeds | 57.4 to 65.9% |
| "spread 9.75, against 2.3 to 4.7" | 7.62, against 2.40 to 4.53 |
| Without the session: "21.0%", "16 of 57", "26 of 67" | 20.1%, 20 of 62, 20 of 62 |

**nb2 cell 11 (fig4c under G2), and the record's notes for fig4c-medulla and fig4c-ALM:**
- ALM: "V1 p = 0.050" (output 0.0488); B2 "V2 p = 0.041" (0.0427); "0.249 to 0.261 over the seeds" (cell 13: 0.251 to 0.266).
- Medulla, main reading: "V1 46.3 against 67.3%, p = 0.020" (44.96 / 67.86, p = 0.0064); "V2 35.7 against 51.7%, p = 0.027" (35.43 / 52.26, p = 0.017).
- Medulla, seeds: "V1 and V2 p 0.008 to 0.027" (0.0048 to 0.0176).
- Medulla, B2: "V2 30.8 against 56.4%, p = 0.005" (31.28 / 55.99, p = 0.0065).
- "95.7%" (95.8).

**nb2 cell 16 (fig4e under G2), and the record:**
- "N1 medulla 10.9, ALM 10.9, p = 0.98; 0.86 to 1.00 over the seeds; under B2 p = 0.876". The output gives 11.21 / 11.42, p = 0.925; 0.80 to 0.98 over seeds; B2 p = 0.699.
- "N2 3.35 against 5.93, p = 0.027" (3.37 / 5.96, p = 0.0255); "B2 3.72 against 6.92, p = 0.018" (3.74 / 6.91, p = 0.0193).
- The nb2 summary's "N2 (p = 0.027), N1 (p = 0.98)" is wrong in the same way.

**nb2 cell 19 (fig4d under G2), and the record:**
- "p = 0.15 to 0.46 under the claim's seed and 0.17 to 0.87 over the other seeds". Cell 18 shows 0.197 to 0.441 and 0.228 to 0.987.

**Other places:**
- Record findings, clocks: "tongue becomes visible a median 56 to 271 ms". Both notebooks show 56 to 262 ms (nb1 cell 9, nb2 cell 3).
- nb1 cell 11 markdown says U2 "cannot place units in the CCF … its nearest form, all units on the region's probe, is shown". Cells 6, 12 and 13 form U2 by label transfer, so this text is stale.
- README run times, "about 30 minutes" and "About 35 minutes": the notebooks print 2455 s (about 41 min, nb1 cell 38) and 3115 s (about 52 min, nb2 cell 18).

None of these mismatches changes an outcome. They show that the text of nb1 cells 36 and 39, nb2 cells 11, 16 and 19, and the matching parts of the record were written from an earlier execution than the one deposited.

**Everything else checks.** The other sentences of nb1 cells 13, 18, 23, 26 and 40, nb2 cell 6, the README table, and the notes for map-session-selection, fig4b, fig4c (G1 parts) and fig4e (G1 parts) agree with the outputs.

**My round-1 reasons in the record.** They are stated in my words, with one inaccuracy. The `reviewed` field says I saw the notebook "with the conclusion cells and the summary removed". My round-1 report says cells 21 and 31 still held the author's result text.

### 3. Round-1 points

| Point | Status |
|---|---|
| B1, selection | Resolved as a check: the electrodes table has CCF x, y, z; labels transferred, 97.3% agree; G2 run. What remains is the G1/G2 asymmetry in section 1. |
| B2, decoding | Resolved: the example.m z-score, span R2, median, per-bin and per-epoch variance were all run, and the cause was traced to predictors per training trial. What remains is the text mismatches in section 2. |
| B3, UMAP | Resolved: within-session shuffle, by-session extents, and a run without the d_null = 1 session. What remains is that cell 39 and the record misreport cell 38. |
| B4, readings | Resolved as disclosure (notes and the seed_sensitive flag) |
| B5, selectivity | Resolved: the block shuffle gives 30.3 / 47.9 / 85.9% |
| B6, text against output | Not resolved. New and larger mismatches, listed in section 2. |
| B7, B8, B9 | Resolved or stated. Untracked bins are at most 0.1% (cell 15). |
| Section C items | Trial labels (N/A is the only no-stim label), moving bins per epoch and the sample-cue time are now printed. The last of these found the 446 other-delay trials, which are now excluded. |

What still bears on a conclusion:
1. The fig4f numbers in nb1 cell 39 and the record are wrong. The partial outcome holds on the real output, but the judgment must be restated from cell 38.
2. The G2 numbers in nb2 and the record must be restated from nb2's outputs. The G2 verdicts do not change.
3. The G1/G2 asymmetry in applying "under one reading" (section 1) should be stated.

### 4. Critical findings

No finding in the attempt record is rated `critical`, and I would rate none of them critical. Nothing shows wrong data:
- Clocks agree (nb1 cell 9).
- The units match across versions (nb1 cell 5).
- The other-delay trials and the missing CCF labels are evident from the files.

The existing ratings are reasonable: selection is major, and the other metadata findings are minor.
