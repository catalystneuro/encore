I've written `claims/jarzebowski-2026.yaml`. The quote checker passes with 0 problems, and nothing has been committed.

**Text read:** the bioRxiv preprint (Europe PMC PPR1261135, posted 28 June 2026), with the main text, STAR Methods and the legends of Figures 1 to 7. No PDF was supplied, so no figure was seen.

**Missing from the paper:**
- **Supplementary figures:** the legends of Figures S1 and S2 are absent; the text has the heading and nothing under it. Earlier files in the registry went ahead in this situation, so I did too. The five claims on S1 and S2 rest only on the Results sentences that cite them, and their tests are read from the general Methods.
- **Code:** the linked repository, github.com/bendor-lab/SETA-model_allen_analysis, is not public (404); the paper says it "will be made available on publication". No code was read, so every method comes from the Methods and legends.

**Claims:** 30, all with quotes, none inferred.
- 14 are simulations of the paper's model (Figs 1 to 4). They are `data: elsewhere`, since the model is fully specified in the Methods but its code is not public.
- 16 use the recorded data (Figs 5 to 7, S1, S2). They are `with_inputs`, because layer labels need the CCFv3 brain atlas annotation.
- 13 claims carry statistics, 45 values in all. 12 claims have expected values, mostly the paper's 95% confidence intervals plus the cell and recording counts.
- 30 claims have criteria. Four are claims of absence, judged on the paper's own test: Fig 5C L2/3 slope, Fig S1F, Fig S2 and Fig 7C.

**Details the paper leaves open, with the readings named:**
- **O1, responsive test:** one-sided or two-sided Wilcoxon, and which presentations enter it.
- **O2, firing rate used for the unit filters:** the whole-session value or the active-task value.
- **O3, optotagging z-score baseline:** a pre-pulse window or the block mean.
- **O4, burst fraction per cell:** pooled over windows or the mean of per-window values.
- **O5, spontaneous windows:** all 250 ms windows or stationary windows only.
- **O6, square-root transform:** for the figures labelled only "Mixed-effects model", a raw change or a change on square-rooted burst fraction.
- **O7, locomotion window:** 250 ms or 750 ms.
- **O8, Fig 5 repetitions:** whether presentations right after an omission are kept.
- **Per claim:**
  - Fig 5C: the coding of repetition in the model. The printed degrees of freedom imply repetitions 2 to 8, seven per cell.
  - Burst-fraction change: a difference or a modulation index.
  - Fig 7C/D: how the 47 L2/3 and 658 L5 cells were selected.
  - Fig S1 novelty: which layer.
  - Fig S2: the test and the trial filtering.
  - Fig 1D: the reference time for the 15 to 20 ms delay, since the model has no L5 ET neuron.
- **Model claims:** the simulation time step, the plotting ranges and the thresholds for "same" or "not substantially" are named as choices made here, because the paper gives none.

**Inconsistencies in the printed statistics:** the Fig 5C L5 slope is printed as t = 8.1 (positive) with a negative CI. The L2/3 slope is printed as t = -0.59 with a CI centred above zero. Both are recorded as printed and flagged in the file header.
