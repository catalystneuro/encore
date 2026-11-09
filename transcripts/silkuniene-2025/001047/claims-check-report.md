The claims file for DANDI:001047 is ready for an attempt. I made nine corrections from the paper and recorded them under `checks` with `ready: true`. Nothing was committed or pushed.

**Checker result** after my edits: `20 claims, 20 quotes, 15 statistical values, 0 problems`. It gave the same result before the edits.

**Changes, by claim**
- **fig2-heating**: the paper says "approximately 2-mm zone". The file allowed up to 2.5 mm with no reason given, so I changed it to 2.2 mm, the default 10% tolerance. The file also set "near the center" to 2 mm, which the paper doesn't give; it is now an open detail with two readings, 1 mm and 2 mm.
- **fig4b-near-electrode-decline**: the file said the power-law fit used the plotted means, which the paper doesn't say. Fitting to the group means and fitting to individual experiments are now both readings.
- **fig5-raised-electrodes-weaken-centre**: the text cites "practically no YP staining near electrodes" to Figure 4, as a premise. The statement now says so. I removed a 10% near-electrode threshold that the reader had made up; that part is judged by fig4b-40-fold-ratio.
- **fig5b-gaussian-pr-lorentzian-yp**: the paper says "left panel of Fig. 5B", not "0-mm data". The statement now says that, and treats the 0-mm panel as one reading.
- **fig5c-nuclear-yp-centre**: the file put zone 3 at 3 to 6 mm from the centre. Results 3.2 and the Figure 5C legend put it across an electrode wall, so it is now the band just outside a wall. Zone 2 is not placed by the text and now has two readings.
- **fig6b-900ns-peak-not-significant**: the paper doesn't say how many comparisons the Bonferroni correction covers. The criterion now runs both two comparisons and all three pairs.
- **fig7be-peak-grows-with-bursts**: judging saturation by the fit's 95% band is a choice made by the reader, since the paper gives no test of saturation. The criterion now says so.
- **fig7-sharpest-one-burst**: "sharpest peak seen in this study" covers every experiment set, so I added set S2 (Figure 5) to the comparison.

**Still open** (each is named in the file as a reading or a standard choice)
- **fig5ab**: the paper puts no number on "slightly larger". The ratio bounds of 1.25 and 1.5 are readings, not the paper's.
- **Other choices the paper doesn't fix**: the hue limits for the heating film (fig2), the deviation measure and Spearman trend (fig3-tail), and the cell segmentation (fig5c).
- **fig6d**: the text says "logarithmic fit" and the legend says "best linear fit", so both are run.
- **Figures not seen**: there is no PDF, so ROI positions, the full list of packet rates tested and the zone locations rest on the text alone.

Every main finding has a claim, and all claims come from this paper.
