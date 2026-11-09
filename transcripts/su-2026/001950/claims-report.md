I wrote 37 claims to `claims/001950/10.1038-s41586-026-11026-0.yaml`. The quote checker passes every quote. It flags 2 p-values as "not found" (Fig 5g and Fig 6a, both p = 3.0e-4). I confirmed by reading that the text prints both as "p = 3.0 × 10 −4", so the checker most likely misses that number format. The quotes and values are as the paper gives them.

**Text read.** The version-of-record file under `paper/` holds only the abstract and the reference list. I therefore read the bioRxiv preprint v1 (doi:10.64898/2026.04.10.717727): Results, Methods, and the legends for Figures 1–6 and S1–S18, which the preprint carries inline. There is no separate supplement file, and nothing the claims rest on is missing. The flattened text lost the Methods equations and Table 3 (the model priors); no claim depends on either.

**Code read**
- `aind-beh-ephys-analysis` at 971c1ca: the physiology analyses. Its README says all physiology and behavior sessions are on DANDI:001950.
- `aind_stan_fit_sim` at 89371ee: the Q-learning model.
- The index repo `locus_coeruleus_norepinephrine_neurons` at 43f7083.

**Counts.** 37 claims; 36 have quotes and 1 is marked `inferred` (Fig S18d, whose legend gives only r and p values). 21 have statistics and 33 have criteria.
- 9 are anatomy, transcriptomics or patch-seq claims marked `data: elsewhere`. They point to the Code Ocean collection the paper names, which has no DOI.
- 3 are `with_inputs`: Fig 5d, 5h and S18d, which use the spatial axes derived from the retrograde tracing and MERFISH data.
- The other 25 rest on the dataset.

**Details the paper leaves open, and the readings named**
- **Switch definition:** against the previous trial (as the regression code does) or against the previous responded trial (as the code's Fig 5f and photometry do).
- **Extra regressors:** for respond/ignore and switch/stay, the Methods name only the event and a drift regressor, while the code adds switch, choice side and their interaction. Both are run.
- **Photometry regressors:** with the isosbestic signal (Methods) or with outcome and no isosbestic signal (code). Window for the outcome analysis: 2 s after outcome (Methods), 1.5 s (Results), or a bin aligned to choice near 0.7 s (code).
- **Photometry unit of sample:** per session (code) or per mouse. The legend says 9 mice, the code has 7, and the Methods say 14.
- **46.5% denominator:** all 241 neurons or the 216 with a defined coefficient. The code does not compute this figure.
- **76.8% "significant regression":** p of the outcome coefficient or the whole-model F-test. The code does not compute it either.
- **Fig 6a p-value:** from the linear or the kNN spatial test.
- **Fisher tests (Fig 5k, p = 7.8e-5; Results, p < 0.01):** axon sessions against all neurons (code), or axons pooled with cortex-projecting neurons against the other neurons, or cortex-projecting neurons against the rest.
- **Fig 6c rank correlation (rho = 0.84):** over session-averaged RPE bins or over pooled trials. The code computes no rank correlation, only a binned plot.
- **Fig 4h population:** the 241 task neurons or the code's 274 units from 21 mice.
- **Go-cue "increase" (240/241):** two-sided p < 0.05, as the code counts, or significant with response above baseline.
- **Fig 4c:** the number of lags and the R² measure.
- **Fig S12 trial counts:** which sessions are counted.
- **Fig S15t:** how a neuron pair is placed on a spatial axis.
- **Fig S18d:** which two axes the legend's correlations refer to.
- **Multiple-comparison correction for the spatial tests:** the code applies FDR, the paper names none, so uncorrected is the main reading.
- **Permutation count:** 5,000 in the Methods, 10,000 in the code. The Methods count is the main reading.

**Missing.** No claim lacked text it needed. Some claims need model variables (Q values and RPE). The code reads them from precomputed per-session files that are not in the repository. Whether the dataset holds them is for the author to find.
