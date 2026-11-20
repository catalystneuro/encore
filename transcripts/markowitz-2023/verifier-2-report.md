**Verifier report, round 2: Markowitz et al. 2023 on DANDI:000559 (0.261113.1911)**

The claims file has 44 claims. The attempt record gives an outcome for all 44: 14 reproduced, 4 partially reproduced, 10 not reproduced and 16 blocked. Six outcomes are marked `assumed: true`: fig1f-syllable-vs-movement-onset, fig1f-dip-then-peak, fig1j, fig2g, ed7d and fig3i.

### 1. Outcomes

I agree with 41 of the 44 outcomes. I disagree with one, agree with one only partly, and agree with two only because their criteria say so (fig2k and ed10i, which section 3 reports as claims-file misreadings).

**Disagree**
- **fig1f-syllable-vs-movement-onset (reproduced).** I would say partially reproduced.
  - Reading (a) is z-scored against shuffles, and that z grows with the square root of the number of events. Cell 15 compares 23,122–43,107 syllable onsets per mouse with 696–1,553 initiations from stillness, about a 30-fold difference.
  - So syllable 2.25 against movement 1.17 can come from event count alone. With all detections (4-fold fewer events than syllable onsets), reading (a) favours movement (P = 0.004).
  - Under the criterion's own definition (all detections), reading (b) meets the rule and reading (a) is significant in the opposite direction.
  - The 25th-percentile stillness rule is stated, but it is not a reasonable basis for the outcome without a count-matched comparison, such as syllable onsets subsampled to the initiation count per mouse.

**Agree only in part**
- **ed10d (blocked, metadata_insufficient).** The direction of stimulation can be recovered from the data. In up sessions the stimulated instances sit above the target's 75th velocity percentile, and in down sessions below its 25th. The five dls-ai32jr mice, whose direction is unstated, may be the paper's five. The block is not settled until this is tried.

**Agree because the criterion says so**
- **fig2k (reproduced).** The outcome follows the criterion. The raw correlations, though, are negative (cell 52: −0.36 and −0.46 under reading (a)) and turn positive only against the destination-permuting null. See section 3.
- **ed10i (reproduced).** Correct on the criterion's two tests. The misreading from round 1 still stands (section 3).

**Agree, with notes**
- **ed3c (reproduced).** This follows the claim's criterion ("processed as in the fig_s03 notebook"). The claims file's own header, however, makes the Methods' fit with intercept the main reading and the no-intercept fit a variant. Under that rule the forelimb r of −0.026 misses. The outcome rests on this choice and should be marked `assumed`. In round 1 I wrongly listed the intercept as not affecting a conclusion.
- **fig2e-not-autocorrelation (partially reproduced).** The criterion has no partial case, so this outcome is a judgment. It should carry `assumed: true`.
- **fig3i (not reproduced).** The trial-matched assumption is stated and reasonable. Comparing stimulation minus catch between the two arms, which share the same 3:1 imbalance, would settle it with more power than discarding two-thirds of the stimulation trials.
- **fig1f-dip-then-peak (reproduced).** The criterion is met, but the maximum (1.67) falls at +1.0 s, the edge of the window the claims file assumed.

**All other outcomes: agree.** The other assumptions are stated and reasonable: fig1j's bound, fig2g's peak-against-peak reading, and ed7d's movement definition (its syllable half fails either way). The other blocks are justified as stated: fig1l too_large, fig2a and fig3c data_missing, and the rest not run.

### 2. Statements the numbers do not support

- **Photometry cell 33 and the record's fig2b-across notes:** "Over 166 experiments". The code-reading set is 164 (cell 3), and the record's deviation says this set was used. In cell 2, a dLight+ChrimsonR file with post-day session numbers that is an excitation session falls in `base_methods` but not in `pure_post`, so it enters `Ic`. That is probably where the 2 extra come from, and they would be the 2-s excitation sessions cell 3 says were left out. If so, every `Ic` analysis includes 2 stimulation sessions: fig1h (a), fig1j, fig2b, fig2i, fig2e, fig2h and fig2k. That is 2 of 166, so unlikely to change an outcome, but unverified.
- **Photometry cell 16 and the record's fig1f notes:** "the outcome rests on the stillness rule, the definition the Methods' description supports". Cell 15 does not separate the definition from the 30-fold difference in event count.
- **Photometry cell 0:** "fig3c-calibration, fig4i | blocked (data_missing)". The record has fig4i as `blocked_by: other`.
- **Photometry cell 66 (Summary):** "22 DLS and 92 DMS photometry-session files have behaviour but no photometry". Cell 3 gives 22 dLight-only plus 10 dLight+ChrimsonR DLS files. The record's finding has this right.
- **README:** "About 30 minutes". The photometry notebook ran from 00:09 to 00:54, about 45 minutes.
- **README:** "The food-reward and calibration sessions are not in the dandiset … were not run within the time". This omits ed10d, which is blocked for insufficient metadata.
- **Photometry cell 49 and the record:** "The overlap of the windows does not explain them". The z values support this (4.78 and 5.07), but with 200 shuffles the neighbours' Holm P is 0.05, the floor of that test (cell 48). Minor.

All other sentences of the conclusions, the Summaries and the record's notes match the printed outputs.

The attempt record states my round-1 reasons accurately and in my own words for all 44 claims.

### 3. Round-1 points

**Resolved**
- 1, clock: the per-mouse check gives a best shift of −3 samples in 19 of 22 mice across all groups.
- 3, fig2h overlap.
- 4, fig2g null.
- 5, experiment set: counts at each step and quality control (b) are now shown, apart from the 166 above.
- 6 and 12, fig1e.
- 7, Monday-baseline variant and learner overlap.
- 9, fig3i: addressed, outcome changed.
- 10, `jsd`.
- 11, 13, 14 and 15.
- Keypoint alignment, fig3m light timing and trial counts, ed10i coordinate ranges, and the blocked reasons.
- fig2k is now tested, and fig4i's `blocked_by` was corrected.

**Partly resolved**
- 2, movement onsets. Diagnostics were added, but the event-count confound described in section 1 is new.

**Remaining points that bear on a conclusion**
1. **fig1f.** Event count drives the shuffle-z comparison. The outcome needs a count-matched test.
2. **fig2k: claims-file misreading.** The Methods z-score against "Pearson coefficients estimated after shuffling dLight peak values". The criterion uses the code's destination-permuting null, which goes against its own rule that the Methods give the main reading. Neither null was run as a variant. With raw r negative, the Methods' null could reverse the outcome.
3. **ed3c: claims-file inconsistency.** The header rule and the claim's criterion name different fits, and the two fits give different outcomes.
4. **ed10i: claims-file misreading (round-1 point 8).** The criterion reads the paper's "experiment-wide" statistic (n = 32 mice) as target-onset JSD per mouse. The notebook's experiment-wide test gives P = 0.005, with Opto-DA lower than controls.
5. **fig2e-not-autocorrelation: criterion gap (point 16).** The criterion has no case for an autocorrelation that turns significantly negative, and n ≥ 10 syllables cannot resolve "a few hundred milliseconds".
6. **Within-DLS group split.** It is not a clock problem, but it is unexplained. Cell 15 gives syllable-onset peaks of −4.28 to 2.73 in dLight+ChrimsonR mice against 2.73 to 5.02 in dLight-only mice. This bears on fig1f reading (b) and the syllable half of ed7d.
7. **ed10d.** Recover the stimulation direction from stimulated-instance velocities before keeping the block.
8. **The 2 extra experiments** in the `Ic` analyses (section 2).
