I checked the claims file for DANDI:001341 against the paper and its SI and made 13 corrections plus one added claim. The file is ready for an attempt.

**Checker result:** `claims/001341/10.1073-pnas.2514107123.yaml: 33 claims, 32 quotes, 6 statistical values, 0 problems`. Before my changes it was 32 claims, 31 quotes, 0 problems.

**Changes, by claim** (each is also recorded under `checks`):
- **Header:** added which figures Table S1 assigns to animals 480 (Fig. 2I, 2L), 489 (Fig. 3E, F, Q, R) and 589 (Fig. S12).
- **fig1lm-staged-modulation:** the epoch 1 window (-1 to 0 s) was stated as fixed, but the paper gives only t < 0. It now names two readings, -1 to 0 s and -0.5 to 0 s.
- **fig1o-trial-end-ramp:** ramp onset was defined without saying the paper leaves it open. It now uses the two onset readings of fig4b-ddm-matches-ramp.
- **figs1-running-speed:** the SI gives the same 21 ± 4 cm/s for habituation day 3. Added that as a reading, usable only if the dataset holds habituation sessions.
- **fig2a-success-rate:** where lateral position is measured from is not given in the paper. Named it as open, with readings.
- **fig2i-ft-rt:** Table S1 assigns Fig. 2I to both 573 and 480; the claim named only 573. Added 480 and the two pooled as readings.
- **fig2jk-glm-mixed-tuning:**
  - The regressors were miscounted: the list named 12 variables and called them "13 regressors plus V_wall". The 13th variable is now marked as open.
  - Added a second reading of "among the strongest" (largest mean log likelihood ratio).
- **fig2l-running-vs-sitting:** the claim said the animal is not named, but Table S1 names 480. It is now judged on 480.
- **fig3-wall-kinematics:** the claim said Table S1 gives 489 for Fig. 3P. Table S1 gives 589 for Fig. 3P and 489 for Fig. 3Q. Corrected, and both animals are now readings for the first-touch fraction.
- **fig3ijkl-whisking-across-epochs:** what the t tests compare (whisk cycles or per-trial means) is not given; both are now readings.
- **fig4-ddm-fit:** which trials the reaction times come from is not said. The 266 trials of Fig. 4B and the 520 of Fig. S7C-D are now readings.
- **fig4g-varce-population, fig4j-corce:** these now say that their tests and thresholds are this file's own, not the paper's.
- **New claim, figs12-tuning-lost-during-decision:** the Results finding that most units lose their tuning during the decision (Fig. S12B-C) had no claim. The animal is open: Table S1 lists 589, which has no recorded units, and 579 has too few trials.

**What remains open:**
- Several criteria use decision rules of this file where the paper reports no test: fig1lm, fig1-ramp-contralateral-only, fig2c, fig4f, fig4g, fig4j. Each says so.
- The paper contradicts itself in places, and the header lists these: unit counts, trial counts for animals 489 and 503, the layer of unit 489101, the number of animals in Fig. 2C-D, the drift-to-bound ratio against the reported drift and bound, "statistically identical" against P < 0.0001, epoch 2 timing against first touch, and the streak index scale. None can be settled from the paper.
- Tables S2 and S3 (fitted model parameters) are images, and no PDF renderer is installed here, so I could not read them. The DDM values rest on the main text.

**Ready:** yes. The file now ends with a `checks` entry saying so (`ready: true`). Nothing was committed.
