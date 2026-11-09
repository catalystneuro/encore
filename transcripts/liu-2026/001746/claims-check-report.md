The claims file has been corrected and is fit for an attempt (`ready: true`).

**Checker result:** `claims/001746/10.1038-s41556-026-02009-4.yaml: 32 claims, 32 quotes, 12 statistical values, 0 problems`. It passed both before and after my edits.

**Changes, by claim:**
- **fig2a-subclass-counts:** The seven stated counts add up to 244, and 244 plus the 29 VENs makes 273. So the paper's counts leave the VENs out. The VENs are now counted apart from L5 ET and L5/6 CT, and the counts with them included are a variant that does not decide.
- **fig2d-l23it-small-tau** (and every claim that reuses its test): The FDR correction was run over the 20 features the Methods name, but the Methods do not list every feature. The code settles it: 39 features (`Ins_patchseq_ephs.xlsx`, `calFDR_ephsio.m`). Those 39 are now the main set and the 20 a variant.
- **ven-firing-rate-variability:** Added a third way of reading "PCs": the layer 5 PC groups pooled, from the Discussion's "Compared with neighbouring PCs".
- **fig3d-saddle-phase-plane:** The criterion used a measure the agent made up (the fraction of cells with a dip between the two phases). The paper says the phase peak index is what quantifies the saddle shape. The claim now takes its outcome from fig3e-phase-peak-index, and the dip fraction is only a description.
- **fig3e-phase-peak-index:** Both corrections for Dunn's test (Bonferroni and Sidak) must now agree, and the claim is blocked when they don't. The criterion also notes that the paper read the peaks by hand, so the automatic reading is not the paper's; if its outcome differs from the code's per-cell values, that is reported as a deviation.
- **fig4i-peak-index-ais-distance-real → model-ais-distance-ap-shape:** The ANCOVA compares the VEN model with the real neurons, so its statistics moved to the model claim. That claim's statement, source (now Fig. 4e-i) and quote were extended to the model-matches-data finding.
- **supp8-ven-subtypes-similar-features:** The statement said Patch-seq cells. The Extended Data Fig. 9 legend says the Supplementary Table 8 comparisons were "obtained without RNA extraction", and the paper takes priority over the code. The claim now names those recordings and is blocked as data_missing if the dataset lacks them; the Patch-seq comparison is a variant.
- **morph-more-distinct-than-ephys:** The source now cites Supplementary Tables 3 and 4, as the paper does (it said 2 and 4).
- **fig7c-tau-rna-distance:** The tau defined in the Methods now decides; the code's first-sweep tau is a variant.
- **ext1d-ven-soma-density:** The statement said AIC and V1 differ in soma size and density. The text states no result for that panel, so the statement now says only that the panel compares them.

**Still open (recorded under `checks`):**
- **ext9cd-ven-subtypes-ap:** The paper does not say which features the FDR correction covers. For a claim of absence this matters, because correcting over only two features makes a difference easier to find.
- **fig4i:** The paper does not say which 62 neurons were used. I did not check whether `NeuronPeakIdx_summary.mat` names them by cell ID.
- **Fig. 4i ANCOVA:** The slope result (P = 0.0031) reads as a significant difference between model and data, which sits oddly with the paper's "closely matched". It is recorded as printed.
- **Not available or not checked:** I took the code details in the opening comment as written and did not reread the code. The Supplementary Information and the values printed only inside figures were not available.
