I checked the claims file against the paper and made eight corrections. The file is ready for an attempt, with three open problems noted below. Nothing is committed.

**Checker result:** `claims/grosmark-2016.yaml: 36 claims, 35 quotes, 21 statistical values, 9 problems`. The file passes schema validation and every quote is word for word. The 9 problems are p-values printed only inside supplement figure panels, which the checker can't find in the text; one of them (3.94e-06) is in the text but written as "3.94 x10-06". I rendered the supplement pages and every value the file says it read from a panel matches (Figures S5, S6, S9, S13, S14, S16 to S19).

**Changes, by claim**
- **figs5e-duration-unchanged:** this is a claim that nothing changed, which must be judged on the paper's test alone, but it passed if either of two event sets gave that result. It is now judged on the events of the replay analysis, which Figure S5 is about; all ripple events are a variant.
- **fig3a-plastic-specificity:** Figure S19E, where the criterion took its measures and significance marks, leaves out the 26 PRE-only cells. The claim is now judged on all rigid and plastic cells, as in Fig. 3A, with S19E as a variant.
- **fig3b-plastic-improve:** the measure was taken from Figure S19F as if it were Fig. 3B's. The Fig. 3B legend and Figure S13C allow other readings, so it now has three readings (a, b, c), and the S19F subset is noted.
- **fig4a-rigid-faster:** added the MAZE medians (1.09 and 1.13 Hz) that the statement quotes but `expected` lacked.
- **figs14-plastic-ripple-gain:** the PRE and session-wide tests were recorded but never used. I added their medians to the statement and `expected`, and required both tests.
- **figs16ab-plastic-synchrony-increase:** the p < 0.023 in Figure S19G comes from the subset without the PRE-only cells. Noted, and that panel is now a variant.
- **figs17-coactivity-preservation:** the paper says PRE-to-RUN coactivity was "weakly but significantly preserved"; added that test.
- **fig4c-pre-fast-coactivation:** noted that Figure S16B shows a significant increase for high-rate cells, which conflicts with "remained unchanged".

**Still open** (recorded in `checks`)
- The three fig4c claims use Spearman and signed-rank tests the paper never names. The fast-cell "unchanged" part may fail under them.
- The test for strongly contributing cells is a rank-sum test in the Methods but a signed-rank test in the Figure S19B legend. Both readings stay in the file.
- Ripple participation and within-ripple "on" rate (Figure S14) have no claim. The main "ripple-related spiking" finding is covered by the gain claim.

**Ready:** yes (`ready: true`). Only `claims/grosmark-2016.yaml` was edited.
