I wrote `claims/000631/10.3390-ijms241310921.yaml`. All 12 quotes pass `tools/claims_check.py` and the file validates against `schemas/claims.schema.json`. Nothing is committed.

**Text read:** the version of record from Europe PMC (PMC10341945): full text, Methods and figure legends. The paper has no supplement, and no PDF was supplied. It links no code (data are "available on request"), so no code was read. The dataset's DANDI description names the Figure 2 experiment: the angle dependence in the triangular array.

**Claims:** 12 findings, all with quotes, none inferred.
- **Figure 2 (5 claims):** about 2-fold weaker uptake at 180° at 1 Hz and 20-fold at 833 kHz; paired and single pulses equal at about 160° and 130°; about 3-fold enhancement at 90–100° with a plateau down to 0°; the effect depends on frequency; a 60-fold co/counter difference at 833 kHz.
- **Figure 3 (4 claims), Figure 4 (1) and Figure 5 (2).**
- **Statistics:** 0 entries. Figure 2 reports only mean ± s.e. (n = 3) and no test. Figure 3 names a two-tailed Student's t-test, but its p-values are printed only in the figure. The schema needs a p-value, so none could be recorded.
- **Criteria:** all 12 have one. 7 also carry expected values with 10% tolerances, or 81–110° for the "90–100°" range.

**Details left open, with the readings named:**
- **Background:** (a) raw ROI intensity, or (b) intensity minus the electrode-footprint uptake. Both are run; the claim is blocked if they disagree. For the "no difference" claims of Figure 3, (b) decides.
- **MemBrite normalization:** not stated. Run as a variant only.
- **Figure 2 percent of control:** (i) ratio per experiment, then the mean, or (ii) ratio of the means. These are readings of the reported numbers.
- **ROI angles:** they come from a Sim4Life simulation, and the paper gives neither the values nor the electrode spacing. Readings: (A) angles held in the dataset; (B) a 2D model with finite-radius cylinders, using electrode positions measured from the images; (C) the same with line sources. If (B) and (C) disagree, the claim is blocked; with no positions at all, the Figure 2 claims are blocked.
- **ROI spacing and end points:** use the dataset's ROIs; otherwise 32 contiguous ROIs, recorded as a deviation.
- **Which control electrode was energized:** mirror-symmetric along the bisector, so it cannot change the outcome. Averaged.
- **"At 180°":** the ROI nearest the base, or the minimum. The plateau level is the mean over 90–100° or from 100° down. The plateau test is (P1) a slope whose 95% CI includes zero, or (P2) the values near 0° within 10% of the level. The 60-fold ratio is the end ROIs, or the paper's own arithmetic of 3 × 20.
- **Figure 3 t-test:** alpha 0.05 (conventional); unpaired, with Welch's test as a variant.
- **Figure 4 "near":** ROIs touching the electrode edge, or 200 µm farther out.

**Missing from the paper:**
- The Figure 2 curves and the Figure 3 bar heights and p-values (no PDF).
- The Sim4Life angle values and the electrode spacing.
- Reference 17 (Kim et al. 2023, Bioelectrochemistry 149:108319). The Methods defer to it for the analysis details, including the background correction. I did not read it.

The checked files for this paper's sibling dandisets (000632, 000633) were already in the repo. I read 000632 and kept the corrections its checker had made.
