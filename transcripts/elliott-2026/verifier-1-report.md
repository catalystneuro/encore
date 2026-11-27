**Verifier report, round 1: Elliott, Andrews et al. 2026 on DANDI:001132**

The claims file holds 24 claims. "Notebook" below means `reproduce_elliott_2026.ipynb` (spikes) and "LFP notebook" means `lfp_elliott_2026.ipynb`.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| sorting-dandiset-link | partially_reproduced | Six of eight sortings link to one file each, with ratios of 74 to 169 against chance (cell 10). S5 and S6 match the electrode layout but no file in time (ratio about 1.3). No S5-layout file (3C) is longer than 3.17 min, while the S5 sorting spans 6.4 min. |
| table1-unit-counts | not_reproduced | All 8 unit counts match exactly, but only 5 of 8 recordings match on both units and file duration (cell 12), and the criterion needs 6. Recordings 7 and 8 have no file to measure. The one real miss is recording 6: the file lasts 2.67 min, the sorted span 2.17 min, the paper says 2.2. |
| fig1g-ka-synchronized-bursting | not_reproduced | Under all four readings the median bursts per epoch is 15 to 40 and the first epoch holds 2 to 4 bursts. Neither is in 5.4 to 8.8 (cell 14). |
| methods-burst-counts | not_reproduced | S1 gives 124 to 353 bursts (expected 67). S2 values all miss: 89 to 157 bursts, a 19 s first epoch, a 486 to 491 s span. Only S1's superburst count (12) and span (344 s) fall in tolerance (cell 18). |
| methods-rate-increase-after-ka | not_reproduced | The rate falls in both slices under readings (b) and (c), by 0.03 to 0.12 spikes/s per unit (cell 21). The criterion's partial outcome needs a rise. |
| methods-onset-latency | blocked (metadata_insufficient) | I confirmed on the archive: session descriptions are empty, the dandiset has no `wasGeneratedBy` entry, the description has no KA timing, and the files have no intervals or stimulus series (cell 3). |
| s4-ka-no-epileptiform | not_reproduced | S3, S5 and S6 have epochs longer than 10 s under every reading (cell 25). However, the positive control S1 also fails under every reading (longest epoch 8 to 10 s), so the test does not discriminate. S4 alone passes under (b, sigma 20). |
| ext3-onset-spectral-signature | partially_reproduced | At the criterion's onset (0.895 s) the baseline is under 1 s and nothing holds. At the paper's initiation time (14.4 s, the author's addition), delta rises at 6 of 6 electrodes and broadband amplitude is above 2x at 6 of 6 (2.1 to 3.0). Theta amplitude never reaches 2x (at most 1.66) (cell 28). |
| fig1j-theta-propagation-stages | not_reproduced | Initiation runs 75 to 79° from the layer axis, and initiation versus seizure differ by 4 to 16°. Plane R² is 0.02 to 0.05 for S1, so the directions carry little information (cell 22). |
| ext4b-theta-delay | not_reproduced | Median lag is -19 to -23 ms against 40 ± 4 ms (cell 24). |
| ext4-electrode-lag-clusters | partially_reproduced | S1 initiation, S1 seizure and S2 seizure are coherent beyond all shuffles. S3 and S4 are not coherent (0.44 against 0.69 to 0.90). S2 initiation in the code's 94 ms window fails (cells 18 and 19). It passes only in the author's own 0.5 s window. S5 and S6 were not tested. |
| methods-rolling-wave-counts | blocked (methods_underspecified) | The criterion allows this. It also names a detector that could be adopted as an assumption, and that was not tried. |
| fig2a-subbursts-track-theta | not_reproduced | In S1 the firing difference does not flip (0.22, then 0.91) and theta does not alternate. In S2 firing flips but theta does not (cell 26). |
| table2-phase-locking-counts | partially_reproduced | Under the code's cycle selection, recordings 1 and 3 match (73, 107). Recordings 2, 4, 5 and 6 stay below 10% with the code's spans (8.0, 5.9, 5.7, 5.5%). Recording 2 never reaches 14 ± 1.4, and recordings 7 and 8 are untested (cell 9). |
| table2-phase-locking-seizure-vs-not | partially_reproduced | Seizure mean is 43.0 to 46.9% (in tolerance) and every other value is below 10%. Envelope selection with the code's spans gives 3 of 4. S2 outside seizure is 8/180 = 4.44%, the paper's own count, which fails 4 ± 0.4 only through rounding (problem 8). |
| fig2b-phase-cluster-kuiper | reproduced | Reading (a) with cycle selection gives p = 0.0042, and reading (c) gives 0.0014 (cell 14). This depends on the code's selection: with the Methods' envelope selection, reading (a) gives p = 0.037, which is only partial. |
| fig2c-sttc-two-clusters | partially_reproduced | S2 holds in 3 of 4 variants. S1 fails in all 4 (Mann-Whitney p 0.20 to 0.59) (cell 30). |
| ext9-sttc-eigenvector-gradient | partially_reproduced | S2 holds (Spearman p = 4e-13). S1 fails (p = 0.26) (cell 33). |
| ext9-sttc-beats-correlation | reproduced | STTC wins on 20 of 20 eigenvalues and 20 of 20 errors (cell 35). |
| fig3a-significant-pairs | reproduced | All 8 counts are exact (cell 37). I checked the STTC helper against a brute-force calculation and it agrees. |
| fig3a-bipolar-angle-histograms | partially_reproduced | S1 and S2 are bipolar and no other slice is, under both y directions. S3 and S4 are never unimodal. S5 and S6 fall in their stated class only with y flipped (cell 40). |
| ext10-baseline-same-circuit | reproduced | Both baselines are bipolar, with modes 0 to 22° from the KA modes (cell 43). |
| table3-geometry-test | reproduced | With y as stored, 8 of 8 are in tolerance, and S1 KA gives p = 9.66e-20 (cell 45). |
| ext12-simulation-recurrence | blocked (other) | The notebook gives no reason beyond "see the attempt record". The claim needs only the repository's simulation code, not the dandiset, so it looks testable. |

### B. Problems

1. **[affects a conclusion]** s4-ka-no-epileptiform (cell 25). The positive control S1 fails under every reading, so "not reproduced" says the measure does not work, not that S3 to S6 burst. The cell also drops "synchronized" from the claim: the fraction of units that rise per burst is 0.15 to 0.34 in S3 to S6, against 0.49 to 0.74 in S1 and S2 (cell 26). The bursts in those slices come from thresholds near noise level (up to 237 bursts/min). The outcome label stands by the criterion, but it should be reported as a test that cannot discriminate.
2. **[affects a conclusion]** ext3 (cell 28). The criterion's onset falls 0.9 s into the recording. The required 5 s baseline does not exist there, and that stretch sits in the edge region of the 0.5 Hz wavelet, so that run is not a valid failure. The only valid run uses 14.4 s, which the author added and the criterion does not name.
3. **[affects a conclusion]** ext4 and fig2a (cells 18 and 26). The code's S2 initiation window is 94 ms, shorter than one theta cycle (median lag 0, 0.2% of lags at the window edge), so k-means on it is meaningless. Whether ext4 is reproduced or partial turns on this. fig2a also takes its S2 modes from these incoherent clusters; S1 fails anyway, so fig2a's outcome does not change. The S2 sub-burst times (35.208, 35.234, 35.265, 35.302 s, about 30 ms apart) are too close together to track theta. Their source in the code was not shown.
4. **[affects a conclusion]** ext12 is blocked with no reason given in the notebook.
5. **[does not affect a conclusion]** hist_shape (cell 40). Unit positions sit on a 17.5 µm grid, so many pair angles fall exactly on the 22.5° bin edges, and mirroring the angles does not mirror the histogram. I confirmed this on a synthetic lattice. The markdown says the classes do not change when y is flipped, but the output shows S4, S5 and S6 change class. S1 and S2 are robust, and the partial outcome holds under both directions.
6. **[does not affect a conclusion]** fig2b (cell 14). Split (b) divides angles by their distance from the mode and then tests the angles, so it is significant by construction (p = 0). This is a flaw in the claims file's reading, and the notebook reports it without comment.
7. **[does not affect a conclusion]** Stage windows (cell 15). The baseline window (13.6 to 14.6 s) overlaps initiation (14.4 to 14.91 s) and contains detected bursts at 13.15 and 13.76 s. The text also places the paper's baseline plot at 14.62 s, which is inside initiation. fig1j fails on its other conditions regardless.
8. **[does not affect a conclusion]** table2-seizure-vs-not. The 4 ± 0.4 tolerance is applied to a rounded percentage, so it rejects the paper's own count of 8/180 (4.44%). This is a claims-file issue. The "others" mean also covers only 4 of the 6 recordings. On chance level: the shuffled-spike null gives 10/212 for S1 and 15/180 for S2, and the paper's 5% outside seizures is the Rayleigh test's nominal false-positive rate.
9. **[does not affect a conclusion]** fig1g, burst readings (claims file). Merging peaks only within 50 ms counts sub-bursts as bursts; the code's S1 sub-bursts are about 170 ms apart. The readings therefore cannot produce the paper's unit of a burst. 67 bursts in 11 superbursts is about 6 per superburst, which agrees with "6 to 8". The 12 epochs found include a spurious one at 0.7 to 2.4 s. Separately, reading (a) uses the separate baseline recording in place of the pre-KA part of the KA recording. This is stated, and the means are similar (4.32 against 4.20).
10. **[does not affect a conclusion]** fig1j and ext4b (cells 22 and 24). I checked the sign conventions of `lag_matrix` and `plane_direction` on a synthetic travelling wave and they are correct. Even so, 87% of pair lags along the fitted seizure direction are negative, which contradicts the direction itself; with R² of 0.05 the plane fit means little. The hilus-on-the-concave-side assumption in `layer_axes`, if reversed, would make the seizure-versus-outward angle 7 to 29°, but the initiation conditions still fail.
11. **[does not affect a conclusion]** table2 counts (cell 8). Moving the code's spans from file time to sorting time is an inference, from the S4 span lying beyond the sorting. It is plausible, and recording 2 fails under every reading anyway. Theta is filtered per window, which adds edge effects in 10 s windows.
12. **[does not affect a conclusion]** ext9 (cell 33). The second-eigenvector test is the author's own and is not in the criterion; S1 passes it (p = 2e-7). It must not count toward the outcome.
13. **[does not affect a conclusion]** table1 (claims file). The paper's durations are the analysed spans: the sorted span matches for all 8 recordings, while the file duration misses for recording 6. Under the strict criterion, recordings 7 and 8 are unmeasurable, not mismatched.
14. **[does not affect a conclusion]** methods-rate-increase readings (b) and (c). They compare separately curated unit sets on different electrode configurations (887 against 1009 channels for S1), so the comparison is not like for like. The readings come from the claims file.

### C. What I could not check

- **Repository inputs.** I did not open the paper's GitHub repository, so I could not verify the sorting-file assignments, the seizure windows, the S2 sub-burst times, the code's spans, or the code group-1 thresholds. Printing each value next to its source file and line would settle this.
- **S5 and S6.** I could not confirm they are absent from the dandiset beyond the notebook's scan. A scan of the S5 sorting against the 3C files concatenated in index order would help.
- **Bin-edge effect on bipolar classes.** Needed outputs: the number of pair angles lying exactly on bin edges, and the classes under a histogram offset by half a bin.
- **s4.** Needed output: a run that keeps only bursts where most units rise.
- **ext3.** Needed outputs: the criterion's onset recomputed with the other three burst readings, and a printout of how much baseline exists before it.
- **S2 initiation.** Needed outputs: windows around 35.2 s of one or more full theta cycles, with their lag-edge fractions.
- **Figures.** Embedded images (rasters, cluster maps, heatmaps) could not be compared with the paper's figures; I relied only on the printed numbers.

I did not open the NWB files themselves; the KA-timing check rests on the archive's API metadata and the notebook's cell 3.
