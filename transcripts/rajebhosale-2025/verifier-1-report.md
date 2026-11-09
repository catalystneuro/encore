**A. Outcomes**

The claims file has 56 claims. The notebook tests 13 of them on the dandiset. It blocks 23 dandiset claims as data missing and 20 claims whose data are elsewhere.

| Claim | Outcome | Reason |
|---|---|---|
| fig1j-sgc-hyperpolarized-rmp | not_reproduced | SGCs are more negative (median −83.8 against −75.3 mV), but the Mann-Whitney test gives U = 32, p = 0.083 with 13 GCs and 9 SGCs (cell 16). Adding the missing 14th GC cannot help: at best U stays 32, and the exact p for 14 and 9 cells is then 0.053, which I computed. |
| fig1k-sgc-narrower-spike | not_reproduced | p = 0.082 under the 20 mV/ms threshold and 0.109 under 10 mV/ms (cell 18). The medians point the right way. |
| fig1l-sgc-faster-downstroke | not_reproduced | p = 0.35 under both readings, which give identical values in all 48 cells (cell 20). The readings agree, so the criterion's "blocked" branch does not apply. |
| fig1m-phase-plots | not_reproduced | Its criterion depends on fig1k and fig1l, and neither reproduces. |
| figs1-remaining-properties-no-difference | partially_reproduced | The cell-type half holds: no property reaches p < 0.05 under reading (a), 13 properties, or reading (b), 16 properties (cell 24). The soma-position half is blocked (data_missing). This absence carries little weight, because the same data also miss the paper's positive effects. |
| fig2i-v321l-rmp-not-different | reproduced | Welch p = 0.59 (cell 26). The "near the WT SGC median" part is only shown: V321L GC −80.1, V321L SGC −82.9, WT SGC −83.8, WT GC −75.3 mV. |
| fig2j-v321l-spike-width-not-different | reproduced | Mann-Whitney p = 0.22 under 20 mV/ms and 0.33 under 10 mV/ms (cell 28). |
| fig2k-v321l-downstroke-not-different | reproduced | p = 0.88 under both readings (cell 30). |
| fig2m-ephys-lda-wt-gc-apart | blocked (methods_underspecified) | The readings disagree (cell 34). In (a), on the z-scored features, WT GC is apart from the other groups and spike width has the top coefficient. In (b), on the top 9 PCs, WT SGC is the extreme group and the top coefficient is spike amplitude. The criterion says blocked when the readings disagree. |
| figs2d-ephys-kmeans-v321l-like-wt-sgc | reproduced | Both conditions hold under both readings and 10 of 10 extra seeds (cell 36). This is marginal: under reading (a) WT GCs split 4/6/2, so the largest WT GC cluster holds exactly half, the limit. |
| figs2e-pca-separation-lost | not_reproduced | The WT GC and WT SGC centroids each lie inside the other group's ellipse under both readings (cell 38). For the data ellipse d² is 1.31 against r² = 9.5, so the WT separation is absent. |
| figs2g-lda-classifier-accuracy | not_reproduced | WT pooled accuracy has a median of 55% over 100 fold assignments, range 35 to 75%, with kappa 0.12; majority-class chance is 60% (cell 40). V321L accuracy is 41.7% or 45.8% depending on scaling. Neither accuracy is within tolerance, and the WT−V321L gap of 9 to 13 points is under 15. |
| figs2f-centroid-separation-reduced | not_reproduced | The distance ratio of 0.08 or 0.14 is below one half. But neither V321L centroid lies on the WT SGC side, under the prior-including boundary or the midpoint variant (cell 42). It also depends on figs2g, which failed. |
| 12 morphology and soma-position claims (fig1f, 1g, 1h, 1i, figs1a-f, figs1g-l, 2c, 2d, 2ef, 2g, figs2b, v321l-multiple-regression) | blocked (data_missing) | I confirmed this in the archive. Every one of the 48 assets lists only CurrentClampSeries and CurrentClampStimulusSeries in variableMeasured. No positions or reconstructions are deposited. |
| 11 Golgi and FISH claims (fig2a, 3b, 4a, 4a-prime, 4d, 6a, 6b, figs9a, 9b, 9d, 7a) | blocked (data_missing) | Same archive check: the dandiset holds no imaging data. |
| 19 snRNA-Seq and snATAC-Seq claims (data elsewhere, GEO GSE280167) | blocked (other) | GEO holds raw multiome matrices covering every barcode (cell 10). It lacks called nuclei, cluster labels and fragment files, so testing would mean rebuilding the paper's pipeline. |
| figs9c-embryonic-sgc-genes | blocked (other) | The notebook makes no attempt. See problem 7. |

