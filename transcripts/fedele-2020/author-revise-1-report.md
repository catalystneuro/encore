I've revised the attempt for every point in the verifier's report and re-run it. `python tools/entry.py all entries/000576-fedele-2020` ran cleanly in 5.7 minutes, its outputs match a scratch run exactly, and `check` reports 0 errors. Every outcome now matches the verifier's, and round 1 is recorded under `verifications`: the verifier agreed with 20 of the 25 outcomes of the first record.

**Outcomes that changed**
| Claim | Before | Now | Why |
|---|---|---|---|
| nsoz-delta-hgp-mi-inverse | reproduced | not reproduced | r is negative in only 2 of the 3 readings that define the MIs |
| table2-delta-reduced-12-of-14 | reproduced | partially reproduced | z-scoring over the whole trial gives 10 negative, below the 11 to 13 range |
| fig1f-hgp-more-specific-than-delta | reproduced | blocked (methods underspecified) | HGP is more specific under two z-scorings and tied under the third |
| fig3b-firing-hgp-no-condition-difference | reproduced | partially reproduced | at 1.5 s and 15 s over concatenated blocks NEUTRAL is still higher (p 0.012, 0.023) |
| fig4b-regression-firing-hgp | partially reproduced | not reproduced | the FRV coefficient is never significant, and the claim needs both FRV and SSI |

**What I corrected**
- **Readings (problems 1 and 6):** outcomes are now judged on all three z-scorings the claims file lists. The baseline z-scoring I had adopted for several outcomes, and the extra `trialsd` reading, no longer decide anything. For other-bands-no-effect the basis is now the verifier's own argument: every reading that shows the paper's delta effect also shows a cluster in another band.
- **Baseline SD (problem 2):** I added a variant that pools the baseline SD over all trials of an amygdala, and the notebook now prints how few independent values the per-trial SD rests on. With the pooled SD, the alpha cluster in the 7 amygdalae outside the SOZ goes away. That is stated in the notes but does not change the outcome.
- **MI windows (problem 3):** where a window reading finds no cluster, the MI is now undefined instead of 0. The fixed windows stay as a reading taken from the paper, with the passages cited.
- **fig3b smoothing (problem 5):** in the concatenated readings each block is now smoothed on its own. The old form is kept as a variant to show that the mixing strengthened the difference but does not explain it.
- **Microwire identity (problem 4):** the units table has no microwire column, and the notebook now prints this. I added an SSI variant that drops pairs likely recorded on one wire, judged from spikes that never coincide within 1 ms. It flags only 4 of 116 testable pairs and changes nothing.

**Outputs the verifier asked for**
- Each amygdala's AVERSIVE minus NEUTRAL difference in 2 s bins, for delta and HGP.
- Per-unit firing rates and a population PSTH, beside the data descriptor's 1.66 Hz.
- MIs under re-mapped patient numbers (subjects 2 and 7 swapped, and 7 as patients 5 and 8). Neither re-mapping brings them clearly closer to Table 2.
- Other binomial intervals beside the Clopper-Pearson one.
- The two other baselines of Methods 4.8. With z-scoring over the amygdala, the previous-epoch baseline gives an HGP cluster from 0.6 s. The previous epoch is always a block of the other condition, and the claims file lists these baselines as variants, so fig1c stays not reproduced; this is recorded in its notes and in the question to the authors.

**Questions and findings**
- I created `questions/000576.yaml` with two questions for a reader. One asks which binomial interval the paper used (point 8). The other notes that the paper's own Table 2 values fail the "not DELTA" half of fig1e (point 12).
- Findings updated: subject 2's file holds the same subject metadata as subject 7's (age 39, gliosis, same sides). The questions to the authors are revised to the new numbers.
- README, notebook summary and conclusions are rewritten to match; the runtime is now given as 6 minutes.

**What I did not change, and why**
- **Point 9 (the 1 s smoothing leaks 0 to 0.5 s into the baseline):** the verifier marked it as not affecting a conclusion, and the readings fig1c fails under are far from threshold.
- **Point 10 (weak spike and iEEG clock check):** also marked as not affecting a conclusion; the firing claims use trial times from the same file.

I did not commit anything; the workflow does that. The untracked dotfiles and `scripts/` directory in the checkout were already there and are not mine.
