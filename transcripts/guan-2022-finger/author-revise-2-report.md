I made all the round-2 corrections. No outcome changed and I proposed no changes, so a third round isn't needed. I re-ran `python tools/entry.py all entries/000252-guan-2022`: 0 check errors, and the notebook ran without error in 661 s. Every number came out the same as before.

**Outcomes:** all 19 stay as the verifier agreed: 11 tested, 8 blocked as `data_missing`. The two `assumed: true` outcomes (fig8b-matching-closer reproduced, jppc-finger-ccgp-low partially reproduced) are kept with their questions for the authors.

**Corrected or added:**
- **tenfinger-decoding-accuracy:** the shuffled-label range in the record now reads 0.04 to 0.17, as cell 7 prints.
- **tenfinger-discriminative-fraction:** "FDR per session gives no more" is replaced in the Result cell and the record. The new text says per-session FDR gives at most 0.3 points more than pooled FDR (40.7 against 40.4, 38.4 against 38.1).
- **Per-participant BH correction:** the verifier noted that the claims file corrects each of J's two arrays separately, while the Methods correct "for m = N … neurons for each participant". This is now a question for a reader in the new file `questions/000252.yaml`. The claim is unchanged, and the question notes that even uncorrected p fails for J-PPC.
- **jppc-finger-ccgp-low:** the record no longer calls the pseudo-population "the better-supported choice". It now calls it a judgement call, with the reasons in the deviation.
- **Cell 21:** it now prints the off-diagonal RDM range (0.57 to 3.90), matching the text.
- **DANDI:000147:** a new code cell prints its name, description, related resources and file list from the archive. It shows 10 files of subject P1 from 2018, a BCI finger-press task and an IsDescribedBy link to eLife.74478.
  - The notes for fig6-online-bmi and the Summary now say only what that cell prints.
  - The paper's text has no reference list, so they link the dandiset to ref 46 through the paper's own description of the task: the Methods figure "adapted from [46]", with feedback 1.5 s after the cue.
- **Run time:** the README now says about eleven minutes and `entry.yaml` has `runtime_minutes: 11`, from the measured run (the notebook prints 10.9 min).
- **Record:** round 2 is added under `verifications`, with the verifier's reasons and my response for each of the 19 claims.

**Not done:**
- The README run-time point applies to no single claim, so it is fixed but has no entry under `verifications`.
- The executed copy was built before my last markdown-only edits (Summary wording). The code and outputs are unchanged by them.
- Nothing is committed, as instructed.
