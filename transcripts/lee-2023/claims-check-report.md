I checked the claims file for DANDI:000636 against the paper and corrected it. It is ready for an attempt, with three problems left open (below). Nothing was committed or pushed.

**Checker result:** `45 claims, 44 quotes, 12 statistical values, 0 problems`. It was 39 claims before the six I added.

I also read the paper's code (AllenInstitute/human_patchseq_gaba at commit 5eb357a) to check the notebook details the criteria cite. Its feature table has 93 feature columns, 9 of them chirp.

**Changes, by claim**
- **Header and figs2b-wfdc2-ephys-43-of-84:** Counting all 93 columns is no longer a reading that can decide the outcome, because the paper counts 84 features and only the 84 non-chirp columns match. The 93-column count is kept as a variant.
- **fig1c-marker-expression-correlated:** The file named the test as Pearson, but the paper names no test. The test, expression scale, pooling across subclasses and source of the 25 genes are now listed as open readings.
- **figs1-microglial-signature:** "Less pronounced" can now mean either a lower fraction of acute cells or lower signature expression.
- **fig1i-wfdc2-ephys-umap-overlap:** Removed the requirement that 80% of neighbours be PVALB cells. The paper says "PVALB-rich" about the morphology UMAP (Fig. 1H), not this one. The thresholds are now marked as choices.
- **fig2f-ap-kinetics:** The direction was wrong. The ratio is peak upstroke over peak downstroke (Methods), so the fastest kinetics give the lowest upstroke/downstroke ratio, not the highest.
- **fig4c-calb1-ephys-by-morphology:** "Adaptation ratio" is now the Methods' ISI adaptation ratio. The Methods call `adapt_hero` the adaptation index, so it is a variant only.
- **fig4d-calb1-genes-by-morphology:** The criterion followed the notebook alone. The Methods (pairwise FindMarkers, 30 PCs) are now the main reading and the notebook (FindAllMarkers, 6 PCs) a variant. The UMAP covers all SST CALB1 neurons, as the legend says.
- **fig3-frzb-transcriptome-intermediate:** The statement now includes that SST FRZB neurons also express several other key genes of each subclass. The SST versus PVALB comparison is placed in the snRNA-seq data (Fig. 3A legend), and the thresholds are marked as choices.
- **fig3g-frzb-morphology-like-pvalb:** The co-clustering choices are now named: the tree is cut at six clusters, the feature set is stated, and 10 and 20 graph neighbours are both run. The criterion notes that the preprint gave P > 0.05 for this panel while the version of record gives P < 0.01; it follows the version of record.
- **fig5b-merfish-layers:** Added a test for the axon-peak part of the statement, which the criterion did not cover.
- **figs7a-dbc-markers:** The cut for "strong" CALB1 expression is marked as a choice the paper does not give.
- **figs5-vip-enhancer-enrichment:** Dropped the "more than half are VIP" requirement, which the paper does not state. Enrichment is now judged against two possible comparison groups with a Fisher test marked as a choice.
- **Six new claims** for Results findings that had none:
  - `figs1a-genes-across-days`
  - `fig1e-wfdc2-transcriptome-overlap`
  - `fig1h-wfdc2-morph-umap-overlap`
  - `figs1de-mapping-unaffected`
  - `fig2a-patchseq-overlaps-snrnaseq`
  - `fig5d-dbc-morph-umap`

**Still open**
- **Supplement missing:** The supplement of the version of record is not under `paper/`. So the tests for figs. S2C, S5, S6, S7B, S8B and S9 are read from the main text and the preprint, and the features plotted in Fig. 2H and fig. S8B are not named anywhere. If the supplement is supplied, these claims should be checked again.
- **UMAP claims:** These judge visual findings with neighbour measures and thresholds the paper does not give. They are marked as choices.
- **Sweep choice:** No text says which sweep supplies AP width, upstroke/downstroke ratio, peak and latency. Each claim lists the possible sweeps and is blocked when they give different results.

**Ready:** yes. The `checks` entry is added with `ready: true`.
