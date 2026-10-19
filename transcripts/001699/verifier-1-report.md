I checked all 27 claims in the claims file and assigned outcomes myself from the notebook outputs, since the attempt record was not in my materials. My tally is 14 reproduced, 7 partially reproduced, 5 not reproduced and 1 blocked. The main caveat is the relabelling of rat H3026 (problem 1): with the archive's own genotype labels, three of the four juvenile positive results stop being significant.

**What I checked**
- **LME test:** `hdfx.lme_lrt` matches statsmodels on synthetic data to four decimals, for both the coefficient and the likelihood-ratio p (maximum-likelihood fits).
- **Other helpers on synthetic inputs:** `hd_info`, `half_width`, `vector_length`, `offset_deg`, `trough_to_peak` and `contamination` behave as expected, in the right units.
- **Train/test split:** the decoder builds tuning curves from the first half of session 1 and decodes only the second half, so there is no leakage.
- **Chance levels:** none of the claims states one.
- **Paper:** version 1 is saved as `paper/v1.xml` and `paper/v1.txt`.

**A. Outcomes**

| claim | outcome | reason |
|---|---|---|
| unit-counts | partially_reproduced | Cell 26, reading (a): juvenile WT 406/7, juvenile KO 372/5 and adult WT 543/6 match exactly; adult KO is 440/5 against 507/6, so 3 of 4 groups match. The archive's labels match 0 of 4. |
| units-per-recording | partially_reproduced | Cell 28: juvenile 8 to 83 matches under (a) all units. Adult is 55 to 114 under (a) and 30 to 81 under (b), so the adult pair never holds under one reading. |
| figs1c-juvenile-behaviour-similar | reproduced | Cell 30: p = 0.37, 0.085 and 0.0504, none significant. Fragile: the speed t is 2.22 against the paper's 1.53, and the first-day variant gives p = 0.031. |
| figs2c-adult-behaviour-similar | reproduced | Cell 30: p = 0.98, 0.35 and 0.67 (t(9); only 5 adult KO rats). |
| figs1-juvenile-cell-metrics-similar | reproduced | Cell 32: LME p = 0.71, 0.72, 0.62 and 0.11. |
| figs2-adult-cell-metrics-similar | reproduced | Cell 32: LME p = 0.11, 0.35, 0.11 and 0.25. |
| fig1ef-juvenile-sharper-tuning | partially_reproduced | Cell 34: HD information is higher in KO (p = 0.033); half-width p = 0.69. HD information is fragile: log values p = 0.12, archive labels 0.24, uniform occupancy 0.08. |
| fig1g-juvenile-halves-correlation | not_reproduced | Cell 36: WT r = 0.761 (needs ≥ 0.81), KO r = 0.840 (needs ≥ 0.855). |
| fig1h-juvenile-smaller-offset | reproduced | Cell 38: KO smaller, p = 0.0125; cells with half-width below 120° give p = 0.016. Archive labels give p = 0.080. |
| fig1j-juvenile-less-drift | not_reproduced | Cell 40: t(10) = -1.95, p = 0.079. The direction matches the paper. |
| figs1j-juvenile-epochs-correlation | partially_reproduced | Cell 42: WT 0.854 is within tolerance; KO 0.757 misses the 0.765 bound. |
| figs1k-juvenile-epoch-drift-similar | reproduced | Cell 42: LME p = 0.93. |
| fig2c-juvenile-isomap-wake-correlation | reproduced | Cell 44: WT 0.826 and KO 0.914, both within tolerance. |
| fig2d-juvenile-isomap-wake-sharper | reproduced | Cell 44: KO higher, p = 0.046. Fragile: first day p = 0.12, archive labels 0.15, log values 0.09. |
| fig2g-juvenile-isomap-rem-correlation | partially_reproduced | Cell 46: KO 0.833 is within tolerance; WT 0.831 is above the 0.803 upper bound. |
| fig2h-juvenile-isomap-rem-sharper | not_reproduced | Cell 46: KO higher, but p = 0.056. |
| fig3ef-adult-tuning-similar | reproduced | Cell 48: p = 0.58 (HD information) and 0.64 (half-width). |
| fig3g-adult-halves-correlation | not_reproduced | Cell 50: WT 0.810 and KO 0.742, both needing ≥ 0.846. |
| fig3h-adult-larger-offset | reproduced | Cell 52: KO larger, p = 0.040; cells with half-width below 120° give p = 0.017. Rat-mean t-test p = 0.071. |
| fig3j-adult-more-drift | reproduced | Cell 54: t(9) = 2.75, p = 0.022, KO higher. |
| figs2j-adult-epochs-correlation | not_reproduced | Cell 56: WT 0.786 (needs ≥ 0.81), KO 0.570 (needs ≥ 0.684). WT is still above KO, as in the paper. |
| figs2k-adult-epoch-drift-larger | reproduced | Cell 56: KO larger, p = 0.028. |
| fig4c-adult-isomap-wake-correlation | partially_reproduced | Cell 58: WT 0.935 is within tolerance; KO 0.688 misses the 0.81 bound. |
| fig4d-adult-isomap-wake-similar | reproduced | Cell 58: p = 0.97. |
| fig4g-adult-isomap-rem-correlation | partially_reproduced | Cell 60: WT 0.820 is within tolerance; KO 0.656 misses the 0.72 bound. |
| fig4h-adult-isomap-rem-similar | reproduced | Cell 60: p = 0.29. |
| figs1d-probe-in-posub | blocked (other: needs anatomical judgement; tract and PoSub are not annotated) | Archive check: 32 of 36 NWB files carry `+image` in their names. The files of H3001 (both days), H4822 and H4823 do not, so there are no images for 3 rats. The most anyone could test is whether images exist per rat, not whether the tract passes through PoSub. |

