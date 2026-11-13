No claim changed, because the reader answered no questions.

**Why there were no answers.** `questions/strickland-2022.yaml` does not exist, and the reader's answer run stopped without changing anything (`transcripts/strickland-2022/answer-report.md`). The reader stopped because of a sentence in the attempt record: the notes on two claims said "The question is in the findings". That read like questions for a reader that had never been filed. They were questions for the paper's authors, about method details the paper leaves open:

- **fig2f-cue-hubs:** whether the averaged coefficient is r or r squared, and whether it uses danger firing only or all three cues. This is filed as a `paper_inconsistency` finding.
- **fig4b-phasic-network and fig4b-tonic-network:** the criterion says "Pearson correlation", and the Methods call it "Pearson's correlation coefficient (R2)". This is filed as a `methods_unavailable` finding.

The record handled both under step 1.6 as assumptions marked `assumed: true`, and the notebook shows the r variant. Neither is a case where the claims file misreads the paper, so there was nothing to put to a reader and the claims file was correctly left alone.

**What I changed.** I only reworded those two notes in `attempts/strickland-2022-01.yaml`. They now say the question is for the paper's authors and is in the findings, and the fig4b note adds that no question was put to a reader. The notebook, helper and README are unchanged.

**Outcomes per claim (unchanged):**
- fig2f-cue-hubs: partially reproduced (assumed), as before.
- fig4b-phasic-network: reproduced (assumed), as before.
- fig4b-tonic-network: reproduced (assumed), as before.
- All other claims are as they were.

**Entry steps:**
- `lock` rewrote the lock file with no change.
- `all` passed with 0 errors. It reused the executed notebook from 01:48 UTC (99 s run) because nothing the run reads had changed, so nothing was executed again.
- `handover` rebuilt `executed/strickland-2022/handover/`.

I did not verify the work, commit or push.

If someone thinks the r versus r squared wording in the fig4b criteria is a misreading of the paper, that would be a new reader question; I don't think it is one.
