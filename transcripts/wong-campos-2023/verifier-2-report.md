**Verifier report, round 2: Wong-Campos et al. 2023 on DANDI:001791 v0.260424.0313**

The claims file holds 19 claims. The attempt record gives: reproduced 3, partially reproduced 6, not reproduced 3, blocked 7. Six outcomes carry `assumed: true`: fig1d, fig1fg, fig2e, fig2f-conduction-speed, fig3d and figs12.

### 1. Outcomes

| Claim | Agree? | Assumption |
|---|---|---|
| fig1d-light-intensity-spike-rate: reproduced | Yes | Stated and reasonable. The pulse windows are inferred, and a 1 s period fits best among periods from 0.8 to 1.2 s (cell 22). |
| fig1fg-dendrite-peaks-after-soma: partially reproduced | Yes | Stated and reasonable. Timing uses a parabola, which is unbiased on average in the synthetic check (cell 26). |
| fig2c-no-trial-variation: blocked (data_missing) | Yes | Not applicable. The figure2h and figure2j files now open, and they hold pooled values with no site labels (cell 9). |
| fig2e-half-amplitude-distance: reproduced | Yes | Stated and reasonable. The site set is LR, with n = 30. |
| fig2f-delay-range: not reproduced | Yes | Not applicable. |
| fig2f-conduction-speed: reproduced | Yes | Stated and reasonable (the LR set). See 3b. |
| fig3d-dendrite-cross-correlation: partially reproduced | Yes | Stated and reasonable. P1 matches; the 3-neuron set P2 does not. |
| figs9-shot-noise-bound, fig3i-coupling-vs-distance, figs11-dendritic-spikes-rare: blocked (data_missing) | Yes | Not applicable. |
| fig4a-doublet-isi: not reproduced | Yes | Not applicable. |
| fig4bc-doublet-first-fails: partially reproduced | Yes | Not applicable. K = 5 with reading (b) gives 0.68 against the 0.70 bound. |
| fig4d-accelerating-amplifies: partially reproduced | Yes | Not applicable. The fig4d criterion does not name the detection thresholds itself, so letting both decide is the stricter, defensible reading. |
| fig4fg-opto-first-bap-attenuated: blocked (other) | Yes | Not applicable. With recordings 14 and 15 read at 1,000 Hz, no dendrite has a delay above 3 ms by either measure (cell 56). |
| fig4h-biphasic-bap-amplitude, figs13-distal-more-modulated: blocked (other) | Yes | Not applicable. |
| fig4ijk-sensory-first-fails: partially reproduced | Yes, changed from my round 1 | Not applicable. The first bAP is smaller in the average under every reading and in 18 of 20 and 20 of 22 trial–dendrite pairs. The 9-of-13 bound fails only for dendrite 1 at K = 5, and the "all start as bAPs" part fails. One part holds and one fails, so partial is fair. |
| fig4l-sensory-plateau: not reproduced | Yes | Not applicable. |
| figs12-spontaneous-failures-both-states: partially reproduced | Yes on the outcome | **Mislabelled.** If column 1 were accepted as the soma, the anesthetized half would pass (failures in 3 to 4 recordings, cell 71), and the claim would be *reproduced*. "Partially" follows from *not* accepting that identification, which cells 13–14 say the data do not support. So the outcome does not rest on the assumption. `assumed: true`, the deviation "Assumed that column 1 … is the soma" and the label "resting on column 1 as the soma" (cell 72, Summary) contradict the reasoning. |

I found no place where the claims file misreads the paper.

### 2. Statements the numbers do not support

- **Cell 54 (fig4d):** "below 1 when decelerating (0.953), p < 1.2e-05, in both windows". In the 0–8 ms window the decelerating reading (c) gives p = 5.9e-05 (cell 52). The attempt record's "(p < 1.2e-05); both windows pass" holds for the 0–5 ms window only.
- **Attempt record, fig4bc notes:** "Measured from its own baseline the second bAP is smaller, median ratios 1.07 to 1.15". Ratios above 1 mean the second bAP is still *larger* than the first; only the ratio is smaller. Cell 50 says it correctly ("lowers the median ratios").
- **Cells 34–35 and the fig2f-delay-range notes:** "No LR delay is exactly 0 … so the small delays are values, not placeholders". The test is exact equality (`de == 0`). Yet the LR minimum prints as 0.000 to 3 decimals (cell 7) and 0.0 in cell 34, so at least one LR value is below 0.0005 ms. The data are given to 0.01 ms, so that value is effectively 0 (a floating-point residue). The check does not show what the sentence says. It does not change the outcome: 23 of 32 LR delays are below 1.35 ms either way.
- **Cell 65 and the fig4ijk notes:** "dendritic events whose somatic event is below or near the detection threshold". Cell 64 shows only that the high-pass soma reaches 0.54 to 1.00 of threshold within −6 to +4 ms. That does not show a somatic event is there. "Not frame-rounding artifacts" is supported, because none has a somatic spike within 1 frame after it.

Everything else in the "**Result:**" cells, the Summary, the README and the attempt-record notes matches the printed outputs. That includes the figs12 count of 6 of 11 Fig. 4a–d recordings (cell 71; my round-1 figure of 5 was wrong) and the 1.9 / 1.8 ms delay offsets (cell 34).

**Verification record:** my round-1 reasons appear in my own words, with the relevant problem points appended to each, and the `agrees` flags match my round-1 outcomes. The figs12 reason keeps my wrong count of 5; the response corrects it.

### 3. Round-1 points

**Resolved:**
- **Point 1:** the figure2h and figure2j files are now opened and printed.
- **Point 2:** fig4fg reading (b) has been added. The distal set is now empty for a correct reason (the 1,000 Hz recordings), the search for the Fig. 4g neuron is reported (no recording has 10 trains), and fig4h and figs13 have their own cells.
- **Point 4:** the fig3d conclusion now says P1 covers only part of the claim.
- **Point 5:** the orphan dendritic spikes have been inspected (cell 64).
- **Point 6:** column 1 of the anesthetized recordings has been checked.
- **Points 7, 8 and 11:** a synthetic check of the parabola, a per-branch variant and a baseline variant for fig4d, and a scan of pulse periods for fig1d have been added.
- **Point 10:** this was my error. The exclusion is frames s−2 to s+2, 10 ms in all, which matches the criterion.
- **Point 9:** needed no change.
- **Point 3:** the possible difference in how delays are defined is now stated in the fig4fg conclusion and the Summary.

**Remaining that bears on a conclusion:**
- **a. figs12:** fix the assumption flag and its wording, as in item 1.
- **b. Delay definition (point 3):** the deposited Fig. 2 delays sit about 1.9 ms below the paper's, so the three blocked opto outcomes (fig4fg, fig4h, figs13) and the empty distal readings of fig4bc and fig4ijk depend on how delays are measured. This is disclosed, and I accept "blocked". It also bears on fig2f-conduction-speed, which the claims file makes depend on fig2f-delay-range: the speed reproduces on the same deposited delays whose range does not. The notebook does not discuss that.
- **c. Wording:** the fig4d p-value, the fig4bc "smaller" sentence, the exact-zero check and the fig4ijk "somatic event below threshold" sentence need correcting as in item 2. None of them changes an outcome.
- **d. Still open:** the site set for fig2e and the conduction speed (point 12), and the Fig. 1 pulse series. Both are stated as assumptions and cannot be settled from the dandiset.
