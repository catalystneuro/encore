I checked the claims file for 000483 against the paper, made six changes, and marked it ready. Nothing was committed.

**Checker result:** `24 claims, 24 quotes, 27 statistical values, 1 problems`. The one problem is the p-value of `fig6b-landmark-cells`, recorded as 0.0008, which the checker could not find. The paper prints it as "8.0 × 10−4", which is the same number, so nothing needed fixing there.

**Changes, by claim**
- **figs5-rotation-direction, figs6-arena-control:** the statements said "RSC tuning persists". The paper says the diversity of responses persisted (a second peak in light like visual axons, a single peak in the dark like ADN axons). I narrowed both statements to that.
- **fig5-three-classes:** the criterion clustered only heading-selective cells, a choice taken from the lab's code. The Methods say "all cells were fit". I made the set of cells an open point with two readings: (a) tuned cells only, (b) all cells.
- **fig5-class-proportions:** I added the cell counts printed on the Figure 5 heat-map axes, as they appear in the extracted text: 332, 409 and 552 cells, out of 1569 tuned cells in Figure 5A. Pooled, these give shares close to the reported 22%, 33% and 28%. I also noted the conflict: 552 landmark cells disagrees with the 522 implied by the statistic F(1,1042).
- **fig6-heading-below-population:** the text cites "Fig. 6C, right", but by its legend the class comparison is Figure 6B, right. The source now says both. I also added mouse as a second reading of the random effect in the mixed model, from the paper's Statistical information.
- **checks:** I appended the 2026-10-23 entry with these changes and the open points below.

**What remains open**
- The supplement (Figures S5 and S6, Table S1) is not in the paper store. So what figs5 and figs6 compare, and the model used in fig6-heading-below-population, rest only on readings.
- No PDF renderer or PDF library was available, so I could not view the figures. Whether there are 552 or 522 landmark cells is unsettled.
- The paper gives no measure for five claims: fig1h, fig4-axons-light-off, fig5e, fig5k and fig6b-180-errors. Their criteria use thresholds that are readings, named as such, not the paper's.
- I did not re-read the code repositories. The code details in the opening comment and criteria are taken as the first reader recorded them.

**Ready:** yes. The open points are named in the criteria, so the author can test them under each reading.
