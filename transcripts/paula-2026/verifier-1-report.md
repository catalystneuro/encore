**Verifier report, round 1: de Paula et al. 2026 (doi:10.1103/wndc-k654) on DANDI:000713 0.240702.1725**

The claims file has 38 claims. The notebook tests all 38 and treats none as blocked. My outcomes: 10 reproduced, 6 partially reproduced, 22 not reproduced.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| table1-sample | not_reproduced | 153 sessions under every reading, against 102 (cell 8). With all units, the neuron counts are about 2× Table I. With the quality filter (qc), the window counts match but the populations and neurons do not. |
| fig1c-cv-region-medians | not_reproduced | All units: the medians of DG (0.564) and NB (0.564) fall outside the widened ranges, and the TH, HP and MB extremes miss. qc: the TH maximum (0.414) misses (cell 12). |
| fig1c-cv-above-surrogate | partially_reproduced | Every Mann-Whitney test gives p ≤ 1.5e-73 with empirical higher, and the VIS surrogate medians are 0.225 to 0.243. The HP ratios for POST (1.32) and DG (3.01) fall outside 1.35 to 2.42 under all five seeds (cell 14). This is the claim's partial rule. |
| fig1d-surrogate-abolishes-cv-correlations | not_reproduced | Surrogate \|r\| reaches 0.79 under reading (a) and 0.66 under (b). 115 and 213 pairs exceed 0.2 (cell 16). |
| fig1e-positive-cv-modules | not_reproduced | Reading (a): top value 0.772, above 0.737. Reading (b): low end 0.450, just outside 0.50 ± 0.05. Same-area fractions (66% and 81%) do hold (cell 18). |
| fig1e-dg-ca3-anticorrelation-hubs | not_reproduced | Reading (b): CA3 and DG are the hubs, but the most negative r is −0.178 (expected −0.27 ± 0.027). Reading (a): NB is the hub and the most negative r is −0.496 (cell 20). |
| fig1e-midbrain-weakest-cv-correlations | not_reproduced | Reading (a): MB mean \|r\| (0.186) is above HP (0.179). Reading (b): only 2 of 115 MB pairs are near zero (cell 22). |
| fig2a-vis-cv-by-condition | reproduced | 12/12 medians within tolerance under readings a/a and b/a with all units (cell 26). The values sit near the upper edge of tolerance, and with qc only 8/12 are within (see B1). |
| fig2a-thalamus-cv-by-condition | reproduced | 4/4 values within tolerance under every reading, and the LP and LGd effects are smaller than in VISp, VISl and VISal (cell 28). |
| fig2a-hippocampus-cv-stable | not_reproduced | DG medians are 0.555 to 0.580, against 0.48 to 0.51 ± 10% (cell 30). This was not run with qc, where DG active is 0.481. |
| fig2a-midbrain-cv-invariant | not_reproduced | MRN maximum is 0.233, against the limit of 0.231 (cell 32). |
| fig2b-vis-summed-js-cv | partially_reproduced | No combination is fully reproduced. Four of 32 meet the partial rule: active and blanks are the closest pair and every other pair differs by more than 15%. Active against blanks is 0.32 to 0.53%, below the 0.5% lower bound (cell 36). |
| fig2b-hp-mb-summed-js-cv | not_reproduced | HP active against spontaneous is 41 to 71%, and the MB maximum is 22 to 41% (cell 38). |
| fig2b-visually-driven-js-cv-low | partially_reproduced | The percentage form, which is the claim's statement, holds in 0/32 combinations. The legend's JS-value form holds in all 8 (cell 40). |
| fig2b-dg-ca3-high-js-cv | not_reproduced | CA3 spontaneous median is at most 0.638 and CA3 blanks at most 0.419, against 0.84 and 0.63 (cell 42). |
| fig2b-legend-js-cv | not_reproduced | TH > 0.33 in at most 1/9 subregions and VIS > 0.44 in at most 3/6, under both readings (cell 44). |
| fig3a-reference-systems | partially_reproduced | White noise, logistic (r = 4) and tent (μ ≈ 2) fit, and so does the correlated walk at α 0.2 to 0.3. The walk at α 0.5 to 0.7 has C 0.23 to 0.26, below range. The other two failures come from the notebook's own choices (B3). |
| fig3b-complexity-levels-by-region | reproduced | Reading (a): VIS 0.161, HP 0.163, TH 0.109, MB 0.101, and the order holds at 36/36 window indices. It also holds with qc (cell 48). |
| fig3c-vis-ch-plane | not_reproduced | The C 2.5th percentile is 0.089, below the 0.090 bound, and the 0–100 span has H down to 0.462. The test (p ≈ 0) and the surrogate median (0.0955) pass. It is a narrow miss (cell 52). |
| fig3d-th-ch-plane | reproduced | The 95% span is inside the range, narrower than VIS, and p < 0.001 (cell 54). |
| fig3e-hp-ch-plane | reproduced | The 95% span is inside, it is the widest of the four areas, and p < 0.001 (cell 56). |
| fig3f-mb-ch-plane | reproduced | The 95% span is inside, it is the narrowest, and p = 2e-194 (cell 58). The 0–100 variant fails. |
| fig3-complexity-range-fractions | not_reproduced | 0/8 within tolerance on active windows, 1/8 on image windows (cell 60). |
| fig4a-vis-complexity-by-condition | not_reproduced | In VISp, natural images (0.178) are not above active (0.190), and images against blanks gives p = 0.53. So the order fails, and the partial rule needs the order (cell 64). |
| fig4b-thalamus-lgd-lp-modulated | reproduced | Kruskal-Wallis p ≤ 3e-63, the visually driven medians are above spontaneous, and the values match the legend's. The effect is smaller than in every VIS area only under effect form (i); form (ii) fails for LGd against VISrl (cell 66). |
| fig4b-other-thalamus-not-modulated | partially_reproduced | Medians are 0.093 to 0.108, inside the range. Kruskal-Wallis finds p < 0.001 in MGd, SGN, MGm and MGv. The pairwise reading passes only as implemented (B4) (cell 68). |
| fig4c-dg-ca3-complexity | reproduced | Holds on the legend reading with spontaneous reading b (a/b, b/b), with the peak in spontaneous activity. The text reading fails because CA1 reaches 0.162. Under a/a, CA3 spontaneous (0.198) sits right at its bound (cell 70). |
| fig4d-midbrain-complexity-invariant | reproduced | Legend values hold and NOT has the largest range across conditions. The text values fail (APN 0.086) (cell 72). |
| fig4e-js-complexity-natural-images | not_reproduced | VIS-VIS, VIS-TH and VIS-MB hold. Only 20% of DG/CA3 pairs lie in 0.27 to 0.55 (median 0.16) (cell 76). |
| fig4fg-js-complexity-active-blanks | not_reproduced | VIS against subcortical pairs above 0.36: 29 to 38%. HP-HP pairs in range: 27 to 33% (cell 78). |
| fig4h-js-complexity-spontaneous-converges | not_reproduced | The mean of all spontaneous pairs is not the lowest (0.264 to 0.332 against 0.218 to 0.255 for blanks) (cell 80). |
| supp-robustness-parameters | partially_reproduced | The pattern holds in 4 of 5 combinations; bin 20 ms with D 3, τ 4 fails (cell 82). This is the claim's partial rule. |
| fig5-vis-complexity-cv-coupling | not_reproduced | The CV spans exceed the quoted ones, and the spontaneous maximum is at least 0.180, against < 0.165 (cell 86). |
| fig5-th-weaker-coupling | not_reproduced | The slopes are positive and below VIS, but the spans exceed CV 0.88 or C 0.22 under every reading (cell 88). |
| fig5-hp-spontaneous-elevated | not_reproduced | The spontaneous peak is 0.238 to 0.244, but the visually driven maxima are 0.17 to 0.41 rather than about 0.19, and spontaneous does not exceed them (cell 90). |
| fig5-mb-flat | not_reproduced | MB bin means reach 0.17 to 0.35 in active and blanks; only the slope part holds (cell 92). |
| supp-fig6-mean-correlation | not_reproduced | VIS active and blank medians are 0.007 to 0.052, against 0.08 to 0.13 (cell 94). |
| complexity-separates-images-from-spontaneous | reproduced | JS reading: complexity has the larger JS in 6/6 VIS subregions under every reading. The IQR reading holds in only 1 to 2 of 6 (cell 96). |

