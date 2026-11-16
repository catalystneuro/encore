Both questions were right, and I changed the claims file for each. The quote check (`python tools/claims_check.py`) reports 0 problems. Nothing is committed.

1. **fig4b-spike-rate-difference: changed.** The paper says it analysed only bright folds ("We did not analyze dark corner-folds", Methods, Corners, paragraph 2). It also says Corners has "a matching set of dark and bright illusory corner-folds" (Results, paragraph 5). It states averaging of two midpoints only for Square and Star, and nowhere puts the S40 fold at the ROI centre. So I dropped both readings, and the criterion now takes the midpoint of the bright S40 fold alone. I made the same change in the opening comment, `fig4a-above-baseline` and `fig4b-pairwise-significance`. The expected values are unchanged.

2. **table1-s40: changed.** For the same reason, readings (i) and (ii) are dropped, and the criterion now uses the ten blocks along the bright S40 fold only. The expected values are unchanged.

Both questions are marked `answered: 2026-11-12`.
