I've written the claims file at `claims/001290/10.1038-s41592-025-02614-5.yaml`. The quote checker passes with 0 problems.

**Text read:** the accepted author manuscript from PubMed Central (PMC13055889). That covers the main text, Methods, figure and Extended Data legends, Extended Data Table 1, and the supplement (proof plus the legends of Supplementary Figs. 1–18). There was no PDF of the main text, so the Extended Data figures could only be read through their legends.

**Code read:**
- evarol/dredge at ed236113
- InterpolationAfterDREDge at 0041079b
- HumanNeuropixelsPipeline at d74413cb

**What the dataset holds:** the paper's Data availability puts the "fast-motion NHP dataset of Extended Data Fig. 3" at DANDI:001290. That is an anesthetized, paralyzed macaque from the Movshon lab. The archive's description calls it "Supp. Fig. 3", which is the preprint's numbering.

**Claims:** 22, all with quotes. 9 claims carry statistics (13 statistical values in all), 9 have expected values, and 7 have criteria.
- **4 claims test this dataset** (Extended Data Fig. 3a–e): the spike-based DREDge estimate, the HDBSCAN clusters, the spline capturing sub-second displacement, and the spline correction improving the raster and localizations. The paper gives no numbers or tests for any of them. The criteria use the paper's own template-correlation metric and its "scrambled" motion-estimate control from Fig. 2e.
- **18 claims are `data: elsewhere`:** the human, NHP-insertion, IBL, NP Ultra, simulated and chronic findings, each with the deposit the paper names.

**Details the paper leaves open, with the readings named:**
- **Preprocessing, detection and localization:** the Methods say these were "chosen to suit each data source" and don't say what was chosen here. I used the IBL pipeline with DARTsort point-source localization as the standard choice. The variant is SpikeInterface's monopolar triangulation, as in the dredge repository's notebook.
- **Rigid or nonrigid registration:** Extended Data Table 1 has no row for this recording. Readings: nonrigid with the code defaults (window step 400 µm, scale 450 µm), or rigid.
- **Raster smoothing:** the Methods smooth at 1 µm and 1 s, but the code doesn't smooth by default. I followed the Methods and named the code's choice as a variant.
- **"High-amplitude" cut for clustering:** top 10% or top 25% of amplitudes.
- **HDBSCAN features:** depth and lateral position with amplitude, or depth with amplitude.
- **HDBSCAN minimum cluster size:** 25 or 100 spikes.
- **Spline form:** the knot spacing is fixed at 2.5 per second. Readings: a least-squares cubic spline, or a penalized cubic spline with the penalty chosen by generalized cross-validation.
- **Recording length:** the paper doesn't say whether it used the whole recording or a snippet. The criteria use the whole recording.
- **Fig. 2b:** the Results and the legend call it a human recording (ref. 13), but the same spline method is tied to this macaque recording in Extended Data Fig. 3. I recorded the Fig. 2b claims as data elsewhere and named the inconsistency.

**Missing from the paper:**
- No linked code implements the spline method (the HDBSCAN clustering and the spline fit), so every step of it comes from one Methods paragraph.
- The paper gives no session length, channel map or spike counts for this recording.

As instructed, nothing was committed.
