I've done steps 1 to 6 for DANDI:000631, pinned at version 0.231012.1508. The entry passes `python tools/entry.py all`, and the handover package is built in `executed/000631-kim-2023/handover/`. Nothing is committed. Four claims are reproduced or partially reproduced and two hold only in part; the 60-fold claim is blocked by the claims file's own rule, and the six Figure 3 and Figure 5 claims are blocked because their data are not in the dandiset. The new files are the entry `entries/000631-kim-2023/` (notebook, helper `swing.py`, README, lock), the record `attempts/000631-kim-2023-01.yaml` and the reader question `questions/000631.yaml`.

**1. Outcomes**

| Claim | Outcome | Key numbers (layout L2, background subtracted) |
|---|---|---|
| fig2-180-cancellation | partially reproduced (assumed) | 1 Hz: 2.42 to 2.51-fold (expected 2 ± 0.2). 833 kHz: 11.8 to 22.0-fold (expected 20 ± 2). The two values never both match under one layout; without subtraction, 1.3 and 3.4-fold at most. |
| fig2-crossover-angle | reproduced (assumed) | 145.3 to 149.6° at 1 Hz (expected 160 ± 16), 124.1 to 125.9° at 833 kHz (expected 130 ± 13), under all 16 readings |
| fig2-facilitation-plateau | partially reproduced (assumed) | About 2.8-fold plateau from about 95° at 833 kHz; at 1 Hz there is no plateau and uptake keeps rising as the angle falls |
| fig2-frequency-dependence | reproduced (assumed) | Holds under all 16 readings |
| fig2-60-fold-co-counter | blocked, `methods_underspecified` | With subtraction, 51.5 to 61.6-fold on one reading; without it, 3.6 to 5.8. The claims file blocks a claim when the two background readings disagree. |
| fig3 (4 claims) | blocked, `data_missing` | No square-array data in the dandiset |
| fig4-unipolar-pattern | reproduced (assumed) | Holds under all 8 readings and in every dish |
| fig5 (2 claims) | blocked, `data_missing` | No FluoVolt strobe data in the dandiset |

**2. The dataset**

- **What it holds:** 15 files, each one stitched two-channel image (MemBrite and YO-PRO-1). There is no pixel size, and no electrode positions, ROIs, angles or measured values.
- **What I built in their place:** electrodes are found from the dark footprints in each image by fitting a rigid triangle. The same triangle (s.d. under 0.08 mm) appears in every dish. Angles come from the claims file's two field models, B and C, which give the same outcomes.
- **Duplicate:** BPAE-03 and BPAE-18 of 7-31-21 are one recording deposited twice (identical chunks and start time). I counted it once.
- **Mislabelled file:** BPAE-13 of 8-24-21 carries the description of a two-electrode bipolar experiment. Its image shows the triangular array and the paired-pulse pattern, so I used it as a paired dish.
- **Wrong description:** every file's image description says "144 images in a 12x12 grid from a six-well plate", which does not fit the paper's 35 mm dishes.
- **Controls:** there are five unique 1 Hz controls from two days, and the paper does not say which were used. With only the two controls from the paired dishes' day, the 1 Hz crossover angle moves to between 130.5 and 161.4°.
- **Assumptions:**
  - A pixel size of 0.65 µm, from the camera and 10x objective. It is consistent with the needle footprints, the base-to-apex distance and the stated 5 to 10 kV/cm.
  - ROI layout L2: 32 contiguous 200 µm ROIs from the apex footprint back past the base midpoint. The claims file's standard layout does not fit (5.37 mm available against 6.4 mm needed).
  - Which base electrode was energised in the single-pulse dishes is taken from the uptake.
- **Questions for the paper's authors** (a `methods_unavailable` finding): where the ROIs were placed, how the angles were obtained, how the footprint correction was applied, which control dishes were used, and the pixel size.
- **Question to a reader:** whether "no background correction" is a reading the paper allows. Methods 4.4 says the footprints were measured "to account for" spontaneous uptake. This reading alone blocks the 60-fold claim.

**3. Where the protocol was unclear**

1. A criterion's reading (no background correction) cannot reach the claimed ratios, yet it blocks a claim. The protocol gives me no way to set it aside, so I asked a reader and applied the criterion as written.
2. Most criteria define only "reproduced" and "blocked". When a criterion fails under every reading, I chose between partially and not reproduced from the protocol's outcome definitions.
3. The schema forbids `assumed` on a blocked outcome, although step 1.6 says outcomes resting on a choice are marked. I put the layout assumption for the 60-fold claim in its deviations and notes.
4. `measured` says "the first reading listed when several match", which says nothing for the case where none match. I recorded L2, subtracted background, normalisation (i), reading (1). The plateau claim has one expected angle but two frequencies, so I recorded 1 Hz and gave 833 kHz in the notes.
5. Step 2's clock check assumes time series; these are still images. I checked instead that each image's uptake pattern matches its condition label.
6. Where a criterion says "under one normalisation at least" over two frequencies, I required both frequencies under the same normalisation.
7. The claims file's standard ROI layout is geometrically impossible here. I handled it under step 1.6 by running two layouts and adopting the better-supported one.
8. There is no guidance on assuming a calibration the files lack, such as pixel size. I recorded it as an assumption, checked three ways.

**4. Runtime and failures**

The run took from 03:10 to about 03:57 UTC. The notebook runs in 3.2 minutes and streams all 18 GB into memory without writing to disk. One `entry.py all` failed on a schema rule (point 3 above) and passed after the fix. Nothing else failed. Some untracked files at the repository root (`.bashrc`, `.idea`, `scripts` and others) are sandbox mounts, not mine, and I left them alone.
