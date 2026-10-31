**Verifier report, round 2: Chartrand et al. 2023 (doi:10.1126/science.adf0805) on DANDI:000630 0.230915.2257**

Counts come from the files. The claims file has 41 claims, and the attempt record has 41 outcomes, one per claim. Notebooks: R = `reproduce_chartrand_2023.ipynb`, M = `mouse_comparison.ipynb`, Mo = `morphology_tables.ipynb`. `docs/protocol.md` is not among my materials, so I worked from the task statement.

### 1. Outcomes and assumptions

No outcome carries `assumed: true`. Several outcomes still rest on choices the attempt made itself. Each is stated in prose but none is flagged:
- **The 50% rule.** This affects every human and mouse electrophysiology claim. It is stated and reasonable for choosing between features. But it goes beyond O1 in one respect: O1 says to fall back to the paper's values (reading b) only where a feature "cannot be computed". The adaptation ratios can be computed, yet reading (a) uses the paper's ratios.
- **Random-forest and cross-validation seeds** (fig6a, figs8a). Reasonable.
- **The attempt's own thresholds** for fig2d, fig4b-mc4r-axon and fig5b-tnfaip8l3-dendrites, where the claims file gives no criterion. Reasonable, taken from the legends.

I agree with these outcomes as recorded:
- dandiset-cell-link, mouse-cell-link
- patchseq-counts, fig2b (amended criterion), figs3a, figs6, figs6c
- fig4b-mc4r-sag-irregularity, fig4b-adarb2, fig5b-tnfaip8l3-ephys
- fig6d, figs8a, figs8b
- fig3d (VISp, both O2 readings partial), fig3e, fig3f, fig3g, fig4d, fig5d
- the three morphology partials, figs6a, fig3b, and the 13 not-attempted blocks.

I agree with these, with caveats:
- **fig2c-subclass-ephys-differences (partial).** Reading (a) is what decides partial over reproduced, and its hero sweep looks wrong in some cells (point 3 below). Leaving out one donor also raises first_isi_inv_hero's uncorrected p to 3.5e-5 (R c26), which the record does not mention.
- **fig1e (blocked, metadata_insufficient).** The reason fits R/M output (M c21: the public mouse table has no deeper t-types). I did not check whether any other public mouse patch-seq metadata gives t-types for the deeper cells.

I disagree with two:
- **fig2c-lamp5-gradient: partially_reproduced → not_reproduced.**
- **fig6a-ephys-dprime-subclass-structure: partially_reproduced → not_reproduced.**

Neither criterion names a partial level. The record changed fig4b-adarb2, fig4d and fig5d to not_reproduced on exactly that ground ("the criterion names no partial level"), so these two should follow the same rule. I gave both as partial in round 1, so this is my inconsistency as well. In fig2c-lamp5, sag misses 0.001 under every reading. In fig6a, the second reading of "high" fails.

Possible claims-file misreadings, reported and not corrected:
- **fig5d.** The criterion requires Lamp5 Krt73's initial firing rate to exceed every other mouse subclass, L1 VIP included. The paper says only that these cells "tended to fire in doublets at stimulus onset". This is the same comparison that a reader removed from fig2b part (iii). The outcome fails only on that comparison: 97.7 Hz against L1 VIP's 171 Hz (M c18).
- **figs3a direction.** Still open; it is with a reader and cannot change the outcome.

### 2. Sentences the printed outputs do not support

