**Round 2 verification: Mantas et al. 2024 on DANDI:001828 (0.261020.1002)**

**1. Outcomes**

The claims file has 38 claims, and the attempt record gives one outcome for each: 4 reproduced, 3 partially reproduced, 3 not reproduced and 28 blocked.

I agree with 37 of the 38. I disagree with one:

- **fig4b-speed-correlation-dcp (record: partially_reproduced; mine: not_reproduced).**
  - The criterion needs both groups to beat the shuffle at p < 0.05. The Anxa1 group fails in every reading (cell 47: t-test p = 0.080 and 0.071, Wilcoxon p = 0.0645).
  - Anxa1 is the subject of the claim. It gets weaker without mouse 687662, whose genotype conflicts between files (p = 0.21 and 0.18), and without the short recordings (p = 0.097 and 0.089).
  - For fig3e the record accepted that a claim is not reproduced when its main part fails. The same rule applies here. "Present but weaker" is a fair description of the effect's direction, not of a part that fails its test.

I now accept **fig6j-reaching-accuracy as partially_reproduced**, withdrawing my round-1 objection. The claim has three parts, and two hold under one reading of the main run: the interaction (p = 0.034), controls improving (p = 0.010) and TeTx below controls (p = 0.0014). Arch is below the controls on day 4 in all 8 main readings (cell 83), although never at Sidak p < 0.05.

**fig1b** stays blocked, with the reason given as "other". The record says the protocol does not allow data_missing for a claim whose data are held elsewhere. I can't check that rule, but the outcome is unchanged.

**2. Sentences the printed numbers do not support**

- **Cell 80 and the fig6c notes:** "raw speeds 2 to 6 times those of the tail base". The group means in cell 79 give ratios of 1.5 to 5.9. For example, controls on day 2 are 190.9 against 130.5, and on day 3 175.0 against 102.1. This is minor.
- **Cell 48 and the fig4b notes:** "Without the seven short recordings … dLight-dCP p = 0.059." That is only the permutation test. Against circular shifts the same cell prints p = 0.0499. This is minor, since the Anxa1 group decides the claim either way.
- **The fig4b notes and the response to problem 2:** "so speed and signal are aligned as run". This goes further than the outputs show:
  - Cell 11 shows that 19 of 160 kinematics files are not at lag 0 (one at 13 frames, one at 30), and it does not say whether any of them are photometry files.
  - Cell 9 shows the speed–signal correlation peaking within 0.5 s of zero lag in only 16 of 31 recordings.
  - Cell 10 itself says the clocks are "consistent … where it can be checked, not shown to share it in every recording".
- **README:** "It takes about five minutes". No total run time is printed. The printed load times add up to about 71 s, so I cannot check this.

Everything else checks against the printed outputs: every other "**Result:**" paragraph (cells 29, 33, 39, 42, 45, 51, 54, 57, 60, 63, 66, 69, 72, 75, 85), the Summary (cell 86), the README table and its counts (10 + 2 + 1 + 15 blocked claims), and the record's notes and findings.

The verifications block gives my round-1 reasons faithfully, in my own wording, with each problem and each "could not check" item attached to the right claim. The only omission is my for-information value for fig4f (R = −0.5713 against the −0.572 bound), which does not matter.

I found no new place where the claims file misreads the paper.

**3. Round-1 points**

Resolved:
- **1. Motif labels:** all ten motif claims are now blocked, and the analyses are marked as not deciding.
- **2. Start times:** they are printed, the labels are shown to sit about 18 frames early, and the analyses are run with the labels shifted.
- **3. fig3fg:** the notebook no longer picks a main reading.
- **5. Arch day-1 laser label:** now stated as a departure from the Methods.
- **6. Maze:** a pixel-scale check was added. It rests on tail-base occupancy, so it is weak but adequate. The lack of smoothing is now stated.
- **8. edgeR route:** documented.
- **9. Preferred limb:** reading (i) matches the claims file as written.
- **10. Recording counts:** reported against the legends.
- **11. The 2 s baseline:** the pre-train trace is flat.
- **From my "could not check" list:** the GEO file listing and the per-file object listing have both been added.

Still open, not affecting a conclusion:
- **4.** Mouse 687662's genotype is still unresolved. The new exclusion variants show fig3d is unaffected.
- **7.** The Sidak tests still use separate t-tests rather than Prism's pooled error term; this is stated.

Still open and bearing on a conclusion:
- **The fig4b-speed-correlation-dcp outcome disagreement** above.
- **fig4b alignment:** it is not shown which recordings fall among the 19 kinematics files that are off lag 0, and only 16 of 31 correlations peak near zero lag. This touches the weak Anxa1 correlation.
- **fig3d, fig3e and fig3fg:** whether a `correct` event's time is the drop-touch frame is still unchecked, because there is no video decoder. The only evidence is that the signal varies more around events than around random times, which cannot tell anything apart in sessions with 1 to 3 events.
