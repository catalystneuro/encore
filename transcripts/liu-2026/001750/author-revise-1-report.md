I've revised the attempt against all of the verifier's round-1 points and re-run it. `python tools/entry.py all entries/001750-liu-2026` passes with 0 errors in about 4 minutes, and every conclusion in the notebook and the record matches the new run's numbers. Nothing is committed.

**Outcome changes**
- **ven-subtypes-similar-physiology: blocked → reproduced.** The verifier said the eEPSP part could be run from column J of the eEPSP sheet. It could, and the paper's code repository also holds the per-cell AP values for the 85 VEN-L and 41 VEN-S cells (`VENsubtype_APs.mat`). None of the three tests is significant: AP width p = 0.55, AP amplitude p = 0.27, eEPSP subtype ANOVA p = 0.958 (paper 0.9852). The record notes as a deviation that this uses the authors' tables, not the DANDI:001746 recordings.
- **fig3e-phase-peak-index: blocked → reproduced.** While writing a reason for each blocked claim I found the repository's per-cell table (`PeakIdx_Fig5e.xlsx`). VENs have the lowest median, and Dunn's test separates them from every pyramidal cell type (Bonferroni p ≤ 0.001). The sheet's cell counts differ from the legend's in four of six types; this is recorded.
- **ven-firing-rate-variability:** still blocked, but now as `methods_underspecified`, which is the reason the claim's own criterion gives. The data size is in the notes.
- **model-na-ratio: kept blocked.** The verifier would give partially reproduced. The claim depends on fig4d, which is blocked, and the protocol blocks a claim that depends on a blocked one. The disagreement is recorded.
- All other outcomes are unchanged.

**Added or corrected**
- **Where the Na⁺ maxima come from:** per cell, the repetition count, noise, step, latency and width of the maximum, plus an I–V table and the averaged trace for all 35 cells. In 10 cells (6 VEN, 4 PC) the maximum is a brief transient about 0.1 ms wide, an artefact, not a Na⁺ current. Noise and repetition count do not differ by cell type (p = 0.34 and 0.89).
- **Variants that decide nothing:** a standard low-pass filter at cut-offs fixed in advance, and a window cut to the first 3 ms. With these, 17 of the 24 baseline-subtracted variants find VENs significantly lower. The earlier smoothing variant is now described as fitted to the table, so it is not independent evidence.
- **Question for a reader:** whether the fig4d readings should include a filtered peak, added to `questions/001750.yaml`. The claim itself is unchanged.
- **Session breakdown for fig4d:** under the code's example reading, and in the paper's own table, VENs are lower only in session HS (p = 0.0028).
- **Patch capacitance:** every value and attribute of every file is now printed (52 per file) and searched, along with the metadata of all 35 assets. Nothing names a capacitance, resistance or seal, so the claim stays blocked (data missing).
- **eEPSP cross-check:** the sheet's "re-orgnized data" block shares 69 of its 78 rows with the block used before. Its ANOVA gives p = 0.0033 against the paper's 0.0034, so the paper most likely ran its test on that block. fig4j stays reproduced.
- **Metabolomics details:** "L-Glutamic acid" is now chosen explicitly as glutamate, with the other entry shown as a variant. The one zero value (L-Cystine) does not change the log2 counts.
- **Record and README:** a reason for each blocked claim in a new "Claims not tested here" section, new findings (the transients, the two disagreeing eEPSP blocks, a wrong folder path in the paper's script), and the round recorded under `verifications` for all 34 claims.

**Not done**
- I did not test fig2df on the repository's Patch-seq feature table. It has cluster numbers, not the subclass names the claim needs, and borrowing names from another figure's table would be an assumption I couldn't defend.
- The morphology and model claims, and the claims assigned to other dandisets, stay blocked for the reasons now given in the notebook.
