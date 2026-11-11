**A. Outcomes** (31 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| cohort-emu-sessions | reproduced | 29 sessions, 16 participants, 13 with two runs. Every participant's run count matches Table 1 (reproduce nb [6]). |
| table1-demographics | reproduced | All 16 EMU participants' age, sex and diagnosis match Table 1. Over 20 participants: 11 female, mean 37.75, SD 13.86 at ddof 0 ([8]). I checked the hand-entered Table 1 rows against the paper. |
| neurons-total-and-areas | reproduced | U = 1450, split 479/261/236/299/175 ([10]). Without the spike rule there are 1457 units. |
| units-per-wire | reproduced | 1.990 over 732 session–wire pairs ([12]). |
| firing-rate | reproduced | 2.471 ± 3.326 spikes/s at ddof 0 ([14]). |
| isi-violations | reproduced | Reading (b), units with isibelow < 3: 0.404 ± 0.529. Reading (a) gives 0.462 ± 0.727, with the s.d. outside tolerance ([16]). One reading is enough. |
| waveform-snr | reproduced | Peak SNR 5.948 ± 3.477, mean SNR 2.066 ± 1.128 ([18]). |
| projection-distance | reproduced | 11.982 ± 8.933 over 1242 pairs ([20]). |
| isolation-distance | reproduced | Median 24.904 over 1001 units ([22]). |
| gaze-missing-p53cs | reproduced | P53CS has 73.6% and 83.6% missing; it is the only participant at or above 50% (next highest: P58CS 37.6%) ([24]). |
| gaze-similarity | reproduced | r = 0.751 ± 0.122. Missing gaze over the 27 kept sessions is 6.63 ± 8.40%, within the ±0.7 / ±0.8 tolerances. Over all 29 it is 11.59 ± 20.01%, which fails ([26]). |
| recognition-auc | reproduced | Reading (a), 29 sessions: 0.789 ± 0.189. Reading (b), per participant: 0.787 ± 0.134, s.d. fails ([28]). |
| auc-run1-vs-run2 | reproduced | p = 0.958 (≥ 0.05). Run 1 0.788 ± 0.138, run 2 0.792 ± 0.245, all within tolerance ([30]). |
| confidence-accuracy | reproduced | 22 sessions; t = 4.36, p = 0.00027 < 0.001; high (89.9%) above low (72.0%) ([32]). |
| memory-sessions-included | reproduced | All three readings remove exactly the five runs the text lists and keep 1266 units ([34]). |
| memory-cells-significant | reproduced | Amygdala 32/436 (p 0.0065), ACC 21/186 (p 0.0005; 21 is within ±2.2 of 22), vmPFC 14/150 (p 0.014) ([36]). |
| memory-cells-not-significant | reproduced | Hippocampus 14/238 (p 0.227), preSMA 17/256 (p 0.135), both ≥ 0.05 ([36]). |
| memory-lfp | reproduced | Significant: amygdala 37 (p 0.003), ACC 32 (p 0.036), preSMA 40 (p 0.0005). Not significant: hippocampus 17 (p 0.90), vmPFC 28/336 (p 0.065 ± 0.0055). Channel totals 368 and 336 ([9] in hfb nb). |
| memory-ieeg | reproduced | Significant: ACC 41 (p 0.001), vmPFC 34 (p 0.016), preSMA 45 (p 0.0005). Not significant: amygdala 25 (p 0.47), hippocampus 31 (p 0.109). All areas 368 channels ([10]). |
| memory-modalities-differ | reproduced | ACC is significant in all three modalities, hippocampus in none, amygdala in cells and LFP but not iEEG ([16]). |
| fig6-examples | reproduced | preSMA cell: familiar above novel, p 0.0030. ACC cell, preSMA macro channel and ACC micro channel: novel above familiar, p 0.0002 each ([18]). |
| scenecut-labels | reproduced | 80 continuity cuts, 13 scene changes; every onset falls inside the movie window in all 29 sessions ([38]). |
| event-cells | reproduced | Counts 10/20/15/7/8 equal the paper's. p: vmPFC 0.004, preSMA 0.0005, amygdala 0.089, ACC 0.226, hippocampus 0.207 ([40]). |
| event-lfp | reproduced | Counts 20/40/33/15/22 equal the paper's; all five areas p ≤ 0.0165; channel totals 448 and 400 ([13]). |
| event-ieeg | reproduced | All five areas p ≤ 0.002. Amygdala 66, within ±6.7 of 67; the others equal. vmPFC has 448 channels, not the paper's 449, which the criterion already flags as a probable misprint ([14]). |
| fig7-examples | reproduced | preSMA cell p 0.0244, vmPFC cell p 0.0298, hippocampus macro channel p 0.0258, preSMA micro channel p 0.0002. All show scene change above continuity cut and the legend's area ([20]). |
| nwb-contents | reproduced | All 29 files have every listed item ([6]). The LFP is 1000 Hz with starting_time ≈ 0. The Usage Notes say timepoints start 10 s before starting_time, and image-onset HFB responses appear on that clock (29.7%/30.5% of channels) but not on the file's own clock (0.8%/0.9%) ([4]). |
| scanner-questions | blocked (other: data not in the dandiset) | The claims file marks it `elsewhere`, "Not tested on the dandiset". The notebook tested it anyway on the code repository's CSV and got 5.967 ± 0.983, which matches ([42]). |
| fmri-motion | blocked (data_missing) | I checked both archives. DANDI 0.240130.2108 holds only the 29 ecephys NWB files. The OpenNeuro ds004798 snapshot 1.0.5 has raw BIDS only, with no `derivatives/`, so there are no fMRIPrep confounds. Nothing can be tested from the dandiset. |
| fmri-tsnr | blocked (data_missing) | Same as fmri-motion: tSNR as the paper computes it needs fMRIPrep outputs, which are not on either archive. |
| fmri-isc | blocked (data_missing) | Same as fmri-motion. |

Totals: 27 reproduced, 4 blocked.

**B. Problems**

1. [does not affect a conclusion] hfb nb [3]/[6], reproduce nb [3]. The markdown says the stored LFP starting_time near 0 contradicts the Usage Notes. It does not: the Usage Notes tell readers to start at 10 s before starting_time. The printed check "starting_time is 10 s before the movie: 0 of 58" tests the wrong thing. The column `lfp_covers_10s_before_movie_after_shift` is true by construction because it is computed after the shift. The real evidence is the image-onset test in [4], which only tells a 0 s offset from a 10 s offset.
2. [does not affect a conclusion] reproduce nb [42]. scanner-questions is tested even though the claims file says it is not tested on the dandiset. The result should be reported as outside data, not as a dandiset reproduction.
3. [does not affect a conclusion] `perm_null_counts`. Sharing bootstrap resamples across the cells of a session is the author's own shortcut, and the notebook says so. I tested it on synthetic data: 300 cells, 2,000 shuffles, both designs. The null-count variance came out at 13.68 vs 13.31 and 8.42 vs 7.99 (shared vs per-cell), and the 95th and 99th percentiles moved by at most 1. That is within Monte Carlo noise, so the shortcut is acceptable.
4. [does not affect a conclusion] `selection_and_null` calls. The permutation seeds are 0, 1, 10, 11, 20 and 21 rather than open detail 8's single seed 0. Each p is reported with its Monte Carlo SE, and no decision sits within 2 SE of 0.05 except vmPFC in memory-lfp (0.065 ± 0.0055), which keeps its decision either way.
5. [does not affect a conclusion] reproduce nb [20]. There are 1242 pairwise distances where k(k−1)/2 gives 1266. The notebook prints the gap but does not explain it. The criterion only asks for the pooled entries, so the result stands.
6. [does not affect a conclusion] reproduce nb [26]. The Gaussian sigma is the mean pixels-per-degree over all 29 sessions, including the two excluded P53CS runs, and is labelled "(code)". I cannot check that attribution, and sensitivity to using the 27 kept sessions is not shown. The effect is likely small.
7. [does not affect a conclusion] Claims file, confidence-accuracy. The statement says "significantly higher", but the paper's sentence says only "significantly different". The criterion's direction requirement is met in any case (18 of 22 sessions have high above low).

Helper checks that passed on synthetic inputs:
- `observed_selection` p-values equal a direct resample-mean implementation.
- `heatmap` drops NaN samples.
- `session_auc` gives values below Mann–Whitney, as expected from the adjustHF clamp (a perfect session gives 0.963).
- `confidence_accuracy` and `scenecuts` match the claims file's rules.

There is no train/test split anywhere, so leakage does not apply.

**C. What I could not check**

- **Fidelity to the original code.** The original scripts are not available, so I cannot confirm that `bmovie.py` ports them faithfully, in particular reseeding `default_rng(13)` once per session block and resampling in the code's order. The match of Fig. 6/7 p-values to three digits and the exact event counts support the port. Printing one cell's p from a literal port of `get_bootstrappval` would settle it.
- **confidence-accuracy exclusions.** Seven sessions are dropped by `check_inclusion`, and the notebook does not say which or why. A table of per-session counts per confidence level would show it.
- **HFB intermediates.** There is no output from the filtering and re-referencing steps, such as a PSD before and after the notch filter, or per-channel z-scored HFB statistics. I can only judge the pipeline by its final counts.
- **LFP clock precision.** The test only compares 0 s and 10 s offsets. A sweep of offsets around 10 s (e.g. ±0.5 s) for the image-onset response would bound the alignment error.
- **Gaze sigma sensitivity.** The gaze r computed with sigma from the 27 kept sessions is not shown.
