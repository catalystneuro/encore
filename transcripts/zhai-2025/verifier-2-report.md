**Verifier report, round 2: Zhai et al. 2025 on DANDI:001538 (0.261124.1858)**

**1. Outcomes**

The claims file has 45 claims: 5 links and 40 findings. The attempt record has 45 outcomes: 6 blocked, 3 not reproduced, 2 partially reproduced and 34 reproduced.

- **I agree with all 45 outcomes.** That includes fig4h-ispn-sr-frequency-unchanged as reproduced, where I disagreed in round 1.
  - The claims file gives no criterion for fig4h beyond the paper's test, under which this claim of absence holds when P ≥ 0.05.
  - The new runs of 10 sweeps give P = 0.064 with the last 10 and with the "nearest run" (cell 77). The every-sweep result is also 0.064, the smoothed-noise variant 0.118 and the paper's own table 0.23.
  - Only the first 10 sweeps give 0.049. So the outcome stands, but it is fragile.
- **The `assumed: true` flags are stated** (link-sr-cells, fig2h, fig2i, fig4g, fig4h).
  - The stand-in detector is a reasonable assumption for the amplitude claims. They hold under both noise variants and on the paper's table (cells 68 and 74).
  - The fig4h "nearest run" assumption is stated but weakly supported. For 2023-04-06 cell 1 the two possible runs give 93 and 89 events against the paper's 73 (cell 66). Both are about 22 to 27% too high, so the choice rests on a 4-event difference from a stand-in detector. It only matters against the first-10 reading.
- **Blocked claims.** I accept `not_runnable` for the five 2PLSM spine claims and for fig4k, for the reason the record gives. In round 1 I had said other and data_missing.
- **Claims-file readings to report:**
  - link-grab-rois treats the mouse as the unit, but the paper's unit is the region. This is still open.
  - link-dendritic-cells defines the Figure 6D letter as the cell's place in the day. Cell 42 shows the letter is the file's cell number: 16 of 16 identifiers match that way, against 14 of 16 by place.
  - link-dendritic-cells also says the row-order assumption is "checked by the somatic link, where rows follow that order". The somatic link uses best matches, not row order, and 9 paper rows are reused (cell 11). Cell 42 also shows two off-state iSPNs that look swapped. So that premise is not established.
  - link-sr-cells names `lid.detect_events`, which is not this attempt's helper.

**2. Sentences the outputs do not support**

- **Summary, cell 134:** "Seven claims rest on the paper's own tables." The claims file has 8 claims with `data: elsewhere`, and the README and cell 107 list 8.
- **Attempt record, finding 6 (GRAB):** "seven regions have an acetylcholine trial that ends before 4 s". Cell 82 shows 6. The seventh row listed, 2024-05-24 Slice1Roi1, is there only because it has no tetrodotoxin trial; its acetylcholine trials last 4.6 and 5.2 s.
- **link-somatic-cells notes:** "18 cells differ by more than 3 spikes, most of them on-state dSPNs … and sulpiride iSPNs". Cell 11 shows 9 of the 18 (6 on-state dSPNs and 3 sulpiride iSPNs), which is half, not most.
- **fig4h notes and cell 78:** the nearest-run reading is "the one the paper's own per-cell counts support". Cell 66 does not show this, for the reason given in section 1.
- **Somatic deviation, repeated in many outcomes:** "so every somatic result is the same under it". The last-sweep variant is only re-run for the rheobase tests of fig1f and fig3d (cells 15 and 24). The changed cell, 2020-02-17 cell 1 (170 to 171 spikes), belongs to the fig6c summed-spikes variant in cell 33, which is not re-run. A change of 1 spike is very unlikely to change anything, but it is not shown.
- **README:** the row "Sr2+-oEPSC … (four claims) | Reproduced, resting on a stand-in event detector" leaves out that fig4h also depends on which sweeps are used. The Summary (cell 134) does state this.
- **Checked and supported:** every other "**Result:" sentence and the rest of the README and attempt-record notes match the printed outputs. This includes the paper-quoted P values (0.0115, 0.0029, 0.0545, 0.012, 0.395, 0.910, 0.5566, 29.30, 0.6340/0.4657, "four mice"), which I checked against `paper/`.
- **My round-1 reasons** are stated faithfully in the record's `verifications`, in my own terms. For fig4h it records `agrees: false` with my reason.

**3. Round-1 points**

- **Resolved:**
  - 1: the red background is now 55 (`zhai.py:193`, 248–249).
  - 2: `keep="last"` now works (`zhai.py:171-176`). Cell 11 shows one cell's total changes, so the variant is no longer a no-op.
  - 4: the wording of the fig1i exclusion variant (cells 49 and 50).
  - 5: reused rows, ties and the agreement between the rheobase and F-I sheet rows (115 of 124) are now reported in cell 11.
  - 6: the one-to-one (15 of 34) and per-mouse (1 of 11) counts are in cell 80.
  - 7: the frame interval is now checked (cell 82). The 2024-04-02 Slice1Roi2 discrepancy is recorded as a finding.
  - 8: cell 102. 9: cell 122. 10: cell 42. 13: cell 9.
  - 11: the stand-in detector is now stated as an assumption.
- **Still bearing on a conclusion:**
  - Point 3: fig4h is reproduced, but sits at the threshold (0.049 against 0.064) depending on one sweep of one cell. The justification for the reading it uses is overstated.
  - Point 12 and the link-dendritic premise above: the claims-file readings. Neither changes an outcome as computed.
  - fig1i-dspn-dendritic-sch-lower is not reproduced because the 2019-04-11 pair is missing from the data (P = 0.066 with the cell, 0.027 without it). That is correctly attributed to the data.

**4. Critical findings**

No finding in the attempt record is rated `critical`. Of the 8 findings, 3 are major, 3 minor, and the 2 `methods_unavailable` findings carry no severity. I would rate none of them critical:
- Each data problem is stated in the dandiset description or is visible from the values: the missing groups, the Figure 8 preprint sheets, the missing 2019-04-11 pair, and the extra Sr2+ sweeps.
- None amounts to duplicated or mislabelled recordings or a clock problem. Cell 7 shows no duplicated somatic cells, dendritic pairs, Sr2+ cells, GRAB regions or AIM mice, and cell 6 passes all the clock checks.
- Finding 6 is correctly rated minor, but its count of short acetylcholine trials should be 6, not 7 (cell 82).
