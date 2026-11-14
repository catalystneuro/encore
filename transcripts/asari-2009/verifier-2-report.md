**Round-2 verification: asari-2009-01 (doi:10.1152/jn.00577.2009, CRCNS ac-1)**

Counts are taken from the source files: the claims file (`asari-2009.yaml`) has 21 claims, and the attempt record (`asari-2009-01.yaml`) has 21 outcomes, one per claim. Cell numbers refer to the re-executed `reproduce_asari_2009.ipynb`, or to `strf_wehr.ipynb` where marked "strf". Cell numbers have shifted since round 1.

### 1. Outcomes

| Claim | Record | Agree? | Note |
|---|---|---|---|
| methods-recording-counts | partially_reproduced | yes | Cell 13. |
| a1-mgb-firing-rates | partially_reproduced | yes | Cell 16: 0 of 32 readings have all four means in tolerance, and the partial rule holds in 28 of 32. With the code's own MGB detector the margin over 5 Hz is still only 0.03–0.07 Hz. The rule is comfortably met only at half that detector's threshold (7.1 Hz), which is an ad hoc choice. |
| fig2-example-reliability | reproduced | yes | Cell 19. |
| fig2-example-long-context | reproduced | yes, with a caveat | See point A below. |
| fig3a-proportion-significant | reproduced | yes | Cell 25, with_silence/all reading. |
| fig3a-significance-decay | partially_reproduced | yes | Cell 31. |
| fig3b-fractional-power-decay | not_reproduced | yes | Cell 34: τ is 1.29–1.78 s in all 8 readings. |
| timescale-longer-than-membrane | reproduced | yes | Cell 38. |
| fig4-predictability-upper-bound | not_reproduced | yes | Cell 41: no τ within 1.04 ± 0.10 s. |
| fig4-strf-performance-low | not_reproduced | yes | strf cell 7: no reading meets both parts. The two assumptions (16 cells, Wilcoxon test) are stated and reasonable. See point B. |
| fig5-example-conductances | blocked (data_missing) | yes | |
| fig6-conductance-decay | blocked (data_missing) | yes | |
| fig7-example-frequency-context | blocked (data_missing) | **now yes** | Cell 70: the DMR frequency variants are 2-octave bands at 0.25–1 up to 8–32 kHz. None is 0.625–2.5, 2.5–10 or 10–40 kHz, and the 4-band group has no natural probe. I withdraw my round-1 reason ("search incomplete"). |
| fig8a-proportion-by-property | partially_reproduced | yes | Cell 46: the order holds and every count is out of tolerance, under all three readings. |
| fig8a-significance-fits | not_reproduced | yes | Cell 49. |
| fig8b-decay-by-property | partially_reproduced | yes | Cell 52: the partial pattern holds under every reading. FM is 0.278 s in the main reading, close to the 0.3 s line. |
| fig8c-relative-effects | not_reproduced | yes | Cell 55: the frequency interval excludes 1 under every reading, the highest bound being 0.938. |
| fig8-natural-synthetic-probes-alike | reproduced | yes, weak | Cell 58: FM has no synthetic probes and AM has 14 from 2 cells. |
| fig9-mgb-fast-decay | reproduced | yes | Cell 61. |
| fig9-example-first-bin | reproduced | yes | Cell 64. |
| figs1-silence-probe | reproduced | yes | Cell 67. |

**Assumptions.** Six outcomes are marked `assumed: true`: fig4-strf and the five fig8 claims. Each assumption is stated in the record.

- The rebuilt property sets are reasonable. Cell 44 prints them for each recording, and they follow the stimulus parameters and the notes.
- The choice of main reading is post hoc. It was picked because it reproduces Table 1's five totals. Its probe-type and cell split does not match Table 1:
  - AM, natural probes: 82 tests in 24 cells here, against 25 in 25.
  - AM, MHT probes: 14 tests in 2 cells here, against 71 in 27.
  - It gets there by counting each natural probe of the 17-stimulus grid recordings up to four times.
- This does not change any outcome, because all three readings give the same outcome for every fig8 claim.

### 2. Sentences the printed numbers do not support

