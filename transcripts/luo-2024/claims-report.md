I wrote `claims/001261/10.1002-cne.70001.yaml`. The quote checker reports 28 claims, 28 quotes, 31 statistical values and 0 problems. Nothing is committed.

**Text read**
- **Paper:** the version of record (open access, PMC11583843, from Europe PMC), including the Methods, Table 1 and all figure legends.
- **Supplement:** the docx (CNE-532-e70001-s001). Its legends are in the text file. I opened four of its figure images (S2-2, S4-1, S7-1, S9-1) only to see which features they mark as significantly different.
- **Code:** the analysis code the Methods link (Zenodo 10.5281/zenodo.10975327), which is github.com/nsdesai/patch_clamp_analysis v1.0.1, commit 17a3265. It holds MATLAB functions that extract the electrophysiological features. It has no code for resting potential, the statistics, PCA, UMAP, LDA or morphology.
- **Dataset:** the archive description says it holds "the physiology data" (current clamp, 36 subjects).

**Claims**
- 28 claims, all with quotes, none marked `inferred`.
- 24 carry statistics, almost all Wilcoxon rank-sum bounds. For the supplementary panels the bounds come from the figure's significance stars.
- 14 carry expected values. The tolerance is 10% of each value; the opening comment explains why I did not use the SD.
- All 28 have criteria.
- They cover:
  - sample sizes;
  - mouse cholinergic vs noncholinergic electrophysiology, morphology, Sholl, UMAP and LDA (Figs 2, 4, 5, S2-2, S4-1);
  - mouse vs macaque electrophysiology, morphology and UMAP (Figs 7, 9, S7-1, S9-1);
  - the combined UMAP, LDA and LDA weights (Fig 10).

**Details left open, with the readings named**
- **Resting potential:** the code does not compute it. Readings: (a) a value stored with each recording; (b) a sweep with no bias current. If the dataset holds neither, it cannot be computed.
- **Downstroke:** the code's window runs to the end of the step, apparently by a bug. Readings: (a) from the first peak to 20 ms after it; (b) the code as written.
- **Adaptation index and CV of interspike intervals:** the Methods say "maximal current step". Readings: (a) the 200 pA step; (b) the step with the most spikes, as the code does. The released code's CV is not a scalar for 3 or more spikes, so the Methods' definition is used.
- **Noncholinergic group:** ChAT-negative only, or with ChAT-unknown neurons added (as the code's `getindices.m` does).
- **Missing values in UMAP and LDA:** drop the neuron, or use the feature mean.
- **UMAP:** its parameters and seed are not given, so I used the package defaults and 10 seeds. The paper never defines its "boundary"; I measure it with a linear boundary in the two UMAP dimensions plus a label-permutation test.
- **LDA:** z-scored or raw features. The "shuffled" control: permuted labels, or each feature permuted on its own. The "weighted differences": |coefficient|, or |coefficient × difference of group means|.
- **"Strong separation" (Fig 7C):** (a) as clean as Fig 2C (at most 2 of 94 misclassified); (b) better than every permutation.
- **Sholl test:** not named. Readings: (a) a rank-sum at each radius; (b) a rank-sum on total intersections.
- **Methods vs code:** where they disagree (input resistance and time-constant steps, spike latency, AHP window, maximum-rate step), the Methods are the main reading and the code's choice is a variant.

**Inconsistencies in the paper**
- **Feature count, macaque vs mouse:** the text says "15 of the 18 … insignificantly different", but the same paragraph reports 7 features that differ. Readings: 15 differ (the sentence read as "significantly"), or 17 (from the legends).
- **Morphology count:** the text says five of 13 features differ; the Fig 9 legend says six. Fig S9-1 is consistent with six.
- **Convex hull volume units:** the text prints ×10³ µm³, but the Fig S4-1B axis shows ×10⁶ µm³. Both are compared.
- **Fig 5A legend:** it contradicts the Results on the shuffled control. I followed the Results.

**Missing**
- There is no PDF, so the main-figure panels 2D, 4D, 7D and 9D could not be read. Which 12 features Fig 7D shows, and the input-resistance values, are therefore unknown. The claims that depend on them say so.
- The morphology and Fig 10 claims need reconstruction data, which the dataset description suggests it may not hold. Checking that is for the author.
