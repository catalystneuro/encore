I checked the claims file for DANDI:000945 and corrected eight things. The file is ready for an attempt.

**Checker:** `claims/000945/10.1088-1741-2552-adbb1f.yaml: 22 claims, 22 quotes, 15 statistical values, 0 problems`. I got the same line before and after my edits.

**Changes, by claim:**
- **Header:**
  - The paper doesn't say whether responses are measured from spike times or from histogram bins. This matters because the 67 ms, 0.2 s and 0.7 s window edges don't line up with the 35.7 ms bins. I named both as readings to run.
  - It also doesn't give the Bonferroni family size, or say whether the off-target sham was also recorded under anesthesia. If the dataset has no anesthetized sham, the parts that compare with it are reported as untestable.
- **fig5a-rsu-time-locked-prf-awake:** The criterion only reported 30 Hz against 300 Hz without letting it decide. The paper says 30 Hz is lower than "all higher PRFs", and that the only difference under anesthesia is that 30 and 300 Hz don't differ. So the awake difference is part of the finding; I added it to the criterion and the statement.
- **fig5c-rsu-time-locked-prf-anesth:** Reworded its part (2) to match: 30 Hz must be below 1500, 3000 and 4500 Hz only.
- **fig6ad-time-adjacent-batch:** "Reduced under anesthesia" was judged at 1500 Hz only, which the paper doesn't say. It is now judged at each of the two frequencies, or with both pooled.
- **fig7a-rsu-time-locked-dc:** The Figure 7A legend says 6% duty cycle is significantly lower than 30%. That was only reported; it now counts toward the outcome and is in the statement.
- **fig7c-rsu-delayed-dc:** The Figure 7C legend says all three duty cycles differ, so 6% against 60% now counts too. Statement updated.
- **sham-no-auditory-response:** The paper gives no test for this. The criterion now says outright that the claim is blocked for lack of a method in the paper.

**Still open (recorded in `checks`):**
- **fig5bd-fsu-time-locked-no-prf and fig7b-fsu-time-locked-dc:** These "no difference" claims are judged on a test across the parameter levels alone. The paper's test may also have included the sham group, and it doesn't say which. The version with sham is shown alongside.
- **Two-way ANOVA claims:** The paper doesn't say which delayed-response window went into the ANOVA. The file uses each state's own window, as in Figure 5.
- **fig4-rsu-time-locked-both-states:** Figure 4 only shows examples, so this claim borrows the comparison with sham that the paper runs elsewhere (Results 3.2).

Every main finding has a claim, and nothing comes from outside this paper. Nothing was committed or pushed.
