**A. Outcomes** (36 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| fig1e-oxtr-avpr1a-coexpression | blocked (other) | The claims file marks this `data: with_inputs` (the outside Kim et al. 2019 atlas). The notebook did not attempt it, so the claim was testable in principle but went untested. |
| fig1f, fig2e, fig2g, fig2-bilateral-editing-spares-sniff-and-mating, fig3c, fig3d, fig3fh, figs3ef, figs7cd, figs7k, figs7l | blocked (data_missing) | I checked the archive API. Version 0.260601.1203 has 10 resident-intruder NWB files. Their metadata lists only BehavioralEpochs and ProcessingModule. There are no slice, photometry or behaviour-cohort files. |
| methods-unit-counts | not_reproduced | Cell 15: 4 control mice with 587 units (paper: 5 mice, 585) and 6 experimental mice with 554 units (paper: 7, 546). The 4 control mice alone already exceed the paper's 585, so the gap is not only the missing mice. |
| figs4a-unilateral-no-behavior-deficit | partially_reproduced | Cell 16: no listed measure reaches p < 0.05, but attack measures cover only 3 control and 5 experimental mice. "Attack probability" is undefined. Read as attack bouts per unit time, it separates the groups completely: experimental mice attack more, p = 0.036. I computed this from cell 16's bout counts and interaction times; the notebook's `attack_bouts` gives the same p. |
| fig4ef-male-activity-slightly-lower | reproduced | Cell 17, unit-pooled reading: experimental activity is lower by both the Mann-Whitney test (p 0.0002–0.014) and the KS test (p ≤ 0.0012), for every baseline and window. The per-mouse reading fails (p 0.06–0.29). The claim rests on n = 4 vs 5 mice and on the assumed baseline. |
| fig4ef-female-activity-unchanged | blocked (data_missing) | There are no female-intruder data; I confirmed this in the archive. |
| figs4e-active-units-unchanged | partially_reproduced | Cell 18: no difference with the "all" and "gap10" baselines or on per-mouse means. With the 7 s baseline the pooled test gives p ≤ 0.0001, so the outcome depends on a reading the paper leaves open. |
| fig4g-male-selective-reduced | blocked (data_missing) | Selectivity needs female data. The male-activated fraction (≥ 2σ, male only) was testable but not reported. From cell 18 counts the pooled control fraction is 23–48%, outside 38.3 ± 3.83 under all six readings. |
| fig4g-female-selective-and-mixed-increased, fig4d, fig4c, figs7b, figs6f | blocked (data_missing) | Each needs female-intruder data, which the archive does not have. |
| fig5ac-behavior-activity-male-lower | blocked (data_missing) | The female half cannot be tested. The male half (cell 22) holds in the pooled reading (sniff p < 0.002, attack p ≤ 0.04) and fails per mouse. |
| figs5c-peth-activity | not_reproduced | The notebook calls it blocked, but cell 23 already decides it. The paper's test (nested Mann-Whitney) finds male sniff and attack not lower at p < 0.05 under any reading (p 0.11–0.79). The claim needs all four directions, so it fails whatever the female data show. |
| fig5bd-behavior-selective-units-reduced | partially_reproduced | Cell 19: under every reading, sniff-selective, attack-selective and active fractions are lower in experimental mice. At most 3 of the 7 values fall within tolerance (sniff_sel_e, active_c, active_e and mixed_reduction are always outside). |
| fig5e-cp-tuning-shift | blocked (data_missing) | The female-sniff values cannot be computed. The three male attack-versus-sniff values could have been, and were not run. |
| figs5e-behavior-decoding-intact | not_reproduced | Cell 20: control accuracy 0.99 vs experimental 0.93, p = 0.036 at all three C values. The paper puts chance at 50% (balanced frames). The notebook's bout-shuffled decoder scores 0.92–0.99, no lower than the real one (p 0.40 and 1.00), so the measure decodes bout identity, not behaviour (problem 3). |
| fig6-rslds-fit-quality | not_reproduced | Variance explained is 0.59 in every seed (range 0.50–0.66), against 85 ± 8.5%. Under the ≥ 90% reading, attack does not fall in one state in most mice (1–4 of 8). |
| fig6a-control-tau1-greater | not_reproduced | Control mean τ1 is 279–665 s (window 90–132 s) and τ2 274–488 s. Dunn's 1-vs-2 comparison gives p = 1.0 in every seed. |
| fig6c-experimental-tau-indistinguishable | not_reproduced | Experimental mean τ1 is 134–825 s, far above 55 s. Control > experimental τ1 at p < 0.01 holds in no seed. |
| fig6f-line-attractor-score | not_reproduced | Control mean score is 0.00–0.78 (expected 1.44–1.76), and no seed gives control > experimental. |
| fig6g-flow-field-line-vs-point | not_reproduced | At most 2 of 4 control mice score above 1, in any seed or reading. |
| fig6e-integration-dimension-persistence | blocked (metadata_insufficient) | The files do not mark when the intruder was removed. The last-bout variant (cell 14) does not support the claim: the experimental drop is significant only in seed 1, and the control drop never is. |
| fig7b-achw-first-dimension | not_reproduced | First-dimension experimental ACHW is 17.4–24.7 s (expected 9.86 ± 1 s), in every seed and units reading. |
| fig7c-achw-all-units | not_reproduced | Cell 21: reduction is 14.6–19.2% at 1–2 min (expected 50.9 ± 5.09%). The estimator is heavily biased over these short windows (problem 2). The whole-file variant gives 46.6%, inside tolerance. |

**B. Problems**

1. [affects a conclusion] Cell 23 / the claims table in cell 0: figs5c is marked blocked even though its testable male half fails the criterion. It should be not_reproduced.
2. [affects a conclusion] `vmh.achw` on 1–2 min windows: it removes the window mean and uses the biased autocorrelation. On synthetic AR(1) data with 600 frames, true ACHW 6.9 s comes out as 3.7 s and 20.8 s as 5.1 s. This compresses group differences: the true reduction of 67% appears as 27%. The estimator is the author's choice; the paper cites Remedios 2017 and gives no estimator. This may drive the fig7c outcome; fig7b, which uses whole-interaction traces, is less affected.
3. [affects a conclusion] `decode_attack_vs_sniff` (cell 20): stratified frame-wise folds put frames of the same bout in both training and test sets. The shuffled decoder therefore scores about 0.95 instead of the paper's 50% chance. The group difference then likely reflects unit count (control 109–225 units, experimental 31–127), and units were not subsampled to equal numbers. The criterion prescribes this scheme, so the outcome stands, but it is weak.
4. [affects a conclusion] Cell 16 (figs4a): "attack probability" was run under only one undeclared reading (`attack_pct`, the share of time attacking). A bout-rate reading gives p = 0.036.
5. [affects a conclusion] Male-only parts of three blocked claims were left untested: the male-activated fraction (fig4g-male) and the male choice-probability values (fig5e). For fig1e the outside atlas was not attempted even though the claims file marks its inputs as available.
6. [does not affect a conclusion] `fit_rslds` calls `fit` with ssm's default `alpha=0.5`. The linked ssm notebook (4-Recurrent-SLDS.ipynb at eb6c8aa, which I fetched) uses `alpha=0.0`, and the notebook does not state the difference. The ELBO change over the last 10 iterations is ≤ 0.1%, and τ values miss by several-fold, so this is unlikely to flip any rSLDS outcome. It is still an unstated departure from the cited code.
7. [does not affect a conclusion] Cell 13 (rSLDS): with a complex eigenvalue pair, columns 1 and 2 of `W` are identical. `argmax` then never assigns units to dimension 2, which is why the "largest" reading gives NaN for seed 0.
8. [does not affect a conclusion] `forward_sim_score` is computed in-sample on inferred latents, not on held-out neural activity as the criterion requires. This is stated.
9. [does not affect a conclusion] Cell 12 draws flow fields only for mice 510 and 500. The criterion asks for every mouse to be shown and described.
10. [does not affect a conclusion] Assumptions carried through without being checked:
    - The baseline is taken as the frames before the first annotated behaviour, and the window starts at that behaviour (stated).
    - Clock alignment is unestablished for mice 497, 510 and 500, which are kept anyway.
    - The files of 510 and 500 are described as GCaMP6m dF/F. The notebook calls that description wrong without evidence.
    - "The files hold only the male part" is asserted, not shown.
    - For mice 510 and 500, the reading-(a) state comes from sniffing frames, because they have no attack annotation.
11. Possible claims-file misreadings, reported and not corrected. Reading "~85% of variance" as the emissions R² is doubtful: 5 latents can hardly explain 85% of 31–225 z-scored units, and the notebook gets 0.59. The 85% may be a different measure, such as the cvR² the paper names. The claims file itself lists this reading as not settled.

**C. What I could not check, and the output that would have let me**

- **fig4g:** per-mouse male-activated fractions. Needed: the per-mouse counts behind cell 18.
- **fig5e:** the male attack-versus-sniff choice-probability fractions. Needed: those fractions under every combination of readings.
- **fig7c:** ACHW with an unbiased estimator (dividing by n − k) for the 1–2 min windows. Needed: that ACHW table.
- **figs5e:** a decoder with units subsampled to equal numbers across mice, and shuffled accuracy at each C. Needed: those accuracies.
- **figs4a:** the bout-rate reading of attack probability. Needed: its Mann-Whitney test.
- **rSLDS:** whether `alpha=0.0`, a sigma-normalized fit, or held-out cvR² would change anything. Needed: one seed fit with `alpha=0.0`, a sigma-normalized fit, and held-out cvR².
- **Mice 510 and 500:** whether they belong to this experiment. Needed: the `session_description` and keywords for each file.
- **fig4ef-male:** how sensitive the result is to dropping mice whose alignment is unestablished. Needed: cell 17 rerun without mice 497, 510 and 500.
