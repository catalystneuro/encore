I've written `claims/mansvelder-2026.yaml`. All 43 quotes pass `tools/claims_check.py` and the schema check is clean. The checker still exits with 30 problems: all are p-values from Supplementary Table 3, which is not in the text file, so the checker cannot find them. I checked each against the supplement PDF; 8 of them are rounded forms of what the table prints. The repository's code had not been read when I wrote this. The paper's own code link returns 404.

**Text read.** The Research Square preprint, version 1 (posted 2026-10-12): main text, Methods, statistics section and the legends of Figs. 1–8. The text file holds the supplement only up to Table S2b, where it is cut. I read the rest of the supplement PDF (Table S3 statistics, Table S4 blocker donors, Table S5 model parameters, the end of the Fig. S6 legend) from its text layer with pypdf, because no page could be rendered. No figure was seen. That includes the Fig. 3b schematic of how sag ratio and input resistance are calculated.

**Code.** github.com/nsham2/Shamugia_et_al_2026 returns 404, so no analysis code was read. I read IPFX v2.0.0 (commit 1ddc0e5), which the paper cites, for its sag, input resistance and chirp routines. It is used only as a named reading where the Methods are silent.

**Counts.**

| Item | Number |
|---|---|
| Claims | 43, all with quotes |
| Claims with criteria | 43 |
| Claims with statistics | 31 (105 p-values) |
| Claims with expected values | 18 |
| Data type | 28 `with_inputs`, 9 `elsewhere` (Allen RNA-seq, the model), 5 `with_labels`, 1 `dataset` |

The `dataset` claim is the ZD7288 blocker experiment. Its new recordings are only available on request.

**Details the paper leaves open, with the readings named:**
- **O1, chirp analysis:** LOWESS fraction, FFT window, frequency range, and where Z0 and f3dB are taken. (a) IPFX averaged chirp, then LOWESS 0.04 (the value given for the model); (b) the same, limited to 0.4–40 Hz.
- **O2, sag ratio:** (a) IPFX sag on the sweep closest to −100 mV; (b) the same formula on the −100 pA step.
- **O3, input resistance:** (a) IPFX slope across hyperpolarizing steps; (b) a single step.
- **O4, the Vm covariate:** (a) pre-chirp baseline; (b) resting potential.
- **O5, mixed models:** (a) Satterthwaite Type III tests (SPSS or lmerTest); (b) statsmodels MixedLM. GEE is shown as a variant.
- **O6, χ² tests:** the Methods describe goodness of fit, which matches the per-subclass values in Table S3. The overall values (43.05, 44.98) match a 2x2 Pearson test without continuity correction. Both readings are named.
- **O7, ZD7288 sample size:** n = 7 cannot give the reported p = 0.004 with an exact Wilcoxon test; 9 cells can. Table S4 lists 8 cells. (a) Cells per measure; (b) cells with all four measures.
- **O8, gene correlations:** (a) CPM; (b) log(CPM+1). The test family is the 20 tests listed in Table S3.
- **O9, Fig. 4b regression direction:** (a) dendritic length on depth; (b) depth on dendritic length.
- **Smaller ones named in criteria:** how L2/L3 cells are selected, which cells enter the Fig. S1 tests, and the frequency ordering of the Fig. 7 morphology result, which the Results and Discussion state in opposite directions.
- **O10, text against Table S3:** recorded where they disagree (χ² 42.76 vs 43.05, mouse n 268 vs 248, several p-values, permuted Fig. 5j medians). Table S3 also contradicts the Fig. 5l "did not differ" claim (VIP p = .046, PV p = .031).

**Missing from the paper:**
- **Data locations:** no archive is named for the mouse recordings, the cultured recordings, the Lee et al. 2023 data or the Patch-seq transcriptomes. There are no per-cell subclass labels, Vm or pia-soma distances.
- **Dandiset coverage:** DANDI:000630 holds only the Chartrand human layer 1 subset, so most claims depend on outside data.
- **Model:** the adapted model is not deposited, and Table S5 does not give the calcium-channel density. The model claims after `fig7-model-ca` can only be rebuilt in part.
