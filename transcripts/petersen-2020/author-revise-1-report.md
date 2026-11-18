I've worked through every point in the round-1 report and re-run the entry. `python tools/entry.py all entries/petersen-2020` passes with 0 errors and the notebook runs in 27 minutes. A repeat run gave the same numbers, and the conclusions, summary, README and attempt record match them. Round 1 is recorded under `verifications`, and nothing is committed.

**Outcome changes** (now 17 reproduced, 19 partially reproduced, 8 not reproduced, 2 blocked):
- **fig4d-precession-slope-decrease: not reproduced → partially reproduced (assumed).** The verifier was right that the slope search was capped at ±1 cycle per field. On the full data that cap pinned 28–32% of slopes at the limit. The search now runs over ±2 cycles per field, stated as an assumption, with ±1 and ±3 shown as variants and the share at the limit printed (8–10% under ±2). Under ±2, precession is flatter during cooling than before (P = 0.016) but not than after (P = 0.073). No reading makes both comparisons significant. A new finding asks the paper's authors what range they used.
- **fig5cg-compression: not reproduced → blocked (methods_underspecified).** The new output shows the surface fit doesn't describe the data. Every fit that converged did worse than a flat surface (R² from −0.10 to −5.1). The smooth outline alone, without the oscillation, explains a median R² of 0.41–0.68 per session. Every failed fit hit the evaluation limit. The paper gives no fitting procedure that would make the fit work. The variants, which aren't the criterion's measure, show no decrease with cooling (for example the per-session ridge slope, P = 0.62).

**Added output, no outcome change:**
- **fig3f (information):** the verifier suspected the pre-to-post drop came from unequal trial counts. With trials subsampled to equal numbers per state, pre to post still falls (P = 0.016), so it stays not reproduced.
- **fig5d (cross-correlogram period):** measured as the spacing between peaks, the period is 107.2 ms (103.5 ms with the other pairing), still outside 85 ± 8.5 ms.
- **suppl1g (waveforms):** with waveforms interpolated to 200 kHz, the latency change is +0.035 ms (P = 3e-11, significant in all 4 sessions). Spike counts per condition are now printed.
- **suppl5gh (rates and temperature):** normalised rates have medians below pre (one-sided test significant) but means above pre. The outcome still rests on raw rates.
- **fig5h (time lags):** stays partially reproduced. It rests on the main signed-rank test, not the rank-sum variant.
- **Bad theta channel (MS13-171130):** fig2i, fig6c, fig6h and fig5i are also shown without that session, and each keeps its outcome.
- **Temperature check:** the notebook now prints the correct 5–45 °C range. No sample inside any trial falls below 15 °C, so the 5 °C and 10 °C sensor-limit values never enter a trial temperature.
- **Text fixes:** the claim that at least half the sessions contribute across the whole aligned window is corrected (11 sessions at the ends against 31 near onset). The notes for fig2h, disc-12, fig6h and fig4f now say how much each outcome depends on the reading chosen.
- **suppl3e:** the measured value is now −0.0262 under the new slope range. The outcome is still partially reproduced.

**Not done:**
- The verifier gave no outcome for suppl2d-interneuron-oscillation-slows (its table has 45 rows for 46 claims). I recorded no result for it and said so in the `reviewed` text.
- I added no reader question, because the report found no place where the claims file misreads the paper.
- I left the session-set point (problem 12) and the absence of chance levels (problem 14) as they were, since neither needed a change.
