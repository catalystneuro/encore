I wrote the claims file at `claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml`. The quote checker reports 34 claims, 33 quotes, 39 statistical values and 0 problems. Nothing is committed.

**What I read.** The version of record (the journal PDF's text), with Results, Discussion, Experimental Procedures and the legends of Figures 1 to 8, plus the supplement (legends of Figures S1 to S8). The article says its supplement includes "Experimental Procedures and eight figures". The supplement as supplied lists only the eight figures on its contents page, so I took the article's Experimental Procedures as the whole Methods. The paper links no code, so none was read. I could not render the PDF, and the text garbles degree, minus and "approximately" signs; quotes avoid those places.

**Counts.**
- 34 claims, all of kind `finding`. 33 have quotes. One, `fig5-regression-coefficients`, is `inferred`, because the coefficients appear only in equations.
- 26 claims carry statistics, 39 values in all.
- All 34 have a criterion.

**Open details, with the readings named for each:**
- **Noise correlation measure:**
  - Whether the reported noise correlations include the renormalization in blocks of 20 trials: without it, or with it.
  - The outlier rule: |z| > 3 or z > 3, with the trial removed for both neurons.
  - The form of the t test: Student or Welch, two-sided.
- **Figure 2C:** where the 31 windows sit. The reading is from stimulus onset to the end of the stimulus.
- **Figure 3:** whether the permutation test was run per condition or on both together. For the Fano fit, which mean and variance enter; the reading is per neuron and heading.
- **Figure 5:** whether the noise correlation is pooled across conditions or taken from the same condition as the signal correlation. How the common-slope plane fit is formed (two readings). Ordinary least squares is shown as a variant.
- **Figure 4:** tuning-curve interpolation (linear or cubic spline), and raw or log thresholds in the ANOVA.
- **Simulations (Figures 6 and 7):** the paper does not give tuning amplitude, baseline, counting window, the headings used for signal correlation, or how bandwidth is defined. The readings are named as assumptions, and the Figure 6B grid range is read from the figure.
- **Figure 7B:** which condition, which pairs (127 or 179) and the interpolation.
- **Figure 8C:** which pairs, and visual or vestibular preference.
- **Smaller ones:** the sample for Figure 1F (179 pairs, or the 127 under 1 mm); the Figure S4 bootstrap count and reference grid (standard choices); renormalization blocks over the session or within each condition (Figure S8C); the unit of the eye-movement t test; the prestimulus window for the Discussion claim; and the identity of the Figure 1 example pair.
- **Per-animal consistency (Figure S2B):** the paper gives no test, so a reading is set.

**Missing from the paper:**
- Several reported p-values disagree between places: the Figure S6 test is p = 0.3 in the Results and p = 0.26 in the legend, and the renormalization test is p > 0.3 in the Methods and p = 0.5 in the Figure S8 legend. Both are recorded.
- The paper does not deposit the single-electrode database (Figure 4, S4, 8A/B), the training histories (2A) or the eye records (S8) anywhere else. The paper uses spike times, distances and tuning curves for several claims. The data descriptor lists only signal and noise correlations per condition and preferred headings for the 127 pairs, so the author will need to check whether the dataset holds more.
- The 10% tolerance on the trained intercept of 0.005 is tighter than any fit can reach. I kept it as the protocol default and asked for the fitted interval to be reported beside it.
