**A. Outcomes** (34 claims in the claims file. Population claims are judged on the notebook's primary partition, N4 (ii), and checked against N2 (ii), the other claims-file partition that looks like the paper's: 7/27/44/91/24 units.)

| Claim | Outcome | Reason |
|---|---|---|
| units-recorded | not_reproduced | Cell 8: 368 units and 7 rats match, but there are 90 sessions, not 95, with zero tolerance. The script's own count gives 84. |
| cue-responsive-193 | reproduced | Cell 10, reading (b): 211 units, 81 sessions, at least 7 per rat. Reading (a) fails because rat ac07 has only 6. |
| fig1c-acquisition | blocked (data_missing) | I checked the bucket listing myself: it holds only `data.zip` and the docs. Cell 13 lists the zip, and it has no pre-surgery sessions. Nothing in this claim can be tested. |
| fig1g-discrimination | reproduced (fragile) | Cell 17: the ANOVA has p < 0.05 and all three means are within tolerance under every reading. With the standard studentized CI, the uncertainty-minus-safety CI contains zero in 5 of 6 readings. In the sixth ((b), 0/0 = 0) it excludes zero at the median, but in only 68% of seeds. The non-reflected interval reproduces all three of the paper's CIs to within about 0.07. |
| fig1h-poke-rate-unrelated | reproduced | Cell 19: no p < 0.05 in 3 of the 4 claims-file readings. Under (a) with 0/0 = 0, danger gives R = 0.76, p = 0.048. |
| fig1h-discrimination-safety | reproduced | R is between -0.978 and -0.986 in every reading. |
| fig2-five-clusters | partially_reproduced | No reading is within tolerance (cell 23). N4 (ii) and N2 (ii) show all five named patterns, and Threat Inhibited and Bidirectional Valence are within tolerance. Threat Excited (6–7), Danger Excited (44–45) and Non-Selective (24–25) are out. |
| populations-by-rat | not_reproduced | Cell 28: the primary partition gives 3/5/6/7 rats against the paper's 2/4/6/7. No partition matches. Sessions (77) are within tolerance. |
| most-units-threat | reproduced | The four differential populations hold 87–97% of units in every claims-file partition. |
| fig3ab-rate-cv-unimodal | reproduced | Every dip p is 0.61 or higher in every partition and CV reading. |
| fig3c-waveform-bimodal | reproduced | Primary partition, boundary (a): all units p = 0, BV p = 0, DE p = 0.118 with 82% narrow, TI 36% narrow, BV 51.7% narrow. I rendered Figure 3C: the dashed line is at about 0.39 on a 0–0.6 ms axis, and the bars (about 38/80/50% narrow) agree. Dip values for TI (0.125) and DE (0.067) are out of tolerance; this is reported only, not judged. |
| fig4ab-thi-threat-firing | partially_reproduced | ANOVA significant and both CIs exclude zero. The means (-0.64 to -0.74) are outside -0.47 ± 0.15 under all claims-file normalizations. |
| fig4b-thi-danger-equals-uncertainty | reproduced | The danger-minus-uncertainty CIs contain zero under all normalizations, in both N4 (ii) and N2 (ii). |
| fig4cd-de-danger-firing | partially_reproduced | All CIs exclude zero and the ANOVA is significant. Onset uncertainty-minus-safety (0.54–0.66) and danger-minus-uncertainty (0.35–0.46) are out of tolerance. |
| fig4ef-bv-danger-decrease | partially_reproduced | The CIs exclude zero and the share is 46.1%. Onset (-0.29 to -0.36) and late (-0.17 to -0.21) means are out of tolerance. |
| fig4f-bv-safety-variability | reproduced | Primary partition, all 4 normalizations: both Pitman-Morgan p < 0.05, with variance ratios of 1.68–1.83. N2 (ii) agrees. |
| fig5ab-the-onset | not_reproduced (partition-dependent) | On the primary partition (n = 6) the interaction p is 0.08–0.11. N2 (ii) (n = 7, p = 0.013) and N4 (i) do reproduce it. |
| fig5cd-ns-nonselective | not_reproduced | The cue effect has p < 0.05 in N4 (ii) and N2 (ii), and the late CI excludes zero under 3 normalizations. |
| fig6-similarity-anova | reproduced | All three terms have p < 0.05 in N4 (ii) and N2 (ii). |
| fig6d-thi-similarity | reproduced | t(27) = 3.08 and 3.49, both p < 0.0056. N2 (ii) agrees. |
| fig6e-de-similarity | not_reproduced | p = 0.023 and 0.011 (primary) and 0.016 and 0.0047 (N2 (ii)). Both comparisons must pass 0.0056 and do not. |
| fig6f-bv-no-similarity-difference | reproduced | No p < 0.0056. |
| fig6-thi-greatest-similarity | reproduced | p ≤ 0.0006 against both populations, and TI danger/uncertainty is the largest of the nine cells. |
| fig7-tuning-curves | reproduced (fragile) | Under per-trial readings (a) and (b) the extremes are 0.75, 0.50 and 0.50. The TI choice of 0.75 over 0.50 rests on -1.020 vs -1.013. Reading (c) and N2 (ii) put TI at 0.50. |
| fig8ab-thi-exaggerated-threat | reproduced (reading-dependent) | Joint model with per-trial reading (a) (0/0 dropped or set to 1) meets every condition. Readings (b) and (c) and the separate models do not. |
| fig8cd-de-exaggerated-threat | partially_reproduced | Exaggerated-threat CIs are above zero and fear-output CIs contain zero. The regressor effect has p = 0.125, and the early difference CI contains zero. |
| fig8ef-bv-exaggerated-threat | partially_reproduced | The ANOVA terms are significant (p = 0.025 and 0.0485). The early exaggerated-threat mean of -0.466 is just outside -0.31 ± 0.14. |
| fig9a-reward-firing | not_reproduced | Under readings (b, sd) and (b, z16), TI has an interval effect (p ≈ 1e-4 and 9e-6). Reading (a) leaves at most 1 event per unit. |
| fig9bcd-reward-pre-post | not_reproduced (unreliable) | The BV pre CI excludes zero, BV post (1.67) is out of tolerance, and TI post excludes zero. The result is affected by problem 1. |
| fig9efg-reward-cue-correlations | partially_reproduced (unreliable) | Under (b, sd) and (b, z16) the BV part holds and TI shows no difference. The DE danger correlation is significant. Affected by problem 1. |
| fig9hij-danger-safety-correlations | not_reproduced | The BV p is 0.33–0.40 under all claims-file normalizations. Only the script normalization reproduces it. |
| fig10a-poke-cessation-anova | not_reproduced | The interval effect has p < 1e-4 under the (b) readings. Reading (a) is an artefact (problem 2). |
| fig10bcd-poke-cessation-pre-post | reproduced (unreliable) | Passes under (b, sd) and (b, z16), but problems 1 and 2 apply. |
| fig10efg-poke-cessation-cue-unrelated | not_reproduced | Under (b), the DE danger correlation has R² = 0.20, p = 0.002. It passes only under reading (a), which has 0–4 events per unit taken at the end of the recorded segments. |

