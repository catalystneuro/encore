**Round 2 verifier report: 001350-iram-2024-01 (doi:10.1073/pnas.2307250121)**

The claims file has 30 claims. The attempt record has 30 outcomes and 30 round-1 results.

**1. Outcomes and assumptions**

| Claim(s) | Record | Agree? | Notes |
|---|---|---|---|
| fig2c, fig2d, fig2e, figs3c, figs3d | blocked, data_missing | Yes | Masks exist for 1 of 5 Flox mice (cell 5). The reason given for not using the segmentation model is acceptable. |
| 5 optic-nerve claims; fig2gk, figs3fg, fig1d, fig1ef, figs1, fig4eg; fig5e, fig5d, culture-mbp | blocked, data_missing | Yes | |
| figs5ab, fig6b, fig6cd, fig6eg | blocked, not_runnable | Yes | The GEO listing (geo cell 32) confirms there are no cluster labels. |
| fig3a | partially_reproduced | Yes | `measured: [848, 312]` records the majority reading, which the notes say is "not adopted". List every reading or only 848. |
| fig3bc | reproduced, assumed | Yes | The assumption (JASPAR MA0083.3 or the strict CC(A/T)6GG box in place of the MEME-ChIP motif) is stated and reasonable. Enrichment survives GC stratification (MH OR 2.14 and 2.75, geo cell 13). |
| fig3d | partially_reproduced, assumed | Yes | The per-cell-type consensus and FIMO default are stated and reasonable. Dataset S1 groups agree (42 of 85, geo cell 16). |
| no-myelin-genes | reproduced, assumed | Yes | The gene list is stated and reasonable. |
| fig4ab | reproduced, assumed | Yes, narrowly | The assumption is stated, but it is weaker than in round 1. See the note below. |
| fig4cd | reproduced, assumed | Yes | Rests on the per-stage model, which is stated. Under (c), Actb in OPCs has padj 0.51. |
| figs4ef | partially_reproduced, assumed | Yes | The assembly set (26 genes) and the per-stage model are stated and reasonable. 1 of 25 assembly genes changes and 1 of 13 disassembly genes changes (geo cell 29). |

Note on fig4ab: the new comparison with the paper's own tables (geo cell 23) shows the paper did not use reading (b). Its baseMean ratio to the paper is 0.73 and 0.85, against 0.99 for (a). In OPCs, (b) recovers only 98 of the paper's 154 genes (Jaccard 0.456). So the 160 matches the count, but by a method the paper did not use. The reading closest to the paper's scale, (a), gives 117 and 294, both outside tolerance.

**2. Text against outputs**

- **Main cell 25:** "where the paper's Fig. 2C and 2D together imply 4.9 and 6.5; the total is close, and the myelinated count is low because the fraction myelinated is lower in the masks". For the Flox mouse this is not supported. Cell 24 gives 3.62 against 4.86 axons per µm², 26% low. That shortfall accounts for about half the density gap (0.74 × 0.71 ≈ 0.53). The record's fig2d notes ("so the low myelinated density goes with a lower fraction myelinated") leave out the same point.
- **Main cell 25, main cell 36 (Summary), record fig2d deviation:** "about half the paper's values in both genotypes". This holds for Flox (0.95/1.8 = 0.53). For cKO, cell 19 gives 0.82 to 0.98 against 1.42 (O4a), 0.58 to 0.69, and up to 0.77 under O4b.
- **Geo cell 24:** "That is what tximport's offsets give, so the paper most likely used offsets". The baseMean scale equally fits no length correction at all, which is reading (a). Only the count gap between (a) and the paper (117 against 154) points to offsets, and pydeseq2 against R could also explain that gap.
- **Geo cell 27:** "and Dataset S2 holds the OPC samples alone, as a per-stage model would". No printed output shows the sample columns of Dataset S2.
- **Geo cell 22 against cell 23:** reading (b) OPC gives 160 in cell 22 and 159 in cell 23, after dropping unnamed or duplicate genes. This is harmless but not mentioned.
- **README:** "Five to twenty minutes". Geo cell 29 prints "notebook ran in 1492 s", about 25 minutes.
- **Record, fig4cd notes:** these mix readings. The Srf and Actb log2FC are from (b), but "Actg1 … p 0.024" is from (a); (b) gives 0.028.

Every other result sentence, summary row, README row and note I checked matches the printed outputs. That includes the fig2c, fig2e, figs3c and figs3d ranges, the fig3a reading table and the Dataset S1 crosstab (799 of 800 listed; 15 omitted), the fig3bc percentages, the fig3d 43/87, 42/85 and 56, the DEG counts, the Cfl1 values, and the claim counts (5 + 14 + 7 + 4 = 30).

The round-1 reasons in `verifications` are in my own words and faithful to my report, including `agrees: false` on fig3a.

I found no misreading of the paper in the claims file. The amended figs4ef statement matches the Results text and Fig. S4F.

**3. Round-1 points**

Resolved:
- 1: data_missing is used, and the reason for not using the model is given.
- 3: the image counts are corrected.
- 4: the deduplication variant changes no mouse's percent by more than 0.02 points.
- 5: no change was needed.
- 6: the warning is noted.
- 7: the no-IgG rows are in the table, the outcome changed, and Dataset S1 was checked.
- 10: the 848 is now described as a count of the deposited file.
- 11: an assembly set was tested and the outcome changed.
- Section C: the mask overlay was added (I viewed it, and it shows no obvious gaps), Dataset S1 was compared, and the snRNA-seq listing was added.

Partly resolved:
- 2: the reversed directions are now discussed. The density gap explanation overstates how close the totals are (see section 2).
- 8: GC strata were added and the one-mismatch reading is labelled as the attempt's own. MEME-ChIP remains a stated deviation.

Remaining items that bear on a conclusion:
- fig4ab: tximport offsets in R DESeq2 are still not run. The paper's tables now argue against (b) as its procedure, so the "reproduced" rests on a count match under a stand-in, with low gene overlap in OPCs.
- fig4ab, fig4cd, figs4ef: reading (a) moved from 118/293 to 117/294 and (c) from 130/418 to 130/423 between rounds. The record says only "in this run". Whether pydeseq2 results vary from run to run, which would also affect the 160 and 264, is not explained.
- fig3a: the `measured` value 312 contradicts "none is adopted".
- TEM (does not change the blocked outcomes): the image scale and the unit of Fig. 2D remain unchecked.
