I've written `claims/000630/10.1126-science.adf0805.yaml`: 39 claims. The quote checker finds all 39 quotes and all 24 statistical values, with 0 problems. Nothing is committed.

**Text read.** I used the author manuscript of the version of record from PubMed Central (PMC11864503). It includes the main text, the legends of Figs 1 to 6, and the supplementary PDF: Materials and Methods, legends of Figs S1 to S9, and Tables S1 and S2. I opened no figures and did not use the bioRxiv preprint.

**Missing from the paper.** The four supplementary data tables (Data S1 to S4, .xlsx) are not under `paper/`. They hold the per-feature statistics. Each claim rests on the sentence or legend it quotes, and the code that wrote Data S2 and S4 stands in for them. I went ahead because the results are stated in the text, as an earlier file for a related Allen Institute paper (dandiset 000636) did. The cost is that no per-feature p-values or effect sizes could be recorded.

**Code read.** github.com/AllenInstitute/patchseq_human_L1 at commit 7777857 (archived on Zenodo as 10.5281/zenodo.8310226). It settles the cell selections, feature filters, tests, FDR correction and classifier settings. The opening comment describes what it holds.

**Claims.**
- 39 claims, all with quotes.
- 21 have statistics, 24 have criteria, 8 have expected values.
- By data source:
  - **14 `with_labels`:** human electrophysiology from the dandiset, with cell-type labels from the code's per-cell table.
  - **7 `with_inputs`:** mouse electrophysiology from DANDI 000020, transcriptomes, or nucleated-patch data.
  - **18 `elsewhere`:** morphology at the Brain Image Library, transcriptomics references, MERFISH and cytoarchitecture data.

The dandiset holds human electrophysiology only (210 files). The author still has to write the link claim matching its files to the code's table.

**Details the paper leaves open, with the readings named:**
- **O1, custom feature definitions.** The adaptation ratio's order, the irregularity ratio, the post-AP slope ("ADP slope"), the ADP voltage and depolarizing sag come from unreleased IPFX code. Readings: (a) the Methods' definitions; (b) the paper's own per-cell feature values, used as a check.
- **O2, cross-species ANOVA.** The Fig. 3D legend says ANOVA on ranks and the Data S4 description says Type II. The code uses raw values, Type I. Both are named.
- **O3, classifier and clustering preprocessing.** The Methods include outlier removal and dropping cells missing over 60% of features; the code does neither for the subclass classifier or the clustering search. Both are named.
- **Fig 6A.** Minimum group size: the legend says at least 4 cells, the code 5. "High d′": d′ ≥ 2.2 (the Methods' threshold for grouping t-types) or above the median between-subclass d′.
- **Fig 6B.** Transcriptomic input scale: CPM (Methods) or log(CPM+1) (code).
- **Fig S8A.** The 82% is read four ways: plain or balanced accuracy, crossed with full or site-aligned features. Fig S8B: plain or balanced accuracy.
- **Fig 4B.** The group compared with the rest of L1: the MC4R subclass or each MC4R t-type.
- **Fig 3F.** The voltage step for each cell's conductance: the +70 mV step or the maximum over steps.
- **Fig 4D.** "No irregular spiking": none, or a minority of cells.
- **Fig 3G.** "Similar amount of variability" is reported, not judged, with a 10% reading.
- **Random seeds** are a standard choice.

**Missing data a claim needs:**
- The file used to constrain the transcriptomic d′ fits for Fig 6B (`zinb_human.h5`) is not public; it is to be refitted from the Methods.
- The paper names no deposit for the mouse TEa electrophysiology (Fig 3E) or the mouse nucleated patches (Fig 3F).
- Nucleated-patch areas come from images.
- I could not tell whether the dandiset holds the Amsterdam and Szeged held-out cells needed for Fig S8B and the LAMP5 within-subclass trend (Fig 2C).
- Only 2 PAX6 TNFAIP8L3 cells have electrophysiology. The Fig 5B test can still reach its threshold.
