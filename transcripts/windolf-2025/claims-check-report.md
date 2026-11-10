The file is **not ready**. The paper text I was given has no Results and no Methods, so most of the file can't be checked against it.

**Checker result:** `claims/windolf-2025.yaml: 34 claims, 34 quotes, 13 statistical values, 35 problems`. The problems are 29 quotes not found and 6 p-values not found (fig5b, fig5c ×3, fig5d, fig6), all from the Results.

**Why so many fail:** `paper/10.1038-s41592-025-02614-5.txt` is the publisher's paywalled preview. It holds only the abstract, Data and Code availability, the references and the Extended Data legends. The supplement PDF holds only the supplementary text and figure legends. The writer worked from the PMC author manuscript (PMC13055889), which isn't under `paper/`. The quotes that do pass are those from Extended Data legends (all of Extended Data Fig. 3, and Extended Data Fig. 1b).

**Changes, by claim:**
- **Header and opening comment:** `papers/datasets/windolf-2025.yaml` lists both DANDI:001290 and DANDI:001282 as primary datasets. I removed the single-dataset `dataset:` block, which the schema says a paper's own claims file leaves out, and named both dandisets.
- **edf3a, edf3b, edf3c, edf3de:** added `datasets: ["001290"]`, which a paper with several datasets requires.
- **fig4-nhp-insertion, fig4f-insertion-anatomy:** these were marked `elsewhere`, but their data is DANDI:001282, one of this paper's two datasets. Changed to `data: dataset`, `datasets: ["001282"]`, and removed `where`. Added Supplementary Fig. 5 (monkey 2) to the fig4 source.
- **supp13-simulated-short-probe:** the Supp. Fig. 13b legend gives two-sided Wilcoxon signed-rank tests with n = 3000 time bins per recording. I corrected the test and n and pointed the source at that legend.
- **fig2fg-unit-spatial-spread:** the recorded p < 0.05 is the Bonferroni threshold in the Extended Data Fig. 5b legend, not a result. I took it out of `statistics` and stated the test and threshold in a criterion.
- **edf6-128-channel:** the legend says "30 μm pitch", not vertical spacing. Corrected the statement.
- **Pipeline step 3 comment:** the Extended Data Fig. 3c zoom covers 100 to 110 s, so the panel spans at least 110 s. Added that.

**Still open (recorded under `checks`):**
- **Missing text:** the full text (Results and Methods) needs to be put under `paper/`, then the file checked again. Until then, none of the Results quotes, Results p-values or criterion details cited to the Methods can be checked. Those details are the spike pipeline, raster bins and smoothing, the AP correlation threshold, time horizon and lambdas, the spline method, the template correlation metric, and the description of the macaque recording.
- **fig4 claims have no criterion:** they now rest on DANDI:001282, so they need one, and it has to come from the Methods, which aren't available.
- **supp14 figure:** the Supp. Fig. 14 legend says failure comes "at the densest layout", which looks like a slip for "sparsest". The ≈50 µm figure in the claim comes from the Results and couldn't be checked.

The last check entry has `ready: false`. Only `claims/windolf-2025.yaml` was changed; nothing was committed.
