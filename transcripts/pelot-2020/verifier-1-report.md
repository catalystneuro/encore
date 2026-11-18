**A. Outcomes** (35 claims in the claims file, all of them addressed in the notebook)

| Claim | Outcome | Reason |
|---|---|---|
| rat-sample-set | reproduced | Cell 18: 9 cervical and 9 subdiaphragmatic samples, 4F/5M at each level, 10 Sprague-Dawley rats, 75–268 days, 381.1 ± 118.4 g. |
| nerve-diameter-anova | reproduced | Cell 28, unbounded REML: species F = 599.6 (p < 1e-4), level F = 11.05 (p = 0.0029), interaction F = 2.455 (p = 0.107). The paper has 577.1, 11.01 and 2.445. The bounded REML variant makes the interaction significant (p = 0.024); see B4. |
| human-pig-nerve-diameter-similar | reproduced | Cell 30: the four means are within the paper's SDs (1.922, 2.195, 1.677, 1.638 mm). Tukey human vs pig main effect p = 0.157 (paper 0.183); effect size −0.32. |
| rat-nerve-diameter | reproduced | Cell 20: 0.2577 ± 0.0249 and 0.1352 ± 0.0148 mm. Both means and both SDs are within tolerance. |
| rat-ten-times-smaller | reproduced | Cell 32: rat vs human and rat vs pig p ≈ 1e-12 to 1e-14, rat smaller. Ratios 0.134, 0.117, 0.081 and 0.082, all inside 0.05–0.2. |
| nerve-cervical-larger | reproduced | Cell 34: level p = 0.0029, cervical least squares mean 1.425 > 1.131 mm. Relative difference human 0.127 < pig 0.254 and rat 0.475. This rests on the claims file's own reading of "clearest". |
| fascicle-number-human-pig | reproduced | Cell 36: means within the SDs. Species p < 1e-4, level p = 0.026, interaction p = 0.12 (F = 216.7, 5.79, 2.61 against the paper's 213.8, 5.486, 2.481). |
| rat-subdiaphragmatic-multifascicular | reproduced | Cell 22: all 9 cervical samples have one fascicle. Exactly R16-1, R22-1 and R23-1 are multifascicular (2, 3 and 2 fascicles). |
| rat-multifascicular-proportions | reproduced | Cell 24: 9 of 9 values within 10%, essentially exact. |
| fascicle-diameter-anova | reproduced | Cell 38: species p = 0.0011, level p < 1e-4, interaction p = 0.0085. Same result in the code-rule and bounded variants. |
| rat-fascicle-diameter | reproduced | Cell 26: 0.2486 and 0.1291 mm, within the paper's SDs. The code's first-trace rule gives 0.1211 ± 0.0323, the paper's numbers exactly (B1). |
| cervical-fascicle-diameter-species | reproduced | Cells 40–41: human vs pig p = 0.00024, human larger. Rat vs human p = 0.716, rat vs pig p = 0.137. Means 0.3548 and 0.1545 mm. |
| subdiaphragmatic-fascicle-diameter-comparable | reproduced | Cell 42: p = 0.283, 0.995 and 0.883, means within the SDs. The code-rule variant gives 0.289, 0.896 and 0.995; the paper has 0.3049, 0.896 and 0.9947. |
| fascicles-larger-cervical | reproduced (fragile) | Cell 44: human p = 1e-5, pig p = 0.048, rat p = 0.044, all with cervical larger. The pig and rat results depend on the degrees-of-freedom method and on which rat fascicle is used (B2). |
| rat-diameter-like-fascicle | reproduced | Cell 46: reading (a) holds at both levels (257.7 µm between 154.5 and 354.8; 135.2 µm between 110.1 and 163.5). |
| human-pig-tissue-proportions | reproduced | Cell 48: all 8 values are within the stated SDs. |
| rat-level-ratios | reproduced | Cell 50: reading (b) gives 0.317 and 0.678, both within 10%. Reading (a) gives 0.270 and 0.525, both outside. The criterion accepts either reading. |
| human-pig-level-ratios | reproduced | Cell 52: 0.198, 0.421, 0.873 and 0.746, all within 10%. |
| human-variability | reproduced | Cell 54: human CV is above pig and rat for nerve diameter and mean fascicle diameter at both levels. Reading (b) also holds for human against pig. |
| literature-comparison-human-pig | partially_reproduced | Cell 58: 9 of 11 parts hold. Human cervical endoneurial area fails: Seki L 1.32 mm² is above the paper's 0.922 + 0.337. "Ranges overlap" fails only because right-side reports are included (B5). |
| rat-literature-comparison | partially_reproduced | Cell 59: the subdiaphragmatic means are above every published mean, so that part holds. Only 1 of 4 published cervical diameters, and 1 of 4 areas, fall within the paper's mean ± SD. The claims file defines no partial outcome; this is my call for one part out of two (B5). |
| perineurium-species-order | reproduced | Cell 69: human > pig > rat across 32–284 µm and at 250 µm. |
| perineurium-ratio-decreases | reproduced | Cell 71: the fitted ratio decreases for all three species. Spearman ρ = −0.92 (human), −0.60 (pig), −0.78 (rat). |
| human-perineurium-fit | reproduced | Cell 65: n = 73, R² = 0.7488 with a linear fit with intercept. |
| pig-perineurium-fit | reproduced | Cell 67: n = 284, R² = 0.2984, the same value as the fit stored in the author's file. |
| rat-perineurium-fit | reproduced | Cell 63: all fascicles, linear with intercept, n = 22, R² = 0.7652. |
| perineurium-thicker-larger-fascicles | reproduced | Cell 73: positive slopes with CIs above zero; Spearman ρ = 0.92 (human) and 0.55 (pig). |
| perineurium-no-level-difference | not_reproduced | Cell 75, reading (a): the human slope CIs do not overlap ([0.025, 0.039] vs [0.049, 0.062]) and the pig intercept CIs do not overlap. Reading (b): human p = 2e-7, pig p = 3e-9. Only the rat part holds (p = 0.87). |
| sunderland-reanalysis | reproduced | Cell 77: n = 777, slope 2.750%, R² = 0.510. |
| rat-perineurium-near-3-percent | reproduced | Cell 79: against the 3% line the fit/reference ratio runs 1.86 to 0.59 and crosses at 80 µm. Against 2.75% it reaches 2.02 at 32 µm, just outside the factor of two. |
| human-pig-perineurium-thicker | reproduced | Cell 81: median ratio human 0.095, pig 0.053; the excess over 3% is larger for small fascicles in both. |
| pig-if-mt-consistent | reproduced | Cell 83: all 10 checks pass. The MT minimum is 23.7 µm against the paper's 5 µm; the check only tests containment (B7). |
| peanut-fascicle-counts | partially_reproduced | Cell 85: the human counts and pig totals match (210 and 179, counted the way the IF code counts). Pig cervical peanut fascicles are 24 against the paper's 25 under both counting methods; the tolerance is 0. |
| no-age-trend | not_reproduced | Cell 87, Pearson reading (a): 3 of 26 tests have p < 0.05, all in pig; chance expectation is 1.3. The rat part shows no trend. The test is the claims file's assumption, and Supplement 6 was not read (B3). |
| rat-carotid-sheath-bundles | blocked (other) | The notebook says only the vagus is traced (cell 89). However, the archive holds the 20x MT micrographs of all 9 cervical samples, and the paper says the whole carotid sheath was sectioned (B6). |

**B. Problems**

1. [affects a conclusion] Cells 15, 16 and 26, `largest_fascicle`: the main analysis uses each rat sample's largest fascicle (the Methods text). The paper's numbers were produced by the code's first-trace rule instead. That rule reproduces the paper's 0.121 ± 0.032 mm exactly, the subdiaphragmatic rat Tukey p values (0.896 and 0.995 against 0.896 and 0.9947), and the species p (0.00154 against 0.0015). The code-rule variant is therefore the paper's actual procedure and should be the primary run for the fascicle-diameter claims. The claims file follows the Methods text and does not notice this; I am reporting that, not correcting it.
2. [affects a conclusion] Cell 44, `satterthwaite_df`, fascicles-larger-cervical:
   - The pig cervical vs subdiaphragmatic contrast gets a Satterthwaite df of 3.74, which is implausible: the more conservative subjects-minus-parameters df (29) gives p = 0.00036, against 0.048 with Satterthwaite.
   - Under the code-rule rat values, the pig Satterthwaite p is 0.0526, so pig fails.
   - Under the largest-fascicle values with subject df, rat fails (p = 0.068).
   - The "reproduced" outcome therefore holds only under some combinations. The rat-only variant's p = 1e-64 is a degenerate fit and should be dropped.
3. [affects a conclusion] Cell 87, no-age-trend: the notebook downloads the paper's supplementary zip for Supplement 4 (`supplement4`) but never opens Supplement 6. Supplement 6 holds the age analysis and would fix the test. As run, the outcome rests on an uncorrected test at p < 0.05 across 26 tests, and the hits (3 of 26 against 1.3 expected) are about chance level.
4. [does not affect a conclusion] Cell 28: the interaction result depends on the estimation choice: unbounded REML gives p = 0.107, the bounded statsmodels fit gives 0.024. The unbounded fit matches the paper's F values closely (599.6/11.05/2.455 against 577.1/11.01/2.445; bounded gives 283.8/21.1/3.71), which supports it as what JMP did.
5. [affects a conclusion] Cells 58 and 59, `lit_table`:
   - The paper's samples are all left cervical, but the comparison also includes right-side literature rows, which the criterion does not ask for. With left-only rows, "human cervical ranges overlap" would become True.
   - The rat cervical row "Fazan and Lachat 1997" with no laterality or n (0.2843 mm, 0.0400 mm²) is a continuation row whose meaning the `supplement4` parser does not establish, yet it counts against the claim.
   - The extra part "fewer fascicles than the posterior study" is from the Results text but is not in the claim statement.
6. [affects a conclusion] Cell 89, rat-carotid-sheath-bundles: the archive (Pennsieve browse of SPARC:60 v5) has `files/derivative/sub-*/sam-3|sam-1/*MT20x.jp2` for all 9 cervical samples, 12–35 MB each. The Discussion says the entire carotid sheath was embedded and sectioned. By the claim's own criterion ("testable only if the dataset holds the cervical micrographs"), the claim is at least partly testable: count the bundles in the sheath and check that the traced one is the largest. Supplementary Figure 16 is presumably in the same Europe PMC zip.
7. [does not affect a conclusion] Cell 83: the min/max checks only test that each value lies inside the widened reported range. Under a per-bound reading the MT minimum fails (23.7 against 5 µm). That 5 µm fascicle is not in `PigVNMorphology_OutputMetrics.mat`, and the notebook does not mention the gap.
8. [does not affect a conclusion] `reml_unbounded` gives multi-df effects the mean of the per-coefficient Satterthwaite df, which is not a standard method. The conclusions are unchanged under the residual-df and subject-df alternatives, which the notebook also prints.
9. [does not affect a conclusion] Cell 75: the fascicles are treated as independent observations, with no clustering by sample. Both readings belong to the claims file, and the human slope gap is large, so the outcome does not change.
10. [does not affect a conclusion] The pig MT values come from the author's output files, not recomputed from the traces (this is stated). Pig IF levels are inferred from list membership, which agrees with the trace-based counts by level (153/131 against 153/132).
11. [does not affect a conclusion] Cell 0 promises a final cell printing every file's SHA-256; that cell is missing. Also, the SPARC:60 readme says the rats were 65–268 days old, but subjects.xlsx and the paper say 75; and "anterior" for the subdiaphragmatic samples comes only from the readme and the code's file lists.
12. [does not affect a conclusion] Helper checks on synthetic inputs, all of which passed:
    - `bwboundaries` and `polyarea` give MATLAB's areas for a square (81), a ring (841/361) and a peanut fascicle (correct grouping).
    - `fit_poly1` matches `polyfit` and the R² from the correlation.
    - `reml_unbounded` and `tukey` match OLS type III F tests on a design with one sample per subject.
    - The rat and human recomputations match the author's code outputs to 0.00 µm (cells 10 and 12).

**C. What I could not check**

- Why the pig Satterthwaite df is 3.7. The per-species variance components and the Hessian of the fascicle model (`fit_fd["H"]`), plus a Kenward–Roger fit (for example lme4/pbkrtest on the exported table FA), would settle this.
- What the Fazan and Lachat no-laterality rows mean. Printing the raw Supplement 4 rows, including their notes column, would settle it.
- The Supplement 6 method and values. An output listing the supplementary zip and Supplement 6's contents would settle it.
- Whether the cervical jp2 micrographs show the carotid-sheath bundles. A downsampled image of each cervical micrograph with the trace overlaid would settle it.
- Where the paper's MT 5 µm minimum and the 25th pig cervical peanut fascicle come from. Per-sample pig IF peanut counts alongside the paper code's own `Nouterperi_peanut` output would settle the second.
