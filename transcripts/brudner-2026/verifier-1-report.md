**Verifier report, brudner-2026, round 1 (DANDI:001871 @ 0.260630.1657)**

The claims file has 22 claims. The notebook tests 6, treats 16 as blocked, and its own table covers all 22.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| fig5e-cue-betas | not_reproduced | The criterion counts a claim as reproduced only if every reading gives that result; here the result depends on the reading. With the SI onset (`rule20`) and smoke-2a, both plumes pass with stored or pooled z-scored signals. Per-trajectory z-scoring fails both plumes: smooth motion p = 0.0066, complex motion p = 0.098 and 0.204 (cell 11). Under the code's readings the complex coefficients have the wrong sign and are out of tolerance (motion −0.0119 against +0.0441 ± 0.0159; cell 12). |
| fig5f-cue-dominance | reproduced | One reading gives both values within tolerance with the right signs: `rule20`, smoke-2a, heading 150–210, z none or pooled gives smooth 0.935 and complex −0.715 (cell 14). smoke-1a with the event start and heading 160–200 also gives 0.879 / −0.701. The result is fragile: under the code's readings the complex value is +0.388. |
| figs5c-turn-angles | reproduced (rests on an added reading) | With the files' event bounds, both readings in the claims file give medians of about ±21°, outside tolerance. Only the notebook's own turn bounds (20% crossings on the rising and falling edges) give −35.0 / +35.9, or −33.1 / +36.6 for the kept turns (cell 16). That rule has a bug (problem 2). |
| fig2c-complex-auc | partially_reproduced | Motion AUC is above gradient AUC under every reading. Under the two samplings the claims file names, the sum AUC is 0.63–0.67, which fails the sum condition. Only the added mirror sampling gives a sum AUC of 0.500. The values miss under every reading: motion 0.602 against 0.618 ± 0.005, gradient 0.554–0.560 against 0.537 ± 0.012 (cell 25). |
| fig2e-complex-weights | partially_reproduced | \|motion\| (0.415–0.424) is larger than \|gradient\| under every reading. The gradient weight (0.234–0.271) is outside 0.098 ± 0.041 under every reading (cell 25). |
| figs1fg-resolution-robustness | not_reproduced | Gradient r at 12 px is 0.613 without smoothing (0.809 with σ 1.5 smoothing, a variant). Motion r at a 4-frame delay is 0.73–0.82 against the required ≥0.8 at every spacing (0.729 at 3 px in both forms). The drop at 8 and 15 frames does hold (cell 21). |
| figs2c-one-frame-delay | blocked (data_missing) | The smooth plume was not read. The complex half holds: AUC at τ = 1 is 0.603, at τ = 15 is 0.505, and τ = 1 is the highest (cell 28). |
| methods-intensity-right-bias | blocked (metadata_insufficient) | The files do not say whether turn direction −1 is left or right. Both conditional outcomes can be stated from cell 11: the smooth intensity coefficient is −0.050 with p < 1e-4, and complex smoke-2a is n.s. So the claim holds if −1 is a right turn and fails if not. The notebook did not state this. |
| fig1eh-snapshot-organization, fig1il-zscore-reliability | blocked (data_missing) | Both need the smooth plume, which is on Dryad and was not staged. |
| figs1-antisymmetry-index, figs1-temporal-statistics | blocked (data_missing) only for the smooth comparison | The archive's dandiset description says the compact asset `sub-figs1-freestream-plumes…behavior.nwb` (57 MB) holds the mean gradient and motion maps and the exact plotted frequency/intermittency points for 5, 10 and 20 cm/s. The three freestream movies and the complex movie are also deposited. The freestream ordering and the "complex highest" parts could therefore be tested; the notebook did not test them. |
| fig2b-smooth-auc, fig2d-smooth-weights | blocked (data_missing) | Both are smooth-plume only. |
| fig3bc, fig3d, fig3e, fig3ij, fig4ef, discussion-ten-percent-gain, figs4, figs5fh | blocked (data_missing) | Each needs the smooth plume or a network trained on it. Some complex-only parts are testable in principle from the deposited movie: the complex MNM filter and its AUC of 0.517, and complex wind-only against complex-trained agents. The agent code is not in the paper's repository. |

### B. Problems

