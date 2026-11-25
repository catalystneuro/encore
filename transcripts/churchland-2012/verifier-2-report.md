**Verifier report, round 2: Churchland et al. 2012 on DANDI:000070 (0.261122.2046)**

The claims file has 22 claims. The attempt record has 22 outcomes:
- 5 reproduced: fig3ef, fig6a, fig6b, rotation-frequency, suppfig5-m1-faster
- 6 partially reproduced: composition, curvature, phase, planes-range, shuffles, velocity model
- 5 not reproduced: var-captured, pc23, suppfig4-j-array, suppfig5-areas, complex model
- 6 blocked (data_missing)

Seven outcomes carry `assumed: true`.

**1. Outcomes**

I agree with all 22 stated outcomes. Every `assumed: true` outcome states its assumption in its deviations.

- **Onset column** (curvature, var-captured, pc23, rotation-frequency, shuffles): the assumption is stated and is now well supported. Cell 6 prints both descriptions ("calculated offline using a robust algorithm" against just "movement onset time"). It also shows median hand speed of 43 and 15 mm/s at the offline onset, against 137 and 160 mm/s at `move_begins_time`, so the hand is already moving at the latter.
- **fig6-velocity-model** (now partially_reproduced): I agree under the stated assumptions, with two cautions.
  - The main reading of the preparatory term was changed after round 1, and the change flipped the outcome from not_reproduced. The record says so openly. The new `prep="lead"` reading, where preparatory activity falls from −150 to −50 ms in `reach.py`, is no less reasonable than the old one; the paper says nothing about its time course.
  - The J-array pass is thin. Its 6-D ratio is 0.517–0.590 against a 0.6 limit, and its angle peak is 0.472π with a plane ratio of 0.909, which looks rotation-like (cell 53).
- **fig6-complex-kinematic-model:** agreed. It is not reproduced under all five seeds of the main reading (cell 55).

**2. Sentences the outputs do not support**

- **Cell 56 and the record's fig6-complex-kinematic-model notes:** "The other readings give not reproduced, except no lead with the falling preparatory term, which gives partially reproduced under every seed." In cell 55, the reading with no lead and a persisting term gives partially reproduced for 3 of the 5 seeds (`['not', 'not', 'partially', 'partially', 'partially']`). The sentence holds for seed 0 only.
- **Record, methods_unavailable finding on the model:** "with no lead near 0 in both, as in Figure 6a." With no lead and a persisting term, the peaks are 0.250π and 0.361π (cell 53). Only the falling term gives peaks near 0 (−0.083π and 0.083π).
- **Record, suppfig5-m1-faster notes:** "here M1 is 1.5 to 2.4 times faster." That holds under the main reading (1.53 and 2.39). Under the other readings N-array is 1.41× (1.491/1.058) and 1.42× (1.528/1.076) (cell 50). This is minor.
- **README:** "It takes about sixteen minutes." Cell 58 prints 19.7 min.
- **Record, fig6-velocity-model notes:** "The stricter reading … changes only the no-lead reading." There are two no-lead readings, and only the one with the falling term changes (cell 53). This is ambiguous rather than wrong.

Every other number in the "Result" cells, the Summary (cell 57), the README table and the record's notes matches the printed outputs. The record's verification entry states my round-1 reasons faithfully, in my own terms. It correctly says I agreed with 21 of 22 and disagreed on the complex model. Problems 7, 8 and 9 are folded into the relevant reasons and the `reviewed` field.

**3. Round-1 points**

Resolved:
- **Problem 1** (the unwrapped peak test): `sim_ok` now tests |peak| < π/4, and the stricter 0 ≤ peak < π/4 is also shown.
- **Problem 7:** the hand paths are now aligned on the same onset column as the neural data (cell 19).
- **Problem 8:** the dead polarity check is gone; `reach.py:347` only sets `v2` as the conjugate.
- **Problem 9:** aligned on target onset, M1 lags PMd by 9 ms in N-array, with half-rise times of 99 and 101 ms. The go-cue lag is 60 ms (cell 8). A fixed clock offset between the arrays is not supported.
- **Problem 5:** the column descriptions and the hand-speed evidence are now printed.
- The other outputs I asked for (non-counter-clockwise conditions, model histograms, seeds) are also printed.

Remaining, and bearing on a conclusion:
- **Onset column:** it still decides 5 outcomes. The assumption is reasonable, but those outcomes are conditional on it.
- **Problem 2** (phase test against the shuffle-3 reference): referred to a reader, with the criterion unchanged. The two new variants point opposite ways. Projected onto the original plane, the claim would be reproduced; predicting from the dividing point, it would be not reproduced (cell 22). The partial outcome rests on a reference that does not test the claim.
- **Problem 3** (rotation strength measured by R2(M_skew) for shuffles 2 and 3): referred to a reader. N-array fails exactly on the shuffles the Supp. Fig. 2 legend says should not remove all structure.
- **Problem 4:** the velocity-model outcome remains decided by modelling choices, now including a main reading chosen after round 1.
- **Problem 6** ("20–35%" taken from the per-area legend): referred to a reader. It does not decide the main reading, but it is the only route by which the `move_begins_time` readings pass.

**4. Critical findings**

No finding in the attempt record is rated `critical`, and I see none that should be. On the other ratings:
- **Finding 3** (two sessions missing the condition columns): I would rate it minor, not major. The paper does not use those sessions, and no main analysis is blocked.
- **Finding 4** (the two onset columns): I would rate it major, not minor. Nothing in the files settles which column is the paper's onset, and the choice changes five outcomes (cells 20, 25, 28, 42, 45).