Step 4 does not apply, since no claim is treated as blocked. I queried the archive myself: it has 4293 assets, 153 ecephys session files and 81 subjects. Nothing in the asset list picks out the paper's 102 sessions.

### B. Problems

1. **[affects a conclusion] The unit reading was chosen against the claims file (cells 8–10).** The claims file says the Table I neuron counts decide between the readings. On those counts, qc is much closer than all units:
   - VIS neurons: qc 0.82× Table I, all units 2.05×.
   - Window counts: qc puts all four within tolerance, all units puts none.

   Yet the notebook takes all units as its main reading, citing an "assumption, above" whose reasoning does not appear in this notebook. qc is run only for fig1c (both claims), fig2a-vis, fig3b and fig3-fractions. Where it was run it changes things: fig2a-vis drops to 8/12. It could change fig2a-hippocampus (qc DG active 0.481, CA3 0.395) and others. qc also undercounts (TH about 0.5×), so a looser filter was never tried. The claims file's presence-ratio cutoff of 0.9 is unverified; to my knowledge the AllenSDK default is 0.95. That is a claims-file issue to report, not to correct.
2. **[affects a conclusion] The session count is unexplained (cells 4, 8).** There are 153 sessions against 102. Session reading (b) changes nothing, because all 153 sessions have the spontaneous epoch. Every pooled median is therefore over a different sample from the paper's.
3. **[affects a conclusion] fig3a uses two of the notebook's own choices (cell 46).**
   - **Ikeda parameter.** It is judged at p = 6, called "fully chaotic" without a source. The map's t = p − 6/(1+x²+y²) repeats every 2π in p, so the textbook chaotic attractor (0.4) sits at p ≈ 6.683 or 12.966, inside the supplement's [5, 17]. Neither value is in the sweep. I ran it: p = 6.683 gives H 0.811, C 0.355; p = 6.5 gives H 0.794, C 0.367, which is inside the widened range.
   - **Sine tolerance.** The rule "H ≤ 0.05" cannot be met. Any sine produces at least two ordinal patterns, so H ≥ ln 2 / ln 720 = 0.105. At 10⁴ points per period I get H 0.107.
