**A. Outcomes**

The claims file has 25 claims. I checked the blocked ones against the archive API: 000489 holds 18 files (Fig1F plus 17 Fig2 dishes), and 000448 holds 18 strobe files covering 9 cells.

| Claim | Outcome | Reason |
|---|---|---|
| fig2a-uptake-rises-with-field | reproduced | Cell 34: under the unpaired test, YP is higher at the strongest-field ROI with p<0.05 for 5/5 amplitudes (p 0.0001 to 0.044), and Spearman ρ ≥ 0.96 for every amplitude. The paired test passes only 3/5, failing for 0% and 25% where n=2 (df=1). The paper's test as written is two-sample. |
| fig2a-vertical-scales | not_reproduced | Cell 36: for 75% the largest mean is 263 a.u. and the largest mean+sem is 339 a.u., both over 250. The unit-free ratio of largest means (unipolar/75%) is 2.47, against 4.8 for the paper's axis limits. This rests on the raw counts being the paper's units, which can't be proven. |
| fig2b-exponential-same-slope | not_reproduced | Cell 38, primary reading (8 kV/cm cutoff, NLS): the exponential beats a straight line for only 3/5 amplitudes, below the required 4, while 0/4 bipolar slopes differ from unipolar. The outcome flips with the reading. At 6 or 7 kV/cm with NLS it is reproduced. With log-linear fits at 6 or 7 kV/cm, 4/4 slopes differ. |
| fig2c-max-inhibition-50-75 | partially_reproduced | Cell 40: the ordering holds at 10/10 fields, and reading (ii) gives p<0.01 at 7/10 fields. The percent is 49.3% (reading a) or 35.1% (reading b), far outside 20±2. If "the test holds" has to hold at every field, the outcome is not_reproduced. |
| fig2c-inhibition-flat-above-8-7 | reproduced (letter of the criterion, main ROI reading only) | Cell 42: under reading (a), 0/4 amplitudes differ. The differences are large, though: +33 points for 50% (p=0.07) and +51 points for 75% (p=0.15). Under the one-sided readings (b+ and b−), 1/4 amplitudes differ. |
| fig2c-weaker-at-6-7 | partially_reproduced | Cell 44: 100% passes on a valid test (per-ROI unpaired, max p=0.0215). 50% reaches p<0.01 only through the pooled unpaired test (p=1.5e-9), which treats 50 ROI values from 5 dishes as independent. Its valid tests give per-ROI max p of 0.08 to 0.10 and a pooled paired p of 0.07. |
| fig3-uptake-linear-in-pulse-number | blocked (data_missing) | Not in 000489 or 000448 (archive listing checked). DANDI:000548, "Effect of the number of pulses…", likely holds it but is outside this attempt. |
| fig3d-cancellation-independent-of-number | blocked (data_missing) | Same as fig3-uptake-linear-in-pulse-number. |
| fig4ac-ns-bipolar-20-25pct | blocked (data_missing) | Not in the two named datasets. DANDI:000549, "Effect of the pulse duration…", is a candidate. |
| fig4d-1200ns-tenfold | blocked (data_missing) | Same as fig4ac-ns-bipolar-20-25pct. |
| fig4eg-us-bipolar-30-50pct | blocked (data_missing) | Same as fig4ac-ns-bipolar-20-25pct. |
| fig4h-us-stronger-at-low-field | blocked (data_missing) | Same as fig4ac-ns-bipolar-20-25pct. |
| fig5-ns-symmetric-along-aa | blocked (data_missing) | Fig. 5 re-analyzes the Fig. 4 dishes, which are not in 000489. The aa' line can't be measured on the Fig. 2 dishes in its place, because the claim is about other pulse durations. |
| fig5-us-anode-stronger | blocked (data_missing) | Same as fig5-ns-symmetric-along-aa. |
| fig6ad-unipolar-833khz-enhanced | blocked (data_missing) | Not in the two named datasets. DANDI:000550, "Pulse repetition rate", is a candidate. |
| fig6be-bipolar-khz-less-than-1hz | blocked (data_missing) | Same as fig6ad-unipolar-833khz-enhanced. |
| fig6cf-833khz-thirtyfold | blocked (data_missing) | Same as fig6ad-unipolar-833khz-enhanced. |
| fig6cf-cancellation-stronger-at-high-field | blocked (data_missing) | Same as fig6ad-unipolar-833khz-enhanced. |
| fig1e-heating | blocked (data_missing) | Neither dataset holds thermometry photographs. Fig1F is a staining image. |
| fig7-unipolar-pole-polarization | reproduced | Cell 13: at 600 ns the cathodic pole is +22.1% (p=0.0012) and the anodic pole −20.7% (p=0.0026), ratio 0.94. This holds under all 4 pole-mask variants. n=5 cells against the paper's 18. |
| fig7-charging-time-constant | not_reproduced | Cell 15: the charging τ of 191 ns is inside tolerance. Everything else is outside: amplitude 23.2% (vs 31±3.1), discharge τ 613 ns (vs 520±52), discharge amplitude 22.7%, and pooled r 0.84 (vs 0.93). Partial credit needs both τ inside tolerance, so it fails. |
| fig7-later-pulses-same-tau-difference | partially_reproduced | Cell 17: discharge τ exceeds charging τ for 4/4 later pulses. No ratio falls in 2.25 to 2.75. Within 10% of the pulse-1 ratio (3.21): 2/4 pulses with the free-start form, 0/4 with the criterion's A(1−exp) form. |
| fig7-bipolar-overshoot | reproduced | Cell 19: (i) bipolar and unipolar don't differ at 600 ns (21.5 vs 22.1%, p=0.86); (ii) the bipolar trace returns sooner (50% decay at 150 vs 475 ns); (iii) the bipolar minimum is −8.1% (p=0.0012). n=4 bipolar cells against the paper's 17. |
| fig7-bipolar-alternation | reproduced | Cell 21: 5/5 pulses have a significant positive end of phase 1 and a significant negative minimum in phase 2. |
| fig7-summation-without-buildup | reproduced (letter of the criterion) | Cell 23: under the unpaired test, later peaks don't differ from the first (p 0.61 to 0.75), and the pre-pulse values stay above zero (p ≤ 0.017). The paired variant does show a build-up: pulses 2 to 4 are 1.7 to 2.2 points higher with p 0.014 to 0.04, at n=5. |

