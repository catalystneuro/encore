**Verifier report, round 2: Watson et al. 2016 on DANDI:000041 and CRCNS:fcx-1**

I counted from the files themselves. The claims file has 53 claims and the attempt record has 53 outcomes, one per claim id, with no missing or extra ids: 27 reproduced, 10 partially reproduced, 16 not reproduced, 0 blocked.

### 1. Outcomes and assumptions

**Outcomes.** I agree with all 53 outcomes in the attempt record.
- **Changed since round 1:**
  - `fig2c-acg-peaks` is now partial, and `fig4cd-packet-rate-lfp-correlations` and `fig4e-within-up-sextiles` are now not reproduced. These are the outcomes I gave in round 1.
  - Judging on CRCNS restores the eight claims that problem 3 would have downgraded.
- **Rechecked after the code fixes:**
  - `burst-index-by-state` stays partial (cell 40). Under every reading the order is nonREM > REM > WAKE, Kruskal-Wallis p < 1e-37 and Dunn p ≤ 7.7e-6, but no reading has all three medians within tolerance. Under reading c, nonREM (11.5%) is inside and WAKE (4.6%) and REM (6.5%) are above.
  - `fig4vi-burst-within-nrem` stays reproduced with spike-time ISIs: R = 0.081 and 0.079, p < 1e-15 (cell 123).
  - `ma-fraction-over-nrem-episodes` stays partial: over SLEEP, p = 0.018 (cell 22).
  - `fig4i-band-power-within-nrem` stays reproduced under reading c: gamma falls over episodes (p = 0.030) and does not change over packets (p = 0.092) (cell 99).
  - `fig4-spindles-within-nrem` stays partial: spindle frequency changes over packets, p = 0.011 and 0.026 (cell 111).
  - `fig3e-wake-before-after-sextiles` stays reproduced under M1 reading a, both as before and with sextiles ranked on held-out WAKE (cell 94).

**Assumptions (`assumed: true`, 6 outcomes):**
- `fig2c-acg-peaks`: a bin is named by its centre. This is stated, reasonable, the alternatives are shown, and it is referred to a reader.
- `fig1e-up-state-dynamics` and `fig4e-late-packet-sigma`: 200 ms windows within UP states. Stated and reasonable; fig1e is partial either way.
- `fig4cd-packet-rate-lfp-correlations` and `fig4e-within-up-sextiles`: a part "holds" at M4's reproduced level. This is stated and reasonable (the stricter reading), the lenient result is given, and it is referred to a reader.
- **`fig2de-fast-before-slow`: this mark does not match a stated assumption.**
  - Its only text that says "assumed" is the DANDI UP/DOWN detection.
  - On the same grounds the author removed the mark from `updown-durations`, `fig3c-updown-over-sleep`, `fig3f-within-up-changes` and `fig4-updown-within-packets`, because their outcomes rest on the deposited CRCNS states.
  - The 200 ms latency window comes from the criterion itself, not from an assumption.
  - So either the mark should go, or the assumption it stands for should be named.

### 2. Sentences the printed numbers do not support

- **Cell 29, and the `fig2a-median-rates` notes:** "No reading puts all six within tolerance on either dataset (DANDI, best reading a, four of six)."
  - DANDI reading c is the best reading, with five of six inside tolerance: 0.72, 0.66, 0.82, 5.23 and 4.78 Hz are in; only pI REM (6.00 Hz) misses.
  - The outcome is unaffected.
- **Cell 29, same notes:** "Per-rat medians vary about twofold (pE WAKE 0.40 to 1.23 Hz)." That range is about threefold.
- **Cell 71, and the `post-sleep-wake-lower` notes:** "Rank-sum tests are not significant."
  - For CRCNS reading ii with M1 a, the one-sided rank-sum p is 0.027 (cell 70).
  - The criterion allows a one-sided test.
- **Cell 130, and the `fig4e-within-up-sextiles` notes:** "DANDI: the same directions." Under DANDI reading a(i), the top sextile rises, from 2.789 to 2.808 Hz (cell 129).
- **Summary (cell 172):** "its deposited intervals and detections reproduce Table S1, except the microarousals."
  - It leaves out the WAKE-SLEEP duration: 4214 s on CRCNS against the 5918 s Table S1 prints.
  - Cell 17 reports this, and the record files it as a `paper_inconsistency` finding.
