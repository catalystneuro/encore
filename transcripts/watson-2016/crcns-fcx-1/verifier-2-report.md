**Round 2 verification: Watson et al. 2016 on CRCNS fcx-1**

The claims file has 41 claims. The attempt record has 41 outcomes: 15 reproduced, 14 partially reproduced, 12 not reproduced, none blocked. Ten are marked `assumed: true`. The README, the notebook summary (cell 138) and the record agree on every outcome.

**1. Outcomes**

I agree with all 41 recorded outcomes. Several hold only narrowly:

- **fig5b-wake-between-packets (partial):** In round 1 I disagreed. I now accept it, because the record states the assumption (motion z-scored per session, which is what the data description says) and says the result rests on 7 triplets (cell 122, R 0.869, p 0.011). It is still thin: reading (b), with 43 triplets, shows no correlation (p 0.11).
- **fig3f-within-up-changes (reproduced, cell 77):** This rests on M2 reading (b), and the parts use different units.
  - The sextile tests use one entry per cell and cycle (slowest p 0.047).
  - The pI test uses one entry per cell (p 0.045).
  - pI per cell and cycle, and M2(b) per cell, are not printed.
- **fig3e-wake-before-after-sextiles (partial, cell 83):** 3 of 4 holds only under M2(b). Under M2(a) it is 2 of 4, which the criterion counts as not reproduced. The record notes regression to the mean. The second-lowest sextile also "increases" under M2(b) (p 0.012, against 0.83 under M2(a)), which fits that worry.
- **fig3c-spindles-over-sleep (partial, assumed):** The only significant incidence decrease is reading (b) with clock (i), p 0.03. Without the duplicated Dino ACC sessions it is p 0.15 (cell 71). The clock assumption is stated; the dependence on counting one day twice is in the notes but not marked as part of the assumption.
- **figs5d-rem-nrem-rem (partial, assumed):** The adopted rule is reasonable given M6, but it gives 660 cells against the paper's about 136, so the triplet set is not the paper's.

Are the assumptions stated and reasonable?

- **Stated and reasonable (8 claims):**
  - The normalization clock: fig3c-spindles-over-sleep, fig4-sextiles-within-nrem.
  - Triplet adjacency of 2 s or less: fig5b-ma-nrem-ma, fig5c-sigma-ma-change, fig5b-ma-between-packets, fig5b-rem-between-packets.
  - The tolerance after REM: figs5d-rem-nrem-rem.
  - Motion z-scored per session: fig5b-wake-between-packets.
- **No assumption stated (2 claims):**
  - fig4cd-packet-rate-lfp-correlations: 4 of 6 holds under both M2 readings (cell 101), and the deviations list only standard choices.
  - fig4-lfp-within-nrem: the partial rule (delta and sigma increase) holds under every reading, clock and variant (cell 86).
  - Either the flag should come off these two, or the assumption should be named.
- **A wording error in the record:** the response for fig4-sextiles-within-nrem says it was "judged under clock (ii) as for other trends". fig3c-spindles-over-sleep was judged under clock (i). The rule actually applied is the best of the two clocks, which the shared deviation text does say.

**2. Sentences the printed numbers do not support**

- **Cell 87 and the record's fig4-lfp-within-nrem notes:** "Gamma decreases within episodes under readings (a) and (b) (R = -0.223 …)". Cell 86 prints R -0.220 (clock i) and -0.245 (clock ii). The value -0.223 is the fig4cd M2(b) delta correlation in cell 101.
- **Record, burst-index-by-state notes:** "Kruskal-Wallis p from 1.1e-48 to 3.6e-54". Reading (a) gives 3.4e-46 (cell 30). Cell 31's "below 1e-45" is correct.
- **README and cell 0:** the stream "takes about 12 minutes". Cell 2 prints 9.2 min. This is minor.
- **Cell 59** cites the first-5-min variant (47 cycles, p 3.9e-10 and 2.8e-06), but those numbers are printed later, in cell 65, which sits under fig3b-sextile-changes. The numbers are right; only the placement is out of order.

Every other "Result" sentence, the Summary, the README and the record's notes match the printed outputs. That includes the ketamine and saline inference in the Summary (cell 5: the injections fall after the last deposited file of each of the three sessions).

My round-1 reasons are given in my own words. Text from my B and C points has been moved into the matching claim reasons; it is accurate. The count "35 of 41 agree" is correct: there are six `agrees: false` entries.

**3. Round-1 points**

Resolved:
- B1, the MA set: the neighbours of the short WakeInterruptions are printed (none lies between two packets), and MA reading (b) was run everywhere it applies.
- B5, the unit of fig4e-within-up-sextiles.
- B7, the sextile readings: M2(a) is now the session's WAKE rate, and M2(b) was run.
- B8, recorded as a deviation.
- B9, the edge windows: checked.
- B12, the Dino ACC/mPFC duplicates: the trends are shown without them.
- All six C items: the 51 cycles, the neighbours of the short interruptions, the pI REM median (same middle cell under both readings), the direction for the lowest sextile in packet-MA-packet, the ketamine timing, and the spindle duration over all spindles.

Still open, and bearing on a conclusion:
- **B2, the post-sleep window:** this decides post-sleep-wake-lower and partly fig3e. The first-5-min variant would make post-sleep-wake-lower reproduced. However, in 38 of the 47 cycles none of that window is scored as WAKE (cell 65), so the variant may not be the paper's "WAKE" either.
- **B3, the triplet set:** no rule reaches the paper's cell counts (figs5d 660 against about 136; packet-WAKE-packet 8 or 52 against 24).
- **B4, motion:** fig5b-wake-between-packets now rests on n = 7.
- **B6, pseudo-replication:** fig2a-fraction-above-2hz still passes only under reading (a). Under reading (b) it would be partial.
- **New from the round-2 changes:**
  - fig3f-within-up-changes mixes M1 readings across its parts (see section 1).
  - fig3c-spindles-over-sleep depends on including both Dino copies.
  - The edge-trimmed spectrogram would make fig4-lfp-within-nrem reproduced under reading (c). The record keeps partial because the claims file names the plain spectrogram.
- **B10 and B11:** reported and handed to a reader. Neither changes an outcome.
