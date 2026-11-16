I've worked through the round-1 report and re-run the entry with `python tools/entry.py all entries/zandvakili-2015`. Checks give 0 errors and the notebook passes in 26 minutes; it now does more work, so `runtime_minutes` is 27. Nothing is committed.

**Outcome changes.** I took the verifier's outcome on all three claims where it disagreed:
- **fig5b-v1v2-latency**: partially reproduced → not reproduced. The criterion needs the median offset within 2.8 ± 0.28 ms and it is 2.0 ms. The criterion has no partial outcome.
- **fig5b-intra-areal-zero-lag**: not reproduced → partially reproduced, still resting on the assumed Wilcoxon test. Both medians are 0.0 ms. V2-V2 holds under both tests, and V1-V1 fails only under Wilcoxon (p = 0.016, mean shift 0.10 ms). That shift follows the order of the unit lists, so it is not one population leading the other.
- **fig7a-threefold**: partially reproduced → not reproduced. The ratio is about 1.9 against 3 ± 1 under every reading that can be formed. The one value at the edge of the range (median 2.011) comes from a single 3 ms bin standing in for reading e-b, which can't be formed at 1 ms resolution.
- **The four simulation claims**: still blocked, but the reason changes from `not_runnable` to `other`, because they were simply not attempted.

**Added or corrected:**
- **Null check of the bootstrap p-values (point 2).** Two independent control-epoch sets were compared with each other.
  - The paired reading p-a gives p < 0.05 at 13 of 150 epochs, against about 7.5 expected, and none pass Bonferroni. It is close to its stated level, so its results can be read.
  - The independent reading p-b gives 0 of 150, so it is conservative.
  - This doesn't change fig6b or fig7d.
- **fig7d and figs4 under every reading (point 6).**
  - fig7d: the peak is 2.5 to 3.5 ms before the V2 spike in every reading, and every reading still has significant epochs after the spike or far before it, so it stays partially reproduced.
  - figs4: the ratio is larger with a V1 partner at all five windows in every reading, so it stays reproduced.
  - fig7d keeps 2000 draws, and the reason is now stated.
- **Epoch counting in fig7d (point 7).** An epoch now counts as "after" only if it lies wholly after the spike. Epochs that include the simultaneous bin are counted separately.
- **Four more shuffle realizations (point 8).** At 5 ms with trials shuffled within orientation, one realization of five goes above the control bound, in both epoch readings. The mean of the five stays below it, so fig7a-above-shuffle stays reproduced, and the notes now say the margin there is fragile.
- **RF row mapping check (point 10).** Only 2 of 564 V1 units fall on a row with no fit. The drop in coupling with RF offset (0.0121) is larger than in all 200 random permutations of the rows (largest 0.0119).
- **Data check.** It now prints the fields of each file (only spikeRasters, stim, trialId, unitCodes, rfInfo) and the sort codes. The sort codes number units per electrode and don't mark single units.
- **Per-session site fractions (point 11).** The excess over the paper's fraction appears in every session, so no single session accounts for it.
- **1 ms resolution notes (points 4 and 5).**
  - Binning widens the 1.5 to 3.5 ms epoch to about 1 to 4 ms.
  - Smoothing a single bin already gives a 3.54 ms wide peak.
  - "Offset above 1 ms" means 2 ms or more.
- **Record and README.** The record has the round-1 `verifications` entry with the verifier's reasons and my responses. Point 9 (the spike's own trial in the jitter pool) was already stated and is unchanged. The bootstrap question to the paper's authors now includes the null-check result. The helper's histograms reproduce the earlier ones exactly, so no earlier number moved.

**Not done:**
- The simulations were not run.
- No question was added to `questions/zandvakili-2015.yaml`, because the verifier reported no place where the claims file misreads the paper.
- I didn't look into why the narrow-peak fractions are higher than the paper's beyond the per-session breakdown; without depths the data can't say more.
