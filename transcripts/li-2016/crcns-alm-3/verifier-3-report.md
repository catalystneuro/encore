**Verifier report, round 3: Li et al. 2016 (doi:10.1038/nature17643) on CRCNS alm-3**

The attempt record has one proposed change of outcome, on fig6-modular-models-robust (record lines 497 to 524). No other claim has a `proposed` entry. Cell numbers count from 0 in the re-executed notebook.

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| fig6-modular-models-robust | not_reproduced | Yes | — | See below. |

**Reason for fig6-modular-models-robust**

1. **The numbers come from the simulation.** In cell 90, `models.run_integrator` simulates the modular integrator. Its matrix (`models.py`, `INTEGRATOR_W`) matches the 8 x 8 matrix printed in the paper's Methods, row by row. The other parameters also match the Methods: tau 10 ms, inputs ±0.04, tonic 40 on the integrator neurons, linear synapses with rates kept positive, and no noise. Module 1 (neurons 1 to 4) is held at zero for 0.2 s < t < 1.0 s, as the criterion says. Cell 90 prints these results:
   - Lick-right trials: the selectivity returns to 13.619 against 14.401 unperturbed, which is within 10%.
   - Lick-left trials: it reaches only -7.200 against -14.400, and the cell marks it as not recovered.
   - The result is the same in every run, because the integrator has no noise. One run per trial type therefore stands for all 100 runs. The integrator recovers in 50% of runs, and the criterion needs 90%.
   - The failure on lick-left trials follows from the printed matrix. The recovery neuron gets positive input from the right-preferring neuron and negative input from the left-preferring one, and its rate cannot go below zero. So it can only restore right-preferring activity. This is a property of the matrix as printed, not a coding error.

2. **No choice behind the outcome was made to reach the result.** The outcome turns on the integrator, and the integrator part uses no free choice: no noise reading, and the matrix exactly as printed. The attractor choices affect only the attractor part, which passes and does not drive the outcome. Those choices are the per-step noise reading, partners that share a preference, and the bilateral run extended to 4 s, which is now listed as a deviation. Cell 90 shows the attractor results:
   - Unilateral recovery in 100% and 98% of runs.
   - After bilateral silencing run to 4 s, all runs settle, at the wrong fixed point in 47% and 55% of runs, within 25% to 75%.
   - Under the second noise reading the unperturbed attractor already ends at the wrong fixed point in 45% to 49% of runs. Set against the per-step reading, this supports the per-step choice as the working model.

3. **The criterion is applied as written.** It says "for the attractor and integrator", and it has no partial rule. The FORCE network only has to be reported, so not simulating it does not affect the outcome. One part fails, so the result is not reproduced. This applies the same rule the record used for ed2e, ed7e and ed10e in round 1, and it matches my disagreement in round 2.
   - Cell 91's conclusion states the same numbers and the same reasoning.
   - Whether the printed matrix lacks the gating neurons of Fig. 6c is a question about the paper's methods. It belongs in the methods_unavailable finding, where it stays, and it does not make the outcome partial.

**Reading of the paper:** I found no place where the claims file misreads the paper for this claim. Its parameters match the Methods text in `paper/`.
