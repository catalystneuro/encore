**Round 2 verification: Starkweather et al. (2018), CRCNS vta-1, attempt starkweather-2018-01**

**1. Outcomes**

The claims file has 32 claims. The attempt record gives 32 outcomes: 20 reproduced and 12 blocked (`data_missing`). I agree with all 32.

- **Blocked (12).** Cell 3 now prints the zip's contents: 173 members, which are the 172 neuron `.mat` files and `data/`. Every file holds only `odor_onsets`, `reward_onsets`, `spiketimes` and `trial_type`. Cell 84 shows 0 reward onsets outside odor A to C rewarded trials. So there are no mPFC units, licks, free-water deliveries, unidentified VTA neurons or no-KORD neurons. The partial ANOVAs in cell 87 are correctly labelled as deviations that decide no outcome.
- **Reproduced (20).** Each meets its criterion on the printed numbers (cells 15 to 82).
- **`assumed: true` (2 outcomes).**
  - `fig5e-task1-significant-slopes-unchanged` and `fig5f-task2-significant-slopes-shift` both rest on trial-by-trial baseline subtraction.
  - The assumption is stated in the deviations, the conclusions (cells 45, 48), the Summary and the README, and is put to the authors as a finding.
  - It is reasonable. Only this reading recovers 29/12/24 and 16/0/16/2, and it gives Fisher p = 0.487 and 0.0405 against the paper's 0.49 and 0.041 (cells 41, 44, 47).
  - Under the mean or no-baseline reading, fig5f fails (p = 0.239, saline has 3 significant negative slopes) and fig5e's SalB count of 18 is outside tolerance.
  - No other outcome depends on a reading: cells 41, 50, 53, 56 and 60 hold under every reading.
- **`fig7ijk-model-timing-impaired` and the claims file.** The claims file is weaker than the paper here. I am reporting this, not correcting it.
  - The paper says omission responses "were abolished (Figure 7K)". The Figure 7 legend says the timing-impaired model, unlike the intact one, does not "display reward omission responses at the time of expected reward".
  - The criterion only asks that the dip is not deeper than the intact run's minimum.
  - Cell 81 shows a remaining dip that is clearly below zero: odor B −0.073 (p = 6.6e-06) and odor C −0.032 (p = 0.045) under reading (a), 25 to 43% of the intact dips.
  - So "reproduced" is correct for the criterion as written. Judged against the paper's own words, this part does not reproduce. The record states this and refers it to a reader.

**2. Sentences against printed outputs**

Almost every number checked matches. These do not, or are looser than the outputs support:

- **Cell 82, and the fig7ijk notes:** "Reading (b), 0.56 for all, gives the same." Under (b), 49 of 50 task 2 slopes are positive (frac_pos_t2 0.98, cell 81), not 50 of 50, and the task 1 slope is −0.015, not positive. The criterion still holds, so only the wording is off.
- **Cell 89, Summary:** "most F and p values to two digits." This holds for F. For p, about half differ in the second digit: 8.4e-16 vs 9.1e-16 (cell 15), 2.5e-5 vs 2.7e-5 (cell 21), 1.4e-17 vs 2.7e-17 (cell 34), 0.032 vs 0.038 (cell 50), 0.027 vs 0.02 (cell 63), 0.81 vs 0.76 (cell 63), and 3.9e-7, 6.8e-4 and 8.7e-4 vs 3.8e-7, 7.0e-4 and 9.0e-4 (cell 66).
- **Attempt record, `fig5f-task2-significant-slopes-shift` notes:** "the only one that recovers the paper's printed counts and Fisher p values." In this same claim the data give 8 significant negative SalB slopes against the printed 9 (cell 47). Cell 48 limits the statement to the listed counts; the notes do not.
- **Cell 48 and the same notes:** "That reading follows the Methods' wording." The Methods say only that responses "were baseline-subtracted, with baseline taken 0-1 s prior to odor onset", which fits either reading. The record's own `methods_unavailable` finding says so. I used the same phrase in round 1 and withdraw it. The match to the printed counts is the actual reason.
- **README:** "It takes about five minutes." Cell 90 prints 189 s. "7.9 MB zip" is not printed anywhere in the notebook.

**Round-1 reasons in the attempt record**

The verification block restates my reasons faithfully and in my wording: A table, B1 to B6, C1, C2 and the C4 subject-ID point. Three points are not in any reason:

- B7: the 40-minute reading uses the session's first spike as recording onset.
- C3: the untyped trials. This appears only in the author's response under fig4a.
- The `_count`, `auroc`, `isi_anova` and `slopes` checks on synthetic inputs, which are summarised only in `reviewed`.

None of these bears on an outcome.

**3. Round-1 points**

Resolved:
- **B1:** the dip depth is now quantified with a t-test, and the conclusion, notes, Summary and README say "reduced, not removed".
- **B2:** reported.
- **B3:** the conclusion, notes and `assumed: true` state the reading.
- **B4:** unchanged; it was already handled.
- **B5:** the partial ANOVAs are run in cells 87 and 88.
- **B6 and C1:** the zip's member list is printed.
- **C3:** cell 11 and the `file-untyped-kept` slope variant show no change.
- **B7:** unchanged, but both readings give the same outcomes.
- **C4:** cannot be resolved, as the data have no subject IDs.

Remaining points that bear on a conclusion:
- **`fig7ijk-model-timing-impaired`:** the criterion does not test the paper's "abolished" or the legend's "does not [display]", and the model leaves a significant dip. The reader's answer could change this outcome.
- **C2, the Python port not checked against a MATLAB run.** The author says MATLAB and Octave are unavailable. `blur_matrix`, `blur_vector` and the tonic and phasic indexing in `simulate` are still not checked line by line. This matters most for fig7ijk, because the size of the remaining dip depends on the blurred transition matrix. It is lower risk for fig7cd and fig7fgh, which hold in 5 of 5 seeds.
- **The two `assumed` outcomes:** fig5f-task2-significant-slopes-shift reverses under the other baseline readings, so it stays open until the authors answer the baseline question.