- **Cell 0:** "Every claim lists both datasets, and each is tested on each." The table in the same cell, and cell 150, say `fig5c-wake-movement` is tested on CRCNS only.
- **README:** "peaks near 10 GB of memory."
  - The only memory figure printed is "peak memory of this process 1.98 GB" (cell 1).
  - The "about 90 GB" streamed is not printed anywhere.
  - Loading alone took 19.5 minutes (6.6 + 12.9), so "about 20 minutes" in total cannot be checked from the outputs.

Every other "**Result:**" sentence, the rest of the Summary, and the rest of the attempt record's notes and findings match the printed outputs. The record's notes copy the conclusion cells, so the errors above are in both places.

**My round-1 reasons in the attempt record.** They are stated faithfully, in my words, with the problem text appended. Three small defects:
- The `fig3e-wake-before-after-sextiles` reason says "See B3" and the `fig3d-first-last-packet-slope` reason says "(B4)". Both are my own mis-numbering from round 1; each should point to problem 5.
- Round 1 said problem 4 applies to every claim that uses MAs. The reasons for `ma-fraction-over-nrem-episodes`, `fig5b-ma-nrem-ma`, `fig5c-sigma-ma-change` and `fig5b-ma-between-packets` do not cite it, although the author's responses do address it.
- Problem 2 was not attached to `fig4i-band-power-within-nrem` or `ma-fraction-over-nrem-episodes`, though the responses address it there too.

### 3. Round-1 points

**Resolved:**
1. **ISIs on the grid (problem 1).** `isi_counts` now counts ISIs from spike times and keeps an ISI when both spikes lie in one interval. I read the code and it is correct. The grid version is printed for comparison and was inflated (5.2/14.3/6.7%).
2. **Bins of reading c (problem 2).** `secs` now gives each grid second to the bin that holds its centre, and the REM part of `figs5-within-wake-rem` also uses exact spike times. The result is unchanged: 2 of 5 sextiles significant.
3. **Outcome rule (problem 3).** Outcomes are now judged on CRCNS.
4. **Regression to the mean (problem 5).** A variant with sextiles ranked on held-out WAKE is added for `fig3e-wake-before-after-sextiles` and `figs5-within-wake-rem`. Reverse slopes are added for `figs3a-first-last-rem-ma-slopes` and `figs2d-interneurons-unchanged`.
5. **Problem 7.** M1 reading b is added, sigma is now 9–25 Hz, a coarse S4B map is shown, and the 5 dropped triplets are explained: they lie in sessions with no top-sextile cell.
6. **Section C.** The table of where the MAs lie is added. DANDI LFP `starting_time` is 0 in every file, and delta power is higher in nonREM than in WAKE in 20 of 20 sessions. DANDI's only ElectricalSeries is the 1250 Hz LFP.

Problem 6 is unchanged; it does not affect a conclusion.

**Still open, and bearing on a conclusion:**
- **MAs (problem 4).** The deposited MAs are now located: 434 in the SLEEP of cycles, 26 in WAKE and 1670 in neither, with medians near 11 s, and no subset gives 790.
  - Which MAs the paper used is still unknown; it is filed as a question for the authors.
  - Six outcomes rest on an MA set that does not match the paper: `ma-statistics`, `ma-fraction-over-nrem-episodes`, the MA slope of `figs3a-first-last-rem-ma-slopes`, `fig5b-ma-nrem-ma`, `fig5c-sigma-ma-change` and `fig5b-ma-between-packets`.
- **`fig3e-wake-before-after-sextiles` rests on M1 reading a**, which enters a cell once per cycle.
  - Under M1 reading b (one entry per cell), the fourth sextile misses: p = 0.077, and 0.055 with held-out ranking.
  - The criterion allows reading a, but under reading b the claim would be partial.
- **Claims-file readings referred to a reader (problem 8).** These outcomes depend on how the reader answers:
  - `fig2c-acg-peaks` would be reproduced if a bin is named by its start.
  - `fig4cd-packet-rate-lfp-correlations` would be reproduced, and `fig4e-within-up-sextiles` partial, if "hold" means p < 0.05.
  - `fig3c-spindles-over-sleep` uses 1.94 against 2.94 spindles per minute; the claim fails either way.
  - `synchrony-skew` passes the criterion's direction-only test at 63% of cells, against the paper's 15%.
  - `figs2d-interneurons-unchanged` has an implausibly narrow interval in the legend.
- **The `assumed` mark on `fig2de-fast-before-slow`** (section 1).
