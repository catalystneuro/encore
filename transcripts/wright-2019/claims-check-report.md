I checked `claims/wright-2019.yaml` against the paper and made seven changes. The file is ready for an attempt, and I've recorded `ready: true` under `checks`. Nothing was committed.

**Checker result:** `claims/wright-2019.yaml: 39 claims, 39 quotes, 50 statistical values, 3 problems`

The three problems are a checker limitation, not errors in the file. The checker drops trailing zeros, so it can't match values printed that way. I confirmed all three by reading the text:
- **9.70e-5** (`fig2b-onset-first-interval`) is in the Results.
- **8.90e-5** (`fig5a-onset-probability-first-interval`) is in the Figure 5A legend.
- **3.20e-3** (`fig5f-ramping-last-interval`) is in the Figure 5F legend.

**Changes, by claim:**
- **`fig4d-onset-patterns`, `fig4h-ramping-patterns`:** the criterion asked for "the only pattern above chance" among all six cue orders. The Methods name four categories and Figure 4D shows four, so it is now judged on those four, with all six as a variant. I also noted that the 1.5 interquartile-range outlier rule is a standard choice the paper doesn't state.
- **`fig4abc-onset-single-unit-biases`, `fig4efg-ramping-single-unit-biases`:** the criterion required positive correlations, but the paper only says "correlated". It now requires p < 0.05 and reports the sign found. I also cited the Methods paragraph that names the sign test and Pearson correlation.
- **`fig1s1b-sr-poke-correlation`:** the legend names no test. Pearson is now stated as a reading taken from the Methods. Per-cue and pooled-over-all-264-points correlations are both named as readings.
- **`fig5s1-regressor-combinations`:** what counts as "significance for fear output" is now open, with two readings:
  - single-sample t-tests against zero, as in Figure 5D;
  - the F tests the supplement legend reports.
  I also added the paper's statement that probability beats each fear regressor when compared with it separately.
- **`fig5f-ramping-last-interval`:** the source pointed at the Results paragraph, but the quoted t-tests are only in the Figure 5F legend. The source now names the legend first.
- **`fig2e-departure-times`:** the number of sliding windows is now named as open. The paper's 0.05/200 correction implies 100 windows per comparison, some running past cue offset. This can't change the departure times, because the paper fixes both thresholds.
- **New claim `fig5s1-ramping-regressor-combinations`:** the Results say the Ramping neurons' pattern holds under the regressor combinations of Figure 5, supplement 1F to 1J, and no claim covered that.

Everything else checked out as written: the quotes, statistics, the degrees of freedom of every ANOVA, the tolerances, and the chi-square reading of `fig6ef-beta-correlations` (8.29 × 39/40 = 8.08 and 4.33 × 39/40 = 4.22, the reported values).

**Still open:**
- **No PDF:** values printed only inside the figures (Figure 4, Figure 5 and the supplement panels) couldn't be read. Those claims rest on the legends and the tests they name.
- **No code:** the code the paper links (the lab website) couldn't be read, so every method comes from the text.
- **Paper inconsistency:** the Figure 2B legend prints 9.70e-4 where the Results print 9.70e-5. This was already noted in the file's header.
- **Minor findings with no claim:**
  - nose-poke stability and timing (Figure 1, supplement 1C and 1D);
  - waveform similarity within one rat (Figure 1, supplement 4);
  - high-firing-rate units signalling threat probability, shown only in panels (Figure 1, supplement 5);
  - how strongly neurons respond to nose-poke cessation (Figure 2, supplement 2C and 2D);
  - the Methods remark that uncertainty shock and omission trials did not differ during the cue.
