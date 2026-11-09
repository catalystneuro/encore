I wrote `claims/001559/10.1021-acssensors.5c01093.yaml` with 21 claims, all of them quoted word for word. The quote checker reports 0 problems and the file validates against the claims schema. Nothing is committed.

**Text read:** the version of record from Europe PMC (PMC12351538): main text, Methods, the legends of Figures 1 to 5, and the Discussion. There was no PDF, so values printed only inside figures could not be read.

**Missing from the paper text:**
- **The supplement is missing.** The Supporting Information PDF (Fig. S1, the brightness data in Fig. S2, the HEK 293T spectrum in Fig. S3, and Table S1) and Movies S1 to S3 are not in `paper/`.
- **Why I went ahead anyway:** the dandiset says it holds only the Figure 4 cortical recordings, and those claims rest on the main text, the Figure 4 legend and the Methods. Earlier readers in the registry (001750 to 001752, 001746) did the same.
- **Claims that need the supplement:** `lysate-brightness`, `cell-brightness`, `hek-spectrum` and `table-s1-fold-gains`. They quote the main text, and their criteria say that their measures and tests are unknown without it.
- **P values:** the unpaired t-test P values for Figs. 2B, 3B and 5C appear only inside the figures, so those tests are named in the criteria but have no `statistics` entry.
- **Response measure for Fig. 5:** it follows an "established procedure" that the Methods cite without describing it.

**Code:** the paper links no analysis code. The dandiset's description says it includes the Figure 4 analysis and figure scripts, but those are dataset files, so I did not open them. If they settle any detail below, that is a question for a reader.

**Counts:**
- 21 claims: 6 on Figure 4, 4 on Figure 5, 4 on Figure 1, 3 on Figures 2 and 3, and 4 that need the supplement.
- Quotes: all 21.
- Statistics entries: 0, because no p-value or interval is printed in the text.
- `expected` values: 10 claims have them.
- Criteria: 15 claims have one.
- Two claims use outside data: `fig5-double-bric` (BRIC values from Tian et al. 2022, doi:10.1038/s41467-022-31673-x) and `table-s1-fold-gains` (Orange CaMBI values from Oh et al. 2019).

**Details left open in Figure 4, with the readings named:**
- **Response window:** (a) the 5 s stimulation period, or (b) the stimulation period plus 5 s after it.
- **Which mice must show the increase:** (i) at least one mouse, since the figure shows one unidentified "representative mouse", or (ii) every mouse recorded under all four conditions.
- **"Individual stimulation events":** (a) single 5 s trials, which matches the Discussion's wording, or (b) single pulses of the 5 Hz train, run as a variant on the unsmoothed signal.
- **Detection threshold:** 2 or 3 baseline standard deviations.
- **Which electrode is "region 1":** the dataset's own labels if it has them, otherwise both assignments.
- **Current for the timing claim:** 4 mA, 2 mA, or both.

**Choices that are mine, not the paper's, and labelled as such in the file:**
- a 5 s pre-stimulus baseline;
- a one-sided Wilcoxon test for "clear increase", since the paper gives no test;
- half of the peak as the rise-time threshold;
- the drift threshold for the "steady baseline" claim.

The paper gives no PMT sampling rate and no trial counts.
