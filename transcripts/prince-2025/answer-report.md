I answered the one open question, and it changed the claims file.

**fig2g-pfc-no-goal-increase (also affects fig5d-stay-hpc-like-delay and every decoding claim): changed.**
- **What was wrong:** the Methods exclude sessions with "less than 50 trials for the behavioral session". The paper's code instead counts the encoder training trials (`_meets_exclusion_criteria`). The protocol puts the Methods first when they and the code disagree, and shared method S1 didn't say which count it followed.
- **What changed:** S1 now counts the session's final-task trials. Warm-up trials are left out because the Methods say they "were not included in electrophysiological analyses". The code's count stays in S1 as a named variant.
- **What stayed the same:** no claim's statement, expected values or criterion changed. The claims file already records n = 47 sessions for the Fig. 2g Wilcoxon tests, which fits the Methods' count.
- **Answer:** I wrote this in the question's `answer`, citing both Methods passages, and set `answered: 2026-11-02`.

**Checks:**
- Both YAML files load.
- `python tools/claims_check.py` matches all 52 quotes word for word.
- It reports 5 problems, all "value not found" for small p-values (for example 3.41e-11 for fig1b-above-chance). They have nothing to do with this edit. They are probably printed in a form the checker doesn't recognise, or appear only in the supplement PDF, which I couldn't read here because no PDF tools are installed. They still need confirming by reading.

Nothing was committed or pushed.
