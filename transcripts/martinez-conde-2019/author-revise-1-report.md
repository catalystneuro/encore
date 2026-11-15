I've responded to every point in the round-1 report and re-run the entry: `tools/entry.py all` passes with 0 errors, and the notebook runs in 53 s. I checked every conclusion, the summary, the README and the record against the new outputs. Nothing is committed.

**What changed in the outcomes**
- **table1-s52: partially reproduced → reproduced.** Following point B6, the squares now weight each pixel by how much of it lies inside, so they cover the paper's full 8 × 8 and 16 × 16 DU; before, an "8 × 8" square held only 7 × 7 pixels. With that change, reading (ii)(a), one the claim names, has all five values within tolerance. The maximum gets in by 0.05 (28.86 against 25.39 ± 3.52). The notes say how fragile this is: 4 of 5 with the old squares, 1 of 5 with another Star baseline placement, and only 12 of the paper's 30 Star neurons.
- **Every other outcome is unchanged.** All main numbers moved by less than 0.2 spikes/s. S90 in fig4b-spike-rate-difference is now within its tolerance by only 0.02, and the record says so.
- **fig7c-fold-edge-equivalence stays not reproduced, recorded as borderline.** S40 is 4.3 from 90 against a step of 3.7. Read as "the level nearest 90 or the one next to it", it would pass. The notebook prints both readings, and the record keeps the distance reading as a stated choice and logs the verifier's objection.

**What I added or corrected**
- **Fields of the map files:** `norm` is 0 in every file, and `smoothed_image_norm` is the map minus BaseActivity, in some files also divided by its maximum. No field holds spike counts or eye time, so spikes-per-condition stays blocked.
- **Zero pixels in the baseline squares:**
  - The one eye time map is stored only at pixels with spikes, so it cannot show which pixels were looked at.
  - The files' BaseActivity agrees better with baselines that keep the zero pixels (Star r = 0.953 against 0.809), so they stay in and leaving them out stays a variant.
- **Star:**
  - The stimulus has the same orientation in every file and differs only in screen position, so it cannot show which diagonal was aligned with each neuron. The 15 unregistered neurons stay out.
  - Their screen maps do not differ detectably from those of the 12 kept (rank sum p 0.41 to 0.63), but the 12 include both monkey A Star neurons.
  - Warped onto the analysis frame, the Star stimulus is at 48 to 50% luminance at the fold midpoint. The S40 fold is 100 DU long, as the Methods imply.
- **fig7a:** the cell now prints the stimulus gray range, the black (0) stimulus beside the Edge, and the 16 × 16 windows at 0, 50 and 100%. The text says the reading (a) fit is degenerate and its parameters mean nothing.
- **Other added output:**
  - fig6 now also runs reading (ii): 0 of 4 tests significant.
  - neuron-counts now prints the check that the 5 spreadsheet rows with no condition marked match the missing neurons in number.
  - fig7c's garbled sentence about a refit is replaced.
- **Questions for a reader:** a new file, `questions/martinez-conde-2019.yaml`, holds the three claims-file points the verifier raised (its point B9):
  - Table 1 rules out reading (a) of fig7c, and "one step" is ambiguous.
  - The stale note in the claims file's checks block about averaging the two S40 folds.
  - The paper's 160 DU Star ROI against the Star's 150 DU radius.
- **Record:** I added a `paper_inconsistency` finding for the Star ROI size and updated four findings. The round is recorded under `verifications`, with the verifier's reasons in its own words and my replies under `response`.

**What I did not do**
- **Baseline placement:** I kept the rule of choosing, for each stimulus, the placement closest to the files' BaseActivity. It is stated as an assumption, the rule itself uses nothing but that agreement, and every placement is still shown.
- **The 15 Star neurons:** I did not register them. Lining their maps up with the stimulus would mean choosing a rotation from their responses, which builds in the very result being tested.
- **Contrast in cd/m²:** I did not compute it with an assumed black level. The paper gives only 14.07 cd/m² at 50%, and on a linear scale starting at 0 the ratio is the same as on gray levels.
