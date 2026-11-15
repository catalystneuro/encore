I've checked `claims/peron-2015.yaml` against the paper and corrected it. The file is ready for an attempt. Nothing was committed or pushed.

**Checker result:** `claims/peron-2015.yaml: 43 claims, 42 quotes, 18 statistical values, 0 problems` (same before and after my edits).

**Changes, by claim**
- **Opening comment:** the spared whiskers listed the third mouse as D2. Table S1 gives C2.
- **Opening comment and `table-s1-roi-counts`:** the paper's two counts don't agree. The core counts add up to 89,784 ROIs, but Table S1 totals 108,374 for the same eight mice, and the paper doesn't say why. I named this as a discrepancy and gave two readings of the per-mouse count.
- **`fig3c-discriminative`:** the sentence leaves open whether the L5, GABAergic and neuropil fractions are principal-column only. The text pulled from Figure 3C settles it: the principal-column values (17%, 21%, 56%) match the Results, the surround values (11%, 13%, 23%) don't. Principal column is now the reading; all columns stays as a variant.
- **`fig3d-population-encoding`:** I widened the tolerance on "about a quarter" from 2.5 to 5 points and gave the reason. The paper's own Figure 3D numbers pool to 22%, which the old band excluded. I also named the region of the neuropil sentence as open, with both readings.
- **`discussion-principal-exclusive-classes`:** the cell count was wrong. 14,165 is the neuropil count; the principal-column L2/3 excitatory count is 13,308.
- **`fig3d-surround-whisking-dominates`, `fig7-touch-declines-surround` (the L1 test), `fig3d-touch-uniform-l5-gaba`, `fig6b-whisking-fraction-early`:** I removed the `test` field where the paper's sentence names no test. The criteria now say which test is assumed.
- **`fig4d-sample-epoch-principal`:** the L2/3 bias toward the sample epoch is judged on principal-column cells, as the Figure 4C legend says.
- **`fig4-neuropil-sample-principal`:** "spatially more concentrated" now has a stated measure, the principal-to-surround touch-fraction ratio, marked as a reading.
- **`fig6d-psychometric-improves`:** the paper doesn't say what percent correct is out of. Trials with a response and all trials are both readings now.
- **`fig7ab-salt-and-pepper`:** the Figure S6 legend draws random neurons "from the entire population". Same region and whole mouse are both readings now.
- **`figs7-direction-stable`:** the source pointed at the wrong paragraph. The Rfit > 0.25 rule is in paragraph 10 of the Model-Based Encoding Analysis, not the last paragraph.
- **`fig8h-passive-active-overlap`:** the paper states the 0.01 Hz event-rate rule for the direction index. Applying it to passive responders, or not, are both readings now.
- **`fig8jk-neuropil-anesthetized`:** the expected sign now uses the paper's own direction index, (R - F)/(R + F), giving r < 0, instead of a redefined index.
- **`fig8b-direction-tuned` and `fig8jk-neuropil-anesthetized`:** the |DI| cutoffs are marked as not the paper's.
- **`figs3d-neuropil-correction`:** the direction of the effect is marked as a reading, since the legend states none.
- **M3 (shared method):** the two bin-width "readings" were the same choice. It is now named a standard choice.

**Still open**
- The PDF could not be rendered, here or in the original run. The Figure 3 numbers I used come from the garbled extracted text, matched to panels by their cell counts. I couldn't confirm the order of the touch, mixed and whisking percentages. The values printed inside Figures 8E, 8I and 8K remain unread.
- Several pass/fail rules come from the file, not the paper: the stereotypy threshold (`fig1g-early-stereotypy`), the bin and envelope rules (`fig7ab-salt-and-pepper`), and the |DI| cutoffs (`fig8b`, `fig8jk`).
- The encoding model's penalty scale, tent knots and kernel lags (M5) are not given in the paper and could change every class fraction. All readings named in M5 have to be run.

The paper's main findings each have a claim, and every claim comes from this paper.
