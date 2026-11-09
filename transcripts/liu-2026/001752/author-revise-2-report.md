Nothing was committed, as instructed. This is a round-2 revision, so no outcome changed. I wrote three changes under `proposed` for a third verification round to settle. `python tools/entry.py all entries/001752-liu-2026` passes: 0 check errors, and both notebooks ran (106 s and 693 s). The conclusions match the new outputs.

**Proposed outcome changes (each outcome stays as verified until round 3)**
- **`fig5b-sipsc-frequency`**: not_reproduced → blocked (methods_underspecified).
- **`fig5c-sipsc-amplitude`**: reproduced → blocked (methods_underspecified).
- The reason for both: the detection cannot tell events from noise in the sIPSC files, and the paper gives no detection setting beyond the 5 pA threshold.
  - No sIPSC file has noise below 2 pA.
  - In 13 of the 15 files the detector finds 0.87 to 1.54 times as many opposite-polarity peaks as events.
  - Only 44 to 83% of injected test events are recovered per file.
  - Frequencies are 1.9 to 24 times the code's sheet values, and amplitudes 0.19 to 0.53 times.
  - A new notebook cell after the sIPSC table shows this file by file.
- **`fig4ac-ap-width-amplitude`**: partially_reproduced → not_reproduced. Neither feature reaches the criterion's p < 0.001. Amplitude gives p = 0.073, and with the L5-subclass PCs the p-values are 0.22 and 0.35. Only the direction agrees with the paper.

**Fixes and additions**
- **`fig4d-sodium-current`** is now marked `assumed: true`. The files hold no capacitance, so reading (b) uses one patch area for every patch. The deviation quotes the Methods' single estimate (about 5 µm² from about 50 fF), and a new `methods_unavailable` finding asks the authors.
- **Detector wording** is corrected in the main notebook (cells 13, 21 and 51, plus the sIPSC result cells), the README and the record notes. In the sEPSC files with 2 to 4 pA noise, opposite-polarity peaks are about half as frequent as events. In sIPSC they are about as frequent in 13 of 15 files and about half in w9b4ds and 1tsbdsc.
- **S02C0321 deviation**: it now says the sheet calls this cell a PC. It would be a VEN only under the table's flipped labels.
- **Elsewhere notebook text**:
  - Cell 15 now says only the first file of each session is read.
  - Cell 39 now gives 135 L5 PCs, not 145.
  - Cell 38 now says the resampling estimates power and does not show the data contradict the claim.
- **464 tau values for 462 cells**: the code's Patch-seq table names one file twice (cell n172), so that file was read and merged twice. Each file is now read once and 461 cells are analysed. One dandiset file that the table never names is printed and recorded as a finding. The numbers for fig2d-f, fig4ac and ven-subtypes are unchanged.
- **Multi-patch annotation problems** are now printed and recorded in the notes and as a finding. Seven of the 18 PC-to-PC connections are typed "Inh". Two rows have a projection label that names different channels from the row itself.
- **Round 2 is recorded under `verifications`** for all 34 claims. Each has the verifier's reasons in their own words and my response. I recorded `agrees: false` for the two sIPSC claims and fig4ac.

**Not done**
- The threshold question (whether "reading (b)", a threshold at each recording's own RMS noise, misreads the Methods) is already in `questions/001752.yaml` and is waiting on a reader. I did not change the claims, so fig5b-sepsc-frequency and fig5b-mipsc-frequency stay blocked by their criteria.
- The ±4 s.d. stability test from round 1 is still not applied. The verifier listed it as minor, and it does not bear on any outcome.
