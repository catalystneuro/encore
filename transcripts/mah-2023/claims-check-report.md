I checked `claims/mah-2023.yaml` and corrected it. It is ready for an attempt.

**Checker result:** `claims/mah-2023.yaml: 32 claims, 32 quotes, 28 statistical values, 0 problems`. It was 30 claims before I added two.

I compared the criteria against the paper's code at the cited commit (b7b68ca8c107). Most of what the file says about the code is accurate. These are the changes, by claim:

- **Header, session inclusion:** the file said a session needs a positive slope; the Methods say a significantly positive one. The Methods' rule now comes first. The code's looser rule is kept as a variant, and the catch-trial count is corrected to "more than 5", which is what the code tests.
- **suppfig2:** I noted that the printed all-trials p is about half the two-tailed Fig. 1i p, which fits the code's one-tailed tests. Both readings stay.
- **suppfig3, fig2c-d:** the pass rules are now marked as readings, since the paper gives no test.
- **fig2e:** I added a code variant. For wait times the code fits the decay curve to the current offer plus 9 previous ones, where the Methods use the 9 previous only. For initiation times the code sets tau to 0 based on the coefficients 2 to 10 trials back.
- **fig2g-h:** "N = 80" in the code is a percentile, not a rat count; now said so.
- **fig3l:** the file treated the code's "N = 60" as a rat count, but it is a percentile. The legend's N = 116 fits both group splits (20/80 and 40/60), not only one. The vague "at least one parameter" is replaced by two readings: the right asymptote (legend) or the slope (Results).
- **fig3i:** the alternative models were set to run only at learning rates below 0.1, but Supplementary Fig. 7 runs them at 0.05, 0.4 and 0.8 with 20-trial smoothing; that is now used. The code's noise settings (8 and 1.5) are named as a variant of the Methods' 4. The statement's dependence on previous rewards (Fig. 3i) had no test; I added one.
- **New claim `fig3f-inferential-model-not-sensitive-to-previous-offer`:** Fig. 3f, a model finding the file did not cover.
- **New claim `suppfig14-contextual-effects-without-threshold`:** the robustness finding of Supplementary Fig. 14, parallel to the existing satiety claim (Supplementary Fig. 6).

**Still open** (recorded under `checks`):
- The repository lacks the model-fitting code, so the free parameters, bounds and folds for the model claims (fig3j, suppfig8, suppfig9, fig3l, fig3f) are not fixed. The paper's fits on Zenodo count as outside data.
- The paper gives two sex splits (184/107 and 160/114). The Results give N = 180 for Fig. 3l, which matches neither group split.
- Fig. 3d,e show the model with hand-picked parameters and one example rat, so they get no claim.

I committed nothing; only the claims file changed.
