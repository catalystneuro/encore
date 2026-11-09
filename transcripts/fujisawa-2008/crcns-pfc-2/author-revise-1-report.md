I finished the round-1 revision and recorded it. Five outcomes changed, and the final run of `python tools/entry.py all` passed with 0 errors in 1,320 s. The record now has 5 reproduced, 8 partially reproduced and 17 not reproduced; nothing is left blocked.

**Outcome changes**
- **unit-count**: reproduced → partially_reproduced, as the verifier argued. 627 cells matches 633, but over three of the four rats, and the files keep a selection of the cells. Their rates fit the data description's 1 Hz rule without showing it.
- **task-performance**: blocked → partially_reproduced. The EE.188 archive holds the nose-poke sensor channels (97, 98), which match the trial table to within 1.6 ms. Together with the position file they give 45 of 46 correct trials (97.8%). Only this one session of 13 is tested.
- **trajectory-divergence**: not_reproduced → partially_reproduced. The new path plot shows the stem runs along x, so the side-to-side coordinate is y. With y the path diverges at 0.28 (target 0.30). Head direction still diverges at 0.01 (target 0.24).
- **fig4-pair-156-136**: not_reproduced → partially_reproduced, as the verifier argued.
- **thinning-preserves-dependence**: reproduced → not_reproduced. The thinning reaches its flatness target in only 23 to 26% of runs, and the two pairs that "held" were never flattened. Counting only flattened runs, 0 pairs hold under reading a and 1 under reading b; at least two are needed.
- **odor-unrelated-to-stem**: reproduced → not_reproduced, marked as resting on an assumption. With the sensor-detected poke window, the side arms show a same-sign association (Spearman r = 0.237, p = 0.010). Pearson gives r = -0.007 there and would not change the outcome.

**Fixes and added outputs**
- **Global band (problem 1)**: every connection claim now uses the Methods' stepping procedure: the narrowest band that still holds at least 99% of the surrogates on both sides. The verifier's fixed 0.5%-per-side split holds a median 99.7% (measured during development, not printed in the notebook), so it is wider than the band the Methods define; 1% per side is kept as a variant. Under the 0.5% split, connected-cells-trajectory-specific briefly had all four values in tolerance. Under the Methods' band, layer 5 pyramidal cells are 73.3% against 84.7 ± 8.47, so it stays partially reproduced.
- **Detector false positives (problem 2)**: with every EE188 spike train shifted in time, the detector flags 0.12 to 0.15% of pairs as excitatory and 0.04 to 0.07% as inhibitory, against 0.70% and 0.26% in the real data. I also added the authors' `pairs_all` list with their `CellsInfo` types as a variant for fig3b and nearby-pyr-int.
- **Spike-order test (problem 3)**: the p-value now comes from both tails of the permutation distribution. A synthetic check finds a fourfold effect in 20 of 20 runs in either direction, and flags 3 of 20 runs where first and later spikes are equally effective.
- **Odor window (problem 5)**: the sensor-detected pokes give 30.8% odor-selective cells, still outside 26 ± 2.6.
- **Smaller items**: presynaptic-only jitter gives 46 to 53 of 389 connections, still outside 67 of 343. I also added connection-based cell types for the speed claim, fixed the pair-count printout, listed the tar's members, and added the chance-level note for retrospective coding.
- **Records**: the attempt record has new notes, deviations and findings, plus the round-1 `verifications` block. The README and the notebook summary are updated to match.

**Not done, and why**
- I did not add a question about two odor ports. The paper describes one hole in the start box, and both trial types start 2 pixels apart, so the claims file does not misread the paper there.
- I added one reader question to `questions/crcns-pfc-2.yaml`: whether "no reliable relationship" in odor-unrelated-to-stem should also exclude opposite-sign associations.
- I did not read the sensor channels for the other 12 sessions. Each archive is about 2 GB to stream, which would push the notebook close to the 60-minute limit.
- Nothing is committed. The untracked dotfiles in the repository root (`.bashrc` and similar) are sandbox mount points, not my changes, and I left them alone.
