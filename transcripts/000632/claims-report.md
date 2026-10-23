I wrote `claims/000632/10.3390-ijms241310921.yaml`. The quote checker reports 12 claims, 11 quotes, 0 statistical values and 0 problems. Nothing is committed.

**Text read:** the version of record as served by Europe PMC (PMC10341945): Results, Discussion, Methods and figure legends. The paper has no supplement and no PDF was supplied. It links no code, and its data are "available on request".

**Claims:** 12 in total, 11 with quotes. The dataset's title points to the Figure 3 experiment, which has five claims:
- co-directional equals cross-directional at 1 Hz (absence);
- co-directional is enhanced at 770 kHz;
- cross-directional at 770 kHz is the same as at 1 Hz (absence);
- co-directional is above cross-directional at 770 kHz (inferred: no sentence states it; it is read from the Results and Figure 3);
- uptake does not depend on the membrane area electroporated.

The other seven cover the rest of the paper:
- Figure 2: cancellation at 180° (2-fold and 20-fold), the crossover angle (160° and 130°), the three-fold plateau at 90 to 100°, and the 60-fold co- versus counter-directional difference.
- Figure 4: the pattern concentrated at the apex electrode.
- Figure 5: the sawtooth of about ±10% between the base electrodes, and about 25% near the apex.

**Statistics:** none recorded. The only test named is Figure 3's two-tailed Student's t-test, and its p-values are printed only in the figure, which I could not read. Criteria are written for all 12 claims; 7 have expected values with 10% tolerances.

**Details left open, with the readings named:**
- **Background:** either the raw intensity in the region of interest, or that intensity minus the uptake measured inside the electrode footprints. The Methods say footprints were measured "to account for" spontaneous uptake, but not how. For the absence claims I set the footprint subtraction to decide the outcome and made the raw reading a variant.
- **MemBrite normalization:** either none, or YP divided by MemBrite (the latter as a variant).
- **Significance level for Figure 3:** not stated; I used the conventional p < 0.05.
- **Paired or unpaired t-test:** not stated; I read it as unpaired with equal variance, with Welch's test as a variant.
- **Figure 2 crossover angle:** located by linear interpolation, a standard choice.
- **Figure 2 plateau:** two definitions are named.
- **Figure 2, 60-fold ratio:** either apex over base, or plateau over base.
- **Figure 4:** two definitions of the regions "adjacent" to each electrode are named.

**Missing for the claims:**
- **Figure 3 values:** the bar values and p-values, so the Figure 3 claims have no expected numbers or statistics. The PDF figure would supply them.
- **Figure 2 curve values:** these could not be read either, beyond what the text states.
- **Reference 17 (Kim et al. 2023, Bioelectrochemistry 149:108319):** the Methods defer the analysis protocol to it, and I did not read it. It may settle the background and normalization questions.
