I wrote `claims/001676/10.1038-s41586-025-10096-w.yaml`. The quote checker passes with 0 problems: 31 claims, 31 quotes, 35 statistical values. Nothing is committed.

**Text read.** The version of record (Nature 652, 2026), from the hand-supplied PDF's text extraction: main text, Methods and all ten Extended Data legends. No figure was opened.
- The Supplementary Information (Supplementary Tables 1 and 2: the electrophysiology recording details and the sessions and HD cells per animal) is not under `paper/`. Neither are the Source Data. No claim rests on either, so I went ahead.
- PDF pages 22 to 25 have no extractable text and could not be rendered here. In Nature PDFs these are usually the reporting summary.
- The paper links no code ("Code will be made available upon request"), so no code was read. Every method detail comes from the Methods or the legends.

**Claims.** 31 claims, all with quotes and none `inferred`. 17 carry statistics and 30 have criteria. All use `data: dataset`; the paper uses no outside data.
- **Fig. 1 (stability in one environment):** ROI counts, HD-cell proportions, the Isomap ring, the V-tests (example mouse, pooled and per animal), registration confounds, drift rates, the shuffle comparisons, the pairwise-offset change, decoding across days, and the decay of population-vector correlation.
- **Fig. 2 (four environments):** offsets across environments, stability within each environment, electrophysiology offsets and waveforms, same versus mixed environments a week apart, the environment classifier, the Rayleigh tests of random remapping, and coherent remapping.
- **Fig. 3 (probe trials):** V-tests and mean vector lengths by delay, probe drift rates, and the interference experiment (Extended Data Fig. 9).
- **Fig. 4 and Extended Data Fig. 10 (single-visit memory):** the single-visit memory tests, the decoder, and the per-environment and per-animal values.

**Details the paper leaves open, and the readings named:**
- **Smoothing kernel**, "σ = 12° bins": 12 degrees, or 12 bins (36 degrees).
- **HDI on dF/F**: computed on the raw or the smoothed tuning curve. Log base 2 is used as the standard choice.
- **Drift rate**, never defined:
  - (a) a least-squares slope over session pairs;
  - (b) the same slope over the per-day-difference means;
  - (c) as (a), with the line through the origin.
- **Absolute change for Fig. 1h**: the session-level circular mean, or the median over cells.
- **Example mouse of Fig. 1f**: animal 4 (as Extended Data Fig. 1g says), or any mouse with 18 sessions. Its v = 17.06 does not match animal 4's V of 14.6 in Extended Data Fig. 4b.
- **Mouse 2 exclusions**: the Methods exclude it from Fig. 2 offsets, but five values are listed. For the Fig. 3 6-week delay, the Methods cite Fig. 3f where the panel is 3g.
- **Unnamed tests**:
  - Fig. 1i "not significantly different": Wilcoxon or paired t-test. With five mice the Wilcoxon cannot reach p < 0.05.
  - Fig. 1k "significant decoding": per session pair or per mouse.
- **Chance for the decoder**: mean or median time-reversed error (the Methods and the legend differ).
- **XGBoost**: hyperparameters (library defaults are the reading), the random splits and seed for the environment decoder, and how population activity is summed.
- **Other open details**:
  - the per-mouse value in the repeated-measures ANOVA;
  - the shuffle summary (median or mean);
  - which environment is which in Extended Data Fig. 10c;
  - the CellReg threshold for Fig. 4 (0.8 or 0.6);
  - the probe-trial order, taken from session dates;
  - the error-variance measure in Extended Data Fig. 8c;
  - whether mice 6 to 10 count toward the 388 sessions;
  - spike tuning-curve bins for the electrophysiology.

**Thresholds I set where the paper gives none.** A second reader should look at these:
- the threshold for "not diffusive" (Extended Data Fig. 4e);
- the reading of "nearly the entire duration" (all day differences up to 20 days, except at most one);
- the comparison standing in for "reduced retention" in Extended Data Fig. 9;
- the waveform-feature definitions;
- the shuffle 95th-percentile rule for coherent remapping.

The Fig. 3f/g spread of ±0.1 is read as a fit's standard error, so I used 10% as the tolerance there.

**Missing from the paper.** No analysis code exists to settle any of these details. The paper's comparison of the Fig. 4 decoder with "other animals" has no named test or data, so I left it untested. The Methods say five mice were used in all experiments, yet they also describe mice 6 to 10; I recorded the conflict.
