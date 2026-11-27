I've revised the attempt for every point in the round-1 report and re-run the entry with `tools/entry.py all`. The check gives 0 errors and the notebook passes in 1214 s. Every conclusion and the record now match the new numbers. Nothing was committed.

**Outcome changes**
- **fig5b** (the long-pulse and ramp distance matrices line up): changed from partially reproduced to reproduced, as the verifier said. The criterion counts a claim as reproduced when it holds under any one allowed choice of method (a "reading"), and that is how I judged fig3a and fig4a. For fig5b I had judged only by the main reading, which was inconsistent.
  - It holds only on the suprathreshold long-pulse sweeps: 32 of 576 combinations, r 0.637 to 0.667 against 0.707 ± 0.071.
  - On those same sweeps the long-pulse loadings (fig2d), the Pvalb/Vip order (fig2e) and the centroid alignment (fig5a) all fail.
  - The verifier suggested a Mantel test, which allows for the 36 distances not being independent. It gives p = 0.0001 under the main readings, but 0.009 to 0.011 for the 32 combinations that hold. So under that test none of them reaches p < 0.001. I kept the Spearman test's own p, which is the one the paper prints, and the notes say so.
- **No other outcome changed.** The verifier agreed with the other 20.

**What I added or corrected**
1. **Shared driver lines (problem 1):** the balanced comparisons now use the lines each pair of protocols shares, as Methods 5 says. Brief response vs brief gain now uses all 11 lines (median 0.795); the 8 lines shared by all three protocols are kept as a variant (0.700). Both are outside 0.62 ± 0.062.
2. **Other readings in the balanced comparisons (problem 2):** fig5c and fig5d-f now also run the suprathreshold and "LP"-named long-pulse sweeps and the 14-feature ramp set, 42 settings in all.
   - fig5c: every median is positive, but no setting puts more than 3 of the 6 pairs within tolerance. It stays partially reproduced.
   - fig5d-f: all six pairs beat the shuffle null in 24 of 84 settings, including the main one. It stays reproduced.
3. **Readings that disagree between claims (problem 3):** a new notebook section, "Readings that hold together", applies one set of method choices to the long-pulse and ramp claims together. At most 5 of the 8 claims hold under any single set. None holds fig3a with fig3d in full, and none holds fig5b with fig2d, fig2e or fig5a. The notes of the affected claims say this.
4. **Fixed thresholds (problem 4) and mixed step lengths (problem 9):**
   - fig2a: I varied the depolarization threshold (10, 20, 30 mV), the high-spiking threshold (10, 20, 40 Hz), the current bins (two other sets), and spike counts per second (the steps last 0.5 s or 1 s). None of the 66 variants reproduces fig2a; PC2 stays between 18.8 and 26.1% against 15 ± 1.5.
   - fig4a: I added 1 ms and 5 ms fast-response windows. The same 6 of 48 readings match under each window, so the window changes no outcome.
5. **Figures (problem 5):** plots are now shown in the notebook (the scatter and density plots, and the null histograms for all six pairs). The silhouette is now described as measuring how much the lines overlap, not whether the cells form a continuum.
6. **"LP"-named sweeps (problem 6):** now included in fig5a (80 of 192 combinations hold) and fig5b.
7. **Shared-line count (problem 7):** now also taken from the data's own largest lines. It gives the same 8 lines.
8. **Long-pulse cell count (fig1c):** the per-cell table the verifier asked for shows that the cells with a usable long-pulse sweep (3276) and a usable ramp sweep (3275) are the same cells but one. No sweep-level quality-control rule here explains the paper's count of about 2270.
9. **Record:** the round is under `verifications`, with the verifier's reasons in its own words and my responses. I updated the notes, deviations, the fig5b and fig5c measured values, two findings about missing method details, the README and the notebook summary.

**Not done**
- I added no reader questions, because the verifier reported no place where the claims file misreads the paper.
- I could not find the cause of the long-pulse count gap from the data.
