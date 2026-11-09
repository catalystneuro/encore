**Verifier report, round 2: Brezovec et al. 2022 on DANDI 000727 (0.240106.0043)**

Counts come from the claims file and attempt record: 20 claims. The record gives 8 reproduced, 5 partially reproduced, 1 not reproduced and 6 blocked. Cell indices below refer to the re-executed notebook and differ from round 1.

**1. Outcomes**

| Claim | Record | Agree? | Note |
|---|---|---|---|
| dataset-structure | reproduced | yes | Cells 3, 5, 14. |
| fig2c-fraction-correlated | partial | yes | Cell 19: (a) 31.1%, (b) 53.5%, rolled null 0.0%. |
| fig2c-venn-categories | partial | yes | Cell 22: under (a) the ranking holds and "all three" is 11.5%, below 20. |
| fig2-symmetry | reproduced | yes | Cell 25: 0.823; 0.672 against 0.449; A/B 2.38 and 0.31. |
| fig2e, fig3, fig6eg, fig7 | blocked (metadata_insufficient) | yes | I accept the author's category. A label for each voxel is metadata, not missing data. |
| fig4bcd-pc-structure | reproduced | yes | Cell 30: all criteria pass under both readings. |
| fig4fg-ridge-r2 | partial | yes | Cell 33: medians 0.155, 0.196, 0.212. |
| fig4h-r2-vs-movement | partial | yes | Cell 37: ρ is positive for all three, but only VR has p < 0.05. Pooled p = 0.064. Max 0.534. |
| fig4i-weights-stereotyped | reproduced | yes | Cell 40: rolled null median pair r ≤ 0.151, against an observed 0.646 or more. |
| fig5a-unique-variance | partial | yes | Cell 43. |
| fig5c-global-below-threshold | reproduced | **yes, changed from round 1** | Cell 46: I asked for a circular-shift null and it supports the result. Under (b) all 9 pass. The weakest is r = 0.013, with roll p = 0.025 against a null 95th percentile of 0.0103. The pass is still marginal: it holds under one reading only, and the left region has 4 blocks. |
| fig5f-ipsi-contra | not reproduced | yes | Cell 49: the demixing-model variant also shows mirror blocks rising (6.5% and 18.8% fall). |
| fig6-peak-time-range | reproduced | yes, by the criterion | Cell 54: reading (b) gives 0.32 s and −1.23 s. Every alternative timing falls outside tolerance (see 3). |
| fig6h-peak-vs-width | reproduced | yes | Cell 57: partial r = 0.623, and the correlation is positive within all 10 planes. |
| fig6fg-ipsi-leads-contra | reproduced | yes | Cell 60. |
| figs2-tdtomato-control | blocked (data_missing) | yes | Cell 63: the raw-channel check does not decide the claim. |
| figs4a-supervoxel-number | blocked (too_large) | yes | The full sweep is too large. A partial sweep on the 12 planes is still not attempted; the record states this. |

**2. Text against the outputs**

Contradicted by the outputs:
- **README:** "It takes about 13 minutes". Cell 65 prints "Notebook ran in 7.3 min".
- **Attempt record, figs4a notes:** "The 12 planes streamed here are 22.1 GB compressed and took 319 s". Cell 1 prints "streamed 12 FDA planes … in 214 s", and that figure includes 40 s of metadata.
- **Attempt record, fig6-peak-time-range response:** "the lag of more than 1 s holds in every plane from 38 on". Cell 54 gives 1st percentiles of −0.84, −0.88, −0.88 and −0.84 s for planes 38, 45, 52 and 80. Only planes 59 to 73 exceed a 1 s lag. Cell 55 and the claim's notes state this correctly ("at least 0.84 s").

Not supported by the outputs:
- **Cell 26, and the attempt record (fig2-symmetry response):** "each fly's brain mask overlaps its own mirror image at 0.804 to 0.916", offered as evidence that no fly is flipped. A mask's overlap with its own mirror is unchanged by a left-right flip, so it cannot show this. I suggested the check in round 1; it was the wrong test.
- **Cell 26:** the comparison of each fly's map with the pooled map against the mirrored pooled map includes that fly in the pooled map. This favours the unflipped answer, and the fly_105 margins are small (0.418 against 0.240, 0.299 against 0.220). A leave-one-out pooled map would settle it.
- **Cell 61:** "largest in the planes from 17 to 38 (0.20 to 0.33 s)". This is approximately right; for VR, planes 45 and 52 (0.22) exceed plane 38 (0.20).

Everything else matches the printed numbers: all other "**Result:" cells, the Summary (cell 66), the remaining README rows and the record's notes and findings.

My round-1 reasons are recorded faithfully in my own words. The exception is B7 (the clock-check null was not comparable): it appears under no claim, though cell 11 has fixed it. My B6 remark that fly_105's half-difference correlates negatively with rotation (cell 11) and that its VF R2 is −0.50 is also left out.

**3. Round-1 points**

Resolved:
- B1: roll null added; I withdraw the fig5c downgrade.
- B3: demixing variant added.
- B4 and B5: now stated in the text.
- B7: the null now uses the same 101 lags.
- B9: rolled null added.
- B10: denominator fixed, now 53.5%.
- B11: the AVIs and every array are listed.
- B12: colour range is now ±0.100.
- C requests met: roll nulls for fig2c and fig5c, the raw tdTomato check, per-plane leads, the within-plane lag-width correlation and the fly_105 orientation check.
- B2 for fig6h: plane is controlled for (partial r = 0.623, positive in all 10 planes).

Remaining points that bear on a conclusion:
- **fig6-peak-time-range (B2):** "reproduced" depends on the 0.32 s 99th percentile, which falls within tolerance only with behaviour sampled at the volume midpoint. Volume-start times give 0.58 s, removing each plane's median gives 0.50 s, and reading (a) gives 0.44 s; all are outside 0.27 to 0.33 s. The cell 55 text says this. The outcome follows the criterion fixed in advance, but the earliest-lead part cannot be tested with the timing the dandiset gives. Only the lag of more than 1 s is robust.
- **fig5c:** reproduced under reading (b) only, on a single marginal correlation (r = 0.013, roll p = 0.025) from a 4-block region. Reading (a) fails (roll p = 0.89).
- **figs4a:** the partial sweep on the 12 planes is still not attempted; the claim stays blocked.

Remaining points that do not bear on a conclusion:
- B6: the orientation evidence is weak, as described in section 2.
- B8: alpha is still selected on the test folds; the nested variant shows the effect is small.