**B. Problems**

1. [affects a conclusion] `nac.event_trace`: the baseline is `m[:4]`, the bins from 2 s to 1 s before the event. The Methods and the claims file say the 1 s before the event (bins 4–7). I confirmed this on synthetic spikes: spikes placed only in the 1 s before the event survive as +40 in bins 4–7 when they should cancel to 0. The `code` branch does the same. The ANOVAs (fig9a, fig10a) are unaffected because they are invariant to a per-unit offset. The pre and post CIs of fig9bcd and fig10bcd, and the across-unit correlations of fig9efg and fig10efg, are affected.
2. [affects a conclusion] `nac.iti_events` and `nac.cessations`: the files hold data only from 20 s before to about 31–33.5 s after each onset (cell 6). Windows that run past the end of a recorded segment are not excluded. Also, the last poke before a recording pause counts as a cessation, because the next poke comes after the pause. Reading (a) consists only of such events, which explains F_bin ≈ 56 in cell 85. Reading (b) contains some of them too. This affects fig10a, fig10bcd and fig10efg, and possibly fig9.
3. [affects a conclusion] `nac.boot_ci`, used throughout: cell 17 shows that the paper's three fig1g CIs are reproduced only by the non-reflected interval (`mirrored=True`). Every judgement uses the standard reflected form. This decides the fig1g uncertainty-minus-safety CI and could flip any CI near zero elsewhere. The module's claim that using an analytic SE "cannot move a bound by more than resampling noise" is not tested; it is doubtful for n = 5–7.
4. [affects a conclusion] Cell 24: the primary partition is picked by "highest smallest cosine", a rule that is not in the claims file. N4 (ii) (0.79) and N2 (ii) (0.77) are almost tied, yet they give different outcomes for fig5ab and for the TI extreme in fig7.
5. [does not affect a conclusion] Cell 11: the 193 units used downstream come from the script's floored-rate screen, which is neither of the claims-file readings. It matches the paper's 193 units and 82 sessions exactly, but the notebook should state it as an assumption.
6. [does not affect a conclusion] Cells 40–89: outcome tallies include partitions whose clusters do not fit their names (`min_cosine` < 0, for example N1 (i) "Danger Excited" with a negative danger centroid). The tallies are not meaningful.
7. [does not affect a conclusion] fig6 readings (a) and (b) (cell 54), and fig7 per-trial readings (a) and (b), are mathematically identical: Pearson R is unchanged by the rescaling, and the regression is orthogonal to the within-type baseline differences. They are not independent readings.
8. [does not affect a conclusion] Cell 10: the "null reference" with onsets shifted by 60 s falls in unrecorded time (no spikes at all), so it does not estimate a false-positive rate. Cell 73 says the reward SD comes from "N1", but `sd_n1` uses `PRIMARY_NORM` (N4).
9. Where the claims file misreads or misses something in the paper, reported and not corrected:
   - 0/0 suppression ratios: only setting 0/0 = 1 reproduces the paper's F(2,12) = 57.41 exactly (57.405 in cell 17). The claims file does not list this reading.
   - Normalization: the claims-file normalization follows the Methods text, but the script normalization reproduces the paper's effect sizes much more closely. Examples: fig4cd 0.24/0.25/0.16 against 0.22/0.21/0.17; fig8ef -0.303/-0.389 against -0.31/-0.39; fig9hij R² 0.21/0.062 against 0.25/0.06; BV reward post 0.463 against 0.47.
   - CI form: the paper's CIs imply the non-reflected interval (problem 3).

**C. What I could not check, and which output would have let me**

- Whether `cubeScriptPR25.m` and `mainAnalysis.m` do what the notebook says: the 0/0 = 1 setting, the reward and cessation baseline columns, the `bootci` call. Printing the relevant script lines would settle it.
- How much problem 1 changes fig9bcd, fig9efg, fig10bcd and fig10efg. Re-run tables using bins 4–7 as the baseline would show this.
- How many reward and cessation events per reading have windows running past the end of the recorded segment. A count per reading, and re-run tables with those events excluded, would show this.
- Whether neural CIs near zero change with the CI form or the seed. The CI-based claims (fig4, fig5, fig8, fig9b, fig10b) recomputed under both interval forms and several seeds would show this. Cell 17 also does not print the seed-1001 exclusion flags for fig1g.
- Why there are 90 sessions instead of 95. A per-rat session count to set against Extended Data Figure 1-1 (not available here) would help.