- **"62 Amsterdam and Szeged cells"** (R c20, R c65, dandiset-cell-link notes, data_missing finding). R c19 prints a strict set of `{'AIBS': 222, 'Gabor': 28, 'Huib': 22}`. That is 50 Amsterdam and Szeged cells. The other 12 of the 62 are Seattle cells that failed feature extraction. The "136 in the paper's table" in the finding is not printed anywhere.
- **"agree … within 1% for 71 to 98% of cells in 39 of the 44 features computed; the five adaptation ratios agree less (4 to 53%)"** (R c18; also R c65, the record notes, and every deviation block's "4 to 53%").
  - peak_v_adapt_ratio (0.534) is one of the 39 features used in reading (a) (R c15, R c16).
  - So the 39 range from 53% to 98%, and the five excluded ratios agree for 4% to 37%.
- **"(Spearman 0.92 to 1.00)"** (dandiset-cell-link notes). R c15 gives 0.886 to 0.997 for the 39 features, for example median_isi_hero 0.886.
- **"so the difference between the readings comes from sweep choice"** (R c27, fig2c notes, verification response). In R c17, only 16 of 31 cells are explained by sweep choice (10 another repeat, 6 another amplitude). 13 have "no sweep here gives the paper's value". The fig2c breakdown of the 28 cells is not printed, so "mostly" is unsupported there.
- **figs3a: "R2 = 0.334 … on the features computed here" and "With the order first over third R2 is 0.149"** (R c33, R c34, record).
  - In reading (a) the ratio is the paper's value. upstroke_adapt_ratio is not in COMPUTED (R c16), and the (a) and (b) ratio ranges are identical in R c33.
  - So 0.334 is computed sag against the paper's ratio. The 0.149 row uses the computed ratio, so it compares data sources as well as order.
  - The deviation "the adaptation ratio is computed here … so the outcome is also shown on the paper's values" has it backwards. Regression on the computed third-over-first ratio is never shown. The outcome is unaffected.
- **fig6d: "On the paper's values the four combinations give LAMP5 0.785 to 0.806 … all others 0.490 to 0.526"** (record). Those ranges cover both feature readings. On the paper's values alone (R c57) the figures are LAMP5 0.802–0.806, MC4R 0.693–0.712, PAX6 0.892–0.896, all others 0.495–0.506. R c58 states this correctly.
- **figs6a: "20 of the 78 reconstructed cells"** (Mo c14, record, finding). Mo c13 counts 51 missing plus 20 known, which is 71 cells.
- **Mo c2: "Of the 71 cells with morphology in the strict L1 set".** Mo c1 prints 78.
- **R c0: "The files hold the current clamp recordings only".** R c5 and M c21 show nucleated-patch voltage-clamp sweeps in 38 files.
- **README run times.** The README says "about 11 minutes, of which about 2 are streaming the files and 6 the Gaussian mixture search", and "about 4 minutes" for the mouse notebook. Printed: 21.2 min total (R c66), 240 s streaming (R c1), 772 s for the GMM (R c57), and 7.3 min for the mouse notebook (M c24).
- **README table.** It has no row for fig3e, fig3f or fig6b. "Transcriptomic, cytoarchitecture and other morphology claims" does not describe them.
- **Deviation blocks of fig3d, fig3g, fig4d and fig5d say "(39 features)".** M c6 uses 38 for both species.
- **figs8b: "session_id PLACEHOLDER".** This value is not printed. R c63 shows only "0 files with a numeric session id".

Everything else in the Result cells, the Summary sections and the record notes matches the printed numbers.

Do the round-1 reasons appear in my own words? Mostly, as faithful abridgements. Two exceptions:
- The 12 not-attempted `elsewhere` claims carry "their inputs are public (B10)". I said that only for fig6b and fig3d-morphology. For the 13 not-attempted claims, my reason was that they were not data_missing (and that fig1e was testable).
- fig2b's entry reads `agrees: true` / "No change needed", while its outcome notes say the first run recorded not_reproduced. One of the two is inaccurate about the round-1 state.

### 3. Round-1 points

Resolved:
- B1: the direction is stated and put to a reader.
- B3: both layer rules are run, and each is traced to a code cell.
- B4: VISp is used, and the fig3d outcome is corrected.
- B5: all 272 mouse cells are run, and the fourth Krt73 cell is identified.
- B6, B7, B8, B11.
- B10: fig3f's mouse sweeps are counted, the fig1e reason is changed, and the inputs are noted as public.
- From section C: the age donor, the 22 missing mouse ids, the figs8b cross-check against 000228 and 000337, and the TEa files.

B2 is partly resolved. The rule is stated and the cells are listed, but the listing raises a new problem (point 3 below).

What remains that bears on a conclusion:
1. **fig2c-lamp5-gradient and fig6a should be not_reproduced** under the rule the record applies to fig4b-adarb2, fig4d and fig5d.
2. **fig5d** rests on a criterion that may misread the paper (the L1 VIP comparison). It should go to a reader, as fig2b did.
3. **Hero-sweep selection, affecting fig2c.**
   - In R c17, the computed "rheobase + 40 pA" sweep is at the rheobase itself or only 10 pA above it in 6 of the 31 listed cells: 653864596, 653907140, 672646211, 712885453, 811804107 and 868243321.
   - The helper's own docstring describes the hero sweep as 39 to 61 pA above rheobase.
   - Either `stim_amp_hero` is mis-indexed (`amps[row.name]` in `l1ephys.py:421`) or the wrong sweep is used.
   - Reading (a) of first_isi_inv_hero decides fig2c between partial (4.7e-7) and reproduced (1.7e-8 on the paper's values). This should be checked before the partial outcome stands.
4. **Adaptation ratios in reading (a).** Reading (a) never uses the computed ratios, although O1 treats them as computable. That is a deviation from the claims file, and the effect is unshown for fig3g and fig6d, where upstroke_adapt_ratio is among the best features. With Spearman 0.92 against the paper's values, an outcome change is unlikely.
