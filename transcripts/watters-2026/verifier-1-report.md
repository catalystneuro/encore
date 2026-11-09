**Verification report, round 1: Watters et al. 2026 on DANDI:000620 (version 0.261019.2000)**

The claims file has 26 claims. The notebooks test 13 of them: 11 in `reproduce_watters_2026.ipynb` and 2 in `decoding_watters_2026.ipynb`. The other 13 need the encoding models fitted, and the notebook blocks them as `too_large`.

### A. Outcomes

| claim | outcome | reason |
|---|---|---|
| fig1b-performance-load | reproduced | Accuracy falls from 1 to 2 to 3 objects and stays above 1/2 and 1/3, for both monkeys, under both trial readings and both radii (cell 8). Reading (a) with the code's radius matches the paper notebook exactly: P 0.953/0.930/0.692, E 0.928/0.759/0.561. |
| fig1c-reaction-times | reproduced | Interquartile range is 50–73 ms and the median 227–273 ms, for both monkeys and both readings (cell 10). |
| ext1-misbinding-errors | reproduced | With the 4.8° radius, non-target responses are both the largest class and more than half of errors: 0.85–0.99 in all four monkey × set-size cells (cell 12). With the Methods' 2.4° radius, Monkey P's 2-object cell fails (0.449). Cell 4 shows every trial within 0.2 arena widths was rewarded and none beyond, so the 4.8° radius is the one the task used. Under 2.4°, rewarded responses near the target are counted as "no vertex" errors. |
| triangle-unit-counts | reproduced | Reading (a) gives exactly 4688 / 2937 / 1751 units and 10 / 14 sessions; reading (b) is also within tolerance (cell 18). |
| ring-unit-counts | reproduced | Reading (a) gives 3052 / 1712 / 1340 against 3051 / 1712 / 1339, with 10 / 12 sessions (cell 18). |
| ext2-stimulus-delay-activity | reproduced | Panel a: Pearson 0.97 / 0.90, Spearman 0.96 / 0.89, and 97–99% of units above 1 Hz in the stimulus phase. Panel b: all 4 plots positive, r 0.40–0.60, p < 1e-89 (cell 20). |
| ext3ab-decoding | partially_reproduced | Delay-phase position decoding beats the shuffled control in all three sessions under both readings (83–99% against about 33%). Identity decoding fails both readings in all three sessions (decoding cell 8). The criterion has no "partial" rule, so this label is mine. The identity failure may come from problem 1. |
| ext3c-decoder-orthogonality | partially_reproduced | Receptive Field synthetic data have medians of 91.6–96.7°, and Ring neural data 88.8° / 93.3°; both readings hold for these. Triangle neural data have medians of 106.7° / 106.5°, which fail both readings (decoding cell 10). The criterion requires both neural and Receptive Field data to pass. |
| fig2b-selectivity-range | partially_reproduced | Position AUC meets the cut-offs for both monkeys under both p methods. Identity AUC's top decile is not above 0.7 for E (0.654 / 0.681) or for P under the Methods p-value (0.700) (cell 24). |
| fig2d-signal-noise-triangle | blocked (methods_underspecified) | The Methods version gives the full result for both monkeys. The code variant gives only the rise for E: its lowest bin has 124 rows, mean +0.0245, interval [−0.030, 0.079] (cell 29). The criterion says that when the two versions differ, the outcome is methods_underspecified. |
| fig5ab-ring-behavior | reproduced | 2-object fraction correct is 0.72–0.90, above 1/2. The Ring/Triangle interquartile-range ratios are 0.94 and 1.10 (cell 14). Values match the paper notebook (P 0.903, E 0.945 / 0.756). |
| fig5cd-ring-tuning | partially_reproduced | Preferred angles fall in all three sectors in every monkey × area. The AUC range check fails: identity for both monkeys, and position for E (top decile 0.658 / 0.674) (cell 26). |
| fig5e-signal-noise-ring | partially_reproduced | Monkey P and the pooled data pass under both readings. Monkey E fails both: lowest bin 0.017 [0.008, 0.027] against highest 0.024 [0.015, 0.032] (cell 31). The criterion is per monkey and has no "partial" rule. |
| fig4a, ext6, ext5, fig4b, nslots-two-best, ext11, ext7, fig4c, fig4d, ext8, fig5f, fig5g, fig5h (13 claims) | blocked (too_large) | All rest on fitting the Slot, Switching and Gain models. The archive check (DANDI API) agrees: 142 assets, of which 47 spikesorting (units, spike times, stable trials), 48 behavior+task and 47 raw ecephys files. There are no fitted models or caches in the dandiset, so the data are complete and only compute blocks these. No part of any of these claims can be tested without fits. The only fit-free quantity is the count of Triangle sessions with more than 100 modeled units (4 with the Methods p-value, 11 with the code's, from cell 22), which is an input to fig4a and not a result. |

### B. Problems

1. **[affects a conclusion]** `wm.decoding_data` / `wm.train_linear` (decoding cell 8): the decoder gets raw rates in Hz (about 1–130), with no per-unit normalisation, and neither the helper module nor the notebook says the paper's `dataset.py` does this. I tested it on synthetic 120-trial × 80-unit data with a weak 3-class signal and a shared gain:
   - with raw rates, the same decoder (SGD at 0.01, L1 0.003) scores 0.70 / 0.73;
   - with z-scored rates it scores 0.94 / 1.00;
   - a nearest-class-mean reference scores 0.76 / 0.98.

   So the ext3ab identity failure, and possibly the ext3c Triangle angles, may be an artifact of input scaling.
2. **[affects a conclusion]** `wm.get_simultaneous` (decoding cells 8 and 10) cuts the unit count far below the modeled units:
   - Triangle 2022-06-04 keeps 20 of 116 units;
   - Ring 2022-06-09 keeps 44 of 89.

   The Methods' orthogonality argument assumes about 100 simultaneously recorded units. The greedy rule behaves sensibly on my synthetic test, but its fidelity to the code can't be checked. The ext3c Triangle neural median pools a 20-unit session, and the notebook prints no per-session medians.
3. **[affects a conclusion]** `wm.train_linear_2obj` with Ring targets (`decoding_data`, kind "2obj"): the outputs are sigmoids, in (0, 1), but the Ring targets are 2x and 2y, in [−0.7, 0.7]. Negative targets can't be reached. The helper module does not show that `models.py` uses a sigmoid for the Ring. The Ring half of the ext3c result rests on this.
4. **[does not affect a conclusion]** `wm.ring_noise` (cell 31) uses ordered pairs, so each pair appears twice. The fig2d code variant has 18 rows per pair. `wm.mean_ci` treats all rows as independent, so the intervals are too narrow. Monkey E fails fig5e anyway and Monkey P's effects are large, so no outcome changes.
5. **[does not affect a conclusion]** `wm.auc_p_code`: on null data it gives about 8% of pairs at p < 0.05 (folded two-sided). The unit-level rule, which takes the best of three pairs, gives about 15% false positives under the Methods p-value. Both follow the paper's or code's method as cited. They inflate shading and model-unit counts but not the AUC deciles that decide fig2b and fig5cd.
6. **[does not affect a conclusion]** Cell 33's cost estimate:
   - it times a numpy CPU network, with sizes and batch said to come from a config that is never printed;
   - no GPU is considered;
   - no reduced partial fit is tried.

   Even 100× faster, the 13 claims would still take days, so `too_large` stands.
7. **[does not affect a conclusion]** Claims-file reading, reported and not corrected:
   - ext3ab requires identity decoding above control, but Methods (Decoding Analyses) say "identity was poorly decodable on single trials". The criterion may be stricter than the paper.
   - T2 leaves the correctness radius open, but the dataset's reward record (cell 4) settles it at 4.8°.
   - The 0.6 / 0.7 decile cut-offs that decide fig2b and fig5cd are the claims-writer's own.
8. **[does not affect a conclusion]** Small points:
   - ext3ab's panel-a test sets hold only 21–24 trials, so the all-ten-splits reading has little power.
   - Excluding Perle 2022-06-06 (2-object trials only) is the author's choice, but it reproduces the paper's 22 Ring sessions.

### C. Not checked

- **Fidelity to the paper's code.** The paper's code was not available to me, so I could not confirm that the helper module matches `dataset.py` (normalisation, the simultaneity filter, the synthetic receptive fields), `models.py` (Ring output nonlinearity), `auc.py`, `run_compute_ring.py` (ordered pairs) or the batch size in the model configs.
- **Outputs that would have settled problems 1–3**, if added to the decoding notebook:
  - units and trials per session before and after `get_simultaneous`;
  - per-session ext3c medians;
  - decoder training accuracy;
  - ext3ab and ext3c re-run with z-scored inputs;
  - Ring ext3c with a linear (or tanh) output.
- **fig2d code variant.** Bin counts with intervals that cluster by pair would show whether the 124-row lowest bin for E is reliable.
