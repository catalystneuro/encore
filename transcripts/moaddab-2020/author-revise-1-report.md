I answered every point in the round-1 report. No outcome changed, and the verifier's disagreement on fig6 is recorded. `entry.py all` passes with 0 errors (the notebook runs in 42 s), and the handover is rebuilt. Nothing is committed.

**Outcomes**
- All 20 outcomes are unchanged. The verifier agreed with 19.
- fig6 stays partially reproduced. The verifier would give reproduced, because the authors' script's normalization reproduces the paper's numbers. I kept the Methods' normalization as the deciding one: the Methods Z-score the trial-averaged firing, the claims file follows them, and the protocol says the Methods decide when they disagree with the code. The disagreement is in the fig6 notes and under `verifications`.

**Added or corrected**
- **B1, script normalization:** now run as a full variant under all 12 regression readings for fig6, figs5, fig7 and figs6.
  - fig6 passes under 9 of 12.
  - fig7 still fails the uncertainty part under all 12.
  - figs6 passes under all 12.
  - figs5 has one-tailed p < 0.05 in 6 of 12 readings, but not under the adopted one (p = 0.059).
  - Under the Methods' normalization, fig6's safety part also fails. I added this to its notes.
- **B2, one rule for choosing the reading:** stated once in the notebook and the summary. Every regression claim is judged under the script's combination (cube Z score, 0/0 trials set to 1). Each claim also reports the outcome under the claims file's own rule. A new table compares all 12 combinations with the paper's printed statistics. The script's combination is closest (mean relative deviation 0.076, next best 0.167, the claims file's own readings 0.236 to 0.724).
- **B3, bregma:** the script never mentions bregma, and the notebook now prints this. The bregma parts of fig4ab and fig4de stay untestable.
- **B4, smaller neuron counts:** I printed the counts the verifier asked for.
  - 24 of the 81 cue-excited neurons come from sessions with 0/0 trials.
  - No beta is missing, and every cue-excited design is of full rank.
  - The script has no exclusion step.
  - None of these gives the paper's 67 or 68 cue-excited neurons, so the question stays open for the authors.
- **B5, session count:** no session holds two behaviour programs and no two share a trial table, so the 3 extra sessions are not duplicates. The difference is still unexplained.
- **New finding on Fig. 7:** the script computes cue-inhibited firing only over the first 5 s and the whole cue. With first-5 s firing and the script's normalization, the paper's Fig. 7 statistics come out closely; for example Control uncertainty R² is 0.042 (p = 0.16) against the paper's 0.04 (p = 0.16), and safety Z is 0.60 against 0.60. The legend says last 5 s, so fig7 stays not reproduced. This is recorded as a `code_mismatch` finding, and the open question to the authors about Fig. 7 now asks about the window.
- Notes in the attempt record, the README and the summary now match the new numbers. Round 1 is recorded under `verifications`.

**Not done**
- I filed no question in `questions/crcns-pag-2.yaml`. The verifier described the normalization issue as a gap in the claims file, not a misreading, and I agree that the claims file follows the Methods.
