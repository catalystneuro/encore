I wrote `claims/000633/10.3390-ijms241310921.yaml`. The quote checker reports 12 claims, 12 quotes and 0 problems. Nothing is committed.

**Text read:** the published article (open access) from Europe PMC (PMC10341945), with the full Results, Discussion, Methods and figure legends. The paper has no supplement. It links no code, and its data are "available on request", so there was no code to read. There was no PDF.

**Dataset:** the archive title ("The difference in electroporation patterns produced by a train of single pulses and a train of paired pulses", 2 files) matches Figure 4, the YO-PRO-1 dye uptake patterns from the triangular electrode array.

**Claims:** 12, all quoted.
- Figure 2 (4 claims): the 2-fold and 20-fold cancellation at 180°; the crossover at about 160° and 130°; the three-fold facilitation at 90–100° with a plateau down to 0°; and the 60-fold difference at 833 kHz. All four are marked `with_inputs`, because each ROI's angle comes from the paper's field simulation, which was not deposited.
- Figure 3 (3 claims): co- and cross-directional pairs are equal at 1 Hz (an absence claim); co-directional pairs are stronger at 770 kHz; cross-directional pairs are the same at 770 kHz as at 1 Hz (an absence claim).
- Figure 4 (3 claims): the single-pulse pattern follows the field map (`with_inputs`, needs the simulated map); the paired-pulse effect is focused at the apex and weak at the base electrodes; the comet shape.
- Figure 5 (2 claims): the ~10% sawtooth between the base electrodes, and the ~25% polarization near the apex.

**Statistics:** 0 entries. The only test the paper names is the two-tailed Student's t-test in the Figure 3 legend, and its p-values are printed only inside the figure. **Criteria:** all 12 claims have one, and 7 also carry expected values with 10% tolerances.

**Details the paper leaves open, with the readings named for each:**
- **Background:** whether the uptake measured inside the electrode footprints is subtracted before analysis (subtracted, or not).
- **Figure 2 angles:** the 180° value is either the ROI nearest the base or a value read from a fitted curve (Grapher 16 is named, the fit function is not). The crossover comes from linear interpolation or that fit. The "90–100°" value is either the mean of the ROIs in that range or the ROI nearest 95°. The co-directional value for the 60-fold ratio is either the plateau or the ROI nearest 0°. The paper gives no test for the plateau; it is judged against the 270–330% tolerance band.
- **Figure 3 test:** unpaired or paired t-test. The significance threshold is not stated; the conventional p < 0.05 is used.
- **Figure 4 analysis:** the paper never quantifies this figure.
  - "Near" an electrode: ROIs centred 100 µm or 500 µm outside the electrode footprint edge.
  - Agreement with the field map: Spearman rank correlation, or the order of the three electrode neighbourhoods.
  - The "electroporated" region for the comet shape: dye above half, or above a quarter, of its maximum.
- **Figure 5 peak:** the largest excursion over the train, or the mean of the per-pulse peaks.

**Missing from the paper that claims needed:**
- The Figure 3 p-values, printed only in the figure; there was no PDF to read them from.
- The field simulation (Figure 7B,C): it gives the angle for every Figure 2 ROI and the field map for Figure 4A, and it was not deposited.
- The staining and analysis protocol: Methods 4.4 defers it to Kim et al. 2023 (Bioelectrochemistry 149, 108319), which I did not read.
