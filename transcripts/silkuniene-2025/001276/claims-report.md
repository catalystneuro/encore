I wrote `claims/001276/10.1016-j.bioelechem.2025.109016.yaml`. The quote checker reports 22 claims, 22 quotes, 15 statistical values and 0 problems.

**Text read.** The accepted author manuscript in PubMed Central (PMC12331426): main text, Methods and figure legends. I did not read the version of record. PMC lists no supplement and the paper cites none. There was no PDF, so I never saw the figures, and every number comes from the text and legends. The paper links no code ("Data will be made available on request"), so I read none.

**Dataset.** From its title and description, it holds the Fig. 7 burst-number series: 1, 2, 4 and 6 bursts at 0.2 MHz, 600 ns pulses, Hoechst and YO-PRO-1 staining. Its "10.0 mm inter-electrode distance" fits the paper's 15.3 mm diagonal if read as the edge-to-edge distance along a side. The opening comment says so.

**Claims.**
- 22 claims, all with a quote and all with a criterion; 8 carry statistics.
- 6 claims are on Fig. 7: central uptake rises linearly with burst number, CT26 saturates at 6 bursts, FWHM against burst number (CT26 p<0.001, CHO p=0.44), the 1.1 mm sharpest peak, the 40–50-fold off-target suppression, and the CHO replication.
- The other 16 cover the packet-rate figures (3 and 4), electrode elevation and cell killing (5), pulse duration (6), heating (2) and the field simulation (1E).
- The field simulation is `with_inputs`: the model files are not public.

**Details the paper leaves open, and the readings named:**
- **Lorentzian fit range for Fig. 7:** ±4, ±5 or ±6 mm. Methods say "4–6 mm"; Fig. 3 used ±4 and Figs. 5–6 used ±5.
- **Fig. 6D fit range:** ±5 mm (legend) or ±4 mm ("as described in 3.1").
- **ROI spacing along the diagonal:** 1 mm or 0.5 mm. ROI orientation is set as a standard choice that cannot change an outcome.
- **Fig. 7 linear fits:** fitted to individual experiments or to group means.
- **"Near electrodes" ratios (40-fold, 40–50-fold):** 6 mm or 7 mm from the center; ratio of group means or mean of per-experiment ratios.
- **Area percentage (2.3%):** three readings. Only "disk of radius FWHM over the square of electrode centers" gives 2.3%.
- **Fig. 6D fit of FWHM on pulse duration:** linear (legend) or logarithmic (text).
- **Fig. 6B absence test:** t-tests with Bonferroni correction or one-way ANOVA. If they disagree, the claim is blocked as `methods_underspecified`.
- **Fig. 4B comparison family:** each rate against 1 Hz, following the Fig. 4C legend; all pairs is shown as a variant.
- **Fig. 4B power-function fit:** to group means or to individual experiments.

**Inconsistencies in the paper:**
- The 0.2 MHz FWHM comparison has p=0.09, yet the text counts it as a decrease.
- The log-fit slope is p<0.001 in the text and p<0.0001 in the legend.

**Missing from the paper:**
- No code, model files or deposited data outside the dataset.
- Several claims rest on measures the paper does not define, so their criteria take the measure from elsewhere in the paper:
  - Saturation is judged against the Fig. 7 confidence band.
  - The Fig. 6C and Fig. 5 tests come from the general Methods rule.
  - Fig. 5C is judged by intensity only; the nuclear-staining part, judged by eye in the paper, is left untested.
- The positions of the Fig. 5C zones are given only in the figure, which I could not see.

Nothing was committed, as instructed.
