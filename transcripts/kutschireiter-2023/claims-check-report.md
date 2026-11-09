The checker passes: `claims/000289/10.1073-pnas.2210622120.yaml: 13 claims, 13 quotes, 0 statistical values, 0 problems`. The file is ready for an attempt (`ready: true`), with the open points below recorded under `checks`.

The paper is a theory and simulation paper. It has no imaging data and reports no statistical tests. The dataset belongs to a different study (Basnak et al.), so only the prediction claim points at it. I checked the code details in the criteria against the paper's repository (DrugowitschLab/BayesianRingAttractor, commit a9db6f9).

**Changes, by claim**
- **Header:** I added three code facts the criteria rely on:
  - `RNN_filter_Run` uses `z` but has no `z` parameter, so it fails (NameError) as released.
  - `Figure4g,h.ipynb` reads its information rates from an empty folder.
  - The Fig. 3C weight in the notebook differs from the Methods: it is scaled by 2/π, not 1/π, and assumes a 100-ms observation, not 10 ms.
- **fig1-conflict-decreases-certainty:** Comparison (a) included the certainty decay of the prediction step, and the observation strength was left to the analyst, which could change the outcome. Comparison (a) now tests the observation update alone (the vector addition of Fig. 1 D and E). The strengths are now the per-step values from the Methods for information rates of 1/s and 10/s.
- **fig2h-bump-tracks-circkf:** I stated the notebook's decoder scaling, (2/N)·A·r. The decay test compares the amplitude with the baseline κ* = 1, so the scale matters.
- **fig3c-update-weights:** The Methods' weight (1/π, 10-ms observation) and the notebook's (2/π, 100 ms) are now both readings, and I said how the observation strength is computed from the rate.
- **fig3f-retuning-reduces-drop:** Which noise level and normalization the 35% refers to are readings of one reported number. The protocol says such a number counts as reproduced if it matches under any reading; the criterion had required all of them, and now requires any.
- **noise-effects-on-mu-and-kappa:** The criterion now says the code fix the run needs (adding `z=None`). It also states the network weights and sets the angular-velocity correction term to 0, since there is no angular-velocity input.
- **fig4gh-drosophila-network-matches:** The reference is now the Bayesian attractor results stored in the same file (same runs, time step 0.001), and the rates come from the scan script.

**Open**
- **Thresholds for vague words:** Several criteria judge words like "similar", "close", "indistinguishable", "mostly" and "broad" with cut-offs the paper does not give. They are named as readings, but an outcome that depends on them rests on the claim writer's bounds.
- **fig3b:** The criterion requires the Bayesian attractor to be at least as accurate at all 23 rates. At the two highest rates both models are near 1 and were run on different trajectories, so sampling noise alone could make the difference slightly negative.
- **prediction-bump-amplitude-cue-reliability:** The paper gives no experimental method. The test readings (a per-fly majority, or a one-sided Wilcoxon test over flies) and the choice of signal are the claim writer's, named as such.

Every main finding has a claim, and all claims come from this paper and its code. I did not commit anything.
