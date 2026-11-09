**A. Outcomes for the 45 claims in the claims file** (the notebook tests all 45 and treats none as blocked)

| Claim | Outcome | Reason |
|---|---|---|
| recorded-units | partially_reproduced | 435 neurons and 14 rats match. There are 195 distinct sessions against 194 (cell 15). The criterion says to report this as a difference in the data set. |
| cue-responsive-screen | reproduced | With the Methods' rates: 271 neurons, 160 sessions, all 14 rats, within tolerance. The authors' floored rates give exactly 257/153 (cell 17). |
| fig1f-suppression-cue-effect | reproduced | F(2,26) = 74.6 to 80.9, p ≈ 1e-11, danger > uncertainty > safety under every O3 reading and both populations (cell 19). |
| fig1f-differential-suppression | reproduced | All three intervals exclude zero and all means are within tolerance (0.29/0.51/0.80) under every reading (cell 21). |
| fig2-excited-inhibited-split | partially_reproduced | On the paper's 257 neurons, Hz with two window means gives 130/127, within tolerance. On the Methods' 271 neurons no claims-file reading is within tolerance: 139 to 155 inhibited (cell 23). |
| ancova-excited-no-baseline-effect | reproduced | On the 131 neurons, p = 0.235 (O1a) and p = 0.182 (O1b). On groups B (Methods' rates) p < 0.001, so the absence depends on A1 (cell 27). |
| ancova-inhibited-baseline-effect | reproduced | p from 1.4e-9 to 1.5e-4 in every reading and group (cell 29). |
| kmeans-three-clusters | reproduced | Reading: CV over the 10 s baselines, raw features, Matlab default of one start after rng(1). This gives 74/34/18, and the F pattern matches, amplitude ratio p = 0.12 (cell 31). The partition is a local optimum (see B3). |
| clusters-differ-in-cue-firing | partially_reproduced | On the paper's clusters under O1a/b all three pairs have p < 0.05, but Low vs Intermediate has p = 0.035/0.011, not < 0.005. Only the code normalization gives p < 0.005 for all pairs (cell 36). |
| clusters-by-rat | reproduced | 11/9/5 rats, and 11 High neurons from pa02, on the main clusters (cell 38). |
| fig3a-low-differential-cue-firing | reproduced | All three effects p < 1e-11 and cue means order D < U < S under O1a/b (cell 42). |
| fig3b-low-inhibited-to-threat-cues | partially_reproduced | The pattern holds under O1b. Means are about 1.7x the paper's (danger onset −0.61 against −0.37 ± 0.08). Under O1a the safety late-cue interval is above zero (cell 44). |
| fig3b-low-differential | partially_reproduced | O1b: the pattern holds but the late-cue U−S mean is −0.28 (tolerance −0.14 ± 0.11). No O1 reading meets both conditions (cell 46). |
| fig3c-intermediate-differential-cue-firing | reproduced | All effects significant and onset order D < U < S (cell 48). |
| fig3d-intermediate-inhibition | partially_reproduced | The pattern holds under O1a/b. Means are about 1.8x the paper's (danger onset −0.97/−0.86 against −0.54 ± 0.15) (cell 50). |
| fig3d-intermediate-differential | partially_reproduced | Under O1a/b the late-cue D−U interval contains zero ([−0.66, 0.04]) and the U−S means are out of tolerance. The code normalization meets everything (cell 52). |
| supp5-low-cue-correlations | not_reproduced | For Low neurons, onset U−S r = 0.36/0.38 with p ≤ 0.0014 is positive under every reading (cell 54). The code's first-5 s period would pass (see B8). |
| supp6-low-nosepoke-pauses | partially_reproduced | Low shows no inhibition under every reading. Intermediate post firing is below zero under 5 s/(ii) ([−0.65, −0.05]) and under code/code (cell 64). |
| fig4a-low-rt-over-fo | reproduced | Relative-threat (RT) beta is further from zero than fear-output (FO) beta at all five assignments in every reading. Both are negative (cell 70). |
| fig4a-low-025-better-than-000 | reproduced | p = 0.007 to 0.012, and \|RT\| at 0.25 is greater than at 0.00 in every reading (cell 72). |
| fig4a-low-025-similar-050 | reproduced | p = 0.36 to 0.58 in every reading (cell 74). |
| fig4b-low-dynamic-shift | reproduced | Model (a) gives p = 0.003 to 0.005 in every reading. Models (b) and (c) give p > 0.1 (cell 76). |
| fig4c-low-early-late-betas | partially_reproduced | Model (a) means are within tolerance, but the late 0.25 interval excludes zero above it ([0.12, 1.00]) under every claims-file reading. Only the code firing gives the full pattern (cell 78). |
| fig4d-low-early-late-shift | reproduced | Model (a): 1.10 / −0.84 / 1.94, all intervals with the reported signs and within tolerance (cell 79). |
| fig4e-int-025-better-than-000 | reproduced | O2a and O2c: RT > FO at every assignment, p = 0.006 to 0.012, and 0.25 > 0.00 (cell 81). |
| fig4e-int-025-similar-050 | reproduced | p = 0.42 to 0.48 (cell 83). |
| fig4f-int-no-assignment-interval | reproduced | p ≥ 0.055 in every reading on the paper's 34 neurons (cell 85). |
| fig4g-int-early-late-betas | not_reproduced | No claims-file reading gives the pattern: model (a) early 0.25 contains zero and late 0.50 is below zero, and model (c) early 0.50 is below zero. Only the code firing reproduces it (cell 87). |
| fig4h-int-early-late-shift | reproduced | Model (a), every O2/O3 reading: 1.39 [0.58, 2.33], −0.81 [−1.82, 0.06], 2.20 [0.49, 4.04], all within tolerance (cell 88). |
| fig4-low-int-combined | reproduced | Models (a) and (b): assignment x interval p ≤ 0.022, three-way p ≥ 0.70 (cell 90). |
| fig5a-low-reward-firing | reproduced | Every reading meets all three conditions (cell 100). |
| fig5bc-reward-pre-post | reproduced | Events (a) and (b) with scaling (i): pattern holds and values within tolerance (cell 102). |
| fig5d-f-low-reward-cue-correlations | partially_reproduced | Signs and p values hold in every reading. R² values are outside the 10% tolerance (cell 104, see B7). |
| fig5-low-fisher-comparisons | reproduced | D vs U p = 0.17 to 0.49 and U vs S p ≤ 0.0055 in every reading (cell 105). |
| fig5g-i-intermediate-no-reward-cue-correlation | reproduced | All correlation p ≥ 0.14 and all Fisher p ≥ 0.31 (cell 106). |
| fig6a-excited-differential-cue-firing | reproduced | All effects significant and onset order D > U > S (cell 56). |
| fig6b-excited-period-firing | partially_reproduced | Every increase and all six difference intervals exclude zero above it. Safety delay is below zero in every reading, and the means are within tolerance only with the code normalization (cell 58). |
| supp8-excited-cue-correlations | partially_reproduced | On the 131 neurons under O1a/b, delay U−S r = −0.08 (p = 0.34). It passes with the code normalization and on groups B (cell 60). |
| supp9-excited-nosepoke-pauses | partially_reproduced | No increase under 10 s, under 5 s/(i) and under the code pauses. Under 5 s/(ii), post 0.17 [0.04, 0.34] and post−pre are above zero (cell 66). |
| fig6-excited-assignment-050 | partially_reproduced | 0.25 vs 0.50 significant and 0.50 has the largest beta in every reading. 0.50 vs 0.75 has p = 0.12 to 0.30 under claims-file readings and p = 0.0497 only under the code variant (cell 92). |
| fig6c-excited-regressor-interval | partially_reproduced | No claims-file reading gives both effects: O2b gives the regressor effect only, O2c the interaction only (cell 94). |
| fig6d-excited-betas | reproduced | O2a and O2c with both O3 readings: pattern holds and values within tolerance (cell 96). |
| fig6ef-excited-reward-firing | reproduced | Events (a) and (b) with scaling (i): interval effect p < 1e-6 and both intervals above zero within tolerance (cell 108). |
| fig6g-excited-reward-cue-correlations | partially_reproduced | All three r are positive with p < 0.05 in every reading. R² is out of the 10% tolerance in every reading (cell 110). |
| fig6-excited-peak-cue-vs-reward | partially_reproduced | Pattern holds only for O1a, O5b, scale (i), where the safety mean of −0.37 is out of tolerance. Those values may not be comparable (B6) (cell 112). |

Totals: 26 reproduced, 17 partially_reproduced, 2 not_reproduced, 0 blocked. Nothing was blocked, and the archive listing confirms the data set is one zip (MD5 43a2887f…, matching checksums.md5) plus the descriptor documents. The paper states no chance level for the cue screen. Six uncorrected tests imply about 26% false positives per neuron under the null, and the notebook does not report this.

**B. Problems**

1. [affects a conclusion] Cells 0 and 24 (A1). The header says the Methods' reading is the main result and the authors' code is a variant. A1 then reverses that for the neuron groups: it uses the code's floored-rate screen and the code's per-trial normalization for the split. On the Methods' population (groups B, 271 neurons), fig2 fails under all four claims-file readings, and ancova-excited becomes significant. The excited/inhibited split on the 257 is also defined by the code normalization, not by a claims-file reading. The Hz two-means reading gives 130/127, and the notebook never shows how far those groups differ from the ones it used.
2. [affects a conclusion] `vp.normalize_cue` and `vp.trial_firing` against the "code" variant. Under the Methods' normalization (both O1 readings), the means come out 1.7 to 2x the paper's. The authors' per-trial normalization (per-trial floored 2 s baseline, Z over single trials) matches the printed values. Taken together, this suggests the paper's Methods do not describe the computation the figures were made with. That decides fig3b, 3d, 4c, 4g, 6b, 6c and 6-assignment. The notebook never isolates which element causes the gap: per-trial vs trial-averaged Z, 2 s vs 10 s baseline, or flooring.
3. [affects a conclusion] Cells 31 to 34, kmeans. The claims file says the seed "cannot change a conclusion beyond the edge of an interval". Here it does. Only 98 of 300 single starts reach 74/34/18, and the lower-SSE optimum (58/46/22, SSE 7254 vs 7997) fails the counts. Every cluster claim (fig3, fig4, fig5, clusters-by-rat) rests on this partition. The main clusters also use the code's features (CV over 20 s, floored baseline), which is not a claims-file reading. The claims-file reading (base10, raw, rng(1)) gives the same counts, but the notebook does not check that the memberships are identical.
4. [affects a conclusion] Cells 64 and 66, nose-poke pauses. The notebook's header table calls supp6 and supp9 "reproduced", but readings 5 s/(ii) (and code/code for Intermediate) show the effect the paper says is absent. Recording was paused between trials, so pause readings can only fall in the about 19.5 s after each trial. Under the 10 s reading, Intermediate neurons have a median of 0 events and only 14 of 34 neurons contribute, which is too little data to support a claim that an effect is absent.
5. [affects a conclusion] Cell 36. Groups B's clusters (74/54/20) are not the paper's clusters, so the all-p < 0.005 result on B should not count toward clusters-differ-in-cue-firing.
6. [affects a conclusion] Cell 112. Under scaling (i), the cue values are Z-scored over cue bins and the reward values over 16 reward bins. They are on different scales, so the cue − reward difference has no common unit. Scaling (i) is the only claims-file reading where the pattern holds.
7. [affects a conclusion] Claims file, fig5d-f and fig6g tolerances. A 10% tolerance on R² (±0.0006 for a null R² of 0.006) is unreasonably tight. The "partial" outcomes come from it, not from the data.
8. [affects a conclusion] Claims file, supp5 and fig6b. supp5 uses a 1 s onset period. The Supplementary Information was not read, and the authors' code correlates the first 5 s; with that period the Low criterion passes. For fig6b, the criterion requires safety late-cue and delay intervals to contain zero. The paper says only that increases were limited to threat cues, so a safety value below zero does not contradict it. These are possible misreadings by the claims file, reported here and not corrected.
9. [does not affect a conclusion] Cell 76, fig4b. The interaction holds only for model (a), which the code supports. Models (b) and (c) give p > 0.1.
10. [does not affect a conclusion] Cell 9. Four same-session unit pairs share more than 70% of their spikes and are likely duplicate units. They are kept in every population.
11. [does not affect a conclusion] Helpers tested on synthetic data:
    - `rm_anova` matches hand-computed sums of squares for two-way repeated measures, mixed group x A x B, and covariate x A x B.
    - `boot_ci` had 0.96 coverage on exponential samples with n = 30.
    - `fisher_z` returns 0.79 / 2.99 from the paper's R² values, as the claims file predicted.
    - Cell 19 contains a dead expression (`... if False else r.values`).

**C. What I could not check**

- Whether the "code" variant reproduces `vpAnalysis.m` and `cubeScriptPR25.m` faithfully. The scripts are inside the zip, which I did not download. A cell printing the cited script lines would settle it.
- Whether the main clusters and the claims-file-reading clusters have the same members. An adjusted Rand index or crosstab in cell 31 would show it.
- Which part of the code normalization makes the paper's values match. A cell varying one element at a time (per-trial vs averaged, 2 s vs 10 s baseline, floor) for fig3b would show it.
- How much the A-group split differs from the claims-file Hz two-means split on the 257. A crosstab in cell 25 would show it.
- How many neurons and events contribute under each pause reading, per neuron. Event counts per neuron in cells 64 and 66 would show this.
- The outcomes above were judged independently of the notebook's header summary table (cell 0), which was not removed despite the instructions.
