I've checked `claims/simmons-2026.yaml` and judge it ready for an attempt. I changed only that file and did not commit it.

**Checker result:** `claims/simmons-2026.yaml: 39 claims, 38 quotes, 36 statistical values, 0 problems`. The first run, before my edits, also passed (38 claims, 0 problems). Every quote, p-value, n and test name matched the paper. I also opened Fig. 2, Fig. 7, Fig. S6 and Fig. S9 in the PDF, and each matched how the claims read them.

**Changes, by claim:**
- **fig1b-gabazine-blocks-gpe-ipsc (new):** the Results, paragraph 1, say gabazine blocks the optically evoked GPe currents, and no claim covered this. The paper gives no test or measure, so its criterion uses a 10% remaining-amplitude threshold, marked as a choice made here.
- **Header, M1:** the 6-min start of the stable drug window is taken from two example time courses in Fig. 7G. It is now marked as a choice.
- **fig2c:** the criterion fixed the basal rate at 0 to 2 s, which the legend does not do. It now names two readings: 0 to 2 s, or 0 to 2 s with 4 to 6 s.
- **fig3b, fig4b, figs4c, fig6c, fig6e:** the statements gave the paper's interpretations as fact ("showing", "so"). The paper says "suggesting", "arguing" or "support the hypothesis", and the statements now say the same. The figs4c statement now gives the paper's own conclusion: astrocytes release an excitatory transmitter, not GABA.
- **fig3d:** the Results cite this experiment as Fig. 3C, but the legend puts it in Fig. 3D. The source now notes this.
- **figs1:** Fig. S1 has n = 39 against 45 in the Fig. 3B legend, and the paper does not say which cells. This is now named as open.
- **fig5ab:** dividing the SNr into thirds is now marked as a choice.
- **figs6:** the paper names no test. The unpaired t test is now marked as a choice, with Welch's t test added as a variant beside Mann-Whitney; these are the paper's three between-group tests.
- **figs5:** the quote was only the table title and states no finding. The schema allows a quote or an `inferred` note but not both, so I replaced the quote with a note naming the table.

**Still open (recorded under `checks`):**
- fig4a judges "similar in magnitude" with a 10-point margin, and fig2b uses 0.5-s windows and a more-than-half-of-cells rule. The paper gives no measure for either, and both are stated as choices.
- Spike-detection settings and which episodes form the stable window are given neither in the paper nor in its code. The readings in M1 stand.

**Ready:** yes. The new `checks` entry is marked `ready: true`.
