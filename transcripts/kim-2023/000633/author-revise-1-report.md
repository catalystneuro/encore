No outcome changed in this round. I recorded the verifier's report as round 1 under `verifications`. I kept fig4-comet-shape as reproduced, resting on an assumption, and recorded that the verifier disagrees: it would give partially_reproduced. The entry re-runs cleanly (`tools/entry.py all`: pass in 211 s, 0 errors) and `check` passes.

**Outcomes:**

| Claim | Outcome | Verifier |
|---|---|---|
| fig4a-single-pulse-follows-field | reproduced, resting on an assumption | agrees |
| fig4bc-paired-pulse-focal-apex | reproduced | agrees |
| fig4-comet-shape | reproduced, resting on an assumption | would give partially_reproduced |
| 9 claims from Figures 2, 3 and 5 | blocked, data missing | agrees |

**What I fixed or added, by problem in the report:**
- **Which electrode is E1 (problem 2):** it no longer comes from the uptake. The paper's Figure 4A labels E1 at the lower right with the apex at the top, and the deposited image has the same orientation, so E1 is `base_a`. To check this I viewed the published figure from PMC outside the notebook; the notebook cites the figure and its legend. What remains assumed is that the image is not mirrored. Both assignments are still shown.
- **The comet maximum (problems 3 and 7):**
  - The notebook now shows the object under the maximum at full resolution in both channels. It is a blurred disc about 105 µm across, bright in YO-PRO-1 and MemBrite alike (14577 and 5266, against 305 and 255 around it), and not saturated. It is most likely debris above the cells.
  - Objects with MemBrite above 10 times the dish median are now left out (0.54% of the region). The literal maximum after that is 1063, and the claim passes at half and at a quarter of it. Thresholds of 5 and 20 times give the same result, as do the two other robust maxima.
  - The 200 µm smoothing now uses only pixels outside the electrode footprints and the image corners.
  - With the object kept, the region is empty and the claim fails. The notes say so, and the disagreement is recorded.
- **Single-pulse file identity (problem 1):** the header, data check, notes and deviations now say that fig4a and fig4bc rest on this file being Figure 4A, although its session description gives a different exposure.
- **Spearman p-values (problem 4):** I added the test on ROIs thinned to 1 and 2 mm spacing.
  - With E1 = `base_a`, p is 2.7e-8 or less at 1 mm spacing.
  - At 2 mm spacing p is below 0.05 in 8 of 10 variants. In the other two it is 0.095, with only 12 ROIs left. This is written into the result.
- **Neighbourhood width (problem 8):** I added a 250 µm neighbourhood and print each neighbourhood's mean in every variant.
- **Footprint fits (problem 5):** a new figure shows every fitted footprint up close.
- **Other records:** new helpers in `swing.py` (`thin_rois`, `load_crop`, `debris_mask`, `masked_mean_filter`); a new dataset finding about the bright object; an updated question to the paper's authors; README text updated.

**Not done:**
- No question was added to `questions/000633.yaml`, because the verifier found no place where the claims file misreads the paper.
- Nothing in the data can settle whether the single-pulse file really is Figure 4A, or whether the image is mirrored. Both remain questions for the paper's authors in the findings.
