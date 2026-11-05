I've revised the attempt in reply to round 1 and re-run it with `python tools/entry.py all`: 0 errors, 28.5 minutes. The last two clean runs gave identical outputs. Five outcomes changed and nothing is committed.

## Outcomes that changed

| Claim | Verified outcome | Now | Why |
|---|---|---|---|
| fig5e-area-ratio-distribution | partially reproduced | not reproduced | Median (1.226–1.565) and IQR (0.874–1.287) are now outside tolerance everywhere, so the partial rule fails. |
| fig5bc-area-intersegment-variation | reproduced | blocked: methods underspecified | Reading (b) fails with all 14 segments (8461.9 against 9476.5); it holds only where 4 segments keep no cross section. The criterion sends a split to methods underspecified. |
| fig5d-polynomial-closest-area-ratio | partially reproduced | reproduced | 4 of 96 combinations put all three shares within tolerance (for example 70.7 / 20.6 / 8.8%). |
| fig6b-resistance-segmentation-peak | partially reproduced | not reproduced | The median is 5.28e15–6.87e15, never within tolerance. The peak is within in one combination (1.68e15), but the partial rule needs the median. |
| fig9a-heights-taper | partially reproduced | reproduced | One of 48 combinations puts all three peaks within tolerance (1.228, 0.820, 0.305). |

Several reproduced outcomes rest on one combination: fig9a, and ellipse-annulus-underestimate (one P4a combination at erosion 1). fig5d rests on four of 96. The notes say so.

Two claims kept their outcome but on firmer ground:
- **fig6a-resistance-power-law:** the partial rule now also holds with all 14 segments kept, not only under P4a.
- **spline-resistance-five-times:** now reproduced on linear bins under P4b (ratio 6.59, against 6.2).

## What I added or corrected

- **Centerline (problem 1):** I added a table of path length against end-to-end distance (1.28–2.24 times before cleaning) and a vessel projection with the path drawn on it. The path is now cleaned: points farther from the polynomial fit than the vessel radius are dropped, and so are points that revisit a stretch already passed. 7534 of 9564 points are kept. Counts are now 202–604, still not reproduced.
- **PVS in each slice (problem 2):** the PVS is now the two largest regions within one vessel radius of the vessel. Planes that the PVS mask fills edge to edge, at E and F only, are cleared. The notebook shows region counts, the share of PVS within 3 R1 of the vessel, and one example slice per location with the fits drawn over it.
- **Slice centring (problem 4):** the edge distance is now measured from the vessel center in the slice, as the Methods describe.
- **Erosion readings (problem 5):** the fit resistances are now solved at all three erosions, not just 3 pixels.
- **Location D (problem 7):** its whole-plane intensity falls with depth in every channel and its PVS lies above the vessel. So its depth axis is consistent with the other files and was kept.
- **Truncated tables:** the long tables now also print compact summaries and value ranges.
- **Notes on two readings:**
  - fig6a reading (b) is dominated by a few outlier cross sections (problem 9).
  - left-right readings (a) and (b) treat neighbouring cross sections as independent (problem 8).
- **Dataset findings:** I added that the vessel mask of E still holds a network of branching vessels, which the Methods say were removed by hand. I also added a question for the authors about fig5bc.
- **Question for a reader:** I added one to `questions/000491.yaml`. fig5b's criterion allows only linear bins, while fig6b's allows logarithmic bins for the same Figure 6B. On logarithmic bins, two fig5b combinations put all four peaks within tolerance.
- **Record:** round 1 is recorded under `verifications`; the verifier agreed with every outcome it reviewed. Deviations and assumptions are updated, and every tested outcome is now marked as resting on an assumption.

## Not done

- **Overlap pixels (problem 10):** the other assignment of pixels in both masks was not run. 381 of 6683 slices are affected, mostly at J and E.
- **Log bins for fig5b and ellipse-annulus (problem 6):** they stay a variant, as their criteria name only linear bins; that is what the reader question asks about.
- **Location E:** its mask problem remains. The cleaned path follows one branch, and only 29–52% of the PVS in its slices is kept as lobes.
- **Formatting:** writing the record back with PyYAML reformatted the whole file, so its diff is large.

The changes under `tools/` were already in the working tree when I started; I didn't touch them.
