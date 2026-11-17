I finished steps 1 to 6 for DANDI:000489 (Kim et al. 2022). The entry locks, checks with 0 errors and runs from a clean environment in 519 s, and the handover is built. None of the 22 claims was reproduced in full: one partially, four not reproduced, one blocked on method, 16 blocked for missing data.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig2a-uptake-rises-with-field | partially reproduced (assumed): 3 of 5 amplitudes pass the strongest-against-weakest test; unipolar (2 dishes) and 25% do not |
| fig2a-vertical-scales | not reproduced (assumed): the 75% mean + s.e.m. is 283 a.u., above the 250 limit |
| fig2b-exponential-same-slope | blocked, methods_underspecified: the criterion's 12 readings disagree (10 not reproduced, 2 partial) |
| fig2c-max-inhibition-50-75 | not reproduced (assumed): 54.5% (mean) or 31.6% (lowest) of unipolar, not ~20%; no test reaches p < 0.01 |
| fig2c-inhibition-flat-above-8-7 | not reproduced: the percent rises toward 8.7 kV/cm, significant under both pairings; every variant agrees |
| fig2c-weaker-at-6-7 | not reproduced (assumed): the unipolar mean at 6.7 kV/cm is −8.6 a.u. (background). The bottom side alone, or the left footprint alone, gives reproduced |
| 16 claims on Figs. 1E and 3 to 7 | blocked, data_missing |

## 2. Dataset, assumptions, questions

What I found about the dataset:
- **Contents:** only the 17 Fig. 2 dishes and a Fig. 1F sample. Each file is one stitched 2-channel uint16 image. There is no pixel size, ROI, field per ROI, footprint values or voltage.
- **Duplicate:** the YP channel of `sub-Fig2-0-03` (unipolar) is identical to that of `sub-Fig2-25-04`. Phase correlation shows the image belongs to 25-04, so the unipolar group has 2 dishes. The main analysis leaves 0-03 out; a variant keeps it.
- **Fig. 1F file:** both channels are the same image.
- **Storage:** the images are ImageSeries of shape (22323, 22323, 2) with a 2 Hz rate, so the first axis reads as time. The three 25% files share the acquisition name `Fig2_25`.
- **Description against paper:** 144 tiles of a six-well-plate well, where the paper says 216 tiles of a 35 mm dish.
- **Days:** all unipolar dishes are from 2021-07-29 and all 75% and 100% dishes from 2021-08-24. The 100% dishes show more uptake than unipolar (761 against 571 a.u.).
- **Scale:** 0.65 µm/px fits the geometry: electrode centres 4.54 mm apart and footprints 1.49 mm across, against 4.5 and 1.5 mm in the paper.

I pinned 0.230518.1811: the paper cites no version, and the draft holds the same files.

Assumptions:
- ROI are 200 µm squares tiled along bb', with the two sides averaged (the claims file's reading a).
- YP_0 and MB_0 are averaged over both footprints.
- Pixel size is 0.65 µm.
- The field is recomputed in closed form for two cylinders (exact in 2D, since the electrodes span the full liquid depth). It gives 15.38 kV/cm at the centre, against the paper's 15.1. I listed it under `inputs`.
- The files' camera counts are the paper's a.u.

Every claim is also shown on one side only, with the scale set from the electrode distance, with each footprint alone, and with 0-03 kept.

Five questions for the paper's authors are recorded as a `methods_unavailable` finding: ROI placement, which footprints, the Fig. 2B fit method, t-test pairing and the comparison behind p < 0.01, and the field values. I asked a reader nothing.

## 3. Protocol points
1. **Same exposure, other dishes.** The Fig. 2 dishes had the same 600 ns exposure as Fig. 4, but they are other dishes. I kept Figs. 4 and 5 blocked and showed their measures on the Fig. 2 dishes in a section that decides no outcome.
2. **The clock check** assumes time series and does not apply to single images. I said so in the notebook.
3. **Readings from both sources.** The claims file's readings multiply with the protocol's step 1.6 readings (ROI side, footprint). Where they changed the outcome, I adopted the best-supported reading and marked the outcome `assumed`.
4. **Recomputed inputs.** The protocol does not say whether a field recomputed from the paper's geometry counts as outside data. I kept `data: dataset` and listed it under `inputs`, citing the paper.
5. **Speed advice.** "Develop on a subset" does not cover a CPU-bound load. I cached the reduced data in a temporary directory during development only, and the notebook streams everything.

## 4. Runtime
The run took about 1 h 20 min (15:31 to 16:51 UTC); the notebook takes 8.7 min. Nothing failed in the final runs. During development, one range request was reset (I added retries) and a newline escape broke a notebook cell (fixed).

Files are in `entries/000489-kim-2022/`:
- reproduce_kim_2022.ipynb
- bipolar.py
- README.md
- entry.yaml

The attempt record is `attempts/000489-kim-2022-01.yaml`.
