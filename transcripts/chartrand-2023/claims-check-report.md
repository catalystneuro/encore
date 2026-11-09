The checker's result line is `39 claims, 39 quotes, 24 statistical values, 0 problems`, both before and after my edits. The file is ready for an attempt (`ready: true`).

I checked the criteria against the paper's Methods, legends, Table S2 and its linked code (github.com/AllenInstitute/patchseq_human_L1 at 7777857), cloned to a temp folder. Only the claims file was changed, and nothing was committed.

**Changes, by claim**
- **Opening comment and patchseq-counts:** Table S2's 194 counts only cells of the ten L1 t-types. The primary set alone also holds cells of non-L1 t-types. The count is now restricted to L1 t-types.
- **fig1a-human-types-separated:** the criterion pointed at Fig. 6C, which is patch-seq d' at the subclass level, not the reference d'. It now uses the Methods' d' on the reference data, and the comparison is named as the reader's reading, since the paper gives no measure for this contrast.
- **fig1e-subclass-proportions:** the cell populations and categories now match the code (human cells with soma in L1, border cells left out; mouse cells in layer 1; "other" and "deeper" t-types as their own categories).
- **fig2c-subclass-ephys-differences:** the code runs pairwise Mann-Whitney post hoc tests where the Methods say Dunn's. Dunn's is kept and the code's choice is shown as a variant.
- **fig2c-lamp5-gradient:** the direction is now judged by the sign of the paper's Spearman correlation. Before, it was "highest/lowest" with no measure named.
- **figs6-donor-condition-ephys:** added the notebook cells for sex and age, which were missing. Also added the code's dropout filter in the age test, and noted that condition, sex and age come from Allen-internal donor records, with the public table's columns standing in.
- **figs6c-region-ephys:** added the code's two manual relabels of brain region.
- **fig3d-ephys-species:** the Fig. 3D legend says Dunn's while the Methods and code use Mann-Whitney. Mann-Whitney is kept and Dunn's is shown as a variant.
- **fig3e-tea-validation:** the legend selects features by effect size against mouse TEa, the code against mouse visual cortex. Both are now readings. Also added the transcriptomic QC filter the code applies to mouse visual cortex cells.
- **fig3f-a-type-conductance:** the statement now says only mouse LAMP5 cells were sampled, as the legend states.
- **fig4b-adarb2-irregular-firing:** "faster sag" was judged on time to sag peak alone. The sag time constant (Table S1, "rapid time constant") is added as a second reading.
- **fig4d-mouse-no-rosehip-ephys:** the outcome accepted either reading of "no irregular spiking", which breaks the protocol's rule. It now needs both readings to agree, and is `methods_underspecified` when they don't.
- **fig6b-dprime-correlation:** the Methods give 5-fold cross-validation and the code uses 4 folds. Both are now readings.

**Still open (recorded in `checks`)**
- **fig5d-mouse-pax6-doublets:** the paper reports no test. Comparing the Lamp5 Krt73 medians against every other mouse subclass is the reader's choice; the legend's pairwise Dunn's tests have no reported results.
- **fig3g-variability-dimensions:** the paper sets no threshold for "similar amount of variability", so that part stays reported and outside the outcome.
- **Cross-species ANOVA (open detail O2):** the code fits the model with a heteroskedasticity correction but then runs the ANOVA without the option that applies it. Whether its p-values carry the correction the Methods name is not settled; both existing readings stand.
- **Coverage:** a few minor morphology and reference-data findings have no claim (Figs. S3B, S3F, S2B to D). All of them rest on data outside the dandiset. Every main finding has a claim, and all claims come from this paper.
