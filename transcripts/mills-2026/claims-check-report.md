I checked `claims/mills-2026.yaml` against the paper and edited only that file. Nothing is committed.

**Checker result** (re-run after my edits): `claims/mills-2026.yaml: 48 claims, 47 quotes, 83 statistical values, 0 problems`. Before the edits it gave 46 claims, 45 quotes and 0 problems.

I also checked the criteria that cite the paper's code against the repository at the cited commit (1fee26d). The 50 Hz unit filter, the trajectory PCA, the decoder settings and the selection for the trial-pair analysis match what the file says.

**Changes, by claim**
- **fig1j-ast-drd2-enriched:** removed the reading that leaves out the nuclei expressing both receptors. 71% and 26% add up to 97%, and the legend counts the dual-expressing nuclei as a third class, so only the reading that includes them fits.
- **fig1l-rnascope-drd2-enriched, figs4-cdh6-slit2-gradient:** added criteria, since neither claim was settled by its expected values. Puncta thresholds, the tests on per-animal log-ratios, and ANOVA with Tukey come from the Methods and legends. The file now says which details are open (how cells are pooled, the eighth region nobody names) and which are this file's reading (the order of means that stands for the gradient).
- **fig2e-ast-sustained-clusters:** cutting the tree into seven clusters and the "sustained" thresholds were written as if fixed. The paper gives neither, so they are now marked as choices, with eight clusters as a variant.
- **fig2o-region-differs-cs-reward:** marked the one-sample t-test as a choice made here, since the paper gives no test for it, and added n.
- **fig2q-trajectories-diverge:** the code's PCA (paired animals only, 90% of variance) was the main test. The Methods say one PCA over paired and unpaired animals, with distance measured in the complete component space. The protocol says the Methods come first, so they are now the main test and the code is a variant. The baseline threshold is marked as a choice.
- **figs8-single-trial-divergence, fig3h-cs-decoded-paired-only:** added a note that with 3 unpaired animals the test cannot reach p < 0.05. That part of each claim can never fail. The figs8 note also says the animal selection comes from code that only plots example pairs.
- **fig3j-cs-encoding-glm:** the Methods call the CS permutation p-value two-sided but write a one-sided formula. The code uses absolute values, so it is two-sided, and the file now takes that as the main test with the formula as a variant.
- **figs10-high-defensive-mice-greater-responses:** the tolerance on mouse counts was 0 with no reason given. It is now 10% (0.8 and 0.7), which still requires the exact counts.
- **fig3b, fig3c, fig4eg, fig6e:** added criteria from the legends and Methods. The open-field freezing scoring is not given in the paper, and the per-mouse measure for fig6e is open; both are named.
- **figs16-drd2-inhibition-freezing-darting:** added the four group means as expected values, with the legend's SEMs as tolerances, and a criterion.
- **fig6f, fig6g-j, figs17:** added n from the legends.
- **New claims:** figs2-ast-many-degs (the many differentially expressed genes in ASt neurons, using the GEO data) and figs12gh-activation-no-epm-effect (activating Drd1a+ or Drd2+ neurons does not change open-arm time).

**Still open**
- fig2-recorded-neurons is a link claim written by the reader, and the protocol gives link claims to the author. I kept it because other claims depend on it and it only checks the paper's own counts.
- Figures S15L-Q and S11B-C have no claim. Both are secondary.
- figs2-ast-many-degs reads "hundreds" as at least 200. That threshold is this file's reading, not the paper's.

**Ready:** yes. The last entry under `checks` records `ready: true`.
