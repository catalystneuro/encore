**Verifier report, round 2: Martinez-Conde et al. 2019 on CRCNS pvc-12**

The claims file has 19 claims, and the attempt record has 19 outcomes: 16 tested and 3 blocked. All conclusions below come from the stored outputs of the re-executed notebook. I re-ran nothing on the data. I found no place where the claims file misreads the paper.

### 1. Outcomes

| Claim | Record | Agree? | Assumption stated and reasonable? |
|---|---|---|---|
| neuron-counts | not_reproduced | Yes (cell 20) | – |
| spikes-per-condition | blocked, data_missing | Yes | – |
| s4-baseline-no-difference | not_reproduced, assumed | Yes, but fragile | Stated and reasonable. Each stimulus's baseline placement is the one closest to the files' `BaseActivity` (cell 18). The outcome does not survive the main reading on the 38 files that have `BaseActivity` (smallest p = 0.060), the files' own values (0.109), or the Corners squares 32 DU further in (0.063). So the difference depends on which neurons are included as well as on placement. The record says both. |
| fig4a-above-baseline | reproduced, assumed | Yes | Yes |
| fig4b-spike-rate-difference | partially_reproduced, assumed | Yes. S90 is 8.39 against 10.69 ± 1.94 (cell 29) | Yes |
| fig4b-pairwise-significance | reproduced | Yes. It holds under every baseline reading, so no assumption flag is needed | – |
| fig5-average-maps | reproduced, assumed | Yes. It is not independent of fig4b | Yes |
| table1-edge | reproduced, assumed | Yes (cell 38: 5 of 5 on the 18 files) | Stated and reasonable, since the Methods say the edge was "never" off the display. Only the main baseline is shown on the 18 files. On all 22 files the result is partial (3 of 5), and other placements give 2 or 0. |
| table1-p180 | partially_reproduced, assumed | Yes (4 of 5 under ia) | Yes |
| table1-s90 | not_reproduced, assumed | Yes. At most 2 of 5 under the main baseline | Yes. The main reading on the 9 files with `BaseActivity` gives 5 of 5, and the record says so. |
| table1-s52 | reproduced, assumed | Yes, under (iia) | Stated. The result is fragile: 3 of 5 with the squares centred, 2 of 5 with the files' values, 1 of 5 with the main reading on those 10 neurons, all on 12 of the paper's 30 neurons. |
| table1-s40 | reproduced, assumed | Yes | Yes |
| fig6-midpoint-representative | reproduced | Yes (rank sum p = 0.49 to 0.93) | – |
| fig7a-rms-contrast-fit | not_reproduced | Yes | – |
| fig7c-fold-edge-equivalence | not_reproduced, assumed | Yes, under the stated assumption | Stated. Reading (a) fails clearly: P180 (4.03) is below the whole Edge profile, which runs 9.23 to 21.26. So the outcome rests only on how reading (b) counts "one step": 94.3 is 4.3 from 90, against a step of 3.7, a miss of 0.6. The record calls the distance-from-90 reading "the most literal" (deviation 3). The level-based reading is equally literal and passes. The outcome is borderline, not settled. |
| fig7c-fold-edge-significance | reproduced, assumed | Yes (cell 51) | Yes |
| fig7d-nonlinear | reproduced, assumed | Yes (cell 54) | Yes |
| fig7d-dog-similar | blocked, data_missing | Yes. I accept the author's protocol citation over my round-1 "other" | – |
| s3-latency-peak | blocked, data_missing | Yes | – |

### 2. Text against the printed outputs

I checked every **Result:** conclusion (cells 21, 24, 27, 30, 33, 36, 40, 43, 46, 49, 52, 55), the Summary (cell 58), the README and the record's notes against the outputs. The numbers match, with these exceptions:

- **"`smoothed_image_norm` is missing from 35 of 77 files"** (cell 4, the Summary in cell 58, and the record's second metadata_error finding) is contradicted by cell 3. The field table there gives 39 files without it: Corners 7, Edge 13, Star 1 + 15 + 2 + 1. Only 38 files have it.
- **"holds a baseline-subtracted map in some and a map scaled to -1 to 1 in others"** (cell 58 and the record's finding) has no printed output behind it.
- **"Corners frames come in two sizes (273 x 209 and 257 x 193 DU)"** (fig5 deviation) appears only in a code comment in cell 35. No output prints it.

The `verifications` block states my round-1 reasons accurately, and largely in my own words. Two small omissions:

- In fig7c-fold-edge-equivalence, the reason leaves out my point that the four border-cut Edge files had been kept for that claim too. It appears only under table1-edge.
- In fig7a-rms-contrast-fit, the reason leaves out my point that standard deviation over mean (reading a) cannot rise from 0.61 to 0.943 without a black-level offset.

Neither omission changes the meaning.

### 3. Round-1 points

**Resolved:**

- **B1, baseline placement.** There is now a per-file comparison with `BaseActivity`, an inward sweep of the squares, two more Corners placements and reruns on the 38-file subset. This also exposed a real bug: the centred Square and Edge squares had been read as zeros outside the authors' frame. The fix moved table1-p180 to partial, table1-s90 to not reproduced and table1-s52 to reproduced.
- **B2, the fig7c margin.** It is now stated as an assumption, and the other reading is printed as a variant.
- **B3, the border-cut Edge files.** The Edge measures use the 18 complete files, and all 22 are shown.
- **B5, the three unchecked registrations.** All 60 files now register (cell 12, r ≥ 0.986).
- **B6, the luminance statement.** The text now says the paper gives 14.07 cd/m² at 50%.
- **B7, units.** Cell 10 now shows that 98.5% of pixels hold non-integer values.
- **B8, `box_mean`.** Samples are now symmetric; I read the code and did not re-run it.
- **The cell 31 coincidence.** The printed 1% Edge profile shows a flat stretch (21.18 against 21.01).
- **The stale summary.** The summary cell left in the round-1 notebook is no longer an issue.

**Remaining, bearing on a conclusion:**

- **s4-baseline-no-difference:** the "not reproduced" result disappears on the files that carry `BaseActivity` and with one other Corners placement. No Corners placement matches the authors' values closely (median difference 0.85 to 2.79 spikes/s).
- **fig7c-fold-edge-equivalence:** the outcome turns on a 0.6-point choice between two equally literal readings of "one step". It should be presented as borderline, without calling the distance reading "the most literal".
- **table1-s52 and table1-s90:** both depend on which neurons are included. With the main reading on the files with `BaseActivity`, S52 gets 1 of 5 and S90 gets 5 of 5. Star rests on 12 of 30 neurons, picked by whether the file holds the authors' aligned map (B4 remains, and cannot be fixed with this data).
- **table1-edge:** "reproduced" holds only on the 18 complete files under the main baseline. Other baseline placements are not shown on those 18 files.
- **Corrections to make:** the "35 of 77" count, and the two claims with no printed support (Section 2).
