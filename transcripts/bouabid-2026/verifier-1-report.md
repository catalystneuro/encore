**Verifier report, round 1: Bouabid, Vu et al. 2026 on DANDI 001692 (0.260303.1724)**

The claims file has 33 claims. My outcomes: 21 reproduced, 8 partially reproduced, 3 not reproduced, 1 blocked. The full-text HTML of the preprint (CC-BY) and an extracted text version are saved under `paper/`. I also read the Zenodo Figure 8 source data and queried the DANDI asset list. I did not stream any NWB files.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| fig1e-dominant-polarity | reproduced | Cell 18: 133 negative / 128 DA-leading / 41 positive / 32 ACh-leading. All four are within tolerance. |
| fig1f-adls-hotspot | partially_reproduced | Cell 21: the hotspot mean is negative (-0.368). Its centroid is anterior (0.63 vs 0.10) and dorsal, but not lateral (ML 2.02 vs median 2.04), so it fails the criterion's "lateral" test by 0.02 mm. A hotspot is always found by this procedure (B1), so finding one carries no evidence on its own. |
| fig1h-in-vs-out | reproduced | Cell 24: p = 1.8e-13, inside median -0.41 vs outside -0.14 (paper 1.67e-16). The test is circular, as the criterion notes. |
| fig1f-positive-posterior | reproduced | Cell 26: positive-r sites have median AP -0.40 vs 0.24, one-sided p = 4.3e-7. |
| ed2-hotspot-per-mouse | reproduced | Cell 28: all 5 mice have the inside median lower; 4 of 5 reach p < 0.05 (UG29 p = 0.079 with n_in = 2). |
| ed1-controls-no-organization | not_reproduced | Cell 30: a positive hotspot is found (mean 0.329). The control correlations are also not weak: median abs(r) is 0.238 vs 0.240 for the sensor mice, and 68% are positive. The hotspot result itself is uninformative (B1); the "weak" part fails on the descriptive numbers. |
| fig2a-directionality | reproduced | Cell 32: median indices -0.27, -0.30, +0.33, +0.12, all with Wilcoxon p < 1e-24. The signs hold in every mouse. |
| fig2-magnitude-correlations | partially_reproduced | Cell 34: counts 115, 70, 90, 76; 70 is outside 81 ± 8.1. No site is significant in the opposite direction. |
| fig2d-magnitude-in-out | partially_reproduced | Cell 36: ACh trough / DA peak is more negative inside (p = 1e-4). ACh peak / DA trough is not (p = 0.12). Neither same-sign type differs. |
| fig2b-pairing-overlaps-hotspot | reproduced | Cell 38: overlap p = 0.015, 0.020, 0.005, 0.000, all below 0.05 (the paper reports < 0.01). This uses raw occurrence with no chance correction (B3). |
| ed3e-transient-rates-in-hotspot | reproduced | Cell 40: all four rates are higher inside, p ≤ 0.003. |
| fig3b-reward-correlation | partially_reproduced | Cell 42: 122 negative, 52 positive (tolerance floor 52.2), mean latencies 172.1 and -59.8 ms. Three of four values are within tolerance. |
| fig3d-reward-in-out | reproduced | Cell 44: p = 7e-9, inside median lower. |
| fig3e-reward-hotspot-overlap | reproduced | Cell 46: reward hotspot mean -0.526, overlap p = 0.01. |
| fig4-cue-sequence | not_reproduced | Cell 48: 58 of 75 sites under both readings, above 49 ± 4.9. The criterion only grants "partial" for counts below the tolerance, so a high count falls to "not reproduced". With the code's percentiles the count is 52, which is within tolerance (B4). |
| fig4c-cue-correlation | partially_reproduced | Cell 50: 41 negative, 34 positive (outside 26 ± 2.6), latencies 206.0 and -83.3 ms. All 75 sites have a significant DA peak, against the paper's apparent 65. |
| fig4h-extinction-correlation | reproduced | Cell 52, reading (a): 38 of 61 dip sites negative, mean lag 118.4 ms. The selection is 61 sites against the paper's 74, and AD2's mean lag is negative. |
| fig4d-cue-in-out | reproduced | Cell 54: p = 0.023 (9 sites inside vs 66 outside), inside median lower. |
| fig4j-extinction-in-out | reproduced | Cell 56: p = 0.034 (8 vs 53), inside median lower. |
| fig5d-initiation-responses | partially_reproduced | Cell 58: DA dip 129 and DA rise 77 are within tolerance. "DA both" (46) and ACh (107 under reading a, 147 under reading b) are not. |
| fig5-latency-order | reproduced | Cell 61: the order holds and all four medians are within tolerance. ACh peak (277.8) and ACh dip (666.7) sit at the tolerance edge, and the DA peak latencies have an IQR of -444 to 500 ms. |
| fig5e-initiation-topography | not_reproduced | Cell 63: negative-DA sites are more anterior but less lateral (p = 0.996). ACh-dip sites are not more anterior or lateral (p = 0.33, 0.25), and 148 of 174 sites have a dip. |
| fig6a-initiation-correlation | reproduced | Cell 65: 99 of 129 sites negative; mean latency 182.4 ms vs 193.8 ± 16.3. |
| fig6c-initiation-in-out | reproduced | Cell 67: p = 6e-8, inside median lower. |
| fig6g-invigoration-in-out | reproduced | Cell 69: 105 of 160 selected sites negative; in vs out p = 4.5e-5. 160 sites are selected against the paper's 131. |
| fig7-da-release | reproduced | Cell 71: 179 of 180. |
| fig7e-ach-suppression | partially_reproduced | Cell 73: 147 of 180 (82%) vs 116 ± 11.6; this falls in the criterion's 40–90% band. |
| ed9-cohort-hotspot | partially_reproduced | Cell 75: part (i) holds at p = 0.0486 (9 inside). Part (ii): the cohort hotspot is negative but its overlap gives p = 0.085. |
| fig7f-ach-dip-in-out | reproduced | Cell 77: p = 5e-4, inside minima lower. This is weakened by B5. |
| fig8b-quinpirole-region | reproduced | Cell 79: F = 105.87, 3.014, 17.80; DLS mean lower. |
| fig8e-cocaine-region | reproduced (notebook: partial) | Cell 81 used Type II sums of squares, giving stimulus F = 47.68. I reran it with Type III (GraphPad Prism, which the Methods name, uses Type III; the design is unbalanced at 8 vs 5 slices) and got 36.374, 10.754, 199.857, all within tolerance. |
| fig8fg-d2-block | reproduced | Cell 83: F = 231.87 (DLS) and 32.57 (NAcC); the block raises ACh in both. Type III gives the same values. |
| fig8c-cocaine-da-similar | blocked (methods_underspecified) | See C. |

