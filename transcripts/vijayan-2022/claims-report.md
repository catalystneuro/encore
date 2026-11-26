I wrote `claims/vijayan-2022.yaml`, and the quote checker passes: 45 claims, 45 quotes, 10 statistical values, 0 problems. Nothing was committed.

**Text read:** the version of record from Europe PMC (PMC9616500), `paper/10.1126-sciadv.abn3852.txt`. That covers the main text, figure legends, Materials and Methods, and the supplement PDF (Figs. S1 to S7, plus the legends for Tables S1 and S2 and Movies S1 to S3). I opened no PDF pages. The paper links no code (the analysis was done in MATLAB), so no method detail is settled by code.

**Claims:**
- **Quotes:** all 45 have one; none needed an `inferred` note.
- **Statistics:** 9 claims carry 10 entries. All tests are two-sided Wilcoxon rank sum; the p-values are bounds of < 0.001 or < 0.005, and Fig. 1F's are Bonferroni-corrected for seven comparisons.
- **Expected values:** 19 claims, at 10% tolerance. The exceptions are the line count of 115 (exact) and the merge points of about 20 s (one bin, ±5 s).
- **Criteria:** all 45 have one.
- **Data:** one claim, the Fig. 7A screen, is `with_labels`, because the line identities are in Table S2. All others use the dataset.
- **Shared methods:** eight are defined once in the opening comment and named by label in the criteria: island assignment, speed, search period, rate function, bin test, choice fraction, pause time, and egg-aligned speed.

**Details the paper leaves open, with the readings named:**
- **Island boundaries in multi-island chambers:** taken from the fig. S1 geometry.
- **Locomotor speed:** frame-to-frame displacement at 2 frames per second, as a standard choice.
- **Search start:** going back from the egg, the first frame where the 18.5-s smoothed speed is below 0.1 mm/s, with a centred filter (the 9-s minimum implies one). Searches under 30 s are padded back to 30 s.
- **Rate-function bin edges:** read from the fig. S2 axis ticks (0, 5, 10, 15, 20, 25, 30, 45, 60, 90, 150, 300, 600, 1200, 7200 s).
- **"Trial" in the bin test:** (a) each visit to the bin; (b) each search that enters the bin.
- **Which two-choice chambers are pooled for the 964/1205 and 918/2744 counts:** (a) the ref. 16 chambers only; (b) those plus this paper's.
- **Fig. 1F:** which pairs the three p-values compare (each glued group against the unglued control, or against its own control).
- **Fig. 2E to G, "nearly completely":** the 200 mM rate at most 10% or at most 20% of the 0 mM rate.
- **Fig. 3D, the "fast egg" clock:** counted from crossing the midline or from leaving 200 mM.
- **Fig. 4A transits:** every visit, or pass-through visits only; medians pooled or per chamber.
- **Fig. 4B:** the indicated bin (5 to 10 s, 0 to 5 s, or 10 to 15 s).
- **Fig. 4E:** which chamber each shade is; the Fig. 4A order is taken, with all six orders shown if it fails.
- **Fig. 6G:** time on 0.8% over all frames or only search frames.
- **Fig. 7A:** hits ranked by fold change or by p.
- **Fig. 7F, "nearly superimposable":** the merge point is the first bin past 5 s, or at most one bin differs.
- **Claims with no test in the paper:** where a claim says "gradually increased", "similar", "unrelated" or "look more like", I fixed a working measure in its criterion and said so.
- **Fig. S4 models:** the kernel fitting comes from ref. 82 and is not described here. I named one reading (a least-squares fit of a zero-area kernel to the 0/200 rate functions), with a block if no fit is defensible.

**Missing from the paper:**
- **Tables S1 and S2:** these are separate spreadsheets, not in the text. S1 summarises all tracking data and holds a p-value the Fig. 4B claim cites; S2 has the screen's line identities.
- **The main-text PDF:** numbers printed only inside main figures could not be read. That includes most bin p-values, the merge-arrow positions, the order of groups in Fig. 8A, and the sucrose levels of the Fig. 6B bars.
- **Ref. 16:** the Methods defer chamber design, tracking and egg annotation to it, and it is not under `paper/`.
- **Two claims probably need hand-scored video:** the latency-to-feeding claims (Figs. 7B and 8B). The dataset is described as holding tracking data, so these may not be testable.
