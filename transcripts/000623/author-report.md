All 26 testable claims reproduced. The three fMRI claims are blocked as `not_runnable`. The entry passes `check` and a clean `all` run, and the handover package is built. Nothing is committed.

## 1. Outcomes

| Claim | Outcome | Key numbers (paper in brackets) |
|---|---|---|
| cohort-emu-sessions | reproduced | 29 runs, 16 participants, 13 with two runs |
| table1-demographics | reproduced | 11 female, age 37.75 (SD 13.86); per-participant rows all match Table 1 |
| neurons-total-and-areas | reproduced | 1450 units; 479 / 261 / 236 / 299 / 175, all exact |
| units-per-wire | reproduced | 1.990 |
| firing-rate | reproduced | 2.471 ± 3.326 spikes/s |
| isi-violations | reproduced | 0.404 ± 0.529%, only under reading (b), units below 3% |
| waveform-snr | reproduced | 5.948 ± 3.477 and 2.066 ± 1.128 |
| projection-distance | reproduced | 11.982 ± 8.933 |
| isolation-distance | reproduced | median 24.904 |
| gaze-missing-p53cs | reproduced | 73.6% and 83.6% (74, 84) |
| gaze-similarity | reproduced | r = 0.751 ± 0.122; missing 6.63 ± 8.40%, only under reading (a), 27 sessions |
| recognition-auc | reproduced | 0.789 ± 0.189, under reading (a), 29 sessions |
| auc-run1-vs-run2 | reproduced | p = 0.958 (0.960) |
| confidence-accuracy | reproduced | p = 0.00027 |
| memory-sessions-included | reproduced | 1266; all three readings drop the same five runs the paper lists |
| memory-cells-significant | reproduced | amygdala 32/436, ACC 21/186 (22), vmPFC 14/150; all p < 0.05 |
| memory-cells-not-significant | reproduced | hippocampus p = 0.227, preSMA p = 0.135 |
| memory-lfp | reproduced | 37, 32 (33), 40, 17, 28; vmPFC p = 0.065 (0.05) |
| memory-ieeg | reproduced | 41, 34, 45, 25, 31 (32) |
| memory-modalities-differ | reproduced | |
| fig6-examples | reproduced | |
| scenecut-labels (link) | reproduced | 80 continuity cuts, 13 scene changes; all 93 placed in all sessions |
| event-cells | reproduced | 10, 20, 15, 7, 8, all exact |
| event-lfp | reproduced | 20, 40, 33, 15, 22, all exact |
| event-ieeg | reproduced | 66 (67), 41, 25, 33, 21; vmPFC denominator is 448, paper prints 449 |
| fig7-examples | reproduced | p = 0.0244, 0.0298, 0.0258, 0.0002 |
| nwb-contents | reproduced | LFP stored start time is 10 s off (finding) |
| scanner-questions | reproduced | 5.967 ± 0.983, from the code repository's copy of the answers |
| fmri-motion, fmri-tsnr, fmri-isc | blocked: not_runnable | OpenNeuro ds004798 has raw BIDS only; fMRIPrep cannot run here |

## 2. Dataset, assumptions and questions
- **Version:** pinned 0.240130.2108, the version the paper cites. All three published versions hold identical assets; the notebook shows this.
- **Main finding:** all 58 LFP series store a start time near 0 s, but the samples begin 10 s before the movie, as the paper's code assumes. On the corrected clock about 30% of channels respond to recognition images; on the stored clock under 1% do.
- **Other findings:**
  - `isibelow` is described as a proportion but holds percentages.
  - 448 units have no isolation distance (NaN), and one has 3.4e27.
  - The electrodes table lists 1242 projection distances; the units per wire imply 1266 pairs.
  - The files hold 1457 units. The paper's 1450 come from a rule found only in the code (at least one spike during the movie).
  - The text's AUC exclusion rule is not in the code; here it makes no difference.
  - P53CS run 2 has 34 recognition trials instead of 40.
  - The files have no scene-cut annotations; these come from the code repository.
- **Assumptions:** none. Every method detail came from the claims file or the code it cites.
- **Questions for the paper's authors:** none.
- **Questions to a reader:** none.

Two implementation choices are mine and are recorded as deviations: the permutation test is seeded, and within each shuffle the cells of a session share one set of bootstrap resamples. Each cell's null result still follows the code's distribution.

## 3. Protocol points
1. Step 2's clock check by decoding scene-cut labels could not tell the two LFP clocks apart (12 to 13% of channels selective either way). A response to recognition-image onsets could. I added that check and recorded both. The protocol could suggest an onset-response check for continuous sessions.
2. For `data: elsewhere` claims, the protocol does not say what to do when the archive holds raw data but the claim needs heavy preprocessing such as fMRIPrep. I used `not_runnable` and said what I looked for.
3. Where a criterion lists readings and only one matches (isi, gaze missing, AUC), the reader rule gives "reproduced" with a deviation. Author step 1.6 instead suggests an assumption when readings give different outcomes. I followed the criterion and did not set `assumed`.
4. The event-ieeg criterion expects a denominator of 449 with tolerance 0, but also says to report the count found. I counted 448, called it reproduced, and added a `paper_inconsistency` finding.
5. The protocol has no rule for a claim whose test needs results from two notebooks. I moved nwb-contents and memory-modalities-differ into the HFB notebook, which recomputes the single-cell result.

## 4. Runtime and failures
- **Run:** about 2 h 30 min, from 00:44 to 03:13 UTC.
- **Notebooks:** `reproduce_keles_2024.ipynb` takes 3.2 min. `hfb_keles_2024.ipynb` takes 24.2 min, near the 30-min limit; streaming and filtering the LFP is 17 min of that.
- **Failures:**
  - A long-regex `grep` on the one-line paper text hung for an hour and cost that time.
  - My first sample load failed because h5py objects cannot be pickled; fixed.
- **Post-run edit:** I wrote the clock numbers into two markdown cells after the final run, in both the source and the executed notebook. No code or outputs changed.
