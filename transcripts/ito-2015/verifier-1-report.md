**Verifier report, round 1: Ito & Doya (2015) on DANDI:001642 (0.260205.0153)**

The claims file has 32 claims and the notebook analyses all 32. My outcomes: 11 reproduced, 8 not reproduced, 13 blocked.

Where a claim's readings disagree, I applied the claims file's rule: such a claim is blocked as methods_underspecified. I also counted the notebook's two unit sets as readings: the dandiset's own `PANs` flag ("deposited") and units selected by the paper's Methods rule ("Methods-rule"). Neither set matches the paper's counts.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| trial-counts | reproduced | Reading (b), 86 sessions with units (cell 8): 75,348 trials, 12,639 / 22,695 / 36,496 / 3,518 by block type, 7 rats. Every count is within 10%. |
| trials-per-block | reproduced | Readings (a), (b) and (c) put all six values within tolerance (cell 10); under (a) the means are 22.50, 47.15 and 41.05. |
| fig2c-extinction-differs | reproduced | All six χ² tests give p < 1e-15 (both readings, with and without Yates), and the fixed tones are further from 0.5 than the choice tone (cell 12). |
| fig2b-extinction-time-course | reproduced | With both Wilson and Clopper-Pearson intervals, the choice tone at trial 2 is closer to 0.5 than at trial 1 (0.815→0.551 and 0.175→0.379). At trial 5 the left-tone interval is above 0.5 and the right-tone interval below it (cell 14). |
| fig2d-f-decision-trees | reproduced | Every reading holds (cell 16). P(L\|L1)=0.80 against P(L\|R1)=0.18. The lowest left-tone branch is 0.70 and the highest right-tone branch 0.25. |
| fig2g-fq-variable-best | not_reproduced | Under both splits Markov 4 beats FQ variable (0.5785 vs 0.5758 and 0.5797 vs 0.5762), and so does DFQ variable. In the random split the Wilcoxon test against Markov 4 gives p = 0.004 (cell 19). |
| actor-critic-near-chance | reproduced | All four fits give 0.500 to 0.503, inside 0.508 ± 0.051 (cell 20). See problem 8 on how little this test can show. |
| neuron-counts | blocked (data_missing) | Stability conditions (1), (2) and (5) need waveforms or histology. The archive metadata lists only ElectrodeGroup, Units and ProcessingModule (542 MB for 87 files). The parts that can be tested do not match: all units 297/255/215; deposited flag 204/112/138, with VS out of tolerance; Methods-rule PANs 183/147/119, with DMS out of tolerance (cell 22). |
| fig4b-vs-phase1 | reproduced | Holds in all 48 readings. The VS proportion is 0.64 to 0.77, and p ≤ 0.02 against both other regions (cell 27). |
| fig4b-dms-phase5 | blocked (methods_underspecified) | Holds in only 2 of 48 readings: the deposited set, no extinction, 30 ms smoothing, "any bin", which is exactly the reading the notebook adopts. Under "first crossing" the DMS proportion is about 0.2 (cell 28). |
| fig4b-vs-phase7 | blocked (methods_underspecified) | Holds in all "any bin" readings (24/24) and fails in all "first crossing" readings (0/24) (cell 29). |
| fig4c-activation-duration | blocked (methods_underspecified) | The order VS > DMS > DLS and both VS tests hold everywhere. DLS vs DMS gives p = 0.054 to 0.082 in the deposited set and 0.018 to 0.10 in the Methods-rule set, so 4 of 12 readings hold (cell 30). |
| fig5b-state-info-vs | blocked (methods_underspecified) | Reading (a), the Phase 1 mean, holds in 10 of 12. Reading (b), per bin, fails in all 12, with only 8 to 13 of 20 bins holding (cell 35). |
| fig5e-action-info-rises-dls | not_reproduced | In every reading, DMS and VS are above threshold in 14 to 15 of the 15 Phase 3 bins (cell 37). |
| fig5e-action-info-cue-offset-dls | not_reproduced | Under the claims file's readings O1 (a) and (b), DLS vs DMS gives p = 0.06 to 0.31 and the claim fails 8 of 8. It holds only under the notebook's added O1 (c) on the deposited set (cell 39). |
| fig5e-action-info-center-exit | reproduced | All 12 readings order DMS > DLS > VS, with DMS–VS and DLS–VS at p ≤ 0.0008 (cell 41). |
| fig5d-action-info-phase5-dms | reproduced | All 24 readings hold, with DMS against DLS at p ≤ 0.0003 (cell 43). |
| fig5g-reward-info | not_reproduced | Part (1) fails in every reading if read as the claims file words it: each region's first threshold crossing is in Phase 1 or 2 ("first phase overall", cell 45). Part (2) holds only for the VS-peak bin in the deposited set. |
| fig6-event-coding-proportions | blocked (methods_underspecified) | Holds in 8 of 8 Methods-rule readings but only 3 of 8 deposited readings. In the deposited set the state window (a) makes DMS largest, and all+ext on the EASH axis makes AC largest in DMS (cell 48). |
| fig6-above-chance | reproduced | All 120 binomial tests give p < 0.01 against chance 0.01, which is the claims file's chance level. The smallest proportion is 13/138 (cell 49). |
| fig6bc-similar-fixed-free | blocked (methods_underspecified) | AC's largest region differs between fixed and free blocks (DMS against DLS) in the deposited set, and is the same in the Methods-rule set (cell 50). |
| fig8a-d-action-reward-coding | blocked (methods_underspecified) | Holds in 6 of 8 readings. Under free-choice trials with events E0–E6, DMS r(t-1) in Phase 7 is 4/112, p = 0.027 (cell 53). |
| fig8e-action-value-dms | blocked (methods_underspecified) | Holds only under free-choice trials on the EASH axis, 2 of 8 readings (cell 54). |
| fig8e-qr-dms | blocked (methods_underspecified) | Holds in 6 of 8 readings and fails in the two (free-choice trials, EASH axis) readings (cell 55). |
| fig8f-state-value-vs | not_reproduced | The test in the first half of Phase 4 fails in all 8 readings: VS vs DMS gives p = 0.12 to 0.76 (cell 56). |
| no-policy-coding | reproduced | No region or window reaches p < 0.01 in any reading. The largest proportion is 3.6% (cell 57). |
| fig9-temporal-order-all-blocks | not_reproduced | Part (1) fails in all 12 readings. For example, in DF blocks DLS, DMS and VS all rise in Phase 3 under combination (a) (cell 60). |
| fig9-dms-never-above-dls | blocked (methods_underspecified) | 1 of 96 tests is significant: deposited set, combination b, O1 b, SF, E4, p = 0.019. The other readings show none (cell 61). |
| fig10a-dls-fixed-above-free | not_reproduced | The window test passes in some readings, but the order SF/DF→FH→FL together with "FL peak lowest" fails in all 12 (cell 64). |
| fig10b-dms-fixed-above-free | not_reproduced | The E3 window is never significant, so no reading holds (cell 65). |
| fig10c-vs-no-fixed-free-difference | blocked (methods_underspecified) | Deposited set with combination (b): Wilcoxon p < 0.05 at E3. Every other reading shows no difference (cell 66). I agree with the notebook. The data are present, so the block comes from the method, not the archive. |
| fig10d-dls-stay-above-switch | blocked (methods_underspecified) | Holds in 5 of 12 readings. With O1 (a), uncorrected, it fails: switch has fewer trials and so more plug-in bias (cell 69). |

