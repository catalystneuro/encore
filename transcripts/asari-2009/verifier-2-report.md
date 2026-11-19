**Verifier report, round 2: Asari & Zador (2009) on CRCNS ac-1.** The claims file has 21 claims, and the attempt record has 21 outcomes: 7 reproduced, 6 partially reproduced, 5 not reproduced, 3 blocked. Cell numbers below refer to the re-executed `reproduce_asari_2009.ipynb`, which now has 65 cells (0–64), unless `strf_wehr.ipynb` is named.

### 1. Outcomes

| Claim | Agree? | Assumption stated and reasonable? |
|---|---|---|
| methods-recording-counts: partially reproduced | Yes | — |
| a1-mgb-firing-rates: partially reproduced (assumed) | Yes | Stated. The partial rule holds only under the variant MGB detectors (half threshold, 4 SD), not under the authors' own detector (4.99 Hz, cell 13). The record says so. |
| fig2-example-reliability: reproduced | Yes | — |
| fig2-example-long-context: reproduced | Yes | — |
| fig3a-proportion-significant: reproduced | Yes | It holds only under the all-probes reading. The record says so and asks the authors. |
| fig3a-significance-decay: partially reproduced | Yes | — |
| fig3b-fractional-power-decay: not reproduced | Yes | — |
| timescale-longer-than-membrane: reproduced | Yes | — |
| fig4-predictability-upper-bound: not reproduced | Yes | — |
| fig4-strf-performance-low: not reproduced (assumed) | Yes, under the stated cell set | The assumptions are stated, but the record leaves out that the outcome depends on which cells are used. In `strf_wehr.ipynb` cell 11, using only the ten 2002 cells (5 to 25 repeats), three of the four all-bins readings meet the full criterion: hann10/contig STRF p = 0.053 and LN p = 0.22; hann10/stim 0.31 and 0.50; hann20/stim 0.28 and 0.86; all means ≤ 0.14. The outcome therefore depends on adding six 2003 cells that have only two trials per sound. This belongs in the notes. |
| fig5-example-conductances, fig6-conductance-decay: blocked (data missing) | Yes | — |
| fig8a-proportion-by-property: not reproduced (assumed) | Yes | 'table1' is the only reading whose totals equal all five columns (cell 10), so it is the reading the criterion points to. The two pure readings would give partially reproduced, and the record says so. |
| fig8b-decay-by-property: partially reproduced (assumed) | Yes | Yes |
| fig8a-significance-fits: not reproduced (assumed) | Yes | Yes |
| fig8c-relative-effects: partially reproduced (assumed, seed-sensitive) | Yes on the outcome; no on the seed-sensitive flag | The flag rests entirely on the trial-resampling reading. The attempt itself calls that reading "not a sound interval" (cell 47): its intervals exclude their own point estimates, for example AM 0.15 against an interval of 0.81–0.93. The sound reading (resampling probes) fails the full criterion under all five seeds (cell 46). |
| fig8-natural-synthetic-probes-alike: reproduced (assumed test) | Yes, changed from round 1 | The labelling objection is answered (see B1 below). The test has almost no power: AM has 14 synthetic tests in 2 cells, and FM has none. The record says so. |
| fig9-mgb-fast-decay: partially reproduced | Yes | The plateau result depends on the detector (1.27, 1.38 and 3.24 spike/s bracket 2.0). Reasonable. |
| fig9-example-first-bin: reproduced | Yes | — |
| fig7-example-frequency-context: blocked | Provisionally | The search is incomplete (see item 3). |
| figs1-silence-probe: reproduced | Yes | — |

### 2. Statements the printed numbers do not support

