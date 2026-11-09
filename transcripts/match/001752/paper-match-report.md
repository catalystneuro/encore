**doi:10.1038/s41556-026-02009-4**, "An atlas of primate insular cortex reveals a signal-processing strategy in von Economo neurons" (Nature Cell Biology): **partial** (`by: agent`).

- **What decided it:** the paper's Data availability section lists this dataset as one of four DANDI deposits: "https://dandiarchive.org/dandiset/001752 (postsynaptic currents)". The Results and Methods describe the same recordings the archive metadata does: spontaneous and miniature EPSCs and IPSCs from von Economo neurons and pyramidal cells in macaque anterior insular cortex slices.
- **Part the dataset holds:** only the postsynaptic current comparison in Fig. 5a–c can be tested here.
- **Where the rest of the paper's data are:**
  - DANDI:001746 (main Patch-seq set)
  - DANDI:001750 (sodium channel currents)
  - DANDI:001751 (multi-patch recordings)
  - GEO GSE319557 and GSE319369 (sequencing)
  - MetaboLights MTBLS13927 (metabolomics)
  - NeuroMorpho.org (neuron morphologies)

All of these are listed in `data_in`. The verdict follows the same pattern as the existing agent verdict for this paper in `papers/match/001750.yaml`.

`papers/match/001752.yaml` passes `python tools/paper_match.py validate`.
