I've written `claims/000623/10.1038-s41597-024-03029-1.yaml`. The quote checker passes with 0 problems. Nothing is committed.

**Text read.** The version of record (Sci Data 11, 214, open access), as Europe PMC serves it. It has the full main text, Methods, Data Records, Technical Validation, Usage Notes, Table 1 and the legends of Figures 1 to 7. The paper is a Data Descriptor and has no supplement. There was no PDF and I opened no figure.

**Code read.** github.com/rutishauserlab/bmovie-release-NWB-BIDS at commit 8c35290. The criteria take from it the unit and session selection, the bootstrap and permutation tests, the HFB (high-frequency broadband power) pipeline, the scene-cut labels, the gaze heatmaps, AUC and the confidence split. The code doesn't hold the run 1 against run 2 test, and it doesn't print the means and s.d. of the quality metrics.

**Claims.** 31 in all: 30 have quotes and 1 has an `inferred` note (Table 1 demographics). 11 have statistics (40 values), and all 31 have criteria.
- **Tested on the dandiset (25):** cohort and sessions, unit counts, spike-sorting quality metrics, eye tracking, recognition AUC, memory-selective cells, LFP and iEEG channels, event-selective cells and channels, the example units in Figs 6 and 7, and NWB contents. Of these, 6 use the code repository's scene-cut annotation file as labels, through a link claim.
- **Outside data (1):** Table 1 demographics, because the four fMRI-only participants' ages are in Table 1 and the code, not the dandiset.
- **Data elsewhere (4):** the fMRI motion, tSNR and inter-subject correlation results are on OpenNeuro ds004798. The in-scanner answers are on Figshare and in the code repository.

**Tolerances.** Counts of deposited records have tolerance 0, and everything else uses 10%. I didn't use the s.d. as a tolerance, because it describes the spread of units or sessions, not the uncertainty of a mean over a fixed deposited set.

**Details the paper leaves open, with the readings named:**
1. **Mean ISI below 3 ms:** over all units, or only the units under 3% that the code plots in Fig. 2c.
2. **s.d. degrees of freedom:** ddof 0 is used as a standard choice and ddof 1 is shown; it can't change an outcome at these sample sizes.
3. **Missing-gaze mean (7% ± 8%):** over the 27 sessions left after P53CS is excluded, or over all 29.
4. **Mean AUC (0.79 ± 0.19):** over the 29 sessions, or over the 16 participants after averaging their runs.
5. **Sessions in the memory analyses:** the code's rule (fewer than 10 correct trials per condition), or the five runs the text lists. The text's "behavioral AUC > 0.6" is read as AUC below 0.6, and the code applies no AUC rule.
6. **Direction of scene-cut selectivity:** the text says "differed significantly"; the code counts only scene change above continuity cut. The code's reading is followed and the either-direction count is a variant.
7. **Run 1 against run 2 AUC test:** not in the code, so it is set as a two-sided paired t-test on per-run AUC.
8. **Unseeded permutation test:** seed 0 is used as a standard choice and the Monte Carlo error is reported. This matters for the vmPFC LFP memory result, whose p of 0.05 sits at the threshold, so its criterion allows a partial result there.

**Missing from the paper.**
- The firing rate (2.47 ± 3.32) is printed without a unit; spikes/s is taken from the code's Fig. 2b axis.
- The per-area neuron counts appear only in Fig. 2h, so they are taken from the scene-cut denominators, which add up to 1450.
- The paper doesn't say which example neuron is Fig. 6a or 6b, or 7a or 7b; units are matched to panels by area and direction.
- The iEEG vmPFC denominator is printed as 449 where every other area is 448. It may be a misprint, and the claim reports the count found.
- No claim was blocked for lack of a method.
