The claims file is ready for an attempt. I made ten corrections, and the checks entry records `ready: true`. Nothing was committed.

**Checker result** (the same before and after my edits): `29 claims, 29 quotes, 82 statistical values, 0 problems`

**Changes, by claim**
- **fig1g-com-corrective:** I reworded the criterion. It now says the initial choice would have been rewarded when the initial arm is the next arm of the sequence. The old wording read as if that defined the initial arm itself.
- **fig1g-com-matches-run-through:** The criterion repeats the test over 100 random draws of nearby trials but never said how those draws decide the outcome. It is now judged on each rat's median p-value over the draws, labelled as a choice the paper does not make.
- **fig1h-final-choice-less-switching:** The sign tests required three rats. The Figure 1H legend reports four (E, J, K, L) for both the initial and final ratios against 2, so four are now required.
- **fig3b-distance-predicts-com:** I removed the fallback "p < 1e-10 with a smaller sample". The paper gives no such threshold.
- **figs7b-no-swr:** If every row is one of the three conditions, the condition and rat indicators are collinear. I noted this and added a third reading: the pseudo-inverse fit that statsmodels OLS uses by default.
- **figs11b-theta-cycles-correct:** The S11B(d) legend does not say whose theta cycles are counted. The criterion had fixed "either kind"; it now names two readings, either kind, or the two kinds as separate predictors.
- **figs11a-more-representations-over-days:** The statement says "in all five animals" but the criterion tested only the pooled model. I added a per-rat direction check and say that the paper gives no per-rat test.
- **fig4c-home-with-other-content:** The criterion required two significant rats per panel. The legend reports three in each (p < 0.01 in panel a, p < 0.05 in panel b), so three are now required at those levels.
- **figs8-late-theta-phase:** The criterion used only the phase at event onset. The Methods analyse 4 ms bins over 60 ms either side of onset, weighted by content. Both readings are now named, and the MUA-derived theta is cited to the Figure S8 legend.
- **figs10-theta-power-and-cycle-length:** The theta source was listed as open, but the Methods settle it: corpus callosum LFP for every theta analysis except S9 and S11. That is now the main reading, with MUA-derived theta as a variant.

**What remains open**
- **Per-rat reward sequence:** The Results and the Figure 1B legend agree with each other but conflict with the Figure S1E label for rat E. The reward log has to decide, as the file's opening comment already says.
- **Event counts:** The Figure 4E counts differ from the Figure 4A remote counts. The S11C counts also differ from the Figure 4A totals for rats J, K and L. The paper explains neither.
- **Repeated estimate:** Figures 4A(b) and 4B print the same estimate and interval (1.50, 1.18 to 1.90). Both claims keep them as printed.
- **Supplementary results without a claim:** S4, S5, S9 and S12 are supporting results, not main findings, so I added no claims for them.

All the main findings have claims, and every claim comes from this paper.