1. **[affects a conclusion]** The choice of complex file set (cells 10–14) is doubtful. The notebook takes smoke-2a as the main set because the claims file says the code selects it. But the archive's own dandiset description says smoke_1a_orig "was analyzed throughout the paper". smoke-1a with the event start and heading 160–200 reproduces the published Fig. 5E coefficients almost exactly: gradient 0.0174 against 0.0185, motion 0.0456 against 0.0441, motion p = 0.0059. smoke-2a gives motion coefficients of the opposite sign. Pooling the two sets passes 0 of 24 readings. Together these suggest the two sets differ in a sign or flip convention. This decides the fig5e and fig5f outcomes, and the notebook neither flags nor investigates it.
2. **[affects a conclusion]** `plumes.onset_20pct` scans runs of |dtheta| ≥ 20% of the peak, ignoring the sign of the rotation. A synthetic test showed the run crossing into an adjacent opposite-direction turn: the onset moved from frame 12 to frame 5, and the integral became −10° instead of +25°. The onset lead reaches 127 frames in cell 7, which is consistent with this. The bug affects every `rule20` reading of fig5e and fig5f, and the SI-bounded integral of figs5c. The rule should scan signed rotation in the turn's direction.
3. **[affects a conclusion]** fig2c passes its sum condition only under the added mirror sampling (`plumes.draw_samples`, "mirror"). The assumption is reasonable: the paper reports a sum AUC of 0.5 with SD 0 and a sum weight of 0 "as expected". But it is the author's own reading. Under the claims file's readings, fig2c is not_reproduced.
4. **[affects a conclusion]** In cell 21, the σ 1.5 smoothing variant was run for the gradient only, not for motion. Smoothing lifts the gradient r at 12 px from 0.61 to 0.81, so the figs1fg gradient part depends on this unstated choice. The motion part was not tried under the same variant.
5. **[affects a conclusion]** figs1-antisymmetry-index and figs1-temporal-statistics are declared wholly blocked. Their freestream and complex parts can be tested from deposited assets (see table A).
6. **[affects a conclusion]** methods-intensity-right-bias: the notebook does not report the outcome under each left/right mapping, although its cell 11 numbers settle it once the mapping is fixed.
7. **[does not affect a conclusion]** The movie is a background-subtracted preprocessing ("bgsub_gauss3…", cell 19), and the mean-map maximum is at row 571, not the centerline row 590. Either may explain the Fig. 2 value misses. The notebook notes the first, but does not test either.
8. **[does not affect a conclusion]** In `draw_samples` "random" and "mirror", 3 M draws with replacement come from about 1.47 M windows, so many test windows also appear in training. "location" sampling avoids this and gives the same AUCs.
9. **[does not affect a conclusion]** In `movie_pass1`, "grad_dt" uses a backward temporal difference, where Fig. 1 uses a centered one.
10. **[does not affect a conclusion]** In `keep`, heading is taken at onset − 50 ms, while position uses turn_x/turn_y at the event start.
11. **[does not affect a conclusion]** The margin readings are identical to no margin. I checked this against the percentiles in cell 5: the x/y region filters already lie inside the 15 mm margin, so the margin removes nothing. This is correct behaviour.
12. **[does not affect a conclusion]** Cell 26 still contains the author's "Result" conclusions. I formed my outcomes from the outputs alone.

### C. What I could not check

- **The paper's code repository.** I could not see `filter_published_turns` (heading column `theta` or `theta_smooth`, which complex substring it selects) or the published Fig. 5 tables' turn counts. An output comparing the kept-turn counts per group with the published `fig5e_*.csv` row counts would settle problem 1.
- **Why smoke-1a and smoke-2a differ in sign.** Output needed: session descriptions and vflip counts per group, and the motion coefficient fitted separately for vflip0 and vflip1 trials.
- **How many turns problem 2 affects.** Output needed: the fraction of turns whose 20% run contains a sign change of dtheta, and fig5e, fig5f and figs5c re-run with a signed onset rule.
- **figs1fg under smoothing.** Output needed: the motion map correlations with σ 1.5 smoothing.
- **The figs1 freestream parts.** Output needed: the index, frequency and intermittency medians from the compact freestream asset and the complex movie.
- **Smooth-plume access.** I did not verify the notebook's statement that Dryad returns 401 without a token. I did confirm through the DANDI API (136 assets and the dandiset description) that the smooth plume is not in the dandiset.

I tested the helpers on synthetic inputs in a temporary environment. `exp_smooth` and its fast version agree exactly, `_pair` aligns correctly, the motion feature has the expected sign, and mirror sampling balances the labels. The only failure found was the `onset_20pct` bug in problem 2.
