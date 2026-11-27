No outcome changed in this round. One change is proposed for round 3: fig2a-rabbit-monotonic stays partially_reproduced as verified, and not_reproduced is written under `proposed`. The entry re-runs cleanly (`python tools/entry.py all entries/wang-2019`: 0 errors, notebook passes in 11 s), and the attempt record validates against the schema. Nothing is committed.

**Changes in reply to the report**
- **fig2a:** The reason given for the partial outcome was false: under reading (ii), APD80 at 60 s is not significant (Holm-Sidak p = 0.18). I removed that sentence from cell 25 and the notes and fixed the doubled "APD80". The notes now say what does hold: at 60 s all three variables change in the stated direction under reading (i), and APD80 falls monotonically. The proposal for not_reproduced gives three reasons:
  - the criterion has no rule for a partial result;
  - the stated basis for partial was wrong;
  - heart rate falls significantly from 50 to 60 s (p = 0.047).
- **fig3d:**
  - I dropped the APD80 25 s pooled result, because its ANOVA is not significant. The notebook now counts pooled-error comparisons only after a significant ANOVA.
  - It now prints heart rate per heart at 0 and 60 s: it rises in 2 of 3 hearts (+32 and +20 bpm, −2 in the third).
  - The text now says the outcome rests on the one unadjusted test (APD80 at 10 s, p = 0.010).
  - The outcome is still not_reproduced.
- **Sphericity check:** I added a Greenhouse-Geisser correction to the repeated measures ANOVA in `sns.py`, checked against the textbook formula. It is printed but decides no outcome. With it:
  - the fig3d heart-rate ANOVA is no longer significant (p = 0.23);
  - the fig2a APD80 ANOVA is not significant either (p = 0.066).
- **Simulation claims (fig8e, fig8f, fig8ij, fig9):** The verifier was right. Octave 10.3.0 installs from conda-forge without root (I tried it). The stated reason is now that the entry's environment is a Python virtual environment built from a pip lock file, which cannot hold Octave.
  - I also ran the mouse model under Octave outside the notebook. It runs after a one-line change to its `ode15s` call, but far slower than real time, so its 70 s simulations would likely not fit the notebook limit.
  - That run only informs the notes and does not decide the outcome. The claims stay blocked as not_runnable.
- **fig3abc:** The outcome now rests on the criterion's own "HR rising" (noradrenaline heart rate stays above time 0 throughout). The notes no longer cite a general "any reading" rule that is not in the criterion.
- **Smaller fixes:**
  - cell 29 now gives the SD as 4.94 ms;
  - the cell 13 range sentence now says one rabbit heart (−6.6 ms) lies outside the base and apex range;
  - the README fig1bc row now says rabbit APD80 holds only on the majority reading;
  - "SigmaPlot's" pooled-error test is now described as a variant, since the paper names no software;
  - the question to the authors in the record now also asks about sphericity.
- **Record:** Round 2 is under `verifications`. Two gaps in the round-1 reasons are restored: the B6 example (rabbit APD80 at 60 s, p = 0.021 against Holm-Sidak 0.18) and "blocked: other" for the simulation claims.

**Not done**
- fig3f is unchanged, because the verifier agreed with the outcome on reading (a).
- I added no new question to `questions/wang-2019.yaml`. The only misreading the verifier reported, the simulation claims' "data elsewhere", is already there.
