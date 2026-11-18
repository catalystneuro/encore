I've worked through every point in the round-2 report. The entry re-ran cleanly from a fresh environment (`python tools/entry.py all entries/tingley-2018`: 0 errors, 53.7 min) and `check` passes. The re-run reproduced all the earlier numbers exactly, because the added null decodes use their own random stream. Nothing is committed.

**Outcomes.** None changed; the counts are still 8 reproduced, 9 partially reproduced, 12 not reproduced and 3 blocked. Two changes are written under `proposed` for round 3:
- **fig6-session-counts: partially reproduced → not reproduced.** I took the verifier's reason: the criterion has no partial rule, LS with CA1 is 25 or 33 against 63, and the 57 from flagged CA1 channels is only a variant. The notebook now prints that all three counts are within tolerance under neither reading. Counting every DT8 session would still give only 42 or 50.
- **fig1i-hpc-rate-phase-equivalent: not reproduced → reproduced.** The verifier said readings were chosen inconsistently between fig4d and fig1i. I now apply one rule to every claim and state it in the notebook header: a criterion counts as met if it holds under any one reading the claims file names, with undefined phase set to 0 and ties broken at random. That is the convention the claims file uses throughout. Under it, fig4d stays reproduced and fig1i passes under ab1 with rate map (b) (p = 0.066 and 0.82). The notes call it fragile, since the KS test finds a difference under 7 of the 8 readings.

**Outputs added**
- **Shifted-phase null for the 1.5 cm readings.** It now runs under ab1 and bb1 as well. In fig4d, the shifted phases under bb1 do not give the across-animal pattern (pooled r = −0.094, p = 0.48). They do reach the within-session majority, 28 of 47 sessions, so that part of fig4d is no stronger than chance.
- **fig1g, real against shifted phase information.** At 2 and 3 bins real phases carry 0.032 to 0.058 bits more than shifted ones (p from 0.013 down to 7.7e-05). That is a small part of the 0.68 to 0.72 bit excess over rate. The notes now say the phase-0 fill causes the match.
- **fig5g, the other decoder readings.** With the cosine phase only, assembly neurons are less negative, the opposite of the claim.
- **Two printed checks.** fig6 now prints the criterion check, and the speed cell prints its exclusion rule.

**Corrections**
- **Section 2 statements.** Every statement the verifier quoted is fixed:
  - README run time, now about 55 min.
  - Fit time: 1,274 s in the final run, about 0.72 CPU-s per pair. The round-1 response's "0.5 s per pair" was wrong.
  - fig4e-onset-mediolateral ranges: 0.074 to 0.740, and p = 0.13 to 0.68.
  - fig2fg: the hippocampal values are larger only at the condition level.
  - The finding on undefined phase: shifted phases beat rate in 0.026 to 0.060 of conditions, 3 to 6 times the nominal 1%.
  - fig6 shortfall: "part", not "much".
  - The speed threshold is now printed and quoted.
- **Decoder weakness.** Its numbers (rate MSE 6,329 against 6,733 for uniform guessing; 30 of 47 sessions) are now in the notes of each single-cell decoding claim.
- **fig5 cluster.** The notes for fig5g, figs5 and fig6e now say they were tested on assemblies that match neither the paper's fraction nor its timescale. The figs5 notes also call that absence fragile.
- **Bug fix.** I fixed a bug in the new fig6 check, which had used the session-reading CA3 count for both readings.
- **Round 2 record.** It is under `verifications`, with the verifier's reasons and my responses.

**Not done**
- **No shuffle-subtracted information and no minimum sample count (point B3).** The criterion fixes the information measure and the paper sets no minimum, so either would change the claim's method. The real-against-shifted comparison is shown instead.
- **No question added to `questions/tingley-2018.yaml`.** The verifier found no place where the claims file misreads the paper.
