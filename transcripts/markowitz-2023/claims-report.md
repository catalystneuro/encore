I rewrote `claims/markowitz-2023.yaml`. The quote checker reports 41 claims, 41 quotes, 38 statistical values and 0 problems. Nothing is committed.

**Text read**
- **Paper:** the version of record (CC BY 4.0) from Europe PMC, PMC9892006: main text, figure legends, Methods and Extended Data legends.
- **Supplement:** only a Reporting Summary and a Peer Review File. No result rests on them, so nothing the claims need is missing.
- **No PDF:** numbers that appear only inside figure panels (for example the r values in Fig. 2b, 2i and 5b) could not be read. No claim relies on them.
- **Code:** github.com/dattalab/dopamine-reinforces-spontaneous-behavior at commit 14ed714.

**Claims:** 41, all with quotes, none inferred. 31 have statistics, 20 have expected values, and all 41 have a criterion.

**What changed**
- **Kept:** all 24 earlier ids.
- **Data-derived choices removed:** the old file was written after the data check had been seen. I took out the choices that came from the data: group and site names in the files, the 0.17 s stimulation latency, and the label range 0 to 36.
- **Criteria that misread the code, corrected:**
  - Fig. 1e: the code uses 1,000 shuffles, not 100, with a two-sided Holm test.
  - Fig. 1h: the measure is now open between three readings.
  - Fig. 3e: counts cover the whole session and the baseline is counted twice.
  - Fig. 2e: segment boundaries come from `dlight_03`.
  - ED7: the transient rate is now in Hz.
- **ED7 "no usage prediction":** now judged on the paper's actual test, the ED7e encoding-model comparison (U = 102).
- **Criteria added** to fig1f, fig2k, fig3i, ed10d, fig4b, fig4c, fig4f, fig4h and fig5, which had none.
- **17 claims added:**

| Group | New claims |
|---|---|
| Fig. 1 and ED2–3 | ED2a syllable count and durations; ED3c keypoint correlations; Fig. 1j |
| Fig. 2 | the Fig. 2e autocorrelation control; Fig. 2g; Fig. 2h |
| ED6 | ED6b and ED6e encoding models |
| ED7 (DMS against DLS) | ED7b transient shape; ED7d peaks; ED7e velocity |
| Fig. 3 and ED10 | Fig. 3c calibration; Fig. 3j,k; ED10a,b specificity; ED10e duration; ED10i place preference |
| Fig. 4 | Fig. 4i extra dopamine |

- **Dropped:** the `dataset:` block, since a paper's own claims file leaves it out.

**Details the paper leaves open, and the readings named**
- **dLight reference fit:** the Methods fit a slope and bias. The code fits no intercept, which is kept as a variant.
- **Quality control:** (a) the Methods' maximum percentage dF/F0 above 1.5; (b) the code's 90th percentile of smoothed dF/F above 1.5, plus dropping any session with raw dF/F above 1.0.
- **Fig. 1e:**
  - Transient threshold: 1.96 (code) or 1 s.d. (ED1h and ED7a).
  - Significance: per bin size at P < 0.05, or two-sided Holm with 5 consecutive bin sizes.
  - "Short timescales": every bin size below 10 s, or only the shortest (0.25 s).
- **Fig. 1f:** the compared quantity is either the mean |z| over ±1 s (code) or the peak from 0 to 0.3 s. Shuffle count is 1,000 (Methods) or 100 (legend).
- **Fig. 1h amplitude:** (a) the mean of per-instance peaks; (b) the mean over 0 to 0.3 s of the per-mouse average waveform (the code gives H = 209.49); (c) that waveform's peak (code gives 193.86). The paper's 209.29 appears nowhere in the code.
- **Fig. 2e, "several minutes":** significant at every n up to 390 syllables (about 3.7 min) or up to 210 (about 2 min). One-sided significance is the main test; the code's two-sided Holm test is a variant.
- **Fig. 2k binning:** 20 equally spaced bins per syllable (Methods) or equal-count bins per mouse (code). Pearson or Spearman, both shown.
- **Fig. 2g:** non-overlapping 3-min windows or windows sliding by 30 s.
- **Spontaneous peaks for Fig. 2a and 3c:** the food-reward experiments or all baseline experiments. The evoked-peak window is 0 to 0.3 s or 0 to 0.6 s.
- **Fig. 3e baseline day:** the Methods' most recent baseline day, or the code's Monday within 5 days (variant).
- **Fig. 3l:** the main test is per group over experiments, as the code runs it. Per-mouse tests and the Methods' pre-onset subtraction are variants.
- **Fig. 4f catch-trial dLight window:** 0 to 0.3 s or 0 to 0.6 s.
- **Fig. 4b/4c per-mouse value:** mean (Methods) or median (code, variant).
- **ED3c:** r pooled over all bins or averaged per mouse.
- **ED2a durations:** pooled over the DLS photometry experiments or over all open-field experiments with offline labels.

**Thresholds fixed here because the paper gives none** (each is stated as an assumption in its criterion):
- Fig. 1j "weakly": |r| < 0.3.
- Fig. 3j,k: the bootstrap interval excludes 0.
- Fig. 4i "closely matched": the best offset lies within the interquartile range (or, for partial, the central 95%) of evoked peaks.

**Missing from the paper or its code**
- **Computed outside the repository**, so those criteria rest on the Methods and the readings above:
  - the raw-to-dF/F pipeline;
  - movement-initiation detection;
  - peak detection for Fig. 2a and 3c;
  - the Fig. 1l classifier;
  - the Fig. 2g cross-correlation;
  - the catch-trial dLight table for Fig. 4f.
- **Statistics with no stated value:** the paper gives no accuracy for Fig. 1l and no rise or decay method for its 67 and 100 ms values.
- **Panels not covered** because their numbers sit only inside figures: the r values of Fig. 2b and 2i, and the Fig. 5b correlations.
