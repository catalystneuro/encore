No outcomes changed. The verifier agreed with all 25 (10 reproduced, 10 partially reproduced, 4 not reproduced, 1 blocked), so this round fixed the nine problems it raised and added the outputs it asked for. The entry passes `tools/entry.py all` (387 s, 6.3 min inside the notebook, peak memory 0.41 GB), and every number quoted in the conclusions and the record is in this run's output.

**The verifier's nine problems**
1. **Bootstrap mode (ms-cells-proportion):** the paper's MATLAB code calls `bootstrapMeanEqualTest(countOld,countNew,B)` with only three arguments (NWB_singleCellAnalysis_release.m line 102, commit 1d95162). That means two-sided with no variance correction, which is what the helper already did. The helper and notebook now cite this. I also added the studentized version as a variant: it gives 92 MS cells (126 under the code's choices), even further from 146, so not_reproduced stands.
2. **Spread of the correct-trials variant:** the MS conclusion now gives it, 132 to 147 over the five seeds and within tolerance with every seed.
3. **Shuffled null:** the MS conclusion now says the main count is 1.55 points above the null (110 units against 81).
4. **Spike-time text:** the data check said spikes start and end with the task. It now gives the real spans (up to 2462 s before the first trial and 2055 s after the last).
5. **Label-coding test:** the conclusion now gives the strict count (78 of 87). It also says the eight short sessions show "old" images whose encoding trials are not in the file.
6. **z-ROC slopes:** sessions with all five hit rates equal get a slope of exactly 0. There are 4; 3 were already dropped. Dropping the fourth (CS24_59) too gives p = 6.6e-9, so the result holds.
7. **IsolationDist read as IsolDist:** no change; this was already stated as an assumption.
8. **Meaningless AUC variant:** removed from the notebook and the record.
9. **fig5f possible misreading:** the paper's text compares "the existing and new dataset", while the claim compares the two sites. I left the claim alone and added a question for a reader in `questions/chandravadia-2020.yaml`. The text's grouping now runs as a variant: no Fisher test finds a difference (p = 0.87, 0.52, 0.70).

**Outputs the verifier said it could not check**
- **Impedance:** `imp` is stored as float64 with the values written as NaN, and NaN is its only value in any file. So impedance is absent, not stored as a placeholder code.
- **Image identity:** the notebook now hashes the pixels of every stimulus image (about 4 minutes of the run). In all 87 files, images and file names match one to one, and the pixel test gives the same fractions as the file-name test.
- **H48:** only session 99 (30 units) is in the dandiset. Faraut et al. (2018) give no neuron count per session, so the missing session 98 can't be checked.
- **The 37-neuron gap (1539 against 1576):** split by brain area against Faraut et al.'s Table 3, it is mostly in the amygdala (913 against 943; hippocampus 626 against 633).

**Record:** I updated the notes on the affected outcomes, one deviation, two findings, the README and `runtime_minutes` (now 6). Round 1 is recorded under `verifications`, with the verifier's reasons and my responses.

**Not done:** I could not say which sessions the 37-neuron gap comes from, because the earlier release gives no per-session counts. I committed nothing, as instructed.
