No outcome changed. The verifier agreed with all 17 outcomes, and after the re-run fig6a is still reproduced, fig6b and the trough claim are still partially reproduced, fig6-peak-narrower is still reproduced, and the other 13 claims are still blocked because their data are not in the dandiset. The entry ran cleanly twice with `python tools/entry.py all` (check: 0 errors). Both runs gave the same numbers. Round 1 is recorded under `verifications` for all 17 claims, and nothing was committed.

**The one finding that affected a conclusion: the fig6b background.** The verifier was right. Full-resolution crops show a faint layer of cells inside the electrode footprints. Their level is 0.74 to 0.94 of the cell layer outside the array, so the footprint median is not the "cell-free or dark offset" the claims file allows for reading b2.
- b2 now subtracts a dark offset estimated from each image, in two ways:
  - **b2-dark:** the darkest 1% of each image, 73.5 to 87.1 counts. Almost all of those pixels lie outside the circular edge of the dish's glass bottom, where no cell layer is in focus.
  - **b2-min:** the darkest pixel near the array, 110 to 200 counts.
- The old footprint reading is kept only as a variant (b2-fp) and counts towards no outcome.
- fig6b stays partially reproduced, now in 13 of 108 combinations: 5 under b2-dark and 8 under b2-min. All of them use a single diagonal and take the peak as one ROI, as the verifier predicted.
- The result is fragile, and the notes say so:
  - Per dish, 1Px4 ranges from 75–145% in dish 24 to 170–380% in dish 23.
  - Subtracting any common offset of 50 counts or more reaches 180%.
  - With both diagonals and the central ROIs, it stays below 155% for offsets up to 300 counts.
- Because the offset is an estimate (the files hold no dark frame), fig6b is now marked as resting on an assumption (`assumed: true`).

**Outputs added at the verifier's request:**
- the array area of each dish at higher resolution, with the fitted electrode circles and ROI lines;
- a footprint crop per dish, and full-resolution patches of the footprint and of the cell layer outside it;
- intensity histograms of the footprint, the cell layer outside the array and the area between the electrodes;
- where the darkest pixels lie;
- per-dish profile plots;
- per-dish values for every partial fig6b combination;
- the 1Px4 value as the subtracted offset grows.

**Other points:**
- **Pixel size:** I kept the assumed 0.65 µm per pixel. A new check shows the paper's 8.4 mm diagonal must be measured between needle edges, because measured centre to centre it leaves less room than the large array's own ROIs cover. That reading implies about 3.8 mm for the small array. At 0.65 µm the images give 3.73 to 4.05 mm. At the verifier's 0.53 µm there is too little room between the footprints for the paper's 3.30 mm of ROIs.
- **fig6-peak-narrower:** the second width measure (the distance between the two minima) is now counted once per combination, so it decreases in 71 of 108. Rows normalized each way are counted separately, and the text now says the unsmoothed first width depends on how the centre is read.
- **Counts that changed:** with three background readings instead of two, the combination counts changed. fig6a is reproduced in 72 of 162 and partial in the other 90, with only the periphery test failing. The trough claim is partial in 79 of 216 and never reproduced, and 10Px4 is never within tolerance. The notes, conclusions, summary and the questions-for-authors finding were updated to match, and the runtime was raised to 5 minutes.

**Not done:**
- No question was added to `questions/000875.yaml`, because the verifier reported no place where the claims file misreads the paper.
- I did not use the camera maker's nominal 100-count dark offset. The images have blocks darker than that (as low as 58 counts), so that offset cannot be read from these files.
- The changes already present in `tools/` were there before this run, and I left them alone.
