**Verifier report, round 2: Padilla-Coreano et al. 2022 on DANDI:001749 (0.260311.1727)**

The claims file has 46 claims, and the attempt record gives an outcome for all 46: 5 reproduced, 1 partially reproduced, 3 not reproduced, 23 blocked as metadata_insufficient and 14 blocked as data_missing. Two outcomes are marked `assumed: true`: fig1i and ed5d. The cell 0 table now counts 46 claims (9 tested, 37 blocked).

### 1. Outcomes

| Claim | Agree? | Comment |
|---|---|---|
| ed5b, ed5e, ed5f, ed5g reproduced | Yes | Unchanged since round 1 (cells 31, 40, 43, 46). Sessions are now the main reading for ed5e. |
| ed5c partially reproduced | Yes | Cell 34: p = 0.498 over sessions. Cell 6 shows that no subject record has a weight field. |
| ed5d not reproduced (assumed) | Yes, with a caveat | The criterion as written is met by the main reading (p = 0.0196) and by the best-shift reading (p = 0.0458). The record says the outcome departs from it on purpose, and the departure is stated and defensible. The latency from the hand-scored labels needs no alignment and fails (p = 0.16 and 0.206). Dropping the files that cannot be aligned gives p = 0.158 and 0.375. The caveat is that the r ≥ 0.3 cut-off is arbitrary and was never varied (cell 37). |
| fig1i reproduced (assumed) | Yes | Cell 53: under the main reading every test passes. Of the other readings, crossings in either direction, no shift, and random folds with the shift all pass. Z-scored rates fail. The assumption (counts and contiguous folds) is stated and reasonable: the paper's input holds counts and run_model.m forms contiguous folds. One part of it is asserted but not shown: that the z-scored failure comes from the 1e-6 learning rate. Z-scored rates give 0 of 9 AUCs above 0.5, which is systematically *below* chance, not at chance. I ran the ported `hmmglm.py` on two kinds of synthetic counts carrying no information about the labels: pure noise, and a shared tone-locked rate with labels that depend on time in the trial. In both, the HMM-GLM AUCs were about 0.50, so the one-step predictor does not leak the true label. |
| ed5j not reproduced | Agree, by the criterion | Cell 57: both readings select 2 states. But the paper's input was run only at 1, 6 and 10 states, so we cannot tell whether the port itself would select 2 on the paper's data. If it would, the failure comes from the method, not the dandiset (see 3). |
| ed5k not reproduced | Agree, by the criterion | Cell 60: training on subordinates and testing on dominants gives 7 of 9 above 0.5 (p = 0.18). This should be marked assumed, or run under the other readings. It inherits fig1i's choice of reading but was run only on the main reading, where AUCs are lowest. Crossings in either direction raised fig1i's median from 0.774 to 0.910. The subordinate group has only 4 mice. |
| 37 blocked claims | Yes | Cell 6 now shows the file tree, the subject fields, the units columns and the "unsorted" quality labels. |

### 2. Sentences the outputs do not support

- **Attempt record, ed5j notes:** "On the paper's input, run for 1, 6 and 10 states only, the values are **-529.6**, -126.5 and -127.6." Cell 57 prints **-498.757** for 1 state.
- **Summary (cell 62):** "on it the port reproduces Figure 1i and **ED Fig. 5k**." Cell 60 runs only the two cross-group directions on the paper's input. ED Fig. 5k's criterion also requires the within-group 10-fold runs, which were not run on that input.
- **Attempt record, fig1i `measured: [965, 34, 14]`:** these are the counts of all labelled files. The test ran on 512 trials, 17 files and 10 mice (cell 53), which is outside every tolerance (965 ± 96, 32 ± 3, 13 ± 1). The deviations do state this, but the measured values misstate what was compared against the expected counts.
- **Attempt record, ed8ij, fig2e and ed9b:** "every one of the 53 subject descriptions says the mouse is in competition with a cagemate." Cell 6 prints one example description, not all 53.
- **Cell 25** is a data-check cell, outside the cells I was asked to check: "two in only 64% and 75%". Cell 24 prints 0.675 and 0.756. The record's finding (68% and 76%) is correct.

I checked every other number in the "**Result:**" cells (32, 35, 38, 41, 44, 47, 55, 58, 61), the Summary, the README and the record's notes against the outputs, and they match.

The record restates my round-1 reasons accurately, mostly close to my wording. The `reviewed` summary is also accurate. The only omission is harmless: for fig4a and the other ex vivo, phototagging and optogenetics claims, it leaves out my remark about the API's measured-variable list.

### 3. Round-1 points

**Resolved:**
- **1 (HMM-GLM):** now attempted.
- **2 (videos):** the response is correct. The LED places the tone in the video, which is already on the behaviour clock, so it cannot give the offset to the logger. My point was mistaken.
- **3 (ed5d):** the requested analyses were run and the outcome changed.
- **4 and 5:** cell 6 now shows the subject records and the file contents.
- **6:** sessions are now the main reading.
- **7:** answered; the block stands.
- **8:** the empty ed5f variant was removed and the switch variant is explained.
- **9 and 10:** stated as deviations.
- **11:** the claim count is fixed.
- **Section C requests:** the units columns were shown.

**Remaining, bearing on a conclusion:**
- **ed5j:** run the paper's input at 1 to 10 states. That would show whether selecting 2 states reflects the dandiset input or the port's likelihood. Also correct the -529.6 in the record.
- **ed5k:** either mark it assumed, or run it under the fig1i readings that passed, especially crossings in either direction.
- **fig1i:** two things are needed:
  - a z-scored run with an adjusted learning rate, or a z-scored run on the paper's input, to back the learning-rate explanation for the below-chance result;
  - a re-run without 20191029-chrimson2-2-2v3. Cell 51 says its 30 trials are probably misaligned by about 8 s, yet it was kept.

  Neither is likely to change the outcome.
- **fig1i record:** make the `measured` values the analysed set (512, 17, 10).
- **ed5d:** show the result at a cut-off other than r ≥ 0.3 (for example 0.2), so the sensitivity to the cut-off is visible.
- **Summary:** change "reproduces … ED Fig. 5k" to say that only the cross-group directions were run on the paper's input.