No chance levels apply. The paper states none, and the analysis makes no selection against one.

**B. Problems**

1. [affects a conclusion] Cell 44, fig2c-weaker-at-6-7. The "pooled" reading runs `ttest_ind` on every dish×ROI value from 10 ROI, about 50 values from 5 dishes, as if they were independent. That is pseudo-replication, and it is the only route by which 50% reaches p<0.01. The cell also ORs together the paired and unpaired variants. The opening comment of the claims file says pairing is a method choice to adopt or block, not to OR. Part of this sits in the claims file, which permits pooling dish values: that is a statistical flaw rather than a misreading of the paper.
2. [affects a conclusion] Cells 31, 42 and 44: the low-field percents are not meaningful. The unipolar denominator at low field rests on n=2 dishes near background (19 a.u. at 2.4 mm, 7 a.u. at 3.0 mm). The bipolar groups sit at 30 to 50 a.u. at the same ROI. That gives 198% and 283% "of unipolar" at 6.7 kV/cm, meaning bipolar uptake exceeds unipolar, which is not the paper's "weaker inhibition". A per-group background offset is likely: the 0% and 25% dishes were imaged on 2021-07-29, the 75% and 100% dishes on 2021-08-24. `process_dish` computes footprint-radius variants (`rois_fp01`, `rois_fp03`), and the helper says they are "varied in the notebook", but no cell uses them.
3. [affects a conclusion] Cell 38, fig2b-exponential-same-slope. The outcome changes with the cutoff and the fit method, both open method choices, and the notebook neither adopts one with a reason nor blocks the claim as the claims file requires. The per-dish slope t-test has almost no power because unipolar has n=2 (slopes 0.205 and 0.41). The slopes of the fits to the means for 50% and 75% are 0.72× unipolar (k 0.189±0.016 and 0.191±0.014 against 0.263±0.027).
4. [affects a conclusion] Cell 42, fig2c-inhibition-flat-above-8-7. The ROI-placement reading changes the outcome: 0/4 under (a), 1/4 under (b+) and (b−). The notebook does not decide between them. In the every-pair variant, 19/180 pairs differ (10.6%), about twice the 5% expected by chance. "No difference" here comes from n=3 to 5 dishes, not from small effects.
5. [affects a conclusion] Cell 40, fig2c-max-inhibition-50-75. The notebook prints counts of fields passing (3/10 under reading i, 7/10 under reading ii) but never applies the criterion's "test holds". Whether that must hold at every field decides between partially_reproduced and not_reproduced.
6. [affects a conclusion] Cells 26 and 31: one YP image is deposited under two dishes, Fig2_0_03 (unipolar) and Fig2_25_04 (25%). Leaving both out is sensible, but it leaves the unipolar reference that every Fig. 2C percent divides by at n=2, below the paper's n=3 to 8. Separately, the 100% bipolar means exceed unipolar at most fields (93 to 139%). That conflicts with the paper's description of 100% as inhibitory. It is not a code error, but it bears on every percent claim and the notebook doesn't mention it.
7. [affects a conclusion] Cell 36, fig2a-vertical-scales. The verdict depends on the image counts being the paper's units, which the notebook assumes and says it cannot verify. The ratio check (2.47 against 4.8) points the same way, but axis limits only bound the data.
8. [does not affect a conclusion] Cell 15, `fit_pulse`. The charging window is frames 0 to 23 (0 to 575 ns), where the criterion says 0 to 600 ns. Onset is defined as the first frame above threshold, so t=0 is late by up to a frame. On synthetic data, a half-frame offset biases τ by −12%. The ±1-frame variant moves charging τ from 149 to 250 ns, so "in tolerance" isn't robust. The verdict doesn't change because discharge τ and the amplitudes fail anyway.
9. [does not affect a conclusion] Cell 17: the free-start charging form is the author's addition, not in the criterion. Both forms give partially_reproduced. The pulse-5 ratio of 2.887 sits just under the 10% bound of 2.889.
10. [does not affect a conclusion] Cells 19 and 21: the time of the minimum is chosen on the mean trace and then tested on the same cells. The effects are large (p ≤ 0.0013).
11. [does not affect the letter of the outcome] Cell 23: as the claims file prescribes, pulses within the same cells are compared with an unpaired test. With n=5, the claim of absence is weak, and the paired variant contradicts it.
12. [does not affect a conclusion] Cell 10: cathode = upper pole is inferred from FluoVolt's sign (it brightens on depolarization), not from metadata. That is reasonable and consistent across all 9 cells.
13. [does not affect a conclusion] Fig. 7 has n=5 unipolar and n=4 bipolar cells against the paper's 18 and 17, so 120 pooled points against 425. The deposit is a subset, and the notebook states this.
14. [does not affect a conclusion] Cell 0: the Fig. 3 to 6 claims are blocked because the claims file assigns them to 000489. The API shows that 000548, 000549 and 000550 exist with titles matching Figs. 3, 4 and 6. This is a scoping issue in the claims file, not a notebook error.
15. Checked and found correct:
    - `field_kv_cm`: 15.38 kV/cm at the centre, and integrating it between the electrodes gives exactly 5.75 kV.
    - `square_mean`, `align_lag`, `shift`, `charge_fit` and `discharge_fit` behave correctly on synthetic inputs.
    - The 0.65 µm pixel size is confirmed by the measured 4.51 mm electrode centre spacing.
    - The footprint overlays in cell 28 sit on the electrode footprints.
    - The 15.1/15.38 field scaling doesn't change which ROI is nearest to each named field.
    - There is no train/test split, so leakage doesn't apply.

**C. What I could not check, and what output would have let me**

- Per-dish ROI values and per-dish YP0/MB0. Printing them would show the background offset between imaging dates.
- The `rois_fp01` and `rois_fp03` results. Rerunning cells 40, 42 and 44 on them would test whether the low-field percents depend on the footprint disc.
- Fig. 2B under each cutoff and fit method. A table with a stated adopted reading and a semi-log plot of the fits would settle problem 3.
- Fig. 7 fit residuals and the overlay of the fits on the traces.
- The masks figure in cell 7. I did not look at it.
- Whether 000548, 000549 and 000550 hold the Fig. 3 to 6 data. Only their titles and asset counts were checked.
