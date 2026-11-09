I checked and corrected `claims/mizuseki-2009.yaml`, and the file is ready for an attempt. Nothing is committed or pushed.

**Checker result line:** `claims/mizuseki-2009.yaml: 37 claims, 35 quotes, 13 statistical values, 3 problems`. All quotes pass. The 3 problems are three p < 10^-4 values in the two Figure 3D claims, which the text prints as "10�4". The PDF legend reads "*p < 10−4", so I left them as they are.

I rendered Table S1 and Figures 3, 4 and 7 from the PDF. The cell counts, the Figure 3D/3H significance marks and bar heights, the Figure 4 arrows and the Figure 7 percentages and n all match the file.

**Changes, by claim**
- **fig2c-ec-cell-classes:** The "different-shank pairs only" reading can't give the 30%, because the 820 cells come from pairs on the same or different shanks (Figure 2C legend, Table S1). It is now a variant. The criterion also now says all three fractions are out of the 2744 EC neurons.
- **fig1-ec3-ca1-theta-coherence:** The 0.6–0.9 coherence range is printed with a citation to Chrobak and Buzsáki (1998). Whether this study measured it is now named as open.
- **fig3-interneurons-min-ascending:** The shaded column in Figure 3 spans about 265–360°, not 280–340°; corrected. I removed an exception for EC5 principal cells that the paper doesn't make (it excepts only EC3).
- **fig3d-ec2-strongest-modulation:** The quoted sentence is about modulation of the whole population (Figures 3A, 3E), not mean R. The statement and criterion now cover both.
- **fig4a-ec-hippocampus-offsets:** I removed the p < 0.001 statistic. It is the threshold that marks significant bins, not a result.
- **fig6-hippocampal-precession:** The "under 10 Hz" bound was made up. The low-rate bound is now named as open with two readings, and I added how the EC part of the statement is judged.
- **fig7-ca1-highest-precession:** I removed an EC3-vs-EC5 comparison the paper doesn't make. The EC3 part is now judged through figs15-ec3-no-precession, "strongest" is named as open with two readings, and the "minority of EC cells" part is added.
- **figs2-ripple-sequence:** The legend doesn't say whether 15–25 ms is the delay per stage or across the whole CA1-to-EC2 axis, so both readings are named. Onset delays and the "EC principal cells recruited less than interneurons" part are added.
- **figs19-fast-firing-minority:** The statement now speaks of neurons, as the quoted legend does. The made-up 4–12 Hz bound for "low rates" is now open with two readings.
- **New claims** for main findings that had none: figs6-identified-cells, figs7-individual-rats, figs12b-burst-single-phase and discussion-ec-interneurons-with-ec2.

**What remains open**
- Many criteria rest on wording the paper gives no threshold for, such as "in phase", "essentially identical", "close correlation" and "small"/"large" lags. Each names the readings it allows.
- fig8-ec-population-predicts-sinks needs CSD data from Montgomery et al. (2009), and the paper names no archive for it.
- Whether hc-2 holds EC units, CA3/DG units, tasks other than the open field, and cell-type and layer labels is for the author to find.

All of this is recorded under `checks` at the end of the file, with `ready: true`.
