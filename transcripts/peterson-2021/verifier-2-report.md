**Verifier report, round 2: Peterson et al. 2021 on DANDI:000055 (0.261123.1703)**

The claims file has 25 claims and the attempt record has 25 outcomes: 15 reproduced, 7 partially reproduced, 2 not reproduced and 1 blocked. My round-1 report gave 14 reproduced and 9 partially reproduced. That was my counting error: my own round-1 table lists 15 and 8.

### 1. Outcomes

I agree with 24 of the 25 outcomes. Every assumption marked `assumed: true` is stated. All but one are reasonable.

- **fig5-recording-day-effects (not_reproduced, assumed): I do not agree that the outcome is settled.**
  - The outcome changed from round 1 only because the main analysis now uses the electrodes marked good in every file of a subject.
  - The claims header's phrase "renormalised to sum to 1 per subject" says the weights are made per subject. It does not say which electrodes count as bad.
  - The notebook's own counts (cell 4) argue against the chosen set. Excluding every electrode that is bad in any file removes 3 to 32 per subject, mean about 17.3. The paper reports 4.9 ± 4.9 surface electrodes removed per subject.
  - Removing only the electrodes bad in every file gives a mean of 3.0 (SD about 4.6), much closer to the paper. That set is also per subject and keeps the electrode mix the same across days.
  - That third set was not run. The result is 18/24 under the chosen set and 20/24 (exactly the threshold) under each file's flags, so the outcome flips on an open choice. I would report it as undecided between partially and not reproduced until that set is run.
- **table1 and fig4:** the same choice moves table1 from 21/24 to 18/24, which is exactly the partial threshold, and fig4 from 3 to 2 parts. Both outcomes stay partially reproduced either way, so I agree with them.
- **fig4 part 4 now fails:** S07 and S09 have 2 bins, and six subjects, S04 and S08 among them, tie at 3 (cell 56). Only one place among the three fewest is left, so S04 and S08 cannot both be in it. Counting this as a fail is reasonable.
- **fig2-reach-shape:** the new density table (cell 30) supports the author. Pooled, only 6.4% of events lie within 15° of −90, which is below the 8.3% a uniform spread would give. The −90 side fails for a reason other than the kernel's boundary effect, so partially reproduced stands.
- **The other assumed outcomes** (segment-rejection pooling, regression electrode set, the R² > 0.03 refit rule for the variants) are stated and reasonable.

### 2. Sentences the numbers do not support

- **Cell 99 (Summary), fig2-reach-shape row:** "no angle density peaks within 15 degrees of +-90". Cell 30 shows a peak at +75.0 pooled and in S01, which is exactly 15° from +90. The code's `<= 15` test counts that as within. The failure is on the −90 side and in the density at 0.
- **Cell 99 (Summary), fig4 row:** "S04 and S08 tied for the narrowest decrease". Cell 56 shows S07 and S09 narrowest at 2 bins, and S04 and S08 tied at 3 bins with four other subjects.
- **Cell 0 and the README:** "runs for about 40 minutes", with about 17 minutes for regression and about 9 minutes for variants. Cell 100 prints 63.5 min. The regression took 2052 s (cell 78) and the variants 620 + 365 s (cells 97–98).
- **Cell 38:** "S05 and S04, which move both arms most". This is only loosely supported. Cell 34 ranks S07's median bimanual ratio (0.308) above S05's (0.296).

I checked every other sentence of the conclusions, the Summary, the README table and the record's notes and findings against the printed outputs, and they match. This includes the 439 dropped events (237 + 125 + 1 + 75 + 1), the 11 significant day-effect pairs, the 21/24 and 20/24 variant results, and the variant ranges for seeds, log speed and bad electrodes.

The record's `verifications` states my round-1 reasons faithfully in its own words, with one omission: my problem 2 (the 86400 s timestamp mismatch) is not among the stated reasons. Only the author's response to fig2-event-counts mentions it.

### 3. Round-1 points

**Resolved:**
- 2: one mismatched event (S08 day 4), now dropped from reading (b).
- 4: the seed, log(onset speed + 1) and bad-electrode variants were run, with Delta R² and coefficients refit (cells 97–98).
- 5: the leakage from forward selection is disclosed.
- 6: the zero rows sit at the electrodes without positions, and shifting the rows lowers the fit in all 12 subjects (cells 7–8).
- 8: the density values are now printed.
- 9: the 0.5–4 s filter was run as a variant.
- 10: the grid-only variant was run.
- 7: stated as a deviation. It does not change any outcome.

**Remaining, bearing on a conclusion:**
- **Problem 1, now as an electrode-set question.** The per-subject reading was run, but the chosen set is the least consistent with the paper's 4.9 ± 4.9 removed electrodes. The outcome of fig5-recording-day-effects depends on it, as described in section 1.
- **Problem 3, partly open.** No electrode's power becomes non-finite, but every analysed event of S09 and S10 has runs of 50 ms or more of zeros on 1 to 15 good electrodes (cell 12). Their effect on band power is not measured.
  - This touches S09's fig4 part-1 failure and S10's HFB day effect (p = 0.054).
  - S09 is also the one subject where neither band differs between onset and pseudo-onset (cell 13), so its alignment of ECoG and events is not established.
- **Not run (criterion gap):** the fig5-recording-day-effects criterion asks for Table 2's per-day intervals for comparison. Cell 67 prints day means only.

### 4. Critical findings

The attempt record has no finding rated `critical`. I see none that should be: the one-event timestamp mismatch, the ECoG ending early, the unit and convention errors, and the depth-group count are all evident from the values or easy to work around.

S09's unconfirmed alignment (cell 13) would be critical only if a misalignment were shown, and nothing in the outputs shows one. Its current listing under checks that passed, noting that alignment could not be established for sub-09, is appropriate.
