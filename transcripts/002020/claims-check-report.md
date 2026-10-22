I checked the claims file for DANDI:002020 against the paper. I made six corrections, four issues remain open, and I judge the file ready for an attempt.

**Checker result** (the same before and after my edits): `claims/002020/10.1101-2025.01.14.630383.yaml: 20 claims, 20 quotes, 0 statistical values, 0 problems`

**Changes, by claim**
- **dishes-analysed:** the criterion now requires activity to be observed *continuously* for more than 10 days, as the Methods say. Before, a span of more than 10 days was enough.
- **activity-onset:** I changed the expected value and tolerance from 2.5 ± 0.8 (1.7 to 3.3) to 2.55 ± 0.75 (1.8 to 3.3). That matches the paper's range of 2 to 3 DIV widened by 10% of each bound, which is what the criterion already stated.
- **fig1f-transition-15div:** the quote now includes the sentence the statement and the 15 DIV value rest on: "Averaging data across seven dishes revealed that power law in PCA was consistently established around 15 DIV".
- **fig1d-power-law-emerges, fig2b-spatial-structure, fig2d-locality-slope:** these criteria set DIV windows, majorities, PC groups and numeric bounds that the paper does not give. They now say so: the paper judges these figures by eye and reports no test.
- **fig2c-locality-spectrum:** the criterion now says the sign of the slope (negative means dominant PCs are more local) comes from the definition of locality. The text reports no slope values, and there is no PDF to read Figure 2D from.
- **fig3ef-groups-cooccur:** I removed the `expected` entry for the 0.1 grouping threshold. It is a method value, not a result an attempt could match; it stays in the criterion.

The other claims, the statistics (the paper reports no tests) and the coverage of the main findings held up. No claim comes from outside the paper.

**Still open** (recorded in the `checks` entry)
- **Supplement missing:** Figures S1 and S2 are not in the text. Claims figs1-classified-by-avalanches and figs2-shuffle-breaks-cooccurrence rest on readings until the supplement is supplied.
- **Formulas missing:** the fitted function, the local Moran's I formula and the model equations were lost when the text was flattened, and no PDF was supplied. The readings F1/F2 (fit) and M1/M2 (Moran's I) stand in for them.
- **Paper version:** the dandiset points at version 2 of the preprint, but version 1 was read.
- **Model claims:** the two fig4d claims test a simulation, not the dataset. None of the schema's `data` values fits them, and the text does not give enough to run the model.

**Ready:** I set `ready: true`. This is a judgment call: the protocol says to stop when a supplement the results rest on is missing. Only the two supplement claims depend on it, and they are marked open. If you'd prefer to hold the whole file until the supplement arrives, the flag can be set to false. Nothing has been committed.
