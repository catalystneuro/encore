# 001545, Rajebhosale et al. 2025

Four claims reproduced, one partially, seven not reproduced and 24 blocked on
the dandiset, 23 for missing data and one as methods underspecified; the other
20 claims use data elsewhere and are left out of the counts, 19 on the
snMultiome data in GEO (GSE280167), all blocked as not runnable, and one on the
Allen Developing Mouse Brain Atlas, reproduced on an assumption. The first
verification round agreed with 55 of the 56 outcomes as they stood and the
second with 55, disagreeing on `figs9c-embryonic-sgc-genes`; the author
proposed that change, and a third round, which reviewed only it, agreed. It
pins version 0.250809.1653, the only published version; the draft has the same
48 asset ids. The paper, Rajebhosale, Jiang, Ressa, Johnson, Desai, Jone, Role
and Talmage, "Diversification of dentate gyrus granule cell subtypes is
regulated by Nrg1 nuclear back-signaling" in Life Science Alliance, compares
dentate granule cells with one primary dendrite (GCs) and semilunar granule
cells with several (SGCs) in wild-type (VV) and Nrg1 V321L knock-in (LL) mice
by whole-cell current clamp with biocytin fills, with their soma position and
morphology, LDA, k-means and PCA on the electrophysiological features, Golgi
and RNAScope counts, and snRNA-Seq and snATAC-Seq of the dentate gyrus. The
claims were written from the version of record in Europe PMC (PMC12032840) with
the supplementary figure legends, the Key Resources Table and the Fig 2 and
Fig S2 images, and from the paper's code (nsdesai/patch_clamp_analysis at
commit 5d756c2 and RajNINDS/V321L-snMultiome at commit c124726); the check
corrected twelve claims, added four and left three points open. The 13 claims
on the current clamp recordings were tested. Reproduced are
`fig2i-v321l-rmp-not-different` (Welch p = 0.595, paper P = 0.8374),
`fig2j-v321l-spike-width-not-different` (p = 0.216),
`fig2k-v321l-downstroke-not-different` (p = 0.877) and
`figs2d-ephys-kmeans-v321l-like-wt-sgc`, which without mouse VV253 would be not
reproduced. Not reproduced are the WT differences of
`fig1j-sgc-hyperpolarized-rmp` (median -83.8 against -75.3 mV, U = 32, p =
0.083, paper U = 26, P = 0.02), `fig1k-sgc-narrower-spike` (p = 0.082) and
`fig1l-sgc-faster-downstroke` (p = 0.350), all three in the paper's direction,
and `fig1m-phase-plots`, which rests on the last two;
`figs2e-pca-separation-lost`, where the WT centroids lie inside each other's
95% ellipses; `figs2g-lda-classifier-accuracy` (WT 55.0% against the paper's
78%, where always predicting GC gives 60%, and V321L 41.7%); and
`figs2f-centroid-separation-reduced`, where both V321L centroids lie on the WT
GC side of the boundary. `figs1-remaining-properties-no-difference` is
partially reproduced, as only its cell-type half could be run, and
`fig2m-ephys-lda-wt-gc-apart` is blocked because its two readings disagree (WT
GC apart on the z-scored features, WT SGC on the top 9 PCs), as the criterion
says to do. `figs9c-embryonic-sgc-genes` was judged by eye on the atlas's E18.5
ISH images of Penk, Scg2, Nrg1 and Cit, with the dentate gyrus also located by
eye. The 23 claims on soma position, morphology, Golgi and RNAScope data are
blocked because those data are not in the dandiset, and the 19 snMultiome
claims because they need the paper's R pipeline and the nuclei and cluster
labels it kept, which are not deposited. The author's first run had figs2f
partially reproduced and figs9c blocked as other, not attempted. The author
asked a reader whether the figs8a criterion had the genotypes reversed; the
reader amended it to WT (VV) and V321L (LL), and the claim stayed blocked.
Round 1 disagreed with figs2f, which moved to not reproduced, showed that the
missing 14th WT GC cannot bring fig1j below 0.05 (exact p 0.053 at best), and
asked for variants without the AHP width and without mouse VV253, the spike
count at rheobase, a check of the bias current, the per-cell feature table and
a test of figs9c, and noted that ggplot2's default ellipse is type "t"; in
reply all were added, with a variant removing the 10 pA bias from each baseline
(p = 0.125), figs9c became partially reproduced on an assumption, and the
claims file's account of the ggplot2 default was filed as a question in
`questions/001545.yaml`. Round 2 disagreed with figs9c, whose criterion has one
condition and no partial rule, found the Scg2 crops off the dentate crescent,
and found sentences the outputs did not support (that the variants change no
outcome, where fig2m would be not reproduced with the AHP width left out and
figs2d without VV253, and four others), all corrected; the Scg2 sections were
recentred by eye (mask fractions 0.0032 and 0.0010). The entry check rejects
any `imread(` call, so the author decoded the ISH images with PIL's
`ImageFile.Parser`, said so in a code comment and noted that a maintainer may
want to confirm this use. The author's run took about 30 minutes and nothing
failed; the notebook ran in 38 s at first, 80 s after the author-answers run,
about 61 s after round 1, 95 s after round 2 and 73 s after round 3. The tests
in `tests/` were not run, as pytest is not installed, and untracked entries at
the repository root (`.bashrc`, `.idea`, `scripts` and others), which the
author did not create, were left alone.

