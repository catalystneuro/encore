I've worked through all of the round-1 report. Seven outcomes changed. I re-ran the entry with `python tools/entry.py all entries/crcns-hc-7-kohus-2016` (0 errors, the notebook passes in 306 s), every conclusion now matches the new numbers, and the record has a `verifications` block for all 44 claims. Nothing is committed.

**Outcome changes**
- **async-charge-epi-vs-160: partially_reproduced → not_reproduced.** This follows from fixing problem 1 (the 160 Hz arm was measured after the isolated 11th AP; it now uses the 10th). CCK+BC pairs still carry more charge after EPI than after the train (4.44 against 1.18 pC), but the difference is no longer significant: p 0.0934 under both readings.
- **decay-epi-vs-160: stays partially_reproduced.** With the same fix it now rests on reading a: both tests hold with EPI longer (p 0.00025 and 0.0121), but only 1 of 4 medians is within tolerance. The 160 Hz medians are 15.07 and 38.51 ms, and these are now the recorded `measured` values.
- **fig6-cckbc-async-onset and cckdti-async-onset: blocked → not_reproduced.** As the verifier said, the claims file gives two onset rules and both were run, so they are judged on them. The CCK+BC EPI median onset is 1.0 to 3.5, against 10 to 12 expected.
- **fig10-cck-cck-heterogeneity and fig10-cck-cck-async: blocked → not_reproduced.** Both rules mark asynchronous release in 9 of 9 pairs (expected 45 to 66%). For the async claim, 0 of 9 pairs have the required onset pattern, and the duration depends on frequency (p 0.00088).
- **fig8-cck-pairs-uipsc, fig8-cckbc-vs-cckdti-pairs and decay-pc-vs-interneuron: not_reproduced → blocked (data_missing).** None of the claims file's single-AP readings exists for the CCK+ pairs. The extra reading I used for them is still shown but decides nothing. The notes say the PV+BC half of decay-pc-vs-interneuron holds.
- **fig10bd-be-async-charge: still blocked, now as data_missing.** There are no 320 Hz trains for these pairs. The 10, 40 and 160 Hz parts are now printed, and they hold.

**Other changes**
- **Pipette solution (problem 4).** The data can't settle which pairs, if any, were recorded with CsCl. I added a per-pair table of recording day, rise time, latency and holding current. No connection type splits into two groups, but a mixture can't be ruled out. The 16 outcomes on interneuron-to-pyramidal-cell pairs are now marked `assumed: true`, with the assumption written out as a deviation.
- **Fixes in the asynchronous-release code.**
  - "Last AP" now means the 10th AP of a train and the 34th of EPI. This also affects fig6-cckbc-pc-trains and cckdti-pc-transmission; their outcomes don't change.
  - Two template fits that hit their bounds are no longer used for the reconstruction.
- **Outputs the verifier asked for:**
  - per-pair charge and decay at 160 Hz and under EPI;
  - per-sweep success at the single AP for fig4c;
  - the 40 Hz-and-below first-success variant (mean 2.57, still outside 4 ± 0.4);
  - the `_EPA` column labels next to the AP times (they confirm T01S01 is the single AP);
  - the list of PV+BC pairs with a 1 Hz train;
  - the number of recovery fits at the 1e5 bound.
- **Questions for a reader** in the new `questions/crcns-hc-7.yaml`:
  - fig4c: should it count only the first sweeps? Judged on the first sweep alone, all 7 pairs are silent.
  - fig5c: reading b is a Mann-Whitney test against a constant vector of ones, which is degenerate. The fig5c outcome doesn't rely on it.
  - The onset rules also flag the PV+ pairs the paper calls synchronous.
- **Text.** The fig5c notes now lead with the Wilcoxon test under M4 b. The header, blocked-claims section, summary and the findings on missing data and the onset question are updated.

**Not done**
- Problem 11 (an infinite test error for the TM depressing model, CCK+BC to PC, weighting a): with the code unchanged, the re-run gives a finite 3765.7 pA², so I couldn't reproduce it. The record says so.
- I can't match the 10 PV+BC pairs with a 1 Hz train to the paper's 16, because the files carry no identifiers.
- I left the claims file unchanged.
