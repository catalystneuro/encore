I judged the one paper `primary`. `papers/match/001785.yaml` passes validation.

**doi:10.1038/s41593-026-02301-4** (Fujimoto et al., Nat. Neurosci. 2026), **primary**.
- **Deciding evidence:** the dataset holds the data behind the paper's main results. The archive describes "Functional MRI (EPI; FC) data acquired before and after DBS in monkeys N, T and D, and pre/post data in monkeys B, W, and H". Its files also include before-and-after FA and T1w scans for monkeys N, T and D, the CC1 immunofluorescence images and the electron microscopy images. Those are the same monkeys and measurements as the paper's white matter and network figures (Figs. 2–6).
- **Mixed evidence:** the paper's Data availability statement names only DANDI:001773, not this dataset. DANDI:001773 is a smaller deposit from the same authors with the analysis code and source data tables. It also has the home cage behavior data (Extended Data Fig. 1), which this dataset lacks, so I listed it in `data_in`. That one behavioral finding can't be tested here. If you'd weigh that gap more heavily, `partial` would also be defensible.

The checks hadn't given a verdict, so there was nothing to correct.
