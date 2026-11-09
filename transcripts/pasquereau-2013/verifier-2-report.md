**Round 2 verification: Pasquereau & Turner 2013 on DANDI:001636 (draft)**

The claims file has 28 claims. The attempt record gives 28 outcomes: 4 reproduced, 3 partially reproduced, 3 not reproduced and 18 blocked (17 methods_underspecified, 1 data_missing).

**1. Outcomes**

I agree with all 28.

The one change from round 1 is `false-positive-rate`, where I had said not_reproduced and the record keeps blocked (methods_underspecified). I now accept blocked:
- The claims file's header (lines 31–35) treats a pseudo-onset rate outside 0.0033–0.03 as showing that "the procedures differ".
- Poisson spike trains give 0.16–0.19 with eight seeds (cell 40), against 0.23 observed (cell 38). So the excess comes from the detection as reconstructed here, and the test says nothing about the paper's own rate.
- I cannot see the protocol rule the author cites.
- The tension sits in the claims file: this claim's criterion only says when it is "Reproduced", which would otherwise default to not_reproduced. It is not a misreading of the paper.

The other 27 match round 1 and the current outputs:
- **cell-counts:** cell 25.
- **antidromic-latency:** cell 35, CSN p = 0.0190 against 0.0167 (False).
- **Kinematics:** cells 83 and 87.
- **EMG:** cells 93, 97 and 101.

I recomputed the baseline rates, torque-related fractions, earliest latencies and reciprocal-plus-unidirectional shares from the new per-cell table (cell 23). All match the notebook.

**2. Sentences the outputs do not support**

- **README, line 52:** "It took 5.2 min in the latest run (1.8 to 4.5 min in earlier runs)". Cell 111 prints "Notebook run time: 1.7 min".
- **Summary (cell 110) and README lines 37–39:** "compared at the same per-trial command step … the m2 response is smaller after MPTP, not larger". Cell 94 supports this only at one step (twice the smallest), and only with 66 against 11 channel-sessions. On triceps longus 2 at that step m2 is larger after MPTP (52.2 against 113.0, n = 4, p = 0.36). The attempt record's notes are qualified correctly; the summary and README are not.
- **Cell 95:** "so it does not rise simply with command size within a state". Cell 93 shows this holds before MPTP only (0.86, 41.85, then 17.09 with n = 5). After MPTP m2 rises with command size (1.81 → 194.4).
- **Cell 110:** "The header now marks the 16 claims blocked by the false-positive rate". Cell 0 marks 16 claims "run, blocked", but that count includes `false-positive-rate` itself, and cell 0's own text says 15 claims depend on it.
- **Cell 43, minor:**
  - "Both rates are more than 3 times the paper's" is true but understates the gap: 0.23 and 0.46 are about 23 and 46 times 0.01.
  - Its "cannot tell whether the paper's procedure differs" sits awkwardly next to the earlier "so the procedure here differs from the paper's".
- **Cell 43 and the record's notes, "14 cell-directions … can never respond":** true only for a baseline SD of exactly 0 (cell 22). Cell 23 shows near-silent cells with thresholds of about 0 that do respond. For example, v5801.1 has a baseline of 0.00, thresholds of 0.00, and an extension "response" at 30 ms. This adds to the detection's false positives, but every dependent claim is blocked, so no conclusion changes.

Every other "**Result:**" sentence, the rest of the Summary and README, and the record's notes match the printed outputs.

The record gives my round-1 reasons faithfully and in my own words, including problems 6–9 and the section C items. Its cell numbers are round-1 indices, which have since shifted (for example, round-1 cell 33 is now cell 38).

**3. Round-1 points**

Resolved:
- **Problem 1:** the cell 0 header now marks the dependent claims as run and blocked.
- **Problem 2:** cell 35 prints each antidromic test against its threshold.
- **Problem 4:** the filter is now run on synthetic movements (cell 88).
- **Problem 6:** the P/NP choice is recorded as a deviation.
- **Problem 7:** the approximate chi-square p is stated, and the threshold variants keep responses that last to the end of the window.
- **Section C, spike windows:** cell 42 shows every window lies inside its trial.
- **Section C, per-cell results:** cell 23 adds the per-cell table.
- **Section C, command size:** comparisons at the same per-trial step are added (cells 84, 88 and 94).

Addressed as far as the data allow:
- **Problem 3, the torque confound:** each conclusion and note now says the effect cannot be attributed to MPTP.
- **Problem 5, pre-MPTP noise crossings:** counts are printed and the cell 98 conclusion says many pre-MPTP responses are brief crossings of a small signal.

What remains that bears on a conclusion:
- `emg-m2-larger` is "reproduced" on the criterion, but it is not evidence of an MPTP effect. At the one comparable command step the pooled median goes the other way (cell 94). The record says this; the Summary and README overstate the reverse finding (item 2).
- The kinematic and EMG "not reproduced" outcomes carry the same confound. The record states it.

Not bearing on a conclusion:
- **Problem 8:** the claims file's reading of the detection rule, where the paper's Methods text reads closer to the t-test variant. Both readings are shown and both block.
- **Claims file header, line 23:** "no unit appears in two files" is no longer true of the draft. The attempt handles this as a deviation; it is not a misreading of the paper.
- **Still unchecked:** I could not check the claims file's expected values against the supplementary table, because no PDF reader is available here.
