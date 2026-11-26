I've written `claims/mckenzie-2025.yaml`. The quote checker passes: 28 claims, 28 quotes, 25 statistical values, 0 problems. Nothing is committed.

**Text read.** `paper/10.7554-elife.105183.txt` is eLife Reviewed Preprint version 1 (January 31, 2025, marked "Not revised"), although its header says "version of record". It has the main text, all eight figure legends, the Methods, and the legends of Supplemental Figures S1 to S7. There is no other supplement and no PDF, and I opened no figure. The paper links no code and has no data or code availability statement.

**Claims.**
- **Totals:** all 28 have quotes, 16 record statistics, 28 have criteria, and 1 has expected values (ensemble size: mean 253.8 neurons, range 191 to 363).
- **Photometry (13 claims, Figures 1 to 6 and S1 to S5):** these recordings are the paper's own and are not in DANDI:000552. The paper deposits them nowhere, so these claims are marked not testable.
- **Spiking (14 claims, Figures 7, 8, S6 and S7):** these reuse the Huszar et al. 2022 data in DANDI:000552 (version 0.230630.2304; 3 mice, 8 sessions).
- **Cross-dataset (1 claim):** the paper's by-eye match between NE decay and the time course of representational settling.

**Details the paper leaves open, with the readings named:**
- **Session count:** the novel environments are listed as 3 linear tracks, 3 figure-eight mazes and 1 arena, which is 7, but every test has 7 degrees of freedom, which implies 8 sessions. The author takes every session that fits the description and reports the count. Where a session has two novel environments, the paper doesn't say which was used, so both the first and the second are run.
- **Cell types:** no thresholds are given for separating pyramidal cells. The criteria use the dataset's own labels.
- **Nearest-neighbour search:**
  - The 1×1 cm location bin is borrowed from the place-field section.
  - Only the bin itself is excluded, because the text says "any other moment".
  - Speed filter: either none or 5 cm/s.
  - Nearest neighbours for the movement differences: 3 (Methods) or 1 (Figure S7C legend).
- **"Minute 10":** either 600 to 660 s (as Figure 8B states) or 540 to 600 s.
- **Decorrelation fit (Figure S6):** the "100-s moving average" is read either as the 60 s windows the figure labels or as a 100 s window. The fitted form is R = β·exp(−lag/τ) + c, and the decay rate is 1/τ.
- **Speed and acceleration:** either the Kalman filter used for the photometry mice or smoothed finite differences.
- **Figure S7E/F model:** either the two-exponential form of the photometry model or a linear model.
- **Ripples:** the recording channel is not named. The pre-experience window is either the 30 min before the novel run or the first 30 min of the recording day. The track vectors are either z-scored or raw counts.
- **Tests:** t(7) over 8 sessions is read as a paired t-test. Two-sided is a standard choice.
- **Claims where the paper gives no test or measure:** the UMAP embedding, in-field versus out-of-field firing, the movement differences over time, and the absence of pre-experience reactivation. Their criteria use a standard choice and mark it as an assumption.

**Missing from the paper:** the photometry data, so 13 claims cannot be tested. No analysis code exists to settle the open choices above.
