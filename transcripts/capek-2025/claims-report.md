I've written `claims/capek-2025.yaml`. The quote checker passes every quote, but it exits non-zero on one p-value. The Extended Data Fig. 7a legend prints that value as "6.30e-3". I read it at line 2074 of the text and it is correct; the checker only looks for the "6.3e-3" form. I left both the checker and the value as they are.

**Text read:** the version of record (`paper/10.1038-s41586-025-08682-z.txt`). That covers the main text, the figure legends, the Methods, the Extended Data Fig. 1–7 legends, the reporting summary, and the Source Data workbook (MOESM3), which has one sheet per panel. The paper has no other supplementary file. There was no code to read: the paper says "No custom algorithms or computer code was produced". The DANDI:001609 description lists TPN-V two-photon dye-fill stacks: five front-view and five top-view per species for four species, extra-strain fills, and D. mojavensis TPN-Ia, Ib and VI fills.

**Counts:**
- 37 claims: 36 findings plus one `link` claim, which checks the dataset's stacks against the Extended Data Fig. 3e centre-of-mass values in the Source Data.
- 36 quotes and no `inferred` notes.
- 14 claims carry `statistics`, 61 test entries in all.
- 33 claims have criteria.
- Only the anatomy claims (11 of them) can be tested on the dataset.
- 18 are `data: elsewhere`: the behaviour, threshold and Q10 claims use the paper's Source Data, plus the hemibrain v1.2.1 connectome, GenBank and SRA PRJNA948454.
- The remaining claims (confocal images, the full set of dye fills, DM1 olfactory fills, the gene locus) rest on data the paper did not deposit.

**Details the paper leaves open, and the readings named for each:**
- **Which stacks make up the n = 5 reconstructions, and which view feeds the lateral horn (LH) centre of mass:** (a) the top-view stacks; (b) the registered reconstructions, projected.
- **How lateral accessory calyx (lACA) extent is measured** (the paper has no measure): (a) traced cable length inside the calyx; (b) above-threshold pixels in the calyx crop. A one-sided Mann-Whitney test is shown as a variant.
- **Clustering linkage:** average or complete, with single as a variant.
- **What SigClust runs on:** distance-matrix rows, a classical MDS embedding, or the UMAP coordinates.
- **"Sorts by species" (Extended Data Fig. 3d):** nearest-neighbour species fraction, or silhouette score.
- **"Cluster by species" (Extended Data Fig. 7g):** nearest neighbour is of its own species, or each extra strain falls on its own species' side of the D. mojavensis split.
- **Pairwise "one-way ANOVA" P values in Fig. 2n:** an ANOVA on each pair alone, Tukey after a three-group ANOVA, or pooled-error contrasts.
- **The 2-way ANOVA in Extended Data Fig. 5e:** Tukey against each control, against the pooled controls, or a one-way ANOVA per temperature.
- **Sequence identity:** counted with gaps, without gaps, or over the shorter sequence. The D. melanogaster sequence has no accession in the paper; the reading is the reference Gr28b-PD protein.
- **RNA-seq:** how reads are assigned to the variants (variant-specific exon or full transcript), and what "comparable" to Ir25a and Ir93a means (inside their range, or within 1 log2 unit).
- **"Prefers 15–20 °C" (Fig. 1b):** significant attraction at both temperatures, or the only negative mean preference indices.
- **Connectome threshold:** whether >9 synapses applies to each hot receptor neuron or to the summed weight.
- **Fixed by the Methods and not left open:** CAJAL settings (100 points, Gromov-Wasserstein), how the two distance matrices are combined, and the behaviour tests (two-tailed one-sample t-tests).

**Missing from the paper or the Source Data that some claims need:**
- The binarization threshold for tracing, the normalized frame size for the centre of mass, and UMAP parameters.
- The genome assembly and annotation for the D. mojavensis Gr28b locus.
- Sources for 22 of the 25 aligned sequences.
- Raw patch-clamp recordings (only per-cell thresholds and Q10 values are deposited).

**Source Data problems,** recorded in the file for the author:
- The sheets for Fig. 5c and 5d have swapped names.
- In Extended Data Fig. 5f, the Gal4/+ values are identical to the Gal4>CsChrimson values, which cannot give the printed p = 0.440.
- In Extended Data Fig. 2, the wild-type 45 °C values equal Fig. 1d's 40 °C column, and the 40 °C group has 7 and 7 values where the legend says N = 11.
- Fig. 2i lists 12 cells against n = 13 in the legend.
- The Fig. 3j legend prints nearly the same P values for the control and the DmelGr28b.d rescue.
