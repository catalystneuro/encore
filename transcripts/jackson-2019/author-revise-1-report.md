I revised the attempt after the verifier's round-1 report. The entry re-runs cleanly: `python tools/entry.py all` reported 0 errors and the notebook passed in 123 s. Every conclusion in the notebook, README and attempt record matches the new outputs. Nothing is committed.

**Outcomes changed (3), all to the verifier's outcome**
- **offctrl-steepness:** partially reproduced → not reproduced. The criterion's reproduced and partially-reproduced outcomes both need the corrected average-reference test to hold, and it does not (FDR p = 0.0531).
- **table2-alpha-offctrl:** partially reproduced → not reproduced, for the same reason.
- **table1-alpha-pac-null:** reproduced (resting on an assumption) → not reproduced. The criterion takes the outcome all readings give, and the null holds under only two of the three phase-filter readings. I dropped the 192-tap assumption. The filter-length question to the paper's authors stays as a finding.

The record now has 8 reproduced, 9 partially reproduced, 7 not reproduced and 0 blocked. Round 1 is recorded under `verifications`: the verifier agreed on 21 claims and disagreed on the 3 above. Each claim has its reason and my response.

**Added or corrected**
- **fig2-pac-off-on:** the criterion contradicts itself on whether W counts. I added this as a question for a reader in the new file `questions/openneuro-ds002778.yaml`. I kept the outcome and did not change the claim.
- **Correction-procedure sensitivity for both Table 2 steepness tests:** Holm, Bonferroni and Benjamini-Yekutieli over six give 0.086 to 0.130, and Benjamini-Hochberg over the three beta tests gives 0.053. Only Benjamini-Hochberg over the three alpha tests falls below 0.05 (0.043), and that is not the family the criterion names.
- **CSD variants (spline flexibility 4; lambda 1e-4 and 1e-6):** none brings off against controls below 0.05 (p = 0.11 to 0.30). I also added C3/C4 band-power ratios before and after CSD.
- **PAC with filter edges dropped (as pacpy does):** PAC changes by at most 5% per recording and W is unchanged.
- **Variants without sub-pd6 and sub-pd16** for PAC, the correlations, the Q4 counts, Table 3 and the off-against-controls tests:
  - The steepness–PAC correlation then falls within tolerance both off and on medication. This is reported as a variant; the outcome is unchanged.
  - The Q4 counts become 9, 9, 6 and 12.
- **Q4 detail:** per-patient peak-to-trough and rise-to-fall ratios at C3 and C4. 16 of 60 points lie within 0.01 of an axis, which can move patients in or out of Q4. The table3 conclusion now says its Q4 subset is 13 patients against the paper's 9, and lists them.
- **UPDRS note:** corrected "0 to 14" to "1 to 14", and noted that the dataset holds no other part of the UPDRS.

**Not done**
- I did not compare MNE's CSD output with the MATLAB CSD toolbox, because that needs MATLAB. The record says this.
- The paper's artifact marks and the pd6/pd16 preprocessing cannot be recovered from the dataset, so the verifier's problem 8 needs no change.
