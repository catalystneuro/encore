I worked through all eight problems in the round-1 report and the outputs it asked for. No outcome changed: the verifier agreed with all 15. The entry was re-run with `python tools/entry.py all entries/000138-churchland-2010`; the check reports 0 errors and the notebook runs in about 8 minutes. Round 1 is now recorded under `verifications`, with the verifier's reason and my response for each claim. Nothing is committed.

**Changed assumption (point 2, fig7c).** In the main reading, the neuron being fit is now left out of the upper-limit space. That follows the Supplemental Procedures passage the verifier quoted, which compares a neuron with the others. The rows that keep the neuron in are still shown but no longer count toward the outcome.
- **New result:** anterior is 0.817 and posterior 0.847 of the random-half value, so both are outside the 10% bound. None of the 8 counted rows meets the criterion, so the outcome stays not reproduced.
- **Direction flips:** anterior is now slightly below posterior (0.785 against 0.814), where the paper reports anterior slightly better.
- **Noise:** the random halves now have their spread printed (SD 0.190), and both arrays fall inside it. The 10% bound is therefore tighter than the sampling noise, which the notes now say.
- **Question for the paper's authors:** I updated it to say which choice I made.

**Draw counts (point 3).** The refit variants in fig7a and fig7c now use 20 draws, as the claims file sets. With 20 draws, the fig7a refit variant passes by a very small margin: the shuffled space's best is 0.159 against the kinematic space's 0.160. fig7a now fails only under the per-axis trial selection. The outcome stays reproduced.

**Outputs the verifier asked for:**
- **Refit curves for fig6:** with refit, fig6-each still meets its criterion, winning 21 of 22 comparisons. The fig6-trend notes now say its fall at high dimensionality may come from fitting 14 components to 27 conditions, and that the outcome rests on the fold reading.
- **Per-condition trial counts:** now printed for every trial-selection reading in the data check.
- **Overlap of draws in fig7d:** a draw holds a mean of 16.5 distinct conditions, and two draws share 10.1. This is added as a deviation.

**Text only (points 4 to 8):** I added notes that the 7–10 dimensionality result (11 here) sits at the edge of its range and is fragile. The fig4e criterion only uses times inside the movement-locked trace. The array mapping in the AP claim rests only on the difference in tuning. The README now gives the longer run time.

**Not done:**
- No questions file was created, because the verifier did not report a place where the claims file misreads the paper.
- What the verifier could not check (whether this is the paper's session, and which id prefix is which array) can't be settled from the files. It stays recorded as findings.
