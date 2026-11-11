**Verification report, round 2: Mah et al. 2023 on DANDI:001169 (0.260825.1909)**

The claims file has 33 claims. The attempt record has 33 outcomes: 23 reproduced, 3 partially_reproduced, 2 not_reproduced and 5 blocked. Five of them carry `assumed: true`: fig3i, fig3f, suppfig9, fig3l and fig5c.

### 1. Outcomes

**The 18 unchanged reproduced outcomes.** I agree with all of them: cohort-size, fig1e, fig1f, fig1i, suppfig2, suppfig3, fig2a, suppfig5, fig2c-d, fig2e, fig2f, fig2g-h, fig2j, fig2k, fig2l, suppfig6, fig3c, bayes, suppfig12, suppfig14, fig5b and fig5d. The re-executed outputs match round 1 or move trivially (fig2e p = 1.25e-45; fig2f p = 0.572).
- fig2g-h now passes on the paper's test (cell 46: p = 0.187 and 0.200) and on the Methods variant (0.223 to 0.260).

**pre-cue-session-link, partially_reproduced.** I agree (cell 86: 14 of 16 rats).

**fig3i, partially_reproduced, assumed.** I agree, and the assumption is stated and reasonable: J004's parameters are used for every rat in the Fig. 3i part.
- Under the criterion as written, with no threshold, the alternatives show both features at 3 of 6 settings (cell 64).
- The noise-only control's 95th percentiles come from only 20 replicates ("positive in 16 of 20"). The decisive margin is small: the RPE model at 0.8 has an overshoot of +0.0284 against a percentile of +0.0291. The control therefore cannot reverse the outcome.
- The deviation saying the Fig. 3i direction "follows from the model's update rule for any small positive alpha_0" has no output behind it.

**fig5c, partially_reproduced, assumed.** I agree, and adopting the legend's 20 µL reading is stated and reasonable. The 20 µL reading fails the population test (cell 92: rank-sum p = 0.0676 by date, 0.47 after 30 sessions).
- The confound argument is not verified in the data. It says post-violation trials repeat the previous offer.
  - If a 20 µL trial after a violation always repeated the offer, its previous offer would be 20 µL, and such trials are excluded from both groups.
  - Yet dropping post-violation trials changes the 20 µL result: 14 rats become 15, and p goes from 0.0676 to 0.611 (cell 92).
  - So offers are not always repeated. The notebook should print the share of post-violation trials that repeat the offer.
- Under the 20 µL reading the per-rat rank-sum flags rats whose mean difference is close to 0, all at p = 0.0000 (cell 92):
  - E008: +0.0007
  - S042: −0.0073
  - M044: −0.0173

  The count of 14 (expected 13 ± 1) is weak support for "modulated", and only 9 of the 14 are in the claimed direction.

**fig3f, not_reproduced, assumed.** I agree.
- The assumption is stated: the likelihood is over opt-out catch trials, fitted with L-BFGS-B. It is reasonable, and parameter recovery on J004 works (within 0.004).
- The effect is the model's own: mislabelled mixed trials combined with kappa_low < kappa_mixed. So it would likely appear under any fit that produces the block effect.
- The paper gives no test for this panel, so the failure rests on the claims file's reading (p ≥ 0.05). The record says so.

**suppfig9, reproduced, assumed.** I agree. The labels depend only on H0 and the session resets. The fold assumption (whole sessions) is stated, and it barely matters because the inference does not use the fitted parameters. Result: 230 of 291 rats, p = 9.72e-23 (cell 71).

**fig3l, not_reproduced, assumed.** I agree, with a caveat that should be in the notes.
- The refit puts 128 rats at the lambda bounds: 59 at 0 and 69 at 1 (cell 74). The paper's 20/80 split gives N = 116, which ties at the bounds could not produce. So the refit's lambda distribution is not the paper's, and the groups come from a tie-break, not the paper's rule.
- The failure therefore cannot be separated from the refit.
- The 40/60 split has no ties and also fails: wait time C p = 0.197 at mixed to low; initiation D p = 0.006 at mixed to high.
- The assumptions (likelihood, lambda grid, tie-break) are stated.

