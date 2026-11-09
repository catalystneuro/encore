**A. Outcomes** (30 claims in the claims file)

| Claim | My outcome | Reason |
|---|---|---|
| fig2c-cc-percent-myelinated | blocked (data_missing) | The masks cover 1 SRF-Flox mouse (sub-370) and 4 cKO mice, which I confirmed on the archive (cell 5). The criterion's test of 5 against 5 cannot be run. Partial data (cell 17): cKO is lower in all 8 combinations, Student p 0.13 to 0.20, and the cKO mean (14.3 to 18.9%) is outside 22 ± 2.2 under every reading. |
| fig2d-cc-myelinated-density | blocked (data_missing) | Same coverage gap. Every labelled mouse has about 0.8 to 1.1 myelinated axons/µm² (cell 19), well below both paper values (1.42 and 1.8). The ratio is within 0.79 ± 0.079 only when sub-373C (15 µm²) is included. |
| fig2e-cc-g-ratio | blocked (data_missing) | Same coverage gap. In all 16 combinations cKO is lower than Flox (−0.009 to −0.026), against the paper's +0.057. |
| figs3c-cc-myelin-thickness-unchanged | blocked (data_missing) | Same coverage gap. p ≥ 0.05 in all 16 combinations, but with one Flox mouse a claim of absence cannot be judged. |
| figs3d-cc-larger-myelinated-diameter | blocked (data_missing) | Same coverage gap. cKO is smaller than Flox in 15 of 16 combinations, the opposite of the claim, but n_flox = 1. |
| figs2b, figs2e, figs2cf, figs2ij, figs2kl (5 optic nerve claims) | blocked (data_missing) | The archive lists only corpus callosum images and masks (134 assets checked). |
| fig2gk, figs3fg, fig1d, fig1ef, figs1, fig4eg | blocked (data_missing) | The dandiset holds no immunostaining, RNAscope or RT-PCR data. |
| fig5e, fig5d, culture-mbp-unchanged | blocked (data_missing) | The dandiset holds no culture imaging. |
| fig3a-chip-peaks | partially_reproduced | The 848 is just the row count of the deposited consensus BED. The 329 depends on the reading (geo cell 8): 312 and 316 with a majority of replicates (in tolerance), 204 to 206 with all replicates and 404 to 409 with at least 2 (both out). |
| fig3bc-chip-tss-carg | reproduced | 64.3% of peaks lie within 2 kb of a TSS (geo cell 10). CArG sites are enriched against both the flank and shuffled backgrounds under FIMO (10.7% against 5.2%) and the strict consensus (9.8% against 3.0%), p < 1e-4 (geo cell 11). |
| fig3d-shared-carg-targets | partially_reproduced | Under the Methods' per-cell-type consensus, about half the CArG target genes are shared (49 to 51% of the union), and every named gene except Arc is among them. The count is 39 to 43, not 60 ± 6. Only 1 of 9 readings is in tolerance (56), and that reading drops Fos, Junb, Srf and Vcl (geo cell 13). |
| no-myelin-genes-direct-targets | reproduced | None of the 11 myelin genes is the nearest gene of any of the 848 peaks (geo cell 15). |
| fig4ab-rnaseq-degs | reproduced, with a caveat | The only length-normalized reading run, (b), gives 160 and 264 (geo cell 17). Readings (a) and (c) skip the length normalization the Methods state and miss (118/293 and 130/418). The canonical tximport-offset reading was not run (problem 9). |
| fig4cd-rnaseq-srf-actb-down | reproduced | Srf is down under every reading. Actb is down at padj < 0.05 in both stages under (a) and (b); under (c), OPC padj is 0.51. Actg1 is down at p < 0.05 in OL, the Fig. 4H threshold (geo cell 19). |
| figs4ef-assembly-not-disassembly-genes | reproduced (tested part) | 0 of the 12 non-Cfl1 disassembly genes change in any reading. Cfl1 is lower in OL (padj 0.002 to 0.03) and unchanged in OPC. The "mainly assembly genes" part is tested only through Actb and Actg1 (geo cell 21). |
| figs5ab-gsea-bulk | blocked (other) | Not run: GeneTrail 3 is a web service. |
| fig6b, fig6cd, fig6eg | blocked (other) | Not run: the snRNA-seq analysis is an R/Seurat/MAST pipeline and R is not installed. |

The claims file gives "Not testable on this dandiset" as the criterion for every GEO claim. So the GEO outcomes above are my own judgement against the expected values and the statements, not against a criterion.

