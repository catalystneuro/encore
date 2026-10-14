I've handled every point in the round-2 report. No outcome changed and nothing is proposed for a third round. The verifier agreed with all 23 outcomes: 9 reproduced, 4 partially reproduced, 7 not reproduced and 3 blocked (data missing). After my edits, `python tools/entry.py all entries/000130-sohn-2019` passed (778 s) and `check` reports 0 errors. Every number in the conclusions comes from that run.

**New analyses the verifier asked for**
- **alt-speed-unmodulated (cell 70):** I compared the null's mean speed with the observed mean speed. The null's is lower in 7 of 8 dataset-priors (ratio 0.65 to 1.18), so the null is not overstating the noise. The observed slopes sit below the null in 16 of 16 comparisons, which points to speed falling during the support, assuming the units are no noisier than Poisson. I didn't test that further. The text now says only that there is no speed increase beyond what noise produces, and that the paper's test cannot detect a change in either direction. The outcome stays reproduced, as the paper's test fixes it.
- **speed-predicts-tp (cell 65):** I added the Poisson null with each trial's own duration. The null correlations average -0.071 (Short) and -0.033 (Long) over 20 simulations. The observed -0.317 and -0.201 are below every null value, so trial duration explains only a small part of the correlation.
- **alt-threshold-monotonic (cells 76 and 77):** I added a direct count of crossings. In 12 of the 16 one-component curves the minimum is a crossing. In 4 the minimum is at Go, and 3 of those are not crossings. The overstated sentence is replaced with these counts.

**Text corrections**
- **Summary, z-scored rates:** it now says the encoding axis still scores above the median random axis in 8 of 8, but above 95% of random axes in none.
- **Bayesian minus linear differences:** the 0.045 to 0.573 range now covers only the datasets where the Bayesian model wins. Hand Right Short (+0.186) is given separately, in the conclusion and in the record.
- **wm and wp:** the ranges are corrected to wm 0.013 to 0.117 and wp 0.090 to 0.106.
- **GPFA:** the unbacked claims about repeated runs are removed. The likelihood gain is quoted from this run (0.064 to 0.085%).
- **Run time:** the README now says about thirteen minutes, and `runtime_minutes` in `entry.yaml` is 13.
- **Unit counts:** the paper recorded 617 (H) and 741 (G) units and kept 536 and 636 for analysis. The Summary and the data_missing finding now say this.
- **N = 107:** the paper_inconsistency finding now says N counts neurons in the single high-yield session used for GPFA, not sessions.

**Paper text:** PMC's BioC service still returned 429 and Europe PMC returned 500, and the PMC page served a captcha. I got the relevant sentences through a web fetch and saved them as quotes in `paper/PMC6805134_excerpts.md`; the full text is still not downloaded. I removed the error pages from `paper/`, including the two the verifier reported.

**Recorded and not done**
- Round 2 is recorded under `verifications`, with the verifier's reasons in its own words and my changes under `response`.
- The run-time and unit-count fixes are not tied to a single claim, and the record format only has per-claim entries. So they appear only in this report and in the corrected files.
- Tables S1 to S3 and Fig. S5 are still unavailable, so the fitted wm and wp and the paper's random-axis values are still not compared.
- I committed and pushed nothing.
