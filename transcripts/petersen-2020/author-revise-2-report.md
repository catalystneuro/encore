I answered every point in the round-2 report. No outcome changed and I proposed no changes. The entry re-ran cleanly with `python tools/entry.py all entries/petersen-2020` (passed, 1365 s), and `check` reports 0 errors.

**Outcomes:** all 46 stay as the verifier agreed: 17 reproduced, 19 partially reproduced, 8 not reproduced, 2 blocked.

**Outputs the verifier asked for:**
- **fig5cg:** I added a bounded least-squares fit. It holds b within 30% of the summed period and starts from the envelope's own fit and from several values of a. It does no better than before: pooled R2 is -0.14 to -5.8 against 0.57 to 0.80 for the envelope alone, and none of the 46 per-session fits reaches the envelope. The density's theta modulation is small (4 to 7% of its level), while the equation's oscillation term takes the density to zero between ridges. The claim stays blocked as `methods_underspecified`. The reason now says the fit fails, and that the paper does not say how the density was prepared for the fit.
- **fig3f:** I added information with equal spike counts per state and a shuffle-corrected version.
  - With equal spikes, pre to post still falls (P = 0.032).
  - Shuffle-corrected, no comparison is significant (P = 0.085).
  - The outcome stays not reproduced, because the claims file names uncorrected Skaggs information. The notes now say that part of the fall is a difference in bias between states.
- **fig5h, fig5j, fig5k:** I added tests over sessions as variants.
  - fig5h: under lag reading (a), cooling lags are longer than pre and post (P = 0.014 and 0.012) and pre and post do not differ (P = 0.98).
  - fig5j: pre against cooling gives P = 1.0.
  - fig5k: still fails per session (P = 0.0047 and 0.0059).
  - The outcomes stand because the claims file fixes the test over pairs and over cycles.
- **fig4d:** The conclusion, notes, README, Summary and finding now say the result depends on the slopes at the search bound. Without those slopes no comparison is significant, and with a 3-cycle range the significant comparison is against post, not pre.

**Corrections:**
- **Tracking rate:** I withdrew this `metadata_error` finding. Printed per session, each behaviour description matches its timestamps (120, 40 or 30 Hz).
- **Temperature finding:** It now cites the raw values printed in the data check (-1751 to 1354 C, 11 sessions).
- **Numbers now printed:** the theta values of the 2018-07-19 sessions and the second cooling intervals of MS12-170717 and MS12-170718.
- **Sentences fixed:** the ones the verifier quoted in cells 26, 60, 77 and 93, the suppl1g P range, the fig5h notes, and the README sentences on Figure 3 and on phase lags.
- **Round-1 record:** I moved problem 12 from fig5-speed-control-cooling to fig5d, where it belongs.
- **Round 2 record:** Recorded under `verifications` for all 46 claims, with the verifier's reasons in its own words and my responses.

**Not done:** I added nothing to `questions/petersen-2020.yaml`, because the report names no place where the claims file misreads the paper. Its points about the fig5d session readings and the fig5i lag reading are about the analysis, not the claims file. Nothing is committed or pushed.
