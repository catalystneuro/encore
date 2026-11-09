The round-1 revision is done. `python tools/entry.py all` passes: the main notebook ran in 977 s and `ofc_simulations.ipynb` in 575 s. `check` reports 0 errors, and nothing is committed.

**Outcomes that changed**
- **fig5c-next-activity:** partially reproduced → reproduced. The paper's code settles which pairs an R² is scored on. It drops test pairs whose command at t or t-1 is above the 95th percentile (`generalization_plots.check_ix_lo`). It also scores the full model and every shuffle on exactly the left-out model's pairs (`plot_loo_r2_overall`). On those pairs all 8 R² values are within tolerance, and decoder-null dynamics beat the shuffle in 8 of 9 Monkey G sessions (G1 p = 0.007).
- **figs4g-generalize-condition-classes:** partially reproduced → reproduced. Monkey J's diagonal-1 failure came from comparing the class with shuffle R² on different pairs. With the shuffle on the same pairs, every class passes in 9 of 9 and 4 of 4 sessions.
- **monkey-j-linear-command:** not reproduced → blocked (`data_missing`). Its criterion says to block when the files hold neither the filter's update nor its parameters, and they hold neither. The verifier's readings are now shown:
  - Rewarded-trial frames with the offset column give 99.63, 99.63, 99.57 and 99.80% (the paper gives 99.6, 99.6, 99.5 and 99.8%).
  - Without the offset column they give 99.10 to 99.63%.
  - Neither is the criterion's test, because the cursor dynamics are fitted together with the map.
- **figs5f-nonlinear-no-better:** still blocked, but now as `not_runnable` instead of `too_large`. The `ssm` package (the code's commit and its only PyPI release) fails to build in the registry's locked install, because it needs Cython at build time without declaring it. A timing run outside the notebook put Monkey J at about 3 h of single-core compute and Monkey G at about 35 h; the notes record both.
- **fig4c, figs4b and fig5e:** outcomes kept, but no longer marked as resting on an assumption, since the code fixes the scored pairs. fig5e is still partially reproduced for a different reason: on the code's pairs every R² is within tolerance, but Monkey J's condition left-out model reaches only pooled p = 0.003 (the paper gives p < 0.001).

**Added or corrected**
- **Like-for-like shuffles:** under all three readings of the scored pairs, each R² is now compared with shuffle R² on the same pairs, and the full model is shown on each left-out model's pairs. This removes the invalid comparisons in problem 1.
- **figs6cd:** the code's pairwise command matching is now the main reading, regressing predicted on true distance as the code does. r is 0.586, 0.655, 0.650 and 0.766, with slopes 0.225 to 0.434 close to the paper's.
- **fig3e:** the fraction pooled over all items is now computed. It also gives 4 of 6 values within tolerance.
- **figs1d and figs1e:** a variant counts a tuple only when 15 or more occurrences remain after the edge occurrences are removed. Neither outcome changes.
- **figs3:** a variant fits the dynamics on rates in Hz. Every eigenvalue count is unchanged.
- **Monkey J Figure 6 simulations:** rerun with the summed 5 ms gain. fig6c and fig6g are unchanged. fig6d's absence then fails in Monkey J session 1 (Wilcoxon p = 0.0016). I kept fig6d as reproduced (on its assumption) because the fitted 100 ms update is the closer approximation of the decoder, and recorded this dependence in the notes.
- **Record:** I removed the `methods_unavailable` finding that asked which pairs are scored, since the code now answers it. Round 1 is recorded under `verifications`.

**Not changed, and why**
- **Problem 7:** each shuffle still permutes the whole session before the folds are split. The code does the same, and the deviations now say so.
- **Problems 8 and 10:** left as noted. The verifier marked both as not affecting a conclusion.
- **Questions file:** I added no reader questions, because the report found no place where the claims file misreads the paper.
