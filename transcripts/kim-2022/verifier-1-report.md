# Verifier report, round 1: Kim et al. 2022 on DANDI:000489 (version 0.230518.1811)

The claims file has 22 claims. The notebook tests 6 (all on Fig. 2) and blocks 16 as data_missing. I had no attempt record, so these counts come from the claims file and the notebook only.

## A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| fig2a-uptake-rises-with-field | partially_reproduced | YP is higher at the strongest field with p < 0.05 for 50%, 75% and 100% under both the paired and the unpaired test, but not for 0% (n = 2, p = 0.17/0.11) or 25% (p = 0.19/0.15) (cell 15). That is 3 of 5. Spearman rho is 0.98 to 0.99 for every amplitude. Under the one-side reading (b), the bottom side gives 2 paired against 3 unpaired, so this outcome depends on the ROI reading. |
| fig2a-vertical-scales | not_reproduced | Largest mean + s.e.m. for 75% is 283.2 a.u., above the 250 limit. Unipolar is 785.4 (limit 1200) with a largest mean of 571.1 (> 250). All variants fail on 75% (255 to 343) (cell 17). Treating camera counts as the paper's a.u. is an assumption the files cannot confirm, but it is reasonable. |
| fig2b-exponential-same-slope | not_reproduced | 10 of 12 readings have a bipolar slope that differs from unipolar at p < 0.05. Slopes for 50% and 75% are 0.68 to 0.72 of unipolar (NLS) or 0.50 to 0.59 (log). The other 2 readings have the exponential beating a straight line for only 3 of 5 amplitudes, so the criterion's "reproduced" fails there too (cell 19). The notebook's methods_underspecified comes from a category it added (problem 3). |
| fig2c-max-inhibition-50-75 | not_reproduced | The percent for 50% is 54.5% as the mean over 8.7 to 15.1 kV/cm and 31.6% at its lowest, both outside 18 to 22%. The p < 0.01 test fails under both readings the notebook ran (cell 21). The ordering does hold. A test-location reading that was not run could raise this to partially_reproduced (problem 4); the ~20% value fails under every reading. |
| fig2c-inhibition-flat-above-8-7 | not_reproduced | At 8.94 kV/cm against 15.24 kV/cm: 50% is 113% vs 35% (paired p = 0.012, unpaired p = 0.0016), and 75% is 156% vs 42% (p = 0.049 / 0.018). Both tests are significant, in every variant (cell 23). |
| fig2c-weaker-at-6-7 | blocked (other) | The unipolar mean at 6.75 kV/cm is −8.6 a.u. (dishes at 11 and −28), so the percent of unipolar is −399% (50%) and −579% (100%). That is a ratio to background, not a measure of inhibition (cell 25). The outcome flips to reproduced on the bottom side and with the left footprint alone, where this denominator changes. |
| fig3-uptake-linear-in-pulse-number | blocked (data_missing) in 000489 | Confirmed: 000489 holds 18 files, the Fig1F sample plus 17 Fig. 2 dishes. The data are in DANDI:000548, which cites this paper; one exception is that 000548 has only 1 dish of 10-pulse bipolar. |
| fig3d-cancellation-independent-of-number | blocked (data_missing) in 000489 | Same as fig3: the data are in 000548. |
| fig4ac-ns-bipolar-20-25pct | blocked (data_missing) in 000489 | DANDI:000549 holds Fig. 4/5 dishes for 300 ns, 1200 ns, 50 µs, 100 µs and 500 µs. It has no 600 ns files; the Fig. 2 0% and 50% dishes may be the paper's 600 ns pair. |
| fig4d-1200ns-tenfold | blocked (data_missing) in 000489 | In 000549: 2 unipolar and 3 bipolar 1200 ns files. |
| fig4eg-us-bipolar-30-50pct | blocked (data_missing) in 000489 | In 000549, with 2 or 3 dishes per arm. Uni50us-03 appears as two files of identical size. |
| fig4h-us-stronger-at-low-field | blocked (data_missing) in 000489 | In 000549. |
| fig5-ns-symmetric-along-aa | blocked (data_missing) in 000489 | The aa' line is in the same 000549 images. Which electrode was the anode is not checked in the metadata. |
| fig5-us-anode-stronger | blocked (data_missing) in 000489 | Same as fig5-ns. |
| fig6ad-unipolar-833khz-enhanced | blocked (data_missing) in 000489 | DANDI:000550 holds 10 kHz, 100 kHz and 833 kHz files. I found no 500 kHz file. 1 Hz would come from the Fig. 2 dishes. |
| fig6be-bipolar-khz-less-than-1hz | blocked (data_missing) in 000489 | In 000550 (except 500 kHz). |
| fig6cf-833khz-thirtyfold | blocked (data_missing) in 000489 | In 000550: 833 kHz with 2 unipolar and 3 bipolar dishes. |
| fig6cf-cancellation-stronger-at-high-field | blocked (data_missing) in 000489 | In 000550. |
| fig7-charging-time-constant | blocked (data_missing) in 000489 | DANDI:000448 cites this paper and holds 9 CHO cells × 2 trials (F/R) of 600 ns, 833 kHz strobe imaging (unipolar in the asset I checked). The paper used 18 unipolar and 17 bipolar cells, so the data are partial. |
| fig7-bipolar-overshoot | blocked (data_missing) in 000489 | In 000448 there may be no bipolar cells; I did not check every asset. |
| fig7-summation-without-buildup | blocked (data_missing) in 000489 | In 000448, partially. |
| fig1e-heating | blocked (data_missing) | No dandiset with thermochromic photographs found in an archive search. |

