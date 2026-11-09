I checked the claims file for DANDI:001752 against the paper. After my changes the file is ready for an attempt.

**Checker:** `33 claims, 33 quotes, 10 statistical values, 0 problems`. Before my changes it was 32 claims, 8 statistical values and 0 problems.

**Changes, by claim** (each is also logged under `checks`):
- **fig5b-sepsc-frequency** (the other Fig. 5 claims refer to it): the criterion said the Methods fix the analysed duration as the whole stable recording. They don't. They give only a minimum 5 min recording after the baseline is stable (no shift beyond 4 s.d.) and at least 200 events. I added both conditions and marked the duration as open. I also wrote that the peak detector is a standard choice, not the paper's own method.
- **scrna-classes:** the "where" field named a processed h5ad on GEO, which the paper doesn't mention; the paper says the GEO deposit is FASTQ. I changed it to FASTQ, plus the Zenodo processed data the paper does name.
- **patchseq-mapping:** the tolerance on 34 was 3; 10% is 3.4, so I corrected it. I also added the 18 and 17 type counts as expected values.
- **fig2d-f-l23-it-tau-width:** the criterion required differences from "most other subclasses", which the paper doesn't say. I replaced it with two readings of "stood out". I also noted that the text gives L6 PC as n = 14 while the legend gives 13.
- **fig4d-sodium-current:** the Methods don't say what is compared. I named two readings: peak current, and current density using the patch area the Methods estimate.
- **fig4i-peak-index-ais-distance:** the statement said the model and real-neuron slopes don't differ. The paper only says the relation "closely matched", and its ANCOVA prints P = 0.0031 for slope. I restated the claim as the paper puts it and added the missing criterion: it is judged on the two slope t-tests and the intercept term, and both readings of the slope term are named.
- **fig5-connectivity-by-type:** the criterion said nothing about what happens if the deposit has no connection labels. It now says the claim is blocked as methods_underspecified in that case. I also added the holding potentials and how cell types were identified, from the Methods.
- **fig6h-subtype-markers:** the criterion gave only one of the Methods' two marker definitions. I added the second (top 50 genes plus four expression criteria) as a reading, and set the groups from the Fig. 6h legend (scRNA-seq clusters, not Patch-seq cells).
- **fig7c-tau-rna-distance:** I added a criterion with the Methods' distance definitions. The transcriptomic distance is taken as 1 − r, since a positive r is only possible under that reading.
- **New claim, fig4g-model-ais-distance-ap-shape** (Fig. 4g,h and Extended Data Fig. 7b): a main finding with no claim. Moving the AIS away from the soma in the VEN model makes APs wider and smaller, and the PC model doesn't show this.

**Still open:**
- The Fig. 5b,c p-values appear only in the figure, not in the text. So I can't confirm that each of the four frequency comparisons was significant on its own; the four claims assume it from one sentence that pools them.
- Fig. 4i prints F(1, 93) = 1.07 with P = 0.5729, but that F gives p ≈ 0.30. The paper also doesn't say what the slope P tests.
- I didn't check the opening comment's code details against the repository (the swapped mEPSC labels, the PC trace counted twice, the "+20mV" sIPSC files, the 30 s window). The criteria use them only as variants, so they don't decide any outcome.

Nothing was committed.
