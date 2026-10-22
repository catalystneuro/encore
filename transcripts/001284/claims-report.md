I didn't write any claims. The safety classifier stopped my response while it was writing `claims/001284/10.1016-j.bioelechem.2025.109016.yaml`, so the file doesn't exist and no quotes were checked. I can't produce that content again, even reworded, so `claims/001284/` is empty. Someone needs to rerun the reader or write the file by hand.

What I found before it stopped:

- **Text read:** the accepted author manuscript in PubMed Central (PMC12331426), with the full Introduction, Methods, Results, Discussion and figure legends. PMC lists no supplement and the paper cites none. There was no PDF, so I couldn't see the figures.
- **Code:** the paper links none ("Data will be made available on request"). Every method detail has to come from the Methods (section 2.5) and the figure legends.
- **Dataset:** its archive description covers only the Fig. 5 experiments: electrodes raised 0, 1 or 2 mm, 0.2 MHz packets, 2 bursts (x4), YO-PRO-1 and propidium staining in CT26 cells. It gives a 10 mm inter-electrode spacing; the paper gives a 15.3 mm diagonal.
- **Planned claims (about 24):**
  - Fig. 2: heating stayed below 44 °C.
  - Figs. 3 and 4: the bright spot at the array centre, the Lorentzian fits (R > 0.9, p < 0.001), and suppression near the electrodes rising with packet rate. YP uptake at the centre did not change with rate. The centre was about 40 times brighter than near the electrodes at 0.2 MHz. FWHM fell from about 4 mm to about 2 mm (p = 0.03, 0.02, 0.09), with a log fit (R = 0.77).
  - Fig. 5: raising the electrodes weakened the centre spot. The YP spot was only slightly larger than the propidium spot. Fit quality (R²) was 0.92 Lorentzian vs 0.96 Gaussian for propidium, and 0.98 vs 0.95 for YP. Reversible electroporation starts at about 2 mm from the centre.
  - Fig. 6: pulse duration. FWHM was 1.7 ± 0.08 mm with 900 ns pulses, with p = 0.028 and 0.0072 against 300 ns, and the slope had p = 0.003.
  - Fig. 7: centre YP grew linearly with the number of bursts. FWHM grew with bursts in CT26 cells but not in CHO cells (p = 0.44). After 1 burst, FWHM was 1.1 mm, 7.3% of the gap and 2.3% of the array area, and electroporation near the electrodes was 40 to 50 times weaker than at the centre.
- **Details the paper leaves open:**
  - **Pooling the diagonals:** average the two diagonals at each signed distance, or average all four directions at each distance.
  - **Lorentzian fit range:** the Methods say 4 to 6 mm, Fig. 3 says ±4 mm, Figs. 5 and 6 say ±5 mm, and Fig. 7 doesn't say.
  - **Group curves:** fitted to the group means, or to all experiments' points pooled.
  - **ROI spacing along the diagonal:** not stated.
  - **"Near electrodes" for the 40-fold ratio:** 6 mm or 7 mm from the centre, as a ratio of means or a mean of per-experiment ratios.
  - **Fig. 6D fit:** the Results call it logarithmic and the legend calls it linear.
  - **The 2.3% of array area:** I couldn't get it from 1.1 mm by any computation I tried.
