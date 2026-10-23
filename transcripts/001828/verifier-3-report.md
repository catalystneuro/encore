# Round 3 verification: Mantas et al. 2024 on DANDI:001828 (0.261020.1002)

The attempt record proposes a change of outcome for one claim only, `fig4b-speed-correlation-dcp`. No other outcome has a `proposed` entry.

| Claim id | Proposed outcome | Agree? | My outcome if different | Reason |
|---|---|---|---|---|
| fig4b-speed-correlation-dcp | not_reproduced (currently partially_reproduced) | Agree | — | See below. |

**Reason, fig4b-speed-correlation-dcp**

- **What the criterion asks.** The claims file says the claim is reproduced when, under one reading, both Anxa1 GCaMP-dCP and dLight-dCP have a mean correlation above 0 and above the shuffle at p < 0.05. It gives no condition for a partial result. The claim's subject is Anxa1 axonal activity; the dLight-dCP part is the "similar correlation" that follows it.
- **The numbers come from the data (cell 47).**
  - Each recording's Pearson r between the dandiset's 30 Hz z-scored trace and `linear_velocity` is printed. It is compared with the mean of 100 permutations and of 100 circular shifts.
  - **Anxa1:** 10 recordings from 8 mice, mean r = 0.0657, 9 of 10 positive. The paired t-test gives p = 0.0803 against permutation and 0.0713 against circular shifts; Wilcoxon gives 0.0645 against both.
  - **dLight-dCP:** mean r = 0.0673, t-test p = 0.0101 and 0.0080. This part passes.
- **Every variant leaves Anxa1 above 0.05 (cell 47).**
  - Without the short recordings: p = 0.0972 and 0.0893 (Wilcoxon 0.0977).
  - Without mouse 687662: p = 0.2057 and 0.1838 (Wilcoxon 0.1484).
  - With speed moved by the kinematics lag: p = 0.0820 and 0.0733 (Wilcoxon 0.0645). Cell 11 identifies the five photometry files this moves: Anxa1 687642 by 5 frames and 816510 by 1, dLight-dCP 776769 by 1 and 829248 by 30, and dLight-cCP 842388 by 1.
  - So the range the reason gives, "p = 0.064 to 0.21", matches these outputs.
- **No choice was made to reach the result.**
  - The proposal goes against the author's own earlier, more favourable outcome.
  - The shuffle, time base and speed follow the readings the claims file names.
  - The one recording that pulls Anxa1 down (842430, r = −0.174, cell 47) is kept. That is right: nothing in the data justifies dropping it, since its photometry starts at the expected point (cell 11) and its peak correlation lies within 0.8 s of zero lag (cell 9).
- **Clock alignment is a caveat, not a reason to keep the partial outcome.**
  - Cell 9 shows the Anxa1 speed–signal correlation peaks within 0.5 s of zero lag in only 5 of 10 recordings. Cells 10 and 48 say this openly.
  - This leaves open that some recordings are misaligned. It does not supply a reading under which Anxa1 passes, and the criterion is judged on the analysis as specified.
- **Why not partially reproduced.** The part that fails in every reading is the claim's main part, so the result is not partial. This is the same rule the record already applies to fig3e, whose dCP part fails in every reading and which is not reproduced. Cell 48 states this reasoning, and it is the reason I gave in rounds 1 and 2.
- **Prose matches the outputs.** The sentences in cell 48 and in the record's notes agree with the printed numbers, including the dLight-dCP values without the short recordings (0.059 and 0.0499) and the lag-moved values (0.028 and 0.023). One small omission: after the lag move, dLight-dCP is 6 of 8 positive with Wilcoxon p = 0.0547 against permutation (cell 47). The notes don't mention this, and it doesn't affect the outcome.

I found no new place where the claims file misreads the paper.
