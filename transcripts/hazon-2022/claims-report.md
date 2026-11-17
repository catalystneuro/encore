I wrote `claims/hazon-2022.yaml`. All 28 quotes pass `claims_check.py`. The checker still exits non-zero on one value: it can't parse the printed "p < 4・10-5" in Suppl. Fig. 11c. I checked that one by reading (supplement legend, text line 597), and the bound is right.

**Text read**
- **Paper:** the version of record, from PMC9314334 via Europe PMC's JATS XML: main text, figure legends and Methods.
- **Supplement:** the Supplementary Information PDF (MOESM1, Suppl. Figs. 1 to 19 and Tables 1 and 2), read from its text.
- **Not read:** the Source Data file and the Reporting Summary, which aren't under `paper/`. No claim needs them.
- **Code:** github.com/approbatory/ML-project at commit 2057af9 (2022-06-07), MATLAB, including the live scripts with their saved outputs.
- **Dataset:** I read only the hc-30 data descriptor, not the data.

**Counts**
- 29 claims: 28 with quotes, and 1 marked `inferred` (the Suppl. Table 1 place-field values, which no sentence states).
- 15 claims carry statistics, 24 entries in all.
- Every claim has a criterion, and 14 have expected values.
- 2 claims are `data: elsewhere` because they rest on simulations (Fig. 5a–d and Suppl. Fig. 9).

**Open details and the readings named**
- **Response variance (0.7263):** the text says variance, but the code averages standard deviations. Both are readings.
- **Single-cell SNR (0.41):** the code that printed it wasn't found, and the code's own version of the ratio has a bug. The definition is taken from the Suppl. Table 1 footnote, with the classes pooled or split by direction.
- **Large-data sessions:** "at least 200" neurons (Methods) or "more than 200" (code).
- **Saturation range (346–1402):** the 73 large-data sessions (code) or all 110 sessions.
- **Fig. 3f direction:** the legend says the signal slope decreases over the run. The code's one-tailed test, which gives the printed p, tests for an increase. Directions pooled (code) or rightward runs only (legend).
- **Fig. 4b/4c overlap:** summed over all PCs (legend and code) or the first six (Methods).
- **Fig. 4c correlation:**
  - the y variable is the unshuffled asymptotic SNR (code) or the SNR ratio (Suppl. Table 2);
  - r² adjusted or plain;
  - the legend's "Pearson 0.81" doesn't match r² = 0.50, so it isn't used.
- **Fig. 5i ratio:** unshuffled over shuffled (legend, code) is the main reading. The Results sentence and the Suppl. Table 2 header word it the other way. The code's session filters are applied or not.
- **Suppl. Fig. 7 tests:** across 110 sessions or the 12 per-animal means.
- **Suppl. Fig. 8 accuracy:** log10 or linear I0N. The code's printed r values (0.402, 0.559) differ from the legend's (0.34, 0.52).
- **Fig. 1d distances:** single distances, with the code's merging of neighbouring distances as a variant.
- **Fig. 2c/2d bins:** 20 positions or 40 bin-and-direction classes.
- **Suppl. Table 1:** how rates are counted, what counts as in-field, and whether directions are pooled. Neither the paper nor the code read fixes these.
- **Correlations vs physical distance:** the paper names no test or threshold. Two thresholds are given, applied to the code's linear fit.
- **Synthetic model (Fig. 5a–d):** uniform half-widths (legend) or log-normal (Methods).
- **Suppl. Fig. 6:** which bin numbers are compared, and where in a bin the prediction is placed.
- **Suppl. Fig. 9:** the trajectory model and time bin.

**Missing from the paper or code**
- No script was found for the synthetic place-field model, the Suppl. Fig. 9 simulation, or the printed single-cell SNR of 0.41.
- The physical-distance claim needs cell positions. The data descriptor lists none, so that claim may not be testable.

Nothing is committed. Only the claims file is mine; the other untracked files in the working tree were already there.
