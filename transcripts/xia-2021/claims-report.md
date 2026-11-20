I wrote `claims/xia-2021.yaml`. The quote checker passes with 0 problems.

**Text read**
- I read the version of record of the PNAS article (main text, figure legends, Methods, Data Availability) and the SI Appendix (legends of Figs. S1 to S16).
- Table S1 is not in the extracted text, and Movies S1 to S4 were not available. No claim needs them.
- I opened no PDF page.
- The paper links no analysis code. It names the AQuA program (ref. 32) without a repository or version, so I read no code.

**Datasets**
- `sparc-75` holds the BTX and nanosensor staining. Three claims rest on it: Fig. S5 alone, Fig. 3D jointly with `sparc-108`.
- `sparc-108` is the deposit named in Data Availability; the other 27 claims rest on it.
- All claims have `data: dataset`.

**Counts**
- 29 claims, all with quotes.
- Only one claim has statistics: Fig. 6, a paired t test with P < 0.01 across four experiments. It is the only test the paper reports.
- 22 claims have expected values, and every claim has a criterion.

**Details the paper leaves open, and the readings named for each**
- **Initial rate (Vsensor):** the frames used are not stated. The readings are (a) a linear fit from onset to peak, or (b) the first 2 to 5 frames.
- **dF/F baseline:** (a) the mean of the frames before onset, or (b) the first frame.
- **Photobleaching fit:** a monoexponential, fitted either to the frames outside the response or to the whole trace.
- **Regions of interest (ROIs):** the hand-drawn ROIs in Figs. 5 and 6 have no coordinates.
- **AQuA parameter values:** none are given. The readings are AQuA's default preset, or settings tuned until events like those of Fig. 7A appear.
- **HPLC peak areas:** two baseline readings (a flat baseline, or a linear baseline under each peak).
- **Michaelis–Menten fit:** fitted either to the means over the three mice or to all points.
- **Upper detection limit (358.01 µM), which the paper never defines:** (a) a fixed fraction of Vmax, or (b) the top of the linear region from the tangent at EC50.
- **Lower detection limit (228 nM), the two-line split:** the split that minimises residuals on linear concentration, the same on log concentration, or the split drawn in Fig. 4B(ii).
- **pKa:** a Henderson–Hasselbalch sigmoid, or interpolation at half the maximal change.
- **3.7% rise:** the value at 15 s, or the peak within 15 s.
- **Control-sensor ratio at 10 V:** a ratio of peaks, or of initial rates.
- **Pulse dose response:** judged by rate, or by peak.
- **Vesamicol paired t test:** one test over the four experiments, or a test within each experiment over matched time points.
- **Fig. S10:** whole ganglion or an ROI.
- **"Peak at 10 to 15 s":** counted from stimulation onset or from event onset.
- **Extinction coefficients:** those for AF647 and pHAb are not given. The dye makers' published values are named as an assumption.
- **Thresholds I chose:** where the paper says only "minimal", "similar", "barely visible" or "no visible increase", I set a threshold and flagged it in the criterion as my choice.

**Discrepancies and gaps**
- Equation 3 applied to the paper's printed unit rates gives 2.86, 10.93 and 79.7 µM, against the reported 2.75, 10.49 and 76.51 µM, about 4% apart. I noted this in the criterion; it stays within the 10% tolerance.
- The Fig. 7 onset times use a tolerance of one frame (0.55 s) instead of 10%, so that the reported order of onsets can still be told apart. The reason is given in the claim.
- Nothing a claim needed is missing from the paper. Some claims cannot be tested unless the dataset holds calibration data the paper describes: the AF647 concentration calibration and the spectra of the pure components. The criteria for those claims say so.
