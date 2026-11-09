No outcome changed and nothing is proposed. The verifier agreed with all 24 outcomes (9 reproduced, 9 partially reproduced, 6 not reproduced), and I found no reason to propose a change. I re-ran the entry with `python tools/entry.py all`: no errors, the notebook passes in 133 s, and every number is the same as before. `entry.py check` also passes. Nothing is committed.

**Added to the notebook**
- **New sensitivity section before the Summary.** It runs all six off-against-on tests of Table 1, under every filter reading, and the three bipolar tests, each without sub-pd6 and sub-pd16, uncorrected and after FDR correction.
  - Every test keeps its direction.
  - The tests that were significant under every reading stay significant: corrected p 0.017 to 0.033 for Table 1 and 0.011 to 0.019 for the bipolar tests.
  - Alpha PAC is not significant under any reading without the two patients (0.064 to 0.087). With all patients it was significant under one reading (0.036).
- **Topography cell (fig2c):** it now prints electrodes tied for the smallest p. With the code's filters, Fz and CP6 tie at 0.020.
- **CSD variant table:** it now shows the mean on and how many patients are higher off. Every variant is higher off, in 12 or 13 of 15 patients.
- **Q4 cell:** it now works out which near-axis points decide whether a patient counts. There are 10, in pd3, pd5, pd11, pd12, pd22, pd26 and pd28. pd9 is no longer listed, and pd5 and pd11 are added.

**Text corrected**
- **Summary, about the dataset:** it no longer says the statistics are "close to the paper's". It now says each of the three main tests holds but has one value out of tolerance, and names the three values.
- **"Each recording once"** is replaced by: patients recorded off and on, controls once, no recording deposited twice.
- **Summary, Sensitivity paragraph:** it now matches the new outputs. It says the edge-dropping variant was run only for the beta test at C3 and C4.
- **Smaller corrections:**
  - "5%" is now 5.1%.
  - The CSD direction sentence now cites the new numbers.
  - The table3 summary row names the third out-of-tolerance value (raw all-patient PAC d 0.85).
- **Attempt record:** the notes for fig2-pac, fig2c, offctrl-pac-csd, q4-patient-counts, table1-alpha-pac-null and pac-beta-larger-than-alpha were updated to match.

**Recorded**
- Round 2 is under `verifications` in the attempt record, with all 24 claims marked as agreed, the verifier's reasons from the report, and a response for each.
- `questions/openneuro-ds002778.yaml` has a new question for a reader: the criterion for pac-beta-larger-than-alpha has no clause for a partial outcome. The earlier fig2-pac-off-on question is still open.

**Not done**
- **CSD toolbox comparison (offctrl-pac-csd):** not run, because the toolbox needs MATLAB and the locked environment does not have it. The record says so.
- **Artifact rejection:** not possible, because the paper's artifact marks and excluded electrodes are not in the dataset. This is already recorded as a finding.
