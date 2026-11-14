**Verifier report, round 2: scholl-2015-01 (Scholl et al. 2015 on CRCNS pvc-10)**

Counts are taken from the claims file and the attempt record. There are 25 claims, all with an outcome: 7 blocked (data_missing), 6 reproduced, 4 partially reproduced and 8 not reproduced. Nine outcomes carry `assumed: true`. Since round 1, 18 claims are tested on the structs in `original/to_remove/`: mice 8 to 10, plus the PV+ cells of mouse 7 for Figure 3.

**1. Outcomes and assumptions**

I agree with these 18 outcomes.

- The 7 blocked claims: fig1e, cell-counts-responsive, figs3, figs5 and the three CaMKIIa claims. The new reason for cell-counts-responsive is supported: all 157 PV+ cells in the structs pass the binocular index (cell 20). The figs3 and figs5 reasons are also supported: neuropilpeaks is the same for every cell of a plane (cell 18).
- fig3abc-pv-more-binocular-fraction, fig3c-contralateral-bias, mi-per-animal (3 animals), fig3def-pv-weaker-disparity-selectivity, fig4ag-salt-and-pepper, pv-larger-dff-low-dsi, fig4f-od-length-constant, figs4-same-plane-control, fig4i, fig4k and fig4jk.
- figs6cd-pvminus-pv-like-disparity. This one rests on population reading (a) and on 9a. The record states both as assumptions, and other readings are significant (cell 77).
- The fig3def assumption does no work. Every cell set in the main pool gives the partial case (cell 42), so `assumed` could be dropped.

I disagree with, or cannot confirm, these five:

- **fig4d-pv-od-matches-local-50um: partially reproduced.** The criterion has no partial case. Two of its three conditions fail under every reading:
  - 18 PV+ cells against 86 ± 8.6.
  - The one-sided shuffle p is 0.015, against the required p < 0.01 (cell 56).

  By the criterion this is not reproduced. The record admits there is no partial case and assigns one anyway.
- **fig4f-pv-od-spatial-decay: not reproduced.** The partial case ("only the 50 um slope is significant") is met under claims-file reading 7b with axis 1b (cell 56):
  - 50 µm: slope 1.42 ± 1.94, p1 = 0.003, the largest slope.
  - 75 to 150 µm: p1 from 0.478 to 0.996.

  Cell 58 and the record check only the full pattern ("No reading shown gives the pattern"). The partial case needs to be addressed. With an SE of 1.94, that 50 µm value is fragile.
- **fig4ef-pvminus-od-unrelated: partially reproduced, stated basis not supported.** The partial case rests on the absence of significance under axis 1a.
  - Under 1a the PV- slopes are unusable: 6.70 ± 6.19 up to 2.39 ± 419.80. A major-axis slope taken on its near-vertical orientation gives bootstrap means dominated by outliers.
  - The Summary itself says 1b "gives slopes of the size the paper reports" (cell 79).
  - Under main 1b, 100 µm is significant (p1 = 0.002), so the absence fails (cell 61).
  - The outcome could still stand on reading 3b with 1b: 50 µm 0.09 ± 0.04 (within tolerance), p1 = 0.013, and no other radius below 0.01. The record does not make that argument.
- **figs6ab-pvminus-pv-like-od: reproduced, rests on an unstated second choice.**
  - For unrestricted populations (a), 1a is the stable orientation, and no p2 falls below 0.10. That part holds.
  - The record says restricted populations (b) also pass (p2 0.778 to 0.757). Those values come from 1a, where the SEs run from 4.29 to 308.
  - In the stable orientation for (b), 1b, the main reading gives p2 = 0.036 at 100 µm and 0.019 at 125 µm (cell 64).
  - So the outcome also rests on population reading (a). The record should state that as an assumption, as it does for figs6cd.
- **fig3-pv-lower-monocularity (partial) and mi-dsi-relation (not reproduced).** Both are judged on the L cell set alone. Under N, the attempt's version of the Methods' criterion, the outcomes would be higher:
  - fig3-pv-lower-monocularity: N with monocular cells, which is claims-file reading (b), puts all four values within tolerance with p = 0.0092. That is reproduced.
  - mi-dsi-relation: N with joint cells meets the partial case (PV+ slope 0.059, PV- 0.151; cells 32, 45).

  The record reports both numbers but does not say why the main reading alone decides when the criteria say "under one reading". Reading (b) cannot be expressed under L at all, because L gives the same cells for joint and mono.

The assumption that the binocmonocinds lists are the responsive cells is stated and is reasonable as a working choice. Its stated support is overstated in two places (cell 29, record deviations):

