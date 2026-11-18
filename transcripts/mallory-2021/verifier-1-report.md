# Verifier report, round 1: Mallory, Hardcastle et al. 2021 on DANDI:000053

The claims file holds 47 claims. The notebooks test 20 of them and treat 27 as blocked. Of the 20 tested, I find 10 reproduced, 6 partially reproduced and 4 not reproduced. The 27 blocked claims are 21 freely moving LN-model claims and 6 head-fixed claims.

## A. Outcomes

| claim | my outcome | reason |
|---|---|---|
| headfixed-session-link | reproduced | Each of the 11 figshare sessions has exactly one candidate file, holding 2861 cells in total, and B, Bs, Eh, Ev and unit 0 all equal (cell 11). In 2 files unit 0 differs as stored because its spike index wrapped at 2^16 (index 5852 becomes 71388, a shift of exactly 65536). After the repair it is identical; `split_units` handles a synthetic wrap correctly. |
| fig1b-head-posture-distributions | reproduced | 8 of 8 values are within tolerance, and even the across-mouse sem values match the legend (4.18, 4.50, 7.61, 3.60, 34.7) (freely moving notebook, cell 11). |
| fig4f-eye-movement-distributions | reproduced | 8 of 8 within tolerance, centred or not (cell 17). |
| fig4j-eye-encoding-cells | reproduced | Under readings (1a, 2a): 718 eye cells, with 341, 243, 238 and 137 per variable, all within tolerance (cell 21). Under (1b) only 614 eye cells and 1 of 4 per-variable counts are within tolerance (folds notebook, cell 5), so the result depends on how folds are built. |
| fig4k-eye-conjunctive | reproduced | 0.955, 0.272 and 0.242, all within tolerance (cell 23). |
| fig5a-eh-nasal-temporal-similar | partially_reproduced | Overall 158 of 341 nasal, P = 0.19, under every reading (cell 28). The two hemisphere tests cannot be run: I checked the archive and no asset records hemisphere. |
| fig5b-ev-up-down-similar | reproduced | 172 cells classified (tolerance 177 ± 17.7); upward P = 0.82 or 0.49 (cell 30). |
| fig5-eye-position-stability | partially_reproduced | Eh is more stable than B (P = 7.7e-30). Ev vs B gives P = 0.0168 against alpha 0.0167, so not significant, by a hair. The Ev median is 0.603, outside 0.72 ± 0.072 (cell 32). |
| fig5av-eh-linear-most-stable | reproduced | Kruskal-Wallis P = 4.2e-10. Linear beats quadratic (P = 0.0015) and higher orders (P = 4.5e-10). All three medians are within tolerance (cell 34). |
| fig5bv-ev-low-order-more-stable | partially_reproduced | The tests hold: KW P = 8.2e-5; linear and quadratic each beat higher orders (P = 1e-4 and 4e-4). Only 1 of 3 medians is in tolerance (0.83, 0.73, 0.11), against the two required (cell 36). The criterion has no partial clause; I call it partial because the statement holds and only the medians fail. |
| fig6-eye-velocity-linear-nasal | partially_reproduced | The tests hold: nasal 36 of 56, P = 0.044; vertical P = 0.41. The linear counts, 56 and 36, are outside 43 ± 4.3 and 29 ± 2.9 (cell 38). |
| fig6-eye-velocity-nonlinear-temporal | not_reproduced | In every one of the 8 reading combinations the horizontal test fails (P ≥ 0.73), and at most 2 of the 4 counts are within tolerance (cell 40). |
| fig6-eye-velocity-stability | not_reproduced | Eh dot is above Bs as claimed (P = 3e-47). Ev dot vs Bs gives P = 0.036, not significant at 0.0167, and the direction is reversed: Ev dot 0.82 is above Bs 0.77 (cell 42). |
| fig6v-asymmetric-more-stable | partially_reproduced | Under rule (6a) the vertical part holds: KW P = 1.5e-4; nonlinear-asymmetric 0.95 beats symmetric 0.61, P = 0.0011. The horizontal part fails under both rules (KW P = 0.084 or 0.41) (cell 44). |
| fig7ab-eye-contributions | reproduced | Under reading (c), 12 of 12 ordered tests hold and 4 of 6 medians are within tolerance, though two of those are at the edge (Bs 0.283 against a limit of 0.286; Eh dot 0.053 against 0.055). Under (a) the tests hold but only 2 of 6 medians do (cell 46). |
| fig7c-head-fixed-model-fit | reproduced | 2140 cells (tolerance 2191 ± 219). Median 0.0513 [0.0215–0.1128] in the units compute_llh.m produces, against the paper's 0.05 [0.02–0.11]. Converted to true bits per spike it would be 0.107 (cell 25). |
| fig7e-eye-no-clustering | not_reproduced | 3 of 30 combinations reach P < 0.005 at some k: Eh–Eh dot, Ev dot–Bs and Ev dot–Eh dot, with P = 0.000 at several k (cell 48). |
| supp4-eye-ln-conservative | not_reproduced | Both shuffle methods find more cells than the LN model, but within-cell shuffling recovers only 0.72, 0.61, 0.79 and 0.78 of the LN cells, against the 0.9 required (cell 52). |
| supp5-eye-model-raw-tuning-agree | reproduced | 4 of 4 medians within tolerance (cell 54). |
| supp7e-eye-velocity-extrema-near-zero | partially_reproduced | Horizontal: 145 of 192 within half range, P = 8e-13, the same proportion as the paper (0.76); median ≠ 0. But the count 145 is outside 170 ± 17. Vertical: 72 of 125, P = 0.11, which fails the test, and the count is outside tolerance (cell 50). |
| 21 freely moving LN claims: fig1c ×4, fig1d, fig2 ×8, fig3ab, fig3c, fig3e, supp3-head, supp4-head, supp5-head, supp9-head | blocked (other: compute not completed) | The data are in hand: Dataset 1 is loaded and Dataset 2 is readable (freely moving notebook, cells 3 and 9). The block is run time only, so all of these are testable. |
| fig8c-eye-tuning-without-landmarks, fig8e-joint-cells-preserve-eye-tuning | blocked (data_missing), not demonstrated | The notebook never inspects the 9 unused ecephys files; see problem 2. |
| methods-hemispheres-similar | blocked (metadata_insufficient) | Confirmed: electrode location is "unknown", and the asset metadata I queried from the API has no hemisphere field. |
| supp3-eye, supp9-eye, supp12 | blocked (too_large / time) | The data are present; only compute is missing. supp9-eye needs just the predictions of the reduced models that the main pass already fits. |