**fig3j and suppfig8, blocked as too_large.** I now accept the reason. By cell 98 the retrospective refit alone takes 1.08 h on 4 cores, plus 1.20 h for the inferential and belief state fits. The numbers in the record are stale (see 2).

**fig4a, fig4c and fig4d, blocked as data_missing.** I agree. The reason for not running a partial test is stated and reasonable.

### 2. Text against outputs

**The fig3j and suppfig8 timings are stale.** They do not match the re-executed cell 98, or cell 102 (run time 45.3 min).

| statement | where | stated | cell output |
|---|---|---|---|
| fig3j notes | record | 0.15 ms per evaluation (19 ms pure Python) | 0.253 ms (28.3 ms) |
| fig3j notes | record | inferential fit about 0.65 s per rat | 1.24 s |
| fig3j notes | record | retrospective 2.6 h on one core (0.64 h on 4) | 4.32 h (1.08 h on 4) |
| fig3j notes | record | inferential and belief state fits 0.6 h | 1.20 h |
| fig3j notes | record | about 3 h in all | about 5.5 h |
| fig3j notes | record | "the 26 minutes the notebook already takes" | 45.3 min (cell 102) |
| suppfig8 notes | record | "about 3 h on one core in all" | as above |
| fig3j, suppfig8 responses | record | 0.15 ms, about 3 h | as above |
| fig3f response | record | "3 min for all rats" | 361 s (cell 68) |
| fig3l response | record | "2.5 min for all rats" | 277 s (cell 74) |
| Summary | cell 101 | fits "estimated at about 3 h on one core" | cell 98 gives 4.32 h + 1.20 h |

**Minor mismatches:**
- Cell 0 and the README say loading takes "about ten minutes"; cell 3 shows 13.5 min.
- Cell 44 and the fig2f notes say both readings are "close to the legend's r = −0.03, p = 0.53". The code reading is r = +0.023, p = 0.693, which has the opposite sign.

**Everything else is supported.** Every other sentence of the Result cells (14 to 96), the Summary, the README and the record notes matches the printed outputs.

**My round-1 reasons in the record.** They are stated faithfully; most are close paraphrases of my report. One inconsistency: the record's fig3j notes call the first run's estimate "138 h", while my reason quoted in the record says 162 h (155 h for the retrospective part).

### 3. Round-1 points

**Resolved:**
- **2 (fig5c):** the outcome was changed and the legend's reading adopted. A new premise check is open (see 1).
- **3 (fig2g-h):** the variants and the bound shares were added, and they agree.
- **4 (header misreading):** forwarded to a reader. I cannot see that file.
- **5 (timing and block reason):** a compiled timing and real fits were added. fig3f, suppfig9 and fig3l are now tested, and too_large is supported by cell 98. Only the text is stale.
- **6 (Fig. 4 partial test):** the author declined, with a stated reason.
- **7 (fig2k):** the directional count is now in the notes.
- **8 (male volumes):** the regressions now use male volumes; the coefficients moved by at most 0.001.
- **9 (smaller points):** each is now documented as following the code, and a variant (opt-out filter) or a pooled test was added where relevant.
- **10 (fig5b dependence on the link):** stated in the notes.

**Partly resolved:**
- **1 (fig3i overshoot measure):** controls were added and reported. The measure still does not separate the models, and the control is thin (20 replicates, a 0.0007 margin). The outcome follows the criterion, so this does not move it.

**What remains that bears on a conclusion:**
1. **fig5c.** The confound argument assumes offers repeat after violations, and cell 92 shows they do not always repeat. The per-rat count under the adopted reading includes rats with mean differences near 0. The outcome holds either way, because the 20 µL population test fails, but the stated reasoning needs the repeat rate printed.
2. **fig3l.** The not_reproduced outcome rests on a refit whose lambda distribution (128 rats at the bounds) is not consistent with the paper's N = 116. The notes should say the failure may be the refit's.
3. **fig3j and suppfig8.** The cost figures in the record and the Summary must be updated to cell 98's numbers (about 5.5 h on one core). The blocked status stands.
