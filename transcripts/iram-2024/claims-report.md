I wrote `claims/001350/10.1073-pnas.2307250121.yaml`, with 29 claims. Five of them can be tested on this dataset. All 29 quotes pass `tools/claims_check.py` word for word, and the file passes the schema. The checker still exits non-zero: it flags 14 p-values as "not found", because the paper prints them only on figure panels. I read each of them off the figure.

**Text read:** the version of record from Europe PMC (PMC10962977): main text, figure legends, Methods, and the SI Appendix (Figs. S1 to S5, their legends, and the Supplementary Methods). Datasets S1 to S3 (spreadsheets) were not read; no claim needs them.
- The main article's PDF was not supplied. I read the values and p-values on Figs. 2 and 5 from the figure images on the PMC article page, and those of Figs. S2 and S3 from the supplement PDF. Values read off bar plots are labelled as such.
- The paper links no analysis code. Its only data deposit is NCBI GEO GSE241561 (the sequencing data). The dataset's description links a segmentation model trained later on these images; that is not the paper's code, and I did not read it.

**Dataset:** adult corpus callosum electron-microscopy (TEM) images, 5 SRF-Flox and 5 SRF-cKO mice, with segmentation masks. These are the data of Fig. 2A to 2E and Fig. S3A to S3D.

**Claims:**
- **29 claims**, all with quotes and all with a criterion.
- **12 claims carry statistics** (18 entries), and 9 have expected values.
- **5 testable here:**
  - Fig. 2C, percent of axons myelinated (p = 0.003)
  - Fig. 2D, myelinated axons per area (p = 0.008)
  - Fig. 2E, g-ratio, 0.760 against 0.703 (p = 0.0145)
  - Fig. S3C, myelin thickness unchanged, a claim of absence (p = 0.08)
  - Fig. S3D, larger diameter of myelinated axons (p = 0.024)
- **24 not testable here:** the optic nerve TEM, immunostaining, RNAscope, cell-culture actin staining, and the ChIP-seq, bulk RNA-seq and single-nucleus RNA-seq results. The sequencing claims are marked as data held elsewhere, in GEO GSE241561.

**Details the paper leaves open** (O1 to O7 in the file's opening comment; each testable claim must give the same outcome under every reading, or it is blocked):
- **O1, how axons are identified:** the paper scored axons by hand in Fiji. The dataset's masks were made for a later project, so using them is a deviation to record, not a reading.
- **O2, a mouse's percent myelinated:** pooled counts across its images, or the mean of per-image percentages.
- **O3, density per mouse:** total count over total area, or the mean of per-image densities. The figure's axis gives no unit; I read it as axons per µm², and the cKO-to-Flox ratio is kept as a unit-free check.
- **O4, axons cut by the image edge:** left out, or kept.
- **O5, what the line tool's "diameter" means:** equivalent-circle diameter, or minimum Feret diameter. Thickness and g-ratio follow from the same choice.
- **O6, which "100 myelinated axons per mouse":** all of them, or 100 drawn at random with a fixed seed, with the spread over draws shown.
- **O7, the t test:** Student's (the Prism default) or Welch's. For the absence claim, Student's test is the paper's and Welch's is a variant.
- **Not stated anywhere:** the adults' age, and how the g-ratio is defined (axon diameter over fibre diameter is assumed).

**Missing from what the claims needed:**
- **Fig. 4 image:** it would not download, so the values and p-values on Fig. 4C to 4F are not recorded. None of those claims can be tested on this dataset.
- **Fig. 2E and Fig. S3D:** only 4 Flox dots are visible, although the legends say n = 5.
- **Fig. 5:** the text says the genotypes are "nearly indistinguishable" at day 7, while Fig. 5E marks the day-7 difference with two asterisks. The claim records both.
- **MBP protein in culture:** stated in the text with no figure and no test.