## B. Problems

1. **[affects a conclusion]** Freely moving notebook, status table: 21 claims are blocked because "the LN model under the four readings did not finish within 60 min". Cohort 1 is only 179 cells. One reading could have been run alone, as the head-fixed notebook does for 2861 cells in about 25 min. These claims are testable, not blocked.
2. **[affects a conclusion]** Cells 0, 7 and 12: "the other 9 are gain and contrast sessions" is asserted but never shown, since trial tables are printed only for the 11 paper sessions. Among the 9 unused files, one per mouse, exactly one 6-mouse subset sums to 1621 units, the Fig. 8 count:
   - npI3 0421
   - npI4 0421 obj-1yyd867
   - npJ2 0512
   - npJ3 0506
   - npJ4 0512
   - npJ5 0505 obj-1ti12l8

   Two of these are second spans of the same probe insertions as paper sessions. The landmark and no-landmark blocks may therefore be in the dandiset, and fig8c and fig8e may be testable.
3. **[affects a conclusion]** Open detail (2b), clipping, was never run. Reading (1b) was run only for the counts. The 9 claims that came out partial or not reproduced (fig5 stability, fig5bv, fig6 ×4, fig7e, supp4-eye, supp7e) rest on readings (1a, 2a) alone. Fig4j shows the fold reading moves the counts by about 100 cells.
4. **[affects a conclusion]** `curve_features`, preference reading (b): it compares slope_pos with −slope_neg, a "steeper rise away from 0". The claims file says "the larger absolute slope". The literal reading was never run. It could change fig6-nonlinear-temporal from not reproduced to partially reproduced (its tests), and fig5a and fig5b too.
5. **[does not affect a conclusion]** Cell 52 (supp4-eye) leaves out the below-0 / above-0 symmetric shuffle test (5th and 95th percentiles) that both the Methods and the criterion specify for Eh dot and Ev dot. That undercounts the velocity cells. The outcome stands anyway, because Eh (0.72) and Ev (0.61) already fail the 90% bar.
6. **[affects a conclusion]** supp3-eye, supp9-eye and supp12 are blocked for time, not for any data reason.
7. **[does not affect a conclusion]** The claims file's fig7c criterion equates "bits per spike" with compute_llh.m, which the helper reports as multiplying by log 2. That equation is the claims file's misreading. The reproduction holds only for the code's quantity (true bits give 0.107), though the matching interquartile range supports that this is the quantity the paper used.
8. **[does not affect a conclusion]** Several results sit at the edge of their thresholds: Ev vs B P = 0.0168 against 0.0167 (cell 32), and the fig7ab reading (c) medians (cell 46). Reading (c) also uses fold 1 only, a single section.
9. **[does not affect a conclusion]** `fold_labels` is applied to the kept bins after about 10% are dropped. A "10-s section" is therefore 500 kept bins, which joins non-adjacent times.
10. **[does not affect a conclusion]** Cell 42 uses all 137 Ev dot cells where the paper uses 131, presumably the classified ones. The reversed direction would not change.
11. **[does not affect a conclusion]** Whole sessions are used, including gain 0.5 and contrast-10 trials (cell 13). This is stated, and it is consistent with the deposit's frame counts.
12. **[does not affect a conclusion]** Cell 28: the nasal fraction varies by mouse from 0.25 to 0.72, which bears directly on the hemisphere sub-tests that cannot be run.

## C. What I could not check, and what would settle it

- **The fig8 block:** the trial-table columns and values (and any track or landmark field) of the 9 unused ecephys files. I did not read file contents, to stay within the no-download rule.
- **Hemisphere:** whether figshare Dataset 3's `cell_info` has a hemisphere field. Printing its field names would settle it.
- **Code conventions:** whether compute_llh.m really multiplies by log 2, and whether forward_search_kfold.m really uses −5 as the first-step baseline. I had no GitHub access, so a quoted code excerpt in the notebook would settle both.
- **Freely moving timing:** the attempt record is not available to me. A one-reading Cohort 1 run, or its timing, would show whether those claims were really out of reach.
- **Chance levels:** the paper's false-detection rates (Supp. Fig. 3c, e.g. 5 of 343 for Eh, 13 of 135 for Ev dot) have no counterpart in the notebook, because supp3-eye was not run.
- **Missing outputs that would settle open points:**
  - the downstream claims under (1b) and (2b);
  - preference reading (5b) as written in the claims file;
  - supp4 with the symmetric velocity test included;
  - fig6 stability on the 134 classified Ev dot cells.
