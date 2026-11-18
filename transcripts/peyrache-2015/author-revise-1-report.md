I've revised the attempt for every point in the verifier's round-1 report, re-run both notebooks from a clean environment, and recorded the round under `verifications`. Both notebooks pass `python tools/entry.py all` with 0 errors, in 21.0 and 21.1 minutes. Nothing is committed.

**Outcome changes.** Of 35 claims, 34 are now tested: 22 reproduced, 7 partially reproduced, 5 not reproduced, 1 blocked.
- **recording-sample**: reproduced → partially reproduced, as the verifier said. The data give 7 mice and 41 sessions, both within tolerance. By the units' own labels, though, 24 sessions in 4 mice hold both structures, against 21 in 3. Mouse20's PoS units sit on electrode groups the lab labelled 'postsub', on a device the files call the post-subicular probe. I now follow the files' labels everywhere, which also fixes the inconsistency the verifier found between cells.
- **ensemble-sizes**: not reproduced → partially reproduced. Under the second HD-cell reading (hd-b), both means are within tolerance (ADn 8.00, PoS 5.22) and both s.d.s are not (4.42, 4.11). The PoS mean depends on counting Mouse20's 3 PoS sessions: without them it is 6.00, outside.
- **fig5d-adn-predicts-pos-reliably** and **fig5e-adn-predicts-pos**: blocked → reproduced. The GLM now runs in its own notebook, `glm_peyrache_2015.ipynb`, with 7 readout windows and the first 20 minutes of each state.
  - ADn assemblies predict PoS cells in every state (Wilcoxon p 2.7e-18 to 9.2e-22).
  - The reverse prediction is weaker in every state (p 0.0095, 6.3e-11, 0.020), with the gap largest in SWS.
- **fig5e-readout-windows** stays blocked as too large. Its criterion needs about 23 windows, roughly 70 minutes against the 60-minute limit.
- **fig2e-decoded-speed**: I kept partially reproduced and recorded the verifier's not reproduced as a disagreement. I now locate the decoded angle below the 1-degree grid, so the 10 ms reading can be tested (ADn SWS/wake ratio 5.11, still not 10). The REM part does hold in the PoS ensembles (0.93 and 1.00), which the criterion counts as partial; the verifier's reasons cite ADn only.

**Fixes and added outputs**
- **OLE (fig4d,e)**: the verifier called my signal estimator my own assumption. I now use the plain reading, with Q taken entirely from the tuning curves, and keep my earlier version as a variant. Both readings give not reproduced:
  - fig4d: the covariance estimator wins in all 5 PoS ensembles, but 5 ensembles cannot reach p < 0.05 (the floor is 0.0625), and its error is 1.26 times the Bayesian decoder's, beyond the 25% margin.
  - fig4e: the ADn ratio is 0.25, not 0.5 or 0.67.
- **fig3b**: added a shuffled-angle control. It shows the 0.05 threshold cannot fail with random references, or with actual-HD references and the mean summary. The outcome now rests on the decoded-HD references with the median summary, where the control gives 0.000 in ADn.
- **supfig5**: the rate groups now use the right peak rate and the rates of the state tested. It is still not reproduced, now in 0 of 96 readings.
- **fig7**: connections now run on every session with both structures, including Mouse28-140314, for 4765 pairs. That is every such pair the dandiset holds, so the paper's 6960 cannot be reached. Pairs per session are printed.
- **Other outputs added**:
  - the scored wake interval coincides with the open-field epoch (overlap 0.9998 to 1);
  - speed-fit quality and pairs at the grid ends, per state;
  - pairs with a zero or infinite speed are left out before the tests;
  - Mouse32's count is reported as untestable, not as a miss;
  - the non-monotonic fall in fig6b is noted;
  - the two borderline results (adn-pos-hd-information, fig7e-driven-pos-hd-information) are described as marginal or fragile.

**Not done**
- I did not decode ensembles under hd-b. The verifier said it would not change a conclusion and it would cost a large share of the run; I print how many sessions would qualify (27 ADn, 11 PoS).
- The GLM covers only the readings where assemblies and targets are HD cells; the all-cell readings were not run, for time.
- I added no reader questions, as the verifier reported no misreading of the claims file. No claim was changed.

Files changed:
- `entries/peyrache-2015/hd.py`
- `entries/peyrache-2015/reproduce_peyrache_2015.ipynb`
- `entries/peyrache-2015/glm_peyrache_2015.ipynb` (new)
- `entries/peyrache-2015/entry.yaml`
- `entries/peyrache-2015/README.md`
- `attempts/peyrache-2015-02.yaml`
