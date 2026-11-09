No outcome changed. The verifier agreed with all 61 in round 2, and nothing I found calls for a change, so nothing is under `proposed` and no third round is needed. I re-ran the entry twice with `tools/entry.py all`; all five notebooks passed and `check` reports 0 errors. I checked the conclusions against the new outputs and they match.

**One point where the verifier was wrong about this run (fig2i).** The verifier said the factor 3 main model printed `converged True`. In both of my runs it prints `converged False`, and every post-hoc fit converges. The coefficients and p values are identical across runs, so only the convergence flag changes between runs. 03 c18 and the record's notes now say that, and I did not adopt the verifier's version.

**Corrected or added:**
- **link-ieeg-yeo-labels:** the text and notes now say the Fig. 2H and 2J matrices are reproduced exactly (maximum difference 0.0), not "to 6e-17".
- **figs13:** the variant sentence moved from the fig3b method text into the figs13 Result in 03 c22.
- **figs38a:** 04 c33 now says the outcome rests on the legend's per-band reading, which the criterion sets. The summary row now says at least one band differs in 40 of 44 readings, and theta and alpha both in 38.
- **figs38b:** the notes now say Bonferroni does not give the same pattern: beta 0.0797 in the main reading, and in the passing code-band reading beta 0.1991 and gamma 0.1989. The verifier quoted 0.1983 for gamma; 0.1989 is what this run prints.
- **fig4b and the dataset finding:** 02 c13 now prints the converter's commented `extra` list next to the 001326 sessions, which shows sub-5's sessions on 2023-07-06 and 2023-08-22. The list has four entries, including 20220223_m95_544; the finding named only three and now names all four.
- **figs15:** 03 c29 now prints the mean ± s.e.m. over participants, which is the statistic the fig. S15H legend gives. Under the mean MCC is still first (2.644), then IFG (2.367) and ORB (2.262), so ORB is third either way. The conclusion and notes say this. I added the median-versus-mean misreading to `questions/001347.yaml` as a question for a reader and did not change the claim.
- **Run times:** the README now says about 40 minutes in all, which matches both runs. The 04 data check now says 8 to 12 minutes, citing 466 s and 690 s; the second run took 697 s, slightly outside the times quoted but within the stated range.
- **Round 2 record:** added under `verifications` in the attempt record, with all 61 claims marked as agreeing, the verifier's reasons as closely quoted as I could, and my responses.

**Not done:**
- **Open questions:** fig5e (which window), figs2bc (the expected 0.34) and fig4b (the normalisation) are waiting on a reader or the authors. The questions for fig5e and figs2bc were already in the questions file; fig4b's is recorded in the verifications.
- **figs27:** the verifier's point is that the criterion has no control without ketamine. The conclusion and notes already say this, and I left the criterion alone because it is not mine to change.
- **The 716 edges:** the paper's edge selection for figs38a and figs38b still cannot be reproduced.
- **Files I did not touch:** `tools/runner/chain.sh` was already modified before I started, and the untracked dotfiles in the repo root (`.bashrc`, `.idea`, `scripts` and others) are not mine.

Nothing is committed or pushed.
