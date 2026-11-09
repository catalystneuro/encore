I checked the claims file for CRCNS:hc-10 and changed five claims. It is ready for an attempt (`ready: true`).

**Checker:** `claims/crcns-hc-10/10.1016-j.neuron.2014.03.034.yaml: 34 claims, 32 quotes, 41 statistical values, 0 problems`. Before my edits it also passed, with 39 statistical values.

**Changes, by claim:**
- **tables1-rheobase:** I removed reading (c), which took the first step at which the group-mean firing in Figure S1E is above zero. That figure shows both group means already firing at about 1 Hz at +100 pA, so this reading cannot give the +150 pA in Table S1.
- **figs3f-pvbc-firing:** In Figure S3F the biological PVBC fires at about 2 Hz at +350 pA, which the claim left out. I added it to the statement and the expected values, with a tolerance of 1 Hz and the reason stated. The criterion now also says the paper does not give the step protocol for the biological PVBCs. It assumes the PCs' 1 s steps in 50 pA increments, which matches the figure's axis.
- **fig2e-bouton-roi-running:** The test was recorded as paired, but the paper gives n = 5 per sublayer without saying the samples are paired. The test now names the paper's general rule without choosing.
- **fig1-kmeans-large-small:** I added a criterion. The reported counts (22 sPCs, 17 dPCs) are the temporal pairs, but the paper does not say whether the clustering used only those 39 pairs or all 53. Both are listed as readings.
- **figs1-pc-morphology:** I added the significance the figure marks (p < 0.05) for basal dendritic length (n = 6 per group) and soma area (n = 11 per group).

The other claims match the paper: statements, sources, statistics, tolerances and methods. Every main finding in Figures 1 to 6 has a claim, and none comes from outside the paper. I rendered Figures S1 and S3 from the PDF, and the values the original author read from them are right.

**Still open** (recorded under `checks`):
- figs1e, figs1h and figs3f compare against values read off figures, with 10% tolerances. The figures also show SEM bars, but the text never states those values.
- figs1g (resting potential): the Table S1 footnote says the PCs were given a tonic current during the sweeps. Whether the deposited sweeps include a baseline with no current is for the author to find in the data.
- fig6c: the Results give 314 and 385 labelled cells with 54 labelled from both regions. The Figure S5C legend gives 271 and 410 labelled from one region only and 56 from both. The claim follows the Results.

Nothing is committed.