### B. Problems

1. **[affects a conclusion]** Cells 0 and 27–29 (`ADOPT`). The notebook marks one adopted reading and its header says only two claims end blocked. By the claims file's every-reading rule, 11 more claims have readings that disagree (the blocked rows above). fig4b-dms-phase5 holds only under the adopted reading.
2. **[affects a conclusion]** Cells 23–24 and 52, unit set. The claims file defines a PAN by the Methods rule, but the notebook's main set is the deposited `PANs` flag. The regression (cell 52) runs only on the deposited set. Which set is used decides fig4c, fig6-event-coding, fig6bc, fig9-dms-never-above-dls, fig10c and fig10d.
3. **[affects a conclusion]** Cell 31 / `mi_bits(pt=True)`. O1 reading (c), the Panzeri-Treves correction, is the author's addition; the claims file gives only (a) and (b). It is the only reading under which fig5e-action-info-cue-offset-dls holds.
4. **[affects a conclusion]** Cell 45. The criterion says the region average "first exceeds its shuffle threshold after E5". The code tests the first crossing at or after E5, which is almost certain to pass. Read as the claims file words it, part (1) fails in every reading, so the outcome is not_reproduced rather than blocked.
5. **[affects a conclusion; a caveat on the method, not a code bug]** `mi_with_shuffles` / `threshold`. Permuting labels across all trials ignores slow drift and block structure. As a result, action MI crosses threshold before the cue in all regions (cell 37: DLS 15 and DMS 12 of 27 Phase 1–2 bins), and reward MI crosses before E5 (cell 33). The margins are tiny (0.002–0.015 bits/s). This is the paper's own method, but these crossings decide fig5e-action-info-rises-dls, fig5g part (1) and the first crossings in fig9.
6. **[does not affect a conclusion]** Cells 18–19, fig2g. Several choices are the author's own:
   - The particle-filter priors are fixed (alpha U(0,1), kappa U(0,5)).
   - The sigma grid is coarse (3×3).
   - Each model gets a single stochastic particle-filter run.
   - The test set is 43 sessions, against the paper's 101.

   The margin is only 0.003, but DFQ variable and Markov 4 both beat FQ variable in both splits, so the conclusion stands.
