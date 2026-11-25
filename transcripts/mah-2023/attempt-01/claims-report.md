I've written `claims/mah-2023.yaml`. The quote checker passes: 30 claims, 30 quotes, 28 statistical values, 0 problems.

**Text read**
- The version of record (Nat Commun 14:7573) as served by Europe PMC (PMC10663503): main text, legends and Methods.
- Three supplement files: the Supplementary Information (Supplementary Figs 1–14 with legends), the peer review file and the reporting summary.
- There was no main-article PDF, and none was needed. Source Data are not in the text.

**Code read**
- github.com/constantinoplelab/published, folder `rat_behavior`, at commit b7b68ca8.
- It has figure scripts, analysis functions, the trial parser and the generative models. It does not have the model-fitting code.
- The fitted models are on Zenodo (doi:10.5281/zenodo.10031483). The claims file names them as outside data.

**Claims:** 30, all with quotes. 16 claims carry statistics (28 entries in total), and all 30 have criteria. 6 are claims of absence, each judged on the paper's own test. All are `data: dataset`.

**Details left open, and the readings named for each**
- **Population block tests (Fig. 1f, 1i):** the Methods compare z-scored means; the code compares raw means.
- **Supplementary Fig. 2b:** the legend says two-tailed; the code runs one-tailed tests.
- **Fig. 2k, which trials:** the Methods use 20 μL mixed-block trials; the code uses all mixed-block trials. For the population test, the legend says rank-sum; the code runs a signed-rank test.
- **Fig. 2j population test:** the legend's rank-sum is primary; the code's signed-rank is a variant.
- **Previous rewards in the initiation-time regression:** 9 in the Methods, 10 in the code.
- **Detrending:** the Methods fit each session; the code fits one line over pooled sessions.
- **Fig. 3l lambda groups:** split at the 20th/80th percentile in the Methods and legend, at 40th/60th in the code. The legend and Results also disagree on which logistic parameter differs, the p-values and N (116 vs 180).
- **Fig. 2f:** the Results print r = 0.08, p = 0.18; the legend prints r = −0.03, p = 0.53. Both are recorded.
- **Bayes observer "variance":** undefined, and so is the unit of the test. I named two variance readings, each tested over trials and over per-rat means.
- **Pre-cue sessions (Fig. 5):** the Methods start after 30 pre-cue sessions; this offset is not visible in the code.
- **Model fitting (Fig. 3j, Supplementary Figs 8 and 9, Fig. 3l):** the free parameters, bounds and folds are not fixed, because the fitting code is missing.
- **Qualitative claims with no test in the paper** (Fig. 2a–b, Supplementary Fig. 5, Fig. 3c, Fig. 4a/c/d, Fig. 5b/d): the windows and ordering rules are stated as readings.

**Missing from the paper**
- No fitting code for the wait-time models.
- No reported test for the transition-dynamics, training and catch-probability claims.
- The sex counts disagree within the Methods (184/107 vs 160/114).
- Whether the dandiset holds the 16 pre-cue rats, the sessions that failed inclusion (needed for Fig. 4) and the catch probabilities is left for the author to check.
