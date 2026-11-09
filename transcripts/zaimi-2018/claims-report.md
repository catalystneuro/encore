I wrote `claims/001436/10.1038-s41598-018-22181-4.yaml`. The quote checker reports 14 claims, 12 quotes and 0 problems. Nothing is committed.

**Text read:** the published version of the paper, as served by Europe PMC (PMC5830647), with its Methods, Results, Discussion, figure legends and Tables 1 to 3. The paper has no supplement and no PDF was supplied, but Table 3 is readable in the text. I also read the paper's code at github.com/neuropoly/axondeepseg, commit 7f60132 (2018-02-28, the last commit before publication). The trained TEM model it ships has not changed since September 2017, before the paper was submitted. The code holds the scoring functions but no script that produced Table 3 or Figure 7, and no list of which images were in the test set.

**Claims:**
- **Quotes:** 12 claims have quotes. The other 2 have an `inferred` note because their numbers appear only in Table 3: the mouse Dice and detection values, and the Dice and detection values for the other test images.
- **Statistics:** none. The paper reports no tests or intervals.
- **Expected values:** 11 claims, each number with a 10% tolerance.
- **Criteria:** every claim has one.
- **Testable on this dataset:** 4 claims, all on the mouse TEM images. They are mouse accuracy (0.9451), mouse axon and myelin Dice, sensitivity and precision, myelin Dice below axon Dice, and sensitivity above 93%. All four need the paper's trained TEM model from the repository, so they are marked `with_inputs`.
- **Not testable here:** 10 claims, on the rat and human SEM images, the macaque image, the full rat spinal cord slice and its Figure 7 measurements, because the dataset does not hold those data. The paper says part of its data is in the White Matter Microscopy Database (osf.io/yp4qg) without saying which part.
- **Settled by the code where the Methods are silent:** segmentation with the code's default settings, the thresholds that turn the label images into axon and myelin masks, and the centroid matching used for sensitivity and precision.

**Details the paper leaves open, and the readings named:**
- **Which mouse images form the test set.** The paper gives "8 × 3 mice" but names neither the mice nor their group. Its Discussion says the models were tested on healthy tissue, while the source study (ref. 27) is a cuprizone study and the dataset holds both control and cuprizone mice. The two readings are:
  - every mouse image in the dataset (this includes the model's own training images);
  - the control mice only.

  The outcome must agree under both readings; if they disagree, the claim is blocked as underspecified. Per-mouse results and the cuprizone mice are to be reported separately.
- **Which 8 images per mouse.** If the dataset has more, all of that mouse's images are used.
- **Figure 7 tract boundaries.** The paper shows the spinal cord tracts only as a schematic diagram, so which areas count as each tract is open. Whether isolated areas at the edge of the white matter mask count towards the g-ratio range is also open.

**Missing from the paper that a claim needed:** the identity of the test mice, and the morphometrics code (AxonSeg, a separate MATLAB package, which I did not read). The SEM, human and macaque images are not in the dataset.