- **README:** the runtimes are wrong.
  - "about 25 minutes": cell 73 prints 18.2 min.
  - "about 22 minutes": strf cell 11 prints 10.0 min.
- **Record, fig4-predictability notes:** "The mean of the smoothed ratio over the first 100 ms is 0.50." That is true only with silence counted. Without silence it is 0.571 (cell 41). Cell 42 states the qualifier; the record leaves it out.
- **Record, fig7 notes, and cell 69:** "they share their modulation parameters." Cell 70 prints only name, description, `ff`, `df` and attenuation, so no printed output shows the modulation parameters.
- **strf cell 9 and record, fig4-strf notes:** two statements depend on one cell, 20020602-mw-001, though the numbers are correct as computed:
  - "LN … not better than the STRF on average (mean gain −0.010)"
  - "at most 0.22 at every window"

  That cell has LN validation performance of −0.574 at 180 ms and −0.713 at 4052 ms, with its ridge parameter at the end of the grid (strf cells 6 and 8). From the per-cell values in strf cell 8, without that cell:

  | | 180 ms | 4052 ms |
  |---|---|---|
  | STRF | 0.190 | 0.222 |
  | LN | 0.214 | 0.250 |

  So LN is better by about 0.025–0.03, and both models exceed 0.22 at 4052 ms. The outcome stays not_reproduced either way, but the notes should say that these two statements rest on that cell.
- **Everything else matches.** I checked every other "**Result:**" cell (14, 17, 20, 23, 29, 32, 36, 39, 42, 47, 50, 53, 56, 59, 62, 65, 68, 71, strf 9), the Summary sections (cell 72, strf cell 10), the README table and every other note in the record against the printed outputs.
- **My round-1 reasons:** the record's `verifications` entries state them in my own words, fairly. It drops my estimate for fig8c (ratios of about 0.97 and 0.89 with the without-silence reference), which no longer matters now that the reading has been run.

### 3. Round-1 points

**Resolved:**
- **1.** STRF is now tested.
- **2.** The MHT sets are printed and match the metadata. MHT-probe tests exist in only 2 recordings, so the remaining gap is in the data, not the parser.
- **3, 4.** The without-silence reference is run and the partial-rule check is corrected.
- **5.** The fig7 search is complete.
- **6.** The window readings and a second MGB detector are run.
- **7.** The cells are listed. The 10 extra cells cannot be named from the data.
- **8.** All significant periods are printed.
- **9.** Fits stuck at the bound are flagged.
- **10.** NaN is returned where no probe runs, and bin 60 is dropped.
- **12.** The 200 shuffles are now stated in cell 24.
- **13.** `asari.py:837` now cuts each set to its own contexts.
- **11.** No change was needed.

**Remaining points that bear on a conclusion:**

- **A. fig2-example-long-context.**
  - The Figure 2B legend says the red trace is "the one shown in A", so the long-context probe is the 0.74-reliability probe of the 0.61-reliability cell.
  - Only 20051222-ha1-001-002 matches those values (cell 19).
  - The passing probe comes from 20060105-ha1-001-002. That cell's mean reliability is 0.309, so it cannot be the paper's example.
  - In the identified cell, probe 4 shows the paper's pattern: significant to 1.60 s, nothing until 3.97 s, then significant again. It misses the strict 2–4 s rule only because a run starts 30 ms before 4 s.
  - Which probe of that cell has reliability 0.737 is not printed.
  - The claims file's criterion does not use this link between 2A and 2B. That is a gap in the claims file, which I report and do not correct.
  - Reproduced is defensible under the criterion as written, but the record should say that the passing probe is not from the paper's example cell.
- **B. fig4-strf.** The two statements in section 2 depend on one cell with negative performance. This does not change the outcome.
- **C. fig8c.** The trial-resampling reading is still not run. It is unlikely to change the outcome: the frequency point estimate is 0.80, and its probe-resampled upper bound is at most 0.938.
- **D. a1-mgb-firing-rates.** With the code's own detector, the partial outcome still rests on a margin of 0.03–0.07 Hz above 5 Hz.