**B. Problems**

1. [affects a conclusion] Main notebook, cells 13–26. The blocking reason is given as `other`. The cause is missing per-mouse measurements: masks exist for 1 of 5 Flox mice, while raw images exist for all 10. `data_missing` describes this better. The notebook also never mentions the segmentation model the dandiset description points to (axondeepseg/model_seg_unmyelinated_tem), which could produce masks for the 77 unlabelled images. Whether that is an acceptable extension of reading O1 decides whether these claims stay blocked.
2. [affects a conclusion] Cells 19 and 22–26. Partial evidence the notebook shows but does not discuss:
   - Density in every fully labelled mouse of both genotypes is about 0.8 to 1.1 per µm², roughly half the paper's values. This points to a systematic difference between the masks and the paper's counting, or to the unit, before any question of n.
   - The g-ratio and diameter directions are reversed in almost every combination.
3. [does not affect a conclusion] Cell 6 text says masks exist for "9 full images". The output shows 8 full images plus 2 ROIs. It also gives sub-366A's image sides as up to 2426 px, where the output shows 2385 rows and 2613 columns.
4. [does not affect a conclusion] `srf_tem.measure_image` counts pixels lying in both masks (up to 51,098 px per cKO image, cell 9) as both myelinated and unmyelinated objects, without deduplication. This is a small bias in percent myelinated.
5. [does not affect a conclusion] `mouse_percent_and_density`, reading O4a. Leaving out edge objects without a counting frame biases density low. Both O4 readings are shown, as the claims file asks.
6. [does not affect a conclusion] Cell 19 raises a scipy "catastrophic cancellation" warning: sub-370's two images have near-identical densities, so the per-image Welch p is unreliable. It is a variant only.
7. [affects a conclusion] geo cell 8 prints that a majority of replicates without the IgG filter gives exactly 329. That is not in the reading table, and it conflicts with the paper's "not in the IgG control". The 329 rests on a definition the notebook cannot pin down.
8. [affects a conclusion] geo cells 11 and 13 (fig3bc, fig3d).
   - The paper ran FIMO on the motifs MEME-ChIP found. The notebook uses JASPAR MA0083.3, and genes are assigned by HOMER's nearest gene.
   - The 1-mismatch "CArG" reading is the author's own; it is not enriched over all peaks (p 0.28).
   - Peak windows are much GC-richer than flank windows (0.546 against 0.449), so the flank comparison is confounded; the shuffled background controls for composition.
9. [affects a conclusion] `srf_geo.deseq` (fig4ab, fig4cd, figs4ef). The paper's "normalization for transcript length" in DESeq2 normally means tximport's average-length offsets, which were not run. pydeseq2 also replaces R's DESeq2. Reading (b), lengthScaledTPM, is a stand-in, and the exact 264 may depend on it.
10. [does not affect a conclusion] geo, fig3a: the "848" reproduces a count of the deposited file, not a re-analysis.
11. [affects a conclusion] geo cell 21 (figs4ef): no set of actin-assembly genes (for example the Arp2/3 subunits) is tested, so "mainly regulates assembly genes" is only partly tested.

Checks that passed:
- On synthetic masks, the helpers behave correctly. Touching fibres are split, equivalent-circle diameters are exact, the minimum Feret of a 20×60 rectangle is 20, and edge flags work. `student_one_vs_many` equals `scipy.stats.ttest_ind` (Student) at n = 1 against 4, and the per-mouse pooled and per-image aggregations are correct.
- The pixel size (0.00493 µm in every sidecar), mask coverage, and the README's ROI coordinates match the archive.

I found no misreading of the paper in the claims file.

**C. What I could not check**

- Whether the masks label every unmyelinated and myelinated axon in an image. One mask overlay on its raw image per genotype would have let me judge mask completeness and the density gap.
- The image scale against a scale bar. The raw images carry none, so this cannot be checked.
- Whether R DESeq2 with tximport offsets gives the same 157 and 264. That reading, added as reading (d), would settle fig4ab.
- What exactly makes up Dataset S1 (the paper's 329 and 60 lists). It was not supplied. Comparing those lists with the notebook's gene sets would settle the readings for fig3a and fig3d.
- Whether GEO GSE241561 holds processed snRNA-seq matrices that a Python pipeline could use for fig6. A listing of its supplementary files would show whether those claims are runnable.
- The values printed on the main Fig. 2 panels (37/22, 1.8/1.42, p values), which the claims file itself lists as unchecked.
