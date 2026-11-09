I wrote `claims/001371/10.1038-s41467-025-60122-8.yaml`. The quote checker finds all 52 quotes word for word and the schema passes. It still exits non-zero on 5 p-values, all of them false alarms: the paper prints them with a trailing zero (`3.410e−11`, `2.630e-8`, `1.020e−7`, `4.490e-5`, `1.330e-5`) and the checker's number formatting drops it. I confirmed each one by reading. Nothing is committed.

**Text read:** the version of record from Europe PMC (PMC12102184), with the main text, Methods and legends. I also read the Supplementary Information PDF (Supplementary Tables 1–2 and Supplementary Figs. 1–14) and the Peer Review File. The Reporting Summary had no extractable text. The Source Data file was not available and nothing needed it. I opened no figure pages.

**Code:** github.com/stephprince/update-project at commit `d8557f0`. Its encoder settings, alignment, goal-arm bounds, choice thresholds, LSTM, residual model, classifier and statistics are cited in the file. Its cached results and R output tables are not in the repository.

**Counts:**
- 52 claims, all with quotes; none is inferred.
- 38 have statistics and 35 have expected values.
- All 52 have criteria, and all use the dataset alone.

**Details left open, with the readings named:**
- **Performance windows:** 40 trials per the Methods, or 15 per the code. Only 15 fits the reported 6252 windows.
- **Unit of the Wilcoxon tests:** sessions or windows for performance; trials or session means for the hippocampal choice difference.
- **Which trial types go into the mixed models:** two (the code; the degrees of freedom fit this), or three (the Supplementary Table 2 note).
- **Residual model fit:** across all trial types and animals (Methods), or per session on switch trials (code).
- **Time windows:**
  - goal bias index: 0–1.5 s or 0–2.5 s
  - Fig. 4h: 0–1.5 s (Methods) or 0–2 s (code)
  - Supplementary Fig. 5e: four windows, because the text and the legend list different ones
- **Theta zones and phases:** "central" zone as the whole central arm or an arm-sized window around the cue; Fig. 3b values over the first half-cycle or the whole cycle.
- **Smaller items:**
  - which second delay and trial set the task timings use
  - the denominator for the trial mix
  - the spread unit (bins or track units)
  - whether the all-trials encoder control uses correct or all trials
  - how the paper's unstated decoding-validation and tuning-tiling checks are measured
- **Settled by the code:** the "highest 10%" choice threshold (outer tenth of the range), the locomotion threshold (1000), and where delay-only trials are aligned (pseudo-update position).
- **Code variants against the Methods:** the encoder also trains on warm-up trials, and the motor response is defined differently. The Methods are followed in both cases.

**Discrepancies inside the paper,** recorded in the claims they touch:
- p-values differ between text and Supplementary Table 2: 0.002 vs 0.0002 (twice), 0.6496 vs 0.4203, 0.0375 vs 0.0490.
- Fig. 4f: the text gives 5.192e-49 for a contrast; the table gives that number as the ANOVA p.
- Fig. 7e: the sign of the new-choice correlation is positive in the text and negative in the table.
- Supplementary Fig. 5g prints a CA1 value of 0.010, beside 0.11 for the other arm; probably a typo for 0.10.

**Missing:** nothing a claim needed. The Source Data file was the only part of the paper not available.
