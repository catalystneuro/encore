The file is ready for an attempt. I corrected 13 claims, mostly method details the earlier writer had fixed without support from the paper; three things remain open. Only `claims/hunt-2018.yaml` was changed, and nothing is committed.

**Checker:** `claims/hunt-2018.yaml: 40 claims, 40 quotes, 15 statistical values, 2 problems`. Both problems are the p < 1e-7 values in `fig8-cue1-value-all-regions` and `fig8-attribute-value-ofc`. The text extraction prints them as "p<1*10 7", dropping the minus sign; I confirmed both by reading.

**Changes, by claim**
- **Eight claims from the cue 1 population section of the Results** (`fig4d`, `fig4e`, `fig4f`, `fig4g`, `fig4h`, `figs2`, `fig4-t75-latencies`, `figs5c`): every paragraph number in the sources was one too low. Corrected.
- **`figs1ab-cue-weights`:** the statement left out the legend's "slight upweighting of the antepenultimate cue". Added; the legend gives no test for it, so it is reported, not judged.
- **`fig4d-spatial-attention`:** "represented in OFC and ACC" now needs the paper's permutation test at p < 0.05, not just a positive coefficient.
- **`fig4h-acc-accept-reject`:** the criterion compared CPDs of two different templates, which the Supplementary Figure 5 legend warns against. "Best explained" is now open, with two readings.
- **`figs4-dlpfc-top-bottom`:** says the "replicate" part is not judged, because the paper defines no templates for 40 conditions.
- **`fig4-t75-latencies`:** the time range is not in the paper, so it is now named as a reading.
- **`fig5a-ofc-value-cpd`:** the baseline was made up. It is now open, with two readings.
- **`fig5gj-cross-correlation-dynamics`:** removed the p < 0.001 entry from the statistics. It is the significance level set in the Methods, not a reported result.
- **`figs67-no-comparison-acc-dlpfc`:** the legends say the stored subspaces (panel F) are present in ACC and DLPFC, so the presence test now includes that correlation.
- **`fig6a-acc-belief-subspace`:** whether T-statistics or parameter estimates are correlated is now open, since the Figure 6A Methods and the Supplementary Figure 10 legend say parameter estimates. The file now says its rule for absence in OFC and DLPFC is its own choice, not the paper's.
- **`fig6c-belief-subspace-rt`:** removed the made-up rule that the effect must hold in 95 of 100 splits. The count is reported instead.

I checked Supplementary Table 1: its columns sum to 198, 195 and 156 units over 29 and 24 sessions, as the file says.

**Open**
- **Main figure legends:** the legends of Figures 1 to 8 are missing from the text, and there is no PDF of the main article. The tests behind several claims therefore could not be read: the Figure 2 behaviour, the single correlations in Figure 5, the region comparisons in Figure 7, and the absence in Figure 6a.
- **Analysis code:** the paper's scripts are among the CRCNS pfc-7 files and were not read. They might settle the open details O1 to O9 and the regressors of the Figure 8 model.
- **Unsupported rules:** some rules have no basis in the paper ("virtually all" read as 18 of 20, the ramp windows in Figure 6d and 6e, the bound in `figs9`). Each criterion now says so or names them as readings.

**Ready:** true.
