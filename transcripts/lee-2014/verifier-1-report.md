**A. Outcomes** (34 claims in the claims file)

| Claim | My outcome | Reason |
|---|---|---|
| figs1e-if-curves | reproduced | The two-way ANOVA finds no group effect: p = 0.411 under reading (a) and 0.866 under (b) (cell 12). Rates at +550 pA are sPC 31.62 / dPC 30.56 Hz (a) and 33.63 / 31.24 Hz (b), all within tolerance. The group means at +100 pA (0.89 and 0.88 Hz, cell 11) match the ~1 Hz the claims file reads from Figure S1E. |
| figs1f-input-resistance | reproduced | Reading (a) gives sPC 118.7 and dPC 124.9 MΩ; reading (b) gives 118.9 and 123.7 MΩ. All are within tolerance, and Mann-Whitney p = 1.000 (cell 15). |
| figs1g-resting-potential | blocked (data_missing) | The criterion's blocking condition holds. No PC file has a current channel, and every 0 pA baseline sits at the −70 mV holding level (−72.2 to −67.4 mV, cell 17). Table S1's footnote says the holding current was given but not recorded. |
| figs1h-sag | reproduced | Reading (a), −400 pA: sPC 8.71 ± 0.67 mV, dPC 5.69 ± 0.48 mV, t test p = 0.0020, both within tolerance (cell 19). Readings (b) and (c) keep the difference, but their means fall outside tolerance. The 1 ms smoothing variant does not change this. |
| tables1-rheobase | partially_reproduced | Reading (a), the median: sPC 200 pA, dPC 150 pA. Reading (b), the rounded mean: both 200 pA (cell 21). So the groups give the same step under (b), but that step is not +150 pA. This is the criterion's definition of partial. |
| figs3f-pvbc-firing | reproduced | Reading (a) on PV34 with rate reading (a): silent from 0 to +300 pA, then 2.0, 17.0, 36.0 and 52.0 Hz at +350 to +500 pA (cell 23). That matches all four values exactly. |
| fig1e-euipsc-dpc-larger, fig1-uipsc-successes, fig1f-connection-probability, fig1g-somatic-distance, fig1-common-pvbc, fig1i-distance-correlation, fig1-kmeans-large-small, fig1j-axon-terminals, fig1-release-properties, fig1k-somatic-dendritic-ratio, fig1l-pv-boutons, fig1n-optogenetic-ipsc, fig2c-fullfield-running, fig2e-bouton-roi-running, fig2f-bouton-density, figs2-ais-correction, fig2gi-pvbc-axon-sublayers, fig3c-spc-excite-pvbc, fig3-epsc-release-properties, fig3ef-reciprocal-motifs, fig4b-pvbc-inhibit-firing, fig5-cckbc-nonselective, fig6c-parallel-projections, fig6e-amg-larger-ipsc, fig6g-mpfc-excite-pvbc, figs1-pc-morphology (26) | blocked (data_missing) | I listed the bucket myself. `hc-10/` holds only `live/Soltesz_data.zip` (MD5 99bc6c87…, as the notebook checked), `checksums.md5`, the docs, and an old description. The zip holds 37 current-step ATF files (cell 3): no paired recordings, imaging, optogenetics or anatomy. No part of these claims can be tested. |
| fig4d-model-feedforward, fig4ef-model-pvbc-rates | blocked (too_large) | Both need simulations of ModelDB 153280 (data: with_inputs). The cost estimate, about 670 core-hours, rests on a timing that was not run in the notebook (cell 24). |

Count: 4 reproduced, 1 partially reproduced, 27 blocked for missing data, 2 blocked as too large. No chance levels apply.

**B. Problems**

1. [does not affect a conclusion] `hc10.input_resistance` (cell 15): the −100 to +100 pA window includes sweeps with spikes at +100 pA in D1_25abf, D4_11abf and S1_47abf. This raises their resistance; D1_25abf goes from 137.7 to 199.9 MΩ. It follows the paper's protocol. The spike-free variant still shows no group difference, though its dPC mean (101.8 MΩ) falls outside tolerance.
2. [does not affect a conclusion] `hc10.firing`, rate reading (b): a sweep with one spike gets 0 Hz, but a sweep with two closely spaced spikes gets a high rate (PV34 at +350 pA: 14.9 Hz under (b) against 2.0 Hz under (a)). This reading is unreliable near rheobase. The claims pass under reading (a) anyway.
3. [does not affect a conclusion] Cell 12: the two-way ANOVA treats each cell-by-step value as independent, which inflates the degrees of freedom. That is the paper's test as written, and the mixed ANOVA variant is shown (p = 0.759 and 0.951), so the absence claim holds either way.
4. [does not affect a conclusion] Cell 21 (rheobase): two dPCs, D5_15abf and D6_19abf, reach rheobase on a single 0 mV crossing at +150 pA. The threshold check in cell 13 reports only total spike counts, not each cell's rheobase. If either cell moved to +200 pA, the outcome would stay partial.
5. [does not affect a conclusion] Cell 23, figs3f reading (a): choosing the best-matching of six cells is permissive. PV34 matches exactly at four steps, so the match is not a chance hit, and PV34's identity as the figure's cell is never stated.
6. [does not affect a conclusion] Cell 0 table: figs1g is listed as blocked with no reason code. The two model claims rest on a timing not shown in the notebook (cell 24).

I found no misreading of the paper in the claims file. Table S1 lists the columns as dPC, sPC, PV (Rin 124 / 117; resting potential −86.6 / −80.9), and the claims assign these correctly. The helper functions behaved correctly on synthetic sweeps: step onset and offset exact, spike counts exact, input resistance 100.0 MΩ under both readings, sag 12.0 mV against 12.0 expected.

**C. What I could not check**

- **SimTracker's CellData tool.** The data descriptor names this tool (mariannebezaire.com/simtracker) as the way to compute the cells' intrinsic properties. Its definitions of rheobase, sag and threshold may be the ones behind Table S1. The notebook did not consult it, and I could not run it. Its rheobase definition, or its rheobase for the 17 PCs, would settle whether the +150 pA gap comes from the method.
- **ATF header line 8** (per-sweep injection start times). The notebook does not print it. Printing it would confirm the onset found from the data.
- **Per-cell rheobase under the −20 and +10 mV thresholds.** This would close problem 4.
- **The model timing in cell 24.** It is not reproducible from the notebook's outputs; a logged run would support the too_large reason.