- "Nearly all their cells pass the joint criterion": the counts in cell 20 sum to 235 of 270, and to 158 of 189 for PV-.
- The 769 PV- total is called "near" the paper's 944. It is 19% lower, outside the claims file's 10% tolerance.

The other basis the record states, blank-subtracted ODI with negatives set to zero, decides fig3abc: without blank subtraction the PV+ fractions fall to 35.8 to 50.0%. That choice is stated as a deviation and is reasonable given cell 18.

**2. Text against outputs**

These sentences are not supported by the printed numbers:

- **Cell 18 (fixed print text):** "the stored DSI is the Methods' vector strength of the blank-subtracted responses, taken as measured". The same cell prints a match for 578 of 578 cells with negatives set to zero, and 399 of 578 taken as measured. The per-struct "dsi differs" counts use the wrong reference.
- **Cell 41:** "(a) as measured (the stored DSI)". Same contradiction. Cell 29 and the record have it right.
- **Cell 65 and the record:** "or restricted to the same ODI range (0.778, 0.288, 0.974, 0.417, 0.757)". These come from the unstable orientation; see section 1.
- **Cell 62 and the record:** "Under reading 1a … the absence at 75 to 150 um holds". This rests on slopes with SEs up to 420 (cell 61).
- **Cell 58 and the record:** "No reading shown gives the pattern" is literally true, but it leaves out the partial case under 7b (cell 56).
- **Cell 49 and the record:** "within mice 8 to 10 alone there is no difference". N with binocular cells, reading (b), gives p = 0.021 (cell 48). "No difference at p < 0.001" would be accurate.
- **Record, fig3def:** "DSI as measured changes only the PV- means". PV- medians and PV+ means also shift under N and W (cell 42). It holds for the main reading only.
- **Record, fig3-pv-lower-monocularity:** "0.4516 before rounding" appears in no output; cell 32 prints 0.452. The outcome does not change, since 0.452 > 0.451.
- **Record finding:** "trial counts per condition match the stim files for all 578 cells". Cell 18 checks "the stim file's repeats or one fewer".
- **README and cell 0:** "their stored traces equal the mask means of the published movies". This was shown for 9 cells on one plane (cell 22). The record says so correctly.
- **README:** "Most outcomes rest on the choice of cell set and are marked as assumed". The record marks 9 of 18, and fig3def's mark has no effect.
- **README:** "The counts of cells are about half the paper's". The local analyses have 18 of 86, 157 of 717 and 130 of 1,090 cells (cells 56, 61, 74). The Summary's "about half … or less" is accurate.

Everything else I checked in the Result lines, the Summary, the README and the record notes matches the outputs. That includes every value and p-value quoted for fig3abc, fig3c, mi-per-animal, fig4ag, fig4f-od, figs4, fig4i, fig4k, fig4jk and figs6cd, and the outcome counts in cell 0, the Summary and the README.

My round-1 reasons are in the record close to my own words. One is mis-pointed: for mi-dsi-relation the record writes "As for fig3abc". My "Same as above" in that row referred to fig3def's reason, that `dsi` is present for mice 8 to 10.

**3. Round-1 points**

Resolved:
- B1 and B2: the use of the folder is now decided on a stated basis, and the findings say the per-cell data are absent from the published folder.
- B3: one entry, the dates, counts and fields are now printed (cell 16).
- B6: the repeat counts and the 125 µm plane are commented on (cell 7).
- B7: the redundant conditional is gone.
- C2 and C3: one entry is one cell, `xy` is the centroid in pixels, and per-mouse counts are printed (cells 16, 20).
- C4: the truncated files are printed (cell 13).

Kept as findings, which is acceptable:
- B4: the frame-rate conflict.
- B5: the circular window, now named, with a per-mask variant shown.
- C1: what the binocmonocinds lists select cannot be settled from the data.

Still open and bearing on a conclusion:
1. fig4d is partial although the criterion has no partial case; by the criterion it is not reproduced.
2. fig4f-pv-od-spatial-decay meets the partial case under 7b with 1b, and this is not addressed.
3. fig4ef's partial case rests on unusable 1a slopes. Restate it on 1b (for example reading 3b) or change it.
4. figs6ab also rests on population reading (a), which is not stated. The restricted-population support quoted comes from the unstable orientation.
5. fig3-pv-lower-monocularity and mi-dsi-relation would be higher under N, the claims-file reading (b). The record needs to say why L alone decides.
6. Most of the 18 tested outcomes rest on the unconfirmed L cell set, which is fair to state. Its support should be given as counts, 235 of 270 and 769 against 944, in place of "nearly all" and "near".

On the claims file: I found no misreading of the paper. The outputs suggest, without proving, that the paper's slopes (PV- 0.10, PV+ 0.78) are on the 1b orientation, where the claims file makes 1a the main reading.