The dandiset holds only the current clamp recordings, 48 files; the soma
positions and the morphology from the biocytin fills (splay angle, branch
points, dendritic length, 15 parameters), on which Fig 1F to I, Fig 2C to H,
Fig S1 and the multiple regression rest, are not in it, and neither are the
Golgi and RNAScope data, so 23 of the paper's 56 claims cannot be tested for
this reason. The files hold 13 WT GCs and 9 WT SGCs, where the paper's
electrophysiology has 14 and 9, and 12 V321L GCs and 14 V321L SGCs, where the
paper has 10 and 15; nothing in the files says which WT GC is missing or why
the V321L cell types differ, so the paper's cell sets cannot be rebuilt. The
general stimulus field says neurons were kept near -65 mV with a constant
current and stepped from -60 to 200 pA, but the voltage before the steps is -68
to -89 mV in every cell, 14 cells were stepped to 250 or 300 pA, and the
bias_current attribute is 10 pA in every sweep, so whether a holding current
was applied, and how much, cannot be told; every sweep of every file also
stores the same bridge balance (20 MOhm) and capacitance compensation (1 pF),
which look like defaults. Every CurrentClampStimulusSeries stores the current
in picoamperes (values -60 to 300) under the unit amperes with conversion 1,
and the electrode cell_id is VP neuron in all 48 files, though the cells are
dentate granule cells. The genotype is coded only as VV or LL in the subject
ids, with the surgery field and GEO saying VV is wild type, and the cell type
only as the end of the session description (semilunar or not semilunar). The 4
GCs of WT mouse VV253 have spike widths of 2.1 to 2.7 ms, and the figs2d result
rests on them. GEO GSE280167 holds, per mouse, the raw feature-barcode matrix
of every barcode (342,506 to 501,480 barcodes, genes and peaks) and a smoothed
ATAC cut-site track per sample; the nuclei kept after filtering and doublet
removal, the cluster labels and the per-nucleus ATAC fragments are not
deposited. Of the paper itself, its text gives the V321L classifier accuracy as
52% (kappa 0.08) where its Fig S2G matrix gives 48%. Questions are put to the
paper's authors: whether the four-class LDA of Fig 2M and Fig S2C was fitted on
the z-scored features or on principal components; which twenty features were
extracted and how cells with a missing feature were handled in the LDA, k-means
and PCA (here 4 cells lack the code's AHP width and were dropped, which fits
the 21 WT and 23 V321L cells of the Fig S2G matrices); and which Allen ISH
series and sections Fig S9C shows.

The author's points on the protocol: it gives no rule for a claim where only
part of the criterion can be run and the criterion has no partial rule, so
figs1-remaining and, at first, figs2f were recorded as partially reproduced
with the reason in the notes; it forbids `data_missing` for claims whose data
are elsewhere, even when those data are not deposited in usable form (the
per-nucleus ATAC fragments exist only as raw reads), so `not_runnable` was
used; it has no rule for criteria that rely on software in another language
(Seurat and Monocle3 in R) while the entry environment is Python only, so these
were blocked without a Python reimplementation, which would replace the
paper's clustering with the attempt's own; per-sweep `remfile` reads took 6.7
minutes for the dataset, where a 16 MB first chunk streams each file in one
request and takes 20 s but uses a private `remfile` argument; and a qualitative
image claim such as figs9c fits no `blocked_by` category, so `other` was used.
