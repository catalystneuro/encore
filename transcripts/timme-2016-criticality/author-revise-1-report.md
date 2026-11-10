I ran the whole entry again with `python tools/entry.py all`. All three notebooks pass: 42 min for the culture notebook, 38 min for complexity and 11 min for the models. `entry.py check` reports 0 errors. The code changes from the earlier revision run, which was cut off before its full run finished, were already in the source; this run executed them, wrote the conclusions and updated the record. Nothing is committed.

**Changes in outcome**
- **fig7ab** (complexity and susceptibility peak in the model): blocked → not reproduced, as the verifier said (B2). The susceptibility rises at every step up to p_trans 0.3, under both readings, and never peaks. The complexity half was not computed.
- **fig7d** (branching ratio near 1): blocked → not reproduced. There is no susceptibility peak to compare against. B_new is closest to 1 at p_trans 0.28, which is within 0.0265 of the paper's 0.265.
- **fig10a** (complexity falls under randomization): partially reproduced → not reproduced, as the verifier gave it. Even with 100 subsets, shuffling raises complexity 78-fold, and the 1-bin jitter is not significant.
- **fig12a** (swapping preserves complexity): not reproduced → reproduced. With 100 subsets, swapping makes no significant difference (corrected p 0.836) and Pearson r is 0.775, which passes the 0.7 threshold. The record notes that it passes only narrowly and that the estimate is noisy (median coefficient of variation 0.78 across repeated draws).
- Every other outcome stays the same. The complexity claims fig5d, fig5e, fig5f, figs8, figs9 and fig12b were redone with the new settings. figs8 is now r 0.90 against the expected 0.23, and fig5f's relative difference is 0.151 against the 5% criterion. fig5f fails because the estimate's own spread across draws (up to 0.675) is larger than 5%.

**What I added or corrected**
- Complexity now uses 100 subsets per size, as Methods 2.9 give (B1). Even at 100, the toolbox's cut keeps a median of 10 of 90 subset sizes in the real data and 74 in shuffled data, so the instability the verifier found is not only due to 10 subsets.
- Outputs the verifier asked for:
  - repeated draws at 10 and 100 subsets on 10 recordings, with the number of subset sizes the cut keeps;
  - five draws on the Bethe raster;
  - for the model, mean avalanche size, B_basic and the one-step ratio against 4·p_trans (the one-step ratio is 0.937 at p_trans 0.25);
  - a log10 histogram of avalanche counts for fig2e. Its median is 10^4.92, so "around 10,000" fails as an order of magnitude too.
- I rewrote the conclusion cells, the summaries, the README, the notebook runtimes in `entry.yaml`, and the record's notes and deviations. I also updated the finding that asks the authors about the cut. Round 1 is recorded under `verifications`, with the verifier's reasons and my responses.

**What I did not do**
- **Fewer recordings for complexity.** It now runs on 40 of 435 recordings, down from 180. At 100 subsets, 40 recordings took 34 min, so more would break the 60-minute limit per notebook. This is recorded as a deviation.
- **figs2 reading (b)** is still blocked as too large. At 100 subsets, the 990 calls come to several hours of computing.
- **p_trans grid.** The 0.005 grid was not run. The fig6 and fig7c results sit at points the 0.005 grid also contains.
- **Smaller verifier points.** B5 (layout b on one recording), B6 (how the power-law fit handles gaps after the cuts) and B7 (exclusion) are answered in the record with no code change.
- **Reader questions.** The verifier reported no misreading of the claims file, so I added none.