7. **[does not affect a conclusion]** Cell 64. The fig10a order uses the sustained rise, whereas the criterion says "crosses threshold first". With first crossings the outcome is the same.
8. **[does not affect a conclusion]** Cells 18 and 20, actor-critic. The fits land on boundary values ([0, 0] gives exactly 0.5000; [1, 0, 0] likewise). On synthetic data generated by an FQ agent, where FQ scores 0.756, `ac_loglik` gives 0.506 when fitted and 0.5125 on a grid. So this model form sits near chance anyway. The tolerance band contains 0.5, so the test has little power.
9. **[does not affect a conclusion]** Cell 33. The comment says the shifted labels are the next trial's reward, but `np.roll(y, 1)` gives the previous trial's reward.
10. **[does not affect a conclusion]** Cell 32. The 100 ms bins are not aligned to the events; for example, the bin from 2.70 to 2.80 s straddles E2 and is counted as Phase 3.
11. **[does not affect a conclusion]** Cell 22. The duplicate check drops the later unit of each pair, without the PETH-similarity part. Condition (4) reading (ii) removes almost every unit, which makes it an implausible reading; it is shown but nothing depends on it.
12. **[does not affect a conclusion]** Synthetic checks: `mi_bits` matches a hand-computed plug-in MI, the bias correction removes the null bias, and `threshold` returns the second-largest value. All behave correctly.
13. **Claims-file readings to report, not correct:**
    - The fig4b reading (b), "first crossing falls in the phase", is not supported by the Fig. 4B legend ("normalized EASHs … reached 0.5 during each trial phase"). It alone blocks fig4b-vs-phase7.
    - fig9-dms-never-above-dls counts any uncorrected p < 0.05 across 8 tests per reading. A single chance hit then blocks the claim.
    - no-policy-coding uses 0.01 as the chance level for a joint event. The claims file already flags this.

### C. Not checked, and what would have settled it

- **Waveforms in the NWB files.** I could not confirm whether the units tables hold waveforms; I saw only the API metadata, not the files. A printout of the units-table columns or the NWB groups in cell 2 would settle neuron-counts as blocked or not reproduced.
- **Unit set in the regression.** Fig. 8 was not run on the Methods-rule set. Running `regress_all` on `SETS["Methods-rule PANs"]` would show whether the Fig. 8 outcomes depend on the unit set.
- **Particle-filter variability.** Repeated particle-filter runs with other seeds, and a finer sigma grid, would show how stable the fig2g gap of 0.003 is.
- **Threshold behaviour.** A shuffle null that keeps block structure (permuting within blocks), shown alongside, would show whether the crossings before the cue and before the reward drive fig5e-action-info-rises-dls, fig5g and fig9.
