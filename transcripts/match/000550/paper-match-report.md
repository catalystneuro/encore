I wrote one verdict to `papers/match/000550.yaml`, and `python tools/paper_match.py validate` passes on it.

**doi:10.1016/j.bioelechem.2022.108319** (Kim et al. 2022, "Action spectra and mechanisms of (in)efficiency of bipolar electric pulses at electroporation"): **partial**.
- **What decided it:** every one of the dataset's 17 files is named for Figure 6 of the paper, for example `sub-Fig6-5xBi-0,83MHz-08_ses-BPAE-5xBipolar-0,83MHz_image.nwb`.
- **What it holds:** the dataset description matches the paper's section 3.4, "Effect of pulse repetition rate": BPAE endothelial cell monolayers given 5 unipolar or bipolar 600 ns pulses at 10 kHz to 833 kHz. Only that section's findings can be tested on it.
- **What it lacks:** the paper's other experiments on pulse shape, duration and number, and the strobe imaging of CHO cells.
- **Other datasets (`data_in`):** I listed DANDI:000448, 000489, 000548 and 000549, which the archive also links to this paper. The paper has no data availability statement, so these come from the archive's links, not from the paper itself. I did not check which figures each of them holds. The registry already records 000489 as this paper's primary dataset (`papers/datasets/kim-2022.yaml`).
