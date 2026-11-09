**Prince et al. 2025 (DANDI:001371): verifier report, round 2**

The claims file has 52 claims and the attempt record gives an outcome for each: 21 reproduced, 5 partially reproduced, 7 not reproduced, 19 blocked (all `too_large`). Correction to my round-1 header: the round-1 table itself gave 6 partially reproduced and 7 not reproduced, not 7 and 6. Three outcomes changed since round 1:
- sfig3c-retrospective-unchanged: reproduced → not reproduced
- fig5d-stay-hpc-below-switch: partially reproduced → reproduced
- fig7c-hpc-commitment-initial-arm: not reproduced → reproduced

### 1. Outcomes

I agree with all 33 tested outcomes under each claim's criterion and the printed outputs. I also agree that the 19 choice-decoding claims are blocked.

- **Fragile outcomes.** Four outcomes turn on choices that are stated in the notes and in the claims file (S1 as amended, S5's code grid):
  - **sfig3c-retrospective-unchanged:** p = 0.036. It is 0.14 under the code's trial count and 0.12 on the round-1 grid. The paper's own p is 0.0513.
  - **sfig12-delay-hpc-no-outcome-difference:** p = 0.043, and 0.096 under the code's count.
  - **fig5d-stay-hpc-below-switch, new arm:** p = 0.0094, and 0.38 on the round-1 grid.
  - **fig7c-hpc-commitment-initial-arm:** p = 0.29, and 0.040 on the round-1 grid.
- **Assumptions.** No outcome in the attempt record is marked `assumed: true`. The choices the outcomes rest on (inclusion rule, time grid, how the arms are split into halves, the spread rule) are stated in the notes and deviations and are reasonable.
- **The 19 blocked claims.** I still think "too_large" is the wrong label for a limit on compute time. The author kept it under a protocol rule that I cannot check from here. The verification block records `agrees: true` for these claims, so my disagreement about the label appears only in the reason text. Blocked is right either way.

### 2. Sentences the printed numbers do not support

- **The LSTM timing is stale.** Cell 116 prints: first epoch 2.4 s, second 1.4 s; "8.2 min for this session", "8.3 h for all 66 sessions", "at best 2.1 h" on 4 cores.
  - Cell 117 says: "10.4 h for all 66 sessions in one process, at best 2.6 h on this machine's 4 cores".
  - The fig4a notes say: "2.8 s for the first epoch and 1.7 s for the second, 10.4 min for the session, and 10.4 h … at best 2.6 h".
  - The same 10.4 h / 2.6 h appears in every verification response for the LSTM claims.
  - The conclusion still holds, because 8.3 h and 2.1 h are both over the 60-minute limit.
- **The fig6e SVM timing is stale.** Cell 119 prints about 0.09 s per fit, "0.7 h for the real labels alone and 28 days with 1000 shuffles".
  - Cell 120 and the fig6e notes say "about 0.13 s per fit … about 1.0 h … about 41 days".
  - At 0.7 h, the real-label run of the CA1 half now fits within the limit. Only the 1000-shuffle permutation test is over it. The block still stands, because the PFC half needs the LSTM and the criterion judges both regions together.
- **The round-1 grid changes three outcomes, not four.**
  - Summary, cell 121: "it gives other outcomes for four claims (… and, under reading b, the second test of fig2g-pfc-no-goal-increase)".
  - The `methods_unavailable` finding: "the shift changes four outcomes".
  - On the round-1 grid, fig2g reading (a) still fails (p = 0.038 and 0.035, cell 100), so fig2g's outcome is not reproduced under both grids.
- **Cell 111:** "all … contrasts … give p < 1e-9 … with either phase and with the code's count of trials". Under the code's count, the new arm's second half gives p = 9.25e-9 (cell 110). The attempt record's "< 1e-8" is correct.
- **Cell 10:** "so the shortfall in each region is those unlabelled units". Only the total is shown to match: 633 = 347 + 286. How the 633 units split between the regions is not known.

Every other sentence I checked matches the printed outputs. That covers the remaining "**Result:**" conclusions, the rest of the Summary, the README and the attempt-record notes, including all the round-1-grid figures quoted against cell 100 and all the tolerance statements.

The attempt record states my round-1 reasons faithfully, mostly in my own words, with the relevant round-1 problems attached to each claim.

### 3. Round-1 points

**Resolved:**
1. **Spread rule:** the author checked the code at the pinned commit. The first-crossing variant gives PFC wider, 0.37 against 0.14 bins, so the outcome is the same under either rule.
2. **Unit regions:** they cannot be recovered. The five units tables have no electrodes column, and the `ch` value cannot tell the probes apart.
3. **fig6e CA1 half:** it was timed, and the block holds.
5. **Arm halves (sfig3ab):** the code's split is now used, with the split over bins that have a posterior as a variant. Three of the four contrasts hold under both.
6. **Time grid:** the code's grid with edges on the cue is now used, and the window bins are printed.
8. **Tuning-tiles bins:** resolved, as before.
9. **Seed:** each session now has its own seed.
10. **Validation bins:** a moving-bins-only variant was added and changes nothing.
11. **Theta phase disagreement:** explained by weak phase locking in that session.
12. **Claims-file points:** passed to a reader.

**Still open and bearing on a conclusion:**
- **Point 4 (LSTM block):** the label is still disputed, and the subset test was declined. This does not change any outcome.
- **Window averaging, a new point, not checkable here:** S7 of the claims file says "The code averages 0.5 s bins of the 0.2 s grid inside the window". `window_mean` takes a plain mean of the 8 bins, while 0.5 s sub-bins would weight them 3/2/3. Three outcomes rest on deciding p values between 0.036 and 0.044 (sfig3c-retrospective-unchanged, sfig12, the sfig3ab new-arm front half), so this weighting could move them.
- **Point 7 (Wald test and Tukey degrees of freedom instead of Kenward-Roger):** not addressed, because R is not available. The effect is probably small, but it now sits under those same borderline outcomes.
- **Text fixes:** the stale timing figures and the "four outcomes" wording in section 2.
