## Report on claims/001326/10.1126-science.adt3971.yaml

**Checker, after my edits:** `52 claims, 52 quotes, 56 statistical values, 0 problems` (before them: 50 claims, 39 statistical values, 0 problems).

I checked every claim against the main text, Methods, legends and table S3, and against the paper's mouse analysis code. I downloaded that code (`analysis.py`) from Zenodo; its md5 matches the one in the file. All tolerances are correct: each is 1.96 × s.e.m. from table S3. The epochs, windows, unit selection, weights, timescale and coupling series, and model fitting all match what the file says the code does.

**Changes, by claim**
- **fig1p-anesthesia-abolishes-both:** the criterion said the paper reports no test. Table S3 (fig. S5 D and E) does report paired t-tests with FDR correction for ketamine/xylazine (K/X) on early and late closure. Those tests and their values are now the claim's statistics, expected values and criterion, and fig. S5D/E is added to the source.
- **fig4g-ketamine-alters-slow-clusters:** table S3 gives 64 ketamine puffs (8 series), but the code uses series 23 to 32 (10 series). The conflict is now named; the criterion follows the code and records the difference as a deviation.
- **fig4de-response-clusters:** the 0.25 s bound for "rapidly and briefly" and the 1 to 2 s test for "persistently" are not in the paper. They are now marked as readings.
- **fig4i-rise-times-unchanged:** the Methods keep regions with at least 30 units; the code keeps regions with more than 30. The Methods count is now named as a variant.
- **fig6j-mouse-coupling:** reading (a) did not say which ten series it uses. It now uses the code's series (Pre 1 to 10, Ketamine 23 to 32).
- **figs6-vpm-muscimol:** fig. S6B and S6H added to the source, since the "fast early closure" part of the statement rests on them.
- **Added figs2g-scaling-puff-number:** late closure scales with puff number but not with puff pressure (fig. S2F/G, cited in the Results). It had no claim.
- **Added figs2h-dose-response:** the dose thresholds stated in the Results (fig. S2H to J). The paper does not say which comparisons the FDR correction covers, so two readings are named and the outcome must hold under both.

**Still open (recorded under `checks`)**
- The paper does not name the animal it excluded from Figs. 5 and 6. The file already runs every mouse whose removal leaves 11 sessions from 9 mice.
- Many qualitative claims depend on cut-offs the paper does not give (for example "dozens" of regions, decay thresholds, the half-peak measure, the 0.1 closure bound). Each is named as a reading in its criterion, and the outcomes may depend on them.
- In figs30-correlation-structure, the start of the ketamine period is taken from one code function. Another function defines it differently, and the correlation analysis itself is not in the released code.
- The model fitting windows in fig5g and figs33 are read from the plotting code. The model's input timing is a global variable the released code never defines.

**Ready:** yes. The last check entry has `ready: true`. Only the claims file was changed; nothing is committed.
