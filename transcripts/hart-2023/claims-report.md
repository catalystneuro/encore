I've written the claims file at `claims/000467/10.1016-j.cell.2023.05.025.yaml`. `tools/claims_check.py` passes it with 32 claims, 32 quotes, 36 statistical values and 0 problems. Nothing is committed.

**Text read.** The PubMed Central author manuscript (PMC10334690, NIHMS1904919), not the version of record. That covers the Results, STAR Methods, Key Resources Table, the legends of Figures 1 to 6, Table 1 and Figures S1 to S7, and the supplement PDF (Tables S1 to S4). I did not read the supplemental videos. There is no PDF of the main text, so I could not read values shown only in figures (the medians on Fig. 6, the boxes of Fig. S5, the vectors of Fig. 5D). Every claim rests on numbers printed in the text.

**Code.** The repository linked in the paper (`HartKronauer2023`) returns 404. I read the lab's `Hart_Kronauer2023` instead, at commit 72d041a; its README names this paper and dandiset 000467. It holds:
- an NWB-to-TIFF converter, which keeps only trials t288, t293, t284 and t290 through a hard-coded filter the Methods never mention (I flagged it so the author doesn't copy it);
- the ImageJ macro for the peak maps. It fixes the stabilizer settings and that frames are counted from 1. It also clips values before the minimum filter, where the Methods filter first; I kept the Methods order as the main reading and the macro's as a variant.

The ROI drawing, the single-glomerulus traces and the R and GraphPad analyses are not in the repository.

**Claims.** 32 in all, every one with a quote. Seven carry statistics: the Fig. 1F / Table S2 Šidák tests with their confidence intervals, the behaviour Dunnett tests, the ablation paired t-test (p = 0.073), and the six Fig. S7C mixed-model p-values. Eleven have expected values and 30 have criteria. By data:
- **In the dataset (calcium imaging), 17 claims.** Several criteria had to be fixed by me because the paper judged them by eye: general odorants, 3-hexanone breadth, bilateral symmetry, absence of decreases, concentration effect and the Fig. 5C dynamics. Each criterion says so.
- **Data the paper never deposited, 7 claims:** the behaviour videos (Fig. 1C to F, S2C to F), Table 1 and the pupa images. These are recorded as `data: dataset` and will be blocked as `data_missing`.
- **Deposited elsewhere, 8 claims:** confocal stacks in the Brain Image Library (the paper doesn't say which of its three IDs holds which figure) and the genome in NCBI BioProject PRJNA947257.

**Details the paper leaves open, with the readings named:**
- **How ROIs are drawn:** connected regions at or above 0.2 that recur in two trials, or the same restricted to glomerulus-sized regions (10 to 20 µm).
- **ROI value:** mean or maximum over its pixels.
- **Counting responding glomeruli:** trial-averaged value at or above 0.2 (Methods), or counts per trial averaged over trials (Fig. S5 legend).
- **Which "highest concentration":** 48% in 8 ants, or each ant's higher concentration in 13 ants.
- **Single glomeruli:** the centre plane is the one where the glomerulus is largest or where its response peaks; the ROI is a 15 µm disc or the region at or above 0.2.
- **Fig. S6 model:** the Methods say "glm with a random effect"; read as individual as a fixed factor, or as a random intercept.
- **Fig. S7C p-values:** sequential F-tests, marginal F-tests, or coefficient t-tests.
- **Concentration in Fig. 5C:** 48%, or all concentrations pooled.
- **Plateau and return to baseline in Fig. S7A:** 90% or 80% of peak; baseline plus 3 SD, or 0.2.
- **Fig. 5D centres:** response centroid or peak pixel, from one trial or the mean over trials.
- **Image orientation:** taken as the figures' L/A axes. If the files give none, Fig. 5D's direction claims are at most partially reproduced.

**Missing from the paper:** the behaviour, transgenesis and pupa-imaging data are not deposited anywhere the paper names. The mapping of the Brain Image Library IDs to figures is not given. The analysis steps above, apart from the peak-map macro, have no code.
