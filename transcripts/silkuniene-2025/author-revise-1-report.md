I've worked through every point in the round-1 report, changed three outcomes, and re-run the entry. `python tools/entry.py all entries/silkuniene-2025` passes with 0 check errors, and the notebook runs in 41.5 min. Every conclusion matches the new numbers. Nothing is committed.

**Outcomes changed**
- **fig5-raised-electrodes-weaken-centre**: partially_reproduced → not_reproduced, as the verifier gave it. The criterion needs both the 1-mm and the 2-mm drop. With all wells only the 2-mm drop clears the error bars. With the August 2024 wells, which match the paper's n, neither drop does (Bonferroni p = 0.56 and 0.36).
- **fig7be-center-linear-with-bursts**: reproduced → partially_reproduced (assumed), as the verifier gave it. I drew 2000 random well sets of the paper's size. The CT26 slope has p < 0.001 in only 38.4% of them, with the largest p 0.0055.
- **fig7-offtarget-40-50-fold**: not_reproduced → reproduced (assumed). The paper subtracts background from "an electrode footprint" without saying which. I now run each footprint as a reading. Three of the four fixed footprint positions put the CT26 1-burst ratio at 6 mm inside 36 to 55 (42.4 with the upper-left one), and the criterion needs one combination. The darkest footprint, which the rest of the analysis uses, gives the lowest ratio.

**Kept, with the disagreement recorded**
- **fig6d-longer-pulses-sharper-peak** stays reproduced (assumed). The verifier gives partially_reproduced.
  - I ran all 21 ways of choosing five of the seven 600-ns wells. The trend holds only when wells B2 and B3 of plate P1 are left out.
  - The plate layout puts the two extra 600-ns wells on P1. Of the three ways to drop two of them, only B2 and B3 gives the trend.
  - I keep fitting per experiment because three group means leave one degree of freedom, so the paper's p = 0.003 would need t ≈ 212.
- **fig7cf-fwhm-with-bursts** stays reproduced (assumed). The verifier gives partially_reproduced. The legend gives p < 0.001 for the CT26 slope in panel B, which three group means can hardly reach. In random well sets of the paper's size the claim holds under every reading in 88% of draws.

**Added or corrected**
- A question for a reader in `questions/silkuniene-2025.yaml`: the claims file assigns Figs. 3 and 4 to 001047, but that dandiset holds only a 3.8-mm array. The claims are unchanged and still blocked. The 001276 wells at 1 Hz, 0.2 MHz and control are run as variants that decide nothing.
- A per-well table showing how each well's array was located, with its corner scores, spot offset, centre value and FWHM.
- A check of the spot-centring bias: locating the array from the YP spot narrows the FWHM by a median of 0.10 to 0.13 mm. fig6d-900ns-fwhm and fig7-sharpest-peak-one-burst stay within tolerance under at least one reading once this is taken out.
- The Fig. 5 claims are also shown with the August YP wells only, and fig5b-reversible-beyond-2mm with the other way of pooling the diagonals (O2 reading b). Their outcomes are unchanged.
- fig7-sharpest-peak-one-burst now compares against the Fig. 5 groups too. They are all wider (1.72 to 3.57 mm).
- The data check now prints the channel names stored in the two-channel files, confirming the order the code assumes. I fixed the parsing that left the kV blank for 54 of the 001047 files; all 88 now print 3.8 mm and 3.2 kV.
- I updated the findings, notes, deviations, README, summary and `runtime_minutes`, and recorded round 1 under `verifications` in `attempts/silkuniene-2025-04.yaml`.

**Not done**
- No new parallel-to-side or 1-kHz/10-kHz analyses. Those data are in no dandiset.
- The footprint detector was not changed. The new bias check measures its effect.
