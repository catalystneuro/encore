I wrote `claims/001746/10.1038-s41556-026-02009-4.yaml` with 32 claims. The quote checker passes with 0 problems. Nothing is committed.

**Text read.** The version of record (open access, Europe PMC PMC13457102): main text, figure and Extended Data legends, Methods, and the Data and Code availability statements. There was no PDF, so values printed only inside figures (box-plot values and their P values) could not be read.

**Missing.** The Supplementary Information (Supplementary Figs. 1–17, Tables 1–12) and the Source Data were not in `paper/`. I did not stop, for two reasons:
- The main findings this dataset tests rest on the Results, legends and Methods, which were all there.
- The code shows how Supplementary Tables 1, 2, 8 and 9 were computed.

The cost is that several claims have no expected values, because those values are only in the supplement. These are the input-resistance, threshold/latency, AP-width and sag claims (Supp. Fig. 11), the VEN firing-rate and variability claim (Supp. Tables 1–2), and the VEN-subtype comparisons (Supp. Tables 8–9). Supplying the supplement would let a later pass add them.

**Code read.**
- github.com/RFLiu2021/AIC_proj at commit 44cd8a6. It holds the per-cell metadata and feature tables, how cells are grouped into subclasses by cluster, the FDR scripts, and the phase peak index, Fig. 4i and Extended Data Fig. 9 scripts.
- PatchAnaLab 1.0 (Zenodo 10.5281/zenodo.19995355), the feature-extraction package.

**Counts.**

| Item | Count |
|---|---|
| Claims (1 link, 31 findings) | 32 |
| With quotes | 32 |
| With statistics | 4 (12 values) |
| With criteria | 32 |
| `data: with_labels` | 17 |
| `data: dataset` | 3 |
| `data: with_inputs` | 3 |
| `data: elsewhere` | 9 (mostly pointing to the 001750, 001751 and 001752 claims files) |

**Details left open, with the readings named:**
- **Which comparison "stood out" or "distinctive" means:** a subclass against the other five pooled, or against each subclass in turn (the code computes both).
- **Spike-timing variability:** the text names no measure. Readings are ISI CV and ISI Fano factor.
- **Sag:** sag ratio or sag value.
- **Which cells count as PCs:** the five PC groups pooled, or each group.
- **Phase peak index:**
  - The paper picked the peaks by hand, so I fixed an automatic rule.
  - Which APs: the first AP, or the median over APs, of the maximal-rate sweep.
  - Dunn's test correction: Bonferroni or Sidak.
- **Fig. 2a counts:** cluster-to-subclass mapping from the code, or from the dataset's metadata. Whether VENs are counted in L5/6 CT is a further reading.
- **"Greater disparity" (VEN-L vs L5/6 CT):** read as more features with FDR < 0.05.
- **Morphology vs physiology:** count or fraction of significant features.
- **Supplementary Table 8 grouping:** the code uses Patch-seq clusters, while the legend says the comparisons were made without RNA extraction. Expert labels are a second reading.
- **Methods vs code:**
  - Tau is averaged over all hyperpolarizing sweeps in the Methods but taken from the first sweep in the code; the code's version is a variant.
  - The steady state is the last 100 ms in the Methods, and the last two-thirds of the step in the code.
  - For the RNA distance in Fig. 7c, the Methods use 10x counts and the code uses Patch-seq counts; the code's version is a variant.
  - The code's plot exclusions are variants.

**Things that may block claims or need checking:**
- **Fig. 4a–c (281 VENs, 306 PCs) and Extended Data Fig. 9c,d (85 VEN-L, 41 VEN-S).** These are "additional" recordings and the paper names no deposit. The dandiset holds 462 assets, the same number of cells as the code's Patch-seq table. If these recordings are absent, the claims are blocked as `data_missing`, with the Patch-seq subset shown as a variant that does not decide.
- **Cell counts.** The code's subclass groups hold 30/22/122/29/17/13 cells, against the legend's 30/17/119/22/16/13. VEN-L and VEN-S counts also differ.
- **Subjects.** The code's table lists 10 subjects; the paper says 12 animals.
- **Fig. 4i.** It needs AIS distances from the morphologies, which is why it is `with_inputs`.
