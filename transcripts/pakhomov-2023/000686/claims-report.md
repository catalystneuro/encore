I wrote the claims file at `claims/000686/10.1016-j.bioelechem.2023.108437.yaml`. The quote checker passes: 20 claims, 20 quotes, 2 statistical values, 0 problems.

**Text read:** the accepted author manuscript in PubMed Central (PMC10247516, NIHMS1891360), with its Methods, Results, Discussion and figure legends. I did not read the version of record. PMC lists no supplement and the text cites none. The paper links no code, so no repository was read and every method detail comes from the Methods or the legends.

**Claims:** 20 claims, all with quotes and none `inferred`.
- **Statistics:** 2 claims have entries, both two-sided Student's t-tests: the bipolar signals against a single pulse (p < 0.001, Fig. 4), and Packets 1 and 3 against Packet 2 near the electrodes (p < 0.01, Fig. 8A).
- **Expected values:** 12 claims. Fig. 4 uses the paper's s.e. as tolerance; the others use 10%, with reported ranges widened by 10% of each bound.
- **Criteria:** all 20 claims have one, and 3 are claims of absence (sham uptake, amplitude not changing the spatial distribution, equal center uptake for the three packets).
- **Data:** the Fig. 3 field simulation is marked `with_inputs`, because it needs an outside Sim4Life model that was not deposited. All other claims use the dataset.

**Details the paper leaves open, and the readings named:**
- **O1, the "center" value:** the ROI at distance 0, or the LOESS fit at 0.
- **O2, the "most peripheral" value:** the mean of the outermost ROIs at every end, or the e1 end alone.
- **O3, normalization:** each dish normalized first and then averaged, or the mean profile normalized.
- **O4, background in monolayer images:** raw intensity, or background subtracted.
- **O5, LOESS span:** not given. Three spans are named; this matters only where a value is read from the fit.
- **O6, t-test within the same dishes:** paired and unpaired are both run. The equal-variance and Welch forms are both named for Fig. 4.
- **O7, Fig. 4 "end of recording":** the last frame, or the mean of the last six frames.
- **Peak width (Fig. 6):** the paper gives no measure. The readings are full width at half height on the mean profile, the same on the LOESS fit, and the distance between the troughs.
- **The trough in "least affected area":** the lowest single ROI, or the minimum of the LOESS fit.

**Missing or inconsistent in the paper:**
- **Fig. 6 and Fig. 8:** the paper does not give the array size for either, nor the voltage for Fig. 6.
- **Fig. 7:** it does not give the intermediate voltages.
- **Fig. 5C:** it prints no number.
- **Array and ROI sizes:** the small array's size is given only as about half the large one, and no ROI size is given.
- **Fig. 8A typo:** the text says "~120 a.u. for packet 1", but by context it must be Packet 2. I read it as Packet 2 and said so in the criterion.
- **"4–5-fold" cancellation (Section 3.4):** the paper's own 4-phasic numbers give 6.1-fold, outside even the widened range of 3.6 to 5.5. So the criterion tests the 8-phasic ratio (18.3 from the paper's means) and the ordering of the three signals.
- **Species:** the archive lists Bos taurus, but the paper used CHO-K1 (hamster) cells. This is noted in the opening comment.

The dataset's title matches the Fig. 5 legend. Which other experiments it holds is left for the author to find.
