**Verifier report, round 2: asari-2009-02 (doi:10.1152/jn.00577.2009, CRCNS ac-1)**

I agree with 19 of the 21 outcomes. I still dispute the fig7 block, and fig9-mgb-fast-decay rests on an assumption the record does not declare. A few conclusion sentences, the README and one restated round-1 reason need correcting.

## 1. Outcomes and assumptions

The claims file has 21 claims, and the attempt record has 21 outcomes.

| Claim | Record | Agree? | Basis / assumption |
|---|---|---|---|
| methods-recording-counts | partially_reproduced | Yes | 305/39 and 93/14 are exact under both silence readings (cell 14). A1 has 132 cells, or 118 in the five named ensembles, against 123. |
| a1-mgb-firing-rates | partially_reproduced, assumed | Yes | The A1 detector assumption is stated and reasonable. The partial rule holds with both MGB detectors (5.07 and 7.15 Hz, cell 17). |
| fig2-example-reliability | reproduced | Yes, with a note | The outcome depends on the pairwise reading (0.310). Leave-one-out gives 0.436, outside tolerance. fig2-example-long-context marks this same choice `assumed: true`; this claim should too, or say it holds under one reading. |
| fig2-example-long-context | reproduced, assumed | Yes | The pairwise assumption is stated and reasonable, since it alone gives the population 0.31. The gap of 1.60 to 3.97 s is confirmed at 0.1 ms (cell 27). |
| fig3a-proportion-significant | reproduced | Yes | Silence counted, all probes: 187, 0.613 and 0.251 (cell 30). |
| fig3a-significance-decay | partially_reproduced | Yes | Cell 34. |
| fig3b-fractional-power-decay | not_reproduced | Yes | τ1 is 1.27 to 1.78 s in all 8 listed readings (cell 37). The stated reason, "criterion has no rule for partial", also fits methods-recording-counts, which is graded partial. The real reason is that τ, the quantity the claim is about, fails. |
| timescale-longer-than-membrane | reproduced | Yes | Cell 44. |
| fig4-predictability-upper-bound | not_reproduced | Yes | τ1 is within tolerance in 0 of 24 fits (cell 41). |
| fig4-strf-performance-low | partially_reproduced, assumed | Yes | The claims file's test is stated and reasonable; the outcome also rests on using 16 of the paper's 20 cells. Wilcoxon p = 0.0031 and 0.025 (strf cell 10). |
| fig5-example-conductances, fig6-conductance-decay | blocked, data_missing | Yes | No voltage-clamp files in the data set. |
| fig8a-proportion-by-property | partially_reproduced, assumed | Yes, but fragile | The order amplitude > frequency holds by 0.0025 (43/70 against 52/85), so one test flips it. It fails with every set as a test (cell 59). |
| fig8a-significance-fits | not_reproduced, assumed | Yes | The sizes are out of order in every reading (cell 62). |
| fig8b-decay-by-property | not_reproduced, assumed | Yes | This holds only in the main reading. Adding the naturalistic probes gives partial (cell 65). The property-set assumption is stated and checked against Table 1 rows. The main reading is said to be fixed before results; nothing in the materials can verify that. |
| fig8c-relative-effects | not_reproduced, assumed | Yes | Same dependence on the reading as fig8b (cell 68). |
| fig8-natural-synthetic-probes-alike | reproduced, assumed | Yes | Low power: there are no synthetic FM probes, and the synthetic AM probes come from 2 cells. |
| fig9-mgb-fast-decay | reproduced | Yes, but undeclared assumption | Reproduced only if the plateau's κ means the fitted κ, which is close to circular. Against the paper's κ = 2.0 the late mean is 0.39 to 0.60 of it (cell 47). Then the criterion's reproduced rule fails and no rule applies. This should be `assumed: true`. |
| fig9-example-first-bin | reproduced | Yes | Cell 50. |
| fig7-example-frequency-context | blocked, data_missing | Not established | See section 3, point 1. |
| figs1-silence-probe | reproduced | Yes | Cell 74. |

## 2. Text against outputs

All other numbers in the conclusions, Summary, README and record notes match the printed outputs. These sentences do not:

