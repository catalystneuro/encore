I wrote the claims file at `claims/openneuro-ds002778/10.1523-eneuro.0151-19.2019.yaml`. The quote checker reports 24 claims, 23 quotes, 29 statistical values and 0 problems. Nothing is committed.

**Text read:** the version of record, full text from Europe PMC (PMC6553574). It includes the Methods, the figure legends and Tables 1 to 3. The only supplement, Extended Data 1, is the analysis code. I read it at github.com/SwannLab/Jackson_2019, commit a7c89f5. The code's printed outputs match the beta values in Tables 1 and 2 and the Figure 3 correlations. I opened no PDF pages. For the dataset I read only its OpenNeuro title and README, which ask users to cite this paper.

**Claims:**
- 24 claims: 23 have quotes and 1 is marked `inferred` (the mu/alpha patients-off-against-controls results, which appear only in Table 2).
- 17 claims carry statistics, 29 entries in all.
- 14 claims have expected values with tolerances.
- All 24 have a criterion.
- They cover:
  - **Off against on medication:** sharpness ratio, steepness ratio and PAC; the bipolar montage; the null results at F7/F8 and T7/T8; the topography; UPDRS.
  - **Off against controls:** sharpness null, steepness higher, PAC null with the average reference, PAC higher with the CSD reference.
  - **Power spectra:** beta and alpha peaks in Figure 1C.
  - **Mu/alpha band:** Tables 1 and 2, and PAC difference larger in beta than in alpha.
  - **Figure 3:** sharpness and steepness each correlate with PAC.
  - **Figure 4 shapes:** most sensorimotor waveforms fall in quadrant 4 (Q4: sharper peaks, steeper decays), with patient counts of 9 at C3 and 8 at C4; F7/F8 shapes vary more; controls show the same pattern.
  - **Table 3:** effect sizes are larger when only Q4 patients are included.

**Details the paper leaves open, with the readings named:**
- **Artifact rejection:** the marks were made by hand and are not published. Readings: (a) the dataset's own annotations, if it has any; (b) no rejection beyond the code's rule that drops extrema within 100 samples of either end.
- **Noisy electrode exclusion:** (a) the dataset's bad-channel marks; (b) all 32 scalp electrodes kept. The eye electrodes stay out of the average reference in both.
- **PAC filter length:** the Methods say 231 ms and 240 ms (118 and 123 samples at 512 Hz). The code uses 231 and 240 taps. The Methods' values are the main reading and the code's are a variant.
- **Mu/alpha PAC phase filter:** 192 taps (3 cycles), 231 taps, or 118 samples.
- **Cohen's d for PAC:** raw PAC (what the code does; gives 0.83, as in Table 1) or log10 PAC (what the Methods say). Table 3 gives 0.75 for the same all-patient effect size, which is inconsistent with Table 1.
- **Wilcoxon p-value:** normal approximation, which is what the code's printed p-values show, with the exact test as a variant.
- **Which UPDRS score:** the motor part (III) total, or the total of all parts.
- **Bipolar montage, FDR family:** the three bipolar measures or the single test.
- **CSD result (p = 0.022):** the paper does not say whether it is corrected; I judge it uncorrected.
- **Undefined terms:** "peak" in the power spectrum is read as a local maximum in the band. "Sensorimotor" topography is read as the most significant electrode being C3, Cz, C4 or their neighbours. "More variable" shape at F7/F8 is read two ways: a smaller share of points in the most common quadrant, or a larger spread.
- **Electrode order in the code:** the code does not say which half of its patient recordings is C3, so the 9 and 8 Q4 counts are also checked in swapped order.

**Missing from the paper or its code:**
- **Preprocessing:** the MATLAB preprocessing and the manual artifact marks.
- **Analyses not in the code:** the mu/alpha, bipolar, CSD, F7/F8, T7/T8, power-spectrum and topography analyses, and the Q4 effect sizes. Their criteria rest on the Methods text alone.

No claim had to be dropped for missing text.
