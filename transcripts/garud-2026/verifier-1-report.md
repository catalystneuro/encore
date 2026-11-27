**A. Outcomes** (18 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| floeder-subjects-sessions | reproduced | Cell 14: 18 mice, 16 to 24 sessions each, both classes in every mouse. Class medians are 16.6 and 53.7 s. Sessions run in blocks (L…S…L), not day-by-day alternation (cell 5); the criterion does not test the order. |
| fig4a-lick-short-above-long | reproduced | Cell 16, two-tailed paired t-test: short 2.39 Hz against long 1.60 Hz, t(17)=4.15, p=6.7e-4 (reading a) and 6.8e-4 (reading b). Short is higher in 16 of 18 mice. |
| fig4b-long-iti-dip-below-baseline | partially_reproduced | Cell 18: the long-ITI measure is below 0 under all 8 readings (t −11.6 to −13.7, p<1e-9). The short-ITI last kept bin is below zero (−0.0067 ± 0.0011 SEM, above 0 in 1 of 18 mice), so the short-ITI part fails. |
| fig4d-dip-deepens-with-training | partially_reproduced | Cell 21: no reading meets the full criterion. fit/reward/trials with all-session numbering gives slope<0, p=0.0043, r_within −0.283 (in tolerance); the two readings with p<0.001 have r_within ≈ −0.35 (out of tolerance). |
| fig4c-lick-rate-rises-with-training | reproduced | Cell 24, long-only sessions with all-session numbering: slope 0.103, p=1.2e-5, r_pooled 0.648 (tolerance 0.585 to 0.715). |
| krausz-included-observations | reproduced | Cell 26: exactly 264,042 rows across 10 rats. |
| fig2a-ramp-toward-goal | reproduced | Cell 28: mean per-rat r = −0.68, t(9)=−7.25, p=4.8e-5. |
| fig2b-ramp-scales-with-reward | reproduced | Cell 30: high slope −0.036 against low −0.015, t(9)=−7.30, p=4.6e-5. The mean-DA reading also holds. |
| fig2c-ramp-similar-early-late | reproduced | Cell 32: p=0.52 (claim of absence). The late ramp is slightly steeper (−0.0277 against −0.0253), so the legend's "modest reduction" is not seen. |
| fig2d-ramp-scales-with-velocity | reproduced | Cell 34: fast 0.162 against slow −0.053, t(9)=7.40, p=4.1e-5, 10 of 10 rats. |
| fig2e-velocity-covaries-with-distance | reproduced | Cell 36: r(distance, velocity) −0.66, p=5e-5. r(DA, velocity) 0.59, p=7e-6. |
| fig2f-coupling-grows-near-goal | reproduced | Cell 38, reading (a): r=−0.494, df=18, p=0.027, an exact match. Readings (b) and (c) miss the tolerance. |
| fig2gh-stationary-dip | reproduced | Cell 40, reading (b1), all rows off the ports: t=−4.274, p=0.001, one-tailed. The Methods reading (a) gives t=−2.81, out of tolerance. |
| fig3-recovered-value-increases | partially_reproduced | Cell 42: A>0 in 7 of 10 rats (min_obs 1) and 6 of 10 (min_obs 5). The criterion gives partial for 7. Only the approach-row stationary set was run (problem 1). |
| fig3cd-gaussian-shape-wins | partially_reproduced | Cell 44: Gaussian wins in 9 rats, with one exponential or one power-law (not 8/1/1). Mean R² is not above 0.8 for all four shapes under either reading. |
| fig5bc-gaussian-ct-td-best | reproduced | Cell 46: CT TD Gaussian has the lowest summed BIC and wins in 8 of 10 rats. |
| fig5d-tonic-term-and-gaussian-contribute | reproduced | Cell 48, reading (a), main effects: 1170.1 and 695.6, both within tolerance. Robustness is unchecked (problem 2). |
| figs2-no-velocity-coupling-without-goal | blocked (methods_underspecified) | The method is in the supplement, which was not read. The Brown et al. data are not in DANDI:001552: I queried the API, which lists 502 assets, all Floeder. |

**B. Problems**

1. [affects a conclusion] Cell 42 / `recover_value`: Fig 3 was run only on the approach rows `I`. The Methods give Fig 2G–H and Fig 3 the same moving/stationary split, and fig2gh matched the paper only with set (b1), all rows off the ports. Fig 3 was never run on (b1), so a reading that could move 7 rats to 8 is untested.
2. [affects a conclusion] `fit_model` and `fit_profile` limit the spatial scale with grids (λ from 1e-4 to 5, σ from 0.3 to 100). The paper's Nelder-Mead is unconstrained, so negative λ is allowed. Cell 46 shows fits stuck at a grid bound: 3 for IM-1322 (σ=100, λ≈0), 2 for IM-1398 and 2 for IM-1532. A lower SSE for CT TD exp or Value would change both ΔBICs of fig5d reading (a), whose tolerance margin is only about 10, and could change per-rat winners in fig5bc. Cell 42 also contains a degenerate fit (A = −6.9e10, IM-1292).
3. [does not affect a conclusion] `dff` together with "baseline = ΔF/F 0", in cells 18 and 21: with the session-wide regression, mean ΔF/F is 0 by construction. I confirmed this on synthetic data: stretches without transients come out negative. A late-ITI value below 0 is therefore largely forced, and the fig4d trend could reflect growing phasic responses. The notebook follows the claims file correctly here, but the test cannot separate a tonic dip from this centering.
4. [does not affect a conclusion] Cell 9: in short-ITI sessions the true-time reward contrast is negative (−0.0045 against +0.0026 for shifted times), so alignment in short sessions is not verified directly. The bin-0 peak in cell 19 (+0.018) suggests alignment is fine.
5. [does not affect a conclusion] Cell 37 markdown says distances 1 to 20 are "the ones with the most rows". Distance 21 has 1097 rows, more than distance 20 (908). The result still matches the paper exactly.
6. [does not affect a conclusion] Cell 28 averages DA per distance. The Methods and the criterion average per hex position.
7. [does not affect a conclusion] Cell 3 checks only the first VR-FP file for the missing event log. Archive metadata supports excluding all 144 VR-FP assets: their variableMeasured is empty, while every FP and dLight-ramp2 asset lists ProcessingModule.
8. [does not affect a conclusion] The fig4b criterion says to adopt the best-supported reading. Cell 5 has evidence for the ITI-from-reward reading: the reward-to-next-cue medians (7.57 and 44.72 s) match the paper's ~8 s and ~45 s. The notebook does not adopt it, but the fig4d outcome is the same either way.

**C. Could not check**

- Whether the FP and dLight files' ProcessingModule holds a depositor ΔF/F that the paper might have used. Needed: a listing of `processing/` for one file.
- Units of `nom_rwd_*`. The values 10, 20, 50, 80 and 90 look like reward probabilities in percent, not µL. Needed: the Mendeley column description.
- Fig 3 on the (b1) stationary set, and `fit_model` with λ allowed negative and a wider σ range. Needed: those fits with per-model SSE and the resulting ΔBICs.
- An alternative fig4b baseline, such as a pre-cue window. Needed: a cue-locked short-ITI trace to confirm alignment.
- The supplement, for figs2 and for the Fig 4 details left open.
