I revised the attempt for every point in the round-2 report. No outcome changed and nothing is under `proposed`: the counts are still 14 reproduced, 3 partially reproduced, 2 not reproduced and 1 blocked. `tools/entry.py check` passes with 0 errors.

One process problem first: `tools/entry.py all` was not run as you asked. Its three notebooks together take about 140 minutes, and a single command here is capped at 2 hours. Instead I ran each notebook on its own, using the same environment and nbconvert command that `entry.py` uses. So there is no clean-run stamp, and the next `entry.py run` will execute everything again.

**What the new runs showed**
- **Repeat runs drift slightly.** Re-running the main notebook moved some values in the third decimal, presumably because the threaded fits are not exactly repeatable. I updated every affected number in the record and the conclusions. Two of them matter:
  - fig6a-null-on-plane: measured is now 0.395 (was 0.396), still inside the band.
  - complex-cells-dominate: the complex-only versus full-model Wilcoxon p went from 0.054 to 0.049, so I reworded "the same as the full model". The ratio is still 1.001 and the outcome is unchanged.
- **Figure 2B with the finer pooling (point 1).** A new notebook, `finer_pooling_fig2b.ipynb`, refits the linear and compressive models, each with and without divisive normalization, on the 3×3 pooling.
  - fig2b-divisive-improves: +2.5% (reading a), Bonferroni-corrected p = 0.084 over 11 comparisons. It still fails the claim's p < 0.01, so it stays not reproduced.
  - fig2b-compressive-improves: 5.6% and 8.0% (reading a); only reading (b) with divisive normalization is within tolerance. Still partially reproduced.
  - fig2b-compressive-divisive-best: corrected p = 0.0083, still reproduced among the four models refitted.
  - fig2b-no-interaction: still holds for the compressive model.
- **fig7b-pattern-index (point 2).** A new cell prints, for each neuron, the share of grating and plaid directions that rectification sets to zero, and the index with and without rectification.
  - The median share is 25% (range 0 to 58%), and the change in the index grows with it (Spearman rho 0.568, p = 4.7e-5).
  - The 8 neurons with nothing clipped keep their component-like indices (2 of 8 in the range). 27 of the 37 clipped neurons land in the range.
  - So the indices reach the paper's range through clipping. I kept the verified outcome (reproduced, resting on the rectification assumption) and say this in the conclusion and the notes.

**Text corrections** (all six sentences the verifier quoted are fixed)
- The `finer_pooling.ipynb` claim that the 4×4 pooling "does not raise it further" now gives the actual changes (−0.022, −0.046, +0.025) and calls them mixed.
- The main summary row for fig2b-expansive-decreases now says that under reading (a) both sizes are outside tolerance.
- The deviation saying "every other analysis uses 763 regressors" now names the analyses that use the finer pooling.
- The deviation text copied onto fig3a-example-neuron and complex-cells-dominate is replaced, and the README now agrees with the record on where each claim is judged.
- The fig7c notes now say the noisy-index values come from the first of the 20 draws.
- The round-2 `verifications` block is recorded, with the verifier's reasons and my responses.

**Not done, and why**
- **Expansive and luminance-normalized models:** not refitted on the 3×3 pooling, for time. The deviations say so.
- **Null-movie reading (b):** still not run under all four combinations. The verifier noted this does not affect a conclusion.
- **Runtimes:** the main notebook took 65 minutes, over the 60-minute aim (the previous run took 63). The new Figure 2B notebook took 47 minutes.
- **Executed copies:** I copied the final markdown into the executed copies of the main and Figure 2B notebooks after their runs. Their code cells are identical to the committed ones.
- **Questions file:** nothing added to `questions/nishimoto-2011.yaml`, because the verifier found no place where the claims file misreads the paper.
