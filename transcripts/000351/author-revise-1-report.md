I've answered every point in the round-1 report and changed two outcomes. The entry was re-run with `python tools/entry.py all`: no errors, and the notebook ran in 67 s. Nothing is committed.

**Outcome changes (both now match the verifier)**
- **figs8e-lick-bout-responses**: partially_reproduced → blocked (`methods_underspecified`). The three lick-bout windows give different results for the non-consummatory test. The claims file's header says that case is blocked.
- **fig4p-background-faster-decay**: partially_reproduced → not_reproduced. The criterion needs background below extinction at p < 0.05 under every reading, and none gets there (p = 0.053 for (a) and (c), 0.097 for (b)). The notebook now says readings (a) and (c) are the same test in different units, so only two were independent.

All other outcomes are unchanged: 27 reproduced, 1 partially reproduced, 2 not reproduced, 8 blocked.

**What I added or corrected**
- **Dopamine values for trials with missing dF/F samples:** The paper's own Matlab function also uses `nansum`, so the port already matched the code. What was wrong was the notebook text saying these trials were dropped. I corrected it, quoting the Matlab line. Each claim on Experiments 2 to 6 now counts these trials (37 of 8721 cue trials overall) and shows its result without them. No outcome changes.
- **Day lists:** the notebook now reads the six Matlab scripts at the pinned commit, prints the lines that define the mouse and day lists, and checks the copies in `jeong.py`. All match, including the two scripts that reuse the initial-learning days.
- **fig4hi dopamine model comparison:**
  - Applying the code's bounds to dF/F in percent instead of as a fraction gives the same outcome (t = −7.74).
  - Dropping HJ-FP-M3 also keeps it (t = 0.99).
  - With no bounds at all, the changing model fits better in every animal (t = 7.83, p = 2.3e-4).

  The outcome therefore does not depend on the dF/F scale, but it does depend on the code's bounds. The criterion fixes those bounds, so the outcome stands; the notes and conclusion say this.
- **fig6i-lower-cs1-asymptote:** I added the per-animal variants the verifier asked for. All three are significant:

  | Variant | t | p |
  |---|---|---|
  | Normalised by the random-reward session | 2.84 | 0.016 |
  | Not normalised | 2.85 | 0.016 |
  | WT-M3's 25-trial last session replaced by its previous one | 2.43 | 0.033 |

  I kept not_reproduced because Supplementary Note 10 and the code both normalise by the first conditioning day's reward, as the criterion does. No passage excludes a short session. The notes say the outcome turns on these choices.
- **fig4jl:** reading (b) is now also run with the Methods' lick measure (t = 3.78, p = 0.0092).
- **fig4p:** two more variants: one without the trials with missing samples, and one using the sessions of `cumsum_pavlovian.m`. Neither meets the criterion.
- **Text-only fixes:**
  - The Experiment 7 session-count SDs look swapped in the paper.
  - The abruptness t values differ from the paper's for a reason I couldn't find; I re-checked the port against the Matlab scripts and found no difference. The notes name one candidate, HJ-FP-M4's missing Day30.
- **Record:** README table, notebook summary and header updated. The round is recorded under `verifications`, with the verifier's reasons and my responses.

**What I did not do**
- **Blocked reason for the seven simulation claims:** I kept `not_runnable`, not the verifier's `other`. The protocol lists `not_runnable` for software that can't run here (Author, step 1.5). The response records the disagreement. Octave is not installed here and can't come from the entry's Python lock file, and I did not attempt a Python port of the models.
- **Questions file:** I added nothing to `questions/000351.yaml`, because the verifier found no place where the claims file misreads the paper.
