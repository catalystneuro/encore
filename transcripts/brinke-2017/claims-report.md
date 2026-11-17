I wrote `claims/brinke-2017.yaml`, and the quote checker passes it with 0 problems (55 claims, 55 quotes, 84 statistical values). Nothing is committed.

**Text read.** The version of record (PMC5760204, from the Europe PMC full-text XML): Results, figure legends and figure-supplement legends, Materials and methods, and Supplementary file 1 (the linear mixed model summaries, docx). No PDF was supplied, so no figure was read; every value used is printed in the text, a legend or Supplementary file 1. The paper links no analysis code, so none was read. I did not open the dataset's example script, `eLife_dataset.m`, because it is a dataset file.

**Counts.**

| | Claims |
|---|---|
| Total | 55 |
| With quotes | 55 (none inferred) |
| With statistics | 44 |
| With criteria | 54 |
| With expected values | 46 |

- Two claims use outside data (`with_inputs`): the Purkinje cell data of ten Brinke et al. (2015) and the IpN model built on them. The paper does not say where those data are.
- The optogenetics claim and the US-only-trials claims are listed under the dataset by default. Whether cb-1 actually holds those trials is for the author to find.

**Details the paper leaves open, with the readings named:**
- **CR amplitude:** the maximum in the CS-US interval (Methods) or closure at US onset (Results and Supplementary file 1).
- **Baseline correction for facilitation and suppression:** two ways of subtracting the "above-baseline activity within the baseline". A second open point is which class a cell meeting both thresholds takes: the larger change, or facilitation first.
- **Second dataset timing:** the paper gives a 200 ms CS-US interval, the dataset description 212 ms, so the last 200 ms is 0–200 or 12–212 ms. The description's trials start 200 ms before the CS, so the 500 ms baseline may not exist; the reading is the whole pre-CS period.
- **CS pause and peak thresholds:** 4.5 SD measured from baseline or as the size of the drop; the 2 SD rebound measured from the trough or from baseline. That gives four combinations. The window is 50–125 ms in the Methods and 50–130 ms in one Results paragraph.
- **Trial-by-trial firing rate:** the trial's own baseline, the cell's mean baseline, or the dataset's per-trial facilitation variable.
- **Bootstrap null:** trials shuffled within each cell, or independent random values. The per-cell alpha is not stated; I used 0.05.
- **Chi-square:** with or without Yates' correction.
- **Spike rate velocity:** not defined; I used the first difference of the spike density function.
- **Correlation matrix:** 20 ms windows at 10 ms steps (Results) or 20 ms bins giving 100×100 (Statistics).
- **Cross-correlation:** the segment and lag range are not given.
- **Training-day coding:** how days after day 6 enter is not said.
- **Group definitions that conflict:**
  - US peak decline: days 1–4 against later in the text, but without/with behavior in the Fig 6C legend.
  - Second US peak: 39.4% fits 83/211 cells, not 83/270.
  - Facilitation-vs-suppression subsets: the printed durations differ from the full-class values.
  - CR latency: passing 5% closure (Fig 4G legend) or the Methods' CR onset.
- **Fig 7F,G similarity:** the paper gives no measure. I named two standard choices and marked them as not the paper's.

**Inconsistencies inside the paper, recorded in the claims:**
- Mouse counts: 19 mice in the Results; 25, 22 and 6 in the Methods, which do not add up.
- US peak correlation: 13 significant cells in the text, 15 in Supplementary file 1.
- US pause trial correlations: n = 41 in the text, 37 in the legend.
- Purkinje eyelid-opening test: p = 0.0254 in the text, 0.0218 in the legend.
- Fig 7: the text's panel citations do not match the legend.
- Fig 7—figure supplement 1C: the black group's second-peak value is printed as both 55 and 34.8 Hz.
- Fig 2B model: the F denominators are printed as 556 and 1556.
- The n values of the second-peak analyses (224, 138, 121 + 46) do not reconcile with 270.
- CS pause and US pause: 105/263 is printed for the "other" cells, although 105 is the total of US pause cells.

**Missing from the paper.** Nothing the claims needed is missing from the text. Recording depth, the optogenetics trials, the US-only trials and the Purkinje cell data are described, but the paper does not say where the Purkinje data are deposited.