- **Attempt record, fig3a-significance-decay:** "with sizes held non-negative over running probes, the claim's seed selects one exponential (0.205, 0.50 s) and the other four seeds two." Cell 25 prints `seed 0 running 0-4.72 s nonneg: 2 exp, alpha [0.162 0.068], tau [0.266 1.095]`, and lists that reading among those with two exponentials. The outcome is unaffected.
- **Cell 59 and the attempt record, fig7:** "in two of their ten frequency tests the last significant period ends after 3.6 s". Cell 58 shows three: 3.6733 s in 20060916-ha3-002-002, as well as 4.58 s and 4.83 s.
- **Attempt record, MHT finding:** "the per-set natural-probe tests of the 19 sixteen-MHT files less one per file (76 - 19 = 57)". No output prints 19 files or 76 tests; cell 10 prints 25 files and 82 tests.
- **Cell 63 (Summary):** "in the MHT ensembles only the natural sound is preceded by more than one fragment". Cell 10 prints 14 AM tests on MHT probes in 2 cells. The statement holds only for the 25 MHT-ensemble files that contain a natural sound.
- **Cell 56 and the attempt record, fig9-example:** they say all 12 probes with the Figure 9A design are in 20071010-ha2-003. Cell 55 prints only the count (12) and the files of the 4 matching probes.
- **Entry README:** "takes about 35 minutes". Cell 64 prints 39.2 min.
- **Attempt record, fig4-strf-performance-low:** every figure quoted matches `strf_wehr.ipynb` cells 6–13. The notes leave out the cell 11 result described in item 1.

Every other sentence I checked in the "**Result:**" cells, the Summary, the README and the record's notes matches the printed outputs. The README and Summary tables match the record's 21 outcomes.

**My round-1 reasons in the attempt record:** the record states them faithfully and mostly in my own words, including the B-point cross-references. The `agrees` flags correctly reflect the author's round-1 outcomes.

### 3. Round-1 points

**Resolved:**
- B1, labels: cell 10 prints 235 MHT fragments with no conditioning fragment and 171 with one, so the natural/synthetic labels follow the files.
- B2: three readings are now shown, with 'table1' as the main one.
- B3: the silence-not-counted denominator (0.621) and the trial-resampling reading are both run.
- B4: the STRF claim is tested in `strf_wehr.ipynb`.
- B5, in part: the search is now shown in cells 58–59.
- B6: the plateau is printed and a 4-SD detector is added.
- B7: the files behind the 133-against-123 difference are listed.
- B8: the two fits that stop at the bound are noted.
- B9: tied values are printed (median 0.025, at most 0.134); the effect is minor.
- B14: the dead code is removed.
- B15: 159 cell folders and 159 cells in Summary.mat; my count of 161 was wrong.
- B10–B13: acknowledged; no change needed.

**What remains that bears on a conclusion:**
1. **fig4-strf-performance-low:** the outcome flips to reproduced with the ten well-repeated 2002 cells (cell 11). The record should disclose this, or explain why cells with two trials belong in the sample.
   - Not decisive, but worth a note: the LN model does much worse than STRF on validation data (one cell at −0.85, gains of −0.025 to −0.34), where the paper says LN does slightly better. This suggests the lowess step fails to generalise.
2. **fig8c-relative-effects:** the seed-sensitive flag should be dropped or qualified. It comes only from a reading the attempt itself calls unsound.
3. **fig7-example-frequency-context (B5, residual):** cell 58 searches only DMR files whose descriptions contain "frequency", yet the Figure 7 legend says "different bandwidths". Cell 58 also lists a fragment band `(625, 2500, 10000, 40000)`, whose edges are those of the example's three bands. Neither its file nor whether that file has a natural probe is printed, and neither are the bands of the other 5 DMR files that have a natural probe. The finding that no recording matches is shown only for the 5 frequency-variant files.
4. **MHT row of Table 1 (B1, residual; bears on the finding, not on an outcome):** Table 1's legend says rows are the probe type, and probes need only two conditioning stimuli. The attempt formed the synthetic rows with silence left out only. An MHT fragment with one conditioning fragment plus silence was not counted, so "cannot be formed from the data set" is shown under one reading only.

On the claims file: I found nothing that misreads the paper. The Figure 7 legend's "different bandwidths" with three 2-octave bands agrees with the Methods' description of frequency-shifted DMRs.