4. **[affects a conclusion] fig4b-other-thalamus-not-modulated: the pairwise test is too lenient (`thal_tests`, cell 68).** A nucleus counts as modulated only if all three visually driven conditions differ from spontaneous at p < 0.001. For a claim of absence, that means one non-significant pair is enough to pass. The smallest pairwise p is not printed. Given Kruskal-Wallis p down to 3e-7, some pairs are probably significant, although the median differences are at most 0.006.
5. **[does not affect a conclusion] fig4b-thalamus-lgd-lp-modulated: the effect definition is the notebook's own (cell 66).** Forms (i) and (ii) are not from the paper or the claims file. Both were run, and the outcome rests on (i).
6. **[does not affect a conclusion] The natural-log JS variant from the claims file was never run (cells 34, 74).** The percentage claims do not depend on the log base, and the threshold claims fail on clauses that rescaling does not rescue (for example fig4h's spontaneous-mean condition).
7. **[does not affect a conclusion] fig2b-legend reading (b) is the notebook's own form (cell 44).** It uses the mean absolute row difference. Both readings fail on TH in any case.
8. **[does not affect a conclusion] fig1d reading (a) is confounded (cell 16).** Concatenating across sessions mixes in session-level differences in surrogate CV, which depend on N and firing rate. Shuffling within each window also keeps the window-to-window rate changes. Both inflate surrogate correlations. The method is as the claims file prescribes, and reading (b) also fails.
9. **[does not affect a conclusion] The blank series are longer than the paper's (cell 4, `flash_table`).** The median is 286 s, against the paper's "about 240 s", so the blank definition differs from the paper's for an unknown reason. It cannot be ruled out that this shifts the blank-condition values.
10. **[does not affect a conclusion] The tests treat every window as independent (cells 14, 50, 62).** Windows pooled across populations and sessions are pseudo-replicated, so the p-values are far smaller than the data justify. The paper appears to do the same, and no claim's outcome turns on this.
11. **[does not affect a conclusion] C-H spans are rounded before comparison (`ch_table`, cell 50).** Spans are rounded to 3 decimals and then compared with the bounds. I checked that no outcome flips.
12. **Helpers check out on synthetic inputs.** `bandt_pompe` matches an independent implementation to 1e-15, with ties ranked higher for the later element, white noise at C 0.0006 and a constant series at 0. `js_divergence` gives 0 for identical and 1 for disjoint distributions. `shuffle_isi` keeps each unit's intervals and last spike. `concat_windows` places the pieces correctly. `mean_corr` and the Q0 constant are correct.

### C. What I could not check, and the output that would settle it

- **The qc reading for every claim.** Re-running each judging cell with `WQ`/`ACTQ`, plus the fig2a-vis order check under qc, would show which outcomes depend on the unit reading.
- **Neuron counts under other unit filters.** Counts for `quality == "good"` and for presence ratio > 0.95 against Table I, using the existing `survey_session`, would test filters closer to the paper's counts.
- **The 102 sessions.** Session counts broken down by genotype, image set or experience level, and number of probes might identify the paper's subset.
- **fig4b-other.** All six pairwise p-values per thalamic nucleus, including the smallest.
- **Blanks.** The distribution of blank-piece durations and the number of flashes per image, to compare with "about 240 s".
- **JS in natural logs.** Outputs of the JS tables with base e.
- **Figures.** The PDF figures were not readable (as also noted in the claims file), so the Fig. 3a parameters, boxplots and matrices were not compared by eye.
