I wrote `claims/000875/10.1016-j.bioelechem.2023.108437.yaml`. The quote checker passes: 16 claims, 16 quotes, 2 statistical values, 0 problems. Nothing is committed.

**Text read.** The PMC author manuscript (PMC10247516, NIHMS1891360), which is not the version of record. It has the full Methods, Results, Discussion and figure legends. There is no supplement (PMC lists none and the paper cites none), and no PDF, so no figures were read. The paper links no code or data repository, so no code was read. The dataset's description on DANDI matches the Fig. 6 experiment (number of packets).

**Claims.** 16 claims:
- **Quotes:** all 16 have one; none rests on an inferred reading.
- **Statistics:** two entries. Fig. 4 has p < 0.001 (each bipolar signal against the unipolar pulse) and Fig. 8 has p < 0.01 (packets 1 and 3 against packet 2 near the electrodes).
- **Criteria:** all 16 have one; 11 also carry expected values with tolerances.
- **Coverage:** Fig. 3 (the field simulation), Fig. 4 (cancellation in single cells), Figs. 5A and 5B/C, four claims on Fig. 6, Fig. 7A and 7B/D, three on Fig. 8 including the Discussion's claim that cancellation predicts targeting, and two on Fig. 9.
- **Absence:** one claim, that targeting does not depend on amplitude (Fig. 7). It is judged on the paper's two-sided Student's t-test.
- **Data:** the Fig. 3 claim is marked `with_inputs`; all others use the dataset.

**Details the paper leaves open, and the readings named.** The shared ones are set out in the file's opening comment.
- **ROI layout:** all 92 or 224 ROIs on one diagonal (about 36 or 33 µm apart), or half on each diagonal (about 72 or 65 µm apart).
- **Background:** raw intensity, or intensity minus a cell-free or dark offset.
- **Center:** the ROI nearest the geometric center, or the highest ROI between the two minima on either side of the center.
- **Periphery:** the outermost ROIs pooled across the ends, or each end on its own.
- **Normalization order:** normalize each dish and then average, or normalize the mean profile.
- **LOESS span:** not given. Criteria use the ROI values; fits with spans 0.25 and 0.5 are shown as variants.
- **Fig. 6 setup:** the array used and the first-pulse voltage are not stated. The author takes them from the images.
- **Peak width (sharpness):** not defined. Readings are the full width at half height above the trough, or the distance between the two minima.
- **"Least affected area":** the mean of the two side minima, or each side alone.
- **Single-cell test (Fig. 4):** Methods 2.2 names none. The Student's t-test from Methods 2.4 is used, with Welch as a variant.
- **"Near the electrode" in the simulation:** how far from the electrode it is measured is not given.

**Problems in the paper itself**, both recorded in the criteria:
- Section 3.4 says "~120 a.u. for packet 1", which contradicts its own sentence. I read it as packet 2, as Fig. 8B and the Discussion imply.
- Section 3.4 puts the cancellation of the other two signals at "4–5-fold", but the paper's own Fig. 4 numbers give 6.1 for the 4-phase signal (and 5.0 for the delayed one). The ratio is reported beside the range.

**Missing that a claim needed.** The Fig. 3 claim can only be tested with a Sim4Life model of the arrays, and the paper deposits none; it points to reference 15 for the setup. The small array's geometry, the medium conductivity and the solution depth are not given.
