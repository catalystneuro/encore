The checker now reports `claims/mansvelder-2026.yaml: 44 claims, 44 quotes, 107 statistical values, 30 problems`. All 30 are values from Supplementary Table 3, which is only in the PDF, so the checker can't search them. I extracted the PDF's text and confirmed each one there, along with the other Table S3 numbers, the Table S4 counts and the Table S5 scaling factors.

**Changes, by claim**
- **fig2ab-peak-range (new):** the Results say human and mouse interneurons peak "roughly in the 2-5 Hz range", and no claim covered it. The claim uses 2 to 5 Hz widened by 10% of each bound. The paper doesn't say which summary of the frequencies the range describes, so the median and the interquartile range of resonant cells are both listed as readings.
- **fig3fh, fig3jl, fig4i, fig4km, figs3, figs4, fig6b, fig4b:** removed `data: with_inputs`. These claims use none of the dandiset's recordings (they rest on mouse cells, transcriptomes or reconstructions). The protocol uses `with_inputs` only when outside data are added to an analysis of the dataset. The paper names no public source for these data, so the claims now use the default and are blocked as data_missing unless the author finds the data public. The header comment says so.
- **figs3-zd7288-mouse:** the statement covers "frequency measures" and the Fig. S3 legend includes the 3 dB cutoff, so the criterion now also requires it to fall (p = 0.017).
- **fig5be-zd7288-human:** the wording about which direction each measure moves was garbled. It now says sag ratio, resonance frequency and resonance strength fall and input resistance rises.
- **figs1-region-pathology:** the statement includes input resistance but the tests didn't. Added the legend's two tests for it and included it in the criterion.
- **fig6b-channel-expression:** the criterion invented a "more than half of cells" threshold and tested acute cells only. It now gives two readings, the first marked as not from the paper, and applies them to acute and cultured cells. It also records that the paper lists CACNA1G both as highly expressed and as lower.
- **fig7fj-model-morphology:** the criterion contradicted its own first reading of which model has the lowest frequencies. It now accepts either reading. It also records that the Discussion says human-like models have lower resonance strength, which conflicts with the Results.
- **figs5-model-gpas:** the limit on how much resonance strength may vary was presented as the paper's. It is now marked as a reading.
- **fig8eg-noisy-modulation:** the Methods say 10 × f trials and Table S5 implies 20 × f, so both are now readings. The "peak" rule is marked as a reading, and the 5 Hz phase in the statement is now reported.
- **figs5-model-normalized-morphology, fig7ae-model-ih, figs2-l23-no-depth:** added the Discussion citation for reading "sharper" as a lower cutoff, and noted that the Results cite the wrong supplementary figure. Noted the 65 s chirp in the legends against 62 s in the Methods. The L2/L3 assignment is now stated as open, not as a standard choice.
- **Header O6:** recomputed the chi-square values from the counts. The goodness-of-fit reading reproduces every per-subclass value in Fig. 5i (163 of 268 cultured cells resonant, 60.8%). The 2×2 reading reproduces both overall values. For VIP the printed p = 0.100 doesn't fit; the counts give p = 1.
- **Header O7:** corrected the exact Wilcoxon minimum p-values. Eight cells also can't give p = 0.004, and p = 0.031 can come from 7 cells, so it doesn't show there were 6.

**Still open**
- The paper's code link returns 404, so the chirp, sag, input resistance and membrane-potential details remain readings based on IPFX.
- The paper names no public source for the mouse, cultured or new recordings, the transcriptomes or the reconstructions.
- No figures could be viewed, so the Fig. 3b sag and input-resistance schematic is unseen.
- The text and Table S3 disagree in several places; these are listed under O10 in the header.

The file is ready for an attempt: the last check entry says `ready: true`. Nothing is committed.
