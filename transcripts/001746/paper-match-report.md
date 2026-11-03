I gave the one paper a verdict of `partial`. The match file passes validation.

**doi:10.1038/s41556-026-02009-4** ("An atlas of primate insular cortex reveals a signal-processing strategy in von Economo neurons", Nature Cell Biology 2026)
- **What decided it:** the paper's Data availability statement lists this dataset as "https://dandiarchive.org/dandiset/001746 (main dataset, Patch-seq)" and also names DANDI:001750 (sodium channel currents), DANDI:001751 (multi-patch recording) and DANDI:001752 (postsynaptic currents).
- **What this dataset holds:** the archive metadata describes 462 NWB files from 10 cynomolgus macaques. They are current-clamp Patch-seq recordings from anterior insular cortex, annotated with transcriptomic cell types. So the paper's Patch-seq electrophysiology findings can be tested on it.
- **What it does not hold:** most of the paper's other data is deposited elsewhere, and I listed these in `data_in`:
  - the scRNA-seq atlas of 122,663 cells and the Patch-seq sequencing reads (GEO GSE319557 and GSE319369)
  - metabolomics (MetaboLights MTBLS13927)
  - neuron morphologies (NeuroMorpho.org)
  - the three other DANDI datasets, 001750, 001751 and 001752

Since the paper is `partial`, the question of where a non-matching paper's data lives does not arise.
