I wrote `claims/silkuniene-2025.yaml`. The quote checker passes it: 27 claims, 27 quotes, 15 statistical values, 0 problems.

**Text read.** The accepted author manuscript in PubMed Central (PMC12331426, NIHMS2087238), not the version of record. It has full Methods 2.1 to 2.5, Results, Discussion, Conclusion and the legends of Figs. 1 to 7. There is no supplement: PMC marks none and the text cites none. No PDF was supplied, so no figure was seen. The paper links no code, so none was read.

**Datasets.** I mapped each dataset from its title and description on DANDI:
- **001047:** the packet-rate series, Figs. 3 and 4. Its description also names propidium, which the paper measures only in the Fig. 5 series, so the four 0-mm Fig. 5 claims (fits, spot sizes, zones) list it too.
- **001284:** the raised-electrode series, Fig. 5.
- **001277:** the pulse-duration series, Fig. 6.
- **001276:** the burst-number series, Fig. 7.
- **No dataset:** no description names the heating images (Fig. 2) or the field simulation (Fig. 1E). Those two claims list all four datasets and are blocked as data_missing if none holds them. The "sharpest peak of the study" claim also lists all four, because it compares groups across series.

**Counts.** 27 claims, all with quotes and criteria, 8 with statistics and 10 with expected values. I kept the earlier ids, taking Figs. 3 to 5 from the 001047 file, Fig. 6 from 001277, Fig. 7 from 001276 and the heating claim's id from 001276/001277. One claim is new: `fig5b-reversible-beyond-2mm` (Results 3.2), which says reversible electroporation starts about 2 mm from the centre.

**Details the paper leaves open, and the readings named:**
- **ROI positions (O1):** whole-mm steps, or contiguous ROIs. Which ROI side lies along the diagonal and which footprint holds the background are standard choices.
- **Pooling diagonals (O2):** two diagonals averaged at each signed distance, or four half-diagonals (Fig. 4A legend).
- **Fit range where no figure fixes it (O3):** Fig. 6D at ±4 or ±5 mm; Fig. 7 at ±4, ±5 or ±6 mm.
- **Regression points (O4):** individual experiments, which Fig. 4C supports, or group means.
- **Centre to near-electrode ratios (O5):** 6 or 7 mm, and the ratio of means or the mean of ratios.
- **How R is computed (Fig. 3):** Pearson correlation of fit and data, or the square root of R².
- **Number of Bonferroni comparisons (Figs. 4C and 6D):** two readings each.
- **Fig. 6D trend form:** linear (legend) or logarithmic (text).
- **Deviation beyond the fit (Fig. 3):** in a.u. or in % of the peak.
- **"Perimeter" (Fig. 3C):** outermost parallel ROIs, or the ROIs at 6 mm.
- **"Slightly larger" (Fig. 5):** ratio bounds of 1.25 or 1.5.
- **The 2-mm boundary (Fig. 5B):** a gap between data points, or a divergence between the fitted curves.
- **Zone locations (Fig. 5C):** zone 2 at 2 to 4 mm or 3 to 5 mm; a cytoplasm ring of 2 to 4 µm or 4 to 8 µm.
- **Heating images (Fig. 2):** two sets of hue limits, and "near the center" as 1 or 2 mm.
- **Which CT26 groups give "40 to 50 times":** 1 burst only, or 1, 2 and 4 bursts.
- **How 2.3% of the array area is computed:** three readings; only a disk of radius FWHM over the electrode-centre square gives 2.3%.
- **Saturation at 6 bursts:** the 95% confidence band, or the error-bar gap rule.

**Where a claim needed something the paper does not give:**
- **Tests not reported:** several findings come with no test (Fig. 5 raised electrodes, Fig. 6C, saturation, near-electrode suppression). These are judged by the paper's own rule from Methods 2.5, that a gap larger than the error bars means p < 0.05.
- **Fig. 5C:** the nuclear-staining comparison needs the high-resolution images, and the footprint check needs the Hoechst image taken after exposure. The paper names no reference level for that Hoechst check.
- **Slips in the paper:** Methods 2.5 says the Gaussian fit appears in Fig. 6, where it is in Fig. 5. The slope p for Fig. 4C is p<0.001 in the text and p<0.0001 in the legend; both are recorded.

I did not commit anything.
