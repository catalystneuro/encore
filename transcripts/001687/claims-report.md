I wrote the claims file at `claims/001687/10.1016-j.neuron.2026.05.027.yaml`. The quote checker passes: 41 claims, 41 quotes, 39 statistical values found, 0 problems. Nothing is committed.

**Text read.** The accepted author manuscript from PubMed Central (NIHMS2191201 / PMC13336321), fetched 2026-10-20. It has the main text, the STAR Methods, the legends of Figures 1–6, and the supplement PDF, which holds the legends of Figures S1–S6 and Tables S2–S5. I did not read the version of record or open any figure.

**Code read.** github.com/wanglab-neuro/2026_Xiao-Severson_Peri-head-distance at commit b1a9f3c (Zenodo doi:10.5281/zenodo.20330279). I read the MATLAB scripts behind Figures 2–6 and S1, the NWB helper scripts and the circuit model. The helpers show the deposited NWB files are meant to carry the paper's own unit labels (wall_responsive, wall_tuned, tuning_type and so on). I did not read the spike-sorting submodule.

**Claims.** All 41 have quotes; 19 carry statistics, 33 have expected values and 41 have criteria.
- They cover the awake vs anesthetized whisker video (S1), the tungsten recordings (S2) and the silicon-probe unit counts and categories (Fig 2F).
- Firing-rate comparisons (S4A–C), preferred distances, the half-split stability check, unit depth and the three time windows each have a claim.
- Population decoding has claims for overall accuracy, per-distance accuracy, error, the single-neuron decoders and the SVM check (Figure 3, S5, Tables S2–S4).
- Whisker cutting has seven claims: baseline, wall firing, per-unit changes, map and proximity units after the cut, decoding, and the unit total.
- Also covered: the GtACR opto experiment, the TeLC claims (kinematics, unit yield, preferred-distance shift, category shares, firing rates, Table S5) and the circuit model.
- The model claim is marked `data: elsewhere` and is run from the repository. Seven claims of absence are each judged on the paper's own test.

**Details left open, with the readings named:**
- **Responsiveness correction.** The Methods print only "p < 0.05"; the code applies BH-FDR across distances. I followed the code and named uncorrected as the variant.
- **Decoding cross-validation.** 10-fold in the Methods (main reading) against 15 splits in the code (variant). The code also z-scores the features, which the Methods don't mention; I followed the code.
- **Decoding window.** The text says "sustained period" while the Methods, code and Table S2 use 3–11 s. Readings: 3–11 s and 4.5–9.5 s.
- **S4B baseline.** Readings: the baseline of the passes at the same distance, or over all passes. The paper's 6.36 sp/s differs from the 5.46 sp/s it gives for the all-pass baseline.
- **Wall firing in whisker cutting.** Median over distances (code) or mean over passes (Methods).
- **Per-unit cutting tests.** Three corrections appear: uncorrected (Results), BH-FDR (Methods and code), Bonferroni (Methods and code). Two pass sets in the code.
- **After cutting.** Whether "remained tuned" requires activation; how a gain change is measured.
- **Tungsten categories.** The silicon-probe rule, or preferred distance alone.
- **Opto bootstrap.** The CI level and what is resampled.
- **TeLC "untuned".** The 177-unit untuned group of Figure S4, or Table S5's 550 and 294.
- **Z-test denominator.** Wall-responsive units or all units.
- **Fig 5D population.** Activated and tuned, or activated only (the code's mask).
- **Temporal windows.** Whether responsiveness is re-tested in each window.
- **Descriptive claims.** Where the paper reports no test (bending, stability, depth, tuning shape), the criteria use pairs of summaries, such as median and mean, and require both to agree.
- **Model.** The code is run, since it adds local terms the Methods' equations don't write.

**Inconsistencies in the paper,** recorded in the file:
- 472 + 213 − 29 = 656 tuned units implies 184 suppressed-only and 112 untuned, but Figure 2F gives 119 and 177.
- The Figure 4B legend gives ± 2.986 where the text gives ± 1.338.
- The Figure S6J legend prints p = 3.98×10⁻³ where the text prints 3.98×10⁻⁵.
- The Methods call the ± on firing-rate comparisons a bootstrap CI, while the legends call it SEM.
- Figure 3C plots SEM while Tables S2–S3 give 95% CI.
- In the code as read, the combined map + proximity decoder group does not use the 36 + 82 subsample. The claims follow the Methods.

**Missing.** Table S1 (mouse sex, age and figure assignments) and Table S6 (test statistics, degrees of freedom and p-values for all analyses) are named but not in the supplement file. No claim needed them, since every number used is in the text, the legends or Tables S2–S5, so I went ahead. The cost is that the opening comment cannot give subject sex and age, and no degrees of freedom are recorded.
