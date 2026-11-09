I gave the one paper a verdict of **partial** in `papers/match/001750.yaml`, and the file passes validation.

**doi:10.1038/s41556-026-02009-4** ("An atlas of primate insular cortex reveals a signal-processing strategy in von Economo neurons"), verdict `partial`.
- **Deciding evidence:** the paper's Data availability section lists this dataset as "https://dandiarchive.org/dandiset/001750 (sodium channel currents)". It is one of four DANDI sets the paper names.
- **What can be tested here:** only one result. That is the outside-out patch-clamp comparison of somatic Na+ currents, which were lower in von Economo neurons (n = 14) than in layer 5 pyramidal cells (n = 21), Fig. 4d.
- **Fit with the dataset:** the archive describes outside-out sodium current recordings from crab-eating monkey anterior insular cortex. It has 35 files from one subject in two session groups, which matches 14 + 21 cells.
- **Where the rest of the data are:**
  - the main Patch-seq recordings: DANDI:001746
  - multi-patch recordings: DANDI:001751
  - postsynaptic currents: DANDI:001752
  - sequencing: GEO GSE319557 and GSE319369
  - metabolomics: MetaboLights MTBLS13927
  - morphology: NeuroMorpho.org

  All of these are listed in `data_in`.