**B. Problems**

1. [does not affect a conclusion] The deposited cell labels differ from the paper's counts: WT has 13 GC and 9 SGC against the paper's 14 and 9, and V321L has 12 GC and 14 SGC against 10 and 15 (cells 3 and 4). The notebook states this but cannot resolve it. For fig1j I computed that one missing GC cannot bring p below 0.05, so the counts do not explain that failure. They could explain part of the other failures.
2. [affects a conclusion: figs2e, figs2g, figs2f] Cells 31 and 32 drop 4 cells whose AHP width is NaN, leaving 20 WT and 24 V321L cells. The paper's Fig S2G counts 21 WT and 23 V321L. The drop rule is from the fig2m criterion and was extended by assumption to the k-means, PCA and classifier. No variant was run that keeps the cells and leaves out `ahp_width`. The figs2g shortfall (55% against 78%) is large enough that this is unlikely to reverse it.
3. [does not affect a conclusion] In `features`, the downstroke is identical under both readings in all 48 cells. That is only plausible if the rheobase sweeps hold a single spike or later spikes repolarize more slowly. The notebook never prints the spike count at rheobase. My synthetic test showed the two readings do coincide when the sweep has one spike.
4. [does not affect a conclusion] One WT mouse, VV253, has much wider spikes and slower downstrokes than the others (GC median 2.24 ms, −30 mV/ms; cells 18 and 20). This points to a recording-condition difference in that mouse. The notebook checks fig1k without it (p = 0.112) but never checks fig1l or the multivariate analyses without it.
5. [does not affect a conclusion] The claims file says normal-theory is ggplot2's `stat_ellipse` default. That is a misreading of ggplot2: the default is `type = "t"`. The notebook follows the claims file. The WT centroids sit far inside the data ellipses (d² 1.31 against 9.5), so the outcome is the same.
6. [does not affect a conclusion] Cell 11 says GEO holds "for ATAC only a smoothed track of cut sites". The output of cell 10 itself shows 68,588 "Peaks" features in the multiome matrices. Per-barcode peak counts are therefore deposited. They would let a non-Signac approximation of figs8b (Penk locus accessibility) be run. The paper's GeneActivity method still needs the fragment files.
7. [does not affect a conclusion] figs9c is blocked as "other" without any attempt. The Allen Developing Mouse Brain ISH images at E18.5 are public, so the claim could at least be partly tested.
8. [does not affect a conclusion] The notebook's "not runnable" for the GEO claims is not one of the protocol's blocked reasons. It should be "other", or "data_missing" for the missing cluster labels.

The helper code checks out. On a synthetic cell, `features` recovered RMP, rheobase, input resistance (both readings), tau, latency, and spike width, threshold, upstroke and downstroke to within 0.01 ms or 1.5 mV/ms of the analytic values. The figs2f boundary computation agreed with `predict` on 500 synthetic points. I found no train/test leakage beyond the paper's own step of fitting PCA on all WT data before cross-validation.

**C. Not checked, and the output that would have allowed it**

- Whether any rheobase sweep holds more than one spike: a per-cell spike count at rheobase.
- Whether the multivariate results (fig2m, figs2d, figs2e, figs2g, figs2f) hold when `ahp_width` is dropped and all 22 WT and 26 V321L cells are kept: those results rerun on the 17 remaining features.
- How robust fig1l and the multivariate claims are to leaving out mouse VV253: those analyses rerun without it.
- Whether the bias current of 10 pA, or the stimulus field's "kept near −65 mV with a constant current", means the pre-step baseline is not the true RMP: per-file holding-current metadata, if any exists, or a printed bias-current check against the baselines.
- The per-cell feature table itself (the 18 features by cell, genotype and type): with it I could recompute every test independently, without re-running the notebook.
