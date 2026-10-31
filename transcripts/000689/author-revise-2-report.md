I made the round-2 revisions. The final code was re-run with `python tools/entry.py all`: it passed in 28 min, and `check` reports 0 errors. Nothing is committed.

## Outcomes
No recorded outcome changed, as round 2 requires. I proposed two changes under `proposed`, for round 3 to review:
- **fig3k (sucrose increase):** stays `partially_reproduced`; I propose `not_reproduced`. The criterion needs p < 0.05 under every reading, and only 2 of 4 readings pass. Those two are one result, since AUC and mean give the same t and p. The significant result also needs both the per-trial z-score and the trial-averaged regression. The pooled-fit regression gives p ≥ 0.44 and the session z-score p ≥ 0.16.
- **fig4c (photoidentification):** stays `not_reproduced`; I propose `blocked` (`metadata_insufficient`). The block taken as the "fake" session gets a short-latency response from 1353 of 1902 units, so the tagged count does not test the claim. I did not use `format_error`, which the verifier offered, because it is not a valid reason to block a claim.
- **fig5dh (behaviour clusters):** stays `partially_reproduced`, which the verifier agreed with. The reasoning behind it changed:
  - Re-running the same code changed the counts. The criterion's literal reading (raw features, installed defaults) now gives 6 sucrose and 5 shock clusters. The round-2 run had given 7 and 5.
  - The raw-feature counts are not reliable. The 10 largest features carry all the variance; an exact PCA gives 8 and 5, and changing each feature by one part in a billion gives 7 and 7. One earlier run on this same runner gave 7 shock clusters where the others gave 5.
  - I now adopt z-scored features with the installed defaults, which give 7 and 3, and `measured` is now [7, 3].
  - Under every reading one count holds and the other does not, so the outcome no longer depends on the scaling or the defaults.

## Added or corrected
- **New outputs:**
  - The data check now lists everything under `acquisition/` and `processing/`. Confocal PVT image stacks are in **27** files, not 29 as the record said, and are labelled only by depth.
  - Units responding to each light block, out of all units.
  - The number of passing fig3k readings for each z-score method.
  - PCA-solver and tiny-noise checks for both scalings.
  - fig5dh without H08, H10 and H24, the sessions whose pose clock is checked least well: 5 and 4 clusters.
  - The BLAS library details.
- **Text fixes the report listed:**
  - The remaining clock lag is 2.8 to 19.2 s, not 1 to 15 s.
  - H11's video is 426 s longer than its pose; H07, H09 and H10 are 818 to 1528 s longer.
  - The pose clock is off by up to 192 s, not "tens of seconds".
  - The smoothing-window cluster count ranges from 6 to 12 and does not change steadily with the window.
  - The wrong "4 to 6 / 3 to 6" ranges are gone.
  - The README's p = 0.005 sentence is now qualified.
  - The fig3k, fig4c and fig5dh conclusions are rewritten.
- **Findings:** one new finding on the unlabelled confocal images. The unsorted-units, light-block, pose-clock and behaviour-question findings are updated.
- **Round 2 recorded** for all 39 claims. I also added to fig3k's round-1 reason the missing point that cell 19 described the regression backwards.
- `runtime_minutes` is now 29.

## Not done
- No new questions for a reader: round 2 reported no misreading of the claims file.
- The fig4d smoothing window is still open, because MATLAB is not available here.
- I did not run the notebook a third time after the last text edits, because the raw-feature counts can change between runs. I copied the edited text cells into the executed copy; its code cells are identical to the final notebook.
- **Runtime risk:** the notebook now takes about 28 to 29 min, close to the 30 min CI limit, and about 16 min of that is the tsfresh feature step. Earlier runs elsewhere took 19 min.
