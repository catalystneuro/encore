**Checker result:** `claims/asari-2009.yaml: 21 claims, 19 quotes, 2 statistical values, 0 problems`. It passed before my edits and passes after them.

**Changes, by claim** (each is recorded with its reason under `checks`):
- **fig2-example-long-context:** `n` said 6 trials in each of three contexts. Figure 2A gives 6 repeats for one context only, so I corrected `n` and the rule for matching the example cell.
- **fig3a-proportion-significant:** Added that the intersequence silences are not probes; the Methods leave them out of Figure 3.
- **timescale-longer-than-membrane:** The criterion said the paper names the intersequence intervals as the source of spontaneous activity. It does not, so that is now named as open. The main reading uses the whole interval; a variant drops its first 1 s.
- **fig4-predictability-upper-bound:** The quantity label said "1 minus alpha1". With alpha1 = -0.49 the value is 1 + alpha1, so I made the label agree with the criterion and the legend.
- **fig4-strf-performance-low:** The paper names no test for this claim of absence, and the protocol judges absence on one test, not on several readings. I fixed one test as an assumption: a paired one-sided Wilcoxon on validation performance, 4052 ms against 180 ms, at 0.05. The Friedman test is shown as a variant. It is now named as open whether "20%" means the validation or the training estimate.
- **fig5-example-conductances:** The sign of the 12 mV liquid junction potential is garbled in the text. The criterion had fixed it at -12 mV; both signs are now readings. The decay of the conductances within about 100 ms, which the statement claims, is now reported.
- **fig8a-proportion-by-property:** Removed the order of the proportions from the condition for "reproduced". The paper reports counts, not an order. The order still applies for "partially reproduced".
- **fig8a-significance-fits:** Removed the rule that 8 of 10 values within tolerance is enough, which the paper does not give. All 10 must now be within tolerance.
- **fig7-example-frequency-context:** The 3 s cutoff for "about 4 s" had no reason given. It is now 3.6 s (4 s less the default 10%).
- **fig9-example-first-bin:** Said that the factor of two is this file's reading of "substantially different", not the paper's.
- **figs1-silence-probe:** The Methods' "within about 1 s" refers to response power, but the criterion tested the proportion of significant probes. It now tests power: Eq. 17 over silence probes, with Eq. 19 as a variant.

**What remains open:**
- The online supplement (Figures S1 to S10) was not supplied, so figs1-silence-probe is written from the Methods only. The main findings do not depend on the supplement.
- I could not render the PDF either, because no PDF renderer is installed here. Garbled symbols ("~", "<" or ">", the sign of the junction potential) are read from context.
- Several grading thresholds are the file's own choices where the paper gives none. Each criterion says so or gives a reason.
- One side remark has no claim: the paper says the STRFs showed no distinct structure longer than several hundred milliseconds. It is not a main finding.

The paper's main findings all have claims, and nothing comes from outside this paper.

**Ready:** yes (`ready: true`). Only `claims/asari-2009.yaml` was changed; nothing is committed or pushed.
