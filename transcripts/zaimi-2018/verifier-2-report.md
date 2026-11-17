**Round-2 verification: zaimi-2018-01 (AxonDeepSeg on DANDI:001436 0.250512.1625)**

Counts come from the claims file and the attempt record. The claims file has 15 claims, and the record has 15 outcomes: 7 reproduced and 8 blocked. Of the blocked ones, 1 is methods_underspecified and 7 are data_missing. No outcome in the record carries `assumed: true`.

## 1. Outcomes

| Claim | Record | Agree? |
|---|---|---|
| osf-group-labels-link | reproduced | Yes. Cell 16: 20 of 20 mice are in exactly one group folder, at most 3 per folder. Cell 17: 16 of 16 counterparts are the same mouse (r 0.593 to 0.903), and the largest other r is 0.487. |
| table3-tem-mice-accuracy | reproduced | Yes. Cell 22: 0.9416 (a) and 0.9349 (b); all 1140 sets of 3 mice give 0.9226 to 0.9683. |
| table3-tem-mice-dice-detection | reproduced | Yes. Cell 26: 4 of 4 within tolerance under both readings and over every set of 3 mice. |
| myelin-dice-below-axon-dice | reproduced | Yes. Cell 29: holds for the means and for 158 of 158 images. |
| sensitivity-above-93 | reproduced | Yes. Cell 32: 0.9863 and 0.9878; the lowest set of 3 mice gives 0.9722. |
| table3-sem-rat-accuracy | reproduced | Yes, if one accepts that these are the paper's images. Cell 37: 0.8955 and 0.8757, both within tolerance. Cell 35: the two images match Table 1's test rows on pixel size, field of view and fixation, which is strong. But the outcome rests on that identification, which is not flagged as an assumption. Also, Rat 1 at 0.8955 lies outside the statement's "between 85% and 88%", though inside tolerance. The record does not mention this. |
| table3-sem-human-accuracy | blocked, data_missing | Yes. |
| table3-tem-macaque-accuracy | blocked, methods_underspecified | I now accept this outcome (round 1: not reproduced). The criterion is "as in table3-tem-mice-accuracy", and that criterion blocks when readings differ in outcome. Cell 44 shows they do: 1 of 7 images is inside. The one passing reading, sample 3, clears the lower bound by only 0.004 (0.7634 against 0.7594). Its sensitivity of 0.316 and precision of 0.525 do not support a match either. |
| table3-other-samples-dice-detection | blocked, data_missing | Yes. Cell 50: rat 8 of 8 within tolerance; macaque 0 of 7 on every measure. |
| macaque-myelin-underestimated | reproduced | Only if flagged as an assumption. Cell 47 shows 7 of 7 below the ground truth. But the result rests on the OSF masks being the paper's ground truth, which the record itself calls "probably not" the paper's (cell 45 and the macaque notes). The same masks are why the accuracy claim is blocked. Treating the masks one way for one claim and the other way for the other is inconsistent. The outcome should carry `assumed: true` with that assumption stated, or be blocked on the same grounds. |
| full-slice-processing-time and the 4 fig7 claims | blocked, data_missing | Yes. Cell 53 lists two OSF candidate panoramas, and the paper gives no way to tie either one to its slice. |

**Unflagged assumptions.** Two outcomes rest on assumptions that are stated in the notes but not marked `assumed: true`:
- table3-sem-rat-accuracy assumes the AxonDeepSeg SEM dataset images are the paper's test images. This is reasonable given the Table 1 match.
- macaque-myelin-underestimated assumes the OSF masks are the paper's ground truth. The author's own text disputes this.

**Claims file: still reported, not corrected.** The macaque-myelin-underestimated criterion tests direction only and drops "slightly". The observed ratio is 0.352 to 0.512 (cell 47).

## 2. Sentences the outputs do not support

- **Network check figures.** Cell 8 prints a largest difference of `1.2159347534179688e-05`. Two sentences contradict it:
  - Attempt record, table3-tem-mice-accuracy deviation: "differs from the model's own saved graph … by at most 9.1e-06".
  - Summary, cell 55: "its output matches the model's own saved graph to within 1e-5 on a test image".
- **Human SEM images.** Cell 52 and the record's table3-sem-human-accuracy notes say the PolytechniqueMontreal/Human images "are at 0.23 um". No cell prints that folder or its pixel size.
- **README.** It leaves out results that bear on two rows:
  - "Dice, sensitivity and precision of the rat, human and macaque rows of Table 3 | Blocked: data missing (human image); the rat values are within tolerance" omits that all 4 macaque values fail on all 7 images (cell 50). The Summary in cell 55 does say so.
  - "Myelin is underestimated on the macaque image (data elsewhere) | Reproduced" omits that the underestimate is not slight and carries little weight (cells 47–48).
  - "linked by mouse number and checked by image content" overstates the check: only 8 of 20 mice were confirmed by content, and 9 are linked by number only (cell 17).
- **Smaller points:**
  - The record's inputs say the mouse micrographs are "dated 2017-03-03 and 2017-03-06", but no output prints the dates of those files.
  - Cell 45 and the macaque notes cite the SEM rat reproduction as evidence the pipeline is sound. That is weak evidence for the TEM path, since the SEM model is different and is run without the inversion. The better evidence, the mouse TEM reproduction, is not the one cited.
- **Everything else checks out.** All other Result sentences, the Summary and the record's notes match the printed numbers. This includes cells 18, 24, 27, 30, 33, 38, 45, 48 and 51, the training-row match in cell 38 (6 of the other 8 images), and the pooled confusion fractions in cell 44.
- **My round-1 reasons in the verifications block.** They are stated faithfully and in substance in my own words, for all 15 claims, including the 0.62 myelin-Dice bound, the "slightly" point and the resize-and-cast point.

## 3. Status of my round-1 points

**Resolved:**
- **2, ground truth not the paper's.** It is now stated in the header and the data check. The filled-delineation variant moves accuracy by less than 0.002 (cell 22) and myelin Dice by +0.003 to +0.004 (cell 26).
- **5, inference only partly verified.** Cell 10 prints the original `resize` followed by `astype(np.uint8)` (apply_model.py, lines 418–421) and the scikit-image 0.13.1 default of order 1, so the helper follows the original code. The SEM network check (8.3e-06) and the nearest-neighbour variants (cells 37 and 44) show the resize step does not drive the results. There is still no end-to-end run, but that does not bear on any conclusion.
- **8, code comment.** Fixed in cell 17.

**Acknowledged and unchanged; none affects a conclusion:**
- **1, leakage.** Covered by the sweep over all 1140 sets of 3 mice.
- **7, link by number.** 8 of 20 mice confirmed by content; the cuprizone point is now in the conclusion.

**Remaining issues that bear on a conclusion:**
- **3, which macaque image and masks.** Cells 41–44 add the OSF description (nothing on which image), confusion matrices and a nearest-neighbour variant. Whether the OSF masks are the paper's is still unknown, and it decides both macaque outcomes. My view has changed: the accuracy claim is properly blocked, but macaque-myelin-underestimated then needs `assumed: true` or the same block.
- **4, "slightly".** A question to a reader is filed, and the outcome is still decided by direction alone. This is a claims-file issue.
- **6, Fig. 7 candidate panoramas.** Still not run; a second candidate (RatSpinalCord2017, 0.13 µm) was found. Blocked is defensible, since neither panorama can be tied to the paper.
- **New.** The 9.1e-06 and "within 1e-5" statements contradict cell 8. They do not change any outcome but should be corrected.
