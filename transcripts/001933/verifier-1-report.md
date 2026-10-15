**A. Outcomes** (18 claims, taken from the claims file; there are no author outcome cells to compare against)

| Claim | Outcome | Reason |
|---|---|---|
| source-data-link | not_reproduced | Cell 24: mice match 100%. Traces match 60.9% and evoked integrals 60.9%, because Calb1 S8D/S8E is 0/384 for both. Spontaneous integrals match 0% under either window. Part 4 is below 50%, so the claim fails. Fig 6E matches the 0.5 mW labels (120/120) and not the 4 mW labels (0/120). |
| fig6e-anxa1-evoked-reduced | reproduced | Cell 32: 64 vs 56 stimulations, GS 48.8 vs WT 128, one-tailed p = 1.16e-22 (paper 1.10e-20). The code window gives 1.1e-20 exactly. |
| fig6e-anxa1-evoked-per-mouse | reproduced | Cell 34: 7 of 8 significant under all four readings, and 3743 is the exception. |
| supp7c-anxa1-evoked-all-powers | reproduced | Cell 36: G2019S is lower at all 4 powers (p from 3.1e-15 to 1.2e-22). Code-window p-values equal the paper's at 0.1, 0.5 and 1 mW. |
| fig6f-anxa1-spontaneous-reduced | reproduced | Cell 40: counts are exactly 1064 and 798, and per-mouse counts run 57 to 285. One-tailed p = 4.85e-72 (paper 2.75e-177; the per-transient-mean variant gives 2.2e-177). |
| fig6f-anxa1-spontaneous-per-mouse | partially_reproduced | Cell 42: 5 of 8 under every reading, with 3743, 4651 and 4652 not significant. The per-transient-mean variant under Student one-tailed gives the paper's 6, with exactly 3743 and 4651 as the exceptions. |
| supp8c-calb1-spontaneous-not-reduced | reproduced | Cell 44: p = 0.0509, which is ≥ 0.05. Counts are 896 and 635, both within tolerance. The margin is very thin and the Calb1 signal is not the paper's (problems 1 and 6). |
| supp8e-calb1-evoked-reduced | reproduced | Cell 46: 56 vs 40 stimulations, G2019S lower at all 4 powers (p from 6.3e-10 to 4.4e-07). |
| supp8e-calb1-few-mice-reduced | partially_reproduced | Cell 48: at 0.5 mW the readings give 7, 6, 4 and 4. The best reading is 4, which the criterion counts as partial. Two of 7 appears only at the variant powers 0.1 and 1 mW under the Student readings. |
| cohens-d-anxa1-larger | not_reproduced | Cell 50: Anxa1 d = 2.21 (in tolerance) but Calb1 d = 1.40 (tolerance 0.684 to 0.836). The ratio is 1.58, below 2. The paper's own source values give 2.06 and 0.765 (cell 24, part 6), so the gap comes from the dandiset's Calb1 trace. |
| fig1d-lrrk2-enriched-vulnerable | reproduced | Cell 53: 16 sections, Aldh1a1+ higher, unpaired p = 4.65e-06 (paper 0.0008). I confirmed the column labels in the sheet. |
| fig2b-rab3-phosphorylation | not_reproduced | Cell 55: under both readings 1694 and 1810 peptides are altered (tolerance 260 to 318). RAB3 T86 is altered but with difference −1.31, meaning it is higher in the samples labelled MLi‑2, the opposite of the direction required. Neither condition holds. |
| fig2eg-prab3-increased | reproduced | Cell 57: all 4 comparisons hold. F values and Sidak p-values equal the legend's (8.593/0.0202, 11.33/0.0069, 14.76/0.0036, 7.398/0.0415). GS+MLi‑2 does not differ from WT. |
| fig3d-rim-binds-unphosphorylated | partially_reproduced | Cell 59: RIM1, RIM2 and RILPL1 hold under the paired test. RILPL2 has no values in the RAB3A pulldowns, so the paired test is undefined: 3 of 4. The notebook's "4 of 4" uses the imputation variant. |
| fig4d-fewer-active-zones | partially_reproduced | Cell 61: (A) holds for both measures (4D p = 6.4e-05 lower; 4E p = 0.030 higher). (B) on the images finds neither effect (p = 0.46, 0.81 and 0.21). |
| fig4i-rim1-reduced | reproduced | Cell 63: synaptosome RIM1 is lower in GS, p = 0.0245, the paper's value exactly. S1 p = 0.90 and SNc p = 0.94. n is 6 per genotype. |
| fig5-bassoon-vulnerable-axons | partially_reproduced | Cell 65: with the duplicated WT section counted once, Aldh1a1+ density Sidak p = 0.058, so 5 of 6 parts hold. As deposited, all 6 hold and the legend's F and p values are reproduced exactly. |
| fig5j-no-axon-loss | reproduced | Cell 67: 12 vs 12 sections, p = 0.117, difference −0.071, d = −0.67. |

Totals: 10 reproduced, 5 partially reproduced, 3 not reproduced, 0 blocked. The notebook treats no claim as blocked, so step 4 does not apply. No claim involves a chance level.

**B. Problems**

