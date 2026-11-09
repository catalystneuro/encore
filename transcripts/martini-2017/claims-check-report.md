I checked `claims/martini-2017.yaml` against the paper and made seven corrections. The file is ready for an attempt.

**Checker result** (same before and after my edits): `claims/martini-2017.yaml: 18 claims, 18 quotes, 15 statistical values, 0 problems`

The statements, sources, quotes, statistics and expected values all match the paper. Every main finding has a claim: Figures 2 to 4, the neuropil comparison, the tuning consistency across halves and the shuffle test of tuning. No claim comes from anywhere but this paper.

**Changes, by claim**
- **Header:** the opening comment said the Methods fix one regression per waveform type. The Methods' wording also allows one regression of all responses with three slopes. I added this as open detail 12, with both readings.
- **fig2ab-example-neuron:** the criterion asked each coefficient to lie inside the paper's interval, but the tolerances are wider than the interval on one side. It now judges each coefficient on its tolerance, and runs both regression readings.
- **fig2de-tuned-fraction:** added the two regression readings to the readings it runs.
- **tuning-consistency:** the criterion presented its meaning of "identical tuning" as if it came from the paper. It now says the paper does not define it and names the reading used.
- **shuffle-significance:** the paper says this test gave "no qualitative change in results", which covers every result that depends on tuning. I added the Figure 4C and 4D tests to the criterion where they can be tested, and to `depends_on`.
- **fig3d-example-correlation-distance:** the tolerance on the shuffled slope (0.00025) contradicted the criterion's own bound of 0.01, which was made up. I set the tolerance to 0.014 per mm, the paper's SEM for shuffled slopes over all fields, with the reason given. I also added pairs up to 300 um as a variant, since the Results look at distances "up to 300 um".
- **fig3g-si-no-spatial-organization:** the paper does not say which neurons or pairs enter the 26 fields. I added two variants next to the main reading: pairs of tuned neurons only, and fields with at least two neurons tuned to a common feature.

**Still open** (recorded in `checks`)
- **responsive-fraction:** the paper never defines a responding neuron, so the 50.2% claim rests on the file's own made-up tests.
- **Example neuron and example field:** the paper doesn't say which mouse or field they come from, so they have to be found by matching the figures to the data. The paper also gives the example field two sizes: 31 neurons (Figure 3B) and 29 neurons with 465 pairs (Figure 3F).
- **Similarity index (SI) scale:** it's unclear whether SI is the raw dot product of tuning coefficients or uses unit-length vectors. The paper's slope sizes fit the unit-length version better. Its SEM of 0.000675 for the median SI slope looks like a misprint, so the file uses 10%.
- **Correlation slope beyond 200 um:** the paper doesn't say whether it is fitted to the far pairs only or to all pairs of those 30 fields. Both readings are named.

Only `claims/martini-2017.yaml` was changed; nothing is committed or pushed.
