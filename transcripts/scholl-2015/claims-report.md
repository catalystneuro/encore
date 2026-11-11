I wrote `claims/scholl-2015.yaml`. The quote checker reports 25 claims, 25 quotes, 10 statistical values and 0 problems. Nothing is committed.

**Text read:** the version of record, as text extracted from the PDF. That covers the main text, figure legends and Experimental Procedures, plus the Supplemental Information (legends of Supplementary Figures 1 to 6). Nothing the results rest on is missing. The paper links no code (the Methods say only "custom MATLAB software" and cite CircStat). I read the dataset's data descriptor only to see which experiments it holds.

**Claims:** 25, all with quotes and none inferred.
- **Statistics:** 6 claims record tests: Mann-Whitney for MI, for DSI and for the two ΔF/F comparisons; the shuffle comparisons for PV+ and PV- ocular dominance and for PV- with ODI between -0.5 and 0; and the distance-similarity tests.
- **Criteria:** all 25 have one.
- **Claims of absence:** 7, each judged on the paper's test or threshold where it gives one.
- **Coverage:** histology co-localization; responsive cell counts; binocular fraction; contralateral bias; MI and DSI differences (pooled and per animal); MI against DSI; the tdTomato and neuropil contamination controls; the salt-and-pepper organization; PV+, PV- and CaMKIIa+ ocular dominance and disparity against local populations; both length constants (71.4 and 78.7 µm); and the Figures S4, S5 and S6 controls.

**Details the paper leaves open, with the readings named:**
- **Visual response criterion:** the Methods require a joint monocular and binocular response, but the Results count the two separately. Readings: (a) each counted on its own, (b) counted among cells meeting the joint criterion. The neuropil requirement is applied with and without, as the paper does not define the neuropil region for it.
- **Which cells enter an analysis** (ODI, DSI, fraction denominators): (a) cells passing the full response criterion, (b) cells responsive to monocular stimuli (binocular, for DSI).
- **Co-localization:** the Results and Methods give the 94.3% and 79.4% the other way round from each other. Both assignments are named.
- **Major-axis slope axes:** individual on population is the main reading, from the Supplementary Figure 5 and 6 axis labels; the reverse is a variant. For MI against DSI: DSI on MI, or MI on DSI.
- **Shuffle test:** one-sided or two-sided. Bootstrap and shuffle counts are not given; 1000 each is used as a standard choice.
- **Exponential fit:** unweighted or weighted by SE.
- **Pixel-to-micron scale:** the text gives 300 µm for a 256 × 455 pixel field. Readings: 300 µm along each image axis, or 300 µm along the 455-pixel axis with square pixels.
- **Fewer than 3 neighbours:** the cell is dropped at that radius only, or from all radii.
- **Cells with DSI < 0.1:** left out as individuals only, or also from the populations.
- **Circular correlation:** the formula as printed in the Methods, or the Batschelet/CircStat coefficient they cite.
- **Test behind "significantly correlated"** for disparity: against the shuffle distribution, or the value more than 1.96 bootstrap SE above zero.
- **"All binocular stimuli" ΔF/F:** each cell's mean over the eight conditions, or all cell-by-condition responses pooled.
- **Negative responses in ODI and DSI:** as measured, or set to zero.
- **MI similarity measure and its p-value** in the salt-and-pepper test: the absolute MI difference of each pair against distance, or each cell's MI against the mean MI of cells at each distance.
- **The 28% "no evoked activity":** two readings of the denominator.
- **"Smaller radii"** in Figure S4A: 50 µm, or 50 and 75 µm.
- **Fo baseline window:** its length is not given.

**Missing from the paper:** no test or threshold for "no relationship" in MI against DSI (the PV+ slope of 0.04 ± 0.02 is called none), so that claim is judged on its values. No tests are given for Figures S4, S5, S6C-D and 5F; the paper's significance level from the related panels is applied and noted as such.

**Possibly missing from the dataset:** the claims on histology, CaMKIIa animals and neuropil patches may not be testable. The descriptor lists only 6 PV-Cre animals; finding out what it holds is the author's job.
