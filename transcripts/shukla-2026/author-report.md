All five Author steps and the handover are done, finishing at 19:40 UTC (1 h 23 min of the 5 h). The entry check passes with 0 errors, and the notebook runs in 14 minutes from a clean environment. Nothing was committed.

**(1) Outcomes** (35 claims: 4 reproduced, 7 partially reproduced, 10 not reproduced, 14 blocked)

| Claim | Outcome |
|---|---|
| fig1e, fig1f, fig1i, fig4i | blocked, methods_underspecified: the two ANOVA readings in the claims file disagree |
| fig3e | blocked, methods_underspecified: the ANOVA readings and the two readings of "optimal" triplet disagree |
| figs3 | blocked, methods_underspecified, by its own criterion (readings shown, not judged) |
| fig6 | blocked, methods_underspecified: simulation with no published code and missing parameters |
| figs1, fig2b, fig2c, fig2e, fig2f, fig3g, fig3h | blocked, data_missing |
| fig1g, fig1h, fig3c, fig3d, fig7b | partially reproduced (rests on an assumption) |
| fig4eg, fig7c | partially reproduced |
| fig4d, fig5d | reproduced |
| fig7e, fig8d | reproduced (rests on an assumption) |
| fig4b, fig4c, fig5e | not reproduced |
| fig1j, figs2, fig4h, fig7g, fig7h, fig8b, fig8e | not reproduced (rests on an assumption) |

**(2) Dataset, assumptions and questions**
- **What it holds:** version 0.260526.1807 is pinned. The paper cites no version. The code repository's README names 0.260519.1308, which turned out to be a partial upload; all of its 1,007 assets are in the pinned version unchanged. The dataset has 10 same-genotype pairs (5 WT, 5 Fmr1), each with both contingencies.
- **What it lacks:** there are no mixed pairs, no sensory-deprived sessions, no visual-cue task and no virtual-agent task.
- **Duplicates:** both files of a pair session hold identical events, so each recording is counted once.
- **Clock check:** positions and pokes share a clock. At a poke the head is a median 2.7 cm from the well; with poke times shifted by ±5 to 10 s it is 30 to 46 cm away.
- **Findings recorded:**
  - About 4.8% of pokes are near-simultaneous pokes at two wells by one rat, which looks like sensor crosstalk. One rat session has 128,979 pokes and 2,447 transitions.
  - The matched pokes never repeat the previous match's well, a rule the files don't describe, and poke offsets are not stored.
  - Session numbers have gaps for three pairs.
  - Session epochs run 10.7 to 57.2 min, against the paper's 20 to 30 min.
- **Assumptions:**
  - Crosstalk pokes are dropped, with the raw sequences shown as a variant.
  - For the Figure 1H shift test, matches are rebuilt from the pokes with a 6 s hold. The rebuilt counts agree with the dataset's at r = 0.994.
  - Synchronous and asynchronous matches, gaze trials and follower trials are built from the poke sequences.
  - For fig4h I adopted the reading the Methods text describes most directly.
- **Questions for the paper's authors:** recorded as four `methods_unavailable` findings, covering the ANOVA type, rate units, event and trial definitions, and the reinforcement-learning parameters.
- **Questions to a reader:** none.

**(3) Where the protocol was unclear**
1. The claims file blocks a claim whenever ANOVA readings A and B disagree, while protocol step 1.6 allows adopting the best-supported reading. Reading A matches the paper's printed df. I followed the claims file, which blocks 5 claims.
2. The protocol says to trust the data, but gives no rule for removing obvious sensor artefacts. I removed them as a stated assumption, showed the raw data as a variant, and recorded a finding.
3. Some criteria have no rule for a result that is neither reproduced nor blocked (fig3c, fig4eg, fig7b). I used the protocol's definition of partially reproduced.
4. Nothing says whether a faster equivalent computation is allowed. For the Figure 1J null I used a modal-class shortcut; it agrees with scikit-learn on 98% of real folds, and I recorded it as a deviation.
5. `measured` is only defined for when a reading matches. When none did, I recorded the reading the outcome rests on, or the first one listed.
6. R, glmmTMB and pymer4 are not available in the locked environment. I fitted the GLMMs by variational Bayes in statsmodels and recorded that as a deviation, without blocking.
7. The version to pin was ambiguous because only the code README named one, and that was a partial upload. I pinned the latest version, which contains all of it.

**(4) Runtime and failures**
- 1 h 23 min in total; the notebook runs in about 14 min, about 4 of them streaming 1,120 NWB files.
- No claim was blocked for time.
- Problems fixed during development:
  - Requesting the S3 URL directly returned 403, so the S3 address is now read from the asset metadata instead.
  - The Figure 1J null at first took 8 minutes until I vectorised it.
  - A mode-name bug made the two downsampling readings identical until fixed.
  - The GLMM with Δt in seconds did not converge, so that reading is fitted in minutes, which is the same model.
- The run left an empty `.claude/.cc-writes` folder in the entry directory; it comes from the harness, not from me.