**B. Problems**

1. [affects a conclusion] Genotype and age relabelling (cells 8–9; `hdfx.JUVENILE_KO`, `JUVENILE_WT`). H3026 is moved from WT to KO and H3029 from adult to juvenile WT, inferred only from unit totals. The exact matches to 406 and 372 support it, and the claims file prescribes it, but nothing in the archive confirms it. H3026 supplies 92 of the 237 juvenile KO cells. Under the archive's labels, fig1ef HD information gives p = 0.24, fig1h p = 0.080 and fig2d p = 0.15.
2. [affects a conclusion] Cells recorded on more than one day are counted on every day (`analyse`; the claims file accepts this); the paper excluded them. This inflates the number of cells behind the near-threshold LME results. For fig2d the first-day-only variant gives p = 0.12, so that "reproduced" depends on the double counting.
3. [does not affect a conclusion] In cell 40, H3001 200201 has its decoder drift computed from only 22 bins (4.4 s), against 500 to 2,700 bins elsewhere. The cause was never examined. Dropping it raises fig1j's p further.
4. [does not affect a conclusion] `frame_counts` is applied to speed-filtered frames that are not contiguous. It zeroes the spikes of the last frame before every gap longer than 2 frames, and gives a frame its neighbour's spikes after a 1-frame gap. On synthetic data with frequent 1-frame gaps it lost 2.6% of spikes. The bias is small, mostly on peak rate.
5. [does not affect a conclusion] Session length is inconsistent (`exploration_sessions`). Blocks of 20 to 30 min are kept whole (H3001 200201 runs 27.7 min), while blocks over 30 min are cut to 1300 s; the paper's sessions are 20 min. H3001 200202's "session 1" is the block after sleep.
6. [does not affect a conclusion] `isomap_angle` fits on 3,000 subsampled bins and projects the rest out of sample; the paper fits all bins. The effect of this was never measured.
7. [does not affect a conclusion] In `hdfx.drift`, the decoding error is interpolated across invalid bins on wrapped angles before unwrapping, and then feeds the Hampel filter and smoothing of neighbouring valid bins.
8. [does not affect a conclusion] The within-session and between-session offsets include untuned cells, whose offsets are random between 0 and 180°. The offsets therefore partly measure tuning strength. The half-width below 120° variants hold (p = 0.016 and 0.017).
9. [does not affect a conclusion] Cell 7 says no file sets the subject's age. The DANDI asset metadata does carry ages (for example P26D), derived from the birth date, including the negative ages of H3023 and H3026.

**C. What I could not check, and the output that would have let me**

- **Why the halves and between-session correlations come out low** (fig1g, fig3g, figs2j). A half-1 against half-2 scatter plot, Spearman r, and r for first-day cells only would show whether outliers or double-counted cells drive it.
- **The 22-bin drift recording.** For each recording, the number of second-half bins with valid tracking and with speed above 2 cm/s.
- **Position values.** The minimum y position is exactly 0.0 in every file stored in centimetres. A count of frames with y == 0 per file would show whether this is an offset or missing tracking coded as 0, which matters for speed and the centre measure.
- **A possible ceiling on Isomap HD information.** In adults the maximum Isomap waking HD information is 2.476 in both genotypes. The recording and unit holding each maximum would show whether that is a coincidence.
- **The Isomap subsampling.** Isomap HD information for one recording with a full fit, set beside the subsampled fit.
- **H3026's genotype.** The files hold no genotyping record; the conclusion rests on problem 1.
- **REM intervals inside exploration sessions** (4 in H3015 210416_2, 3 in H4822). The REM Isomap result with those intervals removed.
