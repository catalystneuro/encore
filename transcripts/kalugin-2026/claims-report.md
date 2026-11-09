I wrote `claims/001074/10.1016-j.neuron.2026.07.008.yaml`. The quote checker passes: 46 claims, 44 quotes, 0 problems. Nothing is committed.

**Text read.** The accepted author manuscript from PubMed Central (PMC13568791), not the version of record. It includes the main text, STAR Methods, figure legends, Table 1, the key resources table, the video legends, and the supplement PDF (Figures S1 to S6). Nothing the results rest on was missing.

**Code read.** github.com/pkalugin/kalugin-et-al-morse at commit fa4526a.
- **Matches the paper:** the outputs printed in `morse_figs3_rev` (Figure 1G-J, S3, Table 1) and `morse_fig2_rev` (the LC optogenetic slices).
- **Does not match:** the dLGN and PVH slice analysis exists only as an older notebook (`morse_fig2`) whose printed values differ from the paper (for example NE peak 2.21 µM against 4.61 µM, and different thresholds).
- **Not in the code at all:** fiber photometry, the probe-stability counts, the "two orders of magnitude" comparison, and the "100–200 cells" count.

**Counts.**
- 46 claims; 44 have quotes. The other two are marked `inferred` because their numbers appear only in Table 1 (off-target EC50s, peak ΔF/F0 on the probes).
- No statistics: the paper reports no test and no p-value anywhere.
- All 46 have criteria, and 33 also have expected values with 10% tolerances (exact for counts).

**Details the paper leaves open, and the readings named.** Method steps shared by many claims (pooling, concentration, threshold, peak, rise time) are defined once in the opening comment and cited by the claims.
- **Peak normalization in slices:** (a) the median of 100 frames centred on the maximum, or (b) the maximum itself. The code used a hand-picked window.
- **Peak window after KCl:** (a) from KCl wash-on to the next wash-on, or (b) 7.5 min after wash-on.
- **Robustness threshold:** the Methods compute it on the peak-normalized signal; the code uses unnormalized ΔF/F0 over the first 5 min. The code's version is a variant.
- **Recordings averaged:** for the dLGN peaks and the 111 s delay, all 9 slices or only the 7 with robust 5-HT.
- **Deconvolution time constant:** taken from the ΔF/F0 fits or from the concentration fits.
- **LC per-train increment:** the code's frame window, or train onset to the next train's onset; "several trains" is read as 5.
- **In vivo onset ("within 10–15 min"):** the rise time (first crossing of (1 − 1/e) of the peak), or the first crossing of the threshold.
- **CSF concentration:** the value at 30 min, or the peak within 0–45 min.
- **EC50 plateau:** the Methods' third-minute mean decides; the code's sorted-frame median is a variant.
- **Undefined words:** "similar" (photometry, serum MORSE against ELISA, choroid plexus against MORSE), "consistent across probes", "fully activated" and "almost all" each get two named readings.
- **How 5-HT events were picked:** for the spontaneous 5-HT elevations the code picks recordings by hand with no rule, so one threshold rule is named.

**Missing or inconsistent things a claim needed.**
- No sentence or code gives how the 100–200 cells per gel were counted.
- The parameter ℱ for each sensor is not printed in the paper; it is taken from `morse_figs3_rev` cell 376.
- The code's hand corrections (cluster labels, detrend frames, peak windows) cannot be repeated.
- Several claims need raw imaging, photometry, ELISA tables or histology. The paper says only single-cell traces are on DANDI and that raw imaging is available on request.
- The paper disagrees with itself in places:
  - 100–300 nM in the text against 100–200 nM in the Figure 2I legend.
  - ">90%" probe stability against n=10/13.
  - IQR "8–9" against 8.25 in the code.
  - The late-warp definition differs between the Figure 1F legend and the code.
  - n=11 mice in the Figure 3D-F legend against 10 in the code.
  - GRAB-AVP2.0 in Figure 6D against AVP0.2 elsewhere.