1. [affects a conclusion] Cells 24, 26 and 27: the dandiset's Calb1 dF/F is not the trace behind Supplementary Fig. 8. None of the 384 S8D traces is within 1e-6 of any epoch (closest 15.7 % dF/F), and the slopes run from −0.88 to 1.55. Recomputing from raw with any background fraction does not close the gap. So `supp8c`, `supp8e` (both claims) and `cohens-d` are tested on a different signal than the paper's. The `cohens-d` failure and the `supp8e-few-mice` partial most likely come from this, not from the biology.
2. [affects a conclusion] Cell 24 part 4 and cells 40 and 42: the sheet column is named `scaled_spontaneous_transient_integral`. The notebook shows these values equal about 0.005 × the mean dF/F of each transient (13 of 15 Anxa1 mice within 1%), not the trapezoid integral the criterion prescribes. That mismatch fails part 4 of `source-data-link` and makes `fig6f-per-mouse` partial.
3. [affects a conclusion] Cell 55 and `archives.volcano_test`: the deposited abundances are not normalized (MLi‑2 sample medians are about 0.6 log2 higher), so 99% of the "altered" peptides are lower with vehicle. Median-centring gives 282 altered, inside the tolerance. The paper's own volcano table has the opposite sign from (vehicle − MLi‑2) for 4592 of 4770 peptides, and it gives only 254 at the legend's thresholds. In the deposited columns, RAB3 T86 is higher in the samples labelled MLi‑2 under every reading. Either the sample labels or the paper's "Difference" are inverted relative to the legend.
4. [affects a conclusion] Cell 59: the closing decision replaces the criterion's paired test with the imputation variant for RILPL2, turning 3 of 4 into 4 of 4. RILPL2 is present in 6 of 6 p‑RAB3A pulldowns and 0 of 6 RAB3A pulldowns, which supports the claim qualitatively, but the criterion's test cannot score it.
5. [affects a conclusion] Cells 21 and 61, `archives.synaptosome_fraction` and `synaptosome_area`: the FIJI re-implementation finds a median of 183 VAMP2 particles per image against the legend's "about 1000". The WT bassoon+ percentage comes out at 52% against 21% in the source data. Part B's null result is therefore weak evidence, and the claim's outcome depends on it. The channel order (0, 1, 2) = (488, 568, 647) is taken from the archive annotation, not read per image. I checked one image's OME metadata and the order is right there.
6. [affects a conclusion] Cell 44: Calb1 spontaneous p = 0.0509 sits right at the threshold. Two variants reach p < 0.05 and would reverse the outcome: the code's window as written (1.8e-05) and the per-transient mean (2.2e-09).
7. [does not affect a conclusion] Cell 65: the legend's statistics are reproduced only with the duplicated WT section (1723, sections 4 and 5) included. The paper's analysis evidently counted it twice.
8. [does not affect a conclusion] Cells 32, 40 and 46: as the legends specify, the tests pool stimulations or transients across mice. Tests on one mean per mouse are much weaker: Anxa1 evoked p = 4e-4, Anxa1 spontaneous p = 0.032, Calb1 evoked p = 0.04 to 0.09 (not significant at 1 and 4 mW).
9. [does not affect a conclusion] `lrrk2.load_source_data`: the 6E records are assigned power 0.5 by the loader, not read from the sheet. Part 3 confirms the assignment indirectly (120/120 at 0.5 mW, 0/120 at 4 mW).
10. [does not affect a conclusion] Cell 53: the paper's p = 0.0008 matches a paired test over sections (0.00076) or an unpaired test on mouse means (0.00082), not the legend's unpaired test over sections (4.65e-06).
11. [does not affect a conclusion] Cells 8 and 9: mice 3742 and 4885 received the paper's powers as 0.33 s trains, and their responses do not follow the labelled power. Excluding them still gives p = 4e-17.
12. [does not affect a conclusion] I tested `double_threshold` (edge runs dropped, sub-threshold runs rejected), `evoked_integrals` (a 0.5 s square pulse integrates to 5.0, and the code window gives 5.1), `cohens_d` and `twoway_anova`/`sidak_within` (they match the classical F on balanced data) on synthetic inputs. All behave correctly.

**C. What I could not check**

- Re-execution, and the 168 synaptosome images beyond one file's metadata. A per-image overlay, or particle counts printed next to the legend's ~1000 per area for a few images, would show whether part B's segmentation is usable.
- The exact form of the 6F/S8C "scaled" values. An output that fits candidate scalings (integral ÷ duration, ÷ 200 and so on) at 1e-4 would settle part 4 of `source-data-link`.
- Whether the PXD065006 Vehicle/MLi‑2 columns are swapped. An output that recomputes the volcano table's Difference and p with Proteome Discoverer-style normalization, under both label assignments, and reports exact agreement would decide it.
- Why the Calb1 trace differs. The deposited processing parameters per Calb1 session, or a raw-to-dF/F recomputation that matches even one S8D trace, would identify the trace the paper used.
- How sensitive `supp8c` is to small changes in the exclusion window (±1 to 10 samples). Printing p over that range would show how fragile the 0.0509 is.