- **Cell 48 (fig9).** "alpha1 5.2 to 12.4 spikes/s ... kappa 0.81 to 1.21" covers only the silence-counted readings; without silence α1 is 1.56 to 3.04. The text also omits that the half-threshold fit without silence over all probes does not converge either (τ1 = 31.3 s). The record's fig9 note, "apart from that fit, tau1 is at most 0.080 s", is true only for the automatic detector: the half-threshold fit without silence gives 0.083 s.
- **Cell 77 (Summary), fig8c row.** "amplitude and frequency effects smaller than natural" is too strong for frequency. In the main reading without silence, with as many probes as the set holds, the frequency interval is 0.552 to 1.066 and includes 1 (cell 68, row 7).
- **README.**
  - The row "Example neuron ... absent from 2 to 4 s | Reproduced" conflicts with the output: the matched probe is significant again from 3.971 s, so it fails the 2 to 4 s reading (cell 26, `strict_2_4 False`).
  - The rows for a1-mgb-firing-rates and fig4-strf-performance-low leave out "resting on an assumption", although both are `assumed: true`.
  - "about 24 minutes" for the STRF notebook; it printed 31.2 min.
- **Restated round-1 reasons.** Most are my own words. Three need correcting:
  - The a1-mgb-firing-rates reason reads "No MGB reading has both means in tolerance, which meets the partial rule." That is a garbled version of what I said: the partial rule is met because the A1 means are below 1 Hz and the MGB evoked mean is above 5 Hz.
  - My round-1 point B12 is not recorded anywhere. It said the "tuning files only" reading is not in the claims file, and the duplicated tuning file is counted twice for two A1 cells.
  - The fig7 entry has no `outcome` field.

## 3. Round-1 points: status

Resolved:
- **B2:** the all-probes reading now runs for fig3b and fig4. It changes τ by at most 0.04 s, and the outcomes are now not_reproduced.
- **B3:** all five fig8 claims are now tested.
- **B5:** the ridge value sits at a grid end in 1 of 208 fits.
- **B6:** 1 − Q is now fitted as a comparison.
- **B7:** the 14 cells behind the 132 against 123 difference are listed.
- **B9:** no change was needed.
- **B10:** `param.sf` is 97656 Hz in all 51 stimulus files.
- **C, threshold scope:** the per-file threshold is explained in the docstring with reference to ViewResp.m. It is described, not quoted.

Remaining points that bear on a conclusion:

1. **fig7 (B1, partly resolved).** The search now covers all 105 recordings. The block still reads `ff` as Hz at face value, and two things argue against that:
   - The five "DMR; frequency variants" recordings with a natural probe include bands at 0.25 to 1, 1 to 4 and 4 to 16 kHz. These are exactly the Figure 7 bands (0.625 to 2.5, 2.5 to 10, 10 to 40 kHz) divided by 2.5.
   - 0.25 kHz is below the 0.625 to 40 kHz carrier range given in the paper's Methods.

   These recordings may hold the Figure 7 design with differently stored band edges. The forward set already reaches 3.673 s in 20060916-ha3-002 (cell 54). Running the significance measure on the three-context subset {0.25–1, 1–4, 4–16} would settle it. Until then, "blocked (data_missing)" and the matching finding are not supported.
2. **fig9 plateau (B8).** The outcome rests on reading κ as the fitted κ (section 1). This should be declared `assumed: true`.
3. **MGB detector (B4, partly resolved).** Cell 18 shows many large deflections between half the threshold and the threshold. File 34 has 1220 spikes, against 23781 at half the threshold. The rates outcome (partial) and the fig9 τ hold under both detectors. The MGB evoked rate and the fig9 magnitudes stay uncertain.
4. **fig8 reading dependence (new, following from B3).** fig8b and fig8c flip to partial when the naturalistic probes are added, and fig8a's partial rests on a 0.0025 margin. The record states this; it should stay explicit wherever these outcomes are reported.

Remaining points that do not affect a conclusion:
- **B11:** the 10-kHz response-sampling reading for the STRF models was not run.
- **B12:** not addressed (section 2).
