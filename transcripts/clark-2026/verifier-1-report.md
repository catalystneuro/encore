**Verifier report, round 1: Clark, Abbott & Sompolinsky (2026) on DANDI:000939 (0.240528.1542)**

The claims file has 30 claims. The four notebooks test 26 of them; the other 4 appear in no notebook. No notebook treats any claim as blocked. I confirmed through the archive API that the pinned version has 31 assets, 9 of them `+ogen.nwb`, as `tuning_curves.ipynb` cell 3 shows.

### A. Outcomes

| claim | outcome | reason |
|---|---|---|
| hd-cell-selection | reproduced | tuning_curves cell 10: 31 sessions, 2,691 units, 1,533 head-direction units under both readings, 0 dropped by nz_mask, 9 opto mice with 315 cells, and counts of 117/93/90/86 for the right mice. |
| tuning-curves-match-cache | reproduced | Cell 12: Pearson r = 1.000000 for 100% of 1,533 units; largest curve difference 1.4e-14. The cache's labels and session order equal the data's. |
| fig1e-heterogeneous-peaks | reproduced | Cell 16: peak counts of 1 to 6 occur; the interquartile range of the separation between the two highest peaks is 1.382 rad, above π/4. |
| fig5d-peak-numbers | reproduced | Cell 18: the data give exactly 1,533/412/55. Generative samples over five seeds give 23,908–24,267 curves with ≥2 peaks and 1,001–1,082 with ≥3, all within tolerance. |
| fig1fg-mean-and-fluctuation-profiles | reproduced | Cell 20: one maximum, at offset 0; symmetry r = 0.9998; sd/mean = 0.56, so both readings hold; median consistency r is 0.996 (mean) and 0.974 (sd). |
| fig3ab-centers-of-mass-uniform | reproduced | Cell 22: 2 sessions with uncorrected P < 0.05, 0 after BH correction, corrected P from 0.592 to 0.968. |
| fig3c-correlation-approaches-circulant | reproduced | Cell 24: the distance from circulant form falls monotonically for all 4 mice and both functions, under all 5 seeds. The leading 4 eigenvectors have ≥0.89 Fourier purity, and eigenvectors 1 and 2 are at frequency 1. |
| fig4-generative-fit | partially_reproduced | Cell 26: the 500k-sample pass chooses σ 1.4737 and β 3.1103, both within tolerance, but b 1.2145, outside 1.73 ± 0.173. The same point wins under all 5 seeds. The paper's grid point comes second (error 0.0095 vs 0.0089), although it ranked first in the 25k-sample shortlist. |
| fig5ab-profiles-match | reproduced | Cell 30: the profiles lie within the mouse range at ≥0.97 of offsets; peaks differ by 3.0% (mean) and 1.3% (sd). This holds at both the fitted and the paper's parameters. |
| fig5c-peak-counts-match | reproduced | Cell 32: total variation is 0.022 at zthresh 1, 0.065 at 0.5 and 0.128 at 0; smallest at zthresh 1 and below 0.15. |
| fig5d-peak-heights-match | reproduced | Cell 34, reading (a): the medians differ by 0.8%, 1.5% and 5.3% for the three peaks. Reading (b) fails for peak 3 (KS distance 0.186). |
| fig5e-flip-symmetry-match | reproduced | Cell 36: the generative fraction in the tail is 1.19× the data's below 0.5 and 1.14× below 0, both within 1.5×. Medians are 0.927 (data) and 0.834 (generative). |
| fig5f-information-match | reproduced | Cell 38: the medians differ by 6.2% and the KS distance is 0.138, so both readings hold (KS only narrowly). |
| fig2l-recorded-bump-tracks-hd | reproduced | Cell 40: reading (a) holds, with a median error of 0.168 rad against π/8 = 0.393. Reading (b) narrowly fails (circular r 0.896). Applying each partition's curves to the other partition's spikes gives 0.172 and 0.177 rad. |
| fig2b-sorted-weights-mexican-hat | reproduced | network cell 7: the profile peaks at offset −8. 88% of intermediate offsets lie below the profile's mean, and 80% are negative. |
| fig2ef-data-network-quasicontinuous | reproduced | Cell 9: readings (a) and (c) hold under all 5 seeds; the median distance falls from 1.97 at 0 s to 0.082 at 1 s, and the manifold angle moves a median 0.0025 rad. Reading (b) fails, because the distance keeps falling until about 5 s. |
| fig2gi-circulant-noise-collapses | partially_reproduced | Cell 11: the circulant-plus-noise matrix ends in 2–7 states (≤10 under all 5 seeds), and the circulant matrix's final states are exact shifts (r = 1.000). The sorted matrix ends in 24–31 states, short of the criterion's 50, so the partial rule applies. That 50 cannot be reached with this measure (problem 3). |
| fig2jk-velocity-integration | reproduced | Cell 13: the median error is 0.011 rad for the constant input and 0.013 rad for A3707's behaviour; circular r = 1.000 for both. |
| figs8-s9-lambda-and-c | partially_reproduced | network_grid cell 4: at c 0 there is divergence or collapse (under reading ii), and no c > 0 diverges. But λ 1e-2 at c 1 does not collapse (radius in the PC plane 4.6, threshold 3.9), and err(1e-8) = 1.7e-8 is not below err(1e-12) = 3.6e-9 (the minimum is at 1e-10). |
| figs11b-data-network-global-stability | partially_reproduced | Cell 17: at standard deviation 1, every final state merges into 1 state, so that part holds. At several standard deviations only 91–94% of final states fall within the largest fig2ef distance at 20 s, against the criterion's 95%. |
| figs14-data-spectrum-doublets | reproduced | Cell 15: the largest \|Im\|/Re among the leading 10 is 0.068, and 4 of 4 pairs are tighter than the gap to the next pair; this is weaker than it looks (problem 6). |
| fig6cd-eigenvalues-real-degenerate | reproduced | theory cell 11, claim seed: the largest relative difference from equation (9) is 5.0%; eigenvalues are real and paired, and the 9th is the Fourier-0 mode. One of 5 seeds exceeds 10% (13.6%). |
| fig6fg-disordered-eigenvectors | reproduced | Cell 13: the model's pair CVs are 0.52–0.53 (structureless) and the circulant's 0.063–0.072 (ring); both spectra have 4 of 4 doublets, under all 5 seeds. |
| fig7-dmft-mexican-hat-and-stability | reproduced | Cell 5: all 12 profiles have a Mexican hat. The bump's second eigenvalue is below 0 and the uniform state's first eigenvalue above 0 at all 800 grid points. With Q fixed the leading eigenvalue is +0.446 (see problem 7). |
| fig7de-dmft-timescales | not_reproduced | Cell 7: "a few τ" fails for both timescales (bump convergence up to 20.5 τ; uniform divergence down to 0.15 τ). "Decreasing" fails for the divergence time, and the max/min ratio over σ reaches 24.3 for it. |
| fig7c-dmft-integrates-behavior | reproduced | Cell 9: median error 0.0315 rad, circular r 0.998. |
| fig8-grid-scores-and-torus | not tested | No notebook cell. The notebook points to an attempt record I don't have. The claim needs only the paper's code, not the archive. |
| figs10-robustness-comparable | not tested | Same as fig8. |
| figs11-s12-global-stability-model | not tested | Same as fig8. |
| figs1-s2-spectrum-does-not-fix-symmetry | not tested | Same as fig8. |

