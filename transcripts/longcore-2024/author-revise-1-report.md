I've handled every point in the verifier's report. One outcome changed. The entry re-ran cleanly with `python tools/entry.py all entries/longcore-2024`: 0 errors, the notebook passes, and the numbers are unchanged.

**Outcome changed**
- `cct-effect-grows-with-intensity` goes from partially_reproduced to not_reproduced, as the verifier gave it. The criterion requires the spread across colour temperatures to be smallest at 0.01 lx. It is 9.28 there and 5.64 at 0.5 lx, so that fails, and the criterion has no partial outcome. The notebook now says the GLM-predicted spreads carry little weight, because a model with a linear interaction makes them grow almost by construction.

The other 12 outcomes are unchanged, and the verifier agreed with each of them.

**Added or corrected**
- **Log-link fits (point 4):** a new cell prints, for each log-link fit, the fitted means, parameters, standard errors and how well-determined the fit is. With illuminance in lux, the parameters are not determined (standard errors up to 43), so the conclusion now says those Wald tests and intervals are not usable. The AICc cell no longer prints "All fits converged". It says the optimizer reported success and that this does not mean the log-link parameters are determined.
- **Models with sex or mouse identity (section C):** a new cell runs the same effect tests with sex or mouse identity added. With mouse identity (identity link, lux), every one of the paper's bounds is met, including the interaction at p 0.0007. With sex added, the interaction p is 0.0038. The criterion names the model without either, so `glm-illuminance-cct-interaction` stays partially reproduced; the notes and a reader question record the difference.
- **Treatment means (points 5 and 6, section C):** the notebook prints the abstract's four treatment means next to the computed ones (all match). It adds one-sample t-tests at the named treatments. The conclusions now give the mouse counts (14 or 15 at the low illuminances where the criterion says 16). They also say the two Table 1 outcomes rest on the sign of means that cannot be told from zero: three of eight for the suppression claim, and all four for the increase claim (p 0.055 to 0.67).
- **Smaller text changes:**
  - The sex conclusion gives the Mann-Whitney p of 0.083 on per-mouse means (point 7).
  - The cFos conclusion explains that the claims file's 8.22 tolerance and its "t near 1.28" remark rest on reading an s.e.m. as an s.d. (point 1). The outcome does not change.
  - The link finding and the summary cite the abstract's "multiple linear regression" (point 2).
- **Reader questions:** the new `questions/longcore-2024.yaml` holds four questions:
  - the cFos 8.22 value;
  - whether the claims file should treat the identity link as the paper's model;
  - whether the paper's GLM p-values come from the model with mouse identity;
  - whether the CCT-spread criterion should use the GLM's spreads.

  No claim in the claims file was changed.
- **Record:** `attempts/longcore-2024-01.yaml` has the round-1 `verifications`, with the verifier's reasons and my response for each claim. The notes match the new outputs, and the README and the notebook summary show the changed outcome. No finding is rated `critical`, so there are no finding reviews to record.

**Not done**
- **AICc offset of about 4 points:** I could not find its source. The paper's 192 rows cannot be rerun because nine values are not in the dataset, and JMP's parameter count is not stated. Both counts are already shown, and the text now says the question is open.
- **Why nine values are missing and whether JMP centres the crossed term:** the data cannot answer the first, and the second does not affect any outcome.

Nothing is committed. `git status` also lists untracked dotfiles and `scripts/`, `.idea` and `.vscode` at the repository root that I did not create; I left them alone.
