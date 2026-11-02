I've worked through all 11 points in the verifier's report, re-run the entry, and recorded the round. The run passes (`tools/entry.py all` ran in about 11 minutes, checks show 0 errors), and the handover now removes every conclusion cell. Nothing is committed.

**Outcomes changed**
- **fig4bc-no-laterality** goes from reproduced (resting on an assumption) to **blocked, `methods_underspecified`**, as the verifier gave. Whether the laterality effect is significant depends on which trials are used, and the paper doesn't say. On cleaned trials p is 0.0003 to 0.010 across every session set and preprocessing; on all trials p is 0.14 to 0.82.
- **fig2c-complex-rl-beat-rl4p** stays reproduced, now marked as resting on an assumption, and the verifier's disagreement (it gave partially reproduced) is recorded. The two forgetting rules for RLFQ3p give different outcomes. I adopted the code's rule because Table 1 and the linked code use it, and it gives the paper's own value (−645.17 against −646.45). The Methods' rule gives −460.66, outside tolerance, and is shown. The claims file's choice of the Methods' rule as the main one is now a question for a reader in the new `questions/001340.yaml`.

Every other outcome is unchanged; 37 of 39 already agreed with the verifier.

**Added or corrected**
- **Session selection (points 1–2):**
  - The selection statistic splits cleanly: sessions without a dopamine response have |t| ≤ 2.89 and all others have t ≥ 7.01, so any threshold between them keeps the same 38 sessions.
  - The notebook now says the reward/omission signs are not an independent test in that set. The 46-session set, which isn't selected on the outcome, gives the same signs.
  - A new section re-runs the main dopamine results on three more sets: the 34 sessions with the strongest response (the paper's count), all 46 usable sessions, and the 38 with the alternative (Lasso) photometry preprocessing. Every outcome holds on the 34-session and Lasso sets. On all 46 sessions two results weaken: the fig4i R_unchosen:Switch interval includes 0, and only 3 animals show the figs5 pattern. These are recorded in the notes.
  - The claims file's AUC reading (near 0.5 by construction) is asked of a reader.
- **Bootstrap (point 4):** I added per-animal Δllk with a t-test across the 5 animals, and a bootstrap that resamples sessions. For fig4f the Bayesian models still come out ahead (BRLfwr above zero in every animal, p = 0.0004). For figs8 dopamine the session bootstrap still excludes 0, but the across-animal test gives p = 0.065.
- **Multi-start fits (point 5):** every model was refitted from 10 starts. The figs8 behaviour result holds (p = 0.045, still close to 0.05), and parameter recovery for BRLfwr and RL_meta is unchanged.
- **Points 7–10:** the Methods' RLFQ3p rule is now in the Holm families and the no-difference tests (non-significant, mean −69.4). The Methods' version of the BIfp RPE is shown for fig4h and fig4-consistent; neither outcome moves. The Lasso variant now covers the dopamine regressions. Five conclusion cells that started "**Result (" were renamed so the handover strips them.
- **Number corrections:** some numbers in the record and conclusions came from an earlier run and differed slightly (for example PearceHall −678.01 to −678.05, fig3c −166.20 to −166.33, fig2b confusion rates). Every conclusion and note now matches the current outputs; the last two runs gave identical outputs. I also fixed a parameter labelled "q" that should be "sw".

**Not done**
- **lme4 was not run.** R isn't installed in this environment, so the mixed models still use statsmodels' MixedLM; the notes say so.
- **The outcome-independent session criterion didn't work.** The paper's "longer tail" rule turned out to be dominated by artefacts, so I used the 46-session set as the independent check instead.

`attempts/001340-qu-2025-01.yaml` also shows reformatting in its diff, because the whole file was rewritten. I matched the original line width, so most unchanged text is identical.
