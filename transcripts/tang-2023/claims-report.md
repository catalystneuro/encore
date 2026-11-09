I wrote `claims/000447/10.1016-j.celrep.2023.112246.yaml`. The quote checker passes except for one p-value the text prints garbled ("1.39e11" in the Figure 3D legend); I read it as 1.39e-11. Nothing is committed.

**Text read.** The NIH author manuscript (PMC10124109, NIHMS1887302) as served by Europe PMC: main text, STAR Methods, figure legends, and the supplement PDF's text (Figures S1 to S7). I did not read the version of record, and the supplement text was clean enough that I didn't open the PDF.

**Code read.** github.com/JadhavLab/GeometricTransformation at commit 5e55e69. Where the Methods are silent, it settles:
- which epochs are N, F and N′;
- which reward well is center, left and right, and so the order of the four trajectories;
- the rules for excluding interneurons;
- the cells used;
- the CCGP and SVM details.

**Claims.**
- 32 claims, all with quotes and all with criteria.
- 25 carry statistics (52 values) and 7 carry expected numbers.
- All are `data: dataset`; the paper uses no outside data.
- They cover Figure 1 and S1 (behaviour), the cell counts, Figures 2, S3 and S4 (remapping, PV similarity, decoding, ramping cells), Figures 3, S5 and S6 (selectivity index, path equivalence, manifolds and distances) and Figures 4 and S7 (CCGP, geometric null model, the 35 dichotomies).

**Details left open, with the readings named:**
- **Rate-map smoothing (garbled in the text, "s = σ cm").** Main reading 8 cm, the σ of the 2D maps; 4 and 2 cm are run as variants.
- **Decoding windows.** The Methods say a 200 ms window "with 50 ms overlap" (a 150 ms step); the code steps 50 ms and keeps only theta periods, which is the variant.
- **Figure 2F, which trial is "−1".** Either the last N trial, or the code's 10th N trial.
- **Figure 2E shuffles.** How many, and what the Wilcoxon test pairs: one shuffle per bin, or the median of 100.
- **Rate overlap (Figure S3A).** Mean of the rate map, or spikes over time.
- **Figure S3D.** The novel trials are N then N′, N alone, or N′ alone.
- **Ramping denominator (Figure S4).** All sessions pooled, or N′ alone.
- **Selectivity index (Figure 3D).** Sessions pooled, N′ alone, or F alone. Figure 3E and S5E: whether "novel" means N′ or N.
- **Figure S5F.** Signed or absolute selectivity index.
- **Manifold cells.** The Methods require spatially tuned cells; the code applies no tuning filter. The expected counts of 98 CA1 and 171 PFC cells decide between them.
- **Distance alignment.**
  - Figure 3H: the Methods are silent; I followed the code, which aligns CA1 by location and PFC by phase.
  - Figure 3I: the Methods and the code disagree. The Methods' pairing is the main reading and the code's is a variant.
  - UMAP bins: the Methods say 1 cm, the code uses normalized length (variant).
- **Geometric null model (Figure S7).** No code; the axes are permuted either in UMAP space or in neuron space.
- **Interpretations I made, not set by the paper.**
  - "Most" dichotomies (Figure S7D) is read as more than half.
  - Which bins count as the reward wells (Figure S4D).
  - The Fisher z test for comparing two correlations (Figure S5E).
  - For the manifold shapes (Figure 3F, 3G), the paper gives no measure. That claim takes its outcome from the distance claims for Figure 3H and 3I.

**Missing that claims need:**
- **Data likely not in the dandiset.** The de novo learning sessions (Figure 1B, 1C, S1B) and the second group of three rats run F-N-F′-N′ (Figure S1C) are probably absent; the dandiset holds only the N, F and N′ epochs. The paper says its raw data are on Brandeis servers, available on request.
- **Absent from the repository.** The code that computes the rate maps, the saved UMAP templates, and code for Figures S3A, S4, the 2E shuffles and the S7 null model.
- **Unlabelled post hoc p-values.** Several legends (Figures 1C, 2E, S3A, S4C, S5D, S6, S7B) give p-values without saying which pair each belongs to.
