I wrote `claims/001340/10.1371-journal.pcbi.1013226.yaml`. The quote checker passes: 38 claims, 38 quotes, 63 statistical values, 0 problems. Nothing is committed.

**Text read.** The version of record from Europe PMC (PMC12233953, update of 2025-07-07). It has the full Results, figure legends, Table 1, Methods, the S1 to S8 Fig legends and the peer review history. The supporting figures are images and were not supplied, so claims from S1 to S8 rest on their legends and on the Results sentences that cite them. There was no PDF. The bioRxiv preprint is also under `paper/`, but I did not use it.

**Code read.** `github.com/Wilbrecht-Lab/cogmodels` at commit 589555c. It holds the cognitive models, their fitting, simulation, parameter recovery and model identification. It has none of the photometry or neural analysis code.

**Counts.**
- 38 claims, all with quotes; none needed `inferred`.
- 16 claims carry statistics (35 entries).
- 21 have expected values.
- All 38 have criteria.
- All use the dataset itself.

**Where the Methods and the code disagree** (Methods followed, code run as a variant):
- **RLFQ3p forgetting rate:** the Methods give (α+ + α−)/2; Table 1 and the code give 1 − (α+ + α−)/2.
- **BIfp pseudo-RPE:** the Methods say observed minus expected reward, read as r − [0.75·b + 0.0001·(1 − b)]; the code computes r − b/2.
- **Simulations:** the Methods say 1000 per model on blocks of 7 to 23 rewards; the code and the S2 legend use 500 runs, and the code uses 500 trials and blocks of 8 to 15 rewards.

The code also settled several things the Methods leave open, such as fitting per mouse and how PearceHall's parameters are counted.

**Details left open, with the readings named:**
- **Trial cleaning:** the side-port gap limit is given as both 1 s and 6 s.
- **Dopamine signal:** the airPLS and robust-regression settings are not given; the processed signal is used if the dataset has it.
- **Session selection:** it relied on visual inspection, which cannot be redone. Readings: use the sessions the dataset marks, or apply the AUC-ROC rule.
- **Dopamine regression (Fig 4F):**
  - It is unclear what "featurized covariates" means.
  - The 70-30 split, the number of repeats and what the bootstrap runs over are not given. Readings: random splits summed over animals, per-animal values, or splits by session.
- **RPE-only regression (Fig 4H):** whether the RPE has two slopes or one; whether the trials are the Fig 4G subset or all cleaned trials.
- **LMER (Fig 4I, J):** the form of the random effects; whether DA is the peak/trough measure or the 0–1 s mean.
- **Reward and omission estimates:** read as an OLS without intercept, the only coding that gives both estimates. The paper prints the reward estimate once as negative; I read it as positive.
- **Model comparison t-tests:** the Holm family (six or seven models), one- or two-sided, and whether ± is an SD or an SEM.
- **Behaviour measures:**
  - "Just after pre-training" could be session 1 or all sessions.
  - Trials after a block switch could be counted from 0 or from 1.
  - Averages could be pooled over trials or blocks, or taken per mouse.
  - "Following the first 7 sessions" could mean sessions 8 to 14 or sessions 1 to 7.
  - The regression unit for the session slope could be the mouse-session or the trial; mouse-session fits the reported t and p.
- **Switch probability by history:** model values could be predicted probabilities or emulated choices.
- **AIC around block switches:** trials 0–4 or 1–5, with or without the 2k penalty, and the mean or the sum over mice.
- **Reward-switch-reward count:** which sessions make up the 30,707 trials (the 34 valid sessions fits).
- **Thresholds the paper never gives:** "poor identifiability", "high recovery", "little to no effect", "consistent", and the port-duration alignment. Each is written as an explicit reading in its criterion.

**Missing from the paper.**
- None of the neural analysis code is shared, so every Fig 4 method rests on the Methods text alone.
- The S1 to S8 figure images are not in the text.
- No sentence gives a result for the S6 Fig B blocking model, so it has no claim.
- One sentence cites S4 Fig where S1 Fig defines the measure.
- The paper lists the history counts as "RR, RU, UR, RU"; I read the fourth as UU.
- The fibre-placement histology (Fig 4A) is verification, not a finding, so it has no claim.