### B. Problems

1. **[affects a conclusion]** tuning_curves cell 26 (fig4). The fit picks b = 1.21, against the paper's 1.73.
   - The paper's point and the chosen one are a near-tie: errors 0.0089 and 0.0095, along a ridge where b and β trade off.
   - The 25k-sample shortlist with 30 re-evaluated points is the author's own deviation. It probably did not change the outcome, since both points were shortlisted and re-run at 500k.
   - The float32 variant was run only at those two points, and favours the chosen point in 4 of 5 seeds.
   - The 500k error at the paper's point is shown for one seed only.
   - The fig5 claims are tested at both parameter sets and come out the same either way.
2. **[does not affect a conclusion]** Cell 12. The printed fraction of smoothing widths that match "exactly" (0.784) is wrong. The comparison uses `==` on floats, and the cache stores values like 0.09999999999999999 where the notebook has 0.1 (both appear in the output). The curves agree to 1e-14; `np.isclose` would give the real fraction.
3. **[affects a conclusion]** network cell 11 (fig2gi). This is a defect in the claims file, which I report rather than correct.
   - The criterion asks for ≥50 states with positions merged within 31 neurons. On 1,533 neurons that cannot be reached.
   - My synthetic test of `count_states` on 103 evenly spaced positions gives single-linkage 1, greedy 35, bins 50.
   - The initial states themselves give only 24–33 states.
   - The notebook's nearest-target variant (50 bins) is the author's own measure.
   - The sorted matrix was run under one seed only.
