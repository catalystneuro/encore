I've finished the round-2 revision. No outcome changed. I propose one change, for ed5h-choice-shuffle-fpr, for a third round. The final `python tools/entry.py all entries/steinmetz-2019` passed (0 errors, 1,658 s), and every number in the text matches the new outputs.

**What changed in the outcomes**
- **ed5h:** the verified outcome stays `not_reproduced`, and `proposed` says `reproduced`. I ran four more shuffles of the choice labels under both versions of the fits. A single shuffle gives anywhere from 0.04% to 0.48%, a wider spread than the tolerance (0.16% to 0.50%). So the first shuffle's 0.14% came down to which shuffle was drawn. The mean over five shuffles is 0.22% under the main fits and 0.25% under the code's fits, both within tolerance. The proposal rests on treating that mean as the test's false-positive rate, which is stated as an assumption.
- All other outcomes are unchanged.

**What I added or corrected**
- **The kernel-model shortfall (2,886 neurons against about 4,240):** I read the paper's fitting code and the glmnet source. Four details of the code's fits were not followed:
  - glmnet is fitted once on all basis columns and then truncated;
  - the prediction has no intercept;
  - variance explained is taken from the variance of the residuals;
  - glmnet divides the ridge term by the response's spread.

  All four now run as a variant. It lets 3,199 neurons pass and leaves every kernel outcome as it was except ed5h. The rest of the gap is still unexplained.
- **Solver check:** a notebook cell now checks both solvers against scikit-learn's ElasticNet; they agree to within 3e-6.
- **fig3d:** the method text of fig3d, fig3e and ed4f now names one denominator, the neurons that enter the nested tests, which is what the code uses. The other set is a variant.
- **fig4d-vis-leads:** the seed table now prints the 0.08 s point on its own. It is significant in 3 of 5 seeds under each baseline. Some point from 0.08 to 0.12 s is significant in 5 of 5 seeds under baseline a and 3 of 5 under baseline b. The text and the record now say this.
- **fig5b:** neuron reading b now uses the claims file's set, every neuron of the 42 regions at 0.1 Hz or more. The outcome is unchanged. The verifier's point that a session count decides a claim about activation is now a question for a reader in `questions/steinmetz-2019.yaml`; the claim itself is unchanged.
- **Text fixes:**
  - The README now gives the measured runtime (about 28 minutes) and drops the unprinted "15 GB".
  - The fig3c time now matches the printed 160 s.
  - The ed4f notes now say the point estimates are ordered as in the paper under every reading, and only the significance fails under one reading.
- **The record:**
  - Round 2 is recorded for all 40 claims.
  - In round 1, the 11 kernel claims are corrected to `agrees: false`. The verifier named nine, but its round-1 reason questioned the block for all 11.
  - The problem-14 response moved from `reviewed` into the recording-counts response.

**What I did not do**
- **fig4c and ed5g** remain blocked. I did not write the decoding from the model's residuals. The protocol leaves a change that needs an analysis not yet run to a new attempt, and the record now says plainly that neither the data nor the time limit stopped it.
- **Untracked files in the repository root:** dotfiles (`.bashrc`, `.gitconfig`, `.idea`, and so on) and a `scripts` directory appeared there. I did not create them and left them alone.

Nothing is committed or pushed.
