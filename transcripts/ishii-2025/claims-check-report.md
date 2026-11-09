The claims file is ready for an attempt. I added a check entry with `ready: true`; nothing is committed.

**Checker result:** `27 claims, 27 quotes, 75 statistical values, 5 problems`. Every quote matches and the file is valid. The 5 problems are p-values the checker failed to find: 0.001035889, 0.65234375, 0.027281171, 0.002659548 and 6.8e-05. I found each one in the legends of Figures 1G, 1J, 1-figure supplement 2B, 6C and 6K. The checker misses them because it only tries numbers rounded to 6 digits, and it doesn't try the trailing zero in "6.80E-05". The same 5 were flagged before my edits.

I also read the paper's code at the cited commit 4e98c43. The Figure 2 method notes match it.

**Changes, by claim**
- **fig1s1-experience:** the statement said virgin females make *fewer* isolation-zone entries. The paper never gives the direction of that difference, so the statement now says only that it differs. The criterion now names the pre-ejaculation part of the session, which is what the code compares, and requires the entries difference to be significant.
- **fig1nt-natural-estrus:** added the mounting and intromission tests (Figure 1R and 1S) to the statistics and the criterion.
- **fig2s-dorsal-raphe:** removed a "..." in the quote where the paper's sentence is continuous.
- **fig3d-mpn-fos:** the measure is now stated as the per-mouse proportion of Fos+ cells averaged over sections, as the code computes it.
- **fig4h-response-magnitude:** added the anogenital sniffing, self-grooming and intromission tests. Anogenital sniffing, which the statement names, is now part of the criterion. Self-grooming is reported but left out of the outcome, because its sign contradicts the Results sentence.
- **fig4i-ejaculation-responders:** added the expected sniff counts (29 and 1), an outcome rule, and a dependency on fig4h.
- **fig5-ejaculation-specific:** the criterion described the code wrongly; `*_only_cells` are values of the `magnitude_cell_types` column, not separate columns. Corrected that reading.
- **fig5c-class-selectivity (new):** Figure 5C had no claim. The legend's last line names a Student's t-test, but the reported values and the code use ANOVA with Tukey's HSD. The claim follows ANOVA and Tukey and states the conflict.
- **fig6c-decay-length:** added a dependency on fig4i for its 184 and 35 cells.
- **fig6k-late-cluster-vgat:** the "cosine metric" applies only to the silhouette score, not to the clustering. Also added:
  - the code's whitening, search ranges and rule for the number of components;
  - the chi-square test with Bonferroni correction;
  - the fast-responder part of the statement;
  - an expected count of 37 Vgat cells;
  - that the code fixes no random seed, so cluster membership may vary between runs.
- **fig7s1-mpn-proportion:** added the panel G tests of Vgat against Vglut2. The legend doesn't name which test G uses, so the criterion says so. It also names two readings of which mice the 0.76 and 0.15 are taken over.
- **fig7s3-inhibition:** for the self-paced assay, the criterion now treats the legend's rank-sum test as the main reading and the code's paired signed-rank test as a variant, as fig7fg already does. For the home cage, it names the uncorrected two-sided Mann-Whitney U test.

**Still open**
- **fig2-density-link** was written by the reader, but the protocol gives link claims to the author. I left it in place; its thresholds are the registry's, not the paper's.
- **fig2c-brain-wide-increase:** the thresholds for "brain-wide" (80% of regions higher, half significant) are the reader's own. Supplementary file 2, which lists the significant regions, isn't in the text.
- Two secondary results have no claim: the pup-care tests in Figure 7-figure supplement 2, and the TRAP accuracy and efficiency tests in Figure 7-figure supplement 1I to 1L.
