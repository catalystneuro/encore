I've rewritten `claims/huszar-2022.yaml` to the current protocol (pilot-16). The quote checker reports 43 claims, 42 quotes, 48 statistical values and 0 problems. Nothing is committed.

**Text read.** The author manuscript in PubMed Central (PMC10807234), which is the full text: main text, Methods, figure legends and Extended Data Figures 1 to 10. Both supplements were read too: the Reporting Summary and Supplementary Tables 1 to 5. The tables are images in the PDF, so I extracted them and read them as images. The version of record is not open access, and the main figure images were not available, so numbers printed only inside panels could not be read.

**Code read.** `github.com/rhuszar/optotagCA1_final`, commit 51320d4 (its only commit). I also took the dataset's title and description from DANDI; I did not open its data.

**Counts.**
- 43 claims: 42 with quotes, and one (`st1-animal-sessions`) marked `inferred`, read from Supplementary Table 1.
- 29 claims carry statistics, 48 entries in all.
- 43 have criteria, 36 have expected values.

**What changed from the old file**
- **Opening comment.** I removed everything that came from the data check: the author's outputs and the choices fixed from them (a ≤5 Hz rate rule for pyramidal cells, a 0.2 s speed smoothing, a 5 cm/s running threshold). Every method detail is now cited to the Methods, a legend, Supplementary Table 1 or the code. The criteria no longer say what the dataset lacks; that is for the author to find.
- **Cohorts.** Supplementary Table 1 shows that one novel-environment mouse (E13.5 26m1) is also among the nine familiar-maze mice, although the Results call the novel cohort "separate". `maze-cohort` now follows the table and the code.
- **Theta-related rate.** Now taken from the code: spikes in theta cycles over cycle time, with no speed threshold. Cycles are kept to waking periods as the Methods say; the code's unrestricted version is a variant.
- **Tolerances.** Back to the protocol: 10% by default, or the paper's s.d. or s.e.m. where it gives one. The old file's 0.03 on the Figure 6c medians is gone.
- **Expected values added** to the birthdate claims (Figures 1c, 1e to h, 2d, 2f, 3c, 3e, 5b, 5d, 7c and 7e).
- **New claims.** Supplementary Table 1 per-animal counts, ED Fig. 2 waveform checks, ED Fig. 1 BrdU, ED Fig. 3 depth control, ED Fig. 5 matched controls, ED Fig. 6 held-out assemblies, ED Fig. 7 hard-coded assemblies, and Figure 7d (transmission peaks at gamma intervals).
- **Ids** are kept wherever the finding is the same.

**Details the paper leaves open, with the readings named**
- **Session count:** 92 (Methods), 96 (Figure 1e, Figure 7f and the 15 homecage mice of Supplementary Table 1) or 104 (all 17 mice).
- **Median SPW-R duration:** pooled over ripples or the median of per-session medians; all ripples or homecage ripples only.
- **Unit counts:** whether they cover the 96 homecage sessions or all sessions.
- **Light-responsive cells:** a stored label, or detection from the light pulses by the Methods.
- **Per-animal synchrony, 11 of 13 (Figure 2b):** the per-animal Wilcoxon test of ED Fig. 4 at p < 0.05, or the difference in z-scored cross-correlograms.
- **Spatial information and coverage (Figure 5b):** left and right maps concatenated or averaged. For coverage, either bins with rate > 5 Hz and more than 1 bit of information, or rate > 5 Hz alone.
- **Ratemap correlation, never-visited bins:** the Methods' exclusion is the main reading; the code's drop-the-pair is a variant.
- **Spatial information in novel environments:** occupancy-weighted (Methods) as the main reading, the code's equal-weight form as a variant.
- **Figure 7g quintile pairs:** the code's pairs of two nonresponsive cells, or all pyramidal pairs.
- **Figure 7e medians:** the legend's values, or Supplementary Table 4's, which differ.
- **Disagreements between code and paper:** burst index 2–5 ms in the legend and 3–5 ms in the code; REM-shift locking at P < 0.01 in the Methods and 0.05 in the code. The paper's choice is used and the code's shown as a variant.
- **Standard choices, named as such:** Kalman filter settings, the binning for the ED Fig. 5 matching, the depth resampling, and the ICA seed.

**Missing from the paper or code that claims needed**
- **Not in the repository:** the session list, the rate-map builder, the code behind the Figure 5b spatial information and coverage values, the theta-cycle and theta-modulation detectors, the monosynaptic-connection detector, `GetTransProb` and the bootstrap ANOVA (`boot_anova1`).
- **Garbled p-value:** the Figure 2f firing-rate p is printed "P = 6 × 10 −0", so it is not recorded and that test is judged at p < 0.05.
- **Inconsistent percentage:** Figure 7f's 65.27% does not match its own pair counts (which give 65.6%). Both are within tolerance.
- **Histology:** Figure 1c and the BrdU claim (ED Fig. 1) rest on histology the paper describes but may not have deposited.
