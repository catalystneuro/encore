I wrote `claims/000036/10.1523-eneuro.0280-21.2021.yaml` and did not commit it. The quote checker passes it with 0 problems.

**Text read:** the version of record, full text from Europe PMC (PMC8856714). That covers the Methods, Results, Discussion, the figure legends, the Extended Data figure legends, and Tables 1 and 2. Nothing the claims need is missing from the text. The Extended Data figures are image files and no PDF was stored, so I did not see the images, only their legends. Extended Data 1 is the analysis code itself.

**Code read:** github.com/wmayner/openscope-differentiation at commit 2d959bd71b47055d2a3fd306091fe9254ceb86fb. It settles most of what the Methods leave open: how a trial is cut and truncated, the spectrum and normalisation, log10, the post hoc contrasts and their multiple-comparison correction, the UMAP settings and seed, the decoding setup, the session subset for the mediation analysis, and the Fig. 8 blur. Its `results/` folder holds the paper's own per-trial ND values for the 44 sessions, which the author can use for a link claim. The code's README names a Zenodo deposit of the processed data (doi:10.5281/zenodo.4734580); I recorded it as outside data.

**Counts:**
- **Claims:** 26.
- **Quotes:** 25 claims have one. The exception is the cell counts per layer and area (`ext1-2-cell-counts`), which appear only in an image. Those numbers come from the code's output for that figure (`results/table-s1.csv`) and are marked as inferred.
- **Statistics:** 16 claims carry them, 82 values in all.
- **Criteria:** all 26 claims have one.

**Details left open, and the readings named for each:**
1. **Artifact removal for running and pupil data:** the Methods say parameters were chosen by hand per session and gives none. Readings: no manual removal, or the per-session parameters in the Zenodo deposit.
2. **Pupil diameter:** the Methods use twice the ellipse's semi-major axis (main reading); the code uses 2·√(area/π) (variant).
3. **Event bins in the multivariate event analysis:** the Methods drop 1-s bins with no events (main); the code keeps them (variant).
4. **Isolation window for the indicator-kinetics events:** the legend says 50 ms before and 100 ms after (main); the code uses 50 and 100 frames (variant).
5. **Permutation p-value:** the Methods count permuted differences "greater than" the observed one; the code counts "greater or equal" and uses p ≤ 0.05. Both are shown.
6. **DC removal for spectral energy:** per-pixel mean (legend) or the movie's global mean (code).
7. **Vague wording turned into thresholds:**
   - Decoding is "high": a mean accuracy of at least 0.75, and at least 0.9.
   - "Most" layers and areas: more than half of the 15.
   - "Nearly all" parameter sets: at least 90%, and at least 80%.
8. **Test for Extended Data Fig. 8-1 (low-level stimulus properties):** the paper names none. Readings: two-sided or one-sided Pearson correlation.

**Inconsistencies in the paper:**
- The Extended Data Fig. 3-1 legend gives the area interaction as χ²(2) = 16.343, which repeats the layer result. The code's output is χ²(4) = 22.213, p = 0.00018, and the claim is judged against that.
- The scrambled-pairs correlation in Fig. 8 has p = 0.530 in the Results and p = 0.523 in the legend.
- The Methods speak of "four continuous stimuli" but list five.
- Two confidence-interval bounds for Fig. 5 differ in the last digit between the Results and Table 2.

**Possible gaps in the dataset (for the author to check):**
- **L0 calcium events:** if the dataset lacks them, they are computed with the event-detection code the paper links.
- **Stimulus movies:** if they are not in the dataset, they come from the Zenodo deposit.
- **Stimulus names:** these may need the code's mapping from stimulus codes to names.
