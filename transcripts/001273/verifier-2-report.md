## 1. Outcomes

The claims file has 17 claims: 6 on DANDI:001273 and 11 marked `data: elsewhere`. The attempt record has 17 outcomes: 2 reproduced, 1 partially reproduced, 2 not reproduced and 12 blocked. Of the 12 blocked, 3 are metadata_insufficient, 6 are other and 3 are too_large. Only one outcome is marked `assumed: true`.

| Claim | Record | Agree? | Comment |
|---|---|---|---|
| fig4-polarized-poles-face-electrodes | reproduced, assumed | yes | The assumption is stated and reasonable. It is that "Up and Bottom" means the image's vertical axis. It decides the outcome: with the axes swapped, 1 of 14 pass (cell 23). Internal support: in each of the four January 19 cells imaged on both axes, the separation turns with the stated axis. The opened-soma variant still passes 12 of 14 (cell 24), but the set of passing experiments changes: 1_20240119 hori goes to 78.3° and 2_20240311 to 60.6°. Individual experiments are sensitive to the mask; the majority holds. |
| fig4-orientation-time-constants | blocked (metadata_insufficient) | yes | Cell 4 now shows the file tree: no ROIs, no labels, no notes. |
| fig4-no-pole-difference | reproduced | yes, but weak | Under the criterion's readings, 0 of 16 are significant (cell 34). The new fit-free variant finds a larger anodic \|dF\| in set A: p = 0.014 for ROI a and 0.011 for ROI b, and p = 0.048 even without the 100 and 130 V runs (cell 35). The fitted \|dFmax\| reaches p = 0.046 in 2 of 8 readings of the window variant. The record says all of this. The outcome holds only because the criterion names the fitted \|dFmax\| and the header readings. |
| fig4-discharging-slower | blocked (metadata_insufficient) | yes | |
| fig4-pooled-time-constants | not_reproduced | yes | No row is within the SEMs under any reading or any variant (cells 28 and 31). |
| fig4-full-charge-within-3us | blocked (metadata_insufficient) | yes | Reading (b) fails both with and without the window filter (cell 41). Reading (a) cannot be tested. |
| fig3c-sustained-firing-2s | partially_reproduced | yes, now | With the revised detector, c7 meets the whole criterion and the firing parts hold in all 4 cells (cell 8). With the first-run detector the result is also partial. However, the record states the per-cell judgement only as a deviation, not as `assumed: true`, and the outcome rests on it. Judged "any cell" (Figure 3C shows one cell), the claim would be reproduced. Judged "most cells", it would not be. This should be flagged as an assumption. c7 also passes only with the bleaching correction (6.66% corrected, 3.30% uncorrected). |
| figs1-di8-anepps-control | not_reproduced | yes | The outcome rests on the claims file's 5% level, not on any assumption by the author. |
| fig1, fig2d, fig2-locks, fig2c, fig3b, figs2 | blocked (other) | yes | |
| fig5, fig6, threshold-depolarization-estimate | blocked (too_large) | outcome yes, reason no | I would still give `other`. The stated reason is the time left in the run, the same reason as for fig1, not the size of the data. |

## 2. Sentences the printed numbers do not support

- **Fig6 notes in the record:** "Streaming the 10.6 GB of this dandiset took 1,115 s". The notebook prints 232 s for listing (cell 1) and 1195 s for loading and reducing (cell 11). Neither 10.6 GB nor 1,115 s appears in any output, and "25.0 GB" for 001274 is not printed either. The count of 232 files is printed (cell 9).
- **fig1, fig3b and figs2 notes and two findings:** these give 16 × 16 stacks at 3,086.4 frames/s for 001032 to 001035, 001034 as a byte-for-byte copy of 001032, all 250-ms sessions in NaCl, and 287 sessions with 71 TTX in 001271. They come from a survey that is not in any notebook. The record says so, but none of it can be checked against outputs.
- **README, line 5:** "181 files ... forming 22 experiments of 7 or 8 replicates." Cell 7 shows 175 files in 22 runs plus 6 single files that are not used.
- **figs1 notes in the record, and cell 10 of `elsewhere_001272.ipynb`:** "under readings (a) and (b) the 5% level finds APs only in neuron 3_20240806 (4 sessions under a, none under b)". Under (b) no neuron fires (cell 8), so "only in neuron 3" is true of (a) alone.
- **Cell 36 and the no-pole notes:** "The criterion's quantity, the fitted |dFmax|, shows no difference under any of its readings." This is true of the header readings, but the window variant, also on fitted |dFmax|, gives p = 0.046 (cell 35). The preceding sentence says so, so this is a wording point.

Every other "**Result:" paragraph, Summary sentence, README cell and record note matches the outputs. I checked the 13 of 14, 10 of 11 and 12 of 14 counts, the 13.8°, 17.1° and 48.7° angles, and the measured values 0.87, 1.62, 0.69 and 2.22. I checked every range of means and medians in cells 28 and 31, the drop counts of 2 to 6, the pair losses of 7 to 10, the 3-τ counts, and the fig3c and figs1 figures (6.66, 3.48, 3.63, 3.30, 3.2, 19 of 52, 2.2 to 2.5%).

The verification block states my round-1 reasons faithfully, close to my own wording. My problems 3, 4, 5, 7 and 9 are attached to the relevant claims. The disagreement on fig3c (`agrees: false`, not_reproduced) is recorded as I gave it.

Claims-file misreading, reported and not corrected: the figs1 test still applies the 5% dF level set for FluoVolt to Di-8-ANEPPS. The author has passed this to a reader question.

## 3. Round-1 points

Resolved:
- **1.** The fig3c detector no longer counts plateau noise: c7 has 0 APs after the ramp.
- **3.** The window variant drops long-τ fits.
- **4.** The docstring now says the fits use the nominal onset, and the estimated-onset variant is added.
- **5.** The fit-free |dF| variant is added.
- **8.** The cell 0 table and the 001274 date check are fixed.
- **9.** The a_clip and opened-soma variants are added.
- All of section C: the HDF5 tree, fit panels for all 22 experiments, onset sensitivity, highest-field traces for both fast-imaging sets, and ROI pixel counts.

Not resolved, by the author's choice, with reasons stated:
- **6.** The 19 experiments cannot be identified.
- **7.** No debris ROI.

What remains that bears on a conclusion:
- **fig3c:** partial versus reproduced depends on how the cells are aggregated. The record should mark this `assumed: true` and state the rule.
- **figs1:** the not_reproduced outcome still depends on the 5% level (round-1 point 2). With a 5 SD level, one neuron ends depolarized, which is still not a majority.
- **fig4-no-pole-difference:** the new variants show an anodic amplitude excess in set A that grows with amplitude. The reproduced outcome holds by the criterion's quantity, not by the data as a whole. It depends on whether the 100 to 130 V runs belong to the paper's 19.
- **fig5, fig6 and threshold-depolarization-estimate:** `blocked_by` should be `other`, not `too_large`. This does not change any outcome.
