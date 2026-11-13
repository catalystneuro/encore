I've checked `claims/brudner-2026.yaml` against the paper, the SI and the rendered figure pages, and corrected it. It is ready for an attempt (`ready: true`).

**Checker result line:** `claims/brudner-2026.yaml: 22 claims, 22 quotes, 4 statistical values, 0 problems` (the same before and after my edits).

**Changes, by claim**
- **fig1eh-snapshot-organization:** the criterion takes its outcome from two other claims but listed only one, so I added `figs1-antisymmetry-index` to `depends_on`.
- **fig1il-zscore-reliability:** the SI gives the 1500-frame window for the complex plume only. The smooth-plume window is now marked open, with two readings: frames 300 to 1799, or the first 1500 frames.
- **figs1-antisymmetry-index:** the map is the plain time average, as the Fig. S1 iii and iv panel titles and raw-unit colour bars show, not the z-score. The freestream centerline row, which the paper doesn't give, is now marked open. The per-cue scores are now reported.
- **figs1-temporal-statistics:** the comparison by medians and the 10% widening are now marked as this file's reading, since the paper gives no measure of "similar".
- **figs1fg-resolution-robustness:** Fig. S1F and S1G fix the reference map (the baseline), so the other reading is gone. The old rule wanted r ≥ 0.8 up to 8 frames, which fails on the paper's own figure (motion r is about 0.65 at 8 frames). It now asks for robustness up to 4 frames (the Discussion's "about 150 ms") and a drop at 8 and 15 frames, past the smooth plume's 15 Hz sampling.
- **figs2c-one-frame-delay:** Fig. S2C is almost flat for the smooth plume at delays 1 to 3, so the rule now allows for spread over repeats. The strict reading is still reported.
- **fig3bc-mnm-filters:** the PDF confirms the 1e-4 learning rate. I reworded "delayed negative lobe" so it can only mean a longer lag.
- **fig3e-mnm-motion-response:** Fig. 3E is back near 0.5 by ±6 frames, so the rule is now set at shifts of +1 and −1 frame.
- **fig3ij-dnm-specialization:** now reports whether the dense networks beat the minimal ones ("modestly better").
- **discussion-ten-percent-gain:** the paper's own Fig. 4 bars give gains of about 11% and 18%, so the per-plume rule failed the complex plume on the paper's numbers. It now tests the mean of the two gains (about 14% on the bars) and needs both to be positive.
- **figs4-threshold-robustness:** I read the thresholds off Fig. S4 (0.05, 0.1, then 0.2 to 0.9). Fig. S4F itself goes against the legend's "across thresholds" for the GLM agents, in both plumes. The rule now asks for every threshold for the network agents and a majority for the GLM agents.
- **fig5e-cue-betas:** turn onset is now as the SI defines it (20% of peak turn speed on the rising edge). The 200 ms gray boxes in Fig. 5D are read as the smoothing time constant.
- **figs5fh-smoothing-agent:** the quoted Results sentence compares across plumes (Fig. S5G), but the rule only tested within each plume (Fig. S5H). The statement and rule now cover both. The Fig. 2 features are the main reading for the agents' cues, since the weights 2.65 and 0.07 match the Fig. 2D smooth weights.
- **fig2b-smooth-auc and fig2d-smooth-weights:** added the paper's Yale Dataverse deposit as a possible source of the smooth plume.

All other figure-derived expected values and stars match the PDF.

**Still open (recorded in `checks`)**
- I could not check any detail the file attributes to the authors' code (frame numbers, filters, turn and position filters, the published tables), because I didn't have the repository.
- The Discussion says "fivefold" spatial range, but Fig. S1F spans 3 to 12 pixels (fourfold).
- The starting-box width differs: 112 mm in the Fig. 4 legend, ±83 mm in the SI. Both readings are kept.
- Two hedged, qualitative results have no claim: the dense-network filter shapes in Fig. 3G and 3H, and the cue-smoothing agents' success rates in Fig. S5F.

Nothing was committed or pushed. To render the figures I installed PyMuPDF into the temporary directory; nothing else in the repository changed.
