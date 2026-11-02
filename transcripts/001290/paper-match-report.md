I gave DANDI:001290's one paper a verdict of **partial**. The file `papers/match/001290.yaml` passes `python tools/paper_match.py validate`.

- **doi:10.1038/s41592-025-02614-5** (DREDge, Windolf et al., Nature Methods)
  - **Deciding evidence:** the paper's Data availability section says "the fast-motion NHP dataset of Extended Data Fig. 3 is available at DANDI (https://dandiarchive.org/dandiset/001290/)".
  - **What this dataset holds:** one NWB file from one *Macaca nemestrina* (sub-L11104). That recording supports only the spline-registration analysis in Extended Data Fig. 3.
  - **Where the rest of the data are:** the paper's main findings rest on human, rodent and other primate recordings held elsewhere. I listed them in `data_in`: DANDI:000397, DANDI:000957, DANDI:001282, Dryad doi:10.5061/dryad.d2547d840, Figshare doi:10.6084/m9.figshare.14024495.v1, and the Ulbert Lab G-node repository.

The archive description says the data appear in "Supp. Fig. 3", but in the paper they are in Extended Data Fig. 3. Supplementary Fig. 3 there is about line-noise removal, so an attempt should use Extended Data Fig. 3.
