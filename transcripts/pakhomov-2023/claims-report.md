I wrote `claims/pakhomov-2023.yaml`. The quote checker passes: 24 claims, 24 quotes, 0 problems. Nothing is committed.

**Text read:** the accepted author manuscript in PubMed Central (PMC10247516), not the version of record. It has the full Methods (2.1 to 2.4), Results, Discussion and the legends of Figs. 1 to 9. The paper has no supplement and links no code or data deposit, so no repository was read. No PDF was supplied, so no figure was read.

**Claims:**
- 24 claims, all with quotes and all with criteria; 12 have expected values.
- 2 have statistics: the bipolar signals against the single unipolar pulse in Fig. 4 (p < 0.001), and Packets 1 and 3 against Packet 2 near the electrodes in Fig. 8 (p < 0.01).
- Where a finding was the same, I reused the id from the old file for the dataset that holds that figure.

**Which claims rest on which dataset** (from the dataset titles):
- 000686: Fig. 5
- 000875: Fig. 6
- 001025: Fig. 7, plus the Discussion's claim that targeting does not depend on array size
- 001027: Fig. 8, plus the claim that cancellation predicts targeting
- 001028: Fig. 9

No title names the single-cell experiment of Fig. 4 or the field simulations of Fig. 3. Those 5 claims list all five datasets; the author checks each and blocks them as `data_missing` if none holds the data.

**Details the paper leaves open, with the readings named:**
- **O1, ROI layout:** the 92 or 224 ROIs cover (a) one diagonal or (b) both. The ROI width across the diagonal is not given; I named a square ROI (side equal to the spacing) and a band three spacings wide. Neither comes from the paper.
- **O2, diagonals:** for Figs. 6 to 9, (a) both diagonals averaged or (b) one diagonal.
- **O3, center:** (a) the ROI nearest the center, or (b) the mean of the two ROIs on either side of it.
- **O4, most peripheral ROI:** (a) the mean of the end ROIs, or (b) each half-diagonal taken to its own end ROI.
- **O5, normalization order:** (a) each dish normalized, then averaged, or (b) the mean profile normalized.
- **O6, background:** for monolayer images, (a) raw intensity, or (b) a background subtracted.
- **O7, raw or fitted:** (a) ROI means, or (b) the LOESS fit; spans 0.25 and 0.75 are standard choices, not the paper's.
- **O8, within-dish comparisons:** (a) paired or (b) unpaired t-test.
- **O9, trough between center and periphery:** (a) the mean of the two sides, or (b) each side.
- **O10, "end of recording" in Fig. 4:** (a) the last image, or (b) the mean of the last six images.
- **Undefined terms:**
  - "Enhanced in the center" in Fig. 5A: (a) a central peak, or (b) a higher center-to-e1 ratio than the trains.
  - The "void" in Fig. 5B: (a) the center below the periphery, or (b) the center as the profile minimum.
  - Peak width in Fig. 6: (a) full width at half height, or (b) the distance between the troughs.
- **Not stated at all:** the array used in Figs. 6 and 8, the voltage of Fig. 6, and the voltages of Fig. 7C and D. The author takes these from the data.
- **Test for the single cells:** Methods 2.2 names none. I used the two-sided Student's t-test that Methods 2.4 names, as a reading, with Welch's test as a variant.

**What the paper is missing or gets wrong:**
- **Fig. 4 and Fig. 3 data:** no dataset title names either. The simulation model is not deposited.
- **Fig. 7 voltages:** the voltages between 2.4 and 5.6 kV appear only in the figure.
- **"~120 a.u. for packet 1":** this contradicts its own sentence, which puts Packets 1 and 3 at 250 to 350 a.u. I read it as Packet 2, which also fits the 183% of Fig. 8B.
- **Fig. 4 fold values:** the paper's own means give 6.1-fold for the 4-phasic signal, outside its stated "4–5-fold". The claim keeps the stated range and reports 6.1 beside the result.
- **Array size:** Fig. 7 gave the small and large arrays different packet numbers (1Px4 against 10Px4), so no comparison in the paper isolates array size. The criterion states this confound.