### B. Problems

1. **[affects a conclusion]** `daach.hotspot` finds a "hotspot" in spatially random data. With 150 random sites and independent values, it found one in 10 of 10 runs (125 to 545 voxels), and every one passed the paper's "more extreme than the striatal mean" rule. The cause is a per-voxel 95th percentile with no correction, plus smoothing that clusters the exceedances. As a result:
   - ed1 (the absence of a hotspot in controls) cannot be tested with this procedure.
   - Finding a hotspot in fig1f, fig3e and ed9 says nothing on its own.

   The real fig1f hotspot (1010 voxels) is larger than any of the random ones, which is weak support. The overlap test does look calibrated: independent random maps gave p < 0.05 in 0 of 11 runs.
2. **[affects a conclusion]** Cell 81 (`anova`, `typ=2`): Type II sums of squares give the wrong stimulus F for the unbalanced Figure_8e. Type III reproduces the paper exactly.
3. **[affects a conclusion]** Cell 38 / `transient_pairs`: pairing occurrence is not corrected for chance. The Methods compute a null pairing rate by shuffling DA and ACh traces across days, and the Results say the overlap holds "even after correcting for chance pairing rates due to higher aDLS event frequencies". Cell 40 shows rates are higher inside the hotspot, so some of the raw-occurrence overlap is expected by chance. That chance-corrected part of the paper's statement is untested.
4. **[affects a conclusion]** fig4-cue-sequence, cell 48: the criterion has no band for counts above the tolerance, so 58 of 75 (a clear majority) scores "not reproduced". The outcome also depends on the percentile choice: 52 under the code's percentiles.
5. **[affects a conclusion]** `ads_mask("and")`, cell 75: the AND exclusion barely removes any samples, so the stimulation-evoked responses (DA up, ACh down) stay in the "spontaneous" correlation data. The cohort hotspot used in fig7f is therefore partly built from the same stimulation responses it is then tested against. Cell 77 was not rerun with the OR-exclusion hotspot.
6. **[does not affect a conclusion]** `event_correlation`, polarity -1: `polarity * nan_to_num(seg, nan=-inf)` turns NaNs into +inf peaks. Combined with `distance=3`, this suppresses a real trough within 2 samples of a NaN. In my synthetic test, 10 of 10 such troughs were missed and a noise sample was taken instead. This affects fig6a and fig6c, where DA has about 1% NaNs, plus the NaN padding at session joins. The size of the effect on the real data is unquantified but likely small.
7. **[does not affect a conclusion]** `in_out` uses `scipy.stats.ranksums`, a normal approximation without continuity or tie correction, for groups as small as n_in = 2 or 3. The borderline ed9(i) result (p = 0.0486) moves to about 0.049 with continuity correction.
8. **[does not affect a conclusion]** `transient_pairs` rates divide by the full session duration, including the excluded post-reward periods and NaN spans.
9. **[does not affect a conclusion]** The `Grid` docstring says the axes are "ML, DV, AP"; the code uses AP, ML, DV.

The following checked out:
- Every number is computed from the loaded data.
- Lag sign conventions, `time_since`, `initiations` and `lagged_corr` are correct; I tested each on synthetic inputs.
- Analysis windows match the criteria.
- The 18 Hz rate is justified against the behaviour timestamps.
- There is no train/test structure, so leakage does not apply.

### C. What I could not check, and what would have let me

- **fig8c (blocked):** I confirmed the blocked status. The DANDI archive has only in vivo photometry (17 subjects, all `_ophys.nwb`). On Zenodo, `Figure_8c_TP` is a voltammogram (Voltage/Current), which the notebook didn't mention, and `_LP`/`_RP` hold 3 mice × 2 conditions × 24 time points per region. I tried ANOVA layouts with 9 consecutive or every-second time points, on the cocaine trace, control trace, difference and ratio; none reproduces F = 0.20 / 5.83 / 0.17. The descriptive part can be tested: peak cocaine/control enhancement is about 1.48 in DLS vs 1.47 in NAcC.
- **Chance-corrected pairing (B3):** a null occurrence per site from cross-day DA/ACh shuffles would be needed.
- **Hotspot false-positive rate on the real site coordinates (B1):** the notebook should run the procedure on shuffled site values and report how often a hotspot appears.
- **ADS exclusion mask (B5):** the fraction of samples the AND mask removes, and fig7f rerun with the OR-mask hotspot.
- **Exact rank-sum p values** for the small per-mouse groups.
- **Effect of the NaN trough bug (B6):** the number of fig6a trials where a NaN lies within 2 samples of the anchor.
- **Paper's 65 cue-responsive sites (fig4c):** I can't say why all 75 sites are significant here. The size of the cue-period null pool, and the result with the code's percentiles for this selection, would help.
