I wrote `claims/001027/10.1016-j.bioelechem.2023.108437.yaml`, and the quote checker passes it: 18 claims, 18 quotes, 2 statistical values, 0 problems.

**Text read:** the accepted author manuscript in PubMed Central (PMC10247516, NIHMS1891360). It has the full Methods and the figure legends. PubMed Central lists no supplement and the text cites none. The paper links no code, so I read no repository. The version of record is not open access. On the archive, the dandiset's title and description match the Fig. 8 experiment only: Packets 1 to 3 at 4 kV, applied once from each electrode. I still wrote claims for all the main findings.

**Claims (18, all with quotes):**
- Fig. 4, single cells (4 claims): the single unipolar pulse gives the most dye uptake; the bipolar signals are weaker (p < 0.001); sham cells take up no dye; the 8-phase signal is about 20 times weaker than one pulse.
- Fig. 5 (3 claims): control trains give stronger uptake everywhere; Packet 2 without rotation peaks in the centre but stays stronger near e1; rotation focuses uptake on the centre.
- Fig. 6 (3 claims): more packets give more uptake; centre-to-edge ratios for each packet number; the central peak gets narrower.
- Fig. 7 (3 claims): fold changes with pulse amplitude; normalized profiles do not change with amplitude; no dependence on array size.
- Fig. 8 (3 claims): equal uptake in the centre; more uptake near the electrodes for Packets 1 and 3; centre values of 183%, 83% and 74%.
- Fig. 9 (2 claims): fold decreases with the 1, 2 and 3 mm gaps; up to 600% at 2 mm.

**Statistics:** 2 entries. Fig. 4: p < 0.001. The paper names no test for this figure; the only test in the Methods is a two-sided Student's t-test. Fig. 8A: p < 0.01, two-sided Student's t-test.

**Criteria:** all 18 claims have one. 14 also have expected values, each with a tolerance. For Fig. 4 the tolerance is the paper's own standard error; elsewhere it is 10% of the value.

**Details the paper leaves open, with the readings named:**
- **Which array was used in Figs. 6 and 8:** not stated. The author reports what the data show; the normalized comparisons do not depend on it.
- **One diagonal or the mean of both:** the paper says only for Fig. 5. Both readings are shown for Fig. 8.
- **The "most peripheral" ROI:** the mean of the ROIs next to each electrode, or each end of the diagonal separately (or the ROI next to e1).
- **The centre ROI:** the ROI at distance 0, or the mean of the two ROIs on either side of it.
- **How profiles are normalized:** normalize each dish and then average, or normalize the mean profile.
- **Background subtraction of the monolayer intensities:** not stated. Raw and background-subtracted values are both shown.
- **Peak width (Fig. 6):** the distance between the two dips on either side of the centre, or the full width at half height. If they disagree, the claim is blocked as underspecified.
- **The low point between centre and electrodes (Fig. 6):** the lower side or the mean of the two sides.
- **Tests the paper does not name (Fig. 4, and the absence claims):** I used the only test the Methods name, the two-sided Student's t-test at p < 0.05.

**Inconsistencies in the paper:**
- Section 3.4 says "~120 a.u. for packet 1", which contradicts the same sentence. I read it as Packet 2.
- Section 3.4 says the other two bipolar signals cancel 4 to 5 fold, but the paper's own means give 6.1 for the 4-phase signal. Both are recorded.
- In Fig. 7, the small array used 1 packet from each electrode and the large array 10, so array size and packet number are confounded in the array-size claim.

**Missing material:** nothing a claim needed. The Sim4Life field simulations (Fig. 3) are not recordings, so I wrote no claim for them.