## B. Problems

1. **[affects a conclusion]** Blocked claims (cell 0 table, cell 12). The notebook calls Figs. 3 to 7 "data missing" without noting four sibling dandisets. 000548 (Fig. 3), 000549 (Figs. 4/5), 000550 (Fig. 6) and 000448 (Fig. 7) each list `IsPublishedIn` doi:10.1016/j.bioelechem.2022.108319. Fifteen claims are blocked only for 000489, not for the archive.
2. **[affects a conclusion]** `sub-Fig2-0-03` exclusion (cells 6 and 7). The exclusion is well supported: its YP overview is identical to 25-04's, its own MB/YP phase correlation is 0.028 against a baseline of 0.018, and MB of 25-04 against this YP is 0.454. It leaves unipolar at n = 2, below the paper's 3 to 8, and the unipolar arm is the denominator of every Fig. 2C claim and one of the failing fig2a amplitudes. In 000548, the 5-pulse files Uni5-06, Uni5-07 and Bi5-xx are exactly 2640 bytes larger than the matching 000489 files, which suggests the same images. Uni5-03 is 1,037,476,805 bytes against 1,021,672,026 for 000489's 0-03, so it may hold the real 0-03 YP image. The notebook did not look. Separately, the "with sub-Fig2-0-03" variant counts a 25% image as unipolar and is not a valid reading.
3. **[affects a conclusion]** `claim_fig2b` (cell 19). It labels "no slope differs, exponential not adequate" as partially_reproduced, a category the criterion does not define. That label is the only source of the disagreement between readings that yields methods_underspecified. Read against the criterion, all 12 readings fail.
4. **[affects a conclusion]** `claim_fig2c_max` (cell 21). Where the p < 0.01 test is made comes from the notebook: either p < 0.01 at all 9 ROI, or on the pooled dish means. It did not run a test at the named fields (8.7, 15.1 kV/cm) or at any single ROI. 50% against unipolar reaches p < 0.01 at 1 of 9 ROI, and the notebook does not print which. With the ordering true, that reading would give partially_reproduced.
5. **[affects a conclusion]** `claim_fig2c_67` and `ratio_table` (cells 13 and 25). The code divides by a unipolar mean that is at or below background at 6.75 kV/cm and never flags it. Whether the test passes depends on the sign of a near-zero denominator.
6. **[affects a conclusion]** `run_variants` (cell 12 onward). The claims file names ROI placement reading (b), one side only, as a reading. The notebook runs it only as a variant, and each `outcome` uses the both-sides table alone. Reading (b) changes the outcome for fig2a (bottom side gives methods_underspecified) and fig2c-weaker (bottom side gives reproduced, top side not_reproduced). The notebook gives no rule for combining top and bottom.
7. **[does not affect a conclusion]** `nearest_j` (cells 21 and 23). It maps 15.1 kV/cm to j = 1 (15.24) and excludes the centre ROI j = 0 (15.38), although the paper's 15.1 is its strongest, central field. The model is 1.9% high. At j = 0 the 50% value is 38.7%, which changes no outcome.
8. **[does not affect a conclusion]** `field_kv_cm` and `roi_mean_field`. I checked these on synthetic inputs. The integral of E across the electrode gap is 5.75 kV, the centre field is 15.38 kV/cm, and the ROI mean is invariant to the axis angle. The 4.5 mm centre distance is backed by the measured 4.54 mm median (cell 8). `roi_table` side selection and `yp_index` behave correctly on synthetic inputs. `find_footprints` recovers two synthetic discs to within 1 px, and the cell 5 overlay shows the footprints and bb' lines placed correctly on all 17 dishes.
9. **[does not affect a conclusion]** `N_ROI_SIDE = 15`. The 3 mm extent (weakest ROI at 5.13 kV/cm) is the author's choice, not stated as an assumption. Distal ROI are at background, so fig2a is unlikely to change.
10. **[does not affect a conclusion]** Cell 10. The YP index goes negative distally (0%-07 down to −77), so footprint background does not match distal background. The log-fit readings drop these points, and the counts are printed.
11. **[does not affect a conclusion]** Data features the notebook reports without testing. Dates confound amplitude: all unipolar dishes are from 2021-07-29 and all 75% and 100% dishes from 2021-08-24. 100% bipolar exceeds unipolar (133% at 15.24 kV/cm). Dish 25-04 is nearly flat (about 75 a.u. at every field).

## C. What I could not check

- **Fig. 2C location of significance:** which ROI gave p < 0.01 for 50% against unipolar in fig2c-max. A per-ROI p-value table would settle problem 4.
- **One-side unipolar values:** the per-dish table and the unipolar mean per ROI for the top-side, bottom-side and single-footprint variants, especially at j = 12. Only the outcome rows are printed, so I cannot see why fig2c-weaker flips.
- **Missing unipolar dish:** whether 000548 `sub-Fig3-Uni5-03` holds the true 0-03 YP image. A phase correlation of its MB and YP channels against 000489's 0-03 would settle it.
- **Fig. 7 cell types:** the pulse shape of every 000448 asset. I read the session metadata of one asset only.
- **Image units:** whether the stitched images were rescaled on export. Nothing in the files states it, which is what fig2a-vertical-scales rests on.