4. **[affects a conclusion]** network_grid cell 4 (figs8-s9).
   - The criterion's test err(1e-8) < err(1e-12) is stricter than Supplementary Note 3, §8.4, which says 1e-8 "sits just above the minimum". The output fits the paper's wording: the minimum is at 1e-10 and the error rises on both sides. This is a claims-file misreading; reported, not corrected.
   - At λ 1e-2 and c 1 the radius in the PC plane (4.6) is just above the 1/10 threshold (3.9).
   - Reading (i), the raw firing-rate norm, cannot detect collapse: the collapsed state has norm about 17, not near 0. Reading (ii) is the sensible one.
   - 34 of the 42 grid points were run with 20 initial conditions rather than 100 (a stated deviation).
5. **[affects a conclusion]** network cell 17 (figs11b). The threshold is the largest of 100 fig2ef distances at 20 s, run with a 1-ms step. It is compared with 34 runs at 30 s with a 5-ms step. That is a comparison against the noise floor: final maxima are 0.00118–0.00154 against a threshold of 0.00132. With 34 runs, the 95% rule fails as soon as 2 exceed it, so pass or fail is close to chance.
6. **[does not affect a conclusion]** network cell 15 (figs14).
   - Pairs 2 and 4 are complex-conjugate pairs, whose real parts are equal by construction, so they count as doublets trivially.
   - The eigenvalue set aside as the "constant mode" is an arbitrary pick: eigenvectors 5–7 tie with a uniform overlap of 0.041 each.
   - Only pairs 1 and 3 are real evidence of doublets, so the criterion as written passes on weak evidence.
7. **[does not affect a conclusion]** theory cell 5 (fig7).
   - At 293 of 800 grid points the "bump" Jacobian has no zero mode (eigenvalue 1 as low as −0.22), so a bump state is not shown to exist there.
   - The largest second eigenvalue is −4.7e-8, which is effectively zero.
   - The criterion checks only eigenvalue 2.
8. **[does not affect a conclusion]**
   - fig2l: the curves are fitted on the same spikes they are tested on. The cross-partition variant shows this doesn't matter.
   - fig5d-peak-numbers: the samples come from a numpy Generator, not the legacy seed 42. All 5 seeds fall within tolerance.
   - fig6cd: 1 of 5 seeds is outside the 10% criterion.
   - fig2gi: `gaussian_filter1d` uses its default reflect mode, not wrap, on a ring.
9. **[affects a conclusion]** fig8, figs10, figs11-s12 and figs1-s2 have no outputs in any notebook, so they have no outcome.

### C. What I could not check, and the output that would let me

- **fig4:** the 500k error at the paper's grid point under all 5 seeds; a float32 final pass over all 30 shortlisted points; and 500k errors for more than the top 30 points.
- **figs8-s9:** 100 initial conditions at every grid point; the paper's cached flow errors per λ (err_grid on Zenodo) to compare with the notebook's.
- **figs11b:** the fig2ef distance at 30 s with a 5-ms step, as a reference on the same footing; and the initial distances.
- **fig2gi:** the initial-to-final angle shift of each trajectory under the sorted matrix, which tests the continuum directly.
- **fig7:** the bump amplitude (max − min of m) at the 293 grid points without a zero mode.
- **The four untested claims:** any output at all.
- **Raw data:** I did not open the NWB files. Spike and head-direction handling is checked only through the exact match to the cache and the clock-lag test in cell 8 (all 31 sessions peak within 0.1 s of zero lag).
- **Chance levels:** the paper states none for any claim. The notebook's 60-s shifted null for fig2l gives 1.294 rad, against the uniform expectation of π/2.
