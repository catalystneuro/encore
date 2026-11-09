I wrote `claims/001968/10.1038-s41593-026-02260-w.yaml`. The quote checker passes on it with 0 problems, and nothing is committed.

**Text read**
- **Paper:** the version of record (open access) as served by Europe PMC (PMC13246448), including the main text, figure legends, Methods and the Extended Data Fig. 1–10 legends.
- **Supplement:** Supplementary Figs. 1–11 and Tables 1–4. Table 1 (the statistics) is garbled in the text, so I read its pages 14–18 from the supplement PDF.
- **Not available:** the main article PDF wasn't supplied, so I never saw the figures, and numbers shown only in figure panels aren't in the file. The reporting summary and source data weren't supplied either.
- **Ref. 16:** the Methods describe behavior scoring, PCA, the shuffle, the similarity index (SI), the bootstrap and photometry as "previously described" in their ref. 16 (Lee et al. 2021, Nature). I read that paper's Methods for those steps only. It settles the PCA bins (50 ms over −1 to 4 s), the per-neuron min-max scaling, a separate PCA per timepoint, the photometry normalization and the T5 trial range.
- **Code:** the lab page the paper links holds only the 2021 place-cell protocol code (`analyze4LinearTracks.m`, `analyzePopulationVector.m`, `boxSpikeInfo3.m`) and has no version or commit. None of it covers this paper's analyses, so the code settles no method detail.

**Claims**
- 42 claims; 40 have quotes. The two without are the per-mouse Fig. 2k and Fig. 2l results, which carry an `inferred` note because no sentence states them.
- 36 have statistics (79 values checked against the text), all 42 have criteria, and 19 have expected values.
- They cover recorded unit counts, spike width and firing rates, cue-responsive cells, PCA distance, SI and bootstrap (young, early trials, old, L-DOPA), decoding, histology, photometry, behavior, optogenetics and L-DOPA (including the PS19 and WT controls).
- All use `data: dataset`. The dandiset's archive metadata points to tetrode electrophysiology only, so photometry, histology and behavior from other mice may be absent; that is for the author to find.

**Details the paper leaves open, with the readings named in the file**
- **Behavioral T5 (trials 121–160):** (B1) the trials of each odor pair that fall in session trials 121–160, or (B2) the last 40 trials of each pair.
- **Correct session:** above 80% (Methods) or at or above 80% (Results).
- **T2 and T4 for units:** never defined. Read as (T-a) 10-trial blocks midway between T1, T3 and T5, or (T-b) the whole second and fourth fifths of each odor's trials.
- **Cue response:** threshold p < 0.05 (Supplementary Table 1) or p < 0.01 (Results); increases only or any change; odor period only or odor, delay and choice periods. That gives eight combinations.
- **PCA scaling and smoothing:** (x − min)/max or (x − min)/(max − min); smoothed or raw binned rates.
- **Shuffle:** one permutation per session or one per cell.
- **SI's mean shuffle distance:** from the A-1 pair itself or averaged over all six pairs.
- **Bootstrap test:** a normal fit (the Results call it "maximum likelihood estimation") or an empirical fraction.
- **"Smaller or larger than the shuffle":** relative to the mean shuffle distance or to the 95th-percentile threshold.
- **Photometry window:** 1–4 s (Fig. 4d legend), 2–4 s (Supplementary Table 1), 0.5–3 s (ref. 16), or 2–3 s for "delay periods".
- **Decoding:** test window 1–4 s or 2–5 s; a sample is each 50 ms bin or the window mean.
- **Smaller ones:** the channel used for spike width, the definition of mean and peak firing rate, how the Supplementary Fig. 7 difference is formed, the baseline for the 3 SD rule, the family for the FDR correction in Fig. 2k, and whether "Odor-A cells" means A only or A among others.

**Where the paper contradicts itself (recorded in the claims)**
- **Statistics:** the Results print χ² = 2.29 for p = 3.6e-9, and F = 30.1 against 5.04 in the table for Supplementary Fig. 1c. The Fig. 6b ANOVA is F = 5.2 against 3.6. The PS19 test is printed as F(2,16) against F(1,16). The Fig. 5c interaction is p = 0.045 in the text and 0.047 in the legend and table.
- **Fig. 3b test:** rank sum in the text, signed-rank in the table.
- **Fig. 4f:** the legend says no significant difference, but the table shows strain effects of p = 0.047 and 0.0061.
- **Counts:** the L-DOPA group has 144 cells in the text but 132 in the table. Mouse #01517 has 97 or 99 cells. The WT L-DOPA group has 4 or 5 mice.

**Missing from the paper:** nothing the claims needed is absent apart from the figure panels themselves and task analysis code. The shuffle thresholds and bootstrap p-values come from Supplementary Table 1.
