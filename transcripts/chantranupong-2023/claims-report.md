I wrote `claims/001767/10.1038-s41586-023-06492-9.yaml`. The quote checker passes: 46 claims, 46 quotes, 29 statistical values, 0 problems. Nothing is committed.

**Text read:** the version of record from Europe PMC (PMC10511323): main text, Methods, figure legends and Extended Data legends, plus the Supplementary Information PDF (Supplementary Results, Discussion and Methods). There is no PDF of the article, so I never saw the figures; each panel is described from its legend and the Results.

**Code read:**
- `lchantran/AchDA_manuscript_photometry` at commit `cd8caf0e`: signal processing, per-mouse statistics, LDA and cross-correlation.
- `lchantran/AchDA_manuscript_behavior` at commit `20c0edb0`: block-transition statistics, the behaviour model (RFLR) and the statistical tests on behaviour.

Neither repository holds the GLM code or the ANOVA across the three genotypes.

**Counts:** 46 claims, all with quotes and none `inferred`. 17 claims carry statistics (29 entries), all 46 have a criterion, and 6 have expected values (the GLM R² values and the LDA accuracy before side entry). All claims use `data: dataset`; the paper uses no outside data.

**Details the paper leaves open, and the readings named:**
- **Windows:** the Methods give 17 samples (0.918 s) before or after side entry but not whether the side-entry sample counts. The two readings are +1 to +17 and 0 to +16. The code's windows (19, 18 and 11 samples) are recorded as variants only.
- **Per-mouse t-test:** the Methods say "paired", but trials from two conditions in one mouse can't be paired. Per mouse, the test is the code's two-sample t-test (`ttest2`); across mice, a paired t-test of per-mouse means is reported alongside.
- **Delta-Ach:** computed per trial, as the code does it. Taking it from the trial-averaged trace is shown but doesn't decide.
- **LDA "higher than 80%":** read as the mean over mice or as every mouse.
- **GLM:**
  - which predictors: the six events the text names, or those plus the other recorded events;
  - how data are pooled: all mice together, per mouse, or per session;
  - number of runs: Y = 10 or 3;
  - how the eight history predictors are defined.
- **Cross-correlation:** the Methods align to centre entry and use raw residuals; the code aligns to side entry and scales residuals by their s.d. The code's version is a variant. For the "side-entry time" in the 2D covariance, readings are side-aligned windows or the median side-entry time.
- **Drd2 ANOVA unit:** one value per mouse, or all trials pooled.
- **ΔF/F₀ baseline:** the session median, or a rolling 1-min baseline.
- **Control groups:** not named for the VLS-TelC behaviour comparison or for the Drd2 RFLR test (Extended Data Fig. 11i).
- **Bootstrap for conditional switching:** resampling by trials or by sessions, and 2- or 3-trial histories.
- **Untested panels:** where the paper gives no test (Figs 3d, 4b,c, 4e,f, 5a, 5c–f), the criterion uses thresholds I chose. Each criterion labels its threshold as one I named, not one from the paper.

**Conflict recorded:** the main text calls the Drd2-cKO RFLR coefficients "comparable", but the Extended Data Fig. 11i legend reports β (p = 0.014) and τ (p = 0.018) as significant. Claim `ed11i-cko-rflr` records the legend and flags the conflict as a deviation.

**Missing:** Supplementary Data 1, the statistics spreadsheet. It holds the exact P-values for Fig. 1e and Extended Data Figs 3e,f, 4c–e, 6d, 8i–k and 11d,e. Those claims record only the legends' threshold (two-sided t-test, P < 0.05). I wrote the claims without it because it holds only P-values, not methods.
