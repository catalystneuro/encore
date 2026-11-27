I've finished steps 1 to 5 for paula-2026 and built the handover with `tools/entry.py handover`; I did not verify the work myself. `tools/entry.py all` passes: 0 errors, and a clean-environment run takes 36.5 minutes, of which 35.7 are spent streaming the 153 sessions. Nothing is committed.

The main caveat: neither of the claims file's unit-selection readings reproduces the paper's counts. I used all 153 sessions and all units, so almost every outcome rests on that assumption.

## 1. Outcomes (38 claims, none blocked)

| Outcome | Claims |
|---|---|
| Reproduced (12) | fig2a-vis-cv-by-condition, fig2a-thalamus-cv-by-condition, fig2b-visually-driven-js-cv-low, fig3b-complexity-levels-by-region, fig3d-th-ch-plane, fig3e-hp-ch-plane, fig3f-mb-ch-plane, fig4b-thalamus-lgd-lp-modulated, fig4b-other-thalamus-not-modulated, fig4c-dg-ca3-complexity, fig4d-midbrain-complexity-invariant, complexity-separates-images-from-spontaneous |
| Partially reproduced (16) | fig1c-cv-above-surrogate, fig1e-positive-cv-modules, fig1e-dg-ca3-anticorrelation-hubs, fig1e-midbrain-weakest-cv-correlations, fig2a-hippocampus-cv-stable, fig2a-midbrain-cv-invariant, fig2b-vis-summed-js-cv, fig2b-dg-ca3-high-js-cv, fig3a-reference-systems, fig3c-vis-ch-plane, fig4a-vis-complexity-by-condition, fig4e-js-complexity-natural-images, supp-robustness-parameters, fig5-vis-complexity-cv-coupling, fig5-th-weaker-coupling, fig5-mb-flat |
| Not reproduced (10) | table1-sample, fig1c-cv-region-medians, fig1d-surrogate-abolishes-cv-correlations, fig2b-hp-mb-summed-js-cv, fig2b-legend-js-cv, fig3-complexity-range-fractions, fig4fg-js-complexity-active-blanks, fig4h-js-complexity-spontaneous-converges, fig5-hp-spontaneous-elevated, supp-fig6-mean-correlation |

Every outcome except table1-sample is marked `assumed: true`. No outcome changes across the five seeds.

## 2. Dataset, assumptions, questions

**Dataset.** Pinned version 0.240702.1725, the one the paper cites and the only published one.
- 153 ecephys sessions from 81 mice. Each has an active block of 3599 to 3611 s, a 289-s gray screen after it, and eight images.
- No recording appears twice.
- Spike times share the stimulus table's clock in all 153 sessions: there is a visual response to flash onsets, and none to onsets shifted into the gray screen.
- The paper's 102 sessions cannot be identified: all 153 pass both session readings in the claims file.
- Some units carry generic location labels (TH, MB, HPF).
- No data findings above severity "none".

**Assumptions.**
- **Unit selection: all units.** Table I is not matched under either reading. "All units" gives about 1.5 to 3 times Table I's neurons per subregion; the Allen quality filters give 0.23 to 0.88 times. I adopted "all units" because it keeps exactly Table I's 26 subregions; the filtered reading is shown as a variant.
- **fig4b test.** For the unnamed "modulation" test I used pairwise Mann-Whitney. Under Kruskal-Wallis instead, MGd, SGN, MGm and MGv also reach p < 0.001, and fig4b-other-thalamus-not-modulated would become not reproduced.
- **fig4b effect size.** I measured the thalamic effect as the largest visually driven median minus the spontaneous one. Using the mean of the three conditions instead reverses the LGd-versus-VISrl comparison.
- **fig3a.** I chose how to sample the sine and what counts as "near 0".

**Questions for the paper's authors.** These are recorded as `methods_unavailable` or `selection_undocumented` findings:
- Which 102 sessions were used?
- Which units form a population?
- How long a span was shuffled for the surrogates? Shuffling within each 100-s window leaves the surrogate CV series correlated across regions (|r| up to 0.80).
- What histogram bins and summation were used for the JS divergences?
- Which test was used for "modulation" and for "all pairwise comparisons"?
- What were the Fig. 5 CV bins and the Fig. 3a parameters?
- How were the blank intervals defined? The files give about 287 s of blank per image, not the stated ~240 s.

**Questions to a reader:** none.

## 3. Where the protocol was unclear or missing something

1. Surrogates are shared by several claims, but seeds are per claim. I drew them once under fig1c-cv-above-surrogate's seed, combined with the session and window indices, and recorded this as a deviation on each claim that uses them.
2. Several criteria have no partial rule. I used `partially_reproduced` when the qualitative part held and some values missed, following the protocol's general definition.
3. The checker requires `inputs` on a tested `data: elsewhere` claim, even when the data are synthetic. I listed the supplement's definitions (Sec. I) as the input.
4. The protocol does not say that thread-count settings must come before numpy is first imported in a notebook. My first clean run hit the 60-minute cell timeout because each of the four worker processes ran several BLAS threads at once (load average about 13 on 4 CPUs). Setting the variables in the first cell fixed it.
5. The pilot-19 code in `entry.py` reads `notebook` and `output` on findings, but the attempt schema rejects them. I left them off.

## 4. Runtime and failures

The run took about 3 h 36 min, from 10:00 to about 13:36 UTC.
- My one development pass over all sessions took 35 min.
- The first `entry.py all` failed on the 60-minute cell timeout (point 3.4).
- The second and third runs passed in about 37 min each. The third was only to remove bold labels and add the header's claims table.

Nothing else failed, and no session failed to load.
